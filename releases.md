# Releases

Release notes for the cancer-automated repository.

---

VVUQ-02 Execution of the Humanoid VVUQ Codegen (v0.8.0)
v0.8.0 - VVUQ-02 Execution of the Humanoid VVUQ Codegen

## Summary

- Adds papers/VVUQ-02/execution, the complete run record of the papers/VVUQ-02/codegen tree, produced by Claude Code Opus 4.7 (1M context) Max running autonomously in a managed cloud container across 8 commits in a single pull request, one large section per commit pushed to GitHub in real time so the agent working memory stays focused on one section at a time.
- Advances the thesis that the robotic code assurance process, not code generation, is the substantial and decision-bearing part of the AI workflow: the control behaviors are generated and compiled deterministically in microseconds, while clearing one for ship requires a 1.0 verification fraction, a validation agreement bar up to 1.00, a relative-error bound as tight as 0.01, a coefficient-of-variation bound as tight as 0.05, a recorded human review, and a hard predicate on each of the three immediate-catastrophe gates. The 10-gate assurance suite carries 64 of the 172 unit tests, more than a third of the budget.
- Emphasizes that the external standards add credibility to the study: every gate, behavior, and safety surface is traced to a published consensus standard already used in real life (ASME V&V 40-2018, NASA-STD-7009A, FDA CM&S 2023, IEC 80601-2-77, IEC 60601-1, ISO 13482, ISO/TS 15066, ISO 10218-1, ISO 9283, IEC 62304, ISO 14971, ISO 13849-1, UL 4600, IEEE 7009), resolved at runtime from the wired standards corpus, so the argument is defensible to a regulator rather than ad hoc.
- Establishes the foundation: CPython 3.11.15 on Linux, a byte-for-byte determinism check that reproduces the committed sensor CSV, the 4-entrant comparison, and the 32-iteration sweep index from seed 20260525, the 172-test suite passing with 0 skipped, and the CI lint-and-format trio (ruff check, ruff format check on 110 files, yamllint) clean.
- Runs the 10-gate decision surface end to end over five cases: the nominal sweep where all 10 gates ACCEPT over their independent references (the only path that reports a composite), and four adversarial cases covering three distinct BLOCK mechanisms (a catastrophe-gate hard predicate, a verification fraction of 0.80, and a validation agreement collapse) plus one ESCALATE at coefficient of variation 0.163 that defaults to hand-back-to-human.
- Features and processes the two substantial generated files: the 1790-line, four-entrant comparison.json (32 iterations times 4 rounds is 128 round verdicts, with a leaderboard and a verified 100 percent caveat coverage on all robot-involving rounds), and the 1000-row, 27-column positional sensor stream (7 arm-joint angles, 5 fingertip forces, 3 end-effector positions, and 12 state channels across 500 ticks for each of two hands, with every row and every positional payload distinct and no repetition).
- Records the deployment reference: the 60-second 8-phase Whipple timeline and the three immediate-catastrophe safety surfaces (vascular no-fly hand, shared-OR human collision FSM, fault e-stop and graceful degradation), each producing the correct boundary behavior.
- Includes prompt-execution.md (the generating prompt verbatim) and output-execution.md (the narrative markdown output of the run), plus an honest limitations section and a this-run-versus-conventional-server section for future executions on leading MacOS, Windows, and Linux platforms.
- Updates the main README (release badge, a v0.8.0 summary above the prior summary, a VVUQ-02 Execution section with an ASCII flow diagram and a table of contents entry, the repository structure tree, the corrected codegen test count, and the citation version), this releases file, the CHANGELOG (v0.8.0), and CITATION.cff.
- All prose uses single dashes only. No em dashes, no double dashes, and no triple dashes outside of Markdown rules, Markdown table separators, and YAML document separators. The section symbol § is used where relevant. The paper template files in papers/VVUQ-02/templates/Template_04 were not processed.

## Features

- papers/VVUQ-02/execution/README.md: the index and technical summary with DOI and status badges, the 10-gate and execution-flow ASCII diagrams, an execution-results summary, a file-generation-outcomes table mapping all 19 artifacts to future paper sections, key quantitative results, the full process taken, limitations, the this-run-versus-conventional comparison, the execution repository tree, and the external-standards credibility basis.
- papers/VVUQ-02/execution/01-foundation: environment-and-verification.md (host, dependency posture, determinism check), test-suite.md (172 tests across 15 modules), and lint-format-yaml.md (the CI lint-and-format checks).
- papers/VVUQ-02/execution/02-pipeline: the intent to compile to act to score record across six behavior groups, with the verbatim pipeline_execution_log.txt artifact.
- papers/VVUQ-02/execution/03-vvuq: the 10-gate decision surface with the gate_decision_surface.txt captures, the nominal vvuq_report.md, and vvuq_decisions.json carrying each gate's resolved external standards.
- papers/VVUQ-02/execution/04-automation: the 32-iteration sweep index, the gated composite_scores.jsonl, the comparison_leaderboard.md, and comparison_analysis.txt processing the 1790-line tournament.
- papers/VVUQ-02/execution/05-humanoid-deployment: the deployment_safety_log.txt for the three catastrophe gates, sensor_stream_analysis.txt processing the 1000-row stream, and the eight_phase_timeline.txt diagram.
- papers/VVUQ-02/execution/prompt-execution.md and output-execution.md: the generating prompt verbatim and the narrative output of the execution step.

## Contributors
@kevinkawchak
@claude

## Notes

This release adds the VVUQ-02 execution record and edits only kevinkawchak/cancer-automated; no other repository is touched. All code was run from a scratch working directory with the codegen tree on PYTHONPATH, so the committed codegen tree was left pristine and a determinism check confirms the generators reproduce their committed artifacts exactly. No Python or notebook files were added outside the already-clean codegen tree, so the CI lint-and-format surface stays green across Python 3.10, 3.11, and 3.12, alongside validate-scripts and test. The on-prem LLM backends, live Zenodo deposition, and any physics or robotics backend were not exercised live; the modules ran on their guarded deterministic offline paths, which is the correct CI behavior, and the committed sensor sample is the first 50 ms of the timeline by design while the full 60-second stream is the Zenodo L0. The H2-Surgical 1.0 is a clearly labeled hypothetical 2030 platform and every number is a simulation result; the 10 VVUQ gates plus a recorded human reviewer must clear any candidate before any non-simulated use, and deployment would require IEC 80601-2-77, IEC 60601, ISO 13482, FDA SaMD Class III clearance, IRB approval, and regulatory authorization.

---

10 Unitree H2 Humanoid Surgical VVUQs (v0.7.0)
v0.7.0 - 10 Mobile Pancreatic Cancer Surgical Unitree H2 Humanoid VVUQs

## Summary

- Adds papers/VVUQ-02/codegen, the standalone generated codebase for 10 humanoid-specific VVUQ gates on an autonomous Unitree H2-Surgical 1.0 (a clearly labeled hypothetical 2030 surgical variant) performing the 60-second 8-phase Whipple on patient PAT-PDAC-0001 with its own two dexterous hands and no teleoperation, authored by Claude Code Opus 4.7 (1M context) Max from papers/VVUQ-02/instructions/output-instruct.md across 11 commits in a single pull request, one set of files per commit pushed to GitHub in real time.
- Advances the code generation leg of the thesis that the robotic code assurance process, not code generation, is the substantial and decision-bearing part of the AI workflow: because one humanoid concentrates all error potential into one body, the VVUQ assurance layer is more substantial, stricter, and more thoroughly exercised than the control code, and a candidate behavior must clear 10 distinct gates before it ships.
- Builds the assurance layer against external standards already used in real life so the credibility argument is defensible to a regulator: ASME V&V 40-2018 and NASA-STD-7009A for model credibility with the FDA 2023 computational modeling guidance, IEC 80601-2-77 and IEC 60601-1 for robotic surgery, ISO 13482 and ISO/TS 15066 and ISO 10218-1 and ISO 9283 for service and collaborative robot safety, IEC 62304 and ISO 14971 and ISO 13849-1 for software and risk, and UL 4600 and IEEE 7009 for autonomy and fail-safe design.
- Each gate verifies with a pass fraction of 1.0, validates observed metrics against an independent reference in data/reference, and quantifies uncertainty across seeded runs by the coefficient of variation, deciding ACCEPT, BLOCK, or ESCALATE; the three immediate-catastrophe gates (vascular no-fly, human collision, fault and e-stop) carry the tightest bounds and an extra hard predicate.
- Wires the real standards input corpus at papers/VVUQ-02/inputs/standards into the gate registry so each gate resolves to a published designation, and supplies clinical baselines (the 2025 Dutch cohort, the Callery Fistula Risk Score).
- Runs a deterministic 32-iteration Latin hypercube sweep with seed 20260525 over five free parameters; all 32 iterations clear all 10 gates, and the 6-component composite (mean 93.56) is reported only because every gate ACCEPTs, so the assurance layer gates the headline number.
- Keeps the tree standalone and lint-clean: it runs on the Python standard library with guarded optional backends, and ruff check, ruff format check, and yamllint stay clean across Python 3.10, 3.11, and 3.12; the suite is 169 passing including a 64-item 10-gate decision surface.
- Updates the main README (release badge, a v0.7.0 summary above the prior summary, a VVUQ-02 section with an ASCII gate diagram and table of contents entry, the repository structure, and the citation version), this releases file, the CHANGELOG (v0.7.0), and CITATION.cff.
- All prose uses single dashes only. No em dashes, no double dashes, and no triple dashes outside of Markdown rules, Markdown table separators, and YAML document separators. The section symbol § is used where relevant.

## Features

- papers/VVUQ-02/codegen/src/vvuq: the 10-gate harness (verification, validation, uncertainty, the gate decision, and the registry that binds every gate to its predicates, independent reference, threshold block, and governing standards).
- papers/VVUQ-02/codegen/config: project.yaml (frozen scope, patient, seed, 8-phase timeline, 71-DOF platform), vvuq_thresholds.yaml (the 10 gate blocks), standards_map.yaml, kinematics, hand, balance, perception, autonomy, safety zones, shared OR actors, and anastomosis targets.
- papers/VVUQ-02/codegen/src: kinematics, sensors, perception, autonomy (the on-prem LLM intent path plus the deterministic plan compiler), hands (finger force, grasp, handover), balance (ZMP and posture), safety (vessel gate, human collision FSM, unified e-stop), suturing (ring tension and bimanual suturing), simulation (the 32-iteration sweep plus a Rust runner), metrics (the gated composite), llm (the 4-entrant tournament), and zenodo (the L0 pointer patcher).
- papers/VVUQ-02/codegen/schemas: JSON Schema plus Protobuf plus Avro for the humanoid sensor record and command, plus vvuq_case, vvuq_decision, and metrics schemas.
- papers/VVUQ-02/codegen/data/reference: the independent validation truth per gate, plus the labeled scene masks for the Dice ground truth.
- papers/VVUQ-02/codegen/docs: methodology (ASME V&V 40), the per-gate specification, the platform and hand specifications, the sensor and perception specifications, the autonomy policy, the shared OR safety protocol, the suturing and anastomosis protocol, the CI checklist, the runtime recipes, and the file-size pyramid.
- papers/VVUQ-02/codegen/prompt-codegen.md and output-codegen.md: the generating prompt verbatim and the narrative output of the generation step; papers/VVUQ-02/inputs records the prior instruction prompt and the Claude Code Opus 4.7 1M Max output that led to this codegen.
- papers/VVUQ-02 placeholders: image-instruct, imagegen, execution, draft-paper, full-paper, and final-paper each carry a README placeholder for the future pull requests.

## Contributors
@kevinkawchak
@claude

## Notes

This release adds the VVUQ-02 humanoid codegen and edits only kevinkawchak/cancer-automated; no other repository is touched. The Unitree H2-Surgical 1.0 is a clearly labeled hypothetical 2030 surgical variant: the base form factor traces to the real H2 bipedal humanoid lineage, but every clinical-grade capability uplift is paper-only, and every comparison against the 8-arm PancreSpeed 1.0 baseline or human surgeons is simulation-against-simulation. The codegen is a draft: the 10 VVUQ gates plus a recorded human reviewer must clear any candidate before any non-simulated use, and deployment would require IEC 80601-2-77, IEC 60601, ISO 13482, FDA SaMD Class III clearance, IRB approval, and regulatory authorization. The autonomy path is gated by VVUQ 04 and VVUQ 10 and defaults to hand-back-to-human on any ESCALATE. The lint-and-format surface (ruff check, ruff format check, yamllint) stays green across Python 3.10, 3.11, and 3.12, alongside validate-scripts and test.

---

VVUQ-01 Full Paper from the Draft Scaffold (v0.6.0)
v0.6.0 - VVUQ-01 Full Paper from the Draft Scaffold

## Summary

- Adds papers/VVUQ-01/full-paper, the full manuscript Two Stage VVUQ Oncology Clinical Trial Verification Automation Priority over Existing Generated Code, built from the v0.5.0 draft scaffold without modifying it, authored autonomously by Claude Code Opus 4.7 (1M context) Max in a managed cloud container, one commit per file and per section, each pushed to GitHub in real time as part of a single pull request.
- Replaces every bracketed processing instruction in the seven body sections with grounded, publication grade prose, tables, and figures, targeting roughly 70 typeset pages, and keeps the title page, style file, bibliography, references block, and back matter intact.
- Advances the paper generation leg of the thesis that the LLM VVUQ process must be more substantial than the generated artifact across codegen, imagegen, and papergen, accomplished faster and less expensively than conventional verification, toward faster, cheaper, and more rigorous physical AI oncology trials.
- Renders the executed evidence: the verification floor (51 of 51 tests across 8 modules), the 2.5x schedule acceleration (30 baseline to 12 automated days), the full VVUQ gate decision surface (1 accept, 5 block, 1 escalate), triple run consensus, the lights off factory safety cases, and the 2030 PDAC pilot (60 second 8 arm robotic Whipple plus six 28 day cycles, 168 regimen days).
- Eighteen tabularx tables sized to the body text width with raggedright paragraph columns, five figures, and twenty nine ieeetr references; the four images use placeholder slots that the author replaces later, so the project compiles either way.
- The bibliography is final: every DOI entry carries its human readable DOI string and a clickable resolver URL in the note; repository entries carry both a GitHub and a Zenodo URL, each once, with no duplicate link and no howpublished field.
- Formatting follows the senior author contract: ragged right body for even inter-word spacing with no rivers, strong widow and orphan control, raggedright paragraph table columns, single dashes only, the section symbol §, and black links with a green ORCID mark.
- A full-paper.zip bundle is provided for one step Overleaf upload; the project compiles as is and the figure slots render as labeled placeholders until the author adds the four images. The PDF is not compiled here.
- Updates the main README (release badge, a v0.6.0 summary, a full paper section and table of contents entry, the repository structure, and the citation version), this releases file, and the CHANGELOG (v0.6.0).
- All prose uses single dashes only. No em dashes, no double dashes, and no triple dashes outside of Markdown rules, Markdown table separators, and YAML document separators.

## Features

- papers/VVUQ-01/full-paper/main.tex: the preamble, the title page with the green ORCID mark and clickable paper DOI, the disclaimer below the abstract, the keywords, the table of contents, the figure placeholder machinery, and the section input lines.
- papers/VVUQ-01/full-paper/new_paper.sty: a single column Computer Modern serif style with ragged right body, widow and orphan control, raggedbottom, and raggedright paragraph column types, with black body and links and a green ORCID mark.
- papers/VVUQ-01/full-paper/references.bib: 29 final ieeetr entries spanning VVUQ and digital twin theory, credibility standards (ASME V&V 40, FDA), prior PDAC and oncology automation work, autonomous tooling, and open science, each with a DOI plus a clickable URL where one exists.
- papers/VVUQ-01/full-paper/README.md: DOI badges, the draft to full build diagram, the file layout, a section to source map, the figure slot table, the Overleaf compile recipe, the formatting contract, the bibliography rules, and ASCII diagrams.
- papers/VVUQ-01/full-paper/sections: abstract (under 300 words, no citations), introduction, methods, results, discussion, limitations_future, conclusions, references (the final bibliography block), and back_matter, each written in full.
- papers/VVUQ-01/full-paper/Images: the four author supplied figure slots plus a guide naming each expected image file.
- papers/VVUQ-01/full-paper/full-paper.zip: the Overleaf ready bundle of the LaTeX project.

## Contributors
@kevinkawchak
@claude
@openai

## Notes

This release adds the full paper built from the v0.5.0 draft scaffold without modifying the draft. It does not change the executable v0.1.0 source modules or the v0.2.0 through v0.5.0 records. The additions are LaTeX, Markdown, and a zip, all outside the ruff and yamllint surface, so lint-and-format (ruff check, ruff format check, yamllint) stays green across Python 3.10, 3.11, and 3.12, alongside validate-scripts and test (51 passed, 0 skipped). The paper is a draft: a VVUQ gate and a human reviewer must clear any deliverable before clinical use, and the Stage 2 references (the lights off factory and the hybrid surgery and medicine pilot) require VVUQ clearance, human oversight, IRB approval, and regulatory authorization before any real use. The four figures are added by the author later; the document compiles with labeled placeholders until then.

---

VVUQ-01 Draft Paper Scaffold with Processing Instructions (v0.5.0)
v0.5.0 - VVUQ-01 Draft Paper Scaffold with Processing Instructions

## Summary

- Adds papers/VVUQ-01/draft-paper, a complete and compilable single column LaTeX scaffold for the manuscript Two Stage VVUQ Oncology Clinical Trial Verification Automation Priority over Existing Generated Code, authored autonomously by Claude Code Opus 4.7 (1M context) Max in a managed cloud container, one file per commit, each pushed to GitHub in real time as part of a single pull request.
- The seven body section files carry bracketed processing instructions rather than finished prose; each names the exact cancer-automated directories and files to process and how to process them, so a future Claude Code Opus 4.7 (1M) Max pass can write a 70+ page paper. The title page, style file, bibliography, and back matter are final.
- Advances the paper generation leg of the thesis that the LLM VVUQ process must be more substantial than the generated artifact across codegen, imagegen, and papergen, accomplished faster and less expensively than conventional verification, toward faster, cheaper, and more rigorous physical AI oncology trials.
- The bibliography is final: 29 ieeetr entries. Every DOI entry carries its human readable DOI string and a clickable resolver URL in the note; repository entries carry both a GitHub and a Zenodo URL, each once, with no duplicate link and no howpublished field. Both the repository DOI and the paper DOI are clickable.
- Formatting follows a senior author contract: ragged right body for even inter-word spacing with no rivers, strong widow and orphan control, raggedright paragraph table columns, single dashes only, the section symbol §, and black links with a green ORCID mark matching the prior template.
- The bracketed instructions ground each section in the existing repository: the execution metrics and the full VVUQ gate decision surface, the codegen and execution per-commit tables, and the imagegen 02, 04, 06, and 08 Python data (the scripts are read for data, never the PNG files; the image-instruct directory is excluded).
- A draft-paper.zip bundle is provided for a one step Overleaf upload; the scaffold compiles as is and the bracketed blocks render as visible placeholders until the future pass replaces them. The PDF is not compiled here.
- Updates the main README (release badge, a v0.5.0 summary, a draft paper section and table of contents entry, the repository structure, and the citation version), this releases file, and the CHANGELOG (v0.5.0).
- All prose uses single dashes only. No em dashes, no double dashes, and no triple dashes outside of Markdown rules, Markdown table separators, and YAML document separators.

## Features

- papers/VVUQ-01/draft-paper/main.tex: the preamble, the title page with the green ORCID mark and clickable paper DOI, the disclaimer below the abstract, the keywords slot, the table of contents, and the section input lines.
- papers/VVUQ-01/draft-paper/new_paper.sty: a single column Computer Modern serif style with ragged right body, widow and orphan control, raggedbottom, and raggedright paragraph column types, with black body and links and a green ORCID mark.
- papers/VVUQ-01/draft-paper/references.bib: 29 final entries spanning VVUQ and digital twin theory, credibility standards (ASME V&V 40, FDA), prior PDAC and oncology automation work, autonomous tooling, and open science, each with a DOI plus a clickable URL where one exists.
- papers/VVUQ-01/draft-paper/README.md: DOI badges, the processing model that separates final files from bracketed instruction sections, the file layout, a section to source map, the Overleaf compile recipe, the formatting contract, the bibliography rules, and ASCII diagrams.
- papers/VVUQ-01/draft-paper/sections: abstract, introduction, methods, results, discussion, limitations_future, conclusions, references (the citation map plus the final bibliography block), and back_matter (final acknowledgments, ethics, rights, citation, and data availability text).
- papers/VVUQ-01/draft-paper/draft-paper.zip: the Overleaf ready bundle of the LaTeX project.

## Contributors
@kevinkawchak
@claude
@openai
@google-gemini

## Notes

This release adds a paper scaffold only; it does not change the executable v0.1.0 source modules or the v0.2.0 through v0.4.0 records. The seven body section files are bracketed instructions for a future Claude Code Opus 4.7 (1M) Max pass; the title page, style file, bibliography, and back matter are final. The additions are LaTeX, Markdown, and a zip, all outside the ruff and yamllint surface, so lint-and-format (ruff check, ruff format check, yamllint) stays green across Python 3.10, 3.11, and 3.12, alongside validate-scripts and test (51 passed, 0 skipped). The scaffold is a draft: a VVUQ gate and a human reviewer must clear any deliverable before clinical use, and the Stage 2 references (the lights off factory and the hybrid surgery and medicine pilot) require VVUQ clearance, human oversight, IRB approval, and regulatory authorization before any real use.

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
