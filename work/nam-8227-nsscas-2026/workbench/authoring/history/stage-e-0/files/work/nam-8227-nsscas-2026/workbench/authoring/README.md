# Stage-E authoring and resume — NSSCAS Mathematics 8227

24 November 2026. Owner Vitalis. Role AUTHOR. NIED December 2020 syllabus, Grade 12.

Vitalis approved the exact Stage-D manifest `4a0548320dcb9209dcd28e18bd4f6c77423480de6538fcbf1b0f8b6d0e17d8ec`
and content digest `e9cd8f58345364e7b3bb45fadf2bab162571cc4c101df5beff2189a514fd8780`,
including MR03-OPS-D4 operations. See `../planning/OWNER-CHECKPOINT.md`.
The original approved bytes remain recoverable through the approval receipt.
No commit, push, import, installation, learner assignment or activation is authorised.

Three parallel same-vendor authors implemented the calculus, trig/log and visual
groups; the lead integrated the provider, projections, package and shared checks.
These are author checks, never independent acceptance.

## Implemented paths

- `../source/groups/`: pure deterministic recipe constructors; all finite domains
  and invalid-case checks live with the appropriate group.
- `../source/provider.py`: seeded selection, frozen memo, qualified identities,
  safe native projections, freshness/exhaustion and sealed asset lookup.
- `../source/catalogue-native.json`: rich educational contract; `recipes.json` is
  the existing provider-v1 descriptor bridge. Its revision 1 means native 0.1.4.
- `../source/assets/` and `asset-index.json`: original SVGs derived from instance
  parameters; part/role/instance/reveal bindings remain explicit.
- `../source/examples/`: 42 frozen seeded runtime examples, separate from the
  42 Stage-D worked paper cases.
- `../source/deck-compositions.json`: unassigned 19/20/17-mark compositions.
- `../candidates/`: immutable candidate checkpoints from the existing
  `yyeni_workbench_tools` builder. Use the exact current pointer in
  `../checks/stage-e/candidate.json`; earlier checkpoints are not active releases.

## Rebuild and check

Run from the repository root. Set `PYTHONDONTWRITEBYTECODE=1` to avoid cache noise.
All resource runtime dependencies are Python standard library. Authoring oracles
use the already installed SymPy/mpmath; syntax/render checks use the existing
application's KaTeX/sharp installation, read-only. Nothing is installed by these commands.

```bash
PYTHONDONTWRITEBYTECODE=1 python3 work/nam-8227-nsscas-2026/workbench/authoring/approval_snapshot.py
PYTHONDONTWRITEBYTECODE=1 python3 work/nam-8227-nsscas-2026/workbench/authoring/calculus-check.py
PYTHONDONTWRITEBYTECODE=1 python3 work/nam-8227-nsscas-2026/workbench/authoring/trig-log-check.py --check
PYTHONDONTWRITEBYTECODE=1 python3 work/nam-8227-nsscas-2026/workbench/authoring/visual-check.py
PYTHONDONTWRITEBYTECODE=1 python3 work/nam-8227-nsscas-2026/workbench/authoring/rebuild_stage_e.py --app-root /Users/professor/conductor/workspaces/yyeni/chiang-mai
PYTHONDONTWRITEBYTECODE=1 python3 work/nam-8227-nsscas-2026/workbench/authoring/check_ids.py
```

`rebuild_stage_e.py` runs the canonical source build, exhaustive integration,
notation and existing provider-v1 checks, then repeats in two relocated minimal
input copies. Source bytes, four reports and candidate manifest must match
without path normalisation. It never registers/activates a candidate. The old
Stage-D live-path freeze is historical after approved statuses change; use
`approval_snapshot.py` to verify all approved bytes through preserved originals.

After any substantive source change, rerun the relevant independent oracle,
shared checks and rebuild before freezing a new candidate. Do not rewrite old
candidates or reinterpret old attempts. Native solution assets/rubrics require the
explicit app conversion in `../app-change-handoff.md`; the v1 transport pass does
not prove that integration.

Read `NOTE-CARRY.md`, `CALCULUS-HANDOVER.md`, `trig-log-handover.md`,
`visual/README.md` and `../checks/author-report.md` before resuming. Only
should-fix or design-blocking findings trigger a repair round. Notes remain
visible and do not silently change approved scores or parameter domains.
