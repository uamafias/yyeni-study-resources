"""Complete the exemplar MCQ slice with original whole-topic questions."""
import json
from authoring_support import stamp

def add_mcq(a):
 a.items=[i for i in a.items if i['item_id']!='ITEM-6116-3-P01']
 prompt='''Identify the correct option in each question. Each is worth 1 mark.
1. Which structure is a site of aerobic respiration?
A. Mitochondrion
B. Cell wall
C. Cell-sap vacuole
D. Ribosome
2. What usually explains permanent activity loss after an enzyme is strongly heated?
A. It was a living cell that died
B. Its active-site structure was altered by denaturation
C. Its substrate became its nucleus
D. Cooling removes its amino acids
3. Why do growing plants need nitrate ions?
A. To replace sunlight
B. To make cellulose directly from nitrate alone
C. To provide nitrogen for amino acids/proteins
D. To turn phloem into xylem
4. Which description defines an artery?
A. Towards the heart regardless of circuit
B. Carrying oxygenated blood
C. Carrying deoxygenated blood
D. Away from the heart
5. Which process uses oxygen to break down nutrients and release energy in cells?
A. Aerobic respiration
B. Pollination
C. Egestion
D. Ventilation alone
6. In bright light, what normally narrows the pupil?
A. Ciliary muscles change lens curvature
B. Circular iris muscles contract while radial muscles relax
C. The retina contracts around the lens
D. The cornea blocks the optic nerve
7. What action helps lower raised blood glucose under normal insulin control?
A. More glycogen converted to glucose
B. Glucose produced from oxygen
C. Increased conversion of glucose to glycogen in the liver
D. Stopping glucose use by cells
8. Two potato samples change from 2.0 to 2.4 g and from 4.0 to 4.4 g. Which has the greater proportional mass gain?
A. Second, because it finishes heavier
B. Equal, because each gains 0.4 g
C. First, 10%
D. First, 20% rather than 10%
9. Flooded roots have plenty of nitrate around them but little oxygen. Nitrate uptake needs energy from respiration. Which explanation fits the lower uptake?
A. Less respiratory energy is available for active uptake
B. Nitrate must have vanished outside
C. Diffusion requires additional respiratory energy
D. Floodwater guarantees higher ion uptake
10. Person X breathes 0.4 L per breath at 12 breaths/min and Y 0.5 L per breath at 15 breaths/min. Which has greater volume ventilated per minute?
A. X, 4.8 L/min
B. Y, 7.5 L/min
C. Equal because both breathe air
D. X, because smaller breaths are faster by definition
11. A kidney filters a normal amount of glucose, but glucose reabsorption is greatly reduced. Which outcome is expected if other processes are unchanged?
A. Glucose must vanish from filtrate by osmosis
B. Glucose can no longer enter the kidney
C. More glucose remains to pass into urine
D. Less glucose reaches urine because reabsorption stopped
12. A leaf warms up, but its stomata close and its water loss falls. Which interpretation fits?
A. Temperature has no effect on evaporation
B. The leaf must have stopped containing water
C. Heating created more water
D. Closing the stomata can outweigh the effect of temperature on water loss
'''
 keys=[
 ('A','Aerobic respiration takes place in mitochondria.','B supports a plant cell; C stores cell sap; D makes proteins.'),
 ('B','Denaturation changes the shape of the protein and its active site.','A treats the enzyme as living; an enzyme has no nucleus (C); cooling does not remove amino acids (D).'),
 ('C','Nitrate supplies nitrogen for amino acids and proteins.','A confuses a mineral ion with light energy; cellulose contains no nitrogen (B); D confuses the transport tissues.'),
 ('D','An artery carries blood away from the heart.','A describes a vein; B and C use oxygen content, but the pulmonary artery carries deoxygenated blood.'),
 ('A','Aerobic respiration breaks down nutrients in cells using oxygen.','B transfers pollen; C removes undigested food; D moves air in and out of the lungs and is not a reaction in cells.'),
 ('B','In bright light the circular muscles of the iris contract and the radial muscles relax.','A describes focusing; the retina has no muscle (C); the cornea does not block the optic nerve (D).'),
 ('C','Insulin causes the liver to convert glucose to glycogen.','A raises blood glucose; glucose is not made from oxygen (B); cells keep using glucose (D).'),
 ('D','The gains are 0.4 ÷ 2.0 = 20% and 0.4 ÷ 4.0 = 10%.','A uses final mass instead of proportion; B ignores the starting mass; C gives the wrong percentage.'),
 ('A','Little oxygen means little aerobic respiration, so less energy for active uptake.','B contradicts the plentiful nitrate; diffusion needs no energy from respiration (C); D ignores the oxygen shortage.'),
 ('B','Y ventilates 0.5 × 15 = 7.5 L/min, more than X at 0.4 × 12 = 4.8 L/min.','A gives the smaller value; C ignores the volumes and rates given; D assumes a rule that does not exist.'),
 ('C','Less glucose is returned to the blood, so more remains in the urine.','Osmosis moves water, not glucose (A); glucose is still filtered (B); D reverses the effect of reabsorption.'),
 ('D','Closed stomata leave water vapour little route out, even though the leaf is warmer.','Warming does increase evaporation (A); the leaf still contains water (B); heat does not create water (C).')]
 a.task('multiple_choice_set',['3.2-08','3.5-04','3.3.2-04','3.3.3-02'],prompt,
  '\n'.join(f'{n}. {k}. {why} Distractors: {wrong}' for n,(k,why,wrong) in enumerate(keys,1)),
  ['1 mark for each correct option, 12 marks in total.','Only the key earns the mark; a distractor, or more than one letter, earns no mark.'],12,['AO1','AO2'])
 item=a.items[-1]
 extra=['OBJ-6116-'+s for s in ('3.6.1.2-04','3.8.1-03','3.10.1-01','3.13.1-18','3.14-06','3.9-07','3.11-05','3.7-08')]
 item['objective_ids']+=extra
 # Whole-topic assessment legitimately cites the other groups' canonical claims after they exist.
 for group in ('3B','3C','3D'):
  p=a.base/f'claims/staging/claims_{group}.json'
  if not p.exists():p=a.base/f'authoring-groups/claims_{group}.json'
  for c in json.loads(p.read_text())['claims']:
   if set(c['objective_ids']) & set(extra):
    item['claim_ids'].append(c['claim_id']);item['claims_seen'][c['claim_id']]=c['revision']
 stamp(item)
 a.notes['deviations'].append({'from':'The reused structural exemplar contained a three-question MCQ slice.','to':'A twelve-question full-topic set, 12 marks, with seven knowledge and five consequential information-handling questions.','why':'Completes the approved performance-task demand; other approved exemplar content remains reused. No flashcard labels or slots change.'})
 a.notes['deviations'].append({'from':'Usual guideline of 2–4 claims per objective.','to':'Approved membrane exemplar retains five cross-mapped claims for 3.3.2-01, -03 and -04.','why':'Preserves distinct approved mechanism, practical-method and misconception claims instead of merging them merely to meet a count.'})
