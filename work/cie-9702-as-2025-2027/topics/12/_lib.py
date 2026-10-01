#!/usr/bin/env python3
"""Shared helpers for building topic 12 artefacts (claims already exist on disk)."""
import json, os, hashlib, sys

ROOT = '/Users/professor/Documents/YYeni Study Resources'
WS = os.path.join(ROOT, 'work/cie-9702-as-2025-2027')
STD = os.path.join(ROOT, 'standard/v0.2.0-draft')
sys.path.insert(0, os.path.join(STD, 'checks'))
from yyeni_checks import _artefact_text  # noqa: E402

TOPIC = '12'
TDIR = os.path.join(WS, 'topics', TOPIC)

LEDGER = json.load(open(os.path.join(TDIR, 'claims/canonical_claim_ledger.json')))
CLAIMS = {c['claim_id']: c for c in LEDGER['claims']}


def stamp(x):
    x['authored_hash'] = hashlib.sha256(_artefact_text(x).encode()).hexdigest()
    return x


def block(block_id, block_type, heading, text, claim_ids, ao=('AO3',)):
    b = {
        'block_id': block_id,
        'block_type': block_type,
        'heading': heading,
        'text': text.strip(),
        'claim_ids': list(claim_ids),
        'context_tags': [],
        'assessment_objectives': list(ao),
        'claims_seen': {cid: CLAIMS[cid]['revision'] for cid in claim_ids},
    }
    return stamp(b)


def wc(text):
    return len(text.split())


def save(path, obj):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w') as fh:
        json.dump(obj, fh, indent=1)
    print('wrote %s' % os.path.relpath(path, WS))
