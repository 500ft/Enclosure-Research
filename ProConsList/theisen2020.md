# Theisen et al. (2020): 3D-Printed Automatic Weather Station

**Source:** https://doi.org/10.5194/amt-13-4699-2020  
**Evidence boundary:** Eight-month outdoor comparison with an Oklahoma Mesonet station. Material, geometry, and multiple failure modes are directly reported.

## Sensors

MCP9808 air temperature; HTU21D RH/temperature; BMP280 pressure/temperature; SI1145 UV/visible/IR; Hall-effect wind-speed, wind-direction, and tipping-bucket rain sensors.

### Pros

- Multiple low-cost digital sensors create a complete weather station.
- Redundant temperature channels help expose enclosure and sensor differences.
- Several measurements compared reasonably with maintained reference instruments.
- Hall-effect sensing supports low-cost custom mechanical instruments.

### Cons

- Naturally aspirated temperature accuracy depended on wind speed.
- Wind direction and printed mechanical components were problematic.
- Moisture, corrosion, connectors, and component failures limited long-term reliability.
- Moving the BMP280 into the electronics box changed its thermal environment.

## Physical Box, Materials, and Geometry

Off-white and gray ASA printed parts, PVC frame, junction box, naturally aspirated radiation shield, polyurethane, conformal coating, PTFE filter, and silicone repairs.

### Pros

- ASA and PVC enabled a low-cost integrated outdoor station.
- Light-colored shield and passive ventilation reduced radiation exposure without consuming power.
- Junction box separated the Raspberry Pi from direct weather exposure.

### Cons

- Printed fasteners, thin parts, and moving components loosened or broke.
- Funnel and seals needed coating and repair.
- Passive shield performance degraded in low wind.
- Integrated geometry created many exposed connections and maintenance points.

## Selection Lessons for This Project

- Use light-colored ASA for printed outdoor shield parts, but use metal fasteners for structural joints.
- Treat passive-shield airflow and connector protection as explicit test variables.
- Avoid assuming printed mechanical sensors will have the same reliability as solid-state sensors.

