#!/usr/bin/env python3
"""Write exemplar/README.md from the exemplar files themselves, so its counts cannot drift."""
import json, glob, os
WS = 'work/nam-6116-nssco-2026'
def load(t):
    units = [json.load(open(f)) for f in sorted(glob.glob(f'{WS}/exemplar/{t}/content-units/*.json'))]
    items = json.load(open(f'{WS}/exemplar/{t}/learning-items/topic_{t}_items.json'))['items']
    claims = json.load(open(f'{WS}/exemplar/{t}/claims/canonical_claim_ledger.json'))['claims']
    return units, items, claims
L = ['# 6116 Biology structural exemplar', '',
     'Generated content by `planning/make_exemplar.py`; this README by `planning/write_exemplar_readme.py`. Slot ids and '
     'labels are read from the live work orders, unit budgets from `curriculum/notes-budget.json`.', '']
for t, what in (('3', 'the whole of 3.3.2 Osmosis and 3.3.3 Active transport: the representative section'),
                ('4', 'part of 4.4.2 Monohybrid inheritance (two objectives)')):
    units, items, claims = load(t)
    kinds = sorted({i['subtype'] or i['item_type'] for i in items})
    L += ['- **%s: %s.** %d items (%s). %s. %d claims, %d of them citing an approved reference.' % (
        t, what, len(items), ', '.join(kinds),
        '; '.join('%s %d words (budget %d-%d)' % (u['title'], u['word_count'], u['word_budget']['min'], u['word_budget']['max'])
                  for u in units),
        len(claims), sum(1 for c in claims if c['evidence']))]
L += ['', 'What it models: a Key points block opening each unit; concise canonical answers; complete investigation plans '
      '(SYNTH, 5 marks); "discuss" cards written as developed points; a full genetic diagram (5 marks); evidence entries '
      'on claims; practical-procedure claims flagged for the teacher verifier.', '',
      '**Reuse.** Group 3A starts units 3.3.2 and 3.3.3 from this exemplar, which already is those units, and completes '
      'them against the work order. Topic 4 extends the 4.4.2 slice to the whole unit. Nowhere else reuse its scenarios. '
      'Copy its shape everywhere.', '',
      'Proof: both slices are installed in a scratch copy of the workspace, with each topic\'s registry branch cut to the '
      'slice objectives in the copy only. The notes are rendered, and `run_checks.py` and `planning/check_unit_budgets.py` '
      'are run. Both read PUBLISH; the only warning is C-18 (per-topic AO mix by item count, reported). C-39 passes; '
      'C-35, C-41 and C-43 do not apply (no generated depiction or practice text). The checks verify structure, scope and '
      'arithmetic, not scientific truth: the claims stay unverified until the teacher verification step.', '']
open(f'{WS}/exemplar/README.md', 'w').write('\n'.join(L))
print('README written')
