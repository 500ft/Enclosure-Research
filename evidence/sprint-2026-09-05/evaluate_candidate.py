"""Execute the prewritten developer procedure; prints evidence, never field data."""

import hashlib
import json
import math
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
from analysis.compute_metrics import compute_metrics


def main():
    manifest = json.loads(Path(__file__).with_name("candidate.json").read_text())
    for relative, expected in manifest["sha256"].items():
        actual = hashlib.sha256((ROOT / relative).read_bytes()).hexdigest()
        if actual != expected:
            raise SystemExit(f"STALE CANDIDATE: {relative}; expected {expected}, got {actual}")
    print("Candidate hashes: PASS (4/4)")
    cases = 0
    for slots in (1, 7, 23):
        for minutes in (2, 7.5):
            for translate in (0, 11):
                start = datetime(2026, 9, 1, 12, 34, tzinfo=timezone.utc) + timedelta(days=translate)
                period = timedelta(minutes=minutes)
                end = start + slots * period
                rows = [(start + k * period, 20, 19) for k in range(0, slots, 2)]
                rows += [(start, 20, 19)] * 4
                rows += [(start + period / 3, 20, 19), (end, 500, 0)]
                result = compute_metrics(list(reversed(rows)), minutes, window_start=start, window_end=end)
                expected_unique = math.ceil(slots / 2)
                expected = {"expected_count": slots, "received_slot_count": expected_unique,
                            "paired_slot_count": expected_unique, "duplicate_slot_records": 4,
                            "off_grid_records": 1, "outside_window_records": 1,
                            "count": expected_unique + 5, "bias": 1, "mae": 1, "rmse": 1,
                            "paired_completeness": expected_unique / slots}
                for key, value in expected.items():
                    if getattr(result, key) != value:
                        raise AssertionError((slots, minutes, translate, key, value, getattr(result, key)))
                cases += 1
                print(f"PASS N={slots} cadence_min={minutes} translation_days={translate} unique={expected_unique}/{slots}")
    print(f"Developer metamorphic cases: {cases}/12 PASS; no field/independent-validation claim")


if __name__ == "__main__":
    main()
