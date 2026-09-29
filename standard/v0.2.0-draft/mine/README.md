# Corpus mining

These read a folder of extracted Cambridge PDFs and turn them into the curriculum
files a subject workspace needs. They are the reason a new syllabus takes an
evening rather than a week.

Nothing here reproduces official wording in learner-facing output. Official
assessment material is `mine_do_not_reproduce`: what is extracted is structure,
frequency and examiner-stated failure. `verify.py` checks that directly.

## Step zero: the syllabus, before anything else

```bash
python3 mine_syllabus.py <code>
```

Nothing else runs first. This transcribes the syllabus's own account of how the subject is
assessed — the assessment objectives, their weighting per qualification **and per paper**, each
paper's structure, and the complete command-word table — into
`work/<qualification>/curriculum/syllabus-facts.json`. **Every value carries the page that states
it and the verbatim line that states it.**

`framework.py` refuses to run without that file. It cannot invent an objective, a weight, a paper
or a command word; it can only read one. And `verify.py` re-opens the PDF and fails if a quote is
not on the page it cites, if an AO weight or a per-paper split differs from the weighting table,
or if the command-word list is not exactly the syllabus's.

Every value the chain produces is tagged with one of three provenances:

| tag | meaning |
|---|---|
| `syllabus` | transcribed from a named page. The authority. |
| `corpus` | counted from the published papers and mark schemes. |
| `judgement` | our reading — neither stated nor measured. Labelled so nobody mistakes it for either. |

**Why this is step zero.** It was once skipped. A command-word list was written from recall and
did not match the syllabus table; per-paper AO splits were inferred from the papers' names and did
not match the weighting table. Both propagate into every item in a subject, and the syllabus was
on disk the whole time. The gate in `verify.py` was tested by re-injecting both errors: it catches
them and names them.

## The chain

| script | reads | writes |
|---|---|---|
| `mine_syllabus.py` | **the syllabus PDF — first, always** | assessment objectives, weights, papers, command words, each with its page |
| `mine_questions.py` | question paper text | question parts, command words, tariffs |
| `mine_ms.py` | mark scheme text | award grammar, AO tags, level bands, refusals |
| `mine_er.py` | examiner report text | error statements |
| `shape.py` | the two above | the answer shape per command word and tariff |
| `cluster_er.py` | error statements | craft failures ranked by series spread; confusion pairs |
| `register.py` | confusion pairs + registry | misconceptions attached to objectives |
| `build_<code>.py` | syllabus text | the objective registry |
| `framework.py` | **syllabus facts** + mark schemes | the syllabus's words reconciled with what the papers do with them |
| `exposure.py` | mark schemes + registry | how often each objective is examined |
| `assemble.py` | all of the above | the workspace `curriculum/` folder |
| `exclusions.py` | syllabus text | the board's own stated content limits, per topic |
| `docs.py` | the workspace | `PLAN-<code>-<slug>.md`, `HANDOVER-<code>-<slug>.md`, and the corpus analysis — **one set per syllabus code** |
| `verify.py` | everything, and the raw text again | pass/fail on every headline claim |

Then `build/make_contract.py` and `build/make_work_order.py` turn the curriculum
folder into per-topic contracts and pre-decided item slots.

## One syllabus code, one set of documents

`docs.py` takes syllabus codes as arguments and writes a separate, self-contained set for each.
A document belonging to 0450 never names 0455 and never sends an agent to another workspace;
`verify.py` asserts both. Subjects are commissioned together and shipped separately, because an
agent works one subject at a time.

## Running it on a new syllabus

1. `python3 mine_syllabus.py <code>` — the syllabus first. Read the JSON it writes and satisfy
   yourself that the AO weights, the per-paper splits and the command words are what the document
   says. This is the five minutes that protects everything after it.
2. Extract the past papers to text into `<code>/`.
3. Write a `build_<code>.py` that parses that syllabus's subject-content tables.
   This is the only per-subject code; everything else is generic.
4. Run the rest of the chain in table order.
5. `python3 build/make_contract.py work/<workspace>`
6. `python3 build/make_work_order.py work/<workspace> --all`
7. `python3 mine/docs.py <code>`
8. `python3 mine/verify.py` and fix what it names.

## What verify.py is for

It re-reads the raw mark schemes and re-counts every headline claim **per question block, not per
file** — the distinction matters: counting per file made two correct findings look false, and a
third pass caught two claims that really were wrong. It also checks that every document names only
paths that exist, that no plan refers to another syllabus, that every slot carries a Bloom level
and a command word the papers actually use at a tariff they actually carry, and that the board's
stated content limits reached the contracts. Run it after any change to the chain.

## Paths

The scripts expect the extracted text under `~/mine/<code>/` and write
intermediates to `~/mine/out/`. Point `ROOT` elsewhere if that does not suit.
