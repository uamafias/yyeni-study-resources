# Corpus integrity sweep

**Root:** `/Users/professor/Documents/YYeni Study Resources`  
**Date:** 2026-09-28  
**Method:** magic-byte check + pypdf parse + text sample over the first 8 pages (floor: 20 words/page). Diagnose-only — no file is modified.

| Bucket | Meaning | Count |
|---|---|---|
| A | CORRUPT — re-acquire | 0 |
| B | LIKELY IMAGE-ONLY — OCR if text is needed | 0 |
| C | OK | 320 |
| | **Total scanned** | **320** |
