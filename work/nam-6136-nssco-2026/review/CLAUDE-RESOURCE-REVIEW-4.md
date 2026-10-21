# Final independent review (round 4): NSSCO Development Studies 6136, Grades 10–11

## Verdict: **FIX CONTENT BEFORE PUBLICATION**

Two targeted content repairs are needed. The plan does not need fixing first.

- I found **no critical or high-severity defect**.
- **No causal mechanism is inverted.** Conditions like woodland regrowth and local participation in tourism travel with their claims.
- **The numbers recompute.** I rechecked every worked figure I met in the notes, cards and packages; only one notes passage fails (F1).
- **Of the earlier findings, 9 of 10 are fully resolved and R3-02 is partly resolved.**
- **Two medium findings remain.**
  - F1: a population-pyramid construction passage contradicts the data block above it.
  - F2: a few worked examples still give the exact answers to their cards.

Separately, the plan's own rule still stands: the 749 claims are unverified and not publishable until the prescribed verification (N-03). That is known debt, not a new defect, but it remains a publication condition.

I did not write `operations/review/…-r4.yaml`. Only Read, Glob and Grep were available, plan mode was active, and the brief was review-only. The findings below use the REVIEWER.md fields so they can be transcribed.

## Findings

**F1 — Medium, quantitative/coherence. Affects BLK-6136-7.1.06-04 and BLK-6136-7.1.06-05.**
- **Finding:** 06-04 gives one population 45% aged 0–14 and 5% aged 65+, and another 25% and 15%. The next block, 06-05, says "For the fictional table above… A's base bars extend 20% each side and older bars 3%; B's are 10% and 10%."
  - No such A/B table exists in the notes.
  - Those bar lengths match card 7.1-026's figures (40/6 and 20/20), not 06-04's.
  - Correct bars for 06-04 would be 22.5/2.5 and 12.5/7.5 each side, and it gives no middle band at all.
  - This is a leftover from the R3-02 rewrite. Codex's age-sex audit read the card stimulus, so it would not catch notes-to-notes drift.
- **Consequence:** a learner following the construction method from the notes gets contradictory figures for the one pyramid worked example.
- **Repair:** give 06-05 its own complete age-sex table (three bands, both sexes, totalling 100%) and matching bar lengths, or rewrite the bar lengths to fit 06-04 and add its 15–64 band. Use figures different from 7.1-026.
- **Confidence:** 0.95.

**F2 — Medium, analysis/curriculum (the remaining part of R3-02). Affects BLK-6136-3.1.10-05, BLK-6136-10.1.10-06 and BLK-6136-10.1.11-06.**
- **Finding:** full card prompts are gone from the notes, but these blocks still carry the exact numbers and answers of their cards and package parts.
  - **3.1.10-05:** "For separate practice, 450 of 1,500 is 30%, 360 of 1,200 is 30%, and 560 of 1,400 is 40%" are the answers to 3.1-049, 051 and 053.
  - **10.1.10-06:**
    - The 60/12 interval-5 list 3, 8, … 58 answers 10.1-040 and P01 A1(3).
    - The 40/20 → 8/4 split answers 10.1-044.
    - The 20-schools/five draw answers 10.1-042.
  - **10.1.11-06:**
    - The pie angles 180°/90°/90° answer 10.1-052 and P03 A1(5)/(6).
    - The 8/7/5 cm divided rectangle answers P02 A2(3).
    - The sketch map answers 10.1-053 and P04 A1(6).
  - So "distinct worked-note examples" is only partly met. The automated check looked for full prompts, not reused numbers.
  - The wider practice of building INTERP/CALC/CHAIN cards on the very scenario in the notes is common in topics 1.1–4.2 (for example BLK-1.1.04-02 → 1.1-018, 1.1.07-02…07 → 027–031, 4.2.01-01 → 002/025). There it fits the "cut cards from the notes" model and is not a defect in itself.
- **Consequence:** the calculation and construction practice in the most-examined topic (Research, 416 corpus marks) becomes recall of numbers already worked out, not transfer of the method.
- **Repair:** change the numbers in these three blocks (for example a 48-unit frame with interval 4, villages of 30 and 15, and a pie from 20 units). Delete the "For separate practice…" sentence.
- **Confidence:** 0.8.

**F3 — Low, curriculum/objective alignment. Affects ITEM-6136-2.2-003 and OBJ-6136-2.2.02-00.**
- **Finding:** the DIST/Differentiate slot now contrasts two HPP pillars. No card now pairs short-term and long-term planning, which is the comparison the objective names. 2.2-005 and 2.2-006 describe each horizon separately, and the subject profile says separate descriptions do not make a comparison. The notes (BLK-2.2.02-01) do teach the contrast.
- **Repair:** pair the horizons in 2.2-003 (scope, level of detail, time frame). The HPP pillars are already practised in 2.2-P02(a) and 2.2-P01(a).
- **Confidence:** 0.7.

**F4 — Low, marking guidance. About 45 items.**
- **Finding:** many marking guides either repeat the model answer or are generic ("Reason: identify the stated mechanism. Consequence: connect…"). Examples include 5.1-032…038, 5.1-041…045, 6.1-013…017, 6.2-012…015/018…021/023, 7.1-007…010, 7.2-004…007, 8.1-026/033…038, 9.1-004/010/015/022/026, and the 10.1 WHY cards 024…047.
- The subject profile requires that short-tariff guidance "names the essential scoring function". R3-10 fixed this for 8.1-025/027–032 only.
- The P01(b) guides in 5.1–9.3 now hold two "Development … [4]" lines: a generic one that mentions a "supplied barrier" even where there isn't one (6.1-P01, 7.1-P01), and the specific one.
- Prompt, answer and guide still agree with each other; the gap is that a self-marker isn't told what earns the marks.
- **Repair:** state one or two scoring criteria per item, and delete the generic P01 line.
- **Confidence:** 0.85.

**F5 — Low, labels/stems.**
- **2.2-P02:** labelled AO B only, but part (a) is mostly recall of pillar names and descriptions (AO A).
- **10.1-P02 A1(1):** the stem says "an interviewer's neutral price questions", which gives away the one-mark answer ("Interview").
- **Confidence:** 0.7.

## Earlier findings R3-01 to R3-10, checked against the current text

| ID | Disposition | Basis |
|---|---|---|
| R3-01 | **Resolved** | All ten P01(b) answers (5.1–9.3) now give four developed, context-specific steps. Guidance duplication logged as F4. |
| R3-02 | **Partially resolved** | Pasted prompts are gone and most rewritten blocks (for example 5.1.04-08, 6.2.04-02, 9.1.05-05, 10.1.10-05) use new cases. Exact answer reuse remains (F2), and the rewrite introduced F1. |
| R3-03 | **Resolved** | 4.2.05-04 now says "100 people available for work". The totals 30/70/70 are reconciled and explained as overlapping. |
| R3-04 | **Resolved** | The 10.1-P02 stem says the totals include spoiled bags, so 80 → 120 usable is supported. |
| R3-05 | **Resolved** | 7.3-006 and BLK-7.3.02-02 share the same facts: no qualification for the apprenticeship; fees and less earning time for college. Both state "illustrates traditional / modern institutional education", and the conclusions agree. |
| R3-06 | **Resolved** | No internal source wording remains in the notes. SDG 4, 5 and 13 are named, with a mechanism for climate impacts, adaptation and future needs plus an attribution caveat. Test 2 below shows this is enough, though just. |
| R3-07 | **Resolved** | 1.2-006 asks for action + benefit + one SDG, marked 1/1/1. SDG 12 fits with no assumed paid-work condition. |
| R3-08 | **Resolved, with F3** | 2.2-003 guidance now matches its prompt. 2.2-P02(a) is a real three-mark description: the learner must name the pillar and link it to the action. It covers 3 of the 5 pillars. Probe below. |
| R3-09 | **Resolved** | 1.2-P01(a) asks for two pillars [2]. BLK-2.2.02-03 gives NDP5's pillar names (Economic Progression, Social Transformation, Environmental Sustainability, Good Governance) and separates them from its goals. Both match my own knowledge. |
| R3-10 | **Resolved as specified** | No item IDs remain in the notes. 8.1-025/027–032 guidance is now specific. The same pattern elsewhere is logged as F4. |

**Codex's two substitutions.**
- **2.2-P02(a)** reaches the "describe three HPP pillars" demand through interpretation, which suits a data-response slot. A pure-recall card would be the cleaner way to test AO A (F5).
- **1.2-P01(a)** meets the two-mark pillar retrieval. The slot labels are unchanged and the change is recorded in authoring_notes.

## The six reviewer questions

1. **Causal validity.** No inverted mechanism. I traced, among others:
   - GNP total vs per person, and urban share vs urban count;
   - the fixed-cost economy of scale, and an investment inflow vs the goods balance;
   - water/sanitation vs malaria transmission routes;
   - woodland, channel and storage balances;
   - responsibility for gender-based violence placed on the perpetrator.
2. **Facts supplied by prompts.** Satisfied after R3-04. The answers to the evaluation cards rest on facts in their stems: feasibility, buyers and funding are given each time.
3. **Conditioned mechanisms.** Renewable wood (regrowth/harvest) and tourism income (local participation or retention) carry their conditions in 1.2, 3.1, 4.1 and 5.1. Statements about decentralisation, credit and ICT also carry their conditions.
4. **Scope.**
   - No out-of-scope sampling methods, and the investigation is never described as coursework. There is no line-graph construction, no HDI/MPI formula and no extra DTM stages.
   - All 30 misconception slots are present and discriminate between the two ideas.
   - The SDG 13 material goes beyond the strict wording of OBJ-1.2.03, which is about SDG 12. The corpus justifies it because 2022 P2 asked about Goal 13.
5. **Numbers and methods.** Sound: percentage change vs percentage points, ‰ vs %, per-person division, proportional allocation, pie and divided-rectangle specifications, and the reconciled package tariffs (35 + 15 = 50 ×4). The one exception is F1.
6. **Top-tariff support.** Yes for the objectives I tested (below).

## Learner tests (notes alone)

**Test 1 — high-tariff sampling explanation.**
- From BLK-10.1.10-01 to -04 and 09-01/02, a learner can define population vs sample and explain each method:
  - **random:** a complete numbered frame, an equal chance, a fair draw, and why "nearest" fails;
  - **stratified:** relevant groups, proportional allocation, random selection within groups, and the limits from non-response;
  - **systematic:** k = N/n, a fair start, and the risk from periodic patterns.
- Frame coverage and recording refusals are also taught.
- **Result: top band.** The only concern is F2: the worked numbers are the cards' own.

**Test 2 — three-mark explanation of why climate action matters for sustainable development.**
- From BLK-1.2.01-R01 a learner can write:
  - drought and flooding harm crops, water and infrastructure, undermining livelihoods and reversing development gains;
  - adaptation reduces present vulnerability;
  - cutting emissions limits further warming, which protects future generations' ability to meet their needs (linked to the 1.2.01-01 definition).
- **Result: three distinct creditable points. It passes, but only just.** There is one sentence of teaching and no card practises it. If the content is extended, one Namibian example (such as drought and rain-fed farming) would help.

**HPP probe — describe three pillars.**
- From BLK-2.2.02-R01 a learner can write:
  - governance means accountable decisions and useful services;
  - economic advancement means productive opportunities and jobs;
  - social progression covers food security, housing, sanitation and skills (infrastructure and international cooperation are also available).
- **Result: 3/3.** The notes describe each pillar rather than just listing it, which addresses the weakness the examiner report notes.

## Coverage

**Learner text.** I read every lesson block in all 18 topics, and every prompt, answer and guide among the 543 items, as the current extraction. That is more than the 20 cards per topic required; for 1.2, 2.1, 2.2 and 9.3 I read every item. I read all four research packages in full: stimuli, A1/A2 answers, tariffs and the Section B fill-in scaffolds. The B scaffolds do not invent fieldwork, and BLK-10.1.12-R01/R02 clearly separate the invented demonstration from the learner's own enquiry.

**Mandatory governance, plan and contract documents (all inspected).**
- **AGENTS.md, TEAM-PLAYBOOK.md and REVIEWER.md:** the six questions were applied, and the severity scale and finding format followed.
- **qualification-profile.yaml:** the AO weights and paper splits match the PLAN table. Commands used in prompts are all in the measured set: no standalone Analyse/Evaluate/Why, and Differentiate, Design and Outline are used only where the corpus observed them.
- **subject-profile.yaml:**
  - answer_structures are honoured in the guides, apart from the generic guides in F4;
  - the variant register is complied with (density/distribution; the two education classifications; money capital vs capital goods; hypothesis vs research question);
  - both conditioned mechanisms are present;
  - the no-renderer depiction rule is respected: specifications only, with disclaimers;
  - the tariff overrides match the slots.
- **PLAN and HANDOVER:** the counts match (505 + 38 = 543, 30 misconception slots, four packages, A1+A2 = 35 and B = 15). Claims remain unverified, items review_required, and "fictional, not the learner's fieldwork" is honoured.
- **The 18 contracts:** every one carries the four excluded constructs, and no learner text matches them. The teaching-depth ceilings for 1.1 (HDI), 7.1 (DTM) and 10.1 (sampling and line graphs) are respected.
- **Objective registry and work orders:** every slot ID, subtype, AO, Bloom level, command and tariff in the packet matches its work order.

**Incompatibilities between plan and content (none blocks publication).**
- **Word budget:** the PLAN projects 86,840–124,830 words of notes; 36,079 were delivered, about 42% of the lower bound. The plan calls the lower bounds advisory, and my depth tests found the sampled objectives adequate. But single-sentence teaching is common in member blocks (2.1's five Vision areas; 5.1 and 8.1 definitions), so the planner should bring the allocations into line with reality.
- **Contract ceilings:** they are copied per theme. 1.2 carries 1.1's HDI ceiling, and 2.1 carries 2.2's NDP-planning ceiling. This is harmless but inaccurate.
- **Profile `objective_types`:** these are identical boilerplate entries (the stale-schema limit already recorded in standard-compatibility.json).
- **AO labels:** 2.2-P02 is labelled AO B only, though part (a) is largely AO A recall (F5).

**Not re-performed or not opened.**
- `round3/actions.json` and `baseline/` were not opened. Every changed artefact was read in its current text through the full packet, but I did not compare it line by line with the old text.
- I did not reopen the syllabus PDF, syllabus-facts.json, GAPS.md, the corpus analysis or the assessment extracts in this session. Syllabus demand was checked through the supplied registry and profiles. Dated facts were checked against my own knowledge only (HPP 2016/Geingob; the HPP and NDP5 pillar names; NDP5 2017/18–2021/22; China 2015; Singapore 1987; SACU membership; EU–SADC EPA 2016). That is not source verification.
- **Overall scope:** complete for the mandatory learner text and the governance, plan and contract documents. Partial for re-checking against original sources.

## Unresolved limitations (known; not new defects in the learner text)

- **N-03:** 749 claims are unverified and not publishable; the external facts and citations (SDG, EPA, NIC illustrations, GBV plan, URLs) are unverified.
- Recurring card scenarios remain: a blocked road or bridge (1.1-026, 4.2-019, 5.1-P01/056, 9.1-025, 9.3-P01/002) and the missing-input cases in 3.1.
- Standard-owner limits remain: the stale profile schema, no compatible graph renderer and the runner's exit-code discrepancy. **C35, C41 and C43 are not_run, not passes**, and no plotted graph has been checked.
- The Codex-run figures were not repeated by me: 18 topics with 0 deterministic failures, 12 targeted checks, 17 numerical checks plus one negative case, 66 restored paragraphs preserved, 0 full card prompts in notes, and one 11-word SDG 8/12 title run in the copied-wording scan. As F1 shows, these checks did not compare notes passages against each other.
- No teacher or specialist approval is claimed or implied.
