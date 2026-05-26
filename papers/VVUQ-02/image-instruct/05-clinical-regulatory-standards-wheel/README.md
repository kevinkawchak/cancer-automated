# Image Instruction 05: Clinical and Regulatory Standards Wheel

Chart family: wheel diagram (concentric ring / sunburst built from wedge patches).
Basis: code generation (v0.7.0 `inputs/` corpus and `codegen/config/project.yaml`
standards groups). Required data R4: the clinical external standards and
regulatory relevancies, including the input subdirectories, must be included.
Output: a single portrait, full page, 300 dpi PNG that organizes the wired input
corpus, the 14 consensus standards and the 2 clinical baselines, into a six domain
wheel around the VVUQ-02 assurance hub, with the regulatory relevancy called out.

This instruction is self contained. Read the shared conventions in
`papers/VVUQ-02/image-instruct/README.md` for the page frame, palette, fonts,
symbols, and dash rules, then build exactly what is specified below.

## Purpose and message

The corpus under `papers/VVUQ-02/inputs/` is what makes the assurance argument
auditable rather than ad hoc. The wheel shows the whole external grounding at a
glance: six domains radiating from the assurance hub, each holding its standards
and, for the clinical domain, the two outcome baselines, with the issuing body on
each segment and a regulatory relevancy ring that names what a real deployment
would require.

## Grounding (cite in the footer)

Sources, used for every segment below:

- `papers/VVUQ-02/inputs/README.md` (the corpus contents and provenance).
- `papers/VVUQ-02/inputs/standards/manifest.yaml` (the 14 consensus standards with
  designation, issuing body, and the `used_for` clause).
- `papers/VVUQ-02/inputs/clinical/dutch_cohort_2025.md` and
  `papers/VVUQ-02/inputs/clinical/fistula_risk_score.md` (the two clinical
  baselines).
- `papers/VVUQ-02/codegen/config/project.yaml` (the `standards` grouping into model
  credibility, robotic surgery, service-robot safety, software and risk, and
  autonomy).

## The wheel data (exact, six domains)

Hub label: `VVUQ-02 assurance corpus (papers/VVUQ-02/inputs)`.

Domain arcs (inner ring) and their segments (outer ring). Each outer segment shows
the designation, the issuing body, and a short `used_for`.

| Domain (inner arc) | Color | Outer segments (designation, body, used_for) |
|--------------------|-------|-----------------------------------------------|
| Model credibility | navy `#1F3A5F` | ASME V&V 40-2018 (ASME, credibility vs risk); NASA-STD-7009A (NASA, uncertainty as first-class); FDA CM&S Credibility 2023 (FDA, regulatory acceptance) |
| Robotic surgery | teal `#2A9D8F` | IEC 80601-2-77:2019 (IEC, accuracy, force, e-stop); IEC 60601-1 (IEC, single-fault safe state) |
| Service-robot safety | slate blue `#4C72B0` | ISO 13482:2014 (ISO, stability); ISO/TS 15066:2016 (ISO, contact and clearance); ISO 10218-1:2011 (ISO, speed and separation); ISO 9283:1998 (ISO, pose accuracy) |
| Software and risk | escalate amber `#E1A93B` | IEC 62304 (IEC, software life cycle); ISO 14971:2019 (ISO, risk management); ISO 13849-1:2023 (ISO, control-path performance level) |
| Autonomy | autonomy purple `#6A4C93` | UL 4600 (2023) (UL, autonomy safety case); IEEE Std 7009-2024 (IEEE, fail-safe default) |
| Clinical baselines | clinical rose `#B5566E` | Dutch cohort 2025 (public literature, human comparator); Callery Fistula Risk Score (published score, anastomosis quality for VVUQ 07) |

That is 14 consensus standards plus 2 clinical baselines, 16 outer segments across
6 domains.

Regulatory relevancy callout (outer annotation band): `Deployment would require
IEC 80601-2-77, IEC 60601, ISO 13482, FDA SaMD Class III clearance, IRB approval,
and regulatory authorization`. Flag the FDA CM&S Credibility 2023 segment and the
clinical domain with a thin regulatory-rose outer tick to show the regulatory and
clinical relevancy.

## Layout specification (portrait, full page)

Use the shared page frame. Build the content with a single square axis centered in
the content band (`GridSpec` 1 by 1, `left=0.10, right=0.90, top=0.88,
bottom=0.16`), equal aspect, axis off, drawn in data coordinates centered on the
origin.

- Header at `y = 0.965`: `Clinical and Regulatory Standards Wheel`. Subtitle at
  `y = 0.935`: `The wired input corpus: 14 consensus standards and 2 clinical
  baselines across 6 domains (papers/VVUQ-02/inputs)`.
- Hub: a filled circle (radius about 0.9 units) in panel fill with a primary navy
  ring, the hub label centered in 11 pt bold, wrapped to about 16 characters.
- Inner ring (radius about 0.9 to 1.7): six domain wedges sized proportionally to
  their segment counts (3, 2, 4, 3, 2, 2 segments), filled with the domain colors
  above at full saturation, the domain name in white 10.5 pt bold along the arc or
  on a leader.
- Outer ring (radius about 1.7 to 3.0): the 16 segments, each within its domain
  wedge, filled with a lighter tint of the domain color, separated by thin white
  borders. In each segment place the designation in 8.5 pt bold and the `body` and
  `used_for` in 7.5 pt, wrapped; rotate text to the wedge angle but keep it upright
  on the left half (flip by 180 degrees where the angle would be upside down).
- Regulatory relevancy band: a thin arc or a footer-adjacent rounded rectangle
  (panel fill, clinical rose left accent) holding the deployment-requirement
  sentence in 9 pt, placed in the lower content band so it does not overlap the
  wheel.
- Body legend at the lower left of the content band: six swatches keyed to the six
  domain colors, 9 pt, with the segment count per domain.
- Issuing-body note: a 9 pt line near the legend, `Issuing bodies: ASME, NASA,
  IEC, ISO, UL, IEEE, FDA, plus published clinical literature`.

## Color, symbol, and dash rules

- Domain wedges in the six domain colors, outer segments in a lighter tint of the
  same color, hub navy, regulatory accents clinical rose. White figure background,
  near black or white-on-color text as contrast requires. No dark mode.
- Use `§` only if a segment references a clause (for example `ASME V&V 40 §8`);
  otherwise plain designations. Render `V&V`, `/TS`, and `(2023)` as written.
- Single hyphens only. Write `first-class`, `single-fault`, `SaMD Class III`, and
  ranges with the word `to`.

## matplotlib implementation directives

- `matplotlib.use("Agg")`; import `matplotlib.pyplot as plt`, `numpy as np`, and
  from `matplotlib.patches` import `Wedge` and `Circle`.
- Build the wheel from a list of domains, each with its color and its list of
  segment dicts; compute each domain wedge angular span proportional to its
  segment count, then split it into equal segment wedges, so all geometry is
  derived.
- Place segment text with `ax.text` using the segment mid angle and a mid radius;
  compute the rotation from the angle and flip text on the left hemisphere to keep
  it upright.
- Set `ax.set_xlim(-3.2, 3.2)`, `ax.set_ylim(-3.2, 3.2)`, `ax.set_aspect("equal")`,
  `ax.axis("off")`.
- Save with `fig.savefig("papers/VVUQ-02/imagegen/05-clinical-regulatory-standards-wheel/05-clinical-regulatory-standards-wheel.png",
  dpi=300, facecolor="white")`. Do not use `bbox_inches="tight"`.

## Output paths

- Script: `papers/VVUQ-02/imagegen/05-clinical-regulatory-standards-wheel/05-clinical-regulatory-standards-wheel.py`.
- Image: `papers/VVUQ-02/imagegen/05-clinical-regulatory-standards-wheel/05-clinical-regulatory-standards-wheel.png`.

## Footer text

`cancer-automated v0.9.0  |  source: inputs/README.md, inputs/standards/manifest.yaml, inputs/clinical/, codegen/config/project.yaml  |  white background, 300 dpi, portrait`

## Per figure acceptance checklist

- Portrait, full page, `figsize=(8.5, 11)`, saved at 300 dpi, white background.
- Hub plus six domain wedges plus 16 outer segments (14 standards and 2 clinical
  baselines), each labeled with designation, body, and used_for.
- The regulatory relevancy callout (IEC 80601-2-77, IEC 60601, ISO 13482, FDA SaMD
  Class III, IRB) is present and the clinical and FDA segments are flagged.
- Segment text upright and legible on both hemispheres; domain legend with counts
  present.
- Header, subtitle, legend, regulatory band, and footer inside their bands, no
  overlap, none clipped.
- The section symbol renders as `§` where used; only single hyphens in visible
  text; no dark mode.
- Script is self contained, uses only matplotlib and numpy, and passes
  `ruff check` and `ruff format --check`.
