# Regression evidence — 2026-09-05

Working directory: canonical sprint checkout in [baseline.md](baseline.md).
Runtime: Python 3.11.8. No private data used; all inputs are synthetic.

## EN-S03 → EN-S04: original API to scheduled accounting

Command before behavior changes:
`python -m unittest discover -s analysis/tests -v`

Exit 1. 15 test methods ran: failures=3, errors=20 (subtests count separately).
Meaningful existing-behavior failures: no ValueError for cadence without intended
window; CSV reader discarded two timestamped deliveries lacking finite pairs;
empty data raised ZeroDivisionError; invalid timestamp error omitted row number.
New explicit-window tests failed because the original API had no window_start.
The independent three-row reproduction in baseline.md returned completeness 1.5.

After the smallest shared scheduling/metric correction:

`python -m compileall -q analysis && python -m unittest discover -s analysis/tests -v`

Exit 0: 15 tests passed in 0.002 seconds. The duplicate/missing-edge fixture now
occupies two of four explicitly intended slots (0.5), while finite-pair bias,
MAE, and RMSE retain their per-observation definitions. Extra channel fields
distinguish delivery 1.0, finite sensor 0.5, and paired availability 0.25 in a
four-slot missing-channel fixture. No estimate was clamped to 1.0.

These are developer regression checks, not held-out field evaluation.

## Deployment integration and consumer boundary (completed 2026-09-06)

Before deployment changes, `python -m unittest discover -s analysis/tests -p
test_deployment_metrics.py -v` exited 1: four tests, failures=1/errors=3. Two
records six minutes apart returned 200% without configuration; empty selected
window raised IndexError. After integration all 19 tests passed (exit 0).

Five consumer-CLI tests then exposed one failure: missing external data produced
a traceback/exit 1. Corrected access/value errors now exit 2 before outputs are
created. The full suite passes 24 tests. Empty selected windows and standalone
header-only accuracy files are supported; the full descriptive-plot exporter
explicitly rejects entirely empty source logs with an actionable error.
Final repeated commands and exact outputs: [final-checks.md](final-checks.md).
