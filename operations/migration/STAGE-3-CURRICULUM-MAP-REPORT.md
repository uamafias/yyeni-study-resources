# Pipeline Stage 3 — global curriculum map, Cambridge AS Business 9609

**Executed:** 2026-08-31 · **Pipeline state:** `INVENTORIED` → **`MAPPED`**

Four artifacts in `work/cie-9609-as-2026-2028/curriculum/`.

## Answering the question directly: yes, Stage 3 was the right place — for most of it

| What you asked for | Where it now lives | Status |
|---|---|---|
| Assessment objectives, with weights | Qualification profile → surfaced in `assessment-framework.json` | Already existed; verified against the syllabus |
| Command words with official meanings | Qualification profile, all nine | Already existed; verified |
| Paper structure, marks, durations, AO weights per paper | `assessment-framework.json` § papers | Extracted |
| **AO and command words attached to every objective** | `objective_registry.json`, fields `assessment_objectives` and `command_words` | **Done — the schema already had these fields** |
| **Command word → AO, mark tariff, paper location, item type, what earns credit** | `assessment-framework.json` § command_words | **New. Did not exist anywhere** |
| **Flashcard subtype → AO** | `assessment-framework.json` § flashcard_subtype_ao_map | **New. Did not exist anywhere** |
| **AO mark budget and target item mix** | `assessment-framework.json` § ao_mark_budget, item_mix_target | **New** |
| AO/command-word intention on each individual card | `learning_items.items[].assessment_objectives` — schema field exists, populated at **Stage 13** | Not yet; the framework is what will drive it |

So: nothing has to wait for a later stage to be *stored*. One thing must not be forgotten later — **Stage 13 must read `assessment-framework.json` when it generates items**, and the hard rules in that file are what make it bite.

One structural point, raised as **CR-001**: these mappings are currently in the workspace, which means they apply to this build only. Subtype→AO belongs in the *subject* profile and command-word→AO in the *qualification* profile, so Economics and the next seventeen subjects inherit them instead of re-inventing them. The change request has the exact YAML to paste.

## The objective registry

**200 objectives — 19 topic parents and 181 atomic objectives — covering all 19 AS topics, 1.1 through 5.5.** Validates against `objective_registry.schema.json`. Unique IDs, every parent and prerequisite reference resolves, every objective carries at least one AO and at least one command word, and only the nine official command words and four official AOs appear anywhere.

Coverage matches the qualification profile's `included_topic_ids` exactly — 19 of 19, no A Level topic present.

Every objective preserves the **exact syllabus bullet wording** in `syllabus_text` (RS-06), including the syllabus's own typo at 1.5.2 ("infuence"), with the corrected form only in the learner-facing `learner_objective`.

### Objective types (from the subject profile's nine)

| Type | Objectives | | Type | Objectives |
|---|---:|---|---|---:|
| Method or strategy | 36 | | Quantitative measure | 23 |
| Concept or definition | 34 | | Process | 13 |
| Comparison | 27 | | Theory or model | 9 |
| Relationship or impact | 26 | | Case/data interpretation | 7 |
| Decision or recommendation | 6 | | | |

### Depth tiers

Tier 1: 15 · Tier 2: 87 · Tier 3: 71 · Tier 4: 8. Against the subject profile's indicative word ranges this projects to roughly **95,000–170,000 words** of learner notes for the AS course, and **1,300–2,400 learning items**. Worth knowing before authoring starts: at 180 guided learning hours, the upper end is more than a learner can read.

### AO reach across the syllabus

| | AO1 | AO2 | AO3 | AO4 |
|---|---:|---:|---:|---:|
| Objectives touching it | 162 | 181 | 131 | 85 |
| Share of the 181 | 90% | 100% | 72% | 47% |

**Forty-seven per cent of AS objectives carry AO4.** Nearly half the course needs an evaluative treatment, not a definition. That single number is the strongest argument for the framework you asked for.

### Command words across the syllabus

Explain 141 · Analyse 130 · Evaluate 71 · Calculate 36 · Advise 24 · Define 20 · Identify 16 · Assess 16 · Justify 5.

Only 20 objectives are Define-shaped. If the finished flashcard set is mostly definitions, it will not resemble the syllabus it came from.

### Provisional source position (RS-11)

Set from what reading the supplied notes actually showed, and marked provisional pending the Stage 8 adequacy audit:

| Action | Objectives | Basis |
|---|---:|---|
| `synthesise` | 94 | Topics 1 and 3 — chapters exist and are substantial, but follow a pre-2023 edition and mix AS with A Level |
| `regenerate` | 51 | Topics 2 and 4 — chapter 2 uses the superseded title and legacy numbering; chapter 4's scope includes A Level project management |
| `generate_gap` | 36 | Topic 5 — no chapter notes exist at all |

**Not one objective is rated `retain`.** That is the honest reading of the evidence and it confirms the R-02 prediction: this is a build, not a clean-up.

## The assessment framework

`curriculum/assessment-framework.json`. All nine command words with official meaning, primary AO, typical tariff, where they appear in the papers, which item types they drive, and what a credit-worthy answer contains. All fifteen flashcard subtypes mapped to AOs — and the subtype list matches the `learning_items` schema enum exactly, so Stage 13 can enforce it.

### The rule that carries the intention

> A topic's learning-item set should distribute across AOs in roughly the qualification's own proportions. Seventy per cent of this qualification lies beyond AO1, so a deck that is mostly definitions is not a light version of the resource — it is the wrong resource.

Target share AO1 30 / AO2 30 / AO3 20 / AO4 20, with five hard rules, including: every tier-3 or tier-4 objective gets an APP item whose context facts change the reasoning; every Analyse objective gets a CHAIN item; every Evaluate/Assess/Justify/Advise objective gets an EVAL item; every quantitative objective gets both CALC and INTERP, because a calculation without interpretation fails RS-22.

### An arithmetic discrepancy

Paper-level AO weights applied to paper marks give **AO1 32, AO2 30, AO3 20, AO4 18** out of 100, against stated qualification weights of **30/30/20/20**. Two marks each on AO1 and AO4. Cambridge publishes both and rounding across two papers explains it — but the validator has a "qualification and paper AO totals" check, so the tolerance should be written down rather than discovered. Recommendation in CR-001: target 30/30/20/20, allow ±3 marks.

## Dependency graph and glossary

`dependency_graph.json` — 25 edges and a recommended topic build sequence. Structural dependencies visible in the syllabus wording; Stage 6 refines them per objective.

`glossary.json` — 10 terms recurring across two or more of the five AS topics, definitions deliberately empty because canonical definitions are authored as claims at Stage 10, not invented here.

**Five of the ten are homonyms, and this is the finding worth carrying forward.** RS-08 says a recurring term inherits one canonical definition. Applied blindly here it would introduce errors:

- **contribution** — the costing term in 5.4 (selling price minus variable cost) versus the ordinary sense in "the contribution of managers to business performance" (2.3) and "the contribution of operations to added value" (4.1)
- **promotion** — marketing promotion in 3.3.5 versus employee promotion as a non-financial motivator in 2.2.4
- **enterprise** — a factor of production, the act of entrepreneurship, and "social enterprise" as an ownership type
- **growth** — business growth (1.3.3) versus market growth (3.1.3), which learners routinely conflate
- **objectives** — business objectives, marketing objectives, and the qualification's assessment objectives

Each is flagged in the glossary with the documented contextual variation RS-08 permits.

## Method, stated plainly

Judgement was applied at **sub-topic granularity — 62 curated decisions** on objective type, AO set, command words and depth tier — then refined per bullet by rules keyed to the syllabus wording ("calculation" → quantitative and Calculate; "advantages and disadvantages" → AO3, AO4 and Evaluate; "appropriateness" or "factors influencing the choice" → decision type with Advise and Justify).

This is a defensible first pass, not a finished decomposition. Two honest limits:

1. **One objective per syllabus bullet.** RS-06 asks for the smallest assessable objectives, and some bullets hold more than one — 1.2.2's list of eight ownership types is the clearest case. Splitting those is Stage 6 work, per topic, and will raise the count above 181.
2. **The `source_coverage` ratings are provisional.** They record what reading the notes showed, not a per-objective audit. Stage 8 replaces them.

## Next

**Stage 4 — assessment-material mining.** Now unblocked in both senses: 84 AS question-paper and mark-scheme pairs are inventoried, and objective IDs exist for evidence records to cite. Mining maps each question to objective IDs, command word, mark tariff, AO focus and context, and records examiner-evidenced misconceptions from the 11 examiner reports.

Two things it will produce that matter beyond this build: the first real measurement of **which objectives actually get examined and at what tariff**, which is what turns the depth tiers above from a judgement into a calibration; and a check on the AO shares in this report against the AO shares Cambridge's own papers exhibit.
