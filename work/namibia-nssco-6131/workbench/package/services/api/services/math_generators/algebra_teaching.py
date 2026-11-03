"""Shared display helpers for fixed algebra teaching examples (never marking)."""
from fractions import Fraction
from .formatting import linear_latex, number_latex


def frac(top, bottom):
    return rf'\frac{{{top}}}{{{bottom}}}'


def bracket(m, c, variable='x'):
    return f'({linear_latex(m,c,variable)})'


def num(value):
    if isinstance(value, (list,tuple)):
        value = Fraction(*value)
    return number_latex(value)


def work(lines, answer):
    """Separate valid equations/expressions, without asserting equality between rows."""
    body = '$$\n\\begin{gathered}\n' + r' \\ '.join(lines) + '\n\\end{gathered}\n$$'
    # Preserve the saved answer's wording, variable pairing and required accuracy.
    return body + '\n\n' + answer


def expression_in(question):
    return question.split('$')[1]
