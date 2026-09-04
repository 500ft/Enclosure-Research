#!/usr/bin/env python3
"""Reproducible reliability audit of the two sensor-box deployment logs.

Regenerates every number and figure cited in PI_MEMO.md from the raw CSVs.

Usage:
    python3 analyze_deployment_logs.py [--data-dir DIR] [--out-dir DIR]

Definitions (stated once, used everywhere):
  * "brownout row"  = a record whose reset_reason == 'BROWNOUT', i.e. the boot
    that produced this record was caused by the ESP32 brownout detector. The
    dedicated `brownout_stage` column is unpopulated in both logs (empty or -1
    on every row) and is NOT used.
  * "successful post" = last_post_ok == 1.
  * Sentinels treated as missing: batt_temp <= -40 (fuel-gauge thermistor
    absent), last_http_status == -1 (no HTTP attempt recorded).
  * QC-flagged env rows: hum == 0 (humidity cannot be 0 %RH outdoors in NYC;
    these cluster at deployment start and are treated as sensor-init/fault
    rows). Flagged rows are EXCLUDED from temperature/RH summaries only; they
    remain in all reliability statistics, which do not depend on env channels.
  * "operational row" = reset_reason == 'DEEPSLEEP_WAKE' AND hum > 0: the
    device completed a normal duty cycle and produced a valid environmental
    read. This is the filter for "the system working as deployed" as opposed
    to brownout-recovery records. Operational subsets are exported to
    <data-dir>/derived/ (kept beside the raw data, outside any repository,
    pending the PI data-path decision).
  * Indoor/outdoor classification is PROVISIONAL: it infers location from the
    internal T/RH signature (daily temperature swing and absolute level vs.
    season) and must be confirmed against the actual deployment history.

No claim of causality is made anywhere: brownout state, low battery, and
failed uploads co-occur; ordering among them is not identifiable from these
logs alone.
"""

import argparse
import json
import hashlib
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd

# Validated categorical palette (dataviz reference instance, light mode)
BLUE = "#2a78d6"   # Log A / successful posts
GREEN = "#008300"  # Log B
RED = "#e34948"    # status: brownout / failure
INK = "#0b0b0b"
INK2 = "#52514e"
GRID = "#e5e4e0"

LOGS = {
    "A": "data1.3_24 - Sheet1.csv",
    "B": "data2_5_29 - Sheet1.csv",
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load(path: Path) -> pd.DataFrame:
    df = pd.read_csv(path)
    df["timestamp"] = pd.to_datetime(df["timestamp"])
    df["brownout"] = df["reset_reason"] == "BROWNOUT"
    df["post_ok"] = df["last_post_ok"] == 1
    df["qc_env_bad"] = df["hum"] == 0
    df.loc[df["batt_temp"] <= -40, "batt_temp"] = pd.NA
    df["operational"] = (df["reset_reason"] == "DEEPSLEEP_WAKE") & (df["hum"] > 0)
    return df.sort_values("timestamp").reset_index(drop=True)


def med_iqr(s: pd.Series) -> str:
    q1, q2, q3 = s.quantile([0.25, 0.5, 0.75])
    return f"{q2:.3f} (IQR {q1:.3f}-{q3:.3f})"


def style_axes(ax):
    ax.spines[["top", "right"]].set_visible(False)
    ax.spines[["left", "bottom"]].set_color(GRID)
    ax.grid(axis="y", color=GRID, linewidth=0.8)
    ax.set_axisbelow(True)
    ax.tick_params(colors=INK2, labelsize=9)


def per_log_section(name: str, df: pd.DataFrame, lines: list):
    n = len(df)
    dt = df["timestamp"].diff().dt.total_seconds().div(60)
    bo, ok = df["brownout"], df["post_ok"]
    lines += [
        f"\n## Log {name}",
        "",
        f"- Records: {n}",
        f"- Span: {df['timestamp'].iloc[0]} to {df['timestamp'].iloc[-1]} "
        f"({(df['timestamp'].iloc[-1] - df['timestamp'].iloc[0]).days} days; logger-local time, timezone unconfirmed)",
        f"- Median record interval: {dt.median():.1f} min "
        f"(IQR {dt.quantile(0.25):.1f}-{dt.quantile(0.75):.1f}); intended cadence unconfirmed",
        f"- Reset reasons: "
        + ", ".join(f"{k} {v} ({100 * v / n:.1f}%)" for k, v in df["reset_reason"].value_counts().items()),
        f"- Successful posts: {ok.sum()} ({100 * ok.mean():.1f}%)",
        f"- Successful posts on brownout rows: {int((bo & ok).sum())} of {int(bo.sum())}",
        f"- Median batt_v [V]: brownout rows {med_iqr(df.loc[bo, 'batt_v'])} vs "
        f"successful rows {med_iqr(df.loc[ok, 'batt_v'])}",
        f"- Median batt_soc [%]: brownout rows {df.loc[bo, 'batt_soc'].median():.1f} vs "
        f"successful rows {df.loc[ok, 'batt_soc'].median():.1f}",
        f"- Median csq_rssi: brownout rows {df.loc[bo, 'csq_rssi'].median():.0f} vs "
        f"successful rows {df.loc[ok, 'csq_rssi'].median():.0f}",
        f"- QC-flagged env rows (hum==0): {int(df['qc_env_bad'].sum())} "
        f"({100 * df['qc_env_bad'].mean():.1f}%)",
        f"- Temp range after QC flag exclusion [degC]: "
        f"{df.loc[~df['qc_env_bad'], 'temp'].min():.1f} to {df.loc[~df['qc_env_bad'], 'temp'].max():.1f}",
        f"- batt_temp: sentinel (<= -40) on {int(df['batt_temp'].isna().sum())} of {n} rows -> channel unusable",
        f"- Brownout rows with batt_v >= 3.8 V: {int((bo & (df['batt_v'] >= 3.8)).sum())} "
        f"({100 * (bo & (df['batt_v'] >= 3.8)).sum() / max(int(bo.sum()), 1):.1f}% of brownout rows) "
        "-> brownouts are not exclusively a depleted-battery phenomenon",
    ]
    op = df["operational"]
    if op.any():
        ospan = df.loc[op, "timestamp"]
        lines += [
            f"- Operational rows (DEEPSLEEP_WAKE & hum>0): {int(op.sum())} ({100 * op.mean():.1f}%), "
            f"span {ospan.iloc[0].date()} to {ospan.iloc[-1].date()}, "
            f"post-ok rate {100 * df.loc[op, 'post_ok'].mean():.1f}%",
        ]

    gaps = df["timestamp"].diff()
    big = gaps[gaps > pd.Timedelta(hours=6)]
    if len(big):
        lines.append(f"- Recording gaps > 6 h: {len(big)}")
        for idx, g in big.items():
            lines.append(
                f"    - {df['timestamp'].iloc[idx - 1]} to {df['timestamp'].iloc[idx]} "
                f"({g.total_seconds() / 3600:.1f} h)"
            )
    else:
        lines.append("- Recording gaps > 6 h: none")


def regime_section(df: pd.DataFrame, lines: list):
    """Segment Log A into contiguous runs of high (>=50%) vs low daily brownout fraction."""
    daily = df.set_index("timestamp")["brownout"].resample("D").mean()
    state = daily.map(lambda v: "MISSING" if pd.isna(v) else ("HIGH" if v >= 0.5 else "LOW"))
    runs, start = [], state.index[0]
    for i in range(1, len(state) + 1):
        if i == len(state) or state.iloc[i] != state.iloc[i - 1]:
            runs.append((start.date(), state.index[i - 1].date(), state.iloc[i - 1]))
            if i < len(state):
                start = state.index[i]
    lines += [
        "\n## Log A regimes (daily brownout fraction, >= 50% = HIGH)",
        "",
        "| Period | Days | State |",
        "|---|---:|---|",
    ]
    for s, e, st in runs:
        lines.append(f"| {s} to {e} | {(e - s).days + 1} | {st} |")
    for s, e, st in runs:
        if st != "MISSING":
            m = (df["timestamp"].dt.date >= s) & (df["timestamp"].dt.date <= e)
            lines.append(
                f"- {s} to {e} ({st}): {int(m.sum())} records, "
                f"brownout {100 * df.loc[m, 'brownout'].mean():.1f}%, "
                f"post-ok {100 * df.loc[m, 'post_ok'].mean():.1f}%, "
                f"median batt_v {df.loc[m, 'batt_v'].median():.3f} V"
            )


def env_signature_section(dfs: dict, lines: list):
    """Provisional indoor/outdoor classification from the internal T/RH signature.

    Rationale: an outdoor box in NYC shows a large daily temperature swing and
    seasonal absolute levels; a box indoors sits near room temperature with a
    small swing regardless of season. Uses valid-env rows (hum > 0) only.
    """
    phases = [
        ("A", "Mar 26 - Apr 4 (commissioning)", "2026-03-26", "2026-04-05", "late March outdoor NYC ~2-12 degC"),
        ("A", "Apr 13 - Apr 19 (healthy, pre-placement)", "2026-04-13", "2026-04-20", "mid-April outdoor NYC ~7-18 degC"),
        ("A", "Apr 20 - May 11 (field deployment)", "2026-04-20", "2026-05-12", "Apr/May outdoor NYC ~8-22 degC"),
        ("A", "May 28 - Jun 4 (terminal)", "2026-05-28", "2026-06-05", "late May outdoor NYC ~15-27 degC"),
        ("B", "May 29 - Jun 4 (full log)", "2026-05-29", "2026-06-05", "late May outdoor NYC ~15-27 degC"),
    ]
    lines += [
        "\n## Provisional indoor/outdoor classification (needs PI confirmation)",
        "",
        "| Log / phase | Records | Brownout | Upload success | Median batt_v [V] | Median temp [degC] | Median RH [%] | Median daily temp range [degC] | Seasonal outdoor reference | Signature |",
        "|---|---:|---:|---:|---:|---:|---:|---:|---|---|",
    ]
    for log, label, lo, hi, season in phases:
        df = dfs[log]
        p = df[(df["timestamp"] >= lo) & (df["timestamp"] < hi)]
        v = p[p["hum"] > 0]
        if not len(v):
            continue
        dr = v.groupby(v["timestamp"].dt.date)["temp"].agg(lambda s: s.max() - s.min()).median()
        sig = "outdoor-like" if dr >= 7 else "indoor-like"
        lines.append(
            f"| {log}: {label} | {len(p)} | {100 * p['brownout'].mean():.1f}% | {100 * p['post_ok'].mean():.1f}% "
            f"| {p['batt_v'].median():.3f} | {v['temp'].median():.1f} | {v['hum'].median():.0f} | {dr:.1f} | {season} | {sig} |"
        )
    lines += [
        "",
        "Reading: only Apr 20 - May 11 carries an outdoor signature (daily minima",
        "drop from a pinned 21 degC to 4-12 degC on Apr 20; 10-20 degC swings).",
        "Apr 13-19 was healthy operation still indoors. The high-brownout phases",
        "and all of Log B sit near room temperature with a small swing, i.e. the",
        "heavy brownout activity looks like bench/indoor behavior, not field",
        "failure. PROVISIONAL: internal T/RH is a biased proxy (self-heating,",
        "enclosure lag); confirm against actual deployment dates (provenance",
        "sheet Q3-5).",
    ]

    # Field-deployment window: the subset that answers "was it deployed and working".
    # Computed by window_metrics() so the markdown here and the committed metrics JSON
    # are the same numbers by construction rather than by coincidence.
    m = window_metrics(dfs)
    lines += [
        "\n## Field-deployment window (Log A, Apr 20 - May 11, provisional)",
        "",
        f"- Records: {m['records']}; operational: {m['operational_records']} ({m['operational_pct']:.1f}%)",
        f"- Brownout fraction: {m['brownout_pct']:.1f}%",
        f"- Upload success: {m['upload_success_pct']:.1f}%",
        f"- Median batt_v: {m['median_batt_v']:.3f} V",
        f"- Completeness vs 6-min cadence: {m['completeness_pct']:.1f}% "
        "(cadence is the observed median, not a confirmed configuration)",
        f"- Internal temp span: {m['temp_min_degc']:.1f} to {m['temp_max_degc']:.1f} degC",
    ]


WINDOW_START, WINDOW_END = "2026-04-20", "2026-05-12"   # provisional outdoor window, Log A
OBSERVED_CADENCE_MIN = 6.0                              # observed median, not a confirmed config


def window_metrics(dfs: dict) -> dict:
    """Headline reliability aggregates for the provisional outdoor window.

    Single source of truth: env_signature_section() renders these into the markdown
    report and main() writes the same dict to the metrics JSON, so the report and the
    committed numbers cannot drift apart.
    """
    a = dfs["A"]
    aw = a[(a["timestamp"] >= WINDOW_START) & (a["timestamp"] < WINDOW_END)]
    dur_min = (aw["timestamp"].iloc[-1] - aw["timestamp"].iloc[0]).total_seconds() / 60
    expected = dur_min / OBSERVED_CADENCE_MIN
    env_ok = aw["hum"] > 0
    return {
        "window_start": WINDOW_START,
        "window_end_exclusive": WINDOW_END,
        "window_days": round(dur_min / 1440.0, 3),
        "records": int(len(aw)),
        "operational_records": int(aw["operational"].sum()),
        "operational_pct": float(100 * aw["operational"].mean()),
        "brownout_records": int(aw["brownout"].sum()),
        "brownout_pct": float(100 * aw["brownout"].mean()),
        "upload_success_pct": float(100 * aw["post_ok"].mean()),
        "median_batt_v": float(aw["batt_v"].median()),
        "completeness_pct": float(100 * len(aw) / expected),
        "completeness_basis": f"observed median cadence {OBSERVED_CADENCE_MIN:g} min; intended cadence unconfirmed",
        "temp_min_degc": float(aw.loc[env_ok, "temp"].min()),
        "temp_max_degc": float(aw.loc[env_ok, "temp"].max()),
    }


def main():
    p = argparse.ArgumentParser()
    # No default: the raw logs are not versioned and live outside any repository, so a
    # default path would only ever be correct on one machine.
    p.add_argument("--data-dir", required=True,
                   help="Directory holding the raw log exports (not versioned).")
    p.add_argument("--out-dir", default=str(Path(__file__).parent / "output"))
    p.add_argument("--metrics-json", default=None,
                   help="Where to write the machine-readable headline metrics. Defaults to "
                        "<out-dir>/deployment_metrics.json. Commit this file: it makes the "
                        "reported percentages traceable while the raw logs stay private.")
    args = p.parse_args()
    data_dir, out_dir = Path(args.data_dir), Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    dfs = {k: load(data_dir / v) for k, v in LOGS.items()}
    lines = [
        "# Deployment-log reliability audit (auto-generated)",
        "",
        f"Generated by `{Path(__file__).name}` on {pd.Timestamp.now():%Y-%m-%d %H:%M}.",
        "Definitions and QC rules are in the script docstring.",
        "",
        "## Inputs",
        "",
    ]
    for k, v in LOGS.items():
        lines.append(f"- Log {k}: `{v}` — sha256 `{sha256(data_dir / v)[:16]}…`")

    for k, df in dfs.items():
        per_log_section(k, df, lines)
    regime_section(dfs["A"], lines)
    env_signature_section(dfs, lines)

    # Export operational subsets beside the raw data (NOT into any repository)
    derived = data_dir / "derived"
    derived.mkdir(exist_ok=True)
    helper_cols = ["brownout", "post_ok", "qc_env_bad", "operational"]
    for k, df in dfs.items():
        out = derived / f"log{k}_operational.csv"
        df[df["operational"]].drop(columns=helper_cols).to_csv(out, index=False)
        lines.append(f"\nOperational subset of Log {k} exported to `{out}` ({int(df['operational'].sum())} rows).")
    dep = dfs["A"]
    depm = dep["operational"] & (dep["timestamp"] >= "2026-04-20") & (dep["timestamp"] < "2026-05-12")
    dep_out = derived / "logA_deployed.csv"
    dep[depm].drop(columns=helper_cols).to_csv(dep_out, index=False)
    lines.append(
        f"\nField-deployment subset (operational AND inside the provisional outdoor window) "
        f"exported to `{dep_out}` ({int(depm.sum())} rows)."
    )

    # Overlap-window comparison: Log B's full span, restricted view of Log A
    a, b = dfs["A"], dfs["B"]
    t0, t1 = b["timestamp"].iloc[0], b["timestamp"].iloc[-1]
    aw = a[(a["timestamp"] >= t0) & (a["timestamp"] <= t1)]
    lines += [
        "\n## Overlap window (Log B span applied to both logs)",
        "",
        f"Window: {t0} to {t1}.",
        "",
        "| Metric | Log A in window | Log B |",
        "|---|---:|---:|",
        f"| Records | {len(aw)} | {len(b)} |",
        f"| Brownout fraction | {100 * aw['brownout'].mean():.1f}% | {100 * b['brownout'].mean():.1f}% |",
        f"| Successful-post fraction | {100 * aw['post_ok'].mean():.1f}% | {100 * b['post_ok'].mean():.1f}% |",
        f"| Median batt_v (all rows) [V] | {aw['batt_v'].median():.3f} | {b['batt_v'].median():.3f} |",
        f"| Median record interval [min] | {aw['timestamp'].diff().dt.total_seconds().div(60).median():.1f} "
        f"| {b['timestamp'].diff().dt.total_seconds().div(60).median():.1f} |",
        "",
        "Interpretation is blocked on provenance: whether A and B are two units,",
        "one unit re-exported, or one unit reconfigured is unknown (see",
        "provenance_questions.md). No comparison claim is made until resolved.",
    ]

    # Fig 1: daily brownout fraction, both logs
    fig, ax = plt.subplots(figsize=(7.5, 3.2), dpi=200)
    for key, df, color in (("Log A", a, BLUE), ("Log B", b, GREEN)):
        daily = df.set_index("timestamp")["brownout"].resample("D").mean().mul(100)
        ax.plot(daily.index, daily.values, color=color, linewidth=2, label=key)
        ax.annotate(key, xy=(daily.index[-1], daily.values[-1]), xytext=(6, 0),
                    textcoords="offset points", color=color, fontsize=9, va="center")
    style_axes(ax)
    ax.set_ylabel("Daily brownout-reset fraction [%]", color=INK2, fontsize=9)
    ax.set_title("Daily fraction of records following a brownout reset",
                 color=INK, fontsize=11, loc="left")
    fig.tight_layout()
    fig.savefig(out_dir / "fig1_daily_brownout_fraction.png")

    # Fig 2: brownout fraction by hour of day
    fig, ax = plt.subplots(figsize=(7.5, 3.2), dpi=200)
    for key, df, color in (("Log A", a, BLUE), ("Log B", b, GREEN)):
        hourly = df.groupby(df["timestamp"].dt.hour)["brownout"].mean().mul(100)
        ax.plot(hourly.index, hourly.values, color=color, linewidth=2, marker="o",
                markersize=4, label=key)
    style_axes(ax)
    ax.set_xticks(range(0, 24, 3))
    ax.set_xlabel("Hour of day (logger-local, timezone unconfirmed)", color=INK2, fontsize=9)
    ax.set_ylabel("Brownout-reset fraction [%]", color=INK2, fontsize=9)
    ax.set_title("Brownout-reset fraction by hour of day (dominated by indoor/bench phases)",
                 color=INK, fontsize=11, loc="left")
    ax.legend(frameon=False, fontsize=9, labelcolor=INK2)
    fig.tight_layout()
    fig.savefig(out_dir / "fig2_hourly_brownout_fraction.png")

    # Fig 3: battery voltage distribution by row outcome (Log A)
    fig, ax = plt.subplots(figsize=(7.5, 3.2), dpi=200)
    groups = [
        ("Successful post", a.loc[a["post_ok"], "batt_v"], BLUE),
        ("Brownout reset", a.loc[a["brownout"], "batt_v"], RED),
    ]
    for i, (label, s, color) in enumerate(groups):
        ax.hist(s, bins=60, range=(3.2, 4.3), density=True, alpha=0.55,
                color=color, edgecolor="none")
        ax.axvline(s.median(), color=color, linewidth=1.5, linestyle="--")
        ax.annotate(f"{label}\nmedian {s.median():.3f} V", xy=(s.median(), ax.get_ylim()[1]),
                    xytext=(5, -10 - 28 * i), textcoords="offset points",
                    color=color, fontsize=9)
    style_axes(ax)
    ax.set_xlabel("Battery voltage [V]", color=INK2, fontsize=9)
    ax.set_ylabel("Density", color=INK2, fontsize=9)
    ax.set_title("Log A: battery voltage on successful-post vs brownout-reset rows",
                 color=INK, fontsize=11, loc="left")
    fig.tight_layout()
    fig.savefig(out_dir / "fig3_battv_by_outcome.png")

    # Fig 4: internal temperature record — the outdoor deployment window is
    # visible as the segment with large diurnal oscillation
    fig, ax = plt.subplots(figsize=(7.5, 3.2), dpi=200)
    for key, df, color in (("Log A", a, BLUE), ("Log B", b, GREEN)):
        v = df[df["hum"] > 0]
        ax.plot(v["timestamp"], v["temp"], color=color, linewidth=0.8, label=key)
    ax.axvspan(pd.Timestamp("2026-04-20"), pd.Timestamp("2026-05-12"),
               color=BLUE, alpha=0.08, lw=0)
    ax.annotate("outdoor-signature window\n(Log A, Apr 20 – May 11)",
                xy=(pd.Timestamp("2026-05-01"), 4), color=INK2, fontsize=8.5, ha="center")
    style_axes(ax)
    ax.set_ylabel("Internal temperature [°C]", color=INK2, fontsize=9)
    ax.set_title("Internal temperature: diurnal swing marks the outdoor deployment window",
                 color=INK, fontsize=11, loc="left")
    ax.legend(frameon=False, fontsize=9, labelcolor=INK2, loc="upper left")
    fig.tight_layout()
    fig.savefig(out_dir / "fig4_temp_deployment_window.png")

    (out_dir / "results.md").write_text("\n".join(lines) + "\n")

    # Machine-readable headline metrics, anchored to the sha256 of the exact inputs.
    # This is the artifact of record for every percentage quoted in docs/results.md and
    # the manuscript: the raw logs stay unversioned, but the numbers become checkable
    # and it is verifiable which files produced them.
    metrics_path = Path(args.metrics_json) if args.metrics_json else out_dir / "deployment_metrics.json"
    metrics = {
        "generated_by": Path(__file__).name,
        "evidence_type": "external field-log analysis",
        "status": "provisional - deployment history and raw exports are maintained outside "
                  "this repository; dates and cadence are unconfirmed",
        "inputs": {k: {"filename": v, "sha256": sha256(data_dir / v)} for k, v in LOGS.items()},
        "field_deployment_window": window_metrics(dfs),
        "all_logs": {
            k: {
                "records": int(len(df)),
                "brownout_records": int(df["brownout"].sum()),
                "brownout_pct": float(100 * df["brownout"].mean()),
                "upload_success_pct": float(100 * df["post_ok"].mean()),
                "operational_records": int(df["operational"].sum()),
            }
            for k, df in dfs.items()
        },
    }
    metrics_path.parent.mkdir(parents=True, exist_ok=True)
    metrics_path.write_text(json.dumps(metrics, indent=1) + "\n")
    print(f"Wrote {out_dir}/results.md, {metrics_path}, and 4 figures.")


if __name__ == "__main__":
    main()
