<!-- atlas-whitepaper:managed:v1 -->

# Court Submission Integrity: improving the path to human justice

## Abstract

Court Submission Integrity is a research alpha for inspecting supplied court-submission material before human review. Its contribution is a bounded separation of source availability, quotation correspondence and annotation-based consistency checks, with itemised evidence and explicit unknowns. This paper explains the contract, follows a fictional mismatch through the report, and proposes an evaluation that measures both useful corrections and the burden of false alerts. The evidence is implementation, regression tests and recorded fictional demonstrations. It does not establish legal accuracy, institutional approval, reduced delay or benefit to court users.

## Thesis: help the court see the record more clearly

Courts need to decide substantive questions through legitimate procedures. Before that can happen, people must locate sources, inspect quotations, reconcile supplied figures and understand the structure of a submission. Court Submission Integrity proposes a bounded technical role: make specified defects and unresolved questions visible before substantive human review.

Its ambition is not a machine verdict. It is a better evidential handoff between filers, registries and judicial reviewers. The best case is fewer avoidable corrections and less wasted effort while preserving every person's opportunity to be heard. That outcome must be demonstrated with actual users; it does not follow from a convincing fictional example.

Prepared for Albert Tan Sin Hon with AI assistance on 2 November 2026; documentation revised against the source identified below on 15 November 2026. This is a design whitepaper, not legal advice, judicial endorsement, independent professional evaluation or permission to process real cases. The alpha's current constraints remain controlling.

## First principles: different questions require different evidence

Source presence, text agreement, contextual support, legal authority and truth are different questions. A quotation can match an authentic judgement while being used for a proposition the judgement does not support. A source may be absent from a package while existing elsewhere. An arithmetic inconsistency may concern competing factual cases rather than an error within one case.

These distinctions define the programme. Supplied sources and explicit annotations are the present input boundary. The output must say what was observed and what remains unknown. `SOURCE_NOT_SUPPLIED` cannot become a finding of fabrication. `QUOTE_AT_DIFFERENT_PINPOINT` cannot silently rewrite a filing. Even matched material retains human review.

The second principle is procedural neutrality. A report should help someone inspect a submission without ranking its merits, credibility or sophistication. Poor grammar, unfamiliar language and self-representation must not be treated as evidence of a weak case. Novel legal argument must remain distinguishable from an unsupported citation.

The third principle is reversibility and challenge. Preserve the original, its receipt time and the precise basis of every flag. An affected person must be able to explain a legitimate exception or challenge a mistaken extraction. A future integration must leave an urgent/manual route available when the tool fails.

## Terms and evidence levels

| Term | Meaning in this alpha | What it does not establish |
| --- | --- | --- |
| Source record | A supplied identity, version, completeness declaration and locator-to-text map | Authenticity or completeness of the original |
| Pinpoint | A typed location such as `para:8` or `printed-page:1` | That physical and printed page numbers coincide |
| Text match | A quotation occurs in a supplied passage after whitespace normalisation | Contextual support, current authority or truth |
| Finding | A reproducible observation under the declared input contract | Misconduct or a filing decision |
| Review candidate | A mapped inconsistency requiring interpretation | That alternative pleadings are contradictory errors |

The [input contract](https://github.com/Albertito-AI/court-submission-integrity/blob/f11dba2e659e3f67d4ee2f6cf1ca6e16f18809a0/docs/INPUT_CONTRACT.md) is the operational definition. Automatic intake recognises selected neutral-citation candidates and a narrower single numeric paragraph profile. Unsupported suffixes, ranges and lists remain unresolved; explicit structured locators can express forms that intake does not recognise. Annotation completeness is itself unassessed.

## Fundamental logic of the alpha

The current local programme accepts structured material and limited document intake. It recognises selected citation candidates, checks typed paragraph/section/page locations against supplied text, and compares quotations with whitespace normalisation. More detailed consistency, arithmetic, chronology, dependency and production-response checks rely on explicit annotations.

That design is less general than an upload-any-document detector, but its findings are easier to reconstruct. A fictional quotation of SGD 1,400 beside a supplied invoice saying SGD 1,250 produces a concrete mismatch. The system displays the relevant passages and location. It does not decide whether the invoice is authentic, whether the debt exists or who should win.

An explicit argument graph can reveal a missing premise or cycle. It does not establish validity of every legal inference. A production-response map can show an unanswered declared request; it cannot decide privilege, proportionality or the scope of a disclosure obligation. These limits are part of the output contract, not fine print to remove when presenting the project.

## Worked example and counterexample

Use the committed [adverse fixture](https://github.com/Albertito-AI/court-submission-integrity/blob/f11dba2e659e3f67d4ee2f6cf1ca6e16f18809a0/examples/adverse.json), whose source and claims are fictional. Claim C1 quotes `Total: SGD 1,400.`; the supplied invoice at `printed-page:1` contains `Total: SGD 1,250.`. The engine first resolves the declared source and locator, then performs the whitespace-only comparison. Its `QUOTE_NOT_MATCHED` finding retains both texts. The separate arithmetic annotation gives components 1,000 and 250 and a stated total of 1,400, so the bounded sum is 1,250 and the arithmetic check also reports a mismatch. These are distinct observations, not two independent confirmations that the invoice is true.

The [recorded demonstration](https://github.com/Albertito-AI/court-submission-integrity/blob/f11dba2e659e3f67d4ee2f6cf1ca6e16f18809a0/docs/DEMO.md) also places a quoted passage at paragraph 8 while the annotation cites paragraph 9. `QUOTE_AT_DIFFERENT_PINPOINT` identifies that discrepancy without rewriting the input. By contrast, the [matched fixture](https://github.com/Albertito-AI/court-submission-integrity/blob/f11dba2e659e3f67d4ee2f6cf1ca6e16f18809a0/examples/matched.json) still requires human review. A perfectly transcribed sentence may omit a decisive exception or support a different proposition. This counterexample explains why matching is intentionally weaker than verification.

### Reproduce the bounded observations

From an exact checkout of `f11dba2e659e3f67d4ee2f6cf1ca6e16f18809a0`, with Python 3.10 or newer and new output directories:

```sh
python -m unittest discover -s tests -v
python -m examples.record_demo --check
python -m court_integrity examples/adverse.json --output paper-adverse
python -m court_integrity examples/matched.json --output paper-matched
```

Read each JSON and HTML report alongside its fixture. Record the commit, Python and optional parser versions, command exits, findings and skipped tests. The standard-library paths work without a model or network call; PDF checks require an already installed optional `pypdf`. An exit of 0 reports successful generation, not an accepted filing. These are reproduction instructions, not a claim that this documentation revision executed them.

| Claim in this paper | Inspectable evidence at the reviewed commit | Evidential limit |
| --- | --- | --- |
| Matched text retains substantive review | [Engine quotation branches and final report](https://github.com/Albertito-AI/court-submission-integrity/blob/f11dba2e659e3f67d4ee2f6cf1ca6e16f18809a0/court_integrity/engine.py) | Code establishes the programmed contract, not real-case accuracy |
| Unsupported intake suffixes do not become shortened pinpoints | [Intake parser](https://github.com/Albertito-AI/court-submission-integrity/blob/f11dba2e659e3f67d4ee2f6cf1ca6e16f18809a0/court_integrity/intake.py) and [boundary tests](https://github.com/Albertito-AI/court-submission-integrity/blob/f11dba2e659e3f67d4ee2f6cf1ca6e16f18809a0/tests/test_reliability.py) | Conservative abstention can also affect ordinary parenthetical commentary |
| Bounded addition is isolated from caller Decimal settings | [Reliability tests](https://github.com/Albertito-AI/court-submission-integrity/blob/f11dba2e659e3f67d4ee2f6cf1ca6e16f18809a0/tests/test_reliability.py) and [15 November record](https://github.com/Albertito-AI/court-submission-integrity/blob/f11dba2e659e3f67d4ee2f6cf1ca6e16f18809a0/docs/VALIDATION_2026-11-15.md) | Recorded engineering checks do not validate the meaning of supplied amounts |
| Fictional outputs can be reconstructed | [Demonstration and procedure](https://github.com/Albertito-AI/court-submission-integrity/blob/f11dba2e659e3f67d4ee2f6cf1ca6e16f18809a0/docs/DEMO.md) | Constructed cases are not a representative court benchmark |

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

## Related work and the scope of the contribution

The Singapore Courts' [Guide on the Use of Generative Artificial Intelligence Tools by Court Users](https://www.judiciary.gov.sg/docs/default-source/news-and-resources-docs/guide-on-the-use-of-generative-ai-tools-by-court-users.pdf), applicable from 1 October 2024, distinguishes checking that authorities exist, checking the propositions attributed to them and checking quotations. Paragraphs 5(3)(c)–(e), printed page 4, also distinguish accurate-source checking from asking another generative system for confirmation. This paper draws a design lesson from those distinctions. It does not claim that the alpha performs all the required work or complies with every jurisdiction's rules.

The [maintained primary-source register](https://github.com/Albertito-AI/court-submission-integrity/blob/main/docs/RESEARCH_SOURCES.md) records further legal and standards references with their limits. Its 15 November 2026 correction identifies the guide passage above as printed page 4 and physical PDF page 4; the earlier frozen register contains the superseded printed-page label. The [fourteen-repository comparison](https://github.com/Albertito-AI/court-submission-integrity/blob/f11dba2e659e3f67d4ee2f6cf1ca6e16f18809a0/docs/research/2026-11-15-repository-comparison.md) is a dated source inspection, not a comparative accuracy trial. Its useful methodological lesson is to keep authoritative-source resolution, access control and jurisdiction-specific interpretation as separately evidenced capabilities. No superiority or novelty claim follows simply from combining these ideas.

## Evaluation design and teaching use

A future permitted evaluation should define its unit before collecting results: one annotated quotation, one arithmetic annotation, or one complete review task. Build independently labelled cases with positive controls, unsupported inputs, authentic-looking misleading extracts and legitimate exceptions. Keep development examples separate from held-out cases. Record per-defect true and false alerts, missed defects, abstentions and extraction failures with denominators. If precision or recall is reported, define the eligible labelled population and report abstentions separately rather than removing difficult cases.

Measure annotation preparation, inspection, correction and dispute time for filers and reviewers, including failed tasks. Use comparable tasks and account for familiarity and order effects before attributing a difference to the tool. The plan has not been conducted and provides no effect-size estimate.

For a teaching exercise, ask learners to explain the adverse finding, then defend why the matched case remains unresolved. Next give a quotation with a legitimate parenthetical suffix and ask whether automatic abstention is preferable to inventing a shorter locator. A satisfactory answer identifies the exact source and location, distinguishes extraction from interpretation, preserves the original and states the remaining human question. Evaluate those distinctions directly; completing a CLI command is not evidence of legal competence.

## What would disprove usefulness

The programme should stop or narrow a workflow if false alarms routinely obscure useful findings, users misunderstand a match as truth, privileged material cannot be protected, or total correction effort increases. A held-out evaluation should include accurate quotations used misleadingly, missing sources, valid unusual arguments and difficult documents. Otherwise a benchmark may reward easy detection while missing the problem courts actually face.

No number of unit tests establishes judicial benefit. The most meaningful milestone is an independently observed, authorised workflow in which people retain control, understand the findings and experience a measurable improvement without unacceptable harm. The ultimate hope is a more navigable evidential process in service of human judgement and legitimate institutions.

## Inspected foundation

Source reviewed for this revision: [`f11dba2e659e3f67d4ee2f6cf1ca6e16f18809a0`](https://github.com/Albertito-AI/court-submission-integrity/tree/f11dba2e659e3f67d4ee2f6cf1ca6e16f18809a0). The source and cited records were inspected; no fresh runtime evaluation is claimed here. See [README](https://github.com/Albertito-AI/court-submission-integrity/blob/f11dba2e659e3f67d4ee2f6cf1ca6e16f18809a0/README.md), [threat and justice safeguards](https://github.com/Albertito-AI/court-submission-integrity/blob/f11dba2e659e3f67d4ee2f6cf1ca6e16f18809a0/docs/THREAT_MODEL.md), [validation](https://github.com/Albertito-AI/court-submission-integrity/blob/f11dba2e659e3f67d4ee2f6cf1ca6e16f18809a0/docs/VALIDATION.md) and [international roadmap](https://github.com/Albertito-AI/court-submission-integrity/blob/f11dba2e659e3f67d4ee2f6cf1ca6e16f18809a0/docs/GLOBAL_ROADMAP.md). Existing reserved rights remain unchanged. No real case material, court contact, model call or deployment is authorised by this paper.
