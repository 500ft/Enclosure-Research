# Military Environmental Sensing Extension

This folder captures the defense-relevant extension of the outdoor sensor-box project.

The recommended framing is:

> A rugged, low-cost, validated environmental sensing node for non-regulatory smoke, particulate, heat, humidity, and base air-quality awareness at military installations and training sites.

This extension should stay dual-use and unclassified. It should not claim regulatory-grade air monitoring, fire detection, CBRN detection, or "military-grade" ruggedness until those claims are supported by specific tests.

## Files

- `research_brief.md` - source-backed research brief and positioning analysis.
- `validation_matrix.md` - measurement, ruggedness, autonomy, and operational validation criteria.

## Related Templates

- `templates/installation_deployment_plan.md` - site planning form for installation-style deployments.
- `templates/installation_deployment_log.csv` - event log for installation-style field trials.
- `templates/ruggedization_test_matrix.md` - selected environmental stress tests and pass/fail criteria.

## Recommended First Prototype

Use a two-zone architecture:

1. A sealed electronics and power compartment with cable glands, serviceable access, and internal temperature/power telemetry.
2. A ventilated, replaceable sensor shield that isolates PM and ambient sensors from electronics heat while blocking direct sun, rain, insects, and debris.

The first validation run should compare the current lab box against this ruggedized architecture during a 14- to 30-day co-location deployment.
