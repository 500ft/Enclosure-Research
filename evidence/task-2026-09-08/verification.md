# EN-D01 — first-class matched-finish control

Prepared 2026-09-08. Source base: `199cb5d38bc70af271b4e064d79d4d8415ff4630`.
Branch: `task/priority-one-20260908`. Candidate identity: containing commit,
reported by the PR; no self-referential commit hash. Repository:
`https://github.com/500ft/Enclosure-Research`.
Commands below run from repository root unless stated otherwise.

## Why this task is P1 and executable now

[Earlier review](../../docs/REVIEW_READY.md) keeps physical matched-finish
comparison open. [Model results](../../analysis/thermal_bias_results.md) call the
painted box a primary control, but baseline `build_variants()` returned only
V0/V1/V2: default CSV/plot omitted the control and the sensitivity print was
its only numerical output. This was verified from code and default execution,
not assumed from the earlier audit. The field denominator and CAD inventory
tasks still need owner-provided data; this correction needs none.

Task: promote the absorptance-matched box to the main analytical outputs.
Test: control invariants, all operating points, null solar intervention,
unchanged existing predictions, real exported CSV/PNG via CLI.
Done when: those tests and CI-equivalent checks pass, the default outputs contain
the control, and the remaining causal/physical limits are explicit.

## Runtime and baseline

`python3 --version`: Python 3.13.7. Initial `python3 -m unittest discover -s
analysis/tests -v` exited 1: missing pandas caused one import error and two
downstream CLI failures. This is not a reproduced product defect.

Existing `python` resolves to `/Users/redhose/ENTER/bin/python`, Python 3.11.8;
numpy 2.1.1, pandas 2.2.3, matplotlib 3.10.1. No dependency installation needed.
Configured identity: `500ft <153922251+500ft@users.noreply.github.com>`.

Before behavior edits:

| Command | Exit | Observation |
|---|---:|---|
| `python -m compileall -q analysis` | 0 | Compile passes |
| `python -m unittest discover -s analysis/tests -v` | 0 | 24 tests, 1.172 s |
| `python analysis/check_literature_coverage.py` | 0 | 26 entries, 26 analyses, complete |
| `python analysis/thermal_bias.py --no-figure --table ''` | 0 | Main table omits painted control; sensitivity prints 4.5°C |

No dedicated type checker, linter or package build is configured; do not infer
that these ran. CI compiles, tests, checks bibliography and executes the model.

## Test-first failure and correction

Added [five tests](../../analysis/tests/test_thermal_bias.py), then ran
`python -m unittest analysis.tests.test_thermal_bias -v` against unchanged
implementation: exit 1, **five failures** (0.650 s). Relevant outputs:

```text
AssertionError: 'V0P' not found ... Primary painted control is absent from the main sweep
AssertionError: 18 != 24
AssertionError: 'Painted closed-box control' not found ...
Ran 5 tests ... FAILED (failures=5)
```

Small change: copy V0 using `dataclasses.replace`, change absorptance to the
existing shield assumption 0.30, add ID/name/note, retain all other parameters.
Append without changing legacy positional V0/V1/V2 order. Sensitivity reuses
that control. Plot supports its color and redundant variant marker; console
explicitly says V0P versus V1 is not an isolated shielding effect.

## Green checks and reproducibility

| Command / procedure | Exit | Observation |
|---|---:|---|
| `python -m compileall -q analysis` | 0 | Compiles |
| `python -m unittest analysis.tests.test_thermal_bias -v` | 0 | 5 pass, 0.649 s |
| `python -m unittest discover -s analysis/tests -v` | 0 | 29 pass, 1.757 s |
| `python analysis/check_literature_coverage.py` | 0 | 26/26 complete |
| `python analysis/thermal_bias.py` | 0 | Regenerates default CSV and PNG |
| `python evidence/sprint-2026-09-05/evaluate_candidate.py` | 0 | Original 4 hashes match; 12/12 developer accounting cases pass |
| Legacy CSV comparison below | 0 | All 30 original rows exactly equal; 10 V0P rows added |
| `git diff --check` | 0 | No whitespace errors |

Final rerun after documentation changes: compile, 29 tests (1.746 s),
bibliography coverage, `python analysis/thermal_bias.py --no-figure`, and diff
check each exited 0. Ledger comparison confirms all 12 historical task rows
byte-preserved, one new EN-D01 row, and the original total still 30 hours.
An initial ad-hoc ledger check incorrectly expected 14 total rows and failed;
the corrected check derives the original count from git and compares each row,
rather than changing the actual ledger to satisfy that mistaken assertion.

The CLI test invokes the absolute script path with the current interpreter from
a newly created temporary directory, exports `bias.csv` and `bias.png`, asserts
V0P's presence and the causal warning, and checks a nonempty image. Generated
default PNG was also visually inspected: four legends/curves are legible and
axis labels do not overlap. PNG byte equality is not required across font builds.

Repeat legacy-row comparison (no writes):

```bash
python - <<'PY'
import csv, io, subprocess
from pathlib import Path
base = '199cb5d38bc70af271b4e064d79d4d8415ff4630'
old_text = subprocess.check_output(['git', 'show', base + ':analysis/output/thermal_bias_table.csv'], text=True)
old = list(csv.DictReader(io.StringIO('\n'.join(old_text.splitlines()[1:]))))
new = list(csv.DictReader(io.StringIO('\n'.join(Path('analysis/output/thermal_bias_table.csv').read_text().splitlines()[1:]))))
assert [r for r in new if r['variant_id'] != 'V0P'] == old
assert len(old) == 30 and len(new) == 40
print('30 unchanged legacy rows; 10 new painted-control rows')
PY
```

Hashes after regeneration (`shasum -a 256`; emitted a locale fallback warning
but exited 0):

| Path | SHA-256 |
|---|---|
| `analysis/thermal_bias.py` | `d6c2f1e6b901d277241690eea0879a404634f0ed8ebcf6e33a32e5401afa787d` |
| `analysis/tests/test_thermal_bias.py` | `69eb77b67cd055800e33722a68120d5d79ce11bf1c5e5489f675b7a6e4343b11` |
| `analysis/output/thermal_bias_table.csv` | `6f6e42ae6a5d7688424e670c30d6fa84496da24430eef158b6db8f92c96a30c4` |
| `analysis/figures/thermal_bias.png` | `e896b361bd5c992035abd436d81209d9fcb7bfd0429c8704d1e7f86b7f64b08e` |

## Interpretation and remaining blockers

At 1000 W/m², 0.5 m/s: V0 19.4162°C, V0P 4.4796°C, V1 3.0025°C.
The 1.4771°C difference is a **whole-system model contrast**. V0P/V1 still
differ in geometry, shielding, coupled internal heat, convection, sky view and
preheated-air treatment. Equal optical properties are assumed, not measured.
At zero solar flux, V0 and V0P match exactly, as required when only absorptance
is changed. This is a mathematical null intervention, not a validated night model.

No new prior-art, hardware, CAD, reference observations, deployment logs or
held-out scientific data were used. Tests are developer checks, not independent
research validation. Human feedback remains pending. Owner inventory/provenance,
physical matched-finish comparison and joint uncertainty still block a physical
validation verdict. Historical rendered publication packages are not regenerated.
The two-hour ledger estimate is scope budgeting, not measured elapsed effort.
