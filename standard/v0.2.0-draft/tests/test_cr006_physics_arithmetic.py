"""CR-006 (2026-09-29), physics. C-32 recomputes a stated product or quotient written with the typeset signs
(x and / already were); scientific notation and chained working are left alone; a multiple-choice set is a
learning-item type, because a qualification with a multiple-choice paper plans one per topic."""
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


def test_a_typeset_product_is_checked():
    assert Y.c32(_b('W = mg = 1.2 kg and 1.2 × 9.81 = 11.8 N'))[0] == 'pass'
    assert Y.c32(_b('1.2 × 9.81 = 13.8 N'))[0] == 'fail'


def test_a_typeset_quotient_is_checked():
    assert Y.c32(_b('R = V / I, so 6.0 ÷ 0.25 = 24 Ω'))[0] == 'pass'
    assert Y.c32(_b('6.0 ÷ 0.25 = 1.5 Ω'))[0] == 'fail'


def test_rounding_inside_the_equality_is_caught():
    # 9.81 x 1.2 is 11.772; writing "= 12" inside the equality states something false, which is why the
    # handover asks for three significant figures in working and rounding only in the final line
    assert Y.c32(_b('9.81 × 1.2 = 12'))[0] == 'fail'
    assert Y.c32(_b('9.81 × 1.2 = 11.8, so the weight is 12 N to two significant figures'))[0] == 'pass'


def test_scientific_notation_is_not_read_as_arithmetic():
    assert Y.c32(_b('Q = It = 2.5 × 10⁻³ × 40 = 0.10 C'))[0] == 'pass'
    assert Y.c32(_b('c = 3.0 × 10⁸ m s⁻¹'))[0] == 'pass'


def test_a_multiple_choice_set_is_a_learning_item_type():
    s = json.load(open(os.path.join(HERE, 'schemas', 'learning_items.schema.json')))
    enum = s['properties']['items']['items']['properties']['item_type']['enum']
    assert 'multiple_choice_set' in enum and 'practical_task' in enum
