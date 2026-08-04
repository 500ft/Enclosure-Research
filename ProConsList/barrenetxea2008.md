# barrenetxea2008: The Hitchhiker's Guide to Successful Wireless Sensor Network Deployments

**Source:** https://doi.org/10.1145/1460412.1460418
**Evidence boundary:** Experience/methodology paper (SenSys '08, pp. 43–56) distilling deployment practice from the SensorScope project's multiple environmental-monitoring campaigns. Citation, venue, and scope verified from publisher/index metadata (2026-07); full text not re-read for this entry — quote specific guidance only after pulling the paper.

## Sensors

SensorScope solar-powered outdoor environmental stations (meteorological sensing suite). Exact sensor models are in the project's papers; not re-verified here.

### Pros

- Guidance is drawn from repeated real campaigns in varied environments, not a single lucky deployment.
- Directly addresses the gap this project just observed in its own logs: system behavior on the bench does not predict field behavior, and vice versa.

### Cons

- 2008-era mesh-radio context; networking-specific lessons transfer only partially to a single cellular node.
- Not an air-quality or calibration study.

## Physical Box, Materials, and Geometry

Mast-mounted solar-powered stations; packaging detail is in the project's papers and is not re-verified here.

### Pros

- The stated theme — a functioning network does not guarantee meaningful data — motivates protocol discipline: documented timelines, on-site validation, monitoring of the monitoring system.

### Cons

- No enclosure-thermal or shield-geometry evidence; do not cite for enclosure design.

## Selection Lessons for This Project

- Supports adding a written deployment protocol (placement/retrieval dates, power configuration, maintenance log) — the absence of which is exactly what forced this project's indoor/outdoor timeline to be inferred from temperature signatures (Section 5.0).
- Supports pre-deployment bench checks that replicate field power conditions, given the commissioning-phase brownouts observed at healthy battery voltage.
- Cannot justify sensor, material, or geometry selections.
