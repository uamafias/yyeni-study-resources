"""Independent standard-library numerical checks of fixed source graph features.
The direct math.sin/cos/tan route is separate from the symbolic feature solver.
It checks equations,not source image pixels or proprietary plotting software.
"""
import json,math
import sympy as sp
from analysis_sources import A,write
from verify_textbook_answers_r5 import expression,compute

def number(value):return float(sp.N(value,35))
def check(operation):
    a,b,c,lo,hi=[number(expression(s))for s in operation['operands']]
    h=number(expression(operation.get('phase_offset','0')))
    factor=math.pi/180 if operation['angle_unit']=='degree'else 1.0
    family=operation['family'];fn={'sin':math.sin,'cos':math.cos,'tan':math.tan}[family]
    def arg(x):return(b*x+h)*factor
    def f(x):return a*fn(arg(x))+c
    exact=compute(operation);period=number(exact['period']);tol=1e-8*(1+abs(a)+abs(c))
    residuals=[]
    for k in range(31):
        point=lo+period*(0.137+k/37)
        if family=='tan'and abs(math.cos(arg(point)))<1e-5:continue
        residuals.append(abs(f(point+period)-f(point))/(1+abs(f(point))))
    assert max(residuals)<1e-9,('numerical periodicity failure',operation,max(residuals))
    zeros=[abs(f(number(p)))for p in exact['window_zero_locations']]
    assert not zeros or max(zeros)<tol,('numerical zero failure',operation,max(zeros))
    poles=[abs(math.cos(arg(number(p))))for p in exact['window_poles']]
    assert not poles or max(poles)<1e-10,('numerical pole failure',operation,max(poles))
    for field,valuefield in[('window_global_min_locations','global_minimum'),('window_global_max_locations','global_maximum')]:
        for point in exact[field]:assert abs(f(number(point))-number(exact[valuefield]))<tol,('numerical extrema failure',operation,point)
    visible=exact['window_range']
    intervals=list(visible.args)if isinstance(visible,sp.Union)else[visible]
    limits=[(number(v.start),number(v.end))for v in intervals]
    samples=0;monotonic=0
    for k in range(501):
        point=lo+(hi-lo)*k/500
        if family=='tan'and abs(math.cos(arg(point)))<1e-6:continue
        y=f(point);samples+=1
        assert any(left-tol<=y<=right+tol for left,right in limits),('numerical visible-range failure',operation,point,y,limits)
        if family=='tan'and abs(math.cos(arg(point)))>0.05:
            step=period*1e-6
            assert(f(point+step)-f(point-step))*a*b>0,('numerical tangent orientation failure',operation,point)
            monotonic+=1
    requested_samples=0;requested_poles=0
    for point,expected in zip(operation.get('at',[]),exact['sample_values']):
        point=number(expression(point))
        if expected is None:
            assert family=='tan'and abs(math.cos(arg(point)))<1e-10
            requested_poles+=1
        else:
            assert abs(f(point)-number(expected))<tol,('independent source sample-value failure',operation,point,expected)
            requested_samples+=1
    return {'periodicity_max_relative_residual':max(residuals),'zero_count_checked':len(zeros),'pole_count_checked':len(poles),
      'range_sample_points_checked':samples,'tangent_orientation_points_checked':monotonic,
      'requested_source_sample_values_checked':requested_samples,'requested_source_poles_checked':requested_poles,
      'source_equation_route':'Python math functions evaluated directly from the source coefficients/angular unit; symbolic solver used only for candidate feature locations/ranges to test',
      'status':'numeric cross-check passed'}

def check_angle(operation):
    theta=number(expression(operation['operands'][0]));degrees=operation['angle_unit']=='degree'
    radians=math.radians(theta)if degrees else theta
    cx,sy=math.cos(radians),math.sin(radians)
    ref=math.atan2(abs(sy),abs(cx));ref=math.degrees(ref)if degrees else ref
    quadrant=0 if min(abs(cx),abs(sy))<1e-12 else 1 if cx>0 and sy>0 else 2 if sy>0 else 3 if cx<0 else 4
    exact=compute(operation)
    assert abs(ref-number(exact['reference_angle']))<1e-9,('independent angle reference failure',operation)
    assert quadrant==int(exact['quadrant']),('independent angle quadrant failure',operation)
    assert math.floor(abs(theta)/(360 if degrees else 2*math.pi)+1e-12)==int(exact['complete_turns'])
    assert abs(cx-number(exact['terminal_unit_vector'][0]))<1e-10 and abs(sy-number(exact['terminal_unit_vector'][1]))<1e-10
    return {'status':'numeric cross-check passed','method':'Direct unit-circle cos/sin signs andatan2(abs(sin),abs(cos))geometry,independent of the symbolic modulo/reference-distance route',
      'reference_angle_numeric':ref,'quadrant':quadrant}

def enumerate_ratio_roots(model,op):
    """Enumerate reference-angle branches with math, not SymPy solveset."""
    from verify_textbook_answers_r5 import x
    argument=expression(model['argument'])
    a=number(sp.diff(argument,x));b=number(argument.subs(x,0))
    assert sp.diff(argument,x,2)==0 and a>0
    lo,hi=[number(expression(v))for v in op['operands'][1:]]
    unit=math.pi/180 if model['angle_unit']=='degree' else 1.0
    amin,amax=(a*lo+b)*unit,(a*hi+b)*unit
    target=number(expression(model['ratio']))
    if model['power']==2:
        assert target>=0
        targets=[math.sqrt(target),-math.sqrt(target)]
    else:targets=[target]
    candidates=[]
    for ratio in targets:
        fn=model['function']
        if fn in['sec','csc','cot']:
            if ratio==0:
                if fn!='cot':continue
                fn='cos';ratio=0
            else:
                ratio=1/ratio;fn={'sec':'cos','csc':'sin','cot':'tan'}[fn]
        if fn in['sin','cos']and abs(ratio)>1:continue
        if fn=='sin':
            base=math.asin(ratio);rays=[base,math.pi-base];period=2*math.pi
        elif fn=='cos':
            base=math.acos(ratio);rays=[base,-base];period=2*math.pi
        else:
            assert fn=='tan';rays=[math.atan(ratio)];period=math.pi
        for ray in rays:
            for k in range(math.floor((amin-ray)/period)-1,math.ceil((amax-ray)/period)+2):
                root=((ray+k*period)/unit-b)/a
                if abs(root-lo)<1e-9:root=lo
                if abs(root-hi)<1e-9:root=hi
                left=root>lo if op.get('left_open',False)else root>=lo
                right=root<hi if op.get('right_open',False)else root<=hi
                if left and right and all(abs(root-v)>1e-8 for v in candidates):candidates.append(root)
    return sorted(candidates)

def check_equation(row):
    candidates=enumerate_ratio_roots(row['source_ratio_model'],row['derivation_inputs'])
    symbolic=sorted(number(v)for v in expression(row['derived_answer']))
    assert len(candidates)==len(symbolic),('independent root-count discrepancy',row['item_id'],row['subpart'],candidates,symbolic)
    assert all(abs(a-b)<1e-9 for a,b in zip(candidates,symbolic)),('independent root-value discrepancy',row['item_id'],row['subpart'],candidates,symbolic)
    return {'item_id':row['item_id'],'subpart':row['subpart'],'numeric_roots':candidates,
      'root_count':len(candidates),'status':'independent numeric root enumeration passed',
      'method':'Python math inverse functions,independent quadrant/period enumeration,original affine argument and open/closed interval filtering; no call to the symbolic answer solver.'}

def check_composite_equation(row):
    op=row['derivation_inputs'];candidates=[]
    for branch in row['source_ratio_branches']:
        for value in enumerate_ratio_roots(branch,op):
            if all(abs(value-c)>1e-8 for c in candidates):candidates.append(value)
    def quotient(a,b):
        if abs(b)<1e-10:raise ValueError('original trigonometric pole')
        return a/b
    functions={'tan':lambda t:quotient(math.sin(t),math.cos(t)),
      'sec':lambda t:quotient(1,math.cos(t)),'csc':lambda t:quotient(1,math.sin(t)),
      'cot':lambda t:quotient(math.cos(t),math.sin(t))}
    from verify_textbook_answers_r5 import x
    original=expression(op['operands'][0])
    f=sp.lambdify(x,original,modules=[functions,'math'])
    valid=[]
    for value in candidates:
        try:
            residual=f(value)
            if not math.isfinite(residual)or abs(residual)>1e-8:continue
        except(ZeroDivisionError,ValueError):continue
        valid.append(value)
    valid.sort();symbolic=sorted(number(v)for v in expression(row['derived_answer']))
    for root in symbolic:
        try:residual=f(root)
        except(ZeroDivisionError,ValueError):
            raise AssertionError(('symbolic answer contains original pole',row['item_id'],row['subpart'],root))
        assert math.isfinite(residual)and abs(residual)<1e-8,('symbolic answer fails original equation',row['item_id'],row['subpart'],root,residual)
    assert len(valid)==len(symbolic),('composite root-count discrepancy',row['item_id'],row['subpart'],valid,symbolic)
    assert all(abs(a-b)<1e-9 for a,b in zip(valid,symbolic)),('composite root-value discrepancy',row['item_id'],row['subpart'],valid,symbolic)
    return {'item_id':row['item_id'],'subpart':row['subpart'],'numeric_roots':valid,'root_count':len(valid),
      'status':'independent numeric factor-branch enumeration passed',
      'method':'Enumerate independently specified algebraic factor branches with Python math,filter the original equation/poles,and compare the union with the independently solved original symbolic equation. Neither route calls the other answer routine.'}

def check_inverse(row,operation,answer,purpose):
    a,b,c,lo,hi=[number(expression(v))for v in operation['operands']]
    fn={'sin':math.sin,'cos':math.cos,'tan':math.tan}[operation['family']]
    formula=expression(answer)[operation['return_fields'].index('expression')]
    from verify_textbook_answers_r5 import x
    def asin(v):
        assert abs(v)<=1+1e-12
        return math.asin(max(-1,min(1,v)))
    def acos(v):
        assert abs(v)<=1+1e-12
        return math.acos(max(-1,min(1,v)))
    inverse=sp.lambdify(x,formula,modules=[{'asin':asin,'acos':acos},'math'])
    errors=[]
    for k in range(101):
        point=lo+(hi-lo)*k/100
        image=a*fn(b*point)+c
        errors.append(abs(inverse(image)-point))
    assert max(errors)<1e-8,('inverse composition failure',row['item_id'],row['subpart'],purpose,max(errors))
    return {'item_id':row['item_id'],'subpart':row['subpart'],'purpose':purpose,'points_checked':101,
      'max_absolute_composition_error':max(errors),'status':'independent numerical inverse composition passed',
      'method':'Evaluate the original source function directly with Python math,then evaluate the derived inverse expression at that image. Analytical branch/endpoint reasoning is recorded separately;this sample alone is not a proof of all inputs.'}

def check_rform(row,operation,answer,purpose):
    """Test persisted exact candidates with a separate library/formulation."""
    a,b=[number(expression(v))for v in operation['operands']]
    candidate=expression(answer)
    # SymPy's printed '(R, phase)' round-trips as a Python tuple rather
    # than Tuple(...). Both are the same two-field persisted candidate.
    assert isinstance(candidate,(tuple,sp.Tuple))and len(candidate)==2,('invalid persisted R-form candidate',row['item_id'],row['subpart'],answer)
    candidate=sp.Tuple(*candidate)
    radius=number(candidate[0]);phase=number(candidate[1])
    if operation['angle_unit']=='degree':phase=math.radians(phase)
    target=operation['target']
    u,v={'sin-plus':(a,b),'sin-minus':(a,-b),'cos-minus':(b,a),'cos-plus':(b,-a)}[target]
    expected_radius=math.hypot(a,b);expected_phase=math.atan2(v,u)
    assert expected_radius>0 and abs(radius-expected_radius)<1e-10*(1+expected_radius),('R-form amplitude discrepancy',row['item_id'],row['subpart'])
    assert abs(math.remainder(phase-expected_phase,2*math.pi))<1e-10,('R-form phase quadrant discrepancy',row['item_id'],row['subpart'],phase,expected_phase)
    fn=math.sin if target.startswith('sin')else math.cos
    sign=1 if target.endswith('plus')else-1
    errors=[]
    for k in range(501):
        point=-2*math.pi+4*math.pi*k/500
        original=a*math.sin(point)+b*math.cos(point)
        formed=radius*fn(point+sign*phase)
        errors.append(abs(original-formed)/(1+expected_radius))
    assert max(errors)<1e-11,('R-form original-function discrepancy',row['item_id'],row['subpart'],max(errors))
    return {'item_id':row['item_id'],'subpart':row['subpart'],'purpose':purpose,
      'points_checked':501,'max_relative_function_error':max(errors),'status':'independent R-form coefficient/phase/function checks passed',
      'method':'Read the persisted unrounded candidate; independently calculate coefficient norm/quadrant with Python math and evaluate the original a*sin(t)+b*cos(t) against the specified formed function. No call to the R-form answer routine.'}

def build(negative_fixture=None):
    data=json.loads((A/'textbook-answer-verification-r5.json').read_text());combinations={};angle_inputs={}
    if negative_fixture:
        target={'lost-trig-branch':'8227:TB:YM:C4:Try-Now-47:1',
          'trig-pole-root':'8227:TB:YM:C4:Try-Now-46:5',
          'cosine-axis-branch-lost':'8227:TB:Goldie:C3:Exercise-3B:4',
          'half-angle-axis-branch-lost':'8227:TB:Goldie:C3:Example:6'}[negative_fixture]
        label={'cosine-axis-branch-lost':'iii','half-angle-axis-branch-lost':'iv'}.get(negative_fixture)
        row=next(r for r in data['subparts']if r['item_id']==target and(label is None or r['subpart']==label))
        roots=sp.FiniteSet(*expression(row['derived_answer']))
        if negative_fixture=='lost-trig-branch':
            roots=sp.FiniteSet(*(r for r in roots if not(80<number(r)<90 or 260<number(r)<270)))
        elif negative_fixture=='cosine-axis-branch-lost':roots=roots-sp.FiniteSet(90)
        elif negative_fixture=='half-angle-axis-branch-lost':roots=roots-sp.FiniteSet(sp.pi)
        else:roots=roots|sp.FiniteSet(sp.pi/4)
        row['derived_answer']=str(roots)
    for row in data['subparts']:
        ops=[]
        if row.get('derivation_inputs',{}).get('kind')=='trig-features':ops.append(('requested table/graph',row['derivation_inputs']))
        if row.get('derivation_inputs',{}).get('kind')=='angle-features':
            operation=row['derivation_inputs'];key=json.dumps(operation,sort_keys=True)
            entry=angle_inputs.setdefault(key,{'operation':operation,'references':[]})
            entry['references'].append({'item_id':row['item_id'],'subpart':row['subpart']})
        for name,op in row.get('additional_operations',{}).items():
            if op.get('kind')=='trig-features':ops.append((name,op))
        for purpose,operation in ops:
            # Different point queries on the same function/window are one
            # mathematical configuration. Union their query points, not counts.
            key=json.dumps({k:v for k,v in operation.items()if k!='at'},sort_keys=True)
            entry=combinations.setdefault(key,{'operation':{**operation,'at':[]},'references':[]})
            points={str(expression(p))for p in[*entry['operation']['at'],*operation.get('at',[])]}
            entry['operation']['at']=sorted(points,key=lambda p:(number(expression(p)),p))
            entry['references'].append({'item_id':row['item_id'],'subpart':row['subpart'],'purpose':purpose,'source_requested_points':operation.get('at',[])})
    results=[]
    for key,row in sorted(combinations.items()):results.append({**row,'checks':check(row['operation'])})
    angle_results=[{**row,'checks':check_angle(row['operation'])}for key,row in sorted(angle_inputs.items())]
    equation_results=[check_equation(row)for row in data['subparts']if row.get('source_ratio_model')]
    composite_results=[check_composite_equation(row)for row in data['subparts']if row.get('source_ratio_branches')]
    inverse_results=[];rform_results=[]
    for row in data['subparts']:
        op=row.get('derivation_inputs',{})
        if op.get('kind')=='r-form-coefficients':
            if op.get('phase_decimal_places')is not None:
                assert 'unrounded_canonical_parameters'in row.get('additional_derived_results',{}),'rounded R-form has no exact validation candidate'
            candidate=row.get('additional_derived_results',{}).get('unrounded_canonical_parameters',row['derived_answer'])
            rform_results.append(check_rform(row,op,candidate,'requested/expository R-form output'))
        if op.get('kind')=='inverse-principal-affine-trig':
            inverse_results.append(check_inverse(row,op,row['derived_answer'],'requested inverse'))
        for name,op in row.get('additional_operations',{}).items():
            if op.get('kind')=='r-form-coefficients'and name!='unrounded_canonical_parameters':
                rform_results.append(check_rform(row,op,row['additional_derived_results'][name],name))
            if op.get('kind')=='inverse-principal-affine-trig':
                inverse_results.append(check_inverse(row,op,row['additional_derived_results'][name],name))
    write(A/'textbook-trig-numeric-checks-r5.json',{'status':'Fixed-source mathematical cross-checks; not independent reviewer acceptance,source-pixel comparison or app testing',
       'unique_function_viewport_combinations':len(results),'referenced_outputs':sum(len(r['references'])for r in results),
       'graph_count_basis':'Exact source function,angular unit,phase andwindow;different requested sample-point lists are merged andchecked explicitly. This counts verification configurations,not problem types,source figures orrecipes.',
       'unique_directed_angle_inputs':len(angle_results),'directed_angle_results':angle_results,
       'bounded_equations_checked':len(equation_results),'bounded_equation_results':equation_results,
       'composite_equations_checked':len(composite_results),'composite_equation_results':composite_results,
       'inverse_compositions_checked':len(inverse_results),'inverse_composition_results':inverse_results,
       'rform_validation_cases':len(rform_results),'rform_validation_results':rform_results,
       'all_passed':True,'date':'2026-11-18','results':results})
    print(len(results),'function/viewport combinations,',len(angle_results),'directed angles,',len(equation_results),'basic,',len(composite_results),'composite equations,',len(inverse_results),'inverse compositions,and',len(rform_results),'R-form cases passed independent numeric checks')
if __name__=='__main__':
    import argparse
    p=argparse.ArgumentParser()
    p.add_argument('--negative-fixture',choices=['lost-trig-branch','trig-pole-root','cosine-axis-branch-lost','half-angle-axis-branch-lost'])
    build(p.parse_args().negative_fixture)
