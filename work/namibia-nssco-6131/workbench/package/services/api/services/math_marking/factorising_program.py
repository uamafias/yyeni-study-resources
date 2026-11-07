"""Instance-authored working for factorising quadratics and completing squares."""
from fractions import Fraction
from ..math_generators.formatting import quadratic_latex, linear_latex, factors_latex, square_form_latex, number_latex
from ..math_generators.algebra_content import _sum
from .solution_programs import SolutionProgram, math_text
from ..math_generators.factorisation_forms import outside_product


def quadratic_program(problem):
    a,b,c=problem.machine['quadratic'];rows=[]
    def add(action,reason,result):rows.append(dict(action=action,reason=reason,result=result))
    def signed(n):return f'({n})' if n<0 else str(n)
    if problem.machine['task']=='factorise':
        (m,p),(n,q)=problem.machine['factors'];r,s=m*q,n*p
        add('Find a pair with the required product and sum',
            (f'Multiply the number in front of x² by the constant: {a} × {c} = {a*c}. ' if a!=1 else '')+f'Find two numbers whose product is {a*c} and whose sum is {b}.',
            rf'{signed(r)}\times {signed(s)}={a*c},\qquad '+_sum((r,''),(s,''))+f'={b}')
        if a!=1:
            add('Split the middle term',
                'Replace the middle term by two terms with the same total coefficient. Keep the first and constant terms.',
                quadratic_latex(a,b,c)+'='+_sum((a,'x^2'),(r,'x'),(s,'x'),(c,'')))
            bracket=f'({linear_latex(n,q)})'
            add('Factor the two groups',
                'Take a common factor from each pair, choosing signs so the bracket is identical in both groups.',
                _sum((m,'x'+bracket),(p,bracket)))
        add('Write the complete factorisation',
            'Write the common bracket once and combine the outside factors. Expanding must reproduce every original coefficient.' if a!=1 else
            'Use the two numbers inside the brackets. Expanding gives their sum as the middle coefficient and their product as the constant.',
            math_text(problem.answer))
    else:
        p,q=problem.machine['form']['p'],problem.machine['form']['q']
        if a!=1:
            add('Take out the leading coefficient from the variable terms',
                'The outside coefficient multiplies the whole bracket. Leave the original constant outside for now.',
                outside_product(a,r'\left('+_sum((1,'x^2'),(Fraction(b,a),'x'))+r'\right)')+(' - '+str(abs(c)) if c<0 else ' + '+str(c) if c else ''))
        add('Halve the coefficient inside the bracket',
            'The middle term of a squared bracket is twice the number added to the variable.',
            rf'\frac{{{number_latex(Fraction(b,a))}}}{{2}}={p}')
        add('Compensate for the constant introduced by the square',
            'Subtract the constant contributed by the squared bracket, including its outside coefficient, from the original constant.',
            f'q={c}-'+signed(a)+r'\times '+signed(p)+f'^2={q}')
        add('Write the completed-square form',
            'Keep the outside coefficient and the compensating constant. Expanding this expression gives the original quadratic.',
            square_form_latex(a,p,q))
        if problem.machine.get('turning_point') is not None:
            add('Read the turning point',
                'The square is zero when the bracket is zero. The horizontal coordinate has the opposite sign to the number inside the bracket.',
                math_text(problem.answer))
    return SolutionProgram(rows,{})


def extension_program(problem):
    from ..math_generators.algebra_content import _term, _power
    m=problem.machine;task=m['task'];rows=[]
    def signed(n):return f'({n})' if n<0 else str(n)
    def squared(value):return value+'^2' if len(value)==1 and value.isalpha() else '('+value+')^2'
    def add(action,reason,result):rows.append(dict(action=action,reason=reason,result=result))
    if task.startswith('perfect_square_'):
        r,s,sign=m['r'],m['s'],m['sign'];x,y=m['letters']
        left=_term(r,x);right=_term(s,y)
        add('Identify the two squared terms','Find the quantities whose squares give the first and last terms.',
            f'{squared(left)}={_term(r*r,x+"^2")},\\qquad {squared(right)}={_term(s*s,y+"^2")}')
        add('Check the middle term','A squared bracket has a middle term twice the product of its two terms, with the displayed sign.',
            rf'{sign*2}\times {left}\times {right}={_term(sign*2*r*s,x+y)}')
        add('Write the squared bracket','Use the positive sign for a positive middle term and the negative sign for a negative middle term. Expanding checks all three terms.',math_text(problem.answer))
    elif task in ('common_factor_quadratic','negative_leading_quadratic'):
        g=m['g'];a,b,c=m['quadratic'];(u,p),(v,q)=m['factors'];r,s=u*q,v*p
        add('Extract the complete common number factor' if g>0 else 'Take out a negative common factor','Divide every original coefficient by the shared number, keeping it outside.' if g>0 else 'Taking out a negative factor makes the inner leading coefficient positive. Divide every original term by that negative factor.',outside_product(g,'('+quadratic_latex(a,b,c)+')'))
        add('Find a pair for the inner quadratic',(f'Multiply the number in front of x² by the constant inside the bracket: {a} × {c} = {a*c}. ' if a!=1 else '')+f'Find two numbers whose product is {a*c} and whose sum is {b}.',
            f'{signed(r)}\\times {signed(s)}={a*c},\\qquad '+_sum((r,''),(s,''))+f'={b}')
        if a!=1:
            add('Split the middle term inside the bracket','Replace the middle term by two terms with the same total coefficient.',
                outside_product(g,'('+_sum((a,'x^2'),(r,'x'),(s,'x'),(c,''))+')'))
            bracket=f'({linear_latex(v,q)})'
            add('Factor the two groups inside the bracket','Both groups must leave the same bracket; keep the original outside factor.',
                outside_product(g,'('+_sum((u,'x'+bracket),(p,bracket))+')'))
        add('Keep every factor in the answer','Keep the outside number. Multiply the brackets back out to check every term in the original question.',math_text(problem.answer))
    elif task=='group_four_variables':
        r,s,k=m['r'],m['s'],m['k'];a,b,x,y=m['letters'];bracket='('+_sum((r,a),(s,b))+')'
        add('Group terms with matching final letters','The first two terms share one letter and the last two share the other.',
            '('+_sum((r,a+x),(s,b+x))+')+('+_sum((k*r,a+y),(k*s,b+y))+')')
        add('Factor each group','Divide every term in a group by its outside factor so both groups leave the same bracket.',
            x+bracket+'+'+str(k)+y+bracket)
        add('Extract the matching bracket','Keep the entire matching bracket as one factor and collect the outside terms as the other.',math_text(problem.answer))
    else:
        g,r,s,sign,power=m['g'],m['r'],m['s'],m['sign'],m['power'];u,v,w=m['letters']
        common=_term(g,_power(u,power));inner=_sum((r,v),(sign*s,w))
        add('Identify the complete shared factor','Take the largest common number factor and the shared letter power, preserving the different remaining letters.',common)
        add('Divide both terms by the shared factor','Keep the remaining letters and the original signs inside the bracket.',inner)
        add('Write the complete product','Multiplying the outside factor by both inside terms must reproduce the original expression.',math_text(problem.answer))
    return SolutionProgram(rows,{})


def basics_program(problem):
    """One clear decision or operation per row, bound to this expression."""
    from ..math_generators.algebra_content import _term, _power
    m=problem.machine;task=m['task'];rows=[]
    def add(action,reason,result):rows.append(dict(action=action,reason=reason,result=result))
    if task in ('common_number_factor','common_letter_factor'):
        g,a,b,sign=m['g'],m['a'],m['b'],m['sign']
        if task=='common_number_factor':
            u,v=m['letters'];common=str(g)
            original=[_term(g*a,u),_term(sign*g*b,v)]
            divided=[_term(a,u),_term(sign*b,v)]
            reason=f'{g} is the largest positive whole number that divides both {g*a} and {g*b}.'
        else:
            v=m['var'];k,j=m['k'],m['j'];common=_term(g,_power(v,k))
            original=[_term(g*a,_power(v,k+j)),_term(sign*g*b,_power(v,k))]
            divided=[_term(a,_power(v,j)),str(sign*b)]
            reason=f'Use the largest shared number factor, {g}, and the largest power of {v} that divides both terms.'
        add('Find the shared factor',reason,common)
        add('Divide each term by the shared factor','These results go inside the bracket. Keep the sign of each term.',
            rf'{original[0]}\div ({common})={divided[0]},\qquad {original[1]}\div ({common})={divided[1]}')
        add('Write the product','Put the shared factor outside the bracket. Multiply back to check both original terms.',math_text(problem.answer))
    elif task=='difference_of_squares':
        g,a,b=m['g'],m['a'],m['b'];u,v=m['letters']
        left,right=_term(a,u),_term(b,v)
        if g>1:
            add('Take out the shared number','Divide both terms by this number before finding the two squares.',
                outside_product(g,'('+_sum((a*a,_power(u,2)),(-b*b,_power(v,2) if v else ''))+')'))
        add('Find what squares to give each term','Find a quantity for each square. The minus sign stays between them.',
            rf'({left})^2={_term(a*a,_power(u,2))},\qquad ({right})^2={_term(b*b,_power(v,2) if v else "")}')
        add('Write a difference bracket and a sum bracket',
            f'Use {left} and {right}: subtract them in one bracket and add them in the other. Keep any number already outside.',math_text(problem.answer))
    elif task=='factorise_by_grouping':
        a,b,c,d=m['a'],m['b'],m['c'],m['d'];u,v,w=m['letters']
        bracket='('+_sum((c,w),(d,''))+')'
        add('Group the terms in pairs','Keep the first two terms together and the last two terms together.',
            '('+_sum((a*c,u+w),(a*d,u))+') + ('+_sum((b*c,v+w),(b*d,v))+')')
        add('Take a shared factor out of each pair','Choose the signs so the same bracket remains in both groups.',
            _sum((a,u+bracket),(b,v+bracket)))
        add('Write the matching bracket once','The terms outside the matching brackets make the other factor. Multiply back to check all four terms.',math_text(problem.answer))
    else:return None
    return SolutionProgram(rows,{})
