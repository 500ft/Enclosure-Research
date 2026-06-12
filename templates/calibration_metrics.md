# Calibration and Autonomy Metrics

Use one matched timestamp table per deployment. At minimum, include:

- `timestamp`
- `sensor_<variable>`
- `reference_<variable>`
- `battery_voltage` if available
- `ambient_temperature` if separate from target sensor
- `relative_humidity` if available
- `solar_radiation` or a sun/shade proxy if available
- `wind_speed` if available

## Accuracy Metrics

| Metric | Formula / definition | Report before calibration | Report after calibration |
|---|---|---:|---:|
| Bias | mean(sensor - reference) | yes | yes |
| MAE | mean(abs(sensor - reference)) | yes | yes |
| RMSE | sqrt(mean((sensor - reference)^2)) | yes | yes |
| Correlation | Pearson r | yes | yes |
| Drift | slope of residual vs time | yes | yes |

## Autonomy Metrics

| Metric | Definition |
|---|---|
| Runtime | Time from deployment start to first required physical intervention |
| Uptime | Fraction of expected logging windows with at least one valid record |
| Data completeness | Valid samples divided by expected samples |
| Sensor dropout count | Number of gaps or invalid periods by sensor channel |
| Maintenance burden | Number and duration of field interventions |
| Recalibration interval | Time until error exceeds chosen threshold |

## Recommended First Thresholds

These thresholds should be reviewed with the PI after the first deployment:

- temperature calibrated RMSE target: TODO deg C
- relative humidity calibrated RMSE target: TODO %RH
- data completeness target: at least 90%
- minimum autonomy target: TODO days
- maintenance interval target: TODO days

