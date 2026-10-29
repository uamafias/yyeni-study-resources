"""Review repair: concise parallel keys and reproducibly shuffled option positions."""
import ast,importlib,random,re,pprint,json
from pathlib import Path
D=Path(__file__).parent
if (D.parent/'planning/mc-option-audit.json').exists():
 raise SystemExit('One-time migration already applied. Use check_review_repairs.py to validate the current source and bank; do not permute migrated rows again.')
# Preserve each scientific proposition while removing explanatory length cues.
short={
(1,3):'View the lower meniscus at eye level', (1,4):'Correcting the offset removes systematic bias',(1,8):'The warmer trial produces gas faster',(1,9):'A volumetric pipette',(1,10):'Colourless solutes can remain dissolved',(1,11):'Ink could produce additional spots',
(2,2):'Random motion spreads perfume molecules.',(2,4):'Isotopes may be stable or radioactive.',(2,5):'X forms X⁺; Y forms Y⁻.',(2,6):'Its first electron shell is full.',(2,7):'Brass is a variable-composition mixture.',(2,8):'Nuclei attract the shared electron pair.',
(3,1):'Sawing reshapes the existing natural material.',(3,4):'They describe different aspects of nylon.',(3,8):'Hydration of cement binds the aggregate.',
(4,1):'One twelfth of a carbon-12 atom’s mass.',(4,2):'The summed relative atomic masses.',
(5,1):'A conductor contacting the electrolyte.',(5,4):'Separated immersed electrodes across a DC supply.',(5,6):'Cathode: lead; anode: bromine.',(5,8):'Cathode: hydrogen; anode: chlorine.',(5,9):'Cathode: lithium; anode: bromine.',(5,12):'It dissolves oxide at a lower temperature.',
(6,1):'A new substance forms.',(6,4):'Combustion transfers energy to the pan.',(6,5):'No operating combustion; weather-dependent output.',(6,6):'A higher gas-production rate.',(6,7):'Successful collisions occur more frequently.',
(7,2):'It neutralises acid but is water-insoluble.',(7,6):'It neutralises acids.',(7,8):'React excess CuO, filter, then crystallise.',
(8,2):'It detects contamination on the wire.',(8,3):'Bright sodium emission masks other colours.',(8,7):'Dissolved ammonia creates alkaline conditions.',(8,9):'Insoluble calcium carbonate precipitates.',(8,11):'Lighted splint: squeaky pop.',
(9,2):'Metallic array with different atom types.',(9,8):'It dissolves oxide at lower temperature.',(9,9):'Recycling reduces demand for ore extraction.',
(10,8):'Alcohol + acid → ester + water',(10,11):'Water breaks amide links, releasing amino acids',(10,12):'Matching conditions permit meaningful comparison',
(11,2):'Insoluble calcium or magnesium soap',(11,3):'Carbonate ions precipitate calcium ions',(11,4):'It supplies deficient mineral nutrients',(11,6):'Acid + carbonate → salt + CO2 + water',(11,7):'It oxidises impurities in molten material',(11,8):'It accumulates and impairs oxygen transport'}
# Parallel product pairs avoid one option being more detailed than its peers.
parallel={
(5,6):['Cathode: hydrogen; anode: oxygen.','Cathode: lead; anode: bromine.','Cathode: bromine; anode: lead.','Cathode: lead oxide; anode: hydrogen.'],
(5,8):['Cathode: sodium; anode: chlorine.','Cathode: hydrogen; anode: sulfur dioxide.','Cathode: copper; anode: oxygen.','Cathode: hydrogen; anode: chlorine.'],
(5,9):['Cathode: lithium; anode: bromine.','Cathode: hydrogen; anode: oxygen.','Cathode: bromine; anode: lithium.','Cathode: lithium hydroxide; anode: hydrogen.']}
report=[]
for t in range(1,12):
 path=D/f'topic{t}_activities.py';s=path.read_text();module=importlib.import_module(f'topic{t}_activities');rows=[]
 rng=random.Random(611700+t);target=list('AAABBBCCCDDD')
 while True:
  rng.shuffle(target)
  if all(not(target[i]==target[i+1]==target[i+2]) for i in range(10)) and all(any(target[i]!=target[i%p] for i in range(p,12)) for p in range(1,7)):break
 for n,(q,opts,key,reason,wrong) in enumerate(module.MC,1):
  opts=list(opts);old=ord(key)-65
  if (t,n) in short:opts[old]=short[t,n]
  if (t,n) in parallel:opts=parallel[t,n]
  remaining=[i for i in range(4) if i!=old];rng.shuffle(remaining);newpos=ord(target[n-1])-65;perm=remaining[:];perm.insert(newpos,old);mapping={chr(65+original):chr(65+j) for j,original in enumerate(perm)}
  wrong=re.sub(r'\b[ABCD]\b',lambda m:mapping[m.group()],wrong)
  newopts=[opts[i] for i in perm];rows.append((q,newopts,target[n-1],reason,wrong))
  lengths=[len(re.findall(r'\w+',v)) for v in newopts];report.append({'topic':t,'part':n,'key':target[n-1],'lengths_words':lengths,'key_unique_longest':lengths[newpos]>max(v for j,v in enumerate(lengths) if j!=newpos),'key_tied_longest':lengths[newpos]==max(lengths)})
 tree=ast.parse(s);node=next(x for x in tree.body if isinstance(x,ast.Assign) and any(isinstance(z,ast.Name) and z.id=='MC' for z in x.targets));lines=s.splitlines(keepends=True);lines[node.lineno-1:node.end_lineno]=['MC='+pprint.pformat(rows,width=120,sort_dicts=False)+'\n'];path.write_text(''.join(lines))
(D.parent/'planning/mc-option-audit.json').write_text(json.dumps({'status':'author_revised_independent_review_pending','method':'Balanced shuffled positions with no run >2 and no repeated period 1–6; option wording shortened or made parallel by chemical meaning, not padded. Distractor labels remapped.','questions':report,'key_unique_longest':sum(x['key_unique_longest'] for x in report),'key_tied_or_longest':sum(x['key_tied_longest'] for x in report)},indent=2)+'\n')
print('Unique longest',sum(x['key_unique_longest'] for x in report),'of 132; including ties',sum(x['key_tied_longest'] for x in report))
