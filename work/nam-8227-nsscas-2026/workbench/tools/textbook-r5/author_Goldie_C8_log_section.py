"""Scope/answer records205–207; supplied derivatives differ from new methods."""
import json
from author_Goldie_C8_opening import W,SRC,SHA,add,answers,new,ev,fig,figures,value,reasoning,compute,expression,equivalent,primitive_agrees,AREA,DEF
answers.clear();new.clear();figures.clear()
EXPINT='8227:2020:M2:T5:O01:D01';REVERSE='8227:2020:M2:T5:O01:D03';PRODUCT='8227:2020:M2:T4:O02:D01'
STATIONARY='8227:2020:M1:T8:O04:D01';CLASSIFY='8227:2020:M1:T8:O04:D02';SKETCH='8227:2020:M1:T3:O05:D01'
p=value('ii','0','log(3)',351,
 'Factor the original denominatorx²−6x+9=(x−3)². The quotient reduces to1/(x−3),with the original exclusionx=3retained. Bounds4and6lie in one positive continuous component,so the proper integral isln3. No partial fractions or general substitution is needed.')
p['operation']={'kind':'proper-definite-integral','operands':['(x-3)/(x**2-6*x+9)','4','6']}
p['additional_operations']={'cancellation':{'kind':'identity','operands':['cancel((x-3)/(x**2-6*x+9))']}};p['additional_operation_expected']={'cancellation':'1/(x-3)'}
row=add('Exercise-8C',2,207,'Only(ii):evaluate∫₄⁶(x−3)/(x²−6x+9)dxby cancelling a common factor. Part(i)has a nonlinear exponential integral outside the listed forms.',[p],[DEF],[EXPINT])
row['scope_check'].update(status='in-scope-parts-only',excluded_or_qualified_parts=['i:nonlinear exponential integration;not a listed affine-exponent form.'])
row['source_interpretation']={'boundary_correction':'The earlier broad note excluded all8C2. Part(ii)is prescribed after elementary cancellation to a reciprocal-linear form.'}
f='(x+3)*exp(-x)'
p=value('i-derivative',f'diff({f},x)','-(x+2)*exp(-x)',351,'Use the product rule on the actual polynomial/exponential product. The derivative is−(x+2)e^(−x),with the sign carried into the next part.')
p2=value('ii-primitive','0','-(x+3)*exp(-x)',351,'The preceding requested derivative is the negative of the new integrand(x+2)/e^x. Reverse that supplied derivative to get−(x+3)e^(−x)+C. This scaffold requires no independently selected integration-by-parts method.')
p2['operation']={'kind':'real-elementary-antiderivative','operands':['(x+2)/exp(x)']};p2['answer_equivalence']='up-to-additive-constant'
p2['source_dependency_edges']=[{'from':'i','type':'cue','cue':'Hence','role':'Use the derivative established in part(i),with a negative sign;no official follow-through award is inferred.'}]
p3=value('iii-point',f'Tuple(solve(diff({f},x),x)[0],({f}).subs(x,solve(diff({f},x),x)[0]))','Tuple(-2,exp(2))',351,'Set the derivative to0. Its exponential factor is positive for every realx,so the sole stationary input is−2. Substitute into the original function to get ordinatee².')
p4=value('iv-second-derivative',f'diff({f},x,2).subs(x,solve(diff({f},x),x)[0])','-exp(2)',351,'Differentiate the actual function a second time and evaluate at the stationary point from(iii). The value−e²is strictly negative.')
p4['source_dependency_edges']=[{'from':'iii','type':'cue','cue':'at the pointS','role':'Evaluate at the stationary input established in(iii).'}]
p5=reasoning('iv-classification','S=(−2,e²)is a maximum.','The second derivative atS is−e²<0and the function is smooth on a neighbourhood ofS. Its first derivative also changes from positive to negative there,independently confirming the classification.',351,'matches')
p5['additional_operations']={'first_derivative_signs':{'kind':'identity','operands':[f'Tuple(sign(diff({f},x).subs(x,-3)),sign(diff({f},x).subs(x,-1)))']}};p5['additional_operation_expected']={'first_derivative_signs':'Tuple(1,-1)'}
p6=reasoning('v-transformation','Foru=e^x>0,lnu=xanddu=e^xdx,so((2+lnu)/u²)du=((2+x)/e^x)dx.',
 'Transform the differential as well as the integrand. This part explicitly requires a general substitution,which remains outside prescribed methods. Its displayed target relationship is nevertheless supplied in the question and can be used conditionally in the final part.',351,'show/prove')
p6['additional_operations']={'transformed_integrand':{'kind':'identity','operands':['((2+x)/exp(2*x))*exp(x)-(2+x)/exp(x)']}};p6['additional_operation_expected']={'transformed_integrand':'0'}
p7=value('vi-integral','0','3-4/exp(1)',351,'Use the displayed conversion from(v)withu=1,e corresponding tox=0,1. The primitive already established in(ii)gives[−(x+3)e^(−x)]₀¹=3−4/e. Independent direct evaluation of the original uintegral verifies the value. The required proof technique in(v)is not silently treated as prescribed.')
p7['operation']={'kind':'proper-definite-integral','operands':['(2+log(x))/x**2','1','E']}
p7['additional_operations']={'given_target_integral':{'kind':'proper-definite-integral','operands':['(2+x)/exp(x)','0','1']}};p7['additional_operation_expected']={'given_target_integral':'3-4/exp(1)'}
p7['source_dependency_edges']=[{'from':'ii','type':'cue','cue':'Hence','role':'Use the previously recovered primitive.'},{'from':'v','type':'cue','cue':'Hence','role':'The transformation target is printed in(v). Treat its use separately from the additional requirement to prove it by substitution.'}]
row=add('Exercise-8C',5,207,'For y=(x+3)e^(−x),differentiate,hence recover an integral,find/classify the stationary point,show the prescribedu=e^xconversion,and hence evaluate a definite integral. Keep the extra required method in(v)separate from the other parts.',[p,p2,p3,p4,p5,p6,p7],[PRODUCT,REVERSE,STATIONARY,CLASSIFY,DEF])
row['scope_check'].update(status='in-scope-parts-only',excluded_or_qualified_parts=['v:mandatory general substitution proof is outside prescribed integration methods.','vi:retained conditionally using the displayed conversion target in(v)and the primitive from(ii);the whole connected source item is not an unqualified8227task.'])
row['value_level_scope_decisions'][0].update(status='outside',parts=['v-required-method'],quoted_value='Show that the substitutionu=e^xconverts∫(2+lnu)/u²duinto∫(2+x)/e^x dx.',reason='The mandatory proof method in(v)is additional. Other requested derivatives,stationarity,reverse recognition and the given-result evaluation remain separately identified.')
row['direct_demand_aspects']=[{'demand_id':PRODUCT,'assessed_facet':'i'},{'demand_id':REVERSE,'assessed_facet':'iiuses the supplied derivative'},{'demand_id':STATIONARY,'assessed_facet':'iii'},{'demand_id':CLASSIFY,'assessed_facet':'iv'},{'demand_id':DEF,'assessed_facet':'vi,conditional on the displayed conversion target;not the general-method proof in(v)'}]
p=reasoning('i-sketch','On0≤x≤2,draw an increasing,concave-down curve from(0,1/2)to(2,e²/(e²+1));it stays below1.',
 'The denominator is positive. The derivativee^x/(e^x+1)²is positive;the second derivativee^x(1−e^x)/(e^x+1)³is negative for0<x≤2. The source key sketch agrees at the start and in shape and shows the full formula’s asymptotey=1. The requested finite viewport still ends at2;its endpoint ordinate is independently derived,not a printed numeric given.',351,'sketch')
p['additional_operations']={'endpoints':{'kind':'identity','operands':['Tuple((exp(x)/(exp(x)+1)).subs(x,0),(exp(x)/(exp(x)+1)).subs(x,2))']},'first_derivative_identity':{'kind':'identity','operands':['diff(exp(x)/(exp(x)+1),x)-exp(x)/(exp(x)+1)**2']},'second_derivative_identity':{'kind':'identity','operands':['diff(exp(x)/(exp(x)+1),x,2)-exp(x)*(1-exp(x))/(exp(x)+1)**3']}}
p['additional_operation_expected']={'endpoints':'Tuple(1/2,exp(2)/(exp(2)+1))','first_derivative_identity':'0','second_derivative_identity':'0'}
p2=value('ii-area','0','log((exp(2)+1)/2)',351,'For internal extension QA,the positive region under the sigmoid on[0,2]has exact area ln(1+e²)−ln2. The nonlinear reciprocal/exponential composition is outside the listed affine integration forms;the sketch in(i)does not turn this into a prescribed integral.')
p2['operation']={'kind':'proper-definite-integral','operands':['exp(x)/(exp(x)+1)','0','2']}
p2['additional_operations']={'displayed_approximation':{'kind':'rounded','operands':['log((exp(2)+1)/2)'],'decimal_places':3}};p2['additional_operation_expected']={'displayed_approximation':'1.434'}
p3=value('iii-integral','0','log((exp(2)+1)/2)',351,'For internal extension QA,evaluate the original proper integral∫₁ᵉ2t/(t²+1)dt. Its primitive ln(t²+1)gives the same exact endpoint expression. This nonlinear-log recognition is not a listed reciprocal-linear integral.')
p3['operation']={'kind':'proper-definite-integral','operands':['2*x/(x**2+1)','1','E']}
p4=reasoning('iv-comparison','The exact values in(ii)and(iii)are equal.',
 'The source relatione^x=t²withpositivet givesx=2ln t,dx=2dt/tand bounds0,2→1,e. Substituting intoe^x/(e^x+1)dxgives2t/(t²+1)dt. Equality can also be seen from the independently evaluated endpoint expressions. The general substitution explanation is supporting extension,not a newly required method.',351,'matches')
p4['additional_operations']={'integrand_relation':{'kind':'identity','operands':['(x**2/(x**2+1))*(2/x)-2*x/(x**2+1)']}};p4['additional_operation_expected']={'integrand_relation':'0'}
row=add('Exercise-8C',6,207,'Sketch y=e^x/(e^x+1)on0..2;then evaluate its area,a companion∫₁ᵉ2t/(t²+1)dt,and explain equality. Only the sketch is directly prescribed here;the nonlinear integrals/comparison are audited as supporting extension.',[p,p2,p3,p4],[SKETCH],teaches=[REVERSE])
row['scope_check'].update(status='in-scope-parts-only',excluded_or_qualified_parts=['iiandiii:nonlinear logarithmic primitives beyond listed affine forms.','iv:comparison of those extension integrals;source offers an additional general substitution explanation.'])
row['direct_demand_aspects']=[{'demand_id':SKETCH,'assessed_facet':'i:finite specified domain only;do not count the whole connected integral task as prescribed.'}]
row['sketch_response_required']=True

for n,page,label,note,teaches,checks in [
 (13,205,'Figure8.5 nonlinear-log area','The given curve2x/(x²+3)has no real pole,passes0,and is positive on the shaded interval[1,5]. Its maximum positive ordinate occurs atx=√3. The original integral is a nonlinear-log extension;the figure remains supporting area/graph evidence.',[AREA,SKETCH],[('Tuple((2*x/(x**2+3)).subs(x,0),(2*x/(x**2+3)).subs(x,1),(2*x/(x**2+3)).subs(x,5))','Tuple(0,1/2,5/14)')]),
 (14,206,'General logarithmic reverse-derivative reference','The reference∫f′(x)/f(x)dx=ln|f(x)|+Cis valid on real components wheref≠0. Its affine subcases are prescribed;the surrounding degree5/6and nonlinear examples do not automatically broaden8227scope.',[REVERSE],[('diff(log(x**2+3),x)','2*x/(x**2+3)')]),
 (15,207,'Exercise8C3 odd nonlinear-exponential graph','The givenx e^(x²)curve has a below-axis region[−1,0]and above-axis region[0,2]. They are not symmetric intervals. The original area integrals are nonlinear-exponential extension,but the region/sign representation is retained.',[AREA],[('(x*exp(x**2)).subs(x,-x)+x*exp(x**2)','0')]),
 (16,207,'Exercise8C4 three-branch rational graph','The given(x+2)/(x²+4x+3)has poles−3and−1and zero−2. Shaded[−5,−4]is below the axis;[1,2]is above. The original integration needs an additional decomposition/nonlinear-log method;the graph itself remains useful internal representation evidence.',[AREA,SKETCH],[('Tuple((x+2)/(x**2+4*x+3)).subs(x,-2)','Tuple(0)'),('Tuple(((x+2)/(x**2+4*x+3)).subs(x,-5),((x+2)/(x**2+4*x+3)).subs(x,-4),((x+2)/(x**2+4*x+3)).subs(x,1),((x+2)/(x**2+4*x+3)).subs(x,2))','Tuple(-3/8,-2/3,3/8,4/15)')])]:
 fig(n,page,label,note,teaches,'table'if n==14 else'graph',checks)
for f in figures:
 f['item_id']=f['item_id'].replace(':C5:',':C8:');f['source_evidence']=ev(f['pdf_page']);f['value_level_scope_decisions']=[{'rule_id':'8227:LIMIT07','status':'not applicable','quoted_value':f['notes'],'reason':'These are supporting representation/reference records. No general substitution is made a required8227response.'}]
pages=[]
notes={205:'8B7is recorded by its own builder;8B8explicitlyforces logarithmic substitution and is excluded. Example6alsoforces a nonlinear-exponential substitution. Example7is an unscaffolded nonlinear-log integral;its given graph is retained as supporting evidence.',206:'Example7continues. The general log-primitive reference is retained with restricted curriculum use. Examples8/9and8C1nonlinear-log/exponential integrals remain outside listed forms;no directly prescribed task starts here.',207:'8C2(ii)is prescribed after cancellation;2(i)is excluded.8C3and4area tasks require extra nonlinear/decomposition methods,but their given figures are retained.8C5and6are explicitly split by part and source-method conditions.'}
for page in range(205,208):
 ids=[r['item_id']for r in answers if r['source_pdf_page']==page]+[r['item_id']for r in figures if r['pdf_page']==page]
 if page==205:ids+=['8227:TB:Goldie:C8:Exercise-8B:7']
 pages.append({'pdf_page':page,'printed_page':page-14,'chapter':8,'page_status':'items enumerated','item_ids':ids,'continuation_item_ids':[],'source_evidence':ev(page),'reader':'Codex author','date':'2026-11-18','non_item_content':notes[page],'scope_screen':'Each excluded group and retained part is named;no entire-chapter inclusion or exclusion is inferred from its heading.'})
if __name__=='__main__':
 for name,data in [('answers-Goldie-C8-log-section.json',{'scope':'Every retained8C2(ii),8C5and8C6response,with extra-method and nonlinear-form boundaries.','items':answers}),('census-Goldie-C8-log-section.json',{'book':'Goldie','book_id':'8227-SRC-015','chapter':8,'source_path':SRC,'source_sha256':SHA,'scope':'Complete205–207including given graphs/reference and the8B7page overlap.','new_items':new+figures,'corrections':[],'pages':pages})]:
  (W/'tools/textbook-r5'/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
 for r in answers:
  for p in r['subparts']:
   if 'operation'in p:
    got=compute(p['operation']);expected=expression(p['printed_key_normalised'])
    assert primitive_agrees(p['operation'],got,expected)if p.get('answer_equivalence')=='up-to-additive-constant'else equivalent(got,expected),(r['item_id'],p['subpart'],got)
   for name,op in p.get('additional_operations',{}).items():assert equivalent(compute(op),expression(p['additional_operation_expected'][name])),(r['item_id'],name)
 print(len(answers),'items;',sum(len(r['subparts'])for r in answers),'outputs;',len(figures),'figures')
