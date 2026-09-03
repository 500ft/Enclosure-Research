# Reviewer / PI-Triage Backlog (STORM analysis, 2026-07-13)

Findings from a STORM multi-perspective review of `paper/manuscript_v1.md`,
captured for the PI conversation. **Leads for author/PI triage, not applied
edits.** Every proposed citation is marked *verify against the primary source
before adding*. Consistent with the paper's no-regulatory-claims constraint;
nothing here overclaims — several items make the paper more conservative.

Audience note: written when this repository was private, on the assumption that it stayed
with the lab. **The repository is public as of 2026-09-03 with the PI's approval** (see
ROADMAP.md), so read these as notes intended for the author and PI that are now visible to
anyone. Nothing here overclaims, but the framing assumed a private audience.

Status of each item as of this note.

## Grounded — worth adding (peer-reviewed / standard)

1. **WMO CIMO anchoring — DONE (2026-07-09, commit a5dae5e).** WMO No. 8 added
   to the literature and standards support added to Methods. Remaining polish:
   state the IOM-136 achievable-uncertainty target (~+-0.2 C) as the decision-
   framework reference line, and tie Holden's +7.4 C open-bottom error to the
   CIMO comparability language.

2. **Nighttime radiative-cooling (cold) bias is not modeled — HIGHEST-VALUE,
   NOT DONE.** The analytical self-heating model and the FEA plan are solar-only
   (predict warm bias). Passive shields also read LOW at night under clear, calm
   skies via longwave exchange with the cold sky (documented 1-3 K air/surface
   deltas, worst at low wind). Fix: the energy-balance model already has a
   radiative term -- extend it to a negative effective sky temperature at night
   and report bias vs. time-of-day, not just worst-case daytime. Makes the one
   substantial lab-independent contribution two-sided. Grounded in peer-reviewed
   radiative-cooling literature (verify specific cites).

3. **PM humidity correction under-specified IF the box has an optical PM sensor
   -- NOT DONE, conditional.** Low-cost optical PM sensors overestimate at
   RH > 70% via hygroscopic growth; the established fix is a kappa-Kohler /
   RH-growth-factor correction (~40% RMSE reduction; nonlinearity onset ~50% RH),
   which linear + MLR will not capture. Sources to verify: AMT 2024 (Copernicus,
   hygroscopic growth calibration for low-cost PM2.5); MDPI Sensors 2018 (RH
   correction for low-cost PM). Add a PM-specific RH-correction note only if PM
   is actually in the box (currently a TODO in the inventory).

4. **Membrane breather vents missing from the enclosure toolbox -- NOT DONE
   (datasheet-flagged).** The sealing section covers glands/drains/gaskets/IP
   boxes but not the standard condensation fix: a PTFE/ePTFE membrane breather
   vent (Gore/Porex-class) that equalizes pressure and vents water vapor while
   blocking liquid/dust to IP67/68. Directly addresses the condensation-corrosion
   failure that ended Theisen's RH board at month 6 (already cited). The two-zone
   sealed-electronics design should specify one. Add as an engineering-practice
   recommendation (datasheet-class, verify), same handling as filament datasheets.

## Open questions -- framing / method, not new citations

5. **Calibration is single-box; the lab's value is density.** Unaddressed:
   sensor-to-sensor transfer (calibrate one, deploy many) and recalibration
   cadence (listed as a metric, no method). Connects to the QUANT/Winter drift
   findings already cited. Frame as "V1 = single-box; network transfer +
   recalibration triggering = V2."

6. **No stated QA/QC flagging pipeline** (range / step / persistence / spike /
   flatline) before analysis -- a stuck sensor inflates completeness while
   corrupting accuracy. Add a short QC subsection; methods hygiene, not novelty.

7. **No measurement-uncertainty budget / reference traceability.** State the
   reference instrument's own uncertainty and timestamp-matching error so
   "error vs reference" is not conflated with "error." Minor.

## Minor -- one-liners

8. Cold-weather power: recommend LiFePO4 vs Li-ion sub-0 C charging + MPPT
   (Arctic COAT cited for failures but no chemistry recommendation given).
9. Anti-insect mesh countermeasure (Theisen's insect-nesting cited, no screen
   proposed).
