## output-full-paper

This document records the narrative output of the full-paper run: what was read,
what was built, and how each requirement was met. It does not reproduce the LaTeX
source files themselves (those live alongside this file in
`papers/VVUQ-02/full-paper/`).

### What was produced

The full, Overleaf-compilable manuscript for **10 Mobile Pancreatic Cancer Unitree
H2 Surgical Humanoids: VVUQ Processing Priority over Code Generation**, processed
from the v1.1.0 `papers/VVUQ-02/draft-paper/` scaffold into
`papers/VVUQ-02/full-paper/`. Every bracketed processing instruction in the eight
body sections was replaced with finished, publication-grade prose and a
left-aligned table set to the body text width. The draft-paper directory was not
modified; the full paper is a separate bundle.

### Research and grounding

Before writing, the repository records named by the scaffold brackets were read so
every number is grounded rather than estimated:

- `papers/VVUQ-02/execution/README.md` (the key-results table, the source-executed
  table, the this-run-versus-conventional section, the limitations section, and the
  headline finding) and the five numbered execution sections, including
  `01-foundation/environment-and-verification.md` and `test-suite.md`,
  `02-pipeline/README.md`, `03-vvuq/README.md`, `04-automation/README.md`, and
  `05-humanoid-deployment/README.md` with their artifacts.
- `papers/VVUQ-02/codegen/` (the README, `config/project.yaml`,
  `config/vvuq_thresholds.yaml`, `config/standards_map.yaml`, the docs specs for the
  platform, hands, sensors, perception, suturing, and the VVUQ methodology, the
  fifteen test modules, and the two featured artifacts).
- `papers/VVUQ-02/inputs/` (the wired `standards/manifest.yaml`, the per-standard
  summaries, and the two clinical baselines).
- `papers/VVUQ-02/image-instruct/` for the five figures (03, 04, 05, 11, 13), used
  for the threshold values, the sensor channel statistics, the binding matrix, and
  the cost-bridge structure.

The two featured artifacts were inspected directly: `comparison.json` (confirmed
1790 lines, a four-entrant leaderboard, and 32 iterations of four rounds) and
`sample_h2_sensor.csv` (confirmed 1000 unique rows across 27 columns).

### Manuscript structure

- **Title page**: the replacement title, Kevin Kawchak with the green ORCID glyph
  and link, CEO ChemicalQDevice, the clickable `10.5281/zenodo.xxxxxxxx` DOI, and
  May 28, 2026.
- **Abstract** (single paragraph, 241 words, no citations) covering the autonomous
  workflow, the thesis, the headline gate and sweep metrics, the four-entrant
  tournament with the second-place explanation, and the external-standards
  strength, followed by the verbatim disclaimer and a one-line keyword set.
- **Introduction** (before the table of contents): the VVUQ primer in oncology-trial
  language, the single-humanoid thesis, the VVUQ-01 lineage and the broader
  autonomous program, the frozen scope and the regulatory moment, and four
  contributions mapped to Results.
- **Methods** (six subsections, five tables, the standards-wheel figure): the
  determinism floor, the 71-DOF platform and frozen configuration set, the
  Verify-Validate-Quantify-Evaluate ten-gate composition, the wired
  external-standards corpus, the pipeline and the 32-iteration design, and the
  172-test verification floor.
- **Results** (six subsections, five tables, the forest and safety-bands figures):
  the decision surface and thresholds, the executed behaviors, the sweep and the
  leaderboard, the featured sensor stream, the timeline and safety surface, and
  determinism.
- **Discussion** (four subsections, two tables, the binding-matrix and cost
  figures): what the test budget shows, the credibility argument against the
  standards, the cost-and-speed half, and comparison to prior work with practical
  insight.
- **Limitations and Future Work**, **Conclusions**, **References** (`\nocite{*}`
  over the 41-entry `ieeetr` bibliography with inline `\cite` anchoring), and the
  **back matter**.

### The four-entrant competition and the second-place result

The Results and the abstract foreground the tournament. The single mobile humanoid
(H2-Surgical 1.0, composite mean 93.334, win rate 0.75) places second to the
eight-arm PancreSpeed 1.0 cart (93.782, 0.875) by under half a composite point.
The explanation is structural: the six-component composite is weighted toward
throughput-sensitive components, and eight arms working in parallel complete the
eight-phase procedure with more simultaneous action than two hands, so the cart
edges ahead on the time-weighted score and wins the head-to-head round 24 of 32
times. The humanoid nonetheless carries more total wins (72 versus 56) because it
appears in three of the four rounds while the cart appears in two, and the win rate
normalizes for appearances. Where the prior PDAC paper featured the multi-arm cart
as the lone fast baseline, this study introduces the single mobile humanoid against
it and finds the humanoid within striking distance while concentrating all risk
into two hands, which is the higher-assurance case the paper is built around. Every
robot-involving verdict carries the simulation-against-simulation caveat.

### Figures (five placeholders)

Each figure keeps its space, dash, and underscore-free label and is referenced in
the body with `\autoref`: `fig:wheel` (Methods), `fig:forest` and `fig:bands`
(Results), and `fig:matrix` and `fig:cost` (Discussion). Each wraps an
`\IfFileExists` test so the manuscript compiles before the rendered PNGs are
dropped into `Images/`; the long placeholder paths use `\nolinkurl` so they break
cleanly and never run off the right margin.

### Formatting compliance

- Thirteen tables, each a `tabularx` set to `\textwidth` so it matches the body
  measure exactly, with every column left aligned and ragged right via the `L{}`
  and `Y` column types (each prepends `\raggedright\arraybackslash`). Long paths
  are abbreviated to leaf names with the parent path given once in the caption or
  the top row.
- The abstract is under 250 words with no citations and only a couple of short
  file names; file names otherwise live in tables, not in the prose.
- The section symbol `§` is used for clause references; single hyphens only, with
  double dashes confined to `\texttt` CLI flags; the navy Palatino styling is
  carried unchanged from the draft.
- `\sloppy`, `\emergencystretch`, `microtype`, and widow and club penalties of
  10000 keep word spacing even, avoid orphan and widow lines, and prevent
  right-margin overflow.

### Commit sequence (single pull request, pushed in real time)

1. `main.tex`
2. `new_paper.sty`
3. `references.bib`
4. `README.md`
5. `sections/abstract.tex`
6. `sections/introduction.tex`
7. `sections/methods.tex`
8. `sections/results.tex`
9. `sections/discussion.tex`
10. `sections/limitations_future.tex`
11. `sections/conclusions.tex`
12. `sections/back_matter.tex`
13. Error-fix and consolidation pass (balanced braces and environments, matched
    labels and `\autoref` targets, verified `\cite` keys, dash and symbol scans,
    the `Images/` placeholder, and the `full-paper.zip` bundle)
14. Repository updates (this file, `prompt-full-paper.md`, `releases.md` v1.2.0,
    `CHANGELOG.md` v1.2.0, the top-level README, and `CITATION.cff`)

### Verification and limitations of this run

`pdflatex` was not available in the container, and the prompt asked not to compile,
so the LaTeX was validated structurally: balanced braces and environments across
all files, every `\autoref` target matched to a `\label`, every `\cite` key present
in the bibliography, even dollar pairs, the correct column count for every
`tabularx` row, no unicode em or en dashes, and the section symbol used for clause
references. The repository `ruff check` and `ruff format --check` pass cleanly, and
no Python or linted YAML was added, so the `lint-and-format` CI matrix stays green
across Python 3.10, 3.11, and 3.12. All work was committed only to
`kevinkawchak/cancer-automated`; no other repository was touched, and the
`draft-paper/` directory was left untouched.
