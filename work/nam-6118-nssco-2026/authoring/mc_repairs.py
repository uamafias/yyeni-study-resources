from card_repairs import records

def apply(A):
 t=int(A.t)
 for n,text in records('mc-repairs.txt').get(t,{}).items():
  wrong=[]
  for chunk in text.split('; '):
   option,reason=chunk.split('|',1);wrong.append((option,reason[0].upper()+reason[1:]+'.'))
  assert len(wrong)==3,(t,n,wrong);A.mc[n-1]['wrong']=wrong
 def wrong(n,k,text,why):A.mc[n-1]['wrong'][k]=(text,why)
 def correct(n,text,why):A.mc[n-1]['correct']=(text,why)
 if t==4:A.mc[0]['prompt']='Which vessel gives a range of contained liquid-volume readings from graduations along its cylindrical open body?'
 if t==5:A.mc[6]['prompt']='When can v = u + at and s = ut + ½at² describe a straight-line journey?';correct(7,'When acceleration is constant','Both equations assume acceleration remains unchanged during the interval.')
 if t==7:
  A.mc[5]['prompt']='Which defect makes the displacement volume of a fully submerged solid too large?'
  A.mc[5]['wrong']=[('Reading initial level too high','This subtracts too much and underestimates the displacement.'),('Failing to immerse the object fully','This displaces too little liquid.'),('Losing liquid while lowering the object','This reduces the final level, underestimating displacement.')]
 if t==8:
  A.mc[1]['prompt']='Which quantity has magnitude but no direction?'
  wrong(7,0,'Reducing heating in a lubricated bearing','This calls for reduced friction, unlike braking.')
 if t==9:
  A.mc[4].update(prompt='Which energy change occurs in an illuminated photovoltaic cell?',correct=('Radiant energy to electrical energy','The cell converts incident light directly into electrical output.'),wrong=[('Radiant energy directly to water flow','A pump needs an electrical/mechanical pathway.'),('Thermal energy to nuclear energy','A photovoltaic cell does not produce nuclear fuel.'),('Electrical energy to sunlight','This reverses the operating energy pathway.')])
  wrong(7,0,'Nuclear fuel releasing CO₂ through burning','Fission is a nuclear process rather than fuel combustion.')
 if t==12:wrong(7,0,'Gas weight acting only on the floor','Molecular impacts create pressure on walls in every orientation.')
 if t==14:
  wrong(5,0,'Mean particle speed must rise throughout melting','Constant temperature means unchanged mean kinetic energy during the ideal plateau.')
  wrong(7,0,'Whole-container rotational kinetic energy','Bulk motion of the object is excluded from internal energy.')
 if t==18:wrong(7,0,'An object just outside the focal point','Its screen image is much farther than f, so lens-screen distance does not approximate focal length.')
 if t==20:
  A.mc[6]['prompt']='Which observation specifically demonstrates a bat’s echolocation?'
  correct(7,'An obstacle is located using delayed returning ultrasound','The outgoing sound reflects and its delay/direction reveal the obstacle.')
  wrong(7,0,'Prey is detected from heat radiation alone','Thermal sensing is not sound-echo detection.')
 if t==21:
  A.mc[0].update(prompt='A rod loses electrons while rubbed with a cloth. Which pair describes their net charges?',correct=('Rod positive, cloth negative','Electrons moved from rod to cloth, leaving equal opposite net charges.'),wrong=[('Both positive','Transfer leaves one electron deficit and one excess.'),('Rod negative, cloth positive','This reverses the stated electron-transfer direction.'),('Both neutral','Electron transfer changes the net balance on each object.')])
  correct(7,'Yes, by redistribution','Electrons shift so leaf and stem acquire like charge and repel, while total electroscope charge may remain zero.')
  A.mc[10]['prompt']='During charging by induction with a negative rod kept nearby, which connection is removed first to leave the insulated conductor positive?'
  correct(11,'Earth connection first','Removing earth while the rod remains prevents replacement electrons entering; the rod is removed afterwards.')
 if t==22:
  correct(4,'Periodic direction reversal','Alternating current repeatedly reverses direction; variation in magnitude alone is insufficient.')
  A.mc[10]['prompt']='Three identical 1.2 V cells are connected in series with each positive terminal joined to the next negative terminal. What voltage is measured with no external load?'
 if t==23:
  A.mc[1]['prompt']='Under what condition is current proportional to voltage for an ohmic metal conductor?'
  A.mc[4]['prompt']='Why does a filament lamp’s current cease to be proportional to voltage as the voltage is increased?'
 if t==24:
  A.mc[5]['prompt']='In the IEC-colour classroom plug model, which colour identifies protective earth?'
  A.mc[11]['prompt']='A 440 W training appliance operates at 220 V. Which fuse is suitable in the simple steady-current exercise: 1 A, 3 A, 13 A or 30 A?'
 if t==28:
  A.mc[4]['prompt']='Which statement correctly describes the decay time of one unstable nucleus?'
  correct(5,'It cannot be predicted exactly','Population probabilities are predictable but the individual nucleus has no scheduled decay time.')
  wrong(7,0,'Move closer to the source','Closer proximity increases exposure under the same other conditions.')
 # Wording used in later questions must stay clear of authoring jargon.
 for q in A.mc:
  q['prompt']=q['prompt'].replace('normal angle','angle to the normal').replace('voltage sweep','range of applied voltages')
 # Remaining reviewer-named alternatives in the application questions.
 def replacements(n,triples):
  assert len(triples)==3;A.mc[n-1]['wrong']=triples
 if t==5:wrong(11,2,'10 m','This adds an unjustified half factor to a rectangle representing steady speed.')
 if t==8:
  replacements(10,[('Force × distance along the beam','Only the perpendicular distance to the force line belongs in a moment.'),('Force × distance to the nearest end','The specified pivot, not an arbitrary end, sets the arm.'),('Equal clockwise and anticlockwise nonzero moments from this one force','The one force has zero moment when its line passes through the pivot.')])
  wrong(11,1,'10 N','This exceeds the 3+5 N downward total and would give an upward resultant.')
  wrong(12,2,'Its gravitational energy increase','The stationary lever has no height change during the hold.')
 if t==9:
  A.mc[8].update(prompt='A hydroelectric installation keeps the same water fall height and efficiency while water mass flow per second halves. What happens to its output power?',correct=('It halves','Each kilogram releases the same mgh, but half as many kilograms pass per second.'),wrong=[('It doubles','Reduced mass flow reduces input energy rate.'),('It is unchanged','Same energy per kilogram does not mean same energy per second.'),('It falls to one quarter','Only one factor has halved, not two.')])
  replacements(11,[('Its whole life cycle has no emissions','Construction, transport and maintenance may have emissions.'),('Its output stays constant','Changing wind changes power availability.'),('Its operation never changes habitat','Land use, noise and wildlife effects still need consideration.')])
 if t==12:
  replacements(8,[('Pressure stays constant because mean speed stays constant','Heating increases mean random speed/energy.'),('Pressure falls because impacts become less frequent','At fixed volume faster particles increase momentum-transfer rate.'),('Pressure stays constant because molecular size stays constant','Pressure depends on impacts, not on particle size alone.')])
  wrong(9,2,'Density rises at fixed mass','Outward piston movement increases volume and lowers density.')
  replacements(12,[('Water that diffused through intact glass','Surface water can come from humid air without crossing the glass.'),('Liquid formed by melting the glass surface','The glass is not a frozen water layer.'),('Liquid evaporated out of the colder glass wall','Cooling vapour causes condensation rather than wall evaporation.')])
 if t==13:
  replacements(4,[('Any graph passing through the origin','Origin passage alone does not guarantee constant slope.'),('A smooth changing-slope curve','Sensitivity varies on a curve.'),('A straight vertical line','One property reading cannot represent many distinct temperatures in this calibration.')])
  replacements(7,[('Mercury is highly flammable at room temperature','Its toxicity, not flammability, is the main handling issue here.'),('Mercury expands too much to have a temperature scale','Expansion is the measuring property.'),('Mercury cannot wet any container','This does not account for its toxic spill risk.')])
  wrong(9,2,'16 K','The Celsius and kelvin degree intervals have equal size, so no factor two is applied.')
 if t==14:
  replacements(12,[('No thermal energy is absorbed','Latent energy can enter at constant temperature.'),('Mean particle kinetic energy rises steadily','Mean kinetic energy tracks the constant temperature.'),('The sample stays in a single phase throughout','A phase-change plateau contains changing phase proportions.')])
 if t==17:
  wrong(9,2,'110°','This is 180−70, the obtuse supplement rather than the incidence angle between ray and normal.')
 if t==18:
  wrong(10,2,'115°','This adds 90+25 rather than taking the acute complement 90−25.')
  replacements(12,[('Refraction along the boundary','Grazing refraction is at the critical angle, not above it.'),('Refraction away from normal into air','Above critical angle there is no transmitted refracted ray in this ideal model.'),('Partial reflection with unchanged transmitted direction','Above critical incidence the ideal reflected fraction is total.')])
 if t==20:
  wrong(8,2,'51 m','This counts three one-way legs instead of the outward and return pair.')
  replacements(11,[('Same amplitude and same frequency','The trace height doubled, so amplitude did not stay fixed.'),('Greater amplitude and greater frequency','The unchanged period means unchanged frequency.'),('Greater amplitude and lower frequency','The unchanged period means unchanged frequency.')])
  replacements(12,[('It decreases','Greater path length takes more time at the same speed.'),('It stays the same','The reflection path becomes longer.'),('It depends only on sound frequency','For the stated fixed-speed path, delay is path length divided by speed.')])
 if t==21:
  replacements(8,[('Positive','Gaining negative electrons makes net charge more negative.'),('Neutral regardless of the gain','A net added electron imbalance changes charge.'),('It depends only on the rod mass','Charge balance depends on electrons and protons, not mass alone.')])
  wrong(10,2,'Upward','Electric force is along or opposite the field, not at right angles to it.')
  replacements(11,[('Remove the rod first','While earth remains, replacement electrons can return.'),('Keep Earth connected after removing the rod','This permits neutralisation through Earth.'),('Disconnect the insulating stand first','The stand is not the charge-flow connection.')])
  replacements(12,[('At a plate edge','Field lines curve near edges.'),('Far outside the plates','The simple uniform central pattern is not applicable.'),('Next to an isolated point charge','Its field is radial rather than uniform.')])
 if t==22:
  replacements(12,[('AC because its size varies','AC requires direction reversal.'),('AC only during the pulse maximum','Classification follows reversal, not instantaneous size.'),('Neither AC nor DC because it is not constant','Unidirectional pulsating current is DC.')])
 if t==24:
  wrong(9,2,'0.0008 kWh','This mishandles both the time multiplication and the kW-to-kWh use; 0.8×2 is required.')
  A.mc[11]['prompt']='A 440 W training appliance operates at 220 V. Which fuse is suitable in the simple steady-current exercise: 1 A, 3 A, 10 A or 13 A?'
 if t==25:
  wrong(10,1,'Circle radius alone reverses while direction stays fixed','Reversing current reverses field direction; radius is a location, not a signed direction.')
  wrong(11,2,'Keep supply voltage fixed and assume current unchanged','Extra winding resistance can change current even at fixed voltage.')
 if t==26:
  correct(10,'It halves','Rotation frequency doubles, so period T=1/f halves.')
  wrong(10,2,'It becomes one quarter','A factor-two frequency increase gives factor-two, not factor-four, period decrease.')
  replacements(11,[('Polarity stays fixed','The direction of field change has reversed.'),('Induced emf stays zero despite moving through a changing field','The moving magnet can produce a nonzero induced emf.'),('Current becomes DC in one direction through both strokes','Reversed magnet motion reverses polarity and current direction in the same closed circuit.')])
 if t==27:wrong(12,2,'Three','Three half-lives leave one eighth, not one quarter.')
 if t==28:
  replacements(10,[('Downward','This is the positive-particle direction, not negative beta.'),('Straight through with no deflection','Beta-minus has charge and experiences an electric force.'),('Toward whichever plate is closer regardless of charge','The field-force direction is opposite E for negative charge.')])
  wrong(12,2,'One twelfth','Decay fraction is (1/2)³, not reciprocal elapsed hours.')
