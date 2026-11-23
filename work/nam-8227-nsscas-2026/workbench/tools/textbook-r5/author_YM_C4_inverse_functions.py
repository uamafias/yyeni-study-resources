"""Fixed-source inverse equations,graphs and branch decisions: YM PDF219–220."""
import hashlib,json
from pathlib import Path
from author_YM_C4_trig_graphs import value,graph,reasoning
from author_YM_C4_equations import eq
W=Path(__file__).resolve().parents[2];ROOT=W.parents[2]
SRC='Y=mc as textbook.pdf';SHA='0b44ad3b67b1ea3de90cba780382d77deef347fae683cf6e28677f36c17a724f'
P='8227:2020:M1:T6:O04:D01';INV='8227:2020:M1:T3:O03:D02';ONE='8227:2020:M1:T3:O03:D01'
RANGE='8227:2020:M1:T3:O02:D02';DOMAIN='8227:2020:M1:T3:O02:D01';SKETCH='8227:2020:M1:T3:O05:D01';INVSKETCH='8227:2020:M1:T3:O05:D02'
BND='8227:2020:M1:T6:O06:D01';ALL='8227:2020:M1:T6:O06:D02'
def ev(page):
    name='YM-key-Try55'if page==613 else'YM-key-614-615-full'if page==614 else'YM-C4-217'
    p=W/f'checks/r5/textbooks/{name}.png'
    return {'path':str(p.relative_to(ROOT)),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
def inverse(label,family,a,b,c,lo,hi,key,kp,fields):
    p=value(label,'0',key,kp,'Independently invert the source output affine transform,then the injective principal trig branch,then the source input multiplier. Derive the inverse domain from the actual original endpoint images;retain the original restriction and requested features.')
    p['operation']={'kind':'inverse-principal-affine-trig','family':family,'operands':[a,b,c,lo,hi],'return_fields':fields}
    return p
answers=[]
def add(kind,n,page,note,parts,direct,sketch=False):
    for p in parts:
        kp=p.pop('key_page_override',page)
        p.update(source_pdf_page=page,source_evidence=ev(page),answer_pdf_page=kp,
          answer_printed_page='A'+str(kp-586)if kp>=602 else kp-12,key_evidence=ev(kp),review_date='2026-11-18')
    row={'item_id':f'8227:TB:YM:C4:{kind}:{n}','source_pdf_page':page,'notes':note,
      'assessed_8227_demand_ids':direct,'component_demand_ids':[],
      'mapping_rationale':'Separate original function domain/range,one-to-one branch decisions,inverse construction,requested sketches,andbounded equation roots. Showing a worked graph does not make it given information in a formula-only stem. Inverse principal-value equations do not acquire additional periodic roots.',
      'representation':'text','sketch_response_required':sketch,
      'value_level_scope_decisions':[{'rule_id':'8227:QUAL08','status':'within','quoted_value':note,
        'reason':'Actual inverse branches are retained. A non-injective full sine cycle is restricted before inversion;using a supplied inverse notation is not silently converted to a periodic equation.'},
       {'rule_id':'8227:QUAL07','status':'within'if sketch else'not applicable','quoted_value':note,
        'reason':'Only the actual simple sine/cosine/tangent transforms andtheir stated finite intervals are used.'if sketch else'No domain/range construction is asked in this inverse-value equation.'}],
      'exam_style':False,'exam_style_basis':'Ordinary worked Example/TryNow;no examination attribution or exam-style label.',
      'precision_angle_check':{'source':'Radian intervals andrequested exactπanswers are retained. Try54Q3key is3significant figures;the source Example55tables round interior samples to1decimal place.',
        'comparison':'Keep exact function/inverse formulas andinterval endpoints. Rounded table pairs are approximate illustrations,not exact inverse identities. The superscript c on a key angle denotes radians,not degrees.'},
      'expected_subpart_labels':[p['subpart']for p in parts],'subparts':parts}
    answers.append(row);return row

p=value('root','sin(-pi/3)/3','-sqrt(3)/6',613,'The right side−π/3is in the arcsine principal range. Hence3x=sin(−π/3)=−√3/2andx=−√3/6;the original inverse input remains in[−1,1].')
p['assertions']=[{'expression':'asin(3*(-sqrt(3)/6))+pi/3','expected':'0'}]
# Try54Q2andQ3lie above the tightly cropped Try55answer evidence.
add('Try-Now-54',2,219,'Solve asin(3x)=−π/3;the principal inverse fixes a single real input x=−√3/6,not a periodic angle family.',[p],[P])
p=value('root','1+sin(atan(3))','39/20',613,'atan3is in(0,π/2),so taking sine givesx−1=3/√10. The unique inputx=1+3/√10lies in the original admissible[0,2];compare its3significant-figure approximation with1.95.')
p['operation']={'kind':'rounded','operands':['1+sin(atan(3))'],'significant_figures':3}
p['additional_operations']={'exact_input':{'kind':'identity','operands':['1+sin(atan(3))']}}
p['assertions']=[{'expression':'sin(atan(3))-3/sqrt(10)','expected':'0'}]
add('Try-Now-54',3,219,'Find x satisfying asin(x−1)=atan3. The inverse ranges select the unique input1+3/√10≈1.95;do not solve an unrestricted sine equation instead.',[p],[P])
for row in answers:
    for part in row['subparts']:
        image=W/'checks/r5/textbooks/YM-key-612-613-full.png'
        part['key_evidence']={'path':str(image.relative_to(ROOT)),'sha256':hashlib.sha256(image.read_bytes()).hexdigest()}

p=inverse('a','tan','3','1/2','-2','-pi/2','pi/2',
 'Tuple(2*atan((x+2)/3),Interval(-5,1))',219,['expression','domain'])
p2=reasoning('b',
 'On the same axes,draw f(x)=3tan(x/2)−2only for−π/2≤x≤π/2,andits inverse reflected in y=x. Forward endpoints(−π/2,−5),(π/2,1)andpoint(0,−2)swap to(−5,−π/2),(1,π/2),(−2,0). Both curves are increasing finite pieces.',
 'The source argumentx/2lies in[−π/4,π/4],strictly inside the tangent principal branch. The function is increasing andhas range[−5,1]. Inverse coordinates swap exactly;the source interior table values−3.2,−.8are rounded approximations of−3.2426… and−.75736…,so their swapped pairs are not asserted as exact.',219,'sketch')
p2['additional_operations']={
 'forward_feature_check':{'kind':'trig-features','family':'tan','angle_unit':'radian','operands':['3','1/2','-2','-pi/2','pi/2'],'at':['-pi/2','-pi/4','0','pi/4','pi/2']},
 'inverse_formula_check':{'kind':'inverse-principal-affine-trig','family':'tan','operands':['3','1/2','-2','-pi/2','pi/2'],'return_fields':['expression','domain','range']},
 'rounded_left_table_value':{'kind':'rounded','operands':['3*tan(-pi/8)-2'],'decimal_places':1},
 'rounded_right_table_value':{'kind':'rounded','operands':['3*tan(pi/8)-2'],'decimal_places':1}}
p2['source_graph_comparison']='The source sketch shows reflection about y=x andtwo finite increasing pieces. Endpoint coordinates/intervals are author-derived mathematical features;no pixel-coordinate or official-award comparison is claimed.'
add('Example',55,219,'For f(x)=3tan(x/2)−2on[−π/2,π/2],(a)derive the inverse andits input domain;(b)sketch f andits inverse on the same axes. The source tables contain rounded interior values.',[p,p2],[INV,DOMAIN,INVSKETCH],True)

parts=[graph('a','sin','4','1','-1','-pi/2','pi/2','radian',613,
  {'window_range':'Interval(-5,3)'},status='matches')]
p=eq('b:x','sin','x','1/4',['0.253'],unit='radian',lo='-pi/2',hi='pi/2',approx=True,dp=3)
p.update(key_page_override=613,source_assessed_part_id='b',units='radian',printed_key_units='radian',
  printed_key_unit_basis='The source superscript c is radian notation,not a degree glyph.')
parts.extend([p,value('b:y','4*sin(0)-1','-1',613,
 'Evaluate the original function atx=0;the y-intercept is(0,−1).')])
parts[-1]['source_assessed_part_id']='b'
parts.append(graph('c','sin','4','1','-1','-pi/2','pi/2','radian',613,
 {'window_range':'Interval(-5,3)','window_domain':'Interval(-pi/2,pi/2)',
  'window_zero_locations':'FiniteSet(asin(1/4))','sample_values':'Tuple(-5,-1,3)'},at=['-pi/2','0','pi/2']))
parts.append(inverse('d','sin','4','1','-1','-pi/2','pi/2',
 'Tuple(asin((x+1)/4),Interval(-5,3),Interval(-pi/2,pi/2))',613,['expression','domain','range']))
add('Try-Now-55',1,220,'For f(x)=4sinx−1on[−π/2,π/2],state range,find both axis-intercepts,sketch the restricted increasing graph,andderive the inverse with its domain/range. The two intercept components belong to source part(b).',parts,[RANGE,BND,SKETCH,INV,DOMAIN],True)

parts=[graph('a','sin','-2','2','5','0','pi','radian',613,{'window_range':'Interval(3,7)'},status='matches'),
 graph('b','sin','-2','2','5','0','pi','radian',613,
  {'window_range':'Interval(3,7)','sample_values':'Tuple(5,3,5,7,5)',
   'window_global_min_locations':'FiniteSet(pi/4)','window_global_max_locations':'FiniteSet(3*pi/4)'},
  at=['0','pi/4','pi/2','3*pi/4','pi']),
 eq('c','sin','2*x','-1/2','FiniteSet(7*pi/12,11*pi/12)',unit='radian',hi='pi')]
parts[-1]['key_page_override']=613
p=value('d','0','pi/4',613,'The source graph starts decreasing fromx=0. Find the first interior stationary point;its nonzero second derivative makes it a turning point,so any larger initial interval contains repeated ordinates andcannot be one-to-one.')
p['operation']={'kind':'first-turning-point-right','operands':['5-2*sin(2*x)','0','pi']}
p['assertions']=[{'expression':'8*sin(2*(pi/4))','expected':'8'}]
parts.append(p)
p=inverse('e','sin','-2','2','5','0','pi/4','Tuple(asin((5-x)/2)/2)',613,['expression'])
p['dependency']={'source_part':'d','role':'Use the derived largest injective branch0≤x≤π/4.'}
p['additional_operations']={'inverse_domain_range':{'kind':'inverse-principal-affine-trig','family':'sin',
 'operands':['-2','2','5','0','pi/4'],'return_fields':['expression','domain','range']}}
parts.append(p)
add('Try-Now-55',2,220,'For f(x)=5−2sin2xon[0,π],find range,sketch,and solvef=6. Then restrict g to[0,k],find the largest k giving an inverse,andderive that branch inverse. Full f is not globally one-to-one;the maximal initial branch is[0,π/4].',parts,[RANGE,SKETCH,BND,ALL,ONE,INV],True)

parts=[eq('a','cos','x','1/2','FiniteSet(pi/4,3*pi/4)',unit='radian',hi='pi',power=2),
 graph('b:i','cos','-4','1','3','0','pi','radian',614,{'window_range':'Interval(-1,7)'},status='matches'),
 graph('b:ii','cos','-4','1','3','0','pi','radian',614,
  {'window_range':'Interval(-1,7)','sample_values':'Tuple(-1,3,7)','window_zero_locations':'FiniteSet(acos(3/4))'},at=['0','pi/2','pi'])]
parts[0]['key_page_override']=613
p=reasoning('b:iii','Yes. For k=1,f(x)=3−4cosx is strictly increasing on[0,π],so every output has at most one input andan inverse exists.',
 'Cosine is strictly decreasing on[0,π]. Multiplying by−4reverses the order;adding3preserves it. Equivalently,f′=4sinx>0in the interior,with distinct endpoint values−1and7. Thus the whole supplied interval is one-to-one;no further restriction is needed.',614,'matches')
parts.append(p)
add('Try-Now-55',3,220,'For f(x)=3−4cos^k x on[0,π],(a)use k=2to solvef=1exactly;(b)use k=1to state range,sketch,andexplain whether an inverse exists. The superscript k is a power,not an input multiplier.',parts,[RANGE,SKETCH,BND,ALL,ONE],True)

figures=[]
for n,label,note,rep in[
 (167,'Example55 paired inverse sketch','The two increasing finite curve pieces are reflections in y=x. Original domain[−π/2,π/2]andrange[−5,1]swap under inversion.','graph'),
 (168,'Example55 forward sample table','Forward inputs−π/2,−π/4,0,π/4,π/2give−5,approximately−3.2,−2,approximately−.8,1. The middle non-integer ordinates are rounded to1decimal place.','table'),
 (169,'Example55 swapped inverse table','The inverse table swaps the source sample pairs. Its rounded−3.2and−.8inputs are approximate illustrations,not exact arguments returning±π/4. Exact endpoint pairs remain valid.','table')]:
    figures.append({'item_id':f'8227:TB:YM:C4:Teaching-figure:{n}','item_kind':'teaching-figure','exercise':'Teaching figure','item_number':str(n),
      'pdf_page':219,'printed_page':207,'source_label':label,'parent_item_id':'8227:TB:YM:C4:Example:55','parent_subpart':'b',
      'notes':note,'what_it_shows':note,'assessed_8227_demand_ids':[],'component_demand_ids':[],
      'teaches_8227_demand_ids':[INV,INVSKETCH],'representation':rep,'source_evidence':ev(219),'learner_display':False,
      'value_level_scope_decisions':[{'rule_id':'8227:QUAL08','status':'within','quoted_value':'f=3tan(x/2)−2;−π/2≤x≤π/2',
        'reason':'The actual argumentx/2lies inside[−π/4,π/4],so tangent is defined andstrictly increasing at alloriginal endpoints/interior points.'}],
      'value_level_scope_review_status_r5':'author original restriction androunded sample table read2026-11-18;independent check pending',
      'exam_representation_check':{'status':'final cross-book/examination comparison pending','examination_part_ids':[],
        'relation':'Source teaching/solution graph andtables;no official examination award orfrequency claim.'},
      'mathematical_feature_review':{'status':'author reflection/endpoint reasoning andnumerical inverse composition checked;independent acceptance pending',
        'method':'Forward values come from the original source function. Exact endpoint coordinates swap. Independent math composition checks use the original function andderived inverse;rounded interior table entries are explicitly approximate.'}})
pages=[]
for page in[219,220]:
    pages.append({'pdf_page':page,'printed_page':page-12,'chapter':4,'page_status':'items enumerated',
      'item_ids':[r['item_id']for r in answers if r['source_pdf_page']==page]+[r['item_id']for r in figures if r['pdf_page']==page],
      'continuation_item_ids':[],'source_evidence':ev(page),
      'non_item_content':'All formal tasks andthree separate Example55solution figures/tables enumerated. Try54Q2/Q3start onPDF219;the previous page has the completeQ1stem. Answer-key sketches are attached to their assessed parts,not counted as additional chapter teaching items.',
      'reader':'Codex author','date':'2026-11-18'})
if __name__=='__main__':
    for name,data in[
      ('answers-YM-C4-inverse-functions.json',{'scope':'All6formal items and18requested outputs onPDF219–220;restricted inverse formulas,sketch features andoriginal domains preserved.','items':answers}),
      ('census-YM-C4-inverse-functions.json',{'book':'YM','book_id':'8227-SRC-017','chapter':4,'source_path':SRC,'source_sha256':SHA,
        'scope':'PDF219–220;allformal tasks andthree separate mathematical teaching figures/tables.','new_items':figures,'corrections':[],'pages':pages})]:
        (W/'tools/textbook-r5'/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
    print(len(answers),'items;',len(figures),'figures;',sum(len(r['subparts'])for r in answers),'outputs')
