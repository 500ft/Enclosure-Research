"""Synthetic accounting tests, not validation of field reliability or accuracy."""

import math
import tempfile
import unittest
from datetime import datetime, timedelta, timezone
from pathlib import Path

from analysis.compute_metrics import compute_metrics, read_rows


START = datetime(2026, 4, 20)
END = START + timedelta(minutes=20)


def scheduled(rows, **kwargs):
    return compute_metrics(
        rows,
        kwargs.pop("expected_interval_minutes", 5),
        window_start=kwargs.pop("window_start", START),
        window_end=kwargs.pop("window_end", END),
        **kwargs,
    )


class MetricsTests(unittest.TestCase):
    def test_cadence_without_intended_window_is_rejected(self):
        rows = [(START, 20, 19), (START, 20, 19), (START + timedelta(minutes=5), 21, 20)]
        with self.assertRaisesRegex(ValueError, "window"):
            compute_metrics(rows, 5)

    def test_duplicate_slots_do_not_inflate_completeness_or_hide_edges(self):
        t = START + timedelta(minutes=5)
        result = scheduled([(t, 20, 19), (t, 20, 19), (t + timedelta(minutes=5), 21, 20)])
        self.assertEqual(result.expected_count, 4)
        self.assertEqual(result.received_slot_count, 2)
        self.assertEqual(result.paired_slot_count, 2)
        self.assertEqual(result.duplicate_slot_records, 1)
        self.assertEqual(result.completeness, 0.5)
        self.assertEqual(result.count, 3)  # error metrics remain per observation
        self.assertEqual(result.bias, 1)

    def test_delivery_sensor_and_pairing_have_different_numerators(self):
        rows = [(START, 20, 19), (START + timedelta(minutes=5), 21, None),
                (START + timedelta(minutes=10), math.inf, 21),
                (START + timedelta(minutes=15), None, None)]
        result = scheduled(rows)
        self.assertEqual(result.delivery_completeness, 1)
        self.assertEqual(result.sensor_completeness, 0.5)
        self.assertEqual(result.paired_completeness, 0.25)
        self.assertEqual(result.count, 1)

    def test_off_grid_is_reported_not_rounded_implicitly(self):
        result = scheduled([(START + timedelta(seconds=1), 20, 19)])
        self.assertEqual(result.off_grid_records, 1)
        self.assertEqual(result.delivery_completeness, 0)
        self.assertEqual(result.count, 1)  # finite in-window pair, not a scheduled hit

    def test_explicit_tolerance_and_slot_collision(self):
        result = scheduled([(START, 20, 19), (START + timedelta(seconds=1), 21, 20)],
                           slot_tolerance_seconds=1)
        self.assertEqual(result.delivery_completeness, 0.25)
        self.assertEqual(result.duplicate_slot_records, 1)

    def test_exclusive_end_and_outside_rows(self):
        result = scheduled([(START - timedelta(seconds=1), 100, 0),
                            (END, 100, 0), (START, 20, 19)])
        self.assertEqual(result.outside_window_records, 2)
        self.assertEqual(result.bias, 1)
        self.assertEqual(result.delivery_completeness, 0.25)

    def test_partial_final_interval_has_scheduled_start(self):
        result = scheduled([], window_end=START + timedelta(minutes=16))
        self.assertEqual(result.expected_count, 4)
        self.assertEqual(result.completeness, 0)
        self.assertIsNone(result.bias)

    def test_empty_unscheduled_is_unavailable_not_zero_accuracy(self):
        result = compute_metrics([], None)
        self.assertEqual(result.count, 0)
        self.assertIsNone(result.completeness)
        self.assertIsNone(result.rmse)

    def test_invalid_intervals(self):
        for interval in (0, -1, math.nan, math.inf, 1e-20):
            with self.subTest(interval=interval), self.assertRaises(ValueError):
                scheduled([], expected_interval_minutes=interval)

    def test_invalid_windows_and_tolerances(self):
        for end in (START, START - timedelta(minutes=1)):
            with self.subTest(end=end), self.assertRaises(ValueError):
                scheduled([], window_end=end)
        for tolerance in (-1, 150, math.nan, math.inf):
            with self.subTest(tolerance=tolerance), self.assertRaises(ValueError):
                scheduled([], slot_tolerance_seconds=tolerance)

    def test_mixed_clock_conventions_rejected(self):
        with self.assertRaisesRegex(ValueError, "timezone"):
            scheduled([(START.replace(tzinfo=timezone.utc), 20, 19)])

    def test_equivalent_timezone_offsets_are_same_slot(self):
        start = START.replace(tzinfo=timezone.utc)
        local = start.astimezone(timezone(timedelta(hours=-4)))
        result = scheduled([(start, 20, 19), (local, 20, 19)], window_start=start,
                           window_end=start + timedelta(minutes=20))
        self.assertEqual(result.received_slot_count, 1)
        self.assertEqual(result.duplicate_slot_records, 1)

    def test_accuracy_definitions_and_sorting_preserved(self):
        result = compute_metrics([(START + timedelta(days=1), 13, 10), (START, 9, 10)], None)
        self.assertEqual(result.bias, 1)
        self.assertEqual(result.mae, 2)
        self.assertAlmostEqual(result.rmse, math.sqrt(5))
        self.assertEqual(result.drift_per_day, 4)

    def test_csv_retains_records_without_finite_pair(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "example.csv"
            path.write_text("timestamp,sensor,reference\n2026-04-20T00:00:00,20,19\n"
                            "2026-04-20T00:05:00,21,\n2026-04-20T00:10:00,inf,22\n")
            rows = read_rows(str(path), "sensor", "reference")
        self.assertEqual(len(rows), 3)
        self.assertIsNone(rows[1][2])
        self.assertIsNone(rows[2][1])

    def test_invalid_timestamp_has_actionable_error(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "bad.csv"
            path.write_text("timestamp,sensor,reference\nwrong,20,19\n")
            with self.assertRaisesRegex(ValueError, "row 2"):
                read_rows(str(path), "sensor", "reference")


if __name__ == "__main__":
    unittest.main()
