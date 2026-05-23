# Image Instruction 05: 2030 PDAC Hybrid Pilot Timeline

Chart family: Gantt timeline. Basis: both code generation (v0.1.0
`physical-ai/hybrid_surgery_medicine.py`) and code execution (v0.2.0 execution
§05 and the saved artifact). Output: a single portrait, full page, 300 dpi PNG
that lays out the 168 day hybrid surgery and medicine pilot as a Gantt, the
Stage 2 analog of the 2030 PDAC 60 second robotic Whipple plus Daraxonrasib
simulation.

Read the shared conventions in `papers/VVUQ-01/image-instruct/README.md` first,
then build exactly what is specified below.

## Purpose and message

Stage 2 combines a sub minute robotic procedure with a multi month adjuvant
regimen, planned as one timeline. The figure is the concrete deliverable type a
future paper extends with real procedure and regimen data once VVUQ clearance and
approvals are in place. It anchors the surgery at day 0 and places each adjuvant
cycle every 28 days through day 168.

## Grounding (cite in the footer)

- `physical-ai/hybrid_surgery_medicine.py` and `physical-ai/README.md` for the
  pilot model (code generation v0.1.0).
- `papers/VVUQ-01/execution/05-physical-ai-stage2/README.md` and
  `papers/VVUQ-01/execution/05-physical-ai-stage2/artifacts/pdac_hybrid_pilot_timeline.txt`
  for the executed summary and timeline (code execution v0.2.0).

## The timeline data (exact, from the saved artifact)

Summary: surgery `Robotic Whipple (60 second)`, surgery seconds 60.0, surgery
arms 8, medicine `Daraxonrasib (adjuvant)`, regimen days 168, events 7, requires
human oversight True.

| Row | Event | Type | Day | Span (days) | Detail |
|-----|-------|------|-----|-------------|--------|
| 1 | Robotic Whipple (60 second) | surgery | 0 | point event | 8 arm procedure, 60 s |
| 2 | Daraxonrasib adjuvant cycle 1 | medicine | 28 | 0 to 28 | cycle administered at day 28 |
| 3 | Daraxonrasib adjuvant cycle 2 | medicine | 56 | 28 to 56 | cycle administered at day 56 |
| 4 | Daraxonrasib adjuvant cycle 3 | medicine | 84 | 56 to 84 | cycle administered at day 84 |
| 5 | Daraxonrasib adjuvant cycle 4 | medicine | 112 | 84 to 112 | cycle administered at day 112 |
| 6 | Daraxonrasib adjuvant cycle 5 | medicine | 140 | 112 to 140 | cycle administered at day 140 |
| 7 | Daraxonrasib adjuvant cycle 6 | medicine | 168 | 140 to 168 | cycle administered at day 168 |

Arithmetic to annotate: regimen days equal cycles times cycle length, 6 times 28
equals 168; timeline events equal 1 surgery plus 6 cycles equals 7.

## Layout specification (portrait, full page)

Use the shared page frame with three stacked regions: a summary strip, the Gantt,
and a Stage 2 assurance note. `GridSpec(3, 1, height_ratios=[0.7, 2.6, 0.6],
left=0.06, right=0.94, top=0.90, bottom=0.07, hspace=0.22)`.

- Header at `y = 0.965`: `2030 PDAC Hybrid Pilot Timeline`. Subtitle at `y =
  0.935`: `A 60 second 8 arm robotic Whipple on day 0 plus six 28 day
  Daraxonrasib cycles, 168 regimen days`.
- Summary strip (top axis): four equal cards on panel fill `#F4F6F8`, each 11 pt:
  `Surgery 60.0 s, 8 arms`, `Medicine Daraxonrasib, 6 cycles`, `Regimen 168 days
  (6 x 28)`, `Events 7, human oversight required`. The oversight card carries an
  escalate amber `#E1A93B` left accent to flag the gating.
- Gantt (middle axis):
  - `x` axis is days 0 to 168 with major ticks at 0, 28, 56, 84, 112, 140, 168,
    gridlines in gridline gray `#D9DEE3`.
  - 7 horizontal rows top to bottom in the row order above. The surgery row is a
    bold point marker at day 0: a primary navy `#1F3A5F` diamond with a block red
    `#C0392B` core, plus a 60 s callout, since the procedure is sub minute and has
    no visible width on a 168 day axis.
  - The six medicine rows are 28 day bars spanning their window, filled with a
    teal progression from light teal at cycle 1 to deeper teal `#2A9D8F` at cycle
    6, rounded ends, each labeled `cycle k` at its left and the administration day
    at its right end (for example `day 168`).
  - A vertical day 0 reference line in navy and a vertical day 168 reference line
    in accept green labeled `regimen complete, day 168`.
  - Left row labels, 10.5 pt, name each event; keep them inside the left margin.
- Stage 2 assurance note (bottom axis) on panel fill: 10 pt, `Stage 2 reference,
  disabled by default. The lights off line requires the vvuq_gate_online
  interlock and this pilot sets requires_human_oversight True. Real use needs
  VVUQ clearance, human oversight, IRB approval, and regulatory authorization`.

## Color, symbol, and dash rules

- Surgery marker navy with block red core, medicine bars teal progression, day
  168 line accept green, oversight accent escalate amber, gridlines gridline
  gray, panel fill for cards and the note, near black text. White background, no
  dark mode.
- No section symbol required. Write the cycle math as `6 x 28` and durations as
  `60.0 s` and `28 day`.
- Single hyphens only in visible text; write `60 second` and `sub minute` with
  single hyphens where hyphenation is natural.

## matplotlib implementation directives

- `matplotlib.use("Agg")`; `matplotlib.pyplot as plt`, `numpy as np`; from
  `matplotlib.patches` import `FancyBboxPatch` for rounded cycle bars or use
  `ax.barh` with rounded caps via `FancyBboxPatch`.
- Drive cycle spans from `starts = [28*k for k in range(6)]` and width 28 so the
  six bars are computed, not hand placed; set fixed `x` limits 0 to 172 so the
  layout is deterministic and the day 168 label is not clipped.
- Place the surgery marker with `ax.scatter` at day 0 on its row, and annotate
  `8 arm, 60 s` to the right of the marker.
- Save to `papers/VVUQ-01/imagegen/05-pdac-pilot-timeline/05-pdac-pilot-timeline.png`
  with `dpi=300, facecolor="white"`, no `bbox_inches="tight"`.

## Output paths

- Script: `papers/VVUQ-01/imagegen/05-pdac-pilot-timeline/05-pdac-pilot-timeline.py`.
- Image: `papers/VVUQ-01/imagegen/05-pdac-pilot-timeline/05-pdac-pilot-timeline.png`.

## Footer text

`cancer-automated v0.3.0  |  source: physical-ai/hybrid_surgery_medicine.py, execution §05 artifact pdac_hybrid_pilot_timeline.txt  |  white background, 300 dpi, portrait`

## Per figure acceptance checklist

- Portrait, full page, `figsize=(8.5, 11)`, saved at 300 dpi, white background.
- Seven rows: a day 0 surgery marker and six 28 day cycle bars at days 28 through
  168, axis ticks at the 28 day grid.
- Summary cards show 60.0 s, 8 arms, 6 cycles, 168 days, 7 events, oversight
  required; the day 168 completion line is accept green.
- Stage 2 assurance note present.
- Header, subtitle, and footer inside their bands, nothing clipped.
- Only single hyphens in visible text; no dark mode.
- Script self contained, only matplotlib and numpy, passes `ruff check` and
  `ruff format --check`.
