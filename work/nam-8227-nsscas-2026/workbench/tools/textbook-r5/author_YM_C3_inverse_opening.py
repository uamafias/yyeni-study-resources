"""YM119: inverse domains,an invalid inverse input and an unstated quadratic branch."""
import json
import author_YM_C3_opening as prior
from author_YM_C3_opening import W,SRC,SHA,pp,ev,v,reasoning,fig,figures,compute,expression,equivalent,ONEONE,NOTATION
prior.answers.clear();prior.new.clear();figures.clear();prior.corrections.clear()
answers=prior.answers;new=prior.new;corrections=prior.corrections
INVERSE='8227:2020:M1:T3:O03:D02'

def extra(p,name,expr,key,kind='identity'):
 p.setdefault('additional_operations',{})[name]={'kind':kind,'operands':[expr]};p.setdefault('additional_operation_expected',{})[name]=key;return p

def add(kind,n,note,parts,scope_status='in-scope',outside=None):
 r=prior.add(kind,n,119,note,parts,[INVERSE])
 r['scope_check']={'status':scope_status,'basis':note,'excluded_or_qualified_parts':outside or[],'limits_considered':['8227:QUAL08']}
 r['mapping_rationale']='An inverse is a function on the ORIGINAL image,with values in the original domain. Algebraic swapping/squaring alone does not establish a valid branch or permit inputs outside that image. A noninjective unrestricted original needs an explicit branch restriction before an inverse function is claimed.'
 r['value_level_scope_decisions']=[{'rule_id':'8227:QUAL08','status':'outside'if outside else'within','parts':outside or[p['subpart']for p in parts],
 'quoted_value':note,'reason':'The named source parts lose an essential inverse-domain/one-to-one restriction; retain them as source-defect/boundary evidence,not valid unqualified originals. Other listed parts have explicit natural domains and valid one-to-one rules.'if outside else'The original is injective on its actual real domain; the inverse domain/image and any original poles are retained.'}]
 r['precision_angle_check']={'source':'Exact algebraic inverses; no rounding or angle units.','comparison':'Principal real square roots have nonnegative outputs. Cubic roots are real odd roots for negative arguments. Inverse notation is not a reciprocal,and natural poles/declared branch restrictions remain essential.'}
 for p in r['subparts']:p['given_representation']='text';p['response_format']='symbolic'
 return r
p=reasoning('a-inverse-domain','g^−1(x)=x²+3,with domainx≥0andimage[3,∞).','The originalg(t)=√(t−3)hasdomain[3,∞)andimage[0,∞). Swap input/output only over those sets:the inverse polynomial is restricted tox≥0. The source prints the formula but omits that essential restriction before using a negative inverse input.',119,'key incomplete')
p['original_function']='sqrt(x-3)';p['original_domain']='Interval(3,oo)';p['inverse_formula']='x**2+3';p['inverse_domain']='Interval(0,oo)'
p['additional_operations']={'original-image':{'kind':'real-image-range','operands':['sqrt(x-3)','Interval(3,oo)']},'restricted-inverse-image':{'kind':'real-image-range','operands':['x**2+3','Interval(0,oo)']}}
p['additional_operation_expected']={'original-image':'Interval(0,oo)','restricted-inverse-image':'Interval(3,oo)'}
p2=v('b-invalid-input','solveset(sqrt(x-3)+2,x,domain=S.Reals)','FiniteSet(7)',119,'The requestedg^−1(−2)asks for a real preimage of−2under√(t−3),which has no real solution. The printed7comes from extending the inverse polynomial outside its domain. Checkingg(7)=2,not−2,exposes the invalid inverse input.')
p2['author_expected_normalised']='S.EmptySet';p2['canonical_response']='Undefined:−2isnotin the originalimage[0,∞).'
extra(p2,'printed-preimage-countercheck','sqrt(7-3)','2')
r=add('Example',10,'Find the inverse of√(x−3),then evaluate it at−2. The formula needs domainx≥0; the second requested input lies outside it.',[p,p2],'in-scope-parts-only',['b-invalid-input: no real preimage; source answer7is invalid'])
r['value_level_scope_decisions'][0]['quoted_value']='g(x)=sqrt(x−3),with requested inverse input−2; original image[0,∞). '
r['source_interpretation']='Retain the original as defective/internal evidence. A valid newly authored inverse evaluation would require an admissible nonnegative input; no replacement recipe is authored in this round.'
p=v('a-inverse','solve(y-(3*x+4),x)[0].subs(y,x)','(x-4)/3',599,'Solve the ORIGINAL equationy=3t+4for t,then relabel the inverse inputx. Nonzero slope3makes the original injective onR.')
p2=v('b-at-minus-five','(-5-4)/3','-3',599,'The affine inverse hasdomainR,so input−5is admissible; its value is−3. Check the originalf(−3)=−5.')
extra(p2,'original-forward-check','3*(-3)+4','-5')
r=add('Try-Now-10',1,'Find an unrestricted affine inverse andevaluate it at an admissible negative argument.',[p,p2])
r['value_level_scope_decisions'][0]['quoted_value']='f(x)=3x+4; evaluateinverse at−5. Nonzero slope3givesone-to-one original onR.'
ps=[]
for label,original,key,method in [
 ('a','5*x','x/5','The slope5isnonzero,so solve the affine equation for its original input; both original andinverse have real domain.'),
 ('d','6*(x+3)','x/6-3','Undo multiplication by6andtranslation by3in reverse order; original/inverse domains areR.'),
 ('e','(x+4)/2','2*x-4','Undo division by2then addition of4; original/inverse domains areR.'),
 ('f','x/4-3','4*x+12','Undo subtraction of3then division by4; distribute the factor4after adding3.'),
 ('g','(x+1)/x','1/(x-1)','Originaldomain excludes0anditsimage excludes1. Solve the rational equation,then retain inverse domainx≠1.'),
 ('h','(x+4)/(2*x-5)','(4+5*x)/(2*x-1)','Originaldomain excludes5/2anditsimage excludes1/2. The nonsingular fractional-linear rule is injective on its full natural domain; retain inverse polex1/2.'),
 ('i','Rational(2,3)*(4*x-5)','(3*x+10)/8','The original slope8/3isnonzero; undo its affine operations exactly,with both domainsR.')]:
 p=v(label,'solve(y-('+original+'),x)[0].subs(y,x)',key,599,method)
 p['original_function']=original;p['inverse_domain']='Complement(S.Reals,FiniteSet(1))'if label=='g'else'Complement(S.Reals,FiniteSet(Rational(1,2)))'if label=='h'else'S.Reals'
 if label=='g':extra(p,'original-natural-domain',original,'Complement(S.Reals,FiniteSet(0))','real-function-domain');extra(p,'inverse-natural-domain',key,'Complement(S.Reals,FiniteSet(1))','real-function-domain')
 if label=='h':extra(p,'original-natural-domain',original,'Complement(S.Reals,FiniteSet(Rational(5,2)))','real-function-domain');extra(p,'inverse-natural-domain',key,'Complement(S.Reals,FiniteSet(Rational(1,2)))','real-function-domain')
 ps.append(p)
p=reasoning('b','g^−1(x)=realcuberoot((x+1)/2),onallrealx.','Solve the originaly=2t³−1by t³=(y+1)/2andthe unique real odd root. The cubic is strictly increasing onR. A principal complex-power interpretation for negative arguments is not the textbook’s real cube-root answer.',599,'matches')
p['original_function']='2*x**3-1';p['inverse_domain']='S.Reals';extra(p,'negative-zero-positive-check','Tuple(2*(-1)**3-1,2*0**3-1,2*1**3-1)','Tuple(-3,-1,1)');ps.append(p)
p=reasoning('c','No inverse FUNCTION for h(x)=x²+2onits unrestricted natural domainR. Conditional branches need a stated original restriction.','The key√(x−2)uses an unstated nonnegative-original-input branch. OnR,h(−1)=h(1)=3,so h isnotone-to-one. Iforiginalx≥0,the inverse is+√(x−2);iforiginalx≤0,it is−√(x−2). Either inverse hasdomain[2,∞),but neither is an inverse for the entire originalRdomain. Keep both conditional options and the missing-source-domain defect explicit.',599,'key incomplete')
p['assessed_8227_demand_ids']=[];p['teaches_8227_demand_ids']=[ONEONE,INVERSE];p['conditional_branches']=[{'original_domain':'Interval(0,oo)','inverse':'sqrt(x-2)','inverse_domain':'Interval(2,oo)'},{'original_domain':'Interval(-oo,0)','inverse':'-sqrt(x-2)','inverse_domain':'Interval(2,oo)'}]
extra(p,'noninjective-original','Tuple((-1)**2+2,1**2+2)','Tuple(3,3)');extra(p,'positive-branch-not-global','sqrt(((-1)**2+2)-2)','1');ps.append(p)
ps.sort(key=lambda p:p['subpart'])
r=add('Try-Now-10',2,'Find nine algebraic inverses. The unrestricted quadratic in(c)needs an explicit original branch; affine,cubic andfractional-linear cases retain their natural inverse domains.',ps,'in-scope-parts-only',['c: originalx²+2has no global inverse function onR; key silently chooses the positive branch'])
r['value_level_scope_decisions'][0]['quoted_value']='Part(c):h(x)=x²+2withnooriginaldomainrestriction. Other originals are5x,2x³−1,6(x+3),(x+4)/2,x/4−3,(x+1)/x,(x+4)/(2x−5),and(2/3)(4x−5). '
r['source_interpretation']='Part(c)remains held as an unqualified source exemplar until an original branch is stated. The conditional branches are analysis of the source defect,not new recipes or generation domains.'
refs=[
 (34,119,'Inverse swapped-pair mapping and undoing arrows','The diagram pairs originalinputs−1,0,3with outputs−5,−2,7under3x−2,and reverses the arrows with inverse(x+2)/3. Swap each full ordered pair,not signs or an arbitrary operation order. The inverse is a function only if the original is one-to-one.',[NOTATION,ONEONE,INVERSE],'diagram',[('Tuple(3*(-1)-2,3*0-2,3*3-2)','Tuple(-5,-2,7)')],None,'teaching-figure'),
 (35,119,'Inverse-function notation box','The superscript−1denotes the inverse FUNCTION,not the reciprocal of f(x). Its permitted inputs are the original image; swapping variables must keep those sets.',[NOTATION,INVERSE],'table',[],None,'teaching-figure'),
 (36,119,'Square-root inverse working and lost domain','Example10correctly obtains polynomialx²+3fromtheinput/output equation,but loses the restrictionx≥0. The final evaluation at−2is undefined for the inverse;g(7)=2cannotjustifyg^−1(−2)=7.',[INVERSE],'table',[('sqrt(7-3)','2')],'Example:10','teaching-figure')]
for n,page,label,note,teaches,rep,checks,parent,kind in refs:
 fig(n,page,label,note,teaches,rep,checks,parent)
 f=figures[-1];f['item_id']=f['item_id'].replace('Goldie:C5:','YM:C3:');f['parent_item_id']=f['parent_item_id'].replace('Goldie:C5:','YM:C3:')if f['parent_item_id']else None
 f.update(printed_page=pp(page),source_evidence=ev(page),value_level_scope_decisions=[],item_kind=kind)
pages=[{'pdf_page':119,'printed_page':108,'chapter':3,'page_status':'items enumerated','item_ids':[r['item_id']for r in answers]+[r['item_id']for r in figures],'continuation_item_ids':[],'source_evidence':ev(119),'reader':'Codex author','date':'2026-11-19','non_item_content':'Everyinverseintroductorymapping/notation reference,Example10andTry10Q1/2response is enumerated. ActualQUAL08decisions retain the square-root inverse domain and the missing quadratic branch. Pole domains and real cube roots are explicit.','scope_screen':'Valid inverse cases are in scope. Example10’s negative inverse argument andTry10Q2(c)’s unrestricted quadratic are defective/unqualified source parts; their conditional analysis stays visible without claiming valid unqualified assessment.'}]
if __name__=='__main__':
 for name,data in [('answers-YM-C3-inverse-opening.json',{'scope':'Every119response and printed reference,including explicit invalid-domain/branch defects.','items':answers}),('census-YM-C3-inverse-opening.json',{'book':'YM','book_id':'8227-SRC-017','chapter':3,'source_path':SRC,'source_sha256':SHA,'scope':'Complete119 page census.','new_items':new+figures,'corrections':corrections,'pages':pages})]:
  (W/'tools/textbook-r5'/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
 for row in answers:
  for p in row['subparts']:
   if'operation'in p:assert equivalent(compute(p['operation']),expression(p.get('author_expected_normalised',p['printed_key_normalised']))),(row['item_id'],p['subpart'])
   for name,op in p.get('additional_operations',{}).items():
    if name in p.get('additional_operation_expected',{}):assert equivalent(compute(op),expression(p['additional_operation_expected'][name])),(row['item_id'],p['subpart'],name)
 print(len(answers),'items;',sum(len(r['subparts'])for r in answers),'responses;',len(figures),'references/assets;',len(pages),'pages')
