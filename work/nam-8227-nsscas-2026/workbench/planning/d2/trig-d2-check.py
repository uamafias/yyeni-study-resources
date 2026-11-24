"""Stage-D D2 design/oracle/precision fixtures. No runtime items or marker emitted."""
from pathlib import Path
from decimal import Decimal,ROUND_HALF_UP
import argparse,hashlib,importlib.util,json,math,collections
import mpmath as mp
import sympy as sp
W=Path(__file__).resolve().parents[2]
spec=importlib.util.spec_from_file_location('d1_trig',W/'planning/d1/trig-discrimination-check.py');old=importlib.util.module_from_spec(spec);spec.loader.exec_module(old)
mp.mp.dps=80

def read(p):return json.loads(p.read_text())
def fmt(x,dp=1):return str(Decimal(str(x)).quantize(Decimal(1).scaleb(-dp),rounding=ROUND_HALF_UP))
def sig(xs):return sorted(fmt(x)for x in xs)
def same(x,y):return abs(mp.mpf(x)-mp.mpf(y))<mp.mpf('1e-50')
def shifted(R,alpha,c):
 if R<=0:return None
 if abs(c/R)>1:return []
 beta=mp.degrees(mp.asin(c/R));eps=mp.mpf('1e-55')
 values=[]
 for k in range(-2,4):
  for z in [beta+360*k,180-beta+360*k]:
   x=z-alpha
   if eps<x<360-eps and not any(abs(x-v)<eps for v in values):values.append(x)
 return sorted(values)
def numeric_oracle(R,alpha,c):
 # Independent bracket-and-bisect search in theta. The analytic solver above
 # enumerates sine families; this one checks the transformed function itself.
 f=lambda x:R*mp.sin(mp.radians(x+alpha))-c
 roots=[]
 def put(x):
  if mp.mpf('1e-50')<x<360-mp.mpf('1e-50') and not any(abs(x-v)<mp.mpf('1e-40')for v in roots):roots.append(x)
 for a in range(360):
  lo=mp.mpf(a);hi=mp.mpf(a+1);fl=f(lo);fh=f(hi)
  if abs(fl)<mp.mpf('1e-65'):put(lo)
  if fl*fh<0:
   for _ in range(225):
    mid=(lo+hi)/2;fm=f(mid)
    if fl*fm<=0:hi=mid
    else:lo=mid;fl=fm
   put((lo+hi)/2)
 return sorted(roots)
def decimal_two_angle_roots(al,be):
 a=Decimal(fmt(al,2));b=Decimal(fmt(be,2));out=set()
 for k in range(-2,4):
  for z in [b+360*k,Decimal(180)-b+360*k]:
   x=z-a
   if 0<x<360:out.add(x)
 return sorted(out)

def rform_precision(domain):
 ft=[];class_changes=[];endpoints=[];rounding=collections.defaultdict(list);ties=[];amplitude_only_collisions=[]
 for a,b,c in domain:
  R,al,be,canon=old.roots_phase(a,b,c);own=mp.degrees(mp.atan2(a,b));ownroots=shifted(R,own,c);oracle=numeric_oracle(R,own,c)
  assert len(oracle)==len(ownroots)and all(same(x,y)for x,y in zip(oracle,ownroots))
  ownz=[x+own for x in ownroots];canonz=[x+al for x in canon]
  if len(ownz)==2 and any(not same(x,y)for x,y in zip(ownz,canonz)):class_changes.append([a,b,c])
  if c==a:
   assert same(own,be)and len(ownroots)==1;endpoints.append([a,b,c])
   ft.append(dict(tuple=[a,b,c],wrong_alpha=str(own),eligible_transformed_roots=[str(x)for x in ownz],eligible_original_roots=[str(x)for x in ownroots],rejected_original_endpoint='0',bM1=1,bM2_if_complete_with_endpoint_rejected=1,bM2_if_endpoint_retained=0,accuracy='Canonical c.a.o. only; not inferred from own-root F.T.',independent_oracle='bracketed transformed sine search agrees'))
  elif [a,b,c]in class_changes:
   ft.append(dict(tuple=[a,b,c],wrong_alpha=str(own),canonical_transformed_roots=[str(x)for x in canonz],eligible_own_transformed_roots=[str(x)for x in ownz],eligible_own_original_roots=[str(x)for x in ownroots],bM2_if_own_interval_complete=1,independent_oracle='bracketed transformed sine search agrees'))
  R3=mp.mpf(mp.nstr(R,3));R4=mp.mpf(mp.nstr(R,4));ratio3=mp.mpf(mp.nstr(c/R,3))
  paths={'alpha_1dp':shifted(R,mp.mpf(fmt(al,1)),c),'beta_1dp':sorted({v-al for k in range(-2,4)for v in [mp.mpf(fmt(be,1))+360*k,180-mp.mpf(fmt(be,1))+360*k]if 0<v-al<360}),'R_3sf':shifted(R3,al,c),'R_4sf':shifted(R4,al,c),'ratio_3sf':sorted({v-al for k in range(-2,4)for v in [mp.degrees(mp.asin(ratio3))+360*k,180-mp.degrees(mp.asin(ratio3))+360*k]if 0<v-al<360}),'alpha_acos_from_R_3sf_beta_exact':shifted(R,mp.degrees(mp.acos(a/R3)),c),'alpha_and_beta_from_R_3sf':shifted(R3,mp.degrees(mp.acos(a/R3)),c)}
  for name,roots in paths.items():
   if sig(roots)!=sig(canon):rounding[name].append(dict(tuple=[a,b,c],canonical_1dp=sig(canon),premature_1dp=sig(roots)))
  both=decimal_two_angle_roots(al,be);assert sorted(fmt(x)for x in both)==sig(canon)
  if any(x*10%1==Decimal('.5')for x in both):ties.append(dict(tuple=[a,b,c],two_dp_intermediate_roots=[str(x)for x in both],half_up_1dp=[fmt(x)for x in both],canonical_1dp=sig(canon)))
  if sig(shifted(mp.mpf(a+b),al,c))==sig(canon):amplitude_only_collisions.append([a,b,c])
 assert len(class_changes)==6 and len(endpoints)==8 and len(ties)==4
 assert len(rounding['alpha_1dp'])==38 and len(rounding['R_3sf'])==15
 assert len(amplitude_only_collisions)==10 and all(c==0 for a,b,c in amplitude_only_collisions)
 phases=[]
 for a,b in [(3,1),(1,3)]:
  R=mp.sqrt(a*a+b*b);R6=mp.mpf(mp.nstr(R,6));actual=mp.degrees(mp.atan2(b,a));via=mp.degrees(mp.acos(a/R6))
  phases.append(dict(a=a,b=b,R_6sf=str(R6),canonical_alpha=str(actual),via_rounded_amplitude=str(via),canonical_2dp=fmt(actual,2),via_rounded_amplitude_2dp=fmt(via,2)))
 # All named wrong root strategies are compared at the actual marked precision.
 collisions=collections.defaultdict(list)
 for a,b,c in domain:
  R,al,be,canon=old.roots_phase(a,b,c)
  bad={'inverted_phase_ratio':shifted(R,mp.degrees(mp.atan2(a,b)),c),'radian_phase_read_as_degrees':shifted(R,mp.atan2(b,a),c),'forget_phase_subtraction':[x+al for x in canon],'second_root_180_minus_final_first':[canon[0],180-canon[0]],'principal_root_only':[be-al]}
  for name,rs in bad.items():
   if sig(rs)==sig(canon):collisions[name].append([a,b,c])
 assert not any(collisions.values())
 return dict(class_change_tuples=class_changes,endpoint_tuples=endpoints,follow_through_fixtures=ft,marked_precision_wrong_root_collisions=dict(collisions),amplitude_sum_b_only_coincidences=amplitude_only_collisions,amplitude_coincidence_disclosure='The 10 zero-target equations do not use R in part (b); wrong R still loses exact amplitude B1 in (a). They are non-diagnostic for amplitude by the roots alone.',premature_rounding_flip_sets=dict(rounding),rounding_flip_counts={k:len(v)for k,v in rounding.items()},both_2dp_half_up_ties=ties,phase_via_R_6sf_cases=phases,review_comparison={'phase_1dp':'38/58 agrees','R_3sf':'15/58 agrees','arccos_path':'33/58 agrees when both alpha and beta use the 3 s.f. R; an isolated alpha error with beta exact gives 34.','ratio_3sf':'14/58 computed with 80-digit mpmath and independent Python math; review reported 10 without persisted code/path definition. These explicit fixtures are for confirmation; agreement is not claimed.'},policy='Round-half-up at marked precision; M/DM survives an accuracy-only rounding error. Fixtures are proposed E/F marker expectations, not a runtime pass.')

def decision_fixtures(doc):
 inv=next(r for r in doc['recipes']if r['recipe_id'].endswith('principal-inverse'));part=inv['branches'][0]['part_specs'][0];cs={c['local_criterion_id']:c for c in part['criteria']}
 assert 'actual target' in cs['P-B1']['what_earns_it']and 'rote interval line alone is insufficient' in cs['P-B1']['what_earns_it']
 assert 'without the separate B1' in cs['P-M1']['what_earns_it']
 assert inv['branches'][0]['conditional_metadata_visibility'].startswith('Resolved instance-specific')
 theta=-sp.pi/6;x=-sp.Rational(1,8);assert -sp.pi/2<theta<sp.pi/2 and sp.asin(4*x)==theta
 forced=sp.sin(-3*sp.pi/4);actual=sp.asin(forced);assert actual==-sp.pi/4 and actual!=-3*sp.pi/4
 dec=mp.asin(mp.mpf('-.7071'));target=-3*mp.pi/4;assert abs(dec-target)>mp.mpf('1.5')
 assert 2*sp.pi/3>sp.pi/2
 log=next(r for r in doc['recipes']if r['recipe_id'].endswith('log-linear-model'));targetp=log['branches'][1]['part_specs'][1];um=targetp['criteria'][0];assert 'earlier' in um['qualifier']or 'previously' in um['qualifier']
 a=8;canonical=sp.Rational(10-a,3);wrong=sp.Rational(10,3);assert canonical==sp.Rational(2,3)and wrong!=canonical
 rows=[dict(id='PI-rote-interval-plus-forward',expected={'P-B1':0,'P-M1':1,'P-A1':1},reason='Actual target never compared or inverse-verified'),dict(id='PI-actual-target-comparison-plus-forward',expected={'P-B1':1,'P-M1':1,'P-A1':1},reason='Actual -pi/6 inside principal interval'),dict(id='PI-inverse-verification',expected={'P-B1':1,'P-M1':1,'P-A1':1},reason='Actual inverse of recovered x verifies target'),dict(id='PI-implicit-outside-bound',expected={'P-B1':1,'P-M1':1,'P-A1':1},reason='2pi/3>pi/2 shows and uses the relevant principal bound'),dict(id='PI-decimal-forced-candidate-contradiction',expected={'P-B1':1,'P-M1':1,'P-A1':1},reason='Principal inverse -0.7854 is decisively not target -2.3562; forced candidate identified'),dict(id='LOG-own-earlier-prefactor-omission',expected={'T-B1':0,'T-M1':1,'T-A1':1,'U-M1':1,'U-A1':0},reason='Earlier own line reused coherently; x10/3 rather than canonical2/3'),dict(id='LOG-new-prefactor-omission-only-in-b',expected={'T-B1':1,'T-M1':1,'T-A1':1,'U-M1':0,'U-A1':0},reason='New error in substitution cannot claim earlier-line F.T.')]
 return dict(expectations=rows,independent_math_checks='Exact inverse and direct-power substitution verified; robust decimal mismatch verified at80digits.',scope='Manually specified criterion expectations with independent mathematical checks. No runtime marker is implemented or tested.')

def records(doc):
 ss=read(W/'planning/trig-model-source-reads.json');reads=ss['readings']+ss['repair_d1']['readings']+ss['repair_d2']['readings'];verified=0
 for r in reads:
  for path,h in [('source_path','source_sha256'),('render_path','render_sha256')]:assert hashlib.sha256(Path(r[path]).read_bytes()).hexdigest()==r[h]
  verified+=1
 for r in doc['recipes']:
  assert r['proposed_version']=='0.1.2'
  for b in r['branches']:
   assert b['classification_version']=='8227-pilot-design-0.1.1'
   assert sum(p['marks']for p in b['part_specs'])==b['marks_total']
   for p in b['part_specs']:
    assert p['classification_version']=='8227-pilot-design-0.1.1'and p['answer_only_marks']==0
    assert sum(c['value']for c in p['criteria'])==p['marks']
 return dict(source_render_pairs=verified,unique_source_page_pairs=len({(r['source_path'],r['pdf_page'])for r in reads}),reading_count_note='Source/render pairs counts checked reading entries, including repeat readings; unique source pages counted separately.',new_D2_rereads=len(ss['repair_d2']['readings']),classification='8227-pilot-design-0.1.1',recipe_versions='0.1.2',bare_answers=0)
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--check',action='store_true');args=ap.parse_args();doc=read(W/'planning/trig-model-design.json')
 r,rd=old.rform();p,pd=old.principal();g,gd=old.graph();t,td=old.gradient();cases=old.cases(doc,rd,pd,gd,td);ft=rform_precision(rd);dec=decision_fixtures(doc);rec=records(doc)
 out=dict(status='pass; D2 author-side design checks, not runtime or independent acceptance',subject='NSSCAS Mathematics8227',recipe_version='0.1.2',classification_version='8227-pilot-design-0.1.1',branches={'degree-cycle':r,'solve-or-explain':p,'graph-intercept':g,'gradient-target':t},exemplar_checks=cases,record_checks=rec,criterion_fixtures=dec)
 paths={W/'checks/plan-repair-d2-trig-validation.json':out,W/'planning/d2/trig-d2-fixtures.json':ft}
 for f,o in paths.items():
  text=json.dumps(o,indent=2)+'\n'
  if args.check:assert f.read_text()==text,('D2 check artifact stale',str(f))
  else:f.write_text(text)
 print(json.dumps(dict(status='pass',branches=4,cases=len(cases),source_render_pairs=rec['source_render_pairs'],class_change_cases=len(ft['class_change_tuples']),endpoint_cases=len(ft['endpoint_tuples']),half_up_ties=len(ft['both_2dp_half_up_ties']),rounding_flip_counts=ft['rounding_flip_counts']),indent=2))
if __name__=='__main__':main()
