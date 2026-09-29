#!/usr/bin/env python3
"""Compute a topic's work order: every slot decided before an author writes a word.

    python3 make_work_order.py <workspace> <topic-id> [--all]

Why this exists. Seventeen topics of 9609 AS were authored in one evening by seventeen
*frontier* authors following one brief. Each made a different judgement call: how many
content units, how to tag AOs on flexible subtypes, whether to invent excluded_constructs,
how to treat a decomposed container. The brief asked for judgement and got seventeen answers.

An open-weights model will write prose about as well and judge considerably worse. So the
judgement is moved out of the prompt and into this script, which derives every decision from
data the build already holds - the registry, the framework, the exposure map and the contract.
The author then fills slots. That is a much smaller thing to ask of a model, and it is the
same thing every time.

Output: topics/<t>/work_order.json (the machine copy the author reads) and work_order.md
(the same plan, readable). Neither is learner-facing; both are regenerated, never edited.
"""
import argparse
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from naming import notes_filename, flashcards_filename, topic_label  # noqa: E402

# The command word a card instructs with follows the SHAPE of the answer it wants, narrowed to
# the words this objective actually carries and this level actually uses. Listed best-first.
CW_BY_SUBTYPE = {
    'DEF': ['Define', 'Identify'], 'FEATURE': ['Identify', 'Explain'], 'DIST': ['Explain', 'Define'],
    'PROC': ['Explain', 'Identify'], 'WHY': ['Explain'], 'MISCON': ['Explain'],
    'CALC': ['Calculate'], 'APP': ['Explain', 'Calculate'], 'INTERP': ['Explain', 'Calculate'],
    'MECH': ['Analyse', 'Explain'], 'CHAIN': ['Analyse', 'Explain'],
    'BEN': ['Analyse', 'Explain'], 'LIM': ['Analyse', 'Explain'],
    'EVAL': ['Evaluate'], 'SYNTH': ['Evaluate', 'Analyse'],
}


# ---------------------------------------------------------------- the encoded judgement
#
# Which subtypes an objective needs, by what KIND of objective it is. This table is the
# judgement that was previously left to each author. It is written down once, here, so every
# topic in every subject answers it the same way.
BY_TYPE = {
    'business_concept':                 ['DEF', 'WHY'],
    'business_comparison':              ['DEF', 'DIST'],
    'business_process':                 ['DEF', 'PROC'],
    'business_theory_model':            ['DEF', 'FEATURE'],
    'business_method_strategy':         ['DEF', 'BEN', 'LIM'],
    'business_relationship_impact':     ['DEF', 'CHAIN'],
    'business_quantitative_measure':    ['DEF', 'CALC', 'INTERP'],
    'business_case_data_interpretation': ['INTERP', 'APP'],
    'business_decision_evaluation':     ['DEF', 'EVAL'],
}
DEFAULT_TYPE = ['DEF', 'WHY']

# Depth tier decides how far past recall an objective is taken. Tier 1 is a term to know;
# tier 4 is a container the whole topic hangs off.
BY_TYPE.update({
    # Cambridge IGCSE Economics 0455. A diagram objective earns a DIAGRAM slot
    # because 'Draw' is a live 4-mark command word on Paper 2, marked as four
    # discrete elements; a cause/effect objective earns CHAIN because that is
    # the shape 'Analyse' is marked in.
    'economics_concept':           ['DEF', 'WHY'],
    'economics_definition':        ['DEF', 'FEATURE'],
    'economics_comparison':        ['DEF', 'DIST'],
    'economics_classification':    ['DEF', 'FEATURE'],
    'economics_mechanism':         ['DEF', 'MECH'],
    'economics_cause_effect':      ['DEF', 'CHAIN'],
    'economics_diagram':           ['DEF', 'DIAGRAM', 'INTERP'],
    'economics_quantitative':      ['DEF', 'CALC', 'INTERP'],
    'economics_policy_evaluation': ['DEF', 'BEN', 'LIM', 'EVAL'],
})

BY_TIER = {1: [], 2: ['APP'], 3: ['APP', 'CHAIN'], 4: ['APP', 'CHAIN', 'EVAL']}

# An objective examined at 8 marks or more has been asked to carry an argument, whatever its
# tier, so it gets evaluation practice.
HIGH_TARIFF_ADDS = ['EVAL']

# Notional mark value and AO split of each performance task, taken from the paper structure the
# framework verified against real papers. These are what the task is WORTH in exam terms, which is
# how the syllabus states its AO weights.
PERF_MARKS_BY_ROLE = {
    'short_answer':  (5,  {'knowledge': 2, 'analysis': 3}),
    'data_response': (30, {'knowledge': 9, 'application': 9, 'analysis': 6, 'evaluation': 6}),
    'essay_plan':    (20, {'analysis': 8, 'evaluation': 12}),
    'case_analysis': (20, {'application': 6, 'analysis': 6, 'evaluation': 8})}

PERFORMANCE = [('short_answer', 'A lender/manager-style question requiring several linked points'),
               ('data_response', 'A short case with figures, answered under AO2 and AO4'),
               ('essay_plan', 'A planned 12-mark evaluation, structured not written out'),
               ('case_analysis', 'An unfamiliar business, analysed then judged')]


def _json(p):
    with open(p) as fh:
        return json.load(fh)


def _yaml(p):
    import yaml
    with open(p) as fh:
        return yaml.safe_load(fh)


# --- assessment objectives are per-qualification, not universal -------------
# 0450 has four (Knowledge, Application, Analysis, Evaluation); 0455 has three
# (Knowledge, Analysis, Evaluation) and no Application objective at all. Every
# AO-shaped calculation below reads the codes off the framework.
AO_CODES = ['AO1', 'AO2', 'AO3', 'AO4']
AO_ROLE = {}          # role -> code, e.g. {'evaluation': 'AO3'} for 0455
MCQ_PAPER = None      # set when the qualification has a multiple-choice component
N_TOPICS = None
MCQ_N = 0             # sized per topic so MCQ practice carries the paper's own share

_ROLE_WORDS = [('knowledge', 'knowledge'), ('application', 'application'),
               ('analysis', 'analysis'), ('evaluation', 'evaluation')]


def set_ao_codes(framework):
    """Read the AO codes and their roles from the framework.

    The role matters because an AO's NUMBER means different things in different
    subjects: 0450's AO3 is Analysis, 0455's AO3 is Evaluation. Anything that
    reasons about what an objective tests must go through the role.
    """
    global AO_CODES, AO_ROLE
    aos = framework.get('assessment_objectives') or []
    if not aos:
        return
    AO_CODES = [a['code'] for a in aos]
    AO_ROLE = {}
    for a in aos:
        name = (a.get('name') or '').lower()
        for word, role in _ROLE_WORDS:
            if word in name:
                AO_ROLE[role] = a['code']
                break
    # A subject with no Application objective assesses application inside its
    # analysis objective; 0455 says so in the AO2 wording itself.
    if 'application' not in AO_ROLE and 'analysis' in AO_ROLE:
        AO_ROLE['application'] = AO_ROLE['analysis']
    if 'evaluation' not in AO_ROLE and AO_CODES:
        AO_ROLE['evaluation'] = AO_CODES[-1]


def set_mcq(framework):
    """Detect a multiple-choice component and remember its marks and AO split.

    0455 carries 30 of its 120 marks as multiple choice, weighted AO1 50 / AO2 50.
    A bank made only of structured-question cards cannot reach the qualification's
    AO1 share, because AO1 marks arrive in twos on Paper 2 and in thirties on
    Paper 1. The fix is to plan MCQ practice, not to pad the bank with definitions.
    """
    global MCQ_PAPER
    MCQ_PAPER = None
    for pp in framework.get('papers') or []:
        if 'multiple choice' in (pp.get('name') or '').lower():
            tot = sum(x.get('marks', 0) for x in framework.get('papers') or []) or 1
            # the paper's STATED weight, not its share of the marks: 0455 weights its
            # 30-mark multiple-choice paper at 30% of 120 marks, not 25%
            share = (pp['weight_percent'] / 100.0 if pp.get('weight_percent')
                     else pp.get('marks', 30) / float(tot))
            MCQ_PAPER = {'marks': pp.get('marks', 30), 'ao_split': pp.get('ao_split', {}),
                         'total': tot, 'share': share}
            return


def size_mcq(slot_marks, n_topics=None):
    """How many multiple-choice questions this topic's set holds.

    Grounded in the paper, not in the AO arithmetic. A multiple-choice paper asks
    one-mark questions across the whole syllabus - 0455 Paper 1 is 30 of them
    over 39 topics. A learner who works through TEN papers' worth of such
    questions has met each topic about ten times its share of one paper, so a
    topic's set is 10 x (questions per paper / topics), held between 4 and 12.

    An earlier version sized the set so MCQ marks equalled the paper's weight of
    all practice marks. Because an MCQ is worth one mark and a structured card
    two to eight, that asked for 59 questions per topic. The AO balance is the
    subject total's job, not something to buy with volume.
    """
    global MCQ_N
    if not MCQ_PAPER:
        MCQ_N = 0
        return 0
    per_paper = MCQ_PAPER['marks']            # one mark per multiple-choice question
    n = n_topics or 1
    MCQ_N = int(max(4, min(12, round(10.0 * per_paper / n))))
    return MCQ_N


PERF_OVERRIDE = None   # set per build from subject-profile.yaml slot_plan.performance_tasks (CR-006)


def performance_items():
    """The performance tasks this qualification needs, including an MCQ set where
    the qualification actually examines by multiple choice."""
    if PERF_OVERRIDE is not None:
        out = []
        for t in PERF_OVERRIDE:
            brief = t['brief']
            if t['item_type'] == 'multiple_choice_set':
                if not (MCQ_PAPER and MCQ_N):
                    continue
                brief = brief.replace('{n}', str(MCQ_N))
            out.append((t['item_type'], brief))
        return out
    items = list(PERFORMANCE)
    if MCQ_PAPER and MCQ_N:
        items.insert(0, ('multiple_choice_set',
                         'A set of %d four-option multiple-choice questions on this topic, one '
                         'mark each, every distractor explained on the back. This models the '
                         'qualification\u2019s multiple-choice paper, which carries %d of its '
                         '%d marks \u2014 %d%% of the whole examination.'
                         % (MCQ_N, MCQ_PAPER['marks'], MCQ_PAPER['total'],
                            round(100 * MCQ_PAPER['share']))))
    return items


def perf_split(kind):
    """Mark split for one performance task, in this subject's AO codes."""
    if PERF_OVERRIDE is not None and kind != 'multiple_choice_set':
        t = next((x for x in PERF_OVERRIDE if x['item_type'] == kind), None)
        return dict(t.get('ao_split') or {}) if t else {}
    if kind == 'multiple_choice_set' and MCQ_PAPER:
        return {a: MCQ_N * v / 100.0 for a, v in MCQ_PAPER['ao_split'].items() if v}
    _, split = PERF_MARKS_BY_ROLE.get(kind, (0, {}))
    return by_role(split)


def role(name):
    """The AO code that carries this role in the subject being built."""
    return AO_ROLE.get(name) or (AO_CODES[-1] if AO_CODES else 'AO1')


def by_role(split):
    """{'knowledge': 9, 'evaluation': 6} -> {'AO1': 9, 'AO3': 6}, merging roles
    that share a code in this subject."""
    out = {}
    for r, v in split.items():
        out[role(r)] = out.get(role(r), 0) + v
    return out


def tariff_marks(t):
    """'5 or 8' -> 5. The conservative reading of a range; stated where it is used."""
    if t is None:
        return 0
    if isinstance(t, (int, float)):
        return int(t)
    nums = [int(x) for x in str(t).replace('or', ' ').split() if x.isdigit()]
    return min(nums) if nums else 0


def ao_marks(slots, perf):
    """AO shares in MARKS-EQUIVALENT, which is the measure the syllabus itself uses.

    A card's tariff is the marks the question it models would carry; those marks are split evenly
    across the AOs the card declares. Performance tasks carry the mark split of the paper part they
    model. This is an estimate, but it is an estimate of the right quantity - an item count is not.
    """
    from collections import Counter
    m = Counter()
    for s_ in slots:
        t = tariff_marks(s_.get('mark_tariff'))
        aos = s_.get('assessment_objectives') or ['AO1']
        for a in aos:
            m[a] += t / len(aos)
    for p_ in perf:
        split = perf_split(p_['item_type'])
        for a, v in split.items():
            m[a] += v
    tot = sum(m.values()) or 1
    return {a: round(100 * m.get(a, 0) / tot) for a in AO_CODES}, round(tot)


def sub_topic(oid):
    """OBJ-9609-2.1.3-01 -> '2.1.3'. The sub-topic decides the content-unit split."""
    core = oid.split('-')[2] if oid.count('-') >= 2 else oid
    return core.split('.')[0] + '.' + '.'.join(core.split('.')[1:3]) if core.count('.') >= 2 else core


def build(ws, topic):
    td = os.path.join(ws, 'topics', topic)
    contract = _json(os.path.join(td, 'contract.json'))
    registry = _json(os.path.join(ws, 'curriculum', 'objective_registry.json'))['objectives']
    framework = _json(os.path.join(ws, 'curriculum', 'assessment-framework.json'))
    set_ao_codes(framework)
    set_mcq(framework)
    global N_TOPICS
    N_TOPICS = len([d for d in os.listdir(os.path.join(ws, 'topics'))
                    if os.path.isfile(os.path.join(ws, 'topics', d, 'contract.json'))])
    exposure = {o['objective_id']: o for o in
                _json(os.path.join(ws, 'curriculum', 'exam-exposure.json'))['objectives']}
    profile = None
    for cand in ('subject-profile.yaml', 'subject_profile.yaml'):
        p = os.path.join(ws, cand)
        if os.path.exists(p):
            profile = _yaml(p)
            break
    structures = (profile or {}).get('answer_structures', {})
    # CR-006: a subject may declare its own slot plan in subject-profile.yaml. Absent, the defaults below
    # apply unchanged, so every subject planned before CR-006 regenerates byte-identical.
    sp = (profile or {}).get('slot_plan') or {}
    by_type = dict(BY_TYPE)
    by_type.update(sp.get('subtypes_by_objective_type') or {})
    by_tier = ({int(k): v for k, v in sp['subtypes_by_tier'].items()} if sp.get('subtypes_by_tier') else BY_TIER)
    cw_by_sub = sp.get('command_words_by_subtype') or CW_BY_SUBTYPE
    high_t = (sp.get('high_tariff') or {}).get('threshold', 8)
    high_adds = (sp.get('high_tariff') or {}).get('adds', HIGH_TARIFF_ADDS)
    t_over = sp.get('tariff_overrides') or {}
    ao_by_type = sp.get('ao_by_objective_type') or {}
    ao_by_paper = sp.get('ao_by_paper') or {}
    ao_by_paper_subtype = sp.get('ao_by_paper_subtype') or {}
    global PERF_OVERRIDE
    PERF_OVERRIDE = None
    ao_map = {s['subtype']: s['assessment_objectives']
              for s in framework.get('flashcard_subtype_ao_map', [])}
    bloom_map = {s['subtype']: s.get('blooms_level')
                 for s in framework.get('flashcard_subtype_ao_map', [])}
    bloom_perf = (framework.get('blooms_taxonomy') or {}).get('by_performance_task', {})

    def bloom(st, o=None):
        """The cognitive demand of this slot.

        The subtype sets it. A tier-4 objective lifts a middling subtype one
        level, because the same subtype on a topic the syllabus expects a
        judgement about really is asking more of the learner."""
        ladder = ['Remember', 'Understand', 'Apply', 'Analyse', 'Evaluate', 'Create']
        b = bloom_map.get(st) or 'Understand'
        if o and (o.get('depth_tier') or 1) >= 4 and b in ('Remember', 'Understand'):
            b = ladder[min(len(ladder) - 1, ladder.index(b) + 1)]
        return b
    tariffs = {c['word']: c.get('exact_mark_tariff') for c in framework.get('command_words', [])
               if c.get('exact_mark_tariff') is not None or c.get('used_at_level')}
    in_use = [c['word'] for c in framework.get('command_words', [])
              if c.get('exact_mark_tariff') is not None or c.get('used_at_level')]

    def by_ao(subtype):
        """Fall back to the in-use command word that serves this subtype's assessment objective at
        the highest tariff. 9609 words a 12-mark judgement 'Evaluate'; 0450 words it 'Consider'.
        Reading it off the framework means neither is hardcoded."""
        want = set(ao_map.get(subtype) or [])
        if cw_by_sub is not CW_BY_SUBTYPE:
            # a subject that declares its words per subtype never falls back to a word it did not list
            listed = [w for w in cw_by_sub.get(subtype, []) if w in in_use]
            if listed:
                return listed[0]
        best, best_marks = None, -1
        for c in framework.get('command_words', []):
            if c['word'] not in in_use:
                continue
            if not want & set(c.get('primary_assessment_objectives') or []):
                continue
            m = tariff_marks(c.get('exact_mark_tariff'))
            if m > best_marks:
                best, best_marks = c['word'], m
        return best

    branch = [o for o in registry if o.get('topic_id') == topic and o.get('parent_id')]
    branch.sort(key=lambda o: o['objective_id'])
    if not branch:
        raise SystemExit('No assessable objectives for topic %s' % topic)
    topic_papers = sorted({p for o in branch for p in (o.get('papers') or [])})
    if sp.get('performance_tasks') is not None:
        PERF_OVERRIDE = [t for t in sp['performance_tasks']
                         if not t.get('papers') or set(t['papers']) & set(topic_papers)]
    # CR-006: a topic's paper key is its papers joined with '+' ('2' for one paper, '1+2' for a topic
    # examined on two papers that assess the same AOs); single-paper behaviour is unchanged.
    pkey = '+'.join(topic_papers)
    remap = ao_by_paper.get(pkey, {})

    def slot_aos(st, o, default):
        """The AOs a slot declares: the subtype's permitted set, narrowed by objective type where the
        profile says so, then re-expressed for the one paper this topic is examined on (a paper that
        assesses no AO1 credits recall of its content as application)."""
        a = list((ao_by_type.get(o.get('objective_type')) or {}).get(st)
                 or (ao_by_type.get('*') or {}).get(st) or ao_map.get(st) or default)
        if (ao_by_paper_subtype.get(pkey) or {}).get(st):
            a = list(ao_by_paper_subtype[pkey][st])
        a = [remap.get(x, x) for x in a]
        return [x for i, x in enumerate(a) if x not in a[:i]]

    def slot_tariff(st, cw):
        if not cw:
            return None
        if '%s:%s' % (st, cw) in t_over:
            return t_over['%s:%s' % (st, cw)]
        if cw in t_over:
            return t_over[cw]
        return tariffs.get(cw)

    # ---- content units: one per sub-topic, never one per objective
    units, order = {}, []
    for o in branch:
        st = sub_topic(o['objective_id'])
        if st not in units:
            units[st] = []
            order.append(st)
        units[st].append(o)
    subject = branch[0]['objective_id'].split('-')[1]
    unit_plan = []
    total = len(branch)
    lo, hi = (contract.get('depth_constraints', {}).get('word_budget') or {}).get('min', 0), \
             (contract.get('depth_constraints', {}).get('word_budget') or {}).get('max', 0)
    for st in order:
        objs = units[st]
        share = len(objs) / total
        unit_plan.append({
            'unit_id': 'CU-%s-%s' % (subject, st),
            'file': 'content-units/CU-%s-%s.json' % (subject, st),
            'sub_topic': st,
            'objective_ids': [o['objective_id'] for o in objs],
            'objectives': [{'objective_id': o['objective_id'],
                            'title': o.get('learner_objective') or o.get('syllabus_text'),
                            'syllabus_text': o.get('syllabus_text'),
                            'depth_tier': o.get('depth_tier')} for o in objs],
            'word_budget': [int(lo * share), int(hi * share)] if hi else None,
            'blocks_required': ['a definition or plain explanation block for every objective above',
                                'at least one worked example or analysis chain where the objectives '
                                'are tier 2 or higher',
                                'a cross-link block naming the topics this one connects to'],
        })

    # ---- item plan: one fully decided slot at a time
    slots, n = [], 0
    for o in branch:
        oid = o['objective_id']
        exp = exposure.get(oid) or {}
        ev = exp.get('evidence') or {}
        max_tariff = ev.get('max_mark_tariff') or 0
        want = list(by_type.get(o.get('objective_type'), DEFAULT_TYPE))
        for s in by_tier.get(o.get('depth_tier') or 1, []):
            if s not in want:
                want.append(s)
        if max_tariff >= high_t:
            for s in high_adds:
                if s not in want:
                    want.append(s)
        for s in (exp.get('required_subtypes') or []):      # the exposure floor
            if s not in want:
                want.append(s)
        waived = {w['subtype'] for w in (contract.get('subtype_waivers') or [])
                  if w.get('objective_id') == oid}
        want = [s for s in want if s not in waived]

        cws = o.get('command_words') or []
        for idx, st in enumerate(want):
            n += 1
            # the word must suit the subtype, be one this objective carries, and be used at level
            cw = next((w for w in cw_by_sub.get(st, []) if w in cws and w in in_use), None)
            if cw is None:
                cw = next((w for w in cw_by_sub.get(st, []) if w in in_use), None)
            if cw is None:
                cw = by_ao(st)          # this subject words it differently; go by what it tests
            slots.append({
                'slot': 'ITEM-%s-%s-%03d-%s' % (subject, topic, n, st),
                'objective_id': oid,
                'objective_title': o.get('learner_objective') or o.get('syllabus_text'),
                'syllabus_text': o.get('syllabus_text'),
                'subtype': st,
                'assessment_objectives': slot_aos(st, o, ['AO1']),
                'command_word': cw,
                'mark_tariff': slot_tariff(st, cw),
                'difficulty': min(5, max(1, (o.get('depth_tier') or 1) + (2 if st in
                                  ('EVAL', 'CHAIN', 'SYNTH') else 0))),
                'blooms_level': bloom(st, o),
                'marking_guidance_must_name': structures.get(st, []),
                'reason': ('instructs with %s, which this objective carries' % cw
                           if cw and cw in cws else
                           'instructs with %s, the shape this subtype needs' % cw if cw else
                           'required by exposure class' if st in (exp.get('required_subtypes') or [])
                           else 'objective type %s, depth tier %s'
                           % (o.get('objective_type'), o.get('depth_tier'))),
            })

    # ---- CR-006: one MISCON slot per examiner-evidenced misconception, on the objective it concerns, naming
    # the register entry it discriminates. Without this a MISCON slot is a guess at which confusion to drill.
    if sp.get('misconception_slots') == 'one_per_entry':
        mp = os.path.join(ws, 'curriculum', 'misconceptions.json')
        entries = [e for e in (_json(mp).get('entries') if os.path.exists(mp) else [])
                   if e.get('topic_id') == topic and e.get('objective_id')]
        by_id = {o['objective_id']: o for o in branch}
        for e in entries:
            o = by_id.get(e['objective_id'])
            if o is None:
                continue
            n += 1
            cw = next((w for w in cw_by_sub.get('MISCON', []) if w in in_use), None)
            slots.append({
                'slot': 'ITEM-%s-%s-%03d-%s' % (subject, topic, n, 'MISCON'),
                'objective_id': o['objective_id'],
                'objective_title': o.get('learner_objective') or o.get('syllabus_text'),
                'syllabus_text': o.get('syllabus_text'),
                'subtype': 'MISCON', 'assessment_objectives': slot_aos('MISCON', o, ['AO1']),
                'command_word': cw, 'mark_tariff': slot_tariff('MISCON', cw),
                'difficulty': min(5, (o.get('depth_tier') or 1) + 1),
                'blooms_level': bloom('MISCON', o),
                'marking_guidance_must_name': structures.get('MISCON', []),
                'misconception_entry': e.get('entry_id'),
                'reason': 'discriminates misconception %s (%d examiner statements): %s'
                          % (e.get('entry_id'), e.get('n', 0), e.get('a', ''))[:240],
            })

    # ---- balance the plan against the framework's AO targets. Every objective needs a recall
    # anchor, so an unbalanced plan is always AO1-heavy; the authors of the first subject all
    # noticed this and each fixed it differently. Fixing it here makes it the same every time.
    from collections import Counter as _C

    def _share(sl, ao):
        return ao_marks(sl, PERFORMANCE_STUB)[0].get(ao, 0)

    size_mcq(sum(tariff_marks(x.get('mark_tariff')) for x in slots), N_TOPICS)
    PERFORMANCE_STUB = [{'item_type': k} for k, _ in performance_items()]
    # The syllabus's own stated AO weights are the target, not a derived item-mix heuristic.
    targets = ((framework.get('ao_mark_budget') or {}).get('stated_qualification_weight_percent')
               or framework.get('item_mix_target', {}).get('target_share_percent', {}))
    # CR-006: where each topic is examined on one paper and the papers split the AOs differently, a topic
    # is balanced against its own paper's split; the subject total still answers to the syllabus weights.
    tbp = sp.get('topic_targets_by_paper') or {}
    if tbp.get(pkey):
        targets = tbp[pkey]
    TOP_UP = [(role('evaluation'), 'EVAL', None, 4), (role('analysis'), 'CHAIN', None, 4),
              (role('application'), 'APP', None, 4), (role('knowledge'), 'DEF', None, 4),
              (role('knowledge'), 'FEATURE', None, 4), (role('knowledge'), 'MISCON', None, 4),
              (role('knowledge'), 'DIST', None, 4)]
    if sp.get('top_up') is not None:
        TOP_UP = [(remap.get(a, a), st_, None, 4) for a, st_ in sp['top_up']]
    for ao, st, word, tol in TOP_UP:
        want = targets.get(ao)
        if not want:
            continue
        word = word or by_ao(st)                 # the word this subject uses for that subtype
        if not word:
            continue
        pool = sorted([o for o in branch if word in (o.get('command_words') or [])],
                      key=lambda o: -(o.get('depth_tier') or 1)) or \
            sorted(branch, key=lambda o: -(o.get('depth_tier') or 1))
        ci = guard = 0
        while _share(slots, ao) < want - tol and guard < 60 and pool:
            o = pool[ci % len(pool)]
            oid = o['objective_id']
            ci += 1
            guard += 1
            if any(x['objective_id'] == oid and x['subtype'] == st for x in slots):
                continue
            if st in {w['subtype'] for w in (contract.get('subtype_waivers') or [])
                      if w.get('objective_id') == oid}:
                continue
            n += 1
            slots.append({
                'slot': 'ITEM-%s-%s-%03d-%s' % (subject, topic, n, st),
                'objective_id': oid,
                'objective_title': o.get('learner_objective') or o.get('syllabus_text'),
                'syllabus_text': o.get('syllabus_text'),
                'subtype': st, 'assessment_objectives': slot_aos(st, o, [ao]),
                'command_word': word if word in in_use else None,
                'mark_tariff': slot_tariff(st, word),
                'difficulty': min(5, (o.get('depth_tier') or 1) + (2 if st == 'EVAL' else 1)),
                'blooms_level': bloom(st, o),
                'marking_guidance_must_name': structures.get(st, []),
                'reason': 'added to reach the framework %s target of %d%%' % (ao, want),
            })
    slots.sort(key=lambda x: (x['objective_id'], x['slot']))

    # ---- performance tasks carry the evaluation share; they are not extra EVAL cards
    size_mcq(sum(tariff_marks(x.get('mark_tariff')) for x in slots), N_TOPICS)
    perf = []
    for i, (kind, note) in enumerate(performance_items(), 1):
        perf.append({'slot': 'ITEM-%s-%s-P%02d' % (subject, topic, i), 'item_type': kind,
                     'brief': note, 'blooms_level': bloom_perf.get(kind, 'Analyse'),
                     'marking_guidance_must_name': structures.get(kind, []),
                     'objective_ids': 'choose 2-4 objectives from this topic that the task '
                                      'genuinely exercises'})

    # ---- what AO mix this plan produces, computed rather than hoped for
    from collections import Counter
    ao = Counter()
    for s in slots:
        for a in s['assessment_objectives']:
            ao[a] += 1
    tot = sum(ao.values()) or 1
    target = framework.get('item_mix_target', {}).get('target_share_percent', {})
    mix = {a: {'planned_share_percent': round(100 * ao.get(a, 0) / tot),
               'target_percent': target.get(a)} for a in AO_CODES}
    bl = Counter(x.get('blooms_level') for x in slots + perf)
    bl_total = sum(bl.values()) or 1
    blooms_mix = {k: {'items': bl.get(k, 0),
                      'share_percent': round(100.0 * bl.get(k, 0) / bl_total)}
                  for k, _ in [(x['level'], 0) for x in
                               (framework.get('blooms_taxonomy') or {}).get('levels', [])]}
    marks_mix, marks_total = ao_marks(slots, perf)
    ao1_floor = round(100 * len(branch) / max(1, tot))
    syl_target = ((framework.get('ao_mark_budget') or {})
                  .get('stated_qualification_weight_percent') or target)
    mix_note = (
        'The syllabus states its AO weights as a share of MARKS, so planned_ao_mix_by_marks is the '
        'one that answers "does this resource match the exam". It values each card at the tariff of '
        'the question it models, split across the AOs the card declares, and values each '
        'performance task at the marks of the paper part it models. The count-based mix below is '
        'reported only because it is what a reader expects to see; do not balance against it. '
        'AO shares by ITEM COUNT: Every objective needs one recall anchor, so AO1 has a '
        'structural floor of about %d%% in this topic (%d objectives against %d slots) and cannot '
        'reach the %s%% target by count however many other cards are added - padding the bank to '
        'chase it makes the resource worse. The framework already measures the AO4 share in '
        'practice time rather than by count for the same reason. Treat AO1 above target as '
        'expected, and AO2/AO3/AO4 below target as the thing worth fixing.'
        % (ao1_floor, len(branch), tot, target.get('AO1')))

    # The contract's item budget is an estimate from exposure; the work order is the
    # operative plan, and the AO balancing pass changes the count. Reconcile the two
    # here rather than leaving an author to discover the mismatch from a failing check.
    realised = len(slots) + len(perf)
    if contract.get('depth_constraints', {}).get('item_budget') != realised:
        contract.setdefault('depth_constraints', {})['item_budget'] = realised
        contract.setdefault('required_outputs', {})['learning_items'] = realised
        contract['item_budget_note'] = (
            'Set from the generated work order, which is the operative plan. The '
            'exposure estimate that seeded it was %s.'
            % contract.get('required_outputs', {}).get('learning_items'))
        with open(os.path.join(td, 'contract.json'), 'w', encoding='utf-8') as _fh:
            json.dump(contract, _fh, indent=1, ensure_ascii=False)

    title = contract.get('topic_title') or ''
    return {
        'work_order_id': 'WO-%s-%s' % (subject, topic),
        'topic_id': topic,
        'topic_title': title,
        'topic': topic_label(topic, title),
        'generated_by': 'build/make_work_order.py — regenerate, never edit',
        'standard': 'v0.2.0-draft',
        'authoring_note': 'Every slot below is decided. Write the prose; do not redesign the plan. '
                          'If a slot is genuinely wrong for the objective, say so in your report '
                          'rather than silently changing it.',
        'output_files': {
            'claims': 'claims/canonical_claim_ledger.json',
            'content_units': [u['file'] for u in unit_plan],
            'learning_items': 'learning-items/topic_%s_items.json' % topic,
            'notes': notes_filename(topic, title),
            'flashcards_when_published': flashcards_filename(topic, title),
        },
        'assessable_objective_count': len(branch),
        'claims_plan': {'per_objective': '2 to 4', 'approximate_total': [len(branch) * 2,
                                                                        len(branch) * 4]},
        'content_units': unit_plan,
        'item_slots': slots,
        'performance_tasks': perf,
        'planned_item_count': len(slots) + len(perf),
        'planned_ao_mix_by_item_count': mix,
        'planned_blooms_mix': blooms_mix,
        'planned_ao_mix_by_marks': {a: {'planned_share_percent': v,
                                        'syllabus_weight_percent': syl_target.get(a)}
                                    for a, v in marks_mix.items()},
        'marks_equivalent_total': marks_total,
        'ao_mix_note': mix_note,
        'excluded_constructs': contract.get('depth_constraints', {}).get('excluded_constructs') or [],
        'adjacent_topics': contract.get('depth_constraints', {}).get('adjacent_topics') or [],
        'excluded_constructs_status': ('declared' if contract.get('depth_constraints', {})
                                       .get('excluded_constructs') else
                                       'MISSING — the planner must supply these before authoring'),
        'subtype_waivers': contract.get('subtype_waivers') or [],
    }


def as_markdown(wo):
    L = ['# Work order — %s' % wo['topic'], '',
         '*%s*' % wo['generated_by'], '',
         '%d assessable objectives · %d planned items · %d content units'
         % (wo['assessable_objective_count'], wo['planned_item_count'], len(wo['content_units'])),
         '', '## Planned AO mix by item count (reported, not targeted)', '',
         '| AO | planned | item-count target |', '|---|---:|---:|']
    for a, v in wo['planned_ao_mix_by_item_count'].items():
        L.append('| %s | %s%% | %s%% |' % (a, v['planned_share_percent'], v['target_percent']))
    L += ['', '## Planned AO mix in marks-equivalent — the measure the syllabus uses', '',
          '| AO | planned | syllabus weight |', '|---|---:|---:|']
    for a, v in wo['planned_ao_mix_by_marks'].items():
        L.append('| %s | %s%% | %s%% |' % (a, v['planned_share_percent'], v['syllabus_weight_percent']))
    L += ['', '%d marks-equivalent of practice in this topic.' % wo['marks_equivalent_total'],
          '', '> %s' % wo['ao_mix_note'], '', '## Content units', '']
    for u in wo['content_units']:
        L.append('**%s** — sub-topic %s, %d objectives%s' % (
            u['unit_id'], u['sub_topic'], len(u['objective_ids']),
            (', %s–%s words' % tuple(u['word_budget'])) if u['word_budget'] else ''))
        for o in u['objectives']:
            L.append('- `%s` tier %s — %s' % (o['objective_id'], o['depth_tier'], o['title']))
        L.append('')
    L += ['## Item slots', '',
          '| Slot | Objective | Subtype | AO | Command word | Tariff | Why |',
          '|---|---|---|---|---|---:|---|']
    for s in wo['item_slots']:
        L.append('| `%s` | %s | %s | %s | %s | %s | %s |' % (
            s['slot'].split('-')[-2] + '-' + s['subtype'], s['objective_title'], s['subtype'],
            '/'.join(s['assessment_objectives']), s['command_word'] or '—',
            s['mark_tariff'] or '—', s['reason']))
    L += ['', '## Performance tasks', '']
    for p in wo['performance_tasks']:
        L.append('- **%s** — %s' % (p['item_type'], p['brief']))
    L += ['', '## Excluded from this topic', '',
          wo['excluded_constructs_status'] if not wo['excluded_constructs']
          else ('Limits the syllabus states, enforced by C-11 in everything a learner reads: '
                + '; '.join('%s (%s)' % (c['construct'], c['source']) if isinstance(c, dict) else '`%s`' % c
                            for c in wo['excluded_constructs'])), '']
    if wo.get('adjacent_topics'):
        L += ['## Owned by another topic', '', 'Name in passing if you must; teach there.', '']
        L += ['- %s' % a for a in wo['adjacent_topics']] + ['']
    return '\n'.join(L)


sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gates import require_prerequisites  # noqa: E402


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('workspace')
    ap.add_argument('topic', nargs='?')
    ap.add_argument('--all', action='store_true', help='every topic in the workspace')
    a = ap.parse_args()
    ws = a.workspace.rstrip('/')
    require_prerequisites(ws)
    topics = ([d for d in sorted(os.listdir(os.path.join(ws, 'topics')))
               if os.path.isdir(os.path.join(ws, 'topics', d))] if a.all else [a.topic])
    if not topics or topics == [None]:
        raise SystemExit('Name a topic, or pass --all')
    done = []
    for t in topics:
        wo = build(ws, t)
        done.append(t)
        td = os.path.join(ws, 'topics', t)
        with open(os.path.join(td, 'work_order.json'), 'w') as fh:
            json.dump(wo, fh, indent=1, ensure_ascii=False)
        with open(os.path.join(td, 'work_order.md'), 'w') as fh:
            fh.write(as_markdown(wo))
        miss = '' if wo['excluded_constructs'] else '   ** excluded_constructs MISSING **'
        m = wo['planned_ao_mix_by_marks']
        syl = '/'.join(str(v['syllabus_weight_percent']) for v in m.values())
        print('%-5s %2d objectives -> %3d items, %d units, AO(marks) %-14s vs syllabus %s%s'
              % (t, wo['assessable_objective_count'], wo['planned_item_count'],
                 len(wo['content_units']),
                 '/'.join(str(v['planned_share_percent']) for v in m.values()), syl, miss))
    if len(done) > 1:
        rows, share, sylw, missing, grand = subject_rollup(ws, done)
        out = write_rollup(ws, rows, share, sylw, missing, grand)
        worst = max(abs(share[a] - (sylw.get(a) or 0)) for a in share)
        print('\nSUBJECT TOTAL  AO %s  vs syllabus %s  (largest gap %d points)  -> %s'
              % ('/'.join(str(share[a]) for a in AO_CODES),
                 '/'.join(str(sylw.get(a)) for a in AO_CODES), worst, out))
        if missing:
            print('%d contracts still have no excluded_constructs — a planner must supply them.'
                  % len(missing))


def subject_rollup(ws, topics):
    """AO coverage for the WHOLE subject, which is the level the syllabus actually stipulates.

    No single topic has to hit the syllabus weights. Enterprise is naturally definitional and
    choosing a source of finance is naturally evaluative; forcing each topic to 30/30/20/20 would
    distort the teaching to satisfy an average. What must match is the subject total, because that
    is what the assessment pages describe - the shape of the whole examination.
    """
    from collections import Counter
    tot = Counter()
    rows, missing = [], []
    syl = {}
    for t in topics:
        wo = _json(os.path.join(ws, 'topics', t, 'work_order.json'))
        m = wo['planned_ao_mix_by_marks']
        syl = {a: v['syllabus_weight_percent'] for a, v in m.items()}
        marks = wo['marks_equivalent_total']
        for a, v in m.items():
            tot[a] += marks * v['planned_share_percent'] / 100.0
        rows.append((t, wo['topic_title'], wo['assessable_objective_count'],
                     wo['planned_item_count'], marks,
                     {a: v['planned_share_percent'] for a, v in m.items()}))
        if not wo['excluded_constructs']:
            missing.append('%s %s' % (t, wo['topic_title']))
    grand = sum(tot.values()) or 1
    share = {a: round(100 * tot.get(a, 0) / grand) for a in AO_CODES}
    return rows, share, syl, missing, round(grand)


def write_rollup(ws, rows, share, syl, missing, grand):
    L = ['# AO coverage — whole subject', '',
         '*Generated by build/make_work_order.py. Regenerate, never edit.*', '',
         'The syllabus states its assessment-objective weights as a share of **marks**, across the '
         'whole examination. That is a property of the subject, not of any one topic: a topic about '
         'what enterprise means is naturally definitional, and a topic about choosing a source of '
         'finance is naturally evaluative. Forcing each topic to the same split would distort the '
         'teaching to satisfy an average. What has to match is the total below.', '',
         '## Subject total', '', '| AO | planned | syllabus weight | gap |', '|---|---:|---:|---:|']
    for a in AO_CODES:
        g = share[a] - (syl.get(a) or 0)
        L.append('| %s | %d%% | %s%% | %+d |' % (a, share[a], syl.get(a), g))
    worst = max(abs(share[a] - (syl.get(a) or 0)) for a in share)
    L += ['', '%s **largest gap %d points** across %s marks-equivalent of practice.'
          % ('✅' if worst <= 5 else '⚠️', worst, format(grand, ',')), '',
          'A gap inside 5 points is the plan matching the exam. A larger one means the item plan '
          'needs more of that kind of practice - not that a topic should be padded.', '',
          '## By topic', '',
          '| Topic | Objectives | Items | Marks-eq | %s |' % ' | '.join(AO_CODES),
          '|---|---:|---:|---:|%s' % ('---:|' * len(AO_CODES))]
    for t, title, nobj, nitem, marks, m in rows:
        L.append('| **%s** %s | %d | %d | %d | %s |'
                 % (t, title, nobj, nitem, marks,
                    ' | '.join('%d%%' % m.get(a, 0) for a in AO_CODES)))
    if missing:
        L += ['', '## Blocking the plan', '',
              'These contracts declare no `excluded_constructs`, so nothing stops an author '
              'teaching beyond the syllabus and the scope check has nothing to enforce. A planner '
              'must supply them:', ''] + ['- %s' % m for m in missing]
    L.append('')
    out = os.path.join(ws, 'curriculum', 'ao_coverage.md')
    open(out, 'w').write('\n'.join(L))
    return out


if __name__ == '__main__':
    main()
