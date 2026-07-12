# Progress update email — Prof. Guibaud (2026-07-12)

*Supersedes the 2026-07-08 draft; covers May 20 → July 12.*

**To:** Prof. Augustin Guibaud
**Subject:** Sensor-box study — progress since late May, and three decisions I need from you

---

Hi Prof. Guibaud,

Here's where the low-cost outdoor sensor-box study stands since late May. Short version: the project went from an enclosure-only idea to a full manuscript scaffold with a verified literature base, a first quantitative thermal model, and standards-anchored methods — everything except the results sections, which wait on lab data.

**What exists now**

- **Manuscript v1** framed around the deployed box as a system: calibration, ambient-condition effects, autonomy/reliability, and enclosure design, ending in a decision framework for future lab boxes. Results sections are scaffolded, pending data.
- **Literature base: 23 sources** — 19 papers plus 4 standards/protocols (EPA air-sensor collocation protocols, WMO-No. 8, ASTM D8406-22, CEN/TS 17660-1), each with a structured extraction row and a per-paper analysis. A PI-ready literature synthesis PDF and short cover memo are in the repo whenever you want them.
- **A first-order solar self-heating model** predicting the enclosure's warm/dry bias per design variant: closed baseline box ~+8 to +23 °C (reads ~19–35 %RH dry), passive multi-plate shield ~1–4 °C, aspirated ~1 °C. All values are labeled simulation predictions, not measurements.

**Rigor pass (this month)**

- Every citation was verified against its source — this caught and fixed a wrong author list and a wrong venue/year in the bibliography before they could reach a referee.
- The thermal model is now bracketed against published *measured* shield errors (Tarara & Hoheisel; Holden; Botero-Valencia; Theisen). The passive-shield and aspirated predictions sit inside the measured bands; the closed-box prediction has no direct measured analog in the literature, so it's explicitly flagged as the thing our solar heat-soak test must check — a falsifiable prediction rather than an assumption.
- Methods are anchored to published protocols: the 30-day co-location target now matches EPA base testing (≥3 identical units against reference monitors for ≥30 days), siting follows WMO-No. 8 practice, and the analysis requires documenting the reference instrument's own uncertainty.

**Three decisions I need from you**

1. **Repo visibility, authorship, licensing.** I switched the GitHub repo to private as the safe default; happy to keep it that way or open it back up — your call, along with intended authorship order.
2. **Data timeline.** Does the lab's existing dataset (or a reference instrument + deployment site for a new co-location) land this summer? This decides whether the paper becomes a results paper or an honest literature-plus-experimental-design contribution.
3. **Acceptance thresholds.** Before data arrives, I'd like 15–20 minutes to agree on pass/fail thresholds (calibrated error, uptime, maintenance frequency) so we define success before we see results, not after.

Happy to walk through any of this whenever works for you.

Best,
[Your name]
NYU — CUSP IgNYte Lab
