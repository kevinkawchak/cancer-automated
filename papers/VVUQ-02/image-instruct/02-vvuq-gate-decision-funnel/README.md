# Image Instruction 02: VVUQ Gate Decision Funnel

Chart family: funnel. Basis: both code generation (v0.7.0
`codegen/config/vvuq_thresholds.yaml`) and code execution (v0.8.0 execution §03
decision surface). Output: a single portrait, full page, 300 dpi PNG that shows
five candidate decision cases entering the assurance layer and only one surviving
to ship, narrowing through the four evaluation dimensions in the exact order the
gate applies them, each drop carrying the verbatim reason from the execution
record.

This instruction is self contained. Read the shared conventions in
`papers/VVUQ-02/image-instruct/README.md` for the page frame, palette, fonts,
symbols, and dash rules, then build exactly what is specified below.

## Purpose and message

The figure makes the central thesis visible in one glance: candidate behaviors
are generated cheaply, and the assurance gate, held to a higher standard than
code, is the substantial filter. Five cases enter (the nominal full-ACCEPT sweep
plus four adversarial cases). The funnel narrows across the four VVUQ dimensions
in evaluation order, and each narrowing carries the verbatim blocking or
escalating reason from execution §03.

## Grounding (cite in the footer)

Sources, used for every value below:

- `papers/VVUQ-02/codegen/config/vvuq_thresholds.yaml` for the dimension
  thresholds (verification fraction 1.0, validation agreement and relative error,
  uncertainty coefficient of variation, the catastrophe hard predicates).
- `papers/VVUQ-02/execution/03-vvuq/README.md` for the five decision cases A to E
  and the verbatim ACCEPT, BLOCK, and ESCALATE outcomes.

Thresholds the gate enforces (from the config): verification checks passed
fraction must equal 1.0; validation agreement from 0.95 up to 1.00 for the
catastrophe gates with maximum relative error as tight as 0.01; uncertainty
coefficient of variation as tight as 0.05 with at least 3 consensus runs; and an
extra hard predicate on gates 06, 09, and 10.

## The funnel data (exact, from execution §03)

The funnel has five narrowing levels plus the accepted tip. Encode the case counts
as the funnel widths.

| Level | Dimension applied | Cases entering | Cases passing | Dropped here |
|-------|-------------------|----------------|---------------|--------------|
| 0 | Generated candidate cases | 5 | 5 | none |
| 1 | Verify, fraction must equal 1.0 | 5 | 4 | Case C |
| 2 | Validate, agreement at or above bound | 4 | 3 | Case D |
| 3 | Quantify, CV at or below bound | 3 | 2 | Case E (escalated) |
| 4 | Hard predicate, catastrophe gates | 2 | 1 | Case B |
| 5 | ACCEPT and shippable | 1 | 1 | none |

The four dropped or escalated cases and their verbatim reasons (right side
callouts):

| Case | Gate | Dropped at | Verbatim reason | Encode color |
|------|------|-----------|------------------|--------------|
| Case C | 08 perception-scene-understanding | Verify | verification fraction 0.80 below 1.0 (4 of 5 structural checks) | block red |
| Case D | 03 whole-body-balance | Validate | validation agreement 0.00 below 0.98; max relative error 0.500 above 0.03 | block red |
| Case E | 02 dexterous-finger-force | Quantify | max cv 0.163 above 0.10; escalated to hand-back-to-human | escalate amber |
| Case B | 06 vascular-no-fly-hand | Hard predicate | hard check failed: hard_stop_violations_zero | block red |

The single accepted case (Case A, the nominal sweep, all 10 gates ACCEPT over
their independent references) carries the verbatim note `all 10 gates ACCEPT:
True; composite reported (sweep mean 93.56)`.

## Layout specification (portrait, full page)

Use the shared page frame. Build the content with a single full width axis in the
content band (`GridSpec` 1 by 1, `left=0.06, right=0.94, top=0.91, bottom=0.07`),
with the funnel centered and callout cards on the right.

- Header at `y = 0.965`: `VVUQ Gate Decision Funnel`. Subtitle at `y = 0.935`:
  `Five candidate cases enter, one ships; verify, validate, quantify, hard
  predicate (execution §03)`.
- Funnel body, centered on `x = 0.40` of the axis, occupying the vertical span of
  the content band. Draw five stacked trapezoid bands top to bottom using
  `matplotlib.patches.Polygon`, where each band tapers from its entering count
  (top width) to its passing count (bottom width). Use exactly these bands so the
  geometry is unambiguous:

  | Band, top to bottom | Top width count | Bottom width count |
  |---------------------|-----------------|--------------------|
  | Verify | 5 | 4 |
  | Validate | 4 | 3 |
  | Quantify | 3 | 2 |
  | Hard predicate | 2 | 1 |
  | Accept | 1 | 1 |

  Map count to half width linearly (one shared scale for all bands) so the
  silhouette tapers smoothly and bands meet edge to edge. Fill with a vertical
  progression from primary navy `#1F3A5F` at the top to teal `#2A9D8F` near the
  bottom, and fill the final Accept band (a width 1 tip) with accept green
  `#2E7D32`. Outline each band in white at 1.5 pt.
- Inside each band, centered, place two lines of 11 pt text: the dimension label
  and the counts, for example `Verify` and `5 in, 4 pass`. Use near black
  `#1A1A1A`; on the dark navy top segment use white text for contrast.
- Left gutter (`x` near 0.04 to 0.14): a thin vertical arrow pointing down labeled
  `gate evaluation order` in neutral gray `#6B7280`, 9 pt, rotated 90 degrees.
- Right callout column (`x` from about 0.60 to 0.98): for each drop, draw a
  rounded rectangle card (`FancyBboxPatch`, panel fill `#F4F6F8`, thin gridline
  gray border) connected to its funnel level by a short leader line. Block cards
  (C, D, B) use a block red `#C0392B` left edge accent; the escalate card (E) uses
  escalate amber `#E1A93B`. Card text is 9.5 pt: the case and gate name in bold,
  then the verbatim reason wrapped to the card width.
- Accept badge: beside the green tip, a small accept green pill labeled `ACCEPT`
  with `Case A: all 10 gates pass; composite 93.56` in 9 pt underneath.
- Asymmetry annotation: a 10 pt italic note near the top, `Generating each
  candidate took microseconds; the four-dimension gate is the substantial step`.
- Legend at lower left of the content band: three swatches, accept green
  `Accepted`, block red `Blocked`, escalate amber `Escalated to human`.

## Color, symbol, and dash rules

- Funnel navy to teal gradient by level, accepted tip accept green, block cards
  block red accent, escalate card escalate amber, cards on panel fill, text near
  black (white on the navy segment). No dark mode, white figure background.
- Use `§` in the subtitle (`execution §03`). If a card references a config clause,
  write the plain file or predicate name.
- Single hyphens only. Write `4 of 5`, `hand-back-to-human`, and ranges with the
  word `to`.

## matplotlib implementation directives

- `matplotlib.use("Agg")`; import `matplotlib.pyplot as plt`, `numpy as np`, and
  from `matplotlib.patches` import `Polygon` and `FancyBboxPatch`.
- One axis spanning the content band; `ax.set_xlim(0, 1)`, `ax.set_ylim(0, 1)`,
  `ax.axis("off")`, geometry in axis coordinates.
- Compute the five trapezoids from a single `bands = [(5, 4), (4, 3), (3, 2),
  (2, 1), (1, 1)]` list of (top, bottom) pairs and one shared count to half width
  scale, so widths are derived and adjacent bands meet edge to edge.
- Wrap long card text with `textwrap.fill` at about 32 characters.
- Save with `fig.savefig("papers/VVUQ-02/imagegen/02-vvuq-gate-decision-funnel/02-vvuq-gate-decision-funnel.png",
  dpi=300, facecolor="white")`. Do not use `bbox_inches="tight"`.

## Output paths

- Script: `papers/VVUQ-02/imagegen/02-vvuq-gate-decision-funnel/02-vvuq-gate-decision-funnel.py`.
- Image: `papers/VVUQ-02/imagegen/02-vvuq-gate-decision-funnel/02-vvuq-gate-decision-funnel.png`.

## Footer text

`cancer-automated v0.9.0  |  source: codegen/config/vvuq_thresholds.yaml, execution §03  |  white background, 300 dpi, portrait`

## Per figure acceptance checklist

- Portrait, full page, `figsize=(8.5, 11)`, saved at 300 dpi, white background.
- Funnel narrows 5, 4, 3, 2, 1 with the accepted tip in accept green.
- All four dropped or escalated cards present with verbatim reasons, none
  overlapping, none clipped.
- Accept badge shows Case A passing all 10 gates with the composite.
- Header, subtitle, legend, asymmetry note, and footer inside their bands.
- The section symbol renders as `§`; only single hyphens in visible text; no dark
  mode.
- Script is self contained, uses only matplotlib and numpy, and passes
  `ruff check` and `ruff format --check`.
