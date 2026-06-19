# Military Applications Research Brief

Branch: `military-environmental-sensing`

Topic: rugged, low-cost, validated environmental sensing hardware for fire, smoke, and base air-quality monitoring.

## Executive Takeaway

The most credible defense framing is not "military air-quality gadget." It is an installation-resilience and force-health sensing layer: low-cost sensor nodes that can be deployed around military bases, training ranges, fire-prone installation boundaries, battery/equipment storage areas, maintenance shops, and temporary response zones to provide local, validated measurements of particulate matter, temperature, humidity, smoke conditions, and selected combustion gases.

The opportunity exists because military installations need more localized and operationally useful environmental data than sparse reference monitors can provide, but consumer air sensors are usually not rugged, validated, or packaged for defense workflows. The useful product wedge is a ruggedized, calibrated, auditable node and deployment protocol that sits between cheap consumer sensors and expensive reference-grade instruments.

## Confirmed Evidence From Primary Sources

### 1. DoD has a real installation-resilience problem

SERDP and ESTCP describe themselves as DoD installation innovation programs that develop and demonstrate scalable technologies to enhance military readiness, improve warfighter capabilities, and strengthen defense infrastructure. Their natural-hazards focus area explicitly says natural disasters hinder DoD mission readiness, damage installation infrastructure, and require tools that help DoD leaders preserve mission-critical operations.

Relevant source:
- SERDP/ESTCP homepage: https://serdp-estcp.mil/
- SERDP/ESTCP Natural Hazards focus area: https://serdp-estcp.mil/focusareas/827388c6-457f-4b28-901b-b5d1054558db/natural-hazards

Implication:
- A base-air-quality sensor project should be positioned as an installation-readiness tool, not only an environmental-science project.

### 2. Wildfire and smoke are named installation hazards

SERDP/ESTCP says weather-related disruptions to installations are becoming more complex and that vulnerable systems include infrastructure exposed to wildfire, storms, and other disturbances. It also states DoD manages about 28 million acres of natural infrastructure supporting test and training missions, with funded work addressing flooding, heat, drought, land degradation, wildfire, and extreme weather.

Relevant source:
- SERDP/ESTCP Natural Hazards focus area: https://serdp-estcp.mil/focusareas/827388c6-457f-4b28-901b-b5d1054558db/natural-hazards

Implication:
- Fire/smoke monitoring is a defensible DoD-adjacent use case, especially for western bases, training lands, and installations near wildland-urban interface zones.

### 3. EPA recognizes low-cost air sensors as useful but variable

EPA's Air Sensor Toolbox says lower-cost, portable air sensor monitors are widely used in the United States and that EPA provides science on sensor performance, operation, and use. EPA also warns that sensor data quality is highly variable, and its performance-target reports are intended to provide consistent testing protocols, metrics, and target values for non-regulatory supplemental and informational monitoring outdoors at fixed locations.

Relevant sources:
- EPA Air Sensor Toolbox: https://www.epa.gov/air-sensor-toolbox
- EPA Air Sensor Performance Targets and Testing Protocols: https://www.epa.gov/air-sensor-toolbox/air-sensor-performance-targets-and-testing-protocols
- EPA Enhanced Air Sensor Guidebook: https://www.epa.gov/air-sensor-toolbox/how-use-air-sensors-air-sensor-guidebook

Implication:
- The product should not claim regulatory-grade measurement. The stronger claim is: "validated non-regulatory supplemental monitoring for operational decisions."

### 4. EPA already has a wildfire smoke data workflow

AirNow has a dedicated wildfire page and Fire and Smoke Map for air quality and smoke near users. That proves smoke-aware public-health workflows already exist, but they are not necessarily dense enough for every base, training range, depot, or tactical logistics site.

Relevant source:
- AirNow Wildfires: https://www.airnow.gov/wildfires/

Implication:
- A defense version should integrate with existing AQI/PM workflows rather than inventing a new risk language from scratch.

### 5. Air Force has an occupational/environmental health customer profile

The U.S. Air Force Bioenvironmental Engineer role focuses on protecting Airmen from environmental hazards, identifying and evaluating dangers, performing health-risk assessments, advising command on operational risk, and addressing chemical, biological, and radiological issues.

Relevant source:
- U.S. Air Force Bioenvironmental Engineer career page: https://www.airforce.com/careers/healthcare/bioenvironmental-engineer

Implication:
- Likely internal customers include Bioenvironmental Engineering, Civil Engineering, Fire Emergency Services, Emergency Management, installation safety offices, and range-control/environmental teams.

### 6. Procurement paths exist for small companies, but the product must be narrow

SBIR/STTR is suitable for a small company developing technology with government mission relevance. SBIR.gov describes Phase I as proof of concept, Phase II as technology development, and Phase III as commercialization, with non-dilutive funding and no government equity/IP ownership.

SAM.gov registration is needed for an entity to bid on federal awards. SERDP/ESTCP also accepts proposals from universities and private-sector organizations through BAAs for high-priority installation challenges.

Relevant sources:
- SBIR.gov: https://www.sbir.gov/
- Defense SBIR/STTR: https://www.defensesbirsttr.mil/
- SAM.gov entity registration: https://sam.gov/entity-registration
- SERDP/ESTCP Work With Us: https://serdp-estcp.mil/workwithus

Implication:
- The first fundable version should be a Phase I-style prototype and validation study, not a full defense product line.

### 7. Ruggedness must be proven, not claimed

MIL-STD-810 is the common reference point for environmental ruggedness. For this project, the relevant test families are likely high temperature, low temperature, temperature shock, solar radiation, rain, humidity, dust/sand, vibration, shock, and possibly salt fog depending on base environment. The key engineering point is that "rugged" must map to named tests, selected severities, and operating conditions.

Relevant source:
- DLA ASSIST MIL-STD-810 document details: https://quicksearch.dla.mil/qsDocDetails.aspx?ident_number=35978

Implication:
- Do not say "military-grade." Say "tested against selected environmental stress conditions relevant to fixed outdoor base deployment."

### 8. Compliance becomes serious once defense-specific data is involved

CMMC Phase 1 implementation began November 10, 2025, focused on Level 1 and Level 2 self-assessments. If the company handles federal contract information or controlled unclassified information, cybersecurity compliance becomes part of the business.

ITAR registration can be required for U.S. persons who manufacture, export, temporarily import defense articles, or furnish defense services. The eCFR also states that registration does not grant export rights and is generally a precondition to licenses or approvals.

Relevant sources:
- DoD CIO CMMC page: https://dodcio.defense.gov/CMMC/
- ITAR registration rules, 22 CFR Part 122: https://www.ecfr.gov/current/title-22/chapter-I/subchapter-M/part-122

Implication:
- Keep the first version dual-use, unclassified, non-weapon, and non-ITAR where possible. Avoid defense-specific detection of CBRN/weapon agents unless guided by counsel and a sponsor.

## Market And Technical Landscape

### Existing sensor products

Consumer and civic air-quality systems already cover parts of the problem:

- PurpleAir Zen: PM2.5-focused indoor/outdoor unit with Wi-Fi, SD logging, dual Plantower particle counters, BME688 temperature/humidity/pressure/gas sensor, and $299 listed price.
- QuantAQ MODULAIR-PM: outdoor PM1/PM2.5/PM10 monitor, cloud-connected, solar-ready, usable for public health, disaster recovery, and fenceline monitoring.

Relevant sources:
- PurpleAir Zen: https://www2.purpleair.com/products/purpleair-zen
- QuantAQ MODULAIR-PM: https://www.quant-aq.com/products/modulair-pm

What they prove:
- There is demand for distributed PM sensing.
- The component stack is technically feasible.
- Cloud dashboards and distributed networks are expected.

What they leave open for this repo:
- Defense installation ruggedness.
- Auditable calibration and validation against EPA-style protocols.
- Enclosure design for heat, dust, rain, wind, condensation, insects, and field maintenance.
- Offline/local-first operation when Wi-Fi/cloud access is not guaranteed.
- Deployment logs and maintenance workflows suitable for installation managers.

## Strongest Defense Use Cases

### A. Wildfire smoke monitoring around installations

Problem:
- Regional AirNow data can miss base-level microclimates, smoke intrusion paths, range conditions, and exposure gradients.

Node requirements:
- PM2.5/PM10, temperature, humidity, pressure, wind optional, solar/battery telemetry.
- Outdoor fixed-location deployment.
- Local logging plus optional cloud upload.
- Alerts when PM2.5 crosses operational thresholds.

Best customer:
- Installation environmental office, emergency management, Bioenvironmental Engineering, base command center.

### B. Training range and prescribed-burn smoke monitoring

Problem:
- Training lands and prescribed burns generate smoke; installations need local data to support go/no-go, personnel exposure, and community-facing decisions.

Node requirements:
- PM2.5/PM10, wind direction/speed integration, timestamped geospatial map.
- Rapid redeployability and tripod/mast mounting.
- Calibration traceability.

Best customer:
- Range control, natural-resources managers, fire management teams.

### C. Battery storage / charging / maintenance-area early warning

Problem:
- Bases increasingly use batteries, e-bikes, drones, portable electronics, EVs, backup systems, and energy-storage infrastructure. Fire and thermal events create smoke and combustion byproducts.

Node requirements:
- Temperature, humidity, PM, CO/VOC screening, battery backup, high-temperature-tolerant enclosure, alarm output.

Best customer:
- Fire emergency services, facilities, logistics, motor pool, drone units.

Important caution:
- Do not claim lithium-ion fire detection without a controlled test campaign. Position it first as "environmental anomaly monitoring near storage/charging areas."

### D. Disaster response and temporary base recovery

Problem:
- After wildfires, industrial fires, storms, or infrastructure damage, commanders need local environmental awareness while facilities are being restored.

Node requirements:
- Rapid install, local display, offline logging, rugged case, low maintenance, solar or battery options.

Best customer:
- Civil engineers, emergency management, Defense Support of Civil Authorities support teams.

## Best Product Positioning

Recommended name:
- Rugged Installation Air Monitoring Node, or RIAM Node.

One-sentence positioning:
- A low-cost, ruggedized, EPA-protocol-aligned environmental sensing node for non-regulatory smoke, PM, heat, humidity, and base air-quality awareness at military installations and training sites.

Do not position it as:
- A regulatory air monitor.
- A CBRN detector.
- A weapons-system sensor.
- A universal fire detector.
- A "military-grade" device without test evidence.

## Minimum Viable Technical Scope

### Sensed variables

Must-have:
- PM2.5
- PM10
- temperature
- relative humidity
- pressure
- internal enclosure temperature
- battery voltage / power status

Nice-to-have:
- CO
- TVOC
- CO2 for indoor/vehicle/shelter use
- wind speed and wind direction via add-on weather station
- GPS or fixed-location metadata

Avoid in v1:
- chemical warfare agent detection
- explosive atmosphere certification
- biological detection
- classified interfaces

### Hardware requirements

Minimum:
- IP-rated commercial electronics box plus replaceable printed sensor shield.
- White or reflective radiation shield.
- Separate airflow path for sensing volume and sealed electronics volume.
- Drainage and insect screens.
- Conformal coating where appropriate.
- Modular sensor cartridge.
- SD/offline logging.
- Watchdog timer and brownout handling.

Defense-leaning upgrades:
- solar/battery pack
- LoRa/cellular option
- tamper-evident mounting
- selected MIL-STD-810-informed tests
- local-only data mode
- exportable CSV with calibration metadata

## Validation Plan That Would Make Reviewers Trust It

Phase 1: Baseline build
- Build 3-5 nodes.
- Co-locate with a reference monitor or credible comparison instrument.
- Use EPA Air Sensor Toolbox guidance for metrics and reporting.
- Record weather, sun exposure, enclosure temperature, and uptime.

Phase 2: Rugged enclosure comparison
- Compare current enclosure against ruggedized design.
- Stress test rain, humidity, heat, solar exposure, dust, vibration/handling, and power cycling.
- Track water ingress, data loss, sensor drift, connector corrosion, and maintenance events.

Phase 3: Defense-relevant deployment
- Deploy around a campus, lab, fire-training area, rooftop, battery test area, or controlled smoke source.
- Map spatial gradients and event detection.
- Produce deployment SOP, maintenance checklist, and calibration report.

Key metrics:
- PM2.5 bias, MAE, RMSE, correlation versus reference.
- AQI category agreement.
- uptime percentage.
- expected samples versus received samples.
- first failure and limiting failure.
- time to maintenance.
- enclosure internal temperature rise above ambient.
- power autonomy.
- sensor-to-sensor agreement.

## Funding And Go-To-Market Paths

### Academic first

Best for an undergrad:
- Publish the ruggedization and validation study.
- Keep data public and unclassified.
- Use EPA-style metrics.
- Target HardwareX, Sensors, IEEE Sensors conference, or environmental monitoring venues.

### SBIR/STTR

Best Phase I framing:
- "Rugged low-cost air-quality sensing network for installation wildfire-smoke and emergency-response awareness."

Possible agencies:
- DoD SBIR/STTR.
- SERDP/ESTCP if framed as installation resilience/environmental security.
- NSF I-Corps or America Seed Fund if kept dual-use.

### Pilot customers

Start with:
- University fire-safety or facilities group.
- Local fire department or emergency management.
- Environmental health/safety office.
- Military-adjacent research lab.
- National Guard, ROTC, or base innovation office only after a civilian prototype exists.

## Main Risks

1. Sensor credibility risk
   Low-cost PM sensors need calibration and correction. Raw readings are not enough.

2. Ruggedness risk
   A 3D-printed enclosure can fail from UV, heat, rain, insects, dust, or connectors before the sensor fails.

3. Procurement risk
   DoD sales cycles are slow. An undergrad project should start with a paper/prototype, not a direct procurement plan.

4. Compliance risk
   Defense-specific data, CUI, exports, or CBRN claims can trigger compliance burdens.

5. Overclaiming risk
   The product should support situational awareness, not life-safety decisions, unless certified and tested for that purpose.

## Best Research Question For This Branch

How can a low-cost outdoor environmental sensor box be ruggedized and validated for non-regulatory military-installation smoke, particulate, and heat-stress awareness while preserving low cost, maintainability, and deployment autonomy?

## Recommended Next Branch Work

1. Add a "military installation use-case" section to `paper/manuscript_v1.md`.
2. Add test requirements for rain, solar heating, dust, vibration/handling, power interruption, and maintenance burden.
3. Add a deployment template for installation-style use: site ID, mission context, exposure source, risk threshold, alert contacts, maintenance log.
4. Add a validation matrix mapping EPA air-sensor metrics to defense installation needs.
5. Keep the core paper civilian/dual-use; put defense framing in a separate discussion section to avoid scope creep.
