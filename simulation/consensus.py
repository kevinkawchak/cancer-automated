"""Consensus across the three simulation runs.

The consensus aggregator computes the mean of each numeric metric across the
runs and the coefficient of variation, then flags any metric whose dispersion
exceeds the divergence threshold. Divergent metrics are the signal that a
deliverable needs human attention before it can ship. Pure standard library.

LICENSE: MIT
"""

from __future__ import annotations

import statistics
from dataclasses import dataclass, field

DEFAULT_MAX_CV = 0.10


@dataclass
class Consensus:
    """Aggregated consensus across simulation runs."""

    n_runs: int
    mean: dict = field(default_factory=dict)
    cv: dict = field(default_factory=dict)
    divergent: list = field(default_factory=list)

    @property
    def converged(self) -> bool:
        return not self.divergent


def _as_metric_dicts(results) -> list[dict]:
    """Accept either RunResult objects or plain dicts."""
    runs: list[dict] = []
    for item in results:
        if hasattr(item, "metrics"):
            runs.append(item.metrics)
        else:
            runs.append(item)
    return runs


def summarize(results, max_cv: float = DEFAULT_MAX_CV) -> Consensus:
    """Summarize runs into a consensus, flagging divergent metrics."""
    runs = _as_metric_dicts(results)
    if not runs:
        return Consensus(n_runs=0)

    common = set(runs[0].keys())
    for run in runs[1:]:
        common &= set(run.keys())

    mean: dict = {}
    cv: dict = {}
    divergent: list = []
    for key in sorted(common):
        try:
            values = [float(run[key]) for run in runs]
        except (KeyError, TypeError, ValueError):
            continue
        avg = statistics.fmean(values)
        stdev = statistics.pstdev(values) if len(values) > 1 else 0.0
        dispersion = (stdev / abs(avg)) if avg != 0 else 0.0
        mean[key] = avg
        cv[key] = dispersion
        if dispersion > max_cv:
            divergent.append(key)

    return Consensus(n_runs=len(runs), mean=mean, cv=cv, divergent=divergent)
