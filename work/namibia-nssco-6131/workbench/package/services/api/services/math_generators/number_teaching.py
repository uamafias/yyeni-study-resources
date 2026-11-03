"""Exact numeric display helpers shared by fixed Numbers and Operations examples."""
from decimal import Decimal,localcontext
from fractions import Fraction
from .algebra_teaching import frac,work
from .formatting import number_latex


def F(value):
    return value if isinstance(value,Fraction) else Fraction(str(value))


def n(value):
    value=F(value);den=value.denominator
    for prime in (2,5):
        while den%prime==0:den//=prime
    if den!=1:return number_latex(value)
    with localcontext() as ctx:
        ctx.prec=60
        text=format(Decimal(value.numerator)/Decimal(value.denominator),'f')
    return text.rstrip('0').rstrip('.') if '.' in text else text


def ratio(parts):
    return ' : '.join(str(v) for v in parts)


def math_spans(text):
    import re
    # Same currency boundary as the safe frontend renderer.
    text=re.sub(r'(?<=[A-Za-z0-9])\$(?=\d)','¤',text)
    return re.findall(r'\$([^$]+)\$',text)
