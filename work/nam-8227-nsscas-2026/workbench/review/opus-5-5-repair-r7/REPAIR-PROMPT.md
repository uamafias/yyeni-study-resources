# Round 7 close-out: five small corrections before step 3 (NSSCAS Mathematics 8227)

You are Codex, the AUTHOR of the 8227 Workbench analysis. The workspace is `work/nam-8227-nsscas-2026/`. Vitalis's decisions are final.

## Where round 7 stands

Claude's short check (2026-11-23) **accepts round 7**:
- the gap search;
- the 28 re-decisions;
- the mixed-branch policy;
- the named fixes;
- the per-objective map.

Five small corrections remain. Make them as this close-out. They need no separate Claude round: Claude confirms them at the start of the step-3 review. **This close-out does not create the PLAN, recipes, generators or work orders.**

Read first: `workbench/review/opus-5-5-repair-r7/report.md`, then `findings.md`. Evidence for the corrections is in the same folder:
- `kept-rejections-r7.json`;
- `gap-search-check-r7.json`;
- `empty-family-check-r7.json`;
- `blind-sample-r7.json`.

Before changing anything, copy `analysis/analysis-snapshot.json` (sha256 `abfc33996b4b91df662939149b5821042b8ba3ad1dbe9edabeca8a0e89f567e8`) to `analysis/history/analysis-snapshot-r7.json`.

## 1. R7-01: re-decide the 12 kept nonordered rejections at sub-part level

For each pair in `kept-rejections-r7.json`:
1. Read every member of the family, not only the worked example.
2. Find the best member and sub-part. The reviewer's best member is a lead, not a decision.
3. Decide on both rendered pages, with the date: same type, structural branch with a direction (easier, harder or mixed), or rejected.

A rejection must say why the best member's matching sub-part fails. "The whole selected source response differs" is not a reason when a sub-part matches.

Example: YM C7 Try Now 39 Q1(c) (PDF 366), "find s in terms of t, then how deep was the shaft after 4 s", against 2021 P1 Q4(b).

## 2. R7-02: gap records

- **2023 P2 Q4(c).**
  - Search once more for an equation in log_a x and log_x a, or a change-of-base equation that leads to a square, e.g. (log₅ y)² = 4.
  - If none is found, record a bounded no-match search, naming Goldie 2B Q10(ii) as the closest rejected item and saying why: the solving step, keeping both roots, and the back-substitution direction all differ.
- **2024 P1 Q9(c).** Make the search note agree with the decision. The note currently calls the selected YM Example 16(f) "closest rejected".
- **2023 P2 Q2.** Add to the search note the nearest related practice:
  - graph-to-quadratic reconstruction, YM Examples 26–27 and Try Now 27 (PDF 35–37);
  - Goldie 1B Q7(i).

  These are related branches, not modulus counterparts. Keep the no-match.

Update the gap counts and the map.

## 3. R7-03: two empty-demand families and one assigned family

- **trig-point-value-parameter-support.** Assign M1:T6:O03:D01 (exact special-angle values), which all three members use, and decide its candidates.
- **exponential-scale-context-support.** Split the family, or record member-level relations:
  - Goldie C2 Prompt 1 and Exercise 2A Q6 (doubling, geometric progression), with 2024 P1 Q4(a)/(b) as candidates;
  - Exercise 2B Q13 and Q14(iii) (solving an exponential/log model), with 2021 P2 Q4(b) as a candidate.

  Decide each.
- **explicit-second-derivative-zero.** Add the product-rule demand at family level, and decide 2022 P2 Q5(a) (y = 6x e^(x/3)).
- **Small fixes:**
  - correct "product rule" to "quotient rule" in the differentiation-conceptual-proof-support reason;
  - choose one rule for unposed textbook prompts, as directly assessed or as support, and apply it to both books.

## 4. R7-04: rewritten rejection reasons

**Do not rewrite all 403 again.** In `batch_rejection_rewrites` and the ledger:
- Add `rejection_reason_status: "template: exam text + source summary; not a part-specific comparison"` to each templated record.
- Where the R6 reason had a part-specific closing sentence, restore it, dropping only the batch phrase ("The target instead…", "none of these targets").
- Fix the 11 reasons cut off mid-sentence.
- In `checks/repair-r7-report.md`, change "part-specific batch rejection rewrites" to describe what was actually done.

## 5. R7-05 and R7-06: notes for step 3

- **The limits note.** Add to the map and the insights limits: same-type and branch counts are lower bounds. About one sampled rejection in five or six is related, so step 3 searches family members and the item-level demand links (union links, R5-03), not only the recorded relations.
- **Missing spaces.** Restore spaces in the new R7 prose where they are missing: correction entries, insight headings and method strings. This is cosmetic.

## Deliverables

- **The updated analysis files and tools,** with a regenerated `analysis-snapshot.json`.
- **`workbench/checks/repair-r7-closeout.md`, containing:**
  - a table of the 12 re-decisions: best member, sub-part, decision, and the reason or the differing decisions;
  - the three gap-record changes;
  - the family changes and their new decisions;
  - before and after counts: relations by kind, exam parts with no textbook relation, and demands with same-type textbook practice.
- **STATUS.md and HANDOVER.md** updated. The next step is step 3 (the recipe contract and the pilot PLAN). Claude confirms this close-out at the start of the step-3 review.

## Checks before handing back

- The double rebuild passes in a fresh copy, and all seeded negatives still fail.
- **New negative fixture:** a nonordered rejection whose family has a member sub-part named as a related lead, with no member-level reason.

## Constraints

- Do not commit or push; Vitalis commits.
- **Do not modify:** any review folder, source PDFs, `standard/`, other subjects, app code or pinned checkouts.
- Acquire anything only with the YYeni Web Harvester. Write no new scraping scripts.
- Textbook originals stay internal (`learner_display: false`).
- No PLAN, recipes, generators, work orders, imports or learner assignment in this close-out.
- No relabelling of item-level demand links (R5-03). Family-level demands may be set as in item 3.
