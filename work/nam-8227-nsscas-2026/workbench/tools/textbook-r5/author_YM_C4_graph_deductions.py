"""R5 source-page census and independent results for YM PDF177–180."""
import json,hashlib
from pathlib import Path
from author_YM_C4_trig_graphs import graph,value,reasoning,BASIC,FEATURE,INTERPRET,SKETCH,RANGE
W=Path(__file__).resolve().parents[2];ROOT=W.parents[2]
SRC='Y=mc as textbook.pdf';SHA='0b44ad3b67b1ea3de90cba780382d77deef347fae683cf6e28677f36c17a724f'
EXACT='8227:2020:M1:T6:O03:D01'
def ev(page):
    name=f'YM-key-C4-{page}'if page==605 else'YM-key-C4-606-609'if page==606 else'YM-C4-177'
    p=W/f'checks/r5/textbooks/{name}.png'
    return {'path':str(p.relative_to(ROOT)),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
answers=[]
def add(kind,n,page,note,parts,direct,components=None,qualifiers=None):
    for part in parts:
        kp=part.pop('key_page_override',page);pp=part.pop('source_page_override',None)or page
        part.update(source_pdf_page=pp,source_evidence=ev(pp),answer_pdf_page=kp,answer_printed_page='A'+str(kp-586)if kp>=602 else kp-12,key_evidence=ev(kp))
    row={'item_id':f'8227:TB:YM:C4:{kind}:{n}','source_pdf_page':page,'notes':note,
      'assessed_8227_demand_ids':direct,'component_demand_ids':components or[],
      'mapping_rationale':'Keep the explicit graph deduction,parameter,range,comparison or exact-ratio output direct. A method used to derive it is a component unless specifically demanded. Distinguish reading/graph reasoning from a full bounded-equation task.',
      'exam_style':False,'exam_style_basis':'Ordinary worked Example/TryNow/teaching illustration,without an examination attribution.',
      'value_level_scope_decisions':qualifiers or[{'rule_id':'8227:QUAL03','status':'not applicable','quoted_value':note,'reason':'This graph-deduction/ratio task does not ask a full bounded trigonometric equation solution set.'}],
      'precision_angle_check':{'source':'These graph coordinates,periods,gradients andspecial-angle ratios are exactpi/surd results. Degree/radian units follow the actual source axes; no rounding of exact values is introduced.',
       'comparison':'Later NSSCAS resources must retain actual answer instructions; a graph label andthe asked function must agree,andunwritten coefficient-sign conventions cannot reject valid alternatives.'},
      'expected_subpart_labels':[p['subpart']for p in parts],'subparts':parts}
    answers.append(row);return row

newpoint=reasoning('c','(−pi/2,−3)',
 'The known maximum is(pi/2,3),so its line through the origin isy=6x/pi. Both curve3sinxandthis line are odd. Reflecting the known maximum in the origin gives(−pi/2,−3),the remaining new intersection besides the already known origin andmaximum. On(0,pi),sinx/xstrictlydecreases,so the positive nonzero crossing is unique; oddness gives the negative one.',177,'matches')
add('Example',15,177,'Sketch3sinxon−pi..pi,find the line through its maximum andthe origin,andidentify the remaining new line/curve intersection using symmetry.',
 [graph('a','sin','3','1','0','-pi','pi','radian',177,{'window_zero_locations':'FiniteSet(-pi,0,pi)','window_global_max_locations':'FiniteSet(pi/2)','window_global_min_locations':'FiniteSet(-pi/2)'}),
  value('b','3/(pi/2)','6/pi',177,'Use the independently derived maximum(pi/2,3)andthe origin tocalculate slope3/(pi/2).'),newpoint],[BASIC,FEATURE,INTERPRET,SKETCH])
row=add('Try-Now-15',1,177,'Sketch−2cosxon−pi..piandstate itsy-axis intersection. The key curve has the correct negative-cosine shape but its printed equation label drops the minus sign.',
 [graph('sketch','cos','-2','1','0','-pi','pi','radian',605,{'y_intercept':'-2','window_global_min_locations':'FiniteSet(0)','window_global_max_locations':'FiniteSet(-pi,pi)','window_zero_locations':'FiniteSet(-pi/2,pi/2)'}),value('y-axis-intersection','Tuple(0,-2*cos(0))','Tuple(0,-2)',605)],[BASIC,INTERPRET,SKETCH])
row['subparts'][0].update(question_formula_normalised='-2*cos(x)',printed_key_formula_normalised='2*cos(x)',source_defect_id='TB-YM-C4-Try15-Q1-LABEL-SIGN')
line=value('line-sketch','Tuple(-S(1)/2,pi/2)','Tuple(-S(1)/2,pi/2)',605,'Rearrange x+2y=pi to y=−x/2+pi/2. Its requested0..pi segment joins(0,pi/2)to(pi,0),as in the source key.')
line['operation']={'kind':'line-from-relation','operands':['x+2*y-pi']}
line['additional_operations']={'line-endpoints':{'kind':'identity','operands':['Tuple(Tuple(0,pi/2),Tuple(pi,0))']}}
add('Try-Now-15',2,177,'Sketch3cos2xandthe linex+2y=pion the same radian axes0..pi; no root count orintersection solution is requested.',
 [graph('curve-sketch','cos','3','2','0','0','pi','radian',605,{'window_global_max_locations':'FiniteSet(0,pi)','window_global_min_locations':'FiniteSet(pi/2)','window_zero_locations':'FiniteSet(pi/4,3*pi/4)'}),line],[BASIC,INTERPRET,SKETCH])
rootcount=value('b-root-count','0','3',605)
rootcount['operation']={'kind':'trig-line-root-count','operands':['2','1','0','-1/pi','1','0','2*pi']}
rootcount['method']='Count intersections ofy=2sinxandy=1−x/pi. The residual derivative2cosx+1/pihas two zeros in0..2pi,so it has three monotone pieces; their endpoint signs eachgive one crossing. Outside0..2pi,no additional root occurs:amplitude bounds confine possiblex to−pi..3pi,andthe sine/line signs disagree on the two exterior subintervals.'
add('Try-Now-15',3,177,'Sketch2sinxon0..2pi,add a suitable line to count all real roots of2pi sinx=pi−x,andstate that line equation.',
 [graph('a','sin','2','1','0','0','2*pi','radian',605,{'window_zero_locations':'FiniteSet(0,pi,2*pi)','window_global_max_locations':'FiniteSet(pi/2)','window_global_min_locations':'FiniteSet(3*pi/2)'}),
  rootcount,value('c-line-equation','(pi-x)/pi','1-x/pi',605,'Divide the original equation bypi:2sinx=1−x/pi. Thus the line is y=1−x/pi,matching the plotted source line.')],[BASIC,INTERPRET,SKETCH])

# The source does not state positive frequency. Preserve genuine equivalent
# coefficients rather than turn a canonical printed choice into an exclusive key.
b=value('a-b','0','FiniteSet(2)',178)
b.update(operation={'kind':'cos-input-multipliers','angle_unit':'radian','operands':['pi']},difference_disposition='key incomplete',
 difference_reason='The displayed cosine hasperiodpi,so|b|=2. Bothb=2andb=−2produce exactlythe samefunction. No b>0condition appears in this source question.',
 method='Read one cosine cycle over0..pi,derive|b|=2pi/pi=2,andretain both signs becausecos(−2x)=cos2x. The printed key gives onlythe positive canonical coefficient.',source_defect_id='TB-YM-C4-Example16-B-SIGN-CONVENTION')
b['assertions']=[{'expression':'cos(-2*x)-cos(2*x)','expected':'0'}]
intersections=value('g','0','FiniteSet(pi/6,5*pi/6)',178,'Solve sinx=cos2xusingcos2x=1−2sin²x. The factorisation(2sinx−1)(sinx+1)=0leaves sinx=1/2on0..pi,with both exact intersections.')
intersections['operation']={'kind':'bounded-trig-equation','operands':['sin(x)-cos(2*x)','0','pi']}
add('Example',16,178,'Given f=sinaxandg=cosbxon0..pi,read coefficients,base period,Acoordinate,value difference,range,inequality interval andequal-value points. The displayed sine is a halfcycle; the cosine is a fullcycle. The sign ofb is not specified.',
 [value('a-a','2*pi/(2*(pi-0))','1',178,'The displayed sine hasone positive halfcycle over0..pi,so its base period is2piandthe positive initial slope fixes a=1.'),b,
  value('b-period-f','2*(pi-0)','2*pi',178),value('c-A-abscissa','pi-pi/6','5*pi/6',178),value('d','sin(pi/2)-cos(2*pi/2)','2',178),
  graph('e-range','sin','1','1','0','0','pi','radian',178,{'window_range':'Interval(0,1)'},status='matches'),
  reasoning('f','pi/6≤x≤5pi/6','Withs=sinx≥0on0..pi, f−g=s−(1−2s²)=(2s−1)(s+1). Thissign is nonnegative exactlywhens≥1/2,which gives the closed intervalpi/6..5pi/6; this agrees with the shaded/upper-curve source description.',178,'matches'),
  intersections],
 [FEATURE,INTERPRET,RANGE],qualifiers=[{'rule_id':'8227:QUAL07','status':'within','quoted_value':'f(x)=sinxon0≤x≤pi','reason':'Simple half-cycle range[0,1],not the unrestricted sine range[−1,1].'}])

pair=value('parameter-triples','0','FiniteSet(Tuple(6,2,3))',605)
pair.update(operation={'kind':'sin-parameter-sign-pairs','angle_unit':'radian','operands':['9','-3','pi','1']},difference_disposition='key incomplete',
 difference_reason='The question does not requirea>0orb>0. The source grapha=6,b=2,c=3also has the identical representationa=−6,b=−2,c=3.',
 method='Frommax9,min−3deriveoffset3and|a|=6. Two cycles on0..2pigive|b|=2. The initial rise requiresab>0,leaving exactlythe two simultaneous-sign triples; compare the single printed canonical triple.',
 source_defect_id='TB-YM-C4-Try16-Q1-SIGN-PAIR-CONVENTION')
pair['assertions']=[{'expression':'(-6*sin(-2*x)+3)-(6*sin(2*x)+3)','expected':'0'}]
add('Try-Now-16',1,179,'Read a sinbx+cfrom a graph withmax9,min−3,intercept3,two cycles on0..2piandinitial rise. Both simultaneous-sign parameter triples are valid unless one coefficient sign is restricted.',[pair],[FEATURE,INTERPRET])
add('Try-Now-16',2,179,'For a+b sinx,read intercept−2andmaximum1on the rising sine branch; recovera=−2andb=3with fixed positive input multiplier1.',
 [value('parameters','Tuple(-2,1-(-2))','Tuple(-2,3)',605,'Atx=0,the intercept isa=−2. The displayed initial rise fixes b>0,andthe maximum a+b=1thereforegivesb=3.')],[INTERPRET])
add('Try-Now-16',3,179,'Given f=−2sinxandg=tanxon0..3pi/2,find the labelled minimumT,periodofg,rangeoff,andBfromA=(2pi/3,−sqrt3). Keep tangent undefined atpi/2and3pi/2; the stated range belongs tof.',
 [value('a','Tuple(pi/2,-2*sin(pi/2))','Tuple(pi/2,-2)',605,'The labelled T is the interior minimum wherecosx=0andf=−2; the endpoint at3pi/2is not this labelled turningpoint.'),
  graph('b','tan','1','1','0','0','3*pi/2','radian',605,{'period':'pi'},status='matches'),graph('c','sin','-2','1','0','0','3*pi/2','radian',606,{'window_range':'Interval(-2,2)'},status='matches'),
  value('d','Tuple(2*pi-2*pi/3,-(-sqrt(3)))','Tuple(4*pi/3,sqrt(3))',606,'Underx→2pi−x,both−2sinxandtanxchange sign,soAreflects toB=(4pi/3,sqrt3). This asks the named pointB,not a claim thatO,A,Bare the only intersections; both curves also pass through(pi,0).')],
 [FEATURE,INTERPRET,RANGE],qualifiers=[{'rule_id':'8227:QUAL07','status':'within','quoted_value':'f(x)=−2sinxon0≤x≤3pi/2','reason':'Simple restricted graph coversboth extrema,so range[−2,2]. The tangent domain separatelyexcludes its poles.'}])

# Two unnumbered worked teaching illustrations in the special-angle table.
add('Worked-illustration',2,180,'The45degree isosceles right triangle has legs1and1:derive its hypotenusesqrt2andall three exact45degree ratios,including rationalised forms.',
 [value('hypotenuse','sqrt(1**2+1**2)','sqrt(2)',180),value('sin45','1/sqrt(2)','sqrt(2)/2',180),value('cos45','1/sqrt(2)','sqrt(2)/2',180),value('tan45','S(1)/1','1',180)],[EXACT])
add('Worked-illustration',3,180,'Bisect an equilateral side2triangle to get a30/60right triangle withhypotenuse2andshortleg1; derive the longlegsqrt3andthe six exact ratios.',
 [value('long-leg','sqrt(2**2-1**2)','sqrt(3)',180),value('sin30','S(1)/2','1/2',180),value('cos30','sqrt(3)/2','sqrt(3)/2',180),
  value('tan30','1/sqrt(3)','sqrt(3)/3',180),value('sin60','sqrt(3)/2','sqrt(3)/2',180),value('cos60','S(1)/2','1/2',180),value('tan60','sqrt(3)/1','sqrt(3)',180)],[EXACT])
new=[]
for row in answers[-2:]:
    new.append({'item_id':row['item_id'],'item_kind':'worked-illustration','exercise':'Worked illustration','item_number':row['item_id'].split(':')[-1],
      'pdf_page':180,'printed_page':168,'notes':row['notes'],'assessed_8227_demand_ids':[EXACT],'component_demand_ids':[],
      'representation':'diagram','source_evidence':ev(180),'answer_key':{'available':True,'pdf_pages':[180],'printed_pages':[168],
       'locator':'Inline special-angle worked triangle/table','source_path':SRC,'source_sha256':SHA}})

specs=[
 (177,'Example15sine sketch','3sinxon−pi..piwithlabelled extrema(pi/2,3),(−pi/2,−3).','Example:15',[BASIC,FEATURE,SKETCH],'graph'),
 (177,'Example15sine/line intersection sketch','Liney=6x/pipasses throughorigin andboth displayed extrema of3sinx; it is an intersection line,not tangent at the maximum.','Example:15',[INTERPRET,SKETCH],'graph'),
 (178,'Example16given two-curve graph','f=sinaxshows one positive halfcycle0..pi;g=cosbxshows one cycle withminimum−1atpi/2. First intersectionpi/6andotherintersectionAare labelled.','Example:16',[FEATURE,INTERPRET,RANGE],'graph'),
 (178,'Example16base sine comparison','Base sine comparison drawn on0..2pireminds that the given0..piplot was onlyhalf a sine cycle.','Example:16',[FEATURE,INTERPRET],'graph'),
 (178,'Example16base cosine comparison','Base cosine comparison on0..2pihasperiod2pi; the given ggraph hasperiodpi. Cosine frequency sign remains unidentifiable without a positivity convention.','Example:16',[FEATURE,INTERPRET],'graph'),
 (178,'Example16inequality comparison plot','Given curves repeated withguide lines atpi/6and5pi/6bound the interval wheref≥g.','Example:16',[INTERPRET],'graph'),
 (179,'TryNow16question1given sine graph','Max9,min−3,intercept3andtwo cycles over0..2piwithinitial rise constrain the function; simultaneous signs ofa,bremain ambiguous.','Try-Now-16:1',[FEATURE,INTERPRET],'graph'),
 (179,'TryNow16question2given shifted sine','Graphy=a+b sinxhasintercept−2andpeak1to the right on the rising branch; these identifya,bwithout a free input-frequency sign.','Try-Now-16:2',[INTERPRET],'graph'),
 (179,'TryNow16question3sine/tangent graph','−2sinxandtanxon0..3pi/2withminimumT,intersectionsA,B,andpolespi/2,3pi/2. The unlabelled common point(pi,0)is also visible.','Try-Now-16:3',[FEATURE,INTERPRET,RANGE],'graph'),
 (180,'Right-triangle ratio definitions','Anatomical labelsopposite,adjacent,hypotenuse accompanysinθ,cosθ,tanθratio definitions; prerequisite support,not a standalone exact-angle question.',None,[],'diagram'),
 (180,'Special-angle triangle/table','45degree legs1/1hypotenusesqrt2andbisected30/60equilateral triangle side2yield exact ratio tables; worked calculations are separate source-item records.',None,[EXACT],'diagram')]
for n,(page,label,note,parent,teaches,rep)in enumerate(specs,52):
    row={'item_id':f'8227:TB:YM:C4:Teaching-figure:{n}','item_kind':'teaching-figure','exercise':'Teaching figure','item_number':str(n),
      'pdf_page':page,'printed_page':page-12,'source_label':label,'parent_item_id':f'8227:TB:YM:C4:{parent}'if parent else None,
      'notes':note,'what_it_shows':note,'assessed_8227_demand_ids':[],'component_demand_ids':[],'teaches_8227_demand_ids':teaches,
      'representation':rep,'source_evidence':ev(page),'learner_display':False,
      'value_level_scope_decisions':[{'rule_id':'8227:QUAL03','status':'not applicable','quoted_value':note,'reason':'Figure teaches graph/ratio interpretation,not a full bounded-equation response.'}],
      'value_level_scope_review_status_r5':'author mathematical labels/relations read; independent check pending',
      'exam_representation_check':{'status':'representation comparison pending final cross-book family synthesis','examination_part_ids':[],
       'relation':'Textbook source evidence alone does not establish NSSCAS same-type examination demand orfrequency.'},
      'mathematical_feature_review':{'status':'author independently checked parent values/relations; source-sign ambiguities explicit; independent acceptance pending',
       'method':'Use the actual labelled extrema,periods,intercepts,angular intervals andtriangle lengths; confirm from fixed-source symbolic derivations rather than measuring schematic pixels.'}}
    if not teaches:row['supports_8227_demand_ids']=[EXACT];row['support_role']='Prior-knowledge right-triangle definitions support later exact ratios; they are not direct exact-angle demand coverage.'
    if n==62:row['parent_item_ids']=['8227:TB:YM:C4:Worked-illustration:2','8227:TB:YM:C4:Worked-illustration:3']
    new.append(row)
pages=[]
for page in range(177,181):
    own=[r['item_id']for r in answers if r['source_pdf_page']==page]+[r['item_id']for r in new if r['pdf_page']==page and r['item_kind']=='teaching-figure']
    pages.append({'pdf_page':page,'printed_page':page-12,'chapter':4,'page_status':'items enumerated','item_ids':own,'continuation_item_ids':[],
      'source_evidence':ev(page),'non_item_content':'All formal task starts,worked teaching calculations andmathematical diagrams are enumerated; ordinary explanatory prose introduces their methods.',
      'reader':'Codex author','date':'2026-11-17'})
if __name__=='__main__':
    for name,data in[
      ('answers-YM-C4-graph-deductions.json',{'scope':'All formal tasks onPDF177–179plus two unnumbered special-angle worked illustrations on180. Missing coefficient-sign conventions remain explicit; canonical key choices are not exclusive.', 'items':answers}),
      ('census-YM-C4-graph-deductions.json',{'book':'YM','book_id':'8227-SRC-017','chapter':4,'source_path':SRC,'source_sha256':SHA,
       'scope':'PDF177–180inclusive; every task,worked illustration andmathematical graph/triangle/table explicitlyenumerated.','new_items':new,'corrections':[],'pages':pages})]:
        (W/'tools/textbook-r5'/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
    print(len(answers),'response items;',len(new)-2,'figures;',sum(len(r['subparts'])for r in answers),'output records')
