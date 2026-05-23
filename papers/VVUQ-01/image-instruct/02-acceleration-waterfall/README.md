# Image Instruction 02: Schedule Acceleration Waterfall

Chart family: waterfall (bridge). Basis: both code generation (v0.1.0
`pipeline/codegen_stage.py` acceleration model) and code execution (v0.2.0
execution §02, observed factor 2.5). Output: a single portrait, full page, 300
dpi PNG that bridges the conventional baseline of 30 days down to the automated
12 days, decomposed by the contribution of each of the three simulation runs.

Read the shared conventions in `papers/VVUQ-01/image-instruct/README.md` first,
then build exactly what is specified below.

## Purpose and message

The figure shows where the 2.5x acceleration comes from. The generated code
computes `automated_days = 30.0 / (1.0 + runs * 0.5)`. Each simulation run adds
0.5 to the denominator, so each run contributes a concrete, decreasing reduction
in the schedule. The waterfall turns that single formula into an auditable bridge
that a reader can add up by eye: 30 down to 20 down to 15 down to 12.

## Grounding (cite in the footer)

- `pipeline/codegen_stage.py` for the generated formula `automated_days = 30.0 /
  (1.0 + runs * 0.5)` and `pipeline/README.md` for the five established methods
  context (code generation v0.1.0).
- `papers/VVUQ-01/execution/02-pipeline/README.md` for the executed result:
  baseline 30 days, automated 12 days, acceleration factor 2.5, with 3 simulation
  runs and deterministic per topic output (code execution v0.2.0).
- `configs/pipeline_config.yaml` for `simulate_runs: 3`.

## The waterfall data (exact, derived from the model)

Evaluate the model at runs 0, 1, 2, 3 and take the differences.

| Step | Bar type | Days at end | Change | Cumulative factor |
|------|----------|-------------|--------|-------------------|
| Conventional baseline | total | 30 | start at 30 | 1.0x |
| Simulation run 1 | decrement | 20 | reduce by 10 | 1.5x |
| Simulation run 2 | decrement | 15 | reduce by 5 | 2.0x |
| Simulation run 3 | decrement | 12 | reduce by 3 | 2.5x |
| Automated schedule | total | 12 | land at 12 | 2.5x |

Headline numbers to annotate: total reduction 18 days, overall acceleration
factor 2.5x, which is a 60 percent shorter schedule.

## Layout specification (portrait, full page)

Use the shared page frame. Place the waterfall in the upper two thirds of the
content band and a small audit panel in the lower third, via `GridSpec(2, 1,
height_ratios=[2.4, 1.0], left=0.06, right=0.94, top=0.91, bottom=0.07,
hspace=0.28)`.

- Header at `y = 0.965`: `Schedule Acceleration Waterfall`. Subtitle at `y =
  0.935`: `30 baseline days to 12 automated days, a 2.5x acceleration`.
- Upper axis, the waterfall. `x` axis has five categorical positions in the
  order above. `y` axis is days from 0 to 32, gridlines in gridline gray
  `#D9DEE3` behind the bars.
  - The two total bars (baseline and automated) are full height columns from 0:
    baseline in primary navy `#1F3A5F`, automated in accept green `#2E7D32`.
  - The three decrement bars float: each starts at the previous level and drops
    by its change. Fill them teal `#2A9D8F`. Draw them as `ax.bar` with a
    computed `bottom` equal to the lower of the two levels and a height equal to
    the absolute change.
  - Connect consecutive bars with thin neutral gray `#6B7280` dashed leader lines
    at the running total, so the staircase reads as one descending bridge.
  - Label each bar above or inside it: the total bars show the day value in 12 pt
    bold (`30 days`, `12 days`); each decrement shows `-10`, `-5`, `-3` in 11 pt
    and the cumulative factor below in 9 pt (`1.5x`, `2.0x`, `2.5x`).
  - Bar category labels under the axis, 10 pt: `Baseline`, `Sim run 1`, `Sim run
    2`, `Sim run 3`, `Automated`.
  - A horizontal accept green reference line at 12 days spanning the axis, dashed,
    labeled `Automated target 12 days` at the right.
- Lower axis, the audit panel on panel fill `#F4F6F8` with a thin border. Show
  the formula `automated_days = 30.0 / (1.0 + runs * 0.5)` in a monospace 11 pt
  box, then a compact three row table of `runs, denominator, days, factor`:
  `1, 1.5, 20, 1.5x` then `2, 2.0, 15, 2.0x` then `3, 2.5, 12, 2.5x`. Right of
  the table, a bold callout: `18 days saved, 60 percent shorter, 2.5x`.
- Legend at the upper axis top right: navy `Baseline`, teal `Per run reduction`,
  accept green `Automated`.

## Color, symbol, and dash rules

- Baseline navy, reductions teal, automated accept green, connectors neutral
  gray dashed, gridlines gridline gray, panel fill behind the audit panel. White
  background, no dark mode, near black text.
- No section symbol required. Write factors as `2.5x` and the reduction with a
  single hyphen, for example `-10`. Use the word `to` for the 30 to 12 range in
  prose labels.
- Single hyphens only in visible text.

## matplotlib implementation directives

- `matplotlib.use("Agg")`; `matplotlib.pyplot as plt`, `numpy as np`.
- Derive every level from `days = [30.0 / (1.0 + r * 0.5) for r in range(4)]` so
  the bridge is computed, not hand placed; the changes are the successive
  differences.
- Use `ax.bar` with explicit `bottom` for the floating decrement bars; place
  value labels with `ax.annotate` anchored to computed bar tops so they never
  overlap the bars.
- Keep `y` limits fixed at 0 to 32 so the layout is deterministic.
- Save to `papers/VVUQ-01/imagegen/02-acceleration-waterfall/02-acceleration-waterfall.png`
  with `dpi=300, facecolor="white"`, no `bbox_inches="tight"`.

## Output paths

- Script: `papers/VVUQ-01/imagegen/02-acceleration-waterfall/02-acceleration-waterfall.py`.
- Image: `papers/VVUQ-01/imagegen/02-acceleration-waterfall/02-acceleration-waterfall.png`.

## Footer text

`cancer-automated v0.3.0  |  source: pipeline/codegen_stage.py, configs/pipeline_config.yaml, execution §02  |  white background, 300 dpi, portrait`

## Per figure acceptance checklist

- Portrait, full page, `figsize=(8.5, 11)`, saved at 300 dpi, white background.
- Bridge descends 30, 20, 15, 12 with correct -10, -5, -3 floating bars and a
  navy baseline and an accept green automated total.
- Cumulative factors 1.5x, 2.0x, 2.5x labeled and the 18 days saved callout
  present.
- Audit panel reproduces the formula and the runs table exactly.
- Header, subtitle, legend, and footer inside their bands, nothing clipped.
- Only single hyphens in visible text; no dark mode.
- Script self contained, only matplotlib and numpy, passes `ruff check` and
  `ruff format --check`.
