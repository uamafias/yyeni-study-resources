"""Author transcription of all Goldie Exercise1B source outputs, from R5 renders.
Maintained evidence input builder; not a learner recipe/generator.
"""
import json,hashlib
from pathlib import Path
W=Path(__file__).resolve().parents[2];rows=[]
ROOT=W.parents[2]
def evidence(name):
 p=W/f'checks/r5/textbooks/{name}.png';return {'path':str(p.relative_to(ROOT)),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
def op(kind,*args,**kw):return {'kind':kind,'operands':list(args),**kw}
def p(label,kind,expr,key,**kw):return {'subpart':label,'operation':op(kind,expr,**kw),'printed_key_normalised':key}
def div(label,kind,a,b,key):return {'subpart':label,'operation':op(kind,a,b),'printed_key_normalised':key}
def sketch(label,expr,roots):return {'subpart':label,'operation':op('polynomial-sketch',expr),'printed_key_features':{'labelled_x_intercepts':roots},'method':'Derive roots,multiplicities,y-intercept and leading-term end behaviour; compare the labelled intercepts and shape on the rendered key.'}
def show(part):part['check_mode']='show/prove';return part

def add(n,note,parts):
 page=28 if n<=7 else 29 if n<=17 else 30
 for part in parts:
  part.update(source_evidence=evidence('Goldie-C1-27'),key_evidence=evidence('Goldie-keys-C1'),answer_pdf_page=333 if n<=6 else 334,answer_printed_page=319 if n<=6 else 320)
  part.setdefault('method','Independently evaluate/factor the transcribed source polynomial,solve the real factors or parameter equations,and compare the separately transcribed key.')
 row={'item_id':f'8227:TB:Goldie:C1:Exercise-1B:{n}','source_pdf_page':page,'notes':note,'component_demand_ids':[],
 'expected_subpart_labels':[v['subpart']for v in parts],'exam_style':n>=17,'exam_style_basis':'Explicit Cambridge paper attribution printed below question.'if n>=17 else'No paper attribution or source exam-style heading on this question.',
 'value_level_scope_decisions':[{'rule_id':'8227:LIMIT05','status':'within'if any(v['operation']['kind']in['quotient','remainder']for v in parts)else'not applicable','quoted_value':'; '.join(v['operation']['operands'][0]for v in parts),'reason':'All explicitly requested divisions have degree3or4 dividends and linear orquadratic divisors. Solving/factoring/sketching is distinct; any supporting division also stays within degree4.'}], 'subparts':parts};rows.append(row);return row
f='x**3+2*x**2-9*x-18'
add(1,'Evaluate seven inputs of x^3+2x^2-9x-18,then factor,solve and sketch its three simple crossings.',[p('i','evaluate-list',f,'Tuple(0,0,-8,-18,-24,-20,0)',at=['-3','-2','-1','0','1','2','3']),p('ii','factor',f,'(x+3)*(x+2)*(x-3)'),p('iii','real-roots',f,'FiniteSet(-3,-2,3)'),sketch('iv',f,['-3','-2','3'])])
f='x**3-4*x'
add(2,'Evaluate x^3-4x on seven integers,then factor outx,use difference of squares,and sketch the odd cubic through-2,0,2.',[p('i','evaluate-list',f,'Tuple(-15,0,3,0,-3,0,15)',at=['-3','-2','-1','0','1','2','3']),p('ii','factor',f,'x*(x+2)*(x-2)'),p('iii','real-roots',f,'FiniteSet(-2,0,2)'),sketch('iv',f,['-2','0','2'])])
f='x**3-19*x+30'
add(3,'Use f(0),f(3)to identify factorx-3; match coefficients against(x-2)(x^2+px+q),solve and sketch roots/intercept.',[p('i','evaluate-list',f,'Tuple(30,0)',at=['0','3']),p('ii','identity','Tuple(p,q)','Tuple(2,-15)',conditions=['p-2','q-2*p+19','-2*q-30'],unknowns=['p','q']),p('iii','real-roots',f,'FiniteSet(-5,2,3)'),sketch('iv',f,['-5','2','3'])])
f='x**3-5*x**2-2*x+24'
add(4,'Establish factorx-3 of x^3-5x^2-2x+24,solve three roots and sketch with y-intercept24.',[show(p('i','identity','(x**3-5*x**2-2*x+24).subs(x,3)','0')),p('ii','real-roots',f,'FiniteSet(-2,3,4)'),sketch('iii',f,['-2','3','4'])])
f='x**4-5*x**2+2*x';first=show(p('i','integer-roots-except',f,'FiniteSet(0)',**{'except':['2']}));first['method']='Verifyf(2)=0,factor x(x-2)(x^2+2x-1),then identify the other integer root0.';first['established_result']='f(2)=0; other integer root0';first['assertions']=[{'expression':'(x**4-5*x**2+2*x).subs(x,2)','expected':'0'}]
r=add(5,'Establish integer roots2and0of x^4-5x^2+2x,find its two irrational roots,then sketch four simple crossings with both tails upwards. Key sketch mislabels the negative crossing-2.',[first,p('ii','real-roots','x**2+2*x-1','FiniteSet(-1-sqrt(2),-1+sqrt(2))'),sketch('iii',f,['-2','2'])]);r['subparts'][2].update(source_evidence=evidence('Goldie-question-1B5'),key_evidence=evidence('Goldie-key-1B5-graph'))
f='x**3-6*x**2+9*x-4'
add(6,'Use root4to recoverk=-4,identify the repeated factor(x-1)^2,and sketch touching at1andcrossing at4.',[p('i','identity','k','-4',conditions=['64-96+36+k'],unknowns=['k']),div('ii','quotient',f,'x-4','(x-1)**2'),sketch('iii',f,['1','4'])])
add(7,'Read simple root-2,double root1and intercept2from a given cubic,then solve it equal to that intercept.',[p('i','identity','Tuple(2,1,(0+2)*(0-1)**2)','Tuple(2,1,2)'),p('ii','real-roots','(x+2)*(x-1)**2-2','FiniteSet(0,sqrt(3),-sqrt(3))')])
f='x**4-3*x**2-4'
add(8,'Treat x^4-3x^2-4as quadratic inx^2,factor further,and count its real zeros. First printed key factorisation has a sign error.',[p('i','factor',f,'(x**2-4)*(x**2-1)'),p('ii','factor',f,'(x+2)*(x-2)*(x**2+1)'),p('iii','real-roots',f,'FiniteSet(-2,2)')])
f='2*x**3+5*x**2-7*x-3'
add(9,'Showx-2is not a factor by evaluating19,then explicitly find quotient and remainder under that divisor.',[show(p('i','identity','(2*x**3+5*x**2-7*x-3).subs(x,2)','19')),div('ii-q','quotient',f,'x-2','2*x**2+9*x+11'),div('ii-r','remainder',f,'x-2','19')])
f='x**3-4*x**2+x+6'
r=add(10,'Enumerate the eight signed divisors of6,test them inx^3-4x^2+x+6,and obtain all three integer roots.',[p('i','integer-root-candidates',f,'FiniteSet(-6,6,-3,3,-2,2,-1,1)'),p('ii','real-roots',f,'FiniteSet(-1,2,3)')]);r['subparts'][0]['candidate_polynomial']=f;r['subparts'][0]['candidate_check_values']={'-6':-360,'6':84,'-3':-60,'3':0,'-2':-20,'2':0,'-1':0,'1':4};r['subparts'][0]['key_comparison_limit']='Key lists candidates only; evaluation working is author-derived,not claimed printed.'
add(11,'Factor four supplied-factor cubics,retaining irreducible quadratics after extracting the given root.',[p('i','factor','x**3-x**2-4*x+4','(x-1)*(x-2)*(x+2)'),p('ii','factor','x**3+1','(x+1)*(x**2-x+1)'),p('iii','factor','x**3+x-10','(x-2)*(x**2+2*x+5)'),p('iv','factor','x**3+x**2+x+6','(x+2)*(x**2-x+3)')])
f='x**4-2*x**3+3*x**2-8';first=show(p('i','evaluate-list',f,'Tuple(-6,-2)',at=['1','-1']));first['key_comparison_limit']='Author proof of the two non-roots; no separate numeric answer to(i)is printed.'
add(12,'Show±1are non-roots of a sparse quartic,then divide byx-1,x+1andx^2-1,retaining scalar orlinear remainders.',[first,div('ii-a-q','quotient',f,'x-1','x**3-x**2+2*x+2'),div('ii-a-r','remainder',f,'x-1','-6'),div('ii-b-q','quotient',f,'x+1','x**3-3*x**2+6*x-6'),div('ii-b-r','remainder',f,'x+1','-2'),div('ii-c-q','quotient',f,'x**2-1','x**2-2*x+4'),div('ii-c-r','remainder',f,'x**2-1','-2*x-4')])
add(13,'Remainder7at-1determinesk in2x^3+3x^2+kx-6.',[p('answer','identity','k','-12',conditions=['-2+3-k-6-7'],unknowns=['k'])])
add(14,'Remainder21at3in a cubic with coefficientspandp^2produces a quadratic giving two possible parameters.',[p('answer','real-roots','(27+9*x+3*x**2-36-21)/3','FiniteSet(2,-5)')])
c=['27+9*a+3*b+8-2','-1+a-b+8+2']
add(15,'Recover two coefficients from different remainders,then evaluate a third remainder at2.',[p('coefficients','identity','Tuple(a,b)','Tuple(-5,4)',conditions=c,unknowns=['a','b']),p('remainder2','identity','8+4*a+2*b+8','4',conditions=c,unknowns=['a','b'])])
c=['2+a+b+6','-2+a-b+6-10']
add(16,'Zero remainderat1and remainder10at-1determinea,b; solve the resulting cubic including its fractional root.',[p('coefficients','identity','Tuple(a,b)','Tuple(-1,-7)',conditions=c,unknowns=['a','b']),p('roots','real-roots','2*x**3+a*x**2+b*x+6','FiniteSet(1,-2,3/2)',conditions=c,unknowns=['a','b'])])
c=['-24+4*a-2*a+a']
add(17,'In3x^3+ax^2+ax+a,the same parameter fills three coefficients; factorx+2determinesa,then division explicitly supplies quotient.',[p('i','identity','a','8',conditions=c,unknowns=['a']),div('ii','quotient','3*x**3+8*x**2+8*x+8','x+2','3*x**2+2*x+4')])
add(18,'Factorx+1and remainder5underx+2determine the two lower coefficients of2x^3+7x^2+ax+b.',[p('answer','identity','Tuple(a,b)','Tuple(2,-3)',conditions=['-2+7-a+b','-16+28-2*a+b-5'],unknowns=['a','b'])])
add(19,'Recover linear coefficienta from factorx+2in2x^3-x^2+ax-6,then factor completely with a nonmonic linear factor.',[p('i','identity','a','-13',conditions=['-16-4-2*a-6'],unknowns=['a']),p('ii','factor','2*x**3-x**2-13*x-6','(x+2)*(2*x+1)*(x-3)')])
c=['8+4*a+2*b+6','1+a+b+6-4']
add(20,'Factorx-2and remainder4underx-1determinea,binx^3+ax^2+bx+6; obtain the other two factors.',[p('i','identity','Tuple(a,b)','Tuple(-4,1)',conditions=c,unknowns=['a','b']),div('ii','quotient','x**3-4*x**2+7','x-2','(x-3)*(x+1)')])
c=['-4+a-b-2','-32+4*a-2*b-2']
add(21,'Roots-1,-2determine coefficients of4x^3+ax^2+bx-2,then a quadratic divisor produces a linear remainder.',[p('i','identity','Tuple(a,b)','Tuple(11,5)',conditions=c,unknowns=['a','b']),div('ii','remainder','4*x**3+11*x**2+5*x-2','x**2+1','x-13')])
f='6*x**4-x**3-26*x**2+4*x+15'
add(22,'Divide quartic byx^2-4,confirm remainder7,then subtract it to solve the related quartic through the factors.',[div('i-q','quotient',f,'x**2-4','6*x**2-x-2'),div('i-r','remainder',f,'x**2-4','7'),p('ii','real-roots','6*x**4-x**3-26*x**2+4*x+8','FiniteSet(-2,2,-1/2,2/3)')])
c=['-8+4*a+b','-1+b-a+18']
add(23,'Combine a factor condition onfand a remainder condition ongto determinea,b; cubic terms cancel,so g-fis a concave quadratic with a greatest value.',[p('i','identity','Tuple(a,b)','Tuple(5,-12)',conditions=c,unknowns=['a','b']),p('ii','quadratic-maximum','(x**3+b*x**2-a)-(x**3+a*x**2+b)','7',conditions=c,unknowns=['a','b'])])
rows[7]['subparts'][0].update(source_evidence=evidence('Goldie-question-1B8'),key_evidence=evidence('Goldie-key-1B8'))
# Recompute parameter substitution from the source conditions in every connected part;
# never feed the printed parameter answers into a later answer function.
for row in rows:
 n=int(row['item_id'].rsplit(':',1)[1]);parts=row['subparts']
 if n in[17,19,20,21]:
  conditions=parts[0]['operation']['conditions'];unknowns=parts[0]['operation']['unknowns']
  polynomial={17:'3*x**3+a*x**2+a*x+a',19:'2*x**3-x**2+a*x-6',20:'x**3+a*x**2+b*x+6',21:'4*x**3+a*x**2+b*x-2'}[n]
  parts[1]['operation']['operands'][0]=polynomial
  parts[1]['operation'].update(conditions=conditions,unknowns=unknowns)
 if n==7:
  parts[0]['operation']['operands'][0]='Tuple(-(-2),1,(0-(-2))*(0-1)**2)'
  parts[0]['source_graph_features']={'simple_zero':'-2','double_zero':'1','intercept_label':'c'}
  parts[0]['method']='Read the simple crossing-2and touching root1from the original graph; a is the negation of the crossing and b is the double root. Substitute0into the reconstructed expression to findc.'

def D(alias):
    m,t,o,d=map(int,alias.split('.'))
    return f'8227:2020:M{m}:T{t}:O{o:02}:D{d:02}'
F1='2.1.4.1';F2='2.1.4.2';F3='2.1.4.3';F4='2.1.4.4'
LIN='2.1.3.1';QUAD='2.1.3.2';QR='2.1.3.3';SKETCH='1.3.5.1';FUNC='1.3.1.1'
mapping={
 1:([F2,F4,SKETCH,FUNC],[],'Requested function values,factorisation,roots and sketch all remain visible.'),
 2:([F4,SKETCH,FUNC],[],'Common-factor/difference-of-squares factorisation does not itself require a factor-theorem claim.'),
 3:([F2,F3,F4,SKETCH,FUNC],[],'The explicit Hence factor decision,unknown coefficients,roots and sketch are requested results.'),
 4:([F2,F4,SKETCH],[LIN,QR],'Show supplied factor is direct; division is the worked route to later roots,not a separately requested quotient.'),
 5:([F2,F4,SKETCH],[],'Establish supplied root,find other roots and sketch; graph is not merely solution decoration.'),
 6:([F3,F4,SKETCH],[F2,LIN],'Parameter and remaining factors/sketch are outputs; using the given factor and division are components.'),
 7:(['1.1.5.2',F4],[FUNC],'Recover the cubic from graph data,then solve; evaluating its intercept is a component of reconstruction.'),
 8:([F4],[],'Quadratic-in-x² factorisation and real-root selection are the requested polynomial solution structure.'),
 9:([F2,LIN,QR],[FUNC],'Non-factor proof and explicit quotient/remainder are targets; substitution arithmetic is a component.'),
 10:([F2,F4],[FUNC,LIN],'The candidate-root tests and solved root set are outputs; value arithmetic/division support them.'),
 11:([F4],[LIN],'Only the factorisation stage is asked; final zero solving is not claimed as an additional output.'),
 12:([F2,LIN,QUAD,QR],[FUNC],'Non-root proofs and three explicitly requested divisions are assessed.'),
 13:([F3],[F1],'The requested result is unknown coefficientk; remainder theorem supplies the relation.'),
 14:([F3],[F1],'The requested result is the possible parameterp; remainder theorem and a quadratic solve support it.'),
 15:([F3,F1],[],'Both coefficient recovery and a new remainder are explicitly requested.'),
 16:([F3,F4],[F1],'Coefficient recovery and all roots are requested; remainder theorem builds the equations.'),
 17:([F3,LIN,QR],[F2],'Unknowna and explicit quotient are assessed; supplied factor generates the coefficient condition.'),
 18:([F3],[F1,F2],'Only the two coefficients are requested; factor and remainder conditions are the components.'),
 19:([F3,F4],[F2,LIN],'Unknowna and full factorisation requested; theorem/division are supporting routes.'),
 20:([F3,F4],[F1,F2,LIN],'Parameters and remaining factors are outputs; factor/remainder interpretation and division are components.'),
 21:([F3,QUAD,QR],[F2],'Two coefficients then an explicitly requested quadratic-divisor remainder; supplied factors are components.'),
 22:([QUAD,QR,F4],[],'Quotient,remainder and related quartic root set are all requested.'),
 23:([F3,'1.1.1.2'],[F1,F2],'Parameters and greatest quadratic value are targets; theorem conditions support parameter recovery.')}
for row in rows:
    n=int(row['item_id'].rsplit(':',1)[1]);direct,component,reason=mapping[n]
    row['assessed_8227_demand_ids']=[D(a)for a in direct]
    row['component_demand_ids']=[D(a)for a in component]
    row['mapping_rationale']=reason
    row['component_demand_roles']=[{'demand_id':D(a),'role':'intermediate skill in a valid worked route; not a separately requested output'}for a in component]
    if n in [6,11,19,20]:row['direct_demand_aspects']={D(F4):'Factorisation stage only; no separate request to solve the polynomial equal to zero. Do not infer full-demand coverage from this item alone.'}
    if n in [4,6,10,11,19,20]:
        row['value_level_scope_decisions'][0]['status']='within'
        row['value_level_scope_decisions'][0]['reason']='Supporting division in the displayed valid route has a cubic dividend and linear divisor. This is a value-level method check,not a claim that quotient output is independently assessed.'

for row in rows:
    n=int(row['item_id'].rsplit(':',1)[1]);parts=row['subparts']
    if n in [6,20]:parts[1]['operation']['kind']='factor-quotient'
    if n in [4,12]:
        parts[0]['author_check_target_normalised']=parts[0].pop('printed_key_normalised')
        parts[0]['comparison_target_kind']='Source show/prove assertion; author-derived proof. No separate printed numerical key entry is claimed.'
    if n==3:
        parts[0]['additional_operations']={'factorised_polynomial':op('factor','x**3-19*x+30')}
        parts[0]['derived_factor_conclusion']='Since f(3)=0,x-3 is a factor by the factor theorem.'
if __name__=='__main__':
 out=W/'tools/textbook-r5/answers-Goldie-1B.json';out.write_text(json.dumps({'scope':'All23question blocks; explicit outputs have stable subpart/result IDs. Comparison limits remain explicit.','items':rows},ensure_ascii=False,indent=2)+'\n')
 old=W/'tools/textbook-r5/answers-Goldie-1B-partial.json'
 if old.exists():old.unlink()
 print(len(rows),'question records')
