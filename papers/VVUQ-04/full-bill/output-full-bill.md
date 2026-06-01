## output-full-bill

This step converts the v2.2.0 `papers/VVUQ-04/draft-bill` scaffold into the
finished, Overleaf-compilable amendment in `papers/VVUQ-04/full-bill`. Every
bracketed drafting instruction in the scaffold was executed against the exact
files it named under `papers/VVUQ-04/instruct-bill` and
`papers/VVUQ-03/final-paper`; the drafting-instruction blocks were then removed.
The input `draft-bill` directory was not modified. Only
`kevinkawchak/cancer-automated` was edited.

### What was produced

The finished bill is **H. R. 9510**, the *Verification Before Generation in
Physical AI Oncology Trials Act of 2026*, an amendment to the Federal Food, Drug,
and Cosmetic Act (21 U.S.C. 301 et seq.). The operative mechanism is a new
**section 515D of the Act (21 U.S.C. 360e-5)**, inserted immediately after the
predetermined change control plan keystone (section 515C; 21 U.S.C. 360e-4), plus
ten conforming amendments and a focused comparative print of the changes in
existing law. The bundle is `full-bill-LaTeX.zip` and compiles in Overleaf with
pdfLaTeX.

### Structure of the bill (main.tex)

- **Caption page.** The bill caption (119th Congress, 2d Session, H. R. 9510),
  the long title, the House referral to the Committee on Energy and Commerce, the
  "A BILL" head, the long title again, and the enacting clause, followed by a
  brief, clearly non-operative cover-page note recording that the measure was
  prepared with the assistance of an autonomous coding agent and is, to the
  drafters' knowledge, among the first bills generated at scale for Physical AI
  oncology trial implementation.
- **SECTION 1.** Short title and a one-line table of contents.
- **SECTION 2.** Fourteen findings, each tied to an in-force authority or a
  recorded study, synthesized from the prior bill's problem statement, findings,
  and policy memo and grounded in the instruct-bill law summaries. The state
  human-in-the-loop laws (California SB 1120, Illinois HB 1806, Texas HB 149,
  Maryland HB 820) appear here as findings of existing practice, not as operative
  authority.
- **SECTION 3.** Subsection (a) is the new section 515D, rendered as quoted
  statutory text in the (a)(1)(A)(i) hierarchy with subsections (a) through (j):
  the verify-before-generate requirement, the order of operations, the gate
  thresholds and decision rule with a ten-gate threshold schedule set to the body
  measure, the readiness gates (Physical AI Standard Level and Unification
  Standard Level), documentation and attestation with a hash-chained audit trail,
  cybersecurity and human oversight and lifecycle, nondiscrimination, regulations
  within 365 days, fifteen definitions, and a rule of construction. Subsection (b)
  states the ten conforming amendments; subsection (c) the clerical amendment to
  the Act's table of contents; subsection (d) the rule of construction; and
  subsection (e) the effective date, the implementation deadline, and a 180-day
  transition rule.
- **SECTION 4.** A comparative print that shows only the affected provisions of
  each of the eleven sections, marking insertions and deletions and using a row of
  asterisks for omitted unchanged matter, wired in 21 U.S.C. order through the
  eleven `sections/*.tex` files.
- **Appendix A.** A research-influence matrix that confines the emerging 119th
  Congress bills (H.R. 238, S. 1399, H.R. 6361, H.R. 5045, H.Res. 694) and the
  executive actions (EO 14179, EO 14365, OMB M-25-21, HHS AI Strategy) to a
  non-operative table, with an explicit statement that none is cited as the basis
  of an operative clause.
- **Appendix B.** A development-transparency and implementation statement covering
  the v2.0.0 to v2.3.0 pipeline, exactly what the coding agent changed in this
  version, and a plain implementation pathway for lawmakers.
- **Back matter.** Authorship, notices, and provenance, then the ieeetr
  bibliography.

### The eleven comparative-print sections

| File | Change made by H. R. 9510 |
|:--|:--|
| s301 | New "Short Title of 2026 Amendment" note |
| s321 | Device definition reaches software that generates or executes robot-patient interaction code |
| s331 | New prohibited act for violating section 515D |
| s351 | New adulteration subsection for use without a cleared section 515D record |
| s355g | Real world evidence includes section 515D records; new application subsection |
| s360 | A verification-governed change needs no new 510(k) notification |
| s360c | Special controls graduated by autonomy (assistive, augmentative, autonomous) |
| s360e | Premarket approval application must include the verification record |
| s360e-4 | Keystone: scope insertions and a new subsection binding the plan to section 515D |
| s360j | Robot-control software is not within the clinical-decision-support exclusion |
| s360k | Savings clause preserving State human-in-the-loop and audit requirements |

### Issues addressed

- **Header overlap.** The running header was carrying the full act title in the
  center and the full current-section heading on the right, which collided. The
  header now uses only short, fixed fields: the page number, the abbreviated
  title "Verification Before Generation Act of 2026," and "H. R. 9510." No two
  fields overlap.
- **The long title appearing twice on the caption page.** This is the authentic
  introduced-House-bill convention: the long title appears once in the caption
  block and once under the "A BILL" head, and both belong to the House because
  this is an H.R. measure. The wording is identical and correct; the enacting
  clause carries the standard "Senate and House of Representatives" recital. The
  duplication was kept because it is the correct congressional style, and the
  separate AI-provenance cover note was added so the page is not merely a repeat.
- **URLs running off the page.** The style file now breaks reference URLs on any
  character and adds stretchable URL spacing, so no link overflows the right
  margin in the bibliography.

### Grounding and the four goals

- **(a) Up to date.** The findings and the operative duties draw on the FDA PCCP
  final guidance, the Quality Management System Regulation (effective February 2,
  2026), 21 CFR part 11, the HIPAA Security Rule, 45 CFR 92.210, the CMS Medicare
  Advantage AI guardrail, and the CPT autonomy taxonomy.
- **(b) Grounded.** Each operative duty is anchored to an in-force statute, rule,
  or recognized standard, and each authority resolves to a BibTeX key in
  `references.bib` (79 entries; bare DOIs, single resolver URLs, no duplicate
  links).
- **(c) Research influences only.** The emerging bills and executive actions are
  used as findings context and in the Appendix A matrix, never in operative text,
  consistent with the legal-crosswalk rule that only enacted statutes, in-force
  rules, and recognized standards carry operative weight. There is no VALID Act in
  the 119th Congress, so none is cited.
- **(d) Streamlined.** The bill follows the structured amendment format: SECTION 1
  short title and contents, SEC. 2 findings, SEC. 3 the amendment, SEC. 4 the
  comparative print, with non-operative appendices kept separate.

### Formatting and fidelity

The body is set RaggedRight for even interword spacing with no right-margin
overflow; widow, orphan, and broken-line penalties are maximal so no single line
is stranded; single hyphens only are used (no en, em, double, or triple dashes);
the section symbol is used for every codified reference in the reproduced Code;
every table is a full-width left-aligned ragged-right table set to the body
measure; and there are no images, mermaid diagrams, or color figures, with links
kept black to match the printed Code.

### Process

The work was authored autonomously across sequential commits in a single pull
request, pushed to GitHub in real time: one commit each for `usctitle.sty`,
`references.bib`, `main.tex`, and the `README`; one commit per `sections/*.tex`
(eleven comparative-print sections); a second-to-last commit that fixed every
error across all files and built the Overleaf bundle; and this final
repository-updates commit. Because pdfLaTeX was not available in the container,
the LaTeX was validated structurally and made compile-safe: braces and
environments balance across `main.tex`, `usctitle.sty`, `references.bib`, and the
eleven sections; all eleven input targets resolve; every bill, US Code, and
comparative-print macro used is defined; all cite keys resolve; there is no stray
math or unescaped special character; the section symbol is the only intended
non-ASCII character; and every table is set to the body measure. The rendered PDF
and final page balancing are produced in Overleaf.

### Repository updates

The final commit updates the main `README.md` (release badge to v2.3.0, a v2.3.0
summary above the prior summary with a similar character count, a new "VVUQ-04
Full Bill (LaTeX)" section with an ASCII process diagram and a table-of-contents
entry, and the repository structure tree extended with a `VVUQ-04/full-bill`
block), `releases.md` (the v2.3.0 notes above v2.2.0 in the required format),
`CHANGELOG.md` (the [2.3.0] entry), and `CITATION.cff` (version 2.3.0). No images,
mermaid diagrams, or color were added to the main README. The additions are
LaTeX, BibTeX, Markdown, and a zip, all outside the ruff, yamllint, and pytest
surface, so the lint-and-format CI job stays green across Python 3.10, 3.11, and
3.12.

This is an independent research draft of a bill, not an enacted law and not legal
advice, and is not endorsed by the FDA, HHS, the OLRC, CFR, ICH, or any member of
Congress.
