"""R5 source annotations for related angles,YM PDF185–188."""
import json,hashlib
from pathlib import Path
import sympy as sp
from author_YM_C4_trig_graphs import value
W=Path(__file__).resolve().parents[2];ROOT=W.parents[2]
SRC='Y=mc as textbook.pdf';SHA='0b44ad3b67b1ea3de90cba780382d77deef347fae683cf6e28677f36c17a724f'
EXACT='8227:2020:M1:T6:O03:D01';PROP='8227:2020:M2:T3:O01:D02'
def ev(page):
    name='YM-key-C4-606-609'if page in[606,607]else'YM-C4-185'
    p=W/f'checks/r5/textbooks/{name}.png'
    return {'path':str(p.relative_to(ROOT)),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
answers=[]
def add(kind,n,page,note,parts,direct):
    for p in parts:
        kp=p.pop('key_page_override',page)
        p.update(source_pdf_page=page,source_evidence=ev(page),answer_pdf_page=kp,answer_printed_page='A'+str(kp-586)if kp>=602 else kp-12,key_evidence=ev(kp))
    row={'item_id':f'8227:TB:YM:C4:{kind}:{n}','source_pdf_page':page,'notes':note,'assessed_8227_demand_ids':direct,'component_demand_ids':[],
      'mapping_rationale':'A directed angle from reference/quadrant is supporting prior knowledge. Same-function acute reduction andgiven-ratio transformations assess related-angle properties. Exact numerical special-angle evaluations assess the exact-value demand. No graph orreciprocal-function demand is invented from the independent verification method.',
      'value_level_scope_decisions':[{'rule_id':'8227:LIMIT02','status':'not applicable','quoted_value':note,'reason':'Fixed angle/property tasks,not a general trigonometric solution family. Where an angle is recovered,its explicit one-turn interval is preserved.'}],
      'exam_style':False,'exam_style_basis':'Ordinary Example/TryNowwithout an examination attribution or exam-style label.',
      'precision_angle_check':{'source':'Retain the actual source degree/radian unit,exact acute reference angle,same trigonometric function where requested,andexact values without a calculator.',
       'comparison':'Equivalent evaluated numbers alone do not satisfy a request for the same function of an acute angle. Quadrant signs andgiven finite-ratio domains remain explicit.'},
      'expected_subpart_labels':[p['subpart']for p in parts],'subparts':parts}
    if PROP in direct:row['direct_demand_aspects']={PROP:'Related-angle properties of sin/cos/tan only; no sec/cosec/cot orgraph response. This is a partial aspect,not fullsix-function properties/graphs coverage.'}
    answers.append(row);return row
def reference(label,beta,q,lo,hi,unit,key,kp):
    p=value(label,'0',key,kp,'Locate the positive coterminal ray from the acute reference angle andspecified quadrant,then retain onlythe value in the explicitlystated open interval. A negative interval requires a clockwise representative,not the positive coterminal angle.')
    p['operation']={'kind':'reference-angle-solutions','angle_unit':unit,'operands':[beta,str(q),lo,hi],'left_open':True,'right_open':True};return p
def reduction(label,family,theta,sign,beta,kp):
    p=value(label,'0',f'Tuple({sign},{beta})',kp,'Derive terminal quadrant andpositive acute reference angle from the original degree angle. Keep the original function andapply its quadrant sign; compare the actual printed same-function form,not just its decimal value.')
    p['operation']={'kind':'same-function-reduction','angle_unit':'degree','family':family,'operands':[theta]}
    p['response_form_check']={'required_family':family,'printed_family':family,'acute_angle_unit':'degree','printed_form':f'{"-"if sign==-1 else""}{family}({beta}degrees)'};return p
def ratio(label,family,expr,given,key,kp):
    p=value(label,'0',key,kp,'Use the relevant related-angle identity symbolically,then substitute the given finite ratio. No particular value orquadrant oftheta is assumed when the identity alreadydetermines the result.')
    p['operation']={'kind':'trig-given-ratio','given_family':family,'operands':[expr,given]};return p

add('Example',21,185,'Given referenceβ=35degrees inquadrantIVwith0<θ<360degrees,andβ=pi/3inquadrantIIwith−2pi<θ<0,find the signed angle ineachspecified interval.',
 [reference('a','35',4,'0','360','degree','FiniteSet(325)',185),reference('b','pi/3',2,'-2*pi','0','radian','FiniteSet(-4*pi/3)',185)],[])
add('Try-Now',21,185,'Findθfromreference/quadrant/interval:(a)40degrees,QIII,0..360;(b)60degrees,QII,−360..0;(c)pi/4,QIV,0..2pi. Everybound is strict.',
 [reference('a','40',3,'0','360','degree','FiniteSet(220)',606),reference('b','60',2,'-360','0','degree','FiniteSet(-240)',606),reference('c','pi/4',4,'0','2*pi','radian','FiniteSet(7*pi/4)',606)],[])
add('Example',22,187,'Express tan135,sin246andcos315degrees using the same trigonometric function ofan acute angle; retain eachfunction andthe correct sign.',
 [reduction('a','tan','135',-1,'45',187),reduction('b','sin','246',-1,'66',187),reduction('c','cos','315',1,'45',187)],[PROP])
add('Try-Now',22,187,'Reduce sin150,cos250andtan330degrees to the same function ofan acute angle,not arbitrary numericallyequivalent expressions.',
 [reduction('a','sin','150',1,'30',606),reduction('b','cos','250',-1,'70',606),reduction('c','tan','330',-1,'30',606)],[PROP])
add('Example',23,187,'Given sinθ=−0.25,find sin(pi−θ),sin(pi+θ),sin(2pi−θ). A4x source reading confirms sin is printed inpart(c); no missing-function defect exists.',
 [ratio('a','sin','sin(pi-x)','-1/4','-1/4',187),ratio('b','sin','sin(pi+x)','-1/4','1/4',187),ratio('c','sin','sin(2*pi-x)','-1/4','1/4',187)],[PROP])
add('Try-Now-23',1,187,'Given tanθ=−1.5,find the tangent values atpi−θ,pi+θand2pi−θ; finite given tangent excludes its undefined poles.',
 [ratio('a','tan','tan(pi-x)','-3/2','3/2',606),ratio('b','tan','tan(pi+x)','-3/2','-3/2',606),ratio('c','tan','tan(2*pi-x)','-3/2','3/2',606)],[PROP])
add('Try-Now-23',2,187,'Given cosθ=0.75,find cosine values atpi−θ,pi+θand2pi−θwithout choosing a particularθ.',
 [ratio('a','cos','cos(pi-x)','3/4','-3/4',606),ratio('b','cos','cos(pi+x)','3/4','-3/4',606),ratio('c','cos','cos(2*pi-x)','3/4','3/4',606)],[PROP])
add('Try-Now-23',3,187,'Given sinθ=0.7,find sine values atpi−θ,pi+θand2pi−θ; sign changes follow the identity,not a guessed original quadrant.',
 [ratio('a','sin','sin(pi-x)','7/10','7/10',606),ratio('b','sin','sin(pi+x)','7/10','-7/10',606),ratio('c','sin','sin(2*pi-x)','7/10','-7/10',606)],[PROP])
add('Example',24,188,'Without calculator,evaluate cos150degrees,tan225degreesandsin5pi/3byrelated special angles andquadrant signs.',
 [value('a','cos(150*pi/180)','-sqrt(3)/2',188),value('b','tan(225*pi/180)','1',188),value('c','sin(5*pi/3)','-sqrt(3)/2',188)],[EXACT])
add('Try-Now',24,188,'Nine exact special-angle values inbothunits:cos240,tan210,sin150,cos330degrees;sin3pi/4,cos2pi/3,tan5pi/3,sin5pi/4,cos7pi/4. Keycontinues fromPDF606to607.',
 [value('a','cos(240*pi/180)','-1/2',606),value('b','tan(210*pi/180)','sqrt(3)/3',606),value('c','sin(150*pi/180)','1/2',606),
  value('d','cos(330*pi/180)','sqrt(3)/2',607),value('e','sin(3*pi/4)','sqrt(2)/2',607),value('f','cos(2*pi/3)','-1/2',607),
  value('g','tan(5*pi/3)','-sqrt(3)',607),value('h','sin(5*pi/4)','-sqrt(2)/2',607),value('i','cos(7*pi/4)','sqrt(2)/2',607)],[EXACT])

# Verify every relation inboth nine-entry degree/radian teaching tables,not a
# sample ofthem. The identitieshold ontheir common defined domains.
x=sp.Symbol('x',real=True);identity_checks=[]
for transform,signs in[(sp.pi-x,[1,-1,-1]),(sp.pi+x,[-1,-1,1]),(2*sp.pi-x,[-1,1,-1])]:
 for fn,sign in zip([sp.sin,sp.cos,sp.tan],signs):
    assert sp.trigsimp(fn(transform)-sign*fn(x))==0
    identity_checks.append(f'{fn(transform)}={sign}*{fn(x)}')

figures=[]
specs=[
 (185,'Example21partasigned-angle solution','QuadrantIVray,reference35degreesandθ325degreeswithanticlockwise sweep.','Example:21','a',[],'diagram'),
 (185,'Example21partbsigned-angle solution','QuadrantIIray,referencepi/3andclockwiseθ−4pi/3in−2pi..0.','Example:21','b',[],'diagram'),
 (185,'Sine unit-circle/unwrapping plate','Unit-circle vertical projections correspond to sine ordinates throughallfourquadrants; signs andrelated-angle identities are labelled.',None,None,[PROP],'diagram'),
 (186,'Cosine unit-circle/unwrapping plate','Unit-circle horizontal projections correspond to cosine ordinates throughallfourquadrants; quadrantII/IIIare negative.',None,None,[PROP],'diagram'),
 (186,'Tangent unit-circle/graph plate','Tangent sign pairs areQI/QIIIpositive,QII/QIVnegative; graph poles at90/270degrees remain separate from the unit-circle projection diagram.',None,None,[PROP],'diagram'),
 (186,'Degree related-angle identity table','Allnine sin/cos/tanrelations for180−β,180+βand360−βare shown withtheir correct quadrant signs.',None,None,[PROP],'table'),
 (186,'CAST mnemonic','QuadrantIallthreepositive;QIIonlysinepositive;QIIIonlytangentpositive;QIVonlycosinepositive. This is a sign mnemonic,not an independent proof task.',None,None,[PROP],'diagram'),
 (187,'Radian related-angle identity table','Allnine relations forpi−β,pi+βand2pi−βmatch the degree table under180degrees=pi radians.',None,None,[PROP],'table'),
 (188,'Example24partareference-angle ray','The150degree ray lies inquadrantIIwithreference30degreesandnegativecosine.','Example:24','a',[EXACT],'diagram'),
 (188,'Example24parta30/60reference triangle','A30/60triangle haslegs1/sqrt3andhypotenuse2;cos30=sqrt3/2supplies the exact magnitude.','Example:24','a',[EXACT],'diagram'),
 (188,'Example24partbreference-angle ray','The225degree ray lies inquadrantIIIwithreference45degreesandtangentpositive.','Example:24','b',[EXACT],'diagram'),
 (188,'Example24partb45degree reference triangle','Legs1/1andhypotenusesqrt2give tan45=1.','Example:24','b',[EXACT],'diagram'),
 (188,'Example24partcreference-angle ray','The5pi/3ray lies inquadrantIVwithreferencepi/3andnegativesine.','Example:24','c',[EXACT],'diagram')]
for n,(page,label,note,parent,part,teaches,rep)in enumerate(specs,80):
    row={'item_id':f'8227:TB:YM:C4:Teaching-figure:{n}','item_kind':'teaching-figure','exercise':'Teaching figure','item_number':str(n),
      'pdf_page':page,'printed_page':page-12,'source_label':label,'parent_item_id':f'8227:TB:YM:C4:{parent}'if parent else None,'parent_subpart':part,
      'notes':note,'what_it_shows':note,'assessed_8227_demand_ids':[],'component_demand_ids':[],'teaches_8227_demand_ids':teaches,
      'representation':rep,'source_evidence':ev(page),'learner_display':False,
      'value_level_scope_decisions':[{'rule_id':'8227:LIMIT02','status':'not applicable','quoted_value':note,'reason':'Fixed-angle/related-function teaching,not general equation solutions.'}],
      'value_level_scope_review_status_r5':'author actual units/quadrant signs read; independent check pending',
      'exam_representation_check':{'status':'finalcross-book/examination representation comparison pending','examination_part_ids':[],
       'relation':'These are source teaching/solution figures; no examinationfrequency orwhole-demand coverage follows from their presence.'},
      'mathematical_feature_review':{'status':'author identities/figure labels independently checked; independent acceptance pending',
       'method':'Allnine related-angle identities are checked symbolically; their degree/radian correspondence andCASTsigns agree. Specific rays/triangles agree withthe independently computed parent answers.'}}
    if n in[82,83,84,85,86,87]:row['mathematical_feature_review']['symbolic_identity_checks']=identity_checks
    if not teaches:row['support_role']='Supporting reference-angle interpretation; no direct ASobjective coverage.'
    figures.append(row)
pages=[]
for page in range(185,189):
    own=[r['item_id']for r in answers if r['source_pdf_page']==page]+[r['item_id']for r in figures if r['pdf_page']==page]
    pages.append({'pdf_page':page,'printed_page':page-12,'chapter':4,'page_status':'items enumerated','item_ids':own,'continuation_item_ids':[],
      'source_evidence':ev(page),'non_item_content':'All formal tasks andmathematical figures/tables enumerated; property-derivation prose belongs to the linked teaching plates.',
      'reader':'Codex author','date':'2026-11-17'})
if __name__=='__main__':
    for name,data in[
      ('answers-YM-C4-related-angles.json',{'scope':'All10formal response items onPDF185–188; same-function acute forms are structurallychecked andbasic-three properties are explicitlypartial M2demand evidence.','items':answers}),
      ('census-YM-C4-related-angles.json',{'book':'YM','book_id':'8227-SRC-017','chapter':4,'source_path':SRC,'source_sha256':SHA,
       'scope':'PDF185–188inclusive; separate diagrams for eachassessed part are individuallyrecorded; integrated named teaching plates/tables remain coherent source figures.','new_items':figures,'corrections':[],'pages':pages})]:
        (W/'tools/textbook-r5'/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
    print(len(answers),'items;',len(figures),'figures;',sum(len(r['subparts'])for r in answers),'outputs')
