"""D3 finite design/oracle checks. Does not emit runtime questions or grade attempts."""
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
 # Hand-specified criterion awards are design expectations, not outputs from a marker.
 def row(id,part,raw,eligible,first=True,datum='one copied question datum',treatment='genuine misread, same object and difficulty',working=True):
  marks=dict(raw);ded=next((x for x in eligible if marks[x]>0),None)if first else None
  if ded:marks[ded]-=1
  assert min(marks.values(),default=0)>=0
  return dict(fixture_id=id,part=part,datum=datum,treatment=treatment,visible_correct_working=working,raw_awards=raw,deducted_from=ded,final_awards=marks,total=sum(marks.values()),runtime_marker_tested=False)
 rows=[]
 assert sp.asin(5*(-sp.Rational(1,10)))==-sp.pi/6
 rows.append(row('PI-k4-copied-as5','p-decision',{'P-B1':1,'P-M1':1,'P-A1':1},['P-B1','P-A1']))
 # Misread theta converts no-solution to solution; canonical obstruction credit is absent.
 forced=-sp.sqrt(2)/6;assert sp.asin(3*forced)==-sp.pi/4
 rows.append(row('PI-no-solution-changed-to-real','p-decision',{'P-B1':0,'P-M1':0,'P-A1':0},[],treatment='No OD-6: changed decision/object and easier real-solution task; normal canonical marking'))
 rows.append(row('PI-own-figure-error','p-decision',{'P-B1':1,'P-M1':1,'P-A1':0},[],treatment='No OD-6: correct 4x=-1/2 followed by own-figure slip; normal accuracy marking'))
 # Independent half-angle polynomial compared with shifted-sine route on misread a.
 R,al,be,rs=old.roots_phase(4,3,1);ind=half_angle(4,3,1)
 assert len(ind)==2 and all(abs(x-y)<mp.mpf('1e-60')for x,y in zip(rs,ind))
 assert d2.sig(rs)==['131.6','334.7']
 rows.append(row('RF-coefficient2-copied-as4-a','a-convert',{'a-B1':1,'a-M1':1,'a-A1':1},['a-B1','a-A1']))
 rows.append(row('RF-same-coefficient-later-b','b-roots',{'b-M1':1,'b-M2':1,'b-A1':1,'b-A2':1},['b-A1','b-A2'],first=False))
 rows.append(row('RF-method-only-no-AB','a-convert',{'a-B1':0,'a-M1':1,'a-A1':0},['a-B1','a-A1']))
 assert 9>R
 rows.append(row('RF-misread-c1-as9-no-solution','b-roots',{'b-M1':1,'b-M2':0,'b-A1':0,'b-A2':0},[],treatment='No OD-6: altered task leaves no real roots; canonical rubric, visible reduction only'))
 # Copying c=1 as3 retains three-criterion transformation/gradient/recovery and two-criterion hence work.
 a=sp.Integer(8);x=-sp.Rational(14,3);assert sp.simplify(2**(3*a)*a**x-2**10)==0
 rows.append(row('LOG-c1-copied-as3-a','t-parameter',{'T-B1':1,'T-M1':1,'T-A1':1},['T-B1','T-A1']))
 rows.append(row('LOG-same-c-later-b','t-target',{'U-M1':1,'U-A1':1},['U-A1'],first=False))
 x=-sp.Rational(4,3);assert sp.simplify(2**a*a**x-2**4)==0
 rows.append(row('LOG-target10-copied-as4-first-use-b','t-target',{'U-M1':1,'U-A1':1},['U-A1']))
 rows.append(row('OD1-bare-misread-answer','p-decision',{'P-B1':0,'P-M1':0,'P-A1':0},['P-B1','P-A1'],working=False))
 rows.append(row('RF-inverted-ratio-is-named-error','a-convert',{'a-B1':1,'a-M1':0,'a-A1':0},[],treatment='No OD-6: inverted phase ratio is a named method error, not copied question data'))
 # Genuine copied coefficient plus an independent inverted-ratio mistake: MR does not repair wrong working.
 wrong_al=mp.degrees(mp.atan2(4,3));wrong_roots=d2.shifted(5,wrong_al,1)
 assert d2.sig(wrong_roots)!=d2.sig(rs)
 rows.append(row('RF-copied-coefficient-plus-inverted-ratio-a','a-convert',{'a-B1':1,'a-M1':0,'a-A1':0},['a-B1','a-A1'],treatment='Genuine copied coefficient qualifies, but named inverted-ratio work still loses method/accuracy; MR-1 removes the earned B1'))
 rows.append(row('RF-copied-coefficient-plus-inverted-ratio-b','b-roots',{'b-M1':1,'b-M2':1,'b-A1':0,'b-A2':0},['b-A1','b-A2'],first=False,treatment='Same copied datum: no second deduction; own-interval method survives, wrong-phase accuracy is not rescued'))
 return {'fixtures':rows,'misread_rform_independent_roots_degrees':[str(v)for v in ind],'unit':'One deduction per datum in its first-use part. If no A/B earned there, no deduction and no later deferred penalty. Later reuse is F.T. without repeat. Earliest eligible earned A/B unless actual scheme specifies order.','scope':'Mathematics independently recomputed; criterion awards are declared design expectations, not marker results.'}
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--check',action='store_true');args=ap.parse_args();doc=read(W/'planning/trig-model-design.json')
 r,rd=old.rform();p,pd=old.principal();g,gd=old.graph();t,td=old.gradient();cases=old.cases(doc,rd,pd,gd,td)
 assert doc['version']=='0.1.3';n=0
 for rec in doc['recipes']:
  assert rec['proposed_version']=='0.1.3'
  for b in rec['branches']:
   assert b['classification_version']=='8227-pilot-design-0.1.1'and sum(x['marks']for x in b['part_specs'])==b['marks_total']
   for part in b['part_specs']:
    n+=1;policy=part['misread_policy'];assert 'OD-6' in policy and 'earliest eligible earned A/B' in policy and 'no repeat deduction' in policy and 'OD-1' in policy
    assert part['answer_only_marks']==0 and sum(x['value']for x in part['criteria'])==part['marks']
 assert n==6
 ss=read(W/'planning/trig-model-source-reads.json');pairs=[]
 for group in [ss['readings'],ss['repair_d1']['readings'],ss['repair_d2']['readings'],ss['repair_d3']['readings']]:
  for entry in group:
   for pk,hk in [('source_path','source_sha256'),('render_path','render_sha256')]:assert hashlib.sha256(Path(entry[pk]).read_bytes()).hexdigest()==entry[hk]
   pairs.append((entry['source_path'],entry['pdf_page']))
 fixtures={'rounding':precision(rd),'misread':misreads(),'principal_no_real_rote_only':{'response':'range is [-pi/2,pi/2]; no real solution','actual_target_comparison':False,'awards':{'P-B1':0,'P-M1':0,'P-A1':0},'total':0,'out_of':3},'later_runtime_status':'All acceptance fixtures pending E/F; no runtime generator/marker tested.'}
 out={'status':'pass; D3 author-side finite design checks, not independent acceptance/runtime validation','recipe_version':'0.1.3','classification_version':'8227-pilot-design-0.1.1','branches':{'degree-cycle':r,'solve-or-explain':p,'graph-intercept':g,'gradient-target':t},'exemplar_checks':cases,'parts':n,'source_render_pairs':len(pairs),'unique_source_pages':len(set(pairs)),'D3_rendered_pages':2,'fixture_summary':{'misread_rows':len(fixtures['misread']['fixtures']),'rounding_counts':fixtures['rounding']['flip_counts'],'no_real_rote_score':'0/3'},'limits':'No domains changed. No generated runtime items, marker, app renderer or independent review acceptance.'}
 for path,obj in [(W/'planning/d3/trig-d3-fixtures.json',fixtures),(W/'checks/plan-repair-d3-trig-validation.json',out)]:
  text=dump(obj)
  if args.check:assert path.read_text()==text,('stale D3 output',str(path))
  else:path.write_text(text)
 print(dump({'status':'pass','parts':n,'examples':len(cases),'misread_rows':len(fixtures['misread']['fixtures']),'rounding_counts':fixtures['rounding']['flip_counts']}))
if __name__=='__main__':main()
