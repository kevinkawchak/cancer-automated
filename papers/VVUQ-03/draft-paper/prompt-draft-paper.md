## prompt-draft-paper

Write new VVUQ Physical AI oncology trial bill instructions based primarily on prior author projects in kevinkawchak/cancer-automated/tree/main/papers/VVUQ-01/final-paper, cancer-automated/tree/main/papers/VVUQ-02/final-paper, and physical-ai-oncology-trials/tree/main/national-platform/new_paper/final_paper, and referencing external authors within these works. Reference other relevant sources from VVUQREF and LEGISLATION below.

“THESIS”
Physical AI oncology trials require rigorous AI VVUQ code automation methods regarding new robot-patient interactions. State of the art repository based AI models are also capable of synthesizing VVUQ code generation and execution results into public documents to improve and accelerate the legislative process. This new bill aims to prioritize and solidify a law that requires the code verification process ahead of code generation to ensure patient safety and efficacy.
“THESIS”

“KEY DIRECTORIES”
kevinkawchak/physical-ai-oncology-trials/tree/main/national-platform/new_paper/final_paper
kevinkawchak/cancer-automated/tree/main/papers/VVUQ-01/full-paper
kevinkawchak/cancer-automated/tree/main/papers/VVUQ-02/final-paper
“KEY DIRECTORIES”

Themes (don’t follow structure for paper):
A. Physical AI Oncology Trial VVUQ Bill
- Rigor is above generated code itself
- Legislation is required for patient safety and efficacy
- VVUQ is essential for high stakes robotic humanoid and on-site surgeries
- VVUQ automation also brings inherit speed, cost benefits vs. traditional AI 
B. Evidence to be included in new bill
- 2 author VVUQ studies proved LLMs are appropriate for code verifications 
- 2 author studies proved practical VVUQ codegen/execution with External Standards
- Physical AI VVUQ supported by 2 author standards and 5 trial/sponsor/mobile simulations

Be sure to include instructions regarding USL and PSL standards that positively affect the VVUQ process synergistically from physical-ai-oncology-trials/tree/main/national-platform/new_paper/final_paper. Be sure to discuss the substantial External Standard incorporations found in cancer-automated/tree/main/papers/VVUQ-02/final-paper.

Utilize the paper template from cancer-automated/tree/main/papers/VVUQ-03/template-paper to now include your own processing instructions and details regarding which directories and files to use in brackets under each specific section; but do not process your own instructions for each section. Direct context from the paper template must first be removed, with new section names (1 section per tex file) to be created, each with their own bracketed instructions and exact files to use in a future prompt. Your new draft paper with these instructions is to be placed into cancer-automated/tree/main/papers/VVUQ-03/draft-paper.

Your instructions must use KEY DIRECTORIES files (both author and external sources) and your knowledge to address the 4 following main points:
1. Algorithm Documentation
2. Attestations & Compliance Statements
3. Prior Law References
4. Must include: Supporting Documentation (Not Physically Attached, But Referenced)

The following laws all must be incorporated into the current project and cited in .bib correctly.
Federal Laws Commonly Referenced:
1. 42 U.S.C. § 1395y - Medicare determinations of medical necessity and appropriateness
2. 45 CFR Parts 160, 164 - HIPAA Privacy and Security Rules
3. 21 CFR Part 860-889 - FDA Medical Device regulations
4. 26 U.S.C. - Federal antidiscrimination laws (Title VI, Americans with Disabilities Act provisions)

If relevant the bill should also reference. Be sure to address Texas, California, New York, and Florida specific legislation.
* New York's Assembly Bill A9149 requires health insurers and HMOs to submit the actual artificial intelligence-based algorithms and training data sets being used in the utilization review process to the state Department of Financial Services, which then certifies that these algorithms and training data sets minimize bias risk based on protected characteristics and adhere to evidence-based clinical guidelines.
* Texas's Senate Bill 1822 originally required insurers to submit the actual AI algorithm and its training datasets to the Texas Department of Insurance, though the committee substitute version modified this to require submission of algorithms only if the commissioner determines additional documentation is needed based on noncompliance concerns.

Incorporate these guidelines with the project in your new bill, where relevant.
A. Policy development before drafting
Usually needed:
•	Policy memo or concept paper.
•	Problem statement and current-law gap.
•	Current-law research: FD&C Act, Medicare, PHSA, HIPAA, state insurance/medical-practice law, civil-rights/nondiscrimination law.
•	Stakeholder materials: health systems, clinicians, patient groups, AI developers, payers, device makers, regulators.
•	Technical definitions: AI, generative AI, algorithm, high-risk AI, AI-enabled device software function, clinical decision support, utilization review tool.
•	Implementation choices: disclosure, auditability, human review, FDA review, CMS reimbursement, grant program, reporting duty, enforcement authority.
•	Budget/funding plan and any offsets.
•	Section-by-section explanation.
•	Draft statutory text
Not usually needed: executable code, model weights, training datasets, or Git repositories.

Sections must provide instructions in [brackets] that includes the exact repository directories and file names (from KEY DIRECTORIES below; be sure to read directory READMEs first), what to process, how to process, how to use files together synergistically, etc. for future Claude Code 4.8 1M Max processing. Do not process your instructions for each of the paper sections, instead only provide the exact instructions, directories, and file names needed for Claude Code to process in a future prompt. Do not generate or include any images. Tables, directory names, and file names are ok for use where appropriate.

It is important that your instructions specify that a comprehensive amount of context for each section be implemented, shouldn’t have too many long file names, and should have the majority of the file names in tables appropriately abbreviated where necessary (make sure the longer path is designated towards the top of tables, where appropriate). In other words, legislation should be publication quality, and not state obvious information readily identified in tables or images (reference tables where necessary). Legislation should look like a top human author wrote it, with comprehensive ideas connect throughout the paper. Utilize the following directories throughout your instructions, where relevant.
 
Do not approximate or shorten any of the required steps. Be sure to describe any limitations of what could not be run, had to be approximated, etc. from the codegen and execution steps.

It is also important to include the significant reference: code generation processing feat and prior execution of the 1700+ line, four competitor results file in cancer-automated/blob/main/papers/VVUQ-02/codegen/results/comparison.json. Additionally, feature the substantial code generation processing and your execution in documentation regarding the 1000 line csv of robot positional data of hands, 5 fingers, arms, etc. with no repetitive data in cancer-automated/blob/main/papers/VVUQ-02/codegen/data/sample_h2_sensor.csv.

1 commit is required for each of the following (main.tex, .sty, .bib, and README); and 1 commit is required for each of the paper’s .tex sections (1 .tex file per section) that each correspond to main.tex. Commit to branch after each commit is finished in real time - don’t hold commits until the draft paper is finished. Don’t insert all text into one file. For the 2nd to last commit, fix all of your errors for all files. For the last commit, perform the remaining repository updates defined below. All commits should be created within 1 PR.

Each commit by you must be performed autonomously, and be uploaded in real time to GitHub each time a commit is finished (each commit is sent separately to make up the single PR). The user cannot interact, and all commits must be processed sequentially by you autonomously. Do not stall, ask questions, or go into plan mode. 

Again, you are not processing any of the files in the attached directories, but setting up the paper and sections, then including bracketed instructions for each section, along with exact directory and file names for AI to process in the future.

Your outputs should be in a single LaTeX zip of all files that will compile correctly as a pdf in Overleaf. Don’t compile the pdf on your own. Only provide the LaTeX zip file to cancer-automated/tree/main/papers/VVUQ-03/draft-paper.

Mentioning of FDA and other governing bodies should be respectful, yet opportunistic to advance the new field of Physical AI oncology trials. The United States needs to remain Number 1 in the world regarding surgical humanoid VVUQ with external standards for patient safety, efficacy, and speed benefits in clinical trials.

Essentially, your new LaTeX paper draft should provide a significant head start so that a future Claude Code request can focus on processing the instructions in brackets using the files in the current repository specified by you. In this new paper draft output, you have to specify exact files and folders to make downstream processing steps as accurate and efficient as possible. Do not stall, ask questions, or go into plan mode.

Future Claude Code processing will create a final 70+ page paper, so your preparations and instructions are important for a high quality final paper in the future. Double check that both repository and paper DOIs are clickable in references.

Please specify that: DOI numbers and actual URLs must be included in .bib, and must also show up in bibliography correctly. Include URLs for both GitHub and Zenodo for repositories (that will both clickable in references in the future). It is critical that the bibliography references have actual DOI numbers and corresponding URLs without loss of any .bib detail. Don’t use “howpublished”, and make sure no duplicate links are shown. 

The README in cancer-automated/tree/main/papers/VVUQ-03/draft-paper must also include common components such as DOI badges, repository structure, and ASCII diagrams where appropriate. Only commit to kevinkawchak/cancer-automated, and not to kevinkawchak/physical-ai-oncology-trials or other repositories.

For your template: specify in your instructions to avoid large white empty spaces without text. Where large spacing between words exist throughout the body of text.: modify \raggedright spacing to make positioning between words look equally and properly spaced. Make sure text doesn’t run off the right side of the page anywhere. Include instructions to avoid lines with a single or two words. All tables need to use a similar format for each column width as in this example: The contents of every table cell must be properly left aligned using the example format:{>{\raggedright\arraybackslash}p{2cm}. Every width value must have a prepended \raggedright\arraybackslash to ensure no big gaps between words in tables.

Specify in your instructions to avoid single lines separate form the main paragraph on the next page. Perform the final formatting steps that a senior author would take by correcting white space formatting and removing and/or adding relevant text to make each section and page look properly formatted and self standing by itself. (Don’t overcrowd the page with text, some white space formatting is ok). Make sure to correct all incorrect symbols such as SS into “§” where relevant. Use single dashes, but no em dashes, double dashes, or triple dashes throughout the paper. Utilize the same text color formatting as in the prior template.

Double check and correct incorrect bill names (if any). Check to see if differing governance exists, then update titles and content where appropriate.

“COVER PAGE” 
“VVUQ Physical AI Oncology Trial Bil” (Replacement Title, 1 Line)
“Draft 1.0” (Replacement Bold Text, 1 Line)
“CEO Kevin Kawchak (Hyperlink: https://orcid.org/0009-0007-5457-8667), ChemicalQDevice, kevink@chemicalqdevice.com (Hyperlink)”
“Notice: This draft was adapted from original CFR documents in the public domain. The original ICH document is copyrighted and may be used, reproduced, incorporated into other works, adapted, modified, translated or distributed under a public license. This current work is not endorsed or sponsored by CFR, ICH, or FDA.” (Plain Text, Multi-Line)
[1 Blank Line]
“Disclaimer: This work is independent and is not endorsed, sponsored, or approved by any trial sponsor, CRO, site, IRB, regulator, or medical society; and was adapted using Claude Code Opus 4.6.” (Plain Text, Multi-Line)
[One Blank Line]
10.5281/zenodo.xxxxxxxx (with Hyperlink: https://doi.org/10.5281/zenodo.xxxxxxxx)(Plain Text, 1 Line)
[Several Blank Lines]
San Diego (Bold Text)
[Several Blank Lines]
“May 30, 2026” (Plain Text)
“COVER PAGE” 

Inside cancer-automated/tree/main/papers/VVUQ-03/draft-paper: Create a prompt-draft-paper.md that uses a “## prompt-draft-paper” heading followed by this entire prompt word-for-word. Create a separate output-draft-paper.md that uses a “## output-draft-paper” heading followed by the entire output of this prompt (containing the Claude markdown output, not the code files).

Include the draft-paper name in GitHub documentation headings and release notes. Be sure to fix and address errors that would cause failed checks for the single pull request (such as for lint and Python environment issues to avoid the following error during final checks): "3 failing checks
x Cl / lint-and-format (3.10) (pull...
x Cl / lint-and-format (3.11) (pull...
x Cl / lint-and-format (3.12) (pull... " Place the new release notes in releases.md under main using the format below. Update other relevant documentation such as project structures. Update the main Readme diagrams, repository structure, etc. where necessary. Update the CHANGELOG.md (v1.3.0).

"FORMAT"
Release title
v1.3.0 - [Fill in Title Here]

## Summary

## Features

## Contributors
@kevinkawchak
@claude
@openai
@google-gemini

## Notes
“FORMAT”

“VVUQREF”
@misc{kawchak_2026_20421754,
  author       = {Kawchak, Kevin},
  title        = {Mobile Pancreatic Cancer Unitree H2 Surgical
                   Humanoid with Priority VVUQ
                  },
  month        = may,
  year         = 2026,
  publisher    = {Zenodo},
  doi          = {10.5281/zenodo.20421754},
  url          = {https://doi.org/10.5281/zenodo.20421754},
}
@misc{kawchak_2026_20372501,
  author       = {Kawchak, Kevin},
  title        = {VVUQ Oncology Clinical Trial LLM Verification
                   Automation Priority over Existing Generated Code
                  },
  month        = may,
  year         = 2026,
  publisher    = {Zenodo},
  doi          = {10.5281/zenodo.20372501},
  url          = {https://doi.org/10.5281/zenodo.20372501},
}
“VVUQREF”

“LEGISLATION”
@misc{kawchak_2026_20045457,
  author       = {Kawchak, Kevin},
  title        = {Patient Priority of Proposed U.S. Bills for
                   Physical AI Oncology Clinical Trials
                  },
  month        = may,
  year         = 2026,
  publisher    = {Zenodo},
  doi          = {10.5281/zenodo.20045457},
  url          = {https://doi.org/10.5281/zenodo.20045457},
}
@misc{kawchak_2026_19244918,
  author       = {Kawchak, Kevin},
  title        = {National Platform for Physical AI Oncology Trials},
  month        = mar,
  year         = 2026,
  publisher    = {Zenodo},
  doi          = {10.5281/zenodo.19244918},
  url          = {https://doi.org/10.5281/zenodo.19244918},
}
@misc{kawchak_2026_19176370,
  author       = {Kawchak, Kevin},
  title        = {Physical AI Oncology Clinical Trial Site Complete
                   Documentation Package
                  },
  month        = mar,
  year         = 2026,
  publisher    = {Zenodo},
  doi          = {10.5281/zenodo.19176370},
  url          = {https://doi.org/10.5281/zenodo.19176370},
}
@misc{kawchak_2026_19057628,
  author       = {Kawchak, Kevin},
  title        = {Adaption: 21 CFR Part 312, End-to-End Physical AI
                   Oncology Clinical Trial Unification
                  },
  month        = mar,
  year         = 2026,
  publisher    = {Zenodo},
  doi          = {10.5281/zenodo.19057628},
  url          = {https://doi.org/10.5281/zenodo.19057628},
}
@misc{kawchak_2026_19040707,
  author       = {Kawchak, Kevin},
  title        = {Adaption: 21 CFR Part 50, End-to-End Physical AI
                   Oncology Clinical Trial Unification
                  },
  month        = mar,
  year         = 2026,
  publisher    = {Zenodo},
  doi          = {10.5281/zenodo.19040707},
  url          = {https://doi.org/10.5281/zenodo.19040707},
}
@misc{kawchak_2026_18973368,
  author       = {Kawchak, Kevin},
  title        = {Adaption: ICH Harmonised Guideline, End-to-End
                   Physical AI Oncology Clinical Trial Unification
                  },
  month        = mar,
  year         = 2026,
  publisher    = {Zenodo},
  doi          = {10.5281/zenodo.18973368},
  url          = {https://doi.org/10.5281/zenodo.18973368},
}
“LEGISLATION”
