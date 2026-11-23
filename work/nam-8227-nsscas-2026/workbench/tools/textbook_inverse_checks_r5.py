"""Fixed-source inverse-function checks; not a runtime problem generator."""
import sympy as sp

def inverse_features(operation,expression,x):
    a,b,c,lo,hi=[expression(s)for s in operation['operands']]
    assert a!=0 and b>0 and lo<hi
    family=operation['family']
    fn,inv={'sin':(sp.sin,sp.asin),'cos':(sp.cos,sp.acos),'tan':(sp.tan,sp.atan)}[family]
    if family=='sin':assert -sp.pi/2<=b*lo<b*hi<=sp.pi/2
    elif family=='cos':assert 0<=b*lo<b*hi<=sp.pi
    else:assert -sp.pi/2<b*lo<b*hi<sp.pi/2
    first=sp.simplify(a*fn(b*lo)+c);last=sp.simplify(a*fn(b*hi)+c)
    output_lo,output_hi=sorted([first,last],key=lambda p:float(sp.N(p,40)))
    # The original argument is wholly within one injective principal branch.
    # Inverting the two affine operations therefore preserves that branch.
    formula=sp.simplify(inv((x-c)/a)/b)
    values={'expression':formula,'domain':sp.Interval(output_lo,output_hi),
            'range':sp.Interval(lo,hi)}
    return sp.Tuple(*(values[name]for name in operation['return_fields']))
