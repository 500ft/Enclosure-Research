# Enclosure: six-day evidence-integrity sprint

## Separate CAD phase — added 2026-09-06

Individual mechanical work orders now live in [CAD_PLAN.md](CAD_PLAN.md), with their own authoritative [CAD_TASKS.csv](CAD_TASKS.csv). They are additional, unexecuted work outside this original 30-hour integrity sprint. Existing physical-readiness and publication gates remain open until their actual evidence arrives.

Prepared 2026-09-05. Mode: plan and execute. Budget: 30 focused hours in six
workload days; these are not promises of unattended work or lab turnaround.
Status is authoritative only in [SPRINT_TASKS.csv](SPRINT_TASKS.csv).

## Outcome and baseline

Publication-state update (2026-09-06): the owner authorized local commits, branch
pushes, and pull requests for this sprint. This does not authorize deployment,
research publication, outreach, spending, or any blocked physical/data action.

Give a reviewer a reproducible reliability-analysis workflow that cannot inflate
scheduled availability by counting duplicate records, and a thermal comparison
that does not confuse painted-surface effects with shield effects. This sprint
can validate software accounting and correct analytical interpretation; it cannot
establish field accuracy or confirm the historical deployment denominator.

- Canonical sprint checkout: `/Users/redhose/Developer/research-sprints/2026-09-05/Enclosure-Research`.
- Remote: `https://github.com/500ft/Enclosure-Research.git`.
- Branch: `sprint/evidence-integrity-20260905`.
- Base: `c8c941dabd02541b3f3bfd67dc0edbc0517e6be9`; tree clean before baseline.
- Original checkout is not being edited. No commits, pushes, raw-data publication,
  spending, or outreach are performed in this workstream.
- Baseline evidence: [baseline.md](../evidence/sprint-2026-09-05/baseline.md).

## Verified gaps, not imported audit assumptions

1. Reproduced failure: [compute_metrics.py](../analysis/compute_metrics.py) returns
   1.5 completeness for three paired rows occupying two five-minute slots.
2. Verified implementation: [analyze_deployment_logs.py](../analysis/analyze_deployment_logs.py)
   divides row count by observed first-to-last span and an unconfirmed cadence;
   missing edge intervals and duplicate records are not protected.
3. Verified analytical sensitivity: the existing model predicts 19.4°C dark-box,
   4.5°C painted-box, and 3.0°C shield rise at 1000 W/m² and 0.5 m/s. These are
   model outputs, not measurements or isolated shielding effects.
4. Reported but unverified: historical 91.4% completeness, 95.7% upload success,
   outdoor deployment identity, and raw-log content. Required external exports,
   deployment intent, cadence, clock provenance, and reference measurements are
   unavailable in this checkout. No historical numeric correction will be guessed.
5. Verified tooling: CI compiles analysis, checks 26/26 bibliography coverage, and
   runs the thermal model. No behavioral test suite or type/lint command exists.

## Scope and contract

Must-haves: tested unique-slot availability accounting; explicit intended start,
exclusive end, cadence, and clock consistency; separate delivered, valid-sensor,
and reference-paired availability; clear missing-data states; CLI/integration
checks; corrected analytical narrative; a review packet with source and command
evidence. Retain per-observation bias/MAE/RMSE definitions, and label that
denominator separately from scheduled availability. Off-grid records do not
silently fill a slot; any allowed timestamp tolerance must be explicit and less
than half the cadence. Do not clamp impossible percentages to 100%.

Excluded: new CHT/CFD, sensor purchases, fabricated data, recalculation of private
field metrics without the source/provenance, physical experiments without access,
and new literature expansion. Packaging means exercising the existing Python CLI
from a separate directory, not inventing a package or publishing a release.

Owner dependency starts Day 1: confirm device/firmware, intended deployment
start/end (timezone), configured cadence, reset semantics, authorized raw-data
access, physical baseline finish/geometry, and reference instrument/access.
An agent prepares the checklist; only Owner/External can supply or approve it.
Critical path: EN-S01 → EN-S03 → EN-S04 → EN-S05 → EN-S07 → EN-S08 → EN-S10.
The private-log path EN-S02 → EN-S09 is independently blocked, not a reason to
hold up software corrections.

## Allocation

| Day | Hours | Primary deliverable |
|---|---:|---|
| 1 | 5 | Baseline, this plan, owner provenance checklist |
| 2 | 5 | Failing regressions and unique-slot correction |
| 3 | 6 | Deployment integration, honest narrative, CI |
| 4 | 4 | Consumer CLI proof and frozen candidate identity |
| 5 | 6 | Bounded software counterexamples and provenance-gated field rerun |
| 6 | 4 | Reviewer packet and feedback/pending record |
| Total | 30 | No physical-validation claim included |

## Ordered daily tasks

### Day 1 — baseline and early dependency (5 h)

- **EN-S01, P0, Agent, 4 h, no dependency.** Inspect existing README, CI,
  requirements, both reliability scripts, thermal model/results, and manuscript.
  Save this new roadmap, new task ledger, new progress log, and baseline evidence.
  Verify with `git status --short`, `git rev-parse HEAD`, `python --version`,
  `python -m compileall -q analysis`, `python analysis/check_literature_coverage.py`,
  `python analysis/thermal_bias.py --no-figure`; retain command/status/output.
  Done when the failure has a complete reproducible input and model comparison
  is verified from the live code, not merely the audit text.
- **EN-S02, P0, Owner, 1 h, depends EN-S01.** Agent prepares new
  `docs/DEPLOYMENT_PROVENANCE_REQUEST.md`; Owner supplies the listed facts and
  authorizes data access. Manual verification: timestamp/timezone/window/cadence
  and data checksum/access route have identified sources, not inferred values.
  Done when confirmed metadata exists; prepared request alone does not close it.

### Day 2 — correctness (5 h)

- **EN-S03, P0, Agent, 1.5 h, depends EN-S01.** New
  `analysis/tests/test_compute_metrics.py`: duplicate slots, missing edges,
  invalid cadence/window/timezones, off-grid records, missing/nonfinite channels,
  empty inputs, and unchanged finite residual metrics. Run
  `python -m unittest discover -s analysis/tests -v`; capture the failing baseline
  before implementation. Done when failures target the intended contract.
- **EN-S04, P0, Agent, 3.5 h, depends EN-S03.** Change
  `analysis/compute_metrics.py`; introduce a shared slot-accounting helper if
  necessary (new file must be labeled in the implementation record).
  Acceptance: unique occupancy numerator / expected scheduled slots; no guessed
  edge boundaries, no implicit timestamp rounding, no infinity/NaN inflation;
  finite paired residuals retain bias/MAE/RMSE meaning. Run the same tests and
  retain red/green outputs. Done when each defect and counterexample passes.

### Day 3 — integration and interpretation (6 h)

- **EN-S05, P0, Agent, 2 h, depends EN-S04.** Change
  `analysis/analyze_deployment_logs.py`; new integration tests in
  `analysis/tests/test_deployment_metrics.py`. Explicit schedule controls the
  denominator; absent provenance yields unavailable completeness rather than a
  new definitive field percentage. Empty target windows remain representable.
  Test reported-row delivery versus channel availability. No raw-log regeneration
  without EN-S02. Verify with full unittest discovery and CLI `--help`.
- **EN-S06, P0, Agent, 2.5 h, depends EN-S01.** Update existing README,
  `docs/results.md`, `analysis/thermal_bias_results.md`, and
  `paper/manuscript_v1.md` so the painted baseline is prominent and prospective
  measurements are not described as completed. Add new
  `docs/RELIABILITY_METRICS.md` documenting exact CLI and denominator semantics.
  Preserve historical field values as provisional, not silently recalculated.
  Verification: reviewer traces 19.4/4.5/3.0 to model sensitivity and identifies
  all historical rates as unconfirmed. Retain model output and narrative diff.
- **EN-S07, P0, Agent, 1.5 h, depends EN-S05.** Add unittest execution to
  `.github/workflows/ci.yml` and CONTRIBUTING; run all real gates. No configured
  type/lint check exists; do not claim one ran. Done when local CI-equivalent
  commands pass and the workflow includes behavioral regressions.

### Day 4 — delivery and candidate freeze (4 h)

- **EN-S08, P0, Agent, 4 h, depends EN-S06/07.** New synthetic CLI fixture under
  `evidence/sprint-2026-09-05/`; invoke `analysis/compute_metrics.py` using an
  absolute script path from outside the checkout, with explicit window/cadence.
  Record source-file hashes, command, artifact hashes, baseline/candidate output,
  and selection rules for Day 5 before evaluating additional cases.
  Done when an independent reviewer can run the CLI without private data.

### Day 5 — bounded evaluation (6 h)

- **EN-S09A, P0, Agent, 3 h, depends EN-S08.** Evaluate deterministic additional
  schedule/duplicate/edge cases under a frozen selection procedure and prewritten
  expectations. Save fixture provenance and disagreements. These synthetic
  developer checks are not independent scientific validation. If they prompt
  fixes, relabel them development inputs and freeze a new candidate.
  Done when outcomes and limitations are retained, not just a larger test count.
- **EN-S09B, P1, External, 3 h, depends EN-S02/05.** With authorized raw logs and
  confirmed metadata, rerun deployment summaries into a new versioned output
  directory and reconcile historical versus scheduled rates. Manual review
  includes edge gaps, clock discontinuities, duplicate upload/reset semantics,
  and missing sensor/reference availability. Blocked until EN-S02; no invented
  path or command presented as an executed field campaign.

### Day 6 — review packet (4 h)

- **EN-S10, P0, Agent, 3 h, depends EN-S08/09A.** Assemble new
  `docs/REVIEW_READY.md`; rerun compile, unittest, literature coverage, thermal,
  consumer CLI, and `git diff --check`. Record final uncommitted/commit status,
  regression evidence, intentional CLI changes, pending field work, and at most
  three remaining priorities. Done when must-have software evidence is linked.
- **EN-S11, P1, Owner, 1 h, depends EN-S10.** Request an independent human review
  using the prepared review request; reconcile feedback if available. External
  availability is not guaranteed. Done when feedback is recorded, otherwise
  explicitly pending. No message is sent by the agent without authorization.

## Overrun and follow-up policy

Drop EN-S09B field regeneration first when provenance is late; keep it blocked.
Defer elaborate additional sensitivity plots/CHT and extended parser cleanup.
Never drop duplicate/invalid-input protections, substitute inferred cadence for
configuration, or claim independence for development fixtures. Day 7 is optional
up to 4 additional focused hours for reviewer fixes; requires an explicit budget
extension. A software-only handoff is partial with respect to field validation.

Resume by reading the ledger/progress, rechecking the branch/tree, and taking the
next unblocked task. No work is scheduled to run after the active session ends.
