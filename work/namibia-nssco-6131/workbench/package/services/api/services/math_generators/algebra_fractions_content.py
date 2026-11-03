"""NSSCO-scope fraction/polynomial examples; Basics PDF pp.13–15 and exam evidence."""
from fractions import Fraction
from .algebra_teaching import frac, bracket, num, work, expression_in
from .formatting import polynomial_latex, linear_latex

LABELS = {1:'Cancelling common factors in quadratic fractions',
          2:'Dividing a polynomial and finding its remainder',
          3:'Factorising fractions with common factors and squares',
          4:'Combining fractions with linear denominators',
          5:'Combining fractions with shared algebraic factors'}


def content(problem):
    m, skill = problem.machine, problem.skill
    original = expression_in(problem.question)
    domain = ''
    if skill == 'simplify_fraction_quadratics':
        p = m['common']; q = m['numerator'][1]-p; r = m['denominator'][1]-p
        shared, top, bottom = bracket(1,p), bracket(1,q), bracket(1,r)
        lines = [original+'='+frac(shared+top,shared+bottom), frac(shared+top,shared+bottom)+'='+frac(top,bottom)]
        explanation = (f'$x$ is the variable. The numerator factorises as ${shared}{top}$ and the denominator '
                       f'as ${shared}{bottom}$. The whole factor ${shared}$ is shared. Divide numerator and denominator '
                       'by that factor; do not cancel individual terms joined by addition or subtraction.')
        domain = f'$x\\ne {num(-p)}$ and $x\\ne {num(-r)}$'
    elif skill == 'divide_cubic_by_linear':
        a,b,c = m['quotient']; k=m['divisor_k']; dividend=m['dividend']; remainder=m['remainder']
        divisor=linear_latex(1,k); first=polynomial_latex([a,a*k,0,0]); rest1=polynomial_latex([b,dividend[2],dividend[3]])
        second=polynomial_latex([b,b*k,0]);rest2=linear_latex(c,dividend[3])
        final=polynomial_latex([a,b,c])
        lines=[frac(f'{a}x^3','x')+f'={a}x^2',
               polynomial_latex(dividend)+f'-({first})={rest1}',
               frac(f'({b})x^2','x')+f'={b}x',
               f'{rest1}-({second})={rest2}',
               f'{rest2}-({c})({divisor})={remainder}',
               polynomial_latex(dividend)+f'=({divisor})({final})+({remainder})']
        explanation=(f'$x$ is the variable. Divide by $({divisor})$ using the leading terms. '
                     f'The quotient terms are ${a}x^2$, ${b}x$ and ${c}$. After each term, multiply it by the '
                     'whole divisor and subtract the whole product, including its signs. '
                     f'The final constant left is ${remainder}$, the remainder. '
                     'The last equation checks dividend = divisor × quotient + remainder; report both requested results.')
    elif skill == 'simplify_fraction_factorise':
        k,t=m['k'],m['m']; two=len(m['variables'])==2
        v=f'{t}y' if two else str(t)
        plus=f'(x+{v})';minus=f'(x-{v})';outside=f'{k}x^2' if two else f'{k}x'
        lines=[original+'='+frac(outside+plus,minus+plus),frac(outside+plus,minus+plus)+'='+frac(outside,minus)]
        explanation=(('$x$ and $y$ are variables. ' if two else '$x$ is the variable. ')
                     +f'The numerator has common factor ${outside}$, leaving ${plus}$. The denominator is a '
                     f'difference of squares, ${minus}{plus}$. Cancel only the matching factor ${plus}$; '
                     f'keep ${outside}$ and the other bracket ${minus}$.')
        domain=f'$x\\ne {v}$ and $x\\ne -{v}$'
    elif skill in ('single_fraction_linear','single_fraction_harder'):
        op='-' if m['subtract'] else '+'; sign=-1 if m['subtract'] else 1
        if skill=='single_fraction_linear':
            A,B=m['tops'];(a,b),(c,d)=m['dens']; left=linear_latex(a,b);right=linear_latex(c,d)
            den=f'({left})({right})'; numerator=f'{A}({right}) {op} {B}({left})'
            expanded=f'({A*c})x+({A*d}) {op} (({B*a})x+({B*b}))'
            restrictions=f'$x\\ne {num(Fraction(-b,a))}$ and $x\\ne {num(Fraction(-d,c))}$'
        elif m['form']=='x_over_x_plus_p':
            p,q=m['p'],m['q'];left=linear_latex(1,p);right='x';den=f'x({left})'
            numerator=f'x^2 {op} {q}({left})';expanded=f'x^2 {op} (({q})x+({q*p}))'
            restrictions=f'$x\\ne 0$ and $x\\ne {-p}$'
        else:
            p,u,v=m['p'],m['u'],m['v'];left=linear_latex(1,p);right=linear_latex(1,-p)
            den=f'({right})({left})';numerator=f'{u}({right}) {op} {v}'
            expanded=f'({u})x+({-u*p}) {op} {v}'
            restrictions=f'$x\\ne {p}$ and $x\\ne {-p}$'
        lines=[original+'='+frac(numerator,den),frac(numerator,den)+'='+frac(expanded,den)]
        explanation=(f'$x$ is the variable. Use ${den}$ as the common denominator. Multiply each numerator '
                     f'by the factor its denominator is missing, giving ${numerator}$. '
                     +('The subtraction applies to the whole second numerator: keep its bracket until every sign has been dealt with. '
                       if m['subtract'] else 'Expand the numerator products and collect like terms. ')
                     +'Write the result as one fraction and cancel any remaining common factor only when it multiplies the entire numerator and denominator.')
        domain=restrictions
    else:
        raise ValueError(skill)
    if domain:
        lines.append(r'\text{Original denominator restrictions: }'+domain.replace('$','').replace(' and ',r'\quad\text{and}\quad '))
        explanation+=f' The original denominators must stay nonzero: {domain}, even if a factor disappears during simplification.'
    return work(lines,problem.answer),explanation
