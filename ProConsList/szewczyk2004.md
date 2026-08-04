# szewczyk2004: An Analysis of a Large Scale Habitat Monitoring Application

**Source:** https://doi.org/10.1145/1031495.1031521
**Evidence boundary:** Experimental systems paper (SenSys '04, pp. 214–226) analyzing a real second-generation deployment of ~150 devices over 4 months (summer–autumn 2003, Great Duck Island) with emphasis on lifetime, reliability, and single- vs multi-hop network behavior. Citation, venue, scope, and deployment scale verified from publisher/index metadata (2026-07); the full text was not re-read for this entry, so specific yield percentages and packaging details must be pulled from the paper before being quoted.

## Sensors

Habitat-monitoring motes carrying temperature/humidity/light-class sensor boards. Exact sensor part numbers are in the paper and its companion papers; not re-verified here.

### Pros

- Demonstrates that a large low-power sensor fleet can produce a scientifically usable multi-month dataset.
- Treats lifetime, node mortality, and data yield as primary reported results — the reporting precedent this project's Section 5.3 follows.

### Cons

- 2003-era mote hardware; absolute power and radio figures do not transfer to modern cellular/ESP32-class nodes.
- Habitat-monitoring sensor suite, not air quality; no calibration-against-reference component.

## Physical Box, Materials, and Geometry

Weatherproofed mote packaging; the detailed packaging description lives in the project's companion papers and is not re-verified here. No shield-geometry comparison is part of the study.

### Pros

- Real outdoor exposure over a full season, so reported failures reflect genuine environmental stress.

### Cons

- Enclosure material/geometry is not analyzable from this paper alone — do not cite it for packaging design choices.

## Selection Lessons for This Project

- Supports reporting data yield, uptime, and failure analysis as first-class field results rather than footnotes (manuscript Sections 2.4, 5.3).
- Supports the expectation that deployment-phase failures differ in kind from bench behavior.
- Cannot justify any sensor selection, enclosure material, or geometry decision.
