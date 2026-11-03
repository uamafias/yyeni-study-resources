"""Fixed-example algebra teaching dispatch, excluding functions.

Scope: NSSCO 6131 syllabus printed p.18. Teaching methods: local Basics PDF
pp.12–14 (printed pp.10–12), not an official NSSCO marking authority.
All numbers come from the original generated instance; no source items copied.
Other selected lessons use the subject presenters imported below. Source paths
and scope are recorded in docs/plans/2026-10-algebra-content-experience.md.
"""
from .formatting import linear_latex, polynomial_latex
from . import (algebra_fractions_content, algebra_formula_content,
               algebra_indices_content, algebra_logs_content,
               algebra_equations_content, algebra_sequences_content)


LEVEL_LABELS = {
    'nssco_algebraic_manipulation_expansion': {
        1: 'Collecting terms and expanding a bracket',
        2: 'Multiplying algebraic terms and dividing fractions',
        3: 'Expanding two brackets',
        4: 'Expanding a square and collecting terms',
        5: 'Multiplying a bracket by a squared bracket',
    },
    'nssco_factorisation_basics': {
        1: 'Taking out a common number factor',
        2: 'Taking out common number and letter factors',
        3: 'Factorising a difference of squares',
        4: 'Factorising by grouping',
    },
}

CONTENT_BUILDERS = {
    'nssco_polynomials_algebraic_fractions': algebra_fractions_content.content,
    'nssco_expressions_formulae': algebra_formula_content.content,
    'nssco_inequalities_indices': algebra_indices_content.content,
    'nssco_logarithms': algebra_logs_content.content,
    'nssco_linear_simultaneous_equations': algebra_equations_content.content,
    'nssco_solving_quadratic_equations': algebra_equations_content.quadratic_content,
    'nssco_sequences': algebra_sequences_content.content,
}
LEVEL_LABELS.update({
    'nssco_polynomials_algebraic_fractions': algebra_fractions_content.LABELS,
    'nssco_expressions_formulae': algebra_formula_content.LABELS,
    'nssco_inequalities_indices': algebra_indices_content.LABELS,
    'nssco_logarithms': algebra_logs_content.LABELS,
    'nssco_linear_simultaneous_equations': algebra_equations_content.LABELS,
    'nssco_solving_quadratic_equations': algebra_equations_content.QUADRATIC_LABELS,
    'nssco_sequences': algebra_sequences_content.LABELS,
})


def _sum(*terms):
    """Signed sum of (integer coefficient, LaTeX monomial) pairs."""
    out = ''
    for coefficient, monomial in terms:
        if not coefficient:
            continue
        body = monomial if abs(coefficient) == 1 and monomial else f'{abs(coefficient)}{monomial}'
        sign = ('-' if coefficient < 0 else '') if not out else (' - ' if coefficient < 0 else ' + ')
        out += sign + body
    return out or '0'


def _term(coefficient, monomial=''):
    return _sum((coefficient, monomial))


def _power(letter, exponent):
    return letter if exponent == 1 else f'{letter}^{{{exponent}}}'


def _chain(original, intermediates, answer):
    # The final answer is the generator's frozen display, not another answer key.
    values = [original, *intermediates, answer.strip('$')]
    values = [v for i, v in enumerate(values) if i == 0 or v != values[i-1]]
    lines = [values[0] + ' &= ' + values[1], *('&= ' + v for v in values[2:])]
    return '$$\n\\begin{aligned}\n' + r' \\ '.join(lines) + '\n\\end{aligned}\n$$'


def expansion_content(problem):
    m, skill = problem.machine, problem.skill
    # Every expansion question has one expression enclosed in inline maths.
    original = problem.question.split('$')[1]
    v = m.get('names', [m.get('var')])[0]
    intro = f'${v}$ is the variable; its value is not given because we are rewriting an expression.'
    if skill == 'collect_like_terms':
        a, b, c, d = m['coefficients']
        middle = f'({a}+({c}))x + ({b}+({d}))y'
        explanation = (f'$x$ and $y$ are variables. The coefficients of the $x$ terms are ${a}$ and ${c}$; '
                       f'those of the $y$ terms are ${b}$ and ${d}$. '
                       f'Collect each kind separately: ${a}+({c})={a+c}$ and ${b}+({d})={b+d}$. '
                       'Terms with different letters cannot be collected into one term.')
        stages = [middle]
    elif skill == 'expand_number_bracket':
        k, a, b = m['k'], m['a'], m['b']
        stages = [f'({k})\\times({a}{v}) + ({k})\\times({b})']
        explanation = (intro + f' The outside multiplier is ${k}$. Multiply both terms inside the bracket by it: '
                       f'$({k})({a})={k*a}$ and $({k})({b})={k*b}$. '
                       'Keep the sign of each product; multiplying only the first term leaves the expansion unfinished.')
    elif skill == 'expand_monomial_bracket':
        a, b = m['a'], m['b']
        if m['two_letters']:
            c = m['c']
            outside = _term(c, 'xy')
            stages = [f'({outside})({a}x) + ({outside})({b}y)']
            explanation = (f'$x$ and $y$ are variables. The whole outside term is ${outside}$. '
                           f'Its products with ${a}x$ and ${b}y$ have coefficients ${c*a}$ and ${c*b}$. '
                           'In the first product, $xy\\times x=x^2y$; in the second, $xy\\times y=xy^2$. '
                           'Multiply the letters as well as the numbers in both terms.')
        else:
            k = m['k']
            outside = _term(k, v)
            stages = [f'({outside})({a}{v}) + ({outside})({b})']
            explanation = (intro + f' The outside term is ${outside}$. '
                           f'The first product has coefficient $({k})({a})={k*a}$ and contains ${v}^2$ '
                           f'because ${v}\\times {v}={v}^2$. The second product is ${_term(k*b, v)}$. '
                           'The outside letter multiplies every term, including the constant inside the bracket.')
    elif skill == 'divide_algebraic_fraction':
        p, q, r = m['p'], m['q'], m['r']
        stages = [f'\\frac{{{_term(p,v)}}}{{{q}}}\\times\\frac{{1}}{{{r}}}',
                  f'\\frac{{{_term(p,v)}}}{{{q*r}}}']
        explanation = (intro + f' The numerator is ${_term(p,v)}$ and the denominator is ${q}$. '
                       f'Dividing by ${r}$ means multiplying by $1/{r}$, so the denominator becomes ${q*r}$. '
                       'Reduce the numerical fraction, keeping the variable in the numerator. '
                       'Only the divisor is replaced by its reciprocal.')
    elif skill == 'expand_two_brackets':
        a, b, c, d = (m[k] for k in ('a', 'b', 'c', 'd'))
        stages = [f'({a}{v})({c}{v}) + ({a}{v})({d}) + ({b})({c}{v}) + ({b})({d})',
                  _sum((a*c, v+'^2'), (a*d, v), (b*c, v), (b*d, ''))]
        explanation = (intro + ' Multiply every term in the first bracket by every term in the second. '
                       f'The four coefficients are ${a*c}$, ${a*d}$, ${b*c}$ and ${b*d}$. '
                       f'The two middle products both contain ${v}$, so their coefficients add to ${a*d+b*c}$. '
                       'Keep all four products before collecting terms.')
    elif skill == 'expand_square_and_collect':
        a, b, k, u, w = (m[key] for key in ('a', 'b', 'k', 'm', 'n'))
        square = polynomial_latex([a*a, 2*a*b, b*b], v)
        stages = [f'{linear_latex(u,w,v)} + ({k})({square})',
                  _sum((k*a*a, v+'^2'), (2*k*a*b, v), (k*b*b, ''), (u,v), (w,''))]
        explanation = (intro + f' The squared bracket means $({linear_latex(a,b,v)})$ multiplied by itself. '
                       f'Its middle coefficient is $2({a})({b})={2*a*b}$, so the square is ${square}$. '
                       f'Then multiply the entire expanded square by ${k}$, and only then collect '
                       f'the remaining ${linear_latex(u,w,v)}$. The outside multiplier is not squared.')
    elif skill == 'expand_square_times_linear':
        a, b, c, d = (m[key] for key in ('a', 'b', 'c', 'd'))
        square = polynomial_latex([c*c, 2*c*d, d*d], v)
        stages = [f'({linear_latex(a,b,v)})({square})',
                  f'({a}{v})({square}) + ({b})({square})',
                  _sum((a*c*c,v+'^3'), (2*a*c*d,v+'^2'), (a*d*d,v),
                       (b*c*c,v+'^2'), (2*b*c*d,v), (b*d*d,''))]
        explanation = (intro + f' Expand the squared bracket first: it becomes ${square}$. '
                       f'The other bracket contains ${a}{v}$ and ${b}$. Multiply each of these by '
                       'all three terms of the expanded square, giving six products before collecting. '
                       f'In particular the constant product is $({b})({d*d})={b*d*d}$; do not leave it out.')
    else:
        raise ValueError(f'Unsupported expansion skill: {skill}')
    return _chain(original, stages, problem.answer), explanation


def factorisation_content(problem):
    m, skill = problem.machine, problem.skill
    a, b = m['a'], m['b']
    if skill == 'common_number_factor':
        g, sign = m['g'], m['sign']
        u, w = m['letters']
        first, second = _term(g*a,u), _term(sign*g*b,w)
        stages = [f'{g}\\left(\\frac{{{first}}}{{{g}}} + \\frac{{{second}}}{{{g}}}\\right)']
        variables = ' and '.join(f'${letter}$' for letter in (u,w) if letter)
        verb = 'represent variables' if w else 'is a variable'
        explanation = (f'{variables} {verb}. The numerical coefficients are ${g*a}$ and ${sign*g*b}$. '
                       f'Their highest common factor is ${g}$. Divide every term by ${g}$: '
                       f'the bracket contains ${_term(a,u)}$ and ${_term(sign*b,w)}$. '
                       'Keep any negative sign. Check by multiplying the outside factor through the bracket.')
    elif skill == 'common_letter_factor':
        g, k, j, sign, v = (m[key] for key in ('g','k','j','sign','var'))
        factor = _term(g, _power(v,k))
        stages = [f'{factor}\\left(\\frac{{{g*a}}}{{{g}}}{_power(v,j)} + \\frac{{{sign*g*b}}}{{{g}}}\\right)']
        explanation = (f'${v}$ is the variable. The number parts have highest common factor ${g}$. '
                       f'The powers of ${v}$ are ${k+j}$ and ${k}$, so the highest shared letter factor is ${_power(v,k)}$. '
                       f'Take out ${factor}$ from both terms. Division leaves ${_term(a,_power(v,j))}$ '
                       f'and ${sign*b}$ inside the bracket. The constant term remains when all shared letters are removed. '
                       'Expand the product to check that both original terms return.')
    elif skill == 'difference_of_squares':
        g = m['g']
        u, w = m['letters']
        first, second = _term(a,u), _term(b,w)
        prefix = '' if g == 1 else str(g)
        stages = [prefix + f'\\left(({first})^2-({second})^2\\right)']
        variables = ' and '.join(f'${letter}$' for letter in (u,w) if letter)
        verb = 'represent variables' if w else 'is a variable'
        explanation = (f'{variables} {verb}. '
                       + (f'Take out the common number factor ${g}$ first. ' if g != 1 else '')
                       + f'The two squared quantities left are ${first}$ and ${second}$. '
                       'A difference of squares is the product of their difference and their sum: '
                       f'$({first})^2-({second})^2=({first}-({second}))({first}+({second}))$. '
                       + (f'Keep the outside factor ${g}$ in the answer. ' if g != 1 else '')
                       + 'The brackets have opposite signs; expanding makes their middle products cancel.')
    elif skill == 'factorise_by_grouping':
        c, d = m['c'], m['d']
        u, v, w = m['letters']
        bracket = linear_latex(c,d,w)
        firstpair = _sum((a*c,u+w),(a*d,u))
        secondpair = _sum((b*c,v+w),(b*d,v))
        stages = [f'({firstpair}) + ({secondpair})',
                  _sum((a,u+f'({bracket})'),(b,v+f'({bracket})'))]
        explanation = (f'${u}$, ${v}$ and ${w}$ are variables. Group the first two and last two terms. '
                       f'The first pair has factor ${_term(a,u)}$ and the second can be written with factor ${_term(b,v)}$. '
                       f'Each leaves the same bracket, $({bracket})$. Take that whole bracket out as a common factor. '
                       'If a group has a negative outside factor, divide both terms by that negative factor. '
                       'Finish with a product of brackets, then expand to check all four original terms.')
    else:
        raise ValueError(f'Unsupported factorisation skill: {skill}')
    return _chain(m['expression'], stages, problem.answer), explanation


def algebra_content(problem):
    builder = CONTENT_BUILDERS.get(problem.generator_id)
    if builder:
        return builder(problem)
    if problem.generator_id == 'nssco_algebraic_manipulation_expansion':
        return expansion_content(problem)
    if problem.generator_id == 'nssco_factorisation_basics':
        return factorisation_content(problem)
    return None
