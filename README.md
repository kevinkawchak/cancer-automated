# Production Automated Physical AI Oncology Trial Daily Deliverables

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Release](https://img.shields.io/badge/Release-v0.6.0-brightgreen.svg)](releases.md)
[![Last Updated](https://img.shields.io/badge/Updated-May%202026-blue.svg)](CHANGELOG.md)
[![Python](https://img.shields.io/badge/Python-3.10%20|%203.11%20|%203.12-blue.svg)](https://www.python.org/)
[![Protocol](https://img.shields.io/badge/Protocol-MCP-purple.svg)](https://modelcontextprotocol.io/)
[![CI](https://img.shields.io/badge/CI-lint%20and%20format-blue.svg)](.github/workflows/ci.yml)
[![Contributors](https://img.shields.io/badge/Contributors-4-blue.svg)](releases.md)

**Production-ready, scalable automation for Physical AI oncology trial daily deliverables, by Claude Code Opus 4.7, Cowork; building on developments proven across physical-ai-oncology-trials, robotic-surgeries, and Clinical-AI-Demos.**

This repository packages the established methods for generating instructions, generating code, executing code, and creating papers into a single repeatable daily-deliverable pipeline. It then layers verification, validation, and uncertainty quantification (VVUQ), triple simulation, robust web, and PDF ingestion.

> **Thesis.** Production-ready, scalable, and automated Physical AI oncology trial daily deliverables are obtained based on established methods for generating instructions, code, code execution, and creating papers, and are further automated, accelerated, and the VVUQ is improved.

**5/25: v0.6.0 (VVUQ-01 Full Paper)** Adds [papers/VVUQ-01/full-paper](papers/VVUQ-01/full-paper): the full manuscript built from the v0.5.0 draft scaffold without modifying it. Every bracketed processing instruction in the seven body sections is replaced with grounded prose, 18 tables, 5 figures, and 29 `ieeetr` references, targeting roughly 70 typeset pages, with a `full-paper.zip` for one step Overleaf upload. The four images use placeholder slots the author replaces later, so the project compiles either way.

**5/25: v0.5.0 (VVUQ-01 Draft Paper Scaffold)** Adds [papers/VVUQ-01/draft-paper](papers/VVUQ-01/draft-paper): a compilable single column LaTeX scaffold for the manuscript *Two Stage VVUQ Oncology Clinical Trial Verification Automation Priority over Existing Generated Code*. 

**5/23: v0.4.0 (VVUQ-01 Publication Figures Rendered)** Renders the 10 image instructions into [papers/VVUQ-01/imagegen](papers/VVUQ-01/imagegen): 10 self-contained matplotlib scripts (the generated code) and the 10 portrait, full-size, 300 dpi PNG figures they produce (the execution output).

**5/23: v0.3.0 (VVUQ-01 Image Instructions for Publication Figures)** Adds [papers/VVUQ-01/image-instruct](papers/VVUQ-01/image-instruct): 10 comprehensive image instructions plus a master README that specify, ahead of any rendering, how Claude Code Opus 4.7 (1M) Max builds 10 figures.

**5/23: v0.2.0 (VVUQ-01 Execution and Stage 2 PDAC Reference)** Executes the entire v0.1.0 codebase and the Stage 2 2030 60-second PDAC procedure code, and records the full run under [papers/VVUQ-01/execution](papers/VVUQ-01/execution). All 15 example scripts ran to exit 0, the test suite passed (51 passed, 0 skipped), the lint-and-format CI surface is clean.

**5/21: v0.1.0 (Initial Automation Platform)** First release of the daily-deliverable pipeline (instruction, code generation, execution, paper assembly), the VVUQ gate held to a higher standard than code generation, triple simulation with consensus, robust web and PDF ingestion.

## Responsible Use

This repository is complementary and open source. Please implement code safely and responsibly. Generated instructions, code, and papers are drafts: a VVUQ gate and a human reviewer must clear any deliverable before clinical use. Intended audience: engineers building automated Physical AI systems (robotics, ML, integration, and validation) for clinical trial settings.

## Table of Contents

- [Thesis and Roadmap](#thesis-and-roadmap)
- [Daily Deliverable Pipeline](#daily-deliverable-pipeline)
- [Two-Stage Roadmap](#two-stage-roadmap)
- [Quick Start](#quick-start)
- [Repository Structure](#repository-structure)
- [Established Methods Proven Across Projects](#established-methods-proven-across-projects)
- [Core Capabilities](#core-capabilities)
- [VVUQ Held Higher Than Code Generation](#vvuq-held-higher-than-code-generation)
- [VVUQ-01 Figures and Image Instructions](#vvuq-01-figures-and-image-instructions)
- [VVUQ-01 Draft Paper](#vvuq-01-draft-paper)
- [VVUQ-01 Full Paper](#vvuq-01-full-paper)
- [Dependencies](#dependencies)
- [Related Repositories](#related-repositories)
- [Citation](#citation)
- [License](#license)

## Thesis and Roadmap

The thesis above is realized by a pipeline that runs the five established methods for every deliverable, then automates, accelerates, and assures the result. The roadmap is organized into two stages that may be realized in the near, mid, or long term.

## Daily Deliverable Pipeline

```
  Inputs                     Five Established Methods            Assured Output
  (web + PDF)            --> (per daily deliverable)        --> (committed + archived)
  +-------------------+      +---------------------------+      +-------------------+
  | Web search        |  ->  | 1. Instruction generation |  ->  | Daily deliverable |
  | PDF processing    |      | 2. Code generation        |      | committed to Git  |
  | Autochunk to 200K |      | 3. Code execution         |      | with per-chunk    |
  | READMEs per chunk |      | 4. Paper assembly         |      | READMEs at 200K   |
  +-------------------+      +---------------------------+      +-------------------+
            |                            |                                ^
            v                            v                                |
  +-------------------+      +---------------------------+      +-------------------+
  | Non-stop commit   |      | Triple simulation         |      | VVUQ gate         |
  | scheduler 24/day  |  ->  | run each project 3 times, |  ->  | V and V and UQ,   |
  | autonomous cadence|      | consensus across runs     |      | stricter than     |
  |                   |      |                           |      | code generation   |
  +-------------------+      +---------------------------+      +-------------------+
```

The pipeline mirrors the multi-stage workflow proven in the prior repositories: instructions feed code generation, code generation feeds execution, and execution feeds paper assembly. Triple simulation and the VVUQ gate sit across the whole flow so a deliverable is only committed once it is verified, validated, and within its uncertainty budget.

## Two-Stage Roadmap

```
  Stage 1 (near to mid term)               Stage 2 (mid to long term)
  +-----------------------------------+    +-----------------------------------+
  | - Non-stop commit schedules       |    | - Code runs physical AI in        |
  | - VVUQs more robust than codegen  | -> |   lights-off factories            |
  | - Auto-simulate projects 3 times  |    | - Hybrid surgery and medicine in  |
  | - Robust web search and PDF       |    |   the first pilot, analogous to   |
  | - Per-file size limits at 200K    |    |   the 2030 PDAC 60-second Whipple |
  | - Autochunk code and docs w/      |    |   plus Daraxonrasib simulation    |
  |   per-chunk READMEs               |    |                                   |
  +-----------------------------------+    +-----------------------------------+
```

| Stage | Goal | Where it lives |
|-------|------|----------------|
| Stage 1 | Non-stop commit schedules | `scheduler/` |
| Stage 1 | VVUQs more robust than code generation | `vvuq/` |
| Stage 1 | Auto-simulate projects three times | `simulation/` |
| Stage 1 | Robust web search and PDF processing | `ingestion/` |
| Stage 1 | Per-file size limits raised to 200K | `chunking/`, `configs/pipeline_config.yaml` |
| Stage 1 | Autochunk code and documents with READMEs | `chunking/` |
| Stage 2 | Code runs physical AI in lights-off factories | `physical-ai/lights_off_factory.py` |
| Stage 2 | Hybrid surgery and medicine first pilot | `physical-ai/hybrid_surgery_medicine.py` |

## Quick Start

```bash
# Clone the repository
git clone https://github.com/kevinkawchak/cancer-automated.git
cd cancer-automated

# Install core dependencies
pip install -r requirements.txt

# Verify the environment
python scripts/verify_installation.py

# Run the test suite
pytest tests/ -v
```

## Repository Structure

```
cancer-automated/
├── README.md
├── CHANGELOG.md
├── releases.md
├── LICENSE
├── CONTRIBUTING.md
├── CODE_OF_CONDUCT.md
├── SECURITY.md
├── SUPPORT.md
├── CITATION.cff
├── requirements.txt
├── ruff.toml
├── .gitignore
│
├── .github/
│   ├── workflows/
│   │   └── ci.yml                  # lint-and-format, validate-scripts, test
│   ├── PULL_REQUEST_TEMPLATE.md
│   └── ISSUE_TEMPLATE/
│       ├── bug_report.md
│       └── feature_request.md
│
├── pipeline/                       # ★ Five established methods, one daily deliverable
│   ├── README.md
│   ├── deliverable.py              # Deliverable data model (enums + dataclasses)
│   ├── instruction_stage.py        # Method 1: generate instructions
│   ├── codegen_stage.py            # Method 2: generate code
│   ├── execution_stage.py          # Method 3: execute code
│   ├── paper_stage.py              # Method 4: assemble paper
│   ├── orchestrator.py             # End-to-end orchestration of all stages
│   └── examples-pipeline/
│       ├── README.md
│       ├── 01_single_deliverable.py
│       ├── 02_instruction_to_paper.py
│       └── 03_full_daily_run.py
│
├── vvuq/                           # ★ Verification, Validation, Uncertainty Quantification
│   ├── README.md
│   ├── verification.py             # Did we build the deliverable right?
│   ├── validation.py               # Did we build the right deliverable?
│   ├── uncertainty.py              # Uncertainty across the three runs
│   ├── vvuq_gate.py                # Gate held to a higher standard than codegen
│   └── examples-vvuq/
│       ├── README.md
│       ├── 01_verification_checks.py
│       ├── 02_validation_against_reference.py
│       └── 03_uncertainty_budget.py
│
├── simulation/                     # ★ Auto-simulate every project three times
│   ├── README.md
│   ├── triple_runner.py
│   ├── consensus.py
│   └── examples-simulation/
│       ├── README.md
│       ├── 01_triple_run.py
│       └── 02_consensus_report.py
│
├── ingestion/                      # ★ Robust web search and PDF processing
│   ├── README.md
│   ├── web_search.py
│   ├── pdf_processor.py
│   └── examples-ingestion/
│       ├── README.md
│       ├── 01_web_search.py
│       └── 02_pdf_extract.py
│
├── chunking/                       # ★ 200K per-file caps, autochunk with READMEs
│   ├── README.md
│   ├── chunker.py
│   ├── readme_generator.py
│   └── examples-chunking/
│       ├── README.md
│       ├── 01_chunk_document.py
│       └── 02_chunk_with_readme.py
│
├── scheduler/                      # ★ Non-stop commit schedules
│   ├── README.md
│   ├── commit_scheduler.py
│   └── examples-scheduler/
│       ├── README.md
│       └── 01_daily_schedule.py
│
├── physical-ai/                    # ★ Stage 2 deployment references
│   ├── README.md
│   ├── lights_off_factory.py       # Code runs physical AI in lights-off factories
│   ├── hybrid_surgery_medicine.py  # Hybrid surgery and medicine first pilot
│   └── examples-physical-ai/
│       ├── README.md
│       ├── 01_lights_off_cell.py
│       └── 02_hybrid_pilot.py
│
├── configs/
│   ├── pipeline_config.yaml        # Stage and automation defaults (200K cap, 3 runs)
│   └── vvuq_thresholds.yaml        # VVUQ gate thresholds
│
├── scripts/
│   └── verify_installation.py
│
├── tests/                          # 8 test modules plus conftest, run with: pytest tests/
│   ├── conftest.py
│   ├── test_foundation.py
│   ├── test_pipeline.py
│   ├── test_vvuq.py
│   ├── test_simulation.py
│   ├── test_ingestion.py
│   ├── test_chunking.py
│   ├── test_scheduler.py
│   └── test_physical_ai.py
│
└── papers/                         # Paper workspaces, execution records, figures
    └── VVUQ-01/
        ├── inputs/                 # Source paper and research chunks (ingestion inputs)
        ├── templates/Template_10/  # LaTeX manuscript template (future paper build)
        ├── execution/              # ★ v0.2.0 execution record of the v0.1.0 codebase
        │   ├── README.md           # Index, badges, ASCII diagrams, results, limitations
        │   ├── 01-foundation/      # Environment, tests (51 passed), lint and format
        │   ├── 02-pipeline/        # Five established methods, generated artifacts
        │   ├── 03-vvuq/            # Gate decision surface (1 accept, 5 block, 1 escalate)
        │   ├── 04-stage1-automation/  # Simulation, ingestion, chunking, scheduler
        │   └── 05-physical-ai-stage2/ # 2030 PDAC pilot and lights-off safety surface
        ├── image-instruct/         # ★ v0.3.0 image instructions (10 specs + master README)
        │   ├── README.md           # Processing model, page frame, palette, 10-spec index
        │   ├── 01-vvuq-gate-funnel/        # Funnel: 6 candidates to 1 accepted
        │   ├── 02-acceleration-waterfall/  # Waterfall: 30 to 12 days, 2.5x
        │   ├── 03-five-methods-flowchart/  # Flowchart: the five established methods
        │   ├── 04-vvuq-assurance-wheel/    # Radar wheel: threshold vs achieved
        │   ├── 05-pdac-pilot-timeline/     # Gantt: 168-day 2030 PDAC pilot
        │   ├── 06-test-coverage-treemap/   # Treemap: 51 tests across 8 modules
        │   ├── 07-lights-off-state-machine/  # State diagram: factory safety surface
        │   ├── 08-fda-cost-efficiency-bridge/  # Financial bridge plus credibility
        │   ├── 09-value-proposition-matrix/  # Matrix: cloud vs conventional server
        │   └── 10-file-generation-sankey/  # Sankey: 13 files to 4 paper roles
        ├── imagegen/               # ★ v0.4.0 rendered figures (10 scripts + 10 PNGs + README)
        │   ├── README.md           # Rendered gallery, generated code vs execution, reproduction
        │   ├── 01-vvuq-gate-funnel/           # 01-vvuq-gate-funnel.py + .png (funnel)
        │   ├── 02-acceleration-waterfall/     # script + 300 dpi PNG (waterfall)
        │   ├── 03-five-methods-flowchart/     # script + 300 dpi PNG (flowchart)
        │   ├── 04-vvuq-assurance-wheel/       # script + 300 dpi PNG (radar wheel)
        │   ├── 05-pdac-pilot-timeline/        # script + 300 dpi PNG (Gantt)
        │   ├── 06-test-coverage-treemap/      # script + 300 dpi PNG (treemap)
        │   ├── 07-lights-off-state-machine/   # script + 300 dpi PNG (state diagram)
        │   ├── 08-fda-cost-efficiency-bridge/ # script + 300 dpi PNG (bridge + bullets)
        │   ├── 09-value-proposition-matrix/   # script + 300 dpi PNG (matrix)
        │   └── 10-file-generation-sankey/     # script + 300 dpi PNG (Sankey)
        ├── draft-paper/            # ★ v0.5.0 draft paper scaffold (LaTeX + instructions)
        │   ├── README.md           # Badges, processing model, section to source map
        │   ├── main.tex            # Title page, disclaimer, TOC, section inputs
        │   ├── new_paper.sty       # Single column serif style; black links, green ORCID
        │   ├── references.bib      # 29 final entries, DOI + clickable URL, no duplicates
        │   ├── draft-paper.zip     # Overleaf ready bundle
        │   └── sections/           # abstract, intro, methods, results, discussion,
        │                           #   limitations_future, conclusions, references, back_matter
        └── full-paper/             # ★ v0.6.0 full manuscript built from the scaffold
            ├── README.md           # Badges, build diagram, section to source map, figures
            ├── main.tex            # Preamble, title page, figure slots, section inputs
            ├── new_paper.sty       # Single column serif style; black links, green ORCID
            ├── references.bib      # 29 final entries, DOI + clickable URL, no duplicates
            ├── full-paper.zip      # Overleaf ready bundle
            ├── Images/             # Four author supplied figure slots plus a guide
            └── sections/           # abstract, intro, methods, results, discussion,
                                    #   limitations_future, conclusions, references, back_matter
```

## Established Methods Proven Across Projects

Several prior projects established and proved the methods that this repository automates. The following developments are the foundation for production-compliant deliverables.

| Source development | Proven method | Path |
|--------------------|---------------|------|
| National Platform paper | AI generates instructions, code, executes code, builds visualizations, and writes a 186-page paper end to end | physical-ai-oncology-trials/national-platform/new_paper/final_paper |
| Accelerated Patient Prediction (four simulations) | Efficient AI methods predict how new physical AI trials are advantageous in the real world with quality and speed | physical-ai-oncology-trials/new-trial/national-24-7-trial/paper/full-paper/final-paper |
| 2030 PDAC 60-second Whipple plus Daraxonrasib | High repository proficiency for a hybrid surgery and medicine deliverable, the Stage 2 analog | robotic-surgeries/2030-pdac-1min/paper/final-paper |
| Humanoid demo project | Multi-stage instruction to code to execution to paper workflow used as the pipeline template | Clinical-AI-Demos/demo-projects/07-humanoid/paper |

## Core Capabilities

| Capability | Module | What it delivers |
|------------|--------|------------------|
| Instruction generation | `pipeline/instruction_stage.py` | Bracketed instruction sets that drive downstream code generation |
| Code generation | `pipeline/codegen_stage.py` | Code authored from instructions, ready for execution |
| Code execution | `pipeline/execution_stage.py` | Captured outputs, logs, and artifacts from running the code |
| Paper assembly | `pipeline/paper_stage.py` | A paper assembled from executed results |
| VVUQ gate | `vvuq/vvuq_gate.py` | Verification, validation, and uncertainty checks stricter than codegen |
| Triple simulation | `simulation/triple_runner.py` | Three independent runs with consensus and divergence flags |
| Robust ingestion | `ingestion/` | Web search and PDF processing with retries and guarded dependencies |
| Autochunking | `chunking/` | 200K per-file caps with a generated README per chunk |
| Non-stop scheduling | `scheduler/commit_scheduler.py` | Autonomous commit cadence for continuous daily deliverables |

## VVUQ Held Higher Than Code Generation

A central Stage 1 principle is that VVUQ is more robust than code generation. Code generation produces a candidate deliverable. VVUQ decides whether that candidate is allowed to ship. The gate enforces:

- Verification: every structural and schema check passes, and the deliverable lints cleanly.
- Validation: agreement with a reference meets the threshold and a human review is recorded.
- Uncertainty quantification: the three simulation runs agree within the configured coefficient of variation.

Thresholds live in `configs/vvuq_thresholds.yaml`, and the gate blocks on any failure and escalates divergence to a human.

## VVUQ-01 Figures and Image Instructions

The image generation leg of the thesis is specified under [papers/VVUQ-01/image-instruct](papers/VVUQ-01/image-instruct) and rendered under [papers/VVUQ-01/imagegen](papers/VVUQ-01/imagegen). The instructions hold 10 comprehensive specifications plus a master README; each fully specifies one publication ready, portrait, full-size, 300 dpi figure, grounded in code generation (v0.1.0) and code execution (v0.2.0). As of v0.4.0 the figures are built: `imagegen` carries 10 self-contained matplotlib scripts (the generated code) and the 10 rendered PNG figures (the execution output), one numbered subdirectory per figure. Writing the full assurance specification before any pixel is rendered is the image generation analog of the VVUQ gate, and the build follows that specification with no manual positioning.

```
  image-instruct/NN-name/         imagegen/NN-name/            imagegen/NN-name/
  +----------------------+        +----------------------+      +-------------------+
  | README.md            |  -->   | NN-name.py           |  --> | NN-name.png       |
  | full figure spec     |  spec  | self-contained       | run  | portrait, 300 dpi |
  | (data, layout, color,| =====> | matplotlib + numpy,  | ===> | white background, |
  |  page frame, paths)  |        | hardcoded grounded   |      | full size, aligned|
  |  v0.3.0 instructions |        | values, ruff clean   |      | no positioning    |
  +----------------------+        +----------------------+      +-------------------+
        generated code (script)  ----------------->  execution output (image)
```

| No. | Instruction | Chart family | Basis |
|-----|-------------|--------------|-------|
| 01 | `01-vvuq-gate-funnel` | Funnel | both |
| 02 | `02-acceleration-waterfall` | Waterfall | both |
| 03 | `03-five-methods-flowchart` | Process flowchart | both |
| 04 | `04-vvuq-assurance-wheel` | Radar wheel | both |
| 05 | `05-pdac-pilot-timeline` | Gantt timeline | both |
| 06 | `06-test-coverage-treemap` | Treemap | execution |
| 07 | `07-lights-off-state-machine` | State diagram | both |
| 08 | `08-fda-cost-efficiency-bridge` | Financial bridge and bullet | both |
| 09 | `09-value-proposition-matrix` | Value proposition matrix | execution |
| 10 | `10-file-generation-sankey` | Sankey flow | both |

The set avoids basic bar, pie, and line charts, shares one professional palette and portrait page frame, uses the section symbol `§` where required, and uses single dashes only. See the [image-instruct README](papers/VVUQ-01/image-instruct) for the processing model, the page frame, the palette, and the per figure specifications, and the [imagegen README](papers/VVUQ-01/imagegen) for the rendered gallery, the generated code versus execution split, and reproduction with matplotlib.

## VVUQ-01 Draft Paper

The paper generation leg of the thesis begins under [papers/VVUQ-01/draft-paper](papers/VVUQ-01/draft-paper), a complete and compilable single column LaTeX scaffold for the manuscript *Two Stage VVUQ Oncology Clinical Trial Verification Automation Priority over Existing Generated Code*. The scaffold separates final files from instruction files: the title page (`main.tex`), the style (`new_paper.sty`), the 29 entry bibliography (`references.bib`), the references section, and the back matter are final, while the seven body section files carry bracketed processing instructions that name the exact repository directories and files for a future Claude Code Opus 4.7 (1M) Max pass to write a 70+ page paper. Writing the assurance specification (which sources, which metrics, which figures, and the formatting contract) ahead of the prose is the paper generation analog of the VVUQ gate.

```
  draft-paper/ (now)                          Future pass (full paper)
  +-----------------------------------+       +-----------------------------------+
  | FINAL    main.tex, new_paper.sty, | -->   | REPLACE the bracketed [ ... ]     |
  |          references.bib, back      | 70+  | blocks in the seven body sections |
  |          matter, references        | page | with grounded prose, tables, and  |
  | INSTRUCT the seven body sections   | ===> | figures; keep the scaffold intact |
  +-----------------------------------+       +-----------------------------------+
```

The bibliography is final: every DOI entry carries its human readable DOI and a clickable resolver URL, and repository entries carry both a GitHub and a Zenodo URL, each once, with no duplicate link and no `howpublished` field. A `draft-paper.zip` bundle is provided for a one step Overleaf upload. The additions are LaTeX, Markdown, and a zip, all outside the `ruff` and `yamllint` surface, so the CI stays green.

## VVUQ-01 Full Paper

The full manuscript is realized under [papers/VVUQ-01/full-paper](papers/VVUQ-01/full-paper). It is built from the v0.5.0 draft scaffold without modifying it: every bracketed processing instruction in the seven body sections is replaced with grounded, publication grade prose, tables, and figures, targeting roughly 70 typeset pages, while the title page, style file, bibliography, references block, and back matter are carried over. The paper renders the executed evidence (51 of 51 tests, the 2.5x acceleration, the full VVUQ gate decision surface of 1 accept and 5 block with 1 escalate, triple run consensus, the lights off factory safety cases, and the 2030 PDAC pilot) across 18 tabularx tables sized to the body text width, 5 figures, and 29 `ieeetr` references.

```
  draft-paper/ (scaffold)                     full-paper/ (this release)
  +-----------------------------------+       +-----------------------------------+
  | FINAL    main.tex, new_paper.sty, | -->   | CARRIED OVER, plus the seven body |
  |          references.bib, back      | 70   | sections written in full with     |
  |          matter, references        | page | grounded prose, 18 tables, and    |
  | INSTRUCT the seven body sections   | ===> | 5 figure slots; scaffold intact   |
  +-----------------------------------+       +-----------------------------------+
```

The four figures use placeholder slots that compile immediately and are replaced automatically once the author drops the final image into `Images/`. A `full-paper.zip` bundle is provided for a one step Overleaf upload, and the additions are LaTeX, Markdown, and a zip, all outside the `ruff` and `yamllint` surface, so the CI stays green.

## Continuous Integration

The `CI` workflow runs on every pull request and push to `main`:

| Job | What it checks | Python |
|-----|----------------|--------|
| `lint-and-format` | `ruff check`, `ruff format --check`, `yamllint -d relaxed` | 3.10, 3.11, 3.12 |
| `validate-scripts` | `python -m py_compile scripts/verify_installation.py` | 3.10 |
| `test` | `pytest tests/` | 3.10, 3.11, 3.12 |

Reproduce the checks locally before opening a pull request:

```bash
ruff check .
ruff format --check .
yamllint -d relaxed configs/ .github/
pytest tests/
```

## Dependencies

### Core Requirements

```
python>=3.10
numpy>=1.24.0
pyyaml>=6.0.0
```

The core daily-deliverable engine runs on the Python standard library so the lint-and-format and test CI jobs stay green without heavy installs. Every heavy or optional dependency is imported through a try/except guard in the module that uses it, so the package remains importable when the dependency is absent. See [requirements.txt](requirements.txt) for the full optional list (agentic backends, ingestion libraries, and simulation backends).

## Related Repositories

| Repository | Purpose | Last Updated |
|------------|---------|--------------|
| [physical-ai-oncology-trials](https://github.com/kevinkawchak/physical-ai-oncology-trials) | End-to-end Physical AI unification, National Platform paper, four-simulation accelerated prediction | May 2026 |
| [robotic-surgeries](https://github.com/kevinkawchak/robotic-surgeries) | 2030 PDAC 60-second robotic Whipple plus medicine simulation | May 2026 |
| [Clinical-AI-Demos](https://github.com/kevinkawchak/Clinical-AI-Demos) | Multi-stage instruction to code to execution to paper demo projects | May 2026 |

## Citation

If you use this repository in your research, please cite:

```bibtex
@software{kawchak2026cancerautomated,
  author = {Kawchak, Kevin},
  title = {cancer-automated: Automated Physical AI Oncology Trial Daily Deliverables},
  version = {0.6.0},
  year = {2026},
  publisher = {GitHub},
  url = {https://github.com/kevinkawchak/cancer-automated}
}
```

## License

MIT License. See [LICENSE](LICENSE) for details.
