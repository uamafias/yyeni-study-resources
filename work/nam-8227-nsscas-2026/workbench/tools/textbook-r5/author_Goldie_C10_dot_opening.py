"""Scalar-product opening264–267,with source methods and proof assumptions."""
import json
from author_Goldie_C10_10B import W,SRC,SHA,add as source_add,answers,new,fig,figures,corrections,ev,v,reasoning,compute,expression,equivalent,MAG,DISP
answers.clear();new.clear();figures.clear();corrections.clear()
DOT='8227:2020:M1:T7:O04:D02';ANGLE='8227:2020:M1:T7:O05:D01';PERP='8227:2020:M1:T7:O05:D02'
def add(*args,**kwargs):
 row=source_add(*args,**kwargs);row['precision_angle_check']={'source':'Examples10.9/11display angles120.5°and27.2°respectively;Example10.10is an exact zero-dot-product proof. The proof prompts use exact symbolic identities.','comparison':'Use degrees for the printed numerical keys. The between-vector angle is0..180°and requires both vectors nonzero. Do not substitute a signed polar orientation or the supplementary angle from reversing just one ray.'};return row
def norm_expr(vector):return 'sqrt('+ '+'.join(f'({z})**2'for z in vector)+')'
def dot_expr(u,vectors):return '+'.join(f'({a})*({b})'for a,b in zip(u,vectors))
def angle(label,u,vectors,key,kp,dp=1,sf=None,unit='degree',method=None):
 expr=f'acos(({dot_expr(u,vectors)})/({norm_expr(u)}*{norm_expr(vectors)}))'
 if unit=='degree':expr+='*180/pi'
 p=v(label,expr,key,kp,method or'Calculate the original vector dot product and both positive norms,then take the0..πinverse-cosine angle. Both vectors must be nonzero. Convert only at the end to the requested angular unit and compare the printed display at its recorded precision.')
 p['operation']={'kind':'rounded','operands':[expr],**({'significant_figures':sf}if sf else{'decimal_places':dp})}
 p['source_angle_vectors']=[u,vectors];p['source_angle_unit']=unit;return p
def dot(label,u,vectors,key,kp,method=None):
 p=v(label,dot_expr(u,vectors),key,kp,method or'Independently multiply corresponding signed components and sum. The result is a scalar,not a vector;the independent numeric check also uses the squared-norm identity.')
 p['source_dot_vectors']=[u,vectors];return p

p=reasoning('assumptions','The main named results are the cosine rule and Pythagoras’ theorem,in rectangular perpendicular coordinates.',
 'The source key names those two theorems. The derivation also uses the joining vectorb−a,ordinary algebraic expansion,and nonzero vector norms before division. The angle is the non-reflex angle between the two rays. Degenerate parallel/opposite cases can be treated separately or by continuity;the zero-vector case has no angle. These are author domain clarifications,not a claim the book supplies an exhaustive axiom list.',357,'matches')
add('Prompt',4,264,'As the scalar-product angle formula is derived,list the results assumed. Retain this source proof-reading task as supporting rationale rather than inventing an additional examined8227objective.',[p],teaches=[DOT,ANGLE,MAG])
add('Example',9,265,'Find the angle between(3,4)and(5,−12). The source uses dot−33andnorms5,13to obtain120.5°,an obtuse angle.',[
 angle('angle',['3','4'],['5','-12'],'120.5',265)],[ANGLE],[DOT,MAG])
p=dot('perpendicularity',['2','4'],['6','-3'],'0',266,'The actual dot product is2·6+4·(−3)=0. Both source vectors have positive norm,so the zero dot product establishes perpendicularity. A zero vector would not establish an ordinary angle or a unique perpendicular direction.')
p['check_mode']='show/prove'
add('Example',10,266,'Show(2,4)and(6,−3)are perpendicular through their zero scalar product,with the nonzero-vector condition retained.',[p],[PERP],[DOT])
p=reasoning('commutativity-proof','For real components,a·b=b·a,because each scalar component product commutes.',
 'In2D,a·b=a₁b₁+a₂b₂=b₁a₁+b₂a₂=b·a. The same termwise argument covers the third component in3D. It does not use a vector cross product or confuse scalar multiplication with a new vector-valued operation. The source key gives the2Dtermwise proof.',357,'show/prove')
p['additional_operations']={'three_component_identity':{'kind':'identity','operands':['expand((a*p+b*q+c*k)-(p*a+q*b+k*c))']}};p['additional_operation_expected']={'three_component_identity':'0'}
add('Prompt',5,266,'Prove the scalar product is commutative. The proof is supporting understanding of the operation,not another numerical angle demand.',[p],teaches=[DOT])
p=reasoning('three-dimensional-angle-proof','For nonzero real3Dvectors,cosθ=(a₁b₁+a₂b₂+a₃b₃)/(|a||b|).',
 'Apply the cosine rule toOABwithOA=a,OB=b,andAB=b−a. Squared lengths are sums of squared rectangular components. Expanding|b−a|²and subtracting from|a|²+|b|²leaves2(a₁b₁+a₂b₂+a₃b₃). Divide by2|a||b|,which is positive for the stated nonzero vectors. This is the3Dextension of the source’s2Dderivation;it uses the same learner decision rather than constituting a new recipe solely from the extra component.',357,'show/prove')
p['additional_operations']={'cosine_numerator_identity':{'kind':'identity','operands':['expand((a**2+b**2+c**2)+(p**2+q**2+k**2)-((p-a)**2+(q-b)**2+(k-c)**2)-2*(a*p+b*q+c*k))']}};p['additional_operation_expected']={'cosine_numerator_identity':'0'}
add('Prompt',6,267,'Show the scalar-product angle formula also holds for3Drectangular components. Retain the proof and its nonzero/domain conditions as supporting formula evidence.',[p],teaches=[ANGLE,DOT,MAG])
p=angle('angle-QPR',['1','4','2'],['2','5','7'],'27.2',268,method='The requested vertex isP=(1,0,−1). SubtractPfromQ=(2,4,1)andR=(3,5,6)to getPQ=(1,4,2),PR=(2,5,7). Their dot is36andnorms√21,√78. Use the two rays from the same vertex;θ=acos(36/√1638)≈27.2°. Reversing only one ray would produce the supplementary angle.')
p['additional_operations']={'original_displacements':{'kind':'identity','operands':['Tuple(Tuple(2-1,4-0,1-(-1)),Tuple(3-1,5-0,6-(-1)))']}};p['additional_operation_expected']={'original_displacements':'Tuple(Tuple(1,4,2),Tuple(2,5,7))'}
add('Example',11,267,'Find∠QPRfrom three3Dpoints. Choosing the common vertex and correctly directed joining vectors is part of the task;the worked solution and given explanatory diagram continue268.',[p],[ANGLE],[DISP,DOT,MAG],continuation=[268])

for n,page,label,note,teaches,checks in [
 (37,264,'Figure10.19 cosine-rule vector triangle','OA=a,OB=b,AB=b−afix the two rays and their included angle. The lengths are positive norms,not free vector expressions to insert as scalars into the cosine rule.',[ANGLE,DOT,MAG],[]),
 (38,265,'Scalar-product angle reference','For nonzeroa,b,the dot product equals|a||b|cosθ. The between-ray angle is0..π;the formula does not define an angle for a zero vector.',[DOT,ANGLE],[]),
 (39,265,'Perpendicularity reference','Nonzero vectors are perpendicular exactly when their dot product is0. The source explicitly states the nonzero qualification for the converse.',[PERP,DOT],[]),
 (40,266,'Scalar rather than vector product note','The dot product is a scalar quantity. The text mentions a separate vector-valued product only to say it is beyond this book;no cross-product learner demand is added to8227.',[DOT],[]),
 (41,266,'Three-component scalar-product illustration','The unprompted example(2,3,4)·(5,6,7)=56illustrates the component rule. It is reference teaching,not an independently asked learner calculation.',[DOT],[('2*5+3*6+4*7','56')]),
 (42,266,'Commutativity worked illustration','Both(2,3)·(6,7)and(6,7)·(2,3)equal33. The following prompt asks for the general reason;two agreeing numeric examples alone would not prove the general rule.',[DOT],[('Tuple(2*6+3*7,6*2+7*3)','Tuple(33,33)')])]:fig(n,page,label,note,teaches,'diagram'if n==37 else'table',checks)
for f in figures:
 f['item_id']=f['item_id'].replace(':C5:',':C10:');f['source_evidence']=ev(f['pdf_page']);f['value_level_scope_decisions']=[]
pages=[]
for page in range(264,268):
 ids=[r['item_id']for r in answers if r['source_pdf_page']==page]+[r['item_id']for r in figures if r['pdf_page']==page]
 if page==264:ids.append('8227:TB:Goldie:C10:Exercise-10B:12')
 pages.append({'pdf_page':page,'printed_page':page-14,'chapter':10,'page_status':'items enumerated','item_ids':ids,'continuation_item_ids':[],'source_evidence':ev(page),'reader':'Codex author','date':'2026-11-18','non_item_content':'All scalar-product opening prompts,examples and reference/given figures recorded.264includes the closing10B12source item. Example10.11continues268,owned by the10Ccensus.','scope_screen':'Scalar-product calculation,between-direction angles and perpendicularity are prescribed. Supporting general proofs remain separate from directly assessed numeric demands.'})
if __name__=='__main__':
 for name,data in [('answers-Goldie-C10-dot-opening.json',{'scope':'EveryPrompt4–6andExample10.9–11response,with assumptions and source precision.','items':answers}),('census-Goldie-C10-dot-opening.json',{'book':'Goldie','book_id':'8227-SRC-015','chapter':10,'source_path':SRC,'source_sha256':SHA,'scope':'Complete264–267including10B12;Example11continues268.','new_items':figures,'corrections':corrections,'pages':pages})]:
  (W/'tools/textbook-r5'/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
 for r in answers:
  for p in r['subparts']:
   if 'operation'in p:
    got=compute(p['operation']);assert equivalent(got,expression(p['printed_key_normalised'])),(r['item_id'],p['subpart'],got)
   for name,op in p.get('additional_operations',{}).items():assert equivalent(compute(op),expression(p['additional_operation_expected'][name])),(r['item_id'],name)
 print(len(answers),'items;',sum(len(r['subparts'])for r in answers),'outputs;',len(figures),'figures')
