## output-codegen

This file records the narrative output of the Claude Code Opus 4.7 1M Max
generation step that produced this `codegen/` tree from
`papers/VVUQ-02/instructions/output-instruct.md`. It is the markdown output of the
run, not the code files themselves. The generating prompt is in
`prompt-codegen.md`. The prior lineage is the instruction prompt at
`papers/VVUQ-02/instructions/prompt-instruct.md` and the prior Claude Code Opus
4.7 1M Max output at `papers/VVUQ-02/instructions/output-instruct.md`.

## Approach

I read the full instruction set, then grounded the build in two existing bodies
of work without modifying them: the VVUQ-01 framework (the V/V/UQ gate, the
strict ACCEPT/BLOCK/ESCALATE decision surface, the per-commit single-PR
discipline) and the PDAC 8-arm surgical context (the 60-second 8-phase Whipple,
patient PAT-PDAC-0001, the 5 vessel safety zones, the 3 anastomosis targets, the
640-channel sensor pattern, the codegen tree layout). I confirmed that a nested
`pyproject.toml` `[tool.ruff]` block governs lint rules for this tree even when CI
runs `ruff check .` from the repository root, then authored every file locally,
ran ruff, yamllint, and pytest before each commit, and pushed each commit to the
single pull request in real time.

A key design choice is that the assurance layer is grounded in external standards
already used in real life (ASME V&V 40-2018, NASA-STD-7009A, IEC 80601-2-77, IEC
60601-1, ISO 13482, ISO/TS 15066, ISO 10218-1, ISO 9283, IEC 62304, ISO 14971,
ISO 13849-1, UL 4600, IEEE 7009), with an independent validation reference per
gate and the real standards input corpus wired into the gate registry, so patient
benefit is preserved by a defensible credibility argument rather than ad hoc
thresholds.

## Commit log (11 commits, single pull request)

1. Skeleton and docs: the codegen README with DOI badges and the gate ASCII
   diagram, MIT license, the nested ruff pyproject, docker-compose, lint configs,
   the frozen `config/project.yaml`, the methodology and standards docs, the wired
   standards input corpus, and the future-use directory placeholders.
2. Platform and kinematics: the H2-Surgical 1.0 specification and hand kinematics
   docs, the kinematics, hand, and balance configs, the JSON Schema plus Protobuf
   plus Avro schemas, and pure-stdlib forward kinematics with tests.
3. Sensors and perception: the humanoid sensor ingest with per-finger and balance
   channels, the segmentation and NIR/US fusion modules scored by the exact Dice
   coefficient against an independent reference, and the publication sample.
4. Autonomy (thesis core): the on-prem LLM intent path with a deterministic
   offline fallback and the seed-stable plan compiler, plus the phase-step
   concordance metric and the fail-safe default.
5. Hands and balance: finger force control under the IEC 80601-2-77 caps, grasp
   with Coulomb slip detection, the 200 ms handover, and the ZMP margin and
   posture controller above the 8 mm ISO 13482 floor.
6. Safety: the vessel no-fly gate (zero hard-stop breaches, 10 us proximity
   e-stop), the human-aware collision FSM (ISO/TS 15066 separation monitoring),
   and the unified fault monitor that hands back to the human on ambiguity.
7. Suturing and anastomosis: bimanual ring-tension control at the PJ, HJ, and GJ
   targets within the plus or minus 0.05 N band, with realized grades.
8. The 10-gate VVUQ harness (centerpiece): verification, validation, uncertainty,
   the gate decision, the registry, the threshold blocks, the standards map, the
   independent references, and the 64-item 10-gate decision-surface tests.
9. Iterations, metrics, tournament, and Zenodo: the deterministic 32-iteration
   sweep that drives the humanoid behaviors through all 10 gates, the composite
   gating overlay, the 4-entrant tournament, the Rust runner, and the L0 pointer
   discipline.
10. Error fixes and cross references: wired the standards corpus into the gate
    registry, fixed a cross-reference gap where three gate-referenced standards
    were missing from the manifest, and added the cross-reference and
    lint-verification docs. Verified ruff and yamllint clean and the suite green.
11. Repository updates: the top-level README (badge, a v0.7.0 summary above the
    prior one, a VVUQ-02 section and table of contents entry, the repository
    structure), `releases.md` (v0.7.0), `CHANGELOG.md` (v0.7.0), `CITATION.cff`,
    and this `output-codegen.md`.

## Verification at the final push

- `ruff check .` and `ruff format --check .` from the repository root: clean
  across the Python 3.10, 3.11, and 3.12 lint-and-format scope, so the three
  previously failing `lint-and-format` checks pass.
- `yamllint` on the codegen configs and the wired corpus: clean.
- `pytest tests`: 169 passing plus 3 dependency-skipped (the standards-corpus
  tests skip gracefully when PyYAML is absent, the honest CI path).
- The deterministic 32-iteration sweep (seed 20260525) clears all 10 gates on
  every iteration; the composite mean is 93.56, reported only because all gates
  ACCEPT.

## Caveats

The Unitree H2-Surgical 1.0 is a clearly labeled hypothetical 2030 surgical
variant; every value is simulation-only and paper-only, and comparisons are
simulation-against-simulation. The codegen is a draft: the 10 VVUQ gates plus a
recorded human reviewer must clear any candidate before any non-simulated use.
Only `kevinkawchak/cancer-automated` was edited.
