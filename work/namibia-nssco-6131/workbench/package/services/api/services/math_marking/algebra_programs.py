"""Authored algebra operations; no explanation inferred from step keywords."""
from .solution_programs import Author
from fractions import Fraction
from .formatting_adapter import q
from .operation_reasons import operation_reason


def algebra_program(p,content):
    f=p.generator_id.removeprefix('nssco_');m=p.machine;t=m.get('task',p.skill)
    a=Author(p,content);add=a.add;n=len(a.rows);awards=()
    if f=='expressions_formulae':
        if t=='expand_and_simplify':
            import re
            variables=list(dict.fromkeys(re.findall(r'[a-z]',re.findall(r'\$([^$]+)\$',p.question)[0])))
            u,v=variables[:2];k=m['m'];b,c=m['bracket'];d,e=m['extra']
            from ..math_generators.algebra_content import _sum
            expanded=_sum((k*b,u),(k*c,v),(d,u),(e,v))
            add('expand','Distribute the outside factor','Multiply both terms in the bracket by the supplied factor, preserving their actual variable names.',expression=expanded)
            add('collect','Collect like variables','Combine coefficients of matching variables only.',expression=_sum((k*b+d,u),(k*c+e,v)))
        elif t=='substitute':
            add('substitution','Replace every variable consistently','Substitute the given values into the complete expression, retaining brackets around negative values.',[0])
            add('evaluate','Follow the order of operations','Evaluate powers before products, then combine signed terms.',range(1,n))
        elif t in ('variation_equation','variation_value'):
            add('rule','Express the proportional relationship','Direct variation multiplies by k; inverse variation divides by the stated power, with a square root only when specified.',[0])
            add('constant','Determine the proportionality constant','Substitute the supplied input/output pair and isolate k.',[1])
            add('equation','Write the determined relationship','Replace k in the general relationship by the determined value.',[2])
            if n>3:add('requested','Use the determined rule for the new input','The same proportionality constant applies to the new input.',range(3,n))
            awards=('rule','constant') if t=='variation_equation' else ('constant','requested')
        elif t=='change_subject':
            form=m['form']
            if form in ('A = sqrt((B - C)/D)','A = sqrt(k(B + C)/D)'):
                add('square','Square the root relationship','Squaring removes the isolated nonnegative square root; square the whole left side.',[0,1])
                add('isolate','Clear the divisor and isolate the subject',('Multiply by the divisor, divide by the outside factor k and subtract the displaced term.' if form=='A = sqrt(k(B + C)/D)' else 'Multiply by the full divisor, then add the displaced term to both sides.'),range(2,n));awards=('square','isolate')
            elif form=='t = k sqrt(y)':
                add('divide','Isolate the square root','Divide the whole equation by the nonzero outside factor.',range(n-1))
                add('square','Square both sides','The square applies to the entire quotient, including its denominator.',[n-1])
            else:
                add('undo','Undo the outer addition or multiplication','Apply the same inverse operation to both sides of the equation.',[0,1])
                add('isolate','Isolate the requested subject','Clear any remaining divisor and divide by the complete coefficient, maintaining nonzero denominator conditions.',range(2,n))
        else:return None
    elif f=='algebraic_manipulation_expansion':
        if t=='divide_algebraic_fraction':
            add('reciprocal','Replace division by reciprocal multiplication','Divide by a nonzero number by multiplying the entire fraction by its reciprocal.',[0])
            add('reduce','Multiply and cancel common factors','Multiply denominators and cancel common nonzero numerical factors; retain the variable factor.',range(1,n))
        elif t in ('expand_square_and_collect','expand_square_times_linear'):
            add('square','Expand the squared bracket','The square (u+v)² contains u², both cross products 2uv, and v², with their signs.',[0])
            add('distribute','Distribute the remaining factor','Multiply every term by the complete outside coefficient or linear factor, preserving signs.',range(1,n-1))
            add('collect','Collect equal powers','Only terms with identical variable powers can be combined.',[n-1]);awards=('square','distribute')
        elif n>1:
            add('distribute','Distribute every factor across its bracket','Every term in one factor multiplies every term of the other factor.',range(n-1))
            add('collect','Collect like terms','Combine coefficients only when their variable powers match.',[n-1])
        else:add('algebraic_operation','Apply the required algebraic operation',operation_reason(f,t),range(n))
    elif f=='factorisation_basics':
        if t=='factorise_by_grouping':
            add('group','Group terms with a common factor','Arrange the terms in pairs that can produce the same binomial factor.',[0])
            add('partial','Factor each group','Extract a factor from each pair while preserving every original term.',[1])
            add('common_bracket','Extract the common binomial','The identical bracket is a multiplicative factor of both grouped terms.',range(2,n))
        else:add('factorisation','Reverse the distributive or product identity',operation_reason(f,t),range(n))
    elif f=='polynomials_algebraic_fractions':
        if t=='single_fraction':
            add('common_denominator','Express the terms over one common denominator','Multiply each numerator by the factor its own denominator is missing.',[0])
            from ..math_generators.formatting import linear_latex,number_latex
            sign=-1 if m['subtract'] else 1
            if 'dens' in m:
                A,B=m['tops'];(u,v),(w,z)=m['dens']
                first=linear_latex(A*w,A*z);second=linear_latex(sign*B*u,sign*B*v)
                expanded=first+(' ' if second.startswith('-') else ' + ')+second
            elif m['form']=='x_over_x_plus_p':
                second=linear_latex(sign*m['q'],sign*m['q']*m['p'])
                expanded='x^2'+(' ' if second.startswith('-') else ' + ')+second
            else:
                first=linear_latex(m['u'],-m['u']*m['p']);constant=sign*m['v']
                expanded=first+(' - ' if constant<0 else ' + ')+number_latex(abs(constant))
            add('expand_numerator','Expand the complete numerator','Distribute every multiplier, and distribute a subtraction sign to every term of the second numerator.',[1],expression=expanded)
            # Show the explicitly simplified numerator, not just a jump in the answer key.
            simplified=next(s.value for s in p.steps if s.description=='Simplify the numerator')
            add('collect_numerator','Collect the numerator terms','Combine like powers after every sign has been applied.',expression=simplified)
            if n>2:add('domain','Record the original excluded inputs','A denominator must remain nonzero, including factors cancelled during simplification. This is explanatory context unless the question asks for restrictions.',range(2,n))
        elif t=='simplify_fraction':
            add('factor','Factor the complete numerator and denominator','Cancellation applies to common multiplicative factors, not individual terms of a sum.',[0])
            add('cancel','Cancel matching nonzero factors','Divide numerator and denominator by the same common factor.',[1])
            if n>2:add('domain','Retain original denominator exclusions','Cancelling a factor does not make a previously undefined input valid.',range(2,n))
        elif t=='divide_polynomial':
            add('division','Divide leading terms, multiply back and subtract','At each division stage choose the term cancelling the current leading power; subtract the complete divisor product.',range(n-1))
            add('reconstruct','Check the quotient and remainder','Dividend must equal divisor × quotient + remainder, with remainder degree below divisor degree.',[n-1])
        else:return None
    elif f=='linear_simultaneous_equations':
        if t=='fraction_coefficient':
            add('fraction','Isolate the fractional term','Add the displaced constant to both sides before clearing its denominator.',[0,1])
            add('denominator','Clear the denominator','Multiply both sides by the complete nonzero denominator.',[2])
            add('isolate','Divide by the variable coefficient','Divide the complete right side by the nonzero coefficient of x.',range(3,n));awards=('denominator','isolate')
        elif t in ('fraction_one','fraction_two','constant_over_linear'):
            add('denominators','Clear denominators across the equation','Multiply every term by the appropriate common denominator, respecting its nonzero restrictions.',[0,1])
            add('isolate','Collect and isolate the unknown','Use equivalent operations on both sides of the resulting linear equation.',range(2,n));awards=('denominators','isolate')
        elif t=='simultaneous_linear':
            add('eliminate','Make one variable cancel','Multiply complete equations by suitable factors and add/subtract them without changing either solution set.',range(min(5,n)))
            add('first_value','Solve the remaining linear equation','The eliminated equation contains one unknown, so divide by its nonzero coefficient.',[5])
            add('substitute','Recover and check the other unknown','Substitute the first value into an original equation and check the resulting pair in the other equation.',range(6,n))
        elif t=='simultaneous_line_curve':
            add('equate','Equate the two expressions for y','A common point has the same y-value in both equations.',range(3))
            add('quadratic','Form and solve the resulting quadratic','Rearrange to zero, factorise and retain both possible x-values.',range(3,n-2))
            add('pairs','Recover the corresponding y-values','Each x-solution must be substituted into an original equation, preserving its own paired y-value.',range(n-2,n))
        else:
            add('equation','Form or rearrange the linear equation','The same operation applied to both sides preserves equality.',range(n-1))
            add('isolate','Divide by the coefficient of the unknown','Dividing the complete right side by the nonzero coefficient isolates the variable.',[n-1])
    elif f=='solving_quadratic_equations':
        if t in ('solve_by_factorising_monic','solve_by_factorising_general'):
            add('factorisation','Rearrange to zero and factorise','The factor product must reconstruct the leading, middle and constant coefficients.',range(n-2))
            add('zero_product','Set each factor equal to zero','A product is zero only if at least one factor is zero; solve each branch separately.',[n-2])
            add('roots','Solve both linear factor equations','Retain each distinct solution with its variable; do not divide by a variable factor and lose a zero root.',[n-1]);awards=('factorisation','zero_product')
        elif t=='solve_factorised':
            add('zero_product','Set each supplied factor equal to zero','A zero product requires at least one zero factor.',range(n-1))
            add('roots','Solve each factor equation','Each factor equation yields a possible root; keep both branches.',[n-1])
        elif t=='solve_square':
            add('square','Isolate the variable square','Divide both sides by the nonzero coefficient before taking roots.',range(n-1))
            add('branches','Take both signs of the square root','An unrestricted real unknown can have both positive and negative square roots.',[n-1])
        else:
            context=t=='quadratic_context_length'
            if context:
                add('model','Form the contextual quadratic','Use the supplied geometric relationship, then collect the terms on one side.',[0,1]);start=2
            else:start=0
            add('coefficients','Identify the signed coefficients','The quadratic formula uses the coefficients of a quadratic equal to zero.',range(start,n-2 if context else n-1))
            add('formula','Apply both branches of the quadratic formula','Use the full discriminant and divide the whole numerator by 2a.',[n-2] if context else [n-1])
            if context:add('context','Choose the admissible root','A physical width must be positive; reject any root violating the original context.',[n-1])
    elif f=='inequalities_indices':
        if t=='numeric_index':
            add('combine_powers','Combine powers with the same base','Products add exponents, while division subtracts the complete denominator exponent.',[0])
            add('exponent','Simplify the combined exponent','Expand the subtraction across the denominator exponent before collecting.',range(1,n));awards=('combine_powers','exponent')
        elif t in ('exponential_linear','exponential_simple'):
            add('base','Express both sides with the same base','The supplied positive base permits the constants to be rewritten as powers of that base.',range(2))
            add('exponent_equation','Equate and solve the exponents','Equal powers of the same positive base other than one have equal exponents.',range(2,n))
        elif t.startswith('inequality_'):
            if t=='inequality_brackets':
                add('expand','Expand the bracket','The outside multiplier applies to every bracketed term.',range(2))
                add('isolate','Collect and isolate the unknown','Equivalent inequality operations preserve direction unless multiplying/dividing by a negative, when direction reverses.',range(2,n))
            else:
                add('bounds','Apply the same operation to every side','For a double inequality, each operation applies to all three expressions; a negative divisor reverses each comparison.',range(n))
        elif t in ('evaluate_fractional','evaluate_fractional_power'):
            add('root','Take the root indicated by the denominator','The denominator of a fractional exponent specifies the root.',[0])
            add('power','Apply the numerator power','Raise that root to the numerator power.',range(1,n))
        else:add('index_law','Apply the stated index identity',operation_reason(f,t),range(n))
    elif f=='sequences':
        if t=='number_of_terms':
            add('term_equation','Use the arithmetic nth-term relationship','The nth term is a+(n−1)d, because the first term has zero added differences.',[0])
            add('index','Isolate the term index','Subtract the first term and divide by the common difference, then add one.',range(1,n));awards=('term_equation','index')
        elif t=='ap_sum':
            add('count','Determine the number of terms','Use the last-term equation to find the inclusive term count.',range(n-2))
            add('sum','Apply the arithmetic-series sum','Pairing first and last terms gives n times their average.',range(n-2,n))
        elif t=='ap_a_and_d':
            add('term_equations','Express both specified terms','Each term has form a+(n−1)d.',range(2))
            add('difference','Eliminate the first term to find d','Subtracting the two term equations cancels a.',range(2,n-1))
            add('first','Recover the first term','Substitute d into either original term equation.',[n-1]);awards=('term_equations','difference')
        elif t=='ap_to_gp':
            add('terms','Express the selected arithmetic terms','Use their original sequence indices in a+(n−1)d.',[0])
            add('geometric','Impose the geometric-sequence relationship','For three consecutive geometric terms, the middle squared equals first × third.',[1])
            add('expand','Expand and collect the relationship','Distribute both products and cancel matching terms.',range(2,n-2))
            add('ratio','Recover the requested common ratio','Substitute the derived relationship into consecutive selected terms and divide second by first.',range(n-2,n))
        elif t=='nth_term':
            add('difference','Find the common difference','Consecutive arithmetic terms differ by the same amount.',[0])
            add('rule','Form and simplify the nth-term expression','Start at a and add n−1 copies of the common difference.',range(1,n-1))
            add('check','Check the rule at the first term','Putting n=1 must recover the original first term.',[n-1])
        else:
            add('difference','Find the common difference','Subtract consecutive terms in the stated order.',[0])
            add('continue','Apply the difference to the last known term','The same signed difference continues the arithmetic sequence.',range(1,n))
    elif f=='logarithms':
        if t=='evaluate_log':
            if m['shape']=='multiple':
                add('power','Express the argument as a power of ten','A base-ten logarithm gives the exponent on ten.',range(n-1))
                add('operation','Apply the outside multiplier','The coefficient multiplies the logarithm value, not its argument.',[n-1])
            else:
                add('power','Express both arguments as powers of ten','A base-ten logarithm equals the exponent required on ten, including negative exponents.',[0])
                add('operation','Perform the stated addition or subtraction','Operate on the two logarithm values with the signs in the original expression.',range(1,n));awards=('power','operation')
        elif t=='combine_logs':
            if m['form']=='log a + log b - log c':
                left,right,den=m['a'],m['b'],m['c']
                add('power_law','Combine the added logarithms','A sum of logarithms is the logarithm of the product of their positive arguments.',expression=rf'\log {left}+\log {right}=\log({left}\times{right})=\log {left*right}')
                add('combine','Apply the quotient law','Subtracting a logarithm divides the argument of the first by the argument of the second.',expression=rf'\log {left*right}-\log {den}=\log\left(\frac{{{left*right}}}{{{den}}}\right)')
            elif n==2:
                add('power_law','Move the coefficients into argument powers','For a positive argument, k log x equals log(xᵏ).',[0])
                add('combine','Combine products and quotients','Sums multiply logarithm arguments; differences divide them.',[1])
            else:
                add('constant','Express the constant as a base-ten logarithm','For an integer c, c=log(10ᶜ).',[0])
                add('power_law','Bring the variable exponent inside its logarithm','The logarithm power law replaces a multiplier with an argument power.',[1])
                add('combine','Multiply all positive logarithm arguments','The sum becomes one logarithm; retain complete bracketed factors.',range(2,n))
            awards=('power_law','combine')
        elif t=='solve_exponential':
            base=m['a'];power=m.get('p',1);offset=m.get('q',m.get('b',0));scale=m.get('k',1)
            rhs=Fraction(str(m['c']))/scale
            from ..math_generators.formatting import linear_latex
            exponent=linear_latex(power,offset)
            quotient=rf'\frac{{\log({q(rhs)})}}{{\log {base}}}'
            add('logarithms','Take logarithms of the isolated exponential','Divide out the outside multiplier, then bring down the complete exponent with the logarithm power law.',expression=rf'{base}^{{{exponent}}}={q(rhs)}\quad\Rightarrow\quad ({exponent})\log {base}=\log({q(rhs)})')
            expression=quotient if offset==0 else quotient+('-'+str(offset) if offset>0 else '+'+str(-offset))
            if power!=1:expression=rf'\frac{{{expression}}}{{{power}}}'
            add('isolate','Divide by the base logarithm and isolate x','Subtract the exponent constant and divide by its coefficient only when these are present.',expression='x='+expression)
            add('precision','Evaluate before final rounding','Retain calculator precision until the requested significant-figure rounding.',expression=rf'x\approx {m["x"]:.10g}')
            awards=('logarithms','isolate')
        elif t=='split_log':
            add('product_quotient','Split products and quotients','For positive arguments, log(ab)=log a+log b and log(a/b)=log a−log b.',[0])
            add('power_law','Bring each argument power outside','The logarithm power law gives log(xᵏ)=k log x.',range(1,n))
        else:
            add('power','Express the argument using the known logarithm base','Rewriting the argument as a power permits the power law.',[0])
            add('substitute','Apply the power law and the given logarithm value','The logarithm of a power is its exponent multiplied by the logarithm of its base.',range(1,n))
    elif f=='functions':
        if t=='composite_quadratic':
            add('order','Identify the inner and outer function','fg(x) means f(g(x)); apply g first.',[0])
            add('square','Expand the squared inner expression','The full inner expression is squared, including its cross term.',[1])
            add('substitution','Substitute the complete inner expression in f','Replace every input occurrence in the outer rule, retaining its outside signs and constants.',[2])
            add('distribute','Distribute and collect the resulting expression','Apply the outside coefficient to every squared-expression term before collecting.',range(3,n));awards=('substitution','distribute')
        elif t in ('composite_value','composite_linear'):
            add('order','Fix the composition order','Read the rightmost function first, then use its output as the outer function input.',[0])
            add('inner','Evaluate or substitute the inner function','Keep the complete inner value or expression as one substituted input.',[1])
            add('outer','Apply the outer function','Evaluate or expand the outer rule after substitution, then collect like terms.',range(2,n))
        elif t=='inverse_linear':
            add('swap','Interchange input and output','An inverse reverses the original input–output relationship.',range(2))
            add('isolate','Solve the swapped relationship for the output','Use equivalent operations to isolate y, dividing by the complete nonzero coefficient.',range(2,n))
        elif t=='solve_function_equation':
            add('equate','Express the function equation in algebra','Use the stated function rules on both sides.',[0])
            add('solve','Collect and isolate the unknown','The same operation on both sides preserves the equation.',range(1,n))
        elif t=='function_of_expression':
            add('substitute','Substitute the entire input expression','The complete expression replaces each occurrence of the function input.',[0])
            add('simplify','Expand and collect the expression','Multiply through brackets before combining like terms.',range(1,n))
        else:add('evaluate','Evaluate the function at its stated input',operation_reason(f,t),range(n))
    elif f=='functions_concepts':add('concept','Apply the function definition to the stated relation',operation_reason(f,t),range(n))
    else:return None
    return a.finish(awards)
