# Handover — NSSCAS Mathematics 8227 repair round 4

17 November 2026. AUTHOR Codex; owner/final decision-maker Vitalis.
Commission: `review/opus-5-5-repair-r3/REPAIR-PROMPT.md`.
**Marking/provenance author repairs are ready for focused review. Textbook
completion is partial. No step 3 PLAN, contract, recipes or runtime generators.**

Read AGENTS.md, TEAM-PLAYBOOK.md, exactly the commissioned role brief, and the
Workbench playbook. All review folders, source PDFs, standard, other subjects,
app code and pinned checkouts are read-only. Preserve unrelated dirty work.
No commits or pushes. No source acquisitions occurred in this round.

## Focused check

1. Verify `analysis/analysis-snapshot.json` and its preserved R3 parent:
   `208a33a2027295d09c84f70423b370aa27e5626df289114842181383ce64389d`.
2. Read `checks/repair-r4-report.md`; review R3-01–08 against the unchanged findings.
   R3-07 is explicitly deferred to step 3 by the commission.
3. Re-read the 821 award rows against `checks/r4/report-YYYY-NNN.png`, using
   `analysis/award-second-read-r4.json`. Check the named 13 marking-changing and
   7 cosmetic corrections, exclusive paths, SC caps, alternatives, F.T. and
   the three derived completions. Reconcile every part, not just question totals.
4. Check consolidated rules against all report contexts and linked award rows.
   `convention-context-scan-r4.json` records every native keyword hit; visual
   table reading supplements extraction. General prose does not erase explicit
   criterion exceptions. Preserve the rejected degree-mode alternative.
5. Review confirmed provenance pairs and four demotions against both rendered
   pages. N1–N10 are pairs020–029; external division is structural030, not a
   proven source. All derived-from labels stay hidden.
6. Reclassify the fresh seeded sample in `analysis/textbook-review-sample.json`
   independently and blind, plus source defects, disputed boundaries and gaps.
   1,933 records are source items, not distinct problem types or accepted recipes.
   `textbook-page-audit-r4.json/.md` provides all 759 target page reads and source
   cautions. Reopen the actual mathematics and answer pages.

## Remaining author textbook work

All 929 discovered headings have dispositions; page/answer comparison subsequently
found missing headingless activities and connected questions. Zero heading backlog
is not an exhaustive population proof. In particular, final independently checked
item/teaching-figure enumeration and value-level qualifier decisions remain open.
Do not mark QUAL01–11 applied merely because every item lists them.

1,913 item answer locator records are separate from 49 independently recomputed
representative results. Finish full answer accuracy before promoting an item to
design evidence. Twenty investigations have explicit author-derived answer notes, separate from printed keys; their complete subtask/graph acceptance still needs independent review. Check continuations and original domain,
branches, angle unit, precision and source cautions. Textbook originals stay internal.
The two assessed-item gaps remain explicit; no routine sampling stop rule is earned.

Fresh sample seed: `8227-r4-textbook-review-v2`; review is prepared, not performed.
Do not substitute an author re-read for independent vendor classification. Resolve
systematic disagreements and enlarge the sample as the completion method requires.

## Rebuild

```bash
python3 work/nam-8227-nsscas-2026/workbench/tools/run_repair_checks.py
python3 work/nam-8227-nsscas-2026/workbench/tools/verify_relocated_r4.py
python3 work/nam-8227-nsscas-2026/workbench/tools/freeze_analysis.py --check
```

The first command rebuilds twice and rejects seven fixtures for their expected
reason. The second uses an isolated independent workspace copy, with source hashes
checked and PDFs hardlinked only as immutable inputs. Dependencies are in
`tools/requirements-analysis.txt`. Passing checks are structural evidence, not
educational acceptance, app testing, import or production readiness.

Next: Claude's focused second-eye check of the completed repairs. Vitalis has not
selected a planning shortcut while textbooks continue; silence is not approval.
Full step 2 completion and acceptance remain separate from the marking checkpoint.
