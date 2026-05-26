# File Size Pyramid (L0 to L4 plus Event Log)

The humanoid sensor record is larger than the 8-arm baseline because the 71-DOF
body adds 40 per-finger joint channels, 20 per-finger force channels, and 12
balance channels on top of the arm and perception channels. The Zenodo discipline
therefore matters more: the raw L0 archive is never committed.

## Layering

| Layer | Rate | Window | What it holds | Committed | Per-iteration size |
|-------|------|--------|---------------|-----------|--------------------|
| L0 raw | 100 kHz force, 10 kHz command | 60 s | full 71-DOF per-tick stream | No (Zenodo only) | pointer + SHA-256 only |
| L1 publication sample | 50 Hz | 60 s | one hand-finger slice for figures | Yes | under 0.5 MB |
| L2 aggregate | 1 Hz | 60 s | per-second body summary | Yes | under 0.2 MB |
| L3 per-phase | 1 per phase | 8 phases | per-phase per-hand rollup | Yes | under 0.1 MB |
| L4 per-anastomosis | 1 per event | 3 events | PJ / HJ / GJ ring-tension rollup | Yes | under 0.05 MB |
| Event log | event-driven | per iteration | gate, safety, balance, fault events | Yes | under 0.1 MB |

## Caps

- Every committed file under 10 MB (GitHub).
- Every committed Parquet under 5 MB (soft cap). This tree commits plain CSV and
  JSONL samples to stay byte-stable and lint-friendly; Parquet is reserved for
  the local and Zenodo paths.
- L0 raw is deposited to Zenodo only. Each committed iteration carries a
  `run_NNNNN_L0_raw.zenodo_pointer.json` with the deposition DOI and the L0
  SHA-256, written by `src/zenodo/patch_pointers.py`.

## Per-iteration committed set

```
data/iterations/
  index.jsonl                                one row per iteration
  run_00000_L3_phase.csv                     per-phase per-hand rollup (sample)
  run_00000_events.csv                       event log (sample)
  run_00000_vvuq.csv                         per-gate decision (sample)
  run_00000_L0_raw.zenodo_pointer.json       DOI + SHA-256 manifest (sample)
```

Only iteration 00000 commits its per-iteration detail files as a worked sample;
the remaining iterations are summarized in `index.jsonl` and the release
manifest, exactly as the PDAC baseline commits a single worked sample.
