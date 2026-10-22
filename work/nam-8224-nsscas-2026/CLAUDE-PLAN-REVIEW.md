# Claude review — NSSCAS Chemistry 8224 corpus analysis and draft plan

**Review method:** Claude Code terminal, Opus, read-only plan mode  
**Date:** 22 October 2026  
**Verdict:** **REVISE**

Claude changed no repository files and did not use the web or YYeni. This review was explicitly requested as an exception to the standing preference that Claude normally reviews once after the complete resource set.

## Overall finding

The evidence base and overall resource design are sound, but the generated work orders do not fully implement what the corpus analysis and plan require. Several generator-input defects would be copied into all 21 topics. The curriculum inputs and subject profile should therefore be corrected and every contract/work order regenerated before the plan is approved or the exemplar is authored.

## Blockers

### 1. No misconception cards were generated

- The subject profile expects one `MISCON` slot per misconception, and the corpus analysis plans 19 of them.
- Each misconception currently stores a subtopic such as `1.1.5` as its `topic_id`, while the work-order generator matches whole topics such as `1.1`.
- All 19 entries are therefore silently dropped.

**Required change:** store the whole topic in `topic_id`, retain the subtopic separately if needed, and regenerate.

### 2. No equation-writing cards were generated

- The subject profile defines `chem_equation`, but no objective in the registry uses that type.
- Important examples are mistyped:
  - 1.1.5-01, balanced equations;
  - 2.2.1-03, balancing using oxidation numbers;
  - 2.2.2-04, ionic half-equations.
- The local corpus contains substantial equation-writing demand, but no generated slot uses `Write`, `Construct`, `Give`, `Name` or `Complete`.

**Required change:** retype the relevant equation and reaction objectives and generate explicit equation-writing practice.

### 3. Calculation objectives are mistyped or under-practised

- 1.4-03, `pV = nRT`, is typed as a description and receives no calculation card.
- 2.1.2-01/02, Hess cycles and calculations, are typed as concepts and receive no calculation slot.
- Only 32 calculation cards exist and all carry a one-mark tariff, despite the answer structure requiring an equation, conversion, substitution, working, answer, unit and significant figures.
- 1.1.5-02 combines reacting-mass, gas-volume and solution calculations into one one-mark calculation card.

**Required change:** type quantitative objectives correctly, split materially different calculation strands, and allow two- and three-mark calculation cards.

### 4. Definition cards are over-generated

- There are 210 `DEF` slots, although only three objectives are typed as definitions.
- This produces unsuitable prompts such as “Define” for analysing an infrared spectrum, calculating percentage by mass, or interpreting volatility.

**Required change:** generate `DEF` only when the objective actually names a term or definition. Use `FEATURE`, `INTERP`, `CALC`, `DIAGRAM`, `EQUATION` or another fitting subtype elsewhere.

### 5. The electric-field requirement is absent from the registry

- The general 1.2.1 syllabus objective includes behaviour of particles in electric fields.
- The corpus analysis and plan identify it as examinable, and misconception MC-8224-05 depends on it.
- No objective or card slot presently covers it.

**Required change:** add an assessable objective under 1.2.1, or amend the relevant existing objective so the requirement is explicit.

### 6. The two-source and human-review gates need decisions

- `STATUS.md` says a claim supported by only one source cannot publish.
- The objective registry currently gives every objective secondary-source coverage rating zero, so the rule would block the entire subject.
- The plan also names a human Chemistry review, while Jeremy’s preferences say unavailable teacher access must not become a prerequisite.

**Jeremy’s decisions required:**

1. Define what counts as a second source—for example, distinct syllabus annexes/data material or a second independent AI review.
2. Decide whether human Chemistry sampling is a publication blocker or a recommended labelled check.

### 7. Step 4 deliverables remain incomplete

- `HANDOVER-8224-nsscas-chemistry.md` is missing.
- The structural exemplar is missing.

These remain required before Step 4 can be marked complete.

## Major issues

### 8. AO padding contradicts the playbook

- Fifty-four `FEATURE` slots were added solely to raise AO A to its target.
- Some repeat existing definition cards.
- The playbook forbids padding the item bank merely to chase an AO percentage.

**Required change:** remove artificial top-up cards, add the missing genuine misconception/equation/knowledge practice, and recalculate AO coverage.

### 9. Bloom mappings are inconsistent

The plan and framework disagree:

| subtype | plan | framework |
|---|---|---|
| FEATURE | Remember | Understand |
| DIST | Understand | Analyse |
| MECH | Understand | Analyse |

There are also 98 `SYNTH` cards labelled Create, including simple or one-mark calculations. Joining objectives does not automatically make a task Bloom Create. Performance tasks are assigned a largely fixed Bloom level irrespective of their actual demand.

**Required change:** reconcile the plan and framework and assign Bloom levels from the learner action rather than card construction.

### 10. Command-word distribution is distorted

| command word | generated slots | corpus parts |
|---|---:|---:|
| Explain | 232 | 17 |
| Suggest | 175 | 13 |
| Define | 134 | 6 |
| Determine | 78 | 3 |
| Write | 0 | 13 |
| Give | 0 | 16 |
| Name | 0 | 7 |

`Sketch` is also inconsistent: the draft plan allows it from 2025 evidence, while the assessment framework marks it as never used.

**Required change:** rebalance prompt openings against objective meaning and corpus evidence, then reconcile the `Sketch` verdict.

### 11. Performance tasks are under-specified

- The 64 task slots lack assessment objectives, command words and mark tariffs.
- Their objective field tells the author to choose two to four objectives, leaving planning judgement unresolved.
- Every content topic gets a 12-question multiple-choice set, regardless of whether it contains three objectives or 25.
- Those approximately 240 component questions are not reflected in the stated 994-item total.

**Required change:** preassign each task’s objectives, AOs, command words and tariff; scale multiple-choice sets by topic size; make the counting basis explicit.

### 12. Practical skills are modelled too repetitively

- Topic 5.1 gives nearly every one of its 39 practical criteria the same four- or five-card pattern, producing 170 cards plus four tasks.
- Its 12,870–18,330-word notes allocation is larger than any content topic.
- The four task families themselves are well chosen, but their objective and AO-C coverage is not explicitly assigned.

**Required change:** use roughly two targeted cards per practical criterion, place much of the integrated coverage in practical tasks, and explicitly map every practical task to Annexe A objectives and AO-C marks.

Claude recommends splitting the mixed thermometric/gravimetric/rates task, adding a second redox-titration task, and capping practical notes at approximately 6,000–8,000 words.

### 13. Contract exclusions and adjacency are too generic

- All contracts repeat the same subject-wide exclusions instead of clarifying what neighbouring topics own.
- Some adjacent-topic links appear keyword-derived and implausible—for example, 4.1 linked to Group 2 and Group 17, and 1.1 linked only to Hydrocarbons.
- Generated `ao_mix_note` text refers to AO1, AO4 and “None%”, apparently inherited from another subject.

**Required change:** repair subject-specific adjacency and exclusions. Report the shared-standard `ao_mix_note` defect rather than hand-editing generated work orders.

## Answers to the requested review questions

### Coverage and resource types

The plan covers all 252 currently registered assessable objectives and includes the right overall resource types: notes, flashcards, multiple-choice sets, structured questions, calculations and practical work.

Material gaps remain:

- electric-field behaviour;
- equation-writing practice;
- sufficient calculation practice;
- explicit attachment of the mathematical requirements, Annexe B quantities/units and Annexe C organic representation conventions.

Practice density is currently too flat: most objectives receive roughly the same number of cards regardless of exposure or complexity.

### Use of the local corpus without mark schemes

The method is sound for syllabus coverage, observed command words, tariffs and question types, provided the limitation remains explicit. Annexe A supplies several practical credit criteria directly. Structured-answer precision should stay bounded by the syllabus, annexes/data material and the 2025 examiner report. Missing mark schemes should be labelled as an evidence limitation rather than stopping the build.

Misconception items can test genuine chemical distinctions without presenting them as frequency claims about examiners.

### Assessment objectives

Using the syllabus’s printed 40/40/20 AO target is defensible. The syllabus’s paper percentages and raw marks do not reconcile perfectly, so that conflict should remain documented. The five-point AO gate currently passes partly because of artificial padding; it must be rerun after the substantive fixes.

### Volume

The draft is overbuilt in low-value repetitive cards and too thin in equation/calculation practice.

Claude’s approximate revision:

| change | cards |
|---|---:|
| Remove AO-padding slots | -54 |
| Reduce Topic 5.1 to two targeted cards per objective | -92 |
| Remove unsuitable definition anchors | approximately -117 |
| Add misconception cards | +19 |
| Add equation cards | approximately +30 |
| Add calculation cards and strands | approximately +10 |

Recommended result: approximately **725 cards and 66 performance tasks**, or around **790 counted items**, within the playbook’s normal 400–900 range. Revised total notes would be approximately **65,000–92,000 words**.

### Topic 5.1

The practical task families match the evidence; the flashcard pattern does not. Integrated practical tasks should carry much of the assessment and explicitly cover the 39 Annexe A criteria. Rename the topic simply “Advanced practical skills”.

### Topic 1.1 exemplar

Topic 1.1 remains the correct content exemplar because it carries high exposure and the clearest calculation-related learner difficulties. It must be regenerated first so it does not model the existing defects. Claude also recommends a thin practical exemplar slice from Topic 5.1, such as one titration task and its supporting cards.

### YYeni repairs

The repairs belong in the existing NSSCAS Chemistry classroom; no new classroom is required. The evidence supports:

- repairing objective records in lessons 6626, 6658, 6674, 6832 and 6508;
- adding the missing Topic 1.2 lesson to the existing classroom;
- moving the Group 2 lesson to the correct existing section.

Before any preview, re-read the live state and confirm the misplaced lesson is 6658. Curriculum repair is necessary before import/mapping, not before repository authoring from verified syllabus objectives.

Still required for platform work:

- a crosswalk from 213 content objectives to the 202 existing YYeni objective records;
- a decision on where Topic 5.1 resources attach without creating a new section;
- an exact preview and Jeremy’s approval before any live change.

## Regeneration risks

- Fixes belong in the curriculum inputs and `subject-profile.yaml`; do not hand-edit generated work orders.
- Rerun `conform_registry`, `make_contract`, and `make_work_order --all` after correcting the inputs.
- Regeneration will renumber slot IDs. That is safe now because no Chemistry items have been authored, but the work orders should be frozen after the exemplar is accepted.
- Use `subtype_waivers` where a generated subtype genuinely does not fit.
- The analysis and exposure files use different mark-counting bases for Topic 1.1; label those bases rather than comparing the numbers directly.

## Required changes before approval

1. Repair misconception topic identifiers.
2. Retype equation and calculation objectives.
3. Add the electric-field objective.
4. Remove AO padding and inappropriate definition anchors.
5. Correct calculation tariffs, SYNTH Bloom labels and Topic 5.1 density.
6. Fully specify performance-task metadata and objectives.
7. Rename 5.1 and repair adjacency/exclusion data.
8. Reconcile the plan with the framework, including `Sketch` and Bloom mappings.
9. Regenerate all 21 contracts/work orders and rerun AO coverage without padding.
10. Create the handover and content/practical exemplar slices.
11. Record Jeremy’s decisions on the second-source rule, human Chemistry sampling and author/reviewer role wording.

## Safe next action

Repair the planning inputs and regenerate the plan artifacts. This is repository-only planner work: it requires no YYeni changes and creates no flashcards. After Jeremy’s policy decisions, author the corrected Topic 1.1 exemplar and a thin Topic 5.1 practical slice. Prepare live YYeni repairs only as a fresh, exact preview for separate approval.
