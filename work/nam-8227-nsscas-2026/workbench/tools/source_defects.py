"""Recompute source findings independently; never change original documents."""
import math
import sympy as sp
from analysis_sources import A, ROOT, WB, digest, write


def recomputations():
    iterations=[];t=.4
    for _ in range(6):t=.25*math.exp(t/2);iterations.append(t)
    def bisect_root(f,a,b):
        # Independent bracketed bisection; no generator answer function.
        assert f(a)*f(b)<0
        for _ in range(90):
            m=(a+b)/2
            if f(a)*f(m)<=0:b=m
            else:a=m
        return (a+b)/2
    tP=bisect_root(lambda t:4*t*t*math.exp(-t)-.25,.1,.7)
    xP=3*tP-6*math.exp(-2*tP)
    tIntercept=bisect_root(lambda t:3*t-6*math.exp(-2*t),.1,1)
    yIntercept=4*tIntercept*tIntercept*math.exp(-tIntercept)
    assert xP<0 and .25<yIntercept
    p,x=sp.symbols('p x',real=True)
    polynomial=(p-2)*x**2+(3*p+1)*x+2*p+3
    discriminant=sp.factor(sp.discriminant(polynomial,x))
    assert discriminant==(p+5)**2
    assert sp.solve(polynomial.subs(p,2),x)==[-1]
    g=lambda a, degrees=False:(3-2*math.cos(2*a*(math.pi/180 if degrees else 1))-math.sin(a*(math.pi/180 if degrees else 1)))**(1/3)
    radians=[];degrees=[]
    for mode,values in [(False,radians),(True,degrees)]:
        value=1.45
        for _ in range(8):value=g(value,mode);values.append(value)
    F=lambda a:a**3+2*math.cos(2*a)+math.sin(a)-2
    f=lambda t:t*math.exp(-t)
    T=.5*(f(0)+2*f(1)+f(2));exact=1-3*math.exp(-2)
    assert T<exact and abs(F(radians[-1])-1)<1e-9 and F(degrees[-1])<0
    A0=sp.Matrix([3,3,6]);B=sp.Matrix([1,5,2]);AP=sp.Rational(3,2)*(B-A0);P=A0+AP
    assert list(P)==[0,6,0] and AP.dot(B)==0
    m=sp.symbols('m',real=True)
    roots=sp.solve(3*(m-4)**2/(5-m)-1,m)
    return {
      '2024P2Q7':{'method':'Independent bracketed bisection solve of y(t)=1/4 and x(t)=0; full-precision fixed-point iteration separately.', 't_at_P':tP,'x_at_P':xP,'y_intercept':yIntercept,'iterates':iterations,'iterates_4sf':[format(v,'.4g')for v in iterations]},
      '2021P2Q12_report':{'sqrt18':str(sp.sqrt(18)),'2sqrt3':float(2*sp.sqrt(3)),'phase_acos_one_third':math.acos(1/3)},
      '2022P1Q13':{'c_if_point_used':-12.0,'curve':'y=2x^2-6/x-12','point_x_in_stated_domain':False,
                   'oracle':'Symbolic integration and substitution; negative-x point cannot constrain positive-domain component.'},
      '2023P1Q9':{'2pi/3':2*math.pi/3,'pi/2':math.pi/2,'in_principal_range':False,
                  'non_principal_reading_x':[round(math.sqrt(2+math.sin(2*math.pi/3)),4),-round(math.sqrt(2+math.sin(2*math.pi/3)),4)],
                  'check_asin_of_that_value':math.asin(math.sin(2*math.pi/3))},
      '2023P1Q1b':{'discriminant':str(discriminant),'disc_at_p=2':49,'leading_coeff_at_p=2':0,'roots_at_p=2':[-1.0]},
      '2023P2Q7':{'radian_iterates':[round(v,6) for v in radians],'degree_iterates':[round(v,6) for v in degrees],
                  'F(radian_root)':round(F(radians[-1]),6),'F(degree_value_as_radians)':round(F(degrees[-1]),6),
                  'g(1.3)':round(1.3-g(1.3),5),'g(1.6)':round(1.6-g(1.6),5),
                  'interpretation':'F evaluated at converged unrounded iterate; reviewer F=0.999998 used rounded a=1.587275.'},
      'TB_p550_Q2':{'M':[1,round(1/math.e,5)],'trapezium_2_intervals':round(T,4),'exact':round(exact,4),
                     'f2_sign_on_[0,2)':"negative: f''=(x-2)e^-x",'verdict':'under-estimate'},
      '2021P1Q6':{'P':[float(v) for v in P],'AP.OB':float(AP.dot(B)),'P_beyond_B':True},
      '2023P1Q5c':{'m':[round(float(v),4) for v in sorted(roots,reverse=True)],'|r|<1':[True,True]},
      '2021P2Q4b':{'t':round(math.log(2)/.02,3)}
    }


def build_defects(questions):
    index={q['source_key']:q for q in questions}
    rows=[]
    def add(code,key,page,issue,decision,check,disposition='hold'):
        q=index[key]
        rows.append({'defect_id':code,'source_path':q['question_source_path'],'source_sha256':q['source_sha256'],
                     'question_key':key,'pdf_page':page,'issue':issue,'disposition':disposition,
                     'authoring_constraint':decision,'recomputation_id':check,
                     'owner':'Vitalis','decision_date':'2026-11-16','independent_repair_acceptance':'pending'})
    add('SRC-8227-DOMAIN-2022-P1-Q13','2022-1-Q13',18,'Domain x>0 conflicts with supplied point P(-2,-1).',
        'Hold exact exemplar. A future original curve-recovery problem must provide a point in its connected domain.','2022P1Q13')
    add('SRC-8227-PRINCIPAL-2023-P1-Q9','2023-1-Q9',16,'Inverse sine cannot have principal value 2pi/3.',
        'Hold defective exemplar; retain standard principal ranges from syllabus and separately labelled Cambridge evidence.','2023P1Q9')
    add('SRC-8227-DEGENERATE-2023-P1-Q1B','2023-1-Q1',3,'At p=2 the equation is linear, contradicting distinct real roots for all p except -5.',
        'Hold part (b) exemplar. Discriminant proofs must state a!=0 in ax^2+bx+c=0.','2023P1Q1b')
    add('SRC-8227-POLYNOMIAL-NAME-2024-P2-Q5','2024-2-Q5',6,'Source defines f(x) then asks to divide p(x).',
        'Retain structure with disclosed typo; future original problems use one consistent polynomial name.',None,'include-with-source-note')
    add('SRC-8227-EXTERNAL-DIVISION-2021-P1-Q6','2021-1-Q6',7,'Old summary said segment; AP=(3/2)AB places P beyond B.',
        'External division is an explicit geometric branch, not an internal-only segment problem.','2021P1Q6','include-corrected-analysis')
    next(r for r in rows if r['defect_id']=='SRC-8227-POLYNOMIAL-NAME-2024-P2-Q5')['provenance_match_ids']=['8227:PROVENANCE:002']
    add('SRC-8227-DIAGRAM-2024-P2-Q7','2024-2-Q7',10,
        'Diagram retains P to the right of the y-axis and above its intercept despite changing y(P) from1 to1/4.',
        'Use x(P)≈-2.50 and y-intercept≈0.79 from the stated equations; future original diagrams must move P left of the y-axis and below that intercept.','2024P2Q7','include-with-source-note')
    rows[-1]['provenance_match_ids']=['8227:PROVENANCE:012']
    rows[-1]['rendered_evidence']='work/nam-8227-nsscas-2026/workbench/checks/r5/provenance-012.png'
    q=index['2023-2-Q7']
    rows.append({'defect_id':'SRC-8227-RADIAN-AWARD-2023-P2-Q7C','source_path':q['report_source'],
      'source_sha256':digest(ROOT/q['report_source']),'pdf_page':338,'question_key':'2023-2-Q7:c',
      'issue':'Award table OR degree-mode answer 0.995 does not solve the stated radian integral or lie in its bracket.',
      'disposition':'reject-degree-mode-alternative; include radian branch',
      'authoring_constraint':'Require radians. No marking credit for the listed degree-mode alternative.',
      'owner':'Vitalis','decision_date':'2026-11-16','recomputation_id':'2023P2Q7','independent_repair_acceptance':'pending'})
    book='Y=mc as textbook.pdf'
    for code,page,issue,decision in [
      ('SRC-8227-TEXTBOOK-REF',550,'Try Now 21 Q2(c): interval in part (a) should refer to integral in part (b).',
       'Resolved reading: integral from 0 to 2 of x*e^-x; trapezium estimate is below the exact integral.'),
      ('SRC-8227-TEXTBOOK-CURVATURE',550,'REMEMBER box names cup shape concave and cap shape convex, conflicting with standard terminology.',
       'Use unambiguous chords/trapezium tops above or below curve in guidance; reports 2023 PDF 335 and 2025 PDF 358 caution against these words.'),
      ('SRC-8227-TEXTBOOK-TABLE-GRAPHS',560,'Example 1 recommends tables to sketch graphs; official reports advise standard graph shapes.',
       'Teach standard transformed graph shapes; do not recommend tables as graph-construction method (2023 PDF 335, 2021 PDF 236, 2024 PDF 338).')]:
        rows.append({'defect_id':code,'source_path':book,'source_sha256':digest(ROOT/book),'pdf_page':page,
                     'printed_page':page-12,'issue':issue,'disposition':'include-with-recorded-correction/convention-conflict',
                     'authoring_constraint':decision,'recomputation_id':'TB_p550_Q2' if page==550 else None,
                     'review_status':'author repair; independent re-review pending'})
    rows.append({'defect_id':'SRC-8227-SYLLABUS-MODULUS-EQUALS','source_path':'Syllabi/Namibian Curricula/NSSCAS/8227_NSSCAS_Mathematics_final_updated_20_November_2020.pdf',
                 'pdf_pages':[14,20,22],'issue':'Source prints an extra equals sign in |a|=|b| iff a^2=b^2.',
                 'disposition':'include normalized statement with explicit typographical note; preserve source bytes'})
    from analysis_sources import evidence_path
    import json
    for r in json.loads((WB/'tools/report_defects_r5_inputs.json').read_text())['entries']:
        ev=r['evidence'];assert ev['render_scale']>=4 and ev['inspection'].startswith('Codex author re-read')
        assert digest(evidence_path(ev['path']))==ev['sha256']
        rows.append(r)
    if (A/'textbook-defects-r5.json').exists():
        rows.extend(json.loads((A/'textbook-defects-r5.json').read_text())['entries'])
    if (A/'textbook-corrections-r6.json').exists():
        rows.extend(json.loads((A/'textbook-corrections-r6.json').read_text())['entries'])
    write(A/'source-defects.json',{'entries':rows,'recomputations':recomputations(),
                                  'scope':'Source-analysis findings, not learner recipe solutions or app marking implementation.'})
    return rows
