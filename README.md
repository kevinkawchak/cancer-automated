# Production Automated Physical AI Oncology Trial Daily Deliverables

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Release](https://img.shields.io/badge/Release-v0.1.0-brightgreen.svg)](releases.md)
[![Last Updated](https://img.shields.io/badge/Updated-May%202026-blue.svg)](CHANGELOG.md)
[![Python](https://img.shields.io/badge/Python-3.10%20|%203.11%20|%203.12-blue.svg)](https://www.python.org/)
[![Protocol](https://img.shields.io/badge/Protocol-MCP-purple.svg)](https://modelcontextprotocol.io/)
[![CI](https://img.shields.io/badge/CI-lint%20and%20format-blue.svg)](.github/workflows/ci.yml)
[![Contributors](https://img.shields.io/badge/Contributors-2-blue.svg)](releases.md)

**Production-ready, scalable automation for Physical AI oncology trial daily deliverables, by Claude Code Opus 4.7, Cowork; building on developments proven across physical-ai-oncology-trials, robotic-surgeries, and Clinical-AI-Demos.**

This repository packages the established methods for generating instructions, generating code, executing code, and creating papers into a single repeatable daily-deliverable pipeline. It then layers verification, validation, and uncertainty quantification (VVUQ), triple simulation, robust web and PDF ingestion, and autochunking on top, so each deliverable is produced faster and with higher assurance.

> **Thesis.** Production-ready, scalable, and automated Physical AI oncology trial daily deliverables are obtained based on established methods for generating instructions, code, code execution, and creating papers, and are further automated, accelerated, and the VVUQ is improved.

**5/21: v0.1.0 (Initial Automation Platform)** First release of the daily-deliverable pipeline (instruction, code generation, execution, paper assembly), the VVUQ gate held to a higher standard than code generation, triple simulation with consensus, robust web and PDF ingestion, 200K autochunking with per-chunk READMEs, and a non-stop commit scheduler. See [releases.md](releases.md) for full release notes.

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
└── tests/                          # 9 test modules, run with: pytest tests/
    ├── conftest.py
    ├── test_foundation.py
    ├── test_pipeline.py
    ├── test_vvuq.py
    ├── test_simulation.py
    ├── test_ingestion.py
    ├── test_chunking.py
    ├── test_scheduler.py
    └── test_physical_ai.py
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
  version = {0.1.0},
  year = {2026},
  publisher = {GitHub},
  url = {https://github.com/kevinkawchak/cancer-automated}
}
```

## License

MIT License. See [LICENSE](LICENSE) for details.
