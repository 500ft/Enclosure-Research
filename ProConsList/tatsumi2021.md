# Tatsumi et al. (2021): Hydrometeorological Measurement System

**Source:** https://doi.org/10.3390/technologies9040078  
**Evidence boundary:** Open-field system evaluation. The exact printed enclosure resin is not reported.

## Sensors

LM60BIZ air/soil temperature, YL-69 soil moisture, G2711-01 GaAsP photodiode, GPS, and micro-SD storage.

### Pros

- Low-cost sensors and Arduino architecture are accessible and replaceable.
- External probes let sensing elements be placed at the measurement location.
- Solar power supports longer autonomous deployment.
- Reference comparisons were performed for the measured variables.

### Cons

- Analog sensors require careful signal conditioning and calibration.
- YL-69-style exposed soil probes can corrode and drift.
- Handmade photodiode cover changes optical response and requires calibration.
- External wiring and terminal blocks increase field-failure points.

## Physical Box, Materials, and Geometry

Compact rectangular printed logger case, approximately 30 x 110 x 110 mm; unspecified printer resin; external sensors connected through detachable terminals.

### Pros

- Compact protective case supports portable, repeatable deployment.
- External terminals improve sensor replacement and modularity.
- Electronics protection is separated from sensor placement.

### Cons

- Unspecified resin prevents weatherability comparison.
- Rectangular sealed or insulated case may trap electronics heat.
- Terminal blocks and external wires require ingress and strain-relief protection.

## Selection Lessons for This Project

- Preserve modular external connections but specify connector sealing and strain relief.
- Record exact material chemistry; "3D-printed" alone is insufficient for design comparison.

