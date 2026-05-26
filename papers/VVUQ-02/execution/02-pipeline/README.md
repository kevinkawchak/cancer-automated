# Section 02: Pipeline Execution (intent to compile to act to score)

This section runs the humanoid control pipeline end to end: an on-prem LLM
proposes phase-level intents, a deterministic policy compiles them to per-hand
commands, the behavior models act (kinematics, perception, hands, balance,
suturing), and the result feeds the composite score that the assurance layer
gates. Every behavior here is the candidate the next section's VVUQ gates judge.
The point of the thesis is visible already: producing these behaviors is fast and
deterministic, while deciding whether they may ship is the substantial work that
follows in Section 03.

## Contents

| File | What it records |
|------|-----------------|
| artifacts/pipeline_execution_log.txt | The verbatim output of the pipeline driver across the six behavior groups |

## Pipeline data flow (as executed)

```
  on-prem LLM intent            deterministic compile           behavior models
  (offline fallback)        --> (policy, schema-conformant)  -->  (act)
  +-------------------+         +----------------------+         +------------------+
  | propose_intents() |  -->    | compile_intents()    |  -->    | kinematics       |
  | phase 1, phase 5  |         | 20-DOF finger target |         | perception (Dice)|
  | source=reference  |         | + tip frame + grasp  |         | hands (force)    |
  +-------------------+         +----------------------+         | balance (ZMP)    |
        |                              |                         | suturing (RMSE)  |
        v                              v                         +------------------+
  VVUQ 04 concordance           h2_command.schema.json                   |
  vs annotated reference        conformant commands                      v
        |                                                          6-component
        +--------------------------------------------------------> composite score
                                                                   (gated in 03)
```

## What ran, and the result

The driver imported the codegen modules directly and exercised one
representative call per behavior group. Backend selection returned `offline`, the
honest CI path: no anthropic, ollama, or openai backend was installed, so the
autonomy module emitted the frozen reference plan. The verbatim output is in
`artifacts/pipeline_execution_log.txt`; the highlights:

### 1. Autonomy: on-prem LLM intent to deterministic compile (VVUQ 04, the thesis core)

```
  backend selected: offline
  phase 1: 2 intents -> 2 commands; source=reference; concordance=1.000
  phase 5: 2 intents -> 2 commands; source=reference; concordance=1.000
```

The compiler turned each high-level intent into a schema-conformant command (a
Cartesian fingertip target plus 20 per-finger joint targets plus a grasp state).
Phase-step concordance against the annotated reference plan is 1.000, the
validation metric for VVUQ 04 under UL 4600 and IEEE 7009.

### 2. Kinematics: forward kinematics of the right 7-DOF arm from config

```
  arm 'R': 7 joints; base (0.0, -0.18, 1.25); tip = (-0.2796, -0.2895, 1.8185) m
```

The DH chain was loaded from `config/h2_kinematics.yaml` and solved to a tip
position in the world frame, the ISO 9283 pose-accuracy property.

### 3. Perception: scene segmentation Dice vs occlusion (VVUQ 08)

```
  occlusion 0.00 -> mean Dice 1.0000
  occlusion 0.10 -> mean Dice 0.9208
  occlusion 0.20 -> mean Dice 0.8290
  occlusion 0.30 -> mean Dice 0.8185
  NIR/US/bile fusion usable structures (>=0.5): ['bile_duct', 'instrument', 'pancreatic_duct', 'tumor_margin', 'vessel']
```

Mean Dice degrades smoothly as blood-or-smoke occlusion rises, and all five
structures remain usable after NIR ICG, ultrasound, and bile-channel fusion.

### 4. Hands: fingertip force, bimanual cap, grasp, handover (VVUQ 02, 05)

```
  track_force -> commanded 1.84 N; soft_exceeded=False; estop=False; err=0.1600 N
  bimanual_check -> cumulative 5.0 N; within_hard=True; estop=False
  grasp(needle_driver) -> success=True; slip=False; quality=0.7521
  handover(R->L) -> success=True; recv_quality=0.7922; duration=200.0 ms
```

Fingertip force tracking stays under the soft cap, the summed cross-hand force is
within the bimanual hard cap, and a needle-driver grasp and a right-to-left
handover both succeed without slip. These are the ISO/TS 15066 force-limit and
IEC 80601-2-77 instrument-handling properties.

### 5. Balance: ZMP margin and posture recovery under disturbance (VVUQ 03)

```
  push   0.0 N -> margin 130.00 mm; corrected 130.00 mm; force_scale 1.0; state=stable; estop=False
  push  20.0 N -> margin 96.17 mm; corrected 96.17 mm; force_scale 1.0; state=stable; estop=False
  push  40.0 N -> margin 62.33 mm; corrected 62.33 mm; force_scale 1.0; state=stable; estop=False
```

The zero-moment-point margin stays well inside the support polygon across the
full disturbance range, so the standing humanoid holds balance without an ankle
strategy reduction, the ISO 13482 stability property.

### 6. Suturing: bimanual anastomosis ring-tension control (VVUQ 07)

```
  pancreaticojejunostomy  : 16 stitches; RMSE 0.00326 N; in-band 1.0; grade A
  hepaticojejunostomy     : 12 stitches; RMSE 0.00328 N; in-band 1.0; grade absent
  gastrojejunostomy       :  9 stitches; RMSE 0.00465 N; in-band 1.0; grade patent
```

All three reconstructions hold ring tension in band for every stitch. The
pancreaticojejunostomy is graded against the Fistula Risk Score, where grade A is
the no-fistula outcome.

## Reproduction

The driver imports the codegen `src` package, so it is run with the codegen tree
on `PYTHONPATH`:

```bash
cd papers/VVUQ-02/codegen
PYTHONPATH=. python - <<'PY'
from src.autonomy.llm_intent import propose_intents, backend_select
from src.autonomy.plan_compiler import compile_intents, phase_step_concordance
# ... see artifacts/pipeline_execution_log.txt for the full driver and output
PY
```

## External standards anchored here

| Behavior group | Gate | Governing standards (add the credibility) |
|----------------|------|-------------------------------------------|
| Autonomy intent and compile | VVUQ 04 | UL 4600 (2023), IEEE Std 7009-2024, IEC 62304 |
| Forward kinematics | VVUQ 01 | ISO 9283:1998, IEC 80601-2-77:2019 |
| Perception and fusion | VVUQ 08 | ASME V&V 40-2018, IEC 62304 |
| Fingertip force and grasp | VVUQ 02, 05 | ISO/TS 15066:2016, IEC 80601-2-77:2019 |
| Whole-body balance | VVUQ 03 | ISO 13482:2014, IEC 60601-1 |
| Suturing and anastomosis | VVUQ 07 | IEC 80601-2-77:2019, Fistula Risk Score |

Each behavior is grounded in a published consensus standard already used in real
life. That grounding is what makes the candidate auditable and is the reason the
assurance argument in Section 03 is defensible rather than ad hoc.
