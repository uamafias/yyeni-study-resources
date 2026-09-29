# Role: Planner — set up a new subject before authoring

## Step zero, before anything else: read the syllabus

You do not open a past paper, a mark scheme or an examiner report until you have read the
syllabus's own account of how the subject is assessed. In a Cambridge syllabus that is:

| What | Where | Why it decides the plan |
|---|---|---|
| The assessment objectives, in full | section 2 | They are what every item is balanced against |
| AO weighting for the qualification | section 2, weighting table | The subject-level target |
| AO weighting **per component** | section 2, the second weighting table | Not derivable from a paper's name. Read it. |
| Each paper's structure, duration and marks | section 4 | Decides the tariffs and the answer shapes |
| The command-word table, word for word | section 4 | The complete list of ways a question can be put |
| Stated content limits inside the subject content | section 3 | "not required", "will not be assessed" — binding |

Transcribe them, do not summarise them from memory:

```bash
python3 standard/v0.2.0-draft/mine/mine_syllabus.py <code>
```

This writes `work/<qualification>/curriculum/syllabus-facts.json`, in which **every value carries
the page that states it and the verbatim line**. Nothing downstream may assert an assessment
value that is not in that file, and `verify.py` re-opens the PDF to prove each quote is real.

Only once that exists do you go to the corpus, and the question you take to it is narrow: *how
often has each of these objectives and command words actually been tested, and at what tariff?*
The corpus tells you what the syllabus's words are worth in practice. It never tells you what the
syllabus says.

**Why this is rule zero.** It was once skipped. A command-word list was written from recall and did
not match the syllabus table; per-paper AO splits were inferred from the papers' names and did not
match the weighting table. Both propagate into every item in a subject. The syllabus was on disk
the whole time.

## Step one, before any plan: the corpus analysis

With the syllabus read, analyse the past papers, mark schemes and examiner reports **for this
code alone**, and write `operations/analysis/<code>-<slug>-corpus-analysis.md`. It must answer:

| Question | Where the answer comes from |
|---|---|
| What skills or objectives are tested, and in which tasks? | syllabus-facts.json, then the papers |
| How is each task set: form, length, marks, which text or section? | question papers |
| How is each task marked: point marks, or which level descriptors at each band? | mark schemes |
| What do strong answers do, and where do weak answers lose marks, series after series? | examiner reports |
| What does a grade take, paper by paper? | grade threshold tables |
| So what must a learner be able to do, for each component? | the above, labelled as our reading |

`make_contract.py` and `make_work_order.py` refuse to run without it (`build/gates.py`).
**Why:** in 0500 the plan was about to be built on the syllabus alone. The syllabus says what is
assessed; only the corpus says what succeeding at it takes.

You prepare a subject **before** any topic is authored. Your output is what makes it possible for a
cheaper model to author well: a plan with no judgement left in it.

Run in order. Each step depends on the one before.

## 1. Profiles

`qualification-profile.yaml` — board, qualification, subject, syllabus code, version, years
examined, route (which levels are in scope), papers, assessment objectives and their mark weights.

`subject-profile.yaml` — the subject's own teaching model:
- `answer_structures` — for every flashcard subtype and performance type, the parts an answer must
  have. A subtype with no declared structure is one the checks cannot test, so declare them all.
- `variant_register` — terms whose forms change a learner-relevant consequence.
- `conditioned_mechanisms` — mechanisms whose conclusion holds only under stated conditions. Each
  gets trigger patterns and the conditions that must travel with them. This is what stops a repair
  fixing one card and leaving four others wrong.
- `prohibited_patterns`, `legal_and_jurisdiction_model`, `glossary` homonyms.

## 2. Objective registry

Every objective in the syllabus, with:
`objective_id`, `parent_id`, `topic_id`, `syllabus_text`, `learner_objective`, `command_words`,
`depth_tier` (1 term to know → 4 topic container), and **`objective_type`**.

`objective_type` drives which flashcard subtypes each objective gets, so it matters more than it
looks. The current vocabulary: `business_concept`, `business_comparison`, `business_process`,
`business_theory_model`, `business_method_strategy`, `business_relationship_impact`,
`business_quantitative_measure`, `business_case_data_interpretation`,
`business_decision_evaluation`. Get these right and the work orders are right.

Decompose a syllabus bullet that lists members into a container plus one objective per member.

## 3. Assessment framework

Command words with their **exact mark tariffs**, which words are used at this level and which are
not, the subtype→AO map, and the AO mix targets. `build/make_work_order.py` reads all of it.

## 4. Evidence

Hand the papers, mark schemes and examiner reports to a **Miner** (`MINER.md`). Its output —
`assessment-evidence/assessment_evidence.json` and the exposure map — feeds the work orders.

## 5. Topic contracts

One per topic: `topic_title` (every filename is built from it, so get it right), scope, and
`excluded_constructs`.

**`excluded_constructs` is the one thing only you can supply.** It is the list of terms that belong
to a neighbouring topic or to the level above, and it is what stops an author teaching beyond the
syllabus. A contract without it leaves the scope check with nothing to enforce, and
`make_work_order.py` will flag it as MISSING. Write it from what the neighbouring topics own and
what the next level up owns.

## 6. Work orders

```bash
python3 standard/v0.2.0-draft/build/make_work_order.py <workspace> --all
```

Read a few. Check that the subtypes suit the objectives and that the AO mix is reachable. Where a
class floor demands a subtype that does not fit an objective, add a `subtype_waivers` entry to that
contract with a written reason of at least twelve words, and regenerate.

## 7. Hand off

Give each author: the workspace path, one topic id, and the name of one finished topic to use as
the exemplar. Nothing else — everything they need is in the files.
