# Independent Step 6 review: 6136 NSSCO Development Studies (Grades 10–11)

**Reviewer:** Claude Code (Opus 5.5), read-only, 2026-10-20. **Author:** Codex. **Workspace:** `work/nam-6136-nssco-2026/` (uncommitted).
**Constraints honoured:** no edits, publishing, commits, imports, web research, subagents or script execution. Because edits were off, no `operations/review/*.yaml` file was written; this report is the record.

## Verdict: FIX CONTENT BEFORE PUBLICATION

The build should not be published or released to learners as it stands. I found no inverted causal mechanism and no arithmetic error in any worked figure I recomputed (all of them). The research packages handle the learner's own enquiry honestly.

The blockers are omissions and exam-readiness defects that a learner would pay for in marks:

- **Untaught, examined content:** Vision 2030 is never defined, and that definition was examined in 2020. The Harambee Prosperity Plan never appears anywhere for learners, yet it is named in the syllabus and was examined in 2022.
- **A replaced syllabus term:** "baby dumping" is replaced throughout by "infant abandonment", and its examined definition, types and factors are not taught. This is an unrecorded deviation from `glossary.json`.
- **Methods missing behind cards:** cards require percentage change and natural increase, but no notes teach either method.
- **A systemic breadth deficit:** the notes teach one conditioned mechanism per concept, while Papers 1 and 2 repeatedly reward several distinct points ("Any 3/4/5").
- **Templated cards:** 72 items have templated prompts whose answers are pasted note paragraphs.

All of these can be repaired within the existing slots and labels, so the playbook's "fix the plan first" label is not required to start repairs. I also found five plan defects (below) that caused several of the content defects. They should be routed to the planner, but they do not have to be resolved before content repair.

Status facts I confirmed: all 717 claims are still `unverified` / `publishable: false`, all items are `review_required`, and nothing here is an independent truth approval.

---

## Coverage: what I actually read

All 30 syllabus PDF pages were read first.

| Topic | Rendered notes | Cards read (prompt + answer) | Inspected in depth | Limits |
|---|---|---|---|---|
| 1.1 | Full (3,447 w) | 34/34, incl. guidance | 017-EVAL, 032-MISCON, P01, P02 | — |
| 1.2 | Full | 10/10 | 005-EVAL, 007/008-MISCON, P01, P02 | Guidance not read for all |
| 2.1 | Full | 4/4 | All | — |
| 2.2 | Full | 8/8 | 004-EVAL, P01, P02; claim CLM 2.2 (NDP5) | `source-check.json` not opened |
| 3.1 | Full (5,848 w) | 75/75 | 066-EVAL, 068–073 MISCON, P01, P02 (guidance) | Guidance read only for P02 |
| 4.1 | Full | 31/31 | 010–017 EVAL, P01, P02 | — |
| 4.2 | Full | 28/28 | 022, 025, 026, P01, P02; CLM-6136-4.2-04-00-02 and `authoring-history/claim-repairs.json` | — |
| 5.1 | Full | 58/58 | 024–030 EVAL, 055/056 MISCON, P01, P02 | — |
| 6.1 | Full | 19/19 | 011-EVAL, 012, P01, P02 | — |
| 6.2 | Full | 27/27 | 018–025, P01, P02; `authoring_notes` | — |
| 7.1 | Full | 35/35 | 011-CALC, 021-EVAL (C-20), 027, P02 | — |
| 7.2 | Full | 16/16 | 003-CALC, 014-MISCON, P02 | — |
| 7.3 | Full | 27/27 | 006-EVAL plus `authoring_notes` deviation, P02 | — |
| 8.1 | Full | 25/41 (001–024, 039) | 039-MISCON | 025–038, 040, P01, P02 not read |
| 9.1 | Full | 22/34 (001–020, 031, 032) | 006/009-CALC, 031/032-MISCON | 021–030, P01, P02 not read |
| 9.2 | Full | 20/20 | 017/018-MISCON, P02 | — |
| 9.3 | Full | 8/8 | All | — |
| 10.1 | Full | 64/64 flashcards plus **all four packages P01–P04 in full, including guidance** | Every subpart tariff and figure recomputed | — |

**Other material I read:**
- `STATUS.md`, `HANDOVER`, `BUILD-INDEX.md`, the whole of `authoring-progress.json` and `topics/audit_build.py`.
- `review/copied-wording.md` and `operations/tools/check_copied_wording.py`; `GAPS.md`.
- Corpus analysis §§3–6.
- Parts of `answer-shapes.json`; `misconceptions.json` entries 001, 006, 009, 025, 026, 029 and 030.
- `slot-demand-specs.json` for slots 1.1-016/017/018; four work-order slots.
- `CLAUDE-PLAN-REVIEW-ACTIONS.json` F-01 to F-05; `standard-compatibility.json`; the status line of `revision-validation.json`.
- The 10.1 qa_report (partial) and the 4.2 qa_report (C-30).
- `authoring_notes` for 4.2, 6.2, 7.3 and 10.1.
- Claim-ledger greps for 2.2, 4.2, 7.1 and 9.3.
- Targeted examiner-report passages (2020, 2022, 2023, 2024) and Paper 3 Section B stems (2021, 2024).

**Not read (an honest limit):**
- `qualification-profile.yaml`, `subject-profile.yaml`, the full `PLAN-6136`.
- `syllabus-facts.json`, `objective_registry.json` (grep only), `performance-slot-specs.json`, `assessment-framework.json`, `scope-scan.json`, `quality-evidence.json`.
- `source-manifest.json`, `assessment_evidence.json`, `CLAUDE-PLAN-REVIEW.md`, `CODEX-PLAN-REVIEW-FIXES.md`, the contracts.
- The primary paper PDFs; I used the saved extracts instead.
- Most content-unit JSON files individually. Their text is what the rendered notes are built from, and I read all of those notes.

The learner-content reading the brief requires is complete. Plan-file inspection was sampled, not exhaustive.

---

## Findings: content repairs

Every finding is open (fixed = false). Severity follows REVIEWER.md, with omissions of examined syllabus content rated by their mark consequence.

| ID | Sev | Location / IDs | Observed defect | Evidence | Learner consequence | Concrete repair | Conf. |
|---|---|---|---|---|---|---|---|
| R6136-001 | High | 2.1; CU-6136-2.1.01; OBJ-6136-2.1.01-00; ITEM-6136-2.1-001…P02 | Vision 2030 is never defined. There is no 2004 baseline and no statement of its overall goal; the notes call it "the long-term development context" only. | `2.1-namibia-vision-2030.md:11`. 2020 P2 asks "What is Vision 2030? [1]". The 2020 report (extract lines 396–403) says candidates missed key words such as "plan"/"development". | Loses a directly examined definition mark. Cannot frame the five areas. | Add a short definition block (framework from 2004 to 2030; aim of improved quality of life and development) and make one card require it. | 0.9 |
| R6136-002 | High | 2.2; CU-6136-2.2.02; OBJ-6136-2.2.02-00 | The Harambee Prosperity Plan appears in no learner-facing text (it exists only in curriculum/work-order files). No card evaluates the real NDP5; all evaluation is fictional. | Syllabus p.6. 2022 P2 Q1(a) examined HPP's aim, launch year/president and pillars; the 2022 report (extract line 389) notes failure to name the president. | Cannot answer recall parts on HPP or evaluate a real NDP. | Add a dated, sourced HPP block (2016 launch, aim, pillars) and one item evaluating NDP5 or HPP goals against evidence types. | 0.85 |
| R6136-003 | High | 6.2; CU-6136-6.2.05/06; ITEM-6136-6.2-018…025; OBJ-6136-6.2.05-00/-02, 6.2.06-00/-02; `curriculum/glossary.json:371` | The syllabus and glossary term "baby dumping" is replaced throughout by "infant abandonment". This deviation is not in `authoring_notes`. The examined definition criteria ("without care / exposing to danger or death"), the types of GBV, and the usual contributing factors and effects are not taught. | 2022 report (extract lines 109–182). Handover rule 4 ("use glossary.json consistently"). | Will not recognise the exam term. Cannot meet the definition criteria. Under-scores the factor and solution lists. | Use the syllabus term with the glossary definition (the synonym can be noted). Teach types, factors and effects sensitively, with no stereotyping. Record the deviation if any wording is kept. | 0.9 |
| R6136-004 | High (systemic) | All topics, especially 3.1 privatisation, 5.1 schemes and cooperatives, 7.1 growth trends, 7.3 traditional/modern education, 9.3 SADC/SACU, 4.1 NIC state role, 10.1 collection methods, 1.1 GNP limitations, 7.1 pyramids | Breadth deficit: notes give one conditioned mechanism per concept. Specific gaps: 7.1 teaches no reasons for high or low birth and growth rates. 1.1 GNP limitations omit subsistence and informal output. 9.3 gives no actual successes or challenges. 10.1 gives no advantage/disadvantage sets for methods. 1.2 never names the SDGs or SDG 12. | Report answer lists, e.g. 2024 report lines 144–164 (cooperatives, schemes), 2022 report lines 96–99 (privatisation), 2021 report lines 351–358 (population). | Under-scores on AO A (35% of marks) and on 3–5-mark "advantages/reasons/solutions" parts. | For each affected objective add a concise set of 3–6 distinct, accurate points within the unit ceilings, keeping the conditions. Do not pad. | 0.85 |
| R6136-005 | High | 7.2: ITEM-6136-7.2-003-CALC, ITEM-6136-7.2-014-MISCON (MISCON-6136-030); 7.1: ITEM-6136-7.1-011-CALC | Cards require percentage change (difference ÷ original × 100) and natural increase (CBR − CDR, with ‰ → %). Neither method is taught in any notes; 1.1 and 4.2 only warn against confusing percentage change with percentage points. | Grep of all notes. MISCON-030 is report-evidenced (2024). | Cannot answer these cards from the notes. A report-documented error goes untaught. | Add a worked percentage-change block (7.2 or 1.1) and a natural-increase block in 7.1, including 20‰ = 2.0%. | 0.95 |
| R6136-006 | Medium | 72 items, e.g. ITEM-6136-6.2-020 ("concerning gbv-related factors"), 9.1-017 ("aspects of nic patterns"), 10.1-031 ("relevant to choose methods"), 6.1-003 ("Describe two aspects of labour."), 7.1-024; also 5.1-014/015, 10.1-024/026/028/030 | Templated prompts. Answers paste the notes paragraph, including advice sentences, instead of two discrete points. "Reason or limitation" cards are answered with a definition. Counts: 5.1 24, 10.1 14, 6.2 9, 9.1 8, 7.2 6, 3.1 4, 7.1 4, 6.1 3. | Item files; compare 5.1 answer 014 with `5.1-rural-development.md:67`. | Confusing prompts. Learners rehearse prose that would not earn the "two features" marks. | Rewrite each prompt naturally with its subject. Give two creditable, separable points per answer. | 0.9 |
| R6136-007 | Medium | ITEM-6136-4.2-022-INTERP; `4.2-urbanisation.md:131` (CU-6136-4.2.05) | Internal contradiction: the population is "100 people available for and seeking more work" but includes 30 who "have their desired hours". The answer uses "70" for two different groups. | Item prompt and answer. | Confuses the unemployment / underemployment / employed distinction this card is meant to teach. | Define the population as people available for work and keep each group distinct (30 + 40 + 30), relabelling consistently. | 0.95 |
| R6136-008 | Medium | EVAL items, e.g. 7.3-006, 7.3-018, 7.3-020, 7.3-022, 9.2-005, 5.1-024, 7.1-018, 7.1-030, 7.2-011, 6.2-010 | Pseudo-evaluation: one option lacks a stated necessity, so the stem decides the judgement. Four-mark answers run about 30–45 words. 7.3-006 also never carries out its "describe" component. Genuine trade-offs do exist in 3.1-066, 4.1-011, 4.1-014 and 4.1-017. | Item text; syllabus AO B.3. | Under-trains weighing alternatives (B.3) and conditioned judgement. | Give both options real merits and costs, require explicit weighing and a conditional judgement, and expand the answers to tariff. | 0.75 |
| R6136-009 | Medium | 4.1 (key industries in Namibia, NIC state role), 5.1 (schemes "used in Southern Africa"), 6.1 (colonial impacts), 6.2 (women in liberation), 9.3 (SADC/SACU successes and challenges; EU) | The no-current-facts caution is over-applied. The syllabus asks for Namibian and Southern African context, but none is named (e.g. resettlement/land reform, conservancies, contract and migrant labour, actual SACU revenue-dependence issues). | Syllabus pp.9–16. The 2024 report mentions conservancies and resettlement. | Generic answers where "with reference to Namibia/SADC" is required. | Add established, dated, non-statistical examples, verified under handover rule 7 where they are current. | 0.75 |
| R6136-010 | Medium | 7.2; OBJ-6136-7.2.01-00, 7.2.02-00 | No disease content at all (no malaria or water-borne diseases), and immunisation is not explained, although the syllabus lists "freedom from disease" and "immunisation". | 2022 report (extract lines 517–521): malaria cause examined. | Cannot answer basic disease questions. | Add a concise disease, prevention and immunisation block. | 0.7 |
| R6136-011 | Medium | 10.1 P01–P04, Section B canonical answers; 10.1 notes | The fictional Section B models are clearly labelled, and the prompts say "do not invent fieldwork". However, each is a ready-made, internally consistent enquiry stored as a canonical answer for spaced repetition, which invites memorising it. There is no template in the notes for logging the learner's own enquiry. | `topic_10.1_items.json:2766–3002`. | Risk that fictional fieldwork is reproduced as the learner's own in Paper 3 Section B. | Make the Section B canonical answers fill-in scaffolds that point to the learner's own record. Keep the fictional model separate and marked. Add an own-enquiry record template block. | 0.7 |
| R6136-012 | Low | `10.1-research-skills.md:239` | Notes refer to "the Omi source in Package 1", "Package 2" and "Package 3", but those packages exist only as items. | Notes text. | A learner reading the notes alone hits dangling references. | Give the data inline or cite the item IDs. | 0.9 |
| R6136-013 | Low | ITEM-6136-10.1-P02, P03 | P02: "resource-use shares" never says what the whole is, so A2(4) asks for a relationship from one period's composition. P03: the 12 travel-mode journeys are not tied to the 5 sampled schools. | Package stems. | Weak data–question coherence in a model of good method. | Define the whole (e.g. share of production cost) and link the journeys to the sample. | 0.7 |
| R6136-014 | Low | `1.1-development.md:103`; ITEM-6136-1.1-017-EVAL; 1.1-P02 | "GNP per person" is applied to sub-national areas H and J. P02 says "reduce unsafe-water access", which is ambiguous. | Notes and item text. | Minor conceptual sloppiness about a national aggregate. | Use "average income per person" for areas; reword to "reduce the share lacking safe water". | 0.7 |
| R6136-015 | Low | 5.1 (8 units), 10.1 (12), 7.3, 9.1, 7.2, 6.x | Identical "Connect the ideas" boilerplate in every unit. The same scenarios recur across topics: 160/100 trees (1.2 and 5.1-034); the 30→10 storage loss (4.1, 5.1-038, 5.1-P02); a blocked road or bridge (1.1, 5.1, 9.1, 9.3 three times); a missing input (3.1, six times). | Notes and items. | Word budget spent on repetition; one reasoning template is over-drilled. | Delete repeated boilerplate and vary the contexts. | 0.85 |
| R6136-016 | Low | ITEM-6136-9.1-031 (MISCON-009), 9.2-017 (MISCON-026), 9.2-018 (MISCON-029) | These restate the definitions rather than discriminating the confusion in a new scenario. | `misconceptions.json` `how_to_use`. | Weaker diagnosis of the actual confusion. | Add a short scenario that applies the separating test. | 0.85 |
| R6136-017 | Low | e.g. NDP5 claim (2.2, ledger line 72), China and Singapore claims (7.1, lines 639/681), SACU (9.3) | Externally sourced facts carry `provenance: generated_gap` and `evidence: []`. Their sources exist only as links in the note prose (and `2.2/source-check.json`). | Claim ledgers. | Traceability gap at truth review. | Fill in evidence locators and check dates. | 0.9 |

**Confirmed errors versus judgements:**
- Confirmed errors: R6136-005, 007, 012, and the omissions in 001/002/003 (absence verified by grep).
- Judgements about severity and adequacy: R6136-004, 008, 009 and 011.
- Factual accuracy: the real-world facts I checked from my own knowledge look correct (NDP5 2017/18–2021/22 and its four goals, China's 2015 change, Singapore's 1987 change, SACU membership, IMF role). This was not verified against sources.

## Plan defects (route to the planner)

| ID | Defect | Evidence | Effect |
|---|---|---|---|
| PL-1 | The slot-demand specs steer away from multi-point answers. EVAL specs say "not a generic advantage list", and no slot asks for listed advantages, limitations or reasons for objectives such as OBJ-6136-1.1.04-00 (GNP limitations), 7.3.02-00 and the 10.1 "evaluate advantages and disadvantages of data collection methods". | `slot-demand-specs.json:451–461`; the corpus "Any n" report answers | Root cause of R6136-004 |
| PL-2 | Member objective titles were generated from templates ("Describe the relevant characteristics or role of X", "Explain one reason or limitation relevant to X"). This repeats the earlier plan-review finding F-02 in a new form. | `5.1/work_order.md:45–46`, 6.2 lines 58–59 | Root cause of R6136-006 |
| PL-3 | Illustrative "e.g." members (HPP; NIC country roles) were folded away even though they had exam exposure (2022 P2). | `2.2/work_order.json:65` | Contributes to R6136-002 |
| PL-4 | The compound "Describe and evaluate" command (one observed 4-mark use) is attached to OBJ-6136-7.3.02-00, which asks only to describe advantages and disadvantages. It also conflicts with the C-14 blacklist. | `7.3/work_order.json:392–406`; `7.3/authoring_notes.json` | Distorts ITEM-6136-7.3-006 (R6136-008) |
| PL-5 | The CALC slots added under F-05 had no matching requirement for the notes to teach the method. | F-05 implementation note | Contributes to R6136-005 |

---

## Standard and tool limitations (not content defects)

| ID | Limitation |
|---|---|
| T-1 | C-35, C-41 and C-43 are `not_run`, not PASS. C-35's message ("No graphical task in this topic") is **false for 10.1**: P01 A1(7) bar chart, P02 A2(3) divided rectangle, P03 A1(6) pie, P04 A1(6) sketch map. It is also false for 7.1 (pyramid construction block). I verified the graph specifications by recomputation only; no rendered figure was verified. |
| T-2 | `audit_build.py:70–81` "independent numeric checks" are hard-coded arithmetic literals that never read the item text. Lines 63–68 take package section marks from the **plan spec**, not the authored items. I recomputed them from the authored subpart text (see Q6). |
| T-3 | `run_checks.py` exits 1 while the JSON decision is `publish`. The subject-profile schema rejects `slot_plan`, `conditioned_mechanisms` and `depictions`. Both are open with the standard owner; `standard/` is unchanged. |
| T-4 | C-18 measures AO share by item count. "C:0, D:0" in 17 topics is a counting artefact. D-labelled demand appears only in the 10.1 packages: the A2 community-project subparts are genuine problem-solving, and many "Suggest" cards elsewhere are D-like but labelled A. The planned D relative shortfall of 25.22% stays documented; metadata cannot establish real demand. |
| T-5 | The C-20 warning on ITEM-6136-7.1-021-EVAL is low concern. Its conditional reasoning is sound: the subsidy addresses cost, leaves the hours barrier, and the answer does not guarantee more births. The four-mark answer is short. |
| T-6 | C-26 advisory minima: I did not count these as failures. The adequacy problems are reported in substance (R6136-004/009/010). |
| T-7 | The copied-wording tool checks exact runs of 8 or more words only. The report extracts cover the relevant sections, not the whole reports, and the tool cannot detect paraphrase or structural borrowing. |

---

## Step 6 questions

**1. Checks.** I could not execute scripts; every run is attributed to Codex.
- `authoring-progress.json` records 18 of 18 topics with JSON decision publish, zero failures, `what_to_fix` exit 0 and runner exit 1. The 10.1 `qa_report.json` agrees: 39 pass, 2 warn, 3 not_run.
- Warnings: C-18 in all topics; C-26 in 1.1, 2.2, 3.1, 4.1, 4.2, 5.1, 6.1, 6.2, 7.1–7.3, 8.1, 9.1–9.3 and 10.1; C-20 on 7.1-021.
- Unavailable checks: C-35, C-41 and C-43, in all topics.

**2. Completeness.** `audit_build.py` compares item ID, AOs, Bloom level, command, tariff, subtype, objective and misconception ID for every slot and reports no mismatches.
- My own spot-checks of 1.1-017, 5.1-024, 7.3-006 and 9.2-018 against the work orders all matched.
- All 30 MISCON entries map to exactly one item.
- Recorded deviations: advisory minima (all topics) and 7.3's command wording.
- Unrecorded deviation: the 6.2 terminology substitution (R6136-003).

**3. Copied wording.** `review/copied-wording.md` records Codex's scan of 40 raw and layout extracts (syllabus excluded): zero runs of 8+ words and zero of 12+.
- The method is exact 8-gram matching over prompts, answers, guidance and unit blocks; the package subparts are included because they sit inside prompts.
- I found no suspicious passages. The Section B commands and the A2 project structure echo exam structure at the level of generic research verbs, not copied phrasing.
- A clean scan does not prove semantic originality (T-7).

**4. Level and scope.**
- Nothing above NSSCO level: HDI and MPI calculation, nuclear physics and company law are explicitly excluded.
- Required content missing: R6136-001, 002, 003, 004, 009 and 010.

**5. Truth.**
- No inverted mechanisms found. Examples I checked: share versus count (4.2), falling growth rate with rising population (7.1), sector share versus count (3.1), and an investment inflow versus the goods balance (9.1).
- Conditions are generally carried: the pump-repair, tourism retention and joint-venture cards all state their conditions.
- Cross-references between topics are correctly numbered, apart from the dangling package references (R6136-012). The internal contradiction is R6136-007.
- The 4.2 claim revision (CLM-6136-4.2-04-00-02, revision 2) is consistent downstream. The before-text is preserved in `authoring-history/claim-repairs.json`, the notes block matches revision 2, and `reviewed_unchanged` records exist on CU-4.2.04 blocks and the affected items. The original wording negated a guarantee rather than asserting one, so the change is harmless.

**6. Numbers and drawings.** Every worked figure I met recomputes correctly. That covers the 1.1 differences and per-person divisions (N$20,000 / N$10,000 / N$30,000), HDI/MPI differences (0.17 / 0.16), sector shares, average cost N$6 → N$3, and all urbanisation shares.
- 10.1: systematic indices 3…58; stratified allocation 8/4; pie angles 180/90/90°; divided-rectangle lengths 8/7/5 cm (boundaries at 8 and 15); funding gaps N$400 and N$60; 3/12 = 25%; litter change 18 − 30 = −12.
- 7.1 pyramid tables both sum to 100%.
- Package tariffs from the authored subpart text:

| Package | A1 | A2 | B | Total |
|---|---|---|---|---|
| P01 | 25 | 10 | 15 | 50 |
| P02 | 20 | 15 | 15 | 50 |
| P03 | 25 | 10 | 15 | 50 |
| P04 | 25 | 10 | 15 | 50 |

  Note: P02 is **A1 20 + A2 15**. That matches the plan spec but not the "25 + 10 for each package" assumption in the brief. The syllabus only fixes Section A at 35 and B at 15.
- All drawing specifications are feasible (separated bars; north-up schematic map). They are written specifications only, not verified figures.

**7. Misconceptions.** All 30 have slots. 27 genuinely test the confusion; three only restate the definitions (R6136-016). MISCON-030's card discriminates correctly but depends on a method the notes never teach (R6136-005).

**8. Learner test.** Most definition, interpretation and calculation cards can be answered from the notes. The exceptions are the cards in R6136-005 and the templated cards in R6136-006, whose answers go beyond what a two-point prompt implies. The two explicit tests are below.

---

## Explicit learner tests

**Test A: OBJ-6136-6.2.05-00 / 6.2.06-00 (GBV and baby dumping), modelled on the 2022 P1 report structure of about 18 marks.**
- What the exam expects: a definition of baby dumping with "without care / danger or death" [1]; reasons [3]; effects [3]; types of GBV [2]; factors [3]; solutions [5].
- Answering from the notes alone:
  - Definition: the notes never use the term, and "infant abandonment" is defined without the key criteria. About 0/1.
  - Reasons: "crisis, fear, stigma, coercion, isolation" earns perhaps 1/3. Unwanted pregnancy, fear of not continuing studies and contraception knowledge are absent.
  - Effects: not taught, 0/3.
  - Types of GBV: not taught, 0/2.
  - Factors: "unequal power, norms tolerating abuse" earns about 2/3.
  - Solutions: "education, safe reporting routes, survivor-centred support" earns about 2–3/5.
- **Estimated 5–6 of 17 marks. Fails.**

**Test B: OBJ-6136-5.1.04-00 (rural schemes in Southern Africa), modelled on 2024 P1 Q2: cooperative advantages [4], list of schemes [4], plus an implementation-problems evaluation (about 4–6).**
- Schemes list: the notes name loans/credit, cooperatives, resettlement, integrated development, grassroots and appropriate methods, so 4/4.
- Cooperative advantages: "pooling storage, purchases or marketing … improve access and bargaining" gives about 2–3/4. Credit access, extension advice and transport savings are absent.
- Problems: one sentence per scheme supports about 2–3 developed points. No Southern African example is available.
- **Estimated 9–11 of 14. Borderline:** recall is strong, applied evaluation and regional reference are weak.

**Positive check: OBJ-6136-10.1.12-00 (recommendation with an implementer, RECOMMEND-3).** The notes and ITEM-6136-10.1-055/056 directly teach a feasible action plus a named implementer. A learner could earn 3/3 on their own enquiry. The research method strand is the strongest part of the subject.

---

## Repair priority for Codex

1. R6136-003, 001, 002, 005: add the untaught examined content and methods.
2. R6136-004 and 010: add concise multi-point teaching sets.
3. R6136-006 and 007: rewrite the 72 templated prompts and fix the 4.2 contradiction.
4. R6136-008, 009, 011: strengthen the EVAL items, add regional context, and convert Section B to scaffolds.
5. The low-severity findings.

Then re-run the checks, restamp with claim-revision trails, and request a focused re-review of the changed items only. Route PL-1 to PL-5 to the planner, and T-1 to T-4 to the standard owner.
