# Dedicated-repository validation | 1 November 2026

Action: `CSI-20261101-DEDICATED-03`. Version `0.1.0a1`.
All checks below are internal AI-assisted engineering checks, not independent
human legal review or a judicial accuracy, efficiency or security certification.

## Source and environment

Original archive SHA-256:
`06216b5b8c1323b9b44f08b7cfff845fdefde9e2df5a579bf812dfa0d1eb8847`.
ZIP CRC validation passed, and extraction rejected unsafe member paths/symlinks.
Runtime code, tests and fictional fixtures were copied without modification.
Publication documentation was updated for the dedicated repository.

Environment: CPython **3.13.5**, Linux x86_64, existing optional **pypdf 5.9.0**.
Python 3.10+ remains a compatibility target, not a verified multi-version result.
The optional parser has not received a production dependency/security approval.

## Checks performed during this launch

- `python -m unittest discover -s tests -v`: **87 passed, no skips**.
- Structured adverse, matched and unknown examples generated JSON and HTML.
- TXT intake with the supplied fictional sources generated its report, package
  and manifest, identifying **four** citation candidates.
- The adverse fixture retained six CHECK_FINDING items, two REVIEW_CANDIDATE
  items and nineteen UNRESOLVED notices. These are constructed test outcomes,
  not measured accuracy on real submissions.
- Reports retained `HUMAN_REVIEW_REQUIRED`, no automatic filing decision and no
  truth certification, including the matched example.
- Python compile checks and local Markdown file-link checks passed.
- Local file/blob fingerprints and the complete Git tree are used to bind the
  uploaded source to the source actually tested. The private receipt retains
  exact revision and readback evidence after publication.

No hosted CI was run or claimed. No model API, external source resolver, hosting
service or paid dependency installation was initiated. New output directories
were used, preserving the refusal to overwrite existing reports.

## Reproduce

From the repository root, with output folders that do not already exist:

```sh
python -m unittest discover -s tests -v
python -m court_integrity examples/adverse.json --output review-adverse
python -m court_integrity examples/matched.json --output review-matched
python -m court_integrity examples/unknown.json --output review-unknown
python -m court_integrity.intake examples/intake_submission.txt --sources examples/intake_sources.json --jurisdiction FICTIONAL --output review-intake
```

Without the optional PDF parser, the suite skips two PDF tests. These skips must
not be reported as passing tests. The core and TXT/DOCX paths use the standard library.

## Outstanding evaluation

Independent source retrieval, general semantic/coherence analysis, real court
integration, authenticated human review, hostile-input isolation and independent
user/legal evaluation remain unimplemented or unverified. Full visual browser,
accessibility and cross-browser validation remain unverified. Earlier browser and
dependency-fetch failures remain in the original archived validation record;
this publication does not imply that those failures have been resolved.

Matching supplied text does not establish authenticity, contextual legal support,
current law or real-world truth. No real-case processing or court deployment is
approved by these tests. See [THREAT_MODEL.md](THREAT_MODEL.md).
