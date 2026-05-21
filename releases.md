# Releases

Release notes for the cancer-automated repository.

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
