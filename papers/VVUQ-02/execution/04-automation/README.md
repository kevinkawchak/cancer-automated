# Section 04: Automation (32-iteration sweep, metrics, tournament, Zenodo)

This section runs the integration layer: a 32-iteration deterministic Latin
hypercube sweep that drives every humanoid behavior through all 10 gates per
iteration, the 6-component composite with the gating overlay, the 4-entrant
comparison tournament, and the Zenodo L0 deposition discipline. It features the
two large generated artifacts the codegen step produced and that this execution
reproduced: the 1790-line four-competitor `comparison.json` and (cross-referenced
from Section 05) the 1000-row positional sensor stream.

## Contents

| File | What it records |
|------|-----------------|
| artifacts/sweep_index.jsonl | The 32-iteration sweep index (id, seed, gates_all_accepted, composite) |
| artifacts/composite_scores.jsonl | The gated composite per iteration |
| artifacts/comparison_leaderboard.md | The 4-entrant tournament leaderboard report |
| artifacts/comparison_analysis.txt | Structural analysis of the 1790-line comparison.json |

## 1. The 32-iteration Latin hypercube sweep

```bash
python -m src.simulation.iterate --seed 20260525 --iterations 32
```

```
ran 32 iterations on seed 20260525: 32 cleared all 10 gates
```

Each iteration samples five free parameters (fingertip placement noise, finger
force noise, balance disturbance amplitude, perception occlusion fraction, ring
tension drift) on a deterministic Latin hypercube, builds the per-gate observed
metrics, runs all 10 gates, and applies the composite gating overlay. The
designed parameter ranges stay inside the gate tolerances, so a well-designed
humanoid clears all 10 gates on every iteration. The regenerated
`sweep_index.jsonl` is byte-for-byte identical to the committed
`data/iterations/index.jsonl`, confirming the sweep is deterministic from the
seed.

Composite distribution across the 32 iterations: min 93.417, max 93.715, mean
93.562. The composite is reported only because every gate ACCEPTs; on any BLOCK
or ESCALATE the gating overlay withholds the headline number, which is the
thesis made mechanical (the score is conditional on the assurance verdict).

## 2. Metrics: the gating overlay

```bash
python -m src.metrics.compute
```

```
wrote 32 gated composite records to outputs/metrics/composite_scores.jsonl
```

The 6-component composite reuses the frozen PDAC weights (Quality 0.30, Time
0.20, Cost 0.15, Safety 0.15, Patient experience 0.05, Anastomosis quality 0.15).
The overlay sets the composite to null whenever any gate is not ACCEPT, so the
assurance layer is decisive over the score.

## 3. The featured 1790-line, four-entrant comparison.json

This is one of the two substantial generated files the prompt asks to feature.
The codegen step generated it and this execution both reproduced it (identical to
the committed file) and processed it structurally. The full structural analysis
is in `artifacts/comparison_analysis.txt`.

```bash
python -m src.llm.compare_agent      # reproduces results/comparison.json
```

Structure: 32 iterations, 4 rounds each, so 128 round verdicts in 1790 lines,
plus a 4-entrant leaderboard. The on-prem LLM judge backend is guarded
(anthropic, ollama, openai) and ran on the deterministic offline stub, the honest
CI path.

### Leaderboard (frozen-weight composite)

| Rank | Entrant | Composite mean | Win rate | Total wins |
|------|---------|----------------|----------|------------|
| 1 | PancreSpeed_1_0 (8-arm cart) | 93.782 | 0.875 | 56 |
| 2 | H2_Surgical_1_0 (humanoid) | 93.334 | 0.75 | 72 |
| 3 | da_Vinci_successor_2030 (teleop) | 83.970 | 0.0 | 0 |
| 4 | Dutch_human_baseline (2025 cohort) | 67.885 | 0.0 | 0 |

A subtlety the processing surfaces: the humanoid has more total wins (72) than
the leader (56) because it appears in three of the four rounds while the 8-arm
cart appears in two; win rate normalizes for appearances, so the cart leads on
rate (0.875) and composite mean. The autonomous single-humanoid result lands
within about half a composite point of the multi-arm cart, which is the headline
the comparison is built to support, with caveats.

### Per-round aggregate winner over 32 iterations

```
  round 1: H2_Surgical vs PancreSpeed   -> PancreSpeed 24/32
  round 2: H2_Surgical vs da_Vinci      -> H2_Surgical 32/32
  round 3: H2_Surgical vs Dutch human   -> H2_Surgical 32/32
  round 4: PancreSpeed vs da_Vinci      -> PancreSpeed 32/32
```

### Caveat coverage (the integrity check)

```
  robot-involving rounds: 128; carrying sim-vs-sim caveat: 128 (100%)
  round-3 human-vs-robot rounds carrying the time-dimension caveat: 32 (all)
```

Every one of the 128 robot-involving verdicts carries the simulation-against-
simulation caveat, and every round-3 human-versus-robot verdict carries the
structural time-dimension caveat (a 1-minute robot run against a multi-hour human
baseline, where the time component dominates the delta). This honesty discipline
is built into the generator and verified here on all 128 verdicts; it is what
keeps an impressive-looking leaderboard from overclaiming.

## 4. Zenodo L0 deposition discipline

```bash
python -m src.zenodo.patch_pointers
```

```
wrote 32 pointers plus manifest releases/v0.1.0/manifest.json
```

The 71-DOF humanoid L0 raw stream is larger than the 8-arm baseline, so the
Zenodo discipline matters more: L0 raw is never committed to git. The patcher
writes one pointer JSON per iteration (deposition DOI plus a SHA-256 of the local
staging file, or a zero hash when staging is absent) and a cross-iteration
manifest. This keeps the repository small while preserving an archival,
content-addressed pointer to the heavy data, the reproducibility-archival
property NASA-STD-7009A expects.

## Automation flow (as executed)

```
  seed 20260525
        |
        v
  +----------------------------+      +----------------------------+
  | iterate: 32-iter LHS        | ---> | metrics: gated composite   |
  | all 10 gates per iteration  |      | null unless all 10 ACCEPT  |
  | 32/32 cleared all gates     |      | 32 records written         |
  +----------------------------+      +----------------------------+
        |                                          |
        v                                          v
  +----------------------------+      +----------------------------+
  | compare: 4-entrant, 128     |      | zenodo: 32 L0 pointers     |
  | verdicts, 100% caveat cover |      | + manifest; L0 never        |
  | 1790-line comparison.json   |      | committed                   |
  +----------------------------+      +----------------------------+
```

## External standards anchored here

The sweep and tournament are model and simulation results, so they sit squarely
under NASA-STD-7009A (uncertainty and reproducibility as first-class credibility
factors) and ASME V&V 40-2018 (credibility proportional to risk). The 100 percent
caveat coverage and the gating overlay are the mechanisms that keep the
quantitative claims honest. Grounding the integration layer in these external
standards is what lets the comparison stand as credible evidence rather than a
marketing number, which is essential for the comparison to inform a future
physical AI oncology trial.
