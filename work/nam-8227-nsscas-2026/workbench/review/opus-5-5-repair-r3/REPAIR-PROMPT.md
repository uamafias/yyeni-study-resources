# Repair round 4: complete the marking register, fix provenance and textbook records (NSSCAS Mathematics 8227)

You are Codex, the author of the 8227 Workbench analysis. Your role is **AUTHOR**; the workspace is `work/nam-8227-nsscas-2026/`. Vitalis commissioned this work, and his decisions are final.

Claude's focused check of round 3 (2026-11-17):

- **Accepted** the round-2 repairs, R2-01 and R2-03 to R2-07.
- **Returned** the new source registers.

This round finishes step 2. It does **not** create the PLAN, recipe contract, recipes, generators or work orders.

## Read first

1. `AGENTS.md`, `TEAM-PLAYBOOK.md`, `standard/v0.2.0-draft/roles/AUTHOR.md` and `workbench/playbook/` (README, quality, templates, textbook-analysis).
2. The review folder `workbench/review/opus-5-5-repair-r3/`: `report.md`, then `findings.md` (each finding gives the locator, the correction and the check), then `inputs.json`.
3. The binding owner decisions: `review/opus-5-5-step-1-3/owner-decisions-2026-11-16.md`.

Before changing anything, copy `analysis/analysis-snapshot.json` (sha256 `208a33a2027295d09c84f70423b370aa27e5626df289114842181383ce64389d`) to `analysis/history/analysis-snapshot-r3.json`.

## A. R3-01 and R3-02: complete the award-table transcription (do this first)

**Why.** The examiner reports print criterion award tables for almost every question, not just 24. Most are **images with no text layer**, so text scanning cannot find them. Work from rendered pages only.

1. **Render and read every page of each Mathematics section:**
   - 2021: PDF 231–243 (the old range stopped at 242; PDF 243 holds 2021 P2 Q12);
   - 2022: PDF 301–316;
   - 2023: PDF 321–339;
   - 2024: PDF 325–343;
   - 2025: PDF 345–364.
2. **Transcribe every award table into criterion rows.** These include at least:
   - 2021 P1 Q1–12 and P2 Q5–12;
   - 2022 P1 Q1–14 and P2 Q1–10;
   - 2023 P1 Q1–13;
   - 2024 P1 Q1–14;
   - 2025 P1 Q1–12 and P2 Q1–12.

   Use the corrected schema:
   - `accepted_alternatives` is a **list of the printed alternatives** ("or", "o.e.", alternative expressions), separate from `condition`.
   - Add SC, F.T., c.a.o., www, s.o.i. and "allow one slip" to `mark_type_normalisation`, with meanings.
   - Wherever you fill in a value the scheme leaves blank, mark it `derived`.
   - Keep exclusive method paths unsummed.
3. **Fix the 13 marking-changing rows and the 7 cosmetic rows** listed in findings R3-02. Start with 2023 P2 Q6(a): the ordinates are ln1, ln3, ln5, ln7, ln9, not ln3…ln11. Move the 2023 Q7(c) degree-path exclusion note from the Q6 table to the Q7 table.
4. **Replace `questions_without_award_tables`** with a per-question coverage table for all 119 questions. Each records `table_present` with its PDF and printed page, or `absent` with the rendered page that shows its absence.
5. **Reconcile** every part and every path total against the printed question-paper tariff.

## B. R3-03: complete the convention register

- **Register each recurring general rule once,** with an `evidence` list of every year and page where it appears. Apply it to all years unless a specific award row overrides it. Must include:
  - "No marks are awarded if only answers are given", quoted with its calculator context (2021 p236, 2022 p307, 2023 p330, 2024 p335);
  - "hence … no marks may be awarded" (2021 p236, 2023 p330, 2024 p335, 2025 p355);
  - formula-sheet variable replacement (2022 p307, 2023 p330, 2024 p335);
  - factorisation or quadratic formula shown (2024 p335).
- **Add the missing question-specific rules from findings R3-03 §2:**
  - f⁻¹(x) notation;
  - vector form not coordinates;
  - "and/or" in inequalities;
  - sketch within the domain;
  - 4 d.p. if decimals are used;
  - unlabelled graphs;
  - the x + 3/2 factor;
  - exact k;
  - two solutions losing the accuracy mark;
  - the first two iterates marked.
- **Complete MC-CONFLICT-04** (2025 PDF 364 "Correct ruled V-shape") **and MC-CONFLICT-05** (2024 PDF 338 prose). Clarify rule 073.
- **Link each rule to the award rows** that state the same requirement.
- **Run a context scan of all report pages** for "must", "no marks", "not accepted", "lose/lost", "condone" and "accept". Every marking-relevant hit must be either registered or recorded as not marking-relevant, with a reason.

## C. R3-04: correct the provenance register

- **Demote 015 and 019** to "structurally similar, no specific source". Remove their derived-from references from the NSSCAS parts.
- **Add N1–N10 from findings R3-04**, each confirmed on both rendered pages, with part correspondence, a complete "changed" field and draft hidden labels.
- **Follow the lead 2021 P1 Q6 ← 9709/13 May/June 2017 Q4.** It may explain SRC-8227-EXTERNAL-DIVISION-2021-P1-Q6.
- **Complete the "changed" field for 001, 003/004, 006, 008, 009 and 011–014, including every tariff change.** Reconsider 009's confidence.
- **Clean up variants and links:**
  - record duplicate Cambridge variants consistently, including for 012, 015 and 016;
  - make `explains_source_defect` consistently null or a defect ID;
  - add the back-link from SRC-8227-POLYNOMIAL-NAME-2024-P2-Q5 to match 002.
- **Give every lead ranked 1–4 in `provenance-search-leads.json` a recorded disposition.**

## D. R3-05 and R3-08: correct the textbook records, then continue completion

- **Fix the two wrong dispositions.**
  - YM C7 Try Now 27(c): the upper limit is ∞, and the value is 1/30. Mark it in-scope, and record the (a) answer error "→ −∞" as a printed error.
  - YM C8 Exercise 8 Q7: this is the remainder theorem, which LIMIT05 does not cover. Make it a calibration caution.
- **Fix the 8 partly-right items and add the missed printed errors listed in R3-05.**
- **Apply the learner-built-rearrangement limit consistently** (Goldie 6B Q5(iii)–(iv) and Q6(ii) against YM Try Now 6).
- **Correct the QUAL01 citation at PDF 127.**
- **Record the Goldie 3E3, 5B12 and 6B2 answers as "not applicable (show/prove)".**
- **Apply the blind-sample corrections in findings R3-08:**
  - replace range-level demand and note assignment (`1B|1-6` style) with item-level records, and fix the listed over-mappings and omissions;
  - apply QUAL01–11 in scope checks;
  - define `exam_style` and apply it consistently;
  - record exact answer pages;
  - record the nine answer-key defects;
  - remove the duplicate count of YM Revision Exercise 6 Q2;
  - add the Goldie 2D Q6 continuation (PDF 67) and the YM PDF 111 handwriting note;
  - check whether "sketch a polynomial from its equation" is a registry gap or out of scope.
- **Then continue the completion work in `HANDOVER.md`:**
  - reconcile the 624 unclassified heading leads;
  - finish the mandatory visual, gap and thin items;
  - check the answers of every candidate design-evidence item;
  - claim a stop rule only if it is earned.

  Note the two weak gap-demand leads: Goldie PDF 190 and PDF 111.

## E. R3-06: make the build relocatable

Store repo-relative paths in `checks/r3/*-manifest.json`, and make the builders reject absolute or outside-workspace evidence paths.

## Deliverables

- Updated tools, records and registers, and a regenerated `analysis-snapshot.json`.
- `workbench/checks/repair-r4-report.md` containing:
  - a table mapping R3-01 to R3-08 to what changed, the file and the check that proves it (or "deferred" with a reason);
  - counts before and after: tables, rows, questions covered, rules, provenance pairs and textbook items;
  - the coverage limits.
- STATUS.md and HANDOVER.md updated. The next step is Claude's focused re-check of R3-01 to R3-05, then step 3.

## Checks before handing back

- The deterministic double rebuild passes **in a fresh copy of the workspace**, and all seeded negative fixtures still fail.
- **Add negative fixtures for:**
  - an award row whose alternatives are summed;
  - a question with neither a table nor a recorded absence;
  - an absolute evidence path.
- Every award table total equals its printed tariff.
- **Second-read every award row against its render**, recording the evidence image and the date. Do not mark a row checked from the text layer.
- Every new or changed provenance pair is confirmed on both rendered pages.

## Not in this round (step 3, the PLAN)

These stay deferred:

- R2-02 same-type references per branch;
- the diagram spec, including must-read givens per crop (R3-07);
- sketch-marking criteria;
- Bloom levels;
- grade bounds as parameter domains;
- shared modules;
- Cambridge variety targets.

## Constraints

- Do not commit or push; Vitalis commits.
- Do not modify:
  - any review folder;
  - source PDFs;
  - `standard/`;
  - other subjects;
  - app code;
  - pinned checkouts.
- Acquire anything only with the YYeni Web Harvester; write no new scraping scripts.
- No PLAN, recipes, generators, work orders, imports or learner assignment.
