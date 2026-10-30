# Codex handover: verify Claude's 6137 cross-review repairs

Workspace: `work/nam-6137-nssco-2026/`. Your role is Reviewer, verifying another vendor's repairs. Read `review/crossreview-report-6137.md` first. No Git, upload, import or publication is authorised by this handover. Keep 0455 and the other subjects untouched.

1. **Text repairs.** Check the repairs logged in `review/crossreview-text-changes-6137.jsonl`: 168 blocks and 147 items, with before and after text and issue ids.
   - Check each for accuracy, NSSCO level, original wording and rubric/tariff fit.
   - The findings are in `review/crossreview-findings-6137-g1…g6.yaml`.
2. **New claims.** Verify the 107 new claims (`CROSSREVIEW-6137` evidence; status `unverified`) against their cited sources. Start with the weakly sourced ones listed in report §5.
3. **Visual re-acceptance.** Re-run visual acceptance for the 10 resources whose bound card text changed. The images are unchanged.
   - Resources: VIS-6137-1.5-05/06/07/08, 3.3-01/02, 4.1-01/02/03 and 4.2-03.
   - Three reviewed notes blocks also changed: BL-6137-3.3.01-05, BL-6137-3.3.04-14 and BL-6137-4.1.04-09.
   - You may update the stale "awaiting Codex visual review" `context.situation` text at the same time.
4. **Checks.** Rerun `run_checks.py` on any topic you change, plus copied wording against `assessment-evidence/extracted`, and run `authoring/publish_guarded_6137.py` read-only.
5. **Do not create** `review/subject-acceptance-6137.json`. Claude records it only after the 2.2/2.6 maps are approved, authored and accepted, and after your verification.

Return a verdict, the defects and repairs, the checks run, and the remaining blockers.
