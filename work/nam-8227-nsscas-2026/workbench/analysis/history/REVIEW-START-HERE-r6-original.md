# Review entry — NSSCAS Mathematics 8227, repair round 6

Owner: Vitalis. Author: Codex, with parallel author assistance explicitly requested by the owner on 22 November 2026. This is source-analysis repair, not step 3 or independent acceptance.

Read the revised `review/opus-5-5-repair-r5/REPAIR-PROMPT.md` in full. It supersedes the original member-level comparison scope. Previous R5 population, mapping and answer acceptance remain bounded by the reviewer’s recorded limitations. The R5 completion declaration and R5 proof files are historical; use the R6 report and proof for the current repair.

1. `checks/repair-r6-report.md` gives the current disposition of R5-01 through R5-06 and all remaining limits.
2. `analysis/objective-problem-map.json` and `.md` are generated from direct exam-part links and the authored family relations. They preserve all 60 objectives and 138 demands.
3. `analysis/textbook-families.json`, `analysis/textbook-insights.md` and `tools/textbook-exam-relations-r6.json` contain family decisions, named response exceptions and actual rendered-read evidence. The uncapped comparison has 2,675 family–part decisions; source-response pairs are preserved. Family counts are not recipe counts.
4. `analysis/textbook-figure-comparisons-r6.json` makes a narrow representation-medium comparison. It does not assert exact geometry or same-type questions from a medium/demand match. Figure content is explicitly not checked; originals stay internal.
5. `analysis/textbook-answer-page-audit-r6.json` records the rendered key-page boundary audit. `tools/check_textbook_answer_pages_r6.py` checks propagation into flat, nested and parent key locators.
6. The spacing inputs are `tools/textbook-note-spacing-r6.json`, `tools/textbook-note-spacing-parallel-r6.json` and `tools/textbook-note-spacing-root-r6.json`. Named transparent author-prose typo corrections are recorded separately from whitespace-only repairs.
7. Provenance pair 037 links 2023 P2 Q4(b) only to Cambridge May/June 2020 Paper 22 Q1, with duplicate23 evidence and a hidden label. The screen’s measured recall is 16/32; a missed candidate is not evidence of originality.

## Required proof and review boundary

A completed handback requires `checks/fresh-copy-verification-r6.json` to report pass, together with `analysis/history/rebuild-verification-r6-final-fresh-copy.json`. Two independent fresh-directory builds must agree and match the author checkout, with all38prior negatives and at least11R6 negatives rejected. Until that evidence exists, the round remains in progress regardless of any author completion wording elsewhere.

Check the current frozen state with:

```bash
python3 work/nam-8227-nsscas-2026/workbench/tools/freeze_analysis_r6.py --check
```

Claude should independently check the repaired family comparisons, nearest-sibling decisions, source-specific membership reasons, figure taxonomy/comparison limits, notes, key boundaries and new provenance. Same-model parallel author checks are not cross-vendor acceptance. No author-selected review sample is prescribed.

Step 3 remains deferred until the focused cross-vendor check accepts this repair. No PLAN, recipe contract, recipes, runtime generators, work orders, publication, imports, assignments, commit or push are included.
