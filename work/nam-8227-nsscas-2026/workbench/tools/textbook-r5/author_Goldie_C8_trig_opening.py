"""208–211: distinguish identity routes from compulsory general methods."""
import json
from author_Goldie_C8_opening import W,SRC,SHA,add,answers,new,ev,fig,figures,value,reasoning,compute,expression,equivalent,primitive_agrees,AREA,DEF
answers.clear();new.clear();figures.clear()
STATIONARY='8227:2020:M1:T8:O04:D01';CLASSIFY='8227:2020:M1:T8:O04:D02';QUOTIENT='8227:2020:M2:T4:O02:D02'
IDENTITY='8227:2020:M2:T5:O02:D01';TRIGINT='8227:2020:M2:T5:O01:D02';LAW='8227:2020:M2:T2:O01:D02';EXACT='8227:2020:M1:T6:O03:D01'
def indefinite(label,f,key,page,method):
 p=value(label,'0',key,page,method);p['operation']={'kind':'real-elementary-antiderivative','operands':[f]};p['answer_equivalence']='up-to-additive-constant';return p
p=value('i-max-input','solve(diff(x/(x**2+1),x),x)[1]','1',351,
 'Differentiate the actual rational function. Stationary inputs are−1and1;the positive point1has negative second derivative and is the indicated maximumM. The negative input is a minimum,not a second maximum to report.')
p['additional_operations']={'all_stationary_inputs':{'kind':'identity','operands':['FiniteSet(*solve(diff(x/(x**2+1),x),x))']},'curvature_at_candidates':{'kind':'identity','operands':['Tuple(diff(x/(x**2+1),x,2).subs(x,-1),diff(x/(x**2+1),x,2).subs(x,1))']}}
p['additional_operation_expected']={'all_stationary_inputs':'FiniteSet(-1,1)','curvature_at_candidates':'Tuple(1/2,-1/2)'}
p2=value('ii-area-formula','integrate(x/(x**2+1),(x,0,p))','log(1+p**2)/2',351,
 'For internal extension QA,integrate the positive-side shaded function from0top>0. The denominator has no real zero and the exact area is½ln(1+p²). This unscaffolded nonlinear-log recognition is outside the listed affine reciprocal forms;the directly prescribed maximum task is retained separately.')
p3=value('iii-positive-p','sqrt(exp(2)-1)','2.53',351,
 'Conditionally using the area expression from(ii),set½ln(1+p²)=1. The algebra givesp=±√(e²−1),but the positive right-hand region requiresp>0and its diagram placespafterM. The source’s3significant-figure answer2.53agrees. This use is supporting inverse practice because the source does not supply the area formula independently of the extension integral.')
p3['operation']={'kind':'rounded','operands':['sqrt(exp(2)-1)'],'significant_figures':3}
row=add('Exercise-8C',7,208,'For y=x/(x²+1)with a given positive maximum and shaded0..pregion,find the maximum input,its area formula,and pwhen the area is1. Only the maximum part is directly prescribed;the nonlinear-log area and its dependent inverse are audited as supporting extension.',[p,p2,p3],[STATIONARY],[QUOTIENT,CLASSIFY],rep='graph',exam_attribution='Cambridge9709Paper3Q9June2005',precision_note='Part(iii)asks3significant figures. The maximum input is exact;no angle variable occurs.')
row['scope_check'].update(status='in-scope-parts-only',excluded_or_qualified_parts=['ii:unscaffolded nonlinear-log integration beyond the listed affine forms.','iii:depends on the unsupplied extension result from(ii);retain its mathematically valid inverse as supporting evidence.'])
row['direct_demand_aspects']=[{'demand_id':STATIONARY,'assessed_facet':'i only;classification/product skills used analytically are components.'}]
p=value('integral','0','1/3',209,
 'Derivecos3x=cos(2x+x)=cosx−4cosxsin²xfrom the prescribed addition/double-angle identities. Thuscosxsin²x=(cosx−cos3x)/4,a sum of permitted linear-angle trig terms. Integrate exactly over0..π/2to obtain1/3. The worked book uses an optional substitution;the original Find instruction does not require it.')
p['operation']={'kind':'proper-definite-integral','operands':['cos(x)*sin(x)**2','0','pi/2']}
p['additional_operations']={'identity_route':{'kind':'trig-identity-residual','operands':['cos(x)*sin(x)**2','(cos(x)-cos(3*x))/4']},'linear_route_integral':{'kind':'proper-definite-integral','operands':['(cos(x)-cos(3*x))/4','0','pi/2']}}
p['additional_operation_expected']={'identity_route':'0','linear_route_integral':'1/3'}
row=add('Example',11,209,'Find∫₀^(π/2)cosxsin²x dxwithout a forced method. An addition/double-angle identity reduces it to linear trig forms,so the source’s optional substitution does not make the original task outside scope.',[p],[IDENTITY,TRIGINT,DEF],precision_note='Radian bounds0andπ/2;the exact value is1/3.')
row['source_interpretation']={'scope_basis':'SyllabusPDF16/printed13says use trigonometrical relationships such as double-angle formulae,withcos²xas an example rather than an exhaustive list. The exact derived identity demonstrates this particular route;no memorised triple-angle formula or general substitution is required.','review_limit':'This author scope judgement and its complexity remain for independent review/grade-bound comparison;it does not claim the task occurred in NSSCAS.'}
p=indefinite('primitive','cos(x)**3','sin(x)-sin(x)**3/3',209,
 'Derivecos3x=4cos³x−3cosxfrom addition/double-angle identities. Then integratecos³x=(cos3x+3cosx)/4. The resulting sin3x/12+3sinx/4is equivalent to the source’ssinx−sin³x/3up to an arbitrary constant. The source allows inspection;general substitution is optional.')
p['additional_operations']={'identity_route':{'kind':'trig-identity-residual','operands':['cos(x)**3','(cos(3*x)+3*cos(x))/4']},'linear_primitive_derivative':{'kind':'trig-identity-residual','operands':['diff(sin(3*x)/12+3*sin(x)/4,x)','cos(x)**3']}}
p['additional_operation_expected']={'identity_route':'0','linear_primitive_derivative':'0'}
row=add('Example',12,209,'Find∫cos³x dxwithout a forced method. A derived addition/double-angle identity gives a permitted finite linear-trig route;the book’s reverse-chain/inspection route is an alternative.',[p],[IDENTITY,TRIGINT],precision_note='Indefinite radian-angle integration;retain an arbitrary additive constant.')
row['source_interpretation']={'scope_basis':'Do not interpret the syllabus’ssuchascos²xexample as a ban on this explicitly derived finite trig identity route. The harder identity choice is visible for later grade-bound review.'}
parts=[]
for label,f,key,method in [
 ('i','cos(3*x)','sin(3*x)/3','Reverse differentiation ofsin3xrequires the coefficient1/3.'),
 ('ii','sin(1-x)','cos(1-x)','The derivative ofcos(1−x)is+sin(1−x);the negative inner derivative cancels the usual minus sign.'),
 ('iii','sin(x)*cos(x)**3','-cos(x)**4/4','Use permitted identities to rewrite as¼sin2x+⅛sin4x,or the source’s allowed otherwise/inspection route. The derivative of−cos⁴x/4checks the original product.'),
 ('vi','sin(2*x)*(1+cos(2*x))**2','-(1+cos(2*x))**3/6','Expand using double-angle/addition relationships to(5/4)sin2x+sin4x+(1/4)sin6x,then integrate linear terms. This differs from the compact source primitive only by an additive constant.')]:
 parts.append(indefinite(label,f,key,351,method+' The question expressly permitsorotherwise,so no general substitution is mandatory.'))
parts[2]['additional_operations']={'identity_route':{'kind':'trig-identity-residual','operands':['sin(x)*cos(x)**3','sin(2*x)/4+sin(4*x)/8']}}
parts[2]['additional_operation_expected']={'identity_route':'0'}
parts[3]['additional_operations']={'identity_route':{'kind':'trig-identity-residual','operands':['sin(2*x)*(1+cos(2*x))**2','5*sin(2*x)/4+sin(4*x)+sin(6*x)/4']}}
parts[3]['additional_operation_expected']={'identity_route':'0'}
parts[3]['operation']['integration_algorithm']='manual'
row=add('Exercise-8D',1,211,'Integrate the stated expressions using the given substitutionorotherwise. Retaini cos3x,ii sin(1−x),iii sinxcos³x,andvi sin2x(1+cos2x)²via permitted linear/finite identity routes. Partsiv/vlead to nonlinear log-trig primitives.',parts,[TRIGINT,IDENTITY],precision_note='All angles are radians. Indefinite primitives have arbitrary constants;all four retained integrands are continuous onR.')
row['scope_check'].update(status='in-scope-parts-only',excluded_or_qualified_parts=['iv:sinx/(2−cosx)requires a nonlinear-log primitive.','v:tanxrequires a nonlinear-log primitive.'])
row['direct_demand_aspects']=[{'demand_id':TRIGINT,'assessed_facet':'iandii directly;iiiandvi after valid finite identities.'},{'demand_id':IDENTITY,'assessed_facet':'iiiandvi have explicit identity routes;this is not a claim that the optional substitutions are mandatory.'}]
p=value('i','0','1',351,
 'The enlarged source is∫₀^(π/2)cos(2x−π/2)dx,not the earlier boundary note’s different shift/bounds. Direct affine-trig integration gives[½sin(2x−π/2)]₀^(π/2)=1. The original explicitly asks suitable substitutions,an additional method condition which is not erased.')
p['operation']={'kind':'proper-definite-integral','operands':['cos(2*x-pi/2)','0','pi/2']}
p2=value('ii','0','1/16',351,
 'Independently usecosxsin³x=¼sin2x−⅛sin4xfrom permitted identities,then integrate0..π/4to get1/16. The source’s mandatory substitution condition remains additional;the numerical result itself has an in-scope identity route.')
p2['operation']={'kind':'proper-definite-integral','operands':['cos(x)*sin(x)**3','0','pi/4']}
p2['additional_operations']={'identity_route':{'kind':'trig-identity-residual','operands':['cos(x)*sin(x)**3','sin(2*x)/4-sin(4*x)/8']}};p2['additional_operation_expected']={'identity_route':'0'}
row=add('Exercise-8D',3,211,'Only(i)/(ii):the original asks suitable substitutions for∫₀^(π/2)cos(2x−π/2)dxand∫₀^(π/4)cosxsin³x dx. Their values have permitted direct/identity routes,but the explicit extra method is retained;remaining parts are outside listed forms.',[p,p2],teaches=[TRIGINT,IDENTITY,DEF],forced=True,continuation=[212],precision_note='All displayed bounds are radians;the retained results1and1/16are exact.')
row['scope_check']['excluded_or_qualified_parts']+=['iii:nonlinear-angle substitution.','iv:nonlinear exponential-of-tangent primitive.','v:nonlinear log-of-tangent primitive.']

for n,page,label,note,teaches,rep,checks,parent in [
 (17,208,'Exercise8C7maximum and area diagram','The givenx/(x²+1)curve has a positive maximum atx=1and ordinate1/2. The shaded region is0..pwithppictured to the right ofM. Retain the positive/right-hand branch when solving forp;the picture does not justify a negative area-bound solution.',[STATIONARY,AREA],'graph',[('(x/(x**2+1)).subs(x,1)','1/2')],'Exercise-8C:7'),
 (18,209,'Example11squared-sine notation reminder','sin²xmeans(sinx)²,not sin(x²). The two functions have different arguments and cannot share the same integral or graph without a new analysis.',[],'table',[],'Example:11'),
 (19,210,'Example13log-derivative reminder','The reference identifies the top line as the derivative of the bottom line. Its cotangent/log-sine use is nonlinear-log extension,not an extra listed affine integral. Poles/zeros still separate real components.',[],'table',[],None),
 (20,210,'Example13exact cosine values','The callout givescos(π/3)=1/2andcos(π/6)=√3/2. These are exact radian special-angle reference values inside an otherwise extension integral.',[EXACT],'table',[('Tuple(cos(pi/3),cos(pi/6))','Tuple(1/2,sqrt(3)/2)')],None),
 (21,210,'Example13quotient-log callout','The positive-argument identityln(√3/2)−ln(1/2)=ln√3is a logarithm-law reference. It is not evidence that the whole cot/tan integration task is prescribed.',[LAW],'table',[('log(sqrt(3)/2)-log(1/2)-log(sqrt(3))','0')],None),
 (22,210,'Example13power-log callout','ln√3=½ln3uses the power law on a positive real argument. Keep this exact form distinct from an arbitrary rounded decimal.',[LAW],'table',[('log(sqrt(3))-log(3)/2','0')],None)]:fig(n,page,label,note,teaches,rep,checks,parent)
for f in figures:
 f['item_id']=f['item_id'].replace(':C5:',':C8:');f['parent_item_id']=f['parent_item_id'].replace(':C5:',':C8:')if f['parent_item_id']else None;f['source_evidence']=ev(f['pdf_page'])
 f['value_level_scope_decisions']=[{'rule_id':'8227:LIMIT07','status':'not applicable','quoted_value':f['notes'],'reason':'A given graph or supporting mathematical reference does not impose a general substitution response.'}]
pages=[]
notes={208:'8C7is split by prescribed maximum versus extension integral/dependent inverse.8C8forces radical substitution and then an extra rational integration method. Example10has an unscaffolded nonlinear trig argument;no prescribed task is inferred from it.',209:'Examples11/12are unforced and admit explicit finite identity routes. The squared-sine notation callout is recorded. Their optional substitution solutions do not impose that method on the original task.',210:'Example13cot/tan integration is nonlinear-log extension;its exact-angle/log-law callouts are retained separately. The note encouraging inspection does not make every such primitive a prescribed form.',211:'Example14and its inverse-tan calculus references are excluded.8D1retained parts expressly alloworotherwise;iv/vremain nonlinear-log extension.8D2requires suitable substitutions.8D3(i)/(ii)are retained as mathematical boundary evidence with the original extra method;partsiii–vcontinue on212and remain excluded.'}
for page in range(208,212):
 pages.append({'pdf_page':page,'printed_page':page-14,'chapter':8,'page_status':'items enumerated','item_ids':[r['item_id']for r in answers if r['source_pdf_page']==page]+[r['item_id']for r in figures if r['pdf_page']==page],
  'continuation_item_ids':[],'source_evidence':ev(page),'reader':'Codex author','date':'2026-11-18','non_item_content':notes[page],'scope_screen':'Unforced identity routes,explicit required methods and nonlinear/inverse-trig forms are separated using the rendered syllabusPDF16.'})
if __name__=='__main__':
 for name,data in [('answers-Goldie-C8-trig-opening.json',{'scope':'Every retained8C7,Examples11/12,8D1and8D3(i)/(ii)response,with original method conditions.','items':answers}),('census-Goldie-C8-trig-opening.json',{'book':'Goldie','book_id':'8227-SRC-015','chapter':8,'source_path':SRC,'source_sha256':SHA,'scope':'Complete208–211source census,including every retained reference/given figure.','new_items':new+figures,'corrections':[],'pages':pages})]:
  (W/'tools/textbook-r5'/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
 for r in answers:
  for p in r['subparts']:
   if 'operation'in p:
    got=compute(p['operation']);expected=expression(p['printed_key_normalised'])
    assert primitive_agrees(p['operation'],got,expected)if p.get('answer_equivalence')=='up-to-additive-constant'else equivalent(got,expected),(r['item_id'],p['subpart'],got)
   for name,op in p.get('additional_operations',{}).items():assert equivalent(compute(op),expression(p['additional_operation_expected'][name])),(r['item_id'],name)
 print(len(answers),'items;',sum(len(r['subparts'])for r in answers),'outputs;',len(figures),'figures')
