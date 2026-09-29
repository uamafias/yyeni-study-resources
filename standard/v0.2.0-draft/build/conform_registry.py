#!/usr/bin/env python3
"""Bring a workspace's objective_registry.json into line with the registry schema (CR-004).

    python3 conform_registry.py <workspace> [--source-rationale "..."]

Adds only what the schema requires and the registry lacks: the profile ids at the top, and
`related_ids` and `source_coverage` on each objective. It never changes an objective's
syllabus text, ids or topic. Idempotent. Found 2026-09-29: the 0450 and 0455 registries failed
C-00 on every topic, so every authored topic would have been rejected on a field the author
cannot fix.
"""
import argparse
import json
import os
import sys

import yaml

HERE = os.path.dirname(os.path.abspath(__file__))
SCHEMA = os.path.join(os.path.dirname(HERE), 'schemas', 'objective_registry.schema.json')
DEFAULT = ('No teaching source is approved for derivation for this syllabus (third-party notes held '
           'are unlicensed, R-04). Content is authored from the syllabus wording and the assessment corpus.')


def conform(ws, rationale=DEFAULT):
    p = os.path.join(ws, 'curriculum', 'objective_registry.json')
    reg = json.load(open(p))
    before = json.dumps(reg, sort_keys=True)
    qp = yaml.safe_load(open(os.path.join(ws, 'qualification-profile.yaml')))
    sp = yaml.safe_load(open(os.path.join(ws, 'subject-profile.yaml')))
    reg.setdefault('qualification_profile_id', qp['profile_id'])
    reg.setdefault('subject_profile_id', sp['profile_id'])
    for o in reg['objectives']:
        o.setdefault('related_ids', [])
        o.setdefault('source_coverage', {'rating': 0, 'action': 'generate_gap', 'rationale': rationale})
    if json.dumps(reg, sort_keys=True) != before:          # never rewrite an unchanged file
        json.dump(reg, open(p, 'w'), indent=1, ensure_ascii=False)
    from jsonschema import Draft202012Validator
    errs = list(Draft202012Validator(json.load(open(SCHEMA))).iter_errors(reg))
    return p, errs


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('workspace')
    ap.add_argument('--source-rationale', default=DEFAULT)
    a = ap.parse_args()
    path, errs = conform(a.workspace.rstrip('/'), a.source_rationale)
    for e in errs[:10]:
        print('  %s: %s' % (list(e.path)[:4], e.message[:140]))
    print('%s: %d schema violations' % (path, len(errs)))
    sys.exit(1 if errs else 0)
