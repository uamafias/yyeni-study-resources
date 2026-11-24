# Step-3 design review report: 8227 Workbench pilot PLAN

Reviewer: Claude Opus 5.5 (cross-vendor REVIEWER). Date: 2026-11-23. Inputs are frozen in `inputs.json` (plan manifest `dd0e5cfe…`). The findings are in `findings.md`. The owner decisions taken during this review are in `owner-decisions-2026-11-23.md`.

## 1. Verdict: repair the design, then a short check, then owner approval

**The R7 close-out is confirmed.**
- The 12 re-decided pairs hold on the pages.
- The gap records and counts are exact.
- The rebuild reproduces all 275 outputs.

Three residual text corrections are folded into this repair (S3-10).

**The stage-D design is sound in selection, structure and mathematics.**
- All 45 worked examples are correct.
- Every claimed parameter count reproduces.
- No admitted instance is mathematically degenerate.
- All 138 demands are accounted for.
- The same-type references are right per part.
- The capability handoff is honest.

**The marking is not ready.** Design-blocking defects affect 7 of the 9 recipes:
- **Bare answers earn credit,** against the NSSCAS rule "No marks are awarded if only answers are given". Owner decision OD-1 now settles that this rule applies.
- **Official mark-scheme conditions are dropped:**
  - "www" on the modulus recovery;
  - follow-through from the learner's own sketch on the trapezium bias;
  - the exclusion for integrating instead of differentiating on the motion recipe.
- **Valid methods are not credited,** such as the first-derivative sign test for a stationary inflexion.
- **Some admitted instances can't separate a common error from correct work,** for example k = 1 in the exponential motion branch.

These would misjudge learners, so they must be fixed before the owner approves the plan.

**Beyond the blocking defects:**
- **The Analyse labels don't hold.** All three Analyse labels fail as specified, because each branch's outcome never varies or is cued.
- **Exam questions reappear unattributed.** Six cited exam questions sit inside the generated pools.
- **Several capacities count surface variation as new problems.**

## 2. What the repair changes and what it doesn't

**The repair does not reopen the recipe selection.** It covers:
- marking rules;
- domain exclusions;
- three branch redesigns or relabels;
- source reads;
- record consistency.

It adds one show-that part (OD-2).

**After the repair:**
1. Claude makes a short focused check: every blocking item, the new show-that part, and a sample of the should-fix items.
2. Vitalis approves the plan (OD-3).

Codex's brief is `REPAIR-PROMPT.md` in this folder.

## 3. Carry into stage E

- **Marking:** R2-02 per-branch references, R3-07 must-read givens and R5-03 union links remain binding.
- **Answer-only rule (OD-1):** apply it to every new recipe and branch, not only the nine.
- **Later tests from `findings.md` §D:** diagram label placement, rounding boundary values, rendering of notation input.
- **Evidence:** family `distinction_basis` / `units_and_precision` text, templated rejection reasons and extracted notes remain non-evidence.

## 4. Limits

- **Delegated reading.** Seven agents did the page reading and domain enumeration. Their evidence is in the `check-*.json` files in this folder.
- **My own verification** covered the following:
  - the two visual blocking findings, on the rendered 2023 and 2025 examiner-report award tables;
  - `CONVENTION:076`;
  - the answer-only wording in three work orders;
  - the stationary-inflexion method wording;
  - the 72 inverted reasons;
  - the rebuild and the negative fixtures.
- **Agents are not a second blind read.** Each recipe was read by one agent, so marking judgements at the margin (for example, how strict a B1 should be) carry that limit.
- **Not run:** no app, generator, renderer or MCP operation exists or was run. This verdict applies to the hashed state in `inputs.json`.
