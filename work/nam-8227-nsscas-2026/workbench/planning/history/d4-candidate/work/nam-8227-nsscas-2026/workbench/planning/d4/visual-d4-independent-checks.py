"""Independent visual mathematics plus derived proposed D4 fixed-evidence ledgers.

This records explicit criterion evidence. It does not recognise submissions,
implement a runtime marker, generate questions or independently accept content.
"""
from pathlib import Path
from fractions import Fraction as F
from decimal import Decimal,ROUND_HALF_UP
import argparse,json,hashlib,subprocess,sys
import mpmath as m
from misread_ledger import award,settle
W=Path(__file__).resolve().parents[2];P=W/'planning';H=P/'d4';m.mp.dps=75
read=lambda p:json.loads(p.read_text())
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def theta(u,v):
 # Angle from Euclidean side lengths, independently of the canonical dot formula.
 uu,vv=dot(u,u),dot(v,v);diff=[x-y for x,y in zip(u,v)];dd=dot(diff,diff)
 return m.acos(m.mpf(uu+vv-dd)/(2*m.sqrt(uu*vv)))*180/m.pi
def fmt(x,n=3):
 d=Decimal(str(x));return str(d.quantize(Decimal(1).scaleb(d.adjusted()-n+1),rounding=ROUND_HALF_UP))if d else'0'
def vector_math(u,v,w):
 a,b=dot(u,w),dot(v,w);p=F(b,a)if a else None;angle=theta(u,v)
 if p is not None:assert dot([p*u[i]-v[i]for i in range(3)],w)==0
 return dict(p=str(p)if p is not None else None,linear_coefficient=a,linear_rhs=b,dot_uv=dot(u,v),norms_squared=[dot(u,u),dot(v,v)],angle_degrees=str(angle),angle_1dp=str(Decimal(str(angle)).quantize(Decimal('.1'),rounding=ROUND_HALF_UP)))
def vector_awards(bits,datum=None,basis='misread'):
 ids=['a:B1','a:M1','a:A1','b:B1','b:M1','b:M2','b:A1'];types=['B','M','A','B','M','M','A']
 return[award(i,i[0],t,bits[j],datum_ids=[datum]if datum else[],basis=basis)for j,(i,t)in enumerate(zip(ids,types))]
def trap_awards(bits,datum=None,parts_on_datum=None,basis='misread'):
 ids=['a:B1','a:M1','a:A1','b:B1','b:B2','c:B1','c:B2','c:B3','d:B1','d:DB1'];types=['B','M','A','B','B','B','B','B','B','DM']
 return[award(i,i[0],t,bits[j],datum_ids=[datum]if datum and i[0]in(parts_on_datum or'abcd')else[],depends_on=['d:B1']if i=='d:DB1'else[],basis=basis)for j,(i,t)in enumerate(zip(ids,types))]
def datum(id,eligible,first,reason):return dict(datum_id=id,eligible=eligible,first_use_part=first,reason=reason)
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--check',action='store_true');ap.add_argument('--negative-fixture',choices=['factorized-B1-lost','no-p-follow-through','free-later-misread']);args=ap.parse_args()
 doc=read(P/'visual-design.json');assert len(doc['recipes'])==3
 assert all(r['proposed_version']=='0.1.4'for r in doc['recipes'])
 assert sum(len(b['part_specs'])for r in doc['recipes']for b in r['branches'])==7
 assert all(q['bloom']['classification_version']=='8227-pilot-design-0.1.1'for r in doc['recipes']for b in r['branches']for q in b['part_specs'])
 old=read(P/'d3/visual-domain-checks.json');new=read(H/'visual-domain-checks.json')
 for a,b in zip(old['branches'],new['branches']):assert a['admitted']==b['admitted']and a['removed']==b['removed'],'unauthorised visual domain change'
 normal=vector_math([1,1,1],[-2,1,-1],[1,2,1]);assert normal['p']=='-1/4'and normal['angle_1dp']=='118.1'
 impossible=vector_math([1,-2,1],[-3,1,-1],[1,1,1]);assert impossible['linear_coefficient']==0 and impossible['linear_rhs']==-3 and impossible['angle_1dp']=='137.6'
 other=vector_math([1,1,1],[2,1,-1],[1,3,1]);assert other['p']=='4/5'
 width=m.mpf(2);nodes=[2,4,6]
 T=m.fsum([(nodes[i+1]-nodes[i])*(m.log(nodes[i]-1)+m.log(nodes[i+1]-1))/2 for i in range(2)])
 J=m.fsum([(nodes[i+1]-nodes[i])*(3*m.log((nodes[i]-1)**2)+3*m.log((nodes[i+1]-1)**2))/2 for i in range(2)])
 assert abs(J-6*T)<m.mpf('1e-70')and fmt(J)=='22.8'and Decimal('3.81')*6==Decimal('22.86')
 ledgers=[]
 def record(id,description,awards,datums,expected,math=None):
  result=settle(awards,datums);assert result['net_total']==expected,(id,result['net_total'],expected)
  ledgers.append(dict(case_id=id,description=description,mathematics=math,result=result))
 MR=datum('OB-x-sign',True,'a','Genuine copied question sign; nonzero vectors and same perpendicular linear solve/angle demand.')
 record('D4-VIS-MR01','D3 full correct OB sign-misread response; one net deduction, no second deduction in b.',vector_awards([1]*7,'OB-x-sign'),[MR],6,normal)
 record('D4-VIS-MR02','D3 learner own-dot miscopy after correct question data; ordinary canonical accuracy, no MR.',vector_awards([1,1,1,0,1,1,0],'own-dot',basis='canonical'),[datum('own-dot',False,'b','Learner own figures are ordinary accuracy errors, not question-data MR.')],5)
 no_p_datum=datum('OA-y-sign',False,'a','Canonical question has a unique p, but this misread makes the perpendicular equation 0p=-3; object changed. Eligibility remains false in b.')
 record('D4-VIS-MR03','D3 no-p first part only; dot-zero M1 demonstrated, no MR accuracy.',vector_awards([0,1,0,0,0,0,0],'OA-y-sign',basis='canonical'),[no_p_datum],1,impossible)
 record('D4-VIS-MR04','D3 no A/B anywhere on an eligible datum; M remains, no negative/borrowed penalty.',vector_awards([0,1,0,0,0,0,0],'OB-x-sign'),[MR],1)
 record('D4-VIS-MR05','D3 wrong resultant is a method error, not a copied question datum.',vector_awards([0,1,0,0,0,0,0]),[],1)
 k_datum=datum('k',True,'b','k=2 copied as 3; same factorised-square/log-law and hence-product demand; not an own-figure error.')
 record('D4-VIS-MR06','D3 k2→k3 with correct factorisation, log law and hence product, other parts complete.',trap_awards([1]*10,'k','b'),[k_datum],9,dict(T=str(T),misread_J=str(J),J_3sf=fmt(J),product_from_reported_a='22.86'))
 record('D4-VIS-MR07','D3 bare visible J=6T=6(11.5), no factorisation/log-law derivation; B2 only.',trap_awards([0,0,0,0,1,0,0,0,0,0]),[],1)
 # Retained D3 partial-question fixture, now an executable two-part ledger.
 aa=[award('a:B1','a','B',1,['datum']),award('a:M1','a','M',1,['datum']),award('a:A1','a','A',1,['datum']),award('b:B1','b','B',1,['datum']),award('b:B2','b','B',1,['datum'])]
 record('D4-VIS-MR08','D3 eligible datum reused across two parts; first earned A/B once, later gross accuracy remains.',aa,[datum('datum',True,'a','Fixed fully demonstrated two-part evidence, unchanged demand.')],4)
 record('D4-VIS-MR09','D3 wrong working plus unsupported answer; no credit is invented by misread treatment.',vector_awards([0]*7,'OB-x-sign'),[MR],0)
 combined=vector_awards([0,1,0,1,1,1,1],'OB-x-sign')
 record('D4-VIS-MR10','OB sign misread plus wrong p(OA-OB): a:M1 only; first earned A/B is b:B1, deduction moves to b.',combined,[MR],4,dict(wrong_resultant_equation='5p=0',wrong_p='0',later_angle_1dp=normal['angle_1dp']))
 # The ineligible datum never receives MR F.T. in the later part.
 no_p_awards=vector_awards([0,1,0,0,1,1,0],'OA-y-sign',basis='canonical')
 if args.negative_fixture=='no-p-follow-through':no_p_awards[3]['basis']='misread'
 record('D4-VIS-MR11','No-p misread reused in b: canonical a1/3 plus canonical b2/4, one settled outcome3/7.',no_p_awards,[no_p_datum],3,impossible)
 record('D4-VIS-MR12','k2→k3 but bare J=6T; B1 absent and only B2 earned, so that B2 pays MR−1; other parts complete.',trap_awards([1,1,1,0,1,1,1,1,1,1],'k','b'),[k_datum],8,dict(J_3sf=fmt(J),J_from_reported_a='22.86'))
 # OC does not enter the prescribed-resultant setup B1: the first A/B on OC is a:A1.
 oc_awards=vector_awards([1]*7)
 for i in [1,2]:oc_awards[i]['datum_ids']=['OC-y']
 record('D4-VIS-MR13','OC (1,2,1) copied as (1,3,1); setup unaffected, correct p4/5; deduction from first OC-dependent A/B a:A1.',oc_awards,[datum('OC-y',True,'a','Same linear perpendicular solve; the given vectors remain nonzero and the p solution unique.')],6,other)
 record('D4-VIS-MR14','Quadratic x²−2x+1 copied as x²−2x+4, no factorised square/hence route; object changed, b0/2 canonical, all other parts complete.',trap_awards([1,1,1,0,0,1,1,1,1,1],'quadratic','b',basis='canonical'),[datum('quadratic',False,'b','Canonical factorised square lost; changed object, no MR concession.')],8)
 # S04 is separate from MR: correct factorisation B1 stands, wrong-law work loses B2.
 factorized_seen=True;law_correct=False
 b1=int(factorized_seen);b2=int(law_correct)
 if args.negative_fixture=='factorized-B1-lost':b1=0
 assert b1==1 and b2==0,'Official factorised-form B1 was lost, or wrong-law B2 was awarded'
 record('D4-VIS-S04','Normal k2 numeric coincidence: 2ln((x−1)²)=2²ln(x−1), J=4T; factorisation B1 stands, wrong log-law B2 www fails.',trap_awards([1,1,1,b1,b2,1,1,1,1,1]),[],9,dict(wrong_scale=4,correct_scale=4,numeric_result_3sf=fmt(4*T)))
 if args.negative_fixture=='free-later-misread':
  broken=settle(combined,[MR]);assert broken['net_total']==5,'Later earned A/B correctly pays the misread deduction'
 # Full gross dependency survives a net deduction of its parent B.
 dep=settle([award('d:B1','d','B',1,['datum']),award('d:DB1','d','DM',1,['datum'],['d:B1'])],[datum('datum',True,'d','Fixed full evidence for the same own-curve reason; unchanged demand.')])
 assert dep['net_total']==1 and dep['dependency_evidence']['d:DB1']['d:B1']==1
 pool=[row for row in new['branches'][2]['admitted']if row['parameters']['h']!=2];exposure=[]
 for e in read(P/'visual-design-asset-checks.json')['exemplar_cases']:
  if not e['recipe_id'].endswith('trapezium-sketch-estimate'):continue
  row=next(q for q in pool if q['parameters']==e['parameters']);remaining=[q for q in pool if all(q['part_keys'][part]!=row['part_keys'][part]for part in'abcd')]
  assert remaining and len({r['parameters']['h']for r in remaining})==1
  exposure.append(dict(example=e['case_id'],remaining_presentations=len(remaining),strict_generated_fresh_packing_after_example=1))
 source=Path('Question Banks/Namibian Examiner Reports/NSSCAS/2023/NSSCAS_Examiners_Report_2023.pdf');render=P/'d1/root-source-pages/2023-337.png'
 result=dict(status='pass',scope=__doc__.strip(),version='0.1.4',classification_version='8227-pilot-design-0.1.1',visual_part_count=7,domains_unchanged=True,derived_ledgers=ledgers,gross_dependency_fixture=dep,generated_fresh_exposure_checks=exposure,source_read=dict(path=str(source),source_sha256=hashlib.sha256(source.read_bytes()).hexdigest(),pdf_page=337,printed_page=335,render_path=str(render),render_sha256=hashlib.sha256(render.read_bytes()).hexdigest(),verification='D4 visual planner viewed native page render: row04 awards factorised form alone; row05 uses6times own(a). B2 www is separately identified as the proposed D4 clarification, never falsely quoted as the official row04 condition.'),eligibility_limits='Modulus redundant-label/orientation conflicts and trapezium strip-count changes remain named E/F eligibility fixtures; no unreviewed judgement is silently settled here.')
 out=H/'visual-d4-independent-checks.json';text=json.dumps(result,indent=2,ensure_ascii=False)+'\n'
 if args.check:assert out.read_text()==text,('stale',str(out))
 else:out.write_text(text)
 print(json.dumps(dict(status='pass',derived_ledgers=len(ledgers),retained_D3_ledger_cases=9,visual_parts=7,vector_combined='4/7',vector_no_p='3/7',trap_k2_wrong_law='9/10')))
if __name__=='__main__':main()
