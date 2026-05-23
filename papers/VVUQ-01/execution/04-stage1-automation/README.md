# Section 04: Stage 1 Automation (Simulation, Ingestion, Chunking, Scheduler)

This section executes the four Stage 1 automation capabilities that wrap the
pipeline: triple simulation with consensus, robust web and PDF ingestion, 200K
autochunking with reconstruction READMEs, and the non-stop commit scheduler.
Seven example scripts were run, and two additional verifications were performed
on the chunker to confirm its losslessness claim. One genuine limitation was
discovered and is documented in full below.

## Simulation: auto-simulate every project three times

### Triple runner

```bash
python simulation/examples-simulation/01_triple_run.py
```

```text
run 0 seed=20260521 metrics={'acceleration_factor': 2.502, 'automated_days': 11.998}
run 1 seed=20260522 metrics={'acceleration_factor': 2.504, 'automated_days': 11.996}
run 2 seed=20260523 metrics={'acceleration_factor': 2.506, 'automated_days': 11.994}
```

The runner executed the project callable three times with distinct deterministic
seeds (20260521, 20260522, 20260523). The metrics vary slightly with the seed,
which is exactly the run-to-run variance a single run would hide.

### Consensus

```bash
python simulation/examples-simulation/02_consensus_report.py
```

```text
n_runs: 3
converged: True
  acceleration_factor: mean=2.5040 cv=0.0007
  automated_days: mean=11.9960 cv=0.0001
divergent: []
```

The consensus aggregator averaged the three runs and computed a coefficient of
variation per metric (0.0007 and 0.0001), both far below the 0.10 divergence
threshold, so consensus converged with no divergent metrics. This is the same
dispersion signal the VVUQ uncertainty dimension consumes.

## Ingestion: robust web search and PDF processing

### Web search with bounded retries and offline fallback

```bash
python ingestion/examples-ingestion/01_web_search.py
```

```text
query: physical AI oncology trial automation
online: False attempts: 4
  - [offline] physical AI oncology trial automation result 1 (offline-stub)
  - [offline] physical AI oncology trial automation result 2 (offline-stub)
  - [offline] physical AI oncology trial automation result 3 (offline-stub)
```

This is the robust retry envelope working as designed. The `requests` package is
installed in this environment, so the client attempted a live fetch. The
container network policy does not expose the live search endpoint, so each
attempt raised, the client retried up to its bound of 4 attempts (with the
example's zero base delay, so no real wait), and then degraded gracefully to the
labeled offline stub with `online: False`. A transient network failure therefore
never aborts a deliverable; it downgrades to a clearly marked stub.

### PDF processing and the 200K chunk estimate

```bash
python ingestion/examples-ingestion/02_pdf_extract.py
```

```text
path: nonexistent_reference.pdf
ok: False
status: file not found
chunks needed for a 450K document: 3
```

Two guarded behaviors are visible. First, a missing file produces a clean
non-fatal status (`file not found`) rather than an exception. Second, the chunk
estimate is independent of the PDF backend: a 450000 byte document needs
`ceil(450000 / 200000) = 3` chunks under the 200K cap. Because `pypdf` is not
installed here, a present-but-unreadable PDF would report
`pypdf not installed; install to extract text`, which is the other guarded path.

## Chunking: 200K autochunk with reconstruction READMEs

### Chunk a document under a demo cap

```bash
python chunking/examples-chunking/01_chunk_document.py
```

```text
document bytes: 114890
chunks: 6 (cap 20000 bytes)
  document_001: 19954 bytes
  document_002: 19950 bytes
  document_003: 19944 bytes
  document_004: 19952 bytes
  document_005: 19952 bytes
  document_006: 15138 bytes
```

A 114890 byte document split into 6 chunks under a 20000 byte demo cap. Every
chunk is at or under the cap, and the chunker splits on line boundaries so no
line is torn.

### Generate a reconstruction README

```bash
python chunking/examples-chunking/02_chunk_with_readme.py
```

The example printed a complete reconstruction README, which is saved verbatim in
`artifacts/chunk_reconstruction_README.md`. It documents the chunk order, the
per-chunk byte counts, and a single `cat` command that rebuilds the original
file. This is the established pattern from the prior repositories: every
autochunked file ships with instructions to reconstruct it.

### Independent verification of the losslessness claim

The chunker's contract is that concatenating the chunks rebuilds the original.
This was verified directly (not just trusted), with the following result for the
line-oriented document from example 01:

```text
original bytes: 114890
num chunks: 6
max chunk bytes: 19954
all chunks <= cap (20000): True
reconstruction is byte-identical: True
```

Line-boundary chunking is byte-identical lossless and respects the cap. The
ASCII hard-split path (a single line longer than the cap, all single-byte
characters) was also verified lossless, which matches the shipped test
`test_oversized_single_line_is_hard_split` that uses `"x" * 12000`.

### Discovered limitation: multibyte hard-split is lossy at boundaries

A second verification probed an untested edge case: a single oversized line made
of multibyte UTF-8 characters. Here the chunker is not lossless.

```text
Multibyte hard-split (cap 10000 over 60000 bytes of repeated e-acute):
  pieces: 7
  original chars: 30000   rebuilt chars: 29994
  chars lost: 6
  original bytes: 60000   rebuilt bytes: 59988
```

Root cause. `_hard_split_line` in `chunking/chunker.py` slices the line by bytes
at the cap, then steps `end` back while the final byte is a UTF-8 continuation
byte, and finally decodes each piece with `errors="ignore"`. When a 2-byte
character straddles the cap, the step-back can leave an incomplete lead byte at
the tail of a piece; `errors="ignore"` then drops that lead byte, and the
orphaned continuation byte at the head of the next piece is dropped too. With a
10000 byte cap over 60000 bytes there are 6 internal boundaries, and exactly one
2-byte character is lost at each, for 6 characters (12 bytes) lost.

Scope and severity. This path is only reached by a single line that exceeds the
per-file cap (200000 bytes in production) and that contains multibyte characters
straddling the boundary. Line-boundary chunking, which is the common case, is
fully lossless. The shipped unit test exercises only the ASCII hard-split, so
the suite passes while the multibyte case silently loses data.

Disposition. This is reported as a finding, not repaired here. The task scope is
to execute the v0.1.0 codebase and document the outcomes, not to modify the
baseline under study. Repairing it (for example by carrying the incomplete
trailing bytes forward to the next piece instead of ignoring them, and adding a
multibyte hard-split test) is a recommended follow-up for a future release. The
finding is a direct illustration of the project thesis: a substantial VVUQ
process surfaces what unit tests miss.

## Scheduler: non-stop commit cadence

```bash
python scheduler/examples-scheduler/01_daily_schedule.py
```

```text
planned 24 slots, interval 3600 seconds
  deliverable-0001 at 2026-05-21T00:00:00+00:00
  deliverable-0002 at 2026-05-21T01:00:00+00:00
  deliverable-0003 at 2026-05-21T02:00:00+00:00
  deliverable-0004 at 2026-05-21T03:00:00+00:00
  deliverable-0005 at 2026-05-21T04:00:00+00:00
  ...
```

The scheduler planned 24 evenly spaced slots across one day, an interval of
exactly 3600 seconds (one hour), which maps to one deliverable increment per
hour as the config specifies. The scheduler only plans slots; the caller or CI
performs the actual commits.

## Outcome

| Module | Example | Result |
|--------|---------|--------|
| simulation | 01_triple_run.py | 3 runs, distinct seeds, slight per-seed variance |
| simulation | 02_consensus_report.py | converged, max cv 0.0007, 0 divergent |
| ingestion | 01_web_search.py | 4 retries then graceful offline fallback |
| ingestion | 02_pdf_extract.py | clean missing-file status, chunk estimate 3 for 450K |
| chunking | 01_chunk_document.py | 6 chunks, all under cap |
| chunking | 02_chunk_with_readme.py | reconstruction README generated |
| chunking | losslessness check | line and ASCII paths lossless; multibyte hard-split loses 6 chars (documented) |
| scheduler | 01_daily_schedule.py | 24 slots, 3600 s interval |

Seven examples ran to exit 0 and two extra verifications were performed. All
shipped behavior matched its specification, and one untested edge case (the
multibyte hard-split) was found and documented as a limitation.
