# Repair round 6 — author handback, NSSCAS Mathematics 8227

**Round-7 correction to the notes claim:** “1,034 notes repaired” meant 1,034 spacing edits, not repaired mathematical prose. Missing relation signs and other extraction damage remain. Read the source page; these notes are not design evidence. The original R6 report is preserved under `analysis/history/repair-r6-report-original.md`.

**Author repair complete; focused Claude cross-vendor acceptance pending. Step 3 still waits.** Owner: Vitalis. Author: Codex with three parallel author assistants, authorised 22 November 2026. No commit or push.

| Finding | What changed | Evidence and author check |
|---|---|---|
| R5-01 | All uncapped family–part candidates decided; actual positive source reads; named response exceptions; 60-objective/138-demand map; all 58 insight comparisons and affected proposals rebuilt. | `textbook-exam-relations-r6.json`, `textbook-families.json`, `objective-problem-map.json`, `textbook-insights.md`; `check_repair_r6.py --final`. |
| R5-02 | Repaired membership/part selection and split topic-led groups; all original 5744 source-response pairs retained. 500 nearest-sibling comparisons, 147 singletons/353 ordered multi-member progressions, family-specific precision and 2385 selected-response membership reasons. | `textbook_family_repairs_r6.py`, `textbook-family-prose-parallel-r6.json`; `check_textbook_family_prose_parallel_r6.py`. Source-input hash refresh requires identical selected method, answer and operands. |
| R5-03 | All 3940 accepted assessed/component/objective/display link projections preserved. Per-objective map retains the accepted item union separately from family matching. | `history/r6-accepted-item-links-r5.json`; preservation and final R6 checks. Registry overlaps remain a step 3 decision; no retagging. |
| R5-04 | All 1758 figures classified, stale status text retired, explicit not-checked content boundary retained; known 9 source-figure errors and 11-entry correction register preserved. Native role/layout ambiguities checked separately. | `textbook-figure-repairs-r6.json`, `textbook-figure-comparisons-r6.json`; `check_textbook_figures_r6.py`. Medium+demand is representation evidence, not exact geometry or same-type equivalence. |
| R5-05 | 1034 note fields received spacing edits; 103 end-key page boundary regions inspected; 15 leaf locators corrected or confirmed through canonical, flat, nested and parent records; two source slips preserved. | Three named note inputs; `textbook-answer-page-audit-r6.json`; `check_textbook_answer_pages_r6.py`. Four transparent author-prose typo changes explicitly recorded; other note repairs preserve every non-whitespace character. |
| R5-06 | Added 2023 P2 Q4(b)←Cambridge 2020 May/June Paper 22 Q1, verified duplicate 23, weaker 2017 template lead; hidden label; Q4(a) stays 027. Pair 021 unchanged tariff removed. Screen recall 16/32, with baseline 16/31. | `nsscas-cambridge-provenance.json`, `provenance-reading-r5.json`, `provenance-full-screen-r5.json`; foundation check and preserved source/render evidence. |

## Counts before and after

| Measure | R5 | R6 |
|---|---:|---:|
| Analysis families, not recipe counts |380|500|
| Main family–part decisions |0|2675|
| Main same-type / ordered branch / rejected decisions |0 /219 summary labels /0|100 /619 /1956|
| Member exception rows |0|126|
| Unique same-type family/part pairs including named exceptions |0|183|
| Family summaries: same-type / branch / textbook-only |0 /219 /161|102 /181 /217|
| Incorrect no-exam insight sections |6|0|
| Genuine no-exam insight sections |2|2|
| Original source-response pairs retained |5744|5744|
| Accepted item-link projections retained |3940|3940|
| Figures: graphic / text callout |not separated|987 /771|
| Stale actual-value / representation-pending figures |1444 /1733|0 /0|
| Figure content explicitly not checked |not consistently explicit|1758|

Two ordered comparisons with the held 2023 P1 Q1(b) stay internal only. They are excluded from usable family anchor lists and active insight proposals; the new held-anchor negative enforces this boundary. All other holds remain binding.

The earlier 2080 candidate count was computed on 380 families. Explicit demand/decision splits produce 500 families and 2675 uncapped candidates; this is not an increase in approved recipes. 208 provisional nonordered comparisons were withdrawn as positive branch claims and retained as rejected/related teaching connections. Branch labels require a warranted easier/harder direction.

## Per-objective problem map

```json
{
  "by_objective": {
    "total": 60,
    "with_exam_parts": 59,
    "with_usable_exam_parts": 58,
    "with_same_type_textbook_practice": 41,
    "with_only_variant_or_other_practice": 19,
    "with_no_practice_anywhere": 0,
    "with_unfinished_textbook_comparison": 0
  },
  "by_demand": {
    "total": 138,
    "with_exam_parts": 127,
    "with_usable_exam_parts": 126,
    "with_same_type_textbook_practice": 69,
    "with_only_variant_or_other_practice": 68,
    "with_no_practice_anywhere": 1,
    "with_unfinished_textbook_comparison": 0
  }
}
```

Eleven demands have no NSSCAS part. Held parts stay visible and do not become usable learner anchors. Interpreting a radian has teaching support but no indexed posed practice item. A supporting drill or topic match is not full examination coverage.

## Narrow repair coverage and limits

Family prose checks: 500 families/2385 memberships. Figure taxonomy uses accepted individual census descriptions, with 23 new native layout/role page reads; no 1758 figure content audit is claimed. {'graphic': 987, 'text callout': 771}. The 512 positive figure comparisons establish an observed medium on a linked demand only; 475 graphics have no such usable recorded part. Text callouts are separated. 42 agent role repairs plus the 2 earlier YM solution-panel corrections are retained.

Notes correction (R7): 1034 unique source-note fields received spacing edits using the original 100 patches plus 200 parallel and 734 root-read proposals. The reviewer’s 634 count had no supplied detection predicate; this broader spacing-edit count is not presented as the same denominator. Original discovery proposals remain discovery; the applied, dated author inputs are authoritative. Four transparent prose typos were corrected with explicit before/after guards. These edits did not restore all missing spaces or mathematical relation signs. The note fields remain extraction-damaged/not design evidence; read the rendered page. No full note repair or new mathematical content audit is claimed.

The 103 key-page inspections cover referenced end-key page tops and column starts (32 Goldie, 71 YM). Inline worked solutions retain prior accepted locators; no new whole-body answer-page audit is claimed. Eight additional question-level locator repairs and two preserved prior repairs account for 15 leaf checks. Two later YM leads were rejected after native label verification and were not edited.

The 32 confirmed provenance pairs cover 29 NSSCAS questions. The matching screen finds 16 of 32 confirmed pairs; no missing match proves original authorship. Textbook originals remain internal and learner_display:false.

## Validation

Two complete builds in independent fresh directories: 281 commands each, 158 byte-identical outputs, matching the author checkout. 60 seeded corruption checks rejected: 38 prior, 12 core R6, 5 family-prose and 5 figure checks. These counts include separately exercised overlapping protections; they are not 60 different educational demands.

`checks/fresh-copy-verification-r6.json` and `analysis/history/rebuild-verification-r6-final-fresh-copy.json` hold the proof. 436 original source hashes and 23 baseline review-file hashes were checked; the single owner-revised prompt hash is the recorded authorised difference. The original R5 snapshot is preserved.

The declared pipeline reproduces assembly from independently copied workspaces that include retained generated records. Byte agreement does not assert that every compared file was regenerated from an empty directory. The recorded tool/input manifest enforces byte equality of the pipeline code and author records; a late dependency correction was staged identically before its dependent family/check stages and is recorded in checks/r6/proof-held-anchor-repair.json.

Passing author checks does not establish educational correctness, cross-vendor acceptance, runtime marking, learner UI, resource installation or production readiness. No PLAN, recipe contract, recipes, runtime generators, work orders, imports, assignments, commit or push were produced.

## Next step

Claude performs the focused cross-vendor check of this frozen repair. Vitalis’s ruling still holds: step 3 starts only after source-analysis acceptance. See `analysis/REVIEW-START-HERE.md`.

