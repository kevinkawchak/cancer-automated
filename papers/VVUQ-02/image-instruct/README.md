# VVUQ-02 Image Instructions (v0.9.0)

[![DOI](https://img.shields.io/badge/DOI-Zenodo%20pending-blue.svg)](../../../CITATION.cff)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](../../../LICENSE)
[![Release](https://img.shields.io/badge/Release-v0.9.0-brightgreen.svg)](../../../releases.md)
[![Authored](https://img.shields.io/badge/Authored-May%202026-blue.svg)](../../../CHANGELOG.md)
[![Runner](https://img.shields.io/badge/Runner-Claude%20Code%20Opus%204.7%201M%20Max-purple.svg)](https://claude.com/product/claude-code)
[![Stage](https://img.shields.io/badge/Stage-imagegen%20instructions-blue.svg)](../imagegen)
[![Figures](https://img.shields.io/badge/Figures-15%20portrait%20300%20dpi-brightgreen.svg)](README.md)
[![Backgrounds](https://img.shields.io/badge/Mode-light%20only-lightgrey.svg)](README.md)
[![Basis](https://img.shields.io/badge/Basis-codegen%20v0.7.0%20%2B%20execution%20v0.8.0-orange.svg)](../codegen)

This directory holds 15 comprehensive image instructions for the
`kevinkawchak/cancer-automated` repository. Each instruction is a complete,
self-contained specification that a future agent can turn into one professional,
publication ready figure. The instructions are grounded in the VVUQ-02 code
generation record (v0.7.0, `papers/VVUQ-02/codegen/`) and the VVUQ-02 code
execution record (v0.8.0, `papers/VVUQ-02/execution/`), so every number, label,
and section reference in a figure traces back to a real source file in this
repository.

> Scope. This directory contains instructions only. It contains no generated
> Python script and no rendered image. The matplotlib scripts and the 300 dpi PNG
> files are produced at a future date under `papers/VVUQ-02/imagegen/`, one
> numbered subdirectory per instruction, by following the steps in `## How Claude
> Code Opus 4.7 (1M) Max processes an instruction` below.

> Note on the DOI badge. The repository has no assigned archival DOI yet. The
> badge is a labeled placeholder pointing at `CITATION.cff`. A Zenodo concept DOI
> is expected when a tagged release is archived.

## Project in brief

VVUQ-02 models a 60-second 8-phase pancreaticoduodenectomy (Whipple) performed by
a single autonomous humanoid surgeon, the clearly labeled hypothetical 2030
Unitree H2-Surgical 1.0 (2 x 7-DOF arms, 2 x 20-DOF dexterous hands, 71 total
DOF), with its own two hands and no teleoperation. The deliverable is 10
humanoid-specific VVUQ gates, each a fully specified Verify then Validate then
Quantify gate bound to an independent reference and to published external
standards. The code generation step (v0.7.0) produced the standalone codebase;
the execution step (v0.8.0) ran every entry point, the 172-test suite, the
10-gate decision surface, the 32-iteration sweep, the 4-entrant tournament, and
the full safety surface, and captured the verbatim outputs. This image generation
step (v0.9.0) specifies the publication figures ahead of any rendering.

## Thesis link

The cancer-automated thesis is that the robotic code assurance process, not code
generation, is the substantial and decision bearing part of the AI workflow,
holding VVUQ to a higher standard than code itself. These safety measures will
ensure upcoming physical AI oncology trial deliverables are faster, less
expensive, and more beneficial towards patients than conventional verifications.

These 15 instructions establish the image generation leg of that thesis: each one
specifies, in full and ahead of time, exactly how a figure is to be built and
checked, so the assurance work is done before a single pixel is rendered. That
front loaded specification is the image generation analog of the VVUQ gate. The
figure set is weighted toward the assurance machinery, the 10 gates, their
thresholds, the standards binding, the test budget, and the decision surface,
because that is where the thesis lives.

## How Claude Code Opus 4.7 (1M) Max processes an instruction

Every instruction in this directory is written to be executed by Claude Code Opus
4.7 (1M context) Max with no further questions and no manual positioning. For each
numbered instruction `NN-name`, the agent performs exactly these steps, in order:

1. Read the instruction at `papers/VVUQ-02/image-instruct/NN-name/README.md` in
   full, including its data tables, its layout specification, and its acceptance
   checklist.
2. Read this top level `papers/VVUQ-02/image-instruct/README.md` to load the
   shared page frame, the shared palette, the font sizes, and the symbol and dash
   rules, so the figure matches every other figure in the set.
3. Confirm the grounding values against the cited source files (the v0.7.0
   codegen modules, configs, and results, and the v0.8.0 execution sections and
   artifacts). The instruction lists the exact source path for every number, so
   this is a direct lookup, not an estimate.
4. Author one self contained matplotlib script at
   `papers/VVUQ-02/imagegen/NN-name/NN-name.py`. The script hardcodes the grounded
   values from the instruction as Python literals. It reads no external data file,
   opens no network connection, and depends only on `matplotlib` (and `numpy`,
   which is already a core dependency). It sets a non interactive backend with
   `matplotlib.use("Agg")` so it renders without a display.
5. Build the figure to the shared page frame: portrait, full page,
   `figsize=(8.5, 11)` inches, saved at `dpi=300`, which yields a 2550 by 3300
   pixel image. Use a deterministic layout (an explicit `GridSpec` with the fixed
   figure fraction margins in `## Standard output conventions`) so nothing
   overlaps and the user never has to nudge a box.
6. Render the figure on a white background only. Do not use dark mode for any
   output type. All text is dark on light and clearly legible.
7. Save the image to `papers/VVUQ-02/imagegen/NN-name/NN-name.png` with `dpi=300`
   and `facecolor="white"`. Do not pass `bbox_inches="tight"`, because that would
   crop the canvas away from the fixed full page portrait size.
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
as the v0.8.0 execution run did, and it commits in real time.

## Directory and file naming conventions

The naming is fixed so the instructions, the future scripts, and the future
images line up one to one across the repository.

| Purpose | Exact path |
|---------|------------|
| Instruction (this directory) | `papers/VVUQ-02/image-instruct/NN-name/README.md` |
| Future matplotlib script | `papers/VVUQ-02/imagegen/NN-name/NN-name.py` |
| Future 300 dpi image | `papers/VVUQ-02/imagegen/NN-name/NN-name.png` |

`NN` is the zero padded two digit index from `01` to `15`. `name` is the short
hyphenated slug shown in the index below. The instruction subdirectory and the
imagegen subdirectory share the identical `NN-name` so a reader can move between
the specification and the rendered output without guessing.

## Standard output conventions

These conventions are shared by all 15 instructions. Each instruction restates
the specific colors and data it uses, but the frame, the fonts, the symbols, and
the dash rules below are common, so the 15 figures form one coherent set.

### Page frame (portrait, full size)

- Orientation portrait, full page. `fig = plt.figure(figsize=(8.5, 11))`.
- Resolution 300 dpi on save, giving 2550 by 3300 pixels.
- Background white only, no dark mode. `fig.savefig(path, dpi=300,
  facecolor="white")`, and axes face color white or the light panel fill below.
- Reserved bands, expressed as figure fractions, so every figure aligns: header
  band `y` in `[0.93, 1.00]`, content band `y` in `[0.07, 0.91]`, footer band `y`
  in `[0.00, 0.06]`, left margin `x = 0.06`, right margin `x = 0.94`.
- Place the content with an explicit `GridSpec(..., left=0.06, right=0.94,
  top=0.91, bottom=0.07)` so the layout is deterministic. Put the header title
  with `fig.text(0.5, 0.965, ...)` centered, the optional subtitle at `y = 0.935`,
  and the footer at `y = 0.03`. Do not rely on `bbox_inches="tight"`.

### Typography

- Font family `DejaVu Sans` (the matplotlib default, always present, no install).
- Title 20 pt bold, subtitle 12.5 pt regular, panel or section headers 14 pt
  bold, body and data labels 11 pt, small annotations and the footer 9 pt.
- Text color `#1A1A1A` near black for all body text on white, so contrast is high
  and every label is clearly visible against the white background.

### Shared professional palette

Use these hex values by role so color carries consistent meaning across the set.
The palette is calm, professional, and prints cleanly on white.

| Role | Hex | Used for |
|------|-----|----------|
| Primary navy | `#1F3A5F` | primary structures, baselines, headers |
| Slate blue | `#4C72B0` | secondary structures, neutral series, left hand |
| Teal | `#2A9D8F` | process flow, automation, positive movement, right hand |
| Accept green | `#2E7D32` | accepted, passed, shippable, within bound |
| Block red | `#C0392B` | blocked, failed, over budget, breach |
| Escalate amber | `#E1A93B` | escalated to human, caution, gate, soft warning |
| Autonomy purple | `#6A4C93` | on-prem LLM intent, autonomy, lineage |
| Clinical rose | `#B5566E` | clinical baselines, patient framing |
| Neutral gray | `#6B7280` | connectors, idle state, secondary text |
| Panel fill | `#F4F6F8` | light card and panel backgrounds |
| Gridline gray | `#D9DEE3` | gridlines and thin separators |
| Near black | `#1A1A1A` | all primary text |

When a figure needs a sequential scale (for example the test coverage treemap or
the binding matrix), derive it from the teal to navy range so it stays inside the
family. The three immediate-catastrophe gates (06 vascular no-fly, 09 shared-OR
collision, 10 fault e-stop) are consistently flagged with the block red accent so
they read the same in every figure.

### Symbols and dashes

- Render the section symbol as `§` (U+00A7) wherever a figure references a paper
  section, an execution section, or a regulatory clause, for example `execution
  §03`, `ASME V&V 40 §8`, or `IEC 80601-2-77 §201.x`. Never spell it as `SS` or
  `Section` in the rendered text where the symbol is intended.
- Use single hyphens only in any visible text. Do not use em dashes, en dashes,
  double dashes, or triple dashes in titles, labels, annotations, legends,
  headers, or footers.
- Use a normal multiplication style `x` for factors, for example `2.5x`, and the
  word `to` for ranges in prose labels, for example `38 to 43 mm`.

### Footer (every figure)

Each figure carries the same footer style at `y = 0.03`, 9 pt, neutral gray:
`cancer-automated v0.9.0  |  source: <grounding paths>  |  white background, 300
dpi, portrait`. The grounding paths are listed in each instruction.

## The 15 image instructions

Each row is delivered in its own commit. Basis says whether the figure is
grounded in code generation (v0.7.0), code execution (v0.8.0), or both. The
required-data column marks the six figures that the data availability brief
requires (R1 to R6). No instruction specifies a basic bar, pie, donut, or basic
line chart; where a bar like element appears it is part of a richer, planned
composition (a waterfall, a forest plot, a strip plot, or a financial bridge).

| No. | Instruction subdirectory | Chart family | Basis | Required data |
|-----|--------------------------|--------------|-------|---------------|
| 01 | `01-platform-pipeline-flow` | Workflow / pipeline flow diagram | both | - |
| 02 | `02-vvuq-gate-decision-funnel` | Funnel | both | - |
| 03 | `03-ten-gate-threshold-forest` | Forest plot | both | R3 (10 gates and thresholds) |
| 04 | `04-gate-standard-binding-matrix` | Heatmap / matrix | both | R2 (external standards anchored) |
| 05 | `05-clinical-regulatory-standards-wheel` | Wheel diagram | codegen | R4 (clinical and regulatory) |
| 06 | `06-test-coverage-treemap` | Treemap | execution | R1 (172 tests) |
| 07 | `07-validation-parity-scatter` | Scatter / parity plot | both | - |
| 08 | `08-sweep-composite-stripplot` | Dot / strip plot | execution | - |
| 09 | `09-composite-weighting-waterfall` | Waterfall | both | - |
| 10 | `10-four-entrant-comparison-violin` | Box / violin plot | both | R6 (4-entrant comparison) |
| 11 | `11-sensor-stream-safety-bands` | Line plot with uncertainty bands | both | R5 (1000-row sensor) |
| 12 | `12-eight-phase-whipple-swimmer` | Swimmer plot | both | - |
| 13 | `13-assurance-cost-assessment` | Financial assessment | both | - |
| 14 | `14-value-proposition-matrix` | Value proposition matrix | both | - |
| 15 | `15-platform-mindmap` | Mind map | both | - |

The 15 chart families are all distinct (no figure type is reused), chosen from
the 20-family menu for best data availability and relevance. The five families
not used are the basic grouped bar, the pie or donut, the duplicate
scatter-regression family (folded into instruction 07), the Kaplan-Meier survival
curve, and the ROC curve; the last two are omitted because VVUQ-02 carries no
time-to-event or labeled-classifier ground truth to ground them honestly.

### Data availability mapping (six required figures)

| Tag | Requirement | Figure | Primary source |
|-----|-------------|--------|----------------|
| R1 | Include the 172 tests | 06 test coverage treemap | `execution/01-foundation/test-suite.md` |
| R2 | External standards anchored throughout | 04 gate-standard binding matrix | `execution/02-pipeline/`, `execution/03-vvuq/`, `execution/05-humanoid-deployment/` |
| R3 | The 10 gates and their thresholds | 03 ten-gate threshold forest | `execution/03-vvuq/` |
| R4 | Clinical external standards and regulatory relevancies | 05 clinical and regulatory standards wheel | `inputs/` and its `standards/` and `clinical/` subdirectories |
| R5 | Feature the 1000-row H2 sensor data | 11 sensor stream safety bands | `codegen/data/sample_h2_sensor.csv` |
| R6 | 2nd place mobile humanoid, 4 competitors | 10 four-entrant comparison violin | `codegen/results/comparison.json` |

## Grounding sources

The instructions cite these source files directly.

Code generation (v0.7.0), under `papers/VVUQ-02/codegen/`:

- `config/project.yaml` (frozen scope, 71-DOF platform, 8-phase timeline, the
  6-component composite weights), `config/vvuq_thresholds.yaml` (the 10 gate
  threshold blocks), and `config/standards_map.yaml` (the gate to standard map).
- `results/comparison.json` and `results/comparison_report.md` (the 1790-line,
  four-entrant tournament and the leaderboard).
- `data/sample_h2_sensor.csv` (the featured 1000-row, 27-column positional sensor
  stream).
- `src/` modules and `tests/` (the 15 test modules, 172 tests).

Code execution (v0.8.0), under `papers/VVUQ-02/execution/`:

- `01-foundation/test-suite.md` (172 tests across 15 modules).
- `02-pipeline/README.md` and `artifacts/pipeline_execution_log.txt` (intent to
  compile to act to score; the external standards anchored here table).
- `03-vvuq/README.md`, `artifacts/vvuq_decisions.json`, `artifacts/vvuq_report.md`
  (the 10-gate thresholds, the decision surface, the resolved standards).
- `04-automation/README.md`, `artifacts/composite_scores.jsonl`,
  `artifacts/comparison_analysis.txt`, `artifacts/comparison_leaderboard.md`.
- `05-humanoid-deployment/README.md`, `artifacts/eight_phase_timeline.txt`,
  `artifacts/sensor_stream_analysis.txt`, `artifacts/deployment_safety_log.txt`.
- `README.md` (the execution results summary, the file-generation outcomes, and
  the this-run-versus-conventional comparison).

The wired external-standards corpus under `papers/VVUQ-02/inputs/standards/` and
the clinical baselines under `papers/VVUQ-02/inputs/clinical/` ground the wheel
(instruction 05) and the binding matrix (instruction 04).

## Repository structure (this directory and its future outputs)

```
papers/VVUQ-02/
+-- image-instruct/                       (this directory, v0.9.0 instructions)
|   +-- README.md                         (this file: conventions and 15-spec index)
|   +-- prompt-image-instruct.md          (the generating prompt, verbatim)
|   +-- output-image-instruct.md          (the narrative markdown output of this run)
|   +-- 01-platform-pipeline-flow/README.md
|   +-- 02-vvuq-gate-decision-funnel/README.md
|   +-- 03-ten-gate-threshold-forest/README.md
|   +-- 04-gate-standard-binding-matrix/README.md
|   +-- 05-clinical-regulatory-standards-wheel/README.md
|   +-- 06-test-coverage-treemap/README.md
|   +-- 07-validation-parity-scatter/README.md
|   +-- 08-sweep-composite-stripplot/README.md
|   +-- 09-composite-weighting-waterfall/README.md
|   +-- 10-four-entrant-comparison-violin/README.md
|   +-- 11-sensor-stream-safety-bands/README.md
|   +-- 12-eight-phase-whipple-swimmer/README.md
|   +-- 13-assurance-cost-assessment/README.md
|   +-- 14-value-proposition-matrix/README.md
|   +-- 15-platform-mindmap/README.md
+-- imagegen/                             (future v-next: scripts + PNGs, one per NN-name)
    +-- NN-name/NN-name.py                (future self-contained matplotlib script)
    +-- NN-name/NN-name.png               (future portrait, 300 dpi, white background)
```

```
  image-instruct/NN-name/         imagegen/NN-name/             imagegen/NN-name/
  +----------------------+        +----------------------+      +-------------------+
  | README.md            |  -->   | NN-name.py           |  --> | NN-name.png       |
  | full figure spec     |  spec  | self-contained       | run  | portrait, 300 dpi |
  | (data, layout, color,| =====> | matplotlib + numpy,  | ===> | white background, |
  |  page frame, paths)  |        | hardcoded grounded   |      | full size, aligned|
  |  v0.9.0 instructions |        | values, ruff clean   |      | no positioning    |
  +----------------------+        +----------------------+      +-------------------+
        assurance specification  ----------------->  rendered figure (future)
```

## Future imagegen workflow and dependency note

When these instructions are executed, the future scripts use `matplotlib`. The
core CI does not install `matplotlib`, and that is fine: the `lint-and-format` job
only runs `ruff` and `yamllint` statically, and the `test` job does not import
`imagegen/`, so the future scripts keep CI green as long as they are ruff clean.
Rendering the PNG files requires `matplotlib` to be installed in the environment
that runs imagegen. Add it there with `pip install matplotlib` (it pulls in
`numpy`, already a core dependency). The scripts must remain pure `matplotlib`
plus `numpy` so they reproduce without any heavy or networked backend.

This v0.9.0 image-instruct pull request adds only Markdown files, so it carries no
Python or YAML and cannot introduce a `ruff` or `yamllint` failure. The
`lint-and-format`, `validate-scripts`, and `test` CI jobs stay green across Python
3.10, 3.11, and 3.12.

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
- Output paths are exactly `papers/VVUQ-02/imagegen/NN-name/NN-name.py` and
  `papers/VVUQ-02/imagegen/NN-name/NN-name.png`.

## File generation outcomes (basis for a future technical paper)

This image-instruct set produces 18 Markdown files: this README, the two lineage
files (`prompt-image-instruct.md`, `output-image-instruct.md`), and the 15 figure
specifications. Each figure maps to the section of a future technical paper it can
illustrate, so the set doubles as a figure plan for that paper.

| Figure | Chart family | Future paper role |
|--------|--------------|-------------------|
| 01 platform pipeline flow | Workflow diagram | Methods: the generation to assurance pipeline |
| 02 VVUQ gate decision funnel | Funnel | Core Results: the assurance filter (thesis) |
| 03 ten-gate threshold forest | Forest plot | Methods: the 10 gates and their thresholds |
| 04 gate-standard binding matrix | Heatmap | Methods: external-standards credibility basis |
| 05 clinical and regulatory wheel | Wheel | Background: clinical and regulatory grounding |
| 06 test coverage treemap | Treemap | Verification: the 172-test budget |
| 07 validation parity scatter | Parity plot | Results: validation against independent references |
| 08 sweep composite strip plot | Strip plot | Results: the 32-iteration sweep stability |
| 09 composite weighting waterfall | Waterfall | Methods: the gated composite score model |
| 10 four-entrant comparison violin | Violin plot | Results: the humanoid versus the field |
| 11 sensor stream safety bands | Line with bands | Results: the featured positional sensor stream |
| 12 eight-phase Whipple swimmer | Swimmer plot | Methods: the 60-second deployment reference |
| 13 assurance cost assessment | Financial bridge | Discussion: faster and less expensive |
| 14 value proposition matrix | Value matrix | Discussion: value to the trial and the patient |
| 15 platform mind map | Mind map | Overview: the whole VVUQ-02 platform |

Together the 15 figures form a Methods plus Results plus Discussion figure
skeleton: the pipeline, gates, thresholds, standards, and tests document the
method; the parity, sweep, composite, comparison, sensor, and swimmer figures
document the results; and the cost, value, and mind map figures frame the
discussion and the overview.

## Consistency and error-fix pass

All 15 instructions were cross checked as a set before release (commit 16). The
pass confirmed:

- Arithmetic reconciles. The treemap test counts sum to 172 across 15 modules
  (64 + 12 + 11 + 11 + 9 + 9 + 8 + 8 + 8 + 7 + 7 + 6 + 5 + 4 + 3); the composite
  weight waterfall sums to 1.00 (0.30 + 0.20 + 0.15 + 0.15 + 0.05 + 0.15); the
  8-phase swimmer durations sum to 60 s (6 + 10 + 8 + 8 + 10 + 6 + 6 + 6); the
  funnel narrows through verify, validate, quantify, and the hard predicate; the
  four-entrant violin uses the per-entrant dispersion (PancreSpeed n=64, H2 n=96,
  da Vinci n=64, Dutch n=32) that sums to 256 entrant-appearances over 128
  verdicts.
- Grounding matches the source files. Every number traces to a cited v0.7.0
  config, result, or data file, or a v0.8.0 execution section or artifact,
  including the 10 gate thresholds, the 5-case decision surface, the leaderboard
  (93.782, 93.334, 83.970, 67.885), the sweep composite (min 93.417, max 93.715,
  mean 93.562), and the 1000-row sensor channel ranges.
- Symbols and dashes are clean. The section symbol renders as `§` (for example
  `execution §03` and `ASME V&V 40 §8`), no em dashes, en dashes, or prose double
  dashes appear, and triple dashes occur only in Markdown table separators.
- Naming is one to one. Each instruction `NN-name` maps to
  `papers/VVUQ-02/imagegen/NN-name/NN-name.py` and `.png`, and every figure uses
  the shared portrait page frame, 300 dpi, white background, and palette.

## Responsible use

These figures describe an automated assurance platform and a hypothetical 2030
humanoid deployment reference. They are planning and documentation artifacts.
Generated instructions, code, images, and papers are drafts: the 10 VVUQ gates
plus a recorded human reviewer must clear any deliverable before clinical use. The
H2-Surgical 1.0 is a clearly labeled hypothetical 2030 platform and every number
is a simulation result; the comparison is simulation against simulation.
Deployment would require IEC 80601-2-77, IEC 60601, ISO 13482, FDA SaMD Class III
clearance, IRB approval, and regulatory authorization. Only
`kevinkawchak/cancer-automated` is edited by this work.
