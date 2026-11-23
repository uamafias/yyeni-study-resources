# Findings: focused check of 8227 repair round 3

Reviewer: Claude Opus 5.5 (cross-vendor, role REVIEWER). Date: 2026-11-17. Inputs are frozen in `inputs.json`. Four sub-checks were delegated to read-only Claude agents. I re-checked the decisive discrepancies myself on rendered source pages; each finding says which.

Severity: **high** blocks step 3 (recipe contract and PLAN); **medium** must be fixed before the affected register is used as design evidence; **low** is a quality correction.

## A. Round-2 findings: dispositions

| Finding | Verdict | Evidence |
|---|---|---|
| R2-01 crops | **Closed** | Both re-crops show the missing givens: 2024 P1 Q9 has "B (90, −3)" and "f(x) = a sin x", and 2025 P1 Q12 has D, its label and the x-axis label. All 39 crops are clean on reviewer contact sheets. Re-run on the old R2 boxes, the containment check rejects both and names the cut labels. |
| R2-02 same-type per branch | Deferred to step 3, as commissioned | Not re-examined. |
| R2-03 demand links | **Closed** | All 13 changes are present in `directly_assessed_demand_ids`. Total links are 576, and the 7 count changes reproduce. |
| R2-04 edges | **Closed** | 2023 P2 Q6 a→d, 2025 P1 Q4 a→c and 2024 P2 Q11 a→c are present with cue records. |
| R2-05 diagram parameters | **Closed** | 55 NSSCAS and 7 Cambridge records have distinct fixed, variable and relations. The relations I recomputed are correct: r = (R−r)sin(θ/2) with R = 3r at π/3; semicircle radius R sin(θ/2); 2r + rθ = L. |
| R2-06 purpose label | **Closed** | s15:11:8-iii is now `variety`. |
| R2-07 held references | **Closed** | The 3 held parts have `learner_display: false` with reasons. The seeded fixture is rejected for the right diagnostic. |
| R2-08 provenance | **Reopened in part** | See R3-04. |
| R13-22 marking conventions | **Not closed** | See R3-01, R3-02 and R3-03. |
| R13-23 textbook inventory | Partial, as the author states | See R3-05 and R3-08. |

The integrity checks hold:

- **Snapshot.** 1,456 files, 435 sources and 10 review files match the snapshot. The R1 and R2 history snapshots are preserved.
- **Rebuild.** In a disposable copy the rebuild is byte-identical: 2 rebuilds, 99 outputs, and all 4 negative fixtures rejected. This needed the R3-06 workaround.

## B. New findings

### R3-01 (high): the award-table coverage claim is false; about 95 official award tables were not transcribed

**Claim.** `marking-conventions.json` says that only 24 questions have criterion award tables (2021 P2 Q1–4, 2023 P2 Q1–9 and 2024 P2 Q1–11). It lists the other 95 as `questions_without_award_tables`, whose later rubrics "must be labelled derived".

**What the source shows.**
- Rendered pages show printed criterion award tables (M1/A1/B1/DM1 with comments and totals) for almost every other question:
  - 2021 Paper 1 Q1–12 (PDF 231–235) and Paper 2 Q5–12 (PDF 239–243);
  - 2022 Paper 1 Q1–14 (PDF 301–306) and Paper 2 Q1–10 (PDF 308–316);
  - 2023 Paper 1 Q1–13 (PDF 321–329);
  - 2024 Paper 1 Q1–14 (PDF 325–334);
  - 2025 Paper 1 Q1–12 (PDF 346–354) and Paper 2 Q1–12 (PDF 356–364).
- Pages with no table are the general-comment pages (2021 p236, 2022 p307, 2023 p330, 2024 p335, 2025 p345 and p355) and 2023 p332 and p334.
- I confirmed tables myself on 2021 PDF 243, 2022 PDF 302 (P1 Q3–5) and 2025 PDF 358 (P2 Q4).

**Probable cause.** These tables are images with no text layer. Text-based token scanning finds M1/A1 only on the 17 pages that were transcribed.

**Range error.** The 2021 range 231–242 is also one page short: PDF 243 (printed 241) holds the 2021 P2 Q12 table.

**Shared responsibility.** My round-2 repair prompt told the author to "transcribe the 24 award tables". I passed the author's count on without checking it, so the anchoring is partly mine.

**Impact.**
- The register covers official criteria for 24 of 119 questions, when about 119 exist.
- The "derived rubric" label would be applied wrongly to about 95 questions.
- Sketch criteria, follow-through, SC caps and accepted alternatives for most of Paper 1 and 2022/2025 are missing, and the recipe contract's marking and feedback depend on them.

**Correction.**
- Transcribe every award table from rendered pages into the same row schema.
- Extend the 2021 range to PDF 243.
- Replace `questions_without_award_tables` with a per-question coverage table recording table present (with PDF page) or absent (with reason).
- Re-run tariff reconciliation for all questions.

**Check.** Every one of the 119 questions has either a transcribed table that reconciles with its tariff, or a recorded absence that a rendered page confirms.

### R3-02 (medium): 13 of the 196 transcribed rows change marking

Delegated check of all 196 rows against scale-3 renders: 176 match, 13 discrepancies change marking and 7 are cosmetic. All locators and all tariffs are correct.

**Rows that change marking:**

1. **2023 P2 Q6(a), row 02 (PDF 337).** Ordinates are listed as ln3, ln5, ln7, ln9, ln11. For ∫₃¹¹ ln(x−2) dx with h = 2 they are ln1, ln3, ln5, ln7, ln9, and the report prose says "use ln 1, ln 3, ln 5 etc". The author's ordinates give 15.00 instead of 11.5. I confirmed this on the render and by computation.
2. **2023 P2 Q3(b)(ii), row 13 (PDF 333).** The added condition "use the identity from preceding part" is not printed. There is no "hence", and direct substitution of 2π/3 earns the M1.
3. **2023 P2 Q3(b)(iii), row 15 (PDF 333).** The B1 is printed for rewriting to cot 2x via the (b)(i) identity. Reaching cos 2x belongs to the M1.
4. **2023 P2 Q2, rows 01–03 (PDF 331).** The "www" (without wrong working) qualifier is dropped from a = −2, b = −3 and c = 2.
5. **2023 P2 Q4(b), row 16, logs path (PDF 335).** The printed "Accept y = (log 8/log 3)x seen without stating k" is missing.
6. **2023 P2 Q4(c), row 18 (PDF 335).** "Both solutions" belongs to the A1, but the row attaches it to the DM1.
7. **2024 P2 Q2, row 03 (PDF 336).** "Equation in tan θ or cot θ" is transcribed as "tan θ or θ".
8. **2024 P2 Q2, row 04 (PDF 336).** The first A1 is printed against tan θ = 4 − √3. An added "two-quadrant inverse solutions" requirement is not printed.
9. **2024 P2 Q3, row 04 (PDF 337).** The M1/A1 pair is printed beside the critical values x = 6, −2, but the row moves the A1 to the final single inequality. Confidence is medium (layout).
10. **2024 P2 Q6(b), row 13 (PDF 339).** The source M1 is for integrating "their expanded brackets", an implicit follow-through. The row requires the correct three terms.
11. **2024 P2 Q8(b), row 08, exponential path (PDF 341).** "A0 if decimals also seen" is printed only on the logs path.

**Cosmetic (7 rows):**
- 2021 P2 Q1(b) row 05 has an unprinted dependency.
- 2021 P2 Q1(b) row 07 and 2023 P2 Q1(c) row 07 fill in root values that are blank in the source. The values are correct, so mark them derived.
- In 2023 P2 Q6(b) row 04 the primary and alternative are swapped.
- 2024 P2 Q5 row 02 attaches "all necessary detail" to the A1 instead of the E1.
- 2024 P2 Q11(b) rows 03–04 omit the decimal alternatives 1.25a and 0.6875a.

**Structural defects:**
- In all 196 rows `accepted_alternatives` is a copy of `condition`, so printed "or" and "o.e." alternatives are not captured.
- `mark_type_normalisation` does not define SC, F.T., c.a.o., www or s.o.i.
- The owner exclusion of the 2023 Q7(c) degree path is stored in the `special_cases` of 2023 P2 Q6.

**Correction.**
- Fix the 13 rows and the cosmetic rows.
- Make `accepted_alternatives` a list of printed alternatives, separate from conditions.
- Add the missing qualifier codes to the normalisation.
- Move the Q7(c) note to Q7.

Apply the same row discipline to the R3-01 transcription.

**Check.** A second-reader comparison of every row against its render, as in this review, finds no marking-changing differences.

### R3-03 (medium): the convention register omits recurring general rules and several question-specific rules; general rules are scoped to one year

**Verified.** All 75 excerpts appear verbatim on the cited pages, and most interpretations are faithful. The completeness gaps below come from my own keyword scan of the five report ranges, read in context.

**1. Recurring general rules are recorded once, or never.** Each report repeats the same "general comments" paragraph, but `applies_to` scopes each rule to its own report year. As a result:

- "No marks are awarded if only answers are given" (2021 p236, 2022 p307, 2023 p330, 2024 p335) is never registered verbatim. Rule 014 softens it to "not an automatic zero for all answer-only B criteria" without quoting it or recording its calculator context.
- "If the question states 'hence' and the previous question is not used, no marks may be awarded" (2021 p236, 2023 p330, 2024 p335, 2025 p355) is registered for 2021 only (rule 006).
- "The variables used on the formula sheet must be replaced" (2023 p330, 2024 p335) is registered for 2022 only (rule 019).
- "The factorisation or substitution into the quadratic formula must be shown at all times" (2024 p335) is not registered.

So 2022–2025 parts carry no "hence" or answer-only rule at all.

**2. Question-specific answer-format, sketch and precision rules are missing:**
- y must be replaced by f⁻¹(x) to score full marks (2022 p315);
- a coordinate answer is not accepted where vector form is required (2024 p331);
- "and" versus "or" in inequality answers; using "or" lost accuracy (2025 p346);
- a sketch drawn outside the domain is not accepted (2025 p347);
- if decimals are used, keep at least 4 d.p. (2023 p337);
- both graphs unlabelled loses all marks (2023 p337);
- a factor written as x + 3/2 for 2x + 3 gets no marks (2024 p337);
- an exact k is required, and a decimal loses the final A (2023 p334);
- two solutions instead of one lose the accuracy mark (2021 p239);
- the first two iteration values written were marked (2021 p240).

**3. Two conflicts are incomplete:**
- MC-CONFLICT-04 misses the 2025 P2 Q12(a) award table's "Correct ruled V-shape" (PDF 364), which is the direct contrast to 2024's "straight by eye".
- MC-CONFLICT-05 misses the 2024 prose on PDF 338 requiring boundary substitution to be shown.

**4. Rule 073 is ambiguous.** It reads "more accurate values are accepted", but the source says that candidates who showed more decimals *before rounding* were not penalised.

**Correction.**
- Register each general rule once, with an evidence list of every year and page where it appears, and apply it across years unless a criterion row overrides it.
- Add the missing question-specific rules and complete conflicts 04 and 05.
- Many prose rules will also appear in the R3-01 tables; link rule to row where they coincide.

**Check.** A keyword-and-context scan of all report pages for "must", "no marks", "not accepted", "lose/lost", "condone" and "accept" finds no marking-relevant statement left unregistered and unlinked.

### R3-04 (medium): provenance has 2 unsupported matches, 10 missed matches and incomplete "changed" fields

**What checked out.** The delegated check rendered every pair on both sides:
- all 19 are the same question, with correct part maps, locators, draft labels and hashes;
- all 39 derived-from references are hidden and identical in `question-analysis.json`;
- 2023 P2 Q5(a) is correctly not linked.

**Unsupported (remove the derived-from attribution):**
- **015, 2025 P2 Q1 ← 9709/21 O/N 2023 Q5(a).** Only the factor (x + 2) and the [5] tariff are shared. NSSCAS has 2x³+ax²+bx+6 with remainder −6 on division by x−1; Cambridge has 6x³+ax²+bx−20 with remainder −11 on division by x+1. I confirmed this by text. The same template appears in at least 7 other P2 papers, 2017–2024. Classify it as structurally similar with no source.
- **019, 2021 P2 Q2 ← 9709/22 O/N 2018 Q6(a).** This is a recurring "∫ k/(linear) dx = ln N" template. 9709/21 (and /23) O/N 2018 Q2, ∫₁⁷ 6/(2x+1) dx = ln 125, is closer. Classify it as structurally similar.

**Missed and visually confirmed.** All of these predate the NSSCAS paper. N1, N2, N4 and N6–N9 were ranked 1–4 in the author's own `provenance-search-leads.json` but were never promoted.

| # | NSSCAS | Cambridge | Changes |
|---|---|---|---|
| N1 | 2025 P2 Q6(a)(b) | 9709/22 F/M 2022 Q3 | y = 3^{2a}a^x; ln y → log₃ y; values |
| N2 | 2025 P2 Q12(a)–(d) | 9709/21 M/J 2022 Q5 | \|5−2x\| = 3 ln x; larger → smaller root; start value added |
| N3 | 2022 P2 Q4(a)(b) | 9709/21 M/J 2015 Q4 | (x+2) → (x+3); remainder −18 → 6; greatest → smallest (I confirmed by text) |
| N4 | 2022 P2 Q7, (a) ← (i) and (b) ← (iii) | 9709/22 F/M 2018 Q6 | (ii) dropped |
| N5 | 2023 P2 Q3(b)(i)–(iii) | 9709/22 F/M 2018 Q6 | cot(π/12) → cosec(2π/3)+cot(2π/3); (a) not linked |
| N6 | 2024 P2 Q9 | 9709/22 (=/23) M/J 2015 Q3 | degrees → radians; +3 tan → −3 tan; 135° → 3π/4 (I confirmed by text) |
| N7 | 2024 P2 Q2 | 9709/21 M/J 2021 Q2 | θ+30° → θ+60°; cosec → sec; tariff 6 → 5 |
| N8 | 2023 P2 Q4(a) | 9709/22 F/M 2019 Q3 | Ae^{px+p}; points changed |
| N9 | 2021 P2 Q12 | 9709/22 (=/23) M/J 2019 Q7 | R-form changed; equation changed |
| N10 | 2022 P1 Q11 stem + (a) | 9709/12 O/N 2017 Q9 | trapezium vectors; 3× → 2×; (b) new |

Unrendered lead worth following: 2021 P1 Q6 ← 9709/13 M/J 2017 Q4 ("P lies on AB … AP = ⅓AB"). This may explain SRC-8227-EXTERNAL-DIVISION-2021-P1-Q6.

**Incomplete "changed" fields (tariff changes are omitted throughout):**
- 003/004: Cambridge (iii) gives no formula or start value. NSSCAS adds both, and the tariffs move 2→3 and 3→2.
- 006: NSSCAS (c) adds the "2 sin²x in terms of cos 2x" hint and drops "exact"; the (b) tariff goes 3→5; A is not a negative intercept (x = 7π/6).
- 009: no value is shared. It is the closest found but should be classed "structurally similar" (a judgement call); tariffs (a) 1→2 and (b) 4→3.
- 001: a sentence is dropped.
- 008: the (a) tariff goes 4→5, and the NSSCAS (b) "were" typo is unrecorded.
- 011: a curve label is added.
- 012: t₁ → t₀, and "by using your answer in (b)" is added.
- 013: pre-drawn axes and "in terms of a" are added.
- 014: a prism diagram is added, and the (a) tariff goes 3→4.

**Schema and consistency:**
- Duplicate Cambridge variants are recorded only for 003/004. They are missing for 012 (9709/23 M/J 2019), 016 (9709/21 O/N 2022) and 015 (9709/23 O/N 2023).
- `explains_source_defect` is null in most matches but "None established" in 003/004.
- SRC-8227-POLYNOMIAL-NAME-2024-P2-Q5 does not link back to match 002.

**Correction.** Demote 015 and 019, add N1–N10, complete the "changed" fields including tariffs, record duplicate variants consistently, normalise the null value and add the defect back-links.

**Check.** A second-reader pass over the pairs agrees with each confidence label, and every pair ranked 1–4 in the leads file has a recorded disposition.

### R3-05 (medium): textbook caution/defect set: 2 wrong, 8 partly right, and errors missed on inspected pages

The delegated check covered all 33 caution and defect items: 23 are confirmed, 8 are partly right and 2 are wrong.

**Wrong:**
- **YM C7 Try Now 27(c), PDF 352.** The upper limit is ∞, the same glyph as in (b); it is not 1, and the integral does not cross x = 2.5. The value is 1/30, matching the YM answer on PDF 628. I confirmed this on the render. The "partial scope" disposition should be in-scope. The (a) answer "→ −∞" is itself a printed error: √(6−x) > 0, so it diverges to +∞.
- **YM C8 Exercise 8 Q7, PDF 401.** It is marked out of scope under LIMIT05. LIMIT05 bounds the division objective; this item assesses the remainder theorem, with f(−½) = 3 matching the key. At most it needs a calibration caution.

**Partly right:**
- **Goldie 6B Q2.** The mathematics is right: forms (iii)–(iv) cannot reach the negative root. But form (iv) is a square root of a quotient, not a fourth root, and this is a branch qualification, not syllabus scope.
- **PDF 554.** It also has sin 2θ printed as 2 sin θ sin θ, and cos 2(½θ) for cos 2(½π).
- **PDF 122.** Domain x ≠ 3 should be x ≠ −3.
- **PDF 216.** cos⁻¹(√3/2) = 150° should be cos⁻¹(−√3/2).
- **PDF 217.** The printed argument is −1/√2, not 1/√2, and a typo in a worked line does not make the item partial-scope.
- **Exercise 4.2 Q3.** The retained-part note misdescribes part (a).
- **PDF 127.** There is no source defect, and QUAL01 (integer coefficients in modulus graphs) is cited wrongly.

**Errors on pages not flagged:**
- PDF 352 Try Now 26(c): lower limit ∞ should be −∞.
- PDF 600: Try Now 12(b) answer domain and range; Try Now 15 range given in x.
- PDF 113: x + 3 for x − 3.
- PDF 112: range treated as codomain.
- PDF 154: 2π printed as 6.28318537….
- Two label slips (PDF 555, PDF 598).

**Inconsistent limit.** Goldie 6B Q5(iii)–(iv) and Q6(ii) (PDF 171) require a learner-built rearrangement but are marked in-scope, while YM Try Now 6 is marked partial for the same reason.

**What held:**
- the seven named checks (with the PDF 217 wording correction);
- the six Goldie section exclusions (chapter 8 slightly over-broad; immaterial);
- the two gap demands, for numbered items. There are weak leads at Goldie PDF 190 (an unnumbered identity-versus-equality prompt with a printed answer, in an excluded section) and PDF 111 (degrees and the y = x tangent).
- the three Goldie answer gaps. These are show/prove items, so record "not applicable" rather than "unknown".

**Correction.**
- Fix the 2 wrong and 8 partly-right dispositions.
- Add the missed printed errors to item defects.
- Apply the rearrangement limit consistently.
- Correct the QUAL01 citation.

**Check.** A re-read of the corrected items agrees.

### R3-06 (low): the rebuild cannot be relocated

`checks/r3/goldie-render-manifest.json` (18), `provenance-render-manifest.json` (19) and `ym-revision-render-manifest.json` (13) store absolute paths to the author's machine. `build_textbook_progress.py` accepts absolute paths, so any copy of the workspace fails the rebuild (it failed in this review until the paths were re-pointed in the copy).

**Correction.** Store repo-relative paths, and make the builders assert that evidence paths are relative and inside the workspace.

**Check.** A rebuild in a fresh copy passes without edits.

### R3-07 (observation): what the containment check can and cannot catch

`check_crop_containment.py` tests only elements that intersect the crop box. A label lying wholly outside the box, or raster content, would not be flagged. It does catch both R2 defects (verified). Visual inspection remains the gate.

The step-3 diagram spec should name each crop's must-read givens, so that a check can assert that each one is inside its crop.

## C. Textbook classification sample

### R3-08 (medium): blind 10% sample; locators reliable, demand mapping range-based, answer keys unverified

**Method.** The reviewer drew its own sample: seed `opus-5-5-r3-reviewer-2026-11-17`, ascending sha256(seed|item_id), 101 items. Nine overlap with the author-prepared sample, whose selection reproduces with `seed:item_id`. A delegated agent classified the items blind and saved its results before opening any author record. One item (YM C1 Example 24) was accidentally exposed to author demand lists, so its demand comparison is excluded.

**Field agreement (n = 101):**

| Field | Agreement |
|---|---|
| Locator | 101 |
| Printed page | 101 |
| Continuation pages | 100 |
| Representation | 100 |
| Sketch response | 100 |
| Scope | 100 |
| Answer available | 101 |

Disagreements:
- **Continuation.** Goldie 2D Q6 parts (iii)–(iv) continue on PDF 67, which is not recorded.
- **Scope.** YM C8 Try Now 9 Q2(e), y = −⅓|x| + 2, is outside QUAL01, but no item considers QUAL01–11.

**Demand links.**
- 210 of the author's 229 links are confirmed (91.7%), and 99 of 101 items share at least one link, but exact set agreement is only 53/101.
- Of the 81 differing links, there are 4 author over-mappings, 6 author omissions and 7 reviewer errors (conceded on re-check). The other 64 are judgement differences, mostly component skills.
- Over-mappings:
  - Goldie 4A Q2 and Q8: implicit/parametric D03 attached to explicit products and quotients;
  - YM Exercise 7 Q1: definite integral on indefinite-only items;
  - YM Try Now 5 Q2: derive-a-rearrangement where the iteration is given.
- Omissions:
  - Goldie 1B Q17: division quotient;
  - Goldie 3C Q6: two demands;
  - YM Try Now 55 Q3: range;
  - YM Try Now 15 Q2: chain rule, linked on the identical Revision Exercise 6 Q2.

**Systematic causes.**
- **Range-level assignment.** Demands and notes are assigned to item ranges in `textbook_inventory_inputs.py` (e.g. `1B|1-6`), which produces the over-mappings and range-wide notes.
- **Inconsistent splits.** M2:T4:O03:D03 is misapplied, and the M2:T2:O01/O02 (logs versus eˣ/ln) boundary is split inconsistently.
- **Duplicates.** YM Revision Exercise 6 Q2 duplicates Try Now 15 Q2 and is counted twice.
- **Possible registry gap.** No demand covers sketching a polynomial from its equation. Check this against the syllabus: it is either a registry gap or out of scope.

**`exam_style` is undefined.** The author's de facto rule is "past-paper attribution (Goldie) or a YM exam-style section". A connected-multipart reading gives 35 more true values. Define the field and apply it consistently.

**Answer keys: 9 of 101 are defective, and none is recorded.**

Wrong values:
- **Goldie 5C Q2(i) (PDF 346):** key 3.1349; the four-strip trapezium gives 3.131176.
- **YM Exercise 1 Q12 (PDF 591):** key "y = 1 or ½" for y⁶ − 9y³ + 8 = 0; the correct answer is 1 or 2. I confirmed this on PDF 47 and PDF 591.
- **YM C3 Try Now 12(b) (PDF 600):** domain and range wrong.
- **YM C8 Try Now 12(f) (PDF 634):** key "x < −1"; the inequality holds for all real x.
- **YM Exercise 6 Q3(b) and Try Now 35 Q1(b) (PDF 623–624):** answers swapped.
- **YM Try Now 42 Q1 (PDF 649):** key says maximum, but d²y/dx² = 2/9 > 0, so it is a minimum (the key omits the dt/dx factor).

Incomplete:
- **Goldie 3B Q4(iii) (PDF 340):** θ = 90° is missing.

Label errors:
- **YM Exercise 4.2 Q5(a) (PDF 614):** "3 cos θ" for cos 3θ.
- **YM Try Now 2 Q1(a) (PDF 653):** eˣ for e²ˣ.

Answer page locators are a two-page section span in 44/101 items; give the exact page.

**Not recorded anywhere.** YM PDF 111 carries handwritten answers by a previous owner.

**Correction.**
- Replace range-level demand and note assignment with item-level records, at least for multi-type ranges. Fix the listed over-mappings and omissions.
- Apply QUAL01–11 in scope checks.
- Define `exam_style`.
- Record exact answer pages, and check the answer of every item before it is used as design evidence. Record the nine key defects.
- Remove the duplicate count, add the Goldie 2D Q6 continuation, and record the PDF 111 handwriting.
- Because the range-level cause is systematic, the method's rule applies: after the item-level fix, draw a fresh seeded sample (a new seed, not this one) for the next check.

**Check.** On a fresh blind sample, exact demand-set agreement is clearly higher, and differences are judgement-level only. No unrecorded answer-key defect is found among the recomputed items.
