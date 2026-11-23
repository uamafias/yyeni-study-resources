"""R5 author source transcription,Exercise1C. Internal verification input."""
import json,hashlib
from pathlib import Path
W=Path(__file__).resolve().parents[2];ROOT=W.parents[2];rows=[]
def evidence(name):
 p=W/f'checks/r5/textbooks/{name}.png';return {'path':str(p.relative_to(ROOT)),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
def part(label,kind,operand,key,**kwargs):return {'subpart':label,'operation':{'kind':kind,'operands':[operand],**kwargs},'printed_key_normalised':key}
def add(n,note,parts):
 for p in parts:
  p.update(source_evidence=evidence('Goldie-C1-35'),key_evidence=evidence('Goldie-keys-C1'),answer_pdf_page=335 if n>=5 else 334,answer_printed_page=321 if n>=5 else 320)
  p.setdefault('method','Solve the independently transcribed absolute-value condition over realx,retain endpoint inclusion,and compare the exact printed answer.')
 row={'item_id':f'8227:TB:Goldie:C1:Exercise-1C:{n}','source_pdf_page':35 if n==1 else 36,'notes':note,'component_demand_ids':[],'expected_subpart_labels':[p['subpart']for p in parts],
 'exam_style':n>=6,'exam_style_basis':'Explicit Cambridge past-paper attribution.'if n>=6 else'No past-paper attribution or source exam-style heading.',
 'value_level_scope_decisions':[{'rule_id':'8227:QUAL01','status':'within'if n==4 else'not applicable','quoted_value':'; '.join(p['operation']['operands'][0]for p in parts),
 'reason':'Every requested modulus graph has integer linear/translation coefficients.'if n==4 else'This item asks equations,inequalities or interval-to-modulus conversion,not a modulus graph; graph-coefficient QUAL01does not apply to its fractional bounds or parameter.'}],
 'subparts':parts};rows.append(row);return row
romans=['i','ii','iii','iv','v','vi','vii','viii','ix']
questions=['Abs(x+4)-5','Abs(x-3)-4','Abs(3-x)-4','Abs(4*x-1)-7','Abs(2*x+1)-5','Abs(8-2*x)-6','Abs(2*x+1)-Abs(x+5)','Abs(4*x-1)-Abs(9-x)','Abs(3*x-2)-Abs(4-x)']
keys=['FiniteSet(-9,1)','FiniteSet(7,-1)','FiniteSet(-1,7)','FiniteSet(-3/2,2)','FiniteSet(-3,2)','FiniteSet(1,7)','FiniteSet(-2,4)','FiniteSet(-8/3,2)','FiniteSet(-1,3/2)']
r=add(1,'Solve six single-modulus linear equations and three equations comparing two moduli,retaining every real branch.',[part(l,'real-roots',q,k)for l,q,k in zip(romans,questions,keys)])
r['assessed_8227_demand_ids']=['8227:2020:M2:T1:O01:D02']
questions=['Abs(x+3)<5','Abs(x-2)<=2','Abs(x-5)>6','Abs(x+1)>=2','Abs(2*x-3)<7','Abs(3*x-2)<=4']
keys=['Interval.open(-8,2)','Interval(0,4)','Union(Interval.open(-oo,-1),Interval.open(11,oo))','Union(Interval(-oo,-3),Interval(1,oo))','Interval.open(-2,5)','Interval(-2/3,2)']
r=add(2,'Solve six one-modulus inside/outside inequalities with strict or inclusive endpoints and scaled linear arguments.',[part(l,'inequality',q,k)for l,q,k in zip(romans,questions,keys)]);r['assessed_8227_demand_ids']=['8227:2020:M2:T1:O01:D03']
bounds=[('-1','3','1','2'),('2','8','5','3'),('-2','4','1','3'),('-1','6','5/2','7/2'),('99/10','101/10','10','1/10'),('1/2','15/2','4','7/2')]
parts=[]
for lab,(a,b,c,d)in zip(romans,bounds):
 p=part(lab,'identity',f'Tuple((({a})+({b}))/2,(({b})-({a}))/2)',f'Tuple({c},{d})');p['method']='Find the interval midpointaand half-widthb; write|x-a|<bwith both strict endpoints retained.';p['source_interval_endpoints']=[a,b];p['derived_answer_form']=f'Abs(x-({c}))<({d})';parts.append(p)
r=add(3,'Convert six open intervals to|x-a|<b,including half-integer and decimal endpoints; this is an inverse representation task,not another forward solve.',parts);r['assessed_8227_demand_ids']=['8227:2020:M2:T1:O01:D03']
graphs=[('1','2','0','Tuple(-2,0)','2','FiniteSet(-2)'),('2','-3','0','Tuple(3/2,0)','3','FiniteSet(3/2)'),('1','2','-2','Tuple(-2,-2)','0','FiniteSet(-4,0)'),('1','0','1','Tuple(0,1)','1','FiniteSet()'),('2','5','-4','Tuple(-5/2,-4)','1','FiniteSet(-9/2,-1/2)'),('1','-2','3','Tuple(2,3)','5','FiniteSet()')]
parts=[]
for lab,(a,b,c,vertex,intercept,roots)in zip(romans,graphs):
 parts.append({'subpart':lab,'operation':{'kind':'modulus-sketch','operands':[a,b,c]},'printed_key_features':{'vertex':vertex,'y_intercept':intercept,'x_intercepts':roots},'method':'For y=|ax+b|+c,derive vertex(-b/a,c),intercepts and both branch slopes; visually compare the rendered key sketch.'})
r=add(4,'Sketch six translated/scaled V-graphs on separate axes; verify vertices,intercepts,slopes and absence of x-intercepts when the minimum is positive.',parts);r['assessed_8227_demand_ids']=['8227:2020:M2:T1:O02:D01']
questions=['Abs(x+3)<Abs(x-4)','Abs(x-5)>Abs(x-2)','Abs(2*x-1)<=Abs(2*x+3)','Abs(2*x)<=Abs(x+3)','Abs(2*x)>Abs(x+3)','Abs(2*x+5)>=Abs(x-1)']
keys=['Interval.open(-oo,1/2)','Interval.open(-oo,7/2)','Interval(-1/2,oo)','Interval(-1,3)','Union(Interval.open(-oo,-1),Interval.open(3,oo))','Union(Interval(-oo,-6),Interval(-4/3,oo))']
r=add(5,'Compare two moduli in six inequalities; squaring is order-preserving for both nonnegative sides,and and/or plus endpoint inclusion must be retained.',[part(l,'inequality',q,k)for l,q,k in zip(romans,questions,keys)]);r['assessed_8227_demand_ids']=['8227:2020:M2:T1:O01:D03']
r=add(6,'Solve|x|>|3x-2|and retain the strict inside interval between the two crossings.',[part('answer','inequality','Abs(x)>Abs(3*x-2)','Interval.open(1/2,1)')]);r['assessed_8227_demand_ids']=['8227:2020:M2:T1:O01:D03']
r=add(7,'Givena>0,solve|x-3a|>|x-a|by comparing distances to the midpoint2a; the printed key reverses the required half-line.',[part('answer','inequality','Abs(x-3*a)>Abs(x-a)','Interval.open(2*a,oo)',parameters_positive=['a'])]);r['assessed_8227_demand_ids']=['8227:2020:M2:T1:O01:D03'];r['subparts'][0]['method']='For positivea,square both nonnegative sides: (x-3a)^2-(x-a)^2=4a(2a-x)>0,sox<2a; checkx=0satisfies original and is excluded by the printed key.'
r=add(8,'Solve|3x+4|=|2x+5|using both equal-sign and opposite-sign linear branches.',[part('answer','real-roots','Abs(3*x+4)-Abs(2*x+5)','FiniteSet(1,-9/5)')]);r['assessed_8227_demand_ids']=['8227:2020:M2:T1:O01:D02']
r=add(9,'Solve|x^3-14|=13by the two exact cubic equations; this extends the inner expression without adding a modulus-graph coefficient claim.',[part('answer','real-roots','Abs(x**3-14)-13','FiniteSet(1,3)')]);r['assessed_8227_demand_ids']=['8227:2020:M2:T1:O01:D02'];r['component_demand_ids']=['8227:2020:M2:T1:O04:D04']

for row in rows:
    n=int(row['item_id'].rsplit(':',1)[1])
    if n==4:
        row['value_level_scope_decisions'][0]['quoted_value']='; '.join(f'y=|({a})x+({b})|+({c})'for part in row['subparts']for a,b,c in [part['operation']['operands']])
    if n==3:row['direct_demand_aspects']={'8227:2020:M2:T1:O01:D03':'Reverse interval-to-modulus representation; not a full forward solve of an arbitrary modulus inequality.'}
    if n==7:
        row['value_level_scope_decisions'][0]['quoted_value']='a>0; |x-3a|>|x-a|'
        row['subparts'][0].update(source_evidence=evidence('Goldie-question-1C7'),key_evidence=evidence('Goldie-key-1C7'))
    row['precision_angle_check']={'source_pdf_page':333,'source_printed_page':319,'book_default':'Non-exact numerical answers3significant figures; degree angles1decimalplace unless specified; avoid intermediate rounding.','item_application':'Exact algebraic,interval or graph features; no rounding or angle conversion required.','NSSCAS_convention_ids':['8227:CONVENTION:003','8227:CONVENTION:004'],'conflict':'none for this item'}
if __name__=='__main__':
 (W/'tools/textbook-r5/answers-Goldie-1C.json').write_text(json.dumps({'scope':'All9Exercise1Cquestion blocks;37explicit subparts. Question4sketches(i)–(iii)keyonPDF334and(iv)–(vi)also onPDF334; allare visually read.','items':rows},ensure_ascii=False,indent=2)+'\n');print(len(rows),'question records')
