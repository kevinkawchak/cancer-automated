# Changelog

All notable changes to this repository are documented here.
Format follows [Keep a Changelog](https://keepachangelog.com/).

## [Unreleased]

## [0.1.0] - 2026-05-21

### Added
- Repository foundation: `ruff.toml`, `requirements.txt`, `.gitignore`, and the
  community-health files (`CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`, `SECURITY.md`,
  `SUPPORT.md`, `CITATION.cff`).
- Continuous integration at `.github/workflows/ci.yml` with `lint-and-format`
  (ruff check, ruff format check, yamllint) across Python 3.10, 3.11, and 3.12,
  plus `validate-scripts` and `test` jobs. Pull request and issue templates.
- `pipeline/`: the daily-deliverable engine. A pure standard-library deliverable
  data model (`deliverable.py`) plus the four producing stages
  (`instruction_stage.py`, `codegen_stage.py`, `execution_stage.py`,
  `paper_stage.py`) and `orchestrator.py`, with examples and tests.
- `vvuq/`: verification, validation, and uncertainty quantification plus the
  `vvuq_gate.py` gate held to a higher standard than code generation, with
  examples and tests for the accept, block, and escalate paths.
- `simulation/`: `triple_runner.py` runs every project three times and
  `consensus.py` aggregates the runs and flags divergent metrics.
- `ingestion/`: `web_search.py` with bounded exponential-backoff retries and an
  offline fallback, and `pdf_processor.py` with a guarded backend and a 200K
  chunk estimate.
- `chunking/`: `chunker.py` autochunks under the 200K per-file cap and
  `readme_generator.py` emits a reconstruction README per chunk set.
- `scheduler/`: `commit_scheduler.py` plans an evenly spaced, non-stop commit
  cadence.
- `physical-ai/`: `lights_off_factory.py` (safety-gated autonomous batch runner)
  and `hybrid_surgery_medicine.py` (combined surgery and medicine pilot
  timeline), disabled by default.
- `configs/pipeline_config.yaml`, `configs/vvuq_thresholds.yaml`,
  `scripts/verify_installation.py`, and the `tests/` harness.
- Comprehensive `README.md` with badges, table of contents, ASCII pipeline and
  roadmap diagrams, the full repository structure, and `releases.md` with the
  v0.1.0 release notes.

### Notes
- The `lint-and-format` CI workflow is green across Python 3.10, 3.11, and 3.12.
- All prose uses single dashes only; triple dashes are reserved for Markdown
  rules, table separators, and YAML document separators.

[Unreleased]: https://github.com/kevinkawchak/cancer-automated/compare/v0.1.0...HEAD
[0.1.0]: https://github.com/kevinkawchak/cancer-automated/releases/tag/v0.1.0
