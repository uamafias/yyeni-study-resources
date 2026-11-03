"""Enforce the reviewed source-card disposition without changing history.

Only slot identities, reviewed decisions and content hashes are retained.
The removed static bank is not needed to draw or preserve historical questions.
"""
from functools import lru_cache
import hashlib
import json
from pathlib import Path

from services.math_generators import GeneratorError

DATA = Path(__file__).resolve().parents[2] / 'data/imports/nam-6131-nssco-2026'
TARGET_GENERATORS=frozenset(k.rsplit(':',1)[0] for k in
    json.loads(Path(__file__).with_name('legacy_rules.json').read_text())['settings'])


class RetiredAssignmentNeedsReview(GeneratorError):
    """No approved equivalent exists; the teacher must refresh the assignment."""


def card_key(generator_id, params):
    return f"{generator_id}:{params.get('level')}:{params.get('slot')}"


@lru_cache(maxsize=1)
def source_policy():
    disposition = json.loads((DATA / 'workbench-disposition.json').read_text())
    if disposition.get('schema_version') != 'workbench-slot-policy-v2':
        raise GeneratorError('Unsupported Workbench slot policy')
    decisions = {r['source_card_key']: r for r in disposition['cards']}
    if len(decisions) != len(disposition['cards']):
        raise GeneratorError('Workbench slot decisions must be unique')
    source = {}
    for key, row in decisions.items():
        gid, _, _ = key.rsplit(':', 2)
        params = row['generator_params']
        if (row['status'] not in {'retained', 'retired', 'excluded_from_main_exam_bank'}
                or any(type(params.get(k)) is not int or params[k] < 1 for k in ('level','slot'))
                or card_key(gid, params) != key
                or (row['status'] != 'retained' and len(row.get('content_sha256', '')) != 64)):
            raise GeneratorError('Invalid workbench source-card disposition')
        source[key] = {'generator_id': gid, 'generator_params': params,
                       'content_sha256': row.get('content_sha256')}
    return source, decisions


def content_hash(card):
    fields = ('question', 'answer', 'explanation', 'question_image_url', 'answer_image_url')
    values = {field: getattr(card, field, None) for field in fields}
    return hashlib.sha256(json.dumps(values, sort_keys=True, ensure_ascii=False).encode()).hexdigest()


def slot_allowed(generator_id, params):
    if generator_id not in TARGET_GENERATORS:
        return True
    _, decisions = source_policy()
    if any(type(params.get(k)) is not int or params[k] < 1 for k in ('level', 'slot')):
        return False
    row = decisions.get(card_key(generator_id, params))
    if row is None and params['slot'] > 10:
        # Existing custom decks may contain more than ten slots. They may draw
        # from a retained setting, subject to screening every actual question.
        prefix = f"{generator_id}:{params['level']}:"
        return any(key.startswith(prefix) and value['status'] == 'retained'
                   for key, value in decisions.items())
    return row is not None and row['status'] == 'retained'


def draw_parameters(generator_id, params):
    """Recover an excluded slot using a reviewed equivalent objective scope.

    No task is dropped. The actual fresh question is still screened and its
    denominator is derived from its own frozen contract. Assignment/history
    snapshots stay untouched; the round records the substitution explicitly.
    """
    if slot_allowed(generator_id,params):
        return dict(params),None
    source,decisions=source_policy()
    key=card_key(generator_id,params)
    original=decisions.get(key)
    if original is None:
        raise GeneratorError('Invalid or unreviewed maths recipe parameters')
    if not original['objective_ids']:
        raise RetiredAssignmentNeedsReview('This assignment includes a retired maths task with no reviewed equivalent. Ask the teacher to refresh the assigned cards.')
    candidates=[k for k,r in decisions.items() if r['status']=='retained'
        and source[k]['generator_id']==generator_id
        and set(r['objective_ids'])==set(original['objective_ids'])]
    candidates.sort(key=lambda k:(abs(source[k]['generator_params']['level']-params['level']),k))
    if not candidates:
        raise RetiredAssignmentNeedsReview('This assignment needs teacher reassignment: no reviewed replacement covers the retired task’s objectives.')
    replacement=candidates[0]
    return dict(source[replacement]['generator_params']),{
        'reason':'Retired source task replaced by a reviewed task with the same assessed objective scope.',
        'original_source_card_key':key,'replacement_source_card_key':replacement,
        'objective_ids':original['objective_ids']}


def filter_topic(content):
    """Filter an already validated historical package in place."""
    for lesson in content['lessons']:
        lesson['cards'] = [c for c in lesson['cards']
                           if slot_allowed(c['generator_id'], c['generator_params'])]
        lesson['generators'] = list(dict.fromkeys(c['generator_id'] for c in lesson['cards']))
    return content


def retirement_plan(cards):
    """Retire excluded rows including copies; preserve edits and report them."""
    source, decisions = source_policy()
    deactivate, edited = [], []
    for card in cards:
        if not card.is_active or not isinstance(card.generator_params, dict):
            continue
        key = card_key(card.generator_id, card.generator_params)
        if key not in decisions or decisions[key]['status'] == 'retained':
            continue
        original = source[key]
        deactivate.append(card)
        if content_hash(card) != original['content_sha256']:
            edited.append(card.id)
    return deactivate, edited
