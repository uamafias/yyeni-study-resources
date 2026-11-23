"""Complete numerical exposition/boxed prompts and combined PDF147–151 census."""
import hashlib,json
from author_Goldie_C5_opening import W,SRC,SHA,value,reasoning,compute,expression,equivalent
from author_Goldie_C5_5C import trapez,TRAPSET,TRAP,BIAS
from author_Goldie_C5_opening import fig,figures
figures.clear()
AREA='8227:2020:M1:T9:O04:D01'
def ev(page):
 name='Goldie-C5-146'if page<150 else'Goldie-C5-150'if page<345 else'Goldie-key-C4-C5-345'
 p=W/f'checks/r5/textbooks/{name}.png';return {'path':str(p.relative_to(W.parents[2])),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
answers=[];corrections=[];new=[]
def add(kind,n,page,note,parts,direct,teaches=None):
 for p in parts:
  kp=p.pop('key_page_override',346);p.update(source_pdf_page=page,source_evidence=ev(page),answer_pdf_page=kp,answer_printed_page=kp-14,key_evidence=ev(kp),review_date='2026-11-18')
 row={'item_id':f'8227:TB:Goldie:C5:{kind}:{n}','source_pdf_page':page,'notes':note,'assessed_8227_demand_ids':direct,'component_demand_ids':[],
  'teaches_8227_demand_ids':teaches or[],'mapping_rationale':'Unprompted worked-rule exposition teaches rather than adding assessed source coverage. Boxed questions have direct demands only for what they actually ask. Formal curvature is author support,not a mandatory learner method.',
  'representation':'graph','sketch_response_required':False,'exam_style':False,'exam_style_basis':'Unattributed worked exposition or boxed prompt.',
  'value_level_scope_decisions':[{'rule_id':'8227:QUAL11','status':'within','quoted_value':note,'reason':'Simple graphs and finite trapezium estimates. Geometry supplies the circle-area check;formal derivatives are optional supporting evidence.'}],
  'precision_angle_check':{'source':'Exposition rounds2/4strip tables to4decimal places and prints decimal prefixes with ellipses for8/16strips and3decimals in the32/50/100/1000strip technology examples. Keep unrounded nodes before the final display.',
   'comparison':'Method instructions in an actual exam requiring the trapezium rule take precedence over this book’s general advice to prefer analytic methods. Refinement agreement alone does not certify an error bound.'},
  'expected_subpart_labels':[p['subpart']for p in parts],'subparts':parts};answers.append(row);return row
f='sqrt(5*x-x**2)';parts=[]
for label,n,key,dp,kp in [('two-strips',2,'6.8990',4,148),('four-strips',4,'7.8990',4,149),('eight-strips',8,'8.2407',4,149),('sixteen-strips',16,'8.3578',4,149),('technology32',32,'8.398',3,149),('technology50',50,'8.409',3,149),('technology100',100,'8.416',3,149),('technology1000',1000,'8.420',3,149)]:
 p=trapez(label,f,0,4,n,key,kp,dp=dp)
 if n in [8,16]:
  raw=compute(p['additional_operations']['unrounded_trapezium'])
  p['operation']={'kind':'decimal-prefix','operands':[str(raw)],'decimal_places':4}
  p['key_normalisation_note']='The source prints an ellipsis after this four-decimal prefix;compare truncation,not a claim of rounding to four decimal places.'
 if n>=32:
  p['operation']['kind']='numeric-trapezium-rule';p['additional_operations']['unrounded_trapezium']['kind']='numeric-trapezium-rule'
 parts.append(p)
for label,expr,key in [('two-A','sqrt(6)','2.4495'),('two-B','sqrt(6)+2','4.4495'),('four-P','1','1.0000'),('four-Q','(2+sqrt(6))/2','2.2247'),('four-R','sqrt(6)','2.4495'),('four-S','(sqrt(6)+2)/2','2.2247')]:
 p=value(label,expr,key,148 if label.startswith('two')else 149,'Calculate this individual trapezium from the exact height pair before rounding;do not add already rounded areas as if they were exact.')
 p['operation']={'kind':'rounded','operands':[expr],'decimal_places':4};parts.append(p)
row=add('Worked-illustration',1,147,'Unprompted y=√(5x−x²)area exposition on[0,4]:derive2/4strip estimates and each constituent trapezium,refine to8/16strips,and use the technology box for32,50,100,1000strips. The graph is a circle arc and every estimate here is below the true area.',parts,[],[TRAPSET,TRAP,BIAS])
row['evidence_role']='prerequisite/supporting worked teaching illustration; no directly assessed source-question coverage'
corrections.append({'item_id':row['item_id'],'continuation_pdf_pages':[148,149]})
area='3/2+25*(pi/2+asin(3/5))/8'
p=reasoning('geometry-and-area','The curve is an upper circle arc with centre(5/2,0),radius5/2. The required area is3/2+(25/8)(π/2+asin(3/5))≈8.4197.',
 'Complete the square:y²+(x−5/2)²=25/4. The region0≤x≤4 combines the left quarter-circle with a sector and right triangle ending at(4,2). The sector sine is(4−5/2)/(5/2)=3/5. Sector/triangle geometry gives the stated expression without requiring an analytic antiderivative.',346,'matches')
p['additional_operations']={'circle_identity':{'kind':'identity','operands':['expand((5*x-x**2)+(x-5/2)**2)']},'area4dp':{'kind':'rounded','operands':[area],'decimal_places':4}}
p['additional_operation_expected']={'circle_identity':'25/4','area4dp':'8.4197'}
T16=compute({'kind':'trapezium-rule','operands':[f,'0','4'],'strips':16})
p2=value('sixteen-strip-error','100*(('+area+')-('+str(T16)+'))/('+area+')','0.7',346,'Compare the unrounded16-strip estimate with the exact geometric area. Its shortfall is about0.0619area units,or0.7%at the source displayed one decimal percentage precision.')
p2['operation']={'kind':'rounded','operands':['100*(('+area+')-('+str(T16)+'))/('+area+')'],'decimal_places':1}
p2['units']='%';p2['printed_key_units']='%'
add('Prompt',3,150,'Find the y=√(5x−x²)area on[0,4]without calculus,and assess how close the16-strip estimate is. Use circle geometry rather than assuming numerical agreement proves exactness.',[p,p2],[AREA,TRAP])
parts=[reasoning('i','Underestimate.','The first given curve bends down across the shaded interval,so its straight interpolation chords lie below the curve. No formula or formal second derivative is needed.',346,'matches'),
 reasoning('ii','Cannot tell from the supplied change of curvature alone.','The middle curve has an inflexion within the integration region. Some chords can lie below and some above;the net signed area error depends on their sizes. A shape with changing curvature need not have a fixed over/under bias.',346,'matches'),
 reasoning('iii','Overestimate.','The third given decreasing curve bends up across the shaded interval. Its interpolation chords lie above it. Decreasing alone would not determine this sign;curvature relative to chords does.',346,'matches')]
row=add('Prompt',4,151,'Read the three shaded graphs in Figure5.7 and decide trapezium underestimate,overestimate or cannot tell. All three response decisions are recorded;the inflecting middle graph must not inherit a blanket bias.',parts,[BIAS])
new.append({'item_id':row['item_id'],'item_kind':'prompt','exercise':'Prompt','item_number':'4','pdf_page':151,'printed_page':137,'notes':row['notes'],'assessed_8227_demand_ids':[BIAS],'component_demand_ids':[],'representation':'graph','source_evidence':ev(151),'learner_display':False})
for n,page,label,note,parent,rep,checks in [
 (11,148,'Figure5.3 two trapezia under circle arc','Given y=√(5x−x²)on[0,4];nodes0,2,4have heights0,√6,2. Two width2chords lie below the concave arc.','Worked-illustration:1','graph',[('Tuple(sqrt(5*x-x**2).subs(x,0),sqrt(5*x-x**2).subs(x,2),sqrt(5*x-x**2).subs(x,4))','Tuple(0,sqrt(6),2)')]),
 (12,148,'Figure5.4 isolated component trapezia','Two source panels unpack the width2areas:triangleAhas parallel heights0and√6;trapeziumBhas heights√6and2. The displayed2.4495height is rounded.','Worked-illustration:1','diagram',[('Tuple(2*(0+sqrt(6))/2,2*(sqrt(6)+2)/2)','Tuple(sqrt(6),sqrt(6)+2)')]),
 (13,149,'Figure5.5 four trapezia','Four unit strips have node heights0,2,√6,√6,2. The shared adjacent heights are counted twice only in the collected-sum formula.','Worked-illustration:1','graph',[('Tuple(*[sqrt(5*x-x**2).subs(x,0)])','Tuple(0)')]),
 (14,150,'Figure5.6 general n-strip schematic','Generic f(x)graph froma tob with equal widthh and ordinatesy₀,…,yₙ. Chords define the trapezium estimate;the schematic’s changing curvature does not imply one global bias.',None,'graph',[]),
 (15,150,'Collected trapezium formula and labelled weights','A≈h/2[y₀+2(y₁+…+yₙ₋₁)+yₙ];the endpoint weights are1,and every interior ordinate has weight2. The book labels strip width,end heights and middle heights.',None,'table',[('expand((a+b)/2+(b+c)/2)','a/2+b+c/2')]),
 (16,151,'Figure5.7(i) concave-down given graph','The increasing concave-down graph’s interpolation chords underestimate the positive shaded area. Increasing alone is not the justification.','Prompt:4','graph',[]),
 (17,151,'Figure5.7(ii) given inflecting graph','The S-shaped increasing graph changes curvature inside the shaded interval. The drawing supplies no net chord-area error,so cannot tell is the supported response.','Prompt:4','graph',[]),
 (18,151,'Figure5.7(iii) concave-up given graph','The decreasing concave-up graph’s interpolation chords overestimate the positive shaded area. Decreasing alone is not the justification.','Prompt:4','graph',[]),
 (19,149,'Technology refinement values','The boxed instruction asks graph software to compare increasingly fine trapezia. Source values32:8.398;50:8.409;100:8.416;1000:8.420are independently recalculated at3decimal places.','Worked-illustration:1','table',[])]:
 # Keep the formula/node check explicit;do not pass Python list comprehensions to the symbolic parser.
 if n==13:checks=[('Tuple(sqrt(5*x-x**2).subs(x,0),sqrt(5*x-x**2).subs(x,1),sqrt(5*x-x**2).subs(x,2),sqrt(5*x-x**2).subs(x,3),sqrt(5*x-x**2).subs(x,4))','Tuple(0,2,sqrt(6),sqrt(6),2)')]
 fig(n,page,label,note,[TRAPSET,TRAP,BIAS],rep,checks,parent)
for row in figures:row['source_evidence']=ev(row['pdf_page'])
pages=[]
for page in range(147,152):
 ids=[r['item_id']for r in answers if r['source_pdf_page']==page]+[r['item_id']for r in figures if r['pdf_page']==page]
 if page==147:ids+=['8227:TB:Goldie:C5:Exercise-5B:12','8227:TB:Goldie:C5:Exercise-5B:13']
 if page==151:ids +=[f'8227:TB:Goldie:C5:Exercise-5C:{n}'for n in[1,2,3]]+['8227:TB:Goldie:C5:Teaching-figure:20']
 pages.append({'pdf_page':page,'printed_page':page-14,'chapter':5,'page_status':'items enumerated','item_ids':ids,'continuation_item_ids':['8227:TB:Goldie:C5:Worked-illustration:1']if page in[148,149]else[],
  'source_evidence':ev(page),'reader':'Codex author','date':'2026-11-18','non_item_content':'Every worked numerical value,boxed question,teaching/given graph and formula/table recorded. Exposition147includes5B12/13;151includesPrompt4and5C1–3. General method warnings are teaching advice,not additional tasks.'})
if __name__=='__main__':
 for name,data in [('answers-Goldie-C5-numerical-opening.json',{'scope':'Full worked illustration,technology estimates,both boxed prompts and their reasons.','items':answers}),('census-Goldie-C5-numerical-opening.json',{'book':'Goldie','book_id':'8227-SRC-015','chapter':5,'source_path':SRC,'source_sha256':SHA,'scope':'Complete147–151including combined exercise starts and allsource figures.','new_items':new+figures,'corrections':corrections,'pages':pages})]:
  (W/'tools/textbook-r5'/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
 for row in answers:
  for p in row['subparts']:
   if 'operation'in p:
    got=compute(p['operation']);assert equivalent(got,expression(p['printed_key_normalised'])),(row['item_id'],p['subpart'],got,p['printed_key_normalised'])
 print(len(answers),'response/illustration items;',sum(len(r['subparts'])for r in answers),'outputs;',len(figures),'figures;one newly discovered boxed prompt')
