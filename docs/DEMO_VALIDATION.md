# Public demonstration verification | 1 November 2026

Action: `CSI-DEMO-20261101-1`. Owner-requested demonstration, profile discovery and
initial non-binding collaboration invitations. This is not scheduled-run credit.

## Exact baseline and change

Dedicated launch: `236c8b02ab536f7b99959bac2b4f8430997bb7b8`, PR #1.
This work resumes the already open continuous-improvement documentation branch,
head `627ed3a0cddd80d750004193ee81f9f47bb50133`, rather than creating a competing
implementation. The actual final head, merge and tree are recorded in PR #2.

The runtime engine, intake parser, original fixtures and rights are unchanged.
New demonstration recording and three regression tests bind public summaries to
actual fictional execution. README navigation, demonstration, capability and
collaboration guides explain current behaviour separately from proposed features.

## Checks actually run

CPython 3.13.5/Linux; already installed pypdf 5.9.0. All **90 unittest cases passed,
with no skips** after adding the three demonstration checks. The original suite
also passed all 87 cases before that change. Four CLI workflows generated local
reports. The reproducibility command compares fresh execution with the committed
summary, including each input's SHA-256, engine version and package digest.

```sh
python -m examples.record_demo --check
python -m unittest discover -s tests -v
```

The public adverse summary contains six CHECK_FINDING, two REVIEW_CANDIDATE and
nineteen UNRESOLVED items. Matched and unknown cases retain three and five unresolved
notices respectively. TXT intake recognises four candidates and retains one check
finding and twelve unresolved notices. All four keep human review required,
no automatic filing decision and no truth certification. These are fixture outcomes,
not a statistical accuracy or operational-efficiency study.

## Failed and unverified checks

A local Chromium attempt to navigate to the generated HTML report was blocked
with `net::ERR_BLOCKED_BY_ADMINISTRATOR`. No policy bypass was attempted. No screenshot,
visual browser pass, mobile-layout pass, accessibility or cross-browser certification
is claimed. The GitHub-readable walkthrough presents program output as text and
tables; local HTML reports remain reproducible through the documented commands.

No hosted CI, external model, paid service or real court input was used. Independent
human legal evaluation, source authentication, measured court-time savings and
production safety remain unverified. Internal AI-assisted review is not independent
human review. Existing historical validation failures remain preserved.

## Next observed outcome

The next useful evidence is a qualified response describing a real workflow and
its evaluation requirements, followed by an authorised independent fictional-data
assessment. Invitations alone are not adoption. The source-resolution development
gate and the separately configured recurring review remain in place.
