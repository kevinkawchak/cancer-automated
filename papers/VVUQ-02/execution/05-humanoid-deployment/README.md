# Section 05: Humanoid Deployment and the Safety Surface

This section runs the deployment reference: the 60-second 8-phase Whipple
timeline, the featured 1000-row humanoid positional sensor stream, and the three
safety-surface gates that protect a single autonomous humanoid concentrating all
surgical action into two hands. These are the immediate-catastrophe gates (06
vascular no-fly, 09 shared-OR collision, 10 fault e-stop), the most safety
critical surfaces in the whole platform.

## Contents

| File | What it records |
|------|-----------------|
| artifacts/deployment_safety_log.txt | Verbatim output of the deployment and safety-surface driver |
| artifacts/sensor_stream_analysis.txt | Structural analysis of the 1000-row positional sensor CSV |
| artifacts/eight_phase_timeline.txt | The 60-second 8-phase Whipple timeline diagram |

## 1. The 60-second 8-phase Whipple timeline

```
  phase 1: [ 0.000,  6.000) s  (len  6.0 s)  Kocher exploration
  phase 2: [ 6.000, 16.000) s  (len 10.0 s)  venous dissection
  phase 3: [16.000, 24.000) s  (len  8.0 s)  arterial dissection
  phase 4: [24.000, 32.000) s  (len  8.0 s)  transection
  phase 5: [32.000, 42.000) s  (len 10.0 s)  pancreaticojejunostomy
  phase 6: [42.000, 48.000) s  (len  6.0 s)  hepaticojejunostomy
  phase 7: [48.000, 54.000) s  (len  6.0 s)  gastrojejunostomy
  phase 8: [54.000, 60.000) s  (len  6.0 s)  closure
  phase_for_time(60.0) clamps -> 8
```

The 60-second timeline reuses the PDAC 8-phase Whipple verbatim from the 8-arm
baseline so the single-humanoid run is directly comparable. The full ASCII
diagram is in `artifacts/eight_phase_timeline.txt`.

## 2. The featured 1000-row humanoid positional sensor stream

This is the second of the two substantial generated files the prompt asks to
feature. The codegen step generated it and this execution reproduced it
byte-for-byte (Section 01) and processed it structurally. The full analysis is in
`artifacts/sensor_stream_analysis.txt`.

Structure: 1002 lines (1 header plus 1000 data rows), 27 columns, covering 500
command ticks across the left and right hands (500 x 2 = 1000 rows). The columns
are exactly the robot positional data the prompt describes, hands, 5 fingers,
arms, and more:

| Channel group | Count | Columns |
|---------------|-------|---------|
| Arm joint angles | 7 | q_arm_1 .. q_arm_7 |
| Fingertip forces (5 fingers) | 5 | finger_force_1 .. finger_force_5 |
| End-effector position | 3 | ee_pos_x, ee_pos_y, ee_pos_z |
| Per-record state and context | 12 | tick, hand_id, phase, grasp_state, vessel_proximity, ring_tension, support_polygon_margin, balance_state, tip_force_scalar, bimanual_cumulative_force, estop_state, collision_state |

### No repetitive data (verified)

```
  distinct whole rows           : 1000 of 1000
  distinct (tick, hand_id) keys : 1000 of 1000
  distinct arm-angle payloads   : 1000 of 1000
  distinct finger-force payloads: 1000 of 1000
  distinct ee-position payloads : 1000 of 1000
```

Every one of the 1000 rows is unique, and so is every per-row arm-angle,
finger-force, and end-effector-position payload. There is no duplicated row and
no constant-padded column in the positional data, which the prompt specifically
calls out. The channel ranges are physically plausible (for example fingertip
forces in 0.401 to 0.700 N, summed bimanual force 4.37 to 6.72 N, support polygon
margin 38.0 to 43.0 mm, all consistent with the ISO/TS 15066 and ISO 13482
limits). The record conforms to `schemas/h2_sensor_record.schema.json`, which
declares 33 properties.

## 3. The safety surface (the three immediate-catastrophe gates)

The verbatim driver output is in `artifacts/deployment_safety_log.txt`.

### Fault monitor and graceful degradation (VVUQ 10)

```
  clean                        -> fault=none           action=none       latency=   0.0 us  safe=True  escalate=False
  balance_loss (single)        -> fault=balance_loss   action=safe_park  latency=  50.0 us  safe=True  escalate=False
  vision_dropout (hand-back)   -> fault=vision_dropout action=hand_back  latency=1000.0 us  safe=True  escalate=True
  multi-fault (escalate)       -> fault=balance_loss   action=hand_back  latency=  50.0 us  safe=True  escalate=True
```

A clean snapshot passes, a single balance fault safe-parks within the 3 ms e-stop
budget, a vision dropout hands back to the human, and any multi-fault escalates to
hand-back by default. This is IEC 60601-1 single-fault safety, ISO 13849-1
performance level, and the IEEE 7009 fail-safe default.

### Shared-OR human collision FSM (VVUQ 09)

```
  actor at 0.80 m (far      ) -> clearance   500.00 mm; state=clear    ; vel_scale=1.0; estop=False
  actor at 0.45 m (proximity) -> clearance   150.00 mm; state=proximity; vel_scale=0.5; estop=False
  actor at 0.40 m (contact  ) -> clearance   100.00 mm; state=contact  ; vel_scale=0.1; estop=False
  actor at 0.30 m (unsafe   ) -> clearance     0.00 mm; state=unsafe   ; vel_scale=0.0; estop=True
```

Clearance to a human keep-out sphere drives a four-state FSM: full speed when
clear, half speed in proximity, crawl on contact, and e-stop when the clearance
reaches the floor. This is the ISO/TS 15066 and ISO 10218-1 speed-and-separation
property.

### Vascular no-fly hand gate (VVUQ 06)

```
  tip +10.0 mm from SMV (phase 2) -> action=clear        dist=10.0000; vel_scale=1.0; estop=False
  tip + 5.0 mm from SMV (phase 2) -> action=no_fly       dist= 5.0000; vel_scale=0.5; estop=False
  tip + 3.0 mm from SMV (phase 2) -> action=soft_warning dist= 3.0000; vel_scale=0.1; estop=False
  tip + 1.0 mm from SMV (phase 2) -> action=hard_stop    dist= 1.0000; vel_scale=0.0; estop=True
  count_hard_stop_violations on a 20-point safe path: 0 (must be 0)
```

The vessel gate layers nested keep-out radii around each active vessel (for the
superior mesenteric vein: no-fly at 6 mm, soft-warning at 4 mm, hard-stop at 2
mm), reducing velocity and finally e-stopping as the fingertip approaches. A safe
path produces zero hard-stop violations, which is exactly the hard predicate
VVUQ 06 enforces (Section 03, case B, blocks when that count is non-zero). This
is the IEC 80601-2-77 hazardous-situation response and ISO 14971 risk control.

## Deployment safety surface (as executed)

```
  60-second 8-phase Whipple (single humanoid, two hands, 71 DOF)
        |
        v
  +-----------------------------+-----------------------------+-----------------------------+
  | VVUQ 06 vascular no-fly      | VVUQ 09 shared-OR collision | VVUQ 10 fault e-stop        |
  | clear/no-fly/soft/hard-stop  | clear/proximity/contact/    | none/safe-park/hand-back    |
  | 0 violations on safe path    | unsafe -> e-stop at floor   | multi-fault -> escalate     |
  | IEC 80601-2-77, ISO 14971    | ISO/TS 15066, ISO 10218-1   | IEC 60601-1, ISO 13849-1    |
  +-----------------------------+-----------------------------+-----------------------------+
        |
        v
  any ESCALATE -> default hand-back-to-human (UL 4600, IEEE 7009)
```

## External standards anchored here

| Surface | Gate | Governing standards (the credibility basis) |
|---------|------|---------------------------------------------|
| Vascular no-fly hand | VVUQ 06 | IEC 80601-2-77:2019, ISO 14971:2019 |
| Shared-OR collision | VVUQ 09 | ISO/TS 15066:2016, ISO 10218-1:2011, ISO 13482:2014 |
| Fault e-stop degradation | VVUQ 10 | IEC 60601-1, ISO 13849-1:2023, IEEE Std 7009-2024 |
| Whole-body balance (stream) | VVUQ 03 | ISO 13482:2014 |

A single humanoid is higher-risk than a teleoperated multi-arm cart because there
is no second cart and no human bedside assistant to take over instantly. The
three catastrophe gates plus the hand-back-to-human default are the controls that
make that risk defensible, and they are built against published consensus
standards already used in real life. That external grounding is what lets this
deployment reference inform a future physical AI oncology trial credibly.
