**Verdict: READY_FOR_PLAN_APPROVAL**

Both blockers are fixed in the current generated files, not just in the repair notes. I found no remaining defect that should block approval. I first checked the syllabus assessment pages (PDF pages 17–19, printed 13–15): AOs A/B/C, Paper 1 at 50/16/34 and Paper 2 at 28/35/37, each paper 80 marks. Nothing I read contradicts them.

**B1 — worked answers no longer appear in the slice prompts: closed**
- `build_shape_slices.py:54` now builds each prompt from `supplied_data` plus the instruction. `context.facts` carries `supplied_data` only. The worked text (`text`) goes only into `TEACHING-EXAMPLE.md`, which is labelled "Worked teaching explanation… Read after attempting the separate learner items."
- The four saved items contain only inputs and instructions in the prompt and facts. The intersections, totals and the shift-versus-movement reasoning appear only in `canonical_answer` and `marking_guidance`.
- **Numbers, recomputed by me:**
  - 3.2: supply equals the original demand only at N$30 / 60 bags, and equals the new demand only at N$40 / 80 bags.
  - 5.3: total cost is N$300, average cost N$10 per bag, revenue N$420, profit N$120.
  - The rubrics add up to 7, 4, 2 and 4.
- **The controls are real.** Lines 70–92 read the saved item files back, parse the values out of the actual prompts, find the unique equilibria and check the results against the answers. They also assert that no leakage phrase or result value (N$300, N$10 per bag, "TC =", "their intersection is") appears in a prompt. The input values that are only supplied (120, 180, 30, the schedules) are correctly left alone.

**B2 — the four descriptive topics no longer have to evaluate: closed**
- `subject-profile.yaml:83-86` defines `case_analysis` as context|data, mechanism|explanation and marks|allocation only. The schema allows it (`learning_items.schema.json:71`).
- C-16 looks up the required parts by `subtype` or, failing that, `item_type`, so it will apply this structure to those items. C-17 only checks items that have a `subtype`, so it does not touch them.
- **Slot counts:** exactly four `case_analysis` slots, in the work orders and `performance-specs.json` alike: 3.1, 3.4, 6.1 and 7.3 P02. Each is Describe 6 / Explain 4 / Explain 4 (A6/B8, Analyse), and none asks for both sides or a judgement.
- The other 24 `data_response` slots keep both sides and a judgement. In 2.3 P02, for example, the last part is "Discuss 7" with "weigh opposing effects…". In total that is 28 short-answer + 28 P02 + 24 essay-plan tasks = 80.
- PLAN §4 (line 53) documents the change.

**Optional suggestions — all addressed**
- **DIAGRAM structure:** the alternatives are in place (`subject-profile.yaml:56`). The 1.1 rubric for the production possibility frontier now reads "Initial position / original curve" with no equilibrium filler, and its (2,8)→(4,4) step is consistent with 2 tomato crates per bean crate.
- **Peg trigger:** now limited to exchange rate, policy/repo rate, monetary policy and appreciation/depreciation. Ordinary interest-rate text no longer sets it off.
- **Learner objectives:** the members of 2.3-05 and 9.1 now say "Discuss and evaluate…", and the members of 6.2-02 and 6.2-03 say "Explain… reason and consequence".
- **Task briefs:** short-answer, case-analysis and evaluative briefs now differ.
- **1.1 exemplar P01:** the prompt now states that sport is the next-best activity.
- **Marginal revenue:** the HANDOVER (line 54) limits it.
- **Dead code:** `short_commands` and `term_object` are gone.

**Residual, non-blocking**
1. Evaluative `data_response` briefs (for example 2.3 P02) still begin "Structured case analysis:", which overlaps with the new `case_analysis` type name. It's cosmetic, but it could blur the difference for authors.
2. The 5.3 slice supplies a selling price that neither item uses. It only feeds the teaching explanation, so it's harmless as a distractor.
3. The 3.2 leakage control matches phrases rather than meaning. That's fine for an exemplar.

**Limitations**
- I ran nothing. The rebuild, mining verification, schema validation, the scarcity exemplar's check results and the totals (458 items, 197 objectives, A801/B630/C693, 4.161-point gap, Bloom rollups) were not re-run or recomputed by me. I only confirmed that the totals agree with PLAN §4.
- The slices are still thin, separately validated examples. They are not certified topics, and no diagram renderer has certified them.
- Human plan approval, the commit and the step-6 review of the authored subject are still pending. I changed no files.
