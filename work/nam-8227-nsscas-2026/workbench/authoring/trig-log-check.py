"""Independent Stage-E mathematical audit; no app calls, no acceptance claim.

R-form answers are rederived by the tangent-half-angle polynomial, not the
generator's phase solver. Log answers are recovered by solving two linear
equations and substituted in the original model. Principal inverse answers are
checked symbolically. Marking fixtures are explicit evidence expectations, not
an assertion that unstructured learner responses have been machine assessed.
"""
from decimal import Decimal, ROUND_HALF_UP
from fractions import Fraction
from pathlib import Path
import argparse
import hashlib
import importlib.util
import json
import math
import re
import xml.etree.ElementTree as ET

import mpmath as mp
import sympy as sp

WB = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("stage_e_trig_log",WB / "source/groups/trig_log.py")
M = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(M)
mp.mp.dps = 75


def sha(data):
    return hashlib.sha256(data).hexdigest()


def round_half_up(value, places):
    return format(Decimal(str(value)).quantize(Decimal(1).scaleb(-places),rounding=ROUND_HALF_UP),f".{places}f")


def half_angle(a,b,c):
    # t=tan(theta/2): (b+c)t² - 2a t + c-b = 0.
    A,B,C=b+c,-2*a,c-b
    if A==0:
        roots=[mp.mpf(180), (2*mp.degrees(mp.atan(-mp.mpf(C)/B)))%360]
    else:
        disc=B*B-4*A*C
        ts=[(-B+sgn*mp.sqrt(disc))/(2*A)for sgn in [-1,1]]
        roots=[(2*mp.degrees(mp.atan(t)))%360 for t in ts]
    return sorted(r for r in roots if 0<r<360)


def parse_exact_latex(s):
    """Tiny checker for the emitted exact scalar vocabulary, not a marking parser."""
    t=s.replace(r"\sqrt{2}","sqrt(2)").replace(r"\sqrt{3}","sqrt(3)")
    t=re.sub(r"\\frac\{([^{}]+)\}\{([^{}]+)\}",r"((\1)/(\2))",t)
    return sp.sympify(t,locals={"sqrt":sp.sqrt},rational=True)


def all_strings(x):
    if isinstance(x,str):yield x
    elif isinstance(x,dict):
        for v in x.values():yield from all_strings(v)
    elif isinstance(x,list):
        for v in x:yield from all_strings(v)


def intersect(rect,a,b):
    # Independent orientation/corner check, distinct from generator Liang-Barsky.
    x0,y0,x1,y1=rect
    if x0<=a[0]<=x1 and y0<=a[1]<=y1:return True
    if x0<=b[0]<=x1 and y0<=b[1]<=y1:return True
    def cross(p,q,r):return(q[0]-p[0])*(r[1]-p[1])-(q[1]-p[1])*(r[0]-p[0])
    def between(p,q,r):return min(p[0],q[0])-1e-9<=r[0]<=max(p[0],q[0])+1e-9 and min(p[1],q[1])-1e-9<=r[1]<=max(p[1],q[1])+1e-9
    def segments(p,q,r,s):
        v=[cross(p,q,r),cross(p,q,s),cross(r,s,p),cross(r,s,q)]
        if v[0]*v[1]<0 and v[2]*v[3]<0:return True
        return any(abs(z)<1e-9 and between(u,w,k)for z,u,w,k in [(v[0],p,q,r),(v[1],p,q,s),(v[2],r,s,p),(v[3],r,s,q)])
    corners=[(x0,y0),(x1,y0),(x1,y1),(x0,y1)]
    return any(segments(a,b,corners[i],corners[(i+1)%4])for i in range(4))


def fixtures():
    def row(fid,recipe,branch,params,kind,submission,earned,total,out_of,**extra):
        return dict(fixture_id=fid,recipe_id=recipe,branch_id=branch,parameters=params,response_kind=kind,
                    submission=submission,expected_gross_earned_local_criterion_ids=earned,
                    expected_net_marks=total,out_of=out_of,assessment_status="authored rubric expectation; not an unstructured-response marker test",**extra)
    PI,RF,LOG=M.RECIPES[1],M.RECIPES[0],M.RECIPES[2]
    allpi=["P-B1","P-M1","P-A1"];allrf=["a-B1","a-M1","a-A1","b-M1","b-M2","b-A1","b-A2"]
    allg=["G-B1","G-M1","G-A1","G-M2","G-A2"];allt=["T-B1","T-M1","T-A1","U-M1","U-A1"]
    p=dict(k=4,theta="-pi/6");rf=dict(a=2,b=3,c=1);g=dict(L="1/2",p="1/2",x1=1,delta_x=2);t=dict(b=2,c=1,m=3,q=10)
    return [
        row("PI-correct",PI,"solve-or-explain",p,"correct",r"-pi/2 < -pi/6 < pi/2; 4x=sin(-pi/6)=-1/2; x=-1/8.",allpi,3,3),
        row("PI-no-applied-range",PI,"solve-or-explain",p,"partially-correct",r"Range is [-pi/2,pi/2]. 4x=-1/2; x=-1/8.",["P-M1","P-A1"],2,3),
        row("PI-bare-correct",PI,"solve-or-explain",p,"answer-only",r"x=-1/8",[],0,3,feedback="Your value is correct; show how it satisfies the principal inverse relation."),
        row("PI-wrong-accepts-forward-candidate",PI,"solve-or-explain",dict(k=3,theta="2*pi/3"),"wrong",r"3x=sin(2pi/3)=sqrt(3)/2, so x=sqrt(3)/6.",[],0,3),
        row("PI-forced-contradiction",PI,"solve-or-explain",dict(k=3,theta="2*pi/3"),"alternative",r"Sine forces x=sqrt(3)/6; asin(3x)=pi/3, not 2pi/3. The only forward candidate fails, so no real solution.",allpi,3,3),
        row("PI-ambiguous-sign",PI,"solve-or-explain",p,"ambiguous",r"Handwritten target copied with an unreadable sign.",[],None,3,pending_clarification=True),
        row("RF-correct",RF,"degree-cycle",rf,"correct",r"R=sqrt(13), tan alpha=3/2, alpha=56.31deg. sin(theta+alpha)=1/sqrt(13); complete shifted root search; theta=107.6deg or 319.8deg.",allrf,7,7),
        row("RF-only-one-original-root",RF,"degree-cycle",rf,"partially-correct",r"Correct conversion and hence sine-subject line; only the first valid original root, without a complete transformed-root search.",["a-B1","a-M1","a-A1","b-M1","b-A1"],5,7),
        row("RF-extra-final-angle",RF,"degree-cycle",rf,"partially-correct",r"Correct conversion and complete working, then both canonical final roots plus an uncancelled coterminal final angle.",allrf[:-1],6,7),
        row("RF-non-hence",RF,"degree-cycle",rf,"alternative-excluded",r"Correct part (a). In (b), solves the original equation by an independent tangent-half-angle method without using part (a).",allrf[:3],3,7),
        row("RF-bare-correct",RF,"degree-cycle",rf,"answer-only",r"Correct converted expression and root pair, with no working.",[],0,7),
        row("RF-ambiguous-root",RF,"degree-cycle",rf,"ambiguous",r"Second handwritten final root is not legible.",[],None,7,pending_clarification=True),
        row("GRAPH-correct",LOG,"graph-intercept",g,"correct",r"ln y=px+p+ln A; p=(2.5-1.5)/(3-1)=1/2; 1.5=1/2+1/2+ln A; A=exp(1/2).",allg,5,5),
        row("GRAPH-omits-offset",LOG,"graph-intercept",g,"partially-correct",r"ln y=px+ln A; p=(2.5-1.5)/2=1/2; ln A=1.5-0.5=1; A=e.",["G-M1","G-A1","G-M2"],3,5),
        row("GRAPH-simultaneous",LOG,"graph-intercept",g,"alternative",r"1.5=2p+ln A; 2.5=4p+ln A. Subtraction gives p=1/2, then ln A=1/2, A=e^(1/2).",allg,5,5),
        row("GRAPH-wrong-parameter-reading",LOG,"graph-intercept",g,"wrong",r"Reads x-coordinates as p and A and submits those values, without log-line working.",[],0,5),
        row("GRAPH-ambiguous-coordinate",LOG,"graph-intercept",g,"ambiguous",r"A copied ordinate is illegible; clarify before deciding which value was used.",[],None,5,pending_clarification=True),
        row("TARGET-correct",LOG,"gradient-target",t,"correct",r"log2 y=a+x log2 a; log2 a=3; a=8. Hence 10=8+3x; x=2/3.",allt,5,5),
        row("TARGET-consistent-earlier-omission",LOG,"gradient-target",t,"partially-correct",r"log2 y=x log2 a; log2 a=3; a=8. Hence 10=3x; x=10/3.",["T-M1","T-A1","U-M1"],3,5),
        row("TARGET-new-prefactor-omission",LOG,"gradient-target",t,"wrong-step",r"Correct line log2 y=a+x log2 a and a=8. Newly writes 10=3x in (b), getting x=10/3.",allt[:3],3,5),
        row("TARGET-ln-alternative",LOG,"gradient-target",t,"alternative",r"ln y=a ln2+x ln a; plotted gradient ln a/ln2=3; a=8. Hence 10 ln2=8 ln2+x ln8; x=2/3.",allt,5,5),
        row("TARGET-bare-correct",LOG,"gradient-target",t,"answer-only",r"a=8, x=2/3",[],0,5),
        row("TARGET-ambiguous-prefactor",LOG,"gradient-target",t,"ambiguous",r"It is unclear whether the prefactor was retained in earlier working.",[],None,5,pending_clarification=True),
        row("PI-eligible-scaling-misread",PI,"solve-or-explain",p,"misread",r"Copies coefficient 4 as 5; applies actual target range, 5x=-1/2, x=-1/10.",allpi,2,3,misread=dict(datum_id="k",canonical=4,misread=5,eligible=True,deduction_criterion="P-B1",gross_marks=3,authority="owner-approved MR03-OPS-D4")),
        row("PI-designed-no-real-sign-misread",PI,"solve-or-explain",dict(k=3,theta="-3*pi/4"),"misread",r"Reads -3pi/4 as +3pi/4; shows 3pi/4>pi/2, so no real solution.",allpi,2,3,misread=dict(datum_id="theta",eligible=True,deduction_criterion="P-B1",gross_marks=3,authority="owner-approved MR03-OPS-D4")),
        row("TARGET-prefactor-misread",LOG,"gradient-target",t,"misread",r"Copies c=1 as 3; log2 y=3a+x log2 a; a=8; 10=24+3x; x=-14/3.",allt,4,5,misread=dict(datum_id="c",eligible=True,deduction_criterion="T-B1",gross_marks=5,authority="owner-approved MR03-OPS-D4")),
    ]


def run():
    result={}; samples=[];gallery=[];rounding_rows=[];math_expressions=set()
    choices=M.choices()
    for ch in choices:
        branch=ch['branch_id']; keys=set();subkeys=set(); outcomes={};allids=set();ns=0
        for index,p in enumerate(ch['parameters']):
            q=M.build(ch['recipe_id'],branch,p);again=M.build(ch['recipe_id'],branch,p)
            assert q==again,('nondeterministic',branch,p)
            for text in all_strings(q):
                assert not any(ord(c)<32 and c not in '\n\t'for c in text),('control character',branch,p,repr(text))
                assert '\t'not in text,('literal tab in mathematical text',branch,p,repr(text))
                if '$'in text:
                    assert text.count('$')%2==0,('unbalanced inline maths',branch,p,text)
                    math_expressions.update(re.findall(r'\$([^$]+)\$',text))
            ids=[c['criterion_id']for pt in q['parts']for c in pt['criteria']]
            assert len(ids)==len(set(ids));allids.update(ids)
            assert sum(c['marks']for pt in q['parts']for c in pt['criteria'])=={'degree-cycle':7,'solve-or-explain':3,'graph-intercept':5,'gradient-target':5}[branch]
            for pt in q['parts']:
                assert pt['answer_only_marks']==0 and pt['worked_steps']
                assert all(set(s)=={'action','reason','result'}and all(s.values())for s in pt['worked_steps'])
            keys.add(tuple(q['exposure_keys']));subkeys.update(q.get('subdecision_exposure_keys',[]))
            if branch=='degree-cycle':
                a,b,c=[p[k]for k in ['a','b','c']];roots=half_angle(a,b,c)
                assert len(roots)==2
                for value,internal in zip(roots,q['private_math']['roots_degrees']):assert abs(value-internal)<mp.mpf('1e-11')
                expected=[round_half_up(r,1)for r in roots]
                emitted=re.findall(r'=(\d+\.\d)\^\\circ',q['parts'][1]['reference_answer'])
                assert emitted==expected,('rounded roots',p,emitted,expected)
                for r in roots:assert abs(a*mp.sin(mp.radians(r))+b*mp.cos(mp.radians(r))-c)<mp.mpf('1e-65')
                alpha=mp.degrees(mp.atan(mp.mpf(b)/a));assert round_half_up(alpha,2)in q['parts'][0]['reference_answer']
                cls='above-sine-coefficient'if c>b else 'zero-target'if c==0 else 'wrap-or-negative'
                outcomes[cls]=outcomes.get(cls,0)+1
                rounding_rows.append(dict(parameters=p,phase_2dp=round_half_up(alpha,2),roots_1dp=expected))
            elif branch=='solve-or-explain':
                theta=sp.sympify(p['theta'],locals={'pi':sp.pi});inside=bool(abs(theta)<=sp.pi/2)
                if inside:
                    exact=parse_exact_latex(q['private_math']['exact_solution']);assert sp.simplify(sp.asin(p['k']*exact)-theta)==0
                    assert q['private_math']['exact_solution']in q['parts'][0]['reference_answer']
                else:
                    assert 'no real solution'in q['parts'][0]['reference_answer']
                    # Direct principal inverse of the forced forward candidate differs.
                    assert sp.simplify(sp.asin(sp.sin(theta))-theta)!=0
                outcomes['real'if inside else 'no-real']=outcomes.get('real'if inside else 'no-real',0)+1
                assert ('8227:2020:M1:T6:O03:D01'in q['conditional_direct_demand_ids'])==inside
            elif branch=='graph-intercept':
                root=ET.fromstring(q['assets'][0]['svg']);assert root.tag.endswith('svg')
                assert not any(e.tag.endswith(('image','script','foreignObject'))for e in root.iter())
                ps=q['private_math']['exact_points'];(x1,u1),(x2,u2)=[[sp.Rational(t)for t in z]for z in ps]
                z,l=sp.symbols('z l');sol=sp.solve([z*x1+z+l-u1,z*x2+z+l-u2],[z,l])
                assert sol[z]==sp.Rational(p['p']) and sol[l]==sp.Rational(p['L'])
                for x,u in [(x1,u1),(x2,u2)]:assert sp.simplify(sp.exp(sol[l])*sp.exp(sol[z]*x+sol[z])-sp.exp(u))==0
                layout=q['assets'][0]['layout_checks']
                points=layout['label_points']
                for label_index,box in enumerate(layout['label_boxes']):
                    assert not intersect(box,*layout['line_segment'])
                    assert all(not intersect(box,*axis)for axis in layout['axes'])
                    assert all(0 <= x <= 1200 for x in [box[0],box[2]]) and all(0 <= y <= 640 for y in [box[1],box[3]])
                    def distance(point):
                        dx=point[0]-min(max(point[0],box[0]),box[2]);dy=point[1]-min(max(point[1],box[1]),box[3])
                        return math.sqrt(dx*dx+dy*dy)
                    assert distance(points[label_index])<distance(points[1-label_index])
                    centre=((box[0]+box[2])/2,(box[1]+box[3])/2)
                    assert math.dist(centre,points[label_index])<math.dist(centre,points[1-label_index])
                origin_box=layout['origin_label']['box']
                assert not intersect(origin_box,*layout['line_segment'])
                assert all(not intersect(origin_box,*axis)for axis in layout['axes'])
                assert len(set(layout['labels']))==2 and all(label in ''.join(root.itertext())for label in layout['labels'])
                outcomes['p-positive'if sol[z]>0 else 'p-negative']=outcomes.get('p-positive'if sol[z]>0 else 'p-negative',0)+1
                if index in [0,5,23,54,72,107,135,188,269]:gallery.append(dict(parameters=p,svg=q['assets'][0]['svg']))
            else:
                a=sp.Integer(p['b'])**p['m'];xx=sp.Rational(q['private_math']['x'])
                assert sp.simplify(p['b']**(p['c']*a)*a**xx-p['b']**p['q'])==0
                assert xx!=0 and a!=p['b']*p['m']and a!=p['m']**p['b']
                emitted=re.search(r'\$x=([^$]+)\$',q['parts'][1]['reference_answer']).group(1)
                assert parse_exact_latex(emitted)==xx
                outcomes['positive-x'if xx>0 else 'negative-x']=outcomes.get('positive-x'if xx>0 else 'negative-x',0)+1
            if index in [0,len(ch['parameters'])//2,len(ch['parameters'])-1]:samples.append(dict(recipe_id=ch['recipe_id'],branch_id=branch,parameters=p,instance=q))
            ns+=1
        result[branch]=dict(generated_instances=ns,unique_whole_card_exposure_key_tuples=len(keys),subdecision_key_count=len(subkeys),outcomes=outcomes,stable_criterion_ids=sorted(allids),strict_fresh_upper_bound=ch['strict_fresh_upper_bound'])
    fs=fixtures()
    for f in fs:
        q=M.build(f['recipe_id'],f['branch_id'],f['parameters']);local={c['local_criterion_id']for p in q['parts']for c in p['criteria']}
        assert set(f['expected_gross_earned_local_criterion_ids'])<=local
        if f['expected_net_marks']is not None:
            gross=len(f['expected_gross_earned_local_criterion_ids']);penalty=1 if 'misread'in f else 0
            assert gross-penalty==f['expected_net_marks']
        else:assert f['pending_clarification']
    # Seed-independent builder rejects inadmissible tuples rather than extending scope.
    rejected=0
    negative_cases=[
        dict(recipe_id=M.RECIPES[0],branch_id='degree-cycle',parameters=dict(a=2,b=2,c=1),reason='excluded equal-coefficient diagnostic collision'),
        dict(recipe_id=M.RECIPES[1],branch_id='solve-or-explain',parameters=dict(k=3,theta='-pi/3'),reason='exact Cambridge original excluded'),
        dict(recipe_id=M.RECIPES[2],branch_id='graph-intercept',parameters=dict(L='0',p='1/2',x1=1,delta_x=2),reason='zero-log-amplitude diagnostic collision'),
        dict(recipe_id=M.RECIPES[2],branch_id='gradient-target',parameters=dict(b=2,c=1,m=2,q=10),reason='nondiagnostic exponentiation collision')]
    for ch in choices:
        # These are numerically equal to an admitted row and would pass a plain
        # ``parameters in domain`` test. Exact runtime scalar types must differ.
        params=dict(ch['parameters'][0])
        integer_key=next(k for k,v in params.items() if type(v) is int)
        params[integer_key]=float(params[integer_key])
        negative_cases.append(dict(recipe_id=ch['recipe_id'],branch_id=ch['branch_id'],parameters=params,reason='equal-valued float must not replace a canonical integer'))
        params=dict(ch['parameters'][0])
        bool_key=next((k for k,v in params.items() if type(v) is int and v in (0,1)),None)
        if bool_key is not None:
            params[bool_key]=bool(params[bool_key])
            negative_cases.append(dict(recipe_id=ch['recipe_id'],branch_id=ch['branch_id'],parameters=params,reason='equal-valued Boolean must not replace a canonical integer'))
    for case in negative_cases:
        rid,bid,p=case['recipe_id'],case['branch_id'],case['parameters']
        try:M.build(rid,bid,p)
        except ValueError:rejected+=1
        else:raise AssertionError(('invalid tuple accepted',rid,bid,p))
    assert rejected==11
    return dict(schema='8227-stage-e-trig-log-author-check-v1',status='pass',branches=result,generated_instances=sum(v['generated_instances']for v in result.values()),rubric_expectation_fixtures=len(fs),invalid_domain_negatives_rejected=rejected,
                invalid_domain_negative_cases=negative_cases,
                oracle_methods=['75-digit tangent-half-angle polynomial and direct original-equation substitution','symbolic principal-inverse consistency and forced-candidate obstruction','independent simultaneous linear equations and original exponential substitution','original-base index-law target recomputation','independent orientation-segment graph-label intersection check'],
                limitations=['Same-vendor author check, not cross-vendor content acceptance.','Fixture expected awards validate memo arithmetic/IDs; no free-text, sketch, photo or handwriting marker has been exercised.','Graph geometry and SVG structure checked for all270; actual app renderer and learner UI not tested.','No resource registry activation, imports, classroom delivery, learner assignments or production operations.'],carry_forward=['R-form endpoint/tangent misread eligibility and canonical routes remain explicit E/F acceptance fixtures.','Log target misread as prefactor can change difficulty; do not auto-approve MR03 eligibility.','Competing eligible misread data sharing one earned A/B remain a common-marker settlement-order fixture.']),samples,fs,gallery,rounding_rows,sorted(math_expressions)


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--check',action='store_true');args=ap.parse_args()
    report,samples,fs,gallery,rounds,math_expressions=run()
    files={WB/'authoring/trig-log-check.json':report,WB/'authoring/trig-log-frozen-examples.json':samples,WB/'authoring/trig-log-marking-fixtures.json':fs,WB/'authoring/trig-log-rounding-oracle.json':rounds,WB/'authoring/trig-log-math-expressions.json':math_expressions}
    for file,value in files.items():
        data=json.dumps(value,indent=2,ensure_ascii=False)+'\n'
        if args.check:assert file.read_text()==data,('stale author evidence',file)
        else:file.write_text(data)
    gallery_dir=WB/'authoring/trig-log-gallery';gallery_dir.mkdir(exist_ok=True)
    index=[]
    for i,row in enumerate(gallery):
        p=gallery_dir/f'graph-{i:02d}.svg';data=row['svg']
        if args.check:assert p.read_text()==data
        else:p.write_text(data)
        index.append(dict(parameters=row['parameters'],path=str(p.relative_to(WB)),sha256=sha(data.encode())))
    data=json.dumps(index,indent=2)+'\n';p=gallery_dir/'index.json'
    if args.check:assert p.read_text()==data
    else:p.write_text(data)
    print(json.dumps(dict(status=report['status'],generated_instances=report['generated_instances'],rubric_expectation_fixtures=len(fs),rejected_negative_domains=report['invalid_domain_negatives_rejected']),indent=2))


if __name__=='__main__':main()
