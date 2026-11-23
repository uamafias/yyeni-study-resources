"""Rendered-source readings and fixed answers for YM PDF215–218."""
import hashlib,json
from pathlib import Path
from author_YM_C4_trig_graphs import value
from author_YM_C4_equations import eq
W=Path(__file__).resolve().parents[2];ROOT=W.parents[2]
SRC='Y=mc as textbook.pdf';SHA='0b44ad3b67b1ea3de90cba780382d77deef347fae683cf6e28677f36c17a724f'
PRINCIPAL='8227:2020:M1:T6:O04:D01';EXACT='8227:2020:M1:T6:O03:D01'
INVERSE='8227:2020:M1:T3:O03:D02';RANGE='8227:2020:M1:T3:O02:D02';REC='8227:2020:M2:T3:O01:D01'
BND='8227:2020:M1:T6:O06:D01';ALL='8227:2020:M1:T6:O06:D02'
def ev(page):
    if page==613:name='YM-key-Try53-units'
    elif page<=216:name='YM-C4-213'
    else:name='YM-C4-217'
    p=W/f'checks/r5/textbooks/{name}.png'
    return {'path':str(p.relative_to(ROOT)),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
def principal(label,expr,key,kp):
    return value(label,expr,key,kp,'Evaluate the original inverse-function input on its standard principal branch. Use the exact reference triangle and the branch sign/quadrant; convert the result to the requested unit without generating other periodic representatives.')
answers=[]
def add(kind,n,page,note,parts,direct,components=None):
    for p in parts:
        kp=p.pop('key_page_override',page)
        # The Try54 key lies below the tightly cropped Try52/Try53 evidence.
        ke=ev(kp)
        if kind=='Try-Now-54':
            image=W/'checks/r5/textbooks/YM-key-612-613-full.png'
            ke={'path':str(image.relative_to(ROOT)),'sha256':hashlib.sha256(image.read_bytes()).hexdigest()}
        p.update(source_pdf_page=page,source_evidence=ev(page),answer_pdf_page=kp,
          answer_printed_page='A'+str(kp-586)if kp>=602 else kp-12,key_evidence=ke,review_date='2026-11-18')
    row={'item_id':f'8227:TB:YM:C4:{kind}:{n}','source_pdf_page':page,'notes':note,
      'assessed_8227_demand_ids':direct,'component_demand_ids':components or[],
      'mapping_rationale':'Use the specified inverse-function principal branch,not the complete periodic solution set. Exact special-angle evaluation is directly assessed only when requested. Supplied inverse notation is distinct from constructing a new inverse formula. Algebra inside an inverse function is a component unless separately requested.',
      'value_level_scope_decisions':[{'rule_id':'8227:QUAL08','status':'within','quoted_value':note,
        'reason':'The supporting principal branch is retained:asin output[−π/2,π/2],acos[0,π],atan(−π/2,π/2),converted to degrees only where requested. This does not add a directly assessed inverse-construction objective.'}],
      'principal_branch_check':{'asin':'Input[−1,1];output[−π/2,π/2].','acos':'Input[−1,1];output[0,π].',
        'atan':'InputR;output(−π/2,π/2),with both finite-angle endpoints excluded.',
        'source_limit':'The printed closed tangent endpoints and mislabelled inverse domains are source defects,not accepted branch definitions.'},
      'exam_style':False,'exam_style_basis':'Ordinary Example/TryNow or unnumbered teaching illustration; no examination attribution.',
      'precision_angle_check':{'source':'Preserve each actual request for degrees,radians,exact special values or3decimal places.',
        'comparison':'A radian key for a degree request is an answer-format conflict even when it denotes the correct physical angle. Literal key values/units remain recorded separately from a unit-normalised comparison.'},
      'expected_subpart_labels':[p['subpart']for p in parts],'subparts':parts}
    answers.append(row);return row

illustrations=[]
for n,expr,key,note,dp in[
 (1,'asin(1/2)*180/pi','30','The unnumbered calculator illustration gives the single principal value asin(.5)=30°.',None),
 (2,'acos(-2/5)*180/pi','113.6','The unnumbered calculator illustration gives acos(−.4)=113.6°,within the cosine principal interval.',1),
 (3,'atan(-2)*180/pi','-63.4','The unnumbered calculator illustration gives atan(−2)=−63.4°,a clockwise principal angle.',1)]:
    p=value('principal-value',expr,key,215,'Independently evaluate the specified inverse function on its principal branch. Convert to degrees and apply the actual displayed decimal precision only at the end.')
    if dp is not None:p['operation']={'kind':'rounded','operands':[expr],'decimal_places':dp}
    row=add('Illustration-principal-value',n,215,note,[p],[])
    row['mapping_rationale']='This is an unprompted teaching illustration,not an additional assigned learner question; it does not earn directly assessed coverage.'
    illustrations.append({'item_id':row['item_id'],'item_kind':'worked-illustration','exercise':'Unnumbered principal-value illustration','item_number':str(n),
      'pdf_page':215,'printed_page':203,'notes':note,'assessed_8227_demand_ids':[],'component_demand_ids':[],
      'representation':'text','source_evidence':ev(215),'learner_display':False,
      'evidence_role':'prerequisite/supporting inline illustration; no directly assessed coverage'})
p=value('principal-value','acos(-sqrt(3)/2)*180/pi','150',216,'The negative cosine ratio has reference30°;restrict to0°..180°and choose150°,not its other periodic representatives.')
p.update(question_formula_normalised='acos(-sqrt(3)/2)',printed_key_formula_normalised='acos(sqrt(3)/2)',
  source_formula_warning='The final Hence line drops the original negative sign. Its numerical150°matches the asked negative input,but not the positive input printed in that last line.')
add('Example',52,216,'Without a calculator,find acos(−√3/2)in degrees. The intended answer150°is correct;the source final line mistakenly changes the input to+√3/2.',[p],[PRINCIPAL,EXACT])
add('Try-Now',52,217,'Without a calculator,give asin(−1/2),atan√3 andacos(1/2)in degrees. The finite outputs are−30°,60°,60°;the accompanying branch reminder has separate label/endpoint defects.',[
 principal('a','asin(-1/2)*180/pi','-30',613),principal('b','atan(sqrt(3))*180/pi','60',613),principal('c','acos(1/2)*180/pi','60',613)],[PRINCIPAL,EXACT])
p=value('b','atan(1)','pi/4',217,'Positive tangent1on the principal interval givesπ/4. The final printed argument must still be1,not the copied negative surd.')
p.update(question_formula_normalised='atan(1)',printed_key_formula_normalised='atan(-1/sqrt(2))',
  source_formula_warning='The final Hence line printsatan(−1/√2)=π/4although the question and preceding work correctly useatan1.')
add('Example',53,217,'Write principal values asin(−1/√2)andatan1in terms ofπ,without a calculator. The intended answers−π/4andπ/4are correct;part(b)has a copied wrong input in its final line.',[
 principal('a','asin(-1/sqrt(2))','-pi/4',217),p],[PRINCIPAL,EXACT])
parts=[]
for label,expr,degrees,radians in[
 ('a','acos(-1/sqrt(2))*180/pi','135','3*pi/4'),
 ('b','atan(-1)*180/pi','-45','-pi/4'),('c','asin(1/sqrt(2))*180/pi','45','pi/4')]:
    p=value(label,expr,degrees,613,'Independently evaluate the principal angle and return degrees as explicitly requested. Convert the separately recorded radian key only to compare physical angles; preserve its wrong requested unit as a separate failure.')
    p.update(units='degree',printed_key_units='radian',printed_key_value_original=radians,
      key_normalisation_basis='Printed radian quantity converted to degrees solely for numerical comparison; the literal radian expression and format mismatch remain explicit.')
    parts.append(p)
row=add('Try-Now',53,217,'The prompt explicitly asks degrees for acos(−1/√2),atan(−1),asin(1/√2);the key instead gives3π/4,−π/4,π/4. Correct degree answers are135°,−45°,45°. Its(a)quadrant label is also wrong.',parts,[PRINCIPAL,EXACT])
row['source_label_warning']='Part(a)key says Quad4for3π/4;that angle is quadrantII.'
p={'subpart':'a','operation':{'kind':'real-roots','operands':['x**2-1-sin(pi/3)']},
 'printed_key_approximate_values':['1.366','-1.366'],'key_decimal_places':3,'key_page_override':218,
 'original_equation_residual':'asin(x**2-1)-pi/3',
 'method':'π/3lies in the arcsine principal range,so x²−1=sin(π/3)=√3/2. Retain both real square-root signs,and substitute them into the original inverse equation; then round each root to3decimal places.'}
add('Example',54,218,'(a)Solve asin(x²−1)=π/3to3decimal places,retaining both real signs. (b)Solve sin(2θ+π/3)=1/2on0≤θ≤π,in terms ofπ;the shifted argument window excludes the firstπ/6ray.',[
 p,eq('b','sin','2*x+pi/3','1/2','FiniteSet(pi/4,11*pi/12)',unit='radian',hi='pi')],[PRINCIPAL,BND,ALL])
add('Try-Now-54',1,218,'Solve asin(4x⁴+x²)=π/6. The inverse range makes this4x⁴+x²=1/2;only real rootsx=±1/2satisfy the original inverse equation.',[
 {'subpart':'roots','operation':{'kind':'real-roots','operands':['4*x**4+x**2-sin(pi/6)']},
  'printed_key_normalised':'FiniteSet(-1/2,1/2)','key_page_override':613,
  'original_equation_residual':'asin(4*x**4+x**2)-pi/6',
  'method':'Convert the principal inverse statement to4x⁴+x²=1/2. Factor in u=x²:8u²+2u−1=(4u−1)(2u+1). Rejectu=−1/2,retainu=1/4andboth real signs;substitute into the original arcsine equation.'}],[PRINCIPAL])

specs=[
 (215,'Restricted sine principal branch','Sine is restricted to[−90°,90°],with range[−1,1],both endpoints included. The graph labels the abscissa asin(a).',None,None,[PRINCIPAL,INVERSE],'graph'),
 (215,'Restricted cosine principal branch','Cosine on[0°,180°]is decreasing with range[−1,1]. Its abscissa is incorrectly labelledasin(b),which should beacos(b).',None,None,[PRINCIPAL,INVERSE],'graph'),
 (215,'Restricted tangent principal branch','The increasing tangent branch has poles at±90°andrangeR. The source incorrectly includes its endpoints andlabels an abscissaasin(c)insteadofatan(c).',None,None,[PRINCIPAL,INVERSE],'graph'),
 (215,'Inverse notation versus reciprocal','The reminder distinguishes asin(x)from(sinx)⁻¹=1/sinx=cosecx. These have different meanings and their respective input/denominator domains still apply.',None,None,[PRINCIPAL,REC],'table'),
 (216,'Arcsine graph and domain/range','Arcsine has domain[−1,1]anddegree range[−90°,90°],including both endpoints;it is increasing.',None,None,[PRINCIPAL,INVERSE,RANGE],'graph'),
 (216,'Arccosine graph and domain/range','Arccosine has domain[−1,1]anddegree range[0°,180°];it is decreasing.',None,None,[PRINCIPAL,INVERSE,RANGE],'graph'),
 (216,'Arctangent graph and domain/range','Arctangent has domainR andopen degree range(−90°,90°). The graph shows horizontal asymptotes,but the printed range uses closed inequalities.',None,None,[PRINCIPAL,INVERSE,RANGE],'graph'),
 (216,'Example52 special triangle','A1,√3,2triangle gives cos30°=√3/2. That caption is correct;the negative original cosine ratio is handled by choosing quadrantII.','Example:52',None,[EXACT],'diagram'),
 (216,'Example52 principal cosine rays','Negative cosine normally permitsII/III,but the principal0°..180°interval keeps only the150°ray.','Example:52',None,[PRINCIPAL,EXACT],'diagram'),
 (217,'Try52 principal-interval reminder','The reminder calls angle intervals Domains of the Inverse functions;they are principal output ranges(or restricted original-function input domains). Its tangent endpoints are also printed closed.','Try-Now:52',None,[PRINCIPAL,INVERSE],'table'),
 (217,'Example53a special triangle','An isosceles1,1,√2triangle gives sin(π/4)=1/√2;the original input is negative.','Example:53','a',[EXACT],'diagram'),
 (217,'Example53a clockwise principal sine ray','The negative sine principal value is−π/4in quadrantIV;the sine range endpoints±π/2are included.','Example:53','a',[PRINCIPAL],'diagram'),
 (217,'Example53b special triangle','An isosceles1,1,√2triangle gives tan(π/4)=1,matching the original requested input1.','Example:53','b',[EXACT],'diagram'),
 (217,'Example53b principal tangent ray','Positive tangent1keeps quadrantIunder the principal branch. The source again prints closed±π/2tangent endpoints,which must be open.','Example:53','b',[PRINCIPAL],'diagram'),
 (218,'Example54a exact sine triangle','The1,√3,2triangle gives sin(π/3)=√3/2before recovering both algebraic x signs.','Example:54','a',[EXACT,PRINCIPAL],'diagram'),
 (218,'Example54b shifted argument rays','The argument2θ+π/3lies in[π/3,7π/3]. Of the positive-sine rays,the valid arguments are5π/6and13π/6,leading toθ=π/4and11π/12.','Example:54','b',[BND,ALL],'diagram')]
figures=[]
for n,(page,label,note,parent,part,teaches,rep)in enumerate(specs,151):
    branch_issue=n in[153,157,160,164]
    figures.append({'item_id':f'8227:TB:YM:C4:Teaching-figure:{n}','item_kind':'teaching-figure','exercise':'Teaching figure','item_number':str(n),
      'pdf_page':page,'printed_page':page-12,'source_label':label,'parent_item_id':f'8227:TB:YM:C4:{parent}'if parent else None,'parent_subpart':part,
      'notes':note,'what_it_shows':note,'assessed_8227_demand_ids':[],'component_demand_ids':[],'teaches_8227_demand_ids':teaches,
      'representation':rep,'source_evidence':ev(page),'learner_display':False,
      'value_level_scope_decisions':[{'rule_id':'8227:QUAL08','status':'outside'if branch_issue else'within',
        'quoted_value':'Printed tangent branch−90°≤x≤90°or−π/2≤x≤π/2;arctangent range also printed closed.'if branch_issue else note,
        'reason':'The named tangent endpoints are undefined/unattainable;the intended corrected principal branch is open. This is a source mathematical defect,not an added syllabus demand.'if branch_issue else'The stated fixed principal branch or exact reference ray is retained;teaching links do not create an assessed inverse-construction task.'}],
      'value_level_scope_review_status_r5':'author actual branch endpoints,labels andangle units read2026-11-18; independent check pending',
      'exam_representation_check':{'status':'final cross-book/examination comparison pending','examination_part_ids':[],
        'relation':'Teaching/solution representation;no claim that every inverse graph is an observed8227task.'},
      'mathematical_feature_review':{'status':'author endpoint,monotonicity andlimit reasoning complete;independent acceptance pending',
        'method':'Sine/cosine endpoint values andmonotonic principal restrictions establish their inverses. Tangent/atan limits establish open endpoints. Exact parent values/rays are independently recomputed. Printed discrepancies remain separately registered,not silently accepted.'}})
    if n in[154,158,161,163,165]:
        figures[-1]['value_level_scope_decisions']=[{'rule_id':'8227:QUAL08','status':'not applicable','quoted_value':note,
          'reason':'A reciprocal-notation reminder or exact reference triangle,not construction of a one-to-one inverse branch.'}]
    if n==166:
        figures[-1]['value_level_scope_decisions']=[{'rule_id':'8227:QUAL03','status':'within',
          'quoted_value':'sin(2θ+π/3)=1/2;0≤θ≤π',
          'reason':'Actual argument multiplier2;its whole shifted finite interval is retained.'}]
pages=[]
for page in range(215,219):
    pages.append({'pdf_page':page,'printed_page':page-12,'chapter':4,'page_status':'items enumerated',
      'item_ids':[r['item_id']for r in answers if r['source_pdf_page']==page]+[r['item_id']for r in figures if r['pdf_page']==page],
      'continuation_item_ids':[],'source_evidence':ev(page),
      'non_item_content':'All formal tasks,three unnumbered calculator illustrations,and mathematical teaching figures/tables enumerated. Try54Q2/Q3start separately onPDF219andremain pending.',
      'reader':'Codex author','date':'2026-11-18'})
if __name__=='__main__':
    import sympy as sp
    x=sp.Symbol('x',real=True)
    assert sp.sin(-sp.pi/2)==-1 and sp.sin(sp.pi/2)==1 and sp.cos(0)==1 and sp.cos(sp.pi)==-1
    assert sp.limit(sp.tan(x),x,-sp.pi/2,dir='+')==-sp.oo
    assert sp.limit(sp.tan(x),x,sp.pi/2,dir='-')==sp.oo
    assert sp.limit(sp.atan(x),x,-sp.oo)==-sp.pi/2 and sp.limit(sp.atan(x),x,sp.oo)==sp.pi/2
    for name,data in[
      ('answers-YM-C4-principal-values.json',{'scope':'Every formal task/output and3unnumbered principal-value illustrations onPDF215–218;literal printed formula/unit defects preserved.','items':answers}),
      ('census-YM-C4-principal-values.json',{'book':'YM','book_id':'8227-SRC-017','chapter':4,'source_path':SRC,'source_sha256':SHA,
        'scope':'PDF215–218;allformal tasks,inline illustrations andseparate mathematical graphs/diagrams/tables.','new_items':figures+illustrations,'corrections':[],'pages':pages})]:
        (W/'tools/textbook-r5'/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
    print(len(answers),'items;',len(figures),'figures;',sum(len(r['subparts'])for r in answers),'outputs')
