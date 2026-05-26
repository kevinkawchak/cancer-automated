# Humanoid Sensor Stack Specification

The H2-Surgical 1.0 sensor record extends the 8-arm baseline (80 channels per arm)
with the channels a 71-DOF body adds: per-finger joints, per-fingertip force, and
whole-body balance. The record schema is published in three bit-identical formats:
`schemas/h2_sensor_record.{schema.json,proto,avsc}`.

## Channel groups (per hand and whole body)

| Group | Count | Rate | Notes |
|-------|-------|------|-------|
| Arm joint position q1..q7 | 7 | 10 kHz | radians |
| Arm joint velocity qd1..qd7 | 7 | 10 kHz | rad/s |
| Arm joint torque tau1..tau7 | 7 | 10 kHz | N.m |
| Finger joint angles | 20 | 10 kHz | 5 fingers x 4 joints |
| Per-fingertip force | 5 | 100 kHz | 0.01 N resolution |
| Hand reference position xyz | 3 | 10 kHz | mm, patient frame |
| Hand reference orientation quaternion | 4 | 10 kHz | qx qy qz qw |
| Hand reference force | 3 | 100 kHz | N |
| Fingertip positions | 15 | 10 kHz | 5 x xyz, mm |
| Vessel surface proximity | 1 | 100 kHz | mm, confocal laser |
| NIR ICG intensity | 4 | 10 kHz | 800 nm |
| Pancreatic duct manometry | 1 | 10 kHz | mmHg, Phase 5 |
| Anastomosis ring tension | 1 | 10 kHz | N, Phases 5 6 7 |
| Bile spectrophotometry | 4 | 10 kHz | 410 470 532 600 nm |
| Ultrasound B-mode | 8 | 10 kHz | dB |
| Centre of mass | 3 | 10 kHz | m, world frame (balance) |
| Zero-moment point | 2 | 10 kHz | m, floor plane (balance) |
| Support polygon margin | 1 | 10 kHz | mm (balance) |
| Ankle torque (L, R) | 2 | 10 kHz | N.m (balance) |
| Hip torque (L, R) | 2 | 10 kHz | N.m (balance) |
| Tip force scalar | 1 | 100 kHz | N |
| Bimanual cumulative force | 1 | 100 kHz | N |
| State enums (grasp, balance, estop, collision) | 4 | 10 kHz | categorical |
| Heartbeat seq + watchdog | 2 | 10 kHz | coordination |

## Balance channels are the humanoid addition

The 8-arm baseline has no centre-of-mass, zero-moment-point, support-polygon, or
ankle and hip torque channels because a fixed base cannot fall. These channels
feed VVUQ 03 (whole-body-balance) and are sampled every command tick.

## Publication sample

`src/sensors/ingest_h2.py` writes a deterministic publication sample to
`data/sample_h2_sensor.csv` and `data/sample_h2_sensor.jsonl`. The sample is a
flattened, scalar-column slice across both hands suitable for human review and
figures; the full per-tick record is reserved for the Zenodo L0 deposition.
