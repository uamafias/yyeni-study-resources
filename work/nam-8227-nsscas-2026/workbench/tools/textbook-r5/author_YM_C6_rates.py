"""YM290–293: rates,kinematics,and forward connected rates."""
import json
import author_YM_C6_opening as h
from author_YM_C6_opening import W,SRC,SHA,pp,ev,v,reasoning,fig,figures,compute,expression,equivalent
h.answers.clear();h.new.clear();h.corrections.clear();figures.clear()
answers=h.answers;new=h.new;corrections=h.corrections
POWER=h.POWER;CHAIN='8227:2020:M1:T8:O02:D02';RATE='8227:2020:M1:T8:O03:D03';MOTION='8227:2020:M1:T8:O03:D04';extra=h.extra
def add(kind,n,page,note,parts,direct,components,powers):
 r=h.add(kind,n,page,note,parts,direct,components,powers=powers)
 r['mapping_rationale']='Distinguish original quantity,first rate and second rate;use the requested differentiation variable. Connected rates require multiplying the local derivative by the SIGNED given input rate,not just finding a gradient. Displacement/velocity/acceleration are distinct physical outputs;speed is the absolute value of velocity.'
 r['precision_angle_check']={'source':'Exact finite decimals,fractions,and explicit pi forms. Physical units are stated per response;the two abstract Try19functions do not name physical units.','comparison':'Carry original time/radius units into rates,including square/cubic powers. Preserve signed decreases. Do not round intermediate derivatives or invent unit precision. Distinguish negative acceleration from deceleration by the velocity direction.'}
 return r
def val(label,expr,key,kp,direct,method,units=None,printed_units=None,components=None):
 p=v(label,expr,key,kp,method);p.update(assessed_8227_demand_ids=direct,component_demand_ids=components or[])
 if units:p.update(units=units,printed_key_units=printed_units or units)
 return p
def time_rate(label,fn,at,key,kp,units=None,chain=False):
 return val(label,f'diff({fn},t).subs(t,{at})',key,kp,[RATE],'Differentiate the ORIGINAL quantity with respect tot,then substitute the specified time. A negative result is a decrease,not an incorrect sign to discard. Use the source time unit and quantity unit;do not import units from a neighbouring example.',units,components=[CHAIN]if chain else[POWER])
def connected(label,fn,var,at,input_rate,key,kp,units,printed_units=None):
 return val(label,f'diff({fn},{var}).subs({var},{at})*({input_rate})',key,kp,[RATE],'Use the ORIGINAL quantity relation,derive its local rate with respect to'+var+',substitute the current'+var+'value,then MULTIPLY by the ORIGINAL SIGNED input rate with respect tot. Decreasing input means a negative factor. Track quantity powers in the final unit.',units,printed_units,[CHAIN])

add('Try-Now-19',1,290,'Find dA/dtatt3from A=2t²−4t+5;no physical units are specified.',[time_rate('dA-dt','2*t**2-4*t+5','3','8',621)],[RATE],[POWER],['2','1'])
add('Try-Now-19',2,290,'Find the time rate of1/sqrt(2t+1)att4,including its negative sign and original rootdomain.',[time_rate('dy-dt','1/sqrt(2*t+1)','4','-Rational(1,27)',621,chain=True)],[RATE],[CHAIN],['−1/2'])
ps=[val('a-i-depth','sqrt(1+2*0)','1',290,[],'Evaluate the ORIGINAL depthh=sqrt(1+2t)att0,not its derivative. The stated time isseconds and depthcm.','cm'),val('a-ii-depth','sqrt(1+2*4)','3',290,[],'Evaluate the ORIGINAL depthatt4. This supplies a physical quantity,not a rate.','cm'),time_rate('b-dh-dt','sqrt(1+2*t)','4','Rational(1,3)',290,'cm/s',True)]
add('Example',20,290,'Water depthsqrt(1+2t)cm:find initial/four-second depths and its rateatt4. The root condition holds for physicalt>=0.',ps,[RATE],[CHAIN],['1/2'])
ps=[val('a-i-M','50/(1+0**2)','50',621,[],'Evaluate the ORIGINAL amount modelatt0hours. This is a source mathematical model,not a medical recommendation.','mg'),val('a-ii-M','50/(1+2**2)','10',621,[],'Evaluate the ORIGINAL amountatt2hours;the denominator isalwayspositive.','mg'),time_rate('b-dM-dt','50/(1+t**2)','2','-8',621,'mg/h',True)]
add('Try-Now',20,290,'For the supplied amount model50/(1+t²)mg with timeinhours,find amountsat0/2hours and the signed rate−8mg/hatt2.',ps,[RATE],[CHAIN],['−1','2'])
ps=[val('a-displacement','(6*t-3*t**2+t**3/3).subs(t,1)','Rational(10,3)',291,[MOTION],'Evaluate the ORIGINAL displacement modelatt1;do not use its derivative or confuse displacement with cumulative distance.','m'),val('b-velocity','diff(6*t-3*t**2+t**3/3,t).subs(t,1)','1',291,[MOTION],'Velocity is the first time derivative of signed displacement. Atthisinstantit ispositive1m/s,so speedalso1.','m/s',components=[POWER]),val('c-acceleration','diff(6*t-3*t**2+t**3/3,t,2).subs(t,1)','-4',291,[MOTION],'Acceleration is the SECOND time derivative of displacement. Here velocityispositive1while acceleration−4,so the speed decreases and the source alternative deceleration4m/s²is validatthisinstant. Negativeaccelerationalonewouldnotalwaysimplydeceleration.','m/s^2',components=[POWER])]
ps[-1]['valid_alternatives']=['Deceleration4m/s²,because the velocity at this instant is positive.']
add('Example',21,291,'Find displacement,velocity and acceleration from6t−3t²+t³/3at1second,keeping signs and units distinct.',ps,[MOTION],[POWER],['3','2','1'])
ps=[val('a-displacement','(10*(2*t+1)**5-7).subs(t,2)','31243',621,[MOTION],'Evaluate the ORIGINAL displacement10(2t+1)^5−7att2. It is statedt>=0andmotionawayfromO;the derivative ispositive there.','m'),val('b-velocity','diff(10*(2*t+1)**5-7,t).subs(t,2)','62500',621,[MOTION],'Use the ORIGINAL first derivative100(2t+1)^4,then substitutet2. Keep the source model values;large magnitudes are not evidence of a different mathematical method.','m/s',components=[CHAIN]),val('c-acceleration','diff(10*(2*t+1)**5-7,t,2).subs(t,2)','100000',621,[MOTION],'Differentiate velocityagain:800(2t+1)^3,then substitutet2. The extra inner derivative2must be retained in both steps.','m/s^2',components=[CHAIN])]
add('Try-Now',21,291,'For the given formal motion model10(2t+1)^5−7metres,t>=0,find all three motion quantitiesatt2seconds. These large values are source-model outputs,not an endorsed realistic everyday scenario.',ps,[MOTION],[CHAIN],['5'])
add('Example',22,292,'Paint-circle radius increases1/5cm/s;find area rateatr10cm in exact pi form.',[connected('dA-dt','pi*x**2','x','10','Rational(1,5)','4*pi',292,'cm^2/s')],[RATE],[POWER],['2'])
p=connected('dA-dt','pi*x**2','x','8','Rational(2,5)','Rational(32,5)*pi',621,'cm^2/s','cm/s')
p['source_unit_warning']='The printed key has6.4pi cm/s,but this is AREAperTIME and requirescm²/s. Numeric6.4piis correct;the source unit is not.'
add('Try-Now-22',1,292,'Circle radius8cm increasing0.4cm/s gives area rate6.4pi cm²/s;the printed key omits the square oncm.',[p],[RATE],[POWER],['2'])
ps=[connected('a-surface-rate','4*pi*x**2','x','6','Rational(1,5)','Rational(48,5)*pi',621,'cm^2/s'),connected('b-volume-rate','Rational(4,3)*pi*x**3','x','6','Rational(1,5)','Rational(144,5)*pi',621,'cm^3/s')]
add('Try-Now-22',2,292,'Sphere radius6cm increasing0.2cm/s:find surface-area and volume rates separately,using the supplied formulas and exact pi answers.',ps,[RATE],[POWER],['2','3'])
add('Example',23,293,'Ony=2+3/(2x−1),xDECREASES0.06units/satx2;the resulting positiveyrate is0.04units/s.',[connected('dy-dt','2+3/(2*x-1)','x','2','-Rational(3,50)','Rational(1,25)',293,'units/s')],[RATE],[CHAIN],['−1'])
add('Try-Now-23',1,293,'On(1/2)(4x−3)^−1atA(1,1/2),xDECREASES0.3units/s;the negative gradient and negative inputrate givepositiveyrate0.6.',[connected('dy-dt','Rational(1,2)*(4*x-3)**(-1)','x','1','-Rational(3,10)','Rational(3,5)',621,'units/s')],[RATE],[CHAIN],['−1'])
add('Try-Now-23',2,293,'On12/(x²+3)atx1,xINCREASES0.012units/s;the negative local gradient givesyrate−0.018.',[connected('dy-dt','12/(x**2+3)','x','1','Rational(3,250)','-Rational(9,500)',621,'units/s')],[RATE],[CHAIN],['−1','2'])
add('Try-Now-23',3,293,'Onsqrt(5x+4)atx1,xINCREASES0.03units/s;the positive local gradient5/6givesyrate0.025.',[connected('dy-dt','sqrt(5*x+4)','x','1','Rational(3,100)','Rational(1,40)',621,'units/s')],[RATE],[CHAIN],['1/2'])

refs=[(28,291,'Displacement-to-velocity-to-acceleration sequence','v=ds/dt,a=dv/dt. Signed velocity differs from speed|v|. The source prose calls the first position derivative speed;the correct general interpretation isvelocity. Negativeaccelerationimpliesdecelerationonlywhenthevelocitydirectionmakes speeddecrease.',[MOTION],'diagram',[]),(29,292,'Connected-rate chain reference','dy/dt=(dy/dx)(dx/dt);forcircleareaA=pi r²,use dA/dt=(2pi r)(dr/dt). The inputrate sign and radius/area units must survive the multiplication.',[RATE],'table',[('diff(pi*x**2,x)','2*pi*x')]),(30,292,'Supplied sphere surface and volume formulas','Surface4pi r²andvolume(4/3)pi r³give derivatives8pi rand4pi r²respectively. Multiply by the SAME given radialrate;do not give identicalunitsforbothoutputs.',[RATE],'table',[('diff(4*pi*x**2,x)','8*pi*x'),('diff(Rational(4,3)*pi*x**3,x)','4*pi*x**2')])]
for n,page,label,note,teaches,rep,checks in refs:
 fig(n,page,label,note,teaches,rep,checks);r=figures[-1];r['item_id']=r['item_id'].replace('Goldie:C5:','YM:C6:');r.update(printed_page=pp(page),source_evidence=ev(page),value_level_scope_decisions=[])
 r['mathematical_feature_review']['method']='Read the source variable/unit labels and derivative arrows. Independently derive the quantity-rate relations and distinguish signed motion,area/volume powers,and supplied versus derived formulas.'
pages=[dict(pdf_page=page,printed_page=pp(page),chapter=6,page_status='items enumerated',item_ids=[r['item_id']for r in answers if r['source_pdf_page']==page]+[r['item_id']for r in figures if r['pdf_page']==page],continuation_item_ids=[],source_evidence=ev(page),reader='Codex author',date='2026-11-19',non_item_content='AllExamples20–23,Try19Q1/2,Try20/21,Try22Q1/2,Try23Q1–3andthreeformula/sequence referencesare enumerated over290–293. SourceTry22Q1unit defect andspeed/velocitywording qualificationare retained.',scope_screen='Prescribed rates,connectedrates,anddisplacement/velocity/acceleration. Preservephysicalt>=0wheregiven,positive radii,root/denominator domains,signed rates,and squared/cubed units. No new physical law or medical advice is inferred.')for page in range(290,294)]
if __name__=='__main__':
 for name,data in [('answers-YM-C6-rates.json',dict(scope='All290–293explicit tasks.',items=answers)),('census-YM-C6-rates.json',dict(book='YM',book_id='8227-SRC-017',chapter=6,source_path=SRC,source_sha256=SHA,scope='Complete290–293page census.',new_items=new+figures,corrections=corrections,pages=pages))]:
  (W/'tools/textbook-r5'/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
 for r in answers:
  for p in r['subparts']:
   if 'operation'in p:assert equivalent(compute(p['operation']),expression(p.get('author_expected_normalised',p['printed_key_normalised']))),(r['item_id'],p['subpart'])
   for name,op in p.get('additional_operations',{}).items():assert equivalent(compute(op),expression(p['additional_operation_expected'][name])),(r['item_id'],p['subpart'],name)
 print(len(answers),'items;',sum(len(r['subparts'])for r in answers),'responses;',len(figures),'references;',len(pages),'pages')
