"""Public labels and verified worked examples for fixed Practice cards only."""
from functools import lru_cache
from .difficulty import current_rating
from fractions import Fraction

from . import GeneratorError, generate_problem, get_generator
from .formatting import (number_latex, quadratic_latex, square_form_latex,
                         linear_latex, factors_latex, signed_constant_latex)
from .algebra_content import LEVEL_LABELS, algebra_content
from .number_content import LEVEL_LABELS as NUMBER_LEVEL_LABELS, number_content

from .functions_content import content as functions_content, LABELS as FUNCTION_LABELS, legacy_unpadded_answer

from .topic_content import topic_content, LEVEL_LABELS as TOPIC_LEVEL_LABELS
from .functions_concepts_content import content as functions_concepts_content
from .graph_bank import teaching as graph_content
from . import registered_generator_ids

CONTENT_LABELS = {**LEVEL_LABELS, **NUMBER_LEVEL_LABELS, **TOPIC_LEVEL_LABELS, "nssco_functions": FUNCTION_LABELS, "nssco_functions_concepts": FUNCTION_LABELS}

CONTENT_LABELS['nssco_prepared_line_graphs'] = {2: 'Read the gradient from a straight-line graph'}

CONTENT_LABELS.update({gid:get_generator(gid).labels for gid in registered_generator_ids() if gid.startswith('nssco_visual_')})

FACTORISING_LABELS = {
    1: 'Factorising positive quadratics',
    2: 'Factorising with negative terms',
    3: 'Factorising with a leading coefficient',
    4: 'Completing the square',
    5: 'Completing the square and turning points',
}


def worked_example(problem):
    if problem.generator_id == 'nssco_factorising_quadratics':
        return _quadratic_teaching_example(problem)
    content = algebra_content(problem) or number_content(problem) or functions_content(problem) or functions_concepts_content(problem) or graph_content(problem) or topic_content(problem)
    if content is not None:
        return content[1]
    rows = []
    for index, step in enumerate(problem.steps, 1):
        value = step.value if '$' in step.value else f'${step.value}$'
        rows.append(f'{index}. {step.description}\n\n   {value}')
    return '\n\n'.join(rows)


def _quadratic_teaching_example(problem):
    """Explain this saved example; do not change its question or grading memo."""
    a, b, c = problem.machine['quadratic']
    original = quadratic_latex(a, b, c)
    names = (f'**Name the quantities.** $x$ is the variable. In $ax^2+bx+c$, '
             f'$a$ is the coefficient of $x^2$, $b$ is the coefficient of $x$, '
             f'and $c$ is the constant term. Here $a={a}$, $b={b}$ and $c={c}$. ')
    if problem.machine['task'] == 'factorise':
        (m, p), (n, q) = problem.machine['factors']
        r, s = m * q, n * p
        if a == 1:
            return (
                f'1. {names}\n\n'
                f'2. **What are we looking for?** $p$ and $q$ are the numbers inside '
                f'the two brackets $(x+p)(x+q)$. Expanding gives '
                f'$x^2+(p+q)x+pq$. The two numbers must multiply to ${c}$ and add to ${b}$.\n\n'
                f'3. **Check both conditions.** Here $p={p}$ and $q={q}$. '
                f'$pq$ means their product: $pq=({p})\\times({q})={c}$. '
                f'$p+q$ means their sum: $p+q={p} + ({q}) = {b}$. '
                'Checking only the product is not enough: the sum must also match the middle coefficient.\n\n'
                f'4. **Write the factors and check by expanding.**\n\n'
                f'   {problem.answer}\n\n'
                f'   Expanding returns ${original}$, including the signs of every term.'
            )
        return (
            f'1. {names}\n\n'
            f'2. **Why split the middle term?** Look for two numbers '
            f'with product $ac=({a})({c})={a*c}$ and sum $b={b}$. This lets us group terms with a shared bracket.\n\n'
            f'3. **Find and check those numbers.** Call the two numbers $r$ and $s$. '
            f'Here $r={r}$ and $s={s}$, so $rs=({r})({s})={a*c}$ '
            f'and $r+s={r} + ({s}) = {b}$.\n\n'
            f'4. **Split, then take out the common bracket.**\n\n'
            f'   $({a}x^2+({r})x)+(({s})x+({c}))$\n\n'
            f'   $({m})x\\bigl({n}x+({q})\\bigr)+({p})\\bigl({n}x+({q})\\bigr)$\n\n'
            f'   Both groups contain $({n}x+({q}))$, so the product is {problem.answer}.\n\n'
            f'5. **Check all three coefficients.** Expanding gives first coefficient '
            f'$({m})({n})={a}$, middle coefficient $({m})({q})+({n})({p})={b}$ '
            f'and constant $({p})({q})={c}$: the original ${original}$.'
        )

    p = problem.machine['form']['p']
    q = problem.machine['form']['q']
    inside = number_latex(Fraction(b, a))
    rows = [names + 'In the target form $a(x+p)^2+q$, $p$ is the number added to $x$ '
            'inside the squared bracket and $q$ is the constant added outside it. '
            'We will find their values; these letters describe this completed-square form.']
    if a != 1:
        rows.append(f'**Keep the leading coefficient.** Take ${a}$ outside the bracket: '
                    f'${a}\\left(x^2+({inside})x+({number_latex(Fraction(c,a))})\\right)$. '
                    'It multiplies every term inside, including the constant adjustment.')
    rows.append(f'**Why halve the coefficient of x?** Expanding $(x+p)^2$ gives '
                f'$x^2+2px+p^2$. Match $2p$ with ${inside}$, so $p=({inside})/2={p}$.')
    rows.append(f'**Keep the expression equal to the original.** The square '
                f'${a}\\left(x+({p})\\right)^2$ has constant $({a})({p})^2={a*p*p}$. '
                f'The original constant is ${c}$, so the outside adjustment must be '
                f'$q={c}-({a})({p})^2={q}$.')
    form = square_form_latex(a, p, q)
    rows.append(f'**Write the completed square and check it.** Here $a={a}$, $p={p}$ '
                f'and $q={q}$, so the expression is ${form}$. '
                f'Expanding returns ${original}$, so no extra value has been introduced.')
    if problem.machine.get('turning_point') is not None:
        kind = 'minimum' if a > 0 else 'maximum'
        rows.append(f'**Read the turning point.** The square is zero when $x+({p})=0$, '
                    f'so $x={-p}$. Then $y={q}$. The {kind} is at $({-p},{q})$; '
                    'the x-coordinate uses the opposite sign to the number inside the bracket.')
    return '\n\n'.join(f'{index}. {row}' for index, row in enumerate(rows, 1))


def _quadratic_written_solution(problem):
    """Numerical working to model a written response, separate from teaching prose.

    Method reference: Basics PDF pp.13,21–22 (printed pp.11,19–20).
    These are original generated examples, not transcribed source questions.
    """
    a, b, c = problem.machine['quadratic']
    original = quadratic_latex(a, b, c)
    if problem.machine['task'] == 'factorise':
        (m, p), (n, q) = problem.machine['factors']
        r, s = m * q, n * p
        checks = (f'$({r})\\times({s})={a*c}$, '
                  f'${r}+({s})={b}$.\n\n')
        split = (quadratic_latex(a, r, 0) + (' + ' if s > 0 else ' - ')
                 + linear_latex(abs(s), 0) + signed_constant_latex(c))
        # The common bracket is kept intact in both groups.
        bracket = f'({linear_latex(n, q)})'
        first = linear_latex(m, 0) + bracket
        second = (' + ' if p > 0 else ' - ') + (str(abs(p)) if abs(p) != 1 else '') + bracket
        lines = [f'{original} &= {split}', f'&= {first}{second}',
                 f'&= {factors_latex(problem.machine["factors"])}']
        return checks + '$$\n\\begin{aligned}\n' + r' \\'.join(lines) + '\n\\end{aligned}\n$$'

    p, q = problem.machine['form']['p'], problem.machine['form']['q']
    inside = number_latex(Fraction(b, a))
    lead = '' if a == 1 else ('-' if a == -1 else str(a))
    square = f'({linear_latex(1, p)})^2'
    lines = [f'{original} &= {lead}\\left(x^2+({inside})x\\right){signed_constant_latex(c)}',
             f'&= {lead}\\left({square} - {p*p}\\right){signed_constant_latex(c)}',
             f'&= {square_form_latex(a, p, q)}']
    text = '$$\n\\begin{aligned}\n' + r' \\'.join(lines) + '\n\\end{aligned}\n$$'
    if problem.machine.get('turning_point') is not None:
        kind = 'minimum' if a > 0 else 'maximum'
        text += (f'\n\n$x={-p},\\quad y={q}$.\n\n'
                 f'Turning point: $({-p},{q})$ ({kind}).')
    return text


@lru_cache(maxsize=512)
def _fixed_example(generator_id, seed, level):
    return generate_problem(generator_id, seed, level)


@lru_cache(maxsize=512)
def _example_marks(generator_id, seed, level):
    from services.math_marking.grading_contract import build_contract
    return build_contract(_fixed_example(generator_id, seed, level))['marks']


def recipe_presentation(generator_id, params, question, answer, *, include_working=True):
    """Never infer working for an edited, unrelated or unrecognised snapshot.

    Old cards used level*1000+slot. New cards retain the chosen canonical seed
    when the planner had to skip a collision. A mismatch simply has no example.
    This helper is not used for live Recall questions or marking.
    """
    result = {'is_generated': bool(generator_id), 'maths_level': None,
              'maths_level_label': None, 'worked_example': None, 'worked_solution': None,
              'example_marks': None, 'maths_difficulty': None}
    if not generator_id or not isinstance(params, dict):
        return result
    level = params.get('level')
    try:
        generator = get_generator(generator_id)
        if type(level) is not int or level not in generator.levels:
            return result
        result['maths_level'] = level
        result['maths_difficulty'] = current_rating(generator_id, level)
        labels = FACTORISING_LABELS if generator_id == 'nssco_factorising_quadratics' else CONTENT_LABELS.get(generator_id, {})
        result['maths_level_label'] = labels.get(level, f'Maths level {level}')
        if not include_working:
            return result
        seed = params.get('canonical_seed')
        if seed is None:
            slot = params.get('slot')
            if type(slot) is not int or slot < 1:
                return result
            seed = level * 1000 + slot
        if type(seed) is not int:
            return result
        problem = _fixed_example(generator_id, seed, level)
        normalise = lambda text: ' '.join((text or '').split())
        legacy_answer = legacy_unpadded_answer(problem)
        answer_matches = normalise(answer) == normalise(problem.answer) or (legacy_answer is not None and normalise(answer) == normalise(legacy_answer))
        if normalise(question) == normalise(problem.question) and answer_matches:
            result['worked_example'] = worked_example(problem)
            result['example_marks'] = _example_marks(generator_id, seed, level)
            if generator_id == 'nssco_factorising_quadratics':
                result['worked_solution'] = _quadratic_written_solution(problem)
            else:
                content = algebra_content(problem) or number_content(problem) or functions_content(problem) or functions_concepts_content(problem) or graph_content(problem) or topic_content(problem)
                if content is not None:
                    result['worked_solution'] = content[0]
    except (GeneratorError, TypeError, ValueError):
        pass
    return result
