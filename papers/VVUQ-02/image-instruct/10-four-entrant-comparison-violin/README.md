# Image Instruction 10: Four-Entrant Comparison Box Plot

Chart family: box plot (with mean markers and a win-rate side panel; the box plot
or violin family). Basis: both code generation (v0.7.0
`codegen/results/comparison.json`) and code execution (v0.8.0 execution §04
`comparison_analysis.txt` and `comparison_leaderboard.md`). Required data R6: the
1790-line, four-entrant comparison, featuring the second-place mobile humanoid.
Output: a single portrait, full page, 300 dpi PNG that shows the composite-score
distribution of each of the four entrants and the leaderboard, with the autonomous
H2 humanoid called out as the second-place finisher.

This instruction is self contained. Read the shared conventions in
`papers/VVUQ-02/image-instruct/README.md` for the page frame, palette, fonts,
symbols, and dash rules, then build exactly what is specified below.

## Purpose and message

The featured 1790-line `comparison.json` records 32 iterations of 4 rounds, 128
verdicts, across four entrants. The figure shows the autonomous single humanoid
(H2-Surgical 1.0) landing in second place by composite mean, within about half a
point of the multi-arm cart, well above the teleoperated successor and the human
baseline, while carrying every honesty caveat. The box plot makes the separation
and the overlap between the two leaders legible at once.

## Grounding (cite in the footer)

Sources, used for every value below:

- `papers/VVUQ-02/codegen/results/comparison.json` (the 1790-line, 4-entrant,
  128-verdict tournament) and `results/comparison_report.md`.
- `papers/VVUQ-02/execution/04-automation/artifacts/comparison_analysis.txt` (the
  per-entrant composite dispersion across all appearances).
- `papers/VVUQ-02/execution/04-automation/artifacts/comparison_leaderboard.md`
  (rank, composite mean, win rate).

## The comparison data (exact, four entrants)

Per-entrant composite dispersion across all appearances (hardcode these as the box
and whisker geometry; the per-appearance arrays live in `comparison.json` and are
summarized here):

| Rank | Entrant | n | min | max | mean | spread | win rate | total wins |
|------|---------|---|-----|-----|------|--------|----------|------------|
| 1 | PancreSpeed_1_0 (8-arm cart) | 64 | 92.764 | 94.730 | 93.782 | 1.966 | 0.875 | 56 |
| 2 | H2_Surgical_1_0 (humanoid) | 96 | 92.468 | 94.417 | 93.334 | 1.949 | 0.75 | 72 |
| 3 | da_Vinci_successor_2030 (teleop) | 64 | 82.928 | 84.832 | 83.970 | 1.904 | 0.0 | 0 |
| 4 | Dutch_human_baseline (2025 cohort) | 32 | 66.911 | 68.884 | 67.885 | 1.973 | 0.0 | 0 |

The four entrant appearance counts sum to 64 + 96 + 64 + 32 = 256, which is 128
verdicts times 2 entrants per verdict. Per-round aggregate winners over 32
iterations: round 1 PancreSpeed 24 of 32; round 2 H2 32 of 32; round 3 H2 32 of
32; round 4 PancreSpeed 32 of 32.

Caveats to print (verbatim, every robot-involving verdict carries the first; every
round-3 human-versus-robot verdict carries the second): `The H2-Surgical 1.0 is a
hypothetical 2030 platform; this comparison is simulation against simulation.` and
`Structural time-dimension caveat: a 1-minute robot run against a multi-hour human
baseline; the time component dominates the delta.`

## Layout specification (portrait, full page)

Use the shared page frame. Build the content with a `GridSpec(2, 1,
height_ratios=[3, 1], left=0.12, right=0.95, top=0.88, bottom=0.12, hspace=0.26)`:
the large top axis is the box plot, the short bottom axis is the win-rate panel and
the caveat band.

- Header at `y = 0.965`: `Four-Entrant Comparison: the Humanoid in Second Place`.
  Subtitle at `y = 0.935`: `Composite score across 128 verdicts in the 1790-line
  comparison.json; H2-Surgical 1.0 is rank 2 (execution §04)`.
- Box plot axis: four vertical boxes, one per entrant left to right in rank order.
  For each entrant draw a box whose whiskers span min to max, a box body spanning a
  central band (use mean plus or minus a quarter of the spread as a readable inner
  box since the per-appearance quartiles are summarized by mean and spread), a mean
  diamond at the mean value with the mean printed beside it, and the entrant label
  with its morphology in two lines below the x axis. Color: PancreSpeed slate blue
  `#4C72B0`; H2-Surgical teal `#2A9D8F` with a 2 pt accept-green outline and a
  `rank 2` badge to feature it; da Vinci neutral gray `#6B7280`; Dutch human
  clinical rose `#B5566E`. y axis composite score 64 to 96.
- Separation guides: a faint dashed horizontal line at the H2 mean 93.334 and at
  the PancreSpeed mean 93.782, with a small bracket annotation `delta about 0.45 of
  a point` between the two leaders.
- Win-rate panel (bottom axis, left two thirds): a horizontal lollipop per entrant
  showing win rate (0.875, 0.75, 0.0, 0.0) with the total wins (56, 72, 0, 0)
  annotated, plus a 9 pt note `the humanoid has more total wins (72) because it
  appears in 3 of 4 rounds; win rate normalizes for appearances`.
- Caveat band (bottom axis, right third or a full-width strip beneath): a panel
  fill card with an escalate amber left accent holding the two verbatim caveats in
  9 pt, wrapped.
- Legend (box axis, upper area): four swatches keyed to the entrant colors with
  rank and mean.

## Color, symbol, and dash rules

- Entrant colors as listed, H2 featured with an accept-green outline and a rank 2
  badge, mean diamonds near black, separation guides dashed neutral gray, caveat
  card escalate amber accent. White figure background, near black text. No dark
  mode.
- Use `§` in the subtitle (`execution §04`). Write `8-arm`, `1-minute`,
  `multi-hour` with single hyphens.
- Single hyphens only. Write `delta about 0.45 of a point`, `3 of 4 rounds`, and
  ranges with the word `to`. Use `x` only as a multiplier elsewhere, not here.

## matplotlib implementation directives

- `matplotlib.use("Agg")`; import `matplotlib.pyplot as plt`, `numpy as np`, and
  from `matplotlib.patches` import `Rectangle` and `FancyBboxPatch`.
- Build the boxes manually from the hardcoded summary (min, max, mean, spread) with
  `Rectangle` for the box body and `ax.vlines`/`ax.hlines` for the whiskers and
  caps, so every drawn coordinate is a cited number; do not call `ax.boxplot` on
  fabricated arrays.
- Assert the appearance counts sum to 256 as a self check.
- Build the caveat card with `FancyBboxPatch`; wrap text with `textwrap.fill` at
  about 50 characters.
- Save with `fig.savefig("papers/VVUQ-02/imagegen/10-four-entrant-comparison-violin/10-four-entrant-comparison-violin.png",
  dpi=300, facecolor="white")`. Do not use `bbox_inches="tight"`.

## Output paths

- Script: `papers/VVUQ-02/imagegen/10-four-entrant-comparison-violin/10-four-entrant-comparison-violin.py`.
- Image: `papers/VVUQ-02/imagegen/10-four-entrant-comparison-violin/10-four-entrant-comparison-violin.png`.

## Footer text

`cancer-automated v0.9.0  |  source: codegen/results/comparison.json, execution §04 comparison_analysis.txt and comparison_leaderboard.md  |  white background, 300 dpi, portrait`

## Per figure acceptance checklist

- Portrait, full page, `figsize=(8.5, 11)`, saved at 300 dpi, white background.
- Four boxes with the exact min, max, and mean per entrant; H2-Surgical featured
  as rank 2 with the accept-green outline and badge.
- The leader separation bracket (about 0.45 of a point), the win-rate lollipops
  (0.875, 0.75, 0.0, 0.0 with wins 56, 72, 0, 0), and both verbatim caveats are
  present.
- Appearance counts reconcile to 256; legend present.
- Header, subtitle, legend, win-rate panel, caveat card, and footer inside their
  bands, no overlap, none clipped.
- The section symbol renders as `§`; only single hyphens in visible text; no dark
  mode.
- Script is self contained, uses only matplotlib and numpy, and passes
  `ruff check` and `ruff format --check`.
