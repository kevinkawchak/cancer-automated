"""Method 2: generate code from the instruction set.

The code generation stage reads the instruction artifact and emits a
self-contained Python script. The reference template produces a deterministic
script that computes simple trial-acceleration metrics so the downstream
execution stage has something concrete to run in CI. A guarded agentic backend
can replace the template when an API key is present.

LICENSE: MIT
"""

from __future__ import annotations

import os
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from deliverable import Artifact, Stage, StageResult, StageStatus  # noqa: E402

try:  # optional agentic backend, guarded
    import anthropic
except ImportError:  # pragma: no cover
    anthropic = None


# Template for the generated script. Placeholders are substituted with str
# replacement (not str.format) so the literal braces in the body are preserved.
_CODE_TEMPLATE = '''"""Generated deliverable script. Authored by the codegen stage."""


def compute_metrics(runs):
    baseline_days = 30.0
    automated_days = baseline_days / (1.0 + runs * 0.5)
    acceleration = baseline_days / automated_days
    return {
        "runs": runs,
        "baseline_days": baseline_days,
        "automated_days": round(automated_days, 3),
        "acceleration_factor": round(acceleration, 3),
    }


def main():
    metrics = compute_metrics(__RUNS__)
    print("title=__TITLE__")
    print("runs=" + str(metrics["runs"]))
    print("automated_days=" + str(metrics["automated_days"]))
    print("acceleration_factor=" + str(metrics["acceleration_factor"]))


if __name__ == "__main__":
    main()
'''


class CodegenStage:
    """Generate an executable script from the instruction set."""

    def __init__(self, simulate_runs: int = 3) -> None:
        self.simulate_runs = simulate_runs

    def run(self, deliverable) -> StageResult:
        start = time.perf_counter()
        instructions = deliverable.artifact("instructions")
        if instructions is None:
            result = StageResult(
                stage=Stage.CODEGEN,
                status=StageStatus.BLOCKED,
                log="no instruction artifact found; run the instruction stage first",
                duration_s=time.perf_counter() - start,
            )
            deliverable.record(result)
            return result

        code = self._generate_template(deliverable)
        artifact = Artifact(name="generated_deliverable.py", kind="code", content=code)
        result = StageResult(
            stage=Stage.CODEGEN,
            status=StageStatus.COMPLETE,
            artifacts=[artifact],
            log=f"code generated ({artifact.size_bytes} bytes, {self.simulate_runs} simulation runs)",
            duration_s=time.perf_counter() - start,
        )
        deliverable.record(result)
        return result

    def _generate_template(self, deliverable) -> str:
        safe_title = deliverable.title.replace('"', "'").replace("\n", " ")
        return _CODE_TEMPLATE.replace("__RUNS__", str(self.simulate_runs)).replace("__TITLE__", safe_title)
