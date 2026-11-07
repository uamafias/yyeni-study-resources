I've finished the review. Here is the report.

# Independent plan review: 6145 NSSCO Economics (`work/nam-6145-nssco-2026/`)

**Verdict: FIX_PLAN_FIRST**

The syllabus facts, the AO arithmetic and the tariff evidence are correct. The defects are in the slot plan:
- It drops several explicit syllabus demands, including one "evaluate" outcome that gets no B or C practice anywhere.
- It leaves out quantitative skills that the syllabus and the plan's own corpus analysis call for.
- It assigns composite tasks to objectives by position in the list, not by what they demand.
- The exemplar breaks the plan's own rule on marking guidance.

None of these is a tooling limitation or an unavailable source. All can be fixed in step 4.

**Source order.** I read the syllabus PDF directly before opening any plan file: assessment pages 17–19, all content pages 8–16, the command words on page 22 and the glossary on pages 23–26. Rendering worked, so I used no fallback extraction.

---

## Findings, most severe first

### F1 (major, confirmed): composite tasks take each topic's first four source objectives, so evaluative bullets are dropped
- **Evidence:** In `planning/performance-specs.json`, `ITEM-6145-2.3-P02` and `-P03` cover `OBJ-6145-2.3-01` to `-04`. They leave out `OBJ-6145-2.3-05`, "describe and **evaluate** the functions of central banks, stock exchanges and commercial banks".
- In `topics/2.3/work_order.md`, that objective gets only `015-FEATURE` plus member DEF/FEATURE slots (`016`–`021`). So an outcome the syllabus says to evaluate has **no B or C practice anywhere**.
- `ITEM-6145-6.2-P02` and `-P03` likewise leave out `6.2-05` (taxes and the budget) and `6.2-06` (interest rate).
- The essay plans then attach "Evaluate" to objectives with no evaluative demand. Example: `ITEM-6145-3.1-P03` evaluates "Explain a market / types of markets".
- The `objective_selection_note` ("Original source objectives anchoring this topic") describes a choice that was not actually made.
- **Required change:**
  - Choose composite `objective_ids` by demand, putting evaluate/discuss/assess bullets first, and record the reason per task.
  - Add BEN/LIM/EVAL (or at least EVAL) for `OBJ-6145-2.3-05`.

### F2 (major, confirmed): typing a bullet as a list drops its source verb
`slot_plan.subtypes_by_objective_type` gives an `economics_list` parent only FEATURE (Identify, 2 marks). Its members become `economics_concept`, which gives DEF + FEATURE, whatever the bullet's verb. These demands are lost:

| Objective | Syllabus demand lost | Slots actually planned |
|---|---|---|
| `1.2-02` explain allocation in market/planned/mixed | how the price mechanism or planner allocates (B) | `010-FEATURE`, members DEF/FEATURE |
| `1.3-03` **discuss** levels of specialisation | discussion | `008-FEATURE`, members DEF/FEATURE |
| `4.3-01` describe how **and why** income groups differ | the "why" | `001-FEATURE`, members DEF/FEATURE |
| `6.2-03` **explain** fiscal and monetary policies | fiscal mechanism (corpus has a 9-mark fiscal evaluation, 2023) | `016-FEATURE`, `017`–`020` DEF/FEATURE |
| `6.2-02` aims and **why they should be achieved** | why, for each aim | one parent BEN/LIM/EVAL; each aim only DEF/FEATURE |
| `8.1-01` developed/developing **and reasons for stages** | the reasons | `001-FEATURE`, members DEF/FEATURE |
| `2.2-07` **explain the role** of employer association | the role (B) | `019-DEF`, `020-FEATURE` only |
| `9.1-01-M01` to `M05` (the five conflicts) | discuss each conflict | only 2-mark A-level DIST/APP; one EVAL on the parent |

**Required change:**
- Keep the list decomposition, but also type each parent (or its members) by the bullet's verb: mechanism or policy_evaluation where the verb is explain, discuss or evaluate.
- Rebuild the work orders afterwards.

The plan's claim that "Lists and their relationships are both taught" (PLAN §0) holds for the content, but not for the demand.

### F3 (major, confirmed): quantitative and graphical skills are missing
- **5.3 Production costs and revenue has no CALC slot at all** (`topics/5.3/work_order.md`: 16 of 20 slots are DEF/FEATURE). This is despite:
  - the general objective "acquire knowledge and **skill in determining** the costs of and revenue from production";
  - the syllabus glossary formulas (AC = TC ÷ Q, AR = TR ÷ Q, TR = P × Q, Profit = TR − TC);
  - a held question that asks the candidate to classify a computed cost (2022 P1 17, `planning/questions-2022.txt:17`);
  - the corpus analysis §9.6, which promises clean examples for "costs".
- **8.2 Living standards has no CALC.** Yet GDP per capita (2020 P1 18) and real income per capita (2023 P2 1(b)) are both in the corpus, and §9.6 promises "income per person".
- **7.1:** the bullet says "**define** retail price index and show its simple calculation", but there is no DEF slot (only `001-CALC` and `002-INTERP`). There is no inflation definition card either.
- **1.1:** "explain and **illustrate** opportunity cost" has no illustrative slot (no PPF or numerical schedule), although the syllabus glossary ties opportunity cost to the PPF.
- **Required change:**
  - Add CALC + INTERP to 5.3 (objectives `-01`, `-02`, `-03`).
  - Add CALC to `8.2-01`.
  - Add DEF to `7.1-01`.
  - Add a schedule-based illustration slot to `1.1-02`.

### F4 (moderate, confirmed): about 15 DEF slots ask learners to "Define" something that is not a term
Affected slots:
- `2.2/003-DEF` (aims of trade unions)
- `4.3/002`, `004`, `006-DEF` (income-group spending/saving/borrowing *patterns*)
- `2.3/004`, `006`, `008-DEF` (functions/qualities/types of money)
- `6.1/003`, `005`, `007-DEF` (government as producer/provider/employer)
- `3.2/012`, `014-DEF` (changes in demand/supply conditions)

Each one leaves the author to choose what to define, which contradicts "a plan with no judgement left in it" (PLANNER.md). **Required change:** retype these members (to FEATURE, APP or MECH) or name the exact term in the registry's `learner_objective`.

### F5 (moderate, confirmed): every short-answer composite is four 2-mark "Define" parts
- All 28 `*-P01` specs are `Define ×4 @2`.
- This conflicts with the task brief ("meaning, distinction or named feature") and with evaluative anchors such as `1.1-03` and `3.5-01`.
- The exemplar's `ITEM-6145-1.1-P01` already deviates (Define / Identify / Explain / Identify) without a recorded deviation.
- **Required change:** set the part command words per objective from observed 2-mark pairs (Define, Identify, State, Explain, Outline at 2 are all observed). Then make the exemplar match.

### F6 (moderate, confirmed): the exemplar does not show a usable shape for the risky parts
The economics in `exemplar/topics/1.1/` is accurate, but:
- **Marking guidance is filler.** Nearly every element reads "credit a relevant, distinct element supported by the response". This breaks PLAN §3 ("not repeat labels as filler").
- **No mark breakdowns.** No per-element allocation is given for the 7-mark EVAL (`007-EVAL`), the 20-mark `P02` or the 14-mark `P03`.
- **The 7-mark Explain answer in `P02` lists element names** instead of modelling a developed answer. That is the "listing without development" failure the corpus analysis warns about.
- **No Namibian context.** Every `context.facts` is empty, and there is no N$, place or invented Namibian entity, although the plan requires them.
- **Only topic 1.1 is covered.** There is no CALC, INTERP or DIAGRAM example. The schedule-instead-of-renderer diagram method (the least proven part of the plan) is never demonstrated.

Also, the fourth `not_run` in `qa_report.json` is the semantic review `SR-1.1-PENDING`. "No failures" is true only of the deterministic checks.

**Required change:**
- Rewrite the exemplar guidance with real credit points and allocations that add up to the tariff.
- Add Namibian data.
- Add a thin 3.2 slice (one DIAGRAM built from a schedule) and one CALC slice.

### F7 (moderate, economic accuracy in Namibian context): the N$–rand peg is never mentioned
- Grepping the profile, glossary, plan, handover, gaps and misconceptions for rand/peg/Common Monetary Area finds nothing.
- Topics `2.3-03/04`, `6.2-03/06` and `7.4-02`, plus `CM-6145-CURRENCY`, will be written with invented Namibian scenarios.
- Without a condition, authors can easily write that the N$ appreciates against the rand, or that the Bank of Namibia sets interest rates with no external constraint.
- The glossary entries for appreciation and depreciation say "under a floating system" but never tell the author how the N$ works.
- **Required change:** add a conditioned mechanism or authoring constraint. *I have not checked this against a source in the repository; the wording should be verified before use, in line with the plan's own rule on jurisdiction-specific claims.*

### F8 (moderate, confirmed): topic ownership and scope guards are weak
- **Generated `adjacent_topics` match words, not meaning:**
  - 3.5 → 7.3 and 5.3 → 7.3 ("Output": firm output vs national output)
  - 6.2 → 3.5 ("Policies": government policy vs pricing policy)
  - 9.1 → 4.3 and 7.3 → 4.3 ("Expenditure")
  - 5.4 → 3.1 and 1.2 → 3.1
- **Real overlaps have no owner:**
  - exchange rates: `2.3-03/04` vs `7.4-02`
  - central bank: `2.3-05` vs `6.2-03/06`
  - the policy aims (`6.2-02-M01/M02/M05`) vs 7.2, 7.1 and 7.4
  - free trade vs protection: `9.1-01-M04` vs 7.4
  - IT: `5.2-04` vs `8.2-03`
  - HIV and AIDS: `5.2-05` vs `6.3-05`
  - public corporation: `2.1-02-M08` vs 6.1
- **The scope patterns don't guard the next level up.** All 28 contracts carry the same five regexes for far-above-level terms (IS-LM, Marshall-Lerner, NPV and so on). Nothing guards against terms one level up, such as AD/AS, multiplier, oligopoly, consumer surplus, deadweight loss or price discrimination. PLANNER.md §5 makes this the planner's job. The settled glossary even includes "price discrimination", which is not in the syllabus.
- **Required change:**
  - Add an ownership/cross-link table to the PLAN and the contract `planning_notes`.
  - Add level-up patterns, with must-catch and must-allow tests.

### F9 (moderate): glossary gaps and no ruling on imprecise syllabus definitions
- **Missing from the settled glossary although the objectives depend on them:**
  - complementary and substitute goods (3.2 demand determinants, MIS-008)
  - PPF (1.1)
  - short run, long run and the law of diminishing returns (the plan's own rule that short-run and long-run effects stay distinct)
  - normal and abnormal profit (3.5)
- **The syllabus's own glossary has imprecise entries that authors will meet, and nothing tells them which to follow:**
  - "Diseconomies of scale" leaves out the long-run, scale condition.
  - "Demand" leaves out "willing and able".
  - "Law of increasing opportunity cost" is worded oddly.
- **Required change:** add the missing entries, plus a disputed-source note stating that the settled glossary wins.

### Minor issues and suggestions (not blocking)
- **Parent and member slots duplicate each other:**
  - 3.3 has three CALC (`013`/`015`/`017`) and three INTERP for two calculations.
  - 3.5 has three BEN/LIM/EVAL triples plus two essay-plan evaluations, which is five evaluations of perfect competition vs monopoly. Yet there is no DEF or FEATURE for what those market structures are.
- **3.1 and 3.4 are lopsided:** 4 flashcards against 42 marks of composites.
- **4.2 members** like "Explain agricultural earnings" are DIST items with nothing to compare against.
- **5.4-05's list** "(size of market; capital; organisation)" was not decomposed, unlike the 31 lists that were.
- **Integration types:** lateral and conglomerate integration are left out. The corpus only shows horizontal and vertical, so this is a suggestion only.
- **Generated work-order prose** mentions "AO1/AO4" and a "None% target". This comes from the standard's generator; report it to Vitalis rather than fixing it here.

---

## Answers to the six questions

**1. Coverage.** Coverage is complete; demand is not faithful.
- I independently counted 28 topics and 96 bullets in the PDF.
- 31 decomposition entries contain 98 members, which gives 194 assessable objectives and 222 nodes. These counts are correct.
- No invented requirements, apart from the "price discrimination" glossary entry.
- I read all 28 slot tables. The demand losses (F1–F3) are the material omissions.

**2. Assessment facts.** The facts are correct.
- The paper structures and the 120 offered vs 80 attempted marks for Paper 2 are right.
- The calculated targets 39 / 25.5 / 35.5 are right.
- 881 + 622 + 721 = 2,224 marks, and the shares reproduce exactly.
- 421 + 84 = 505 items reconciles with the per-topic flashcard sums.
- Every slot's command word and tariff pair is in the observed table.
- The AO labels are defensible:
  - Paper 1 Section A is AO A by syllabus statement.
  - Describe → A, Explain → B and Discuss → C follow the syllabus page-13 AO prose (printed page 13).
- They are not tuned slot by slot, but AO C is structural. The composites carry 588 of the 721 C marks (82%); flashcards carry only C 133 (19 EVAL × 7). The balance therefore comes from the uniform three-task template, and under F1 that template puts C marks on non-evaluative objectives.

**3. Task design.** The three tasks per topic are reasonable in form, and the tariffs are honest (part sums, not invented single-question tariffs). The problems are:
- the mechanical objective selection (F1);
- the four-Define short answers (F5);
- evaluation forced onto 3.1 and 3.4;
- duplicated parent/member slots.

An author **cannot** follow the handover without material planning decisions (F2, F4, F5, F8).

**4. Glossary, mechanisms, misconceptions and exemplar.**
- The 124 glossary senses I read are economically sound. The gaps are F7 and F9.
- The five conditioned mechanisms are accurate. The minimum-wage rationale is correct.
- The roughly 27 misconception tests I read are discriminating and accurate.
- The exemplar teaches correctly but does not model credit points, Namibian context or the risky shapes (F6).

**5. Tooling caveats.** They are transparent and acceptable on their own: the nested-exposure adapter, the old closed schemas, the exit-code vs JSON-decision mismatch, and the C-18 warning with C-35/41/43 not run. The only knock-on blocker is that the uncertified diagram method has no worked example (F6).

**6. Readiness.** Not ready for Jeremy's approval. F1, F2 and F3 must be fixed, and F4–F9 should be, then the plan rebuilt.

Already accepted and **not** counted as defects: the pilot exception, the source gaps (no standalone mark schemes, no 2025 papers, papers marked "First Proof") and the main topics being unauthored.

---

## Scope and limitations
**Reviewed:**
- AGENTS.md, TEAM-PLAYBOOK.md and PLANNER.md
- the syllabus PDF pages 1–26
- the plan, handover, STATUS, syllabus brief and corpus analysis
- `decomposition-map.json`, the registry's learner objectives and `plan-validation.json`
- `performance-specs.json`: specs for 1.1, 2.3, 3.1, 6.2 and 8.1 read; the 28 short-answer specs checked by pattern search
- `subject-profile.yaml` and the glossary senses
- about 27 of the 32 misconceptions
- `source-discrepancies.json`
- all 28 work-order slot tables
- the 3.5 contract in full, plus the adjacency field of every contract
- the exemplar notes, items and `qa_report.json`
- the question lists, searched for calculations and integration

**Not independently verified:**
- `exam-exposure.json` and the C-39 recomputation
- `syllabus-facts.json` quote by quote
- the scope-scan catch/allow examples
- `GAPS.md`, `SOURCE-INVENTORY.md` and `qualification-profile.yaml`
- the remaining misconceptions and composite specs
- an exact count of the 124 glossary entries
- the N$ peg claim (F7), which comes from my own knowledge, not a repository source

I had read-only tools and ran no scripts or checks. I changed no files.
