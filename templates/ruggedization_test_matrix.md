# Ruggedization Test Matrix

This matrix is a practical pre-qualification screen for a low-cost installation sensor node. It is inspired by defense environmental test thinking, but it is not a substitute for formal MIL-STD-810 qualification.

## Test Article

- Box ID:
- Hardware revision:
- Firmware revision:
- Enclosure material:
- Sensor shield material:
- Mounting configuration:
- Test date:
- Tester:

## Tests

| Test | Setup | Powered? | Duration / cycles | Measurements | Pass / fail criteria | Result |
|---|---|---|---|---|---|---|
| Solar heat soak | Full sun or lamp exposure; log ambient, internal, sensor readings | yes | TODO | internal temp rise, sensor bias, data continuity | no thermal shutdown; bias within threshold | TODO |
| Rain / splash | Simulated rain from above and windward side | yes and no | TODO | water ingress, connector status, data continuity | no water in electronics volume | TODO |
| Humidity / condensation | High-RH sealed-bin or chamber exposure followed by cool/warm cycle | yes | TODO | RH recovery, PCB inspection, logs | no condensation damage; data recovers | TODO |
| Dust / debris | Dust exposure around inlet and vents | yes | TODO | inlet blockage, PM fan status, data continuity | inlet serviceable; no fan fault | TODO |
| Handling / vibration | Transport in case, tripod/mast movement, connector tug check | yes | TODO | enclosure cracks, connector looseness, log gaps | no structural failure or data interruption | TODO |
| Power brownout | Force battery depletion or power cycling | yes | TODO | reboot behavior, timestamp continuity, file integrity | clean restart and no corrupted log | TODO |
| Maintenance access | Timed sensor cartridge or SD card replacement | no | 3 repeats | service time, tool count, damaged parts | service under threshold with no damage | TODO |

## Inspection Checklist

- Electronics compartment dry:
- Cable glands intact:
- Sensor shield intact:
- Insect screen clear:
- PM inlet clear:
- Fan audible/telemetry normal:
- Mounting hardware tight:
- SD/log file readable:
- Battery voltage normal:
- Calibration metadata present:

## Summary

- Passed tests:
- Failed tests:
- Required design changes:
- Retest required:
