"""YM571–574: connected differentiation, bracket and iteration; radians."""
from author_YM_C13_late_support import *
reset()
DIFF='8227:2020:M2:T4:O01:D01';PRODUCT='8227:2020:M2:T4:O02:D01';QUOTIENT='8227:2020:M2:T4:O02:D02'
p=reason('a-provided-log-relation','p=3ln(20/(p+3)), p>−3.','Differentiate the original6xe^(x/3):yprime=2(x+3)e^(x/3). Set equal40; positive exponential implies p+3>0. Rearrange e^(p/3)=20/(p+3)>0 and take ln. Product differentiation is a component of the requested relation, not a separately asked derivative.',571,[REARRANGE,RELATE]);p['component_demand_ids']=[DIFF,PRODUCT];extra(p,'original-derivative','diff(6*x*exp(x/3),x)','2*(x+3)*exp(x/3)')
f='x-3*log(20/(x+3))'
q=a.bracket('b-sign-bracket',f,'Rational(33,10)','Rational(7,2)','Rational(33,10)-3*log(Rational(200,63))','Rational(7,2)-3*log(Rational(40,13))',571,'Original stationary-gradient relation has continuous real log argument on this bracket; signs negative then positive.');q['depends_on_source_parts']=['a-provided-log-relation']
seq=b.sequence_parts('c','3*log(20/(x+3))','Rational(17,5)',['3.4183','3.4097','3.4137'],4,571,f,['Rational(33,10)','Rational(7,2)'],'3.41',2,'No start specified; worked benchmark3.4. The source requests5dp per iterate but prints only4dp in its table.')
for p5,key5 in zip(seq[:-1],['3.41830','3.40974','3.41374']):
    p5['check_mode']='key incomplete';p5['display_precision']='Source requested5decimalplaces; printed table supplies4.'
    p5['requested_precision']='5 decimal places'
    p5['correct_requested_precision_value']=key5
    p5['source_key_limitation']='Four-place table numerically agrees at its printed accuracy but omits the fifth requested decimal digit.'
    p5.setdefault('additional_operations',{})['requested-five-place-value']={**p5['operation'],'rounding':dict(decimal_places=5)}
    p5.setdefault('additional_operation_expected',{})['requested-five-place-value']=key5
parts=[p,q]+seq
add('Example',7,571,'Original6xe^(x/3), gradient40 atp: show provided log relation; bracket3.3..3.5; iterate to root2dp3.41. Source asks each5dp but prints4; independently completed5dp values recorded.',parts)
f='x-2-6*exp(-x/2)'
p=reason('a-gradient-relation','x=2+6e^(−x/2).','Differentiate original(x−4)e^(x/2): yprime=(x/2−1)e^(x/2). Set3 and multiply by positive2e^(−x/2), givingx−2=6e^(−x/2). The source GIVEN graph locates P on the rising branch; it is not a sketch request.',654,[REARRANGE,RELATE],rep='graph');p['component_demand_ids']=[DIFF,PRODUCT];extra(p,'original-derivative','diff((x-4)*exp(x/2),x)','(x/2-1)*exp(x/2)')
q=a.bracket('b-sign-bracket',f,'Rational(31,10)','Rational(33,10)','Rational(11,10)-6*exp(-Rational(31,20))','Rational(13,10)-6*exp(-Rational(33,20))',654,'Bracket3.1..3.3 selects P; original gradient-equation residual is continuous and strictly increasing.');q['depends_on_source_parts']=['a-gradient-relation']
parts=[p,q]+b.sequence_parts('c','2+6*exp(-x/2)','Rational(16,5)',['3.2114','3.2045','3.2087','3.2061'],4,654,f,['Rational(31,10)','Rational(33,10)'],'3.21',2,'No start specified; key chooses3.2, within provided bracket.')
add('Try-Now-7',1,572,'GIVEN curve(x−4)e^(x/2), gradient3 atP: provided recurrence relation, bracket3.1..3.3, each4dp and root2dp3.21. No sketch requested; key benchmark3.2 is not mandatory.',parts,'graph')
p=val('a-derivative','diff(x**2/(1+exp(3*x)),x)','(2*x*(1+exp(3*x))-3*x**2*exp(3*x))/(1+exp(3*x))**2',654,[DIFF,QUOTIENT],'Quotient rule on original x²/(1+e^(3x)); denominator is positive for every realx. Explicit derivative requested before the HENCE relation.')
q=reason('a-hence-maximum-relation','m=(2/3)(e^(−3m)+1).','Set the derivative numeratorx[2(1+e^(3x))−3xe^(3x)] tozero. The GIVEN maximum M has m>0, so dividing bym does not discard the requested maximum; the stationary point0 is a minimum. Divide by positivee^(3m) and rearrange.',654,[REARRANGE,RELATE],rep='graph');extra(q,'factored-stationary-numerator','expand(2*x*(1+exp(3*x))-3*x**2*exp(3*x))','x*(2+2*exp(3*x)-3*x*exp(3*x))');q['depends_on_source_parts']=['a-derivative']
f='x-2*(exp(-3*x)+1)/3'
r=a.bracket('b-sign-bracket',f,'Rational(7,10)','Rational(4,5)','Rational(1,30)-2*exp(-Rational(21,10))/3','Rational(2,15)-2*exp(-Rational(12,5))/3',655,'Continuous maximum-coordinate residual, f.7 negative and f.8 positive.');r['depends_on_source_parts']=['a-hence-maximum-relation']
parts=[p,q,r]+b.sequence_parts('c','2*(exp(-3*x)+1)/3','Rational(3,4)',['0.73693','0.73974','0.73913','0.73926'],5,655,f,['Rational(7,10)','Rational(4,5)'],'0.739',3,'No start specified; source benchmark.75. Keep selected positive maximum, not the stationary origin.')
add('Try-Now-7',2,572,'GIVEN maximum ofx²/(1+e^(3x)): explicitly find derivative, hence show relation form; bracket.7..8; each5dp and root3dp.739. Nonzero m from the diagram justifies division.',parts,'graph')
f='cos(x)-2+2*x'
p=a.sketch('a-one-interval-root',['cos(x)','2-2*x'],'Radian interval[0,pi/2]: cos decreases from1to0; line2−2x starts2 and crosses the axis at1; exactly one crossing in(.5,1).','On the specified interval, difference derivative2−sin x>=1 and endpoint signs are opposite. Count only this interval, not all periodic real branches.',573)
q=a.bracket('b-sign-bracket',f,'Rational(1,2)','1','cos(Rational(1,2))-1','cos(1)',573,'Radian values approximately−.122,+.540; continuity proves existence.')
r=reason('c-map-to-equation','A fixed point of1−cos x/2 solves cos x=2−2x.','Collect2x=2−cos x. For the actual start.6, the map keeps[.5,1] invariant and attracts the unique root; the latter is independent author QA. The source working only establishes the fixed-point equality, not convergence from arbitrary starts.',573,[RELATE,REARRANGE]);extra(r,'equation-reconstruction','expand(2*(x-(1-cos(x)/2)))',f)
parts=[p,q,r]+b.sequence_parts('d','1-cos(x)/2','Rational(3,5)',['0.5873','0.5838','0.5828'],4,573,f,['Rational(1,2)','1'],'0.58',2,'Stem stipulates.6; radians. Display each calculated state4dp.')
row=add('Example',8,573,'Radian cos x=2−2x on0<=x<=pi/2: choose sketch pair, bracket.5..1, relate provided map, start.6; each4dp and root2dp.58.',parts)
row['continuation_pdf_pages']=[574]
p=a.sketch('a-one-interval-root',['cot(x)','x'],'Radian interval(0,pi/2): cot decreases from positive infinity to0; linex increases from0; one crossing in(.8,.9).','Difference derivative−csc²x−1<0 on the open interval; endpoint limiting signs are opposite. Excluded pole0 must not be used as a finite evaluation.',655)
q=a.bracket('b-sign-bracket','x-cot(x)','Rational(4,5)','Rational(9,10)','Rational(4,5)-cot(Rational(4,5))','Rational(9,10)-cot(Rational(9,10))',655,'Radian values approximately−.1712,+.1064.')
r=reason('c-principal-inverse-rearrangement','x=atan(1/x), in(0,pi/2).','The selected interval makes tan and cot reciprocals with x>0 and fixes the principal inverse-tangent branch. Without this interval, takingatan would not preserve every periodic solution.',655,[REARRANGE,RELATE]);extra(r,'reciprocal-identity','trigsimp(cot(x)*tan(x))','1')
parts=[p,q,r]+b.sequence_parts('d','atan(1/x)','Rational(17,20)',['0.8663','0.8569','0.8623'],4,655,'x-cot(x)',['Rational(4,5)','Rational(9,10)'],'0.86',2,'No start specified; key chooses.85. Stem asks iteration results but does not stipulate their decimal places; key uses4dp.')
row=add('Try-Now',8,574,'cot x=x, restricted0<x<pi/2radians. Sketch unique root, bracket.8..9, justify principalatan rearrangement; iterate root2dp.86. Benchmark.85 and4dp displays are key choices.',parts)
row['value_level_scope_decisions'].append(dict(rule_id='8227:QUAL08',status='within',quoted_value='0<x<pi/2, x=atan(1/x)',reason='The original positive interval is inside principalatan range and excludes the cotangent pole.'))
refs=[
 (41,571,'Example7 derivative and logarithm working','Positive exponential givesp>−3; product differentiation then supplied log relation.',[REARRANGE],'table','Example:7',False),
 (42,571,'Example7 sign-bracket calculation','Original residual negative at3.3 and positive at3.5.',[BRACKET],'table','Example:7',False),
 (43,571,'Example7 iteration table precision defect','Three printed states4dp despite source5dp instruction. Correct5dp3.41830,3.40974,3.41374; final3.41right.',[ITERATE,STOP],'table','Example:7',False),
 (44,572,'Try7Q1 GIVEN product-exponential curve','Curve(x−4)e^(x/2), pointP on rising branch with prescribedgradient3; read branch, not coordinates from scale.',[REARRANGE],'graph','Try-Now-7:1',True),
 (45,572,'Try7Q2 GIVEN maximum curve','Positive maximum M ofx²/(1+e^(3x)); origin is a separate stationary minimum.',[REARRANGE],'graph','Try-Now-7:2',True),
 (46,573,'Example8 cosine values','Cos0=1, cos(pi/4) approximately.7, cos(pi/2)=0; radians.',[ROOTG],'table','Example:8',False),
 (47,573,'Example8 linear values','2−2x through(0,2),(1,0).',[ROOTG],'table','Example:8',False),
 (48,573,'Example8 SOLUTION pair graph','Single crossing on prescribed first-quadrant interval; not a GIVEN input.',[ROOTG],'graph','Example:8',False),
 (49,573,'Example8 bracket and fixed-point algebra','Opposite signs at.5,1; fixed-point equality alone is conditional, not arbitrary-start convergence proof.',[BRACKET,RELATE],'table','Example:8',False),
 (50,573,'Example8 calculated-state table','Given.6 then.5873,.5838,.5828; final.58at2dp.',[ITERATE,STOP],'table','Example:8',False),
 (51,574,'Rounding-cell sign-test note','Native source correctly prints NEGATIVEf(.575)=−.010807697... and positivef(.585)=.003712085887...; no sign defect. This supports.58 to2dp.',[BRACKET,STOP],'table','Example:8',False),
 (52,574,'Staircase convergence graph','SuppliedF=1−cosx/2 with diagonal; local positive slope gives one-sided staircase in this example.',[CONVERGE],'graph','Example:8',False),
 (53,574,'Staircase enlarged inset','Magnified local iteration path; no new assigned problem.',[CONVERGE],'diagram','Example:8',False),
 (54,574,'Qualitative gradient-pattern note','Local positive/negative map slopes describe staircase/spiral examples; do not promote sign alone into a convergence theorem.',[CONVERGE,FAIL],'table',None,False)]
for args in refs:panel(*args)
extra(parts[0],'selected-domain-check','sign(pi/2-Rational(9,10))','1')
pages=census(571,574,{571:'All Example7 parts and three actual working panels. Native requested5dp versus printed4dp discrepancy recorded.',572:'Both Try7 questions, GIVEN graphs and derivative/rearrangement/sign/iteration outputs. No extra sketch response invented.',573:'Complete Example8 prompt, both value tables, worked sketch, bracket/rearrangement and iteration panel.',574:'Example8 continuation: correct native rounding-cell sign values, staircase and inset. Try8 complete; inverse branch and radians preserved.'},{574:['8227:TB:YM:C13:Example:8']})
if __name__=='__main__':save('calculus',pages)
