# Stage-D text errata D4.1: NSSCAS Mathematics 8227

You are Codex, the PLANNER for the 8227 Workbench pilot. The workspace is `work/nam-8227-nsscas-2026/`. Vitalis's decisions are final.

## Where the plan stands

Claude checked D4 (manifest `71ee10b6…`).
- **All four D3 groups are repaired.**
- **No design blocker remains.**
- **Two should-fix text items remain**, both in wording Vitalis would be approving.

D4.1 is a **text-only errata**. It changes:
- no mark, tariff, domain, answer or fixture score;
- no analysis input or analysis tool.

**Read first,** in `workbench/review/opus-5-5-d4-confirm/`: `report.md` and `findings.md` §B and §D, plus the `check-*.json` record behind each ID.

**Before you change anything,** copy `planning/plan-manifest.json` (sha256 `71ee10b6388064079137412da8834623b63e7179af7e0b8a280a345f13f1e4bb`) to `planning/history/plan-manifest-d4.json`, and keep the D4 candidate recoverable under `planning/history/d4-candidate/`.

## 1. D4-S01: two authority residues

Reword these two lines so they no longer credit the per-datum unit to OD-6. For example: "follows MR03: the OD-6 MR−1 principle, under the proposed MR03-OPS-D4 per-datum mechanics".
- `work-orders/WB8227-vector-geometry.md:73`;
- `exemplars/WB8227-implicit-normal.md:125`.

Then grep the live files once more for "OD-6" next to "once-per-datum", "per-datum", "first-use" or "ledger".

## 2. D4-S02: clarify the MR03 operational sentence

Add three clauses to the MR03-OPS-D4 operational sentence. It appears in:
- `subject-rules.md:67`;
- `planning/d4/shared-misread-policy.json` `operational_rules` and `work_order_line`.

Propagate it with your existing script to all nine work-order lines and all 27 part policies, including the pilot-design and part-register copies.

1. **Define "on that datum":** "An A/B is on a datum when it lies in the datum's first-use part or a later part whose working uses the misread data, whether or not that criterion's own value changes." This is the convention every current fixture already uses. Do not change any fixture tags or scores.
2. **Eligibility:** "Eligibility is judged at first use for the connected question." Implicit WO `:142` already says this.
3. **Override limits:** "Eligible follow-through never overrides MR09 (no F.T. into a supplied result) or OD-1 answer-only rules." This restores the D3 limit that our D4 prompt §2(e) left out.

Keep the authority split exactly as D4 has it: the OD-6 principle binding, the operations proposed and pending.

## 3. Notes to apply while editing

Each is text-only.
- **D4-N01:** `planning/d4/visual-d4-independent-checks.py:95` must write a repo-relative `render_path`, so that the rebuild and freeze check pass in a relocated copy.
- **motion-D4-06:** restore "The D1 short check confirmed …" at `PLAN.md:11`.
- **shared-D4-04, visual-D4-04:** at `capability-gaps.md:34` and `recipe-contract.md:162`, write "16 November owner decision 6 (visual demands)".
- **shared-D4-03, trig-D4-03:** fix the stale labels:
  - `planning/part-evidence-register.md:3`;
  - the calculus and visual status fields named in the finding;
  - `checks/plan-repair-d4-trig-validation.json:2`, via its generator.
- **Motion work order:**
  - motion-D4-01: at `:75`, add one sentence giving the reason for the T 3→5 score of 2/6. R1 judges the decision against the printed interval; R2 does not depend on T; R5 needs an attempted primitive with both bounds.
  - motion-D4-03: at `:35`, say the recipe version is provenance only and does not reset exposure. At `:25`, name 0.1.1–0.1.3 as the old versions.
  - motion-D4-02: at `:73`, say "best **visible** single/pair 156/168", and add that (d/a, T) reaches 162/168.
- **motion-D4-05:** give the polynomial and exponential policies their own eligibility notes instead of the mixed-branch text.
- **calc-D4-01:** qualify the implicit C 4→5 9/9 fixture (`WO:148`, exemplar `:151`) as the product route, and name the other routes as an E/F fixture.
- **calc-D4-04:** give the gradient-only `eligibility_notes` text that fits that branch.
- **visual-D4-02:**
  - cite 2023 P2 Q6 AWARD05 in the row that holds the B2 www clarification, or give the clarification its own register ID;
  - add one clause at trapezium `WO:95`.
- **visual-D4-03, shared-D4-07:** in the errata report, record the generic visual policy tails and the trapezium strict-unseen 3 → 2 correction.

## Deliverables

1. **`checks/plan-errata-d4-1-report.md`:**
   - each change with its file:line, before and after;
   - a statement that no score, tariff, domain or count changed, backed by your existing fixture checks;
   - the rebuild and freeze results.
2. **A new `planning/plan-manifest.json`** pinning all live `checks/plan-*` files and the D4 recovery.
3. **Updated records:** `planning/OWNER-CHECKPOINT.md` (approval still pending), STATUS.md and HANDOVER.md.
4. **`planning/CLAUDE-D4-1-CHECK.md`,** asking Claude for a **diff-only check** of D4 → D4.1. Claude will check:
   - that only the listed lines changed;
   - that the propagated MR03 text is identical everywhere;
   - that no score moved;
   - that the rebuild passes in two relocated copies.

Then Vitalis approves the exact manifest.

## Constraints

- **No commit or push.** Vitalis commits.
- **Do not modify:** any review folder, the source PDFs, `standard/`, other subjects, app code or pinned checkouts.
- **Scope:** no stage-E authoring, generators, runtime items, imports or learner assignments.
- **Sources:**
  - Textbook originals stay internal.
  - NSSCAS and Cambridge originals appear only with attribution.
  - Cambridge is always a comparable board, never Namibian.
  - Held originals are never anchors.
