"""Targeted leak and activity repair; explicit limits remain in the review brief."""
import re
CARDS={}
def card(k,p,a,g,recall=0,sub='APP',ao='B',bloom='Apply'):
 CARDS[k]=dict(prompt=p,canonical_answer=a,marking_guidance=g.split('|'),recall=recall,subtype=sub,assessment_objectives=[ao],blooms_level=bloom)
card('8-013','Explain why “precipitate remains in excess ammonia” cannot distinguish Fe²⁺ from Fe³⁺. State the further observation that distinguishes them.','Both hydroxide precipitates remain insoluble in excess ammonia. Their colours distinguish them: Fe²⁺ gives green and Fe³⁺ red-brown.','Shared insolubility cannot distinguish the ions (1).|Green for Fe²⁺ and red-brown for Fe³⁺; both links required (1).',1,'PROC','C','Apply')
card('9-015','Explain a suitable broad extraction method for a metal X lying below carbon in the reactivity series, when X occurs as its oxide.','Heat the oxide with carbon or a suitable carbon-containing reducing agent: carbon is more reactive than X and can remove its oxygen.','Carbon/carbon-monoxide reduction linked to X lying below carbon, so oxygen can be removed from its oxide; method alone is insufficient (1).')
card('8-029','Describe the halide indicated when a sample acidified with dilute nitric acid gives a cream precipitate with silver nitrate that remains in dilute ammonia. Explain how the ammonia result distinguishes it from chloride, whose silver precipitate dissolves in dilute ammonia.','Bromide is indicated. Its silver precipitate remains, unlike silver chloride, which dissolves in the supplied comparison.','Bromide / Br⁻ identified from the test (1).|Persistence in dilute ammonia excludes the supplied chloride behaviour (1).',1,'PROC','C','Apply')
card('7-056','State the general solubility pattern for most metal hydroxides.','Most metal hydroxides are insoluble. Sodium, potassium and barium hydroxides are soluble exceptions; calcium hydroxide is slightly soluble.','Most metal hydroxides are insoluble (1).',1,'DEF','A','Remember')
# Keep the existing stimulus and answer, but use a command that matches the task.
RENAMES={'8-023':('Deduce','Analyse'),'8-024':('Plan','Create')}
SHARED='''A solution X contains one of Cu²⁺, Fe²⁺ or Fe³⁺ and one of Cl⁻, Br⁻ or I⁻. The following laboratory record applies to all five parts.

| Portion | Treatment | Observation |
|---|---|---|
| A | NaOH added dropwise | Light-blue solid appears |
| A | More NaOH added until in excess | The solid remains |
| B | Aqueous ammonia added dropwise, then in excess | Light-blue solid first appears; in excess it disappears and the liquid is deep blue |
| C | Reserved, untreated portion | Available for a halide test |

A subsequent test on C produces a white silver-salt precipitate. No repeat trials or purity measurements have been made.'''
PARTS={
'a':('Complete a results table for portion A with separate entries for initial appearance, behaviour in excess, and whether each observation describes a solid or a solution.', 'Initially a light-blue precipitate forms. In excess NaOH it remains as an insoluble solid, rather than becoming a blue solution.', ['Initial light-blue precipitate recorded (1).','Solid remains in excess, so it is insoluble (1).','Physical state correctly identified as a solid/precipitate, not a solution (1).'],0,3),
'b':('Deduce the cation from A and B, and correct the description “deep-blue precipitate in excess ammonia” using the recorded change in B.', 'Cu²⁺ is supported. In excess ammonia the solid disappears, so the deep-blue material is a solution, not a precipitate.', ['Cu²⁺ / copper(II) (1).','Deep-blue solution because the solid has dissolved; the label precipitate is incorrect (1).'],1,2),
'c':('Describe the reagent sequence to carry out the halide test on the reserved portion C before obtaining the recorded white precipitate.', 'Add dilute nitric acid to C, followed by aqueous silver nitrate.', ['Acidify the fresh portion with dilute nitric acid (1).','Then add aqueous silver nitrate (1).'],2,2),
'd':('Explain the anion identification supported by the result from (c), why nitric acid is used instead of hydrochloric acid, and why portion C was kept separate from A.', 'The white silver precipitate supports chloride. Hydrochloric acid would introduce chloride and could create the positive result itself. Separate C avoids NaOH carried over from A interfering with the silver-nitrate test.', ['Chloride / Cl⁻ from the white silver precipitate (1).','HCl introduces chloride, so it could cause a false positive (1).','A separate portion avoids carry-over of NaOH/earlier reagents into this test (1).'],1,3),
'e':('Explain why these results do not establish that X is pure copper(II) chloride, and give one improvement to the strength of the identification evidence.', 'Positive tests support the presence of the named ions, not the absence of every other substance. Repeat the tests on fresh portions with appropriate controls, or use a further independent identification test.', ['Presence of the ions does not exclude other dissolved substances/purity is not established (1).','Repeat on fresh portions with appropriate controls or use an independent confirmatory test (1).'],0,2)
}
# Concrete replacement work after the additional honest recall allocations; these retain their environmental/gas contexts.
card('11-057','Describe the changes in a vehicle exhaust after a catalyst is fitted: CO falls from 8 to 2 units, nitrogen oxides from 6 to 1, and CO2 rises from 10 to 14 under the same test conditions. Explain why “all harmful emissions fell” is not supported.','CO and nitrogen oxides both decrease, but CO2 increases. The results support reduced CO/NOx pollution, not a fall in every harmful emission because CO2 contributes to the greenhouse effect.','Both CO and NOx fall, with the stated before/after data used (1).|Reject all-emissions claim because CO2 rises and contributes to greenhouse warming (1).',0,'INTERP','B','Analyse')
card('11-045','Describe a conclusion and a limitation from a food-packaging trial. Identical foods in sealed air-filled packs develop rancidity by day 4; nitrogen-flushed packs do so by day 12. Both groups are kept at the same temperature.','Nitrogen flushing delays rancidity under these conditions. It does not prevent deterioration indefinitely or prove the food sterile, because deterioration still occurs and no microbial tests were made.','Delay supported by day 4 versus day 12 under matched conditions (1).|A stated limit: later deterioration still occurs, or sterility was not tested (1).',0,'INTERP','B','Analyse')
def apply_card(x,k):
 if k=='8-019':
  x['objective_ids']=list(dict.fromkeys(x.get('objective_ids',[])+['OBJ-6117-8.1-01-12']))
  x['claim_ids']=list(dict.fromkeys(x.get('claim_ids',[])+['CLM-6117-8.1-01-12-T1']))
 if k in RENAMES:
  command,bloom=RENAMES[k];x['prompt']=re.sub(r'^\w+',command,x['prompt']);x['blooms_level']=bloom
 if k not in CARDS:return None
 for f,v in CARDS[k].items():
  if f!='recall':x[f]=v
 return CARDS[k]['recall']
def apply_part(z):
 if z['task_id']=='ITEM-6117-8-P03':
  p,a,g,r,m=PARTS[z['part']];z.update(prompt=p,canonical_answer=a,marking_guidance=g,mark_tariff=m,command_word=p.split()[0]);z['credit_requirement']=' '.join(g)
  return r
 return None
def learner_text(s):
 s=re.sub(r'\b[Oo]riginal synthetic results(?: for)?\b','Results for',s)
 s=s.replace('For syllabus answers on Namibia’s water scarcity, retain the stated limitation: seawater desalination is expensive and is not presented as the solution to the national water-scarcity problem. The curriculum does not require assessment of a particular modern plant. Infrastructure and energy costs matter, but an unverified project webpage is not evidence for an examinable claim.','Seawater desalination is expensive, so it is not a complete solution to Namibia’s water-scarcity problem. Its energy and infrastructure requirements limit its use.')
 s=s.replace('ships and industrial heating','ships and home heating systems')
 s=s.replace('Cooling apparatus and separate hardness-testing apparatus, with required measurements and controls.','Cooling-investigation apparatus: labelled answer/reference arrangement.')
 s=s.replace('sodium and potassium hydroxides are soluble, while calcium hydroxide is slightly soluble','sodium, potassium and barium hydroxides are soluble, while calcium hydroxide is slightly soluble')
 s=s.replace('diesel oil, fuel oil and bitumen','diesel oil, fuel oil, lubricating fraction and bitumen')
 return s
