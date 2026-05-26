# Unitree H2-Surgical 1.0 Platform Specification (Hypothetical 2030)

## Hypothetical-platform rule (mandatory)

The Unitree H2 is a real full-size bipedal humanoid lineage with dexterous
multi-finger hands and on-board compute. A surgical H2 does not exist. This
project therefore defines a clearly labeled "Unitree H2-Surgical 1.0 (hypothetical
2030 surgical variant)". The base form factor traces to the real H2 lineage;
every clinical-grade capability uplift (sub-0.1 mm fingertip accuracy, 100 kHz
fingertip force, 3 ms e-stop) is explicitly flagged hypothetical 2030 and is
paper-only. Every comparison against PancreSpeed 1.0 or human surgeons is flagged
simulation-against-simulation in the limitations.

## Specification table

| Property | H2-Surgical 1.0 (hyp. 2030) | PancreSpeed 1.0 (PDAC baseline) | Stock H2 lineage (real, circa 2025) |
|----------|------------------------------|----------------------------------|--------------------------------------|
| Morphology | Bipedal humanoid, standing at table | 8 fixed coelomic arms on boom | Bipedal humanoid |
| Manipulators | 2 arms | 8 arms | 2 arms |
| DOF per arm | 7 | 7 | 7 |
| Hands | 2 dexterous, 5 fingers each | rigid tool end-effectors | 2 dexterous |
| DOF per hand | 20 (5 fingers x 4 joints) | n/a | about 20 |
| Locomotion / stance DOF | 2 legs x 6 + waist 3 | none (fixed base) | 2 legs x 6 + waist |
| Head / vision DOF | 2 (pan, tilt) | n/a | 2 |
| Total DOF | 14 arm + 40 hand + 15 stance + 2 head = 71 | 56 | matches base |
| Fingertip positioning accuracy at peak vel (mm RMS) | 0.05 (hyp.) | 0.05 | mm-class |
| Fingertip force resolution (N) | 0.01 at 100 kHz (hyp.) | 0.01 at 100 kHz | coarse |
| Per-fingertip force cap soft / hard (N) | 2.5 / 3.0 | 2.5 / 3.0 (per arm) | n/a |
| Bimanual cumulative tip force cap soft / hard (N) | 5.0 / 6.0 | 15.0 / 18.0 (8 arms) | n/a |
| Hand-arm e-stop latency (ms) | 3 (hyp.) | 3 | n/a |
| Joint park latency (us) | 50 (hyp.) | 50 | n/a |
| Balance recovery bandwidth (Hz) | 200 (hyp.) | n/a (fixed base) | balance-capable |
| Control / command rate (kHz) | 10 | 10 | lower |
| Force sample rate (kHz) | 100 | 100 | lower |
| On-prem LLM command interface | yes (thesis) | yes (thesis) | research |
| Regulatory framing | IEC 80601-2-77 + 60601 + ISO 13482 + FDA SaMD Class III | IEC 80601-2-77 + FDA SaMD | none clinical |

## The decisive difference from PancreSpeed

Balance and dexterity are now safety-critical. A fixed arm cannot fall over; a
standing humanoid can. Fingers can drop a needle. These differences motivate VVUQ
gates 01, 02, 03, 05, and 09. The bimanual cumulative force cap (6.0 N hard)
reflects two hands rather than eight arms (18.0 N hard on the baseline).

## Per-arm 7-DOF chain

J1 shoulder yaw, J2 shoulder pitch, J3 upper-arm yaw, J4 elbow pitch, J5 wrist
yaw, J6 wrist pitch, J7 wrist roll. Denavit-Hartenberg parameters and joint
limits are in `config/h2_kinematics.yaml`. Forward kinematics is implemented in
`src/kinematics/forward_kinematics.py` and gated by VVUQ 01.

## Supporting specifications

- `docs/h2_hand_kinematics.md` per-finger 4-DOF chains and grasp taxonomy.
- `docs/perception_stack_spec.md` head stereo, NIR ICG, endoscopic and ultrasound
  fusion, plus wrist and palm cameras.
- `docs/autonomy_policy_spec.md` the on-prem-LLM-to-motion stack.
- `docs/shared_or_safety_protocol.md` human-aware whole-body collision avoidance.
- `docs/suturing_anastomosis_protocol.md` bimanual suturing and ring-tension.
