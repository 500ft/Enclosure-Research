# Grimsley et al. (2021): EnviSense Low-Power Hydrological Nodes

**Source:** https://doi.org/10.1145/3477085.3478988  
**Evidence boundary:** Multi-node field deployment emphasizing autonomy, communication, and maintainability. Exact IP67 enclosure material is not reported.

## Sensors

MaxBotix outdoor ultrasonic range sensor or SDI-12 vented pressure transducer; internal temperature, RH, pressure, battery voltage/current, GPS, and LoRa radio.

### Pros

- External measurement probes allow electronics to remain sealed.
- Multiple sensor options support modular deployments.
- Device-health sensing improves remote diagnostics.
- LoRa and low-power design support long autonomy.

### Cons

- External probes and cables add connector and ingress risks.
- Ultrasonic measurements depend on mounting and environmental conditions.
- Pressure transducers require submerged installation and maintenance.
- Communication and power-system behavior become part of measurement reliability.

## Physical Box, Materials, and Geometry

Commercial rectangular IP67 enclosure with four sealed ports and external probes; exact enclosure material is not reported.

### Pros

- Strong separation between protected logger and exposed sensing element.
- Sealed modular ports support serviceability and sensor replacement.
- Clear management-port cap aids field maintenance.

### Cons

- Sealed enclosure can trap heat and condensation.
- Multiple penetrations increase sealing complexity.
- External antennas, probes, and cables remain exposed.
- Missing material information prevents thermal/weatherability comparison.

## Selection Lessons for This Project

- Use a sealed electronics zone with external or separately ventilated sensors.
- Log device-health and power data, and design ports for replacement and inspection.

