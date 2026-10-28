#!/usr/bin/env python3
"""
Publish 6145 with its diagram images.

    python3 work/nam-6145-nssco-2026/diagrams/publish_6145_with_diagrams.py [--out DIR] [--allow-incomplete]

The standard publisher copies notes and flashcards but not images. This helper:

1. refuses to run while any work-order slot is unfilled, unless --allow-incomplete is given, and
   refuses --allow-incomplete for the real publish/ folder, so a partial build is never published;
2. runs standard/v0.2.0-draft/build/publish_subject.py unchanged;
3. copies every PNG the published notes reference (diagrams/<name>.png) from its topic folder into
   <out>/notes/diagrams/, and fails if any reference does not resolve;
4. writes <out>/diagram-assets.json, the asset manifest with publication-relative paths and hashes,
   as the sidecar for the later managed-image import.

It never edits exported notes or flashcards.
"""
import argparse
import glob
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
WS = os.path.dirname(HERE)
ROOT = os.path.dirname(os.path.dirname(WS))
REF = re.compile(r'\]\((diagrams/[A-Za-z0-9._-]+\.png)\)')


def sha(path):
    return hashlib.sha256(open(path, 'rb').read()).hexdigest()


def unfilled_slots():
    missing = []
    for d in sorted(glob.glob(os.path.join(WS, 'topics', '*', ''))):
        t = os.path.basename(d.rstrip('/'))
        wo = json.load(open(os.path.join(d, 'work_order.json')))
        have = {i['item_id'] for i in json.load(open(os.path.join(d, 'learning-items', 'topic_%s_items.json' % t)))['items']}
        slots = [s['slot'] for s in wo['item_slots']] + [p.get('package_id', p.get('slot')) for p in wo['performance_tasks']]
        missing += [s for s in slots if s not in have]
    return missing


def complete_build_errors():
    """A full set of IDs is insufficient: the standard publisher skips failing topics."""
    from collections import Counter
    errors = []
    for d in sorted(glob.glob(os.path.join(WS, 'topics', '*', ''))):
        topic = os.path.basename(d.rstrip('/'))
        wo = json.load(open(os.path.join(d, 'work_order.json')))
        items = json.load(open(os.path.join(d, 'learning-items', 'topic_%s_items.json' % topic)))['items']
        counts = Counter(i['item_id'] for i in items)
        wanted = {s['slot'] for s in wo['item_slots'] + wo['performance_tasks']}
        if set(counts) != wanted or any(n != 1 for n in counts.values()):
            errors.append('%s: item IDs do not fill every slot exactly once' % topic)
        qa = json.load(open(os.path.join(d, 'qa_report.json')))
        if qa.get('release_decision') != 'publish':
            errors.append('%s: topic is not PUBLISH' % topic)
        if qa.get('metrics', {}).get('learning_item_count') != len(wanted):
            errors.append('%s: QA counts do not describe the complete current scope' % topic)
    return errors


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--out', default=os.path.join(ROOT, 'publish', os.path.basename(WS)))
    ap.add_argument('--allow-incomplete', action='store_true',
                    help='test run while slots are still unfilled; refused for the real publish/ folder')
    a = ap.parse_args()
    out = os.path.abspath(a.out)
    real = os.path.abspath(os.path.join(ROOT, 'publish', os.path.basename(WS)))
    missing = unfilled_slots()
    if missing and not a.allow_incomplete:
        sys.exit('%d work-order slots are unfilled (first: %s). Publication waits for every slot.' % (len(missing), missing[0]))
    if missing and out == real:
        sys.exit('Refusing to write an incomplete build into %s.' % os.path.relpath(real, ROOT))
    if not a.allow_incomplete:
        errors = complete_build_errors()
        if errors:
            sys.exit('Refusing a partial or unchecked publication:\n  ' + '\n  '.join(errors))

    subprocess.run([sys.executable, os.path.join(ROOT, 'standard', 'v0.2.0-draft', 'build', 'publish_subject.py'),
                    WS, '--out', out], check=True, cwd=ROOT)

    if not a.allow_incomplete:
        expected = {s['slot'] for p in glob.glob(os.path.join(WS, 'topics', '*', 'work_order.json'))
                    for s in (lambda wo: wo['item_slots'] + wo['performance_tasks'])(json.load(open(p)))}
        from collections import Counter
        exported = Counter(i['item_id'] for p in glob.glob(os.path.join(out, 'flashcards', '*.json'))
                           for i in json.load(open(p))['items'])
        if set(exported) != expected or any(n != 1 for n in exported.values()):
            sys.exit('Publication does not contain every approved slot exactly once; do not upload it.')

    copied, broken = {}, []
    dest_dir = os.path.join(out, 'notes', 'diagrams')
    for notes in sorted(glob.glob(os.path.join(out, 'notes', '*.md'))):
        topic = os.path.basename(notes).split('-', 1)[0]
        for ref in REF.findall(open(notes).read()):
            src = os.path.join(WS, 'topics', topic, ref)
            if not os.path.exists(src):
                broken.append('%s -> %s' % (os.path.basename(notes), ref))
                continue
            os.makedirs(dest_dir, exist_ok=True)
            shutil.copy2(src, os.path.join(dest_dir, os.path.basename(ref)))
            copied[ref] = sha(src)
    for ref, h in copied.items():
        if sha(os.path.join(out, 'notes', ref)) != h:
            broken.append('copy mismatch %s' % ref)
    if broken:
        sys.exit('Unresolved or damaged image references:\n  ' + '\n  '.join(broken))

    manifest = json.load(open(os.path.join(HERE, 'asset-manifest.json')))
    side_out = {'manifest': manifest['manifest'], 'paths_are_relative_to': 'the publication folder',
                'upload_status': manifest['upload_status'], 'items': {}}
    for iid, e in manifest['items'].items():
        if 'question' not in e:
            side_out['items'][iid] = {'status': e['status']}
            continue
        entry = {'topic_id': e['topic_id'], 'status': e['status']}
        for side in ('question', 'answer'):
            src = os.path.join(WS, e[side]['png'])
            rel = 'card-images/' + os.path.basename(src)
            os.makedirs(os.path.join(out, 'card-images'), exist_ok=True)
            shutil.copy2(src, os.path.join(out, rel))
            entry[side] = {'png': rel, 'png_sha256': sha(src), 'alt_text': e[side]['alt_text'],
                           'yyeni_field': e[side]['yyeni_field'], 'yyeni_asset_id': None}
        side_out['items'][iid] = entry
    json.dump(side_out, open(os.path.join(out, 'diagram-assets.json'), 'w'), indent=2, ensure_ascii=False)
    print('notes images copied: %d; card images: %d; sidecar: %s' % (
        len(copied), 2 * sum(1 for e in side_out['items'].values() if 'question' in e), os.path.join(out, 'diagram-assets.json')))


if __name__ == '__main__':
    main()
