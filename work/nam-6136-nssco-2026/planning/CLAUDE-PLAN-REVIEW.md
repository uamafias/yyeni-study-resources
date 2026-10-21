# Independent Claude Code review: 6136 NSSCO Development Studies, Step 4 plan

Reviewer: Claude Code (Opus 5.5), read-only, 2026-10-20. This is a plan review only. It is not subject-teacher approval and not a resource or publication verdict.

---

## 1. Verdict

**FIX PLAN FIRST.**

The qualification facts are faithful to the primary syllabus, and so are the AO definitions, the paper grid, and the 102→101 source bridge with the enterprise consolidation. The corpus evidence and the limits of the source set are recorded honestly.

The generated slot plan, though, does not carry the syllabus demand or the corpus demand. That is its main job. The cause is one generator rule, so the planner can fix it without touching `standard/`:

- `planning/build_plan.py:149` overrides the semantic type decision for every outcome that lists members.
- `build_plan.py:168` then gives all 292 members the same template ("explain and apply X") and the same State/2 (A) plus Describe/2 (B) pair.

The consequences:

- "Define", "explain", "assess", "evaluate" and "differentiate" outcomes mostly get a Suggest/3 A card instead.
- Define/What-is-meant-by and Calculate, both frequent in the corpus, are almost absent.
- Evaluation sits on describe-only lists, while real evaluate/assess outcomes have none.
- The headline AO balance (largest gap 4.29 points) mostly reflects how subtypes are labelled. It is not a measure of the analysis learners actually practise.
- On Paper 3, the community-project problem-solving question is missing, and the four research cycles share one identical scaffold.

As things stand, Codex would have to either reproduce these labels or make hundreds of educational decisions as "deviations". The handover is meant to prevent exactly that.

Nothing here is BLOCKED. The standard-owner issues stay open but do not stop plan approval.

---

## 2. What I inspected, and the limits

**Primary sources read directly as page images**

- **Syllabus** `Syllabi/Namibian Curricula/NSSCO (New)/NSSCO_DevelopmentStudies_Syllabus.pdf`, PDF pp.8–29:
  - content pp.5–17;
  - AOs p.18, scheme p.19, grid p.20, grade descriptions pp.21–22;
  - Paper 3 notes pp.22–24;
  - glossary pp.24–26.
  - I counted the bullets myself: 7+3+1+2+14+6+5+8+3+6+7+3+7+5+8+3+2+12 = 102, with 3.1's p.7 enterprise row continued on p.8.
- **2020 P1** (`2020/6136_1.pdf`), PDF pp.2–5: Q1 GNP table, definitions, GNP-per-capita calculation, relationship-with-statistics; Q2 factors of production, money capital vs capital goods, division of labour, technology; Q3 industrialisation and MNC definition.
- **2024 P3** (`2024/6136-3.pdf`), PDF pp.2–8: the whole paper. Section A Q1 school dropout (25) and Q2 small-scale community activity (10); Section B Q3 own investigation (15).
- **2024 examiner report**, PDF pp.166–168 (printed pp.164–166): P3 Q1(b)(ii)–(d), Q2 organisation/funding/problems, Q3 pilot "0 = for the meaning", the level-marked report, and the researcher-problem cap.

**Extractions used to navigate (not primary-checked)**

- `2021-P3-layout.txt` in full.
- Grep across all five P3 layout files for Section A structure.
- Grep across P1/P2 layout files for Define, What-is-meant-by, Calculate and By-how-much.
- `2024-ER-layout.txt` lines 690–960, including the teacher advice on sampling, line graphs and small-scale projects on printed p.166–167. Only the start of that advice is on the PDF pages I viewed.

**Workspace files read**

- STATUS, PLAN, HANDOVER, `qualification-profile.yaml`.
- Planning: `build_plan.py` in full; `build_exemplar.py` lines 100–190; `registry_decisions.json`; `profile_quality_decisions.json`; `glossary_decisions.json`; `plan-validation.json`; `standard-compatibility.json`.
- Curriculum: `performance-slot-specs.json` in full; `scope-scan.json`; GAPS.md.
- Registry: all 411 `objective_type` values, all 448 `syllabus_text` values, and the 292 member templates (counted).
- Work orders: 1.1, 3.1, 7.1 and 10.1 in full. 8.1, 2.2, 4.1, 5.1, 6.1, 6.2, 7.2 and 7.3 at slot level for the relevant outcomes. Subtype and command counts across all 18 `work_order.json` files.
- Exemplar: README; both rendered notes files; both item files.
- Corpus analysis §§1–6 and the recommendation on line 170.
- Standard code: `run_checks.py:22–23`; `yyeni_checks.py` C-16 (lines 883–899) and C-26 (lines 1030–1036); `make_work_order.py:306–477`.

**Not inspected, or only partly**

- `member_evidence_decisions.json` (the 91 member assignments).
- `exam-exposure.json` per objective.
- `answer-shapes.json` and `quality-evidence.json` as files. I checked them through the generator and the decisions file, and checked four of their citations against primary pages.
- `syllabus-facts.json`, `source-bullet-bridge.json`, the contract JSONs and `finalise_plan.py`.
- `misconceptions.json` beyond four entries.
- The 2020–2023 examiner reports, Paper 2 PDFs, and P1/P3 PDFs for 2021–2023.

This is a sample, not a complete audit of the 419 records or the 393 targets.

---

## 3. Prioritised findings

Severity scale: **C** critical (must fix before authoring), **H** high, **M** medium, **L** low. Every finding is confirmed in the cited files unless it says otherwise.

| ID | Sev | Where | Finding | Consequence | Correction |
|---|---|---|---|---|---|
| F-01 | C | `build_plan.py:149–151`; `registry_decisions.json` `types` | Any outcome with members becomes `ds_overview`, which gives one APP/Suggest/3/A slot. The concept/mechanism/strategy decisions are silently discarded. **50 content parents are affected.** Examples: 1.1:1 "define development" → `001-APP` Suggest 3; 7.1:1 "define population density and distribution" → `001-APP`; 8.1:1/3/5 "explain…" → APP Suggest (8.1 has no Explain slot apart from one MISCON); 6.1:3 and 6.2:3 "assess…" → `015-APP` / `012-APP`, labelled A. | The source verb of each parent outcome is not practised. Most "parent integration" is a single 3-mark Suggest card. | Honour the decision types. Give each parent a subtype that matches its verb: define → DEF; explain → CHAIN or WHY; assess/evaluate → EVAL; differentiate → a comparison subtype. |
| F-02 | C | `build_plan.py:163–168`; registry `learner_objective` (292/292) | Every member reads "In <topic>, explain and apply <X>; retain the parent outcome's required relationship and judgement." All 230 content `ds_member` objectives get FEATURE State/2 (A) plus INTERP Describe/2 (B), whatever the member's role. | Demand is invented: "explain and apply diet" for an *etc.* list in 1.1:5; "explain and apply India" for an *e.g.* list in 4.1:4; "explain and apply social development" for a *define* bullet. | Type each member by its role: **term** → DEF Define/1; **factor/cause** → CHAIN Explain; **example/illustration** → FEATURE or fold into the parent; **listed strategy under evaluate** → EVAL; **data indicator** → CALC or INTERP with data. Write each member's learner objective from the parent verb. |
| F-03 | H | Subtype→AO map `SUBAOS` (INTERP→B); `plan-validation.json` `exact_ao_marks` | 230 member INTERP Describe/2 slots supply **460 of the 965 B marks-equivalent (48%)**. Most describe a category with no data, for example 1.1 `003-INTERP` "social development" and 3.1 `065-INTERP` "primary production". That is A.2/A.4 work. Relabelling only those slots by task gives about **A 61% / B 24%** (my arithmetic from the counts). | The 4.29-point gap hides a real deficit of roughly 20+ points in analysis/interpretation (B.1/B.2/B.3). The tolerance check passes on labels, not on skills. | Label AO by actual task. Make INTERP slots genuinely data-based, with a self-contained mini-table, and B only when they are. Re-run the balance after fixing. Do not pad. |
| F-04 | H | All work orders: Define appears in 14 slots (6 content, 8 research); 0 What | Corpus: Define 34 + What 40 parts, mostly 1-mark "what is meant by". Primary check: 2020 P1 1(a)(i), 2(a)(i), 2(d)(i), 3(b)(i). Explicit "define" outcomes with no DEF slot: 1.1:1, 7.1:1, 7.1:3 ("define the terms" CBR/DR/IMR…), 7.3:1, 9.1:3, 9.2:1, 10.1:8. | The single most common P1/P2 demand gets almost no flashcard practice. | DEF Define/1 (or What/1) for each term member and each define outcome. Use FEATURE only where the source asks for features. |
| F-05 | H | One CALC slot subject-wide (1.1 `031-CALC`); 17 content `data_response` specs are Describe 2 + Discuss 4 with no Calculate | Corpus has Calculate 10 + By how much 3 across P1 and P2. Primary: 2020 P1 1(a)(iii) GNP per capita. Grep: 2021 P1 export–import difference, 2022 P2 percentage change, 2023 P1/P2 "by how much", 2024 P1 percentage change. The 2024 report (primary p.164) says learners could not convert percentages to degrees. 7.1, 7.3 and 9.1 have no numerical slot. | PLAN rule 4 (absolute vs percentage change, units) is stated but not practised. A report-evidenced weakness goes unaddressed. | Add CALC (Calculate/2, By how much/2) in 1.1, 3.1 (sector %), 4.2 (urban growth), 6.2, 7.1 (density, natural increase), 7.2, 7.3 (literacy/enrolment) and 9.1 (balance of trade). Let some data tasks use Calculate + Describe instead of Discuss. |
| F-06 | H | `build_plan.py:166` hard-codes 3.1:6/7/9 as `ds_strategy`; 10.1 `ds_research_method` members | EVAL Discuss/4 sits on 8 energy sources, 4 technology types, labour/capital-intensive production, "identify research topic", and the four "features of a good topic" (10.1 `002/005/007/009/011-EVAL`). Their source verbs are describe, explain, identify and state. Real evaluate/assess outcomes have **no** EVAL: 2.2:2 (`003-INTERP` D/2), 4.1:4 (`027-INTERP`), 5.1:7 (`073-INTERP`), 6.1:3 (`015-APP` A), 6.2:3 (`012-APP` A), 6.2:4 (`021-INTERP`). | Evaluation is invented where it isn't asked for and missing where it is. B.3 ("evaluate alternative approaches") is under-practised. | Move EVAL to the evaluate/assess outcomes. Energy and technology need Describe plus an explained "potential role in future development". Topic features need State/Explain. |
| F-07 | H | `CW['EVAL']=['Discuss']`; `performance-slot-specs.json` | About 75 Discuss prompts: 54 flashcards, 17 data tasks, 4 research subparts. The corpus has 3 Discuss parts out of 419. Most judgement in the corpus comes through Explain (advantages/disadvantages), Suggest, Choose…give reasons (3/5), and Describe and evaluate (4). | Each pair is "observed", but the mix is unrepresentative, and the plan's own "observed somewhere" test is too weak. | Allow several commands per subtype: EVAL → `['Describe and evaluate','Explain','Choose','Discuss']`. Set objective `command_words` from the syllabus verb plus mapped evidence (see F-17). |
| F-08 | H | No flashcard uses Differentiate, Compare, Identify or Name | Syllabus verbs: differentiate (4.2:5, 10.1:4/5/9), distinguish (7.3:3), identify (4.1:2/4, 10.1:1), name and describe/explain (9.1:8, 10.1:6/10). Corpus: Identify 45, Differentiate 6, Compare 5, Name 10. The "paired comparison" quality criterion (COMPARE-3) has no flashcard vehicle. Exemplar 3.1 `002-FEATURE` "State two features that distinguish…" is a Differentiate task (cf. 2020 P1 2(b)(i) Differentiate [2], primary) labelled State. | Paired comparison is a report-evidenced weakness and is not drilled. | Add a comparison subtype (Differentiate/2–3, Compare/2–3) for paired members. Use Identify/1 and Name/1 for source-reading and recall items. |
| F-09 | H | `profile_quality_decisions.json` `answer_structures`; C-16 (`yyeni_checks.py:883–899`) | A 2-mark INTERP must have guidance naming evidence, relationship, meaning *and* limit. CALC/2 needs five parts, CHAIN/3 four, EVAL/4 five. C-16 checks only that the guidance contains these keywords. Exemplar 3.1 `005-INTERP` has to bolt "State a limit" onto a 2-mark Describe. | The structure pushes authors towards compound prompts and boilerplate guidance, not tariff-true answers. | Scale structures to tariff. For example, INTERP ≤2 = evidence + relationship, with limit only at ≥3; CALC/2 = working + unit + answer. |
| F-10 | H | `performance-slot-specs.json` P01/P03/P05/P07 | Paper 3 Section A is two questions (25+10; 2022 20+15; 2023 24+11 per corpus §2). The second is sometimes small-scale community-project problem solving: 2024 Q2 aims/organised/funded/problems+recommendations [10] (primary PDF p.5); 2021 Q2 organisation/finance problems + solutions [10] (layout). The 2024 report tells teachers to teach this (layout lines 950–953). The approved corpus analysis (line 170) asked for "practical community project planning". All four 35-mark packs are one dataset with the same 10 parts; only MISCON-027 touches organisation vs funding. | The main D vehicle on Paper 3 is unpractised. It also explains part of the D shortfall. | Recast each 35-mark pack as about 25 supplied-research plus about 10 second-question marks. At least two cycles should plan a small-scale community project (aims → organisation → funding → problems paired with solutions and an implementer). The others should use a second short data stimulus. |
| F-11 | M | Same file, P02/P04/P06/P08 and P01/P03/P05/P07 | The four cycles have identical command/tariff/AO sequences. Only the theme names differ ("sampling", "representation", "evaluating recommendations"). Observed Section B asks are missing from the scaffold: explain the pilot actually done (2024 3(a)(iv)), justify choice of method or presentation, factors in choosing the issue (2022 3(a)(ii)), advantages and disadvantages of local research (2021 3(b)), and researcher problem with solution (2024 3(b)). | The cycles may differ only in topic, not in the method, data or problem practised. | Give each cycle distinct subparts tied to its named focus. Spread the observed Section B asks across the four cycles. |
| F-12 | M | `plan-validation.json` D = 49/2105 = 2.33% | Against a 5% target this is a 53% relative shortfall, hidden by an absolute 5-point tolerance. Practical-repair tasks (pilot repair, researcher obstacles, MISCON-028) are labelled C, and D appears in only 3 flashcards. | The problem-solving skill is under-weighted. | Fix through F-10 and task-true labelling, not padding. Report each AO's relative shortfall alongside the absolute gap. |
| F-13 | M | `make_work_order.py:408–422` (budget share = objective count) | About 240–380 words per objective, regardless of tier. Budgets follow list length rather than demand: 1.1 gets 8.3–11.9k words (4.9% of corpus marks) and 8.1 gets 7.7–11.1k (3.3%), while 7.2 gets 3.4–4.8k (7.4%) and 4.2 gets 4.4–6.3k (7.7%). The *e.g./etc.* lists in 1.1:5 and 3.1:6 each take about 2.1–3.2k. C-26 only warns, so nothing forces padding. | My judgement is that the 95–137k total is inflated by roughly 30–40% and mis-proportioned. | After F-02, fold examples into parents, then regenerate. Have the HANDOVER state that budgets are ceilings and the floor is a warning only. |
| F-14 | M | Registry members; `related_ids`/`prerequisite_ids` empty for every objective | Duplicates: "non-formal education" twice (`7.3.03-03`, `7.3.06-01`); GNP member `1.1.05-01` vs outcome 1.1.04; capitalism/communism (`1.1.02-04` vs `8.1.03-01/04`); MNCs (`3.1.12-04`, `4.1.03-04`, `9.2.02-01`); cooperatives (`3.1.12-02`, `5.1.04-02`); division of labour (`3.1.04-01`, `5.1.02-02`); infrastructure (`8.1.04-03`, `9.1.08-01`). | Repeated State/Describe cards, and inconsistent definitions are likely. | Cross-link with `related_ids`. Keep one teaching home per concept and give the other topics a distinct applied angle, or drop the card. |
| F-15 | M | 4.1:4, 4.1:5, 1.1:5, 2.2:2 members | Illustrative *e.g./etc.* items become full members with two cards each: the four NIC countries (current-classification risk), "evaluation of an NDP example" (NDP5's period has ended), housing and diet. | Optional examples become compulsory card sets, and currency risk rises. | Use one parent case-study slot with a dated example. Keep the examples in the notes, not as cards per country. |
| F-16 | M | `build_exemplar.py:128–151`; both exemplar item files | Marking guidance comes from one shared keyword dictionary and is cross-contaminated. 10.1 `002-APP` guidance says "purchase the missing productive input… working machine and missing cloth"; 3.1 `003-INTERP` cites "four confused pilot participants". The 3.1 slice has six items on one distinction. The notes themselves are sound, and every answer can be rebuilt from them. The pilot slice matches PILOT-APPLICATION-2 well. | The PUBLISH result proves schema conformity and guidance keywords, not marking quality. Authors are told to copy this shape. | Regenerate with guidance written per item. State in the README that C-16 checks keywords only. |
| F-17 | M | `build_plan.py:134` → `make_work_order.py:473` | An objective's `command_words` are computed from its own subtype map. So the work-order reason "instructs with Suggest, which this objective carries" is circular: it suggests evidence from the syllabus or corpus that does not exist. | The labels misinform the author and the reviewer. | Fill `command_words` from the syllabus verb plus the commands in that objective's mapped evidence records. |
| F-18 | M | `scope-scan.json` | The three regexes catch only their own canned sentences, and there is no ceiling on depth. The 2024 report insists on random, systematic and stratified sampling only and advises against line graphs (layout lines 931–937; line graphs also flagged in 2023). The file says "pending teacher judgement", which contradicts Jeremy's no-teacher decision. Leaving no content out is being treated as if there were no upper bound. | Authors could drift into cluster or quota sampling, HDI geometric-mean formulae, BoP sub-accounts or extra DTM stages. | Add a pattern that catches non-syllabus sampling methods. Decide on line graphs now as a practice policy based on the report. Put short depth ceilings in the contracts' depth guidance. |
| F-19 | L | `glossary_decisions.json` | "Random sampling… known selection opportunities" departs from the level-appropriate "each has an equal chance" used in the 2024 report (layout line 713). Exam-defined terms are missing: multinational company (2020 P1 3(b)(i), primary), grassroots development, baby dumping, export, rural–urban migration, subsistence farming, NIC, LEDC/MEDC, intermediate technology, cooperative, primary health care, literacy rate, DTM. All other entries I checked are accurate. | Minor inconsistency and gaps. | Reword the random-sampling entry and add the observed terms. |
| F-20 | L | `slot_plan.ao_by_objective_type['*'].MISCON=['A']` | Data-reading confusions such as MISCON-011 (highest level vs largest increase) are labelled A. | Small AO mislabel. | Label by task. |
| F-21 | L | `10.1.02-04`; `10.1.08-00` | "specific (area, time, date)" loses "date". "Define pilot study" has no DEF slot; the application-first approach is right, but the source verb still asks for a definition. | Minor scope slip. | Restore "date" and add a 1-mark DEF next to the application slots. |

---

## 4. Assessment against your ten questions

**Q1. Qualification facts: sound.**
Checked against PDF pp.19–20:
- Paper 1: 80 marks, 135 minutes, 40%. Paper 2: 70 marks, 120 minutes, 35%. Paper 3: 50 marks, 105 minutes, 25%.
- Grid: A.1/A.2 20/15 (combined); A.3 15; A.4 20; B.1 25/15/5; B.2 –/25/5; B.3 –/15/5; C 25; D 10.
- So A 35, B 47.5, C 12.5, D 5. Each mark is worth 0.5% on every paper, so summing marks gives the percentages directly.
- Per-paper AO shares in `qualification-profile.yaml` (P1 68.75/31.25, P2 21.43/78.57, P3 0/30/50/20) are correct.
- A–D definitions match p.18. No AO1–AO4 meaning is imported into any planner file; that wording survives only in standard boilerplate (S-05 below).
- The two Paper 3 statements (p.22 says C/D only; the grid adds B15) are preserved correctly.

**Q2. Decomposition and coverage.**
- Every clause I compared appears somewhere: all 102 rows, with 3.1:11 correctly folded into 3.1:12. The member lists are faithful transcriptions.
- The problems are the uniform member template (F-02), the overridden parent types (F-01), examples treated as compulsory (F-15) and duplicates (F-14).
- The 393 targets are not padded, but each one becomes exactly two generic cards. That template, not the target count, drives both volume and words (F-13).

**Q3. Commands and tariffs.**
- Every chosen pair is observed in the corpus, but commands are chosen by subtype, not by demand (F-17).
- The flashcards use effectively seven commands (State, Describe, Suggest, Explain, Discuss, Define, Calculate).
- Define/What, Identify, Differentiate, Compare and Calculate are nearly absent, and Discuss is used about 25 times more often than the corpus would suggest.
- Counting one primary command per part is *not* being over-applied: compound prompts are allowed (exemplar 3.1 `001-APP` "Suggest… Explain why"). The real problem is keyword overload at short tariffs (F-09).
- Define/State, description, explanation, data interpretation and evaluation are distinct in `SUBAOS`/`STRUCTURES`, but they are attached to the wrong outcomes.

**Q4. AO assignments.**
- Labelling research definitions C is defensible, because the Paper 3 grid has no A.
- Labelling every overview Suggest as A is not: it turns assess/evaluate outcomes into A (F-06). INTERP→B on members without data inflates B (F-03).
- Applied A.3 is reasonably represented by APP on strategy parents.
- D has 49 marks-equivalent, and the 5-point tolerance hides a 53% relative shortfall (F-12).

**Q5. Activities.**
- The 737 flashcards are coherent in format but redundant in substance: two cards per member, and six items on one distinction in the exemplar.
- All 17 content short-answer tasks are State 2 + Explain 4 and all 17 data tasks are Describe 2 + Discuss 4. They are reasonable but identical, with no Calculate.
- Each research cycle pair adds up correctly to B15/C25/D10. The four cycles are identical (F-11), and they miss the Section A two-question shape and the community-project problem (F-10).
- The AO splits are rightly labelled as planner estimates.

**Q6. Quality evidence.**
- I checked four of the seven criteria against primary pages: RELATIONSHIP-3 (2020 P1 1(a)(iv)), COMPARE-3 (2020 P1 2(e)(ii)), METHOD-APPLICATION-4 (2024 P3 1(b)(i) with the report's "2 + 2" note) and PILOT-APPLICATION-2 (2024 P3 3(a)(iv), "0 = for the meaning").
- PROBLEM-SOLUTION-2 matches the printed cap, and the cap is genuinely ambiguous.
- The patterns borrowed from other subjects have been adapted with explicit limits on what was carried over (`profile_quality_decisions.reference_patterns`). I found no imported content or rubrics.
- Glossary: accurate apart from F-19.

**Q7. Scope.** See F-18. "No content exclusion" is correct. "No upper boundary" is the gap. The report advice on sampling methods and line graphs should become plan policy, explicitly labelled as coming from the report.

**Q8. Exemplars.**
- The pedagogy is good. The pilot slice shows a trial, the difficulty found, the repair, a re-test, and the limits of a six-person pilot. The capital slice shows money capital vs capital goods through a bottleneck decision.
- Every answer can be rebuilt from the notes.
- Their checks prove claim, hash and keyword structure. They do not prove the marking guidance (F-16), coverage of whole topics, or anything about graphs (C-35/C-41/C-43 not run).

**Q9. Standard issues: handled honestly, and I found no bypass.** Verified points:
- `run_checks.py:23` exits 0 only when the decision equals `'pass'`.
- The schema discrepancy is recorded as an error, not filtered out.
- not_run is listed by id and reason.
- `standard/` is untouched as far as I could see; I did not check diffs.

One addition for the owner: the generated work orders contain AO1-style boilerplate with "None%" (`topics/1.1/work_order.md:27`).

**Q10. Handover.** Roles, checkpoints, missing sources and the not-yet-authorised status are stated clearly and honestly. But it makes the work orders authoritative, and at the scale of F-01 to F-10 that hands educational redesign to the author. The plan must be fixed first.

**What is sound:** the facts; the bridge; the honesty of GAPS and limitations; the 30 misconceptions with locators; the limits written into the answer shapes, including no one-mark-per-point rule; the sensitivity and currency rules; the rule that conditions travel with claims; the totals of the research pairs; the role and process discipline; and the pilot exemplar's teaching.

---

## 5. Who fixes what

**Codex can fix these in the plan** (planner-owned: `build_plan.py`, `registry_decisions.json`, the subject profile `slot_plan`, `performance-slot-specs.json`, the glossary, the scope scan, the exemplar builder):

F-01 through F-21. In particular:
- `slot_plan.command_words_by_subtype` accepts lists, and the generator picks the first command the objective carries (`make_work_order.py:455`).
- Objective types and `command_words` are set in the workspace.
- `subtype_waivers` and `ao_by_objective_type` exist for targeted control.

**Standard maintainer** (blocks pilot completion, not plan approval):

| ID | Issue |
|---|---|
| S-01 | `run_checks.py` exit code vs PUBLISH |
| S-02 | Subject-profile schema rejects `slot_plan`, `conditioned_mechanisms` and `depictions` |
| S-03 | C-35/C-41 support break-even charts only; no checks for pie/bar charts, sketch maps or pyramids |
| S-04 | PUBLISH is returned when checks are not_run |
| S-05 | Cambridge/AO1–AO4 and "None%" boilerplate |
| S-06 | (Advisory) C-16 checks keywords only, and C-26 budgets are proportional to objective count; both shape the incentives behind F-09 and F-13 |

**Transparent non-applicability:** C-43 not running when no practice text exists is fine, provided it stays listed.

A subject teacher or another authoring trial is not needed to resolve any of the findings above. They are resolved from the syllabus and corpus evidence already held.

---

## 6. Should Jeremy approve the plan as it stands?

**No.** The minimum changes, then regenerate and re-validate:

1. **Re-type parents and members by their actual demand.** Honour the `types` decisions and assign members by role. This fixes F-01, F-02, F-06, F-08 and F-04, adding DEF, Differentiate and Identify where the source asks for them.
2. **Relabel AOs by task and recompute.** Report each AO's relative shortfall as well as the absolute gap (F-03, F-12). Do not pad.
3. **Add numerical practice** in the data-bearing topics, and vary the data-task commands away from mandatory Discuss (F-05, F-07).
4. **Rebuild the four research cycles** around the Section A two-question shape, include community-project planning in at least two, and make the cycles genuinely distinct (F-10, F-11).
5. **Scale answer structures to tariff** (F-09). Regenerate the exemplar with item-specific guidance, or label it plainly as a structure-only demonstration (F-16).
6. **After retyping, fold *e.g./etc.* examples into parents, cross-link duplicates, and treat word budgets as ceilings** (F-13, F-14, F-15).

F-17 to F-21 should be done in the same pass but are not individually gating. Once these are done, the topic table, AO table and work orders need a fresh look before Jeremy approves and commits, but no new trial stage is needed.