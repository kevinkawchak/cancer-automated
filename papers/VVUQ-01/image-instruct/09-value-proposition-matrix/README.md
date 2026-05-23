# Image Instruction 09: Value Proposition Matrix

Chart family: 2 by 2 strategic positioning matrix with a structured better,
different, worse summary. Basis: code execution (v0.2.0 execution README, the
comparison of this autonomous cloud run with conventional high-end server
processing). Output: a single portrait, full page, 300 dpi PNG.

Read the shared conventions in `papers/VVUQ-01/image-instruct/README.md` first,
then build exactly what is specified below.

## Purpose and message

The figure positions the autonomous cloud run against a conventional high-end
workstation or server on two axes that matter for this work, then summarizes the
honest tradeoff. The message is the net finding from the execution record: for
executing, verifying, and documenting a standard library codebase under strict
assurance, the autonomous cloud run was faster, cheaper, and more reproducible;
for exercising live model, network, and physics backends, a provisioned server
does more.

## Grounding (cite in the footer)

- `papers/VVUQ-01/execution/README.md`, the section `This execution versus
  conventional high-end server processing`, for every better, different, and
  worse point and the net verdict (code execution v0.2.0).

## The two positioned approaches

Axes: horizontal `Cost and setup efficiency` from low to high, vertical `Live
backend capability` from low to high.

| Approach | Cost and setup efficiency | Live backend capability | Quadrant |
|----------|---------------------------|-------------------------|----------|
| Autonomous cloud run, Claude Code Opus 4.7 1M | high | low to medium | lower right |
| Conventional high-end server or workstation | low to medium | high | upper left |

Quadrant labels: lower right `Fast, cheap, reproducible assurance`; upper left
`Full live backends, heavier setup`; upper right `Ideal future target, both at
once`; lower left `Manual and unassured baseline`.

## The structured summary (exact points)

| Better, autonomous cloud | Different | Worse |
|--------------------------|-----------|-------|
| Near zero setup, ran before any heavy install | Ephemeral and commit driven, nothing persists unless pushed | No live heavy backends, no agentic model, web, PDF, or physics |
| One integrated loop, run, observe, document, lint, commit | Real time per section commits, a finer granularity | No display or GPU, no Isaac Sim, no graphics, no LaTeX render |
| Systematic assurance beyond the shipped tests, surfaced the multibyte limitation | Cross version testing delegated to the CI matrix | No persistent caches, each session starts cold |
| Self verifying documentation, every command and output recorded | | |

Net verdict to render as a banner: `Net: faster, cheaper, and more reproducible
for standard library assurance; a provisioned server does more for live model,
network, and physics backends`.

## Layout specification (portrait, full page)

Use the shared page frame with three stacked regions. `GridSpec(3, 1,
height_ratios=[2.0, 1.6, 0.4], left=0.07, right=0.93, top=0.90, bottom=0.07,
hspace=0.26)`.

- Header at `y = 0.965`: `Value Proposition Matrix`. Subtitle at `y = 0.935`:
  `Autonomous cloud run versus conventional high-end server`.
- Top region, the 2 by 2 matrix:
  - Draw the four quadrants as light rectangles on the content axis, the upper
    right quadrant tinted a faint accept green to mark the ideal target, the
    others on panel fill `#F4F6F8`. Draw the two axes as arrowed lines through the
    center with axis titles `Cost and setup efficiency, low to high` along the
    bottom and `Live backend capability, low to high` up the left.
    Label each quadrant in 10 pt at its corner.
  - Plot the autonomous cloud run as a teal `#2A9D8F` rounded marker in the lower
    right quadrant and the conventional server as a slate blue `#4C72B0` rounded
    marker in the upper left quadrant, each with a 10.5 pt label and a short
    descriptor.
- Middle region, three summary columns:
  - Three equal cards side by side. The Better card has an accept green `#2E7D32`
    header bar, the Different card a slate blue `#4C72B0` header bar, the Worse
    card an escalate amber `#E1A93B` header bar. Card bodies on panel fill.
  - List the grounded points as 9.5 pt bulleted lines, wrapped to the card width
    so nothing overflows. The Better card has four points, Different three, Worse
    three.
- Bottom region, the verdict banner: a full width primary navy `#1F3A5F` bar with
  the net verdict in white 11 pt, centered.

## Color, symbol, and dash rules

- Cloud marker teal, server marker slate blue, ideal quadrant faint accept green,
  Better green header, Different slate header, Worse amber header, verdict banner
  navy with white text, panel fill cards, near black text elsewhere. White
  background, no dark mode.
- No section symbol required. Single hyphens only in visible text; write
  `high-end`, `Near zero`, `commit driven` with single hyphens where natural and
  no em dashes.

## matplotlib implementation directives

- `matplotlib.use("Agg")`; `matplotlib.pyplot as plt`; from `matplotlib.patches`
  import `Rectangle`, `FancyBboxPatch`, `FancyArrowPatch`.
- Place quadrant rectangles and markers in fixed axis coordinates so the matrix is
  deterministic; wrap card text with `textwrap.fill` to the card width so the
  three columns stay aligned and no bullet overflows.
- Save to `papers/VVUQ-01/imagegen/09-value-proposition-matrix/09-value-proposition-matrix.png`
  with `dpi=300, facecolor="white"`, no `bbox_inches="tight"`.

## Output paths

- Script: `papers/VVUQ-01/imagegen/09-value-proposition-matrix/09-value-proposition-matrix.py`.
- Image: `papers/VVUQ-01/imagegen/09-value-proposition-matrix/09-value-proposition-matrix.png`.

## Footer text

`cancer-automated v0.3.0  |  source: execution README, autonomous cloud versus conventional server  |  white background, 300 dpi, portrait`

## Per figure acceptance checklist

- Portrait, full page, `figsize=(8.5, 11)`, saved at 300 dpi, white background.
- 2 by 2 matrix with labeled axes and four quadrant labels; the cloud run sits
  lower right and the conventional server upper left.
- Three summary cards with the exact better, different, and worse points; the
  verdict banner reads as specified.
- Header, subtitle, and footer inside their bands, nothing clipped or
  overflowing.
- Only single hyphens in visible text; no dark mode.
- Script self contained, only matplotlib and numpy, passes `ruff check` and
  `ruff format --check`.
