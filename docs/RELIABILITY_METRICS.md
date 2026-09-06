# Reliability metric contract — 2026-09-05 correction

The raw field exports and intended configuration are external. Software tests
below use synthetic data; they do not correct or independently verify the
historical 91.4% or 95.7% values. No historical figures/PDFs are regenerated here.

## Denominators

Given intended first sample `start`, exclusive end `end`, and positive finite
cadence Δ, expected slots are `start + kΔ < end`, `k = 0,1,...`. Endpoints are
required, not inferred from observed rows. Missing beginning/end intervals stay
in the denominator. A partial final interval still has its scheduled start.

| Output | Numerator / denominator |
|---|---|
| delivery_completeness | Unique scheduled slots with a received record / expected slots |
| sensor_completeness | Unique slots with a finite sensor observation / expected slots |
| paired_completeness | Unique slots with a finite sensor and reference in the same record / expected slots |
| completeness | Compatibility alias for paired_completeness in compute_metrics.py; not uptime |
| count | Finite paired observations in the window, including duplicates and off-grid pairs |
| bias / MAE / RMSE | Mean residual / mean absolute residual / root mean square residual over those observations |

Accuracy remains observation-weighted and does not claim independent duplicates.
Missing/nonfinite channels remain received records but do not qualify the relevant
channel or pair. A header-only CSV is valid empty input: scheduled availability
is zero if a schedule exists; accuracy and unscheduled completeness are unavailable.
Invalid timestamps fail with CSV row number instead of being silently dropped.
Correlation and drift remain undefined (`nan`) when too few observations or no
variation makes their existing formula undefined.

Default matching is exact. `--slot-tolerance-seconds` permits only explicit
nearest-slot matching strictly less than half the cadence. Off-grid records and
duplicate accepted slot records are counted separately; no silent averaging,
flooring into arbitrary bins, or clamping to 100%. The configured first-sample
phase matters. A telemetry upload timestamp is not a sensing timestamp unless
the metadata establishes that correspondence. Use one device/stream per run;
multiple device IDs require separate schedules and analyses.

All timestamps and boundaries must use a consistent naive or timezone-aware
convention. Aware timestamps normalize to UTC; equivalent offsets count as one
slot. Naive timestamps do not establish their physical timezone. Cadence is
represented at microsecond resolution; sub-microsecond values are rejected.

## Reproducible standalone CLI (repository-contained synthetic data)

From repository root:

```bash
python analysis/compute_metrics.py evidence/sprint-2026-09-05/consumer.csv \
  --sensor sensor --reference reference --expected-interval-minutes 5 \
  --window-start 2026-04-20T00:00:00Z --window-end 2026-04-20T00:20:00Z
```

Expected: four expected slots; three delivered; two finite-sensor slots; one
paired slot; one duplicated slot record; one off-grid record. Availability is
0.75 / 0.5 / 0.25 respectively. The three finite in-window pairs retain bias,
MAE, and RMSE of 1. `completeness` is 0.25, not the received-row delivery rate.

Omit all schedule arguments to report finite-pair accuracy with completeness
unavailable. Supplying cadence without both window endpoints is an intentional
API/CLI error (exit 2 for CLI). This replaces the unsafe observed-span estimate.

## Deployment exporter

The existing exporter still requires two authorized files named in README. Its
row outcome summaries are not uptime, its indoor/outdoor signature remains an
exploratory inference, and it does not contain a reference instrument channel.
The `window_metrics` result uses `completeness_pct` for **delivery** availability;
`valid_environment_availability_pct` requires finite temperature and humidity
with `0 < RH <= 100`; reference-paired availability is unavailable, not zero.
This environmental-QC availability is distinct from the legacy `operational`
flag (`DEEPSLEEP_WAKE` and `hum > 0`), retained for historical row summaries.

Supply `--window-start`, `--window-end`, `--expected-interval-minutes` together,
and an explicit tolerance if justified. Without those, the historical provisional
window supplies descriptive row summaries only, with completeness null. Plot
panels showing the historical outdoor-signature window remain exploratory; a
custom scheduled window is identified separately in the metrics/report.

The external command is intentionally not represented as already run:

```bash
python analysis/analyze_deployment_logs.py --help
```

After the [owner provenance checklist](DEPLOYMENT_PROVENANCE_REQUEST.md) is
answered, substitute authorized paths and confirmed schedule values in that
CLI and use a **new versioned output directory**. The exporter also writes
derived subsets beside raw files under `derived/`; permission for that write
must exist. Compare duplicate/off-grid/edge accounting with the historical
estimator before replacing any published rate. A supplied argument is not proof
that firmware or deployment records confirmed it.
