# Hearing Testimony and Research-Influence Brief: H. R. 9510, the Verification Before Generation in Physical AI Oncology Trials Act of 2026

*Independent research draft. Not an enacted law, not pending legislation, and not legal advice; not endorsed by the FDA, HHS, or any Member of Congress. The bills and executive actions discussed are research influences only and are not the legal basis of any operative provision.*

**Bill:** H. R. 9510 (illustrative), 119th Congress, 2d Session. The Verification Before Generation in Physical AI Oncology Trials Act of 2026. **Amends:** the Federal Food, Drug, and Cosmetic Act; adds a new section 515D, codified at 21 U.S.C. § 360e-5. **Committee context:** House Committee on Energy and Commerce (Subcommittee on Health).

This document has two parts. Part I is hearing testimony, written to be read aloud in about five minutes. Part II is a research-influence brief that records, for the hearing record, exactly how the recent executive actions and the 119th Congress emerging bills relate to the measure, and exactly why none of them appears in its operative text.

---

## PART I - Hearing Testimony

Chairman, Ranking Member, and Members of the Subcommittee: thank you for the opportunity to testify on the verification of artificial intelligence in cancer trials, and specifically on the safety of AI that does not merely advise a clinician but physically moves around a patient and acts upon that patient.

### Who I am

I am Kevin Kawchak, Chief Executive Officer of ChemicalQDevice. Our work concerns the verification, validation, and uncertainty quantification, or VVUQ, of high-consequence AI systems, including the control software for surgical and patient-contacting robots used in oncology research. I appear in an independent research capacity. The draft bill I will describe, H. R. 9510, is an illustrative research instrument; no Member has agreed to sponsor it, and nothing I say should be taken as the position of the FDA, of HHS, or of any Member of Congress.

### The problem

Cancer trials are beginning to place robots in direct physical contact with patients: surgical humanoids that cut and suture, positioning systems that hold a patient during treatment, and platforms that place biopsy or delivery needles. What such a robot does at the instant it touches a patient is decided by software, and that software is increasingly written by AI in real time rather than typed, line by line, by a human engineer.

Here is the gap. No Federal law governs the order of operations. A trial sponsor today may generate the robot-patient interaction code, run it on a patient, and document the safety checks afterward, in whatever order it chooses, because the order is simply not regulated. We call this the sequencing gap.

Sequence matters because of embodiment. In an ordinary data pipeline, a software error produces a wrong number that a human can catch downstream before anyone is harmed. In an embodied surgical system, the same class of error produces a wrong physical motion that a human cannot catch in time, because one moving body concentrates every failure mode into a single instrument acting in real time. Embodiment turns a software error into an uncatchable physical motion. Checking the code after it has already moved is, in this setting, checking too late.

### The proposal

H. R. 9510 supplies the one missing rule. It amends the Federal Food, Drug, and Cosmetic Act and adds a single new section, 515D, codified at 21 U.S.C. § 360e-5, placed immediately after the predetermined change control authority at section 515C that it most resembles.

The core rule is one sentence of policy: verify before generate. No robot-patient interaction code may be generated or executed in a Physical AI oncology clinical investigation unless an automated VVUQ process, bound to named external standards, has first cleared that interaction, with the record documented and attested. A record created after generation or execution does not satisfy the section. The timing of the record is itself the compliance fact.

The gate is concrete, not aspirational. Each check returns one of three results: ACCEPT, BLOCK, or ESCALATE, which returns the interaction to a qualified human. For each interaction the verification fraction must equal 1.0, meaning every check passes, with no partial credit. Three gates carry a hard catastrophe predicate at perfect agreement: no breach of a vascular no-fly volume, a guaranteed minimum clearance from any human sharing the room, and a guaranteed safe state on fault or emergency stop.

### Why it is feasible

This is not a hope; it has been run. In a first study, VVUQ-01, an automated pipeline held the verification fraction at 1.0 across 51 of 51 tests, with 1 ACCEPT and 5 BLOCK outcomes. In a second study, VVUQ-02, a ten-gate assurance suite over the control software for a surgical humanoid cleared 172 of 172 tests, with a composite mean of 93.56, reproducibly from a fixed seed, 20260525. The bill asks sponsors to do, as a precondition, what has already been demonstrated to work.

The gate is also bound to recognized standards rather than to anyone's discretion. Its thresholds tie to ASME V&V 40, IEC 80601-2-77, ISO/TS 15066, ISO 14971, NASA-STD-7009A, and IEEE 7009. That binding is what makes the test auditable and what keeps it from becoming a moving target.

### Why it fits existing law

I want to be candid about the policy environment, because it matters to this Subcommittee. The current Federal posture toward AI is deliberately deregulatory and pro-innovation. This bill is designed to complement that posture, not to fight it. It is not a broad AI mandate. It is a narrow, standards-bound safety gate for one thing: embodied robot-patient code in clinical trials.

The bill is additive. It leaves the investigational-device exemption, human-subject protection, and the investigational new drug framework in place. It frames the gate as a pre-authorized change-control discipline of the kind section 515C already contemplates, routes its records through the electronic-records rule and the quality-system regulation that sponsors already meet, and adds a savings clause so existing State human-in-the-loop laws are preserved. It creates no new agency and no new spending program; it directs rulemaking only.

### Respectful asks

I respectfully ask the Subcommittee to consider three things. First, treat the sequencing gap as a discrete, well-defined safety question, separate from the larger and more contested debates about AI policy generally. Second, recognize that verification before generation is technically achievable today, on the evidence I have summarized, so the question before you is one of timing and assurance, not of feasibility. Third, if the Subcommittee acts, keep any measure narrow and standards-bound, so that it strengthens the credibility of American oncology research without becoming the broad mandate that current Federal policy disfavors.

Thank you for your attention. I welcome your questions.

---

## PART II - Research-Influence Brief

This brief is the companion to Appendix D of the bill, the Research Influence Matrix. Its purpose is to put on the record how each recent executive action and each emerging 119th Congress bill relates to H. R. 9510, and to demonstrate that none of them is, or could be, the legal basis of any operative provision. The placement column below is kept consistent with that appendix, so the same authority carries the same placement in both documents.

### Research-influence table

| Authority | What it is | What it informs | Placement |
|:--|:--|:--|:--|
| EO 14179 | Removing Barriers to American Leadership in AI (90 FR 8741) | Deregulatory posture in the findings narrative; the framing of the gate as voluntary credibility rather than mandate | Memo; matrix; testimony |
| EO 14365 | Ensuring a National Policy Framework for AI | State-law review and preemption context; the case for one national documentation standard over a patchwork | Appendix; matrix; testimony |
| OMB M-25-21 | Accelerating Federal Use of AI (pre-deployment testing) | The pre-deployment-testing analogue; the surviving Federal lifecycle the gate maps onto | Memo; matrix; testimony |
| HHS AI Strategy | The HHS Artificial Intelligence Strategy (Dec. 2025) | Governance and reproducibility framing that resonates with VVUQ goals | Memo; matrix |
| H.R. 238 | Healthy Technology Act of 2025 | AI prescribing-authority direction; why autonomous clinical AI raises the evidentiary bar | Testimony; matrix |
| S. 1399 | Health Tech Investment Act | Medicare payment-class direction; clearance-gated payment makes validation the entry ticket | Testimony; matrix |
| H.R. 6361 | Ban AI Denials in Medicare Act | The human-over-AI signal; bipartisan distrust of opaque AI decisions | Findings narrative; matrix |
| H.R. 5045 | HEALTH AI Act | Generative-AI research direction; potential funding for validation methodology | Memo; matrix |
| H.Res. 694 | Sense of the House on the CMS WISeR AI pilot | The countervailing human-review signal; demand for auditable AI | Findings narrative; matrix |

### How each influence relates to the bill, and how it stays out of operative text

The executive actions set the environment the bill is drafted into, and they explain its tone. EO 14179 and EO 14365 together describe a deregulatory, preemption-minded Federal posture; they influence the bill in one direction only, arguing against a broad mandate and in favor of a narrow, voluntary-credibility framing and a single national documentation standard. OMB M-25-21 is more structural: its requirement of pre-deployment testing, an impact assessment, and ongoing monitoring is the cleanest surviving Federal articulation of a VVUQ-style lifecycle, and the bill uses it as an analogue to show that verifying before deployment is already a recognized Federal idea. The HHS Artificial Intelligence Strategy of December 2025, with its emphasis on governance and research reproducibility, is invoked only to show alignment of values.

Crucially, none of these is operative authority, and the bill never treats them as such. They are executive and sub-regulatory instruments, not statutes; they can change with an administration; and a safety gate that drew its legal force from an executive order would be unstable by construction. The bill therefore takes its operative force from the Federal Food, Drug, and Cosmetic Act and from recognized consensus standards, and confines the executive actions to the findings narrative, the policy memo, this brief, and the matrix.

The emerging bills play a different role: they establish legislative momentum on both sides of one question. On the autonomy side, H.R. 238 would let AI qualify as a practitioner eligible to prescribe, and S. 1399 would create a Medicare new-technology payment class for cleared algorithm-based services; both raise the stakes of getting autonomous clinical AI right, which is the gap a verification gate addresses. On the human-oversight side, H.R. 6361 would bar AI-driven prior authorization in traditional Medicare, and H.Res. 694 urges CMS to halt an AI coverage pilot; both reflect a bipartisan insistence that a human stay accountable for consequential AI decisions. H.R. 5045 sits alongside these as a research-funding vehicle that could support validation and evaluation methodology.

These bills inform the testimony, the findings, and the matrix, and nothing more. They are introduced or in-committee measures; not one is enacted, and an introduced bill has no legal effect, so citing one as the basis of an operative clause would be both incorrect and misleading. The operative-versus-influence rule the package follows keeps every one of them out of the statutory text and the comparative print, exactly where this brief records them.

### Verification note

Each authority above was verified by number, subject, and status before use, and each is presented strictly as a research influence. Readers should re-verify currency before relying on any entry, because executive actions and bill statuses change.

Three cautions govern this brief. First, there is no valid Act in the 119th Congress on this subject; the measures titled VALID Act of 2025 are an unrelated matter, so no such Act is cited here or anywhere in the package. Second, a standalone AI-in-clinical-trials bill and a standalone Federal health-AI liability bill could not be verified, and no bill numbers are assigned to them. Third, the sponsor of H.Res. 694 was not cleanly confirmable, so it is cited by number and subject only, without attribution to a specific Member. Consistent with the whole package, only enacted statutes, in-force rules, and recognized standards carry operative weight; the bills and executive actions in this brief carry none.

*Author: CEO Kevin Kawchak, ChemicalQDevice (ORCID 0009-0007-5457-8667). AI-assisted (Claude Code Opus 4.8). DOI 10.5281/zenodo.xxxxxxxx.*
