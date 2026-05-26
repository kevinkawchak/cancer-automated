# Cross References

This table is the single map from each VVUQ gate to its specification, code,
configuration, independent reference, governing standards, and tests. Every path
is relative to `papers/VVUQ-02/codegen/` unless noted.

| # | Gate | Code | Config | Reference | Tests |
|---|------|------|--------|-----------|-------|
| 01 | bimanual-handeye-servo | src/kinematics/forward_kinematics.py | config/h2_kinematics.yaml | data/reference/handeye_reference.json | tests/test_kinematics.py |
| 02 | dexterous-finger-force | src/hands/finger_force.py | config/hand_model.yaml | data/reference/finger_force_reference.json | tests/test_hands.py |
| 03 | whole-body-balance | src/balance/zmp.py, src/balance/posture_controller.py | config/balance_model.yaml | data/reference/balance_zmp_reference.json | tests/test_balance.py |
| 04 | autonomous-plan-correctness | src/autonomy/llm_intent.py, src/autonomy/plan_compiler.py | config/autonomy_plan.yaml | data/reference/plan_reference.json | tests/test_autonomy.py |
| 05 | instrument-grasp-handover | src/hands/grasp.py, src/hands/handover.py | config/hand_model.yaml | data/reference/grasp_reference.json | tests/test_hands.py |
| 06 | vascular-no-fly-hand | src/safety/vessel_gate.py | config/safety_zones.yaml | data/reference/vessel_reference.json | tests/test_safety.py |
| 07 | bimanual-suturing-anastomosis | src/suturing/ring_tension.py, src/suturing/bimanual_suture.py | config/anastomosis_targets.yaml | data/reference/ring_tension_reference.json | tests/test_suturing.py |
| 08 | perception-scene-understanding | src/perception/segment.py, src/perception/fuse_nir_us.py | config/perception_model.yaml | data/reference/scene_masks_reference.json, perception_reference.json | tests/test_perception.py |
| 09 | shared-or-human-collision | src/safety/human_collision.py | config/shared_or_actors.yaml | data/reference/collision_reference.json | tests/test_safety.py |
| 10 | fault-estop-graceful-degradation | src/safety/estop.py | config/project.yaml (timing) | data/reference/fault_reference.json | tests/test_safety.py |

## Harness and integration

| Concern | Code | Config | Tests |
|---------|------|--------|-------|
| 10-gate harness | src/vvuq/{verification,validation,uncertainty,vvuq_gate,gate_registry}.py | config/vvuq_thresholds.yaml | tests/test_vvuq_framework.py, tests/test_vvuq_gates.py |
| Standards binding | src/vvuq/gate_registry.py | config/standards_map.yaml, ../inputs/standards/manifest.yaml | tests/test_standards_corpus.py |
| 32-iteration sweep | src/simulation/iterate.py, src/simulation/runner.rs | config/project.yaml | tests/test_simulation.py |
| Composite overlay | src/metrics/compute.py | config/project.yaml | tests/test_metrics.py |
| 4-entrant tournament | src/llm/compare_agent.py | prompts/comparison_prompt.md | tests/test_llm.py |
| Zenodo L0 pointers | src/zenodo/patch_pointers.py | releases/v0.1.0/manifest.json | tests/test_zenodo.py |

## Specification documents

- docs/architecture.md, docs/vvuq_methodology.md, docs/standards_map.md
- docs/h2_robot_specification.md, docs/h2_hand_kinematics.md
- docs/sensor_spec.md, docs/perception_stack_spec.md, docs/autonomy_policy_spec.md
- docs/shared_or_safety_protocol.md, docs/suturing_anastomosis_protocol.md
- docs/vvuq_gate_spec.md, docs/ci_compliance_checklist.md
- docs/runtime_environments.md, docs/file_size_pyramid.md
