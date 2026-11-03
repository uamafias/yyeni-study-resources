"""Set calculations and graph properties from the existing text-described tasks."""
import re
from math import isqrt
from .topic_teaching import *
from .family_sets_graphs import _TWO_SET_EXPRS,_THREE_SET_EXPRS,_lx,_eval_set,_members

LABELS={
'nssco_defining_sets_notation':{1:'Listing a set from its description',2:'Combining sets and taking complements',3:'Using membership, subsets and cardinality'},
'nssco_venn_diagrams':{1:'Counting two-set regions',2:'Finding an overlap',3:'Combining three listed sets',4:'Probabilities from set regions'},
'nssco_linear_programming':{1:'Writing a condition as an inequality',2:'Testing points against all conditions',3:'Combining three constraints',4:'Comparing an objective at vertices'},
'nssco_quadratic_graphs':{1:'Calculating quadratic table values',2:'Finding axis intercepts',3:'Finding a turning point or symmetry axis',4:'Solving equations and quadratic sign conditions'},
'nssco_sketching_quadratics_gradients':{1:'Finding intercepts for a sketch',2:'Reading a turning point from square form',3:'Calculating a turning point',4:'Chord gradients and turning-point tangents'},
'nssco_advanced_graphs':{1:'Evaluating reciprocal functions',2:'Evaluating cubic functions',3:'Evaluating exponential functions',4:'Identifying asymptotes',5:'Solving reciprocal, cubic and exponential equations'},
}


def set_tex(values):return r'\{'+', '.join(map(str,sorted(values)))+r'\}' if values else r'\varnothing'


def set_rows(p):
    m=p.machine;universe_text=re.search(r'\\xi = \\\{(.*?)\\\}',p.question)[1]
    universe=list(map(int,re.findall(r'\d+',universe_text)));members=_members(universe,m['sets'])
    tree=next(t for t in (*_TWO_SET_EXPRS,*_THREE_SET_EXPRS) if _lx(t)==m['expression'])
    lines=[]
    def visit(t):
        if t[0]=='set':return
        for child in t[1:]:visit(child)
        row=_lx(t)+'='+set_tex(_eval_set(t,universe,members))
        if row not in lines:lines.append(row)
    visit(tree)
    if m['task']=='set_count':lines.append('n('+m['expression']+')='+str(len(_eval_set(tree,universe,members))))
    return lines,len(universe)


def roots(a,b,c):
    disc=b*b-4*a*c;r=isqrt(disc)
    if r*r!=disc:raise ValueError('Expected exact constructed quadratic roots')
    return sorted([F(-b-r)/(2*a),F(-b+r)/(2*a)])


def poly_at(coefficients,x):
    degree=len(coefficients)-1
    return '+'.join(f'({q(a)})({q(x)})'+(f'^{{{degree-i}}}' if degree-i else '') if degree-i else f'({q(a)})' for i,a in enumerate(coefficients) if a) or '0'


def poly_value(coefficients,x):
    value=F(0)
    for a in coefficients:value=value*x+F(a)
    return value


def content(p):
    if p.generator_id not in LABELS:return None
    m=p.machine;t=m['task'];lines=[];gid=p.generator_id
    if gid=='nssco_defining_sets_notation':
        if t.startswith('list_'):
            values=m['elements'];lines=[set_tex(values)]
            method={'list_natural':'Natural numbers start at 1 in this question. Include every positive integer below the stated upper limit.', 'list_multiples':'Generate successive positive multiples of the stated number, stopping before the strict upper limit.', 'list_primes':'A prime is greater than 1 and has exactly two positive divisors. Test possible prime divisors; 1 is not prime.', 'list_factors':'A positive factor divides the given integer with no remainder. Check factor pairs and include 1 and the integer itself.', 'list_squares':'Square successive positive integers and stop before the stated upper limit.'}[t]
            e=method+f' The qualifying elements here are ${set_tex(values)}$. List each once inside set braces; the order of elements does not change a set.'
        elif t in ('set_list','set_count'):
            lines,total=set_rows(p);e=f'The universal set $\\xi$ has ${total}$ elements and bounds every complement. $A$ and $B$ are the given sets. $\\cup$ means in either set (or both), $\\cap$ means in both, and a prime means the elements of $\\xi$ outside the whole bracketed set. Work from the innermost brackets. '+('The final $n$ asks for the number of qualifying elements, not their list.' if t=='set_count' else 'Write the qualifying elements once each; do not count them instead of listing them.')
        elif t=='cardinality':
            name=re.search(r'\$([A-Z]) =',p.question)[1];lines=[f'n({name})={len(m["elements"])}'];e=f'$n({name})$ means the number of distinct members of {name}. Here the given members are ${set_tex(m["elements"])}$, so count each once. Cardinality is a number, whereas {name} itself is a set written inside braces.'
        else:
            lines=[authored_math(p.steps[0].value).replace('∉',r'\notin ').replace('∈',r'\in ').replace('⊂',r'\subset ')]
            e={'subset':'The first named set is contained in the second: every member of the smaller set is also a member of the larger set. Use a subset relation between two sets, not a membership sign for a single element.', 'element':'The named number occurs in the displayed set, so use the element-of symbol. This relates one element to a set, not one set to another.', 'not_element':'The named number does not occur anywhere in the displayed set, so use the not-an-element symbol. Do not confuse absence of an element with one set not being a subset of another.'}[m['relation']]
    elif gid=='nssco_venn_diagrams':
        if t=='three_set_list':
            lines,total=set_rows(p);e=f'The universal set contains ${total}$ elements. A, B and C are the listed sets, not their sizes. Evaluate the bracketed union/intersection first, take any complement relative to $\\xi$, then apply the outer operation. The working lists the actual elements at each stage; retain a member only when it satisfies the whole expression.'
        else:
            a,b,both,d=(m[k] for k in ('only_a','only_b','both','neither'));total=a+b+both+d
            lines=[f'n(A\\setminus B)={a}',f'n(A\\cap B)={both}',f'n(B\\setminus A)={b}',f'n(\\xi)={a}+{both}+{b}+{d}={total}']
            if t=='find_both':lines.extend([f'n(A\\cup B)={total}-{d}={total-d}',f'n(A\\cap B)={a+both}+{b+both}-{total-d}={both}'])
            else:
                ask=m['ask'];v={'only_a':a,'both':both,'sb':b+both,'neither':d,'not_b':a+d,'union':a+b+both}[ask]
                formula={'only_a':f'{a+both}-{both}','both':str(both),'sb':f'{b}+{both}','neither':f'{total}-({a}+{both}+{b})','not_b':f'{a}+{d}','union':f'{a}+{both}+{b}'}[ask]
                lines.append(label('Requested region count')+'='+formula+f'={v}')
                if t=='venn_probability':lines.append('P='+frac(v,total))
            e=f'$A$ is the first subject group, $B$ the second and $\\xi$ the whole class of ${total}$. Their exclusive regions contain ${a}$ in A only, ${both}$ in both, ${b}$ in B only and ${d}$ in neither. The overlap belongs to both subject totals but is counted only once in a union. '+('Use $n(A\\cap B)=n(A)+n(B)-n(A\\cup B)$ to recover the overlap.' if t=='find_both' else 'Select the regions matching the requested group, including neither when asking for learners not in a subject.')+(' A random learner is chosen from the whole class, so divide the favourable count by the whole class size, not by the union.' if t=='venn_probability' else '')
    elif gid=='nssco_linear_programming':
        if t=='test_points':
            total,a,b=m['limits'];good=0
            for x,y in m['points']:
                passes=x+y<=total and x>=a and y>=b;good+=passes
                lines.append(f'({x},{y}):\\quad {x}+{y}={x+y},\\quad '+label('passes all' if passes else 'fails a condition'))
            lines.append(label('Number satisfying all three')+f'={good}')
            e=f'$x$ and $y$ are the coordinates of each candidate point. It must satisfy $x+y\\le{total}$, $x\\ge{a}$ and $y\\ge{b}$ simultaneously. Substitute both coordinates into every condition. The non-strict signs include boundary points; passing only one or two conditions is insufficient.'
        elif t=='best_value':
            a,b=m['objective']
            for x,y in m['vertices']:lines.append(f'P({x},{y})={a}({x})+{b}({y})={a*x+b*y}')
            e=f'$P$ is the objective value; $x$ and $y$ are the two quantities in the feasible region. Here $P={a}x+{b}y$. For this bounded polygon and linear objective, compare the values at every listed vertex, then choose the '+('greatest' if m['greatest'] else 'least')+' value. Optimising outside the feasible region is not permitted. Keep the objective’s stated units.'
        else:
            lines=[authored_math(step.value) for step in p.steps]
            e='$x$ counts the first kind named in the question and $y$ the second. “At most” includes its limit and uses $\\le$; “at least” uses $\\ge$; “more than” is strict. Multiply each quantity by its own resource use before adding a shared total. Twice as many of the second kind means $y\\ge2x$, not $x\\ge2y$. '+('Keep all three simultaneous conditions; satisfying the total alone does not meet the individual minimums.' if t=='three_inequalities' else 'Write the requested constraint using the actual limit given in the question.')
    elif gid in ('nssco_quadratic_graphs','nssco_sketching_quadratics_gradients'):
        if t=='square_form_turning_point':
            a,b,c=m['a'],m['p'],m['q'];lines=[f'x+({b})=0',f'x={-b}',f'y={a}(0)^2+({c})={c}'];e=f'The rule is in $a(x+p)^2+q$ form, with $a={a}$, $p={b}$ and $q={c}$. The squared bracket vanishes at $x=-p={-b}$, leaving $y=q={c}$. This gives the turning point, not the axis intercept. The sign of $a$ determines whether it is a minimum or maximum.'
        elif t=='solve_f_equals_g':
            a,b,c=m['f'];d,e=m['g'];r1,r2=roots(a,b-d,c-e)
            lines=[f'{polynomial_latex(m["f"])}={linear_latex(d,e)}',f'{polynomial_latex([a,b-d,c-e])}=0',f'{a}(x-({q(r1)}))(x-({q(r2)}))=0']
            e=f'The two graphs meet where their outputs are equal for the same input $x$. Here subtract ${linear_latex(d,e)}$ from the quadratic to obtain one quadratic equation. Factor it or use another valid quadratic method. Each zero factor gives an $x$-coordinate of intersection; retain both solutions.'
        else:
            a,b,c=m['quadratic'];f=lambda x:a*x*x+b*x+c;formula=polynomial_latex([a,b,c])
            if t=='table_values':
                lines=[f'x={q(x)}:\\quad y={poly_at([a,b,c],F(x))}={q(f(F(x)))}' for x in m['x']]
                e=f'Use the rule $y={formula}$ for each listed input separately. The coefficients are $a={a}$, $b={b}$ and $c={c}$. Bracket a negative input before squaring, multiply each term, then add. Keep the outputs in the same order as the inputs; a table is not a sorted list of outputs.'
            elif t=='y_intercept':
                lines=[f'x=0,\\quad y={a}(0)^2+({b})(0)+({c})={c}'];e=f'The graph $y={formula}$ meets the $y$-axis where $x=0$. Both variable terms vanish, leaving ${c}$. Give the point $(0,{c})$, not just the constant if coordinates are requested.'
            elif t in ('other_root','x_intercepts','range_of_x'):
                r1,r2=roots(a,b,c);lines=[f'{formula}=0',f'{a}(x-({q(r1)}))(x-({q(r2)}))=0',f'x={q(r1)}\\quad\\text{{or}}\\quad x={q(r2)}']
                e=f'The $x$-intercepts of $y={formula}$ have $y=0$, so solve the displayed quadratic. The roots are ${q(r1)}$ and ${q(r2)}$. '+('The given root is one of these; select the other, and give its point with second coordinate zero.' if t=='other_root' else 'Write intercepts as points with second coordinate zero.' if t=='x_intercepts' else f'The coefficient ${a}$ makes the parabola open '+('upwards' if a>0 else 'downwards')+f'. Compare the sign of the factored expression in the three intervals split by the roots, and choose those where $y{m["sign"]}0$. Strict inequalities exclude the roots themselves.')
            elif t=='chord_gradient':
                x1,x2=map(F,m['x']);y1,y2=f(x1),f(x2);lines=[f'y_1={poly_at([a,b,c],x1)}={q(y1)}',f'y_2={poly_at([a,b,c],x2)}={q(y2)}','m='+frac(f'({q(y2)})-({q(y1)})',f'({q(x2)})-({q(x1)})')]
                e=f'The chord joins the graph at inputs ${q(x1)}$ and ${q(x2)}$. Its endpoint outputs are ${q(y1)}$ and ${q(y2)}$. Gradient $m$ is change in $y$ divided by change in $x$, using the same subtraction order above and below. This chord gradient is not generally the tangent gradient at either endpoint.'
            elif t=='turning_point_gradient':
                lines=[label('Tangent at the turning point is horizontal'), 'm=0'];e=f'The question asks for the tangent gradient at the turning point of $y={formula}$. At a quadratic maximum or minimum the tangent is horizontal, so its gradient is zero. The turning point’s coordinates are positions, not gradients.'
            else:
                x=F(-b)/(2*a);y=f(x);lines=['x='+frac('-b','2a')+'='+frac(f'-({b})',f'2({a})')+'='+q(x),f'y={poly_at([a,b,c],x)}={q(y)}']
                e=f'In $y=ax^2+bx+c$, the actual coefficients are $a={a}$, $b={b}$ and $c={c}$. The turning input is $x=-b/(2a)={q(x)}$, and substitution gives $y={q(y)}$. '+('The symmetry axis is the vertical line at this $x$ value.' if t=='axis_of_symmetry' else 'The requested extreme value is this output $y$, not the input.' if t=='extreme_value' else 'Pair these two values as the turning-point coordinates.')+(' Positive $a$ gives a minimum.' if a>0 else ' Negative $a$ gives a maximum.')
    else:
        if t in ('reciprocal_values','cubic_values','exp_values'):
            for x in map(F,m['x']):
                if t=='reciprocal_values':power=2 if m['squared'] else 1;expression=frac(m['k'],f'({q(x)})^{power}');v=F(m['k'])/x**power
                elif t=='cubic_values':expression=poly_at(m['coefficients'],x);v=poly_value(m['coefficients'],x)
                else:expression=f'{m["a"]}\\times{m["b"]}^{{({q(x)})}}';v=m['a']*F(m['b'])**int(x)
                lines.append(f'x={q(x)}:\\quad y={expression}={q(v)}')
            e='The displayed rule defines $y$ from input $x$. Substitute each listed input, in its original order, before calculating the corresponding output. Bracket negative inputs; a negative exponent means a reciprocal, while cubing a negative preserves its sign. A reciprocal function cannot take input zero. Keep exact fractions instead of rounding intermediate table entries.'
        elif t=='exp_intercept':
            a,b=m['a'],m['b'];lines=[f'x=0,\\quad y={a}\\times{b}^0={a}'];e=f'For $y={a}\\times{b}^x$, the $y$-axis has $x=0$. Any nonzero base raised to zero equals one, so $y={a}$. Give the intercept as $(0,{a})$; the base ${b}$ is not the intercept.'
        elif t=='asymptotes':
            shift=m['shift'];lines=[f'y={shift}']
            if m['shape']!='exp':lines.insert(0,'x=0')
            e=f'The constant shift is ${shift}$ and moves the horizontal asymptote to $y={shift}$. '+('As the input tends far into the negative direction, the positive-base exponential term approaches zero. This horizontal asymptote is not a vertical boundary.' if m['shape']=='exp' else 'The reciprocal term is undefined when its denominator is zero, so $x=0$ is a vertical asymptote. At large input magnitude the reciprocal term approaches zero, leaving the constant shift. An asymptote is a line equation, not an isolated coordinate.')
        else:
            equation=re.findall(r'\$([^$]+)\$',p.question)[0];lines=[equation]+[authored_math(step.value) for step in p.steps]
            if t=='solve_cubic':
                rhs=equation.split('=')[1].strip();lines.insert(1,'x=\\sqrt[3]{'+rhs+'}')
                e=f'The equation is ${equation}$. Undo a cube using a cube root, retaining its sign. This gives one real solution; do not attach an extra $\\pm$ as if the exponent were two. Check by cubing the resulting input.'
            elif t=='solve_recip':
                nums=re.findall(r'\\frac\{(\d+)\}\{([^{}]+)\}',equation);top=nums[0][0];rhs=equation.split('=')[1];lines.insert(1,'x='+frac(top,rhs))
                e=f'Here ${equation}$ has a nonzero denominator $x$. Multiply both sides by $x$, then divide by the entire given right-hand value to isolate $x$. Keep a fractional right-hand side together when dividing. Substitute the answer back into the reciprocal expression to check it.'
            elif t=='solve_recip_sq':
                squared=p.steps[0].value.split('=')[1].strip();lines.insert(-1,'x=\\pm\\sqrt{'+squared+'}')
                e=f'For ${equation}$, first multiply by $x^2$ and isolate the square. Both positive and negative square roots satisfy a positive square equation; $x=0$ is excluded by the original denominator. State both allowed inputs and check them in the original equation.'
            else:
                e=f'For ${equation}$, rewrite the right side using the same positive base as the left. Equal powers of the same base (other than one) have equal exponents. Compare the exponents to find $x$, and verify the resulting power. Do not divide the output by the base as if the exponent were a coefficient.'
    return finish(p,lines,e)
