"""R5 exact-ratio and directed-angle source readings,YM PDF181–184."""
import json,hashlib
from pathlib import Path
from author_YM_C4_trig_graphs import value
W=Path(__file__).resolve().parents[2];ROOT=W.parents[2]
SRC='Y=mc as textbook.pdf';SHA='0b44ad3b67b1ea3de90cba780382d77deef347fae683cf6e28677f36c17a724f'
EXACT='8227:2020:M1:T6:O03:D01'
def ev(page):
    name='YM-key-C4-606-609'if page==606 else'YM-C4-181'
    p=W/f'checks/r5/textbooks/{name}.png'
    return {'path':str(p.relative_to(ROOT)),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
def angle(label,theta,unit,beta,quadrant,key_page,printed_theta=None,turns=None):
    features={'reference_angle':beta,'quadrant':str(quadrant),'rotation_sign':'-1'if theta.startswith('-')else'1'}
    if printed_theta is not None:features['original_angle']=printed_theta
    if turns is not None:features['complete_turns']=str(turns)
    return {'subpart':label,'operation':{'kind':'angle-features','angle_unit':unit,'operands':[theta]},'printed_key_features':features,
      'check_mode':'sketch','key_page_override':key_page,
      'method':'Reduce the actual signed angle moduloone fullturn to locate its terminal ray,retain clockwise/anticlockwise rotation from its original sign,andmeasure the positive reference angle to the nearest x-axis ray. Compare the printed angle/reference labels anddrawn quadrant; full revolutions do not change the terminal ray.'}
answers=[]
def add(kind,n,page,note,parts,direct):
    for p in parts:
        kp=p.pop('key_page_override',page)
        p.update(source_pdf_page=page,source_evidence=ev(page),answer_pdf_page=kp,answer_printed_page='A20'if kp==606 else kp-12,key_evidence=ev(kp))
    row={'item_id':f'8227:TB:YM:C4:{kind}:{n}','source_pdf_page':page,'notes':note,
      'assessed_8227_demand_ids':direct,'component_demand_ids':[],
      'mapping_rationale':'Without-calculator exact ratios/lengths directly assess the special-angle demand. Drawing a general directed angle/reference ray is supporting prior knowledge; it is not silentlycounted as an AS exact-ratio,trig-graph,orunit-conversion question.',
      'exam_style':False,'exam_style_basis':'Ordinary Example/TryNow/unnumbered teaching illustration without an examination attribution.',
      'value_level_scope_decisions':[{'rule_id':'8227:LIMIT02','status':'not applicable','quoted_value':note,'reason':'Fixed exact evaluations orspecified directed angles,not general trigonometric equation solution forms.'}],
      'precision_angle_check':{'source':'Exact surds/piorinteger degree reference angles; show clockwise/anticlockwise direction andretain the actual signed angle even after fullturns.',
       'comparison':'Do not replace a negative directed angle byits positive acute reference angle. Rationalised andunrationalised equivalent exact values are both mathematical alternatives unless the particular source explicitlyrequires rationalisation.'},
      'expected_subpart_labels':[p['subpart']for p in parts],'subparts':parts}
    answers.append(row);return row

add('Example',17,181,'Without calculator,evaluate tan30/cos60and cos(pi/4)/[tan(pi/4)+tan²(pi/6)]; compare the exact rationalised source results.',
 [value('a','tan(pi/6)/cos(pi/3)','2*sqrt(3)/3',181),value('b','cos(pi/4)/(tan(pi/4)+tan(pi/6)**2)','3*sqrt(2)/8',181)],[EXACT])
add('Try-Now',17,181,'Without calculator,evaluate three mixed special-angle ratios; part(c)requires rationalising the binomial denominator sqrt2+2.',
 [value('a','sin(pi/6)/tan(pi/3)','1/(2*sqrt(3))',606),value('b','cos(pi/3)*sin(pi/6)/(cos(pi/4)*tan(pi/4))','sqrt(2)/4',606),
  value('c','tan(pi/4)*cos(pi/3)/(sin(pi/4)+tan(pi/4))','(2-sqrt(2))/2',606)],[EXACT])
add('Example',18,182,'Read the two right-angle markers:AB=6,CAB=45degrees,ADC=60degrees. RecoverBC,thenAC,thenADexactly across the connected right triangles.',
 [value('a','6*tan(pi/4)','6',182),value('b','6/cos(pi/4)','6*sqrt(2)',182),value('c','(6/cos(pi/4))/sin(pi/3)','4*sqrt(6)',182)],[EXACT])
row=add('Try-Now-18',1,182,'Right triangleCBAhasAC=8andangleC30degrees;DonBCmakesADB45degrees. Asked lengths areAB,AD,andBC. The source key(c)insteadanswersCD.',
 [value('a','8*sin(pi/6)','4',606),value('b','8*sin(pi/6)/sin(pi/4)','4*sqrt(2)',606),value('c','8*cos(pi/6)','4*sqrt(3)-4',606)],[EXACT])
row['subparts'][-1]['source_defect_id']='TB-YM-C4-Try18-Q1c-BC-VS-CD'
add('Try-Now-18',2,182,'TriangleABCwithAB=18,angleC60degreesandangleB45degrees: findBCwithout calculator. Drop a perpendicular to splitBCinto two positive projections in this acute triangle.',
 [value('BC','18*cos(pi/4)+18*sin(pi/4)/tan(pi/3)','3*sqrt(6)+9*sqrt(2)',606,
  'Height fromAtoBCis18sin45=9sqrt2. The B-side projection is18cos45=9sqrt2; the C-side projection isheight/tan60=3sqrt6. Their sum gives the exact requested base; compound-angle formulae are an optional validation route,not a required learner method here.')],[EXACT])

add('Example',19,183,'Draw positive directed angles250degrees,490degreesand9pi/8; showanticlockwise rotation andthe positive acute reference angles in the drawn quadrants.',
 [angle('a','250','degree','70',3,183,'250',0),angle('b','490','degree','50',2,183,'490',1),angle('c','9*pi/8','radian','pi/8',3,183,'9*pi/8',0)],[])
add('Try-Now',19,184,'Draw positive directed angles220degrees,520degreesand13pi/6,retaining the extra fullturn wherepresent andthe correct terminal quadrant.',
 [angle('a','220','degree','40',3,606,'220',0),angle('b','520','degree','20',2,606,'520',1),angle('c','13*pi/6','radian','pi/6',1,606,'13*pi/6',1)],[])
add('Example',20,184,'Draw clockwise angles−210degrees,−370degreesand−3⅔pi; their positive reference angles are30degrees,10degreesandpi/3respectively.',
 [angle('a','-210','degree','30',2,184,'-210',0),angle('b','-370','degree','10',4,184,'-370',1),angle('c','-11*pi/3','radian','pi/3',1,184,'-11*pi/3',1)],[])
row=add('Try-Now',20,184,'Draw clockwise angles−235degrees,−690degreesand−5pi/6. The final key ray is in the right quadrant,butits angle/reference labels are incorrect.',
 [angle('a','-235','degree','55',2,606,'-235',0),angle('b','-690','degree','30',1,606,'-690',1),angle('c','-5*pi/6','radian','pi/3',3,606,'pi/6',0)],[])
row['subparts'][-1]['source_defect_id']='TB-YM-C4-Try20c-ANGLE-LABELS'

# Each of the eight explicitly described "examples" in the two teaching tables
# has an individual source-item record; the two table figures remain separate.
new=[]
for n,(theta,q,page)in enumerate([(50,1,183),(130,2,183),(230,3,183),(310,4,183),(-50,4,184),(-130,3,184),(-230,2,184),(-310,1,184)],4):
    note=f'Unnumbered directed-angle teaching example:θ={theta}degrees,terminal quadrant{q},reference angle50degrees; '+('anticlockwise.'if theta>0 else'clockwise.')
    row=add('Worked-illustration',n,page,note,[angle('ray-and-reference',str(theta),'degree','50',q,page,str(theta),0)],[])
    row['subparts'][0]['response_evidence_role']='supporting source-illustration feature check; no separately posed learner sketch response'
    row['source_interpretation']={'drawing_role':'Rendered183–184show these eight rays in worked teaching tables. The later numbered Example19/20 andTryNow questions explicitly request drawings; those are separate source items.',
        'verification_status_is_not_response_demand':'The sketch status records an author check of the drawn ray and labels; it does not make a table illustration an assigned drawing task.'}
    new.append({'item_id':row['item_id'],'item_kind':'worked-illustration','exercise':'Worked illustration','item_number':str(n),
      'pdf_page':page,'printed_page':page-12,'notes':note,'assessed_8227_demand_ids':[],'component_demand_ids':[],
      'evidence_role':'prerequisite/supporting angle interpretation; no direct AS-demand coverage claimed',
      'representation':'diagram','source_evidence':ev(page),'answer_key':{'available':True,'pdf_pages':[page],'printed_pages':[page-12],
       'locator':'Inline positive/negative directed-angle worked table','source_path':SRC,'source_sha256':SHA}})

specs=[
 (181,'Special60degree ratio recap','Table repeats sin60=sqrt3/2,cos60=1/2,tan60=sqrt3andtheirpi/3notation; no new independently posed task.',None,[EXACT]),
 (181,'Example17parta30/60reference triangle','The part(a)reference triangle has30/60angles,hypotenuse2,andlegs1/sqrt3; it supports tan30/cos60.','Example:17',[EXACT]),
 (182,'Example18given two right triangles','AB6,CAB45degrees,ADC60degrees; right angles atBandCmust be read from the figure.','Example:18',[EXACT]),
 (182,'Example18partb45degree solution aid','The45degree right triangle haslegs1/1andhypotenusesqrt2; it supports the exact ACcalculation inpart(b).','Example:18',[EXACT]),
 (182,'TryNow18question1given triangle','AC8,angleC30degrees,ADB45degrees,andright angle atB;C,D,Bare collinear in that order. The asked final length isBC,notCD.','Try-Now-18:1',[EXACT]),
 (182,'TryNow18question2given triangle','AB18,angleB45degrees,angleC60degrees; the triangle is acute,so a perpendicular fromAfalls insideBC.','Try-Now-18:2',[EXACT]),
 (183,'Positive/negative rotation convention','Two Cartesian rays distinguish anticlockwisepositiveθfrom clockwisenegativeθ; signed sweep is separate from the acute reference angle.',None,[]),
 (183,'Positive-angle four-quadrant worked table','θ=50,130,230,310degrees,giving quadrantI,II,III,IVandreference50degreesin everycase.',None,[]),
 (183,'Example19partapositive-angle solution','The250degree anticlockwise sweep ends inquadrantIII,withreference70degrees.','Example:19',[]),
 (184,'Negative-angle four-quadrant worked table','θ=−50,−130,−230,−310degrees,giving quadrantIV,III,II,Iwithreference50degreesin everycase.',None,[]),
 (184,'Example20partanegative-angle solution','The−210degree clockwise sweep ends inquadrantII,withreference30degrees.','Example:20',[]),
 (181,'Example17partb45degree reference triangle','The part(b)reference triangle has45degrees,legs1/1andhypotenusesqrt2; it supports the exact mixed-ratio expression.','Example:17',[EXACT]),
 (182,'Example18partc30/60solution aid','The30/60right triangle haslegs1/sqrt3andhypotenuse2; it supplies sin60for the exact ADcalculation.','Example:18',[EXACT]),
 (183,'Example19partbpositive-angle solution','The490degree anticlockwise sweep includesone fullturn,ends inquadrantII,andhasreference50degrees.','Example:19',[]),
 (183,'Example19partcpositive-angle solution','The9pi/8anticlockwise sweep ends inquadrantIIIwithreferencepi/8.','Example:19',[]),
 (184,'Example20partbnegative-angle solution','The−370degree clockwise sweep includesone fullturn,ends inquadrantIV,andhasreference10degrees.','Example:20',[]),
 (184,'Example20partcnegative-angle solution','The−11pi/3clockwise sweep includesone fullturn,ends inquadrantI,andhasreferencepi/3.','Example:20',[])]
for n,(page,label,note,parent,teaches)in enumerate(specs,63):
    row={'item_id':f'8227:TB:YM:C4:Teaching-figure:{n}','item_kind':'teaching-figure','exercise':'Teaching figure','item_number':str(n),
      'pdf_page':page,'printed_page':page-12,'source_label':label,'parent_item_id':f'8227:TB:YM:C4:{parent}'if parent else None,
      'notes':note,'what_it_shows':note,'assessed_8227_demand_ids':[],'component_demand_ids':[],'teaches_8227_demand_ids':teaches,
      'representation':'diagram'if n!=63 else'table','source_evidence':ev(page),'learner_display':False,
      'value_level_scope_decisions':[{'rule_id':'8227:LIMIT02','status':'not applicable','quoted_value':note,'reason':'Teaching fixed exact ratios ordirected-angle rays; not a general-equation solution family.'}],
      'value_level_scope_review_status_r5':'author actual values/geometry/rotation read; independent check pending',
      'exam_representation_check':{'status':'final family/examination representation comparison pending','examination_part_ids':[],
       'relation':'Triangle/ray pictures are not automatically equivalent to any whole NSSCAS problem. Directed-angle drawings here are supporting prior knowledge,not automatic ASobjective coverage.'},
      'mathematical_feature_review':{'status':'author diagram labels/relations checked against parent derivation; independent check pending',
       'method':'Exact side ratios follow the marked30/45/60anglesandright angles. Directed rays follow signed rotation,coterminal quadrant andpositive reference angle; source keys withwrong labels are registered individually.'}}
    if not teaches:row['support_role']='Prerequisite angle/quadrant interpretation for later trigonometry; no separately assessed ASdemand link claimed.'
    part_labels={64:'a',66:'b',71:'a',73:'a',74:'b',75:'c',76:'b',77:'c',78:'b',79:'c'}
    if n in part_labels:row['parent_subpart']=part_labels[n]
    if n in[70,72]:row['parent_item_ids']=[f'8227:TB:YM:C4:Worked-illustration:{k}'for k in(range(4,8)if n==70 else range(8,12))]
    new.append(row)
pages=[]
for page in range(181,185):
    own=[r['item_id']for r in answers if r['source_pdf_page']==page]+[r['item_id']for r in new if r['pdf_page']==page and r['item_kind']=='teaching-figure']
    pages.append({'pdf_page':page,'printed_page':page-12,'chapter':4,'page_status':'items enumerated','item_ids':own,'continuation_item_ids':[],
      'source_evidence':ev(page),'non_item_content':'All formal tasks,eight unnumbered worked angle examples,andmathematical diagrams/tables are enumerated; rationalisation/advice prose is not an extra problem.',
      'reader':'Codex author','date':'2026-11-17'})
if __name__=='__main__':
    for name,data in[
      ('answers-YM-C4-exact-angles.json',{'scope':'All formal tasksonPDF181–184andall eight worked directed-angle table examples; exact ratios are direct ASpractice,ray drawing remains supporting.','items':answers}),
      ('census-YM-C4-exact-angles.json',{'book':'YM','book_id':'8227-SRC-017','chapter':4,'source_path':SRC,'source_sha256':SHA,
       'scope':'PDF181–184inclusive; every source task,worked angle example andmathematical figure/table enumerated.','new_items':new,'corrections':[],'pages':pages})]:
        (W/'tools/textbook-r5'/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
    print(len(answers),'response items;',len(new)-8,'figures;',sum(len(r['subparts'])for r in answers),'outputs')
