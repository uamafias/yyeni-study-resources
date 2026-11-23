# Findings: focused check of 8227 repair round 4

Reviewer: Claude Opus 5.5 (cross-vendor, role REVIEWER). Date: 2026-11-17. Inputs are frozen in `inputs.json`: snapshot `f3b68249…dccde1`, preserved R3 parent `208a33a2…389d`, HEAD `11cd03fe`, with rounds 2–4 uncommitted. Each finding gives the locator, the evidence, the correction and the check that would close it.

**How the check was done.**
- **Integrity and rebuild:** I checked these myself.
- **Award rows:** all 821 rows were reread by five read-only agents, one per report year. Each agent read every printed table blind before opening the author's rows, then compared row by row. They worked from pages I rendered myself with PDFKit at scale 2.6, never from the author's renders or notes. I re-read every high-confidence marking difference on its crop.
- **Provenance:** the 26 confirmed pairs and 4 structural comparisons were checked by a sixth agent on both rendered pages. I ran my own rare-phrase screen of all 355 Cambridge 9709 question papers in the corpus, and confirmed its new hits on renders.
- **Rules, context scan, textbook corrections and cross-record consistency:** I checked these myself, by script and on the source pages.

## A. Round-3 findings: dispositions

| Finding | Disposition | Evidence |
|---|---|---|
| R3-01 award-table coverage | **Closed** | All 119 questions have a transcribed table. Blind row counts agree with the author for every 2021 and 2022 question; the few 2023–2025 differences are explained (a derived row, an SC cap modelled separately, one note folded into a row). The two claimed absences are confirmed: 2023 P1 Q5(a), where the commentary is on PDF 324 (printed 322), and 2024 P1 Q13(a), where the 13(b) table is printed twice. The missing final row of the 2025 P2 Q3 third-angle path is confirmed, and its derived completion of ½ is correct. The 2021 section ends on PDF 243: PDF 244 is blank and PDF 245 starts Physics. |
| R3-02 row corrections | **Closed** for all 13 named marking rows and 7 cosmetic rows | All confirmed on the renders, including the 2023 P2 Q6(a) ordinates ln1…ln9, recomputed to 11.5051. Structural fixes hold: `accepted_alternatives` never copies `condition`; SC, F.T., c.a.o., www, s.o.i. and "allow one slip" are defined; the Q7(c) degree path sits in Q7 and is excluded from pilot use. The residual row errors from the new transcription are in R4-01. |
| R3-03 convention register | **Closed** | Covered below this table. |
| R3-04 provenance | **Partly closed**; residual in R4-03 | 015 and 019 are demoted, and 009 too (justified, see R4-03). N1–N10 are added as pairs 020–029, all genuine, with correct correspondence and labels. Tariff changes are complete in every pair. The 2024 P2 Q5 defect back-link is present. Derived-from references exist exactly for the 25 confirmed questions and are all hidden; the 4 structural items carry none. |
| R3-05 textbook cautions | **Closed** | Covered below this table. |
| R3-06 relocatable build | **Closed** | A fresh copy of the workspace with no path edits passes both rebuilds and all 7 negative fixtures. Its 113 outputs are byte-identical to the delivered tree, except `rebuild-verification.json`, which records the copy's own path. The new fixtures (summed alternatives, missing coverage, absolute path) fail for the right reason. |
| R3-07 crop containment | **Deferred to step 3**, as commissioned | — |
| R3-08 textbook sample | **Named corrections closed; the finding stays open, as the author states** | Covered below this table. |

**R3-03 detail.**
- **Rule register.** All 95 rules have evidence lists. 146 of 147 evidence excerpts are verbatim in the page text layer; the remaining one ("Correct ruled V-shape", PDF 364) is in a raster table and was confirmed visually.
- **Recurring general rules.** Each is registered once and applied across years: answers-only (076: 2021 p236, 2022 p307, 2023 p330, 2024 p335); hence (006: nine evidence entries); formula-sheet variables (078); factorisation shown (079).
- **Specific rules.** All ten are added (080–089).
- **Conflicts.** 04 now has the 2025 "Correct ruled V-shape" and 05 has the 2024 PDF 338 prose. Rule 073 is clarified. Conflicts 06–09 are sound additions.
- **Context scan.** My own broader keyword scan (must, no marks, not accepted, lose/lost, condone, accept, penalised, ignore, A0/B0/M0) found 207 hits against the author's 191. The extra hits fall on three pages and are award-table text already transcribed as rows. I agree with all 21 "not marking-relevant" dispositions (pen and pencil, centre administration, teaching advice). One wording point is in R4-05.

**R3-05 detail.** I re-read every named item in the inventory:
- **The two wrong dispositions are fixed.** YM C7 Try Now 27(c) is in scope with value 1/30, and the (a) key sign error is recorded. YM C8 Exercise 8 Q7 is now a calibration caution.
- **The partly-right items are fixed:** Goldie 6B Q2 (branch, not scope), PDF 554, 122, 216, 217, 127 and Exercise 4.2 Q3.
- **The missed errors are recorded:** PDF 352 Try Now 26(c), PDF 600 (Try Now 12(b), Try Now 15), PDF 113, PDF 112, and the labels on PDF 555 and 598.
- **The rearrangement limit is now applied consistently** to Goldie 6B Q5/Q6 and YM C13 Try Now 6.
- **The QUAL01 citation is corrected.**
- **Goldie 3E Q3, 5B Q12 and 6B Q2 are "not applicable (show/prove)".**

**R3-08 detail.**
- **Named corrections, all verified in the inventory:**
  - all nine answer-key defects;
  - the four over-mappings (Goldie 4A Q2/Q8, YM Exercise 7 Q1, YM C13 Try Now 5 Q2) and four omissions;
  - the duplicate alias (YM Revision Exercise 6 Q2), plus a second duplicate the author found;
  - the Goldie 2D Q6 continuation to PDF 67;
  - the YM PDF 111 handwriting note;
  - QUAL01 on YM C8 Try Now 9 Q2(e);
  - an `exam_style` definition ("source-labelled");
  - the polynomial-sketch registry decision;
  - the fresh sample seed, which reproduces as `seed:item_id`.
- **What remains open:**
  - Exact demand-set agreement with my round-3 blind sample is unchanged at 53/99. In 29 items the author's set is narrower; most of these are the judgement differences recorded in round 3.
  - 448 of the 1,921 items in multi-item blocks still share their descriptive note with a sibling. Some notes are block-level, for example YM C6 Try Now 35 items 1–3 and YM C7 Exercise 7 Q1, whose note still says "finite definite integrals" after the definite-integral demand was correctly removed.
  - Population completeness, value-level qualifier decisions, full answer accuracy and the independent classification of the fresh sample remain open, as the author reports.

## B. New findings

### R4-01 (medium): 8 of 821 award rows still change marking; 2 of them assert a source defect that is not in the source

The full second read found 4 high-confidence and 4 medium-confidence marking differences, about 1% of rows. In round 3 the rate was 13 of 196 (6.6%).

**High confidence (I confirmed each on the crop):**
1. **2025 P1 Q7(c), row 04 (PDF 350).**
   - The print is "B1√ FT y ≤ their p".
   - The row says "F.T. y<their p (source condition prints strict inequality)".
   - The ≤ is unambiguous. There is no source defect, and the row would refuse follow-through to a correct "y ≤ their p".
2. **2025 P2 Q2, row 09, SC2 (PDF 356).**
   - The print is "SC2: Just x = 1/4 or −1/2 (Just one leg)".
   - The row says "x=1/4 or 1/2" and claims the source prints +1/2.
   - The minus sign is printed, and the second leg gives −1/2. There is no source defect.
3. **2022 P1 Q2(b), row 03 (PDF 301).**
   - The print is "M1√", the report's follow-through tick, used the same way on the same page ("B1√ F.T. their (−b, c)").
   - The row records no F.T., so a candidate who uses wrong (a) roots correctly is refused the M1.
   - The author does record √ as F.T. elsewhere, for example 2025 P1 Q7(c).
4. **2022 P2 Q1(b), row 06 (PDF 308).**
   - The print is "y = log₅(5/3) o.e. or 0.317".
   - The row keeps only "0.317", so equivalent exact forms are not accepted.

**Medium confidence (layout or allocation):**
5. **2022 P2 Q6(b)(i), rows 06–07 (PDF 313).**
   - "A1: can be awarded without M2" is printed against the 4.9° A1, and "A0 if more than 2 answers" against the 78.7° A1.
   - The rows copy both notes onto both A1s, so a candidate with extra answers would lose both A marks. The page 312 commentary says such candidates lost "an accuracy mark".
6. **2022 P2 Q4(a), row 01 (PDF 311).** "Allow one slip in manipulation for B2" covers both B1s, but the qualifier is only on row 02.
7. **2023 P2 Q1(b), row 05 (PDF 331).** "B0, M0, A0 for correct 3 brackets without any working" names the M mark, but the clause is on rows 04 and 06 only.

**Correction.**
- Fix the eight rows.
- Remove the two invented source-defect notes.
- Before recording any "source prints X" note, re-read the crop at scale ≥ 4.

**Check.** A focused re-read of these rows agrees with the print.

### R4-02 (low): schema and record-consistency defects that a step-3 builder would trip on

1. **E marks are normalised to A.**
   - 42 rows print E1 (establish a given result): 8 in 2021, 8 in 2022, 10 in 2023, 7 in 2024 and 9 in 2025.
   - These rows are stored as `mark_type: A`, and nothing in the row says the mark requires establishing a given answer.
   - DM and DB rows keep their meaning through the `dependent_award` flag (41 of 41), but E rows have no equivalent flag.
   - Keep `E` as the mark type, or add an explicit establishment flag.
2. **60 rows list the main answer itself as an "accepted alternative".** Remove these self-alternatives so that the list holds only printed alternatives.
3. **The question records are stale.** `question-analysis.json` still says "no complete award schedule verified" (198 parts) or "linked official excerpts; criterion reconciliation pending" (52 parts). Every part now links its official rows (821 of 821, all on the correct part). Regenerate the field from the register.
4. **2023 P2 Q1(c), row 08** has an empty `what_earns_it`. The roots appear only in the derived note.
5. **2025 P2 Q3, row 12.** The derived completion omits the c.a.o. carried by the final rows of the two printed paths.
6. **Source gaps and defects the agents found but the register does not flag:**
   - **2024 P2 Q4(a) (PDF 337):** "B3" with only two itemised criteria; step 3 must author the third.
   - **2022 P1 Q1(a) (PDF 301):** the scheme prints b = (x − 3/2)², but b = −3/2.
   - **2024 P2 Q7(b) (PDF 340):** the headline iterates are truncated (0.3053, 0.2891, 0.2888). The correct 4 s.f. values appear only as the "or" alternatives.
   - **2024 P1 Q11(c) (PDF 332):** a dangling "OR".
   - **2023 P2 Q9(a) (PDF 339):** a garbled "v′ = k … k ≠ (±60)".
   - **Commentary errors:** 2021 P1 Q6 (PDF 233: "AP ⟂ OP" should be OB) and 2021 P2 Q12 (PDF 242: "√18 or 2√3", and 0.123… for 1.23…).

**Check.** A schema check over the register: no E row without its flag; no self-alternatives; `marking_rule_status` derived from the linked rows.

### R4-03 (medium): provenance remains incomplete; the ranked leads were not read

1. **Lead dispositions are boilerplate.**
   - 450 of the 476 rank 1–4 lead records say "not promoted; discovery lead only… no visual confirmation recorded for this pair".
   - The commission asked for a recorded disposition, meaning a reading. These records restate that the lead was not read.
2. **Three more matches are confirmed missing.** My rare-phrase screen of all 355 9709 question papers in the corpus ranks every one of the author's confirmed pairs at or near the top. On renders it confirms three further adaptations:
   - **2023 P2 Q8 ← 9709/22/M/J/18 Q5.**
     - The same curve, y³ sin 2x + 4y = 8.
     - Cambridge asks for the tangent where the curve crosses the y-axis [6]. NSSCAS splits this into (a) show the given dy/dx and (b) hence find the gradient at the y-axis crossing.
     - This was the author's rank-2 lead (via the duplicate variant /23).
   - **2023 P2 Q1 ← 9709/21/M/J/16 Q4.**
     - The same three-part structure: find the quotient on division by (x + 2) and show the remainder; hence factorise p(x) ∓ 5 completely; write down the roots.
     - The cubic is changed, and Cambridge (iii) uses p(|x|).
     - This was not among the author's ranked leads.
   - **2025 P2 Q3 ← 9709/21/O/N/22 Q3.**
     - "It is given that sec θ = √17 where 0 < θ < ½π. Find the exact value of tan(θ + ¼π)" becomes √10 and tan(θ − ¼π).
     - This was the author's rank-1 lead. Its Cambridge mark scheme is also the natural reference for the missing third-angle row (R3-01).
   - A fourth near-hit, 2021 P1 Q5(a) "2/cos θ = 7 − 3 cos θ" against 9709/12/O/N/21 Q1 "2 cos θ = 7 − 3/cos θ", is a different equation and is chronologically implausible. I do not count it.
3. **Two further part-level sources were found by the delegated check.** I confirmed both from the paper text:
   - **2023 P2 Q3(a) ← 9709/22/F/M/20 Q1.**
     - Cambridge: "Solve 2 sin(θ + 30°) + 5 cos θ = 2 sin θ for 0° < θ < 90°" [4].
     - NSSCAS: "2 cos(θ + 30°) + 5 sin θ = 4 cos θ", same interval, [4].
     - The template is unique in the local corpus, and m20/22 is already the source of pairs 006 and 007. Pair 024 records Q3(a) as "unrelated" only relative to m18/22.
   - **2023 P2 Q5(a) ← 9709/22/M/J/19 Q3** (= /23 Q3).
     - "Find the exact coordinates of the stationary point of the curve with equation y = 3x/ln x" [5] becomes 5x/ln x.
     - The wording is identical, and s19/22 is already the source of 012 and 028.

   So **five** adaptations are missing in total, three whole-question and two part-level. Both 2023 P2 Q3 and Q5 now have parts from two different Cambridge sources.
4. **Pair-level results from the delegated check.** All 26 pairs are genuine. Every part correspondence and learner label (paper, session, year) is correct, and all five duplicate-variant leads checked are word-for-word identical. No tariff change is missing. The remaining problems are in the text fields:
   - **False or inaccurate "changed" clauses:**
     - 006: "A is at positive x = 7π/6, not a negative intercept" describes no difference.
     - 021: "NSSCAS prints alternative formula" is inaccurate; NSSCAS adds only the initial value 1.698.
   - **Material omissions:**
     - **012 (2024 P2 Q7).** NSSCAS keeps the Cambridge diagram, but with y = ¼, t ≈ 0.289 and P lies at x ≈ −2.50, left of the y-axis and below the y-intercept (≈ 0.79). The diagram draws P to the right of the axis and above the intercept; I confirmed this on the render and by computation. This is an unregistered **NSSCAS source defect** in a learner-displayable original question. The step-3 diagram rule "generate from the same instance values" already guards new items, but the source note is missing.
     - 028 (b): NSSCAS 4/tan 2x + 5 = tan x is not an equivalent rewrite of Cambridge 4 cot 2x = 5 + tan x. The quadratic changes from 3t² + 5t − 2 to 3t² − 5t − 2. Also, the radians/degrees change belongs to (a)(i), not (a)(ii).
     - 024 (b)(ii): the Cambridge "Hence find … cot(π/12)" becomes a direct evaluation of cosec(2π/3) + cot(2π/3), so the "hence" link is lost.
     - 025: the variable θ is renamed x. "Use an appropriate formula" is dropped and "Using your value of tan x in part (a)" is added.
     - 014 (c): "the nature of this stationary value" becomes "whether … a minimum or maximum value. Show all necessary working."
   - **Minor issues:**
     - 026: the domain changes from strict to inclusive.
     - 029: the diagram is redrawn.
     - 011: "shared" says sec²x, but both papers print 1/cos²x.
     - 002: worth noting that the remainder −6 survives the divisor change, since f(½) = f(−3/2) = −6.
   - **Duplicate handling:** 003 and 004 attribute the same NSSCAS question to identical variants /22 and /23 as two records with two learner labels. Elsewhere (012, 016, 025, 028) the convention is one record plus a duplicate lead. Fold 004 into 003.
   - **Structural items:**
     - The demotions of 009, 015 and 019 are justified; their templates recur in 9–10 local papers, and no values carry over.
     - **030 (2021 P1 Q6 ← 9709/13/M/J/17 Q4) is better recorded as "possible source (wording only)".** The sentence "The point P lies on AB such that AP = k·AB" occurs only in s17/13 Q4 in the local corpus. It would explain the external-division defect: Cambridge's ratio ⅓ keeps P on AB, while NSSCAS's 3/2 puts P beyond B.
     - The present record says the "on AB wording [was] retained" and then concludes "no specific source", which contradicts itself.

**Correction.**
- Add the five pairs (three whole-question, two part-level), each with both pages, part correspondence and a complete "changed" field.
- Correct the 006 and 021 clauses, and add the omissions listed for 012, 028, 024, 025 and 014.
- Register the 2024 P2 Q7 diagram as a source defect with its computed position of P. Link it to 012, and add a source note to the learner-displayable original reference.
- Fold 004 into 003 as a duplicate lead.
- Re-record 030 as a wording-only possible source, explaining the defect; keep it hidden.
- Replace the boilerplate with a real screen. A rare-phrase and value search over every page of the corpus (not only the eight ranked pages per question) is cheap. Visually dispose of every hit above a stated threshold, and record the threshold and what was read.

**Check.** The reviewer's screen finds no confirmed adaptation that is missing from the register.

### R4-04 (observation): what the marking register now supports

- The register is now fit to be the source for step-3 rubrics, once R4-01 and R4-02 are fixed. These are a short, mechanical correction, not another full transcription round.
- After that, the next focused check needs only the corrected rows and a schema check; a full second read is not needed again.
- The three derived completions, and the 2024 P2 Q4(a) third B mark, must be authored and reviewed in step 3, never used as official criteria.

### R4-05 (low): rule 076's interpretation is narrower than its evidence

The interpretation limits "No marks are awarded if only answers are given" to "the stated differentiation/integration context". But the 2024 p335 context is calculators that solve cubic equations, and the sentence stands on its own in each report.

**Correction.** Word the interpretation as "answers produced without supporting working earn no marks, the reports citing calculators that differentiate, integrate or solve cubics". Explicit B, SC and F.T. awards still govern.
