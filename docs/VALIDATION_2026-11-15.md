# Reliability validation, 15 November 2026

Baseline: `3612e5f512ecdf6bd721e2db25d43bdd1bb3ec68` (47 files).
Implementation and distinct review were AI-assisted. No independent human legal
review, court adoption or real-case evaluation is claimed.

## Repairs and acceptance

| Trigger in the baseline | Result after the repair | Evidence |
| --- | --- | --- |
| Caller Decimal context changes exponent bounds, traps, rounding or formatting | Bounded sums and displayed totals use a complete local context, preserving caller state | Full report invariance, caller-state checks and independent report/HTML comparisons |
| Numeric pinpoint followed by unsupported suffix, oversized token, range or list | Intake abstains rather than inventing a shorter locator | Positive controls, adversarial suffixes, original offsets and explicit structured locators |
| A size-bounded JSON file contains an integer exceeding the interpreter conversion limit | CLI returns invalid-input exit 2 and `filing_decision: NONE`, without report files | Actual core/intake subprocess tests and precise duplicate/non-finite diagnostics |

The automatic pinpoint profile deliberately abstains on following parenthetical
or bracketed text and unsupported attached prose. This may leave an otherwise
valid citation for manual annotation. The [input contract](INPUT_CONTRACT.md)
documents this trade-off; typed structured locators remain available.

## Executed local checks

Environment: CPython 3.12.14/Linux, optional pypdf 6.21.4 already installed.
The exact baseline's 90 tests passed with no skips. The repaired runtime passed
100 tests with no skips, all four fictional CLI workflows and
`python -m examples.record_demo --check`.

The ten added test methods failed against the original runtime with 39 failing
subcases and five errors. An independent agent repeated the suite and separately
checked 60 full-report/HTML comparisons across altered Decimal contexts, twelve
actual CLI error cases and 43 pinpoint cases. Explicit `para:12A` structured
input remained supported. A review finding on spaced suffixes was repaired and
retested before acceptance.

Exact rollback restored every baseline file and passed all 90 tests and the
recorded demo. Exact reapplication of the four runtime/test files passed all 100
tests and the demo. Rollback therefore restores the known earlier behaviour,
including the three reproduced defects; it is a recovery option, not a preferred
runtime.

## Integration and limits

These are observed local results. The pull request and its associated Actions
runs provide the separate exact-commit hosted checks; no future run is certified
by this document. Existing workflow, rights, dependency declarations, fictional
fixtures, version and zero-network runtime remain unchanged.

The [comparative review](research/2026-11-15-repository-comparison.md) inspected
fourteen upstream projects without executing their code. It informed boundary
tests and future design gates. No foreign code, private source text or real court
data was imported. Source availability, quotation correspondence, proposition
support and truth remain separate. The authoritative-source resolver is still a
future gate.
