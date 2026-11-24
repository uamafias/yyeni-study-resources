"""D1 finite design/discrimination checks; not a question generator or marker.

No learner items are emitted. Wrong-method comparisons inspect the declared finite
mathematics, while fixed credit examples are manually specified expectations.
"""
from pathlib import Path
from fractions import Fraction
from decimal import Decimal, ROUND_HALF_UP
import argparse,collections,hashlib,itertools,json,math
import mpmath as mp
import sympy as sp

WB=Path(__file__).resolve().parents[2]
mp.mp.dps=80

def rnd(x,places):
    return str(Decimal(str(x)).quantize(Decimal('1').scaleb(-places),rounding=ROUND_HALF_UP))

def roots_phase(a,b,c):
    R=mp.sqrt(a*a+b*b);al=mp.degrees(mp.atan2(b,a));be=mp.degrees(mp.asin(c/R))
    rs=sorted({v-al for k in range(-1,3) for v in [be+360*k,180-be+360*k] if 0<v-al<360})
    assert len(rs)==2
    return R,al,be,rs

def roots_half_angle(a,b,c):
    # Separate oracle: solve (b+c)t²-2at+(c-b)=0, t=tan(theta/2).
    A=b+c;B=-2*a;C=c-b
    if A:
        disc=B*B-4*A*C;assert disc>0
        ts=[(-B+mp.sqrt(disc))/(2*A),(-B-mp.sqrt(disc))/(2*A)];rs=[]
    else:
        assert B;ts=[mp.mpf(-C)/B];rs=[mp.mpf(180)]
    rs +=[(2*mp.degrees(mp.atan(t)))%360 for t in ts]
    return sorted(rs)

def signature(xs):return tuple(sorted(rnd(x,1)for x in xs))
def same(x,y,tol=mp.mpf('1e-45')):return abs(mp.mpf(x)-mp.mpf(y))<tol

def rform():
    grid=list(itertools.product(range(1,5),range(1,5),range(-3,4)))
    feasible=[t for t in grid if t[2]**2<t[0]**2+t[1]**2]
    endpoints=[t for t in feasible if t[2]!=t[1]]
    old=[t for t in endpoints if math.gcd(math.gcd(t[0],t[1]),abs(t[2]))==1]
    knife={(1,4,-3),(1,4,3),(4,1,-3),(4,1,3),(2,4,-1),(2,4,1),(3,4,-2),(3,4,2)}
    rounded=[t for t in old if t not in knife];diag=[t for t in rounded if t[0]==t[1]];domain=[t for t in rounded if t[0]!=t[1]]
    assert [len(x)for x in [grid,feasible,endpoints,old,rounded,domain]]==[112,102,90,78,70,58]
    errors=collections.defaultdict(list);classes=collections.Counter();subclasses=collections.Counter();maxres=mp.mpf(0)
    for t in domain:
        a,b,c=t;R,al,be,rs=roots_phase(*t);oracle=roots_half_angle(*t)
        assert all(same(x,y)for x,y in zip(rs,oracle))
        for x in rs:maxres=max(maxres,abs(a*mp.sin(mp.radians(x))+b*mp.cos(mp.radians(x))-c))
        cls='c>b'if c>b else'c=0'if c==0 else'nonzero c<b';classes[cls]+=1;subclasses['positive wrap'if 0<c<b else'negative sine'if c<0 else cls]+=1
        if rnd(mp.degrees(mp.atan2(a,b)),2)==rnd(al,2):errors['inverted_phase_ratio'].append(t)
        if rnd(mp.atan2(b,a),2)==rnd(al,2):errors['radian_numeric_phase_reported_as_degrees'].append(t)
        if same(a+b,R):errors['amplitude_sum'].append(t)
        if a>=b and same(mp.sqrt(a*a-b*b),R):errors['amplitude_difference_of_squares'].append(t)
        # Explicit named incorrect root procedures; compare the full requested response.
        if signature([be-al])==signature(rs):errors['principal_root_only'].append(t)
        shifted=[x+al for x in rs]
        if signature(shifted)==signature(rs):errors['forget_phase_subtraction'].append(t)
        if signature([rs[0],180-rs[0]])==signature(rs):errors['second_root_180_minus_final_first'].append(t)
        coterminal=rs[1]-360;assert coterminal<0 and len({rnd(rs[0],1),rnd(rs[1],1),rnd(coterminal,1)})==3
    assert not any(errors.values()),dict(errors)
    assert dict(classes)=={'nonzero c<b':42,'c=0':10,'c>b':6}
    fixtures=[]
    for t in sorted(knife):
        R,al,be,rs=roots_phase(*t);ar=mp.mpf(rnd(al,2));br=mp.mpf(rnd(be,2));rounded_roots=sorted({v-ar for k in range(-1,3)for v in [br+360*k,180-br+360*k]if 0<v-ar<360})
        fixtures.append({'tuple':list(t),'exact_roots':[str(x)for x in rs],'canonical_1dp':[rnd(x,1)for x in rs],'using_both_2dp_angles':[str(x)for x in rounded_roots],'both_2dp_final':[rnd(x,1)for x in rounded_roots],'changed_root':signature(rs)!=signature(rounded_roots),'admitted_D1':False})
    phases=[]
    for a,b in [(1,2),(2,1),(1,3),(3,1),(2,4),(4,2)]:
        R=mp.sqrt(a*a+b*b);al=mp.degrees(mp.atan2(b,a));R5=mp.mpf(mp.nstr(R,5));bad=mp.degrees(mp.acos(a/R5));phases.append({'a':a,'b':b,'canonical_alpha':str(al),'canonical_2dp':rnd(al,2),'rounded_R_5sf':str(R5),'alpha_via_rounded_R':str(bad),'alpha_2dp_via_rounded_R':rnd(bad,2),'stage_EF_marker_fixture_not_runtime_pass':True})
    return {'raw_counts':{'grid':112,'feasible':102,'endpoint_filtered':90,'primitive_D0':78,'rounding_filtered':70,'diagnostic_D1':58},'removed_rounding_tuples':[list(x)for x in sorted(knife)],'removed_inverse_ratio_tuples':[list(x)for x in diag],'removal_sets_disjoint':not bool(knife&set(diag)),'part_semantic_capacities':{'a_convert_prompts':len({(a,b)for a,b,c in domain}),'a_phase_ratio_classes':len({(a//math.gcd(a,b),b//math.gcd(a,b))for a,b,c in domain}),'b_root_equations':len(domain)},'root_classes':dict(classes),'root_subclasses':dict(subclasses),'named_errors_tested':['inverted_phase_ratio','radian_numeric_phase_reported_as_degrees','amplitude_sum','amplitude_difference_of_squares','principal_root_only','forget_phase_subtraction','second_root_180_minus_final_first'],'canonical_response_collisions_remaining':dict(errors),'independent_half_angle_oracle':'58/58agree','max_original_residual':str(maxres),'rounding_exclusion_fixtures':fixtures,'near_2dp_phase_fixtures':phases},domain

def principal():
    theta=[-sp.pi,-3*sp.pi/4,-2*sp.pi/3,-sp.pi/3,-sp.pi/4,-sp.pi/6,sp.pi/6,sp.pi/4,sp.pi/3,2*sp.pi/3,3*sp.pi/4,sp.pi]
    raw=list(itertools.product([2,3,4,5],theta));domain=[(k,t)for k,t in raw if not(k==3 and t==-sp.pi/3)]
    valid=[];invalid=[]
    for k,t in domain:
        v=sp.sin(t)/k;inverse=sp.simplify(sp.asin(k*v));good=bool(-sp.pi/2<=t<=sp.pi/2)
        assert (sp.simplify(inverse-t)==0)==good
        (valid if good else invalid).append({'k':k,'theta':str(t),'forward_only_candidate':str(v),'actual_principal_inverse':str(inverse)})
    assert len(raw)==48 and len(domain)==47 and len(valid)==23 and len(invalid)==24
    # The full canonical response includes P-B1/P-M1 reasoning. Value-level
    # accidental success on real targets is deliberately disclosed, not hidden.
    return {'one_uncued_branch':True,'public_marks_every_outcome':3,'raw_grid':48,'original_equation_excluded':{'k':3,'theta':'-pi/3','source':'9709/12/F/M/2016Q4(a)'},'raw_admitted':47,'semantic_target_keys':len({str(t)for k,t in domain}),'valid_target_keys':len({x['theta']for x in valid}),'invalid_target_keys':len({x['theta']for x in invalid}),'valid_numeric_variants':len(valid),'obstruction_raw_variants':len(invalid),'named_error':'take sine and accept candidate without checking the principal inverse','value_level_error_coincidences':valid,'error_rejected_by_inverse_consistency':invalid,'discrimination_limit':'23valid numeric variants are non-diagnostic for the range misconception by value alone; forward-only working lacks P-B1 and cannot earn full3. Invalidtargets expose the error. Do not claim0value-levelcollisions.','unexplained_bare_conclusions_expected_credit':0,'valid_substitution_contradiction_expected_credit':3,'fixture_scope':'Manual design-credit expectations; no runtime marker executed'},domain

def qmp(x):
    x=Fraction(x);return mp.mpf(x.numerator)/x.denominator

def graph():
    Ls=[Fraction(-1),Fraction(1,2),Fraction(1),Fraction(2),Fraction(3)]
    ps=[Fraction(-3,4),Fraction(-1,2),Fraction(-1,4),Fraction(1,4),Fraction(1,2),Fraction(3,4)]
    domain=[];collisions=collections.defaultdict(list);invalid_extra_log=0;zeroordinates=0;mixedsign=0
    names=['omit_offset','first_ordinate_as_intercept','extra_log_of_already_log_ordinate','wrong_product_log_model','wrong_base_antilog','invert_gradient']
    for L,p,x1,dx in itertools.product(Ls,ps,[1,2,3],[1,2,3]):
        x2=x1+dx;u1=p*x1+p+L;u2=p*x2+p+L;A=mp.exp(qmp(L));pf=qmp(p);key=[str(L),str(p),x1,dx]
        assert (u2-u1)/dx==p and u1-p*x1-p==L
        # Independent original-model check at both actual abscissae.
        for x,u in [(x1,u1),(x2,u2)]:assert same(mp.log(A*mp.exp(pf*(x+1))),qmp(u))
        if same(mp.exp(qmp(L+p)),A):collisions['omit_offset'].append(key)
        if same(mp.exp(qmp(u1-p)),A):collisions['first_ordinate_as_intercept'].append(key)
        if same(mp.power(10,qmp(L)),A):collisions['wrong_base_antilog'].append(key)
        if same(1/pf,pf):collisions['invert_gradient'].append(key)
        bad1=A*pf*(x1+1);bad2=A*pf*(x2+1)
        if same(bad1,qmp(u1))and same(bad2,qmp(u2)):collisions['wrong_product_log_model'].append(key)
        if u1>0 and u2>0:
            badp=(mp.log(qmp(u2))-mp.log(qmp(u1)))/dx;badL=mp.log(qmp(u1))-badp*(x1+1);badA=mp.exp(badL)
            if same(badp,pf)and same(badA,A):collisions['extra_log_of_already_log_ordinate'].append(key)
        else:invalid_extra_log+=1
        zeroordinates+=int(u1==0 or u2==0);mixedsign+=int(u1*u2<0);domain.append((L,p,x1,dx))
    assert len(domain)==270 and not any(collisions.values()),dict(collisions)
    old_collisions=[]
    for p,x1,dx in itertools.product(ps,[1,2,3],[1,2,3]):
        A=mp.mpf(1);p0=qmp(p);u1=p*(x1+1);u2=p*(x1+dx+1)
        assert same(A*p0*(x1+1),qmp(u1))and same(A*p0*(x1+dx+1),qmp(u2));old_collisions.append([str(p),x1,dx])
    assert len(old_collisions)==54
    return {'D0_models':30,'D1_models':30,'D1_presentations':270,'recovered_amplitude_values':5,'gradient_values':6,'removed_L0_models':6,'removed_L0_presentations':54,'replaced_by_L_half_models':6,'old_wrong_product_log_collisions':old_collisions,'named_errors_tested':names,'canonical_full_parameter_collisions_remaining':dict(collisions),'extra_log_method_undefined_for_presentations':invalid_extra_log,'presentations_with_zero_ordinate':zeroordinates,'presentations_with_mixed_sign_ordinates':mixedsign,'raw_to_semantic_rule':'All9point-pair presentations for one(L,p) share a parameter-part exposure key.'},domain

def gradient():
    raw=list(itertools.product([2,3],[1,3],[2,3],[0,1,4,10,30]))
    mul=[t for t in raw if t[0]**t[2]==t[0]*t[2]]
    after=[t for t in raw if t not in mul];rev=[t for t in after if t[0]**t[2]==t[2]**t[0]]
    domain=[t for t in after if t not in rev]
    assert len(raw)==40 and len(mul)==10 and len(rev)==10 and len(domain)==20
    errors=collections.defaultdict(list);outputs=[];positive=0;negative=0
    for t in domain:
        b,c,m,q=t;a=b**m;x=Fraction(q-c*a,m)
        assert q!=c*a and c*a+m*x==q
        # Exact original powers, separate from the rearranged answer expression.
        original=sp.Integer(b)**(c*a)*sp.Integer(a)**sp.Rational(x.numerator,x.denominator)
        assert sp.simplify(original-sp.Integer(b)**q)==0
        if a==b*m:errors['multiply_base_gradient'].append(t)
        if a==m**b:errors['reverse_exponent'].append(t)
        if same(mp.power(10,m),a):errors['wrong_base10'].append(t)
        if same(mp.exp(m),a):errors['wrong_natural_base_without_plot_conversion'].append(t)
        if Fraction(q,m)==x:errors['omit_prefactor'].append(t)
        if x==0:errors['inspection_zero'].append(t)
        positive+=x>0;negative+=x<0;outputs.append(str(x))
    assert not any(errors.values()) and (3,2,2,4)not in domain
    assert all(not(b==3 and c==2 and m==2)for b,c,m,q in domain)
    return {'new_grid':40,'removed_multiplication_coincidences':[list(t)for t in mul],'removed_reversed_exponent_coincidences_after_multiply_filter':[list(t)for t in rev],'diagnostic_full_tuples':20,'parameter_model_keys':len({(b,c,m)for b,c,m,q in domain}),'exponentiation_subdecision_keys':len({(b,m)for b,c,m,q in domain}),'target_equation_tasks':20,'distinct_x_outcomes':len(set(outputs)),'positive_x':positive,'negative_x':negative,'zero_x':outputs.count('0'),'max_symbolic_prefactor_exponent':max(c*b**m for b,c,m,q in domain),'original_tuple_excluded':[3,2,2,4],'original_parameter_subpart_excluded':'No c2 triple is admitted; sourcepart(a) cannot be recycled with another target.','named_errors_tested':['multiply_base_gradient','reverse_exponent','wrong_base10','wrong_natural_base_without_plot_conversion','omit_prefactor','inspection_zero'],'canonical_collisions_remaining':dict(errors)},domain

def cases(doc,rd,pd,gd,td):
    checked=[]
    for recipe in doc['recipes']:
        for e in recipe['exemplar_cases']:
            p=e['parameters'];ans=e['expected_answers'];kind=e['branch_id']
            if recipe['recipe_id'].endswith('trig-rform-equation'):
                a,b,c=[p[k]for k in ['a','b','c']];assert(a,b,c)in rd
                roots=roots_half_angle(a,b,c);assert all(abs(x-y)<mp.mpf('1e-8')for x,y in zip(roots,ans['roots_degrees']))
                assert sp.simplify(sp.sympify(ans['R'])**2-a*a-b*b)==0
            elif recipe['recipe_id'].endswith('principal-inverse'):
                k=p['k'];theta=sp.sympify(p['theta']);assert(k,theta)in pd
                if ans['real_solution']:assert sp.simplify(sp.asin(k*sp.sympify(ans['x']))-theta)==0
                else:assert bool(theta<-sp.pi/2 or theta>sp.pi/2)
            elif kind=='graph-intercept':
                L=Fraction(str(p['L']));pp=Fraction(p['p']);x1=p['x1'];dx=p['x2']-x1;assert(L,pp,x1,dx)in gd
                exactA=sp.sympify(ans['A_exact']);assert sp.simplify(sp.log(exactA)-sp.Rational(L.numerator,L.denominator))==0
                for x,u in zip([x1,p['x2']],ans['log_ordinates']):assert Fraction(u)==pp*x+pp+L
            else:
                b,c,m,q=[p[k]for k in ['b','c','m','q']];assert(b,c,m,q)in td
                a=ans['a'];xx=sp.sympify(ans['x']);assert sp.simplify(sp.Integer(b)**(c*a)*sp.Integer(a)**xx-sp.Integer(b)**q)==0
            checked.append({'case_id':e['case_id'],'branch_id':kind,'role':e['case_role'],'marks':e['marks_total'],'result':'pass'})
    assert len(checked)==12
    return checked

def segment_box(P,Q,box):
    # Liang-Barsky intersection, including boundary contact.
    xmin,ymin,xmax,ymax=box;dx=Q[0]-P[0];dy=Q[1]-P[1];lo,hi=0.0,1.0
    for p,q in [(-dx,P[0]-xmin),(dx,xmax-P[0]),(-dy,P[1]-ymin),(dy,ymax-P[1])]:
        if p==0:
            if q<0:return False
        elif p<0:lo=max(lo,q/p)
        else:hi=min(hi,q/p)
        if lo>hi:return False
    return True

def records(doc):
    inputs=json.loads((WB/'planning/trig-model-source-reads.json').read_text());reads=inputs['readings']+inputs['repair_d1']['readings'];verified=0
    for r in reads:
        for pk,hk in [('source_path','source_sha256'),('render_path','render_sha256')]:
            assert hashlib.sha256(Path(r[pk]).read_bytes()).hexdigest()==r[hk],(r['reading_id'],pk)
        verified+=1
    diagrams=json.loads((WB/'planning/d1/trig-paper-diagrams.json').read_text());figs=[]
    for r in diagrams['figures']:
        for kind in ['svg','png']:assert hashlib.sha256(Path(r[kind+'_path']).read_bytes()).hexdigest()==r[kind+'_sha256']
        for b in r['label_geometry']:
            assert not b['opaque_box']and not segment_box(*r['line'],b['bbox']),(r['case_role'],b)
        figs.append({'case_role':r['case_role'],'label_line_bbox_overlap':False,'opaque_label_boxes':False,'result':'pass'})
    partrows=0
    for r in doc['recipes']:
        assert r['proposed_version']=='0.1.1'
        for b in r['branches']:
            assert sum(p['marks']for p in b['part_specs'])==b['marks_total']
            assert max(p['bloom']for p in b['part_specs'])==b['whole_bloom']
            for p in b['part_specs']:
                assert p['answer_only_marks']==0
                assert sum(c['value']for c in p['criteria'])==p['marks']
                assert p['primary_objective_id']in p['directly_assessed_objective_ids']
                partrows+=1
            for ref in b['examination_references']:
                if ref['relation']!='same-type':assert ref['learner_display']is False
    assert partrows==6
    return {'native_reading_hashes':verified,'D1_native_rereads':len(inputs['repair_d1']['readings']),'part_slots':partrows,'bare_answer_marks_each':0,'part_totals_and_branch_maxima':'pass','static_paper_diagrams':figs,'limit':'Only3staticlabel/linechecks; all270runtime presentation layouts, app notation and marker behavior remain stageE/F.'}

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--check-only',action='store_true');args=ap.parse_args()
    doc=json.loads((WB/'planning/trig-model-design.json').read_text());r,rd=rform();p,pd=principal();g,gd=graph();t,td=gradient();e=cases(doc,rd,pd,gd,td);v=records(doc)
    out={'subject':'NSSCAS Mathematics8227 December2020','owner':'Vitalis','role':'PLANNER','version':'0.1.1','status':'D1finite mathematics, named-error, exemplar and record checks pass; not independent review/runtime acceptance','branches':{'degree-cycle':r,'solve-or-explain':p,'graph-intercept':g,'gradient-target':t},'exemplar_checks':e,'record_checks':v,'manual_credit_expectations':[{'part':'all6assessedslots','bare_correct_answer':0,'basis':'OD-1/D1-MR01; no official bare-answer exception'},{'part':'principal','complete_inverse_substitution_contradiction':3,'basis':'P-B1/P-M1/P-A1; no rote interval sentence required'},{'part':'Rformb','complete_non_hence_method':0,'basis':'Actual2022RformtablehasnoSC; differentquestionSC1nottransferred'},{'part':'loggraph','wronglineomits_offset_but_gradient_and_coherent_coordinate_substitution_visible':3,'basis':'G-M1/G-A1/G-M2; state-or-imply B1requirescorrectline; finalamplitudeaccuracyfails'}]}
    if not args.check_only:(WB/'checks/plan-repair-d1-trig-validation.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({'branches_checked':4,'cases':len(e),'source_and_render_hashes':v['native_reading_hashes'],'rform':58,'principal_raw':47,'principal_semantic':12,'graph_models':30,'gradient':20,'status':'pass'},indent=2))

if __name__=='__main__':main()
