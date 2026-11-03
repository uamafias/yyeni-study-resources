"""Explicit whole-question, solution and marking format for seeded recipes."""
from fractions import Fraction
from decimal import Decimal, ROUND_HALF_UP
import math


# Reasons are authored per demanded mathematical operation. A generic
# "apply the relationship" sentence is not accepted as meaningful teaching.
CALC_REASONS = {
    'number-properties': ['The HCF is the greatest integer dividing both numbers; take the common prime powers with their smaller exponents.', 'The LCM is the least positive common multiple; take every needed prime power with its larger exponent.'],
    'squares-cubes-roots': ['Squaring multiplies the number by itself.', 'Cubing multiplies three equal factors.', 'The square root is the nonnegative number whose square is the given value.', 'The real cube root is the number whose cube is the given value; an odd power preserves a negative sign.'],
    'fraction-quantity-context': ['A fraction of a quantity is found by multiplying the quantity by that fraction.', 'The amount remaining is the original amount minus the amount used.'],
    'six-way-conversions': ['A terminating decimal has a power-of-ten denominator; reduce the resulting fraction.', 'Divide the numerator by the denominator to obtain a decimal.', 'Percent means per hundred, so multiply the proportion by 100.', 'Write the percentage over 100 and cancel common factors.', 'Divide the percentage by 100 to obtain the proportion.', 'Multiply the decimal proportion by 100 to express it as a percentage.'],
    'ordering-and-relations': {},
    'standard-form-four-operations': ['For addition, first express both terms with the same power of ten.', 'For subtraction, first express both terms with the same power of ten.', 'Multiply the coefficients and add the exponents, then normalise the coefficient.', 'Divide the coefficients and subtract the exponents.'],
    'mixed-arithmetic': ['Evaluate brackets and multiplication before combining signed terms.', 'Align decimal place values when adding and subtracting.', 'Carry out multiplication and division from left to right.', 'Use a common denominator for addition and subtraction of fractions.', 'Dividing by a nonzero fraction is multiplying by its reciprocal.'],
    'increase-decrease-ratio': ['The new amount is five quarters of the original amount.', 'The new amount is three quarters of the original amount.'],
    'check-calculator-answer': {0:'Rounding each factor to one significant figure gives a quick order-of-magnitude check.',2:'Multiply the original unrounded factors to check the proposed product.'},
    'household-finance': ['Percentage profit uses profit divided by cost price.', 'Percentage loss uses loss divided by cost price.', 'A 15% discount leaves 85% of the original price.', 'Simple interest is based on the original principal for each year.', 'Compound interest multiplies the current balance by the growth factor each year.'],
    'types-of-earnings': ['A year has twelve monthly salary payments.', 'Piece-work pay is the number of completed items times the rate per item.', 'Add hourly wages and commission calculated on sales.'],
    'water-bill-table': ['Metered consumption is the current cumulative reading minus the previous reading.', 'Multiply usage by its unit tariff, then add the fixed charge once.', 'Credit already paid reduces the amount still owed.'],
    'income-tax-table': {0:'Choose the matching income band, add its base tax, and tax only the income above that band threshold.',1:'Subtract annual tax from annual income before dividing by twelve.'},
    'metric-quantities': ['There are 1000 metres in one kilometre.', 'There are 1000 grams in one kilogram.', 'Area conversion squares the length conversion factor: 1 m² = 10 000 cm².', 'A litre is 1000 cubic centimetres.', 'Volume conversion cubes the length conversion factor: 1 m³ = 1 000 000 cm³.'],
    'bus-timetable': {1:'Subtract arrival from departure at the same stop.',2:'Compare the starting departure with the final arrival, including the waiting time.'},
    'cube-and-prism-measures': ['Prism volume is cross-sectional area multiplied by its length.', 'The surface consists of two triangular ends and one rectangle for each side of the cross-section.', 'A cube has six equal square faces and volume equal to the cube of its edge length.'],
    'sphere-cone-pyramid-measures': ['Use the supplied sphere formulae; surface area involves the square of the radius, while volume involves its cube.', 'Use Pythagoras to find the slant height, then add the circular base area to the curved area.', 'The supplied pyramid volume formula is one third of base area multiplied by perpendicular height.'],
    'symmetry-properties': {0:'A midpoint divides a segment into two equal lengths.'},
    'line-plane-angle': {0:'The base diagonal is the hypotenuse of a right triangle with sides AB and BC.',1:'The space diagonal is the hypotenuse of a right triangle with horizontal side AC and vertical side CG.'},
    'factorising-required-forms': ['Extract the common numerical factor from both terms.', 'Group terms so that the same binomial factor appears twice.', 'A difference of two squares factors as the difference times the sum.', 'The middle term is twice the product of the square roots of the outer terms, so this is a perfect square.', 'Choose two linear factors whose product reconstructs the leading, middle and constant terms.'],
    'algebraic-fraction-operations': ['Use a common denominator before adding the numerators.', 'Use a common denominator and subtract the whole second numerator.', 'Multiply numerators and denominators, then cancel nonzero common factors.', 'Multiply by the reciprocal of the divisor, then cancel nonzero common factors.'],
    'polynomial-operations': ['Add coefficients only for equal powers of x.', 'Subtract every term of Q, changing all its signs before collecting.', 'Distribute each term of the first bracket across the second, then collect like powers.'],
    'all-index-types': {2:'A fractional power first takes the indicated root and then raises the result to the numerator power.'},
    'geometric-nth-term-and-sum': {0:'The nth geometric term uses n−1 applications of the common ratio to the first term.'},
}

DEPENDENCIES={
    'fraction-quantity-context':{1:['a']},
    'water-bill-table':{1:['a'],2:['b']},
    'income-tax-table':{1:['a']},
    'line-plane-angle':{1:['a'],2:['a']},
    'combined-transformations':{1:['a']},
    'percentiles-and-interpretation':{2:['b']},
    'power-sum-exponential-graphs':{1:['a'],2:['b']},
    'linear-quadratic-graph-intersections':{1:['a']},
    'make-scale-drawing':{1:['a']},
    'complete-linear-programme':{1:['a']},
    'frequency-bar-pie-pictogram':{1:['a'],2:['a'],3:['a']},
    'household-spending-chart':{2:['b']},
    'intersecting-loci':{2:['a','b']},
    'relative-frequency-experiment':{1:['a']},
    'locus-constructions':{2:['a','b']},
    'similarity-problems':{2:['a']},
    'line-equation-from-graph':{1:['a']},
}


def significant(value, digits=3):
    """Decimal display with explicit significant zeros, never Python e-notation."""
    number = Decimal(str(value))
    if not number.is_finite() or digits < 1:
        raise ValueError('A finite value and positive precision are required')
    if not number:
        return '0.' + '0' * (digits - 1)
    exponent = number.copy_abs().adjusted() - digits + 1
    rounded = number.quantize(Decimal(1).scaleb(exponent), rounding=ROUND_HALF_UP)
    exponent = rounded.copy_abs().adjusted() - digits + 1
    # Standard form makes trailing significant zeros unambiguous for large values.
    if exponent > 0:
        power = rounded.copy_abs().adjusted()
        coefficient = rounded.scaleb(-power)
        return rf'{coefficient:.{digits-1}f}\times10^{{{power}}}'
    return format(rounded, 'f')


def polynomial(coefficients, variable='x'):
    terms=[]
    degree=len(coefficients)-1
    for i, coefficient in enumerate(coefficients):
        if not coefficient:
            continue
        power=degree-i
        symbol=variable+(f'^{{{power}}}' if power>1 else '') if power else ''
        magnitude='' if abs(coefficient)==1 and power else fmt(abs(coefficient))
        terms.append(('-' if coefficient<0 else '+' if terms else '')+magnitude+symbol)
    return ''.join(terms) or '0'


def coordinates(points, labels=None):
    labels = list(labels) if labels is not None else [''] * len(points)
    return '; '.join(f'{label}({fmt(x)}, {fmt(y)})' for label,(x,y) in zip(labels,points))


def ref(s):
    section, number = s.split('.')
    return f'6131:{section}:{int(number):02d}'


def fmt(x):
    if isinstance(x, Fraction):
        return str(x.numerator) if x.denominator == 1 else ('-' if x < 0 else '') + rf'\frac{{{abs(x.numerator)}}}{{{x.denominator}}}'
    if isinstance(x, float):
        return f'{x:.6g}'
    return str(x)


def step(action, reason, result):
    return {'action': action, 'reason': reason, 'result': str(result)}


def part(prompt, answer, steps, marks=1, criteria=None, objectives=(), checks=()):
    assert steps and all(set(s) == {'action', 'reason', 'result'} for s in steps)
    assert isinstance(marks, int) and marks > 0
    if criteria is None:
        assert marks == 1, 'Multi-mark parts need authored criteria, not inferred model-step counts.'
        needs_reason=any(word in prompt.lower() for word in ('explain','give a reason','justify'))
        criteria = [(1, ('A correct mathematical explanation, not a bare conclusion. Reference: '+str(answer)) if needs_reason else
                        'Correct requested result, with the required mathematical form and units. Reference: '+str(answer))]
    assert sum(m for m, _ in criteria) == marks
    for passed, description in checks:
        assert passed, description
    return {'prompt': prompt, 'reference_answer': str(answer), 'worked_steps': steps,
            'proposed_marks': marks,
            'criteria': [{'marks': m, 'achievement': a} for m, a in criteria],
            'objective_ids': [ref(s) for s in objectives],
            'validation_checks': [description for _, description in checks],
            'alternative_methods': 'Accept mathematically valid alternative methods unless the prompt explicitly requires a method.',
            'feedback_rule': 'Recognise valid progress, locate the first relevant error, and explain the repair in logical mathematical order. Do not equate model steps with marks.'}


def question(key, objectives, title, stem, parts, *, variant=0, gaps=(), assets=(), paper='structured'):
    assert parts and len(parts) <= 8
    for index,p in enumerate(parts):
        if not p['objective_ids']:
            p['objective_ids'] = [ref(s) for s in objectives]
        if p['worked_steps'][0]['reason']=='AUTHOR_REASON_REQUIRED':
            reasons=CALC_REASONS.get(key,{})
            reason=reasons.get(index) if isinstance(reasons,dict) else reasons[index] if index<len(reasons) else None
            assert reason, (key,index,'Missing authored mathematical reason')
            p['worked_steps'][0]['reason']=reason
        dependency_key='power-sum-exponential-graphs' if key.startswith('power-sum-exponential-graphs-') else key
        dependencies=DEPENDENCIES.get(dependency_key,{}).get(index,[])
        p['depends_on_parts']=dependencies
        p['follow_through_policy']=(
            'Proposed adaptation: award the method criterion for a mathematically valid operation using the learner’s clearly stated earlier value/graph, within the original domain and with compatible units. The final accuracy criterion still requires the correct reference result unless it explicitly grants follow-through. Independent review must confirm this route.'
            if dependencies else 'No dependency on a previous submitted part is required; assess this part from its own givens.')
    return {'card_key': f'wb6131:{key}:{variant}', 'recipe_id': f'wb6131:{key}',
            'variant': variant, 'title': title, 'stem': stem, 'parts': parts,
            'objective_ids': sorted({ref(s) for s in objectives} | {o for p in parts for o in p['objective_ids']}),
            'closes_gaps': list(gaps), 'assets': list(assets), 'paper_style': paper,
            'proposed_total_marks': sum(p['proposed_marks'] for p in parts),
            'tariff_status': 'authored_proposal_pending_independent_review',
            'exam_style_basis': 'Original question following the NSSCO short-answer/structured-paper formats; syllabus demand is authoritative. Source analogues are attached by the bank builder.',
            'content_status': 'draft_for_independent_review',
            'submission': 'Submit working for the complete question, including every labelled part.'}


def calc(prompt, answer, setup, result, *, reason='AUTHOR_REASON_REQUIRED', marks=2, objectives=(), checks=()):
    # A setup and its routine evaluation form one consequential action. Do not
    # invent a second teaching step merely to mirror a two-mark allocation.
    working = str(setup) if str(setup)==str(result) else f'{setup}; result: {result}'
    steps = [step('Calculate the requested quantity', reason, working)]
    criteria = [(1, f'A valid setup equivalent to {setup}; accept valid alternative methods.'), (1, f'Correct requested result: {answer}.')]
    if marks == 1:
        criteria = [(1, 'Correct requested result and form.')]
    return part(prompt, answer, steps, marks, criteria, objectives, checks)


PARTIAL = '''1a.1 1a.2 1b.1 1d.1 1d.2 1e.1 1f.2 1g.1 1k.1 1l.2 1l.4 1l.5
2main.1 2main.2 3main.1 3main.4 4main.1 4main.3 5a.1 5a.3 5a.4 5b.1 5b.2 5c.1 5c.2 5d.1 5e.1
6a.4 6b.4 6b.5 6c.1 6d.4 6d.5 6e.1 6f.4 6g.1 7a.2 7b.1 7c.3 7d.1 7d.2 7d.4 7d.5 7d.6
9a.2 9a.4 9b.3 9b.5 10main.1 10main.3 11main.6 12a.3 12a.4 12a.7 12b.2'''.split()
MISSING = '''1h.3 1j.3 1k.2 1l.3 1l.6 5a.2 5b.4 6a.1 6f.3 10main.4 12a.1 12b.5'''.split()
assert len(PARTIAL) == 55 and len(MISSING) == 12
