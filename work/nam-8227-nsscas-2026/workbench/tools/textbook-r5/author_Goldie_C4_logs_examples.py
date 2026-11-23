"""Fixed-source log/exponential examples and graph prompt, PDF106–107."""
import hashlib,json,sys
from pathlib import Path
from author_YM_C4_trig_graphs import value,reasoning
from author_Goldie_C4_opening import derivative
W=Path(__file__).resolve().parents[2];ROOT=W.parents[2]
sys.path.insert(0,str(W/'tools'))
from verify_textbook_answers_r5 import compute,expression,equivalent
SRC='sources/namibia/nsscas/8227-mathematics/textbooks/Goldie_Pure-Mathematics-2-and-3_2nd-edition_2018.pdf'
SHA='f030d64259ffe233a7408d2a64dea21c0a04f1ac0426439f5efaea694eb72e85'
ELEMENTARY='8227:2020:M2:T4:O01:D01';COMPOSITE='8227:2020:M2:T4:O01:D02';QUOTIENT='8227:2020:M2:T4:O02:D02'
POWER='8227:2020:M1:T8:O02:D01';LOGGRAPH='8227:2020:M2:T2:O02:D02';LOGLAW='8227:2020:M2:T2:O01:D02';DOMAIN='8227:2020:M1:T3:O02:D01'
def ev(page):
    name='Goldie-key-C3-341'if page==342 else'Goldie-C4-106'
    p=W/f'checks/r5/textbooks/{name}.png';return {'path':str(p.relative_to(ROOT)),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
answers=[]
def add(kind,n,page,note,parts,direct,components=None):
    for p in parts:
        kp=p.pop('key_page_override',page);p.update(source_pdf_page=page,source_evidence=ev(page),answer_pdf_page=kp,
          answer_printed_page=kp-14,key_evidence=ev(kp),review_date='2026-11-18')
    row={'item_id':f'8227:TB:Goldie:C4:{kind}:{n}','source_pdf_page':page,'notes':note,
      'assessed_8227_demand_ids':direct,'component_demand_ids':components or[],
      'mapping_rationale':'Differentiate the actual function with its original real domain. A log-law alternative is a component unless the law itself is requested. The graph prompt assesses a natural-log graph relationship and explicit domain,not every facet of the inverse-graph demand.',
      'representation':'text','sketch_response_required':False,
      'value_level_scope_decisions':[{'rule_id':'8227:QUAL10','status':'within'if kind=='Example'and n in[7,9]else'not applicable','quoted_value':note,
        'reason':'The inner polynomial powers are2or4,so rational-power restrictions are respected.'if kind=='Example'and n in[7,9]else'No power-rule scope boundary is involved.'},
       {'rule_id':'8227:QUAL07','status':'within'if kind=='Prompt'else'not applicable','quoted_value':note,
        'reason':'Both natural logarithms requirex>0,a simple positive-domain condition.'if kind=='Prompt'else'Original real domains are retained for differentiation;no separate range determination is asked.'},
       {'rule_id':'8227:LIMIT06','status':'not applicable','quoted_value':note,'reason':'No logarithm-base change.'}],
      'exam_style':False,'exam_style_basis':'Ordinary worked Example or prompt without an examination attribution.',
      'precision_angle_check':{'source':'Exact algebraic/natural-log/exponential answers;no angle or rounding.',
        'comparison':'ln(x^4)has domainx≠0;the source working4lnxloses its negative branch. Do not silently restrict the original function to make a convenient log law valid.'},
      'expected_subpart_labels':[p['subpart']for p in parts],'subparts':parts}
    if kind=='Prompt':row['direct_demand_aspects']=[{'demand_id':LOGGRAPH,'assessed_facet':'Natural-log graph translation/shape only;no exponential inverse construction is asked.'}]
    answers.append(row);return row
add('Example',7,106,'Differentiate3e^(x²+1)byu=x²+1;the inner derivative2xgives6x*e^(x²+1). This is a composite exponential,not a logarithmic-equation task.',[
 derivative('derivative','3*exp(x**2+1)','6*x*exp(x**2+1)',106)],[COMPOSITE],[ELEMENTARY,POWER])
p=derivative('ii','log(3*x)','1/x',106,'x>0.')
p['additional_operations']={'alternative_log_law_derivative':{'kind':'identity','operands':['diff(log(3)+log(x),x)']}}
p['additional_operation_expected']={'alternative_log_law_derivative':'1/x'}
add('Example',8,106,'Differentiate2lnxandln(3x),bothx>0. The latter may use chain rule or the valid positive-domain identityln(3x)=ln3+lnx.',[
 derivative('i','2*log(x)','2/x',106,'x>0.'),p],[ELEMENTARY,COMPOSITE])
p=reasoning('shape','y=ln(3x)is the graph ofy=lnxtranslated vertically upward byln3;they have the same shape andgradient function onx>0.',
 'Onx>0,the log law givesln(3x)=ln3+lnx. A constant vertical difference leaves the gradient unchanged. Equal gradients alone imply only a constant difference on a connected interval,not identical functions. The key gives this translation.',342,'matches')
p['additional_operations']={'gradient_difference':{'kind':'identity','operands':['diff(log(3*x),x)-diff(log(x),x)']}}
p['additional_operation_expected']={'gradient_difference':'0'}
p2=value('domain','0','Interval.open(0,oo)',342,'Require3x>0andx>0for the two real logarithms;their common domain isx>0.')
p2['operation']={'kind':'real-function-domain','operands':['log(3*x)+log(x)']}
add('Prompt',2,106,'ln(3x)andlnxhave the same gradient function:explain the relationship between the curves andstate thex-values for which it is valid. Their common domain isx>0;the vertical difference isln3.',[p,p2],[LOGGRAPH,DOMAIN],[LOGLAW])
p=derivative('i','log(x**4)','4/x',107,'Original real domainx≠0,both positive andnegative components.')
p['author_source_working_comparison']={'status':'key incomplete','observed_step':'The source rewritesln(x^4)=4ln(x)without a positive-xrestriction.',
 'correct_step':'For all realx≠0,use ln(x^4)=4ln|x|,or differentiate the original composite directly. The printed final derivative4/xis correct.',
 'reason':'Atx=−1,the original real logarithm isln1=0butln(−1)is not real. The stated working drops a valid negative-domain branch without saying so;the final derivative remains correct.'}
p['additional_operations']={'original_domain':{'kind':'real-function-domain','operands':['log(x**4)']},
 'negative_input_original':{'kind':'identity','operands':['log((-1)**4)']},
 'negative_input_printed_working_complex_extension':{'kind':'identity','operands':['4*log(-1)']}}
p['additional_operation_expected']={'original_domain':'Union(Interval.open(-oo,0),Interval.open(0,oo))','negative_input_original':'0','negative_input_printed_working_complex_extension':'4*I*pi'}
add('Example',9,107,'Differentiateln(x^4)andln(x²+1). The first is defined on bothx<0andx>0;the source final derivative4/xis correct but its4lnxworking omits the negative branch. The second has all-real domain andderivative2x/(x²+1).',[
 p,derivative('ii','log(x**2+1)','2*x/(x**2+1)',107)],[COMPOSITE],[ELEMENTARY,POWER])
add('Example',10,107,'Differentiate(lnx)/xforx>0;the quotient calculation gives(1−lnx)/x². The equivalent productlnx*x^−1is a valid alternative;the problem doesnot explicitly force one rule.',[
 derivative('derivative','log(x)/x','(1-log(x))/x**2',107,'x>0.')],[QUOTIENT],[ELEMENTARY])
figures=[]
for n,label,note,checks in[
 (11,'Logarithm derivative summary panel','Foralnx,ln(ax),andln(f(x)),derivatives area/x,1/x,andf′/f. Keepx>0foralnx;ax>0witha≠0forln(ax);f(x)>0forreal ln(f(x)). The printed1/xrule doesnot make ln(ax)defined whena=0.',[
  ('diff(a*log(x),x)','a/x'),('diff(log(a*x),x)','1/x')]),
 (12,'Exponential derivative summary panel','For a*e^x,e^(ax),ande^(f(x)),derivatives area*e^x,a*e^(ax),andf′*e^f. Real coefficientacan bezero;the constant exponential case still fits.',[
  ('diff(a*exp(x),x)','a*exp(x)'),('diff(exp(a*x),x)','a*exp(a*x)')])]:
    results=[]
    for expr,target in checks:
        got=compute({'kind':'identity','operands':[expr]});assert equivalent(got,expression(target));results.append({'operation':{'kind':'identity','operands':[expr]},'source_normalised':target,'derived':str(got)})
    figures.append({'item_id':f'8227:TB:Goldie:C4:Teaching-figure:{n}','item_kind':'teaching-figure','exercise':'Teaching figure','item_number':str(n),'pdf_page':107,'printed_page':93,
     'source_label':label,'notes':note,'what_it_shows':note,'assessed_8227_demand_ids':[],'component_demand_ids':[],'teaches_8227_demand_ids':[ELEMENTARY,COMPOSITE],
     'representation':'table','source_evidence':ev(107),'learner_display':False,
     'value_level_scope_decisions':[{'rule_id':'8227:LIMIT06','status':'not applicable','quoted_value':note,'reason':'Derivative reference,not change of base.'}],
     'value_level_scope_review_status_r5':'author source coefficients/domains read2026-11-18;independent check pending',
     'exam_representation_check':{'status':'final cross-book/examination comparison pending','examination_part_ids':[],
       'relation':'Internal teaching support;not official award or examination-frequency evidence.'},
     'mathematical_feature_review':{'status':'author source render and exact derivative/domain checks;independent acceptance pending',
       'method':'Check every given numeric/general coefficient derivative;for generic differentiablef,the chain rule givesf′/forf′exp(f)on the stated real domains. The original log argument must stay positive.','checks':results}})
pages=[{'pdf_page':page,'printed_page':page-14,'chapter':4,'page_status':'items enumerated',
 'item_ids':[r['item_id']for r in answers if r['source_pdf_page']==page]+[r['item_id']for r in figures if r['pdf_page']==page],
 'continuation_item_ids':[],'source_evidence':ev(page),'non_item_content':'AllExamples7–10,prompt2andtwoformula-referencepanelsenumerated. The alternative log-law note belongs toExample8(ii);it isnot a separate assessed question.',
 'reader':'Codex author','date':'2026-11-18'}for page in[106,107]]
if __name__=='__main__':
    for name,data in[
     ('answers-Goldie-C4-logs-examples.json',{'scope':'AllPDF106–107tasks;originalfunctiondomainsretained.','items':answers}),
     ('census-Goldie-C4-logs-examples.json',{'book':'Goldie','book_id':'8227-SRC-015','chapter':4,'source_path':SRC,'source_sha256':SHA,
      'scope':'Everytask/referencepanelon106–107.','new_items':figures,'corrections':[],'pages':pages})]:
        (W/'tools/textbook-r5'/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
    print(len(answers),'items;',sum(len(r['subparts'])for r in answers),'outputs;',len(figures),'figures;4referenceformulachecks')
