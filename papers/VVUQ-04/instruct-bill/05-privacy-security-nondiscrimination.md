# 05 - Privacy, Security, and Nondiscrimination Rules for Medical AI

Scope: the HHS Office for Civil Rights and Federal Trade Commission rules that
govern protected health information (PHI), cybersecurity, and nondiscrimination
as applied to AI. These rules supply the bill's audit-trail lineage and its
single best in-force nondiscrimination anchor, 45 CFR § 92.210.

| Field | Value |
|:--|:--|
| File | 05 of 10 |
| Companion bibliography | federal-regulations-guidance.bib |
| Data current through | May 31, 2026 |
| Primary legal sources | federalregister.gov, ecfr.gov, hhs.gov/ocr, ftc.gov |
| Statutes implemented | HIPAA, HITECH, ACA § 1557, Title VI, ADA, § 504 (file 01) |

## Role in the bill update (points a through d)

1. Point a (currency): adds the January 2025 HIPAA Security Rule proposal and
   confirms the May 2025 compliance date for the § 92.210 AI duty.
2. Point b (grounding): the HIPAA Security Rule and § 92.210 are mass-adopted and
   directly on point for the bill's audit-trail and nondiscrimination clauses.
3. Point c (precision): a common misreading freezes all of the 1557 rule; in fact
   the § 92.210 AI duty is in force and was not stayed.
4. Point d (structure): supplies the bill's cybersecurity, audit-trail, and
   nondiscrimination provisions and their compliance language.

## A. Privacy and security of PHI

| Key | Item | Citation | Date / status | Substance for the bill |
|:--|:--|:--|:--|:--|
| cfr-hipaa-164 | HIPAA Privacy Rule and Security Rule | 45 CFR Parts 160 and 164 | In force | Govern use, disclosure, and safeguarding of PHI flowing through robot-patient systems and AI training pipelines. The Security Rule audit-control standard (§ 164.312(b)) and integrity standard (§ 164.312(c)) directly support the bill's hash-chained audit-trail mandate. |
| fr-hipaa-security-nprm | HIPAA Security Rule NPRM: To Strengthen the Cybersecurity of Electronic Protected Health Information | 90 FR 898; doc. 2024-30983 | Proposed Jan. 6, 2025; comments closed Mar. 7, 2025; not finalized as of May 31, 2026 | Would remove the addressable-versus-required distinction, and mandate multifactor authentication, encryption, network segmentation, annual compliance audits, and asset inventories. If finalized, raises the security and audit baseline the bill inherits. |

## B. Nondiscrimination in AI decision-support

| Key | Item | Citation | Date / status | Substance for the bill |
|:--|:--|:--|:--|:--|
| fr-1557-2024 | Section 1557 Final Rule: Nondiscrimination in Health Programs and Activities | 89 FR 37522; doc. 2024-08711; 45 CFR Part 92 | Published May 6, 2024; effective July 5, 2024 | Applies § 1557 nondiscrimination across covered health programs, expressly reaching AI, clinical algorithms, and predictive analytics. The parent rule for § 92.210. |
| cfr-92-210 | 45 CFR § 92.210: Nondiscrimination in the use of patient care decision support tools | 45 CFR § 92.210 | Effective July 5, 2024; identify-and-mitigate duties compliance date May 1, 2025 | Requires covered entities to make reasonable efforts to identify uses of patient-care decision support tools (including AI) that employ a protected characteristic as an input, and to mitigate the resulting discrimination risk. The core nondiscrimination anchor for the bill; in force and not stayed by the 1557 litigation. |

Precision note: the 2024 stays and nonenforcement notices reach only the rule's
extension of sex discrimination to gender identity and pregnancy-related matters.
They do not vacate the § 92.210 AI decision-support duty, which remains effective
with a May 1, 2025 compliance date. A bill that models its nondiscrimination
clause on § 92.210 stands on solid, in-force ground.

## C. Consumer-facing health AI outside HIPAA

| Key | Item | Citation | Date / status | Substance for the bill |
|:--|:--|:--|:--|:--|
| fr-ftc-hbnr | FTC Health Breach Notification Rule (2024 amendments) | 89 FR 47028; 16 CFR Part 318 | Final; effective July 29, 2024 | Extends breach-notification duties to non-HIPAA health apps and connected-device vendors. A gap-filler if a Physical AI oncology companion app sits outside HIPAA. The FTC Act § 5 backstop is in file 01. |

## How these rules wire into the gate (ASCII)

```
  Robot-patient interaction + PHI
        |
        v
  +----------------------------+      +-------------------------------+
  | HIPAA Security Rule         |      | Section 1557 / 45 CFR 92.210  |
  | 164.312(b) audit controls   |      | identify + mitigate AI bias   |
  | 164.312(c) integrity        |      | (in force, compliance 5/1/25) |
  +----------------------------+      +-------------------------------+
        |                                    |
        v                                    v
  Hash-chained VVUQ audit trail        Nondiscrimination gate
  (strengthened if the 2025 NPRM       (fairness factor shared with
   is finalized: MFA, encryption,       HTI-1 IRM, file 03)
   annual audits, asset inventory)
        |
        v
  Outside HIPAA: FTC Health Breach Notification Rule + FTC Act 5 backstop
```

## Crosswalk to prior-bill provisions

| Prior-bill element | Privacy or civil-rights anchor | Use in the new draft |
|:--|:--|:--|
| Cybersecurity and audit trail | cfr-hipaa-164; fr-hipaa-security-nprm | Ground the audit trail in § 164.312(b) and (c); note the pending NPRM uplift. |
| Nondiscrimination clause | cfr-92-210; fr-1557-2024 | Adopt the identify-and-mitigate duty and cite the in-force § 92.210. |
| Human oversight | cfr-92-210 mitigation duty | Pair mitigation with the human-decision rule from file 04. |
| Consumer-app coverage | fr-ftc-hbnr | Extend breach duties to any non-HIPAA companion component. |

## Correlations to other VVUQ-04 files

1. File 01 supplies the HIPAA, HITECH, ACA § 1557, Title VI, ADA, and § 504 statutes these rules implement.
2. File 03 (ONC) shares the fairness, security, and privacy factors through the HTI-1 IRM list.
3. File 04 (CMS) provides the prior-authorization audit and transparency rails the audit trail aligns with.
4. File 06 (state law) shows parallel state bias-testing and audit requirements (for example California SB 1120, Colorado SB 21-169).
5. File 10 (crosswalk) consolidates these into the bill's cybersecurity and nondiscrimination sections.

## Bibliography pointer

The HIPAA rules, the Security Rule NPRM, the Section 1557 rule and § 92.210, and
the FTC Health Breach Notification Rule are carried in
federal-regulations-guidance.bib under cfr-hipaa-164, fr-hipaa-security-nprm,
fr-1557-2024, cfr-92-210, and fr-ftc-hbnr. The underlying statutes (pl-hipaa,
pl-hitech, usc-1557, usc-titlevi, usc-ada, usc-504, usc-ftc5) are in
federal-statutes.bib, referenced but not duplicated here.
