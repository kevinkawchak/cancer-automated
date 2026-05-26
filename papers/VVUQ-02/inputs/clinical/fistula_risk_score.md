# Callery Fistula Risk Score (FRS)

This file summarizes the Fistula Risk Score used to ground anastomosis quality for
VVUQ 07 (bimanual-suturing-anastomosis). It is a published clinical scoring
system, not a model output.

## Definition (10-point scale)

| Input | Source | Contribution |
|-------|--------|--------------|
| Gland texture | preoperative assessment | soft = 2 points, firm = 0 points |
| Pathology | histology | PDAC = 0 points, other = 1 point |
| Pancreatic duct diameter | preoperative imaging | linear, 1 mm = 4 points down to >= 5 mm = 0 points |
| Estimated blood loss | intraoperative | linear, 0 mL = 0 points up to >= 1000 mL = 4 points |

Risk categories: total 0 to 2 negligible (< 1 percent), 3 to 6 moderate (5 to 10
percent), 7 to 10 high (15 to 25 percent).

## Patient PAT-PDAC-0001

Gland texture soft (2), pathology PDAC (0), duct diameter 3.2 mm (2), estimated
blood loss 200 mL (1): total 5, moderate category. This is the preoperative FRS
of 5 recorded in `codegen/config/project.yaml`.

## How VVUQ-02 uses it

VVUQ 07 validates the realized ring-tension control at the three reconstruction
targets (PJ 0.45 N, HJ 0.50 N, GJ 0.60 N, each within a plus or minus 0.05 N
band) and reports the realized PJ leak grade (A subclinical, B clinically
relevant, C severe) against the FRS-derived expectation.
