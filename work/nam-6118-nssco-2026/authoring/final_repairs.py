"""Task/rubric alignment and source-scope clean-up after the first regeneration."""
import re

def apply(A):
 t=int(A.t)
 def item(n):
  s=next(s for s in A.wo['item_slots'] if int(s['slot'].split('-')[-2])==n)
  return getattr(A,'slot_overrides',{}).get(s['slot'],A.miscons[s['misconception_entry']] if s['subtype']=='MISCON' else A.data[s['objective_id']])
 if A.practical:
  A.practical['aim']=A.practical['aim'].replace('investigate how','measure how').replace('investigate','test')
  A.practical['arrangement']=A.practical['arrangement'].replace('projected wave image','projected wave pattern')
  A.practical['method']=[s.replace('projected wave image','projected wave pattern') for s in A.practical['method']]
 if t==5:
  item(4)['answer']='Displacement is a vector from the initial to the final position. Its magnitude is their straight-line separation and its direction is from start to finish.'
  item(4)['guidance']=['1 mark: straight-line separation from initial to final position AND the direction from initial to final; accept final position vector minus initial position vector. Total path length is not displacement.']
  A.structured[2]['answer']='The distance-time line has zero gradient and hence zero speed. A horizontal nonzero speed-time line directly states steady motion.'
  A.structured[4]['guidance']='One mark for distance = average speed × duration, equivalent constant-acceleration displacement equation, or trapezium area; one for 12 m with unit. Retain method credit after arithmetic error.'
 if t==6:item(2)['answer']='It can decrease speed or change the direction of motion; either is a change in velocity.'
 if t==9:A.data['OBJ-6118-2.10.2-02-M01']['detail']='An electrical load receives the cell output; a battery can store part of the daytime energy for later use.'
 if t==13:
  item(8).update(prompt='Explain how a narrower capillary changes sensitivity and usable range when liquid amount, bulb and stem length are unchanged.',answer='The same liquid expansion produces a larger column rise per degree, so sensitivity increases.~The fixed stem accommodates a smaller temperature interval, reducing range.',guidance=['1 mark: greater length change per temperature degree at unchanged bulb/liquid.','1 mark: less temperature interval fits the same stem length; both compared under the stated conditions.'])
 if t==14:
  item(7).update(prompt='Describe the calculation step after measuring block mass m, absorbed energy Q and temperature rise ΔT.',answer='The calculated specific heat capacity is c = Q/(mΔT).',guidance=['1 mark for Q divided by the product of mass and temperature rise; accept an algebraically equivalent equation with compatible units. No extra measurement sequence is needed for this calculation-step card.'])
  item(8).update(prompt='Describe which energy quantity must be matched when comparing temperature rises for different masses of the same material.',answer='Each mass must absorb the same thermal energy, with other conditions matched.',guidance=['1 mark for equal absorbed thermal energy; equal heater times alone require matched power and accounted losses.'])
  A.structured[0]['guidance']='One mark for J/(kg K), J/(kg °C), J kg⁻¹ K⁻¹ or J kg⁻¹ °C⁻¹; equivalent energy/mass/temperature-interval units accepted.'
 if t==16:
  for v in A.data.values():
   for k in ['core','detail','teach']:v[k]=v[k].replace('wave image','wave pattern')
 if t==21:
  item(2)['answer']='A dry polythene rod rubbed with wool attracts small paper pieces or deflects an electroscope; electron transfer produces the charge.'
  item(13)['answer']='Copper has mobile electrons that carry charge through the metal.~In dry plastic or glass the electrons remain bound, so charge does not flow freely through the material.'
  item(18)['answer']='A negative rod near a conductor on an insulating stand repels electrons to its far side. Earthing lets those electrons leave.~Removing Earth first and then the rod leaves an electron deficit and positive conductor.'
  A.data['OBJ-6118-5.1-06']['teach']+=' Collisions between ice and water particles in a storm cloud separate charge, producing a large potential difference between charged regions or ground. A sufficiently strong field ionises air and opens a conducting discharge path.'
 if t==23:
  item(10).update(prompt='Describe the calculation step using paired voltmeter V and ammeter I readings for a conductor.',answer='Resistance is calculated as R = V/I using voltage across and current through the conductor.',guidance=['1 mark for calculation action V/I with quantities for the same conductor and reading; accept correctly rearranged V=IR. The full apparatus plan is assessed separately in the practical task.'])
  # Actual connection junctions and polarity belong to this circuit, not to a decorative caption.
  p=A.figures['OBJ-6118-5.3-01'];p['circles'] += [dict(centre=[.2,2],radius=.045,color='black'),dict(centre=[1.8,2],radius=.045,color='black')];p['labels'] += [[-.65,.6,'+'],[.15,.6,'−']]
 if t==26:
  for v in A.data.values():
   for k in ['core','detail','teach']:
    v[k]=v[k].replace('The familiar line-loss relation varies with the square of current.','At fixed wire resistance, lower current reduces the energy lost as wire heating.').replace('magnetic linkage','magnetic field through the coil')
 if t==27:
  d=A.data['OBJ-6118-6.1.1-06-M02'] if 'OBJ-6118-6.1.1-06-M02' in A.data else None
  for ob,v in A.data.items():
   if not v['core']:v['core']='Beta-minus decay leaves the nucleon number unchanged and increases the daughter proton number by one.'
   if not v['detail']:v['detail']='The emitted electron balances the daughter’s increase in nuclear charge in the school decay equation.'
 if t==28:
  item(1)['prompt']='Describe one exposure-reduction action for an authorised supervised radioactive-source demonstration.'
  A.supplementals[0]['guidance'][-1]='Graph/conclusion (1): approximately half survive each round with random fluctuations; the graph gives a model half-life of about one round. Accept dice with the correct survival fraction and a fitted model half-life.'
 # Wrong answers are explicitly fallible alternatives, and their errors need no unqualified universal slogans.
 replacements={'in every case':'for that interaction','only from gravity':'from gravity','only through surrounding air':'through surrounding air instead of the core','guarantees a fuse trips before any shock':'makes a fuse trip before a shock','only by weighing the pipe':'by weighing the pipe','in every terrain':'for a typical route','each second regardless of motion':'every second without a changing field'}
 for q in A.mc:
  for k,v in replacements.items():
   q['prompt']=q['prompt'].replace(k,v)
   q['wrong']=[(x.replace(k,v),r.replace(k,v)) for x,r in q['wrong']]
 # Remove remaining off-scope terminology in performance feedback as well as the cards.
 for p in A.structured:
  p['answer']=p['answer'].replace('More dipoles or domains align','More atomic magnetic effects align')
 for q in A.mc:
  q['correct']=tuple(s.replace('conductance','ease of current flow') for s in q['correct'])
  q['wrong']=[tuple(s.replace('conductance','ease of current flow') for s in v) for v in q['wrong']]
 if t==2:
  item(3)['answer']='A suitable thermometer has a range covering the water temperature, with its bulb immersed in the water.'
  item(9)['answer']='The aim is to measure how heating duration affects water temperature at fixed heater power and water mass.'
 if t==4:item(13)['answer']='The controlled comparison uses different pivot-to-bob-centre lengths, with repeated period measurements at each while bob mass and small release angle stay matched.'
 if t==22:
  item(2)['answer']='The ammeter is in series in the lamp branch, with a suitable range and polarity.'
  item(12)['answer']='The voltmeter spans the lamp terminals in parallel, with suitable range and polarity.'
 if t==14:A.data['OBJ-6118-3.2.3-04']['teach']='The schematic curve starts with ice warming to 0 °C, pauses for melting, rises while liquid warms to 100 °C, then has a longer boiling plateau. The time scale is qualitative; actual durations depend on mass, heater power and energy losses. In a constant-power illustration, a much longer boiling plateau than melting plateau is physically appropriate for water.'
 if t==23:
  A.figures['OBJ-6118-5.3-01-M02']['circles'] += [dict(centre=[-3.5,0],radius=.055,color='black'),dict(centre=[-2.5,0],radius=.055,color='black')]
 if t==9:
  A.mc[6]['wrong']=[('Combustion ash from burning coal','Coal ash is a combustion issue, not the particular fission-product problem.'),('Flooding a reservoir valley','Reservoir flooding is associated with hydroelectric construction.'),('Wind-turbine blade noise','This is a wind-installation issue rather than the named fission-product difficulty.')]
