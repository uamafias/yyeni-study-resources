"""CR-006 (2026-09-29). C-32 checks binary arithmetic in base 2 and fixed-width results modulo their width;
C-35 and C-41 read the subject's chart model, so pseudocode in a labelled fence is code, not a chart."""
import os
import sys
import types

sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'checks'))
import yyeni_checks as Y  # noqa: E402


def _items(*answers, prompt='Add the numbers.', subtype='CALC', ctx=None):
    return [{'item_id': 'I%d' % n, 'item_type': 'flashcard', 'subtype': subtype, 'prompt': prompt,
             'canonical_answer': a, 'marking_guidance': [], 'context': ctx or {}} for n, a in enumerate(answers)]


def _b(items, profile=None, units=()):
    return types.SimpleNamespace(items=items, profile=profile, units=list(units))


NONE = {'depictions': {'chart_model': 'none', 'code_fence_languages': ['pseudocode', 'sql']}}
CODE = 'Trace this:\n```pseudocode\nCount <- 0\nWHILE NOT EOF("A.txt")\n   Count <- Count + 1\nENDWHILE\n```'


def test_a_correct_binary_sum_passes():
    assert Y.c32(_b(_items('0011 0110 + 0001 1011 = 0101 0001.')))[0] == 'pass'


def test_a_wrong_binary_sum_fails():
    status, msg, _ = Y.c32(_b(_items('0011 0110 + 0001 1011 = 0101 0011')))
    assert status == 'fail' and 'binary' in msg


def test_a_fixed_width_result_is_checked_modulo_its_width():
    # 20 + (-10) in 8-bit two's complement: the carry out of the register is discarded
    assert Y.c32(_b(_items('0001 0100 + 1111 0110 = 0000 1010')))[0] == 'pass'


def test_denary_arithmetic_is_unchanged():
    assert Y.c32(_b(_items('1024 x 8 = 8192')))[0] == 'pass'
    assert Y.c32(_b(_items('1024 x 8 = 8000')))[0] == 'fail'


def test_a_labelled_code_fence_is_not_a_chart():
    it = _items('Count ends at 3.', prompt=CODE, subtype='INTERP')
    assert Y.c35(_b(it, NONE))[0] != 'fail'
    assert Y.c41(_b(it, NONE))[0] != 'fail'


def test_a_hand_drawn_plot_still_fails_where_there_is_no_renderer():
    it = _items('It rises.', prompt='The graph:\n```\n 10 |    *\n  5 |  *\n  0 |*\n```', subtype='INTERP')
    status, msg, _ = Y.c41(_b(it, NONE))
    assert status == 'fail' and 'table' in msg


def test_the_break_even_model_is_unchanged_without_a_profile_key():
    it = _items('Break-even is 4 000 units.', prompt='The chart:\n```\n x \n```', subtype='INTERP')
    assert Y.c35(_b(it, {}))[0] == 'fail'
