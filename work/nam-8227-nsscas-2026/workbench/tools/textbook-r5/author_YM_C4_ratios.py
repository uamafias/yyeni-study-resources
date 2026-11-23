"""Author source readings: YM PDF189–192, all tasks and mathematical figures."""
import hashlib,json
from pathlib import Path
from author_YM_C4_trig_graphs import value
W=Path(__file__).resolve().parents[2];ROOT=W.parents[2]
SRC='Y=mc as textbook.pdf';SHA='0b44ad3b67b1ea3de90cba780382d77deef347fae683cf6e28677f36c17a724f'
PROP='8227:2020:M2:T3:O01:D02';REC='8227:2020:M2:T3:O01:D01';EXACT='8227:2020:M1:T6:O03:D01'
def ev(page):
    name='YM-key-607-Try25-28'if page==607 else'YM-C4-189'
    p=W/f'checks/r5/textbooks/{name}.png'
    return {'path':str(p.relative_to(ROOT)),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
answers=[]
def add(kind,n,page,note,parts,direct):
    for p in parts:
        kp=p.pop('key_page_override',page)
        p.update(source_pdf_page=page,source_evidence=ev(page),answer_pdf_page=kp,
          answer_printed_page='A'+str(kp-586)if kp>=602 else kp-12,key_evidence=ev(kp))
    row={'item_id':f'8227:TB:YM:C4:{kind}:{n}','source_pdf_page':page,'notes':note,
      'assessed_8227_demand_ids':direct,'component_demand_ids':[],
      'mapping_rationale':'Classify the requested ratio, reciprocal relationship or same-function related-angle form. Arbitrary-angle ratios do not establish exact special-angle evaluation. Using Pythagoras or a quotient identity in the author recomputation does not turn a numerical ratio task into an identity proof or bounded-angle solution question.',
      'value_level_scope_decisions':[{'rule_id':'8227:LIMIT02','status':'not applicable','quoted_value':note,
        'reason':'The requested outputs are ratios or reference-angle expressions, not general forms of trigonometric equation solutions. Any actual source quadrant/reflex interval still restricts the allowed ratio branches.'}],
      'exam_style':False,'exam_style_basis':'Ordinary worked Example/TryNow; no examination attribution or exam-style label.',
      'precision_angle_check':{'source':'Exact values and symbolic roots are retained without a calculator. Negative angles preserve the stated degree/radian units and required same-function basic-angle form.',
        'comparison':'Exact source tasks do not become decimal approximation tasks. A positive square root is selected only where the original acute angle or quadrant warrants it. Unrestricted examples retain all compatible branches.'},
      'expected_subpart_labels':[p['subpart']for p in parts],'subparts':parts}
    if PROP in direct:row['direct_demand_aspects']={PROP:'Ratio signs and related-angle properties are a partial aspect of this broad six-function/graph demand; these tasks do not assess graph construction.'}
    answers.append(row);return row
def numeric(label,family,given,target,key,kp,signs=None,interval=None):
    p=value(label,'0',key,kp,'Derive both possible unit-circle coordinate branches from the original given ratio and sin²θ+cos²θ=1. Apply only the printed sign/angle restrictions; evaluate the requested expression on every surviving branch. The printed key is not used to choose a quadrant.')
    p['operation']={'kind':'numeric-given-trig-ratio','given_family':family,'operands':[given,target]}
    if signs:p['operation']['sign_constraints']=signs
    if interval:p['operation']['angle_interval']=interval
    return p
def acute(label,family,given,target,key,kp,source_angle):
    p=value(label,'0',key,kp,'The original angle is acute, so both sine and cosine are positive. Independently derive its complementary positive square root, expand the requested related-angle function, and substitute the original given ratio. Preserve the symbolic denominator and its 0<value<1 condition.')
    p['operation']={'kind':'acute-given-trig-ratio','given_family':family,'angle_condition':'acute',
      'given_value_condition':'0 < value < 1','original_source_angle':source_angle,'operands':[target,given]}
    return p
negative_tan=[{'function':'tan','sign':-1}]
add('Example',25,189,'Given cosθ=−5/13 and tanθ<0, recover sinθ and tanθ exactly; the signs determine quadrant II.',
 [numeric('sin-theta','cos','-5/13','sin(x)','FiniteSet(12/13)',189,negative_tan),
  numeric('tan-theta','cos','-5/13','tan(x)','FiniteSet(-12/5)',189,negative_tan)],[PROP])
add('Try-Now-25',1,189,'Given sinθ=−3/5 and tanθ<0, recover cosine and tangent; quadrant IV is required.',
 [numeric('cos-theta','sin','-3/5','cos(x)','FiniteSet(4/5)',607,negative_tan),
  numeric('tan-theta','sin','-3/5','tan(x)','FiniteSet(-3/4)',607,negative_tan)],[PROP])
add('Try-Now-25',2,189,'Given cosθ=√3/2 and θ a reflex angle (π<θ<2π), find sinθ exactly; the related special-angle sine is negative.',
 [numeric('sin-theta','cos','sqrt(3)/2','sin(x)','FiniteSet(-1/2)',607,interval=['pi','2*pi'])],[EXACT])
add('Try-Now-25',3,189,'Given tanθ=2/3 with π<θ<2π, recover sine and cosine; both are negative in quadrant III.',
 [numeric('sin-theta','tan','2/3','sin(x)','FiniteSet(-2/sqrt(13))',607,interval=['pi','2*pi']),
  numeric('cos-theta','tan','2/3','cos(x)','FiniteSet(-3/sqrt(13))',607,interval=['pi','2*pi'])],[PROP])
add('Example',26,189,'Given sin35°=k, express cos35°,tan215° and sin55° in terms of k. The actual acute 35° implies 0<k<1 and fixes the positive complementary root.',
 [acute('a','sin','k','cos(x)','sqrt(1-k**2)',189,'35 degrees'),
  acute('b','sin','k','tan(pi+x)','k/sqrt(1-k**2)',189,'35 degrees'),
  acute('c','sin','k','sin(pi/2-x)','sqrt(1-k**2)',189,'35 degrees')],[PROP])
add('Try-Now-26',1,190,'Given cos50°=a (0<a<1), express sin50°,sin230°,tan310°,cos310°,tan40° and cos40° in terms of a.',
 [acute(label,'cos','a',target,key,607,'50 degrees')for label,target,key in[
  ('a','sin(x)','sqrt(1-a**2)'),('b','sin(pi+x)','-sqrt(1-a**2)'),
  ('c','tan(2*pi-x)','-sqrt(1-a**2)/a'),('d','cos(2*pi-x)','a'),
  ('e','tan(pi/2-x)','a/sqrt(1-a**2)'),('f','cos(pi/2-x)','sqrt(1-a**2)')]],[PROP])
add('Try-Now-26',2,190,'Given cosx=p for an acute angle x in degrees (0<p<1), derive sinx,tanx and tan(90°−x), retaining the positive complementary root.',
 [acute(label,'cos','p',target,key,607,'acute x in degrees')for label,target,key in[
  ('a','sin(x)','sqrt(1-p**2)'),('b','tan(x)','sqrt(1-p**2)/p'),('c','tan(pi/2-x)','p/sqrt(1-p**2)')]],[PROP])

def reductions(specs,kp):
    parts=[]
    for label,theta,unit,beta,signs in specs:
        for fn,sign in zip(['sin','cos','tan'],signs):
            p=value(label+'-'+fn,'0',f'Tuple({sign},{beta})',kp,'Reduce the original signed angle modulo one full turn, derive its acute reference angle and each function sign, then retain the same function. An evaluated number alone is not the requested basic-angle form.')
            p['operation']={'kind':'same-function-reduction','family':fn,'angle_unit':unit,'operands':[theta]}
            p['response_form_check']={'required_family':fn,'printed_family':fn,'acute_angle_unit':unit,
              'printed_form':f'{"-"if sign==-1 else""}{fn}({beta} {unit})'}
            parts.append(p)
    return parts
add('Example',27,190,'Express sine,cosine,tangent via the basic angle for −70°,−120°,−4π/3 and −7π/4. This asks related-angle expressions, not exact numerical special values.',
 reductions([('a','-70','degree','70',[-1,1,-1]),('b','-120','degree','60',[-1,-1,1]),
  ('c','-4*pi/3','radian','pi/3',[1,-1,-1]),('d','-7*pi/4','radian','pi/4',[1,1,1])],190),[PROP])
add('Try-Now',27,190,'Express sine,cosine,tangent via basic angles for −30°,−170°,−5π/4 and −5π/3, preserving each original function and quadrant sign.',
 reductions([('a','-30','degree','30',[-1,1,-1]),('b','-170','degree','10',[-1,-1,1]),
  ('c','-5*pi/4','radian','pi/4',[1,-1,-1]),('d','-5*pi/3','radian','pi/3',[1,1,1])],607),[PROP])

FUNCTIONS=['sin','cos','tan','csc','sec','cot']
def coordinate(label,px,py,key,kp):
    p=value(label,'0',key,kp,'Independently compute the positive radius √(x²+y²) from the original nonzero point; derive all six ratios using signed coordinates and reciprocal definitions. Compare the ordered sine,cosine,tangent,cosecant,secant,cotangent vector, not an unsigned triangle.')
    p['operation']={'kind':'coordinate-trig-ratios','operands':[px,py],'return_functions':FUNCTIONS}
    p['answer_component_order']=FUNCTIONS;return p
add('Example',28,191,'For P(−7,24), determine all six ratios of ∠POQ without a calculator; r=25 is positive, with sine/cosecant positive and the remaining four negative.',
 [coordinate('six-ratios','-7','24','Tuple(24/25,-7/25,-24/7,25/24,-25/7,-7/24)',191)],[REC,PROP])
add('Try-Now',28,192,'Determine all six ratios from points (4,3),(−21,20),(−35,−12),(1,−√3), in 0≤θ≤360°. All points are nonzero and neither coordinate vanishes; the radii 5,29,37,2 are positive, while the coordinates retain their signs.',
 [coordinate('a','4','3','Tuple(3/5,4/5,3/4,5/3,5/4,4/3)',607),
  coordinate('b','-21','20','Tuple(20/29,-21/29,-20/21,29/20,-29/21,-21/20)',607),
  coordinate('c','-35','-12','Tuple(-12/37,-35/37,12/35,-37/12,-37/35,35/12)',607),
  coordinate('d','1','-sqrt(3)','Tuple(-sqrt(3)/2,1/2,-sqrt(3),-2/sqrt(3),2,-1/sqrt(3))',607)],[REC,PROP])
row=add('Example',29,192,'Given √7 cosecθ+4=0, find tanθ,1/cotθ,sinθ/cosθ and sin²θ+cos²θ. No quadrant restriction is given: both III and IV survive, and the worked source explicitly retains both.',
 [numeric('a','csc','-4/sqrt(7)','tan(x)','FiniteSet(-sqrt(7)/3,sqrt(7)/3)',192),
  numeric('b','csc','-4/sqrt(7)','1/cot(x)','FiniteSet(-sqrt(7)/3,sqrt(7)/3)',192),
  numeric('c','csc','-4/sqrt(7)','sin(x)/cos(x)','FiniteSet(-sqrt(7)/3,sqrt(7)/3)',192),
  numeric('d','csc','-4/sqrt(7)','sin(x)**2+cos(x)**2','FiniteSet(1)',192)],[REC,PROP])
row['correlated_branch_check']={'source':'The source gives separate quadrant III and quadrant IV columns, not independent arbitrary sign choices.',
 'branches':[{'quadrant':3,'sin':'-sqrt(7)/4','cos':'-3/4','a_b_c':'sqrt(7)/3','d':'1'},
             {'quadrant':4,'sin':'-sqrt(7)/4','cos':'3/4','a_b_c':'-sqrt(7)/3','d':'1'}],
 'reason':'Each of parts a,b,c must use the same sign when answering on one chosen ray. The two printed columns agree with the independently derived unit-circle branches.'}
row['subparts'][0]['additional_operations']={'coupled_sine_cosine_branches':{
 'kind':'numeric-given-trig-ratio','given_family':'csc','operands':['-4/sqrt(7)','Tuple(sin(x),cos(x))']}}

figures=[]
specs=[
 (189,'Example25 sign-selection CAST','Cosine negative and tangent negative intersect only in quadrant II.','Example:25',None,[PROP],'diagram'),
 (189,'Example25 signed coordinate triangle','Point(−5,12),positive radius13,and quadrant II ray give sine12/13 and tangent−12/5.','Example:25',None,[PROP],'diagram'),
 (189,'Example26a acute unit triangle','For 35°,opposite k,hypotenuse1 and positive adjacent√(1−k²),with0<k<1.','Example:26','a',[PROP],'diagram'),
 (189,'Example26b quadrant III unit triangle','At215°,both coordinates are negative; tan215=k/√(1−k²).','Example:26','b',[PROP],'diagram'),
 (189,'Example26c complementary unit triangle','At55°,opposite√(1−k²) and adjacent k exchange the35° triangle legs.','Example:26','c',[PROP],'diagram'),
 (190,'Negative-angle reflected-ray diagram','Positive acute θ and clockwise−θ reflect across the x-axis; the negative ray has the same terminal position as360°−θ.',None,None,[PROP],'diagram'),
 (190,'Negative-angle identities','sin(−θ)=−sinθ,cos(−θ)=cosθ,tan(−θ)=−tanθ on their common defined domains.',None,None,[PROP],'table'),
 (190,'Example27a negative ray','Clockwise−70° lies in quadrant IV with reference70°.','Example:27','a',[PROP],'diagram'),
 (190,'Example27b negative ray','Clockwise−120° lies in quadrant III with reference60°.','Example:27','b',[PROP],'diagram'),
 (190,'Example27c negative ray','Clockwise−4π/3 lies in quadrant II with referenceπ/3.','Example:27','c',[PROP],'diagram'),
 (190,'Example27d negative ray','Clockwise−7π/4 lies in quadrant I with referenceπ/4.','Example:27','d',[PROP],'diagram'),
 (191,'Reciprocal definitions and sign diagram','cosec=r/y,sec=r/x,cot=x/y; the coordinate ray and CAST signs extend to the reciprocal functions. sec is undefined atx=0;cot/cosec at y=0. The reciprocal-of-tangent expression is read on its common domain; cot itself is defined ascos/sin when tangent has a pole.',None,None,[REC,PROP],'table'),
 (191,'Six-ratio reciprocal-pair chart','sin=y/r,cos=x/r,tan=y/x,cot=x/y,sec=r/x,cosec=r/y are paired reciprocals wherever both expressions exist.',None,None,[REC],'table'),
 (191,'Example28 quadrant II coordinate ray','P(−7,24),projection Q(−7,0),positive r25 and radius OP determine all six signed ratios.','Example:28',None,[REC,PROP],'diagram'),
 (192,'Example29 two admissible rays','Both rays have y=−√7,r4; x=−3 in quadrant III andx=3 in quadrant IV. The paired tangent signs remain correlated across parts a,b,c.','Example:29',None,[REC,PROP],'diagram')]
for n,(page,label,note,parent,part,teaches,rep)in enumerate(specs,93):
    figures.append({'item_id':f'8227:TB:YM:C4:Teaching-figure:{n}','item_kind':'teaching-figure','exercise':'Teaching figure','item_number':str(n),
      'pdf_page':page,'printed_page':page-12,'source_label':label,'parent_item_id':f'8227:TB:YM:C4:{parent}'if parent else None,'parent_subpart':part,
      'notes':note,'what_it_shows':note,'assessed_8227_demand_ids':[],'component_demand_ids':[],'teaches_8227_demand_ids':teaches,
      'representation':rep,'source_evidence':ev(page),'learner_display':False,
      'value_level_scope_decisions':[{'rule_id':'8227:LIMIT02','status':'not applicable','quoted_value':note,'reason':'A ratio/sign/reciprocal teaching figure, not a general solution formula.'}],
      'value_level_scope_review_status_r5':'author actual coordinates,ratio denominators and angle units read; independent check pending',
      'exam_representation_check':{'status':'final cross-book/examination representation comparison pending','examination_part_ids':[],
        'relation':'Source teaching/solution evidence; no examination frequency or full-demand coverage claim.'},
      'mathematical_feature_review':{'status':'author source features checked against exact ratio derivations; independent acceptance pending',
        'method':'Positive radius and signed coordinates determine the displayed ratio signs. Negative-angle identities were verified symbolically; all parent tasks are independently recomputed from source givens.'}})

pages=[]
for page in range(189,193):
    pages.append({'pdf_page':page,'printed_page':page-12,'chapter':4,'page_status':'items enumerated',
      'item_ids':[r['item_id']for r in answers if r['source_pdf_page']==page]+[r['item_id']for r in figures if r['pdf_page']==page],
      'continuation_item_ids':[],'source_evidence':ev(page),'non_item_content':'Every formal task and mathematical figure/table enumerated. Explanatory ratio/sign prose belongs to the corresponding teaching evidence.',
      'reader':'Codex author','date':'2026-11-17'})
if __name__=='__main__':
    import sympy as sp
    x=sp.Symbol('x',real=True)
    assert all(sp.trigsimp(fn(-x)-sgn*fn(x))==0 for fn,sgn in[(sp.sin,-1),(sp.cos,1),(sp.tan,-1)])
    for name,data in[
      ('answers-YM-C4-ratios.json',{'scope':'All12formal items PDF189–192; every requested ratio/function output; exact source branches retained.','items':answers}),
      ('census-YM-C4-ratios.json',{'book':'YM','book_id':'8227-SRC-017','chapter':4,'source_path':SRC,'source_sha256':SHA,
        'scope':'PDF189–192 inclusive; separate source solution diagrams and mathematical teaching tables enumerated.',
        'new_items':figures,'corrections':[],'pages':pages})]:
        (W/'tools/textbook-r5'/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
    print(len(answers),'items;',len(figures),'figures;',sum(len(r['subparts'])for r in answers),'outputs')
