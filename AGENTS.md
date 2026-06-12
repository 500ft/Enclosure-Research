# Repository Research Rules

When adding any paper or literature source to this repository:

1. Add or verify its citation in `paper/references.bib`.
2. Add it to `literature/literature_matrix.csv`.
3. Record its sensors, reported materials, geometry, and experimental setup in `literature/sensor_material_geometry_summary.md`.
4. Create a matching `ProConsList/<citation-key>.md` using `ProConsList/TEMPLATE.md`.
5. Include pros and cons of the sensor selection.
6. Include pros and cons of the physical box, material, geometry, airflow, and placement.
7. If no physical box is used or details are not reported, analyze the experimental setup and explicitly state the evidence limitation.
8. Run `python3 analysis/check_literature_coverage.py`.

Do not infer unreported materials or geometry.

