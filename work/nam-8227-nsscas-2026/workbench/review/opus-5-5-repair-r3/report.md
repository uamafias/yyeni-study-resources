# Focused check report: 8227 repair round 3

Reviewer: Claude Opus 5.5 (cross-vendor, role REVIEWER). Date: 2026-11-17. Inputs are frozen in `inputs.json` (snapshot `208a33a2…389d`; HEAD `11cd03fe` with rounds 2 and 3 uncommitted). Findings are in `findings.md`.

## 1. Verdict: repairs accepted; marking register and provenance returned

**Accepted:** the round-2 repairs, R2-01 and R2-03 to R2-07. Their checks:

- Both crops now carry their missing givens, and all 39 crops are clean.
- The containment check would have caught both original defects.
- The link, edge, parameter, label and held-reference corrections are exactly as commissioned.
- Integrity and the deterministic rebuild hold.

**Returned to the author:** the new source registers. They are not yet fit to be used as design evidence for the recipe contract.

- **Marking register (R13-22 is not closed).**
  - The claim that only 24 questions have award tables is false. The reports print criterion award tables for almost all 119 questions; most are images with no text layer (R3-01, high).
  - 13 of the 196 transcribed rows change marking (R3-02).
  - The convention rules omit general rules repeated every year and several answer-format and sketch rules (R3-03).
- **Provenance (R2-08).**
  - 2 of the 19 matches are templates, not sources.
  - 10 confirmed matches are missing, 7 of them from the author's own top-ranked leads.
  - The "changed" fields omit tariff and wording changes (R3-04).
- **Textbook inventory (R13-23).**
  - It remains partial, as the author says.
  - In the caution set, 2 of 33 dispositions are wrong and 8 are partly right, and real printed errors were missed (R3-05).
  - **Blind 10% sample:** locators, pages, representation, sketch and scope are reliable (100–101 of 101). But demand links are assigned to ranges of items, not item by item (exact agreement 53/101), and `exam_style` is undefined. 9 of 101 book answer keys are wrong or incomplete, and none was recorded (R3-08).

**Step 3 (recipe contract and pilot PLAN) stays blocked until:**
- the full award-table transcription and the convention register are complete and re-checked;
- the textbook population and answer work is either completed or explicitly scoped by the owner.

## 2. What the author got right

- **The commissioned repairs were done exactly**, with build checks that fail for the right reason. The crop containment check is a real control; it rejects both R2 defects.
- **Honest limits.** The report says plainly that the textbook work is incomplete and that no stop rule was applied. It treats an unmatched provenance search as "not original", not as evidence of originality, and keeps derived-from labels hidden.
- **Faithful excerpts and correct arithmetic.**
  - All 75 rule excerpts are verbatim on the cited page.
  - Every page locator in the 196 award rows is correct.
  - Every tariff reconciles.
  - 17 of the 19 provenance pairs are genuine adaptations.
  - 23 of the 33 textbook cautions are correct.
  - Five real textbook errors were correctly found, and two false alarms were correctly cleared.

## 3. Remaining work, in the agreed sequence

### Step 2: finish the source analysis (author, round 4)

1. **R3-01, the full award-table transcription.**
   - Transcribe every printed award table (2021 to 2025, both papers) from rendered pages, into the corrected row schema.
   - Fix the 2021 range (add PDF 243).
   - Record per-question coverage: table present with its page, or absent with its reason.
   - This is the largest item and the one that most affects the recipe contract.
2. **R3-02, row corrections.** Fix the 13 marking-changing rows and the cosmetic rows. Separate accepted alternatives from conditions, and complete the qualifier codes.
3. **R3-03, convention register.**
   - Register each general rule once, with all its evidence pages, and apply it across years.
   - Add the missing question-specific rules, complete conflicts 04 and 05, and link rules to award rows.
4. **R3-04, provenance.** Demote 015 and 019, add N1–N10, complete the "changed" fields (including tariffs), record duplicate variants, and follow the 2021 P1 Q6 lead.
5. **R3-05 and R3-08, textbook.**
   - Correct the dispositions and add the missed errors.
   - Continue the completion work in `HANDOVER.md`: 624 heading leads, answer checks, and a stop rule only if it is earned.
6. **R3-06.** Use repo-relative evidence paths.

Then a focused re-check by Claude of R3-01 to R3-05. The award transcription will be checked by a full second read, as in this round.

### Step 3: recipe contract and pilot PLAN

Unchanged from the round-2 report §3 (references per branch, diagram spec, sketch marking, Bloom, grade bounds, shared modules, thin demands), with two additions:

- **Marking rubrics** are built from the official award rows where a table exists. They are labelled derived only where the coverage table records no table.
- **The diagram spec** names each crop's must-read givens, so that a check can assert they are inside the crop (R3-07).

## 4. Limits

- **Delegated sub-checks.** Four sub-checks were done by read-only Claude agents. Their marking-changing and unsupported-match claims were spot-verified by me on the source:
  - the 2023 P2 Q6(a) ordinates;
  - award tables on 2021 PDF 243, 2022 PDF 302 and 2025 PDF 358;
  - match 015, and new matches N3 and N6;
  - YM PDF 352.

  The other row-level verdicts rest on the agents' renders, which are kept in the scratchpad.
- **Not covered.** I did not read the content of the roughly 95 untranscribed award tables, criterion-to-demand alignment, or textbook items outside the caution set and the sample.
- **Provenance search scope.** It covered 9709 Paper 1 and 2 for 2015–2025 only.
- **No app code was run.** This verdict applies to the hashed state in `inputs.json`.
