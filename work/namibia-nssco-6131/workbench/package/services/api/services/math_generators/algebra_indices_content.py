"""Indices and inequalities: syllabus p.19, Basics indices/inequations sections."""
from .algebra_teaching import frac,num,work,expression_in
from .formatting import linear_latex

LABELS={1:'Multiplying, dividing and raising powers',2:'Roots, negative powers and algebraic products',
        3:'Writing and solving a simple inequality',4:'Inequalities with brackets, two sides or two bounds',
        5:'Combining powers and solving exponential equations'}
OPS={'<':'<','>':'>','<=':r'\le','>=':r'\ge'}


def content(problem):
    m=problem.machine;task=m['task'];original=expression_in(problem.question)
    if task in ('index_multiply','index_divide','index_power'):
        v,a,b=m['var'],m['m'],m['n'];op={'index_multiply':'+','index_divide':'-','index_power':r'\times'}[task]
        lines=[original+f'={v}^{{{a}{op}{b}}}',f'{v}^{{{a}{op}{b}}}={v}^{{{m["result"]}}}']
        rule={'index_multiply':'Multiplying powers with the same base adds their exponents.',
              'index_divide':'Dividing powers with the same nonzero base subtracts the denominator exponent.',
              'index_power':'Raising a power to another power multiplies the exponents.'}[task]
        explanation=(f'${v}$ is the base; ${a}$ and ${b}$ are the exponents shown. '+rule+
                     f' Here the exponent calculation is ${a}{op}{b}={m["result"]}$. Keep the base ${v}$ unchanged.')
    elif task in ('evaluate_fractional','evaluate_fractional_power'):
        base,n,b=m['base'],m['n'],m['b'];power=m.get('m',1)
        root=f'\\sqrt[{n}]{{{base}}}'
        lines=[root+f'={b}',original+f'=({root})^{{{power}}}={b}^{{{power}}}']
        explanation=(f'The base is ${base}$. The denominator ${n}$ of the fractional exponent tells us to take the '
                     f'${n}$th root: ${root}={b}$. The numerator ${power}$ tells us the power to apply afterwards. '
                     'Enter the entire fractional exponent in brackets on a calculator; dividing the base by the denominator is a different calculation.')
    elif task=='evaluate_negative':
        b,k=m['b'],m['k'];lines=[original+'='+frac(1,f'{b}^{k}')+'='+frac(1,b**k)]
        explanation=(f'The base is ${b}$ and the exponent is $-{k}$. A negative exponent means take the reciprocal, '
                     f'not make the answer negative. First calculate ${b}^{k}={b**k}$, then write $1/{b**k}$.')
    elif task=='power_of_product':
        u,v=m['vars'];c,k,a,b=m['c'],m['k'],m['a'],m['b']
        lines=[original+f'={c}^{k}{u}^{{{a}\\times{k}}}{v}^{{{b}\\times{k}}}']
        explanation=(f'${u}$ and ${v}$ are variables. The outside power ${k}$ applies to every factor: '
                     f'the number becomes ${c}^{k}={c**k}$, and the letter exponents become '
                     f'${a}\\times{k}={a*k}$ and ${b}\\times{k}={b*k}$. Multiply nested exponents; do not add them.')
    elif task=='product_of_terms':
        u,v=m['vars'];a,b,c,d=m['exps'];c1,c2=m['c1'],m['c2']
        lines=[original+f'=({c1}\\times{c2}){u}^{{{a}+{c}}}{v}^{{{b}+{d}}}']
        explanation=(f'${u}$ and ${v}$ are different bases. Multiply the numerical coefficients: '
                     f'${c1}\\times{c2}={c1*c2}$. Add exponents only within each base: '
                     f'${a}+{c}={a+c}$ for ${u}$, and ${b}+{d}={b+d}$ for ${v}$. Do not merge the two letters into one exponent.')
    elif task=='divide_terms':
        v=m['var'];c1,c2,e1,e2=(m[k] for k in ('c1','c2','e1','e2'))
        lines=[original+'='+frac(c1,c2)+f'{v}^{{{e1}-{e2}}}']
        explanation=(f'${v}$ is the common base, with ${v}\\ne0$ in the original fraction. Divide the coefficients '
                     f'${c1}/{c2}={num(c1//c2)}$ and subtract exponents ${e1}-{e2}={e1-e2}$. The coefficient and the exponent use different operations.')
    elif task.startswith('inequality'):
        if task=='inequality_double':
            v,k,c,lo,hi=(m[key] for key in ('var','m','n','lo','hi'));left,right=map(OPS.get,m['ops'])
            lines=[original,f'{lo*k} {left} {k}{v} {right} {hi*k}',f'{lo} {left} {v} {right} {hi}']
            explanation=(f'${v}$ is the unknown. Subtract ${c}$ from all three parts, then divide all three by '
                         f'the positive coefficient ${k}$. Both inequalities must hold together; the answer is the interval '
                         f'between ${lo}$ and ${hi}$, keeping each strict or inclusive end as written.')
        else:
            op=OPS[m['op']]
            if task=='inequality_basic':
                a,b,c=m['a'],m['b'],m['c'];coef=a;constant=c-b
                lines=[original,f'{a}x {op} {constant}']
                method=f'Subtract ${b}$ from both sides.'
            elif task=='inequality_form_solve':
                a,b,c=m['a'],m['bb'],m['c'];coef=a;constant=c+b
                lines=[f'{a}x-{b} {op} {c}',f'{a}x {op} {constant}']
                method=f'Translate the wording first, then add ${b}$ to both sides. “More than” is strict; “at least” includes equality.'
            else:
                a,b,c,d=(m[k] for k in ('a','b','c','d'));coef=a-c
                constant=d-a*b if task=='inequality_brackets' else d-b
                lines=[original]
                if task=='inequality_brackets':lines.append(f'{linear_latex(a,a*b)} {op} {linear_latex(c,d)}')
                lines.append(f'({coef})x {op} {constant}')
                method='Expand any bracket, then collect the unknown terms on one side and the numbers on the other.'
            explanation=(f'$x$ is the unknown. '+method+f' The coefficient to divide by is ${coef}$. '
                         +('It is negative, so reverse the inequality sign when dividing.' if coef<0 else 'It is positive, so keep the inequality sign when dividing.')
                         +' Retain an inequality in the answer; an equation describes only its boundary.')
    elif task=='numeric_index':
        b,a1,a2,c=m['b'],m['a1'],m['a2'],m['c']
        numerator=linear_latex(2,a1-a2);denominator=linear_latex(2,-c)
        lines=[original+f'={b}^{{({numerator})-({denominator})}}',f'={b}^{{{a1-a2+c}}}']
        explanation=(f'$x$ is the exponent variable and ${b}$ is the common base. Add the two numerator exponents, '
                     f'giving ${numerator}$. Subtract the entire denominator exponent $({denominator})$. '
                     f'The $x$ terms cancel and the exponent becomes ${a1-a2+c}$, so the result is a number.')
    elif task=='single_power':
        p,q,r=m['p'],m['q'],m['r']
        lines=[original+f'=5^{{{3*p}x}}\\times5^{{{2*q}y}}\\div5^{{{r}x}}',
               f'=5^{{({3*p}-{r})x+{2*q}y}}']
        explanation=(f'$x$ and $y$ are variables in the exponents. Use $125=5^3$ and $25=5^2$. '
                     f'The numerator powers become ${3*p}x$ and ${2*q}y$; division subtracts ${r}x$. '
                     f'The final exponent is ${m["ex"]}x+{m["ey"]}y$. Keep the answer as a single power of $5$.')
    elif task=='exponential_simple':
        b,k=m['b'],m['k'];lines=[original,f'{b}^x={b}^{{{k}}}',f'x={k}']
        explanation=(f'$x$ is the unknown exponent. Rewrite the right side as ${b}^{k}$. '
                     f'Equal powers with the same positive base ${b}\\ne1$ have equal exponents, so $x={k}$.')
    elif task=='exponential_linear':
        b,p,q,r=(m[k] for k in ('b','p','q','r'))
        lines=[original,f'{b}^{{{linear_latex(p,q)}}}={b}^{r}',f'{linear_latex(p,q)}={r}',f'{p}x={r-q}']
        explanation=(f'$x$ is the unknown in the exponent. Rewrite the right side with base ${b}$, giving exponent ${r}$. '
                     f'Equate the whole exponent ${linear_latex(p,q)}$ to ${r}$, then solve the resulting linear equation.')
    else:raise ValueError(task)
    return work(lines,problem.answer),explanation
