# Capabilities, beneficiaries and current limits

[See the fictional demonstration](DEMO.md) | [Propose collaboration](COLLABORATION.md)

## The workflow we are testing

A filer or authorised reviewer supplies a document and permitted source material.
The program produces an itemised report. A human checks the original, corrects or
explains a finding, and remains responsible for the filing and substantive decision.
The current software implements local inspection, not that entire operational cycle.

| User and task | What works in this alpha | Possible benefit to test | Still required |
| --- | --- | --- | --- |
| Filer checking citations and quotations | Selected neutral-citation recognition, supplied-source pinpoint checks and annotated quotation comparison | Fewer avoidable citation and transcription corrections | Independent authority retrieval, broader citation coverage and substantive legal review |
| Registry reviewing a production index | Declared request/response/document linkage and explanation-presence checks | Faster identification of missing package items or unanswered requests | Exact local rules and orders, rights checks, human review of objections and privilege |
| Judicial assistant tracing a proposition | Source/claim references, side-by-side passages, source-version metadata and explicit unresolved findings | Less time locating the material that needs attention | Reliable source identity, contextual support and assessment of evidence weight |
| Reviewer checking consistency | Annotated amounts, same-context values, date ordering and argument dependencies | Earlier identification of a specific inconsistency requiring explanation | Accurate annotations and contextual review; no general free-text logic evaluation |
| Court technology team assessing feasibility | Offline Python API/CLI, structured JSON, reproducible fictional inputs and local HTML | Inspectable starting point for a bounded evaluation | Security hardening, authentication, court-specific adapter and independently measured usefulness |

These benefits are hypotheses. No court has endorsed this program or demonstrated
saved judicial time through these examples. An invitation, reply, test run and
operational adoption are separate outcomes.

## Working components

The deterministic core validates the documented input structure, preserves the
supplied material, records input fingerprints and returns findings with locations
and next checks. Physical PDF pages, printed pages, paragraphs and sections remain
different locator types. Unavailable sources and partial extraction remain visible.

TXT and Markdown intake retain text offsets. The bounded DOCX reader extracts
supported text without running macros or following external relationships. Optional
PDF extraction does not perform OCR or guarantee recovery of layout and all text.
Sources are supplied transcriptions and metadata, not authenticated originals.

The structured engine distinguishes `fact`, `allegation`, `legal_argument` and
`inference` annotations. It does not decide which contested assertion is true.
Consistency groups retain party position, context, scenario and unit. Its argument
graph can expose missing references or cycles, not prove logical validity.

## Planned, not implemented or approved

Independent official/licensed source retrieval is the next product gate. General
proposition extraction, contextual legal-support analysis, free-text coherence
assessment, reliable citation treatment and court-specific rule packs need separate
implementation and evaluation. A second model's agreement would not establish truth.

A correction/explanation workspace, authenticated reviewer actions, immutable
operational history and live filing-system adapters are proposed developments.
The project is not currently a hosted service, e-filing gateway or certified court
product. It does not promise worldwide compatibility.

## Conditions for any real use

The alpha is for fictional or independently cleared material in a trusted local
environment. Binary parsing is not isolated for hostile files; generated reports
may repeat supplied information. Real case use needs appropriate institutional
permission, confidentiality and privilege controls, rights, security review,
retention rules, accountable staff and a validated jurisdiction/document profile.

Do not automatically reject, delay, rank or sanction a filing or person using this
prototype. Do not treat language fluency, legal novelty, an opposing account or
source unavailability as proof of poor merits or falsity.

## What would establish value

Measure per-defect false alarms and missed defects on independently labelled
examples. Record source coverage, abstention and extraction failures. Compare total
filer, registry and judicial-review effort with ordinary manual review, including
setup, corrections, explanations, escalations and false-alarm checking. Preserve
unfavourable results and stop or revise an approach that adds burden.

[The improvement protocol](CONTINUOUS_IMPROVEMENT.md) specifies the recurring review
and evidence gates. [The roadmap](GLOBAL_ROADMAP.md) separates a local demonstration,
independent evaluation, approved shadow pilot and actual integration. Publication
and internal tests are not substitutes for those stages. Existing [rights](../RIGHTS.md)
remain reserved; public visibility does not grant a new licence.
