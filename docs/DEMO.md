# See it in action

**A three-minute walkthrough of actual fictional outputs. No installation is needed to read this page.**

[Capabilities and limits](CAPABILITIES.md) | [Collaborate on an evaluation](COLLABORATION.md) | [Reproduction record](DEMO_VALIDATION.md)

Court Submission Integrity helps a reviewer locate a specific discrepancy and its
source, rather than reading a submission with no indication of where to check.
These examples were executed with alpha `0.1.0a1` on 1 November 2026. They are
constructed demonstrations, not independent tests of legal accuracy or efficiency.

## 1. A quotation does not match the supplied invoice

| The annotated submission says | The supplied fictional source says | Actual result |
| --- | --- | --- |
| `Total: SGD 1,400.` | `Fictional invoice. Total: SGD 1,250.` | `QUOTE_NOT_MATCHED`, claim C1, reference 1 |

The report shows both passages and the pinpoint `printed-page:1`. It asks the
reviewer to check the original, punctuation, translation and context. It does not
silently change the submission or decide that either amount is true. The source
itself is supplied, not independently authenticated.

**Potential operational use:** a filer can correct or explain a transcription
problem before a registry officer or judge spends time tracing it. That time saving
has not yet been measured.

## 2. The quotation exists, but at a different pinpoint

The fictional submission links **"a court may order production."** to `para:9`.
The supplied exercise places those words at `para:8`; paragraph 9 discusses exceptions.
The actual result is `QUOTE_AT_DIFFERENT_PINPOINT`, retaining the submitted
pinpoint and identifying the other supplied location for human inspection.

**Potential operational use:** make a citation defect correctable without a reviewer
searching the entire bundle. The program does not infer the legal proposition,
automatically repair the citation or determine the authority's current status.

## 3. A document-production package contains further review questions

The same [fictional adverse input](../examples/adverse.json) produces these results:

| Constructed problem | Actual finding | Human question that remains |
| --- | --- | --- |
| 1,000 + 250 is stated as 1,400 | `ARITHMETIC_MISMATCH`: computed sum 1,250 | Were the numbers, unit and intended calculation mapped correctly? |
| One party's same transfer is annotated as both 1,200 and 1,500 | `ASSERTION_INCONSISTENCY_CANDIDATE` | Is there an explanation, timing difference or legitimate alternative case? |
| A declared send date follows its declared receipt date | `CHRONOLOGY_ORDER_CONFLICT` | Are the dates and assumed ordering correct? |
| A declared production request has no response record | `REQUEST_RESPONSE_NOT_SUPPLIED` | Is a response missing from the package, or is there an objection to record? |
| A produced document ID is absent from the package | `RESPONSE_SOURCE_NOT_SUPPLIED` | Does the production index need reconciliation? |
| Two annotated arguments depend on each other | `ARGUMENT_DEPENDENCY_CYCLE` | Is the mapping wrong, or is an independent premise needed? |

These structured checks require explicit annotations. The alpha does not discover
all facts or argument relationships in unrestricted prose. Opposing parties'
positions and alternative pleadings must not be treated as contradictions merely
because they differ. Withholding is not automatically a defect or misconduct.

## 4. Missing information stays unknown

The [unknown-source example](../examples/unknown.json) returns five `UNRESOLVED`
notices and **no `CHECK_FINDING`**. No external search is performed, so it does not
call the absent source fictitious.

The [matched example](../examples/matched.json) matches a quotation but still
returns `HUMAN_REVIEW_REQUIRED`, three unresolved scope/review notices and no truth
certificate. A correct quotation can be attached to an unsupported proposition.

## 5. Direct document intake

The [fictional TXT submission](../examples/intake_submission.txt) contains four
recognised citation candidates. Intake identifies one absent pinpoint in the
supplied transcription, leaves a paragraph range unresolved rather than reducing
it to its first paragraph, and marks an unsupplied source as unavailable.

The six extracted blocks produce one `CHECK_FINDING` and twelve `UNRESOLVED`
notices. Recognition is not exhaustive. TXT/Markdown, bounded DOCX and optional
text-bearing PDF input are supported; there is no OCR or independent retrieval.
Quotation and argument checks beyond this intake require explicit annotations.

## Reproduce the observations and open the HTML report

After obtaining the source, run from the repository root:

```sh
python -m examples.record_demo --check
python -m unittest discover -s tests -v
python -m court_integrity examples/adverse.json --output demo-adverse
python -m court_integrity.intake examples/intake_submission.txt --sources examples/intake_sources.json --jurisdiction FICTIONAL --output demo-intake
```

Open `demo-adverse/report.html` or `demo-intake/report.html` locally. Each workflow
also creates JSON. Use new output directories; existing ones are not overwritten.
The first command compares a fresh offline run with the committed
[observation summary](../examples/demo-observations.json), including input hashes.
It is a reproduction check, not a judicial quality score. Python 3.13.5/Linux is
the tested environment; other supported-version targets are not newly verified.

| Executed example | Check findings | Review candidates | Unresolved notices |
| --- | ---: | ---: | ---: |
| Structured adverse input | 6 | 2 | 19 |
| Matched quotation | 0 | 0 | 3 |
| Unknown source | 0 | 0 | 5 |
| Document intake | 1 | 0 | 12 |

Every example retains `filing_decision: NONE` and `truth_certification: false`.
Counts include scope and human-review notices, not just defects. No real case data,
external model calls, court-system access or demonstrated backlog reduction is
involved. The walkthrough displays recorded findings, not a browser screenshot.

**The evaluation question:** does this reduce justified correction and total human
review effort, or simply add false alarms? Help answer that through a
[scoped collaboration](COLLABORATION.md).
