#!/usr/bin/env python3
"""Break compound syllabus bullets into distinct assessable skills.

PLANNER.md: "Decompose a syllabus bullet that lists members into a container plus
one objective per member."

Up to 2026-10-17 this was a regex splitter. On this syllabus it could not tell a
list of things a learner must handle from a list that only qualifies one skill,
and it produced non-objectives ("explain deci", "state lakes", "identify on
drawings"). Which lists to split is a planning judgement, so it is now written
down as one: planning/decomposition.json, provenance `judgement`, each entry
naming its sub-topic, the opening words of its bullet and the member objectives.

This script only applies that table. It fails if an entry matches no bullet or
more than one, so a re-transcription that moves a bullet cannot silently drop
its decomposition.

  members     container + one objective per member (member wording is ours,
              built from the bullet's own words; the bullet stays verbatim)
  LEAD_IN     a bullet such as "define the terms:" whose members are the next
              N bullets; they are absorbed and given the lead-in's verb
"""
import json, collections, sys

WS = 'work/nam-6116-nssco-2026'
facts = json.load(open(f'{WS}/curriculum/syllabus-facts.json'))
table = json.load(open(f'{WS}/planning/decomposition.json'))

by_code = {r['code']: r for r in facts['content']}
for r in facts['content']:
    for o in r['specific_objectives']:
        o['decomposition'] = None
        o.pop('absorbed_by', None)

errors, applied = [], collections.Counter()
for e in table['entries']:
    row = by_code.get(e['sub_topic'])
    if not row:
        errors.append(f"{e['sub_topic']}: no such sub-topic")
        continue
    hits = [i for i, o in enumerate(row['specific_objectives'])
            if o['text'].startswith(e['starts_with'])]
    if len(hits) != 1:
        errors.append(f"{e['sub_topic']} '{e['starts_with']}': matched {len(hits)} bullets")
        continue
    i = hits[0]
    o = row['specific_objectives'][i]
    if e.get('kind') == 'LEAD_IN':
        n = e['absorbs_following']
        follow = row['specific_objectives'][i + 1:i + 1 + n]
        if len(follow) != n:
            errors.append(f"{e['sub_topic']} lead-in: only {len(follow)} bullets follow")
            continue
        o['decomposition'] = {'kind': 'LEAD_IN', 'provenance': 'judgement',
                              'members': [f"{e['prefix']} {f['text']}" for f in follow]}
        for f in follow:
            f['absorbed_by'] = o['text']
    else:
        o['decomposition'] = {'kind': 'MEMBERS', 'provenance': 'judgement',
                              'members': e['members']}
    applied[o['decomposition']['kind']] += 1

if errors:
    sys.exit('decomposition table does not match the transcription:\n  ' + '\n  '.join(errors))

bullets = [o for r in facts['content'] for o in r['specific_objectives']]
whole = [o for o in bullets if not o['decomposition'] and not o.get('absorbed_by')]
split = [o for o in bullets if o['decomposition']]
facts['decomposition_summary'] = {
    'rule': table['rule'],
    'source': 'planning/decomposition.json (provenance: judgement)',
    'bullets': len(bullets),
    'bullets_decomposed': len(split),
    'bullets_absorbed_into_a_lead_in': sum(1 for o in bullets if o.get('absorbed_by')),
    'bullets_left_whole': len(whole),
    'assessable_skills_after_decomposition':
        len(whole) + sum(len(o['decomposition']['members']) for o in split),
}
json.dump(facts, open(f'{WS}/curriculum/syllabus-facts.json', 'w'), indent=2, ensure_ascii=False)
s = facts['decomposition_summary']
print(f"bullets: {s['bullets']}  decomposed: {s['bullets_decomposed']} {dict(applied)}  "
      f"absorbed: {s['bullets_absorbed_into_a_lead_in']}  left whole: {s['bullets_left_whole']}")
print(f"assessable skills after decomposition: {s['assessable_skills_after_decomposition']}")
