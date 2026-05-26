# Test Suite

The shipped automated test suite is the verification floor of the codegen tree.
Every gate, behavior model, and harness primitive has a test module. The suite
must be green before any example, sweep, or decision-surface run is trusted. It
maps directly to ASME V&V 40-2018 §8 (verification: did we build the model
right?) and IEC 62304 software verification.

## Command and result

```bash
cd papers/VVUQ-02/codegen
python -m pytest tests -q
```

```
........................................................................ [ 41%]
........................................................................ [ 83%]
............................                                             [100%]
172 passed in 1.38s
```

172 tests passed, 0 failed, 0 skipped, in about 1.4 seconds.

## Per-module breakdown

The 172 tests span 15 modules. The largest by far is `test_vvuq_gates.py` at 64
tests, which is the centerpiece: it exercises the 10-gate registry, the per-gate
thresholds, and the ACCEPT / BLOCK / ESCALATE decision logic. This weighting is
itself evidence for the thesis, the assurance harness carries more than a third
of the entire test budget.

| Test module | Tests | Subject |
|-------------|-------|---------|
| test_vvuq_gates.py | 64 | the 10-gate registry, thresholds, and decision surface (centerpiece) |
| test_safety.py | 12 | estop fault monitor, human-collision FSM, vessel no-fly gate |
| test_suturing.py | 11 | bimanual suture, ring-tension restore, RMSE and in-band metrics |
| test_hands.py | 11 | fingertip force tracking, bimanual caps, grasp, handover |
| test_vvuq_framework.py | 9 | verification, validation, uncertainty, gate composition |
| test_kinematics.py | 9 | DH forward kinematics, joint-limit clamp, distance |
| test_perception.py | 8 | scene segmentation, Dice, NIR/US/bile fusion |
| test_balance.py | 8 | ZMP computation, support-polygon margin, posture recovery |
| test_autonomy.py | 8 | LLM intent proposal, deterministic compile, concordance |
| test_sensors.py | 7 | per-tick per-hand sensor record synthesis and serialization |
| test_llm.py | 7 | the 4-entrant tournament agent and caveats |
| test_simulation.py | 6 | the 32-iteration Latin hypercube sweep |
| test_metrics.py | 5 | the 6-component composite and the gating overlay |
| test_zenodo.py | 4 | L0 pointer JSON and cross-iteration manifest |
| test_standards_corpus.py | 3 | the wired external-standards manifest binding |
| Total | 172 | |

## What the suite verifies, gate by gate

The suite does not just check that functions return; it pins the safety
semantics each external standard requires:

- The catastrophe gates (06 vascular no-fly, 09 shared-OR collision, 10
  fault e-stop) have tests asserting a hard-stop, an e-stop, or a hand-back is
  produced at the boundary, matching IEC 80601-2-77 §201.x hazardous-situation
  response, ISO/TS 15066 contact limits, and IEC 60601-1 single-fault safety.
- The balance gate (03) tests the ZMP margin against the support polygon, the
  ISO 13482 stability property for a standing service robot.
- The autonomy gate (04) tests phase-step concordance between the compiled plan
  and the annotated reference, the UL 4600 and IEEE 7009 autonomy property.
- The standards-corpus tests confirm each gate resolves its governing standards
  to published designations through the wired manifest, so the credibility
  argument is traceable rather than asserted.

## Reproduction

```bash
cd papers/VVUQ-02/codegen
python3 -m venv .venv && source .venv/bin/activate
pip install -e .[dev]
python -m pytest tests -q
```

All 172 tests pass on Python 3.11.15 here and are covered on 3.10, 3.11, and
3.12 by the CI test job. The suite is the floor; the sections that follow run
the harness over real decision cases the unit tests do not by themselves cover.
