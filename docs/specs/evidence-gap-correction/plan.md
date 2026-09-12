# Intake evidence correction

Status: done (bounded software/documentation correction only) — 2026-09-11

Authoritative task ledger: `docs/SPRINT_TASKS.csv`; this is a bounded execution
checklist, not a replacement task register. Baseline is clean main
`182cb1f7bfa7905c09dc465cc559267d416f16c5`; branch `fix/evidence-gaps-20260911`.

Scope: verify the existing canonical intake, repair demonstrated input-boundary
failures, provide the requested filename as a delegating module entrypoint, and
reconcile preparation/software/physical validation explicitly. No new thermal
acceptance bands, results, raw exports, license edits, outreach or approvals.

## Gates (from .github/workflows/ci.yml)

No standalone typechecker or linter is configured. Compile is the syntax gate;
`git diff --check` is whitespace checking, not a substitute typechecker/linter.

1. `python -m compileall -q analysis`
2. `git diff --check`
3. `python -m unittest discover -s analysis/tests -v`
4. `python analysis/check_literature_coverage.py`
5. `python analysis/thermal_bias.py --no-figure --table /private/tmp/enclosure-correction-day-20260911.csv --night-table /private/tmp/enclosure-correction-night-20260911.csv`
6. `diff -u analysis/output/thermal_bias_table.csv /private/tmp/enclosure-correction-day-20260911.csv` and equivalent night-table diff.
7. `python tools/check_presentation.py . 'Sensor Enclosure Thermal Design' sensor-enclosure-thermal-design` and `python tools/test_presentation.py`.

## Execution

- [x] Baseline: compile, 48 analysis tests, 26/26 literature coverage, unchanged
  regenerated day/night tables, presentation checker and 4 negative controls pass.
- [x] Write regression tests for diagnostic malformed timestamps and both module
  CLIs (hash, malformed CSV/metadata, coverage, synthetic isolation, physical-label
  review-only). Red: 4 test methods failed (10 timestamp-type subtest errors and
  absent compatibility module); tests preceded code changes.
- [x] Fix demonstrated parser boundary and add delegating `analysis/intake_gate.py`;
  preserve `analysis.colocation_intake` as canonical implementation. Compile,
  whitespace and 52-test suite pass after the minimal fix.
- [x] Correct EN-D03 deliverables and append separate reconciliation rows for draft
  protocol, tested executable, and blocked actual pilot validation; prepare owner
  session packet distinguishing unanswered decisions from approval. Ledger parsed;
  pre-EN-D03 rows unchanged, EN-R03 remains blocked.
- [x] Full CI-equivalent verification and evidence report: all commands in
  `test-report.md` passed. Local configured-identity commit contains this report;
  no push or merge; actual PI/equipment/calibration/acquisition remain blocked.
