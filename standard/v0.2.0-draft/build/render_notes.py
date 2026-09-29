#!/usr/bin/env python3
"""
Render a topic's offline learner notes from its approved content units.

RS-16: published outputs are derived from the same approved structured source.
RS-39: rendering rather than hand-writing the notes makes notes-to-card drift
structurally impossible - the notes ARE the content units.

    python3 render_notes.py <workspace> <topic-id>

The output filename is derived from the contract's topic_title (see build/naming.py),
so every topic in every subject is named the same way and a human can read the folder.
"""
import os, sys, json, glob, argparse, datetime

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
    ap.add_argument('workspace'); ap.add_argument('topic')
    ap.add_argument('--out', default=None,
                    help='override the derived filename. Do not: the name is derived from the '
                         'contract title so that every subject names its files the same way.')
    a = ap.parse_args()
    td = os.path.join(a.workspace, 'topics', a.topic)
    # The filename is DERIVED from the topic title in the contract, never chosen by the author.
    # A file called notes-4.3.md tells a human nothing; 4.3-capacity-utilisation-and-outsourcing.md
    # tells them everything without opening it.
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    from naming import notes_filename
    title = json.load(open(os.path.join(td, 'contract.json'))).get('topic_title', '')
    out = a.out or os.path.join(td, notes_filename(a.topic, title))
    stale = [p for p in sorted(set(glob.glob(os.path.join(td, 'notes-*.md')) +
                                   glob.glob(os.path.join(td, '*.md'))))
             if os.path.basename(p) != os.path.basename(out) and
             (os.path.basename(p).startswith('notes-') or os.path.basename(p)[0].isdigit())]
    text = render(a.workspace, a.topic)
    open(out, 'w').write(text)
    print('notes -> %s  (%d words)' % (out, len(text.split())))
    for p in stale:
        try:
            os.remove(p)
            print('       removed superseded %s' % os.path.basename(p))
        except OSError:
            print('       NOTE: %s is a superseded notes file under the old naming and could not be '
                  'removed here. Delete it by hand so the topic has one notes file.' % p)


if __name__ == '__main__':
    main()
