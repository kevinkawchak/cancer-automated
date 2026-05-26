# Bimanual Suturing and Anastomosis Protocol (VVUQ 07)

The humanoid reconstructs the three Whipple anastomoses with two hands where the
8-arm baseline used arm pairs. Targets are reused verbatim so the runs compare
directly. Configuration is in `config/anastomosis_targets.yaml`.

## Ring-tension targets

| Anastomosis | Technique | Ring tension (N) | Band (N) | Manometry (mmHg) | Phase |
|-------------|-----------|------------------|----------|------------------|-------|
| Pancreaticojejunostomy | duct to mucosa | 0.45 | +/- 0.05 | duct 12 | 5 |
| Hepaticojejunostomy | end to side | 0.50 | +/- 0.05 | bile 8 | 6 |
| Gastrojejunostomy | antecolic, pylorus preserving | 0.60 | +/- 0.05 | n/a | 7 |

## Bimanual ring-tension control

`src/suturing/ring_tension.py` holds the tension in band. On drift outside the
band the controller commands the suturing hand and the presenting hand in
opposite directions to restore the target, the bimanual analogue of the PDAC
arm-pair coordination. The two restoring deltas are equal and opposite.

## Realized grade taxonomy

`src/suturing/bimanual_suture.py` sutures each anastomosis under a per-stitch
ring-tension drift (one of the five sweep free parameters) and maps the realized
RMS error to a grade:

- Pancreaticojejunostomy: A (subclinical, RMSE <= 0.02 N), B (clinically
  relevant, RMSE <= 0.05 N), C (severe, RMSE > 0.05 N).
- Hepaticojejunostomy: leak absent (RMSE <= 0.05 N) or present.
- Gastrojejunostomy: patent (RMSE <= 0.05 N) or delayed.

## VVUQ 07 validation

VVUQ 07 validates the realized ring-tension RMS error against the plus or minus
0.05 N band reference and reports the in-band fraction and the realized grade,
grounded in IEC 80601-2-77 and the Callery Fistula Risk Score (FRS 5, moderate,
for PAT-PDAC-0001).
