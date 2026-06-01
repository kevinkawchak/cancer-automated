# Production Automated Physical AI Oncology Trial Daily Deliverables

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Release](https://img.shields.io/badge/Release-v2.3.1-brightgreen.svg)](releases.md)
[![Last Updated](https://img.shields.io/badge/Updated-June%202026-blue.svg)](CHANGELOG.md)
[![Python](https://img.shields.io/badge/Python-3.10%20|%203.11%20|%203.12-blue.svg)](https://www.python.org/)
[![Protocol](https://img.shields.io/badge/Protocol-MCP-purple.svg)](https://modelcontextprotocol.io/)
[![CI](https://img.shields.io/badge/CI-lint%20and%20format-blue.svg)](.github/workflows/ci.yml)
[![Contributors](https://img.shields.io/badge/Contributors-4-blue.svg)](releases.md)

**Production-ready, scalable automation for Physical AI oncology trial daily deliverables, by Claude Code Opus 4.7, Cowork; building on developments proven across physical-ai-oncology-trials, robotic-surgeries, and Clinical-AI-Demos.**

This repository packages the established methods for generating instructions, generating code, executing code, and creating papers into a single repeatable daily-deliverable pipeline. It then layers verification, validation, and uncertainty quantification (VVUQ), triple simulation, robust web, and PDF ingestion.

> **Thesis.** Production-ready, scalable, and automated Physical AI oncology trial daily deliverables are obtained based on established methods for generating instructions, code, code execution, and creating papers, and are further automated, accelerated, and the VVUQ is improved.

**6/1: v2.3.1 (Papers Directory READMEs)** Adds five comprehensive landing READMEs: [papers](papers) plus one each for [papers/VVUQ-01](papers/VVUQ-01), [papers/VVUQ-02](papers/VVUQ-02), [papers/VVUQ-03](papers/VVUQ-03), and [papers/VVUQ-04](papers/VVUQ-04). Each details the VVUQ verification developments and progress, shows the building process with ASCII diagrams, and covers what the results mean for the Physical AI oncology trial industry, the processing feat accomplished by AI, and the accelerated timeline versus conventional methods. Each carries DOI badges and the final paper or bill DOI (VVUQ-01 20372501, VVUQ-02 20421754, VVUQ-03 20454870, VVUQ-04 20485580).

**6/1 [Bill PDF](https://doi.org/10.5281/zenodo.20485580): v2.3.0 (VVUQ-04 Full Bill, LaTeX)** Adds [papers/VVUQ-04/full-bill](papers/VVUQ-04/full-bill): the finished LaTeX amendment to the Federal Food, Drug, and Cosmetic Act (21 U.S.C. § 301 et seq.), processed from the v2.2.0 draft scaffold by executing every bracketed drafting instruction against the named instruct-bill and final-paper sources. The bill is **H. R. 9510**, the *Verification Before Generation in Physical AI Oncology Trials Act of 2026*, adding a new section 515D (21 U.S.C. § 360e-5). 

**6/1: v2.2.0 (VVUQ-04 Draft Bill, LaTeX)** Adds [papers/VVUQ-04/draft-bill](papers/VVUQ-04/draft-bill): a LaTeX draft amendment to the Federal Food, Drug, and Cosmetic Act (21 U.S.C. § 301 et seq.) that recasts the prior *VVUQ Physical AI Oncology Trial Bill* (H.R. 9510) as a properly targeted amendment, citing each affected provision by its 21 U.S.C. section number and naming Public Law 119-93 only as the currency point, not amending Public Law 119-93 or Title 21 generally. It is an amendment scaffold with bracketed DRAFTING INSTRUCTIONS. 

**5/31: v2.1.0 (VVUQ-04 Template Bill, LaTeX)** Adds [papers/VVUQ-04/template-bill/LaTeX](papers/VVUQ-04/template-bill/LaTeX): a LaTeX template bill that reproduces the look and feel of the official United States Code, Title 21 - Food and Drugs (current through Public Law 119-93), reduced from 29 chapters and 757 sections to the 11 Federal Food, Drug, and Cosmetic Act device sections relevant to the Physical AI oncology trial context (§§ 301, 321, 331, 351, 355g, 360, 360c, 360e, 360e-4, 360j, 360k). 

**5/31: v2.0.0 (VVUQ-04 Instruct Bill)** Adds [papers/VVUQ-04/instruct-bill](papers/VVUQ-04/instruct-bill): structured U.S. medical AI bill and law summaries current through May 31, 2026 that make the *VVUQ Physical AI Oncology Trial Bill* (H.R. 9510) more current, better grounded, and XML-ready. Ten markdown files cover federal statutes, FDA device regulation, ONC algorithm transparency, CMS payment, privacy and nondiscrimination, state law, executive actions, emerging bills, VVUQ standards, and a legal crosswalk. 

**5/30 [Final PDF](https://doi.org/10.5281/zenodo.20454870): v1.4.0 (VVUQ-03 Final Paper)** Processes the v1.3.0 scaffold into the full, Overleaf-compilable bill under [papers/VVUQ-03/full-paper](papers/VVUQ-03/full-paper): the *VVUQ Physical AI Oncology Trial Bill* (H.R. 9510, 119th Congress, 2d Session; Draft 1.0). Every bracketed instruction becomes finished legislative prose with left-aligned, body-width tables (21 in all); the four main points, the USL and PSL synergy, and the fourteen external standards.

**5/30: v1.3.0 (VVUQ-03 Draft Paper)** Adds [papers/VVUQ-03/draft-paper](papers/VVUQ-03/draft-paper): a compilable single column LaTeX scaffold for the *VVUQ Physical AI Oncology Trial Bill* (Draft 1.0), a proposed U.S. law requiring the VVUQ verification process to clear robot-patient interaction code before that code is generated or executed. Every body section is a bracketed processing instruction.

**5/27: v1.2.0 (VVUQ-02 Full Paper)** Processes the v1.1.0 scaffold into the full, Overleaf-compilable manuscript under [papers/VVUQ-02/full-paper](papers/VVUQ-02/full-paper): *10 Mobile Pancreatic Cancer Unitree H2 Surgical Humanoids: VVUQ Processing Priority over Code Generation*. Every bracketed instruction becomes finished prose and a left-aligned, body-width table grounded in the inputs, codegen (v0.7.0), and execution (v0.8.0) records. 

**5/27: v1.1.0 (VVUQ-02 Draft Paper)** Adds [papers/VVUQ-02/draft-paper](papers/VVUQ-02/draft-paper): a compilable single column LaTeX scaffold for *10 Mobile Pancreatic Cancer Unitree H2 Surgical Humanoids: VVUQ Processing Priority over Code Generation*, built from the Template_04 regulatory and FDA submission scaffold. Every body section is a bracketed processing instruction naming the exact codegen, execution, inputs, and imagegen files.

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
- [Papers Directory READMEs](#papers-directory-readmes)
- [VVUQ-01 Figures and Image Instructions](#vvuq-01-figures-and-image-instructions)
- [VVUQ-01 Draft Paper](#vvuq-01-draft-paper)
- [VVUQ-01 Full Paper](#vvuq-01-full-paper)
- [VVUQ-02 Humanoid VVUQ Codegen](#vvuq-02-humanoid-vvuq-codegen)
- [VVUQ-02 Execution](#vvuq-02-execution)
- [VVUQ-02 Image Instructions](#vvuq-02-image-instructions)
- [VVUQ-02 Imagegen](#vvuq-02-imagegen)
- [VVUQ-02 Draft Paper](#vvuq-02-draft-paper)
- [VVUQ-02 Full Paper](#vvuq-02-full-paper)
- [VVUQ-03 Draft Paper](#vvuq-03-draft-paper)
- [VVUQ-03 Full Paper](#vvuq-03-full-paper)
- [VVUQ-04 Instruct Bill](#vvuq-04-instruct-bill)
- [VVUQ-04 Template Bill (LaTeX)](#vvuq-04-template-bill-latex)
- [VVUQ-04 Draft Bill (LaTeX)](#vvuq-04-draft-bill-latex)
- [VVUQ-04 Full Bill (LaTeX)](#vvuq-04-full-bill-latex)
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
    ├── README.md                   # ★ v2.3.1 papers landing page: four works, lineage, final DOIs
    ├── VVUQ-01/
        ├── README.md           # ★ v2.3.1 VVUQ-01 landing page: developments, build, results, DOIs
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
    ├── VVUQ-02/                     # ★ v0.7.0 codegen, ★ v0.8.0 execution
        ├── README.md           # ★ v2.3.1 VVUQ-02 landing page: developments, build, results, DOIs
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
        ├── full-paper/             # ★ v1.2.0 processed full manuscript (finished prose)
        │   ├── README.md           # DOI badges, lineage and assurance ASCII, results tables
        │   ├── main.tex            # preamble, title page, TOC, \input wiring
        │   ├── new_paper.sty       # Palatino + navy style (carried from the draft)
        │   ├── references.bib      # 41 final entries; clickable DOIs; standards heavy
        │   ├── sections/           # abstract..back_matter: finished prose + body-width tables
        │   ├── Images/             # author drops the five rendered PNGs here later
        │   ├── full-paper.zip      # Overleaf-ready LaTeX bundle
        │   ├── prompt-full-paper.md    # the generating prompt, verbatim
        │   └── output-full-paper.md    # the narrative output of the full-paper step
        └── final-paper/            # placeholder (future submission-ready manuscript)
    ├── VVUQ-03/                     # ★ v1.4.0 full paper (VVUQ Physical AI Oncology Trial Bill, H.R. 9510)
        ├── README.md           # ★ v2.3.1 VVUQ-03 landing page: developments, build, results, DOIs
        ├── template-paper/         # 21 CFR Part 312 adaptation chunks + .sty + .bib (source model)
        ├── draft-paper/            # v1.3.0 LaTeX bill scaffold (bracketed instructions + final refs)
        │   ├── README.md           # DOI badges, ASCII diagrams, section-to-source map, build validation
        │   ├── main.tex            # cover page, TOC, fifteen section \input lines, format directives
        │   ├── new_paper.sty       # Palatino body, navy accent (prior template family)
        │   ├── references.bib      # 60 final entries; clickable DOIs; federal and state laws; standards
        │   ├── sections/           # abstract..back_matter: 15 bracketed build-instruction files
        │   ├── draft-paper.zip     # Overleaf-ready LaTeX bundle
        │   ├── prompt-draft-paper.md   # the generating prompt, verbatim
        │   └── output-draft-paper.md   # the narrative output of the draft-paper step
        └── full-paper/             # ★ v1.4.0 finished bill (H.R. 9510; 15 sections; 21 body-width tables)
            ├── README.md           # DOI badges, bill-identity table, ASCII diagrams, source map
            ├── main.tex            # cover + H.R. 9510 header, TOC, fifteen \input lines, xltabular
            ├── new_paper.sty       # Palatino body, navy accent; widow/club/broken penalties 10000
            ├── references.bib      # 60 final entries; clickable DOIs; no howpublished
            ├── sections/           # abstract..back_matter: 15 finished legislative-prose files
            ├── full-paper.zip      # Overleaf-ready LaTeX bundle
            ├── prompt-full-paper.md    # the generating prompt, verbatim
            └── output-full-paper.md    # the narrative output of the full-paper step
    └── VVUQ-04/                     # ★ v2.0.0 instruct + v2.1.0 template + v2.2.0 draft + v2.3.0 full bill (LaTeX)
        ├── README.md           # ★ v2.3.1 VVUQ-04 landing page: developments, build, results, DOIs
        ├── instruct-bill/          # head start for the next bill draft (10 md + 5 bib + README)
        │   ├── README.md           # DOI badges, repo structure, file and bib correlations
        │   ├── 01-federal-statutory-framework.md        # Title 21, 42, 29, 15 statutes
        │   ├── 02-fda-ai-device-regulation.md           # PCCP, lifecycle, QMSR, credibility
        │   ├── 03-onc-astp-algorithm-transparency.md    # HTI-1 DSI, source attributes, HTI-5
        │   ├── 04-cms-coverage-payment-ai.md            # MA AI rule, WISeR, CPT autonomy
        │   ├── 05-privacy-security-nondiscrimination.md # HIPAA, Section 1557 and 92.210, FTC
        │   ├── 06-state-medical-ai-laws.md              # CA, CO, UT, TX, IL, MD, NE, NV, NY
        │   ├── 07-executive-actions-national-ai-strategy.md # EO 14179, AI Action Plan, OMB
        │   ├── 08-emerging-federal-bills.md             # 119th Congress, research influences
        │   ├── 09-vvuq-standards-clinical-trial-oncology.md # ASME, IEC, ISO, IEEE, ICH, OCE
        │   ├── 10-legal-crosswalk-and-bill-style.md     # research matrix + bill-style template
        │   ├── federal-statutes.bib                     # bib 1 (20 entries)
        │   ├── federal-regulations-guidance.bib         # bib 2 (36 entries)
        │   ├── state-laws.bib                           # bib 3 (20 entries)
        │   ├── executive-actions-and-emerging-bills.bib # bib 4 (25 entries)
        │   ├── standards-and-literature.bib             # bib 5 (44 entries)
        │   ├── prompt-instruct-bill.md                  # the generating prompt, verbatim
        │   └── output-instruct-bill.md                  # the narrative output of this step
        ├── template-bill/          # ★ v2.1.0 Title 21 device-provisions excerpt (LaTeX)
        │   ├── xml_usc21@119-93.zip # input: full Title 21 USLM XML (12.4 MB)
        │   └── LaTeX/              # Overleaf-ready U.S. Code look-and-feel reproduction
        │       ├── README.md       # DOI badges, section/interaction/file tables, ASCII
        │       ├── main.tex        # Title 21 head, structure, 11 \input lines, references
        │       ├── usctitle.sty    # U.S. Code style: serif, hanging indents, note styling
        │       ├── references.bib  # provenance + VVUQ lineage (11 entries)
        │       ├── template-bill-LaTeX.zip   # Overleaf-ready bundle
        │       ├── prompt-template-bill/LaTeX.md  # the generating prompt, verbatim
        │       ├── output-template-bill/LaTeX.md  # the narrative output of this step
        │       └── sections/       # 11 FD&C Act device sections, one .tex each
        │           ├── s301.tex s321.tex s331.tex s351.tex s355g.tex
        │           └── s360.tex s360c.tex s360e.tex s360e-4.tex s360j.tex s360k.tex
        ├── draft-bill/             # ★ v2.2.0 FD&C Act amendment scaffold (LaTeX)
        │   ├── README.md           # DOI badges, amendment-structure map, ASCII diagrams
        │   ├── main.tex            # caption, SECTION 1-2, SEC. 3 amendment, SEC. 4 comparative print
        │   ├── usctitle.sty        # US Code reproduction + amendment apparatus + draftbox
        │   ├── references.bib      # provenance + research sources (uscode_download + lineage)
        │   ├── draft-bill-LaTeX.zip   # Overleaf-ready bundle
        │   ├── prompt-draft-bill.md   # the generating prompt, verbatim
        │   ├── output-draft-bill.md   # the narrative output of this step
        │   └── sections/           # 11 reproduced sections, each + bracketed draft instructions
        │       ├── s301.tex s321.tex s331.tex s351.tex s355g.tex
        │       └── s360.tex s360c.tex s360e.tex s360e-4.tex s360j.tex s360k.tex
        └── full-bill/              # ★ v2.3.0 finished FD&C Act amendment, H. R. 9510 (LaTeX)
            ├── README.md           # DOI badges, what-changed table, ASCII diagrams
            ├── main.tex            # caption, SECTION 1-4, new § 360e-5, appendices, references
            ├── usctitle.sty        # US Code reproduction + amendment apparatus (no draftbox)
            ├── references.bib      # 79 provenance + research sources (ieeetr)
            ├── full-bill-LaTeX.zip    # Overleaf-ready bundle
            ├── prompt-full-bill.md    # the generating prompt, verbatim
            ├── output-full-bill.md    # the narrative output of this step
            └── sections/           # 11 comparative-print sections, each finished + marked
                ├── s301.tex s321.tex s331.tex s351.tex s355g.tex
                └── s360.tex s360c.tex s360e.tex s360e-4.tex s360j.tex s360k.tex
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

## Papers Directory READMEs

As of v2.3.1 the [papers/](papers) directory carries five comprehensive landing READMEs that document the four sequential VVUQ works as one evidence-to-law pipeline. The [papers README](papers) details the verification developments and progress for each of the four works, shows the building process from one work to the next with ASCII diagrams, and discusses what the results mean for the new Physical AI oncology trial industry, the processing feat accomplished by AI, and the accelerated timeline versus conventional methods to reach the final VVUQ-04 bill. One landing README per work then focuses on that work alone, each with DOI badges, the repository structure, ASCII diagrams of the building process within the work, and the final paper or bill DOI shown in an organized way.

| Landing page | Focus | Final paper or bill DOI |
|:--|:--|:--|
| [papers](papers) | All four works, lineage, and the final DOIs | the four below |
| [papers/VVUQ-01](papers/VVUQ-01) | Two Stage VVUQ method paper | [10.5281/zenodo.20372501](https://doi.org/10.5281/zenodo.20372501) |
| [papers/VVUQ-02](papers/VVUQ-02) | Mobile humanoid priority VVUQ paper | [10.5281/zenodo.20421754](https://doi.org/10.5281/zenodo.20421754) |
| [papers/VVUQ-03](papers/VVUQ-03) | VVUQ Physical AI Oncology Trial Bill (H. R. 9510) | [10.5281/zenodo.20454870](https://doi.org/10.5281/zenodo.20454870) |
| [papers/VVUQ-04](papers/VVUQ-04) | FD&C Act amendment (H. R. 9510) | [10.5281/zenodo.20485580](https://doi.org/10.5281/zenodo.20485580) |

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

## VVUQ-02 Full Paper

As of v1.2.0 the full manuscript is realized under [papers/VVUQ-02/full-paper](papers/VVUQ-02/full-paper), built from the v1.1.0 draft scaffold without modifying it. Every bracketed processing instruction in the eight body sections is replaced with grounded, publication-grade prose and left-aligned tables set to the body text width, while the title page, the Palatino and navy style, the 41 entry `ieeetr` bibliography, and the back matter are carried over. The manuscript renders the recorded assurance evidence: the 172 of 172 tests with 64 in the ten-gate suite, the five ACCEPT, BLOCK, and ESCALATE decision cases, the ten gate thresholds tightening toward the three catastrophe gates, the 32 of 32 sweep at composite mean near 93.6, the four-entrant tournament, the featured 1000-row sensor stream, and byte-for-byte determinism from seed 20260525.

```
  draft-paper/ (scaffold)                     full-paper/ (this release)
  +---------------------------+               +---------------------------+
  | [bracketed instructions]  |   process     | finished prose + tables   |
  | + final references.bib    | ============> | + 13 body-width tables    |
  | + five \autoref figures   |   +grounding  | + five \autoref figures   |
  +---------------------------+               +---------------------------+
        the build order  ----------------->   the 70+ page manuscript
```

The four-entrant tournament is the comparison the abstract foregrounds: the single mobile humanoid lands second to the eight-arm PancreSpeed cart by under half a composite point, because parallel arms shorten the throughput-weighted score, whereas the prior PDAC paper featured that multi-arm baseline alone; the humanoid is nonetheless the higher-risk, higher-assurance platform the paper is built around. The five figures use placeholder slots that compile immediately and are replaced once the author drops the PNGs into `Images/`. A `full-paper.zip` bundle is provided for a one step Overleaf upload, and the additions are LaTeX, Markdown, and a zip, all outside the `ruff` and `yamllint` surface, so the CI stays green. See the [full-paper README](papers/VVUQ-02/full-paper) for the headline-results and leaderboard tables and the formatting rules.

## VVUQ-03 Draft Paper

As of v1.3.0 a new draft paper is staged under [papers/VVUQ-03/draft-paper](papers/VVUQ-03/draft-paper): the *VVUQ Physical AI Oncology Trial Bill* (Draft 1.0), a proposed United States bill that would require an automated VVUQ verification process to clear robot-patient interaction code before that code is generated or executed in a Physical AI oncology clinical trial. It is built from the VVUQ-03 template-paper (the 21 CFR Part 312 adaptation) with the CFR context removed and new section names created, and is a head start, not a finished bill: every body section is a bracketed processing instruction that names the exact VVUQ-01, VVUQ-02, national-platform, and template files a future Claude Code Opus 4.8 (1M) Max pass must read. The four required main points (algorithm documentation; attestations and compliance; prior law; and supporting documentation referenced, not attached) are each a section; USL and PSL are given full treatment for their synergistic effect on the VVUQ process; the fourteen external standards and two clinical baselines and the featured 1790-line `comparison.json` and 1001-row `sample_h2_sensor.csv` are wired in; and the federal laws (with the antidiscrimination citation corrected to 42 U.S.C.) and the New York, Texas, California, and Florida statutes are cited in a 60-entry bibliography with clickable DOIs and URLs and no `howpublished` field.

```
  VVUQ-01 + VVUQ-02 + national-platform + template
       (evidence, standards, simulations, cover model)
                          |
                          v
  VVUQ-03/draft-paper  ====>  [bracketed instructions per section]
          |                   + final references.bib + Overleaf zip
          v
  VVUQ-03 full-paper / final-paper   (future 70+ page bill)
```

The additions are LaTeX, Markdown, and a zip, all outside the `ruff` and `yamllint` surface, so the CI stays green. See the [draft-paper README](papers/VVUQ-03/draft-paper) for the DOI badges, the section-to-source map, the build-validation note, and the senior-author formatting rules.

## VVUQ-03 Full Paper

As of v1.4.0 the full bill is realized under [papers/VVUQ-03/full-paper](papers/VVUQ-03/full-paper), built from the v1.3.0 draft scaffold without modifying it. Every bracketed processing instruction in the fifteen sections becomes finished, publication-quality legislative prose and left-aligned tables set to the body text width (21 tables in all), while the navy Palatino style and the 60-entry `ieeetr` bibliography are carried over. The instrument is designated **H.R. 9510** (119th Congress, 2d Session), a 2026-specific number confirmed unused in the current Congress, with the short title *Verification Before Generation in Physical AI Oncology Trials Act of 2026* and an enacting clause. The Draft Statutory Text is enactable language in Sections 1 to 9 with the (a)(1)(i) hierarchy: verification before generation, the ten gate thresholds in one full-width table bound to the fourteen external standards and two clinical baselines, the PSL and USL readiness gates with Phase 0 validation, documentation and attestation, cybersecurity and human oversight, nondiscrimination, and enforcement. Algorithm Documentation features the 1790-line four-entrant `comparison.json` and the 1001-row non-repetitive `sample_h2_sensor.csv`, and the four required main points are each a section.

```
  VVUQ-03/draft-paper (scaffold)              VVUQ-03/full-paper (this release)
  [bracketed instructions per section]   ==>  finished legislative prose + 21 tables
  + final references.bib + Overleaf zip       H.R. 9510; Sections 1 to 9; no images
```

The additions are LaTeX, Markdown, a `.bib`, a `.sty`, and a zip, all outside the `ruff` and `yamllint` surface, so the CI stays green. See the [full-paper README](papers/VVUQ-03/full-paper) for the DOI badges, the bill-identity table, the section-to-source map, and the senior-author formatting rules.

## VVUQ-04 Instruct Bill

As of v2.0.0 a new instruction set is staged under [papers/VVUQ-04/instruct-bill](papers/VVUQ-04/instruct-bill): structured U.S. medical AI bill and law summaries, current through May 31, 2026, that give the next Claude Code Opus 4.8 (1M context) Max pass a head start in producing a more current and relevant draft of the *VVUQ Physical AI Oncology Trial Bill* (H.R. 9510), which is then converted to XML in a later step. Ten markdown files each cover one legal domain: federal statutes (01); FDA AI device regulation (02); ONC and ASTP algorithm transparency (03); CMS coverage and payment (04); privacy, security, and nondiscrimination (05); state medical AI laws (06); executive actions and national AI strategy (07); emerging federal bills as research influences (08); VVUQ and robotics standards with clinical-trial and oncology law (09); and a legal crosswalk, research matrix, and bill-style template (10). Five BibTeX bibliographies carry 145 entries with DOIs and URLs, no `howpublished` field, and no duplicate links, and a README maps every file-to-file and file-to-bibliography correlation. The emerging bills and executive actions are flagged as research influences for a memo, appendix, testimony, or research matrix, not for operative bill text.

```
  Ten domain summaries (01 to 09)            Synthesis and reuse
  federal + state + agency + standards  ==>  10 crosswalk: operative vs memo
  five .bib (statutes; rules; state;         + structured law format for XML
  exec and bills; standards)                 + prior bill at VVUQ-03/final-paper
```

The additions are Markdown and BibTeX, all outside the `ruff` and `yamllint` surface, so the lint-and-format CI job stays green across Python 3.10, 3.11, and 3.12. See the [instruct-bill README](papers/VVUQ-04/instruct-bill) for the DOI badges, the repository structure, the correlation diagrams, and the operative-versus-influence rule.

## VVUQ-04 Template Bill (LaTeX)

As of v2.1.0 a LaTeX template bill is staged under [papers/VVUQ-04/template-bill/LaTeX](papers/VVUQ-04/template-bill/LaTeX): a faithful reproduction of the official United States Code, Title 21 - Food and Drugs (current through Public Law 119-93), reduced from 29 chapters and 757 sections to the 11 Federal Food, Drug, and Cosmetic Act device sections relevant to the Physical AI oncology trial context. The source is the OLRC USLM XML in `papers/VVUQ-04/template-bill/xml_usc21@119-93.zip`. The section selection follows the legal crosswalk in `papers/VVUQ-04/instruct-bill` and the statutory crosswalk in `papers/VVUQ-03/final-paper`; no bracketed instructions or file names are inserted into the law, so a future Claude Code Opus 4.8 (1M context) Max pass can read the laws in place and, with the instruct-bill and the final paper, draft the amendment to Public Law 119-93, Title 21.

The retained sections are the device-regulation backbone of the Act: § 301 (short title), § 321 (definitions; the device definition in (h)), § 331 (prohibited acts), § 351 (adulterated devices), § 355g (real world evidence), § 360 (registration; the 510(k) pathway in (k)), § 360c (classification), § 360e (premarket approval), § 360e-4 (predetermined change control plans, the keystone for an automated verification-before-change rule), § 360j (general device provisions; the software and CDS exclusion in (o)), and § 360k (state preemption). Each section is its own `.tex` file wired into one `main.tex`; `usctitle.sty` renders the bold catchlines, the hanging-indent (a)(1)(A)(i)(I) hierarchy, the centered cross-headings, the small-caps note headings, and the parenthetical source credits in the United States Code look and feel.

```
  Title 21 USLM XML (29 chapters, 757 sections)
        |  keep only the FD&C Act device pathway
        v
  Chapter 9 (FD&C Act): define -> classify -> clear/approve -> change-control
   s321(h) + s360j(o)  ->  s360c  ->  s360(k) / s360e  ->  s360e-4
        |  plus s351 (quality), s331 (enforcement), s355g (evidence),
        |  s360k (preemption), s301 (short title)
        v
  main.tex + usctitle.sty + references.bib + 11 sections -> Overleaf PDF
        |  same look and feel as the United States Code
        v
  Next pass: amend Public Law 119-93, Title 21 (new section after s360e-4)
```

The additions are LaTeX, BibTeX, Markdown, and a zip, all outside the `ruff` and `yamllint` surface, so the lint-and-format CI job stays green across Python 3.10, 3.11, and 3.12. See the [template-bill/LaTeX README](papers/VVUQ-04/template-bill/LaTeX) for the DOI badges, the per-section contents table, the statutory-layering and file-correlation diagrams, the exclusion rationale, and the Overleaf compile recipe.

## VVUQ-04 Draft Bill (LaTeX)

As of v2.2.0 a LaTeX draft amendment is staged under [papers/VVUQ-04/draft-bill](papers/VVUQ-04/draft-bill): a draft amendment to the Federal Food, Drug, and Cosmetic Act (21 U.S.C. § 301 et seq.) that recasts the prior *VVUQ Physical AI Oncology Trial Bill* (H.R. 9510) as a properly targeted amendment. Following the amendment-drafting correction, it amends the Act and cites each affected provision by its 21 U.S.C. section number, naming Public Law 119-93 only as the currency point, rather than amending Public Law 119-93 or Title 21 generally. It is an amendment scaffold with bracketed DRAFTING INSTRUCTIONS, not a finished bill: under each part, a draftbox names the exact files in `papers/VVUQ-04/instruct-bill` and `papers/VVUQ-03/final-paper` that a future Claude Code Opus 4.8 (1M context) Max pass must process to produce publication-quality statutory text.

The operative mechanism is a new section 515D of the Act (21 U.S.C. § 360e-5), "Verification before generation of robot-patient interaction code in Physical AI oncology investigations," inserted after the predetermined change control plan authority (§ 515C; § 360e-4), with conforming amendments to the device definition (§ 321(h)), prohibited acts (§ 331), adulteration (§ 351), real world evidence (§ 355g), the 510(k) pathway (§ 360(k)), classification (§ 360c), premarket approval (§ 360e), the change-control keystone (§ 360e-4), the software and CDS exclusion (§ 360j(o)), and state preemption (§ 360k). Each of the 11 reproduced sections keeps its original statutory text and adds a draftbox of bracketed instructions with exact directories and file names. The emerging 119th Congress bills and executive actions are kept to a non-operative Research Influence Matrix appendix, the findings, or a memo.

```
  VVUQ-03/final-paper + VVUQ-04/instruct-bill + VVUQ-04/template-bill
        |  prior bill text + medical-AI law crosswalk + Title 21 sections
        v
  draft-bill: amend the Federal Food, Drug, and Cosmetic Act
   SECTION 1 short title -> SEC. 2 findings -> SEC. 3 amendment
   (new § 360e-5 after § 360e-4, plus conforming) -> SEC. 4 comparative print
        |  each part = original text + bracketed DRAFTING INSTRUCTIONS
        v
  Next pass: process the named files to produce the finished amendment
```

The additions are LaTeX, BibTeX, Markdown, and a zip, all outside the `ruff` and `yamllint` surface, so the lint-and-format CI job stays green across Python 3.10, 3.11, and 3.12. See the [draft-bill README](papers/VVUQ-04/draft-bill) for the DOI badges, the amendment-structure map, the per-section contents table, the statutory-layering and file-correlation diagrams, and the Overleaf compile recipe.

## VVUQ-04 Full Bill (LaTeX)

As of v2.3.0 the finished LaTeX amendment is staged under [papers/VVUQ-04/full-bill](papers/VVUQ-04/full-bill): **H. R. 9510**, the *Verification Before Generation in Physical AI Oncology Trials Act of 2026*, produced from the v2.2.0 draft scaffold by executing every bracketed drafting instruction against the named `papers/VVUQ-04/instruct-bill` and `papers/VVUQ-03/final-paper` sources. The drafting-instruction blocks are gone and the operative text is fully drafted: SECTION 1 short title and table of contents, SEC. 2 with 14 grounded findings, SEC. 3 the new section 515D plus ten conforming amendments and the clerical, rule-of-construction, and effective-date changes, and SEC. 4 a focused comparative print of the changes in existing law.

The operative mechanism is a new section 515D of the Act (21 U.S.C. § 360e-5): no robot-patient interaction code may be generated or executed in a Physical AI oncology investigation until an automated verification, validation, and uncertainty quantification process bound to named external standards has cleared, with the cleared record documented and attested. Subsections (a) through (j) carry the requirement, the order of operations, the ten-gate threshold schedule, the readiness gates, documentation and attestation, cybersecurity and oversight, nondiscrimination, regulations, definitions, and a rule of construction. Appendix A keeps the emerging 119th Congress bills and executive actions to a non-operative research-influence matrix; Appendix B records the v2.0.0 to v2.3.0 development and the implementation pathway for lawmakers.

```
  VVUQ-04/draft-bill (v2.2.0 scaffold + bracketed DRAFTING INSTRUCTIONS)
        |  execute each instruction against the named instruct-bill and
        |  final-paper files; anchor each duty to an in-force authority
        v
  full-bill: H. R. 9510, finished amendment to the FD&C Act
   SECTION 1 short title -> SEC. 2 findings -> SEC. 3 new section 360e-5
   + conforming -> SEC. 4 comparative print -> Appendix A -> Appendix B
        |  drafting instructions removed; header, URL, and table formatting fixed
        v
  Overleaf-ready bundle (main.tex, usctitle.sty, references.bib, 11 sections, zip)
```

This finished version fixes the issues flagged in the draft: the running header is abbreviated so no two fields overlap, long reference URLs break rather than run off the page, and every table is set to the body measure with left-aligned ragged-right columns. The additions are LaTeX, BibTeX, Markdown, and a zip, all outside the `ruff` and `yamllint` surface, so the lint-and-format CI job stays green across Python 3.10, 3.11, and 3.12. See the [full-bill README](papers/VVUQ-04/full-bill) for the DOI badges, the what-changed table, the section 515D subsection map, the per-section comparative-print table, and the Overleaf compile recipe.

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
