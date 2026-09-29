# Authoring plan — Cambridge IGCSE Business Studies 0450

For an agent authoring the **whole subject in one run**. Namibian secondary learners, English medium, sitting the exam within weeks. There is no review round: you generate, you run the deterministic checks, you fix what they name, you are done.

Working root: `cie-0450-igcse-2026`. Everything below is derived from the curriculum folder, so read the files, do not re-derive them.

## What the corpus says, and why it changes what you write

This plan is built from **84 published question papers, 84 mark schemes and 17 Principal Examiner Reports, 2020–2025**. 1169 question parts carrying 6660 marks, mined from 84 published mark schemes across 18 examination series, 2020-2025. Three things came out of it that you would otherwise have got wrong.

**1. The command words the syllabus lists are not the command words the paper uses.**

Live in the papers: **Calculate, Consider, Define, Explain, Identify, Outline, Refer, State, Using**.

Listed in the syllabus table but appearing **zero times** in 84 mark schemes: *Analyse, Describe, Discuss, Give, Justify, Recommend*. Never write a prompt with one of these.

Used in the papers but **absent from the syllabus table**: **Using**. These are real; the paper is the authority on what is asked.

| command word | modal tariff | observed tariffs | times seen |
|---|---:|---|---:|
| Explain | 6 | 6m ×202, 8m ×160, 12m ×8 | 370 |
| Define | 2 | 2m ×153 | 153 |
| Identify | 2 | 2m ×122, 4m ×31 | 153 |
| Outline | 4 | 2m ×3, 4m ×121, 6m ×1 | 125 |
| Consider | 12 | 12m ×115 | 115 |
| Using | 12 | 2m ×1, 4m ×1, 6m ×3, 8m ×5, 12m ×37 | 47 |
| Calculate | 2 | 2m ×42 | 42 |
| State | 2 | 2m ×16, 4m ×12 | 28 |

**2. Each command word and tariff has a repeating answer shape, and the mark schemes state it.**

`curriculum/answer-shapes.json` carries all of them, each with the share of that question population it was verified against. Write to the shape; where the share is below 90%, the exceptions are named so you know when it does not apply.

The ones that matter most:

- **Define, 2 marks** (seen 153 times) — full definition = 2; partial definition = 1
  - *guard*: an example is not a definition
- **Identify|State, 2 marks** (seen 138 times) — 1 mark per item; two items
  - *guard*: only the first two responses are marked
- **Identify|State, 4 marks** (seen 43 times) — 1 mark per item x 4; or 2 items each with a context reference
- **Outline, 4 marks** (seen 121 times) — 2 points, each: point + application
  - *verified*: 95% award a mark per point plus a mark per relevant reference to the named business, giving 2 x (point + application).
  - *guard*: answers must address the party the question names, not another stakeholder
- **Explain, 6 marks** (seen 202 times) — 2 points, each: point + application + consequence
  - *caps*: max two of each mark type
  - the single most common question form in Paper 1: a 2 x 3 grid
  - *verified*: 141 of 202 (70%) carry all three mark types. Of the rest, 18% carry identification + explanation with no application mark and 12% carry application + explanation. The missing mark is almost always application, on a question written without a case context.
  - *guard*: Naming a context word is not application. The mark is for the point being worked through that context. Examiners refuse a context word used as decoration in 27 separate statements.
- **Calculate, 2 marks** (seen 42 times) — method / working = 1; correct answer with unit = 1
  - own-figure rule applies: a correct method on a wrong earlier figure still earns the method mark
- **Explain, 8 marks** (seen 160 times) — one mark for each distinct relevant point, capped (max two or max four); one further mark for each point that is developed to its consequence
  - Paper 2. Four of these carry 32 of the paper’s 80 marks.
  - *verified*: 94% state a cap on the number of points; 99% award development marks separately. Only 16% award a separate application mark, so unlike the 6-mark Explain this is a point-and-development question, not a point-context-consequence one.
- **Consider|Using|Explain, 12 marks** (seen 160 times)
  - **top band 9-12** needs all of: sound application of knowledge and understanding of relevant business concepts using appropriate terminology; detailed discussion of two or more of the named options; a well-justified recommendation
  - **the ceiling of that band** is reserved for: all named options discussed in detail and in context, with an explicit statement of why the rejected options were rejected
  - the stem names the options to weigh: three (×77), two (×55), unstated (×34)
  - 48 of Paper 2's 80 marks. The band-3 ceiling turns on rejecting the alternatives explicitly.
  - *verified*: 100% are level-banded over three bands. 99% require a well-justified recommendation or conclusion for the top band. 94% reserve the ceiling of the top band for candidates who also say why the rejected options were rejected — the single most reliable finding in the whole corpus, and the one examiner reports most often say candidates miss.

**3. Examiners name the same failures every single year.**

These are not style preferences; they are where the marks go. In all 17 reports:

- naming a context word from the case does not earn the application mark; the point has to be worked through in that context
- an example is not a definition and is not an explanation
- an answer written from the wrong stakeholder's point of view scores nothing
- a solution offered where the question asked for a cause or an effect scores nothing
- a point restated in different words is not a second point

`curriculum/misconceptions.json` holds **72 examiner-evidenced confusions**, each attached to the objective it belongs to. Every one earns a MISCON card, and a MISCON card is a *discrimination* card: it states the boundary and gives the test that separates the two ideas. It does not restate the correct definition.

## Where the marks actually are

Topics ordered by marks examined in the corpus. This calibrates how much worked example and how many variants a topic gets — **never whether it is taught**. Under RS-05 every objective in the registry is taught and practised, including the 21 never seen in six years of papers.

| topic | title | objs | core/freq | items | words | marks in corpus | share | miscon |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| **3.3** | Marketing mix | 16 | 6 | 70 | 4470–6430 | 906 | 13.7% | 9 |
| **1.3** | Enterprise, business growth and size | 11 | 7 | 53 | 3260–4670 | 726 | 11.0% | 4 |
| **2.2** | Organisation and management | 7 | 4 | 30 | 2070–2970 | 528 | 8.0% | 6 |
| **6.3** | Business and the international economy | 8 | 4 | 34 | 2310–3320 | 424 | 6.4% | 6 |
| **4.1** | Production of goods and services | 8 | 4 | 35 | 2340–3360 | 366 | 5.5% | 6 |
| **2.3** | Recruitment, selection and training of employe | 11 | 3 | 45 | 3050–4390 | 354 | 5.4% | 4 |
| **5.1** | Business finance: needs and sources | 7 | 4 | 32 | 2030–2910 | 316 | 4.8% | 0 |
| **4.2** | Costs, scale of production and break-even anal | 11 | 4 | 63 | 3030–4360 | 280 | 4.2% | 1 |
| **6.2** | Environmental and ethical issues | 7 | 2 | 38 | 2010–2890 | 276 | 4.2% | 7 |
| **3.2** | Market research | 7 | 4 | 33 | 1970–2830 | 236 | 3.6% | 3 |
| **2.1** | Motivating employees | 7 | 3 | 29 | 1980–2850 | 222 | 3.4% | 3 |
| **1.4** | Types of business organisation | 5 | 3 | 20 | 1430–2050 | 218 | 3.3% | 4 |
| **4.4** | Location decisions | 4 | 1 | 25 | 1080–1550 | 206 | 3.1% | 0 |
| **3.1** | Marketing, competition and the customer contin | 12 | 2 | 47 | 3130–4500 | 206 | 3.1% | 0 |
| **4.3** | Achieving quality production | 3 | 2 | 21 | 900–1290 | 182 | 2.8% | 1 |
| **1.5** | Business objectives and stakeholder objectives | 7 | 2 | 28 | 1960–2820 | 176 | 2.7% | 2 |
| **2.4** | Internal and external communication | 4 | 2 | 33 | 1140–1640 | 176 | 2.7% | 1 |
| **1.1** | Business activity | 4 | 1 | 21 | 1070–1540 | 130 | 2.0% | 4 |
| **3.4** | Marketing strategy | 6 | 0 | 37 | 1580–2280 | 120 | 1.8% | 1 |
| **5.3** | Income statements | 5 | 2 | 28 | 1390–2000 | 114 | 1.7% | 6 |
| **6.1** | Economic issues | 6 | 1 | 27 | 1610–2320 | 110 | 1.7% | 2 |
| **5.2** | Cash-flow forecasting and working capital | 6 | 2 | 44 | 1560–2240 | 108 | 1.6% | 0 |
| **5.5** | Analysis of accounts | 9 | 0 | 64 | 2330–3360 | 108 | 1.6% | 0 |
| **5.4** | Statement of financial position | 2 | 1 | 16 | 570–820 | 78 | 1.2% | 1 |
| **1.2** | Classification of businesses | 3 | 0 | 15 | 770–1110 | 46 | 0.7% | 1 |

**Subject total: 888 items, 49040–70500 words across 25 topics.**

## The files

Read, in this order:

1. `AGENTS.md` at the repo root — it routes you to `standard/v0.2.0-draft/roles/AUTHOR.md`.
2. `cie-0450-igcse-2026/curriculum/answer-shapes.json` — the shape of every answer you will write.
3. `cie-0450-igcse-2026/curriculum/misconceptions.json` — filter on your topic.
4. `cie-0450-igcse-2026/subject-profile.yaml` — answer structures per subtype, conditioned mechanisms, prohibited patterns.
5. `cie-0450-igcse-2026/topics/<TOPIC>/contract.json` — your scope and budgets.
6. `cie-0450-igcse-2026/topics/<TOPIC>/work_order.json` — every item slot, pre-decided.

The work order is a computed baseline, not a cage. Where a slot does not fit the objective, change it and record the change in `topics/<TOPIC>/authoring_notes.json` as `{from, to, why}`. An unrecorded deviation is the only kind that is wrong.

Produce, per topic, in `cie-0450-igcse-2026/topics/<TOPIC>/`:

1. `claims/canonical_claim_ledger.json` — every factual claim, mapped to objectives.
2. `content-units/CU-0450-<sub-topic>.json` — one per sub-topic.
3. `learning-items/topic_<TOPIC>_items.json` — the cards and performance tasks.
4. Then render and check.

You choose no filenames. `render_notes.py` derives the notes filename from the contract’s `topic_title`; `publish_subject.py` names the flashcard file to match.

## Finishing

```bash
python3 standard/v0.2.0-draft/build/render_notes.py work/cie-0450-igcse-2026 <TOPIC>
python3 standard/v0.2.0-draft/checks/run_checks.py   work/cie-0450-igcse-2026 <TOPIC>
python3 standard/v0.2.0-draft/checks/what_to_fix.py  work/cie-0450-igcse-2026 <TOPIC>
```

Fix every FAIL and re-run until there are none. Then, once the whole subject is clean:

```bash
python3 standard/v0.2.0-draft/build/publish_subject.py work/cie-0450-igcse-2026
```

Under RS-42 as amended, the deterministic suite is the publication gate. Semantic review runs on published material and its findings are debt the topic carries visibly.

## Known debt in this plan

- The AO mix is reported in `curriculum/ao_coverage.md`. Read it before you start: it says where the plan already differs from the syllabus weights and why padding would make the resource worse rather than better.
- 20 of 25 contracts carry no scope guards. The guards that exist are derived from the syllabus’s own structure, not from an A Level boundary. Stay inside your contract’s objective list and you will not need them.
- Exposure is measured by matching question wording to syllabus wording. 13 of parts did not match any objective and were reported rather than distributed.
