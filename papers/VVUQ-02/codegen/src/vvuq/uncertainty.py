"""Uncertainty quantification across the seeded runs (NASA-STD-7009A).

For each numeric metric shared by every run, computes the mean, the population
standard deviation, and the coefficient of variation (cv = stdev / mean). The
maximum cv is the dispersion measure the gate compares against its per-gate bound;
divergence above the bound sets ESCALATE. Pure standard library.

LICENSE: MIT
"""

from __future__ import annotations

import statistics
from dataclasses import dataclass, field


@dataclass
class UncertaintyResult:
    """Per-metric dispersion across the runs."""

    n_runs: int
    per_key: dict = field(default_factory=dict)

    @property
    def max_cv(self) -> float:
        return max((s["cv"] for s in self.per_key.values()), default=0.0)

    def divergent_keys(self, max_cv: float) -> list[str]:
        return [k for k, s in self.per_key.items() if s["cv"] > max_cv]


def quantify(runs: list[dict], keys: list[str] | None = None) -> UncertaintyResult:
    """Quantify dispersion of numeric metrics across runs.

    Args:
        runs: list of metric dicts, one per seeded run.
        keys: optional explicit metric keys; defaults to the intersection of keys
            present in every run.
    """
    if not runs:
        return UncertaintyResult(n_runs=0)
    if keys is None:
        common = set(runs[0].keys())
        for run in runs[1:]:
            common &= set(run.keys())
        keys = sorted(common)
    per_key: dict = {}
    for key in keys:
        values: list[float] = []
        ok = True
        for run in runs:
            try:
                values.append(float(run[key]))
            except (KeyError, TypeError, ValueError):
                ok = False
                break
        if not ok or not values:
            continue
        mean = statistics.fmean(values)
        stdev = statistics.pstdev(values) if len(values) > 1 else 0.0
        cv = (stdev / abs(mean)) if mean != 0 else 0.0
        per_key[key] = {"mean": mean, "stdev": stdev, "cv": cv}
    return UncertaintyResult(n_runs=len(runs), per_key=per_key)
