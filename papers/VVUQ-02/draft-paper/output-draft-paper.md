## output-draft-paper

This document records the narrative output of the draft-paper run: what was
explored, what was built, and how each requirement was met. It does not reproduce
the LaTeX source files themselves (those live alongside this file in
`papers/VVUQ-02/draft-paper/`).

### What was produced

A complete LaTeX draft manuscript scaffold for **10 Mobile Pancreatic Cancer
Unitree H2 Surgical Humanoids: VVUQ Processing Priority over Code Generation**,
placed in `papers/VVUQ-02/draft-paper/`. The scaffold is a head start, not a
finished paper: every section body is a `[bracketed instruction]` that names the
exact repository files a future Claude Code Opus 4.7 (1M context) Max pass must
read and synthesise into publication-quality prose. The references are already
final, and the five figure floats, captions, labels, and `\autoref` targets are
already placed.

### Research and grounding

Before writing, the relevant directory READMEs and source files were read so the
instructions name real paths:

- `papers/VVUQ-02/templates/Template_04/` (the LaTeX scaffold: `main.tex`,
  `new_paper.sty`, `references.bib`, the eight section files).
- `papers/VVUQ-01/final-paper/references.bib` (the bibliography conventions and
  reusable entries; per the prompt, only bibtex was carried over).
- `papers/VVUQ-02/codegen/` (README, the ten-gate design, `config/`, `src/`,
  `tests/`, and the two featured data files).
- `papers/VVUQ-02/execution/` (the five-section execution record, the
  environment-and-verification report, the pipeline standards anchoring, the VVUQ
  decision surface, the automation tournament, and the deployment safety surface).
- `papers/VVUQ-02/inputs/` (the wired standards manifest and clinical baselines).
- `papers/VVUQ-02/image-instruct/` for figures 03, 04, 05, 11, and 13.

Two featured artifacts were inspected directly: `comparison.json` (confirmed 1790
lines, a `leaderboard` of four entrants, and 32 iterations of rounds) and
`sample_h2_sensor.csv` (confirmed 1000 data rows over 27 columns of per-hand arm,
finger-force, and end-effector channels). The external-standard reference URLs
were verified by web search so the bibliography links resolve.

### Manuscript structure

- **Title page**: the replacement title, Kevin Kawchak with the green ORCID glyph
  and link, CEO ChemicalQDevice, the clickable `10.5281/zenodo.xxxxxxxx` DOI, and
  May 28, 2026.
- **Abstract** (instructions: workflow overview, headline metrics, external
  standards strength, under 250 words) followed by the verbatim AI and
  independence disclaimer, then a one-line keyword set with no underline.
- **Introduction** before the table of contents (matching the template family):
  the VVUQ primer in oncology-trial language, the single-humanoid thesis, the
  VVUQ-01 lineage, the frozen scope, and the contributions.
- **Methods, Results, Discussion, Limitations and Future Work, Conclusions**, each
  a set of bracketed instructions naming exact files and the synergistic reads.
- **References** via `\nocite{*}` so all 41 entries render in the draft, with
  `ieeetr` printing the DOI and resolver URL from each `note` field.
- **Back matter**: acknowledgments, ethical disclosures, rights and permissions,
  cite-this-article with a clickable DOI, and data availability.

### Figures (five placeholders)

Each uses the provided figure-code block wrapped in `\IfFileExists` so the draft
compiles before the PNGs exist. One-line captions and space/dash/underscore-free
labels were assigned and `\autoref` is used in the body:

| Label | Section | Image |
|:--|:--|:--|
| `fig:wheel` | Methods | clinical and regulatory standards wheel (05) |
| `fig:forest` | Results | ten-gate threshold forest (03) |
| `fig:bands` | Results | sensor-stream safety bands (11) |
| `fig:matrix` | Discussion | gate to standard binding matrix (04) |
| `fig:cost` | Discussion | assurance cost assessment (13) |

### References

The bibliography is final and polished with 41 entries: the project anchors
(this paper and the prior VVUQ-01 paper, the cancer-automated repository with both
GitHub and Zenodo links, and Clinical-AI-Demos), the prior author program, the
domain literature, sixteen standards and regulatory references (ASME V&V 40-2018,
NASA-STD-7009A, IEC 80601-2-77, IEC 60601-1, ISO/TS 15066, ISO 13482, ISO 10218-1,
ISO 9283, IEC 62304, ISO 14971, ISO 13849-1, UL 4600, IEEE 7009, FDA CM&S
credibility, FDA real-time clinical trials, and ICH E6(R3)), the autonomous LLM
tooling, and open-science entries. Every entry carries the DOI string and the
clickable resolver URL in its `note`, repository entries carry GitHub and Zenodo
once each, and no `howpublished` field is used anywhere. Both the paper DOI and the
repository DOI resolve as clickable links.

### Formatting compliance

The global production directives are embedded in `main.tex` and the README:
left-aligned fixed-width table columns with `\raggedright\arraybackslash` on every
`p{}` width, abbreviated file names in tables with the parent path near the top,
no large white bands or right-margin overflow, no orphan or two-word lines, the
`§` symbol for clause references, single hyphens only, and the navy Palatino
styling carried unchanged from the template family.

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
13. Error-fix and consolidation pass (verified braces, environments, labels,
    dashes, `§`, and green ruff lint and format; added the `Images/` placeholder)
14. Repository updates (this file, `prompt-draft-paper.md`, the LaTeX zip,
    `releases.md` v1.1.0, `CHANGELOG.md` v1.1.0, the top-level README, and
    `CITATION.cff`)

### Verification and limitations of this run

`pdflatex` was not available in the container, so compilation was not performed
locally (the prompt also asked not to compile); instead the LaTeX was validated
structurally (balanced braces and environments, matched labels and references,
dash and symbol scans) and the bundle was made compile-safe with `\IfFileExists`
figure placeholders. The repository ruff lint and format checks pass cleanly, and
no Python or linted YAML was added, so the `lint-and-format` CI matrix stays green
across 3.10, 3.11, and 3.12. All work was committed only to
`kevinkawchak/cancer-automated`; no other repository was touched.
