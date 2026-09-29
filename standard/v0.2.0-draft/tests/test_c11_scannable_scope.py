"""C-11 / RS-15 after CR-004 (2026-09-29). An excluded construct is a term or a declared pattern, and an
entry C-11 cannot scan is a failure, never a silent pass."""
import os
import sys
import types

sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'checks'))
import yyeni_checks as Y  # noqa: E402

PED = {'construct': 'the PED formula', 'pattern': r'\bPED\s*=|(?:percentage|%) change in quantity demanded\s*(?:/|divided by)',
       'source': 'syllabus, page 18'}
MR = {'construct': 'marginal revenue', 'pattern': r'\bmarginal revenue\b|(?-i:\bMR\b)', 'source': 'syllabus, page 18'}


def _b(entries, text):
    b = types.SimpleNamespace(contract={'depth_constraints': {'excluded_constructs': entries}})
    b.learner_text = lambda: [('CU-1', 'b1', text)]
    b.answer_text = lambda: []
    return b


def test_a_declared_pattern_catches_teaching_past_the_limit():
    assert Y.c11(_b([PED], 'PED = % change in quantity demanded divided by % change in price.'))[0] == 'fail'


def test_a_declared_pattern_leaves_in_scope_teaching_alone():
    assert Y.c11(_b([PED], 'Price elastic demand means customers respond strongly to a price change.'))[0] == 'pass'


def test_a_case_sensitive_island_does_not_fire_on_mr_as_a_title():
    assert Y.c11(_b([MR], 'Mr Shikongo runs a small firm.'))[0] == 'pass'
    assert Y.c11(_b([MR], 'Output rises until MR equals zero.'))[0] == 'fail'


def test_a_sentence_entry_fails_instead_of_passing_without_looking():
    old = ['Knowledge of the formula and calculations of PED will not be assessed.  [stated in the syllabus]']
    status, msg, _ = Y.c11(_b(old, 'PED = % change in quantity demanded / % change in price'))
    assert status == 'fail' and 'not terms' in msg


def test_an_adjacent_topic_label_in_the_list_fails():
    assert Y.c11(_b(['Marketing mix \u2014 taught in topic 3.3  [adjacent topic]'], 'anything'))[0] == 'fail'


def test_plain_terms_still_work_as_before():
    assert Y.c11(_b(['activity-based costing'], 'Activity-based costing assigns overheads.'))[0] == 'fail'
    assert Y.c11(_b(['activity-based costing'], 'Full costing spreads overheads.'))[0] == 'pass'


def test_a_pattern_that_does_not_compile_fails():
    assert Y.c11(_b([{'construct': 'broken', 'pattern': '(unclosed'}], 'text'))[0] == 'fail'
