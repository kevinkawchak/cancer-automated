# 10 - Legal Crosswalk, Research Matrix, and Bill-Style Template

Scope: the capstone file. It consolidates files 01 through 09 into a single
research matrix, maps each legal source to a bill artifact, separates
operative-text law (mass-adopted, point b) from research-influence bills
(memo and appendix only, point c), and specifies the structured law format and
visual styling (point d) that the next draft must follow for the planned XML
conversion.

| Field | Value |
|:--|:--|
| File | 10 of 10 |
| Companion bibliography | standards-and-literature.bib (prior-bill anchors); all five .bib files via cross-reference |
| Data current through | May 31, 2026 |
| Prior bill | VVUQ Physical AI Oncology Trial Bill (H.R. 9510, Draft 1.0); PRIORBILL DOI 10.5281/zenodo.20454870 |
| Prior-bill source | papers/VVUQ-03/final-paper (main.tex, references.bib, sections) |

## A. Master research matrix

Columns: domain, lead authority, file, the bill artifact it feeds, and whether it
belongs in the operative statutory text or only in supporting matter.

| Domain | Lead authority | File | Bill artifact | Placement |
|:--|:--|:--|:--|:--|
| Device and software statutes | FD&C Act; PCCP § 360e-4; CDS exclusion § 360j(o) | 01 | Statutory text; prior-law crosswalk | Operative |
| Public health and Medicare | PHSA; 42 U.S.C. § 1395y | 01 | Findings; coverage rationale | Operative |
| Civil rights | ACA § 1557; Title VI; ADA; § 504 | 01 | Nondiscrimination section | Operative |
| FDA AI device regulation | PCCP and lifecycle guidance; QMSR Part 820 | 02 | Statutory text; definitions; attestations | Operative |
| Model credibility | FDA credibility guidance; ASME V&V 40 | 02, 09 | Gate thresholds; definitions | Operative |
| Algorithm transparency | HTI-1 DSI source attributes and IRM | 03 | Algorithm Documentation; Attestations | Operative |
| Coverage and payment | CMS MA AI rule; WISeR; CPT autonomy taxonomy | 04 | Human-oversight section; findings | Operative |
| Privacy and security | HIPAA 45 CFR Part 164; Security Rule NPRM | 05 | Cybersecurity and audit-trail section | Operative |
| Nondiscrimination rule | 45 CFR § 92.210 | 05 | Nondiscrimination section | Operative |
| State law analogues | CA SB 1120; IL WOPR; CO and TX frameworks | 06 | Findings; human-oversight section | Operative (as findings) |
| Executive and strategy | EO 14179; OMB M-25-21; AI Action Plan | 07 | Policy memo; findings | Memo and findings |
| Emerging federal bills | H.R. 238; S. 1399; H.R. 2385; H.Res. 694 | 08 | Research matrix; policy memo; testimony | Memo and appendix only |
| VVUQ and robotics standards | ASME, IEC, ISO, IEEE, UL, NASA | 09 | Gate thresholds; definitions | Operative |
| Reporting guidelines | TRIPOD+AI; DECIDE-AI; SPIRIT-AI; CONSORT-AI | 09 | Supporting documentation; methodology | Appendix |
| Clinical-trial law | 21 CFR 312, 50, 56, 11; ICH E6(R3) | 09 | Statutory text; attestations | Operative |
| Oncology and autonomy evidence | OCE; Project Optimus; Yang 0-5; SRT-H | 09 | Findings | Findings |

## B. Operative law versus research influence

```
  OPERATIVE TEXT (mass-adopted, point b)        RESEARCH INFLUENCE (point c)
  -------------------------------------         ------------------------------
  FD&C Act + PCCP + QMSR                         119th Congress bills (file 08)
  HIPAA + Section 1557 / 92.210                  Executive orders + AI Action Plan
  CMS MA AI rule + WISeR architecture            HHS strategy documents
  ASME V&V 40 + IEC/ISO/IEEE standards           NIST AI RMF (framing)
  21 CFR 312/50/56/11 + ICH E6(R3)               House AI Task Force report
  State human-over-AI laws (as findings)         FDA-EMA joint AI principles (framing)
        |                                                |
        v                                                v
  Cited in Sections 1 to 9 and the                Cited in the policy memo,
  prior-law crosswalk                             findings narrative, appendix,
                                                  testimony, and research matrix
```

Rule for the next draft: an emerging bill or executive action may motivate a
finding or appear in the policy memo, but it may never be cited as the legal basis
of an operative clause. Only enacted statutes, in-force rules, and recognized
standards carry operative weight.

## C. Bill-section to file map

The prior bill (papers/VVUQ-03/final-paper) has fifteen sections. This map tells
the next pass which VVUQ-04 files feed each.

| Prior-bill section | Primary VVUQ-04 files |
|:--|:--|
| Abstract and synopsis | 10 |
| Policy memo | 07, 08, 10 |
| Problem statement and current-law gap | 01, 02, 03, 08 |
| Definitions | 02, 09 (autonomy, VVUQ, device, SaMD) |
| Findings and evidentiary record | 04, 06, 07, 09 |
| Algorithm documentation | 03 (source attributes), 02 |
| Attestations and compliance | 03 (IRM), 02 (QMSR), 09 (ICH) |
| Prior law references and crosswalk | 01, 02, 03, 04, 05, 06 |
| Supporting documentation referenced | 09 (reporting guidelines) |
| Statutory text, Sections 1 to 9 | 01, 02, 05, 09 |
| Implementation, oversight, enforcement | 04, 05, 07 |
| Section-by-section analysis | all files |
| Limitations and future work | 03 (HTI-5 rollback), 08 |
| Conclusions and effective date | 10 |
| Back matter | all .bib files |

## D. Structured law format (visual style, point d)

The next draft must read and look like a current United States bill. The required
skeleton:

1. Designation line and short title (for example, "Verification Before Generation
   in Physical AI Oncology Trials Act of 2026").
2. Enacting clause ("Be it enacted by the Senate and House of Representatives of
   the United States of America in Congress assembled,").
3. Section 1, Short title; table of contents.
4. Section 2, Findings (numbered paragraphs).
5. Section 3, Definitions (alphabetized terms).
6. Sections 4 and following, operative requirements using the standard hierarchy.
7. A final section, Effective date and authorization.

Hierarchy convention for operative text:

```
  Sec. 4.
    (a) Subsection
        (1) Paragraph
            (A) Subparagraph
                (i) Clause
                    (I) Subclause
```

Visual and typographic rules carried from the prior bill family:

1. The section symbol § is used for every codified reference (for example,
   42 U.S.C. § 1395y or ASME V&V 40-2018 § 8). SS is never used.
2. Single hyphens only. No em dashes, en dashes, double dashes, or triple dashes.
3. Tables are left-aligned and set to the body width; long facts go in tables,
   not in prose.
4. Black body text and consistent formatting throughout; no images.
5. Each operative duty cites its anchoring authority by the keys in the five .bib
   files so the next pass can resolve every reference.

XML-readiness note: because a future step converts the draft to XML, keep one
idea per clause, keep the hierarchy strictly nested, avoid inline footnotes in
operative text, and keep citations in a consistent "Title U.S.C. § number" or
"Standard number § clause" form so they map cleanly to elements.

## E. Drafting conventions checklist

1. Verify every bill number and law name against the official source before use.
2. Place antidiscrimination citations in Title 42 or Title 29, never Title 26.
3. Use § 360(k) for 510(k) and § 360k only for state preemption.
4. Mark emerging bills as research influences wherever they appear.
5. Keep each cited source in exactly one .bib file to avoid duplicate links.
6. Prefer in-force rules over proposed rules for operative clauses; cite proposed
   rules (for example the HIPAA Security Rule NPRM and HTI-5) only as direction.

## F. Prior-bill and project anchors

| Key | Item | Use |
|:--|:--|:--|
| kawchak2026vvuqbill | VVUQ Physical AI Oncology Trial Bill (PRIORBILL) | The bill being updated; DOI 10.5281/zenodo.20454870. |
| repo-cancer-automated | cancer-automated repository | Source of VVUQ-01 through VVUQ-04 records. |
| repo-physical-ai | physical-ai-oncology-trials repository | Source of the USL and PSL standards and the simulations. |
| kawchak2026vvuq01 | VVUQ-01 verification-before-generation study | Evidence that an LLM VVUQ gate is appropriate for verification. |
| kawchak2026vvuq02 | VVUQ-02 surgical-humanoid VVUQ study | The fourteen-standard, two-baseline gate evidence. |

## Correlations to other VVUQ-04 files

1. This file consumes files 01 through 09 and the five .bib files.
2. It is the entry point for the next Claude Code pass: read this matrix first,
   then pull the operative authorities from files 01 to 06 and 09, then the
   framing from files 07 and 08.
3. The README provides the file-level and .bib-level correlation diagrams that
   complement this matrix.

## Bibliography pointer

The prior-bill and project anchors are carried in standards-and-literature.bib
under kawchak2026vvuqbill, repo-cancer-automated, repo-physical-ai,
kawchak2026vvuq01, and kawchak2026vvuq02. All other keys cited in this matrix live
in their domain .bib file (federal-statutes.bib, federal-regulations-guidance.bib,
state-laws.bib, executive-actions-and-emerging-bills.bib, standards-and-literature.bib),
each source appearing once.
