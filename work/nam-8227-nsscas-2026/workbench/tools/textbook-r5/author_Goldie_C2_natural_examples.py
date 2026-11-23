"""Worked Examples9–12 and every mathematical callout/figure on63–66."""
import hashlib,json
from author_Goldie_C5_opening import W,SRC,SHA,value,reasoning,fig,figures,compute,expression,equivalent
NAT='8227:2020:M2:T2:O02:D01';INV='8227:2020:M2:T2:O02:D02';LAW='8227:2020:M2:T2:O01:D02';EQ='8227:2020:M2:T2:O03:D01'
def ev(page):
 name='Goldie-C2-62'if page<66 else'Goldie-C2-66'
 p=W/f'checks/r5/textbooks/{name}.png';return {'path':str(p.relative_to(W.parents[2])),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
answers=[]
def add(n,page,note,parts,direct,components=None):
 for p in parts:
  kp=p.pop('key_page_override',page);p.update(source_pdf_page=page,source_evidence=ev(page),answer_pdf_page=kp,answer_printed_page=kp-14,key_evidence=ev(kp),review_date='2026-11-18')
 row={'item_id':f'8227:TB:Goldie:C2:Example:{n}','source_pdf_page':page,'notes':note,'assessed_8227_demand_ids':direct,'component_demand_ids':components or[],
  'mapping_rationale':'The e/ln definitions and graphs are direct when requested; solving a time threshold, rearranging a log equation and filtering a quadratic exponential substitution remain distinct decisions. Direct substitution alone does not establish a separate progression demand.',
  'representation':'text','sketch_response_required':any(p.get('author_comparison_status')=='sketch'for p in parts),'exam_style':False,'exam_style_basis':'Worked example without examination attribution.',
  'value_level_scope_decisions':[{'rule_id':'8227:LIMIT06','status':'not applicable','quoted_value':note,'reason':'Natural inverse identities and power laws suffice; no general change-of-base recall is required.'}],
  'precision_angle_check':{'source':'Population after20days is nearest whole insect;the threshold key says just over16days. Radioactive mass after1hour is2decimal places,half-life1decimal place. Example12is3significant figures.',
   'comparison':'Continuous model time is not automatically rounded up to an integer observation. Convert1hour to3600seconds in the given exponent. Physical meaning claims beyond the supplied mathematical model remain unverified.'},
  'expected_subpart_labels':[p['subpart']for p in parts],'subparts':parts};answers.append(row);return row
def rounded(label,expr,key,page,sf=None,dp=None,method=None):
 p=value(label,expr,key,page,method or 'Derive from the original source formula,retain exact values,then round only the requested final result.')
 p['operation']={'kind':'rounded','operands':[expr],**({'significant_figures':sf}if sf else{'decimal_places':dp})};return p
p=reasoning('i','On t≥0,sketch N=2000e^(0.1t)starting at(0,2000),increasing with positive curvature and no finite upper bound.',
 'At0 the exponential is1. Both first and second derivatives are positive on the physical time domain;the source graph agrees. A negative-time asymptote of the abstract full-real formula is outside the physical viewport.',64,'sketch')
p2=rounded('ii','2000*exp(20/10)','14778',64,dp=0)
p3=reasoning('iii','The continuous threshold time is10ln5≈16.094days,just over16days.',
 'Set10000=2000e^(t/10),divide by2000and apply the inverse natural log to gett=10ln5. The source does not ask for a first whole-number day;rounding this up to17would change the question.',64,'matches')
p3['additional_operations']={'threshold_substitution':{'kind':'identity','operands':['2000*exp((10*log(5))/10)']}};p3['additional_operation_expected']={'threshold_substitution':'10000'}
add(9,63,'For N=2000e^(0.1t),t days since observation began,sketch the model,find the20-day population and solve the10000-insect continuous threshold.',[p,p2,p3],[INV,EQ])
p=reasoning('i','For t≥0,sketch a decreasing convex curve from(0,25),approaching the horizontal asymptote M=0from above.',
 'The original mass model25e^(−0.0012t)is positive,has negative first derivative and positive second derivative. It never reaches0at finite time. Source Figure2.18agrees.',64,'sketch')
p2=value('ii','25*exp(0)','25',64,'The initial mass is the value at0seconds,not the remaining mass after an hour.');p2['units']='g';p2['printed_key_units']='g'
p3=rounded('iii','25*exp(-(12/10000)*3600)','0.33',65,dp=2,method='The model time is seconds. Convert1hour to3600seconds before substituting;the exact positive mass is about0.3325g,displayed to2decimal places.');p3['units']='g';p3['printed_key_units']='g'
p4=rounded('iv','log(2)/(12/10000)','577.6',65,dp=1,method='The supplied half-life definition requires M=25/2. Divide the original model by25,apply ln to1/2=e^(−0.0012t),and solve for positive time. Do not substitute minutes into a per-second exponent.');p4['units']='s';p4['printed_key_units']='s'
add(10,64,'For M=25e^(−0.0012t)grams with t in seconds,sketch decay,state initial mass,find mass after1hour and calculate half-life from its supplied definition.',[p,p2,p3,p4],[INV,EQ],[NAT])
p=value('p','solve(p-exp(t)*(1-p),p)[0]','exp(t)/(1+exp(t))',65,'Original logs require0<p<1. Combine them into ln(p/(1−p))=t,exponentiate,and solve the resulting linear equation in p. The resulting p=e^t/(1+e^t)lies strictly between0and1for every realt,so it preserves the original domain.')
p['additional_operations']={'quotient_at_solution':{'kind':'identity','operands':['((exp(t)/(1+exp(t)))/(1-exp(t)/(1+exp(t))))']}}
p['additional_operation_expected']={'quotient_at_solution':'exp(t)'}
add(11,65,'Make p the subject of ln p−ln(1−p)=t;retain both positive log arguments and verify the final logistic expression lies in0<p<1.',[p],[LAW,NAT])
p=rounded('i','solve(x-4-exp(-4)*x,x)[0]','4.07',66,sf=3,method='Original logarithms require x>4. Exponentiating givesx−4=xe^(−4),hencex=4/(1−e^(−4))>4. Compare only the rounded final value;the exact solution satisfies the original logs.')
p2=rounded('ii','log(2)','0.693',66,sf=3,method='Letu=e^x>0. Solve u²+u−6=(u−2)(u+3)=0,discard−3,and usex=ln2. The positive exponential-substitution domain is essential.')
p2['additional_operations']={'all_substitution_roots':{'kind':'identity','operands':['FiniteSet(*solve(x**2+x-6,x))']}}
p2['additional_operation_expected']={'all_substitution_roots':'FiniteSet(-3,2)'}
add(12,66,'Solve ln(x−4)=lnx−4and e^(2x)+e^x=6to3significant figures. The first requiresx>4;the second discards a negative exponential substitution root.',[p,p2],[LAW,NAT,EQ],['8227:PRIOR:NSSCO:quadratic'])
figures.clear()
for n,page,label,note,teaches,rep,checks,parent in [
 (35,63,'Figure2.15 exponential family','All shown a^xcurves pass(0,1). Bases3,e,2,1.5increase;0.5decreases;the1^x=1case is constant. It is a displayed boundary case,not a valid logarithm base or an increasing exponential.',[NAT,INV],'graph',[('Tuple(3**0,exp(0),2**0,(3/2)**0,1**0,(1/2)**0)','Tuple(1,1,1,1,1,1)')],None),
 (36,63,'Figure2.16 natural exponential decay','y=e^(−x)has intercept(0,1),decreases convexly and approaches0from above asx→∞;it is the y-axis reflection ofe^x.',[INV],'graph',[('limit(exp(-x),x,oo)','0')],None),
 (37,64,'Figure2.17 colony model','N=2000e^(0.1t)starts2000at t=0and increases convexly for t≥0. Population and time labels belong to the same supplied instance.',[INV],'graph',[('(2000*exp(x/10)).subs(x,0)','2000')],'Example:9'),
 (38,64,'Example9 initial-value callout','At t=0,N=2000e^0=2000. The coefficient is the model initial value,not a growth multiplier per whole day.',[NAT],'table',[('2000*exp(0)','2000')],'Example:9'),
 (39,64,'Example9 inverse-log callout','ln(e^u)=ufor every real exponent u;hereu=0.1t. Applying this after dividing by the initial population gives the continuous threshold time.',[NAT],'table',[('log(exp(x/10))','x/10')],'Example:9'),
 (40,64,'Figure2.18 radioactive mass model','M=25e^(−0.0012t)starts25gand decreases toward0for t≥0seconds. A horizontal asymptote does not imply a finite extinction time.',[INV],'graph',[('(25*exp(-12*x/10000)).subs(x,0)','25')],'Example:10'),
 (41,65,'Example11 quotient-log callout','The quotient law combinesln p−ln(1−p)asln(p/(1−p))only with both p>0and1−p>0. A positive quotient alone would not retain both original log domains.',[LAW],'table',[],'Example:11'),
 (42,65,'Example11 exponential inverse callout','e^(lnu)=uforpositiveu. Hereu=p/(1−p)with0<p<1. Exponentiation is followed by a linear rearrangement,not a choice of a negative logarithmic branch.',[NAT],'table',[('exp(log(2))','2')],'Example:11')]:fig(n,page,label,note,teaches,rep,checks,parent)
for f in figures:f['item_id']=f['item_id'].replace(':C5:',':C2:');f['parent_item_id']=f['parent_item_id'].replace(':C5:',':C2:')if f['parent_item_id']else None;f['source_evidence']=ev(f['pdf_page'])
pages=[]
for page in range(63,66):
 pages.append({'pdf_page':page,'printed_page':page-14,'chapter':2,'page_status':'items enumerated','item_ids':[r['item_id']for r in answers if r['source_pdf_page']==page]+[r['item_id']for r in figures if r['pdf_page']==page],
  'continuation_item_ids':['8227:TB:Goldie:C2:Example:9']if page==64 else['8227:TB:Goldie:C2:Example:10']if page==65 else[],
  'source_evidence':ev(page),'reader':'Codex author','date':'2026-11-18','non_item_content':'Every worked Example,graph and mathematical callout enumerated. Example12on66awaits the combined Exercise2Dcensus;non-mathematical radioactivity characterisation is not certified by this model audit.'})
if __name__=='__main__':
 for name,data in [('answers-Goldie-C2-natural-examples.json',{'scope':'All Example9–12requested outputs,with exact domains and source precision.','items':answers}),('census-Goldie-C2-natural-examples.json',{'book':'Goldie','book_id':'8227-SRC-015','chapter':2,'source_path':SRC,'source_sha256':SHA,'scope':'Complete63–65;Example12response on66recorded,combined page census pending2D.','new_items':figures,'corrections':[{'item_id':'8227:TB:Goldie:C2:Example:9','continuation_pdf_pages':[64]},{'item_id':'8227:TB:Goldie:C2:Example:10','continuation_pdf_pages':[65]}],'pages':pages})]:
  (W/'tools/textbook-r5'/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
 for r in answers:
  for p in r['subparts']:
   if 'operation'in p:assert equivalent(compute(p['operation']),expression(p['printed_key_normalised'])),(r['item_id'],p['subpart'])
   for name,op in p.get('additional_operations',{}).items():assert equivalent(compute(op),expression(p['additional_operation_expected'][name])),(r['item_id'],name)
 print(len(answers),'items;',sum(len(r['subparts'])for r in answers),'outputs;',len(figures),'figures')
