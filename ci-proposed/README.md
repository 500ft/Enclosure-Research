# Thermal table verification — installed on the review branch

The old proposal is superseded by [the active workflow source](../.github/workflows/ci.yml).
Current credentials include workflow permission; the previous restriction was
historical, not a current blocker.

CI now regenerates both day and night tables into the runner's temporary directory
and compares them to the committed references. It must not overwrite the references
before comparing, which would let changed outputs compare equal to themselves.
PR triggers include the day-1 manual stack base. Hosted success is recorded in the
review handoff after pushing; the presence of this file alone is not success.
