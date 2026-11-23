"""Fixed-source author checks for YM C4 exam-style/revision, PDF225–228."""
import hashlib,json
from pathlib import Path
from author_YM_C4_trig_graphs import value,graph,reasoning
from author_YM_C4_composite_equations import roots,transform
W=Path(__file__).resolve().parents[2];ROOT=W.parents[2]
SRC='Y=mc as textbook.pdf';SHA='0b44ad3b67b1ea3de90cba780382d77deef347fae683cf6e28677f36c17a724f'
ARC='8227:2020:M1:T5:O02:D01';AREA='8227:2020:M1:T5:O02:D02';EXACT='8227:2020:M1:T6:O03:D01'
RANGE='8227:2020:M1:T3:O02:D02';FUNCTION='8227:2020:M1:T3:O01:D01';SKETCH='8227:2020:M1:T6:O02:D03'
TRANS='8227:2020:M1:T6:O05:D02';BND='8227:2020:M1:T6:O06:D01';ALL='8227:2020:M1:T6:O06:D02'
AP='8227:2020:M1:T2:O03:D01';GP='8227:2020:M1:T2:O03:D02';SUM='8227:2020:M1:T2:O05:D02'
TRI='8227:PRIOR:NSSCO:right-triangle-trig';SIM='8227:PRIOR:NSSCO:simultaneous-equations';D='(x*pi/180)'
def ev(page):
    name='YM-key-614-615-full'if page>=614 else'YM-C4-225'
    p=W/f'checks/r5/textbooks/{name}.png'
    return {'path':str(p.relative_to(ROOT)),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
def rounded(label,expr,key,kp=615,sf=3,dp=None,mode=None,units=None):
    p=value(label,expr,key,kp,
      'Independently derive the exact result from original source lengths,angles or progression terms. Retain full intermediate accuracy, then round only the requested output. Compare with the separately transcribed key.')
    p['operation']={'kind':'rounded','operands':[expr],**({'decimal_places':dp}if dp is not None else{'significant_figures':sf})}
    p['additional_operations']={'unrounded_exact':{'kind':'identity','operands':[expr]}}
    if mode:p['check_mode']=mode
    if units:p['units']=units
    return p
answers=[]
def add(kind,n,page,note,parts,direct,components=None,sketch=False,rep='text',roles=None):
    for p in parts:
        kp=p.pop('key_page_override',page if kind=='Example'else 615);p.pop('source_page_override',None)
        p.update(source_pdf_page=page,source_evidence=ev(page),answer_pdf_page=kp,
          answer_printed_page='A'+str(kp-586)if kp>=614 else kp-12,key_evidence=ev(kp),review_date='2026-11-18')
    row={'item_id':f'8227:TB:YM:C4:{kind}:{n}','source_pdf_page':page,'notes':note,
      'assessed_8227_demand_ids':direct,'component_demand_ids':components or[],
      'component_demand_roles':roles or{},
      'mapping_rationale':'Map the actual requested sector/arc, progression sum, exact special-angle value, range, bounded roots or sketch. Algebraic parameter recovery from function values is not interpreting a given graph. Acute inverse ratios and elementary right-triangle geometry are components, not principal-value classification or special-angle coverage unless that work is explicitly assessed.',
      'representation':rep,'sketch_response_required':sketch,
      'value_level_scope_decisions':[{'rule_id':'8227:QUAL03','status':'within'if kind=='Revision-Exercise-4'and n in[3,5]else'not applicable',
        'quoted_value':note,'reason':'The actual bounded-equation multiplier is 2.'if kind=='Revision-Exercise-4'and n in[3,5]else'No periodic trig equation is requested; context geometry is not an argument-multiplier exercise.'},
       {'rule_id':'8227:QUAL07','status':'within'if(kind=='Example'and n==58)or(kind=='Revision-Exercise-4'and n==5)else'not applicable',
        'quoted_value':note,'reason':'The original simple cosine transform and finite full-cycle interval determine the requested range/sketch.'if(kind=='Example'and n==58)or(kind=='Revision-Exercise-4'and n==5)else'No function range/sketch demand is asked.'}],
      'exam_style':True,'exam_style_basis':'Examples57/58 and TryNow57/58 are inside section4.3 explicitly headed Exam-Style Questions; RevisionExercise4 is a formal mark-tariff end-of-chapter assessment. This does not establish examination provenance or frequency.',
      'precision_angle_check':{'source':'Example57(a) specifies4decimal places in radians. Other numeric outputs/keys use3significant figures; exact surds/π answers are retained where asked. Revision5 uses superscript c for radian key values.',
        'comparison':'Use exact angles internally. Example57working reuses its rounded0.6435 andprints8.04375 for a sector: this is an approximate intermediate, not an exact/high-accuracy area. Distinguish stated show-that tolerance from later rounding.'},
      'expected_subpart_labels':[p['subpart']for p in parts],'subparts':parts}
    answers.append(row);return row

p=rounded('a','asin(3/5)','0.6435',225,dp=4,mode='show/prove',units='radian')
p2=reasoning('b:BAP','Sector BAP = 25 asin(3/5)/2 ≈ 8.0437638599 square units; the printed 8.04375 agrees at 3 significant figures but comes from the rounded angle0.6435.',
 'The sector centre is B, radius BA=BP=5, and angle ABP=asin(3/5). Hence area=25asin(3/5)/2. The independent exact value is8.0437638599…; the source instead computes25(0.6435)/2=8.04375. These agree to3significant figures. Do not copy the source intermediate as an exact quantity or assert5decimal-place accuracy.',225,'matches')
p2['additional_operations']={'exact_area':{'kind':'identity','operands':['25*asin(3/5)/2']},
 'source_intermediate_arithmetic':{'kind':'identity','operands':['25*(6435/10000)/2']},
 'full_precision_3sf':{'kind':'rounded','operands':['25*asin(3/5)/2'],'significant_figures':3}}
p3=value('b:DAQ','3**2*(pi/2)/2','9*pi/4',225,
 'DAQ is a quadrant centred at D with radius DA=3, so its area is9π/4 square units. The perpendicular rectangle sides fix π/2 exactly.')
p4=rounded('c','25*asin(3/5)/2+9*pi/4-9','6.11',225,units='square units')
p4['method']='Place D=(0,0),A=(0,3),B=(5,3),C=(5,0). P has x=5−√(25−9)=1. Trapezium ABPD therefore has area3(5+1)/2=9. The overlap of the two sectors is their area sum minus that trapezium; calculate both angles at full precision before rounding.'
add('Example',57,225,'Rectangle AB=5, BC=3; arc AP has centre B and arc AQ centre D, with P,Q on DC. Show angle ABP to4dp, calculate both sector areas, and the doubly curved shaded overlap. All radii and arc centres come from the diagram.',[p,p2,p3,p4],[AREA],[TRI],rep='diagram',roles={TRI:'Use acute right-triangle ratio to obtain the sector angle; no special-angle ratio is involved.'})

p=rounded('a','6*sqrt(2)*pi/4','6.66',614,units='cm')
p['method']='In right isosceles triangle BOC, BC=6√2 and angle CBD=π/4. Arc DC has centre B and radius BC, so s=(6√2)(π/4). Radius6 of the original semicircle is not this arc radius.'
p2=rounded('b','18/(9*pi-18)','1.75',615)
p2['method']='Region Q is sector BDC minus right triangle BOC: Q=(1/2)(72)(π/4)−18=9π−18. The left quadrant AOC has area9π, so P=9π−Q=18. Thus P/Q=18/(9π−18); all areas are positive and the ratio is dimensionless.'
add('Try-Now',57,225,'Semicircle centre O, radius6cm, C above O with OC perpendicular to AB; arc DC has centre B. Calculate that arc length, then the ratio of labelled regions P/Q to3sf. The two arcs have different centres/radii.',[p,p2],[ARC,AREA],[TRI],rep='diagram',roles={TRI:'The right isosceles triangle gives BC=6√2 and π/4; geometric prior technique, not a new standalone assessed objective.'})

p=value('a','Tuple(a,b)','Tuple(4,6)',226,
 'Evaluate the source f at0 and2π/3: a+b=10, a−b/2=1. Solve the two original simultaneous equations independently; do not infer coefficients from the illustrative solution graph.')
p['operation'].update(conditions=['a+b-10','a+b*cos(2*pi/3)-1'],unknowns=['a','b'])
p2=graph('b','cos','6','1','4','0','2*pi','radian',226,{'window_range':'Interval(-2,10)'},status='matches')
p3=value('c','4+6*cos(5*pi/6)','4-3*sqrt(3)',226,
 'Use the solved parameters and exact cos(5π/6)=−√3/2. The requested value is4−3√3, not a decimal substitute.')
add('Example',58,226,'For f(x)=a+b cosx on[0,2π], f(0)=10 and f(2π/3)=1; find a,b, the image range, and exact f(5π/6). The supplied information is function values, not a graph.',[p,p2,p3],[RANGE,EXACT],[FUNCTION,SIM],roles={FUNCTION:'Parameter part interprets supplied function values; it is not given-graph interpretation.',SIM:'Two linear simultaneous equations determine a,b.'})
for n,condition,key,note in[
 (1,['a+b*cos(pi/3)-5','a+b*cos(pi)-11'],'Tuple(7,-4)','f(x)=a+b cosx on[0,2π], f(π/3)=5 and f(π)=11: infer a=7,b=−4 from two exact function values.'),
 (2,['a+b*sin(pi/6)-4','a+b*sin(pi/2)-3'],'Tuple(5,-2)','f(x)=a+b sinx for all real x, f(π/6)=4 and f(π/2)=3: infer a=5,b=−2 from two exact function values.')]:
    p=value('parameters','Tuple(a,b)',key,615,
      'Substitute the two stated arguments, evaluate their exact special-angle ratios and solve the two source linear equations. No graph reading is asked.')
    p['operation'].update(conditions=condition,unknowns=['a','b'])
    row=add('Try-Now-58',n,226,note,[p],[],[FUNCTION,EXACT,SIM],roles={FUNCTION:'Use the function-value notation to form parameter conditions.',EXACT:'Special-angle ratios are intermediate coefficients, not separately requested outputs.',SIM:'Supporting linear parameter inference.'})
    row['evidence_role']='prerequisite/supporting symbolic trig-parameter practice; no forced graph-interpretation coverage'
    row['direct_demand_aspects']={'unmatched_supporting_practice':'The requested parameter inference is useful symbolic function support. No current decomposed8227demand names algebraic trig-parameter inference; do not inflate graph-interpretation coverage to force a link.'}

p=value('a','(2*sin(pi/6)+2*sqrt(3)*sin(pi/3))*p','4*p',615,
 'Use d>0 as the positive length scale (symbol p here). ED=ABsin30°=d and CE=BCsin60°=3d; C,E,D are collinear, so CD=4d. Intermediate CE/ED are not separately assessed answers.')
p['source_symbol_normalisation']='p denotes the source length scale d, strictly positive.'
p2=reasoning('b','angle CAD = atan(2/√3)',
 'AF=ABcos30°=√3d and BE=BCcos60°=√3d. Since AFED is a rectangle and d>0, AD=AF+BE=2√3d. In right triangle ACD, tan(CAD)=CD/AD=2/√3. CAD is acute, so the stated principal inverse expression follows; no principal-range classification is asked.',615,'show/prove')
p2['additional_operations']={'height_scale':{'kind':'identity','operands':['2*sin(pi/6)+2*sqrt(3)*sin(pi/3)']},
 'base_scale':{'kind':'identity','operands':['2*cos(pi/6)+2*sqrt(3)*cos(pi/3)']}}
add('Revision-Exercise-4',1,227,'Trapezium ABED has right angles E,D and C,E,D collinear. AB=2d, BC=2√3d, BAD=30°, CBE=60°, d>0. Find CD and show the specified inverse tangent for CAD; tariff2+3.',[p,p2],[EXACT],[TRI],rep='diagram',roles={TRI:'Right-triangle projections and acute inverse tangent are geometric components, not full principal-value coverage.'})

p=value('a','50/(1-sqrt(32/50))','250',615,
 'From positive GP terms, 50r²=32 and r must be positive. Thus r=4/5, |r|<1, and S∞=50/(1−4/5)=250. The negative root is excluded by the stated all-positive condition.')
p2=reasoning('b:i','tanx = 4/3',
 'The AP condition says 2(3cosx)=2sinx+(sinx+2cosx), hence4cosx=3sinx. As x is acute, cosx>0 and division is valid, giving tanx=4/3. This derives a ratio, not a bounded root set or a numerical angle.',615,'show/prove')
p2['additional_operations']={'ap_residual_equivalence':{'kind':'trig-identity-residual','operands':['2*3*cos(x)-(2*sin(x)+sin(x)+2*cos(x))','4*cos(x)-3*sin(x)']}}
p3=value('b:ii','20*(2*(2*4/5)+19*(3*3/5-2*4/5))/2','70',615,
 'Acute tanx=4/3 gives sinx=4/5, cosx=3/5. AP first term8/5 and difference1/5 give S20=20[16/5+19/5]/2=70. Retain exact fifths instead of premature decimal rounding.')
p3['dependency']={'source_part':'b:i','role':'Use the derived acute ratio and original AP first terms.'}
add('Revision-Exercise-4',2,227,'(a) Positive-term GP first term50 and third32: find sum to infinity. (b) AP first terms2sinx,3cosx,sinx+2cosx, x acute: show tanx=4/3 then find S20; tariff3+3+3.',[p,p2,p3],[GP,SUM,AP],[TRANS],roles={TRANS:'The AP middle-term condition rearranges to the requested tangent ratio. It does not ask for all bounded angles or special30/45/60values.'})

p=transform('a','sin(2*x)+3*cos(2*x)-3*(sin(2*x)-cos(2*x))','-2*sin(2*x)+6*cos(2*x)',[],
 'all source x for the original equation; converting to tan2x additionally needs cos2x != 0. If cos2x=0, the original residual is nonzero, so no solution is lost.',615)
p['additional_operations']={'requested_constant':{'kind':'identity','operands':['6/2']}}
p['source_requested_answer']='tan2x=3, so k=3; the residual equality verifies the independently derived reduction, not a verbatim key expression.'
p2=roots('b',f'sin(2*{D})+3*cos(2*{D})-3*(sin(2*{D})-cos(2*{D}))',
 ['-54.2','35.8'],615,[('tan','2*x','3',1)],lo='-90',hi='90',approx=True)
p2['dependency']={'source_part':'a','role':'Hence use tan2x=3, preserving the doubled original interval and excluded tangent poles.'}
add('Revision-Exercise-4',3,227,'Rewrite sin2x+3cos2x=3(sin2x−cos2x) as tan2x=k and find k; hence solve on −90°≤x≤90°. The source inclusive endpoints remain included in screening; tariff2+3.',[p,p2],[TRANS,BND,ALL])

p=rounded('area','6-9*atan(3/4)/2-2*atan(4/3)-pi/4','0.464',615,units='cm²')
p['method']='The 3–4–5 triangle is right at C, so its area is6. Its angles are A=atan(3/4), B=atan(4/3), C=π/2. Subtract the three internally tangent sectors with radii3,2,1: area=6−9A/2−4B/2−(π/2)/2. Check their radii sum to each side (3+2=5,3+1=4,2+1=3), so no overlap or misplaced tangency is assumed.'
add('Revision-Exercise-4',4,228,'ABC has sides AB=5, AC=4, BC=3cm; circles centred A,B,C have radii3,2,1cm and touch at E,F,G on the sides. Find the curvilinear triangular gap area; tariff3.',[p],[AREA],[TRI],rep='diagram',roles={TRI:'Prior triangle angles/area determine three sector angles; this is compound sector subtraction, not the distinct single-circle segment demand.'})

p=value('a','Tuple(a,b)','Tuple(3,-4)',615,
 'Use f(0)=a+b=−1 and f(π/2)=a+bcosπ=a−b=7. Solve for a=3,b=−4; no given graph is being interpreted.')
p['operation'].update(conditions=['a+b+1','a+b*cos(pi)-7'],unknowns=['a','b'])
p2=roots('b','3-4*cos(2*x)',['0.361','2.78'],615,[('cos','2*x','3/4',1)],unit='radian',hi='pi',approx=True)
p2['dependency']={'source_part':'a','role':'Use the function coefficients determined from its stated values.'}
p3=graph('c','cos','-4','2','3','0','pi','radian',615,
 {'sample_values':'Tuple(-1,7,-1)','window_range':'Interval(-1,7)'},at=['0','pi/2','pi'])
p3['dependency']={'source_part':'a','role':'Sketch the derived function only over its original0≤x≤πdomain.'}
add('Revision-Exercise-4',5,228,'f(x)=a+bcos2x on0≤x≤π, f(0)=−1 and f(π/2)=7. Find coefficients, both x-intercepts in radians, and sketch the restricted full cycle; tariff3+3+2.',[p,p2,p3],[BND,ALL,SKETCH],[FUNCTION,SIM],True,roles={FUNCTION:'Interpret function values to recover symbolic parameters; no input graph.',SIM:'Prior simultaneous equations recover a,b.'})

figures=[]
for n,page,label,note,parent,kind,rep,teaches in[
 (176,225,'Example57 given overlapping arcs','Rectangle AB=5,BC=3; arc AP centredB,arc AQ centredD; P,Q lie onDC. Shaded overlap must use the actual two circle centres.','Example:57','given-figure','diagram',[AREA]),
 (177,225,'Example57 radii and triangle construction','The solution adds BP=BA=5 and angleABP; AD=3. Thus P is1unit right ofD and trapeziumABPD has area9.','Example:57','teaching-figure','diagram',[AREA]),
 (178,225,'Example57 regionsAandB decomposition','RegionA is trapeziumABPD minus sectorBAP; RegionB is rectangle minus sectorDAQ. The desired overlap is sectorBAP+sectorDAQ−trapeziumABPD.','Example:57','teaching-figure','diagram',[AREA]),
 (179,225,'Try57 semicircle and offset-centre arc','Semicircle centreO,radius6; OC perpendicularAB. ArcDC has centreB,radiusBC=6√2. P,Q lie in left quadrantAOC,partitioned byDC.','Try-Now:57','given-figure','diagram',[ARC,AREA]),
 (180,226,'Example58 provisional cosine illustration','The preliminary guide is the basic cosine graph with ordinate±1andthe2π/3argument. It is an evaluation aid,not the actual unknown f=a+bcosx or given parameter data.','Example:58','teaching-figure','graph',[FUNCTION]),
 (181,226,'Example58 CAST at2π/3','The2π/3 angle is in quadrantII with cosine−1/2,using referenceπ/3.','Example:58','teaching-figure','diagram',[EXACT]),
 (182,226,'Example58 special-angle ratio triangle','Theπ/6,π/3 right triangle with sides1,√3,2supports cosπ/3=1/2.','Example:58','teaching-figure','diagram',[EXACT]),
 (183,226,'Example58 derived cosine graph','The derived f=4+6cosx on[0,2π] has maximum10andminimum−2. It is a solution graph,not given parameter data.','Example:58','teaching-figure','graph',[RANGE]),
 (184,226,'Example58 CAST at5π/6','The5π/6 angle is in quadrantII,referenceπ/6,andcosine−√3/2,so f(5π/6)=4−3√3.','Example:58','teaching-figure','diagram',[EXACT]),
 (185,227,'Revision4Q1 trapezium and triangles','AB=2d,BC=2√3d; C,E,D collinear; right anglesE,D; anglesBAD30°,CBE60°. Positive d gives CD4d,AD2√3d.','Revision-Exercise-4:1','given-figure','diagram',[EXACT]),
 (186,228,'Revision4Q4 three touching circles','CentresA,B,C form3–4–5triangle; radii3,2,1sum to side lengths. E,F,G are side tangencies; shaded gap is triangle minus three nonoverlapping sectors.','Revision-Exercise-4:4','given-figure','diagram',[AREA])]:
    figures.append({'item_id':f'8227:TB:YM:C4:Teaching-figure:{n}','item_kind':kind,'exercise':'Teaching figure','item_number':str(n),
      'pdf_page':page,'printed_page':page-12,'source_label':label,'parent_item_id':'8227:TB:YM:C4:'+parent,
      'notes':note,'what_it_shows':note,'assessed_8227_demand_ids':[],'component_demand_ids':[],
      'teaches_8227_demand_ids':teaches,'representation':rep,'source_evidence':ev(page),'learner_display':False,
      'value_level_scope_decisions':[{'rule_id':'8227:QUAL03','status':'not applicable','quoted_value':note,
        'reason':'Teaching/given geometry or solution sketch,not a periodic equation to solve.'}],
      'value_level_scope_review_status_r5':'author actual values read 2026-11-18; independent check pending',
      'exam_representation_check':{'status':'final cross-book/examination comparison pending','examination_part_ids':[],
        'relation':'Textbook exam-style section is labelled as such; it supplies no official examination attribution or award.'},
      'mathematical_feature_review':{'status':'source render and parent exact geometry/formula derivation checked; independent acceptance pending',
        'method':'Use original geometry constraints and exact function values,distinguishing source givens from solution additions and rounded illustrative workings.'}})
pages=[{'pdf_page':page,'printed_page':page-12,'chapter':4,'page_status':'items enumerated',
 'item_ids':[r['item_id']for r in answers if r['source_pdf_page']==page]+[r['item_id']for r in figures if r['pdf_page']==page],
 'continuation_item_ids':[],'source_evidence':ev(page),'non_item_content':'All section4.3 examples/TryNow tasks,RevisionExercise4 questions,and11separate given/teaching figures enumerated. Answer-section diagrams attach to their parent response checks.',
 'reader':'Codex author','date':'2026-11-18'}for page in range(225,229)]
if __name__=='__main__':
    for name,data in[
      ('answers-YM-C4-final.json',{'scope':'All10formal source items in section4.3andRevisionExercise4; every requested response.','items':answers}),
      ('census-YM-C4-final.json',{'book':'YM','book_id':'8227-SRC-017','chapter':4,'source_path':SRC,'source_sha256':SHA,
        'scope':'PDF225–228; every task and mathematical figure.','new_items':figures,'corrections':[],'pages':pages})]:
        (W/'tools/textbook-r5'/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
    print(len(answers),'items;',len(figures),'figures;',sum(len(r['subparts'])for r in answers),'outputs')
