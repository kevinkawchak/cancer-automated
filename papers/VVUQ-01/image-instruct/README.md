# VVUQ-01 Image Instructions (v0.3.0)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](../../../LICENSE)
[![Release](https://img.shields.io/badge/Release-v0.3.0-brightgreen.svg)](../../../releases.md)
[![Authored](https://img.shields.io/badge/Authored-May%202026-blue.svg)](../../../CHANGELOG.md)
[![Runner](https://img.shields.io/badge/Runner-Claude%20Code%20Opus%204.7%201M%20Max-purple.svg)](https://claude.com/product/claude-code)
[![Stage](https://img.shields.io/badge/Stage-imagegen%20instructions-blue.svg)](../imagegen)
[![Outputs](https://img.shields.io/badge/Images-10%20portrait%20300%20dpi-brightgreen.svg)](README.md)
[![Backgrounds](https://img.shields.io/badge/Mode-light%20only-lightgrey.svg)](README.md)

This directory holds 10 comprehensive image instructions for the
`kevinkawchak/cancer-automated` repository. Each instruction is a complete,
self-contained specification that a future agent can turn into one professional,
publication ready figure. The instructions are grounded in the code generation
record (v0.1.0) and the code execution record (v0.2.0), so every number, label,
and section reference in a figure traces back to a real source file in this
repository.

> Scope. This directory contains instructions only. It does not contain any
> generated Python script and it does not contain any rendered image. The
> matplotlib scripts and the 300 dpi PNG files are produced at a future date
> under `papers/VVUQ-01/imagegen/`, one numbered subdirectory per instruction,
> by following the steps in `## How Claude Code Opus 4.7 (1M) Max processes an
> instruction` below.

## Thesis link

The cancer-automated thesis is that the LLM VVUQ process must be more
substantial than the generated artifact itself across code generation, image
generation, and paper generation, accomplished faster and less expensively than
current verification methods. v0.1.0 implemented code generation and paper
generation; v0.2.0 executed and verified them. These instructions establish the
image generation leg: each one specifies, in full and ahead of time, exactly how
a figure is to be built and checked, so the assurance work is done before a
single pixel is rendered. That front loaded specification is the image
generation analog of the VVUQ gate.

## What a reader gets from this set

The 10 figures cover the established methods, the assurance machinery, the Stage
1 automation, the Stage 2 2030 PDAC reference, and the value and financial case,
using professional and effective chart families rather than basic bar, pie, or
line charts. The index in `## The 10 image instructions` maps each instruction
to its chart family and its grounding.

## How Claude Code Opus 4.7 (1M) Max processes an instruction

Every instruction in this directory is written to be executed by Claude Code
Opus 4.7 (1M context) Max with no further questions and no manual positioning.
For each numbered instruction `NN-name`, the agent performs exactly these steps,
in order:

1. Read the instruction at `papers/VVUQ-01/image-instruct/NN-name/README.md` in
   full, including its data tables, its layout specification, and its acceptance
   checklist.
2. Read this top level `papers/VVUQ-01/image-instruct/README.md` to load the
   shared page frame, the shared palette, the font sizes, and the symbol and
   dash rules, so the figure matches every other figure in the set.
3. Confirm the grounding values against the cited source files (the v0.1.0
   modules and configs and the v0.2.0 execution sections). The instruction lists
   the exact source path for every number, so this is a direct lookup, not an
   estimate.
4. Author one self contained matplotlib script at
   `papers/VVUQ-01/imagegen/NN-name/NN-name.py`. The script hardcodes the
   grounded values from the instruction as Python literals. It reads no external
   data file, opens no network connection, and depends only on `matplotlib`
   (and `numpy`, which is already a core dependency). It sets a non interactive
   backend with `matplotlib.use("Agg")` so it renders without a display.
5. Build the figure to the shared page frame: portrait, full page, `figsize=(8.5,
   11)` inches, saved at `dpi=300`, which yields a 2550 by 3300 pixel image. Use
   a deterministic layout (an explicit `GridSpec` with the fixed figure fraction
   margins in `## Standard output conventions`) so nothing overlaps and the user
   never has to nudge a box.
6. Render the figure on a white background only. Do not use dark mode for any
   output type. All text is dark on light and clearly legible.
7. Save the image to `papers/VVUQ-01/imagegen/NN-name/NN-name.png` with
   `dpi=300` and `facecolor="white"`. Do not pass `bbox_inches="tight"`, because
   that would crop the canvas away from the fixed full page portrait size.
8. Verify the result against the instruction acceptance checklist: portrait and
   full size, every label present and aligned, the legend and the header and the
   footer inside their reserved bands, the section symbol rendered as `§` where
   required, and only single hyphens used in any visible text.
9. Confirm the new script passes `ruff check` and `ruff format --check` under the
   repository `ruff.toml`, so adding it later keeps the `lint-and-format` CI job
   green across Python 3.10, 3.11, and 3.12.
10. Commit the script and the PNG together for that instruction, then continue to
    the next one.

The agent works one instruction at a time so its context stays focused, exactly
as the v0.2.0 execution run did, and it commits in real time.

## Directory and file naming conventions

The naming is fixed so the instructions, the future scripts, and the future
images line up one to one across the repository.

| Purpose | Exact path |
|---------|------------|
| Instruction (this directory) | `papers/VVUQ-01/image-instruct/NN-name/README.md` |
| Future matplotlib script | `papers/VVUQ-01/imagegen/NN-name/NN-name.py` |
| Future 300 dpi image | `papers/VVUQ-01/imagegen/NN-name/NN-name.png` |

`NN` is the zero padded two digit index from `01` to `10`. `name` is the short
hyphenated slug shown in the index below. The instruction subdirectory and the
imagegen subdirectory share the identical `NN-name` so a reader can move between
the specification and the rendered output without guessing.

## Standard output conventions

These conventions are shared by all 10 instructions. Each instruction restates
the specific colors and data it uses, but the frame, the fonts, the symbols, and
the dash rules below are common, so the 10 figures form one coherent set.

### Page frame (portrait, full size)

- Orientation portrait, full page. `fig = plt.figure(figsize=(8.5, 11))`.
- Resolution 300 dpi on save, giving 2550 by 3300 pixels.
- Background white only, no dark mode. `fig.savefig(path, dpi=300,
  facecolor="white")`, and axes face color white or the light panel fill below.
- Reserved bands, expressed as figure fractions, so every figure aligns:
  header band `y` in `[0.93, 1.00]`, content band `y` in `[0.07, 0.91]`, footer
  band `y` in `[0.00, 0.06]`, left margin `x = 0.06`, right margin `x = 0.94`.
- Place the content with an explicit `GridSpec(..., left=0.06, right=0.94,
  top=0.91, bottom=0.07)` so the layout is deterministic. Put the header title
  with `fig.text(0.5, 0.965, ...)` centered, the optional subtitle at `y =
  0.935`, and the footer at `y = 0.03`. Do not rely on `bbox_inches="tight"`.

### Typography

- Font family `DejaVu Sans` (the matplotlib default, always present, no install).
- Title 20 pt bold, subtitle 12.5 pt regular, panel or section headers 14 pt
  bold, body and data labels 11 pt, small annotations and the footer 9 pt.
- Text color `#1A1A1A` near black for all body text on white, so contrast is
  high and every label is clearly visible.

### Shared professional palette

Use these hex values by role so color carries consistent meaning across the set.
The palette is calm, professional, and prints cleanly on white.

| Role | Hex | Used for |
|------|-----|----------|
| Primary navy | `#1F3A5F` | primary structures, baselines, headers |
| Slate blue | `#4C72B0` | secondary structures, neutral series |
| Teal | `#2A9D8F` | process flow, automation, positive movement |
| Accept green | `#2E7D32` | accepted, passed, shippable |
| Block red | `#C0392B` | blocked, failed, over budget |
| Escalate amber | `#E1A93B` | escalated to human, caution, gate |
| Neutral gray | `#6B7280` | connectors, idle state, secondary text |
| Panel fill | `#F4F6F8` | light card and panel backgrounds |
| Gridline gray | `#D9DEE3` | gridlines and thin separators |
| Near black | `#1A1A1A` | all primary text |

When a figure needs a sequential scale (for example the test coverage treemap),
derive it from the teal to navy range so it stays inside the family.

### Symbols and dashes

- Render the section symbol as `§` (U+00A7) wherever a figure references a paper
  section or a regulatory section, for example `FDA §VI.B` or `Validation §4.5`.
  Never spell it as `SS` or `Section` in the rendered text where the symbol is
  intended.
- Use single hyphens only in any visible text. Do not use em dashes, en dashes,
  double dashes, or triple dashes in titles, labels, annotations, legends,
  headers, or footers.
- Use a normal multiplication style `x` for factors, for example `2.5x`, and the
  word `to` for ranges in prose labels, for example `30 to 12 days`.

### Footer (every figure)

Each figure carries the same footer style at `y = 0.03`, 9 pt, neutral gray:
`cancer-automated v0.3.0  |  source: <grounding paths>  |  white background, 300
dpi, portrait`. The grounding paths are listed in each instruction.

## The 10 image instructions

Each row is delivered in its own commit. Basis says whether the figure is
grounded in code generation (v0.1.0), code execution (v0.2.0), or both.

| No. | Instruction subdirectory | Chart family | Basis | Future script and image |
|-----|--------------------------|--------------|-------|--------------------------|
| 01 | `01-vvuq-gate-funnel` | Funnel | both | `imagegen/01-vvuq-gate-funnel/01-vvuq-gate-funnel.{py,png}` |
| 02 | `02-acceleration-waterfall` | Waterfall (schedule) | both | `imagegen/02-acceleration-waterfall/02-acceleration-waterfall.{py,png}` |
| 03 | `03-five-methods-flowchart` | Process flowchart and swimlane | both | `imagegen/03-five-methods-flowchart/03-five-methods-flowchart.{py,png}` |
| 04 | `04-vvuq-assurance-wheel` | Radar wheel | both | `imagegen/04-vvuq-assurance-wheel/04-vvuq-assurance-wheel.{py,png}` |
| 05 | `05-pdac-pilot-timeline` | Gantt timeline | both | `imagegen/05-pdac-pilot-timeline/05-pdac-pilot-timeline.{py,png}` |
| 06 | `06-test-coverage-treemap` | Treemap | execution | `imagegen/06-test-coverage-treemap/06-test-coverage-treemap.{py,png}` |
| 07 | `07-lights-off-state-machine` | State diagram | both | `imagegen/07-lights-off-state-machine/07-lights-off-state-machine.{py,png}` |
| 08 | `08-fda-cost-efficiency-bridge` | Financial bridge and bullet | both | `imagegen/08-fda-cost-efficiency-bridge/08-fda-cost-efficiency-bridge.{py,png}` |
| 09 | `09-value-proposition-matrix` | Value proposition matrix | execution | `imagegen/09-value-proposition-matrix/09-value-proposition-matrix.{py,png}` |
| 10 | `10-file-generation-sankey` | Sankey flow | both | `imagegen/10-file-generation-sankey/10-file-generation-sankey.{py,png}` |

No instruction specifies a basic bar chart, a basic pie chart, or a basic line
chart. Where a bar like element appears (for example inside the waterfall or the
bullet assessment) it is part of a richer, planned composition, not a standalone
basic chart.

## Grounding sources

The instructions cite these source files directly.

Code generation (v0.1.0):

- `pipeline/` modules and `pipeline/README.md` (five established methods).
- `vvuq/` modules and `vvuq/README.md`, plus `configs/vvuq_thresholds.yaml`.
- `simulation/`, `ingestion/`, `chunking/`, `scheduler/`, and
  `configs/pipeline_config.yaml`.
- `physical-ai/` modules and `physical-ai/README.md`.

Code execution (v0.2.0), under `papers/VVUQ-01/execution/`:

- `01-foundation/test-suite.md` and `01-foundation/lint-format-yaml.md`.
- `02-pipeline/README.md` and its `artifacts/`.
- `03-vvuq/README.md` (the full gate decision surface).
- `04-stage1-automation/README.md` and its `artifacts/`.
- `05-physical-ai-stage2/README.md` and
  `05-physical-ai-stage2/artifacts/pdac_hybrid_pilot_timeline.txt`.
- `papers/VVUQ-01/execution/README.md` (results summary and file outcomes).

Selected qualitative grounding for the financial and credibility figure draws on
the input corpus under `papers/VVUQ-01/inputs/`, which references 117 distinct
external DOIs.

## Future imagegen workflow and dependency note

When these instructions are executed, the future scripts use `matplotlib`. The
core CI does not install `matplotlib`, and that is fine: the `lint-and-format`
job only runs `ruff` and `yamllint` statically, and the `test` job does not
import `imagegen/`, so the future scripts keep CI green as long as they are ruff
clean. Rendering the PNG files requires `matplotlib` to be installed in the
environment that runs imagegen. Add it there with `pip install matplotlib` (it
pulls in `numpy`, already a core dependency). The scripts must remain pure
`matplotlib` plus `numpy` so they reproduce without any heavy or networked
backend.

## Global acceptance criteria

A rendered figure is accepted only when all of the following hold. Each
instruction repeats this as a per figure checklist.

- Portrait orientation, full page, `figsize=(8.5, 11)`, saved at 300 dpi.
- White background only, no dark mode, dark legible text throughout.
- Header title, optional subtitle, content, legend, and footer each sit inside
  their reserved bands with no overlap and no clipping.
- Every number and label traces to a cited source in this repository.
- The section symbol renders as `§` where required, and only single hyphens
  appear in visible text.
- The script is self contained, uses only `matplotlib` and `numpy`, and passes
  `ruff check` and `ruff format --check`.
- Output paths are exactly `papers/VVUQ-01/imagegen/NN-name/NN-name.py` and
  `papers/VVUQ-01/imagegen/NN-name/NN-name.png`.

## Responsible use

These figures describe an automated assurance platform and a Stage 2 deployment
reference. They are planning and documentation artifacts. Generated
instructions, code, images, and papers are drafts: a VVUQ gate and a human
reviewer must clear any deliverable before clinical use. The Stage 2 references
require VVUQ clearance, human oversight, IRB approval, and regulatory
authorization before any real use.
