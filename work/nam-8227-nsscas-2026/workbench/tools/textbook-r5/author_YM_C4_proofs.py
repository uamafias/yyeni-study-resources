"""Fixed-source proof readings, YM PDF197–201; not learner question generation."""
import json,hashlib
from pathlib import Path
W=Path(__file__).resolve().parents[2];ROOT=W.parents[2]
SRC='Y=mc as textbook.pdf';SHA='0b44ad3b67b1ea3de90cba780382d77deef347fae683cf6e28677f36c17a724f'
PROOF='8227:2020:M1:T6:O05:D01';REC='8227:2020:M2:T3:O01:D01'
def ev(page):
    name='YM-key-608-609-full'if page in[608,609]else'YM-key-610-611-full'if page==610 else'YM-C4-201'if page==201 else'YM-C4-197'
    p=W/f'checks/r5/textbooks/{name}.png'
    return {'path':str(p.relative_to(ROOT)),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
def proof(label,left,right,middle,domain,kp,worked=True):
    row={'subpart':label,'operation':{'kind':'trig-identity-residual','operands':[left,right]},
      'printed_key_normalised':'0','check_mode':'show/prove','proof_expressions':[left,*middle,right],
      'original_common_domain':domain,'key_page_override':kp,'review_date':'2026-11-18',
      'method':'Independently transform the original expression through the listed algebraic/trigonometric equalities. Each adjacent pair is checked symbolically. Preserve the original common domain through every cancellation; conclude the requested identity rather than assuming it as a starting equality.',
      'key_comparison':'Published worked proof read and mathematically checked; the independently derived equality chain may use a shorter valid route.'if worked else'The answer section prints only Prove. No publisher worked proof is available; the equality chain is author-derived, and the stated identity is independently checked.',
      'normalisation_note':'Zero is the independently computed LHS−RHS residual, not a verbatim publisher numerical answer.'}
    if not worked:
        row.update(key_presence='no separate key',key_absence_reason='The source answer entry says only Prove; no worked proof is supplied.',inspected_key_pdf_pages=[kp])
    return row
answers=[]
def add(kind,n,page,note,parts,reciprocal=False):
    for p in parts:
        kp=p.pop('key_page_override');worked='key_presence'not in p
        p.update(source_pdf_page=page,source_evidence=ev(page),answer_pdf_page=kp if worked else None,
          answer_printed_page=('A'+str(kp-586)if kp>=602 else kp-12)if worked else None,key_evidence=ev(kp))
    row={'item_id':f'8227:TB:YM:C4:{kind}:{n}','source_pdf_page':page,'notes':note,
      'assessed_8227_demand_ids':[PROOF]+([REC]if reciprocal else[]),'component_demand_ids':[],
      'mapping_rationale':'The explicit output is a proof, not solving for an angle or estimating roots. Basic Pythagorean/quotient identities establish the equality; where reciprocal functions occur, their relationship is also directly used. Algebraic expansion/factorisation are supporting steps, not automatically additional assessed8227demands.',
      'value_level_scope_decisions':[{'rule_id':'8227:LIMIT02','status':'not applicable','quoted_value':note,
        'reason':'An identity proof on its original common domain, not a general trigonometric equation solution.'}],
      'exam_style':False,'exam_style_basis':'Ordinary Example/TryNow, no examination attribution or exam-style label.',
      'precision_angle_check':{'source':'Symbolic identity, no calculator precision or numerical angle mode is requested.',
        'comparison':'All proof expressions share the same angle symbol after harmless renaming to x; preserve the source denominator restrictions, not an unrestricted equality of extended functions.'},
      'expected_subpart_labels':[p['subpart']for p in parts],'subparts':parts}
    answers.append(row)

add('Try-Now',31,197,'Prove(sinx−cosx)²≡1−2sinxcosx: square expansion and the Pythagorean pair, with no denominator restrictions.',[
 proof('proof','(sin(x)-cos(x))**2','1-2*sin(x)*cos(x)',
 ['sin(x)**2-2*sin(x)*cos(x)+cos(x)**2'],'all real x',608)])
add('Example',32,197,'Prove(sinA+cosA)(1−sinAcosA)≡sin³A+cos³A by grouping the four expansion terms and replacing1−sin²/1−cos².',[
 proof('proof','(sin(x)+cos(x))*(1-sin(x)*cos(x))','sin(x)**3+cos(x)**3',
 ['sin(x)*(1-cos(x)**2)+cos(x)*(1-sin(x)**2)'],'all real x',197)])
add('Try-Now',32,197,'Prove(sinA−sinAcosA)/(cosA−(1−sin²A))≡tanA; common factors1−cosA andcosA cannot vanish.',[
 proof('proof','(sin(x)-sin(x)*cos(x))/(cos(x)-(1-sin(x)**2))','tan(x)',
 ['sin(x)*(1-cos(x))/(cos(x)*(1-cos(x)))','sin(x)/cos(x)'],
 'cos(x) != 0 and cos(x) != 1; these are the original denominator/tangent restrictions',608,False)])
add('Example',33,197,'Prove sinθ/(1+cosθ)+(1+cosθ)/sinθ≡2cosecθ by an LCM, Pythagorean simplification and cancellation.',[
 proof('proof','sin(x)/(1+cos(x))+(1+cos(x))/sin(x)','2*csc(x)',
 ['(sin(x)**2+(1+cos(x))**2)/(sin(x)*(1+cos(x)))',
  '2*(1+cos(x))/(sin(x)*(1+cos(x)))','2/sin(x)'],
 'sin(x) != 0 and 1+cos(x) != 0; latter is already implied for real x by the former',197)],True)
add('Try-Now',33,198,'Three identity proofs: a paired fraction gives2secθ; a difference gives2tan²θ; a mixed sine/cosine pair gives1/(sin²θ−cos²θ). Denominators differ by part.',[
 proof('a','(1+sin(x))/cos(x)+cos(x)/(1+sin(x))','2*sec(x)',
 ['((1+sin(x))**2+cos(x)**2)/(cos(x)*(1+sin(x)))','2/cos(x)'],
 'cos(x) != 0 and 1+sin(x) != 0',608),
 proof('b','sin(x)/(1-sin(x))-sin(x)/(1+sin(x))','2*tan(x)**2',
 ['2*sin(x)**2/(1-sin(x)**2)','2*sin(x)**2/cos(x)**2'],
 '1-sin(x) != 0,1+sin(x) != 0,cos(x) != 0',608,False),
 proof('c','sin(x)/(sin(x)+cos(x))+cos(x)/(sin(x)-cos(x))','1/(sin(x)**2-cos(x)**2)',
 ['(sin(x)**2+cos(x)**2)/((sin(x)+cos(x))*(sin(x)-cos(x)))'],
 'sin(x)+cos(x) != 0 and sin(x)-cos(x) != 0',608,False)],True)
add('Example',34,198,'Show(1+secx)/(tanx+sinx)≡cosecx using sine/cosine fractions and factoring sinx(1+cosx); retain all original poles.',[
 proof('proof','(1+sec(x))/(tan(x)+sin(x))','csc(x)',
 ['(1+cos(x))/(sin(x)*(1+cos(x)))','1/sin(x)'],
 'cos(x) != 0,sin(x) != 0,tan(x)+sin(x) != 0; the latter excludes any cancelled zero denominator',198)],True)
add('Try-Now',34,198,'Prove three reciprocal identities: tanx+1/tanx; a quotient(tanx+1)/(sinxtanx+cosx); and(1+sinx)/(1+cosecx). Preserve each original domain.',[
 proof('a','tan(x)+1/tan(x)','1/(sin(x)*cos(x))',
 ['(sin(x)**2+cos(x)**2)/(sin(x)*cos(x))'],'sin(x) != 0 and cos(x) != 0',608),
 proof('b','(tan(x)+1)/(sin(x)*tan(x)+cos(x))','sin(x)+cos(x)',
 ['((sin(x)+cos(x))/cos(x))/((sin(x)**2+cos(x)**2)/cos(x))'],
 'cos(x) != 0 and sin(x)*tan(x)+cos(x) != 0; latter never vanishes where cos(x) != 0',608,False),
 proof('c','(1+sin(x))/(1+csc(x))','sin(x)',
 ['sin(x)*(1+sin(x))/(sin(x)+1)'],'sin(x) != 0 and sin(x) != -1',608,False)],True)
add('Example',35,199,'Prove(1/sinθ−1/tanθ)²≡(1−cosθ)/(1+cosθ): first combine terms, then square and use a difference of squares.',[
 proof('proof','(1/sin(x)-1/tan(x))**2','(1-cos(x))/(1+cos(x))',
 ['(1-cos(x))**2/sin(x)**2','(1-cos(x))**2/((1-cos(x))*(1+cos(x)))'],
 'sin(x) != 0,cos(x) != 0,tan(x) != 0 and1+cos(x) != 0; preserve the original tangent poles',199)],True)
add('Try-Now',35,199,'Seven identity proofs vary fraction aggregation,cancellation,squared differences and quotient differences; these are not seven cosmetic number substitutions.',[
 proof('a','sin(x)/(cot(x)+csc(x))','1-cos(x)',
 ['sin(x)**2/(1+cos(x))','(1-cos(x))*(1+cos(x))/(1+cos(x))'],
 'sin(x) != 0 and cot(x)+csc(x) != 0',609),
 proof('b','sin(x)*tan(x)/(1-cos(x))','1+1/cos(x)',
 ['sin(x)**2/(cos(x)*(1-cos(x)))','(1+cos(x))/cos(x)'],
 'cos(x) != 0 and1-cos(x) != 0',609,False),
 proof('c','(1/cos(x)-tan(x))**2','(1-sin(x))/(1+sin(x))',
 ['(1-sin(x))**2/cos(x)**2','(1-sin(x))**2/((1-sin(x))*(1+sin(x)))'],
 'cos(x) != 0 and1+sin(x) != 0',609,False),
 proof('d','sec(x)/(cot(x)+tan(x))','sin(x)',
 ['(1/cos(x))/((cos(x)**2+sin(x)**2)/(sin(x)*cos(x)))'],
 'sin(x) != 0,cos(x) != 0 andcot(x)+tan(x) != 0',609),
 proof('e','(1-tan(x)**2)/(1+tan(x)**2)','1-2*sin(x)**2',
 ['(cos(x)**2-sin(x)**2)/(cos(x)**2+sin(x)**2)','cos(x)**2-sin(x)**2'],
 'cos(x) != 0; 1+tan(x)**2 is positive wherever defined',609,False),
 proof('f','(1-sec(x)**2)/((1+cos(x))*(1-cos(x)))','-sec(x)**2',
 ['-tan(x)**2/sin(x)**2','-1/cos(x)**2'],'sin(x) != 0 andcos(x) != 0',609,False),
 proof('g','(cot(x)-tan(x))/(cot(x)+tan(x))','cos(x)**2-sin(x)**2',
 ['(cos(x)**2-sin(x)**2)/(cos(x)**2+sin(x)**2)'],
 'sin(x) != 0,cos(x) != 0 andcot(x)+tan(x) != 0',609,False)],True)
add('Example',36,200,'Prove(1−sinβ)/cosβ≡cosβ/(1+sinβ) by multiplying by the conjugate(1+sinβ)/(1+sinβ).',[
 proof('proof','(1-sin(x))/cos(x)','cos(x)/(1+sin(x))',
 ['(1-sin(x)**2)/(cos(x)*(1+sin(x)))','cos(x)**2/(cos(x)*(1+sin(x)))'],
 'cos(x) != 0 and1+sin(x) != 0',200)])
add('Try-Now',36,200,'Six proofs include a conjugate quotient,tan−cot,a cancelled sine denominator,a squared reciprocal sum,a mixed square identity,and a difference of weighted ratios.',[
 proof('a','(1-cos(x))/sin(x)','sin(x)/(1+cos(x))',
 ['(1-cos(x)**2)/(sin(x)*(1+cos(x)))'],'sin(x) != 0 and1+cos(x) != 0',609),
 proof('b','(1-2*cos(x)**2)/(sin(x)*cos(x))','tan(x)-cot(x)',
 ['(sin(x)**2-cos(x)**2)/(sin(x)*cos(x))'],'sin(x) != 0 andcos(x) != 0',609,False),
 proof('c','1+cos(x)**2/(sin(x)-1)','-sin(x)',
 ['1+(1-sin(x))*(1+sin(x))/(sin(x)-1)'],'sin(x) != 1',609,False),
 proof('d','(1+cos(x))/(1-cos(x))','(csc(x)+cot(x))**2',
 ['(1+cos(x))**2/sin(x)**2'],'sin(x) != 0 and1-cos(x) != 0',609),
 proof('e','(1-cos(x)**2)/(1-sin(x)**2)+tan(x)*cot(x)','sec(x)**2',
 ['sin(x)**2/cos(x)**2+1'],'sin(x) != 0 andcos(x) != 0',609,False),
 proof('f','(3*sin(x)+cos(x))/sin(x)-(3*cos(x)-sin(x))/cos(x)','sec(x)*csc(x)',
 ['cos(x)/sin(x)+sin(x)/cos(x)','1/(sin(x)*cos(x))'],
 'sin(x) != 0 andcos(x) != 0',609,False)],True)

add('Example',37,201,'Prove(1−tan²θ)/(1+tan²θ)≡cos⁴θ−sin⁴θ by simplifying the two sides independently to cos²θ−sin²θ.',[
 proof('proof','(1-tan(x)**2)/(1+tan(x)**2)','cos(x)**4-sin(x)**4',
 ['(cos(x)**2-sin(x)**2)/(cos(x)**2+sin(x)**2)','cos(x)**2-sin(x)**2',
  '(cos(x)**2+sin(x)**2)*(cos(x)**2-sin(x)**2)'],
 'cos(x) != 0; the RHS alone also exists at excluded tangent poles, but those are outside the original equality domain',201)])
add('Try-Now',37,201,'Eight proofs include reciprocal products,equality via a common expression,quotient differences,fourth powers,and an expanded mixed fourth-power form. Some original domains are narrower than their simplified polynomials.',[
 proof('a','sin(x)*sec(x)*csc(x)*cos(x)','tan(x)*cot(x)',['1'],'sin(x) != 0 andcos(x) != 0',609,False),
 proof('b','1+1/cos(x)','tan(x)**2/(sec(x)-1)',
 ['(1+cos(x))/cos(x)','sin(x)**2/(cos(x)*(1-cos(x)))'],
 'cos(x) != 0 andcos(x) != 1',610),
 proof('c','sec(x)-cos(x)','tan(x)*sin(x)',['(1-cos(x)**2)/cos(x)','sin(x)**2/cos(x)'],
 'cos(x) != 0',610,False),
 proof('d','tan(x)+cot(x)','sec(x)*csc(x)',
 ['(sin(x)**2+cos(x)**2)/(sin(x)*cos(x))','1/(sin(x)*cos(x))'],
 'sin(x) != 0 andcos(x) != 0',610,False),
 proof('e','cos(x)**2-sin(x)**2','cos(x)**4-sin(x)**4',
 ['(cos(x)**2+sin(x)**2)*(cos(x)**2-sin(x)**2)'],'all real x',610),
 proof('f','sin(x)/(1+cos(x))','csc(x)-cot(x)',
 ['sin(x)*(1-cos(x))/(1-cos(x)**2)','(1-cos(x))/sin(x)'],
 'sin(x) != 0 and1+cos(x) != 0',610),
 proof('g','sec(x)**4-tan(x)**4','(1+sin(x)**2)/cos(x)**2',
 ['(sec(x)**2-tan(x)**2)*(sec(x)**2+tan(x)**2)','(1+sin(x)**2)/cos(x)**2'],
 'cos(x) != 0',610,False),
 proof('h','(tan(x)-cot(x))/(tan(x)+cot(x))','2*sin(x)**4+2*sin(x)**2*cos(x)**2-sin(x)**2-cos(x)**2',
 ['sin(x)**2-cos(x)**2','2*sin(x)**2-1',
  '(2*sin(x)**2-1)*(sin(x)**2+cos(x)**2)'],
 'sin(x) != 0 andcos(x) != 0; tan(x)+cot(x) cannot vanish on that domain',610)],True)

figure={'item_id':'8227:TB:YM:C4:Teaching-figure:121','item_kind':'teaching-figure','exercise':'Teaching figure','item_number':'121',
 'pdf_page':200,'printed_page':188,'source_label':'Two independent sides to a common expression proof flow',
 'notes':'LHS andRHS are simplified independently to the same expression,then equality is concluded. This is a proof organisation diagram, not permission to assume the required equality.',
 'what_it_shows':'Two simplification arrows converge on a common expression,followed by LHS=RHS.',
 'assessed_8227_demand_ids':[],'component_demand_ids':[],'teaches_8227_demand_ids':[PROOF],
 'representation':'diagram','source_evidence':ev(200),'learner_display':False,
 'value_level_scope_decisions':[{'rule_id':'8227:LIMIT02','status':'not applicable','quoted_value':'LHS andRHS simplify separately to the same expression','reason':'Proof structure,not a general angle solution.'}],
 'value_level_scope_review_status_r5':'author proof-structure diagram read2026-11-18; independent check pending',
 'exam_representation_check':{'status':'final cross-book/examination comparison pending','examination_part_ids':[],
  'relation':'Teaching a proof method does not establish that this flow diagram is an examination question representation.'},
 'mathematical_feature_review':{'status':'author logic checked; independent acceptance pending',
  'method':'Transitivity of equality is valid when each independent simplification is justified on the original common domain. Example37 immediately demonstrates the structure.'}}
pages=[]
for page in range(197,202):
 pages.append({'pdf_page':page,'printed_page':page-12,'chapter':4,'page_status':'items enumerated',
  'item_ids':[r['item_id']for r in answers if r['source_pdf_page']==page]+([figure['item_id']]if page==200 else[]),
  'continuation_item_ids':[],'source_evidence':ev(page),
  'non_item_content':'All worked andTryNow proofs enumerated; the only separate teaching diagram is the proof flow onPDF200. Handwritten annotations/contact labels are not publisher instructions.',
  'reader':'Codex author','date':'2026-11-18'})
if __name__=='__main__':
 for name,data in[
  ('answers-YM-C4-proofs.json',{'scope':'All13formal proof items onPDF197–201; all35requested proofs. Prove-only keys explicitly have no publisher worked solution.','items':answers}),
  ('census-YM-C4-proofs.json',{'book':'YM','book_id':'8227-SRC-017','chapter':4,'source_path':SRC,'source_sha256':SHA,
   'scope':'PDF197–201 inclusive; formal proofs and the separate proof-flow teaching diagram.','new_items':[figure],'corrections':[],'pages':pages})]:
  (W/'tools/textbook-r5'/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
 print(len(answers),'items;',sum(len(r['subparts'])for r in answers),'proofs')
