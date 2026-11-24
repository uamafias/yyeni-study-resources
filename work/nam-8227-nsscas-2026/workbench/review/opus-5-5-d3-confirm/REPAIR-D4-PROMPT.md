# Stage-D design repair D4: NSSCAS Mathematics 8227

You are Codex, the PLANNER for the 8227 Workbench pilot. The workspace is `work/nam-8227-nsscas-2026/`. Vitalis's decisions are final.

## Where the plan stands

Claude checked D3 (manifest `4667a860…`).
- **Confirmed:** most of D3, including the motion enumeration, all counts, capacities and exemplars, the register layout, the pins and a byte-identical two-copy rebuild.
- **No design blocker.**
- **Not yet confirmed:** four should-fix groups remain.

D4 is a small text repair plus one swap of the four no-change motion contexts.

Read these files in `workbench/review/opus-5-5-d3-confirm/`:
1. `report.md`;
2. `findings.md`. The IDs, locators and repairs are in §D; §B says where our own D3 prompt caused three of the defects;
3. the agent evidence `check-*.json`. Each finding names its agent ID; read that record before changing anything.

**Owner decisions.** OD-1 to OD-6 bind. Do not reopen the recipe selection. The only domain change allowed is the motion no-change contexts in §3.

**Before you change anything,** copy `planning/plan-manifest.json` (sha256 `4667a86020652f09a8c8b8e7df8612fb08656c1254a5eed20b319e77a6354fc7`) to `planning/history/plan-manifest-d3.json`, and keep the D3 candidate files recoverable under `planning/history/d3-candidate/`.

## 1. D3-S01: separate the owner decision from the operational rules

**What is the owner's (OD-6, binding):**
- a genuine misread of question data, with object and difficulty unchanged, costs one mark, deducted from the A or B marks;
- all A and B marks then follow through on the misread value, and M and DM are judged as usual;
- misreading the learner's own figures is an accuracy error;
- a misread that changes the object or difficulty gets no misread treatment;
- practice feedback names the misread.

**What is not the owner's:** the unit, the order, the ledger and the eligibility details. They are **proposed operational rules, pending Vitalis's approval** of the exact manifest. They came from our D3 prompt and from your design.

**Where to fix it:**
- `planning/OWNER-CHECKPOINT.md:15,43`;
- `planning/d3/deviation-register.json:190,192`: the OD-6 row stays an owner decision, and a separate row holds the proposed operational rules;
- `subject-rules.md:67`: label only the principle binding;
- `HANDOVER.md:17`;
- `recipe-contract.md:303`;
- the "owner approved" tag in the trig dispositions.

Do not edit the D3 archives; supersede them.

## 2. D3-S02: restate MR03 once, then copy it consistently

Rewrite `subject-rules.md` MR03, then make the misread line in all nine work orders and the `misread_policy` of all 27 parts agree with it.

**(a) No free misread.** Make one deduction per misread datum. Take it from the first A/B earned on that datum in question order: the first-use part, otherwise the next part that uses the datum. Nothing is deducted only if no A/B is earned on that datum anywhere.
- Re-mark the vector OB sign misread plus a wrong resultant: 4/7, not 5/7.
- Re-mark motion V 12→21 plus the wrong −V/k factor: 2/5, not 3/5.

**(b) Net penalty.** The deduction is applied after marking. The criterion it comes from still counts as earned for every dependency (DM, "dependent on", www), so one misread never costs more than one mark. Show this on a motion R2/R4 case and a calculus G2 or S2 case.

**(c) Eligibility is decided once.** Decide it at first use and record it in the ledger. An ineligible misread is marked canonically in every later part. State the single outcome of each of these:
- the vector no-p misread in (b): expected 3/7;
- the two implicit-normal edges in calc-D3-02;
- a motion misread that flips the sign-change outcome. This changes the object, so it is marked canonically.

**(d) No-solution clause.** "Leaves no solution" means no solution where the canonical question has one. A designed "no real solution" outcome (principal inverse) keeps the OD-6 treatment. Add the (3, −3π/4) read as 3π/4 fixture: 2/3.

**(e) Qualifiers.** For eligible misreads only, OD-6 follow-through overrides "not F.T." and c.a.o. qualifiers. State this in MR03, and add a pointer at motion S3 (`WB8227-motion-integration.md:46`, `calculus-design.json:3560`) and at the trig c.a.o. qualifiers.

**(f) Feedback sentence.** Add "practice feedback names the misread" to MR03, to the 13 policies that lack it (motion 6, visual 7) and to the motion, modulus and trapezium work-order lines. Remove the trig-only "unless the actual scheme specifies an order", or justify it in MR03.

**Then:**
- recompute every misread sample and fixture under the restated rule;
- update `planning/d3/misread-policy-check.json`, or its D4 successor, so the ledgers are derived, not typed in.

## 3. D3-S03: motion

**(a) Remove the ratio shortcut.**
- **The problem:** all 24 no-change tuples use c = 1.
  - "−b/a ≥ T" separates all 168 instances.
  - |b| ≥ 4|a| and v(0) = v(T) occur only in no-change cases.
- **What to change:** spread c (and r if needed) across the four no-change contexts. Keep the root beyond T by a clear margin, no root at an endpoint, a bounded minority, and T and |k| shared by both outcomes. The reviewer's candidate is (4,1,3), (4,3,3), (5,2,4), (6,3,5). Choose your own if you have a better reason.
- **Extend the separation test** to derived features: −b/a against T, |b/a| thresholds, d/a, v(0) = v(T), the vertex against T/2, and triples containing T. Report the best lookup accuracy for each.
- **Then re-check:**
  - re-enumerate the domain;
  - re-run the nine sweeps at 3 s.f. decimal half-up;
  - recompute the affected exemplars;
  - update the counts, shapes, directions, part keys, aliases and capacity sum.

**(b) Remove the vertex route.** Delete "or a vertex bound" from R1 (work order `:49`, `calculus-design.json:5439`, `pilot-design.json:6532`). In this domain the vertex lies inside (0, T), and its value never proves constant sign. Keep endpoint signs plus concavity, or name another route that is valid here. Add a fixture: a vertex-value-only argument scores R1 = 0.

**(c) Correct the stale count.** `PLAN.md:54` says "54 triangle-method coincidences"; use the current exclusion count.

## 4. D3-S04: trapezium k = 2 fixture

Keep b:B1 for the factorised form, as official row 04 gives it. Wrong log-law reasoning after the factorised form loses b:B2 (www), in line with work order `:85` and `:110`. The fixture stays a feedback fixture.

Align these:
- `planning/visual-design.json:580`;
- `pilot-design.json:680`;
- the trapezium work order `:139`;
- exemplar `:91`.

## 5. Notes to apply while editing

- **Naming clash:** rename "owner decision 6" (the 16 November visual-demand decision) at `PLAN.md:74`, trapezium work order `:58`, modulus `:39` and vector `:55`, so it cannot be read as OD-6.
- **Stale wording:**
  - modulus work order `:45` ("bind every row");
  - the shared-D3-05 lines;
  - leftover "short check" gate wording.
- **Motion:**
  - motion-D3-08: change "may earn 4/4" to "earns 4/4";
  - motion-D3-09: correct the D1 label on the new case.
- **Calculus and trig:**
  - calc-D3-05: remove the pasted proof-target sentence from criteria that have no target;
  - trig-D3-04/05.
- **Report and receipts:**
  - correct the D3 report locators (calc-D3-06, trig-D3-07);
  - derive the coverage receipt literals (coverage-D2-03).

**Do not change analysis inputs or tools in D4.** If you do, re-run the R7 rebuild in two fresh copies plus the negatives.

## Deliverables

**`checks/plan-repair-d4-report.md`** must contain:
- a disposition for D3-S01 to D3-S04, with the file:line of each change;
- before/after counts for the motion domain: capacity, outcome split, shapes, directions, part keys, capacity sum;
- the extended separation table and the nine sweeps;
- an independent recomputation of every changed sample and fixture, including the four re-marked misread cases in §2.

**Other files to update or create:**
- a new `planning/plan-manifest.json`, pinning all live `checks/plan-*` files;
- `planning/OWNER-CHECKPOINT.md`, with the split OD-6 rows, and approval still pending;
- STATUS.md and HANDOVER.md.

**The prompt for Claude.** Write the D4 confirmation prompt at `planning/CLAUDE-D4-CONFIRM.md`, limited to the D4 changes. Claude then confirms, and Vitalis approves.

## Constraints

- **No commit or push.** Vitalis commits.
- **Do not modify:** any review folder, the source PDFs, `standard/`, other subjects, app code or pinned checkouts.
- **Scope:** no stage-E authoring, generators, runtime items, imports or learner assignments.
- **Sources:**
  - Textbook originals stay internal.
  - NSSCAS and Cambridge originals appear only with attribution, and never as generated variants.
  - Cambridge is always a comparable board, never Namibian.
  - Held originals are never anchors.
- **Acquisition:** use the YYeni Web Harvester only. Write no new scraping scripts.
