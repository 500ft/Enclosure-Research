"""Exercise the shipped scripts as a consumer, without the checkout on cwd."""

import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]


class CliTests(unittest.TestCase):
    def run_cli(self, name, *arguments):
        with tempfile.TemporaryDirectory() as directory:
            return subprocess.run([sys.executable, str(ROOT / "analysis" / name), *arguments],
                                  cwd=directory, capture_output=True, text=True)

    def test_consumer_fixture(self):
        result = self.run_cli("compute_metrics.py", str(ROOT / "evidence/sprint-2026-09-05/consumer.csv"),
                              "--sensor", "sensor", "--reference", "reference",
                              "--expected-interval-minutes", "5", "--window-start", "2026-04-20T00:00:00Z",
                              "--window-end", "2026-04-20T00:20:00Z")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("delivery_completeness: 0.75", result.stdout)
        self.assertIn("paired_completeness: 0.25", result.stdout)
        self.assertIn("off_grid_records: 1", result.stdout)
        self.assertIn("outside_window_records: 1", result.stdout)

    def test_unscheduled_fixture_is_explicitly_unavailable(self):
        result = self.run_cli("compute_metrics.py", str(ROOT / "evidence/sprint-2026-09-05/consumer.csv"),
                              "--sensor", "sensor", "--reference", "reference")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("completeness: None", result.stdout)
        self.assertIn("unavailable: no intended schedule", result.stdout)

    def test_cadence_only_is_actionable_cli_error(self):
        result = self.run_cli("compute_metrics.py", str(ROOT / "evidence/sprint-2026-09-05/consumer.csv"),
                              "--sensor", "sensor", "--reference", "reference", "--expected-interval-minutes", "5")
        self.assertEqual(result.returncode, 2)
        self.assertIn("intended window", result.stderr)
        self.assertNotIn("Traceback", result.stderr)

    def test_deployment_missing_data_is_access_error_not_traceback(self):
        result = self.run_cli("analyze_deployment_logs.py", "--data-dir", "/not-an-enclosure-fixture")
        self.assertEqual(result.returncode, 2)
        self.assertIn("No such file", result.stderr)
        self.assertNotIn("Traceback", result.stderr)

    def test_deployment_incomplete_schedule_fails_before_data_access(self):
        result = self.run_cli("analyze_deployment_logs.py", "--data-dir", "/not-an-enclosure-fixture",
                              "--expected-interval-minutes", "6")
        self.assertEqual(result.returncode, 2)
        self.assertIn("supply window-start", result.stderr)


if __name__ == "__main__":
    unittest.main()
