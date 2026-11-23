# Repair round 7: fix the gap list and the rejection labels (NSSCAS Mathematics 8227)

You are Codex, the author of the 8227 Workbench analysis. Your role is **AUTHOR**; the workspace is `work/nam-8227-nsscas-2026/`. Vitalis's decisions are final.

## Where round 6 stands

Claude's focused check (2026-11-23) **accepted** most of round 6:
- every candidate decided;
- positive relations, which are reliable;
- the named round-5 fixes;
- the insight sections' exam-part lists;
- the per-objective map structure;
- figure statuses and the registered errors;
- provenance 037 and recall;
- the rebuild.

It **returned** a short list:
- the gap list (R6-01);
- the rejection labels (R6-02);
- the 61 families with no assessed demand (R6-04);
- named record fixes (R6-05 to R6-07).

Step 3 still waits for this round and Claude's short check. This round does **not** create the PLAN, recipes, generators or work orders.

## Read first

1. `workbench/review/opus-5-5-repair-r6/report.md`, then `findings.md`.
2. In the same folder:
   - `blind-pair-disagreements.json`: 28 pairs, with the reviewer agents' reasons, best members and parts;
   - `no-textbook-relation-parts-r6.json`: the 22 syllabus parts and 9 prior/ability parts with no relation.

Before changing anything, copy `analysis/analysis-snapshot.json` (sha256 `13dcf9f7b0377ff760324e4f0847dd17c7c3be4f21991c547124bb9e5e818464`) to `analysis/history/analysis-snapshot-r6.json`.

## A. R6-01: re-check every exam part recorded as having no textbook practice (main job)

For each of the 22 syllabus parts in `no-textbook-relation-parts-r6.json`:

1. **Search the books directly.** Use the chapter and exercise index, `textbook-exercise-index.json` and the rendered pages, not only demand-ID candidates. Find the closest textbook items.
2. **Record a relation:** same type, or structural branch (with the differing decision and a direction), read on both rendered pages with the date. Use the existing family where it fits; otherwise add a member-level relation.
3. **If there is genuinely no counterpart,** record a search note with:
   - the chapters, exercises and pages searched;
   - the closest items rejected, each with its reason.

**Start with the confirmed cases:**
- **2024 P2 Q4(a)** "Differentiate (3e²ˣ − 7)⁵": YM C7 Try Now 12 Q2(a) and Q3(a) (PDF 334), and Goldie 4B Q2(viii) (PDF 108).
- **2023 P2 Q3(b)(ii)** "exact value of cosec(2π/3) + cot(2π/3)": test reciprocal-exact-values (e.g. Goldie 3A Q2) and special-angle-exact-values. It is a forward exact evaluation, not the integral in (b)(iii).

Treat these as likely false gaps until read: 2022 P1 Q13, 2022 P1 Q14(a), 2023 P2 Q4(b) and (c), 2025 P1 Q10(b), 2025 P2 Q6(a) and (b).

**Also:**
- Correct the eight 2023 P2 Q3(b)(ii) rejections. Four describe part (b)(iii).
- Rewrite the "Exact special angles and connected geometry" section and its step-3 proposal.

## B. R6-02: rejections

1. **Nonordered connections (202).** A branch may differ in both directions.
   - Allow `difficulty_relative_to_exam: "mixed"`.
   - Convert each `nonordered_connection` rejection to a structural branch with direction "mixed", keeping its differing-decision text. Do this where the pair has one or two named differing decisions or responses; otherwise leave it rejected with a specific reason.
   - Pairs already read on pages need no new reading; otherwise read them.
2. **The 28 disputed pairs** in `blind-pair-disagreements.json`.
   - Read each pair again on both pages and re-decide it.
   - Record per pair whether you agree with the reviewer agent, and why.
   - PAIR-024 is verified by Claude as same type: YM C7 Try Now 12 Q2(b) against 2024 P2 Q4(b).
3. **The same-type test.** A change in values, coefficients, context or the kind of inner function, where the learner's decisions and response are the same, is **same type**, not a branch. Apply this rule to the pairs you re-decide in this round; a full relabel is not required (R6-03).
4. **Batch-worded rejection reasons** ("the target instead…", "none of these targets"; 389 records).
   - Replace each with a part-specific reason that names the part's actual task.
   - Re-decide any that turn out to describe a different part.
5. **Labels.**
   - In `objective-problem-map` and `textbook-insights.md`, describe rejected families neutrally as "relation not established" rather than as different learner decisions.
   - Remove the stale "no verified relation recorded yet" wording.

## C. R6-04: families with no assessed demand

For each of the 61 families with empty `assessed_demand_ids` whose members carry examined item-level assessed demands (41 members), do one of:
- set the family's assessed demands and decide its candidates as in round 6; or
- record, per family, why its members do not assess those demands at family level.

Also fix implicit-given-point-gradient: all its members require D01, "Differentiate implicit curve".

## D. R6-05 to R6-07: named record fixes

1. **Membership misfits.** Make each membership part-level or move the member to a family it fits:
   - modulus-quartic-root-count: correct its demand claim (YM Revision 8 Q3 is "show two roots by sketching");
   - identity-common-expression: YM Try Now 35(e) and 37(b);
   - parametric-point-plot-support: Goldie Worked illustration 1;
   - log-derivative-division-integral-chain: Goldie 5A Q8(i);
   - elementary-exponential-primitives: Goldie 9B Q1(iii) carries part (iv)'s reason, and its progression mentions a square no member has;
   - elementary-reciprocal-definite-logform: Goldie Examples 5.2–5.4 and 8H Q2(ii);
   - vector-division-position: YM Revision 5 Q3 and Goldie 10F Q11(i).

   Also check whether quadratic-exponential-recovery and exponential-positive-substitution are one family.
2. **Family prose. Do not rewrite all 500.**
   - Remove the doubled "Compared with X:" prefix (428 families).
   - Fix the contradictory precision text in photo-density-estimation-support and trig-derivative-hence-integrals.
   - Add a top-level `limits` note: `distinction_basis` and `units_and_precision` are author descriptors that contain template sentences; they are not design evidence.
3. **Transcription and source issues:**
   - YM Try Now 17 Q1(b) (PDF 543) prints tan²x, not tan²2x: correct the record and its result (√3/3 − π/6), or register a source discrepancy if you can show the print is a defect;
   - register YM Example 12(c) (PDF 174), where the question says y = 3cos x + 2 but the solution sketches 3cos 2x − 1;
   - check YM Example 12 (PDF 122): domain x ≠ 3 against −3, and the range of √(x − 5);
   - complete Goldie 3D Q9(ii) and (iv) (smallest positive θ);
   - completed-square-interpretation selected results must be completed forms;
   - repair the truncated selected-result keys in trig-formula-restricted-sketch.
4. **Answer pages:**
   - YM C4 Try Now 50 Q1(b) → PDF 612;
   - YM C13 Try Now 4 Q3(a) → PDF 653 (start);
   - correct the item names in the page observations for YM 623, YM 634, Goldie 352 and Goldie 354.
5. **Figures:**
   - Goldie C10 Teaching-figure 22 → teaching;
   - YM C4 Teaching-figure 13 → given;
   - choose one rule for long divisions and apply it to both books;
   - count vector diagrams on squared paper as diagrams for medium comparison;
   - count parts where the learner reads back their own sketch.
6. **Insights:**
   - transform-equations branch for 2021 P1 Q5(a): a quadratic in cos θ, not sec θ;
   - principal inverse: don't treat the held 2023 P1 Q9 as design evidence, and cite the Cambridge comparators the map links to.
7. **Notes (R6-06).** Do not attempt a full repair.
   - Mark every note whose text lost spaces or "=" signs with `"notes_text_status": "extraction-damaged; read the page"`.
   - Correct the round-6 report's "1,034 notes repaired" statement.
8. **Hygiene:**
   - update the stale `status` strings (`textbook-exam-relations-r6.json`, the note-spacing inputs);
   - rebuild the objective map after the final inventory;
   - restore spaces in the provenance 037 text fields.

## Deliverables

- **The updated analysis files and their tools,** and a regenerated `analysis-snapshot.json`.
- **`workbench/checks/repair-r7-report.md`, containing:**
  - a table for the 22 gap parts: the relation found, or the search note;
  - a table for the 28 disputed pairs: the new decision, whether you agree with the reviewer, and why;
  - counts before and after:
    - relations by kind, including "mixed" branches;
    - exam parts with no textbook relation;
    - families with empty assessed demands that are compared or justified;
    - demands with same-type textbook practice in the map.
- **STATUS.md and HANDOVER.md** updated. The next step is Claude's short check, then step 3.

## Checks before handing back

- **Rebuild.** The deterministic double rebuild passes in a fresh copy, and all seeded negatives still fail.
- **New negative fixtures:**
  - an exam part with no textbook relation and no search note;
  - a `nonordered_connection` stored as a rejection without a specific reason;
  - a family with empty assessed demands whose members have examined demands and no recorded reason;
  - a doubled "Compared with" prefix.

## Constraints

- Do not commit or push; Vitalis commits.
- **Do not modify:**
  - any review folder;
  - source PDFs;
  - `standard/`;
  - other subjects;
  - app code;
  - pinned checkouts.
- Acquire anything only with the YYeni Web Harvester; write no new scraping scripts.
- Textbook originals stay internal (`learner_display: false`).
- No PLAN, recipes, generators, work orders, imports or learner assignment.
- No relabelling of demand links (R5-03). You may add a family candidate where a search in A shows a counterpart.
