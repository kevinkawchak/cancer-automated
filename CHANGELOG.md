# Changelog

All notable changes to this repository are documented here.
Format follows [Keep a Changelog](https://keepachangelog.com/).

## [Unreleased]

## [0.5.0] - 2026-05-25

### Added
- `papers/VVUQ-01/draft-paper/`: a complete and compilable single column LaTeX
  scaffold for the manuscript "Two Stage VVUQ Oncology Clinical Trial
  Verification Automation Priority over Existing Generated Code", authored
  autonomously by Claude Code Opus 4.7 (1M context) Max, one file per commit,
  each pushed to GitHub in real time as part of a single pull request. The
  seven body section files (`sections/abstract.tex`, `introduction.tex`,
  `methods.tex`, `results.tex`, `discussion.tex`, `limitations_future.tex`,
  `conclusions.tex`) carry bracketed processing instructions that name the
  exact repository directories and files to process for a future 70+ page
  paper. The title page (`main.tex`), style (`new_paper.sty`), bibliography
  (`references.bib`), references section (`sections/references.tex`), and back
  matter (`sections/back_matter.tex`) are final.
- `references.bib`: 29 final entries rendered with `ieeetr`. Every DOI entry
  carries its human readable DOI string and a clickable resolver URL in the
  note; repository entries carry both a GitHub and a Zenodo URL, each once,
  with no duplicate link and no `howpublished` field. Both the repository DOI
  and the paper DOI are clickable.
- `draft-paper.zip`: an Overleaf ready bundle of the LaTeX project.

### Changed
- `README.md`: release badge updated to v0.5.0, a new v0.5.0 summary added
  above the v0.4.0 summary, a VVUQ-01 draft paper section and table of contents
  entry added, the repository structure now expands
  `papers/VVUQ-01/draft-paper`, and the citation version was bumped.
- `releases.md`: v0.5.0 release notes added above the v0.4.0 notes.
- @kevinkawchak removed images from cancer-automated/tree/main/papers/VVUQ-01/imagegen subdirectories, and linked images to Google Drive to reduce repository file size from 4.7MB to 450KB on 2026-05-24.

### Notes
- This release adds a paper scaffold only; it does not change the executable
  v0.1.0 source modules or the v0.2.0 through v0.4.0 records. The additions are
  LaTeX, Markdown, and a zip, all outside the `ruff` and `yamllint` surface, so
  `lint-and-format` (ruff check, ruff format check, yamllint) stays green across
  Python 3.10, 3.11, and 3.12, alongside `validate-scripts` and `test` (51
  passed, 0 skipped).
- All prose uses single dashes only; triple dashes are reserved for Markdown
  rules, table separators, and YAML document separators.

## [0.4.0] - 2026-05-23

### Added
- `papers/VVUQ-01/imagegen/`: the rendered realization of the 10 v0.3.0 image
  instructions, authored autonomously by Claude Code Opus 4.7 (1M context) Max.
  Each numbered subdirectory holds one self contained matplotlib script
  `NN-name/NN-name.py` (the generated code) and the portrait, full page, 300 dpi
  figure `NN-name/NN-name.png` it produces (the execution output, 2550 by 3300
  pixels, white background only). A comprehensive `README.md` documents the
  rendered gallery, the generated code versus execution split, the shared page
  frame and palette, and reproduction with matplotlib.
- The 10 figures use professional chart families and avoid basic bar, pie, and
  line charts: `01-vvuq-gate-funnel` (funnel), `02-acceleration-waterfall`
  (waterfall), `03-five-methods-flowchart` (process flowchart),
  `04-vvuq-assurance-wheel` (radar wheel), `05-pdac-pilot-timeline` (Gantt),
  `06-test-coverage-treemap` (treemap), `07-lights-off-state-machine` (state
  diagram), `08-fda-cost-efficiency-bridge` (financial bridge and bullets),
  `09-value-proposition-matrix` (matrix), and `10-file-generation-sankey`
  (Sankey). Every number traces to code generation (v0.1.0) or code execution
  (v0.2.0).

### Changed
- `README.md`: release badge updated to v0.4.0, a new v0.4.0 summary added above
  the v0.3.0 summary, the figures section text diagram and closing links updated
  to reflect the rendered build, the repository structure now expands
  `papers/VVUQ-01/imagegen` with its README and the 10 figure subdirectories,
  and the citation version was bumped.
- `releases.md`: v0.4.0 release notes added above the v0.3.0 notes.
- Removed the `papers/VVUQ-01/imagegen/a.md` placeholder now that the directory
  holds the rendered scripts and figures.

### Notes
- This release renders the figures specified in v0.3.0; it does not change the
  executable v0.1.0 source modules or the v0.2.0 and v0.3.0 records. Each script
  depends only on `matplotlib` and `numpy` and renders headless via the `Agg`
  backend. Rendering requires `matplotlib`; the core CI does not install it and
  the `test` job does not import `imagegen/`, so `lint-and-format` (ruff check,
  ruff format check, yamllint) and `test` (51 passed, 0 skipped) stay green
  across Python 3.10, 3.11, and 3.12 because the scripts are ruff clean.
- All prose uses single dashes only; triple dashes are reserved for Markdown
  rules, table separators, and YAML document separators.

## [0.3.0] - 2026-05-23

### Added
- `papers/VVUQ-01/image-instruct/`: 10 comprehensive image instructions plus a
  master `README.md`, authored autonomously by Claude Code Opus 4.7 (1M context)
  Max. Each instruction is a complete, self contained specification for one
  publication ready, portrait, full page, 300 dpi figure, grounded in code
  generation (v0.1.0) and code execution (v0.2.0). The master README defines the
  processing model, the directory and file naming, the shared page frame, the
  palette and typography, the symbol and dash rules, the index, the grounding
  sources, the future imagegen workflow, and the acceptance criteria.
- The 10 instructions use professional chart families and avoid basic bar, pie,
  and line charts: `01-vvuq-gate-funnel` (funnel), `02-acceleration-waterfall`
  (waterfall), `03-five-methods-flowchart` (process flowchart), `04-vvuq-assurance-wheel`
  (radar wheel), `05-pdac-pilot-timeline` (Gantt), `06-test-coverage-treemap`
  (treemap), `07-lights-off-state-machine` (state diagram), `08-fda-cost-efficiency-bridge`
  (financial bridge and bullets), `09-value-proposition-matrix` (matrix), and
  `10-file-generation-sankey` (Sankey).

### Changed
- `README.md`: release badge updated to v0.3.0, the repository structure now
  shows `papers/VVUQ-01/image-instruct` and `papers/VVUQ-01/imagegen`, a new
  figures section with a text diagram and a table of contents entry was added,
  the citation version was bumped, and a v0.3.0 release line was added.
- `releases.md`: v0.3.0 release notes added above the v0.2.0 notes.

### Notes
- This release adds instructions only. No matplotlib script and no PNG file is
  generated yet; those are produced at a future date under
  `papers/VVUQ-01/imagegen/`, which requires `matplotlib` in the rendering
  environment. The additions are Markdown and fall outside the `ruff` and
  `yamllint` surface, so `lint-and-format` stays green across Python 3.10, 3.11,
  and 3.12, alongside `validate-scripts` and `test` (51 passed, 0 skipped).
- Prior code generation (v0.1.0) and code execution (v0.2.0) files are unchanged.
- All prose uses single dashes only; triple dashes are reserved for Markdown
  rules, table separators, and YAML document separators.

## [0.2.0] - 2026-05-23

### Added
- `papers/VVUQ-01/execution/`: the complete execution record of the v0.1.0
  codebase and the Stage 2 2030 PDAC procedure code, produced autonomously by
  Claude Code Opus 4.7 (1M context) on Python 3.11.15. Includes a comprehensive
  index `README.md` with badges, ASCII diagrams, a file-generation-outcomes
  summary, the full process narrative, limitations, and a comparison with
  conventional high-end server processing.
- `01-foundation/`: environment and dependency posture, the
  `verify_installation.py` output, the full `pytest` run (51 passed, 0 skipped
  across 8 test modules), and the `ruff` and `yamllint` static-analysis evidence.
- `02-pipeline/`: the three pipeline examples run end to end, the four generated
  artifacts (instructions, generated code, execution log, paper), and per-stage
  logs and timing. The acceleration factor is 2.5 (30 baseline to 12 automated
  days).
- `03-vvuq/`: the three vvuq examples plus the full gate decision surface across
  six cases (one accept, five block, one escalate), demonstrating the gate is
  held higher than code generation.
- `04-stage1-automation/`: the seven simulation, ingestion, chunking, and
  scheduler examples, an independent chunk-losslessness verification, and a
  documented multibyte hard-split limitation.
- `05-physical-ai-stage2/`: the two physical-ai examples, the full lights-off
  factory safety surface, and the 2030 PDAC hybrid pilot timeline (60-second
  8-arm Whipple plus six 28-day Daraxonrasib cycles, 168 regimen days).

### Changed
- `README.md`: release and contributors badges updated for v0.2.0, the
  repository structure now shows `papers/VVUQ-01/execution`, and a v0.2.0
  release line was added.

### Notes
- This release is an execution and documentation record; it does not change the
  executable v0.1.0 source modules.
- The `lint-and-format` CI workflow remains green across Python 3.10, 3.11, and
  3.12, alongside `validate-scripts` and `test`.
- All prose uses single dashes only; triple dashes are reserved for Markdown
  rules, table separators, and YAML document separators.

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

[Unreleased]: https://github.com/kevinkawchak/cancer-automated/compare/v0.5.0...HEAD
[0.5.0]: https://github.com/kevinkawchak/cancer-automated/compare/v0.4.0...v0.5.0
[0.4.0]: https://github.com/kevinkawchak/cancer-automated/compare/v0.3.0...v0.4.0
[0.3.0]: https://github.com/kevinkawchak/cancer-automated/compare/v0.2.0...v0.3.0
[0.2.0]: https://github.com/kevinkawchak/cancer-automated/compare/v0.1.0...v0.2.0
[0.1.0]: https://github.com/kevinkawchak/cancer-automated/releases/tag/v0.1.0
