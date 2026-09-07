"""Synthetic integration checks; the private field exports are not fixtures."""

import unittest

import pandas as pd

from analysis.analyze_deployment_logs import window_metrics


def frame(timestamps, hum=None):
    count = len(timestamps)
    return pd.DataFrame({
        "timestamp": pd.to_datetime(timestamps), "hum": hum if hum is not None else [50] * count,
        "temp": [20] * count, "operational": [True] * count,
        "brownout": [False] * count, "post_ok": [True] * count, "batt_v": [3.9] * count,
    })


class DeploymentMetricTests(unittest.TestCase):
    def test_unconfirmed_configuration_cannot_emit_completeness(self):
        result = window_metrics({"A": frame(["2026-04-20T00:00", "2026-04-20T00:06"])})
        self.assertIsNone(result["completeness_pct"])
        self.assertIn("unavailable", result["completeness_basis"])

    def test_explicit_schedule_counts_edges_and_duplicate_deliveries(self):
        rows = frame(["2026-04-20T00:06", "2026-04-20T00:06", "2026-04-20T00:12"])
        result = window_metrics({"A": rows}, window_start="2026-04-20T00:00",
                                window_end="2026-04-20T00:24", expected_interval_minutes=6)
        self.assertEqual(result["expected_slots"], 4)
        self.assertEqual(result["delivered_slots"], 2)
        self.assertEqual(result["duplicate_slot_records"], 1)
        self.assertEqual(result["completeness_pct"], 50)
        self.assertEqual(result["upload_success_pct"], 100)  # received-row outcome, not uptime

    def test_empty_window_has_no_rate_or_accuracy_fabrication(self):
        result = window_metrics({"A": frame(["2026-06-01"])})
        self.assertEqual(result["records"], 0)
        self.assertIsNone(result["upload_success_pct"])
        self.assertIsNone(result["completeness_pct"])
        self.assertIsNone(result["temp_min_degc"])

    def test_valid_environment_availability_differs_from_delivery(self):
        rows = frame(["2026-04-20T00:00", "2026-04-20T00:06"], hum=[50, 0])
        result = window_metrics({"A": rows}, window_start="2026-04-20T00:00",
                                window_end="2026-04-20T00:12", expected_interval_minutes=6)
        self.assertEqual(result["completeness_pct"], 100)
        self.assertEqual(result["valid_environment_availability_pct"], 50)
        self.assertIsNone(result["reference_paired_availability_pct"])


if __name__ == "__main__":
    unittest.main()
