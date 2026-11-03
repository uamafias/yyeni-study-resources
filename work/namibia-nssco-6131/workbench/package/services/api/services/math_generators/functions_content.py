"""Fixed Functions examples: NSSCO Topic 7(c); no graph or live Recall changes."""
import re
from fractions import Fraction
from .algebra_teaching import frac, num, work
from .formatting import linear_latex, polynomial_latex

LABELS = {
    1: 'Function meaning, mapping notation, evaluation and cube roots',
    2: 'One-one functions and inverse functions',
    3: 'Using function notation, equations and composite values',
    4: 'Forming a composite of two linear functions',
    5: 'Expanding a composite with a quadratic function',
}


def definitions(question):
    """Read ONLY the generator's constant/linear/quadratic definition grammar.

    These are verified saved examples, never learner-supplied expressions.
    Full matching prevents an unfamiliar expression becoming a plausible rule.
    """
    result = {}
    for name, rhs in re.findall(r'\$([fgh])\(x\) = ([^$]+)\$', question):
        compact = rhs.replace(' ', '')
        terms = re.findall(r'[+-]?(?:\d*x(?:\^2)?|\d+)', compact)
        if ''.join(terms) != compact: raise ValueError(f'Unrecognised function rule: {rhs}')
        coefficients = [0, 0, 0]
        for term in terms:
            if 'x' not in term: coefficients[2] += int(term)
            else:
                coefficient, _, power = term.partition('x')
                value = -1 if coefficient == '-' else 1 if coefficient in ('', '+') else int(coefficient)
                coefficients[0 if power == '^2' else 1] += value
        result[name] = tuple(coefficients)
    return result


def at(coefficients, argument):
    """Bracket an entire replacement, including a negative number or expression."""
    terms = []
    for coefficient, power in zip(coefficients, (2, 1, 0)):
        if coefficient:
            term = f'({coefficient})'
            if power: term += f'({argument})' + ('^2' if power == 2 else '')
            terms.append(term)
    return '+'.join(terms) or '0'


def value(coefficients, x):
    a, b, c = coefficients
    return a*x*x+b*x+c


def content(problem):
    if problem.generator_id != 'nssco_functions': return None
    m = problem.machine; task = m['task']; rules = definitions(problem.question)
    if task == 'cube_equation':
        cube = m['n']; root = round(cube ** (1/3))
        if root**3 != cube: raise ValueError('Expected an exact integer cube')
        lines = [f'x^3={cube}', f'x=\\sqrt[3]{{{cube}}}={root}', f'{root}^3={cube}']
        explanation = f'$x$ is the unknown whose cube is ${cube}$. Undo cubing by taking the cube root, not by dividing by $3$. Here ${root}\\times{root}\\times{root}={cube}$, so the real solution is ${root}$. Cubing preserves the sign; there is no extra negative root as there would be for a positive square equation.'
    elif task == 'evaluate_function':
        x = m['x']; coefficients = rules['f']; result = value(coefficients, x)
        lines = [f'f({x})='+at(coefficients, str(x))+f'={result}']
        explanation = f'$f$ names the function, $x$ its input, and $f(x)$ its output; this notation does not mean $f$ multiplied by $x$. The rule here is $f(x)={polynomial_latex(coefficients)}$. For $f({x})$, replace every $x$ by the complete input ${x}$ in brackets. Calculate powers before multiplication and addition. In particular, squaring a bracketed negative input gives a positive square. The resulting output is ${result}$.'
    elif task == 'inverse_linear':
        a, b, name = m['a'], m['b'], m['name']
        lines = [f'y={linear_latex(a,b)}', f'x={linear_latex(a,b,"y")}',
                 f'x-({b})={a}y', 'y='+frac(f'x-({b})', a)]
        explanation = f'${name}$ names the function. In $y={name}(x)$, $x$ is the input and $y$ the output. Here $y={linear_latex(a,b)}$. The coefficient ${a}$ is nonzero, so different real inputs give different outputs: this linear function is one-one and has an inverse. Swap the input and output letters, then subtract the constant ${b}$ and divide the whole result by ${a}$. Write the resulting rule as ${name}^{{-1}}(x)$. The superscript $-1$ means the function that reverses ${name}$, not its reciprocal $1/{name}(x)$.'
    elif task == 'composite_value':
        x = m['x']; inner = value(rules['f'], x); result = value(rules['g'], inner)
        lines = [f'gf({x})=g(f({x}))', f'f({x})='+at(rules['f'], str(x))+f'={inner}',
                 f'g({inner})='+at(rules['g'], str(inner))+f'={result}']
        explanation = f'$f$ and $g$ are function names, with rules $f(x)={polynomial_latex(rules["f"])}$ and $g(x)={polynomial_latex(rules["g"])}$. In $gf({x})=g(f({x}))$, apply $f$ first to input ${x}$, obtaining ${inner}$. This output becomes the input to $g$, giving ${result}$. Composition is neither multiplication of the two outputs nor permission to reverse the order. Bracket the complete inner output before squaring it.'
    elif task == 'solve_function_equation':
        a, b, p, q = (m[k] for k in ('a','b','p','q')); exact = Fraction(q-b, a-p)
        lines = [f'{linear_latex(a,b)}={linear_latex(p,q)}', f'{linear_latex(a-p,0)}={q-b}',
                 'x='+frac(q-b, a-p)+'='+num(exact)]
        explanation = f'$x$ is the unknown input. Here $f(x)={linear_latex(a,b)}$, and the required output is ${linear_latex(p,q)}$. Replace $f(x)$ by its rule and solve the resulting equation. Subtract ${linear_latex(p,0)}$ and the constant ${b}$ from both sides, then divide by ${a-p}$. Keep the exact fraction ${num(exact)}$ during the working and give the final answer to the requested three significant figures. Finding $f$ at a guessed input would not solve this equation.'
    elif task == 'function_of_expression':
        a, b, k = m['a'], m['b'], m['k']
        lines = [f'g({k}x)={a}({k}x)+({b})', f'g({k}x)={linear_latex(a*k,b)}']
        explanation = f'$g$ names the function and its rule is $g(x)={linear_latex(a,b)}$. The requested input is the entire expression ${k}x$. Replace only the input $x$ inside the rule by ${k}x$: the coefficient becomes ${a}\\times{k}={a*k}$, while the constant ${b}$ stays unchanged. $g({k}x)$ is different from ${k}g(x)$, which would multiply the constant as well.'
    elif task == 'composite_linear':
        order = m['order']; outer, inner = rules[order[0]], rules[order[1]]
        _, a, b = outer; _, c, d = inner
        lines = [f'{order}(x)={order[0]}({order[1]}(x))',
                 f'{order}(x)={a}({linear_latex(c,d)})+({b})',
                 f'{order}(x)={linear_latex(a*c,a*d)}+({b})',
                 f'{order}(x)={linear_latex(a*c,a*d+b)}']
        explanation = f'$f$ and $g$ are function names and $x$ is the input. Here $f(x)={polynomial_latex(rules["f"])}$ and $g(x)={polynomial_latex(rules["g"])}$. Read ${order}(x)$ as ${order[0]}({order[1]}(x))$: apply ${order[1]}$ first, then use its entire output ${linear_latex(c,d)}$ in ${order[0]}$. The outer coefficient ${a}$ multiplies both terms in the bracket; its constant ${b}$ is added afterwards. Expand and collect like terms. Reversing the functions generally changes the result.'
    elif task == 'composite_quadratic':
        order = 'fg' if m['shape'] == 'c_minus_square' else 'gf'
        outer = rules[order[0]]; u, v = m['u'], m['v']; a, _, c = outer
        square = polynomial_latex([u*u, 2*u*v, v*v])
        lines = [f'{order}(x)={order[0]}({order[1]}(x))',
                 f'({linear_latex(u,v)})^2=({u}x)^2+2({u}x)({v})+({v})^2={square}',
                 f'{order}(x)=({a})({linear_latex(u,v)})^2+({c})',
                 f'{order}(x)=({a})({square})+({c})',
                 f'{order}(x)={polynomial_latex([a*u*u,2*a*u*v,a*v*v+c])}']
        explanation = f'$f$ and $g$ name the given rules: $f(x)={polynomial_latex(rules["f"])}$ and $g(x)={polynomial_latex(rules["g"])}$. In ${order}(x)$, ${order[1]}$ is the inner function and supplies the whole expression ${linear_latex(u,v)}$ to ${order[0]}$. Square the entire bracket using $(A+B)^2=A^2+2AB+B^2$, with $A={u}x$ and $B={v}$. The middle term is ${2*u*v}x$ and must be retained. Then multiply every squared-bracket term by the outer coefficient ${a}$ and add its constant ${c}$. A minus before the bracket changes all its term signs.'
    else: raise ValueError(task)
    return work(lines, problem.answer), explanation


def legacy_unpadded_answer(problem):
    """Only the previous exact short-decimal spelling of this same question."""
    if problem.generator_id != 'nssco_functions' or problem.machine.get('task') != 'solve_function_equation':
        return None
    from .family_algebra_b import _short_exact, _dec_text
    m = problem.machine
    exact = Fraction(m['q']-m['b'], m['a']-m['p'])
    return f'$x = {_dec_text(exact)}$' if _short_exact(exact) else None
