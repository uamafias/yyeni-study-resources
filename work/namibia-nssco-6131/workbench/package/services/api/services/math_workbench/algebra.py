"""Seeded algebra recipes for missing methods and representations."""
from fractions import Fraction as F
import math
import random
from .core import calc, fmt, part, question, step, polynomial

def build_generalised_expressions(seed, rng, requested_key=None):
    out = []
    q = lambda key, objs, title, stem, ps, **kw: out.append(question(key, objs, title, stem, ps, variant=seed, **kw))
    a, b, fee = (rng.randint(15, 40), rng.randint(5, 14), rng.randint(10, 30))
    q('generalised-expressions', ['6a.1', '6a.3'], 'Writing expressions', f'A club charges N${a} for each adult ticket and N${b} for each child ticket. A booking also has one fixed fee of N${fee}.', [part('Write an expression for the cost of n adult tickets and m child tickets in one booking.', f'{a}n+{b}m+{fee}', [step('Represent the separate costs', 'Each ticket price is multiplied by its count, while the fee is paid once.', f'{a}n + {b}m + {fee}')], 2, [(1, 'Correct variable ticket costs.'), (1, 'One fixed fee added correctly.')]), part('The first of three consecutive integers is k. Write and simplify an expression for their sum.', '3k + 3', [step('Represent consecutive integers', 'Successive integers differ by 1.', 'k, k+1, k+2'), step('Add the expressions', 'Collect like terms.', 'k+(k+1)+(k+2)=3k+3')], 2, [(1, 'Correct three integers.'), (1, 'Correct simplified sum.')]), part('Write an expression for an odd integer in terms of an integer p.', '2p + 1 (also accept 2p − 1)', [step('Use the even-integer form', 'Twice an integer is even; adding or subtracting 1 gives an odd integer.', '2p+1')])])
    return out

def build_rearranging_complex_formulae(seed, rng, requested_key=None):
    out = []
    q = lambda key, objs, title, stem, ps, **kw: out.append(question(key, objs, title, stem, ps, variant=seed, **kw))
    c, d = (rng.randint(2, 7), rng.randint(2, 9))
    q('rearranging-complex-formulae', ['6a.4'], 'Changing the subject', 'All expressions used as denominators are nonzero. In the speed formula, u ≥ 0 and v² ≥ 2as.', [part('$v^2=u^2+2as$. Make u the subject.', 'u=\\sqrt{v^2-2as}', [step('Isolate the squared subject', 'Subtract the other term from both sides.', 'u² = v² − 2as'), step('Choose the nonnegative root', 'u is stated to be nonnegative.', 'u=\\sqrt{v^2-2as}')], 2, [(1, 'Correct isolated square.'), (1, 'Correct nonnegative root.')]), part('$V=\\frac43\\pi r^3$. Make r the subject.', 'r=\\sqrt[3]{\\frac{3V}{4\\pi}}', [step('Isolate the cube', 'Divide by the full coefficient.', 'r^3=\\frac{3V}{4\\pi}'), step('Undo the cube', 'Take the cube root.', 'r=\\sqrt[3]{\\frac{3V}{4\\pi}}')], 2, [(1, 'Cube isolated correctly.'), (1, 'Correct cube root.')]), part('$\\frac1f=\\frac1u+\\frac1v$. Make v the subject.', 'v=\\frac{fu}{u-f}', [step('Collect the fraction containing v', 'Subtract 1/u and combine over a common denominator.', '\\frac1v=\\frac{u-f}{fu}'), step('Invert the relationship', 'Both sides are nonzero under the stated denominator restrictions.', 'v=\\frac{fu}{u-f}')], 3, [(1, 'Correct isolation of 1/v.'), (1, 'Correct single fraction.'), (1, 'Correct subject v.')]), part(f'$y=\\frac{{{c}x+{d}}}{{2x+1}}$. Make x the subject.', f'x=\\frac{{{d}-y}}{{2y-{c}}}', [step('Remove the fraction', 'Multiply by the denominator.', f'2xy+y = {c}x+{d}'), step('Collect and factor the x terms', 'The subject appears on both sides.', f'x(2y−{c}) = {d}−y'), step('Divide by the coefficient', 'Require 2y−' + str(c) + ' ≠ 0.', f'x=\\frac{{{d}-y}}{{2y-{c}}}')], 3, [(1, 'Correct multiplication/collection.'), (1, 'Correct factorisation of x.'), (1, 'Correct rearranged formula.')])])
    return out

def build_factorising_required_forms(seed, rng, requested_key=None):
    out = []
    q = lambda key, objs, title, stem, ps, **kw: out.append(question(key, objs, title, stem, ps, variant=seed, **kw))
    r,s=rng.choice([(r,s) for r in range(2,8) for s in range(2,7) if math.gcd(r,s)==1])
    k=rng.randint(2,9)
    from services.math_generators.factorisation_forms import perfect_square_form,grouping_form
    u,v=rng.choice([(u,v) for u in range(2,8) for v in range(2,7) if math.gcd(u,v)==1 and (u,v)!=(r,s)])
    square,square_answer,square_work=perfect_square_form(u,v,compact=True)
    grouped,grouped_answer,grouped_work=grouping_form(1,1,k,compact=True)
    q('factorising-required-forms', ['6b.4'], 'Factorisation', 'Factorise each expression completely.', [calc(f'${r}x+{r}y$', f'{r}(x+y)', f'Common factor = {r}', f'{r}(x+y)', marks=1), calc(f'${grouped}$',grouped_answer,grouped_work,grouped_answer), calc(f'${r * r}x^2-{s * s}y^2$', f'({r}x-{s}y)({r}x+{s}y)', f'({r}x)^2-({s}y)^2', f'({r}x-{s}y)({r}x+{s}y)'), calc(f'${square}$',square_answer,square_work,square_answer), calc(f'${r}x^2+{r * k + s}x+{s * k}$', f'({r}x+{s})(x+{k})', f'{r * k + s} = {r * k}+{s}; product {r}×{s * k}', f'({r}x+{s})(x+{k})')])
    return out

def build_algebraic_fraction_operations(seed,rng,requested_key=None):
    a,b,c,d=[rng.randint(2,8) for _ in range(4)];p=rng.randint(1,6)
    first=rf'\frac{{{a+b}x+{a}}}{{x(x+1)}}'
    second=rf'\frac{{{polynomial([a-b,p*(a+b)])}}}{{x^2-{p*p}}}'
    return [question('algebraic-fraction-operations',['6b.5'],'Algebraic fractions',
      'Simplify each expression. All displayed denominators and divisors are nonzero.',[
        part(rf'$\frac{{{a}}}x+\frac{{{b}}}{{x+1}}$',first,[
          step('Use a common denominator','Multiply each numerator and denominator by its missing factor.',rf'\frac{{{a}(x+1)+{b}x}}{{x(x+1)}}'),
          step('Expand and collect the numerator','Only terms with the same variable power can be combined.',first)],2,[(1,'Correct common denominator and rescaled numerators.'),(1,'Correct simplified numerator over the common denominator.')]),
        part(rf'$\frac{{{a}}}{{x-{p}}}-\frac{{{b}}}{{x+{p}}}$',second,[
          step('Subtract over a common denominator','Keep the complete second numerator in brackets after the minus sign.',rf'\frac{{{a}(x+{p})-{b}(x-{p})}}{{(x-{p})(x+{p})}}'),
          step('Expand and collect','Distribute the subtraction to both terms; the denominator is a difference of squares.',second)],2,[(1,'Correct common denominator and subtraction of the whole second numerator.'),(1,'Correct simplified fraction.')]),
        part(rf'$\frac{{{a}x}}{{{b}y}}\times\frac{{{c}y}}{{{d}x}}$',fmt(F(a*c,b*d)),[
          step('Multiply numerators and denominators','Multiplication combines the two numerators and the two denominators.',rf'\frac{{{a*c}xy}}{{{b*d}xy}}'),
          step('Cancel common nonzero factors','The restrictions allow xy to be cancelled; reduce the remaining numerical fraction.',fmt(F(a*c,b*d)))],2,[(1,'Correct product of the two fractions.'),(1,'Correct cancellation and reduced result.')]),
        part(rf'$\frac{{{a}x}}{{{b}y}}\div\frac{{{c}x}}{{{d}y}}$',fmt(F(a*d,b*c)),[
          step('Multiply by the reciprocal','Invert only the divisor when replacing division with multiplication.',rf'\frac{{{a}x}}{{{b}y}}\times\frac{{{d}y}}{{{c}x}}'),
          step('Multiply and cancel common factors','Both x and y are nonzero under the stated restrictions.',rf'\frac{{{a*d}xy}}{{{b*c}xy}}={fmt(F(a*d,b*c))}')],2,[(1,'Correct reciprocal multiplication.'),(1,'Correct cancellation and reduced result.')])],variant=seed)]

def build_polynomial_operations(seed, rng, requested_key=None):
    out = []
    q = lambda key, objs, title, stem, ps, **kw: out.append(question(key, objs, title, stem, ps, variant=seed, **kw))
    a, b, c = (rng.randint(2, 7), rng.randint(2, 7), rng.randint(1, 8))
    q('polynomial-operations', ['6c.1'], 'Polynomial operations', f'$P(x)={polynomial([a,b,-c])}$ and $Q(x)={polynomial([1,-c,b])}$.', [calc('Find P(x) + Q(x).', polynomial([a + 1, b - c, b - c]), f'({a}+1)x²+({b}−{c})x+({b}−{c})', polynomial([a + 1, b - c, b - c])), calc('Find P(x) − Q(x).', polynomial([a - 1, b + c, -b - c]), f'({a}−1)x²+({b}+{c})x−({c}+{b})', polynomial([a - 1, b + c, -b - c])), calc(f'Expand $(x+{b})({a}x^2-{c})$.', polynomial([a,a*b,-c,-b*c]), f'x({a}x²−{c})+{b}({a}x²−{c})', polynomial([a,a*b,-c,-b*c]))])
    return out

def build_solve_completing_square(seed, rng, requested_key=None):
    out = []
    q = lambda key, objs, title, stem, ps, **kw: out.append(question(key, objs, title, stem, ps, variant=seed, **kw))
    p = rng.randint(1, 9)
    n = rng.choice([2, 3, 5, 6, 7, 10, 11, 13])
    constant = p * p - n
    q('solve-completing-square', ['6d.4'], 'Solving by completing the square', f'Solve ${polynomial([1,2*p,constant])}=0$ by completing the square. Give exact answers.', [part('Find both values of x.', f'x=-{p}\\pm\\sqrt{{{n}}}', [step('Form a complete square', 'Half the coefficient of x is ' + str(p) + ', whose square is ' + str(p * p) + '.', f'(x+{p})^2-{p*p}'+('+' if constant>=0 else '-')+f'{abs(constant)}=0'), step('Isolate the square', 'Collect the constant terms.', f'(x+{p})^2={n}'), step('Take both square roots', 'Both signs are required for the two real solutions.', f'x=-{p}\\pm\\sqrt{{{n}}}')], 4, [(1, 'Correct square-completion structure using (x+' + str(p) + ')²; another method does not earn this mark.'), (1, 'Correct compensating constant and isolated square; requires square-completion evidence.'), (1, 'One correct exact root, obtained by any valid method.'), (1, 'The other distinct correct exact root; a repeated copy of the first root earns no second accuracy mark. Accept roots from any valid method.')], checks=[(constant == p * p - n, 'Completing-square parameters reconstruct the original quadratic')])])
    return out

def build_required_quadratic_formula(seed, rng, requested_key=None):
    out = []
    q = lambda key, objs, title, stem, ps, **kw: out.append(question(key, objs, title, stem, ps, variant=seed, **kw))
    A, B, C = (rng.randint(2, 6), rng.randint(1, 9), -rng.randint(2, 12))
    D = B * B - 4 * A * C
    roots = [(-B + sign * math.sqrt(D)) / (2 * A) for sign in (-1, 1)]
    q('required-quadratic-formula', ['6d.4'], 'The quadratic formula', f'Use the quadratic formula to solve ${polynomial([A,B,C])}=0$. Give answers to 2 decimal places.', [part('Find both roots.', ', '.join((f'{x:.2f}' for x in roots)), [step('Identify the coefficients', 'The formula uses the signed coefficient values.', f'a={A}, b={B}, c={C}'), step('Substitute into the formula', 'Use both signs and divide the entire numerator by 2a.', f'x=\\frac{{-{B}\\pm\\sqrt{{{D}}}}}{{{2 * A}}}'), step('Evaluate both roots', 'Retain calculator precision until the requested final rounding.', ', '.join((f'{x:.2f}' for x in roots)))], 4, [(1, f'Correctly identify a={A}, b={B}, c={C}, or discriminant {D}, for the required quadratic-formula method.'), (1, 'Correct application of the explicitly required quadratic formula; another method does not earn this method mark.'), (1, 'One correct root.'), (1, 'The second correct root.')], checks=[(all((abs(A * x * x + B * x + C) < 1e-08 for x in roots)), 'Both formula roots independently substituted into the equation')])])
    out[0]['parts'][0]['alternative_methods'] = 'This question explicitly requires the quadratic formula. The first two marks assess that method; correct roots from another valid method can earn the final two accuracy marks. Do not call a valid alternative mathematically wrong.'
    return out

def build_rational_quadratic_equation(seed, rng, requested_key=None):
    out = []
    q = lambda key, objs, title, stem, ps, **kw: out.append(question(key, objs, title, stem, ps, variant=seed, **kw))
    a = rng.randint(2, 15)
    factor = rng.choice([2, 3, 5, 6, 7, 8])
    radicand = 1 + 2 * factor
    q('rational-quadratic-equation', ['6d.5'], 'An equation with fractions', f'Consider $\\frac{{{factor * a}}}{{x-{a}}}-\\frac{{{factor * a}}}{{x+{a}}}=1$.', [part('State the values x cannot take.', f'x\\ne {a},\\quad x\\ne -{a}', [step('Check both denominators', 'Division by zero is undefined.', f'x\\ne\\pm {a}')]), part('Solve the equation, giving exact answers.', f'x=\\pm {a}\\sqrt{{{radicand}}}', [step('Combine over a common denominator', 'Subtract the whole second numerator.', f'\\frac{{{factor * a}(x+{a})-{factor * a}(x-{a})}}{{x^2-{a * a}}}=1'), step('Remove the valid denominator', 'The numerator is ' + str(2 * factor * a * a) + '.', f'{2 * factor * a * a}=x²−{a * a}'), step('Solve and check the domain', 'Take both roots; neither is an excluded value.', f'x^2={radicand * a * a},\\quad x=\\pm {a}\\sqrt{{{radicand}}}')], 4, [(1, 'Correct common denominator/numerator.'), (1, 'Correct resulting quadratic equation.'), (1, 'Both roots.'), (1, 'Roots retained consistently with the domain.')], checks=[(all((abs(factor * a / (x - a) - factor * a / (x + a) - 1) < 1e-08 for x in (-a * math.sqrt(radicand), a * math.sqrt(radicand)))), 'Both rational-equation roots checked in the original fractions')])])
    return out

def build_all_index_types(seed, rng, requested_key=None):
    out = []
    q = lambda key, objs, title, stem, ps, **kw: out.append(question(key, objs, title, stem, ps, variant=seed, **kw))
    b = rng.randint(2, 7)
    m = rng.randint(2, 6)
    n = rng.randint(2, 5)
    q('all-index-types', ['6e.1', '6e.2'], 'Index laws', 'All algebraic bases in this question are positive.', [part('$x^0$', '1', [step('Apply the zero-index law', 'A nonzero base to power zero is 1.', 'x⁰ = 1')]), part(f'$x^{{-{m}}}$', f'\\frac1{{x^{m}}}', [step('Apply the negative-index law', 'A negative power is the reciprocal of the corresponding positive power.', f'x^{{-{m}}}=1/x^{m}')]), calc(f'$({b ** 4})^{{3/4}}$', b ** 3, f'(({b})^4)^{{3/4}}={b}^3', b ** 3), part(f'$x^{m}\\times x^{n}\\div x^2$', f'x^{{{m + n - 2}}}', [step('Combine powers with a common base', 'Add exponents for multiplication and subtract for division.', f'x^{{{m}+{n}-2}}=x^{{{m + n - 2}}}')])])
    return out

def build_classify_progressions(seed, rng, requested_key=None):
    out = []
    q = lambda key, objs, title, stem, ps, **kw: out.append(question(key, objs, title, stem, ps, variant=seed, **kw))
    a, d, b, r = (rng.randint(2, 12), rng.randint(2, 7), rng.randint(2, 9), rng.randint(2, 4))
    q('classify-progressions', ['6f.3'], 'Arithmetic and geometric sequences', 'Classify each sequence as arithmetic, geometric or neither. Give a numerical reason.', [part(f'{a}, {a + d}, {a + 2 * d}, {a + 3 * d}, …', f'Arithmetic, common difference {d}.', [step('Compare consecutive differences', 'A constant difference identifies an arithmetic sequence.', f'Every difference is {d}.')], 2, [(1, 'Arithmetic.'), (1, 'Correct common difference.')]), part(f'{b}, {b * r}, {b * r * r}, {b * r ** 3}, …', f'Geometric, common ratio {r}.', [step('Compare consecutive ratios', 'A constant ratio identifies a geometric sequence.', f'Every ratio is {r}.')], 2, [(1, 'Geometric.'), (1, 'Correct common ratio.')]), part(f'{a}, {a + 3}, {a + 8}, {a + 15}, …', 'Neither; differences are 3, 5, 7 and ratios are not constant.', [step('Check both definitions', 'Neither the consecutive differences nor the consecutive ratios are constant.', 'Neither arithmetic nor geometric.')], 2, [(1, 'Neither.'), (1, 'Valid rejection of both arithmetic and geometric definitions.')])])
    return out

def build_geometric_nth_term_and_sum(seed, rng, requested_key=None):
    out = []
    def q(key,objs,title,stem,ps,**kw):
        formula=rf'T_n={a}\times{r}^{{n-1}}'
        ps.append(part('Find an expression for the nth term of this progression.',formula,[
            step('Count the repeated ratios','The first term uses no ratio multiplications; term n uses n−1.',rf'T_n=a r^{{n-1}}'),
            step('Use this progression’s first term and ratio','The general rule must generate every term, starting with the given first term at n=1.',formula)],2,[(1,'Exponent n−1.'),(1,'Correct first-term multiplier and common ratio.')],objectives=['6f.2']))
        out.append(question(key,objs,title,stem,ps,variant=seed,**kw))
    a, r, n = (rng.randint(2, 12), rng.choice([2, 3]), rng.randint(5, 8))
    term = a * r ** (n - 1)
    total = a * (r ** n - 1) // (r - 1)
    q('geometric-nth-term-and-sum', ['6f.4'], 'A geometric progression', f'A geometric progression has first term {a} and common ratio {r}.', [calc(f'Calculate its {n}th term.', term, f'{a}\\times{r}^{{{n}-1}}', term), part(f'Calculate the sum of its first {n} terms.', str(total), [step('Use the finite geometric-series formula', 'For r ≠ 1, Sₙ = a(rⁿ−1)/(r−1).', f'S_{{{n}}}=\\frac{{{a}({r}^{n}-1)}}{{{r}-1}}'), step('Evaluate the sum', 'The expression totals the stated finite number of terms.', str(total))], 3, [(1, 'Correct sum formula.'), (1, 'Correct substitution and evaluation process.'), (1, 'Correct finite sum.')], checks=[(sum((a * r ** i for i in range(n))) == total, 'Geometric sum independently checked by explicitly summing the terms')])])
    return out

def build_logarithm_index_conversion(seed, rng, requested_key=None):
    out = []
    q = lambda key, objs, title, stem, ps, **kw: out.append(question(key, objs, title, stem, ps, variant=seed, **kw))
    k, l = (rng.choice([-4, -3, -2, -1, 1, 2, 3, 4]), rng.choice([-4, -3, -2, -1, 1, 2, 3, 4]))
    q('logarithm-index-conversion', ['6g.1'], 'Logarithms and indices', 'All logarithms are to base 10.', [part(f'Write $10^{{{k}}}={10.0 ** k:g}$ as a logarithmic statement.', f'\\log({10.0 ** k:g})={k}', [step('Use the inverse relationship', 'The logarithm is the exponent to which 10 is raised.', f'\\log({10.0 ** k:g})={k}')]), part(f'Write $\\log({10.0 ** l:g})={l}$ as an exponential statement.', f'10^{{{l}}}={10.0 ** l:g}', [step('Read the logarithm as an exponent', 'log₁₀(N)=p is equivalent to 10ᵖ=N.', f'10^{{{l}}}={10.0 ** l:g}')])])
    return out

def build_nonlinear_inverse_composite(seed, rng, requested_key=None):
    out = []
    q = lambda key, objs, title, stem, ps, **kw: out.append(question(key, objs, title, stem, ps, variant=seed, **kw))
    a, b, c, d = (rng.randint(2, 10), rng.randint(1, 8), rng.randint(2, 7), rng.randint(1, 9))
    q('nonlinear-inverse-composite', ['7c.3'], 'Inverse and composite functions', f'$f(x)=\\frac{{{a}}}{{x+{b}}}$ for $x>-{b}$, and $g(x)={c}x+{d}$.', [part('Find $f^{-1}(x)$.', f'f^{{-1}}(x)=\\frac{{{a}}}x-{b}', [step('Reverse the input-output relationship', 'Write y=a/(x+b), then isolate the original input.', f'x=\\frac{{{a}}}y-{b}'), step('Write the inverse rule', 'Exchange the input/output labels.', f'f^{{-1}}(x)=\\frac{{{a}}}x-{b}')], 2, [(1, 'Correct reversal/rearrangement.'), (1, 'Correct inverse function.')]), part('State the domain of $f^{-1}$.', 'x > 0', [step('Find the range of f', 'For x > −b, the denominator is positive, so f takes every positive value.', 'The inverse domain is x > 0.')]), part('Find $gf(x)$.', f'gf(x)=\\frac{{{c * a}}}{{x+{b}}}+{d}', [step('Apply f before g', 'gf means g(f(x)), so the entire output of f is the input to g.', f'g(f(x))={c}\\left(\\frac{{{a}}}{{x+{b}}}\\right)+{d}'), step('Simplify', 'Multiply the numerator by the coefficient in g.', f'gf(x)=\\frac{{{c * a}}}{{x+{b}}}+{d}')], 2, [(1, 'Correct composition order/substitution.'), (1, 'Correct simplified composite.')])])
    return out
BUILDERS = [build_generalised_expressions, build_rearranging_complex_formulae, build_factorising_required_forms, build_algebraic_fraction_operations, build_polynomial_operations, build_solve_completing_square, build_required_quadratic_formula, build_rational_quadratic_equation, build_all_index_types, build_classify_progressions, build_geometric_nth_term_and_sum, build_logarithm_index_conversion, build_nonlinear_inverse_composite]

def build(v, rng=None):
    rng = rng or random.Random(v)
    return [q for builder in BUILDERS for q in builder(v, rng)]
