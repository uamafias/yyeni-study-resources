# Cambridge International AS Level Physics 9702 (examined 2025-2027)

Study notes and flashcards. 12 topics, 860 flashcards and performance tasks, 61,599 words of notes.

Every topic here passes the full deterministic check suite. Semantic review runs on published material rather than ahead of it, so the **Open issues** column is debt that ships visibly and is cleared in a maintenance pass - it is not a warning that the topic is unusable.


## Topic 1 — Physical quantities and units

| Topic | Notes | Flashcards | Items | Words | Open issues |
|---|---|---|---:|---:|---:|
| **1** Physical quantities and units | [1-physical-quantities-and-units.md](notes/1-physical-quantities-and-units.md) | [1-physical-quantities-and-units-flashcards.json](flashcards/1-physical-quantities-and-units-flashcards.json) | 59 | 3,718 | — |

## Topic 2 — Kinematics

| Topic | Notes | Flashcards | Items | Words | Open issues |
|---|---|---|---:|---:|---:|
| **2** Kinematics | [2-kinematics.md](notes/2-kinematics.md) | [2-kinematics-flashcards.json](flashcards/2-kinematics-flashcards.json) | 64 | 3,699 | — |

## Topic 3 — Dynamics

| Topic | Notes | Flashcards | Items | Words | Open issues |
|---|---|---|---:|---:|---:|
| **3** Dynamics | [3-dynamics.md](notes/3-dynamics.md) | [3-dynamics-flashcards.json](flashcards/3-dynamics-flashcards.json) | 52 | 4,660 | — |

## Topic 4 — Forces, density and pressure

| Topic | Notes | Flashcards | Items | Words | Open issues |
|---|---|---|---:|---:|---:|
| **4** Forces, density and pressure | [4-forces-density-and-pressure.md](notes/4-forces-density-and-pressure.md) | [4-forces-density-and-pressure-flashcards.json](flashcards/4-forces-density-and-pressure-flashcards.json) | 65 | 4,407 | — |

## Topic 5 — Work, energy and power

| Topic | Notes | Flashcards | Items | Words | Open issues |
|---|---|---|---:|---:|---:|
| **5** Work, energy and power | [5-work-energy-and-power.md](notes/5-work-energy-and-power.md) | [5-work-energy-and-power-flashcards.json](flashcards/5-work-energy-and-power-flashcards.json) | 71 | 3,728 | — |

## Topic 6 — Deformation of solids

| Topic | Notes | Flashcards | Items | Words | Open issues |
|---|---|---|---:|---:|---:|
| **6** Deformation of solids | [6-deformation-of-solids.md](notes/6-deformation-of-solids.md) | [6-deformation-of-solids-flashcards.json](flashcards/6-deformation-of-solids-flashcards.json) | 61 | 3,435 | — |

## Topic 7 — Waves

| Topic | Notes | Flashcards | Items | Words | Open issues |
|---|---|---|---:|---:|---:|
| **7** Waves | [7-waves.md](notes/7-waves.md) | [7-waves-flashcards.json](flashcards/7-waves-flashcards.json) | 69 | 6,111 | — |

## Topic 8 — Superposition

| Topic | Notes | Flashcards | Items | Words | Open issues |
|---|---|---|---:|---:|---:|
| **8** Superposition | [8-superposition.md](notes/8-superposition.md) | [8-superposition-flashcards.json](flashcards/8-superposition-flashcards.json) | 57 | 3,920 | — |

## Topic 9 — Electricity

| Topic | Notes | Flashcards | Items | Words | Open issues |
|---|---|---|---:|---:|---:|
| **9** Electricity | [9-electricity.md](notes/9-electricity.md) | [9-electricity-flashcards.json](flashcards/9-electricity-flashcards.json) | 83 | 5,001 | — |

## Topic 10 — D.C. circuits

| Topic | Notes | Flashcards | Items | Words | Open issues |
|---|---|---|---:|---:|---:|
| **10** D.C. circuits | [10-d-c-circuits.md](notes/10-d-c-circuits.md) | [10-d-c-circuits-flashcards.json](flashcards/10-d-c-circuits-flashcards.json) | 89 | 5,242 | — |

## Topic 11 — Particle physics

| Topic | Notes | Flashcards | Items | Words | Open issues |
|---|---|---|---:|---:|---:|
| **11** Particle physics | [11-particle-physics.md](notes/11-particle-physics.md) | [11-particle-physics-flashcards.json](flashcards/11-particle-physics-flashcards.json) | 55 | 5,763 | — |

## Topic 12 — Practical skills (Paper 3)

| Topic | Notes | Flashcards | Items | Words | Open issues |
|---|---|---|---:|---:|---:|
| **12** Practical skills | [12-practical-skills.md](notes/12-practical-skills.md) | [12-practical-skills-flashcards.json](flashcards/12-practical-skills-flashcards.json) | 135 | 11,915 | — |

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

This folder is the copy to upload. The source of record is `work/cie-9702-as-2025-2027/topics/<number>/`, which holds each topic's claim ledger, content units, learning items and QA report. Regenerate this folder at any time with `build/publish_subject.py`; nothing in it is edited by hand.
