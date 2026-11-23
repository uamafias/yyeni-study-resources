# Owner decision: step 3 waits for the textbooks (8227)

Recorded 2026-11-17 by Claude (reviewer) from Vitalis's reply to `report.md` §4. Author inputs are unchanged. The brief that carries this decision into work is `REPAIR-PROMPT.md` in this folder.

## The question (report §4)

Should step 3 (recipe contract and pilot PLAN) start once the round-5 marking and provenance fixes pass Claude's short check, with textbook completion continuing in parallel? Claude recommended yes.

## Decision

**No. Step 3 starts only after the textbook work is complete and accepted. It does not run in parallel.** This supersedes the reviewer's recommendation.

**Reason (Vitalis):** the textbooks may give useful insights for planning, so the findings should be available when the PLAN is written.

## Consequences

1. The round-3 condition for step 3, "textbook population and answer work completed or explicitly scoped by the owner", is resolved as **completed**. No scoping shortcut applies.
2. Round 5 carries the short marking and provenance fixes (R4-01 to R4-05) and the full textbook completion.
3. The textbook work includes the family-level mining required by `workbench/playbook/textbook-analysis.md` ("Mine exercise families, not isolated numbers"), plus a planning-insights synthesis written for the step-3 planner.
4. Step 3 starts after Claude's check accepts both:
   - the round-5 marking and provenance fixes;
   - the textbook completion: page census, item records, qualifier decisions, answer accuracy, families and insights, and a fresh independent blind sample drawn with a reviewer seed.
