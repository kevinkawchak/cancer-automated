# Chunk 09 — Section 11: Limitations and QSP Trial Conclusions; Section 12: Future Work; Section 13: Deliverables and Impact; Section 14: Financial Assessments; Data Availability; Acknowledgments; Ethical Disclosures; Rights and Permissions; About This Study

---

## 11. Limitations and QSP Trial Conclusions

While the virtual trial provided rich insights, it's important to acknowledge its limitations and the lessons learned:

- **Model Assumptions:** We assumed no acquired resistance, fully compliant patients, and ideal pharmacodynamics for novel agents. These assumptions likely made some outcomes optimistic (especially long-term durability of responses). We communicated these assumptions, and in interpreting results we always considered how breaking these assumptions would affect outcomes (e.g. if resistance emerges, Arm H/I's long OS would drop). The lesson is that model-based predictions are only as good as the assumptions – and including stakeholders in reviewing those assumptions was crucial. In our case, clinicians immediately questioned the lack of acquired resistance, prompting us to add that to future model plans.
- **Data Gaps:** For experimental components (like CD47 or CD40 agents in PDAC), we had to generate patients, which introduces uncertainty. We mitigated it by doing sensitivity analyses (seeing that our conclusions didn't hinge on exact assumed potency, as noted). The learning here is to perform UQ around any poorly-known parameters and be cautious in over-interpreting results that depend on them. We clearly flagged where data was thin (e.g. "magrolimab effect may be overestimated since clinical PDAC data is lacking").
- **Numerical Stability vs. Convenience:** A key lesson was the importance of numerical stability. Initially, we were comfortable with dt = 0.5 days for faster simulation, but the AI assistant uncovered that this introduced subtle inaccuracies (inflating ORRs). Based on that, we re-ran with dt = 0.05 days and got corrected, more realistic results. This was a valuable reminder that even if convergence tests suggest a plateau, using the finest feasible resolution is safest when seeking high accuracy. It did cost more computing time, but ultimately it improved model fidelity (Arm A's ORR dropping from 50% to 15% after this fix fundamentally changed our interpretation of some arms). Thus, we learned not to cut corners on resolution when it can materially affect outcomes.
- **Biology vs. Artifacts:** Some initial results that looked interesting turned out to be artifacts of the model rather than true biology – for example, Arm A's very high ORR was an artifact. Once corrected, the story changed: Arm A became a more realistic baseline (and some arms like B went from looking like "no OS improvement" to a slight improvement in relative terms). However, some end points such as mPFS and Grade 3 AEs remained suboptimal throughout code iterations, as apparent in final trial summaries. The take-home is that one must distinguish genuine biological insights from model quirks. Our layered verification (both numerical and biological calibration) helped us filter out those artifacts before drawing conclusions.
- **Generality:** Our results apply to the specific scenario modeled (metastatic PDAC trial with certain drugs). One limitation is the generality of these findings – e.g. the success of Arm C (KRAS G12D inhibition, shown in Figure 10D) assumes a drug as effective as MRTX-1133; if real drugs are weaker, outcomes would differ. We framed our findings in a comparative way intentionally – focusing on which strategies outperform others, rather than the exact percentages. The lesson is that QSP virtual trials are best at comparative effectiveness and scenario exploration, not absolute prediction. We conveyed that nuance to stakeholders (e.g. we said "Arm H could in principle improve survival vs current therapy, if the drugs work as modeled," making it clear this is conditional and illustrative).
- **Stakeholder Communication:** We learned the importance of communicating these complex results in understandable terms. We iteratively improved our presentation – adding interpretive text ("this could translate to X months benefit in a trial") and visual aids (Kaplan–Meier curves, bar charts for ORR/toxicity) that we included in this report. This made the findings accessible. A lesson was that the QSP model's value is only realized if the end-users (clinicians, decision-makers) can grasp the insights, so significant effort went into translating model-speak into clinical-speak. The retrospective nature helped because we could refine our messaging after seeing initial confusion.
- **AI Integration:** Using AI (LLMs) was a novel aspect. It accelerated coding and documentation, but we also encountered its limits (the AI was limited in the number of parameters being modified at one time). We found that AI was excellent for first drafts and tedious tasks (like converting code to text), but human oversight was essential for prompting additional fixes. The lesson is that AI can enhance productivity, but it's not a replacement for expert review – rather, it's a tool that needs guidance. When we followed up on the AI's recommendations (like testing more dt values), we gained unexpected insights. So being receptive to the AI "suggestions" (even though they were not always explicit – in one case the AI simply flagged a discrepancy, which we interpreted as a suggestion to investigate) proved beneficial.

In conclusion, the virtual trial yielded valuable insights but also highlighted the importance of rigorous validation and clear communication. The limitations noted are not detriments but rather guideposts for improving future models and for tempering conclusions with appropriate caution. A virtual trial is a powerful tool to explore "what-if" scenarios, but it must be continually cross-checked with reality and presented with its assumptions front and center. We believe this retrospective analysis has illustrated both the potential and the current boundaries of QSP-driven virtual trials in oncology.

---

## 12. Future Work and Model Extensions

Building on this project, several future directions have been identified:

- **Acquired Resistance Module:** As noted, adding an acquired resistance mechanism is a priority. We plan to introduce a stochastic process during simulation where a fraction of sensitive tumor cells can become resistant each cycle, at rates informed by clinical data (e.g. resistance mutations emerging after a median of X months on therapy). This will allow us to model eventual relapse even in arms that initially perform well, providing more realistic long-term projections (e.g. turning those flat OS tails into gradually declining ones).
- **Tumor-Immune Dynamics Expansion:** Explicitly modelling T cell and macrophage populations, and interactions like checkpoint inhibition kinetics and myeloid suppression would likely improve results. This could enable exploration of immunotherapy scheduling (e.g. induction chemo to release antigens, followed by delayed PD-1 blockade, etc.) and a deeper analysis of why certain patients might not respond. We would calibrate this to any PDAC immune data available (tumor-infiltrating lymphocyte counts, etc.). Biomarker-Driven Patient Enrollment: In this virtual trial, each arm was run on an appropriate subset, but in reality, one might design trials that test multiple strategies in the same patient (adaptive trials) or require biomarker pre-selection. We could simulate an adaptive trial design where, say, KRAS G12C patients are adaptively randomized between Arm H and Arm I to see which is better – mimicking a head-to-head in that niche population. This would involve coding an "umbrella" trial logic atop our model. It could help address questions like, should chemo be added or omitted if a KRAS G12C drug is available? Our current results hint "omit chemo," but a formal trial simulation could confirm significance and optimal decision rules.
- **Cost-Effectiveness and Multi-Criteria Optimization:** While our model focused on efficacy and toxicity, a real decision might include drug costs or quality-of-life metrics. We can extend the analysis to incorporate a simple cost model (drug costs, hospitalization costs from toxicity) and even a quality-adjusted survival metric. This would allow assessing, for example, if Arm H's small survival edge over Arm I is worth the presumably higher cost and worse quality of life (likely not, according to our current thinking). Such extensions move into the health economics realm, broadening the impact of the model for decision-makers.
- **Other Indications and Generalizability:** The core model can be adapted to other indications (e.g. earlier-stage PDAC). We identified that by swapping out the tumor growth parameters and recalibrating drug effects, we could potentially simulate, say, a pancreatic adjuvant therapy trial that tests a similar immunotherapy combo. Exploring the model's flexibility in this regard is future work – essentially testing how reusable the QSP modules are beyond this specific trial.
- **Mechanistic Detail Additions:** We plan to enrich certain mechanisms. One example is pharmacokinetics: currently drug effects are direct, but adding PK sub-models (e.g. gemcitabine clearance, peak/trough concentrations) could allow exploring dose adjustments or scheduling changes. Another example is a more detailed toxicity model that distinguishes types of toxicities (hematologic vs hepatic, etc.) and their timing – useful if considering supportive care interventions. These additions would make the model more granular and possibly reveal time-dependent effects (like needing to delay doses due to toxicity, which isn't currently simulated explicitly beyond drop-out).
- **Collaboration and Validation:** We aim to validate the model's predictions with any emerging clinical trial data. For instance, if a trial of KRAS G12C inhibitor + chemo in PDAC reports results, we will compare those to our Arm H prediction. Any discrepancies will guide model refinement (maybe adjusting the immune effect or the cross-resistance assumptions). We also could collaborate with experimentalists: e.g. using the model to design a mouse study that could test a hypothesis (like "chemo-free combo is better for KRAS G12C – test this in a PDAC mouse model with KRAS G12C and see if immune response is durable"). This would further strengthen the model's credibility and potentially feed back new data to improve it. Overall, the future work will enhance the model's realism, extend its applicability, and integrate it more tightly with the experimental/clinical workflow.

---

## 13. Deliverables and Impact

Finally, we summarize the key deliverables from this project here and in Data availability:

- **Comprehensive Playbook (this paper):** A structured report detailing the trial design, model implementation, V&V summarization, and results. It serves as both a record of what was done (for internal knowledge management or audits) and a communication tool for external stakeholders (e.g. to include in a regulatory submission or share with a pharma partner considering a similar approach). By numbering sections according to requirements and including all results and interpretations, it ensures transparency and traceability from objectives to outcomes.
- **Initial Protocol (Part A):** The original trial design document (text format) capturing the clinical context and intent. It describes the trial arms A-E and G-K, patient population, inclusion/exclusion criteria, dosing schedules, and endpoint definitions. Essentially, this is the written Phase II protocol that served as the starting blueprint for the model. It's included to provide the clinical reference for all modeling decisions.
- **Verified QSP Model Code (Part B):** The Python code and notebooks that implement the trial simulation. The impact of this deliverable is that anyone can reproduce the virtual trial or even modify parameters/arms using Python 3.12 to test new ideas, fostering confidence in the model's effectiveness and reusability. (.ipynb, .py, csv for each trial run)
- **Reverse-Engineered Model Spec (Part C):** A human-readable document that describes the model in plain language, generated from the code. This is useful for team members or external reviewers who prefer not to read code. It enhances understanding and trust, as it reads like a protocol describing each arm's mechanism and the equations in words. Future conversions back to code should primarily utilize Part B, accompanied by author notes taken from Part C.
- **VVUQ Report (Part D) summarized here:** A compilation of all verification, validation, and uncertainty quantification activities. It demonstrates that the model was built rigorously. The impact is to satisfy governance requirements (anyone auditing the model development can see we tested numerical stability, explored uncertainties, etc.) and to identify the model's domain of validity.
- **Simulation Output Data:** All raw and processed data from the virtual trial runs have been included as supplementary files as CSV files. This includes patient-level outcomes and arm-level summaries. This data can be mined further by statisticians or used to perform additional analyses (for example, subgroup outcomes or correlations between toxicity and efficacy). By delivering the data, we allow others to verify our summary statistics and derive new insights.
- **Key Prompts (Part E):** We included pivotal prompts used on the study to a) Import patient arms and archetypes from a prior article b) Obtain Part A text based clinical trial c) Improve performance of the code based trial d) Expand to the Part B code with multi-mechanism toxicity e) Obtain the Part C text based trial instructions from Part B.
- **Figures and Plots:** A collection of figures (Kaplan–Meier curves, waterfall plots of tumor shrinkage, bar charts of ORR, etc.) were generated. Where individual patient data from log files were incorporated, AI utilized sampling from patients for dashboards included in this playbook. Visualizing the results makes the impact more tangible – for instance, seeing the separation of survival curves drives home how much better Arm H was than Arm G, and how toxicity succinctly shows how toxic Arm E was relative to others.

In sum, the project deliverables provide a 360-degree view of the virtual trial and ensure that its insights can be acted upon. The in silico findings have already influenced our pipeline decisions. By sharing this playbook with the broader team and stakeholders, we enabled data-driven prioritization: resources can be focused on the most promising strategies (KRAS and BRCA targeted combos) and away from likely dead-ends (toxic immunotherapy overloads). This illustrates the real impact of the QSP virtual trial – it's not just an academic exercise, but a tool that informs practical decisions, potentially saving time and cost by avoiding unfruitful paths and highlighting high-yield opportunities.

---

## 14. Financial Assessments

Figure 14A: (A) Industry QSP simulation estimated trial cost vs prospective real trials; (B) ROI from avoiding the larger cost; (C) Cost distribution of QSP trials vs. in-person trials.

Figure 14B: (A) Current study cost estimate and ROI vs Phase II, III trials; (B) Time to trial results favored by current study; (C) Per-patient cost reduction factor. Key Findings: Virtual trials are ~300× cheaper than Phase II, ~1000× cheaper than Phase III, with 24-40× faster results.

---

## Data Availability

**Column 1:**
1. A1_Initial_Protocol.pdf
2. B1_Final_Trial_Code.csv
3. B1_Final_Trial_Code.ipynb
4. B1_Final_Trial_Code.py
5. B2_Trial_Sequence
   - B2_Draft_1: B2_Draft_1.csv, B2_Draft_1.ipynb, B2_Draft_1.py
   - B2_Draft_2: B2_Draft_2.csv, B2_Draft_2.ipynb, B2_Draft_2.py
   - B2_Draft_3: B2_Draft_3.csv, B2_Draft_3.ipynb, B2_Draft_3.py
   - B2_Neg_Control: B2_Neg_Control.csv, B2_Neg_Control.ipynb, B2_Neg_Control.py
   - B2a_Prior_Files: 2 .pdfs, 1 .ipynb files
6. B3_Final_Triplicate
   - B3_Final_1: B3_Final_1.csv, B3_Final_1.ipynb, B3_Final_1.py
   - B3_Final_2: B3_Final_2.csv, B3_Final_2.ipynb, B3_Final_2.py
   - B3_Final_3: B3_Final_3.csv, B3_Final_3.ipynb, B3_Final_3.py
   - **Numerical Stability**
7. B4_Verify_Time_Step
   - B4_dt_005: B4_dt_005.csv, B4_dt_005.ipynb, B4_dt_005.py
   - B4_dt_010: B4_dt_010.csv, B4_dt_010.ipynb, B4_dt_010.py
   - B4_dt_025: B4_dt_025.csv, B4_dt_025.ipynb, B4_dt_025.py
   - B4_dt_045: B4_dt_045.csv, B4_dt_045.ipynb, B4_dt_045.py

**Column 2:**
7. B4_Verify_Time_Step (cont.)
   - B4_dt_050: B4_dt_050.csv, B4_dt_050.ipynb, B4_dt_050.py
   - B4_dt_055: B4_dt_055.csv, B4_dt_055.ipynb, B4_dt_055.py
   - B4_dt_060: B4_dt_060.csv, B4_dt_060.ipynb, B4_dt_060.py
8. B5_Verify_Grid_Size
   - B5_Grid_Size_2: B5_Grid_Size_2.csv, B5_Grid_Size_2.ipynb, B5_Grid_Size_2.py
   - B5_Grid_Size_3: B5_Grid_Size_3.csv, B5_Grid_Size_3.ipynb, B5_Grid_Size_3.py
   - B5_Grid_Size_4: B5_Grid_Size_4.csv, B5_Grid_Size_4.ipynb, B5_Grid_Size_4.py
   - B5_Grid_Size_5: B5_Grid_Size_5.csv, B5_Grid_Size_5.ipynb, B5_Grid_Size_5.py
   - B5_Grid_Size_6: B5_Grid_Size_6.csv, B5_Grid_Size_6.ipynb, B5_Grid_Size_6.py
   - B5_Grid_Size_7: B5_Grid_Size_7.csv, B5_Grid_Size_7.ipynb, B5_Grid_Size_7.py
   - **Sensitivity Analysis**
9. B6_Quantify_Tumor_Vol
   - B6_dVol_res_003: B6_dVol_res_003.csv, B6_dVol_res_003.ipynb, B6_dVol_res_003.py
   - B6_dVol_res_006: B6_dVol_res_006.csv, B6_dVol_res_006.ipynb, B6_dVol_res_006.py
   - B6_dVol_res_009: B6_dVol_res_009.csv, B6_dVol_res_009.ipynb, B6_dVol_res_009.py

**Column 3:**
10. B7_Quantify_Emax_Mrtx
    - B7_Emax_036: B7_Emax_036.csv, B7_Emax_036.ipynb, B7_Emax_036.py
    - B7_Emax_072: B7_Emax_072.csv, B7_Emax_072.ipynb, B7_Emax_072.py
    - B7_Emax_108: B7_Emax_108.csv, B7_Emax_108.ipynb, B7_Emax_108.py
11. B8_Quantify_Vol_Resist
    - B8_Vol_Res_005: 8_Vol_Res_005.csv, 8_Vol_Res_005.ipynb, 8_Vol_Res_005.py
    - B8_Vol_Res_015: B8_Vol_Res_015.csv, B8_Vol_Res_015.ipynb, B8_Vol_Res_015.py
    - B8_Vol_Res_030: B8_Vol_Res_030.csv, B8_Vol_Res_030.ipynb, B8_Vol_Res_030.py
12. B9_Quantify_EC50_Mrtx
    - B9_EC50_100: B9_EC50_100.csv, B9_EC50_100.ipynb, B9_EC50_100.py
    - B9_EC50_050: B9_EC50_050.csv, B9_EC50_050.ipynb, B9_EC50_050.py
    - B9_EC50_025: B9_EC50_025.csv, B9_EC50_025.ipynb, B9_EC50_025.py
    - **Final Documentation**
13. C1_Final_Protocol.pdf
14. D1_VVUQ_Report.pdf
15. E1_Key_Prompts.pdf
16. F1_Trial_Charts.ipynb
17. F1_Trial_Charts.py
18. F1_Trial_Images

Source: Zenodo [20KawchakQSPPDAC]

---

## Acknowledgments

The author would like to acknowledge OpenAI for providing access to ChatGPT, Google for providing access to Gemini, Anthropic for providing access to Claude, and xAI for providing access to Grok.

---

## Ethical Disclosures

The author of the article declares no competing interests.

---

## Rights and Permissions

This article is distributed under the terms of the Creative Commons Attribution 4.0 International License (CC BY 4.0), which permits unrestricted use, distribution, and reproduction in any medium, provided the original author(s) and source are properly credited, a link to the Creative Commons license is provided, and any modifications made are indicated. To view a copy of this license, visit https://creativecommons.org/licenses/by/4.0/.

---

## About This Study

Kawchak K. QSP Metastatic Pancreatic Cancer AI Clinical Trial Simulation From Protocol to Prediction: Code, VVUQ, and Playbook. Zenodo. 2025; 10.5281/zenodo.17001137 [20KawchakQSPPDAC].
