## output-instruct.md
I'll research both repositories to understand the prior VVUQ-01 project structure and the surgical context, then synthesize the VVUQ-02 instructions. Let me start by loading the GitHub tools I need.

Now let me explore both directories in parallel to understand the prior project structure and surgical context.

Both share a parallel structure. Let me explore the key instruction-bearing directories in both projects in parallel.

The `execution/README.md` (21KB) and `image-instruct/README.md` (16KB) are the core methodology docs. Let me read those and explore the pdac codegen/instructions directories in parallel.

I now understand the VVUQ-01 pattern well (execution-record + front-loaded VVUQ gate + image-instruct + paper templates). Now let me read the codegen architecture and the core surgical specification files from the PDAC paper to ground the VVUQ-02 instructions.

Excellent grounding on the codegen architecture and surgical specs. Now let me pull the actual VVUQ gate decision surface from VVUQ-01 plus the remaining surgical safety/sensor/anastomosis specs to ground the 10 humanoid-specific VVUQs precisely.

I now have full grounding from both repos: the VVUQ-01 framework (the V/V/UQ gate with its exact thresholds, the front-loaded instruction → execution → imagegen → paper lineage, single-PR per-section commits) and the PDAC surgical context (robot spec, 640-channel sensor stack, multi-arm coordination, vascular safety zones, anastomosis protocols, the codegen tree pattern). Here is the complete VVUQ-02 instruction set.

---

# VVUQ-02 Project Instructions: 10 Unitree H2 Autonomous Humanoid Surgeon VVUQs

> House-style note: this document follows the source-repo conventions so it can drop straight into your tree - single hyphens only (no em/en/double dashes), plain GitHub-Flavored Markdown, black text, ASCII for diagrams. It is a specification only. It contains zero generated source code; it tells a future Claude Code Opus 4.7 1M Max session exactly what to author. Nothing here is committed.

## 0. What VVUQ-02 is, in one paragraph

VVUQ-01 (`cancer-automated/papers/VVUQ-01`) established the thesis that the LLM VVUQ process must be more substantial than the artifact it gates, and proved a strict 3-dimension gate (Verification, Validation, Uncertainty Quantification → ACCEPT / BLOCK / ESCALATE) over codegen, imagegen, and papergen. The PDAC paper (`robotic-surgeries/2030-pdac-1min/paper`) applied an on-premises-LLM-commands-a-surgical-robot thesis to a fixed 8-arm coelomic platform (PancreSpeed 1.0). **VVUQ-02 fuses the two**: it applies the VVUQ-01 gate to a fundamentally harder subject - a **single autonomous humanoid** (Unitree H2 surgical variant) that performs the surgery with its own two dexterous hands, standing at the table, with no teleoperation. The deliverable is **10 humanoid-specific VVUQs**, each a fully specified verify/validate/quantify gate, plus the codegen, imagegen, and paper scaffolding to execute and document them.

---

## 1. Placement, naming, and the hypothetical-platform rule

| Item | Value |
|------|-------|
| Project root | `cancer-automated/papers/VVUQ-02/` (sibling of `VVUQ-01/`) |
| Spec/instruction dir | `papers/VVUQ-02/instructions/` (analogue of PDAC `paper/instructions/` and VVUQ-01 `paper-instruct/`) |
| Generated codebase target | `papers/VVUQ-02/codegen/` (analogue of PDAC `paper/codegen/`) |
| Figure specs | `papers/VVUQ-02/image-instruct/NN-name/README.md` |
| Future figure outputs | `papers/VVUQ-02/imagegen/NN-name/NN-name.{py,png}` |
| Execution record (future run) | `papers/VVUQ-02/execution/` |
| Paper drafts | `papers/VVUQ-02/{draft-paper,full-paper,final-paper}/` |
| LaTeX template | `papers/VVUQ-02/templates/Template_11/` |
| Inputs corpus | `papers/VVUQ-02/inputs/` |

**Hypothetical-platform rule (mandatory, inherited from PDAC `robot_specification_pancrespeed.md`).** The Unitree H2 is a real full-size bipedal humanoid lineage with dexterous multi-finger hands and on-board compute. A *surgical* H2 does not exist. Therefore the project defines a clearly labeled **"Unitree H2-Surgical 1.0 (hypothetical 2030 surgical variant)"**: the base form factor traces to the real H2 lineage; every clinical-grade capability uplift (sub-0.1 mm fingertip accuracy, 100 kHz fingertip force, 3 ms e-stop) is explicitly flagged hypothetical 2030 and is paper-only. Every comparison against PancreSpeed 1.0 or human surgeons is flagged simulation-against-simulation in the limitations, exactly as PDAC does.

---

## 2. Thesis and scope

**Thesis (VVUQ-02).** An on-premises, repository-based LLM issues high-level commands to a single autonomous humanoid surgeon that senses in real time and acts through its own two hands via x/y/z tip and per-finger joint targets. Because one humanoid concentrates all error potential into one body (no second cart, no human bedside assistant in the loop), the **VVUQ assurance layer must be more substantial, stricter, and more thoroughly exercised than the humanoid's control code itself** - and it must clear 10 distinct humanoid-specific gates before any candidate behavior is allowed to ship. The assurance work, done cheaply and reproducibly by an autonomous agent, is the substantial part; the motion code is the easy part.

**Scope (frozen, single synthetic patient, single procedure).**
- Reuse PDAC patient **PAT-PDAC-0001** (68 y, head-of-pancreas PDAC, 3.4 cm abutting the SMV at 75 deg, KRAS G12D, neoadjuvant mFOLFIRINOX x4) and the **60-second 8-phase Whipple timeline** from PDAC `instructions/README.md`, so VVUQ-02 is directly comparable to the 8-arm PancreSpeed baseline. The only change is the **actuator**: one H2-Surgical humanoid with two 7-DOF arms and two ~20-DOF dexterous hands replaces eight fixed coelomic arms.
- One robot: **Unitree H2-Surgical 1.0 (hypothetical 2030)**.
- One iteration design: **32 deterministic iterations**, seed `20260525` (your `currentDate`), Latin hypercube, identical contract to PDAC.
- One competition: H2-Surgical vs the 8-arm PancreSpeed 1.0 (VVUQ-01/PDAC baseline) vs a teleoperated da Vinci-successor vs the 2025 Dutch human-surgeon cohort. Time-dimension caveat (1 min robot vs 4-8 h human) preserved in every rationale.
- Ten VVUQs (Section 4) are the primary deliverable.

---

## 3. Unitree H2-Surgical 1.0 platform specification (author as `instructions/h2_robot_specification.md`)

Author a spec file in the exact shape of PDAC `robot_specification_pancrespeed.md`, fixing these hypothetical 2030 values. Flag the uplift as hypothetical; base form factor as real H2 lineage.

| Property | H2-Surgical 1.0 (hyp. 2030) | PancreSpeed 1.0 (PDAC baseline) | Stock H2 lineage (real, ~2025) |
|----------|------------------------------|----------------------------------|-------------------------------|
| Morphology | Bipedal humanoid, standing at table | 8 fixed coelomic arms on boom | Bipedal humanoid |
| Manipulators | 2 arms | 8 arms | 2 arms |
| DOF per arm | 7 | 7 | 7 |
| Hands | 2 dexterous, 5 fingers each | rigid tool end-effectors | 2 dexterous |
| DOF per hand | 20 (5 fingers x 4 joints) | n/a | ~20 (tendon/linkage) |
| Locomotion/stance DOF | 2 legs x 6 + waist 3 | none (fixed base) | 2 legs x 6 + waist |
| Head/vision DOF | 2 (pan, tilt) | n/a | 2 |
| Total DOF | 14 arm + 40 hand + 15 stance + 2 head = 71 | 56 | ~ matches base |
| Fingertip positioning accuracy at peak vel (mm RMS) | 0.05 (hyp.) | 0.05 | mm-class |
| Fingertip force resolution (N) | 0.01 at 100 kHz (hyp.) | 0.01 at 100 kHz | coarse |
| Per-fingertip force cap soft / hard (N) | 2.5 / 3.0 | 2.5 / 3.0 (per arm) | n/a |
| Bimanual cumulative tip force cap soft / hard (N) | 5.0 / 6.0 | 15.0 / 18.0 (8 arms) | n/a |
| Hand-arm e-stop latency (ms) | 3 (hyp.) | 3 | n/a |
| Joint park latency (us) | 50 (hyp.) | 50 | n/a |
| Balance recovery bandwidth (Hz) | 200 (hyp.) | n/a (fixed base) | balance-capable |
| Control/command rate (kHz) | 10 | 10 | lower |
| Force sample rate (kHz) | 100 | 100 | lower |
| On-prem LLM command interface | yes (thesis) | yes (thesis) | research |
| Regulatory framing | IEC 80601-2-77 + 60601 + ISO 13482 (personal-care/service robot) + FDA SaMD Class III | IEC 80601-2-77 + FDA SaMD | none clinical |

The decisive difference from PancreSpeed: **balance and dexterity are now safety-critical**. A fixed arm cannot fall over; a standing humanoid can. Fingers can drop a needle. These differences motivate VVUQs 1, 2, 3, 5, and 9 below.

Also author the supporting spec files:
- `instructions/h2_hand_kinematics.md` - per-finger 4-DOF chains, tendon/coupling limits, fingertip frames, the bimanual workspace, grasp taxonomy (pinch, tripod, power, needle-driver hold).
- `instructions/perception_stack_spec.md` - head stereo RGB + NIR ICG + endoscopic/ultrasound fusion channels (reuse PDAC NIR ICG, vessel proximity, bile spectrophotometry, US B-mode definitions from `sensor_specification_100khz.md`); add wrist/palm cameras.
- `instructions/autonomy_policy_spec.md` - the on-prem-LLM-to-motion stack: LLM emits phase-level intents; a deterministic policy compiles intents to x/y/z tip + per-finger joint targets; the 8-phase timeline is the reference plan.
- `instructions/shared_or_safety_protocol.md` - human-aware whole-body collision avoidance (humanoid analogue of PDAC `multi_arm_coordination_8arm.md`).
- `instructions/suturing_anastomosis_protocol.md` - bimanual suturing/knot-tying realizing the PDAC `anastomosis_protocols.md` ring-tension targets (PJ 0.45 N, HJ 0.50 N, GJ 0.60 N, +/-0.05 N band) with two hands instead of arm pairs.

---

## 4. The 10 Unitree H2-Surgical VVUQs (the heart of the project)

Author as `instructions/vvuq_gate_spec.md`. Each VVUQ is a self-contained gate that reuses the VVUQ-01 contract exactly: **Verification** (structural/policy checks; pass fraction must == 1.0), **Validation** (agreement vs a reference >= threshold, max relative error <= threshold, human review recorded == true), **Uncertainty Quantification** (coefficient of variation across >= 3 runs <= threshold; divergence sets ESCALATE). Decision = ACCEPT / BLOCK / ESCALATE; any single dimension failing blocks. These mirror VVUQ-01 `configs/vvuq_thresholds.yaml` and `execution/03-vvuq/README.md`.

### 4.1 Master table

| # | VVUQ (slug) | What it gates (humanoid-specific) | Primary metric(s) | V agreement | V max rel err | UQ max CV | Grounding |
|---|-------------|------------------------------------|-------------------|-------------|---------------|-----------|-----------|
| 01 | `bimanual-handeye-servo` | Closed-loop fingertip placement under onboard vision | fingertip RMS error (mm) vs optical-tracker truth | 0.97 | 0.05 | 0.08 | H2 spec 0.05 mm; PDAC ee_pos 0.01 mm |
| 02 | `dexterous-finger-force` | Per-finger force control on fragile tissue | per-fingertip force tracking error (N) | 0.95 | 0.05 | 0.10 | per-fingertip 2.5/3.0 N; PDAC force caps |
| 03 | `whole-body-balance` | Standing stability while exerting surgical reaction forces | ZMP stability margin (mm) inside support polygon | 0.98 | 0.03 | 0.06 | ISO 13482; H2 balance bandwidth |
| 04 | `autonomous-plan-correctness` | On-prem-LLM plan matches the 8-phase Whipple reference | phase-step concordance vs annotated reference plan | 0.95 | 0.05 | 0.10 | PDAC 8-phase timeline; thesis |
| 05 | `instrument-grasp-handover` | Grasping/swapping human-designed instruments, slip detection | grasp-success rate, slip-event count | 0.96 | 0.05 | 0.10 | PDAC tool changer; hand kinematics |
| 06 | `vascular-no-fly-hand` | Hand/instrument tip respects vessel hard-stop volumes | hard-stop violation count (must be 0); e-stop latency | 1.00 | 0.01 | 0.05 | PDAC `vascular_safety_protocol.md` |
| 07 | `bimanual-suturing-anastomosis` | Two-hand ring-tension control at PJ/HJ/GJ targets | ring-tension RMS error vs +/-0.05 N band | 0.96 | 0.05 | 0.08 | PDAC `anastomosis_protocols.md`, FRS |
| 08 | `perception-scene-understanding` | Segmentation of vessels/ducts/margins/instruments under blood/smoke | Dice/agreement vs labeled reference | 0.95 | 0.05 | 0.10 | PDAC NIR ICG, US, bile spectro |
| 09 | `shared-or-human-collision` | Human-aware whole-body collision avoidance in shared OR | min human-clearance (mm); intrusion-reaction latency | 1.00 | 0.02 | 0.06 | PDAC collision FSM, human-aware |
| 10 | `fault-estop-graceful-degradation` | Detect balance/joint/vision/thermal faults; safe park or hand-back | fault-detection latency; safe-state success rate | 1.00 | 0.02 | 0.05 (ESCALATE-heavy) | PDAC e-stop budgets; ESCALATE policy |

VVUQs 06, 09, 10 carry a **Verification fraction of 1.0 and the tightest CV** because they are immediate-catastrophe gates (a 1 mm arterial breach, a human collision, an undetected fall). VVUQs 01-05, 07-08 are capability gates at the VVUQ-01 default-strict level.

### 4.2 Per-VVUQ detail to author (template, repeat x10)

For each VVUQ author one block in `vvuq_gate_spec.md` containing exactly these fields, so the future codegen is deterministic:

1. **Capability statement** - one sentence on the humanoid behavior being gated.
2. **Verification checks (list, all must pass, fraction == 1.0)** - structural/policy predicates. Example for `whole-body-balance`: ZMP samples present for all 600,000 ticks; support-polygon config loaded; no NaN in CoM trace; estop_state schema valid; output Parquet under 5 MB; ruff/yamllint clean.
3. **Validation reference + thresholds** - the named reference artifact (e.g., `data/reference/balance_zmp_reference.parquet`), the agreement metric definition, the agreement threshold and max-relative-error from the master table, and `require_human_review: true`.
4. **Uncertainty design** - >= 3 seeded runs, the per-metric CV computation (`cv = stdev/mean`), the max-CV bound, and the divergence → ESCALATE rule.
5. **Humanoid-specific numbers** - the hard physical limits this gate enforces (force caps, latencies, clearances, accuracy) taken from Section 3 and the PDAC specs.
6. **Failure taxonomy** - the BLOCK reasons and the ESCALATE reason, mirroring the PDAC/VVUQ-01 verbatim case list (e.g., "balance margin 3.2 mm below 8 mm floor → BLOCK"; "CV 0.21 above 0.06 → BLOCK + ESCALATE").
7. **Grounding citations** - relative paths into VVUQ-01 and the PDAC paper.

---

## 5. Repository tree to generate (codegen target - do NOT generate now)

Author this tree under `papers/VVUQ-02/codegen/`, mirroring the PDAC `codegen/` layout but reorganized around the humanoid and the 10 VVUQs.

```
papers/VVUQ-02/codegen/
  README.md                      # project README (PDAC codegen README shape)
  LICENSE.txt                    # MIT
  pyproject.toml                 # py3.10/3.11/3.12 + ruff + extras [dev,llm-local,zenodo,viz]
  docker-compose.yml             # python + rust + duckdb services
  .gitignore .yamllint .markdownlint.yaml .pre-commit-config.yaml
  config/
    project.yaml                 # frozen scope: patient, seed 20260525, 32 iters
    h2_kinematics.yaml           # 2x7-DOF arms DH params; head/waist/leg chains
    hand_model.yaml              # per-finger 4-DOF, tendon coupling, fingertip caps
    balance_model.yaml           # mass, CoM, support polygon, ZMP margins
    perception_model.yaml        # camera intrinsics, NIR/US/bile channel map
    vvuq_thresholds.yaml         # <-- the 10 VVUQ gates (Section 7)
    iterations.yaml              # 32-iter Latin hypercube, seed 20260525
    safety_zones.yaml            # 5 vessel no-fly volumes (copied from PDAC)
    anastomosis_targets.yaml     # 3 ring-tension targets (copied from PDAC)
    shared_or_actors.yaml        # human actor poses/keep-out volumes
  schemas/
    h2_sensor_record.schema.json / .proto / .avsc   # per-tick humanoid sensor record
    h2_command.schema.json / .proto                 # x/y/z tip + per-finger joint targets
    vvuq_case.schema.json                           # one VVUQ candidate case
    vvuq_decision.schema.json                       # ACCEPT/BLOCK/ESCALATE + reasons + scores
    metrics.schema.json                             # composite score breakdown
  src/
    perception/      segment.py, fuse_nir_us.py        # VVUQ 08
    autonomy/        llm_intent.py, plan_compiler.py   # VVUQ 04 (thesis core)
    hands/           grasp.py, finger_force.py, handover.py  # VVUQ 02, 05
    balance/         zmp.py, posture_controller.py     # VVUQ 03
    control/         arm_loop.cpp, hand_loop.cpp        # 10 kHz command, 100 kHz force
    safety/          vessel_gate.py, human_collision.py, estop.py  # VVUQ 06, 09, 10
    suturing/        bimanual_suture.py, ring_tension.py # VVUQ 07
    vvuq/            verification.py, validation.py, uncertainty.py,
                     vvuq_gate.py, gate_registry.py     # <-- the 10-gate harness
    simulation/      iterate.py, runner.rs              # 32-iter deterministic sweep
    metrics/         compute.py                         # composite score
    llm/             compare_agent.py                   # 4-entrant tournament
    zenodo/          patch_pointers.py                  # L0 raw pointer manifest
  data/
    reference/       per-VVUQ reference artifacts (truth for the validation dimension)
    sample_h2_sensor.csv, sample_h2_sensor.jsonl
    iterations/      run_NNNNN_{L1,L2,L3,L4,events}.* , index.jsonl, *_L0_raw.zenodo_pointer.json
    human_surgeon_baseline.csv
  prompts/           autonomy_intent_prompt.md, comparison_prompt.md
  results/           vvuq_decisions.json, vvuq_report.md, comparison_report.md
  viz/               *.txt ASCII (per-VVUQ + balance + grasp + collision diagrams)
  outputs/           per-VVUQ outputs, diagrams/, logs/
  notebooks/         vvuq_analysis.ipynb, balance_analysis.ipynb, perception_analysis.ipynb
  tests/             one test module per src package + per-VVUQ gate tests
  docs/              architecture.md, sensor_spec.md, vvuq_methodology.md, ...
  releases/v0.1.0/   manifest.json, metrics.json, iterations_index.jsonl, sample_seeds.txt
```

---

## 6. Exact code generation instructions (per module, behavior-level - no source code)

For every file the future session authors, specify path, language, purpose, public signatures (described, not implemented), inputs/outputs, the thresholds/limits it enforces, and its covering test. Below is the exact instruction content to write into the per-commit instruction files. **Do not write function bodies; write contracts.**

### 6.1 `src/vvuq/` - the 10-gate harness (centerpiece, must be authored first and tested hardest)

- `verification.py` - define `verify(case) -> VerificationResult` returning `fraction_passed: float`, `all_passed: bool`, and a per-check list. Instruction: implement exactly the VVUQ-01 6-check pattern (all_stages_complete, artifacts_present, artifacts_non_empty, within_file_cap, schema_valid, lint_clean) generalized so each of the 10 VVUQs supplies its own check predicates from `vvuq_thresholds.yaml`. Gate requires `fraction_passed == 1.0`.
- `validation.py` - define `validate(observed, reference, *, require_human_review) -> ValidationResult` returning `agreement: float`, `max_relative_error: float`, `human_review: bool`. Instruction: agreement = fraction of compared metrics within the per-VVUQ max-relative-error tolerance; mirror VVUQ-01 Example 2 semantics.
- `uncertainty.py` - define `quantify(runs) -> UncertaintyResult` returning per-metric `mean, stdev, cv` and `max_cv`, with `min_consensus_runs` and `confidence_level`. CV = population stdev / mean, exactly as VVUQ-01.
- `vvuq_gate.py` - define `class VVUQGate` with `evaluate(verification, validation, uncertainty, thresholds) -> GateDecision`. `GateDecision` fields: `accepted, blocked, escalate, reasons[], scores{}`. Logic: block on any dimension failure; set escalate when `max_cv > max_cv_threshold` (divergence). Identical control flow to VVUQ-01 `vvuq/vvuq_gate.py`.
- `gate_registry.py` - define `GATES: dict[str, GateSpec]` enumerating the 10 VVUQ slugs, each binding its verification predicates, its reference artifact path, and its threshold block from `vvuq_thresholds.yaml`. Provide `run_gate(slug, iteration_outputs) -> GateDecision` and `run_all(iteration_outputs) -> dict[slug, GateDecision]`.
- Tests: for each of the 10 gates, author at minimum 1 ACCEPT case and 4-5 BLOCK/ESCALATE cases (mirror VVUQ-01 `execution/03-vvuq` six-case surface). Total target: >= 60 gate tests plus package unit tests, so the suite is comparable to VVUQ-01's 51.

### 6.2 `src/autonomy/` - the "all on their own" core (VVUQ 04)

- `llm_intent.py` - `propose_intents(scene_state, phase) -> list[Intent]`. Instruction: on-prem LLM path with a deterministic offline template fallback (guarded import of `anthropic`/local model; if absent, emit the frozen reference plan). This is the honest-CI path VVUQ-01 documents.
- `plan_compiler.py` - `compile(intents) -> list[Command]` where `Command` conforms to `schemas/h2_command.schema.json` (x/y/z tip target per hand + per-finger joint targets + tool/grasp state). Deterministic, seed-stable. Enforce phase-timeline concordance used by VVUQ 04.

### 6.3 `src/perception/` (VVUQ 08), `src/hands/` (VVUQ 02, 05), `src/balance/` (VVUQ 03)

- `perception/segment.py` - `segment(frame_bundle) -> SceneMasks` (vessels, pancreatic duct, bile duct, tumor margin, instruments). `fuse_nir_us.py` - `fuse(rgb, nir_icg, us_bmode, bile_spectro) -> FusedScene`. Outputs feed VVUQ 08 Dice/agreement against `data/reference/scene_masks_reference.*`.
- `hands/finger_force.py` - `track_force(target_N, measured_N) -> FingerForceCmd`, enforcing per-fingertip soft 2.5 N / hard 3.0 N and bimanual cumulative soft 5.0 / hard 6.0 N. `grasp.py` - `grasp(object_pose, taxonomy) -> GraspResult` with slip detection. `handover.py` - instrument pick/place/swap (200 ms swap analogue).
- `balance/zmp.py` - `zmp_margin(com, support_polygon, external_wrench) -> float` (mm inside polygon). `posture_controller.py` - `stabilize(...)` maintaining margin above the 8 mm floor under surgical reaction forces. Feeds VVUQ 03.

### 6.4 `src/safety/` (VVUQ 06, 09, 10)

- `vessel_gate.py` - port PDAC `safety_zone_gate.py` exactly (clear / no-fly 50% / soft-warning 10% / hard-stop e-stop), driven by the per-hand tip and the 100 kHz vessel-proximity sensor (10 us one-tick e-stop). VVUQ 06 requires zero hard-stop violations.
- `human_collision.py` - whole-body human-aware FSM (clear/proximity/contact/unsafe) keyed on min distance from any humanoid link to any human actor in `shared_or_actors.yaml`. VVUQ 09 requires min-clearance never below the hard floor and intrusion-reaction within budget.
- `estop.py` - unified fault monitor: balance-loss, joint fault, vision dropout, thermal, power. Emits safe-park or hand-back-to-human. VVUQ 10 measures detection latency and safe-state success, and is the gate most likely to ESCALATE.

### 6.5 `src/control/` (C++), `src/simulation/`, `src/metrics/`, `src/llm/`, `src/zenodo/`

- `control/arm_loop.cpp`, `hand_loop.cpp` - 10 kHz command + 100 kHz force loops, deterministic, no GPU/display required (pure-stdlib reference, guarded heavy backends), per VVUQ-01 limitations posture.
- `simulation/iterate.py` (+ `runner.rs`) - 32-iteration Latin hypercube sweep, seed `20260525`, bit-identical Parquet across platforms; free parameters: fingertip placement noise, finger-force noise, balance disturbance amplitude, perception occlusion fraction, ring-tension drift.
- `metrics/compute.py` - reuse PDAC 6-component composite (Quality 0.30, Time 0.20, Cost 0.15, Safety 0.15, Patient experience 0.05, Anastomosis quality 0.15) and add the 10-VVUQ pass/escalate roll-up as a gating overlay (composite is reported only if all 10 gates ACCEPT; otherwise the report shows BLOCK/ESCALATE).
- `llm/compare_agent.py` - 4-entrant tournament (H2-Surgical vs PancreSpeed 1.0 vs da Vinci-successor vs Dutch human baseline) under frozen weights, time-caveat preserved.
- `zenodo/patch_pointers.py` - L0 raw pointer/SHA-256 manifest; L0 never committed (humanoid L0 is larger - 71 DOF - so the Zenodo discipline matters more).

### 6.6 Schemas, data pyramid, CI

- Schemas: author JSON Schema + Protobuf + Avro for the sensor record and command; JSON Schema for `vvuq_case` and `vvuq_decision`. The humanoid sensor record extends the PDAC 80-channel-per-arm pattern with per-finger joint/force channels and balance channels (CoM, ZMP, support-polygon margin, ankle/hip torques).
- Pyramid: same L0(Zenodo)/L1/L2/L3/L4(event)/events layering as PDAC `file_size_pyramid_1min.md`; every committed Parquet < 5 MB, every committed file < 10 MB.
- CI: ruff format --check, ruff check, yamllint -d relaxed, markdownlint, file-size and Parquet-size caps, line-ending and trailing-whitespace gates - identical to PDAC `ci_compliance_checklist.md`. Heavy/optional backends guarded so core runs with no install (VVUQ-01 posture).

---

## 7. `config/vvuq_thresholds.yaml` contents (author exactly these 10 blocks)

Specify the YAML so codegen is deterministic. One top-level key per VVUQ slug; each block carries the three dimensions plus the gate policy. Use the master-table values from Section 4.1. Shape (described, not as runnable code):

- `verification:` `min_checks_passed_fraction: 1.0`, `require_schema_valid: true`, `require_lint_clean: true`, plus a `checks:` list of the per-VVUQ predicate names.
- `validation:` `min_agreement: <from table>`, `max_relative_error: <from table>`, `require_human_review: true`, `reference: <path>`.
- `uncertainty:` `max_coefficient_of_variation: <from table>`, `min_consensus_runs: 3`, `confidence_level: 0.95`.
- `gate:` `block_on_any_failure: true`, `escalate_on_divergence: true`.

A global `defaults:` block holds the VVUQ-01 baseline (agreement 0.95, max_rel_err 0.05, max_cv 0.10) and each VVUQ overrides only what differs (e.g., `vascular-no-fly-hand` sets `max_relative_error: 0.01`, `max_coefficient_of_variation: 0.05`, and an extra hard check `hard_stop_violations == 0`).

---

## 8. Deterministic seed and iteration contract

- Root seed `20260525`; 32 iterations; Latin hypercube over the five free parameters in 6.5. Per-iteration committed budget mirrors PDAC (target total ~30-35 MB; L0 to Zenodo only). Outputs are bit-identical across MacOS/Windows/Linux/A100/H100/Claude Code, per PDAC `runtime_environments.md` (author the same five recipes).

---

## 9. Image-instruct set (10 figures, one per VVUQ) - author as `image-instruct/README.md` + `NN-name/README.md`

Reuse the VVUQ-01 `image-instruct/README.md` conventions verbatim: portrait `figsize=(8.5, 11)`, 300 dpi, white background only, `matplotlib.use("Agg")`, the shared palette (navy `#1F3A5F`, teal `#2A9D8F`, accept green `#2E7D32`, block red `#C0392B`, escalate amber `#E1A93B`, ...), `§` for sections, single hyphens, ruff-clean self-contained scripts, future outputs at `imagegen/NN-name/NN-name.{py,png}`, one commit per figure. Map each figure to its VVUQ and a non-basic chart family:

| No. | Figure slug | Chart family | Gated VVUQ |
|-----|-------------|--------------|------------|
| 01 | `ten-vvuq-gate-funnel` | Funnel (candidates → 10 gates → ACCEPT) | all |
| 02 | `handeye-accuracy-radial` | Radial error / polar scatter | 01 |
| 03 | `finger-force-ridgeline` | Ridgeline of per-finger force | 02 |
| 04 | `balance-zmp-support-polygon` | Support-polygon + ZMP trace | 03 |
| 05 | `autonomy-plan-swimlane` | Swimlane vs reference plan | 04 |
| 06 | `vessel-no-fly-heatmap` | Proximity heatmap | 06 |
| 07 | `bimanual-suture-tension-stream` | Streamgraph of ring tension | 07 |
| 08 | `perception-dice-treemap` | Treemap of per-structure Dice | 08 |
| 09 | `shared-or-clearance-statemap` | State diagram + clearance bands | 09 |
| 10 | `fault-escalation-sankey` | Sankey ACCEPT/BLOCK/ESCALATE flow | 10 |

Add a per-figure acceptance checklist identical to VVUQ-01's global criteria.

---

## 10. Paper, templates, and the future execution record

- `templates/Template_11/` - LaTeX scaffold (`main.tex`, section `\input`s, `new_paper.sty`, `references.bib`). Carry the PDAC BibTeX set plus VVUQ-01's citation, plus an ISO 13482 / IEC 80601-2-77 / FDA SaMD anchor set. Validate `\input` resolution statically (do not require a TeX toolchain), exactly as VVUQ-01 notes.
- `execution/` (future run, not now) - mirror VVUQ-01's numbered sections: `01-foundation` (env, pytest, ruff, yamllint), `02-pipeline` (intent→compile→act→score), `03-vvuq` (the 10-gate decision surface, with verbatim ACCEPT/BLOCK/ESCALATE captures for each gate), `04-automation` (sweep, chunk losslessness, scheduler), `05-humanoid-deployment` (the 60 s Whipple run + balance/collision/fault safety surface). Each section is its own commit; honest limitations + "this run vs conventional server" section required.

---

## 11. Single-PR commit plan (11 commits, mirrors PDAC's 9 + the two-extra-gate complexity)

| Commit | Focus | Emits |
|--------|-------|-------|
| 1 | Skeleton + docs | README, LICENSE, pyproject, docker-compose, lint configs, `config/project.yaml` |
| 2 | Platform + kinematics | `h2_kinematics.yaml`, `hand_model.yaml`, `balance_model.yaml`, schemas |
| 3 | Sensors + perception | `perception_model.yaml`, `src/perception/`, sensor schema/sample |
| 4 | Autonomy (thesis core) | `src/autonomy/`, `prompts/autonomy_intent_prompt.md`, command schema |
| 5 | Hands + balance | `src/hands/`, `src/balance/` |
| 6 | Safety (06, 09, 10) | `src/safety/`, `safety_zones.yaml`, `shared_or_actors.yaml` |
| 7 | Suturing + anastomosis | `src/suturing/`, `anastomosis_targets.yaml` |
| 8 | **VVUQ harness + thresholds** | `src/vvuq/`, `config/vvuq_thresholds.yaml`, `data/reference/`, gate tests |
| 9 | Iterations + metrics + tournament + Zenodo | `src/simulation/`, `src/metrics/`, `src/llm/`, `src/zenodo/`, `results/` |
| 10 (2nd-last) | Error fixes | lint/format/cross-ref fixes; CI green across 3.10/3.11/3.12 |
| 11 (last) | Repository updates | top-level README, `releases.md`, `CHANGELOG.md`, version badge |

Each commit pushed in real time; all in one PR; agent works one commit at a time (VVUQ-01 discipline). Image-instruct figures (Section 9) are a separate downstream PR, one commit per figure, exactly as VVUQ-01 separates `image-instruct` from `imagegen`.

---

## 12. Conventions and CI (non-negotiable, inherited)

Single hyphens only; plain GFM; black text; ASCII/Mermaid for diagrams (no SVG for high-frequency series); committed files < 10 MB; Parquet < 5 MB; ruff + yamllint + markdownlint clean on 3.10/3.11/3.12; guarded optional imports so the core runs with zero heavy installs; deterministic seed contract; per-section/per-commit pushes.

---

## 13. Responsible use and regulatory framing (must appear in README and paper)

A single autonomous humanoid concentrating all surgical action into two hands is higher-risk than a teleoperated multi-arm cart. State plainly: every generated instruction, config, behavior, figure, and paper is a draft; the 10 VVUQs plus a recorded human reviewer must clear any candidate before any non-simulated use; the H2-Surgical 1.0 is hypothetical 2030 and simulation-only; deployment would require IEC 80601-2-77, IEC 60601, ISO 13482, FDA SaMD Class III clearance, IRB approval, and regulatory authorization. The autonomy ("all on their own") path is gated by VVUQ 04 and VVUQ 10 and must default to hand-back-to-human on any ESCALATE.

---

## 14. Grounding citations (cite inline with relative paths, as both source repos do)

- VVUQ-01 framework: `cancer-automated/papers/VVUQ-01/execution/README.md`, `execution/03-vvuq/README.md` (the V/V/UQ gate and the 6-case decision surface), `image-instruct/README.md` (figure conventions), `configs/vvuq_thresholds.yaml`.
- PDAC surgical context: `robotic-surgeries/2030-pdac-1min/paper/instructions/README.md` (8-phase 60 s timeline), `robot_specification_pancrespeed.md`, `sensor_specification_100khz.md`, `multi_arm_coordination_8arm.md`, `vascular_safety_protocol.md`, `anastomosis_protocols.md`, and `codegen/README.md` (9-commit tree pattern).

---

That is the complete VVUQ-02 instruction set: thesis, the hypothetical H2-Surgical platform, the 10 humanoid-specific VVUQs with exact V/V/UQ thresholds, the codegen target tree, behavior-level (no-source) codegen instructions module by module, the `vvuq_thresholds.yaml` contract, the 10-figure image-instruct set, the paper/execution scaffolding, the 11-commit single-PR plan, CI/convention rules, and grounding citations. As requested, no code was generated and nothing was committed. 

Two things worth flagging before any future build: (1) I framed the surgical robot as a clearly-labeled **hypothetical 2030 Unitree H2-Surgical variant** to stay honest about what the real H2 can do today, exactly as the PDAC paper does with PancreSpeed 1.0 - if you'd rather I anchor to specific published H2 hardware numbers instead, point me at the source. (2) I reused the PDAC patient and 60 s Whipple so VVUQ-02 is directly comparable to the 8-arm baseline; if you want a different procedure or a fully autonomous-from-scratch scenario, that mainly changes Sections 2-4. Want me to expand any single VVUQ (e.g., #4 autonomy or #3 balance) into its full per-block spec next?
