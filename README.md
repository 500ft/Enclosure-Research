# Enclosure Research

Working repository for the paper:

**Calibration, Ambient Conditions, and Integration Effects on the Accuracy and Autonomy of a Low-Cost Outdoor Multi-Sensor Box**

## Current V1.0 scope

This repo has been reframed from an enclosure-only study into a full deployed sensor-box evaluation. The current draft focuses on:

- sensor accuracy against reference measurements
- calibration improvement from raw to corrected data
- autonomy, uptime, data completeness, and maintenance burden
- enclosure material, geometry, airflow, sealing, and weather exposure
- a decision framework for future lab sensor-box designs

## Military installation extension

The `military-application-implementation` branch adds a defense-relevant extension for rugged, low-cost, validated environmental sensing hardware. The recommended framing is a dual-use, non-regulatory sensing node for smoke, particulate matter, heat, humidity, and base air-quality awareness at military installations, training ranges, battery/storage areas, and emergency-response sites.

This extension should not claim regulatory-grade monitoring, fire detection, CBRN detection, or formal military qualification unless those claims are supported by specific certification and test evidence.

## Files

- `paper/manuscript_v1.md` - working manuscript V1.0
- `paper/references.bib` - first-pass bibliography
- `literature/literature_matrix.csv` - literature extraction matrix
- `literature/sensor_material_geometry_summary.md` - verified sensor, material, geometry, and setup comparison
- `literature/additional_literature_list.md` - prioritized list of newly identified research
- `ProConsList/` - required per-paper sensor and physical-box pros/cons analyses
- `templates/baseline_system_description.md` - lab box inventory template
- `templates/deployment_log.csv` - field deployment log template
- `templates/calibration_metrics.md` - metric definitions and reporting table
- `templates/installation_deployment_plan.md` - defense-relevant site planning template
- `templates/installation_deployment_log.csv` - installation-style event and maintenance log
- `templates/ruggedization_test_matrix.md` - practical outdoor ruggedization test checklist
- `military_applications/research_brief.md` - source-backed defense use-case research brief
- `military_applications/validation_matrix.md` - validation criteria for installation awareness
- `analysis/compute_metrics.py` - helper script for first-pass accuracy, uptime, and completeness metrics
- `deliverables/PI_Literature_Synthesis_Outdoor_Sensor_Box.pdf` - PI-ready synthesis of all 19 literature sources
- `deliverables/PI_Literature_Synthesis_Outdoor_Sensor_Box.docx` - editable version of the PI literature synthesis

## Current PI Deliverable

The literature synthesis summarizes every source currently referenced in the repository. For each paper, it records:

- sensors used;
- reported materials and enclosure geometry;
- experimental setup;
- main result and brief conclusion;
- relevance to the proposed lab-box study;
- evidence-supported considerations for the experimental phase.

The synthesis also recommends framing the experiment around the current box baseline, a strong passive shield, and an optional actively aspirated accuracy benchmark.

## Next data needed from the lab

Before the results section can become a real results section, collect:

- exact sensor model names and datasheets
- microcontroller/logger model
- power system details, battery capacity, solar panel if any
- enclosure material and geometry
- sensor placement, venting, sealing, and cable routing
- logging interval and storage/transmission method
- reference instrument used for co-location
- deployment timestamps, maintenance events, and failure notes

## Adding Literature

Every new paper must include a sensor-selection and physical-box analysis in `ProConsList/`. Follow `ProConsList/README.md` and use `ProConsList/TEMPLATE.md`. Run:

```bash
python3 analysis/check_literature_coverage.py
```

before considering a literature update complete.
