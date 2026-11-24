# Claude diff-only E1 check — NSSCAS Mathematics 8227

Role REVIEWER. Workspace `work/nam-8227-nsscas-2026/`, owner Vitalis, NIED December
2020 syllabus. Read AGENTS, TEAM-PLAYBOOK, exactly REVIEWER and the Workbench
playbook/quality. This is the requested **Stage-E → E1 diff-only check**; do not
restart accepted source analysis, syllabus mapping or planning.

Start with `review/opus-stage-e/report.md`, `findings.md`, `REPAIR-E1-PROMPT.md`,
then `checks/stage-e-repair-e1-report.md`, current STATUS/HANDOVER and the current
`authoring/stage-e-manifest.json`. Check the exact manifest hash against
`checks/stage-e-repair-e1-freeze.json` and run:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 work/nam-8227-nsscas-2026/workbench/authoring/freeze_stage_e.py --check
PYTHONDONTWRITEBYTECODE=1 python3 work/nam-8227-nsscas-2026/workbench/authoring/check_e1_preservation.py
```

The E0 manifest is preserved unchanged at `authoring/history/stage-e-0/manifest.json`,
SHA256 `22cd1799146ce1d07c25c837f7078b6bb0f717d0e5b9985d57f4371f2ec87025`.
Its 1,017 files are under the sibling `files/<repository-relative-path>`. The old
candidate `candidates/fcd4b71e07baa07a/`, SHA256
`7022ea5049b0f5b02452828d5226f0a533816873f20d551186925e8aacacb250`,
is untouched. Compare those bytes with the current source/candidate; keep all
old review evidence unchanged.

The output-affecting repair uses native/package 0.1.5 / provider-v1 transport 2.
The approved design/rubric identity and literal criterion IDs remain 0.1.4;
`design_rubric_version` explicitly records that basis. The new provider rejects
old transport 1; its old immutable candidate remains replayable. Native selection,
part and semantic exposure identities do not reset or change. No attempts exist.

Check only the named repairs and their propagated outputs:

1. **SE-01/02:** actual raised derivative primes, unit coefficient/sign formatting,
   shared formatter and negative fixtures. Inspect actual rendered expressions,
   not only strict KaTeX success. Calculator/math values remain unchanged.
2. **SE-03/04:** the actual instance coefficient in no-real principal solutions;
   canonical trapezium answers free of marker instructions, with those rules
   preserved in the private criteria/memo.
3. **SE-05/06:** all 44 modulus and 270 log graph geometry tests, original bad-layout
   negatives, actual rerenders. Inspect modulus 4/19, log 45–62/132 and their contacts.
   Check label-to-own-dot association and the origin0 rectangle.
4. **SE-07/08:** concavity shorthand restored in both runtime DB1 and the reviewed
   catalogue row; increasing alone insufficient. Gradient-only alternatives use
   G1–G5 with no target/S3/S4/back-substitution obligation and its own five-mark cap.
5. **SE-09/10:** the two alternative scripts now show required working without new
   scores. Check the 19 additional rounding declarations independently, including
   exponential flips, distance 233/2→117 and displacement ∓265/2. Exact answers remain
   accepted. The original 97 expectation IDs/scores remain unchanged.
6. **SE-11:** required-vs-emitted key split. Gradient 0 exposes its shared proof;
   a subsequent fresh normal test cannot return old normal 3/same proof. Do not
   tighten the reverse direction: gradient 23 and normal 8 are the approved bounds.
7. **SE-12/13:** all three learner mode/reveal payloads use neutral mixed-motion
   public IDs and preserve a verified native mapping; native/teacher/marking IDs
   stay unchanged. Teacher references omit held/related refs and internal paths,
   source hashes and reviewer annotations. Check the held 2023 P1 Q9 regression.

Read the three `authoring/e1-*-report.md` / `e1-visual-handover.md` records and
`checks/stage-e/e1-runtime.json`, `e1-preservation.json`. Prime screenshots and SVG
render evidence are in `authoring/e1-calculus-primes-*.png`, `e1-trig-gallery/` and
`visual/e1/`. These are static resource renders, not actual website acceptance.

The invariant comparison covers all 1,702 rows and every ordered criterion/mark/
dependency/FT/accuracy/answer-only flag, mathematical data, domain, bound and
owner score. Supplement it independently. The original 51 calculus records have
29 concrete scripts and 22 declarative records, a corrected count classification;
19 rounding records are additional declarations. None is a raw-response recogniser.
Pending rubric cases in your prior findings remain notes with no new score.

Repeat `authoring/rebuild_stage_e.py --app-root /path/to/yyeni` in an independent
copy as useful. It supplies the necessary minimal inputs for canonical plus two
relocated builds and compares 385 source files/eight reports/candidate digest
without normalisation. Group oracles and focused scripts were rerun separately.
Check that only the named source/authoring/generated/check/status/version-handoff
outputs changed and that no review, PDF, analysis/curriculum/design, standard,
other subject, app/pinned checkout or registry was edited.

Write a new `review/opus-stage-e1-check/` with exact inputs, diff findings and
rebuild/render receipts. State whether the named E1 changes are confirmed and
whether the resource scope can proceed to local website/app testing. Do not claim
actual app rendering, marking/photo recognition, access/history, MCP, production
or release acceptance: none was run or authorised. Only real should-fix or
design-blocking findings trigger another repair round; carry notes forward.

No commit/push, app edits, installation, import, assignment or publication.
