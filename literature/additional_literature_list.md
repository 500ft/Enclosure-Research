# Additional Research Literature for the Paper

This is a prioritized list of additional primary research added after the initial literature review.

## Highest-Priority Reading

1. **Tarara and Hoheisel (2007), Low-cost Shielding to Minimize Radiation Errors of Temperature Sensors in the Field**  
   Directly compares low-cost plate, stacked-plate, tube, cone, and hybrid shield geometries made from the same reflective insulation. It provides unusually clear geometry-selection evidence: stacked plates outperformed tubes; open bottoms suffered reflected-radiation heating; tube shields needed more than 30% sidewall perforation.  
   https://doi.org/10.21273/HORTSCI.42.6.1372

2. **Deford et al. (2025), Development of a Low-Cost, 3D-Printed, Aspirated Air Temperature Measurement Radiation Shield**  
   Provides an open-source white-PLA aspirated geometry with a 90-degree inlet elbow, concentric air-gap walls, insect screen, and low-power fan. It directly connects accuracy improvement to an autonomy cost from fan power.  
   https://doi.org/10.1175/JTECH-D-24-0006.1

3. **Holden et al. (2013), Design and Evaluation of an Inexpensive Radiation Shield for Monitoring Surface Air Temperatures**  
   Demonstrates a roughly USD 3 folded white corrugated-plastic Gill-style shield that performed similarly to a commercial passive shield. It is a strong manufacturability and low-cost comparison.  
   https://doi.org/10.1016/j.agrformet.2013.06.011

4. **García Izquierdo et al. (2024), COAT Project: Intercomparison of Thermometer Radiation Shields in the Arctic**  
   Compares ten shield models and 41 thermometers over 14 months. It provides long-duration evidence that shield response depends strongly on solar irradiance and wind speed, while also documenting fan, logger, mounting, storm, memory, and power failures.  
   https://doi.org/10.3390/atmos15070841

5. **Lazarescu (2015), Design and Field Test of a WSN Platform Prototype for Long-Term Environmental Monitoring**  
   Highly relevant to autonomy. It shows how packaging, antenna placement, mechanical strain, solar heating, battery monitoring, firmware behavior, and failed nodes affect field reliability and maintenance.  
   https://doi.org/10.3390/s150409481

## Geometry and Material Design

6. **Liu et al. (2023), Design and Experiments of a Naturally-Ventilated Radiation Shield for Ground Temperature Measurement**  
   Uses a Pt100 with silver-coated aluminum plates, black inner surfaces, white-resin annular plates, eight vents, and a truncated-cone reflector. Useful for studying surface finish, reflected radiation, and vent geometry.  
   https://doi.org/10.3390/atmos14030523

7. **Jin et al. (2026), Design and Experimental Validation of a High-Accuracy Naturally Ventilated Radiation Shield**  
   A recent shield study combining square upper/lower shading plates, bowl-cover flow-guiding shrouds, a Pt100 in a copper spherical shell, CFD material comparisons, and outdoor validation. It evaluates plastic, wood, Fe-Ni alloy, and aluminum configurations.  
   https://doi.org/10.3390/atmos17030272

## Calibration, Drift, and Long-Term Reliability

8. **Diez et al. (2024), Long-term Evaluation of Commercial Air Quality Sensors: The QUANT Study**  
   A three-year evaluation of 43 commercial devices containing 119 gas sensors and 118 PM sensors across UK urban environments. It supports long-term accuracy, relocation, manufacturer-correction, uncertainty, and black-box-system analysis.  
   https://doi.org/10.5194/amt-17-3809-2024

9. **Winter et al. (2025), Sustained Performance of Low-Cost Air Quality Sensors in Long-Term Deployments**  
   Evaluates Alphasense electrochemical gas sensors over three years. It finds limited degradation with frequently updated calibration, while mechanical and electrical failures often limit service life first.  
   https://doi.org/10.1021/acssensors.5c00566

## Complete Deployed Sensor-Box Systems

10. **Daepp et al. (2022), Eclipse: An End-to-End Platform for Low-Cost, Hyperlocal Environmental Sensing in Cities**  
    Describes 115 solar-powered, cellular-connected urban sensor boxes measuring PM2.5, temperature, RH, pressure, and optional gases. More than 90% of expected sensor-hours were collected during the reported deployment.  
    https://doi.org/10.1109/IPSN54338.2022.00010

## How These Sources Improve the Paper

- **Sensor accuracy:** Holden, Tarara, Deford, Liu, Jin, COAT, QUANT.
- **Calibration and drift:** QUANT and Winter.
- **Autonomy and maintenance:** Lazarescu, Eclipse, COAT, and Winter.
- **Material selection:** Tarara, Holden, Deford, Liu, and Jin.
- **Geometry selection:** Tarara, Holden, Deford, Liu, Jin, and COAT.
- **Failure-mode analysis:** Lazarescu, COAT, QUANT, and Winter.

