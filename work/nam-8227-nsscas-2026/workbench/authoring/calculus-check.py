#!/usr/bin/env python3
"""Independent Stage-E calculus checks, using visible polynomials and CAS.

This checks mathematical truth independently of the answer functions. Marking
fixtures are declared evidence judgments, not an automatic free-text marker.
"""
from pathlib import Path
from importlib.util import spec_from_file_location,module_from_spec
from collections import Counter
from fractions import Fraction
import hashlib,json,re
import sympy as sp
from sympy.parsing.sympy_parser import parse_expr,standard_transformations,implicit_multiplication_application

W=Path(__file__).resolve().parents[1]
from build_source import load_source
m=load_source(name='_e1_calculus_author').groups()[0]
x,y,t=sp.symbols('x y t',real=True)

def expression(text):
    text=re.sub(r'\\frac\{(-?\d+)\}\{(\d+)\}',r'(\1/\2)',text)
    text=re.sub(r'e\^\{([^{}]+)\}',r'exp(\1)',text)
    text=re.sub(r'\^\{([^{}]+)\}',r'**(\1)',text).replace('^','**')
    return parse_expr(text,local_dict={'x':x,'t':t,'y':y,'exp':sp.exp},transformations=standard_transformations+(implicit_multiplication_application,),evaluate=True)

def visible_poly(q):
    if 'stationary' in q['recipe_id']:
        return expression(q['stem'].split('$f(x)=')[1].split('$')[0])
    return expression(q['stem'].split('$v(t)=')[1].split('$')[0].strip())

def assert_equal(actual,expected):
    assert sp.simplify(actual-expected)==0,(actual,expected)

results=[];examples=[];total=0
for choice in m.choices():
    branch=choice['branch_id'];ids=set();key_sets={};outcomes=Counter()
    for p in choice['parameters']:
        q=m.build(choice['recipe_id'],branch,p);q2=m.build(choice['recipe_id'],branch,p)
        assert q==q2,'non-deterministic group build'
        total+=1
        assert q['proposed_total_marks']=={'gradient':5,'normal':9,'two-extrema':6,'flat-classification':6,'polynomial-chain':6,'exponential-positive':5,'interior-reversal':6}[branch]
        math=q['private_math']
        for part in q['parts']:
            assert part['worked_steps'] and all(all(s.get(k) for k in ('action','reason','result')) for s in part['worked_steps'])
            assert part['answer_only_credit']==0
            key_sets.setdefault(part['local_part_id'],set()).add(part['semantic_key'])
            cids=[c['criterion_id'] for c in part['criteria']]
            assert len(cids)==len(set(cids))
            assert all(cid.startswith(q['recipe_id']+'@0.1.4:'+branch+':') for cid in cids)
            assert all(c['achievement'] and c['marks']==1 for c in part['criteria'])
        all_ids=[c['criterion_id'] for pp in q['parts'] for c in pp['criteria']]
        assert len(all_ids)==len(set(all_ids)),'duplicate criterion identity'
        if branch in ('gradient','normal'):
            a,k,qv=(p[z] for z in ('a','k','q'));C=qv*(a+qv)
            displayed=q['stem'].split('$')[1];left,right=displayed.split('=')
            assert_equal(expression(left)-expression(right),a*sp.exp(k*x)*y+y*y-C)
            # Solve the quadratic explicitly, then differentiate that local branch.
            sigma=sp.sign(a+2*qv)
            local=(-a*sp.exp(k*x)+sigma*sp.sqrt(a*a*sp.exp(2*k*x)+4*C))/2
            derivative=sp.diff(local,x).subs(x,0)
            assert_equal(derivative,sp.Rational(math['gradient']))
            assert_equal(local.subs(x,0),qv)
            assert_equal(derivative*sp.Rational(math['normal_slope']),-1)
            assert derivative!=0 and derivative.is_finite
            assert C==math['C']
        elif branch in ('two-extrema','flat-classification'):
            f=visible_poly(q)
            # Parsing the actual displayed expanded polynomial checks presentation
            # as well as independently computing location/classification.
            derivative=sp.diff(f,x)
            roots=sorted(sp.solve(derivative,x))
            points=[[int(z),int(f.subs(x,z))] for z in roots]
            assert points==math['stationary_points']
            assert_equal(derivative,sp.Poly.from_list(math['derivative_coefficients'],x).as_expr())
            classes=[]
            for root in roots:
                # First nonzero Taylor derivative: independent of emitted sign test.
                degree=sp.degree(f,x)
                for order in range(2,degree+1):
                    value=sp.diff(f,x,order).subs(x,root)
                    if value!=0:
                        typename=('stationary point of inflexion' if order%2 else ('minimum' if value>0 else 'maximum'))
                        classes.append(typename);break
            assert classes==math['types']
            outcomes.update(classes)
        elif branch=='polynomial-chain':
            A,B,u,T=(p[z] for z in ('A','B','u','T'))
            acceleration=expression(q['stem'].split('$a(t)=')[1].split('$')[0])
            primitive=sp.integrate(acceleration,t)
            velocity=primitive+u-primitive.subs(t,0)
            assert_equal(velocity,sp.Poly.from_list(math['velocity_coefficients'],t).as_expr())
            assert_equal(sp.integrate(velocity,(t,0,T)),sp.Rational(math['distance']))
            assert velocity.subs(t,0)>0 and all(z>=0 for z in math['velocity_coefficients'])
        elif branch=='exponential-positive':
            V,T=p['V'],p['T'];k=sp.Rational(p['k'])
            v=expression(q['stem'].split('$v(t)=')[1].split('$')[0])
            assert_equal(v,V*sp.exp(-k*t))
            accel=sp.diff(v,t)
            assert_equal(accel,sp.Rational(math['acceleration_coefficient'])*sp.exp(-k*t))
            dist=sp.integrate(v,(t,0,T))
            drec=math['distance_exact_form']
            assert_equal(dist,sp.Rational(drec['amplitude'])*(1-sp.exp(sp.Rational(drec['exponent']))))
            assert abs(float(dist.evalf())-math['distance_numeric'])<1e-10
        else:
            v=visible_poly(q);T=p['T']
            # Derive zeros from the displayed expanded function; no hidden r use.
            roots=sorted(sp.solve(v,t));inner=[z for z in roots if 0<z<T]
            assert [int(z) for z in inner]==math['interior_roots']
            bounds=[0]+inner+[T]
            signed=[sp.integrate(v,(t,a,b)) for a,b in zip(bounds,bounds[1:])]
            assert_equal(sum(abs(z) for z in signed),sp.Rational(math['distance']))
            assert_equal(sp.integrate(v,(t,0,T)),sp.Rational(math['displacement']))
            assert [str(z) for z in signed]==math['signed_legs']
            outcomes['sign-change' if inner else 'no-change']+=1
        encoded=json.dumps(q,ensure_ascii=False)
        assert not any(chr(n) in encoded for n in [0,8,11,12]),'escaped control glyph'
    # Type/domain mutation must fail, even when Python treats bool equal to 1.
    for bad in [dict(choice['parameters'][0],__extra=1),{},dict(choice['parameters'][0],**{next(iter(choice['parameters'][0])):False})]:
        try:m.build(choice['recipe_id'],branch,bad)
        except ValueError:pass
        else:raise AssertionError('invalid parameter accepted')
    results.append({'branch':branch,'rows_checked':len(choice['parameters']),'part_semantic_counts':{k:len(v) for k,v in key_sets.items()},'strict_complete_fresh_bound':choice['strict_complete_fresh_bound'],'outcomes':dict(outcomes),'invalid_parameter_fixtures_rejected':3})

# Freeze all 21 approved normal/changed/boundary parameter cases as real output.
case_inputs=json.loads((W/'planning/d4/calculus-case-inputs.json').read_text())['cases']+json.loads((W/'planning/d4/motion-cases.json').read_text())
for c in case_inputs:
    p=c['parameters'];q=m.build(c['recipe_id'],c['branch_id'],p)
    examples.append({'case_id':c['case_id'],'case_role':c['case_role'],'parameter_identity':p,'question':q,'sha256':hashlib.sha256(json.dumps(q,sort_keys=True,separators=(',',':'),ensure_ascii=False).encode()).hexdigest()})
assert len(examples)==21

# These are evidence-labelled submission fixtures, not an OCR/symbolic evaluator.
fixtures=[]
bybranch={c['branch_id']:c for c in m.choices()}
for branch,c in bybranch.items():
    chosen=next(e for e in examples if e['question']['branch_id']==branch)
    q=chosen['question'];full=q['proposed_total_marks'];allids=[z['criterion_id'] for p in q['parts'] for z in p['criteria']]
    canonical_submission=[{'local_part_id':part['local_part_id'],'working':'\n'.join(step['result'] for step in part['worked_steps']),'answer':part['reference_answer']} for part in q['parts']]
    alternatives={
      'gradient':r'Let C=4 and y=(-3e^{2x}-sqrt(9e^{4x}+16))/2 (the negative root through P). Differentiating gives y prime=-3e^{2x}-9e^{4x}/sqrt(9e^{4x}+16). At x=0, y prime=-3-9/5=-24/5.',
      'normal':r'Divide by nonzero y: 3e^{2x}+y=4/y. Differentiate: 6e^{2x}+y prime=-4y prime/y^2. Thus y prime=-6e^{2x}y^2/(y^2+4). Substituting 4=3e^{2x}y+y^2 gives y prime=-6e^{2x}y/(3e^{2x}+2y). At P=(0,-4), substitute m=-6e^0(-4)/(3e^0+2(-4))=24/(-5)=-24/5, so normal gradient is 5/24 and y+4=(5/24)x.',
      'two-extrema':r'f prime=3x^2-3=3(x-1)(x+1); roots -1,1; f(-1)=(-1)^3-3(-1)+2=4 and f(1)=1^3-3(1)+2=0. f prime(-2)=9, f prime(0)=-3, f prime(2)=9. Positive to negative at -1 gives maximum (-1,4); negative to positive at 1 gives minimum (1,0).',
      'flat-classification':r'f prime=3x^2-6x+3=3(x-1)^2=0 gives x=1; f(1)=1^3-3(1)^2+3(1)-3=-2. f second=6x-6 is negative for x<1 and positive for x>1, so concavity changes at the stationary point: stationary inflexion (1,-2).',
      'polynomial-chain':r'Integrate a=4t+1: v=2t^2+t+C; v(0)=3 gives C=3. All coefficients nonnegative and 3>0 imply v>0 on [0,2]. Position is s=(2/3)t^3+t^2/2+3t+D and s(0)=0 gives D=0. Distance=s(2)-s(0)=40/3 m.',
      'exponential-positive':r'a=12(-1/2)e^{-t/2}=-6e^{-t/2}. Integrate v to d=-24e^{-t/2}+C. d(0)=0 gives C=24, so d(2)=24(1-e^{-1}) m. Velocity is positive throughout.',
      'interior-reversal':r'v=2(t-1)(t+1) has roots -1,1, only 1 inside [0,3]. It is negative then positive. Primitive F=(2/3)t^3-2t. Integral |v| from 0 to3 = -[F(1)-F(0)]+[F(3)-F(1)]=4/3+40/3=44/3 m. Signed displacement=(F(1)-F(0))+(F(3)-F(1))=12 m.'}
    for role,expected,note in [
      ('correct',full,'Complete canonical shown working.'),
      ('bare-correct',0,'Correct final values only: OD-1 still requires working.'),
      ('wrong',0,'No correct relevant working or answers.'),
      ('ambiguous',None,'Unlabelled or illegible competing expressions require clarification; never choose the favourable reading.'),
      ('alternative',full,'Complete correct approved alternate route fills the same slots once, with all required evidence.')]:
        fixtures.append({'fixture_id':f'calc:{branch}:{role}','case_id':chosen['case_id'],'kind':role,'expected_marks':expected,'max_marks':full,'expected_state':'clarification-required' if expected is None else 'marked','evidence':note,'scope':'declared evidence expectation; not automatic learner-response interpretation','learner_submission':canonical_submission if role=='correct' else ([{'local_part_id':pp['local_part_id'],'answer':pp['reference_answer'],'working':''} for pp in q['parts']] if role=='bare-correct' else (alternatives[branch] if role=='alternative' else ('Unlabelled competing expressions: 12, 44/3. I have not indicated which is distance or displacement.' if role=='ambiguous' and branch=='interior-reversal' else ('The overwritten sign/coefficient is illegible; two uncancelled answers remain.' if role=='ambiguous' else 'I did no relevant working; my final answer is 0.'))))})

partials=[
 ('gradient',3,'The wrong exponential-index derivative has the right value at x=0. G1/G3/G4 only; G2/G5 www are lost.', ['G1','G3','G4']),
 ('normal',5,'Ineligible a3→4 on the normal exemplar: S1/S3, H1, N1/N2 remain ordinary method credit.', ['S1','S3','H1','N1','N2']),
 ('two-extrema',4,'Complete point working but no classification evidence: P1–P4 only.', ['P1','P2','P3','P4']),
 ('flat-classification',3,'Complete point working followed only by f second equals zero therefore inflexion: no classification marks.', ['I1','I2','I3']),
 ('polynomial-chain',3,'Correct velocity integration and initial condition, no distance working.', ['V1','V2','V3']),
 ('exponential-positive',3,'Wrong integrated acceleration coefficient ±V/k, correct complete distance working: E3/E4/E5 only.', ['E3','E4','E5']),
 ('interior-reversal',3,'Credible one-slip root/sign decision and correct primitive with own-leg bounds: R1/R2/R3 only for distance; wrong total and absent displacement.', ['R1','R2','R3'])]
for branch,marks,note,awards in partials:
    fixtures.append({'fixture_id':f'calc:{branch}:partial','kind':'partial','expected_marks':marks,'expected_earned_suffixes':awards,'evidence':note,'scope':'declared evidence expectation; not automatic learner-response interpretation'})
fixtures += [
 {'fixture_id':'calc:normal:copied-target','kind':'proof','expected_part_marks':{'show-derivative':0,'gradient':2,'normal':3},'expected_marks':5,'evidence':'Copied target is no proof; later correct substitution into displayed formula and shown canonical normal working can earn later marks.'},
 {'fixture_id':'calc:normal:divided-missing-backsub','kind':'alternative-partial','expected_proof_marks':3,'evidence':'S1/S2/S3 correctly differentiate ae^(kx)+y=C/y; missing back-substitution loses S4 only.'},
 {'fixture_id':'calc:normal:invalid-ln-y','kind':'invalid-alternative','maximum_proof_marks':1,'evidence':'Negative y makes real ln(y) invalid. S1/S2/S4 fail; separately correct S3 may survive.'},
 {'fixture_id':'calc:flat:coefficient-slip','kind':'partial','expected_marks':5,'evidence':'For normal flat cubic, derivative 2(x−1)^2 loses I1; shown solve and original-function point earn I2/I3; correct sign classification earns I4/I5/I6.'},
 {'fixture_id':'calc:gradient:eligible-k-misread','kind':'misread','expected_gross_marks':5,'expected_marks':4,'net_deduct_from_suffix':'G2','evidence':'Read k2 as3 on normal exemplar, correctly differentiate/substitute. Point remains on curve; genuine nonunit chain demand unchanged. Gross evidence persists after one net deduction.'},
 {'fixture_id':'calc:exponential:deferred-misread','kind':'misread','expected_gross_marks':3,'expected_marks':2,'net_deduct_from_suffix':'E3','evidence':'V12→21 with separate −V/k acceleration error earns no E1/E2; correct misread-data distance E3/E4/E5 gives gross3, deduct once from E3.'},
 {'fixture_id':'calc:mixed:ineligible-interval','kind':'misread','expected_marks':2,'evidence':'No-change exemplar T3→5 changes decision outcome, ineligible throughout. Canonical R2 and ordinary method R5 only.'},
 {'fixture_id':'calc:normal:C4-to5-product','kind':'carry','expected_marks':9,'evidence':'Approved product-route-only 9/9 canonical fixture retained; other divided/log/explicit-root routes remain unresolved E/F carries.'},
 {'fixture_id':'calc:competing-data','kind':'carry','expected_marks':None,'expected_state':'unresolved-policy-fixture','evidence':'Two eligible data compete for the same earned A/B; datum-list ordering must not silently settle the score.'}
]
report={'status':'pass','scope':'author checks only; Stage F/G and app acceptance remain separate','domain_rows_independently_checked':total,'branches':results,'frozen_parameter_examples':len(examples),'submission_evidence_fixtures':len(fixtures),'concrete_script_count_under_stage_e_review':29,'declarative_record_count_under_stage_e_review':22,'oracle':'Independent SymPy differentiation/solve/Taylor classification/integration of displayed expanded polynomials, and explicit local quadratic root for implicit derivative. No generator answer function is used by the oracle.','limitations':['Submission fixture scores are declared rubric expectations, not evidence that a learner text/photo marker implements them.','Independent mathematics does not establish cross-vendor educational acceptance or app rendering.','Competing-misread settlement, implicit C-misread alternative routes and nonconstant stationary coefficient eligibility remain explicit E/F carries.'],'source_sha256':hashlib.sha256((W/'source/groups/calculus.py').read_bytes()).hexdigest(),'domain_sha256':hashlib.sha256((W/'source/domains/calculus.json').read_bytes()).hexdigest()}
for name,data in [('calculus-check.json',report),('calculus-examples.json',examples),('calculus-fixtures.json',fixtures)]:
    (W/'authoring'/name).write_text(json.dumps(data,indent=2,ensure_ascii=False)+'\n')
print(json.dumps({'status':report['status'],'rows':total,'branches':len(results),'examples':len(examples),'fixtures':len(fixtures)}))
