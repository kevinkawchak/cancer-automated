# 07 - Executive Actions and National AI Strategy

Scope: the executive orders, Office of Management and Budget memoranda, NIST
frameworks, and HHS strategies that set the federal AI policy environment the
bill is drafted into. The current posture is deregulatory and pro-innovation,
which reframes VVUQ from a federal mandate toward a voluntary, standards-based
credibility discipline, and points toward a single national documentation
standard rather than a state patchwork.

| Field | Value |
|:--|:--|
| File | 07 of 10 |
| Companion bibliography | executive-actions-and-emerging-bills.bib (with NIST frameworks in standards-and-literature.bib) |
| Data current through | May 31, 2026 |
| Primary legal sources | federalregister.gov, govinfo.gov, whitehouse.gov, ai.gov, nist.gov, hhs.gov |
| Status of these items | Executive and sub-regulatory; not statutes |

## Role in the bill update (points a through d)

1. Point a (currency): adds the January 2025 to March 2026 executive actions and
   strategies that postdate the prior bill.
2. Point b (grounding): OMB M-25-21 supplies the cleanest surviving federal
   lifecycle (test, assess, monitor) the bill can map VVUQ onto.
3. Point c (influences): the AI Action Plan sandbox and open-results model and the
   federal preemption orders are directional signals for a memo or testimony, not
   bill text.
4. Point d (positioning): the bill is framed as counter-cyclical to deregulation
   but aligned with the lifecycle and uniform-standard themes.

## A. Executive orders

| Key | Order | Citation | Date / status | Substance for the bill |
|:--|:--|:--|:--|:--|
| eo-14179 | Removing Barriers to American Leadership in Artificial Intelligence | EO 14179; 90 FR 8741; doc. 2025-02172 | Signed Jan. 23, 2025; operative | Sets deregulatory federal AI policy and directs an AI action plan; reviews and rescinds actions taken under the revoked EO 14110. Shifts VVUQ toward a voluntary, sponsor-driven credibility differentiator. |
| eo-14110 | Safe, Secure, and Trustworthy Development and Use of AI (revoked) | EO 14110; 88 FR 75191 | Signed Oct. 30, 2023; revoked Jan. 20, 2025 | The prior whole-of-government framework (model reporting, NIST testing and evaluation). Its revocation removed the federal safety-testing anchor; legacy NIST products persist. |
| eo-14148 | Initial Rescissions of Harmful Executive Orders and Actions | EO 14148; doc. 2025-01901 | Signed Jan. 20, 2025 | The instrument that actually revoked EO 14110; cited so testimony does not misattribute the revocation. |
| eo-14365 | Ensuring a National Policy Framework for Artificial Intelligence | EO 14365; doc. 2025-23092 | Signed Dec. 11, 2025; operative | Directs review and preemption of conflicting state AI laws. Pushes toward a single national documentation and disclosure standard, which favors uniform VVUQ artifacts across multi-state trials. |

## B. National strategy and OMB lifecycle controls

| Key | Item | Date / status | Substance for the bill |
|:--|:--|:--|:--|
| ai-action-plan-2025 | Winning the Race: America's AI Action Plan | Released July 23, 2025 | Directs FDA and other agencies to create regulatory sandboxes and AI Centers of Excellence with open sharing of data and results, and directs NIST to convene health-sector standards work. A direct hook for standardized, shareable, automated VVUQ evidence. |
| omb-m2521 | OMB M-25-21, Accelerating Federal Use of AI | Issued Apr. 3, 2025; rescinds M-24-10 | Defines high-impact AI (a principal basis for consequential decisions, presumptively including clinical decision-making) and requires pre-deployment testing, an AI impact assessment, and ongoing monitoring. The cleanest surviving federal articulation of a VVUQ-style lifecycle. |
| omb-m2522 | OMB M-25-22, Driving Efficient Acquisition of AI in Government | Issued Apr. 3, 2025 | Shapes how federally funded AI specifies testing and performance evidence in solicitations; relevant if oncology-trial robotics is federally procured. |
| nist-caisi-2025 | Center for AI Standards and Innovation (CAISI) | Renamed June 3, 2025 | The federal locus for AI testing, evaluations, and standards; its evaluation competencies can inform rigorous VVUQ methods for high-consequence Physical AI. |

The NIST AI Risk Management Framework (AI 100-1) and its Generative AI Profile
(AI 600-1) are carried in standards-and-literature.bib (file 09) under nist-airmf
and nist-genai-profile; the framework's Measure function is the conceptual home
of VVUQ and is referenced from here.

## C. HHS strategy and agency AI use

| Key | Item | Date / status | Substance for the bill |
|:--|:--|:--|:--|
| hhs-ai-plan-2025 | HHS Strategic Plan for the Use of AI in Health, Human Services, and Public Health | Released Jan. 10, 2025 | The earlier external roadmap addressing algorithmic bias, privacy, and a trustworthy AI lifecycle; several health-IT transparency pieces were later pared back. |
| hhs-ai-strategy-2025 | HHS Artificial Intelligence Strategy (OneHHS) | Released Dec. 4, 2025 | Five pillars including governance and risk management and research reproducibility, with an AI Governance Board and an Acting Chief AI Officer. The reproducibility emphasis resonates with VVUQ goals. |

FDA agency AI use (the Elsa tool and the FDA AI Councils) is treated in file 02
and carried under fda-elsa-2025 in
federal-regulations-guidance.bib, referenced from here as a signal that FDA itself
governs agentic AI with built-in human oversight.

## Reading the posture (ASCII)

```
  Deregulatory pivot (EO 14179, EO 14365)
        |
        v
  VVUQ as federal mandate  --X-->  VVUQ as voluntary, standards-based credibility
        |                          (sponsor-driven differentiator)
        |                                 ^
        |                                 |
  But surviving lifecycle controls keep the structure:
   OMB M-25-21 high-impact AI: test -> impact assessment -> monitor
   AI Action Plan sandboxes: open sharing of data and results
   NIST AI RMF Measure function + CAISI evaluations
        |
        v
  The bill positions automated VVUQ as the engine that produces the
  credibility evidence this posture rewards, under a single national standard.
```

## Crosswalk to prior-bill provisions

| Prior-bill element | Executive or strategy anchor | Use in the new draft |
|:--|:--|:--|
| VVUQ lifecycle (test, validate, monitor) | omb-m2521 | Map the gate's stages to the high-impact-AI minimums. |
| Shareable, reproducible evidence | ai-action-plan-2025; hhs-ai-strategy-2025 | Frame the audit trail and public deposit as sandbox-ready open results. |
| Uniform national standard | eo-14365 | Argue for one federal VVUQ documentation standard over a state patchwork. |
| Measurement vocabulary | nist-airmf (file 09) | Anchor the gate's metrics in the Measure function. |

## Correlations to other VVUQ-04 files

1. File 08 (emerging bills) lists the legislative vehicles reacting to this posture.
2. File 02 (FDA) holds the FDA agency-AI items (Elsa, AI Councils) and the device guidance the AI Action Plan references.
3. File 06 (state law) is the patchwork that EO 14365 would preempt.
4. File 09 (standards) holds the NIST frameworks and the consensus standards the strategy points toward.
5. File 10 (crosswalk) places these items in the bill's findings and policy memo, not the operative text.

## Bibliography pointer

The executive orders, the AI Action Plan, the OMB memoranda, CAISI, and the HHS
strategies are carried in executive-actions-and-emerging-bills.bib under the keys
in the tables (for example eo-14179, ai-action-plan-2025, omb-m2521,
hhs-ai-strategy-2025). The NIST frameworks (nist-airmf, nist-genai-profile) live
in standards-and-literature.bib, and the FDA agency-AI item fda-elsa-2025 lives
in federal-regulations-guidance.bib, each referenced once to avoid duplicate
links.
