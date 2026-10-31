"""Bind generated task slots to explicit topic objectives and original numerical contexts."""
from pathlib import Path
import json
W=Path(__file__).resolve().parents[1];ROOT=W.parents[1]
# topic: principal source-bullet anchors, physical context, x label, y label,
# x values, gradient, intercept. Invented values are planning stimuli, never real observations.
SPEC={
'1':(['1.1-02','1.2.4-03'],'Timing repeated pendulum oscillations','Oscillation count','Elapsed time / s',[5,10,15,20,25,30],1.6,0),
'2':(['1.2.1-02','1.2.2-03'],'Controlled low-voltage water heating','Heating time / s','Temperature / °C',[0,30,60,90,120,150],.08,22),
'3':(['1.2.3-09','1.2.5-05'],'Position readings from a slowly moving model vehicle','Time / s','Position / cm',[0,2,4,6,8,10],3,5),
'4':(['2.1-05','2.2-04'],'Timing a pendulum with repeated complete oscillations','Oscillation count','Elapsed time / s',[5,10,15,20,25,30],1.4,0),
'5':(['2.3.2-07','2.3.3-05'],'Uniformly accelerating model vehicle','Time / s','Speed / m s⁻¹',[0,1,2,3,4,5],.2,.1),
'6':(['2.4-05','2.4-06'],'Loading a spring within its proportional range','Force / N','Extension / mm',[0,.2,.4,.6,.8,1],12,0),
'7':(['2.6-01','2.6-02'],'Mass and volume of a liquid after subtracting the container mass','Volume / cm³','Mass / g',[5,10,15,20,25,30],.8,0),
'8':(['2.7-04','2.7-06'],'Balancing a lever with a fixed opposing moment','Effort distance / m','Reciprocal effort / N⁻¹',[.05,.10,.15,.20,.25,.30],.5,0),
'9':(['2.10.2-01','2.10.2-02'],'Model solar water heater over a short interval with steady illumination','Time / min','Water temperature / °C',[0,2,4,6,8,10],.8,21),
'10':(['2.10.3-04','2.10.5-02'],'Lifting a fixed load slowly at a steady rate','Time / s','Gravitational energy gained / J',[0,2,4,6,8,10],3,0),
'11':(['2.11-05','2.11-07'],'Pressure difference at different depths in water','Depth / m','Pressure difference / Pa',[0,.02,.04,.06,.08,.10],10000,0),
'12':(['3.1-02','3.1-03'],'Thermal expansion of a liquid in a narrow tube over a limited range','Temperature / °C','Liquid-column length / mm',[20,25,30,35,40,45],.6,10),
'13':(['3.2.1-03','3.2.1-06'],'Calibrating a liquid-column thermometer','Reference temperature / °C','Column length / mm',[20,30,40,50,60,70],.7,8),
'14':(['3.2.2-06','3.2.2-07'],'Heating a fixed 0.20 kg sample with negligible loss in this model','Temperature rise / K','Energy supplied / J',[0,2,4,6,8,10],800,0),
'15':(['3.3.3-03','3.3.4-01'],'Initial cooling of a covered water container over a short approximately linear interval','Time / s','Temperature / °C',[0,20,40,60,80,100],-.08,78),
'16':(['4.1-09','4.1-12'],'Ripple-tank waves at fixed water depth','Period / s','Wavelength / cm',[.10,.15,.20,.25,.30,.35],20,0),
'17':(['4.3.2-03','4.3.2-05'],'Ray-box investigation of a plane mirror','Incidence angle / °','Reflection angle / °',[10,20,30,40,50,60],1,0),
'18':(['4.3.3-04','4.3.3-05'],'Ray-box investigation of refraction through a rectangular block','sin r','sin i',[.10,.20,.30,.40,.50,.60],1.5,0),
'19':(['4.3.4-01','4.3.4-03'],'Electromagnetic band ordering, applications and hazards',None,None,[],0,0),
'20':(['4.4-06','4.4-10'],'Echo timing with a supplied average air sound speed model','Round-trip time / s','Reflector distance / m',[.10,.20,.30,.40,.50,.60],170,0),
'21':(['5.1-08','5.1-10'],'Electron transfer and induction using labelled conductor diagrams',None,None,[],0,0),
'22':(['5.2.1-03','5.2.2-05'],'Measuring open-circuit voltage from identical cells in series','Cell count','Potential difference / V',[1,2,3,4,5,6],1.45,0),
'23':(['5.2.4-04','5.3-07'],'Fixed-temperature metallic resistor at low voltage','Current / A','Potential difference / V',[.05,.10,.15,.20,.25,.30],12,0),
'24':(['5.4-02','5.4-04'],'Energy accounting for a fixed-power low-voltage heater','Heating time / s','Supplied energy / J',[0,20,40,60,80,100],5,0),
'25':(['5.7.1.1-03','5.7.1.2-01'],'Empirical lifting-force measurements for an electromagnet at fixed geometry','Current / A','Lifting force / N',[.10,.20,.30,.40,.50,.60],2,.1),
'26':(['5.7.2.3-02','5.7.2.3-05'],'A model transformer with fixed primary supply and idealised readings','Secondary turns','Secondary voltage / V',[20,40,60,80,100,120],.05,0),
'27':(['6.1.1-05','6.1.2-01'],'Nuclide-number tables and original alpha/beta decay equations',None,None,[],0,0),
'28':(['6.2.4-01','6.2.5-02'],'Original activity-time data for half-life reasoning',None,None,[],0,0)}
reg=json.loads((W/'curriculum/objective_registry.json').read_text())['objectives'];ids={x['objective_id'] for x in reg};rows=[]
for t,(anchors,context,xlabel,ylabel,xs,slope,intercept) in SPEC.items():
 oids=['OBJ-6118-'+x for x in anchors];assert set(oids)<=ids,(t,oids)
 p=W/f'topics/{t}/work_order.json';wo=json.loads(p.read_text())
 spec=dict(topic_id=t,objective_ids=oids,context=context,stimulus_origin='Original invented planning data; not observed measurements or official question text.',practical_data=None,source_architecture_refs=['curriculum/answer-shapes.json','planning/task-shape-anchors.json'])
 if xs:
  spec['practical_data']=dict(x_heading=xlabel,y_heading=ylabel,rows=[[x,round(slope*x+intercept,6)] for x in xs],expected_gradient=slope,expected_intercept=intercept,unit_rule='Vertical-axis unit divided by horizontal-axis unit; angle/count ratios may be dimensionless.',model_limit='Idealised practice data only. Do not infer that every real dataset is exact, that every line passes through the origin, or that the gradient is automatically a familiar constant.')
 if t=='8':spec['context_limit']='The opposing moment is 2.0 N m; plotting reciprocal effort avoids pretending effort itself is proportional to its arm.'
 if t=='12':spec['context_limit']='Use empirical expansion readings; do not turn the qualitative gas laws into added quantitative theory.'
 if t=='14':spec['context_limit']='The model corresponds to specific heat capacity 4000 J kg⁻¹ K⁻¹; do not call this the measured value for all liquids.'
 if t=='20':spec['context_limit']='Distance is one-way; the travel time is for the return trip. Sound speed is twice the plotted gradient.'
 if t=='24':spec['context_limit']='Energy is calculated from the stated 5 W input. The graph is data-processing practice, not an independent experimental verification of E = Pt.'
 if t=='25':spec['context_limit']='An illustrative empirical range only; do not infer a universal linear magnetic-force law or teach F = BIl beyond the syllabus.'
 for task in wo['performance_tasks']:
  task['objective_ids']=oids;task['task_specification']=f'curriculum/topic-task-specifications.json: topic {t}'
  task['assessment_objectives']=['C'] if task['item_type']=='practical_task' else ['A','B']
  task['mark_tariff']=16 if task['item_type']=='practical_task' else 12 if task['item_type']=='multiple_choice_set' else 8
  task['ao_split']={'C':16} if task['item_type']=='practical_task' else {'A':7.5,'B':4.5} if task['item_type']=='multiple_choice_set' else {'A':4,'B':4}
  if task['item_type']=='short_answer':
   application='Explain' if t in {'2','9','12','15','17','19','21','25'} else 'Calculate'
   task['parts']=[dict(command_word='State',marks=1,assessment_objectives=['A']),dict(command_word='State',marks=1,assessment_objectives=['A']),dict(command_word='Explain',marks=2,assessment_objectives=['A']),dict(command_word=application,marks=2,assessment_objectives=['B']),dict(command_word=application,marks=2,assessment_objectives=['B'])]
   task['command_word']='State'
  elif task['item_type']=='practical_task':
   task['command_word']='Draw';task['parts']=[dict(command_word='Draw',marks=5,assessment_objectives=['C']),dict(command_word='Calculate',marks=3,assessment_objectives=['C']),dict(command_word='Plan',marks=8,assessment_objectives=['C'])]
  else:task['command_word']=None
  task['brief']=task['brief']+' Topic-specific binding: '+context+'. Use the stated objective IDs and the original stimulus specification. Introduce every physical relation used; do not reuse exemplar values.'
  if task['item_type']=='practical_task':assert spec['practical_data'] is not None,t
 wo['generated_by']='standard make_work_order.py plus planning/bind_task_specs.py (explicit task bindings; item counts unchanged)';p.write_text(json.dumps(wo,indent=2,ensure_ascii=False)+'\n')
 rows.append(spec)
# Use the standard renderer for the human-readable generated work order too.
import sys
sys.path.insert(0,str(ROOT/'standard/v0.2.0-draft/build'))
from make_work_order import as_markdown
for t in SPEC:
 p=W/f'topics/{t}/work_order.json';p.with_suffix('.md').write_text(as_markdown(json.loads(p.read_text())))
(W/'curriculum/topic-task-specifications.json').write_text(json.dumps(dict(specifications=rows,policy='These bindings decide the physical context, primary objectives and initial data. Authors write original teaching and context-specific rubrics within the source-anchored task structures. Add realistic rounding/scatter only with correct model behaviour and record material deviations.'),indent=2,ensure_ascii=False)+'\n')
print('Bound',len(rows),'topic task specifications without changing slot counts.')
