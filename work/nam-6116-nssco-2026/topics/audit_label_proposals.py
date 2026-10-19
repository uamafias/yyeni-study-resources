#!/usr/bin/env python3
"""Assemble the AO / Bloom / command-word label audit into review/AO-BLOOM-LABEL-AUDIT-2026-10-19.{json,md}.

INPUT : review/label-audit-inputs/out_<group>.json (reviewer proposals, saved unmodified) and the live items.
OUTPUT: an item-level table and recalculated AO mixes. NOTHING is applied: work orders, items and labels are unchanged.
        Applying any row needs an operator decision, an edit of the approved work order (and the AO audit that feeds it),
        and a re-run of the documented regeneration order.
Run from the repository root with .venv/bin/python.
"""
import glob, json
from collections import Counter
from fractions import Fraction
from pathlib import Path

W = Path(__file__).resolve().parents[1]
IN = W / 'review/label-audit-inputs'
items, slots = {}, {}
for t in range(1, 6):
    wo = json.loads((W / f'topics/{t}/work_order.json').read_text())
    for s in wo['item_slots'] + wo['performance_tasks']:
        slots[s['slot']] = s
    for f in glob.glob(str(W / f'topics/{t}/learning-items/*.json')):
        for i in json.loads(Path(f).read_text())['items']:
            items[i['item_id']] = i
props = []
for f in sorted(IN.glob('out_*.json')):
    for r in json.loads(f.read_text()):
        r['reviewer_file'] = f.name
        props.append(r)


def mix(overrides):
    """Same estimator as topics/audit_authoring.py; `overrides` maps item_id -> proposed AO list."""
    planned, uniform = Counter(), Counter()
    for iid, i in items.items():
        ao = overrides.get(iid, i['assessment_objectives']); m = i['mark_tariff']
        for a in ao:
            uniform[a] += Fraction(m, len(ao))
        if i['item_type'] == 'flashcard':
            for a in ao:
                planned[a] += Fraction(m, len(ao))
        elif i['item_type'] == 'practical_task':
            planned['AO3'] += m
        else:
            planned['AO1'] += Fraction(m * 5, 8); planned['AO2'] += Fraction(m * 3, 8)
    pct = lambda c: {k: round(float(v / sum(c.values()) * 100), 2) for k, v in sorted(c.items())}
    return {'estimator_percent': pct(planned), 'whole_item_label_percent': pct(uniform),
            'estimator_marks': {k: str(v) for k, v in sorted(planned.items())}}


def kind(p):
    c, n = p['current'], p['proposed']
    return [k for k, a, b in (('AO', c['AO'], n['AO']), ('Bloom', c['bloom'], n['bloom']),
                              ('command_word', c['command_word'], n['command_word'])) if a != b]


changes = [p for p in props if p['verdict'] == 'change']
keep = [p for p in props if p['verdict'] == 'boundary_keep']
ao_all = {p['item_id']: p['proposed']['AO'] for p in changes if 'AO' in kind(p)}
ao_clear = {k: v for k, v in ao_all.items() if not next(p for p in changes if p['item_id'] == k).get('touches_operator_decision')}
rows = []
for p in changes:
    s = slots.get(p['item_id'], {})
    k = kind(p)
    impact = []
    if 'AO' in k:
        impact.append("slot assessment_objectives and ao_demand (topics/%s/work_order.json), planning/ao_demand_audit.json record, exact AO rollup" % p['item_id'].split('-')[2])
    if 'Bloom' in k:
        impact.append('slot blooms_level (work order); no check reads Bloom, learner display only')
    if 'command_word' in k:
        impact.append('slot command_word and its tariff rule (C-15 / command-word register), prompt opener')
    rows.append({'item_id': p['item_id'], 'prompt_demand': p['prompt_demand'], 'changes': k, 'current': p['current'],
                 'proposed': p['proposed'], 'reason': p['reason'], 'uncertainty': p['uncertainty'],
                 'touches_operator_decision': bool(p.get('touches_operator_decision')),
                 'tariff': items[p['item_id']]['mark_tariff'], 'work_order_impact': impact,
                 'recommendation': 'operator decision first: touches a settled AO ruling or a documented boundary'
                 if p.get('touches_operator_decision') else 'review; low-risk if the Biology reviewer agrees'})
out = {'status': 'PROPOSALS ONLY. No label, work order, item or AO plan was changed.',
       'method': 'Eight independent read-only passes (one per author script; topic 3 split by group) read every item against its prompt, answer, guidance and planned AO demand, applying the operator-settled AO rules in planning/ao_operator_review.json. Reviewers proposed a change only when confident and listed boundary cases they kept. This is one reviewer per item, not a teacher panel.',
       'items_reviewed': len(items), 'proposals': len(changes), 'boundary_cases_kept': len(keep),
       'proposal_kinds': dict(Counter(tuple(r['changes']) and '+'.join(r['changes']) for r in rows)),
       'recalculated_ao_mix': {
           'current': mix({}),
           'if_all_AO_proposals_applied': mix(ao_all),
           'if_only_AO_proposals_not_touching_operator_decisions': mix(ao_clear)},
       'ao_items_proposed': {k: {'all': ao_all[k], 'excluded_in_second_scenario': k not in ao_clear} for k in ao_all},
       'patterns_for_a_rule_decision': [
           'Written recall of a practical procedure is labelled inconsistently: microscope sequence AO3 (3-003, 3-004) versus food-test procedures AO1 (3-189 to 3-193) and Topic 1 apparatus/safety/technique recall labelled AO3 (1-015, 1-028, 1-082, 1-084, 1-086, 1-088, 1-094). One rule should cover them (recall of a method is A; applying it to results or planning is C).',
           'Conclusions from a controlled investigation are labelled both AO2 (3-233, 3-237) and AO3 (3-242, 3-261, 3-309, 3-378, 3-393, 3-454).',
           'Drawing from a photograph or photomicrograph: 3-355 is AO3 while 3-068 and 3-386 are AO1; decide together (3-386 is proposed AO3).',
           'Several APP cards (e.g. 3-026, 3-089, 3-094, 3-103, 3-431, 3-440, 3-382, 4-045..4-051, 5-052/054/058) re-run a taught account in a new setting: only just AO2.',
           'Fifteen Topic 1 INTERP cards carry Bloom Analyse because that is the subtype default, though each is a one-step routine task.',
           '"Describe why" opens eleven prompts whose task is to give reasons (command word explain).'],
       'rows': rows,
       'boundary_cases_kept': [{k: p[k] for k in ('item_id', 'prompt_demand', 'current', 'reason', 'uncertainty', 'touches_operator_decision')} for p in keep]}
(W / 'review/AO-BLOOM-LABEL-AUDIT-2026-10-19.json').write_text(json.dumps(out, indent=1, ensure_ascii=False) + '\n')

m = out['recalculated_ao_mix']
L = ['# AO, Bloom and command-word label audit (proposals only)', '',
     'Date: 2026-10-19. Status: **proposals only; nothing was changed.** Approved work orders, item labels and the AO plan are untouched.', '',
     out['method'], '',
     '## Result', '',
     '- Items read: %d. Proposed changes: %d (%s). Boundary cases kept as labelled: %d.' % (out['items_reviewed'], len(changes), ', '.join('%s %d' % kv for kv in out['proposal_kinds'].items()), len(keep)),
     '- Only %d proposals change an AO label; the rest are Bloom or command-word proposals.' % len(ao_all), '',
     '| Basis | A / AO1 | B / AO2 | C / AO3 |', '|---|---:|---:|---:|']
for name, key in (('Current approved estimator', 'current'), ('All AO proposals applied', 'if_all_AO_proposals_applied'),
                  ('AO proposals not touching an operator ruling', 'if_only_AO_proposals_not_touching_operator_decisions')):
    e = m[key]['estimator_percent']; L.append('| %s (estimator) | %s | %s | %s |' % (name, e['AO1'], e['AO2'], e['AO3']))
for name, key in (('Current', 'current'), ('All AO proposals applied', 'if_all_AO_proposals_applied')):
    e = m[key]['whole_item_label_percent']; L.append('| %s (whole-item label split) | %s | %s | %s |' % (name, e['AO1'], e['AO2'], e['AO3']))
L += ['', 'The stated target is 47 / 28 / 25. These figures are diagnostics: the proposals move the bank further from the paper weighting because a number of AO2 cards are only just B. There is no quota, and no card is to be relabelled or added to move a percentage.', '',
      '## Patterns that need one rule rather than item-by-item edits', ''] + ['- ' + x for x in out['patterns_for_a_rule_decision']] + ['',
      '## Item-level proposals', '',
      '| Item | Change | Current | Proposed | Prompt demand | Reason | Uncertainty | Operator ruling touched |', '|---|---|---|---|---|---|---|---|']
for r in rows:
    c, n = r['current'], r['proposed']
    L.append('| %s | %s | %s / %s / %s | %s / %s / %s | %s | %s | %s | %s |' % (r['item_id'].replace('ITEM-6116-', ''), '+'.join(r['changes']), '+'.join(c['AO']), c['bloom'], c['command_word'],
             '+'.join(n['AO']), n['bloom'], n['command_word'], r['prompt_demand'].replace('|', '/'), r['reason'].replace('|', '/'), r['uncertainty'].replace('|', '/'), 'yes' if r['touches_operator_decision'] else 'no'))
L += ['', '## Work-order impact if adopted', '',
      '- AO: edit the slot `assessment_objectives` and `ao_demand` in `topics/<T>/work_order.json` through the approved route (`planning/ao_demand_audit.json`, then `apply_ao_demand_audit.py`), recompute the exact rollup and re-run `audit_authoring.py`.',
      '- Bloom: edit slot `blooms_level`; no deterministic check reads it.',
      '- Command word: edit the slot `command_word`; the prompt opener and the tariff rule for that word must still agree (C-15).',
      '- After any approved change run the documented regeneration order and every check; then restamp the affected items.', '',
      '## Boundary cases kept (%d)' % len(keep), '', '| Item | Current | Why it stays | Uncertainty |', '|---|---|---|---|']
for p in keep:
    c = p['current']
    L.append('| %s | %s / %s / %s | %s | %s |' % (p['item_id'].replace('ITEM-6116-', ''), '+'.join(c['AO']), c['bloom'], c['command_word'], p['reason'].replace('|', '/'), p['uncertainty'].replace('|', '/')))
(W / 'review/AO-BLOOM-LABEL-AUDIT-2026-10-19.md').write_text('\n'.join(L) + '\n')
print('proposals', len(changes), '| AO proposals', len(ao_all), '| kept', len(keep))
print(json.dumps(m['current']['estimator_percent']), json.dumps(m['if_all_AO_proposals_applied']['estimator_percent']), json.dumps(m['if_only_AO_proposals_not_touching_operator_decisions']['estimator_percent']))
