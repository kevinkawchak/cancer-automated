# chunking/ - 200K Per-File Caps and Autochunked READMEs

Stage 1 raises the per-file size cap to 200K and requires that autochunked code
and documents carry a reconstruction README. This module enforces both.

```
   oversized file (> 200K)
        |
        v
  +-----------------------------+
  | Chunker.chunk_text          |
  | split on line boundaries,   |
  | hard-split any line that is |
  | itself over the cap         |
  +-----------------------------+
        |
        v
  chunk_001  chunk_002  ...  chunk_NNN
        |
        v
  +-----------------------------+
  | readme_generator            |
  | reconstruction README with  |
  | ordered cat instructions    |
  +-----------------------------+
```

## Modules

| File | Responsibility |
|------|----------------|
| `chunker.py` | Split text into chunks that each stay within the 200K byte cap |
| `readme_generator.py` | Emit a reconstruction README for a set of chunks |

## Usage

```python
import os, sys
sys.path.insert(0, os.path.abspath("chunking"))
from chunker import Chunker
from readme_generator import generate_readme

chunks = Chunker(cap_bytes=200_000).chunk_text(big_text)
readme = generate_readme("big_document.md", chunks, extension=".md")
```

See `examples-chunking/` for runnable examples.
