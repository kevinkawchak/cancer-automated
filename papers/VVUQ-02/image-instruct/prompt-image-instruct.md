## prompt-image-instruct

Your goal is to generate the following comprehensive image instructions based on kevinkawchak/cancer-automated/tree/main/papers/VVUQ-02/codegen and subdirectories (codegen) plus cancer-automated/tree/main/papers/VVUQ-02/execution and subdirectories (execution). Place the instructions into cancer-automated/tree/main/papers/VVUQ-02/image-instruct and relevant subdirectories (over-write this directory’s prior image instructions), along with a comprehensive README.md. 

There needs to be 15 image instructions based on code generation (v0.7.0) and code execution (v0.8.0). Individual instructions can be based on only codegen files, or only execution files, or both. Your instructions must specify that each of the generated images be full-size and portrait. You are not generating new images, but only writing instructions that will be used to generate matplotlib py scripts and 300 dpi png files at a future date. Do not use dark mode for any of the image instruction output types.

Your instructions must specify exactly how Claude Code Opus 4.7 (1M) Max will process  your instructions, and the exact directory names and file names to utilize throughout the entire cancer-automated/tree/main/papers/VVUQ-02 directory. Don’t commit anything to physical-ai-oncology-trials or other repositories.

Use 1 commit per image instruction for 15 commits across 1 created PR. For the 16th commit, focus on error fixes of all image instructions. For the 17th commit, perform the remaining repository updates defined below.

Your comprehensive image instructions should specify exact papers/VVUQ-02 codegen and execution directories and files to use. Make sure figures are professionally colored. (Pick 15 of the 20 figure types based on best data availability and figure relevancy) (Use identical figure types only when necessary)
1) Grouped bar chart
2) Line plot: uncertainty bands or error bars
3) Box plot or violin plot
4) Scatter / parity / bubble plot
5) Heatmap / matrix plot
6) Kaplan–Meier survival curve 
7) Waterfall plot 
8) Forest plot 
9) Swimmer or spider plot
10) Workflow / pipeline / flow diagram
11) Treemap
12) Value proposition
13) Financial assessment
14) Funnel plot 
15) Wheel diagram
16) Scatter plot / regression plot
17) ROC curve
18) Dot plot / strip plot
19) Pie / donut chart
20) Mind map

“DATA AVAILABILITY” (6 of 15 figures must be based on the following data)
- 1 Figure: Include 172 tests in a figure: cancer-automated/blob/main/papers/VVUQ-02/execution/01-foundation/test-suite.md
- 1 Figure: “External standards anchored here” - use this information type throughout directories such as this directory: must all be represented in an image: cancer-automated/tree/main/papers/VVUQ-02/execution/02-pipeline
- 1 Figure: The 10 gates and their thresholds must be included: cancer-automated/tree/main/papers/VVUQ-02/execution/03-vvuq
- 1 Figure: Clinical external standards and regulatory relevancies must be included (include subdirectories): cancer-automated/tree/main/papers/VVUQ-02/inputs
- 1 Figure: Awesome, feature this 1000 row H2 sensor data: cancer-automated/blob/main/papers/VVUQ-02/codegen/data/sample_h2_sensor.csv
- 1 Figure: Awesome, 2nd Place Mobile Humanoid 1700 lines of code, 4 Competitors: cancer-automated/blob/main/papers/VVUQ-02/codegen/results/comparison.json
“DATA AVAILABILITY”

The 15 final image instructions you chose must show substantial planning and be publication ready quality. Do not output instructions for basic bar charts, pi charts, and line charts. Specify professionally coded Python scripts using matplotlib for 300 dpi outputs to be written in the future - making sure text, boxes, text boxes, headers, footers, legends, and other components to correctly align, with no additional positioning needed by the user. 

The README in cancer-automated/tree/main/papers/VVUQ-02/image-instruct must also include common components such as DOI badges, repository structure, and ASCII diagrams where appropriate. The image-instruct directory README.md needs to cover the basics of the project and summarize the file generation outcomes as a basis for a technical paper in the future. Only commit to kevinkawchak/cancer-automated, and not to kevinkawchak/physical-ai-oncology-trials or other repositories.

“THESIS”
The robotic code assurance process, not code generation, is the substantial and decision bearing part of the AI workflow, holding VVUQ to a higher standard than code itself. These safety measures will ensure upcoming physical AI oncology trial deliverables are faster, less expensive, and more beneficial towards patients than conventional verifications.
“THESIS”

Inside cancer-automated/tree/main/papers/VVUQ-02/image-instruct: Create a prompt-image-instruct.md that uses a “## prompt-image-instruct” heading followed by this entire prompt word-for-word. Create a separate output-image-instruct.md that uses a “## output-image-instruct” heading followed by the entire output of this prompt (containing the Claude markdown output, not the code files).

In later commits, update cancer-automated/blob/main/README.md repository structures, badges, ASCII diagrams and toc, and other affected areas in the repository (this is the only repository that needs to be edited). Add a short summary for this update above the previous summary. Don’t include any images, mermaid diagrams, or colored images.  

Each commit by you must be performed autonomously, and be uploaded in real time to GitHub each time a set of files are created (each commit is sent separately to make up the single PR). The user cannot interact, and all commits must be processed sequentially by you autonomously. Do not stall, ask questions, or go into plan mode.

Make sure to utilize correct symbols in images such as SS into “§” where relevant. Use single dashes, but no em dashes, double dashes, or triple dashes throughout the images. Use text that can be seen clearly by humans against the white background.

Do not approximate or shorten taking any of the required steps. Be sure to correctly process all of the repository files correctly. Do not approximate or shorten any of the required steps. Be sure to include images based on the key directories below.

Be sure to fix and address errors that would cause failed checks for the single pull request (such as for lint and Python environment issues to avoid the following error during final checks): "3 failing checks
x Cl / lint-and-format (3.10) (pull...
x Cl / lint-and-format (3.11) (pull...
x Cl / lint-and-format (3.12) (pull... " Place the new release notes in releases.md under main using the format below. Update other relevant documentation such as project structures. Update the main Readme diagrams, repository structure, etc. where necessary. Update the CHANGELOG.md (v0.9.0).

"FORMAT"
Release title
v0.9.0 - [Fill in Title Here]

## Summary

## Features

## Contributors
@kevinkawchak
@claude
@openai
@google-gemini

## Notes
“FORMAT”
