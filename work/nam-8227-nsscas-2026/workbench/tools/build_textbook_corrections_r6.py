"""Narrow R6 source corrections confirmed on native rendered pages."""
import math,json
from analysis_sources import A,WB,ROOT,digest,write

# These are authored readings,not inferred defects from a heading or a renderer.
READINGS=[
 ('Goldie:C6:Worked-illustration:7',170,'ITERATE-LABELS',
  'Figure6.10swaps the x1 and x2 abscissa labels.',
  'x1=0.5 is the initial point; x2=(1-0.5 exp(0.5))/0.5 is approximately0.3513,so the label at0.5 is x1 and the label near0.35 is x2.',
  'Evaluate the original supplied map at the stated start. The third iterate is approximately1.43;changing labels does not change the recurrence.',
  ['Goldie:C6:Teaching-figure:16']),
 ('YM:C4:Teaching-figure:83',186,'COSINE-QUADRANT',
  'The cosine graph labels the90degree–180degree quadrant as Quadrant3.',
  'That interval is Quadrant2;180degree–270degree is Quadrant3.',
  'The terminal angle definition fixes the quadrants;cosine is negative in bothIIandIII,but that does not make their labels interchangeable.',[]),
 ('YM:C7:Teaching-figure:60',350,'NEGATIVE-INFINITY-SIGNS',
  'The x<0 rows of the multiplication/division infinity table contain incorrect signs.',
  'For a fixed finite negative c:c times positive-infinity tends to negative-infinity;c times negative-infinity tends to positive-infinity;positive-infinity/c tends to negative-infinity;negative-infinity/c tends to positive-infinity.',
  'Use a fixed negative multiplier/divisor and a real variable tending to each directed infinity. This is limiting shorthand,not arithmetic on an infinite real number.',[]),
 ('YM:C11:Teaching-figure:36',495,'LOG-SQUARE-DOMAIN',
  'The worked expansion ln(x squared)=2ln(x) omits the x>0condition.',
  'For real x!=0,use ln(x squared)=2ln(abs(x));the original ln(3x squared) has both positive and negative components. Its derivative2/x remains correct.',
  'At x=-1,the original logarithm is defined but ln(x) is not real. On either nonzero component the absolute-log derivative is2/x.',[]),
 ('YM:C10:Teaching-figure:105',474,'R-EXTREMUM-PHASE',
  'The summary uses cos(theta+alpha)=plus/minus1as an interchangeable condition for the same sine-phase R-form.',
  'For a sin(theta)+b cos(theta)=R sin(theta+alpha),extrema require sin(theta+alpha)=plus/minus1. A cosine alternative needs its own coefficient-matched phase,not the same alpha.',
  'Counterexample:a=b=1,alpha=45degrees. The maximum is at theta45degrees,where sin(theta+alpha)=1 but cos(theta+alpha)=0.',[]),
 ('YM:C13:Teaching-figure:54',574,'STAIRCASE-GRADIENT-RULE',
  'The margin note says both graph gradients can be negative for the staircase comparison against y=x.',
  'The reference y=x has gradient+1,so both gradients cannot be negative. A positive local map slope can give a staircase pattern;a negative map slope can give alternating/cobweb behaviour. Sign alone is not a convergence test.',
  'Differentiate the actual reference line and distinguish pattern direction from convergence magnitude. Formal convergence conditions remain outside the required8227scope.',[]),
 ('YM:C12:Teaching-figure:121',555,'CONCAVITY-WORD',
  'The solution calls the upward-bending cosecant curve concave without the qualifying upward direction.',
  'On pi/4..pi/2,cosec(x) is convex/concave-up and the chord tops lie above it;the trapezium overestimate conclusion is correct.',
  'Its second derivative is cosec(x)cot(x)^2+cosec(x)^3>0 on that interval. A source terminology error is separate from its correct bias conclusion.',[]),
 ('YM:C9:Teaching-figure:58',429,'DUPLICATE-LOG-LEGEND',
  'The lower four-logarithm plot repeats the legend name g(x);the fourth displayed rule is the intended u(x).',
  'Use distinct source names:f=log base(1/2),g=log base(1/10),h=log base(1/1.2),u=log base(1/e)=-ln(x).',
  'Read the preceding task labels and each displayed denominator. The fourth curve does not share the second curve rule merely because its legend repeats g.',[]),
 ('YM:C9:Teaching-figure:122',447,'INCREASING-BASE-HEADER',
  'The increasing exponential summary header says a>0.',
  'The increasing case requires a>1. For0<a<1,the exponential is decreasing;for a=1,it is constant.',
  'All displayed increasing examples10,e,2,1.2exceed1;the general header must match those actual cases.',[]),
 ('YM:C2:Example:7',57,'AP-WORKING-SIGN',
  'Part(b)prints13-2(-3)in its final substitution line while reporting the correct terms13,10,7.',
  'With a=13,d=-3,the third term is13+2(-3)=7. Correct the working sign;the printed final terms remain correct.',
  'T8=13+7(-3)=-8andT16=13+15(-3)=-32;the original givens and final terms reconcile.',[]),
 ('YM:C2:Example:25',74,'SIGMA-BRACKETS',
  'The source prints Sigma3n+2without grouping the whole intended summand.',
  'Write sum from n1to4of(3n+2)=5+8+11+14=38. The alternative(sum3n)+2would equal32,so the scope must be explicit.',
  'Expand both possible readings independently. The source expanded series and final38show its intended grouped summand.',[]),
]

def build():
    items={i['item_id']:i for i in json.loads((A/'textbook-inventory.json').read_text())['items']}
    rows=[]
    for short,page,slug,issue,correct,working,related in READINGS:
        iid='8227:TB:'+short;item=items[iid];book='Goldie'if':Goldie:'in iid else'YM'
        evidence=WB/f'checks/r6/source/{book}-{page}.png';assert evidence.is_file()
        rows.append(dict(defect_id='TB-R6-'+slug,item_id=iid,subpart='figure/working',
            also_affects_item_ids=['8227:TB:'+s for s in related],source_path=item['source_path'],source_sha256=item['source_sha256'],
            source_pdf_page=page,source_printed_page=item['printed_page'],answer_pdf_page=None,answer_printed_page=None,
            kind='printed figure/working/notation error; final answer is a separate check',issue=issue,correct_answer=correct,working=working,
            evidence=[dict(path=str(evidence.relative_to(ROOT)),sha256=digest(evidence),render_scale=4)],
            date='2026-11-21',reviewer='Codex author; visually checked on the native source render in R6; independent repair check pending',
            disposition='Internal source evidence with explicit correction;do not reuse the defective label,sign,condition or wording.',learner_display=False))
    # Independent elementary checks for the two corrected workings and the phase
    # counterexample. These are not inputs to the original answer construction.
    assert [13+k*(-3)for k in range(3)]==[13,10,7]
    assert sum(3*n+2 for n in range(1,5))==38 and sum(3*n for n in range(1,5))+2==32
    assert abs(math.sin(math.pi/4)+math.cos(math.pi/4)-math.sqrt(2))<1e-12
    assert abs(math.cos(math.pi/4+math.pi/4))<1e-12
    write(A/'textbook-corrections-r6.json',dict(status='eleven narrow author corrections checked against rendered source;independent repair acceptance pending',entries=rows))
    write(WB/'checks/r6/source-readings.json',dict(scope='Nine named figure corrections,two printed slips,two named answer-page offsets and worked-solution roles;no full figure-content audit',
        checked_by='Codex author',date='2026-11-21',source_pages=[dict(path=str(p.relative_to(ROOT)),sha256=digest(p))for p in sorted((WB/'checks/r6/source').glob('*.png'))if not p.name.startswith('contact-')and p.name not in['two-slips.png','YM-64.png','YM-77.png']],
        not_a_pair_reading_record=True))
    print(len(rows),'narrow corrections;original final-answer statuses unchanged')
if __name__=='__main__':build()
