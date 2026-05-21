"""Method 3: execute the generated code and capture its outputs.

The execution stage compiles the generated script (a syntax-level verification)
and runs it in an isolated namespace while capturing stdout. The captured
``key=value`` lines are parsed into structured results stored on the deliverable
metadata so the paper stage can tabulate them.

Security note: this reference executor runs the generated code in-process for
determinism in CI. The code it runs is produced by the codegen template in this
repository, not by untrusted external input. Production deployments must execute
generated code inside a sandbox (container, seccomp, CPU and memory limits, no
network) before trusting any output.

LICENSE: MIT
"""

from __future__ import annotations

import contextlib
import io
import os
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from deliverable import Artifact, Stage, StageResult, StageStatus  # noqa: E402


class ExecutionStage:
    """Compile and run the generated code, capturing its output."""

    def run(self, deliverable) -> StageResult:
        start = time.perf_counter()
        code_artifact = deliverable.artifact("code")
        if code_artifact is None:
            result = StageResult(
                stage=Stage.EXECUTION,
                status=StageStatus.BLOCKED,
                log="no code artifact found; run the codegen stage first",
                duration_s=time.perf_counter() - start,
            )
            deliverable.record(result)
            return result

        try:
            compiled = compile(code_artifact.content, code_artifact.name, "exec")
        except SyntaxError as exc:
            result = StageResult(
                stage=Stage.EXECUTION,
                status=StageStatus.FAILED,
                log=f"generated code failed to compile: {exc}",
                duration_s=time.perf_counter() - start,
            )
            deliverable.record(result)
            return result

        namespace: dict = {"__name__": "__generated__"}
        buffer = io.StringIO()
        status = StageStatus.COMPLETE
        log = "execution complete"
        try:
            with contextlib.redirect_stdout(buffer):
                exec(compiled, namespace)
                main_fn = namespace.get("main")
                if callable(main_fn):
                    main_fn()
        except Exception as exc:  # noqa: BLE001 - capture any runtime failure into the log
            status = StageStatus.FAILED
            log = f"execution raised {type(exc).__name__}: {exc}"

        captured = buffer.getvalue()
        results = self._parse_output(captured)
        deliverable.metadata["execution_results"] = results

        artifact = Artifact(name="execution_log.txt", kind="execution_log", content=captured or log)
        result = StageResult(
            stage=Stage.EXECUTION,
            status=status,
            artifacts=[artifact],
            log=log,
            duration_s=time.perf_counter() - start,
        )
        deliverable.record(result)
        return result

    @staticmethod
    def _parse_output(captured: str) -> dict:
        """Parse ``key=value`` lines from the captured stdout into a dict."""
        results: dict = {}
        for line in captured.splitlines():
            if "=" in line:
                key, _, value = line.partition("=")
                results[key.strip()] = value.strip()
        return results
