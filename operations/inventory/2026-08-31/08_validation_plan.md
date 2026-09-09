# 8. Validation plan

## 8.1 What the package already validates, verified independently

The standard package's own suite was re-run in a clean environment with `jsonschema>=4.18`, `PyYAML>=6.0` and `pytest>=8.0`:

```text
$ python3 -m pytest -q
.............                                   [100%]
13 passed in 0.80s

$ python3 validate_project.py tests/fixtures/valid_project/build_manifest.json
Errors: 0 | Warnings: 0
RESULT: PASS
```

This reproduces `TEST_RESULTS.txt` from an independent run rather than taking it on trust. Two things are worth recording:

- The suite requires `jsonschema>=4.18`. The machine holding the repository has **jsonschema 3.2.0 and no pytest**, so the validator cannot currently run there. Before Stage 2, install the dependencies in `standard/v0.1.0-draft/tests/requirements.txt` (a virtual environment beside the standard folder is the cleanest option).
- The bundled fixture is correctly *not* publishable: it passes structural validation while remaining in `draft` because assessment mining and semantic review are incomplete. That is the behaviour the pilot should reproduce, and §8.4 treats it as the acceptance criterion rather than a failure.

## 8.2 Artifact already produced and validated

`data/source_inventory.cie-9609-as-2026-2028.candidate.json` — a real Stage 2 source inventory for the pilot, covering all 20 files, validated against `schemas/source_inventory.schema.json` (draft 2020-12):

```text
SCHEMA VALIDATION: PASS
20 sources
authority_category: official_curriculum 1, official_assessment 5, learner_notes 1, uncertain 13
status: active 14, reference_only 2, out_of_scope 4
ocr_required: 1
```

Every entry carries a full SHA-256 computed from the file on disk, the real page count, a measured text-extraction sample, quality flags drawn from what reading the file actually showed, and `reuse_constraints` — the field nothing in the repository currently populates. It is a candidate, not a live artifact, because its `original_filename` values are pre-migration paths; Stage 2 rewrites them.

The 13 `uncertain` authority categories are not a shortcut. They are the honest answer for unattributed third-party notes whose licence and provenance nobody has established, and they are the concrete form of open question Q-1.

## 8.3 Validation at each migration stage

| Stage | Check | Passes when |
|---|---|---|
| 0 | Baseline manifest complete | 3,235 SHA-256 entries; total bytes match `du` |
| 1 | Additive only | baseline manifest still matches exactly |
| 2 | Copy fidelity | each of 20 target hashes equals its source hash |
| 2 | Inventory validity | `source_inventory.json` validates against the schema |
| 2 | Gate behaviour | `validate_project.py` reports the *expected* blockers, not PASS (§8.4) |
| 3 | Move fidelity + reclamation | all hashes match; retained duplicate copy present; 279 MB freed |
| 4 | Per-subject conservation | count in = count out; all hashes match; mismatch log reviewed |
| 5 | Rename safety | all hashes match; no new-name collisions; `r7-unparsed.csv` signed off |
| 6 | Classification completeness | every migrated note has non-null `authority_category` and non-empty `reuse_constraints` |
| 7 | Global conservation | new-tree + quarantine + archive = 3,229 files; bytes reconcile |
| 8 | Layout checks | the three new checks in §8.5 pass |

The conservation check is the important one and it is cheap: a migration that loses a file is caught by arithmetic before anyone notices the file is gone.

## 8.4 Pilot acceptance criteria

The pilot is a success when the validator **blocks publication for the right reasons**. Specifically, after Stage 2 the build should report:

- ✅ `source_inventory.json` schema-valid, 20 sources, unique IDs, hashes present
- ✅ scope lock recorded: board Cambridge International, code 9609, syllabus version 2, exam years 2026–2028, route AS only, papers 1 and 2
- ✅ four A Level sources present in `sources/` but marked `out_of_scope`, and no AS objective citing them
- ⛔ **blocked:** assessment evidence incomplete — RS-05 unsatisfiable, no AS question paper held
- ⛔ **blocked:** no independent semantic review — RS-28/RS-29
- ⛔ **blocked:** mandatory objective coverage incomplete — the objective registry for topics 1.1–5.5 has not been built yet

A PASS at this point would mean the gates are not working. Reporting exactly these three blockers, from real data, is the outcome that justifies the standard.

## 8.5 Three repository-level checks to add

The current suite validates a *project*. It does not validate the *repository* the project lives in, and three of the risks in document 06 are only catchable at that level. Proposed as `standard/v0.1.0-draft/tests/test_repository_layout.py`:

**C1 — Every source is inventoried exactly once, with a matching hash.**
Walk `sources/**`, excluding `_quarantine/`. Every file must appear in exactly one `work/*/inventory/source_inventory.json` with a `content_hash` that matches the file on disk. Fails on: an orphan file nobody has inventoried; a file inventoried twice under different IDs; a file whose bytes changed after inventorying.

**C2 — `sources/` is immutable.**
Maintain `operations/backups/sources-register.sha256`. Any file under `sources/` whose hash differs from the register, or that has appeared without a corresponding acquisition record in `operations/acquisition/`, fails the check. This is what makes the immutability claim in document 03 §3.1 enforceable rather than aspirational.

**C3 — No active build depends on an expired syllabus.**
For every workspace in `work/` whose latest release state is not `superseded`, read the exam window from its qualification profile. Fail if the window's last year is earlier than the current year. On today's data this catches nothing; after November 2026 it catches every build resting on the 25 syllabi identified in document 02 §2.4.

Two further checks are worth considering once open question Q-1 is answered:

**C4 — Scope boundary by source class.** No claim in an AS-only build may cite a source whose `levels` exclude AS or whose `source_id` class is `ALQ`/`ALM`. The existing suite checks level boundaries on content; this extends it to source citations.

**C5 — Licence boundary.** No claim marked `publishable` may trace to a source whose `reuse_constraints` include `do_not_redistribute` or `licence_check_required`. This is the deterministic form of risk R-04, and it is the single highest-value check to add.

## 8.6 Running validation on the repository machine

```bash
cd "/Users/professor/Documents/YYeni Study Resources/standard/v0.1.0-draft"
python3 -m venv .venv && . .venv/bin/activate
pip install -r tests/requirements.txt
python3 -m pytest -q                                    # expect 13 passed
python3 validate_project.py ../../work/cie-9609-as-2026-2028/builds/build_manifest.r*.json
```

`.venv` inside `standard/` conflicts with that folder being read-only after Stage 8; put it in `operations/.venv` instead, or install the three dependencies system-wide with `pip install --user`.

## 8.7 What validation cannot tell you

Every check in this document is structural. None of them can tell you whether a note teaches Business well, whether an analysis chain has a defensible mechanism, or whether a worked application does real reasoning work rather than naming an industry. That is what `prompts/SEMANTIC_REVIEW_PROTOCOL.md` and the five reviewer perspectives are for, and it is why the pilot cannot reach `APPROVED` on deterministic checks alone — open question Q-7 (who reviews, and is one of them human) is on the critical path to the first published resource, not after it.
