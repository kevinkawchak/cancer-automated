# Releases

Release notes for the cancer-automated repository.

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
