# Claude review of Codex's plan completion and authored package, 2026-10-18

Scope: Codex's Step 4 repairs, its approval records, and the Step 5 draft (886 items, 1,102 claims, 50 content units, about 57,100 unit words). Nothing in the workspace was edited. Checks were rerun on a scratch copy. Three independent readers sampled 223 items (all 15 performance tasks plus random flashcards) and read the notes for topics 1, 2, 4 and 5 in full and the main sections of topic 3. This is a sample, not a full read, and it is not the Step 6 review or a named-teacher verification.

## Verdict

The plan is sound and honestly recorded. The authored package is **not release-ready**, but it is closer than the C-35 block suggests. The science in the sample is good. The faults are packaging faults that can be fixed mechanically.

## 1. The C-35 "framework blocker" is a one-line profile omission

Codex reported C-35 as a shared-framework defect: the checker treats the words "graph" and "chart" in four prompts as a break-even chart. The framework already has the switch for this. `standard/v0.2.0-draft/checks/yyeni_checks.py:581-583` reads `depictions.chart_model`, and `none` makes C-35 check only items that declare a chart. The CHANGELOG records it, and the 0460, 9702 and 9618 profiles set it. Biology's `subject-profile.yaml` simply does not.

Verified on a scratch copy: adding `chart_model: none` under `depictions:` makes all five topics report PUBLISH (checks only) with warnings C-18, C-20 and C-26 and no failures. The four items are ITEM-6116-1-044-PROC, 3-258-APP, 4-089-PROC and 5-045-APP.

This is a defect in the Biology profile, which is a planning input. It is not a framework defect, and it should be withdrawn from the Vitalis report. I made no change to the real profile, because Codex was told not to edit protected inputs.

Interpreter trap: the checker loads YAML with `yaml.safe_load` and returns no profile if PyYAML is missing. System `python3` has no PyYAML, so checks run that way silently use no profile. Use `.venv/bin/python`. Codex's report is consistent with the venv.

## 2. Release blockers in the learner text (systematic)

| Problem | Where | Size |
|---|---|---|
| Internal figure codes, "reviewed" and "pending" wording in learner prompts, so the item cannot be answered | 40 held items citing `Fig. VIS-6116-…` | 40 prompts, 20 answers or guidance |
| Pipeline wording in the notes ("remain pending", "visual hold", "A/B", "disputed past-paper mapping", "the bank") | topic 3 about 52 lines, topic 4 7, topic 1 5, topic 5 3, topic 2 1 | about 68 lines |
| Rubric template labels in marking guidance that do not fit the item ("Named feature:", "Data/reading:", "Proposed:", "This situation:") | 198 items | 198 items |

The 40 image items are held, which is correct by the plan. The held state must also be visible in the build. The held wording must not reach a learner, and the notes need the contamination removed before any release.

## 3. Content findings from the sample

- **No confirmed arithmetic or genetics errors.** Every calculation and cross the readers recomputed was correct. Confirmed science weaknesses were few:
  - "beak" as a diagnostic bird feature (ITEM-6116-2-020).
  - A credited oxygen consequence of deforestation that overstates the effect (5-033).
  - Smaller doubts: quiver-tree leaf storage, the "virus reproduce" wording, and the kidney-tubule and water-channel mentions against scope.
- **Mark design.** Several 2-mark items credit a remedy the question never asks for (1-028, 1-083, 1-016, 1-089, 1-095). Some 1-mark items hold two or four facts (3-243, 3-221, 5-038). Some DEF cards split a short definition into two marks (4-079, 4-099, 4-001). Guidance often pastes the answer instead of naming each creditable point.
- **Labels.**
  - Bloom is inflated on several tasks (3-P03 Evaluate, 3-P02 Analyse, 4-P02 Analyse, 5-105 Create against "describe").
  - 2-P03 is linked to a drawing objective but is ecological counting.
  - 3-161 is labelled AO3 but explains a known concept.
  - Seven generic EVAL cards are labelled AO1. This follows the operator's settled "taught comparison is A" decision, so it is intentional. The cards still carry Bloom "Evaluate" and should be aligned.
- **Notes.** They are repetitive and over-hedged ("do not claim…", "Where this connects…"). Several headings mislead (3.4, 3.6.2, 3.13.1, 4.3.2, 5.2). Some sentences are garbled (4.2.1, 5.1). Namibian content is thin but not invented.
- **Originality.** My own eight-word screen of all items and notes against the 18 papers and the report text found 21 texts with overlap. They are all syllabus definitions, which the handover allows. No question stems were copied.

## 4. Status of the build and the evidence

- Topics 1, 3, 4, 5: REJECT on C-35 only (see section 1). Topic 2: PUBLISH.
- Units below minimum: 16 of 50. Most miss by under 5%. The largest shortfalls are 4.2.2 (77%), 4.1 (82%), 4.4.3 (84%), 3.13.3 (86%) and 3.12 (87%). Total unit words are 57,133 against a budget of 50,800–80,040. Topic 4 is at 96% of its minimum.
- All 1,102 claims are `unverified` and `publishable: false`. 442 have no evidence entry (topic 1 has none at all). Verification waits on a named teacher and textbook (SRC-SCHOOL), which are still unnamed.
- Authored AO mix by marks: A 56.6 / B 17.0 / C 26.4 against the stated 47/28/25. This matches the approved coverage-first decision. Expect a skewed bank: only 17% of marks practise application and analysis, against 28% in the paper.
- Protected inputs: nothing under `standard/`, `curriculum/`, `planning/` or `exemplar/` is newer than the approved PLAN, and no commit or push.

## 5. Visual bank and approvals

Codex's holds and derivative disclosures are sound. Ten assets are held and counted towards no need. The operator approval covers all 254 assets and pins their hashes. It rightly does not supply reuse rights or scientific verification: the reference-only extractions remain unreleasable and the accuracy defects are still recorded. Delivery in YYeni is still unavailable.

## 6. Recommended next steps, in order

1. Add `depictions.chart_model: none` to `subject-profile.yaml` and rebuild. This needs authorisation, because Codex treated the profile as protected. Withdraw the C-35 framework item.
2. Strip pipeline wording from notes, prompts and guidance, and make held items unmistakably non-releasable.
3. Replace the 198 template guidance blocks with one creditable sentence per mark, and fix the tariffs listed in section 3.
4. Correct the confirmed science points and the Bloom/AO labels. Tighten the notes (repetition, headings, hedges). Lift the 16 thin units.
5. Name the Biology verifier and textbook, then run a source and scientific verification pass on the 1,102 claims. Run the Step 6 cross-vendor review afterwards.

> Correction, 2026-10-19: the "442 claims with no evidence entry" above was summed from a stale topic 4 figure (75). The ledger-derived count is **448** (topic 4 is 81): topics/authoring_audit.json.
