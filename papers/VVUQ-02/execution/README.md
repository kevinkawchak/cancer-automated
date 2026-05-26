# VVUQ-02 Execution: 10 Humanoid VVUQ Gates for the Autonomous H2-Surgical Whipple

[![DOI](https://img.shields.io/badge/DOI-Zenodo%20pending-blue.svg)](../../../CITATION.cff)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](../../../LICENSE)
[![Release](https://img.shields.io/badge/Release-v0.8.0-brightgreen.svg)](../../../releases.md)
[![Executed](https://img.shields.io/badge/Executed-May%202026-blue.svg)](README.md)
[![Python](https://img.shields.io/badge/Python-3.11.15-blue.svg)](https://www.python.org/)
[![Runner](https://img.shields.io/badge/Runner-Claude%20Code%20Opus%204.7%201M%20Max-purple.svg)](https://claude.com/product/claude-code)
[![CI](https://img.shields.io/badge/lint--and--format-green-brightgreen.svg)](../../../.github/workflows/ci.yml)
[![Tests](https://img.shields.io/badge/pytest-172%20passed-brightgreen.svg)](01-foundation/test-suite.md)
[![Standard](https://img.shields.io/badge/Standard-ASME%20V%26V%2040--2018-orange.svg)](../codegen/docs/vvuq_methodology.md)
[![Gates](https://img.shields.io/badge/VVUQ%20Gates-10-red.svg)](03-vvuq/README.md)

This directory holds the complete execution record of the
`papers/VVUQ-02/codegen/` tree, the v0.1.0 generated codebase for 10 mobile
pancreatic cancer surgical Unitree H2 humanoid VVUQs. It was produced by Claude
Code Opus 4.7 (1M context) Max running autonomously in a managed ephemeral cloud
container. Every entry-point module, the 172-test suite, the static-analysis
checks, the 10-gate decision surface, the 32-iteration sweep, the 4-entrant
tournament, and the full balance, collision, and fault safety surface were
executed, and their verbatim outputs are captured in the five numbered sections.
This README is the index and the technical summary a future paper can build on.

> Note on the DOI badge. The repository has no assigned archival DOI yet. The
> badge is a labeled placeholder pointing at `CITATION.cff`. A Zenodo concept DOI
> is expected when a tagged release is archived. The L0 raw humanoid stream is
> deposited to Zenodo and never committed; the per-iteration pointer JSON carries
> the deposition DOI and a SHA-256.

## Thesis

The robotic code assurance process, not code generation, is the substantial and
decision bearing part of the AI workflow, holding VVUQ to a higher standard than
code itself. These safety measures will ensure upcoming physical AI oncology
trial deliverables are faster, less expensive, and more beneficial towards
patients than conventional verifications.

This execution is itself evidence for the thesis. The control behaviors in
Section 02 were generated and compiled deterministically in microseconds, while
Section 03 shows that turning any one of them into a shippable result requires
clearing a 1.0 verification fraction, an agreement bar up to 1.00, a
relative-error bound as tight as 0.01, a coefficient-of-variation bound as tight
as 0.05, a recorded human review, and, on the three catastrophe gates, an extra
hard predicate. The assurance harness carries 64 of the 172 unit tests, more than
a third of the budget, and an autonomous agent performed all of it cheaply and
reproducibly. Because one humanoid concentrates all error potential into two
hands, with no second cart and no human bedside assistant in the loop, the
assurance layer must be larger and stricter than the control code, which is
exactly what the record shows.

## What VVUQ-02 codegen is

The codegen tree models a 60-second pancreaticoduodenectomy (Whipple) performed
by a single autonomous humanoid surgeon, the hypothetical 2030 Unitree
H2-Surgical 1.0 (2 x 7-DOF arms, 2 x 20-DOF dexterous hands, 71 total DOF). The
deliverable is 10 humanoid-specific VVUQ gates, each a fully specified Verify then
Validate then Quantify gate grounded in real-world standards, plus the code to
execute and document them.

### The 10 VVUQ gates (as executed)

```
  candidate humanoid behaviors (Section 02)
        |
   +----v-------------------------------------------------------+
   | 01 bimanual-handeye-servo        06 vascular-no-fly-hand *  |
   | 02 dexterous-finger-force        07 bimanual-suturing       |
   | 03 whole-body-balance            08 perception-scene        |
   | 04 autonomous-plan-correctness   09 shared-or-collision *   |
   | 05 instrument-grasp-handover     10 fault-estop-degrade *   |
   +----v-------------------------------------------------------+
        |  each gate: Verify (fraction == 1.0) -> Validate (>= agreement
        |             vs an independent reference) -> Quantify (CV bound)
        v
   ACCEPT (all 10 pass)  /  BLOCK (any fail)  /  ESCALATE (divergence)

  * immediate-catastrophe gates: 1.00 agreement, tightest CV bounds, plus an
    extra hard predicate; any ESCALATE defaults to hand-back-to-human.
```

### Execution flow of this run

```
  Section 01  Foundation        determinism, pytest (172), ruff, yamllint
      |
      v
  Section 02  Pipeline          intent -> compile -> act -> score, 6 behavior groups
      |
      v
  Section 03  VVUQ              10-gate surface, 5 cases (10 ACCEPT, 3 BLOCK, 1 ESCALATE)
      |
      v
  Section 04  Automation        32-iter sweep, metrics, 1790-line tournament, Zenodo
      |
      v
  Section 05  Humanoid deploy    60 s Whipple, 1000-row sensor stream, safety surface
      |
      v
  This README + prompt-execution.md + output-execution.md + repository updates
```

## Execution results summary

| Section | Scope | Commands run | Result |
|---------|-------|--------------|--------|
| 01 Foundation | environment, determinism, tests, lint | interpreter, 3 regenerations, pytest, ruff x2, yamllint | all reproduced, 172 passed, all clean |
| 02 Pipeline | intent to compile to act to score | 6 behavior-group driver | all behaviors ran, concordance 1.000 |
| 03 VVUQ | the 10-gate decision surface | run_all + 4 adversarial cases | 10 ACCEPT, 3 BLOCK, 1 ESCALATE, as specified |
| 04 Automation | sweep, metrics, tournament, Zenodo | iterate, compute, compare, patch | 32/32 cleared all gates, 128 verdicts, 32 pointers |
| 05 Humanoid deploy | 60 s Whipple, sensor stream, safety | timeline, sensor analysis, 3 safety gates | all safety paths correct, 1000 unique rows |

Aggregate: every codegen entry point executed (all exit 0), 172 automated tests
passed, 3 static-analysis checks clean, 5 VVUQ decision cases and the full
3-gate safety surface exercised, and 3 large artifacts reproduced exactly from
seed 20260525 (the sensor CSV byte-for-byte, the comparison and the sweep index
identically).

## File generation outcomes (basis for a future paper)

This execution generated 19 documentation and artifact files under
`papers/VVUQ-02/execution/`, plus this README, the two lineage files, and the
final repository updates. Each is mapped to the paper section it can support.

| Generated file | Bytes | Kind | Future paper role |
|----------------|-------|------|-------------------|
| 01-foundation/README.md | 2763 | index | Methods: foundation gate |
| 01-foundation/environment-and-verification.md | 4401 | report | Methods: reproducibility, determinism |
| 01-foundation/test-suite.md | 3824 | report | Verification: automated test evidence |
| 01-foundation/lint-format-yaml.md | 3292 | report | Verification: static analysis evidence |
| 02-pipeline/README.md | 6816 | report | Methods and Results: the control pipeline |
| 02-pipeline/artifacts/pipeline_execution_log.txt | 1809 | artifact | Results: captured pipeline output |
| 03-vvuq/README.md | 8813 | report | Core Results: the VVUQ decision surface |
| 03-vvuq/artifacts/gate_decision_surface.txt | 1396 | artifact | Results: ACCEPT/BLOCK/ESCALATE captures |
| 03-vvuq/artifacts/vvuq_report.md | 778 | artifact | Results: nominal all-ACCEPT report |
| 03-vvuq/artifacts/vvuq_decisions.json | 4062 | artifact | Results: per-gate scores and standards |
| 04-automation/README.md | 7205 | report | Results: integration layer |
| 04-automation/artifacts/comparison_analysis.txt | 1894 | artifact | Results: 1790-line tournament processed |
| 04-automation/artifacts/comparison_leaderboard.md | 558 | artifact | Results: 4-entrant leaderboard |
| 04-automation/artifacts/composite_scores.jsonl | 2258 | artifact | Results: gated composite per iteration |
| 04-automation/artifacts/sweep_index.jsonl | 2770 | artifact | Results: 32-iteration sweep index |
| 05-humanoid-deployment/README.md | 7953 | report | Results: deployment and safety |
| 05-humanoid-deployment/artifacts/deployment_safety_log.txt | 2428 | artifact | Results: safety-surface captures |
| 05-humanoid-deployment/artifacts/sensor_stream_analysis.txt | 2311 | artifact | Results: 1000-row stream processed |
| 05-humanoid-deployment/artifacts/eight_phase_timeline.txt | 911 | artifact | Results: 60 s Whipple timeline |

The five section reports are the structured evidence; the artifacts are the
primary captured deliverables. Together they form a Methods plus Results
skeleton: the foundation report documents reproducibility, the pipeline report
documents the generation, the VVUQ report documents the assurance (the core
result), and the automation and deployment reports document the integration and
the safety surface.

### Key quantitative results to cite

| Quantity | Value | Source section |
|----------|-------|----------------|
| Automated tests passed | 172 of 172 (0 skipped) | 01 |
| Assurance share of the test budget | 64 of 172 tests (the 10-gate suite) | 01, 03 |
| Determinism | sensor CSV byte-identical; comparison and sweep identical | 01 |
| VVUQ decision cases exercised | 5 (10 ACCEPT, 3 BLOCK paths, 1 ESCALATE) | 03 |
| Verification fraction to ship | 1.0 required (a single fail blocks) | 03 |
| Tightest gate bounds (catastrophe) | agreement 1.00, rel err 0.01, CV 0.05 | 03 |
| Sweep result | 32 of 32 iterations cleared all 10 gates | 04 |
| Composite across the sweep | min 93.417, max 93.715, mean 93.562 | 04 |
| Tournament | 4 entrants, 128 verdicts, 100% caveat coverage | 04 |
| Featured comparison.json | 1790 lines, 32 iters x 4 rounds | 04 |
| Featured sensor CSV | 1000 unique rows, 27 columns, 0 duplicates | 05 |
| Safety surface | vascular, collision, fault all correct at boundaries | 05 |

## The full process taken

This records every step, in order, so the run is reproducible and nothing is
implied to have happened that did not.

1. Surveyed the codegen tree: read the README, `pyproject.toml`, the CI workflow,
   the root `ruff.toml`, the five entry-point modules (iterate, gate_registry,
   compute, compare_agent, patch_pointers), the VVUQ primitives (verify,
   validate, quantify, evaluate), the pipeline and safety modules, the standards
   manifest, and the two featured data files. Confirmed the VVUQ-01 execution
   directory as the structural template.
2. Established the baseline on the container: confirmed CPython 3.11.15, installed
   the core packages (numpy, click, pyyaml, jsonschema) plus the lint and test
   tooling (ruff, yamllint, pytest), and ran the CI lint trio plus the 172-test
   suite. All green before any artifact was added.
3. Verified determinism: regenerated the sensor CSV, the comparison, and the
   sweep index in a scratch working directory and confirmed they match the
   committed files exactly. The codegen tree itself was left pristine throughout
   (all code was run from `/tmp` with the codegen tree on `PYTHONPATH`).
4. Section 01 Foundation: captured the environment, the determinism check, the
   test suite, and the static-analysis checks. Committed and pushed.
5. Section 02 Pipeline: ran a driver across the six behavior groups (autonomy,
   kinematics, perception, hands, balance, suturing) and captured the verbatim
   log. Committed and pushed.
6. Section 03 VVUQ: ran the 10-gate registry over the nominal references and four
   adversarial cases covering three BLOCK mechanisms and one ESCALATE. Captured
   the surface, the report, and the decisions JSON. Committed and pushed.
7. Section 04 Automation: ran the 32-iteration sweep, the metrics overlay, the
   tournament, and the Zenodo patcher, then processed the 1790-line comparison
   structurally. Committed and pushed.
8. Section 05 Humanoid deployment: ran the timeline, processed the 1000-row
   sensor stream, and exercised the three catastrophe-gate safety surfaces.
   Committed and pushed.
9. This README plus `prompt-execution.md` and `output-execution.md` (this commit).
10. Second-to-last commit: re-ran every CI check end to end and fixed any issue
    so the single pull request has no failing checks.
11. Last commit: repository updates (top-level README, `releases.md` v0.8.0,
    `CHANGELOG.md` v0.8.0, `CITATION.cff`).

Each large section was a separate commit, pushed to GitHub in real time, so the
work is incremental and the agent's working context stayed focused on one section
at a time. All commits belong to one pull request on
`kevinkawchak/cancer-automated`. No other repository was touched. The paper
template files under `papers/VVUQ-02/templates/Template_04/` were not processed,
as instructed.

## Limitations, approximations, and what could not be run

This section is deliberately complete. The thesis depends on honest VVUQ, so the
gaps are stated plainly.

- On-prem LLM backends not exercised live. anthropic, ollama, and openai are not
  installed and no API key was present, so the autonomy intent module and the
  comparison judge ran on their deterministic offline paths. This is the guarded
  CI path and the correct behavior, but the live agentic authoring and judging
  paths were not executed here.
- Live Zenodo deposition not performed. requests is not installed and no
  ZENODO_TOKEN was set, so the patcher wrote pointer JSON with zero-hash
  placeholders against an absent staging directory rather than depositing real L0
  files. The pointer and manifest logic ran fully; the network deposition did
  not.
- No physics or robotics backend. There is no mujoco, NVIDIA Isaac Sim, Isaac
  Lab, ROS 2, GPU, or display in the container. The behavior models are pure
  standard-library analytic references and ran fully, but no physics-backed or
  rendered simulation was executed. These are planning and assurance references,
  not a robot controller.
- The committed sensor sample is the first 50 ms of the timeline. At the 10 kHz
  command rate, 500 ticks is 0.05 s, so the 1000-row sample sits entirely in
  phase 1 with a single grasp state. This is the intended publication sample; the
  full 60-second stream (about 600k ticks per hand) is the Zenodo L0, by design
  not committed. The analysis in Section 05 is honest about this scope.
- Single Python version run locally. The container provides 3.11.15 only.
  Behavior on 3.10 and 3.12 is covered by the CI matrix, not a local
  multi-version run. No version-specific behavior is expected (standard library
  plus guarded imports).
- Paper templates intentionally not processed. `papers/VVUQ-02/templates/
  Template_04/` was excluded as instructed and is out of scope for this
  execution.
- The hypothetical platform is simulation-only. The H2-Surgical 1.0 is a
  hypothetical 2030 device. Every number here is a simulation result, not a
  measurement from hardware, and the comparison is simulation against simulation.

## This execution versus conventional high-end server processing

How an autonomous Claude Code Opus 4.7 1M Max run on a managed cloud container
compares with running the same codebase on a conventional high-end MacOS,
Windows, or Linux workstation or server. Honest notes follow, for future
executions on those platforms.

### Better

- Near-zero setup. The codegen is standard library plus four small packages with
  guarded optional imports, so it ran immediately. A conventional setup often
  begins by installing the full optional matrix (anthropic, openai, mujoco), which
  is slow and can fail on transitive or platform constraints. Here the guarded
  design meant everything core ran before any heavy install.
- One integrated loop. Reading code, running it, processing the two large
  artifacts, writing documentation, re-running lint, committing, and pushing all
  happened in a single agent loop with no context switch between terminal, editor,
  and git client. This is the cost half of the thesis: faster and cheaper than a
  human cycling those tools.
- Assurance breadth beyond the shipped tests. The agent ran the full
  ACCEPT/BLOCK/ESCALATE surface and the full safety surface, and processed the
  1790-line comparison and the 1000-row stream structurally (caveat coverage, row
  uniqueness, channel ranges), which the unit tests do not do by themselves.
- Self-verifying record. Every command and its verbatim output is captured, so a
  reader can reproduce and check each claim rather than trust a summary.

### Different

- Ephemeral and commit-driven. The container is reclaimed after the session, so
  nothing persists unless committed and pushed. This enforced the
  commit-per-section discipline and a clean scratch-versus-tree separation (all
  code ran from `/tmp`, leaving the codegen tree pristine). A workstation keeps
  state across days, more forgiving but less reproducible.
- Real-time per-section commits. The agent pushed each section as it finished, a
  finer granularity than a human typically uses, making the pull request a clean
  section-by-section narrative.
- Cross-version testing delegated. Local runs use one Python; the CI matrix
  carries 3.10, 3.11, and 3.12. A conventional setup might use pyenv or conda to
  cover all three locally.

### Worse

- No live heavy backends. A conventional server with GPUs and API keys could
  exercise the live on-prem LLM intent and judging, real Zenodo deposition, and
  mujoco or Isaac physics. None of those live paths ran here; only the
  deterministic and guarded paths did.
- No display or GPU. Rendered or accelerated workloads (Isaac Sim, any
  visualization) are out of reach in this container. A workstation handles those
  directly.
- No persistent caches. Each session starts cold, so repeated heavy work cannot
  reuse a warm cache the way a long-lived server can.

Net: for executing, verifying, and documenting a standard-library assurance
codebase under strict VVUQ, the autonomous cloud run was faster and cheaper and
produced a more reproducible record. For exercising live model, network, and
physics backends, a conventional provisioned server would do more.

## Repository structure (execution outputs)

```
papers/VVUQ-02/execution/
+-- README.md                         (this file: index and technical summary)
+-- prompt-execution.md               (the generating prompt, verbatim)
+-- output-execution.md               (the narrative output of this execution)
+-- 01-foundation/
|   +-- README.md
|   +-- environment-and-verification.md
|   +-- test-suite.md
|   +-- lint-format-yaml.md
+-- 02-pipeline/
|   +-- README.md
|   +-- artifacts/
|       +-- pipeline_execution_log.txt
+-- 03-vvuq/
|   +-- README.md
|   +-- artifacts/
|       +-- gate_decision_surface.txt
|       +-- vvuq_report.md
|       +-- vvuq_decisions.json
+-- 04-automation/
|   +-- README.md
|   +-- artifacts/
|       +-- sweep_index.jsonl
|       +-- composite_scores.jsonl
|       +-- comparison_leaderboard.md
|       +-- comparison_analysis.txt
+-- 05-humanoid-deployment/
    +-- README.md
    +-- artifacts/
        +-- deployment_safety_log.txt
        +-- sensor_stream_analysis.txt
        +-- eight_phase_timeline.txt
```

## Source executed (v0.1.0 platform)

| Package | Modules | Section |
|---------|---------|---------|
| autonomy/ | llm_intent, plan_compiler | 02 |
| kinematics/ | forward_kinematics | 02 |
| perception/ | segment, fuse_nir_us | 02 |
| hands/ | finger_force, grasp, handover | 02 |
| balance/ | zmp, posture_controller | 02 |
| suturing/ | bimanual_suture, ring_tension | 02 |
| vvuq/ | verification, validation, uncertainty, vvuq_gate, gate_registry | 03 |
| simulation/ | iterate | 04 |
| metrics/ | compute | 04 |
| llm/ | compare_agent | 04 |
| zenodo/ | patch_pointers | 04 |
| sensors/ | ingest_h2 | 01, 05 |
| safety/ | estop, human_collision, vessel_gate | 05 |
| tests/ | 15 test modules, 172 tests | 01 |

## External standards (the credibility basis)

The assurance layer is built against published consensus standards already used
in real life, and that grounding is what gives the study its credibility. The
gate registry resolves each gate's standards at runtime from
`papers/VVUQ-02/inputs/standards/manifest.yaml`, so every decision is traceable to
a published designation rather than an ad hoc threshold. A reviewer or regulator
can follow each gate to its governing standard, which is precisely what makes the
argument defensible and what lets this inexpensive autonomous run stand as
evidence for a future physical AI oncology trial.

| Domain | Standards exercised in this execution |
|--------|---------------------------------------|
| Model credibility | ASME V&V 40-2018, NASA-STD-7009A, FDA CM&S Credibility 2023 |
| Robotic surgery | IEC 80601-2-77:2019, IEC 60601-1 |
| Service-robot safety | ISO 13482:2014, ISO 10218-1:2011, ISO/TS 15066:2016, ISO 9283:1998 |
| Software and risk | IEC 62304, ISO 14971:2019, ISO 13849-1:2023 |
| Autonomy | UL 4600 (2023), IEEE Std 7009-2024 |

## Reproduction

```bash
git clone https://github.com/kevinkawchak/cancer-automated.git
cd cancer-automated/papers/VVUQ-02/codegen
python3 -m venv .venv && source .venv/bin/activate
pip install -e .[dev]
python -m pytest tests -q
ruff check . && ruff format --check .
# then reproduce the execution from seed 20260525:
python -m src.sensors.ingest_h2          # the 1000-row sensor CSV
python -m src.simulation.iterate --seed 20260525 --iterations 32
python -m src.metrics.compute
python -m src.vvuq.gate_registry         # the nominal all-ACCEPT surface
python -m src.llm.compare_agent          # the 1790-line comparison
python -m src.zenodo.patch_pointers
```

## Responsible use

A single autonomous humanoid concentrating all surgical action into two hands is
higher-risk than a teleoperated multi-arm cart. Every generated config, behavior,
figure, and document is a draft. The 10 VVUQ gates plus a recorded human reviewer
must clear any candidate before any non-simulated use. The H2-Surgical 1.0 is
hypothetical 2030 and simulation-only. Deployment would require IEC 80601-2-77,
IEC 60601, ISO 13482, FDA SaMD Class III clearance, IRB approval, and regulatory
authorization. The autonomy path is gated by VVUQ 04 and VVUQ 10 and defaults to
hand-back-to-human on any ESCALATE.

## Citation

See `CITATION.cff` at the repository root. If you use this execution record, cite
the cancer-automated repository at version 0.8.0.
