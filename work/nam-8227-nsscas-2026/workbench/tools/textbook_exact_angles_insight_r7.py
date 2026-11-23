"""Narrow R7 author correction after the generic R6 insight rewrite.

No family or curriculum retagging: selected responses and direct exam demand links
supply the comparison evidence. This prevents overlapping family tags from hiding
an independently checked match from this demand's narrative.
"""
DEMAND = '8227:2020:M1:T6:O03:D01'
TITLE = 'Exact special angles and connected geometry'


def repair_exact_special_angle_insight(insights, families, parts):
    matches = [row for row in insights if row['title'] == TITLE]
    assert len(matches) == 1, ('expected one exact-angle insight', len(matches))
    row = matches[0]
    assert DEMAND in row['demand_ids']
    active = sorted(pid for pid, p in parts.items()
                    if DEMAND in p['directly_assessed_demand_ids']
                    and p['disposition'] == 'include' and not p.get('hold_ids'))
    comparisons = []
    seen = set()
    for family in families:
        relations = list(family.get('exam_relations', []))
        relations += [r for exception in family.get('member_level_exceptions', [])
                      for r in exception.get('exam_relations', [])]
        for relation in relations:
            if relation['part_id'] in active and relation['relation'] in ('same type', 'structural branch'):
                key = (family['family_id'], relation['part_id'], relation['relation'])
                if key not in seen:
                    seen.add(key)
                    comparisons.append((family['family_id'], relation))
    same = [(fid, r) for fid, r in comparisons if r['relation'] == 'same type']
    branches = [(fid, r) for fid, r in comparisons if r['relation'] == 'structural branch']
    reciprocal = [(fid, r) for fid, r in same
                  if fid == '8227:TEXTBOOK-FAMILY:reciprocal-exact-values'
                  and r['part_id'] == '8227:EXAM:2023:P2:Q3:b.ii']
    assert reciprocal, 'R7 exact-value counterpart must be attached before rewriting its insight'
    anchor = ('8227:TEXTBOOK-FAMILY:reciprocal-exact-values against '
              '8227:EXAM:2023:P2:Q3:b.ii')
    row['examination_comparison'] = (
        'Directly assessed NSSCAS parts: ' + ', '.join(active) + '.\n\n'
        'A checked same-type exact-value counterpart is ' + anchor + ': Goldie chapter 3 '
        'Exercise 3A Q2(i) and Q2(iii), PDF page 74 / printed page 60. The selected responses '
        'evaluate cotangent and cosecant at related special angles exactly; the exam asks for '
        'cosec(2pi/3)+cot(2pi/3). Reciprocal definitions, quadrant signs and exact surd arithmetic '
        'are the shared decisions. Adding the two exact values is ordinary arithmetic variation. '
        'The original exam target is a numerical exact value, not the integral in part b(iii).\n\n'
        'The other directly linked parts embed special values in different complete tasks: '
        'bounded trigonometric equations, compound-angle work, or geometry. Their exact-value '
        'DD link demonstrates that special values are assessed; it does not make a basic value '
        'drill the same type as the complete connected task. The selected-response ledger records '
        f'{len(same)} same-type and {len(branches)} structural-branch family/part comparisons '
        'against the active parts listed above. These counts describe recorded comparisons, '
        'not distinct recipes, examination frequency or an accepted coverage score.\n\n'
        'Demands without an NSSCAS part in this section: none. The previous absence-of-match '
        'proposal is withdrawn: a concrete counterpart has now been read and recorded.'
    )
    row['implications_for_step3'] = (
        'Use the checked Goldie 3A Q2 / 2023 P2 Q3(b)(ii) selected responses as an exact '
        'reciprocal-evaluation comparison when planning. Preserve exact rather than decimal '
        'answers, radians/degrees, defined reciprocal values and quadrant signs. Textbook '
        'items remain internal evidence; later recipe references require branch-level review.\n\n'
        'Keep a graduated progression visible: basic 30/45/60 values; related-angle signs; '
        'reciprocal values and exact combinations; then compound-angle, bounded-root and '
        'diagram-connected tasks. Decide whether these are separate recipes or embedded '
        'modules in step 3. A non-special angle obtained by a compound identity and a basic '
        'special value are different decisions, even when both final answers are surds.\n\n'
        'Do not replace the observed full tasks with isolated arithmetic drills. Compare '
        'the actual selected textbook responses with each examination part, and use the '
        'explicit extra decisions to set scaffolding and difficulty. Retain the accepted '
        'source-item union for overlapping assessed/component DD tags until planning resolves '
        'the registry overlap; do not retag items merely to improve match counts.\n\n'
        'These are evidence-backed suggestions for planning, not an approved recipe split, '
        'marking contract, generated diagram or learner-display permission.'
    )
    row['examination_part_ids'] = active
    row['exam_comparison_r7'] = {
        'basis': 'Direct part-to-demand links plus checked selected-response relations across families; no family-DD intersection gate.',
        'same_type_relations': len(same), 'structural_branches': len(branches),
        'unexamined_demand_ids': [],
        'exact_value_anchor': anchor,
        'evidence_record': 'analysis/textbook-gap-search-r7.json#8227:EXAM:2023:P2:Q3:b.ii',
        'source_read_date': '2026-11-23',
    }
    return row['exam_comparison_r7']
