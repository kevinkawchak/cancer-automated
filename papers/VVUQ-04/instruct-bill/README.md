# VVUQ-04 instruct-bill

[![License](https://img.shields.io/badge/License-CC%20BY%204.0-yellow.svg)](https://creativecommons.org/licenses/by/4.0/)
[![Prior Bill DOI](https://img.shields.io/badge/Prior%20Bill%20DOI-10.5281%2Fzenodo.20454870-blue.svg)](https://doi.org/10.5281/zenodo.20454870)
[![Repository DOI](https://img.shields.io/badge/Repository%20DOI-10.5281%2Fzenodo.20372501-blue.svg)](https://doi.org/10.5281/zenodo.20372501)
[![National Platform DOI](https://img.shields.io/badge/National%20Platform%20DOI-10.5281%2Fzenodo.19244918-blue.svg)](https://doi.org/10.5281/zenodo.19244918)
[![Bill](https://img.shields.io/badge/Bill-H.R.%209510%20(119th%2C%202d%20Sess.)-darkblue.svg)](https://www.congress.gov/browse/119th-congress)
[![Files](https://img.shields.io/badge/Files-10%20md%20%7C%205%20bib%20%7C%20README-orange.svg)](.)
[![Data current through](https://img.shields.io/badge/Current%20through-May%2031%2C%202026-green.svg)](.)

Structured U.S. medical AI bill and law summaries that bring the prior *VVUQ
Physical AI Oncology Trial Bill* (H.R. 9510, Draft 1.0; prior bill DOI
10.5281/zenodo.20454870; source at `papers/VVUQ-03/final-paper`) up to date with
medical AI law through May 31, 2026. The set is the research head start for a
future Claude Code Opus 4.8 (1M context) Max pass that will read these files plus
the prior final paper and produce a substantially more current and relevant draft
of the bill. The next bill version will then be converted to XML, so these files
are written to be effective, machine readable, and consistently styled.

## Purpose against the four goals

| Goal | What this folder supplies |
|:--|:--|
| a. Currency | Federal, state, agency, and standards developments from 2023 to May 31, 2026 that postdate the prior bill (files 01 to 09). |
| b. Grounding | The mass-adopted, in-force law the bill cites in operative text (files 01 to 06, 09; marked operative in file 10). |
| c. Emerging influences | The 119th Congress bills and executive actions used only in the memo, appendix, testimony, or research matrix (files 07, 08; marked memo-only in file 10). |
| d. Structure and style | The structured law format, visual styling, and XML-readiness conventions (file 10, section D). |

## Repository structure

```
papers/VVUQ-04/instruct-bill/
  README.md                                  (this file)
  prompt-instruct-bill.md                    (the generating prompt, verbatim)
  output-instruct-bill.md                    (the narrative output of this step)
  01-federal-statutory-framework.md          (Title 21, 42, 29, 15 statutes)
  02-fda-ai-device-regulation.md             (PCCP, lifecycle, QMSR, credibility)
  03-onc-astp-algorithm-transparency.md      (HTI-1 DSI, source attributes, HTI-5)
  04-cms-coverage-payment-ai.md              (MA AI rule, WISeR, CPT autonomy)
  05-privacy-security-nondiscrimination.md   (HIPAA, Section 1557 / 92.210, FTC)
  06-state-medical-ai-laws.md                (CA, CO, UT, TX, IL, MD, NE, NV, NY)
  07-executive-actions-national-ai-strategy.md (EO 14179, AI Action Plan, OMB)
  08-emerging-federal-bills.md               (119th Congress, research influences)
  09-vvuq-standards-clinical-trial-oncology.md (ASME, IEC, ISO, IEEE, ICH, OCE)
  10-legal-crosswalk-and-bill-style.md       (research matrix + bill-style template)
  federal-statutes.bib                       (bib 1: 20 entries)
  federal-regulations-guidance.bib           (bib 2: 36 entries)
  state-laws.bib                             (bib 3: 20 entries)
  executive-actions-and-emerging-bills.bib   (bib 4: 25 entries)
  standards-and-literature.bib               (bib 5: 44 entries)
```

## The ten instruction files

| File | Focus | Primary bill artifact it feeds | Primary .bib |
|:--|:--|:--|:--|
| 01 | Federal statutory framework (FD&C Act, PCCP § 360e-4, CDS exclusion, HIPAA, civil rights, Medicare) | Statutory text; prior-law crosswalk | federal-statutes.bib |
| 02 | FDA AI and ML device regulation (PCCP, lifecycle draft, QMSR, computational-model credibility) | Statutory text; definitions; attestations | federal-regulations-guidance.bib |
| 03 | ONC/ASTP algorithm transparency (HTI-1 DSI, 31 source attributes, IRM, HTI-5 rollback) | Algorithm documentation; attestations | federal-regulations-guidance.bib |
| 04 | CMS coverage and payment (Medicare Advantage AI rule, WISeR, CPT autonomy taxonomy) | Human-oversight section; findings | federal-regulations-guidance.bib |
| 05 | Privacy, security, nondiscrimination (HIPAA Parts 160 and 164, Security Rule NPRM, § 92.210, FTC) | Cybersecurity and nondiscrimination sections | federal-regulations-guidance.bib |
| 06 | State medical AI laws (human-over-AI, disclosure, bias testing, high-risk frameworks) | Findings; human-oversight section | state-laws.bib |
| 07 | Executive actions and national AI strategy (EO 14179, AI Action Plan, OMB M-25-21) | Policy memo; findings | executive-actions-and-emerging-bills.bib |
| 08 | Emerging federal bills, research influences only (H.R. 238, S. 1399, H.Res. 694) | Research matrix; memo; testimony | executive-actions-and-emerging-bills.bib |
| 09 | VVUQ and robotics standards, clinical-trial and oncology law (ASME V&V 40, IEC, ISO, IEEE, ICH E6(R3)) | Gate thresholds; definitions; statutory text | standards-and-literature.bib |
| 10 | Legal crosswalk, research matrix, and bill-style template (operative versus memo; structured format) | All sections; the entry point for the next pass | standards-and-literature.bib (anchors) |

## The five bibliographies and their relationships

Each cited source appears in exactly one .bib file, and no link is duplicated
across the set, so a later merge with the prior final paper produces no duplicate
references. A markdown file may cite a key held in another file's .bib; the table
below shows each .bib file's home domain and which markdown files draw from it.

| Bibliography | Scope | Entries | Read by files |
|:--|:--|:--|:--|
| federal-statutes.bib | Acts of Congress and codified U.S. Code sections | 20 | 01 (home); 02, 04, 05, 10 (cross-reference) |
| federal-regulations-guidance.bib | FDA, ONC/ASTP, CMS, OCR, FTC rules and guidance | 36 | 02, 03, 04, 05 (home); 07 (FDA agency-AI) |
| state-laws.bib | State statutes, an insurance circular, FSMB, NCSL | 20 | 06 (home) |
| executive-actions-and-emerging-bills.bib | Executive orders, OMB, strategy, 119th Congress bills | 25 | 07, 08 (home) |
| standards-and-literature.bib | Consensus standards, reporting guidelines, clinical-trial CFR and ICH, literature, prior-bill anchors | 44 | 09, 10 (home); 02 (ASME V&V 40); 07 (NIST frameworks) |

The federal-regulations and standards bibliographies are the largest because
files 02 to 05 and file 09 are the citation-dense domains; the statute, state,
and executive bibliographies are smaller and self-contained. Total entries: 145.

## How the files correlate

```
                         +-------------------------------+
                         | 10 crosswalk + bill style     |
                         | (research matrix; entry point)|
                         +---------------+---------------+
                                         |
          consumes and organizes all files below
                                         |
   +----------------+----------------+----+-----------+----------------+
   |                |                |                |                |
   v                v                v                v                v
+------+        +------+         +------+         +------+         +------+
|  01  |  base  |  02  | impl.   |  03  | transp. |  04  | pay.    |  05  |
|stat. |------->| FDA  |-------->| ONC  |-------->| CMS  |-------->|priv. |
+------+        +------+         +------+         +------+         +------+
   |               |  \            |                |                |
   | statutes      |   \ standards | IRM + fairness | autonomy       | fairness +
   | implemented   |    v          | shared         | taxonomy       | audit shared
   | by 02-05      | +------+       |                |                |
   |               | |  09  |<------+----------------+----------------+
   |               | |std + |  binds each gate threshold to a standard
   |               | |trial |
   |               | +------+
   v               v
+------+        +------+         +------+
|  06  | state  |  07  | strategy|  08  |
|state |  human |exec  | posture |bills |  (research influences; memo only)
|laws  |  -over | EO   |-------->|119th |
+------+  -AI   +------+         +------+
```

Narrative correlations:

1. File 01 is the statutory base; files 02 through 05 are the federal rules and
   guidance that implement it. File 02 connects to file 09 because the FDA
   computational-model credibility guidance recognizes the ASME and IEC standards.
2. Files 03, 04, and 05 share a transparency, autonomy, and fairness thread: the
   HTI-1 Intervention Risk Management factors (03), the CPT autonomy taxonomy (04),
   and the § 92.210 nondiscrimination duty (05) are reused as bill provisions.
3. File 06 supplies the state human-over-AI analogues that reinforce file 04 and
   file 05; file 07 supplies the federal posture that file 08 navigates.
4. File 09 binds every gate threshold to a recognized standard and to the
   clinical-trial framework; file 10 consumes all files and sorts each authority
   into operative text or memo-only matter.

## How the next pass should use this folder

1. Read file 10 first: the research matrix tells you which authorities are
   operative and which are memo-only, and the section map tells you which files
   feed each bill section.
2. Pull operative authorities from files 01 to 06 and 09; pull framing from files
   07 and 08; never place an emerging bill or executive action in operative text.
3. Resolve every citation key against the five .bib files (each key lives in one
   file). Carry DOIs and URLs through to the new bill's references with no
   duplicate links.
4. Apply the structured law format and the visual and XML-readiness conventions in
   file 10, section D, and read the prior bill at `papers/VVUQ-03/final-paper` for
   the section structure to update.

## Formatting and citation conventions (consistent across every file)

1. The section symbol § is used for every codified reference; SS is never used.
2. Single hyphens only. No em dashes, en dashes, double dashes, or triple dashes.
3. Black body text and consistent formatting throughout; no images, only tables,
   ASCII diagrams, numbered lists, and bullet points.
4. BibTeX entries carry a bare doi field, a resolver or canonical url, and a note
   with the clickable \url{}; no howpublished field; no duplicate links.
5. Law and bill names and numbers are verified against the official source; all
   antidiscrimination citations are in Title 42 or Title 29, never Title 26.

## Data currency and verification

The summaries reflect official sources (govinfo.gov, the Federal Register,
eCFR.gov, FDA.gov, CMS.gov, HHS.gov/OCR, congress.gov, state legislature sites,
and the NCSL database) and consensus-standard publishers, current through May 31,
2026. Proposed rules (the HIPAA Security Rule NPRM and HTI-5) and draft guidances
(the January 2025 FDA AI drafts) are labeled as such and are cited only as
direction, not as operative authority. Emerging 119th Congress bills are labeled
as research influences and are excluded from operative text.

## Responsible use

This is an independent research aid, not legal advice and not an enacted law. It
is not endorsed by the FDA, CMS, HHS, ONC/ASTP, OCR, any standards body, or any
member of Congress. The prior bill it supports is a clearly labeled independent
draft. Mentions of agencies are respectful and non-presumptuous, written to
advance Physical AI oncology trials and to keep the United States first in
surgical-humanoid VVUQ with external standards for patient safety, efficacy, and
clinical-trial speed.

## License

Generated text under the Creative Commons Attribution 4.0 International License
(CC BY 4.0).
