# Contributing

This repository keeps literature, field-analysis code, figures, and manuscript
statements connected. A contribution should update every affected layer.

## Development setup

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

## Literature contributions

For every new paper or standard:

1. add or update its entry in `paper/references.bib`;
2. add it to `literature/literature_matrix.csv`;
3. record its sensors, materials, geometry, and setup in
   `literature/sensor_material_geometry_summary.md`;
4. create `ProConsList/<citation-key>.md` from
   `ProConsList/TEMPLATE.md`; and
5. run `python analysis/check_literature_coverage.py`.

Do not infer materials, dimensions, or test conditions that a source does not
report.

## Analysis contributions

- Keep simulation outputs separate from field measurements.
- Record units and assumptions beside every new model input.
- Regenerate affected figures from the analysis script rather than editing them
  by hand.
- Do not commit private or owner-supplied raw deployment exports.
- If a metric changes, update the figure, manuscript text, and any PI deliverable
  derived from it.

## Checks

```bash
python -m compileall -q analysis
python analysis/check_literature_coverage.py
python analysis/thermal_bias.py --no-figure
```

## Pull requests

State which source, dataset, model, or deliverable changed; list the commands
used to regenerate outputs; and identify any lab measurements still needed.
