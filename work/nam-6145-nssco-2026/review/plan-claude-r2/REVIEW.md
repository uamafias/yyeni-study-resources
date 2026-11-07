# Re-review of the r1 plan repairs: 6145 NSSCO Economics (`work/nam-6145-nssco-2026/`)

**Verdict: FIX_PLAN_FIRST**

Most of the repairs are real. Seven of the nine findings are resolved in the generated work orders, not just in the repair report. The totals reconcile with what you stated: 458 items, 197 objectives, A801/B630/C693, a gap of 4.161 points, 24×3 + 4×2 = 80 tasks, and 28 topics matching syllabus pages 8–16. The AO balance comes from what each task actually asks; I found no relabelling.

Two defects remain, both confirmed and both cheap to fix. Each makes a repaired finding fail in practice.

## Confirmed blockers

**B1. Both shape slices print the worked answer in the learner's prompt (F6 not resolved).**
- **Cause:** `planning/build_shape_slices.py:51` builds every prompt as `data['text'] + prompt`. That `text` already contains the results.
- **3.2 slice:** the prompt itself says "Their intersection is N$30 and 60 bags… The new intersection is N$40 and 80 bags. This is a demand shift and a movement along supply…".
  - The rubric then gives marks for exactly those points: original equilibrium, new equilibrium and the explanation.
- **5.3 slice:** the prompt states "Total cost is N$120 + N$180 = N$300… Average cost is N$300 divided by 30 = N$10", then asks the learner to calculate TC and AC.
- **Affected:**
  - items `EX-6145-3.2-DIAGRAM`, `EX-6145-3.2-INTERP`, `EX-6145-5.3-CALC` and `EX-6145-5.3-INTERP`;
  - their `context.facts`;
  - both `TEACHING-EXAMPLE.md` files.
- The numbers are right (I recomputed them) and the rubrics add up to 7, 4, 2 and 4. But these items can't test anything, and the handover tells authors to copy them.
- **Fix:**
  - Split each slice's `text` into supplied data (schedules, or FC/VC/Q/P) and worked results.
  - The prompt and `context.facts` get the data plus the instruction only. The intersections, totals and the shift-versus-movement reasoning go only into `canonical_answer` and the marking guidance.
  - Keep `TEACHING-EXAMPLE.md` as the worked version, labelled as such.
  - Make the numeric checks parse the values that actually appear in the item. At present they assert hard-coded constants.

**B2. The four "no evaluation" topics are still structurally required to evaluate (F1 repair contradicted).**
- `subject-profile.yaml:71-76` requires every `data_response` rubric to contain `both sides|opposing arguments` and `judgement|conclusion`.
- C-16 (`standard/.../yyeni_checks.py:897-904`) looks these words up by `item_type`. It will therefore fail `ITEM-6145-3.1-P02`, `-3.4-P02`, `-6.1-P02` and `-7.3-P02` (all Describe 6 / Explain 4 / Explain 4, A6/B8).
- Their `work_order.json` slots carry the same requirement. I confirmed it in 3.1 and 6.1; 3.4 and 7.3 come from the same code path.
- An author can then only add evaluation the plan says isn't there, or stuff in the keywords.
- **Fix:**
  - Give those four slots a separate schema-legal type, for example `item_type: case_analysis`.
  - Add a matching `answer_structures` entry: `context|data`, `mechanism|explanation`, `marks|allocation`.
  - Then rebuild those four work orders and `performance-specs.json`.

## Status of F1–F9

| Finding | Status | What I checked in the generated outputs |
|---|---|---|
| F1 | **Mostly resolved; see B2** | `2.3-05` members M01–M03 each have an EVAL (016–018), and 2.3-P02/P03 use `05` for the decision. 6.2 tasks include `05` and `06`. Task objectives are chosen by demand (`TASKS` in `review_fixes.py:67-96`). 3.1/3.4/6.1/7.3 have no essay plan. |
| F2 | Resolved | Each demand is now kept on the parent or its members: 1.2-02 (MECH+APP), 1.3-03 (MECH+EVAL), 4.3-01 (MECH+APP), 6.2-02 aims (MECH+APP each), 6.2-03 fiscal/monetary (MECH+APP), 8.1-01 (MECH), 2.2-07 (MECH+APP), 9.1 M01–M05 (EVAL each). |
| F3 | Resolved | 5.3 has 3 CALC and 3 INTERP. 8.2 has `002-CALC`. 7.1 has a DEF for RPI and one for inflation, plus CALC and INTERP. 1.1 has a schedule-based `005-DIAGRAM`. |
| F4 | Resolved | The DEF slots that didn't name a term are now FEATURE or MECH: 2.2/003, 4.3, 2.3-02 members, 6.1, and 3.2-04 members. |
| F5 | Resolved | Short parts are explicit (`SHORT_PARTS`) and every command/tariff pair is observed. The exemplar P01 matches its spec. |
| F6 | **Partially resolved; see B1** | The 1.1 exemplar is now sound: concrete credit points, allocations that add up (8, 20 = 6+7+7, 14 = 7+7, EVAL 2+2+1+2), a correct linear production possibility frontier (2 tomato crates per bean crate), and Namibian context. The slices fail. |
| F7 | Resolved | `jurisdiction-sources.json`, the authoring constraints and `CM-6145-NAMIBIA-PEG` record the one-to-one rand peg, which matches my understanding of the Common Monetary Area. I did not re-open the Bank of Namibia pages. |
| F8 | Resolved | `topic-ownership.json` and the contracts' `adjacent_topics` now hold meaningful ownership rules, not word matches. Two next-level-up patterns were added, with must-catch and must-allow tests in code. All work orders list 7 boundaries. |
| F9 | Resolved | Glossary now has complementary/substitute goods, the production possibility frontier, short run, long run, diminishing returns, and normal/abnormal profit. Price discrimination is gone. `definition-rulings.json` is present. |
| Minor items | Resolved | 3.3 has exactly 2 CALC. 3.5 has DEF+EVAL for perfect competition and for monopoly. 4.2 members name a comparison and a cause. 5.4-05 is decomposed. Not adding lateral/conglomerate integration is acceptable. |

## Optional suggestions (not blocking)

1. **DIAGRAM rubric wording.** The DIAGRAM structure requires the literal phrase `original equilibrium`. That forced the 1.1 exemplar's filler line ("original equilibrium is not applicable to this production frontier"). It will force the same line on `5.4/008-DIAGRAM` and `010-DIAGRAM`, which are average-cost diagrams. Allowing `original equilibrium|initial position|original curve` would fix it.
2. **Peg trigger is too broad.** `CM-6145-NAMIBIA-PEG` fires on any N$ text that also mentions an interest rate. Household-loan cards in 4.3, 2.3 and 7.1 would then need peg or "hypothetical" wording. Narrowing the second trigger to exchange-rate or policy-rate terms would avoid this.
3. **Learner objectives say "Describe…" but the slot is EVAL or MECH.** This affects the 2.3-05, 1.3-03, 6.2-02/03 and 9.1 members. Rewording them as was done for 3.5 would fix it.
4. **Same brief on all three tasks.** Each topic's three tasks share one `focus` brief, so A-only short answers read "assess…". The data-response part demands are also generic templates.
5. **1.1 exemplar P01 part 4.** The rubric credits a "supplied ranking" that the prompt never supplies.
6. **5.1 essay plan.** It evaluates objectives whose syllabus verb is only "analyse". This is defensible under AO C3 (decisions based on novel data); I'm noting it, not objecting.
7. **Marginal revenue.** The glossary entry and the MIS-027 slot in 5.3 lean on marginal revenue, which the syllabus does not list. Keep it limited to telling it apart from average revenue.
8. **Dead code.** `short_commands` and `term_object` in `task_specs` are never used.

## Limits of this review

- **Read:**
  - all of the PDF pages you specified (8–16 and 17–19);
  - the REVIEW, REPAIRS and repair-validation files, the PLAN and the HANDOVER;
  - `review_fixes.py` and `build_shape_slices.py`;
  - `plan-validation.json`, the subject profile's answer structures and slot plan, the jurisdiction sources, definition rulings and selected glossary entries;
  - the work-order slot tables for 22 of the 28 topics, the adjacency fields of 7 contracts, the 2.3/3.1/5.1 performance specs, and the full exemplar and slice items.
- **Not read:**
  - the work orders for 2.1, 4.1, 5.1, 5.2, 6.3, 7.2 and 7.4 (I only grepped them for CALC and DIAGRAM);
  - `scope-scan.json` (I relied on the assertions in the code that writes it);
  - `audit_review_fixes.py`, the exemplar `qa_report.json`, and most of the specs and glossary.
- **Not done:** I ran nothing. The AO totals were reconciled by arithmetic on the task allocations, not recomputed slot by slot. All of this was read-only; I changed no files.
