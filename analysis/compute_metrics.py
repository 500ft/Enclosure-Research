#!/usr/bin/env python3
"""Compute first-pass accuracy and data completeness metrics for deployment data.

Input CSV requirements:
  - timestamp column parseable by pandas
  - one sensor column, e.g. sensor_temperature
  - one reference column, e.g. reference_temperature

Example:
  python analysis/compute_metrics.py data/matched.csv \
    --sensor sensor_temperature \
    --reference reference_temperature \
    --expected-interval-minutes 5
"""

from __future__ import annotations

import argparse
import csv
import math
from dataclasses import dataclass
from datetime import datetime


@dataclass
class Metrics:
    count: int
    expected_count: int | None
    completeness: float | None
    bias: float
    mae: float
    rmse: float
    correlation: float
    drift_per_day: float


def parse_timestamp(value: str) -> datetime:
    if value.endswith("Z"):
        value = value[:-1] + "+00:00"
    return datetime.fromisoformat(value)


def parse_float(value: str) -> float | None:
    try:
        parsed = float(value)
    except (TypeError, ValueError):
        return None
    return parsed if math.isfinite(parsed) else None


def mean(values: list[float]) -> float:
    return sum(values) / len(values)


def pearson_r(x_values: list[float], y_values: list[float]) -> float:
    if len(x_values) < 2:
        return float("nan")
    x_mean = mean(x_values)
    y_mean = mean(y_values)
    numerator = sum((x - x_mean) * (y - y_mean) for x, y in zip(x_values, y_values))
    x_ss = sum((x - x_mean) ** 2 for x in x_values)
    y_ss = sum((y - y_mean) ** 2 for y in y_values)
    denominator = math.sqrt(x_ss * y_ss)
    return numerator / denominator if denominator else float("nan")


def slope(x_values: list[float], y_values: list[float]) -> float:
    if len(x_values) < 2:
        return float("nan")
    x_mean = mean(x_values)
    y_mean = mean(y_values)
    denominator = sum((x - x_mean) ** 2 for x in x_values)
    if denominator == 0:
        return float("nan")
    numerator = sum((x - x_mean) * (y - y_mean) for x, y in zip(x_values, y_values))
    return numerator / denominator


def read_rows(csv_path: str, sensor_col: str, reference_col: str) -> list[tuple[datetime, float, float]]:
    rows: list[tuple[datetime, float, float]] = []
    with open(csv_path, newline="") as handle:
        reader = csv.DictReader(handle)
        required = {"timestamp", sensor_col, reference_col}
        missing = required.difference(reader.fieldnames or [])
        if missing:
            raise ValueError(f"Missing required columns: {', '.join(sorted(missing))}")
        for row in reader:
            sensor = parse_float(row.get(sensor_col, ""))
            reference = parse_float(row.get(reference_col, ""))
            if sensor is None or reference is None:
                continue
            rows.append((parse_timestamp(row["timestamp"]), sensor, reference))
    return sorted(rows, key=lambda item: item[0])


def compute_metrics(
    rows: list[tuple[datetime, float, float]],
    expected_interval_minutes: float | None,
) -> Metrics:
    residuals = [sensor - reference for _, sensor, reference in rows]
    sensor_values = [sensor for _, sensor, _ in rows]
    reference_values = [reference for _, _, reference in rows]
    count = len(rows)
    bias = mean(residuals)
    mae = mean([abs(value) for value in residuals])
    rmse = math.sqrt(mean([value**2 for value in residuals]))
    correlation = pearson_r(sensor_values, reference_values)

    start = rows[0][0]
    elapsed_days = [(timestamp - start).total_seconds() / 86400.0 for timestamp, _, _ in rows]
    drift_per_day = slope(elapsed_days, residuals)

    expected_count = None
    completeness = None
    if expected_interval_minutes and count >= 2:
        duration_minutes = (rows[-1][0] - rows[0][0]).total_seconds() / 60.0
        expected_count = int(math.floor(duration_minutes / expected_interval_minutes)) + 1
        completeness = float(count / expected_count) if expected_count else None

    return Metrics(
        count=count,
        expected_count=expected_count,
        completeness=completeness,
        bias=bias,
        mae=mae,
        rmse=rmse,
        correlation=correlation,
        drift_per_day=drift_per_day,
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("csv_path")
    parser.add_argument("--sensor", required=True)
    parser.add_argument("--reference", required=True)
    parser.add_argument("--expected-interval-minutes", type=float)
    args = parser.parse_args()

    rows = read_rows(args.csv_path, sensor_col=args.sensor, reference_col=args.reference)
    if not rows:
        raise SystemExit("No valid rows found.")
    metrics = compute_metrics(rows, expected_interval_minutes=args.expected_interval_minutes)

    for key, value in metrics.__dict__.items():
        if isinstance(value, float):
            print(f"{key}: {value:.6g}")
        else:
            print(f"{key}: {value}")


if __name__ == "__main__":
    main()
