## output-draft-bill

I built **H. R. 9510 Bill v3.0**, the visual draft of the *Verification Before
Generation in Physical AI Oncology Trials Act of 2026*, into
`papers/VVUQ-05/draft-bill`. It is a LaTeX scaffold: it keeps the full operative
text of Bill v2.0 (the VVUQ-04 `final-bill`) so it stands on its own as a bill,
and it layers a visual perspective on top, with figure and table slots and
bracketed drafting instructions that name the exact files a future Claude Code
Opus 4.8 (1M context) Max pass must process to render each visual on a white
background and to write each submission deliverable. I committed it across a
single pull request, one file per commit, pushed to GitHub in real time, ending
with an error-fix-and-bundle commit and a repository-updates commit.

### What I read first (READMEs before files)

I started from the README and index files, as instructed, then opened only the
sources they pointed to:

- `papers/README.md` and `papers/VVUQ-04/final-bill/README.md` and `main.tex`
  (Bill v2.0, the basis), and `papers/VVUQ-04/draft-bill` (the analogous
  bracketed-instruction scaffold and its `usctitle.sty` `draftbox` macros).
- `papers/VVUQ-05/update-bill/figures-bill/README.md` and the five catalogs
  (`01RootREADME.md`, `02VVUQ01.md`, `03VVUQ02.md`, `04VVUQ03.md`,
  `05VVUQ04.md`), which hold every ASCII diagram, timeline, repository tree, and
  table across VVUQ-01 through VVUQ-04.
- `papers/VVUQ-05/update-bill/next-steps` (`output-1-next-steps.md` and
  `output-2-next-steps.md`), which define the pre-submission deliverables.
- The prompt-evolution files across the works and the CI workflow
  (`.github/workflows/ci.yml`, `ruff.toml`) so the pull request stays green.

### The structure I produced

The bill keeps the formal congressional structure so it is still a bill, and adds
five non-operative appendices that carry the visual, deliverable, and
explainability perspective. Sections are defined by the figures and tables they
share.

- **SECTION 1** (in `main.tex`): short title and table of contents.
- **SEC. 2 Findings** (`sections/s2-findings.tex`): the fourteen v2.0 findings
  condensed to a lettered narrative, with Figure 1 (four-work lineage), Table 1
  (the four works at a glance), and Figure 2 (accelerated timeline).
- **SEC. 3 Amendment** (`sections/s3-amendment.tex`): the new section 515D (21
  U.S.C. 360e-5) and the ten conforming amendments, with Table 2 (ten-gate
  threshold schedule), Figure 3 (gate decision surface and funnel), Figure 4
  (statutory layering), and Table 3 (conforming crosswalk).
- **SEC. 4 Comparative print** (`sections/s4-comparative.tex`): Table 4 (the
  per-section change map) and Figure 5 (Title 21 threading).
- **Appendix A Visual engineering evidence** (`sections/a5-evidence.tex`):
  Figures 6 to 8 (the gate funnel comparison, the procedure timelines, the
  humanoid safety figure) and Table 5 (the external standards map).
- **Appendix B Required submission deliverables** (`sections/a6-deliverables.tex`):
  Table 6 and a per-deliverable instruction for twelve standalone, submission-
  quality Markdown documents plus a package README under
  `papers/VVUQ-05/deliverables`.
- **Appendix C The VVUQ explainability standard** (`sections/a7-explainability.tex`):
  Figure 9 (prompt evolution), Figure 10 (internal bill evolution), and Table 7
  (the standard mapped to the four NISTIR 8312 principles).
- **Appendix D Research influence matrix** (`sections/a8-research-matrix.tex`):
  Table 8, confining the emerging bills and executive actions to a non-operative
  matrix.
- **Appendix E Development transparency and commit schedule**
  (`sections/a9-transparency.tex`): Table 9 (version lineage), Table 10 (the
  single-PR commit schedule), and Figure 11 (the build-and-handoff process).

### How the three objectives are met

- **(a) A visualization of Bill v2.0.** Appendix A and the figure and table slots
  throughout draw their visuals from `papers/VVUQ-05/update-bill/figures-bill`;
  each slot names the exact catalog file and heading to render from.
- **(b) Instructions for every deliverable.** Appendix B gives one bracketed
  instruction per deliverable, naming the output file under
  `papers/VVUQ-05/deliverables`, its purpose, and the exact source files, and
  specifying each as complete and submission quality at this bill version.
- **(c) A new explainability standard.** Appendix C establishes the VVUQ-01
  through VVUQ-04 record (recorded prompts, outputs, VVUQ gates, and commit
  trail) as a reusable standard for explaining how United States legislation was
  created.

### Formatting and fidelity

I centralized the senior-author formatting in `usctitle.sty`: a white background
everywhere; RaggedRight with even interword spacing and a small right-skip
stretch so no large gaps open and no line runs off the right margin; maximal
widow and orphan penalties so no single line is stranded; an abbreviated,
non-overlapping running header; URL breaking; single hyphens only; the section
symbol for every codified reference; and left-aligned, ragged-right full-width
tables (every column prepended with `\raggedright\arraybackslash`). ASCII figures
are set verbatim in white, black-ruled monospace frames so they look as they
would in a fenced GitHub Markdown block. The cover page is condensed to a single
long title dated June 3, 2026, closing with an ASCII overview of the v3.0
process; there are no images, mermaid diagrams, or colored figures.

### Commit plan (single pull request, real time)

main.tex; usctitle.sty; references.bib; the eight section files
(s2-findings, s3-amendment, s4-comparative, a5-evidence, a6-deliverables,
a7-explainability, a8-research-matrix, a9-transparency); README.md; the
error-fix-and-bundle commit adding `prompt-draft-bill.md`, `output-draft-bill.md`,
and `draft-bill-LaTeX.zip`; and the final repository-updates commit (the main
`README.md`, `releases.md` with the v3.0.0 notes, `CHANGELOG.md`, and
`CITATION.cff`). Only `kevinkawchak/cancer-automated` is edited, and the
additions are LaTeX, Markdown, BibTeX, and a zip, all outside the ruff, yamllint,
and pytest surface, so the lint-and-format CI job passes across Python 3.10,
3.11, and 3.12.

This draft is a head start by design: the next pass spends its effort on
synthesis, not on searching, because every figure, table, and deliverable names
the exact files to process.
