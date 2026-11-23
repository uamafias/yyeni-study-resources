"""Mixed calculus/identity/periodic-area parts212–213; source methods retained."""
import json
from author_Goldie_C8_opening import W,SRC,SHA,add,answers,new,ev,fig,figures,value,reasoning,compute,expression,equivalent,primitive_agrees,AREA,DEF
answers.clear();new.clear();figures.clear()
STAT='8227:2020:M1:T8:O04:D01';PRODUCT='8227:2020:M2:T4:O02:D01';ELEMENTARY='8227:2020:M2:T4:O01:D02'
TRIGINT='8227:2020:M2:T5:O01:D02';IDENTITY='8227:2020:M2:T5:O02:D01';PERIOD='8227:2020:M1:T6:O02:D02'
PROOF='8227:2020:M2:T3:O02:D05'
q='asin(sqrt(2/5))';f='sin(2*x)**2*cos(x)'
p=value('i-max-input','0','0.685',351,
 'Differentiate the original function and independently bracket its interior critical point. Analytically,y=4sin²xcos³xand y′=4sinxcos²x(2−5sin²x). In0<x<π/2there is one critical inputasin√(2/5). The function is0at both endpoints and positive inside;the derivative changes positive to negative at that input,so it is the global maximum on the stated interval. The key displays0.685;no exact precision is requested in(i).')
p['operation']={'kind':'bracketed-source-root','operands':[f'diff({f},x)','3/5','4/5'],'rounding':{'decimal_places':3}}
p['author_answer_form']='x=asin√(2/5)≈0.684719…radians;key0.685.'
p['additional_operations']={'exact_critical_residual':{'kind':'identity','operands':[f'diff({f},x).subs(x,{q})']},'endpoint_values':{'kind':'identity','operands':[f'Tuple(({f}).subs(x,0),({f}).subs(x,pi/2))']},'derivative_factorisation':{'kind':'trig-identity-residual','operands':[f'diff({f},x)','4*sin(x)*cos(x)**2*(2-5*sin(x)**2)']}}
p['additional_operation_expected']={'exact_critical_residual':'0','endpoint_values':'Tuple(0,0)','derivative_factorisation':'0'}
p2=value('ii-area','0','8/15',351,
 'The source explicitly requiresu=sinx,an additional general-method condition. Independently verify the mathematical area using the permitted identitysin²2xcosx=½cosx−¼cos3x−¼cos5x,and integrate the linear trig terms on0..π/2. It gives8/15. The selected substitution would instead give4∫₀¹u²(1−u²)du,the same value.')
p2['operation']={'kind':'proper-definite-integral','operands':[f,'0','pi/2']}
p2['additional_operations']={'identity_route':{'kind':'trig-identity-residual','operands':[f,'cos(x)/2-cos(3*x)/4-cos(5*x)/4']},'source_transformed_integral':{'kind':'proper-definite-integral','operands':['4*x**2*(1-x**2)','0','1']}}
p2['additional_operation_expected']={'identity_route':'0','source_transformed_integral':'8/15'}
row=add('Exercise-8D',6,212,'For y=sin²2xcosx on0≤x≤π/2,find the maximum input,then use the explicitly requiredu=sinxmethod to find its shaded area. The maximum is directly prescribed;the area’s mathematical identity route is valid but its original method instruction remains additional.',[p,p2],[STAT],[PRODUCT,ELEMENTARY],rep='graph',exam_attribution='Cambridge9709Paper33Q9June2013',precision_note='Radian interval0..π/2;the key prints maximum input0.685and exact area8/15. No numeric precision is asked in(i).')
row['scope_check'].update(status='in-scope-parts-only',excluded_or_qualified_parts=['ii-required-method:u=sinxis an additional source instruction. Its mathematical area can also be checked through permitted finite identities.'])
row['value_level_scope_decisions'][0].update(status='outside',parts=['ii-required-method'],quoted_value='Using the substitutionu=sinx,find the shaded area.',reason='The original forces a general substitution. Keep that demand distinct from the valid mathematical area and the prescribed maximum calculation.')
row['direct_demand_aspects']=[{'demand_id':STAT,'assessed_facet':'i only;the area method condition in(ii)is extra.'}]
g='exp(2*sin(x))*cos(x)';r='(sqrt(17)-1)/4'
p=value('i-area','0','(exp(2)-1)/2',351,
 'For internal supporting QA,the source’s mandatedu=sinxmaps0..π/2to0..1and makes the area∫₀¹e^(2u)du=(e²−1)/2. The original nonlinear-exponential integral and forced method are beyond the listed affine forms;the maximum in(ii)is a separate prescribed task.')
p['operation']={'kind':'proper-definite-integral','operands':[g,'0','pi/2']}
p['additional_operations']={'transformed_integral':{'kind':'proper-definite-integral','operands':['exp(2*x)','0','1']}};p['additional_operation_expected']={'transformed_integral':'(exp(2)-1)/2'}
p2=value('ii-max-input','0','0.896',351,
 'Differentiate the original function and bracket its interior critical point independently. The derivativee^(2sinx)(2cos²x−sinx)has the sign of2−s−2s²for s=sinx∈[0,1]. Its sole admissible zero iss=(√17−1)/4;the other quadratic root is below−1. The derivative changes positive to negative,so this is the unique maximum on0..π/2. Return3decimal places in radians.')
p2['operation']={'kind':'bracketed-source-root','operands':[f'diff({g},x)','4/5','1'],'rounding':{'decimal_places':3}}
p2['author_answer_form']='x=asin((√17−1)/4)≈0.895907…radians.'
p2['additional_operations']={'exact_critical_residual':{'kind':'identity','operands':[f'diff({g},x).subs(x,asin({r}))']},'sine_quadratic_roots':{'kind':'identity','operands':['FiniteSet(*solve(2*p**2+p-2,p))']},'endpoint_values':{'kind':'identity','operands':[f'Tuple(({g}).subs(x,0),({g}).subs(x,pi/2))']}}
p2['additional_operation_expected']={'exact_critical_residual':'0','sine_quadratic_roots':'FiniteSet((-1-sqrt(17))/4,(-1+sqrt(17))/4)','endpoint_values':'Tuple(1,0)'}
row=add('Exercise-8D',7,212,'For y=e^(2sinx)cosx on0≤x≤π/2,use the forcedu=sinxmethod for the area and separately find the maximum input to3decimal places. The maximum is prescribed explicit-function calculus;the original area method/form is supporting extension.',[p,p2],[STAT],[PRODUCT,ELEMENTARY],rep='graph',exam_attribution='Cambridge9709Paper33Q9June2014',precision_note='Radian interval0..π/2. Part(ii)explicitly asks3decimal places;part(i)asks an exact area.')
row['scope_check'].update(status='in-scope-parts-only',excluded_or_qualified_parts=['i:forced nonlinear-exponential substitution outside the listed affine forms.'])
row['value_level_scope_decisions'][0].update(status='outside',parts=['i'],quoted_value='Using the substitutionu=sinx,find the exact area under e^(2sinx)cosx.',reason='Part(i)requires the extra method/nonlinear integral. The independently requested maximum in(ii)does not depend on that integral.')
row['direct_demand_aspects']=[{'demand_id':STAT,'assessed_facet':'ii only.'}]
p=value('i-identity','0','0',212,
 'On sinθcosθ≠0,combinecotθ+tanθ=(cos²θ+sin²θ)/(sinθcosθ)=1/(sinθcosθ)=2cosec2θ. Use the Pythagorean and double-angle identities;the original domains agree. The expected identity is stated in the question,not supplied as a separate worked key.')
p['operation']={'kind':'trig-identity-residual','operands':['cot(x)+tan(x)','2*csc(2*x)']};p['check_mode']='show/prove';p['key_presence']='stated result in original question;no separate worked key'
p2=value('ii-integral','0','log(3)/2',212,
 'For internal extension QA,integrate the original positive cosecant expression on[π/6,π/3],which contains no pole. The identity from(i)gives half the sum ofcotθandtanθintegrals,and endpoint evaluation is½ln3. Those nonlinear-log primitives are not listed affine forms;the identity proof remains the directly prescribed part.')
p2['operation']={'kind':'proper-definite-integral','operands':['csc(2*x)','pi/6','pi/3']};p2['check_mode']='show/prove';p2['key_presence']='stated result in original question;no separate worked key'
row=add('Exercise-8D',8,212,'Prove cotθ+tanθ≡2cosec2θ,then show the given cosecant integral is½ln3. The proof is prescribed;the nonlinear-log integral is checked as supporting extension.',[p,p2],[PROOF],['8227:2020:M2:T3:O01:D01','8227:2020:M2:T3:O02:D03'],exam_attribution='Cambridge9709Paper31Q5November2013',precision_note='Angles and boundsπ/6..π/3are radians. Both results are exact stated-result checks.')
row['scope_check'].update(status='in-scope-parts-only',excluded_or_qualified_parts=['ii:cosecant integration leads to nonlinear-log primitives beyond listed affine forms.'])
p=reasoning('i-transformation','On the positive branch0<θ<π/2, x=sin²θgives√(x/(1−x))dx=2sin²θdθ.',
 'Here√(sin²θ/cos²θ)=tanθanddx=2sinθcosθdθ. The branch matters:the square root cannot be replaced by a signed tangent without it. The original explicitly requires this general trig substitution;it is not a prescribed integration method.',212,'show/prove')
p['key_presence']='stated result in original question;no separate worked key'
p2=value('ii-integral','0','pi/6-sqrt(3)/4',351,
 'For supporting QA,positive-branch boundsx=0,1/4map toθ=0,π/6. The transformed integral2∫₀^(π/6)sin²θdθevaluates by a permitted double-angle identity toπ/6−√3/4. Independent direct quadrature of the original integrand checks the number;the original method in(i)remains additional.')
p2['operation']={'kind':'proper-definite-integral','operands':['sqrt(x/(1-x))','0','1/4']}
p2['additional_operations']={'given_transformed_integral':{'kind':'proper-definite-integral','operands':['2*sin(x)**2','0','pi/6']}};p2['additional_operation_expected']={'given_transformed_integral':'pi/6-sqrt(3)/4'}
add('Exercise-8D',9,212,'Show a requiredbounded-branchx=sin²θtransformation for√(x/(1−x)),then evaluate its0..1/4integral. The transformed sin²θcalculation is useful supporting evidence;the original general substitution is additional.',[p,p2],teaches=[IDENTITY,TRIGINT,DEF],forced=True,exam_attribution='Cambridge9709Paper3Q6November2005',precision_note='Original xbounds0..1/4are ordinary numbers,not angles. The selected transformed branch has radian bounds0..π/6;the result is exact.')
p=value('a-primitive','0','3*x+tan(2*x)/2',351,
 'Use1+tan²2x=sec²2xto rewrite4+tan²2xas3+sec²2x. Integrate the constant and affine secant-square term,retaining coefficient1/2. The original poles cos2x=0remain excluded;the arbitrary constant is local to each connected component.')
p['operation']={'kind':'real-elementary-antiderivative','operands':['4+tan(2*x)**2']};p['answer_equivalence']='up-to-additive-constant'
p['additional_operations']={'identity_route':{'kind':'trig-identity-residual','operands':['4+tan(2*x)**2','3+sec(2*x)**2']}};p['additional_operation_expected']={'identity_route':'0'}
p2=value('b-integral','0','(sqrt(3)*pi+log(4))/8',351,
 'For supporting QA,use the addition formula to rewrite the integrand as√3/2+½cotx. Its exact positive-bound integral is√3π/8+¼ln2. The cotangent primitive is a nonlinear-log extension,so this part is not counted as a prescribed affine-trig integral.')
p2['operation']={'kind':'proper-definite-integral','operands':['sin(x+pi/6)/sin(x)','pi/4','pi/2']}
row=add('Exercise-8D',10,213,'Integrate4+tan²2x,and separately evaluate∫_(π/4)^(π/2)sin(x+π/6)/sinx dx. Part(a)reduces directly to affine sec²;part(b)needs an extra nonlinear-log primitive.',[p,p2],[IDENTITY,TRIGINT],exam_attribution='Cambridge9709Paper31Q5June2015',precision_note='All angles are radians. Part(a)has componentwise arbitrary constants across its poles;part(b)asks an exact value.')
row['scope_check'].update(status='in-scope-parts-only',excluded_or_qualified_parts=['b:the addition formula gives a cotangent term whose primitive is beyond listed affine forms.'])
row['direct_demand_aspects']=[{'demand_id':IDENTITY,'assessed_facet':'a only'},{'demand_id':TRIGINT,'assessed_facet':'a only'}]
h='sin(2*x)**3*cos(2*x)**3'
p=value('i-first-lobe-area','0','1/24',351,
 'The first positive lobe is0..π/4. The source requiresu=sin2x,which is one-to-one on this lobe and yields½∫₀¹u³(1−u²)du=1/24. Independently verify the mathematical area viaf=(sin4x)³/8=(3sin4x−sin12x)/32. The original required substitution remains additional.')
p['operation']={'kind':'proper-definite-integral','operands':[h,'0','pi/4']}
p['additional_operations']={'source_transformed_integral':{'kind':'proper-definite-integral','operands':['x**3*(1-x**2)/2','0','1']},'identity_route':{'kind':'trig-identity-residual','operands':[h,'(3*sin(4*x)-sin(12*x))/32']}}
p['additional_operation_expected']={'source_transformed_integral':'1/24','identity_route':'0'}
p2=value('ii-k','40*(pi/4)/pi','10',351,
 'f(x+π/4)=−f(x),so|f|has equal positive-area lobes of widthπ/4. Starting at0,40lobes end at40π/4=10π;thereforek=10. The numerical value ofAfrom(i)is unnecessary:onlythe given first-lobe areaA>0is used. The accumulated absolute area is strictly increasing despite isolated zeros,so this endpoint is unique without assumingkinteger.')
p2['additional_operations']={'absolute_period_sign_flip':{'kind':'trig-identity-residual','operands':[f'({h}).subs(x,x+pi/4)',f'-({h})']}}
p2['additional_operation_expected']={'absolute_period_sign_flip':'0'}
p2['source_dependency_edges']=[{'from':'given diagram/definition ofA','type':'cue','cue':'40A','role':'Use equal unsigned lobe areas;the numerical integration method in(i)is not needed.'}]
row=add('Exercise-8D',11,213,'For sin³2xcos³2x,the first shaded lobe has areaA. Part(i)forcesu=sin2xto calculateA;part(ii)uses∫₀^(kπ)|sin³2xcos³2x|dx=40Ato findkby periodic unsigned areas,without needing the numericA.',[p,p2],[AREA,PERIOD],teaches=[IDENTITY],rep='graph',exam_attribution='Cambridge9709Paper33Q7November2012',precision_note='Radian xaxis. The first-lobe area1/24andk=10are exact. Absolute value is essential;the signed whole-period integral would cancel.')
row['scope_check'].update(status='in-scope-parts-only',excluded_or_qualified_parts=['i-required-method:u=sin2xis an additional source instruction,although the mathematical area also has a permitted finite identity route.'])
row['value_level_scope_decisions'][0].update(status='outside',parts=['i-required-method'],quoted_value='Use the substitutionu=sin2xto find the valueofA.',reason='The prescribed part(ii)can use the given positive lobe area without the extra integration method in(i).')
row['direct_demand_aspects']=[{'demand_id':AREA,'assessed_facet':'ii:interpret the absolute integral as a sum of equal geometric lobe areas.'},{'demand_id':PERIOD,'assessed_facet':'ii:establish/use the unsigned lobe repeat widthπ/4.'}]
p=reasoning('method-claim','The obviousu=x²−1choice is unsuitable,but the absolute claim that no previously taught integration technique can work is too strong.',
 'On x>1,chooseu=(x−1)/(x+1). Then u′/u=2/(x²−1),so the general substitution already taught earlier gives∫du/u=lnu+C. Equivalently reverse-differentiate ln(x−1)−ln(x+1). The printed key only explains whyu=x²−1fails;that does not exclude this valid alternative. General-method selection is still outside required8227techniques.',351,'key incomplete')
p['additional_operations']={'ratio_substitution':{'kind':'identity','operands':['diff((x-1)/(x+1),x)/((x-1)/(x+1))-2/(x**2-1)']},'candidate_primitive_derivative':{'kind':'identity','operands':['diff(log((x-1)/(x+1)),x)-2/(x**2-1)']}}
p['additional_operation_expected']={'ratio_substitution':'0','candidate_primitive_derivative':'0'}
row=add('Prompt',4,213,'The boxed prompt asks why none of the techniques learnt so far can integrate2/(x²−1). Its key only rejects the obviousu=x²−1candidate;an already-taught general substitution supplies a counterexample to that blanket premise.',[p])
row['scope_check'].update(status='in-scope-parts-only',excluded_or_qualified_parts=['General integration-method comparison is supporting source-quality evidence,not a directly prescribed8227calculation. The counterexample uses a technique the book previously taught;it does not commission that technique for8227.'])

for n,page,label,note,teaches,checks,parent in [
 (23,212,'Exercise8D6maximum/area diagram','The function sin²2xcosx is nonnegative on[0,π/2],zero at both endpoints and has one interior maximumatasin√(2/5). The shaded region uses the same bounded curve,not a full-period sine sketch.',[STAT,AREA],[('Tuple((sin(2*x)**2*cos(x)).subs(x,0),(sin(2*x)**2*cos(x)).subs(x,pi/2))','Tuple(0,0)')],'Exercise-8D:6'),
 (24,212,'Exercise8D7nonlinear-exponential maximum diagram','e^(2sinx)cosxstarts at1and ends0on[0,π/2],remaining positive inside. Its unique interior maximum corresponds tosinx=(√17−1)/4. The left boundary is the y-axis;the shaded area is not zero atx=0.',[STAT,AREA],[('Tuple((exp(2*sin(x))*cos(x)).subs(x,0),(exp(2*sin(x))*cos(x)).subs(x,pi/2))','Tuple(1,0)')],'Exercise-8D:7'),
 (25,213,'Exercise8D11periodic signed/unsigned lobes','The first positive lobe of sin³2xcos³2x is shaded0..π/4. The function flips sign afterπ/4;the absolute value repeats. Its ordinary period isπ/2and peak magnitude1/8. The integral in(ii)explicitlyuses absolute value.',[AREA,PERIOD],[('(sin(2*x)**3*cos(2*x)**3).subs(x,pi/8)','1/8')],'Exercise-8D:11'),
 (26,213,'Partial-fraction polynomial identity reminder','After clearing denominators,the equation2≡A(x+1)+B(x−1)is a polynomial identity and can be evaluated atx=±1. Those inputs remain excluded from the original fraction. This teaches identity/domain reasoning,not a new required partial-fractions method.',['8227:2020:M1:T1:O03:D01'],[('expand(1*(x+1)-1*(x-1))','2')],None)]:
 fig(n,page,label,note,teaches,'graph'if n<26 else'table',checks,parent)
for f in figures:
 f['item_id']=f['item_id'].replace(':C5:',':C8:');f['parent_item_id']=f['parent_item_id'].replace(':C5:',':C8:')if f['parent_item_id']else None;f['source_evidence']=ev(f['pdf_page']);f['value_level_scope_decisions']=[{'rule_id':'8227:LIMIT07','status':'not applicable','quoted_value':f['notes'],'reason':'A given figure/reference does not require a general integration method.'}]
pages=[]
notes={212:'8D3(iii)–(v)continues with additional nonlinear forms;8D4/5are inverse-tan integration.8D6/7separate required extra area methods from prescribed maxima.8D8separates proof from nonlinear-log integration;8D9is bounded-branch substitution support.',213:'8D10splits affine-sec²integration from a nonlinear-log extension.8D11separates the extra required first-area method from prescribed unsigned-lobe counting. The overbroad impossibility prompt has a verified alternative;the following partial-fraction identity is retained only as domain/identity reference.'}
for page in[212,213]:
 pages.append({'pdf_page':page,'printed_page':page-14,'chapter':8,'page_status':'items enumerated','item_ids':[r['item_id']for r in answers if r['source_pdf_page']==page]+[r['item_id']for r in figures if r['pdf_page']==page],
  'continuation_item_ids':['8227:TB:Goldie:C8:Exercise-8D:3']if page==212 else[],
  'source_evidence':ev(page),'reader':'Codex author','date':'2026-11-18','non_item_content':notes[page],'scope_screen':'All original method demands remain visible;an in-scope independent part is not discarded because its neighbour is additional.'})
if __name__=='__main__':
 for name,data in [('answers-Goldie-C8-8D.json',{'scope':'Every retained8D6–11andPrompt4response,with prescribed parts and supporting method-boundary work separated.','items':answers}),('census-Goldie-C8-8D.json',{'book':'Goldie','book_id':'8227-SRC-015','chapter':8,'source_path':SRC,'source_sha256':SHA,'scope':'Complete212–213,with all three given diagrams and identity reference.','new_items':new+figures,'corrections':[],'pages':pages})]:
  (W/'tools/textbook-r5'/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
 for r in answers:
  for p in r['subparts']:
   if 'operation'in p:
    got=compute(p['operation']);expected=expression(p['printed_key_normalised'])
    assert primitive_agrees(p['operation'],got,expected)if p.get('answer_equivalence')=='up-to-additive-constant'else equivalent(got,expected),(r['item_id'],p['subpart'],got)
   for name,op in p.get('additional_operations',{}).items():assert equivalent(compute(op),expression(p['additional_operation_expected'][name])),(r['item_id'],name)
 print(len(answers),'items;',sum(len(r['subparts'])for r in answers),'outputs;',len(figures),'figures')
