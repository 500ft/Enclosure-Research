# Enclosure-Research — revised CAD work orders

For the plain-language list of physical parts and assemblies, see [CAD_ITEMS.md](CAD_ITEMS.md). It maps to the existing work orders without adding tasks, estimates or completion status.

Amended 2026-09-06 after source review. Planning only: no CAD, fixture, fabrication or calibration result exists from this amendment.

**Main-branch placement authorized — 2026-09-06 (America/New_York).** The owner explicitly requested merging these PRs to their respective main branches. This supersedes the earlier placement hold for this PR's current documents and prerequisite integrity changes; it is not a blanket policy for future private material. Hardware, measurement and disclosure gates remain unchanged. See [CAD_REVIEW_DISPOSITION.md](CAD_REVIEW_DISPOSITION.md).

[CAD_TASKS.csv](CAD_TASKS.csv) is the sole CAD status ledger. [SPRINT_TASKS.csv](SPRINT_TASKS.csv) remains byte-preserved for the earlier integrity sprint. [Scope tiers](specs/cad-development/scope.md) and [reproduction checks](CAD_PLAN_CHECKS.md) describe this amendment, not physical validation.

## Verified source context

An existing CAD/FEA plan already names variants and geometry inputs, but does not provide individual trackable CAD tasks. The analytical comparison also requires a same-geometry painted-box control so color is not confused with shield geometry.

Inspected source documents:

- [docs/cad_fea_plan.md](cad_fea_plan.md)
- [templates/baseline_system_description.md](../templates/baseline_system_description.md)
- The older plan references `templates/ruggedization_test_matrix.md`, but that file is absent in this checkout. EN-CAD-01 must define the required CAD inspection/validation mapping; no existing test matrix or qualification is assumed.
- [analysis/thermal_bias.py](../analysis/thermal_bias.py)


## Revised finish line and priority

Park CAD until the actual lab-box inventory and explicit owner promotion exist. Instantiate the existing section 3.1 contract instead of duplicating it; thermal/field verification remains separate.

## Tool and verification decision

**Selected design approach:** CadQuery code-CAD for parameterized families and neutral STEP verification; Onshape for hand-modeled fixtures with confirmed owner account/access. No Onshape automation, credentials or paid access is assumed. Agent owns code-CAD generators/tests; Owner or an authorized CAD operator owns interactive Onshape work. Lack of Onshape access blocks only affected fixture modeling and requires a documented alternative, not the entire parameter pipeline.

The dedicated tooling task budgets environment locking and CI setup. Pin actual Python/CadQuery/OCP versions only after a clean isolated install plus STEP export/reimport smoke test. No version, environment or geometry CI is claimed tested today. CadQuery's official [installation](https://cadquery.readthedocs.io/en/stable/installation.html) and [STEP import/export](https://cadquery.readthedocs.io/en/stable/importexport.html) docs establish the chosen workflow, not a completed build.

Required future automated sequence: read reviewed parameters.csv → reject invalid/missing dimensions and units → regenerate native geometry → export STEP → reimport into a fresh process → calculate geometric metrics → assert against predeclared tolerances. Geometry acceptance uses numeric JSON plus source/export identity; retain screenshots only for explanatory views. A golden image or a hash is not a geometry test. Tests include analytic nominal cases, registered bounds and invalid cases; expected values cannot be copied from the candidate's own output. CAD geometry tests do not validate physical stiffness, safety or fatigue.

Proposed commands (files DO NOT exist yet): `python cad/generate.py --parameters <registered-parameters.csv> --output <temporary-output>`; `python -m pytest cad/tests -q`. The tooling task must replace placeholders with actual checked-in defaults and wire CI before a model task can close.

## Rebaselined allocation

**0 estimated hours in the prioritized phase; 28 estimated hours parked.** This supersedes the previous CAD allocation, not the original 30-hour software sprint. Only tasks marked todo are executable now; blocked/parked estimates are not scheduled work. Owner decisions, fabrication lead times and external calibration do not shrink into focused hours.

| Workload day | Hours | Order |
| --- | ---: | --- |
| Parked | 0 active | Owner/research entry decision required |

## Individual work orders

IDs retain continuity with the first PR. New IDs represent split inputs, tooling or release tasks; display order is execution priority rather than numerical ID order. Proposed deliverables below are NEW, not present artifacts. Current status exists only in CAD_TASKS.csv.

### EN-CAD-02 — Inventory and approve actual enclosure/component geometry

- Owner: Owner; priority: P2; estimate: 2 h; day: conditional.
- Dependencies: none.
- Proposed output: `NEW cad/enclosure/baseline-inputs.md`.
- Done when: Complete the existing baseline-system template with dimensions, vents, drains, glands, sensor/electronics separation and heat-source provenance; identify manufacture capability and disclosure permissions for supplied drawings.
- Verification/evidence: Retain dimensioned inspection photos or authorized drawing references and unresolved fit tolerances.

### EN-CAD-01 — Instantiate existing CAD contract from inventory

- Owner: Agent; priority: P2; estimate: 1 h; day: conditional.
- Dependencies: EN-CAD-02.
- Proposed output: `NEW cad/enclosure/parameters.csv; cad/enclosure/inspection-requirements.md`.
- Done when: Use docs/cad_fea_plan.md section 3.1 as design authority and populate its parameter table from inventory. Do not create a competing design specification. Add only same-geometry paint-control metadata and the missing inspection-to-interface mapping.
- Verification/evidence: Review against thermal_bias.py and cad_fea_plan.md; retain a variant matrix showing which variables change. Define a prospective rain/humidity/handling inspection-to-interface map because the older referenced test matrix is absent; test loads and acceptance require later owner review.

### EN-CAD-09 — Establish code-CAD regeneration and CI geometry tests

- Owner: Agent; priority: P2; estimate: 3 h; day: conditional.
- Dependencies: EN-CAD-01.
- Proposed output: `NEW cad/requirements.lock; cad/generate.py; cad/tests/; .github/workflows/cad-geometry.yml`.
- Done when: Use CadQuery for parameter-driven families and neutral STEP checks, Onshape for hand-modeled fixtures after confirming account/access. Pin Python/CadQuery/OCP dependencies after a clean isolated install and export/reimport smoke test. Add geometry CI before accepting a parametric model; screenshots are supplementary, not acceptance.
- Verification/evidence: Proposed commands, NOT YET IMPLEMENTED: python cad/generate.py --parameters <registered-parameters.csv> --output <temporary-output>; python -m pytest cad/tests -q. Assert geometry metrics against a reviewed contract with declared tolerances; prove failure on an altered parameter, invalid dimensions, missing inputs and bad STEP. Retain version lock, numeric JSON and STEP outputs.

### EN-CAD-03 — Model the as-built baseline and identical-geometry paint control

- Owner: Agent; priority: P2; estimate: 4 h; day: conditional.
- Dependencies: EN-CAD-01;EN-CAD-09.
- Proposed output: `NEW cad/enclosure/v0/ (editable source, STEP, sections)`.
- Done when: Model lid, openings, mounts and internal components from inventory. Painted V0 reuses exactly the baseline geometry and placement; only declared finish/coating treatment differs. Do not guess critical lab dimensions.
- Verification/evidence: Overlay geometry exports or compare invariant dimensions; retain model-to-inventory discrepancy table and finish metadata.

### EN-CAD-04 — Model passive shield and two-zone component mounts

- Owner: Agent; priority: P2; estimate: 5 h; day: conditional.
- Dependencies: EN-CAD-03;EN-CAD-09.
- Proposed output: `NEW cad/enclosure/v1/ (source, STEP, assembly drawing)`.
- Done when: Parameterize plate count, gaps, sensor stand-off, ventilated sensing and sealed electronics zone; show fasteners and service access. Preserve reference sensor positions needed to interpret comparison.
- Verification/evidence: CadQuery must regenerate plate/gap variants from registered parameters.csv, export/reimport STEP and assert gaps, count, vent/open area, envelope and positive solid volumes against declared tolerances. Test bounded inputs and invalid gap/count failures in CI; no thermal/airflow validation from geometry.

### EN-CAD-05 — Detail glands, drainage, seals and test-mount interfaces

- Owner: Agent; priority: P2; estimate: 3 h; day: conditional.
- Dependencies: EN-CAD-03;EN-CAD-04.
- Proposed output: `NEW cad/enclosure/interfaces/ (detail drawings, tolerance table)`.
- Done when: Specify cable routing/drip paths, seal compression assumptions, drainage and shared co-location mounting datums. Avoid closing required sensing ventilation while protecting electronics.
- Verification/evidence: Review section views and critical stack-ups against the prospective EN-CAD-01 inspection requirements; no absent test-matrix row or IP rating is treated as established.

### EN-CAD-06 — Prepare analysis geometry and boundary-condition mapping

- Owner: Agent; priority: P2; estimate: 3 h; day: conditional.
- Dependencies: EN-CAD-03;EN-CAD-04;EN-CAD-05.
- Proposed output: `NEW cad/enclosure/analysis-export/ (STEP, simplification log, boundary map)`.
- Done when: Create simplified solids with named solar, ambient, sensor and heat-source surfaces; preserve vent dimensions and material interfaces. Log removed details and geometry revision so later meshes can be traced.
- Verification/evidence: Reopen geometry and compare volume/opening areas to detailed CAD; review boundary labels and unknown optical/thermal inputs. No solver run is included.

### EN-CAD-07 — Release drawings, visual comparison and inspection pack

- Owner: Agent; priority: P2; estimate: 3 h; day: conditional.
- Dependencies: EN-CAD-05;EN-CAD-06.
- Proposed output: `NEW cad/enclosure/release/ (BOM, drawings, renders, source/export manifest)`.
- Done when: Provide editable source, STEP and fabrication drawings, consistent section/exploded views for baseline, paint control and shield, plus as-built inspection checklist. Mark models predicted and fabrication pending.
- Verification/evidence: Reproduce exports and dimensions from source; check units, source references and variant isolation with a second reviewer.

### EN-CAD-08 — Model optional active-aspiration reference

- Owner: Agent; priority: P2; estimate: 4 h; day: conditional.
- Dependencies: EN-CAD-07.
- Proposed output: `NEW cad/enclosure/v2/ (source, STEP, fan and flow-path drawing)`.
- Done when: Trigger requires documented low-wind/solar bias plus approved fan/reference plan. Isolate fan heat, vibration, airflow path and reference-sensor placement; do not replace passive primary comparison.
- Verification/evidence: Review fan curve/interface source, electrical/thermal assumptions and matched comparison conditions before promoting V2.

## Stop and release rules

Do not equate prepared drawings with fabricated/inspected apparatus. Unknown fit-critical dimensions block manufacture. Owner/facility review, actual metrology and prospective reference freezes remain separate gates. No spending, manufacture, pressurization, rotor operation, flight, publication or new third-party drawing disclosure is authorized here.

If time overruns, cut decorative views and already-parked variants first. Keep reference controls, fit/clearance tests, source provenance, filled measurement budgets and pre-load model freeze. Update estimates explicitly rather than claiming blocked hours as progress. Every future public visual needs a source/version, problem explained and CAD-only label.
