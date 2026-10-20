# 6116 NSSCO Biology — corpus analysis

Written after the syllabus brief (`6116-nssco-biology-syllabus-brief.md`) and before any plan, as
the playbook requires. Evidence lives in `work/nam-6116-nssco-2026/assessment-evidence/` and the
derived curriculum files; the scripts that produced it are in that workspace's `planning/`.

**Derivation policy.** Official assessment material is mine, do not reproduce. Question stems are
quoted only inside the evidence JSON so a human can audit a mapping. No question or indicative
answer wording reaches a learner.

## 0. Two issues carried in from the syllabus stage, still open

- The denominator of *"not more than 24% recall"* is undefined in the syllabus. No interpretation
  is adopted here and nothing in this analysis depends on one.
- Paper 1's duration is unconfirmed for 2026: the syllabus says 45 minutes, the 2025 paper says
  1 hour. Both retained. This analysis does not claim a 2026 duration.

## 1. The corpus

| Source | Held | Note |
|---|---|---|
| Question papers | **18** — Papers 1/2/3 for 2020, 2021, 2022, 2023, 2024, 2025 | 2022 and 2023 are **First Proof** versions and may differ from what was printed |
| Examiner reports | **6** combined NSSCO volumes, 2020–2025 | Each carries a Biology 6116 section: PDF p.49 for 2020–2024, p.47 for 2025; 8–16 pages each |
| **Mark schemes** | **none** | DNEA does not publish them. This is the single largest evidential gap |

Set aside: nothing. All six years sit on the current (NIED 2018) syllabus.

The examiner reports print **39 indicative `Answer:` blocks** beside some questions. These are not
mark schemes — no tariff breakdown, no award grammar, no band descriptors, and present for only a
subset of parts. They are recorded as partial answer-shape evidence and labelled as such.

## 2. What each paper looks like

**Paper 1** — forty four-choice multiple-choice questions, one mark each, 40 marks. Confirmed at
exactly 40 questions in all six years, against the cover's own statement that "There are forty
questions on this paper". No glossary command word opens these.

**Papers 2 and 3** — **341 question parts carrying a tariff**. Paper 2 contributes **480 marks
across its six papers** (80 each) from 213 parts; Paper 3 contributes **240 across its six** (40
each) from 128 parts; together **720 marks across twelve papers**. Question totals are held separately so they do not
contaminate the part-tariff distribution.

**Every paper reconciles to its stated total.** All twelve structured papers were checked part-sum
against cover total: Paper 2 is 80/80 in each of the six years, Paper 3 is 40/40 in each. An
earlier pass reported 479 for Paper 2; that was an extraction defect, not a property of the papers
— a length threshold meant to discard question-total lines was also discarding the genuine part
"(ii) phagocyte [1]" (2021 Q3) because its text ran to nine characters. The test is now for absence
of words rather than shortness. The reconciliation is a standing check: a paper that does not sum
to its cover total means the extractor is wrong.

| Tariff | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|
| Parts | 118 | 124 | 50 | 38 | 9 | 1 |

**70% of parts in the sampled papers are worth 1 or 2 marks**, and the largest observed part is
6 marks.

**This is an observation about six sampled series, not a rule about the qualification.** Nothing in
the syllabus caps a part at 6 marks, and a future paper may exceed it. The claim is bounded to what
was examined in 2020-2025, two of which are First Proof versions.

**A low tariff here does not mean low cognitive demand.** Every part at 5 or 6 marks was read, and
they are the reasoning-heavy items in the subject:

| Series | Part | Marks | Demand |
|---|---|---|---|
| 2021 P2 | 4(iii) | 6 | Complete a table reasoning what was done to three seedlings, the effect on growth-substance concentration, and the result - three parallel causal chains |
| 2023 P3 | 4(b) | 5 | Design an investigation comparing vitamin C in two foods using the DCPIP test |
| 2024 P3 | 1(a) | 5 | Design an investigation into distilled water and salt solution on red onion epidermal cells |
| 2020 P3 | 3(b) | 5 | Design a food test on watermelon cotyledons |
| 2020 P2 | 8(c) | 5 | Draw a fully labelled genetic diagram, heterozygous brown-eyed x blue-eyed |
| 2022 P2 | 7(iii) | 5 | Genetic diagram for recessive hypotrichosis inheritance |
| 2021 P2 | 8(b) | 5 | Effects of nitrogen fertilisers on the environment |
| 2025 P2 | 6(ii) | 5 | Control of glucose concentration during a stated period |

Experimental design, multi-step causal explanation and genetic reasoning all appear, carried in
tariffs of 5 and 6 rather than in essays. The subject asks for reasoning in compressed form.

## 3. Command words actually used

Measured across the 340 parts. This is the rule for which words may open a generated prompt
(AGENTS.md rule 5).

| Command word | Parts | Modal tariff | Tariffs seen | In glossary? |
|---|---:|---:|---|---|
| describe | 53 | 2 | 1–5 | yes |
| **name** | 39 | 1 | 1–5 | **no** |
| explain | 35 | 2 | 1–4 | yes |
| state | 28 | 1 | 1–4 | yes |
| suggest | 25 | 2 | 1–4 | yes |
| **identify** | 25 | 2 | 1–4 | **no** |
| calculate | 19 | 2 | 1–3 | yes |
| define | 12 | 2 | 1–3 | yes |
| **complete** | 9 | 2 | 1–6 | **no** |
| discuss | 8 | 3 | 2–4 | yes |
| **label** | 7 | 3 | 1–3 | **no** |
| outline | 7 | 3 | 2–4 | yes |
| **draw** | 5 | 5 | 1–5 | **no** |
| describe and explain | 3 | 2 | 2–4 | yes |
| **distinguish** | 3 | 2 | 2 | **no** |
| list | 3 | 3 | 1–3 | yes |
| determine, measure | 2 each | 1 | 1 | yes |
| **plot** | 2 | 5 | 3–5 | **no** |
| estimate | 1 | 1 | 1 | yes |
| **indicate, find** | 1 each | — | 3–4 | **no** |

**Five glossary words never open a part in the sampled papers: `apply/use`, `compare`,
`give a reason/give reasons`, `predict`, `sketch`.**

**This governs prompt wording only. It does not remove the underlying skills from scope.** The
syllabus requires prediction (B6 "make predictions and propose hypotheses", and the glossary's own
`Predict`), comparison (A1-A2 and `Compare`), and application (`Apply/use`, and AO B throughout).
Paper 3's Annexe A criterion (j) requires planning an investigation "including making reasoned
predictions of expected results". These skills must be practised whatever word the papers happen to
use to ask for them. What the measurement settles is which word may OPEN a generated prompt - not
which skills the resource teaches. Conflating the two would strip assessable content from the
subject on a vocabulary count.

**Nine words open parts but are not in the glossary**, led by `name` (39 parts, the second most
frequent opener in the subject) and `identify` (25). The AO descriptions name most of these as
question openers even though the glossary does not define them — so the glossary is not the
operative command-word list for this subject. The papers are.

Per paper: Paper 2 is led by *describe* (39), *name* (31), *state* (20), *identify* (20),
*explain* (20). Paper 3 is led by *calculate* (16), *explain* (15), *describe* (14), *suggest* (14)
— a visibly different mix, weighted to calculation and interpretation.

## 4. What a creditable answer looks like

**This section cannot be evidenced, and that is a finding rather than an omission.**

The playbook derives answer shape from mark-scheme structure: how many distinct points, whether a
point must be developed, whether context is required, what a top band needs. **No mark scheme
exists for NSSCO 6116.** `curriculum/answer-shapes.json` therefore carries `answer_structure: null`
for all 22 command words, with the tariff behaviour that *is* measurable recorded beside it.

What can be said from the papers alone: the 1-mark part dominating the distribution implies
one creditable point per mark, and the absence of anything above 6 marks means no item in this
subject requires extended argument. Both are inferences from tariff structure, not from award
grammar, and are labelled as such.

**What may and may not be claimed.** The resource cannot state official marking rules for this
subject, because none are published. It CAN produce source-backed model answers and marking
guidance derived from the syllabus objectives, the observed tariffs and the examiner evidence,
provided every such item is labelled `proposed` and carries the evidence behind it, and provided no
item is presented as the board's own marking. `answer-shapes.json` records `answer_structure: null`
to mean "no official structure is evidenced", not "no guidance may be written"; the proposed
structures belong in the subject profile at the planning stage and are subject to review.

The 39 indicative answer blocks give a partial, non-systematic view of a subset of parts. They are
evidence worth reading before authoring and are not a substitute for the missing schemes.

## 5. Where the marks fall

Exposure is computed at **sub-topic level** into `curriculum/exam-exposure.json`, from 340 mapped
parts across 53 leaf sub-topics. It measures examined demand. It is not a card count and nothing
here converts it into one.

Heaviest by marks seen across six years:

| Sub-topic | Marks | Parts |
|---|---:|---:|
| 1.2.3 Drawing graphs and tables | 42 | 19 |
| 2.1 Classification of living organisms | 34 | 14 |
| 2.2 Diversity of living organisms | 32 | 14 |
| 3.2 Cell structure, organisation and levels of organisation | 31 | 15 |
| 4.4.2 Monohybrid inheritance | 27 | 10 |
| 1.2.6 Experimental techniques | 26 | 15 |
| 3.6.1.3 Photosynthesis | 26 | 12 |
| 3.5 Enzymes | 25 | 10 |
| 3.7 Transport in plants | 25 | 11 |

**Topic 1 Scientific processes is examined far more heavily than its size suggests.** It holds 43
of 393 objectives (11%) but *Drawing graphs and tables* alone is the most-examined sub-topic in the
subject, and *Experimental techniques* is sixth. Topic 2 Classification holds only 9 objectives yet
supplies two of the top three.

Three leaf sub-topics drew **no proposed question part in six years**: 3.6.2.1 Diet and nutrients
(6 objectives), 4.3.3 Methods of birth control and increasing fertility (3), 5.3 Population (8).
These are proposals, not confirmed absences — a reviewed mapping pass must confirm before any
emphasis decision rests on them. **Low exposure never removes coverage.**

## 6. How candidates lose marks

**261 statements** were mined from the six Biology sections and classified:

| Class | Count |
|---|---:|
| misconception | 59 |
| omission | 47 |
| spelling/terminology | 41 |
| command-word miss | 18 |
| teaching advice | 19 |
| shallow development | 1 |
| unclassified, kept only for its scoring percentage | 76 |
| **total** | **261** |

**Spelling and terminology is the surprise.** 41 statements — the third largest class — concern
candidates losing marks on spelling or imprecise terms, repeatedly on structure names. For a
flashcard resource this is directly actionable: precise terminology is the thing cards are best at
drilling, and the examiners say plainly that it is where marks go.

**What the 76 unclassified statements are.** All 76 are Paper 1 commentary that reports how
candidates performed without describing an error - "About 67% of candidates knew the correct
answer", "Many candidates found this question difficult and only 38.5% answered correctly". They
are retained because the percentage is evidence; they say nothing about failure type. 185
classified + 76 unclassified = 261.

**Classes do not overlap in the data, but they do in reality.** Each statement is assigned the
first class whose pattern matches, so every statement appears exactly once. **13 statements (5%)
match more than one class** - most often misconception with spelling/terminology, or command-word
miss with misconception - and the secondary class is currently lost. The counts are therefore
lower bounds per class, and curation should record multiple classes where they apply.

**On "shallow development = 1": that count is an artefact, not a finding.** Its patterns are the
narrowest of the six and the examiner wording here ("answers lacked depth", "candidates only
stated") largely escapes them. A single hit across 70 pages of commentary should be read as a
classifier limitation.

**Withdrawn: the earlier conclusion that "the failures are knowing and naming, not arguing".**
It is not supported, and this analysis's own evidence contradicts it. `explain` opens 35 parts and
`suggest` 25; `calculate` leads Paper 3 with 16; every 5- and 6-mark task is experimental design,
multi-step causal explanation or genetic reasoning (section 2); AO B is 28% of raw marks and AO C
25%, neither of which is recall. Category counts from examiner reports describe which errors
examiners chose to comment on. They cannot establish that reasoning is unimportant in this subject,
and the measured demand says the opposite.

### Candidate scoring percentages — EXCLUDED FROM PLANNING INPUTS

**Decision, 2026-10-17: these figures do not enter the plan.** The evidence and its limitations are
preserved below because they are real and may become usable if per-paper data improves, but no
topic-difficulty ranking derived from them feeds the registry, the contracts or the work orders.


76 statements carry a candidate-scoring percentage. **How the figures were produced:** a percentage
is taken from an examiner sentence only when that sentence also carries candidate-performance
language (scored / answered / correct / performed); it is attributed to a sub-topic by the same
distinctive-term proposal used for everything else; the "mean" is the unweighted arithmetic mean of
whatever observations landed on that sub-topic.

**Three properties make them unfit for ranking topic difficulty as presented earlier:**

| Sub-topic | n | Mean | Spread | Mapping confidence |
|---|---:|---:|---|---|
| 2.2 Diversity of living organisms | **1** | 38.5% | single point | **low** |
| 3.8.3 Defence against diseases | **1** | 39.0% | single point | medium |
| 3.9 Gas exchange in humans | **1** | 40.0% | single point | **low** |
| 1.2.4 Basic units and derived units | 18 | 48.9% | **25%-80%** | low (all 18) |
| 1.1 Mathematical requirements | 4 | 55.1% | 45%-62% | low |

1. **The three apparently hardest sub-topics rest on one observation each**, two with low mapping
   confidence. A single Paper 1 item is not a measure of a sub-topic.
2. **Every percentage comes from Paper 1.** The reports give per-question percentages for the
   multiple-choice paper and essentially none for Papers 2 and 3. These therefore measure
   multiple-choice item difficulty, not topic difficulty, and are not comparable across papers.
3. **Where n is large the mean hides the spread.** 1.2.4's 18 observations run from 25% to 80%.

**Treat all of this as provisional.** The earlier claim that 2.2 Diversity is "the sharpest teaching
signal in the corpus" rested on one low-confidence data point and is withdrawn. No emphasis
decision should use these figures until the mapping pass has run and the per-paper limitation is
accounted for.



## 7. Examiner-evidenced misconceptions

`curriculum/misconceptions.json` holds **77 raw entries**, every one citing a named examiner
statement with its report year, paper, question reference and page range. None is invented.

`curated: false` throughout. The playbook requires a curation pass to drop duplicates, fragments
and mere answering habits, and to write each one's discriminating test — the 0450 register went
from 72 raw entries to 29 real confusions. **That pass has not run**, so the 77 is a raw ceiling,
not a misconception count.

## 8. Scope

`curriculum/scope-scan.json` holds the syllabus's five stated limits with their pages: water
potential and hydrostatic pressure; nephron detail; stages of cell division; maternal and paternal
chromosome detail; endosperm production and development. Each needs its catch patterns and its
in-scope counter-examples written against the surrounding objective before the scan can run.

## 9. What this means for the plan

1. **Compressed-answer subject, in the sampled papers.** 70% of parts are 1-2 marks and the largest
   observed is 6. Item shapes should follow that distribution, but the 5- and 6-mark tasks carry
   experimental design, multi-step causal explanation and genetic reasoning, so the resource needs
   items that build those skills inside a short answer. The observed ceiling is not a syllabus rule.
2. **The operative command-word list for PROMPT WORDING is the papers', not the glossary's.** Five
   defined words never open a part in the sample; `name` and `identify` are frequent openers absent
   from the glossary. Set `use_in_prompts` from this measurement. **This does not narrow scope:**
   prediction, comparison and application remain syllabus requirements (B6, Annexe A (j), the
   glossary's own entries) and must be practised regardless of which word asks for them.
3. **Paper 3 is a different subject in miniature** — calculation and interpretation led, where
   Paper 2 is description and naming led. Its demand is specified by Annexe A's eleven criteria.
4. **Terminology precision is a scoring issue**, named in 41 examiner statements. This should shape
   card design directly.
5. **Topic 1 appears under-weighted by objective count and over-examined.** Provisional: it rests
   on the same unreviewed mapping as everything in section 5. Emphasis follows measured demand once
   confirmed, never a percentage converted into a quota.
6. **The missing mark schemes bound what the resource may CLAIM, not what it may write.** No
   official marking rule can be stated. Source-backed model answers and marking guidance labelled
   `proposed`, carrying their evidence and subject to review, are legitimate and expected.
7. **Two quality gates must close before the plan is built**, not after:
   - **Validate the mappings** that will guide emphasis. 110 of 341 parts are low confidence and
     every scoring percentage is Paper 1 only. Emphasis built on unvalidated proposals is emphasis
     built on term overlap.
   - **Curate the 77 raw misconceptions** into real confusions with discriminating tests.
   Coverage is not subject to either gate: **every mandatory syllabus objective is covered
   regardless of measured exposure.** Exposure calibrates emphasis; it never removes an objective,
   and the three sub-topics currently showing no question part stay fully in scope.

## Derivation policy

Mine, do not reproduce. 12 or more identical words copied from a paper or indicative answer into
learner-facing text is a defect; 8 to 11 is reviewed by eye and allowed only for standard
terminology, a standard definition or a formula.

## Corrections at the plan stage, 2026-10-18

Recorded here rather than by rewriting the approved text above.

- **Misconceptions (section 7).** The raw register is 89 entries, not 77, after the examiner-report
  re-scan. Curation is done: an automatic pass, then an entry-by-entry review
  (`work/nam-6116-nssco-2026/planning/misconception_review.json`). The result is **27 curated
  confusions**, each tied to one objective and carrying a written discriminating test. Two of them
  are evidenced in two series: xylem/phloem, and red/white blood cells. Three are flagged for a
  teacher. The earlier figure of 40 is superseded: it kept fragments, one word-form slip, and sides
  read off sentences by a regex.
- **Scope (section 8).** The syllabus states **seven** limits, not five. The line scan missed two
  that wrap across lines: "details of β cells are not required" (3.14) and "no reference to full
  names is required" for DNA bases (3.4). Two of the 2026-10-17 patterns would also have blocked
  required content: "water potential" is required in 3.3.2 and excluded only for tissue fluid in
  3.8.2, and "maternal and paternal chromosomes" is the wording of objective 4.1 itself. All seven
  patterns are now tested against must-catch and must-allow examples
  (`work/nam-6116-nssco-2026/planning/scope_patterns.json`).
- **Command words (section 3).** The table above is unchanged. The plan applies the repo's rule:
  a word may open a prompt if it opens at least one part (`used_at_level = observed_count > 0`,
  `standard/v0.2.0-draft/mine/assemble.py:144`). That gives 22 words. An earlier draft plan
  required two observations; that was our own heuristic, not a repository requirement, and it is
  withdrawn. Estimate, find and indicate open one part each and are marked as thin evidence.
- **Objective count.** The transcription was redone from word positions in the PDF. 364
  syllabus bullets decompose into **540 assessable objectives**. Sub-topics 4.1 and 4.2.1 had
  collapsed into two run-on bullets; three 3.6.2.3 bullets were split mid-sentence; topic-heading
  fragments such as "of teaching time)" had been registered as objectives.
- **Command-word counts (section 3), re-mined 2026-10-18.** The miner recorded the first glossary
  word found anywhere in a stem, and kept only the innermost reference level. Both are fixed
  (`work/nam-6116-nssco-2026/assessment-evidence/GAPS.md`). Recounted from the repaired records:
  describe 52, name 39, explain 39, state 34, suggest 28, identify 22, define 12, draw 10, complete
  10, calculate 9, give a reason 9; draw's modal tariff is 4, list's 2. The table in section 3 is
  superseded by `curriculum/answer-shapes.json`. Glossary words that open no part: apply/use,
  compare, predict, sketch. "Give a reason" does open parts once its slashed form is read.
