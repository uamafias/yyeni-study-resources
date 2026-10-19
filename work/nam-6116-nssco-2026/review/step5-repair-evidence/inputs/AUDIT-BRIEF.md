# Brief: audit AO and Bloom labels against what each prompt asks the learner to do (READ-ONLY)

You are an independent reviewer. You change NOTHING in the workspace and propose, never apply. Output only the JSON file named in your task.

Workspace: /Users/yyeniai/yyeni-study-resources/work/nam-6116-nssco-2026. Your items: the items_<GROUP>.json file named in your task (each record has the item's prompt, answer, guidance, current AO, Bloom, command word, tariff and the planned AO demand note from the approved work order).

## Context you need (read these)
- planning/ao_operator_review.json and planning/ao_demand_audit.json (rule and operator decisions), PLAN-6116-nssco-biology.md section on the AO approach (grep "AO" and "demand"), and the AO text of the syllabus as summarised in curriculum/syllabus-facts.json (search its assessment objectives).
- AO crosswalk in this workspace: AO1 = A (knowledge with understanding: recall, definitions, taught explanations, taught comparisons/implications); AO2 = B (handling information and problem solving: consequential processing of supplied information or data, application to a situation that needs actual inference or calculation, genotype inference, interpreting a table/graph/key, reasoned explanation of a new situation); AO3 = C (experimental skills and investigations: planning, observing and recording, interpreting and evaluating results of an investigation, method and error evaluation, drawing from a specimen).
- Rule from the operator: classify the ACTUAL reasoning/processing demanded, not novelty alone and not the command word alone. A table or a standard ratio alone does not make it B. Operator-settled decisions you must PRESERVE: seven generic taught comparison/EVAL slots are A (AO1); genotype inference and full cross derivation are B; consequential information processing is B; actual investigation-method/results demands are C. Two documented boundaries stay as recorded and must not be proposed for change: breastfeeding study-pattern items (3-437 CHAIN A, 3-438 APP B provisional) and genetic-ratio recognition versus derivation (4-110 CALC B, 4-111 WHY B provisional).
- Bloom labels follow the cognitive demand of the task. Bloom Evaluate can be defensible for a balanced judgement; Create for planning an investigation even if the opening verb is "Describe". Do not propose relabelling by command-word alone. Do not propose changes just to move the AO percentages; there is no quota. Do not propose adding or removing items.

## What to do
For EVERY item in your file decide: does the current AO label match what the prompt really asks the learner to do (given the answer and guidance)? Does the Bloom label? Does the command word describe the task? Then write the JSON list of ONLY the items where you propose a change, plus the items that are real boundary cases which you recommend keeping unchanged. Be conservative: propose a change only when you are confident a teacher would agree; otherwise mark it a boundary case and keep. Never invent reasons.

## Output (JSON list, write with the Write tool to the path in your task)
[{"item_id": "...", "verdict": "change" | "boundary_keep",
  "prompt_demand": "one sentence: what the learner actually has to do",
  "current": {"AO": ["AO1"], "bloom": "Apply", "command_word": "state"},
  "proposed": {"AO": ["AO2"], "bloom": "Understand", "command_word": "state"},   (for boundary_keep, repeat current)
  "reason": "one or two sentences",
  "uncertainty": "low|medium|high and what would change your mind",
  "touches_operator_decision": false}]
Then reply with under 150 words: counts (items read, proposed AO changes, proposed Bloom changes, command-word changes, boundary cases) and any systematic pattern. Commands words must come from the syllabus list used in this workspace (the item's current command word or one of the 18 in curriculum/syllabus-facts.json); if the command word does not describe the task say so but only propose one you can justify; changing a command word may change the tariff rules, so flag it.
