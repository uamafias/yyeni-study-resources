# Stage-D design repair D3: NSSCAS Mathematics 8227

You are Codex, the PLANNER for the 8227 Workbench pilot. The workspace is `work/nam-8227-nsscas-2026/`. Vitalis's decisions are final.

## Where the plan stands

Claude confirmed D2 (manifest `2b9e53a5…`).
- **Repaired:** D1-B01, OD-4 and OD-5, and 28 of the 31 D1 findings.
- **Reproduced:** every count, capacity, exemplar and rebuild output.
- **No design blocker remains.**

D3 is a small repair. It covers one new owner decision (OD-6, misread), one domain change in the motion branch, and twelve text corrections.

Read these files in `workbench/review/opus-5-5-d2-confirm/`:
1. `report.md`;
2. `findings.md`. The IDs, locators and repairs are in §D. §B lists where our D2 prompt caused two of the motion defects;
3. `owner-decisions-2026-11-24-d2.md`, which records OD-6.

The agent evidence is in `check-*.json`. Each finding names its agent ID; read that record before changing anything.

**Owner decisions.** OD-1 to OD-6 bind. Do not reopen the recipe selection. The only domain change allowed is the motion one in §2.

**Before you change anything,** copy `planning/plan-manifest.json` (sha256 `2b9e53a54664e70feb4f0546c1a4967eab2d21bd5d5c2efbed77b57c9d8543f2`) to `planning/history/plan-manifest-d2.json`, and keep the D2 candidate files recoverable under `planning/history/d2-candidate/`.

## 1. OD-6: misread (owner decision)

Replace D2-MISREAD-ALLOCATION everywhere with the Cambridge convention Vitalis chose.

**The rule:**
- A genuine misread of question data, where the object and difficulty of the question are unchanged, costs one mark, deducted from the A or B marks. All A and B marks then follow through on the misread value. M and DM marks are judged as usual.
- Misreading the learner's own figures is an accuracy error, not a misread.
- A misread that changes the object or difficulty of the question gets no misread treatment, and is marked as normal against the canonical question. Examples: one that makes the task easier, or one that leaves no solution.
- Cite NSSCAS 2025 report PDF 345, item 4 (`CONVENTION:108`), and Cambridge `9709_m16_ms_12.pdf` PDF 3, "Penalties". Label Cambridge as a comparable board's convention, never as Namibian.

**Settle and state these:**
- **The unit.** Make the deduction once per misread datum, in the part where it is first used. Later parts that use the same misread value follow through with no further deduction. If you choose differently, say why.
- **No A or B marks earned.** If there are no A or B marks to deduct from, nothing is deducted.
- **www and named errors.** A follow-through on a misread value still needs correct working. It never rescues a named error or an answer given without working (OD-1).

**Where to apply it:**
- `subject-rules.md` (MR03; the headings at :43 and :57, so that only the OD-backed rules are called binding; and :149).
- One consistent misread line in each of the nine work orders. Remove the implicit G1–G5 example from the stationary work order.
- A `misread_policy` for every part in the design JSON, including the calculus recipes, which have none. Correct the vector (a) copy.
- Every exemplar sample: motion V = 21; the V = 18 and V = 30 copies; vector.
- The register: replace the D2-MISREAD-ALLOCATION row with an OD-6 owner-decision row.

## 2. Motion: make the outcome unpredictable from visible parameters

- **D2-S01.**
  - Overlap the no-change and sign-change classes on T and on |k|. For example, admit no-change tuples with T ∈ {3, 4, 5} and |k| ∈ {1, 3}, with the positive root beyond T by a clear margin.
  - Keep a bounded minority, state its proportion and give your reason.
  - Show that no single visible parameter, or simple pair of them, separates the outcomes.
  - Use a strategy-neutral public title, for example "Distance and displacement from a quadratic velocity".
- **D2-S02.**
  - Add an R1 alternative: a valid complete argument that v keeps one sign on [0, T], such as endpoint signs plus concavity, or the vertex value. It earns the same award, and the two routes are not additive.
  - State the score when a slip puts a root inside (0, T) in a no-change case and the split total is still canonical.
  - Disclose the vertex/zero split coincidences.
- **D2-S03.** Change R5 to "… or the signed sum of the legs from (a), evaluated from an attempted primitive with both bounds". Align the work order, both JSON files and the exemplars.
- **Re-check after the change:**
  - re-enumerate the mixed domain;
  - re-run the named-error and coincidence sweeps at the marked precision (triangle, signed area, |∫v|, always-split, never-split, wrong root, harmless interior split);
  - recompute every changed exemplar;
  - update the capacity, normalised shapes, part keys and the key-alias rule. Cross-reference the alias rule in the work order (motion-D2-11).

## 3. Text corrections

Fix D2-S04 to D2-S13 as each row of `findings.md` §D describes. In short:
- **S04: authority.** Re-attribute two records: "owner OD4 permits … one fixed 4+2 rubric", and the "owner-fixed" log domain.
- **S05 to S07: stale figures.** Capacity 387 → 402. Regenerate the `@0.1.1` Bloom rationales. Fix the Bloom 4 line in the stationary exemplar, and the D1 receipt citations.
- **S08 to S12: contradictory marking text.**
  - S08: back-substitution goes in S4.
  - S09: principal no-real P-B1, plus a 0/3 fixture.
  - S10: R-form :84.
  - S11: trapezium packing 3 vs generated-fresh 2.
  - S12: the trapezium "2k scale" must be derived from the log law, plus a 1/2 sample row.
- **S13: the approval record.** Restore normal spacing in the register, give every row a status class, and mark `checkpoint-stage-d.json` historical.

Also apply the §D notes where they touch text you are already changing. Pin the live `checks/plan-*` files in the plan manifest (closeout-D2-02).

**Do not change analysis inputs or tools in D3.** The two remaining close-out notes, closeout-D2-01 and closeout-D2-03, go into HANDOVER as later maintenance. If you do change any analysis file, re-run the R7 rebuild in two fresh copies plus the negatives.

## Deliverables

**`checks/plan-repair-d3-report.md`** must contain:
- a disposition for D2-OD6 and for each of D2-S01 to D2-S13, with the file:line of each change;
- before/after counts. At least: the motion mixed capacity, outcome split and shapes; any changed part keys; Bloom; deck totals;
- the motion separation test and the sweeps from §2;
- an independent recomputation of every new or changed exemplar, including each misread sample under OD-6.

**Other files to update or create:**
- a new `planning/plan-manifest.json`;
- `planning/OWNER-CHECKPOINT.md`, with the OD-6 row and the readable register, and approval still pending;
- STATUS.md and HANDOVER.md.

**The prompt for Claude.** Write the D3 confirmation prompt at `planning/CLAUDE-D3-CONFIRM.md`, limited to the D3 changes. Claude then confirms, and Vitalis approves.

## Constraints

- **No commit or push.** Vitalis commits.
- **Do not modify:** any review folder, the source PDFs, `standard/`, other subjects, app code or pinned checkouts.
- **Scope:** no stage-E authoring, generators, runtime items, imports or learner assignments.
- **Sources:**
  - Textbook originals stay internal.
  - NSSCAS and Cambridge originals appear only with attribution, and never as generated variants.
  - Held originals are never anchors.
- **Acquisition:** use the YYeni Web Harvester only. Write no new scraping scripts.
