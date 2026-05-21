"""Uncertainty quantification across the three simulation runs.

For each numeric metric shared by every run, this computes the mean, the
population standard deviation, and the coefficient of variation (cv). The cv is
the dispersion measure the VVUQ gate compares against its threshold. Pure
standard library (uses ``statistics``).

LICENSE: MIT
"""

from __future__ import annotations

import statistics
from dataclasses import dataclass, field


@dataclass
class UncertaintyResult:
    """Per-metric dispersion across the simulation runs."""

    n_runs: int
    per_key: dict = field(default_factory=dict)

    @property
    def max_cv(self) -> float:
        return max((stats["cv"] for stats in self.per_key.values()), default=0.0)

    def divergent_keys(self, max_cv: float) -> list[str]:
        return [key for key, stats in self.per_key.items() if stats["cv"] > max_cv]


def quantify(runs: list[dict], keys: list[str] | None = None) -> UncertaintyResult:
    """Quantify dispersion of numeric metrics across runs.

    Args:
        runs: list of metric dicts, one per simulation run.
        keys: optional explicit metric keys; defaults to the intersection of
            keys present in every run.
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
