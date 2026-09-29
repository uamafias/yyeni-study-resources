# Operator runbook — generating notes and flashcards for one subject

**Standard:** v0.2.0-draft · **Audience:** anyone at YYeni assigned a batch of subjects
**You need:** Cowork (with the repository folder connected), Codex, and the official syllabus PDF.

This is the repeatable loop. It is the same for AS Business, IGCSE Maths and Grade 8 Life Science: everything subject-specific lives in files you fill in, never in the process.

---

## 0. Before you start

**One workspace per qualification, route and exam window.** Name it `<board-short>-<code>-<route>-<first>-<last>`, e.g. `cie-9609-as-2026-2028`. Two routes of the same subject are two workspaces.

**Never write into `sources/`.** Sources are immutable. Everything you generate goes in `work/<workspace>/`.

**Install the check dependencies once per machine:**

```bash
pip3 install --user 'jsonschema>=4.18' 'PyYAML>=6.0'
```

---

## 1. Stages 1–5 — scope, sources, curriculum, assessment, contracts

Run these once per qualification, not once per topic. The output is the shared spine every topic then draws on.

| Stage | You produce | Where |
|---|---|---|
| 1 Scope lock | `qualification-profile.yaml` — board, code, syllabus version, exam years, route, papers, language | workspace root |
| 2 Source inventory | `inventory/source_inventory.json` — every source hashed, classified, readability measured | workspace |
| 3 Curriculum map | `curriculum/objective_registry.json`, `dependency_graph.json`, `glossary.json`, `assessment-framework.json` | workspace |
| 4 Assessment mining | `assessment-evidence/assessment_evidence.json`, `exam-exposure.json` | workspace |
| 5 Topic contracts | `topics/<id>/contract.json` for every topic | workspace |

**Three things at these stages decide how much rework you do later.**

**A. Decompose to the member, not the bullet.** A syllabus bullet that lists five instruments is five objectives, not one. If you do not split, you cannot later tell whether each member is taught, and no check can tell you either.

**B. Fill in the subject profile's two human registers.** Nothing else in the pipeline can generate these, and two whole rule families are unenforceable without them:

- `variant_register` — terms in this subject whose forms change a learner-relevant consequence. In Business: recourse vs non-recourse factoring, the four crowd-funding models, secured vs unsecured lending. In Chemistry it would be reaction types; in History, source categories. Ask: *if a learner knew only one form of this, what would they get wrong?*
- `answer_structures` — the required parts of each item subtype, each part with alternative keywords. Take them from the qualification's own credit-worthy-answer descriptions.

**C. Fill in each contract's `depth_constraints.excluded_constructs`** — what belongs to the higher level or to a different topic. Prose in the notes saying "this is out of scope" enforces nothing. This list does.

---

## 2. Stages 10–13 — author one topic

Author against the contract, not against a textbook. For each objective: claims → content units → notes → learning items, in that order, so everything downstream is derived from approved claims (RS-16).

**Eight habits that produced fifteen review defects on the pilot. Read them before you write.**

1. **No universals.** "Only", "never", "always", "any other", "no lender will" — unless the statement is definitional, legal or arithmetic, and then say which on the claim. Almost everything you want to write as a rule is a tendency.
2. **A generalisation must survive its own members.** If you write "all internal sources cost nothing" and one of them creates lease payments, the summary is wrong — do not fix it by teaching the exception two pages later. Declare `generalisation_scope` on the block.
3. **Third parties do not have certain behaviour.** A lender *may* refuse, and here is why. Do not invent the provider's internal method unless your evidence names it for that context.
4. **Never say what examiners reward** unless you can cite a mapped assessment-evidence record. If the evidence status is `partial`, say nothing about examiners at all.
5. **Practise the command word.** An Explain objective needs an item that says *Explain*, at that tariff, in that answer shape. Coverage by recall cards is not coverage.
6. **Map only what you practise.** An item's `objective_ids` are the objectives it actually works on. Citing fifteen objectives on one card manufactures coverage and the suite will say so.
7. **A card must be reconstructible from the notes.** If the answer leans on a mechanism the notes never teach, the offline learner cannot get there. Add it to the notes or take it out of the card.
8. **Model every declared part.** An EVAL item that never says what to do has not evaluated, however good the prose.

---

## 3. Run the checks

```bash
python3 standard/v0.2.0-draft/checks/run_checks.py work/<workspace> <topic-id>
```

Writes `topics/<topic>/qa_report.json` and `topics/<topic>/packet.sha256`. Exits non-zero unless everything passes.

**Fix everything it names before going further.** It names IDs, so this is cheap — and every defect you fix here is one the reviewer does not spend its attention on.

**`not_run` is not a pass.** It means a check could not see its input. Either supply the input or accept that you are the only line of defence there.

Re-run until only `pass` remains, or until the remainder are warnings you have consciously accepted.

---

## 4. Generate the review packet

```bash
python3 standard/v0.2.0-draft/checks/make_review_packet.py "$PWD" work/<workspace> <topic-id> \
  --display-root "/Users/<you>/Documents/YYeni Study Resources"
```

`--display-root` is the path **the reviewer** will open. Cowork often runs inside a container mount, so `$PWD`
there is not a path Codex can use; the tool warns if the root it is about to write looks like one.

Writes `operations/review/<workspace>-<topic>-BRIEF.md` and `-PROMPT.txt`, both assembled from the build itself.

**Do not hand-edit the brief.** If it says something wrong, the build or the standard is wrong. Fix that and regenerate.

---

## 5. Review with Codex

Paste the contents of `-PROMPT.txt` into Codex, pointed at the repository. It writes `operations/review/<workspace>-<topic>-review.yaml`.

Merge the result into the qa report's `semantic_reviews` array and set `release_decision` from the review's status.

**The reviewer is not a rubber stamp.** On the pilot it returned *reject* with three critical issues on a build that had passed 22 of 25 mechanical checks. Expect a reject on your first topic in a new subject. That is the system working.

---

## 6. Repair, then re-review

Repair against the review. Re-run the checks. Send back only what changed, plus enough context to judge it.

**When a defect is a habit rather than a fact, it belongs in the standard, not just in the fix.** Raise a change request in `operations/standard-change-requests/`. That is how CR-003 and the eight rules behind this runbook came to exist, and it is the only thing that stops sixty people making the same mistake sixty times.

---

## 7. Release

A topic is done when: every check passes or is a consciously accepted warning; the review is `pass` or `conditional pass` with nothing open; generated-gap claims have documented human approval (RS-13); jurisdiction-sensitive claims have a human wording decision (RS-23); and the build manifest records standard version, profile versions, syllabus version, source hashes, counts computed from the final artifact and output hashes (RS-32).

---

## What is worth your time, and what is not

The expensive parts of this process are the parts only a person can do: splitting the syllabus honestly, writing the variant register, deciding what is out of scope, and judging a review's findings. The cheap parts are everything the suite checks.

If you find yourself hand-checking counts, coverage, duplicate prompts or command words, stop — that is the suite's job, and doing it yourself means the real questions go unasked.

## Known limits of the machinery

Two defect classes on the pilot could not be mechanised and will reach you through the reviewer or not at all:

- **An inverted causal mechanism** — a fluent, well-formed sentence stating a true relationship backwards. No pattern separates it from its correct form.
- **Whether a learner could actually build an answer from the notes.** A check for this was written and withdrawn: it fired on 47 of 68 items because ordinary English variation swamps the signal. The mechanical floor is that every claim an item cites is also taught in a content-unit block; the rest is the reviewer's reconstruction test.

Do not try to solve these with more regexes. Both are why the reviewer exists.

---

## Authoring a subject at scale (added 2026-09-12)

`AUTHORING_BRIEF.md` in this folder is the single instruction set for building one topic. Hand it
to an author — a person or a model — together with the workspace path, the topic id, and the name
of one finished topic to use as the exemplar. It is subject-agnostic: it reads the command words,
tariffs, AO targets and answer structures out of the subject's own profile files, so the same brief
serves every syllabus.

**Topics are independent, so author them in parallel.** Seventeen topics of 9609 AS were built
concurrently in one evening by one author per topic. This is the part that scales; running topics
one at a time behind a review gate is what did not.

```bash
# per topic, by the author
python3 standard/v0.2.0-draft/build/render_notes.py <workspace> <TOPIC>
python3 standard/v0.2.0-draft/checks/run_checks.py   <workspace> <TOPIC>

# once, when the subject is clean
python3 standard/v0.2.0-draft/build/publish_subject.py <workspace>
```

### Naming is generated, never typed

`build/naming.py` is the single source of every published filename, derived from `topic_title` in
the contract: `4.3` + *Capacity utilisation and outsourcing* gives
`4.3-capacity-utilisation-and-outsourcing.md` and
`4.3-capacity-utilisation-and-outsourcing-flashcards.json`.

This exists because the first run of 9609 left each author to name their own notes file, and the
subject shipped `notes-1.1.md` beside `notes-1.2-business-structure.md`. Nobody can manage a folder
they have to decode. `render_notes.py` now derives the name and removes a superseded one; if it
cannot delete, it prints the path for you to remove by hand.

`publish_subject.py` writes `publish/<qualification>/` containing `notes/`, `flashcards/`,
`INDEX.md` (every topic by name, grouped by syllabus unit, with counts and open issues) and
`MANIFEST.json`. Each flashcard file carries `topic_number`, `topic_title` and — on every card —
`objective_titles` beside `objective_ids`, so a reviewer sees what a card teaches without looking
up a code. Only topics whose checks pass are published; the rest are reported and the run
continues, so one broken topic cannot hold up a subject.

---

## Running the pipeline on open-weights models (added 2026-09-13)

The division of labour: **frontier models mine and plan, open models author, checks verify,
frontier reviews after publication.** Vitalis set this on 2026-09-12.

### The routing layer

`AGENTS.md` at the repository root is what every agent reads first, whatever tool it runs in —
OpenCode, Hermes Agent, Claude Code. It states the three rules that apply to everyone and routes to
exactly one role brief in `standard/v0.2.0-draft/roles/`:

| Role | Brief | Model |
|---|---|---|
| Author — one topic's notes and cards | `roles/AUTHOR.md` | open weights |
| Planner — set a subject up | `roles/PLANNER.md` | frontier |
| Miner — papers, mark schemes, examiner reports | `roles/MINER.md` | frontier |
| Reviewer — fixed question set, one round | `roles/REVIEWER.md` | frontier |

Starting an author needs three things and nothing else: the workspace path, one topic id, and the
name of a finished topic to use as the exemplar.

### Why authors get a work order, not a brief alone

```bash
python3 standard/v0.2.0-draft/build/make_work_order.py <workspace> --all
```

Seventeen frontier authors followed one brief on the first subject and made seventeen different
judgement calls — how many content units, how to tag AOs on flexible subtypes, whether to invent
excluded constructs, how to treat a decomposed container. A cheaper model writes prose about as
well and judges considerably worse, so the judgement is computed instead.

`work_order.json` fixes every slot before anyone writes: the content-unit split (one per sub-topic),
each card's objective, subtype, assessment objectives, command word, tariff, difficulty and the
parts its marking guidance must name, plus the AO balance and the word budgets. Validated against
the first subject, it reproduces the unit split 18 topics out of 19.

It derives subtypes from `objective_type` and `depth_tier` in the registry, so **the registry is now
load-bearing**: a wrong `objective_type` produces a wrong slot. That is a feature — the work order
shows its reasoning in the `reason` column, so a bad type is visible rather than silent.

The one thing it cannot compute is `excluded_constructs`. It prints `** excluded_constructs
MISSING **` for any contract lacking them, and that is the Planner's job.

### The fix loop

```bash
python3 standard/v0.2.0-draft/checks/what_to_fix.py <workspace> <topic>
```

`run_checks.py` prints 43 lines, mostly passes. This prints only failures, ordered structure-first,
each with its affected ids and the single action that clears it, and exits 0 when the topic is
clean. An author loops on it. This is what lets a smaller model converge where one shot would not:
it never has to understand the standard, only to clear the next named thing.
