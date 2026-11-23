"""Fixed-source numerical-equation QA; no renewable instance generation.
A sign bracket computes a reference independently of a supplied iteration.
"""
import mpmath as mp
import sympy as sp

def bracketed_root(operation,expression,check_domain):
    x=expression('x');f,a,b=map(expression,operation['operands'])
    assert a<b;check_domain(f,a,b)
    with mp.workdps(80):
        fn=sp.lambdify(x,f,'mpmath');lo,hi=[mp.mpf(str(sp.N(t,79)))for t in[a,b]]
        fa,fb=fn(lo),fn(hi)
        assert mp.isfinite(fa)and mp.isfinite(fb)and fa*fb<=0,'source root lacks a continuous sign bracket'
        if fa==0:result=lo
        elif fb==0:result=hi
        else:
            for unused in range(260):
                mid=(lo+hi)/2;fm=fn(mid)
                if fm==0:lo=hi=mid;break
                if fa*fm<0:hi=mid
                else:lo=mid;fa=fm
            result=(lo+hi)/2
        assert abs(fn(result))<mp.mpf('1e-65')*(1+abs(result)),'source root residual unresolved'
        return sp.Float(str(result),70)

def supplied_iteration(operation,expression):
    x=expression('x');F=expression(operation['operands'][0]);start=expression(operation['operands'][1]);count=operation['steps']
    assert isinstance(count,int)and 0<=count<=1000
    with mp.workdps(80):
        fn=sp.lambdify(x,F,'mpmath');current=mp.mpf(str(sp.N(start,79)));values=[current]
        for unused in range(count):
            current=fn(current)
            assert isinstance(current,mp.mpf)and mp.isfinite(current),'supplied source iteration left its real finite domain'
            values.append(current)
        if operation.get('return_sequence'):
            return sp.Tuple(*(sp.Float(str(q),70)for q in values))
        return sp.Float(str(current),70)
