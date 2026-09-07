# Bounded additional developer evaluation — frozen 2026-09-06 before outputs

Candidate source hashes: [candidate.json](candidate.json). This is a synthetic
metamorphic check selected by the implementing agent, not an independent review,
field trial, unseen scientific dataset, or evidence of general accuracy.
The criteria are written before executing the additional cases. The code tests
have already informed development; these cases reuse the same requirements with
different counts/cadences/translation and do not acquire scientific independence
by being hashed.

Selection: exhaustive cross-product of expected slot counts N={1,7,23} and
cadences Δ={2,7.5} minutes. First sample is 2026-09-01T12:34:00Z, exclusive end
is start+NΔ. Every even-numbered slot has a finite pair with error 1. Add four
duplicates of slot zero, one off-grid observation at start+Δ/3, and one row
exactly at the exclusive end. Repeat the same case translated by 11 days, then
reverse row order. No fixture is selected using candidate predictions.

Prewritten expected judgments for each of six base cases and six translations:

- expected_count=N, received/paired unique slots=ceil(N/2);
- paired_completeness=ceil(N/2)/N, duplicate_slot_records=4;
- off_grid_records=1, outside_window_records=1;
- finite in-window pair count=ceil(N/2)+5 and bias/MAE/RMSE=1;
- reversing input order and calendar translation do not change these values.

Separately verify candidate hashes before evaluation; a mismatch is a stale
candidate, not a failed scientific result. Save command and outcomes in
evaluation.md. If a case motivates a fix, record the disagreement, mark it as
development material, and make a new source snapshot before further evaluation.
No field claim, human approval, or deployment rate is inferred from success.
