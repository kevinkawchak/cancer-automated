# VVUQ-01 Execution: Stage 1 Establishment and Stage 2 PDAC Reference

[![DOI](https://img.shields.io/badge/DOI-Zenodo%20pending-blue.svg)](../../../CITATION.cff)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](../../../LICENSE)
[![Release](https://img.shields.io/badge/Release-v0.2.0-brightgreen.svg)](../../../releases.md)
[![Executed](https://img.shields.io/badge/Executed-May%202026-blue.svg)](README.md)
[![Python](https://img.shields.io/badge/Python-3.11.15-blue.svg)](https://www.python.org/)
[![Runner](https://img.shields.io/badge/Runner-Claude%20Code%20Opus%204.7%201M-purple.svg)](https://claude.com/product/claude-code)
[![CI](https://img.shields.io/badge/lint--and--format-green-brightgreen.svg)](../../../.github/workflows/ci.yml)
[![Tests](https://img.shields.io/badge/pytest-51%20passed-brightgreen.svg)](01-foundation/test-suite.md)

This directory holds the complete execution record of the
`kevinkawchak/cancer-automated` v0.1.0 codebase and the Stage 2 2030 PDAC
procedure code. It was produced by Claude Code Opus 4.7 (1M context) running
autonomously in a managed cloud container. Every example script, the test
suite, the static-analysis checks, and the safety and gate decision surfaces
were executed, and their verbatim outputs are captured in the five numbered
sections. This README is the index and the technical summary that a future
paper can build on.

> Note on the DOI badge. The repository has no assigned archival DOI yet. The
> badge above is a labeled placeholder pointing at `CITATION.cff`. A Zenodo
> concept DOI is expected to be minted when a tagged release is archived. The
> input corpus for this paper references 117 distinct external DOIs, listed by
> the paper input chunks under `../inputs/`.

## Thesis

The LLM VVUQ process needs to be more substantial than the generated code
itself throughout codegen, imagegen, and papergen automation. This is
accomplished faster and less expensive than current verification methods. The
cancer-automated v0.1.0 codebase was executed here to establish Stage 1, and
the Stage 2 2030 60-second PDAC procedure code was also executed for use in a
future paper.

This execution is itself evidence for the thesis. The pipeline produced a
complete deliverable in well under a millisecond, while the VVUQ section shows
that turning that candidate into a shippable result requires clearing six
verification checks, a 0.95 agreement bar, a recorded human review, and a
dispersion bound across three runs. Five of six gate cases were blocked. The
assurance work, not the generation, is the substantial part, and an autonomous
agent performed all of it cheaply and reproducibly.

## What cancer-automated is

cancer-automated packages five established methods into one repeatable
daily-deliverable pipeline, then layers assurance and automation on top.

1. Instruction generation (`pipeline/instruction_stage.py`)
2. Code generation (`pipeline/codegen_stage.py`)
3. Code execution (`pipeline/execution_stage.py`)
4. Paper assembly (`pipeline/paper_stage.py`)
5. The VVUQ gate (`vvuq/vvuq_gate.py`), held to a higher standard than codegen

Around those five methods sit triple simulation, robust web and PDF ingestion,
200K autochunking with reconstruction READMEs, and a non-stop commit scheduler
(Stage 1), plus a lights-off factory controller and a hybrid surgery and
medicine pilot (Stage 2).

### Daily deliverable pipeline (as executed)

```
  Inputs                    Five Established Methods           Assured Output
  (web + PDF)           --> (per daily deliverable)        --> (committed)
  +-----------------+       +--------------------------+       +----------------+
  | Web search      |  -->  | 1. Instruction generation|  -->  | Deliverable    |
  | PDF processing  |       | 2. Code generation       |       | committed with |
  | Autochunk 200K  |       | 3. Code execution        |       | per-chunk      |
  | READMEs/chunk   |       | 4. Paper assembly        |       | READMEs at 200K|
  +-----------------+       +--------------------------+       +----------------+
          |                            |                               ^
          v                            v                               |
  +-----------------+       +--------------------------+       +----------------+
  | Non-stop commit |       | Triple simulation        |       | VVUQ gate      |
  | scheduler 24/day|  -->  | run each project 3 times,|  -->  | V and V and UQ,|
  | autonomous      |       | consensus across runs    |       | stricter than  |
  |                 |       |                          |       | code generation|
  +-----------------+       +--------------------------+       +----------------+
```

### Two-stage roadmap (as executed)

```
  Stage 1 (established here)                Stage 2 (reference, executed)
  +-----------------------------------+     +-----------------------------------+
  | - Non-stop commit schedules       |     | - Code runs physical AI in        |
  | - VVUQ more robust than codegen   | --> |   lights-off factories            |
  | - Auto-simulate projects 3 times  |     | - Hybrid surgery and medicine     |
  | - Robust web search and PDF       |     |   pilot, the 2030 PDAC 60-second  |
  | - Per-file size limits at 200K    |     |   robotic Whipple plus            |
  | - Autochunk code and docs w/      |     |   Daraxonrasib analog             |
  |   per-chunk READMEs               |     |                                   |
  +-----------------------------------+     +-----------------------------------+
       Sections 01 to 04                          Section 05
```

### VVUQ gate decision flow (as executed)

```
  candidate deliverable
        |
        v
   verify() ----------> validation() ----------> quantify() ----------> GateDecision
   6 checks             agreement vs ref          cv across 3 runs       |
   fraction == 1.0      >= 0.95, err <= 0.05       <= 0.10                |
   schema, lint         human review recorded      runs >= 3             |
        |                    |                          |                v
        +--------------------+--------------------------+-----> any failure -> BLOCK
                                                                cv > 0.10  -> ESCALATE
                                                                all pass   -> ACCEPT
```

## Execution flow of this run

```
  Section 01  Foundation        verify_installation, pytest (51), ruff, yamllint
      |
      v
  Section 02  Pipeline          3 examples, 5 deliverables, 4 artifacts each
      |
      v
  Section 03  VVUQ              3 examples + 6 gate cases (1 accept, 5 block)
      |
      v
  Section 04  Stage 1 automation 7 examples + chunk losslessness verification
      |
      v
  Section 05  Physical-AI Stage 2 2 examples + full safety surface, 2030 PDAC
      |
      v
  This README + repository updates (releases.md, CHANGELOG.md, top-level README)
```

## Execution results summary

| Section | Scope | Commands run | Result |
|---------|-------|--------------|--------|
| 01 Foundation | environment, tests, lint | verify script, pytest, ruff x2, yamllint | core ready, 51 passed, all clean |
| 02 Pipeline | five established methods | 3 example scripts | 5 deliverables, all 4 stages complete, factor 2.5 |
| 03 VVUQ | gate held higher than codegen | 3 examples + 6 gate cases | 1 accept, 5 block, 1 escalate, all as specified |
| 04 Stage 1 automation | sim, ingest, chunk, schedule | 7 example scripts + 2 checks | all green, 1 limitation found and documented |
| 05 Physical-AI Stage 2 | 2030 PDAC, lights-off | 2 examples + 4 safety cases | pilot built, all safety paths correct |

Aggregate: 15 example scripts executed (all exit 0), 51 automated tests passed,
3 static-analysis checks clean, 6 VVUQ gate cases and 4 factory safety cases
exercised, and 2 independent correctness verifications performed.

## File generation outcomes (basis for a future paper)

This execution generated 13 documentation and artifact files under
`papers/VVUQ-01/execution/`, plus the repository updates in the final commit.
Each is mapped below to the paper section it can support.

| Generated file | Bytes | Kind | Future paper role |
|----------------|-------|------|-------------------|
| 01-foundation/README.md | 1899 | index | Methods: environment gate |
| 01-foundation/environment-and-verification.md | 4994 | report | Methods: reproducibility, dependency posture |
| 01-foundation/test-suite.md | 7072 | report | Verification: automated test evidence |
| 01-foundation/lint-format-yaml.md | 3245 | report | Verification: static analysis evidence |
| 02-pipeline/README.md | 8559 | report | Methods and Results: the five methods |
| 02-pipeline/artifacts/instructions.md | 963 | artifact | Results: generated instruction set |
| 02-pipeline/artifacts/execution_log.txt | 95 | artifact | Results: captured execution output |
| 02-pipeline/artifacts/paper.md | 1000 | artifact | Results: auto-assembled paper draft |
| 03-vvuq/README.md | 8812 | report | Core Results: the VVUQ decision surface |
| 04-stage1-automation/README.md | 8646 | report | Results: Stage 1 automation, limitation |
| 04-stage1-automation/artifacts/chunk_reconstruction_README.md | 506 | artifact | Results: chunk reconstruction evidence |
| 05-physical-ai-stage2/README.md | 7538 | report | Results: Stage 2 PDAC and safety |
| 05-physical-ai-stage2/artifacts/pdac_hybrid_pilot_timeline.txt | 662 | artifact | Results: 2030 PDAC pilot timeline |

The three saved pipeline artifacts (instructions, execution log, paper) plus the
chunk reconstruction README and the PDAC timeline are the primary generated
deliverables. The five section reports are the structured evidence around them.
Together they constitute a Methods plus Results skeleton: the foundation report
documents reproducibility, the pipeline and Stage 1 reports document the
generation and automation, the VVUQ report documents the assurance, and the
Stage 2 report documents the deployment reference.

### Key quantitative results to cite

| Quantity | Value | Source section |
|----------|-------|----------------|
| Automated tests passed | 51 of 51 (0 skipped) | 01 |
| Acceleration factor | 2.5 (30 baseline days to 12 automated days) | 02 |
| VVUQ gate cases exercised | 6 (1 accept, 5 block, 1 escalate) | 03 |
| Verification fraction to ship | 1.0 required (a single fail blocks) | 03 |
| Max coefficient of variation (accept) | 0.0068 against a 0.10 bound | 03, 04 |
| Triple-run consensus | converged, 0 divergent metrics | 04 |
| Chunk losslessness | line and ASCII lossless; multibyte loses 6 chars | 04 |
| 2030 PDAC pilot | 60 s 8-arm Whipple, 6 cycles, 168 regimen days | 05 |
| Factory safety | estop on over-budget faults, block on interlock | 05 |

## The full process taken

This records every step, in order, so the run is reproducible and so nothing is
implied to have happened that did not.

1. Surveyed the repository: read the top-level README, CHANGELOG, releases,
   requirements, ruff configuration, CI workflow, both config files, and all
   source modules across pipeline, vvuq, simulation, ingestion, chunking,
   scheduler, and physical-ai, plus all 15 example scripts and the test harness.
2. Established the baseline on the container: confirmed Python 3.11.15, then
   installed the linting and test tooling (`ruff`, `yamllint`, `pytest`) and the
   declared core packages so the full check matrix could run. Confirmed `ruff
   check`, `ruff format --check`, and `yamllint` were clean and that the suite
   passed before adding anything.
3. Section 01 Foundation: ran `scripts/verify_installation.py`, the full
   `pytest tests/` suite, and the three static-analysis checks. Captured all
   outputs and committed.
4. Section 02 Pipeline: ran the three pipeline examples, then captured the four
   full generated artifacts and the per-stage logs through the orchestrator.
   Saved the non-Python artifacts as files and committed.
5. Section 03 VVUQ: ran the three vvuq examples, then exercised the gate across
   six cases covering the accept, block, and escalate paths. Committed.
6. Section 04 Stage 1 automation: ran the seven simulation, ingestion, chunking,
   and scheduler examples, then independently verified chunk reconstruction.
   This is where the multibyte hard-split limitation was discovered. Committed.
7. Section 05 Physical-AI Stage 2: ran the two physical-ai examples, then
   exercised the full lights-off safety surface and the 2030 PDAC pilot.
   Committed.
8. Wrote this comprehensive README (this commit).
9. Second-to-last commit: re-ran every CI check end to end and fixed any issue
   so the single pull request has no failing checks.
10. Last commit: repository updates (releases.md v0.2.0, CHANGELOG.md v0.2.0,
    and the top-level README structure and diagrams).

Each large section was a separate commit, pushed to GitHub in real time, so the
work is incremental and the agent's working context stayed focused on one
section at a time. All commits belong to one pull request on
`kevinkawchak/cancer-automated`. No other repository was touched.

## Limitations, approximations, and what could not be run

This section is deliberately complete. The thesis depends on honest VVUQ, so the
gaps are stated plainly.

- Agentic backends not exercised live. `anthropic` and `openai` are not
  installed and no API key was present, so the instruction and code generation
  stages ran on their deterministic offline templates, not a live model. This is
  the guarded path and is the correct CI behavior, but it means the live
  agentic authoring path was not executed here.
- Live web search not reachable. `requests` is installed, so the web search
  client attempted a real fetch, exhausted its four-attempt retry budget against
  the unreachable endpoint, and degraded to the labeled offline stub. The live
  search HTML parsing path was therefore not executed.
- PDF extraction backend absent. `pypdf` is not installed, so the PDF processor
  reported its clean non-fatal status and only the backend-independent chunk
  estimate ran. No real PDF text extraction was performed.
- Physics and robotics backends absent. `mujoco`, NVIDIA Isaac Sim, Isaac Lab,
  and ROS 2 are not present and the container has no GPU or display. The
  physical-ai modules are pure standard library references and ran fully, but
  any real physics-backed simulation path was not executed. These modules are
  disabled by default and are planning references only.
- Multibyte chunking edge case. The chunker is byte-identical lossless for
  line-boundary splits and for ASCII hard-splits (both tested and verified). A
  single oversized line of multibyte UTF-8 loses one character per internal
  boundary because of an `errors="ignore"` decode after a byte-level split. This
  was found during Section 04 and is documented there. It is reported, not
  repaired, because the task scope is to execute v0.1.0, not to modify the
  baseline. Repair plus a multibyte test is a recommended follow-up.
- LaTeX paper template not compiled. `papers/VVUQ-01/templates/Template_10/`
  contains `main.tex`, eight section files, `new_paper.sty`, and a five-entry
  `references.bib`. The structure was validated statically: all eight `\input`
  targets resolve to present files. It was not compiled to PDF because no TeX
  toolchain (`pdflatex`, `latexmk`, `xelatex`, `tectonic`) is available in the
  container, and the template is a future-paper scaffold rather than part of the
  executable v0.1.0 platform. The executed paper artifact is the Markdown paper
  produced by the pipeline paper stage.
- Imagegen has no executable code in v0.1.0. The thesis spans codegen, imagegen,
  and papergen. v0.1.0 implements codegen (`pipeline/codegen_stage.py`) and
  papergen (`pipeline/paper_stage.py`); the `papers/VVUQ-01/imagegen/` and
  `image-instruct/` directories are placeholders with no source to run. Imagegen
  automation is future work and could not be executed.
- Single Python version run locally. The container provides Python 3.11.15 only.
  Cross-version behavior on 3.10 and 3.12 is covered by the CI matrix rather
  than by a local multi-version run. No version-specific behavior is expected
  because the code is standard library with guarded imports.

## This execution versus conventional high-end server processing

The task asks how an autonomous Claude Code Opus 4.7 1M run on a managed cloud
container compares with running the same codebase on a conventional high-end
MacOS, Windows, or Linux workstation or server. Honest notes follow.

### Better

- Near-zero setup. The core engine is pure standard library with guarded
  optional imports, so it ran immediately. A conventional setup often begins
  with installing the full `requirements.txt` (anthropic, openai, mujoco, and
  more), which is slow and can fail on transitive or platform constraints. Here
  the guarded design meant the core ran before any heavy install.
- One integrated loop. Running code, observing output, writing documentation,
  re-running the lint checks, committing, and pushing all happened in a single
  agent loop with no context switch between a terminal, an editor, and a git
  client. This is faster and less expensive than a human cycling those tools,
  which is the cost half of the thesis.
- Systematic assurance beyond the shipped tests. The agent exercised the full
  gate decision surface and the full factory safety surface, and independently
  re-verified the chunk losslessness claim, which surfaced the multibyte
  limitation that the unit tests miss. Doing this breadth by hand is tedious;
  doing it automatically is cheap and repeatable.
- Self-verifying documentation. Every command and its verbatim output is in the
  record, so a reader can reproduce and check each claim rather than trust a
  summary.

### Different

- Ephemeral and commit-driven. The container is reclaimed after the session, so
  nothing persists unless committed and pushed. This enforced the
  commit-per-section discipline. A workstation keeps state across days, which is
  more forgiving but less reproducible.
- Real-time per-section commits. The agent pushed each section as it finished,
  which is a finer commit granularity than a human typically uses, and it makes
  the pull request a clean section-by-section narrative.
- Cross-version testing is delegated. Local runs use one Python; the CI matrix
  carries 3.10, 3.11, and 3.12. A conventional setup might use pyenv or conda to
  cover all three locally.

### Worse

- No live heavy backends. A conventional high-end server with GPUs and API keys
  could exercise the live agentic generation, the live web search and HTML
  parsing, real PDF extraction, and mujoco or Isaac physics. None of those live
  paths ran here; only the deterministic and guarded paths did.
- No display or GPU. GUI-driven or accelerated workloads (Isaac Sim, any
  visualization, LaTeX with graphics) are out of reach in this container. A
  workstation handles those directly.
- No persistent caches. Each session starts cold, so repeated heavy work cannot
  reuse a warm cache the way a long-lived server can.

Net: for executing, verifying, and documenting a standard-library codebase under
strict assurance, the autonomous cloud run was faster and cheaper and produced a
more reproducible record. For exercising live model, network, and physics
backends, a conventional provisioned server would do more.

## Repository structure (execution outputs)

```
papers/VVUQ-01/execution/
+-- README.md                         (this file: index and technical summary)
+-- 01-foundation/
|   +-- README.md
|   +-- environment-and-verification.md
|   +-- test-suite.md
|   +-- lint-format-yaml.md
+-- 02-pipeline/
|   +-- README.md
|   +-- artifacts/
|       +-- instructions.md
|       +-- execution_log.txt
|       +-- paper.md
+-- 03-vvuq/
|   +-- README.md
+-- 04-stage1-automation/
|   +-- README.md
|   +-- artifacts/
|       +-- chunk_reconstruction_README.md
+-- 05-physical-ai-stage2/
    +-- README.md
    +-- artifacts/
        +-- pdac_hybrid_pilot_timeline.txt
```

## Source executed (v0.1.0 platform)

| Package | Modules | Section |
|---------|---------|---------|
| pipeline/ | deliverable, instruction_stage, codegen_stage, execution_stage, paper_stage, orchestrator | 02 |
| vvuq/ | verification, validation, uncertainty, vvuq_gate | 03 |
| simulation/ | triple_runner, consensus | 04 |
| ingestion/ | web_search, pdf_processor | 04 |
| chunking/ | chunker, readme_generator | 04 |
| scheduler/ | commit_scheduler | 04 |
| physical-ai/ | lights_off_factory, hybrid_surgery_medicine | 05 |
| scripts/ | verify_installation | 01 |
| tests/ | 8 test modules, 51 tests | 01 |

## Reproduction

```bash
git clone https://github.com/kevinkawchak/cancer-automated.git
cd cancer-automated
pip install -r requirements.txt          # core runs without the optional heavy packages
python scripts/verify_installation.py
python -m pytest tests/ -v
ruff check . && ruff format --check . && yamllint -d relaxed configs/ .github/
# then run any example, for example:
python pipeline/examples-pipeline/01_single_deliverable.py
```

## Responsible use

Generated instructions, code, and papers are drafts. A VVUQ gate and a human
reviewer must clear any deliverable before clinical use. The Stage 2 references
(lights-off factory and the hybrid surgery and medicine pilot) are planning and
simulation references, disabled by default, and require VVUQ clearance, human
oversight, IRB approval, and regulatory authorization before any real use.

## Citation

See `CITATION.cff` at the repository root. If you use this execution record,
cite the cancer-automated repository at version 0.2.0.
