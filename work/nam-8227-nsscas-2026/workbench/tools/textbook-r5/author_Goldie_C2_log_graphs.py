"""All source tasks and mathematical figures on46–50,with2Bowned separately."""
import hashlib,json
from author_Goldie_C5_opening import W,SRC,SHA,value,reasoning,fig,figures,compute,expression,equivalent
IND='8227:2020:M2:T2:O01:D01';LAW='8227:2020:M2:T2:O01:D02';SKETCH='8227:2020:M1:T3:O05:D01';DOMAIN='8227:2020:M1:T3:O02:D01'
def ev(page):
 name='Goldie-C2-46'if page<50 else'Goldie-C2-50'if page<335 else'Goldie-key-C2-335'
 p=W/f'checks/r5/textbooks/{name}.png';return {'path':str(p.relative_to(W.parents[2])),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
answers=[]
def add(kind,n,page,note,parts,direct,sketch=False):
 for p in parts:
  kp=p.pop('key_page_override',336);p.update(source_pdf_page=page,source_evidence=ev(page),answer_pdf_page=kp,answer_printed_page=kp-14,key_evidence=ev(kp),review_date='2026-11-18')
 row={'item_id':f'8227:TB:Goldie:C2:{kind}:{n}','source_pdf_page':page,'notes':note,'assessed_8227_demand_ids':direct,'component_demand_ids':[],
  'mapping_rationale':'The base2/basea graph and inverse-index meaning are assessed. They are not specifically a natural-log/e graph. The fixed-base log-law references teach their links without another assessed exercise.',
  'representation':'graph'if kind=='Prompt'else'text','sketch_response_required':sketch,'exam_style':False,'exam_style_basis':'Unattributed activity or boxed justification prompt.',
  'value_level_scope_decisions':[{'rule_id':'8227:LIMIT06','status':'not applicable','quoted_value':note,'reason':'Exact inverse-index meaning and graph properties,not memorised change of base.'}],
  'precision_angle_check':{'source':'Activity3estimates√2from a graph;keyabout1.4. Prompt2assumesa>1throughout.','comparison':'A graphical estimate is not expected to have calculator precision. The inverse-reflection line isy=x;positive argument/domain and base restrictions remain explicit.'},
  'expected_subpart_labels':[p['subpart']for p in parts],'subparts':parts};answers.append(row);return row
p=reasoning('graph','Plot(1/8,−3),(1/4,−2),(1/2,−1),(1,0),(2,1),(4,2),(8,3),(16,4),joining with a smooth increasing,concave-down curve forx>0and asymptotex=0.',
 'Each input is an exact power of2. The inverse-index definition supplies all ordinates,while the increasing exponential inverse determines monotonicity and shape. The source key’s labelled plot agrees;do not join to an invented point atx=0.',336,'sketch')
p['additional_operations']={'specified_points':{'kind':'identity','operands':['Tuple(log(1/8,2),log(1/4,2),log(1/2,2),log(1,2),log(2,2),log(4,2),log(8,2),log(16,2))']}}
p['additional_operation_expected']={'specified_points':'Tuple(-3,-2,-1,0,1,2,3,4)'}
p2=reasoning('sqrt2-estimate','Readxat ordinate½to estimate√2≈1.4.',
 'log2(√2)=½by the index definition. A horizontal read fromy=½to the curve and then down to thex-axis gives approximately1.4,as in the printed key. The exact square root is author reference only;do not require its full decimal expansion from this graph.',336,'matches')
p2['additional_operations']={'inverse_definition':{'kind':'identity','operands':['log(sqrt(2),2)']},'one_decimal_reference':{'kind':'rounded','operands':['sqrt(2)'],'decimal_places':1}}
p2['additional_operation_expected']={'inverse_definition':'1/2','one_decimal_reference':'1.4'}
add('Activity',3,46,'Drawy=log2xfrom the eight specified inputs1/8,1/4,1/2,1,2,4,8,16;use the graph to estimate√2via ordinate½.',[p,p2],[SKETCH,IND],True)
spec=[('intercept','(1,0)isthe unique x-axis crossing.','log_a1=0becausea^0=1and the inverse exponential isone-to-one.'),
 ('domain','The real curve is defined exactly forx>0.','a^yispositive for every realy,and forvalidbasea>1mapsRonto(0,∞). Its real inverse has positive-input domain.'),
 ('asymptote-sign','x=0is a vertical asymptote from the right,and0<x<1givesnegativey.','Asy→−∞,a^y→0+. As0<x<1,its exponentyisnegative becausea>1. Use the inverse index meaning;there is no left-side real branch.'),
 ('growth-gradient','The graph has no upper height bound,and its positive gradient decreases asxgrows.','Foranytargetheighty,the inputa^yexists,so the logarithm is unbounded above. Differentiation givesy′=1/(xln a)>0andy″=−1/(x²ln a)<0forx>0,a>1. Equivalently use reflection of the increasing convex exponential. Monotonicity alone would not establish decreasing gradient.'),
 ('base-point','The curve passes through(a,1).','The defining identitya^1=aimplieslog_a a=1forvalida>1.')]
parts=[reasoning(label,conclusion,working,336,'matches')for label,conclusion,working in spec]
add('Prompt',2,47,'Justify all five listed properties ofy=log_a xfora>1:crossing(1,0),positive domain,right-hand zero asymptote/negative branch,unbounded increasing graph with decreasing slope,and point(a,1).',parts,[IND,DOMAIN])
figures.clear()
rows=[
 (14,46,'Root logarithm reference','Forx>0andpositive integern,log_a(nthrootx)=log_a x/n,witha>0,a≠1. Repeated multiplication supplies the stated proof;invalid bases and nonpositive real arguments are excluded.',[LAW],'table',[('log(16**(1/4),2)','log(16,2)/4')],None),
 (15,46,'Logarithm to its own base reference','log_a a=1requiresa>0,a≠1. The introductory5^1=5example does not license every real number as a logarithm base.',[IND],'table',[('log(5,5)','1')],None),
 (16,46,'Reciprocal logarithm reference','Forpositiveyandvalidbase,log_a(1/y)=−log_a y. Forbase>1and y>1,the reciprocal’s log is negative;its argument is between0and1.',[LAW],'table',[('log(1/8,2)','-log(8,2)')],None),
 (17,47,'Figure2.5 general logarithm graph','For a>1,the curve has point(1,0),point(a,1),positive input domain,vertical asymptotex=0,and a concave-down increasing branch. The small guide lines labelaand1,not fixed numeric data.',[IND,SKETCH],'graph',[], 'Prompt:2'),
 (18,47,'Figure2.6 inverse exponential/logarithm reflection','The exponentialy=a^xand logarithmy=log_a xare reflections in y=xfor a>1. Points(0,1),(1,a)reflect to(1,0),(a,1). Their asymptotes arey=0andx=0respectively;the diagonal is not either curve.',[IND,SKETCH],'graph',[],None),
 (19,48,'Inverse-index identities and domains','Forvalidpositivebasea≠1,log_a(a^x)=xforallrealxanda^(log_a x)=xforx>0. Exponential domainRand range(0,∞)reverse for its logarithmic inverse. The two occurrences ofxhave different admissible domains.',[IND,DOMAIN],'table',[('log(2**(-3),2)','-3'),('2**log(8,2)','8')],None)]
for n,page,label,note,teaches,rep,checks,parent in rows:fig(n,page,label,note,teaches,rep,checks,parent)
for f in figures:
 f['item_id']=f['item_id'].replace(':C5:',':C2:');f['parent_item_id']=f['parent_item_id'].replace(':C5:',':C2:')if f['parent_item_id']else None;f['source_evidence']=ev(f['pdf_page'])
pages=[]
for page in range(46,51):
 ids=[r['item_id']for r in answers if r['source_pdf_page']==page]+[r['item_id']for r in figures if r['pdf_page']==page]
 ids +=[f'8227:TB:Goldie:C2:Exercise-2B:{n}'for n in(range(1,7)if page==48 else range(7,14)if page==49 else range(14,21)if page==50 else[])]
 pages.append({'pdf_page':page,'printed_page':page-14,'chapter':2,'page_status':'items enumerated','item_ids':ids,'continuation_item_ids':[],
  'source_evidence':ev(page),'reader':'Codex author','date':'2026-11-18','non_item_content':'Everyactivity,boxed prompt,reference block,teaching graph and2Bquestion enumerated. Source equations in exercises are part of their question,not additional teaching figures. Printed exam attributions retained internally.'})
if __name__=='__main__':
 for name,data in [('answers-Goldie-C2-log-graphs.json',{'scope':'EveryActivity2.3response and all five Prompt2justifications.','items':answers}),('census-Goldie-C2-log-graphs.json',{'book':'Goldie','book_id':'8227-SRC-015','chapter':2,'source_path':SRC,'source_sha256':SHA,'scope':'Complete46–50;2Banswer records generated separately.','new_items':figures,'corrections':[],'pages':pages})]:
  (W/'tools/textbook-r5'/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
 for r in answers:
  for p in r['subparts']:
   for name,op in p.get('additional_operations',{}).items():assert equivalent(compute(op),expression(p['additional_operation_expected'][name])),(r['item_id'],name)
 print(len(answers),'items;',sum(len(r['subparts'])for r in answers),'outputs;',len(figures),'figures')
