# 7. Staged migration plan

**Nothing in this plan has been executed.** Stages 0–2 are non-destructive; the first move of an existing file happens at Stage 3, and only after explicit approval.

## 7.0 Backup strategy (precondition for everything)

The folder is 4.0 GB across 3,235 files. Before any stage runs:

1. **Verify an off-machine copy exists.** This inspection could not verify one. If none exists, make one first — the fastest route is a copy of the whole `YYeni Study Resources` folder to external storage or cloud storage before Stage 1.
2. **Write a hash manifest** to `operations/backups/pre-migration-2026-08-31/manifest.sha256`: full SHA-256 for all 3,235 files, plus a count and total byte size. This is the artifact every later stage verifies against, and it is what makes rollback provable rather than hopeful. Expect 10–20 minutes of I/O.
3. **Record the manifest's own hash** in `operations/migration/state.json` so a tampered manifest is detectable.

The 13 files over 20 MB must be hashed and moved in place on the machine — they exceed the desktop bridge's per-file transfer limit and cannot be round-tripped through a cloud step.

## 7.1 The stages

### Stage 0 — Freeze and baseline (no writes to existing content)
**Do:** confirm the off-machine backup; generate the hash manifest; freeze acquisition (no new files dropped into the legacy tree while the migration runs); confirm nobody else has the folder open in a sync client that will fight the moves.
**Verify:** manifest contains 3,235 entries; total bytes match `du`.
**Rollback:** n/a.
**Approval gate:** Vitalis confirms the backup exists.

### Stage 1 — Create the target skeleton (additive only)
**Do:** create `standard/`, `shared/`, `sources/`, `work/`, `releases/`, `operations/`, `archive/` and their second-level directories. Move this inspection package to `operations/inventory/2026-08-31/`. Copy `data/raw_file_census.json` in as the baseline census. Write `shared/subject-slugs.csv` (the single subject-slug table from document 05 §5.2).
**Verify:** the 3,235-file manifest still matches — Stage 1 adds directories and touches no existing file.
**Rollback:** delete the new empty directories.
**Approval gate:** none needed; nothing existing is affected.

### Stage 2 — Pilot copy-forward (additive only, 20 files)
**Do:** **copy** (not move) the 20 pilot files per document 04 §4.3 into `sources/cambridge/as-a-level/9609-business/`. Create `work/cie-9609-as-2026-2028/` with the frozen qualification profile and `inventory/source_inventory.json` (the candidate in `data/` becomes the live artifact once paths are rewritten to the new locations). Create `assessment-evidence/assessment_evidence.json` with an explicit gaps list per document 04 §4.4.
**Verify:** each copy's SHA-256 matches the original; `source_inventory.json` validates against the schema; `validate_project.py` runs against a draft build manifest and reports the expected blockers (missing assessment evidence, no semantic review) rather than passing.
**Rollback:** delete `sources/cambridge/as-a-level/9609-business/` and `work/cie-9609-as-2026-2028/`. The legacy tree is untouched, so rollback is free.
**Approval gate:** the team reviews the pilot layout and the source inventory before anything moves. **This is the stage that proves the architecture on real files at zero risk, and it is where I recommend stopping for review.**

### Stage 3 — Quarantine, archive and duplicates (first moves — 65 files)
**Do:** move the 16 corrupt/encrypted/unreadable files to `sources/_quarantine/2026-08-31/` with `quarantine.json`; move 29 Botswana BGCSE syllabi to `archive/out-of-scope/botswana-bgcse/`; move the 20 non-canonical duplicate copies to `archive/duplicates/2026-08-31/` with `provenance.json`. Delete 5 `.DS_Store` and 1 Word lock file.
**Verify:** every moved file's hash matches the pre-move manifest; for each duplicate archived, the retained copy exists and its hash matches; the 279 MB reclamation is measurable.
**Rollback:** `operations/migration/rollback-stage3.json` records source→target for every move; reversing it restores the exact prior state.
**Approval gate:** yes — first destructive-ish stage.

### Stage 4 — Cambridge sources (1,898 files: 1,848 assessment + 50 syllabi)
**Do:** run R6 fully automatically, one subject at a time, largest first. Run R3 semi-automatically after `operations/migration/r3-syllabus-code-map.csv` is completed by a human (12–18 rows).
**Verify:** per subject, count in = count out; every hash matches; `r6-path-filename-mismatch.log` reviewed (expect the three known cases from document 02 §2.1 D); no target collision unresolved.
**Rollback:** per-subject rollback manifests, so a single subject can be reverted without touching the rest.
**Approval gate:** after the first subject (recommend Business 9609, then Accounting 9706 as the volume test).

### Stage 5 — Namibian and GCSE sources (648 files)
**Do:** R7 (556 assessment, with rename), R8 (13 examiner reports, deduplicated), R4 (76 syllabi), R5 (3 GCSE, of which 1 goes to quarantine).
**Verify:** every renamed file's hash matches; `r7-unparsed.csv` is empty or explicitly signed off; the JSC listening/talking code table is applied; no two files collide on a new name.
**Rollback:** per-route rollback manifests. **Rename-heavy stage — the rollback manifest is the only way back, so verify it is written before the first move.**
**Approval gate:** yes, on the rename convention as applied to a sample of 20 files.

### Stage 6 — Revision notes → `supporting/` (615 files)
**Do:** R9, one level at a time (AS, IGCSE, NSSCAS, NSSCO, JSC, SP). For each file assign `authority_category` and `reuse_constraints` — this is where open question Q-1 must already be answered. Optionally run OCR into `.ocr.txt` sidecars (open question Q-5).
**Verify:** count in = count out; hashes match; every file has a non-null `authority_category`; no file lands with `reuse_constraints: []`.
**Rollback:** per-level rollback manifests.
**Approval gate:** yes — this stage cannot start before Q-1 and Q-2 are decided.

### Stage 7 — Decommission the legacy tree
**Do:** confirm `Question Banks/`, `Revision Notes/` and `Syllabi/` are empty of files; remove them and the 148 empty directories; move the standard package to `standard/v0.1.0-draft/` (R1).
**Verify:** file count under the new tree plus quarantine plus archive equals 3,229 (3,235 minus the 6 deletions from Stage 3); total bytes reconcile against the baseline minus 282 MB of archived duplicates.
**Rollback:** the composite of all prior rollback manifests. Past this point rollback means restoring from the Stage 0 backup, so **do not run Stage 7 until Stages 4–6 have been verified and a working build exists.**
**Approval gate:** yes, explicitly.

### Stage 8 — Freeze and instrument
**Do:** set `sources/`, `standard/` and `archive/` read-only (open question Q-9); commit the repository-layout checks from document 08 as `standard/v0.1.0-draft/tests/test_repository_layout.py`; regenerate the full census into `operations/inventory/<date>/` and diff against the 2026-08-31 baseline; write `operations/acquisition/` from the quarantine list and the assessment gaps.
**Verify:** the layout checks pass; the census diff accounts for every difference by migration rule.
**Approval gate:** none; this is the closing stage.

## 7.2 Effort and sequencing

| Stage | Files touched | Nature | Can it be automated? |
|---|---:|---|---|
| 0 | 0 (read 3,235) | baseline | yes |
| 1 | 0 | additive | yes |
| 2 | 20 copied | additive | yes |
| 3 | 65 moved, 6 deleted | moves | yes |
| 4 | 1,898 | moves + rename | R6 fully; R3 needs 12–18 human rows |
| 5 | 648 | moves + rename | mostly; R7 needs a small code table |
| 6 | 615 | moves + classification | **no** — needs a per-file authority/licence decision |
| 7 | cleanup | deletion of empty dirs | yes |
| 8 | 0 | instrumentation | yes |

Stage 6 is the only stage whose cost is dominated by human judgement rather than I/O. It is also the stage that carries the copyright exposure, which is why it is sequenced last among the content stages.

## 7.3 Guardrails that apply to every stage

1. **Hash before, hash after.** No move is complete until the target hash matches the recorded source hash.
2. **Move, never copy-then-delete** within the same volume — a partial copy followed by a delete is the one failure mode that loses content.
3. **One rollback manifest per stage, written before the first move**, recording source, target, hash, size and timestamp.
4. **Never delete a file the plan does not name.** The only deletions in the entire plan are 5 `.DS_Store`, 1 Word lock file, and 148 empty directories.
5. **Idempotent runs.** Re-running a stage after a partial failure must skip already-correct files rather than duplicating or failing.
6. **Dry-run first.** Every rule runs in `--dry-run` and its output is reviewed before it runs for real. Dry-run output goes to `operations/migration/dryrun-<rule>-<timestamp>.csv`.
7. **The legacy tree stays until Stage 7.** Between Stages 3 and 7, both trees exist; consumers point at the new one, and the old one is the fallback.

## 7.4 Recommended immediate next step

Approve Stages 0–2 only. They are non-destructive, they take under an hour of machine time, and they answer the question that matters: does the proposed architecture actually work on the pilot's real files, and does the validator behave as the standard says it should? Stages 3–8 should not be scheduled until open questions Q-1, Q-2 and Q-6 are answered.
