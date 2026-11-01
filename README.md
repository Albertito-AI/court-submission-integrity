# Court Submission Integrity

**An inspectable preflight report for submissions, not an automated judge.**

A standalone research program prepared for **Albert Tan Sin Hon**, with
AI-assisted implementation. Research alpha **0.1.0a1**, 1 November 2026.
No court affiliation, endorsement, operational approval or adoption is claimed.

**Canonical repository:** https://github.com/Albertito-AI/court-submission-integrity

This is the dedicated project repository. It is independent of RegNav and has no
runtime dependency on another portfolio project. The earlier research-hub copy is
retained as historical provenance, not the location for continuing development.

[Run the examples](#run-the-examples) | [Capabilities](#what-the-alpha-checks) |
[Roadmap](docs/GLOBAL_ROADMAP.md) | [Validation](docs/VALIDATION.md) |
[Publication record](docs/PUBLICATION.md) | [Rights](RIGHTS.md)

## Run the examples

Clone this repository, or download and extract its source archive. From its root:

```sh
git clone https://github.com/Albertito-AI/court-submission-integrity.git
cd court-submission-integrity
python -m unittest discover -s tests -v
python -m court_integrity examples/adverse.json --output demo-adverse
python -m court_integrity.intake examples/intake_submission.txt --sources examples/intake_sources.json --jurisdiction FICTIONAL --output demo-intake
```

Open `demo-adverse/report.html` or `demo-intake/report.html` in a browser.
Each workflow also writes machine-readable JSON. Output directories must not
already exist, and their parent directory must exist. Exit code `0` means report
generation succeeded, not that a submission is accurate, admissible or fit to file.

The core, TXT/Markdown and bounded DOCX intake use Python's standard library.
No API key, model call, network connection or paid service is needed after obtaining
the source. Python 3.10+ is the compatibility target; the recorded local checks used
**CPython 3.13.5/Linux**. PDF intake needs an already installed optional `pypdf`
parser. Without it, two PDF tests are skipped. No package is installed automatically.

Additional fictional examples:

```sh
python -m court_integrity examples/matched.json --output demo-matched
python -m court_integrity examples/unknown.json --output demo-unknown
```

Even matched text remains `HUMAN_REVIEW_REQUIRED`. An unavailable source is not
labelled fictitious. All examples are original fictional exercises.

## What the alpha checks

| Area | Implemented check | Boundary |
| --- | --- | --- |
| Document intake | TXT/Markdown, bounded DOCX, optional text-bearing PDF; selected SG/UK neutral-citation candidates | No OCR, exhaustive recognition or independent source retrieval |
| Pinpoints and quotations | Typed paragraph, section and page locators; whitespace-only quotation comparison against supplied text | A match does not authenticate the source or establish substantive support |
| Evidence links | Missing references, absent passages, incomplete extraction and unanchored claim annotations | Detailed checks require explicit annotations and supplied source records |
| Consistency | Conflicting annotated values in the same context, party position, scenario and unit | Opposing accounts and alternative pleadings remain distinct |
| Arithmetic and chronology | Explicit decimal sums and declared date ordering | No automatic factual verification or legal deadline calculation |
| Argument structure | Missing references/premises and cycles in an explicit dependency graph | Not general logical, coherence or legal-merits evaluation |
| Document production | Declared requests, responses and linked document records | No privilege, proportionality or disclosure-duty decision |
| Reporting | Escaped offline HTML, JSON, input fingerprints and itemised review questions | No truth percentage, credibility score or automated filing decision |

**This is not an upload-any-document factuality or hallucination detector.** It is
an inspectable foundation for source-grounded submission review. Independent
source resolution, semantic reasoning analysis and court interfaces remain
separate development gates. No tagged release or hosted service is implied by
publication of this source alpha.

## Documentation and development

Read the [product brief](docs/PRODUCT_BRIEF.md), [input contract](docs/INPUT_CONTRACT.md),
[integration design](docs/INTEGRATION_DESIGN.md), [threat model](docs/THREAT_MODEL.md),
[research references](docs/RESEARCH_SOURCES.md) and [progress record](docs/PROGRESS.md).
The [global roadmap](docs/GLOBAL_ROADMAP.md) separates shared engineering from
jurisdiction-specific legal and institutional evaluation.
The [continuous improvement protocol](docs/CONTINUOUS_IMPROVEMENT.md) links recurring
maintenance to evidenced court tasks, independent evaluation and measured outcomes.

The repository includes runnable TXT/JSON fixtures and the original example
generators. Prebuilt binary samples and historical logs remain in the owner's
preserved archive. The optional `python -m examples.make_intake_documents` generator
requires already installed developer-only `python-docx` and `reportlab` packages.
It is not needed for the core examples or test suite.

Use fictional or independently cleared inputs in a trusted local environment.
Do not commit real court submissions, sealed or privileged documents, client or
student information, credentials or private generated reports. Independent
professional, security, accessibility and court-user evaluation remain outstanding.

## Rights and attribution

Public visibility is not an open-source licence. [RIGHTS.md](RIGHTS.md) preserves
the original reserved-rights position. [AUTHORS.md](AUTHORS.md) records Albert's
product direction and AI assistance without inventing independent human review.
