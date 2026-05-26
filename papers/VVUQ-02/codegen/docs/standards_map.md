# Standards Map: VVUQ Gates to Real-World Standards

Every VVUQ gate binds to one or more published consensus standards already used
in real life. The binding is machine-readable in `config/standards_map.yaml` and
is loaded at runtime by `src/vvuq/gate_registry.py`. This document is the human
readable view.

## Cross-cutting standards (apply to all 10 gates)

| Standard | Role |
|----------|------|
| ASME V&V 40-2018 | Model credibility framework (context of use, model risk, credibility goals) |
| NASA-STD-7009A | Models and simulations credibility, uncertainty quantification factor |
| FDA CM&S Credibility 2023 | Regulatory acceptance of the V&V 40 credibility argument |
| IEC 62304:2006+AMD1 | Medical device software life cycle (verification, software safety class) |
| ISO 14971:2019 | Risk management (model risk, risk control verification, human review) |
| IEC 80601-2-77:2019 | Basic safety and essential performance of robotically assisted surgery |

## Per-gate primary standards

| # | Gate slug | Governing standards | Standard-derived limit enforced |
|---|-----------|---------------------|---------------------------------|
| 01 | bimanual-handeye-servo | IEC 80601-2-77, ISO 9283, ASME V&V 40 | fingertip 0.05 mm RMS positioning, validate vs optical-tracker truth |
| 02 | dexterous-finger-force | IEC 80601-2-77, ISO/TS 15066 | per-fingertip soft 2.5 N / hard 3.0 N force limiting |
| 03 | whole-body-balance | ISO 13482, IEC 60601-1 | ZMP stability margin >= 8 mm inside support polygon |
| 04 | autonomous-plan-correctness | UL 4600, IEEE 7009, IEC 62304 | plan concordance vs reference plan, fail-safe default |
| 05 | instrument-grasp-handover | IEC 80601-2-77, ISO 9283 | grasp success, slip detection, repeatable handover |
| 06 | vascular-no-fly-hand | IEC 80601-2-77, ISO 14971 | zero hard-stop volume breaches, 10 us proximity e-stop |
| 07 | bimanual-suturing-anastomosis | IEC 80601-2-77, Fistula Risk Score | ring tension within +/- 0.05 N of PJ/HJ/GJ targets |
| 08 | perception-scene-understanding | ASME V&V 40, IEC 62304 | Dice agreement vs labeled reference under blood and smoke |
| 09 | shared-or-human-collision | ISO/TS 15066, ISO 10218-1, ISO 13482 | biomechanical clearance floor, intrusion-reaction latency |
| 10 | fault-estop-graceful-degradation | IEC 60601-1, ISO 13849-1, IEEE 7009 | single-fault safe state, fault-detection latency, safe park |

## Regulatory deployment gate (paper-only, simulation framing)

Deployment of the hypothetical H2-Surgical 1.0 would require, at minimum:

- IEC 80601-2-77:2019 and IEC 60601-1 basic safety and essential performance.
- ISO 13482:2014 personal-care / service-robot stability and fall prevention.
- ISO/TS 15066:2016 biomechanical limits for the shared operating room.
- IEC 62304 software life cycle with the highest software safety classification.
- ISO 14971 risk management file.
- FDA Software as a Medical Device (SaMD) Class III clearance and IRB approval.

Every value in this tree is simulation-only and paper-only. No value here is a
cleared specification of any real device.
