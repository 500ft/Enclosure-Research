# CAD / Thermal-FEA workstream (install-pending scaffolding)

This directory holds the finite-element scaffolding for the thermal analysis in
`docs/cad_fea_plan.md` Section 3.2. **Nothing here runs a solve today** -- the
CAD kernel and FEA stack are not installed in this environment. It is staged so
the same files run end-to-end once the toolchain exists.

## What is the actual result right now?

The current, runnable deliverable is the **lumped analytical model**:

```bash
python3 analysis/thermal_bias.py
```

That model gives the bias-vs-variant table (`analysis/thermal_bias_results.md`)
and is the **analytical baseline** the conjugate-heat-transfer (CHT) FEA here
will later refine. Every number in both places is a **SIMULATION** output,
pending lab and co-location data -- no regulatory-grade or certified claim.

## Files

- `thermal_fea_pipeline.py` -- install-pending STUB of the CHT pipeline
  (geometry -> mesh -> steady thermal/CHT solve -> sensor delta-T). Each stage is
  a `NotImplementedError` stub. Running it today just prints install/run steps;
  it does **not** require the toolchain to succeed.

## Why FEA is *not* needed for the headline number

The paper's core error mechanism -- radiative self-heating biasing T/RH (and gas)
-- is first order. A lumped steady-state energy balance (absorbed solar vs.
convective + radiative loss, with an internal self-heating source) bounds the
sensor delta-T per variant without a mesh. See `analysis/thermal_bias.py`.

What the CHT FEA *adds* on top of the baseline:

1. The **internal natural-convection field** and plate-to-air coupling that the
   lumped model approximates with a single `shield_air_preheat` term.
2. A **spatial** sensor-surface temperature (gradients, hot spots) instead of one
   lumped node.
3. **Geometry-driven** sweeps (plate count/spacing, vent area, sensor position)
   straight from the parametric CAD.

## Install (pending)

See the header of `thermal_fea_pipeline.py` for exact, copy-pasteable steps.
Summary of the two supported stacks:

- **Conjugate heat transfer:** CadQuery (geometry) + gmsh (mesh) +
  OpenFOAM `chtMultiRegionFoam` *or* Elmer FEM (multiphysics).
- **Decoupled fallback:** CadQuery + gmsh + SfePy/CalculiX thermal solve with
  convection entered as Robin BCs taken from the *same* correlations as the
  lumped model, so the two stay consistent.

## Consistency rule

The FEA boundary conditions reuse the **same input ledger**
(`thermal_bias.ASSUMPTIONS`: alpha, eps, T_sky offset, h(wind), internal load,
plate/vent geometry). The lumped baseline and the FEA refinement are driven from
one source of truth and are cross-checked, not allowed to drift.
