"""Internal checks that public fictional demonstration records stay reproducible."""
import json
import unittest
from unittest.mock import patch
from examples.record_demo import RECORD, observations, main


class PublicDemoTests(unittest.TestCase):
    def test_saved_record_matches_offline_execution(self):
        with patch('socket.socket', side_effect=AssertionError('network attempted')):
            self.assertEqual(json.loads(RECORD.read_text(encoding='utf-8')), observations())

    def test_every_example_retains_human_decision_and_uncertainty(self):
        record = observations()
        self.assertEqual(set(record['cases']), {'adverse', 'matched', 'unknown', 'intake'})
        for case in record['cases'].values():
            self.assertEqual(case['status'], 'HUMAN_REVIEW_REQUIRED')
            self.assertEqual(case['filing_decision'], 'NONE')
            self.assertIs(case['truth_certification'], False)
        self.assertNotIn('CHECK_FINDING', record['cases']['unknown']['finding_counts'])

    def test_altered_record_fails_verification(self):
        with patch('pathlib.Path.read_text', return_value='{}'):
            self.assertEqual(main(['--check']), 1)


if __name__ == '__main__':
    unittest.main()
