# Lazarescu (2015): Long-Term Environmental WSN Field Test

**Source:** https://doi.org/10.3390/s150409481  
**Evidence boundary:** Fifty temperature nodes and two gateways deployed for approximately 2.5 months in an olive field.

## Sensors

NTC temperature transducer, ATtiny25 microcontroller, TI CC1150 transmitter, gateway radios, battery and system-health measurements.

### Pros

- NTC sensing and transmit-only communication permit extremely low average current.
- Hourly heartbeats enable missing-node detection.
- Self-test and fault reporting can reduce field-maintenance burden.

### Cons

- Direct solar heating caused false alerts.
- Manually soldered NTC leads failed from cyclic thermal strain.
- Transmit-only nodes reduce energy use but cannot receive updates or confirmations.

## Physical Box, Materials, and Geometry

Compact node package with downward-facing air aperture and protective resin; gateway electronics in a sealed plastic package inside a divided wooden birdhouse with solar panels.

### Pros

- Downward-facing aperture improves thermal contact while reducing direct ingress.
- Protective resin reduces moisture and insect exposure.
- Separate gateway compartments and solar power support autonomous operation.

### Cons

- Package and nearby metal components attenuated RF.
- Gateway placement near solar panels caused major RF loss.
- Solar heating, charger failure, and inadequate thermal design reduced autonomy.
- Packaging material is not specified sufficiently for thermal comparison.

## Selection Lessons for This Project

- Log system health, test failure propagation, and design for remote fault isolation.
- Treat antenna clearance, solder fatigue, enclosure heat, and battery-state estimation as box-design parameters.

