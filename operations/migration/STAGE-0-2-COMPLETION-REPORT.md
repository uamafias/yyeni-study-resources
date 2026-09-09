# Stages 0–2 completion report

**Executed:** 2026-08-31 · **Approved by:** Vitalis · **Plan:** `operations/inventory/2026-08-31/07_staged_migration_plan.md`

**Result: all three stages complete. The legacy tree is bit-for-bit unchanged — re-hashed after the work and diffed against the Stage 0 baseline: 3,235 files, 0 missing, 0 added, 0 modified.** Everything added is additive; nothing existing was moved, renamed, modified or deleted.

---

## Stage 0 — Freeze and baseline

| Item | Value |
|---|---|
| Files hashed | **3,235** |
| Total bytes | **4,260,697,886** (3.97 GiB) |
| Algorithm | SHA-256 |
| Elapsed | 17.1 s |
| Manifest | `operations/backups/pre-migration-2026-08-31/manifest.sha256` |
| Manifest's own SHA-256 | `8eb958b24f9772859bdad047d6f6d889c0b219e1c0f026a053ebd4e4f40db1f6` |

The file count matches the 2026-08-31 inventory exactly. The manifest hash is recorded in `operations/migration/state.json`, so a tampered manifest is detectable.

**⚠ Outstanding: the off-machine backup is still unverified.** Stages 0–2 are additive, so nothing was at risk. **Stage 3 is the first stage that moves an existing file and must not run until a verified off-machine copy of this folder exists.**

## Stage 1 — Target skeleton

Created the six zones and their second-level directories: `standard/`, `shared/{subject-profiles,glossaries,templates}/`, `sources/{cambridge/{as-a-level,igcse,lower-secondary},namibia/{sp,jsc,jsc-legacy,jssee,nssco,nssco-legacy,nsscas},gcse-uk,_quarantine}/`, `work/`, `releases/`, `operations/{inventory,migration,backups,acquisition}/`, `archive/{out-of-scope,superseded-syllabi,duplicates}/`.

The inspection package moved from `_inventory/2026-08-31/` to **`operations/inventory/2026-08-31/`**, as the plan specified. *(The now-empty `_inventory/` directory could not be removed: the shell used here cannot delete on this machine. Remove it by hand, or it goes with the empty-directory sweep in Stage 7.)*

### `shared/subject-slugs.csv` — the canonical subject table

Built from the folder evidence, not invented: **62 subjects with a code confirmed in a folder name**, and **52 subject folders that carry no code and need one**.

It immediately earns its place. Aliases it found for the same subject:

- 9609 → `Business (9609)` **and** `Business Studies (9609)`
- 0450 → `Business Studies (0450)` **and** `IGCSE Business Studies (0450)`
- 0460 → `Geography (0460)`, `Geography (0460) igcse` **and** `IGCSE Geography (0460)`
- 9093 → `English 1st (9093)` **and** `English Language (9093)`
- 9709 → four folders (`Pure Mathematics 1`, `Pure Mathematics 2`, `(9709) Mechanics Mathematics`, `(9709) Probability and Statistics`), all one syllabus; slug normalised to `mathematics`

### `operations/migration/r3-syllabus-code-map.csv` — brought forward from Stage 4

129 syllabus files (Cambridge, Namibian, GCSE), each with its declared version, declared exam years and last exam year read from inside the PDF:

| Code status | Files |
|---|---:|
| Code present in the filename | 18 |
| Derived from question-bank folder evidence — **confirm before use** | 44 |
| No code derivable — needs a human | 66 |

Better than the estimate in the migration map. **Cambridge needs only 11 manual rows** (2 AS/A Level, 7 IGCSE, 2 Lower Secondary), not 12–18. The remaining 53 are Namibian: JSC, JSC-legacy and SP syllabi genuinely do not carry subject codes, so those need a code list from NIED/DNEA rather than a reading of the files.

Rows whose last exam year is 2026 are flagged `EXPIRES_AFTER_2026` in the CSV — 25 of them, matching the syllabus currency register.

## Stage 2 — Pilot copy-forward

**20 of 20 files copied, 20 of 20 hash-verified**, each against its Stage 0 baseline hash before the copy and against the source again after. Report: `operations/migration/stage2-copy-report.json`.

```text
sources/cambridge/as-a-level/9609-business/
  syllabus/cie-9609-syllabus-v2-2026-2028.pdf
  assessment/2020/w20/ms/9609_w20_ms_21.pdf
  assessment/2023/s23/ms/9609_s23_ms_43.pdf
  assessment/2024/s24/qp/9609_s24_qp_33.pdf
  assessment/2024/w24/qp/9609_w24_qp_31.pdf   9609_w24_qp_32.pdf
  supporting/chapter-notes-2019/      (4 files)
  supporting/single-topic-2020/       (8 files)
  supporting/znotes-v2/               (1 file)
  supporting/revision-guide-scan/     (1 file)
```

The variant folders vanished as predicted: `2024/Oct-Nov (Variant 1)/…_qp_31` and `Variant 2/…_qp_32` both landed in `assessment/2024/w24/qp/`, because the variant is already the second digit of the paper number.

### Workspace created — `work/cie-9609-as-2026-2028/`

| Artifact | Status |
|---|---|
| `qualification-profile.yaml` | frozen copy; **validates** against `qualification_profile.schema.json` |
| `subject-profile.yaml` | frozen copy of the Business subject profile |
| `inventory/source_inventory.json` | 20 sources, unique IDs, full SHA-256, page counts, measured extraction quality, authority categories, quality flags, `reuse_constraints`; **validates** against `source_inventory.schema.json` |
| `assessment-evidence/assessment_evidence.json` | `status: "unavailable"`, `records: []`; **validates**. Detail in `GAPS.md` |
| `builds/stage-state.json` | pipeline state `INVENTORIED`; publication `BLOCKED` under RS-31 |
| `builds/NO-MANIFEST-YET.md` | why a schema-valid build manifest cannot exist yet |

### Scope lock verified (RS-02)

Read back from the frozen profile: board Cambridge International Education · code **9609** · syllabus **version 2** · exam years **2026, 2027, 2028** · route **AS_ONLY** · included papers **P1, P2** · excluded **P3, P4** · AO weights P1 35/30/20/15 and P2 30/30/20/20. This matches the syllabus PDF on disk, which states Version 2, published December 2025, for exams in 2026, 2027 and 2028.

Four A Level papers now live in `sources/` while carrying `status: out_of_scope` and `levels: ["A Level"]` — the distinction the old folder structure could not express.

---

## Acceptance criteria — met

Document 08 §8.4 said the pilot succeeds when the validator blocks publication **for the right reasons**. It does:

- ✅ source inventory schema-valid, 20 sources, unique IDs, hashes present
- ✅ scope lock recorded and verified
- ✅ the four A Level sources present but marked out of scope
- ⛔ assessment evidence unavailable — RS-05 unsatisfiable, no AS question paper held
- ⛔ no independent semantic review — RS-28 / RS-29
- ⛔ objective registry for topics 1.1–5.5 not built — pipeline Stage 3 not run

A PASS here would have meant the gates were not working.

---

## Three findings about the standard itself

Running the standard against real files surfaced three schema problems that a fixture cannot show. All are `v1.0` decisions.

**1. `build_manifest.schema.json` cannot express a pre-authoring build.** It requires `content_units` and `learning_items` with `minItems: 1`, plus `objective_registry`, `claim_ledger` and `qa_report` paths. `PIPELINE.md` defines `INVENTORIED`, `MAPPED` and `PLANNED` as build states, and none can be recorded in a manifest — yet Stage 5 puts the topic contract *in* the manifest and RS-32 requires every release to have one. Smallest fix: allow empty arrays and null paths while `status` is `draft`.

**2. `assessment_evidence.schema.json` cannot record a gap.** `additionalProperties: false` with only `map_id`, `status`, `records`. A map can say `unavailable` but not why, or what is missing. Given RS-05 and the release gates, "what assessment material do we not have" is exactly the fact that most needs to be machine-readable. Suggest a `gaps` array or `unavailable_reason`.

**3. `source_inventory.schema.json` has no resolvable `path`.** Only `original_filename`. After migration, a source needs both its current repository path (for a build to open it) and its pre-migration name (for provenance). The current path went into `original_filename` and the pre-migration path into `notes` — workable, but it makes `original_filename` mean two different things at two different times. Suggest adding `path` and keeping `original_filename` as history.

## One operational finding

**The validator cannot run on this machine.** It has jsonschema 3.2.0 and no pytest; `tests/requirements.txt` needs `jsonschema>=4.18`, `PyYAML>=6.0`, `pytest>=8.0`, and the shell used for this work has no network access to install them. All validation reported here was executed in an isolated environment on **hash-identical copies** of the artifacts. Before Stage 3, install the three dependencies on this machine — `pip install --user -r tests/requirements.txt`, or a venv at `operations/.venv` — so validation runs where the files live.

For reference, the standard package's own suite was re-run independently and passes: **13 passed**, and `validate_project.py` on the bundled fixture reports `Errors: 0 | Warnings: 0 | RESULT: PASS`.

---

## Before Stage 3

Stage 3 moves 65 files and deletes 6. It needs:

1. **a verified off-machine backup** — still outstanding;
2. **delete permission for this session**, or a person to remove the 6 files by hand (5 × `.DS_Store`, 1 × `~$220-M1.docx`) — the shell used here cannot delete on this machine;
3. answers to **Q-1** (source approval) and **Q-2** (assessment-material policy) before Stage 6, and **Q-6** (does the pilot stay on 9609, given it needs 24–36 documents acquired) before further work on this workspace.

`operations/migration/state.json` records stages 0–2 as complete and 3–8 as `not_authorised`.
