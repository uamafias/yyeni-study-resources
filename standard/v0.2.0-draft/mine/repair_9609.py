# -*- coding: utf-8 -*-
"""Apply one batch of the 9609 command-word repair.

    python3 repair_9609.py <batch.json>

A batch is {"rewrites": [...], "unchanged": [...]}. Each rewrite names an item and gives its new prompt,
canonical answer, marking guidance, command word and tariff. The applier keeps the objective, the claims
and claims_seen, records the old text's hash as prior_hash, recomputes authored_hash, writes a repair_note,
and appends {from, to, why} to the topic's authoring_notes.json. assessment_objectives follow the
subject's subtype map (a flashcard may only carry AOs its subtype permits; the mark-level AO split lives in
the marking guidance), so a rewrite that asks for an AO its subtype does not carry is refused.
"""
import datetime, hashlib, json, os, re, sys
HOME = os.path.expanduser('~')
REPO = os.path.join(HOME, 'mnt', 'YYeni Study Resources')
WS = os.path.join(REPO, 'work', 'cie-9609-as-2026-2028')
sys.path.insert(0, os.path.join(REPO, 'standard', 'v0.2.0-draft', 'checks'))
from yyeni_checks import _artefact_text  # noqa: E402
TODAY = datetime.date.today().isoformat()
SIX = ('Identify', 'Define', 'Explain', 'Calculate', 'Analyse', 'Evaluate')
FW = json.load(open(os.path.join(WS, 'curriculum', 'assessment-framework.json')))
AO_MAP = {m['subtype']: m['assessment_objectives'] for m in FW['flashcard_subtype_ao_map']}
BLOOM = FW['blooms_taxonomy']['by_subtype'] if 'blooms_taxonomy' in FW else {}


def load(tid):
    p = os.path.join(WS, 'topics', tid, 'learning-items', 'topic_%s_items.json' % tid)
    return p, json.load(open(p))


def main(batch_path):
    batch = json.load(open(batch_path))
    files, notes, done = {}, {}, []
    for r in batch.get('rewrites', []):
        tid = r['item_id'].split('-')[2]
        if tid not in files:
            files[tid] = load(tid)
            np_ = os.path.join(WS, 'topics', tid, 'authoring_notes.json')
            notes[tid] = (np_, json.load(open(np_)) if os.path.exists(np_) else [])
        items = files[tid][1]['items']
        it = next(i for i in items if i['item_id'] == r['item_id'])
        old_prompt, old_hash = it['prompt'], it.get('authored_hash')
        if r.get('prompt_replace'):
            old, new = r['prompt_replace']
            if old not in it['prompt']:
                raise SystemExit('%s: prompt_replace text not found' % r['item_id'])
            r['prompt'] = it['prompt'].replace(old, new, 1)
        if not any(re.search(r'\b%s\b' % w, r['prompt'], re.I) for w in SIX):
            raise SystemExit('%s: new prompt instructs with none of %s' % (r['item_id'], ', '.join(SIX)))
        it['prompt'] = r['prompt']
        if r.get('canonical_answer') is not None:
            it['canonical_answer'] = r['canonical_answer']
        if r.get('marking_guidance') is not None:
            it['marking_guidance'] = r['marking_guidance']
        if r.get('subtype'):
            it['subtype'] = r['subtype']
        if r.get('claim_ids'):
            # a rewrite that no longer rests on its old claim cites the one it does rest on, at its current revision
            led = json.load(open(os.path.join(WS, 'topics', tid, 'claims', 'canonical_claim_ledger.json')))
            rev = {c['claim_id']: c.get('revision', 1) for c in led['claims']}
            missing = [c for c in r['claim_ids'] if c not in rev]
            if missing:
                raise SystemExit('%s: claims %s are not in the topic ledger' % (r['item_id'], missing))
            it['claim_ids'] = r['claim_ids']
            it['claims_seen'] = {c: rev[c] for c in r['claim_ids']}
        aos = r.get('assessment_objectives') or it['assessment_objectives']
        if it['item_type'] == 'flashcard' and not set(aos) <= set(AO_MAP[it['subtype']]):
            raise SystemExit('%s: %s not permitted for %s (%s)' % (r['item_id'], aos, it['subtype'], AO_MAP[it['subtype']]))
        it['assessment_objectives'] = aos
        it['command_word'] = r['command_word']
        it['mark_tariff'] = r['mark_tariff']
        if r.get('blooms_level') and r['blooms_level'] != it.get('blooms_level'):
            it['blooms_level'] = r['blooms_level']
            it['blooms_level_basis'] = 'set at the command-word repair (%s): %s' % (TODAY, r.get('bloom_why', ''))
        elif it.get('blooms_level_basis'):
            it['blooms_level_basis'] = it['blooms_level_basis'].replace('the authored text is unchanged',
                                                                          'unchanged by the command-word repair')
        if old_hash:
            it['prior_hash'] = old_hash
        it['repair_note'] = ('Command-word repair %s: %s' % (TODAY, r['why']))
        it['authored_hash'] = hashlib.sha256(_artefact_text(it).encode()).hexdigest()
        notes[tid][1].append({'item_id': r['item_id'], 'change': 'command-word repair', 'date': TODAY,
                              'from': old_prompt, 'to': r['prompt'], 'why': r['why']})
        done.append(r['item_id'])
    for tid, (p, d) in files.items():
        json.dump(d, open(p, 'w'), indent=1, ensure_ascii=False)
        np_, nl = notes[tid]
        json.dump(nl, open(np_, 'w'), indent=1, ensure_ascii=False)
    rep = os.path.join(WS, 'curriculum', 'command-word-repair-log.json')
    log = json.load(open(rep)) if os.path.exists(rep) else {'rewritten': [], 'left_unchanged': []}
    log['rewritten'] = sorted(set(log['rewritten']) | set(done))
    known = {u['item_id'] for u in log['left_unchanged']}
    log['left_unchanged'] += [u for u in batch.get('unchanged', []) if u['item_id'] not in known]
    json.dump(log, open(rep, 'w'), indent=1, ensure_ascii=False)
    print('rewrote %d items in topics %s; %d recorded as unchanged' % (len(done), ', '.join(sorted(files)), len(batch.get('unchanged', []))))


if __name__ == '__main__':
    main(sys.argv[1])
