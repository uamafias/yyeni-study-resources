# 4. Source-to-target migration map

Two layers: **13 deterministic rules** that cover every file in the repository, and a **file-level map** for the 9609 AS pilot that will be executed first.

## 4.1 Coverage check

| Rule | Source | Files | Target |
|---|---|---:|---|
| R1 | `YYeni_Study_Resource_Generation_Standard_v0.1.0/**` | 45 | `standard/v0.1.0-draft/**` |
| R2 | `Syllabi/BOTSWANA (BGCSE)/**` | 29 | `archive/out-of-scope/botswana-bgcse/**` |
| R3 | `Syllabi/Cambridge Curricula/**` | 50 | `sources/cambridge/<level>/<code>-<slug>/syllabus/` |
| R4 | `Syllabi/Namibian Curricula/**` | 76 | `sources/namibia/<route>/<code>-<slug>/syllabus/` |
| R5 | `Syllabi/GCSE (UK)/**` | 3 | `sources/gcse-uk/<board>-<code>-<slug>/syllabus/` |
| R6 | `Question Banks/Cambridge Curricula/**` | 1,848 | `sources/cambridge/<level>/<code>-<slug>/assessment/<yyyy>/<series>/<kind>/` |
| R7 | `Question Banks/Namibian Curricula/**` | 556 | `sources/namibia/<route>/<code>-<slug>/assessment/<yyyy>/` |
| R8 | `Question Banks/Namibian Examiner Reports/**` | 13 | `sources/namibia/<route>/_examiner-reports/<yyyy>/` |
| R9 | `Revision Notes/**` | 615 | `sources/<board>/<level>/<code>-<slug>/supporting/<set-slug>/` |
| | **Total** | **3,235** | |

3,235 of 3,235 files assigned; no file matches two rules. Four override rules act on subsets of the above rather than adding files:

| Rule | Applies to | Effect |
|---|---|---|
| R10 | 20 verified byte-identical duplicates | one canonical copy migrates; the rest go to `archive/duplicates/2026-08-31/` with `provenance.json` |
| R11 | 16 corrupt / empty / encrypted files | go to `sources/_quarantine/2026-08-31/` instead of their rule target |
| R12 | 148 empty directories | not recreated |
| R13 | 5 × `.DS_Store`, 1 × `~$220-M1.docx` | deleted (the only deletions in this plan) |

## 4.2 Rule detail

### R1 — standard package
Straight move, contents unchanged. `.DS_Store` inside it is dropped by R13, so 45 files become 45 files at the new path. After the move, `standard/v0.1.0-draft/` is read-only; the next standard revision becomes `standard/v0.2.0/`, never an edit in place.

### R2 — Botswana BGCSE
Out of scope per the agreed route list, and there is no BGCSE question bank or note set to orphan. Preserved rather than deleted so a future decision to include it costs a move, not a re-acquisition.

### R3 — Cambridge syllabi (50 files)
Level from the parent folder: `Cambridge AS & A Level` → `as-a-level`, `IGCSE Cambridge ` → `igcse`, `Cambridge Lower Secondary (7-9)` → `lower-secondary`.

**This rule needs human input.** 30 of the 50 filenames contain no syllabus code, so the code must come from opening the file. Every one of the 44 qualification syllabi was already opened during this inspection to read its exam years and version, and `data/syllabus_currency.json` records the result — but the *code* still has to be mapped, and for a few files the subject itself is ambiguous (`AS & A Level English Syllabus.pdf` could be 9093 First Language or 8021 General Paper; `German Language Syllabus.pdf` versus `German 2025-2027-syllabus.pdf`).

Proposal: R3 runs semi-automatically. A per-file mapping table is generated in `operations/migration/r3-syllabus-code-map.csv` with the code pre-filled where the filename or the PDF title gives it unambiguously, blank where it does not, and no file moves until every row has a code. Estimated manual rows: 12–18.

Target filename: `cie-<code>-syllabus-v<version>-<firstyear>-<lastyear>.pdf`. Where the exam window has passed, the file lands in `archive/superseded-syllabi/cambridge/<code>/` instead — currently **zero** files, since the earliest window still runs to 2026, but 25 files will move there after the November 2026 series (document 02 §2.4).

### R4 — Namibian syllabi (76 files)
Route from the parent folder: `SP Grade 4-7 Namibia` → `sp`, `JSC (Legacy)` → `jsc-legacy`, `JSC (New)` → `jsc`, `NSSCAS` → `nsscas`, `NSSCO (New)` → `nssco`.

Most Namibian syllabus filenames already carry the code (`NSSCAS_8245_Business_Studies_...`, `NSSCO_6144_Business_Studies_...`), so this rule is largely automatic. Three specific interventions:

- `Syllabi/Namibian Curricula/NSSCO (New)/JSAgriculturalScienceSyllabusDecember2025.pdf` is a *Junior Secondary* syllabus misfiled under NSSCO (document 02 §2.1 C). It migrates to `sources/namibia/jsc/`, not `nssco/`, and the JSC copy is the canonical one.
- `JSAccountingSyllabusDecembe2025.docx` and `.pdf` are the same syllabus in two formats. Both migrate; the PDF is canonical, the DOCX gets `quality_flags: ["duplicate_format_of_canonical_pdf"]` in the inventory.
- `(1)` suffixes on four JSC/SP filenames are stripped.

### R5 — GCSE (UK) (3 files)
Board and specification code from the filename: `aqa-8464-combined-science`, `edexcel-1ma1-mathematics`, `pearson-1hi0-history`. The AQA file is AES-encrypted, so under R11 it goes to quarantine, not to `sources/`, until someone confirms text extraction is possible within its permissions. **Net result: GCSE lands 2 of 3 files.** Document 06 R-08 covers what this route actually needs.

### R6 — Cambridge question banks (1,848 files) — fully automatic
Every filename matches `^(?<code>\d{4})_(?<series>[smw])(?<yy>\d{2})_(?<kind>qp|ms|in|er|sf|gt|ci|rp)_(?<paper>\d)(?<variant>\d)`, with optional download debris (`-1`, `-2`, `(1)`) before the extension. Target:

```text
sources/cambridge/<level>/<code>-<slug>/assessment/20<yy>/<series><yy>/<kind>/<code>_<series><yy>_<kind>_<papervariant>.pdf
```

Example: `Question Banks/Cambridge Curricula/Cambridge AS and A Level/Business Studies (9609)/2024/Oct-Nov (Variant 1)/9609_w24_qp_31.pdf`
→ `sources/cambridge/as-a-level/9609-business/assessment/2024/w24/qp/9609_w24_qp_31.pdf`

Three properties make this the safest rule in the plan:

1. **The path is derived from the filename, not the folder.** Document 02 §2.1 D found three papers whose folder said one variant and whose filename said another; in every case the filename was right. Where they disagree the rule follows the filename and writes a line to `operations/migration/r6-path-filename-mismatch.log`.
2. **The variant folder disappears**, because the variant is already the second digit of the paper number. `2024/Oct-Nov (Variant 1)/…_qp_31` and `2024/Oct-Nov (Variant 2)/…_qp_32` both land in `assessment/2024/w24/qp/`, and 30 of the 148 empty directories were variant folders that never had content.
3. One file is a `.docx` whose stem follows the convention (`0460_s24_qp_11.docx`). It migrates under R6 with `quality_flags: ["unexpected_format_for_official_paper"]` and `authority_category: uncertain` — an official Cambridge paper should not be a Word document.

### R7 — Namibian question banks (556 files) — rename required
Current filenames are unreliable as identifiers (document 02 §2.2: `1100-P1.pdf` exists 7 times). Target:

```text
sources/namibia/<route>/<code>-<slug>/assessment/<yyyy>/<code>-p<paper>-<yyyy>-<kind>.pdf
```

Example: `Question Banks/Namibian Curricula/NSSCO (New)/Business Studies (6144)/2022/NSSCO - Business Studies Paper 1 6144-1 - First Proof 08.04.2022.pdf`
→ `sources/namibia/nssco/6144-business-studies/assessment/2022/6144-p1-2022-qp.pdf`

The original filename, the "First Proof" label and the proof date are **not discarded** — they move into the source inventory as `original_filename`, `quality_flags: ["internal_proof_label"]` and `notes`. That is where they belong: they are metadata about provenance, and 170 files carrying an internal draft label in their name is a live authority question (document 06 R-05), not a naming preference.

Where the paper number or kind cannot be parsed, the file lands at `assessment/<yyyy>/unparsed/` under its original name and is listed in `operations/migration/r7-unparsed.csv` for manual resolution. Expected volume: the JSC legacy codes (`1100-P3-LT`, `1131-P3-TT` — LT/TT are listening/talking variants) will need a small lookup table.

### R8 — Namibian examiner reports (13 files)
Each report is an all-subject volume, so it belongs at route level, not subject level:

```text
sources/namibia/<route>/_examiner-reports/<yyyy>/<route>-examiner-report-<yyyy>.pdf
```

Combined with R10 this collapses 16 files into 4 and reclaims 279 MB. Subjects that mine a report reference it by `source_id` from their own inventory; nothing is copied.

### R9 — Revision notes (615 files) → `supporting/`
The single largest interpretive rule, because "Revision Notes" mixes levels, boards and provenance under folder names that carry no version data.

```text
sources/<board>/<level>/<code>-<slug>/supporting/<set-slug>/<original-filename>
```

- Board and level from the `Revision Notes/<level>/` segment: `AS` and `IGCSE` → `cambridge/as-a-level` and `cambridge/igcse`; `NSSCAS`, `NSSCO`, `JSC`, `SP` → the matching `namibia/` route.
- Subject code from the parentheses in the folder name where present (11 of 49 subject folders lack one — `IGCSE History`, `NSSCO Agriculture`, `NSSCAS Accounting`, `Subject Resources Grade 8/9`, the four SP grades — and need the same semi-automatic table as R3).
- `<set-slug>` preserves provenance groupings that the current folders encode by accident. For the pilot: `chapter-notes-2019`, `single-topic-2020`, `znotes-v2`, `revision-guide-scan`.
- **Original filenames are preserved under R9**, unlike R7. These are third-party documents; renaming them destroys the only attribution trail they have (`... Cambridge (CIE) IGCSE Business Revision Notes 2018 - YHZv86SrgvpNRfXK.pdf` names its source and its asset ID).
- Every file migrated under R9 gets `authority_category` of `learner_notes`, `teacher_created`, `endorsed_conceptual` or `uncertain`, plus `reuse_constraints`. This is the point at which the copyright question in document 06 R-04 becomes unavoidable, and it is better faced during migration than after publication.

Grade-based folders (`Subject Resources Grade 8`, `SP/Grade 5`) map to `namibia/jsc/_grade-8/` and `namibia/sp/grade-5/<subject-slug>/` — grade is the organising axis there, not subject code.

### R10 — duplicates
Only files with a verified matching SHA-256 are treated as duplicates. The canonical copy is chosen by: (1) the copy whose filename matches the convention; (2) the copy whose folder matches its filename; (3) the shortest path. Non-canonical copies go to `archive/duplicates/2026-08-31/<original-relative-path>` with `provenance.json` recording the hash and the kept path.

### R11 — quarantine
16 files (document 02 §2.3) plus anything that fails a post-move hash check. `quarantine.json` records path, size, hash, failure reason and the acquisition action needed. Quarantined items are listed in `operations/acquisition/` so that "the insert is missing" becomes a task rather than a silent zero-byte file.

### R12 / R13
Empty directories are not recreated; the target tree is created by the files that land in it. `.DS_Store` files and the Word lock file `~$220-M1.docx` are deleted.

## 4.3 File-level map for the pilot (Stage 2 of the migration)

All 20 files, copied — not moved — so the legacy tree stays intact while the pilot is validated. SHA-256 for each is in `data/source_inventory.cie-9609-as-2026-2028.candidate.json`.

| # | Current path (relative to root) | Target path | Rule |
|---:|---|---|---|
| 1 | `Syllabi/Cambridge Curricula/Cambridge AS & A Level/Business Studies 2026-2028-syllabus.pdf` | `sources/cambridge/as-a-level/9609-business/syllabus/cie-9609-syllabus-v2-2026-2028.pdf` | R3 |
| 2 | `Question Banks/.../Business Studies (9609)/2020/Oct-Nov (Variant 1)/9609_w20_ms_21.pdf` | `sources/cambridge/as-a-level/9609-business/assessment/2020/w20/ms/9609_w20_ms_21.pdf` | R6 |
| 3 | `.../2023/May-June (Variant 3)/9609_s23_ms_43.pdf` | `.../assessment/2023/s23/ms/9609_s23_ms_43.pdf` | R6 |
| 4 | `.../2024/May-June (Variant 3)/9609_s24_qp_33.pdf` | `.../assessment/2024/s24/qp/9609_s24_qp_33.pdf` | R6 |
| 5 | `.../2024/Oct-Nov (Variant 1)/9609_w24_qp_31.pdf` | `.../assessment/2024/w24/qp/9609_w24_qp_31.pdf` | R6 |
| 6 | `.../2024/Oct-Nov (Variant 2)/9609_w24_qp_32.pdf` | `.../assessment/2024/w24/qp/9609_w24_qp_32.pdf` | R6 |
| 7–10 | `Revision Notes/AS/Business (9609)/Chapter Wise Notes .../chapter-1..4-*.pdf` | `.../supporting/chapter-notes-2019/<same filename>` | R9 |
| 11–18 | `Revision Notes/AS/Business (9609)/AS and A Level Business Chapter Wise Notes .../*.pdf` (8 files) | `.../supporting/single-topic-2020/<same filename>` | R9 |
| 19 | `Revision Notes/AS/Business (9609)/cie-as-business-9609-v2-znotes.pdf` | `.../supporting/znotes-v2/cie-as-business-9609-v2-znotes.pdf` | R9 |
| 20 | `Revision Notes/AS/Business (9609)/cambridge international as and a level business revision guide.pdf` | `.../supporting/revision-guide-scan/<same filename>` | R9 |

Note what files 4, 5 and 6 demonstrate: three A Level Paper 3 question papers migrate into `sources/`, because they are genuine 9609 material, but the inventory marks them `status: out_of_scope` and `levels: ["A Level"]`. The AS-only route must not mine them (RS-02), and the deterministic scope check (document 08, C4) will fail the build if an AS objective cites them. Keeping the file while excluding it from scope is the distinction the current folder cannot express and the new one can.

## 4.4 What the pilot map does not produce

After Stage 2 the pilot has a validated source inventory and 20 correctly placed sources. It does **not** have assessment evidence, because there is nothing to mine: no AS question paper, no examiner report, no specimen. `work/cie-9609-as-2026-2028/assessment-evidence/assessment_evidence.json` will be created with an explicit `gaps` list rather than left absent, so the blocker is data in the build manifest rather than a missing file someone might overlook.
