> **Current re-check scope:** use [REVIEW-DELTA-2026-10-30.md](REVIEW-DELTA-2026-10-30.md) on the repaired working tree. The previous independent full-card/activity review is recorded there. The original broad brief below is historical; do not claim its remaining coverage is complete.

# Independent re-review — NSSCO Chemistry 6117

Read TEAM-PLAYBOOK.md Step 6 and the reviewer role brief. Review `work/nam-6117-nssco-2026/`, authored by Codex. Start with `FINAL-EDITORIAL-HANDOVER-6117.md`, especially “Latest reviewer follow-up — implemented”. Earlier reports contain superseded counts and findings; use the current files as evidence.

The user has instructed us to proceed after the latest repairs. This is authorization to prepare the independent review, not evidence that the reviewer has approved it or that the recall rule and AO drift have been independently accepted.

First re-verify the latest requested fixes:

1. All 132 MC questions must have scientifically correct reasons for all three wrong options in answer feedback and marking guidance. Check reasons against the actual current option letters. Check the repaired 11-P01(3) filtration distractor. There should be no generic fallback sentence.
2. Check 9-015's zinc-oxide/cost application; State commands on 10-028 and 10-045; and 11-003's evidence-sufficiency framing.
3. Confirm authoring uses of “Original” are absent from learner notes; retain legitimate references to original samples/readings. Check all 12 “Worked example:” placements against their neighbouring explanations, and confirm the two recurring fraction-advice sentences each occur once.
4. Verify both length measures: word count gives 3 uniquely longest keys and 72 ties; characters including spaces give 14 uniquely longest and 14 ties. These statistics do not establish distractor quality by themselves.
5. Verify the four activity Markdown image attachments. The previous 71-visual ledger is explicitly an author inspection, not independent approval.

Then complete the outstanding independent scope without repeating already valid work unnecessarily: read the current notes and visuals, review at least 20 cards per topic and all 19 examiner-evidenced misconception cards, inspect the rubrics and cognitive-demand decisions, and resolve any issues found. Use previous independent findings only where the current content is unchanged. Report exactly what you checked.

Current totals: 808 cards + 36 activities; 236 activity parts; 1,637 marks. AO marks A 784 / B 550 / C 303. Recall author estimate 392/1,637 = 23.95%; the next recall mark reaches the internal review trigger. Confirm the credit-level rule rather than accepting Bloom labels as proof. Do not silently approve either the AO balance or recall rule on the user's behalf.

Run the subject adapter for all 12 topics:

```sh
for topic in {1..12}; do
  .venv/bin/python work/nam-6117-nssco-2026/planning/check_resource_topic.py "$topic"
done
.venv/bin/python work/nam-6117-nssco-2026/authoring/check_round10_repairs.py
.venv/bin/python work/nam-6117-nssco-2026/authoring/audit_production.py
.venv/bin/python work/nam-6117-nssco-2026/authoring/check_full_demand_repairs.py
.venv/bin/python work/nam-6117-nssco-2026/authoring/check_copied_wording_full.py
```

These commands regenerate QA/audit artifacts; running them is part of the authorized review. Zero failures is not independent semantic approval: four checks remain `not_run`, and the subject adapter intentionally retains `hold`. Do not change the standard or suppress this hold merely to obtain a PUBLISH label. Record a separate independent verdict and any remaining operator decision.

Preserve controls: examiner-report rows are internal sources, learner answers must be reworded and numbers recomputed; no invented allocations for the five commentary-only parts; Paper 1 is 45 minutes with the 2025 discrepancy recorded; 2022/2023 papers are first proofs. Leave unrelated Biology files, harvest logs and uncommitted 2025 papers untouched. Do not publish or push as part of this review.

Deliver a concise verdict with verified fixes, any remaining defects, actual review coverage and the exact next action. Update STATUS.md honestly; do not infer human approval or independent coverage from author checks.
