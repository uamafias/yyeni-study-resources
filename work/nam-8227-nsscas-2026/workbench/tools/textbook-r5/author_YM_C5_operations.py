"""YM240–243: vector operation references and parallel scalar parameters."""
import json
import author_YM_C5_opening as prior
from author_YM_C5_opening import W,SRC,SHA,pp,ev,v,fig,figures,compute,expression,equivalent,NOTATION,GEOM,SCALE
prior.answers.clear();prior.new.clear();figures.clear();prior.corrections.clear()
answers=prior.answers;new=prior.new;corrections=prior.corrections
ADD='8227:2020:M1:T7:O02:D01';DISP='8227:2020:M1:T7:O03:D02'
def extra(p,name,expr,key):
 p.setdefault('additional_operations',{})[name]={'kind':'identity','operands':[expr]};p.setdefault('additional_operation_expected',{})[name]=key;return p
def add(kind,n,note,parts):
 r=prior.add(kind,n,243,note,parts,[GEOM,SCALE]);r['representation']='text';r['component_demand_ids']=[]
 r['mapping_rationale']='The asked parameters enforce one consistent scalar-multiple relation across all vector components. Positive/negative scale determines orientation; parallel does not mean same direction. Component algebra is subsidiary and not an independent new objective.'
 r['precision_angle_check']={'source':'Exact scalar parameters; original vectors are nonzero. No angle or rounding is requested by these tasks.','comparison':'Match every signed component with one common scale factor. Reversing which vector is the multiple reciprocates the nonzero factor. Distinguish scalar parameters from vectors.'}
 r['scope_check']={'status':'in-scope','basis':note,'excluded_or_qualified_parts':[],'limits_considered':[],'qualifier_applicability_note':'No unrelated calculus/modulus/inverse restriction. The original first components fix unique nonzero scalar factors.'}
 for p in parts:p.update(given_representation='text',response_format='numeric',assessed_8227_demand_ids=[GEOM,SCALE])
 return r
system='solve([10-5*k,2*a-2*b-3*k,4-(a+b)*k],(a,b,k),dict=True)[0]'
p=v('a',system+'[a]','Rational(5,2)',243,'From ORIGINAL parallel columns(5,3,a+b)and(10,2a−2b,4),one common multiplierk satisfies all3components. First k2,then a−b3 and a+b2,so a5/2. The variablesa,b are scalar entries,despite the header calling them vectors.')
p2=v('b',system+'[b]','-Rational(1,2)',243,'Solve the same correlated3component system,retaining the common k2. Then b−1/2. The native working correctly prints4=2a+2b; the suspected missing2was a false low-resolution lead.')
extra(p2,'original-columns','Tuple(5,3,Rational(5,2)-Rational(1,2),10,2*Rational(5,2)-2*(-Rational(1,2)),4)','Tuple(5,3,2,10,6,4)')
r=add('Example',6,'Find scalar entries a,b making(5,3,a+b)and(10,2a−2b,4)parallel; common factor2gives a5/2,b−1/2.',[p,p2]);r['source_label_warning']='The original header says find the vectors a and b,but these are scalar entries. All printed algebra/final numeric values are correct. A reversed multiple equation also works with a reciprocal scalar,not the same numeric k.'
p=v('x','6/(-3)','-2',616,'Original(x,6,y)=h(1,−3,5). The middle component gives h−2; first component is x=h=−2.')
p2=v('y','5*(6/(-3))','-10',616,'Use the SAME original scalar h−2 in the third component y=5h. Do not choose scales independently per component.')
add('Try-Now-6',1,'Given(x,6,y)=h(1,−3,5),find x−2,y−10 from common factorh−2; the scalar h itself is not separately asked.',[p,p2])
p=v('q','6*((-4)/2)','12',616,'Original AB=(2,−3,6),CD=(−4,6,q). The first component gives factor−2 and the second independently confirms6/(−3)=−2. Therefore q=−12. Printed+12breaks the common scalar relation; parallel permits the opposite orientation.')
p['author_expected_normalised']='-12';extra(p,'correct-cross-product','Tuple((-3)*(-12)-6*6,6*(-4)-2*(-12),2*6-(-3)*(-4))','Tuple(0,0,0)');extra(p,'printed-cross-product','Tuple((-3)*12-6*6,6*(-4)-2*12,2*6-(-3)*(-4))','Tuple(-72,-48,0)')
add('Try-Now-6',2,'Find q for AB=(2,−3,6)parallelCD=(−4,6,q); opposite-direction factor−2requires q−12,not printed+12.',[p])

refs=[
 (24,240,'Head-to-tail resultant grid panels','The displayed vectorsa=(4,2),b=(−2,3)join QtoR after PtoQ; resultant PR=(2,5). Translate a free vector without changing its length/direction before joining arrows.',[ADD,GEOM],'graph',[('Tuple(4+(-2),2+3)','Tuple(2,5)')]),
 (25,240,'Named-arrow addition connection','The notation panel links terminalQofPQtoinitialQofQR,givingPQ+QR=PR. The shared point is essential for this chained-route statement; it is not arbitrary letter cancellation in unrelated arrows.',[NOTATION,DISP,ADD],'diagram',[]),
 (26,240,'Component-addition rule and example','Add corresponding components,not magnitudes. The source columns(4,2)+(−2,3)=(2,5)match the combined grid and preserve signed horizontal motion.',[ADD],'table',[('Tuple(4-2,2+3)','Tuple(2,5)')]),
 (27,240,'Same endpoints and different routes note','Different polygonal routes with the SAME start/end have the same displacement resultant. They can have different travelled distances; route length is not displacement magnitude.',[DISP,GEOM],'table',[]),
 (28,241,'Opposite vectors and return bearings','A10km displacement on bearing070degrees reverses to an equal-magnitude10km displacement on bearing250degrees. Bearings are clockwise from north; this is supporting orientation,not a scalar-product angle assessment.',[DISP,GEOM],'diagram',[('(70+180)%360','250')]),
 (29,241,'Subtraction and reversed-vector grids','Subtractbbyadding−b. For sourcea=(4,2),b=(−2,3),the result is(6,−1); reverse BOTH components ofb,not only its horizontal component.',[ADD,GEOM],'graph',[('Tuple(4-(-2),2-3)','Tuple(6,-1)')]),
 (30,241,'Component-subtraction rule','The exact columns(4,2)−(−2,3)=(6,−1)agree with the reversal construction. a−b differs fromb−a by an overall sign.',[ADD],'table',[('Tuple(4-(-2),2-3)','Tuple(6,-1)')]),
 (31,242,'Scalar multiplication grid and columns','Factor2takes(4,2)to(8,4)in the same direction; scale every corresponding component. A negative factor would reverse direction and a zero factor would give a zero vector.',[SCALE,GEOM],'graph',[('Tuple(2*4,2*2)','Tuple(8,4)')]),
 (32,242,'Scalar division grid and columns','Dividing(4,2)by2is multiplying by1/2,giving(2,1). Division requires a nonzero scalar; the displayed half-size arrow keeps direction.',[SCALE,GEOM],'graph',[('Tuple(4/2,2/2)','Tuple(2,1)')]),
 (33,243,'Positive/negative parallel multiples reference','Vectors(9,−6,12)and(−12,8,−16)are respectively3and−4times(3,−2,4). Both are parallel; only the positive multiple has the same orientation. These examples do not license independent per-component factors.',[SCALE,GEOM],'table',[('Tuple(3*3,3*(-2),3*4,-4*3,-4*(-2),-4*4)','Tuple(9,-6,12,-12,8,-16)')])]
for n,page,label,note,teaches,rep,checks in refs:
 fig(n,page,label,note,teaches,rep,checks,None)
 f=figures[-1];f['item_id']=f['item_id'].replace('Goldie:C5:','YM:C5:');f.update(printed_page=pp(page),source_evidence=ev(page),value_level_scope_decisions=[],item_kind='teaching-figure')
 f['mathematical_feature_review']['method']='Read original arrowhead/tail,component signs,bearing reference direction and matching grid displacements. Independently recompute printed examples; perspective or grid reading remains a manual source check.'
pages=[{'pdf_page':page,'printed_page':pp(page),'chapter':5,'page_status':'items enumerated','item_ids':[r['item_id']for r in answers if r['source_pdf_page']==page]+[r['item_id']for r in figures if r['pdf_page']==page],'continuation_item_ids':[],'source_evidence':ev(page),'reader':'Codex author','date':'2026-11-19','non_item_content':'All240–242operation/bearing/scaling teaching panels and243parallel reference,Example6/ Try6Q1/2 outputs are recorded. Native243clears the suspected missing2in4=2a+2b; only the scalar/vector header terminology is defective there. Try6Q2key+12is independently disproved by the signed multiple and cross product.','scope_screen':'Vector operations and common-multiple geometry are prescribed. The bearing illustration is supporting orientation,not new scalar-product angle coverage. Distinguish pure teaching examples from explicit asked outputs.'}for page in range(240,244)]

if __name__=='__main__':
 for name,data in [('answers-YM-C5-operations.json',{'scope':'Every240–243 explicit learner output and supporting operation panel.','items':answers}),('census-YM-C5-operations.json',{'book':'YM','book_id':'8227-SRC-017','chapter':5,'source_path':SRC,'source_sha256':SHA,'scope':'Complete240–243 page census.','new_items':new+figures,'corrections':corrections,'pages':pages})]:
  (W/'tools/textbook-r5'/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
 for row in answers:
  for p in row['subparts']:
   if 'operation'in p:assert equivalent(compute(p['operation']),expression(p.get('author_expected_normalised',p['printed_key_normalised']))),(row['item_id'],p['subpart'])
   for name,op in p.get('additional_operations',{}).items():assert equivalent(compute(op),expression(p['additional_operation_expected'][name])),(row['item_id'],p['subpart'],name)
 print(len(answers),'items;',sum(len(r['subparts'])for r in answers),'responses;',len(figures),'references/assets;',len(pages),'pages')
