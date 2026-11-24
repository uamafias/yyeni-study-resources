"""D4 finite design/oracle checks. Does not emit runtime questions or grade attempts."""
from pathlib import Path
from decimal import Decimal,ROUND_HALF_UP
import argparse,hashlib,importlib.util,json
import mpmath as mp
import sympy as sp
W=Path(__file__).resolve().parents[2]
spec=importlib.util.spec_from_file_location('d2_trig',W/'planning/d2/trig-d2-check.py');d2=importlib.util.module_from_spec(spec);spec.loader.exec_module(d2)
old=d2.old;mp.mp.dps=80

def dump(o):return json.dumps(o,indent=2)+'\n'
def read(p):return json.loads(p.read_text())
def half_angle(a,b,c):
 # Independent original-equation quadratic; not the transformed sine solver.
 A=b+c;B=-2*a;C=c-b
 if A==0:ts=[-mp.mpf(C)/B];rs=[mp.mpf(180)]
 else:
  D=B*B-4*A*C;ts=[(-B+mp.sqrt(D))/(2*A),(-B-mp.sqrt(D))/(2*A)];rs=[]
 rs.extend((2*mp.degrees(mp.atan(t)))%360 for t in ts)
 return sorted(rs)
def precision(domain):
 sets={k:[]for k in ['R_4sf_alpha_2dp','ratio_3sf_alpha_exact','ratio_3sf_alpha_2dp','coupled_acos_R_3sf_alpha_2dp']}
 for a,b,c in domain:
  R,al,be,canon=old.roots_phase(a,b,c);a2=mp.mpf(d2.fmt(al,2));R3=mp.mpf(mp.nstr(R,3));R4=mp.mpf(mp.nstr(R,4));ratio=mp.mpf(mp.nstr(c/R,3));betar=mp.degrees(mp.asin(ratio))
  from_beta=lambda bb,aa:sorted({v-aa for k in range(-2,4)for v in [bb+360*k,180-bb+360*k]if 0<v-aa<360})
  paths={'R_4sf_alpha_2dp':d2.shifted(R4,a2,c),'ratio_3sf_alpha_exact':from_beta(betar,al),'ratio_3sf_alpha_2dp':from_beta(betar,a2),'coupled_acos_R_3sf_alpha_2dp':d2.shifted(R3,mp.mpf(d2.fmt(mp.degrees(mp.acos(a/R3)),2)),c)}
  for name,rs in paths.items():
   if d2.sig(rs)!=d2.sig(canon):sets[name].append({'tuple':[a,b,c],'canonical_1dp':d2.sig(canon),'path_1dp':d2.sig(rs)})
 counts={k:len(v)for k,v in sets.items()};assert counts=={'R_4sf_alpha_2dp':3,'ratio_3sf_alpha_exact':14,'ratio_3sf_alpha_2dp':10,'coupled_acos_R_3sf_alpha_2dp':35},counts
 R=mp.sqrt(10);a=mp.degrees(mp.atan2(3,1));via=mp.degrees(mp.asin(3/mp.mpf(mp.nstr(R,6))));assert d2.fmt(a,2)=='71.57'and d2.fmt(via,2)=='71.56'
 return {'flip_sets':sets,'flip_counts':counts,'six_sf_asin_fixture':{'a':1,'b':3,'canonical_alpha_2dp':d2.fmt(a,2),'rounded_amplitude_asin_alpha_2dp':d2.fmt(via,2)},'interpretation':'14 and 10 are both correct for different phase-carry paths. Existing coupled exact-phase 33 and isolated phase 34 remain frozen D2 calculations.','status':'Author-recomputed stage-E/F acceptance expectations; runtime acceptance pending.'}
def misreads():
 # Mathematical evidence below is supplied by this independent design oracle.
 # The common helper derives the net question ledger, not learner recognition.
 from misread_ledger import settle,award
 rows=[]
 def add(id,awards,datums,proof,expected,historical_ids=()):
  out=settle(awards,datums);assert out['net_total']==expected,(id,out['net_total'],expected)
  rows.append(dict(fixture_id=id,mathematical_check=proof,derived_ledger=out,expected_total=expected,recomputed_historical_fixture_ids=list(historical_ids),runtime_marker_tested=False));return out
 def datum(id,eligible,first,reason,canonical=None,misread=None):return dict(datum_id=id,eligible=eligible,first_use_part=first,reason=reason,canonical_value=canonical,misread_value=misread)
 def awards(part,seq,data=(),basis='misread'):
  return[award(cid,part,typ,credit,list(data),basis=basis)for cid,typ,credit in seq]
 PI=[('P-B1','B',1),('P-M1','M',1),('P-A1','A',1)]
 assert sp.asin(5*(-sp.Rational(1,10)))==-sp.pi/6
 add('PI-k4-copied-as5',awards('p-decision',PI,['k']),[datum('k',True,'p-decision','Nonzero divisor changes only scaling; exact-angle and real decision preserved',4,5)],dict(inverse_check='asin(5*(-1/10))=-pi/6',canonical_x='-1/8',misread_x='-1/10'),2,['PI-k4-copied-as5'])
 forced=-sp.sqrt(2)/6;assert sp.asin(3*forced)==-sp.pi/4
 add('PI-no-solution-changed-to-real',awards('p-decision',[(i,t,0)for i,t,_ in PI],['theta'],'canonical'),[datum('theta',False,'p-decision','No-real to real flips the assessed object; canonical in every use','-3*pi/4','-pi/4')],dict(misread_candidate=str(forced),actual_principal_inverse='-pi/4',canonical_outside_target='-3*pi/4'),0,['PI-no-solution-changed-to-real'])
 assert sp.Rational(-1,2)/4==-sp.Rational(1,8)
 add('PI-own-figure-error',awards('p-decision',[('P-B1','B',1),('P-M1','M',1),('P-A1','A',0)],basis='canonical'),[],dict(correct_forward='4*x=-1/2',correct_x='-1/8',learner_own_slip='-1/4'),2,['PI-own-figure-error'])
 R,al,be,rs=old.roots_phase(4,3,1);ind=half_angle(4,3,1)
 assert len(ind)==2 and all(abs(x-y)<mp.mpf('1e-60')for x,y in zip(rs,ind));assert d2.sig(rs)==['131.6','334.7']
 RA=[('a-B1','B',1),('a-M1','M',1),('a-A1','A',1)];RB=[('b-M1','M',1),('b-M2','DM',1),('b-A1','A',1),('b-A2','A',1)]
 ar=awards('a-convert',RA,['a'])+awards('b-roots',RB,['a']);ar[4]['depends_on']=['b-M1']
 add('RF-coefficient2-copied-as4-whole-question',ar,[datum('a',True,'a-convert','Conversion and two distinct interior-root search preserved',2,4)],dict(R='5',roots_degrees=[str(v)for v in ind]),6,['RF-coefficient2-copied-as4-a','RF-same-coefficient-later-b'])
 add('RF-method-only-no-AB-anywhere',awards('a-convert',[('a-B1','B',0),('a-M1','M',1),('a-A1','A',0)],['a']),[datum('a',True,'a-convert','Eligible datum but only method evidence earned in this scoped submission',2,4)],dict(evidence='Phase comparison attempted; no accurate amplitude or phase; no later response supplied'),1,['RF-method-only-no-AB'])
 assert 9>mp.sqrt(13)
 add('RF-misread-c1-as9-no-solution',awards('b-roots',[('b-M1','M',1),('b-M2','DM',0),('b-A1','A',0),('b-A2','A',0)],['c'],'canonical'),[datum('c',False,'b-roots','Two real roots replaced by no roots; canonical throughout',1,9)],dict(canonical_amplitude='sqrt(13)',misread_rhs_exceeds_amplitude=True,retained_evidence='Visible sine-subject reduction only; canonical root set not searched'),1,['RF-misread-c1-as9-no-solution'])
 a=sp.Integer(8);x=-sp.Rational(14,3);assert sp.simplify(2**(3*a)*a**x-2**10)==0
 LA=[('T-B1','B',1),('T-M1','M',1),('T-A1','A',1)];LB=[('U-M1','M',1),('U-A1','A',1)]
 add('LOG-c1-copied-as3-whole-question',awards('t-parameter',LA,['c'])+awards('t-target',LB,['c']),[datum('c',True,'t-parameter','Same log transform, exponentiation and nonzero hence substitution demand',1,3)],dict(a='8',misread_log_line='log2(y)=24+3x',misread_x=str(x),direct_residual='0'),4,['LOG-c1-copied-as3-a','LOG-same-c-later-b'])
 x=-sp.Rational(4,3);assert sp.simplify(2**a*a**x-2**4)==0
 add('LOG-target10-copied-as4-first-use-b',awards('t-parameter',LA,basis='canonical')+awards('t-target',LB,['q']),[datum('q',True,'t-target','Same nonzero target substitution; only b first uses q',10,4)],dict(log_equation='4=8+3x',x=str(x),direct_residual='0'),4,['LOG-target10-copied-as4-first-use-b'])
 add('OD1-bare-misread-answer',awards('p-decision',[(i,t,0)for i,t,_ in PI],['k']),[datum('k',True,'p-decision','Eligible copied datum; OD-1 gives no gross evidence for bare answer',4,5)],dict(evidence='Bare -1/10; no range/forward/verification work'),0,['OD1-bare-misread-answer'])
 add('RF-inverted-ratio-is-named-error',awards('a-convert',[('a-B1','B',1),('a-M1','M',0),('a-A1','A',0)],basis='canonical'),[],dict(method='tan(alpha)=a/b instead of b/a; named method error, not copied data'),1,['RF-inverted-ratio-is-named-error'])
 wrong_al=mp.degrees(mp.atan2(4,3));wrong_roots=d2.shifted(5,wrong_al,1);assert d2.sig(wrong_roots)!=d2.sig(rs)
 ar=awards('a-convert',[('a-B1','B',1),('a-M1','M',0),('a-A1','A',0)],['a'])+awards('b-roots',[('b-M1','M',1),('b-M2','DM',1),('b-A1','A',0),('b-A2','A',0)],['a']);ar[4]['depends_on']=['b-M1']
 add('RF-copied-coefficient-plus-inverted-ratio-whole-question',ar,[datum('a',True,'a-convert','Copied coefficient itself preserves demand; the independent phase error is not rescued',2,4)],dict(correct_misread_roots=d2.sig(rs),wrong_phase_roots=d2.sig(wrong_roots),wrong_phase_degrees=str(wrong_al)),2,['RF-copied-coefficient-plus-inverted-ratio-a','RF-copied-coefficient-plus-inverted-ratio-b'])
 # New D4 required designed-no-real outcome: the sign change preserves the decision.
 assert -3*sp.pi/4 < -sp.pi/2 and 3*sp.pi/4 > sp.pi/2
 add('PI-designed-no-real-negative-target-read-positive',awards('p-decision',PI,['theta']),[datum('theta',True,'p-decision','Both canonical and misread targets require the same no-real principal-range comparison','-3*pi/4','3*pi/4')],dict(canonical_comparison='-3*pi/4 < -pi/2',misread_comparison='3*pi/4 > pi/2',designed_no_real_outcome_preserved=True),2)
 # Actual new question data used twice: every datum gets one independent ledger entry.
 _,_,_,twors=old.roots_phase(4,3,-1);twoind=half_angle(4,3,-1);assert all(abs(x-y)<mp.mpf('1e-60')for x,y in zip(twors,twoind))
 ar=awards('a-convert',RA,['a'])+awards('b-roots',RB,['a','c']);ar[4]['depends_on']=['b-M1']
 add('RF-two-distinct-copied-data',ar,[datum('a',True,'a-convert','Same conversion/two-root demand',2,4),datum('c',True,'b-roots','Same negative-target interior-root search',1,-1)],dict(roots_degrees=d2.sig(twoind),first_deduction='a-B1',second_deduction='b-A1'),5)
 oldids={x['fixture_id']for x in read(W/'planning/d3/trig-d3-fixtures.json')['misread']['fixtures']}
 covered={x for row in rows for x in row['recomputed_historical_fixture_ids']};assert covered==oldids,(covered^oldids)
 return dict(fixtures=rows,recomputed_D3_fixture_rows=len(covered),derived_whole_question_ledgers=len(rows),unit='Proposed MR03-OPS-D4: one deduction per eligible datum from first earned A/B in question order, including later parts; none only if no A/B earned anywhere. Dependencies use gross earned evidence.',authority='OD-6 principle binding; unit/order/once-only eligibility ledger/net allocation proposed pending exact-manifest approval.',scope='Independent mathematics plus declared gross design evidence; net ledgers derived by common fixed-fixture helper, not a runtime marker.',stage_EF_carryforward=['RF c misread as b or +/-R: endpoint/tangent eligibility and canonical award paths.','LOG q misread as c*a: inspection-shortcut eligibility and canonical target awards.','Principal supplementary target pi-theta: forced candidate can coincide with canonical x; settle actual evidence at E/F.'])

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--check',action='store_true');args=ap.parse_args();doc=read(W/'planning/trig-model-design.json')
 r,rd=old.rform();p,pd=old.principal();g,gd=old.graph();t,td=old.gradient();cases=old.cases(doc,rd,pd,gd,td)
 baseline=read(W/'planning/history/d3-candidate/work/nam-8227-nsscas-2026/workbench/planning/trig-model-design.json')
 assert len(doc['recipes'])==len(baseline['recipes'])==3
 domains_unchanged=[]
 for current,previous in zip(doc['recipes'],baseline['recipes']):
  assert current['recipe_id']==previous['recipe_id']
  for b,oldb in zip(current['branches'],previous['branches']):
   for key in ['domain','capacity','raw_capacity','raw_parameter_count','presentation_count','semantic_capacity','semantic_capacity_by_part','capacity_detail','marks_total','whole_bloom','whole_card_bloom']:
    assert b.get(key)==oldb.get(key),(current['recipe_id'],b['branch_id'],key,'D4 domain/capacity changed')
   domains_unchanged.append(b['branch_id'])
  for case,oldcase in zip(current['exemplar_cases'],previous['exemplar_cases']):
   assert case['parameters']==oldcase['parameters']and case['expected_answers']==oldcase['expected_answers']
 assert doc['version']=='0.1.4';n=0
 for rec in doc['recipes']:
  assert rec['proposed_version']=='0.1.4'
  for b in rec['branches']:
   assert b['classification_version']=='8227-pilot-design-0.1.1'and sum(x['marks']for x in b['part_specs'])==b['marks_total']
   for part in b['part_specs']:
    n+=1;policy=part['misread_policy'];assert policy['policy_id']=='MR03-D4' and policy['owner_principle_id']=='OD-6' and 'pending' in policy['operational_status']
    assert part['answer_only_marks']==0 and sum(x['value']for x in part['criteria'])==part['marks']
 assert n==6
 ss=read(W/'planning/trig-model-source-reads.json');pairs=[]
 for group in [ss['readings'],ss['repair_d1']['readings'],ss['repair_d2']['readings'],ss['repair_d3']['readings']]:
  for entry in group:
   for pk,hk in [('source_path','source_sha256'),('render_path','render_sha256')]:assert hashlib.sha256(Path(entry[pk]).read_bytes()).hexdigest()==entry[hk]
   pairs.append((entry['source_path'],entry['pdf_page']))
 fixtures={'rounding':precision(rd),'misread':misreads(),'principal_no_real_rote_only':{'response':'range is [-pi/2,pi/2]; no real solution','actual_target_comparison':False,'awards':{'P-B1':0,'P-M1':0,'P-A1':0},'total':0,'out_of':3},'later_runtime_status':'All acceptance fixtures pending E/F; no runtime generator/marker tested.'}
 out={'status':'pass; D4 author-side finite design checks, not independent acceptance/runtime validation','recipe_version':'0.1.4','classification_version':'8227-pilot-design-0.1.1','branches':{'degree-cycle':r,'solve-or-explain':p,'graph-intercept':g,'gradient-target':t},'exemplar_checks':cases,'parts':n,'unchanged_domains_checked':domains_unchanged,'source_render_pairs':len(pairs),'unique_source_pages':len(set(pairs)),'D3_retained_rendered_pages':2,'fixture_summary':{'misread_ledgers':len(fixtures['misread']['fixtures']),'recomputed_D3_fixture_rows':fixtures['misread']['recomputed_D3_fixture_rows'],'rounding_counts':fixtures['rounding']['flip_counts'],'no_real_rote_score':'0/3'},'limits':'No domains changed. No generated runtime items, marker, app renderer or independent review acceptance.'}
 for path,obj in [(W/'planning/d4/trig-d4-fixtures.json',fixtures),(W/'checks/plan-repair-d4-trig-validation.json',out)]:
  text=dump(obj)
  if args.check:assert path.read_text()==text,('stale D4 output',str(path))
  else:path.write_text(text)
 print(dump({'status':'pass','parts':n,'examples':len(cases),'misread_ledgers':len(fixtures['misread']['fixtures']),'recomputed_D3_fixture_rows':fixtures['misread']['recomputed_D3_fixture_rows'],'rounding_counts':fixtures['rounding']['flip_counts']}))
if __name__=='__main__':main()
