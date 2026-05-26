# VVUQ-02 Inputs Corpus

This is the real input corpus the VVUQ-02 assurance layer is built against. It is
"wired" into the codegen: `codegen/src/vvuq/gate_registry.py` loads
`standards/manifest.yaml` at runtime and binds each of the 10 VVUQ gates to the
governing standards and the specific clause-derived limits enforced by the gate.
A standalone copy of the machine-readable binding also lives at
`codegen/config/standards_map.yaml`, so the codegen tree runs even if this corpus
is not present.

## Contents

```
inputs/
  README.md                       # this file
  standards/
    manifest.yaml                 # machine-readable index of standards + clauses
    asme_vv40_2018.md             # model credibility framework
    iec_80601_2_77_2019.md        # robotically assisted surgical equipment
    iso_ts_15066_2016.md          # collaborative robot biomechanical limits
    iso_13482_2014.md             # personal care robot safety and stability
    nasa_std_7009a.md             # models and simulations credibility
  clinical/
    dutch_cohort_2025.md          # human-surgeon outcome baseline
    fistula_risk_score.md         # Callery Fistula Risk Score definition
```

## Provenance and use

Each standards file is a factual summary of a published consensus standard, with
its designation, issuing body, scope, and the specific clauses VVUQ-02 relies on.
The full normative text of each standard is the property of its issuing body
(ASME, IEC, ISO, NASA, UL, IEEE, FDA) and must be obtained from that body. These
summaries are used here only to ground the assurance thresholds and to make the
gate-to-standard binding auditable. The clinical baseline files summarize public
outcome literature used as the human comparator.
