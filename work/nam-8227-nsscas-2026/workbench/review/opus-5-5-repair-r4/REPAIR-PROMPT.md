# Repair round 5: complete the textbooks and finish the step-2 records (NSSCAS Mathematics 8227)

You are Codex, the author of the 8227 Workbench analysis. Your role is **AUTHOR**; the workspace is `work/nam-8227-nsscas-2026/`. Vitalis commissioned this work, and his decisions are final.

**Owner decision, 2026-11-17:** step 3 waits until the textbook work is complete and accepted. It does not run in parallel. Vitalis wants the textbook findings available when the PLAN is written. See `review/opus-5-5-repair-r4/owner-decisions-2026-11-17.md`.

Claude's focused check of round 4 (2026-11-17):
- **Accepted:** R3-01, R3-02, R3-03, R3-05 and R3-06. R3-07 stays deferred to step 3.
- **Accepted subject to a short correction:** the marking register (R4-01, R4-02).
- **Returned for a narrow repair:** provenance (R4-03).
- **Not yet complete:** the textbook work (R3-08).

This round has two parts:
- **Part 1 (short):** correct the marking rows, the schema and provenance (R4-01 to R4-05).
- **Part 2 (the main job):** take the textbook analysis to completion, including exercise families and a synthesis of insights for the step-3 planner.

When both parts pass Claude's check, step 2 is complete and step 3 can start. This round does **not** create the PLAN, recipe contract, recipes, generators or work orders.

## Read first

1. `AGENTS.md`, `TEAM-PLAYBOOK.md`, `standard/v0.2.0-draft/roles/AUTHOR.md` and `workbench/playbook/`, especially `workbench/playbook/textbook-analysis.md`.
2. `workbench/review/opus-5-5-repair-r4/`: `report.md`, then `findings.md` (every Part 1 item is located there with its page), then `inputs.json`.
3. The textbook findings from round 3: `workbench/review/opus-5-5-repair-r3/findings.md`, sections R3-05 and R3-08.
4. The binding owner decisions: `review/opus-5-5-step-1-3/owner-decisions-2026-11-16.md` and `review/opus-5-5-repair-r4/owner-decisions-2026-11-17.md`.

Before changing anything, copy `analysis/analysis-snapshot.json` (sha256 `f3b682495a66d71f6750e76df7972899eb8cb1a2a4b3f0f87cd15aaef5dccde1`) to `analysis/history/analysis-snapshot-r4.json`.

---

# Part 1: marking, schema and provenance (short)

## A. R4-01: correct 8 award rows (re-read each crop at scale ≥ 4 first)

| Row | PDF | Printed | Fix |
|---|---|---|---|
| 2025 P1 Q7(c) row 04 | 350 | "B1√ FT y ≤ their p" | Condition "F.T. y ≤ their p". Delete the claim that the source prints a strict inequality. |
| 2025 P2 Q2 row 09 (SC2) | 356 | "Just x = 1/4 or −1/2 (Just one leg)" | Earns "x = 1/4 or x = −1/2". Delete the claim that the source prints +1/2. |
| 2022 P1 Q2(b) row 03 | 301 | "M1√ Realizing relationship" | √ is the report's follow-through tick. Add F.T. (y^½ = their roots from (a)). |
| 2022 P2 Q1(b) row 06 | 308 | "y = log₅(5/3) o.e. or 0.317", C.A.O. | Add "o.e." to the alternatives, alongside 0.317. |
| 2022 P2 Q6(b)(i) rows 06–07 | 313 | "A1 can be awarded without M2" sits beside the 4.9° A1; "A0 if more than 2 answers" sits beside the 78.7° A1 | Attach each note to its own row. Record the layout reading and the page 312 commentary ("an accuracy mark"). |
| 2022 P2 Q4(a) row 01 | 311 | "Allow one slip in manipulation for B2" | Apply "allow one slip" to both B1 rows (01 and 02). |
| 2023 P2 Q1(b) row 05 | 331 | "B0, M0, A0 for correct 3 brackets without any working" | Add the clause to the M1 row too, or make it a part-level condition. |

Rule for all source notes: never record "the source prints X" without a scale ≥ 4 crop as evidence.

## B. R4-02: schema and record consistency

1. **E marks.** Keep `E` as a mark type (or add `establishes_given_result: true`) on all 42 printed E rows. Define it in `mark_type_normalisation`.
2. **Self-alternatives.** Remove the main answer from `accepted_alternatives` in the 60 rows where it is repeated. Only printed alternatives remain.
3. **Stale question records.** Regenerate `marking_rule_status` in `question-analysis.json` from the linked award rows: official complete, official with derived completion, or absent.
4. **Small row fixes:**
   - 2023 P2 Q1(c) row 08: fill `what_earns_it` and keep the derived note.
   - 2025 P2 Q3 row 12 (derived): add the c.a.o. that the printed paths carry.
5. **Register these report gaps and defects as source evidence.** They are not award rows. Step 3 authors the missing criteria.
   - 2024 P2 Q4(a): "B3" with only two itemised criteria.
   - 2022 P1 Q1(a): b printed as (x − 3/2)²; b = −3/2.
   - 2024 P2 Q7(b): the headline iterates are truncated.
   - 2024 P1 Q11(c): a dangling "OR".
   - 2023 P2 Q9(a): a garbled "v′ = k".
   - 2021 P1 Q6 commentary: "OP" should be "OB".
   - 2021 P2 Q12 commentary: "√18 or 2√3" and "0.123…".
6. **R4-05.** Reword rule 076's interpretation to cover all its evidence contexts (calculators that differentiate, integrate or solve cubics). Explicit B, SC and F.T. awards still govern.

## C. R4-03: provenance

1. **Add five pairs.** Confirm each on both rendered pages, with part correspondence, a complete "changed" field (including tariffs) and draft hidden labels.
   - 2023 P2 Q8 ← 9709/22/M/J/18 Q5 (duplicate /23)
   - 2023 P2 Q1 ← 9709/21/M/J/16 Q4
   - 2025 P2 Q3 ← 9709/21/O/N/22 Q3 (duplicate /23)
   - 2023 P2 Q3(a) ← 9709/22/F/M/20 Q1 (part-level; Q3(b) stays with 024)
   - 2023 P2 Q5(a) ← 9709/22/M/J/19 Q3 (duplicate /23; part-level; Q5(b) stays with 010)
2. **Correct the "changed" fields:**
   - delete the false clause in 006 and the inaccurate clause in 021;
   - add the omissions in 028(b) (the sign change: the quadratic 3t² + 5t − 2 becomes 3t² − 5t − 2; the degrees change belongs to (a)(i));
   - 024(b)(ii): the "Hence" link is lost;
   - 025: the variable is renamed and the instructions changed;
   - 014(c): the wording now names both options;
   - 026: the domain is now inclusive;
   - 029: the diagram is redrawn;
   - 011: the "shared" field should say 1/cos²x.
3. **Register the 2024 P2 Q7 diagram defect.**
   - With y = ¼, t ≈ 0.289, so P is at x ≈ −2.50, left of the y-axis and below the y-intercept (≈ 0.79). The diagram draws P to the right of the axis and above the intercept.
   - Link it to pair 012, and add a source note to the learner-displayable original reference.
4. **Duplicates and structural items.**
   - Fold 004 into 003 as a duplicate-variant lead, with one learner label.
   - Re-record structural030 as "possible source (wording only)": "The point P lies on AB such that AP = k·AB" is unique to 9709/13/M/J/17 Q4 locally. Explain the external-division defect from it, and keep it hidden.
5. **Replace the boilerplate lead dispositions with a real screen.**
   - Run a rare-phrase and value comparison of every NSSCAS question against every page of the local 9709 corpus, not only the eight ranked pages.
   - Visually dispose of every candidate above a stated threshold.
   - Record the method, the threshold and what was read.
   - A lead that was not read stays "unread". It is not "disposed".

---

# Part 2: complete the textbook analysis (the main job)

**Scope:**
- **Books:** both.
  - YM (`8227-SRC-017`): all 13 chapters.
  - Goldie (`8227-SRC-015`): everything except the recorded scope exclusions.
- **Answer pages:** the pages that answer every in-scope item.
- **Display:** textbook originals stay internal (`learner_display: false`).

**"Complete" means T1 to T6 below are all done.** A zero heading backlog is not proof of completeness, as your own handover says.

## T1. Population census (proof of completeness)

1. Read every page of every in-scope section in both books. For each page, record everything on it and link each entry to its inventory record:
   - every exercise question, worked Example, Try Now, activity, investigation and boxed prompt;
   - every teaching figure.

   A page with no items says so ("prose only").
2. Add everything the census finds that the inventory lacks: headingless activities, connected questions and continuations.
3. **Teaching figures** get their own records:
   - what the figure shows;
   - the demand it teaches;
   - whether the NSSCAS exams use that representation.

   These feed the step-3 diagram spec.
4. **Re-confirm each Goldie scope exclusion on the pages.** R3-05 noted that the chapter 8 exclusion is slightly over-broad.
5. **Two demands have no textbook support:** "Distinguish identity from equation" (`M1:T1:O03:D01`) and "Interpret radian" (`M1:T5:O01:D01`). Search the census for both and record the result with the pages searched. Leads:
   - Goldie PDF 190: an unnumbered identity-versus-equality prompt, in an excluded section;
   - YM PDF 111: degrees and the y = x tangent.
6. Write `analysis/textbook-page-census.json` with page counts per book and chapter. Set `coverage.exhaustive: true` only when every in-scope page is accounted for.

## T2. Item records

1. **Item-level notes.**
   - About 448 items still share a descriptive note with a sibling. Give each one its own note describing that item.
   - Correct any note that contradicts the item's demands. Example: the note on YM C7 Exercise 7 Q1 still says "finite definite integrals", although that demand was removed.
2. **A written mapping rule, applied to every item.**
   - `assessed_8227_demand_ids` holds what the item asks the learner to achieve.
   - Component skills used along the way go in a separate field, such as `component_demand_ids`.
   - Why: in round 3, 64 of the 81 differing links were component-skill judgement calls. The split makes the classification checkable.
3. **Re-check the two systematic classes from R3-08:**
   - `M2:T4:O03:D03` (implicit/parametric) attached to explicit items;
   - the `M2:T2:O01`/`O02` boundary (logarithms versus eˣ and ln).
4. **Apply the `exam_style` definition to every item.**

## T3. Qualifier and limit decisions at value level

For every item whose objective is governed by QUAL01–11 or LIMIT01–08, record the decision from the item's actual values. Examples:
- **QUAL01:** are the modulus coefficients integers? YM C8 Try Now 9 Q2(e), y = −⅓|x| + 2, is outside.
- **QUAL03:** the value of n.
- **QUAL04:** the kind of improper integral.
- **QUAL06:** the axis of rotation.
- **QUAL08:** whether the branch restriction is kept.

Each decision records:
- a status: within, outside (the whole item or named parts) or not applicable;
- the value it rests on, quoted from the item.

Keep "not linked" only where the qualifier genuinely does not apply. Never mark a qualifier as applied just because it is listed.

## T4. Answer accuracy (every item, every assessed subpart)

Expect many defects. In round 3, 9 of the 101 sampled keys were wrong or incomplete, which suggests well over a hundred across the population.

1. **Derive each answer independently and compare it with the printed key.**
   - Use computer algebra or a numeric check where possible.
   - Check sketches and graphs on the render.
   - Keep the scripts in `tools/` so a reviewer can rerun them.
2. **Record one status per subpart:**

   | Status | Meaning |
   |---|---|
   | `matches` | The derived answer agrees with the printed key. |
   | `key wrong` | Record the correct value and the working. |
   | `key incomplete` | Something is missing from the key, e.g. Goldie 3B Q4(iii) lacks θ = 90°. |
   | `no key` | An author-derived answer, labelled as such. |
   | `show/prove` | Confirm the stated result is true. |
   | `sketch` | List the key features a correct sketch must show. |
3. **Record** the exact answer page (not a two-page section span), the method used and the date.
4. **Register every defect as a source defect with evidence.** This covers wrong keys, plus question-print defects found while solving (e.g. YM PDF 122, where x ≠ 3 should read x ≠ −3).
5. **Finish the 20 investigations.** Check every subtask and graph.
6. **Precision and angle units.** Note where a book's convention differs from the NSSCAS rules in `marking-conventions.json`.

## T5. Exercise families and planning insights

This is why Vitalis wants the textbooks finished before planning. Follow "Mine exercise families, not isolated numbers" in `workbench/playbook/textbook-analysis.md`.

### `analysis/textbook-families.json`

Group the items from both books into exercise families. Members of a family share the same learner decisions and structure; different values alone do not make a new family.

Record for each family:
- its ID and member items;
- demand links;
- the learner's decisions;
- givens and unknowns;
- constraints;
- representation;
- scaffolding and connected parts;
- alternative methods;
- units and precision;
- the answer form;
- how difficulty grows across the family, i.e. what makes the hard items hard;
- its relation to the exam evidence, one of:
  - **same type as** an exam pattern (cite the NSSCAS question parts);
  - **structural branch** of an exam pattern;
  - **textbook-only** (no exam evidence; label it `textbook-derived`).

Every claim cites item IDs and pages.

### `analysis/textbook-insights.md`

A synthesis per demand, written for the step-3 planner. Small demands may be grouped by topic. Cover:
- **How each book teaches the demand:** the worked-example method and the order of steps, and where the two books differ.
  - YM is written for this syllabus. Note where its method, notation or answer form differs from the NSSCAS mark schemes or from Goldie.
- **The difficulty range** of the textbook practice, set against:
  - the exam questions;
  - the grade descriptions (owner decision 4, 2026-11-16).
- **Pitfalls the books warn about.** Label them textbook-derived, and say whether the examiner reports (`examiner-difficulties.json`) confirm them.
- **Gaps in both directions:** exam patterns with little or no textbook practice, and textbook families with no exam evidence (candidate variety).
- **Representations and diagrams** the books use that the exams do not, and the reverse.
- **A closing "Implications for step 3" list.** Concrete, cited proposals, such as:
  - candidate branches;
  - scaffold sequences;
  - misconceptions to target in feedback;
  - diagram types.

  They are proposals for the PLAN, not decisions.

Textbook evidence never establishes exam frequency or official marking (playbook). Keep the labels.

## T6. Declare completion

- **Item status.** Set each item's `design_use_status` to "author-complete; awaiting independent check". Only Claude's acceptance promotes an item.
- **No author sample.** Retire `analysis/textbook-review-sample.json` (author seed). Do not prepare or pre-classify a review sample: Claude will draw its own, with its own seed.
- **Say it plainly.** In HANDOVER.md and STATUS.md, state "Textbook population complete; ready for Claude's independent check", with the counts.

## What Claude will check

- **Census:** randomly chosen pages are re-read for missing items or figures.
- **Classification:** a fresh blind sample (at least 10%, reviewer seed) is classified independently. Differences must be judgement-level only, with no systematic class.
- **Answers:** an independent recomputation of a sample finds no unrecorded key defect.
- **Qualifiers:** every value-level decision in the sample is checked.
- **Families and insights:** each claim is traced to its cited pages, and the family splits are justified.

If these pass, together with the Part 1 corrections, step 2 is complete and step 3 can start.

---

## Deliverables

- **Part 1:** updated registers and tools.
- **Part 2:**
  - `textbook-page-census.json`;
  - the updated `textbook-inventory.json`;
  - `textbook-families.json`;
  - `textbook-insights.md`.
- A regenerated `analysis-snapshot.json`.
- `workbench/checks/repair-r5-report.md`, containing:
  - a table mapping R4-01 to R4-05 to what changed, the file and the check that proves it;
  - a table for T1 to T6, with counts before and after: pages, items, teaching figures, item-level notes, qualifier decisions, answers by status, key defects and families;
  - anything still open, with the reason.
- STATUS.md and HANDOVER.md updated.

## Checks before handing back

- **Rebuild.** The deterministic double rebuild passes in a fresh copy, and all seeded negative fixtures still fail.
- **New fixtures.** Each must fail for its expected reason:
  - an E row without its flag;
  - an alternative identical to `what_earns_it`;
  - a part whose `marking_rule_status` disagrees with its linked rows;
  - an item note shared with a sibling;
  - a qualifier marked applied with no quoted value;
  - an answer marked `matches` with no method;
  - a census entry with no inventory record.
- **Marking rows.** Every corrected row is re-read against a scale ≥ 4 crop, recorded with the evidence image and the date.
- **Provenance.** Every new or changed pair is confirmed on both rendered pages.

## Working across sessions

This is a large round, so work in checkpoints. After each checkpoint, update HANDOVER.md so the next session can continue where you stopped.

Hand back when Part 1 and all of Part 2 are done. Hand back earlier only if you are blocked by a decision that belongs to Vitalis; in that case, state the question and your recommendation.

## Not in this round

- The step-3 PLAN and recipe contract.
- R2-02 same-type references per branch.
- The diagram spec, including R3-07 must-read givens.
- Sketch-marking criteria, Bloom levels, grade bounds, shared modules and Cambridge variety targets.

`textbook-insights.md` may *propose* for these; it does not decide them.

## Constraints

- Do not commit or push; Vitalis commits.
- Do not modify:
  - any review folder;
  - source PDFs (do not refile `Y=mc as textbook.pdf`);
  - `standard/`;
  - other subjects;
  - app code;
  - pinned checkouts.
- Acquire anything only with the YYeni Web Harvester; write no new scraping scripts.
- No PLAN, recipes, generators, work orders, imports or learner assignment.
