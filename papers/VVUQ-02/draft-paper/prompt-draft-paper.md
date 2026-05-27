## prompt-draft-paper

Utilize the paper template from kevinkawchak/cancer-automated/tree/main/papers/VVUQ-02/templates/Template_04 to now include your own processing instructions and details regarding which directories and files to use in brackets under each specific section; but do not process your own instructions for each section. Your new draft paper with these instructions is to be placed into cancer-automated/tree/main/papers/VVUQ-02/draft-paper.

Sections must provide instructions in [brackets] that includes the exact repository directories and file names (from the available directories in Research Directories below; be sure to read directory READMEs first), what to process, how to process, how to use files together synergistically, etc. for future Claude Code 4.7 1M Max processing. Do not process your instructions for each of the paper sections, instead only provide the exact instructions, directories, and file names needed for Claude Code to process in a future prompt. 

It is important that your instructions specify that a comprehensive amount of context for each section be implemented, shouldn't have too many long file names, and should have the majority of the file names in tables appropriately abbreviated where necessary (make sure the longer path is designated towards the top of tables, where appropriate). In other words, paragraphs should be publication quality, and not state obvious information readily identified in tables or images (reference tables where necessary). Paragraphs should look like a top human author wrote it, with comprehensive ideas connect throughout the paper. Utilize the following directories throughout your instructions, where relevant.

"Research Directories"
1. cancer-automated/tree/main/papers/VVUQ-02 (You are responsible for all subdirectories) (Create references with working URLs based on external standards and other regulations (must include several external standard sources), including cancer-automated/tree/main/papers/VVUQ-02/inputs and subdirectories.)
2. cancer-automated/tree/main/papers/VVUQ-01/final-paper (also use for implementing relevant references)
"Research Directories"

Do not approximate or shorten any of the required steps. Be sure to describe any limitations of what could not be run, had to be approximated, etc. from the codegen and execution steps.

It is also important to include the significant codegen processing feat and prior execution of the 1700+ line, four competitor results file in cancer-automated/blob/main/papers/VVUQ-02/codegen/results/comparison.json. Additionally, feature the substantial code generation processing and your execution in documentation regarding the 1000 line csv of robot positional data of hands, 5 fingers, arms, etc. with no repetitive data in cancer-automated/blob/main/papers/VVUQ-02/codegen/data/sample_h2_sensor.csv.

"THESIS"
The robotic code assurance process, not code generation, is the substantial and decision bearing part of the AI workflow, holding VVUQ to a higher standard than code itself. These safety measures will ensure upcoming physical AI oncology trial developments are faster, less expensive, and more beneficial towards patients than conventional verifications.
"THESIS"

1 commit is required for each of the following (main.tex, .sty, .bib, and README); and 1 commit is required for each of the paper's .tex sections (1 .tex file per section) that each correspond to main.tex. For the 2nd to last commit, fix all of your errors for all files. For the last commit, perform the remaining repository updates defined below. All commits should be created within 1 PR. 

Each commit by you must be performed autonomously, and be uploaded in real time to GitHub each time a commit is finished (each commit is sent separately to make up the single PR). The user cannot interact, and all commits must be processed sequentially by you autonomously. Do not stall, ask questions, or go into plan mode. 

Keep in mind this project is for the future of patient safety, so present these works within the project as checking steps off, so the industry does not have to. You should also be able to write practical insights regarding how close to real-life the application is.

The following 5 file image IDs and corresponding directory data should be utilized in your instructions, as they represent significant evidence towards fulfilling paper objectives. Utilize cancer-automated/tree/main/papers/VVUQ-02/image-instruct, and additional data from the python scripts in cancer-automated/tree/main/papers/VVUQ-02/imagegen. (Simply use the data, don't create the images).
Utilize context from:
Image 03: 10 VVUQ gates forest plot
Image 04: Matrix of 10 VVUQ gates vs. exact regulations
Image 05: Clinical/standards wheel
Image 11: Safety bands, 1000 rows, 2 humanoid hands force, distance
Image 13: Cost assessment waterfall

Be sure to utilize the figure code as a placeholder for each of the 5 images (the actual images will be added by the author at a later time). Include a logical 1 line caption, and a brief label without spaces, dashes, underscores, etc. for each figure code. Provide instructions to use \autoref in the body text for each of the images.
"FIGURE CODE"
\begin{figure}[H]
   \hspace{-0.95cm}
   \includegraphics[width=1.1\linewidth, trim={0 0 0 0}, clip]{Images/}
    % \vspace{-0.25cm}
    \caption{}
    \label{}
\end{figure}
"FIGURE CODE"

Disperse your instructions and specific directories and file names appropriately throughout the paper using the following sections:
-Abstract (Include instructions that there should be both an overview that captures the code instructions, code generations/code execution, draft generation, full paper production, and also provides important result metrics detail towards the end. It is also important that the exact strengths of utilizing external standards for this study are. Provide instructions to keep abstract under 250 words.
-Introduction (Be sure to briefly discuss the principles of VVUQ in based on the context of oncology clinical trials such as this example: Verification: Asks: "Did we build the code correctly?", Validation: Asks: "Did we build the right model?", Uncertainty Quantification (UQ): Asks: "How confident are we in the results?") Also include the developments from cancer-automated/tree/main/papers/VVUQ-01/final-paper that led to this paper.
-Methods (Include relevant sections from cancer-automated/blob/main/papers/VVUQ-02/execution/01-foundation/environment-and-verification.md)(Include external standards anchored here: cancer-automated/tree/main/papers/VVUQ-02/execution/02-pipeline)
-Results
-Discussion (Discuss the VVUQ tests performed: cancer-automated/tree/main/papers/VVUQ-02/codegen/tests)(Discuss the quality and confidence of the results to the external standards such as ASME V&V 40-2018, NASA-STD-7009, IEC 80601-2-77, etc.)
-Limitations and Future Work (Future work should focus on adapting this 10 robot VVUQ automation application with external standards throughout all oncology clinical trials due to speed, quality, and cost benefits)
-Conclusions
-References (There should be at least 20 references based on relevant bibtex entries from the prior VVUQ-01/final-paper and external standards/regulations in VVUQ-02. The external standards/regulations should be well represented in references). Your references should be polished and final.
-Remaining Sections

Again, you are not processing any of the files in the attached directories, but setting up the paper and sections, then including bracketed instructions for each section, along with exact directory and file names for AI to process in the future.

Your outputs should be in a single LaTeX zip of all files that will compile correctly as a pdf in Overleaf. Don't compile the pdf on your own. Only provide the LaTeX zip file to cancer-automated/tree/main/papers/VVUQ-02/draft-paper.

Mentioning of FDA and other governing bodies should be respectful, yet opportunistic to advance the new field of Physical AI oncology trials. The United States needs to remain Number 1 in the world regarding surgical humanoid VVUQ with external standards for patient safety, efficacy, and speed benefits in clinical trials.

Don't directly copy context from any of the original paper template or cancer-automated/tree/main/papers/VVUQ-01/final-paper context (except for bibtex entries); only use context needed for this current paper based on the provided directory locations. You will need to define and set up the entire paper structure (with Title, table of contents, sections, etc.).  

Essentially, your new LaTeX paper draft should provide a significant head start so that a future Claude Code request can focus on processing the instructions in brackets using the files in the current repository specified by you. In this new paper draft output, you have to specify exact files and folders from to make downstream processing steps as accurate and efficient as possible. Do not stall, ask questions, or go into plan mode.

Future Claude Code processing will create a final 70+ page paper, so your preparations and instructions are important for a high quality final paper in the future. Double check that both repository and paper DOIs are clickable in references.

Please specify that: DOI numbers and actual URLs must be included in .bib, and must also show up in bibliography correctly. Include URLs for both GitHub and Zenodo for repositories (that will both clickable in references in the future). It is critical that the bibliography references have actual DOI numbers and corresponding URLs without loss of any .bib detail. Don't use "howpublished", and make sure no duplicate links are shown. 

Each commit by you must be performed autonomously, and be uploaded in real time to GitHub each time a commit is finished (each commit is sent separately to make up the single PR). The user cannot interact, and all commits must be processed sequentially by you autonomously.  

The README in cancer-automated/tree/main/papers/VVUQ-02/draft-paper must also include common components such as DOI badges, repository structure, and ASCII diagrams where appropriate. Only commit to kevinkawchak/cancer-automated, and not to kevinkawchak/physical-ai-oncology-trials or other repositories.

For your template: specify in your instructions to avoid large white empty spaces without text. Where large spacing between words exist throughout the body of text.: modify \raggedright spacing to make positioning between words look equally and properly spaced. Make sure text doesn't run off the right side of the page anywhere. Include instructions to avoid lines with a single or two words. All tables need to use a similar format for each column width as in this example: The contents of every table cell must be properly left aligned using the example format:{>{\raggedright\arraybackslash}p{2cm}. Every width value must have a prepended \raggedright\arraybackslash to ensure no big gaps between words in tables.

Specify in your instructions to avoid single lines separate form the main paragraph on the next page. Perform the final formatting steps that a senior author would take by correcting white space formatting and removing and/or adding relevant text to make each section and page look properly formatted and self standing by itself. (Don't overcrowd the page with text, some white space formatting is ok). Make sure to correct all incorrect symbols such as SS into "§" where relevant. Use single dashes, but no em dashes, double dashes, or triple dashes throughout the paper. Utilize the same text color formatting as in the prior template.

Inside cancer-automated/tree/main/papers/VVUQ-02/draft-paper: Create a prompt-draft-paper.md that uses a "## prompt-draft-paper" heading followed by this entire prompt word-for-word. Create a separate output-draft-paper.md that uses a "## output-draft-paper" heading followed by the entire output of this prompt (containing the Claude markdown output, not the code files).

"BibTeX" (include as prior VVUQ paper)
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
"BibTeX"

"TITLE PAGE" 
"10 Mobile Pancreatic Cancer Unitree H2 Surgical Humanoids: VVUQ Processing Priority over Code Generation" (Replacement Title)
"Kevin Kawchak" "https://orcid.org/0009-0007-5457-8667" (use template's green Orcid logo and link) (1 Line)
"CEO ChemicalQDevice" (1 Line)
"10.5281/zenodo.xxxxxxxx" (with hyperlink: https://doi.org/10.5281/zenodo.xxxxxxxx) (1 Line) 
"May 28, 2026" (1 Line)
"Disclaimer: This work is independent and not endorsed or sponsored by trial sponsors, FDA, CRO, site, IRB, regulator, or medical society; and was generated using Artificial Intelligence." (Use below the abstract) (2 Lines)
[Complete The Abstract]
[Add Appropriate Keywords] (1 line, don't use an underline)
[Start Introduction] [Finish Intro]
[Start Table of Contents] [Finish TOC]
[BODY]
[REFERENCES]
[BACK MATTER]
"TITLE PAGE" 

"REMAINING PAPER SECTIONS"
Acknowledgments
The author would like to acknowledge Anthropic for providing access to Claude Code for instruction, code, execution, along with the paper generation process; OpenAI for providing access to ChatGPT for deep research summaries, and Google Gemini AI Overview for additional search assistance.

Ethical disclosures
The author of the article declares no competing interests.

Rights and permissions
This article is distributed under the terms of the Creative Commons Attribution 4.0 International License (CC BY 4.0), which permits unrestricted use, distribution, and reproduction in any medium, provided the original author(s) and source are properly credited, a link to the Creative Commons license is provided, and any modifications made are indicated. To view a copy of this license, visit https://creativecommons.org/licenses/by/4.0/.

Cite this article
Kawchak K. 10 Mobile Pancreatic Cancer Unitree H2 Surgical Humanoids: VVUQ Processing Priority over Code Generation. Zenodo. 2026; 10.5281/zenodo.xxxxxxxx.
"REMAINING PAPER SECTIONS"

Be sure to fix and address errors that would cause failed checks for the single pull request (such as for lint and Python environment issues to avoid the following error during final checks): "3 failing checks
x Cl / lint-and-format (3.10) (pull...
x Cl / lint-and-format (3.11) (pull...
x Cl / lint-and-format (3.12) (pull... " Place the new release notes in releases.md under main using the format below. Update other relevant documentation such as project structures. Update the main Readme diagrams, repository structure, etc. where necessary. Update the CHANGELOG.md (v1.1.0).

"FORMAT"
Release title
v1.1.0 - [Fill in Title Here]

## Summary

## Features

## Contributors
@kevinkawchak
@claude
@openai
@google-gemini

## Notes
"FORMAT"
