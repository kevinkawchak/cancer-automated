# Releases

Release notes for the cancer-automated repository.

---

VVUQ-01 Publication Figures Rendered (v0.4.0)
v0.4.0 - VVUQ-01 Publication Figures Rendered

## Summary

- Renders the 10 v0.3.0 image instructions into papers/VVUQ-01/imagegen: 10 self contained matplotlib scripts (the generated code) and the 10 portrait, full page, 300 dpi PNG figures they produce (the execution output), one numbered subdirectory per figure, plus a comprehensive README with an embedded gallery. Authored autonomously by Claude Code Opus 4.7 (1M context) Max in a managed cloud container, one figure per commit, with every commit pushed to GitHub in real time as part of a single pull request.
- Advances the image generation leg of the thesis that the LLM VVUQ process must be more substantial than the generated artifact across codegen, imagegen, and papergen. Because the full assurance specification for each figure was front loaded in v0.3.0, each figure builds deterministically from its instruction with no manual positioning. The directory keeps a clean split between the generated code (the NN-name.py script) and execution (running the script to render NN-name.png), the same split the pipeline draws between code generation and code execution.
- The 10 figures use professional and effective chart families and avoid basic bar, pie, and line charts: a VVUQ gate decision funnel, a schedule acceleration waterfall, a five established methods process flowchart, a VVUQ assurance radar wheel, a 2030 PDAC Gantt timeline, a test coverage treemap, a lights off factory safety state machine, an FDA cost efficiency financial bridge with measured credibility bullets, a value proposition matrix, and a file generation Sankey.
- Numbers are grounded and reconciled, matching the v0.2.0 execution record: the funnel narrows 6, 5, 3, 1 across the six gate cases; the waterfall evaluates the codegen model to 30, 20, 15, 12 days with reductions 10, 5, 3; the treemap tiles 51 of 51 tests across 8 modules; the wheel plots six normalized assurance spokes; the Gantt carries the 60 second 8 arm Whipple plus six 28 day cycles over 168 regimen days; the cost bridge cascades 100, 82, 66, 54, 40, 30 with measured credibility scores 81.9 and 85.75 against a target 80; and the Sankey byte flows sum to 54127 across the five sections and the four paper roles.
- Every figure inherits one shared page frame (portrait 8.5 by 11 inches, 300 dpi giving 2550 by 3300 pixels, white background only with no dark mode), one professional palette, fixed reserved header, content, and footer bands, the section symbol § where required, and single dashes only; long headers, subtitles, and footers auto shrink to stay inside the frame so the author needs no manual positioning.
- Each script is self contained, depends only on matplotlib and numpy, sets a non interactive Agg backend, and passes ruff check and ruff format check, so the lint-and-format CI workflow (ruff check, ruff format check, yamllint) stays green across Python 3.10, 3.11, and 3.12, alongside validate-scripts and the test job (51 passed, 0 skipped). matplotlib is the one added rendering dependency; the core CI does not install it and does not import imagegen.
- Updates the repository documentation: the main README release badge, a new v0.4.0 summary above the previous summary, the figures section text diagram and closing links, the repository structure now expanding papers/VVUQ-01/imagegen, the citation version, the CHANGELOG (v0.4.0), and these release notes; the comprehensive imagegen README is added.
- All prose uses single dashes only. No em dashes, no double dashes, and no triple dashes outside of Markdown rules, Markdown table separators, and YAML document separators.

## Features

- papers/VVUQ-01/imagegen/README.md: the rendered gallery and build record, including the generated code versus execution split table, the 10 figure index, the embedded figure gallery with grounding, the shared output conventions, the reproduction steps with matplotlib, and the as built acceptance summary.
- 01-vvuq-gate-funnel: a funnel narrowing six candidate deliverables to one accepted with verbatim block and escalate reasons, grounded in vvuq/vvuq_gate.py and configs/vvuq_thresholds.yaml (v0.1.0) and execution §03 (v0.2.0).
- 02-acceleration-waterfall: a schedule waterfall bridging 30 baseline days to 12 automated days with an audit panel reproducing the codegen formula, grounded in pipeline/codegen_stage.py and configs/pipeline_config.yaml (v0.1.0) and execution §02 (v0.2.0).
- 03-five-methods-flowchart: a process flowchart with an orchestrator swimlane and a VVUQ gate diamond carrying module names, byte counts, and stage durations, grounded in pipeline/ (v0.1.0) and execution §02 DAILY-0001 (v0.2.0).
- 04-vvuq-assurance-wheel: a radar wheel of six normalized assurance spokes with the threshold ring, the accepted polygon, and per spoke failing markers, grounded in configs/vvuq_thresholds.yaml and vvuq/ (v0.1.0) and execution §03 (v0.2.0).
- 05-pdac-pilot-timeline: a Gantt timeline of the 2030 PDAC hybrid pilot, grounded in physical-ai/hybrid_surgery_medicine.py (v0.1.0) and the execution §05 timeline artifact (v0.2.0).
- 06-test-coverage-treemap: a treemap of 51 of 51 passing tests across 8 modules with a sequential teal to navy scale, grounded in execution §01 test-suite.md (v0.2.0).
- 07-lights-off-state-machine: a safety gating state diagram with four interlocks, four states, and four cases, grounded in physical-ai/lights_off_factory.py (v0.1.0) and execution §05 (v0.2.0).
- 08-fda-cost-efficiency-bridge: an illustrative cost bridge with measured credibility bullets referencing FDA §VI.B and ASME V&V 40, grounded in the execution comparison and the pipeline and vvuq levers (v0.1.0 and v0.2.0) and the inputs corpus.
- 09-value-proposition-matrix: a 2 by 2 positioning matrix and a better, different, worse summary with a net verdict banner, grounded in the execution README comparison (v0.2.0).
- 10-file-generation-sankey: a top to bottom Sankey flowing 13 generated files and 54127 bytes into four future paper roles, grounded in the execution README file generation outcomes (v0.2.0) and the pipeline artifacts (v0.1.0).
- README.md, CHANGELOG.md, and releases.md updated for v0.4.0: the release badge, a new figures summary, the figures section text diagram and links, the repository structure now expanding papers/VVUQ-01/imagegen, the citation version, and a v0.4.0 release line.

## Contributors
@kevinkawchak
@claude

## Notes

This release renders the figures specified in v0.3.0; it does not change the executable v0.1.0 source modules or the v0.2.0 and v0.3.0 records. Each script depends only on matplotlib and numpy and renders headless through the Agg backend. Rendering the PNG files requires matplotlib in the rendering environment (pip install matplotlib, which pulls in numpy, already a core dependency); the core CI does not install matplotlib and the test job does not import imagegen, so lint-and-format (ruff check, ruff format check, yamllint) and test stay green across Python 3.10, 3.11, and 3.12 because the scripts are ruff clean. The figures are planning and documentation drafts: a VVUQ gate and a human reviewer must clear any deliverable before clinical use, and the Stage 2 references (the lights off factory and the hybrid surgery and medicine pilot) require VVUQ clearance, human oversight, IRB approval, and regulatory authorization before any real use.

---

VVUQ-01 Image Instructions for Publication Figures (v0.3.0)
v0.3.0 - VVUQ-01 Image Instructions for Publication Figures

## Summary

- Adds papers/VVUQ-01/image-instruct, a set of 10 comprehensive image instructions plus a master README, authored autonomously by Claude Code Opus 4.7 (1M context) Max in a managed cloud container, with each instruction committed and pushed to GitHub in real time as part of a single pull request. Each instruction is a complete, self contained specification for one publication ready, portrait, full page, 300 dpi figure, grounded in code generation (v0.1.0) and code execution (v0.2.0).
- Advances the image generation leg of the thesis that the LLM VVUQ process must be more substantial than the generated artifact across codegen, imagegen, and papergen. The full assurance specification for each figure is written ahead of time, before any pixel is rendered, which is the image generation analog of the VVUQ gate. No images are generated in this release; the instructions specify exactly how Claude Code Opus 4.7 (1M) Max writes the matplotlib scripts and renders the PNG files at a future date under papers/VVUQ-01/imagegen.
- The 10 figures use professional and effective chart families and avoid basic bar, pie, and line charts: a VVUQ gate decision funnel, a schedule acceleration waterfall, a five established methods process flowchart, a VVUQ assurance radar wheel, a 2030 PDAC Gantt timeline, a test coverage treemap, a lights off factory safety state machine, an FDA cost efficiency financial bridge with measured credibility bullets, a value proposition matrix, and a file generation Sankey.
- Every figure inherits one shared page frame (portrait 8.5 by 11 inches, 300 dpi, white background only with no dark mode), one professional palette, fixed reserved header, content, and footer bands, the section symbol § where required, and single dashes only, so the set is coherent and a renderer needs no manual positioning.
- Numbers are grounded and reconciled: the Sankey byte flows sum to 54127 across both the five section nodes and the four paper roles, the treemap tiles 51 of 51 tests across 8 modules, the waterfall evaluates the codegen model to 30, 20, 15, 12 days, the funnel narrows 6, 5, 3, 1 across the six gate cases, and the PDAC timeline carries the 60 second 8 arm Whipple plus six 28 day cycles over 168 regimen days.
- Updates the repository documentation: the main README badges, repository structure, a new figures section with a text diagram and a table of contents entry, the citation version, the CHANGELOG (v0.3.0), and these release notes.
- All prose uses single dashes only. No em dashes, no double dashes, and no triple dashes outside of Markdown rules, Markdown table separators, and YAML document separators.

## Features

- papers/VVUQ-01/image-instruct/README.md: the master specification, including the exact processing model for Claude Code Opus 4.7 (1M) Max, the directory and file naming convention mapping each instruction to papers/VVUQ-01/imagegen/NN-name/NN-name.py and .png, the shared portrait page frame, the professional palette and typography, the symbol and dash rules, the 10 instruction index, the grounding sources, the future imagegen workflow and matplotlib dependency note, the cross instruction consistency results, and the global acceptance criteria.
- 01-vvuq-gate-funnel: a funnel narrowing six candidate deliverables to one accepted across verification, validation, and uncertainty, grounded in vvuq/ (v0.1.0) and execution §03 (v0.2.0).
- 02-acceleration-waterfall: a schedule waterfall bridging 30 baseline days to 12 automated days by per run reductions, grounded in pipeline/codegen_stage.py (v0.1.0) and execution §02 (v0.2.0).
- 03-five-methods-flowchart: a process flowchart with an orchestrator swimlane and a VVUQ gate node, grounded in pipeline/ (v0.1.0) and execution §02 (v0.2.0).
- 04-vvuq-assurance-wheel: a radar wheel of six normalized assurance spokes with the threshold ring, the accepted polygon, and per spoke failing markers, grounded in configs/vvuq_thresholds.yaml and vvuq/ (v0.1.0) and execution §03 (v0.2.0).
- 05-pdac-pilot-timeline: a Gantt timeline of the 2030 PDAC hybrid pilot, grounded in physical-ai/hybrid_surgery_medicine.py (v0.1.0) and execution §05 (v0.2.0).
- 06-test-coverage-treemap: a treemap of 51 of 51 passing tests across 8 modules, grounded in execution §01 (v0.2.0).
- 07-lights-off-state-machine: a safety gating state diagram with four interlocks and four cases, grounded in physical-ai/lights_off_factory.py (v0.1.0) and execution §05 (v0.2.0).
- 08-fda-cost-efficiency-bridge: a financial bridge with measured credibility bullets referencing FDA §VI.B and ASME V&V 40, grounded in the execution comparison and the pipeline and vvuq levers (v0.1.0 and v0.2.0) and the inputs corpus.
- 09-value-proposition-matrix: a 2 by 2 positioning matrix and a better, different, worse summary, grounded in the execution README comparison (v0.2.0).
- 10-file-generation-sankey: a top to bottom Sankey flowing 13 generated files and 54127 bytes into four future paper roles, grounded in the execution README file generation outcomes (v0.2.0) and the pipeline artifacts (v0.1.0).
- README.md, CHANGELOG.md, and releases.md updated for v0.3.0: the release and updated badges, the repository structure now showing papers/VVUQ-01/image-instruct and papers/VVUQ-01/imagegen, a new figures section with a text diagram and a table of contents entry, the citation version, and a v0.3.0 release line.

## Contributors
@kevinkawchak
@claude

## Notes

This release adds instructions only. No matplotlib script and no PNG file is generated yet; those are produced at a future date under papers/VVUQ-01/imagegen by following the per instruction steps, which require matplotlib to be installed in the rendering environment. The lint-and-format CI workflow (ruff check, ruff format check, yamllint) stays green across Python 3.10, 3.11, and 3.12 because the additions are Markdown and fall outside the ruff and yamllint surface, alongside validate-scripts and the test job (51 passed, 0 skipped). Prior code generation (v0.1.0) and code execution (v0.2.0) files are unchanged. The figures are planning and documentation drafts: a VVUQ gate and a human reviewer must clear any deliverable before clinical use, and the Stage 2 references (the lights off factory and the hybrid surgery and medicine pilot) require VVUQ clearance, human oversight, IRB approval, and regulatory authorization before any real use.

---

VVUQ-01 Execution and Stage 2 PDAC Reference (v0.2.0)
v0.2.0 - VVUQ-01 Execution and Stage 2 PDAC Reference

## Summary

- Executes the entire cancer-automated v0.1.0 codebase and the Stage 2 2030 60-second PDAC procedure code, and records the full run under papers/VVUQ-01/execution. The run was performed autonomously by Claude Code Opus 4.7 (1M context) in a managed cloud container on Python 3.11.15 and Linux, with each large section committed and pushed in real time as part of a single pull request.
- Advances the thesis that the LLM VVUQ process must be more substantial than the generated code itself across codegen, imagegen, and papergen automation, accomplished faster and less expensively than current verification methods. The pipeline produces a complete candidate deliverable in well under a millisecond, while the VVUQ gate blocks five of six candidate cases, which shows that the assurance work, not the generation, is the substantial part.
- Establishes Stage 1 by executing all 15 example scripts to exit 0, passing the full test suite (51 passed, 0 skipped), and confirming the CI lint-and-format surface is clean (ruff check, ruff format check, yamllint), alongside validate-scripts (py_compile) and the test job.
- Executes the Stage 2 references for a future paper: the lights-off factory controller across its full safety surface (clean run returns to dark, over-budget faults trigger emergency stop, an unsatisfied interlock blocks the run), and the 2030 PDAC analog hybrid pilot (a 60-second 8-arm robotic Whipple on day 0 plus six 28-day Daraxonrasib adjuvant cycles, 168 regimen days over 7 timeline events).
- Documents one discovered limitation: the chunker is byte-identical lossless for line-boundary and ASCII hard-split paths (both tested and re-verified), but the untested multibyte hard-split path loses one character per internal boundary because of an errors-ignore decode. It is reported, not repaired, since the scope is to execute v0.1.0, not to modify the baseline.
- Adds a comprehensive execution README with relevant badges, ASCII diagrams, a file-generation-outcomes summary mapped to future paper sections, the full process narrative, an explicit limitations section, and notes comparing the autonomous cloud run with conventional high-end server processing.
- All prose uses single dashes only. No em dashes, no double dashes, and no triple dashes outside of Markdown rules, Markdown table separators, and YAML document separators.

## Features

- papers/VVUQ-01/execution/README.md: the index and technical summary of the run, including DOI and status badges, the pipeline and two-stage and VVUQ-gate and execution-flow ASCII diagrams, the results summary across all five sections, the generated-file inventory, the limitations, and the conventional-versus-cloud comparison.
- papers/VVUQ-01/execution/01-foundation: environment and dependency posture, the verify_installation.py output, the full pytest run (51 passed across 8 modules), and the ruff and yamllint static-analysis evidence.
- papers/VVUQ-01/execution/02-pipeline: the three pipeline examples run end to end, the four full generated artifacts (instructions, generated code, execution log, paper) with the non-Python artifacts saved as files, plus per-stage logs and timing.
- papers/VVUQ-01/execution/03-vvuq: the three vvuq examples plus the full gate decision surface across six cases (one accept and five distinct block reasons, one of which escalates), demonstrating the gate is held higher than code generation.
- papers/VVUQ-01/execution/04-stage1-automation: the seven simulation, ingestion, chunking, and scheduler examples, an independent chunk-losslessness verification, and the documented multibyte limitation, with the generated reconstruction README saved as an artifact.
- papers/VVUQ-01/execution/05-physical-ai-stage2: the two physical-ai examples, the full lights-off safety surface, and the 2030 PDAC pilot timeline saved as an artifact.
- README.md, CHANGELOG.md, and releases.md updated for v0.2.0: the release and contributors badges, the repository structure now showing papers/VVUQ-01/execution, and a v0.2.0 release line.

## Contributors
@kevinkawchak
@claude
@openai
@google-gemini

## Notes

The v0.2.0 release is an execution and documentation record built on the v0.1.0 platform; it does not change the executable v0.1.0 source modules. Generated instructions, code, and papers remain drafts: a VVUQ gate and a human reviewer must clear any deliverable before clinical use. The Stage 2 references (lights-off factory and the hybrid surgery and medicine pilot) are planning and simulation references, disabled by default in configs/pipeline_config.yaml, and require VVUQ clearance, human oversight, IRB approval, and regulatory authorization before any real use. Limitations of this run are stated in full in the execution README: the agentic, live web search, PDF, and physics backends were absent or unreachable so only the deterministic and guarded paths ran; the LaTeX paper template was validated structurally but not compiled because no TeX toolchain was available; imagegen has no executable code in v0.1.0; and cross-version behavior on Python 3.10 and 3.12 is covered by the CI matrix rather than a local multi-version run.

---

Initial Automation Platform (v0.1.0)
v0.1.0 - Initial Automation Platform

## Summary

- First release of cancer-automated, a production-ready, scalable platform that automates Physical AI oncology trial daily deliverables. The repository is modeled after physical-ai-oncology-trials and incorporates methods proven across robotic-surgeries and Clinical-AI-Demos so that several projects demonstrate the same established methods.
- Realizes the thesis: production-ready, scalable, and automated Physical AI oncology trial daily deliverables are obtained based on established methods for generating instructions, code, code execution, and creating papers, and are further automated, accelerated, and the VVUQ is improved.
- Packages the four producing methods into one daily-deliverable pipeline (instruction generation, code generation, code execution, paper assembly) wired together by an orchestrator that invokes an optional VVUQ gate. The core engine is pure standard library and runs offline and deterministically; agentic backends are imported through try/except guards.
- Adds a VVUQ framework held to a higher standard than code generation. The gate combines verification, validation, and uncertainty quantification against the thresholds in configs/vvuq_thresholds.yaml, blocks on any failure, and escalates divergent uncertainty to a human.
- Delivers the Stage 1 automation capabilities: triple simulation with consensus, robust web search with bounded exponential-backoff retries, guarded PDF processing, 200K per-file autochunking with a reconstruction README per chunk, and a non-stop commit scheduler.
- Delivers the Stage 2 deployment references: a safety-gated lights-off factory runner and a hybrid surgery and medicine pilot timeline analogous to the 2030 PDAC 60-second robotic Whipple plus Daraxonrasib simulation. Both are disabled by default and require VVUQ clearance and human oversight.
- The lint-and-format CI workflow (ruff check, ruff format check, yamllint) on Python 3.10, 3.11, and 3.12 is green, alongside validate-scripts and a test job. The full test suite passes (49 passed, 2 environment-skipped).
- All prose uses single dashes only. No em dashes, no double dashes, and no triple dashes outside of Markdown rules, Markdown table separators, and YAML document separators.

## Features

- Repository foundation: ruff.toml, requirements.txt, .gitignore, CITATION.cff, and the community-health files (CONTRIBUTING.md, CODE_OF_CONDUCT.md, SECURITY.md, SUPPORT.md). CI at .github/workflows/ci.yml with lint-and-format across Python 3.10, 3.11, and 3.12 plus validate-scripts and test jobs. Pull request and issue templates under .github/.
- pipeline/: the deliverable data model (deliverable.py) plus instruction_stage.py, codegen_stage.py, execution_stage.py, paper_stage.py, and orchestrator.py, with runnable examples and tests covering the end-to-end flow, the blocked path, and gate invocation.
- vvuq/: verification.py, validation.py, uncertainty.py, and vvuq_gate.py, with examples and tests for the accept, block, and escalate paths.
- simulation/: triple_runner.py runs each project three times with distinct seeds and consensus.py aggregates the runs and flags divergence.
- ingestion/: web_search.py with bounded exponential-backoff retries and an offline fallback, and pdf_processor.py with a guarded backend and a 200K chunk estimate.
- chunking/: chunker.py autochunks under the 200K per-file cap and readme_generator.py emits a reconstruction README per chunk set.
- scheduler/: commit_scheduler.py plans an evenly spaced, non-stop commit cadence.
- physical-ai/: lights_off_factory.py is a safety-gated autonomous batch runner and hybrid_surgery_medicine.py builds the combined surgery and medicine pilot timeline.
- configs/: pipeline_config.yaml (stage and automation defaults including the 200K cap and three simulation runs) and vvuq_thresholds.yaml (gate thresholds).
- scripts/verify_installation.py reports core and optional dependency availability and validates the config files.
- README.md with badges, a table of contents, ASCII pipeline and two-stage roadmap diagrams, the full repository structure, an established-methods table referencing the four foundational developments, and core-capability tables.
- CHANGELOG.md records the v0.1.0 release in Keep a Changelog format.

## Contributors
@kevinkawchak
@claude

## Notes

The v0.1.0 release is the foundation of the automated daily-deliverable platform. Generated instructions, code, and papers are drafts: a VVUQ gate and a human reviewer must clear any deliverable before clinical use. The Stage 2 deployment references (lights-off factory and hybrid surgery and medicine pilot) are planning and simulation references, disabled by default in configs/pipeline_config.yaml, and require VVUQ clearance, human oversight, IRB approval, and regulatory authorization before any real use. The established methods packaged here were proven across the National Platform paper, the four-simulation accelerated patient prediction paper, the 2030 PDAC 60-second surgery plus medicine paper, and the humanoid multi-stage demo workflow.
