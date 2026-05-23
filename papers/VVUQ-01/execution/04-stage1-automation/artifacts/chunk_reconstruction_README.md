# Chunks of `big_document.md`

`big_document.md` exceeded the 200K per-file cap and was autochunked into 4 pieces (63890 bytes total).

## Chunks

| Order | File | Bytes |
|-------|------|-------|
| 1 | document_001.md | 19989 |
| 2 | document_002.md | 19994 |
| 3 | document_003.md | 19994 |
| 4 | document_004.md | 3913 |

## Reconstruction

Concatenate the chunks in order to rebuild the original file:

```bash
cat document_001.md document_002.md document_003.md document_004.md > big_document.md
```

