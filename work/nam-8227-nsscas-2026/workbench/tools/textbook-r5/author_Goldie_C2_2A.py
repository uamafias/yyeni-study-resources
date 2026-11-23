"""Every2Aresponse,physical domains,discrete frequency count and two source tables."""
import hashlib,json
from author_Goldie_C5_opening import W,SRC,SHA,value,reasoning,compute,expression,equivalent
SKETCH='8227:2020:M1:T3:O05:D01';GPMODEL='8227:2020:M1:T2:O03:D03';GP='8227:2020:M1:T2:O03:D02';EXPEQ='8227:2020:M2:T2:O03:D01';LOGIND='8227:2020:M2:T2:O01:D01'
def ev(page):
 name='Goldie-C2-38'if page==41 else'Goldie-C2-42'if page<335 else'Goldie-key-C2-335'
 p=W/f'checks/r5/textbooks/{name}.png';return {'path':str(p.relative_to(W.parents[2])),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
answers=[]
def add(n,page,note,parts,direct,components=None,sketch=False,rep='text'):
 for p in parts:
  kp=p.pop('key_page_override',336 if n>=3 else 335);p.update(source_pdf_page=page,source_evidence=ev(page),answer_pdf_page=kp,answer_printed_page=kp-14,key_evidence=ev(kp),review_date='2026-11-18')
 row={'item_id':f'8227:TB:Goldie:C2:Exercise-2A:{n}','source_pdf_page':page,'notes':note,'assessed_8227_demand_ids':direct,'component_demand_ids':components or[],
  'mapping_rationale':'Sketching and solving a threshold are assessed only where actually requested. Direct evaluation of a supplied power is prerequisite arithmetic,not automatic log-law or exponential-equation coverage. The musical table supplies its own doubling convention.',
  'component_demand_roles':[{'role':'prerequisite index arithmetic/direct formula evaluation','demand_ids':[],'reason':'Do not invent an8227objective for isolated power substitution.'}],
  'representation':rep,'sketch_response_required':sketch,'exam_style':False,'exam_style_basis':'Ordinary exercise without examination attribution.',
  'value_level_scope_decisions':[{'rule_id':'8227:QUAL07','status':'not applicable'if n==6 else'within','quoted_value':note,'reason':'The octave-count task uses a supplied discrete table and doubling rule,not an admissible-domain/range question.'if n==6 else'Pure graphs use realx;contextual time is nonnegative. Preserve physical time and the asymptote of the actual formula.'}],
  'precision_angle_check':{'source':'Population after5years is rounded to the nearest whole person. Frequency values in the source table are already rounded to whole hertz. Tree threshold is only described qualitatively in the key.',
   'comparison':'Do not import exact modern tuning frequencies over the supplied rounded table,or impose an unstated root precision. Keep continuous growth models separate from literal integer counts at every possible real time.'},
  'expected_subpart_labels':[p['subpart']for p in parts],'subparts':parts};answers.append(row);return row
for n,base,sgn,offsets in [(1,'2',1,[0,1,-1]),(2,'3',-1,[0,2,-1])]:
 parts=[]
 for label,d in zip(['i','ii','iii'],offsets):
  f=f'{base}**({sgn}*x)+({d})';intercept=1+d;direction='increasing'if sgn==1 else'decreasing';end='−∞'if sgn==1 else'+∞'
  p=reasoning(label,f'Sketch a {direction},convex exponential with y-intercept(0,{intercept})and horizontal asymptotey={d}asx→{end}.',
   'The positive-base power is always positive. Its first derivative has the stated sign for all realx,and its second derivative is positive. The vertical offset moves both intercept and limiting level;preserve the full real input domain.',335,'sketch')
  p['additional_operations']={'intercept_asymptote':{'kind':'identity','operands':[f'Tuple(({f}).subs(x,0),limit({f},x,{"-oo"if sgn==1 else"oo"}))']}}
  p['additional_operation_expected']={'intercept_asymptote':f'Tuple({intercept},{d})'};parts.append(p)
 add(n,41,'Sketch three '+direction+' exponential graphs,showing each horizontal asymptote and y-intercept. Original formulas:'+(';'.join(f'{base}^({sgn}x)+({d})'for d in offsets))+'.',parts,[SKETCH],sketch=True)
p=value('i-initial','10000*10**0','10000',336,'At t=0,the model gives the stated initial population.')
p2=value('i-five-years','10000*10**(5/10)','31623',336,'Evaluate the source model at5years,retaining exact10000√10before rounding to the nearest whole person.')
p2['operation']={'kind':'rounded','operands':['10000*10**(5/10)'],'decimal_places':0}
p3=reasoning('ii','Fort≥0,sketch increasing convexpopulationPstarting at(0,10000),with no finite upper bound.',
 'The given formulaP=10000·10^(0.1t)has a positive increasing exponential factor. The physical years-after-start domain begins0. The key sketch agrees. A negative-time horizontal asymptote of the abstract formula is not a required physical-domain feature here.',336,'sketch')
add(3,41,'UseP=10000·10^(0.1t)to state the initial population,calculate it after5years,and sketch the physical growth model. No inverse exponential solve is asked.',[p,p2,p3],[SKETCH],sketch=True)
f='20-19*(9/10)**x'
p=value('i',f'({f}).subs(x,0)','1',336);p['units']='m';p['printed_key_units']='m'
p2=value('ii',f'({f}).subs(x,2)','4.61',336);p2['units']='m';p2['printed_key_units']='m'
p3=reasoning('iii','The tree reaches10metres just after6years;an independent author value is about6.09years.',
 'Use actual trial values in the original height model:at6years the height is below10andat6.1years it is above10. The model is continuous and strictly increasing,so this brackets the unique time. The key asks no decimal-place count and saysjustover6years. The log/reference solve is independent QA,not a substitute for the requested trial-and-improvement evidence.',336,'matches')
p3['additional_operations']={'trial_signs':{'kind':'identity','operands':[f'Tuple(sign((({f})-10).subs(x,6)),sign((({f})-10).subs(x,61/10)))']},'reference_time':{'kind':'bracketed-source-root','operands':[f'({f})-10','6','7'],'rounding':{'decimal_places':2}}}
p3['additional_operation_expected']={'trial_signs':'Tuple(-1,1)','reference_time':'6.09'}
p4=value('iv',f'limit({f},x,oo)','20',336,'The positive decaying factor tends to0,so the limiting height is20metres;the model does not reach it at a finite time.');p4['units']='m';p4['printed_key_units']='m'
add(4,41,'Forh=20−19·0.9^t,t≥0,find initial and two-year heights,use trial and improvement for the10metre time,and state the eventual model height. Time is continuous;do not silently round its threshold up to the next annual observation.',[p,p2,p3,p4],[EXPEQ])
f='200+320*2**(-x)'
p=value('i',f'({f}).subs(x,0)','520',336)
p2=value('ii',f'({f}).subs(x,5)','210',336)
p3=reasoning('iii','Fort≥0,sketch a decreasing convex curve from520toward horizontal asymptoten=200,staying above200.',
 'The positive2^(−t)term decays toward0. The model represents an idealised population trend;the source asks the counts at specific integer times rather than demanding integer values at every realt. The graph must use the same initial value and limiting level.',336,'sketch')
p4=value('iv',f'limit({f},x,oo)','200',336,'The long-term model size is the fixed offset200birds.')
add(5,42,'For the island-bird modeln=200+320·2^(−t),find arrival count,five-year count,a physical-domain sketch and long-term size. The sustainability context is supplied,not inferred from another population formula.',[p,p2,p3,p4],[SKETCH],sketch=True)
p=value('i','247*2**3','1976',336,'The supplied Bfrequency is247Hz,and every octave multiplies it by2. Three octaves up therefore gives247·8using the rounded input table.');p['units']='Hz';p['printed_key_units']='Hz'
p2=reasoning('ii','The27.5Hznote isA,three octaves below the listed middleA.',
 'The supplied middleAis220Hz,and220/2³=27.5. Search the given seven-letter table under the exact doubling rule;do not replace it with external tuning data or count twelve chromatic notes per octave.',336,'matches')
p2['additional_operations']={'octave_value':{'kind':'identity','operands':['220/2**3']}}
p2['additional_operation_expected']={'octave_value':'27.5'}
notes={'A':220,'B':247,'C':262,'D':294,'E':330,'F':349,'G':392};heard=[];bounds=[]
for label,freq in notes.items():
 low=int(expression(f'ceiling(log(75/{freq})/log(2))'));high=int(expression(f'floor(log(9000/{freq})/log(2))'))
 bounds.append({'note':label,'minimum_octave_offset':low,'maximum_octave_offset':high})
 for k in range(low,high+1):heard.append({'note':label,'octave_offset':k,'frequency_hz':str(expression(f'{freq}*2**({k})'))})
assert len(heard)==48 and len({r['frequency_hz']for r in heard})==48
p3=reasoning('iii','She can hear48notes in the stated seven-letter standard scale,fromEtwo octaves below toCfive octaves above the table.',
 'For each supplied frequencyf,the integer octave offsetksatisfies75≤f·2^k≤9000. Derive finite bounds separately for each of the seven notes,and count each pitch once. There are3notes in the lowest partial octave,6complete seven-note octaves,and3in the highest partial octave:3+42+3=48. The provided table and exact octave rule suffice;an external chromatic piano convention would change the question.',336,'matches')
p3['heard_note_bounds']=bounds;p3['heard_notes']=heard
p3['additional_operations']={'count':{'kind':'identity','operands':['3+6*7+3']},'boundary_frequencies':{'kind':'identity','operands':['Tuple(294/4,330/4,262*32,294*32)']}}
p3['additional_operation_expected']={'count':'48','boundary_frequencies':'Tuple(73.5,82.5,8384,9408)'}
row=add(6,42,'Use the supplied roundedA–Gfrequency table and exact octave doubling:findBthree octaves up,identify27.5Hz,and count audible standard-scale pitches in[75,9000]Hz. Seven distinct letter notes per doubling interval avoid repeated-octave endpoint double counting.',[p,p2,p3],[GPMODEL,GP],rep='table')
row['direct_demand_aspects']=[{'demand_id':GP,'assessed_facet':'Multiplicative terms and finite admissible integer-index count,not a GPsum.'}]
from author_Goldie_C5_opening import fig,figures
figures.clear()
fig(5,42,'2A6given musical frequency table','A220,B247,C262,D294,E330,F349,G392Hzare explicitly rounded to whole numbers. The source separately states exact doubling per octave;use those supplied model inputs consistently.',[GPMODEL,GP],'table',parent='Exercise-2A:6')
fig(6,42,'Indices multiplication and logarithm definition reference','The unprompted81·243example is3⁴·3⁵=3⁹=19683. The reference equatesy=a^xwithlog_a y=xfor valid positive basea≠1andpositivey. These are teaching relations,not a separate learner exercise.',[LOGIND],'table',[('81*243','3**9')])
for row in figures:row['item_id']=row['item_id'].replace(':C5:',':C2:');row['parent_item_id']=row['parent_item_id'].replace(':C5:',':C2:')if row['parent_item_id']else None;row['source_evidence']=ev(row['pdf_page'])
pages=[]
for page in[41,42]:
 ids=[r['item_id']for r in answers if r['source_pdf_page']==page]+[r['item_id']for r in figures if r['pdf_page']==page]
 if page==41:ids+=['8227:TB:Goldie:C2:Teaching-figure:4']
 pages.append({'pdf_page':page,'printed_page':page-14,'chapter':2,'page_status':'items enumerated','item_ids':ids,'continuation_item_ids':['8227:TB:Goldie:C2:Example:1']if page==41 else[],
  'source_evidence':ev(page),'reader':'Codex author','date':'2026-11-18','non_item_content':'Every2Aquestion and response recorded. Page41includes the Example1solution/graph continuation;page42includes the supplied frequency table and unpromptedindices/logarithm teaching reference.'})
if __name__=='__main__':
 for name,data in [('answers-Goldie-C2-2A.json',{'scope':'Every2Agraph,value,threshold and discrete frequency-count response.','items':answers}),('census-Goldie-C2-2A.json',{'book':'Goldie','book_id':'8227-SRC-015','chapter':2,'source_path':SRC,'source_sha256':SHA,'scope':'Complete41–42including Example1continuation and first logarithm reference.','new_items':figures,'corrections':[],'pages':pages})]:
  (W/'tools/textbook-r5'/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
 for row in answers:
  for p in row['subparts']:
   if 'operation'in p:
    got=compute(p['operation']);assert equivalent(got,expression(p['printed_key_normalised'])),(row['item_id'],p['subpart'],got)
   for name,op in p.get('additional_operations',{}).items():assert equivalent(compute(op),expression(p['additional_operation_expected'][name])),(row['item_id'],name)
 print(len(answers),'items;',sum(len(r['subparts'])for r in answers),'outputs;48audible pitch entries;two source tables')
