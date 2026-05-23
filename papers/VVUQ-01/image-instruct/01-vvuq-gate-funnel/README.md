# Image Instruction 01: VVUQ Gate Decision Funnel

Chart family: funnel. Basis: both code generation (v0.1.0 `vvuq/`) and code
execution (v0.2.0 execution §03). Output: a single portrait, full page, 300 dpi
PNG that shows six candidate deliverables entering the VVUQ gate and only one
surviving to ship, with each drop labeled by the dimension that blocked it.

This instruction is self contained. Read the shared conventions in
`papers/VVUQ-01/image-instruct/README.md` for the page frame, palette, fonts,
symbols, and dash rules, then build exactly what is specified below.

## Purpose and message

The figure makes the central thesis visible in one glance: code generation is
trivial and the assurance process is the substantial filter. Six syntactically
valid candidate deliverables enter. The gate, held to a higher standard than
code generation, blocks five and accepts one. The funnel narrows across the
three VVUQ dimensions in the exact order the gate evaluates them, and each
narrowing carries the verbatim blocking reason from the execution record.

## Grounding (cite in the footer)

Sources, used for every value below:

- `vvuq/vvuq_gate.py` and `vvuq/README.md`, plus `configs/vvuq_thresholds.yaml`,
  for the gate dimensions and thresholds (code generation v0.1.0).
- `papers/VVUQ-01/execution/03-vvuq/README.md` for the six gate cases and the
  verbatim accepted and blocked outcomes (code execution v0.2.0).

Thresholds the gate enforces (from `configs/vvuq_thresholds.yaml`): verification
checks passed fraction must equal 1.0; validation agreement at or above 0.95 with
maximum relative error at or below 0.05 and a recorded human review; uncertainty
maximum coefficient of variation at or below 0.10 with at least 3 consensus runs;
block on any failure and escalate to a human on divergence.

## The funnel data (exact, from execution §03)

The funnel has four levels. Encode the counts as the funnel widths.

| Level | Stage label | Candidates entering | Candidates passing | Dropped here |
|-------|-------------|---------------------|--------------------|--------------|
| 0 | Generated candidates (under 1 ms each) | 6 | 6 | none |
| 1 | Verification, fraction must equal 1.0 | 6 | 5 | Case 6 |
| 2 | Validation, agreement at least 0.95, human review | 5 | 3 | Case 2, Case 4 |
| 3 | Uncertainty, CV at most 0.10, runs at least 3 | 3 | 1 | Case 3 (escalated), Case 5 |
| 4 | Accepted and shippable | 1 | 1 | none |

The five blocked cases and their verbatim reasons (right side callouts):

| Case | Dropped at | Verbatim reason | Encode color |
|------|-----------|------------------|--------------|
| Case 6 | Verification | verification fraction 0.83 below 1.0 (artifact exceeds 200K cap) | block red |
| Case 2 | Validation | human review not recorded | block red |
| Case 4 | Validation | validation agreement 0.00 below 0.95; max relative error 0.600 above 0.05 | block red |
| Case 3 | Uncertainty | max cv 0.365 above 0.1, escalated to human | escalate amber |
| Case 5 | Uncertainty | only 2 runs, need 3 | block red |

The single accepted case (Case 1, clean, human reviewed, low CV) carries the
verbatim accept scores: verification fraction 1.0, validation agreement 1.0, max
relative error 0.0, max cv 0.0068, n runs 3.

## Layout specification (portrait, full page)

Use the shared page frame. Build the content with a single full width axis in
the content band (`GridSpec` 1 by 1, `left=0.06, right=0.94, top=0.91,
bottom=0.07`), with the funnel centered and callout columns on the right.

- Header at `y = 0.965`: `VVUQ Gate Decision Funnel`. Subtitle at `y = 0.935`:
  `Six candidate deliverables enter, one ships, five are blocked`.
- Funnel body, centered on `x = 0.42` of the axis, occupying the vertical span of
  the content band. Draw four stacked trapezoid bands top to bottom using
  `matplotlib.patches.Polygon`, where each band tapers from its entering count
  (top width) to its passing count (bottom width). Use exactly these bands so the
  geometry is unambiguous:

  | Band, top to bottom | Top width count | Bottom width count |
  |---------------------|-----------------|--------------------|
  | Verification | 6 | 5 |
  | Validation | 5 | 3 |
  | Uncertainty | 3 | 1 |
  | Accept | 1 | 1 |

  Map count to half width linearly (the same scale for all bands) so the
  silhouette tapers smoothly and the bands meet edge to edge. Fill with a vertical
  progression from primary navy `#1F3A5F` at the top to teal `#2A9D8F` near the
  bottom, and fill the final Accept band (a width 1 tip) with accept green
  `#2E7D32`. Outline each band in white at 1.5 pt so the boundaries read cleanly.
- Inside each band, centered, place two lines of 11 pt text: the stage label and
  the counts, for example `Verification` and `6 in, 5 pass`. Use near black
  `#1A1A1A`; on the dark navy top segment use white text for contrast.
- Left gutter (`x` near 0.04 to 0.16 of the axis): a thin vertical arrow pointing
  down labeled `Gate evaluation order` in neutral gray `#6B7280`, 9 pt, rotated
  90 degrees, so the reader sees the dimensions are applied in sequence.
- Right callout column (`x` from about 0.62 to 0.98 of the axis): for each drop,
  draw a rounded rectangle card (`FancyBboxPatch`, panel fill `#F4F6F8`, thin
  gridline gray border) connected to its funnel level by a short leader line.
  Block cards use a block red `#C0392B` left edge accent; the escalate card
  (Case 3) uses escalate amber `#E1A93B`. Card text is 9.5 pt: the case name in
  bold then the verbatim reason wrapped to the card width.
- Accept badge: beside the green tip, a small accept green pill labeled `ACCEPT`
  with the accept scores in 9 pt underneath (`verification 1.0, agreement 1.0,
  rel err 0.0, max cv 0.0068, n=3`).
- Asymmetry annotation: a 10 pt italic note near the top, `Generation of all six
  candidates took under 1 ms of stage time; the gate is the substantial step`.
- Legend at lower left of the content band: three swatches, accept green
  `Accepted`, block red `Blocked`, escalate amber `Escalated to human`.

## Color, symbol, and dash rules

- Funnel navy to teal gradient by level, accepted tip accept green, block cards
  block red accent, escalate card escalate amber, cards on panel fill, text near
  black (white where it sits on the navy segment). No dark mode, white figure
  background.
- No section symbol is required in this figure. If a level label references the
  threshold file, write the plain file name, not a section.
- Single hyphens only in all visible text. Write `under 1 ms`, `2.5x` style, and
  ranges with the word `to`.

## matplotlib implementation directives

- `matplotlib.use("Agg")`; import `matplotlib.pyplot as plt`, `numpy as np`, and
  from `matplotlib.patches` import `Polygon` and `FancyBboxPatch`.
- One axis spanning the content band; call `ax.set_xlim(0, 1)`, `ax.set_ylim(0,
  1)`, `ax.axis("off")` and place all geometry in axis coordinates so the layout
  is fully deterministic and needs no manual nudging.
- Compute the four trapezoids from a single `bands = [(6, 5), (5, 3), (3, 1), (1,
  1)]` list of (top count, bottom count) pairs and one shared count to half width
  scale, so the widths are derived, not hand placed, and adjacent bands meet edge
  to edge.
- Wrap long card text with `textwrap.fill` at about 34 characters so no text
  leaves its card.
- Save with `fig.savefig("papers/VVUQ-01/imagegen/01-vvuq-gate-funnel/01-vvuq-gate-funnel.png",
  dpi=300, facecolor="white")`. Do not use `bbox_inches="tight"`.

## Output paths

- Script: `papers/VVUQ-01/imagegen/01-vvuq-gate-funnel/01-vvuq-gate-funnel.py`.
- Image: `papers/VVUQ-01/imagegen/01-vvuq-gate-funnel/01-vvuq-gate-funnel.png`.

## Footer text

`cancer-automated v0.3.0  |  source: vvuq/vvuq_gate.py, configs/vvuq_thresholds.yaml, execution §03  |  white background, 300 dpi, portrait`

## Per figure acceptance checklist

- Portrait, full page, `figsize=(8.5, 11)`, saved at 300 dpi, white background.
- Funnel narrows 6, 5, 3, 1 with the accepted tip in accept green.
- All five blocked or escalated cards present with verbatim reasons, no overlap,
  none clipped.
- Accept badge shows the five accept scores exactly.
- Header, subtitle, legend, asymmetry note, and footer inside their bands.
- Only single hyphens in visible text; no dark mode.
- Script is self contained, uses only matplotlib and numpy, and passes
  `ruff check` and `ruff format --check`.
