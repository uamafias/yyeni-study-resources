"""
Regression tests for the v0.2.0 check suite.

Each new check is proven twice: it must FIRE on a minimal bad build and PASS on the
same build repaired. Fixtures are synthetic and subject-neutral, so the checks are
not merely tuned to the pilot topic.
"""
import json, os, sys, shutil, tempfile
import pytest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'checks'))
from yyeni_checks import run  # noqa: E402


def _write(base, rel, obj):
    p = os.path.join(base, rel)
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, 'w') as fh:
        if rel.endswith('.json'):
            json.dump(obj, fh, indent=1)
        else:
            fh.write(obj)


def make_workspace(tmp, *, bad):
    """A two-objective topic. `bad=True` plants one defect per new check."""
    ws = os.path.join(tmp, 'ws')
    T = 'X.1'

    _write(ws, 'curriculum/objective_registry.json', {'objectives': [
        {'objective_id': 'OBJ-X.1', 'parent_id': None, 'topic_id': T, 'command_words': [], 'depth_tier': 4},
        {'objective_id': 'OBJ-X.1-01', 'parent_id': 'OBJ-X.1', 'topic_id': T,
         'command_words': ['Explain'], 'depth_tier': 2},
        {'objective_id': 'OBJ-X.1-02', 'parent_id': 'OBJ-X.1', 'topic_id': T,
         'command_words': ['Explain'], 'depth_tier': 2},
    ]})
    _write(ws, 'curriculum/assessment-framework.json', {
        'command_words': [
            {'word': 'Explain', 'used_at_level': True, 'exact_mark_tariff': '3'},
            {'word': 'Justify', 'used_at_level': False},
        ],
        'flashcard_subtype_ao_map': [{'subtype': 'DEF', 'assessment_objectives': ['AO1']}],
        'item_mix_target': {'target_share_percent': {'AO1': 100}},
    })
    _write(ws, 'assessment-evidence/assessment_evidence.json', {'status': 'partial', 'records': []})
    _write(ws, 'subject-profile.yaml',
           'variant_register:\n'
           '  - term: widget\n    variants: [round, square]\n    consequence: shape changes the outcome\n'
           'answer_structures:\n  DEF: ["meaning|precise"]\n')

    claims = [
        {'claim_id': 'C1', 'objective_ids': ['OBJ-X.1-01'], 'provenance': 'generated_gap',
         'verification': {'status': 'unverified'}, 'publishable': False,
         'text': ('A widget can be obtained only from a supplier.' if bad
                  else 'A widget is usually obtained from a supplier.')},
        {'claim_id': 'C2', 'objective_ids': ['OBJ-X.1-02'], 'provenance': 'generated_gap',
         'verification': {'status': 'unverified'}, 'publishable': False,
         'text': 'A round widget behaves differently from a square widget.'},
    ]
    _write(ws, 'topics/%s/claims/canonical_claim_ledger.json' % T, {'claims': claims})

    prose_bad = ('A widget is a component. No supplier will refuse an order. '
                 'Examiners reward this point most consistently. Every source is priced the same way.')
    prose_good = ('A widget is a component, and it may be round or square. A supplier may refuse an order '
                  'where the buyer has no record, because the supplier carries the risk of non-payment. '
                  'Round widgets and square widgets are priced differently.')
    blocks = [{'block_id': 'b1', 'block_type': 'explanation', 'heading': 'Widgets',
               'text': prose_bad if bad else prose_good, 'claim_ids': ['C1', 'C2']}]
    if not bad:
        blocks[0]['generalisation_scope'] = ['OBJ-X.1-01', 'OBJ-X.1-02']
    _write(ws, 'topics/%s/content-units/CU-X1.json' % T, {
        'unit_id': 'CU-X1', 'objective_ids': ['OBJ-X.1-01', 'OBJ-X.1-02'], 'blocks': blocks,
        'word_count': 40, 'qa_status': 'review_required'})
    _write(ws, 'topics/%s/notes-x1.md' % T, prose_bad if bad else prose_good)

    items = [
        {'item_id': 'I1', 'item_type': 'flashcard', 'subtype': 'DEF', 'assessment_objectives': ['AO1'],
         'objective_ids': ['OBJ-X.1-01', 'OBJ-X.1-02'] if bad else ['OBJ-X.1-01'],
         'claim_ids': ['C1'],
         'prompt': 'Justify the widget.' if bad else 'Explain what a widget is.',
         'canonical_answer': 'A widget is a component.',
         'marking_guidance': ['Anything goes.'] if bad else ['Precise meaning only.'],
         'qa_status': 'review_required'},
        {'item_id': 'I2', 'item_type': 'flashcard', 'subtype': 'DEF', 'assessment_objectives': ['AO1'],
         'objective_ids': ['OBJ-X.1-02'], 'claim_ids': ['C2'],
         'prompt': 'Say something.' if bad else 'Explain how a round widget differs from a square one.',
         'canonical_answer': 'They differ.',
         'marking_guidance': ['Anything.'] if bad else ['Precise meaning of each.'],
         'qa_status': 'review_required'},
    ]
    _write(ws, 'topics/%s/learning-items/items.json' % T, {'items': items})
    _write(ws, 'topics/%s/contract.json' % T, {
        'topic_id': T, 'depth_constraints': {'excluded_constructs': ['forbidden thing']}})
    return ws, T


def statuses(ws, topic):
    return {c['check_id']: c['status'] for c in run(ws, topic)['deterministic_checks']}


NEW_CHECKS = ['C-04', 'C-08', 'C-09', 'C-10', 'C-12', 'C-13', 'C-14', 'C-15', 'C-16']


@pytest.fixture(scope='module')
def results():
    tmp = tempfile.mkdtemp()
    try:
        bad_ws, t = make_workspace(os.path.join(tmp, 'bad'), bad=True)
        good_ws, _ = make_workspace(os.path.join(tmp, 'good'), bad=False)
        yield statuses(bad_ws, t), statuses(good_ws, t)
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


@pytest.mark.parametrize('cid', NEW_CHECKS)
def test_check_fires_on_bad_build(results, cid):
    bad, _ = results
    assert bad[cid] == 'fail', '%s did not fire on a build that plants its defect' % cid


@pytest.mark.parametrize('cid', NEW_CHECKS)
def test_check_clears_on_good_build(results, cid):
    _, good = results
    assert good[cid] == 'pass', '%s still fails after the defect is repaired' % cid


def test_not_run_is_never_a_pass():
    """A check whose input is absent must say not_run, and not_run must hold the release."""
    tmp = tempfile.mkdtemp()
    try:
        ws, t = make_workspace(os.path.join(tmp, 'x'), bad=False)
        os.remove(os.path.join(ws, 'subject-profile.yaml'))     # removes RS-35 and RS-38 inputs
        rep = run(ws, t)
        st = {c['check_id']: c['status'] for c in rep['deterministic_checks']}
        assert st['C-12'] == 'not_run' and st['C-16'] == 'not_run'
        assert rep['release_decision'] != 'pass'
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def test_a_raising_check_fails_rather_than_skips():
    import yyeni_checks as Y
    original = dict(Y.CHECKS[0][3].__globals__)
    tmp = tempfile.mkdtemp()
    try:
        ws, t = make_workspace(os.path.join(tmp, 'x'), bad=False)
        with open(os.path.join(ws, 'topics', t, 'learning-items', 'items.json'), 'w') as fh:
            json.dump({'items': [{'item_id': 'broken'}]}, fh)     # missing every expected field
        rep = run(ws, t)
        assert rep['release_decision'] != 'pass'
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
        del original
