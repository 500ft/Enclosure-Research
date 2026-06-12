# Consolidated Sensor and Physical-Box Selection Pros and Cons

This file preserves the cross-paper pros and cons developed from the initial literature set.

## Sensor Selection

### Digital Temperature and Relative-Humidity Sensors

Examples: MCP9808, HTU21D, SHT10, and BME280.

**Pros**

- Low cost, compact, low power, and easy to integrate.
- Digital interfaces simplify logging and reduce analog signal problems.
- Calibration can reduce systematic bias.
- Secondary temperature channels can help identify internal enclosure heating.

**Cons**

- Direct solar exposure and low airflow create substantial temperature error.
- Relative-humidity measurements inherit temperature error and are affected by condensation and aging.
- Individual units can differ enough to require unit-specific calibration.
- A sensor inside the electronics box may measure the box microclimate rather than ambient conditions.

### Optical Particulate-Matter Sensors

Examples: Plantower PMS5003, Plantower PMS7003, and Alphasense OPC-N3.

**Pros**

- Measure multiple particle-size fractions at relatively low cost.
- Support high-frequency distributed monitoring.
- Widely represented in calibration literature.

**Cons**

- Humidity, aerosol composition, sensor age, and deployment location affect response.
- Require an airflow path, which conflicts with enclosure sealing.
- Fans, inlets, and optical chambers require maintenance and can fail.
- Calibration may not transfer between sites or seasons.

### Electrochemical Gas Sensors

Examples: Alphasense CO-B4, NO2-B43F, NO-B4, OX-A431, and related cells.

**Pros**

- Low power and suitable for distributed outdoor systems.
- Multiple gases can be measured in one integrated station.

**Cons**

- Temperature, RH, cross-sensitivity, drift, and aging affect output.
- Require repeated co-location and calibration.
- Enclosure airflow strongly affects response.

### External Environmental Probes

Examples: ultrasonic range sensors, SDI-12 pressure transducers, and soil probes.

**Pros**

- Permit sealed electronics and direct placement at the measurement location.
- Support modular replacement.

**Cons**

- Cables, connectors, and glands create ingress and reliability risks.
- Exposed probes can be damaged by weather, corrosion, or debris.

## Material Selection

### White or Off-White ASA

**Pros:** UV/weather resistance, reduced solar absorption, and support from outdoor printed-station studies.

**Cons:** More difficult printing, warping risk, and printed thin parts or fasteners can still fail.

### PLA

**Pros:** Low cost, accessible, and easy to print for prototypes.

**Cons:** Poorer long-term UV and thermal durability; dark colors increase solar heating.

### Commercial IP-Rated Enclosures

**Pros:** Strong electronics protection, established gaskets, and serviceable construction.

**Cons:** Trap electronics heat, restrict ambient airflow, and can still accumulate condensation.

### PVC Frames and Fittings

**Pros:** Low cost, weather resistant, available, and easy to modify.

**Cons:** Bulky, joints can loosen, and it is primarily a support rather than a sensing enclosure.

### Coatings, Filters, Glands, and Sealants

**Pros:** Improve moisture, contamination, and wiring-penetration protection.

**Cons:** Can slow or block sensor response, age outdoors, trap moisture, and add maintenance.

### Reflective Foil and White Corrugated Sheet

**Pros:** Extremely inexpensive, high-reflectance options that can be cut and folded into stacked-plate shields; useful for rapid geometry screening.

**Cons:** Structural rigidity, build repeatability, UV durability, and long-term water resistance are weaker or less documented than engineered outdoor plastics.

### Coated Aluminum and Mixed-Material Shields

**Pros:** Reflective outer metal surfaces can reduce solar heating, while selected dark inner surfaces can absorb reflected radiation; metal provides stiffness and heat spreading.

**Cons:** Oxidation, coating aging, high thermal conductivity, mixed-material assembly, and manufacturing complexity require validation.

## Geometry Selection

### Passive Multi-Plate or Truncated-Cone Shield

**Pros:** Blocks direct sun and rain, permits passive airflow, and consumes no power.

**Cons:** Accuracy remains wind-dependent; openings allow contamination and wind-driven rain.

### Actively Aspirated Shield

**Pros:** More consistent airflow and lower low-wind solar-heating error.

**Cons:** Requires fan power, filtering, and maintenance; fan failure changes measurement accuracy.

The Deford et al. double-wall elbow design shows a practical low-cost implementation, but its 680 mW fan makes the accuracy-versus-autonomy tradeoff directly measurable.

### Fully Sealed Single-Compartment Box

**Pros:** Simple and protective for electronics.

**Cons:** Traps heat and condensation and is unsuitable for sensors requiring ambient air exchange.

### Two-Zone or External-Sensor Box

**Pros:** Separates protected electronics from ventilated or exposed sensing elements.

**Cons:** Requires more parts, careful cable routing, sealing, and larger packaging.

### Flow-Guided and Mixed-Radiation Passive Shields

**Pros:** Bowl-cover shrouds, diversion pipes, annular layers, and lower reflectors can address airflow, direct solar radiation, and upward/reflected radiation without fan power.

**Cons:** These geometries are larger and harder to fabricate, and their CFD-predicted advantages require field validation and weathering tests.

## Current Best-Supported Starting Architecture

- White ASA passive shield for temperature and RH.
- Commercial IP-rated enclosure for electronics and power.
- Separate ventilated sensor zone or external probes.
- Controlled inlet/outlet geometry for PM or gas sensors.
- Replaceable filters, shields, sensors, and sealed connectors.
- A low-cost reflective stacked-plate shield as a manufacturability benchmark.
- A double-wall aspirated shield as the active accuracy benchmark.
