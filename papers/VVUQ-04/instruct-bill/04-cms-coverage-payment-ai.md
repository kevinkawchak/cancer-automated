# 04 - CMS Coverage, Coding, and Payment for Medical AI

Scope: how the Centers for Medicare and Medicaid Services (CMS) and the American
Medical Association coding system treat AI and algorithm-based services. The CMS
Medicare Advantage rule and the WISeR model are the strongest federal precedents
for the bill's human-over-AI oversight principle, and the CPT autonomy taxonomy
is a ready-made graduated-autonomy structure for the gate.

| Field | Value |
|:--|:--|
| File | 04 of 10 |
| Companion bibliography | federal-regulations-guidance.bib |
| Data current through | May 31, 2026 |
| Primary legal sources | federalregister.gov, cms.gov, ecfr.gov; AMA CPT for coding |
| Statute implemented | Social Security Act / Medicare (42 U.S.C. § 1395y), file 01 |

## Role in the bill update (points a through d)

1. Point a (currency): adds the 2024 to 2026 CMS actions (the prior-authorization
   rule, the Medicare Advantage AI guardrail, the WISeR model, the CY2026 fee
   schedule) and the March 2026 CPT taxonomy revision.
2. Point b (grounding): the Medicare Advantage rule and its FAQ are mass-adopted,
   litigated, and crisp statements that AI may assist but a human must decide.
3. Point c (gap): payment for autonomous AI is real but methodologically
   unsettled, which the bill's documentation can help resolve.
4. Point d (structure): the assistive, augmentative, autonomous tiers give the
   bill a graduated-autonomy spine for tying VVUQ rigor to autonomy level.

## A. The human-over-AI precedents

| Key | Item | Citation | Date / status | Substance for the bill |
|:--|:--|:--|:--|:--|
| cms-4201-ma | Medicare Advantage and Part D final rule, AI and algorithm guardrail | 88 FR 22120; doc. 2023-07115; 42 CFR § 422.101(c) | Published Apr. 12, 2023; applicable for coverage beginning Jan. 1, 2024 | An MA plan may use AI to assist a coverage decision, but an adverse determination must rest on the individual patient's circumstances; an algorithm keyed to a population dataset cannot alone justify a denial. The leading federal human-judgment-over-AI rule. |
| cms-ma-faq-2024 | CMS FAQ on MA use of AI in utilization management | CMS FAQ memo | Released Feb. 6, 2024 | Reinforces that plans cannot fully delegate medical-necessity decisions to AI; an algorithm using a larger data set instead of the individual record is non-compliant. Crisp statutory-style language the bill can mirror for non-delegation. |
| cms-wiser | WISeR Model (Wasteful and Inappropriate Service Reduction) | CMS Innovation Center model (Request for Applications, not a Federal Register rule) | Six-year model, Jan. 1, 2026 to Dec. 31, 2031; six states (AZ, NJ, OH, OK, TX, WA) | First at-scale AI prior authorization in traditional Medicare: AI screens requests, but all non-affirmation (denial) recommendations must be made by licensed clinicians applying standardized, transparent, evidence-based criteria, with appeal rights preserved. The cleanest automated-screen plus mandatory-licensed-review architecture to model the gate on. |

## B. The CPT autonomy taxonomy as the gate's autonomy spine

| Key | Item | Date / status | Substance for the bill |
|:--|:--|:--|:--|
| cpt-appendix-s | AMA CPT Appendix S: AI taxonomy (assistive, augmentative, autonomous) | Effective Jan. 1, 2022; substantially revised Mar. 26, 2026 | Classifies AI services by autonomy and required human involvement. The March 2026 revision adds the type of evidence needed to justify each category, echoing validation-evidence requirements. |
| cms-pfs-2026 | CY2026 Physician Fee Schedule final rule (CMS-1832-F), including CPT 92229 autonomous AI payment | FR doc. 2025-19787; published Nov. 5, 2025 | CPT 92229 (autonomous AI diabetic-retinopathy analysis) shows Medicare will pay directly for autonomous AI output. CMS solicited comment on how to value SaaS and AI tools and how to credit physician work interpreting AI outputs, signaling an unsettled payment methodology. |

```
  CPT Appendix S tier      Human role                 Bill VVUQ rigor (graduated)
  --------------------      -----------------------    ---------------------------
  Assistive            ->   physician interprets   ->  baseline VVUQ + disclosure
  Augmentative         ->   physician interprets   ->  intermediate VVUQ + review
  Autonomous           ->   physician acts on it   ->  maximal VVUQ + ex ante gate
                            (or robot executes)        + continuous re-run
```

The robot-patient interaction code in a Physical AI oncology trial sits at the
autonomous end, so it draws the strictest VVUQ and human-oversight tier.

## C. The payment and prior-authorization rails

| Key | Item | Citation | Date / status | Substance for the bill |
|:--|:--|:--|:--|:--|
| cms-0057-prior-auth | Interoperability and Prior Authorization final rule (CMS-0057-F) | 89 FR 8758; doc. 2024-00895 | Published Feb. 8, 2024; operational provisions effective Jan. 1, 2026; FHIR Prior Authorization API by Jan. 1, 2027 | Requires payers to build FHIR-based prior-authorization APIs, send decision reasons, and report metrics. Natural attachment points for VVUQ audit logging and transparency. |
| cms-ipps-2026 | FY2026 IPPS final rule, New Technology Add-on Payment (NTAP) for AI tools | FR doc. 2025-14681 | Published Aug. 4, 2025; effective Oct. 1, 2025 | NTAP pays on top of the MS-DRG for new technologies, including AI diagnostic and monitoring tools; a new cost-criterion transparency requirement begins FY2027. The inpatient channel by which a validated Physical AI technology could earn incremental payment. |

## Crosswalk to prior-bill provisions

| Prior-bill element | CMS anchor | Use in the new draft |
|:--|:--|:--|
| Human oversight and escalation | cms-4201-ma; cms-ma-faq-2024; cms-wiser | Codify that AI may inform but a qualified human decides, on individual facts. |
| Graduated VVUQ by autonomy | cpt-appendix-s | Tie gate rigor and human-review intensity to the autonomy tier. |
| Medicare necessity and coverage | usc-1395y (file 01); cms-pfs-2026 | Connect VVUQ evidence to reasonable-and-necessary determinations and payment. |
| Audit trail and transparency | cms-0057-prior-auth | Align the audit trail with the prior-authorization decision-reason and metrics duties. |

## Correlations to other VVUQ-04 files

1. File 01 supplies the Medicare necessity statute (§ 1395y) CMS implements.
2. File 03 (ONC) pairs HTI-4 electronic prior authorization with CMS-0057-F.
3. File 05 (privacy and nondiscrimination) supplies the security and fairness duties that audit logging must satisfy.
4. File 08 (emerging bills) covers the prior-authorization bills (for example H.R. 6361, S. 1816) reacting to AI in coverage.
5. File 10 (crosswalk) folds the autonomy taxonomy and the human-decision rule into the bill's oversight and enforcement sections.

## Bibliography pointer

The CMS rules, the WISeR model, the CPT taxonomy, and the fee-schedule and IPPS
rules are carried in federal-regulations-guidance.bib under cms-4201-ma,
cms-ma-faq-2024, cms-wiser, cpt-appendix-s, cms-pfs-2026, cms-0057-prior-auth,
and cms-ipps-2026. The Medicare necessity statute is in federal-statutes.bib
(usc-1395y), referenced but not duplicated here.
