# Independent Validation References

These artifacts are the trusted reference (the validation truth) for the 10 VVUQ
gates. Each is produced independently of the run under test: the values are
derived from standard-defined nominal values and closed-form analytic models, not
from the same stochastic simulation that produces the observed metrics. This
independence is what makes the comparison a validation rather than a self-check,
per ASME V&V 40-2018 section 9.

| File | Gate | Reference metric and provenance |
|------|------|---------------------------------|
| handeye_reference.json | 01 | fingertip 0.05 mm RMS, IEC 80601-2-77 / ISO 9283 positioning spec |
| finger_force_reference.json | 02 | 0.02 N force tracking error, IEC 80601-2-77 force-limiting nominal |
| balance_zmp_reference.json | 03 | 45 mm ZMP margin, analytic cart-table nominal at rest (ISO 13482) |
| plan_reference.json | 04 | 1.0 phase-step concordance, the annotated reference plan |
| grasp_reference.json | 05 | 0.97 grasp success, 0 slip events, ISO 9283 repeatability nominal |
| vessel_reference.json | 06 | 0 hard-stop breaches, 10 us proximity e-stop, IEC 80601-2-77 |
| ring_tension_reference.json | 07 | 0.02 N ring-tension RMSE, the plus or minus 0.05 N band midpoint |
| perception_reference.json | 08 | 0.97 mean Dice, the credibility target under blood and smoke |
| collision_reference.json | 09 | 60 mm min clearance, 3 ms reaction, ISO/TS 15066 |
| fault_reference.json | 10 | 50 us detection, 1.0 safe-state success, IEC 60601-1 single fault |
| scene_masks_reference.json | 08 | the labeled five-structure masks, the Dice ground truth |

The observed metrics from a run are compared against these references by
`src/vvuq/validation.py`; agreement is the fraction of metrics within the
per-gate maximum relative error. The masks file is the Dice ground truth consumed
by `src/perception/segment.py`.
