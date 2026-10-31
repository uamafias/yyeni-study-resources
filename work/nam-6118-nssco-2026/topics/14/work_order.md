# Work order — 14 Heat capacity and changes of state

*standard make_work_order.py plus planning/bind_task_specs.py (explicit task bindings; item counts unchanged)*

18 assessable objectives · 23 planned items · 2 content units

## Planned AO mix by item count (reported, not targeted)

| AO | planned | item-count target |
|---|---:|---:|
| A | 76% | 47% |
| B | 24% | 28% |
| C | 0% | 25% |

## Planned AO mix in marks-equivalent — the measure the syllabus uses

| AO | planned | syllabus weight |
|---|---:|---:|
| A | 51% | 47% |
| B | 26% | 28% |
| C | 24% | 25% |

68 marks-equivalent of practice in this topic.

> The syllabus states its AO weights as a share of MARKS, so planned_ao_mix_by_marks is the one that answers "does this resource match the exam". It values each card at the tariff of the question it models, split across the AOs the card declares, and values each performance task at the marks of the paper part it models. The count-based mix below is reported only because it is what a reader expects to see; do not balance against it. AO shares by ITEM COUNT: Every objective needs one recall anchor, so AO1 has a structural floor of about 86% in this topic (18 objectives against 21 slots) and cannot reach the None% target by count however many other cards are added - padding the bank to chase it makes the resource worse. The framework already measures the AO4 share in practice time rather than by count for the same reason. Treat AO1 above target as expected, and AO2/AO3/AO4 below target as the thing worth fixing.

## Content units

**CU-6118-3.2.2** — sub-topic 3.2.2, 12 objectives, 1583–2510 words
- `OBJ-6118-3.2.2-01` tier 2 — relate a rise in the temperature of a body to an increase in internal energy
- `OBJ-6118-3.2.2-02` tier 2 — explain the term thermal capacity
- `OBJ-6118-3.2.2-03` tier 1 — define heat capacity of an object [C] as the heat required [Q] to raise its temperature [∆𝑇] by one kelvin
- `OBJ-6118-3.2.2-04` tier 2 — Use heat capacity C = Q/ΔT.
- `OBJ-6118-3.2.2-05` tier 1 — define specific heat capacity [c] as the heat required [Q] to raise the temperature of a 1 kg mass [m] of a substance by one kelvin
- `OBJ-6118-3.2.2-06` tier 2 — Use specific heat capacity c = Q/(mΔT).
- `OBJ-6118-3.2.2-07` tier 2 — describe an experiment to measure the specific heat capacity [c] of a substance
- `OBJ-6118-3.2.2-08` tier 2 — describe an investigation to establish that the temperature increase is proportional to the time of heating (for a constant mass) and inversely proportional to mass (for a constant time of heating)
- `OBJ-6118-3.2.2-09` tier 1 — define latent heat [L] as the quantity of heat energy [Q] absorbed or released when a substance changes state without changing its temperature (L = Q)
- `OBJ-6118-3.2.2-10` tier 1 — define specific latent heat [l]as the quantity of heat energy [Q] absorbed or released when a 1 kg mass [m] of a substance changes state without changing its temperature
- `OBJ-6118-3.2.2-11` tier 2 — use the term, and give a molecular interpretation of latent heat [L]
- `OBJ-6118-3.2.2-12` tier 2 — Use specific latent heat l = Q/m.

**CU-6118-3.2.3** — sub-topic 3.2.3, 6 objectives, 791–1255 words
- `OBJ-6118-3.2.3-01` tier 2 — describe melting and boiling in terms of energy input without a change in temperature
- `OBJ-6118-3.2.3-02` tier 4 — define melting point and boiling point as the temperature at which a change of state occurs
- `OBJ-6118-3.2.3-02-M01` tier 1 — Define melting point
- `OBJ-6118-3.2.3-02-M02` tier 1 — Define boiling point
- `OBJ-6118-3.2.3-03` tier 2 — distinguish between boiling and evaporation
- `OBJ-6118-3.2.3-04` tier 2 — plot and interpret heating and cooling curves of water

## Item slots

| Slot | Objective | Subtype | AO | Command word | Tariff | Why |
|---|---|---|---|---|---:|---|
| `001-MECH` | relate a rise in the temperature of a body to an increase in internal energy | MECH | A | Explain | 2 | instructs with Explain, which this objective carries |
| `002-MECH` | explain the term thermal capacity | MECH | A | Explain | 2 | instructs with Explain, which this objective carries |
| `003-DEF` | define heat capacity of an object [C] as the heat required [Q] to raise its temperature [∆𝑇] by one kelvin | DEF | A | Define | 1 | instructs with Define, which this objective carries |
| `004-CALC` | Use heat capacity C = Q/ΔT. | CALC | B | Calculate | 2 | instructs with Calculate, which this objective carries |
| `005-DEF` | define specific heat capacity [c] as the heat required [Q] to raise the temperature of a 1 kg mass [m] of a substance by one kelvin | DEF | A | Define | 1 | instructs with Define, which this objective carries |
| `006-CALC` | Use specific heat capacity c = Q/(mΔT). | CALC | B | Calculate | 2 | instructs with Calculate, which this objective carries |
| `007-PROC` | describe an experiment to measure the specific heat capacity [c] of a substance | PROC | A | Describe | 1 | instructs with Describe, which this objective carries |
| `008-PROC` | describe an investigation to establish that the temperature increase is proportional to the time of heating (for a constant mass) and inversely proportional to mass (for a constant time of heating) | PROC | A | Describe | 1 | instructs with Describe, which this objective carries |
| `009-DEF` | define latent heat [L] as the quantity of heat energy [Q] absorbed or released when a substance changes state without changing its temperature (L = Q) | DEF | A | Define | 1 | instructs with Define, which this objective carries |
| `010-DEF` | define specific latent heat [l]as the quantity of heat energy [Q] absorbed or released when a 1 kg mass [m] of a substance changes state without changing its temperature | DEF | A | Define | 1 | instructs with Define, which this objective carries |
| `019-MISCON` | define specific latent heat [l]as the quantity of heat energy [Q] absorbed or released when a 1 kg mass [m] of a substance changes state without changing its temperature | MISCON | A | Explain | 2 | discriminates misconception MIS-09 (1 examiner statements): Specific latent heat concerns phase change per unit mass; specific heat capacity concerns temperature rise per unit mass. |
| `011-MECH` | use the term, and give a molecular interpretation of latent heat [L] | MECH | A | Explain | 2 | instructs with Explain, which this objective carries |
| `020-MISCON` | use the term, and give a molecular interpretation of latent heat [L] | MISCON | A | Explain | 2 | discriminates misconception MIS-10 (1 examiner statements): Energy supplied during a constant-temperature phase change changes intermolecular potential energy rather than increasing average kinetic energy. |
| `012-CALC` | Use specific latent heat l = Q/m. | CALC | B | Calculate | 2 | instructs with Calculate, which this objective carries |
| `013-MECH` | describe melting and boiling in terms of energy input without a change in temperature | MECH | A | Explain | 2 | instructs with Explain, which this objective carries |
| `014-SYNTH` | define melting point and boiling point as the temperature at which a change of state occurs | SYNTH | A/B | Explain | 2 | instructs with Explain, which this objective carries |
| `015-DEF` | Define melting point | DEF | A | Define | 1 | instructs with Define, which this objective carries |
| `016-DEF` | Define boiling point | DEF | A | Define | 1 | instructs with Define, which this objective carries |
| `017-DIST` | distinguish between boiling and evaporation | DIST | A | Explain | 2 | instructs with Explain, which this objective carries |
| `018-INTERP` | plot and interpret heating and cooling curves of water | INTERP | B | Draw | 2 | instructs with Draw, which this objective carries |

## Performance tasks

- **multiple_choice_set** — Create 12 original four-option, one-mark MC questions for this topic. State each key and explain every distractor. Include both knowledge and application; the A/B split is a practice-design estimate, not an official code for individual items. Topic-specific binding: Heating a fixed 0.20 kg sample with negligible loss in this model. Use the stated objective IDs and the original stimulus specification. Introduce every physical relation used; do not reuse exemplar values. Topic-specific binding: Heating a fixed 0.20 kg sample with negligible loss in this model. Use the stated objective IDs and the original stimulus specification. Introduce every physical relation used; do not reuse exemplar values. Topic-specific binding: Heating a fixed 0.20 kg sample with negligible loss in this model. Use the stated objective IDs and the original stimulus specification. Introduce every physical relation used; do not reuse exemplar values.
- **short_answer** — An original eight-mark structured task: two one-mark knowledge parts, one two-mark definition/explanation and two two-mark applications or calculations. Use checked task architecture and topic-appropriate verbs; replace the structure if the topic is non-numerical and record the reason. Topic-specific binding: Heating a fixed 0.20 kg sample with negligible loss in this model. Use the stated objective IDs and the original stimulus specification. Introduce every physical relation used; do not reuse exemplar values. Topic-specific binding: Heating a fixed 0.20 kg sample with negligible loss in this model. Use the stated objective IDs and the original stimulus specification. Introduce every physical relation used; do not reuse exemplar values. Topic-specific binding: Heating a fixed 0.20 kg sample with negligible loss in this model. Use the stated objective IDs and the original stimulus specification. Introduce every physical relation used; do not reuse exemplar values.
- **practical_task** — An original 16-mark practical task in an in-scope physical context: construct a graph (5), derive and interpret its gradient (3), then plan an investigation (8). Provide realistic invented data with units, a complete operational method, controls, a results table and a data-based conclusion. Use the task-specific source anchors; do not label a reciprocal gradient as density or stiffness. This practices components, not a fixed complete Paper 3 question. Topic-specific binding: Heating a fixed 0.20 kg sample with negligible loss in this model. Use the stated objective IDs and the original stimulus specification. Introduce every physical relation used; do not reuse exemplar values. Topic-specific binding: Heating a fixed 0.20 kg sample with negligible loss in this model. Use the stated objective IDs and the original stimulus specification. Introduce every physical relation used; do not reuse exemplar values. Topic-specific binding: Heating a fixed 0.20 kg sample with negligible loss in this model. Use the stated objective IDs and the original stimulus specification. Introduce every physical relation used; do not reuse exemplar values.

## Excluded from this topic

Limits the syllabus states, enforced by C-11 in everything a learner reads: Collision definitions (syllabus PDF 14; topic 2.4); Nuclide formulae in energy-source teaching (syllabus PDF 17; topic 2.10.1); Standalone diverging-lens theory (syllabus PDF 28; topic 4.3.3)
