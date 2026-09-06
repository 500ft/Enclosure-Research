# Enclosure-Research — individual CAD tasks

Prepared 2026-09-06. **Planning only: no CAD model, drawing, fabrication, calibration or physical result was produced by this amendment.**

[CAD_TASKS.csv](CAD_TASKS.csv) is the sole status ledger for this new CAD phase. The earlier [SPRINT_TASKS.csv](SPRINT_TASKS.csv) remains the authority for the separate 30-hour evidence-integrity sprint; its estimates and achieved software evidence are unchanged. This plan expands mechanical work orders, not publication or test permission. Scope tiers are in [scope.md](specs/cad-development/scope.md).

## Verified reason for the work

An existing CAD/FEA plan already names variants and geometry inputs, but does not provide individual trackable CAD tasks. The analytical comparison also requires a same-geometry painted-box control so color is not confused with shield geometry.

Inspected source documents:

- [docs/cad_fea_plan.md](cad_fea_plan.md)
- [templates/baseline_system_description.md](../templates/baseline_system_description.md)
- The older plan references `templates/ruggedization_test_matrix.md`, but that file is absent in this checkout. EN-CAD-01 must define the required CAD inspection/validation mapping; no existing test matrix or qualification is assumed.
- [analysis/thermal_bias.py](../analysis/thermal_bias.py)

## Outcome and boundaries

A reviewer can reopen editable, version-pinned geometry; regenerate neutral STEP exports; understand the assembly, critical fits and measurement datums; and distinguish design assumptions from inspected hardware. STL is only a manufacturing derivative where appropriate, not the sole editable master. For hosted CAD retain a version-specific share reference and authorized portable source/export archive; record tool/version and export settings. Do not require a particular commercial tool before checking access.

**Entry decision:** Owner supplies the baseline enclosure inventory, actual sensor/electronics interfaces and fabrication access. Active aspiration is considered only after evidence of low-wind/solar bias and a separately approved fan/reference measurement plan.

**Excluded:** No new CHT/CFD run, certified ingress rating, environmental qualification or co-location result. Do not treat baseline inventory or manufacturing as already done.

Agent owns document preparation and modeling once inputs exist; Owner owns actual component/access choices and review authority; External fabricators/operators own quotes, manufacture and facility approval. No approval, purchase, fabrication booking, IP disclosure of third-party drawings, or test run is completed by checking in this plan. Unknown critical dimensions block fabrication; conceptual placeholders must be visible and cannot become as-built evidence.

## Focused-hour allocation

The initial CAD phase is **22 estimated focused hours**, additional to the earlier software sprint. A further **4 hours** is deferred behind explicit triggers. These are estimates, not recorded work. Each day is a workload bucket after its prerequisites, not a calendar promise; quotes, calibration and facility lead times are not compressed into CAD hours.

| Workload day | Hours | Ordered tasks |
| --- | ---: | --- |
| 1 | 4 | EN-CAD-01 → EN-CAD-02 |
| 2 | 4 | EN-CAD-03 |
| 3 | 5 | EN-CAD-04 |
| 4 | 3 | EN-CAD-05 |
| 5 | 3 | EN-CAD-06 |
| 6 | 3 | EN-CAD-07 |

Critical path follows the explicit task dependencies below: input register → owner decisions → parts/fixtures → release review. Independent branches may proceed after their shared inputs close.

## Individual work orders

All output paths below are **proposed NEW deliverables**, not existing artifacts. Current task state appears only in the CSV; the headings below define acceptance, not completion.

### EN-CAD-01 — Define baseline/painted-control/shield parameter contract

- Owner: Agent; priority: P1; estimate: 2 h; workload day: 1.
- Dependencies: none; source inspection is available now.
- Scope: initial CAD phase, subject to its input/owner gate.
- Proposed deliverables: `cad/enclosure/parameters.csv; cad/enclosure/variant-contract.md; cad/enclosure/inspection-requirements.md`.
- Done when: Map V0, same-geometry painted V0 and passive V1 to geometry, finish and heat-source inputs. Keep optical properties separate from material geometry and source every dimension or flag unknown.
- Verification and evidence to retain: Review against thermal_bias.py and cad_fea_plan.md; retain a variant matrix showing which variables change. Define a prospective rain/humidity/handling inspection-to-interface map because the older referenced test matrix is absent; test loads and acceptance require later owner review.

### EN-CAD-02 — Inventory and approve actual enclosure/component geometry

- Owner: Owner; priority: P1; estimate: 2 h; workload day: 1.
- Dependencies: EN-CAD-01.
- Scope: initial CAD phase, subject to its input/owner gate.
- Proposed deliverables: `cad/enclosure/baseline-inputs.md`.
- Done when: Complete the existing baseline-system template with dimensions, vents, drains, glands, sensor/electronics separation and heat-source provenance; identify manufacture capability and disclosure permissions for supplied drawings.
- Verification and evidence to retain: Retain dimensioned inspection photos or authorized drawing references and unresolved fit tolerances.

### EN-CAD-03 — Model the as-built baseline and identical-geometry paint control

- Owner: Agent; priority: P1; estimate: 4 h; workload day: 2.
- Dependencies: EN-CAD-02.
- Scope: initial CAD phase, subject to its input/owner gate.
- Proposed deliverables: `cad/enclosure/v0/ (editable source, STEP, sections)`.
- Done when: Model lid, openings, mounts and internal components from inventory. Painted V0 reuses exactly the baseline geometry and placement; only declared finish/coating treatment differs. Do not guess critical lab dimensions.
- Verification and evidence to retain: Overlay geometry exports or compare invariant dimensions; retain model-to-inventory discrepancy table and finish metadata.

### EN-CAD-04 — Model passive shield and two-zone component mounts

- Owner: Agent; priority: P1; estimate: 5 h; workload day: 3.
- Dependencies: EN-CAD-02, EN-CAD-03.
- Scope: initial CAD phase, subject to its input/owner gate.
- Proposed deliverables: `cad/enclosure/v1/ (source, STEP, assembly drawing)`.
- Done when: Parameterize plate count, gaps, sensor stand-off, ventilated sensing and sealed electronics zone; show fasteners and service access. Preserve reference sensor positions needed to interpret comparison.
- Verification and evidence to retain: Regenerate reviewed parameter bounds; inspect vent area, shadow/air paths and assembly interference. These are geometric checks, not airflow or temperature validation.

### EN-CAD-05 — Detail glands, drainage, seals and test-mount interfaces

- Owner: Agent; priority: P1; estimate: 3 h; workload day: 4.
- Dependencies: EN-CAD-03, EN-CAD-04.
- Scope: initial CAD phase, subject to its input/owner gate.
- Proposed deliverables: `cad/enclosure/interfaces/ (detail drawings, tolerance table)`.
- Done when: Specify cable routing/drip paths, seal compression assumptions, drainage and shared co-location mounting datums. Avoid closing required sensing ventilation while protecting electronics.
- Verification and evidence to retain: Review section views and critical stack-ups against the prospective EN-CAD-01 inspection requirements; no absent test-matrix row or IP rating is treated as established.

### EN-CAD-06 — Prepare analysis geometry and boundary-condition mapping

- Owner: Agent; priority: P1; estimate: 3 h; workload day: 5.
- Dependencies: EN-CAD-03, EN-CAD-04, EN-CAD-05.
- Scope: initial CAD phase, subject to its input/owner gate.
- Proposed deliverables: `cad/enclosure/analysis-export/ (STEP, simplification log, boundary map)`.
- Done when: Create simplified solids with named solar, ambient, sensor and heat-source surfaces; preserve vent dimensions and material interfaces. Log removed details and geometry revision so later meshes can be traced.
- Verification and evidence to retain: Reopen geometry and compare volume/opening areas to detailed CAD; review boundary labels and unknown optical/thermal inputs. No solver run is included.

### EN-CAD-07 — Release drawings, visual comparison and inspection pack

- Owner: Agent; priority: P1; estimate: 3 h; workload day: 6.
- Dependencies: EN-CAD-05, EN-CAD-06.
- Scope: initial CAD phase, subject to its input/owner gate.
- Proposed deliverables: `cad/enclosure/release/ (BOM, drawings, renders, source/export manifest)`.
- Done when: Provide editable source, STEP and fabrication drawings, consistent section/exploded views for baseline, paint control and shield, plus as-built inspection checklist. Mark models predicted and fabrication pending.
- Verification and evidence to retain: Reproduce exports and dimensions from source; check units, source references and variant isolation with a second reviewer.

### EN-CAD-08 — Model optional active-aspiration reference

- Owner: Agent; priority: P2; estimate: 4 h; workload day: conditional.
- Dependencies: EN-CAD-07.
- Scope: trigger-gated extension; not required for initial CAD release.
- Proposed deliverables: `cad/enclosure/v2/ (source, STEP, fan and flow-path drawing)`.
- Done when: Trigger requires documented low-wind/solar bias plus approved fan/reference plan. Isolate fan heat, vibration, airflow path and reference-sensor placement; do not replace passive primary comparison.
- Verification and evidence to retain: Review fan curve/interface source, electrical/thermal assumptions and matched comparison conditions before promoting V2.

## Release review and overrun rule

Every release includes an assembly/exploded view, a critical section/detail view and a measurement/inspection setup view. Captions identify the question illustrated, source revision, dimensions/units and **CAD prediction—not measured** state; cite vendor/hand-calculation references actually used. Render quality is not evidence of fit or performance.

Before marking a CAD task done, attach real source/export identities, regeneration instructions and the corresponding acceptance evidence in CAD_TASKS.csv. A second AI pass is a development check, not independent human or laboratory validation. Retain failed fits and unresolved assumptions; do not silently tune experimental geometry after observing confirmation data.

If the phase overruns, postpone decorative renders, optional variants and mechanism extensions first. Do not remove required fits, safety interfaces, reference controls, source traceability or measurement access. Fabrication-release review, apparatus commissioning and physical evaluation remain separate future actions; updated geometry may require a new prospective analysis/reference freeze. Preparing drawings does not close an existing physical-readiness or publication blocker.

## PR review scope

This amendment changes task planning and navigation only. It is stacked on the open evidence-integrity PR so its diff excludes earlier fixes. No software behavior or frozen scientific threshold is changed. Review task dependencies and claim boundaries now; actual CAD acceptance is assessed when those artifacts exist.
