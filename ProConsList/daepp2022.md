# Daepp et al. (2022): Eclipse City-Scale Sensor Platform

**Source:** https://doi.org/10.1109/IPSN54338.2022.00010  
**Evidence boundary:** End-to-end deployment of 115 custom solar-powered, cellular-connected sensor boxes. Exact enclosure material is not reported.

## Sensors

PM2.5, temperature, RH, barometric pressure, and optional modular O3, NO2, SO2, and CO sensors.

### Pros

- Modular sensing supports different local measurement priorities.
- Solar power and cellular communication reduce infrastructure requirements.
- More than 90% of expected sensor-hours were collected in the reported deployment.

### Cons

- PM and gas sensors require environmental correction and calibration.
- Larger sensor suites increase power, airflow, and maintenance demands.
- Cellular communication introduces recurring cost and coverage dependence.

## Physical Box, Materials, and Geometry

Custom unobtrusive weatherproof urban enclosure optimized for sensing; enclosure material and detailed airflow path are not reported.

### Pros

- Complete integrated design supported deployment at 115 sites.
- Modular architecture supports maintenance and configuration changes.
- External reset capability reduces the need to open the enclosure.

### Cons

- Unreported material and airflow geometry limit reproduction.
- Solar exposure and panel placement can thermally affect the box.
- Urban mounting constraints can create site-specific bias.

## Selection Lessons for This Project

- Track expected sensor-hours as an autonomy metric.
- Design service and reset actions that do not require opening the box.

