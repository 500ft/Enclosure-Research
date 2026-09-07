# Final local checks — 2026-09-06

Working directory: `/Users/redhose/Developer/research-sprints/2026-09-05/Enclosure-Research`. Commands below actually executed; stdout/stderr retained.

No configured typecheck/lint command; compile and tests are the real Python gates. No GitHub workflow execution, publication, private-log replay, or physical test occurred.

## python --version

Exit status: 0

```text
Python 3.11.8
```

## python -m compileall -q analysis

Exit status: 0

```text
(no output)
```

## python -m unittest discover -s analysis/tests -v

Exit status: 0

```text
test_accuracy_definitions_and_sorting_preserved (test_compute_metrics.MetricsTests.test_accuracy_definitions_and_sorting_preserved) ... ok
test_cadence_without_intended_window_is_rejected (test_compute_metrics.MetricsTests.test_cadence_without_intended_window_is_rejected) ... ok
test_csv_retains_records_without_finite_pair (test_compute_metrics.MetricsTests.test_csv_retains_records_without_finite_pair) ... ok
test_delivery_sensor_and_pairing_have_different_numerators (test_compute_metrics.MetricsTests.test_delivery_sensor_and_pairing_have_different_numerators) ... ok
test_duplicate_slots_do_not_inflate_completeness_or_hide_edges (test_compute_metrics.MetricsTests.test_duplicate_slots_do_not_inflate_completeness_or_hide_edges) ... ok
test_empty_unscheduled_is_unavailable_not_zero_accuracy (test_compute_metrics.MetricsTests.test_empty_unscheduled_is_unavailable_not_zero_accuracy) ... ok
test_equivalent_timezone_offsets_are_same_slot (test_compute_metrics.MetricsTests.test_equivalent_timezone_offsets_are_same_slot) ... ok
test_exclusive_end_and_outside_rows (test_compute_metrics.MetricsTests.test_exclusive_end_and_outside_rows) ... ok
test_explicit_tolerance_and_slot_collision (test_compute_metrics.MetricsTests.test_explicit_tolerance_and_slot_collision) ... ok
test_invalid_intervals (test_compute_metrics.MetricsTests.test_invalid_intervals) ... ok
test_invalid_timestamp_has_actionable_error (test_compute_metrics.MetricsTests.test_invalid_timestamp_has_actionable_error) ... ok
test_invalid_windows_and_tolerances (test_compute_metrics.MetricsTests.test_invalid_windows_and_tolerances) ... ok
test_mixed_clock_conventions_rejected (test_compute_metrics.MetricsTests.test_mixed_clock_conventions_rejected) ... ok
test_off_grid_is_reported_not_rounded_implicitly (test_compute_metrics.MetricsTests.test_off_grid_is_reported_not_rounded_implicitly) ... ok
test_partial_final_interval_has_scheduled_start (test_compute_metrics.MetricsTests.test_partial_final_interval_has_scheduled_start) ... ok
test_empty_window_has_no_rate_or_accuracy_fabrication (test_deployment_metrics.DeploymentMetricTests.test_empty_window_has_no_rate_or_accuracy_fabrication) ... ok
test_explicit_schedule_counts_edges_and_duplicate_deliveries (test_deployment_metrics.DeploymentMetricTests.test_explicit_schedule_counts_edges_and_duplicate_deliveries) ... ok
test_unconfirmed_configuration_cannot_emit_completeness (test_deployment_metrics.DeploymentMetricTests.test_unconfirmed_configuration_cannot_emit_completeness) ... ok
test_valid_environment_availability_differs_from_delivery (test_deployment_metrics.DeploymentMetricTests.test_valid_environment_availability_differs_from_delivery) ... ok
test_cadence_only_is_actionable_cli_error (test_metrics_cli.CliTests.test_cadence_only_is_actionable_cli_error) ... ok
test_consumer_fixture (test_metrics_cli.CliTests.test_consumer_fixture) ... ok
test_deployment_incomplete_schedule_fails_before_data_access (test_metrics_cli.CliTests.test_deployment_incomplete_schedule_fails_before_data_access) ... ok
test_deployment_missing_data_is_access_error_not_traceback (test_metrics_cli.CliTests.test_deployment_missing_data_is_access_error_not_traceback) ... ok
test_unscheduled_fixture_is_explicitly_unavailable (test_metrics_cli.CliTests.test_unscheduled_fixture_is_explicitly_unavailable) ... ok

----------------------------------------------------------------------
Ran 24 tests in 1.001s

OK
```

## python analysis/check_literature_coverage.py

Exit status: 0

```text
Bibliography entries: 26
Per-paper analyses: 26
Coverage complete.
```

## python analysis/thermal_bias.py --no-figure

Exit status: 0

```text
==============================================================================
ASSUMPTIONS LEDGER (every input; SIMULATION, pending lab data)
==============================================================================
input                        value  units         status
------------------------------------------------------------------------------
G_clear_sky               800-1000  W/m^2         swept/bounded
T_air                         30.0  degC          bounded
RH_air                        50.0  %             bounded
T_sky_offset                  20.0  K             bounded
alpha_V0                       0.9  -             bounded
alpha_shield                   0.3  -             bounded
eps_surface                    0.9  -             bounded
f_sky_V0                       0.5  -             bounded
f_sky_shield                  0.05  -             bounded
A_proj_V0                     0.03  m^2           geometry/TODO-from-lab
A_conv_V0                     0.09  m^2           geometry/TODO-from-lab
A_proj_shield                0.012  m^2           geometry/TODO-from-lab
A_conv_shield                 0.02  m^2           geometry/TODO-from-lab
shield_solar_factor           0.18  -             bounded
Q_int_V0                       0.8  W             bounded/TODO-from-lab
Q_int_shielded                 0.1  W             bounded/TODO-from-lab
h_free_floor                   5.0  W/m^2K        physics
h_wind_slope                   4.0  W/m^2K per (m/s)physics
shield_conv_boost              1.4  -             bounded
shield_air_preheat_calm         1.2  K             bounded
preheat_wind_halflife          1.5  m/s           bounded
h_fan_V2                      25.0  W/m^2K        bounded
wind_sweep                 0.0-5.0  m/s           swept
------------------------------------------------------------------------------
Notes:
  G_clear_sky: Clear-sky global horizontal irradiance on the projected area; sweep band.
  T_air: Ambient air temperature for the heat-soak case (warm clear day).
  RH_air: True ambient relative humidity used to anchor the RH-error mapping.
  T_sky_offset: Clear-sky radiant sky temperature is taken as T_air - 20 K (clear-sky depression).
  alpha_V0: Solar absorptance of the baseline box surface (dark/unspecified finish, worst-ish case).
  alpha_shield: Solar absorptance of a light/white high-reflectance shield surface (framework rec.).
  eps_surface: Long-wave emissivity of painted plastic/printed surface (typical 0.85-0.95).
  f_sky_V0: Fraction of the baseline box outer area that radiates to the cold sky (upper/side faces); the rest exchanges long-wave with surroundings (ground/mast) at ~ambient.
  f_sky_shield: Fraction of the shielded sensor element that sees the cold sky directly; the plates intentionally block the sky view, so the sensor exchanges long-wave mostly with the surrounding plates/air at ~ambient (this is why a shield does not over-cool below ambient).
  A_proj_V0: Sun-facing projected area of the baseline box (~0.17 x 0.17 m face).
  A_conv_V0: Convecting/radiating external area of the baseline box (~6 faces of ~0.17 m cube minus mount).
  A_proj_shield: Effective sun-exposed projected area reaching the shielded sensor zone (plates shade most of it).
  A_conv_shield: Convecting/radiating area of the small shielded sensor element wetted by inter-plate through-flow (a sensor PCB/probe is small; only the local element, not the whole shield, sets its balance).
  shield_solar_factor: Fraction of incident solar flux that still reaches the sensor through a multi-plate shield (view-factor/shading reduction; multi-plate shields cut direct load by roughly 80-90%, but diffuse/reflected sky and warm-plate re-radiation leak in, so this is deliberately not near-zero).
  Q_int_V0: Internal electronics+battery dissipation coupled to the sensor in the single-zone baseline.
  Q_int_shielded: Residual self-heating reaching the sensor in the two-zone (electronics separated) layout.
  h_free_floor: Free/low-wind convective coefficient floor used at ~0 m/s wind.
  h_wind_slope: Linear wind term: h_ext ~= h_free_floor + slope * wind (flat-plate forced-convection scaling).
  shield_conv_boost: Natural-convection enhancement of the multi-plate shield (open inter-plate gaps chimney air).
  shield_air_preheat_calm: Solar-heated shield plates warm the through-flowing air slightly above true ambient before it reaches the sensor; this plate-to-air coupling is the dominant residual bias of a real passive screen at low wind. Modeled as a calm-wind air pre-heat that decays as wind/aspiration rises.
  preheat_wind_halflife: Wind speed at which the shield air pre-heat is cut in half (ventilation flushes the warmed air).
  h_fan_V2: Forced-convection coefficient at the sensor with the low-power aspiration fan running.
  wind_sweep: External wind speed sweep mapped to h_ext via the linear correlation above.

Operating ambient: T_air = 30.0 degC, RH_true = 50.0 %, T_sky = 10.0 degC (clear-sky depression 20 K)

==============================================================================
BIAS-VS-VARIANT TABLE  (SIMULATION -- pending lab co-location data)
delta-T = sensor temperature rise above true ambient [degC]
RH_err  = reported-minus-true relative humidity [%RH] (negative = reads dry)
==============================================================================
 G[W/m2]  wind[m/s]  Baseline closed box dT/RHerrPassive multi-plate shield dT/RHerrActively aspirated reference dT/RHerr
-------------------------------------------------------------------------------------------------------------------------
     800        0.0           17.6        -30.7          3.0         -7.7          1.1         -3.0
     800        0.5           15.0        -28.0          2.4         -6.4          1.1         -3.0
     800        1.0           13.1        -25.6          2.0         -5.4          1.1         -3.0
     800        2.0           10.4        -21.9          1.5         -4.0          1.1         -3.0
     800        5.0            6.4        -15.1          0.7         -2.0          1.1         -3.0
-------------------------------------------------------------------------------------------------------------------------
    1000        0.0           22.7        -35.0          3.7         -9.4          1.3         -3.7
    1000        0.5           19.4        -32.4          3.0         -7.8          1.3         -3.7
    1000        1.0           17.0        -30.0          2.5         -6.6          1.3         -3.7
    1000        2.0           13.5        -26.1          1.8         -4.9          1.3         -3.7
    1000        5.0            8.3        -18.6          0.9         -2.5          1.3         -3.7
-------------------------------------------------------------------------------------------------------------------------

Range across wind 0.0-5.0 m/s at G=1000 W/m^2:
  Baseline closed box            dT =  22.7 (calm) ..  8.3 (windy) degC,  RH_err =  -35.0 .. -18.6 %RH
  Passive multi-plate shield     dT =   3.7 (calm) ..  0.9 (windy) degC,  RH_err =   -9.4 ..  -2.5 %RH
  Actively aspirated reference   dT =   1.3 (calm) ..  1.3 (windy) degC,  RH_err =   -3.7 ..  -3.7 %RH

[table] wrote analysis/output/thermal_bias_table.csv
==============================================================================
SENSITIVITY (one-at-a-time), reference point G=1000 W/m^2, wind=0.5 m/s
delta-T [degC]; shows which uncertain input dominates the bias
==============================================================================
perturbation                                       V0 dT     V1 dT
------------------------------------------------------------------
baseline                                            19.4       3.0
V0 surface painted white (alpha 0.90 -> 0.30)        4.5         -
V1 shading worse (solar_factor 0.18 -> 0.30)           -       4.4
V1 no convection boost (1.4 -> 1.0)                    -       3.4
V1 plate air pre-heat doubled (1.2 -> 2.4 K calm)         -       3.9
V0 internal load doubled (0.8 -> 1.6 W)             20.1         -
V0 low emissivity (0.90 -> 0.50)                    26.4         -
------------------------------------------------------------------

NOTE: All values above are SIMULATION outputs and are the analytical
baseline that the conjugate-heat-transfer FEA (docs/cad_fea_plan.md 3.2)
will refine. They are predictions pending lab and co-location data; no
regulatory-grade or certified-performance claim is implied.
```

## python evidence/sprint-2026-09-05/evaluate_candidate.py

Exit status: 0

```text
Candidate hashes: PASS (4/4)
PASS N=1 cadence_min=2 translation_days=0 unique=1/1
PASS N=1 cadence_min=2 translation_days=11 unique=1/1
PASS N=1 cadence_min=7.5 translation_days=0 unique=1/1
PASS N=1 cadence_min=7.5 translation_days=11 unique=1/1
PASS N=7 cadence_min=2 translation_days=0 unique=4/7
PASS N=7 cadence_min=2 translation_days=11 unique=4/7
PASS N=7 cadence_min=7.5 translation_days=0 unique=4/7
PASS N=7 cadence_min=7.5 translation_days=11 unique=4/7
PASS N=23 cadence_min=2 translation_days=0 unique=12/23
PASS N=23 cadence_min=2 translation_days=11 unique=12/23
PASS N=23 cadence_min=7.5 translation_days=0 unique=12/23
PASS N=23 cadence_min=7.5 translation_days=11 unique=12/23
Developer metamorphic cases: 12/12 PASS; no field/independent-validation claim
```

## git diff --check

Exit status: 0

```text
(no output)
```

## git diff --exit-code -- analysis/output/thermal_bias_table.csv analysis/figures

Exit status: 0

```text
(no output)
```

## git rev-parse HEAD

Exit status: 0

```text
c8c941dabd02541b3f3bfd67dc0edbc0517e6be9
```

## git status --short

Exit status: 0

```text
 M .github/workflows/ci.yml
 M CONTRIBUTING.md
 M README.md
 M analysis/analyze_deployment_logs.py
 M analysis/compute_metrics.py
 M analysis/thermal_bias_results.md
 M docs/data-and-figures.md
 M docs/results.md
 M paper/manuscript_v1.md
?? analysis/tests/
?? docs/DEPLOYMENT_PROVENANCE_REQUEST.md
?? docs/RELIABILITY_METRICS.md
?? docs/REVIEW_READY.md
?? docs/SPRINT_PROGRESS.md
?? docs/SPRINT_ROADMAP.md
?? docs/SPRINT_TASKS.csv
?? evidence/
```

