"""Method 1: generate a bracketed instruction set for a deliverable.

The instruction set is the contract that drives code generation. It names the
inputs, the ordered steps (the five established methods), the production
constraints (single dashes, 200K per-file cap, autochunked READMEs), and the
acceptance criteria (the VVUQ gate).

An optional agentic backend (Anthropic) can author the instructions when an API
key is present. The backend import is guarded, so the module is fully usable
offline with a deterministic template.

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
except ImportError:  # pragma: no cover - exercised only when the package is absent
    anthropic = None


PER_FILE_CAP_BYTES = 200_000


class InstructionStage:
    """Generate the instruction set that the code generation stage consumes."""

    def __init__(self, per_file_cap_bytes: int = PER_FILE_CAP_BYTES, use_llm: bool = False) -> None:
        self.per_file_cap_bytes = per_file_cap_bytes
        self.use_llm = use_llm

    def run(self, deliverable, sources: list[str] | None = None) -> StageResult:
        start = time.perf_counter()
        sources = sources or []
        if self.use_llm and anthropic is not None and os.environ.get("ANTHROPIC_API_KEY"):
            content = self._generate_with_llm(deliverable, sources)
            backend = "anthropic"
        else:
            content = self._generate_template(deliverable, sources)
            backend = "template"
        artifact = Artifact(name="instructions.md", kind="instructions", content=content)
        result = StageResult(
            stage=Stage.INSTRUCTION,
            status=StageStatus.COMPLETE,
            artifacts=[artifact],
            log=f"instructions generated via {backend} backend ({artifact.size_bytes} bytes)",
            duration_s=time.perf_counter() - start,
        )
        deliverable.record(result)
        return result

    def _generate_template(self, deliverable, sources: list[str]) -> str:
        source_lines = "\n".join(f"- {src}" for src in sources) or "- (no external sources)"
        return (
            f"# Instruction Set: {deliverable.title}\n\n"
            f"Deliverable ID: {deliverable.deliverable_id}\n"
            f"Topic: {deliverable.topic}\n\n"
            "## Inputs\n\n"
            f"{source_lines}\n\n"
            "## Ordered Steps (the five established methods)\n\n"
            "1. Generate this instruction set.\n"
            "2. Generate code from the instructions.\n"
            "3. Execute the generated code and capture outputs.\n"
            "4. Assemble a paper from the executed results.\n\n"
            "## Production Constraints\n\n"
            "- Use single dashes in prose. Reserve triple dashes for Markdown rules and YAML separators.\n"
            f"- Keep every committed file at or under {self.per_file_cap_bytes} bytes.\n"
            "- Autochunk any oversized code or document and emit a README per chunk.\n"
            "- Guard heavy or optional imports so modules stay importable.\n\n"
            "## Acceptance Criteria\n\n"
            "- The deliverable passes the VVUQ gate (verification, validation, uncertainty).\n"
            "- The three simulation runs agree within the configured coefficient of variation.\n"
            "- A human review is recorded before any clinical use.\n"
        )

    def _generate_with_llm(self, deliverable, sources: list[str]) -> str:  # pragma: no cover
        client = anthropic.Anthropic()
        prompt = (
            f"Author a bracketed instruction set for the oncology-trial deliverable "
            f"titled {deliverable.title!r} on the topic {deliverable.topic!r}. "
            f"Sources: {sources}. Use single dashes only."
        )
        message = client.messages.create(
            model="claude-opus-4-7",
            max_tokens=2000,
            messages=[{"role": "user", "content": prompt}],
        )
        return message.content[0].text
