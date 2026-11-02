<!-- atlas-whitepaper:managed:v1 -->

# Court Submission Integrity: improving the path to human justice

## Thesis: help the court see the record more clearly

Courts need to decide substantive questions through legitimate procedures. Before that can happen, people must locate sources, inspect quotations, reconcile supplied figures and understand the structure of a submission. Court Submission Integrity proposes a bounded technical role: make specified defects and unresolved questions visible before substantive human review.

Its ambition is not a machine verdict. It is a better evidential handoff between filers, registries and judicial reviewers. The best case is fewer avoidable corrections and less wasted effort while preserving every person's opportunity to be heard. That outcome must be demonstrated with actual users; it does not follow from a convincing fictional example.

Prepared for Albert Tan Sin Hon with AI assistance, 2 November 2026. This is a design whitepaper, not legal advice, judicial endorsement, independent professional evaluation or permission to process real cases. The alpha's current constraints remain controlling.

## First principles: different questions require different evidence

Source presence, text agreement, contextual support, legal authority and truth are different questions. A quotation can match an authentic judgement while being used for a proposition the judgement does not support. A source may be absent from a package while existing elsewhere. An arithmetic inconsistency may concern competing factual cases rather than an error within one case.

These distinctions define the programme. Supplied sources and explicit annotations are the present input boundary. The output must say what was observed and what remains unknown. `SOURCE_NOT_SUPPLIED` cannot become a finding of fabrication. `QUOTE_AT_DIFFERENT_PINPOINT` cannot silently rewrite a filing. Even matched material retains human review.

The second principle is procedural neutrality. A report should help someone inspect a submission without ranking its merits, credibility or sophistication. Poor grammar, unfamiliar language and self-representation must not be treated as evidence of a weak case. Novel legal argument must remain distinguishable from an unsupported citation.

The third principle is reversibility and challenge. Preserve the original, its receipt time and the precise basis of every flag. An affected person must be able to explain a legitimate exception or challenge a mistaken extraction. A future integration must leave an urgent/manual route available when the tool fails.

## Fundamental logic of the alpha

The current local programme accepts structured material and limited document intake. It recognises selected citation candidates, checks typed paragraph/section/page locations against supplied text, and compares quotations with whitespace normalisation. More detailed consistency, arithmetic, chronology, dependency and production-response checks rely on explicit annotations.

That design is less general than an upload-any-document detector, but its findings are easier to reconstruct. A fictional quotation of SGD 1,400 beside a supplied invoice saying SGD 1,250 produces a concrete mismatch. The system displays the relevant passages and location. It does not decide whether the invoice is authentic, whether the debt exists or who should win.

An explicit argument graph can reveal a missing premise or cycle. It does not establish validity of every legal inference. A production-response map can show an unanswered declared request; it cannot decide privilege, proportionality or the scope of a disclosure obligation. These limits are part of the output contract, not fine print to remove when presenting the project.

## Why abstention is a positive capability

An unresolved result can be the most accurate and useful result. If extraction is incomplete, the report should preserve that fact rather than calculate a reassuring coverage percentage. If opposing parties assert different amounts, the system should retain their positions rather than merge them into an internal contradiction.

This creates a useful hierarchy: deterministic observations where the input permits them; clearly labelled review candidates where interpretation is needed; and explicit unsupported or unavailable states. A future model-assisted layer could propose questions, but every question should retain source anchors, coverage, reasons and an abstention path. Agreement between models would not substitute for independent evidence or a qualified person's review.

## Public-interest purpose and distribution of burdens

The project hopes to improve court operations and access to justice together. A tool that saves registry time by transferring excessive correction work to unrepresented filers may fail that purpose. An interface that makes polished submissions look credible while overflagging translated or scanned material may deepen inequality.

Evaluation should therefore examine the distribution of costs and errors. Measure work for filers, registry staff and substantive reviewers separately. Include represented and self-represented users, difficult extraction, legitimate alternative pleadings and differing language needs. Preserve the right to file and to challenge a flag. No automatic rejection, sanction or merits recommendation is proposed by this alpha.

The beneficial mechanism is practical: a filer finds a genuine defect early, understands it, corrects it without losing the original record, and reduces later reconstruction. A reviewer gains a clearer source trail. Whether those mechanisms reduce total effort or delay is an empirical question.

## Ideal progression and wishlist

| Gate | Intended capability | Necessary evidence |
| --- | --- | --- |
| Inspectable kernel | Local fictional checks and transparent reports | Reproducible examples and retained unknowns |
| One useful document profile | Hardened intake and an approved source-resolution route | Independently labelled permitted examples, coverage and failure reporting |
| Professional evaluation | Review questions that assist rather than distract | Blinded labels, per-defect precision/recall, false alarms and full workflow time |
| Court-approved shadow pilot | Read-only operation beside normal procedure | Local authorisation, confidentiality, challenge routes and measured burden |
| Scoped integration | Versioned adapters and accountable review records | Security, recovery, audit, accessibility and institutional acceptance |
| Another jurisdiction | A separately maintained local pack | Local sources, language coverage, qualified review and explicit exceptions |

The long-term wishlist includes accessible explanations, multilingual source navigation, reliable quotation conventions, provenance-aware correction histories and court-controlled deployment. Global reach should arise from a common engineering core with locally validated packs, not a universal claim that one jurisdiction's approval applies everywhere.

## What would disprove usefulness

The programme should stop or narrow a workflow if false alarms routinely obscure useful findings, users misunderstand a match as truth, privileged material cannot be protected, or total correction effort increases. A held-out evaluation should include accurate quotations used misleadingly, missing sources, valid unusual arguments and difficult documents. Otherwise a benchmark may reward easy detection while missing the problem courts actually face.

No number of unit tests establishes judicial benefit. The most meaningful milestone is an independently observed, authorised workflow in which people retain control, understand the findings and experience a measurable improvement without unacceptable harm. The ultimate hope is a more navigable evidential process in service of human judgement and legitimate institutions.

## Inspected foundation

Baseline: [`3587d109f13798f0f416258ed7076a792c7255d5`](https://github.com/Albertito-AI/court-submission-integrity/tree/3587d109f13798f0f416258ed7076a792c7255d5). See [README](https://github.com/Albertito-AI/court-submission-integrity/blob/3587d109f13798f0f416258ed7076a792c7255d5/README.md), [threat and justice safeguards](https://github.com/Albertito-AI/court-submission-integrity/blob/3587d109f13798f0f416258ed7076a792c7255d5/docs/THREAT_MODEL.md), [validation](https://github.com/Albertito-AI/court-submission-integrity/blob/3587d109f13798f0f416258ed7076a792c7255d5/docs/VALIDATION.md) and [international roadmap](https://github.com/Albertito-AI/court-submission-integrity/blob/3587d109f13798f0f416258ed7076a792c7255d5/docs/GLOBAL_ROADMAP.md). Existing reserved rights remain unchanged. No real case material, court contact, model call or deployment is authorised by this paper.
