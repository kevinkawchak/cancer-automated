# VVUQ-02: 10 Mobile Pancreatic Cancer Surgical Unitree H2 Humanoid VVUQs (v0.1.0)

Released on 26 May 2026
CEO Kevin Kawchak, ChemicalQDevice

[![Release](https://img.shields.io/badge/Release-v0.7.0-brightgreen.svg)](../../../releases.md)
[![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.xxxxxxxx-blue)](https://doi.org/10.5281/zenodo.xxxxxxxx)
[![Standard](https://img.shields.io/badge/Standard-ASME%20V%26V%2040--2018-orange.svg)](https://www.asme.org/codes-standards/find-codes-standards/v-v-40-assessing-credibility-computational-modeling-verification-validation-application-medical-devices)
[![Platform](https://img.shields.io/badge/Platform-H2--Surgical%201.0%20(hypothetical%202030)-purple.svg)](docs/h2_robot_specification.md)
[![Gates](https://img.shields.io/badge/VVUQ%20Gates-10-red.svg)](docs/vvuq_gate_spec.md)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE.txt)
[![Python](https://img.shields.io/badge/Python-3.10%2F3.11%2F3.12-3776ab.svg)](pyproject.toml)

This directory contains the v0.1.0 generated codebase produced by Claude Code
Opus 4.7 1M Max from the instruction set at
`papers/VVUQ-02/instructions/output-instruct.md`. The simulation models a
60-second pancreaticoduodenectomy (Whipple procedure) performed by a single
autonomous humanoid surgeon, the hypothetical 2030 Unitree H2-Surgical 1.0, with
its own two dexterous hands at mixed 100 kHz fingertip force plus 10 kHz command
resolution. The deliverable is 10 humanoid-specific VVUQ gates, each a fully
specified verify / validate / quantify gate grounded in real-world standards,
plus the codegen to execute and document them. Everything is generated under a
single pull request across 11 sequential commits.

## Lineage (this version of the repository)

This codegen tree is the third artifact in a documented lineage:

1. `papers/VVUQ-02/instructions/prompt-instruct.md` is the prior instruction
   prompt.
2. `papers/VVUQ-02/instructions/output-instruct.md` is the Claude Code Opus 4.7
   1M Max output produced from that prompt; it is a specification only and
   contains zero source code.
3. This `codegen/` tree is the Claude Code Opus 4.7 1M Max output produced from
   `output-instruct.md`, with `prompt-codegen.md` and `output-codegen.md` in this
   directory recording the prompt and the narrative output of the generation
   step.

## Thesis

The robotic code assurance process, not code generation, is the substantial and
decision-bearing part of the AI workflow, holding VVUQ to a higher standard than
code itself. Because one humanoid concentrates all error potential into one body
(no second cart, no human bedside assistant in the loop), the VVUQ assurance
layer must be more substantial, stricter, and more thoroughly exercised than the
humanoid's control code, and it must clear 10 distinct humanoid-specific gates
before any candidate behavior is allowed to ship. These safety measures are built
against external standards already used in real life so the assurance argument is
defensible to a regulator and so upcoming physical AI oncology trial deliverables
are faster, less expensive, and more beneficial to patients than conventional
verifications.

## External standards (used in real life)

| Domain | Standard |
|--------|----------|
| Model credibility | ASME V&V 40-2018, ASME V&V 10, ASME V&V 20, NASA-STD-7009A, FDA CM&S Credibility 2023 |
| Robotic surgery | IEC 80601-2-77:2019, IEC 60601-1 |
| Service-robot safety | ISO 13482:2014, ISO 10218-1, ISO/TS 15066:2016, ISO 9283 |
| Software and risk | IEC 62304, ISO 14971:2019, ISO 13849-1 |
| Autonomy | UL 4600, IEEE 7009-2024 |

See `docs/vvuq_methodology.md` and `docs/standards_map.md` for the binding from
each gate to its governing standards.

## The 10 VVUQ gates

```
  candidate humanoid behaviors
        |
   +----v-------------------------------------------------------+
   | 01 bimanual-handeye-servo        06 vascular-no-fly-hand *  |
   | 02 dexterous-finger-force        07 bimanual-suturing       |
   | 03 whole-body-balance            08 perception-scene        |
   | 04 autonomous-plan-correctness   09 shared-or-collision *   |
   | 05 instrument-grasp-handover     10 fault-estop-degrade *   |
   +----v-------------------------------------------------------+
        |  each gate: Verify (== 1.0) -> Validate (>= agreement,
        |             independent reference) -> Quantify (cv bound)
        v
   ACCEPT (all 10 pass)  /  BLOCK (any fail)  /  ESCALATE (divergence)

  * immediate-catastrophe gates: verification fraction 1.0 and the
    tightest coefficient-of-variation bounds plus an extra hard predicate.
```

## Project scope (frozen)

- One simulated patient: PAT-PDAC-0001 (reused verbatim from the PDAC 8-arm
  baseline so the single-humanoid run is directly comparable).
- One procedure: classic pancreaticoduodenectomy with pylorus preservation, the
  60-second 8-phase Whipple timeline.
- One robot: Unitree H2-Surgical 1.0 (hypothetical 2030), 2 x 7-DOF arms, 2 x
  20-DOF dexterous hands, 71 total DOF.
- One iteration design: 32 deterministic iterations, seed 20260525, Latin
  hypercube over five free parameters.
- One competition: H2-Surgical vs the 8-arm PancreSpeed 1.0 vs a teleoperated
  da Vinci-successor vs the 2025 Dutch human-surgeon cohort.

## 11-commit plan (single pull request)

| Commit | Focus | Emits |
|--------|-------|-------|
| 1 | Skeleton and docs | README, LICENSE, pyproject, docker-compose, lint configs, `config/project.yaml`, `docs/` |
| 2 | Platform and kinematics | `h2_kinematics.yaml`, `hand_model.yaml`, `balance_model.yaml`, schemas |
| 3 | Sensors and perception | `perception_model.yaml`, `src/perception/`, sensor schema and sample |
| 4 | Autonomy (thesis core) | `src/autonomy/`, `prompts/autonomy_intent_prompt.md`, command schema |
| 5 | Hands and balance | `src/hands/`, `src/balance/` |
| 6 | Safety (06, 09, 10) | `src/safety/`, `safety_zones.yaml`, `shared_or_actors.yaml` |
| 7 | Suturing and anastomosis | `src/suturing/`, `anastomosis_targets.yaml` |
| 8 | VVUQ harness and thresholds | `src/vvuq/`, `config/vvuq_thresholds.yaml`, `data/reference/`, gate tests |
| 9 | Iterations, metrics, tournament, Zenodo | `src/simulation/`, `src/metrics/`, `src/llm/`, `src/zenodo/`, `results/` |
| 10 | Error fixes | lint and format fixes; CI green across 3.10 / 3.11 / 3.12 |
| 11 | Repository updates | top-level README, `releases.md`, `CHANGELOG.md`, version badge |

## Repository tree (generated)

```
papers/VVUQ-02/codegen/
  README.md                     # this file
  LICENSE.txt                   # MIT
  pyproject.toml                # project plus nested ruff config
  docker-compose.yml            # python + rust + duckdb + ollama
  .gitignore .yamllint .markdownlint.yaml .pre-commit-config.yaml
  prompt-codegen.md             # the generating prompt, verbatim
  output-codegen.md             # the narrative output of the generation step
  config/
    project.yaml                # frozen scope: patient, seed 20260525, 32 iters
    standards_map.yaml          # gate to standard bindings
    h2_kinematics.yaml          # 2 x 7-DOF arms; head, waist, leg chains
    hand_model.yaml             # per-finger 4-DOF, tendon coupling, caps
    balance_model.yaml          # mass, CoM, support polygon, ZMP margins
    perception_model.yaml       # camera intrinsics, NIR / US / bile channels
    autonomy_plan.yaml          # the 8-phase reference plan
    vvuq_thresholds.yaml        # the 10 VVUQ gates
    iterations.yaml             # 32-iter Latin hypercube, seed 20260525
    safety_zones.yaml           # 5 vessel no-fly volumes
    shared_or_actors.yaml       # human actor poses and keep-out volumes
    anastomosis_targets.yaml    # 3 ring-tension targets
  schemas/                      # JSON Schema + Protobuf + Avro
  src/
    kinematics/  sensors/  perception/  autonomy/  hands/  balance/
    safety/  suturing/  vvuq/  simulation/  metrics/  llm/  zenodo/
  data/
    reference/                  # INDEPENDENT validation truth per gate
    iterations/                 # sample run files, index, L0 pointer
    sample_h2_sensor.{csv,jsonl}
    human_surgeon_baseline.csv
  prompts/  results/  viz/  outputs/  notebooks/  tests/  docs/
  releases/v0.1.0/              # manifest, metrics, index, seeds
```

## Quick start

```bash
cd papers/VVUQ-02/codegen
python3.12 -m venv .venv && source .venv/bin/activate
pip install -e .[dev]
python -m src.simulation.iterate --seed 20260525 --iterations 32
python -m src.vvuq.gate_registry --iterations-dir data/iterations
python -m pytest tests -q
```

## Responsible use

A single autonomous humanoid concentrating all surgical action into two hands is
higher-risk than a teleoperated multi-arm cart. Every generated instruction,
config, behavior, figure, and paper is a draft. The 10 VVUQ gates plus a recorded
human reviewer must clear any candidate before any non-simulated use. The
H2-Surgical 1.0 is hypothetical 2030 and simulation-only. Deployment would require
IEC 80601-2-77, IEC 60601, ISO 13482, FDA SaMD Class III clearance, IRB approval,
and regulatory authorization. The autonomy path is gated by VVUQ 04 and VVUQ 10
and defaults to hand-back-to-human on any ESCALATE.

## License

Code under the MIT License (see LICENSE.txt). Generated text and diagrams under
the Creative Commons Attribution 4.0 International License (CC BY 4.0).

## See also

- `papers/VVUQ-02/instructions/output-instruct.md` for the full instruction set.
- `papers/VVUQ-01/` for the prior VVUQ framework this tree reuses.
- `robotic-surgeries/2030-pdac-1min/paper/` for the 8-arm PDAC surgical baseline.
- `../../../releases.md` and `../../../CHANGELOG.md` for the v0.7.0 release notes.
