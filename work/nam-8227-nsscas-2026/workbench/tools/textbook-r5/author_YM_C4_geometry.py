"""Fixed-source geometric trigonometry on YM PDF 221–222; not a recipe generator."""
import hashlib,json
from pathlib import Path
from author_YM_C4_trig_graphs import value,reasoning
W=Path(__file__).resolve().parents[2];ROOT=W.parents[2]
SRC='Y=mc as textbook.pdf';SHA='0b44ad3b67b1ea3de90cba780382d77deef347fae683cf6e28677f36c17a724f'
EXACT='8227:2020:M1:T6:O03:D01';PRINCIPAL='8227:2020:M1:T6:O04:D01'
PRIOR='8227:PRIOR:NSSCO:right-triangle-trig'
def ev(page):
    name='YM-key-Try56-lengths'if page==614 else'YM-C4-221'
    p=W/f'checks/r5/textbooks/{name}.png'
    return {'path':str(p.relative_to(ROOT)),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
answers=[]
def add(kind,n,page,note,parts):
    for p in parts:
        kp=p.pop('key_page_override',page if kind=='Example'else 614)
        p.update(source_pdf_page=page,source_evidence=ev(page),answer_pdf_page=kp,
          answer_printed_page='A28'if kp==614 else kp-12,key_evidence=ev(kp),review_date='2026-11-18')
    row={'item_id':f'8227:TB:YM:C4:{kind}:{n}','source_pdf_page':page,'notes':note,
      'assessed_8227_demand_ids':[EXACT],'component_demand_ids':[PRIOR,PRINCIPAL],
      'component_demand_roles':{PRIOR:'Prior right-triangle side ratios and Pythagoras implement the geometry; this supplementary prerequisite never counts as AS objective coverage.',
        PRINCIPAL:'The acute geometric angle is written using standard principal arctangent notation. The task does not separately ask the learner to classify inverse ranges or choose between inverse branches, so this is component support only.'},
      'direct_demand_aspects':{EXACT:'Exact 30°/60° ratios determine the requested lengths and exact angle-expression ingredients; retain positive length scale and surd answers.'},
      'mapping_rationale':'Exact special-angle geometry is assessed. The requested show-that inverse-angle expressions use elementary acute inverse notation as a component; they do not separately assess principal-range interpretation. Do not add bounded-periodic solving, identity proofs or general modelling merely because the author cross-check uses vectors.',
      'representation':'diagram','sketch_response_required':False,
      'value_level_scope_decisions':[{'rule_id':'8227:QUAL08','status':'within','quoted_value':note,
        'reason':'All lengths are positive. Each inverse tangent denotes the acute right-triangle angle fixed by the given diagram; no periodic alternative or negative length is admitted.'},
       {'rule_id':'8227:QUAL03','status':'not applicable','quoted_value':note,
        'reason':'Geometric angle expressions and exact lengths are requested; no bounded periodic equation with an input multiplier is asked.'}],
      'exam_style':False,'exam_style_basis':'Ordinary Example/Try Now; no examination attribution or exam-style label.',
      'precision_angle_check':{'source':'Example 56 uses degrees; Try 56 question 2 explicitly uses radians. Try 56 question 1 asks an unevaluated inverse expression, with 150° geometry.',
        'comparison':'Convert all angles before calculation. Do not subtract 30 degrees from a radian arctangent. Exact surd lengths are not rounded; p and x are strictly positive length scales.'},
      'expected_subpart_labels':[p['subpart']for p in parts],'subparts':parts}
    answers.append(row);return row
p=value('a:AC','cos(pi/6)*p','sqrt(3)*p/2',221,
 'In right triangle ADC, AD=p>0 and angle DAC=30°. Thus AC=p cos30°. The coordinate cross-check scales a unit triangle by positive p.')
p2=value('a:BC','2*sin(pi/6)*p','p',221,
 'DC=p sin30°=p/2, and D is the midpoint of BC. Hence BC=2DC=p.')
p3=value('a:AB','sqrt(cos(pi/6)**2+(2*sin(pi/6))**2)*p','sqrt(7)*p/2',221,
 'Pythagoras in ABC gives AB=p√[(cos30°)²+(2sin30°)²]. Pulling p outside the square root is justified by its positive length meaning, not an unrestricted real-symbol identity.')
p3['check_mode']='show/prove'
p4=reasoning('b','x = (180/π)atan(2/√3) − 30 degrees',
 'The whole acute angle BAC has tan(BAC)=BC/AC=2/√3. Since 30°<BAC<90°, the principal arctangent gives BAC, and x=BAC−30°. Independently use unit-p vectors AD=(√3/2,1/2) and AB=(√3/2,1): their normalized dot product is 5/(2√7). The stated acute angle difference has that same cosine, which uniquely determines x on (0°,90°).',221,'show/prove')
p4['additional_operations']={'angle_degrees':{'kind':'identity','operands':['180*(atan(2/sqrt(3))-pi/6)/pi']},
 'independent_vector_cosine':{'kind':'identity','operands':['(3/4+1/2)/(sqrt(3/4+1/4)*sqrt(3/4+1))']},
 'angle_cosine_residual':{'kind':'identity','operands':['cos(atan(2/sqrt(3))-pi/6)-5/(2*sqrt(7))']}}
add('Example',56,221,'ABC is right-angled at C; D is the midpoint of BC; AD=p>0, angle DAC=30° and BAD=x°. Find AC and BC exactly, show AB=√7 p/2, and show x=atan(2/√3)−30° with the inverse evaluated in degrees.',[p,p2,p3,p4])

p=value('a:BX','6*cos(pi-pi*150/180)','3*sqrt(3)',614,
 'A,B,X are collinear in that order, so angle CBX=180°−150°=30°. Its adjacent side BX=6cos30°=3√3 cm; CX=6sin30°=3 cm is an intermediate, not a separately asked answer.')
p2=reasoning('a:CAB','angle CAB = atan(3/(4+3√3))',
 'The diagram fixes AX=AB+BX=4+3√3 and CX=3, so tan(CAB)=3/(4+3√3). CAB is acute, and its principal arctangent is therefore the requested angle. Retain the unevaluated inverse expression; the source does not request a numerical angle/unit.',614,'show/prove')
p2['additional_operations']={'height':{'kind':'identity','operands':['6*sin(pi/6)']},
 'tangent_of_CAB':{'kind':'identity','operands':['6*sin(pi/6)/(4+6*cos(pi/6))']}}
p3=value('b','sqrt((4+6*cos(pi/6))**2+(6*sin(pi/6))**2)','sqrt(52+24*sqrt(3))',614,
 'Pythagoras in AXC gives AC²=(4+3√3)²+3²=52+24√3, and AC is the positive square root. As an independent route, the cosine rule in ABC with included angle 150° gives 4²+6²−2·4·6cos150°, the same squared length.')
p3['check_mode']='show/prove';p3['assertions']=[{'expression':'4**2+6**2-2*4*6*cos(5*pi/6)','expected':'52+24*sqrt(3)'}]
add('Try-Now-56',1,222,'In the diagram A,B,X are collinear with AB=4 cm, BC=6 cm, angle ABC=150° and CX perpendicular to ABX. Find exact BX, show the specified principal arctangent for CAB, and show AC=√(52+24√3) cm.',[p,p2,p3])

p=value('a','sqrt((2*tan(pi/3))**2+1)*x','sqrt(13)*x',614,
 'BM=MC=x>0 and angle ABC=π/3. First AC=2x tan(π/3)=2√3x. Then AM=x√[(2tan(π/3))²+1]=√13x. AC is an intermediate, not another requested output. The rendered key root bar covers 13 only, so it agrees.')
p2=reasoning('b','θ = π/6 − atan(1/(2√3)) radians',
 'Angle BAC=π/2−π/3=π/6. In right triangle ACM, angle MAC=atan(MC/AC)=atan(1/(2√3)), an acute principal value. Subtract MAC from BAC to get BAM=θ. Independent vectors from A to B and M have normalized dot product 7/(2√13), equal to the cosine of the stated positive acute difference.',614,'show/prove')
p2['additional_operations']={'angle_radians':{'kind':'identity','operands':['pi/6-atan(1/(2*sqrt(3)))']},
 'vector_cosine':{'kind':'identity','operands':['(2+12)/(sqrt(4+12)*sqrt(1+12))']},
 'angle_cosine_residual':{'kind':'identity','operands':['cos(pi/6-atan(1/(2*sqrt(3))))-7/(2*sqrt(13))']}}
add('Try-Now-56',2,222,'ABC is right-angled at C; M is the midpoint of BC, BM=MC=x>0, angle ABC=π/3 and BAM=θ radians. (a) Find AM in terms of x. (b) Show θ=π/6−atan(1/(2√3)).', [p,p2])

figures=[]
for n,page,label,note,parent,role in[
 (170,221,'Example 56 given triangle','ABC right at C, D midpoint of BC; AD=p>0, angle DAC=30°, BAD=x°. Tick marks enforce BD=DC.','Example:56','given-figure'),
 (171,221,'Example 56 special-angle solution triangle','The 30°/60° right triangle has sides 1,√3,2 and supports exact cos30°=√3/2. It is a solution aid, not an extra given.','Example:56','teaching-figure'),
 (172,222,'Try 56 question 1 given triangle','A,B,X are collinear in that order; AB=4 cm, BC=6 cm, angle ABC=150°, CX perpendicular to AX. The exterior 30° angle determines positive projections.','Try-Now-56:1','given-figure'),
 (173,222,'Try 56 question 2 given triangle','ABC right at C; M is the midpoint of BC, BM=MC=x>0, angle ABC=π/3 and BAM=θ radians. The marked midpoint must remain on segment BC.','Try-Now-56:2','given-figure')]:
    figures.append({'item_id':f'8227:TB:YM:C4:Teaching-figure:{n}','item_kind':role,'exercise':'Teaching figure','item_number':str(n),
      'pdf_page':page,'printed_page':page-12,'source_label':label,'parent_item_id':'8227:TB:YM:C4:'+parent,
      'notes':note,'what_it_shows':note,'assessed_8227_demand_ids':[],'component_demand_ids':[],
      'teaches_8227_demand_ids':[EXACT,PRINCIPAL],'representation':'diagram','source_evidence':ev(page),'learner_display':False,
      'value_level_scope_decisions':[{'rule_id':'8227:QUAL08','status':'within','quoted_value':note,
        'reason':'Positive right-triangle geometry fixes the acute inverse branch; no ambiguous periodic solution is introduced.'}],
      'value_level_scope_review_status_r5':'author actual geometry read 2026-11-18; independent check pending',
      'exam_representation_check':{'status':'final cross-book/examination comparison pending','examination_part_ids':[],
        'relation':'Source geometric representation; no claim of official marking or examination frequency.'},
      'mathematical_feature_review':{'status':'source given/solution figure read; parent exact length and angle derivations checked; independent acceptance pending',
        'method':'Use marked collinearity, midpoint, right angle and positive length constraints; independent Pythagoras/cosine-rule/vector checks support the parent results.'}})
pages=[{'pdf_page':page,'printed_page':page-12,'chapter':4,'page_status':'items enumerated',
 'item_ids':[r['item_id']for r in answers if r['source_pdf_page']==page]+[r['item_id']for r in figures if r['pdf_page']==page],
 'continuation_item_ids':[],'source_evidence':ev(page),'non_item_content':'All formal geometric tasks and four separate mathematical diagrams enumerated; intermediate AC in Try 56 question 2 is not counted as an assessed subpart.',
 'reader':'Codex author','date':'2026-11-18'}for page in[221,222]]
if __name__=='__main__':
    for name,data in[
      ('answers-YM-C4-geometry.json',{'scope':'All three source items and nine requested geometric outputs, PDF 221–222.','items':answers}),
      ('census-YM-C4-geometry.json',{'book':'YM','book_id':'8227-SRC-017','chapter':4,'source_path':SRC,'source_sha256':SHA,
        'scope':'PDF 221–222; every task and given/teaching diagram.','new_items':figures,'corrections':[],'pages':pages})]:
        (W/'tools/textbook-r5'/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
    print(len(answers),'items;',len(figures),'figures;',sum(len(r['subparts'])for r in answers),'outputs')
