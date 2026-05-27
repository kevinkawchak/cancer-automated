# Production Automated Physical AI Oncology Trial Daily Deliverables

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Release](https://img.shields.io/badge/Release-v1.1.0-brightgreen.svg)](releases.md)
[![Last Updated](https://img.shields.io/badge/Updated-May%202026-blue.svg)](CHANGELOG.md)
[![Python](https://img.shields.io/badge/Python-3.10%20|%203.11%20|%203.12-blue.svg)](https://www.python.org/)
[![Protocol](https://img.shields.io/badge/Protocol-MCP-purple.svg)](https://modelcontextprotocol.io/)
[![CI](https://img.shields.io/badge/CI-lint%20and%20format-blue.svg)](.github/workflows/ci.yml)
[![Contributors](https://img.shields.io/badge/Contributors-4-blue.svg)](releases.md)

**Production-ready, scalable automation for Physical AI oncology trial daily deliverables, by Claude Code Opus 4.7, Cowork; building on developments proven across physical-ai-oncology-trials, robotic-surgeries, and Clinical-AI-Demos.**

This repository packages the established methods for generating instructions, generating code, executing code, and creating papers into a single repeatable daily-deliverable pipeline. It then layers verification, validation, and uncertainty quantification (VVUQ), triple simulation, robust web, and PDF ingestion.

> **Thesis.** Production-ready, scalable, and automated Physical AI oncology trial daily deliverables are obtained based on established methods for generating instructions, code, code execution, and creating papers, and are further automated, accelerated, and the VVUQ is improved.

**5/27: v1.1.0 (VVUQ-02 Draft Paper)** Adds [papers/VVUQ-02/draft-paper](papers/VVUQ-02/draft-paper): a compilable single column LaTeX scaffold for *10 Mobile Pancreatic Cancer Unitree H2 Surgical Humanoids: VVUQ Processing Priority over Code Generation*, built from the Template_04 regulatory and FDA submission scaffold. Every body section is a bracketed processing instruction naming the exact codegen, execution, inputs, and imagegen files a future pass must read; the references (41 entries with clickable DOIs and well-represented external standards) are final, and the five figure floats (forest, binding matrix, standards wheel, sensor bands, cost assessment) are placed with captions, labels, and `\autoref`. Authored across 14 commits in a single pull request, one file per commit pushed in real time, and shipped as a single Overleaf-ready LaTeX zip.

**5/26: v1.0.0 (VVUQ-02 Imagegen)** Renders the v0.9.0 image instructions into [papers/VVUQ-02/imagegen](papers/VVUQ-02/imagegen): 15 self-contained matplotlib scripts (the generated code) and the 15 portrait, full-size, 300 dpi PNG figures they produce (the execution output), one numbered subdirectory per figure, plus a comprehensive README. Every figure is grounded in the codegen (v0.7.0) and execution (v0.8.0) records, renders on a white background with no dark mode, and is ruff clean.

**5/26: v0.9.0 (VVUQ-02 Image Instructions)** Adds [papers/VVUQ-02/image-instruct](papers/VVUQ-02/image-instruct): 15 comprehensive image instructions plus a master README that specify, ahead of any rendering, how Claude Code Opus 4.7 (1M) Max builds 15 portrait, full-size, 300 dpi figures from the codegen (v0.7.0) and execution (v0.8.0) records. Instructions only; the matplotlib scripts and PNGs are rendered in v1.0.0.

**5/26: v0.8.0 (VVUQ-02 Execution)** Executes the entire [papers/VVUQ-02/codegen](papers/VVUQ-02/codegen) tree and records the full run under [papers/VVUQ-02/execution](papers/VVUQ-02/execution) across 8 commits in a single pull request. Every entry point ran to exit 0, the suite passed (172 passed, 0 skipped).

**5/26: v0.7.0 (VVUQ-02 Humanoid VVUQ Codegen)** Adds [papers/VVUQ-02/codegen](papers/VVUQ-02/codegen): the standalone generated codebase for 10 humanoid-specific VVUQ gates on an autonomous Unitree H2-Surgical 1.0 (hypothetical 2030) performing the 60-second 8-phase Whipple. 

**5/25 [Final PDF](https://doi.org/10.5281/zenodo.20372501): v0.6.0 (VVUQ-01 Full Paper)** Adds [papers/VVUQ-01/full-paper](papers/VVUQ-01/full-paper): the full manuscript built from the v0.5.0 draft scaffold without modifying it. Every bracketed processing instruction in the seven body sections is replaced with grounded prose, 18 tables.

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
- [VVUQ-02 Humanoid VVUQ Codegen](#vvuq-02-humanoid-vvuq-codegen)
- [VVUQ-02 Execution](#vvuq-02-execution)
- [VVUQ-02 Image Instructions](#vvuq-02-image-instructions)
- [VVUQ-02 Imagegen](#vvuq-02-imagegen)
- [VVUQ-02 Draft Paper](#vvuq-02-draft-paper)
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
    ├── VVUQ-01/
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
    └── VVUQ-02/                     # ★ v0.7.0 codegen, ★ v0.8.0 execution
        ├── instructions/           # prompt-instruct.md, output-instruct.md (lineage)
        ├── inputs/                 # ★ wired standards corpus + clinical baselines
        │   ├── standards/          # ASME V&V 40, IEC 80601-2-77, ISO/TS 15066, ...
        │   └── clinical/           # Dutch cohort baseline, Fistula Risk Score
        ├── templates/Template_04/  # Regulatory and FDA submission LaTeX scaffold
        ├── codegen/                # ★ standalone 10-gate humanoid codebase
        │   ├── README.md           # DOI badges, gate ASCII diagram, repo tree
        │   ├── prompt-codegen.md   # the generating prompt, verbatim
        │   ├── output-codegen.md   # the narrative output of the generation step
        │   ├── config/             # frozen scope, kinematics, thresholds, standards map
        │   ├── schemas/            # JSON Schema + Protobuf + Avro sensor and command
        │   ├── src/                # kinematics, sensors, perception, autonomy, hands,
        │   │                       #   balance, safety, suturing, vvuq, simulation, ...
        │   ├── data/reference/     # independent validation truth per gate
        │   ├── docs/               # methodology, gate spec, platform, safety protocols
        │   └── tests/              # 172 passing (64-item 10-gate decision surface)
        ├── execution/              # ★ v0.8.0 full run record of the codegen tree
        │   ├── README.md           # DOI badges, gate ASCII diagram, outcomes table
        │   ├── prompt-execution.md # the generating prompt, verbatim
        │   ├── output-execution.md # the narrative output of the execution step
        │   ├── 01-foundation/      # environment, determinism, 172 tests, lint
        │   ├── 02-pipeline/        # intent to compile to act to score
        │   ├── 03-vvuq/            # the 10-gate ACCEPT/BLOCK/ESCALATE surface
        │   ├── 04-automation/      # 32-iter sweep, 1790-line tournament, Zenodo
        │   └── 05-humanoid-deployment/  # 60 s Whipple, 1000-row stream, safety
        ├── image-instruct/         # ★ v0.9.0 image instructions (15 specs + master README)
        │   ├── README.md           # Conventions, palette, page frame, 15-spec index, badges
        │   ├── prompt-image-instruct.md   # the generating prompt, verbatim
        │   ├── output-image-instruct.md   # the narrative output of the image-instruct step
        │   ├── 01-platform-pipeline-flow/        # Workflow: generation to assurance pipeline
        │   ├── 02-vvuq-gate-decision-funnel/     # Funnel: 5 cases to 1 ACCEPT
        │   ├── 03-ten-gate-threshold-forest/     # Forest: the 10 gates and thresholds
        │   ├── 04-gate-standard-binding-matrix/  # Heatmap: gates to 15 standards
        │   ├── 05-clinical-regulatory-standards-wheel/  # Wheel: inputs corpus, 6 domains
        │   ├── 06-test-coverage-treemap/         # Treemap: 172 tests across 15 modules
        │   ├── 07-validation-parity-scatter/     # Parity: observed vs reference
        │   ├── 08-sweep-composite-stripplot/     # Strip: 32-iteration composite
        │   ├── 09-composite-weighting-waterfall/ # Waterfall: 6 weights to 1.00, gated
        │   ├── 10-four-entrant-comparison-violin/  # Box: 4 entrants, humanoid rank 2
        │   ├── 11-sensor-stream-safety-bands/    # Line bands: 1000-row sensor stream
        │   ├── 12-eight-phase-whipple-swimmer/   # Swimmer: 60 s 8-phase Whipple
        │   ├── 13-assurance-cost-assessment/     # Financial: autonomous vs conventional
        │   ├── 14-value-proposition-matrix/      # Value matrix: faster, cheaper, patient
        │   └── 15-platform-mindmap/              # Mind map: the whole VVUQ-02 platform
        ├── imagegen/               # ★ v1.0.0 rendered figures (15 scripts + 15 PNGs + README)
        │   ├── README.md           # Conventions, palette, 15-figure index, outcomes, badges
        │   ├── prompt-imagegen.md  # the generating prompt, verbatim
        │   ├── output-imagegen.md  # the narrative output of the imagegen step
        │   └── NN-name/            # NN-name.py (matplotlib + numpy) and NN-name.png (300 dpi)
        ├── draft-paper/            # ★ v1.1.0 LaTeX draft scaffold (instructions + final refs)
        │   ├── README.md           # DOI badges, section to source map, formatting rules
        │   ├── main.tex            # title page, TOC, \input wiring, format directives
        │   ├── new_paper.sty       # Palatino + navy style (template family)
        │   ├── references.bib      # 41 final entries; clickable DOIs; standards heavy
        │   ├── sections/           # abstract..back_matter: bracketed build instructions
        │   ├── Images/             # author drops the five rendered PNGs here later
        │   ├── draft-paper.zip     # Overleaf-ready LaTeX bundle
        │   ├── prompt-draft-paper.md   # the generating prompt, verbatim
        │   └── output-draft-paper.md   # the narrative output of the draft-paper step
        └── full-paper/ final-paper/  # placeholders (future 70+ page manuscript)
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

## VVUQ-02 Humanoid VVUQ Codegen

The code generation leg of the thesis advances to a harder subject under [papers/VVUQ-02/codegen](papers/VVUQ-02/codegen): a single autonomous humanoid surgeon (a clearly labeled hypothetical 2030 Unitree H2-Surgical 1.0) that performs the 60-second 8-phase Whipple on patient PAT-PDAC-0001 with its own two dexterous hands, no teleoperation. Because one humanoid concentrates all error potential into one body, the VVUQ assurance layer must be more substantial, stricter, and more thoroughly exercised than the control code, and a candidate behavior must clear 10 distinct humanoid-specific gates before it ships. The codebase was generated by Claude Code Opus 4.7 (1M) Max from [papers/VVUQ-02/instructions/output-instruct.md](papers/VVUQ-02/instructions/output-instruct.md) across 11 commits in a single pull request, one set of files per commit pushed in real time.

The assurance layer is built against external standards already used in real life, so the credibility argument is defensible to a regulator. Each gate binds to its governing standards through a machine-readable map and the wired standards input corpus, validates observed metrics against an independent reference, and quantifies uncertainty across seeded runs.

```
  candidate humanoid behaviors per iteration
        |
   +----v-------------------------------------------------------+
   | 01 bimanual-handeye-servo        06 vascular-no-fly-hand *  |
   | 02 dexterous-finger-force        07 bimanual-suturing       |
   | 03 whole-body-balance            08 perception-scene        |
   | 04 autonomous-plan-correctness   09 shared-or-collision *   |
   | 05 instrument-grasp-handover     10 fault-estop-degrade *   |
   +----v-------------------------------------------------------+
        |  each gate: Verify (== 1.0) -> Validate (independent
        |  reference) -> Quantify (coefficient of variation)
        v
   ACCEPT (all 10 pass)  /  BLOCK (any fail)  /  ESCALATE (divergence)
   composite reported only when all 10 gates ACCEPT
   * immediate-catastrophe gates: V == 1.0, tightest CV, plus a hard predicate
```

Standards anchor set: ASME V&V 40-2018 and NASA-STD-7009A for model credibility (with the FDA 2023 computational modeling guidance), IEC 80601-2-77 and IEC 60601-1 for robotic surgery, ISO 13482 and ISO/TS 15066 and ISO 10218-1 and ISO 9283 for service and collaborative robot safety, IEC 62304 and ISO 14971 and ISO 13849-1 for software and risk, and UL 4600 and IEEE 7009 for autonomy and fail-safe design. The deterministic 32-iteration Latin hypercube sweep (seed 20260525) clears all 10 gates on every iteration; the composite mean is 93.56, reported only because all gates ACCEPT. The tree is standalone, runs on the Python standard library with guarded optional backends, and keeps `ruff check`, `ruff format --check`, and `yamllint` clean across Python 3.10, 3.11, and 3.12; its 172 tests include a 64-item 10-gate decision surface (one ACCEPT plus several BLOCK and ESCALATE cases per gate). The execution record is realized in v0.8.0 and the 15 image instructions in v0.9.0 (both below); the manuscript is reserved as a placeholder for a future pull request.

## VVUQ-02 Execution

The full run record of the codegen tree is under [papers/VVUQ-02/execution](papers/VVUQ-02/execution), produced by Claude Code Opus 4.7 (1M) Max running autonomously across 8 commits in a single pull request, one section per commit pushed in real time. Every codegen entry point executed (exit 0), the 172-test suite passed with 0 skipped, and the CI lint-and-format surface stayed clean across Python 3.10, 3.11, and 3.12. The record mirrors the VVUQ-01 execution layout in five numbered sections, with an honest limitations section and a this-run-versus-conventional-server section for future runs on leading MacOS, Windows, and Linux platforms.

```
  01 foundation     determinism (sensor CSV byte-identical), 172 tests, lint green
        |
  02 pipeline       intent -> compile -> act -> score, concordance 1.000
        |
  03 vvuq           10-gate surface: 10 ACCEPT, 3 BLOCK paths, 1 ESCALATE
        |
  04 automation     32-iter sweep (32/32 clear all gates), 1790-line tournament
        |
  05 deployment     60 s Whipple, 1000-row positional stream, 3 catastrophe gates
```

The decision-bearing result is the operationalized thesis: control behaviors are generated and compiled in microseconds, while clearing one for ship requires a 1.0 verification fraction, an agreement bar up to 1.00, a relative-error bound as tight as 0.01, a coefficient-of-variation bound as tight as 0.05, a recorded human review, and a hard predicate on each catastrophe gate. The two substantial generated files are featured and processed: the 1790-line four-entrant `comparison.json` (128 round verdicts, 100 percent caveat coverage) and the 1000-row, 27-column positional sensor stream (every row and every arm-angle, finger-force, and end-effector payload distinct, no repetition). Each gate, behavior, and safety surface is traced to the published external standard that governs it, so the credibility argument is defensible rather than ad hoc, which is what lets an inexpensive autonomous run stand as evidence for a future physical AI oncology trial.

## VVUQ-02 Image Instructions

The image generation leg of the thesis is specified under [papers/VVUQ-02/image-instruct](papers/VVUQ-02/image-instruct): 15 comprehensive image instructions plus a master README, each a self-contained specification for one publication ready, portrait, full-size, 300 dpi figure grounded in the VVUQ-02 code generation record (v0.7.0) and code execution record (v0.8.0). As of v1.0.0 the figures are built under [papers/VVUQ-02/imagegen](papers/VVUQ-02/imagegen), one numbered subdirectory per instruction (see [VVUQ-02 Imagegen](#vvuq-02-imagegen) below). Writing the full assurance specification before any pixel is rendered is the image generation analog of the VVUQ gate, and the build follows that specification with no manual positioning.

```
  image-instruct/NN-name/         imagegen/NN-name/             imagegen/NN-name/
  +----------------------+        +----------------------+      +-------------------+
  | README.md            |  -->   | NN-name.py           |  --> | NN-name.png       |
  | full figure spec     |  spec  | self-contained       | run  | portrait, 300 dpi |
  | (data, layout, color,| =====> | matplotlib + numpy,  | ===> | white background, |
  |  page frame, paths)  |        | hardcoded grounded   |      | full size, aligned|
  |  v0.9.0 instructions |        | values, ruff clean   |      | no positioning    |
  +----------------------+        +----------------------+      +-------------------+
        assurance specification  ----------------->  rendered figure (v1.0.0)
```

| No. | Instruction | Chart family | Basis |
|-----|-------------|--------------|-------|
| 01 | `01-platform-pipeline-flow` | Workflow diagram | both |
| 02 | `02-vvuq-gate-decision-funnel` | Funnel | both |
| 03 | `03-ten-gate-threshold-forest` | Forest plot | both |
| 04 | `04-gate-standard-binding-matrix` | Heatmap matrix | both |
| 05 | `05-clinical-regulatory-standards-wheel` | Wheel | codegen |
| 06 | `06-test-coverage-treemap` | Treemap | execution |
| 07 | `07-validation-parity-scatter` | Parity plot | both |
| 08 | `08-sweep-composite-stripplot` | Strip plot | execution |
| 09 | `09-composite-weighting-waterfall` | Waterfall | both |
| 10 | `10-four-entrant-comparison-violin` | Box plot | both |
| 11 | `11-sensor-stream-safety-bands` | Line with bands | both |
| 12 | `12-eight-phase-whipple-swimmer` | Swimmer plot | both |
| 13 | `13-assurance-cost-assessment` | Financial assessment | both |
| 14 | `14-value-proposition-matrix` | Value matrix | both |
| 15 | `15-platform-mindmap` | Mind map | both |

The 15 chart families are all distinct, chosen from a 20-family menu for best data availability and relevance, and avoid basic bar, pie, and line charts. Six figures satisfy a required-data brief: 172 tests (06), the external-standards anchoring (04), the 10 gates and thresholds (03), the clinical and regulatory corpus (05), the featured 1000-row sensor stream (11), and the four-entrant comparison (10). The set shares one professional palette and portrait page frame, uses the section symbol `§` where required, uses single dashes only, and renders on a white background with no dark mode. See the [image-instruct README](papers/VVUQ-02/image-instruct) for the processing model, the page frame, the palette, and the per figure specifications.

## VVUQ-02 Imagegen

As of v1.0.0 the 15 instructions are rendered under [papers/VVUQ-02/imagegen](papers/VVUQ-02/imagegen): 15 self-contained matplotlib scripts (the generated code) and the 15 portrait, full-size, 300 dpi PNG figures they produce (the execution output), one numbered subdirectory per figure, plus a comprehensive README and the two lineage files. Each script is pure `matplotlib` plus `numpy`, sets `matplotlib.use("Agg")`, hardcodes its grounded values, and renders a fixed `figsize=(8.5, 11)` frame at 300 dpi (2550 by 3300 pixels) on a white background. A shared auto-fit frame keeps the header, subtitle, and footer from clipping, so no manual positioning is needed.

```
  image-instruct/NN-name/         imagegen/NN-name/             imagegen/NN-name/
  +----------------------+        +----------------------+      +-------------------+
  | README.md            |  read  | NN-name.py           |  run | NN-name.png       |
  | full figure spec     | =====> | self-contained       | ===> | portrait, 300 dpi |
  | v0.9.0 instructions  |  spec  | matplotlib + numpy   |      | white background  |
  +----------------------+        +----------------------+      +-------------------+
        assurance specification  ----------------->  rendered figure (v1.0.0)
```

| No. | Figure | Chart family | Required data |
|-----|--------|--------------|---------------|
| 01 | `01-platform-pipeline-flow` | Workflow diagram | - |
| 02 | `02-vvuq-gate-decision-funnel` | Funnel | - |
| 03 | `03-ten-gate-threshold-forest` | Forest plot | R3 (10 gates and thresholds) |
| 04 | `04-gate-standard-binding-matrix` | Heatmap matrix | R2 (external standards) |
| 05 | `05-clinical-regulatory-standards-wheel` | Wheel | R4 (clinical and regulatory) |
| 06 | `06-test-coverage-treemap` | Treemap | R1 (172 tests) |
| 07 | `07-validation-parity-scatter` | Parity plot | - |
| 08 | `08-sweep-composite-stripplot` | Strip plot | - |
| 09 | `09-composite-weighting-waterfall` | Waterfall | - |
| 10 | `10-four-entrant-comparison-violin` | Box plot | R6 (4-entrant comparison) |
| 11 | `11-sensor-stream-safety-bands` | Line with bands | R5 (1000-row sensor) |
| 12 | `12-eight-phase-whipple-swimmer` | Swimmer plot | - |
| 13 | `13-assurance-cost-assessment` | Financial assessment | - |
| 14 | `14-value-proposition-matrix` | Value matrix | - |
| 15 | `15-platform-mindmap` | Mind map | - |

The arithmetic reconciles to the source files: the treemap tile areas sum to 172 tests across 15 modules, the composite weights sum to 1.00, the swimmer durations sum to 60 s, the four-entrant appearances sum to 256 over 128 verdicts, and the sweep strip plot reproduces min 93.417, max 93.715, and mean 93.562. The scripts depend only on `matplotlib` and `numpy` and keep `ruff check` and `ruff format --check` clean across Python 3.10, 3.11, and 3.12; the core CI does not import `imagegen/`. See the [imagegen README](papers/VVUQ-02/imagegen) for the rendered gallery, the generated-code versus execution split, and reproduction with matplotlib.

## VVUQ-02 Draft Paper

As of v1.1.0 the draft manuscript scaffold lives under [papers/VVUQ-02/draft-paper](papers/VVUQ-02/draft-paper): a compilable single column LaTeX bundle for *10 Mobile Pancreatic Cancer Unitree H2 Surgical Humanoids: VVUQ Processing Priority over Code Generation*, built from the Template_04 regulatory and FDA submission scaffold. It is a head start, not a finished paper. Each body section is a bracketed processing instruction that names the exact codegen (v0.7.0), execution (v0.8.0), inputs, and imagegen files a future Claude Code Opus 4.7 (1M) Max pass must read and synthesise into publication-quality prose, with the long paths kept in tables and the prose reserved for connected argument. The references are already final (41 entries, every DOI and resolver URL clickable, the external standards well represented), and the five figure floats are placed with one-line captions, labels, and `\autoref`.

```
  codegen/ + execution/ + inputs/ + imagegen/        draft-paper/ (this bundle)
  +---------------------------------------+          +---------------------------+
  | source files named per section        |  cite    | main.tex + sections/*.tex |
  | (the grounding for every claim)        | =======> | [bracketed instructions]  |
  +---------------------------------------+  +refs    | references.bib (final)    |
                                                      +---------------------------+
        scaffold + instructions  ----------------->  future 70+ page full paper
```

The bundle ships as a single Overleaf-ready zip (`draft-paper.zip`). Until the author drops the five rendered PNGs into `Images/`, each figure float renders a labelled placeholder via `\IfFileExists`, so the draft compiles cleanly now and again once the images are added. The figures are `fig:wheel` (Methods), `fig:forest` and `fig:bands` (Results), and `fig:matrix` and `fig:cost` (Discussion). See the [draft-paper README](papers/VVUQ-02/draft-paper) for the section to source-file map, the figure table, and the senior-author formatting rules.

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
  version = {0.9.0},
  year = {2026},
  publisher = {GitHub},
  url = {https://github.com/kevinkawchak/cancer-automated}
}
```

## License

MIT License. See [LICENSE](LICENSE) for details.
