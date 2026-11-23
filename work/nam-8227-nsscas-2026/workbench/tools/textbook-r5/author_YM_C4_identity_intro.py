"""Explicit source census and independent answers for YM PDF193–196."""
import hashlib,json
from pathlib import Path
from author_YM_C4_trig_graphs import value
from author_YM_C4_ratios import numeric
W=Path(__file__).resolve().parents[2];ROOT=W.parents[2]
SRC='Y=mc as textbook.pdf';SHA='0b44ad3b67b1ea3de90cba780382d77deef347fae683cf6e28677f36c17a724f'
PROP='8227:2020:M2:T3:O01:D02';REC='8227:2020:M2:T3:O01:D01'
PROOF='8227:2020:M1:T6:O05:D01';SQUARE='8227:2020:M2:T3:O02:D01'
def ev(page):
    name={607:'YM-key-607-Try28',608:'YM-key-608-Try29-30'}.get(page,'YM-C4-193')
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
      'mapping_rationale':'Ratio evaluation, reciprocal comparison and proof are distinct learner outputs. A numerical equality comparison is not an identity proof. Source-imposed obtuse/acute restrictions determine signs; a wider interval need not determine a unique quadrant when squared ratios already give a unique result.',
      'value_level_scope_decisions':[{'rule_id':'8227:LIMIT02','status':'not applicable','quoted_value':note,
        'reason':'These tasks ask exact ratios, comparisons or identity proofs, not general solutions of trigonometric equations. Actual bounded-angle conditions are retained to select all admissible ratio branches.'}],
      'exam_style':False,'exam_style_basis':'Ordinary Example/TryNow or inline teaching illustration; no exam-style attribution.',
      'precision_angle_check':{'source':'Exact symbolic values without a calculator. Degree intervals in Try29Q1/Q2/Q4 and radian intervals in Q3/Example30/Try30 are kept as stated.',
       'comparison':'No decimal rounding is substituted for an exact output. Unit conversion in the checker preserves each original interval; it does not change the learner prompt.'},
      'expected_subpart_labels':[p['subpart']for p in parts],'subparts':parts}
    if PROP in direct:row['direct_demand_aspects']={PROP:'Related and reciprocal ratio properties only; no graph output, so not whole six-function graph-demand coverage.'}
    answers.append(row);return row

parts=[]
for label,target,key in [('a','cos(x)','-15/17'),('b','1/sec(x)','-15/17'),
 ('c','cos(x)-1/sec(x)','0'),('d','cot(x)','-15/8'),
 ('e','cos(x)/sin(x)','-15/8'),('f','cot(x)-cos(x)/sin(x)','0')]:
    p=numeric(label,'sin','8/17',target,f'FiniteSet({key})',607,interval=['pi/2','pi'])
    if label in['c','f']:
        p['printed_key_text']='The answers of the preceding pair are the same.'
        p['normalisation_note']='The derived difference is zero, which verifies this requested comparison statement; zero is not presented as a verbatim printed numerical answer.'
    parts.append(p)
add('Try-Now-29',1,193,'Given sinθ=8/17 and θ obtuse, show all working without finding θ: evaluate cosθ,1/secθ,cotθ,cosθ/sinθ and compare the two corresponding pairs.',parts,[REC,PROP])
parts=[]
for label,target,key,kp in [('a','cot(x)**2','225/64',607),('b','csc(x)**2-1','225/64',607),
 ('c','cot(x)**2-(csc(x)**2-1)','0',608),('d','tan(x)**2','64/225',608),
 ('e','sec(x)**2-1','64/225',608),('f','tan(x)**2-(sec(x)**2-1)','0',608)]:
    p=numeric(label,'tan','8/15',target,f'FiniteSet({key})',kp,interval=['pi/2','2*pi'])
    if label in['c','f']:
        p['printed_key_text']='The answers of the preceding pair are the same.'
        p['normalisation_note']='Zero difference normalises the requested equality comparison, not a printed zero answer.'
    parts.append(p)
add('Try-Now-29',2,193,'Given 15tanφ−8=0 and90°<φ<360°, evaluate cot²φ,cosec²φ−1,tan²φ,sec²φ−1 and compare the corresponding pairs. Squared ratios remove the sign branch.',parts,[REC,PROP,SQUARE])
add('Try-Now-29',3,193,'Given5sinβ+4=0,0<β<2π, determine every possible value of3tanβ without a calculator; both III and IV satisfy the given negative sine.',
 [numeric('all-values','sin','-4/5','3*tan(x)','FiniteSet(-4,4)',608,interval=['0','2*pi'])],[PROP])
p=value('mixed-ratios','0','FiniteSet(11)',608,'Treat x and y as independent angles. Derive all compatible ratios from cosx=3/4,0<x<180°, and siny=3/5,90°<y<270°, respectively; combine 7cosec²x with4secy only after each original interval is enforced.')
p['operation']={'kind':'independent-ratio-sum','operands':[],'terms':[
 {'coefficient':'7','operation':{'kind':'numeric-given-trig-ratio','given_family':'cos','operands':['3/4','csc(x)**2'],'angle_interval':['0','pi']}},
 {'coefficient':'4','operation':{'kind':'numeric-given-trig-ratio','given_family':'sin','operands':['3/5','sec(x)'],'angle_interval':['pi/2','3*pi/2']}}]}
add('Try-Now-29',4,193,'Evaluate7cosec²x+4secy for siny=3/5,90°<y<270° and cosx=3/4,0°<x<180°. The two variables have distinct intervals; y is quadrantII andx quadrantI.',[p],[REC,PROP])

def symbolic(label,family,given,target,key,kp,condition):
    p=value(label,'0',key,kp,'Read the original acute/obtuse condition, determine sine/cosine signs, derive the missing positive magnitude with sin²+cos²=1, and substitute into the expanded related-angle expression. A negative cosine in quadrantII is not replaced by an arbitrary positive square root.')
    p['operation']={'kind':'quadrant-given-symbolic-ratio','given_family':family,'angle_condition':condition,
      'given_value_condition':'value > 0'if family=='tan'else'0 < value < 1','operands':[target,given]}
    return p
add('Example',30,194,'The acute angle x radians satisfies tanx=k withk>0. Express tan(π−x),tan(π/2−x) and sinx in terms ofk, with positive hypotenuse√(1+k²).',
 [symbolic('a','tan','k','tan(pi-x)','-k',194,'acute'),
  symbolic('b','tan','k','tan(pi/2-x)','1/k',194,'acute'),
  symbolic('c','tan','k','sin(x)','k/sqrt(1+k**2)',194,'acute')],[PROP,REC])
add('Try-Now',30,194,'θ is obtuse in radians andsinθ=q,so0<q<1 andcosθ<0. Derive cosθ,tanθ,sin(θ+π) andsin(π/2−θ) with the correct signed root.',
 [symbolic(label,'sin','q',target,key,608,'obtuse')for label,target,key in[
 ('a','cos(x)','-sqrt(1-q**2)'),('b','tan(x)','-q/sqrt(1-q**2)'),
 ('c','sin(x+pi)','-q'),('d','sin(pi/2-x)','-sqrt(1-q**2)')]],[PROP])

# Three explicitly printed unnumbered numerical illustrations, not invented tasks.
new_items=[]
for n,(left,right,note)in enumerate([
 ('sin(25*pi/180)','cos(65*pi/180)','Complementary25° and65° give sin25°=cos65°.'),
 ('cos(53*pi/180)','sin(37*pi/180)','Complementary53° and37° give cos53°=sin37°.'),
 ('tan(20*pi/180)','cot(70*pi/180)','Complementary20° and70° give tan20°=cot70°. Neither angle is a pole.')],1):
    p=value('identity',f'({left})-({right})','0',193,'Use the complementary-angle identity on the actual degree arguments; compare zero difference with the printed equality on its common defined domain.')
    p['check_mode']='show/prove'
    row=add('Illustration-complementary',n,193,note,[p],[PROP])
    new_items.append({'item_id':row['item_id'],'item_kind':'worked-illustration','exercise':'Unnumbered complementary-angle illustration','item_number':str(n),
      'pdf_page':193,'printed_page':181,'notes':note,'assessed_8227_demand_ids':[PROP],'component_demand_ids':[],
      'representation':'text','source_evidence':ev(193),'learner_display':False,
      'evidence_role':'inline worked illustration, not an additional learner exercise'})
p=value('proof','(sin(x)+cos(x))**2-(1+2*sin(x)*cos(x))','0',196,
 'Expand the left square to sin²x+2sinxcosx+cos²x; replace sin²x+cos²x by1 to obtain the stated right side. All terms are defined for every real x, so no denominator or reversible-step restriction is needed.')
p['check_mode']='show/prove';p['proof_steps']=['Expand the left square.','Group sin²x+cos²x.','Substitute1 andretain2sinxcosx.','Identify the stated RHS.']
add('Example',31,196,'Prove(sinx+cosx)²≡1+2sinxcosx by expanding one side and applying the basic Pythagorean identity; no denominator exclusions are needed.',[p],[PROOF])

specs=[
 (193,'Complementary-angle right triangle','Legsx,y,hypotenuser andacuteθ/90°−θ exchange sine/cosine and tangent/cotangent.',None,[PROP],'diagram'),
 (193,'Complementary degree/radian property table','Six listed degree/radian identities agree under90°=π/2; the adjacent three numerical illustrations are separately recorded.',None,[PROP],'table'),
 (194,'Example30 positive acute triangle','Adjacent1,oppositek>0,hypotenuse√(1+k²),with x andπ/2−x complementary.','Example:30',[PROP,REC],'diagram'),
 (194,'Unit circle signed-coordinate derivation','The first circle labels P(x,y),radius1,and positive coordinate projections to motivate sine/cosine.',None,[PROP],'diagram'),
 (194,'Unit circle trigonometric-coordinate derivation','The second circle rewrites P(cosθ,sinθ),radius1,with projectionscosθ andsinθ.',None,[PROP],'diagram'),
 (194,'Quotient and square identity derivations','tan=sin/cos,cot=cos/sin;sin²+cos²=1;division gives1+cot²=cosec² andtan²+1=sec² only on their defined denominator domains.',None,[PROOF,REC,SQUARE],'table'),
 (195,'Nine rearranged Pythagorean identities','The three base square identities are rearranged into nine equivalent expressions on common defined domains.',None,[PROOF,SQUARE],'table'),
 (195,'Six-function mnemonic hexagon','The labelled order sin,cos,cot,cosec,sec,tan surrounds1; this is a mnemonic rather than a proof.',None,[REC,PROP],'diagram'),
 (195,'Reciprocal-identity hexagon','Opposite vertices pair tan/cot,sin/cosec,cos/sec; identities apply where both sides exist.',None,[REC],'diagram'),
 (195,'Quotient-identity hexagon','Clockwise fromtan gives sin/cos; anticlockwise fromcot gives cos/sin, with denominator restrictions.',None,[REC],'diagram'),
 (195,'Product-identity hexagon','Each listed function is the product of adjacent functions on their common defined domains; removable singularities are not silently restored.',None,[PROP,REC],'diagram'),
 (195,'Pythagorean clockwise shaded hexagon','The shaded mnemonic encodes sin²+cos²=1, tan²+1=sec² and1+cot²=cosec².',None,[PROOF,SQUARE],'diagram'),
 (195,'Pythagorean anticlockwise shaded hexagon','The second shaded mnemonic encodes1−cos²=sin²,sec²−1=tan²,cosec²−cot²=1.',None,[PROOF,SQUARE],'diagram')]
for n,(page,label,note,parent,teaches,rep)in enumerate(specs,108):
    new_items.append({'item_id':f'8227:TB:YM:C4:Teaching-figure:{n}','item_kind':'teaching-figure','exercise':'Teaching figure','item_number':str(n),
      'pdf_page':page,'printed_page':page-12,'source_label':label,'parent_item_id':f'8227:TB:YM:C4:{parent}'if parent else None,
      'notes':note,'what_it_shows':note,'assessed_8227_demand_ids':[],'component_demand_ids':[],'teaches_8227_demand_ids':teaches,
      'representation':rep,'source_evidence':ev(page),'learner_display':False,
      'value_level_scope_decisions':[{'rule_id':'8227:LIMIT02','status':'not applicable','quoted_value':note,'reason':'Teaching identities/ratios,not general trigonometric solution forms.'}],
      'value_level_scope_review_status_r5':'author actual formulae,angles and denominator restrictions read; independent check pending',
      'exam_representation_check':{'status':'final cross-book/examination representation comparison pending','examination_part_ids':[],
        'relation':'Teaching mnemonic or derivation,not an examination frequency claim.'},
      'mathematical_feature_review':{'status':'author formula identities checked symbolically; independent acceptance pending',
        'method':'Every printed reciprocal,quotient,product and square relation was symbolically reduced to zero on common defined domains. Mnemonic placement was compared with these equations; the diagram itself is not treated as proof.'}})
pages=[]
for page in range(193,197):
    pages.append({'pdf_page':page,'printed_page':page-12,'chapter':4,'page_status':'items enumerated',
      'item_ids':[r['item_id']for r in answers if r['source_pdf_page']==page]+[r['item_id']for r in new_items if r['pdf_page']==page and r['item_kind']=='teaching-figure'],
      'continuation_item_ids':[],'source_evidence':ev(page),
      'non_item_content':'All tasks,inline numerical illustrations and mathematical figures/tables enumerated. PDF196 proof-guidance prose and hints box are retained as instructional evidence,not a new exercise or diagram.',
      'reader':'Codex author','date':'2026-11-17'})
if __name__=='__main__':
    import sympy as sp
    x=sp.Symbol('x',real=True)
    relations=[sp.sin(sp.pi/2-x)-sp.cos(x),sp.cos(sp.pi/2-x)-sp.sin(x),sp.tan(sp.pi/2-x)-sp.cot(x),
      sp.tan(x)-1/sp.cot(x),sp.sin(x)-1/sp.csc(x),sp.cos(x)-1/sp.sec(x),
      sp.tan(x)-sp.sin(x)/sp.cos(x),sp.cot(x)-sp.cos(x)/sp.sin(x),
      sp.sin(x)-sp.cos(x)*sp.tan(x),sp.cos(x)-sp.sin(x)*sp.cot(x),sp.tan(x)-sp.sin(x)*sp.sec(x),
      sp.cot(x)-sp.cos(x)*sp.csc(x),sp.sec(x)-sp.tan(x)*sp.csc(x),sp.csc(x)-sp.cot(x)*sp.sec(x),
      sp.sin(x)**2+sp.cos(x)**2-1,1+sp.cot(x)**2-sp.csc(x)**2,sp.tan(x)**2+1-sp.sec(x)**2]
    assert all(sp.trigsimp(relation)==0 for relation in relations)
    for name,data in[
      ('answers-YM-C4-identity-intro.json',{'scope':'All7formal items and3unnumbered complementary-angle illustrations onPDF193–196.','items':answers}),
      ('census-YM-C4-identity-intro.json',{'book':'YM','book_id':'8227-SRC-017','chapter':4,'source_path':SRC,'source_sha256':SHA,
        'scope':'PDF193–196 inclusive; every task,inline illustration and mathematical teaching figure/table.','new_items':new_items,'corrections':[],'pages':pages})]:
        (W/'tools/textbook-r5'/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
    print(len(answers),'items;',len(specs),'figures;',sum(len(r['subparts'])for r in answers),'outputs')
