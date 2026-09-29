# Authoring plan — Cambridge IGCSE Economics 0455

For an agent authoring the **whole subject in one run**. Namibian secondary learners, English medium, sitting the exam within weeks. There is no review round: you generate, you run the deterministic checks, you fix what they name, you are done.

Working root: `cie-0455-igcse-2026`. Everything below is derived from the curriculum folder, so read the files, do not re-derive them.

## What the corpus says, and why it changes what you write

This plan is built from **84 published question papers, 84 mark schemes and 17 Principal Examiner Reports, 2020–2025**. 1002 question parts carrying 4580 marks, mined from 42 published mark schemes across 18 examination series, 2020-2025. Three things came out of it that you would otherwise have got wrong.

**1. The command words the syllabus lists are not the command words the paper uses.**

Live in the papers: **Analyse, Calculate, Define, Discuss, Draw, Explain, Identify, State, Why**.

Listed in the syllabus table but appearing **zero times** in 84 mark schemes: *Describe, Give*. Never write a prompt with one of these.

Used in the papers but **absent from the syllabus table**: **Draw**. These are real; the paper is the authority on what is asked.

| command word | modal tariff | observed tariffs | times seen |
|---|---:|---|---:|
| Discuss | 8 | 3m ×1, 6m ×84, 8m ×165 | 250 |
| Explain | 4 | 2m ×34, 3m ×1, 4m ×212 | 247 |
| Analyse | 6 | 4m ×22, 5m ×40, 6m ×167 | 229 |
| Identify | 2 | 2m ×120 | 120 |
| Define | 2 | 2m ×75 | 75 |
| Calculate | 1 | 1m ×42 | 42 |
| State | 2 | 2m ×21 | 21 |
| Draw | 4 | 4m ×19 | 19 |

**2. Each command word and tariff has a repeating answer shape, and the mark schemes state it.**

`curriculum/answer-shapes.json` carries all of them, each with the share of that question population it was verified against. Write to the shape; where the share is below 90%, the exceptions are named so you know when it does not apply.

The ones that matter most:

- **Define, 2 marks** (seen 75 times) — two creditable elements of the definition
- **Identify|State|Give, 2 marks** (seen 141 times) — 1 mark per item; two items
  - *guard*: if more than two are given, only the first are considered
- **Calculate, 1 mark** (seen 42 times) — correct answer
  - own-figure rule applies
- **Explain, 4 marks** (seen 212 times) — four distinct, correct, linked statements, one mark each
  - the most common question form on Paper 2: a 2 x 2 grid
  - *verified*: This is point-marked from a pool, not a fixed grid. 31% state the pool as two reasons each developed once; 36% open with "logical explanation which might include" and list far more creditable statements than there are marks; 8% use a variant of the identify-plus-explain wording. The rule that fits all of them: one mark per distinct linked statement, up to four.
  - *guard*: A statement that only restates the one before it earns nothing. Each of the four has to add something — a reason, a consequence, or a further step in the chain.
- **Analyse, 4-6 marks** (seen 229 times) — one mark per distinct linked statement, from an open pool; each statement carries its reason; a bare assertion is not analysis; the answer runs point → because → therefore → consequence for the economic agent named; on a data question: expected relationship → supporting evidence from the data → analysis of the expected relationship → exception → analysis of the exception
  - *verified*: 94% of 6-mark Analyse questions open with "coherent analysis which might include" and list a median of 17 creditable statements for 6 marks, so the pool is wide and the marking is point-by-point. 16% require a diagram as well as the written analysis. The chain below is how the mark schemes structure their own lists, not a phrase they state.
  - *guard*: Quoting figures is description, not analysis. State the relationship, give a direct comparison as evidence, then give the reason. Examiners refuse figure-quoting explicitly.
- **Discuss, 8 marks** (seen 165 times) — the answer runs why it might → why it might not
  - **top band 6-8** needs all of: a reasoned discussion that accurately examines both sides of the economic argument; use of economic information; clear and logical analysis to evaluate economic issues and situations
  - *verified*: 95% are level-banded over three bands. 96% require the top band to examine BOTH sides of the argument. 78% lay the answer out as "why it might" then "why it might not", which is the skeleton to write to.
- **Discuss, 6 marks** (seen 84 times) — the answer runs why it might → why it might not
  - same two-sided architecture at a lower tariff

**3. Examiners name the same failures every single year.**

These are not style preferences; they are where the marks go. In all 17 reports:

- restating the figures is description, not analysis
- a diagram on its own earns nothing where a written point is required
- an example is not a definition
- a point credited once is not credited again in other words
- a near-miss term is refused where the syllabus term is specific (GDP per head is not GDP)

`curriculum/misconceptions.json` holds **66 examiner-evidenced confusions**, each attached to the objective it belongs to. Every one earns a MISCON card, and a MISCON card is a *discrimination* card: it states the boundary and gives the test that separates the two ideas. It does not restate the correct definition.

## Where the marks actually are

Topics ordered by marks examined in the corpus. This calibrates how much worked example and how many variants a topic gets — **never whether it is taught**. Under RS-05 every objective in the registry is taught and practised, including the 18 never seen in six years of papers.

| topic | title | objs | core/freq | items | words | marks in corpus | share | miscon |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| **3.3** | Workers | 4 | 2 | 30 | 1150–1650 | 577 | 12.7% | 3 |
| **4.7** | Employment and unemployment | 6 | 3 | 37 | 1730–2480 | 465 | 10.2% | 3 |
| **2.7** | Price elasticity of demand (PED) | 5 | 2 | 35 | 1390–1990 | 348 | 7.7% | 4 |
| **4.6** | Economic growth | 6 | 1 | 43 | 1640–2360 | 295 | 6.5% | 3 |
| **6.2** | Globalisation, free trade and protection | 6 | 3 | 30 | 1760–2520 | 250 | 5.5% | 3 |
| **3.5** | Firms | 5 | 4 | 26 | 1500–2150 | 241 | 5.3% | 1 |
| **4.3** | Fiscal policy | 9 | 5 | 39 | 2560–3680 | 228 | 5.0% | 3 |
| **6.4** | Current account of balance of payments | 4 | 2 | 32 | 1130–1620 | 149 | 3.3% | 2 |
| **3.8** | Market structure | 2 | 1 | 21 | 600–860 | 139 | 3.1% | 0 |
| **4.2** | The macroeconomic aims of government | 2 | 1 | 16 | 600–860 | 136 | 3.0% | 1 |
| **2.5** | Price determination | 2 | 1 | 21 | 580–830 | 122 | 2.7% | 0 |
| **5.3** | Population | 3 | 2 | 22 | 900–1290 | 110 | 2.4% | 2 |
| **2.9** | Market economic system | 2 | 2 | 13 | 600–860 | 108 | 2.4% | 1 |
| **4.5** | Supply-side policy | 3 | 1 | 22 | 810–1160 | 108 | 2.4% | 0 |
| **3.1** | Money and banking | 2 | 2 | 16 | 630–900 | 106 | 2.3% | 1 |
| **6.3** | Foreign exchange rates | 5 | 2 | 27 | 1410–2030 | 100 | 2.2% | 5 |
| **3.6** | Firms and production | 3 | 1 | 23 | 850–1220 | 95 | 2.1% | 2 |
| **5.4** | Differences in economic development between countries | 1 | 1 | 11 | 300–430 | 88 | 1.9% | 0 |
| **1.2** | The factors of production | 3 | 2 | 19 | 880–1260 | 81 | 1.8% | 1 |
| **3.4** | Trade unions | 3 | 0 | 18 | 810–1170 | 77 | 1.7% | 3 |
| **5.2** | Poverty | 3 | 1 | 22 | 840–1210 | 74 | 1.6% | 0 |
| **5.1** | Living standards | 2 | 1 | 18 | 570–820 | 73 | 1.6% | 1 |
| **2.2** | The role of markets in allocating resources | 3 | 2 | 26 | 870–1250 | 70 | 1.5% | 1 |
| **3.2** | Households | 1 | 1 | 11 | 330–470 | 68 | 1.5% | 0 |
| **3.7** | Firms’ costs, revenue and objectives | 5 | 1 | 27 | 1350–1940 | 67 | 1.5% | 1 |
| **4.8** | Inflation and deflation | 5 | 0 | 33 | 1250–1800 | 56 | 1.2% | 0 |
| **2.3** | Demand | 4 | 1 | 36 | 1030–1480 | 53 | 1.2% | 2 |
| **1.3** | Opportunity cost | 2 | 1 | 13 | 570–820 | 52 | 1.1% | 1 |
| **6.1** | International specialisation | 2 | 0 | 18 | 540–780 | 44 | 1.0% | 1 |
| **2.8** | Price elasticity of supply (PES) | 4 | 1 | 28 | 1010–1450 | 44 | 1.0% | 1 |
| **1.1** | The nature of the economic problem | 2 | 2 | 12 | 600–860 | 39 | 0.9% | 4 |
| **4.4** | Monetary policy | 3 | 0 | 22 | 750–1080 | 24 | 0.5% | 1 |
| **1.4** | Production possibility curve (PPC) diagrams | 4 | 0 | 38 | 1000–1440 | 22 | 0.5% | 1 |
| **2.4** | Supply | 4 | 0 | 36 | 1020–1470 | 19 | 0.4% | 0 |
| **2.6** | Price changes | 2 | 0 | 19 | 500–720 | 10 | 0.2% | 0 |
| **2.1** | Microeconomics and macroeconomics | 2 | 0 | 16 | 520–750 | 6 | 0.1% | 0 |
| **4.1** | The role of government | 1 | 0 | 11 | 230–330 | 0 | 0.0% | 0 |

**Subject total: 887 items, 34810–49990 words across 37 topics.**

## The files

Read, in this order:

1. `AGENTS.md` at the repo root — it routes you to `standard/v0.2.0-draft/roles/AUTHOR.md`.
2. `cie-0455-igcse-2026/curriculum/answer-shapes.json` — the shape of every answer you will write.
3. `cie-0455-igcse-2026/curriculum/misconceptions.json` — filter on your topic.
4. `cie-0455-igcse-2026/subject-profile.yaml` — answer structures per subtype, conditioned mechanisms, prohibited patterns.
5. `cie-0455-igcse-2026/topics/<TOPIC>/contract.json` — your scope and budgets.
6. `cie-0455-igcse-2026/topics/<TOPIC>/work_order.json` — every item slot, pre-decided.

The work order is a computed baseline, not a cage. Where a slot does not fit the objective, change it and record the change in `topics/<TOPIC>/authoring_notes.json` as `{from, to, why}`. An unrecorded deviation is the only kind that is wrong.

Produce, per topic, in `cie-0455-igcse-2026/topics/<TOPIC>/`:

1. `claims/canonical_claim_ledger.json` — every factual claim, mapped to objectives.
2. `content-units/CU-0455-<sub-topic>.json` — one per sub-topic.
3. `learning-items/topic_<TOPIC>_items.json` — the cards and performance tasks.
4. Then render and check.

You choose no filenames. `render_notes.py` derives the notes filename from the contract’s `topic_title`; `publish_subject.py` names the flashcard file to match.

## Finishing

```bash
python3 standard/v0.2.0-draft/build/render_notes.py work/cie-0455-igcse-2026 <TOPIC>
python3 standard/v0.2.0-draft/checks/run_checks.py   work/cie-0455-igcse-2026 <TOPIC>
python3 standard/v0.2.0-draft/checks/what_to_fix.py  work/cie-0455-igcse-2026 <TOPIC>
```

Fix every FAIL and re-run until there are none. Then, once the whole subject is clean:

```bash
python3 standard/v0.2.0-draft/build/publish_subject.py work/cie-0455-igcse-2026
```

Under RS-42 as amended, the deterministic suite is the publication gate. Semantic review runs on published material and its findings are debt the topic carries visibly.

## Known debt in this plan

- The AO mix is reported in `curriculum/ao_coverage.md`. Read it before you start: it says where the plan already differs from the syllabus weights and why padding would make the resource worse rather than better.
- 11 of 37 contracts carry no scope guards. The guards that exist are derived from the syllabus’s own structure, not from an A Level boundary. Stay inside your contract’s objective list and you will not need them.
- Exposure is measured by matching question wording to syllabus wording. 13 of parts did not match any objective and were reported rather than distributed.
