# Co-location owner session — prepared, not scheduled or approved

Prepared 2026-09-11. No message sent, acquisition authorized, equipment reserved,
or approval inferred. This supplements the historical
[deployment provenance request](DEPLOYMENT_PROVENANCE_REQUEST.md), which remains
open; it does not fill missing register entries with guesses.

Bring the [draft protocol](COLOCATION_PROTOCOL.md), actual device/reference
inventory and calibration records, a proposed site/access permission record,
and the intended acquisition window. Record owner, decision date and supporting
source for each answer; leave missing answers explicitly unknown.

| Decision | Required evidence | Current disposition |
| --- | --- | --- |
| PI and site/data permission | Named authorized reviewer and written scope/conditions | Blocked; none supplied |
| Actual equipment and controls | Box/reference IDs, finish/geometry, sensor placement, firmware and heat load | Blocked; no inventory verified |
| Reference quality | Current calibration, aspiration/shield characterization, uncertainty budget and pre/post check method | Blocked; no calibration verified |
| Prospective protocol freeze | Approved version/commit, positions and pairing, intended UTC start/end, cadence, interventions and uncertainty method recorded before acquisition | Draft only; not frozen |
| Acquisition and custody | Authorized operator, raw export location, raw-byte SHA-256, omissions and separate sky/intervention records | Blocked; no pilot acquired |
| Physical interpretation | Authenticated provenance review, as-built prediction and propagated uncertainty, application tolerance registered before comparison | Blocked; no model-agreement band exists |

Suggested session sequence: review unknowns and permissions; inspect actual
equipment/calibration; accept or amend the draft prospectively; assign an
authorized acquisition operator only after those gates close. Record approval,
rejection or deferred decision explicitly, with identity/date/source. Session
attendance or checklist completion alone is not experimental approval.

After authorized acquisition, run from the repository root:

```sh
python -m analysis.intake_gate CSV_PATH --metadata METADATA_JSON
```

Paths are placeholders, not claims that an export exists. Keep private raw data
out of git and preserve original bytes. Retain the JSON report, exit code, CSV
and metadata hashes in the authorized evidence store. Exit 2 requires input or
coverage investigation without deleting unfavorable observations; exit 3 is
synthetic-only. Exit 0 admits a physical-labeled pilot for human provenance review
and **does not validate the model**. Metadata labels can be falsified; a hash only
binds bytes. No software test authenticates measurements or closes EN-R03.

Do not derive acceptance bands from the simulated −4 °C or +8–23 °C scenarios.
If hardware or weather cannot meet the proposed pilot requirements, document a
prospective amendment instead of relaxing thresholds after observing results.
