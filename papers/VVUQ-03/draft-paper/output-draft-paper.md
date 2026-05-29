## output-draft-paper

This document records the narrative output of the VVUQ-03 draft-paper run: what
was explored, what was built, and how each requirement was met. It does not
reproduce the LaTeX source files themselves (those live alongside this file in
`papers/VVUQ-03/draft-paper/`).

### What was produced

A complete LaTeX **draft-paper** scaffold for the *VVUQ Physical AI Oncology
Trial Bill* (Draft 1.0), placed in `papers/VVUQ-03/draft-paper/`. The scaffold is
a head start, not a finished bill: every section body is a `[bracketed
instruction]` that names the exact repository files a future Claude Code Opus 4.8
(1M context) Max pass must read and synthesise into publication-quality
legislative prose. No section is processed. The references are already final, and
no images are used anywhere (tables carry the dense facts).

The deliverable is `main.tex`, `new_paper.sty`, `references.bib`, a `README.md`,
fifteen `sections/*.tex` files, `prompt-draft-paper.md`, `output-draft-paper.md`,
and a single Overleaf-ready `draft-paper.zip`.

### Research and grounding (READMEs read first)

Before writing, the relevant directory READMEs and source files were read so the
bracketed instructions name real paths and real numbers:

- `papers/VVUQ-01/final-paper/` (nine sections; the proof that an LLM-driven VVUQ
  gate, held above generation, is appropriate for code verification: 51 of 51
  tests, one ACCEPT against five BLOCK and one ESCALATE, verification fraction
  1.0).
- `papers/VVUQ-02/` (codegen, execution, and final-paper; practical VVUQ codegen
  and execution against fourteen external standards and two clinical baselines:
  172 tests with 64 in the ten-gate suite, the 1790-line four-entrant
  `comparison.json`, the 1001-row non-repetitive `sample_h2_sensor.csv`, both
  reproduced byte for byte from seed 20260525).
- `physical-ai-oncology-trials/national-platform/new_paper/final_paper/` (the USL
  robot-readiness standard, the PSL site-compliance standard, and the trial,
  sponsor, and mobile simulations).
- `papers/VVUQ-03/template-paper/` (the 21 CFR Part 312 adaptation; its cover
  page, `.sty` navy accent, and Subpart J supplied the structural model, with all
  direct CFR context removed and replaced by new section names).

### How the bill addresses the thesis

The scaffold elevates the VVUQ code-verification process above the generated code
itself and requires verification ahead of generation for any robot-patient
interaction. The instructions also develop the second half of the thesis, that
repository-based AI models synthesise VVUQ code generation and execution results
into public, reproducible documents (this bill is one) that accelerate the
legislative process.

### Section structure (one .tex per section, one commit each)

Direct template context was removed and new section names were created: Abstract
and Bill Synopsis; Policy Memorandum and Concept Paper; Problem Statement and
Current-Law Gap; Definitions and Technical Terminology; Legislative Findings and
Evidentiary Record; Algorithm Documentation Requirements; Attestations and
Compliance Statements; Prior Law References and Statutory Crosswalk; Supporting
Documentation Referenced (Not Physically Attached); Draft Statutory Text;
Implementation, Oversight, Enforcement, and Fiscal Provisions; Section-by-Section
Analysis; Limitations and Future Work; Conclusions and Effective Date; and Back
Matter with a Stakeholder Register.

### The four required main points

1. **Algorithm Documentation** is its own section, stating the documentation duty
   and demonstrating it against the VVUQ-02 records, featuring the 1790-line
   four-entrant `comparison.json` and the 1001-row non-repetitive
   `sample_h2_sensor.csv` of hand, five-finger, and arm positional data.
2. **Attestations and Compliance Statements** sets out the AI compliance statement
   and signed attestation (verification-before-generation certification, bias
   minimization, retained human review) and maps each clause to machine-checkable
   evidence (the CI checklist, the standards map, the PSL and USL gates).
3. **Prior Law References** is a federal and state statutory crosswalk.
4. **Supporting Documentation (Not Physically Attached, But Referenced)** lists the
   codegen tree, the execution records, the featured data files, the Zenodo L0
   pointer pattern, and the national-platform documentation package, each by
   stable path and resolvable DOI, per the policy guidance that executable code,
   model weights, training data sets, and repositories are referenced not filed.

### Laws incorporated and corrections made

The federal laws are cited in `references.bib`: 42 U.S.C. § 1395y (Medicare); 45
CFR Parts 160 and 164 (HIPAA); 21 CFR Parts 860 to 892 (devices); and the
antidiscrimination titles. The prompt listed the antidiscrimination laws under
"26 U.S.C."; that is the Internal Revenue Code, so the bill corrects the citation
to 42 U.S.C. § 2000d (Title VI) and 42 U.S.C. § 12101 (the ADA) and notes the
correction in the problem-statement and prior-law sections. Supporting federal
authorities (FD&C Act, PHSA, 21 CFR Part 11, and original Parts 312 and 50) are
also cited. State legislation is addressed for all four requested states: New York
A9149, Texas SB 1822 (with its filed-to-committee-substitute governance change),
California SB 1120 (the Physicians Make Decisions Act), and Florida HB 527 with
companion SB 202; the California and Florida bills were located and verified by
web search since the prompt supplied only the New York and Texas specifics. The
cover-page title was corrected from the prompt's "Bil" to "Bill."

### USL, PSL, and the External Standards

The definitions section gives USL and PSL full treatment and states how they
strengthen the VVUQ process synergistically: PSL verifies the site environment and
USL validates the robot platform, forming a dual-layer gate around the code-level
VVUQ, with USL dimensional variation read as quantified uncertainty and Phase 0
simulation validation as a pre-enrollment gate. The findings section requires a
comprehensive treatment of the fourteen external standards and two clinical
baselines from VVUQ-02 and their per-gate bindings, because that external-standard
anchoring is what makes the assurance argument defensible to a regulator.

### References policy

`references.bib` has 60 entries rendered with `ieeetr`, which prints the `note`
field, so every entry shows its DOI string and its clickable resolver URL. The two
author VVUQ studies and the six legislation and platform works were carried in
verbatim from the prompt. Repository entries carry the GitHub and the Zenodo link
once each; there is no `howpublished` field; both the paper DOI and the repository
DOIs resolve as clickable links; and no link is duplicated within an entry.

### Commit plan, CI safety, and formatting

The work was committed autonomously and pushed in real time within a single pull
request on `claude/hopeful-shannon-fIdwM`: one commit each for `README.md`,
`new_paper.sty`, `references.bib`, and `main.tex`; one commit per section file; a
second-to-last commit that validated and consolidated all files; and a final
repository-updates commit (this file, the prompt file, the zip, `releases.md`,
`CHANGELOG.md`, the main `README.md`, and `CITATION.cff`). Only
`kevinkawchak/cancer-automated` is edited. No Python or linted YAML is added, so
the `lint-and-format` CI job stays green across Python 3.10, 3.11, and 3.12
(verified locally with `ruff check` and `ruff format --check`). The formatting
directives carried throughout: left-aligned ragged-right fixed-width table columns
with `\raggedright\arraybackslash` prepended to every width, longer parent paths
at the top of tables with abbreviated leaf names, no large white bands or
right-margin overflow, no orphan or widow or one-or-two-word lines, the section
symbol § (never SS), single hyphens only, the navy Palatino styling from the prior
template, and no images.

### Limitations recorded honestly

The limitations section gives an unshortened account of what could not be run or
was approximated in the codegen and execution steps (offline LLM, web, and PDF
backends; no physics engine; a single local interpreter with cross-version
coverage on CI; the VVUQ-01 multibyte six-character loss; the self-referential
accept case and the unwired corpus), the simulation caveats (the hypothetical 2030
Unitree H2-Surgical 1.0, simulation against simulation), and this draft-paper
step's own limits (pdflatex was unavailable and compilation was not requested, so
the LaTeX was validated structurally and made compile-safe).

### Responsible use

Mentions of the FDA and other governing bodies are respectful and
non-presumptuous, written to advance the field and to keep the United States first
in surgical-humanoid VVUQ with external standards for patient safety, efficacy,
and clinical-trial speed. The bill is an independent draft, not enacted law, and is
not endorsed by any sponsor, CRO, site, IRB, regulator, or medical society, nor by
CFR, ICH, or FDA.
