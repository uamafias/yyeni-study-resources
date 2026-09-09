# 2. Duplicate and outdated-source report

Method: SHA-256 computed for every file sharing a byte size with at least one other file (71 files — the complete candidate set for byte-identical duplication), plus basename collision analysis across the whole tree, plus exam-year and version data read from inside every syllabus PDF.

## 2.1 Byte-identical duplicates

**12 duplicate groups, 20 redundant files, 282.0 MB reclaimable.**

### Group A — Namibian NSSCO examiner reports held four times each (16 files, 279 MB)

Each annual report is a single all-subjects volume that was copied into three subject folders *and* the dedicated examiner-reports branch:

| Year | Pages | Size | Copies |
|---|---:|---:|---|
| 2020 | 483 | 24.0 MB | Biology 6116, Business Studies 6144, Chemistry 6117, `Namibian Examiner Reports/NSSCO (New) /2020/NSSCO(New) Examiners Report 2020 (1).pdf` |
| 2021 | 504 | 19.3 MB | same three subjects + `.../2021/NSSCO New 2021 (Gr 11).pdf` |
| 2022 | 590 | 14.4 MB | same three subjects + `.../2022/NSSCO 2022.pdf` |
| 2023 | 687 | 33.9 MB | same three subjects + `.../2023/Examiners Report NSSCO 2023.pdf` |

This is the whole of the 282 MB. It is also a design signal: an all-subject examiner report is a **route-level** artifact, not a subject-level one. Copying it per subject is what created the duplication, and the target tree removes the incentive (rule R8: one copy at `sources/namibia/nssco/_examiner-reports/<year>/`, referenced by `source_id` from every subject that mines it).

### Group B — the same syllabus under two names (6 files, 3 groups)

| Kept name | Duplicate name |
|---|---|
| `Cambridge AS & A Level/History-2026-syllabus.pdf` | `Cambridge AS & A Level/AS History (9489).pdf` |
| `IGCSE Cambridge /History 2024-2026-syllabus.pdf` | `IGCSE Cambridge /IGCSE History Syllabus.pdf` |
| `IGCSE Cambridge /Design & Technology-2024-2026-syllabus.pdf` | `IGCSE Cambridge /IGCSE Design & Technology Syllabus.pdf` |

Both members of each pair are byte-identical, so there is no version question — only a naming one, which document 05 settles.

### Group C — cross-route syllabus copy (2 files)

`Syllabi/Namibian Curricula/JSC (New)/JSAgriculturalScienceSyllabusDecember2025 (1).pdf` is byte-identical to `Syllabi/Namibian Curricula/NSSCO (New)/JSAgriculturalScienceSyllabusDecember2025.pdf`. This is a **misfile, not a duplicate**: a *Junior Secondary* syllabus is sitting in the NSSCO (senior secondary) folder. Deleting the "duplicate" would be the wrong call; the NSSCO copy is the one to remove, and NSSCO Agricultural Science already has its own syllabus (`NSSCO_Agricultural_Science_syllabus.pdf`).

### Group D — Cambridge paper filed under two variants (4 files, 2 groups)

- `Law (9084)/2022/Oct-Nov (Variant 1)/9084_w22_qp_12.pdf` = `Law (9084)/2022/Oct-Nov (Variant 2)/9084_w22_qp_12.pdf` — the filename says variant 2, so the copy under Variant 1 is misfiled.
- `Travel & Tourism (9395)/2024/Oct-Nov (Variant 1)/9395_w24_in_42.pdf` = `.../Variant 3/9395_w24_in_42-1.pdf` — filename says variant 2; both locations are wrong.
- `Geography (9696)/2023/May-June (Variant 2)/9696_s23_ms_33-1.pdf` = `.../Variant 3/9696_s23_ms_33.pdf` — filename says variant 3, so the Variant 2 copy is misfiled.

**These three cases prove the folder path is less reliable than the Cambridge filename.** Migration rule R6 therefore derives the target path from the filename and treats a mismatch with the source folder as a warning to log, not an error to stop on.

### Group E — JSC entrepreneurship summary (2 files)

`Revision Notes/JSC/Subject Resources Grade 8/Entrepreneurship/ENTREPRENEURSHIP SUMMARY gr. 9 2.pdf` = `Revision Notes/JSC/Subject Resources Grade 9/ENTREPRENEURSHIP SUMMARY gr. 9 2 (2).pdf`. The content says Grade 9; the Grade 8 copy is misfiled.

## 2.2 Same filename in different folders — 67 basenames, 260 files

Almost all are Namibian legacy papers whose filenames are bare subject codes (`1100-P1.pdf` appears 7 times, `1500-P2.pdf` 6 times, `1130-P1.pdf` 6 times, and so on). In every case the copies have **different byte sizes**, i.e. they are genuinely different years of the same paper, disambiguated only by their parent year folder.

This is not duplication, but it is fragile: move one of these files out of its folder and its identity is gone. Migration rule R7 renames every Namibian paper to carry code, paper, year and kind in the filename itself.

## 2.3 Corrupt, empty and unreadable files (16)

| Count | Problem | Files |
|---:|---|---|
| 13 | **Zero bytes** — failed downloads | 6 × IGCSE Computer Science 0478 (`s20_qp_12`, `s20_qp_22`, `s20_ms_12`, `s20_ms_22`, `s20_qp_13`, `s20_ms_23`), 5 × IGCSE English 0500 (`s20_in_11`, `s20_in_21`, `s20_in_12`, `s20_in_22`, `s20_in_23`), 1 × IGCSE Business 0450 (`s20_in_23`), 1 × NSSCO English 2nd 2023 Examiners Notes |
| 1 | **AES-encrypted** | `Syllabi/GCSE (UK)/AQA-8464-SP-2016 (1).pdf` — printable and copyable, but modification is blocked; text extraction needs the permission handled explicitly |
| 1 | **Not a PDF** (1,665 bytes) | `Revision Notes/NSSCAS/NSSCAS Mathematics (8227)/y=mx+c AS Level .pdf` — the only file in that subject folder |
| 1 | **Malformed header, unreadable** | `Question Banks/.../IGCSE Geography (0460)/2020/May-June (Variant 2)/0460_s20_in_22.pdf` (267 KB) |

Because all 13 zero-byte files share a size of 0, they also share a SHA-256 and would appear as one "duplicate group" to a naive hash-only check. They are counted here as corrupt, not duplicate, and the 282.0 MB reclaimable figure excludes them.

Migration rule R11 sends all 16 to `sources/_quarantine/` with the failure reason recorded, so that no build can silently treat a zero-byte insert as "the insert exists".

## 2.4 Syllabus currency register — the finding with a deadline

Exam years and version numbers were read from inside each of the 44 Cambridge qualification syllabus PDFs (Lower Secondary curriculum frameworks excluded, as they carry no exam years).

| Last exam session | Syllabi | Status |
|---|---:|---|
| **2026** | **25** | **Expire after the November 2026 series** |
| 2027 | 11 | Usable through 2027 |
| 2028 | 8 | Current |

**Twenty-five of 44 Cambridge syllabi in this repository stop being valid after the 2026 series.** Any notes generated from them will be out of scope for 2027 candidates. The 25:

*AS & A Level:* Computer Science 9618 (v2), Pseudocode Guide (v1), English (v2), Geography 9696 (v1), Psychology (v1), History 9489 (v3, held twice), Afrikaans (v1), Travel & Tourism (v1), Sociology (v2).
*IGCSE:* Accounting (v2), Art & Design (v2), Business Studies 0450 (v2), Design & Technology (v2, held twice), Economics 0455 (v2), English 2nd (v3), English 1st (v1), Enterprise (v2), French 1st (v2), German 1st (v2), Geography (v2), History (v1, held twice), Travel & Tourism (v2).

Current through 2028 (8): AS Law 9084 v2, AS Economics 9708 v2, AS Accounting 9706 v2, **AS Business 9609 v2**, IGCSE Computer Science 0478 v5, IGCSE Biology 0610 v2, IGCSE Chemistry 0620 v1, IGCSE Physics 0625 v2.

Recommendation: the target tree encodes the exam window in the path (`sources/cambridge/as-a-level/9609-business/syllabus/`, file `cie-9609-syllabus-v2-2026-2028.pdf`), so expiry becomes visible in a directory listing rather than requiring someone to open 44 PDFs. Document 08 proposes a deterministic check that fails when any active build points at a syllabus whose last exam year has passed.

Two ambiguities remain to be resolved by opening the files, and are **not** duplicates: `Cambridge AS & A Level/Sociology 2024-2026-syllabus.pdf` (v2) versus `IGCSE Cambridge /Sociology- 2025-2027-syllabus.pdf` (v3) are different qualifications (9699 and 0495) filed in the right places; `Cambridge AS & A Level/Cambridge AS & A Level Travel & Tourism-syllabus.pdf` (v1, 2024–2026) and `IGCSE Cambridge /Travel & Tourism-2024-2026-syllabus.pdf` (v2) likewise.

## 2.5 Namibian syllabus currency

None of the Namibian syllabi declare exam years in the Cambridge style, so currency has to be read from the implementation year on the front matter:

- **NSSCO (New)**: 20 syllabi, all "to be implemented in 2019".
- **NSSCAS**: 16 syllabi, all "to be implemented in 2021".
- **JSC (New)**: 20 syllabi dated 2024 or December 2025 — this is the live junior secondary reform.
- **JSC (Legacy)**: 11 syllabi from 2016 (one from 2006). Superseded by JSC (New) but retained, correctly, because the legacy question bank (184 files) is only interpretable against them.
- **SP Grade 4–7**: 8 syllabi, implementation 2024–2025.

The legacy/new split is already modelled in the folder names, and this is the one part of the current structure that should survive migration essentially as-is. Document 03 keeps `jsc-legacy` and `nssco-legacy` as first-class source routes rather than archiving them.

## 2.6 Filename and path hygiene

| Issue | Occurrences | Example |
|---|---:|---|
| Copy suffix `(1)`, `-1`, `-2`, `(2)` | 177 path segments | `9489_s21_qp_21-3.pdf`, `2022/May-June (Variant 2)(1)` |
| Internal proof label "First Proof" | 170 files | `NSSCO - Business Studies Paper 1 6144-1 - First Proof 08.04.2022.pdf` |
| Embedded proof date | 185 files | as above |
| Leading or trailing space in a path segment | 40 | `Namibian Examiner Reports/NSSCO (New) `, `Revision Notes/AS/Business (9609)/Chapter Wise Notes ... Notes ` |
| Double space | 3 | `Revision Notes/IGCSE/Chemistry(0620)  IGCSE` |
| Misspelled subject folders and filenames | 5 | `Economis (8246)`, `Entreprenuership (8247)`, `Entreprenuership`, `AS - Business Stufies Paper 1 ...pdf`, `JSAccountingSyllabusDecembe2025` |
| Inconsistent subject-folder grammar | throughout | `Business Studies (9609)` vs `Business (9609)`; `Geography (0460) igcse` vs `IGCSE Geography (0460)`; `Math (0580) Core IGCSE` vs `Mathematics Core (0580)` |

The trailing-space segments are the operationally dangerous ones: they break shell globs, tab completion and any naive path join, and two of them sit on directories that the migration must traverse.

The 177 copy suffixes need care. Most are *not* duplicates — `9489_s21_qp_21-3.pdf` is the only copy of that paper and the `-3` is download debris. Rule R6 strips the suffix when reconstructing the canonical Cambridge filename, and flags a collision only if the stripped name already exists.

## 2.7 Question-paper / mark-scheme pairing

Across 908 Cambridge paper slots (code + series + year + paper-variant):

- 679 complete question-paper + mark-scheme pairs (and 4 slots holding only an insert booklet);
- **133 mark schemes with no question paper** — heaviest in Psychology 9990 (21), Biology 9700 (13), English 9093 (11), Chemistry 9701 (9), Physics 0625 (8), History 0470 (8), English 0500 (7);
- **92 question papers with no mark scheme** — heaviest in Mathematics 9709 (22), Psychology 9990 (22), Chemistry 0620 (7).

For assessment mining (RS-05) an unpaired artifact is half-useful: a mark scheme without its paper gives credit-worthy reasoning without the stimulus; a paper without its mark scheme gives the task without the standard. Both are worth recording as gaps in the assessment-evidence map rather than silently accepting. Business 9609 is the extreme case, below.

## 2.8 The pilot subject: Cambridge AS Business 9609

Everything the repository holds for the pilot, in full:

**Syllabus (1 file, correct and current).** `Business Studies 2026-2028-syllabus.pdf` — opened and verified as **Version 2, published December 2025, for exams in 2026, 2027 and 2028**, 46 pages, clean text layer. This matches `profiles/cambridge_9609_as_2026_2028.yaml` exactly, so RS-02 scope lock can be satisfied from material already on disk.

**Assessment material (5 files, and this is the problem).**

| File | Paper | In AS scope? |
|---|---|---|
| `9609_w20_ms_21.pdf` | AS Paper 2 mark scheme, 2020 Oct/Nov | Yes — but the question paper is absent |
| `9609_s23_ms_43.pdf` | A Level Paper 4 mark scheme | No |
| `9609_s24_qp_33.pdf` | A Level Paper 3 | No |
| `9609_w24_qp_31.pdf` | A Level Paper 3 | No |
| `9609_w24_qp_32.pdf` | A Level Paper 3 | No |

The AS route is assessed by Papers 1 and 2. **The repository contains no AS question paper for 9609, and one orphan AS mark scheme from a series that predates the current syllabus edition.** There are no examiner reports and no specimen papers. RS-05 cannot be satisfied, and RS-31 blocks publication while a required stage is incomplete — which is exactly the behaviour the standard was designed to produce, but it means the pilot's first real deliverable is *acquiring papers*, not generating notes.

**Supporting notes (14 files).** Three distinct sets:

1. `Chapter Wise Notes .../chapter-1..4` — four Word-2013 PDFs (April 2019), good text layer, 237 pages combined. Two problems, both confirmed by reading them: the chapter titles use **superseded syllabus wording** ("People in Organisations", where 9609 v2 topic 2 is *Human resource management*; "Operations and Project Management", where AS topic 4 is *Operations management* and project management is A Level), and chapter 2 carries **legacy topic numbering** ("1.6 MANAGEMENT AND LEADERSHIP"). There is **no chapter 5**, so topic 5 *Finance and accounting* — a fifth of the AS course — has no chapter notes at all. Surface quality is also weak ("BUSINESS AND IT'S ENVIRONMENT", "MANGEMENT", "goods managers usually the skills").
2. `AS and A Level Business Chapter Wise Notes .../` — eight single-topic watermarked PDFs (August 2020, producer "A-PDF Watermark 3.9.0") covering Boston matrix, delegation, employment legislation, financing a business, HRM, HR planning, IMF/WTO, leadership. Overlapping subject matter with set 1, different provenance, unattributed.
3. Two whole-course documents: `cie-as-business-9609-v2-znotes.pdf` (24 pages, partial text layer, the **only** supplied source with substantive topic 5 finance content) and `cambridge international as and a level business revision guide.pdf` (40 pages at 36 chars/page — a **scan**, OCR required, apparently a commercial publication whose licence is unverified).

Applying RS-10/RS-11 to this evidence, the honest prediction is that most of the AS course will be `regenerate` or `generate-gap` rather than `retain` or `refine`, and that topic 5 is a near-total gap. That is a legitimate outcome under the standard — but it should be stated in the topic contract before authoring starts, not discovered at review.

A schema-valid Stage 2 inventory for all 20 of these sources, with authority categories, extraction states, quality flags and reuse constraints filled in, is at `data/source_inventory.cie-9609-as-2026-2028.candidate.json`.

## 2.9 Recommended dispositions

| Action | Files | Rule |
|---|---:|---|
| Archive verified byte-identical duplicates (keep one canonical copy) | 20 | R10 |
| Quarantine corrupt / empty / unreadable | 16 | R11 |
| Archive out-of-scope jurisdiction (Botswana BGCSE) | 29 | R2 |
| Re-file the six misfiled files identified in §2.1 C–E | 6 | R6/R7 with warning log |
| Flag 25 Cambridge syllabi as expiring after the 2026 series | 25 | document 08 check C3 |
| Delete `~$220-M1.docx` (Word lock file) and 5 × `.DS_Store` | 6 | R13 |
| Do not recreate empty directories | 148 dirs | R12 |

No deletion of educational content is proposed anywhere in this package. Duplicates move to `archive/duplicates/` with a provenance record; the only outright deletions are a Word lock file and macOS metadata.
