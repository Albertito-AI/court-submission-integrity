# Progress and next gates

## CSI-20261115-RELIABILITY | Core reliability and comparative learning

Three independently reproduced defects were repaired: caller Decimal settings
affecting bounded arithmetic, unsupported pinpoint tokens becoming shorter
locators, and a JSON integer-conversion error escaping the CLI input contract.
The runtime now uses a complete local arithmetic context, conservative complete-
token recognition and explicit invalid-input handling.

Observed local acceptance: 100 tests without skips, four fictional CLI workflows,
the recorded demonstration, distinct agent review and exact rollback/reapply.
The new regressions fail against the original runtime. The
[dated validation record](VALIDATION_2026-11-15.md) records the environment,
independent checks, recognition trade-offs and limits. Integration status is
established by the actual pull request and associated workflow runs.

The [fourteen-repository review](research/2026-11-15-repository-comparison.md)
and pinned source index distinguish useful design concepts, conditional static
findings and unsuitable transfers. No upstream code was executed or copied.
Future work remains a permitted, versioned authority resolver, followed by
source-bound correction and independent workflow evaluation. Legal accuracy,
court readiness and an efficiency multiplier remain unverified.

## CSI-20261101-DEDICATED-03 | Dedicated repository launch

**Owner:** Albert Tan Sin Hon. **Implementation/review:** AI-assisted engineering.
**Beneficiary:** prospective researchers and court-technology evaluators needing
an inspectable, reproducible submission-review prototype.

The owner requested a separate repository and created
`Albertito-AI/court-submission-integrity`. This action publishes the prepared
`0.1.0a1` source at that repository's root. It corrects the earlier substitution
of a project folder in the profile repository. The earlier snapshot and original
private archive are preserved as provenance, not competing development locations.

**Acceptance:** complete runnable code, tests, fictional examples and documentation
on the new repository's main branch; exact uploaded-tree comparison; verified PR
merge; updated private launch record. See [PUBLICATION.md](PUBLICATION.md) and
GitHub's actual history for delivery evidence. No source release or merge is
inferred merely from a configured branch.

**Observed local checks:** 87 tests passed without skips on CPython 3.13.5/Linux;
four fictional CLI workflows completed. [Validation](VALIDATION.md) records scope,
environment and remaining limits. No implementation behaviour was changed by this
migration. Tests do not establish legal accuracy, adoption or reviewer efficiency.
No paid API, hosted CI, deployment, court outreach or new scheduler was initiated.
Albert's elapsed effort and commercial outcome remain unmeasured.

**Knowledge distinction retained:** source availability, textual correspondence,
substantive support and real-world truth remain separate. Source absence and
incomplete extraction must not become findings of falsity. A source hash does not
authenticate a document or a reviewer. No private research text is republished.

## Preserved earlier milestones

- `CSI-20261101-01`: initial local standalone alpha, fictional demonstrations and
  product design. Original private archive and detailed validation retained.
- `CSI-20261101-PUBLISH-02`: public research-hub snapshot, PR 36 in
  `Albertito-AI/Albertito-AI`, merge `a5181d571b1bf46cdee4a8b4a5ddf9af1c55f91a`.
  This was a folder publication, not creation of the required separate repository.

## Next bounded work

1. Engineering: implement one permitted, version-pinned authoritative-source
   resolver with exact identity, retrieval provenance and explicit unavailable
   states. Do not imply current-law or truth certification.
2. Authorised independent legal reviewers: construct a permitted held-out
   benchmark distinguishing quotation fidelity from contextual support, genuine
   disputes, alternatives and incomplete extraction. No invented human review.
3. Court/operator and engineering: only after separate evidence and permission,
   evaluate a specific local profile and read-only integration in shadow mode.

No milestone date, customer demand, funding, deployment or court approval is
established by publication. Existing rights and operational gates remain intact.

## CSI-CONT-20261101-1 | 1 November 2026 | Recurring court-operations improvement

Albert requested continuous upgrading towards demonstrated court usefulness.
The existing Academic GitHub Development automation was updated successfully,
without changing its daily flexible morning schedule, timezone or enabled state.
It now includes daily CSI checks and a Wednesday court-workflow checkpoint/report,
starting 4 November 2026, within existing priorities and shared capacity.
No duplicate task was created and no future execution or efficiency gain is claimed.

The dedicated launch was independently read back from GitHub as merged PR #1,
commit `236c8b02ab536f7b99959bac2b4f8430997bb7b8`. This is publication evidence,
not independent human evaluation. The [improvement protocol](CONTINUOUS_IMPROVEMENT.md)
records source-based work selection, accuracy/false-alarm checks, whole-workflow
human effort, independent evaluation gates, deferral reporting and stop criteria.
README navigation is updated; runtime, tests, rights and version are unchanged.

Validation for this documentation change: the 17 checked source, test, fixture
and boundary-document blobs matched exact main-branch identifiers; all 87 local
tests passed with no skips on CPython 3.13.5/Linux with pypdf 5.9.0. Four fictional
CLI workflows completed, and Python compilation passed. Changed Markdown links
and whitespace were checked. No hosted CI, model calls or court data were used.
Review was internal and AI-assisted. Independent benefit remains NOT_VERIFIED.

Next owner/action: the development task should complete a bounded authoritative-
source-resolution requirement/baseline; the Wednesday checkpoint must show evidence,
progress or a dated reason for deferral. Independent human evaluation and any
court shadow pilot retain their separate permission and readiness requirements.

## 22 November 2026: optional PDF parser security maintenance

The optional `pdf` extra now requires `pypdf>=7.1.1,<8`, replacing the range
that excluded current upstream parser fixes. The
[dated dependency record](DEPENDENCY_SECURITY_2026-11-22.md) contains the
advisory evidence, verified wheel hash and remaining parser-isolation boundary.
On isolated Linux/CPython 3.12.14 with pypdf 7.1.1, all 100 existing tests passed
without skips; the four CLI examples and recorded demonstration also passed.
These are fictional-data engineering observations. Existing installations need
an explicit parser upgrade; real-case use still requires the documented
isolation, rights and independent evaluation gates.
