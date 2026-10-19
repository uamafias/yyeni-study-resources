# REVIEW ONLY. NOT FOR LEARNERS. Namibia Senior Secondary Certificate Ordinary (NSSCO) Biology 6116 (examined 2026)

Study notes and flashcards. 5 topics, 851 flashcards and performance tasks, 72,833 words of notes.

Every topic here passes the deterministic checks, which verify structure only: no claim is verified by a Biology teacher and no figure is supplied. The standard builder's Open issues column is not populated for this subject: semantic review, teacher verification of every claim and the figures are all still open, so read this folder as a draft under review.


## Unit 1

| Topic | Notes | Flashcards | Items | Words | Open issues |
|---|---|---|---:|---:|---:|
| **1** Scientific processes | [1-scientific-processes.md](notes/1-scientific-processes.md) | [1-scientific-processes-flashcards.json](flashcards/1-scientific-processes-flashcards.json) | 107 | 7,446 | — |

## Unit 2

| Topic | Notes | Flashcards | Items | Words | Open issues |
|---|---|---|---:|---:|---:|
| **2** Classification and diversity of living organisms | [2-classification-and-diversity-of-living-organisms.md](notes/2-classification-and-diversity-of-living-organisms.md) | [2-classification-and-diversity-of-living-organisms-flashcards.json](flashcards/2-classification-and-diversity-of-living-organisms-flashcards.json) | 26 | 2,081 | — |

## Unit 3

| Topic | Notes | Flashcards | Items | Words | Open issues |
|---|---|---|---:|---:|---:|
| **3** Organisation and maintenance of the organism | [3-organisation-and-maintenance-of-the-organism.md](notes/3-organisation-and-maintenance-of-the-organism.md) | [3-organisation-and-maintenance-of-the-organism-flashcards.json](flashcards/3-organisation-and-maintenance-of-the-organism-flashcards.json) | 461 | 36,358 | — |

## Unit 4

| Topic | Notes | Flashcards | Items | Words | Open issues |
|---|---|---|---:|---:|---:|
| **4** Development of the organism and the continuity of life | [4-development-of-the-organism-and-the-continuity-of-life.md](notes/4-development-of-the-organism-and-the-continuity-of-life.md) | [4-development-of-the-organism-and-the-continuity-of-life-flashcards.json](flashcards/4-development-of-the-organism-and-the-continuity-of-life-flashcards.json) | 149 | 16,647 | — |

## Unit 5

| Topic | Notes | Flashcards | Items | Words | Open issues |
|---|---|---|---:|---:|---:|
| **5** Relationship of organisms with one another and with their environment | [5-relationship-of-organisms-with-one-another-and-with-their-environment.md](notes/5-relationship-of-organisms-with-one-another-and-with-their-environment.md) | [5-relationship-of-organisms-with-one-another-and-with-their-environment-flashcards.json](flashcards/5-relationship-of-organisms-with-one-another-and-with-their-environment-flashcards.json) | 108 | 10,301 | — |

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

This folder is an internal review copy built by `topics/build_review_package.py`, not a learner upload. Items whose figures are not yet supplied are left out; see HELD-ITEMS-OMITTED.json. Rebuild it with `topics/build_review_package.py`; nothing in it is edited by hand.
