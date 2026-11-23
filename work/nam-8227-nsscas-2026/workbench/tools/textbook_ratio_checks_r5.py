"""Independent derivations from source givens, never from the publisher key.

These helpers check fixed textbook items; they do not generate learner problems.
"""
import sympy as sp

FUNCTIONS={'sin':sp.sin,'cos':sp.cos,'tan':sp.tan,
           'csc':sp.csc,'sec':sp.sec,'cot':sp.cot}

def ratios(s,c):
    return {'sin':s,'cos':c,'tan':sp.simplify(s/c)if c!=0 else None,
            'csc':sp.simplify(1/s)if s!=0 else None,
            'sec':sp.simplify(1/c)if c!=0 else None,
            'cot':sp.simplify(c/s)if s!=0 else None}

def substitute(expr,values,x):
    if isinstance(expr,sp.Tuple):return sp.Tuple(*(substitute(part,values,x)for part in expr))
    expr=sp.expand_trig(expr)
    replacements={fn(x):values[name]for name,fn in FUNCTIONS.items()if values[name]is not None}
    result=sp.simplify(expr.xreplace(replacements))
    assert not result.has(x),('source givens do not determine expression',expr,result)
    assert result not in[sp.zoo,sp.nan,sp.oo,-sp.oo]
    return result

def check(operation,expression,x):
    v=[expression(p)for p in operation['operands']]
    kind=operation['kind']
    if kind=='independent-ratio-sum':
        totals=sp.FiniteSet(0)
        for term in operation['terms']:
            values=check(term['operation'],expression,x)
            coefficient=expression(term['coefficient'])
            totals=sp.FiniteSet(*(sp.simplify(a+coefficient*b)for a in totals for b in values))
        return totals
    if kind=='coordinate-trig-ratios':
        px,py=v;r=sp.sqrt(px**2+py**2);assert r>0
        values=ratios(sp.simplify(py/r),sp.simplify(px/r))
        return sp.Tuple(*(values[name]for name in operation['return_functions']))
    if kind in['acute-given-trig-ratio','quadrant-given-symbolic-ratio']:
        target,given=v
        # This is a source condition, not a guess made to fit the printed root.
        assert operation['angle_condition']in['acute','obtuse']
        family=operation['given_family']
        if family=='tan':
            assert operation['angle_condition']=='acute'and operation['given_value_condition']=='value > 0'
            c=1/sp.sqrt(1+given**2);s=given*c
        else:
            assert family in['sin','cos']and operation['given_value_condition']=='0 < value < 1'
            s=given if family=='sin'else sp.sqrt(1-given**2)
            c=given if family=='cos'else sp.sqrt(1-given**2)
            if operation['angle_condition']=='obtuse':
                assert family=='sin';c=-c
        return substitute(target,ratios(s,c),x)
    assert kind=='numeric-given-trig-ratio'
    given,target=v;family=operation['given_family']
    if family in['csc','sec','cot']:
        assert given!=0
        given=1/given;family={'csc':'sin','sec':'cos','cot':'tan'}[family]
    if family in['sin','cos']:
        assert -1<=given<=1
        other=sp.sqrt(1-given**2)
        pairs=[(given,sign*other)if family=='sin'else(sign*other,given)for sign in[-1,1]]
    else:
        assert family=='tan'
        pairs=[(sp.simplify(sign*given/sp.sqrt(1+given**2)),sp.simplify(sign/sp.sqrt(1+given**2)))for sign in[-1,1]]
    answers=[]
    for s,c in set(pairs):
        values=ratios(s,c)
        constraints=operation.get('sign_constraints',[])
        if any(values[rule['function']]is None or sp.sign(values[rule['function']])!=rule['sign']for rule in constraints):continue
        if operation.get('angle_interval'):
            lo,hi=map(expression,operation['angle_interval']);base=sp.Mod(sp.atan2(s,c),2*sp.pi)
            possible=[base+2*k*sp.pi for k in range(int(sp.floor(lo/(2*sp.pi)))-1,int(sp.ceiling(hi/(2*sp.pi)))+1)]
            if not any(bool(lo<t<hi)for t in possible):continue
        assert sp.simplify(s**2+c**2-1)==0
        answers.append(substitute(target,values,x))
    assert answers,('no branch satisfies original source restrictions',operation)
    return sp.FiniteSet(*answers)
