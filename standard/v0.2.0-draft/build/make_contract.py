# -*- coding: utf-8 -*-
"""Generate a topic contract for every topic in a subject, from the curriculum.

A contract is the author's brief: what is in scope, what is out, which command
words and tariffs are live, how deep to go, and how much to write. Everything in
it is derived - from the objective registry, the measured assessment framework,
the measured exposure map and the subject profile - so a new syllabus needs a
curriculum folder and nothing else.

Usage:  python3 make_contract.py <workspace> [--force]
"""
import json, os, re, sys, datetime, collections

NOW = datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')


def _json(p):
    with open(p, encoding='utf-8') as fh:
        return json.load(fh)


def _yaml(p):
    try:
        import yaml
    except ImportError:
        return {}
    with open(p, encoding='utf-8') as fh:
        return yaml.safe_load(fh) or {}


# Words per assessable objective, by how heavily the objective is examined.
# Full teaching depth throughout; exposure decides how much worked example and
# how many variants, not whether the objective is taught. RS-05.
WORDS_BY_EXPOSURE = {'core': (330, 470), 'frequent': (300, 430),
                     'occasional': (270, 390), 'rare': (250, 360),
                     'unseen': (230, 330)}
ITEMS_BY_EXPOSURE = {'core': 6, 'frequent': 5, 'occasional': 5, 'rare': 4, 'unseen': 4}


def stop_words():
    return set('''the a an and or of to in for on with by from as is are was were be
    been that this these those it its their they them not no but which who what when
    where why how some many most other more less than then so such e.g eg i.e ie
    definition definitions example examples including include includes appropriate
    relevant different various main basic simple types type nature role roles use
    used using between within terms term concept concepts understanding knowledge'''.split())


def sub_topic(oid):
    """OBJ-0450-2.1.3-01 -> '2.1.3';  OBJ-0455-2.3.1 -> '2.3.1'.

    The sub-topic decides the content-unit split, so it has to survive both
    id shapes: a registry with a trailing -NN item suffix and one without.
    """
    core = oid.split('-')[2] if oid.count('-') >= 2 else oid
    core = core.split('-')[0]
    parts = core.split('.')
    return '.'.join(parts[:3])


def topic_phrases(objs):
    """Each topic's own title, as a phrase, with the distinctive words it turns on.

    Scope guards are stated as TOPICS, never as bare words. Telling an author not
    to teach 'price' in the Demand topic would be wrong and harmful; telling them
    that Price determination is topic 2.5 is exactly right.
    """
    sw = stop_words()
    out = {}
    for o in objs:
        if o.get('parent_id'):
            continue
        title = re.sub(r'^\d+(\.\d+)*\s+', '', o['syllabus_text'])
        key = [w for w in re.findall(r"[a-z][a-z'-]{3,}", title.lower()) if w not in sw]
        if key:
            out[o['topic_id']] = (title, set(key))
    return out


def neighbours(tid, objs, phrases, limit=8):
    """Topics whose own subject matter this topic's wording reaches into."""
    mine = ' '.join((o['syllabus_text'] + ' ' + o.get('syllabus_guidance', '')).lower()
                    for o in objs if o.get('parent_id') and o['topic_id'] == tid)
    unit = tid.split('.')[0]
    out, seen = [], set()
    for other, (title, key) in sorted(phrases.items(),
                                      key=lambda kv: [int(x) for x in kv[0].split('.')]):
        if other == tid:
            continue
        # the whole title phrase, or every distinctive word of a short title
        hit = title.lower() in mine or (len(key) <= 2 and all(k in mine for k in key))
        if hit and other not in seen:
            seen.add(other)
            out.append('%s \u2014 taught in topic %s%s'
                       % (title, other, ' (same unit)' if other.split('.')[0] == unit else ''))
        if len(out) >= limit:
            break
    return out


def build(ws, force=False):
    cur = os.path.join(ws, 'curriculum')
    reg = _json(os.path.join(cur, 'objective_registry.json'))
    objs = reg['objectives']
    fw = _json(os.path.join(cur, 'assessment-framework.json'))
    exp = {o['objective_id']: o for o in
           _json(os.path.join(cur, 'exam-exposure.json'))['objectives']}
    units = {}
    up = os.path.join(cur, 'unit_titles.json')
    if os.path.exists(up):
        units = _json(up)
    # Cambridge states its own scope limits inside the subject content. These beat
    # any heuristic about which topic owns which word, so they go first and are
    # labelled with their authority.
    stated = {}
    sp = os.path.join(cur, 'syllabus-exclusions.json')
    if os.path.exists(sp):
        stated = _json(sp)
    # C-11 scans for terms, so each stated limit needs its scannable form (curriculum/scope-scan.json,
    # written by mine/scope_scan.py). Without one the limit would be recorded and never enforced.
    scan = []
    cp = os.path.join(cur, 'scope-scan.json')
    if os.path.exists(cp):
        scan = [{'construct': e['construct'], 'pattern': e['pattern'], 'source': e['source']}
                for e in _json(cp)['entries']]
    elif any(stated.values()):
        raise SystemExit('The syllabus states content limits (syllabus-exclusions.json) but there is no '
                         'curriculum/scope-scan.json to enforce them. Run mine/scope_scan.py first.')
    profile = {}
    for cand in ('qualification-profile.yaml', 'subject-profile.yaml'):
        p = os.path.join(ws, cand)
        if os.path.exists(p):
            profile.update(_yaml(p))

    subject = re.search(r'-(\d{4})-', os.path.basename(ws.rstrip('/'))).group(1)
    qual = os.path.basename(ws.rstrip('/'))

    in_use = [c['word'] for c in fw['command_words'] if c.get('observed_count', 0) > 0]
    never = fw.get('command_words_listed_but_never_used', [])
    tariffs = {c['word']: c.get('modal_tariff') for c in fw['command_words']
               if c.get('observed_count', 0) > 0}
    all_tariffs = {c['word']: c.get('observed_tariffs') for c in fw['command_words']
                   if c.get('observed_count', 0) > 0}
    ao_targets = fw['ao_mark_budget']['stated_qualification_weight_percent']

    titles = {}
    for o in objs:
        if not o.get('parent_id'):
            titles[o['topic_id']] = re.sub(r'^\d+(\.\d+)*\s+', '', o['syllabus_text'])
    phrases = topic_phrases(objs)

    written, skipped = [], []
    for tid in sorted(titles, key=lambda x: [int(y) for y in x.split('.')]):
        kids = [o for o in objs if o.get('parent_id') and o['topic_id'] == tid]
        if not kids:
            continue
        td = os.path.join(ws, 'topics', tid)
        path = os.path.join(td, 'contract.json')
        if os.path.exists(path) and not force:
            skipped.append(tid)
            continue
        cls = [exp.get(o['objective_id'], {}).get('exposure_class', 'unseen') for o in kids]
        lo = sum(WORDS_BY_EXPOSURE[c][0] for c in cls)
        hi = sum(WORDS_BY_EXPOSURE[c][1] for c in cls)
        items = sum(ITEMS_BY_EXPOSURE[c] for c in cls)
        seen = [o for o in kids
                if exp.get(o['objective_id'], {}).get('times_examined', 0) > 0]
        marks = sum(exp.get(o['objective_id'], {}).get('marks_examined', 0) for o in kids)
        cw_here = collections.Counter()
        for o in kids:
            for w, n in (exp.get(o['objective_id'], {}).get('command_words') or {}).items():
                cw_here[w] += n
        contract = {
            'contract_id': 'CONTRACT-%s-%s' % (subject, tid),
            'topic_id': tid,
            'topic_title': titles[tid],
            'unit': units.get(tid.split('.')[0]),
            'qualification': qual,
            'standard_version': '0.2.0-draft',
            'generated_at': NOW,
            'generated_by': 'make_contract.py',
            'status': 'active',
            'scope': {
                'included_objective_ids': [o['objective_id'] for o in kids],
                'included_count': len(kids),
                'objective_types': dict(collections.Counter(o['objective_type'] for o in kids)),
                'depth_tiers': dict(collections.Counter(o['depth_tier'] for o in kids))},
            'target_learner_profile': {
                'prior_teaching': profile.get('prior_teaching')
                                  or 'None assumed beyond the syllabus’s own prerequisites.',
                'context': 'Namibian secondary learners, %s, English medium.'
                           % profile.get('qualification', 'Cambridge IGCSE'),
                'note_purpose': ['source of record for flashcard generation',
                                 'offline reading', 'standalone study text']},
            'assessment_expectations': {
                'papers': ['P%s' % p['paper'] for p in fw.get('papers', [])],
                'command_words_in_scope': in_use,
                'command_words_never_used_in_the_corpus': never,
                'modal_tariffs': tariffs,
                'observed_tariffs': all_tariffs,
                'command_words_seen_on_this_topic': dict(cw_here.most_common()),
                'ao_targets': ao_targets,
                'answer_shapes': 'curriculum/answer-shapes.json',
                'note': 'The command words in scope are the ones the papers actually use, '
                        'measured across the held corpus, not the ones the syllabus table '
                        'lists. Never write a prompt with a word under '
                        'command_words_never_used_in_the_corpus.'},
            'exposure': {
                'objectives_examined': len(seen),
                'objectives_never_seen': len(kids) - len(seen),
                'marks_examined_in_corpus': marks,
                'classes': dict(collections.Counter(cls)),
                'principle': 'RS-05: exposure calibrates emphasis. Every objective in scope '
                             'is taught and practised whether or not it has been examined.'},
            'depth_constraints': {
                'note_mode': 'full teaching depth',
                'word_budget': {'min': lo, 'max': hi},
                'item_budget': items,
                'excluded_constructs': scan,
                'excluded_constructs_stated_by_syllabus': stated.get(tid, []),
                'adjacent_topics': neighbours(tid, objs, phrases),
                'excluded_constructs_source':
                    'excluded_constructs are the limits the syllabus states anywhere in the subject, each '
                    'as the pattern C-11 scans learner-facing text for (curriculum/scope-scan.json): the '
                    'sentence is Cambridge\u2019s, the pattern is our judgement of what teaching past it '
                    'looks like, and any match fails the topic. adjacent_topics are not scanned: they '
                    'name subject matter a neighbouring topic owns. Naming one in passing is fine and '
                    'often necessary; teaching it here is scope creep.'},
            'required_outputs': {
                'claim_ledger': True,
                'content_units': len({sub_topic(o['objective_id']) for o in kids}),
                'learning_items': items,
                'notes': True},
            'misconceptions': 'curriculum/misconceptions.json (filter on topic_id "%s")' % tid,
            'subtype_waivers': []}
        os.makedirs(td, exist_ok=True)
        with open(path, 'w', encoding='utf-8') as fh:
            json.dump(contract, fh, indent=1, ensure_ascii=False)
        written.append(tid)
    return written, skipped


sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gates import require_prerequisites  # noqa: E402


def main():
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    if not args:
        print(__doc__)
        return 2
    require_prerequisites(args[0])
    w, s = build(args[0], force='--force' in sys.argv)
    print('contracts written %d, skipped (already present) %d' % (len(w), len(s)))
    if s:
        print('  re-run with --force to regenerate: %s' % ' '.join(s[:12]))
    return 0


if __name__ == '__main__':
    sys.exit(main())
