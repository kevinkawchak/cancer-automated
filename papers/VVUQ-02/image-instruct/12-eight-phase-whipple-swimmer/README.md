# Image Instruction 12: 60-Second 8-Phase Whipple Swimmer Plot

Chart family: swimmer plot (per-actor timeline lanes with milestone markers).
Basis: both code generation (v0.7.0 `codegen/config/project.yaml` phases) and code
execution (v0.8.0 execution §05 `eight_phase_timeline.txt`). Output: a single
portrait, full page, 300 dpi PNG that lays the 60-second 8-phase Whipple across
time as lanes for the left hand, the right hand, the suturing window, and the
continuously active catastrophe-gate safety surface, with the three anastomosis
milestones marked.

This instruction is self contained. Read the shared conventions in
`papers/VVUQ-02/image-instruct/README.md` for the page frame, palette, fonts,
symbols, and dash rules, then build exactly what is specified below.

## Purpose and message

The deployment reference is a single autonomous humanoid performing the full
8-phase Whipple in 60 seconds with its own two hands. The swimmer plot shows both
hands active every phase, the suturing window where the needle-driver grasp builds
three anastomoses, and a safety lane making clear that the three catastrophe gates
monitor continuously across the whole procedure, not just at the end.

## Grounding (cite in the footer)

Sources, used for every segment and marker below:

- `papers/VVUQ-02/codegen/config/project.yaml`, the `phases` block (id, name,
  start_s, end_s, duration_s, active_hands) and the `anastomosis_count` 3.
- `papers/VVUQ-02/execution/05-humanoid-deployment/artifacts/eight_phase_timeline.txt`
  (the timeline diagram and the suturing-phase note).
- `papers/VVUQ-02/codegen/config/anastomosis_targets.yaml` referenced ring-tension
  targets via execution §02.6 (PJ 0.45 N, HJ 0.50 N, GJ 0.60 N).

## The swimmer data (exact, eight phases)

Phases across the 60-second timeline (both hands active every phase):

| Phase | Name | start s | end s | duration s |
|-------|------|---------|-------|------------|
| 1 | Kocher exploration | 0 | 6 | 6 |
| 2 | venous control, dissection | 6 | 16 | 10 |
| 3 | uncinate dissection, artery first | 16 | 24 | 8 |
| 4 | specimen removal en bloc | 24 | 32 | 8 |
| 5 | pancreaticojejunostomy (PJ) | 32 | 42 | 10 |
| 6 | hepaticojejunostomy (HJ) | 42 | 48 | 6 |
| 7 | gastrojejunostomy (GJ) | 48 | 54 | 6 |
| 8 | hemostasis, closure | 54 | 60 | 6 |

Durations sum to 6 + 10 + 8 + 8 + 10 + 6 + 6 + 6 = 60 s. Suturing window: phases 5
to 7 use the needle-driver grasp. Anastomosis milestones (place a diamond at each
phase end with its ring-tension target): PJ at 42 s (0.45 N, graded A against the
Fistula Risk Score), HJ at 48 s (0.50 N), GJ at 54 s (0.60 N).

## Layout specification (portrait, full page)

Use the shared page frame. Build the content with a single full width axis in the
content band (`GridSpec` 1 by 1, `left=0.13, right=0.95, top=0.86, bottom=0.12`),
x axis time 0 to 60 s, four horizontal lanes stacked top to bottom.

- Header at `y = 0.965`: `60-Second 8-Phase Whipple Swimmer`. Subtitle at `y =
  0.935`: `One autonomous humanoid, two hands active every phase; the catastrophe
  gates monitor throughout (execution §05)`.
- Lanes (y, top to bottom): `Left hand (L)`, `Right hand (R)`, `Suturing window
  (needle driver)`, `Catastrophe-gate safety surface (VVUQ 06, 09, 10)`. Label each
  lane at the far left in 10.5 pt.
- Left hand and Right hand lanes: draw the 8 phase segments as rounded horizontal
  bars spanning each phase start to end. Color the 8 phases with a coherent
  sequential progression from teal `#2A9D8F` (phase 1) to primary navy `#1F3A5F`
  (phase 8); use the same color per phase in both hand lanes. Inside each segment
  write `P{n}` and, where the segment is wide enough, the short phase name; place
  the duration in 8.5 pt under the segment in the left hand lane only to avoid
  clutter.
- Suturing window lane: a single clinical rose `#B5566E` bar spanning 32 to 54 s
  (phases 5 to 7) labeled `needle-driver grasp`; place three clinical rose
  diamonds at 42, 48, 54 s for PJ, HJ, GJ, each annotated with its ring-tension
  target (`PJ 0.45 N grade A`, `HJ 0.50 N`, `GJ 0.60 N`).
- Safety-surface lane: a single full width band from 0 to 60 s with a light block
  red tint and the label `vascular no-fly, shared-OR collision, fault e-stop active
  every tick`, to show continuous monitoring; place three small block red gate
  pips labeled `06`, `09`, `10` at the left of the band.
- Phase boundary guides: thin vertical dashed gridlines at 0, 6, 16, 24, 32, 42,
  48, 54, 60 s, with the second value labeled on the bottom time axis.
- Time axis label under the lanes: `procedure time (s), reused verbatim from the
  PDAC 8-arm baseline for comparability`.
- Legend (upper area or right gutter): a small phase color ramp keyed `P1` to `P8`,
  plus clinical rose `anastomosis milestone` and block red tint `catastrophe gate
  active`.

## Color, symbol, and dash rules

- Phase segments in a teal to navy sequential ramp (same color per phase across
  both hand lanes), suturing window and milestones clinical rose, safety band block
  red tint with block red gate pips. White figure background, near black text,
  white text on the darker phase segments. No dark mode.
- Use `§` in the subtitle (`execution §05`). Use `N` for newtons and `s` for
  seconds.
- Single hyphens only. Write `needle-driver`, `no-fly`, `en bloc`, `artery first`,
  and ranges with the word `to`.

## matplotlib implementation directives

- `matplotlib.use("Agg")`; import `matplotlib.pyplot as plt`, `numpy as np`, and
  from `matplotlib.patches` import `FancyBboxPatch` and `Rectangle`.
- Drive the lanes from the phase list (id, name, start, end, duration); derive the
  phase color from a teal to navy colormap sampled at 8 points; assert the
  durations sum to 60 as a self check.
- Place milestone diamonds with `ax.scatter(marker="D")` at the phase-end times;
  draw lane bars with `FancyBboxPatch`.
- Set `ax.set_xlim(-1, 61)`, hide the y spine, and set y lane centers explicitly so
  spacing is deterministic.
- Save with `fig.savefig("papers/VVUQ-02/imagegen/12-eight-phase-whipple-swimmer/12-eight-phase-whipple-swimmer.png",
  dpi=300, facecolor="white")`. Do not use `bbox_inches="tight"`.

## Output paths

- Script: `papers/VVUQ-02/imagegen/12-eight-phase-whipple-swimmer/12-eight-phase-whipple-swimmer.py`.
- Image: `papers/VVUQ-02/imagegen/12-eight-phase-whipple-swimmer/12-eight-phase-whipple-swimmer.png`.

## Footer text

`cancer-automated v0.9.0  |  source: codegen/config/project.yaml phases, execution §05 eight_phase_timeline.txt  |  white background, 300 dpi, portrait`

## Per figure acceptance checklist

- Portrait, full page, `figsize=(8.5, 11)`, saved at 300 dpi, white background.
- Four lanes present; both hand lanes carry all 8 phase segments with correct
  start and end times summing to 60 s.
- The suturing window spans phases 5 to 7 with the three anastomosis milestones (PJ
  0.45 N, HJ 0.50 N, GJ 0.60 N); the safety lane spans the full 60 s with the 06,
  09, 10 pips.
- Phase boundary guides at the listed times; legend and time axis label present.
- Header, subtitle, legend, and footer inside their bands, no overlap, none
  clipped.
- The section symbol renders as `§`; only single hyphens in visible text; no dark
  mode.
- Script is self contained, uses only matplotlib and numpy, and passes
  `ruff check` and `ruff format --check`.
