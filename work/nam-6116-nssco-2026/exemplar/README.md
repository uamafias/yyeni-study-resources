# 6116 Biology structural exemplar

Generated content by `planning/make_exemplar.py`; this README by `planning/write_exemplar_readme.py`. Slot ids and labels are read from the live work orders, unit budgets from `curriculum/notes-budget.json`.

- **3: the whole of 3.3.2 Osmosis and 3.3.3 Active transport: the representative section.** 25 items (APP, CHAIN, DEF, FEATURE, LIM, MISCON, PROC, SYNTH, WHY, multiple_choice_set, practical_task, short_answer). Osmosis 1401 words (budget 920-1440); Active transport 584 words (budget 500-800). 29 claims, 22 of them citing an approved reference.
- **4: part of 4.4.2 Monohybrid inheritance (two objectives).** 5 items (CALC, DEF, MISCON, WHY, short_answer). Monohybrid inheritance 364 words (budget 230-370). 7 claims, 7 of them citing an approved reference.

What it models: a Key points block opening each unit; concise canonical answers; complete investigation plans (SYNTH, 5 marks); "discuss" cards written as developed points; a full genetic diagram (5 marks); evidence entries on claims; practical-procedure claims flagged for the teacher verifier.

**Reuse.** Group 3A starts units 3.3.2 and 3.3.3 from this exemplar, which already is those units, and completes them against the work order. Topic 4 extends the 4.4.2 slice to the whole unit. Nowhere else reuse its scenarios. Copy its shape everywhere.

Proof: both slices are installed in a scratch copy of the workspace, with each topic's registry branch cut to the slice objectives in the copy only. The notes are rendered, and `run_checks.py` and `planning/check_unit_budgets.py` are run. Both read PUBLISH; the only warning is C-18 (per-topic AO mix by item count, reported). C-39 passes; C-35, C-41 and C-43 do not apply (no generated depiction or practice text). The checks verify structure, scope and arithmetic, not scientific truth: the claims stay unverified until the teacher verification step.
