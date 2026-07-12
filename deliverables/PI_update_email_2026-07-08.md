# Progress update email — Prof. Guibaud (2026-07-08)

**To:** Prof. Augustin Guibaud
**Subject:** Sensor-box study — progress update (mid-May → early July)

---

Hi Prof. Guibaud,

A short update on the low-cost outdoor multi-sensor box study since our last check-in. The short version: the project has moved from a broad enclosure idea to a documented, literature-backed research plan, and this past two weeks I added the first quantitative modeling — a solar self-heating bias analysis that puts numbers on the "the enclosure reads hot" problem.

**Where it stands**

- **Manuscript v1** drafted around the full deployed sensor box (calibration, ambient-condition effects, autonomy, and enclosure design), not just the shell. Results sections are scaffolded and waiting on lab data.
- **Literature base complete:** 19-source extraction matrix with a matching per-paper sensor + physical-box pros/cons analysis for every entry, consolidated into materials/geometry design tables.
- **PI-ready deliverables:** a full literature synthesis (PDF/DOCX) and a short cover memo. A detailed progress report is attached.
- **Data-collection infrastructure ready:** baseline inventory template, deployment log, calibration-metric definitions, and first-pass analysis scripts — so a co-location deployment can be logged and analyzed from day one.

**New since mid-June — CAD/FEA workstream**

- Wrote a full **CAD/FEA analysis plan** tying each modeled result to a specific paper claim: thermal/conjugate-heat-transfer, passive-shield venting, structural/modal screening, and sealing/tolerance.
- Ran a first **analytical solar self-heating model**. Predicted sensor temperature rise above true ambient under worst-case sun: baseline closed box **+8 to +23 °C (≈ −35 %RH bias)**, passive multi-plate shield **~1–4 °C**, aspirated reference **~1 °C**. Sensitivity analysis says the baseline bias is driven hardest by surface color/optical properties — painting it white alone cuts the error roughly 4×.
- **Important caveat:** every one of these numbers is a simulation prediction, explicitly flagged as *pending lab and co-location data*. Nothing is presented as a measured or certified result.

**What I need from you**

- The roadmap's first step is really yours to settle: the repo is currently **public** — I want to confirm that's OK under lab/NYU policy, or make it private. Same for intended **authorship order and licensing**.
- Whether lab **measurement data** (sensor models, power, deployment logs, reference co-location) is likely to land this summer — that decides whether this becomes a results paper or a literature-review + experimental-design contribution.
- If data is available: which **reference instrument** I can co-locate against, and a deployment site.

Happy to walk through any of this whenever works for you.

Best,
[Your name]
NYU — CUSP IgNYte Lab

---

*Attachment: `pi_progress_since_may15.pdf` — note: current PDF covers through June 19 and should be regenerated to include the CAD/FEA work before sending.*
