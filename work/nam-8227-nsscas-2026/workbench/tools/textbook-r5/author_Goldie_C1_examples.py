"""Rendered-source transcriptions of Goldie C1 examples; internal answer checking."""
import json
import hashlib
from pathlib import Path
W=Path(__file__).resolve().parents[2]
ROOT=W.parents[2]
rows=[]
def evidence(page):
    start=15+4*((page-15)//4)
    path=W/f'checks/r5/textbooks/Goldie-C1-{start}.png'
    return {'path':str(path.relative_to(ROOT)),'sha256':hashlib.sha256(path.read_bytes()).hexdigest()}
def part(label,kind,operands,key=None,**kwargs):
    if isinstance(operands,str):operands=[operands]
    result={'subpart':label,'operation':{'kind':kind,'operands':operands,**kwargs}}
    if key is not None:result['printed_key_normalised']=key
    return result
def add(n,page,note,parts,key_page=None):
    key_page=key_page or page
    for p in parts:
        p.update(source_evidence=evidence(page),key_evidence=evidence(key_page),answer_pdf_page=key_page,answer_printed_page=key_page-14)
        p.setdefault('method','Recompute from the question operands; compare the inline worked answer independently of its arithmetic steps.')
    row={'item_id':f'8227:TB:Goldie:C1:Example:{n}','source_pdf_page':page,'notes':note,
      'component_demand_ids':[],'expected_subpart_labels':[p['subpart']for p in parts],'exam_style':False,
      'exam_style_basis':'Numbered teaching example,not labelled as a past-paper or exam-style question.',
      'value_level_scope_decisions':[{'rule_id':'8227:LIMIT05','status':'not applicable','quoted_value':'; '.join(p['operation']['operands'][0]for p in parts),'reason':'No polynomial division is requested in this item; any later component limits are recorded explicitly.'}],
      'precision_angle_check':{'source_pdf_page':333,'book_default':'Non-exact results3significant figures; degree angles1decimalplace; no intermediate rounding.','item_application':'Exact algebraic/interval/graph answers; no angle units involved.','NSSCAS_convention_ids':['8227:CONVENTION:003','8227:CONVENTION:004'],'conflict':'none for the checked exact answer'},'subparts':parts}
    rows.append(row)
    return row
add(1,16,'Add two given quartics in aligned columns or by collecting like powers; the missing x^2term in the first operand must be retained as zero.',[part('answer','expand','(5*x**4-3*x**3-2*x)+(7*x**4+5*x**3+3*x**2-2)','12*x**4+2*x**3+3*x**2-2*x-2')])
add(2,17,'Subtract a quartic from another quartic; reverse every subtrahend sign,including its negative constant.',[part('answer','expand','(5*x**4-3*x**3-2*x)-(7*x**4+5*x**3+3*x**2-2)','-2*x**4-8*x**3-3*x**2-2*x+2')])
add(3,17,'Multiply cubic x^3+3x-2by quadratic x^2-2x-4; both column multiplication and direct expansion give a quintic. LIMIT05does not limit multiplication degree.',[part('answer','expand','(x**3+3*x-2)*(x**2-2*x-4)','x**5-2*x**4-x**3-8*x**2-8*x+8')])
f='2*x**3-3*x**2+x-6'
r=add(4,18,'Divide a cubic by x-2with zero remainder; long division,coefficient matching against an identity,and inspection are valid worked alternatives.',[part('quotient','quotient',[f,'x-2'],'2*x**2+x+3'),part('remainder','remainder',[f,'x-2'],'0')])
r['value_level_scope_decisions'][0].update(status='within',quoted_value='(2x^3-3x^2+x-6) divided by(x-2)',reason='Actual dividend degree3and divisor degree1.')
r['alternative_method_check']='All three displayed methods establish the same identity (x-2)(2x^2+x+3)=2x^3-3x^2+x-6; separate stage pages18–19were read.'
r=add(5,21,'Solve4x^3-8x^2-x+2=0; the book starts with a plotted value table then confirms the three exact roots by substitution/factors.',[part('answer','real-roots','4*x**3-8*x**2-x+2','FiniteSet(-1/2,1/2,2)')],key_page=22)
r['assessed_8227_demand_ids']=['8227:2020:M2:T1:O04:D04'];r['component_demand_ids']=['8227:2020:M2:T1:O04:D02']
r['mapping_rationale']='The learner is asked to solve the cubic; factor-theorem use and plotting in the worked solution are methods,not additional requested responses.'
f='x**3-6*x**2+11*x-6'
sketch=part('iv','polynomial-sketch',f);sketch['printed_key_features']={'labelled_x_intercepts':['1','2','3']}
add(6,23,'Evaluate five given inputs,then factor,solve and sketch x^3-6x^2+11x-6using its three successive positive roots and intercept-6.',[part('i','evaluate-list',f,'Tuple(-6,0,0,0,6)',at=['0','1','2','3','4']),part('ii','factor',f,'(x-1)*(x-2)*(x-3)'),part('iii','real-roots',f,'FiniteSet(1,2,3)'),sketch])
p=part('i','identity','(x**3-x**2-3*x+2).subs(x,2)','0');p['check_mode']='show/prove'
r=add(7,24,'Establish supplied factorx-2,then solve the remaining irrational quadratic in x^3-x^2-3x+2. Inline working gives exact radicals before a3dp final display.',[p,part('ii','real-roots','x**3-x**2-3*x+2','FiniteSet(2,(-1-sqrt(5))/2,(-1+sqrt(5))/2)')])
r['assessed_8227_demand_ids']=['8227:2020:M2:T1:O04:D02','8227:2020:M2:T1:O04:D04'];r['component_demand_ids']=['8227:2020:M2:T1:O03:D01','8227:2020:M2:T1:O03:D03']
r['precision_angle_check']['conflict']='Book final line gives -1.618 and0.618to3dp,though the task gives no rounding instruction. Retain exact radical values under NSSCAS exact-form guidance; do not infer a general3dp rule.'
r['value_level_scope_decisions'][0].update(status='within',quoted_value='(x^3-x^2-3x+2) divided by(x-2)',reason='Supporting division is cubic by linear; it is a method,not a separately requested quotient.')
add(8,25,'Find an integer root of x^3-3x^2+2x-6by testing signed divisors of6; the successful value is3.',[part('answer','integer-roots-except','x**3-3*x**2+2*x-6','FiniteSet(3)',**{'except':[]})])
add(9,25,'Decide whether x^3-3x^2+2x-5has an integer root; all four signed divisors of5fail,without claiming the cubic has no real root.',[part('answer','integer-roots-except','x**3-3*x**2+2*x-5','FiniteSet()',**{'except':[]})])
c=['-24+4*a+b','64/9+16*a/9+b']
add(10,25,'Use supplied factors3x-4andx+2of3x^3+ax^2+bto determine a,bfrom exact root inputs4/3and-2.',[part('answer','identity','Tuple(a,b)','Tuple(14,-32)',conditions=c,unknowns=['a','b'])],key_page=26)
add(11,27,'Find the remainder of2x^3-3x+5underx+1by evaluating at-1; zero x^2coefficient needs no long division.',[part('answer','identity','(2*x**3-3*x+5).subs(x,-1)','6')])
add(12,27,'A remainder2under nonmonic divisor2x-1fixes the constant coefficient of4x^2-6x+a; evaluate at1/2.',[part('answer','identity','a','4',conditions=['1-3+a-2'],unknowns=['a'])])
r=add(13,27,'Find the linear remainder of sparse quartic2x^4-3x^3+4under quadratic x^2+1; keep blank x^2andxcolumns in the displayed long division.',[part('answer','remainder',['2*x**4-3*x**3+4','x**2+1'],'3*x+6')])
r['assessed_8227_demand_ids']=['8227:2020:M2:T1:O03:D03'];r['component_demand_ids']=['8227:2020:M2:T1:O03:D02']
r['mapping_rationale']='The requested output is the remainder; quadratic division is the valid worked method,not a separately requested quotient.'
r['value_level_scope_decisions'][0].update(status='within',quoted_value='(2x^4-3x^3+4) divided by(x^2+1)',reason='Actual dividend degree4and divisor degree2; sparse terms change bookkeeping,not scope.')
first=part('i','affine-sketch',['-1','1']);first['printed_key_features']={'y_intercept':'1','x_intercepts':'FiniteSet(1)','slope':'-1'}
second=part('ii','modulus-sketch',['-1','1','0']);second['printed_key_features']={'vertex':'Tuple(1,0)','y_intercept':'1','x_intercepts':'FiniteSet(1)'}
third=part('iii','modulus-sketch',['-1','1','2']);third['printed_key_features']={'vertex':'Tuple(1,2)','y_intercept':'3','x_intercepts':'FiniteSet()'}
add(14,32,'Sketch the line1-x,reflect its negative branch to form|1-x|,then translate upwards2to2+|1-x|; preserve the three separate axes and vertices.',[first,second,third])
rows[-1]['value_level_scope_decisions']=[{'rule_id':'8227:QUAL01','status':'within','quoted_value':'y=1-x; y=|1-x|; y=2+|1-x|','reason':'Modulus graph coefficients are integers; the first line is a precursor,not itself governed by QUAL01.'}]
add(15,33,'Solve three differently arranged modulus inequalities,including a constant minus a modulus; distinguish connected intervals from two outside branches.',[part('i','inequality','Abs(x+3)<=4','Interval(-7,1)'),part('ii','inequality','Abs(2*x-1)>9','Union(Interval.open(-oo,-4),Interval.open(5,oo))'),part('iii','inequality','5-Abs(x-2)>1','Interval.open(-2,6)')])
add(16,34,'Recover midpoint2and half-width4from-2<x<6to express the interval as|x-2|<4.',[part('answer','identity','Tuple((-2+6)/2,(6-(-2))/2)','Tuple(2,4)')])
add(17,34,'Solve2x<|x-3|; negative left-side values must not be lost by unjustified squaring. The graph supports the final half-line x<1.',[part('answer','inequality','2*x<Abs(x-3)','Interval.open(-oo,1)')])
add(18,35,'Solve equality of|2x-1|and|x-2|,then use relative height or squaring to obtain the strict interval for the corresponding inequality.',[part('i','real-roots','Abs(2*x-1)-Abs(x-2)','FiniteSet(-1,1)'),part('ii','inequality','Abs(2*x-1)<Abs(x-2)','Interval.open(-1,1)')])

for row in rows:
    n=int(row['item_id'].rsplit(':',1)[1])
    if n==5:
        row['subparts'][0]['additional_operations']={'plotted_value_table':{'kind':'evaluate-list','operands':['4*x**3-8*x**2-x+2'],'at':['-1','0','1','2','3']}}
        row['subparts'][0]['assertions']=[{'expression':'Tuple((4*x**3-8*x**2-x+2).subs(x,-1),(4*x**3-8*x**2-x+2).subs(x,0),(4*x**3-8*x**2-x+2).subs(x,1),(4*x**3-8*x**2-x+2).subs(x,2),(4*x**3-8*x**2-x+2).subs(x,3))','expected':'Tuple(-9,2,-3,0,35)'}]
    if n==7:
        row['subparts'][1]['additional_operations']={'displayed_division_quotient':{'kind':'quotient','operands':['x**3-x**2-3*x+2','x-2']},'displayed_division_remainder':{'kind':'remainder','operands':['x**3-x**2-3*x+2','x-2']}}
    if n==9:
        row['component_demand_ids']=['8227:2020:M2:T1:O04:D02']
        row['mapping_rationale']='Integer-root exclusion is supporting practice; it does not solve the cubic over the reals or establish full assessed-demand coverage.'
    if n==14:
        row['assessed_8227_demand_ids']=['8227:2020:M2:T1:O02:D01']
        row['component_demand_ids']=['8227:2020:M2:T1:O01:D01']
        row['mapping_rationale']='Three graphs are the requested outputs; modulus notation is a component rather than a second independent response.'
    if n==16:
        row['assessed_8227_demand_ids']=['8227:2020:M2:T1:O01:D03']
        row['direct_demand_aspects']={'8227:2020:M2:T1:O01:D03':'Reverse interval-to-modulus representation,not an arbitrary forward inequality solve.'}
if __name__=='__main__':
    (W/'tools/textbook-r5/answers-Goldie-C1-examples.json').write_text(json.dumps({'scope':'All18numbered C1worked examples; exact answer page recorded per output.','items':rows},ensure_ascii=False,indent=2)+'\n')
    print(len(rows),'example records')
