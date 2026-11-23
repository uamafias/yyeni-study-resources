# Repair round 6: fix the textbook-to-exam comparison (NSSCAS Mathematics 8227)

You are Codex, the author of the 8227 Workbench analysis. Your role is **AUTHOR**; the workspace is `work/nam-8227-nsscas-2026/`. Vitalis commissioned this work, and his decisions are final.

> **Revised 2026-11-21, after round 6 had started.** Section A is replaced and a new deliverable is added (A.5, the per-objective problem map). Keep the work already done: the r5 baseline copy, the 11 source corrections and the corrected answer-page locators. The first version asked for member-level comparison against any demand overlap. That came to 16,246 pairs, which is more than step 3 needs. This version compares at family level: about 2,080 pairs, every one still decided.

## Where round 5 stands

Claude's independent check of round 5 (2026-11-21):

**Accepted:**
- Part 1: R4-01, R4-02, R4-03 (one part-level pair to add; R5-06) and R4-05.
- T1, the census.
- T2, item records, with a recorded limitation (R5-03; no relabelling needed).
- T3, qualifiers.
- T4, answers.
- T6, the declaration.
- The rebuild.

**Returned:** T5, the comparison between textbook families and the NSSCAS exams (R5-01, R5-02). Figure records also need a narrow repair (R5-04).

**Owner decision, 2026-11-17:** step 3 waits until the textbooks are complete and accepted. This round is that last repair. It does **not** create the PLAN, recipe contract, recipes, generators or work orders.

**What the result is for.** Vitalis wants a problem set for every syllabus learning objective. For each objective, the planner must see:
- the NSSCAS exam questions;
- the textbook practice of the same type;
- the close textbook variants and how each differs;
- the other textbook practice;
- the Cambridge items.

Objectives never examined still get problem sets, built from the textbook and Cambridge evidence. Nothing is discarded because it has no exam match.

## Read first

1. `AGENTS.md`, `TEAM-PLAYBOOK.md`, `standard/v0.2.0-draft/roles/AUTHOR.md` and `workbench/playbook/textbook-analysis.md`.
2. `workbench/review/opus-5-5-repair-r5/`: `report.md`, then `findings.md` (every item below is located there), then `inputs.json`.
3. Owner decisions:
   - `review/opus-5-5-step-1-3/owner-decisions-2026-11-16.md`, especially N1 ("same type as" references);
   - `review/opus-5-5-repair-r4/owner-decisions-2026-11-17.md`.

If you have not already done so, copy `analysis/analysis-snapshot.json` (sha256 `03cde4e4192d6bcd0bd43ab776d283d9f96b12c7da91f53a656996f214b5022d`) to `analysis/history/analysis-snapshot-r5.json` before changing anything.

## Order of work

1. **B.1 and B.2 first:** fix family membership and split topic-led families. Relations recorded before a family is split would have to be redone.
2. **Then A:** the exam comparison and the per-objective map.
3. **Then** B.3–B.5, C and D, in any order.

## A. R5-01: rebuild the exam comparison at family level (the main job)

**What is wrong.**
- No family is ever "same type": all 219 exam links are "structural branch", even where a member differs from an exam part only in values. Examples:
  - YM C8 Try Now 25 Q3 against 2023 P2 Q1;
  - Goldie 5A Q6(ii) against 2021 P2 Q2;
  - YM C8 Try Now 6(f) against 2025 P2 Q2.
- 94 of the 161 "textbook-only" families have every assessed demand directly assessed by an exam part in your own `question-analysis.json`.
- Six insight sections say "Examination parts: none claimed" although exam parts exist. The worst cases are:
  - the trig equations (14 or more parts);
  - identity proofs (2021 P1 Q5(b), 2023 P1 Q8(a), 2025 P1 Q6(a)).

**What to do.**

1. **Candidates.** For each family (after B.1–B.2), list every NSSCAS exam part whose directly assessed demands overlap the family's assessed demands. Do this by script from `question-analysis.json`.
   - **Do not rank or cap the list.** Claude tested both shortcuts against the five same-type pairs named in `findings.md`:
     - a top-2 or top-3 cap by demand overlap drops two or three of them;
     - a filter requiring the exam part to cover all of the family's demands drops two.
   - On the round-5 data this gives 2,080 family–part pairs across 325 families (a median of 5 per family, at most 22). 55 families have no candidate. The numbers will move after B.
2. **Decide each pair.** Record one relation and its evidence:
   - **same type:** the same learner decisions and response; only values, context or wording change. Read both rendered pages, record the date and name the exemplar member or members you read. These relations feed N1's "Same type as …" references.
   - **structural branch:** read both rendered pages and record the date. Name the exemplar members and the specific decision or response that differs, e.g. "member supplies the factor; exam requires finding it". Say whether the branch is easier or harder than the exam form.
   - **rejected:** a one-line reason naming the decision or response that differs, e.g. "shares only the chain-rule demand; the exam part integrates, the family differentiates". A render is not required.

   It may be quicker to work exam part by exam part: each part has a median of 7 candidate families.
3. **Store.**
   - Put the relations on the family as `exam_relations[]`, each with:
     - `part_id`;
     - `relation`;
     - `exemplar_member_ids`;
     - `differing_decision` or `rejection_reason`;
     - `read_date` for same-type and branch relations.
   - Add **member-level** relations only for exceptions: part-level members, and any member the reading shows to behave differently from the exemplar.
   - Derive the family summary from these records; do not assign it as a default. A family is "textbook-only" only if it has no same-type or structural-branch relation. For the 55 families without candidates, record the demands searched.
4. **Fix the named mislinks:**
   - elementary-exponential-primitives: remove 2021 P2 Q2 (no exponential) and test 2021 P2 Q9(a), ∫ (4 − 2e³ˣ)/e³ˣ dx;
   - re-test 2021 P2 Q9(a) against log-derivative-division-integral-chain and mixed-retained-definite-integrals;
   - write a reason of its own for mixed-retained-definite-integrals, because the current one is copied;
   - modulus-quartic-root-count is the same type as 2025 P2 Q12(a).
5. **New deliverable: the per-objective problem map.**
   - Generate `analysis/objective-problem-map.json` and `.md` from the records above. They are derived output; do not hand-edit them.
   - For each syllabus objective, list each of its demands with:
     1. the NSSCAS exam parts that directly assess it, with their year, paper and question;
     2. the textbook families of the same type as one of those parts, with their exemplar items;
     3. the textbook structural branches (close variants), each with its differing decision and whether it is easier or harder;
     4. the other textbook families on the demand (no exam relation), each labelled by kind: a teaching step or drill, practice on a never-examined demand, or another kind you name;
     5. the Cambridge 9709 items already recorded in `cambridge-evidence.json`.
   - Mark demands with no NSSCAS exam part plainly. On the round-5 data that is 11 of the 138.
   - Give header counts, by objective and by demand:
     - with exam parts;
     - with same-type textbook practice;
     - with only variant or other practice;
     - with no practice anywhere.
6. **Rewrite every "Examination comparison" section in `textbook-insights.md`** from the family relations.
   - Each section names its same-type parts, its structural branches and its genuine gaps.
   - "None claimed" is allowed only where no exam part assesses the section's demands. On current evidence, that means radian meaning and conversion, and segments and chords.
   - Replace weak anchors:
     - stationary classification should cite 2022 P1 Q8(b), 2024 P2 Q10(b) and 2025 P1 Q9(c), not only 2021 P1 Q11(a);
     - identity proof should not cite 2023 P1 Q1(b).
   - Update the "Proposals for step 3" where the corrected comparison changes them.
7. **Figures (T1.3).** No figure record may say "pending". For each graphic figure, do one of the following:
   - record whether the NSSCAS exams use that representation, citing the parts; or
   - record the comparison once at family or insight level and point the figure record to it.

## B. R5-02: family membership and demand claims

1. **Every member must assess each of its family's assessed demands.** Where a member does not, either make the membership part-level (name the parts) or move the member to a family it fits. Named cases:
   - numerical-supplied-map-chain: Goldie 6B Q1 and 6B Q3, YM Exercise 13 Q1 and Try Now 11 do not ask for the rearrangement;
   - polynomial-factor-solve: Goldie 11B Q9 is the reverse task;
   - secant-identity-integral: Goldie 5B Q9(i) and 5B Q10(i);
   - parametric-point-plot-support: Example 4.21.
2. **Split topic-led families** into groups that share learner decisions, e.g. natural-log-exponential-values and mixed-retained-definite-integrals.
3. **`distinction_basis`** must state a learner-decision difference from the nearest sibling, not a scope or process note.
4. **`difficulty_progression`** is only for families with more than one member, and it must describe an ordered change. Single-member families say "single item".
5. **Replace the boilerplate** with family-specific text:
   - `units_and_precision` (12 strings across 380 families);
   - `membership_reason` (12 strings across 2,338 memberships).

   The repeated exam-reason disclaimer can go in one top-level `limits` note.

## C. R5-04: figure records

1. **Graphic or text.** Add a field separating graphic figures (graphs, diagrams, drawn tables) from text callouts (formula boxes, REMEMBER/NOTE boxes, key-point lists, margin notes). About 29% of the sampled "figures" are text callouts.
2. **Retire the stale statuses:**
   - "pending actual-value screening" on 1,444 figures;
   - "comparison pending" on 1,733 figures (see A.7).
3. **Content checks.** Mark every figure without a content check `"content_check": "not checked; not design evidence until checked"`. A full figure-content audit is **not** required.
4. **Register these printed errors**, then check each against the render:

   | Book | Figure | Error |
   |---|---|---|
   | Goldie | Figure 6.10 (C6 Worked illustration 7, PDF 170) | x₁ and x₂ labels swapped |
   | YM | C4 TF 83 | the 90°–180° quadrant is labelled "Quadrant 3" |
   | YM | C7 TF 60 | x < 0 infinity sign rules |
   | YM | C11 TF 36 | ln x² = 2 ln x without x > 0 |
   | YM | C10 TF 105 | cos(θ+α) alternative for the extrema |
   | YM | C13 TF 54 | the "both gradients negative" staircase rule |
   | YM | C12 TF 121 | "concave" |
   | YM | C9 TF 58 | duplicated legend name |
   | YM | C9 TF 122 | header "a > 0" should be a > 1 |
5. **Re-check the given/teaching role** of figures that sit inside worked solutions. For example, YM C1 TF 48 and 49 are solution panels, not given.

## D. Small fixes

1. **R5-05, notes.** Regenerate the 634 notes that lost their spaces.
2. **R5-05, answer pages.** For every answer whose key falls at the top of a page, check the page. (The two sampled cases, Goldie 5B Q11(ii) → PDF 346 and YM C3 Try Now 4 Q3 → PDF 599, are already fixed.)
3. **R5-05, slips.** Register:
   - YM C2 Example 7(b), whose working reads "13 − 2(−3)";
   - YM C2 Example 25, which prints Σ3n + 2 without brackets.
4. **R5-06, the missing pair.** Add the provenance pair **2023 P2 Q4(b) ← 9709/22/M/J/20 Q1** (duplicate /23 Q1). Record:
   - both rendered pages;
   - the part correspondence: Q4(b) only, while Q4(a) stays with 027;
   - "changed": bases 2ʸ = 9³ˣ → 3ʸ = 2³ˣ, and 3 s.f. → exact value;
   - a hidden draft label.

   Mention 9709/21/M/J/17 Q1 (y = mx) as a weaker template lead.
5. **R5-06, screen recall.** Record the screen's measured recall on the confirmed pairs in its limitations: currently 16 of 31 are among the candidates. In pair 021, delete "(d) 3→3".

## Not in this round

- **Step-3 work:**
  - the PLAN and recipe contract;
  - R2-02 per-branch references (the family relations from A will feed them);
  - the diagram spec and R3-07;
  - sketch criteria, Bloom levels, grade bounds and Cambridge variety targets.
- **No relabelling of demand links (R5-03).** The direct/component split stays as it is; step 3 will use union links and resolve the overlapping registry demands.
- **No full content audit of the 1,758 figures.**
- **No textbook images for learners.** Textbook originals stay internal. Step 3 plans generated diagrams; it does not reuse textbook figures.

## Deliverables

- **Updated analysis files**, plus their tools:
  - `textbook-families.json/.md`;
  - `textbook-insights.md`;
  - `textbook-inventory.json`;
  - `source-defects.json`;
  - `nsscas-cambridge-provenance.json`.
- **New:** `objective-problem-map.json/.md` (A.5).
- **A regenerated** `analysis-snapshot.json`.
- **`workbench/checks/repair-r6-report.md`**, containing:
  - a table mapping R5-01 to R5-06 to what changed, the file and the check that proves it;
  - counts before and after:
    - families by relation;
    - family–part decisions by kind;
    - member-level exceptions;
    - same-type pairs;
    - "none claimed" sections;
    - figures by graphic/text and by status;
  - the header counts of the per-objective map.
- **STATUS.md and HANDOVER.md** updated. The next step is Claude's short focused check, then step 3.

## Checks before handing back

- **Rebuild.** The deterministic double rebuild passes in a fresh copy, and all seeded negatives still fail.
- **New negative fixtures:**
  - a family with a demand-overlap candidate that has no recorded decision;
  - a same-type or structural-branch relation with no rendered-page read date;
  - a family assessed demand that one member does not assess, without a part-level membership;
  - an insight section with "none claimed" while `question-analysis.json` has a part for its demands;
  - a figure record with a "pending" status;
  - a demand in `demand-registry.json` missing from the per-objective map.
- **Rendered pages.** Every same-type and structural-branch relation is read on both rendered pages, with the date.

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
- **Working across sessions.** Save checkpoints. Report completed checks, not percentages.
