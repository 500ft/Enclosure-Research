# Intake evidence correction — test report

Date: 2026-09-11. Base: `182cb1f7bfa7905c09dc465cc559267d416f16c5`.
Branch: `fix/evidence-gaps-20260911`. Local correction only; no push or merge.
Execution used execute-and-test and quality-gates. No standalone typechecker or
linter exists in this repository; no new toolchain was claimed or installed.

## Reconciliation

| Work item | Evidence actually present | Disposition |
| --- | --- | --- |
| Draft protocol / EN-R01 | `docs/COLOCATION_PROTOCOL.md`, owner-session packet | Preparation complete; PI approval and freeze are not complete |
| Executable intake / EN-R02 | Existing `analysis/colocation_intake.py`, corrected metadata boundary, delegating `analysis/intake_gate.py`, both test files | Software verification complete; not inferred from protocol text |
| Actual co-location validation / EN-R03 | No actual pilot CSV or authenticated equipment/calibration/permission supplied | Blocked; no physical validation performed |

EN-D03 now cites the existing executable and its tests in its deliverable field.
Earlier rows are retained, and the CSV was parsed to confirm all 13 columns,
unchanged pre-EN-D03 row values and blocked EN-R03. No dataset/register values or
thermal results were invented or overwritten.

## Red → green evidence

Baseline: 48 analysis tests passed; compile, 26/26 literature coverage, day/night
table reproduction and presentation checks passed. The requested filename was
absent, but the canonical co-location implementation already checked raw hashes,
provenance declarations, intended sampling/exposure coverage and synthetic status.

Tests were added before the parser/wrapper changes. Command:

```sh
python -m unittest analysis.tests.test_colocation_intake.IntakeTests.test_nonstring_window_timestamps_are_diagnostic_input_errors analysis.tests.test_intake_gate -v
```

It exited 1: non-string `window_start`/`window_end` raised `AttributeError` from
`value.endswith`, and the compatibility CLI returned `No module named
analysis.intake_gate`. The final pre-implementation run reported 4 test methods,
31 assertion failures and 10 timestamp-type errors (subtests include both missing
module and output-equivalence failures). An initial test-helper issue that indexed
missing failure results was corrected before that run; no assertion was weakened.

Minimal correction: validate both metadata timestamp types before parsing; delegate
the requested module name to canonical `evaluate`/`main`. All 52 analysis tests
then passed. No thermal criterion changed.

## Acceptance coverage

| Criterion | Test evidence | Result |
| --- | --- | --- |
| Malformed window timestamp types fail diagnostically | `test_nonstring_window_timestamps_are_diagnostic_input_errors`; CLI timestamp-type case | PASS; ValueError / exit 2, no traceback |
| Both documented module CLIs agree | Every `IntakeGateCliTests.run_case` checks return code, stdout and stderr equality | PASS |
| Reject bad raw hash, headers/schema, metadata, duplicate/off-grid/outside/naive/out-of-order timestamps and nonfinite weather | `test_bad_hash_schema_metadata_and_schedule_are_rejected` | PASS; exit 2 |
| Reject deficient paired, illuminated or low-solar coverage even with physical label | `test_declared_physical_incomplete_coverage_is_rejected` | PASS; INCOMPLETE / exit 2 |
| Synthetic-only never validates physical results | `test_synthetic_only_and_declared_physical_review_only` and existing synthetic test | PASS; exit 3; validates_thermal_model false |
| Physical label grants review eligibility only | Same routing test uses deliberately relabeled generated fixture | PASS; REVIEWABLE_PILOT / exit 0; validates_thermal_model false |
| Missing finite temperatures and excessive uncertainty do not pass | Existing `IntakeTests` | PASS |

All fixtures are generated in temporary directories. Even the physical-labeled
case is synthetic test data, not an acquired pilot. The CLI cannot detect dishonest
labels or authenticate identity/calibration/permission from strings and hashes.

## Full local CI-equivalent gates

Run from the repository root with existing `python` (3.11 environment):

```sh
python -m compileall -q analysis
git diff --check
python -m unittest discover -s analysis/tests -v
python analysis/check_literature_coverage.py
python analysis/thermal_bias.py --no-figure --table /private/tmp/enclosure-correction-day-20260911.csv --night-table /private/tmp/enclosure-correction-night-20260911.csv
diff -u analysis/output/thermal_bias_table.csv /private/tmp/enclosure-correction-day-20260911.csv
diff -u analysis/output/thermal_bias_night_table.csv /private/tmp/enclosure-correction-night-20260911.csv
python tools/check_presentation.py . 'Sensor Enclosure Thermal Design' sensor-enclosure-thermal-design
python tools/test_presentation.py
```

All exit 0: compile/whitespace clean, 52 analysis tests passed, 26/26 literature
coverage, both regenerated tables byte-identical, presentation checker reports
zero issues (65 local links; nine external links not fetched), four presentation
negative-control tests passed. Regenerated tables were written outside the
repository so committed model outputs remain unchanged.

## Remaining external gates

EN-S02, EN-S09B, EN-S11 and EN-R03 remain blocked. The owner-session packet is
prepared, not sent or scheduled. Actual PI approval, equipment/site inventory,
calibration and uncertainty records, prospective protocol freeze, authorized lab
acquisition and authenticated evidence review remain necessary. As-built model
uncertainty and a prospectively registered application tolerance are unavailable;
the simulated temperature ranges are not acceptance bands.

Deviation: reused the existing implementation instead of duplicating its policy.
No license, research result, real export, outreach, push or merge was changed.
