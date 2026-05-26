# The 10 Unitree H2-Surgical VVUQ Gates (Specification)

Each gate is a self-contained verify / validate / quantify gate that reuses the
VVUQ-01 contract exactly: verification (pass fraction must equal 1.0), validation
(agreement vs an independent reference at or above the threshold, max relative
error at or below the threshold, human review recorded), uncertainty (coefficient
of variation across at least three runs at or below the threshold; divergence sets
ESCALATE). Decision is ACCEPT / BLOCK / ESCALATE; any single dimension failing
blocks. Thresholds are in `config/vvuq_thresholds.yaml`; standard bindings in
`config/standards_map.yaml`.

## Master table

| # | Gate (slug) | What it gates | V agreement | V max rel err | UQ max CV | Standards |
|---|-------------|---------------|-------------|---------------|-----------|-----------|
| 01 | bimanual-handeye-servo | closed-loop fingertip placement under onboard vision | 0.97 | 0.05 | 0.08 | IEC 80601-2-77, ISO 9283, ASME V&V 40 |
| 02 | dexterous-finger-force | per-finger force control on fragile tissue | 0.95 | 0.05 | 0.10 | IEC 80601-2-77, ISO/TS 15066 |
| 03 | whole-body-balance | standing stability while exerting reaction forces | 0.98 | 0.03 | 0.06 | ISO 13482, IEC 60601-1 |
| 04 | autonomous-plan-correctness | on-prem-LLM plan matches the 8-phase reference | 0.95 | 0.05 | 0.10 | UL 4600, IEEE 7009, IEC 62304 |
| 05 | instrument-grasp-handover | grasping and swapping instruments, slip detection | 0.96 | 0.05 | 0.10 | IEC 80601-2-77, ISO 9283 |
| 06 | vascular-no-fly-hand | tip respects vessel hard-stop volumes | 1.00 | 0.01 | 0.05 | IEC 80601-2-77, ISO 14971 |
| 07 | bimanual-suturing-anastomosis | two-hand ring-tension at PJ/HJ/GJ targets | 0.96 | 0.05 | 0.08 | IEC 80601-2-77, FRS |
| 08 | perception-scene-understanding | segmentation under blood and smoke | 0.95 | 0.05 | 0.10 | ASME V&V 40, IEC 62304 |
| 09 | shared-or-human-collision | human-aware whole-body collision avoidance | 1.00 | 0.02 | 0.06 | ISO/TS 15066, ISO 10218, ISO 13482 |
| 10 | fault-estop-graceful-degradation | detect faults; safe park or hand back | 1.00 | 0.02 | 0.05 | IEC 60601-1, ISO 13849-1, IEEE 7009 |

Gates 06, 09, and 10 carry a verification fraction of 1.0 and the tightest CV
because they are immediate-catastrophe gates (a 1 mm arterial breach, a human
collision, an undetected fall). Each adds a hard predicate that must also pass.

## Per-gate blocks

Each block lists, in order: capability statement, verification checks (all must
pass), validation reference and thresholds, uncertainty design, humanoid-specific
numbers, failure taxonomy (BLOCK and ESCALATE reasons), and grounding citations.

### 01 bimanual-handeye-servo

1. Capability: closed-loop fingertip placement to a Cartesian target under onboard
   vision.
2. Verification: fingertip_samples_present, no_nan_in_tip_trace, within_file_cap,
   schema_valid, lint_clean.
3. Validation: reference `data/reference/handeye_reference.json` (fingertip 0.05
   mm RMS); agreement >= 0.97, max rel err <= 0.05; human review required.
4. Uncertainty: >= 3 seeded runs; cv = stdev / mean per metric; max cv <= 0.08;
   divergence sets ESCALATE.
5. Numbers: 0.05 mm RMS fingertip accuracy at peak velocity.
6. Failure: agreement 0.94 below 0.97 -> BLOCK; cv 0.11 above 0.08 -> BLOCK plus
   ESCALATE.
7. Grounding: IEC 80601-2-77 essential performance; ISO 9283 pose accuracy;
   `src/kinematics/forward_kinematics.py`.

### 02 dexterous-finger-force

1. Capability: per-finger force control that keeps fragile tissue within the cap.
2. Verification: force_samples_present, force_caps_loaded, no_nan_in_force_trace,
   schema_valid, lint_clean.
3. Validation: reference `finger_force_reference.json` (0.02 N tracking error);
   agreement >= 0.95, max rel err <= 0.05; human review required.
4. Uncertainty: max cv <= 0.10.
5. Numbers: per-fingertip soft 2.5 N, hard 3.0 N; bimanual cumulative soft 5.0 N,
   hard 6.0 N.
6. Failure: measured force at or above 3.0 N -> e-stop and BLOCK; cv above 0.10 ->
   BLOCK plus ESCALATE.
7. Grounding: IEC 80601-2-77 force limiting; ISO/TS 15066; `src/hands/finger_force.py`.

### 03 whole-body-balance

1. Capability: standing stability while the hands exert surgical reaction forces.
2. Verification: zmp_samples_present, support_polygon_loaded, no_nan_in_com_trace,
   schema_valid, lint_clean.
3. Validation: reference `balance_zmp_reference.json` (45 mm nominal margin);
   agreement >= 0.98, max rel err <= 0.03; human review required.
4. Uncertainty: max cv <= 0.06.
5. Numbers: ZMP margin floor 8 mm; warning 15 mm; recovery bandwidth 200 Hz.
6. Failure: margin 3.2 mm below the 8 mm floor -> BLOCK; cv 0.21 above 0.06 ->
   BLOCK plus ESCALATE.
7. Grounding: ISO 13482 stability; IEC 60601-1; `src/balance/zmp.py`.

### 04 autonomous-plan-correctness

1. Capability: the on-prem-LLM plan matches the annotated 8-phase reference.
2. Verification: plan_present, reference_plan_loaded, all_phases_covered,
   schema_valid, lint_clean.
3. Validation: reference `plan_reference.json` (1.0 concordance); agreement >=
   0.95, max rel err <= 0.05; human review required.
4. Uncertainty: max cv <= 0.10.
5. Numbers: tip-target tolerance 2.0 mm; 8 phases; 2 intents per phase.
6. Failure: concordance 0.80 below 0.95 -> BLOCK; ambiguous plan -> ESCALATE and
   hand back to human.
7. Grounding: UL 4600 autonomy safety case; IEEE 7009 fail-safe; IEC 62304;
   `src/autonomy/`.

### 05 instrument-grasp-handover

1. Capability: grasping and swapping human-designed instruments with slip
   detection.
2. Verification: grasp_events_present, taxonomy_valid, no_nan_in_grasp_trace,
   schema_valid, lint_clean.
3. Validation: reference `grasp_reference.json` (0.97 success, 0 slips);
   agreement >= 0.96, max rel err <= 0.05; human review required.
4. Uncertainty: max cv <= 0.10.
5. Numbers: 200 ms swap time; four grasp taxonomy classes.
6. Failure: slip event count above 0 -> BLOCK; cv above 0.10 -> BLOCK plus
   ESCALATE.
7. Grounding: IEC 80601-2-77; ISO 9283; `src/hands/grasp.py`, `src/hands/handover.py`.

### 06 vascular-no-fly-hand

1. Capability: the hand or instrument tip respects the five vessel hard-stop
   volumes.
2. Verification: proximity_samples_present, safety_zones_loaded,
   no_nan_in_distance_trace, schema_valid, lint_clean.
3. Validation: reference `vessel_reference.json` (0 breaches, 10 us e-stop);
   agreement >= 1.00, max rel err <= 0.01; human review required.
4. Uncertainty: max cv <= 0.05.
5. Numbers: venous radii 2.0/4.0/6.0 mm; arterial 1.5/3.0/5.0 mm; 10 us
   proximity hard-stop.
6. Hard predicate: hard_stop_violations == 0.
7. Failure: any hard-stop breach -> BLOCK; cv above 0.05 -> BLOCK plus ESCALATE.
   Grounding: IEC 80601-2-77; ISO 14971; `src/safety/vessel_gate.py`.

### 07 bimanual-suturing-anastomosis

1. Capability: two-hand ring-tension control at the PJ, HJ, and GJ targets.
2. Verification: ring_tension_samples_present, targets_loaded,
   no_nan_in_tension_trace, schema_valid, lint_clean.
3. Validation: reference `ring_tension_reference.json` (0.02 N RMSE); agreement >=
   0.96, max rel err <= 0.05; human review required.
4. Uncertainty: max cv <= 0.08.
5. Numbers: PJ 0.45 N, HJ 0.50 N, GJ 0.60 N, each plus or minus 0.05 N.
6. Failure: RMSE outside the band -> BLOCK with grade C; cv above 0.08 -> BLOCK
   plus ESCALATE.
7. Grounding: IEC 80601-2-77; Callery Fistula Risk Score; `src/suturing/`.

### 08 perception-scene-understanding

1. Capability: segmentation of vessels, ducts, margins, and instruments under
   blood and smoke.
2. Verification: masks_present, reference_masks_loaded, all_structures_segmented,
   schema_valid, lint_clean.
3. Validation: reference `perception_reference.json` (0.97 mean Dice) and
   `scene_masks_reference.json`; agreement >= 0.95, max rel err <= 0.05; human
   review required.
4. Uncertainty: max cv <= 0.10.
5. Numbers: five structures; 16 x 16 grid; occlusion sweep parameter.
6. Failure: mean Dice 0.90 below 0.95 -> BLOCK; cv above 0.10 -> BLOCK plus
   ESCALATE.
7. Grounding: ASME V&V 40 validation; IEC 62304; `src/perception/`.

### 09 shared-or-human-collision

1. Capability: human-aware whole-body collision avoidance in the shared OR.
2. Verification: clearance_samples_present, actors_loaded,
   no_nan_in_clearance_trace, schema_valid, lint_clean.
3. Validation: reference `collision_reference.json` (60 mm clearance, 3 ms
   reaction); agreement >= 1.00, max rel err <= 0.02; human review required.
4. Uncertainty: max cv <= 0.06.
5. Numbers: clearance floor 50 mm; bands 50 / 150 / 300 mm; reaction budget 3 ms.
6. Hard predicate: min_clearance_mm >= 50.0.
7. Failure: clearance below 50 mm -> BLOCK and e-stop; cv above 0.06 -> BLOCK plus
   ESCALATE. Grounding: ISO/TS 15066; ISO 10218; ISO 13482; `src/safety/human_collision.py`.

### 10 fault-estop-graceful-degradation

1. Capability: detect balance, joint, vision, thermal, and power faults; safe park
   or hand back.
2. Verification: fault_events_present, budgets_loaded, no_nan_in_latency_trace,
   schema_valid, lint_clean.
3. Validation: reference `fault_reference.json` (50 us detection, 1.0 safe-state
   success); agreement >= 1.00, max rel err <= 0.02; human review required.
4. Uncertainty: max cv <= 0.05 (the most ESCALATE-prone gate).
5. Numbers: 3 ms e-stop budget; 50 us park; per-fault detection latencies.
6. Hard predicate: safe_state_success_rate == 1.0.
7. Failure: safe state not reached in budget -> BLOCK; ambiguous or multiple
   faults -> ESCALATE and hand back. Grounding: IEC 60601-1; ISO 13849-1; IEEE
   7009; `src/safety/estop.py`.
