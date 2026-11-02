# Court Submission Integrity

**An inspectable preflight report for submissions, not an automated judge.**

A standalone research program prepared for **Albert Tan Sin Hon**, with
AI-assisted implementation. Research alpha **0.1.0a1**, 1 November 2026.
No court affiliation, endorsement, operational approval or adoption is claimed.

**Canonical repository:** https://github.com/Albertito-AI/court-submission-integrity

This is the dedicated project repository. It is independent of RegNav and has no
runtime dependency on another portfolio project. The earlier research-hub copy is
retained as historical provenance, not the location for continuing development.

[See demo](#see-it-in-action) | [Capability guide](docs/CAPABILITIES.md) |
[Collaborate and evaluate](docs/COLLABORATION.md) | [Run the examples](#run-the-examples) |
[Roadmap](docs/GLOBAL_ROADMAP.md) | [Validation](docs/VALIDATION.md) |
[Publication record](docs/PUBLICATION.md) | [Rights](RIGHTS.md)

## See it in action

**[Read the three-minute fictional demonstration](docs/DEMO.md).** No installation
is needed to inspect the examples and actual recorded findings.

| Supplied fictional material | What the program actually returns |
| --- | --- |
| Submission quotation: `Total: SGD 1,400.`; source passage: `Total: SGD 1,250.` | `QUOTE_NOT_MATCHED`, with both passages and their source location |
| Quotation points to paragraph 9 but appears at paragraph 8 in the supplied source | `QUOTE_AT_DIFFERENT_PINPOINT`, without silently changing the submission |
| A source is absent from the supplied package | `SOURCE_NOT_SUPPLIED`, unresolved rather than a finding of fabrication |

The walkthrough also shows annotated arithmetic, chronology, production-response
and argument-dependency checks. [Recorded observations](examples/demo-observations.json)
are reproducible with `python -m examples.record_demo --check`. These are constructed
examples, not evidence of general factual accuracy or reduced court backlogs.

**For courts and justice-technology teams:** the aim is to help filers correct
avoidable defects and help registry/judicial reviewers locate the material that
needs attention. [The capability guide](docs/CAPABILITIES.md) distinguishes working
components from future source verification, reasoning assistance and integration.
[Discuss a scoped fictional-data evaluation](docs/COLLABORATION.md) before any real
case processing, institutional participation or live-system access.

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

The [automated regression workflow](.github/workflows/tests.yml) runs the unittest
suite and independently verifies the recorded fictional demonstration on Python
3.10, 3.12 and 3.13. It installs the optional PDF parser in CI so that the PDF
cases are exercised rather than skipped. These checks establish reproducibility
of the supplied test cases, not the correctness of real legal submissions or
any court adoption.

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
