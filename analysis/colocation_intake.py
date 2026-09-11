"""Admit a proposed 24-hour pilot for review, never validate a thermal model."""
import argparse
import csv
import hashlib
import json
import math
from pathlib import Path

from analysis.compute_metrics import parse_float, parse_timestamp, scheduled_slots

FIELDS = {"timestamp", "sensor_temperature", "reference_temperature", "solar_w_m2", "wind_m_s"}
IDENTITIES = ("sensor_id", "reference_id", "site_id", "firmware", "clock_basis",
              "calibration_reference", "uncertainty_reference", "permission_reference",
              "protocol_reference")


def evaluate(rows, metadata):
    if not isinstance(metadata, dict):
        raise ValueError("metadata must be a JSON object")
    for key in IDENTITIES:
        if not isinstance(metadata.get(key), str) or not metadata[key].strip():
            raise ValueError("missing declared provenance: " + key)
    if metadata.get("evidence_kind") not in {"synthetic", "physical"}:
        raise ValueError("evidence_kind must be synthetic or physical")
    uncertainty = metadata.get("paired_u95_c")
    if type(uncertainty) not in {int, float} or not math.isfinite(uncertainty) or uncertainty <= 0:
        raise ValueError("paired_u95_c must be finite and positive")
    for key in ("window_start", "window_end"):
        if not isinstance(metadata.get(key), str):
            raise ValueError(key + " must be an ISO timestamp string")
    start, end = (parse_timestamp(metadata[k]) for k in ("window_start", "window_end"))
    if start.utcoffset() is None or end.utcoffset() is None:
        raise ValueError("window must declare a timezone")
    if (end-start).total_seconds() != 86400:
        raise ValueError("this pilot requires an explicit 24-hour window")
    times = [parse_timestamp(r["timestamp"]) for r in rows]
    expected, slots, inside = scheduled_slots(times, start, end, 1, 0)
    if not all(inside) or any(s is None for s in slots):
        raise ValueError("records outside window or off the exact 60-second sample grid")
    if len(set(slots)) != len(slots):
        raise ValueError("duplicate sampling slot; reconcile raw logger records first")
    if slots != sorted(slots):
        raise ValueError("rows must be chronological")
    paired = illuminated = low_solar = 0
    for row in rows:
        if set(row) != FIELDS:
            raise ValueError("CSV fields differ from the intake schema")
        solar, wind = parse_float(row["solar_w_m2"]), parse_float(row["wind_m_s"])
        if solar is None or wind is None or solar < 0 or wind < 0:
            raise ValueError("weather observations must be finite and nonnegative")
        valid = all(parse_float(row[k]) is not None for k in ("sensor_temperature", "reference_temperature"))
        paired += valid
        illuminated += valid and solar >= 200
        low_solar += valid and solar <= 5
    complete = (paired / expected >= 0.90 and illuminated >= 120 and low_solar >= 120
                and uncertainty <= 0.5)
    classification = ("SYNTHETIC_ONLY" if metadata["evidence_kind"] == "synthetic"
                      else "REVIEWABLE_PILOT") if complete else "INCOMPLETE"
    return dict(classification=classification, expected_slots=expected, received_slots=len(rows),
                paired_slots=paired, paired_fraction=paired/expected,
                illuminated_paired_slots=illuminated, low_solar_paired_slots=low_solar,
                declared_paired_u95_c=uncertainty, validates_thermal_model=False,
                limitation="Declared metadata is not authenticated; low solar is not proof of clear-sky night.")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("csv_path", type=Path)
    parser.add_argument("--metadata", required=True, type=Path)
    args = parser.parse_args()
    try:
        metadata = json.loads(args.metadata.read_text())
        if not isinstance(metadata, dict):
            raise ValueError("metadata must be a JSON object")
        digest = hashlib.sha256(args.csv_path.read_bytes()).hexdigest()
        if metadata.get("csv_sha256") != digest:
            raise ValueError("csv_sha256 mismatch")
        with args.csv_path.open(newline="") as handle:
            reader = csv.DictReader(handle)
            if not reader.fieldnames or len(reader.fieldnames) != len(set(reader.fieldnames)):
                raise ValueError("missing or duplicate CSV header")
            if set(reader.fieldnames) != FIELDS:
                raise ValueError("CSV fields differ from the intake schema")
            result = evaluate(list(reader), metadata)
        result["csv_sha256"] = digest
        result["metadata_sha256"] = hashlib.sha256(args.metadata.read_bytes()).hexdigest()
    except (OSError, ValueError, KeyError, TypeError) as error:
        parser.exit(2, str(error) + "\n")
    print(json.dumps(result, indent=2, allow_nan=False))
    raise SystemExit({"REVIEWABLE_PILOT": 0, "SYNTHETIC_ONLY": 3, "INCOMPLETE": 2}[result["classification"]])


if __name__ == "__main__":
    main()
