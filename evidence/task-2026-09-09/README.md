

## Review amendment — 2026-09-09

Read [the reproduced findings, corrections and current checks](../review-2026-09-09/README.md)
before the historical day-2 counts below. Review branch `review/day-two-20260909`;
amendment targets the existing day-2 PR, not main. No owner/measurement gate closes.

# EN-D02 verification — 2026-09-09

Base: head of `task/priority-one-20260908` (PR #7). Deliverable: the zero-solar case of the existing
thermal model — [`--night-table`](../../analysis/thermal_bias.py), the
[night table](../../analysis/output/thermal_bias_night_table.csv), six
[`NightClearSkyTests`](../../analysis/tests/test_thermal_bias.py) and a
[results section](../../analysis/thermal_bias_results.md). Authoritative status: [SPRINT_TASKS.csv](../../docs/SPRINT_TASKS.csv).

No new physics and no new assumption: `run_sweep` is called with `g_values=[0.0]` and the same
`T_sky_offset`. The daytime table and figure are byte-unchanged (asserted below). Everything remains
SIMULATION / pending lab data; no field number is claimed.

## Commands, as `research-checks` runs them (repo root on `PYTHONPATH`, as the runner has it)

| Command | Observed |
| --- | --- |
| `python -m compileall -q analysis` | exit 0 |
| `python -m unittest discover -s analysis/tests` | Ran 35; **2 failures, both pre-existing** (see below) |
| `python -m unittest analysis.tests.test_thermal_bias` | Ran 11, OK — 5 day-1 + 6 new |
| `python analysis/check_literature_coverage.py` | exit 0 |
| `python analysis/thermal_bias.py --no-figure` | exit 0; writes day table and night table |
| `git diff --quiet HEAD -- analysis/output/thermal_bias_table.csv analysis/figures/thermal_bias.png` | exit 0 — daytime outputs byte-unchanged |

The two failures are `test_deployment_incomplete_schedule_fails_before_data_access` and `test_deployment_missing_data_is_access_error_not_traceback` in `test_metrics_cli`
(exit code 1 where 2 is expected). They reproduce identically on the untouched day-1 branch in this
environment (`Ran 29 tests in 2.012s` there) and that branch is green
in CI, so they are an artefact of this sandbox's process environment, not of this change. Not
diagnosed further here; nothing in this task touches `compute_metrics` or its CLI.

## What the model says at G = 0

V0 baseline box: -4.028 °C calm, -1.390 °C at 5 m/s (cold bias). V1 shield -0.012 °C, V2 aspirated -0.005 °C.
Daytime V0 at 1000 W/m² calm, for contrast: +22.664 °C. The tests assert sign, sign reversal vs day,
shield < box in magnitude, painted control == dark box, and monotone decrease with wind — never a
magnitude typed by hand.

Why it matters for the project: the error a field co-location must resolve is sign-changing over the
diurnal cycle, so the co-location plan (EN-S09B, owner-gated) needs 24 h coverage, not midday.
