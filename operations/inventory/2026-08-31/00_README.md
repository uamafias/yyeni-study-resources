# YYeni Study Resources — Inspection Package (2026-08-31)

**Produced for:** `YYeni_Study_Resource_Generation_Standard_v0.1.0` → `prompts/CLAUDE_COWORK_HANDOFF.md`
**Status:** Proposal for review. **No existing file has been created, deleted, renamed, moved or modified.**
**Scope agreed with Vitalis:** repo-wide architecture; in-scope routes are **Cambridge, Namibian and GCSE (UK)**. Botswana BGCSE is treated as out of scope and archived rather than deleted.

## What is in this folder

| File | Handoff output | Contents |
|---|---|---|
| `01_current_folder_inventory.md` | 1 | Full census of the folder: 3,235 files, 4.0 GB, branch-by-branch counts, extraction quality, empty directories |
| `02_duplicate_and_outdated_source_report.md` | 2 | Byte-identical duplicates, corrupt files, superseded syllabus editions, syllabus expiry register |
| `03_proposed_target_folder_tree.md` | 3 | Target architecture separating immutable sources / generated work / published releases |
| `04_source_to_target_migration_map.md` | 4 | 13 deterministic migration rules covering all 3,235 files, plus the file-level map for the 9609 AS pilot |
| `05_naming_and_versioning_convention.md` | 5 | Path, filename, identifier and release-versioning rules |
| `06_risks_and_open_questions.md` | 6 | 14 risks with severity, and the decisions the team must take before migration |
| `07_staged_migration_plan.md` | 7 | 9 stages with preconditions, verification and rollback; backup strategy |
| `08_validation_plan.md` | 8 | How `validate_project.py` and the schemas are used, plus three proposed repository-level checks |
| `data/raw_file_census.json` | — | Machine-readable census: every file with size, mtime, page count, text-extraction sample; plus empty directories |
| `data/syllabus_currency.json` | — | Exam years and version numbers extracted from inside each syllabus PDF |
| `data/source_inventory.cie-9609-as-2026-2028.candidate.json` | — | A real, schema-valid Stage 2 source inventory for the pilot qualification (20 sources) |

## How these figures were produced

Everything was measured on the actual folder, not estimated:

- directory walk with `os.walk`, excluding `.DS_Store`;
- SHA-256 computed for every file sharing a byte size with another file (the complete candidate set for byte-identical duplication) — 71 files hashed;
- SHA-256 computed in full for all 20 pilot sources;
- `pdfinfo` for page count, producer, creator and encryption state on all 3,177 PDFs;
- `pdftotext` on the first three pages of all 3,177 PDFs to measure characters per page, the proxy used here for text-layer quality;
- `pdftotext` on the full text of each syllabus PDF to read its declared exam years and version number.

The raw census is included so any number in these documents can be re-derived rather than trusted.

## Verification performed

- The package's own test suite was re-run independently in a clean environment with `jsonschema>=4.18`: **13 passed**, and `validate_project.py` on the bundled fixture reports **Errors: 0 | Warnings: 0 | RESULT: PASS**.
- `data/source_inventory.cie-9609-as-2026-2028.candidate.json` validates against `schemas/source_inventory.schema.json` (draft 2020-12).
- The migration map in document 04 accounts for **3,235 of 3,235 files** with no file assigned to two rules and none unassigned.
- The Cambridge 9609 syllabus on disk was opened and confirmed to be **Version 2, published December 2025, for exams in 2026, 2027 and 2028** — an exact match for `profiles/cambridge_9609_as_2026_2028.yaml`.

## The one thing to read first

The pilot qualification cannot reach `PUBLISHED` on the material currently in this folder. There is **no AS-level Business 9609 question paper** in the repository — only one orphan AS mark scheme, plus four A Level papers that the AS-only route excludes. RS-05 (assessment-material mining) and RS-31 (hard release gates) therefore both bite. Details in document 02, §5 and document 06, risk R-01.

## After Stage 1 of the migration

This folder becomes `operations/inventory/2026-08-31/`. Keep it: it is the pre-migration state of record and the rollback reference.
