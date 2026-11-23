"""Retained graph,calculus and numerical-equation parts in223–226."""
import json
from author_Goldie_C8_opening import W,SRC,SHA,add,answers,new,ev,fig,figures,value,reasoning,compute,expression,equivalent,AREA,DEF
from source_iteration_trace_r5 import trace
answers.clear();new.clear();figures.clear()
SKETCH='8227:2020:M1:T3:O05:D01';STAT='8227:2020:M1:T8:O04:D01';TANGENT='8227:2020:M1:T8:O03:D01'
ELEMENTARY='8227:2020:M2:T4:O01:D02';PRODUCT='8227:2020:M2:T4:O02:D01'
ROOTG='8227:2020:M2:T6:O01:D01';BRACKET='8227:2020:M2:T6:O01:D02';ITERATE='8227:2020:M2:T6:O04:D01';STOP='8227:2020:M2:T6:O04:D02'
def v(label,op,key,method,page=353):
 p=value(label,'0',key,page,method);p['operation']=op;return p
def dep(p,source,cue,role):p['source_dependency_edges']=[{'from':source,'type':'cue','cue':cue,'role':role}]
def partial(row,excluded):
 row['scope_check'].update(status='in-scope-parts-only',excluded_or_qualified_parts=excluded);return row

f='(2-x)*exp(-x)'
p=v('i-intercepts',{'kind':'identity','operands':[f'Tuple(solve({f},x)[0],({f}).subs(x,0))']},'Tuple(2,2)',
 'The exponential is strictly positive,so the sole xintercept is(2,0);the yintercept is(0,2). The response stores their two nonzero coordinate values in that order.')
p2=reasoning('ii-sketch','Draw the continuous curve through(0,2)and(2,0),decreasing to a minimum(3,−e^(−3)),then increasing towardy=0from below.',
 'The derivative is(x−3)e^(−x),so its sign changes only at3. Asx→−∞the curve rises without bound;asx→∞it tends to0from below. The source key shows the intercepts,bounded right-hand minimum and the right asymptotic approach. The requested sketch is of the original full real-domain formula;no artificial endpoint at2is introduced.',353,'sketch')
p2['additional_operations']={'derivative':{'kind':'identity','operands':[f'diff({f},x)']},'stationary_ordinate':{'kind':'identity','operands':[f'({f}).subs(x,3)']},'right_limit':{'kind':'identity','operands':[f'limit({f},x,oo)']}}
p2['additional_operation_expected']={'derivative':'(x-3)*exp(-x)','stationary_ordinate':'-exp(-3)','right_limit':'0'};dep(p2,'i-intercepts','Hence sketch','Use both axis intercepts;source provides no official sketch-award table here.')
p3=v('iii-area',{'kind':'proper-definite-integral','operands':[f,'0','2']},'1+exp(-2)',
 'The bounded first-quadrant region is0≤x≤2. Its exact positive area is1+e^(−2),as independently checked from the original curve. The original explicitly requires integration by parts;that additional method is not erased by retaining the prescribed sketch and intercept parts.')
row=partial(add('Exercise-8G',2,224,'Find both axis intercepts and hence sketch(2−x)e^(−x),then use the explicitly required parts method for its first-quadrant area. Intercepts/sketch are prescribed;the area result is supporting QA with the original method condition intact.',[p,p2,p3],[SKETCH],rep='graph'),['iii:explicit integration-by-parts requirement.'])
row['sketch_response_required']=True;row['direct_demand_aspects']=[{'demand_id':SKETCH,'assessed_facet':'iandii:intercepts and full curve sketch;not the forced method iniii.'}]

p=reasoning('i-sketch-shade','On0≤x≤π,sketch one positive lobe ofy=xsinxwith zeros at0andπ,and shade the region between the curve and the xaxis.',
 'The sine is positive in the open interval,so the whole requested region is above the axis. At0the slope is0;atπit is−π. The derivative sinx+xcosxis positive on(0,π/2). On(π/2,π),its sole zero satisfies tanx=−x,since tanx+xstrictly increases from−∞toπ. Thus the lobe has one maximum. The key depicts that shape without an exact peak coordinate requirement.',353,'sketch')
p['additional_operations']={'endpoints':{'kind':'identity','operands':['Tuple((x*sin(x)).subs(x,0),(x*sin(x)).subs(x,pi))']},'endpoint_gradients':{'kind':'identity','operands':['Tuple(diff(x*sin(x),x).subs(x,0),diff(x*sin(x),x).subs(x,pi))']}};p['additional_operation_expected']={'endpoints':'Tuple(0,0)','endpoint_gradients':'Tuple(0,-pi)'}
p2=v('ii-area',{'kind':'proper-definite-integral','operands':['x*sin(x)','0','pi']},'pi',
 'The positive area equals the proper integral on0..π. Its primitive−xcosx+sinxgivesπ. The source forces integration by parts;the result is checked internally without changing that original method demand.')
row=partial(add('Exercise-8G',3,224,'Sketchxsinxon0..πand shade its positive area,then calculate that area using the required integration-by-parts method. The sketch is prescribed;the method-specific integral is additional.',[p,p2],[SKETCH],rep='graph'),['ii:explicit integration by parts.']);row['sketch_response_required']=True

parts=[]
for label,method in [('i-parts','The original explicitly requires integration by parts.'),('ii-named-substitution','The original explicitly requiresu=x+1.')]:
 p=v(label,{'kind':'proper-definite-integral','operands':['-x*sqrt(x+1)','-1','0']},'Rational(4,15)',
  'The curve is below the xaxis on−1<x<0,so geometric area is minus its signed integral. Rewrite x=(x+1)−1and integrate linear powers to independently obtain4/15. '+method+' Both original method requirements remain additional;the valid direct rewrite does not silently replace them.')
 parts.append(p)
row=partial(add('Exercise-8G',6,224,'Find the area bounded by the negative xaxis andx√(x+1),first by parts and then by the namedu=x+1substitution. Both outputs equal4/15and are supporting method-boundary evidence.',parts,teaches=[AREA],forced=True,precision_note='Real interval−1..0;the finite zero at−1is not an integrand pole. The area is exact and positive.'),['Both source responses force additional methods;the direct linear-power rewrite is an independent author check.'])
row['value_level_scope_decisions'][0].update(quoted_value='(i)using integration by parts;(ii)using the substitutionu=x+1.',reason='Both explicit source methods remain additional even though direct linear-power integration can verify the mathematical area.')

p=reasoning('i-fixed-point-equation','The stated integral condition impliesa=2+e^(−a/2).',
 'For supporting QA,∫₀ᵃxe^(x/2)dx=(2a−4)e^(a/2)+4. Setting this to6gives(a−2)e^(a/2)=1,and division by the positive exponential gives the displayed fixed-point equation. Deriving this unscaffolded product integral is extra. The equation itself is explicitly printed as the result to use in later parts.',225,'show/prove')
p['additional_operations']={'candidate_primitive':{'kind':'identity','operands':['diff((2*x-4)*exp(x/2),x)-x*exp(x/2)']},'fixed_point_rearrangement':{'kind':'identity','operands':['((2*x-4)*exp(x/2)+4-6)/(2*exp(x/2))-(x-2-exp(-x/2))']}};p['additional_operation_expected']={'candidate_primitive':'0','fixed_point_rearrangement':'0'}
p2=reasoning('ii-unique-root-sketch','Sketch the increasing liney=xand strictly decreasingy=2+e^(−x/2);they intersect exactly once,between2and2.5.',
 'Forx≤2,the exponential curve is strictly above2≥x,so there is no intersection there. Onx>2the line increases and the other curve decreases towardy=2. Their differencex−2−e^(−x/2)has strictly positive derivative1+½e^(−x/2). Its signs at2and2.5are opposite,so continuity gives one intersection and monotonicity gives uniqueness. The source key shows these two graphs,including exponential intercept3.',353,'sketch')
p2['additional_operations']={'exp_intercept':{'kind':'identity','operands':['(2+exp(-x/2)).subs(x,0)']},'derivative_difference':{'kind':'identity','operands':['diff(x-2-exp(-x/2),x)']}};p2['additional_operation_expected']={'exp_intercept':'3','derivative_difference':'1+exp(-x/2)/2'}
dep(p2,'i-fixed-point-equation','this equation','Use the displayed result,without needing to reproduce the extra integral method.')
p3=reasoning('iii-bracket','ForF(x)=x−2−e^(−x/2),F(2)=−e^(−1)<0andF(2.5)=½−e^(−5/4)>0;the continuous root lies between2and2.5.',
 'Both endpoints are in the full real domain;the sign change and continuity certify a root. Part(ii)provides the separate uniqueness argument. Opposite endpoint signs alone would not prove uniqueness.',225,'show/prove')
p3['additional_operations']={'endpoint_signs':{'kind':'identity','operands':['Tuple(sign((x-2-exp(-x/2)).subs(x,2)),sign((x-2-exp(-x/2)).subs(x,Rational(5,2))))']}};p3['additional_operation_expected']={'endpoint_signs':'Tuple(-1,1)'}
p4=v('iv-iteration',{'kind':'bracketed-source-root','operands':['x-2-exp(-x/2)','2','5/2'],'rounding':{'decimal_places':2}},'2.31',
 'Execute the explicitly supplied fixed-point relationxₙ₊₁=2+e^(−xₙ/2). The source does not prescribe a start;this trace labels the author startx₀=2. Keep full internal states,display each iterate to4decimal places,and certify the final2decimal-place cell against the original fixed-point residual. A separate bracketed root and Ridder comparison check the final answer.')
p4['iteration_trace']=trace('2+exp(-x/2)','2','x-2-exp(-x/2)','2','5/2',2,4)
dep(p4,'i-fixed-point-equation','based on the equation in part(i)','The equation is given explicitly;no new rearrangement need be selected.')
row=partial(add('Exercise-8G',9,225,'The integral condition leads to the printed fixed-point equationx=2+e^(−x/2). Retain its graph/uniqueness proof,2..2.5bracket and supplied iteration with4decimal-place displays and2decimal-place answer;the initial product integration remains extra.',[p,p2,p3,p4],[ROOTG,BRACKET,ITERATE,STOP],rep='graph',exam_attribution='Cambridge9709Paper3Q9November2008',precision_note='Part(iv)requires each iteration to4decimal places andato2decimal places. The full-precision internal trace and final rounding-cell certificate are recorded separately.'),['i:unscaffolded product integration;ii–ivuse its explicitly printed target equation.'])
row['sketch_response_required']=True

f='exp(-x/2)*sqrt(1+2*x)'
p=v('i-maximum-input',{'kind':'identity','operands':[f'solve(diff({f},x),x)[0]']},'Rational(1,2)',
 'The real domain isx≥−1/2. On its interior,the derivative ise^(−x/2)(1−2x)/(2√(1+2x)),with sole zerox=1/2. It is positive before1/2and negative afterwards. The curve is0at−1/2and tends to0asx→∞,so this point is the global maximum.')
p2=v('ii-volume',{'kind':'proper-definite-integral','operands':['pi*(1+2*x)*exp(-x)','-1/2','0']},'pi*(2*sqrt(E)-3)',
 'The source regionRlies betweenx=−1/2and0,to the left of the yaxis. Rotating about the xaxis givesπ∫_(−1/2)^0y²dxwithy²=(1+2x)e^(−x). Its exact value isπ(2√e−3). This unscaffolded polynomial-exponential integration is additional,while the volume setup and given geometry remain valuable supporting evidence.')
row=partial(add('Exercise-8G',10,225,'Find the maximum input ofe^(−x/2)√(1+2x),then rotate the given left-of-axis regionRabout the xaxis. Retain the maximum directly;the volume result/setup is internally checked with the extra product-integration demand explicit.',[p,p2],[STAT],[PRODUCT,ELEMENTARY],rep='graph',exam_attribution='Cambridge9709Paper3Q9June2008'),['ii:unscaffolded polynomial-exponential integration after the prescribed volume setup.'])
row['value_level_scope_decisions'].append({'rule_id':'8227:QUAL06','status':'within','parts':['ii-setup'],'quoted_value':'Rrotated completely about the xaxis;−1/2≤x≤0.','reason':'The rotation axis is a coordinate axis. The separate integration-method extension is not an axis restriction.'})

f='3*x*exp(-2*x)'
p=v('i-derivative-value',{'kind':'identity','operands':[f'diff({f},x).subs(x,-Rational(1,2))']},'6*E',
 'Differentiate the original product to3e^(−2x)(1−2x)and only then substitute−1/2. The exact derivative value is6e;there is no implicit or parametric differentiation here.')
p2=v('ii-signed-integral',{'kind':'proper-definite-integral','operands':[f,'-1/2','0']},'-Rational(3,4)',
 'The original function is negative on−1/2<x<0,so the requested signed integral is negative. Its exact value is−3/4. The unscaffolded polynomial-exponential primitive is additional;do not replace the signed answer by positive area3/4.')
row=partial(add('Exercise-8G',11,225,'Forf(x)=3xe^(−2x),evaluatef′(−1/2)exactly and separately integrateffrom−1/2to0. The derivative is directly prescribed;the unscaffolded product integral is retained as supporting QA.',[p,p2],[PRODUCT],exam_attribution='Cambridge9709Paper33Q5November2012'),['ii:unscaffolded product integration;the source requests a derivative value in(i),not a given primitive for(ii).'])

f='sqrt(x)*log(x)'
p=v('i-tangent',{'kind':'identity','operands':[f'simplify(({f}).subs(x,1)+diff({f},x).subs(x,1)*(x-1))']},'x-1',
 'On the original domainx>0,the curve passes through(1,0). Its derivative ln(x)/(2√x)+1/√xhas value1atx=1. Thus the tangent isy=x−1,in the requestedmx+cform.')
p2=v('ii-volume',{'kind':'proper-definite-integral','operands':['pi*x*log(x)**2','1','E']},'pi*(E**2-2)/4',
 'The shaded region is1≤x≤eabove the xaxis,so xaxis rotation givesπ∫₁ᵉxln²x dx. Direct independent integration givesπ(e²−1)/4;the source key incorrectly printsπ(e²−2)/4. The squared logarithm needs extra unscaffolded integration methods;the prescribed tangent in(i)is independent of that demand.')
p2['known_source_defect']='TB-Goldie-C8-8G12-VOLUME-KEY';p2['author_correct_normalised']='pi*(E**2-1)/4'
p2['additional_operations']={'primitive_derivative':{'kind':'identity','operands':['diff(pi*x**2*(log(x)**2/2-log(x)/2+Rational(1,4)),x)-pi*x*log(x)**2']}};p2['additional_operation_expected']={'primitive_derivative':'0'}
row=partial(add('Exercise-8G',12,226,'Find themx+ctangent to√xlnxatx=1,and then the volume when the given shaded region1..eis rotated about the xaxis. The tangent is prescribed;the volume is internal method-boundary evidence.',[p,p2],[TANGENT],[PRODUCT],rep='graph',exam_attribution='Cambridge9709Paper32Q9June2012'),['ii:unscaffolded logarithmic product integration.'])
row['value_level_scope_decisions'].append({'rule_id':'8227:QUAL06','status':'within','parts':['ii-setup'],'quoted_value':'Rbetween the curve,the xaxis andx=e,rotated about the xaxis.','reason':'The axis is permitted. Its extra integration method is a separate limitation.'})

for n,page,label,note,teaches,checks,parent in [
 (31,223,'Figure8.6 area underxcosx','The region is0≤x≤π/2underxcosxand above the xaxis. Both endpoint heights are0and it is positive inside. The original unscaffolded product integral is extra;the bounded-region representation is retained.',[AREA],[('Tuple((x*cos(x)).subs(x,0),(x*cos(x)).subs(x,pi/2))','Tuple(0,0)')],None),
 (32,225,'Exercise8G10 left-side region and maximum','The domain starts at−1/2,where the curve is0. Its yintercept is1;maximum input1/2is to the right of the yaxis. RegionRfor rotation is the separate left-side area−1/2..0,not the region up to the maximum.',[STAT,AREA],[('Tuple((exp(-x/2)*sqrt(1+2*x)).subs(x,-Rational(1,2)),(exp(-x/2)*sqrt(1+2*x)).subs(x,0))','Tuple(0,1)')],'Exercise-8G:10'),
 (33,226,'Exercise8G12 logarithmic curve and shaded region','The curve√xlnxis defined forx>0,crosses the xaxis at1,and is positive on1..e. Only that positive bounded regionRrotates about the xaxis. The negative left lobe is not part ofR.',[TANGENT,AREA],[('Tuple((sqrt(x)*log(x)).subs(x,1),(sqrt(x)*log(x)).subs(x,E))','Tuple(0,sqrt(E))')],'Exercise-8G:12')]:
 fig(n,page,label,note,teaches,'graph',checks,parent)
for f in figures:
 f['item_id']=f['item_id'].replace(':C5:',':C8:');f['parent_item_id']=f['parent_item_id'].replace(':C5:',':C8:')if f['parent_item_id']else None;f['source_evidence']=ev(f['pdf_page']);f['value_level_scope_decisions']=[{'rule_id':'8227:LIMIT07','status':'not applicable','quoted_value':f['notes'],'reason':'The given/reference figure does not itself mandate a general integration method.'}]
notes={223:'Example8.22unscaffolded product integration is excluded. Example8.23also needs parts,but Figure8.6is retained as a region/representation reference;its solution continues224.',224:'8G1,4,5are unscaffolded product/logarithmic integrals;8G7uses inverse-tan.8G2/3retain the independently requested intercepts/sketches.8G6has both required methods recorded as additional with an independent linear-power check.',225:'8G8requires logarithmic parts integration.8G9retains the explicitly given fixed-point equation’s graph,bracket and iteration.8G10/11retain independent maximum/derivative parts;their extra integrals are checked as supporting evidence. The given8G10diagram is recorded.',226:'8G12splits its prescribed tangent from extra logarithmic-product integration;its given region figure is recorded. The following general method-choice prompt belongs to the closing-section census and is linked here.'}
pages=[]
for page in range(223,227):
 ids=[r['item_id']for r in answers if r['source_pdf_page']==page]+[r['item_id']for r in figures if r['pdf_page']==page]
 if page==226:ids.append('8227:TB:Goldie:C8:Prompt:6')
 pages.append({'pdf_page':page,'printed_page':page-14,'chapter':8,'page_status':'items enumerated','item_ids':ids,'continuation_item_ids':[],'source_evidence':ev(page),'reader':'Codex author','date':'2026-11-18','non_item_content':notes[page],'scope_screen':'All independently prescribed parts survive;extra source integration methods remain explicit.'})
if __name__=='__main__':
 for name,data in [('answers-Goldie-C8-8G.json',{'scope':'Every retained8G2/3/6/9/10/11/12response;prescribed versus extra methods explicit.','items':answers}),('census-Goldie-C8-8G.json',{'book':'Goldie','book_id':'8227-SRC-015','chapter':8,'source_path':SRC,'source_sha256':SHA,'scope':'Complete223–226with the closing Prompt6linked from its own builder.','new_items':new+figures,'corrections':[],'pages':pages})]:
  (W/'tools/textbook-r5'/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
 for r in answers:
  for p in r['subparts']:
   if 'operation'in p:
    got=compute(p['operation'])
    if p.get('known_source_defect'):
     assert not equivalent(got,expression(p['printed_key_normalised']))and equivalent(got,expression(p['author_correct_normalised'])),(r['item_id'],p['subpart'],got)
    else:assert equivalent(got,expression(p['printed_key_normalised'])),(r['item_id'],p['subpart'],got)
   for name,op in p.get('additional_operations',{}).items():assert equivalent(compute(op),expression(p['additional_operation_expected'][name])),(r['item_id'],name)
 print(len(answers),'items;',sum(len(r['subparts'])for r in answers),'outputs;',len(figures),'figures')
