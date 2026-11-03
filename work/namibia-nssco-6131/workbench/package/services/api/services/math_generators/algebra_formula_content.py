"""Formulae/substitution/variation: Basics PDF pp.12–13,15–16,28."""
import re
from .algebra_teaching import frac, work, expression_in
from .formatting import linear_latex

LABELS={1:'Collecting terms and simplifying expressions',2:'Substituting values, including negatives',
        3:'Rearranging linear and fractional formulae',4:'Finding and using variation equations',
        5:'Rearranging formulae containing square roots'}


def content(problem):
    m=problem.machine;task=m['task'];lines=[]
    if task=='collect_like_terms':
        terms=m['terms'];letters=sorted({v for _,v in terms})
        grouped=[f"({' + '.join(f'({c})' for c,v in terms if v==letter)}){letter}" for letter in letters]
        lines=[expression_in(problem.question)+'='+' + '.join(grouped)]
        explanation=(' and '.join(f'${v}$' for v in letters)+' are variables. '
                     +'Collect only terms with the same letter and power. The signed coefficient sums here are '
                     +'; '.join(f"${' + '.join(f'({c})' for c,v in terms if v==letter)}={sum(c for c,v in terms if v==letter)}$ for ${letter}$" for letter in letters)
                     +'. The letters themselves stay in the expression; they are not given numerical values.')
    elif task=='expand_and_simplify':
        k=m['m'];a,b=m['bracket'];c,d=m['extra']
        lines=[expression_in(problem.question)+f'=({k*a})a+({k*b})b+({c})a+({d})b',
               f'=({k*a}+({c}))a+({k*b}+({d}))b']
        explanation=(f'$a$ and $b$ are variables. The outside multiplier ${k}$ multiplies both terms, giving '
                     f'coefficients ${k*a}$ and ${k*b}$. Then combine the $a$ coefficients ${k*a}$ and ${c}$, '
                     f'and separately the $b$ coefficients ${k*b}$ and ${d}$. Keep the signs of the extra terms.')
    elif task=='substitute':
        form=m['form']
        if form=='a^2 - kb':
            a,b,k=m['a'],m['b'],m['k'];expr=f'a^2-{k}b';sub=f'({a})^2-({k})({b})';calc=f'{a*a}-{k*b}'
            names=f'$a={a}$ and $b={b}$; the multiplier of $b$ is ${k}$.'
        elif form=='kx + my':
            x,y,k,t=m['x'],m['y'],m['k'],m['m'];expr=f'{k}x+{t}y';sub=f'({k})({x})+({t})({y})';calc=f'{k*x}+({t*y})'
            names=f'$x={x}$ and $y={y}$; their multipliers are ${k}$ and ${t}$.'
        else:
            u,a,t=m['u'],m['a'],m['t'];expr='v';sub=f'({u})+({a})({t})';calc=f'({u})+({a*t})'
            names=f'$v$ is the requested value. In $v=u+at$, $u={u}$, $a={a}$ and $t={t}$.'
        lines=[f'{expr}={sub}',f'={calc}']
        explanation=(names+' Replace each letter by its given number, using brackets around negative values. '
                     'Evaluate powers first, then products, then addition or subtraction. '
                     'A negative value squared is positive; a negative value multiplied by a positive value stays negative.')
    elif task=='change_subject':
        letters=m['letters'];form=m['form']
        equation=re.findall(r'\$([^$]+)\$',problem.question)[1]
        if form=='P = A + BC':
            P,A,B,C=letters;target=C
            lines=[equation,f'{P}-{A}={B}{C}',f'{C}='+frac(f'{P}-{A}',B)]
            method=f'Subtract ${A}$ from both sides, then divide the whole difference by ${B}$. The denominator ${B}$ must be nonzero.'
        elif form=='P = k(A + B)':
            P,A,B=letters;k=m['k'];target=A
            lines=[equation,frac(P,k)+f'={A}+{B}',f'{A}='+frac(P,k)+f'-{B}']
            method=f'Divide both sides by the outside multiplier ${k}$ first. Then subtract ${B}$.'
        elif form=='P = A/B + C':
            P,A,B,C=letters;target=B
            lines=[equation,f'{P}-{C}='+frac(A,B),f'{B}({P}-{C})={A}',f'{B}='+frac(A,f'{P}-{C}')]
            method=f'Subtract ${C}$ first, then multiply both sides by ${B}$. Divide by the entire bracket $({P}-{C})$, which must be nonzero. The original denominator ${B}$ must also be nonzero.'
        elif form=='t = k sqrt(y)':
            T,Y=letters;target=Y;factor=equation.split('=')[1].split(r'\sqrt')[0].strip()
            lines=[equation,frac(T,factor)+f'=\\sqrt{{{Y}}}',f'{Y}=\\left({frac(T,factor)}\\right)^2']
            method=f'Divide both sides by ${factor}$, then square the whole quotient. Squaring applies to the whole denominator too. The original square root requires ${Y}\\ge0$ and the quotient to be nonnegative.'
        elif form=='A = sqrt((B - C)/D)':
            A,B,C,D=letters;target=B
            lines=[equation,f'{A}^2='+frac(f'{B}-{C}',D),f'{D}{A}^2={B}-{C}',f'{B}={D}{A}^2+{C}']
            method=f'Square both sides, multiply by ${D}$, then add ${C}$. The original root is nonnegative, so ${A}\\ge0$, and ${D}\\ne0$.'
        else:
            A,B,C,D=letters;k=m['k'];target=B
            lines=[equation,f'{A}^2='+frac(f'{k}({B}+{C})',D),f'{D}{A}^2={k}({B}+{C})',
                   frac(f'{D}{A}^2',k)+f'={B}+{C}',f'{B}='+frac(f'{D}{A}^2',k)+f'-{C}']
            method=f'Square both sides, multiply by ${D}$, divide by ${k}$, then subtract ${C}$. The original root requires ${A}\\ge0$ and ${D}\\ne0$.'
        explanation=(f'${target}$ is the subject we want on its own; '+', '.join(f'${v}$' for v in letters if v!=target)
                     +' are the other quantities in the formula. No numerical values are supplied for them. '
                     +method+' Apply each operation to both sides. Leave a formula in the given letters rather than inserting invented numbers.')
    elif task in ('variation_equation','variation_value'):
        y,x=re.findall(r'\$([^$]+)\$',problem.question)[:2];x0,y0=m['given'];k=m['k'];key=m['key']
        if key=='square':
            factor=f'{x}^2';givenfactor=f'({x0})^2';find=frac(y0,givenfactor);relation=f'{y}=k{factor}';equation=f'{y}={k}{factor}'
        elif key=='root':
            factor=f'\\sqrt{{{x}}}';givenfactor=f'\\sqrt{{{x0}}}';find=frac(y0,givenfactor);relation=f'{y}=k{factor}';equation=f'{y}={k}{factor}'
        else:
            power=3 if key=='inverse_cube' else 2;factor=f'{x}^{power}';givenfactor=f'({x0})^{power}';find=f'({y0}){givenfactor}';relation=f'{y}='+frac('k',factor);equation=f'{y}='+frac(k,factor)
        lines=[relation,f'k={find}={k}',equation]
        if 'ask' in m:
            x1=m['ask']
            value={'square':f'{k}({x1})^2','root':f'{k}\\sqrt{{{x1}}}',
                   'inverse_square':frac(k,f'({x1})^2'),'inverse_cube':frac(k,f'({x1})^3')}[key]
            lines.append(f'{x}={x1}\\quad\\Rightarrow\\quad {y}={value}')
        explanation=(f'${y}$ is the dependent quantity and ${x}$ the quantity it varies with. '
                     f'$k$ is the constant of proportionality. The given pair is ${x}={x0}$, ${y}={y0}$. '
                     f'Use the stated square, root or reciprocal relationship ${relation}$, then substitute that pair to find $k={k}$. '
                     'Replace $k$ by its numerical value in the equation. '
                     +('Use the new input only after finding that constant. ' if 'ask' in m else 'The requested answer is the connecting equation, not just the value of $k$. ')
                     +('For an inverse relationship the denominator cannot be zero.' if key.startswith('inverse') else 'Keep the stated power or root; simple direct proportion would describe a different relationship.'))
    else:
        raise ValueError(task)
    return work(lines,problem.answer),explanation
