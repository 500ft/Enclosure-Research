# Fresh baseline — 2026-09-05

All commands run in `/Users/redhose/Developer/research-sprints/2026-09-05/Enclosure-Research`.
Source `c8c941dabd02541b3f3bfd67dc0edbc0517e6be9`, branch
`sprint/evidence-integrity-20260905`, remote
`https://github.com/500ft/Enclosure-Research.git`. `git status --short` empty before
checks. No AGENTS.md found in the checkout or the intervening parent directories.

Runtime: Python 3.11.8 (conda-forge; Clang 16.0.6), numpy 2.1.1, pandas 2.2.3,
matplotlib 3.10.1. Runtime query:

```bash
python -c 'import sys,importlib.metadata as m; print(sys.version); print({p:m.version(p) for p in ["numpy","pandas","matplotlib"]})'
```

| Command | Exit | Selected observed output |
|---|---:|---|
| `git rev-parse HEAD` | 0 | `c8c941dabd02541b3f3bfd67dc0edbc0517e6be9` |
| `python -m py_compile analysis/compute_metrics.py analysis/analyze_deployment_logs.py analysis/check_literature_coverage.py analysis/thermal_bias.py` | 0 | no output |
| `python -m compileall -q analysis` | 0 | no output; whole-directory CI compile also passed |
| `python analysis/check_literature_coverage.py` | 0 | Bibliography entries: 26; Per-paper analyses: 26; Coverage complete. |
| `python analysis/thermal_bias.py --no-figure` | 0 | wrote analysis/output/thermal_bias_table.csv; sensitivity baseline V0 19.4/V1 3.0, painted V0 4.5 |

No baseline behavioral tests, typecheck, or lint command are configured in CI.
These checks establish execution, not physical thermal accuracy.

## Complete duplicate reproduction

```bash
python -c 'from analysis.compute_metrics import compute_metrics,parse_timestamp; a=parse_timestamp("2026-04-20T00:00:00"); b=parse_timestamp("2026-04-20T00:05:00"); print(compute_metrics([(a,20,19),(a,20,19),(b,21,20)],5))'
```

Exit 0, output:

```text
Metrics(count=3, expected_count=2, completeness=1.5, bias=1.0, mae=1.0, rmse=1.0, correlation=1.0, drift_per_day=0.0)
```

Status: reproduced failure. Three observations are not three distinct scheduled
opportunities. This does not establish that the historical 91.4% is incorrect.

## Source-backed boundaries

`analysis/analyze_deployment_logs.py` uses first/last observed timestamps and
`OBSERVED_CADENCE_MIN=6.0` for completeness. Actual intended cadence/window and
private exports are unavailable here; field rates are reported but unverified.
`analysis/thermal_bias_results.md` sensitivity matches live model output. Dark vs
shield changes finish and several other assumptions; it does not identify the
incremental shielding effect alone.
