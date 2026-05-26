# Autonomy Policy Specification (VVUQ 04, Thesis Core)

The thesis of VVUQ-02 is that an on-premises, repository-based LLM issues
high-level intents to a single autonomous humanoid that senses in real time and
acts through its own two hands. This document specifies that stack.

## Two-layer stack

```
  on-prem LLM (guarded)            deterministic policy compiler
        |                                   |
        v                                   v
  src/autonomy/llm_intent.py  --->  src/autonomy/plan_compiler.py
  proposes phase-level intents      emits x/y/z tip + 20 finger
  (offline fallback = reference     joint targets + grasp, schema
   plan, the honest CI path)        h2_command.schema.json
```

### Layer 1: intent (LLM, guarded)

`propose_intents(phase, scene_state, backend)` tries an on-prem backend
(anthropic, ollama, or openai) selected by the `AUTONOMY_BACKEND` environment
variable. When no backend is installed or the backend declines, it emits the
frozen reference plan for the phase, tagged with the `reference` source. This is
the honest CI path: the suite runs green with zero heavy installs and the
reference plan is the deterministic stand-in for the model.

### Layer 2: compile (deterministic)

`compile_intents(intents, tick)` maps each intent to a `Command`: the tip target
passes through, the grasp selects a fixed 20-DOF finger joint target, the
orientation defaults to identity, and the velocity scale and force soft cap are
set for downstream safety gating. The compiler is pure and deterministic.

## VVUQ 04 metric: phase-step concordance

`phase_step_concordance(compiled, reference, tolerance)` is the fraction of
reference intents matched by a compiled command, where a match requires the same
phase, hand, and grasp, and a tip target within a 2 mm Euclidean tolerance. VVUQ
04 validates this concordance against the gate agreement threshold.

## Fail-safe default

Per UL 4600 and IEEE 7009-2024, any ESCALATE from VVUQ 04 or VVUQ 10 must default
to hand-back-to-human. The prompt at `prompts/autonomy_intent_prompt.md` instructs
the model to propose the hand-back-to-human intent whenever the fused confidence
for the target structure is below 0.5 or the balance margin is below the warning
threshold.
