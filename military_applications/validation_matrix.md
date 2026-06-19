# Military Installation Validation Matrix

Use this matrix to translate the general sensor-box study into a defense-relevant validation package. The goal is credible supplemental monitoring for installation awareness, not regulatory compliance or life-safety certification.

## Measurement Validation

| Claim | Required evidence | Minimum metric | Preferred metric | Notes |
|---|---|---|---|---|
| PM2.5 trend awareness | Co-location with reference or credible comparison monitor | correlation, bias, RMSE | EPA-style performance report | Include humidity and high-PM event behavior. |
| PM10 trend awareness | Co-location with reference or credible comparison monitor | correlation, bias, RMSE | EPA-style performance report | Useful for dust, smoke, and training-range conditions. |
| Temperature awareness | Co-location with shielded reference probe | bias, RMSE, drift | error vs solar/wind/enclosure temperature | Track warm bias from enclosure heating. |
| Relative humidity awareness | Co-location or chamber step test | bias, RMSE, response time | response curve fit and hysteresis | RH affects PM sensor interpretation. |
| AQI-style category awareness | Matched sensor/reference PM2.5 timestamps | category agreement | false high/false low table by category | Use only as informational, non-regulatory output. |
| Calibration stability | Time-split validation | test-period RMSE | drift and recalibration interval | Train on earlier data, test on later data. |

## Ruggedness Validation

| Stress | Why it matters | Test approach | Pass condition |
|---|---|---|---|
| Solar heating | Direct sun can bias ambient readings | Full-sun outdoor exposure; record internal and ambient temperature | Internal heat rise and sensor bias stay within project threshold. |
| Rain / splash | Outdoor base deployment includes storms and washdown risk | Hose/spray or controlled rain exposure with powered and unpowered states | No water path to electronics; no data loss after test. |
| Humidity / condensation | Condensation causes corrosion and sensor failure | Humidity chamber, sealed-bin test, or repeated cool/warm cycling | No visible condensation on PCB; readings recover after exposure. |
| Dust / insects | Ranges and dry bases have dust; vents invite insects | Dust exposure plus screen inspection | No blocked inlet; filter/screen remains serviceable. |
| Vibration / handling | Nodes may be transported, mast-mounted, or moved between sites | Repeated handling, transport, tripod/mast shake, connector inspection | No cracked mount, loose connector, or data interruption. |
| Power interruption | Field nodes lose power and must recover cleanly | Battery depletion and forced brownout cycles | Logging restarts with correct timestamps and no corrupted files. |

## Autonomy And Operations

| Claim | Required evidence | Metric |
|---|---|---|
| Useful unattended deployment | Continuous field run | runtime before physical intervention |
| Reliable data capture | Expected samples vs received samples | uptime and data completeness |
| Maintainable field hardware | Timed service event | minutes to replace sensor cartridge, SD card, battery, or shield |
| Operational alerts | Logged threshold crossings | alert latency, missed alerts, false alerts |
| Auditability | Exported data package | timestamps, calibration version, sensor IDs, site metadata, maintenance log |

## Decision Thresholds To Set With A Sponsor

| Threshold | Initial placeholder |
|---|---:|
| PM2.5 calibrated RMSE | TODO |
| PM2.5 AQI-style category agreement | TODO |
| Temperature calibrated RMSE | TODO |
| Data completeness | at least 90% |
| Minimum unattended runtime | TODO days |
| Maximum field service time | TODO minutes |
| Maximum internal heat rise above ambient | TODO deg C |

