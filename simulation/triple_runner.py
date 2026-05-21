"""Auto-simulate every project three times.

The triple runner executes a project callable a fixed number of times (three by
default), each with a distinct deterministic seed, and collects the per-run
metric dicts. Running three times is a Stage 1 requirement: it exposes run to
run variance that a single run would hide and feeds the consensus aggregator and
the VVUQ uncertainty check. Pure standard library.

LICENSE: MIT
"""

from __future__ import annotations

import time
from dataclasses import dataclass, field
from typing import Callable

DEFAULT_RUNS = 3
DEFAULT_BASE_SEED = 20260521


@dataclass
class RunResult:
    """The metrics from one simulation run."""

    run_index: int
    seed: int
    metrics: dict = field(default_factory=dict)
    duration_s: float = 0.0


class TripleRunner:
    """Run a project callable three times with distinct seeds."""

    def __init__(self, n_runs: int = DEFAULT_RUNS, base_seed: int = DEFAULT_BASE_SEED) -> None:
        if n_runs < 1:
            raise ValueError("n_runs must be at least 1")
        self.n_runs = n_runs
        self.base_seed = base_seed

    def run(self, project_fn: Callable[[int], dict]) -> list[RunResult]:
        """Run ``project_fn(seed)`` ``n_runs`` times and collect the metrics.

        Args:
            project_fn: callable that accepts an integer seed and returns a dict
                of numeric metrics.

        Returns:
            A list of ``RunResult`` in run order.
        """
        results: list[RunResult] = []
        for index in range(self.n_runs):
            seed = self.base_seed + index
            start = time.perf_counter()
            metrics = dict(project_fn(seed))
            results.append(
                RunResult(
                    run_index=index,
                    seed=seed,
                    metrics=metrics,
                    duration_s=time.perf_counter() - start,
                )
            )
        return results
