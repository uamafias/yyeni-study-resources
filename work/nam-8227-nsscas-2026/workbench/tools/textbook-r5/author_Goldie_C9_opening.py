"""Retain rate formation and elementary integration inside the ODE chapter.

Separation of variables is not made a required8227method. Source context
models are conditional mathematical premises,not verified scientific laws.
"""
import json,hashlib
import author_Goldie_C8_opening as base
from author_Goldie_C8_opening import W,SRC,SHA,value,reasoning,fig,figures,compute,expression,equivalent,primitive_agrees
RATE='8227:2020:M1:T8:O03:D03';NOTATION='8227:2020:M1:T8:O01:D02'
POWER='8227:2020:M1:T9:O01:D02';CONSTANT='8227:2020:M1:T9:O02:D01';AFFINE='8227:2020:M2:T5:O01:D01';TRIGINT='8227:2020:M2:T5:O01:D02'
def ev(page):
 name='Goldie-C8-summary-key354-source'if page==354 else'Goldie-C9-end-keys-source'if page>=355 or page==247 else f'Goldie-C9-{231+4*((page-231)//4)}-source'
 p=W/f'checks/r5/textbooks/{name}.png';return {'path':str(p.relative_to(W.parents[2])),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
base.ev=ev;base.answers.clear();base.new.clear();figures.clear();answers=base.answers;new=base.new
def add(*args,**kwargs):
 row=base.add(*args,**kwargs);row['item_id']=row['item_id'].replace(':C8:',':C9:');new[-1]['item_id']=row['item_id']
 row['mapping_rationale']='Rate notation,proportional-rate modelling and differentiating known geometry are prescribed rate-problem facets. Directly integrate a derivative depending only on the independent variable. Choosing/solving a general separable equation is additional;no source context certifies an actual scientific law.'
 row['value_level_scope_decisions']=[{'rule_id':'8227:LIMIT07','status':'not applicable','quoted_value':row['notes'],'reason':'This retained task forms a rate relation or directly integrates an explicit function of the independent variable;it requires no general integration substitution or separation-of-variables procedure.'}]
 return row
def v(label,expr,key,method,page):return value(label,expr,key,page,method)

parts=[]
for label,conclusion in [('drinkable-time','No unique time is determined without an initial temperature,ambient temperature,cooling constant and an agreed meaning of drinkable.'),('cold-time','Cold also needs an explicit temperature threshold;Newton cooling approaches ambient asymptotically and does not reach it in finite time in the ideal model.'),('meaning','Treat drinkable/cold as context-dependent temperature ranges,not exact mathematical or safety definitions.')]:
 parts.append(reasoning(label,conclusion,'The opening source gives no measured cooling constant or temperature data. Its answer section offers illustrative5–10minute/25minute estimates under unspecified conditions;these are not independently determined answers. A model-based time would solveT₀+(Tinitial−T₀)e^(−λt)=Tthresholdwithλ>0and a reachable threshold. No personal temperature or drinking-safety recommendation is made.',354,'key incomplete'))
row=add('Prompt',1,231,'Discuss waiting times for the pictured coffee to become drinkable/cold,and define those terms. The prompt supplies no parameters or thresholds,so its illustrative key times cannot be unique derived values.',parts,teaches=[RATE],rep='diagram')
# This is an explicitly open prompt. Its key's illustrative suggestions are not
# a defect: manual status is no-key for a unique mathematical value,with the
# actual source illustrative content retained in the derivation.
for p in parts:p['author_comparison_status']='no key';p['key_presence']='Open response;illustrative estimates exist but no determinate numerical answer.'

p=v('model','(-1)/5','-Rational(1,5)',
 'Write dv/dt=−kvwithk>0because the source states velocity is decreasing. Atv=5anddv/dt=−1,the coefficient is−1/5;hencedv/dt=−v/5. The response stores the multiplier ofv;no differential-equation solution is requested.',233)
row=add('Example',1,233,'Form the rate equation for an object whose decreasing velocity rate is proportional to velocity,and calibrate it fromv=5m/sanddv/dt=−1m/s². Resultdv/dt=−v/5.',[p],[RATE])
p=reasoning('model','dθ/dr=−k/r²withk>0and r>0.',
 'The specified gradient decreases with outward radial distancer,so choose the negative sign;inverse-square proportionality gives1/r². This expresses the stipulated mathematical model without solving a differential equation. The source itself says the model breaks down near the stellar centre;no actual stellar law is certified.',233,'matches')
add('Example',2,233,'Translate the given outward decreasing inverse-square temperature gradient into dθ/dr=−k/r². The independent variableris distance,not time;the centre is excluded.',[p],[RATE])
p=v('side-rate','k*x/diff(x**2,x)','k/2',
 'For a nondegenerate square of sides>0,A=s²anddA/ds=2s. The stipulated area rate isks. Chain rates giveds/dt=(dA/dt)/(dA/ds)=ks/(2s)=k/2. Do not divide bysat a degenerate zero square.',234)
add('Example',3,234,'A square’s area increases at a rate proportional to its side. UseA=s²anddA/dt=ksto findds/dt=k/2for s>0;no ODE solving occurs.',[p],[RATE])

p=reasoning('interpretation','dv/dtis acceleration;the stated equation gives acceleration5v²,which is nonnegative and proportional to the square of signed velocity.',
 'The independent variable is time in seconds and velocity is measured in metres per second,so dv/dthas acceleration unitsm/s². Sincev²≥0,the acceleration is positive wheneverv≠0. This does not imply that speed increases for a negative velocity:positive acceleration then initially reduces its magnitude. The key states acceleration and proportional-to-square meaning.',354,'matches')
add('Exercise-9A',1,234,'Interpretdv/dt=5v²for one-dimensional motion. Identify acceleration and the proportional-square dependence while keeping signed velocity distinct from speed.',[p],[RATE,NOTATION])

spec=[
 (2,'inverse-square-speed','k/x**2','k/x**2','The source gives speed inversely proportional to the positive distance travelleds,so ds/dt=k/s²withk>0ands>0. The expression usesxto represent the source distances;it is singular at the start and is only the stipulated model.'),
 (3,'height-rate','k*log(a-x)','k*log(a-x)','The stipulated rate is kln(H−h);the expression usesaforHandxforh. A real logarithm requiresH−h>0. The stated increasing-rate interpretation additionally restricts the chosen model range/sign;the formula is not a certified global growth law approachingH.'),
 (4,'mass-rate','k/x','k/x','For positive massmofB,dm/dt=k/m. This is a translation of the question’s inverse-proportional premise,not a verified chemical rate law.'),
 (5,'profit-rate','k*sqrt(x)','k*sqrt(x)','For stipulated nonnegative profitP,dP/dt=k√Pwithk>0. Keep the real square-root domain;the advertising context is a premise,not causal evidence.'),
 (6,'temperature-rate','k*x','k*x','The derivative isde/dθ=kθ,not a time derivative. The stipulated temperature variable must use the source’s chosen scale. The model is used only over a range preserving0≤e≤1;no global physical extrapolation is asserted.'),
 (7,'cooling-coefficient','(-Rational(1,2))/(95-15)','-Rational(1,160)','Use dθ/dt=c(θ−15). The initial dataθ95andrate−0.5°C/sforcec=−1/160s⁻¹. The output storesc;the full relation is−(θ−15)/160.'),
 (8,'bacterial-coefficient','10**5/(2*10**6)','Rational(1,20)','The proportional initial-growth modelN′=cNhasc=100000/2000000=1/20perday. Keep the per-day time unit and the stated initial-growth limitation.'),
 (9,'acceleration-coefficient','2*sqrt(4)','4','The stipulated relationdv/dt=k/√vusesv>0. Withv4andacceleration2,k=4,sodv/dt=4/√v. This is model calibration,not verification of the named force.'),
 (10,'oil-area-rate','diff(pi*x**2,x)*k/(pi*x**2)','2*k/x','Forr>0,A=πr²anddr/dt=k/A. Chain rates givedA/dt=2πr·k/A=2k/r=2k√π/√A. The computed expression usesr=x;its equivalentAform is recorded in the conclusion.'),
 (11,'distance-gradient-coefficient','-10/40','-Rational(1,4)','Temperature decreases with distance from the fire end: dθ/ds=cs. The halfway distances40cmandgradient−10°C/cmforcec=−1/4. This is not a time-cooling equation.')]
for n,label,expr,key,method in spec:
 p=reasoning(label,method,method,354,'matches')if n in[2,3,4,5,6]else v(label,expr,key,method,354)
 row=add('Exercise-9A',n,235,f'9A{n}: '+method,[p],[RATE])
 if n==10:p['author_answer_form']='dA/dt=2k√π/√AwithA>0.'
p=v('volume-coefficient','-8/((Rational(4,3))*pi*15**3)','-2/(1125*pi)',
 'The stipulated outflow is proportional to remaining volume,soV′=cVwithc<0. At radius15cm,the sphere contains4500πcm³. The loss8cm³/sgivesc=−8/(4500π)=−2/(1125π). ThusV′=−2V/(1125π).',354)
add('Exercise-9A',12,236,'Calibrate a spherical-balloon volume-loss rate fromradius15cmandoutflow8cm³/s. The radius only fixes that calibration volume;the model is proportional to volume,not directly to radius.',[p],[RATE])
p=reasoning('height-rate','dh/dt=(2−k√h)/100,withh≥0andk>0.',
 'For the square-base tank,the cross-sectional area is100cm²andV=100h. Net volume rate is inflow2minusoutflowk√hcm³/s,so100dh/dt=2−k√h. The source specifies the outflow coefficient only up to proportionality;keepk>0andh≥0.',354,'matches')
add('Exercise-9A',13,236,'Find the water-height rate in a10cm-square-base tank with2cm³/sinflow and outflow proportional to√h. Resultdh/dt=(2−k√h)/100;there is no separation-of-variables task.',[p],[RATE])

p=v('primitive','integrate(3*x**2-2,x)','x**3-2*x',
 'Integrate the explicitly supplied derivative3x²−2termwise. The family isy=x³−2x+Cwith any real constant;differentiate the result to confirm the original gradient. The equation’s chapter label does not turn this into a new separable-method requirement.',237)
p['author_answer_form']='y=x³−2x+C,C∈ℝ.'
add('Example',4,237,'Recover the general curve fromdy/dx=3x²−2by direct elementary integration. Preserve the arbitrary constant and family of vertical translations.',[p],[POWER,CONSTANT])

p=reasoning('one-constant','Two additive constants collapse to one because only their difference matters.',
 'If antiderivatives satisfy ln|y|+C₁=x²/2+C₂,subtractC₁to writeln|y|=x²/2+CwithC=C₂−C₁. A difference of arbitrary real constants is arbitrary real. The algebraic constant principle is prescribed integration support;the surrounding separation-of-variables solution remains additional. With sourcey>0,the later multiplicative constantA=e^Cmust be positive.',354,'matches')
row=add('Prompt',2,238,'Explain why integrating both sides needs only one arbitrary additive constant. Retain that constant-combination concept separately from the surrounding extra separable-ODE method.',[p],teaches=[CONSTANT])
row['scope_check'].update(status='in-scope-parts-only',excluded_or_qualified_parts=['The surrounding general separation-of-variables technique is additional;only the arbitrary-constant principle is retained.'])

parts=[]
for label,f,key in [('i','x**2','x**3/3'),('ii','cos(x)','sin(x)'),('iii','exp(x)','exp(x)'),('iv','sqrt(x)','2*x**(Rational(3,2))/3')]:
 p=v(label,'0',key,'Independently integrate the explicit function ofxand differentiate the resulting primitive;include an arbitrary constant. For√x,the real interior isx>0and the curve extends to0. No separation of variables or new substitution method is needed.',354)
 p['operation']={'kind':'real-elementary-antiderivative','operands':[f]};p['answer_equivalence']='up-to-additive-constant';parts.append(p)
row=add('Exercise-9B',1,239,'Recover the four general curves fromdy/dx=x²,cosx,e^xand√x. These are ordinary prescribed primitives,despite the differential-equations chapter heading.',parts,[POWER,CONSTANT,AFFINE,TRIGINT])
row['direct_demand_aspects']=[{'demand_id':POWER,'assessed_facet':'iandiv'},{'demand_id':CONSTANT,'assessed_facet':'all four general primitives'},{'demand_id':AFFINE,'assessed_facet':'iii'},{'demand_id':TRIGINT,'assessed_facet':'ii'}]

for n,page,label,note,teaches,rep,checks,parent in [
 (1,231,'Coffee photograph','A context photograph fixes no cooling constant,initial condition or temperature threshold. It cannot supply a unique waiting time or be reused as numerical temperature evidence.',[],'diagram',[], 'Prompt:1'),
 (2,231,'Figure9.1 cooling graph','The illustrative temperature curve decreases toward ambientT₀from above as time increases. ForT′=k(T−T₀)this shape requiresk<0. A visual horizontal asymptote is not a finite time at which ambient temperature is attained.',[RATE],'graph',[],None),
 (3,232,'Figure9.2 signed position and rate definitions','The number line marks a positive position+5. Velocity isds/dtandaccelerationdv/dt. Positive velocity means increasing signed coordinate,which can point toward the origin from a negative position;the adjacent generic away/toward wording needs this qualification.',[RATE,NOTATION],'diagram',[],None),
 (4,233,'Inverse-square stellar model boundary note','The source warns its inverse-square temperature-gradient model breaks down near the centre. Retainr>0and its modelling limitation;the context does not verify stellar physics.',[RATE],'table',[], 'Example:2'),
 (5,234,'Figure9.3 growing square','The given square has sidesandareaA=s². For positives,the derivative2slinks area and side rates;the limiting degenerate square does not permit cancellation bys.',[RATE],'diagram',[('diff(x**2,x)','2*x')],'Example:3'),
 (6,237,'General integral as vertically translated curves','For the explicit derivative3x²−2,the general curvex³−2x+Chas the same derivative for everyC. A later point condition selects a member;general separable-ODE solution is not needed for this example.',[CONSTANT],'table',[('diff(x**3-2*x+c,x)','3*x**2-2')],'Example:4')]:
 fig(n,page,label,note,teaches,rep,checks,parent)
for f in figures:
 f['item_id']=f['item_id'].replace(':C5:',':C9:');f['parent_item_id']=f['parent_item_id'].replace(':C5:',':C9:')if f['parent_item_id']else None;f['source_evidence']=ev(f['pdf_page']);f['value_level_scope_decisions']=[{'rule_id':'8227:LIMIT07','status':'not applicable','quoted_value':f['notes'],'reason':'A rate/primitive reference or given figure;no general integration method is required.'}]
notes={231:'All three open coffee questions,context photo and cooling graph retained. The open key estimates are illustrative,not unique mathematical results.',232:'Rate-notation and signed-position reference retained. The generic away/toward-velocity wording has a coordinate-sign caution;the diagram shows only one positive-position example.',233:'Examples9.1/2form proportional-rate equations without solving them. The inverse-square model-limit warning is recorded separately.',234:'Example9.3uses connected rates for a square.9A1interprets acceleration. Both are retained;their chapter name does not require ODE solution methods.',235:'Every9A2–11rate-model response retained. Context laws remain stipulated toy premises with domains/units;none of these questions asks separation of variables.',236:'9A12/13are retained calibration/net-volume/height-rate problems. The UnderPressure investigation and map begin here and are owned by the next builder;they must exist before a census build.',237:'Example9.4is ordinary direct integration and is retained. Example9.5chooses general separation of variables and is additional. Its supplied y>0restriction matters for its positive multiplicative constant.',238:'The boxed constant-combination prompt is retained. General separation exposition and its arbitrary-method differential notation are additional;the supporting algebra principle does not expand scope.',239:'All four9B1direct primitives retained.9B2explicitly forces separating variables and is additional. Example9.6is a separate extra nonlinear-ODE task;its absolute-value/domain statement is not certified here. The particular-solution prose continues on240.'}
pages=[]
for page in range(231,240):
 ids=[r['item_id']for r in answers if r['source_pdf_page']==page]+[r['item_id']for r in figures if r['pdf_page']==page]
 if page==236:ids+=['8227:TB:Goldie:C9:Investigation:1','8227:TB:Goldie:C9:Teaching-figure:7']
 if page==238:ids+=['8227:TB:Goldie:C9:Teaching-figure:15','8227:TB:Goldie:C9:Teaching-figure:16']
 if page==239:ids+=['8227:TB:Goldie:C9:Teaching-figure:14']
 pages.append({'pdf_page':page,'printed_page':page-14,'chapter':9,'page_status':'items enumerated','item_ids':ids,'continuation_item_ids':[],'source_evidence':ev(page),'reader':'Codex author','date':'2026-11-18','non_item_content':notes[page],'scope_screen':'Rate formation and direct independent-variable integration survive the wider separable-ODE chapter exclusion.'})
if __name__=='__main__':
 for name,data in [('answers-Goldie-C9-opening.json',{'scope':'Every retained231–239rate/explicit-primitive response;separable-method scope separate.','items':answers}),('census-Goldie-C9-opening.json',{'book':'Goldie','book_id':'8227-SRC-015','chapter':9,'source_path':SRC,'source_sha256':SHA,'scope':'Complete231–239with UnderPressureinvestigation/maplinked to the next builder.','new_items':new+figures,'corrections':[],'pages':pages})]:
  (W/'tools/textbook-r5'/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
 for r in answers:
  for p in r['subparts']:
   if 'operation'in p:
    got=compute(p['operation']);target=expression(p['printed_key_normalised'])
    assert primitive_agrees(p['operation'],got,target)if p.get('answer_equivalence')=='up-to-additive-constant'else equivalent(got,target),(r['item_id'],p['subpart'],got)
   for name,op in p.get('additional_operations',{}).items():assert equivalent(compute(op),expression(p['additional_operation_expected'][name])),(r['item_id'],name)
 print(len(answers),'items;',sum(len(r['subparts'])for r in answers),'outputs;',len(figures),'figures')
