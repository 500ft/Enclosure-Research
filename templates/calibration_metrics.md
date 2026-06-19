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
| Category agreement | fraction of matched samples in the same PM2.5 category bin | PM2.5 only | PM2.5 only |

## Autonomy Metrics

| Metric | Definition |
|---|---|
| Runtime | Time from deployment start to first required physical intervention |
| Uptime | Fraction of expected logging windows with at least one valid record |
| Data completeness | Valid samples divided by expected samples |
| Sensor dropout count | Number of gaps or invalid periods by sensor channel |
| Maintenance burden | Number and duration of field interventions |
| Recalibration interval | Time until error exceeds chosen threshold |

## Installation-Awareness Metrics

Use these when the deployment is framed around smoke, fire response, range activity, or base air-quality awareness.

| Metric | Definition |
|---|---|
| PM2.5 category agreement | Fraction of matched timestamps where sensor and reference fall in the same AQI-style category |
| False high category events | Sensor category is higher than reference category |
| False low category events | Sensor category is lower than reference category |
| Alert threshold crossings | Number of times a configured operational threshold is crossed |
| Alert latency | Time from threshold crossing to local record or transmitted alert |
| Offline recovery | Whether local logs survive power or network interruption |
| Field service time | Minutes required for sensor, shield, SD card, or battery maintenance |

## Recommended First Thresholds

These thresholds should be reviewed with the PI after the first deployment:

- temperature calibrated RMSE target: TODO deg C
- relative humidity calibrated RMSE target: TODO %RH
- PM2.5 category agreement target: TODO %
- data completeness target: at least 90%
- minimum autonomy target: TODO days
- maintenance interval target: TODO days

## Script Example

For PM2.5 AQI-style category agreement, pass category upper bounds to `analysis/compute_metrics.py`:

```bash
python3 analysis/compute_metrics.py data/matched.csv \
  --sensor sensor_pm25 \
  --reference reference_pm25 \
  --expected-interval-minutes 5 \
  --category-breakpoints 9,35.4,55.4,125.4,225.4
```
