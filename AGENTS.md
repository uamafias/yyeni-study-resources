# YYeni Study Resources — start here

You are working inside the repository that produces YYeni's learner notes and flashcards from
official syllabuses, past papers and examiner reports.

**Read this file, then read exactly one role brief below. Do not read the others.**

Whoever started you should have told you your **role** and your **workspace**
(`work/<qualification>/`). An author takes the whole subject and works through every topic in one
run. If either is missing, ask before doing anything.

**One syllabus code, one set of documents.** Every plan, handover and analysis belongs to exactly
one syllabus code and is named for it. An agent working 0450 never needs a file belonging to 0455,
and no document is written as a comparison between two subjects. Subjects are commissioned together
and shipped separately.

| Syllabus | Workspace | The plan you work to |
|---|---|---|
| Cambridge IGCSE Business Studies 0450 | `work/cie-0450-igcse-2026/` | `PLAN-0450-igcse-business-studies.md` |
| Cambridge IGCSE Economics 0455 | `work/cie-0455-igcse-2026/` | `PLAN-0455-igcse-economics.md` |
| Cambridge IGCSE First Language English 0500 | `work/cie-0500-igcse-2024-2026/` | `PLAN-0500-igcse-first-language-english.md` |
| Cambridge AS Business 9609 | `work/cie-9609-as-2026-2028/` | `standard/v0.2.0-draft/AUTHORING_BRIEF.md` |
| Cambridge AS Computer Science 9618 | `work/cie-9618-as-2026/` | `PLAN-9618-as-computer-science.md` |
| Cambridge AS Physics 9702 | `work/cie-9702-as-2025-2027/` | `PLAN-9702-as-physics.md` |
| Cambridge IGCSE Geography 0460 | `work/cie-0460-igcse-2025-2026/` | `PLAN-0460-igcse-geography.md` |
| Cambridge AS English Language 9093 | `work/cie-9093-as-2024-2026/` | `PLAN-9093-as-english-language.md` |

Each workspace also holds `HANDOVER-<code>-<slug>.md`, the prompt an operator pastes into a harness
to start the run. The evidence behind a plan is in `operations/analysis/<code>-<slug>-corpus-analysis.md`. That analysis is written after the syllabus is read and before any plan; the build tools refuse without it.

| Your role | Read this, and only this | Typical model |
|---|---|---|
| **Author** — write a whole subject's notes and flashcards | `standard/v0.2.0-draft/roles/AUTHOR.md` | open weights |
| **Planner** — set up a new subject before authoring | `standard/v0.2.0-draft/roles/PLANNER.md` | frontier |
| **Miner** — turn papers, mark schemes and examiner reports into evidence | `standard/v0.2.0-draft/roles/MINER.md` | frontier |
| **Reviewer** — check published material against a fixed question set | `standard/v0.2.0-draft/roles/REVIEWER.md` | frontier |

## The rules that apply to every role

**0. The syllabus is the source of truth, and it is read first.**

Before any past paper, any mark scheme, any examiner report and any plan, the syllabus itself is
read: its **assessment objectives**, their **weighting per qualification and per paper**, its
**paper structures**, and its **command-word table**. That document is the subject's user manual.
It says what the learner must do, how they will be assessed, and in what words the questions will
be put. Everything else in this repository is calibrated to it, so getting it second-hand ruins
everything downstream.

Then, and only then, the corpus is used to ask what those objectives and command words do in
practice: how often each is tested, at what mark tariff, on which paper.

This rule is written down because it was once broken. A command-word list was typed from recall
instead of read off the table, and per-paper AO splits were inferred from the papers' names
instead of read off the weighting table. Both were wrong. Both would have mis-shaped every item in
a subject.

So the rule has teeth:

- `mine/mine_syllabus.py` transcribes the assessment pages into
  `work/<qualification>/curriculum/syllabus-facts.json`, and **every value carries the page that
  states it plus the verbatim line**.
- `mine/framework.py` refuses to build without that file. It cannot invent an objective, a
  weighting, a paper or a command word; it can only read one.
- Every value downstream is tagged `syllabus` (transcribed), `corpus` (counted) or `judgement`
  (our reading), so the three are never confused.
- `mine/verify.py` re-opens the PDF and fails if any quote is not on the page it cites, if any AO
  weight or paper split differs from the syllabus table, or if the command-word list is not exactly
  the syllabus's.

**A value that cannot name where it came from is a value we do not have.**

**1. The checks are the contract.** Nothing is finished until this returns no failures:

```bash
python3 standard/v0.2.0-draft/checks/run_checks.py <workspace> <topic>
```

It runs in about four seconds. To see only what failed, in the order worth fixing, with the one
action that clears each:

```bash
python3 standard/v0.2.0-draft/checks/what_to_fix.py <workspace> <topic>
```

It exits 0 when the topic is clean, so it drives a fix loop directly. You do not need to have read
the whole standard — you need to make the checks pass. When no check fails, the decision reads
`PUBLISH`. That is the publication gate; nothing else gates it.

**2. Derived things are generated, never typed.** Filenames, charts, exposure figures, contract
counts, work orders — all of these come out of `standard/v0.2.0-draft/build/`. If you find yourself
typing a filename or drawing a diagram by hand, stop: there is a generator for it, and a check that
fails when the two disagree.

**3. Stay in your lane.** Never edit anything under `standard/`. Never touch a topic that is not
yours. Never edit another role's outputs. Never open a workspace other than the one you were given.
If something outside your lane is wrong, say so in your report.

**4. Every item carries two labels, and they are different axes.** `assessment_objectives` is what
the examination credits. `blooms_level` is what the learner is being asked to do — Remember,
Understand, Apply, Analyse, Evaluate, Create. The work order decides both for every slot; carry
both onto the item. A subject whose assessment objectives do not name application still sets cards
that ask a learner to apply something, and those are Bloom Apply whatever AO credits them.

**5. Command words come from the papers, not from the syllabus table.** Each subject's framework
carries a verdict per word: how often it actually opens a question, at what tariffs, on which
paper. Only a word with `use_in_prompts: true` may appear in a generated prompt. A word the
syllabus lists but the papers never use models a question that does not exist.

## Where everything lives

```
work/<qualification>/
  qualification-profile.yaml    route, papers, assessment objectives, years examined
  subject-profile.yaml          answer structures, variant register, conditioned mechanisms
  curriculum/
    objective_registry.json     every objective, its command words, depth tier, type
    assessment-framework.json   command words, exact tariffs, subtype→AO map, AO targets
    exam-exposure.json          how often each objective is examined, and at what tariff
    glossary.json               settled definitions, including homonyms to keep apart
    answer-shapes.json          the answer architecture behind each command word and tariff
    misconceptions.json         examiner-evidenced confusions, attached to objectives
    syllabus-exclusions.json    the board's own stated content limits
    ao_coverage.md              the subject's AO balance against the syllabus weights
  PLAN-<code>-<slug>.md         the authoring brief for this subject
  HANDOVER-<code>-<slug>.md     the prompt an operator pastes into a harness
  assessment-evidence/          mined question, mark-scheme and examiner-report evidence
  topics/<topic>/
    contract.json               scope, exclusions, budgets for this topic
    work_order.json / .md       THE PLAN — every slot decided. Authors read this.
    claims/ content-units/ learning-items/
    <n>-<topic-name>.md         the rendered notes
    qa_report.json              what the checks said last time they ran
publish/<qualification>/        the upload folder: INDEX.md, notes/, flashcards/
standard/v0.2.0-draft/
  roles/                        the four role briefs
  checks/run_checks.py          the deterministic suite
  build/                        every generator
  mine/                         the corpus miners that build a curriculum folder from PDFs
  RUNTIME_STANDARD.md           the 47 rules, if you need the reasoning behind a check
  OPERATOR_RUNBOOK.md           how a human drives all of this
operations/analysis/            one corpus analysis per syllabus code
```

## House facts

- Learners are Namibian secondary students, English medium. Worked examples use Namibian dollars
  (N$) and businesses a learner in Namibia would recognise. Invented businesses only — never a real
  named company.
- Official assessment sources are **mine, do not reproduce**. Analyse the demand — command words,
  tariffs, AO focus, contexts, examiner-evidenced misconceptions — and never reproduce question text
  or mark-scheme wording in anything a learner reads.
- Notes serve three purposes at once: the source flashcards are cut from, the offline study text,
  and a standalone learning text. That is why they are written at full teaching depth.
