# Enclosure-Research — tasks to completion

> **Objective.** Produce the strongest, most honestly-packaged evidence — not a completed
> project. Priority flows from leverage (does it unblock other work, or add decisive evidence)
> and from executability. Never from a calendar, and never from this project's ceiling.

Generated from an audit of the committed state of this repository. Every task is anchored to a
checked fact; no dates or estimates appear anywhere, by design.

## Two finish lines

**Ceiling.** A CHT campaign validated against a reference co-location, feeding a result the lab uses, with your name on the output.

**Floor.** The literature matrix, the analytical model with traceable numbers, and the reliability audit, handed over with predicted-versus-measured stated plainly.

The floor is the realistic finish line for anything gated on a measurement, and its tasks are
listed alongside the ceiling's — so the project is presentable even if the measurement never
happens.

_14 tasks · 7 Tier 0 · 7 executable now._

**Gate types.** `preregister` — write the threshold down *before* the thing it judges;
`external` — needs a resource or a person outside this repo; `build` — new work;
`hygiene` — reproducibility debt.

**Tiers.** 0 finish · 1 package · 2 park. A task whose blocker is not secured cannot be Tier 0
however decisive it is, which is why several measurements sit in Tier 2 with their
preregistration in Tier 0 ahead of them.

---

## Tier 0 — finish

### ER-01 · Merge PR #1 (audit/traceable-numbers)

`hygiene` · executable now

**Why it matters.** The thermal table is not committed as the artifact of record, --data-dir still defaults to a personal path, and the visibility approval is unrecorded.

**What it adds.** Numbers that trace to committed artifacts, and a recorded approval.

**Done when.** main carries the thermal table, the required --data-dir and the visibility record; research-checks stays green.

### ER-02 · Apply ci-proposed/ci-thermal-table-diff.patch and merge PR #2

`hygiene` · **blocked-on-workflow-scope** · after ER-01,XC-02

**Why it matters.** CI runs the thermal model but never compares its output to the committed table, so a model change passes silently.

**What it adds.** A CI barrier around the model's numeric output.

**Done when.** The research-checks job diffs the regenerated table against the committed one; changing an assumption goes red.

### ER-03 · Run analyze_deployment_logs.py against the log directory and commit deployment_metrics.json

`hygiene` · executable now · after ER-01

**Why it matters.** 95.7% upload success, 91.4% completeness, zero brownout resets over 22 days and the 4,079 bench-phase resets are quoted in the manuscript but derive from unversioned exports. I could verify none of them, and neither can the PI or a reviewer.

**What it adds.** Makes every quoted percentage checkable, and records which export produced it, while the raw logs stay private.

**Done when.** deployment_metrics.json committed with the input sha256s; the manuscript percentages match it.

### ER-04 · Close the authorship and licence gate with the PI

`external` · **blocked-on-PI**

**Why it matters.** ROADMAP names a co-authored paper as the single most valuable outcome, and its own gate says everything below depends on this. It is still unchecked.

**What it adds.** A settled authorship order, which is the thing the ceiling is actually made of.

**Done when.** Authorship order and licence recorded in ROADMAP.

### ER-05 · Confirm the lab measurement data timeline with the PI

`external` · **blocked-on-PI** · after ER-04

**Why it matters.** Whether co-location data arrives decides whether the ceiling or the floor is the realistic finish line, and therefore which tasks are worth doing.

**What it adds.** The information that makes the rest of this list schedulable.

**Done when.** Timeline recorded in ROADMAP.

### ER-06 · Commit the CHT validation criteria before running the campaign

`preregister` · executable now · after ER-05

**Why it matters.** cad_fea_plan.md 3.2 names the refinement but not what would make it usable. Criteria written afterwards cannot fail.

**What it adds.** A CHT campaign whose result means something.

**Done when.** Mesh-convergence criterion, benchmark and agreement band committed, no case solved.

### ER-07 · Add the nighttime radiative-cooling case to the model

`build` · executable now · after ER-06

**Why it matters.** Your own reviewer_backlog flags this as highest-value and not done: the model and the FEA plan are solar-only, so they predict warm bias while a passive shield also reads low at night under clear calm skies. A framework that only models one sign of the error will recommend the wrong enclosure.

**What it adds.** Coverage of the bias direction the current model cannot express.

**Done when.** The cold-bias case is modelled and its figure regenerates, or it is explicitly scoped out in writing.

## Tier 1 — package

### ER-08 · Wire the FEA pipeline stubs and run the campaign

`build` · executable now · after ER-06

**Why it matters.** Every stage raises NotImplementedError, so the CHT plan is scaffolding.

**What it adds.** The refined prediction the analytical model is explicitly a placeholder for.

**Done when.** Stages run, each case regenerates from committed inputs, and the mesh-convergence study is committed.

### ER-09 · Register the FEA outputs in the figure manifest with their evidence type

`hygiene` · executable now · after ER-08

**Why it matters.** New figures without manifest entries are how a repo loses track of what produced what - the discipline the two existing entries already follow.

**What it adds.** A manifest that still describes the repository after the campaign.

**Done when.** Every new figure has an entry, a runnable command and an evidence_type.

### ER-11 · Re-label every simulation-only claim against the measurement

`build` · **blocked-on-lab** · after ER-10

**Why it matters.** The SIMULATION labelling is currently consistent; after a measurement it stops being accurate.

**What it adds.** A document where measured and predicted are not confusable.

**Done when.** Each claim marked simulation-only, measurement-anchored or contradicted.

### ER-12 · Package the analytical floor for the PI

`build` · executable now · after ER-03

**Why it matters.** If lab data never lands within the window, the literature matrix, the analytical model and the reliability audit are already a deliverable.

**What it adds.** A handover the PI can use without any new measurement - the honest finish line if the campaign never runs.

**Done when.** One document committed stating what is predicted, what is measured, and what is pending.

### ER-13 · Deliver a result the lab uses

`external` · **blocked-on-PI** · after ER-12

**Why it matters.** A deliverable nobody uses does not produce a recommendation letter.

**What it adds.** Evidence the work mattered to someone other than you.

**Done when.** The PI accepts a handover artifact and the decision it feeds is named.

## Tier 2 — park

### ER-10 · Run the reference co-location and test the predicted bias bands

`external` · **blocked-on-lab** · after ER-07

**Why it matters.** The manuscript abstract already promises this test. Until it runs, the predicted 8.3-22.7 degC and 0.9-3.7 degC bands are untested.

**What it adds.** The ceiling: a measured comparison against a preregistered prediction.

**Done when.** Co-location data committed or its location declared, scored against ER-06 without adjusting the band.

### ER-14 · Get your name on the resulting output

`external` · **blocked-on-PI** · after ER-13

**Why it matters.** ROADMAP names this as the single most valuable outcome of the project.

**What it adds.** The ceiling: attributed authorship.

**Done when.** Co-authorship, acknowledgment or an attributed lab report recorded.

---

## Cross-cutting

These span repositories and are tracked identically in the others they touch.

### XC-01 · Reconcile the repo, portfolio and resume headline numbers

`hygiene` · executable now

**Why it matters.** A reviewer clicks between the three, and a disagreement there is more damaging than any single wrong number because it looks like carelessness rather than a stale file. Checked so far: the portfolio quotes 174.7 Hz (matches the repo - 163.8 Hz was the 0.20 kg placeholder tip mass, not drift) and r = 0.885 (matches), and makes no drone-mass claim. The resume was not available to check. This repository is covered by the portfolio as `outdoor-air-quality-sensor-enclosure`, so its numbers are reachable by a reader.

**Done when.** Every headline number in the portfolio and resume traced to a committed artifact, with any disagreement fixed at the source.

### XC-02 · Obtain a token with workflow scope, or route the three CI patches to a session that has one

`hygiene` · **blocked-on-workflow-scope**

**Why it matters.** Three CI barriers exist as reviewed patches and none of them run. Each guards a defect class that has already occurred once.

**Done when.** RR-01, CR-01 and ER-02 are applied and their checks appear on subsequent pull requests.
