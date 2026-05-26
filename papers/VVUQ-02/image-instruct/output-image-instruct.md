## output-image-instruct

This file records the narrative markdown output of the Claude Code Opus 4.7 (1M
context) Max run that authored the `papers/VVUQ-02/image-instruct/` set. It is the
markdown output of the run, not the figure scripts or the rendered images (those
are produced at a future date under `papers/VVUQ-02/imagegen/`). The generating
prompt is in `prompt-image-instruct.md`. The prior lineage is the instruction
prompt and output in `papers/VVUQ-02/instructions/`, the codegen prompt and output
in `papers/VVUQ-02/codegen/` (`prompt-codegen.md`, `output-codegen.md`), and the
execution prompt and output in `papers/VVUQ-02/execution/` (`prompt-execution.md`,
`output-execution.md`).

## Approach

I read the full task, then surveyed the two grounding trees without modifying
them: the VVUQ-02 codegen tree (v0.7.0) and the VVUQ-02 execution tree (v0.8.0). I
read the codegen `config/project.yaml`, `config/vvuq_thresholds.yaml`, and
`config/standards_map.yaml`; the `results/comparison.json` and its report; the
featured `data/sample_h2_sensor.csv`; and the input corpus under `inputs/`. I read
every execution section README and its artifacts: `01-foundation/test-suite.md`
(172 tests across 15 modules), `02-pipeline` (the intent to compile to act to
score record and the external-standards anchoring), `03-vvuq` (the 10 gates, their
thresholds, and the five-case decision surface), `04-automation` (the 32-iteration
sweep, the gated composite, and the 1790-line four-entrant tournament), and
`05-humanoid-deployment` (the 60-second 8-phase timeline, the 1000-row sensor
stream analysis, and the three catastrophe safety surfaces). I confirmed the
VVUQ-01 image-instruct directory as the structural template and mirrored its
shape, the shared page frame, the professional palette, the processing model, and
the per-figure specification format, for VVUQ-02.

A key design choice was to keep the set instructions-only and lint-safe by
construction. Every file added under `image-instruct/` is Markdown, so the pull
request carries no Python or YAML and cannot introduce a `ruff` or `yamllint`
failure; the `lint-and-format`, `validate-scripts`, and `test` CI jobs stay green
across Python 3.10, 3.11, and 3.12. The matplotlib scripts and 300 dpi PNG files
are specified in full but deferred to a future `imagegen` pull request, exactly as
VVUQ-01 separated `image-instruct` from `imagegen`.

A second design choice was to ground every number. Each figure instruction names
the exact source path for every value it uses, so a future agent renders by direct
lookup rather than estimation. I verified the arithmetic invariants by computation
before release.

## What I produced

I authored 18 Markdown files: the master `README.md` (conventions, the 15-spec
index, the data-availability mapping, DOI badges, the repository-structure ASCII,
the file-generation outcomes, and the consistency pass), the two lineage files
(`prompt-image-instruct.md` verbatim and this `output-image-instruct.md`), and the
15 figure specifications, each at `NN-name/README.md`.

## The 15 figures and why each was chosen

I picked 15 of the 20 chart families for best data availability and relevance, all
distinct (no family reused), and avoided the basic grouped bar, the pie or donut,
the duplicate scatter-regression family, the Kaplan-Meier curve, and the ROC curve
(the last two because VVUQ-02 carries no time-to-event or labeled-classifier
ground truth to ground them honestly). Six figures satisfy the required-data
brief.

1. Platform pipeline flow (workflow diagram, both): generation to assurance in
   three tiers, the assurance tier visibly thickest. Grounded in execution §02 and
   the execution README flow.
2. VVUQ gate decision funnel (funnel, both): five decision cases narrow through
   verify, validate, quantify, and the hard predicate to one ACCEPT. Grounded in
   execution §03 and `vvuq_thresholds.yaml`.
3. Ten-gate threshold forest (forest plot, both, R3): the 10 gates by validation
   agreement, maximum relative error, and CV bound, catastrophe gates strictest.
   Grounded in execution §03 and `vvuq_thresholds.yaml`.
4. Gate to standard binding matrix (heatmap, both, R2): 10 gates plus a
   cross-cutting row against 15 standards; every standard used at least once.
   Grounded in `standards_map.yaml`, the manifest, and the anchoring tables in
   execution §02, §03, and §05.
5. Clinical and regulatory standards wheel (wheel, codegen, R4): the input corpus,
   14 consensus standards and 2 clinical baselines across 6 domains, with the
   regulatory relevancy called out. Grounded in `inputs/` and `project.yaml`.
6. 172-test coverage treemap (treemap, execution, R1): all 172 tests across 15
   modules in 3 subsystems, the 64-test gate suite dominant. Grounded in execution
   §01 `test-suite.md`.
7. Validation parity scatter (parity plot, both): observed versus independent
   reference, on-diagonal passes, off-diagonal blocks, dispersion escalates.
   Grounded in execution §03 `vvuq_decisions.json` and the adversarial cases.
8. Sweep composite strip plot (strip plot, execution): the 32 gated composite
   scores with mean and range, and the gating overlay lane. Grounded in execution
   §04 `composite_scores.jsonl`.
9. Composite weighting waterfall (waterfall, both): the six frozen composite
   weights cascade to 1.00, then the gating overlay. Grounded in `project.yaml` and
   execution §04.
10. Four-entrant comparison box plot (box plot, both, R6): the 1790-line tournament
    distributions, the H2 humanoid featured at rank 2. Grounded in
    `comparison.json` and execution §04.
11. Sensor stream safety bands (line with bands, both, R5): three channels of the
    featured 1000-row stream versus their gate bounds. Grounded in
    `sample_h2_sensor.csv` and execution §05.
12. Eight-phase Whipple swimmer (swimmer plot, both): the 60-second timeline as
    hand lanes plus suturing and continuous safety lanes. Grounded in `project.yaml`
    phases and execution §05.
13. Assurance cost assessment (financial bridge, both): the cost half of the
    thesis as an illustrative, clearly labeled relative index grounded in the
    execution README this-run-versus-conventional section.
14. Value proposition matrix (value matrix, both): a credibility versus efficiency
    quadrant plus the three thesis pillars and the stakeholder value. Grounded in
    the execution README thesis, execution §03, and the standards map.
15. Platform mind map (mind map, both): a one-page radial overview of the platform,
    the codegen modules, the 10 gates, the standards, the execution sections, and
    the lineage.

## How a future agent processes the set

Each instruction is written so Claude Code Opus 4.7 (1M) Max can render it with no
further questions and no manual positioning: read the instruction, read the master
README for the shared frame and palette, confirm the grounding values, author one
self-contained `matplotlib` plus `numpy` script at
`papers/VVUQ-02/imagegen/NN-name/NN-name.py`, build to the portrait full-page frame
(`figsize=(8.5, 11)`, 300 dpi, white background, deterministic `GridSpec`), save to
`papers/VVUQ-02/imagegen/NN-name/NN-name.png`, verify against the per-figure
checklist, confirm `ruff check` and `ruff format --check` pass, and commit the
script and the PNG together. The full processing model is in the master README.

## The error-fix pass (commit 16)

I cross-checked all 15 instructions as a set. The arithmetic reconciles: the
treemap counts sum to 172 across 15 modules and to subsystem totals 76, 74, and
22; the composite weights sum to 1.00; the swimmer durations sum to 60 s; the
four-entrant appearance counts sum to 256 over 128 verdicts; and the 32 strip-plot
composite values reproduce min 93.417, max 93.715, and mean 93.562 exactly. The
grounding matches the source files, including the 10 gate thresholds, the
five-case decision surface, the leaderboard means, and the 1000-row channel
ranges. Symbols and dashes are clean: the section symbol renders as `§`, and only
single hyphens appear in the visible figure text, with triple dashes confined to
Markdown table separators and ASCII-diagram art. Naming is one to one between each
`NN-name` instruction and its future `imagegen/NN-name/NN-name.py` and `.png`. I
refined the sensor-stream figure so it frames the raw force samples as the gate
input rather than implying the raw sample is itself a guaranteed-safe trace.

## Repository updates (commit 17)

The final commit updates only `kevinkawchak/cancer-automated`: the top-level
`README.md` (release badge to v0.9.0, a short v0.9.0 summary above the prior
summary, a VVUQ-02 image instructions section with an ASCII diagram and a table of
contents entry, the repository structure tree with the image-instruct directory
expanded, and the citation version), `releases.md` (the v0.9.0 release notes),
`CHANGELOG.md` (v0.9.0), and `CITATION.cff`. No images, Mermaid diagrams, or
colored images are added anywhere. No other repository is touched.

## Limitations and honest notes

- This set contains instructions only. No script and no image is rendered here;
  rendering is a future `imagegen` pull request that requires `matplotlib`
  installed in that environment.
- The assurance cost assessment (figure 13) uses an illustrative relative index,
  not measured dollars, because the repository records no cost figures; the
  direction and the advantages are grounded verbatim in the execution README, and
  the axis is labeled illustrative so the figure does not overclaim.
- The H2-Surgical 1.0 is a clearly labeled hypothetical 2030 platform and every
  number is a simulation result; the four-entrant comparison is simulation against
  simulation, and the figures carry the same caveats as the source records.
- The figures are planning and documentation artifacts. The 10 VVUQ gates plus a
  recorded human reviewer must clear any deliverable before clinical use, and a
  real deployment would require IEC 80601-2-77, IEC 60601, ISO 13482, FDA SaMD
  Class III clearance, IRB approval, and regulatory authorization.

## Thesis link

The robotic code assurance process, not code generation, is the substantial and
decision bearing part of the AI workflow, holding VVUQ to a higher standard than
code itself. These figures specify, ahead of any rendering, exactly how that
assurance story is shown: the gate funnel, the threshold forest, the standards
binding, the test budget, the decision parity, and the gated composite all make
the assurance layer the visible center of the platform, which is the image
generation analog of the VVUQ gate and the basis for a future technical paper.
