#!/usr/bin/env python3
"""Assemble a whole subject's learner-facing folder, named for humans.

    python3 publish_subject.py <workspace> [--out publish/<qualification>]

Produces, from the approved build and nothing else:

    publish/<qualification>/
      INDEX.md                       one page: every topic by name, grouped by syllabus unit
      MANIFEST.json                  the same, machine-readable
      notes/4.3-capacity-utilisation-and-outsourcing.md
      flashcards/4.3-capacity-utilisation-and-outsourcing-flashcards.json

Every filename is derived from the topic title in the contract (build/naming.py), and every
flashcard carries `objective_titles` beside `objective_ids` so a person reviewing a card sees
what it teaches without looking up a code. Nothing here is typed by hand, so the next subject
comes out named the same way without anyone remembering to do it.

A topic whose deterministic checks fail is NOT published; the run reports it and continues, so
one broken topic cannot hold up a subject.
"""
import argparse
import datetime
import glob
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(os.path.dirname(HERE), 'checks'))
from naming import notes_filename, flashcards_filename, topic_label  # noqa: E402
from yyeni_checks import read_practice_text  # noqa: E402

UNIT_TITLES_HINT = ('unit_titles.json in the workspace curriculum folder, if present, maps a '
                    'leading topic digit to a unit name for the index headings.')


def _json(p):
    with open(p) as fh:
        return json.load(fh)


def _key(t):
    try:
        return [int(x) for x in t.split('.')]
    except ValueError:
        return [9999]


def collect(ws):
    reg_path = os.path.join(ws, 'curriculum', 'objective_registry.json')
    titles = {}
    if os.path.exists(reg_path):
        for o in _json(reg_path)['objectives']:
            titles[o['objective_id']] = o.get('learner_objective') or o.get('text') or ''
    tdir = os.path.join(ws, 'topics')
    rows = []
    for t in sorted([d for d in os.listdir(tdir) if os.path.isdir(os.path.join(tdir, d))], key=_key):
        d = os.path.join(tdir, t)
        cp = os.path.join(d, 'contract.json')
        if not os.path.exists(cp):
            continue
        c = _json(cp)
        title = c.get('topic_title') or ''
        notes = os.path.join(d, notes_filename(t, title))
        if not os.path.exists(notes):
            legacy = sorted(glob.glob(os.path.join(d, 'notes-*.md')))
            notes = legacy[0] if legacy else None
        items = []
        for f in sorted(glob.glob(os.path.join(d, 'learning-items', '*.json'))):
            items += _json(f).get('items', [])
        qa = os.path.join(d, 'qa_report.json')
        q = _json(qa) if os.path.exists(qa) else {}
        rows.append({'topic_id': t, 'title': title, 'notes_path': notes, 'items': items,
                     'qa': q, 'objective_titles': titles, 'dir': d})
    return rows


def qualification_name(ws):
    """The human name, composed from the qualification profile - board level, subject, code,
    syllabus version and the years it is examined. Falls back to the folder slug."""
    qp = os.path.join(ws, 'qualification-profile.yaml')
    if not os.path.exists(qp):
        return os.path.basename(ws.rstrip('/'))
    try:
        import yaml
        q = yaml.safe_load(open(qp)) or {}
    except Exception:
        return os.path.basename(ws.rstrip('/'))
    name = ' '.join(str(x) for x in (q.get('qualification'), q.get('subject'),
                                     q.get('syllabus_code')) if x).strip()
    bits = []
    if q.get('syllabus_version'):
        bits.append('syllabus v%s' % q['syllabus_version'])
    yrs = q.get('examination_years') or []
    if yrs:
        bits.append('examined %s' % (('%s-%s' % (yrs[0], yrs[-1])) if len(yrs) > 1 else yrs[0]))
    if bits:
        name = '%s (%s)' % (name, ', '.join(bits))
    return name or os.path.basename(ws.rstrip('/'))


def publish(ws, out):
    os.makedirs(os.path.join(out, 'notes'), exist_ok=True)
    os.makedirs(os.path.join(out, 'flashcards'), exist_ok=True)
    rows, man, skipped = collect(ws), [], []
    qual = qualification_name(ws)
    slug_id = os.path.basename(ws.rstrip('/'))
    for r in rows:
        t, title, q = r['topic_id'], r['title'], r['qa']
        if q.get('release_decision') == 'reject':
            skipped.append('%s (%s): deterministic checks fail, so it is not published'
                           % (t, title or 'untitled'))
            continue
        if not r['notes_path']:
            skipped.append('%s (%s): no rendered notes' % (t, title or 'untitled'))
            continue
        nf = notes_filename(t, title)
        with open(os.path.join(out, 'notes', nf), 'w') as fh:
            fh.write(open(r['notes_path']).read())
        items = []
        for it in r['items']:
            it = dict(it)
            it['objective_titles'] = [r['objective_titles'].get(o, o) for o in (it.get('objective_ids') or [])]
            tid = (it.get('context') or {}).get('text_id')
            if tid:                       # RS-48: the practice text travels with the task that uses it
                tp = os.path.join(r['dir'], 'texts', tid + '.md')
                meta, body = read_practice_text(tp)
                it['stimulus_text'] = {'text_id': tid, 'title': meta.get('title'), 'genre': meta.get('genre'),
                                       'words': len(body.split()), 'body': body}
                os.makedirs(os.path.join(out, 'texts'), exist_ok=True)
                with open(os.path.join(out, 'texts', tid + '.md'), 'w') as fh:
                    fh.write(open(tp, encoding='utf-8').read())
            items.append(it)
        ff = flashcards_filename(t, title)
        with open(os.path.join(out, 'flashcards', ff), 'w') as fh:
            json.dump({'topic_number': t, 'topic_title': title, 'topic': topic_label(t, title),
                       'qualification': qual, 'item_count': len(items), 'items': items},
                      fh, indent=1, ensure_ascii=False)
        open_issues = sum(1 for rv in q.get('semantic_reviews', []) for i in rv.get('issues', [])
                          if i.get('status') not in ('resolved', 'rejected'))
        man.append({'topic_id': t, 'title': title, 'topic': topic_label(t, title),
                    'notes': nf, 'flashcards': ff, 'items': len(items),
                    'notes_words': len(open(r['notes_path']).read().split()),
                    'release_decision': q.get('release_decision', 'unknown'),
                    'deterministic': (q.get('notes') or [''])[0].split('. ', 1)[-1],
                    'open_review_issues': open_issues})
    return man, skipped, qual


def write_index(out, man, qual, ws):
    up = os.path.join(ws, 'curriculum', 'unit_titles.json')
    units = _json(up) if os.path.exists(up) else {}
    L = ['# %s' % qual, '',
         'Study notes and flashcards. %d topics, %s flashcards and performance tasks, %s words of notes.'
         % (len(man), format(sum(m['items'] for m in man), ','),
            format(sum(m['notes_words'] for m in man), ',')), '',
         'Every topic here passes the full deterministic check suite. Semantic review runs on '
         'published material rather than ahead of it, so the **Open issues** column is debt that '
         'ships visibly and is cleared in a maintenance pass - it is not a warning that the topic '
         'is unusable.', '']
    cur = None
    for m in sorted(man, key=lambda m: _key(m['topic_id'])):
        u = m['topic_id'].split('.')[0]
        if u != cur:
            cur = u
            L += ['', '## %s' % units.get(u, 'Unit %s' % u), '',
                  '| Topic | Notes | Flashcards | Items | Words | Open issues |',
                  '|---|---|---|---:|---:|---:|']
        L.append('| **%s** %s | [%s](notes/%s) | [%s](flashcards/%s) | %d | %s | %s |'
                 % (m['topic_id'], m['title'], m['notes'], m['notes'], m['flashcards'],
                    m['flashcards'], m['items'], format(m['notes_words'], ','),
                    m['open_review_issues'] or '—'))
    L += ['', '## What is in a flashcard file', '',
          'One JSON file per topic, carrying `topic_number`, `topic_title` and a list of `items`. '
          'Each item has:', '',
          '- `prompt` — what the learner sees',
          '- `canonical_answer` — the model answer',
          '- `marking_guidance` — what earns credit, part by part',
          '- `subtype` — DEF, DIST, APP, CHAIN, EVAL, CALC and so on, or a performance task',
          '- `assessment_objectives` — what the examination credits, and `difficulty` 1 to 5',
          '- `blooms_level` — what the learner is being asked to do: Remember, Understand, Apply, '
          'Analyse, Evaluate or Create. A different axis from the assessment objective, and on '
          'every item',
          '- `objective_ids` **and `objective_titles`** — what the card teaches, by code and in words',
          '- `claim_ids` — the claims in the topic ledger the answer rests on', '',
          '## Where the source lives', '',
          'This folder is the copy to upload. The source of record is '
          '`%s/topics/<number>/`, which holds each topic\'s claim ledger, content units, learning '
          'items and QA report. Regenerate this folder at any time with '
          '`build/publish_subject.py`; nothing in it is edited by hand.' % ws, '']
    open(os.path.join(out, 'INDEX.md'), 'w').write('\n'.join(L))


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('workspace')
    ap.add_argument('--out', default=None)
    a = ap.parse_args()
    ws = a.workspace.rstrip('/')
    out = a.out or os.path.join('publish', os.path.basename(ws))
    man, skipped, qual = publish(ws, out)
    write_index(out, man, qual, ws)
    with open(os.path.join(out, 'MANIFEST.json'), 'w') as fh:
        json.dump({'qualification': qual,
                   'qualification_id': os.path.basename(ws),
                   'generated_at': datetime.datetime.now(datetime.timezone.utc)
                   .strftime('%Y-%m-%dT%H:%M:%SZ'),
                   'standard': 'YYeni Study Resource Generation Standard v0.2.0-draft',
                   'gate': 'Deterministic check suite only. Semantic review runs on published '
                           'material (RS-42, amended 2026-09-12).',
                   'totals': {'topics': len(man), 'items': sum(m['items'] for m in man),
                              'notes_words': sum(m['notes_words'] for m in man)},
                   'not_published': skipped,
                   'topics': man}, fh, indent=1, ensure_ascii=False)
    print('published %d topics -> %s' % (len(man), out))
    print('  %d items, %s words of notes'
          % (sum(m['items'] for m in man), format(sum(m['notes_words'] for m in man), ',')))
    for s in skipped:
        print('  NOT PUBLISHED: %s' % s)


if __name__ == '__main__':
    main()
