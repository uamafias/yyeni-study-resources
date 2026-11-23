"""Exact R-form checks for fixed textbook operands; no instance generation."""
import sympy as sp

def coefficients(operation,expression):
    """Read a*sin(t)+b*cos(t) and the source's specified target form."""
    a,b=[expression(v)for v in operation['operands']]
    assert all(v.is_number and v.is_real is True for v in[a,b]),'R-form source check needs fixed real coefficients'
    amplitude=sp.sqrt(a*a+b*b)
    assert amplitude>0,'zero amplitude has no unique phase; record that source case explicitly'
    target=operation['target']
    if target=='sin-plus':u,v=a,b
    elif target=='sin-minus':u,v=a,-b
    elif target=='cos-minus':u,v=b,a
    else:
        assert target=='cos-plus'
        u,v=b,-a
    # atan(Q/P) would lose the quadrant and the P=0 axis case.
    phase=sp.atan2(v,u)
    assert sp.simplify(amplitude*sp.cos(phase)-u)==0
    assert sp.simplify(amplitude*sp.sin(phase)-v)==0
    unit=operation['angle_unit']
    assert unit in['degree','radian']
    phase_out=sp.simplify(phase*180/sp.pi)if unit=='degree'else phase
    if operation.get('phase_bounds'):
        lo,hi=[expression(v)for v in operation['phase_bounds']]
        left=phase_out>lo if operation.get('left_open',True)else phase_out>=lo
        right=phase_out<hi if operation.get('right_open',True)else phase_out<=hi
        assert bool(left)and bool(right),('derived phase violates the actual source restriction',operation,phase_out)
    return sp.Tuple(sp.simplify(amplitude),phase_out)
