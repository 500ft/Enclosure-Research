# Consumer CLI proof — 2026-09-06

Python 3.11.8; working directory `/private/tmp`, outside checkout. Input
[consumer.csv](consumer.csv) is authored synthetic data, not field evidence.
Source and input hashes are in [candidate.json](candidate.json).

Exact executed command:

```bash
python /Users/redhose/Developer/research-sprints/2026-09-05/Enclosure-Research/analysis/compute_metrics.py /Users/redhose/Developer/research-sprints/2026-09-05/Enclosure-Research/evidence/sprint-2026-09-05/consumer.csv --sensor sensor --reference reference --expected-interval-minutes 5 --window-start 2026-04-20T00:00:00Z --window-end 2026-04-20T00:20:00Z
```

Exit 0; observed stdout:

```text
count: 3
expected_count: 4
completeness: 0.25
bias: 1
mae: 1
rmse: 1
correlation: 1
drift_per_day: 0
records: 5
received_slot_count: 3
sensor_slot_count: 2
paired_slot_count: 1
delivery_completeness: 0.75
sensor_completeness: 0.5
paired_completeness: 0.25
duplicate_slot_records: 1
off_grid_records: 1
outside_window_records: 1
completeness_basis: unique slots in supplied intended schedule; paired alias is not uptime
```

This exercises the actual source-distributed CLI, not a package, registry, or
deployment. Automated equivalent: [CLI tests](../../analysis/tests/test_metrics_cli.py).
