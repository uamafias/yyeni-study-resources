"""CR-007 (2026-10-01), from the first four authoring runs. C-32 evaluates a left side of any length, with
multiplication and division first, and never starts an operand inside another number; a MISCON item may carry
the register entry it discriminates."""
import json
import os
import sys
import types

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(HERE, 'checks'))
import yyeni_checks as Y  # noqa: E402


def _b(*answers):
    return types.SimpleNamespace(items=[{'item_id': 'I%d' % n, 'item_type': 'flashcard', 'subtype': 'CALC',
                                         'prompt': 'Calculate.', 'canonical_answer': a, 'marking_guidance': [],
                                         'context': {}} for n, a in enumerate(answers)], profile=None, units=[])


def test_a_three_factor_product_is_evaluated_whole():
    assert Y.c32(_b('p = ρgΔh = 1000 × 9.81 × 0.20 = 1962 Pa'))[0] == 'pass'
    assert Y.c32(_b('p = 1000×9.81×0.20 = 1962 Pa'))[0] == 'pass'
    assert Y.c32(_b('E = 0.5 × 2.0 × 3.0 = 3.0 J'))[0] == 'pass'


def test_a_wrong_chain_still_fails():
    status, msg, _ = Y.c32(_b('1000 x 9.81 x 0.20 = 2962'))
    assert status == 'fail' and '1962' in msg


def test_precedence_is_respected():
    assert Y.c32(_b('2 + 3 × 4 = 14'))[0] == 'pass'
    assert Y.c32(_b('2 + 3 × 4 = 20'))[0] == 'fail'
    assert Y.c32(_b('profit = 50 - 20 - 10 = 20'))[0] == 'pass'


def test_no_operand_starts_inside_a_decimal():
    # before CR-007 the 81 of 9.81 was read as the left operand of "81 × 0.20 = 1962"
    assert Y.c32(_b('a = 9.81 × 0.20 = 1.962'))[0] == 'pass'


def test_scientific_notation_is_still_left_alone():
    assert Y.c32(_b('Q = It = 2.5 × 10⁻³ × 40 = 0.10 C'))[0] == 'pass'


def test_a_miscon_item_may_name_its_register_entry():
    from jsonschema import Draft202012Validator
    v = Draft202012Validator(json.load(open(os.path.join(HERE, 'schemas', 'learning_items.schema.json'))))
    item = {'item_id': 'ITEM-X-1-001-MISCON', 'objective_ids': ['OBJ-X'], 'claim_ids': ['CLM-X'], 'item_type': 'flashcard',
            'subtype': 'MISCON', 'assessment_objectives': ['AO1'], 'difficulty': 3, 'prompt': 'x', 'canonical_answer': 'x',
            'marking_guidance': ['x'], 'context': {'sector': None, 'business_size': None, 'ownership': None, 'situation': None,
                                                   'facts': []},
            'prerequisite_item_ids': [], 'core_status': 'core', 'intentional_duplicate_group': None, 'provenance': 'x',
            'qa_status': 'review_required'}
    for k in ('misconception_entry', 'misconception_id'):
        errs = list(v.iter_errors({'dataset_id': 'x', 'topic_id': '1', 'items': [dict(item, **{k: 'MC-X-1-01'})]}))
        assert not errs, errs[0].message
