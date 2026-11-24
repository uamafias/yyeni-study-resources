# D3 confirmation report: 8227 Workbench pilot PLAN

**Reviewer:** Claude Opus 5.5 (cross-vendor REVIEWER). **Date:** 2026-11-24.

This is the changed-scope confirmation of Codex's D3 repair.
- **Inputs:** frozen in `inputs.json` (plan manifest `4667a860…`, content digest `75b2e3da…`).
- **Findings:** `findings.md`.
- **Agent evidence:** `check-*.json`.
- **Rebuild:** `rebuild.json`.

## 1. Verdict: not yet confirmed. One more small repair (D4), a short confirmation, then owner approval

**No design-blocking defect remains, and most of D3 is confirmed.**
- **11 of the 14 D2 items are fully repaired.** The other 3 are partly repaired: OD-6, D2-S01 and D2-S02.
- **The new motion domain reproduces exactly:**
  - 168 = 144 sign-change + 24 no-change, minority 1/7, 28 shapes, directions 84/84;
  - T and |k| are shared by both outcomes, and no single visible parameter or pair separates them;
  - all nine sweeps reproduce at 3 s.f. half-up.
- **The OD-6 samples recompute:**
  - motion V = 12→21, 18→81 and 30→36: 4/5 each;
  - vector sign misread: 6/7.
- **The rest holds:**
  - all counts are unchanged (9/14/42/27; Bloom 13/1; decks 19/20/17);
  - every capacity and changed exemplar recomputes;
  - the register is readable, and all 47 live plan checks are pinned.
- **Totals:** 180 independent recomputations, 179 agree; the one disagreement is a finding. 72 marking tests.
- **Rebuild:** the design rebuild reproduces byte for byte in two fresh copies. Analysis, tools and curriculum are unchanged.

**Why approval should wait for D4.** Vitalis would be approving three things that are wrong or contradictory, all fixable in text plus one small domain swap.
- **D3-S01: the record credits Vitalis with choices he did not make.** It says he chose the detailed misread mechanics: one deduction per number, in the first part that uses it, from the earliest accuracy mark. OD-6 decided only the principle. The details came from our D3 prompt and from Codex.
- **D3-S02: the detailed misread rules contradict OD-6 at the edges.**
  - A misread can cost nothing when an unrelated error removes the first accuracy mark (vector 5/7 instead of 4/7; motion 3/5 instead of 2/5).
  - A deducted mark can also cancel a dependent mark, so one misread costs two.
  - Further gaps: reused ineligible misreads, the designed "no real solution" outcome, "not F.T." qualifiers and the feedback sentence.
- **D3-S03: motion.**
  - **A shortcut remains.** A coefficient ratio still predicts the outcome, because every no-change case uses c = 1: "−b/a ≥ T" separates all 168.
  - **An invalid route.** The suggested R1 route "or a vertex bound" never proves constant sign here.
  - **A stale count.** PLAN still says 54 exclusions; the domain excludes 18.
- **D3-S04: the trapezium k = 2 fixture contradicts the official row 04.**

**Three of these trace to our own D3 prompt wording** (findings §B): the first-use-part unit, the "vertex value" example and the too-narrow "single or pair" separation test.

## 2. Next steps

1. Vitalis gives Codex `REPAIR-D4-PROMPT.md` (this folder).
2. Claude confirms only the D4 changes:
   - MR03 and its copies;
   - the register split;
   - the motion re-enumeration and sweeps;
   - the trapezium fixture.
3. Vitalis approves the exact D4 manifest and its register.

## 3. Carry into stage E/F

**Fixtures:**
- calc-D3-04: stationary coefficient-misread eligibility;
- trig-D3-02: degenerate or excluded misreads;
- visual-D3-05: modulus label and strip-count eligibility;
- the more precise vector angle;
- the items already carried in the D2 report.

**Binding rules:** OD-1 to OD-6. The operational misread rules bind only once Vitalis approves the exact manifest.

## 4. Limits

**Who did the checking.** Five same-vendor agents did the re-testing; their evidence is in `check-*.json`.

**What I verified myself:**
- the two misread source pages, rendered;
- the rebuild and freeze checks;
- the write scope;
- each should-fix locator, in the current bytes;
- the motion ratio separator and the vertex claim, from the domain rules.

**Single read.** Each recipe had one agent. Marking judgements at the margin carry that limit.

**Not run.** No app, generator, marker, renderer or MCP operation was run.

This verdict applies to the hashed state in `inputs.json`.
