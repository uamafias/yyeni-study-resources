# E1 visual repairs — NSSCAS Mathematics 8227

24 November 2026. Codex AUTHOR. Stable approved Stage-D rubric0.1.4; native resource
version is managed by the shared provider. This is same-vendor author verification,
not cross-vendor acceptance or actual app/marker/website acceptance.

| Finding | Before → after | Actual affected rows | Proof |
|---|---|---:|---|
| SE-02 | Explicit unit multipliers in modulus formula, trapezium b prompt/criterion/step and vector solution → shared `formatting.coefficient` suppresses ±1 and preserves exact values | 16modulus,8trapezium,20vector | `e1-visual-check.json`; regex checks on actual fields and all96 mathematical oracle rows |
| SE-04 | Learner b/d answers contained follow-through/own-graph marking rules → canonical answer only; unchanged criteria retain the marking behavior | 22 | `visual.py:239,256`; every generated b/d reference answer inspected by the regression check |
| SE-05 | Fixed point-label offsets intersected continuing blue arms → all labels placed in clear conservative glyph rectangles with short leaders | 44SVGs redrawn; baseline collision indices recorded | Independent orientation-based emitted-SVG check passes all44; actual old idx4/19 are detected as negative fixtures; fresh contact sheets/full-size renders inspected |
| SE-07 | d:DB1 omitted permitted unambiguous concavity shorthand → exact allowance restored in achievement, retaining the unchanged dependent mark and own-curve rule | 22 | `visual.py:261`; declared correct-sketch/concave-down fixture remains2/2 under WO:79 |

Root owns the corresponding catalogue reviewed-row patch for SE-07 and the plural
asset binding support. `log-solution` now declares `part_ids=['c','d']`. All stable
criterion IDs, mark types, tariffs, dependencies, FT objects, parameter domains,
answer values and scores are unchanged. The script compares every criterion object
against the preserved Stage-E baseline, allowing only achievement wording to differ.

Cheap notes folded in: second-integrand help no longer supplies "square"; decimal
working shows nine useful guard digits instead of an unwieldy truncated tail;
width factors are simplified and a sole interior ordinate is written directly;
solution top chords are green dashed lines to distinguish them from the curve.
Domain/mathematical capacity and more-precise vector-answer policy are unchanged.

Commands from the repository root:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 work/nam-8227-nsscas-2026/workbench/authoring/visual-check.py
PYTHONDONTWRITEBYTECODE=1 python3 work/nam-8227-nsscas-2026/workbench/authoring/e1-visual-check.py
node work/nam-8227-nsscas-2026/workbench/authoring/e1-visual-render.mjs /Users/professor/conductor/workspaces/yyeni/chiang-mai/apps/web
```

The all-domain oracle passes96instances and six negative domain/original-subtask
fixtures, recovering graph coefficients, adding individual high-precision trapezia,
comparing independent quadrature and using cosine-law vector angles. E1 geometry
checks separately parse the emitted SVG/text and use an intersection algorithm
different from placement. All44modulus labels avoid every arm. All67 native visual
SVGs were freshly rendered, all44modulus instances inspected through four contact
sheets, with former worst cases4/19, merged-origin24 and trapezium0/3/19 inspected
full-size. See `e1-visual-renders.json` for exact PNG hashes and limitations.

No source PDF, review, history, planning, core/provider, other group, app, standard,
other subject or pinned checkout edited. No commit or push. Source is stable for
root's shared package/replay/notation checks and final immutable candidate build.
