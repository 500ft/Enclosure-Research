#!/usr/bin/env python3
"""Compute first-pass accuracy and data completeness metrics for deployment data.

Input CSV requirements:
  - ISO-8601 timestamp column, using one consistent clock convention
  - one sensor column, e.g. sensor_temperature
  - one reference column, e.g. reference_temperature

Example:
  python analysis/compute_metrics.py data/matched.csv \
    --sensor sensor_temperature \
    --reference reference_temperature \
    --expected-interval-minutes 5 \
    --window-start 2026-04-20T00:00:00Z --window-end 2026-04-21T00:00:00Z

Completeness requires an intended schedule; it is never inferred from observed
first/last rows. Window end is exclusive. See docs/RELIABILITY_METRICS.md.
"""

from __future__ import annotations

import argparse
import csv
import math
from dataclasses import dataclass
from datetime import datetime, timezone


@dataclass
class Metrics:
    count: int
    expected_count: int | None
    completeness: float | None
    bias: float | None
    mae: float | None
    rmse: float | None
    correlation: float | None
    drift_per_day: float | None
    records: int
    received_slot_count: int | None
    sensor_slot_count: int | None
    paired_slot_count: int | None
    delivery_completeness: float | None
    sensor_completeness: float | None
    paired_completeness: float | None
    duplicate_slot_records: int | None
    off_grid_records: int | None
    outside_window_records: int
    completeness_basis: str


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


def normalize_clock(timestamp: datetime) -> datetime:
    if not isinstance(timestamp, datetime) or timestamp != timestamp:
        raise ValueError("timestamp must be a valid datetime")
    return timestamp.astimezone(timezone.utc) if timestamp.utcoffset() is not None else timestamp


def scheduled_slots(
    timestamps: list[datetime], window_start: datetime, window_end: datetime,
    interval_minutes: float, tolerance_seconds: float = 0,
) -> tuple[int, list[int | None], list[bool]]:
    """Return expected count, assigned slot IDs, and in-window flags.

    Grid: start + k * interval, strictly before exclusive end. No bin averaging
    or inferred timestamp tolerance. Multiple records may map to one slot; the
    caller must count unique IDs. Normalize aware timestamps to UTC before
    arithmetic; mixing naive and aware clocks is rejected.
    """
    if not math.isfinite(interval_minutes) or interval_minutes <= 0:
        raise ValueError("expected interval must be finite and positive")
    interval_us_float = interval_minutes * 60_000_000
    if not math.isfinite(interval_us_float):
        raise ValueError("expected interval is too large")
    interval_us = round(interval_us_float)
    if interval_us < 1:
        raise ValueError("expected interval must resolve at least one microsecond")
    if not math.isfinite(tolerance_seconds) or not 0 <= tolerance_seconds < interval_us / 2_000_000:
        raise ValueError("slot tolerance must be finite, nonnegative, and less than half the interval")
    start, end = normalize_clock(window_start), normalize_clock(window_end)
    times = [normalize_clock(t) for t in timestamps]
    aware = start.utcoffset() is not None
    if any((t.utcoffset() is not None) != aware for t in [end, *times]):
        raise ValueError("timezone convention must agree for timestamps and window")
    if end <= start:
        raise ValueError("window end must be after window start")
    duration = end - start
    duration_us = (duration.days * 86400 + duration.seconds) * 1_000_000 + duration.microseconds
    expected = (duration_us + interval_us - 1) // interval_us
    slots, inside = [], []
    for timestamp in times:
        in_window = start <= timestamp < end
        inside.append(in_window)
        if not in_window:
            slots.append(None)
            continue
        elapsed = timestamp - start
        elapsed_us = (elapsed.days * 86400 + elapsed.seconds) * 1_000_000 + elapsed.microseconds
        quotient, remainder = divmod(elapsed_us, interval_us)
        slot = quotient + int(remainder * 2 >= interval_us)
        error_us = abs(elapsed_us - slot * interval_us)
        slots.append(slot if slot < expected and error_us <= tolerance_seconds * 1_000_000 else None)
    return expected, slots, inside


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


def read_rows(csv_path: str, sensor_col: str, reference_col: str) -> list[tuple[datetime, float | None, float | None]]:
    """Keep every timestamped delivery, including records lacking valid channels."""
    rows: list[tuple[datetime, float | None, float | None]] = []
    with open(csv_path, newline="") as handle:
        reader = csv.DictReader(handle)
        required = {"timestamp", sensor_col, reference_col}
        missing = required.difference(reader.fieldnames or [])
        if missing:
            raise ValueError(f"Missing required columns: {', '.join(sorted(missing))}")
        for number, row in enumerate(reader, 2):
            sensor = parse_float(row.get(sensor_col, ""))
            reference = parse_float(row.get(reference_col, ""))
            try:
                timestamp = parse_timestamp(row["timestamp"])
            except (AttributeError, TypeError, ValueError) as exc:
                raise ValueError(f"Invalid timestamp at CSV row {number}: {row.get('timestamp')!r}") from exc
            rows.append((timestamp, sensor, reference))
    return rows


def compute_metrics(
    rows: list[tuple[datetime, float | None, float | None]],
    expected_interval_minutes: float | None,
    *, window_start: datetime | None = None, window_end: datetime | None = None,
    slot_tolerance_seconds: float = 0,
) -> Metrics:
    """Per-observation finite-pair errors plus unique scheduled availability.

    Accuracy includes finite in-window observations, even off-grid observations;
    it is row weighted and makes no independence claim about repeated records.
    ``completeness`` is a compatibility alias for paired_completeness, not uptime.
    """
    times = [normalize_clock(row[0]) for row in rows]
    if times and any((t.utcoffset() is not None) != (times[0].utcoffset() is not None) for t in times):
        raise ValueError("timezone convention must agree for all timestamps")
    expected_count = None
    slots: list[int | None] = [None] * len(rows)
    inside = [True] * len(rows)
    if expected_interval_minutes is not None:
        if window_start is None or window_end is None:
            raise ValueError("intended window start and end are required with expected interval")
        expected_count, slots, inside = scheduled_slots(
            times, window_start, window_end, expected_interval_minutes, slot_tolerance_seconds)
    elif window_start is not None or window_end is not None or slot_tolerance_seconds != 0:
        raise ValueError("window and slot tolerance require an expected interval")

    finite_sensor = [parse_float(row[1]) is not None for row in rows]
    finite_pair = [valid and parse_float(row[2]) is not None for valid, row in zip(finite_sensor, rows)]
    pairs = sorted((t, float(row[1]), float(row[2])) for t, row, valid, in_window
                   in zip(times, rows, finite_pair, inside) if valid and in_window)
    residuals = [sensor - reference for _, sensor, reference in pairs]
    if any(not math.isfinite(r) for r in residuals):
        raise ValueError("finite input values overflow the residual calculation")
    count = len(pairs)
    bias = mean(residuals) if count else None
    mae = mean([abs(value) for value in residuals]) if count else None
    try:
        rmse = math.sqrt(mean([value**2 for value in residuals])) if count else None
        correlation = pearson_r([p[1] for p in pairs], [p[2] for p in pairs]) if count else None
        elapsed_days = [(t - pairs[0][0]).total_seconds() / 86400 for t, _, _ in pairs]
        drift_per_day = slope(elapsed_days, residuals) if count else None
    except OverflowError as exc:
        raise ValueError("input magnitude overflows error-metric calculation") from exc

    received = {slot for slot in slots if slot is not None}
    sensed = {slot for slot, valid in zip(slots, finite_sensor) if slot is not None and valid}
    paired = {slot for slot, valid in zip(slots, finite_pair) if slot is not None and valid}
    ratio = lambda occupied: len(occupied) / expected_count if expected_count is not None else None
    paired_completeness = ratio(paired)

    return Metrics(
        count=count,
        expected_count=expected_count,
        completeness=paired_completeness,
        bias=bias,
        mae=mae,
        rmse=rmse,
        correlation=correlation,
        drift_per_day=drift_per_day,
        records=sum(inside),
        received_slot_count=len(received) if expected_count is not None else None,
        sensor_slot_count=len(sensed) if expected_count is not None else None,
        paired_slot_count=len(paired) if expected_count is not None else None,
        delivery_completeness=ratio(received),
        sensor_completeness=ratio(sensed),
        paired_completeness=paired_completeness,
        duplicate_slot_records=sum(s is not None for s in slots) - len(received) if expected_count is not None else None,
        off_grid_records=sum(s is None and in_window for s, in_window in zip(slots, inside)) if expected_count is not None else None,
        outside_window_records=len(rows) - sum(inside),
        completeness_basis="unique slots in supplied intended schedule; paired alias is not uptime" if expected_count is not None else "unavailable: no intended schedule supplied",
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("csv_path")
    parser.add_argument("--sensor", required=True)
    parser.add_argument("--reference", required=True)
    parser.add_argument("--expected-interval-minutes", type=float)
    parser.add_argument("--window-start", help="Intended first sampling instant, ISO-8601")
    parser.add_argument("--window-end", help="Intended exclusive end, ISO-8601")
    parser.add_argument("--slot-tolerance-seconds", type=float, default=0,
                        help="Explicit matching tolerance, less than half cadence; default exact")
    args = parser.parse_args()

    try:
        rows = read_rows(args.csv_path, sensor_col=args.sensor, reference_col=args.reference)
        metrics = compute_metrics(rows, expected_interval_minutes=args.expected_interval_minutes,
                                  window_start=parse_timestamp(args.window_start) if args.window_start else None,
                                  window_end=parse_timestamp(args.window_end) if args.window_end else None,
                                  slot_tolerance_seconds=args.slot_tolerance_seconds)
    except (OSError, ValueError) as exc:
        parser.error(str(exc))

    for key, value in metrics.__dict__.items():
        if isinstance(value, float):
            print(f"{key}: {value:.6g}")
        else:
            print(f"{key}: {value}")


if __name__ == "__main__":
    main()
