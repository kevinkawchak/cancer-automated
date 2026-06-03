## output-full-bill

I built **H. R. 9510 Bill v3.0**, the finished visual amendment of the
*Verification Before Generation in Physical AI Oncology Trials Act of 2026*, into
`papers/VVUQ-05/full-bill`, by executing every bracketed drafting instruction in
the VVUQ-05 `draft-bill` scaffold against the exact files it names. The
drafting-instruction blocks and figure slots are gone: eleven text figures and ten
full-width tables are rendered on a white background, centered, and sized to their
content, and the full operative text of Bill v2.0 is carried so the bill stands on
its own. I committed it across a single pull request, one file per commit, pushed
to GitHub in real time, ending with an error-fix-and-bundle commit and a
repository-updates commit. Documentation release v3.1.0.

### What I read first (READMEs before files)

I started from the scaffold and the catalogs it points to, then opened only the
sources they named:

- `papers/VVUQ-05/draft-bill` (the v3.0 scaffold: `main.tex`, `usctitle.sty`,
  `references.bib`, the eight section files, and the README) to recover every
  bracketed instruction and the figure and table inventory.
- `papers/VVUQ-05/update-bill/figures-bill` (`01RootREADME.md`, `02VVUQ01.md`,
  `03VVUQ02.md`, `05VVUQ04.md`, and the README) for the verbatim ASCII diagrams,
  timelines, and tables.
- `papers/VVUQ-05/update-bill/next-steps` (`output-1-next-steps.md` and
  `output-2-next-steps.md`) for the pre-submission deliverables.
- `papers/VVUQ-04/final-bill` (`main.tex`, `README.md`, and the eleven
  `sections/*.tex` files) for the exact operative section 515D text, the ten-gate
  schedule, the conforming amendments, and the comparative print.
- `.github/workflows/ci.yml` and `ruff.toml` so the pull request stays green.

### The bill I produced

The bill keeps the formal congressional structure and renders every visual:

- **SECTION 1** (`main.tex`): short title and a **clickable, page-filling table of
  contents**; each entry links to its part and the entries are distributed with
  evenly spaced leaders to fill the remainder of the page.
- **SEC. 2 Findings** (`sections/s2-findings.tex`): the fourteen v2.0 findings
  condensed to a grounded lettered narrative, with Figure 1 (four-work lineage),
  Table 1 (the four works), and Figure 2 (accelerated timeline).
- **SEC. 3 Amendment** (`sections/s3-amendment.tex`): the new section 515D (21
  U.S.C. 360e-5), subsections (a) through (j), and the ten conforming amendments,
  with Table 2 (ten-gate threshold schedule), Figure 3 (decision rule and funnel),
  Figure 4 (statutory layering), and Table 3 (conforming crosswalk).
- **SEC. 4 Comparative print** (`sections/s4-comparative.tex`): Table 4 (change
  map), Figure 5 (the eleven sections in print order), and the eleven affected
  Title 21 provisions reproduced inline with insertions and deletions marked.
- **Appendix A** (`a5-evidence.tex`): Figures 6 to 8 (the gate funnel comparison,
  the procedure timelines, the humanoid safety figure) and Table 5 (standards map).
- **Appendix B** (`a6-deliverables.tex`): Table 6 and the completed deliverables
  package under `deliverables`.
- **Appendix C** (`a7-explainability.tex`): Figure 9 (prompt evolution), Figure 10
  (internal bill evolution), and Table 7 (the four NISTIR 8312 principles).
- **Appendix D** (`a8-research-matrix.tex`): Table 8, confining the emerging bills
  and executive actions to a non-operative matrix.
- **Appendix E** (`a9-transparency.tex`): Table 9 (version lineage), Table 10 (the
  single-PR commit schedule), and Figure 11 (the build-and-handoff process).

### The figure issue I fixed

The cover figure and every other figure are now **centered and correctly
weighted**. In `usctitle.sty` the ASCII figure is captured into a content-width
box (`BVerbatim` inside an `lrbox`), framed with a thin black rule on a white
fill, and centered on the page, so a figure is neither off-center nor stretched;
wide diagrams are set a size smaller so no line runs off the right margin, and
every figure renders as it would in a fenced GitHub Markdown block. All non-ASCII
symbols were kept out of the verbatim frames (the section symbol becomes "sec." in
diagrams), so the document compiles cleanly.

### The deliverables (processed as separate tasks)

I wrote the thirteen submission deliverables under `deliverables` as separate
tasks, each a standalone, submission-quality Markdown document with
white-background tables, single hyphens, the section symbol for codified
references, and no images or mermaid diagrams: the one-page summary, the
section-by-section analysis, the policy memo, the legislative findings, the
Ramseyer comparative print, the Constitutional Authority Statement, the PAYGO and
cost note, the sponsor and cosponsor packet, the stakeholder engagement plan, the
Legislative Counsel routing memo, the currency and cross-reference matrix, the
testimony and research-influence brief, and the package README. Each was committed
individually in real time.

### Formatting and fidelity

I centralized the senior-author formatting in `usctitle.sty`: white background
everywhere; centered, content-width ASCII figures; RaggedRight with even interword
spacing and a small right-skip stretch so no large gaps open and no line runs off
the right margin; maximal widow and orphan penalties so no single line is
stranded; an abbreviated, non-overlapping running header; URL breaking; single
hyphens only; the section symbol for every codified reference; and left-aligned,
ragged-right full-width tables (every column prepended with
`\raggedright\arraybackslash`, every table set to the body measure). I verified,
across all files, that braces and environments balance, every `\input` resolves,
every citation key exists, and every table row carries the right number of
columns.

### Commit plan (single pull request, real time)

main.tex; usctitle.sty; references.bib; the eight section files; the folder
README; the thirteen deliverables (one commit each); the error-fix-and-bundle
commit adding `prompt-full-bill.md`, `output-full-bill.md`, and
`full-bill-LaTeX.zip`; and the final repository-updates commit (the main
`README.md`, `releases.md` with the v3.1.0 notes, `CHANGELOG.md`, and
`CITATION.cff`). Only `kevinkawchak/cancer-automated` was edited, and the
additions are LaTeX, Markdown, BibTeX, and a zip, all outside the ruff and
yamllint surface, so the lint-and-format CI job passes across Python 3.10, 3.11,
and 3.12.

The result is a finished, legislator-readable visual amendment that stands on its
own, keeps every specific from the draft scaffold, and carries its full submission
package.
