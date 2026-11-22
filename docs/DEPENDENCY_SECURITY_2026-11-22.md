# Optional PDF parser security update | 22 November 2026

The optional `pdf` extra now requires `pypdf>=7.1.1,<8`. The previous
`pypdf>=5.9,<7` range excluded current fixes for published parser defects.
The standard-library core and TXT/DOCX paths retain their existing dependencies.

## Evidence and exposure

The upstream maintainer's
[cross-reference stream advisory](https://github.com/py-pdf/pypdf/security/advisories/GHSA-59jv-x5x2-gg4c)
affects versions below 7.0.0, while the
[image memory-allocation follow-up](https://github.com/py-pdf/pypdf/security/advisories/GHSA-fhff-j4m8-439h)
affects versions below 7.0.1. The [7.1.1 release](https://pypi.org/project/pypdf/7.1.1/)
includes subsequent parsing limits and supports Python 3.10+.

`court_integrity/intake.py` calls `PdfReader` and `page.extract_text()` on
supplied PDF bytes. This makes parser maintenance relevant. The image-specific
advisory is not asserted to be reachable through text extraction alone.
No exploit or compromise was demonstrated. The existing threat model's
hostile-input isolation limitation remains: a compressed file-size or page
limit is not a hard parser memory/CPU sandbox.

## Verification actually performed

On Linux, CPython 3.12.14, a fresh virtual environment contained the official
`pypdf` 7.1.1 wheel, whose SHA-256 matched the PyPI release metadata:
`04c5680d4b4cfa04ab505b09393fc949860c34a4dad6565284d11a2f5c3ce8b1`.
No project installation or automatic dependency hook was executed.

- All 100 existing unittest cases passed, including both optional PDF cases;
  no test was skipped.
- The adverse, matched and unknown structured examples and TXT intake completed
  successfully. Their reports retain `HUMAN_REVIEW_REQUIRED` and filing decision
  `NONE`.
- `python -m examples.record_demo --check` reproduced the four recorded fictional
  observations.

These are internal engineering checks on fictional data, not court approval,
independent human review or certification against malicious PDFs. Existing
installations must upgrade their parser explicitly. Continue the existing
input-isolation, rights and independent evaluation gates before real-case use.
