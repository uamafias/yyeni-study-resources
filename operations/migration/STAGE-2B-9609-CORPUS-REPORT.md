# Stage 2b — 9609 assessment corpus into `sources/`

**Executed:** 2026-08-31 · **Operation:** copy, non-destructive. The Question Bank originals are untouched.

## What ran

Migration rule R6 applied to all 363 files in `Question Banks/…/Business Studies (9609)/`. Target path derived from the filename, not the folder:

```text
sources/cambridge/as-a-level/9609-business/assessment/20<yy>/<series><yy>/<kind>/<filename>
```

| Result | Files |
|---|---:|
| Copied and hash-verified | **346** |
| Already present, byte-identical | 17 |
| Hash conflicts | **0** |
| Unparseable filenames | **0** |
| **Total** | **363** |

Of the 17 already present, 5 were the Stage 2 pilot copies. The other **12 were written into `sources/` by the harvester** — `9609_s23_qp_11` through `_23` and their mark schemes — at exactly the R6 paths, byte-identical to the Question Bank copies. It had clearly read the target architecture. No conflict, but worth knowing: alongside the 16 duplicates in `_quarantine/`, that is 28 files an external process placed inside the immutable zone. Repository check C2 exists for precisely this.

Report: `operations/migration/stage2b-copy-report.json`.

## Source inventory rebuilt

`work/cie-9609-as-2026-2028/inventory/source_inventory.json` — **20 sources → 378**, schema-valid against `source_inventory.schema.json`.

| | |
|---|---:|
| Sources | 378 |
| Unique source IDs | 378 / 378 |
| Full SHA-256 present | 378 / 378 |
| Duplicate content hashes | 0 |
| Paths resolving inside `sources/` | 378 / 378 |
| `reuse_constraints` populated | 378 / 378 |
| Text layer complete | 334 |
| OCR required | 1 (the scanned revision guide) |

| Authority | Count | | Status | Count |
|---|---:|---|---|---:|
| `official_assessment` | 363 | | `active` | 208 |
| `uncertain` | 13 | | `out_of_scope` | 168 |
| `official_curriculum` | 1 | | `reference_only` | 2 |
| `learner_notes` | 1 | | | |

IDs moved to a systematic scheme — `SRC-CIE9609-QP-W24-31`, `SRC-CIE9609-MS-S23-43`, `SRC-CIE9609-ER-S23`, `SRC-CIE9609-GT-W25` — so an ID is readable and stable. Safe to renumber now because no objective, claim or content unit references any source yet; after Stage 3 it would not be.

### Quality flags carried into the inventory

| Flag | Sources | Meaning for the build |
|---|---:|---|
| `a_level_paper_outside_as_only_route` | 168 | Present in `sources/`, excluded from AS scope by `status: out_of_scope` (RS-02) |
| `series_predates_2023_syllabus_revision` | 162 | 2020–2022 series. Usable, but check any question against the current syllabus before treating it as in scope |
| `march_series_india_only` | 51 | Valid AS evidence; flagged so context diversity can be measured honestly |
| `fourth_variant_june_2021` | 7 | The extra June 2021 variant the acquisition manifest failed to anticipate |

## Assessment evidence: `unavailable` → `not_started`

A real state change. The material exists; mining has not begun. `GAPS.md` records what remains: five recent examiner reports (Hub-only) and four specimen documents. The consequence is now specific rather than total — **examiner-evidenced misconceptions are available for 2020–2023 but not 2024–2025**, so pipeline Stage 12 should note that limitation instead of passing over it.

## Syllabus alignment of the corpus

Syllabus v2 states there are no significant content changes from the 2023 edition, so 2023–2025 series are aligned with the 2026–2028 scope and are recorded as `9609 2023-2025 edition (content aligned with v2 2026-2028)`. Earlier series are recorded as `9609 pre-2023 edition`. Weight the newer series when calibrating emphasis.

## Pipeline state

`INVENTORIED`. Publication still **BLOCKED** under RS-31 — correctly, and now for two reasons instead of three:

| Gate | Before | Now |
|---|---|---|
| Assessment material held | ⛔ none | ✅ 168 AS papers, 84 complete pairs, 11 examiner reports |
| Objective registry (Stage 3) | ⛔ not built | ⛔ not built |
| Assessment evidence mined (Stage 4) | ⛔ impossible | ⛔ blocked on the registry |
| Independent semantic review | ⛔ no reviewers | ⛔ no reviewers (Q-7) |

## Next: Stage 3 — the objective registry

Mining cannot start without it. Every record in `assessment_evidence.json` requires at least one objective ID (`objective_ids`, `minItems: 1`) and no objective IDs exist yet. Stage 3 decomposes syllabus topics 1.1–5.5 into atomic assessable objectives (RS-06), preserving exact syllabus wording, and builds the dependency graph and glossary (RS-08).

Inputs are all present and verified: the syllabus PDF (v2, 46 pages, clean text layer), the frozen qualification profile, and the Business subject profile with its nine objective types.

## Two housekeeping items still open

1. **28 files an external process wrote into `sources/`** — 16 duplicates in `_quarantine/2026-08-31_out-of-scope-A-Level/` (every one byte-identical to a Question Bank file, safe to delete) and the 12 s23 AS files, which are now legitimately inventoried and should stay. Deleting the quarantine folder needs a person; the shell used here cannot delete on this machine.
2. **The Question Bank copies are now redundant** for 9609 — the same 363 files exist in both trees, roughly 190 MB duplicated. That resolves itself at Stage 7 when the legacy tree is decommissioned. Until then both exist by design, which is what the staged plan intends.
