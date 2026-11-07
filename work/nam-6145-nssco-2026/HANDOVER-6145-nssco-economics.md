# Handover prompt — 6145 NSSCO Economics

Jeremy approved the plan on 7 November 2026. Use after the human plan commit. Owner Jeremy; authoring tool Codex. Current stage is planning, not authoring permission.

## Start here

Read AGENTS.md and TEAM-PLAYBOOK.md, then this subject's PLAN-6145-nssco-economics.md, subject-profile.yaml, curriculum/answer-shapes.json, curriculum/glossary.json and the AUTHOR role when step 5 starts. This handover wins over generic authoring instructions, but the team playbook controls order and human checkpoints. Do not reopen another subject or regenerate the plan.

## The job

Author 458 items: 378 flashcards and 80 composite tasks, across 28 topics and 197 assessable objectives. Full notes total 49,260–70,760 words. Topic order:

```text
1.1   Basic economic problem: scarcity and exercise of choice
1.2   Types of economic systems and economic resources
1.3   Specialisation and division of labour
2.1   Business organisations
2.2   Trade unions and employer association
2.3   Financial institutions
3.1   What is a market?
3.2   Market forces
3.3   Price elasticity
3.4   Advertising
3.5   Policies
4.1   Occupational choices
4.2   Earnings
4.3   Expenditure
5.1   The private firm as producer and employer
5.2   Productivity
5.3   Production costs and revenue
5.4   Economies and diseconomies of scale
6.1   Government as producer and employer
6.2   Government economic policies
6.3   Government control
7.1   Prices
7.2   Employment
7.3   Output
7.4   International trade
8.1   Population
8.2   Living standards
9.1   Conflicts
```

For each topic read its generated contract and work_order, plus the matching records in planning/performance-specs.json. Write claims/canonical_claim_ledger.json, the named content-units file and learning-items/topic_<T>_items.json. The renderer chooses the markdown filename. Main topics currently contain plans only; the isolated exemplar is not completed topic output and must not be copied into main topics wholesale.

## Every item carries its labels

Use the slot ID as item_id. Copy subtype or item_type, assessment_objectives, blooms_level, command_word and mark_tariff. Composite totals are sums of their observed part tariffs. MISCON items copy misconception_entry. Claim IDs resolve to original claim statements; every item-objective mapping is supported by a cited claim, and the notes teach that claim. Set revision 1 initially; claims_seen records cited revisions and authored_hash is SHA-256 of _artefact_text. All new derivatives have qa_status review_required; claims stay unverified and publishable false.

## Rules that come from the syllabus and the corpus

Follow the plan's command/tariff table and economic answer shapes. Full context and data live in the item prompt. A two-mark Paper 1-style application can carry A while Bloom is Apply. Do not convert every B into C by adding the word judgement. Four-mark explanations develop mechanisms; evaluations genuinely weigh opposing arguments and a decisive condition. State the exact marking elements and an allocation that totals the item's parts.

Teach every source objective and every listed member, including objectives with zero direct frequency. Preserve original wording only as internal syllabus metadata. Write every learner scenario, question, answer and rubric originally. No reproduced exam scenarios, real named companies, copied mark-scheme answers or assessment-frequency claims. Use the glossary and conceptual boundaries. No unverified current legal/numerical assertions. Keep marginal revenue limited to distinguishing it from average revenue and the source-evidenced profit-maximisation treatment; do not expand it into a separate advanced unit.

For diagrams, supply clean schedules and construction/interpretation instructions for the learner to plot. The standard has no demand/supply renderer; do not use break-even art for it, hand-author fences or claim that a nonexistent diagram is verified. Keep short-run diminishing returns distinct from long-run scale effects and state the conditions on causal claims.

## Voice

Plain British English, connected explanatory prose, invented Namibian or southern African scenarios and N$. Notes are a standalone teaching resource. Worked examples explain the steps and economic meaning, not just the result. No filler added to meet counts and no instructional implementation details in learner prose.

## The work order is a baseline, not a cage

A genuinely unsuitable slot is reported with objective, proposed change and reason in topics/<T>/authoring_notes.json as {from, to, why}. Preserve totals and labels unless a deviation is justified. Do not add high-level content to make a seven-mark question easier to write. The paired evaluation plans use the explicit first/second conditions in performance-specs.json, not duplicated wording. Narrow descriptive topics have no essay-plan slot. Follow topic ownership and definition rulings; actual N$ exchange examples must respect the rand peg documented in jurisdiction-sources.json. Separate supplied data from worked results. Learner prompts/context contain the inputs and task only; canonical answers and separately labelled teaching explanations contain the solution. Read the exemplar and the 3.2/5.3 shape slices; copy their rubric discipline and data consistency, never their scenarios.

## Finishing each topic

Run the standard render_notes.py, run_checks.py and what_to_fix.py with this workspace and topic. Read the JSON verdict as well as exit status: the current run_checks wrapper expects an older pass string while the suite returns publish. Fix every fail; never call not_run a pass. Report inapplicable checks separately with their reason, and investigate missing applicable inputs. Stop after three unsuccessful attempts on the same real check and record the blocker, then continue other topics as the playbook directs.

## Boundaries

Do not edit standard/, sources/, another subject, curriculum files, the exemplar or generated work orders while authoring. Do not commit or push. The person commits at playbook checkpoints. Do not treat deterministic success as human or cross-vendor review. The required reviewer after Codex authors is Claude.

## Report back when the subject is finished

Under 250 words: topics completed/blocked, claims/units/items/notes totals, final check verdicts, remaining not_run checks and warnings, deviations, plan problems and whether publication was performed. Update STATUS.md throughout. No material is published during step 4.
