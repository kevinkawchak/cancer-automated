# Image Instruction 03: Ten-Gate Threshold Forest Plot

Chart family: forest plot (small-multiple caterpillar forest). Basis: both code
generation (v0.7.0 `codegen/config/vvuq_thresholds.yaml`) and code execution
(v0.8.0 execution §03 threshold table). Required data R3: the 10 gates and their
thresholds must be included. Output: a single portrait, full page, 300 dpi PNG
with three side by side forest panels (validation agreement, maximum relative
error, coefficient-of-variation bound), each row one of the 10 gates, showing how
the bounds tighten toward the three immediate-catastrophe gates.

This instruction is self contained. Read the shared conventions in
`papers/VVUQ-02/image-instruct/README.md` for the page frame, palette, fonts,
symbols, and dash rules, then build exactly what is specified below.

## Purpose and message

The figure shows that the gate is not one bar; it is 10 gates whose bounds are
set in proportion to model risk. Every gate also requires a verification fraction
of exactly 1.0 (a single failed check blocks), which is stated as a band, not a
forest row, because it is identical for all 10. The three immediate-catastrophe
gates carry the strictest agreement, relative-error, and dispersion bounds, which
the forest makes visible as a rightward and tighter shift.

## Grounding (cite in the footer)

Sources, used for every value below:

- `papers/VVUQ-02/execution/03-vvuq/README.md`, table `The 10 gates and their
  thresholds (as loaded from config)`.
- `papers/VVUQ-02/codegen/config/vvuq_thresholds.yaml` (defaults and per-gate
  overrides; the hard predicates for gates 06, 09, 10).

## The threshold data (exact, all 10 gates)

Defaults (the baseline reference line in each panel): validation agreement 0.95,
maximum relative error 0.05, coefficient-of-variation bound 0.10. Verification
fraction must equal 1.0 for every gate.

| # | Gate slug | Agreement | Max rel err | CV bound | Catastrophe |
|---|-----------|-----------|-------------|----------|-------------|
| 01 | bimanual-handeye-servo | 0.97 | 0.050 | 0.08 | no |
| 02 | dexterous-finger-force | 0.95 | 0.050 | 0.10 | no |
| 03 | whole-body-balance | 0.98 | 0.030 | 0.06 | no |
| 04 | autonomous-plan-correctness | 0.95 | 0.050 | 0.10 | no |
| 05 | instrument-grasp-handover | 0.96 | 0.050 | 0.10 | no |
| 06 | vascular-no-fly-hand | 1.00 | 0.010 | 0.05 | yes |
| 07 | bimanual-suturing-anastomosis | 0.96 | 0.050 | 0.08 | no |
| 08 | perception-scene-understanding | 0.95 | 0.050 | 0.10 | no |
| 09 | shared-or-human-collision | 1.00 | 0.020 | 0.06 | yes |
| 10 | fault-estop-graceful-degradation | 1.00 | 0.020 | 0.05 | yes |

Hard predicates (annotate beside the catastrophe rows): 06
`hard_stop_violations == 0`, 09 `min_clearance_mm >= 50.0`, 10
`safe_state_success_rate == 1.0`.

## Layout specification (portrait, full page)

Use the shared page frame. Build the content with a `GridSpec(1, 3, left=0.13,
right=0.96, top=0.88, bottom=0.10, wspace=0.30)` so the three forest panels share
one y axis of 10 gate rows. Reserve the left margin region (`x < 0.13`) for the
gate row labels written once with `fig.text`, aligned to the panel row centers.

- Header at `y = 0.965`: `Ten VVUQ Gate Thresholds`. Subtitle at `y = 0.935`:
  `Bounds tighten with model risk; the three catastrophe gates are strictest
  (codegen/config/vvuq_thresholds.yaml, execution §03)`.
- Rows: gates `01` (top) to `10` (bottom) on a shared categorical y axis, evenly
  spaced. Write each row label once at the far left as `NN slug` in 9.5 pt; render
  the catastrophe rows (06, 09, 10) label in block red `#C0392B` bold.
- Panel 1, `Validation agreement (>=)`: x from 0.94 to 1.005. Draw a dashed
  neutral gray default line at 0.95 labeled `default 0.95`. For each gate, draw a
  thin connector segment from 0.95 to the gate value and a filled circle marker at
  the gate value; markers for catastrophe gates in block red, others in slate blue
  `#4C72B0`. Annotate each marker value (for example `1.00`) in 8.5 pt just right
  of the marker.
- Panel 2, `Max relative error (<=)`: x from 0.0 to 0.055, drawn so smaller is
  tighter; plot markers at each gate value with a connector from the 0.05 default
  line (dashed gray, labeled `default 0.05`). Catastrophe gates land at 0.010 and
  0.020 (clearly leftmost and tightest), block red; others at 0.030 or 0.050,
  slate blue.
- Panel 3, `CV bound (<=)`: x from 0.04 to 0.105; default dashed line at 0.10
  labeled `default 0.10`; markers and connectors as above. Catastrophe gates at
  0.05 and 0.06, block red.
- Verification band: a slim full width strip just under the subtitle (`y` about
  0.90 to 0.905 of the figure) in accept green tint with 9 pt text `All 10 gates
  also require verification fraction == 1.0 (a single failed check blocks)`.
- Catastrophe annotations: to the right of Panel 3, three short 8.5 pt notes
  keyed to rows 06, 09, 10 stating the hard predicate, each with a block red
  left tick.
- Legend at the bottom (`y` about 0.07): two markers, slate blue `standard gate`,
  block red `immediate-catastrophe gate`, plus a dashed gray sample `default
  bound`.

## Color, symbol, and dash rules

- Standard gate markers slate blue, catastrophe gate markers and labels block red,
  default lines dashed neutral gray, verification band accept green tint, panel
  backgrounds white with gridline gray vertical guides. Near black text. No dark
  mode.
- Use `§` in the subtitle (`execution §03`). Use `>=` and `<=` as written for the
  bound directions, and `==` for the verification equality.
- Single hyphens only. Write thresholds as decimals (for example `0.010`) and use
  the word `to` for any range in prose.

## matplotlib implementation directives

- `matplotlib.use("Agg")`; import `matplotlib.pyplot as plt` and `numpy as np`.
- Three axes via `GridSpec`; set a shared `ax.set_ylim(-0.5, 9.5)` with row 0 at
  the top (invert the y axis) and identical y tick positions; only the left panel
  carries no y tick labels because the labels are drawn once with `fig.text`.
- Drive all three panels from one list of dicts, each with `id`, `slug`,
  `agreement`, `rel_err`, `cv`, `catastrophe`, so the markers, connectors, colors,
  and annotations are derived, not hand placed.
- Use `ax.hlines`/`ax.plot` for connectors and markers; keep marker size 7 to 8 pt
  so values are readable.
- Save with `fig.savefig("papers/VVUQ-02/imagegen/03-ten-gate-threshold-forest/03-ten-gate-threshold-forest.png",
  dpi=300, facecolor="white")`. Do not use `bbox_inches="tight"`.

## Output paths

- Script: `papers/VVUQ-02/imagegen/03-ten-gate-threshold-forest/03-ten-gate-threshold-forest.py`.
- Image: `papers/VVUQ-02/imagegen/03-ten-gate-threshold-forest/03-ten-gate-threshold-forest.png`.

## Footer text

`cancer-automated v0.9.0  |  source: codegen/config/vvuq_thresholds.yaml, execution §03  |  white background, 300 dpi, portrait`

## Per figure acceptance checklist

- Portrait, full page, `figsize=(8.5, 11)`, saved at 300 dpi, white background.
- All 10 gates appear as rows in all three panels with the exact threshold values
  marked; catastrophe gates 06, 09, 10 in block red with their hard predicates
  noted.
- Default lines at 0.95, 0.05, and 0.10 are drawn and labeled; the verification
  fraction == 1.0 band is present.
- Row labels, panel titles, verification band, legend, and footer inside their
  bands, no overlap, none clipped.
- The section symbol renders as `§`; only single hyphens in visible text; no dark
  mode.
- Script is self contained, uses only matplotlib and numpy, and passes
  `ruff check` and `ruff format --check`.
