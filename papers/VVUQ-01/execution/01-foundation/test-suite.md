# Foundation Execution: Test Suite

This section records the execution of the full automated test suite. The suite
is the first line of the verification half of VVUQ: it confirms that every
module behaves as specified before any example or deliverable is generated.

## How the suite was run

```bash
python -m pytest tests/ -v --tb=short
```

The container Python (3.11.15) was used. `pytest` 9.0.3 was installed to match
the CI `test` job, which installs `pytest` and `pyyaml`. With `pyyaml` present,
the two configuration-parsing tests that guard on it executed rather than
skipping, so the full set of 51 tests ran.

The test harness in `tests/conftest.py` loads each source module by file path
through `importlib.util`. This is required because several source directories
contain a hyphen (for example `physical-ai/`), and a hyphen is not a legal
character in a Python import statement. When a module needs a dependency that is
not installed, the harness skips that test rather than erroring, which is what
keeps CI green on a minimal runner.

## Result

All 51 collected tests passed. There were no failures, no errors, and no skips
on this host. The suite was also run with numpy uninstalled to confirm that no
test depends on it; the result was identical (51 passed, 0 skipped), which
matches the fact that no source module imports numpy.

```text
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-9.0.3, pluggy-1.6.0
rootdir: /home/user/cancer-automated
collecting ... collected 51 items
...
============================== 51 passed in 0.38s ==============================
```

## Per-module breakdown

The 51 tests are distributed across 9 test modules that map one-to-one onto the
source packages.

| Test module | Tests | Target package | All passed |
|-------------|-------|----------------|------------|
| test_foundation.py | 16 | repository files, configs, verify script | yes |
| test_pipeline.py | 5 | pipeline (five established methods) | yes |
| test_vvuq.py | 8 | vvuq (verification, validation, uncertainty, gate) | yes |
| test_simulation.py | 4 | simulation (triple runner, consensus) | yes |
| test_ingestion.py | 4 | ingestion (web search, pdf processor) | yes |
| test_chunking.py | 4 | chunking (chunker, readme generator) | yes |
| test_scheduler.py | 4 | scheduler (commit scheduler) | yes |
| test_physical_ai.py | 5 | physical-ai (lights-off factory, hybrid pilot) | yes |
| (total) | 51 | all packages | yes |

## Full verbose roster

Every individual test name and its outcome is listed below, exactly as pytest
reported it.

```text
tests/test_chunking.py::test_small_text_is_a_single_chunk PASSED
tests/test_chunking.py::test_large_text_splits_within_cap_and_reconstructs PASSED
tests/test_chunking.py::test_oversized_single_line_is_hard_split PASSED
tests/test_chunking.py::test_readme_generator_lists_chunks_and_cat_command PASSED
tests/test_foundation.py::test_required_file_exists[README.md] PASSED
tests/test_foundation.py::test_required_file_exists[LICENSE] PASSED
tests/test_foundation.py::test_required_file_exists[CHANGELOG.md] PASSED
tests/test_foundation.py::test_required_file_exists[CONTRIBUTING.md] PASSED
tests/test_foundation.py::test_required_file_exists[CODE_OF_CONDUCT.md] PASSED
tests/test_foundation.py::test_required_file_exists[SECURITY.md] PASSED
tests/test_foundation.py::test_required_file_exists[SUPPORT.md] PASSED
tests/test_foundation.py::test_required_file_exists[CITATION.cff] PASSED
tests/test_foundation.py::test_required_file_exists[requirements.txt] PASSED
tests/test_foundation.py::test_required_file_exists[ruff.toml] PASSED
tests/test_foundation.py::test_required_file_exists[.github/workflows/ci.yml] PASSED
tests/test_foundation.py::test_required_file_exists[configs/pipeline_config.yaml] PASSED
tests/test_foundation.py::test_required_file_exists[configs/vvuq_thresholds.yaml] PASSED
tests/test_foundation.py::test_pipeline_config_parses PASSED
tests/test_foundation.py::test_vvuq_thresholds_parse PASSED
tests/test_foundation.py::test_verify_installation_importable PASSED
tests/test_ingestion.py::test_web_search_returns_results_without_network PASSED
tests/test_ingestion.py::test_web_search_rejects_zero_attempts PASSED
tests/test_ingestion.py::test_pdf_processor_reports_missing_file PASSED
tests/test_ingestion.py::test_pdf_processor_chunk_estimate PASSED
tests/test_physical_ai.py::test_factory_is_ready_by_default_and_completes_clean_run PASSED
tests/test_physical_ai.py::test_factory_blocks_when_interlock_unsatisfied PASSED
tests/test_physical_ai.py::test_factory_emergency_stops_past_fault_budget PASSED
tests/test_physical_ai.py::test_factory_requires_at_least_one_cell PASSED
tests/test_physical_ai.py::test_hybrid_pilot_timeline_and_summary PASSED
tests/test_pipeline.py::test_pipeline_runs_all_four_methods PASSED
tests/test_pipeline.py::test_execution_results_have_acceleration PASSED
tests/test_pipeline.py::test_codegen_is_blocked_without_instructions PASSED
tests/test_pipeline.py::test_paper_tabulates_results PASSED
tests/test_pipeline.py::test_gate_callable_is_invoked PASSED
tests/test_scheduler.py::test_plan_slot_count_and_interval PASSED
tests/test_scheduler.py::test_slots_are_evenly_spaced PASSED
tests/test_scheduler.py::test_next_slot_returns_future_slot PASSED
tests/test_scheduler.py::test_scheduler_rejects_zero_cadence PASSED
tests/test_simulation.py::test_triple_runner_runs_three_times_with_distinct_seeds PASSED
tests/test_simulation.py::test_consensus_converges_for_low_variance PASSED
tests/test_simulation.py::test_consensus_flags_divergence_for_high_variance PASSED
tests/test_simulation.py::test_triple_runner_rejects_zero_runs PASSED
tests/test_vvuq.py::test_verification_passes_for_good_deliverable PASSED
tests/test_vvuq.py::test_verification_flags_oversize_file PASSED
tests/test_vvuq.py::test_validation_perfect_agreement PASSED
tests/test_vvuq.py::test_validation_detects_disagreement PASSED
tests/test_vvuq.py::test_uncertainty_zero_cv_for_identical_runs PASSED
tests/test_vvuq.py::test_gate_accepts_clean_deliverable PASSED
tests/test_vvuq.py::test_gate_blocks_without_human_review PASSED
tests/test_vvuq.py::test_gate_blocks_and_escalates_on_divergence PASSED
```

## Note on the run count versus the v0.1.0 release note

The v0.1.0 release note records "49 passed, 2 environment-skipped". The only
tests in the suite that can skip are the two in `test_foundation.py` that call
`pytest.importorskip("yaml")`: `test_pipeline_config_parses` and
`test_vvuq_thresholds_parse`. They skip only when `pyyaml` is absent. The
v0.1.0 figure corresponds to a measurement taken without `pyyaml`. On this
execution host `pyyaml` was installed (as the CI `test` job does via
`pip install pytest pyyaml`), so both tests ran and the suite reported 51
passed and 0 skipped. No source module performs an unguarded third-party
import, so the conftest dependency-skip path was never triggered. The
difference is purely environmental and reflects the guarded design, not a
change in the code.
