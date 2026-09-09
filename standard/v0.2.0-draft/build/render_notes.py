#!/usr/bin/env python3
"""
Render a topic's offline learner notes from its approved content units.

RS-16: published outputs are derived from the same approved structured source.
RS-39: rendering rather than hand-writing the notes makes notes-to-card drift
structurally impossible - the notes ARE the content units.

    python3 render_notes.py <workspace> <topic-id> [--out notes-<slug>.md]
"""
import os, json, glob, argparse, datetime

SKIP = {'learner_objective'}
LABEL = {
    'definition': None, 'plain_explanation': None, 'components': None,
    'analysis_chain': 'Analysis', 'worked_application': 'Worked example',
    'misconception': 'Common errors', 'practice_guidance': 'In the exam',
    'evaluation': None, 'summary': None, 'cross_link': 'Connections',
}


def render(workspace, topic):
    td = os.path.join(workspace, 'topics', topic)
    contract = json.load(open(os.path.join(td, 'contract.json')))
    units = [json.load(open(p)) for p in sorted(glob.glob(os.path.join(td, 'content-units', '*.json')))]
    # Order by where each unit's first objective sits in the registry, not by filename.
    # Filename order put external sources before internal ones on the pilot topic.
    reg_path = os.path.join(workspace, 'curriculum', 'objective_registry.json')
    pos = {}
    if os.path.exists(reg_path):
        pos = {o['objective_id']: n for n, o in enumerate(json.load(open(reg_path))['objectives'])}
    units.sort(key=lambda u: min([pos.get(o, 10 ** 6) for o in u.get('objective_ids', [])] or [10 ** 6]))

    out = ['# %s %s' % (topic, contract.get('topic_title', '')), '']
    out.append('*%s. Offline study notes, rendered from the approved content units on %s. '
               'Everything here is also what the flashcards are built from.*'
               % (contract.get('qualification', ''), datetime.date.today().isoformat()))
    out.append('')
    objs = []
    for u in units:
        for b in u['blocks']:
            if b['block_type'] == 'learner_objective' and b.get('text'):
                objs.append(b['text'].strip())
    if objs:
        out.append('**What this topic asks of you**')
        out.append('')
        for o in objs:
            out.append('- ' + o)
        out.append('')

    for u in units:
        out.append('---')
        out.append('')
        out.append('## ' + u.get('title', u['unit_id']))
        out.append('')
        for b in u['blocks']:
            if b['block_type'] in SKIP:
                continue
            head = b.get('heading')
            label = LABEL.get(b['block_type'])
            if head:
                out.append('### ' + head)
            elif label:
                out.append('### ' + label)
            out.append('')
            if b.get('text'):
                out.append(b['text'].strip())
                out.append('')
    return '\n'.join(out).rstrip() + '\n'


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('workspace'); ap.add_argument('topic'); ap.add_argument('--out', default=None)
    a = ap.parse_args()
    td = os.path.join(a.workspace, 'topics', a.topic)
    existing = sorted(glob.glob(os.path.join(td, 'notes-*.md')))
    out = a.out or (existing[0] if existing else os.path.join(td, 'notes-%s.md' % a.topic))
    text = render(a.workspace, a.topic)
    open(out, 'w').write(text)
    print('notes -> %s  (%d words)' % (out, len(text.split())))


if __name__ == '__main__':
    main()
