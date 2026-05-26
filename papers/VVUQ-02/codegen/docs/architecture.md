# Architecture: Autonomous H2-Surgical 1.0 Whipple Under 10 VVUQ Gates

## Thesis

An on-premises, repository-based LLM issues high-level intents to a single
autonomous humanoid surgeon that senses in real time and acts through its own two
hands via x/y/z tip and per-finger joint targets. Because one humanoid
concentrates all error potential into one body, the VVUQ assurance layer must be
more substantial, stricter, and more thoroughly exercised than the humanoid's
control code, and it must clear 10 distinct humanoid-specific gates before any
candidate behavior is allowed to ship.

## Data and control flow

```
  inputs/standards/        on-prem LLM            deterministic policy
  (real corpus)            (guarded, offline      compiler
        |                   fallback to plan)            |
        v                        |                       v
  config/*.yaml  --->  src/autonomy/llm_intent  --->  src/autonomy/plan_compiler
  (frozen scope)         phase-level intents          x/y/z tip + per-finger
        |                                              joint targets (commands)
        |                                                     |
        |                                                     v
        |                            +--------------------------------------------+
        |                            | per-tick humanoid execution (simulated)    |
        |                            | src/sensors  src/perception  src/hands     |
        |                            | src/balance  src/safety  src/suturing      |
        |                            +--------------------------------------------+
        |                                                     |
        |                                       per-tick sensor records + outcomes
        v                                                     v
  src/simulation/iterate (32-iter Latin hypercube, seed 20260525)
        |
        v
  +---------------------------------------------------------------+
  | src/vvuq  (the 10-gate harness, the centerpiece)              |
  |   verification.py  validation.py  uncertainty.py              |
  |   vvuq_gate.py     gate_registry.py                           |
  |   reference truth: data/reference/*                           |
  +---------------------------------------------------------------+
        |
        +--> all 10 ACCEPT --> src/metrics/compute (composite reported)
        +--> any BLOCK or ESCALATE --> composite withheld; report shows reason
        |
        v
  results/vvuq_decisions.json   results/vvuq_report.md
  src/llm/compare_agent (4-entrant tournament)   src/zenodo (L0 pointers)
```

## Package responsibilities

| Package | Responsibility | Gates served |
|---------|----------------|--------------|
| `src/kinematics` | forward kinematics for the 2 x 7-DOF arms and finger chains | 01 |
| `src/sensors` | per-tick humanoid sensor record ingest (fingers, balance, perception) | 08 |
| `src/perception` | segmentation and NIR/US fusion of the surgical scene | 08 |
| `src/autonomy` | on-prem LLM intents and the deterministic plan compiler | 04 |
| `src/hands` | per-finger force control, grasp, instrument handover | 02, 05 |
| `src/balance` | ZMP margin and posture control while exerting reaction forces | 03 |
| `src/safety` | vessel no-fly gate, human-collision FSM, unified e-stop monitor | 06, 09, 10 |
| `src/suturing` | bimanual suturing and ring-tension control | 07 |
| `src/vvuq` | the 10-gate verify/validate/quantify harness | all |
| `src/simulation` | 32-iteration deterministic sweep | all |
| `src/metrics` | 6-component composite with the 10-gate gating overlay | all |
| `src/llm` | 4-entrant comparison tournament | all |
| `src/zenodo` | L0 raw pointer and SHA-256 manifest | all |

## Hypothetical-platform rule

The Unitree H2 is a real bipedal humanoid lineage. A surgical H2 does not exist.
This tree defines a clearly labeled "Unitree H2-Surgical 1.0 (hypothetical 2030
surgical variant)". The base form factor traces to the real H2 lineage; every
clinical-grade uplift (sub-0.1 mm fingertip accuracy, 100 kHz fingertip force,
3 ms e-stop) is explicitly flagged hypothetical 2030 and is paper-only. Every
comparison against the 8-arm PancreSpeed 1.0 or against human surgeons is flagged
simulation-against-simulation.

## Decisive difference from the 8-arm baseline

A fixed coelomic arm cannot fall over; a standing humanoid can. Fingers can drop
a needle. Balance and dexterity are now safety-critical. These differences
motivate gates 01, 02, 03, 05, and 09.
