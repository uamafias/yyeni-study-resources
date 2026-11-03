"""Display helpers for authored, fixed topic examples; never learner input."""
import re
from fractions import Fraction
from .algebra_teaching import frac, work
from .number_teaching import F, n
from .formatting import number_latex, polynomial_latex, linear_latex


def q(value):
    if isinstance(value,(list,tuple)) and len(value)==2:return number_latex(Fraction(*value))
    return n(F(value))


def point(values):return '('+', '.join(q(x) for x in values)+')'
def vector(values):return r'\begin{pmatrix}' + r'\\'.join(q(x) for x in values) + r'\end{pmatrix}'
def matrix(values):return r'\begin{pmatrix}' + r'\\'.join(' & '.join(q(x) for x in row) for row in values) + r'\end{pmatrix}'
def label(text):return r'\text{'+text+'}'
def mul(*values):return r'\times'.join('('+q(x)+')' for x in values)

def exact_fraction(text):
    try:return number_latex(F(text))
    except (ValueError,TypeError):return str(text)


def authored_math(text):
    """Convert the existing trusted generator's ASCII working to display maths."""
    text=str(text)
    text=re.sub(r'sqrt\(([^()]*)\)',r'\\sqrt{\1}',text)
    text=text.replace('<=',r'\le ').replace('>=',r'\ge ').replace('!=',r'\ne ')
    text=text.replace('*',r'\times ')
    text=re.sub(r'(?<![\w.])(-?\d+)/(\d+)(?![\w.])',lambda m:frac(m[1],m[2]),text)
    return text


def step_work(problem):
    """Retain named geometry reasons and ordered outputs from the vetted instance."""
    return '\n\n'.join(f'${authored_math(step.value)}$ — {step.description}.' for step in problem.steps)


def finish(problem,lines,explanation):
    return work(lines,problem.answer),explanation
