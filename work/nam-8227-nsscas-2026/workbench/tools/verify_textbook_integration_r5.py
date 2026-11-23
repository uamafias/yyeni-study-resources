"""Independent quadrature/real-branch spot checks of fixed textbook QA inputs.
Quadrature is additional numerical evidence, not a proof of global correctness.
"""
import json,sys,math,os,subprocess,itertools
import mpmath as mp
import sympy as sp
from analysis_sources import A,WB,ROOT,write,digest
from verify_textbook_answers_r5 import compute,expression,equivalent,primitive_agrees,trig_residual,x,check_proper_integral_domain

def fixtures():
    checks=[]
    for expr,sf,key in [('2*(exp(15)-exp(3))',3,'6540000'),('2*(exp(8)-1)',3,'5960'),('12345',3,'12300'),('-12345',3,'-12300'),('log(13/3)/5',3,'0.293')]:
        got=compute({'kind':'rounded','operands':[expr],'significant_figures':sf});assert equivalent(got,expression(key))
        checks.append({'expression':expr,'significant_figures':sf,'expected':key,'actual':str(got)})
    try:compute({'kind':'proper-definite-integral','operands':['1/x','-1','1']})
    except AssertionError as e:assert 'original discontinuity'in str(e);message=str(e)
    else:raise AssertionError('pole-crossing fixture passed')
    return checks,message

def source_primitive_stability(source_name='answers-Goldie-C8-trig-opening.json',item_id='8227:TB:Goldie:C8:Exercise-8D:1',subpart='vi',earlier_forms=None):
    source=WB/'tools/textbook-r5'/source_name
    item=next(i for i in json.loads(source.read_text())['items']if i['item_id']==item_id)
    part=next(p for p in item['subparts']if p['subpart']==subpart);op=part['operation']
    assert op.get('integration_algorithm')=='manual','observed unstable primitive lost its fixed algorithm'
    program='import sys,json;sys.path.insert(0,sys.argv[1]);from verify_textbook_answers_r5 import compute;print(str(compute(json.loads(sys.argv[2]))))'
    runs=[]
    for seed in ['0','1','2','3']:
        result=subprocess.run([sys.executable,'-c',program,str(WB/'tools'),json.dumps(op)],cwd=ROOT,env={**os.environ,'PYTHONHASHSEED':seed},check=True,capture_output=True,text=True)
        runs.append({'hash_seed':seed,'derived_primitive':result.stdout.strip()})
    assert len({r['derived_primitive']for r in runs})==1,'fixed-source primitive changed across fresh processes'
    canonical=compute(op);shifts=[]
    if earlier_forms is None:earlier_forms=['sin(2*x)**2/2-cos(2*x)**3/6-cos(2*x)/2','-cos(2*x)**3/6-cos(2*x)**2/2-cos(2*x)/2']
    for earlier in earlier_forms:
        difference=canonical-expression(earlier)
        shift=sp.simplify(difference.subs(x,0))
        assert shift.is_finite is True and trig_residual(difference,shift)==0,('primitive change is not an additive constant',difference)
        shifts.append({'earlier_observed_form':earlier,'canonical_minus_earlier':str(shift)})
    return {'item_id':item['item_id'],'subpart':subpart,'source_input_path':str(source.relative_to(ROOT)),'source_input_sha256':digest(source),'original_operation':op,'fresh_process_runs':runs,'constant_shift_checks':shifts,'limits':'Fixed-source author QA for an observed symbolic-representation instability;not runtime variation or educational acceptance.'}

def main():
    stability=source_primitive_stability()
    additional_stability=source_primitive_stability('answers-YM-C12-examstyle.json','8227:TB:YM:C12:Example:24','a-primitive',
        ['x*sin(x)**2+x*cos(x)**2-sin(x)**2','x*sin(x)**2+x*cos(x)**2+cos(x)**2','x+cos(2*x)/2'])
    primitive_comparisons=[]
    for integrand,candidate,expected in [('x**2','x**3/3+7',True),('sin(x)*cos(x)','-cos(x)**2/2',True),('x**2','x**3/3+x**2',False),('1/x','log(Abs(x))+7',True),('3/(7-9*x)','-log(Abs(7-9*x))/3',True),('3/(7-9*x)','log(Abs(7-9*x))/3',False)]:
        op={'kind':'real-elementary-antiderivative','operands':[integrand]}
        actual=primitive_agrees(op,compute(op),expression(candidate))
        assert actual is expected,(integrand,candidate,actual)
        primitive_comparisons.append({'original_integrand':integrand,'source_candidate':candidate,'agrees_up_to_additive_constant':actual,'expected':expected})
    affine_op={'kind':'real-elementary-antiderivative','operands':['x**2+1/cos(2-3*x)**2'],'integration_coordinate':{'scale':'3','offset':'-2'}}
    affine_primitive=compute(affine_op)
    for candidate,expected in [('x**3/3-tan(2-3*x)/3+17',True),('x**3/3+tan(2-3*x)/3',False)]:
        actual=primitive_agrees(affine_op,affine_primitive,expression(candidate))
        assert actual is expected,('shifted affine primitive regression',candidate,actual)
        primitive_comparisons.append({'original_operation':affine_op,'source_candidate':candidate,'agrees_up_to_additive_constant':actual,'expected':expected})
    shifted_derivative=compute({'kind':'identity','operands':['diff(7*tan(x/2-pi/6)**4,x)']})
    assert equivalent(shifted_derivative,expression('14*tan(x/2-pi/6)**3*sec(x/2-pi/6)**2')),'previously verified shifted tangent derivative rejected'
    op={'kind':'real-elementary-antiderivative','operands':['x**2']}
    try:primitive_agrees(op,compute(op),expression('x**3/3+Piecewise((1,x>0),(0,True))'))
    except AssertionError as error:
        assert 'primitive branch needs component analysis'in str(error)
        primitive_comparisons.append({'original_integrand':'x**2','source_candidate':'x**3/3+Piecewise((1,x>0),(0,True))','rejected':True,'reason':str(error)})
    else:raise AssertionError('discontinuous primitive branch passed as an additive constant')
    limit_checks=[]
    for source,target in [('limit(2**x,x,-oo)','0'),('limit(2**(-x),x,-oo)','oo'),('limit(3**x,x,oo)','oo'),('limit(3**(-x),x,oo)','0'),('limit(2**x+1,x,-oo)','1')]:
        got=compute({'kind':'identity','operands':[source]});assert equivalent(got,expression(target)),(source,got,target)
        limit_checks.append({'source_expression':source,'expected':target,'computed':str(got),'basis':'Exact positive-base rewrite to exp(u ln a);regression for observed SymPy1.14direction error.'})
    sf,negative=fixtures();quadrature=[];branches=[];trapezia=[];seen=set()
    with mp.workdps(55):
        for path in sorted((WB/'tools/textbook-r5').glob('answers-*.json')):
            for item in json.loads(path.read_text())['items']:
                for part in item['subparts']:
                    operations=[part.get('operation',{}),*part.get('additional_operations',{}).values()]
                    for op in operations:
                        if op.get('kind')=='proper-definite-integral':
                            f,lo,hi=map(expression,op['operands']);domain=sp.calculus.util.continuous_domain(f,x,sp.S.Reals)
                            check_proper_integral_domain(f,lo,hi)
                            a,b=[mp.mpf(str(sp.N(q,54)))for q in [lo,hi]]
                            fn=sp.lambdify(x,f,'mpmath');q=mp.quad(fn,[a,(a+b)/2,b]);expected=mp.mpf(str(sp.N(compute(op),54)))
                            error=abs(q-expected);assert error<mp.mpf('1e-40')*(1+abs(expected)),(item['item_id'],part['subpart'],error)
                            quadrature.append({'item_id':item['item_id'],'subpart':part['subpart'],'original_integrand':str(f),'lower':str(lo),'upper':str(hi),'quadrature':str(q),'CAS_exact_value_numeric':str(expected),'absolute_difference':str(error)})
                        elif op.get('kind') in ['trapezium-rule','numeric-trapezium-rule']:
                            clean={k:v for k,v in op.items()if k!='rounding'}
                            marker=(item['item_id'],part['subpart'],json.dumps(clean,sort_keys=True))
                            if marker in seen:continue
                            seen.add(marker)
                            f,lo,hi=map(expression,op['operands']);a,b=float(lo),float(hi);n=op['strips'];h=(b-a)/n
                            fn=sp.lambdify(x,f,'math');scale=float(expression(op.get('scale','1')))
                            # Independently sum individual interpolation segments,not the endpoint/middle rearrangement.
                            total=scale*math.fsum((h/2)*(fn(a+j*h)+fn(a+(j+1)*h))for j in range(n))
                            expected=float(sp.N(compute(clean),25));error=abs(total-expected)
                            assert error<1e-11*(1+abs(expected)),(item['item_id'],part['subpart'],error)
                            trapezia.append({'item_id':item['item_id'],'subpart':part['subpart'],'strips':n,'source_scale':scale,'segment_area_sum':total,'symbolic_or_high_precision_sum':expected,'difference':error})
                        elif op.get('kind')=='tabulated-trapezium':
                            nodes,values=[list(map(float,expression(q)))for q in op['operands']]
                            total=math.fsum((b-a)*(u+z)/2 for a,b,u,z in zip(nodes,nodes[1:],values,values[1:]))
                            expected=float(compute(op));assert abs(total-expected)<1e-10
                            trapezia.append({'item_id':item['item_id'],'subpart':part['subpart'],'tabulated_segment_sum':total,'symbolic_sum':expected})
                        elif op.get('kind')=='real-elementary-antiderivative':
                            original=expression(op['operands'][0]);original_F=compute(op)
                            parameters=sorted((original.free_symbols|original_F.free_symbols)-{x},key=str)
                            assert len(parameters)<=2,('parameter fixture needs explicit source analysis',item['item_id'],parameters)
                            # Numeric finite-difference checks need concrete constants.
                            # The exact derivative identity still checks the symbolic
                            # integrand; these samples are additional,not a parameter proof.
                            choices=itertools.product([sp.Rational(-3,2),sp.S.Zero,sp.Rational(7,3)],repeat=len(parameters))
                            for chosen in choices:
                                substitutions=dict(zip(parameters,chosen));f=original.subs(substitutions);F=original_F.subs(substitutions)
                                domain=sp.calculus.util.continuous_domain(f,x,sp.S.Reals)
                                try:regular_domain=domain.interior
                                except NotImplementedError:regular_domain=domain
                                fn=sp.lambdify(x,f,'mpmath');primitive=sp.lambdify(x,F,'mpmath');values=[]
                                for point in [sp.Rational(-7),sp.Rational(-3),sp.Rational(-1),sp.Rational(1,2),sp.Rational(1),sp.Rational(2),sp.Rational(3),sp.Rational(7)]:
                                    membership=regular_domain.contains(point);evaluated=f.subs(x,point)
                                    if membership is sp.S.false:continue
                                    # Principal fractional powers can be complex on a
                                    # negative base. Never call such a numeric sample a
                                    # real-root check; source scripts check real negative
                                    # odd-root rewrites separately where applicable.
                                    if evaluated.is_real is not True or evaluated.is_finite is not True:continue
                                    z=mp.mpf(str(point.evalf(54)));actual=mp.diff(primitive,z);target=fn(z)
                                    if not mp.isfinite(actual)or not mp.isfinite(target):continue
                                    error=abs(actual-target);assert error<mp.mpf('1e-35')*(1+abs(target)),(item['item_id'],part['subpart'],point,error)
                                    values.append({'point':str(point),'difference':str(error)})
                                assert values,('no verified regular real sample point',item['item_id'],part['subpart'],domain,substitutions)
                                branches.append({'item_id':item['item_id'],'subpart':part['subpart'],'primitive':str(F),'original_domain':str(domain),'constant_samples':{str(k):str(v)for k,v in substitutions.items()},'real_branch_spot_checks':values})
    previous=WB/'checks/r5/answers-before-integration-rounding-fix.json';changes=[]
    if previous.exists():
        old={(r['item_id'],r['subpart']):r for r in json.loads(previous.read_text())['subparts']}
        for row in json.loads((A/'textbook-answer-verification-r5.json').read_text())['subparts']:
            prior=old.get((row['item_id'],row['subpart']))
            if prior and (row['status']!=prior['status']or row.get('derived_answer')!=prior['derived_answer']):changes.append({'item_id':row['item_id'],'subpart':row['subpart'],'before':prior,'after':{'status':row['status'],'derived_answer':row.get('derived_answer')}})
    earlier=WB/'checks/r5/answers-before-exponential-limit-fix.json';limit_changes=[]
    if earlier.exists():
        old={(r['item_id'],r['subpart']):r for r in json.loads(earlier.read_text())['subparts']}
        for row in json.loads((A/'textbook-answer-verification-r5.json').read_text())['subparts']:
            prior=old.get((row['item_id'],row['subpart']))
            if prior and(row['status']!=prior['status']or row.get('derived_answer')!=prior['derived_answer']):limit_changes.append({'item_id':row['item_id'],'subpart':row['subpart'],'before':prior,'after':{'status':row['status'],'derived_answer':row.get('derived_answer')}})
    write(WB/'checks/r5/integration-independent-checks.json',{'status':'author additional quadrature/real-branch checks passed; independent reviewer acceptance pending','proper_integral_checks':quadrature,'real_primitive_branch_checks':branches,'independent_trapezium_segment_checks':trapezia,'significant_figure_fixtures':sf,'exponential_limit_fixtures':limit_checks,'primitive_comparison_fixtures':primitive_comparisons,'primitive_determinism_check':stability,'additional_primitive_determinism_checks':[additional_stability],'pole_crossing_fixture_rejected':negative,'previous_1248_output_changes':changes,'previous_1575_output_changes':limit_changes,'limits':'mpmath quadrature and numerical derivative spot checks supplement the symbolic source QA. They do not certify every future parameter, establish a global error bound or complete either textbook. Primitive comparisons allow additive constants only after both derivatives match the original integrand on the stated real components; numerical derivative samples use regular interiors.'})
    print(len(quadrature),'proper integrals;',len(branches),'real primitives;',len(trapezia),'trapezium checks;',len(changes),'previous1248changes;',len(limit_changes),'previous1575changes; rounding and pole guards passed')
if __name__=='__main__':main()
