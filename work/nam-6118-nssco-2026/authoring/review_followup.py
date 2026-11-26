"""Second Claude feedback: remaining small defects and concrete coverage additions."""
import json,re,copy
from pathlib import Path
from figure_repairs import seg
W=Path(__file__).resolve().parents[1]

def calculations():
 out={}
 for line in (W/'authoring/calculation-points.txt').read_text().splitlines():
  if line.strip():
   key,s=line.split(':',1);t,n=key.split('/');out[f'ITEM-6118-{t}-{n}-CALC']=s.strip().split(' | ')
 return out

def apply(A):
 t=int(A.t);prior_supplements=len(A.supplementals)
 def target(n):
  s=next(s for s in A.wo['item_slots'] if int(s['slot'].split('-')[-2])==n)
  return getattr(A,'slot_overrides',{}).get(s['slot'],A.miscons[s['misconception_entry']] if s['subtype']=='MISCON' else A.data[s['objective_id']])
 def note(ob,heading,text):A.extra_blocks.append(('OBJ-6118-'+ob,heading,text))
 def supplement(ob,sub,cw,marks,prompt,answer,guidance):
  idx=len(A.supplementals)+1;iid=f'ITEM-6118-{t}-R{idx:02}-{sub}'
  A.supplementals.append(dict(item_id=iid,objective_id='OBJ-6118-'+ob,subtype=sub,assessment_objectives=['A'] if sub in ['FEATURE','DEF'] else ['A','B'],blooms_level='Remember' if sub in ['FEATURE','DEF'] else 'Understand',command_word=cw,mark_tariff=marks,prompt=prompt,answer=answer,guidance=guidance,item_type='flashcard'))
  note(ob,'Further practice: '+prompt,answer)
 if t==2:
  pr=A.practical
  pr['arrangement']='A 6 V immersion heater rated about 35 W, a suitably rated current-limited 6 V supply and leads, 0.100 kg water in an insulated beaker, thermometer, stirrer and stopwatch'
  pr['method'][0]='Weigh 0.100 kg of water into the insulated beaker and immerse the 6 V, approximately 35 W heater before switching it on.'
  pr['meaning']='The slope is temperature rise per second, 0.08 °C/s. For 0.100 kg of water with c = 4200 J/(kg K), the water gains energy at mc(dT/dt) = 33.6 W. A roughly 35 W heater allows about 1.4 W for losses in this idealised example; voltage alone does not set its power.'
  pr['conclusion']='The temperature-time gradient gives the warming rate. Convert to power only when water mass and specific heat capacity are included and heat losses/container heating are allowed for.'
  note('1.2.2-01' if 'OBJ-6118-1.2.2-01' in A.data else next(iter(A.data)).removeprefix('OBJ-6118-'),'Heater rating and the practice readings',pr['meaning'])
 if t==4:
  pr=A.practical
  pr['method'][3]='For each selected oscillation count, repeat the timing at least three times, retain all raw values and calculate the mean elapsed time.'
  pr['method'][4]='Use several counts at each length, then compare period estimates at new lengths; keep bob mass and small release angle matched.'
  pr['table']='For each pendulum length, record pivot-to-bob-centre length / m, oscillation count, three elapsed-time readings / s and mean elapsed time / s. Use a separate labelled section or length column for each length.'
  pr['stimulus_note']='For this invented practice table, the specified pivot-to-bob-centre pendulum length is 0.49 m. Record the measured length alongside each timing series when repeating the investigation at other lengths.'
  pr['table_caption']='Specified pendulum length for the supplied readings: 0.49 m (pivot to bob centre).'
  pr['legend_outside']=True;pr['readings_marker']='o'
  pr['measurement_credit']='One mark each: time a stated number of full cycles using the same fiducial and direction; repeat each timing at least three times and take a mean; measure new pivot-to-centre lengths and repeat the period comparison.'
 if t==5:
  A.practical['conclusion']='A straight speed-time line of constant gradient shows constant acceleration within the measurement uncertainty. Here that gradient is 0.20 m/s²; a changing gradient would indicate changing acceleration.'
  A.figures['OBJ-6118-2.3.2-08']['ylim']=[-.35,4.5]
 if t==6:
  target(18)['answer']='If the net external force on a system is zero, its total momentum stays unchanged.'
  target(18)['guidance']=['1 mark: unchanged total system momentum with zero resultant external force. Accept constant vector sum of momenta in an isolated system; internal interaction forces may still act.']
  supplement('2.4-01','FEATURE','State',1,'State Newton’s first law, including the force condition.','With zero resultant force, an object stays at rest or continues moving at the same velocity.',['1 mark for both the zero-resultant condition and unchanged velocity/rest. Accept no acceleration when forces balance; do not require zero individual forces.'])
  supplement('2.4-03','FEATURE','State',1,'State what friction opposes between two touching surfaces.','Friction opposes their relative sliding or tendency to slide.',['1 mark: opposes relative motion or impending slip at the contact. Accept grip preventing sliding. Do not credit a claim that friction always opposes the object’s velocity.'])
  note('2.4-03','Friction at a contact','Friction is a contact force opposing relative sliding or the tendency to slide at touching surfaces. Static friction provides grip before slip, while sliding friction resists existing slip. For a shoe on the ground, the ground is the agent and the shoe receives the friction force.')
 if t==8:
  q=A.mc[6];q.update(prompt='A cyclist applies a rim brake. Which interaction directly provides the intended frictional braking torque on the wheel?',correct=('Brake pad rubbing on the wheel rim','The pad’s tangential friction force on the rim produces the braking moment.'),wrong=[('Air resistance on the rider','This retards the bicycle but is not the intended pad-on-wheel braking torque.'),('Normal support from the level road','This support is perpendicular to the road, not the pad’s tangential friction force.'),('Chain tension driving the rear wheel','Driving tension supplies a driving torque rather than the stated brake interaction.')])
  q=A.mc[3];q['wrong']=[(s,r.replace('A couple can still turn the body.','Equal opposite forces along separate lines can still turn the body.').replace('couple','separated force pair')) for s,r in q['wrong']]
 if t==10:
  note('2.10.3-01','Energy forms and transfers','Useful school descriptions include kinetic (motion), gravitational potential (height), strain/elastic potential (deformation), chemical (fuels and batteries), nuclear and internal/thermal energy stores. Energy is transferred electrically, by heating, by mechanical work, or by radiation such as light. Sound also carries energy through matter. A falling ball changes gravitational potential energy into kinetic energy; a lamp transfers electrical input into light and internal energy. The complete energy balance includes the surroundings.')
  supplement('2.10.3-01','FEATURE','State',2,'State any two energy forms or stores and give one example of each.','Examples include kinetic energy of a moving trolley, gravitational potential energy of raised water, strain energy of a stretched spring, chemical energy in fuel, nuclear energy in a fuel nucleus and internal energy in warm water.',['Any two distinct correct form–example pairs, 1 mark each. Accept elastic for strain, thermal for internal, light/radiant energy from a lamp, sound energy from a vibrating source, or electrical energy in an appropriate transfer example. No second mark for two examples of the same form.'])
  note('2.10.4-05','Named levers, gears and pulleys','A crowbar pivots against a support: a long effort arm can lift a load with a smaller force. Scissors are paired levers with the screw as fulcrum. A bicycle’s chain connects toothed gears; a small driving gear turning a larger driven gear gives lower output speed and greater turning effect in an ideal model. A crane can use a movable pulley supported by two rope sections: half the ideal load force is traded for twice the pulled-rope distance. A single fixed flagpole pulley mainly changes the effort direction. Real friction increases the input work; an ideal machine conserves work.')
  supplement('2.10.4-05-M01','MECH','Explain',2,'Explain how a crowbar can lift a load with a smaller effort.','The support is its fulcrum and the effort acts farther from it than the load. The longer perpendicular effort arm gives the needed turning moment with less force, while the effort travels farther.',['1 mark for identifying a longer effort arm relative to the load arm.','1 mark for the resulting smaller force at equal moment, with greater effort travel. Accept another named lever with the same correctly located pivot, load and effort.'])
  supplement('2.10.4-05-M02','FEATURE','State',1,'State one named use of gears.','Bicycle gears change the relationship between pedalling speed and wheel turning effect.',['Any one named use for 1 mark: bicycle gearing, car gearbox, clock or hand drill, with a relevant transmission/speed/turning-effect role. A machine name without any gear function is insufficient.'])
  supplement('2.10.4-05-M03','MECH','Explain',2,'Explain how a crane’s ideal two-section movable pulley reduces the lifting effort.','Two rope sections support the load, each carrying the same tension. The effort is half the load force, while twice the rope length must be pulled for a given rise.',['1 mark for two supporting tensions sharing the load.','1 mark for effort half the load with twice the rope travel. Accept a correctly labelled equivalent pulley diagram; do not apply this force reduction to one fixed pulley.'])
 if t==12:
  # Same concepts, similar-length alternatives: no systematic shortest-answer cue.
  changes={1:('A gas sample','A solid sample','A liquid sample','All equally compressible'),2:('Vibrate near fixed positions','Remain still until melting','Move freely throughout the solid','Travel only along its surface'),3:('Mean molecular kinetic energy','Mean molecular physical size','Total molecules in sealed gas','Total gas mass without added gas'),4:('Random motion of particles','Coherent flow of the liquid','Growth of individual particles','Gravity-directed horizontal motion'),5:('Energy changes particle arrangement','Energy supply falls to zero','Mean kinetic energy rises steadily','All molecular motion stops'),6:('Larger suspended tracer particles','Individual surrounding molecules','Smoothly drifting bulk liquid','Motion of the microscope stage'),7:('Molecular impacts on the walls','Weight acting only on the base','Particle size without any motion','Attraction to the container base')}
  for n,opts in changes.items():
   q=A.mc[n-1];q['correct']=(opts[0],q['correct'][1]);q['wrong']=[(s,q['wrong'][k][1]) for k,s in enumerate(opts[1:])]
  A.mc[0]['correct']=('A contained gas','Its widely separated particles allow large volume changes without changing particle size.')
  A.mc[0]['wrong']=[('A solid block','Close particles in a solid leave little compressible space.'),('A liquid sample','Liquids have much less compressible space than a gas.'),('Each phase equally','Particle separation makes gases substantially more compressible.')]
  A.mc[7].update(correct=('Pressure rises as particles speed up','At fixed volume, increased mean kinetic energy increases wall momentum transfer.'),wrong=[('Pressure falls as particles slow down','Heating raises rather than lowers the mean molecular kinetic energy.'),('Pressure stays fixed as particles enlarge','Particles do not expand to absorb the temperature rise; their motion becomes more energetic.'),('Pressure falls as the volume expands','The stated rigid vessel has fixed volume.')])
  A.mc[8].update(correct=('Volume rises; gas density falls','The piston moves outward at fixed external pressure; unchanged mass occupies more volume.'),wrong=[('Volume falls; gas density rises','Warming at the given fixed pressure moves the piston outward, not inward.'),('Volume stays fixed; density falls','Unchanged mass at fixed volume could not have falling density.'),('Volume rises; gas density rises','At fixed mass, increasing volume reduces density.')])
  A.mc[9].update(correct=('Pressure increases','At fixed temperature the smaller volume gives more frequent wall impacts.'),wrong=[('Pressure decreases','A smaller volume gives greater rather than lower wall impact rate.'),('Pressure unchanged','Constant temperature does not imply constant pressure when volume changes.'),('Particles grow','Compression reduces particle spacing, not individual particle size.')])
  A.mc[11].update(correct=('Water vapour from air condenses','Vapour cools at the surface and changes to liquid.'),wrong=[('Liquid leaks through glass','The glass is stated to be intact; surface condensation does not require leakage.'),('The glass surface melts','The cold wall is not a layer of frozen water that melts.'),('The glass itself evaporates','Evaporation would remove material, not form the observed liquid-water droplets.')])
 if t==13:
  for v in A.data.values():
   for k in ['core','detail','teach']:
    v[k]=re.sub(r'[^.!?]*\bresolution\b[^.!?]*[.!?]?', '',v[k],flags=re.I).strip()
  A.data['OBJ-6118-3.2.1-04-M01']['detail']='For a given bulb and liquid, a narrower capillary gives more column movement per degree but a smaller temperature span on a fixed stem.'
 if t==15:
  q=A.mc[1];q['prompt']='Compared with an ordinary nonmetal, which additional mobile particles help transfer thermal energy through a metal?'
  q['wrong']=[('Ions flowing through the metal','Metal ions mainly vibrate near fixed positions; they do not flow through the solid.'),('Neutrons migrating between nuclei','Neutrons are bound within nuclei and are not the mobile thermal carriers here.'),('Whole atoms flowing from hot to cold','Bulk material flow is not ordinary conduction through the solid.')]
  A.mc[2].update(prompt='Which sample can sustain ordinary bulk convection within it?',correct=('Liquid water','Its material can circulate, carrying thermal energy.'),wrong=[('A rigid copper block','A solid block does not circulate bodily inside itself.'),('A solid rubber block','Solid material cannot form the ordinary circulating fluid current.'),('An evacuated vessel','A vacuum has no fluid to circulate.')])
  pr=A.practical;data=copy.deepcopy(next(s for s in json.loads((W/'curriculum/topic-task-specifications.json').read_text())['specifications'] if s['topic_id']==A.t)['practical_data']);data['y_heading']='Black-can temperature / °C';pr['data']=data
  pr['plot_y_heading']='Temperature / °C';pr['plot_label']='Black can';pr['comparison_data']=dict(label='Shiny can',y_heading='Shiny-can temperature / °C',rows=[[0,78],[20,77],[40,76],[60,75],[80,74],[100,73]])
  pr['arrangement']='Two light metal cans of the same dimensions with black and shiny finishes, each holding 0.025 kg of water, matching lids with thermometer/stirrer holes, a balance, thermometers and stopwatch'
  pr['method'][0]='Weigh 0.025 kg of water into each light can and bring both to the same initial temperature; record room temperature.'
  pr['method'][3]='Stir gently through each lid hole and record both labelled temperatures every 20 s for 100 s, using thermometers at matched depth.'
  pr['measurement_credit']='One mark each: match and record 0.025 kg water mass and starting temperature in both cans; read both labelled temperatures at common timed intervals; repeat at least three runs, exchange can positions and take mean temperatures at each time.'
  pr['table']='Time / s, black-can temperature / °C and shiny-can temperature / °C, with separate repeats and mean columns for each can.'
  pr['graph']='Time / s is horizontal and Temperature / °C vertical. Plot and label both cans separately; use a separate straight fit over this short supplied interval and show the black-can gradient triangle.'
  pr['meaning']='The black-can slope is (70 − 78)/(100 − 0) = −0.08 °C/s. The shiny-can slope is (73 − 78)/(100 − 0) = −0.05 °C/s. The black can has the steeper negative gradient and cools faster under the matched conditions.'
  pr['conclusion']='The black can has the steeper negative gradient (−0.08 rather than −0.05 °C/s), showing faster cooling in the matched short-interval comparison. Do not infer a surface effect unless water mass, can dimensions, lids and starting/room temperatures were matched.'
  note('3.3.3-03-M01','Small-sample cooling example','The two-can table is an invented short-interval example for matched light cans containing 0.025 kg water each. The water alone releases thermal energy at about 0.025×4200×0.08 = 8.4 W for the black-can slope; the can also cools. It does not imply a 67 W water-energy loss from a 0.20 kg sample. A real cooling curve usually changes slope as the water approaches room temperature.')
 if t==18:
  note('4.3.3-15','Eye and camera parts compared','The eye’s iris changes pupil size and so controls the amount of light entering. A camera’s adjustable aperture/diaphragm performs the corresponding function. The retina is the eye’s light-sensitive receiving surface; film or an electronic sensor is the camera equivalent. Both receive a real inverted image. A camera shutter controls exposure duration, whereas the iris chiefly changes the opening. Focusing is separate: a simple camera changes lens-to-film/sensor distance; the eye changes lens shape and power while the retina stays nearly fixed.')
  supplement('4.3.3-15','DIST','Explain',2,'Explain the corresponding functions of iris/aperture and retina/film in an eye and camera.','The iris varies the pupil opening as a camera aperture controls the light entering. The retina receives the eye’s image as film or a sensor receives the camera’s real inverted image.',['1 mark for iris/pupil opening compared with adjustable aperture as a light-admission control. Accept diaphragm as the camera part.','1 mark for retina compared with film or sensor as the image-receiving light-sensitive surface. Do not credit the lens as the receiving surface.'])
 if t==19:
  A.mc[2]['wrong'][2]=('Low-frequency broadcast radio','This option is outside the microwave frequency band named for the satellite-link example.')
 if t==20:
  d=A.data['OBJ-6118-4.4-07'];d['core']='Sound is a mechanical wave that needs matter to carry its disturbance.';d['detail']='Solids, liquids and gases can transmit sound; an ideal vacuum has no material particles to pass on the vibration.';d['teach']+=' In a solid the interactions between neighbouring particles transmit vibration; liquid and gas particles also pass on sound disturbances. A vacuum does not provide this medium.'
 if t==21:
  A.mc[7]['prompt']='An initially neutral material gains electrons and no other charge is transferred. What is its resulting net charge?'
  A.mc[10].update(prompt='An initially neutral conductor on an insulating stand is earthed while a negative rod is held nearby. Which sequence leaves the conductor positively charged?',correct=('Disconnect Earth, then remove the rod','The rod is still repelling electrons when the earth path is removed, so an electron deficit remains.'),wrong=[('Remove the rod, then disconnect Earth','Electrons can return through the earth path before it is removed.'),('Remove the rod and keep Earth connected','The remaining earth path permits neutralisation.'),('Disconnect Earth before bringing the rod nearby','Without an earth path while the rod is present, electrons cannot leave to create the intended net positive charge.')])
  target(8).update(prompt='State how illumination creates the charge pattern on a photocopier drum.',answer='Light discharges the exposed regions of the charged drum; unlit image regions retain charge and attract toner.',guidance=['1 mark for light discharging the exposed drum regions so the unlit image retains charge. Accept illuminated areas lose their charge. Toner attraction without the light-discharge stage is insufficient for this prompt.'])
 if t==24:
  A.mc[11]['prompt']='A 440 W training appliance operates at 220 V. For this steady-load exercise choose the smallest listed fuse rating above its normal current: 1 A, 3 A, 10 A or 13 A.'
  A.mc[11]['correct']=('3 A','Normal current is 440/220 = 2 A; 3 A is the smallest listed rating above 2 A.')
 if t==25:
  A.practical['stimulus_note']='The supplied lifting-force values are uncorrected readings. The 0.1 N intercept may include a force-gauge zero offset; record the offset before applying a correction.'
  A.practical['data']=copy.deepcopy(next(s for s in json.loads((W/'curriculum/topic-task-specifications.json').read_text())['specifications'] if s['topic_id']==A.t)['practical_data'])
  A.practical['data']['y_heading']='Uncorrected lifting force / N'
 if t==26:
  d=A.data['OBJ-6118-5.7.2.3-06'];d.update(core='An AC generation-to-consumer pathway uses transformers at transmission and distribution stages.',detail='A step-up transformer raises voltage for transmission, while step-down transformers provide lower distribution and consumer voltages.',teach='An AC generator feeds a step-up transformer before long-distance lines. Higher transmission voltage permits lower current for the same power, reducing line heating. Step-down transformers later supply the lower voltages needed by consumers.',prompt='Describe the roles of transformers between an AC generator and consumers.',answer='A step-up transformer raises voltage before long-distance transmission; step-down transformers lower it for distribution and consumers.',guidance=['1 mark for both correctly placed roles: step-up before transmission and step-down before consumers. Accept a labelled generator → step-up → lines → step-down → consumer sequence.'])
  target(14)['guidance']=['1 mark: higher voltage at fixed transmitted power means lower current and therefore less heating loss in the same wires. Accept a linked lower-current/lower-wire-heating explanation.']
 if t==28:
  A.mc[9]['wrong'][2]=('Toward whichever plate is closer regardless of charge','Distance to a plate does not set the force direction: beta-minus has negative charge and is attracted toward the upper positive plate.')
 if t==23:
  A.geometry('5.3-01-M06',[seg([[-4,0],[-2,0]],'black'),seg([[-3.7,-.3],[-2.3,-.3],[-2.3,.3],[-3.7,.3],[-3.7,-.3]],'black'),seg([[-.3,-.4],[.3,-.4],[.3,.4],[-.3,.4],[-.3,-.4]],'black'),seg([[0,.4],[0,1.2]],'black'),seg([[0,-.4],[0,-1.2]],'black'),seg([[.7,.5],[1.4,.5]],'black'),seg([[1.4,.5],[2.25,1]],'black'),seg([[2.4,.5],[3.1,.5]],'black'),seg([[.3,.1],[1.8,.1],[1.8,.72]],'grey',style='--')],circles=[dict(centre=[1.4,.5],radius=.05,color='black'),dict(centre=[2.4,.5],radius=.05,color='black')],labels=[[-3.5,-.8,'Fuse'],[.4,-.65,'Relay coil'],[1.0,1.5,'Separate open switch'],[-.6,1.45,'Coil lead'],[-.6,-1.6,'Coil lead']],title='Fuse and relay: rectangular coil, vertical leads, separate switch')
 if t==14:
  A.figures['OBJ-6118-3.2.3-04']['annotations']=[dict(xy=[.5,-5],xytext=[20,-12],text='Ice warming',textcoords='data',arrowprops=dict(arrowstyle='->',lw=.8)),dict(xy=[27,50],xytext=[58,40],text='Liquid warming',textcoords='data',arrowprops=dict(arrowstyle='->',lw=.8)),[9,0,'Melting'],[95,100,'Boiling']]
 # Every calculation has its own written criteria; no canonical-answer sentence template.
 credit=calculations()
 for s in A.wo['item_slots']:
  if s['subtype']=='CALC':
   d=target(int(s['slot'].split('-')[-2]));assert s['slot'] in credit;d['guidance']=credit[s['slot']]
 for s in A.supplementals:
  if s['subtype']=='CALC':assert s['item_id'] in credit;s['guidance']=credit[s['item_id']]
 # Explicit, task-specific accepted vocabulary. These do not relax any required condition.
 alternatives=[('perpendicular','at right angles'),('elapsed time','duration'),('independent variable','deliberately changed input'),('dependent variable','measured response'),('mean','arithmetic average'),('magnitude','size'),('net external force','resultant external force'),('resultant force','net force'),('temperature rise','temperature increase'),('nucleon number','mass number'),('proton number','atomic number'),('beta-minus','β⁻'),('alpha','α'),('gamma','γ'),('repulsion','pushing apart'),('repel','push apart'),('attract','pull together'),('fulcrum','pivot'),('turning effect','moment'),('moment','turning moment'),('kinetic energy','energy of motion'),('strain energy','elastic potential energy'),('gravitational potential','energy associated with height in a gravitational field'),('density','mass per unit volume'),('inertia','resistance to a velocity change'),('displacement','directed start-to-finish separation'),('frequency','complete cycles per second'),('period','time per complete cycle'),('amplitude','maximum displacement from equilibrium'),('wavelength','distance between adjacent in-phase points'),('wavefront','line of equal phase'),('conduction','thermal transfer through matter without bulk flow'),('convection','thermal transfer by bulk fluid circulation'),('vacuum','region with no material particles'),('virtual','located by backward ray extensions rather than actual ray convergence'),('refraction','changed light speed on transmission between media'),('potential difference','voltage'),('e.m.f.','source energy supplied to each coulomb'),('parallel','side-by-side lines in the same direction'),('neutral','zero net charge'),('transverse','oscillation perpendicular to propagation'),('longitudinal','oscillation parallel to propagation'),('half-life','average time for the undecayed population to halve'),('spontaneous','not triggered by an external event'),('ionisation','removal of electrons to form ions'),('ionise','remove electrons to form ions'),('torque','turning moment'),('commutator','split-ring current reverser'),('slip rings','separate continuous ring contacts'),('fission','splitting of a heavy nucleus'),('chemical energy','energy stored in chemical bonds'),('radiant','carried by electromagnetic waves'),('hotter','at higher temperature'),('less dense','lower mass per unit volume'),('gradient','slope'),('horizontal','x-axis'),('vertical','y-axis')]
 for s in A.wo['item_slots']:
  if s['subtype']=='CALC':continue
  d=target(int(s['slot'].split('-')[-2]));text=' '.join(d['guidance'][:s['mark_tariff']]).lower();terms=[]
  for old,new in alternatives:
   if old in ['horizontal','vertical'] and not re.search(r'\b(?:axes|graph|horizontal axis|vertical axis)\b',text):continue
   if old=='parallel' and not re.search(r'\b(?:lines|rays|wavefronts|fronts)\b',text):continue
   if re.search(r'(?<!\w)'+re.escape(old)+r'(?!\w)',text):terms.append(f'“{new}” for “{old}”')
   if len(terms)==2:break
  if terms:d['guidance'].append('Accepted alternative wording: '+('; '.join(terms))+'. The stated directions, quantities and conditions are still required.')
 explicit={}
 for line in (W/'authoring/accepted-alternatives.txt').read_text().splitlines():
  key,text=line.split(':',1);explicit[key]=text.strip()
 for s in A.wo['item_slots']:
  key=f"{t}/{s['slot'].split('-')[-2]}"
  if key in explicit:target(int(s['slot'].split('-')[-2]))['guidance'].append(explicit[key])
 for s in A.supplementals:
  key=f"{t}/{s['item_id'].split('-')[-2]}"
  if key in explicit:s['guidance'].append(explicit[key])

 if len(A.supplementals)>prior_supplements:
  A.deviations.append(dict(from_='First repair had no separate assessment slots for the follow-up coverage findings',to=f'{len(A.supplementals)-prior_supplements} additional labelled coverage cards; all first-repair item IDs retained.',why='Lotto requested the second feedback be implemented before the Step 6 verdict. Derived contract counts follow the added cards; curriculum and work-order files remain unchanged.'))
