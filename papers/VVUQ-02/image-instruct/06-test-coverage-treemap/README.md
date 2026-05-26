# Image Instruction 06: 172-Test Coverage Treemap

Chart family: treemap (deterministic slice-and-dice, area exactly proportional to
test count). Basis: code execution (v0.8.0 execution §01
`01-foundation/test-suite.md`). Required data R1: include the 172 tests in a
figure. Output: a single portrait, full page, 300 dpi PNG whose tile areas encode
the 172 tests across the 15 test modules, grouped into three subsystems, with the
64-test gate suite as the dominant tile.

This instruction is self contained. Read the shared conventions in
`papers/VVUQ-02/image-instruct/README.md` for the page frame, palette, fonts,
symbols, and dash rules, then build exactly what is specified below.

## Purpose and message

The test budget is itself evidence for the thesis: the assurance harness carries
more of the test budget than the control code it judges. The treemap shows all
172 tests at once, with `test_vvuq_gates.py` (64 tests, the 10-gate decision
surface) as by far the largest tile, and the assurance subsystem (76 of 172, more
than a third) as the largest group.

## Grounding (cite in the footer)

Source, used for every tile below:

- `papers/VVUQ-02/execution/01-foundation/test-suite.md`, the per-module breakdown
  table (172 tests across 15 modules) and the note that
  `test_vvuq_gates.py` carries 64 of the 172.

## The treemap data (exact, 15 modules, 3 subsystems)

Subsystems (the three color groups) and their modules with test counts:

| Subsystem | Color | Module (tests) |
|-----------|-------|----------------|
| Assurance harness | navy `#1F3A5F` | test_vvuq_gates.py (64); test_vvuq_framework.py (9); test_standards_corpus.py (3) |
| Behavior models | teal `#2A9D8F` | test_safety.py (12); test_suturing.py (11); test_hands.py (11); test_kinematics.py (9); test_perception.py (8); test_balance.py (8); test_autonomy.py (8); test_sensors.py (7) |
| Integration and harness | slate blue `#4C72B0` | test_llm.py (7); test_simulation.py (6); test_metrics.py (5); test_zenodo.py (4) |

Subsystem totals: assurance 76, behavior models 74, integration 22. Grand total
76 + 74 + 22 = 172. Each module subject (one line) for the tile subtitle:

- test_vvuq_gates.py: the 10-gate registry, thresholds, decision surface
- test_safety.py: estop, human-collision FSM, vessel no-fly
- test_suturing.py: bimanual suture, ring tension, RMSE
- test_hands.py: fingertip force, bimanual caps, grasp, handover
- test_vvuq_framework.py: verify, validate, uncertainty, composition
- test_kinematics.py: DH forward kinematics, joint-limit clamp
- test_perception.py: segmentation, Dice, NIR/US/bile fusion
- test_balance.py: ZMP, support-polygon margin, recovery
- test_autonomy.py: LLM intent, deterministic compile, concordance
- test_sensors.py: per-tick per-hand sensor record synthesis
- test_llm.py: the 4-entrant tournament agent and caveats
- test_simulation.py: the 32-iteration Latin hypercube sweep
- test_metrics.py: the 6-component composite and gating overlay
- test_zenodo.py: L0 pointer JSON and cross-iteration manifest
- test_standards_corpus.py: the wired external-standards binding

## Layout specification (portrait, full page)

Use the shared page frame. Build the content with a single full width axis in the
content band (`GridSpec` 1 by 1, `left=0.06, right=0.94, top=0.90, bottom=0.08`),
drawn in axis coordinates `0..1`, axis off.

- Header at `y = 0.965`: `172-Test Coverage Treemap`. Subtitle at `y = 0.935`:
  `15 modules, 3 subsystems; the 10-gate suite carries 64 of 172 (execution §01)`.
- Treemap construction (deterministic slice-and-dice so tile area equals
  count / 172 of the content rectangle):
  1. Split the content rectangle into three columns whose widths are proportional
     to the subsystem totals (76, 74, 22), in the order assurance, behavior,
     integration left to right.
  2. Within each column, stack the module tiles top to bottom with heights
     proportional to each module count divided by the subsystem total, sorted
     descending by count.
  3. With this construction each tile area equals (subsystem_total / 172) times
     (count / subsystem_total) which is count / 172 of the content area, so areas
     are exactly proportional to test counts across the whole figure.
- Tiles: fill each module tile with its subsystem color; within a subsystem, vary
  lightness slightly by rank (darkest for the largest module) so adjacent tiles
  separate. Outline each tile in white at 1.5 pt. Place the module name in bold and
  the count in larger bold inside each tile, with the one-line subject in 8 pt
  where the tile is tall enough; for the small tiles (counts 3 to 6) place only
  `name (count)` and move the subject to a 7.5 pt leader outside the tile if it
  would not fit.
- The dominant tile (`test_vvuq_gates.py`, 64) gets a 13 pt count and a thin
  accept-green inner keyline to mark it as the assurance centerpiece.
- Subsystem headers: above each column, a 11 pt bold label `Assurance harness 76`,
  `Behavior models 74`, `Integration and harness 22`.
- Annotation: a 10 pt italic note in a clear corner, `Assurance carries 76 of 172
  tests, more than a third in the single gate suite alone`.
- Legend at the bottom: three swatches keyed to the subsystem colors with their
  totals, 9 pt.

## Color, symbol, and dash rules

- Three subsystem colors with slight per-tile lightness steps, white tile borders,
  accept-green keyline on the dominant gate tile. White figure background, near
  black text, white text on the dark navy tiles. No dark mode and no rainbow.
- Use `§` in the subtitle (`execution §01`).
- Single hyphens only. Write counts as integers and any range with the word `to`.

## matplotlib implementation directives

- `matplotlib.use("Agg")`; import `matplotlib.pyplot as plt`, `numpy as np`, and
  from `matplotlib.patches` import `Rectangle`.
- Encode the data as a list of subsystems, each with color and a list of (module,
  count, subject); compute column widths and tile heights from the counts as
  described, so the layout is fully derived and reconciles to 172.
- Derive per-tile lightness with a simple blend toward white by rank index; keep
  the largest tile fully saturated.
- Use `ax.add_patch(Rectangle(...))` and `ax.text(...)`; set `ax.set_xlim(0, 1)`,
  `ax.set_ylim(0, 1)`, `ax.axis("off")`.
- Save with `fig.savefig("papers/VVUQ-02/imagegen/06-test-coverage-treemap/06-test-coverage-treemap.png",
  dpi=300, facecolor="white")`. Do not use `bbox_inches="tight"`.

## Output paths

- Script: `papers/VVUQ-02/imagegen/06-test-coverage-treemap/06-test-coverage-treemap.py`.
- Image: `papers/VVUQ-02/imagegen/06-test-coverage-treemap/06-test-coverage-treemap.png`.

## Footer text

`cancer-automated v0.9.0  |  source: execution §01 test-suite.md  |  white background, 300 dpi, portrait`

## Per figure acceptance checklist

- Portrait, full page, `figsize=(8.5, 11)`, saved at 300 dpi, white background.
- All 15 module tiles present, areas proportional to counts, the counts summing to
  172; the 64-test gate tile is clearly the largest.
- Three subsystem columns with totals 76, 74, 22; subsystem headers and the
  assurance-share annotation present.
- Tile labels and counts legible, small-tile subjects not clipped, legend present.
- Header, subtitle, legend, and footer inside their bands, no overlap, none
  clipped.
- The section symbol renders as `§`; only single hyphens in visible text; no dark
  mode.
- Script is self contained, uses only matplotlib and numpy, and passes
  `ruff check` and `ruff format --check`.
