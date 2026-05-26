# Image Instruction 08: 32-Iteration Composite Strip Plot

Chart family: dot / strip plot (jittered, with summary overlay and a gated-versus-
withheld lane). Basis: code execution (v0.8.0 execution §04
`composite_scores.jsonl` and the sweep summary). Output: a single portrait, full
page, 300 dpi PNG that shows every one of the 32 sweep composite scores as a
point, with the mean and range, and a second lane illustrating the gating overlay
that withholds the score whenever any gate is not ACCEPT.

This instruction is self contained. Read the shared conventions in
`papers/VVUQ-02/image-instruct/README.md` for the page frame, palette, fonts,
symbols, and dash rules, then build exactly what is specified below.

## Purpose and message

The 32-iteration Latin hypercube sweep clears all 10 gates on every iteration, so
the composite is reported for all 32, and the spread is tight (about 0.30 of a
point). The figure shows each iteration as a point, the mean and range, and, in a
second lane, the rule that makes the thesis mechanical: the composite is reported
only because every gate ACCEPTs; on any BLOCK or ESCALATE the gating overlay sets
it to null.

## Grounding (cite in the footer)

Sources, used for every value below:

- `papers/VVUQ-02/execution/04-automation/artifacts/composite_scores.jsonl` (the
  32 gated composite records, each `gates_all_accepted: true`).
- `papers/VVUQ-02/execution/04-automation/README.md` (composite distribution: min
  93.417, max 93.715, mean 93.562; 32 of 32 cleared all 10 gates; the gating
  overlay sets the composite to null on any non-ACCEPT).

## The strip data (exact, 32 iterations)

Composite score per iteration id 0 to 31 (hardcode these 32 values as a Python
list, in id order):

```
93.573, 93.519, 93.668, 93.587, 93.537, 93.583, 93.600, 93.622,
93.515, 93.474, 93.631, 93.527, 93.649, 93.461, 93.715, 93.522,
93.669, 93.522, 93.482, 93.600, 93.558, 93.594, 93.601, 93.593,
93.507, 93.417, 93.443, 93.663, 93.611, 93.443, 93.528, 93.574
```

That is exactly 32 values (ids 0 to 31). Summary to annotate: n 32, min 93.417
(id 25), max 93.715 (id 14), mean 93.562, range 0.298, all 32 with
`gates_all_accepted` true.

## Layout specification (portrait, full page)

Use the shared page frame. Build the content with a `GridSpec(3, 1,
height_ratios=[1, 3, 2], left=0.10, right=0.95, top=0.88, bottom=0.10,
hspace=0.30)`: a thin top marginal axis, the main strip axis, and a lower
gating-overlay lane axis. All three share the same composite x range 93.38 to
93.74.

- Header at `y = 0.965`: `32-Iteration Sweep Composite Scores`. Subtitle at `y =
  0.935`: `All 32 iterations cleared all 10 gates; the score is reported only
  because every gate ACCEPTs (execution §04)`.
- Top marginal axis: a thin outline density (a smoothed histogram or a 12-bin step
  outline) of the 32 values in teal, no fill, to show the tight unimodal spread;
  axis spines off except a faint baseline.
- Main strip axis: plot the 32 composite values as accept green circles on a
  single horizontal lane, with a small deterministic vertical jitter (for example
  y = 0.5 plus a fixed pseudo-random offset seeded so the layout is reproducible)
  so overlapping points separate. Overlay a vertical mean line at 93.562 labeled
  `mean 93.562`, a horizontal min to max range bar from 93.417 to 93.715 labeled
  `range 0.298`, and a hollow diamond at the mean. Mark the min (93.417, iter 25)
  and max (93.715, iter 14) points with small labels.
- Gating-overlay lane axis: two stacked rows. Top row, accept green, 32 small
  ticks at their composite x with the label `gates_all_accepted = true -> composite
  reported (this sweep: 32 of 32)`. Bottom row, neutral gray hatched, a single
  greyed placeholder with the label `any BLOCK or ESCALATE -> composite = null
  (withheld)`, with a block red and an escalate amber pip to key the two
  non-ACCEPT outcomes. A short connecting brace shows the overlay is a switch on
  the gate verdict.
- Annotation: a 10 pt italic note in the main axis, `Spread is about 0.30 of a
  point across 32 seeded iterations; the gate verdict, not the score, is the
  decision`.
- Legend (main axis, upper right): accept green `iteration (all gates ACCEPT)`,
  hollow diamond `mean`, gray `withheld on non-ACCEPT`.

## Color, symbol, and dash rules

- Iteration points accept green, mean line and diamond near black, range bar
  neutral gray, density outline teal, withheld lane gray with block red and
  escalate amber pips. White figure background, near black text. No dark mode.
- Use `§` in the subtitle (`execution §04`). Use `=` in `gates_all_accepted =
  true` and `composite = null`.
- Single hyphens only. Write the scores as decimals and `32 of 32`; use the word
  `to` for ranges.

## matplotlib implementation directives

- `matplotlib.use("Agg")`; import `matplotlib.pyplot as plt` and `numpy as np`.
- Hardcode the 32 composite values as a list; compute min, max, and mean in the
  script and assert they match 93.417, 93.715, and 93.562 (rounded) as a self
  check.
- Use `np.random.default_rng(20260525)` for the deterministic jitter so the strip
  is reproducible from the project seed.
- Use `ax.scatter`, `ax.axvline`, and `ax.hlines`; draw the density with
  `np.histogram` and `ax.step`.
- Save with `fig.savefig("papers/VVUQ-02/imagegen/08-sweep-composite-stripplot/08-sweep-composite-stripplot.png",
  dpi=300, facecolor="white")`. Do not use `bbox_inches="tight"`.

## Output paths

- Script: `papers/VVUQ-02/imagegen/08-sweep-composite-stripplot/08-sweep-composite-stripplot.py`.
- Image: `papers/VVUQ-02/imagegen/08-sweep-composite-stripplot/08-sweep-composite-stripplot.png`.

## Footer text

`cancer-automated v0.9.0  |  source: execution §04 composite_scores.jsonl, 04-automation README  |  white background, 300 dpi, portrait`

## Per figure acceptance checklist

- Portrait, full page, `figsize=(8.5, 11)`, saved at 300 dpi, white background.
- All 32 iteration points plotted; mean line at 93.562, range bar 93.417 to
  93.715, min and max points labeled.
- The top density marginal and the bottom gating-overlay lane are present, with
  the reported-versus-withheld switch shown.
- Annotation and legend present; the self-check on min, max, mean is stated in the
  instruction so the script can assert it.
- Header, subtitle, legend, and footer inside their bands, no overlap, none
  clipped.
- The section symbol renders as `§`; only single hyphens in visible text; no dark
  mode.
- Script is self contained, uses only matplotlib and numpy, and passes
  `ruff check` and `ruff format --check`.
