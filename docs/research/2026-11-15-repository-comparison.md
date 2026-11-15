# Repository comparison for Atlas Court

Date: 15 November 2026. Status: completed source review; Atlas runtime repairs accepted locally, with integration recorded separately in the pull request.

Four read-only reviews account for all fourteen supplied repositories at exact default-branch heads. They inspected complete trees, README/licence material, representative implementation and tests through GitHub. No upstream application, test, installer, model, database, credential or committed index was executed or probed. Findings below describe inspected source, with conditional consequences distinguished from observed behaviour. Educational and preliminary projects are evaluated within their stated scope, not against an invented production promise.

Atlas remains an offline, reserved-rights submission-integrity prototype requiring human review. “Adopt” means independently implement a design concept, not copy foreign code. “Defer” requires the stated evidence before expansion. “Reject” identifies an unsuitable transfer into Atlas. A software licence does not automatically clear legal texts, personal data, models or bundled assets. Public visibility is not permission. The [source index](repository-source-index.json) records full heads, licence inspection, evidence anchors and decisions; commit links below pin the displayed abbreviations.

| Repository | Reviewed commit | Inspected licence position |
|---|---|---|
| 1. bcgov/SCJ-Online-Booking | [80b75ce123d5](https://github.com/bcgov/SCJ-Online-Booking/commit/80b75ce123d54a05d4e996201d8a1ed59d800336) | Apache-2.0 |
| 2. nationalarchives/ds-caselaw-judiciary-guidance | [59aaf3806edf](https://github.com/nationalarchives/ds-caselaw-judiciary-guidance/commit/59aaf3806edf516d54912d5662abbf13a0539177) | No explicit grant found |
| 3. brazanation/go-documents | [4b8a986bc944](https://github.com/brazanation/go-documents/commit/4b8a986bc944042abb3e7d732a1363dbae7f16e8) | MIT |
| 4. adamcohen3/fines-and-fees-calculator | [fddd1b6d9713](https://github.com/adamcohen3/fines-and-fees-calculator/commit/fddd1b6d97131fb79650f9773d9fb7294cc551a3) | GPL-3.0 |
| 5. viru0909-dev/nyay-setu-working | [c84da82d6789](https://github.com/viru0909-dev/nyay-setu-working/commit/c84da82d67891166bf51e5d17c088217bd8b873a) | MIT text; API NOASSERTION |
| 6. rohitroy-github/vite-project-evault | [d07168a329a7](https://github.com/rohitroy-github/vite-project-evault/commit/d07168a329a7b3b7676fb532aeb9714840329a96) | Contract MIT header only |
| 7. capybara-brain346/atjbot | [5e538944e498](https://github.com/capybara-brain346/atjbot/commit/5e538944e498dfb5da8d9bb9a45ba94dac687403) | MIT |
| 8. animesh-s/Judiciary-Information-System | [927531d6a01e](https://github.com/animesh-s/Judiciary-Information-System/commit/927531d6a01e8457ff97fb439b9bf0874ac5fc89) | No explicit grant found |
| 9. egeakin/National-Judiciary-System | [c8a01310823a](https://github.com/egeakin/National-Judiciary-System/commit/c8a01310823ad73adb840df01abd9c9f37704157) | No explicit grant found |
| 10. gaurav-karki/ngm | [174088b33191](https://github.com/gaurav-karki/ngm/commit/174088b33191e0062b9385603571bc3218de2ee1) | MIT |
| 11. 5hreyanshPandey/InfoSetu_AI_ChatBot | [a32a26945902](https://github.com/5hreyanshPandey/InfoSetu_AI_ChatBot/commit/a32a26945902205c42f9c35757a1cbda25bda831) | No explicit grant found |
| 12. kumar-shubham1/CaseRank | [effe4e19e959](https://github.com/kumar-shubham1/CaseRank/commit/effe4e19e95982f82448bb87b61045c4f7df1007) | No project grant found |
| 13. MokshShahh/JudiciaryAI | [f88fa442af5d](https://github.com/MokshShahh/JudiciaryAI/commit/f88fa442af5d2639413d93e15179ccf3dafe3965) | No explicit grant found |
| 14. nyimbi/caseke | [ec5f162784b1](https://github.com/nyimbi/caseke/commit/ec5f162784b141fd08abe5987efa2a2a62d6e713) | MIT |

## Workflow and publication references

<a id="r1"></a>

### 1. BC Supreme Court booking

The controller separates a completed regular booking from a submitted fair-use request and preserves correction context. Adopt that distinction for intake, review and completed analysis; an analysis receipt must never imply court acceptance. [CaseConfirm](https://github.com/bcgov/SCJ-Online-Booking/blob/80b75ce123d54a05d4e996201d8a1ed59d800336/app/Controllers/ScLotteryEnabledControllerBase.cs#L190-L225) shows the useful boundary. The sampled [integration tests](https://github.com/bcgov/SCJ-Online-Booking/blob/80b75ce123d54a05d4e996201d8a1ed59d800336/tests/RemoteApiTests.cs#L65-L105) distinguish success/failure in names but merely assert non-null results; the fake SOAP client depends on environment configuration. Four exact-head CodeQL checks passed, which does not establish functional booking acceptance. Defer live integration and reject importing British Columbia scheduling rules, lottery assumptions or fairness claims.

<a id="r2"></a>

### 2. National Archives judiciary guidance

This is static publishing guidance, not the Find Case Law parser or an authority resolver. It identifies [DOCX conversion losses and replacement publications](https://github.com/nationalarchives/ds-caselaw-judiciary-guidance/blob/59aaf3806edf516d54912d5662abbf13a0539177/content/about_this_guidance.html#L7-L35), and [citation guidance](https://github.com/nationalarchives/ds-caselaw-judiciary-guidance/blob/59aaf3806edf516d54912d5662abbf13a0539177/content/ncn.html#L188-L196) recognises decisions without neutral citations. Adopt separate original/extracted digests and profile-specific unknown states. A stable URL is not an immutable document; an unrecognised citation is not proof of fabrication. Successful build/deploy/pre-commit checks concern the site, not legal conformance. Defer resolver claims and reject redaction certification or copying text/assets without an established grant. Public-sector ownership alone does not establish a repository licence.

<a id="r3"></a>

### 3. Brazilian identifier library

Typed identifiers and example tests provide a useful separation between identifier kind, display format and validation. [NewDocument](https://github.com/brazanation/go-documents/blob/4b8a986bc944042abb3e7d732a1363dbae7f16e8/internal/document.go#L15-L49) removes all non-digits, however, which would damage legal citations. The [bounds and validation order](https://github.com/brazanation/go-documents/blob/4b8a986bc944042abb3e7d732a1363dbae7f16e8/internal/document.go#L74-L107) gives one- or two-digit CPF inputs an unsafe static path: slicing precedes validation and later code can index an empty base. This was not executed; empty input is not asserted always to panic. Adopt raw/canonical separation and malformed-boundary tests. Defer new identifier profiles without specifications; reject checksum results as identity authentication. Configured Go tests exist, but no exact-head check result was returned.

<a id="r4"></a>

### 4. Hawaii fines and fees calculator

The Shiny workflow offers validation, correction, review and explicitly provisional estimates. [chargeList](https://github.com/adamcohen3/fines-and-fees-calculator/blob/fddd1b6d97131fb79650f9773d9fb7294cc551a3/app.R#L1203-L1222) selects dated charge versions and stable identifiers. Adopt those concepts with independently verified jurisdiction profiles; the underlying RDS rules, current legal accuracy, README study participation claim and any effectiveness outcomes were not independently established. [Dropbox persistence and session logging](https://github.com/adamcohen3/fines-and-fees-calculator/blob/fddd1b6d97131fb79650f9773d9fb7294cc551a3/app.R#L63-L105) are implemented data flows, not evidence of a privacy breach. No automated suite or CI was found in the complete tree. Defer substantive rule reuse and reject inherited telemetry, Hawaiian formulae presented as universal, or GPL source transplantation into reserved-rights Atlas without a compatibility decision.

## Intake, provenance and access boundaries

<a id="r5"></a>

### 5. Nyay Setu

Substantial draft, confirmation, role, document and audit machinery is present. Adopt staged review and explicit evidence states. [Draft create/list handlers](https://github.com/viru0909-dev/nyay-setu-working/blob/c84da82d67891166bf51e5d17c088217bd8b873a/backend/nyaysetu-backend/src/main/java/com/nyaysetu/backend/controller/CaseDraftController.java#L36-L150) lack the ownership binding used by confirmation, while the [request wrapper](https://github.com/viru0909-dev/nyay-setu-working/blob/c84da82d67891166bf51e5d17c088217bd8b873a/backend/nyaysetu-backend/src/main/java/com/nyaysetu/backend/filter/XssSanitizationFilter.java#L25-L85) converts binary bodies through text, so original bytes are not necessarily preserved. The [audit chain](https://github.com/viru0909-dev/nyay-setu-working/blob/c84da82d67891166bf51e5d17c088217bd8b873a/backend/nyaysetu-backend/src/main/java/com/nyaysetu/backend/service/AuditChainService.java#L17-L105) lacks an independently fixed expected tail/count; a remaining prefix can validate after tail removal. AI paths provide different provenance guarantees, and numeric section ranges do not establish proposition support. Sampled Java/Python tests do not establish these missing boundaries. Defer multi-user/AI expansion; reject hash-as-admissibility claims and treating a global role as case assignment. These are static findings, not demonstrated deployed exploits.

<a id="r6"></a>

### 6. E-vault

The contract and frontend implement participant/case records, wallet calls, Pinata upload and identifier readback. Adopt stable identifiers and exact receipts as offline concepts. [Contract methods](https://github.com/rohitroy-github/vite-project-evault/blob/d07168a329a7b3b7676fb532aeb9714840329a96/blockchain-hardhat/contracts/EVault_Main.sol#L1-L593) treat UID existence as login, and case updates lack assignment/caller checks. Public mappings and document locators do not establish confidentiality. [Browser uploads](https://github.com/rohitroy-github/vite-project-evault/blob/d07168a329a7b3b7676fb532aeb9714840329a96/frontend-vite/src/blockchain-api/uploadCaseDocument.jsx#L19-L58) require provider credentials available to client execution; no credential value was tested or reproduced. Hardhat tests include happy-path readback, not demonstrated rejection of unauthorised mutations. Defer online storage. Reject private evidence on public chains, wallet connection as case permission and timestamp-based allocation as fairness. The MIT header covers the contract; no project-wide grant was found.

<a id="r7"></a>

### 7. Access-to-justice chatbot

React language choices, Flask chat, Chroma ingestion and cloud model calls are implemented. In [query_rag](https://github.com/capybara-brain346/atjbot/blob/5e538944e498dfb5da8d9bb9a45ba94dac687403/backend/utils.py#L19-L117), answer context and displayed links come from separate collections; metadata and scores are discarded. A link therefore does not establish support for a proposition. [Ingestion](https://github.com/capybara-brain346/atjbot/blob/5e538944e498dfb5da8d9bb9a45ba94dac687403/bot/pipeline/run_rag_pipelines.py#L1-L123) adds absent IDs without replacing changed content under existing IDs. Success returns a tuple while failure returns a string, weakening the endpoint's error contract. Adopt typed unavailable states and versioned source-bound chunks. Defer multilingual fidelity claims; a manual checklist is not an executed evaluation. Reject separate link search as evidence, unversioned corpus assumptions and prompt-only safeguards.

## Case relationships and import completeness

<a id="r8"></a>

### 8. Judiciary Information System

The Java Swing prototype provides role screens and case/hearing/summary database operations; the README's broader requirements are not implementation proof. [Case registration](https://github.com/animesh-s/Judiciary-Information-System/blob/927531d6a01e8457ff97fb439b9bf0874ac5fc89/src/Cases.java#L307-L340) concatenates GUI text into SQL and [can display success after a caught error](https://github.com/animesh-s/Judiciary-Information-System/blob/927531d6a01e8457ff97fb439b9bf0874ac5fc89/src/Cases.java#L321-L341). [Registrar updates](https://github.com/animesh-s/Judiciary-Information-System/blob/927531d6a01e8457ff97fb439b9bf0874ac5fc89/src/Registrar.java#L394-L419) overwrite fields without an accompanying actor/time/reason event in the inspected handlers. Adopt event vocabulary and failure receipts; defer database workflows until transactional and authorised. Reject raw SQL concatenation and copied credentials or local criminal-case assumptions. The 2016 tree contains a test-design PDF but no executable tests/build manifest. No database was contacted and deployment compromise is not claimed.

<a id="r9"></a>

### 9. National Judiciary System

This course project supplies a schema/bootstrap, screenshots and reports; its linked PHP application's source is absent. A [composite trial/statement relationship](https://github.com/egeakin/National-Judiciary-System/blob/c8a01310823ad73adb840df01abd9c9f37704157/Java/src/Main.java#L143-L158) usefully binds a statement to a case and hearing. Adopt explicit referential checks, while deferring a hearing-identity profile because a date alone may be insufficient. [Main.main](https://github.com/egeakin/National-Judiciary-System/blob/c8a01310823ad73adb840df01abd9c9f37704157/Java/src/Main.java#L6-L19) unconditionally drops domain tables before rebuilding; [another loop prints password fields](https://github.com/egeakin/National-Judiciary-System/blob/c8a01310823ad73adb840df01abd9c9f37704157/Java/src/Main.java#L379-L401). Reject destructive bootstrap and personal-data fixtures. No executable tests or CI appear in the 2019 tree. Role entities and visibility strings do not demonstrate authorisation; the program was not run and seeded identities were not assumed real.

<a id="r10"></a>

### 10. Nepal court-data pipeline

Court-scoped case IDs and separate calendar fields are useful ingestion concepts. [Daily-list processing](https://github.com/gaurav-karki/ngm/blob/174088b33191e0062b9385603571bc3218de2ee1/ngm/ngscrape/spiders/district_court_cases.py#L184-L220) can mark a date complete after missing tables or skipped malformed rows. The [enrichment selector](https://github.com/gaurav-karki/ngm/blob/174088b33191e0062b9385603571bc3218de2ee1/ngm/ngscrape/spiders/district_case_enrichment.py#L103-L122) uses SQL IN with NULL rather than an explicit null predicate, and failed records fall outside that selection. Request retries do exist. Adopt namespaced identities and complete/partial/failed states, preserving original calendar and source versions. Defer collection pending permissions and reproducibility; reject completion markers as proof of completeness. Re-enrichment replaces entities and fields, risking lost history. Five collection workflows are not tests, and no test files were found; no live loss was observed.

## Retrieval, reasoning and model boundaries

<a id="r11"></a>

### 11. InfoSetu

The inspected final Flask implementation performs deterministic CSV lookups, not the README's named GPT/Voiceflow workflow: those implementation files are absent. [bot_response](https://github.com/5hreyanshPandey/InfoSetu_AI_ChatBot/blob/a32a26945902205c42f9c35757a1cbda25bda831/final/coi_casedata/app.py#L83-L132) has explicit not-found and clarification responses, and [message rendering](https://github.com/5hreyanshPandey/InfoSetu_AI_ChatBot/blob/a32a26945902205c42f9c35757a1cbda25bda831/final/coi_casedata/static/main.js#L102-L108) escapes HTML. Adopt these useful restrained behaviours. The sampled data/answer contract lacks authoritative source versions, hashes and pinpoints; a mock case CSV does not establish live court integration. No project tests or CI were found. Defer legal/current-case claims until provenance is established; reject unlicensed code/assets, official branding assumptions and mock records presented as live facts.

<a id="r12"></a>

### 12. CaseRank

Source defines bounded uploads, Gemini analysis and weighted ranking, but an imported [controller contains unresolved merge-conflict markers](https://github.com/kumar-shubham1/CaseRank/blob/effe4e19e95982f82448bb87b61045c4f7df1007/backend/controllers/caseController.js#L306-L348), blocking that source path. [Analysis failures](https://github.com/kumar-shubham1/CaseRank/blob/effe4e19e95982f82448bb87b61045c4f7df1007/backend/utils/gemini.js#L19-L220) become ordinary Medium/5 fallback objects that the controller can persist as success; its smoke script can report success after such fallback. Adopt upload bounds, origin labels and explicit unavailable results. Defer model integration until reproducibility and evidence support are demonstrated. Reject automated judicial/merits priority weights, fallback-as-assessment and cloud transmission of private submissions. No npm test script or CI was found. Source definitions and README model names do not establish a working runtime; none was executed.

<a id="r13"></a>

### 13. JudiciaryAI

PDF extraction, chunks, FAISS and cloud generation are present. [Ingestion](https://github.com/MokshShahh/JudiciaryAI/blob/f88fa442af5d2639413d93e15179ccf3dafe3965/bot/add_pdfs.py#L20-L51) discards page metadata and rebuilds the same index for successive PDFs. The [answer chain](https://github.com/MokshShahh/JudiciaryAI/blob/f88fa442af5d2639413d93e15179ccf3dafe3965/bot/app.py#L28-L64) suppresses PDF references and returns no evidence ledger. Generated HTML rendering and dangerous pickle loading create conditional risks, not demonstrated exploits. Adopt source/page/chunk identities, versioned multi-document manifests and abstention on unsupported spans. Defer RAG until reproducible dependencies and provenance tests exist: the sampled React test imports an absent module and backend requirements omit imported packages. Reject citation suppression, raw model HTML, untrusted indexes and unlicensed source/corpus reuse.

<a id="r14"></a>

### 14. caseke

The explicitly preliminary application has a useful case/filing/document/hearing graph. [Document and event models](https://github.com/nyimbi/caseke/blob/ec5f162784b141fd08abe5987efa2a2a62d6e713/app/models.py#L493-L557) offer metadata, but [admin views](https://github.com/nyimbi/caseke/blob/ec5f162784b141fd08abe5987efa2a2a62d6e713/app/views.py#L665-L740) permit editing/deletion, so the log is not append-only. The [document observer](https://github.com/nyimbi/caseke/blob/ec5f162784b141fd08abe5987efa2a2a62d6e713/app/mixins.py#L846-L887) hashes text without encoding and assigns a 64-character SHA-256 to a 40-character field; these are conditional runtime incompatibilities, not executed failures. Adopt the small relationship graph and source-bound correction events. Defer service deployment until dependency, permission and persistence tests exist. No tests/CI were found; legacy pins and a 2022 head are maintenance signals, not proof of vulnerabilities. Reject configuration/data exports and boolean flags presented as enforced confidentiality.

## Three development gates

**1. Rigorous core and intake, this slice.** The independently inspected Atlas baseline is `3612e5f512ecdf6bd721e2db25d43bdd1bb3ec68`. Its 90 tests, demo consistency check and four CLI cases passed locally. Additional original fictional witnesses nevertheless reproduced three gaps: [ambient Decimal settings](https://github.com/Albertito-AI/court-submission-integrity/blob/3612e5f512ecdf6bd721e2db25d43bdd1bb3ec68/court_integrity/engine.py#L365-L372) changed arithmetic, formatting or exceptions; [unsupported pinpoint tokens](https://github.com/Albertito-AI/court-submission-integrity/blob/3612e5f512ecdf6bd721e2db25d43bdd1bb3ec68/court_integrity/intake.py#L214-L224) such as `12A` or seven-digit numbers were truncated into shorter locators; a bounded 5,000-digit JSON integer [escaped as `ValueError`](https://github.com/Albertito-AI/court-submission-integrity/blob/3612e5f512ecdf6bd721e2db25d43bdd1bb3ec68/court_integrity/__main__.py#L28-L39). These are independently reproduced Atlas defects, not defects caused by the external repositories. The repaired runtime passed independent local acceptance: 100 tests, the recorded demo, four CLI cases and exact rollback/reapply. See the [dated validation record](../VALIDATION_2026-11-15.md); hosted integration is established separately by actual pull-request checks.

The gate requires full-report invariance under hostile Decimal contexts while preserving caller state, complete-token pinpoint recognition with safe abstention and preserved ordinary positives, and documented invalid-input errors without output artefacts for oversized JSON integers. Preserve `HUMAN_REVIEW_REQUIRED`, `filing_decision: NONE` and no truth certification. Existing tests alone are insufficient: add negative witnesses, independent review, exact rollback/reapply and actual candidate CI acceptance. Comparative lessons support this discipline: go-documents exposes boundary-order concerns, while CaseRank, atjbot and the Swing prototype show why caught failure must not resemble success.

**2. Permitted, versioned authority resolver next.** Before network retrieval, establish source permissions, jurisdiction/profile scope and retention rules. Preserve original bytes, derivative text, source URL, publication/effective/retrieval dates, digest, exact page/paragraph span and supersession state. Resolve each citation to that specific version; separate syntax, existence, pinpoint match and proposition support. Test changed/deleted sources, duplicate identifiers, incomplete extraction, unsupported locators and explicit unavailable outcomes. TNA, the dated calculator, ngm and the retrieval projects inform these requirements. No copied corpus, live authority resolution or legal-currentness claim is delivered by this review.

**3. Source-bound correction and independent workflow evaluation later.** Corrections must retain the original input, proposed change, supporting source, actor/reason, review decision and resulting version. Evaluate realistic synthetic workflows with independent reviewers using predefined measures: false-success rate, unsupported-citation rate, abstention quality, source-location accuracy and correction traceability. Test binary preservation, changed evidence, missing pages and ambiguous versions; add object-level permissions only if multi-user functionality is separately authorised. Completion means the declared checks passed, not filing acceptance, admissibility, substantive truth or a court decision. Automated merits ranking, outcome prediction and guarantees of adoption remain outside the proposed work.

