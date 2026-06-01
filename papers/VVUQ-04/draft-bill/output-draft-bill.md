## output-draft-bill

This step produced `papers/VVUQ-04/draft-bill`, a LaTeX **draft amendment** to the
**Federal Food, Drug, and Cosmetic Act** that recasts the prior *VVUQ Physical AI
Oncology Trial Bill* (H.R. 9510) into a properly targeted amendment. The output is
an amendment **scaffold with bracketed DRAFTING INSTRUCTIONS**, not a finished
bill: under every part it names the exact repository files a future Claude Code
Opus 4.8 (1M context) Max pass must process to produce the publication-quality
amendment. Below is the narrative of what was built and why.

### 1. The amendment target (the key correction)

Per the amendment-drafting instructions, the correct target is **not** "Public
Law 119-93, Title 21." Public Law 119-93 is the public law *through which* Title
21 is current; it is not itself the law being changed. The substantive device
authorities live in the **Federal Food, Drug, and Cosmetic Act**, codified in
Title 21. The draft therefore amends the Federal Food, Drug, and Cosmetic Act and
cites each affected provision by its `21 U.S.C. §` number, naming Public Law
119-93 only as the currency point of the reproduced existing law. This correction
is stated in `main.tex`, the `README.md`, and the bracketed instructions, and it
is the single most important structural decision of the draft.

### 2. The structured amendment format

`main.tex` lays out the exact congressional amendment structure required to be
accepted as an amendment, with a draftbox under each part:

- Bill caption (119th Congress, 2d Session, H. R. ____), the long title in the
  "To amend the Federal Food, Drug, and Cosmetic Act to ... and for other
  purposes." form, the referral to the Committee on Energy and Commerce, the
  "A BILL" head, and the enacting clause.
- **SECTION 1. SHORT TITLE; TABLE OF CONTENTS.** retains the prior short title,
  "Verification Before Generation in Physical AI Oncology Trials Act of 2026."
- **SEC. 2. FINDINGS.** the one operative location where research-influence
  material may appear, framed strictly as findings of fact.
- **SEC. 3. AMENDMENT TO THE FEDERAL FOOD, DRUG, AND COSMETIC ACT.** with (a) In
  General (the new section), (b) Conforming Amendments, (c) Clerical Amendment,
  (d) Rule of Construction, and (e) Effective Date; Implementation Deadline;
  Transition Rule.
- **SEC. 4. COMPARATIVE PRINT; CHANGES IN EXISTING LAW.** which wires in the 11
  reproduced section files and renders the marked changes with the
  `[strike: ...]` and `[insert: ...]` convention.
- **Appendix A. Research Influence Matrix (Non-Operative)** and an authorship,
  notices, and provenance block.

### 3. The new operative section

The operative mechanism is a **new section 515D of the Act (21 U.S.C. §
360e-5)**, "Verification before generation of robot-patient interaction code in
Physical AI oncology investigations," inserted immediately after the
predetermined change control plan authority (§ 515C; § 360e-4). The draftbox in
`main.tex` directs the next pass to convert the prior bill's nine operative
sections in `papers/VVUQ-03/final-paper/sections/statutory_text.tex` into the
subsections of § 360e-5 (requirement; order of operations; gate thresholds;
readiness gates; documentation and attestation; cybersecurity, human oversight,
and lifecycle; nondiscrimination; regulations; definitions; rule of
construction), anchoring each duty to in-force authority.

### 4. The conforming amendments (one section file each)

Each of the 11 reproduced Title 21 sections keeps its original statutory text and
adds a draftbox naming the exact instruct-bill and final-paper files, the
amendatory action, and the comparative-print markers:

| Section | Conforming amendment |
|:--|:--|
| § 321(h) | Confirm a Physical AI system / robot-control software is a device, not removed by § 360j(o). |
| § 331 | Add the prohibited act of generating or executing code without a cleared § 360e-5 record. |
| § 351 | Deem such a device adulterated when used without a cleared verification record (QMSR tie). |
| § 355g | Extend the real-world-evidence program to recognize VVUQ records for device oncology trials. |
| § 360(k) | A § 360e-5 and PCCP-consistent change needs no new 510(k) notification (kept distinct from § 360k). |
| § 360c | Add special controls graduated by the assistive/augmentative/autonomous taxonomy. |
| § 360e | Require the verification record and gate evidence in a PMA application. |
| § 360e-4 | Keystone: require an automated verification-before-change protocol in a PCCP. |
| § 360j(o) | Confirm autonomous robot-control software is not within the CDS exclusion. |
| § 360k | Savings clause preserving non-conflicting state human-in-the-loop and audit law. |
| § 301 | Add a Short Title of 2026 Amendment note; the Act citation anchor. |

### 5. The four goals

- **(a) Up to date:** the instructions pull from `instruct-bill` files 01-05 and
  09 (FDA PCCP final guidance, QMSR effective Feb. 2, 2026, 45 CFR § 92.210, the
  CMS Medicare Advantage AI guardrail, the CPT autonomy taxonomy).
- **(b) Grounded:** every operative duty resolves to an in-force statute, rule,
  or recognized standard via a key in `references.bib`.
- **(c) Research influences only:** the 119th Congress emerging bills and the
  executive actions feed the findings, a memo, testimony, or the non-operative
  Research Influence Matrix appendix, never the operative text.
- **(d) Streamlined:** the document follows the structured amendment format end
  to end.

### 6. The instruction mechanism and formatting

The bracketed instructions are carried in a set-off `draftbox` environment
(defined in `usctitle.sty`) with `\dstep` directives, visually distinct from
statutory text and meant to be deleted as each part is drafted. Formatting
hardening is centralized: `RaggedRight` body for even interword spacing and no
right-margin overflow, maximal widow and orphan penalties so no single line is
stranded, single hyphens only (no em or double dashes), the § symbol for every
codified reference, and a left-aligned ragged-right table column type.

### 7. Process and deliverables

The work was committed autonomously, one file per commit, pushed to GitHub in
real time within a single pull request: `main.tex`, then `usctitle.sty`, then
`references.bib`, then `README.md`, then the 11 section files, then a
second-to-last commit fixing all errors across every file and bundling the
Overleaf-ready `draft-bill-LaTeX.zip` and `prompt-draft-bill.md`, then this final
commit performing the repository updates (main `README.md`, `releases.md`,
`CHANGELOG.md`, `CITATION.cff`) and adding this `output-draft-bill.md`. Only
`kevinkawchak/cancer-automated` was edited. The LaTeX was validated structurally
(balanced braces and `draftbox` environments, no unescaped specials outside
comments, single hyphens only, all 11 `\input` targets resolving, every macro
defined) but not compiled, per instruction; the bundle is intended to compile to
a PDF in Overleaf.

### 8. Responsible use

This is a draft amendment scaffold, not an enacted law and not legal advice. The
reproduced statutory text is a work of the United States Government and is in the
public domain; the generated framing is released under CC BY 4.0. The work is
independent and is not endorsed by the FDA, HHS, the Office of the Law Revision
Counsel, CFR, ICH, or any member of Congress, and was adapted using Claude Code
Opus 4.8 (1M context) Max.
