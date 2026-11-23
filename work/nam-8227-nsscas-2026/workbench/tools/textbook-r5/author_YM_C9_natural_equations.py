"""YM424: natural-log inequalities,rearrangements and original-domain root filters."""
import json
import author_YM_C9_opening as g
from author_YM_C9_opening import h,W,SRC,SHA,pp,ev,v,fig,figures,extra,compute,expression,equivalent
g.answers.clear();g.new.clear();g.corrections.clear();figures.clear()
answers=g.answers;new=g.new;corrections=g.corrections
LAW='8227:2020:M2:T2:O01:D02';INEQ='8227:2020:M2:T2:O03:D02';NAT='8227:2020:M2:T2:O02:D01'
def cutoff(label,condition,key,side,kp):
 p=v(label,'solve('+condition+',x)[0]',key,kp,'Take the natural logarithm of the ORIGINAL isolated positive exponential. Since ln is increasing,retain the source strict/inclusive relation;then divide by the actual positive affine exponent coefficient. Preserve the exact boundary separately from its requested3sf display.')
 p.update(operation={'kind':'rounded','operands':['solve('+condition+',x)[0]'],'significant_figures':3},assessed_8227_demand_ids=[INEQ],component_demand_ids=[NAT],response_format='symbolic',solution_relation=side,exact_boundary_expression='solve('+condition+',x)[0]',boundary_display_note='3sf displayed bound is approximate,not an exact replacement of the real solution cutoff.')
 return p
def roots(label,poly,domain,key,kp,original):
 p=v(label,'Intersection(solveset('+poly+',x,domain=S.Reals),'+domain+')',key,kp,'Derive the algebraic relation from the ORIGINAL natural logs,with every original argument positive. Solve all algebraic branches,then intersect with the original domain;do not retain an invalid root merely because its compressed product is positive.')
 p.update(original_equation=original,original_domain=domain,assessed_8227_demand_ids=[LAW],component_demand_ids=[NAT],response_format='symbolic')
 return p
def add(kind,n,note,parts):
 r=g.add(kind,n,424,note,parts);r['mapping_rationale']='Natural-log algebra applies the same common-base laws while retaining original argument domains. Rearranging a relationship and filtering roots are explicit requested outputs; a simplified formula does not extend its original domain.';return r
add('Example',24,'Solve5e^(2x+3)>1to3sf. Exact lower boundary(−ln5−3)/2has source display−2.30;strict>isretained.',[cutoff('inequality','log(5)+2*x+3','-Rational(23,10)','>',424)])
add('Try-Now',24,'Solve e^x<12 and2e^(5x−2)≥70to3sf. Keepstricta,inclusiveb,and exact internal cutoffsln12and(ln35+2)/5.',[cutoff('a','x-log(12)','Rational(62,25)','<',638),cutoff('b','5*x-2-log(35)','Rational(111,100)','>=',638)])
p=v('y-in-x','solve(y+5-x**2*y,y)[0]','5/(x**2-1)',424,'Original ln(y+5)−lny=2lnx requiresy>0andx>0. Exponentiating givesy+5=x²y,so y=5/(x²−1). Positivity ofythen requiresx>1. The other rational branches are not solutions of the original logarithmic relationship.')
p.update(assessed_8227_demand_ids=[LAW],component_demand_ids=[NAT],response_format='symbolic',original_domain='y>0,x>0;the resulting solution relation hasx>1.',author_answer_form='y=5/(x²−1),x>1.',source_domain_caution='The printed rational formula is correct on its original logarithmic domain;do not silently permitx<−1or0<x<1after rearrangement.')
add('Example',25,'Expressyintermsofxwithoutlogs fromln(y+5)−lny=2lnx. Preserve the original positivity and finalx>1branch with y5/(x²−1).',[p])
p=v('z-in-y','solve(p*y**2-(y+2),p)[0]','(y+2)/y**2',639,'Use the ORIGINAL lnz=ln(y+2)−2lnywithy>0. Common-base quotient/power laws yieldz=(y+2)/y²,automaticallypositive on that original domain.')
p.update(assessed_8227_demand_ids=[LAW],component_demand_ids=[NAT],response_format='symbolic',original_domain='y>0,z>0.',author_answer_form='z=(y+2)/y²,y>0.')
extra(p,'original-exponentiated-relation','simplify(((y+2)/y**2)*y**2-(y+2))','0')
add('Try-Now-25',1,'Expresszin terms ofywithoutlogs,with ORIGINALy>0. The denominator y²doesnotjustify including negativeywhere lnyisundefined.',[p])
ps=[roots('a','x*(2*x-1)-(4*x-3)','Interval.open(Rational(3,4),oo)','FiniteSet(1,Rational(3,2))',639,'ln(2x−1)=ln(4x−3)−lnx'),roots('b','x+7-(x+1)**2','Interval.open(-1,oo)','FiniteSet(2)',639,'ln(x+7)=2ln(x+1)'),roots('c','(x+3)**2-x*(2*x-2)','Interval.open(1,oo)','FiniteSet(9)',639,'2ln(x+3)−lnx=ln(2x−2)'),roots('d','3-x**2-x**2','Interval.open(0,sqrt(3))','FiniteSet(sqrt(Rational(3,2)))',639,'ln(3−x²)=2lnx')]
ps[-1]['printed_key_display']='sqrt(3/2)=1.22;retain exact radical as the primary value.'
add('Try-Now-25',2,'Four natural-log equations require original-domain filtering. Part(a)retainsboth1,3/2;parts(b),(c)reject extraneous negative algebraic roots;part(d)retains onlythepositive radical.',ps)
p=v('x-in-e','solve(3*x+1-E*(x+2),x)[0]','(2*E-1)/(3-E)',639,'Original ln(3x+1)−ln(x+2)=1requiresx>−1/3. Exponentiate the quotient to e,then solve(3−e)x=2e−1. Since1<e<3,the exact root is positive and satisfies the original domain.')
p.update(assessed_8227_demand_ids=[LAW],component_demand_ids=[NAT],response_format='symbolic',original_domain='x>−1/3.',requested_answer_form='in terms ofe')
extra(p,'original-quotient-at-exact-root','simplify((3*((2*E-1)/(3-E))+1)/(((2*E-1)/(3-E))+2))','E')
add('Try-Now-25',3,'Solve the original log difference and give the answer IN TERMS OFe,not a rounded decimal. Exact(2e−1)/(3−e)isin the original positive-argument domain.',[p])
refs=[(46,'Example24 natural-log inequality arrows','Divide by5,takeln,and retain the original exponent2x+3before isolatingx. A rounded boundary is display metadata.',[INEQ],'Example:24'),(47,'Example25 exponentiation and rearrangement','The original separate logs requirex,ypositive. Quotient(y+5)/y=x²leads to y5/(x²−1)onlyontheoriginalx>1branch.',[LAW],'Example:25')]
for n,label,note,teaches,parent in refs:
 fig(n,424,label,note,teaches,'table',[],parent);figures[-1].update(item_id=f'8227:TB:YM:C9:Teaching-figure:{n}',printed_page=pp(424),source_evidence=ev(424),value_level_scope_decisions=[],item_kind='teaching-figure',parent_item_id='8227:TB:YM:C9:'+parent)
 figures[-1]['mathematical_feature_review']['method']='Read original natural-log arguments and inequality signs;derive exact cutoffs,positive-domain restrictions and equivalent rational relationships independently.'
pages=[dict(pdf_page=424,printed_page=pp(424),chapter=9,page_status='items enumerated',item_ids=[r['item_id']for r in answers]+[r['item_id']for r in figures],continuation_item_ids=[],source_evidence=ev(424),reader='Codex author',date='2026-11-20',non_item_content='AllExamples24–25,Try24/Try25Q1–3andtwo method panels enumerated. Every requested original-domain root and exact answer form retained.',scope_screen='Natural-log algebra and exponential inequalities;no unsupported e/ln-to-arbitrary-base classification or learner change-of-base requirement.')]
def save():
 for name,data in [('answers-YM-C9-natural-equations.json',dict(scope='Complete424natural-log source responses and domains.',items=answers)),('census-YM-C9-natural-equations.json',dict(book='YM',book_id='8227-SRC-017',chapter=9,source_path=SRC,source_sha256=SHA,scope='Complete424page/item/reference census.',new_items=new+figures,corrections=corrections,pages=pages))]:
  (W/'tools/textbook-r5'/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
 for r in answers:
  for p in r['subparts']:
   if'operation'in p:assert equivalent(compute(p['operation']),expression(p['printed_key_normalised'])),(r['item_id'],p['subpart'])
   for name,op in p.get('additional_operations',{}).items():assert equivalent(compute(op),expression(p['additional_operation_expected'][name])),(r['item_id'],p['subpart'],name)
 print(len(answers),'items;',sum(len(r['subparts'])for r in answers),'responses;',len(figures),'references;',len(pages),'pages')
if __name__=='__main__':save()
