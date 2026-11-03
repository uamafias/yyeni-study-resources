"""Shared expression construction for whole exam questions and focused recipes."""
from .algebra_content import _sum


def perfect_square_form(r,s,x='x',y='y',sign=1,*,compact=False):
    expression=_sum((r*r,x+'^2'),(sign*2*r*s,x+y),(s*s,y+'^2'))
    bracket=_sum((r,x),(sign*s,y))
    answer=f'({bracket})^2'
    middle='+' if sign>0 else '-'
    identity=f'({r}{x})^2{middle}2({r}{x})({s}{y})+({s}{y})^2'
    if compact:return expression.replace(' ',''),answer.replace(' ',''),identity
    return expression,answer,identity


def grouping_form(r,s,k,letters=('p','q','x','y'),*,compact=False):
    a,b,x,y=letters
    expression=_sum((r,''.join(sorted(a+x))),(s,''.join(sorted(b+x))),(k*r,''.join(sorted(a+y))),(k*s,''.join(sorted(b+y))))
    common='('+_sum((r,a),(s,b))+')'
    answer=common+'('+_sum((1,x),(k,y))+')'
    working=x+common+'+'+str(k)+y+common
    if compact:return tuple(text.replace(' ','') for text in (expression,answer,working))
    return expression,answer,working


def factor_product(factors):
    """Use a square for repeated factors; preserve a complete integer product."""
    from .formatting import linear_latex
    if len(factors)==2 and tuple(factors[0])==tuple(factors[1]):
        return '('+linear_latex(*factors[0])+')^2'
    return ''.join('('+linear_latex(*factor)+')' for factor in factors)


def outside_product(number,inside):
    return ('' if number==1 else '-' if number==-1 else str(number))+inside
