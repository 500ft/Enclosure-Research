# Owner/lab request — prepared, not sent

Prepared 2026-09-05. No raw exports have been accessed or published in this sprint.
Please provide source-backed answers or explicitly mark unknown. Inferred values
are useful for exploration but do not close the confirmed-denominator gate.

1. Device identity for each log, firmware version, configured sample period, and
   whether upload cadence differs from sensor sampling cadence.
2. Intended deployment start and exclusive end, timezone/UTC offset, clock sync
   method, timestamp meaning (sample/boot/upload), clock corrections, and outages
   or planned excluded intervals. Does the first sample occur exactly at start?
3. Confirmed indoor/outdoor dates and maintenance/intervention history. The
   existing Apr 20–May 11 classification was inferred from the signal itself.
4. Meaning of each reset/upload field, duplicate/retry semantics, and whether
   repeated BROWNOUT rows represent repeated resets or repeated reported state.
5. Permission-cleared access route for original exports and their checksums.
   Do not email/commit sensitive raw records merely to complete this checklist.
6. Physical baseline geometry, material/finish, sensor position, coupled
   electronics dissipation, weathering, and photographs with sharing permission.
7. Reference instrument identity, calibration/uncertainty, availability, mounting
   constraints, and lab authorization for a matched-finish comparison.

Once these exist, retain a metadata record with source/owner/date per answer,
store derived outputs in a new versioned directory, and compare scheduled
availability with the historical observed-span estimate. Do not overwrite the
published 91.4% silently. The software fixes can proceed while this is blocked.

Suggested comparison: dark baseline, the same baseline with a measured white
finish, and matched-finish shield. Keep sensor identity, exposure, and electronics
load matched or explicitly account for changes. Register pairing/randomization,
reference uncertainty, solar/wind strata, exclusions, and acceptance criteria
before inspecting comparative measurements. No exact physical agreement target
is specified until instrument resolution and the actual task tolerance are known.
