> **Current version:** [Recall queue implemented](RECALL-QUEUE-IMPLEMENTED-6117.md). Recall **373/1,637 (22.79%)** after 11 actual queue replacements and the cited card repairs; all 12 topic QA runs pass. Publication remains **hold** for independent review. Earlier totals below are historical.

# Wording and visual follow-up — 29 October 2026

All requested wording/asset fixes are implemented. All 12 topic QA runs pass without failing checks; release remains **hold**. These are author/tool checks, not independent review approval.

- 2-P03(c) now opens “Explain these observations:”. A scan of current items, activity parts, claims, content units and rendered notes found no remaining DATA tags or the targeted replacement fragments. This also removed DATA-11 from a caption and DATA-10 from the chromatography figure title.
- Thirteen binary-choice prompts now require an answer without supplied alternatives. The synthetic-polymer rubric now accepts valid alternatives to nylon, rather than silently treating it as the only answer.
- Removed the repeated “Accept scientifically equivalent wording” sentence from current learner-facing rubrics. Specific accepted answers and stated alternatives remain. This removal does not mean semantically equivalent correct answers should be rejected.
- Diamond now has an explicit four-bond wedge/dash tetrahedral projection, with continuation into the network explained. Gas curves are A/B throughout the relevant task and graph. The cooling learner image has bare vessel outlines without the controls being assessed. All three revised images were visually inspected.
- Short-card tariffs are retained deliberately: 395 one-mark, 379 two-mark, **33 three-mark** and one six-mark card. The review's “3 three-mark” count was a typo. Repeated Explain commands are retained where they correctly ask for causal reasoning; changing the command or inflating tariffs merely for variety would misrepresent the assessment demand. The 36 activities remain the longer-response practice.

Four newly open factual prompts were reclassified to FEATURE / AO A / Remember and counted as recall: 1-051, 1-066, 1-070 and 12-014. This avoids carrying their former interpretation labels into plain knowledge questions. Recall is now **395/1,637 = 24.13%**. It crosses the internal 24% trigger, although it remains below 25%; keep release paused and resolve the rule/independent classifications before publishing. Use the existing contingency to replace factual demands with genuine applications if this estimate stands. No recall savings have been claimed in advance.

The bank remains 808 cards plus 36 activities. All current production, full-demand freshness, MC/learner-asset, round-five and round-six checks pass. See planning/round6-polish-checks.json. Earlier copied-wording results remain historical; this follow-up did not rerun that source-comparison check. No new scientific data, quantities or numerical answers were introduced.

Rebuild with authoring/apply_round5_repairs.py (which now imports round6_polish.py), then render changed visuals and all notes, run all topic checks and the existing accounting checks, and finally authoring/check_round6_polish.py. Old repair stages must not be run afterwards. Nothing has been committed or published.
