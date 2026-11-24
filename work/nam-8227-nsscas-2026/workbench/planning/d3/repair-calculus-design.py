"""D3 stage-D input repair only; no runtime authoring or generation.

Only replaces the two owned recipe objects. Fresh-read/write preserves motion.
"""
from pathlib import Path
from copy import deepcopy
import json
HERE=Path(__file__).resolve().parent
WB=HERE.parent.parent
P=WB/'planning'
IDS={'WB8227-implicit-normal','WB8227-stationary-inflexion'}

def replace_strings(value):
 if isinstance(value,str):
  return value.replace('@0.1.2:', '@0.1.3:').replace('adapted D2 proposal','adapted D3 proposal').replace('D2 proposal; Claude confirmation','D3 proposal; Claude confirmation')
 if isinstance(value,list):return [replace_strings(v)for v in value]
 if isinstance(value,dict):return{k:replace_strings(v)for k,v in value.items()}
 return value

def policy(part):
 cs=part['criteria'];ab=[c['suffix'] for c in cs if c['mark_type'] in ['A','B']];methods=[c['suffix']for c in cs if c['mark_type']in ['M','DM']]
 return dict(policy_id='OD-6',authority='Owner decision, 24 November 2026; NSSCAS 2025 report PDF 345 item 4 CONVENTION:108 plus comparable Cambridge 9709_m16_ms_12.pdf PDF 3 Penalties, not a Namibian tariff.',eligibility='A genuinely misread question datum only, with the object and difficulty unchanged; no easier or no-solution task. Misreading own figures is ordinary accuracy error.',unit='Once per genuinely misread datum in the first part where that misread is used; no repeat charge in later parts.',deduction=dict(amount=1,mark_types=['A','B'],selection='Earliest earned A/B criterion in this part in canonical criterion order, after eligibility and working checks; never make a criterion or part negative.',if_none='Deduct zero if no A/B award was earned in that first-use part; do not transfer a charge to a later part.'),follow_through_award_suffixes=ab,method_award_suffixes=methods,continuation='All eligible A/B awards follow through on the misread value, subject to their existing evidence, dependency and www conditions; M/DM judged normally. Record previous deduction and do not charge again.',excluded='Own-figure errors, object/difficulty changes, easier/no-solution cases receive ordinary canonical marking without MR adjustment. Named method errors and bare answers are not rescued.',ledger_fields=['datum_id','canonical_value','misread_value','eligibility_reason','first_use_part_id','earned_A_B_before_deduction','deducted_criterion_id','deduction','prior_deduction'],feedback='Name the misread and distinguish valid work on that value from the canonical datum.')

def main():
 d=json.loads((P/'calculus-design.json').read_text())
 protected=[deepcopy(r)for r in d['recipes']if r['recipe_id']not in IDS]
 baseline=json.loads((P/'history/d2-candidate/work/nam-8227-nsscas-2026/workbench/planning/calculus-design.json').read_text())
 owned={r['recipe_id']:r for r in baseline['recipes']if r['recipe_id']in IDS}
 for i,live in enumerate(d['recipes']):
  if live['recipe_id']not in IDS:continue
  old=owned[live['recipe_id']]
  r=replace_strings(old);r['version']=r['proposed_version']='0.1.3'
  for b in r['branches']:
   for part in b['part_specs']:
    part['misread_policy']=policy(part)
    for c in part['criteria']:
     # OD-6 is the sole new accuracy F.T. exception; the answer-given proof target is fixed.
     if c['mark_type']in ['A','B']:
      c['qualifiers'].append('OD-6 only: eligible genuine question-data misreads permit accuracy follow-through with correct working; apply the once-per-datum A/B deduction ledger. The fixed supplied proof target is not changed.')
    if part['part_id']=='show-derivative':
     part['alternative_criterion_mapping']['S3']='Correct implicit derivatives of the remaining y-terms and treatment of C as constant. No back-substitution in this slot; the explicit-root route alone uses its justified root/y identity here.'
     part['alternative_criterion_mapping']['S4']='Complete correct forward rearrangement, including back-substitution of C=ae^(kx)y+y^2 where needed, establishes the fixed supplied target or an explicitly shown equivalent form; S1–S3 correct and complete; no follow-through into a given result.'
     part['misread_policy']['supplied_target_guard']='The supplied target remains fixed. A misread making the curve and supplied target inconsistent changes the proof object and receives ordinary canonical marking, not MR treatment. S4 always needs a complete correct proof of the actual supplied target.'
     part['alternative_route_conditions'].append('Every accepted path (product, explicit-root, divided, log-absolute) is stored; do not fabricate product-rule evidence for a path that does not use it.')
     part['alternative_route_conditions'].append('At the supplied negative-y branch, real ln(y) without moduli is invalid: S1=0, dependent S2=0 and S4=0; independently correct remaining implicit derivative/constant evidence may earn S3 only, maximum 1/4. Valid ln|y| proofs can earn 4/4.')
     part['alternative_marking_samples']=[dict(sample='divided-proof-correct-differentiation-failed-back-substitution',criterion_awards={'S1':1,'S2':1,'S3':1,'S4':0},score=3,total=4),dict(sample='ln-y-without-moduli-at-supplied-negative-branch',criterion_awards={'S1':0,'S2':0,'S3':1,'S4':0},score=1,total=4,condition='Independently correct S3 evidence is visible; otherwise zero.')]
    if b['branch_id'].endswith(':normal')and part['part_id']=='gradient':
     part['marking_clarification']='The known e-index error in the failed proof can still yield the canonical value at x=0: eligible H1 substitution plus that value earns H1/H2=2/2. S2/S4 remain lost; gradient-only G5 has its separate www condition. This is an ordinary numerical coincidence, not OD-6.'
    if part['part_id']=='normal':
     n1=next(c for c in part['criteria']if c['suffix']=='N1')
     n1['qualifiers'][0]='A labelled perpendicular-gradient value equal to -1/(their m) in working is sufficient M1; an explicit reciprocal calculation is not mandatory. Negation or positive reciprocal is not accepted.'
    if b['branch_id'].endswith(':flat-classification')and part['part_id']=='point':
     for dd,role in [('8227:2020:M2:T1:O03:D01','linear polynomial division'),('8227:2020:M2:T1:O03:D03','identify quotient and zero remainder')]:
      part['prerequisite_demand_ids'].append(dict(demand_id=dd,role='conditional prerequisite for power=4: '+role+' in the factor-theorem route; alternative to binomial-cube recognition, not directly assessed coverage',condition='power=4',alternative_route='factor-theorem'))
     route=next(z for z in part['prerequisite_routes']if z['route_id']=='factor-theorem')
     route['demand_ids']+=['8227:2020:M2:T1:O03:D01','8227:2020:M2:T1:O03:D03'];route['module_dependencies'].append('M2:T1:O03')
    part['bloom_criterion_ids']=part['fully_qualified_criterion_ids']=[c['criterion_id']for c in part['criteria']]
    part['bloom_rationale']+=' D3 evidence: '+', '.join(part['fully_qualified_criterion_ids'])+'.'
  d['recipes'][i]=r
 assert [r for r in d['recipes']if r['recipe_id']not in IDS]==protected,'Unowned motion changed'
 d['d3_calculus_scope']='Owned implicit/stationary marking clarifications and per-part OD-6; domains, capacities, part demands and Apply labels retained. Stage-D only; Claude confirmation then Vitalis approval pending.'
 (P/'calculus-design.json').write_text(json.dumps(d,indent=2,ensure_ascii=False)+'\n')

if __name__=='__main__':main()
