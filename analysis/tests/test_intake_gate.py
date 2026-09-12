"""CLI contract tests using generated fixtures only, never actual pilot evidence."""
import csv
import hashlib
import io
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from analysis.tests.test_colocation_intake import fixture


class IntakeGateCliTests(unittest.TestCase):
    def run_case(self, rows, metadata, expected_exit, classification=None, raw_text=None):
        if raw_text is None:
            output = io.StringIO(newline="")
            writer = csv.DictWriter(output, fieldnames=list(fixture()[0][0]))
            writer.writeheader()
            writer.writerows(rows)
            raw_text = output.getvalue()
        with tempfile.TemporaryDirectory() as directory:
            raw, meta = Path(directory) / "raw.csv", Path(directory) / "metadata.json"
            raw.write_bytes(raw_text.encode())
            if isinstance(metadata, dict):
                metadata.setdefault("csv_sha256", hashlib.sha256(raw.read_bytes()).hexdigest())
            meta.write_text(json.dumps(metadata))
            results = []
            for module in ("analysis.colocation_intake", "analysis.intake_gate"):
                with self.subTest(module=module):
                    result = subprocess.run(
                        [sys.executable, "-m", module, str(raw), "--metadata", str(meta)],
                        cwd=Path(__file__).resolve().parents[2], capture_output=True, text=True)
                    results.append((result.returncode, result.stdout, result.stderr))
                    self.assertEqual(result.returncode, expected_exit, result.stderr)
                    self.assertNotIn("Traceback", result.stderr)
                    if classification:
                        report = json.loads(result.stdout)
                        self.assertEqual(report["classification"], classification)
                        self.assertFalse(report["validates_thermal_model"])
                        self.assertEqual(report["metadata_sha256"], hashlib.sha256(meta.read_bytes()).hexdigest())
            self.assertEqual(results[0], results[1], "compatibility CLI must delegate unchanged")

    def test_synthetic_only_and_declared_physical_review_only(self):
        rows, metadata = fixture()
        self.run_case(rows, metadata, 3, "SYNTHETIC_ONLY")
        # Deliberately relabeled fixture tests routing only, not authenticity.
        metadata["evidence_kind"] = "physical"
        self.run_case(rows, metadata, 0, "REVIEWABLE_PILOT")

    def test_declared_physical_incomplete_coverage_is_rejected(self):
        for mode in ("paired", "illuminated", "low_solar"):
            with self.subTest(mode=mode):
                rows, metadata = fixture()
                metadata["evidence_kind"] = "physical"
                if mode == "paired":
                    rows = rows[:1295]
                else:
                    for row in rows:
                        row["solar_w_m2"] = "0" if mode == "illuminated" else "500"
                self.run_case(rows, metadata, 2, "INCOMPLETE")

    def test_bad_hash_schema_metadata_and_schedule_are_rejected(self):
        for mode in ("hash", "schema", "duplicate_header", "metadata", "timestamp_type",
                     "duplicate", "off_grid", "out_of_window", "timezone", "weather", "order"):
            with self.subTest(mode=mode):
                rows, metadata = fixture()
                metadata["evidence_kind"] = "physical"
                raw_text = None
                if mode == "hash":
                    metadata["csv_sha256"] = "0" * 64
                elif mode == "schema":
                    raw_text = "timestamp,wrong\n2026-01-01T00:00:00+00:00,1\n"
                elif mode == "duplicate_header":
                    raw_text = "timestamp,timestamp\n"
                elif mode == "metadata":
                    metadata = []
                elif mode == "timestamp_type":
                    metadata["window_start"] = None
                elif mode == "duplicate":
                    rows.append(rows[0])
                elif mode == "off_grid":
                    rows[0]["timestamp"] = "2026-01-01T00:00:01+00:00"
                elif mode == "out_of_window":
                    rows[0]["timestamp"] = metadata["window_end"]
                elif mode == "timezone":
                    rows[0]["timestamp"] = "2026-01-01T00:00:00"
                elif mode == "weather":
                    rows[0]["wind_m_s"] = "nan"
                elif mode == "order":
                    rows[0], rows[1] = rows[1], rows[0]
                self.run_case(rows, metadata, 2, raw_text=raw_text)


if __name__ == "__main__":
    unittest.main()
