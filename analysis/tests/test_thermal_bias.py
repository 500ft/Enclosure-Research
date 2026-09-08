"""Developer checks for the matched-finish control, not physical validation."""

import csv
from dataclasses import asdict
import io
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

import numpy as np

from analysis.thermal_bias import build_variants, run_sweep, write_bias_table


class MatchedFinishTests(unittest.TestCase):
    def setUp(self):
        self.variants = build_variants()
        self.by_id = {v.vid: v for v in self.variants}

    def sweep(self, solar):
        return run_sweep(self.variants, np.array([0.0, 0.5, 5.0]), solar,
                         30.0, 50.0, 10.0, 5.0, 4.0)

    def test_painted_control_changes_only_absorptance_and_labels(self):
        self.assertIn("V0P", self.by_id, "Primary painted control is absent from the main sweep")
        dark = asdict(self.by_id["V0"])
        painted = asdict(self.by_id["V0P"])
        for key in ("vid", "name", "note", "alpha"):
            dark.pop(key)
            painted.pop(key)
        self.assertEqual(dark, painted)
        self.assertEqual(self.by_id["V0P"].alpha, self.by_id["V1"].alpha)
        self.assertEqual(self.by_id["V0P"].eps, self.by_id["V1"].eps)

    def test_control_does_not_mutate_dark_box_and_keeps_existing_predictions(self):
        self.assertEqual(self.by_id["V0"].alpha, 0.9)
        result = self.sweep([1000.0])
        for vid, expected in (("V0", 19.4), ("V0P", 4.5), ("V1", 3.0), ("V2", 1.3)):
            self.assertIn(vid, result.dT)
            self.assertAlmostEqual(result.dT[vid][1000.0][1], expected, delta=0.1)

    def test_no_solar_means_absorptance_control_has_no_effect(self):
        result = self.sweep([0.0])
        self.assertIn("V0P", result.dT)
        np.testing.assert_array_equal(result.dT["V0"][0.0], result.dT["V0P"][0.0])
        np.testing.assert_array_equal(result.rh_err["V0"][0.0], result.rh_err["V0P"][0.0])

    def test_csv_contains_matched_control_at_every_operating_point(self):
        result = self.sweep([800.0, 1000.0])
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "bias.csv"
            write_bias_table(result, self.variants, [0.0, 0.5, 5.0], str(output))
            lines = output.read_text().splitlines()
        self.assertIn("SIMULATION", lines[0])
        rows = list(csv.DictReader(io.StringIO("\n".join(lines[1:]))))
        self.assertEqual(len(rows), 24)
        for g in ("800", "1000"):
            for wind in ("0.0", "0.5", "5.0"):
                self.assertEqual({r["variant_id"] for r in rows
                                  if r["g_w_m2"] == g and r["wind_m_s"] == wind},
                                 {"V0", "V0P", "V1", "V2"})

    def test_consumer_cli_exports_control_and_figure_outside_checkout(self):
        script = Path(__file__).resolve().parents[1] / "thermal_bias.py"
        with tempfile.TemporaryDirectory() as directory:
            result = subprocess.run(
                [sys.executable, str(script), "--table", "bias.csv", "--figure", "bias.png"],
                cwd=directory, text=True, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertIn("Painted closed-box control", result.stdout)
            self.assertIn("not an isolated shielding effect", result.stdout)
            self.assertIn(",V0P,", (Path(directory) / "bias.csv").read_text())
            self.assertGreater((Path(directory) / "bias.png").stat().st_size, 1000)


if __name__ == "__main__":
    unittest.main()
