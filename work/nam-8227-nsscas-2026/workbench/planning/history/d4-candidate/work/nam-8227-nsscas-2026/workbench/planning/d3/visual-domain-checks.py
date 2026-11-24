"""Stage-D3 finite-domain/discrimination audit; not a runtime generator.

Enumerates design tuples and named wrong-method models only. It never emits
questions, instances, solutions or learner assignments. Source D0 is archived.
"""
from pathlib import Path
from fractions import Fraction
from decimal import Decimal, localcontext, ROUND_HALF_UP
from itertools import product, combinations
import argparse,json,hashlib
import mpmath as mp
WB=Path(__file__).resolve().parents[2]
DEST=WB/'planning/d3/visual-domain-checks.json'

def sig(value,n=3):
    with localcontext()as ctx:
        ctx.prec=85
        x=Decimal(str(value))
        if not x:return '0'
        return format(x.quantize(Decimal(1).scaleb(x.adjusted()-n+1),rounding=ROUND_HALF_UP),'f')

def decimal_angle(r,s):
    with mp.workdps(80):
        theta=mp.acos(mp.mpf(s+r-1)/mp.sqrt((r*r+2)*(s*s+2)))*180/mp.pi
        with localcontext()as ctx:
            ctx.prec=85
            return str(theta),format(Decimal(str(theta)).quantize(Decimal('.1'),rounding=ROUND_HALF_UP),'f')

def modulus_reasons(a,b,d):
    c=-a*d;y=a*abs(b)+c;reasons=[]
    if Fraction(-c,d*d)==a:reasons.append('parabola-via-zero-gives-canonical-a')
    if Fraction(y-c,b*b)==a:reasons.append('parabola-via-y-intercept-gives-canonical-a')
    if y==b:reasons.append('read-b-from-y-intercept-gives-canonical-b')
    if(a,b,d)==(-2,-3,1):reasons.append('excluded-official-original-2023-P2-Q2')
    return reasons

def vector_reasons(r,s,t):
    p=Fraction(s+t-1,2+r*t);badcoef=3-s+r*t-t;out=[]
    if r==t:out.append('A-equals-C')
    if p==0:out.append('wrong-p-times-difference-gives-canonical-p0')
    if badcoef==0:out.append('wrong-p-times-difference-produces-identity')
    return out

def trapezium_reasons(h,L,n,k):
    reasons=[]
    if(h,L,n)==(2,8,4):reasons.append('excluded-official-original-parts-2023-P2-Q6-for-all-k')
    if(L,n,k)==(4,4,2):reasons.append('square-estimate-collides-at-marked-3sf')
    if h not in[1,2,3]or L not in[4,8]or n not in[2,4]or k not in[1,2,3]:reasons.append('outside-reviewed-trapezium-domain')
    return reasons

def generated_fresh_trapezium_reasons(h,L,n,k):
    reasons=trapezium_reasons(h,L,n,k)
    if h==2:reasons.append('h2-sketch-is-attributed-original-subtask-not-generated-fresh')
    return reasons

def build():
    modulus=[];modremoved=[]
    for a,b,d in product([-3,-2,-1,1,2,3],[-3,-2,-1,1,2,3],[1,2,3]):
        c=-a*d;y=a*abs(b)+c;why=modulus_reasons(a,b,d);row=dict(parameters=dict(a=a,b=b,d=d),canonical_coefficients=[a,b,c],reasons=why)
        if why:modremoved.append(row);continue
        assert Fraction(-c,d*d)!=a and Fraction(y-c,b*b)!=a and y!=b
        assert -b!=b and y!=c # other named vertex/y-intercept misreads never collide
        assert all(a*abs(x+b)+c==yy for x,yy in[(-b,c),(-b-d,0),(-b+d,0),(0,y)])
        row['semantic_key']=['modulus-model',a,b,d];row['part_keys']={'a':['modulus-model',a,b,d]};modulus.append(row)
    assert len(modulus)==44 and len(modremoved)==64
    crowded=[];origin=[]
    for row in modulus:
        a,b,d=[row['parameters'][k]for k in['a','b','d']];c=-a*d;pts=set([(-b,c),(-b-d,0),(-b+d,0),(0,a*abs(b)+c)])
        if any(0<(x-u)**2+(y-v)**2<=2 for (x,y),(u,v)in combinations(pts,2)):crowded.append(row['parameters'])
        if abs(b)==d:origin.append(row['parameters'])
    vectors=[];vecremoved=[]
    for r,s,t in product([1,2,3],[-3,-2,-1,1,2,3],[1,2,3]):
        why=vector_reasons(r,s,t);p=Fraction(s+t-1,2+r*t);row=dict(parameters=dict(r=r,s=s,t=t),p=str(p),reasons=why)
        if why:vecremoved.append(row);continue
        u=(1,r,1);v=(s,1,-1);w=(1,t,1);res=tuple(p*x-y for x,y in zip(u,v));assert sum(x*y for x,y in zip(res,w))==0 and res!=(0,0,0)
        assert r!=t and p!=0 and(3-s+r*t-t)!=0
        dot=s+r-1;nu=r*r+2;nv=s*s+2;dist=sum((x-y)**2 for x,y in zip(u,v));assert Fraction(nu+nv-dist,2)==dot and dot*dot<nu*nv
        th,rounded=decimal_angle(r,s);row.update(angle_degrees=th,angle_1dp=rounded,part_keys={'a':['vector-perpendicular',r,s,t],'b':['vector-angle',r,s]},semantic_key=['vector-complete',r,s,t],reverse_ray_error_applicable=dot!=0)
        # A right angle remains right when a ray is reversed; that is a valid
        # geometrical equivalence, not a named wrong-method collision.
        if dot!=0:assert Decimal(rounded)!=Decimal(sig(180-mp.mpf(th),5)).quantize(Decimal('.1'))
        vectors.append(row)
    assert len(vectors)==30 and len(vecremoved)==24
    fixtures=[]
    for r,s in[(1,-2),(1,2),(2,-3),(2,1),(3,3)]:
        for t in[1,2,3]:
            exact,canonical=decimal_angle(r,s)
            with mp.workdps(80):
                normu=mp.mpf(sig(mp.sqrt(r*r+2)));normv=mp.mpf(sig(mp.sqrt(s*s+2)));theta=mp.acos(mp.mpf(s+r-1)/(normu*normv))*180/mp.pi
                with localcontext()as ctx:
                    ctx.prec=85;prem=format(Decimal(str(theta)).quantize(Decimal('.1'),rounding=ROUND_HALF_UP),'f')
                    cos3=mp.mpf(sig(mp.mpf(s+r-1)/mp.sqrt((r*r+2)*(s*s+2))))
                    prem_cos=format(Decimal(str(mp.acos(cos3)*180/mp.pi)).quantize(Decimal('.1'),rounding=ROUND_HALF_UP),'f')
                    both3=mp.mpf(sig(mp.mpf(s+r-1)/(normu*normv)))
                    prem_both=format(Decimal(str(mp.acos(both3)*180/mp.pi)).quantize(Decimal('.1'),rounding=ROUND_HALF_UP),'f')
            changing=[name for name,value in [('norms3sf',prem),('cos3sf',prem_cos),('norms-and-cos3sf',prem_both)]if value!=canonical]
            assert changing,('reviewer rounding fixture lacks a demonstrated changing route',r,s,t)
            fixtures.append(dict(parameters=dict(r=r,s=s,t=t),original_D0_fixture=True,D1_admitted=not vector_reasons(r,s,t),D1_exclusion_reasons=vector_reasons(r,s,t),canonical_angle_degrees=exact,canonical_1dp=canonical,premature_norms_3sf_angle_1dp=prem,premature_cos_3sf_angle_1dp=prem_cos,premature_norms_and_cos_3sf_angle_1dp=prem_both,rounding_routes_changing_final=changing,expected_marking='If submitted route prematurely rounds and loses the final digit: retain genuine B/M work, b:A1=0; give premature-rounding feedback. Removed tuples remain negative regression fixtures.'))
    assert len(fixtures)==15 and sum(f['D1_admitted']for f in fixtures)==9
    trapezium=[];trapremoved=[]
    for h,L,n,k in product([1,2,3],[4,8],[2,4],[1,2,3]):
        why=trapezium_reasons(h,L,n,k)
        if why:trapremoved.append(dict(parameters=dict(h=h,L=L,n=n,k=k),reasons=why));continue
        with mp.workdps(80):
            dx=mp.mpf(L)/n;ys=[mp.log(1+j*dx)for j in range(n+1)];T=dx*(ys[0]+ys[-1]+2*sum(ys[1:-1]))/2;integral=(L+1)*mp.log(L+1)-L
            assert T<integral
            a=sig(T);canonical=sig(2*k*T);ft=Decimal(a)*(2*k);accepted=sorted({canonical,format(ft,'f'),sig(ft)},key=Decimal)
            assert sig(T*T)!=canonical and sig(k*T)!=canonical # compare at marked precision, not only unrounded values
            wrong_single_interior=dx*(ys[0]+ys[-1]+sum(ys[1:-1]))/2
            wrong_double_last=dx*(ys[0]+2*ys[-1]+2*sum(ys[1:-1]))/2
            assert sig(wrong_single_interior)!=a and sig(wrong_double_last)!=a and sig(-T)!=a
            row=dict(parameters=dict(h=h,L=L,n=n,k=k),a_exact_log_value=str(T),a_3sf=a,b_canonical_3sf=canonical,b_canonical_path_fixture_strings=accepted,b_accepted_answer_rule='B2 judges2k times the learner own(a) value visible in final or working; exact product or any3sf-correct rendering of that product. Canonical-path fixture strings are non-exhaustive.',semantic_key=['trapezium-context',L,n,k],part_keys={'a':['trapezium-quadrature',L,n],'b':['trapezium-hence',L,n,k],'c':['log-sketch',h],'d':['own-log-chord-context',h,L,n]},bias_outcome='underestimate')
            row['allowed_delivery_route']='attributed-original-subtask mixed practice only'if h==2 else'generated-fresh subject to exposurekeys'
            trapezium.append(row)
    assert len(trapezium)==30 and len(trapremoved)==6
    trapkeys={tuple(r['semantic_key'])for r in trapezium};partcounts={p:len({tuple(r['part_keys'][p])for r in trapezium})for p in['a','b','c','d']}
    assert len(trapkeys)==11 and partcounts==dict(a=4,b=11,c=3,d=11)
    # Mathematical packing3 includes h2, which is an attributed-original sketch subtask.
    # Strict generated-fresh pool blocks that part key, leaving packing2.
    pack=[next(r for r in trapezium if tuple(r['parameters'].values())==z)for z in[(1,4,2,1),(2,4,4,3),(3,8,2,3)]]
    assert all(len({tuple(row['part_keys'][p])for row in pack})==3 for p in['a','b','c','d'])
    generated=[row for row in trapezium if not generated_fresh_trapezium_reasons(**row['parameters'])];assert len(generated)==22
    assert {part:len({tuple(row['part_keys'][part])for row in generated})for part in['a','b','c','d']}==dict(a=4,b=11,c=2,d=8)
    generatedpack=[next(row for row in generated if tuple(row['parameters'].values())==z)for z in[(1,4,2,1),(3,8,2,3)]]
    assert all(len({tuple(row['part_keys'][part])for row in generatedpack})==2 for part in['a','b','c','d'])
    doc=dict(version='8227-stage-D3-visual-audit-0.1.3',status='pass',scope='Finite planner-domain and discrimination audit only; no runtime generation/marking acceptance.',branches=[
        dict(recipe_id='WB8227-modulus-graph-recovery',branch_id='vertex-intercepts',raw_domain_count=108,admitted_raw_count=44,semantic_task_count=44,part_semantic_counts={'a':44},strict_all_assessed_parts_unseen_capacity=44,removed=modremoved,admitted=modulus,named_error_checks=['parabola coefficient via zero','parabola coefficient via y-intercept','b read as y-intercept','b read as vertex x','c read as y-intercept','official tuple excluded'],remaining_accidental_named_error_successes=0,later_render_fixture_counts=dict(crowded_D0=28,crowded_D1=len(crowded),origin_merge_D0=36,origin_merge_D1=len(origin)),crowded_render_fixtures=crowded,origin_merge_fixtures=origin),
        dict(recipe_id='WB8227-vector-geometry',branch_id='scalar-combination-and-origin-angle',raw_domain_count=54,admitted_raw_count=30,semantic_task_count=30,part_semantic_counts={'a':30,'b':17},strict_all_assessed_parts_unseen_capacity=17,removed=vecremoved,admitted=vectors,named_error_checks=['p(OA-OB) gives p0 or identity','A=C cross-part collapse','reversed ray with no supplementary correction when angle not90'],remaining_accidental_named_error_successes=0,exact_right_angle_admitted=sum(r['angle_1dp']=='90.0'for r in vectors),right_angle_reverse_ray_note='At90 reversing a ray is geometrically equivalent and not incorrect working. Exact60/90 values are accepted without trailing decimal zero.'),
        dict(recipe_id='WB8227-trapezium-sketch-estimate',branch_id='logarithmic-hence-chain',raw_domain_count=36,admitted_raw_count=30,semantic_task_count=11,part_semantic_counts=partcounts,strict_all_assessed_parts_unseen_capacity=2,mathematical_packing_witness=[r['parameters']for r in pack],mathematical_all_parts_unseen_packing=3,strict_generated_fresh_capacity=2,fully_generated_raw_presentations=22,fully_generated_part_semantic_counts={'a':4,'b':11,'c':2,'d':8},generated_fresh_packing_witness=[r['parameters']for r in generatedpack],blocked_generated_fresh_part_keys=[['log-sketch',2]],canonical_bias_outcome_classes=1,raw_to_semantic_presentation_collisions=19,removed=trapremoved,admitted=trapezium,comparison_precision='Decimal half-up3sf, same comparison as marked final answers; canonical path fixtures non-exhaustive',named_error_checks=['square estimate instead of log-law scaling','omit logarithm power2','negative width; omit interior factor2; double nonzero last endpoint','claim bias from monotonicity without chord evidence'],remaining_accidental_named_error_successes=0,bias_discrimination_limit='Underestimate is fixed across this branch. Apply3 only; d semantic identity uses the actual own-graph/chord context, not the word underestimate. A monotonicity-only explanation is rejected for its missing credited reason, not because its verdict differs.',premature_rounding_limit='2dp ordinate rounding visibly changes canonical(a) only for L4,n4. Method evidence and rounding feedback remain distinct; no domain change.')])
    trailing_zero=[]
    for r,ss,t in [(3,-1,1),(3,3,1),(3,3,2)]:
        exact,canonical=decimal_angle(r,ss);assert canonical in ['80.0','63.0']
        trailing_zero.append(dict(parameters=dict(r=r,s=ss,t=t),angle_degrees=exact,accepted_strings=[canonical,canonical+'°'],rejected_strings=[str(int(Decimal(canonical))),str(int(Decimal(canonical)))+'°'],reason='Non-exact angle: requested1dp form is assessed even when numeric value is an integer. Exact60/90 retain their exception.'))
    return doc,dict(status='frozen-stage-E/F-regression-fixtures',original_fixture_count=15,D1_admitted=9,D1_filtered=6,fixtures=fixtures,nonexact_trailing_zero_fixtures=trailing_zero)

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--check',action='store_true');parser.add_argument('--negative-fixture',choices=['modulus-parabola','vector-wrong-resultant','trapezium-original','trapezium-original-part','trapezium-original-sketch','trapezium-precision-collision']);a=parser.parse_args();doc,fixtures=build()
    if a.negative_fixture=='modulus-parabola':
        assert not modulus_reasons(-2,3,1),'seeded modulus named-error collision rejected: parabola gives canonical a'
    if a.negative_fixture=='vector-wrong-resultant':
        assert not vector_reasons(1,-1,2),'seeded vector named-error collision rejected: p0 from wrong resultant'
    if a.negative_fixture=='trapezium-original':
        assert not trapezium_reasons(2,8,4,3),'seeded trapezium official-original tuple rejected'

    if a.negative_fixture=='trapezium-original-part':
        assert not trapezium_reasons(2,8,4,1),'seeded trapezium original subpart forchanged k rejected'
    if a.negative_fixture=='trapezium-original-sketch':
        assert not generated_fresh_trapezium_reasons(2,4,2,1),'seeded h2originalsketch asgeneratedfresh rejected'
    if a.negative_fixture=='trapezium-precision-collision':
        assert not trapezium_reasons(1,4,4,2),'seeded marked-precision squaring collision rejected'

    outputs={DEST:doc,WB/'planning/d3/visual-rounding-fixtures.json':fixtures}
    for p,d in outputs.items():
        text=json.dumps(d,indent=2,ensure_ascii=False)+'\n'
        if a.check:assert p.read_text()==text,('stale visual design audit',str(p))
        else:p.write_text(text)
    print(json.dumps(dict(status='pass',domain_counts=[r['admitted_raw_count']for r in doc['branches']],semantic_counts=[r['semantic_task_count']for r in doc['branches']],strict_wholly_unseen_counts=[r['strict_all_assessed_parts_unseen_capacity']for r in doc['branches']],rounding_fixtures=15),indent=2))
if __name__=='__main__':main()
