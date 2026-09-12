#!/usr/bin/env python3
"""
Plan (but do not author) the learning items a topic needs.

This is Step A of a two-step flashcard/learning-item pipeline:

    plan_items.py   (this file)  -- deterministic, no model calls.
                                     claims + content-unit blocks -> a shaped
                                     list of items to write, plus a command-word
                                     coverage gap report (RS-37).
    author_items.py (not built yet) -- takes one planned row at a time, gives an
                                     agent ONLY the cited claims' text, and asks
                                     it to write prompt/canonical_answer/
                                     marking_guidance, stamping claims_seen +
                                     authored_hash (RS-41).

Why split this way: RS-39 requires every canonical answer to be reconstructible
from the topic's own content units. The only reliable way to guarantee that is
to decide, mechanically, exactly which claims an item is allowed to cite BEFORE
any prose is written -- so the authoring step physically cannot reach outside
its citation set.

    python3 plan_items.py <workspace-dir-containing-build_manifest.json> \
        [--out item_plan.json] [--command-map command_word_map.json]

Output: item_plan.json --
  { "topic_id": ..., "candidates": [...], "command_word_gaps": [...] }

A "candidate" is not a learning item. It has no prompt or answer yet -- only
enough to hand to the authoring step: which claims, which shape, why.
"""
import os
import json
import argparse
import hashlib

# --- block_type -> a flashcard subtype, for blocks whose content is naturally
# one atomic recall fact. RS-24: this is a default, not a mandate -- every
# other block type below still needs a home, they just don't collapse to a
# single flashcard.
FLASHCARD_SUBTYPE = {
    'definition': 'DEF',
    'components': 'FEATURE',
    'comparison': 'DIST',
    'process': 'PROC',
    'benefit': 'BEN',
    'limitation': 'LIM',
    'evaluation': 'EVAL',
    'misconception': 'MISCON',
    'interpretation': 'INTERP',
    'summary': 'SYNTH',
}

# block_type -> (item_type, subtype). Quantitative content gets its own family
# per RS-22 (formula, variables, units, worked calc, interpretation, limits).
DIRECT_ITEM_TYPE = {
    'worked_calculation': ('calculation', 'CALC'),
    'formula': ('calculation', 'CALC'),
}

# Blocks that only make sense combined into a richer, contextual item rather
# than split into atomic flashcards (RS-20: genuine context; RS-21: defensible
# causal chains). One candidate per *unit* here, not per block.
APPLIED_BLOCK_TYPES = {'worked_application', 'analysis_chain'}

# Blocks that support the prose but aren't independently assessable as an item
# on their own. Not silently ignored -- listed in the report as "not_planned"
# so a human can see the decision, not just infer it from absence.
NOT_PLANNED = {
    'learner_objective', 'key_question', 'cross_link', 'practice_guidance',
    'plain_explanation', 'example', 'non_example', 'stakeholder_effect',
    'enrichment',
}

# Default command-word -> acceptable (item_type, subtype) shapes, used only to
# find GAPS (RS-37: every objective needs practice shaped like its own command
# words). This belongs in the qualification/subject profile long-term (RS-03,
# RS-19) -- pass --command-map to override with a profile-derived file.
DEFAULT_COMMAND_WORD_SHAPES = {
    'Define': [('flashcard', 'DEF')],
    'State': [('flashcard', 'DEF')],
    'Identify': [('flashcard', 'FEATURE')],
    'Describe': [('flashcard', 'FEATURE'), ('flashcard', 'PROC')],
    'Explain': [('flashcard', 'WHY'), ('flashcard', 'MECH'), ('case_analysis', None)],
    'Analyse': [('case_analysis', None), ('flashcard', 'CHAIN'), ('data_response', None)],
    'Evaluate': [('case_analysis', None), ('essay_plan', None), ('flashcard', 'EVAL')],
    'Discuss': [('essay_plan', None), ('case_analysis', None)],
    'Calculate': [('calculation', 'CALC')],
    'Compare': [('flashcard', 'DIST')],
    'Assess': [('essay_plan', None), ('case_analysis', None)],
}


def load(path):
    with open(path) as f:
        return json.load(f)


def resolve(base, rel):
    return os.path.normpath(os.path.join(base, rel))


def claim_hash(text):
    return hashlib.sha256(text.encode('utf-8')).hexdigest()[:16]


def load_workspace(workspace):
    manifest = load(os.path.join(workspace, 'build_manifest.json'))
    ledger = load(resolve(workspace, manifest['claim_ledger']))
    registry = load(resolve(workspace, manifest['objective_registry']))
    units = [load(resolve(workspace, rel)) for rel in manifest['content_units']]
    existing = []
    for rel in manifest.get('learning_items', []):
        path = resolve(workspace, rel)
        if os.path.exists(path):
            existing.append(load(path))
    return manifest, ledger, registry, units, existing


def claims_by_objective(ledger):
    out = {}
    for c in ledger['claims']:
        for oid in c['objective_ids']:
            out.setdefault(oid, []).append(c)
    return out


def existing_claim_sets(existing_datasets):
    """(item_type, subtype, frozenset(claim_ids)) already authored -> item_id.
    Used only to avoid re-planning something already written; not a QA check."""
    seen = {}
    for ds in existing_datasets:
        for it in ds['items']:
            key = (it['item_type'], it.get('subtype'), frozenset(it['claim_ids']))
            seen[key] = it['item_id']
    return seen


def plan_objective(obj, obj_claims, units, seen):
    claim_ids = {c['claim_id'] for c in obj_claims}
    claim_text = {c['claim_id']: c['text'] for c in obj_claims}
    candidates = []
    not_planned = []
    applied_claims = set()
    applied_blocks = []

    for unit in units:
        for block in unit['blocks']:
            cited = [cid for cid in block.get('claim_ids', []) if cid in claim_ids]
            if not cited:
                continue
            bt = block['block_type']

            if bt in APPLIED_BLOCK_TYPES:
                applied_claims.update(cited)
                applied_blocks.append(block['block_id'])
                continue

            if bt in NOT_PLANNED:
                not_planned.append({'block_id': block['block_id'], 'block_type': bt,
                                     'claim_ids': cited})
                continue

            if bt in DIRECT_ITEM_TYPE:
                item_type, subtype = DIRECT_ITEM_TYPE[bt]
            elif bt in FLASHCARD_SUBTYPE:
                item_type, subtype = 'flashcard', FLASHCARD_SUBTYPE[bt]
            else:
                not_planned.append({'block_id': block['block_id'], 'block_type': bt,
                                     'claim_ids': cited, 'reason': 'unmapped_block_type'})
                continue

            key = (item_type, subtype, frozenset(cited))
            candidates.append({
                'objective_id': obj['objective_id'],
                'source_block_ids': [block['block_id']],
                'claim_ids': sorted(cited),
                'claim_text': {cid: claim_text[cid] for cid in cited},
                'item_type': item_type,
                'subtype': subtype,
                'core_status': obj.get('route_status', 'core'),
                'already_authored_as': seen.get(key),
                'rationale': 'block_type=%s' % bt,
            })

    if applied_claims:
        key = ('case_analysis', None, frozenset(applied_claims))
        candidates.append({
            'objective_id': obj['objective_id'],
            'source_block_ids': applied_blocks,
            'claim_ids': sorted(applied_claims),
            'claim_text': {cid: claim_text[cid] for cid in applied_claims},
            'item_type': 'case_analysis',
            'subtype': None,
            'core_status': obj.get('route_status', 'core'),
            'already_authored_as': seen.get(key),
            'rationale': 'worked_application/analysis_chain blocks combined for genuine context (RS-20)',
        })

    return candidates, not_planned


def command_word_gaps(obj, candidates, shapes):
    have = {(c['item_type'], c['subtype']) for c in candidates}
    have_typeless = {c['item_type'] for c in candidates}
    gaps = []
    for cw in obj.get('command_words', []):
        acceptable = shapes.get(cw)
        if acceptable is None:
            gaps.append({'objective_id': obj['objective_id'], 'command_word': cw,
                         'reason': 'command word has no configured shape -- add to command-word map'})
            continue
        satisfied = any((it, st) in have or (st is None and it in have_typeless)
                        for it, st in acceptable)
        if not satisfied:
            gaps.append({'objective_id': obj['objective_id'], 'command_word': cw,
                         'reason': 'no planned item matches an acceptable shape',
                         'acceptable_shapes': acceptable})
    return gaps


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('workspace', help='directory containing build_manifest.json')
    ap.add_argument('--out', default=None)
    ap.add_argument('--command-map', default=None,
                     help='JSON file of {command_word: [[item_type, subtype], ...]} overriding the built-in defaults')
    args = ap.parse_args()

    shapes = dict(DEFAULT_COMMAND_WORD_SHAPES)
    if args.command_map:
        override = load(args.command_map)
        shapes.update({k: [tuple(pair) for pair in v] for k, v in override.items()})

    manifest, ledger, registry, units, existing = load_workspace(args.workspace)
    seen = existing_claim_sets(existing)
    by_obj = claims_by_objective(ledger)

    all_candidates, all_gaps, all_not_planned = [], [], []
    for obj in registry['objectives']:
        obj_claims = by_obj.get(obj['objective_id'], [])
        if not obj_claims:
            all_gaps.append({'objective_id': obj['objective_id'],
                              'command_word': None,
                              'reason': 'objective has no claims in the ledger -- nothing to plan from'})
            continue
        candidates, not_planned = plan_objective(obj, obj_claims, units, seen)
        all_candidates.extend(candidates)
        all_not_planned.extend(not_planned)
        all_gaps.extend(command_word_gaps(obj, candidates, shapes))

    plan = {
        'topic_id': manifest.get('scope', {}).get('selected_level'),
        'source_manifest': manifest['build_id'],
        'candidates': all_candidates,
        'command_word_gaps': all_gaps,
        'not_planned_blocks': all_not_planned,
    }

    out = args.out or os.path.join(args.workspace, 'item_plan.json')
    with open(out, 'w') as f:
        json.dump(plan, f, indent=2)

    to_author = sum(1 for c in all_candidates if not c['already_authored_as'])
    print('item_plan -> %s' % out)
    print('  %d candidates (%d already authored, %d to author)' %
          (len(all_candidates), len(all_candidates) - to_author, to_author))
    print('  %d not-planned blocks (review these -- see NOT_PLANNED set)' % len(all_not_planned))
    print('  %d command-word coverage gaps' % len(all_gaps))
    for g in all_gaps:
        print('    - %s: %s (%s)' % (g['objective_id'], g['command_word'], g['reason']))


if __name__ == '__main__':
    main()
