"""All retained Exercise8Bparts and Activity8.1; explicit source-method limits."""
import json
from author_Goldie_C8_opening import W,SRC,SHA,add,answers,new,ev,fig,figures,value,reasoning,compute,expression,equivalent,primitive_agrees,AREA,DEF,POWER
answers.clear();new.clear();figures.clear()
RECOVER='8227:2020:M1:T9:O02:D02';CONSTANT='8227:2020:M1:T9:O02:D01'
p=value('tidied','factor(2*(x-2)**(5/2)/5+4*(x-2)**(3/2)/3)','2*(3*x+4)*(x-2)**(3/2)/15',351,
 'Factor the common(2/15)(x−2)^(3/2)from the two terms. The remaining factor is3(x−2)+10=3x+4. This is algebraic simplification of the previous result,not selection of a new integration method;retain the real domainx≥2.')
add('Activity',1,204,'Complete the algebraic tidying of Example8.5:factor(2/5)(x−2)^(5/2)+(4/3)(x−2)^(3/2)into(2/15)(3x+4)(x−2)^(3/2).',[p],teaches=[POWER],qualifier='Exponents5/2and3/2,real x≥2.')
p=value('i-total-area','0','45/2',351,
 'The integrand6x(x²+1)³is an odd polynomial,negative on[−1,0]and positive on[0,1]. Expand it or use the independent polynomial primitive;the positive geometric area is twice∫₀¹6x(x²+1)³dx=45/2. The signed integral over[−1,1]is0and is not the requested area.')
p['operation']={'kind':'proper-definite-integral','operands':['12*x*(x**2+1)**3','0','1']}
p['additional_operations']={'signed_integral':{'kind':'proper-definite-integral','operands':['6*x*(x**2+1)**3','-1','1']},'odd_symmetry':{'kind':'identity','operands':['(6*x*(x**2+1)**3).subs(x,-x)+6*x*(x**2+1)**3']}}
p['additional_operation_expected']={'signed_integral':'0','odd_symmetry':'0'}
p2=value('ii-area','0','10/9',351,
 'On[2,4],x/(x−1)³is positive and the pole1is outside the interval. Rewrite it as(x−1)^−2+(x−1)^−3and integrate those linear powers. Keep the original pole even though this rewrite needs no partial-fractions decomposition.')
p2['operation']={'kind':'proper-definite-integral','operands':['x/(x-1)**3','2','4']}
p2['additional_operations']={'rewrite':{'kind':'identity','operands':['x/(x-1)**3-1/(x-1)**2-1/(x-1)**3']}};p2['additional_operation_expected']={'rewrite':'0'}
row=add('Exercise-8B',3,204,'Find both diagrammed geometric areas:6x(x²+1)³between−1and1,with one region below the axis;andx/(x−1)³between2and4. The first is polynomial after expansion,the second a sum of linear powers.',[p,p2],[AREA],[DEF],rep='graph',qualifier='6x(x²+1)³expands into polynomial powers; x/(x−1)³=(x−1)^−2+(x−1)^−3,bounds2and4avoid pole1.')
row['source_interpretation']={'scope_correction':'The earlier boundary note called3(i)a nonlinear-argument area. Its integrand is a finite polynomial,so direct termwise integration is prescribed and no general substitution is needed.'}
p=value('curve','integrate(1/sqrt(2*x+3),x)+2*sqrt(3)-integrate(1/sqrt(2*x+3),x).subs(x,0)','sqrt(2*x+3)+sqrt(3)',351,
 'Integrate the supplied gradient independently,then enforce the original point(0,2√3). The primitive√(2x+3)has value√3at0,so the required constant is√3. The derivative’s real regular component through the point isx>−3/2. This fixed-point curve is not equivalent up to an arbitrary constant.')
p['additional_operations']={'gradient_check':{'kind':'identity','operands':['diff(sqrt(2*x+3)+sqrt(3),x)']},'point_check':{'kind':'identity','operands':['(sqrt(2*x+3)+sqrt(3)).subs(x,0)']}}
p['additional_operation_expected']={'gradient_check':'1/sqrt(2*x+3)','point_check':'2*sqrt(3)'}
add('Exercise-8B',4,204,'Recover the curve with dy/dx=1/√(2x+3)through(0,2√3),determining its integration constant on the real component containing the point.',[p],[RECOVER],[POWER,CONSTANT],qualifier='(2x+3)^−1/2with affine inner function;pointx=0iswithin x>−3/2.')
p=value('area','0','4/3',351,
 'Read the region between the upper liney=2and lower curvey=√(x+1),bounded by the y-axis. Their intersection hasx=3,consistent with the diagram. Integrate2−√(x+1)from0to3;it stays nonnegative. Do not use the whole area under either graph.')
p['operation']={'kind':'proper-definite-integral','operands':['2-sqrt(x+1)','0','3']}
p['additional_operations']={'intersection':{'kind':'identity','operands':['solve(sqrt(x+1)-2,x)[0]']}};p['additional_operation_expected']={'intersection':'3'}
add('Exercise-8B',5,204,'Use the given y=√(x+1),y=2and y-axis diagram to find the shaded area between the curves over0≤x≤3.',[p],[AREA],[DEF],rep='graph',qualifier='The linear power(x+1)^(1/2)isfinite on[0,3];the upper/lower curves meet atx=3.')
p=value('i-a','0','8*sqrt(x)-3/(2*x**2)',351,
 'Independently integrate4x^(−1/2)+3x^−3termwise. Its real domain isx>0because of the square root and reciprocal. Retain an arbitrary additive constant only for this indefinite integration output.')
p['operation']={'kind':'real-elementary-antiderivative','operands':['4/sqrt(x)+3/x**3']};p['answer_equivalence']='up-to-additive-constant'
p2=value('i-b','0','2*(1+x**2)**(3/2)',351,
 'For internal boundary QA,independently recognise the derivative of(1+x²)^(3/2)as3x√(1+x²);the original coefficient6therefore requires twice that primitive. This nonlinear-root integration is supporting extension,not automatically a listed linear-power integral. The enlarged printed key does contain2;the suspected missing-factor error is cleared.')
p2['operation']={'kind':'real-elementary-antiderivative','operands':['6*x*sqrt(1+x**2)'],'integration_algorithm':'manual'};p2['answer_equivalence']='up-to-additive-constant'
p3=reasoning('ii-substitution','k=2,a=1,b=2under the required x=u²substitution with positiveu.',
 'For1≤x≤4,the positive branchu=√xlies1≤u≤2,anddx=2udu. The original denominator√x=u cancels this factoru,leaving2(1+u)³du. The enforced substitution method is additional to prescribed requirements;the original integral also expands into ordinary powers.',351,'show/prove')
p4=value('ii-integral','0','65/2',351,
 'Independently expand the original integrand asx^(−1/2)+3+3x^(1/2)+xand integrate directly from1to4. The result65/2=32.5also equals the source’s transformed2∫₁²(1+u)³du. This verifies the value without relying on the same substitution.')
p4['operation']={'kind':'proper-definite-integral','operands':['(1+sqrt(x))**3/sqrt(x)','1','4']}
p4['additional_operations']={'transformed_integral':{'kind':'proper-definite-integral','operands':['2*(1+x)**3','1','2']}};p4['additional_operation_expected']={'transformed_integral':'65/2'}
row=add('Exercise-8B',7,205,'Integrate4/√x+3/x³and6x√(1+x²),then explicitly transform∫₁⁴(1+√x)³/√x dxusingx=u²,givek,a,b,and evaluate. Only(i-a)is directly prescribed as stated;(i-b)is a nonlinear-root extension,and(ii)enforces an extra method.',[p,p2,p3,p4],[POWER],qualifier='(i-a)uses exponents−1/2and−3;(ii)expands into exponents−1/2,0,1/2,1but explicitly forcesx=u².')
row['scope_check'].update(status='in-scope-parts-only',excluded_or_qualified_parts=['i-b:nonlinear-root reverse-chain integration,not a listed linear-power form','ii:requiredx=u²substitution is additional,though the original mathematical integral can be expanded into prescribed powers.'])
row['direct_demand_aspects']=[{'demand_id':POWER,'assessed_facet':'Part(i-a)only;do not let its directly assessed link cover(i-b)or the mandatory method in(ii).'}]
row['value_level_scope_decisions'].append({'rule_id':'8227:LIMIT07','status':'outside','parts':['ii-required-method'],'quoted_value':'Show that the substitutionx=u²transforms∫₁⁴(1+√x)³/√x dx.','reason':'The original explicitly requires a general substitution;its extra method remains visible.'})
row['source_interpretation']={'key_factor_check':'Native4xcrops of source and key confirm coefficient6in the question and coefficient2in the primitive. No missing-factor defect is claimed.'}

for n,page,label,note,teaches,checks,parent in [
 (10,204,'Exercise8B3(i)polynomial two-region diagram','The odd polynomial6x(x²+1)³has shaded bounds−1and1and root0. The left shaded region is below the axis;the right is above. Geometric areas add,while the signed symmetric integral cancels.',[AREA],[('expand(6*x*(x**2+1)**3)','6*x**7+18*x**5+18*x**3+6*x')],'Exercise-8B:3'),
 (11,204,'Exercise8B3(ii)rational area diagram','The originalx/(x−1)³has polex=1and shaded interval[2,4],where the curve is positive. The dashed pole lies outside the area and cannot be crossed by an antiderivative endpoint subtraction.',[AREA],[('Tuple((x/(x-1)**3).subs(x,2),(x/(x-1)**3).subs(x,4))','Tuple(2,4/27)')],'Exercise-8B:3'),
 (12,204,'Exercise8B5line and root-curve diagram','The shaded region lies belowy=2and abovey=√(x+1),between the y-axis and intersection(3,2). The curve passes(0,1);the picture’s right-hand interval is a region bound,not its full domain.',[AREA],[('Tuple(sqrt(0+1),sqrt(3+1))','Tuple(1,2)')],'Exercise-8B:5')]:fig(n,page,label,note,teaches,'graph',checks,parent)
for f in figures:
 f['item_id']=f['item_id'].replace(':C5:',':C8:');f['parent_item_id']=f['parent_item_id'].replace(':C5:',':C8:');f['source_evidence']=ev(f['pdf_page'])
pages=[{'pdf_page':204,'printed_page':190,'chapter':8,'page_status':'items enumerated','item_ids':[r['item_id']for r in answers if r['source_pdf_page']==204]+[r['item_id']for r in figures],
 'continuation_item_ids':[],'source_evidence':ev(204),'reader':'Codex author','date':'2026-11-18',
 'non_item_content':'Activity8.1,8B3–5and every given figure retained.8B1and2explicitly require suggested/suitable general substitutions;8B6requiresu=x³−4. Those original required-method tasks are outside prescribed scope. Their polynomial/linear-power ingredients do not silently erase the method condition.'}]
if __name__=='__main__':
 for name,data in [('answers-Goldie-C8-8B.json',{'scope':'Every retained8B3–5,7andActivity8.1response;named extra methods and parts stay explicit.','items':answers}),('census-Goldie-C8-8B.json',{'book':'Goldie','book_id':'8227-SRC-015','chapter':8,'source_path':SRC,'source_sha256':SHA,'scope':'Complete204;8B7on205recorded,combined205census awaits8.3figures and boundary records.','new_items':new+figures,'corrections':[],'pages':pages})]:
  (W/'tools/textbook-r5'/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
 for r in answers:
  for p in r['subparts']:
   if 'operation'in p:
    got=compute(p['operation']);expected=expression(p['printed_key_normalised'])
    assert primitive_agrees(p['operation'],got,expected)if p.get('answer_equivalence')=='up-to-additive-constant'else equivalent(got,expected),(r['item_id'],p['subpart'])
   for name,op in p.get('additional_operations',{}).items():assert equivalent(compute(op),expression(p['additional_operation_expected'][name])),(r['item_id'],name)
 print(len(answers),'items;',sum(len(r['subparts'])for r in answers),'outputs;',len(figures),'figures')
