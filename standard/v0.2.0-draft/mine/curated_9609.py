# -*- coding: utf-8 -*-
"""9609 misconceptions, curated by reading every AS examiner-report statement.

The pair regex that worked for IGCSE's 17 reports is too noisy on 9609's 11: it
catches phrases like "is a term that most candidates understood but". So each
entry below was restated from the report sentence by hand. Only the confused pair
is kept - never the examiner's wording - and each carries the series it was
reported in, so recurrence is visible.
"""
import json, os, sys
sys.path.insert(0, os.path.expanduser('~/mine'))
import register as R

A = 'adjacent_concept'; N = 'near_neighbour_term'; W = 'wrong_angle_same_concept'
O = 'opposite_direction'; C = 'cause_vs_consequence'

PAIRS = [
 ('market segment', 'target market', A, ['m20']),
 ('private limited company', 'public limited company', N, ['m21', 'w20', 'w22']),
 ('shareholders', 'stakeholders', N, ['m21', 'w21']),
 ('acid test ratio', 'current ratio', N, ['m22']),
 ('price skimming', 'penetration pricing', O, ['m25', 'w20']),
 ('democratic leadership', 'autocratic leadership', A, ['m25', 's22']),
 ('laissez-faire leadership', 'democratic leadership', A, ['w20', 'm25']),
 ('market segmentation', 'multiple product branding', A, ['s21']),
 ('leasing an asset', 'buying an asset', A, ['s21']),
 ('re-order level', 'stock rotation', A, ['s21']),
 ('buffer inventory', 'just-in-time inventory', A, ['s21']),
 ('just-in-time as inventory control', 'just-in-time as fast delivery to customers', W, ['s23']),
 ('product portfolio analysis', 'product life cycle', A, ['s21', 'w22']),
 ('product differentiation', 'product portfolio analysis', A, ['s21', 's23']),
 ('batch production', 'flow production', A, ['s21']),
 ('working capital', 'start-up capital or machinery', A, ['s21', 's22']),
 ('microfinance', 'crowdfunding', A, ['s21']),
 ('crowdfunding', 'other external sources of finance', A, ['w22']),
 ('economies of scale as falling unit cost from larger scale', 'a list of causes such as bulk buying', W, ['s21']),
 ('technical economies of scale', 'technological change', N, ['w20']),
 ('profit', 'profit margin', N, ['s21', 'w22']),
 ('gross profit', 'gross profit margin', N, ['w20']),
 ('cash flow', 'profit', A, ['s22']),
 ('Mintzberg’s management roles', 'Maslow’s hierarchy of needs', A, ['s21']),
 ('the 4Cs', 'the 4Ps', N, ['s22']),
 ('break-even as a number of units of output', 'break-even as a period of time', W, ['s22', 'w21']),
 ('dismissal', 'redundancy', A, ['s22', 's23']),
 ('joint venture', 'merger', A, ['s22']),
 ('joint venture', 'partnership', A, ['w21']),
 ('costs', 'prices', A, ['s23']),
 ('mass market', 'mass marketing', N, ['s23']),
 ('labour productivity', 'labour-intensive production', N, ['s23']),
 ('productivity as output per unit of input', 'productivity as input per unit of output', O, ['w22']),
 ('market share', 'selling shares in the business', N, ['w20']),
 ('venture capital', 'venture capitalist', N, ['w20']),
 ('efficiency', 'effectiveness', N, ['w20']),
 ('CAD', 'CAM', N, ['w20', 'w22']),
 ('loan', 'overdraft', A, ['w21']),
 ('capacity', 'production', A, ['w21']),
 ('psychographic segmentation', 'demographic segmentation', A, ['w21']),
 ('emotional intelligence', 'leadership qualities', A, ['w22']),
 ('ethical requirement', 'legal requirement', A, ['w22']),
 ('person specification', 'job description', N, ['w22', 'w20']),
 ('public sector', 'public limited company', N, ['w22']),
 ('sampling methods', 'market research methods', A, ['w22']),
 ('recruitment', 'selection', A, ['w21']),
 ('marginal cost', 'costs in general', W, ['m22']),
 ('extension strategies', 'new product development', A, ['m23']),
 ('adding value through marketing', 'marketing a product', W, ['w21']),
 ('franchisee', 'franchisor', O, ['s22']),
 ('supply factors', 'demand factors', A, ['m21']),
 ('intangible assets', 'motivation and efficiency', A, ['m21']),
]

# The systemic failures: not one topic's confusion but a way of misreading any
# question. Each is named in several reports and fixes a class of card, not one.
SYSTEMIC = [
 {'failure': 'answered for the wrong party',
  'what': 'The question named one party - the business, or its employees, or the franchisee - '
          'and the answer was written for another.',
  'series': ['m25', 's21', 's22', 'w20', 'w22'],
  'fix': 'Every prompt that names a party carries that party into its canonical answer by name, '
         'and its marking guidance states that an answer for a different party scores nothing.'},
 {'failure': 'several points where one was asked for',
  'what': 'An "Explain one..." or "Analyse one..." question answered with two or three shallow '
          'points, none developed.',
  'series': ['m23', 'm25', 's23', 'w21', 'w22'],
  'fix': 'Cards that model a one-point question give ONE point taken all the way into context, '
         'which is the shape the AO grid rewards: AO1 1 for the point, AO2 2 for its application.'},
 {'failure': 'the opposite side of the question',
  'what': 'Advantages given where disadvantages or limitations were asked for, or the reverse.',
  'series': ['m22', 's22'],
  'fix': 'Cards on benefits and limitations of the same concept are paired, each prompt says '
         'which side it wants, and each answer opens on that side.'},
 {'failure': 'the wrong business context',
  'what': 'A retail business answered as a manufacturer, a car-hire firm as a car dealer.',
  'series': ['m20', 'm22', 'w20'],
  'fix': 'Application items state the kind of business in the stem and the answer turns on what '
         'that kind of business does.'},
 {'failure': 'summary offered as evaluation',
  'what': 'A closing paragraph that repeats the analysis, where a judgement was required.',
  'series': ['s21', 's23', 'w21'],
  'fix': 'EVAL cards end on a judgement that could have gone the other way, with the criterion '
         'that decided it. Repeating the argument is not a conclusion.'},
]

SYLLABUS_TOPIC = {
 'market segment': '3.1', 'private limited company': '1.2', 'shareholders': '1.5',
 'price skimming': '3.3', 'democratic leadership': '2.3', 'laissez-faire leadership': '2.3',
 'market segmentation': '3.1', 'leasing an asset': '5.2', 're-order level': '4.2',
 'buffer inventory': '4.2', 'just-in-time as inventory control': '4.2',
 'product portfolio analysis': '3.3', 'product differentiation': '3.3', 'batch production': '4.1',
 'working capital': '5.1', 'microfinance': '5.2', 'crowdfunding': '5.2', 'cash flow': '5.3',
 'Mintzberg\u2019s management roles': '2.3',
 'break-even as a number of units of output': '5.4', 'dismissal': '2.1',
 'joint venture': '1.3', 'costs': '5.4', 'mass market': '3.1', 'labour productivity': '4.1',
 'productivity as output per unit of input': '4.1', 'market share': '3.1',
 'venture capital': '5.2', 'efficiency': '4.1', 'loan': '5.2', 'capacity': '4.3',
 'psychographic segmentation': '3.1', 'ethical requirement': '1.4',
 'person specification': '2.1', 'public sector': '1.2', 'sampling methods': '3.2',
 'recruitment': '2.1', 'marginal cost': '5.4', 'extension strategies': '3.3',
 'adding value through marketing': '1.1', 'franchisee': '1.2', 'supply factors': '3.1',
 'intangible assets': '3.3',
}
# In an older report, but the current AS syllabus does not teach it.
OUT_OF_AS_SCOPE = {
 'acid test ratio': 'liquidity ratios are A Level, topic 10.2',
 'economies of scale as falling unit cost from larger scale': 'economies of scale are A Level, topic 9.1',
 'technical economies of scale': 'economies of scale are A Level, topic 9.1',
 'profit': 'profit margin is A Level, topics 10.1-10.2',
 'gross profit': 'gross profit and its margin are A Level, topics 10.1-10.2',
 'the 4Cs': 'the 4Cs are not in the syllabus; the marketing mix is taught as the 4Ps in 3.3',
 'CAD': 'CAD and CAM are not in the syllabus',
 'emotional intelligence': 'emotional intelligence is A Level, topic 7.3',
}

def build():
    pairs, dropped = [], []
    for a, b, k, ser in PAIRS:
        e = {'a': a, 'b': b, 'kind': k, 'series': ser, 'n': len(ser)}
        if a in OUT_OF_AS_SCOPE:
            e['dropped_because'] = OUT_OF_AS_SCOPE[a]
            dropped.append(e)
            continue
        tid = SYLLABUS_TOPIC.get(a)
        e['topic_id'] = tid
        e['topic_source'] = ('located in the syllabus subject content, topic %s' % tid
                             if tid else 'not located')
        pairs.append(e)
    # the objective inside the topic still comes from vocabulary overlap, but only
    # among that topic's objectives, so it cannot wander into another topic
    idx = R.registry('9609', R.REGISTRIES['9609'])
    for e in pairs:
        pool = [x for x in idx if x[1] == e['topic_id']]
        if pool:
            best = R.attach([dict(e)], pool)[0]
            e['objective_id'] = best.get('objective_id')
            e['objective_text'] = best.get('objective_text')
    return pairs, dropped

if __name__ == '__main__':
    ps, dropped = build()
    REPO = os.path.expanduser('~/mnt/YYeni Study Resources')
    import collections, datetime
    out = {
     'register_id': 'MISCON-CIE-9609-AS-2026',
     'generated_at': datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ'),
     'authority': 'Cambridge Principal Examiner Reports for Teachers, AS Business 9609, Papers 1 and '
                  '2 only, 11 series 2020-2025. Sections on Papers 3 and 4 (A Level) were removed '
                  'before reading.',
     'method': 'Curated by reading every statement, because the automatic pair extraction was '
               'too noisy on 11 reports. Only the confused pair is kept; no examiner wording is.',
     'derivation_policy': 'No examiner-report wording appears in learner-facing output.',
     'how_to_use': 'Every entry earns one MISCON card on the objective it attaches to. A MISCON '
                   'card is a DISCRIMINATION: it states the boundary between the two ideas and gives '
                   'the test that separates them. It does not restate the correct definition.',
     'systemic_failures': SYSTEMIC,
     'dropped_as_out_of_scope': dropped,
     'scope_rule': 'Every entry was located in the CURRENT syllabus subject content before it was '
                   'kept. A confusion reported in an older series about content the syllabus now '
                   'teaches only at A Level is recorded under dropped_as_out_of_scope with its '
                   'reason, and earns no card.',
     'entries': sorted(ps, key=lambda x: (x.get('topic_id') or 'zz', -x['n']))}
    p = os.path.join(REPO, 'work/cie-9609-as-2026-2028/curriculum/misconceptions.json')
    json.dump(out, open(p, 'w'), indent=1)
    print('%d kept, all located in the syllabus: %d; %d dropped as out of AS scope; '
          '%d recur in 2+ series; %d systemic failures'
          % (len(ps), sum(1 for x in ps if x['topic_id']), len(dropped),
             sum(1 for x in ps if x['n'] >= 2), len(SYSTEMIC)))
    print('by topic:', dict(sorted(collections.Counter(x['topic_id'] for x in ps).items())))
    for x in dropped:
        print('  dropped  %-28s %s' % (x['a'][:28], x['dropped_because']))
