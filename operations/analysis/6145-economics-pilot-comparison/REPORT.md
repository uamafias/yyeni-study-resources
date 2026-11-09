# NSSCO Economics 6145 — audit of the two pilots (provisional)

Date: 2026-11-08. Repo: uamafias/yyeni-study-resources (live, read-only). Nothing imported, archived, edited or assigned.

## 1. Executive recommendation

**Neither pilot should be adopted whole. Use V as the base and import selected J items; then run the repair and authoring backlog before release.**

- **V** = main, frozen at `31e97b9` (content = `06c382c`, 28 Oct 2026): 625 items (513 flashcards + 112 tasks, 12 diagram cards with PNGs).
- **J** = `nssco-6145-economics`, content frozen at `3a596e7` (tip `7df7918` only adds import audit files): 458 items (378 flashcards + 80 tasks; its 6 DIAGRAM cards have no images).
- V is stronger on breadth of examined content, notes-backed definitions, and the only verified diagrams. J is stronger on 4.3 and 5.3, on calculation/interpretation transfer cases, and on several V items that leak their answer (e.g. V 3.2-007/011/014 are better in J). J has the more serious economics errors (3.5 N$10 price vs N$9 cost under free entry; 3.2 supply-decrease receipts N$640 to N$600 judged "cannot assume"), more answer leakage in prompts (97 answerability flags overall, 63 in J), no 5.4 content on types of scale, and a rand-peg line injected into unrelated 2.3 items.
- V's characteristic defects: placeholder/boilerplate marking (131 marking flags), repeated template tasks (19 "P02" short answers restate cards; 20 of 27 essay plans share one "solely... not supplied" shape), and mark criteria stricter than the exam (e.g. 2.3-011, 2.3-029, 5.4 definitions).
- Recommended final bank: **710 items** (V 463, J 247): **536 flashcards + 174 assessment tasks** (see `canonical_manifest.csv`). 271 of those need a specified revision before use.
- This is a content and curriculum judgement. **No learner evidence exists for either pilot**, so nothing here shows that one produces better learning.

## 2. Theme/topic comparison (V/J counts: audited ; in final selection)

| Topic | Audited V/J | Final V/J | Recommended source |
|---|---|---|---|
| 1.1 | 15/10 | 14/2 | combination |
| 1.2 | 22/20 | 17/10 | combination |
| 1.3 | 16/17 | 12/7 | combination |
| 2.1 | 22/26 | 18/4 | V |
| 2.2 | 31/22 | 23/11 | combination |
| 2.3 | 48/21 | 40/16 | combination |
| 3.1 | 12/6 | 7/3 | reconstruct |
| 3.2 | 29/22 | 23/11 | combination |
| 3.3 | 26/17 | 18/10 | combination |
| 3.4 | 12/6 | 9/5 | V |
| 3.5 | 9/8 | 8/4 | combination |
| 4.1 | 12/9 | 11/5 | V |
| 4.2 | 29/25 | 21/18 | combination |
| 4.3 | 16/20 | 12/17 | J |
| 5.1 | 18/11 | 15/9 | combination |
| 5.2 | 20/14 | 14/8 | combination |
| 5.3 | 28/20 | 10/13 | combination |
| 5.4 | 37/25 | 21/11 | combination |
| 6.1 | 13/7 | 5/4 | combination |
| 6.2 | 42/41 | 31/22 | combination |
| 6.3 | 23/10 | 18/5 | combination |
| 7.1 | 18/11 | 13/5 | combination |
| 7.2 | 24/10 | 17/8 | combination |
| 7.3 | 20/18 | 16/5 | combination |
| 7.4 | 23/16 | 19/8 | combination |
| 8.1 | 22/23 | 17/12 | combination |
| 8.2 | 19/12 | 14/7 | combination |
| 9.1 | 19/11 | 15/5 | V |

Single-source topics: V for 2.1, 3.4, 4.1, 9.1; J for 4.3. 3.1 must be reconstructed: V teaches physical/digital markets, J product/factor markets, and neither is the syllabus's "types of market".

## 3. Item-level audit
All 1,083 items have a verdict, reason, defect tags and counterpart in `item_audit_all_1083.csv`.

| Verdict | V (625) | J (458) |
|---|---|---|
| Keep unchanged | 313 | 149 |
| Keep with revision | 174 | 120 |
| Replace with counterpart | 49 | 72 |
| Remove as redundant | 80 | 99 |
| Move to another format | 6 | 16 |
| Unresolved | 3 | 2 |

## 4. Coverage
`framework.md/json`: 9 themes, 28 topics, 96 printed bullets mapped to the 10 papers (271 parts, 1,000 marks) and examiner reports. Syllabus entitlement never examined (8 bullets: 2.2.2, 2.2.5, 3.1.2, 3.2.1, 3.4.1, 4.2.3, 5.1.3, 6.2.1) is kept separate from exam emphasis. Per-requirement V/J coverage is in the stage-1 results (`audit/results/G*.json`, 103 requirements; some 96-bullet gaps remain as terse entries, see limitations).

## 5. Overlap map
`duplicate_overlap_map.json`: 109 clusters coded 1-6; 45 items dropped from the selection as exact or reworded duplicates (relation 1 or 2). Transfer variations and progressions were kept.

## 6. Selection manifest
`canonical_manifest.csv` and `.json`: source commit, item ID, bank (flashcard vs assessment), exact revision, superseded items, and a prerequisite-based order. The proposed sequence departs from syllabus order: opportunity cost, money, demand/supply, elasticity, labour market, firms/costs/scale, market structure, macro indicators, policy, population, conflicts.
Assessment bank: all 22 EVAL cards (4+ marks) and all 12 PROC diagram cards, plus the 145 non-flashcard tasks, should be a **separate** bank from flashcards. Retain/revise/remove lists are in the coherence output (`audit/results/COH.json`, `assessment_tasks`). Notably: J's 14-mark two-case essays do not match any examined format; V's routine 7-mark parts are inflated; task counts do not track examined share (3.1 and 3.5 carry 0.2% of marks but have 4 and 7 tasks).

## 7. Repair backlog (priority order)
1. **Accuracy / marking that could cost correct answers marks (28 accuracy, 237 marking flags).** Fix: V 2.3-011, 2.3-029, 5.4 definitions 016-028 (boilerplate second mark; stage-1 and challenger disagree on 019-028, resolve by removing the template), V 1.2-014/015; J 3.5-005/P01/P02; J 3.2-016/P02/P03; J 7.4-013 ("capital account" per 2023 exam); J 2.3 peg lines; V 2.2-P03 (cooperative vs joinery firm).
2. **Answer leakage and trivial cards (97 answerability flags).** Includes V 1.2-P01, V 1.1-P01/009, V 2.3-P03, J 3.3-P01(d), J 3.2-016, and J 2.1 cards copying answers from stems.
3. **Revisions dropped in the first selection:** now resolved from stage-1 text; revision wording itself has not had a second review.
4. **Policy for inconsistently handled items:** recall bundles, two-case plans and MOVE_FORMAT items were treated differently by topic; apply one rule (assessment bank).
5. **New authoring:** 181 gap entries in `gaps_new_authoring.csv` (many overlap). Highest value: weighted RPI; MC=MR and marginal analysis; define real income and state which method (exact deflation gives N$4,831 vs the examiner report's N$4,825); public goods, merit goods, privatisation, SOEs (6.1); consumer and employee protection with verified Namibian sources; monopoly control and price maker; PED determinants; decrease-in-demand diagram; collective bargaining, union advantages, dispute resolution; exchange-rate effects and currency conversion both ways; GDP per capita and reasons for measuring national income; population growth reasons; characteristics of developing countries; between-nations comparison (8.2); social/external cost definitions; WTO and import quota reasons; types of economies and diseconomies of scale for J-sourced items; mergers, firm size measures, reading fixed cost from a table.
6. **Sequence:** reorder; several dependents precede prerequisites (real income before inflation, 3.2-P03(d) before elasticity).
7. **Contradictions to reconcile:** rand-peg treatment; PED sign convention (J 3.3-010 prints -0.5); whether inflation helps borrowers (V 7.1-010 vs J 7.1-008/V 7.1-P04); MC=MR given on one card but MC never defined.

## 8. Verification and limits
- **Read:** 1,083/1,083 items read by stage-1 reviewers (V 625, J 458; per-group counts all complete, no ID missing or duplicated, checked by script). The 743 provisional selection rows were re-read by two challengers (375 + 368) and a coherence reviewer (743). I did not read every item myself; I spot-checked the N$4,825 figure against the 2022 examiner-report extract (present, as a worked answer).
- **Recommendation is therefore provisional** because: (a) supporting notes were only grepped or heading-read (10 topics in full by the coherence reviewer); (b) challenger and coherence reviewers read truncated prompt/marking text (about 300-450 characters) on long tasks; (c) examiner-report text comes from a pilot's extraction, spot-checked against the original PDFs (2020-22: 30/30 each; 2023: 26/30; 2024: 8/30, misses were layout interleaving); (d) the 2021 P1 report has comments displaced against answers for Q4 and Q7-Q10; (e) the "requirements" and "selection" fields from stage 1 are terse, and 40 plus 26 selection rows originally carried placeholder revisions, now filled from stage-1 item text.
- **Not verifiable / not verified:** Namibian company-law limits (partnership 20, close corporation 1-10, private company), NSX trading claim, CRAN/NaCC/NSI/NAMFISA roles, the 1998 HIV code, the 2017 domestic-worker minimum wage, ordinary-hours rule (45/week). **Verified online 2026-11-08:** N$ pegged 1:1 to the rand; Labour Act 2007 s5 prohibits HIV-based employment discrimination (per a parliamentary statement, Act text not read); 2024 Consumer Protection Bill still pending (so no CPA is in force). A "Consumer Credit Act" could not be verified.
- **No standalone mark schemes exist.** The examiner reports embed answer points and level descriptors; reviewer references to "mark scheme" mean those.
- **Calculations:** every numeric example was recalculated by reviewers; none had an arithmetic error. Weak points are wording and marking. 12+ V diagram PNGs were opened and matched; J diagram cards have no images, so they could not be checked.
- **Provenance:** V's tracker shows 580 items at `c7d6bb1` and 625 at `06c382c` after a reopened plan; the material was authored and reviewed, not piloted with learners. J's 458 items were imported into six live YYeni classrooms on 8 Nov 2026, and 953 older cards (a legacy set unrelated to V) were archived. Import is not evidence that the pilot worked. I did not examine learner activity in YYeni; if any exists for the new cards it was not reviewed here.
- **Unresolved disagreements** (kept, not averaged): stage-1 UNRESOLVED items are J 2.1-021 (challenger: rewrite as a new formal-versus-informal card), J 6.2-037, V 6.1-009 and V 6.3-009 (challenger: still unresolved), and V 5.1-014 (stage 1 said move to 7.3, challenger reversed to keep as a value-added definition; applied). Challenger restores applied to the manifest: V 1.2-009, V 2.2-003, J 2.2-012, V 5.1-014, V 6.3-009 (as a flagged unresolved item), V 6.1-007, V 6.1-008, V 5.3-004, J 5.4-014, V 7.2-015, J 6.3-007, V 5.2-003. Not applied: CH2's proposal to extract part of V 6.1-P02 and its flag that V 6.2-006 is treated inconsistently. Both need a decision. 45 duplicate drops were applied from the coherence review; they are not independently re-verified.
- Methods: matching by skill, not ID (only 139 IDs coincide across pilots); no semantic-similarity score was used as a verdict; no numeric overall score is given.
