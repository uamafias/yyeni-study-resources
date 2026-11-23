"""R5 source readings for all trig investigations and graph tasks,PDF165–176.
Every requested investigation row/graph has a labelled result; blank source
tables stay author-derived rather than being presented as publisher answers.
"""
import json,hashlib
from pathlib import Path
W=Path(__file__).resolve().parents[2];ROOT=W.parents[2]
SRC='Y=mc as textbook.pdf';SHA='0b44ad3b67b1ea3de90cba780382d77deef347fae683cf6e28677f36c17a724f'
T=lambda tail:'8227:2020:M1:T6:'+tail
BASIC=T('O01:D01');FEATURE=T('O02:D01');INTERPRET=T('O02:D02');SKETCH=T('O02:D03');RANGE='8227:2020:M1:T3:O02:D02'
KEY_PAGES=list(range(602,616))
def ev(page):
    if page in[603,604,605]:name=f'YM-key-C4-{page}'
    elif 606<=page<=609:name='YM-key-C4-606-609'
    elif 610<=page<=613:name='YM-key-C4-610-613'
    elif page in[614,615]:name='YM-key-C4-614-615'
    else:name=f'YM-C4-{165+4*((page-165)//4)}'
    p=W/f'checks/r5/textbooks/{name}.png'
    return {'path':str(p.relative_to(ROOT)),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
def graph(label,family,a,b,c,lo,hi,unit,key_page,features=None,source_page=None,at=None,status='sketch'):
    row={'subpart':label,'operation':{'kind':'trig-features','family':family,'angle_unit':unit,'operands':[a,b,c,lo,hi],'at':at or[]},
      'check_mode':status,'key_page_override':key_page,'source_page_override':source_page,
      'method':'Independently derive amplitude from absolute output scale,positive period from angular unit/input multiplier,and exact zeros,extrema,poles and endpoint values from the given function. Compare the specifically transcribed source graph/table features; do not join tangent branches across poles. Global and displayed-interval ranges remain distinct.'}
    if features is not None:row['printed_key_features']=features
    else:
        row.update(key_presence='no separate key',inspected_key_pdf_pages=KEY_PAGES,
          author_feature_derivation='The source provides a blank row/requested graph,not a separate answer. Exact feature equations are derived from the actual function and viewport. The complete chapter4answer sectionPDF602–615was inspected for investigation headings; none occurs. Printed outcome summaries are compared separately where present.')
    return row
def value(label,expr,key,key_page,method=None):
    return {'subpart':label,'operation':{'kind':'identity','operands':[expr]},'printed_key_normalised':key,'key_page_override':key_page,
      'method':method or'Solve from the original extrema/equations and check the requested scalar or coefficient vector against the independently transcribed printed result.'}
def reasoning(label,conclusion,derivation,key_page=None,status='no key'):
    row={'subpart':label,'verification_mode':'manual-derivation','author_comparison_status':status,
      'author_conclusion':conclusion,'author_derivation':derivation,'method':'Author mathematical reasoning from the original task; explicit source support/absence recorded. This logical comparison is not an automated proof.','key_page_override':key_page}
    if key_page is None:row.update(key_presence='no separate key',inspected_key_pdf_pages=KEY_PAGES)
    return row
answers=[];corrections=[]
def add(kind,n,page,note,parts,direct,range_quote=None):
    iid=f'8227:TB:YM:C4:{kind}:{n}'
    for p in parts:
        kp=p.pop('key_page_override',None);pp=p.pop('source_page_override',None)or page
        p.update(source_pdf_page=pp,source_evidence=ev(pp),answer_pdf_page=kp,answer_printed_page=kp-586 if kp and kp>=602 else kp-12 if kp else None,
          key_evidence=ev(kp if kp else 615))
        if kp and kp>=602:p['answer_printed_page']='A'+str(kp-586)
    decisions=[{'rule_id':'8227:QUAL03','status':'not applicable','quoted_value':note,'reason':'These are graph/feature/parameter tasks,not bounded trigonometric equations. The small-multiplier equation restriction is not imposed on graph periods.'}]
    if range_quote:decisions.append({'rule_id':'8227:QUAL07','status':'within','quoted_value':range_quote,'reason':'Range of a basic or simply transformed sine/cosine/tangent function,with any stated interval preserved. Viewport and mathematical domain are explicitly distinguished.'})
    row={'item_id':iid,'source_pdf_page':page,'notes':note,'assessed_8227_demand_ids':direct,'component_demand_ids':[],
      'mapping_rationale':'Classify the explicit graph,feature,range,parameter or explanation output. Software menu actions are procedure context,not a mathematical assessment objective. Do not attach implicit/parametric differentiation or trigonometric-equation demands to an explicit graph task.',
      'value_level_scope_decisions':decisions,'exam_style':False,'exam_style_basis':'Ordinary worked Example/TryNow/investigation; no examination attribution or exam-style label.',
      'precision_angle_check':{'source':'Degree graphs retain degree scales; radian graphs retainpi ticks. Examples11andTry11ask periods in both units; exact periods are compared under both representations.',
       'comparison':'A source graph window is not automatically a function-domain restriction. Where the function is expressly restricted,the sketch must stop at those endpoints. Tangent amplitude is undefined; it is never0.'},
      'expected_subpart_labels':[p['subpart']for p in parts],'subparts':parts}
    answers.append(row);return row

# Basic investigation: software setup/screenshot instructions are recorded as
# procedure,while each mathematical output is independently derived.
row=add('Investigation-basic-trig-graphs',1,165,'Set degree viewport−500..500and−4..4,plot sine,and complete its minimum,maximum,amplitude,period andrange table.',
 [graph('sine-graph','sin','1','1','0','-500','500','degree',None),
  graph('sine-table','sin','1','1','0','-500','500','degree',166,{'global_minimum':'-1','global_maximum':'1','amplitude':'1','period':'360','global_range':'Interval(-1,1)'},status='matches')],
 [BASIC,FEATURE,INTERPRET,RANGE],range_quote='y=sinx in degrees; function domain all real numbers,plot viewport−500≤x≤500')
row['procedural_subtasks']=[{'source_labels':['a','b','c'],'status':'Source menu/window/screenshot instructions read; mathematical function/window features independently computed. The proprietary application menu sequence is not an assessed mathematical output and was not executed.'}]
row=add('Investigation-basic-trig-graphs',2,166,'Repeat the degree plotting and feature table for cosine andtangent; tangent has no finite extrema oramplitude,and its poles must remain open.',
 [graph('cosine-graph','cos','1','1','0','-500','500','degree',None),graph('tangent-graph','tan','1','1','0','-500','500','degree',None),
  graph('cosine-table','cos','1','1','0','-500','500','degree',167,{'global_minimum':'-1','global_maximum':'1','amplitude':'1','period':'360','global_range':'Interval(-1,1)'},status='matches'),
  graph('tangent-table','tan','1','1','0','-500','500','degree',167,{'global_minimum':None,'global_maximum':None,'amplitude':None,'period':'180','global_range':'S.Reals'},status='matches')],
 [BASIC,FEATURE,INTERPRET,RANGE],range_quote='y=cosx,y=tanx in degrees; cosine range[−1,1],tangent rangeR with odd90degree poles excluded from its domain')
row['procedural_subtasks']=[{'source_labels':['d'],'status':'Repeat plotting/screenshot procedure forcosandtan; mathematical graphs andtable outputs recorded above.'}]
proof=reasoning('periodicity-explanation','All three functions are periodic:sine/cosine repeat after360degrees,tangent after180degrees.',
 'Adding360degrees leaves sine andcosine unchanged by the addition formulas. Adding180degrees changes both sine andcosine signs,so their ratio tangent is unchanged wherever defined. The repeated shapes in the wider graph illustrate these facts; finite screenshots alone are not a universal proof.',167,'matches')
row=add('Investigation-basic-trig-graphs',3,166,'Widen degree viewport to−9000..9000for sine,cosine,tangent,and motivate whether their graphs are periodic without mistaking wider viewing bounds for a changed period.',
 [*[graph(f'{family}-wide-graph',family,'1','1','0','-9000','9000','degree',None)for family in['sin','cos','tan']],proof],[BASIC,FEATURE])
row['procedural_subtasks']=[{'source_labels':['e'],'status':'Wide-window mathematical replots recorded; source screenshot procedure is contextual.'}]

# Transformed investigation: every requested table row includes its graph and
# all feature cells. Blank source rows never become invented printed answers.
parts=[]
for a in['1','2','3']:
    key={'global_maximum':'1','global_minimum':'-1','amplitude':'1','period':'360','window_global_max_locations':'FiniteSet(90)','window_global_min_locations':'FiniteSet(270)'}if a=='1'else None
    parts.append(graph(f'sin-output-factor-{a}','sin',a,'1','0','0','360','degree',170 if key else None,key,source_page=170))
row=add('Investigation-transformed-trig-graphs',1,169,'For output factors1,2,3,plot sine and complete maximum/minimum positions,sketch,amplitude andperiod. The sine1row is supplied; the other rows are blank.',parts,[FEATURE,INTERPRET,SKETCH])
row['procedural_subtasks']=[{'source_labels':['a','b','c'],'status':'Degree window−500..500andverticalwindow−4..4are specified; row sketches summarise a0..360degree cycle,while local QA retains both the requested source window andglobal features.'}]
for p in row['subparts']:
    source_view=dict(p['operation']);source_view['operands']=[*source_view['operands'][:3],'-500','500']
    p['additional_operations']={'source_plot_view':source_view};p['plot_y_bounds']=['-4','4']
parts=[]
for family in['cos','tan']:
 for a in['1','2','3']:
    key=None
    if a=='1':key={'global_maximum':'1','global_minimum':'-1','amplitude':'1','period':'360','window_global_max_locations':'FiniteSet(0,360)','window_global_min_locations':'FiniteSet(180)'}if family=='cos'else{'global_maximum':None,'global_minimum':None,'amplitude':None,'period':'180'}
    parts.append(graph(f'{family}-output-factor-{a}',family,a,'1','0','0','360','degree',170 if key else None,key))
row=add('Investigation-transformed-trig-graphs',2,170,'Repeat output-factor1,2,3tables andsketches for cosine andtangent; the two base-function rows are supplied. Tangent output scaling changes steepness,notamplitude orperiod.',parts,[FEATURE,INTERPRET,SKETCH])
for p in row['subparts']:
    source_view=dict(p['operation']);source_view['operands']=[*source_view['operands'][:3],'-500','500']
    p['additional_operations']={'source_plot_view':source_view};p['plot_y_bounds']=['-4','4']
add('Investigation-transformed-trig-graphs',3,170,'Explain the effect of positive output multiplierausing the source values1,2,3; do not add a negative-multiplier requirement to this investigation.',
 [reasoning('effect-of-a','For sine/cosine,the positive factorascales vertical distances andamplitude byawithperiod unchanged. For tangent,it scales ordinates/steepness whileamplitude remains undefined andperiod unchanged.',
 'For a=1,2,3,the ordinate is multiplied bya. Sine/cosine ranges become[−a,a],so amplitudea. Multiplying outputs does not change where a fullcycle repeats orwhere tangent is undefined. These conclusions agree with the printed positive-asummary table; negative-a reflection is a separate worked-example branch.',172,'matches')],[INTERPRET])
parts=[]
for family in['sin','cos','tan']:
 for b in['1','2','3','1/2','1/3']:
    p=graph(f'{family}-input-factor-{b.replace("/","over")}',family,'1',b,'0','-500','500','degree',None,source_page=171)
    if b=='1/3'and family in['sin','cos']:
        p['source_window_limit']='Width1000degrees is less than the1080degree period. Forcos(x/3),the global minima at±540are outside the stated window; infer global features analytically or use a wider instructional view. Do not claim the source window displays them.'
    parts.append(p)
add('Investigation-transformed-trig-graphs',4,171,'Plot andcomplete15rows for sine,cosine,tangent with input factors1,2,3,1/2,1/3. Preserve the source−500..500degree viewport anddistinguish global extrema from visible ones.',parts,[FEATURE,INTERPRET,SKETCH])
add('Investigation-transformed-trig-graphs',5,171,'Explain how the positive source input factors1,2,3,1/2,1/3affect trig graph periods andhorizontal scale.',
 [reasoning('effect-of-b','For sine/cosine,P=360/bdegrees; for tangent,P=180/bdegrees. Larger positivebcompresses horizontally; smaller positivebstretches. Vertical amplitude is unchanged.',
 'A full base-function argument increment is360degrees forsin/cosor180fortan. Since the argument isbx,the needed x increment is that increment dividedbyb. The source factors are positive/nonzero; use absolute value if later extending to negativeb. The printed summary agrees for this positive domain.',172,'matches')],[FEATURE,INTERPRET])
parts=[]
for family in['sin','cos']:
 for c in['0','1','2','-1','-2']:
    parts.append(graph(f'{family}-vertical-shift-{c}',family,'1','1',c,'0','360','degree',None,source_page=172))
row=add('Investigation-transformed-trig-graphs',6,172,'Complete10rows andsketches for sine/cosine shifted vertically by0,1,2,−1,−2; minimum/maximum translate while amplitude andperiod stay fixed.',parts,[FEATURE,INTERPRET,SKETCH])
for p in row['subparts']:
    source_view=dict(p['operation']);source_view['operands']=[*source_view['operands'][:3],'-500','500']
    p['additional_operations']={'source_plot_view':source_view};p['plot_y_bounds']=['-4','4']
add('Investigation-transformed-trig-graphs',7,172,'Explain howc=1,2,−1,−2changes the graphs ofsinx+candcosx+c.',
 [reasoning('effect-of-c','Addingctranslates the graph up forc>0anddown forc<0. Maximum/minimum increase byc; amplitude1andperiod360degrees stay unchanged.',
 'Every ordinate becomes its previous value plusc,so the difference between extrema andthe x-spacing of a repeat are unchanged. This matches the printed rowsa+c,−a+cfor the source positivea=1. It does not change the input orangle unit.',172,'matches')],[INTERPRET])

reflection=lambda label,kp:reasoning(label,'Reflection in the x-axis.',
 'Replacing f(x)by−f(x)maps each point(x,y)to(x,−y),so the paired curves are reflections in the x-axis with the same domain. Undefined tangent points stay undefined.',kp,'matches')
add('Example',10,168,'Sketch tanxand−tanxon−pi..pianddescribe their reflection; the displayed value table includes undefined±pi/2.',
 [graph('a-tan','tan','1','1','0','-pi','pi','radian',168,{'window_poles':'FiniteSet(-pi/2,pi/2)','window_zero_locations':'FiniteSet(-pi,0,pi)','sample_values':'Tuple(0,1,None,-1,0,1,None,-1,0)'},at=['-pi','-3*pi/4','-pi/2','-pi/4','0','pi/4','pi/2','3*pi/4','pi']),
  graph('a-minus-tan','tan','-1','1','0','-pi','pi','radian',168,{'window_poles':'FiniteSet(-pi/2,pi/2)','sample_values':'Tuple(0,-1,None,1,0,-1,None,1,0)'},at=['-pi','-3*pi/4','-pi/2','-pi/4','0','pi/4','pi/2','3*pi/4','pi']),reflection('b',168)],[BASIC,INTERPRET,SKETCH])
add('Try-Now-10',1,168,'Sketch sinxand−sinxon−pi..piandspecify the transformation between the two curves.',
 [graph('a-sin','sin','1','1','0','-pi','pi','radian',603,{'window_zero_locations':'FiniteSet(-pi,0,pi)','window_global_max_locations':'FiniteSet(pi/2)','window_global_min_locations':'FiniteSet(-pi/2)'}),
  graph('a-minus-sin','sin','-1','1','0','-pi','pi','radian',603,{'window_zero_locations':'FiniteSet(-pi,0,pi)','window_global_max_locations':'FiniteSet(-pi/2)','window_global_min_locations':'FiniteSet(pi/2)'}),reflection('b',603)],[BASIC,INTERPRET,SKETCH])
add('Try-Now-10',2,168,'Sketch cosxand−cosxon−360..0degreesanddescribe the reflection; retain the degree coordinate unit.',
 [graph('a-cos','cos','1','1','0','-360','0','degree',603,{'window_global_max_locations':'FiniteSet(-360,0)','window_global_min_locations':'FiniteSet(-180)','window_zero_locations':'FiniteSet(-270,-90)'}),
  graph('a-minus-cos','cos','-1','1','0','-360','0','degree',603,{'window_global_max_locations':'FiniteSet(-180)','window_global_min_locations':'FiniteSet(-360,0)'}),reflection('b',603)],[BASIC,INTERPRET,SKETCH])

parts=[]
for label,family,a,b,c,features in[
 ('a','sin','4','1/3','-2',{'global_minimum':'-6','global_maximum':'2','amplitude':'4','period':'1080','y_intercept':'-2'}),
 ('b','cos','-5','4','6',{'global_minimum':'1','global_maximum':'11','amplitude':'5','period':'90','y_intercept':'1'}),
 ('c','tan','3','2','1',{'global_minimum':None,'global_maximum':None,'amplitude':None,'period':'90','y_intercept':'1'})]:
    parts.append(graph(label+'-features',family,a,b,c,'0','1080','degree',173,features,status='matches'))
    base_period='2*pi'if family!='tan'else'pi'
    parts.append(value(label+'-period-radians',f'({base_period})/({b})','6*pi'if label=='a'else'pi/2',173,'Derive the period in radians independently from the argument multiplier; compare the source exactpi result.'))
add('Example',11,173,'For4sin(x/3)−2,6−5cos4xand3tan2x+1,find extrema,amplitude,period in both angular units,andy-intercept. Negative cosine scale swaps the extrema labels; tangent has no amplitude.',parts,[FEATURE,INTERPRET])
parts=[]
for label,family,a,b,c,features,kp,radkey in[
 ('a','cos','9','1/5','-5',{'global_minimum':'-14','global_maximum':'4','amplitude':'9','period':'1800','y_intercept':'4'},603,'10*pi'),
 ('b','sin','-8','2','3',{'global_minimum':'-5','global_maximum':'11','amplitude':'8','period':'180','y_intercept':'3'},603,'pi'),
 ('c','tan','-2','1/2','-3',{'global_minimum':None,'global_maximum':None,'amplitude':None,'period':'360','y_intercept':'-3'},604,'2*pi')]:
    parts.append(graph(label+'-features',family,a,b,c,'0','1800','degree',kp,features,status='matches'))
    parts.append(value(label+'-period-radians',f'({"pi"if family=="tan"else"2*pi"})/({b})',radkey,kp))
add('Try-Now',11,173,'For9cos(x/5)−5,3−8sin2xand−2tan(x/2)−3,find extrema,amplitude,degree/radian periods,andy-intercepts. Parts(a),(b)keys arePDF603and(c)PDF604.',parts,[FEATURE,INTERPRET])
row=add('Example',12,174,'Initial function3cos2x−1on0..2pi:find extrema,amplitude,period,range. Part(c)explicitlychanges the requested function to3cosx+2; the source solution incorrectlyrepeats the initial graph.',
 [graph('a','cos','3','2','-1','0','2*pi','radian',174,{'global_minimum':'-4','global_maximum':'2'},status='matches'),
  graph('b','cos','3','2','-1','0','2*pi','radian',174,{'amplitude':'3','period':'pi','window_range':'Interval(-4,2)'},status='matches'),
  graph('c','cos','3','1','2','0','2*pi','radian',174,{'window_range':'Interval(-4,2)','y_intercept':'2','period':'pi'})],
 [FEATURE,INTERPRET,SKETCH,RANGE],range_quote='3cos2x−1on0≤x≤2pi; part(c)3cosx+2on0≤x≤2pi')
row['subparts'][-1]['source_defect_id']='TB-YM-C4-Example12c-DIFFERENT-FUNCTION'
add('Try-Now-12',1,175,'For2sinx+1on0..2pi,find extrema,amplitude,period,range,andthen sketch the samefunction over exactlyone full radian cycle.',
 [graph('a','sin','2','1','1','0','2*pi','radian',604,{'global_minimum':'-1','global_maximum':'3'},status='matches'),
  graph('b','sin','2','1','1','0','2*pi','radian',604,{'amplitude':'2','period':'2*pi','window_range':'Interval(-1,3)'},status='matches'),
  graph('c','sin','2','1','1','0','2*pi','radian',604,{'y_intercept':'1','window_global_max_locations':'FiniteSet(pi/2)','window_global_min_locations':'FiniteSet(3*pi/2)','window_zero_locations':'FiniteSet(7*pi/6,11*pi/6)'})],
 [FEATURE,INTERPRET,SKETCH,RANGE],range_quote='2sinx+1on0≤x≤2pi')
add('Try-Now-12',2,175,'Sketch four degree graphs on0..360andstate amplitude/period:4cosx,3sin2x,3−cos3x,sin(x/2)−2. The last shows onlyhalf its720degree cycle.',
 [graph('a','cos','4','1','0','0','360','degree',604,{'amplitude':'4','period':'360','window_global_max_locations':'FiniteSet(0,360)','window_global_min_locations':'FiniteSet(180)'}),
  graph('b','sin','3','2','0','0','360','degree',604,{'amplitude':'3','period':'180','window_global_max_locations':'FiniteSet(45,225)','window_global_min_locations':'FiniteSet(135,315)'}),
  graph('c','cos','-1','3','3','0','360','degree',604,{'amplitude':'1','period':'120','window_global_max_locations':'FiniteSet(60,180,300)','window_global_min_locations':'FiniteSet(0,120,240,360)'}),
  graph('d','sin','1','1/2','-2','0','360','degree',604,{'amplitude':'1','period':'720','window_range':'Interval(-2,-1)','window_global_max_locations':'FiniteSet(180)','sample_values':'Tuple(-2,-1,-2)'},at=['0','180','360'])],[FEATURE,INTERPRET,SKETCH])
add('Example',13,175,'For5tan4x,state the periodandsketch from0toone period. Worked table/axis explicitlyuse degrees(0..45),with a pole at22.5; record that unit rather than assume radians from the unlabelled formula.',
 [value('a-period-degrees','180/4','45',175),
  graph('b','tan','5','4','0','0','45','degree',175,{'window_poles':'FiniteSet(45/2)','window_zero_locations':'FiniteSet(0,45)','y_intercept':'0'})],[FEATURE,SKETCH])
add('Try-Now-13',1,176,'For4tan6x,state the periodandsketch0..one period; use the key degree convention0..30with asymptote15degrees,andretain the equivalentpi/6radian period.',
 [value('a-period-degrees','180/6','30',604),graph('b','tan','4','6','0','0','30','degree',604,{'window_poles':'FiniteSet(15)','window_zero_locations':'FiniteSet(0,30)','sample_values':'Tuple(0,4*sqrt(3),-4*sqrt(3),0)'},at=['0','10','20','30'])],[FEATURE,SKETCH])
row=add('Try-Now-13',2,176,'Sketch f(x)=3tan(x/2)−2with expresslyrestricted domain−pi/2≤x≤pi/2. This finite branch has endpoints(−pi/2,−5),(pi/2,1),andno internal pole. The printed key isPDF605,not604.',
 [graph('sketch','tan','3','1/2','-2','-pi/2','pi/2','radian',605,{'y_intercept':'-2','sample_values':'Tuple(-5,-2,1)','window_poles':'FiniteSet()'},at=['-pi/2','0','pi/2'])],[SKETCH])
row['subparts'][0]['author_source_graph_comparison']={'status':'key incomplete','observed_features':'The printed curve continues below/left of the labelled(−pi/2,−5)pointandabove/right of the labelled(pi/2,1)point; no endpoint restriction is drawn.',
 'reason':'The formula values on the requested branch are correct,but this function was defined onlyon the closed interval−pi/2..pi/2. A complete sketch must stop at the two included endpoints; it must not present continuation as part of this restricted function.'}
row['subparts'][0]['source_defect_id']='TB-YM-C4-Try13-Q2-DOMAIN-ENDPOINTS'
add('Example',14,176,'Forasinx+bwitha>0,maximum6andminimum−2,recovera,b,then amplitudeandy-intercept.',
 [value('a-coefficients','Tuple((6-(-2))/S(2),(6+(-2))/S(2))','Tuple(4,2)',176),value('b-amplitude','(6-(-2))/S(2)','4',176),value('b-y-intercept','(6+(-2))/S(2)','2',176)],[FEATURE,INTERPRET])
add('Try-Now-14',1,176,'Foracosx+bwitha>0,maximum8andminimum−2,finda,b,amplitudeandy-intercept. Cosine makes the intercept8,notb=3.',
 [value('a-coefficients','Tuple((8-(-2))/S(2),(8+(-2))/S(2))','Tuple(5,3)',605),value('b-amplitude','(8-(-2))/S(2)','5',605),value('b-y-intercept','(8-(-2))/S(2)+(8+(-2))/S(2)','8',605)],[FEATURE,INTERPRET])
add('Try-Now-14',2,176,'For a−bcosxwitha,b>0on0..360degrees,maximum10andminimum−2,findconstants,amplitude,interceptandsketch the reflected cosine.',
 [value('a-coefficients','Tuple((10+(-2))/S(2),(10-(-2))/S(2))','Tuple(4,6)',605),value('b-amplitude','(10-(-2))/S(2)','6',605),value('b-y-intercept','(10+(-2))/S(2)-(10-(-2))/S(2)','-2',605),
  graph('c','cos','-6','1','4','0','360','degree',605,{'y_intercept':'-2','window_global_max_locations':'FiniteSet(180)','window_global_min_locations':'FiniteSet(0,360)','window_range':'Interval(-2,10)'})],[FEATURE,INTERPRET,SKETCH])

figures=[]
specs=[
 (165,'Basic investigation sine response table','Blank sine row asks minimum,maximum,amplitude,period,range; graphing window is−500..500degrees.','Investigation-basic-trig-graphs:1',[BASIC,FEATURE,INTERPRET,RANGE],'table'),
 (166,'Basic investigation cosine/tangent response table','Two blank rows ask the samefivefeatures; tangent has no finite extrema oramplitude.','Investigation-basic-trig-graphs:2',[BASIC,FEATURE,INTERPRET,RANGE],'table'),
 (166,'Sine property graph','Degree sine graph labels amplitude1,period360degrees,zeros atmultiples180,andrepeat extrema±1; surrounding list supplies the feature values.','Investigation-basic-trig-graphs:1',[BASIC,FEATURE],'graph'),
 (167,'Cosine property graph','Degree cosine graph hasmaxima at0and±360,minima at±180,amplitude1andperiod360.','Investigation-basic-trig-graphs:2',[BASIC,FEATURE],'graph'),
 (167,'Sine/cosine phase comparison','Two curves show the90degree phase relationship; this is teaching support,not a newly posed phase-shift calculation.',None,[BASIC],'graph'),
 (167,'Tangent property graph','Increasing tangent branches are separated atodd90degree poles; period180,rangeR,no amplitude.','Investigation-basic-trig-graphs:2',[BASIC,FEATURE],'graph'),
 (168,'Example10paired tangent value table','Values for tanxand−tanxon−pi..piinpi/4steps;±pi/2are undefinedrather thanzero.','Example:10',[BASIC,SKETCH],'table'),
 (168,'Example10paired tangent sketches','Opposite-sign tangent curves reflect in the x-axis andshare poles±pi/2.','Example:10',[BASIC,INTERPRET,SKETCH],'graph'),
 (170,'Output-scale sine investigation table','Base sine row is filled,with90/270degree extrema andamplitude1;2sinxand3sinxrows are blank.','Investigation-transformed-trig-graphs:1',[FEATURE,INTERPRET,SKETCH],'table'),
 (170,'Output-scale cosine/tangent investigation table','Base cosine/tangent rows andsketches are supplied;factor2and3rows must be completed. Tangent amplitude is markedN.A.','Investigation-transformed-trig-graphs:2',[FEATURE,INTERPRET,SKETCH],'table'),
 (171,'Input-scale investigation table','Fifteen rows use sin,cos,tanwithmultipliers1,2,3,1/2,1/3; all graph/feature response cells are blank.','Investigation-transformed-trig-graphs:4',[FEATURE,INTERPRET,SKETCH],'table'),
 (172,'Vertical-shift investigation table','Ten rows use sin/coswithshifts0,1,2,−1,−2; extrema,sketch,amplitudeandperiod are requested.','Investigation-transformed-trig-graphs:6',[FEATURE,INTERPRET,SKETCH],'table'),
 (172,'Trig feature summary table','Summary coversasinbx+c,asin(x/b)+c,acosbx+c,acos(x/b)+c,atanbx,andatan(x/b)+c. High-resolution read confirms the first tangent row hasno+c,so its zero intercept is correct. Extrema formulas usepositivea; negativea is handled explicitly inExample11b.',None,[FEATURE,INTERPRET],'table'),
 (173,'Coefficient-effects annotation','Arrows identify a withamplitude,b withperiod,andc withvertical translation inasin(bx)+c; tangent amplitude remains separately undefined.',None,[FEATURE,INTERPRET],'diagram'),
 (174,'Example12worked graph mismatch','Printed curve is3cos2x−1withtwo cycles andrange[−4,2],whilepart(c)asks3cosx+2withonecycle andrange[−1,5]. Retain as a documented source defect,not an accepted model for the asked function.','Example:12',[SKETCH],'graph'),
 (175,'Example13tangent value table','5tan4xatdegree0,10,15,20,22.5,25,30,35,45;22.5is a pole.','Example:13',[FEATURE,SKETCH],'table'),
 (175,'Example13tangent sketch','One45degree tangent cycle withpole22.5,zeros0/45andseparate increasing branches.','Example:13',[FEATURE,SKETCH],'graph')]
for n,(page,label,note,parent,teaches,rep)in enumerate(specs,35):
    entry={'item_id':f'8227:TB:YM:C4:Teaching-figure:{n}','item_kind':'teaching-figure','exercise':'Teaching figure','item_number':str(n),
      'pdf_page':page,'printed_page':page-12,'source_label':label,'parent_item_id':f'8227:TB:YM:C4:{parent}'if parent else None,
      'notes':note,'what_it_shows':note,'assessed_8227_demand_ids':[],'component_demand_ids':[],'teaches_8227_demand_ids':teaches,
      'representation':rep,'source_evidence':ev(page),'learner_display':False,
      'value_level_scope_decisions':[{'rule_id':'8227:QUAL03','status':'not applicable','quoted_value':note,'reason':'Graph/table teaching evidence,not a bounded trigonometric equation.'}],
      'value_level_scope_review_status_r5':'author actual-angle/unit/domain reading complete; independent check pending',
      'exam_representation_check':{'status':'cross-book/examination representation synthesis pending','examination_part_ids':[],
        'relation':'Do not claim same-type coverage from a topic/shape alone; textbook investigation tables andteaching panels are separate from examination frequency.'},
      'mathematical_feature_review':{'status':'source mismatch recorded'if page==174 else'author figure features checked; independent acceptance pending',
       'method':'Compare labels,angle units,zeros,extrema,poles,periods,global versus visible ranges,and any parent fixed-source derivation. Blank response tables are explicitlyauthor-derived; supplied rows are compared with printed values.'}}
    figures.append(entry)

for kind,n,page,more in [('Investigation-basic-trig-graphs',1,165,[166]),('Investigation-basic-trig-graphs',2,166,[167]),('Investigation-transformed-trig-graphs',1,169,[170])]:
    corrections.append({'item_id':f'8227:TB:YM:C4:{kind}:{n}','continuation_pdf_pages':more})
pages=[]
for page in range(165,177):
    own=[r['item_id']for r in answers if r['source_pdf_page']==page]+[f['item_id']for f in figures if f['pdf_page']==page]
    continued=[r['item_id']for r in corrections if page in r['continuation_pdf_pages']]
    pages.append({'pdf_page':page,'printed_page':page-12,'chapter':4,'page_status':'items enumerated',
      'item_ids':own,'continuation_item_ids':continued,'source_evidence':ev(page),
      'non_item_content':'Software setup,screenshot,QR/video leads andgraph-sketching advice are recorded as procedural/prose context,not extra assessed mathematical tasks. All numbered tasks,response tables,provided graph panels andannotations are enumerated.',
      'reader':'Codex author','date':'2026-11-17'})
if __name__=='__main__':
    for name,data in[
      ('answers-YM-C4-trig-graphs.json',{'scope':'All10basic/transformed investigation question records plus all Examples/TryNowonPDF168–176. Every requested function row,graph,feature andexplanation output is explicit; proprietary software menu actions are not claimed tested.','items':answers}),
      ('census-YM-C4-trig-graphs.json',{'book':'YM','book_id':'8227-SRC-017','chapter':4,'source_path':SRC,'source_sha256':SHA,
       'scope':'PDF165–176inclusive. Source mathematical figures/tables are separate records; response-key plots are checked per answer rather than counted as new practice items.','new_items':figures,'corrections':corrections,'pages':pages})]:
        (W/'tools/textbook-r5'/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
    print(len(answers),'items;',sum(len(r['subparts'])for r in answers),'output records;',len(figures),'figures')
