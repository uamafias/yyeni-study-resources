"""D3 authored design edit. Finite design enumeration, never runtime generation."""
import json,itertools
from pathlib import Path
import sympy as s
P=Path(__file__).resolve().parents[1];W=P.parent
read=lambda p:json.loads(p.read_text())
dump=lambda p,d:p.write_text(json.dumps(d,indent=2,ensure_ascii=False)+'\n')
d=read(P/'calculus-design.json');r=next(r for r in d['recipes']if r['recipe_id']=='WB8227-motion-integration')
ks=[-3,-2,-1,1,2,3]
rev=[(k,r,c,T)for k,r,c,T in itertools.product(ks,range(1,5),range(1,4),[3,4,5])if r<T and 2*r!=T]
outside=[(4,1,3),(5,1,3),(5,1,4),(6,1,5)]
no=[(k,r,c,T)for k in ks for r,c,T in outside]
assert len(rev)==144 and len(no)==24
r.update(version='0.1.3',status='D3 proposal; Claude changed-scope confirmation then Vitalis approval pending',total_capacity=137+56+len(rev)+len(no))
b=r['branches'][-1];b['capacity']=168;b['accepted_tuple_keys']=[[str(x)for x in row]for row in rev+no]
b['display_title']='Distance and displacement from a quadratic velocity'
b['legacy_id_note']='interior-reversal is an immutable internal historical ID, not a public hint. Version 0.1.3 changes the admitted domain; earlier versioned work retains its saved meaning.'
b['domain_spec']={
 'velocity':'k*(t-r)*(t+c), rendered expanded as a*t^2+b*t+d; only a,b,d,T visible',
 'tuple_order':['k','r','c','T'],
 'reversal':{'k':ks,'r':[1,2,3,4],'c':[1,2,3],'T':[3,4,5],'include':'0<r<T','exclude':'2*r=T (triangle coincidence)'},
 'no_reversal':{'k':ks,'contexts_r_c_T':[list(x)for x in outside],'include':'r>T, with margin r-T equal to 1 or 2'},
 'constraints':['Negative root -c lies outside the interval; positive root never at an endpoint.','Same T and |k| domains in both outcomes. Expanded coefficients do not label either outcome.','No answer cue in title, stem or pre-submission metadata.'],
 'outcome_proportion':{'sign_change':144,'no_sign_change':24,'no_sign_change_fraction':'1/7','reason':'A bounded 14.29% minority makes the direction decision necessary while retaining most practice on two-leg integration. It is a planner choice, not examination prevalence. All six signed amplitudes occur in every outside-root context.'}}
b['semantic_capacity']={
 'whole_parameter_tasks':168,'distance_part_contexts':168,'displacement_part_contexts':168,
 'amplitude_and_direction_normalised_shapes':28,'normalised_shapes_by_outcome':{'sign_change':24,'no_sign_change':4},
 'decision_outcome_classes':{'sign_change':144,'no_sign_change':24},'initial_direction_classes':{'negative':84,'positive':84},
 'fresh_whole_upper_bound':168,'no_repeat_keys':{'distance':['k','r','c','T'],'displacement':['k','r','c','T']},
 'key_alias_rule':'The expanded polynomial is uniquely identified by k,r,c with k nonzero and exactly one positive/one negative root. Both part keys use the same tuple; a fixed complete interval never gains freshness by re-factoring or changing root order. A changed T is a new bounded task but the same polynomial model; retain model exposure separately. See planning/d3/motion-design-check.json separation/key audit.',
 'rescaling_note':'24 reversal and 4 outside-root shapes after sign/amplitude normalisation; each has six signed amplitudes. Shapes are not different reasoning types.'}
b['official_qualifiers'].update(
 R1='M1 solve v=0 (one algebra/arithmetic slip allowed) then coherently compare roots/signs with (0,T); OR give a complete correct constant-sign argument on [0,T], for example endpoint signs plus the appropriate concavity or a vertex bound. The alternatives fill one slot, never add marks. A guessed decision/root or vertex location alone is insufficient.',
 R3='DM1 dependent on R1: from an attempted primitive evaluate both bounds of each chosen leg and sum nonnegative lengths. One or two legs; limited FT from their credible solved root and interval decision. Calculator quadrature values alone do not earn this mark.',
 R4='A1 canonical distance exact or 3sf, dependent on R2 and R3 and correct working (www); no ordinary own-root FT. A one-slip false interior root in a no-change case loses R4 even if the total coincides, giving 3/4 with R1/R2/R3. OD-6 genuine unchanged-difficulty datum misreads instead follow the shared A/B FT rule.',
 R5='M1 signed whole-interval integration from an attempted primitive with both bounds, or the signed sum of the legs from (a), evaluated from an attempted primitive with both bounds. Reusing the earlier primitive is accepted; calculator legs alone are insufficient.',
 R6='A1 canonical signed displacement, dependent on valid R5; no ordinary own-answer FT. OD-6 eligible datum misreads follow the shared A/B FT rule.')
b['named_deviation']='D2-MOTION-LIVE-CHECK: OD-4 requires mixed outcomes and a live direction decision. The exact fixed 4+2 tariff, R1 alternative, primitive-based own-root DM1 and R4 www are planner proposals, not an owner-fixed rubric or an official table; pending exact-manifest approval.'
for branch in r['branches']:
 for q in branch['part_specs']:
  for key in ['criterion_id_rule','bloom_rationale']:
   if key in q:q[key]=q[key].replace('@0.1.1:', '@0.1.3:').replace('@0.1.2:', '@0.1.3:').replace('recipe_id@0.1.2','recipe_id@0.1.3')
  for key in ['fully_qualified_criterion_ids','bloom_criterion_ids']:
   q[key]=[x.replace('@0.1.2:', '@0.1.3:')for x in q[key]]
  q['misread_policy']={'policy_id':'OD-6','eligibility':'Genuine misread of question datum with object and difficulty unchanged; own-figure misreads and easier/no-solution tasks use ordinary canonical rules.',
   'first_use_part':'This part if first use; otherwise use the existing per-datum ledger without another deduction.',
   'deduction':{'unit':'once per genuinely misread datum','amount':1,'mark_types':['A','B'],'selection':'earliest eligible earned A/B criterion in part and criterion order','if_none':'zero; do not deduct from M/DM or another part'},
   'follow_through':'All A/B awards follow through the eligible misread; M/DM judged as usual. Correct working, named exclusions, dependencies and OD-1 answer-only restrictions still apply.',
   'ledger_fields':['datum_id','canonical_value','misread_value','eligibility_reason','first_use_part','deducted_criterion','deduction_applied'],
   'sources':['8227:CONVENTION:108 / NSSCAS 2025 report PDF345 item4','Cambridge 9709_m16_ms_12.pdf PDF3 Penalties (comparable board convention, owner adopted)']}
  q['bloom_rationale']=q['bloom_rationale'].replace('Outcomes vary108/24','Outcomes vary 144/24').replace('R1 root/interval decision','R1 root/interval or complete constant-sign decision')
t=s.symbols('t')
cases=[c for c in d['exemplar_cases']if c['recipe_id']==r['recipe_id']]
for case in cases:
 case['recipe_version']='0.1.3'
 if case['branch_id'].endswith('interior-reversal')and case['case_role']=='changed':
  p={'k':-1,'r':4,'c':1,'T':3};case['parameters']=p
  v=s.expand(p['k']*(t-p['r'])*(t+p['c']));F=s.integrate(v,t);ans=s.integrate(v,(t,0,3))
  case['expected_answers']={'roots':[-1,4],'interior_roots':[],'sign_change':False,'signed_legs':[str(ans)],'displacement':str(ans),'distance':str(ans),'primitive':str(F),'expanded_velocity':str(v)}
 for key in ['velocity','acceleration','distance_exact']:
  if key in case['expected_answers']:case['expected_answers'][key]=str(s.sympify(case['expected_answers'][key],locals={'t':t}))
dump(P/'d3/motion-cases.json',cases)
d['counts']['branch_qualified_capacity']=sum(b['capacity']for rec in d['recipes']for b in rec['branches'])
dump(P/'calculus-design.json',d)
print(json.dumps({'mixed_capacity':168,'outcomes':[144,24],'shape_count':28,'motion_raw':r['total_capacity'],'legacy_branch_sum':d['counts']['branch_qualified_capacity']}))
