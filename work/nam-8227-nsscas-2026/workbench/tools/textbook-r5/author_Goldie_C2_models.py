"""Audit the fixed data/graphs in Examples6–8 and all Exercise2C items.

Fits are author checks of the printed data,not renewable-question generators.
Book answers fitted by eye are recorded separately from least-squares fits.
"""
import hashlib,json,math
from author_Goldie_C5_opening import W,SRC,SHA,value,reasoning,fig,figures,compute,expression,equivalent
LIN='8227:2020:M2:T2:O04:D01';PARAM='8227:2020:M2:T2:O04:D02';EQ='8227:2020:M2:T2:O03:D01';LAW='8227:2020:M2:T2:O01:D02'
def ev(page):
 name='Goldie-C2-50' if page<54 else 'Goldie-C2-54' if page<58 else 'Goldie-C2-58' if page<335 else 'Goldie-key-C2-335'
 p=W/f'checks/r5/textbooks/{name}.png'
 return {'path':str(p.relative_to(W.parents[2])),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
answers=[];datasets=[]
def add(kind,n,page,note,parts,direct,components=None,rep='table',continuation=None):
 for p in parts:
  kp=p.pop('key_page_override',page if kind=='Example' else 337 if n<=2 else 338)
  pp=p.pop('source_page_override',page)
  p.update(source_pdf_page=pp,source_evidence=ev(pp),answer_pdf_page=kp,answer_printed_page=kp-14 if kp else None,key_evidence=ev(kp or 338),review_date='2026-11-18')
  if kp is None:p.update(key_presence='no separate key',inspected_key_pdf_pages=[337,338])
 row={'item_id':f'8227:TB:Goldie:C2:{kind}:{n}','source_pdf_page':page,'notes':note,'assessed_8227_demand_ids':direct,'component_demand_ids':components or[],
  'mapping_rationale':'The requested linearisation,plot,parameter recovery,model prediction and limitation explanation are distinct outputs. Fitted-by-eye constants are not unique exact answers. A raw straight-line warm-up does not automatically assess log linearisation.',
  'representation':rep,'sketch_response_required':any(p.get('author_comparison_status')=='sketch' for p in parts),'exam_style':kind=='Exercise-2C' and n==9,
  'exam_style_basis':'Cambridge9709Paper2Q2June2007attribution.' if kind=='Exercise-2C' and n==9 else 'Unattributed worked example or ordinary exercise.',
  'value_level_scope_decisions':[{'rule_id':'8227:LIMIT06','status':'not applicable','quoted_value':note,'reason':'Taking common logs and applying product/power laws linearises the stated model;no memorised change-of-base formula is asked.'}],
  'precision_angle_check':{'source':'Exercise2Ckey explicitly allows variation from fitting lines by eye. Source tables use rounded measurements;Example7log table is2decimal places,Example8log table3decimal places. Q9(ii)asks2decimal places.',
   'comparison':'Retain data units and axis orientation. A regression provides an independent reproducible comparison,not a requirement that a learner reproduce exact least-squares coefficients from a hand graph. Extrapolations remain conditional on the selected model.'},
  'expected_subpart_labels':[p['subpart'] for p in parts],'subparts':parts}
 if continuation:row['continuation_pdf_pages']=continuation
 if kind=='Example' and n==6:row['evidence_role']='prerequisite/supporting raw straight-line plotting and fitting warm-up;no direct logarithmic-demand coverage.'
 answers.append(row);return row
def manual(label,answer,working,kp,status='matches'):
 return reasoning(label,answer,working,kp,status)
def checks(p,spec):
 p['additional_operations']={name:{'kind':'identity','operands':[expr]} for name,expr,target in spec}
 p['additional_operation_expected']={name:target for name,expr,target in spec};return p
def fit_data(name,xs,ys,mode):
 """Derive intercept/slope twice: standard-math covariance and CAS sums."""
 assert len(xs)==len(ys)>2 and mode in ['linear','exponential','power']
 X=[float(expression(v)) for v in xs];Y=[float(expression(v)) for v in ys]
 if mode=='power':assert min(X)>0;X=list(map(math.log10,X))
 if mode!='linear':assert min(Y)>0;Y=list(map(math.log10,Y))
 xb=math.fsum(X)/len(X);yb=math.fsum(Y)/len(Y)
 slope=math.fsum((a-xb)*(b-yb) for a,b in zip(X,Y))/math.fsum((a-xb)**2 for a in X);intercept=yb-slope*xb
 tx=[f'N(log({a})/log(10),45)' if mode=='power' else str(a) for a in xs]
 ty=[f'N(log({a})/log(10),45)' if mode!='linear' else str(a) for a in ys]
 n=len(xs);sx='('+ '+'.join(tx)+')';sy='('+ '+'.join(ty)+')'
 sxy='('+ '+'.join(f'({a})*({b})' for a,b in zip(tx,ty))+')';sxx='('+ '+'.join(f'({a})**2' for a in tx)+')'
 m=f'(({n}*{sxy}-{sx}*{sy})/({n}*{sxx}-{sx}**2))';c=f'(({sy}-({m})*{sx})/{n})'
 op={'kind':'identity','operands':[f'Tuple({c},{m})']}
 got=compute(op)
 assert math.isclose(float(got[0]),intercept,rel_tol=1e-11,abs_tol=1e-11)
 assert math.isclose(float(got[1]),slope,rel_tol=1e-11,abs_tol=1e-11)
 physical={'intercept':intercept,'slope':slope,'k':10**intercept if mode!='linear' else intercept,'b_or_n':10**slope if mode=='exponential' else slope}
 def predict(t):return intercept+slope*t if mode=='linear' else physical['k']*physical['b_or_n']**t if mode=='exponential' else physical['k']*t**slope
 physical['original_response_sse']=math.fsum((predict(float(expression(a)))-float(expression(b)))**2 for a,b in zip(xs,ys))
 record={'dataset_id':name,'x':xs,'y':ys,'fit_mode':mode,'author_fit':physical,'independent_CAS_operation':op,'CAS_intercept_slope':str(got),
  'method':'Standard-math centred covariance,independently compared with45digit CASnormal-equation sums. Transformed-response least squares is not claimed to minimise original-response SSE;SSE only compares these explicitly defined candidate fits.'}
 datasets.append(record);return record
def with_fit(p,data):
 p['source_data_fit']=data;p.setdefault('additional_operations',{})['independent_fit']=data['independent_CAS_operation'];return p
temperature=fit_data('Example6-temperature',['20','40','60','80','100','120'],['16.3','20.4','24.2','28.5','32.0','36.3'],'linear')
pipe=fit_data('Example7-pipe',['1','2','3','5','10'],['0.02','0.32','1.62','12.53','199.80'],'power')
coffee=fit_data('Example8-coffee',['2','4','6','8','10','12'],['81','70','61','52','45','38'],'exponential')
moons=fit_data('2C1-moons',['1.9','2.7','4.5','15.9','79.3'],['290000','380000','530000','1220000','3560000'],'power')
mould=fit_data('2C2-mould',['0','1','2','3','4','5'],['0.9','1.3','1.8','2.5','3.5','5.2'],'exponential')
power=fit_data('2C6-power',['4','7','10','13','20'],['3','3.97','4.74','5.41','6.71'],'power')
virus=fit_data('2C7-virus',['1','2','3','4','5'],['240','150','95','58','38'],'exponential')
shopfits=[fit_data('2C8-shopping-'+mode,['2','3','4','5','6'],['4600','5000','5300','5500','5700'],mode) for mode in ['linear','exponential','power']]
shopping=shopfits[-1]

p=manual('i','Plot all six temperature points with time in seconds on the horizontal axis and temperature°Cvertically;they lie close to a straight increasing line.',
 'The increments are approximately4°Cper20seconds. Plot the actual rounded observations,not an exponential curve inferred from the chapter title. The independent raw-data line has slope about0.19886and intercept12.3567;the source hand line0.2t+12.3is a close graphical model.',51,'sketch');with_fit(p,temperature)
p2=manual('ii','A reasonable source model is θ≈0.2t+12.3°C.',
 'From source endpoint readings(20,16.3),(120,36.3),gradient=(36.3−16.3)/100=0.2and intercept16.3−0.2·20=12.3. These are fitted approximate data,not six exact collinear givens. No log transformation is requested.',51)
checks(p2,[('endpoint_line','Tuple((36.3-16.3)/(120-20),16.3-((36.3-16.3)/(120-20))*20)','Tuple(0.2,12.3)')])
add('Example',6,51,'Plot six experimental temperature/time observations and find a raw straight-line relation;the near-linear warm-up does not itself assess logarithmic linearisation.',[p,p2],[])
p=manual('i','For R=kd^n,taking common logs gives logR=nlogd+logk. Either axis orientation gives a straightness test,but swaps slope/intercept interpretation.',
 'The question asks logd against logR;then logd=(1/n)logR−logk/n for n≠0. The worked solution instead plots logR vertically against logd,where gradient=nand intercept=logk. Both straightness tests are valid;their gradient interpretations cannot be interchanged.',52)
p2=manual('ii-table-plot','The source solution uses logd=(0,0.30,0.48,0.70,1.00)and logR=(−1.70,−0.49,0.21,1.10,2.30),then plots logR against logd.',
 'Transform each positive measurement before rounding to2decimal places;retain both axis labels. The five points are almost exactly linear in these coordinates. A learner following the requested reversed axes should obtain reciprocal slope and still recover the same original model.',53,'sketch');with_fit(p2,pipe)
p3=manual('iii-parameters','The source model is R≈0.020d^4,so n≈4andk≈0.020.',
 'From the worked orientation,gradient4and logk≈−1.70give k=10^(−1.70)≈0.020. Independently fitting the original data gives exponent very close4and coefficient near0.020. In the requested reverse orientation,the slope is≈1/4and intercept≈0.425.',53)
add('Example',7,52,'Test the pipe-flow power model R=kd^n,make transformed table/plot,and recover constants. The question orders logd against logR;the worked plot reverses these axes while returning the same original relation.',[p,p2,p3],[LIN,PARAM],rep='table',continuation=[53])
p=manual('i','Plot the six decreasing temperature observations against time;join with a smooth decay curve,not a straight raw-data line.',
 'All data are positive and decrease with progressively smaller absolute drops. The raw source plot agrees. A chosen exponential model extrapolated beyond these data is not a verified full cooling law.',54,'sketch')
p2=manual('ii','Test θ=ka^tby plotting logθagainstt;straightness supports the proposed exponential relationship.',
 'For k>0,a>0,logθ=logk+tloga. The log-ordinate line has interceptlogkand gradientloga. It does not require plotting logt.',54,'show/prove')
p3=manual('iii-table-plot','The3dpcommon-log temperatures are1.908,1.845,1.785,1.716,1.653,1.580at t=2,4,6,8,10,12.',
 'Transform all six measured temperatures and plot these ordinate values against original time. They lie near a decreasing straight line. The actual data,not the rounded key log values,feed the independent fit.',54,'sketch');with_fit(p3,coffee)
p4=manual('iii-parameters','The source graphical estimates are k≈94.2and a≈0.927,thus θ≈94.2·0.927^t.',
 'Its displayed fitted intercept1.974gives10^1.974≈94.2and gradient−0.033gives10^(−0.033)≈0.927. The independent data fit is nearby. These are graphical approximations,not exact coefficients fixed uniquely by the noisy data.',55)
add('Example',8,53,'Plot cooling measurements,derive a suitable logarithmic test,make the transformed table/graph,and estimate exponential decay constants. Worked solution continues54–55.',[p,p2,p3,p4],[LIN,PARAM],continuation=[54,55])

p=manual('i','Plot logRagainstlogT;R=kT^nbecomes logR=nlogT+logk.',
 'Use R in kilometres,including the table’s×10^5factor. A consistent scaled-radius plot is also valid,but its coefficient kdiffers by10^5. Keep units when recovering the intercept.',337,'show/prove')
p2=manual('ii-table-graph','Plot the five transformed positive-radius/period observations;the source’s2dplogRvalues are5.46,5.58,5.72,6.09,6.55andlogT0.28,0.43,0.65,1.20,1.90.',
 'Common logs preserve the stated physical units in the numerical arguments. The data form a close straight line. All five actual pairs are retained;an independent log-space fit has n≈0.66743,k≈192739km,showing that source graphical coefficients are not unique exact answers.',337,'sketch');with_fit(p2,moons)
p3=manual('iii','The printed hand-graph model uses n≈0.690,k≈1.8×10^5km. A reproducible least-squares alternative is n≈0.66743,k≈1.92739×10^5km.',
 'Recover exponent from transformed gradient and coefficient from exponentiating the intercept. The key explicitly allows some variation for eye fitting. Its model and the independent fit differ,so neither pair is a unique exact marking target. Preserve the original measurements and each chosen model for follow-on predictions.',337)
p4=manual('iv','Using the printed graphical model,R=1.4×10^5km gives T≈0.70days;the independent fitted model gives about0.62days.',
 'For either chosen positive model,solve T=(R/k)^(1/n). Carry the same model’s coefficients into this part;do not mark a different defensible graphical fit wrong solely for disagreeing with0.7. The measurement/model fit controls uncertainty;this is not an exactly determined orbital period.',337)
checks(p4,[('source_model','(140000/180000)**(1/(69/100))','(7/9)**(100/69)')]);p4['source_page_override']=56
add('Exercise-2C',1,55,'Use the five moon radii(×10^5km)and periods(days)to test R=kT^n,make the transformed plot,estimate k,nand predict a sixth moon’s period. Part(iv)continues56;source graphical parameters are nonunique.',[p,p2,p3,p4],[LIN,PARAM,EQ],continuation=[56])
p=manual('i','logA=tlogb+logk.','Take common logs of A=kb^twith positive A,k,b;apply product and power laws. The model is linear in tversuslogA.',337,'show/prove')
p2=manual('ii','Plot logAvertically against original time t.','The proposed form has constant gradientlogband interceptlogk;logt would test a different power model and would also be undefined at the suppliedt=0.',337)
p3=manual('iii','The source hand-graph estimates are b≈1.4,k≈0.89. The independent data fit gives b≈1.41178,k≈0.90329.',
 'Transform and plot all six positive areas,including0.9at t=0with a negative logarithm. Recover both parameters from the fitted line. The source graph and table agreement are approximate;do not require an exact fit through every measured point.',337,'sketch');with_fit(p3,mould)
p4=manual('iv-a','A reasonable graphical time to2cm²is about2.3–2.4days;the source key gives2.4days.',
 'For a chosen model,solve t=log(2/k)/logb. The source rounded parameters give approximately2.41days;the independent data-fit parameters give approximately2.31days. Preserve the selected model and graphical uncertainty rather than forcing a unique two-decimal value.',337)
p5=manual('iv-b','The area at3.5days is approximately3cm²;the key gives3.0cm².',
 'Evaluate the same fitted exponential at t=3.5. The independent fit gives about3.02cm²;the source rounded parameters give about2.89cm². Such differences are model/graph rounding,not an exact measurement contradiction.',337)
p6=manual('v','Exponential growth.','The fitted factor b>1multiplies the area over each equal time increment. It is not a constant additive growth model.',337)
add('Exercise-2C',2,56,'Test the mould-area model A=kb^tfrom six rounded measurements,choose and draw log axes,estimate constants,predict time/area and identify the growth type.',[p,p2,p3,p4,p5,p6],[LIN,PARAM,EQ])
p=manual('i','logN=tloga+logk.','Take logs of N=ka^twith positive coefficient/base. The given straight graph is logNagainst original years since1930.',338,'show/prove')
p2=manual('ii','The source estimates k≈3.2×10^6trees,a≈0.98; krepresents the modelled number of trees in1930.',
 'The line’s intercept is about6.5,so k≈10^6.5≈3.16million. A gradient near−0.008gives a≈10^(−0.008)≈0.982. The source rounded graphical estimates are consistent. At t=0,the original model is N=k;do not interpret the logarithmic intercept6.5as the tree count.',338)
add('Exercise-2C',3,56,'Derive the exponential deforestation log relation;read the supplied logNagainst years-since1930graph,estimate k,aand explain k.',[p,p2],[LIN,PARAM],rep='graph')
p=manual('i','logs=nlogt+logkfor t>0.','The suggested s=kt^nwith positive measured distance admits common logs. The log plot excludes t=0even though the original journey starts there.',338,'show/prove')
p2=manual('ii','The source graphical estimates are k≈1100,n≈1.6.','Read the given log-plot slope and intercept;the intercept islogk,so exponentiate it. The time unit in the original relationship remains minutes.',338)
p3=manual('iii','The estimated distance in100seconds is about2500m.','Convert100seconds to5/3minutes before evaluating1100(5/3)^1.6≈2490.9m. The graphical parameters justify an approximate answer,not an exact2491m requirement.',338)
checks(p3,[('unit_conversion','100/60','5/3')])
p4=manual('iv','The early-journey power fit need not remain valid after10minutes.','For n≈1.6the model predicts continually increasing speed;the actual train may reach cruising speed or slow down. A fit over the observed short interval does not establish its longer-time physical validity.',338)
add('Exercise-2C',4,57,'Assume s=kt^nfor train distance in metres and time in minutes;derive the log line,read k,n,predict the first100seconds and discuss extrapolating to10minutes.',[p,p2,p3,p4],[LIN,PARAM],rep='graph')
p=manual('i','logA=tlogb+logk.','Apply logarithm laws to the positive exponential model;the gradient islogband interceptlogk.',338,'show/prove')
p2=manual('ii','b=10^0.1375≈1.37,k=10^0.2≈1.58.',
 'The supplied transformed points(0,0.2),(4,0.75)fix the line exactly:gradient0.55/4=0.1375. Unlike a line fitted to noisy data,this given line has exact slope/intercept before rounding.',338)
checks(p2,[('slope','(0.75-0.2)/4','0.1375')])
add('Exercise-2C',5,57,'For A=kb^t,derive the log line and recover constants from the given transformed points(0,0.2),(4,0.75),rather than noisy measurements.',[p,p2],[LIN,PARAM],rep='graph')
p=manual('model-test','Plot logyagainstlogx;straightness tests y=Ax^B. Nonlinear transformed points would reject that proposed form over the observed data.',
 'Take logs with x,y,Apositive. Gradient is B,and intercept islogA. A visually near-straight finite dataset supports this candidate fit;it does not prove a global physical law.',338)
p2=manual('plot-parameters','The table is closely modelled by y≈1.5x^0.5,with A≈1.5,B≈0.5.',
 'Plot all five positive observations in log coordinates;the independently fitted intercept/slope are close to log1.5and0.5. The source labelled graph and formula agree. The variable Bdoes not denote a logarithm base.',338,'sketch');with_fit(p2,power)
add('Exercise-2C',6,58,'Explain a power-model test and how to recover A,B,then carry it out for x=4,7,10,13,20and y=3,3.97,4.74,5.41,6.71.',[p,p2],[LIN,PARAM])
p=manual('i','Plot the five observed weekly cases against week1–5and join with a smooth decreasing positive curve.',
 'The counts240,150,95,58,38fall by an approximately constant ratio. The source answer section supplies no separate raw-plot key;these features are author-derived from its actual table.',None,'sketch')
p2=manual('ii','An exponential decay model is suitable;plot logyagainstt. The source graphical fit is y≈400·0.63^t;an independent fit is y≈379.75·0.6290^t.',
 'The transformed observed points are close to a line. Recover coefficient and base together,then retain them consistently. The source’s coarse hand-fit coefficient differs from the least-squares intercept;it is not a unique exact requirement.',338);with_fit(p2,virus)
p3=manual('iii','The fitted weekly count at t=15is about0.4;this is a modelled rate/expectation,not a literal fractional recorded case.',
 'Using the source fit gives400·0.63^15≈0.391. The independent fit gives a nearby smaller value. Both indicate a large predicted decline under the assumed continuation. The source says undercontrol;that is a model interpretation,not verified medical evidence or proof the infection is eliminated.',338)
add('Exercise-2C',7,58,'Plot weekly virus cases after vaccination,choose a suitable mathematical decay model and transformed plot,then interpret its prediction at week15without claiming clinical effectiveness.',[p,p2,p3],[LIN,PARAM])
p=manual('i','Among the specified simple linear,exponential and power candidates,the data best support a power fit close to P=4000t^0.2.',
 'The independent fits give original-response SSEabout19000(linear),26951(exponential),985(power). These compare the explicitly defined fitted candidates on the same response scale,not incomparable transformedR²values. The source model4000t^0.2also closely matches the observations;other model classes have not been exhausted.',338)
p['candidate_model_fits']=shopfits;with_fit(p,shopping)
p2=manual('ii','The source model predicts4000users at the end of week1.','Evaluate4000·1^0.2=4000. An independently fitted power curve gives about4030;the difference is fitting uncertainty. This is extrapolation one week before the first observation at t=2.',338)
p3=manual('iii','The fitted power grows without bound,so it cannot remain a literal local-population model indefinitely.',
 'Although the growth rate decreases for exponent0.2,it stays positive and the model has no finite upper bound. The finite local population limits sustained extrapolation. The source also notes slowing growth;slowing alone does not impose a finite cap.',338)
add('Exercise-2C',8,58,'Investigate models for users P=4600,5000,5300,5500,5700at weeks2–6,estimate first-week use and discuss long-term validity. The enlarged key correctly prints4000,not400.',[p,p2,p3],[LIN,PARAM])
p=manual('i-line','y=((log4)/(log3))x+2(log4)/(log3),a straight line of exact gradientlog4/log3.',
 'Take common logs of3^y=4^(x+2):ylog3=(x+2)log4. Solve the linear equation in y. The resulting quotient arises from the equation,not a request to memorise a general change-of-base law.',338,'show/prove')
p2=value('ii-intersection','(2*log(4)/log(3))/(2-log(4)/log(3))','3.42',338,'Set the independently derived line equal toy=2x,solve the resulting linear equation and round thexcoordinate to2decimal places.')
p2['operation']={'kind':'rounded','operands':['(2*log(4)/log(3))/(2-log(4)/log(3))'],'decimal_places':2}
add('Exercise-2C',9,58,'Linearise3^y=4^(x+2),give the exact gradient,and find its intersection with y=2xto2decimal places. Cambridge9709Paper2Q2June2007attribution.',[p,p2],[LIN])

# Check the exact transformation identities and every printed transformed
# table cell as well as the independent fits. Positive domains are stated
# in the item reasoning; force expansion does not remove those conditions.
for kind,n,label,formula in [
 ('Example',7,'i','expand_log(log(k*x**n),force=True)-log(k)-n*log(x)'),
 ('Example',8,'ii','expand_log(log(k*a**t),force=True)-log(k)-t*log(a)'),
 ('Exercise-2C',1,'i','expand_log(log(k*t**n),force=True)-log(k)-n*log(t)'),
 ('Exercise-2C',2,'i','expand_log(log(k*b**t),force=True)-log(k)-t*log(b)'),
 ('Exercise-2C',3,'i','expand_log(log(k*a**t),force=True)-log(k)-t*log(a)'),
 ('Exercise-2C',4,'i','expand_log(log(k*t**n),force=True)-log(k)-n*log(t)'),
 ('Exercise-2C',5,'i','expand_log(log(k*b**t),force=True)-log(k)-t*log(b)'),
 ('Exercise-2C',6,'model-test','expand_log(log(a*x**b),force=True)-log(a)-b*log(x)')]:
 row=next(r for r in answers if r['item_id']==f'8227:TB:Goldie:C2:{kind}:{n}')
 part=next(p for p in row['subparts'] if p['subpart']==label)
 part.setdefault('additional_operations',{})['linearisation_identity']={'kind':'identity','operands':[formula]}
 part.setdefault('additional_operation_expected',{})['linearisation_identity']='0'
for kind,n,label,columns in [
 ('Example',7,'ii-table-plot',[(pipe['x'],['0','0.30','0.48','0.70','1.00'],2),(pipe['y'],['-1.70','-0.49','0.21','1.10','2.30'],2)]),
 ('Example',8,'iii-table-plot',[(coffee['y'],['1.908','1.845','1.785','1.716','1.653','1.580'],3)]),
 ('Exercise-2C',1,'ii-table-graph',[(moons['x'],['0.28','0.43','0.65','1.20','1.90'],2),(moons['y'],['5.46','5.58','5.72','6.09','6.55'],2)])]:
 row=next(r for r in answers if r['item_id']==f'8227:TB:Goldie:C2:{kind}:{n}');part=next(p for p in row['subparts'] if p['subpart']==label)
 for j,(inputs,targets,places) in enumerate(columns):
  for i,(operand,target) in enumerate(zip(inputs,targets)):
   key=f'table_{j}_cell_{i}'
   part.setdefault('additional_operations',{})[key]={'kind':'rounded','operands':[f'log({operand})/log(10)'],'decimal_places':places}
   part.setdefault('additional_operation_expected',{})[key]=target

figures.clear()
figure_rows=[
 (43,51,'Example6 temperature table','Six rounded time/temperature pairs:20..120seconds in steps20and16.3,20.4,24.2,28.5,32.0,36.3°C. The data are approximately,not exactly,collinear.',[],'table','Example:6'),
 (44,51,'Figure2.7 temperature line','The plotted raw data and fittedθ≈0.2t+12.3use original time/temperature axes;the small break in the vertical axis must not be mistaken for a zero ordinate.',[],'graph','Example:6'),
 (45,52,'Example7 pipe-flow table','Diameter d=1,2,3,5,10cm;rate R=.02,.32,1.62,12.53,199.80litres/s. All positive entries allow common logs;units affect the coefficient k.',[LIN,PARAM],'table','Example:7'),
 (46,52,'Example7 linear-form correspondence','logR=nlogd+logkidentifies ordinate,horizontal variable,gradient andintercept for the worked orientation. The ordered axes differ from those requested by the preceding question.',[LIN],'table','Example:7'),
 (47,53,'Example7 transformed table','The displayed2dplogd/logRvalues preserve the original five observations. Rounding before fitting can slightly alter coefficients;retain raw values for independent QA.',[LIN],'table','Example:7'),
 (48,53,'Figure2.8 pipe transformed graph','The worked axes are logRvertical/logdhorizontal;intercept≈−1.70and slope≈4. Reversing axes requires reciprocal slope and a correspondingly changed intercept.',[PARAM],'graph','Example:7'),
 (49,53,'Example8 coffee table','Time t=2,4,6,8,10,12minutes;θ=81,70,61,52,45,38°C. This is finite experimental data,not proof an unshifted exponential remains physically valid forever.',[LIN,PARAM],'table','Example:8'),
 (50,54,'Figure2.9 raw coffee decay','The six raw observations form a smooth decreasing curved trend,with time and temperature on original axes. They are not the straight transformed-log plot.',[LIN],'graph','Example:8'),
 (51,54,'Example8 exponential linear-form correspondence','logθ=tloga+logkuses original time as horizontal variable. The fitted gradient isloga,not a;the intercept islogk,not k.',[LIN],'table','Example:8'),
 (52,54,'Example8 transformed table','The six3dplog temperatures are1.908,1.845,1.785,1.716,1.653,1.580at the original times2..12. No logtime is taken.',[LIN],'table','Example:8'),
 (53,55,'Figure2.10 coffee log plot','The approximate line has ordinate intercept1.974and negative gradientabout−.033. Positive decay base≈.927is obtained by exponentiation,not by reading the negative gradient as the base.',[PARAM],'graph','Example:8'),
 (54,55,'Example8 decay-base note','The positive base.927isbelow1,so its power decreases with increasing time. A negative loggradient does not imply a negative exponential base.',[PARAM],'table','Example:8'),
 (55,55,'Exercise2C1 moon table','Five labelled moon periods and radii are supplied;radius column uses×10^5km. A scaled/unscaled logordinate changes the coefficient but not the exponent.',[LIN,PARAM],'table','Exercise-2C:1'),
 (56,56,'Exercise2C2 mould table','Times0..5days and areas.9,1.3,1.8,2.5,3.5,5.2cm²allow logarea,including negative log(.9). logtime cannot include0.',[LIN,PARAM],'table','Exercise-2C:2'),
 (57,56,'Exercise2C3 deforestation graph','The supplied logNagainst years-since1930graph has ordinate interceptabout6.5and a small negative slope. The original initial tree count is10^intercept.',[PARAM],'graph','Exercise-2C:3'),
 (58,57,'Exercise2C4 train log graph','The supplied logsagainstlogtline is used for k≈1100,n≈1.6. Original time is minutes;logt=0means1minute,not departure time0.',[PARAM],'graph','Exercise-2C:4'),
 (59,57,'Exercise2C5 given transformed points','The line logAagainsttpasses exactly(0,.2),(4,.75). Gradient.1375=logband intercept.2=logk. These given points differ from a best-fit scatter dataset.',[PARAM],'graph','Exercise-2C:5'),
 (65,58,'Exercise2C6 power observations','x=4,7,10,13,20and y=3,3.97,4.74,5.41,6.71are positive rounded observations close to1.5√x.',[LIN,PARAM],'table','Exercise-2C:6'),
 (66,58,'Exercise2C7 weekly cases table','Weeks1..5and240,150,95,58,38cases support comparing mathematical decay fits. This table alone is not evidence of vaccine causality or clinical elimination.',[LIN,PARAM],'table','Exercise-2C:7'),
 (67,58,'Exercise2C8 user-count table','Weeks2..6and4600,5000,5300,5500,5700users. Original-response comparisons use the same five data points;the first-week answer extrapolates beyond them.',[LIN,PARAM],'table','Exercise-2C:8')]
for n,page,label,note,teaches,rep,parent in figure_rows:fig(n,page,label,note,teaches,rep,[],parent)
for f in figures:
 f['item_id']=f['item_id'].replace(':C5:',':C2:');f['parent_item_id']=f['parent_item_id'].replace(':C5:',':C2:');f['source_evidence']=ev(f['pdf_page'])
pages=[]
for page in range(51,59):
 continuation={53:['Example:7'],54:['Example:8'],55:['Example:8'],56:['Exercise-2C:1']}.get(page,[])
 pages.append({'pdf_page':page,'printed_page':page-14,'chapter':2,'page_status':'items enumerated','item_ids':[r['item_id']for r in answers if r['source_pdf_page']==page]+[r['item_id']for r in figures if r['pdf_page']==page],
  'continuation_item_ids':['8227:TB:Goldie:C2:'+iid for iid in continuation],'source_evidence':ev(page),'reader':'Codex author','date':'2026-11-18',
  'non_item_content':'Every worked example,exercise question,data table,teaching graph and mathematical callout enumerated. Best-fit key values remain explicitly approximate;source measurements are preserved separately.'})
if __name__=='__main__':
 for name,data in [('answers-Goldie-C2-models.json',{'scope':'EveryExample6–8and Exercise2C1–9response;fitted models are nonunique.','items':answers}),('census-Goldie-C2-models.json',{'book':'Goldie','book_id':'8227-SRC-015','chapter':2,'source_path':SRC,'source_sha256':SHA,'scope':'Complete51–58including every given table,worked/given graph and callout.','new_items':figures,'corrections':[{'item_id':r['item_id'],'continuation_pdf_pages':r['continuation_pdf_pages']}for r in answers if r.get('continuation_pdf_pages')],'pages':pages}),('data-fits-Goldie-C2.json',{'status':'Author fixed-source mathematical QA;independent acceptance pending.','datasets':datasets})]:
  (W/'tools/textbook-r5'/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
 for r in answers:
  for p in r['subparts']:
   if 'operation'in p:assert equivalent(compute(p['operation']),expression(p['printed_key_normalised'])),(r['item_id'],p['subpart'])
   for name,expected in p.get('additional_operation_expected',{}).items():assert equivalent(compute(p['additional_operations'][name]),expression(expected)),(r['item_id'],p['subpart'],name)
 print(len(answers),'items;',sum(len(r['subparts'])for r in answers),'outputs;',len(figures),'figures;',len(datasets),'independently cross-checked data fits')
