"""Supplied identity coefficients and scaffolded reverse differentiation,214–222.

This is fixed-source author evidence,not a runtime problem generator. An extra
method or negative-binomial expansion is not silently made an8227requirement.
"""
import json
from author_Goldie_C8_opening import W,SRC,SHA,add,answers,new,ev,fig,figures,value,reasoning,compute,expression,equivalent,primitive_agrees,DEF,POWER
answers.clear();new.clear();figures.clear()
COEFF='8227:2020:M1:T1:O03:D02';FACTOR='8227:2020:M2:T1:O04:D02'
PRODUCT='8227:2020:M2:T4:O02:D01';REVERSE='8227:2020:M2:T5:O01:D03';AFFINE='8227:2020:M2:T5:O01:D01'

def val(label,op,key,method,page=352):
 p=value(label,'0',key,page,method);p['operation']=op;return p

# The general decomposition and negative-binomial choice are explicitly extra.
# The integration of a resulting polynomial/linear-fraction sum is retained
# conditionally,without pretending that the question supplies that sum itself.
f='3/((1+x)*(1-2*x))'
p=val('i-a-fractions',{'kind':'identity','operands':[f'apart({f},x)']},'2/(1-2*x)+1/(1+x)',
 'Independently decompose the original rational expression and multiply back. The source asks the learner to choose the partial-fraction form;that additional technique is not prescribed merely because the resulting linear fractions can be integrated.')
p2=val('i-b-integral',{'kind':'rounded','operands':[f'integrate({f},(x,0,1/10))'],'decimal_places':5},'0.31845',
 'The original denominator has no zero on[0,1/10]. Once(i-a)is available,the two reciprocal-linear terms have prescribed primitives−ln(1−2x)+ln(1+x). Their endpoint difference is ln(11/8),rounded only at the end to the required5decimal places.')
p2['additional_operations']={'original_proper_integral':{'kind':'proper-definite-integral','operands':[f,'0','1/10']}};p2['additional_operation_expected']={'original_proper_integral':'log(11/8)'}
p3=val('ii-a-first-three-terms',{'kind':'identity','operands':[f'series({f},x,0,3).removeO()']},'3+3*x+9*x**2',
 'Expand the original expression independently. Both source binomial exponents are−1,so this infinite-series requirement is outsideQUAL02. The resulting polynomial is retained as a conditional input to(ii-b),not as evidence of prescribed binomial coverage.')
p4=val('ii-b-approximation',{'kind':'identity','operands':['integrate(3+3*x+9*x**2,(x,0,1/10))']},'0.318',
 'Integrate the three displayed terms termwise on0..1/10. This gives3/10+3/200+3/1000=159/500. The source displays0.31800to align with the earlier5decimal-place integral. This calculation is prescribed polynomial integration conditional on the additional expansion in(ii-a).')
p5=val('ii-c-percentage-error',{'kind':'rounded','operands':['100*(log(11/8)-Rational(159,500))/log(11/8)'],'decimal_places':2},'0.14',
 'Compare the approximation with the exact original integral ln(11/8),not with a prematurely rounded denominator. The relative error is about0.14248percent,so the printed0.14percent agrees. This comparison supports numerical practice;it is not another syllabus demand by itself.')
row=add('Exercise-8E',3,216,'Compare an exact reciprocal-linear result with integration of three negative-binomial series terms for3/((1+x)(1−2x))on0..0.1. The general decomposition and n=−1expansion are extra;the following elementary integrations are conditionally prescribed once those earlier results exist.',[p,p2,p3,p4,p5],[DEF,AFFINE,POWER])
row['scope_check'].update(status='in-scope-parts-only',excluded_or_qualified_parts=['i-a:unsupplied partial-fraction decomposition is an additional method.','ii-a:negative-binomial expansion with exponent−1is outsideQUAL02.','ii-c:percentage comparison is supporting numerical context.'])
row['value_level_scope_decisions'].append({'rule_id':'8227:QUAL02','status':'outside','parts':['ii-a'],'quoted_value':'3(1+x)^(−1)(1−2x)^(−1)','reason':'The required expansion exponents−1are not positive integers. The following polynomial integration can be recorded conditionally without claiming the expansion is prescribed.'})
row['direct_demand_aspects']=[{'demand_id':DEF,'assessed_facet':'i-bandii-b,conditional on the earlier decomposition/expansion;these inputs are not initially supplied.'},{'demand_id':AFFINE,'assessed_facet':'i-bonly,afteri-a.'},{'demand_id':POWER,'assessed_facet':'ii-bonly,afterii-a.'}]
for target,source,cue in [(p2,'i-a','Hence'),(p4,'ii-a','Use the first three terms'),(p5,'ii-b','percentage error in your answer to part(b)')]:target['source_dependency_edges']=[{'from':source,'type':'cue','cue':cue,'role':'Use the earlier result;no official follow-through award table is available here.'}]
row['precision_angle_check']['source']='i-bexplicitly asks5decimal places. ii-bkey0.31800is the exact polynomial approximation with padded zeros. ii-cprints0.14percent without a separate precision instruction.'

f='(2*x**3-1)/(x**2*(2*x-1))'
identity='A*x**2*(2*x-1)+B*x*(2*x-1)+C*(2*x-1)+D*x**2-(2*x**3-1)'
p=val('i-coefficients',{'kind':'identity','operands':['Tuple('+','.join(f'solve(Poly({identity},x).all_coeffs(),(A,B,C,D))[{v}]'for v in['A','B','C','D'])+')']},'Tuple(1,2,1,-3)',
 'The source suppliesA+B/x+C/x²+D/(2x−1). Clear the original denominator,compare polynomial coefficients,and solve the linear system. This uses a provided identity template rather than choosing a partial-fraction method. The polynomial identity holds even at the excluded rational-function inputs0and1/2;those original domain exclusions are retained.')
p2=val('ii-integral',{'kind':'proper-definite-integral','operands':[f,'1','2']},'Rational(3,2)+log(Rational(16,27))/2',
 'On[1,2]the original denominator is nonzero. Insert the provided-form coefficients from(i),then integrate1+2/x+1/x²−3/(2x−1)using only constant,power and reciprocal-linear primitives. Evaluatex+2lnx−1/x−(3/2)ln(2x−1)at2and1. The result is3/2+½ln(16/27),as stated in the question.')
p2['check_mode']='show/prove';p2['key_page_override']=216
p2['source_dependency_edges']=[{'from':'i-coefficients','type':'cue','cue':'Hence show that','role':'The provided identity structure makes the remaining integrations elementary;no official F.T.award is inferred.'}]
row=add('Exercise-8E',4,216,'Use the supplied rational identity template to determineA,B,C,Dfor(2x³−1)/(x²(2x−1)),then hence establish its exact integral from1to2. Both the coefficient task and the subsequent elementary integrations survive the surrounding chapter exclusion.',[p,p2],[COEFF,DEF,AFFINE],[POWER],exam_attribution='Cambridge9709Paper32Q10June2010')
row['value_level_scope_decisions'][0].update(status='not applicable',quoted_value='A+B/x+C/x²+D/(2x−1);bounds1and2.',reason='No general substitution or unsupplied decomposition is requested:the ansatz is given,and all resulting primitive forms are prescribed.')
row['value_level_scope_decisions'].append({'rule_id':'8227:QUAL05','status':'within','parts':['ii'],'quoted_value':'x^(−2),together with a constant and reciprocal-linear terms,on1≤x≤2.','reason':'The power exponent−2is rational and is not−1;the separate reciprocal terms belong to Mathematics2.'})

f='(12+8*x-x**2)/((2-x)*(4+x**2))'
identity='A*(4+x**2)+(B*x+C)*(2-x)-(12+8*x-x**2)'
p=val('i-coefficients',{'kind':'identity','operands':['Tuple('+','.join(f'solve(Poly({identity},x).all_coeffs(),(A,B,C))[{v}]'for v in['A','B','C'])+')']},'Tuple(3,4,0)',
 'Clear the given denominator and compare coefficients in the suppliedA/(2−x)+(Bx+C)/(4+x²)form. The solution isA=3,B=4,C=0. The native4xkey confirms3/(2−x),not2/(2−x);the small-contact reading was not a textbook error. The original real domain excludesx=2.')
p2=val('ii-integral',{'kind':'proper-definite-integral','operands':[f,'0','1']},'log(Rational(25,2))',
 'For internal boundary QA,the original denominator is positive on[0,1]. The supplied-form result gives primitive−3ln(2−x)+2ln(4+x²). Its endpoint difference is3ln2+2ln(5/4)=ln(25/2). The second nonlinear-log primitive is beyond the explicitly listed affine forms;the independent coefficient task remains prescribed.',217)
p2['check_mode']='show/prove';p2['key_presence']='stated result in the question;no separate worked key'
row=add('Exercise-8E',6,217,'Determine the coefficients in the suppliedA/(2−x)+(Bx+C)/(4+x²)identity for(12+8x−x²)/((2−x)(4+x²)),then show its0..1integral isln(25/2). The coefficient identity is prescribed;the second nonlinear-log primitive in(ii)is supporting extension.',[p,p2],[COEFF],exam_attribution='Cambridge9709Paper31Q8November2011')
row['scope_check'].update(status='in-scope-parts-only',excluded_or_qualified_parts=['ii:integration of4x/(4+x²)is a nonlinear-log form beyond the listed affine forms.'])
row['direct_demand_aspects']=[{'demand_id':COEFF,'assessed_facet':'i only:the decomposition template is supplied.'}]

p=val('i-factor',{'kind':'identity','operands':['(4*x**3-x**2-11*x-6).subs(x,-1)']},'0',
 'Substitutex=−1into the given cubic:−4−1+11−6=0. By the factor theorem,x+1is a factor. Polynomial division independently gives quotient4x²−5x−6. Part(ii)requires an unsupplied rational-integration method and is not counted as prescribed factor-theorem coverage.',217)
p['check_mode']='show/prove';p['key_presence']='stated result in question;no separate worked key'
p['additional_operations']={'quotient_identity':{'kind':'identity','operands':['expand((x+1)*(4*x**2-5*x-6))-(4*x**3-x**2-11*x-6)']}};p['additional_operation_expected']={'quotient_identity':'0'}
row=add('Exercise-8E',7,217,'Showx+1is a factor of4x³−x²−11x−6. Retain this independently requested factor-theorem part;the following unscaffolded rational integral is outside the prescribed method list.',[p],[FACTOR],exam_attribution='Cambridge9709Paper33Q7November2015')
row['scope_check'].update(status='in-scope-parts-only',excluded_or_qualified_parts=['ii:unsupplied partial-fraction integration.'])

parts=[]
for label,f,derivative,primitive,integrand,rearrangement in [
 ('i','x*cos(x)','-x*sin(x)+cos(x)','-x*cos(x)+sin(x)','x*sin(x)','I=−xcosx+∫cosx dx'),
 ('ii','x*exp(2*x)','(2*x+1)*exp(2*x)','(x-Rational(1,2))*exp(2*x)','2*x*exp(2*x)','I=xe^(2x)−∫e^(2x)dx')]:
 p=val(label+'-a-derivative',{'kind':'identity','operands':[f'diff({f},x)']},derivative,
  'Differentiate the explicitly supplied product using the product rule. This is prescribed Mathematics2differentiation;it does not require inventing a primitive for an unscaffolded product integral.')
 parts.append(p)
 p=reasoning(label+'-b-rearrangement',rearrangement,
  'Integrate the derivative identity obtained in(a),then isolate the requested integralI. The original product to differentiate is supplied. This is the prescribed use of a given derivative to recover an integral,not an independent selection of the integration-by-parts formula.',352,'matches')
 p['source_dependency_edges']=[{'from':label+'-a-derivative','type':'cue','cue':'rearrange your expression','role':'Use the supplied-product derivative.'}];parts.append(p)
 p=val(label+'-c-primitive',{'kind':'real-elementary-antiderivative','operands':[integrand]},primitive,
  'Use the derivative relation supplied through(a)and rearranged in(b),then integrate only the remaining affine sine/cosine or exponential term. Independently integrate the original target and differentiate the final primitive to verify the result,up to an additive constant on its real domain.')
 p['answer_equivalence']='up-to-additive-constant';p['source_dependency_edges']=[{'from':label+'-b-rearrangement','type':'cue','cue':'use this expression','role':'The earlier identity supplies the missing reverse-differentiation scaffold.'}];parts.append(p)
row=add('Activity',2,218,'Activity8.2suppliesxcosxandxe^(2x). For each,differentiate by the product rule,rearrange to obtain the stated target integral,and finish it using an elementary remaining integral. All six requested responses are retained;deriving a general parts rule is a later,additional task.',parts,[PRODUCT,REVERSE])

p=reasoning('general-method','The resulting general rule is∫u dv/dx dx=uv−∫v du/dx dx,obtained by integrating and rearranging the product-rule identity.',
 'Differentiateuvto getuv′+u′v,then integrate on a common differentiable interval and rearrange. Activity8.2used explicitly supplied products;choosing arbitraryu,vfor a new target is a further method. The source key likewise says each earlier integral starts from the derivative ofuv. This is supporting explanation rather than a new prescribed8227technique.',352,'matches')
row=add('Prompt',5,218,'After Activity8.2,ask how to recover these integral expressions without first differentiating a specifically supplied product. This motivates the general integration-by-parts rule;its general-method selection stays supporting extension.',[p],teaches=[PRODUCT,REVERSE])
row['scope_check'].update(status='in-scope-parts-only',excluded_or_qualified_parts=['Deriving/selecting a general parts method is beyond the listed8227integration techniques.'])

for n,page,label,note,teaches,checks in [
 (27,214,'Repeated-denominator coefficient identity in Example8.15','The original integral needs an additional decomposition method. Its worked polynomial identityx+4=A(x+1)²+B(2x−1)(x+1)+C(2x−1)hasA=2,B=−1,C=−1. It is valid atx=−1and1/2after clearing denominators,but the original quotient still excludes those inputs.',[COEFF],[('expand(2*(x+1)**2-(2*x-1)*(x+1)-(2*x-1))','x+4')]),
 (28,215,'Quadratic-denominator coefficient identity in Example8.16','The worked identityx−2=(Ax+B)(x+1)+C(x²+2)hasA=1,B=0,C=−1. The subsequent nonlinear-log integration and the inverse-tan note are additional;this supporting block illustrates coefficient comparison and positivity ofx²+2.',[COEFF],[('expand(x*(x+1)-(x**2+2))','x-2')]),
 (29,218,'Product-rule reverse-differentiation scaffold','Activity8.2supplies the product to differentiate before asking for a target integral. This scaffolding is the reason its reverse-differentiation responses remain prescribed;the general parts formula below is not silently added to syllabus scope.',[PRODUCT,REVERSE],[]),
 (30,222,'Definite-parts endpoint warning','The displayed formula evaluatesu vat the bounds;it does not integrate that boundary product again. The formula is additional general-method support,not a required8227parts technique.',[],[])]:
 fig(n,page,label,note,teaches,'table',checks)
for f in figures:
 f['item_id']=f['item_id'].replace(':C5:',':C8:');f['source_evidence']=ev(f['pdf_page']);f['value_level_scope_decisions']=[{'rule_id':'8227:LIMIT07','status':'not applicable','quoted_value':f['notes'],'reason':'A supporting reference block creates no general integration-method requirement.'}]
pages=[]
notes={214:'The unnumbered partial-fractions integral continues from213. Example8.15requires an additional decomposition technique;its coefficient-identity teaching block is retained. No source integral is claimed prescribed merely from its location.',
 215:'Example8.16requires additional rational integration;its coefficient-identity block is retained. The following inverse-tan reference is outside prescribed derivatives/integrals.',
 216:'8E1/2and5require unsupplied partial-fraction integration. 8E3retains conditional elementary integration with its negative-binomial/method limits explicit.8E4has a supplied coefficient template and entirely elementary ensuing integral,so both parts are retained.',
 217:'8E6retains the supplied-template coefficient part but separates the nonlinear-log integral.8E7retains its independent factor-theorem proof.8E8forces general substitution. Example8.17starts an unscaffolded parts integral,excluded as a whole source task.',
 218:'Example8.17continues. Activity8.2and its product-rule scaffold are fully retained;Prompt5and the general parts derivation are additional conceptual support.',
 219:'Parts method-selection prose and Example8.18are outside required integration techniques;no independently prescribed question or teaching diagram starts here.',
 220:'Examples8.19/20require unscaffolded integration ofxlnxandlnx;both are additional methods. No independently requested differentiation subpart is present.',
 221:'Examples8.20continuation and8.21twice-by-parts integral are excluded as original source tasks. Their worked derivatives do not create new assessed subparts.',
 222:'8F1/2/5explicitly require parts;8F3/4explicitly require parts and a named substitution;8F6/7are unscaffolded parts integrals;8F8also uses inverse-tan. The endpoint-formula warning is retained as supporting reference only.'}
for page in range(214,223):
 ids=[r['item_id']for r in answers if r['source_pdf_page']==page]+[r['item_id']for r in figures if r['pdf_page']==page]
 pages.append({'pdf_page':page,'printed_page':page-14,'chapter':8,'page_status':'items enumerated'if ids else'scope-screened; no in-scope item starts','item_ids':ids,'continuation_item_ids':[],
  'source_evidence':ev(page),'reader':'Codex author','date':'2026-11-18','non_item_content':notes[page],'scope_screen':'Rendered-page exclusions distinguish additional original methods from independent or supplied-result prescribed subparts.'})

if __name__=='__main__':
 for name,data in [('answers-Goldie-C8-8E-activity.json',{'scope':'Provided coefficient templates,factor proof,conditional elementary integration,and every Activity8.2response;all extra methods explicit.','items':answers}),('census-Goldie-C8-8E-activity.json',{'book':'Goldie','book_id':'8227-SRC-015','chapter':8,'source_path':SRC,'source_sha256':SHA,'scope':'Rendered214–222scope and item census.','new_items':new+figures,'corrections':[],'pages':pages})]:
  (W/'tools/textbook-r5'/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
 for r in answers:
  for p in r['subparts']:
   if 'operation'in p:
    got=compute(p['operation']);target=expression(p['printed_key_normalised'])
    assert primitive_agrees(p['operation'],got,target)if p.get('answer_equivalence')=='up-to-additive-constant'else equivalent(got,target),(r['item_id'],p['subpart'],got)
   for name,op in p.get('additional_operations',{}).items():assert equivalent(compute(op),expression(p['additional_operation_expected'][name])),(r['item_id'],name)
 print(len(answers),'items;',sum(len(r['subparts'])for r in answers),'outputs;',len(figures),'figures')
