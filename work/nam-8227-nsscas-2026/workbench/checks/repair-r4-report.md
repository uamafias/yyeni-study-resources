# Repair round 4 checkpoint — NSSCAS Mathematics 8227

**In progress. Step 2 is not complete; no recipe planning is authorised by this record.** Author: Codex, commissioned by Vitalis. The marking repair is ready for a focused second-eye check. The textbook page and heading passes are recorded; final population/figure completeness, value-level qualifier decisions, full answer accuracy and independent classification remain open. No textbook sampling stop rule has been earned. This is not an independent acceptance, owner acceptance, website test or publication.

Preserved round 3 snapshot: `analysis/history/analysis-snapshot-r3.json`, SHA256 `208a33a2027295d09c84f70423b370aa27e5626df289114842181383ce64389d`. Review files and source PDFs remain immutable. No commit or push.

| Finding | Current disposition / change | Evidence / executable check |
|---|---|---|
| R3-01 | Author transcription complete: 119 question records, 821 rows; every row second-read against its render. | `analysis/marking-conventions.json`, `award-second-read-r4.json`; `tools/check_repair_r4.py`,250 part reconciliations. |
| R3-02 | Named 13 marking-changing and 7 cosmetic corrections applied; degree-mode rejection is in Q7, not Q6. | `tools/award_rows_r4.txt`; frozen row fingerprints and page-specific second-read notes. |
| R3-03 |95 consolidated rules, all 191 native context hits disposed,73 visual award-condition hits retained; conflict04/05 completed,073 clarified. | `analysis/convention-context-scan-r4.json`; `tools/scan_convention_context_r4.py`; direct requirement links separated from related part rows. |
| R3-04 |015/019 demoted; 009 also demoted; N1–N10 confirmed on both page images; external-division lead remains structural, not proven source. | `analysis/nsscas-cambridge-provenance.json`, `provenance-reading-r4.json`;26 confirmed pairs,4 structural comparisons;476 rank 1–4 lead dispositions. |
| R3-05 |Named scope, label and key defects corrected in individually addressed items. Exact-key evidence and selected independent recomputations recorded; further defects found during continuing reading. | `tools/textbook_source_cautions.py`, `textbook_repairs_r4.py`; `checks/textbook-recomputations-r4.json`; viewed sheets in `checks/r4/`. |
| R3-06 |Manifest evidence paths are repo-relative and constrained to this subject workspace. Fresh isolated copy passed two builds and all 7 negative fixtures. | `tools/analysis_sources.py:evidence_path`; `checks/fresh-copy-verification-r4.json`. The fresh-copy check must match the current output count. |
| R3-07 |Deferred to step 3 as explicitly required by repair prompt. Containment checks remain structural; branch specs must name must-read givens. | Existing 39 crop checks retained; no claim to detect labels wholly outside crop or raster omissions. |
| R3-08 |**Partial, continuing.** Range seeds expanded to individual rows; named mapping omissions/over-mappings corrected; duplicates linked without double-counting; QUAL01 issue explicitly handled; qualifier screening exposed. Fresh seed prepared. All 929 discovery headings are disposed and all 759target source pages read. Headingless tasks and late parts found during the sweep are individually catalogued. Final independent completeness, value-level qualifier decisions and full answer accuracy remain open. | `analysis/textbook-inventory.json`, `textbook-reading-r3.json`, `textbook-review-sample.json`; no blanket answer-verification claim. |

| Measure | Round3 | Current |
|---|---:|---:|
| Mathematics report pages read |86|87|
| Questions with transcribed award tables |24|119|
| Criterion rows including exclusive alternatives |196|821(818official,3derived completions)|
| Part budgets reconciled |24-question subset|250|
| Rows with recorded author second read |not recorded|821|
| Convention rules |75(repeated general rules)|95(deduplicated plus additions)|
| Confirmed provenance pair records |19|26|
| Distinct NSSCAS questions with a confirmed specific source |18|25|
| Structural comparisons without attribution |not separated|4|
| Catalogued textbook items |1003|1933|
| Unclassified textbook heading leads |624|0|
| Target textbook source pages with inspected render evidence |not reconciled|759/759|
| Recorded item answer-location checks |not separately tallied|1913|
| Independent author mathematical recomputations |not separately tallied|49|
| Native report context hits awaiting disposition |not registered|0|

## Source gaps and limits

The reports contain a table for every question, but two individual parts have no official breakdown:2023 P1 Q5(a), 2 marks, and2024 P1 Q13(a), 3 marks(the report duplicates the(b)table). The2025 P2 Q3 third-angle alternative is missing its final1-mark row. These are3 **derived completion rows**, not official marking instructions. They reconcile paper budgets without disguising missing content. Step 3 must author and review the missing criteria; a tariff placeholder is not a runtime rubric.

The full transcribed register supplements the old native-text excerpt scan, which found only24 question excerpts. New part→criterion links name the full register. Coverage of syllabus demands still comes from part→demand links, never families.

General report prose does not silently erase explicit B,SC or F.T. awards. The register preserves additional disagreements about unlabelled graphs and final precision. General-rule applicability, direct award wording and contextual related rows are separately recorded.

Provenance is an inference from documents, not proof of examiner authorship history. The2021P1Q6lead shares a template but changes all vectors, the AP multiplier and subsequent demands; it does not establish the origin of the external-division wording. All draft derived-from references stay hidden. Duplicate variants are explicitly labelled leads, not independent breadth. Unpromoted ranked leads remain unresolved, not rejected or proven original.

Textbook counts describe source items, not distinct problem types or accepted design evidence. The2 textbook-support gaps remain visible: distinguishing identity from equation and the defining meaning of a radian. Weak Goldie leads were read and recorded without silently closing them. There are1,913 published answer-page or explicit no-entry location checks and 20 investigations with author-derived answer notes and no separate printed key located. The 49 independent recomputation checks cover representative results,not every item or graph feature. Named answer entries are distinguished from no standalone key entries. Even exact answer locations do not certify all mathematical values or branches. QUAL01–11screening is visible per item, with unresolved checks labelled; merely listing a qualifier is not acceptance. No item is learner-displayable.

## Checkpoint and continuation

Run `python3 work/nam-8227-nsscas-2026/workbench/tools/run_repair_checks.py`, then `verify_relocated_r4.py`. The last completed checkpoint compared 113 assembled outputs byte for byte and rejected7fixtures, including summed alternatives, missing award coverage and absolute evidence paths. The current isolated copy also passed two rebuilds with the same output count and all 7fixtures,without path edits;435source hashes were checked. Further content changes require repeating these checks. The checks establish structural behaviour, not educational acceptance.

Use `textbook-page-audit-r4.json/.md` for the759-page reading trail and source cautions. There are0 unclassified discovered headings, but that is not an exhaustive verified census: TryNow28 Q2/Q3 and Example/TryNow16 were found by page/answer comparison after heading reconciliation. Complete final connected-part/teaching-figure completeness, value-level qualifiers and answer accuracy before claiming full step 2 completion. The new sample seed is `8227-r4-textbook-review-v2`; it is prepared for independent blind classification, not already reviewed. Vitalis has been asked whether the marking checkpoint should receive Claude's check while this work continues. No planning shortcut is assumed from silence.

The next review is Claude's focused check of the actual completed changes. Step 3(recipe contract and pilot PLAN) stays out of this round. No app, runtime generator, import, assignment, deployment, source acquisition, commit or push occurred.
