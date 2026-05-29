\section{SUBPART J --- PHYSICAL AI SYSTEMS IN CLINICAL INVESTIGATIONS (NEW)}

\textit{Note: This subpart is entirely new and has no corresponding subpart in the original 21 CFR Part 312. It consolidates and expands upon the Physical AI-specific requirements introduced throughout this adapted regulation.}

\subsection{\S~312.400 Purpose and Scope of Subpart J}

(a) \textit{Purpose.} This subpart establishes the comprehensive regulatory framework for the use of Physical AI systems in clinical investigations of investigational new drugs. It consolidates the Physical AI-specific requirements referenced throughout this part and provides additional detailed requirements for Physical AI system validation, operation, monitoring, and lifecycle management during clinical investigations.

(b) \textit{Scope.} This subpart applies to all clinical investigations conducted under this part in which a Physical AI system, as defined in \S~312.1(b), is used to assist in, perform, or monitor any aspect of investigational drug administration, including but not limited to:

\begin{description}[leftmargin=0.8cm,style=sameline]
\item[(1)] Robotic surgical systems that administer investigational drugs during surgical procedures;
\item[(2)] Automated drug delivery systems that prepare, measure, or deliver investigational drugs;
\item[(3)] AI-guided treatment planning systems that use digital twin models, simulation data, or machine learning algorithms to determine drug administration parameters;
\item[(4)] Robotic monitoring systems that assess patient response to investigational drugs through automated vital sign measurement, biomarker sampling, or imaging; and
\item[(5)] Integrated Physical AI platforms that combine two or more of the above functions.
\end{description}

(c) \textit{Relationship to other subparts.} The requirements of this subpart supplement, and do not replace, the requirements of Subparts A through I. In the event of a conflict between a provision of this subpart and a Physical AI adaptation provision in another subpart, the more specific provision shall control.

[Physical AI adaptation added 17 March 2026.]

\subsection{\S~312.401 Physical AI System Classification for Clinical Investigations}

(a) \textit{Risk-based classification.} Physical AI systems used in clinical investigations shall be classified according to their level of autonomy and clinical risk:

\begin{description}[leftmargin=0.8cm,style=sameline]
\item[(1)] \textit{Class I --- Assistive Physical AI.} Systems that provide decision support, guidance, or enhanced visualization to the investigator but do not directly manipulate the investigational drug or the patient. The investigator retains full manual control of drug administration at all times. Examples include AI-guided imaging systems that assist in identifying optimal injection sites and digital twin systems used solely for treatment planning without automated execution.
\item[(2)] \textit{Class II --- Collaborative Physical AI.} Systems that perform specific drug administration tasks under continuous direct supervision by a qualified investigator who maintains the ability to override or halt the system's actions in real time. The system and investigator share control of the drug administration process. Examples include robotic infusion systems that execute physician-approved infusion protocols and robotic surgical systems that perform drug delivery under surgeon guidance.
\item[(3)] \textit{Class III --- Supervised Autonomous Physical AI.} Systems that can execute complete drug administration procedures with limited investigator intervention, under supervisory oversight. The investigator monitors the system's performance and intervenes when specified conditions are met, but does not control each individual action. Examples include automated closed-loop drug delivery systems that adjust dosing based on real-time patient monitoring data and robotic brachytherapy systems that autonomously place radioactive sources according to a pre-approved treatment plan.
\end{description}

(b) \textit{Classification requirements.} The sponsor shall classify each Physical AI system in the Physical AI System Description submitted under \S~312.23(g). FDA may reclassify a Physical AI system if it determines that the sponsor's classification does not accurately reflect the system's level of autonomy or clinical risk.

(c) \textit{Class-specific requirements.}

\begin{description}[leftmargin=0.8cm,style=sameline]
\item[(1)] \textit{Class I systems} are subject to the general Physical AI requirements of this part, including the Physical AI System Description, simulation validation, and Physical AI adverse event reporting requirements.
\item[(2)] \textit{Class II systems} are subject to all Class I requirements and, in addition, must demonstrate USL scores meeting or exceeding the thresholds specified in \S~312.1(e), must implement real-time safety monitoring with automatic safety stop capabilities, and must provide the investigator with real-time feedback on system actions and drug administration status.
\item[(3)] \textit{Class III systems} are subject to all Class I and Class II requirements and, in addition, must demonstrate enhanced simulation validation including multi-scenario failure mode testing, must implement redundant safety systems with independent monitoring channels, must maintain continuous telemetry logging at a resolution sufficient to reconstruct all system decisions and actions, and must undergo periodic re-validation during the clinical investigation as specified in the PCCP.
\end{description}

[Physical AI adaptation added 17 March 2026.]

\subsection{\S~312.402 Physical AI System Validation Requirements}

(a) \textit{Pre-clinical validation.} Before a Physical AI system may be used in a clinical investigation, the sponsor shall complete the following validation activities:

\begin{description}[leftmargin=0.8cm,style=sameline]
\item[(1)] \textit{Simulation validation.} The Physical AI system shall be validated through simulation testing as described in \S~312.21(d), including validation across multiple simulation frameworks to demonstrate cross-framework behavioral consistency. The simulation validation shall test the system across the full range of clinical scenarios anticipated in the protocol, including normal operating conditions, boundary conditions, and failure scenarios;
\item[(2)] \textit{Bench testing.} The Physical AI system shall undergo bench testing using physical phantoms, tissue analogues, or other non-clinical test articles that replicate the mechanical, thermal, and chemical properties of the target clinical environment. Bench testing shall include verification of drug delivery accuracy, force and torque limits, sensor calibration, and emergency stop response times;
\item[(3)] \textit{Integration testing.} The Physical AI system shall be tested in its complete clinical configuration, including all hardware components, software modules, network connections, and peripheral devices, to verify that all system components function correctly in concert and that no integration defects compromise safety or performance; and
\item[(4)] \textit{Sim-to-real gap assessment.} The sponsor shall quantify the sim-to-real gap by comparing the Physical AI system's performance in simulation to its performance in bench testing, identifying any discrepancies, and establishing tolerance ranges for acceptable divergence. The sim-to-real gap assessment shall be updated as the system is modified during the investigation.
\end{description}

(b) \textit{Clinical site validation.} Before a Physical AI system may be used in clinical procedures at a specific investigational site, the following site-specific validation shall be completed:

\begin{description}[leftmargin=0.8cm,style=sameline]
\item[(1)] \textit{Installation qualification.} Verification that the Physical AI system has been installed at the site in accordance with the manufacturer's specifications and the Physical AI System Description, including environmental conditions (temperature, humidity, vibration, electromagnetic interference), power supply and backup power systems, network connectivity and bandwidth, and physical space and access requirements;
\item[(2)] \textit{Operational qualification.} Verification that the Physical AI system operates within the specified performance parameters at the site, including execution of the standard test procedures defined in the Physical AI System Description, verification of all safety systems including emergency stop, force limits, and collision detection, and confirmation of communication with all required peripheral devices and monitoring systems; and
\item[(3)] \textit{Performance qualification.} Demonstration that the Physical AI system can consistently perform the clinical procedures authorized under the protocol, using site-specific test articles, within the acceptance criteria defined in the Physical AI System Description.
\end{description}

(c) \textit{Ongoing validation.} During the clinical investigation, the sponsor shall:

\begin{description}[leftmargin=0.8cm,style=sameline]
\item[(1)] Monitor Physical AI system performance against the pre-specified acceptance criteria established during pre-clinical validation;
\item[(2)] Re-validate the Physical AI system following any software update, AI/ML model update, hardware modification, or safety event, in accordance with the PCCP and the procedures described in the Physical AI System Description; and
\item[(3)] Conduct periodic re-validation at intervals specified in the protocol, including USL reassessment and simulation re-validation, to confirm that the system's performance has not degraded over time.
\end{description}

[Physical AI adaptation added 17 March 2026.]

\subsection{\S~312.403 Physical AI System Cybersecurity Requirements}

(a) \textit{Cybersecurity by design.} Physical AI systems used in clinical investigations shall incorporate cybersecurity protections in their design, including:

\begin{description}[leftmargin=0.8cm,style=sameline]
\item[(1)] \textit{Authentication and access control.} Multi-factor authentication for operator access, role-based access controls that limit system functions to authorized personnel, and automatic session timeout after periods of inactivity;
\item[(2)] \textit{Data protection.} Encryption of data in transit and at rest, including telemetry data, patient data, drug administration records, and system configuration data. Encryption shall use algorithms and key lengths consistent with current NIST guidelines;
\item[(3)] \textit{Network security.} Network segmentation isolating the Physical AI system from general hospital networks, intrusion detection and prevention systems monitoring Physical AI network traffic, and firewall configurations restricting inbound and outbound connections to authorized endpoints;
\item[(4)] \textit{Software integrity.} Secure boot processes that verify firmware and software integrity at startup, code signing for all software components with verification before execution, and integrity monitoring that detects unauthorized modifications to system software; and
\item[(5)] \textit{Audit trails.} Hash-chained, cryptographically signed audit trails that record all system events, operator actions, configuration changes, and network communications in a manner that prevents undetected tampering.
\end{description}

(b) \textit{Vulnerability management.} The sponsor shall maintain a vulnerability management program for the Physical AI system, including:

\begin{description}[leftmargin=0.8cm,style=sameline]
\item[(1)] Regular vulnerability scanning and assessment;
\item[(2)] A defined process for evaluating and applying security patches, with timelines proportionate to the severity of the vulnerability;
\item[(3)] A software bill of materials (SBOM) identifying all third-party software components and their versions; and
\item[(4)] Monitoring of vulnerability databases and threat intelligence sources for vulnerabilities affecting Physical AI system components.
\end{description}

(c) \textit{Incident response.} The sponsor shall maintain a cybersecurity incident response plan that includes:

\begin{description}[leftmargin=0.8cm,style=sameline]
\item[(1)] Procedures for detecting, containing, and remediating cybersecurity incidents affecting the Physical AI system;
\item[(2)] Criteria for determining when a cybersecurity incident constitutes a Physical AI adverse event reportable under \S~312.32(g);
\item[(3)] Communication procedures for notifying affected investigational sites, FDA, and other relevant parties; and
\item[(4)] Procedures for preserving forensic evidence from cybersecurity incidents for analysis and regulatory review.
\end{description}

[Physical AI adaptation added 17 March 2026.]

\subsection{\S~312.404 Physical AI Human Oversight Requirements}

(a) \textit{General oversight requirement.} All Physical AI-assisted clinical procedures involving investigational drugs shall be conducted under human oversight by a qualified investigator or subinvestigator. No Physical AI system shall administer an investigational drug to a human subject without human oversight, regardless of the system's classification under \S~312.401.

(b) \textit{Levels of oversight.} The level of human oversight required shall correspond to the Physical AI system's classification:

\begin{description}[leftmargin=0.8cm,style=sameline]
\item[(1)] \textit{Class I systems.} The investigator maintains full manual control and uses the Physical AI system's output as advisory information. No additional oversight requirements beyond standard clinical practice.
\item[(2)] \textit{Class II systems.} The investigator maintains continuous direct supervision of the Physical AI system during all drug administration activities. The investigator must be physically present in the procedure room, must have immediate access to manual override controls, and must be able to halt the system and assume manual control within a response time specified in the protocol (not to exceed 2 seconds for drug delivery systems and 500 milliseconds for surgical systems).
\item[(3)] \textit{Class III systems.} In addition to the Class II requirements, a second qualified individual shall be present during all drug administration procedures to serve as an independent safety monitor. The safety monitor's sole responsibility during the procedure shall be to observe the Physical AI system's performance and alert the supervising investigator to any anomalies. The protocol shall define the specific performance indicators the safety monitor is required to observe.
\end{description}

(c) \textit{Operator-to-system ratio.} No investigator or subinvestigator shall simultaneously supervise more than one Physical AI system performing drug administration procedures. The protocol may specify a higher operator-to-system ratio (i.e., more operators per system) based on procedure complexity or risk.

(d) \textit{Fatigue management.} The protocol shall include provisions to prevent operator fatigue from compromising human oversight effectiveness, including maximum continuous supervision periods and mandatory rest intervals for Physical AI system operators during extended procedures.

(e) \textit{Override and emergency stop.}

\begin{description}[leftmargin=0.8cm,style=sameline]
\item[(1)] Every Physical AI system used in clinical investigations shall be equipped with a physical emergency stop mechanism that is immediately accessible to the supervising investigator and that, when activated, brings the system to a safe state within a time period appropriate for the clinical procedure (not to exceed 500 milliseconds for all moving components);
\item[(2)] The emergency stop mechanism shall function independently of the Physical AI system's software and shall not be subject to software override or delay;
\item[(3)] The Physical AI system shall provide the supervising investigator with a manual override capability that allows the investigator to assume direct control of any system function at any time during a procedure; and
\item[(4)] The protocol shall define the criteria under which the investigator shall activate the emergency stop or manual override, including but not limited to: unexpected patient physiological response, Physical AI system behavior outside pre-specified parameters, loss of system sensor data, and loss of communication with the Physical AI system.
\end{description}

[Physical AI adaptation added 17 March 2026.]

\subsection{\S~312.405 Physical AI System Lifecycle Management}

(a) \textit{Configuration management.} The sponsor shall maintain configuration management records for each Physical AI system used in the investigation, documenting:

\begin{description}[leftmargin=0.8cm,style=sameline]
\item[(1)] The complete hardware configuration, including all components, serial numbers, firmware versions, and calibration dates;
\item[(2)] The complete software configuration, including operating system version, application software versions, AI/ML model versions and training data provenance, and all configuration parameters; and
\item[(3)] All changes to the hardware or software configuration, including the date of the change, the nature of the change, the rationale, the validation performed, and any required regulatory submissions under \S~312.30.
\end{description}

(b) \textit{AI/ML model management.} When the Physical AI system includes AI/ML models that influence drug administration decisions or actions:

\begin{description}[leftmargin=0.8cm,style=sameline]
\item[(1)] The sponsor shall document the training data, training methodology, performance metrics, and validation results for each AI/ML model;
\item[(2)] Model updates shall be managed in accordance with the PCCP submitted under \S~312.23(g)(vi), including pre-specified performance criteria for accepting or rejecting model updates;
\item[(3)] The sponsor shall monitor for model drift, data drift, and concept drift that could affect model performance in the clinical setting, and shall implement corrective actions when drift exceeds pre-specified thresholds; and
\item[(4)] The sponsor shall maintain a complete model version history, including the ability to revert to any previous model version if a new model version demonstrates unacceptable performance.
\end{description}

(c) \textit{Decommissioning.} When a Physical AI system is removed from a clinical investigation, the sponsor shall:

\begin{description}[leftmargin=0.8cm,style=sameline]
\item[(1)] Complete all required data archival, including transfer of telemetry data, system logs, and audit trails to the sponsor's long-term storage;
\item[(2)] Securely erase all patient data, investigational drug data, and access credentials from the Physical AI system;
\item[(3)] Revoke all network access, authentication tokens, and MCP server configurations associated with the system;
\item[(4)] Document the decommissioning in the Physical AI system maintenance record; and
\item[(5)] Retain the Physical AI system or key components for the record retention period specified in \S~312.57(f), or document the disposition of the system if it is returned to the manufacturer or otherwise disposed of.
\end{description}

[Physical AI adaptation added 17 March 2026.]

\clearpage

\section*{REFERENCES AND BIBLIOGRAPHY}

\addcontentsline{toc}{section}{References and Bibliography}

The following references informed the development of this Physical AI adaptation of 21 CFR Part 312. This bibliography includes the original regulatory sources, FDA guidance documents, relevant standards, and the Physical AI and oncology literature that provides the technical foundation for the adapted provisions.

\subsection*{Primary Regulatory Sources}

\begin{enumerate}
\item 21 CFR Part 312 --- Investigational New Drug Application. Code of Federal Regulations, Title 21, Chapter I, Subchapter D, Part 312. U.S. Food and Drug Administration.

\item Federal Food, Drug, and Cosmetic Act (FD\&C Act), 21 U.S.C. \S\S~301--399i, as amended.

\item Public Health Service Act, 42 U.S.C. \S~262 (Section 351), as amended.

\item 21 CFR Part 50 --- Protection of Human Subjects. Code of Federal Regulations, Title 21, Chapter I, Subchapter A.

\item 21 CFR Part 56 --- Institutional Review Boards. Code of Federal Regulations, Title 21, Chapter I, Subchapter A.

\item 21 CFR Part 11 --- Electronic Records; Electronic Signatures. Code of Federal Regulations, Title 21, Chapter I, Subchapter A.
\end{enumerate}

\subsection*{FDA Guidance Documents}

\begin{enumerate}[resume]
\item U.S. Food and Drug Administration. ``Artificial Intelligence and Machine Learning (AI/ML)-Enabled Device Software Functions: Lifecycle Management and Marketing Submission Recommendations.'' Draft Guidance, January 2025.

\item U.S. Food and Drug Administration. ``Marketing Submission Recommendations for a Predetermined Change Control Plan for Artificial Intelligence/Machine Learning (AI/ML)-Enabled Device Software Functions.'' Guidance for Industry, December 2024.

\item U.S. Food and Drug Administration. ``Cybersecurity in Medical Devices: Quality System Considerations and Content of Premarket Submissions.'' Guidance for Industry, September 2023.

\item U.S. Food and Drug Administration. ``Computer Software Assurance for Production and Quality System Software.'' Guidance for Industry, September 2022.

\item U.S. Food and Drug Administration. ``Clinical Decision Support Software.'' Guidance for Industry and FDA Staff, September 2022.

\item U.S. Food and Drug Administration. ``Content of Premarket Submissions for Device Software Functions.'' Guidance for Industry, June 2023.

\item U.S. Food and Drug Administration. ``Investigational Device Exemptions (IDEs) for Early Feasibility Medical Device Clinical Studies, Including Certain First in Human (FIH) Studies.'' Guidance for Industry, October 2013.
\end{enumerate}

\subsection*{Robotics and Physical AI Standards}

\begin{enumerate}[resume]
\item ISO 13482:2014. Robots and robotic devices --- Safety requirements for personal care robots. International Organization for Standardization.

\item ISO 10218-1:2011. Robots and robotic devices --- Safety requirements for industrial robots --- Part 1: Robots. International Organization for Standardization.

\item IEC 62304:2006/AMD 1:2015. Medical device software --- Software life cycle processes. International Electrotechnical Commission.

\item IEC 80001-1:2021. Application of risk management for IT-networks incorporating medical devices. International Electrotechnical Commission.

\item IEEE 7001-2021. IEEE Standard for Transparency of Autonomous Systems. Institute of Electrical and Electronics Engineers.

\item IEEE 7010-2020. IEEE Recommended Practice for Assessing the Impact of Autonomous and Intelligent Systems on Human Well-Being. Institute of Electrical and Electronics Engineers.

\item NIST AI 100-1. Artificial Intelligence Risk Management Framework (AI RMF 1.0). National Institute of Standards and Technology, January 2023.
\end{enumerate}

\subsection*{Physical AI and Simulation Literature}

\begin{enumerate}[resume]
\item Kawchak, K. ``Physical AI Oncology Trials: A Framework for Integrating Robotic Systems into Clinical Drug Investigations.'' GitHub Repository, 2025--2026. Available at: https://github.com/kevinkawchak/physical-ai-oncology-trials.

\item NVIDIA Corporation. ``Isaac Sim: Robotics Simulation and Synthetic Data Generation.'' NVIDIA Developer Documentation, 2024--2025.

\item NVIDIA Corporation. ``NVIDIA Cosmos: World Foundation Models for Physical AI.'' Technical Report, 2025.

\item Google DeepMind. ``Gemini Robotics: Bringing AI into the Physical World.'' Technical Report, March 2025.

\item Todorov, E., Erez, T., and Tassa, Y. ``MuJoCo: A physics engine for model-based control.'' In Proceedings of IEEE/RSJ International Conference on Intelligent Robots and Systems, 2012.

\item Makoviychuk, V., et al. ``Isaac Gym: High Performance GPU-Based Physics Simulation for Robot Learning.'' In Proceedings of the Neural Information Processing Systems (NeurIPS) Datasets and Benchmarks Track, 2021.

\item Tobin, J., et al. ``Domain Randomization for Transferring Deep Neural Networks from Simulation to the Real World.'' In Proceedings of IEEE/RSJ International Conference on Intelligent Robots and Systems, 2017.

\item Zhao, W., et al. ``Sim-to-Real Transfer in Deep Reinforcement Learning for Robotics: A Survey.'' IEEE Transactions on Neural Networks and Learning Systems, 2020.
\end{enumerate}

\subsection*{Oncology Robotics and Drug Delivery}

\begin{enumerate}[resume]
\item Trejos, A.L., et al. ``Robot-assisted minimally invasive surgery and interventional oncology.'' In Handbook of Robotic and Image-Guided Surgery, Elsevier, 2020.

\item Fichtinger, G., et al. ``Robotic assistance for ultrasound-guided brachytherapy.'' Medical Image Analysis, 2008.

\item Podder, T.K., et al. ``AAPM and GEC-ESTRO guidelines for image-guided robotic brachytherapy: Report of Task Group 192.'' Medical Physics, 2014.

\item Yang, G.-Z., et al. ``Medical robotics --- Regulatory, ethical, and legal considerations for increasing levels of autonomy.'' Science Robotics, 2017.

\item Dupont, P.E., et al. ``A decade retrospective of medical robotics research from 2010 to 2020.'' Science Robotics, 2021.
\end{enumerate}

\subsection*{AI/ML in Clinical Trials}

\begin{enumerate}[resume]
\item Topol, E.J. ``High-performance medicine: the convergence of human and artificial intelligence.'' Nature Medicine, 25(1):44--56, 2019.

\item Liu, X., et al. ``Reporting guidelines for clinical trial reports for interventions involving artificial intelligence: the CONSORT-AI extension.'' The Lancet Digital Health, 2(10):e537--e548, 2020.

\item Cruz Rivera, S., et al. ``Guidelines for clinical trial protocols for interventions involving artificial intelligence: the SPIRIT-AI extension.'' The Lancet Digital Health, 2(10):e549--e560, 2020.

\item U.S. Food and Drug Administration. ``Using Artificial Intelligence and Machine Learning in the Development of Drug and Biological Products.'' Discussion Paper, May 2023.

\item Anthropic. ``Model Card and Evaluations for Claude Models.'' Technical Documentation, 2024--2025.
\end{enumerate}

\subsection*{Cybersecurity in Medical Systems}

\begin{enumerate}[resume]
\item NIST Special Publication 800-53, Rev. 5. ``Security and Privacy Controls for Information Systems and Organizations.'' National Institute of Standards and Technology, September 2020.

\item NIST Special Publication 800-183. ``Networks of `Things'.'' National Institute of Standards and Technology, July 2016.

\item Health Care Industry Cybersecurity Task Force. ``Report on Improving Cybersecurity in the Health Care Industry.'' U.S. Department of Health and Human Services, June 2017.

\item Medical Device Innovation Consortium (MDIC). ``Medical Device Cybersecurity: Regional Incident Preparedness and Response Playbook.'' 2018.
\end{enumerate}

\subsection*{Digital Twins and Treatment Planning}

\begin{enumerate}[resume]
\item Lal, A., et al. ``Digital twins and AI in clinical trials.'' Nature Medicine, 30:3405--3407, 2024.

\item Corral-Acero, J., et al. ``The `Digital Twin' to enable the vision of precision cardiology.'' European Heart Journal, 41(48):4556--4564, 2020.

\item Hernandez-Boussard, T., et al. ``Digital twins for predictive oncology will be a paradigm shift for precision cancer care.'' Nature Medicine, 27:2065--2066, 2021.

\item Venkatesh, K.P., et al. ``Health digital twins as tools for precision medicine: Considerations for computation, implementation, and regulation.'' npj Digital Medicine, 5:150, 2022.
\end{enumerate}

\vspace{1cm}

\noindent\rule{\textwidth}{0.4pt}

\vspace{0.5cm}

\begin{center}
\textbf{END OF ADAPTED REGULATION}

\vspace{0.3cm}

\textit{This adaptation of 21 CFR Part 312 for Physical AI systems in oncology clinical trials was prepared as part of the Physical AI Oncology Trials project.}

\vspace{0.2cm}

\textit{Version 1.0 --- 17 March 2026}

\vspace{0.2cm}

\textit{This document is intended for research and educational purposes. It does not represent official FDA regulation or guidance.}
\end{center}

\end{document}
