"""Small instance programs that need extra working beyond legacy presenters."""
from fractions import Fraction
from .solution_programs import Author
from ..math_generators.formatting import number_latex


def q(value):
    return number_latex(Fraction(str(value)))


def simple_interest_program(p):
    m=p.machine;t=m['task'];P,r,time=map(lambda k:Fraction(str(m[k])),('p','r','t'));I=P*r*time/100
    a=Author(p,('', ''))
    if t=='principal':
        a.add('relationship','Apply simple interest to the given interest, rate and time',
            'The supplied amount is interest alone; substitute it directly in I=Prt/100.',
            expression=rf'{q(I)}=\frac{{P\times{q(r)}\times{q(time)}}}{{100}}')
        a.add('isolate','Make the principal the subject','Multiply by 100 and divide by the complete rate–time product.',
            expression=rf'P=\frac{{{q(I)}\times100}}{{{q(r)}\times{q(time)}}}')
    else:
        amount=Fraction(str(m['amount']))
        a.add('interest','Separate the interest from the final balance',
            'The final balance includes the original principal; their difference is interest.',
            expression=rf'I={q(amount)}-{q(P)}={q(I)}')
        expression=(rf'r=\frac{{{q(I)}\times100}}{{{q(P)}\times{q(time)}}}' if t=='rate'
                    else rf't=\frac{{{q(I)}\times100}}{{{q(P)}\times{q(r)}}}')
        a.add('isolate','Rearrange the simple-interest relationship',
            'Substitute the known values in I=Prt/100 and divide by the factors multiplying the requested unknown.',expression=expression)
    return a.finish(('relationship' if t=='principal' else 'interest','isolate'))
