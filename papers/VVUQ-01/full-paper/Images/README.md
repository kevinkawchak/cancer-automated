# Images for the full paper

The manuscript references four figures. Until each image file below is present,
`main.tex` renders a labeled placeholder slot in its place, so the project
compiles in Overleaf either way. Drop the final rendered image into this
directory under the exact name listed, and the real figure replaces the
placeholder automatically with no edits to the `.tex` files.

| Expected file | Figure | Section | Grounded in (imagegen script) |
|:--------------|:-------|:--------|:------------------------------|
| `acceleration-waterfall.png` | Schedule acceleration waterfall | Results | `02-acceleration-waterfall` |
| `vvuq-assurance-wheel.png` | VVUQ assurance wheel | Results | `04-vvuq-assurance-wheel` |
| `test-coverage-treemap.png` | Test coverage treemap | Results | `06-test-coverage-treemap` |
| `fda-cost-bridge.png` | FDA cost efficiency bridge | Discussion | `08-fda-cost-efficiency-bridge` |

Portrait, full size, 300 dpi PNG (or PDF) renders are recommended, matching the
imagegen scripts under `../../imagegen/`. Each figure is placed with
`width=1.1\linewidth` and a small negative `\hspace` so it is centered on the
page.
