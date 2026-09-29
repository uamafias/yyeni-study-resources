# Authoring brief — one topic, one pass

You are authoring the complete learner resource for **one topic** of one syllabus. Read this
whole file before you touch anything.

**There is no review round.** You generate once, run the deterministic checks, fix what they name,
and you are done. Do not aim for a reviewer's approval; aim for a learner who has nothing else.
A finished, correct topic beats a perfect card in an unfinished subject — RS-42, amended
2026-09-12, makes the deterministic suite the publication gate and moves semantic review to
*after* publication, where its findings are debt the topic carries visibly.

## What you are given

Your dispatcher names the **workspace** (`work/<qualification>/`) and your **topic id**. From the
repository root:

```
work/<qualification>/
  curriculum/objective_registry.json     every assessable objective, with its command words
  curriculum/assessment-framework.json   command words, exact mark tariffs, subtype→AO map, AO targets
  curriculum/exam-exposure.json          how often each objective has been examined, and at what tariff
  curriculum/glossary.json               settled definitions — use these exactly, including homonyms
  subject-profile.yaml                   answer structures per subtype, variant register,
                                         conditioned mechanisms, prohibited patterns, legal model
  qualification-profile.yaml             route, papers, assessment objectives, years examined
  topics/<TOPIC>/contract.json           YOUR BRIEF: scope, exclusions, budgets, depth, title
standard/v0.2.0-draft/
  schemas/*.json                         the shapes your files must validate against
  checks/run_checks.py                   the deterministic suite — run it, it is fast
  build/render_notes.py                  renders the notes from your content units
  build/render_chart.py                  renders any break-even chart. NEVER draw one by hand.
  build/naming.py                        derives every published filename from the topic title
  build/publish_subject.py               assembles the subject's learner-facing folder
```

**Read one finished topic first** — your dispatcher will name the exemplar. Its claim ledger,
content units, items and rendered notes are the standard to match. Copy its structure, its depth
and its voice. Do not copy its content.

## What you produce

Three files in `work/<qualification>/topics/<TOPIC>/`, then two commands:

1. **`claims/canonical_claim_ledger.json`** — every factual claim the topic teaches, each mapped to
   the objectives it serves. Roughly 2–4 claims per assessable objective.
2. **`content-units/CU-<subject>-<sub-topic>.json`** — **one unit per sub-topic.** A topic `2.1`
   with objectives `OBJ-…-2.1.1-*` and `OBJ-…-2.1.2-*` gets two units, not one and not one per
   objective. (Stage 5 set many contracts' `required_outputs.content_units` to an *objective*
   count; if yours looks like that, it is wrong — recompute it and note the correction.)
3. **`learning-items/topic_<TOPIC>_items.json`** — flashcards and performance tasks, roughly
   **5 per assessable objective**.

### You do not choose any filename

`render_notes.py` derives the notes filename from `topic_title` in your contract — topic 4.3
becomes `4.3-capacity-utilisation-and-outsourcing.md`, never `notes-4.3.md` — and
`publish_subject.py` names the flashcard file the same way. **Do not pass `--out`, and do not
rename anything afterwards.** A folder of numbered files is one a human has to decode before they
can manage it, and that cost lands on whoever maintains the subject for years.

**So check `topic_title` in your contract before you start.** Every filename, every index row and
every flashcard file header is built from it. If it is missing or wrong, fix it first.

## How to write

**Notes carry full teaching depth.** They are three things at once: the source the flashcards are
cut from, the offline study text when the platform is down, and a standalone learning text. A
learner reading offline cannot ask a follow-up question, so every mechanism, formula and worked
example is written out. Aim for roughly 300–350 words per assessable objective, and stay inside
the contract's word budget.

**Stay inside the objective.** Teach what the syllabus wording requires — not less, and not more.
The contract's `excluded_constructs` must not appear in learner-facing text. If the contract
declares none, write the list yourself from what belongs to neighbouring topics and to the level
above, so the scope check has something to enforce.

**Voice.** Plain, direct explanatory prose. Short paragraphs. Worked examples in the local currency
and in businesses a learner recognises. No hedging filler, no "it is important to note", no
bullet-point soup where prose teaches better. Invented businesses, never real named ones.

## The rules that shape the output

These came from four rounds of adversarial review on the first two topics ever built. They are the
mistakes that actually got made, so read them before you write, not after.

**Coverage and traceability**
- Every assessable objective in the contract must be *taught* by a content block and *practised*
  by an item. An objective listed on an item that the item does not really practise is not
  coverage — it is manufactured coverage, and the checks will catch it.
- Every item cites at least one claim, and that claim must serve the objective the item claims.
- The registry may hold more assessable objectives than the contract lists: a *decomposed
  container* with a parent counts too. Teach and practise it in its own right rather than letting
  its members stand in for it.

**Truth and conditions**
- No unqualified universals. "Always", "never", "every X is", "only from" — unless the statement is
  definitional, legal or arithmetic. Write tendencies as tendencies.
- What an independent third party will do — a lender, investor, buyer, supplier, regulator — is a
  likelihood with a reason, never a certainty.
- A mechanism whose conclusion holds only under conditions must carry those conditions **every time
  it appears**, not only in the claim. The commonest failure found in review was a correct claim
  beside three cards teaching the same mechanism with the condition stripped out.
- Never claim what examiners reward, what carries most marks, or what a paper contains.
- A generalisation must hold for every member it covers, or must declare which members it covers.
- Anything jurisdiction-dependent is taught as a principle that depends on national law, never as
  a flat legal rule.

**Answers**
- A canonical answer may not rest on a fact its own prompt does not supply. If the answer turns on
  a figure being the *total* cost, the stem has to say so, or the recommendation has to be
  explicitly conditional on checking it.
- Flashcards are self-contained. No card may depend on another card's content.
- Arithmetic must be correct, every figure carries its unit or currency, and a quantity is named in
  the units it is measured in — a margin of safety is units, a profit is money.
- A claim about how big an effect is must state the number.

**Assessment shape**
- Use only the command words and exact tariffs in `assessment-framework.json` for this
  qualification. Words the framework marks as not used at this level must never appear in a prompt.
- Every objective needs at least one item whose prompt instructs with one of *that objective's* own
  command words, at that tariff and answer shape.
- Each flashcard subtype has a declared answer structure in `subject-profile.yaml` under
  `answer_structures`. The marking guidance must name every declared part. Check it.
- Hit the AO mix target in the framework. The AO4 share is carried by extended performance tasks,
  not by multiplying evaluation flashcards.
- Where an exposure class requires a subtype that genuinely does not fit the objective, add an
  entry to the contract's `subtype_waivers` with a written reason of at least twelve words, rather
  than padding the bank with a card that teaches nothing.

**Depictions**
- A chart is generated, never drawn:
  `sys.path.insert(0, 'standard/v0.2.0-draft/build'); from render_chart import render_break_even`,
  and declare the parameters on the item as `context.chart`. A hand-drawn chart fails the checks,
  and worse, it will not show what it claims to show — that defect shipped once and reached review
  as a critical.
- If you need a figure the renderer does not produce, emit it as a generated table of plotted
  points rather than as hand-typed art.

## Metadata each artefact carries

Copy the exact field set from the exemplar. Every block and item needs:

- `claims_seen`: `{claim_id: revision}` for every claim it cites (revision is `1` for new claims)
- `authored_hash`:
  ```python
  import sys, hashlib
  sys.path.insert(0, 'standard/v0.2.0-draft/checks')
  from yyeni_checks import _artefact_text
  x['authored_hash'] = hashlib.sha256(_artefact_text(x).encode()).hexdigest()
  ```
- `qa_status`: `"review_required"`

Set the contract's `depth_constraints.item_budget`, `required_outputs.learning_items` and
`required_outputs.content_units` to what you actually produced — a check compares them to the live
build and fails if they drift.

## Finishing

```bash
cd <repo root>
python3 standard/v0.2.0-draft/build/render_notes.py <workspace> <TOPIC>
python3 standard/v0.2.0-draft/checks/run_checks.py   <workspace> <TOPIC>
```

Fix every **FAIL** and re-run until there are none. A `C-30` warning about stamps, and `not_run` on
checks whose input genuinely does not apply (`C-35`/`C-41` on a topic with no chart, `C-39` where
exposure was never measured), are all fine. When no check fails the decision reads **PUBLISH**.

Once every topic in the subject is clean, one command assembles the folder that gets uploaded —
notes and flashcards named for humans, plus `INDEX.md` and `MANIFEST.json`:

```bash
python3 standard/v0.2.0-draft/build/publish_subject.py <workspace>
```

It publishes only topics whose checks pass and reports any it skipped. Run it as often as you like;
it regenerates the folder from the build, and nothing in it is edited by hand.

Do not edit anything under `standard/`, and do not touch another topic's directory.

**Report back**: the topic, the number of claims / content units / items / notes words, the final
check line, and anything you had to judge rather than derive — places where the syllabus wording
was ambiguous, or where you made a scope call. Keep it under 150 words.
