# CAD and FEA Design/Analysis Workstream Plan

Reference correction (2026-09-06): `templates/ruggedization_test_matrix.md` is referenced below but is not present in this checkout. Those validation hooks remain proposed, not available test procedures. EN-CAD-01 in the CAD ledger explicitly prepares the inspection-to-interface requirements before CAD release.

Individual CAD implementation tasks and estimates are now in [CAD_PLAN.md](CAD_PLAN.md) and [CAD_TASKS.csv](CAD_TASKS.csv). This workstream remains a broader analysis plan, not a second status ledger. The CAD comparison explicitly adds a same-geometry painted V0 control: changing finish must not be attributed to shield geometry. Optional V2 and later solver/physical work retain their own gates.

This document plans the computer-aided design (CAD) and finite-element analysis (FEA) work for the sensor-box study. Its purpose is to turn the qualitative enclosure lessons in the literature synthesis into modeled, comparable predictions that feed the paper's decision framework for future lab sensor-box designs.

**Status:** plan only. Nothing in this document is a result. Every temperature, airflow, stress, and frequency value referenced here is a future simulation output, not a measured quantity. Simulation outputs are treated as predictions to be checked against lab and co-location data before they are reported as findings.

**Honesty constraints (consistent with `README.md`):**

- No regulatory-grade, certification, or formal-qualification claims. Structural screening is inspired by defense environmental-test thinking but is not a substitute for MIL-STD-810 qualification, matching the framing already used in `templates/ruggedization_test_matrix.md`.
- Material optical properties (solar absorptance/reflectance, emissivity) are color- and finish-dependent and are not on filament datasheets; they are model inputs to be measured or bounded, not assumed, consistent with `paper/manuscript_v1.md` Section 2.3.
- Where a model input is unknown (sensor self-heating, vent area, gap tolerances), the analysis is run as a bounded sensitivity sweep rather than a single point estimate, and the assumption is logged.
- Simulation never replaces co-location. Its role is to explain and rank mechanisms (for example, *which* design factor drives the warm bias), not to certify accuracy.

## 1. Objectives

1. Build parametric CAD of the baseline box and the candidate radiation-shield variants so geometry can be varied and re-analyzed rather than redrawn.
2. Predict, per variant, the radiative self-heating bias that the enclosure adds to temperature and relative humidity, and its knock-on effect on gas-sensor readings. This is the core "the enclosure reads hot" error source the paper cares about.
3. Check that the passive shield can actually move enough air by natural convection to realize the predicted bias reduction.
4. Provide structural and modal screening for the rugged-installation extension (wind, drop, vibration of the mounted box).
5. Provide a sealing/tolerance analysis relating ingress protection and cable-gland routing to internal humidity.
6. Tie every analysis to a specific paper claim or a design-framework recommendation, so a future design decision can cite a modeled tradeoff.

## 2. Variants to model

These follow the shortlist already recommended in `literature/sensor_material_geometry_summary.md` and the manuscript, so CAD does not introduce new untested options.

| ID | Variant | Description | Why it is in the set |
|---|---|---|---|
| V0 | Current baseline box | The lab's existing enclosure as built, including the sensor placement relative to heat-producing electronics and battery. | Baseline that all biases are measured against; defined by `templates/baseline_system_description.md`. |
| V1 | Passive multi-plate radiation shield (Stevenson-style) | Naturally aspirated stacked-plate / multi-plate shield around the temperature/RH sensors, with a sealed electronics compartment below (two-zone layout). | Most directly supported outdoor passive design; covers the stacked-plate and multiplate/Stevenson arrangements reported by Tarara and Hoheisel, Holden et al., Botero-Valencia et al., and García Izquierdo et al. |
| V2 | Actively aspirated reference (optional) | The V1 shield plus a low-power fan forcing air past the sensor, modeled only as a benchmark and only if V0 shows strong low-wind or solar bias. | Upper-bound airflow case, mirroring the actively aspirated reference in Theisen et al. and the aspiration tradeoff in Deford et al. |

Parametric variables exposed in CAD (the geometry levers already listed in the literature summary): shield color/surface finish (drives optical inputs), number of plates/cones, plate/cone spacing, vent opening area and orientation, passive vs. fan-driven airflow, sensor distance from electronics and battery, roof/overhang geometry, drain path and bottom openings, cable-gland and connector locations, enclosure internal volume, and internal heat-source magnitude.

**Geometry source of truth:** when the lab box is inventoried via `templates/baseline_system_description.md`, the recorded enclosure material, geometry, vent path, drain path, gland locations, and sensor-to-electronics distance become the V0 model dimensions. Until then, V0 is parameterized with explicit placeholder dimensions flagged `TODO-from-lab`.

## 3. Analyses, deliverables, and claim mapping

Each analysis below lists its inputs, the deliverable, the validation hook (how the prediction will later be checked against measurement), and the paper claim or framework recommendation it supports.

### 3.1 Parametric CAD of the variants

- **Scope:** Solid CAD of V0, V1, and (optionally) V2 with the parametric levers in Section 2 driven from a single parameter table, so a geometry change re-drives the analysis meshes.
- **Inputs:** baseline-box dimensions from `templates/baseline_system_description.md`; plate count/spacing and vent area as swept parameters; sensor and electronics positions.
- **Deliverable:** a versioned CAD parameter table plus exported geometry for each variant, and a short dimensioned drawing per variant for the paper's methods figure.
- **Validation hook:** as-built measurements of the lab box are compared against the V0 model; deviations are logged before any thermal run is trusted.
- **Supports:** the methods/figure description of the modeled variants, and the framework recommendation that future designs record geometry parameters (color, plate count/spacing, vent area, sensor-to-electronics distance) rather than only a photo.

### 3.2 Steady-state thermal FEA / conjugate heat transfer (core analysis)

- **Scope:** Steady-state solar load to internal-air and sensor-surface temperature for each variant. Where the tool supports it, a conjugate-heat-transfer (CHT) setup couples external solar radiation, enclosure conduction, internal natural convection, and the sensor surface in one model; a simpler decoupled thermal-FEA-plus-convection-coefficient model is the fallback if CHT meshing is not practical. Internal electronics/battery dissipation is included as a heat source so the sensor sees both solar and self-heating loads.
- **Inputs (all logged, several swept):** incident solar flux (clear-sky bound), shield/enclosure solar absorptance and emissivity (measured or bounded, **not** from filament datasheets), ambient air temperature, wind-driven external convection coefficient swept from low-wind to moderate-wind, internal electronics dissipation (W) from the power inventory, and sensor position.
- **Deliverable — primary:** a **bias-vs-variant comparison table**: predicted sensor-air temperature offset above true ambient (Delta-T) for V0, V1, and V2, reported as a range across the wind/solar sweep rather than a single number, with the dominant contributor (solar vs. self-heating) attributed for each variant.
- **Deliverable — derived:** the knock-on effect of that Delta-T on relative humidity (warm air at fixed vapor content reads low RH) and on gas sensors. The gas knock-on is reported as a flagged, bounded estimate using published temperature-sensitivity behavior of the relevant electrochemical/metal-oxide sensors, because gas cross-sensitivity to temperature/RH is sensor-specific and will be stated as "indicative, pending sensor datasheets and co-location," not as a calibrated correction.
- **Validation hook:** the predicted Delta-T range is compared against the solar-heat-soak test in `templates/ruggedization_test_matrix.md` (internal-temp-rise and sensor-bias rows) and against co-location bias vs. the reference instrument. Agreement, or the gap, is reported.
- **Supports (core paper claim):** the manuscript's central enclosure claim that a passive shield reduces solar-radiation error relative to an exposed/baseline sensor, and that the error is ventilation-limited (Botero-Valencia et al.; Theisen et al.). It also supports the framework recommendation to separate ambient sensors from internal heat sources (two-zone layout) and to prefer high-reflectance, low-absorptance light-colored surfaces.

### 3.3 Natural-convection venting analysis (passive shield)

- **Scope:** Establish whether V1 can move enough air by buoyancy/cross-flow to realize the bias reduction predicted in 3.2 — i.e., confirm the passive shield is not effectively a sealed warm box. Covers vent sizing and airflow paths (inlet area, inter-plate gaps, exhaust/roof geometry, drain openings).
- **Inputs:** vent opening area and orientation, plate spacing, internal heat load, ambient temperature, and a low-wind external condition (the worst case for passive ventilation, consistent with the literature finding that passive shields degrade at low wind).
- **Deliverable:** a vent-sizing recommendation for the passive shield (minimum effective open area and plate-gap range that keeps internal air well-coupled to ambient under low wind), plus the predicted airflow path, expressed as a design rule rather than a guaranteed flow rate.
- **Validation hook:** cross-checked against the solar-heat-soak and low-wind behavior in the test matrix; if the shield reads hot at low wind in testing, the vent model is revisited.
- **Supports:** the framework recommendation on vent opening area/orientation and plate spacing, and the explicit literature warning that open bottoms and weak ventilation increase warm bias (Tarara and Hoheisel) while aspiration helps mainly at low wind (Theisen et al.; Deford et al.).

### 3.4 Structural and modal FEA (ruggedization / military-installation extension)

- **Scope:** Static and dynamic structural screening of the mounted box for the defense-relevant extension: (a) static wind-pressure loading on the box and mast/mount, (b) drop/handling shock as a quasi-static or explicit transient case on the enclosure and its fasteners, and (c) modal analysis to find natural frequencies of the mounted assembly and flag any that fall in a transport/wind-excitation band. The actively aspirated variant's fan mount is included as a vibration source if V2 is carried forward.
- **Inputs:** enclosure wall material and thickness, mount/mast stiffness, mass distribution (electronics, battery, shield), a bounded wind-pressure case, and a drop height/orientation set; fastener and printed-clamp details where the box is 3D-printed.
- **Deliverable:** a structural screening summary per load case — peak stress vs. material allowable (with margin), predicted deflection, and the first several natural frequencies with a note on any resonance risk in the relevant excitation band.
- **Validation hook:** mapped one-to-one to `templates/ruggedization_test_matrix.md` rows — "Handling / vibration" and "Solar heat soak"/mounting-stiffness items — so each predicted failure mode (cracking, fastener loosening, resonance) has a corresponding physical pass/fail test. The literature failure modes this anticipates (sheared anemometer head from reduced infill, loosened printed clamps and nuts in Theisen et al.; solder/mechanical fatigue in Lazarescu) are listed as the things the model is looking for.
- **Supports:** the ruggedization extension and its framework recommendations on wall thickness, infill/print orientation for load-bearing printed parts, mount stiffness, and fastener choice. Reported strictly as pre-qualification screening, **not** as MIL-STD-810 qualification.

### 3.5 Sealing and tolerance analysis (ingress vs. internal humidity)

- **Scope:** Relate enclosure sealing and cable-gland routing to internal humidity and condensation risk. Covers gap/tolerance stack at lid and gland interfaces, cable-gland placement and routing, drain-path geometry, and the tradeoff between a tightly sealed electronics compartment and a ventilated sensor compartment.
- **Inputs:** lid/seal gap tolerances, gland sizes and positions, internal vs. external temperature swing (drives condensation), and the two-zone split between sealed electronics and ventilated sensing.
- **Deliverable:** an IP-style ingress and routing assessment — a qualitative ingress rating target with a tolerance-stack check on the sealing interfaces, plus a gland-placement and drain-path recommendation that keeps liquid water out of the electronics volume while still letting the sensor compartment exchange air. Stated as an IP-*style* design target, not a certified IP rating.
- **Validation hook:** mapped to the "Rain / splash," "Humidity / condensation," and "Dust / debris" rows of `templates/ruggedization_test_matrix.md` and the inspection checklist (electronics compartment dry, cable glands intact, insect screen clear).
- **Supports:** the framework recommendation on sealing strategy, gland/connector placement, and drain-path geometry, and the literature observations on moisture-driven board corrosion, glue/coating aging, water intrusion at printed-part joints, and the heat-vs-sealing tension in fully sealed IP boxes (Theisen et al.; Grimsley et al.; consolidated material-options table).

## 4. Tooling and reproducibility

- **CAD:** parametric solid modeler with a single driving parameter table per variant; geometry exported per variant for meshing.
- **FEA/CFD:** steady-state thermal and CHT for Sections 3.2 to 3.3; static, transient, and modal structural solvers for Section 3.4. Specific package is the author's choice; the requirement is that mesh, boundary conditions, material inputs, and solver settings are recorded so a run is reproducible.
- **Inputs ledger:** every material/optical/load input is recorded with its source and its status (measured, datasheet, bounded assumption). Unknowns are swept, not guessed.
- **Outputs:** model files and result tables are kept under version control alongside this plan; the bias-vs-variant table (3.2) is the headline deliverable that the paper and framework cite.

## 5. Claim-mapping summary

| Analysis | Deliverable | Validation hook | Paper claim / framework recommendation |
|---|---|---|---|
| 3.1 Parametric CAD | Parameter table + per-variant drawings | As-built vs. V0 model check | Methods figure; record geometry parameters, not just photos |
| 3.2 Thermal / CHT | **Bias-vs-variant table** (Delta-T, RH and gas knock-on, attributed) | Solar-heat-soak test + co-location bias | Passive shield reduces solar bias; error is ventilation-limited; separate sensors from internal heat; prefer light/low-absorptance surfaces |
| 3.3 Venting | Vent-sizing / plate-gap design rule | Low-wind heat-soak behavior | Vent area/orientation and plate spacing; avoid open-bottom/weak ventilation |
| 3.4 Structural / modal | Stress margins, deflection, natural frequencies | Handling/vibration + mounting rows of test matrix | Ruggedization extension: wall thickness, infill/print orientation, mount stiffness, fasteners (screening only) |
| 3.5 Sealing / tolerance | IP-style ingress + gland/drain routing assessment | Rain, humidity, dust rows + inspection checklist | Sealing strategy, gland placement, drain geometry; manage heat-vs-sealing tradeoff |

## 6. Sequence and dependencies

1. Inventory the lab box (`templates/baseline_system_description.md`) to fix V0 dimensions and internal heat load. *(Blocks quantitative 3.2; until then 3.2 runs on flagged placeholders.)*
2. Build parametric CAD (3.1).
3. Run thermal/CHT (3.2) and venting (3.3) together, since venting feeds the achievable bias reduction.
4. Run structural/modal (3.4) and sealing (3.5) for the ruggedization extension.
5. Compare every prediction against the corresponding `ruggedization_test_matrix.md` row and co-location data; report agreement or gap. No simulation output is promoted from "prediction" to "finding" until this step is done.
