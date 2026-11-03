"""Base-10 logarithms: NSSCO syllabus p.20; local logs notes and exam evidence."""
from fractions import Fraction
import re
from .algebra_teaching import frac,num,work,expression_in
from .formatting import linear_latex

LABELS={1:'Evaluating logarithms of powers of ten',2:'Splitting logarithms and using a given logarithm',
        3:'Combining expressions into one logarithm',4:'Solving exponential equations with logarithms',
        5:'Solving exponential equations with several operations'}


def content(problem):
    m=problem.machine;task=m['task'];original=expression_in(problem.question)
    base='Here $\\log$ means logarithm to base $10$: it gives the exponent needed on $10$.'
    if task=='evaluate_log':
        exponents=[int(step.value) for step in problem.steps[:-1]]
        if m['shape']=='multiple':
            a=exponents[0];coefficient=int(re.match(r'(\d+)',original)[1])
            lines=[f'10^{{{a}}}={num(Fraction(10)**a)}',f'\\log(10^{{{a}}})={a}',f'{coefficient}\\log(10^{{{a}}})={coefficient}({a})']
        else:
            a,b=exponents[:2];op='+' if m['shape']=='sum' else '-'
            lines=[f'10^{{{a}}}={num(Fraction(10)**a)},\\quad10^{{{b}}}={num(Fraction(10)**b)}',
                   original+f'=({a}){op}({b})']
        explanation=base+' Rewrite each number as a power of $10$, then use its exponent as the logarithm value. '
        explanation+='Keep any negative exponent and carry out the addition, subtraction or outside multiplication as written. Show these steps because the question requests working.'
    elif task=='log_in_terms_of_m':
        p=m['p'];c=num(m['coefficient']);original=re.findall(r'\$([^$]+)\$',problem.question)[1]
        lines=[original+f'=\\log({p}^{{{c}}})',f'={c}\\log {p}',f'=({c})m']
        explanation=(base+f' In this question $m$ names the given value $\\log {p}$; it is not a new logarithm argument. '
                     f'Rewrite the argument using powers of ${p}$. The net exponent is ${c}$, so the power law '
                     f'gives $({c})\\log {p}=({c})m$. Roots give fractional exponents, and denominator powers are subtracted. '
                     'Replace the given logarithm by $m$, not by $\\log m$.')
    elif task=='split_log':
        k=m['k'];form=m['form']
        if form=='k x^n':
            n=m['n'];lines=[original+f'=\\log {k}+\\log(x^{n})',f'=\\log {k}+{n}\\log x']
            detail=f'The constant factor is ${k}$ and the power on $x$ is ${n}$.'
        elif form=='k sqrt(x)':
            lines=[original+f'=\\log {k}+\\log(x^{{1/2}})',f'=\\log {k}+\\frac12\\log x']
            detail=f'The constant factor is ${k}$, and $\\sqrt{{x}}=x^{{1/2}}$.'
        else:
            n=m['n'];lines=[original+f'=\\log(x^{n})-\\log {k}',f'={n}\\log x-\\log {k}']
            detail=f'The numerator power is ${n}$ and the denominator constant is ${k}$.'
        explanation=(base+' $x$ is the variable. '+detail+
                     ' For the separate-log form shown, $x>0$ is required. Products inside a logarithm become sums; '
                     'quotients become differences; a power becomes a multiplier of the logarithm. '
                     'These rules do not split a sum inside a logarithm.')
    elif task=='combine_logs':
        form=m['form']
        if form=='log a + log b - log c':
            a,b,c=m['a'],m['b'],m['c'];lines=[original+''.join(['=\\log\\left(', format(frac(''.join([format(a, ''), '\\times', format(b, '')]), c), ''), '\\right)'])]
            detail=f'The logarithm arguments are ${a}$, ${b}$ and ${c}$. Multiply the first two and divide by the third.'
        elif form=='p log x + q log y - log z':
            p,q=m['p'],m['q'];lines=[original+f'=\\log(x^{p})+\\log(y^{q})-\\log z',f'=\\log\\left({frac(f"x^{p}y^{q}","z")}\\right)']
            detail=f'$x$, $y$ and $z$ are positive variables. The multipliers ${p}$ and ${q}$ become powers inside their logarithms.'
        else:
            c,n,t=m['constant'],m['n'],m['t'];ten=10**c
            lines=[f'{c}=\\log {ten}',original+f'=\\log {ten}+\\log(x^{n})+\\log(x+{t})',f'=\\log({ten}x^{n}(x+{t}))']
            detail=f'$x$ is positive. The constant ${c}$ is $\\log {ten}$, and the multiplier ${n}$ becomes a power of $x$. Keep $(x+{t})$ intact.'
        explanation=(base+' '+detail+' Additions of logarithms become products of their arguments; '
                     'subtractions become quotients. The requested final form is one logarithm. '
                     'A sum inside a logarithm cannot be split into a sum of logarithms.')
    elif task=='solve_exponential':
        a,c=m['a'],m['c'];form=m['form'];p=m.get('p',1);q=m.get('q',m.get('b',0));k=m.get('k',1)
        rhs=num(Fraction(str(c))/k);exponent=linear_latex(p,q)
        lines=[original]
        if k!=1:lines.append(f'{a}^x={rhs}')
        lines.extend([f'({exponent})\\log {a}=\\log({rhs})',
                      f'{exponent}='+frac(f'\\log({rhs})',f'\\log {a}')])
        exact=frac(frac(f'\\log({rhs})',f'\\log {a}')+f'-({q})',p)
        lines.append(f'x={exact}')
        lines.append(f'x\\approx {m["x"]:.10g}\\ldots')
        explanation=(base+f' $x$ is the unknown exponent and ${a}$ the exponential base. '
                     +(f'Divide both sides by the outside multiplier ${k}$ before taking logarithms. ' if k!=1 else '')
                     +f'Take logarithms of both sides; the whole exponent $({exponent})$ becomes the multiplier of $\\log {a}$. '
                     f'Divide by $\\log {a}$, then undo the remaining linear operations. '
                     'Keep calculator precision during the calculation and round only the final answer to the requested three significant figures.')
    else:raise ValueError(task)
    return work(lines,problem.answer),explanation
