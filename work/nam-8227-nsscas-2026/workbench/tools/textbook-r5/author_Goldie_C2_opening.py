"""Every opening task and figure,Goldie PDF38–40;Example1continues41."""
import hashlib,json
from author_Goldie_C5_opening import W,SRC,SHA,value,reasoning,compute,expression,equivalent
SKETCH='8227:2020:M1:T3:O05:D01';INTERSECT='8227:2020:M1:T4:O02:D01';GPMODEL='8227:2020:M1:T2:O03:D03';GP='8227:2020:M1:T2:O03:D02';EXPI='8227:2020:M2:T2:O03:D02'
def ev(page):
 name='Goldie-key-C2-335'if page>=335 else'Goldie-C2-38'
 p=W/f'checks/r5/textbooks/{name}.png';return {'path':str(p.relative_to(W.parents[2])),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
answers=[];new=[];corrections=[]
def add(kind,n,page,note,parts,direct,components=None,rep='text',sketch=False,new_kind=None):
 for p in parts:
  kp=p.pop('key_page_override',335);p.update(source_pdf_page=page,source_evidence=ev(page),answer_pdf_page=kp,answer_printed_page=kp-14 if kp else None,key_evidence=ev(kp or 335),review_date='2026-11-18')
  if kp is None:p.update(key_presence='no separate key',inspected_key_pdf_pages=[335,336])
 row={'item_id':f'8227:TB:Goldie:C2:{kind}:{n}','source_pdf_page':page,'notes':note,'assessed_8227_demand_ids':direct,'component_demand_ids':components or[],
  'mapping_rationale':'Record the actual model term/threshold,graph-intersection or sketch demand. Being in a logarithm chapter does not make ordinary power evaluation a log-law assessment. Global parameter claims retain real-base and variable domains.',
  'representation':rep,'sketch_response_required':sketch,'exam_style':False,'exam_style_basis':'Unattributed opening prompt,activity or example.',
  'value_level_scope_decisions':[{'rule_id':'8227:QUAL07','status':'within','quoted_value':note,'reason':'Simple exponential/monomial graph or contextual domain,with real inputs and explicit physical-time restrictions. General-all-a exploration is separately qualified.'}],
  'precision_angle_check':{'source':'Cell counts and elapsed whole days are discrete;cost model time is continuous and nonnegative. Exact intersections/feature formulas are kept before any approximate auxiliary roots.',
   'comparison':'Do not turn a rounded continuous threshold into an exact discrete count,or infer a full real-domain inequality from an unstated positive-domain graph convention.'},
  'expected_subpart_labels':[p['subpart']for p in parts],'subparts':parts};answers.append(row)
 if new_kind:new.append({'item_id':row['item_id'],'item_kind':new_kind,'exercise':kind,'item_number':str(n),'pdf_page':page,'printed_page':page-14,'notes':note,'assessed_8227_demand_ids':direct,'component_demand_ids':components or[],'representation':rep,'source_evidence':ev(page),'learner_display':False})
 return row
p=value('five-days','2**5','32',335,'One initial cell doubles once per whole day,so the day-ncount is2^n.')
p2=value('ten-days','2**10','1024',335,'Use the same initial day0count and exactly ten doublings.')
p3=value('million-threshold','ceiling(log(1000000)/log(2))','20',335,'The continuous solution is about19.9316days,but exact daily doubling gives integer counts. Twenty is the first whole day with at least one million;there is no day with exactly1,000,000cells in this idealised model.')
p3['assertions']=[{'expression':'Tuple(2**19<1000000,2**20>=1000000)','expected':'Tuple(True,True)'}]
row=add('Prompt',1,38,'Under the stated idealised daily-doubling/no-deaths assumptions,find the cell counts after5and10days and an approximate million-cell time. Preserve the day0initial count and the discrete-day interpretation.',[p,p2,p3],[GPMODEL,GP,EXPI])
row['direct_demand_aspects']=[{'demand_id':GP,'assessed_facet':'Geometric term values,not a finite-sum question.'},{'demand_id':EXPI,'assessed_facet':'First whole-day threshold;does not automatically cover every exponential inequality form.'}]
p=value('i-a','Tuple(Tuple(2,2**2),Tuple(4,2**4))','Tuple(Tuple(2,4),Tuple(4,16))',335,'Check both labelled positive-graph intersections in the original2^xandx²,not just their x-coordinates.')
p['assertions']=[{'expression':'Tuple((2**x-x**2).subs(x,2),(2**x-x**2).subs(x,4))','expected':'Tuple(0,0)'}]
p2=reasoning('i-b','On the intended positive domain,the answer is0<x<2orx>4. On all realx,it isr<x<2orx>4,where r≈−0.766665,and0is included.',
 'The source key explicitly gives the positive-domain answer,but the stem does not statex>0. The given figure displays the nonnegative side. On the full real domain,there is a further negative intersection and2^0>0². Record the intended-domain interpretation and the complete real-domain alternative as a question-domain ambiguity,not a silent universal claim.',335,'key incomplete')
p2['additional_operations']={'negative_intersection':{'kind':'bracketed-source-root','operands':['2**x-x**2','-1','0'],'rounding':{'decimal_places':6}},'zero_comparison':{'kind':'identity','operands':['2**0-0**2']}}
p2['additional_operation_expected']={'negative_intersection':'-0.766665','zero_comparison':'1'}
p3=reasoning('ii-a','For3^xandx³:exponential positive/convex with intercept1;cubic odd with intercept0;two positive intersections,one near2.478and the exact(3,27). No negative intersection.',
 'Forx≤0,the cubic is nonpositive and the exponential is positive. For positivex,the intersection condition islnx/x=ln3/3;the left side rises to its unique maximum ateandthen falls,so there are two positive intersections. Check the lower one on[2,2.7]and the exact one3. These are author-derived software-sketch features;the key supplies no separate graphs.',None,'no key')
p3['additional_operations']={'lower_positive_crossing':{'kind':'bracketed-source-root','operands':['3**x-x**3','2','27/10'],'rounding':{'decimal_places':3}},'exact_upper_crossing':{'kind':'identity','operands':['3**3-3**3']}}
p3['additional_operation_expected']={'lower_positive_crossing':'2.478','exact_upper_crossing':'0'}
p4=reasoning('ii-b','For4^xandx⁴:the quartic is even with minimumO;the exponential has intercept1. The full real graph has a negative crossing r≈−0.766665and positive crossings(2,16),(4,256).',
 'Both functions are nonnegative,so4^x=x⁴is equivalent to(2^x)²=(x²)²,and hence2^x=x². Reuse the independently checked crossing set;do not omit the negative branch when asking for a full real graph. On the source’s positive plotting convention only the two positive crossings appear.',None,'no key')
p4['additional_operations']={'square_equivalence':{'kind':'identity','operands':['expand((2**x)**2-(x**2)**2)-(4**x-x**4)']},'positive_crossings':{'kind':'identity','operands':['Tuple(4**2-2**4,4**4-4**4)']}}
p4['additional_operation_expected']={'square_equivalence':'0','positive_crossings':'Tuple(0,0)'}
p5=reasoning('iii-a','Yes,for every admissible positive basea,the two expressions agree atx=a:both equala^a.',
 'Substitute the same value intoa^xandx^a. Negative bases are not real exponential functions for arbitrary realx,and0^0is not part of the usual definition. Statea>0rather than extending the verbal claim to undefined cases.',335,'matches')
p6=reasoning('iii-b','No,not for all admissible positivea. For examplea=½gives(½)^x<√xfor everyx≥1.',
 'Forx≥1,(½)^x≤½while√x≥1,so there is no eventual dominance of the exponential in that case. For fixeda>1,the exponential eventually dominates the power,but that conditional statement is different from the source’s all-aquantifier. The source key’sNois correct.',335,'matches')
p6['additional_operations']={'counterexample_at_one':{'kind':'identity','operands':['Tuple((1/2)**1,sqrt(1))']}}
p6['additional_operation_expected']={'counterexample_at_one':'Tuple(1/2,1)'}
row=add('Activity',1,39,'Read the given2^x/x²intersections and ordering,draw3^x/x³and4^x/x⁴using software if available,and test the two general-a assertions. The positive plotting convention and valid exponential-base domain must be explicit.',[p,p2,p3,p4,p5,p6],[SKETCH,INTERSECT],rep='graph',sketch=True)
row['scope_check']={'status':'in-scope-parts-only','basis':'Given/simple graph comparison is relevant;general-all-parameter dominance is supporting exploration and the original inequality domain is ambiguous.','excluded_or_qualified_parts':['i-b:state the intended positive domain or the full-real alternative','iii:general-parameter exploration is supporting breadth,not a new prescribed asymptotic theorem']}
# The boxed transformation prompt on40was absent from the prior population;IDs2/3already belong47/59.
p=reasoning('i','A vertical translation bykhas asymptotey=kand y-intercept(0,1+k). The source key’s(0,k)misses the original1.',
 'For either original curvea^xora^(−x),the value at0is1. Addingkaddsktothat value. The symbolic base2counterexample has(2^0+k)=1+k,whereas the printed point usesk. The asymptote statement is correct.',335,'key wrong')
p['additional_operations']={'translated_features':{'kind':'identity','operands':['Tuple(limit(2**x+k,x,-oo),(2**x+k).subs(x,0))']}}
p['additional_operation_expected']={'translated_features':'Tuple(k,k+1)'}
p2=reasoning('ii','Translating right byhpreserves asymptotey=0and moves the point(0,1)to(h,1);the new y-intercepts area^(−h)anda^hfor the two orientations.',
 'Replace xbyx−h. The moved point need not remain on the y-axis. The source key correctly gives the image point(k,1),not a new y-intercept. This distinction prevents a false key-error report.',335,'matches')
p3=reasoning('iii','A horizontal stretch by positivespreserves the point(0,1)and asymptotey=0;the input becomesx/s.',
 'Atx=0,the exponent remains0. A positive finite horizontal scale preserves the corresponding infinite-end limit. A zero scale is not an ordinary stretch,and a negative scale additionally reflects orientation.',335,'matches')
p4=reasoning('iv','A vertical stretch by nonzerovhas y-intercept(0,v)and asymptotey=0.',
 'Multiply the original function byv. At0,the result isv. A nonzero finite factor preserves a zero asymptotic limit;v<0reflects vertically. The zero-factor constant function is a separate degeneracy,not a renewable ordinary stretch.',335,'matches')
row=add('Prompt',4,40,'Explain how the asymptote and marked point ofa^x/a^(−x)change under vertical/horizontal translations and stretches. Distinguish the image of a marked point from a y-intercept;retain positive-base/nonzero-scale conditions.',[p,p2,p3,p4],[SKETCH],new_kind='prompt')
p=value('i','(10+20*2**(-x)).subs(x,0)','30',41,'Evaluate the supplied cost function at the initial time0;the model’s currency is the source dollar sign.');p['units']='$';p['printed_key_units']='$'
p2=value('ii','limit(10+20*2**(-x),x,oo)','10',41,'The decaying term tends to0,so the cost approaches the fixed lower level10rather than0.');p2['units']='$';p2['printed_key_units']='$'
p3=reasoning('iii','Fort≥0,sketch a decreasing convex curve fromC=30toward horizontal asymptoteC=10,without reaching it at finite time.',
 'The exponential factor2^(−t)is positive and decreasing. The cost curve remains strictly above10;the physical years-after-production domain begins0. The source sketch agrees with the intercept and limiting cost.',41,'sketch')
row=add('Example',1,40,'Given machine costC=10+20·2^(−t),find its initial value,large-time behaviour and a sketch on the physicaldomaint≥0. This is evaluation/graph interpretation,not solving an exponential equation.',[p,p2,p3],[SKETCH],rep='text',sketch=True)
row['component_demand_roles']=[{'role':'prerequisite integer-index arithmetic and direct formula evaluation','demand_ids':[],'reason':'No invented8227log-law demand for evaluating a supplied power.'}]
corrections.append({'item_id':row['item_id'],'continuation_pdf_pages':[41]})
from author_Goldie_C5_opening import fig,figures
figures.clear()
for n,page,label,note,rep,checks,parent in [
 (1,39,'Figure2.1 given exponential/monomial comparison','The displayed positive-side curves2^xandx²cross atA=(2,4),B=(4,16). The drawing does not by itself define a full real-domain inequality answer;the negative intersection matters if all realxare allowed.','graph',[('Tuple(2**2-2**2,2**4-4**2)','Tuple(0,0)')],'Activity:1'),
 (2,39,'Figure2.2 exponential graphs and overgeneralised prose','The shown2^xand3^xcurves pass(0,1),increase convexly,and have asymptotey=0. The nearby claim extends this intercept toallka^xwitha>1,but its actual intercept isk;positivity ofkis also needed for the increasing-convex direction.','graph',[('Tuple((k*2**x).subs(x,0),diff(k*2**x,x,2))','Tuple(k,k*2**x*log(2)**2)')],None),
 (3,40,'Figure2.3 negative-input reflection','Graphsy=2^xandy=2^(−x)are reflections in they-axis,share(0,1)and asymptotey=0at opposite infinite ends.','graph',[('(2**x).subs(x,-x)-2**(-x)','0')],None),
 (4,41,'Figure2.4 cost-model solution graph','ForC=10+20·2^(−t),t≥0,the source graph starts(0,30),decreases towardC=10and stays above that asymptote. The time and cost axes must remain consistent with the same formula.','graph',[('Tuple((10+20*2**(-x)).subs(x,0),limit(10+20*2**(-x),x,oo))','Tuple(30,10)')],'Example:1')]:
 fig(n,page,label,note,[SKETCH],rep,checks,parent)
for f in figures:f['item_id']=f['item_id'].replace(':C5:',':C2:');f['parent_item_id']=f['parent_item_id'].replace(':C5:',':C2:')if f['parent_item_id']else None;f['source_evidence']=ev(f['pdf_page'])
pages=[]
for page in range(38,41):
 pages.append({'pdf_page':page,'printed_page':page-14,'chapter':2,'page_status':'items enumerated','item_ids':[r['item_id']for r in answers if r['source_pdf_page']==page]+[r['item_id']for r in figures if r['pdf_page']==page],
  'continuation_item_ids':[],'source_evidence':ev(page),'reader':'Codex author','date':'2026-11-18','non_item_content':'Every posed opening task,missing transformation prompt,example and teaching graph recorded. The microscopy photograph is illustrative context,not a countable given for the doubling problem. Page41awaits combined2Acensus.'})
if __name__=='__main__':
 for name,data in [('answers-Goldie-C2-opening.json',{'scope':'Complete opening tasks and Example1response;physical/discrete/base domains explicit.','items':answers}),('census-Goldie-C2-opening.json',{'book':'Goldie','book_id':'8227-SRC-015','chapter':2,'source_path':SRC,'source_sha256':SHA,'scope':'Complete38–40;Example1andfigure4continue41pending2Acensus.','new_items':new+figures,'corrections':corrections,'pages':pages})]:
  (W/'tools/textbook-r5'/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
 for row in answers:
  for p in row['subparts']:
   if 'operation'in p:
    got=compute(p['operation']);assert equivalent(got,expression(p['printed_key_normalised'])),(row['item_id'],p['subpart'],got)
   for name,op in p.get('additional_operations',{}).items():assert equivalent(compute(op),expression(p['additional_operation_expected'][name])),(row['item_id'],name)
 print(len(answers),'items;',sum(len(r['subparts'])for r in answers),'outputs;',len(figures),'figures;newPrompt4')
