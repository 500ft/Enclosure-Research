# Sprint progress

## 2026-09-05 — baseline and plan

Worktree: `/Users/redhose/Developer/research-sprints/2026-09-05/Enclosure-Research`.
Branch `sprint/evidence-integrity-20260905`; base
`c8c941dabd02541b3f3bfd67dc0edbc0517e6be9`. Initial tree clean. Original
checkout untouched. No commit/push/outreach performed.

Read the applicable execute-and-test and quality-gates skills, CONTRIBUTING,
README, CI, analysis scripts, results, and manuscript claim locations.
Baseline compile, literature coverage, and thermal execution passed. Duplicate
paired timestamp input reproduced completeness 1.5. Evidence is in
[baseline.md](../evidence/sprint-2026-09-05/baseline.md).

Saved six-day/30-hour plan and authoritative task CSV before behavior changes.
Current modifications are new sprint documentation/evidence only; running the
thermal model regenerated its existing table without a tracked numeric diff.
No type/lint command or behavioral suite exists in baseline CI; use standard
library unittest for regressions, adding no test dependency.

Next action: prepare the owner provenance request, then EN-S03 failing regression
tests after the parent presents the plan. Behavioral implementation has not begun.

## 2026-09-05 — scheduled-accounting correction

Parent presented plans and authorized continuation. Prepared owner checklist (not
sent). EN-S03 tests failed on original behavior, then EN-S04 corrected the
accounting. Fifteen regression tests and whole-analysis compile pass; see
[regressions.md](../evidence/sprint-2026-09-05/regressions.md). Existing positional
cadence-only calls now fail with an intended-window instruction. This deliberate
contract change prevents inferred edge denominators. Finite-pair accuracy remains
per observation; availability has unique delivery/sensor/paired numerators.

Next: EN-S05 deployment integration tests first. Historical field outputs remain
untouched. Branch/base unchanged; changes uncommitted.

## 2026-09-06 — software review packet

Resumed same branch/base and rechecked existing changes. Integration tests first
reproduced the missing-window crash and unconfirmed 200% rate; metadata-free
completeness is now null. Consumer tests then caught a missing-data traceback;
the exporter now reports actionable input errors before emitting files. Empty
selected windows are supported; entirely empty sources are explicitly rejected
by the full descriptive-plot exporter.

Added real unittest CI step. Compile, 24 tests, 26/26 bibliography coverage,
thermal execution, and diff checks pass. Exact outputs are in
[final-checks.md](../evidence/sprint-2026-09-05/final-checks.md). Source CLI ran
from `/private/tmp`: synthetic delivery/sensor/paired availability 0.75/0.5/0.25.
Candidate hashes and prewritten procedure preceded 12 additional deterministic
developer cases, all passing; not independent scientific evaluation.

Narrative now highlights painted control and withdraws unsupported completed
measurement, uptime, unattended-operation, and causal/exoneration language.
Historical reported figures are preserved as unverified. Raw exports, frozen
images, thermal CSV values, and rendered reports were not changed. Legacy
rendered reports are not a corrected publication package.

Bounded software lane complete; overall field-validation handoff partial.
EN-S02/09B await confirmed provenance/access and EN-S11 awaits human review.
Owner request prepared, not sent. No commits/push/publication/outreach. HEAD
remains c8c941dabd02541b3f3bfd67dc0edbc0517e6be9; nine tracked files modified plus
new tests/docs/evidence. Ledger estimates are planned hours, not claims of elapsed
calendar days. Next resume command, after checking status and reading ledger:
`python -m unittest discover -s analysis/tests -v`. Next external unblock:
[owner provenance checklist](DEPLOYMENT_PROVENANCE_REQUEST.md). No background
work is scheduled.
