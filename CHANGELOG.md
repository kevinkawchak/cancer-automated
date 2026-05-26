# Changelog

All notable changes to this repository are documented here.
Format follows [Keep a Changelog](https://keepachangelog.com/).

## [Unreleased]

## [1.0.0] - 2026-05-26

### Added
- `papers/VVUQ-02/imagegen/`: the 15 rendered figures, authored by Claude Code Opus
  4.7 (1M context) Max running autonomously in a managed cloud container across 15
  commits in a single pull request, one figure per commit pushed to GitHub in real
  time, then a 16th commit for the error-fix and consistency pass and a 17th commit
  for the repository updates. Each figure is one self-contained `NN-name.py`
  matplotlib script (the generated code) and one `NN-name.png` (the execution
  output), portrait `figsize=(8.5, 11)` at 300 dpi (2550 by 3300 pixels), white
  background only with no dark mode, rendering its v0.9.0 specification with no
  manual positioning.
- 15 distinct chart families rendered from the codegen (v0.7.0) and execution
  (v0.8.0) records: platform pipeline flow, gate decision funnel, ten-gate threshold
  forest, gate to standard binding matrix, clinical and regulatory standards wheel,
  172-test coverage treemap, validation parity scatter, sweep composite strip plot,
  composite weighting waterfall, four-entrant comparison box plot, sensor stream
  safety bands, eight-phase Whipple swimmer, assurance cost assessment, value
  proposition matrix, and platform mind map. Six satisfy the required-data brief.
- A comprehensive `imagegen/README.md` with DOI and status badges, the conventions,
  the 15-figure index, the data-availability mapping, repository-structure and
  spec-to-script-to-PNG ASCII diagrams, the reproduction note, and the verification
  pass.
- `prompt-imagegen.md` (the generating prompt, verbatim) and `output-imagegen.md`
  (the narrative markdown output of this run).

### Changed
- Top-level `README.md`: release badge to v1.0.0, a v1.0.0 summary above the prior
  summary, a VVUQ-02 Imagegen section with an ASCII flow diagram and a table of
  contents entry, the repository structure tree (the imagegen directory expanded to
  the rendered figure set), and the cross-references in the VVUQ-02 image
  instructions section.
- `releases.md` (v1.0.0 release notes), this `CHANGELOG.md` (v1.0.0), and
  `CITATION.cff` (v1.0.0).

### Notes
- Every script is pure `matplotlib` plus `numpy`, sets `matplotlib.use("Agg")`, and
  passes `ruff check` and `ruff format --check` repository-wide, so the
  `lint-and-format` CI job stays green across Python 3.10, 3.11, and 3.12; the
  `test` and `validate-scripts` jobs do not import `imagegen/`. Re-rendering is
  deterministic (byte-identical PNGs; any jitter is seeded). The arithmetic
  reconciles (treemap 172, weights 1.00, swimmer 60 s, appearances 256, sweep
  min/max/mean). No images, Mermaid diagrams, or colored images are added to any
  Markdown. The v0.9.0 image instruction files are not modified, and only
  `kevinkawchak/cancer-automated` was edited.

## [0.9.0] - 2026-05-26

### Added
- `papers/VVUQ-02/image-instruct/`: 15 comprehensive image instructions plus a
  master README, authored by Claude Code Opus 4.7 (1M context) Max running
  autonomously in a managed cloud container across 15 commits in a single pull
  request, one figure specification per commit pushed to GitHub in real time. The
  set specifies, ahead of any rendering, how a future agent builds 15 portrait,
  full-size, 300 dpi figures grounded in the codegen (v0.7.0) and execution
  (v0.8.0) records. Instructions only; no script and no image is rendered here.
- 15 distinct chart families chosen from a 20-family menu for best data
  availability and relevance (no family reused, and no basic bar, pie, or line
  chart): workflow pipeline flow, gate decision funnel, ten-gate threshold forest,
  gate to standard binding matrix, clinical and regulatory standards wheel,
  172-test coverage treemap, validation parity scatter, sweep composite strip plot,
  composite weighting waterfall, four-entrant comparison box plot, sensor stream
  safety bands, eight-phase Whipple swimmer, assurance cost assessment, value
  proposition matrix, and platform mind map.
- Six figures satisfy the required-data brief: the 172 tests (treemap), the
  external-standards anchoring (binding matrix), the 10 gates and thresholds
  (forest), the clinical and regulatory corpus (wheel), the featured 1000-row H2
  sensor stream (line with bands), and the four-entrant comparison featuring the
  second-place mobile humanoid (box plot).
- `prompt-image-instruct.md` (the generating prompt, verbatim) and
  `output-image-instruct.md` (the narrative markdown output of this run).
- A master `README.md` with DOI and status badges, the shared page frame, palette,
  font, symbol, and dash conventions, the processing model for Claude Code Opus 4.7
  (1M) Max, the data-availability mapping, repository-structure ASCII diagrams, the
  file-generation outcomes as a basis for a future technical paper, and a
  consistency and error-fix pass.

### Changed
- Top-level `README.md`: release badge to v0.9.0, a v0.9.0 summary above the prior
  summary, a VVUQ-02 Image Instructions section with an ASCII flow diagram and a
  table of contents entry, the repository structure tree (the image-instruct
  directory expanded to the 15 specifications), the corrected forward references in
  the VVUQ-02 codegen section, and the citation version.
- `releases.md` (v0.9.0 release notes), this `CHANGELOG.md` (v0.9.0), and
  `CITATION.cff` (v0.9.0).

### Notes
- The image-instruct pull request adds only Markdown, so it carries no Python or
  YAML and cannot introduce a `ruff` or `yamllint` failure; the `lint-and-format`,
  `validate-scripts`, and `test` CI jobs stay green across Python 3.10, 3.11, and
  3.12. No images, Mermaid diagrams, or colored images are added. The matplotlib
  scripts and 300 dpi PNG files are deferred to a future imagegen pull request. The
  assurance cost assessment figure uses an illustrative relative index, not
  measured dollars, with the direction grounded in the execution README. Only
  `kevinkawchak/cancer-automated` was edited.

## [0.8.0] - 2026-05-26

### Added
- `papers/VVUQ-02/execution/`: the complete run record of the
  `papers/VVUQ-02/codegen/` tree, produced by Claude Code Opus 4.7 (1M context)
  Max running autonomously in a managed cloud container across 8 commits in a
  single pull request, one large section per commit pushed to GitHub in real time.
- `01-foundation/`: the host (CPython 3.11.15 on Linux), the dependency posture,
  a byte-for-byte determinism check that reproduces the committed sensor CSV, the
  4-entrant comparison, and the 32-iteration sweep index from seed 20260525, the
  172-test suite (0 skipped, the 10-gate suite carries 64 of the 172), and the CI
  lint-and-format checks, all green.
- `02-pipeline/`: the intent to compile to act to score record across six
  behavior groups (autonomy at concordance 1.000, kinematics, perception, hands,
  balance, suturing), with a verbatim execution log.
- `03-vvuq/`: the 10-gate decision surface over five cases (10 ACCEPT nominal,
  three distinct BLOCK mechanisms, one ESCALATE at coefficient of variation
  0.163), with the captures, the nominal report, and a decisions JSON carrying
  each gate's resolved external standards.
- `04-automation/`: the 32-iteration sweep (32 of 32 clear all 10 gates,
  composite mean 93.56), the gated composite, the Zenodo L0 pointer discipline,
  and a structural analysis of the featured 1790-line four-entrant
  `comparison.json` (128 round verdicts, 100 percent caveat coverage).
- `05-humanoid-deployment/`: the 60-second 8-phase Whipple timeline, a structural
  analysis of the featured 1000-row, 27-column positional sensor stream (every
  row and every positional payload distinct, no repetition), and the three
  immediate-catastrophe safety surfaces (vascular no-fly, human collision, fault
  e-stop), each correct at the boundary.
- `prompt-execution.md` and `output-execution.md` recording the generating prompt
  verbatim and the narrative output of the execution step.

### Changed
- Top-level `README.md`: release badge to v0.8.0, a v0.8.0 summary above the prior
  summary, a VVUQ-02 Execution section with an ASCII flow diagram and a table of
  contents entry, the repository structure tree (the execution directory
  expanded), the corrected codegen test count (172), and the citation version.
- `releases.md` (v0.8.0 release notes), this `CHANGELOG.md` (v0.8.0), and
  `CITATION.cff` (v0.8.0).

### Notes
- The external standards (ASME V&V 40-2018, NASA-STD-7009A, FDA CM&S 2023, IEC
  80601-2-77, IEC 60601-1, ISO 13482, ISO/TS 15066, ISO 10218-1, ISO 9283, IEC
  62304, ISO 14971, ISO 13849-1, UL 4600, IEEE 7009) anchor the credibility of the
  run; every gate, behavior, and safety surface is traced to a published standard.
- All code ran from a scratch working directory with the codegen tree on
  `PYTHONPATH`, leaving the committed codegen tree pristine. No Python or notebook
  files were added outside the already-clean codegen tree, so the CI
  lint-and-format surface stays green across Python 3.10, 3.11, and 3.12. The
  paper template files in `papers/VVUQ-02/templates/Template_04/` were not
  processed. Only `kevinkawchak/cancer-automated` was edited.

## [0.7.0] - 2026-05-26

### Added
- `papers/VVUQ-02/codegen/`: the standalone generated codebase for 10
  humanoid-specific VVUQ gates on an autonomous Unitree H2-Surgical 1.0
  (hypothetical 2030 surgical variant) performing the 60-second 8-phase Whipple on
  patient PAT-PDAC-0001 with its own two dexterous hands. Authored by Claude Code
  Opus 4.7 (1M context) Max from `papers/VVUQ-02/instructions/output-instruct.md`
  across 11 commits in a single pull request, one set of files per commit pushed
  to GitHub in real time.
- The assurance layer (`src/vvuq/`) is held to a higher standard than code
  generation and is grounded in real-world standards: ASME V&V 40-2018 and
  NASA-STD-7009A for model credibility, IEC 80601-2-77 and IEC 60601-1 for robotic
  surgery, ISO 13482, ISO/TS 15066, ISO 10218-1, and ISO 9283 for service and
  collaborative robot safety, IEC 62304, ISO 14971, and ISO 13849-1 for software
  and risk, and UL 4600 and IEEE 7009 for autonomy and fail-safe design.
- Each of the 10 gates (handeye servo, finger force, balance, autonomous plan,
  grasp and handover, vascular no-fly, suturing, perception, human collision,
  fault and e-stop) verifies (pass fraction 1.0), validates against an independent
  reference in `data/reference/`, and quantifies uncertainty across seeded runs,
  deciding ACCEPT, BLOCK, or ESCALATE. The three immediate-catastrophe gates carry
  the tightest bounds and an extra hard predicate.
- `papers/VVUQ-02/inputs/standards/`: the real standards input corpus wired into
  the gate registry, plus clinical baselines (the 2025 Dutch cohort, the Callery
  Fistula Risk Score).
- `config/vvuq_thresholds.yaml`, `config/standards_map.yaml`, JSON Schema plus
  Protobuf plus Avro schemas, a deterministic 32-iteration Latin hypercube sweep
  (seed 20260525) where all 32 iterations clear all 10 gates, a 6-component
  composite reported only when all gates ACCEPT, a 4-entrant comparison tournament,
  and the Zenodo L0 pointer discipline.
- README placeholders for the future-use directories (`image-instruct`,
  `imagegen`, `execution`, `draft-paper`, `full-paper`, `final-paper`), plus
  `prompt-codegen.md` and `output-codegen.md` recording the generation lineage.

### Changed
- Updated the main README (release badge v0.7.0, a v0.7.0 summary above the prior
  summary, a VVUQ-02 section with an ASCII gate diagram and table of contents
  entry, the repository structure, and the citation version), this CHANGELOG, the
  releases file, and `CITATION.cff` (v0.7.0).

### Notes
- The H2-Surgical 1.0 is a clearly labeled hypothetical 2030 surgical variant;
  every value is simulation-only and paper-only, and comparisons are
  simulation-against-simulation. The codegen tree keeps `ruff check`,
  `ruff format --check`, and `yamllint` clean across Python 3.10, 3.11, and 3.12;
  its 169 tests include a 64-item 10-gate decision surface. Only
  `kevinkawchak/cancer-automated` was edited.

## [0.6.0] - 2026-05-25

### Added
- `papers/VVUQ-01/full-paper/`: the full manuscript "Two Stage VVUQ Oncology
  Clinical Trial Verification Automation Priority over Existing Generated Code",
  built from the v0.5.0 draft scaffold without modifying it, authored
  autonomously by Claude Code Opus 4.7 (1M context) Max, one commit per file and
  per section, each pushed to GitHub in real time as part of a single pull
  request. Every bracketed processing instruction in the seven body sections is
  replaced with grounded, publication grade prose, tables, and figures, targeting
  roughly 70 typeset pages, while `main.tex`, `new_paper.sty`, `references.bib`,
  `sections/references.tex`, and `sections/back_matter.tex` are carried over.
- The full paper renders the executed evidence: 51 of 51 tests across 8 modules,
  the 2.5x acceleration (30 to 12 days), the full VVUQ gate decision surface (1
  accept, 5 block, 1 escalate), triple run consensus, the lights off factory
  safety cases, and the 2030 PDAC pilot. It carries 18 tabularx tables sized to
  the body text width, 5 figures, and 29 `ieeetr` references.
- `papers/VVUQ-01/full-paper/Images/`: a guide naming the four author supplied
  figure files. Each figure environment renders a labeled placeholder slot until
  its image is present, so the project compiles in Overleaf either way.
- `papers/VVUQ-01/full-paper/full-paper.zip`: an Overleaf ready bundle of the
  LaTeX project.

### Changed
- `README.md`: release badge updated to v0.6.0, a new v0.6.0 summary added above
  the v0.5.0 summary, a VVUQ-01 full paper section and table of contents entry
  added, the repository structure now expands `papers/VVUQ-01/full-paper`, and
  the citation version was bumped.
- `releases.md`: v0.6.0 release notes added above the v0.5.0 notes.

### Notes
- This release adds the full paper only; it does not change the executable v0.1.0
  source modules or the v0.2.0 through v0.5.0 records, and it does not modify the
  draft scaffold. The additions are LaTeX, Markdown, and a zip, all outside the
  `ruff` and `yamllint` surface, so `lint-and-format` (ruff check, ruff format
  check, yamllint) stays green across Python 3.10, 3.11, and 3.12, alongside
  `validate-scripts` and `test` (51 passed, 0 skipped).
- All prose uses single dashes only; triple dashes are reserved for Markdown
  rules, table separators, and YAML document separators.

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
