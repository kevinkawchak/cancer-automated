# Images

The author drops the five rendered figure PNGs here. Until then, each figure float
in the manuscript renders a labelled placeholder box (via `\IfFileExists`), so the
full paper compiles cleanly in Overleaf without these files.

Copy each PNG from its `papers/VVUQ-02/imagegen/` render directory into this folder
under the same leaf name:

| Place here as | Rendered by |
|:--|:--|
| `03-ten-gate-threshold-forest.png` | `imagegen/03-ten-gate-threshold-forest/03-ten-gate-threshold-forest.py` |
| `04-gate-standard-binding-matrix.png` | `imagegen/04-gate-standard-binding-matrix/04-gate-standard-binding-matrix.py` |
| `05-clinical-regulatory-standards-wheel.png` | `imagegen/05-clinical-regulatory-standards-wheel/05-clinical-regulatory-standards-wheel.py` |
| `11-sensor-stream-safety-bands.png` | `imagegen/11-sensor-stream-safety-bands/11-sensor-stream-safety-bands.py` |
| `13-assurance-cost-assessment.png` | `imagegen/13-assurance-cost-assessment/13-assurance-cost-assessment.py` |

To render a bitmap ORCID logo in the title block, place `orcid_icon.png` in the
project root next to `main.tex` (the `\IfFileExists{orcid_icon.png}` test in
`main.tex` looks there). Without it, the title shows a green `iD` glyph linked to
the ORCID record, which is the default styling for this template family.
