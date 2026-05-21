"""Generate a reconstruction README for a set of chunks.

Every autochunked file ships with a README that explains how to reconstruct the
original from its chunks. This is the established pattern from the prior
repositories: chunked sources always carry reconstruction instructions.

LICENSE: MIT
"""

from __future__ import annotations


def generate_readme(original_name: str, chunks, extension: str = "") -> str:
    """Build a Markdown README that documents and reconstructs the chunks.

    Args:
        original_name: the name of the original (pre-chunk) file.
        chunks: a sequence of objects with ``name`` and ``size_bytes``.
        extension: optional file extension applied to chunk file names.

    Returns:
        Markdown text for the chunk directory README.
    """
    chunk_list = list(chunks)
    suffix = extension if extension.startswith(".") or extension == "" else f".{extension}"

    rows = "\n".join(
        f"| {index + 1} | {chunk.name}{suffix} | {chunk.size_bytes} |" for index, chunk in enumerate(chunk_list)
    )
    ordered_names = " ".join(f"{chunk.name}{suffix}" for chunk in chunk_list)
    total_bytes = sum(chunk.size_bytes for chunk in chunk_list)

    return (
        f"# Chunks of `{original_name}`\n\n"
        f"`{original_name}` exceeded the 200K per-file cap and was autochunked into "
        f"{len(chunk_list)} pieces ({total_bytes} bytes total).\n\n"
        "## Chunks\n\n"
        "| Order | File | Bytes |\n"
        "|-------|------|-------|\n"
        f"{rows}\n\n"
        "## Reconstruction\n\n"
        "Concatenate the chunks in order to rebuild the original file:\n\n"
        "```bash\n"
        f"cat {ordered_names} > {original_name}\n"
        "```\n"
    )
