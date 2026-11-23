"""Exact features of fixed trigonometric source items for independent answer QA.
No sampling,parameter generation,learner delivery or recipe behaviour lives here.
"""
import sympy as sp

def features(operation,expression):
    a,b,c,lo,hi=[expression(s)for s in operation['operands']]
    h=expression(operation.get('phase_offset','0'))
    assert a!=0 and b!=0 and lo<hi
    family=operation['family'];assert family in['sin','cos','tan']
    degrees=operation['angle_unit']=='degree'
    assert degrees or operation['angle_unit']=='radian'
    scale=sp.pi/180 if degrees else sp.Integer(1)
    turn=sp.Integer(360)if degrees else 2*sp.pi
    period=sp.simplify((turn/2 if family=='tan'else turn)/abs(b))
    fn={'sin':sp.sin,'cos':sp.cos,'tan':sp.tan}[family]
    def at(point):
        phase=sp.simplify((b*point+h)*scale)
        if family=='tan'and sp.simplify(sp.cos(phase))==0:return None
        return sp.simplify(a*fn(phase)+c)
    def repeated(rad_bases,rad_period):
        phase_ends=[sp.simplify((b*p+h)*scale)for p in[lo,hi]]
        low,high=sorted(phase_ends,key=lambda v:float(sp.N(v,30)))
        found=set()
        for base in rad_bases:
            kmin=int(sp.floor(sp.N((low-base)/rad_period,40)))-1
            kmax=int(sp.ceiling(sp.N((high-base)/rad_period,40)))+1
            for k in range(kmin,kmax+1):
                point=sp.simplify(((base+k*rad_period)/scale-h)/b)
                if bool(point>=lo)and bool(point<=hi):found.add(point)
        return sp.FiniteSet(*found)
    poles=repeated([sp.pi/2],sp.pi)if family=='tan'else sp.FiniteSet()
    target=sp.simplify(-c/a)
    if family=='sin':
        zeros=repeated([sp.asin(target),sp.pi-sp.asin(target)],2*sp.pi)if abs(target)<=1 else sp.FiniteSet()
        stationary=repeated([sp.pi/2],sp.pi)
    elif family=='cos':
        zeros=repeated([sp.acos(target),-sp.acos(target)],2*sp.pi)if abs(target)<=1 else sp.FiniteSet()
        stationary=repeated([0],sp.pi)
    else:
        zeros=repeated([sp.atan(target)],sp.pi);stationary=sp.FiniteSet()
    if family!='tan':
        vmin=sp.simplify(c-abs(a));vmax=sp.simplify(c+abs(a))
        value_pairs=[(p,at(p))for p in{lo,hi,*stationary}]
        window_min=min((v for _,v in value_pairs),key=lambda v:float(sp.N(v,30)))
        window_max=max((v for _,v in value_pairs),key=lambda v:float(sp.N(v,30)))
        visible_range=sp.Interval(window_min,window_max)
        minpoints=sp.FiniteSet(*(p for p in stationary if sp.simplify(at(p)-vmin)==0))
        maxpoints=sp.FiniteSet(*(p for p in stationary if sp.simplify(at(p)-vmax)==0))
        global_range=sp.Interval(vmin,vmax)
    else:
        vmin=vmax=None;minpoints=maxpoints=sp.FiniteSet();global_range=sp.S.Reals
        # Each continuous tangent branch is monotone. Treat undefined endpoints
        # as one-sided infinities rather than connecting across a vertical pole.
        boundaries=sorted({lo,hi,*poles},key=lambda v:float(sp.N(v,30)))
        increasing=bool(a*b>0);ranges=[]
        for left,right in zip(boundaries,boundaries[1:]):
            lv=(-sp.oo if increasing else sp.oo)if left in poles else at(left)
            rv=(sp.oo if increasing else-sp.oo)if right in poles else at(right)
            lower,upper=(lv,rv)if increasing else(rv,lv)
            ranges.append(sp.Interval(lower,upper))
        visible_range=sp.Union(*ranges)
    return {'global_minimum':vmin,'global_maximum':vmax,'amplitude':None if family=='tan'else abs(a),
      'period':period,'y_intercept':at(0),'global_range':global_range,
      'window_range':visible_range,'window_domain':sp.Complement(sp.Interval(lo,hi),poles),
      'window_minimum':visible_range.inf if visible_range.inf in visible_range else None,
      'window_maximum':visible_range.sup if visible_range.sup in visible_range else None,
      'window_zero_locations':zeros,'window_poles':poles,
      'window_global_min_locations':minpoints,'window_global_max_locations':maxpoints,
      'sample_values':sp.Tuple(*(at(expression(s))for s in operation.get('at',[]))),
      'window_length_in_periods':sp.simplify((hi-lo)/period)}
