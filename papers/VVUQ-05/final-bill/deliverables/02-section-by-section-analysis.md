# Section-by-Section Analysis of H. R. 9510, the Verification Before Generation in Physical AI Oncology Trials Act of 2026

*Independent research draft. Not an enacted law, not pending legislation, and not legal advice; not endorsed by the FDA, HHS, or any Member of Congress.*

This analysis walks through H. R. 9510 (illustrative), 119th Congress, 2d Session, provision by provision. The bill amends the Federal Food, Drug, and Cosmetic Act (21 U.S.C. § 301 et seq.), current through Public Law 119-93. Its operative mechanism is a new section 515D (21 U.S.C. § 360e-5), inserted after section 515C (21 U.S.C. § 360e-4), backed by ten conforming amendments, a clerical amendment, a rule of construction, and a phased effective date. The core rule is one sequencing requirement: an automated verification, validation, and uncertainty quantification (VVUQ) process must clear robot-patient interaction code before that code is generated or executed in a Physical AI oncology clinical investigation.

## SEC. 1. Short Title; Table of Contents

Subsection (a) supplies the citation, the "Verification Before Generation in Physical AI Oncology Trials Act of 2026." Subsection (b) sets out the table of contents (short title, findings, the amendment, and the comparative print). This is standard front matter: it fixes how the Act is cited and maps what follows, and carries no substantive duty.

## SEC. 2. Findings

Section 2 records fourteen congressional findings that justify the rule and establish that it is feasible today. They make four moves. First, they state the problem: Physical AI oncology trials put robots in direct physical contact with patients, the robot's behavior at contact is governed by increasingly machine-generated software, and no Federal law requires that code to be verified before it is generated or executed. Second, they explain why embodiment raises the stakes: in a disembodied pipeline an error yields a wrong number a human can catch downstream, but in an embodied surgical system the same error class yields a wrong motion no human can catch in time. Third, they identify the closest existing analogues (the section 515C predetermined change control plan authority and FDA guidance, the Quality Management System Regulation at 21 CFR part 820, and the part 11 electronic-records rule) and note that each is voluntary, submission-based, and not required in advance of generation. Fourth, they ground the mechanism in recognized consensus standards (ASME V&V 40, NASA-STD-7009A, IEEE 7009, IEC 80601-2-77, ISO 14971, ISO/TS 15066, among others), in human-over-AI precedent in State law and the Medicare Advantage guardrail, and in Federal nondiscrimination law, reporting that automated verification has already been demonstrated. The findings are not operative commands; they supply the evidentiary and legal predicate a court or agency would consult when construing the Act.

## SEC. 3. Amendment to the Federal Food, Drug, and Cosmetic Act

This is the operative heart of the bill. Subsection (a) inserts new section 515D into subchapter V of the Act, after section 515C (21 U.S.C. § 360e-4). Subsection (b) makes the ten conforming amendments; subsection (c) is the clerical amendment, (d) the rule of construction, and (e) the effective date. The new section 515D is itself organized into subsections (a) through (j).

### New § 515D(a) Requirement

States the central rule. No robot-patient interaction code may be generated or executed in a Physical AI oncology clinical investigation unless an automated VVUQ process, bound to one or more named external standards, has first cleared for that interaction, and the cleared record has been documented and attested under subsection (e). This converts "verify before generate" from an engineering best practice into a binding statutory precondition.

### New § 515D(b) Order of Operations

Locks the sequence. A sponsor may not generate, and may not execute, the code in advance of the cleared verification record, and a record created after generation or execution does not satisfy the section. This forecloses the practice of generating and running code first and documenting afterward; the timing of the record is itself the compliance fact.

### New § 515D(c) Gate Thresholds and Decision Rule

Supplies the quantitative test each interaction must pass. Every gate emits ACCEPT, BLOCK, or ESCALATE: a single failing dimension sets BLOCK, and ambiguity or divergence sets ESCALATE and returns the interaction to a qualified human. For each interaction the verification fraction must equal 1.0 (every verification check passes), the validation agreement must meet or exceed the per-gate threshold with the maximum relative error at or below the per-gate bound and the human review recorded, the coefficient of variation across not fewer than three seeded runs must stay within the per-gate bound, and, where a hard catastrophe predicate applies, that predicate must also hold. The ten-gate schedule below ties each gate to a minimum agreement, a maximum coefficient of variation, the presence of a hard predicate, and a governing external standard, making the gate auditable rather than discretionary.

| Gate | Min. agreement | Max. CV | Hard predicate | Governing external standards |
|:--|:--|:--|:--|:--|
| 01 Bimanual hand-eye servo | 0.97 | 0.08 | No | IEC 80601-2-77; ISO 9283; ASME V&V 40 |
| 02 Dexterous finger force | 0.95 | 0.10 | No | IEC 80601-2-77; ISO/TS 15066 |
| 03 Whole-body balance | 0.98 | 0.06 | No | ISO 13482; IEC 60601-1 |
| 04 Autonomous plan correctness | 0.95 | 0.10 | No | UL 4600; IEEE 7009; IEC 62304 |
| 05 Instrument grasp and handover | 0.96 | 0.10 | No | IEC 80601-2-77; ISO 9283 |
| 06 Vascular no-fly volume (hand) | 1.00 | 0.05 | Yes | IEC 80601-2-77; ISO 14971 |
| 07 Bimanual suturing anastomosis | 0.96 | 0.08 | No | IEC 80601-2-77; Fistula Risk Score |
| 08 Perception scene understanding | 0.95 | 0.10 | No | ASME V&V 40; IEC 62304 |
| 09 Shared-room human collision | 1.00 | 0.06 | Yes | ISO/TS 15066; ISO 10218-1; ISO 13482 |
| 10 Fault, emergency stop, degradation | 1.00 | 0.05 | Yes | IEC 60601-1; ISO 13849-1; IEEE 7009 |

Gates 06, 09, and 10 carry the hard catastrophe predicate at agreement 1.00: zero breach of a vascular no-fly volume, a guaranteed minimum human clearance, and a guaranteed safe state on fault.

### New § 515D(d) Readiness Gates

Sets the site-level and robot-level preconditions before a patient is enrolled or a robot acts. The trial site must pass the Physical AI Standard Level gate on legislative authorization, regulatory compliance, and operational readiness. Each robot must meet the minimum Unification Standard Level for its functional type: not less than 7.0 for a surgical type, 6.0 for a therapeutic positioning or diagnostic needle placement type, 4.0 for a rehabilitative type, and 3.0 for a companion monitoring type. And each robot's behavior must be validated across not fewer than two simulation frameworks within cross-framework tolerances of less than 2 millimeters of trajectory deviation and less than 0.5 newton of force discrepancy. The graduated robot floor matches scrutiny to the physical risk of the function.

### New § 515D(e) Documentation and Attestation

Defines the record subsection (a) requires. For each covered algorithm the sponsor files algorithm documentation (a plain-language summary, the decision logic or architecture, the training or conditioning data sets, the gate bindings identifying the governing standard and threshold, the verification-before-generation record, and a determinism statement giving the seed). A responsible officer must sign a compliance attestation certifying that the gate cleared before generation, that each gate met its standard-bound threshold, that the site and robots cleared their readiness gates, that bias on protected characteristics is minimized, and that a licensed human retained the medical-necessity decision. All records sit in a hash-chained, tamper-evident audit trail satisfying 21 CFR part 11. This makes the duty enforceable and the attestation a personal certification.

### New § 515D(f) Cybersecurity, Human Oversight, and Lifecycle

Imposes operational controls across the system's life. Each Physical AI system must incorporate authentication and access control, encryption in transit and at rest, network segmentation, and software-integrity verification; operate under recorded human oversight with a manual override and an emergency stop that reaches a safe state within a procedure-appropriate budget plus hand-back-to-human escalation; and manage configuration and model versions, monitor for model and data drift, and, on decommissioning, archive the audit trail, securely erase patient data, and revoke access. These duties guard the gate against tampering and degradation over time.

### New § 515D(g) Nondiscrimination

Requires that each covered algorithm and its training data minimize the risk of bias on protected characteristics and adhere to evidence-based clinical guidelines, and that each system be designed and operated consistent with applicable accessibility and accommodation requirements. This carries Federal civil-rights and accessibility norms into the gate as substantive criteria, not afterthoughts.

### New § 515D(h) Regulations

Directs the Secretary to issue final regulations not later than 365 days after enactment, and permits interim guidance in the meantime, with a sponsor able to comply by meeting subsections (a) through (g) until the regulations issue. This makes the statute self-executing rather than dormant pending rulemaking.

### New § 515D(i) Definitions

Defines the fifteen operative terms, including Physical AI system, robot agent, robot-patient interaction code, generative artificial intelligence, AI-enabled device software function, verification, validation, uncertainty quantification, verification fraction (an equality to 1.0), validation agreement, coefficient-of-variation bound (over not fewer than three seeded runs), hard catastrophe predicate, Physical AI Standard Level, Unification Standard Level (a 1.0 to 10.0 robot-readiness score), and hash-chained audit trail. Precise definitions are what let the quantitative gate operate without discretion.

### New § 515D(j) Rule of Construction

Confirms the section's limits. It does not displace the investigational-device exemption under section 520(g), human-subject protection under 21 CFR part 50, the IND framework under 21 CFR part 312, or the section 515C change-control authority as it applies outside Physical AI, and it reclassifies no device. This positions section 515D as an additive sequencing gate layered on the existing trial framework, not a replacement for it.

### § 3(b) Conforming Amendments

Subsection (b) threads the new duty through ten surrounding device provisions so the Act stays internally consistent. Each amendment carries one subheading.

#### Conforming amendment (1): § 201(h) (21 U.S.C. § 321(h)), device definition

Confirms that software that generates or executes robot-patient interaction code, or that directs the autonomous physical action of a robot in contact with a human subject, is a device. This pulls the regulated code squarely inside FDA jurisdiction.

#### Conforming amendment (2): § 301 (21 U.S.C. § 331), prohibited acts

Adds a new prohibited act reaching generation or execution of the code in violation of section 515D and the failure to make or file the required documentation and attestation. This supplies the enforcement hook.

#### Conforming amendment (3): § 501 (21 U.S.C. § 351), adulteration

Deems a Physical AI device software function used without a cleared section 515D record to be adulterated. This attaches the Act's strongest existing consequence to a missing verification record.

#### Conforming amendment (4): § 505F (21 U.S.C. § 355g), real world evidence

Recognizes records generated under section 515D as real world evidence and applies the program to devices in Physical AI oncology investigations. This lets compliant verification records do double duty as evidence.

#### Conforming amendment (5): § 510(k) (21 U.S.C. § 360(k)), premarket notification

Provides that a verification-governed change consistent with an established predetermined change control plan needs no new premarket notification. This rewards the gate by streamlining compliant change.

#### Conforming amendment (6): § 513 (21 U.S.C. § 360c), classification

Graduates special controls for a device that generates or executes the code by its degree of autonomy. This matches regulatory rigor to how much the system acts on its own.

#### Conforming amendment (7): § 515 (21 U.S.C. § 360e), premarket approval

Requires a PMA application for such a device to include the cleared verification record and gate evidence required by section 515D. This integrates the gate into the highest-tier device pathway.

#### Conforming amendment (8): § 515C (21 U.S.C. § 360e-4), change control plans

Requires a predetermined change control plan for such a device to include an automated verification-before-change protocol consistent with section 515D. This carries the verify-before rule forward into the lifecycle.

#### Conforming amendment (9): § 520(o) (21 U.S.C. § 360j(o)), clinical-decision-support exclusion

Confirms that such a software function is not within the clinical-decision-support exclusion and remains a device. This closes the carve-out that autonomous robot-control software might otherwise slip through.

#### Conforming amendment (10): § 521 (21 U.S.C. § 360k), preemption savings clause

Adds a savings clause preserving State human-in-the-loop and audit requirements that are not different from, or in addition to, a Federal device requirement. This protects the existing State human-over-AI laws cited in the findings.

### § 3(c) Clerical Amendment

Inserts the new "Sec. 515D" item into the Act's table of contents after the item for section 515C. This is a housekeeping change so the codified table reflects the new section.

### § 3(d) Rule of Construction

Restates at the Act level that nothing in the Act displaces the section 520(g) IDE exemption, 21 CFR part 50 human-subject protection, the 21 CFR part 312 IND framework, the section 515C authority outside Physical AI, or any State law preserved under section 521 as amended, and that nothing reclassifies any device. It guards against reading the bill more broadly than intended.

### § 3(e) Effective Date; Implementation Deadline; Transition Rule

Sets the timing. The Act takes effect on the first day of the first calendar quarter beginning not less than one year after enactment; the Secretary must issue the final section 515D(h) regulations not later than 365 days after enactment; and an investigation already enrolling on the effective date has 180 days to come into compliance, with the February 2, 2026, effective date of the Quality Management System Regulation left undisturbed. This gives sponsors and the agency a predictable runway.

## SEC. 4. Comparative Print; Changes in Existing Law

Section 4 reproduces the eleven affected Title 21 device sections in 21 U.S.C. order, showing only the affected provisions, with matter to be deleted struck through, matter to be inserted underscored, and omitted unchanged matter marked by a row of asterisks. It is a Ramseyer-style comparative print: it carries no new duty but lets a reader see exactly how each conforming amendment changes existing law, the transparency record a committee expects before introduction.
