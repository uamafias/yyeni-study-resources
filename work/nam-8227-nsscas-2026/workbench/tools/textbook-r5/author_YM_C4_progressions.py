"""Fixed-source progression/trigonometry connections on YM PDF214."""
import hashlib,json
from pathlib import Path
from author_YM_C4_trig_graphs import value,reasoning
from author_YM_C4_composite_equations import roots
W=Path(__file__).resolve().parents[2];ROOT=W.parents[2]
SRC='Y=mc as textbook.pdf';SHA='0b44ad3b67b1ea3de90cba780382d77deef347fae683cf6e28677f36c17a724f'
AP='8227:2020:M1:T2:O03:D01';CONV='8227:2020:M1:T2:O05:D01';SUM='8227:2020:M1:T2:O05:D02'
BND='8227:2020:M1:T6:O06:D01';ALL='8227:2020:M1:T6:O06:D02';EXACT='8227:2020:M1:T6:O03:D01'
def ev(page):
    name='YM-C4-213'if page==214 else'YM-key-612-613-full'
    p=W/f'checks/r5/textbooks/{name}.png'
    return {'path':str(p.relative_to(ROOT)),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
answers=[]
def add(kind,n,note,parts,direct,components=None):
    for p in parts:
        kp=p.pop('key_page_override',613)
        p.update(source_pdf_page=214,source_evidence=ev(214),answer_pdf_page=kp,
          answer_printed_page='A'+str(kp-586)if kp>=602 else kp-12,key_evidence=ev(kp),review_date='2026-11-18')
    row={'item_id':f'8227:TB:YM:C4:{kind}:{n}','source_pdf_page':214,'notes':note,
      'assessed_8227_demand_ids':direct,'component_demand_ids':components or[],
      'mapping_rationale':'Classify the requested AP sum,GP convergence or sum to infinity. A trigonometric intermediate does not automatically add a separately assessed exact-value/identity objective. Try51Q1 explicitly asks the angle values after forming the AP sum equation,so its bounded solving is also assessed.',
      'value_level_scope_decisions':[{'rule_id':'8227:QUAL03','status':'within'if kind=='Try-Now-51'and n==1 else'not applicable',
        'quoted_value':note,'reason':'The AP angle equation uses a single argument x (multiplier1).'if kind=='Try-Now-51'and n==1 else'These are progression sums and convergence inequalities,not general trigonometric equation forms.'}],
      'exam_style':False,'exam_style_basis':'Ordinary Example/TryNow without exam attribution or an exam-style label.',
      'precision_angle_check':{'source':'Original radian intervals and exact-in-π convergence boundaries retained. Try51Q1key uses3significant figures for its numerical angles.',
        'comparison':'The strict GP condition is|r|<1. An equality boundary does not become convergent merely because the source interval includes it.'},
      'expected_subpart_labels':[p['subpart']for p in parts],'subparts':parts}
    if components:row['component_demand_roles']={EXACT:'Part(b)uses the exact tangent atπ/6to calculate the GP ratio; no separate exact-ratio answer is asked.'}
    answers.append(row);return row
p=value('a','0','Tuple(10,45)',214,'From the original AP first term1,second termcos²x andn=10,derive S10=10/2[2+9(cos²x−1)]. Extract a andb in the requested a−b sin²x form independently; verify that form for every x.')
p['operation']={'kind':'sine-square-form-coefficients','operands':['10*(2+9*(cos(x)**2-1))/2']}
p2=reasoning('b','π/6 < x < 5π/6',
 'The GP ratio isr=2cosx/√3. Convergence requires−1<r<1,so−√3/2<cosx<√3/2. Cosine is strictly decreasing on[0,π],with the two boundary values atπ/6and5π/6. Both boundaries are excluded because they give|r|=1.',214,'matches')
add('Example',51,'(a)AP first terms1,cos²x;express S10=a−b sin²x andfinda,b. (b)GP first terms√3,2cosx for0≤x≤π;find every x giving convergence. These are two connected source parts with different progression decisions.',[p,p2],[AP,CONV])
add('Try-Now-51',1,'An AP starts cosx,cosx+sin²x with0<x<π andS13=52. Derive its common difference sin²x,form the sum equation,andfind both possible radian angles.',[
 roots('roots','13*(2*cos(x)+12*sin(x)**2)/2-52',['0.841','2.09'],613,
  [('cos','x','2/3',1),('cos','x','-1/2',1)],unit='radian',hi='pi',approx=True,opened=True)],[AP,BND,ALL])
p=reasoning('a','0 < x < π/3',
 'Here r=tan²x/3 and0<x<π/2,so r>0 and convergence reduces to tan²x<3. Tangent is positive and strictly increasing on this interval,therefore tanx<√3 exactly when x<π/3. Retain the original lower bound0. The printed key introduces√(−3)as a lower bound after taking roots; that step is not a real inequality. Its final upper boundπ/3is nevertheless correct within the original domain.',613,'key wrong')
p['comparison_scope']='Final convergence interval agrees after carrying the original domain; the published intermediate radical step is mathematically invalid.'
p2=value('b','1/(1-tan(pi/6)**2/3)','9/8',613,
 'At the original x=π/6,tan²x=1/3,sor=1/9. Since|r|<1,the first term1gives S∞=1/(1−1/9)=9/8. Derive this from the original terms,not from the key.')
add('Try-Now-51',2,'A GP starts1,(tan²x)/3 with0<x<π/2. (a)Find its convergence interval. (b)Atx=π/6find the exact sum to infinity. The answer key has an invalid intermediate negative radicand in(a).',[p,p2],[CONV,SUM],[EXACT])
figures=[]
for n,label,note in[
 (149,'Example51b exact-reference triangle','A30°/60°triangle with sides1,√3,2supports the GP boundary cos(π/6)=√3/2.'),
 (150,'Example51b restricted cosine CAST','The source0≤x≤πinterval excludes quadrantsIII/IV; convergence lies strictly between theπ/6and5π/6rays.')]:
 figures.append({'item_id':f'8227:TB:YM:C4:Teaching-figure:{n}','item_kind':'teaching-figure','exercise':'Teaching figure','item_number':str(n),
  'pdf_page':214,'printed_page':202,'source_label':label,'parent_item_id':'8227:TB:YM:C4:Example:51','parent_subpart':'b',
  'notes':note,'what_it_shows':note,'assessed_8227_demand_ids':[],'component_demand_ids':[],
  'teaches_8227_demand_ids':[CONV,EXACT],'representation':'diagram','source_evidence':ev(214),'learner_display':False,
  'value_level_scope_decisions':[{'rule_id':'8227:QUAL03','status':'not applicable','quoted_value':note,'reason':'GP convergence-boundary teaching,not a general trigonometric solution form.'}],
  'value_level_scope_review_status_r5':'author side lengths,exact reference angle andstrict boundary rays checked2026-11-18; independent check pending',
  'exam_representation_check':{'status':'final cross-book/examination comparison pending','examination_part_ids':[],
    'relation':'A mathematical teaching diagram supporting GP convergence; no direct examination-frequency claim.'},
  'mathematical_feature_review':{'status':'author features checked with the independent convergence derivation; independent acceptance pending',
    'method':'The triangle gives the exact cosine boundary; substituting either boundary yields r=±1,so neither ray belongs to the convergent set.'}})
page={'pdf_page':214,'printed_page':202,'chapter':4,'page_status':'items enumerated',
 'item_ids':[r['item_id']for r in answers]+[r['item_id']for r in figures],'continuation_item_ids':[],
 'source_evidence':ev(214),'non_item_content':'All formal progression/trigonometry tasks and both separate solution diagrams enumerated.',
 'reader':'Codex author','date':'2026-11-18'}
if __name__=='__main__':
 for name,data in[
  ('answers-YM-C4-progressions.json',{'scope':'All3formal items andall5part outputs onPDF214; manual interval proofs explicitly distinguished from executable calculations.','items':answers}),
  ('census-YM-C4-progressions.json',{'book':'YM','book_id':'8227-SRC-017','chapter':4,'source_path':SRC,'source_sha256':SHA,
   'scope':'PDF214; allformal tasks and both separate mathematical solution diagrams.','new_items':figures,'corrections':[],'pages':[page]})]:
  (W/'tools/textbook-r5'/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
 print(len(answers),'items;',len(figures),'figures;',sum(len(r['subparts'])for r in answers),'outputs')
