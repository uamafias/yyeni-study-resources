# Second independent Step 6 review: 6136 NSSCO Development Studies (repaired workspace)

I reviewed this read-only on 2026-10-20, with Jeremy's authorisation for a second review. I made no edits and ran no scripts. I did not publish, commit, import, use subagents or do web research. Because edits were off, I wrote no review YAML; this report is the record. The first review (`review/CLAUDE-RESOURCE-REVIEW.md`) is untouched.

## Verdict: **fix content before publication**

The plan repairs hold, so the plan does not need fixing first. Most of the first-review content repairs are real and good: Vision 2030, the Harambee Prosperity Plan (HPP), the baby-dumping and GBV teaching, the calculation methods, disease and immunisation, the 32 evaluation cards and the Section B scaffolds.

**The repair also caused a serious new problem that Codex's report does not mention.** `repair_resources.py:481–491` looked for each old card answer inside the note text and replaced it with the new short answer. In the original build the note paragraphs and the old card answers were the same text. So by my count about 66 teaching paragraphs (I compared 32 against the saved pre-repair copy) were replaced with two-sentence card answers. Definitions, conditions and anti-stereotyping cautions were lost. Several headings no longer match the text under them.

The worst case is 10.1. The notes no longer define random, stratified or systematic sampling, or questionnaires and interviews. These are examined in Paper 3 every year. A learner using the notes alone would now lose marks they could have earned before the repair.

Nothing here approves publication. All 749 claims are still `unverified` / not publishable, and all items are `review_required`.

---

## Findings

### New findings

| ID | Sev | Where | Defect | What it costs the learner | Repair | Conf. |
|---|---|---|---|---|---|---|
| **N-01** | **High** | `repair_resources.py:481–491`. Affected: 5.1 (24 sections, e.g. CU-5.1.01 Hunter-gatherers…; CU-5.1.02 Division of labour, Tools, Colonial influences…; CU-5.1.06 The state, Formal/Informal groups, Culture and values), 6.1 CU-.01 (Labour, Food production, Family welfare), 6.2 (7), 7.1 (4), 7.2 CU-.01 and .03 (6), 9.1 (8), 10.1 CU-.02, .05, .06, .07 and .10 (14) | The new card answers overwrote whole teaching paragraphs. This is recorded nowhere in `content-actions.json` or `REPAIR-REPORT.md`. **Lost definitions:** the three sampling methods, the four collection methods, an adequate diet, formal and informal groups. **Headings no longer match their text:** "Random sampling" now describes non-random selection; "Disease prevention and care" talks about clinic buildings; "Poverty and stress" no longer mentions stress. **Sentences with no subject:** "It can reduce exposure…" (7.2), "Its period or population…" (10.1), "…from its narrow export base" (9.1). **Cautions dropped:** that gender and age roles are not natural or fixed (5.1), that culture is not a blanket explanation (5.1), that doing work does not mean controlling its proceeds (6.1), and that poverty is not blame (7.2). The claim records still hold the old claims, so the notes now cite claims they no longer teach. | Cannot describe the sampling or collection methods from the notes (see Test C). Loses context in 5.1, 7.2 and 9.1. May absorb uncautioned generalisations. | Restore each overwritten paragraph from `review/repairs/baseline/` and then add the new two-point example as extra text. Add an audit that compares every pre-existing paragraph with the baseline and logs every change. | 0.95 |
| **N-02** | Medium | BLK-6136-4.2.05-04 (`4.2-urbanisation.md:131`) | The R6136-007 contradiction is still in the notes. The paragraph is unchanged from baseline, but the report says the "notes example" was fixed. Only the card (4.2-022) was repaired. | The notes still confuse unemployed, underemployed and employed people. | Apply the repaired card's framing to the paragraph (30 + 40 + 30, with the two overlapping totals of 70 labelled). | 0.97 |
| **N-03** | Medium | `repair_resources.py:496–509`. CLM-6136-2.2-02-00-01, -02-01-01/02, -02-02-01/02; the 7.1 China and Singapore claims; all CLM-6136-9.3-01-* | Source links were attached wholesale: every claim in a unit got every link in that unit. Generic planning ideas now cite the NDP5 page as corroboration; the China claim cites Singapore's library and the Singapore claim cites UNFPA's China statement. New real-world facts (the HPP pillars, the 2016 EU–SADC EPA, conservancies, contract labour, the cause of malaria) cite only an examiner report or the generic placeholder `6136-syllabus-and-local-assessment-corpus`. | Indirect: a truth reviewer cannot tell which source supports which claim, and the mislinks look like verification. | Attach a source to a claim only where it supports that claim. Add dated official sources for HPP, the EPA and conservancies. Keep all claims `unverified`. | 0.95 |
| **N-04** | Medium | ITEM-6136-8.1-025, 027–032; 9.2-011–016 | The same template-card defect as R6136-006 survives outside the 72 rewritten cards ("Explain one development mechanism concerning X"; "…of World Bank"). The answers paste whole note paragraphs, and 8.1-032 answers "one mechanism" with a list of five barriers. The first review only sampled 8.1-001–024, so it missed these. | Learners rehearse paragraphs instead of creditable points. | Rewrite naturally, with two discrete points per answer. | 0.9 |
| **N-05** | Low–Med | ITEM-6136-7.3-006 | The card is mapped to OBJ-6136-7.3.02-00 (traditional vs modern education) but compares a craft apprenticeship with a college course; neither is framed as traditional or modern. It asks learners to describe and give a "reasoned judgement" but never says "evaluate". The metadata honestly keeps `Describe and evaluate`, and the deviation is recorded. | Weak practice of the objective; the command word in the metadata and the learner's prompt differ. | Reframe as community/traditional learning vs institutional/modern education. Restore "evaluate" once the standard owner fixes check C-14. | 0.8 |
| N-06 | Low | ITEM-6136-2.2-004 | The card refers to NDP5 "economic-progress and social-inclusion goals", but these are not the four NDP5 goals the notes teach, while the marking guidance demands "named NDP5 goals". No card tests the HPP pillars, because slot 2.2-003 ended up reverting to the Vision 2030 / HPP timeframe comparison (`repair_resources.py:392`). | Learner uses goal names that are not NDP5's. | Use the taught goal wording. | 0.85 |
| N-07 | Low | 10.1-P01–P04, first marking-guidance line | Every package still says "The model Section B is fictional…", but no model exists any more. | Confusing for teachers and learners. | Delete the clause. | 0.95 |
| N-08 | Low | `slot-demand-specs.json` CALC `task_requirement` (e.g. line 496) | The prerequisite-method sentence appears twice. | None (tidiness). | Remove the duplicate. | 0.95 |

### First-review content findings

| ID | Disposition | Evidence |
|---|---|---|
| R6136-001 | **Resolved** | `2.1…md:21–23`; ITEM 2.1-001 asks for the definition. |
| R6136-002 | **Resolved** (see N-06) | HPP paragraph `2.2…md:53–55`. Year and president are correct: 2016, Hage Geingob. The five pillars are correct. 2.2-P01 tests them. |
| R6136-003 | **Resolved** | The syllabus term is back. Definition, GBV types, factors, effects and responses are in `6.2…md:117–147`. Cards 018/020/021/024/025 are specific. |
| R6136-004 | **Partially resolved** | Breadth sets added: GNP, privatisation, NIC roles, schemes, birth rates, education, SACU/SADC, methods, decentralisation, trade, aid. N-01 removed breadth elsewhere (e.g. 6.1 food stages, 10.1 methods). SDGs: only SDG 12 is named, and the economic/social/environmental "pillars" framing is absent, yet 2023 P1 asked learners to state SDGs. |
| R6136-005 | **Resolved** | 7.1 natural-increase paragraph (30 − 10 = 20‰ = 2.0%). 7.2 worked percentage change (80→100 = +25%, 100→80 = −20%). 7.1-011, 7.2-003 and 7.2-014 can be answered. |
| R6136-006 | **Partially resolved** | All 72 cards are now natural, two-point items. But the fix spilled into the notes (N-01), and template cards remain elsewhere (N-04). |
| R6136-007 | **Partially resolved** | The card is fixed; the notes paragraph is not (N-02). |
| R6136-008 | **Resolved** | All 32 evaluation cards weigh real benefits and costs on both sides and end in a conditional judgement. 7.3-006 does describe both routes (see N-05). |
| R6136-009 | **Mostly resolved** | Added: conservancies, land reform and resettlement, contract labour, women in the liberation struggle, the 2016 EPA, South Africa and India state roles, Namibian processing industries. N-01 thinned 5.1 "Colonial influences". Sourcing for these facts is weak (N-03). |
| R6136-010 | **Resolved** | Malaria route, cholera and WASH, and immunisation (7.2 notes line 35). |
| R6136-011 | **Resolved** | All Section B answers (B lines) are bracketed scaffolds for the learner's own enquiry. The invented demonstration is separate and labelled (`10.1…md:265–267`). The old models are kept only in `prior-fictional-section-b-models.json`. No learner answer presents fictional data as the learner's own (N-07 aside). |
| R6136-012 | **Resolved** | `10.1…md:207` gives the data inline and cites the package IDs. |
| R6136-013 | **Resolved** | P02 defines total production cost as the whole. P03 links the journeys to the five sampled schools. |
| R6136-014 | **Resolved** | `1.1…md:103`; P02 now says "the share lacking safe water". |
| R6136-015 | **Partially resolved** | The repeated end-of-unit boilerplate is gone. Repeated scenarios remain: 30→10 losses (4.1 notes, 5.1-P02); blocked road or bridge (1.1-026, 4.2-019, 5.1-P01/056, 9.1-025, 9.3-002/P01); missing-input cases in 3.1 (×5). Notes now carry more verbatim prompt-plus-answer prose. |
| R6136-016 | **Resolved** | 9.1-031, 9.2-017 and 9.2-018 now apply the distinction to a new scenario. |
| R6136-017 | **Partially resolved** | Locators were added but attached wholesale and misattributed (N-03). Status is honestly left `unverified`. |

### Plan and tool findings

| ID | Disposition | Evidence |
|---|---|---|
| PL-1 | **Resolved** (plan) | The evaluation task requirement in `slot-demand-specs.json:461` now requires real trade-offs plus multi-point knowledge in the notes. Breadth is still practised only through the notes, not through recall cards. |
| PL-2 | **Resolved** (plan) | 82 objective titles were replaced (e.g. OBJ-6136-5.1.02-08) and the work orders regenerated; no generic titles remain. The template cards in N-04 are still unrepaired. |
| PL-3 | **Resolved** | Amendment PL-3; HPP is taught. |
| PL-4 | **Partially resolved** | The limitation is recorded honestly in `7.3/authoring_notes.json`. Check C-14's command blacklist is a **standard-owner** problem. See N-05 for whether the card fits its objective. |
| PL-5 | **Resolved** | Method map plus the CALC requirement (N-08 is tidiness). |
| T-1 | **Open (standard owner)** | C-35, C-41 and C-43 are `not_run`, not PASS. The C-35 message ("No graphical task") is still false for 10.1 (`qa_report.json:93`) and for 7.1. I checked the chart and map specifications by recomputation only; no drawn figure has been verified. |
| T-2 | **Resolved locally (limited scope)** | `audit_research.py` really does parse the authored stimuli, answers and tariffs, and three deliberately corrupted cases were rejected. Limits: it covers only the 10.1 packages and one 7.1 table, and its answer check only confirms a number appears somewhere in the answer. These are Codex's runs; I did not execute anything. |
| T-3 | **Open (standard owner)** | `STATUS.md:79`: the subject-profile schema rejects fields the tools use, and the runner exits 1 while its JSON says publish. `standard/` is unchanged. |
| T-4 | **Open / accepted** | Check C-18 measures AO share by item count, which is a counting artefact. The D-objective shortfall stays documented. |
| T-5 | **Closed** | 7.1-021 is rewritten and sound. |
| T-6 | **Open (advisory), now masking content loss** | Check C-26 (word budgets) warns in 16 of 18 topics (10.1: 11 units). Several of these units are short because of N-01, not because they are concise. |
| T-7 | **Open (tool limit)** | Codex reports zero matches of 8+ words. My spot check: the new baby-dumping definition and effects list closely follow the structure of the 2022 report's answer key. That is acceptable as a standard definition, but it is not structurally original. |

---

## Numbers I recomputed

Everything below matches what the cards and notes state.

- **1.1:** P02 averages N$20,000 and N$30,000; 55% vs 20% lack safe water; 400/1,000 and 700/1,000 participation.
- **3.1:** sector shares 40/25/35 (sum 100); 30%, 30%, 40%; P02 = 30%.
- **4.1:** 100→60/90 queue; 70/30 vs 90/10 saleable/spoiled; P02 25/25.
- **4.2:** 40%→30%; 100→180 and 150→250 households per point; 50%.
- **5.1:** 105→125 water units; 180 − 125 = 55; N$40 more retained / 30 fewer water units per visitor.
- **6.2:** 40% and 60%.
- **7.1:** pyramid tables sum to 100/100; 400/1,000 = 40%; 32 − 12 = 20‰.
- **7.2:** 25% and 60%.
- **7.3:** 70%, 80/60, 80→90, 10%, 60/75.
- **9.1:** −30 and N$600,000.
- **9.2:** N$700 outstanding.

**10.1 packages:**

| Package | A1 | A2 | B | Total |
|---|---|---|---|---|
| P01 | 25 | 10 | 15 | 50 |
| P02 | 20 | 15 | 15 | 50 |
| P03 | 25 | 10 | 15 | 50 |
| P04 | 25 | 10 | 15 | 50 |

Package figures: systematic selection 3…58; stratified 8 and 4; usable bags 80→120; rectangle 8/7/5 cm; pie 180/90/90°; funding gaps N$400 and N$60; litter −12.

## Learner tests (notes only)

- **Test A, OBJ-6136-6.2.05/06 (GBV and baby dumping), modelled on the structure of the 2022 Paper 1 question.** The notes now give: a definition with the required "without care" and "danger/death" criteria (1/1); three or more distinct reasons (3/3); three or more effects on the people involved (3/3); two GBV types (2/2); three factors (3/3); and five distinct responses (5/5). **About 17 of 17 → pass** (before the repair: 5–6). The adjacent abortion-attitudes subpart (2 marks) is not taught; it is arguably outside the syllabus.
- **Test B, OBJ-6136-5.1.04 (rural schemes in Southern Africa).** Six distinct cooperative benefits (4/4), a list of schemes (4/4), separate barriers for each scheme, and Namibian land reform and conservancies for regional reference. **About 13–14 of 14 → pass.**
- **Test C (demonstrates N-01), OBJ-6136-10.1 "name and describe random, stratified and systematic sampling" [6].** Under "Random sampling" the notes say what random sampling is *not*. Under "Stratified sampling" they give only an advantage. Under "Systematic sampling" they give only a risk, and the word "systematic" appears nowhere in the worked interval example. **About 3 of 6 → fail.** Before the repair the notes defined all three methods.

## Coverage and limits

**Coverage per topic.** I read every topic's rendered notes in full. I read the prompt and canonical answer of every item:

| Topic | Items read |
|---|---|
| 1.1 | 34 |
| 1.2 | 10 |
| 2.1 | 4 |
| 2.2 | 8 |
| 3.1 | 75 |
| 4.1 | 31 |
| 4.2 | 28 |
| 5.1 | 58 |
| 6.1 | 19 |
| 6.2 | 27 |
| 7.1 | 35 |
| 7.2 | 16 |
| 7.3 | 27 |
| 8.1 | 41 |
| 9.1 | 34 |
| 9.2 | 20 |
| 9.3 | 8 |
| 10.1 | 68 |
| **Total** | **543** (all 505 cards and all 38 activities) |

Some long answers came from the `EVALUATIONS` dictionary in the repair script; I checked six of those against the item files directly.

**Read thoroughly:**
- All 72 rewritten cards and all 32 rewritten evaluation cards.
- All four 10.1 packages, including their full marking guidance and every Section B scaffold.
- The whole `REPAIR-REPORT.md`, `content-actions.json`, the amendments file and `repair_resources.py` lines 1–539.
- `audit_research.py`, the numerical audit and its negative-check file, the validation and run logs, and the 10.1 `qa_report`.

**Also checked:**
- Syllabus PDF printed pages 2–23.
- The 2022 examiner report's GBV section.
- Grep of the extracts for SDG questions.
- Baseline comparisons for CU-5.1.01/.02/.06, 6.1.01, 7.2.01, 10.1.06/.10 and 4.2.05.
- Claim ledgers for 2.2, 7.1 and 9.3.
- Objective registry samples, work-order greps and `7.3/authoring_notes.json`.

**Not read:**
- Every content-unit JSON and claim ledger in full.
- `qualification-profile.yaml` and `subject-profile.yaml`.
- The contracts.
- The original paper PDFs (I used the saved extracts).
- `finish()` beyond line 539.

The count of 66 overwritten paragraphs is my reading of the rendered notes; 32 are confirmed against the baseline. All check results are **Codex's runs**, and I executed nothing.

**Anything new?** Yes: N-01 to N-08. N-01 is a regression introduced by the repair itself and blocks publication.

None of these findings has been fixed by me, and this report does not authorise publication.