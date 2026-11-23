"""Goldie PDF104–105 log/exponential exposition, prompt and Examples5–6."""
import hashlib,json,sys
from pathlib import Path
from author_YM_C4_trig_graphs import value,reasoning
from author_Goldie_C4_opening import derivative
W=Path(__file__).resolve().parents[2];ROOT=W.parents[2]
sys.path.insert(0,str(W/'tools'))
from verify_textbook_answers_r5 import compute,expression,equivalent
SRC='sources/namibia/nsscas/8227-mathematics/textbooks/Goldie_Pure-Mathematics-2-and-3_2nd-edition_2018.pdf'
SHA='f030d64259ffe233a7408d2a64dea21c0a04f1ac0426439f5efaea694eb72e85'
ELEMENTARY='8227:2020:M2:T4:O01:D01';COMPOSITE='8227:2020:M2:T4:O01:D02';POWER='8227:2020:M1:T8:O02:D01'
INTEGRATE='8227:2020:M2:T5:O01:D01';REVERSE='8227:2020:M2:T5:O01:D03'
def ev(page):
    name='Goldie-key-C3-341'if page==342 else'Goldie-C4-102'
    p=W/f'checks/r5/textbooks/{name}.png';return {'path':str(p.relative_to(ROOT)),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
answers=[];new=[];corrections=[]
def add(kind,n,page,note,parts,direct,components=None,new_item=False):
    for p in parts:
        kp=p.pop('key_page_override',page);p.update(source_pdf_page=page,source_evidence=ev(page),answer_pdf_page=kp,
          answer_printed_page=kp-14,key_evidence=ev(kp),review_date='2026-11-18')
    row={'item_id':f'8227:TB:Goldie:C4:{kind}:{n}','source_pdf_page':page,'notes':note,
      'assessed_8227_demand_ids':direct,'component_demand_ids':components or[],
      'mapping_rationale':'The requested composite exponential derivative is assessed; standard elementary derivatives are its components. The nonzero-polynomial prompt asks a degree argument,not solving a logarithmic or exponential equation. Unprompted derivative/integration relationships are teaching evidence only.',
      'representation':'text','sketch_response_required':False,
      'value_level_scope_decisions':[{'rule_id':'8227:QUAL10','status':'within'if kind=='Prompt'else'not applicable','quoted_value':note,
        'reason':'Polynomial powers are nonnegative integers; leading coefficient is nonzero,including the constant case.'if kind=='Prompt'else'An exponential derivative or teaching relationship,not a power-rule restriction.'},
       {'rule_id':'8227:LIMIT06','status':'not applicable','quoted_value':note,'reason':'No change of logarithm base is used or requested.'}],
      'exam_style':False,'exam_style_basis':'Ordinary prompt/exposition/worked Example; no examination attribution.',
      'precision_angle_check':{'source':'Exact symbolic derivatives. The ln(x)/1/xreference usesx>0as the natural real-log branch.',
        'comparison':'Do not generalise the printedln(x)antiderivative to negative xwithoutln|x|andconnected-domain constants. This is a domain convention,not a new change-of-base demand.'},
      'expected_subpart_labels':[p['subpart']for p in parts],'subparts':parts}
    if not direct:row['evidence_role']='prerequisite/supporting conceptual task or teaching exposition; no directly assessed core-demand coverage'
    answers.append(row)
    if new_item:new.append({'item_id':row['item_id'],'item_kind':'prompt'if kind=='Prompt'else'worked-derivation','exercise':kind,'item_number':str(n),'pdf_page':page,'printed_page':page-14,
      'notes':note,'assessed_8227_demand_ids':[],'component_demand_ids':components or[],'teaches_8227_demand_ids':components or[],
      'representation':'text','source_evidence':ev(page),'evidence_role':row['evidence_role'],
      'answer_key':{'available':True,'pdf_pages':[342]if kind=='Prompt'else[104,105],'printed_pages':[328]if kind=='Prompt'else[90,91],'locator':'Polynomial prompt answer(Page90),PDF342'if kind=='Prompt'else'Inline natural-log/inverse-exponential differentiation exposition'},'learner_display':False})
    return row
p=reasoning('degree-argument','A nonzero polynomial cannot equal its own derivative identically.',
 'If degree n≥1and leading coefficienta_n≠0,the derivative has degreen−1andno x^nterm,so equality is impossible by coefficient comparison. Ifn=0,the polynomial is a nonzero constant andits derivative iszero,also unequal. The zero polynomial would be a counterexample without the source nonzero-leading-coefficient condition. The key degree argument is read with this constant boundary case made explicit.',342,'matches')
p['additional_operations']={'nonzero_constant_boundary':{'kind':'identity','operands':['diff(a,x)-a']}}
add('Prompt',7,104,'A polynomial f(x)=a_n*x^n+…+a_0ofordernhasnonzero leading coefficient. Explain whyf′cannot equal fidentically;include n=0nonzero-constant boundary. The task doesnot ask to solve a logarithmic or exponential equation.',[p],[],[POWER],new_item=True)
p=reasoning('standard-derivative-relationships','Onx>0,d(lnx)/dx=1/x;using inverse-function differentiation givesd(e^x)/dx=e^xfor all realx. Reverse differentiation gives the corresponding local antiderivatives.',
 'The source begins with∫(1/x)dx=lnxinthe positive real-log context. Thus ifx=lny,withy>0,then dx/dy=1/yis nonzero,so dy/dx=y=e^x. Reverse differentiation then verifies∫e^xdx=e^x+C. Thelnxprimitive is valid on positive intervals; a general real reciprocal primitive needsln|x|on each nonzero connected interval. This is exposition,not an explicitly asked integral or inverse problem.',105,'matches')
p['additional_operations']={'log_derivative':{'kind':'identity','operands':['diff(log(x),x)']},
 'exponential_derivative':{'kind':'identity','operands':['diff(exp(x),x)']},
 'log_positive_primitive_residual':{'kind':'identity','operands':['diff(log(x),x)-1/x']},
 'exponential_primitive_residual':{'kind':'identity','operands':['diff(exp(x),x)-exp(x)']}}
p['additional_operation_expected']={'log_derivative':'1/x','exponential_derivative':'exp(x)','log_positive_primitive_residual':'0','exponential_primitive_residual':'0'}
row=add('Worked-derivation',3,104,'Headingless derivative/integral relationship forlnxandexp(x)starts104andcontinues105:invertx=lnyforpositiveyto obtain the exponential derivative;retain the positive-log branch andintegrationconstant convention.',[p],[],[ELEMENTARY,INTEGRATE,REVERSE],True)
corrections.append({'item_id':row['item_id'],'continuation_pdf_pages':[105]})
add('Example',5,105,'Differentiate e^(5x)usingu=5xandthe chain rule. The inner derivative5multiplies the original exponential;it isnot moved into the exponent.',[
 derivative('derivative','exp(5*x)','5*exp(5*x)',105)],[COMPOSITE],[ELEMENTARY])
add('Example',6,105,'Differentiate4/e^(2x)by first rewriting it as4e^(−2x);the negative inner derivative−2gives−8e^(−2x).',[derivative('derivative','4/exp(2*x)','-8*exp(-2*x)',105)],[COMPOSITE],[ELEMENTARY])
figures=[]
for n,label,note,teaches,checks in[
 (9,'Natural-log/exponential differentiation–integration table','Two rows:lnx↦1/xandexp(x)↦exp(x)under differentiation;1/x↦lnx+Candexp(x)↦exp(x)+Cunder integration. The real-log row is positive-domain evidence; it doesnot supply the negative-domainln|x|case.',[ELEMENTARY,INTEGRATE,REVERSE],[('diff(log(x),x)','1/x'),('diff(exp(x),x)','exp(x)'),('diff(log(x)+a,x)','1/x'),('diff(exp(x)+a,x)','exp(x)')]),
 (10,'Affine-exponential derivative rule panel','For y=e^(ax),dy/dx=a*e^(ax),withaany realconstant. The zero coefficienta=0also works,giving derivativezero; no division byaisneeded.',[COMPOSITE,ELEMENTARY],[('diff(exp(a*x),x)','a*exp(a*x)'),('diff(exp(0*x),x)','0')])]:
    results=[]
    for original,target in checks:
        got=compute({'kind':'identity','operands':[original]});assert equivalent(got,expression(target));results.append({'operation':{'kind':'identity','operands':[original]},'source_normalised':target,'derived':str(got),'comparison':'author exact check agrees;independentacceptancepending'})
    figures.append({'item_id':f'8227:TB:Goldie:C4:Teaching-figure:{n}','item_kind':'teaching-figure','exercise':'Teaching figure','item_number':str(n),'pdf_page':105,'printed_page':91,
      'source_label':label,'notes':note,'what_it_shows':note,'assessed_8227_demand_ids':[],'component_demand_ids':[],'teaches_8227_demand_ids':teaches,
      'representation':'table','source_evidence':ev(105),'learner_display':False,
      'value_level_scope_decisions':[{'rule_id':'8227:LIMIT06','status':'not applicable','quoted_value':note,'reason':'Natural-log/exponential formula support;no change of logarithm base.'}],
      'value_level_scope_review_status_r5':'authoractualformulas/domainsread2026-11-18;independentacceptancepending',
      'exam_representation_check':{'status':'final cross-book/examination comparison pending','examination_part_ids':[],
        'relation':'Textbook teachingreference,notassessed practice orofficialaward/frequency evidence.'},
      'mathematical_feature_review':{'status':'authorrenderandexplicitderivativechecks;independentacceptancepending','method':'Differentiate each original fixed formula exactly,retainx>0forlnxandnonzeroconnecteddomainsforareciprocal primitive.','checks':results}})
pages=[]
for page in[104,105]:
    own=[r['item_id']for r in answers if r['source_pdf_page']==page]+[r['item_id']for r in figures if r['pdf_page']==page]
    if page==104:own+=['8227:TB:Goldie:C4:Exercise-4A:8','8227:TB:Goldie:C4:Teaching-figure:8']
    pages.append({'pdf_page':page,'printed_page':page-14,'chapter':4,'page_status':'items enumerated','item_ids':own,
     'continuation_item_ids':[r['item_id']for r in corrections if page in r['continuation_pdf_pages']],
     'source_evidence':ev(page),'non_item_content':'All4A8parts/givengraph,polynomialprompt,headinglesslog/exponentialexposition,referencepanels,andExamples5–6enumerated.4A8answerdetailsliveinthe4Asegment;thepagecensusiscombinedherewithoutduplicatingpage104.',
     'reader':'Codex author','date':'2026-11-18'})
if __name__=='__main__':
    for name,data in[
     ('answers-Goldie-C4-logs-intro.json',{'scope':'NewpolynomialPrompt7,headinglessderivationandExamples5–6,PDF104–105.','items':answers}),
     ('census-Goldie-C4-logs-intro.json',{'book':'Goldie','book_id':'8227-SRC-015','chapter':4,'source_path':SRC,'source_sha256':SHA,
      'scope':'Completepages104–105,including4A8/givengraphfromtheprevioussegment.','new_items':new+figures,'corrections':corrections,'pages':pages})]:
        (W/'tools/textbook-r5'/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
    print(len(answers),'items;',sum(len(r['subparts'])for r in answers),'outputs;',len(figures),'figures;6referenceformulachecks')
