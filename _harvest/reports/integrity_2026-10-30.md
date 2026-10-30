# Corpus integrity sweep

**Root:** `/Users/professor/Documents/YYeni Study Resources`  
**Date:** 2026-10-30  
**Method:** magic-byte check + pypdf parse + text sample over the first 8 pages (floor: 20 words/page). Diagnose-only — no file is modified.

| Bucket | Meaning | Count |
|---|---|---|
| A | CORRUPT — re-acquire | 6 |
| B | LIKELY IMAGE-ONLY — OCR if text is needed | 0 |
| C | OK | 0 |
| | **Total scanned** | **6** |

## Bucket A — CORRUPT · 6 files

| Path | Size | Pages | Words | Signature |
|---|---|---|---|---|
| `work/nam-6137-nssco-2026/assets/sources/photos/VIS-6137-4.2-05_original.jpg` | 5.1 MB | 0 | 0 | corrupted binary header (not %PDF, not HTML) |
| `work/nam-6137-nssco-2026/assets/sources/photos/VIS-6137-4.2-06_original.jpg` | 9.2 MB | 0 | 0 | corrupted binary header (not %PDF, not HTML) |
| `work/nam-6137-nssco-2026/assets/sources/photos/VIS-6137-4.2-07_original.jpg` | 7.3 MB | 0 | 0 | corrupted binary header (not %PDF, not HTML) |
| `work/nam-6137-nssco-2026/assets/sources/photos/VIS-6137-4.2-08_original.jpg` | 863.8 KB | 0 | 0 | corrupted binary header (not %PDF, not HTML) |
| `work/nam-6137-nssco-2026/assets/sources/photos/VIS-6137-4.2-09_original.jpg` | 7.1 MB | 0 | 0 | corrupted binary header (not %PDF, not HTML) |
| `work/nam-6137-nssco-2026/assets/sources/photos/VIS-6137-4.2-10_original.jpg` | 5.4 MB | 0 | 0 | corrupted binary header (not %PDF, not HTML) |

---
**Note (Claude, 30 Oct 2026):** the six "corrupt" verdicts above are false positives. `harvest verify` currently recognises only PDF, HTML and zip headers, so it labels any JPEG as a "corrupted binary header". All six files (`work/nam-6137-nssco-2026/assets/sources/photos/VIS-6137-4.2-0[5-9]_original.jpg` and `…-10_original.jpg`):
- decode fully with Pillow;
- have SHA-1 hashes equal to those Wikimedia Commons records for the source files.

The checks are recorded in `work/nam-6137-nssco-2026/assets/checklists/ITEM-6137-4.2-02[7-9]*.md`, `…-03[0-2]*.md` and the specs. The toolkit lacks image verification; that is reported as a toolkit gap, not repaired here.
