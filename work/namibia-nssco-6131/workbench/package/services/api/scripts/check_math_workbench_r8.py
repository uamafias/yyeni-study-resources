"""Independent numeric/domain and semantic checks; no DB or model calls."""
from collections import Counter
from fractions import Fraction
from pathlib import Path
from decimal import Decimal
import json,math,re,sys,types

API=Path(__file__).resolve().parents[1]
module=types.ModuleType('services');module.__path__=[str(API/'services')]
sys.modules.setdefault('services',module)
from services.math_workbench.registry import generate_question,recipes,validate_question
from services.math_workbench.content_format import display_content,validate_content


def check(seed_count=64):
    counts=Counter();states=set();divisors=set();parities=set()
    for seed in range(seed_count):
        for suffix in ('power-minus-2','power-minus-1','power-0','power-1','power-2','power-3','sum','exponential'):
            q=generate_question('wb6131:power-sum-exponential-graphs-'+suffix,seed)
            p=q['parameter_evidence'];target=Fraction(*p['target_rational'])
            assert len(re.findall(r'\d{12,}',q['stem']+str([part['prompt'] for part in q['parts']])))==0
            assert min(p['inputs'])<0<max(p['inputs'])
            assert (0 not in p['inputs'])==p['excluded_zero']
            if suffix.startswith('power-'):
                a=Fraction(*p['coefficient']);n=p['exponent']
                if n:
                    assert len(p['roots'])==(2 if n in (-2,2) else 1)
                    for x in p['roots']:
                        assert x not in p['inputs'] and -3<x<3 and x!=0
                        assert math.isclose(float(a)*x**n,float(target),rel_tol=1e-10,abs_tol=1e-10)
                else:
                    states.add(p['solution_kind'])
                    assert 'x^{0}' in q['parts'][2]['prompt']
                    assert (a==target)==(p['solution_kind']=='all_domain')
                    assert not p['roots']
            if suffix=='exponential':
                base=int(re.search(r'y=(\d+)\^x',q['stem'])[1])
                assert math.isclose(base**p['roots'][0],float(target),rel_tol=1e-10)
            if suffix=='sum':
                b,c=map(int,re.search(r'y=x\^2\+(\d+)x\+\\frac\{(\d+)\}',q['stem']).groups())
                for x in p['roots']:assert math.isclose(x*x+b*x+c/x,float(target),rel_tol=1e-8,abs_tol=1e-8)
            counts['graph_cases']+=1
        q=generate_question('wb6131:general-intersecting-line-loci',seed);p=q['parameter_evidence']
        origin=p['centre'];directions=[math.radians(p['rotation_degrees']+v) for v in (0,p['angle_degrees'])]
        assert len(p['intersections'])==4
        for x,y in p['intersections']:
            dx,dy=x-origin[0],y-origin[1]
            assert math.isclose(math.hypot(dx,dy),p['circle_radius'])
            distances=[abs(dx*math.sin(t)-dy*math.cos(t)) for t in directions]
            assert math.isclose(*distances,abs_tol=1e-9)
        assert 'four' in q['parts'][1]['reference_answer']
        counts['general_locus_cases']+=1
        q=generate_question('wb6131:contextual-direct-inverse-variation',seed);p=q['parameter_evidence']
        assert p['workers']*p['hours']==p['new_workers']*p['new_hours']
        assert q['parts'][1]['reference_answer']==f"N${p['new_mass']*p['price_per_kg']}"
        assert q['parts'][3]['reference_answer']==f"{p['worker_hours']//p['new_workers']} hours"
        counts['contextual_variation_cases']+=1
        for kind in ('telephone-bill','cell-phone-bill','till-receipt','payment-receipt','clothing-account'):
            q=generate_question('wb6131:'+kind,seed);p=q['parameter_evidence']
            actual=[int(Decimal(s)*100) for part in q['parts'] for s in re.findall(r'N\$(\d+\.\d{2})',part['reference_answer'])]
            assert actual==p['answers_cents']
            if kind=='telephone-bill':assert actual[-1]+p['credit_cents']-p['fixed_cents']==p['minutes']*p['rate_cents']
            if kind=='cell-phone-bill':assert actual[-1]+p['credit_cents']-p['fixed_cents']==(p['used_minutes']-p['included_minutes'])*p['rate_cents']
            if kind=='till-receipt':assert actual[-1]+actual[-2]==p['tendered_cents'] and actual[0]==p['quantity']*p['unit_price_cents']
            if kind=='payment-receipt':assert actual[0]+p['change_cents']==p['tendered_cents'] and sum(actual)==p['balance_cents']
            if kind=='clothing-account':assert actual[-1]+p['return_cents']+p['payment_cents']==p['opening_cents']+p['purchases_cents']
            counts['bill_receipt_cases']+=1
        q=generate_question('wb6131:ratio-all-shares',seed)
        answers=[part['reference_answer'] for part in q['parts']]
        assert len(set(re.sub(r'[A-Za-z$.,; ]','',s) for s in answers))==len(answers)
        q=generate_question('wb6131:exponential-equation-forms',seed)
        assert q['parts'][1]['reference_answer']!=q['parts'][2]['reference_answer']
        assert not re.search(r'\\frac\{[^{}]+\}\{1\}',str(q['parts']))
        q=generate_question('wb6131:defining-sets-all-forms',seed)
        divisors.add(re.search(r'multiples of (\d+)',q['parts'][0]['prompt'])[1]);parities.add(q['parts'][2]['reference_answer'].split()[1])
        assert 'a enlargement' not in generate_question('wb6131:combined-transformations',seed)['stem']
        q=generate_question('wb6131:legacy:nssco_transformations_coordinates:3',seed)
        assert 'x-(0)' not in str(q['parts']) and 'E=' not in str(q['parts'])
        q=generate_question('wb6131:graphical-linear-solution',seed)
        target=float(re.search(r'=(\-?[\d.]+)\$',q['parts'][0]['prompt'])[1])
        diagram=q['assets'][0]['question_diagram'];lo,hi=diagram['coordinate_bounds'][2:]
        assert lo<=target<=hi and any(c['kind']=='text' and c['value']==f'{target:g}' for c in diagram['commands'])
        counts['low_issue_seed_sets']+=1
        q=generate_question('wb6131:standard-form-four-operations',seed)
        coefficient=re.search(r'Write ([\d.]+) in standard form',q['parts'][4]['prompt'])[1]
        assert Decimal(1)<=Decimal(coefficient)<10 and q['parts'][4]['reference_answer']==coefficient+r'\times10^0'
        q=generate_question('wb6131:check-calculator-answer',seed)
        sacks=int(re.search(r'contains (\d+) sacks',q['parts'][3]['prompt'])[1])
        rounded=int(Decimal(sacks).quantize(Decimal('1E1'),rounding='ROUND_HALF_UP'))
        mass=Decimal(re.search(r'each with mass ([\d.]+) kg',q['parts'][3]['prompt'])[1])
        rounded_mass=int(mass.quantize(Decimal('1'),rounding='ROUND_HALF_UP'))
        assert q['parts'][3]['reference_answer']==f'About {rounded*rounded_mass} kg.'
        q=generate_question('wb6131:similarity-problems',seed)
        a=int(re.search(r'PQ=(\d+)',q['stem'])[1]);scaled=int(re.search(r'XY=(\d+)',q['stem'])[1])
        assert q['parts'][2]['reference_answer']==f'{(scaled//a)**2}:1'
        q=generate_question('wb6131:geometric-nth-term-and-sum',seed)
        a,r=map(int,re.search(r'first term (\d+) and common ratio (\d+)',q['stem']).groups())
        assert q['parts'][2]['reference_answer']==rf'T_n={a}\times{r}^{{n-1}}'
        q=generate_question('wb6131:three-by-three-matrix-arithmetic',seed);p=q['parameter_evidence']
        def read_matrix(value):
            inside=re.search(r'\\begin\{pmatrix\}(.*?)\\end\{pmatrix\}',value)[1]
            return [[int(v) for v in row.split('&')] for row in inside.split('\\\\')]
        from sympy import Matrix
        R=Matrix([p['row_vector']]);C=Matrix(p['column_vector'])
        assert Matrix(read_matrix(q['parts'][2]['reference_answer']))==R*C
        assert Matrix(read_matrix(q['parts'][3]['reference_answer']))==C*R
        q=generate_question('wb6131:speed-time-rates',seed);p=q['parameter_evidence']
        from sympy import symbols,integrate,Rational
        t=symbols('t');u=p['initial_speed'];v=p['peak_speed'];t1=p['first_time'];t2=p['braking_time']
        area=integrate(u+Rational(v-u,t1)*t,(t,0,t1))+integrate(v-Rational(v,t2)*t,(t,0,t2))
        assert area==Rational(*p['distance']) and Rational(v,t2)==Rational(*p['deceleration'])
        q=generate_question('wb6131:line-equation-from-graph',seed);p=q['parameter_evidence']
        graph=q['assets'][0]['question_diagram'];drawn=graph['commands'][-1]
        xmin,xmax,ymin,ymax=graph['coordinate_bounds'];sx=(graph['width_mm']-24)/(xmax-xmin);sy=(graph['height_mm']-24)/(ymax-ymin)
        a,b=drawn['a'],drawn['b'];slope=(b[1]-a[1])/(b[0]-a[0])*sx/sy
        x=(a[0]-12)/sx+xmin;y=(a[1]-12)/sy+ymin
        assert math.isclose(slope,p['gradient']) and math.isclose(y-slope*x,p['intercept'],abs_tol=1e-10)
        counts['clause_gap_seed_sets']+=1
    assert states=={'all_domain','none'} and len(divisors)>1 and parities=={'odd','even'}
    for source in ['The interior angle sum of a pentagon is (5−2) × 180°.', 'A valid setup gives x=4.', 'x≈2.00 (allow ±0.2 per reading).','x+y≤8; these inequalities describe R.']:
        content=validate_content(display_content(source))
        assert not any(b['kind']=='math' and b['value'] in ('a','A','R.','(') for b in content['blocks'])
    for source,expected in [(r'k log x',r'\log'),('cos C',r'\cos')]:
        assert expected in str(display_content(source)['blocks'][0]['value'])
    try:validate_content({'format':'text_math_blocks_v1','blocks':[{'kind':'math','value':'('}]})
    except AssertionError:pass
    else:raise AssertionError('Punctuation-only maths accepted')
    q=generate_question('wb6131:household-finance',0);q['parts'][0]['prompt']='Compute 13333333333333333.'
    try:validate_question(q)
    except AssertionError as e:assert 'digit' in str(e)
    else:raise AssertionError('Float artefact accepted')
    return dict(counts)


if __name__=='__main__':
    result=check()
    print(json.dumps({'checks':'passed','seed_count':64,**result},indent=2))
