# Changelog

All notable changes to this repository are documented here.
Format follows [Keep a Changelog](https://keepachangelog.com/).

## [Unreleased]

## [3.0.0] - 2026-06-03

### Added
- `papers/VVUQ-05/draft-bill/`: H. R. 9510 Bill v3.0, a LaTeX visual draft of the
  *Verification Before Generation in Physical AI Oncology Trials Act of 2026*. It
  keeps the full operative text of Bill v2.0 (the `papers/VVUQ-04/final-bill`
  amendment) so it stands on its own, and adds a more visual perspective: every
  operative part carries a figure or table slot, and a set-off drafting-instruction
  block names the exact repository files a future Claude Code Opus 4.8 (1M context)
  Max pass processes to render that figure or table on a white background as a
  text-based diagram, with no raster image.
- `papers/VVUQ-05/draft-bill/main.tex`, `usctitle.sty`, and `references.bib`: the
  assembler (condensed caption with the v3.0 process diagram, SECTION 1, the
  section inputs, and the back matter), the v3.0.0 style (US Code reproduction,
  amendment apparatus, the restored draftbox, and the white-background asciifig,
  figslot, and figcaption visual primitives), and 94 ieeetr sources (the Bill v2.0
  authority set plus the v3.0 layer).
- `papers/VVUQ-05/draft-bill/sections/`: eight section files defined by their
  common figures and tables (`s2-findings`, `s3-amendment`, `s4-comparative`,
  `a5-evidence`, `a6-deliverables`, `a7-explainability`, `a8-research-matrix`,
  `a9-transparency`), each with operative or framing text, figure and table slots,
  and a draftbox of bracketed instructions naming the exact files to process.
- `papers/VVUQ-05/draft-bill/README.md`, `prompt-draft-bill.md`,
  `output-draft-bill.md`, and `draft-bill-LaTeX.zip`: the landing page, the prompt
  verbatim, the narrative output, and the Overleaf-ready bundle.
- Answers three objectives: a visualization of Bill v2.0 from
  `papers/VVUQ-05/update-bill/figures-bill`; instructions for every U.S. House
  submission deliverable to be written under `papers/VVUQ-05/deliverables` based on
  `papers/VVUQ-05/update-bill/next-steps`, each complete and submission quality;
  and a new explainability standard from the VVUQ-01 through VVUQ-04 record.
- Authored autonomously across sequential commits in a single pull request, one
  file per commit pushed in real time, then a second-to-last error-fix-and-bundle
  commit and a final repository-updates commit. The additions are LaTeX, BibTeX,
  Markdown, and a zip, outside the ruff, yamllint, and pytest surface, so the
  lint-and-format CI job passes across Python 3.10, 3.11, and 3.12.

### Changed
- `README.md`: release badge to v3.0.0, a v3.0.0 summary above the prior summary,
  one new "H. R. 9510 Bill v3.0 (Visual Draft)" section with a table-of-contents
  entry, and the repository structure tree extended with a `VVUQ-05` block.
- `releases.md`: v3.0.0 release notes added above v2.3.1.
- `CITATION.cff`: version bumped to 3.0.0.

## [2.3.1] - 2026-06-01

### Added
- `papers/README.md`: a comprehensive landing page for the four sequential VVUQ
  works, detailing the verification developments and progress for each VVUQ-xx
  directory, the building process from one work to the next with ASCII diagrams,
  what the results mean for the new Physical AI oncology trial industry, the
  processing feat accomplished by AI, and the accelerated timeline versus
  conventional methods to reach the final VVUQ-04 bill. Includes DOI badges, the
  repository structure, ASCII diagrams, and the final paper or bill DOI for each
  work in a "Please see Zenodo for author final edits: PDF and LaTeX Source
  Files" line.
- `papers/VVUQ-01/README.md`, `papers/VVUQ-02/README.md`,
  `papers/VVUQ-03/README.md`, and `papers/VVUQ-04/README.md`: one landing page per
  work, each focused only on its own directory, with the verification
  developments and progress, the building process within the work shown with
  ASCII diagrams, what the results mean for the industry, the processing feat
  accomplished by AI, and the accelerated timeline versus conventional methods to
  reach that work's end goal. Each includes DOI badges, the repository structure,
  and the final paper or bill DOI for all four works in an organized table.
- Authored autonomously across sequential commits in a single pull request, one
  README per commit pushed in real time, then a second-to-last error-fix commit
  and this final repository-updates commit. The additions are Markdown only and
  contain no images or mermaid diagrams.

### Changed
- `README.md`: release badge to v2.3.1, a v2.3.1 summary above the prior summary,
  a new "Papers Directory READMEs" section with a table-of-contents entry, and the
  repository structure tree extended with the five new `README.md` files.
- `releases.md`: v2.3.1 release notes added above v2.3.0.
- `CITATION.cff`: version bumped to 2.3.1.
- @kevinkawchak made main/README.md more concise by abbreviating summaries and paragraphs on 2026-06-02.
- @kevinkawchak added prompts and outputs to next-steps; and added prompt and outputs to figures-bill 2026-06-02.

## [2.3.0] - 2026-06-01

### Added
- `papers/VVUQ-04/full-bill/`: the finished, Overleaf-compilable LaTeX amendment
  to the Federal Food, Drug, and Cosmetic Act (21 U.S.C. § 301 et seq.),
  processed from the v2.2.0 `draft-bill` scaffold by executing every bracketed
  drafting instruction against the named `instruct-bill` and `VVUQ-03/final-paper`
  sources. The bill is H. R. 9510, the Verification Before Generation in Physical
  AI Oncology Trials Act of 2026. Authored autonomously across sequential commits
  in a single pull request, one file per commit pushed in real time, then a
  second-to-last error-fix-and-bundle commit and a final repository-updates
  commit. The input `draft-bill` directory is left untouched.
- `main.tex` (caption with H. R. 9510 and a cover-page provenance note, SECTION 1
  short title and table of contents, SEC. 2 with 14 grounded findings, SEC. 3 the
  new section 515D / 21 U.S.C. § 360e-5 plus ten conforming amendments and the
  clerical, rule-of-construction, and effective-date changes, SEC. 4 the
  comparative print, Appendix A research-influence matrix, Appendix B
  development-transparency and implementation statement, and references),
  `usctitle.sty` (US Code reproduction plus the amendment apparatus, the
  header-overlap fix, URL breaking, and full-width ragged-right tables; the
  draftbox is removed), `references.bib` (79 ieeetr entries), a detailed
  `README.md` with DOI badges and ASCII diagrams, `full-bill-LaTeX.zip`, and
  `prompt-full-bill.md` and `output-full-bill.md`.
- `papers/VVUQ-04/full-bill/sections/`: the 11 comparative-print sections (s301,
  s321, s331, s351, s355g, s360, s360c, s360e, s360e-4, s360j, s360k), each a
  focused print of the affected provisions with insertions and deletions marked.
  The new operative duty is section 515D inserted after § 360e-4.

### Changed
- `README.md`: release badge to v2.3.0, a v2.3.0 summary above the prior summary,
  a new "VVUQ-04 Full Bill (LaTeX)" section with an ASCII process diagram and a
  table-of-contents entry, and the repository structure tree extended with a
  `VVUQ-04/full-bill` block.
- `releases.md`: v2.3.0 release notes added above v2.2.0.
- `CITATION.cff`: version bumped to 2.3.0.
- @kevinkawchak updated cancer-automated/blob/main/papers/VVUQ-04/final-bill/README.md with final bill files and link to Zenodo PDF on 2026-06-01.
- @kevinkawchak added a supplementary prompt and output to cancer-automated/tree/main/papers/VVUQ-04/update-bill, and made version summaries more concise in main/README on 2026-06-01.

## [2.2.0] - 2026-06-01

### Added
- `papers/VVUQ-04/draft-bill/`: a LaTeX draft amendment to the Federal Food,
  Drug, and Cosmetic Act (21 U.S.C. § 301 et seq.) that recasts the prior *VVUQ
  Physical AI Oncology Trial Bill* (H.R. 9510) as a properly targeted amendment.
  Following the amendment-drafting correction, it amends the Act and cites each
  affected provision by its 21 U.S.C. section number, naming Public Law 119-93
  only as the currency point, rather than amending Public Law 119-93 or Title 21
  generally. It is an amendment scaffold with bracketed DRAFTING INSTRUCTIONS,
  not a finished bill: each part names the exact `papers/VVUQ-04/instruct-bill`
  and `papers/VVUQ-03/final-paper` files a future Claude Code Opus 4.8 (1M
  context) Max pass must process. Authored autonomously across sequential commits
  in a single pull request, one file per commit pushed in real time, then a
  second-to-last error-fix commit and a final repository-updates commit.
- `main.tex` (bill caption, A BILL head and enacting clause, SECTION 1 short
  title and table of contents, SEC. 2 findings, SEC. 3 amendment with new section
  515D / 21 U.S.C. § 360e-5 plus conforming, clerical, rule-of-construction, and
  effective-date changes, SEC. 4 comparative print, Appendix A research-influence
  matrix, authorship and notices, references), `usctitle.sty` (US Code
  reproduction commands plus the congressional amendment apparatus, the
  comparative-print markers, the DRAFTING INSTRUCTIONS `draftbox`, and formatting
  hardening), `references.bib` (provenance and research sources including the
  required `uscode_download` reference), a detailed `README.md` with DOI badges
  and ASCII diagrams, `draft-bill-LaTeX.zip` (Overleaf-ready bundle), and
  `prompt-draft-bill.md` and `output-draft-bill.md`.
- `papers/VVUQ-04/draft-bill/sections/`: the 11 reproduced Title 21 device
  sections (s301, s321, s331, s351, s355g, s360, s360c, s360e, s360e-4, s360j,
  s360k), each keeping its original statutory text and adding a `draftbox` of
  bracketed instructions with exact directories and file names, the amendatory
  action, and the comparative-print markers. The new operative duty is a new
  section 515D inserted after § 360e-4 (the change-control keystone).

### Changed
- `README.md`: release badge to v2.2.0, last-updated badge to June 2026, a
  v2.2.0 summary above the prior summary, a new "VVUQ-04 Draft Bill (LaTeX)"
  section with an ASCII process diagram and a table-of-contents entry, and the
  repository structure tree extended with a `VVUQ-04/draft-bill` block.
- `releases.md`: v2.2.0 release notes added above v2.1.0.
- `CITATION.cff`: version bumped to 2.2.0 and date to 2026-06-01.

## [2.1.0] - 2026-05-31

### Added
- `papers/VVUQ-04/template-bill/LaTeX/`: a LaTeX template bill that reproduces
  the look and feel of the official United States Code, Title 21 - Food and Drugs
  (current through Public Law 119-93), reduced from the source USLM XML
  (`papers/VVUQ-04/template-bill/xml_usc21@119-93.zip`; 29 chapters, 757
  sections) to the 11 Federal Food, Drug, and Cosmetic Act device sections
  relevant to the Physical AI oncology trial context, so a future Claude Code
  Opus 4.8 (1M context) Max pass can read the laws in place and, with
  `papers/VVUQ-04/instruct-bill` and `papers/VVUQ-03/final-paper`, draft the
  amendment to Public Law 119-93, Title 21. No bracketed instructions or file
  names are inserted into the statutory text. Authored autonomously across
  sequential commits in a single pull request, one file per commit pushed in real
  time, then a second-to-last error-fix commit and this final
  repository-updates commit.
- `main.tex` (Title 21 head, section analysis, Chapter 9 / subchapter / part
  structure, eleven `\input` lines, provenance references), `usctitle.sty` (the
  United States Code style: Times-like serif, hanging-indent (a)(1)(A)(i)(I)
  hierarchy, cross-headings, small-caps note headings, source credits), and
  `references.bib` (11 ieeetr entries, bare DOIs, resolver URLs, no
  `howpublished`, no duplicate links).
- Eleven section files, one per retained section: `s301` (short title), `s321`
  (definitions; device definition in (h)), `s331` (prohibited acts), `s351`
  (adulterated drugs and devices), `s355g` (real world evidence), `s360`
  (registration; 510(k) in (k)), `s360c` (classification), `s360e` (premarket
  approval), `s360e-4` (predetermined change control plans), `s360j` (general
  device provisions; software/CDS exclusion in (o)), and `s360k` (state
  preemption).
- `README.md` (DOI badges, per-section contents table, statutory-layering and
  file-correlation diagrams, exclusion rationale, Overleaf compile recipe),
  `template-bill-LaTeX.zip` (Overleaf-ready bundle),
  `prompt-template-bill/LaTeX.md` (the generating prompt, verbatim), and
  `output-template-bill/LaTeX.md` (the narrative output of this step).

### Changed
- `README.md` release badge to v2.1.0, a v2.1.0 summary above the prior summary,
  a VVUQ-04 Template Bill (LaTeX) section with an ASCII process diagram and a
  table-of-contents entry, and the repository structure tree with a VVUQ-04
  template-bill/LaTeX block; `releases.md` (v2.1.0); and `CITATION.cff` (version
  2.1.0).

## [2.0.0] - 2026-05-31

### Added
- `papers/VVUQ-04/instruct-bill/`: structured U.S. medical AI bill and law
  summaries (current through May 31, 2026) that bring the *VVUQ Physical AI
  Oncology Trial Bill* (H.R. 9510, Draft 1.0) up to date for a future Claude Code
  Opus 4.8 (1M context) Max pass that will read these files plus
  `papers/VVUQ-03/final-paper` and draft a new bill version (later converted to
  XML). Authored autonomously across sequential commits in a single pull request,
  one file per commit pushed to GitHub in real time, then a second-to-last
  error-fix commit and this final repository-updates commit.
- Ten instruction markdown files (01 to 10): federal statutory framework; FDA AI
  and ML device regulation; ONC and ASTP algorithm transparency; CMS coverage and
  payment; privacy, security, and nondiscrimination; state medical AI laws;
  executive actions and national AI strategy; emerging federal bills (research
  influences only); VVUQ standards with clinical-trial and oncology law; and a
  legal crosswalk, research matrix, and bill-style template.
- Five BibTeX bibliographies (145 entries total): federal-statutes.bib (20),
  federal-regulations-guidance.bib (36), state-laws.bib (20),
  executive-actions-and-emerging-bills.bib (25), and standards-and-literature.bib
  (44), each with bare DOIs, resolver or canonical URLs, and a note with the
  clickable link; no `howpublished` field and no duplicate links across the set.
- `README.md` (DOI badges, repository structure, file-to-file and
  file-to-bibliography correlation diagrams), `prompt-instruct-bill.md` (the
  generating prompt, verbatim), and `output-instruct-bill.md` (the narrative
  output of this step).
- Verified developments through May 31, 2026 including the FDA PCCP final
  guidance and QMSR, the ONC HTI-1 and HTI-5 rules, the CMS Medicare Advantage AI
  rule and WISeR model, Section 1557 § 92.210, the 2024 to 2026 state AI laws, EO
  14179 and the AI Action Plan, the 119th Congress bills, and the ASME, IEC, ISO,
  IEEE, and ICH standards, with antidiscrimination citations corrected to Title 42
  and Title 29 and the section symbol § used throughout.

### Changed
- Top-level `README.md`: release badge to v2.0.0, a v2.0.0 summary above the prior
  summary, a VVUQ-04 Instruct Bill section with an ASCII process diagram and a
  table-of-contents entry, and the repository structure tree with a VVUQ-04
  instruct-bill block.
- `releases.md` (v2.0.0 notes) and `CITATION.cff` (version 2.0.0).

## [1.4.0] - 2026-05-30

### Added
- `papers/VVUQ-03/full-paper/`: the full, Overleaf-compilable manuscript for the
  *VVUQ Physical AI Oncology Trial Bill* (H.R. 9510, 119th Congress, 2d Session;
  Draft 1.0), a proposed United States bill requiring an automated VVUQ
  verification process to clear robot-patient interaction code before that code is
  generated or executed. Processed from the v1.3.0 draft-paper scaffold by Claude
  Code Opus 4.8 (1M context) Max running autonomously across 21 commits in a
  single pull request, one file per commit pushed to GitHub in real time, then a
  second-to-last error-fix and consolidation commit and a final
  repository-updates commit. The `draft-paper/` directory is left untouched.
- `main.tex` (cover page with the H.R. 9510 and 119th Congress designation, table
  of contents, fifteen section `\input` lines, `xltabular` and `float` added for
  full-width breakable tables, navy clickable hyperlinks, and the global
  formatting directives), `new_paper.sty` (Palatino body with the navy accent
  carried from the draft, widow, club, and broken penalties at 10000, and even
  list spacing), and `references.bib` (the final 60-entry `ieeetr` bibliography
  with DOIs and clickable URLs and no `howpublished` field).
- Fifteen `sections/*.tex` files, each finished legislative prose with
  left-aligned body-width tables (21 tables total): abstract, policy_memo,
  problem_statement, definitions, findings, algorithm_documentation,
  attestations_compliance, prior_law, supporting_documentation, statutory_text,
  implementation_enforcement, section_by_section, limitations_future, conclusions,
  and back_matter.
- The four required main points as their own sections, with Algorithm
  Documentation featuring the 1790-line four-entrant `comparison.json` and the
  1001-row non-repetitive `sample_h2_sensor.csv`; USL and PSL given full treatment
  with their synergistic effect on the VVUQ process; the fourteen external
  standards and two clinical baselines and the ten gate thresholds; the Draft
  Statutory Text as Sections 1 to 9 with the (a)(1)(i) hierarchy and an enacting
  clause; and the federal laws (42 U.S.C. for Title VI and the ADA) and the four
  state laws (NY A9149, TX SB 1822, CA SB 1120, FL HB 527).
- `full-paper.zip` (the Overleaf-ready LaTeX bundle), `prompt-full-paper.md`, and
  `output-full-paper.md`.

### Changed
- Top-level `README.md`: release badge to v1.4.0, a v1.4.0 summary above the prior
  summary, a VVUQ-03 Full Paper section with an ASCII process diagram and a
  table-of-contents entry, and the repository structure tree with a VVUQ-03
  full-paper block.
- `releases.md` (v1.4.0 notes) and `CITATION.cff` (version 1.4.0).
- @kevinkawchak updated README file DOI badge locations, created the instruct-paper file architecture, and populated instruct-paper with corresponding prompt and three outputs for cancer-automated/tree/main/papers/VVUQ-03 on 2026-05-29.
- @kevinkawchak updated the final bill LaTeX source files and README on cancer-automated/tree/main/papers/VVUQ-03/final-paper; and also included the bill link for main/README.md on 2026-05-30.

## [1.3.0] - 2026-05-30

### Added
- `papers/VVUQ-03/draft-paper/`: a compilable single-column LaTeX draft scaffold
  for the *VVUQ Physical AI Oncology Trial Bill* (Draft 1.0), a proposed United
  States bill requiring an automated VVUQ verification process to clear
  robot-patient interaction code before that code is generated or executed in a
  Physical AI oncology clinical trial. Built from the VVUQ-03 template-paper (the
  21 CFR Part 312 adaptation) with the direct CFR context removed and new section
  names created, authored by Claude Code Opus 4.8 (1M context) Max running
  autonomously across 21 commits in a single pull request, one file per commit
  pushed to GitHub in real time, then a second-to-last error-fix and consolidation
  commit and a final repository-updates commit.
- `main.tex` (cover page kept verbatim to spec, table of contents, fifteen section
  `\input` lines, navy clickable hyperlinks, ragged-right tabularx column types,
  and the global production and formatting directives; no images), `new_paper.sty`
  (Palatino body with the navy accent carried from the prior template), and
  `references.bib` (the final 60-entry `ieeetr` bibliography with DOIs and
  clickable URLs and no `howpublished` field).
- Fifteen `sections/*.tex` files, each a bracketed processing instruction naming
  the exact source files: abstract, policy_memo, problem_statement, definitions,
  findings, algorithm_documentation, attestations_compliance, prior_law,
  supporting_documentation, statutory_text, implementation_enforcement,
  section_by_section, limitations_future, conclusions, and back_matter.
- The four required main points as their own sections, with Algorithm
  Documentation featuring the 1790-line four-entrant `comparison.json` and the
  1001-row non-repetitive `sample_h2_sensor.csv`; USL and PSL given full treatment
  with their synergistic effect on the VVUQ process; the fourteen external
  standards and two clinical baselines from VVUQ-02; and the federal laws (with the
  prompt's 26 U.S.C. corrected to 42 U.S.C. for Title VI and the ADA) and the four
  state laws (NY A9149, TX SB 1822, CA SB 1120, FL HB 527).
- `draft-paper.zip` (the Overleaf-ready LaTeX bundle), `prompt-draft-paper.md`, and
  `output-draft-paper.md`.

### Changed
- Top-level `README.md`: release badge to v1.3.0, a v1.3.0 summary above the prior
  summary, a VVUQ-03 Draft Paper section with an ASCII process diagram and a
  table-of-contents entry, and the repository structure tree with a VVUQ-03 block.
- `releases.md` (v1.3.0 notes) and `CITATION.cff` (version 1.3.0).

## [1.2.0] - 2026-05-27

### Added
- `papers/VVUQ-02/full-paper/`: the full, Overleaf-compilable manuscript for *10
  Mobile Pancreatic Cancer Unitree H2 Surgical Humanoids: VVUQ Processing Priority
  over Code Generation*, processed from the v1.1.0 draft scaffold by Claude Code
  Opus 4.7 (1M context) Max running autonomously in a managed cloud container
  across 14 commits in a single pull request, one file per commit pushed to GitHub
  in real time, then a second-to-last error-fix and consolidation commit and a
  final repository-updates commit. The draft-paper directory is left untouched.
- `main.tex` (preamble, title page, abstract, table of contents, and section
  `\input` wiring with a ragged-right tabularx column type), `new_paper.sty` (the
  Palatino and navy style carried from the draft), `references.bib` (the final
  41-entry `ieeetr` bibliography), and eight `sections/*.tex` files (abstract,
  introduction, methods, results, discussion, limitations and future work,
  conclusions, and back matter) with finished publication prose and 13 left-aligned
  tables set to the body text width.
- Grounded assurance evidence throughout: 172 of 172 tests with 64 in the ten-gate
  suite, the five ACCEPT, BLOCK, and ESCALATE decision cases, the ten gate
  thresholds, the 32 of 32 sweep at composite mean near 93.6, the four-entrant
  tournament leaderboard (the mobile humanoid second to the eight-arm PancreSpeed
  cart by under half a composite point), the 1000-row non-repetitive sensor stream,
  and byte-for-byte determinism from seed 20260525.
- Five figure floats kept with `\autoref` targets and `\IfFileExists` placeholders
  (`fig:wheel`, `fig:forest`, `fig:bands`, `fig:matrix`, `fig:cost`); the
  `full-paper.zip` Overleaf bundle; the `Images/` placeholder; and
  `prompt-full-paper.md` and `output-full-paper.md`.

### Changed
- Top-level `README.md`: release badge to v1.2.0, a v1.2.0 summary above the prior
  summary, a VVUQ-02 Full Paper section with an ASCII process diagram and a table
  of contents entry, and the repository structure tree (the full-paper directory
  expanded and final-paper kept as a placeholder).
- `releases.md` (v1.2.0 release notes) and `CITATION.cff` (version 1.2.0).

## [1.1.0] - 2026-05-27

### Added
- `papers/VVUQ-02/draft-paper/`: a compilable single column LaTeX draft scaffold
  for *10 Mobile Pancreatic Cancer Unitree H2 Surgical Humanoids: VVUQ Processing
  Priority over Code Generation*, built from the Template_04 regulatory and FDA
  submission scaffold and authored by Claude Code Opus 4.7 (1M context) Max running
  autonomously in a managed cloud container across 14 commits in a single pull
  request, one file per commit pushed to GitHub in real time, then a
  second-to-last error-fix and consolidation commit and a final repository-updates
  commit.
- `main.tex` (title page, table of contents, section `\input` wiring, and the
  global production and formatting directives), `new_paper.sty` (the Palatino and
  navy style carried from the template family), and eight `sections/*.tex` files
  (abstract, introduction, methods, results, discussion, limitations and future
  work, conclusions, and back matter), each a bracketed processing instruction that
  names the exact codegen, execution, inputs, and imagegen files a future pass must
  read and synthesise into publication-quality prose. No section is processed here.
- `references.bib`: a final, polished bibliography of 41 entries with the DOI
  string and its clickable resolver URL in every `note` field, the external
  standards and regulations well represented (ASME V&V 40-2018, NASA-STD-7009A,
  IEC 80601-2-77, IEC 60601-1, ISO/TS 15066, ISO 13482, ISO 10218-1, ISO 9283,
  IEC 62304, ISO 14971, ISO 13849-1, UL 4600, IEEE 7009, FDA CM&S credibility, FDA
  real-time clinical trials, and ICH E6(R3)), GitHub and Zenodo links once each for
  repositories, no `howpublished` field, and both the paper and repository DOIs
  clickable.
- Five figure floats placed with one-line captions, space and dash and underscore
  free labels, and `\autoref` usage: `fig:wheel` (Methods), `fig:forest` and
  `fig:bands` (Results), and `fig:matrix` and `fig:cost` (Discussion). Each wraps
  the supplied figure code in `\IfFileExists` so the draft compiles before the
  rendered PNGs are dropped into `Images/`.
- `papers/VVUQ-02/draft-paper/README.md` with DOI badges, the lineage and file
  layout ASCII diagrams, the section to source-file map, the figure table, the
  senior-author formatting rules, and the references policy; `draft-paper.zip` (the
  Overleaf-ready LaTeX bundle); and `prompt-draft-paper.md` and
  `output-draft-paper.md`.

### Changed
- Top-level `README.md`: release badge to v1.1.0, a v1.1.0 summary above the prior
  summary, a VVUQ-02 Draft Paper section with an ASCII flow diagram and a table of
  contents entry, and the repository structure tree (the draft-paper directory
  expanded to the scaffold file set).
- `releases.md` (v1.1.0 release notes), `CITATION.cff` (version 1.1.0).

## [1.0.0] - 2026-05-26

### Added
- `papers/VVUQ-02/imagegen/`: the 15 rendered figures, authored by Claude Code Opus
  4.7 (1M context) Max running autonomously in a managed cloud container across 15
  commits in a single pull request, one figure per commit pushed to GitHub in real
  time, then a 16th commit for the error-fix and consistency pass and a 17th commit
  for the repository updates. Each figure is one self-contained `NN-name.py`
  matplotlib script (the generated code) and one `NN-name.png` (the execution
  output), portrait `figsize=(8.5, 11)` at 300 dpi (2550 by 3300 pixels), white
  background only with no dark mode, rendering its v0.9.0 specification with no
  manual positioning.
- 15 distinct chart families rendered from the codegen (v0.7.0) and execution
  (v0.8.0) records: platform pipeline flow, gate decision funnel, ten-gate threshold
  forest, gate to standard binding matrix, clinical and regulatory standards wheel,
  172-test coverage treemap, validation parity scatter, sweep composite strip plot,
  composite weighting waterfall, four-entrant comparison box plot, sensor stream
  safety bands, eight-phase Whipple swimmer, assurance cost assessment, value
  proposition matrix, and platform mind map. Six satisfy the required-data brief.
- A comprehensive `imagegen/README.md` with DOI and status badges, the conventions,
  the 15-figure index, the data-availability mapping, repository-structure and
  spec-to-script-to-PNG ASCII diagrams, the reproduction note, and the verification
  pass.
- `prompt-imagegen.md` (the generating prompt, verbatim) and `output-imagegen.md`
  (the narrative markdown output of this run).

### Changed
- Top-level `README.md`: release badge to v1.0.0, a v1.0.0 summary above the prior
  summary, a VVUQ-02 Imagegen section with an ASCII flow diagram and a table of
  contents entry, the repository structure tree (the imagegen directory expanded to
  the rendered figure set), and the cross-references in the VVUQ-02 image
  instructions section.
- `releases.md` (v1.0.0 release notes), this `CHANGELOG.md` (v1.0.0), and
  `CITATION.cff` (v1.0.0).
- @kevinkawchak relocated images from cancer-automated/tree/main/papers/VVUQ-02/imagegen to Google Drive, reducing repository size from 9MB to 1MB on 2026-05-26.

### Notes
- Every script is pure `matplotlib` plus `numpy`, sets `matplotlib.use("Agg")`, and
  passes `ruff check` and `ruff format --check` repository-wide, so the
  `lint-and-format` CI job stays green across Python 3.10, 3.11, and 3.12; the
  `test` and `validate-scripts` jobs do not import `imagegen/`. Re-rendering is
  deterministic (byte-identical PNGs; any jitter is seeded). The arithmetic
  reconciles (treemap 172, weights 1.00, swimmer 60 s, appearances 256, sweep
  min/max/mean). No images, Mermaid diagrams, or colored images are added to any
  Markdown. The v0.9.0 image instruction files are not modified, and only
  `kevinkawchak/cancer-automated` was edited.

## [0.9.0] - 2026-05-26

### Added
- `papers/VVUQ-02/image-instruct/`: 15 comprehensive image instructions plus a
  master README, authored by Claude Code Opus 4.7 (1M context) Max running
  autonomously in a managed cloud container across 15 commits in a single pull
  request, one figure specification per commit pushed to GitHub in real time. The
  set specifies, ahead of any rendering, how a future agent builds 15 portrait,
  full-size, 300 dpi figures grounded in the codegen (v0.7.0) and execution
  (v0.8.0) records. Instructions only; no script and no image is rendered here.
- 15 distinct chart families chosen from a 20-family menu for best data
  availability and relevance (no family reused, and no basic bar, pie, or line
  chart): workflow pipeline flow, gate decision funnel, ten-gate threshold forest,
  gate to standard binding matrix, clinical and regulatory standards wheel,
  172-test coverage treemap, validation parity scatter, sweep composite strip plot,
  composite weighting waterfall, four-entrant comparison box plot, sensor stream
  safety bands, eight-phase Whipple swimmer, assurance cost assessment, value
  proposition matrix, and platform mind map.
- Six figures satisfy the required-data brief: the 172 tests (treemap), the
  external-standards anchoring (binding matrix), the 10 gates and thresholds
  (forest), the clinical and regulatory corpus (wheel), the featured 1000-row H2
  sensor stream (line with bands), and the four-entrant comparison featuring the
  second-place mobile humanoid (box plot).
- `prompt-image-instruct.md` (the generating prompt, verbatim) and
  `output-image-instruct.md` (the narrative markdown output of this run).
- A master `README.md` with DOI and status badges, the shared page frame, palette,
  font, symbol, and dash conventions, the processing model for Claude Code Opus 4.7
  (1M) Max, the data-availability mapping, repository-structure ASCII diagrams, the
  file-generation outcomes as a basis for a future technical paper, and a
  consistency and error-fix pass.

### Changed
- Top-level `README.md`: release badge to v0.9.0, a v0.9.0 summary above the prior
  summary, a VVUQ-02 Image Instructions section with an ASCII flow diagram and a
  table of contents entry, the repository structure tree (the image-instruct
  directory expanded to the 15 specifications), the corrected forward references in
  the VVUQ-02 codegen section, and the citation version.
- `releases.md` (v0.9.0 release notes), this `CHANGELOG.md` (v0.9.0), and
  `CITATION.cff` (v0.9.0).

### Notes
- The image-instruct pull request adds only Markdown, so it carries no Python or
  YAML and cannot introduce a `ruff` or `yamllint` failure; the `lint-and-format`,
  `validate-scripts`, and `test` CI jobs stay green across Python 3.10, 3.11, and
  3.12. No images, Mermaid diagrams, or colored images are added. The matplotlib
  scripts and 300 dpi PNG files are deferred to a future imagegen pull request. The
  assurance cost assessment figure uses an illustrative relative index, not
  measured dollars, with the direction grounded in the execution README. Only
  `kevinkawchak/cancer-automated` was edited.

## [0.8.0] - 2026-05-26

### Added
- `papers/VVUQ-02/execution/`: the complete run record of the
  `papers/VVUQ-02/codegen/` tree, produced by Claude Code Opus 4.7 (1M context)
  Max running autonomously in a managed cloud container across 8 commits in a
  single pull request, one large section per commit pushed to GitHub in real time.
- `01-foundation/`: the host (CPython 3.11.15 on Linux), the dependency posture,
  a byte-for-byte determinism check that reproduces the committed sensor CSV, the
  4-entrant comparison, and the 32-iteration sweep index from seed 20260525, the
  172-test suite (0 skipped, the 10-gate suite carries 64 of the 172), and the CI
  lint-and-format checks, all green.
- `02-pipeline/`: the intent to compile to act to score record across six
  behavior groups (autonomy at concordance 1.000, kinematics, perception, hands,
  balance, suturing), with a verbatim execution log.
- `03-vvuq/`: the 10-gate decision surface over five cases (10 ACCEPT nominal,
  three distinct BLOCK mechanisms, one ESCALATE at coefficient of variation
  0.163), with the captures, the nominal report, and a decisions JSON carrying
  each gate's resolved external standards.
- `04-automation/`: the 32-iteration sweep (32 of 32 clear all 10 gates,
  composite mean 93.56), the gated composite, the Zenodo L0 pointer discipline,
  and a structural analysis of the featured 1790-line four-entrant
  `comparison.json` (128 round verdicts, 100 percent caveat coverage).
- `05-humanoid-deployment/`: the 60-second 8-phase Whipple timeline, a structural
  analysis of the featured 1000-row, 27-column positional sensor stream (every
  row and every positional payload distinct, no repetition), and the three
  immediate-catastrophe safety surfaces (vascular no-fly, human collision, fault
  e-stop), each correct at the boundary.
- `prompt-execution.md` and `output-execution.md` recording the generating prompt
  verbatim and the narrative output of the execution step.

### Changed
- Top-level `README.md`: release badge to v0.8.0, a v0.8.0 summary above the prior
  summary, a VVUQ-02 Execution section with an ASCII flow diagram and a table of
  contents entry, the repository structure tree (the execution directory
  expanded), the corrected codegen test count (172), and the citation version.
- `releases.md` (v0.8.0 release notes), this `CHANGELOG.md` (v0.8.0), and
  `CITATION.cff` (v0.8.0).

### Notes
- The external standards (ASME V&V 40-2018, NASA-STD-7009A, FDA CM&S 2023, IEC
  80601-2-77, IEC 60601-1, ISO 13482, ISO/TS 15066, ISO 10218-1, ISO 9283, IEC
  62304, ISO 14971, ISO 13849-1, UL 4600, IEEE 7009) anchor the credibility of the
  run; every gate, behavior, and safety surface is traced to a published standard.
- All code ran from a scratch working directory with the codegen tree on
  `PYTHONPATH`, leaving the committed codegen tree pristine. No Python or notebook
  files were added outside the already-clean codegen tree, so the CI
  lint-and-format surface stays green across Python 3.10, 3.11, and 3.12. The
  paper template files in `papers/VVUQ-02/templates/Template_04/` were not
  processed. Only `kevinkawchak/cancer-automated` was edited.

## [0.7.0] - 2026-05-26

### Added
- `papers/VVUQ-02/codegen/`: the standalone generated codebase for 10
  humanoid-specific VVUQ gates on an autonomous Unitree H2-Surgical 1.0
  (hypothetical 2030 surgical variant) performing the 60-second 8-phase Whipple on
  patient PAT-PDAC-0001 with its own two dexterous hands. Authored by Claude Code
  Opus 4.7 (1M context) Max from `papers/VVUQ-02/instructions/output-instruct.md`
  across 11 commits in a single pull request, one set of files per commit pushed
  to GitHub in real time.
- The assurance layer (`src/vvuq/`) is held to a higher standard than code
  generation and is grounded in real-world standards: ASME V&V 40-2018 and
  NASA-STD-7009A for model credibility, IEC 80601-2-77 and IEC 60601-1 for robotic
  surgery, ISO 13482, ISO/TS 15066, ISO 10218-1, and ISO 9283 for service and
  collaborative robot safety, IEC 62304, ISO 14971, and ISO 13849-1 for software
  and risk, and UL 4600 and IEEE 7009 for autonomy and fail-safe design.
- Each of the 10 gates (handeye servo, finger force, balance, autonomous plan,
  grasp and handover, vascular no-fly, suturing, perception, human collision,
  fault and e-stop) verifies (pass fraction 1.0), validates against an independent
  reference in `data/reference/`, and quantifies uncertainty across seeded runs,
  deciding ACCEPT, BLOCK, or ESCALATE. The three immediate-catastrophe gates carry
  the tightest bounds and an extra hard predicate.
- `papers/VVUQ-02/inputs/standards/`: the real standards input corpus wired into
  the gate registry, plus clinical baselines (the 2025 Dutch cohort, the Callery
  Fistula Risk Score).
- `config/vvuq_thresholds.yaml`, `config/standards_map.yaml`, JSON Schema plus
  Protobuf plus Avro schemas, a deterministic 32-iteration Latin hypercube sweep
  (seed 20260525) where all 32 iterations clear all 10 gates, a 6-component
  composite reported only when all gates ACCEPT, a 4-entrant comparison tournament,
  and the Zenodo L0 pointer discipline.
- README placeholders for the future-use directories (`image-instruct`,
  `imagegen`, `execution`, `draft-paper`, `full-paper`, `final-paper`), plus
  `prompt-codegen.md` and `output-codegen.md` recording the generation lineage.

### Changed
- Updated the main README (release badge v0.7.0, a v0.7.0 summary above the prior
  summary, a VVUQ-02 section with an ASCII gate diagram and table of contents
  entry, the repository structure, and the citation version), this CHANGELOG, the
  releases file, and `CITATION.cff` (v0.7.0).

### Notes
- The H2-Surgical 1.0 is a clearly labeled hypothetical 2030 surgical variant;
  every value is simulation-only and paper-only, and comparisons are
  simulation-against-simulation. The codegen tree keeps `ruff check`,
  `ruff format --check`, and `yamllint` clean across Python 3.10, 3.11, and 3.12;
  its 169 tests include a 64-item 10-gate decision surface. Only
  `kevinkawchak/cancer-automated` was edited.

## [0.6.0] - 2026-05-25

### Added
- `papers/VVUQ-01/full-paper/`: the full manuscript "Two Stage VVUQ Oncology
  Clinical Trial Verification Automation Priority over Existing Generated Code",
  built from the v0.5.0 draft scaffold without modifying it, authored
  autonomously by Claude Code Opus 4.7 (1M context) Max, one commit per file and
  per section, each pushed to GitHub in real time as part of a single pull
  request. Every bracketed processing instruction in the seven body sections is
  replaced with grounded, publication grade prose, tables, and figures, targeting
  roughly 70 typeset pages, while `main.tex`, `new_paper.sty`, `references.bib`,
  `sections/references.tex`, and `sections/back_matter.tex` are carried over.
- The full paper renders the executed evidence: 51 of 51 tests across 8 modules,
  the 2.5x acceleration (30 to 12 days), the full VVUQ gate decision surface (1
  accept, 5 block, 1 escalate), triple run consensus, the lights off factory
  safety cases, and the 2030 PDAC pilot. It carries 18 tabularx tables sized to
  the body text width, 5 figures, and 29 `ieeetr` references.
- `papers/VVUQ-01/full-paper/Images/`: a guide naming the four author supplied
  figure files. Each figure environment renders a labeled placeholder slot until
  its image is present, so the project compiles in Overleaf either way.
- `papers/VVUQ-01/full-paper/full-paper.zip`: an Overleaf ready bundle of the
  LaTeX project.

### Changed
- `README.md`: release badge updated to v0.6.0, a new v0.6.0 summary added above
  the v0.5.0 summary, a VVUQ-01 full paper section and table of contents entry
  added, the repository structure now expands `papers/VVUQ-01/full-paper`, and
  the citation version was bumped.
- `releases.md`: v0.6.0 release notes added above the v0.5.0 notes.

### Notes
- This release adds the full paper only; it does not change the executable v0.1.0
  source modules or the v0.2.0 through v0.5.0 records, and it does not modify the
  draft scaffold. The additions are LaTeX, Markdown, and a zip, all outside the
  `ruff` and `yamllint` surface, so `lint-and-format` (ruff check, ruff format
  check, yamllint) stays green across Python 3.10, 3.11, and 3.12, alongside
  `validate-scripts` and `test` (51 passed, 0 skipped).
- All prose uses single dashes only; triple dashes are reserved for Markdown
  rules, table separators, and YAML document separators.

## [0.5.0] - 2026-05-25

### Added
- `papers/VVUQ-01/draft-paper/`: a complete and compilable single column LaTeX
  scaffold for the manuscript "Two Stage VVUQ Oncology Clinical Trial
  Verification Automation Priority over Existing Generated Code", authored
  autonomously by Claude Code Opus 4.7 (1M context) Max, one file per commit,
  each pushed to GitHub in real time as part of a single pull request. The
  seven body section files (`sections/abstract.tex`, `introduction.tex`,
  `methods.tex`, `results.tex`, `discussion.tex`, `limitations_future.tex`,
  `conclusions.tex`) carry bracketed processing instructions that name the
  exact repository directories and files to process for a future 70+ page
  paper. The title page (`main.tex`), style (`new_paper.sty`), bibliography
  (`references.bib`), references section (`sections/references.tex`), and back
  matter (`sections/back_matter.tex`) are final.
- `references.bib`: 29 final entries rendered with `ieeetr`. Every DOI entry
  carries its human readable DOI string and a clickable resolver URL in the
  note; repository entries carry both a GitHub and a Zenodo URL, each once,
  with no duplicate link and no `howpublished` field. Both the repository DOI
  and the paper DOI are clickable.
- `draft-paper.zip`: an Overleaf ready bundle of the LaTeX project.

### Changed
- `README.md`: release badge updated to v0.5.0, a new v0.5.0 summary added
  above the v0.4.0 summary, a VVUQ-01 draft paper section and table of contents
  entry added, the repository structure now expands
  `papers/VVUQ-01/draft-paper`, and the citation version was bumped.
- `releases.md`: v0.5.0 release notes added above the v0.4.0 notes.
- @kevinkawchak removed images from cancer-automated/tree/main/papers/VVUQ-01/imagegen subdirectories, and linked images to Google Drive to reduce repository file size from 4.7MB to 450KB on 2026-05-24.

### Notes
- This release adds a paper scaffold only; it does not change the executable
  v0.1.0 source modules or the v0.2.0 through v0.4.0 records. The additions are
  LaTeX, Markdown, and a zip, all outside the `ruff` and `yamllint` surface, so
  `lint-and-format` (ruff check, ruff format check, yamllint) stays green across
  Python 3.10, 3.11, and 3.12, alongside `validate-scripts` and `test` (51
  passed, 0 skipped).
- All prose uses single dashes only; triple dashes are reserved for Markdown
  rules, table separators, and YAML document separators.

## [0.4.0] - 2026-05-23

### Added
- `papers/VVUQ-01/imagegen/`: the rendered realization of the 10 v0.3.0 image
  instructions, authored autonomously by Claude Code Opus 4.7 (1M context) Max.
  Each numbered subdirectory holds one self contained matplotlib script
  `NN-name/NN-name.py` (the generated code) and the portrait, full page, 300 dpi
  figure `NN-name/NN-name.png` it produces (the execution output, 2550 by 3300
  pixels, white background only). A comprehensive `README.md` documents the
  rendered gallery, the generated code versus execution split, the shared page
  frame and palette, and reproduction with matplotlib.
- The 10 figures use professional chart families and avoid basic bar, pie, and
  line charts: `01-vvuq-gate-funnel` (funnel), `02-acceleration-waterfall`
  (waterfall), `03-five-methods-flowchart` (process flowchart),
  `04-vvuq-assurance-wheel` (radar wheel), `05-pdac-pilot-timeline` (Gantt),
  `06-test-coverage-treemap` (treemap), `07-lights-off-state-machine` (state
  diagram), `08-fda-cost-efficiency-bridge` (financial bridge and bullets),
  `09-value-proposition-matrix` (matrix), and `10-file-generation-sankey`
  (Sankey). Every number traces to code generation (v0.1.0) or code execution
  (v0.2.0).

### Changed
- `README.md`: release badge updated to v0.4.0, a new v0.4.0 summary added above
  the v0.3.0 summary, the figures section text diagram and closing links updated
  to reflect the rendered build, the repository structure now expands
  `papers/VVUQ-01/imagegen` with its README and the 10 figure subdirectories,
  and the citation version was bumped.
- `releases.md`: v0.4.0 release notes added above the v0.3.0 notes.
- Removed the `papers/VVUQ-01/imagegen/a.md` placeholder now that the directory
  holds the rendered scripts and figures.

### Notes
- This release renders the figures specified in v0.3.0; it does not change the
  executable v0.1.0 source modules or the v0.2.0 and v0.3.0 records. Each script
  depends only on `matplotlib` and `numpy` and renders headless via the `Agg`
  backend. Rendering requires `matplotlib`; the core CI does not install it and
  the `test` job does not import `imagegen/`, so `lint-and-format` (ruff check,
  ruff format check, yamllint) and `test` (51 passed, 0 skipped) stay green
  across Python 3.10, 3.11, and 3.12 because the scripts are ruff clean.
- All prose uses single dashes only; triple dashes are reserved for Markdown
  rules, table separators, and YAML document separators.

## [0.3.0] - 2026-05-23

### Added
- `papers/VVUQ-01/image-instruct/`: 10 comprehensive image instructions plus a
  master `README.md`, authored autonomously by Claude Code Opus 4.7 (1M context)
  Max. Each instruction is a complete, self contained specification for one
  publication ready, portrait, full page, 300 dpi figure, grounded in code
  generation (v0.1.0) and code execution (v0.2.0). The master README defines the
  processing model, the directory and file naming, the shared page frame, the
  palette and typography, the symbol and dash rules, the index, the grounding
  sources, the future imagegen workflow, and the acceptance criteria.
- The 10 instructions use professional chart families and avoid basic bar, pie,
  and line charts: `01-vvuq-gate-funnel` (funnel), `02-acceleration-waterfall`
  (waterfall), `03-five-methods-flowchart` (process flowchart), `04-vvuq-assurance-wheel`
  (radar wheel), `05-pdac-pilot-timeline` (Gantt), `06-test-coverage-treemap`
  (treemap), `07-lights-off-state-machine` (state diagram), `08-fda-cost-efficiency-bridge`
  (financial bridge and bullets), `09-value-proposition-matrix` (matrix), and
  `10-file-generation-sankey` (Sankey).

### Changed
- `README.md`: release badge updated to v0.3.0, the repository structure now
  shows `papers/VVUQ-01/image-instruct` and `papers/VVUQ-01/imagegen`, a new
  figures section with a text diagram and a table of contents entry was added,
  the citation version was bumped, and a v0.3.0 release line was added.
- `releases.md`: v0.3.0 release notes added above the v0.2.0 notes.

### Notes
- This release adds instructions only. No matplotlib script and no PNG file is
  generated yet; those are produced at a future date under
  `papers/VVUQ-01/imagegen/`, which requires `matplotlib` in the rendering
  environment. The additions are Markdown and fall outside the `ruff` and
  `yamllint` surface, so `lint-and-format` stays green across Python 3.10, 3.11,
  and 3.12, alongside `validate-scripts` and `test` (51 passed, 0 skipped).
- Prior code generation (v0.1.0) and code execution (v0.2.0) files are unchanged.
- All prose uses single dashes only; triple dashes are reserved for Markdown
  rules, table separators, and YAML document separators.

## [0.2.0] - 2026-05-23

### Added
- `papers/VVUQ-01/execution/`: the complete execution record of the v0.1.0
  codebase and the Stage 2 2030 PDAC procedure code, produced autonomously by
  Claude Code Opus 4.7 (1M context) on Python 3.11.15. Includes a comprehensive
  index `README.md` with badges, ASCII diagrams, a file-generation-outcomes
  summary, the full process narrative, limitations, and a comparison with
  conventional high-end server processing.
- `01-foundation/`: environment and dependency posture, the
  `verify_installation.py` output, the full `pytest` run (51 passed, 0 skipped
  across 8 test modules), and the `ruff` and `yamllint` static-analysis evidence.
- `02-pipeline/`: the three pipeline examples run end to end, the four generated
  artifacts (instructions, generated code, execution log, paper), and per-stage
  logs and timing. The acceleration factor is 2.5 (30 baseline to 12 automated
  days).
- `03-vvuq/`: the three vvuq examples plus the full gate decision surface across
  six cases (one accept, five block, one escalate), demonstrating the gate is
  held higher than code generation.
- `04-stage1-automation/`: the seven simulation, ingestion, chunking, and
  scheduler examples, an independent chunk-losslessness verification, and a
  documented multibyte hard-split limitation.
- `05-physical-ai-stage2/`: the two physical-ai examples, the full lights-off
  factory safety surface, and the 2030 PDAC hybrid pilot timeline (60-second
  8-arm Whipple plus six 28-day Daraxonrasib cycles, 168 regimen days).

### Changed
- `README.md`: release and contributors badges updated for v0.2.0, the
  repository structure now shows `papers/VVUQ-01/execution`, and a v0.2.0
  release line was added.

### Notes
- This release is an execution and documentation record; it does not change the
  executable v0.1.0 source modules.
- The `lint-and-format` CI workflow remains green across Python 3.10, 3.11, and
  3.12, alongside `validate-scripts` and `test`.
- All prose uses single dashes only; triple dashes are reserved for Markdown
  rules, table separators, and YAML document separators.

## [0.1.0] - 2026-05-21

### Added
- Repository foundation: `ruff.toml`, `requirements.txt`, `.gitignore`, and the
  community-health files (`CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`, `SECURITY.md`,
  `SUPPORT.md`, `CITATION.cff`).
- Continuous integration at `.github/workflows/ci.yml` with `lint-and-format`
  (ruff check, ruff format check, yamllint) across Python 3.10, 3.11, and 3.12,
  plus `validate-scripts` and `test` jobs. Pull request and issue templates.
- `pipeline/`: the daily-deliverable engine. A pure standard-library deliverable
  data model (`deliverable.py`) plus the four producing stages
  (`instruction_stage.py`, `codegen_stage.py`, `execution_stage.py`,
  `paper_stage.py`) and `orchestrator.py`, with examples and tests.
- `vvuq/`: verification, validation, and uncertainty quantification plus the
  `vvuq_gate.py` gate held to a higher standard than code generation, with
  examples and tests for the accept, block, and escalate paths.
- `simulation/`: `triple_runner.py` runs every project three times and
  `consensus.py` aggregates the runs and flags divergent metrics.
- `ingestion/`: `web_search.py` with bounded exponential-backoff retries and an
  offline fallback, and `pdf_processor.py` with a guarded backend and a 200K
  chunk estimate.
- `chunking/`: `chunker.py` autochunks under the 200K per-file cap and
  `readme_generator.py` emits a reconstruction README per chunk set.
- `scheduler/`: `commit_scheduler.py` plans an evenly spaced, non-stop commit
  cadence.
- `physical-ai/`: `lights_off_factory.py` (safety-gated autonomous batch runner)
  and `hybrid_surgery_medicine.py` (combined surgery and medicine pilot
  timeline), disabled by default.
- `configs/pipeline_config.yaml`, `configs/vvuq_thresholds.yaml`,
  `scripts/verify_installation.py`, and the `tests/` harness.
- Comprehensive `README.md` with badges, table of contents, ASCII pipeline and
  roadmap diagrams, the full repository structure, and `releases.md` with the
  v0.1.0 release notes.

### Notes
- The `lint-and-format` CI workflow is green across Python 3.10, 3.11, and 3.12.
- All prose uses single dashes only; triple dashes are reserved for Markdown
  rules, table separators, and YAML document separators.

[Unreleased]: https://github.com/kevinkawchak/cancer-automated/compare/v0.5.0...HEAD
[0.5.0]: https://github.com/kevinkawchak/cancer-automated/compare/v0.4.0...v0.5.0
[0.4.0]: https://github.com/kevinkawchak/cancer-automated/compare/v0.3.0...v0.4.0
[0.3.0]: https://github.com/kevinkawchak/cancer-automated/compare/v0.2.0...v0.3.0
[0.2.0]: https://github.com/kevinkawchak/cancer-automated/compare/v0.1.0...v0.2.0
[0.1.0]: https://github.com/kevinkawchak/cancer-automated/releases/tag/v0.1.0
