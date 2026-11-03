"""Equation solutions: Basics PDF pp.16–18; source-specific method restrictions retained."""
from fractions import Fraction
from .algebra_teaching import frac,num,work,expression_in,bracket
from .formatting import linear_latex,quadratic_latex

LABELS={1:'Solving linear equations with exact answers',2:'Equations on both sides and cost problems',
        3:'Solving equations containing fractions',4:'Solving simultaneous linear equations',
        5:'Solving simultaneous linear and quadratic equations'}
QUADRATIC_LABELS={1:'Solving equations already in factors',2:'Solving square equations with both roots',
                  3:'Rearranging and factorising monic quadratics',4:'Solving quadratics with a leading coefficient',
                  5:'Using the quadratic formula and interpreting context'}


def _two(a,b):
    return linear_latex(a,0)+(' + ' if b>0 else ' - ')+(str(abs(b)) if abs(b)!=1 else '')+'y'


def content(problem):
    m=problem.machine;task=m['task'];original=expression_in(problem.question)
    if task=='linear':
        a,b,c=m['a'],m['b'],m['c'];lines=[original,f'{a}x={c}-({b})={c-b}',f'x='+frac(c-b,a)]
        explanation=(f'$x$ is the unknown, its coefficient is ${a}$ and the added constant is ${b}$. '
                     f'Subtract ${b}$ from both sides, then divide both sides by ${a}$. '
                     'Keep an exact fraction when it does not simplify to a whole number. Substitute the answer into the original equation to check.')
    elif task=='linear_reversed':
        p,q,r=m['p'],m['q'],m['r'];lines=[original,f'{q}x={p}-({r})={p-r}',f'x='+frac(p-r,q)]
        explanation=(f'$x$ is the unknown. The original variable term is $-{q}x$. '
                     f'Add ${q}x$ to both sides and subtract ${r}$, leaving ${q}x={p-r}$. '
                     f'Divide by ${q}$ and retain the exact answer. Check the signs in the original equation.')
    elif task=='linear_both_sides':
        a,b,c,d=(m[k] for k in ('a','b','c','d'));lines=[original,f'({a}-({c}))x={d}-({b})',f'{a-c}x={d-b}',f'x='+frac(d-b,a-c)]
        explanation=(f'$x$ is the same unknown on both sides. Subtract ${c}x$ and ${b}$ from both sides. '
                     f'The resulting coefficient is ${a-c}$ and the number on the other side is ${d-b}$. '
                     'Divide only after collecting those terms. Moving a term is shorthand for applying the same operation to both sides.')
    elif task=='cost':
        count,price,unit,total=(m[k] for k in ('fixed_count','fixed_price','unit_price','total'));fixed=count*price
        lines=[f'n=\\text{{number of oranges}}',f'{count}({price})+{unit}n={total}',f'{unit}n={total}-{fixed}={total-fixed}',f'n='+frac(total-fixed,unit)]
        explanation=(f'$n$ is the unknown number of oranges. The fixed purchase costs N${fixed}, '
                     f'from ${count}$ items at N${price} each. Subtract that fixed cost from N${total}, '
                     f'then divide the remaining N${total-fixed} by N${unit} per orange. '
                     'An equation accounts for the fixed purchase; applying direct proportion to the whole bill would not.')
    elif task=='fraction_one':
        p,q,r=m['p'],m['q'],m['r'];lines=[original,f'{linear_latex(1,p)}={q}({r})={q*r}',f'x={q*r}-({p})']
        explanation=(f'$x$ is the unknown. Multiply both sides by the denominator ${q}$, keeping the whole numerator '
                     f'$({linear_latex(1,p)})$ together. Then subtract ${p}$ from both sides. '
                     'Multiplication clears the fraction; it does not multiply only one term of the numerator.')
    elif task=='fraction_coefficient':
        a,q,r=m['a'],m['q'],m['r'];lines=[original,frac(f'{a}x',q)+f'={r}',f'{a}x={q*r}',f'x='+frac(q*r,a)]
        explanation=(f'$x$ is the unknown. Add ${r}$ to both sides, multiply both sides by ${q}$, '
                     f'then divide by ${a}$. Carry out those inverse operations in order and check by substitution.')
    elif task=='constant_over_linear':
        a,p,q,d=(m[k] for k in ('a','p','q','d'));den=linear_latex(p,q)
        lines=[original,f'{a}={d}({den})',f'{den}='+frac(a,d),f'{p}x='+frac(a,d)+f'-({q})']
        explanation=(f'$x$ occurs inside the denominator $({den})$, which must be nonzero. '
                     f'Multiply both sides by that entire denominator, then divide by ${d}$. '
                     f'Subtract ${q}$ and divide by ${p}$ to isolate $x$. Check that the result does not make the original denominator zero.')
    elif task=='fraction_two':
        a,b,u,v=m['a'],m['b'],m['m'],m['n'];total=Fraction(*m['total']);common=u*v;rhs=total*common
        lines=[original,f'{v}({linear_latex(1,a)})+{u}({linear_latex(1,b)})={num(rhs)}',
               f'{u+v}x+({v*a+u*b})={num(rhs)}',f'{u+v}x={num(rhs-v*a-u*b)}']
        explanation=(f'$x$ is the unknown. A common denominator is ${common}$. Multiply every term on both sides '
                     f'by ${common}$, leaving multipliers ${v}$ and ${u}$ on the two numerator brackets. '
                     'Expand the whole brackets, collect the unknown terms, then divide by their combined coefficient. '
                     'Do not add denominators or discard signs.')
    elif task=='simultaneous_linear':
        a,b,c=m['eq1'];d,e,f=m['eq2'];x,y=m['solution'];det=a*e-d*b;rhs=c*e-f*b
        lines=[f'{_two(a,b)}={c}',f'{_two(d,e)}={f}',
               f'{_two(a*e,b*e)}={c*e}',f'{_two(d*b,e*b)}={f*b}',
               f'({det})x={rhs}',f'x={x}',f'({a})({x})+({b})y={c}',f'y='+frac(c-a*x,b),
               f'({d})({x})+({e})({y})={f}']
        explanation=(f'$x$ and $y$ must satisfy both equations. Multiply the first equation by ${e}$ and the second '
                     f'by ${b}$, making the $y$ coefficients equal. Subtract the second scaled equation from the first; '
                     f'this gives $({det})x={rhs}$. With $x={x}$, substitute into the first equation to get $y={y}$. '
                     'The last line checks the pair in the other original equation. Other valid methods, including substitution, also work.')
    elif task=='simultaneous_line_curve':
        k,s,t=m['k'],m['m'],m['n'];(x1,y1),(x2,y2)=m['solutions']
        curve=quadratic_latex(1,0,k);line=linear_latex(s,t)
        lines=[f'y={curve}',f'y={line}',f'{curve}={line}',f'{quadratic_latex(1,-s,k-t)}=0',
               f'{bracket(1,-x1)}{bracket(1,-x2)}=0',f'x={x1}\\quad\\text{{or}}\\quad x={x2}',
               f'x={x1}:\\quad y=({x1})^2+({k})={y1}',f'x={x2}:\\quad y=({x2})^2+({k})={y2}']
        explanation=(f'$x$ and $y$ are the coordinates satisfying both equations. Write the line as $y={line}$ '
                     f'and substitute it into $y={curve}$. Solve the resulting quadratic for both $x$ values. '
                     f'Here $x={x1}$ belongs with $y={y1}$, and $x={x2}$ with $y={y2}$. '
                     'Keep each pair together and check it in both original equations; two unpaired lists are incomplete.')
    else:raise ValueError(task)
    return work(lines,problem.answer),explanation


def quadratic_content(problem):
    m=problem.machine;task=m['task'];v=m.get('var','x');original=expression_in(problem.question)
    if task in ('solve_factorised','solve_by_factorising_monic','solve_by_factorising_general'):
        if task=='solve_by_factorising_monic':
            r,s=m['r'];factors=[(1,-r),(1,-s)];a,b,c=1,-r-s,r*s
        else:
            factors=m['factors'];(a1,b1),(a2,b2)=factors;a,b,c=a1*a2,a1*b2+a2*b1,b1*b2
        (u,w),(s,t)=factors
        lines=[original]
        if task!='solve_factorised':
            lines.extend([f'{quadratic_latex(a,b,c,v)}=0',f'{bracket(u,w,v)}{bracket(s,t,v)}=0'])
        lines.extend([f'{linear_latex(u,w,v)}=0\\quad\\text{{or}}\\quad {linear_latex(s,t,v)}=0',
                      f'{v}={num(Fraction(-w,u))}\\quad\\text{{or}}\\quad {v}={num(Fraction(-t,s))}'])
        explanation=(f'${v}$ is the unknown. '+('Use the brackets already given. ' if task=='solve_factorised' else 'Rearrange to zero before factorising. ')
                     +f'A product is zero when at least one factor is zero. Set ${linear_latex(u,w,v)}=0$ '
                     f'or ${linear_latex(s,t,v)}=0$ and solve each linear equation. '
                     'Give both roots, keeping exact fractions. Do not divide by a variable factor and lose a possible zero root.')
    elif task=='solve_square':
        a,k=m['a'],m['k'];value=Fraction(k,a)
        lines=[original,f'{v}^2={num(value)}',f'{v}=\\pm\\sqrt{{{num(value)}}}']
        explanation=(f'${v}$ is the unknown and ${a}$ multiplies its square. Divide by ${a}$ first, '
                     f'giving ${v}^2={num(value)}$. Both the positive and negative square root satisfy the equation. '
                     'The square-root symbol itself denotes the nonnegative root; the plus/minus supplies both equation solutions.')
    elif task in ('quadratic_formula','quadratic_context_length'):
        contextual=task=='quadratic_context_length'
        a,b,c=(1,m['k'],-m['area']) if contextual else m['abc'];disc=m['disc']
        lines=[]
        if contextual:lines.append(f'x(x+{b})={m["area"]}')
        lines.extend([f'{quadratic_latex(a,b,c,v)}=0',
                      f'a={a},\\quad b={b},\\quad c={c}',
                      f'b^2-4ac=({b})^2-4({a})({c})={disc}',
                      f'{v}='+frac(f'-({b})\\pm\\sqrt{{{disc}}}',f'2({a})')])
        explanation=(f'${v}$ is '+('the field width in metres. Length × width gives the area equation. ' if contextual else 'the unknown. ')
                     +f'In $a{v}^2+b{v}+c=0$, the coefficient values are $a={a}$, $b={b}$ and $c={c}$. '
                     +f'The quadratic formula is ${v}='+frac('-b\\pm\\sqrt{b^2-4ac}','2a')+'$. '
                     'Bracket every substituted negative coefficient, square $b$ before subtracting $4ac$, and apply the denominator to the whole numerator. '
                     +('The minus choice gives a negative width, which is impossible for this field. Keep the positive root and round to three significant figures.' if contextual
                       else 'Evaluate both plus and minus choices without rounding intermediate results; round the final roots to two decimal places.'))
        if contextual:lines.append(r'x>0\quad\text{(width in metres)}')
    else:raise ValueError(task)
    return work(lines,problem.answer),explanation
