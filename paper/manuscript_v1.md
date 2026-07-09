# Calibration, Ambient Conditions, and Integration Effects on the Accuracy and Autonomy of a Low-Cost Outdoor Multi-Sensor Box

**Version:** V1.0 working draft  
**Status:** Draft for PI/lab review  
**Repository:** 500ft/Enclosure-Research

## Abstract

Low-cost outdoor sensor boxes can increase the spatial and temporal resolution of environmental measurements, but their usefulness depends on more than the nominal accuracy of individual sensors. Once sensors are integrated into an enclosure, their measurements can be affected by calibration error, solar heating, internal electronics heat, airflow restriction, water ingress, dust, sensor aging, power limitations, firmware reliability, and data loss. This paper evaluates the lab's existing low-cost outdoor multi-sensor box as a deployed system rather than as a single enclosure component. The study measures raw sensor accuracy against reference instruments, quantifies improvement after simple calibration, tracks autonomy and data completeness during field operation, and identifies which design factors most limit performance. The expected output is a practical decision framework that helps the lab choose future materials, geometries, sensor layouts, and maintenance schedules based on accuracy, reliability, autonomy, manufacturability, and weather resistance.

## 1. Introduction

Environmental monitoring often requires measurements at locations or spatial densities where commercial weather stations and regulatory-grade instruments are too expensive or too difficult to deploy. Low-cost sensor boxes can help fill this gap by making local measurements of temperature, relative humidity, pressure, particulate matter, gas concentration, light, or other ambient variables. They are especially useful for laboratory field campaigns, distributed outdoor experiments, teaching, and preliminary site characterization.

However, a low-cost sensor box is not accurate simply because its datasheet reports an acceptable sensor tolerance. Outdoor deployment changes sensor behavior. Solar radiation can heat the enclosure and bias temperature and relative humidity. Poor airflow can delay response and create a microclimate inside the box. Rain, snow, condensation, dust, and ultraviolet exposure can degrade materials and electronics. Battery voltage and power management can affect runtime and data continuity. Wireless links, SD cards, firmware, and connectors can fail before the sensing element itself fails. These integration effects determine whether the box produces useful data for days, weeks, or months without intervention.

The working research question is:

> Can the lab's low-cost sensor box collect accurate, reliable outdoor data for a useful period of time without constant maintenance, and what factors most affect that performance?

This question expands the earlier enclosure-only direction. The previous scope emphasized passive 3D-printed radiation shields, temperature and relative-humidity bias, response time, and short-term weathering. Those issues remain relevant, but they are now treated as part of a larger sensor-box performance problem. The main contribution of this paper is therefore not a universal sensor-box design. It is a structured evaluation of the lab's current box, the calibration improvement achievable from field data, and the design criteria that should guide future versions.

## 2. Background and Literature Review

### 2.1 Low-cost outdoor sensor systems

Low-cost weather and environmental sensing systems are usually justified by their ability to increase measurement density and reduce deployment cost. Theisen et al. evaluated a 3D-printed weather station beside an Oklahoma Mesonet station for eight months and found that several measurements were comparable to commercial sensors, while wind direction and durability were more problematic [@theisen2020]. That study is important for this paper because it evaluates the complete station over time, including longevity and component failure, not only instantaneous accuracy.

Tatsumi et al. presented an open-source, low-cost hydrometeorological measurement system for open-field use, emphasizing a compact board, 3D-printed housing, and field comparison with reference values [@tatsumi2021]. Their work supports the design logic of documenting the full system architecture: sensors, board, housing, data storage, and deployment context must be described together because performance depends on the integrated system.

Air quality sensor studies show the same pattern. Low-cost platforms can be useful complements to reference networks, but field calibration, environmental correction, and deployment reliability determine whether their data can be interpreted quantitatively [@clements2017; @desouza2022; @giordano2021; @airsenseur2023]. These studies are directly relevant even if the lab box is not primarily an air-quality box, because they provide calibration and validation practices that generalize to outdoor low-cost sensing.

Recent complete-system deployments strengthen the case for evaluating the box as an integrated instrument. Eclipse deployed 115 solar-powered, cellular-connected urban sensor devices and collected more than 90% of expected sensor-hours during the reported campaign [@daepp2022]. In a different application, Lazarescu's long-term environmental WSN field test showed that mechanical strain, enclosure heat, antenna placement, charging failures, and faulty-node behavior can limit service before the nominal battery lifetime is reached [@lazarescu2015].

### 2.2 Calibration and ambient-condition effects

Calibration is necessary because low-cost sensors can be biased by sensor-to-sensor variability, environmental cross-sensitivity, sensor aging, and differences between laboratory and field conditions. The common baseline approach is co-location with a reference instrument, followed by a statistical correction model. Linear regression and multiple linear regression are widely used first because they are interpretable, require modest data, and provide a defensible baseline before more complex machine-learning models are introduced [@clements2017; @desouza2022; @vajs2021].

For this V1.0 study, calibration should start with:

1. raw sensor value compared with the reference;
2. univariate linear correction using the target sensor reading;
3. multiple linear correction using ambient covariates such as temperature, relative humidity, solar radiation, wind speed, battery voltage, or enclosure temperature if available.

More complex models should only be added after the baseline data show a clear nonlinear pattern and after enough data are available to avoid overfitting. This is especially important for a research paper because the engineering result should remain explainable: the lab needs to know which factor limits the box, not only which model gives the lowest error on one dataset.

Long-duration studies also show why a one-time calibration is insufficient. The three-year QUANT study found substantial variation among commercial sensor systems and documented effects from relocation, manufacturer corrections, and long-term behavior [@diez2024]. Winter et al. found that Alphasense electrochemical sensors could remain stable over three years with frequently updated calibration, while mechanical and electrical failures often limited service first [@winter2025].

### 2.3 Enclosure materials and geometries

Outdoor enclosures and radiation shields affect sensor accuracy by controlling solar exposure, convective airflow, water protection, and thermal coupling between electronics and sensing elements. This section collects the materials and geometries reported in the literature, augments them with candidates of interest to the lab, and records the source of every property so the data can feed the a priori screening in Section 4.6. Following a source hierarchy, what a system was *built from and tested as* is taken from the primary papers, while quantitative material properties are taken from manufacturer datasheets or standard polymer references and are flagged for verification against the specific filament grade actually used. Optical surface properties (solar absorptance/reflectance) are not reported on filament datasheets because they depend on color and finish rather than the base polymer; these are marked as quantities to be measured, not assumed. The full extraction lives in `literature/materials_options.csv` and `literature/geometries_options.csv`.

#### Evidence from the literature

Theisen et al. built a 3D-printed weather station based on the UCAR 3D-PAWS design and ran it beside an Oklahoma Mesonet reference station for eight months [@theisen2020]. More than 100 parts were printed in off-white ASA, chosen over PLA for higher ultraviolet, temperature, and impact resistance; parts used a grid infill to cut print time. Temperature/RH/pressure sensors sat in a *naturally aspirated* radiation shield at 1.5 m, the support frame was standard PVC pipe, and the Raspberry Pi logger was housed in a sealed electrical junction box with a secondary sensor monitoring internal box temperature — effectively a two-zone layout. Two findings are directly relevant to material and geometry selection. First, temperature RMSE fell from 1.22 °C toward ~1.08 °C and lower as wind speed increased, because the passive shield approached the performance of the reference station's actively aspirated shield only at higher airflow; the radiation error is therefore ventilation-limited, and the authors suggest a 5 V aspiration fan as a remedy. Second, the dominant failures were integration and weathering failures, not sensing-element failures: relative-humidity sensor board corrosion at month 6, an anemometer head that sheared off (attributed partly to reduced infill weakening the print), 3D-printed clamps and nuts that loosened over time, insects nesting in 3D-print grooves, glue yellowing on the UV cover, and water intrusion at the joints between printed parts and the PVC frame (resolved with sealant and drain holes).

Botero-Valencia et al. designed an open-source 3D-printed radiation shield from six stacked truncated cones — five with a central perforation and a solid top cone — separated by 20 mm metallic M3 separators that admit airflow while keeping the interior dry, with the SHT10 temperature/RH sensor held inside the second cone from the bottom so it never sees direct light, and a 1-inch PVC pipe coupling at the base for mounting [@botero2022]. They fabricated the shield in both PLA and ASA and compared both against an unshielded sensor and a Davis Vantage Pro reference station; ASA was preferred for ultraviolet resistance, hardness, and degradation resistance, while PLA was cheaper (about \$5.70 versus \$9.00 in material).

Tatsumi et al. reinforce the system-level point: an open-field measurement system must document the board, the 3D-printed housing, and the data storage/communication path together, because field performance depends on the integrated package rather than the sensor alone [@tatsumi2021]. The air-quality platforms in the review [@clements2017; @desouza2022; @giordano2021; @vajs2021] do not treat enclosure material as a primary variable, so they contribute calibration and reliability practice rather than material/geometry data.

Controlled shield comparisons provide stronger geometry-selection evidence, and they put measured magnitudes on the radiation error. Tarara and Hoheisel found that reflective stacked-plate configurations outperformed tube-shaped designs under low wind (<1 m/s) and high irradiance (>600 W/m²): their best stacked-plate shield held errors between −0.7 and +2.2 °C (89% of daytime readings within 1.5 °C), while cone designs reached +5.4 °C and open-bottom tube designs +7.4 °C, which is why open-bottom shields vulnerable to reflected radiation are not advised and tube shields appeared to require more than roughly 30% sidewall perforation to ventilate effectively; aspirated shields in the same study averaged within ±0.5 °C [@tarara2007]. Holden et al. showed that a roughly \$3 folded white corrugated-plastic Gill-style shield could perform similarly to a commercial passive shield — bias under 0.5 °C beneath forest canopy and a mean absolute error of 0.99 °C against mechanically aspirated references in the open — although a warm full-sun low-wind bias remained [@holden2013]. Deford et al. demonstrated a low-cost white-PLA aspirated shield with a double-wall elbow inlet and low-power fan, directly exposing the accuracy-versus-autonomy tradeoff introduced by aspiration [@deford2025].

More complex recent designs address upward radiation and guided airflow. Liu et al. combined silver-coated aluminum plates, black inner surfaces, white-resin layers, eight vents, and a truncated-cone reflector [@liu2023]. Jin et al. used square shading plates and bowl-cover flow-guiding shrouds while comparing plastic, wood, Fe-Ni alloy, and aluminum configurations through CFD and outdoor validation [@jin2026]. A 14-month Arctic intercomparison of ten shield models further showed that shield differences decrease with wind speed and that fan, logger, power, memory, mounting, and storm failures must be included in the design evaluation [@garciaizquierdo2024].

#### Synthesis: material options

| Material | UV / weather | HDT (°C) | Density (g/cm³) | Printability | Used in lit. | Goal served |
|---|---|---:|---:|---|---|---|
| PLA | Poor | ~55 | ~1.24 | Easy | Botero (PLA variant) | Accuracy screening only |
| ABS | Poor (yellows) | ~98 | ~1.04 | Hard (warps, fumes) | General baseline | Heat resistance, UV-limited |
| ASA | **Excellent** | ~95 | ~1.07 | Hard (warps) | Theisen, Botero | **Accuracy + autonomy** |
| PETG | Moderate–good | ~70 | ~1.27 | Easy | Common option | Autonomy / manufacturability |
| PC | Moderate (needs stabilizer) | ~130 | ~1.20 | Very hard | — | High-temp / high-strength |
| PMMA (acrylic) | Excellent | ~95 | ~1.18 | Sheet, not FDM | — | UV-stable windows |
| PVC (box/pipe) | Moderate | ~60–70 | ~1.38 | Off-the-shelf | Theisen, Botero | Mount + sealed electronics zone |

Property values are representative and must be verified against the datasheet of the specific filament grade used; solar absorptance is color/finish dependent and is to be measured, not assumed. UV ratings and glass-transition values are from a published filament comparison and are consistent with the field UV durability Theisen observed for ASA. Full sourcing per cell is in `materials_options.csv`.

#### Synthesis: geometry options

| Geometry | Airflow | Radiation blocking | Water protection | Electronics coupling | Used in lit. |
|---|---|---|---|---|---|
| Naturally aspirated stacked-plate / louvered shield | Passive crossflow | Good | Moderate | Low (sensor isolated) | Theisen |
| Stacked truncated-cone shield | Passive crossflow | Good | Good (20 mm gaps) | Low | Botero |
| Actively aspirated (fan) shield | Forced | Best | Moderate | Low | Suggested by Theisen |
| Two-zone: sealed electronics box + external probe | Sealed + ventilated region | Design-dependent | High (electronics) | Designed-low | Theisen (junction box + Pi) |
| Vented / perforated box (sensor inside) | Passive | Poor–moderate | Moderate | High (warm bias) | Baseline |
| Commercial IP-rated junction box | Sealed | n/a | High (IP65+) | High if sensor inside | Theisen |
| Reflective stacked-plate handmade shield | Passive crossflow | Good | Moderate | Low | Tarara; Holden |
| Double-wall elbow aspirated shield | Fan-forced | Very good | Good | Low | Deford |
| Mixed-finish multilayer eight-vent shield | Passive through vents | Very good | Good | Low | Liu |
| Bowl-cover flow-guided passive shield | Guided passive flow | Very good | Good | Low | Jin |

The material and geometry decision is therefore not simply "which enclosure protects electronics best." A fully sealed box may protect the electronics but create poor airflow or heat buildup. A highly ventilated shield may improve temperature and humidity response but increase risk of water ingress, dust, insects, or connector corrosion. A reflective white ASA shield may reduce heat absorption and survive ultraviolet exposure better than a dark PLA shield, but it may be harder or more expensive to print. Theisen's wind-dependent temperature error and Botero's PLA-versus-ASA comparison are concrete evidence for these tradeoffs.

For the a priori screening in Section 4.6, the enclosure is treated as a set of measurable design factors, each tied to one of the project's two goals (accuracy or autonomy):

- material: PLA, ASA, PETG, ABS, polycarbonate, acrylic, PVC, commercial junction box plastic, or metal;
- color and surface finish (solar absorptance — to be measured): white, reflective, matte, painted, coated, or dark;
- geometry: louvered shield, stacked plates, helical path, perforated box, aspirated shield, sealed electronics box plus external probe;
- airflow path (drives radiation error — see Theisen): passive crossflow, chimney flow, fan aspiration, blocked vents, bottom openings;
- thermal layout: sensor near electronics, sensor isolated from heat sources, sensor outside main electronics volume;
- weather exposure (drives autonomy/lifetime): rain path, drain holes, gasket, cable glands, condensation path, UV exposure.

#### Candidates of interest for this lab

The cited work favors ASA for outdoor durability, but the lab's fabrication capability constrains what is realistic in-house. The current printer is an open-frame FDM machine without a heated chamber, which prints PLA and PETG reliably but makes ASA, ABS, and PC difficult or impractical (ASA and ABS warp without an enclosure; PC needs chamber heating and 270–310 °C). Two consequences follow for candidate selection.

First, **PETG becomes the primary in-house outdoor material.** It prints easily on an open machine, warps little, and has moderate-to-good UV resistance — a better outdoor default than PLA, and achievable without the enclosure ASA demands. ASA is retained as the literature benchmark and an upgrade path (outsourced prints or a future enclosed printer), and PLA is kept only as a control or as a coated part, not as an uncoated outdoor material.

Second, **surface treatment is promoted to a first-class design variable** rather than an afterthought. For an open-FDM lab this is the practical lever on the two properties that most limit performance: a white reflective exterior coating lowers solar absorptance (directly reducing the radiation-heating bias, and supplying the optical value that no filament datasheet provides — to be measured, not assumed), a UV-resistant clear coat extends the field life of PLA/PETG substrates (Theisen used polyurethane to seal a print), and conformal coating on the sensor board targets the moisture-corrosion failure that ended Theisen's relative-humidity sensor at month 6. These appear as candidate rows in `materials_options.csv` and must be validated for adhesion and field-UV durability rather than taken on faith.

On geometry, the study will test, beyond the literature's single-layer stacked-plate and truncated-cone shields: a fan-aspirated shield (to attack the ventilation-limited radiation error directly, at a known power cost), a double/multi-louver Stevenson-type shield (to see how far a purely passive design can close the gap before a fan is needed), a helical/chimney buoyancy-driven shield (fan-like ventilation without the power draw), the two-zone sealed-electronics-plus-external-sensor architecture, and — as the strongest fit for an open-FDM lab — a commercial IP-rated junction box paired with a small printed, field-replaceable PETG vent/shield module. The last option deliberately separates the hard sealing problem (bought off the shelf) from the printable shield problem (cheap to iterate). The vented box with the sensor sharing the electronics volume is retained only as a negative control, since it couples self-heating into the ambient reading. Full candidate details and proxy parameters are in `geometries_options.csv`.

### 2.4 Autonomy and reliability

Autonomy is the period during which the box operates without physical intervention. This is not only battery life. A box loses autonomy when data are missing, sensors drop out, storage fills, clocks drift, wireless upload fails, connectors corrode, firmware hangs, or the enclosure requires repair. EnviSense and similar low-power environmental sensing work demonstrates that field reliability depends on deployment planning, remote device management, and system co-design with domain users, not only the sensor bill of materials [@grimsley2021].

The expanded literature shows why autonomy must be measured from observed field behavior rather than estimated battery capacity alone. Eclipse reports expected sensor-hours as an operational reliability measure [@daepp2022]. Lazarescu documents how a theoretically long-lived low-power network still required intervention after thermal, mechanical, charging, and communication failures [@lazarescu2015]. The COAT Arctic comparison lost data from fan, logger, power, memory, mounting, and storm events [@garciaizquierdo2024], while Winter et al. found that mechanical and electrical failures could occur before meaningful electrochemical sensing-element degradation [@winter2025].

For the lab's sensor box, autonomy should be reported with several metrics: runtime before physical intervention, uptime percentage, data completeness, number and type of maintenance events, number of power failures, number of sensor dropouts, and time before recalibration is needed. These metrics connect directly to the PI's question: how long can the box last without someone having to change it or fix it?

## 3. Sensor Box Description

This section must document the current lab box before any modification. Table 1 is the required baseline inventory.

| Component | Current lab box value | Notes to collect |
|---|---:|---|
| Sensor models | TODO | Include manufacturer, exact part number, measurement variable, range, datasheet accuracy |
| Microcontroller/logger | TODO | ESP32, Arduino, Raspberry Pi, Particle, custom PCB, etc. |
| Power system | TODO | Battery chemistry/capacity, solar panel, regulator, sleep mode |
| Enclosure material | TODO | PLA, ASA, PETG, ABS, commercial box, metal, etc. |
| Enclosure geometry | TODO | Louvered, stacked plate, vented box, sealed box, aspirated shield |
| Sensor placement | TODO | Inside main box, external probe, distance from electronics, orientation |
| Logging rate | TODO | Seconds/minutes between samples |
| Data storage/transmission | TODO | SD card, flash, Wi-Fi, LoRa, cellular, serial download |
| Firmware behavior | TODO | Watchdog, retry logic, timestamp source, power saving |
| Known failure problems | TODO | Water ingress, battery drain, missing data, corrosion, bad calibration |

The first field deployment should use the existing box as-is. This creates the baseline against which any enclosure, power, firmware, or calibration improvement can be compared.

## 4. Methods

### 4.1 Study design

The study has four phases:

1. **Inventory and bench check.** Document hardware, inspect enclosure, confirm sensor operation, verify timestamps, and log battery voltage.
2. **Reference co-location.** Deploy the sensor box near reference instruments under real outdoor conditions. The reference should measure the same variables as the lab sensors whenever possible.
3. **Baseline analysis.** Compare raw data to reference data and quantify error, missing data, uptime, and failure modes.
4. **Calibration and decision analysis.** Apply simple calibration models, compare error reduction, and identify whether the limiting factor is sensor calibration, power, enclosure design, firmware, or maintenance.

### 4.2 Deployment setup

The box should be mounted in the same orientation and exposure expected for normal use. Mounting height, nearby surfaces, shade, roof overhangs, vegetation, walls, and ground material must be recorded because they affect the local microclimate. If possible, wind speed, solar radiation, rain, and ambient temperature should be recorded from a nearby weather station or reference system.

The minimum recommended deployment is 14 days for a first baseline check, with a stronger target of 30 days. A 30-day co-location is long enough to capture day-night cycles, several weather states, battery behavior, and early failures, and it matches the U.S. EPA's non-regulatory air-sensor base-testing protocols, which recommend collocating at least three identical sensor units with reference-grade (FRM/FEM) monitors for a minimum of 30 days per site [@duvall2021]. For any gas or particulate channels, ASTM D8406-22 provides a standardized field performance-evaluation practice for outdoor sensor instruments [@astm2022d8406], and CEN/TS 17660-1 defines the corresponding European evaluation and classification framework [@cen2021ts17660]. For the meteorological channels, sensor siting and exposure — mounting height, radiation shielding, and distance from surfaces and obstructions — should follow the practice in the WMO Guide to Instruments and Methods of Observation where practical [@wmo2023no8]. Longer deployment is preferred if the box is intended for seasonal use.

### 4.3 Accuracy metrics

Let \(x_i\) be the sensor value and \(y_i\) be the reference value at matched timestamp \(i\).

- Bias: mean of \(x_i - y_i\)
- MAE: mean absolute error
- RMSE: square root of mean squared error
- Correlation: Pearson correlation between sensor and reference
- Drift: change in bias over time, estimated by a linear trend in residuals
- Response lag: time offset that maximizes correlation after weather transitions, if sampling rate supports it

Metrics should be reported for each sensor variable before and after calibration. This metric set is aligned with the evaluation metrics recommended by the EPA air-sensor performance protocols — linearity (coefficient of determination), slope, intercept, RMSE/normalized RMSE, and data completeness [@duvall2021] — with drift and response lag added because enclosure thermal behavior is a study variable here.

The uncertainty of the reference instrument itself must be documented and reported alongside these metrics: sensor-minus-reference differences smaller than the reference uncertainty cannot be interpreted as sensor error. Each reference should therefore be identified by make, model, calibration date, and traceability class — FRM/FEM designation for air-quality references [@duvall2021], or documented conformance to WMO measurement-uncertainty and exposure requirements for meteorological references [@wmo2023no8].

### 4.4 Calibration models

The first calibration model should be linear:

\[
y = \beta_0 + \beta_1 x
\]

The second model should include ambient or system covariates when measured:

\[
y = \beta_0 + \beta_1 x + \beta_2 RH + \beta_3 T + \beta_4 V_{battery} + \beta_5 S + \epsilon
\]

where \(RH\) is relative humidity, \(T\) is temperature, \(V_{battery}\) is battery voltage, and \(S\) is solar radiation or another solar-exposure proxy. Not every variable will be available for every sensor. The model should stay simple enough to interpret.

Calibration should be evaluated with a train/test split by time, not random row splitting only. A time split better represents future deployment because the model is trained on earlier data and tested on later data.

### 4.5 Autonomy and reliability metrics

Autonomy is evaluated with:

- total runtime before intervention;
- uptime percentage;
- expected sample count versus received sample count;
- data completeness by sensor channel;
- number of sensor dropouts;
- number of logger resets or firmware hangs;
- battery-voltage trend and low-voltage events;
- physical maintenance events;
- time until recalibration is needed.

The study should report both the first failure and the limiting failure. For example, a short wireless outage may be the first problem, but the limiting problem may be battery depletion after six days.

### 4.6 Material and geometry classification

Candidate materials and geometries should be classified before testing using practical criteria. This is an a priori classification; it helps decide which design variants deserve testing.

| Design factor | Why it matters | Higher-priority direction |
|---|---|---|
| Density / mass | Affects thermal inertia, mounting load, print time | Low enough for field mounting, not so low that parts become fragile |
| Weatherability | UV, rain, freeze-thaw, dust, corrosion | ASA, PETG, UV-stable commercial plastics, coatings |
| Heat absorption | Dark materials and low reflectance increase radiation heating | White or reflective exterior, low solar absorptance |
| Airflow | Controls response time and heat/moisture buildup | Open shield around sensing elements, isolated sealed electronics |
| Water protection | Prevents rain and condensation damage | Overhangs, drains, glands, splash-resistant vent paths |
| Manufacturability | Determines repeatability and cost | Simple prints, few supports, standard fasteners |
| Maintainability | Determines field repair burden | Modular sensor access, replaceable shields, visible status indicators |

## 5. Results

This V1.0 draft does not include measured lab results yet. The results section below is the intended reporting structure.

### 5.1 Raw accuracy

Report raw bias, MAE, RMSE, correlation, and drift for each sensor channel. Include a time-series plot showing the sensor and reference together, plus a residual plot showing error against time, temperature, humidity, solar exposure, and battery voltage.

| Sensor variable | Bias | MAE | RMSE | Correlation | Drift | Notes |
|---|---:|---:|---:|---:|---:|---|
| Temperature | TODO | TODO | TODO | TODO | TODO | TODO |
| Relative humidity | TODO | TODO | TODO | TODO | TODO | TODO |
| Pressure | TODO | TODO | TODO | TODO | TODO | TODO |
| PM2.5 / gas / light / other | TODO | TODO | TODO | TODO | TODO | TODO |

### 5.2 Calibrated accuracy

Compare raw data against calibrated data. The key result is not only whether RMSE improves, but whether the calibration remains stable across weather conditions and time.

| Sensor variable | Raw RMSE | Linear RMSE | Multiple linear RMSE | Error reduction | Recommended model |
|---|---:|---:|---:|---:|---|
| Temperature | TODO | TODO | TODO | TODO | TODO |
| Relative humidity | TODO | TODO | TODO | TODO | TODO |
| Pressure | TODO | TODO | TODO | TODO | TODO |
| PM2.5 / gas / light / other | TODO | TODO | TODO | TODO | TODO |

### 5.3 Autonomy and data completeness

Report runtime and data loss as engineering results, not as secondary notes.

| Metric | Value | Interpretation |
|---|---:|---|
| Deployment length | TODO | Calendar duration |
| Runtime before intervention | TODO | True autonomy |
| Uptime | TODO | Percent of expected logging period with valid records |
| Data completeness | TODO | Percent of expected samples received |
| Battery low-voltage events | TODO | Power limitation indicator |
| Sensor dropout events | TODO | Sensor or firmware limitation |
| Maintenance events | TODO | Practical field burden |

### 5.4 Failure modes

Failure modes should be coded by type:

- calibration failure: persistent bias, drift, environmental cross-sensitivity;
- power failure: battery depletion, regulator instability, solar charging failure;
- enclosure failure: heat buildup, water ingress, condensation, UV damage, broken mount;
- firmware/data failure: missing timestamps, SD write errors, wireless upload failure, watchdog resets;
- maintenance failure: difficult access, fragile connectors, repeated manual intervention.

## 6. Discussion

The discussion should identify the dominant limiting factor in the current box. Possible interpretations are:

- If calibration sharply reduces error and autonomy is acceptable, the current hardware may be usable with a defined calibration workflow.
- If error remains strongly correlated with solar radiation, wind speed, or enclosure temperature after calibration, the enclosure geometry or material is likely limiting accuracy.
- If the box stops early or misses many samples, power or firmware reliability is more important than sensor accuracy.
- If sensors fail physically, corrode, or drift rapidly, weather protection and replacement schedule become the design priority.
- If maintenance is frequent or difficult, future design should prioritize modularity, connector protection, and easier field access.

The paper should avoid claiming that one material or geometry is universally best. Instead, it should report which component most affects the lab's measurement goal. A temperature and relative-humidity box may need airflow and radiation shielding above all else. A particulate-matter box may need inlet geometry, fan reliability, and humidity correction. A multi-sensor box may need separation between a ventilated sensor region and a sealed electronics/power region.

## 7. Design Criteria for Future Lab Boxes

The lab should use a weighted decision framework when choosing future box designs. The weights can change by experiment, but the criteria should stay consistent.

| Criterion | Metric | Better design means |
|---|---|---|
| Accuracy | Calibrated RMSE, bias, drift | Lower error after calibration |
| Calibration robustness | Test-period error and drift | Correction works across weather states |
| Autonomy | Days before intervention | Longer runtime without field visit |
| Reliability | Uptime and data completeness | Fewer missing samples and dropouts |
| Weather resistance | Physical inspection and failure events | Less UV, rain, condensation, and dust damage |
| Thermal behavior | Error versus sun/wind/enclosure temperature | Less heat-induced bias |
| Maintainability | Time to replace sensor/battery | Faster repair with fewer fragile steps |
| Manufacturability | Print/build time, cost, repeatability | Faster, cheaper, more repeatable builds |

For the next prototype, a strong default architecture is a two-zone design:

1. a sealed electronics and power compartment with cable glands, drain-aware mounting, and serviceable access;
2. a ventilated external sensing region or radiation shield that isolates temperature/RH and other ambient sensors from electronics heat while blocking direct solar radiation and rain.

The first material set to compare should be the current enclosure material against at least one more weatherable and reflective option, such as white ASA or white PETG, depending on the lab's printer capability. Dark materials should be avoided for parts near ambient-temperature sensors unless they are painted or shielded from solar radiation.

## 8. Conclusion

This V1.0 paper reframes the project around the deployed sensor box rather than only the enclosure. The proposed evaluation measures raw accuracy, calibration improvement, autonomy, reliability, and design effects from material, geometry, airflow, sealing, and weather exposure. The immediate next step is to document the lab's current hardware and run a baseline co-location deployment. After that, the paper can identify whether the current box is limited mainly by calibration, power, enclosure design, firmware, or maintenance. The final contribution will be a practical decision framework for building the lab's next outdoor sensor boxes with clearer tradeoffs between accuracy, autonomy, reliability, and manufacturability.

## References

See `references.bib`.
