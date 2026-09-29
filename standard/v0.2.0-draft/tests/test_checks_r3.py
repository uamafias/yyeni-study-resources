"""
Regression tests for the checks added after review SR-9609-5.4-CODEX-R3:
C-37 conditioned mechanisms, C-38 answer completeness, C-39 derived exposure metadata,
C-40 quantity units, and C-27's waiver mechanism.

Each is proven twice - it must FIRE on a minimal bad build and PASS on the same build
repaired - on a synthetic, subject-neutral fixture, so none of them is tuned to the
pilot subject.
"""
import json, os, shutil, sys, tempfile
import pytest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'checks'))
from yyeni_checks import run  # noqa: E402

T = 'Y.1'
NEW = ['C-37', 'C-38', 'C-39', 'C-40']


def _w(base, rel, obj):
    p = os.path.join(base, rel)
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, 'w') as fh:
        json.dump(obj, fh, indent=1) if rel.endswith('.json') else fh.write(obj)


def make(tmp, *, bad):
    ws = os.path.join(tmp, 'ws')
    _w(ws, 'curriculum/objective_registry.json', {'objectives': [
        {'objective_id': 'OBJ-Y.1', 'parent_id': None, 'topic_id': T, 'command_words': []},
        {'objective_id': 'OBJ-Y.1-01', 'parent_id': 'OBJ-Y.1', 'topic_id': T, 'command_words': ['Explain']},
    ]})
    _w(ws, 'curriculum/assessment-framework.json', {
        'command_words': [{'word': 'Explain', 'used_at_level': True, 'exact_mark_tariff': '3'}],
        'flashcard_subtype_ao_map': [{'subtype': 'DEF', 'assessment_objectives': ['AO1']}],
        'item_mix_target': {'target_share_percent': {'AO1': 100}}})
    # two evidence records: 2 parts, 2 series, max 8 marks -> probed_high by tariff
    _w(ws, 'assessment-evidence/assessment_evidence.json', {'status': 'partial', 'records': [
        {'evidence_id': 'EV-1', 'exam_series': 's21', 'mark_tariff': 8, 'command_word': 'Analyse',
         'objective_ids': ['OBJ-Y.1-01']},
        {'evidence_id': 'EV-2', 'exam_series': 's22', 'mark_tariff': 3, 'command_word': 'Explain',
         'objective_ids': ['OBJ-Y.1-01']}]})
    entry = {'objective_id': 'OBJ-Y.1-01', 'exam_exposure': 'probed_high',
             'evidence': {'question_parts_naming_it': 2, 'distinct_series': 2, 'max_mark_tariff': 8,
                          'command_words_observed': {'Analyse': 1, 'Explain': 1}, 'match_confidence': 'H'},
             'item_allocation': 1, 'required_subtypes': ['DEF'], 'review_sets': []}
    if bad:
        # C-39 defect: a superseded top-level metric kept beside the nested one, and it disagrees
        entry['question_parts_naming_it'] = 9
    _w(ws, 'curriculum/exam-exposure.json', {
        'classes': {'probed_high': 'Named in a stem and either reaching 8 marks or more or named in 5 or more '
                                   'distinct series. Gets DEF - 1 item.',
                    'probed_low': 'Named in a stem, capped at 5 marks or fewer, and named in fewer than 5 '
                                  'distinct series. 1 item.'},
        'objectives': [entry]})

    _w(ws, 'subject-profile.yaml',
       'answer_structures:\n  DEF: ["meaning|precise"]\n'
       'conditioned_mechanisms:\n'
       '  - mechanism_id: CM-TEST\n'
       '    name: Removing a shared resource\n'
       '    rationale: The conclusion holds only where the cost is unavoidable.\n'
       '    asserted_when:\n'
       "      - 'withdraw'\n"
       "      - 'shared charge'\n"
       "      - 'remains'\n"
       '    required_conditions:\n'
       '      - name: whether the charge is unavoidable\n'
       '        any_of:\n'
       "          - 'unavoidable'\n"
       "          - 'fixed by contract'\n")

    cond = '' if bad else ' The shared charge is unavoidable for the rest of the contract term.'
    _w(ws, 'topics/%s/claims/canonical_claim_ledger.json' % T, {'claims': [
        {'claim_id': 'C1', 'objective_ids': ['OBJ-Y.1-01'], 'provenance': 'generated_gap',
         'verification': {'status': 'unverified'}, 'publishable': False,
         'text': 'Where a unit is withdrawn the shared charge remains with the others.' + cond}]})
    prose = 'A unit may be withdrawn, and the shared charge remains on the rest.' + cond
    _w(ws, 'topics/%s/content-units/CU-Y1.json' % T, {
        'unit_id': 'CU-Y1', 'objective_ids': ['OBJ-Y.1-01'],
        'blocks': [{'block_id': 'b1', 'block_type': 'explanation', 'heading': 'Shared charges',
                    'text': prose, 'claim_ids': ['C1'], 'generalisation_scope': ['OBJ-Y.1-01']}],
        'word_count': 30, 'qa_status': 'review_required'})
    _w(ws, 'topics/%s/notes-y1.md' % T, prose)

    if bad:
        # C-38: the answer asserts completeness the stem never gives.
        # C-40: a currency amount named in physical units.
        prompt = 'Explain what the offer of 40 rand a crate adds, given a handling charge of 12 rand a crate.'
        answer = ('The only cost the offer causes is the 12 rand handling charge, so each crate adds 28 rand '
                  'and 50 crates of profit follow.')
    else:
        prompt = ('Explain what the offer of 40 rand a crate adds, given that the total variable cost is '
                  '12 rand a crate and the offer causes no other cost.')
        answer = ('The total cost the offer causes is the 12 rand a crate the stem gives, so each crate adds '
                  '28 rand and 50 crates add 1 400 rand of profit.')
    _w(ws, 'topics/%s/learning-items/items.json' % T, {'items': [
        {'item_id': 'I1', 'item_type': 'flashcard', 'subtype': 'DEF', 'assessment_objectives': ['AO1'],
         'objective_ids': ['OBJ-Y.1-01'], 'claim_ids': ['C1'], 'prompt': prompt,
         'canonical_answer': answer, 'marking_guidance': ['Precise meaning only.'],
         'qa_status': 'review_required'}]})
    _w(ws, 'topics/%s/contract.json' % T, {'topic_id': T,
                                           'depth_constraints': {'excluded_constructs': ['forbidden thing']}})
    return ws, T


def statuses(ws):
    return {c['check_id']: c['status'] for c in run(ws, T)['deterministic_checks']}


@pytest.fixture(scope='module')
def results():
    tmp = tempfile.mkdtemp()
    try:
        bad, _ = make(os.path.join(tmp, 'bad'), bad=True)
        good, _ = make(os.path.join(tmp, 'good'), bad=False)
        yield statuses(bad), statuses(good)
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


@pytest.mark.parametrize('cid', NEW)
def test_fires_on_bad_build(results, cid):
    bad, _ = results
    assert bad[cid] == 'fail', '%s did not fire on a build that plants its defect' % cid


@pytest.mark.parametrize('cid', NEW)
def test_clears_on_good_build(results, cid):
    _, good = results
    assert good[cid] == 'pass', '%s still fails after the defect is repaired' % cid


def test_c37_is_not_run_without_a_register():
    """No register is an honest 'nothing to enforce', never a silent pass."""
    tmp = tempfile.mkdtemp()
    try:
        ws, _ = make(os.path.join(tmp, 'x'), bad=False)
        p = os.path.join(ws, 'subject-profile.yaml')
        open(p, 'w').write('answer_structures:\n  DEF: ["meaning|precise"]\n')
        assert statuses(ws)['C-37'] == 'not_run'
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def test_c27_waiver_needs_a_written_reason():
    """A waiver is a justification, not a switch: a token reason fails the check."""
    tmp = tempfile.mkdtemp()
    try:
        ws, _ = make(os.path.join(tmp, 'x'), bad=False)
        ip = os.path.join(ws, 'topics', T, 'learning-items', 'items.json')
        d = json.load(open(ip))
        d['items'][0]['subtype'] = 'WHY'                 # the required DEF card is now absent
        d['items'][0]['assessment_objectives'] = ['AO1']
        json.dump(d, open(ip, 'w'))
        assert statuses(ws)['C-27'] == 'fail'            # missing and unwaived

        cp = os.path.join(ws, 'topics', T, 'contract.json')
        c = json.load(open(cp))
        c['subtype_waivers'] = [{'objective_id': 'OBJ-Y.1-01', 'subtype': 'DEF', 'reason': 'not needed'}]
        json.dump(c, open(cp, 'w'))
        assert statuses(ws)['C-27'] == 'fail'            # waived, but with no usable reason

        c['subtype_waivers'][0]['reason'] = ('The definable term belongs to the parent objective and is '
                                             'already practised there, so a second definition card would '
                                             'duplicate it without adding anything.')
        json.dump(c, open(cp, 'w'))
        assert statuses(ws)['C-27'] == 'pass'
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


# --- checks added after review SR-9609-5.4-CODEX-R4 ---------------------------------

CHART = {'price': 80, 'variable_cost': 40, 'fixed_costs': 160000, 'current_output': 6000, 'asks': 'break-even'}


def _with_chart(tmp, *, authored):
    """A build whose item shows a chart. `authored=True` plants a hand-drawn plot."""
    ws, _ = make(os.path.join(tmp, 'c'), bad=False)
    sys.path.insert(0, os.path.join(ROOT, 'build'))
    from render_chart import render_break_even
    plot, _f = render_break_even(CHART)
    if authored:
        plot = plot.replace('X', '.')          # one character wrong is still not the generated picture
    ip = os.path.join(ws, 'topics', T, 'learning-items', 'items.json')
    d = json.load(open(ip))
    d['items'][0]['prompt'] = 'Explain what the chart shows.\n\n' + plot
    d['items'][0]['context'] = {'chart': dict(CHART)}
    json.dump(d, open(ip, 'w'))
    return ws


def test_c41_fires_on_an_authored_depiction():
    tmp = tempfile.mkdtemp()
    try:
        assert statuses(_with_chart(tmp, authored=True))['C-41'] == 'fail'
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def test_c41_clears_on_a_generated_depiction():
    tmp = tempfile.mkdtemp()
    try:
        assert statuses(_with_chart(tmp, authored=False))['C-41'] == 'pass'
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def test_c41_fires_when_a_plot_declares_no_chart():
    """A picture with nothing to regenerate it from cannot be verified, so it fails rather than passes."""
    tmp = tempfile.mkdtemp()
    try:
        ws = _with_chart(tmp, authored=False)
        ip = os.path.join(ws, 'topics', T, 'learning-items', 'items.json')
        d = json.load(open(ip))
        d['items'][0]['context'] = {}
        json.dump(d, open(ip, 'w'))
        assert statuses(ws)['C-41'] == 'fail'
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def test_c42_fires_when_the_contract_outgrows_the_build():
    tmp = tempfile.mkdtemp()
    try:
        ws, _ = make(os.path.join(tmp, 'x'), bad=False)
        cp = os.path.join(ws, 'topics', T, 'contract.json')
        c = json.load(open(cp))
        c['depth_constraints']['item_budget'] = 92          # the build has 1
        json.dump(c, open(cp, 'w'))
        assert statuses(ws)['C-42'] == 'fail'
        c['depth_constraints']['item_budget'] = 1
        json.dump(c, open(cp, 'w'))
        assert statuses(ws)['C-42'] == 'pass'
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def test_the_renderer_puts_the_lines_where_the_data_says():
    """The geometry itself, not only the metadata: R4-001 was a chart whose lines never crossed."""
    sys.path.insert(0, os.path.join(ROOT, 'build'))
    from render_chart import render_break_even
    plot, f = render_break_even(CHART)
    assert f['break_even_output'] == 4000 and f['break_even_value'] == 320000
    body = [l for l in plot.splitlines() if l.startswith(('  ', '    ')) and '|' in l]
    xs = [l for l in body if 'X' in l]
    assert len(xs) == 1, 'the intersection must appear exactly once'
    row = xs[0]
    assert row.lstrip().startswith('320'), 'the intersection must sit on the N$320 000 gridline'
    # revenue starts at the origin and total cost starts at the fixed-cost level
    assert body[-1].split('|')[1].startswith('*'), 'TR must leave the origin'
    assert '+' in body[0].split('|')[1] or '*' in body[0].split('|')[1]
