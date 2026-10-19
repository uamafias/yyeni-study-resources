# Framework reports for the framework owner (standard/ is not edited in this lane)

Date: 2026-10-19. Each item: code path, expected, actual, minimal example, and the workaround used in the Biology workspace.

## Withdrawn
- **C-35 "business chart" failure on Biology graph prompts** (reported earlier as a framework defect). Withdrawn: `depictions.chart_model: none` is the supported switch (yyeni_checks.py:581-583, CHANGELOG CR-006) and the Biology profile had omitted it. Fixed in `subject-profile.yaml`.

## Open

1. **publish_subject.py exports held items.** `build/publish_subject.py` `collect()` and `publish()` read every item of every topic and ignore `authoring_notes.json` and `visuals_pending`. Its generated INDEX.md calls the output "the copy to upload". Expected: a deterministic refusal or omission for items whose required figure is unsupplied, and an INDEX that does not call an unreleased draft an upload. Actual: all 35 held Biology items would ship. Workaround: `topics/build_review_package.py` runs the standard builder on a filtered copy, writes only to `review-package/`, and refuses to run if `publish/nam-6116-nssco-2026` exists.
2. **Learner notes header names the internal workspace and the pipeline.** `build/render_notes.py` line 3 of every note: "*<workspace slug>. Offline study notes, rendered from the approved content units on <date>. Everything here is also what the flashcards are built from.*" Expected: learner-appropriate text. Not hand-edited here.
3. **"What this topic asks of you" is built only from `learner_objective` blocks.** `build/render_notes.py` lists those blocks and nothing else, so a topic whose units mostly lack them shows a blurb covering two objectives (topic 3 showed only osmosis and active transport). Workaround: the two exemplar-derived units' blocks were removed in a script copy so the blurb no longer misleads. Expected: either a blurb generated from all units or none.
4. **run_checks.py exits 1 on a clean PUBLISH.** `checks/run_checks.py` final exit compares `release_decision` with `pass`; a clean report is `publish`. `what_to_fix.py` exits 0 on the same report. `topics/scratch_check.sh` uses `what_to_fix.py` for the verdict.
5. **YAML silently optional.** `yyeni_checks.py:_yaml()` returns `None` when PyYAML is missing, so every profile-dependent check runs as if the profile were empty and the C-35 default (break-even) applies. Expected: a hard error. Seen with system `python3`.
6. **No route for biological images** (render_chart.py, C-41 support break-even charts only), **C-24 has no post-review state** (any verification.status other than null or unverified fails), **make_contract.py:34 word budgets ignore the subject profile**, **make_work_order.py:281 `sub_topic()` truncates to three levels**, **make_work_order.py:455-471 can emit a null command word or empty marking parts without a warning**. Details as in review/CODEX-PLAN-REVIEW-2026-10-18.md.
