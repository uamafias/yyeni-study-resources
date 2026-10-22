# NSSCAS Chemistry 8224 (examined 2026)

Study notes and flashcards. 1 topics, 1 flashcards and performance tasks, 284 words of notes.

Every topic here passes the full deterministic check suite. Semantic review runs on published material rather than ahead of it, so the **Open issues** column is debt that ships visibly and is cleared in a maintenance pass - it is not a warning that the topic is unusable.


## The Particulate Nature Of Matter and Stoichiometry

| Topic | Notes | Flashcards | Items | Words | Open issues |
|---|---|---|---:|---:|---:|
| **1.2** Atomic structure | [1.2-atomic-structure.md](notes/1.2-atomic-structure.md) | [1.2-atomic-structure-flashcards.json](flashcards/1.2-atomic-structure-flashcards.json) | 1 | 284 | — |

## What is in a flashcard file

One JSON file per topic, carrying `topic_number`, `topic_title` and a list of `items`. Each item has:

- `prompt` — what the learner sees
- `canonical_answer` — the model answer
- `marking_guidance` — what earns credit, part by part
- `subtype` — DEF, DIST, APP, CHAIN, EVAL, CALC and so on, or a performance task
- `assessment_objectives` — what the examination credits, and `difficulty` 1 to 5
- `blooms_level` — what the learner is being asked to do: Remember, Understand, Apply, Analyse, Evaluate or Create. A different axis from the assessment objective, and on every item
- `objective_ids` **and `objective_titles`** — what the card teaches, by code and in words
- `claim_ids` — the claims in the topic ledger the answer rests on

## Where the source lives

This folder is the copy to upload. The source of record is `/var/folders/zd/ztqtclyx75vchvjc9csmmqcm0000gp/T/8224-visual-9kqeeuuj/topics/<number>/`, which holds each topic's claim ledger, content units, learning items and QA report. Regenerate this folder at any time with `build/publish_subject.py`; nothing in it is edited by hand.
