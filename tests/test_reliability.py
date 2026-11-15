"""Original fictional controls for deterministic checks and explicit abstention."""
from copy import deepcopy
import decimal
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

from court_integrity.engine import InputError, check_submission
from court_integrity.intake import prepare_package
from court_integrity.__main__ import load_package
from examples.make_examples import matched_package


def context_snapshot(context):
    return (context.prec, context.rounding, context.Emin, context.Emax,
            context.capitals, context.clamp, dict(context.flags), dict(context.traps))


def arithmetic_package(components, total):
    package = matched_package()
    package['arithmetic'][0].update(components=components, total=total)
    return package


def fictional_document(tail):
    text = '[2099] SGHC 900001 ' + tail
    raw = text.encode('utf-8')
    return {'input_name': 'fictional.txt', 'input_file_sha256': hashlib.sha256(raw).hexdigest(),
            'input_bytes': len(raw), 'format': 'txt', 'parser': {'name': 'fixture', 'version': '1'},
            'extraction_status': 'UNVERIFIED_TRANSCRIPTION', 'notes': [],
            'segments': [{'id': 'B0001', 'text': text, 'origin': {'kind': 'test-fixture'}}]}


class ArithmeticContextTests(unittest.TestCase):
    def test_report_is_identical_under_altered_caller_contexts(self):
        packages = [arithmetic_package(['1000', '1000'], '2000'),
                    arithmetic_package(['1000'], '0'),
                    arithmetic_package(['0.00000001'], '0'),
                    arithmetic_package(['1', '-1'], '1'),
                    arithmetic_package(['999999999999999999.99999999'] * 1000, '0')]
        expected = [check_submission(p) for p in packages]
        mutations = [({'prec': 1}, {}), ({'Emax': 2}, {decimal.Overflow: True}),
                     ({'Emax': 2}, {decimal.Overflow: False}),
                     ({'Emin': 0}, {decimal.Subnormal: True}),
                     ({'Emin': 0}, {decimal.Underflow: True}),
                     ({'Emin': 0, 'Emax': 2}, {decimal.Inexact: True, decimal.Rounded: True}),
                     ({'rounding': decimal.ROUND_FLOOR}, {}),
                     ({'rounding': decimal.ROUND_UP}, {}),
                     ({'capitals': 0}, {}),
                     ({'clamp': 1, 'Emax': 5}, {decimal.Clamped: False}),
                     ({'clamp': 1, 'Emax': 5}, {decimal.Clamped: True})]
        for settings, traps in mutations:
            with self.subTest(settings=settings, traps=traps), decimal.localcontext() as caller:
                for name, value in settings.items():
                    setattr(caller, name, value)
                caller.traps.update(traps)
                caller.flags[decimal.Inexact] = True
                before = context_snapshot(caller)
                for package, report in zip(packages, expected):
                    original = deepcopy(package)
                    self.assertEqual(check_submission(package), report)
                    self.assertEqual(package, original)
                    self.assertEqual(context_snapshot(caller), before)

    def test_mutated_default_context_does_not_change_report(self):
        package = arithmetic_package(['0.00000001'], '0')
        expected = check_submission(package)
        saved = decimal.DefaultContext.copy()
        try:
            decimal.DefaultContext.prec = 1
            decimal.DefaultContext.Emax = 2
            decimal.DefaultContext.Emin = 0
            decimal.DefaultContext.rounding = decimal.ROUND_FLOOR
            decimal.DefaultContext.capitals = 0
            decimal.DefaultContext.clamp = 1
            decimal.DefaultContext.flags[decimal.Inexact] = True
            decimal.DefaultContext.traps[decimal.Subnormal] = True
            poisoned = context_snapshot(decimal.DefaultContext)
            self.assertEqual(check_submission(package), expected)
            self.assertEqual(context_snapshot(decimal.DefaultContext), poisoned)
        finally:
            for field in ('prec', 'Emax', 'Emin', 'rounding', 'capitals', 'clamp'):
                setattr(decimal.DefaultContext, field, getattr(saved, field))
            decimal.DefaultContext.flags = saved.flags
            decimal.DefaultContext.traps = saved.traps

    def test_exact_results_and_human_review_boundary(self):
        for components, stated, expected in [(['0.00000001'], '0', '1E-8'),
                                             (['1', '-1'], '1', '0'),
                                             (['999999999999999999.99999999'] * 1000, '0',
                                              '999999999999999999999.99999000')]:
            with self.subTest(expected=expected):
                report = check_submission(arithmetic_package(components, stated))
                finding = next(f for f in report['findings'] if f['code'] == 'ARITHMETIC_MISMATCH')
                self.assertEqual(finding['evidence']['computed_sum'], expected)
                self.assertEqual(report['overall_status'], 'HUMAN_REVIEW_REQUIRED')
                self.assertFalse(report['truth_certification'])


class PinpointBoundaryTests(unittest.TestCase):
    def assert_locator(self, tail, expected, state):
        document = fictional_document(tail)
        original = deepcopy(document)
        package, manifest = prepare_package(document)
        self.assertEqual(document, original)
        candidate, = manifest['citation_candidates']
        self.assertEqual(candidate['locator'], expected)
        self.assertEqual(candidate['pinpoint_state'], state)
        self.assertEqual(package['claims'][0]['evidence'][0]['locator'], expected)
        self.assertEqual(document['segments'][0]['text'][candidate['start']:candidate['end']],
                         candidate['citation_text'])
        report = check_submission(package)
        self.assertEqual(report['overall_status'], 'HUMAN_REVIEW_REQUIRED')
        self.assertFalse(report['truth_certification'])

    def test_supported_single_tokens_and_punctuation_are_preserved(self):
        for tail, token in [('at [12].', '12'), ('at para 12', '12'),
                            ('para 000012', '000012'), ('at para 0', '0'),
                            ('at para 123456', '123456'), ('at para ١٢', '١٢'),
                            ('at para １２', '１２'), ('at [12], discussed here.', '12'),
                            ('at para 12; discussed here.', '12'),
                            ('at para 12: discussed here.', '12'), ('at para 12)', '12')]:
            with self.subTest(tail=tail):
                self.assert_locator(tail, 'para:' + token, 'SINGLE_PARAGRAPH_CANDIDATE')

    def test_unsupported_attached_tokens_are_not_shortened(self):
        tails = ['at para 1234567', 'at para 12A', 'at para 12.5', 'at para 12(1)',
                 'at para 12_3', 'at para 12²', 'at para 12\u0301', 'at para 12\u200d3',
                 'at [12]A', 'at [12](1)', 'at [12].5', 'at [1234567]',
                 'at para 12..14', 'at para 12.A', 'at para 12\\13',
                 'at para 12-a', 'at [12] (1)', 'at [12] (a)', 'at [12] (iv)',
                 'at [12] \u200d3', 'at para 12 (1.2)', 'at para 12 (a-b)',
                 'at [12] [a]', 'at [12] (see discussion)']
        for tail in tails:
            with self.subTest(tail=tail):
                self.assert_locator(tail, '', 'NOT_RECOGNISED')

    def test_ranges_and_lists_keep_explicit_annotation_state(self):
        tails = ['at [12]-[14]', 'at [12]–[14]', 'at [12], [14]',
                 'at paras 12 and 14', 'at paras 12 to 14', 'at paras 12 or 14',
                 'at para 12/13', 'at para 12 / 14', 'at [12][14]',
                 'at [12] [14]', 'at [12]; [14]']
        for tail in tails:
            with self.subTest(tail=tail):
                self.assert_locator(tail, '', 'RANGE_OR_LIST_REQUIRES_ANNOTATION')

    def test_long_numeric_tokens_never_become_shorter_locations(self):
        for length in (7, 8, 64, 1000):
            for form in ('at para {}', 'at [{}]'):
                with self.subTest(length=length, form=form):
                    self.assert_locator(form.format('1' * length), '', 'NOT_RECOGNISED')


class JsonFailureContractTests(unittest.TestCase):
    def test_decoder_value_error_is_normalised_to_input_error(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / 'input.json'
            path.write_text('{}', encoding='utf-8')
            with patch('court_integrity.__main__.json.loads', side_effect=ValueError('integer bound')):
                with self.assertRaisesRegex(InputError, 'bounded UTF-8 JSON'):
                    load_package(path)

    def test_existing_specific_json_diagnostics_are_preserved(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / 'input.json'
            for text, detail in [(' {"x":1,"x":2}', 'Duplicate JSON key'),
                                 ('{"x":NaN}', 'Non-standard JSON constant'),
                                 ('{"x":Infinity}', 'Non-standard JSON constant')]:
                with self.subTest(text=text):
                    path.write_text(text, encoding='utf-8')
                    with self.assertRaisesRegex(InputError, detail):
                        load_package(path)

    def test_cli_huge_integer_errors_are_structured_and_create_no_output(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            path = root / 'input.json'
            path.write_text('{"schema_version":' + '9' * 5000 + '}', encoding='utf-8')
            document = root / 'fictional.txt'
            document.write_text('Original fictional submission.', encoding='utf-8')
            commands = [['-m', 'court_integrity', str(path)],
                        ['-m', 'court_integrity.intake', str(document), '--sources', str(path)]]
            for index, command in enumerate(commands):
                with self.subTest(command=command):
                    output = root / ('output-' + str(index))
                    env = dict(os.environ, PYTHONINTMAXSTRDIGITS='640')
                    result = subprocess.run([sys.executable, *command, '--output', str(output)],
                                            cwd=Path(__file__).resolve().parents[1], env=env,
                                            text=True, capture_output=True, timeout=10)
                    self.assertEqual(result.returncode, 2, result.stderr)
                    self.assertEqual(result.stdout, '')
                    error = json.loads(result.stderr)
                    self.assertEqual(error['error'], 'InputError')
                    self.assertEqual(error['filing_decision'], 'NONE')
                    self.assertNotIn('Traceback', result.stderr)
                    self.assertFalse(output.exists())


if __name__ == '__main__':
    unittest.main()
