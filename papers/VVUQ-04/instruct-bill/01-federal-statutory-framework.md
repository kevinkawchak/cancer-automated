# 01 - Federal Statutory Framework for Medical AI

Scope: the standing United States statutes (the U.S. Code and the Public Laws
that created them) that any Physical AI oncology trial bill must build on,
cross-reference, or amend. This file is the statutory floor for the *VVUQ
Physical AI Oncology Trial Bill* (the prior bill, designated H.R. 9510, Draft
1.0; see PRIORBILL DOI 10.5281/zenodo.20454870). Regulations and agency guidance
that implement these statutes are treated in files 02 through 05; this file holds
only Acts of Congress and their codified sections.

| Field | Value |
|:--|:--|
| File | 01 of 10 |
| Companion bibliography | federal-statutes.bib |
| Data current through | May 31, 2026 |
| Primary legal sources | govinfo.gov (Public Laws), Cornell Legal Information Institute (U.S. Code) |
| Symbol convention | section symbol § used for every codified section; SS never used |

## Role in the bill update (points a through d)

1. Point a (currency): confirms that the operative federal hooks for AI in
   medicine are the device, biologic, privacy, and civil rights statutes, plus
   the 2022 Predetermined Change Control Plan authority that did not exist when
   older device law was written.
2. Point b (grounding): supplies the mass adopted, mature statutory anchors
   (FD&C Act, HIPAA, ACA § 1557) that a regulator and a court already recognize,
   so the bill is grounded in law rather than in novel assertion.
3. Point c (emerging influences): isolates the genuine statutory gap (no general
   human-in-the-loop or automated-VVUQ mandate exists) that the emerging bills in
   file 08 would fill; that gap is the bill's reason to exist.
4. Point d (structure): the statute list here is the source for the bill's
   "Prior Law References and Statutory Crosswalk" section and for its enacting
   and amendatory clauses.

## A. Food, drug, device, and software authorities (Title 21)

| Key | Statute | Citation | Status | Substance and relevance to robot-patient VVUQ |
|:--|:--|:--|:--|:--|
| usc-fdca | Federal Food, Drug, and Cosmetic Act | 21 U.S.C. § 301 et seq. | In force (1938) | Master FDA statute for drugs, devices, biologics. A surgical or oncology robot and its control software are regulated here; the bill's VVUQ, audit, and oversight duties layer on the device authorities. |
| usc-321h | Device definition | 21 U.S.C. § 321(h) | In force | Threshold question: is robot-patient interaction software a regulated device. Redesignated (h)(1) by the Safeguarding Therapeutics Act (Pub. L. 116-304). |
| usc-360c | Classification of devices (§ 513) | 21 U.S.C. § 360c | In force | Risk-based Class I, II, III scheme. A patient-contacting oncology robot is likely Class II or III, which sets the premarket pathway and the rigor of VVUQ the bill can require. |
| usc-360k | Premarket notification, "510(k)" (§ 510(k)) | 21 U.S.C. § 360(k) | In force | Substantial-equivalence clearance for most Class II devices. Distinct from § 360k (state preemption); the bill must cite the correct subsection. |
| usc-360e | Premarket approval, "PMA" (§ 515) | 21 U.S.C. § 360e | In force | Most rigorous Class III pathway. The natural home for stringent VVUQ and human-oversight conditions on a high-risk surgical humanoid. |
| usc-360e4 | Predetermined Change Control Plans (§ 515C) | 21 U.S.C. § 360e-4 | In force (added by FDORA, 2022) | Lets FDA pre-authorize planned AI/ML device-software modifications without a new submission. The single best statutory anchor for an "automated VVUQ on every code change" rule. |
| usc-360j-o | Software and clinical decision support exclusion (§ 520(o)) | 21 U.S.C. § 360j(o) | In force (added by Cures Act § 3060) | Excludes five software categories from the device definition unless the software interprets a clinical test or device data. The bill must confirm robot-control code does not fall through this exclusion, or close the gap. |
| pl-cures | 21st Century Cures Act | Pub. L. 114-255, 130 Stat. 1033 | Enacted Dec. 13, 2016 | Source of § 3060 (software/CDS) and the real-world-evidence program (21 U.S.C. § 355g). RWE is relevant to evidence generation in Physical AI oncology trials. |

## B. Public health, biologics, and Medicare authorities (Title 42)

| Key | Statute | Citation | Status | Substance and relevance |
|:--|:--|:--|:--|:--|
| usc-phsa | Public Health Service Act | 42 U.S.C. § 201 et seq. | In force | Umbrella PHS authority (FDA biologics, NIH, human-subjects context). Cross-reference for biologic plus device trials. |
| usc-262 | Biologics licensure (PHSA § 351) | 42 U.S.C. § 262 | In force | BLA standard ("safe, pure, and potent"). Relevant where an oncology robot delivers a biologic, creating a combination-product VVUQ scope. |
| usc-1395y | Medicare "reasonable and necessary" (SSA § 1862(a)(1)(A)) | 42 U.S.C. § 1395y(a)(1)(A) | In force | Medical-necessity coverage exclusion. Even FDA-cleared Physical AI must be reasonable and necessary for Medicare payment; audit-trail evidence supports that determination (see file 04). |

## C. Privacy and security statutes

| Key | Statute | Citation | Status | Substance and relevance |
|:--|:--|:--|:--|:--|
| pl-hipaa | Health Insurance Portability and Accountability Act | Pub. L. 104-191; SSA §§ 1171-1179 | Enacted Aug. 21, 1996 | Statutory basis for the Privacy and Security Rules governing protected health information (PHI) processed by robot-patient systems and used as AI training data. |
| pl-hitech | HITECH Act (Title XIII of ARRA) | Pub. L. 111-5, §§ 13001 et seq. | Enacted Feb. 17, 2009 | Strengthened HIPAA enforcement, added breach notification (§ 13402), and extended duties to business associates such as AI vendors. Underpins the bill's audit-trail and security obligations. |

## D. Civil rights and nondiscrimination statutes

The prior bill correctly places the antidiscrimination guarantees in Title 42 (or
Title 29), never Title 26 (the Internal Revenue Code). That correction is carried
forward here.

| Key | Statute | Citation | Status | Substance and relevance |
|:--|:--|:--|:--|:--|
| usc-titlevi | Title VI, Civil Rights Act of 1964 | 42 U.S.C. § 2000d | In force | Bars race, color, or national-origin discrimination in federally funded programs. Foundational hook incorporated by ACA § 1557. |
| usc-ada | Americans with Disabilities Act | 42 U.S.C. § 12101 et seq. | Enacted 1990; amended 2008 | Disability nondiscrimination; reaches accessibility and bias of Physical AI affecting disabled patients. |
| usc-504 | Section 504, Rehabilitation Act of 1973 | 29 U.S.C. § 794 | In force | Disability nondiscrimination in federally funded programs; operationalized for AI tools by 45 CFR § 92.210 (file 05). |
| usc-gina | Genetic Information Nondiscrimination Act, Title II | 42 U.S.C. § 2000ff et seq. | Enacted 2008; eff. Nov. 21, 2009 | Bars use of genetic information in employment and insurance. Relevant when oncology-trial AI ingests genomic data. |
| usc-1557 | Affordable Care Act Section 1557 | 42 U.S.C. § 18116 | Enacted 2010; in force | Cross-cutting health-program nondiscrimination statute (incorporates Title VI, Title IX, ADEA, § 504). Statutory authority for the 45 CFR § 92.210 patient-care decision-support-tool rule, the best existing nondiscrimination anchor for the bill. |

## E. Consumer-protection backstop (non-HIPAA components)

| Key | Statute | Citation | Status | Substance and relevance |
|:--|:--|:--|:--|:--|
| usc-ftc5 | Federal Trade Commission Act § 5 | 15 U.S.C. § 45 | In force | Bars unfair or deceptive acts. Basis for FTC action against unsubstantiated AI performance and safety claims, reaching any consumer-facing Physical AI oncology component outside HIPAA. |

## Statutory layering (ASCII)

```
  Robot-patient interaction code in a Physical AI oncology trial
        |
        v
  +---------------------------------------------------------------+
  | Is it a "device"? 21 U.S.C. 321(h)   <--- 360j(o) may exclude  |
  +---------------------------------------------------------------+
        | yes
        v
  +-------------------+   classify (360c)   +------------------------+
  | Class II -> 510(k)|-------------------->| Class III -> PMA (360e)|
  | (360(k))          |                     | highest VVUQ rigor     |
  +-------------------+                     +------------------------+
        |                                            |
        +----------------> PCCP (360e-4) <-----------+
                  pre-authorized AI/ML changes; the
                  statutory home for automated VVUQ on change
        |
        v
  Cross-cutting duties that attach regardless of pathway:
   - PHI privacy and security ........ HIPAA / HITECH (Parts 160, 164)
   - Nondiscrimination ............... 1557 (18116) + Title VI + ADA + 504
   - Medicare necessity .............. 1395y(a)(1)(A)
   - Deceptive-claims backstop ....... FTC Act 5 (15 U.S.C. 45)
```

## Crosswalk to prior-bill provisions

| Prior-bill element | Anchoring statute(s) | Use in the new draft |
|:--|:--|:--|
| Verification before generation (core mandate) | § 360e-4 (PCCP); § 360c | Frame the gate as a pre-authorized change-control discipline under existing device law. |
| Documentation and attestation duties | § 360e / § 360(k) submissions; HITECH | Tie filings to recognized premarket evidence and business-associate duties. |
| Cybersecurity and audit trail | HIPAA / HITECH | Ground the hash-chained audit trail in the Security Rule lineage (detailed in file 05). |
| Nondiscrimination clause | § 18116, § 2000d, § 12101, § 794 | Replace any Title 26 mislabel with the correct Title 42 / Title 29 citations. |
| Coverage and reasonableness | § 1395y(a)(1)(A) | Connect VVUQ evidence to medical-necessity determinations (file 04). |

## Correlations to other VVUQ-04 files

1. File 02 (FDA AI device regulation) implements §§ 360c, 360(k), 360e, 360e-4,
   360j(o) through guidance and the device CFR.
2. File 03 (ONC/ASTP transparency) and file 04 (CMS payment) operationalize the
   Cures Act and the Social Security Act.
3. File 05 (privacy, security, nondiscrimination) implements HIPAA/HITECH and
   ACA § 1557 through 45 CFR Parts 164 and 92.
4. File 08 (emerging bills) targets the human-in-the-loop and AI-prescriber gaps
   left open by these statutes.
5. File 10 (crosswalk and bill style) consolidates this statutory list into the
   bill's amendatory and prior-law sections.

## Bibliography pointer

All entries in this file are carried in federal-statutes.bib under the keys shown
in the first column of each table (for example usc-fdca, usc-360e4, usc-1557).
Regulations that implement these statutes are cited from
federal-regulations-guidance.bib in files 02 through 05, so no statute URL is
duplicated across the bibliography set.
