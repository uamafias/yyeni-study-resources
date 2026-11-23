# Findings: independent check of 8227 repair round 5

Reviewer: Claude Opus 5.5 (cross-vendor, role REVIEWER). Date: 2026-11-21. Inputs: `inputs.json` (snapshot `03cde4e4…022d`, preserved R4 snapshot `f3b68249…ccde1`, HEAD `11cd03fe`, rounds 2–5 uncommitted).

## How this check was done

- **Rebuild.** I rebuilt in my own fresh copy outside the repository. I did not run `verify_relocated_r5.py`, because it writes its results back into the author tree.
- **Part 1.** I checked it myself, by script and on source pages.
- **Textbooks.** I drew my own sample with seed `opus-5-5-r5-reviewer-2026-11-21`: ascending sha256(seed|item_id) within each book × figure/non-figure stratum, taking the first 10% of each stratum. That gave 396 records: 61 Goldie items, 35 Goldie figures, 158 YM items and 142 YM figures. No author-selected sample was used.
- **Delegated checks.** Eight read-only agents worked from my renders and packets:
  - five classified the 396 records blind, without access to any author textbook record;
  - two recomputed 105 answers blind;
  - one re-read 51 census pages blind.

  A ninth agent traced 20 families and 6 insight sections against their cited pages. That check was not blind, by design.
- **My own verification.** I confirmed every finding below on the source, by computation or render, except where it is marked as resting on an agent's reading.

## A. Round-4 findings: dispositions

| Finding | Disposition | Evidence |
|---|---|---|
| R4-01, the 8 award rows | **Closed** | All 8 rows read as commissioned. The two invented misprint notes are gone: no "strict inequality" or "+½" claim remains in the marking files. Repair records cite detail crops (`award-repairs-r5.json`, `checks/r5/award-*`). |
| R4-02, schema and records | **Closed** | All 42 E rows keep `establishes_given_result: true`, and E is defined in `mark_type_normalisation`. There are 0 self-alternatives and 0 empty earns fields. `marking_rule_status` is regenerated (247 official complete, 3 official with derived completion, 0 inconsistent with their rows). Row 08 is filled, and row 12 carries c.a.o. All seven report gaps are registered (`SRC-8227-REPORT-*`). |
| R4-03, provenance | **Closed except one part-level pair (R5-06)** | Five pairs were added as requested (031–035). A sixth genuine pair was found by the author: 036, 2023 P2 Q6 ← 9709/22/F/M/18 Q3, which I confirmed from the text. The "changed" fields are corrected. The 2024 P2 Q7 diagram defect is registered with the computed position of P, linked to 012, and carries a learner source note. 004 is folded into 003, and 030 is re-recorded as wording-only. The screen covers the same 214 pure-paper files as mine, and all 158 candidates were read. |
| R4-04 | Observation; still holds | — |
| R4-05, rule 076 | **Closed** | The interpretation now names differentiating, integrating and cubic-solving calculators, and keeps explicit B, SC and F.T. authority. |
| R3-08, textbook completion | **Population, records, qualifiers and answers accepted (section B). The exam comparison is returned (R5-01, R5-02).** | — |

## B. Textbook completion (T1–T6): what the independent checks found

**T1, the census: accepted.**
- On 45 randomly drawn envelope pages, my blind re-read found no posed question, worked example, Try Now, activity, investigation or continuation missing from the author's census.
- The 6 boundary pages are correctly outside the envelope: Goldie PDF 14 and YM 11 are front matter, Goldie 333 and YM 588/590 are answers, and YM 586 is a tribute page. YM 139 is correctly a duplicate scan.
- The only differences are in figure granularity. The author groups some multi-panel figures (YM 111, 112) and splits summary boxes into separate records (12 "key point" records on Goldie 133). See R5-04.

**T2, item records: accepted with a recorded limitation (R5-03).**
- Start pages agree 396/396, continuations 394/396 and record kinds 376/396.
- Exam-style flags agree on 213 of 219 items, and scope status on 212 of 219.
- In every disagreement the author's reading is defensible. The reviewer missed the YM §4.3 Exam-Style heading on Example 58, and the scope differences are prior-knowledge judgement calls on radical and index equations.

**T3, value-level qualifiers: accepted.**
- In the 126 sampled items where either side applied a limit, there is no case of one side saying "within" and the other "outside".
- Every difference is one side recording an applicability note that the other omitted, most often QUAL10 (rational powers) or LIMIT04/07.
- The divergent integral in YM C7 Try Now 14(e) is handled as in-scope-parts-only by the author and as QUAL04-outside by the reviewer: the same substance.

**T4, answers: accepted.**
- 105 items were checked: 70 random and 35 targeted at wrong, incomplete or missing keys, sketches and proofs, plus the x^x exception. That is 270 reviewer subparts, each derived before the key was read.
- The reviewer found key defects in 21 items, and the author had already recorded 19.
- The two the author did not record are minor:
  - Goldie 2C Q7(ii): A = 400 against a least-squares 380. This is within the book's by-eye tolerance, so arguably not a defect.
  - YM C2 Example 7(b): a working line prints "13 − 2(−3)" for 13 + 2(−3), though the final terms are correct.
- The author recorded 9 further defects that the reviewer had passed. I recomputed one: YM Revision Exercise 11 Q5, where the key's second derivative is 2/5 but the correct value is 4/25. The author is right.
- Answer pages are exact for 103 of 105 items. The two misses are both at page breaks (R5-05).

**T5, families and insights: returned.** The textbook-side claims largely hold: of 36 cited claims traced to their pages, 24 are supported, 10 partly supported and 2 unsupported or uncited. The comparison with the examinations is unreliable (R5-01), and family membership and demand claims need tightening (R5-02).

**T6, declaration: accepted.**
- All 3,940 records are "author-complete; awaiting independent check", and all have `learner_display: false`.
- The author-seeded sample file is retired.

**Rebuild: passed.**
- Two builds of 273 commands each produced 143 byte-identical outputs, and all 38 seeded negatives were rejected.
- My outputs match the author checkout file for file. My 143 = the author's 141 plus the two completion declarations, which also match.

## C. New findings

### R5-01 (medium): the textbook-to-examination comparison is unreliable, and it is the part step 3 needs most

Vitalis held step 3 back so the textbook findings would inform planning. The most useful finding for a planner is which textbook families practise exactly what the exams ask, which vary it, and which have no exam counterpart. That comparison does not hold up.

**1. No family is ever "same type".**
- All 219 exam-linked families are labelled "structural branch". The relation is applied at family level and never recorded at member or part level.
- In 6 of the 7 sampled exam-linked families, a member is the same type as a cited or obvious exam part, differing only in values:
  - **polynomial-factor-solve:** YM C8 Try Now 25 Q3 (PDF 400) against 2023 P2 Q1 (divide, show the remainder, hence factorise and solve).
  - **log-derivative-division-integral-chain:** Goldie 5A Q6(ii) (PDF 141), "show ∫ 1/(2x+3) dx = ln 3", against 2021 P2 Q2, "prove ∫₁⁴ 8/(2x+1) dx = ln 81".
  - **modulus-variable-rhs-equation:** YM C8 Try Now 6(f) (PDF 381), |2x+7| = 3x with a rejected root, against 2025 P2 Q2, which reduces to |1−x| = 3x with x = −½ rejected.
  - **numerical-supplied-map-chain** and **secant-identity-integral:** same pattern (`check.json`).

**2. "Textbook-only" is wrong for many families.**
- For 94 of the 161 textbook-only families, every assessed demand is directly assessed by at least one exam part in the author's own `question-analysis.json`. Not all 94 will be the same type, but the label "no exam evidence" cannot stand without a reading.
- Confirmed contradiction: **modulus-quartic-root-count** (YM Revision 8 Q3, PDF 405: "by sketching a suitable pair of graphs, show |3x| = 16 − x⁴ has two real roots") against 2025 P2 Q12(a) ("by sketching y = |5 − 2x| and y = 3 ln x … show … exactly two roots").

**3. Mislinks.**
- **elementary-exponential-primitives** is linked only to 2021 P2 Q2, which contains no exponential (∫ 8/(2x+1) dx).
  - Its real counterpart, 2021 P2 Q9(a), ∫ (4 − 2e³ˣ)/e³ˣ dx, is not linked to it.
  - That part is instead linked to two families it does not fit.
- **mixed-retained-definite-integrals** copies its exam reason word for word from log-derivative-division-integral-chain, and the reason does not describe its member (Goldie 8H Q2).

**4. Insight sections.**
- Eight sections say "Examination parts: none claimed". Six of them cover demands that `question-analysis.json` links directly to exam parts:

  | Section | Exam parts |
  |---|---|
  | Basic and transformed trig graphs | 7 |
  | Exact special angles and connected geometry | 10 |
  | Principal inverse values | 1 (the held 2023 P1 Q9) |
  | Basic-identity proof structures | 3: 2021 P1 Q5(b), 2023 P1 Q8(a), 2025 P1 Q6(a) |
  | Transform equations and enumerate complete bounded solutions | 14 or more; trig equations appear on every paper |
  | Magnitude, unit vectors and sign of parallel direction | 4 |

- "Basic-identity proof structures" instead discusses 2023 P1 Q1(b), which is a discriminant question.
- Other exam anchors are weak. Stationary classification cites 2021 P1 Q11(a), which asks only for coordinates, and omits the parts that classify: 2022 P1 Q8(b), 2024 P2 Q10(b) and 2025 P1 Q9(c).

**5. Figures (T1.3).** 1,733 of 1,758 figure records still say the examination-representation comparison is "pending". The commission asked, for each teaching figure, whether the NSSCAS exams use that representation.

**Why it matters.**
- Owner decision N1 requires "same type as" references for every part, family and recipe.
- The planner needs to know where textbook practice matches exam demand and where it adds variety.
- As recorded, the comparison would tell step 3 that whole topics, including bounded trig equations and identity proofs, have no exam counterpart.

**Correction.** See `REPAIR-PROMPT.md` §A. In outline:
- Compute exam-part candidates from demand overlap for every member.
- Read each candidate and record a member-level relation: same type, structural branch (naming the differing decision) or no counterpart (with the demands searched).
- Rebuild the family and insight summaries from those records.
- Fill or re-home the figure comparison.

### R5-02 (low–medium): some families are topic-led, and some demand claims hold only for the union of members

Of the 20 sampled families:
- **Membership.**
  - 14 share their structure genuinely or are valid single-member families.
  - 6 are topic-led or contain a member that does not fit:
    - polynomial-factor-solve includes Goldie 11B Q9 (PDF 304), the reverse task in the complex-numbers chapter;
    - secant-identity-integral includes Goldie 5B Q9(i) and 5B Q10(i), which make no identity choice;
    - parametric-point-plot-support includes Example 4.21, an elimination with no plot;
    - natural-log-exponential-values joins three different responses;
    - mixed-retained-definite-integrals is a mixed revision set.
- **Assessed demands.** These hold for every member in only 9 families. Six claim demands that only some members assess. Example: numerical-supplied-map-chain claims "derive or verify the rearrangement" for Goldie 6B Q1, 6B Q3 and YM Exercise 13 Q1, and for Try Now 11, none of which ask for it.
- **Distinction basis.** Three are scope or process notes, not learner-decision differences.
- **Difficulty progression.** Seven restate a single item; there are 70 single-member families in total.
- **Boilerplate.**
  - `units_and_precision` has 12 distinct values across 380 families, and one string is shared by 128.
  - `membership_reason` has 12 distinct values across 2,338 memberships, and one is shared by 661.
  - 85 of the 219 exam reasons end in the same disclaimer.

**Correction.**
- Every member must assess each of its family's assessed demands. Otherwise, record a part-level membership or move the member.
- Split topic-led families.
- Make the units/precision and membership reasons specific.
- Give a difficulty progression only for families with more than one member.

### R5-03 (limitation, not a repair): demand mapping is precise but its direct/component split is not reproducible

On 219 sampled items:
- **Exact assessed-set agreement is 58%** (Goldie 48%, YM 61%), against 54% in round 3.
- **The author's links are precise:** 94.8% of the author's assessed links appear in the reviewer's assessed or component set.
- **The author's links are somewhat under-inclusive:** 13.5% of the reviewer's assessed links appear nowhere in the author's record.

Of the 148 differing links:
- **73** are the same demand placed on opposite sides of the direct/component line (42 one way, 31 the other). This is a judgement call, not a bias.
- **68** are links one side omits altogether: 50 the reviewer adds, 18 the author adds. They are concentrated in overlapping registry demands:
  - M2:T3:O02:D05 ("use identities … equations") against the specific identity demands D01–D04;
  - M1:T8:O03:D01 ("find tangent or normal") against M2:T4:O03:D03 ("use an implicit or parametric derivative in a geometric demand");
  - M1:T4:O02:D01 (graph intersections) against linearisation and stationary demands.
- **7** are sibling demands within the same objective.

**Decision.** Another relabelling round would not fix this, because the registry itself overlaps. I accept the mapping with this limitation:
- In step 3, "textbook support for demand X" should use the union of assessed and component links.
- Support counts are lower bounds.
- The recipe contract must resolve the overlapping demand pairs above when it allocates criteria.

### R5-04 (low): figure records — stale statuses, unchecked content, and text callouts counted as figures

- **Stale statuses.** 1,444 figure records still say "pending actual-value screening".
- **Unchecked content.** 1,363 of 1,758 have no mathematical feature checks, and only 77 carry any registered defect. In my sample, 14 of 177 figure records (about 8%) contain a printed error that is not registered. The clearest:

  | Book | Figure | Error |
  |---|---|---|
  | Goldie | Figure 6.10 (C6 Worked illustration 7, PDF 170) | x₁ and x₂ labels swapped |
  | YM | C4 TF 83 | the 90°–180° quadrant is labelled "Quadrant 3" |
  | YM | C7 TF 60 | the x < 0 infinity rules have the wrong signs |
  | YM | C11 TF 36 | ln x² = 2 ln x without x > 0 |
  | YM | C10 TF 105 | the cos(θ+α) alternative for the R-form extrema is mis-stated |
  | YM | C13 TF 54 | "both gradients negative → staircase" cannot occur against y = x |
  | YM | C12 TF 121 | "concave" for an upward-bending curve |
  | YM | C9 TF 58 | duplicated legend name |
  | YM | C9 TF 122 | the summary header "a > 0" should read a > 1; it is noted on the record but not registered |

- **Text callouts.** About 29% of the sampled figure records are text callouts (formula boxes, REMEMBER boxes, margin notes, key-point lists), not graphics. The reviewer read 51 author "table" figures as text.
- **Roles.** Given/teaching roles disagree in 9 of 177.

**Correction.**
- Add a field that separates graphic figures from text callouts.
- Retire the stale statuses.
- Register the listed errors.
- Mark figures without content checks as "not design evidence until checked". Figures are cited as evidence in only 5 places in the insights, so a full figure-content audit is not required now.

### R5-05 (low): record hygiene

- **Notes without spaces.** 634 of 3,940 notes have lost their spaces (e.g. "For0°≤α≤360°,decidewhen secα,cosecα,cotαareallpositive"). They are unreadable for a planner.
- **Answer pages at page breaks.** Two of 105 sampled answer pages are wrong, both where the answer falls just past a break:
  - Goldie 5B Q11(ii): the key is on PDF 346 (printed 332), not 345;
  - YM C3 Try Now 4 Q3: the key is on PDF 599, not 598.
- **Unregistered printed slips in non-figure items:**
  - YM C2 Example 7(b) working line;
  - YM C2 Example 25, where Σ3n + 2 is printed without brackets.

### R5-06 (low): provenance — one part-level pair missing, and the screen's recall is unmeasured

**The missing pair.**
- **NSSCAS 2023 P2 Q4(b)** [3]: "Given that 3ʸ = 2³ˣ, use logarithms to show that y = kx and find the exact value of k."
- **9709/22/M/J/20 Q1** (= /23 Q1) [3]: "Given that 2ʸ = 9³ˣ, use logarithms to show that y = kx and find the value of k correct to 3 significant figures."
- I confirmed both on renders.
- The only other local occurrence of this wording is 9709/21/M/J/17 Q1 (5ˣ = 3⁴ʸ, y = mx), which is a weaker match.
- Pair 027 covers only Q4(a), so 2023 P2 Q4 now draws on two Cambridge sources.
- My own round-4 screen had ranked this pair, but I did not confirm it then.

**Screen recall.**
- Only 16 of the 31 confirmed pairs appear among the 158 candidates of the author's screen. The threshold (an 8-word phrase, or a 5-word phrase plus two rare values) suits near-verbatim copies but misses adapted ones.
- My part-level rare-4-gram screen of all 214 pure-paper files found no further specific source. The remaining high scorers are recurring templates: 3D-vector setups, "the point C is such that AB = BC", and inverted-cone water.

**Minor.** In pair 021, "(d) 3→3" is not a change.

**Correction.**
- Add the pair with both pages, part correspondence, "changed" (exact versus 3 s.f.; bases changed) and a hidden label.
- Record the screen's measured recall on known pairs in its limitations.
