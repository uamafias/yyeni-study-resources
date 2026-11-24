# Stage-D design repair D2: NSSCAS Mathematics 8227

You are Codex, the PLANNER for the 8227 Workbench pilot. The workspace is `work/nam-8227-nsscas-2026/`. Vitalis's decisions are final.

## Where the plan stands

Claude ran the OD-3 short check on D1 (manifest `c8914cf9…`). D1 repaired every step-3 blocking item. The counts, capacities, exemplars, show-that part and R7 totals all reproduce.

**One new blocking defect remains (D1-B01).** Thirty should-fix items also need correcting before approval (D1-S01 to D1-S30).

Read these files in `workbench/review/opus-5-5-d1-short-check/`:
1. `report.md`;
2. `findings.md`. The IDs, locators and repairs are there; §B lists four points where Claude's step-3 review was wrong and your D1 was right;
3. `owner-decisions-2026-11-23-d1.md`, which records OD-4 and OD-5.

The agent evidence is in `check-*.json`. Each finding names its agent ID; read that record before you change anything.

**Owner decisions:**
- OD-1, OD-2 and OD-3 still bind.
- **OD-4:**
  - make the motion direction-change decision live;
  - relabel stationary-point classification Apply 3;
  - the pilot keeps one Analyse branch, which its own criteria must support.
- **OD-5:** accept D1-TRAP-FT-BRIDGE, reworded.

Do not reopen the recipe selection. The only branch change allowed is the motion one in OD-4.

**Before you change anything,** copy `planning/plan-manifest.json` (sha256 `c8914cf96c78367f138058e40ffa62bdc0d9770efa1a6fe787c42b8759a04f22`) to `planning/history/plan-manifest-d1.json`, and keep the D1 candidate files recoverable.

## 1. D1-B01: modulus answer-only (blocking)

OD-1 already settles this, because the official 2023 P2 Q2 row (report PDF 331) awards "a = −2 www B1" etc., plus the allowance for values in the formula.
- Correct a, b and c with no wrong working earn B1 www each, whether given as named values or in the formula.
- Feedback still asks for the vertex or point reasoning.
- Remove `D1-MOD-OD1-LIST` and its "owner-binding" label.
- Update the exemplar sample rows.
- Add `answer_only_*` fields for the three visual recipes in `visual-design.json`.

## 2. OD-4: Bloom and the motion decision

- **Stationary-point classification (D1-S01).** Relabel it Apply 3. Keep the uncued mixed outcomes.
- **Motion reversal (D1-S02, with D1-S11).**
  - Admit a bounded minority of instances where v has no sign change on [0, T]. For example, the positive root lies beyond T, never at T, and keeps a clear margin from it. State the proportion and your reason.
  - Use one outcome-neutral tariff for both outcomes, as in the principal solve-or-explain branch.
  - R1 is M1 for deciding whether v changes sign on (0, T): solve v = 0 (one slip allowed), then compare the roots with the interval or test signs.
  - R3 takes the legs from an attempted primitive with both bounds, and F.T. from their root.
  - R4 depends on R2 and R3.
  - Re-run the named-error and coincidence sweeps on the new instances: triangle, signed area, |∫v|, always-split, never-split and wrong root.
  - Rename the outcome classes honestly.
  - Recompute the capacity, the exemplars and Bloom from the criteria. PLAN: 13 Apply, 1 Analyse.

## 3. OD-5: trapezium bridge (D1-S14)

- Reword the rule. The 2023 Q6(d) row is kept in full: "must be correct from their graph" means own-graph F.T. for B1, and no drawn trapeziums are needed. The only extension is that DB1 is judged on the learner's own curve, supported by 2025 Q4(b).
- Define two missing cases: a drawn chord with a brief statement, and more than one graph in (c).
- Add the c → d follow-through edge (D1-S19).

## 4. The remaining should-fix items

Fix D1-S03 to D1-S30 as each row of `findings.md` §D describes. In short:
- **Principal and R-form:** S03 and S04.
- **Implicit and stationary:** S05 to S08. S05 adds the e-index error and G5 www. S06 maps the alternative proof.
- **Motion and log:** S09, S10, S12 and S13. S09 excludes the part-(a) originals (3,1,2,\*) and (30,½,\*).
- **Trapezium and modulus:** S15 to S18, S20 and S21. S15 compares wrong methods at the marked precision. S16 excludes (2,8,4,\*). S17 judges b:B2 against the learner's own (a). S18 judges c:B1 against the learner's own asymptote.
- **Vector and shared rules:** S22 and S23. S23 decides the misread rule once and applies it everywhere.
- **Records and IDs:**
  - S24: put a consolidated register of every named deviation into OWNER-CHECKPOINT, so Vitalis approves an explicit list.
  - S25: one classification-version string.
  - S26 and S27: coverage wording, citations and the gap row.
- **R7 close-out:**
  - S28: revert the 19 over-negated sentences and negate the 12 that are still inverted.
  - S29: compare sentence polarity against R6, and add an over-negation fixture.
  - S30: restore the freeze scope to the whole workspace, excluding only the review folders and the stage-D files the plan manifest pins.

Also apply the §F notes where they touch text you are already changing.

## Deliverables

**`checks/plan-repair-d2-report.md`** must contain:
- a disposition for D1-B01 and for each of D1-S01 to D1-S30, with the file:line of each change;
- before/after counts. At least: the Bloom split; the motion reversal, polynomial and exponential capacities; trapezium capacity and packing; any changed part keys; deck totals.
- discrimination sweeps for every changed domain, run at the marked precision;
- an independent oracle recomputation of every new or changed exemplar;
- the R7 rebuild in two fresh copies plus the negatives. This is required because S28 to S30 change analysis inputs and tools.

**Other files to update or create:**
- a new `planning/plan-manifest.json`;
- `planning/OWNER-CHECKPOINT.md`, including the deviation register, with approval still pending;
- STATUS.md and HANDOVER.md.

**The prompt for Claude.** Write the D2 confirmation prompt for Claude at `planning/CLAUDE-D2-CONFIRM.md`. Claude then checks only the changed scope, and Vitalis then approves.

## Constraints

- **No commit or push.** Vitalis commits.
- **Do not modify:** any review folder, the source PDFs, `standard/`, other subjects, app code or pinned checkouts.
- **Scope:** no stage-E authoring, generators, runtime items, imports or learner assignments.
- **Sources:**
  - Textbook originals stay internal.
  - NSSCAS and Cambridge originals appear only with attribution, and never as generated variants.
  - Held originals are never anchors.
- **Acquisition:** use the YYeni Web Harvester only. Write no new scraping scripts.
