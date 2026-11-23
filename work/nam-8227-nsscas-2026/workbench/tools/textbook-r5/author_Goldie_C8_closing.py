"""Closing228–230practice and method references; mixed scope kept explicit."""
import json
from author_Goldie_C8_opening import W,SRC,SHA,add,answers,new,ev,fig,figures,value,reasoning,compute,expression,equivalent,primitive_agrees,DEF,POWER
answers.clear();new.clear();figures.clear()
IDENTITY='8227:2020:M2:T5:O02:D01';TRIGINT='8227:2020:M2:T5:O01:D02';AFFINE='8227:2020:M2:T5:O01:D01'
COEFF='8227:2020:M1:T1:O03:D02';STAT='8227:2020:M1:T8:O04:D01';PRODUCT='8227:2020:M2:T4:O02:D01'
def v(label,op,key,method,page=354):
 p=value(label,'0',key,page,method);p['operation']=op;return p
def partial(row,excluded):row['scope_check'].update(status='in-scope-parts-only',excluded_or_qualified_parts=excluded);return row

parts=[]
for label,answer,why in [
 ('i','General partial fractions:2/(x+3)−1/(x−1).','Factorx²+2x−3=(x+3)(x−1);the numerator is not proportional to its derivative. A general decomposition choice is additional8227method scope.'),
 ('ii','Recognise half the denominator derivative,then a logarithmic primitive.','The numeratorx+1is half of2x+2. This nonlinearF′/Fcase is useful supporting method evidence but is beyond the listed reciprocal-linear forms.'),
 ('iii','Integration by parts is the source’s selected method.','Forxe^x,the product is not of the supplied reverse-differentiation form here. General parts selection is additional.'),
 ('iv','Chooseu=x²for the source’s general substitution method.','The exponent derivative is2x. The original asks the learner to choose this method forxe^(x²);it is a nonlinear-exponential extension.'),
 ('v','Recognise the denominator derivative2x+cosx.','This givesln|x²+sinx|on nonzero components. It is a nonlinear-log extension,not a listed reciprocal-linear integral.'),
 ('vi','Useu=sinxas the source’s method;an alternative permitted route is a finite trig identity.','The source selection is extra general-method discussion. Independently,cosxsin²x=(cosx−cos3x)/4,derived from addition/double-angle identities,and can be integrated as affine cosines.')]:
 parts.append(reasoning(label,answer,why,353,'matches'))
row=partial(add('Prompt',6,226,'For six displayed integrals,select a method and a substitution variable where appropriate,but do not perform the integrations yet. The source methods are recorded as supporting selection evidence. Part(vi)also has a specifically derived finite-identity route within8227mathematics.',parts,teaches=[IDENTITY,TRIGINT]),['The original asks general method choices,not six new prescribed integration techniques. Its later Activity8.3supplies the separate integration task.'])

p=v('vi-primitive',{'kind':'real-elementary-antiderivative','operands':['cos(x)*sin(x)**2']},'sin(x)**3/3',
 'The Activity asks for the integral without mandating the earlier method suggestion. Derivecosxsin²x=(cosx−cos3x)/4from addition/double-angle identities,then integrate those affine cosine terms. The resulting sine combination equals sin³x/3up to its arbitrary constant;differentiate both forms against the original integrand.',353)
p['answer_equivalence']='up-to-additive-constant';p['additional_operations']={'finite_identity':{'kind':'trig-identity-residual','operands':['cos(x)*sin(x)**2','(cos(x)-cos(3*x))/4']}};p['additional_operation_expected']={'finite_identity':'0'}
row=partial(add('Activity',3,228,'Activity8.3revisits the six earlier integrals. Retain(vi),cosxsin²x,through its explicit finite-identity alternative. Parts(i)–(v)require additional unsupplied partial-fraction,parts or nonlinear-log/exponential methods.',[p],[IDENTITY,TRIGINT]),['i–v:additional unsupplied decomposition,parts,or nonlinear-log/exponential methods;no direct8227coverage is claimed from them.'])

parts=[]
for label,integrand,key,method,page in [
 ('i','cos(3*x-1)','sin(3*x-1)/3','Integrate the affine cosine and retain the reciprocal input-gradient factor1/3.',353),
 ('iii','exp(1-x)','-exp(1-x)','The affine exponent has gradient−1,so its primitive needs a negative coefficient.',353),
 ('iv','cos(2*x)','sin(2*x)/2','Integrate the affine cosine with multiplier1/2.',353),
 ('vii','sqrt(2*x-3)','(2*x-3)**(Rational(3,2))/3','Integrate the linear power with n=1/2,on its real domainx≥3/2;the primitive derivative is checked on the interiorx>3/2.',353),
 ('xiv','sin(2*x)**3','-cos(2*x)/2+cos(2*x)**3/6','Use sin³2x=(3sin2x−sin6x)/4,derived from addition/double-angle relations. Integrate the two affine sine terms;the printed cosine-cube form is an equivalent primitive.',354)]:
 p=v(label,{'kind':'real-elementary-antiderivative','operands':[integrand]},key,method+' An arbitrary constant is retained on the original real component.',page);p['answer_equivalence']='up-to-additive-constant';parts.append(p)
parts[-1]['additional_operations']={'finite_identity':{'kind':'trig-identity-residual','operands':['sin(2*x)**3','(3*sin(2*x)-sin(6*x))/4']}};parts[-1]['additional_operation_expected']={'finite_identity':'0'}
row=partial(add('Exercise-8H',1,228,'Choose methods and integrate the mixed list. Retain(i),(iii),(iv),(vii)as direct affine trig/exponential/power forms and(xiv)through a finite derived trig identity. The other original parts need additional methods;they are not silently included through the chapter heading.',parts,[TRIGINT,AFFINE,POWER,IDENTITY],qualifier='Part(vii)is(2x−3)^(1/2),with rational exponent1/2≠−1.'),['ii,vi:nonlinear reverse-chain rational forms beyond the listed affine primitive inputs.','v,ix:unscaffolded logarithmic-product integration.','viii,x:unsupplied partial-fractions integration.','xi:nonlinear exponential primitive.','xii:nonlinear trig-log primitive.','xiii:unscaffolded product integration requiring repeated parts.'])
row['direct_demand_aspects']=[{'demand_id':TRIGINT,'assessed_facet':'i,ivandxiv'},{'demand_id':AFFINE,'assessed_facet':'iii'},{'demand_id':POWER,'assessed_facet':'vii'},{'demand_id':IDENTITY,'assessed_facet':'xiv;finite identity derived explicitly,not a memorised extra rule.'}]

parts=[]
for label,f,lo,hi,key,method in [
 ('i','1/sqrt(3*x-8)','8','24','Rational(8,3)','The enlarged original has bounds8and24. Its radicand ranges16..64,so this is a proper finite linear-power integral,not an endpoint-improper one. Primitive(2/3)√(3x−8)gives(2/3)(8−4)=8/3.'),
 ('ii','1/(3*x-8)','8','24','log(4)/3','The denominator stays positive16..64. Evaluate(1/3)ln(3x−8)at the bounds to get(1/3)ln4.'),
 ('iii','9*x/(3*x-8)','8','24','48+8*log(4)','Rewrite9x/(3x−8)=3+8/(3x−8),then integrate the constant and reciprocal-linear term. The interval avoids the original pole8/3.'),
 ('iv','sin(x)**3','0','pi/2','Rational(2,3)','Use sin³x=(3sinx−sin3x)/4,derived from prescribed addition/double-angle identities. Integrate the finite sine sum and evaluate the radian bounds0andπ/2.')]:
 parts.append(v(label,{'kind':'proper-definite-integral','operands':[f,lo,hi]},key,method))
parts[-1]['additional_operations']={'finite_identity':{'kind':'trig-identity-residual','operands':['sin(x)**3','(3*sin(x)-sin(3*x))/4']}};parts[-1]['additional_operation_expected']={'finite_identity':'0'}
row=partial(add('Exercise-8H',2,228,'Retain the three proper rational/linear-power integrals on8..24and the finite-identity sin³xintegral on0..π/2. The enlarged source resolves an earlier false endpoint-improper boundary note. Other parts require additional nonlinear or product methods.',parts,[DEF,POWER,AFFINE,IDENTITY,TRIGINT]),['v,viii,x:unscaffolded product integration.','vi,vii,ix:nonlinear reverse-chain power/logarithm forms beyond the listed affine inputs.'])
row['value_level_scope_decisions'].append({'rule_id':'8227:QUAL04','status':'not applicable','parts':['i','ii','iii'],'quoted_value':'All three lower bounds8andupper bounds24;3x−8ranges16..64.','reason':'These are proper continuous finite integrals. The old endpoint-improper description was an author boundary-reading error,not a textbook defect.'})
row['precision_angle_check']['source']='All retained answers are exact. Only(iv)has angular bounds;0..π/2are radians.'

f='(6+6*x)/((2-x)*(2+x**2))';identity='A*(2+x**2)+(B*x+C)*(2-x)-(6+6*x)'
op='Tuple('+','.join(f'solve(Poly({identity},x).all_coeffs(),(A,B,C))[{v}]'for v in['A','B','C'])+')'
p=v('i-coefficients',{'kind':'identity','operands':[op]},'Tuple(3,3,0)',
 'Clear the suppliedA/(2−x)+(Bx+C)/(2+x²)template and compare coefficients. Solve the resulting linear system to getA=3,B=3,C=0. Preserve the original exclusionx=2.')
p2=v('ii-integral',{'kind':'proper-definite-integral','operands':[f,'-1','1']},'3*log(3)',
 'After(i),the second term3x/(2+x²)is odd and continuous on[−1,1],so its symmetric integral is0without needing any nonlinear-log primitive. Integrate3/(2−x)using the listed reciprocal-linear rule to obtain3ln3. This provided-template and symmetry route keeps the original integral within prescribed mathematics.',228)
p2['check_mode']='show/prove';p2['key_presence']='stated result in the original question;no separate worked key'
p2['additional_operations']={'odd_term':{'kind':'identity','operands':['(3*x/(2+x**2)).subs(x,-x)+3*x/(2+x**2)']},'affine_remainder':{'kind':'proper-definite-integral','operands':['3/(2-x)','-1','1']}};p2['additional_operation_expected']={'odd_term':'0','affine_remainder':'3*log(3)'}
p2['source_dependency_edges']=[{'from':'i-coefficients','type':'cue','cue':'Show that','role':'Use the supplied-form decomposition;the odd term cancels on symmetric bounds.'}]
add('Exercise-8H',3,228,'Use a supplied coefficient template for(6+6x)/((2−x)(2+x²)),then show its−1..1integral is3ln3. The nonlinear rational term is odd on the symmetric interval,so no extra primitive is needed;both parts are retained.',[p,p2],[COEFF,DEF,AFFINE],exam_attribution='Cambridge9709Paper33Q8June2014')

f='x**2*exp(2-x)'
p=v('i-maximum-input',{'kind':'identity','operands':[f'diff({f},x).subs(x,2)']},'0',
 'Differentiate the supplied product toxe^(2−x)(2−x). The stationary inputs are0and2;at0the derivative changes negative to positive,so0is a minimum. At2it changes positive to negative,so the labelled maximumMhas input2and ordinate4. The requested stated input2is thereby established.',229)
p['check_mode']='show/prove';p['key_presence']='stated result in original question'
p['additional_operations']={'derivative_factorisation':{'kind':'identity','operands':[f'diff({f},x)-x*exp(2-x)*(2-x)']},'stationary_inputs':{'kind':'identity','operands':[f'FiniteSet(*solve(diff({f},x),x))']},'second_derivative_at_max':{'kind':'identity','operands':[f'diff({f},x,2).subs(x,2)']}};p['additional_operation_expected']={'derivative_factorisation':'0','stationary_inputs':'FiniteSet(0,2)','second_derivative_at_max':'-2'}
p2=v('ii-integral',{'kind':'proper-definite-integral','operands':[f,'0','2']},'2*E**2-10',
 'Independently evaluate the original positive integral on0..2and compare the printed2e²−10. It needs an unscaffolded polynomial-exponential primitive,so its result stays supporting extension rather than a prescribed repeated-parts demand.')
row=partial(add('Exercise-8H',4,229,'Show the labelled maximum ofx²e^(2−x)has input2,and then evaluate its0..2integral. The derivative/stationary proof is prescribed;the unscaffolded product integral is supporting extension.',[p,p2],[STAT],[PRODUCT],rep='graph',exam_attribution='Cambridge9709Paper31Q9June2015'),['ii:unscaffolded repeated-parts integration.'])

for n,page,label,note,teaches,checks,parent in [
 (34,227,'Standard integration table','The listed powers,rational reciprocal,exponential,sine and cosine primitives are relevant. Powers needn≠−1,reciprocals needx≠0,and every indefinite primitive has a componentwise arbitrary constant.',[POWER,AFFINE,TRIGINT],[('diff(exp(x),x)','exp(x)'),('diff(-cos(x),x)','sin(x)')],None),
 (35,227,'Method-choice comparison table','Affine standard-function variants and double-angle trig rewrites are prescribed. General substitution,parts,unsupplied partial fractions and inverse-tan primitives are additional. The table is a source method taxonomy,not a scope extension;odd-trig finite identity alternatives are checked individually.',[IDENTITY,TRIGINT],[],None),
 (36,229,'Exercise8H4 stationary-point diagram','x²e^(2−x)is nonnegative,has a minimum at(0,0),and a maximumM=(2,4). The negative-xbranch is above the axis. The integral in(ii)uses0..2rather than an unbounded drawn region.',[STAT],[('(x**2*exp(2-x)).subs(x,2)','4')],'Exercise-8H:4'),
 (37,229,'Mixed key-point reference block','The power,affine-exponential and reciprocal-linear reference rules are relevant. The inverse-tan derivative and general nonlinearF′/Freference are broader source teaching support. Constantsa≠0and real domains are required when a primitive divides bya.',[POWER,AFFINE],[],None),
 (38,230,'Affine-trigonometric primitive summary','The boxed cos(ax+b),sin(ax+b),sec²(ax+b)primitives requirea≠0;ifa=0the integrand is constant when defined and is handled separately. Inverse-tan,partial-fractions and parts outcomes alongside them remain additional.',[TRIGINT],[('diff(sin(a*x+b)/a,x)','cos(a*x+b)'),('diff(-cos(a*x+b)/a,x)','sin(a*x+b)'),('diff(tan(a*x+b)/a,x)','sec(a*x+b)**2')],None)]:
 fig(n,page,label,note,teaches,'graph'if n==36 else'table',checks,parent)
for f in figures:
 f['item_id']=f['item_id'].replace(':C5:',':C8:');f['parent_item_id']=f['parent_item_id'].replace(':C5:',':C8:')if f['parent_item_id']else None;f['source_evidence']=ev(f['pdf_page']);f['value_level_scope_decisions']=[{'rule_id':'8227:LIMIT07','status':'not applicable','quoted_value':f['notes'],'reason':'The reference/given figure is support,not a new general integration-method demand.'}]
pages=[]
notes={227:'Both standard-rule and method-comparison tables have separate reference records;broader methods are explicitly labelled additional.',228:'Activity8.3(vi),five retained8H1parts,four retained8H2parts,and both8H3parts are recorded. The negative-binomial/parts/nonlinear-method groups are not automatically included. 8H2(i)has proper bounds8and24,not an improper endpoint.',229:'8H4splits prescribed stationarity from its additional product integral;its diagram and mixed summary block are recorded.8H5forces substitution plus parts and is outside required methods.',230:'The affine-trig summary has a reference record. The remaining outcomes introduce no new independently requested task;inverse-tan,general substitution,partial fractions and parts outcomes are additional.'}
for page in range(227,231):
 ids=[r['item_id']for r in answers if r['source_pdf_page']==page]+[r['item_id']for r in figures if r['pdf_page']==page]
 pages.append({'pdf_page':page,'printed_page':page-14,'chapter':8,'page_status':'items enumerated','item_ids':ids,'continuation_item_ids':[],'source_evidence':ev(page),'reader':'Codex author','date':'2026-11-18','non_item_content':notes[page],'scope_screen':'Only specified original parts are prescribed;finite-identity and symmetric-cancellation routes are independently shown. Prompt6on226is linked by the8Gcensus.'})
if __name__=='__main__':
 for name,data in [('answers-Goldie-C8-closing.json',{'scope':'Closing method prompt,Activity8.3vi,and retained8Hparts;extra methods kept visible.','items':answers}),('census-Goldie-C8-closing.json',{'book':'Goldie','book_id':'8227-SRC-015','chapter':8,'source_path':SRC,'source_sha256':SHA,'scope':'Complete227–230plusPrompt6on226owned by the8Gcensus.','new_items':new+figures,'corrections':[],'pages':pages})]:
  (W/'tools/textbook-r5'/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
 for r in answers:
  for p in r['subparts']:
   if 'operation'in p:
    got=compute(p['operation']);target=expression(p['printed_key_normalised'])
    assert primitive_agrees(p['operation'],got,target)if p.get('answer_equivalence')=='up-to-additive-constant'else equivalent(got,target),(r['item_id'],p['subpart'],got)
   for name,op in p.get('additional_operations',{}).items():assert equivalent(compute(op),expression(p['additional_operation_expected'][name])),(r['item_id'],name)
 print(len(answers),'items;',sum(len(r['subparts'])for r in answers),'outputs;',len(figures),'figures')
