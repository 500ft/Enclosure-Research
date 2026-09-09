# Enclosure night-case review — 2026-09-09

Review base: `11cf7218cb3e347953f2e301658b1f9365b16490`. Candidate is the containing commit / PR head.
Python 3.11.8 at `/Users/redhose/ENTER/bin/python`; all checks run from this
repository root unless the test explicitly creates an external temporary directory.

## Findings and amendments

Day 1's painted-box control is a useful computational comparison. Day 2 adds useful zero-solar scenarios, but the original printed summary used extrema as wind endpoints: at night the maximum is windy, not calm. The summary now indexes the actual minimum/maximum wind values. The CSV values were already correct.

The night conclusion was also too broad. With unchanged V0 geometry/load, changing sky temperature from 10 to 29 C at 30 C air changes calm-night bias from -4.028 to +0.566 C. This is an existing-model counterexample, not new physics or a measured cloudy-sky condition. Prose now calls day/night results conditional steady states, not a diurnal transient. V1 changes several parameters, so the comparison does not isolate sky-view causation.

Added three tests: actual calm/windy summary labels, opposite-sign sky-temperature control, and CLI regeneration of both tables from an external working directory without overwriting reference artifacts. Activated CI compares temporary day/night outputs against committed CSVs; the obsolete patch was removed. PR base filtering now includes the day-1 stack.

## Verification and boundaries

Original day-2 suite: 35 tests passed here. Revised suite: 38 passed; bibliography coverage 26/26, compile and table comparisons pass. The earlier two test_metrics_cli failures do not reproduce with Python 3.11.8 and PYTHONPATH=.; their historical report is retained, not asserted to be a current product bug. Solver physics, all committed CSV/PNG outputs, owner approval and lab status remain unchanged.

[Original-function counterexample output](counterexamples.json). New regression
inputs live in the tests; they are development material, not unseen scientific
or independent-human evaluation. No typecheck/lint task is configured; existing
suite, syntax and CI checks are used. Hosted status is recorded after push.

## Direction

Keep the painted control and signed cases. Next is owner-authorized co-location across measured weather, sky and load conditions. One 24-hour cycle is not general validation, and the model does not independently solve shield-plate nighttime cooling.
