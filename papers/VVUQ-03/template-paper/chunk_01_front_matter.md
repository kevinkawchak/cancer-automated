\documentclass[11pt]{article}
\usepackage{Physical_AI_21_CFR_Part_312}
\addbibresource{Physical_AI_21_CFR_Part_312.bib}
\title{End-to-End Physical AI Oncology Clinical Trial Unification}
\author{Kevin Kawchak, ChemicalQDevice}
\date{17 March 2026}
\begin{document}

\begin{titlepage}
\centering
{\Large END-TO-END PHYSICAL AI ONCOLOGY CLINICAL TRIAL UNIFICATION\par}
\vspace{1.5cm}
{\Huge\bfseries Adaption: 21 CFR Part 312\par}
\vspace{0.5cm}
{\LARGE\bfseries Investigational New Drug Application\par}
\vspace{0.3cm}
{\Large Modified ECFR\par}
\vspace{0.8cm}
{\large Draft release\par}
\vspace{0.2cm}
{\large Released on 17 March 2026\par}
\vspace{0.2cm}
{\large \href{https://doi.org/10.5281/zenodo.19057628}{10.5281/zenodo.19057628}\par}
\vspace{0.2cm}
{\large CEO Kevin Kawchak, ChemicalQDevice\par}
\vfill
{\small The original 21 CFR Part 312 document is a work in the public domain under 17 U.S.C. \S~105, and may be used, reproduced, incorporated into other works, adapted, modified, translated or distributed under a public license. 21 CFR Part 312 --- Investigational New Drug Application. \href{https://www.ecfr.gov/current/title-21/chapter-I/subchapter-D/part-312}{Source ECFR}. This current work is not endorsed or sponsored by CFR. The original ECFR formatting was reconstructed into Markdown, and adapted further into LaTeX using Claude Code Opus 4.6.\par}
\end{titlepage}

\pagenumbering{roman}
\tableofcontents
\clearpage
\section*{Prefatory Note}

This adaptation extends the prior 21 CFR Part 312 --- Investigational New Drug Application to address the end-to-end integration of Physical AI systems, advanced robotics, digital twins, and AI/ML agents into oncology clinical trials. The prior 21 CFR Part 312 regulation established foundational procedures and requirements governing the use of investigational new drugs, including submission, review, and approval of INDs by the Food and Drug Administration. This current document adapts those procedures to encompass the specialized requirements of Physical AI oncology clinical trial unification, including autonomous surgical robots, therapeutic positioning systems, diagnostic needle-placement platforms, rehabilitative exoskeletons, companion monitoring systems, AI-driven decision support, simulation-validated procedures, and federated multi-site trial coordination.

The Unification Standard Level (USL) scoring framework (v1.4.0 through v1.8.0) provides quantitative readiness assessments for robotic platforms across four dimensions: simulation switching, AI integration, cross-robot sharing, and clinical trial collaboration. USL scores range from 1.0 to 10.0 and are referenced throughout this adaptation to establish minimum readiness thresholds for clinical deployment and to inform IND submission requirements for Physical AI components.

The national MCP-PAI standard (v1.2.0) defines the five-server Model Context Protocol topology (authorization, FHIR, DICOM, ledger, provenance), 23 standardized tools, six actor roles, and five cumulative conformance levels that govern data access, audit, and robot agent operations in Physical AI oncology trials. This protocol infrastructure underpins the data management, safety reporting, and electronic records requirements throughout this adaptation.

This adaptation should be read in conjunction with the physical-ai-oncology-trials repository (v2.5.0, DOI: 10.5281/zenodo.19057628), the national MCP-PAI oncology trials standard (v1.2.0, DOI: 10.5281/zenodo.18869776), the ICH E6(R3) Physical AI adaptation (DOI: 10.5281/zenodo.18973368), the 21 CFR Part 50 Physical AI adaptation (DOI: 10.5281/zenodo.19040707), and the federated learning framework (DOI: 10.5281/zenodo.18840880).

\section*{Document History}

\begin{description}[leftmargin=3.8cm,style=sameline]
\item[Prior Regulation] 21 CFR Part 312 --- Investigational New Drug Application. Originally published at 52 FR 8831, March 19, 1987, with subsequent amendments through 2023. The prior regulation established the baseline framework for IND submissions, clinical investigation phases, sponsor and investigator responsibilities, safety reporting, and expanded access provisions.
\item[Current Adaptation] End-to-End Physical AI Oncology Clinical Trial Unification: Adaption of 21 CFR Part 312, released 17 March 2026. This adaptation incorporates Physical AI requirements throughout for oncology clinical investigations involving autonomous robotic systems, digital twins, simulation frameworks, and AI/ML agents.
\item[Repository Refs] physical-ai-oncology-trials v2.5.0 (March 2026), national-mcp-pai-oncology-trials v1.2.0 (March 2026). These repositories provide validated code, tools, specifications, and documentation supporting this adaptation.
\end{description}

\clearpage
\pagenumbering{arabic}

\section*{Prior 21 CFR Part 312: Public Domain Notice}

This section preserves the public domain notice from the prior 21 CFR Part 312 regulation. The original 21 CFR Part 312 document is a work of the United States Government and is in the public domain under 17 U.S.C. \S~105. It may be used, reproduced, incorporated into other works, adapted, modified, translated or distributed under a public license. This current adaptation is not endorsed or sponsored by CFR. The original ECFR formatting was reconstructed into Markdown and adapted further into LaTeX. All adaptations, modifications, and additions for Physical AI are clearly identified throughout.

\textbf{Authority:} 21 U.S.C. 321, 331, 351, 352, 353, 355, 360bbb, 371; 42 U.S.C. 262.

\textbf{Source:} 52 FR 8831, Mar. 19, 1987, unless otherwise noted.

\textbf{Editorial Note:} Nomenclature changes to part 312 appear at 69 FR 13717, Mar. 24, 2004.

\clearpage

\section*{Change Summary Table}

The following table identifies every section of the prior 21 CFR Part 312 regulation that has been modified in this adaptation and summarizes the nature of the Physical AI additions. Sections not listed below retain their original text without modification.

\begin{longtable}{>{\raggedright\arraybackslash}p{2.2cm} >{\raggedright\arraybackslash}p{11.5cm}}
\toprule
\textbf{Section} & \textbf{Nature of Physical AI Additions} \\
\midrule
\endfirsthead
\toprule
\textbf{Section} & \textbf{Nature of Physical AI Additions} \\
\midrule
\endhead
\midrule
\multicolumn{2}{r}{\textit{Continued on next page}} \\
\bottomrule
\endfoot
\bottomrule
\endlastfoot
\S~312.1 & Extended scope to include Physical AI systems performing, assisting, or monitoring clinical procedures; added applicability to robotic platforms, simulation frameworks, and digital twins \\
\S~312.2 & Added Physical AI applicability provisions for IND exemptions; clarified that Physical AI system components require IND coverage when used in clinical investigations \\
\S~312.3 & Added 22 Physical AI definitions covering robot agents, USL, digital twins, simulation frameworks, MCP, conformance levels, hash-chained audit trails, federated learning, PCCP, and safety constructs \\
\S~312.6 & Extended labeling requirements to Physical AI system components and robot-administered investigational drugs \\
\S~312.7 & Extended promotion restrictions to Physical AI system capabilities associated with investigational drugs \\
\S~312.8 & Added Physical AI cost recovery provisions for robotic system deployment, simulation validation, and digital twin infrastructure \\
\S~312.10 & Extended waiver provisions to accommodate Physical AI system requirements \\
\S~312.20 & Added IND requirement for Physical AI system components used in clinical investigations \\
\S~312.21 & Added Physical AI considerations for each phase of clinical investigation, including simulation-based Phase 0 validation \\
\S~312.22 & Extended IND submission principles to Physical AI system documentation requirements \\
\S~312.23 & Added comprehensive Physical AI documentation requirements for IND content, including robot specifications, simulation validation data, digital twin models, AI/ML algorithms, and cybersecurity assessments \\
\S~312.30 & Extended protocol amendment requirements to Physical AI system modifications, algorithm updates, and simulation framework changes \\
\S~312.31 & Extended information amendment requirements to Physical AI technical updates \\
\S~312.32 & Added Physical AI safety reporting requirements including robot malfunction events, AI prediction errors, digital twin divergence, and cybersecurity incidents \\
\S~312.33 & Extended annual reporting to Physical AI system performance metrics, USL score updates, and simulation validation results \\
\S~312.38 & Extended IND withdrawal procedures to Physical AI system decommissioning \\
\S~312.40 & Added Physical AI general requirements for IND effectiveness, including simulation validation and USL threshold verification \\
\S~312.42 & Added Physical AI grounds for clinical hold including robotic safety failures, AI model degradation, and simulation-reality divergence \\
\S~312.44 & Extended termination grounds to Physical AI system failures and cybersecurity compromises \\
\S~312.45 & Extended inactive status provisions to Physical AI system dormancy and reactivation \\
\S~312.47 & Added Physical AI system demonstration requirements for regulatory meetings \\
\S~312.48 & Extended dispute resolution to Physical AI technical disagreements \\
\S~312.50 & Extended sponsor responsibilities to Physical AI system selection, validation, monitoring, and lifecycle management \\
\S~312.52 & Extended CRO transfer provisions to Physical AI obligations \\
\S~312.53 & Extended investigator and monitor selection to Physical AI qualifications \\
\S~312.54 & Extended emergency research monitoring to Physical AI systems \\
\S~312.55 & Extended investigator information requirements to Physical AI system updates \\
\S~312.56 & Extended ongoing investigation review to Physical AI system compliance monitoring \\
\S~312.57 & Extended recordkeeping to Physical AI system logs, simulation data, and digital twin records \\
\S~312.58 & Extended inspection access to Physical AI system records and audit trails \\
\S~312.59 & Extended drug disposition to Physical AI system decommissioning procedures \\
\S~312.60 & Extended investigator responsibilities to Physical AI system oversight \\
\S~312.61 & Extended drug control to Physical AI system access control \\
\S~312.62 & Extended investigator recordkeeping to Physical AI case histories and system interaction logs \\
\S~312.64 & Extended investigator reporting to Physical AI system events and performance metrics \\
\S~312.66 & Extended IRB review assurance to Physical AI system components \\
\S~312.68 & Extended inspection access to Physical AI investigator records \\
\S~312.69 & Extended controlled substance handling to Physical AI-mediated administration \\
\S~312.70 & Extended disqualification to Physical AI system misuse and noncompliance \\
\S~312.80 & Extended life-threatening illness provisions to Physical AI accelerated development pathways \\
\S~312.81 & Extended scope to Physical AI-assisted therapies for life-threatening diseases \\
\S~312.82 & Extended early consultation to Physical AI system design review \\
\S~312.83 & Extended treatment protocols to Physical AI-assisted therapeutic delivery \\
\S~312.84 & Extended risk-benefit analysis to Physical AI system risk profiles \\
\S~312.85 & Extended Phase 4 studies to Physical AI post-market performance monitoring \\
\S~312.87 & Extended active monitoring to Physical AI system clinical performance \\
\S~312.88 & Extended patient safety safeguards to Physical AI-specific protections \\
\S~312.110 & Extended import/export requirements to Physical AI system components and software \\
\S~312.120 & Extended foreign clinical study acceptance to Physical AI system validation data \\
\S~312.130 & Extended public disclosure provisions to Physical AI system data \\
\S~312.140 & Extended correspondence requirements to Physical AI-specific submissions \\
\S~312.145 & Extended guidance document provisions to 8 Physical AI-specific guidance topics \\
\S~312.160 & Extended laboratory use provisions to Physical AI preclinical testing \\
\S~312.300 & Extended expanded access scope to Physical AI-assisted treatment \\
\S~312.305 & Extended expanded access requirements to Physical AI system safeguards \\
\S~312.310 & Extended individual patient access to Physical AI-assisted emergency treatment \\
\S~312.315 & Extended intermediate-size access to Physical AI multi-site deployment \\
\S~312.320 & Extended treatment IND to Physical AI widespread treatment use \\
New J & New Subpart J: Additional Requirements for Physical AI Investigational Systems in Oncology Trials \\
\end{longtable}

\clearpage
