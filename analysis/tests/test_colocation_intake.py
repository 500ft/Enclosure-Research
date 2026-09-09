"""Synthetic admission cases; none are environmental validation data."""
import copy
import csv
import hashlib
import json
import subprocess
import sys
import tempfile
import unittest
from datetime import datetime, timedelta, timezone
from pathlib import Path
from analysis.colocation_intake import evaluate


def fixture():
    start = datetime(2026, 1, 1, tzinfo=timezone.utc)
    rows = [dict(timestamp=(start + timedelta(minutes=i)).isoformat(),
                 sensor_temperature="20", reference_temperature="20.2",
                 solar_w_m2="500" if 360 <= i < 1080 else "0", wind_m_s="1")
            for i in range(1440)]
    metadata = dict(window_start=start.isoformat(), window_end=(start+timedelta(days=1)).isoformat(),
        sensor_id="SYNTHETIC-SENSOR", reference_id="SYNTHETIC-REFERENCE", site_id="SYNTHETIC-SITE",
        firmware="fixture", clock_basis="UTC sample time", calibration_reference="synthetic fixture only",
        uncertainty_reference="synthetic fixture only", permission_reference="not actual permission",
        protocol_reference="synthetic development case", evidence_kind="synthetic", paired_u95_c=0.2)
    return rows, metadata


class IntakeTests(unittest.TestCase):
    def test_complete_synthetic_data_never_physical_validation(self):
        rows, metadata = fixture()
        result = evaluate(rows, metadata)
        self.assertEqual(result["classification"], "SYNTHETIC_ONLY")
        self.assertEqual(result["expected_slots"], 1440)
        self.assertFalse(result["validates_thermal_model"])

    def test_duplicate_rejected(self):
        rows, metadata = fixture()
        with self.assertRaisesRegex(ValueError, "duplicate"):
            evaluate(rows+[rows[0]], metadata)

    def test_day_only_is_inconclusive(self):
        rows, metadata = fixture()
        self.assertEqual(evaluate(rows[360:1080], metadata)["classification"], "INCOMPLETE")

    def test_bad_uncertainty_rejected(self):
        for value in (float("nan"), -0.1, True, 0):
            rows, metadata = fixture()
            metadata["paired_u95_c"] = value
            with self.assertRaises(ValueError):
                evaluate(rows, metadata)

    def test_no_calibration_identity_rejected(self):
        rows, metadata = fixture()
        metadata["calibration_reference"] = ""
        with self.assertRaises(ValueError):
            evaluate(rows, metadata)

    def test_invalid_timestamp_or_weather_rejected(self):
        for field, value in (("timestamp", "bad"), ("solar_w_m2", "nan"), ("wind_m_s", "-1")):
            rows, metadata = fixture()
            rows[0][field] = value
            with self.assertRaises(ValueError):
                evaluate(rows, metadata)

    def test_missing_sensor_values_are_missing_not_zero(self):
        rows, metadata = fixture()
        for row in rows[:200]:
            row["sensor_temperature"] = ""
        result = evaluate(rows, metadata)
        self.assertEqual(result["paired_slots"], 1240)
        self.assertEqual(result["classification"], "INCOMPLETE")

    def test_high_uncertainty_does_not_pass_quality(self):
        rows, metadata = fixture()
        metadata["paired_u95_c"] = 1.0
        self.assertEqual(evaluate(rows, metadata)["classification"], "INCOMPLETE")

    def test_cli_checks_raw_hash_and_labels_synthetic(self):
        rows, metadata = fixture()
        root = Path(__file__).resolve().parents[2]
        with tempfile.TemporaryDirectory() as directory:
            raw = Path(directory) / "raw.csv"
            meta = Path(directory) / "metadata.json"
            with raw.open("w", newline="") as handle:
                writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
                writer.writeheader()
                writer.writerows(rows)
            metadata["csv_sha256"] = hashlib.sha256(raw.read_bytes()).hexdigest()
            meta.write_text(json.dumps(metadata))
            command = [sys.executable, "-m", "analysis.colocation_intake", str(raw), "--metadata", str(meta)]
            valid = subprocess.run(command, cwd=root, capture_output=True, text=True)
            self.assertEqual(valid.returncode, 3, valid.stderr)
            self.assertEqual(json.loads(valid.stdout)["classification"], "SYNTHETIC_ONLY")
            raw.write_text(raw.read_text() + "\n")
            invalid = subprocess.run(command, cwd=root, capture_output=True, text=True)
            self.assertEqual(invalid.returncode, 2)
            self.assertIn("csv_sha256 mismatch", invalid.stderr)


if __name__ == "__main__":
    unittest.main()
