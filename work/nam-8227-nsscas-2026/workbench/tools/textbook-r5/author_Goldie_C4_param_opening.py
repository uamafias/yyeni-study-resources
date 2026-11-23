"""Parametric ride exposition and extra-scope physical prompt, PDF122–123."""
import hashlib,json,sys
from pathlib import Path
from author_YM_C4_trig_graphs import value,reasoning
W=Path(__file__).resolve().parents[2];ROOT=W.parents[2]
sys.path.insert(0,str(W/'tools'))
from verify_textbook_answers_r5 import compute,expression,equivalent
SRC='sources/namibia/nsscas/8227-mathematics/textbooks/Goldie_Pure-Mathematics-2-and-3_2nd-edition_2018.pdf'
SHA='f030d64259ffe233a7408d2a64dea21c0a04f1ac0426439f5efaea694eb72e85'
PARAM='8227:2020:M2:T4:O03:D02'
TRIANGLE='8227:PRIOR:NSSCO:right-triangle-trig';COORD='8227:PRIOR:NSSCO:coordinate-geometry'
def ev(page):
    name='Goldie-key-C3-341'if page==344 else'Goldie-C4-122'
    p=W/f'checks/r5/textbooks/{name}.png';return {'path':str(p.relative_to(ROOT)),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
answers=[]
def add(kind,n,page,note,parts,components):
    for p in parts:
        kp=p.pop('key_page_override',123);pp=p.pop('source_page_override',None)or page
        p.update(source_pdf_page=pp,source_evidence=ev(pp),answer_pdf_page=kp,answer_printed_page=kp-14,key_evidence=ev(kp),review_date='2026-11-18')
    row={'item_id':f'8227:TB:Goldie:C4:{kind}:{n}','source_pdf_page':page,'notes':note,'assessed_8227_demand_ids':[],'component_demand_ids':components,
      'mapping_rationale':'The position equations and plotting are prerequisite representation for later parametric calculus,not an assessed derivative. The greatest-sensations prompt is outside the prescribed mathematical demand and lacks a physical motion/force criterion.',
      'evidence_role':'prerequisite/supporting teaching context;no directly assessed calculus coverage','representation':'diagram'if kind!='Prompt'else'graph','sketch_response_required':False,
      'value_level_scope_decisions':[{'rule_id':'8227:QUAL03','status':'not applicable','quoted_value':note,'reason':'Parametric position/plotting or informal physical context,not finite trig-equation solving.'}],
      'exam_style':False,'exam_style_basis':'Unprompted chapter exposition or informal prompt;no examination attribution.',
      'precision_angle_check':{'source':'Lengths/positions are metres;the plotting examples use degree labels0°,30°etc. The conditional acceleration audit explicitly uses radianθandisnot a learner demand.',
        'comparison':'Keep exact original coordinates;compare the displayed3.46at its written2decimalplaces. Do not copy a degree parameter into an unscaled radian derivative or infer a time law from a static path.'},
      'expected_subpart_labels':[p['subpart']for p in parts],'subparts':parts}
    answers.append(row);return row
p=reasoning('position-formulas','x=4cosθ+2cos3θ,y=4sinθ+2sin3θ,with positions inmetres.',
 'The first rodOAhaslength4andabsoluteangleθ. The second rodAPhaslength2andhasrotated2θrelative toOA,so its absoluteangleisθ+2θ=3θ. Add the two horizontal projections andthetwoverticalprojections. The formula is teaching exposition;no derivative is asked.',123,'matches');p['source_page_override']=123
p2=value('at-0-degrees','Tuple(4*cos(0)+2*cos(0),4*sin(0)+2*sin(0))','Tuple(6,0)',123);p2['source_page_override']=123
X30='4*cos(pi/6)+2*cos(pi/2)';Y30='4*sin(pi/6)+2*sin(pi/2)'
p3=value('at-30-degrees-x',X30,'3.46',123,'Derive the exact degree30coordinate2√3fromthe original two-rod formula,thencompare the printed3.46atitswritten2dp. The source intermediate3.464isrounded;it isnot reused as an exact input.')
p3['operation']={'kind':'rounded','operands':[X30],'decimal_places':2};p3['source_page_override']=123
p3['additional_operations']={'exact_coordinate':{'kind':'identity','operands':[X30]}}
p4=value('at-30-degrees-y',Y30,'4',123);p4['source_page_override']=123
row=add('Worked-illustration',1,122,'Headingless parametric ride exposition:two rods4m/2m,firstangleθandsecondrelativeangle2θ,give absolute second angle3θ. It supplies position formulas,two degree-labelled numerical examples anda full-cycle labelled path;it doesnot ask for a derivative.',[p,p2,p3,p4],[TRIANGLE,COORD])
row['source_interpretation']={'teaching_context_demand_id':PARAM,'component_role':'Actual components are right-triangle projections andcoordinate addition;the exposition prepares parametric differentiation butdoesnot use orassess that derivative.','units':'metres for x,y;degrees in the displayed plotting samples.'}
p=reasoning('physical-criterion','No unique calculative location of greatest felt sensations follows from the static path alone;additional motion/force assumptions and a definition of the sensation are needed.',
 'The source key suggests where the rate ofchangeofgradientisgreatest. A geometric slope-change quantity alone isnot a physical acceleration or passenger-force criterion. Forpositionr(θ(t)),accelerationisr″(θ)θdot²+r′(θ)θddot;the time law is notgiven,andfeltforce also depends ongravity/orientation. Under the explicitly extra assumption ofconstantθdotwithradianθ,one can compute a conditional acceleration measure,but that doesnotanswer the unrestricted source wording. Retain this as informal extra-scope context,not a marked8227physical optimum.',344,'key incomplete')
p['additional_operations']={'conditional_uniform_radian_parameter_acceleration_squared':{'kind':'identity','operands':['expand_trig(diff(4*cos(x)+2*cos(3*x),x,2)**2+diff(4*sin(x)+2*sin(3*x),x,2)**2)']}}
p['additional_operation_expected']={'conditional_uniform_radian_parameter_acceleration_squared':'340+144*cos(2*x)'}
row=add('Prompt',4,123,'Given the ride path,ask where the greatest sensations would be felt. No motion-time law or physical sensation metric is provided;the prompt is outside8227assessedscope andits informal key isnot a calculative criterion.',[p],[])
row['source_interpretation']={'scope':'Retain only as informal internal source context,not an assessed8227physical problem.','missing_givens':['θas a function oftime','what quantity measures the sensation','necessary force/orientation assumptions'],'conditional_audit_only':'The stored second-parameter-derivative norm assumes a uniform radian parameter rate;it isnot a source answer or a new learner requirement.'}
new=[{'item_id':'8227:TB:Goldie:C4:Worked-illustration:1','item_kind':'worked-illustration','exercise':'Worked illustration','item_number':'1','pdf_page':122,'printed_page':108,
 'notes':answers[0]['notes'],'assessed_8227_demand_ids':[],'component_demand_ids':[TRIANGLE,COORD],'teaches_8227_demand_ids':[PARAM],'representation':'diagram',
 'source_evidence':ev(122),'evidence_role':'prerequisite/supporting teaching exposition;no directly assessed derivative coverage',
 'answer_key':{'available':True,'pdf_pages':[123],'printed_pages':[109],'locator':'Inline parametric position/projection exposition'},'learner_display':False}]
figures=[]
X='4*cos(x)+2*cos(3*x)';Y='4*sin(x)+2*sin(3*x)'
for n,page,label,note,rep,checks,method in[
 (31,122,'Figure4.10(a) aligned ride rods','InitialO,A,Parecollinear,OA=4mandAP=2m,soP=(6,0)atthechosenreferenceangle. Thephotoiscontext,notmetricdata.','diagram',
  [('Tuple(4+2,0)','Tuple(6,0)')],'Addthetwohorizontalrodlengths;thisisapositionreference,notanassumedangularspeed.'),
 (32,122,'Figure4.10(b) relative andabsolute angles','OAhasrotatedθ;APhasrotated2θrelative toOAandtherefore3θabsolutely. Themarkedθ/2θ/3θrelationshipmuststayconsistentwhenredrawing.','diagram',
  [('x+2*x','3*x')],'Distinguisharelativejointrotationfromanabsoluteaxisangle;do notuse2θastheAPaxisangle.'),
 (33,123,'Figure4.11 two-rod coordinate projections','Horizontalprojectionsare4cosθand2cos3θ;verticalprojections4sinθand2sin3θ. The4m/2mrodsandaxisdirectionsarethecommonunderlyinggivens.','diagram',
  [('(4*cos(x))**2+(4*sin(x))**2','16'),('(2*cos(3*x))**2+(2*sin(3*x))**2','4')],
  'Eachrodprojectionpairhasthecorrectfixedlength;thetwopairsaddtoP.Thepicturedisplaysoneorientation,notallpossibleprojection-signcases.'),
 (34,123,'Figure4.12 full-cycle ride path','Thepositioncurvehasouterhorizontalextremes(±6,0),self-intersections(0,±2√3),andinnerlooppoints(0,±2). Degreelabels30°,150°,210°,330°markpoints(±2√3,±4),not globalheightmaxima.','graph',
  [(f'Tuple(({X}).subs(x,0),({Y}).subs(x,0))','Tuple(6,0)'),
   (f'Tuple(({X}).subs(x,pi/3),({Y}).subs(x,pi/3),({X}).subs(x,2*pi/3),({Y}).subs(x,2*pi/3))','Tuple(0,2*sqrt(3),0,2*sqrt(3))'),
   (f'Tuple(({X}).subs(x,pi/2),({Y}).subs(x,pi/2))','Tuple(0,2)'),
   (f'(({X}).subs(x,pi-x))+({X})','0'),(f'(({Y}).subs(x,pi-x))-({Y})','0'),
   (f'(({X}).subs(x,x+pi))+({X})','0'),(f'(({Y}).subs(x,x+pi))+({Y})','0')],
  'Independentlyevaluatealllabelledspecial-anglepositionsandusex(π−θ)=−x(θ),y(π−θ)=y(θ),andhalf-turnsymmetryfortheremaininglabels. Theparameterplotprovidesgeometricposition,notthetime/force informationmissingfromPrompt4.')]:
    results=[]
    for expr,target in checks:
        got=compute({'kind':'identity','operands':[expr]});assert equivalent(got,expression(target)),(label,got)
        results.append({'operation':{'kind':'identity','operands':[expr]},'source_normalised':target,'derived':str(got)})
    figures.append({'item_id':f'8227:TB:Goldie:C4:Teaching-figure:{n}','item_kind':'teaching-figure','exercise':'Teaching figure','item_number':str(n),
     'pdf_page':page,'printed_page':page-14,'source_label':label,'notes':note,'what_it_shows':note,'assessed_8227_demand_ids':[],'component_demand_ids':[],
     'teaches_8227_demand_ids':[PARAM],'representation':rep,'source_evidence':ev(page),'parent_item_id':'8227:TB:Goldie:C4:Worked-illustration:1','learner_display':False,
     'value_level_scope_decisions':[{'rule_id':'8227:QUAL03','status':'not applicable','quoted_value':note,'reason':'Parametricposition/plottingteaching,notanassessedperiodic-equationproblem.'}],
     'value_level_scope_review_status_r5':'authorrodlengths/relativeangles/positionsread2026-11-18;independentcheckpending',
     'exam_representation_check':{'status':'finalcross-book/examinationcomparisonpending','examination_part_ids':[],'relation':'Internalprerequisiteparametricrepresentation;notderivative/exam-frequencycoverage.'},
     'mathematical_feature_review':{'status':'authorsourcerenderandexplicitprojection/coordinatechecks;independentacceptancepending','method':method,'checks':results}})
pages=[]
for page in[122,123]:
    own=[r['item_id']for r in answers if r['source_pdf_page']==page]+[r['item_id']for r in figures if r['pdf_page']==page]
    if page==122:own+=[f'8227:TB:Goldie:C4:Exercise-4D:{n}'for n in[11,12]]
    pages.append({'pdf_page':page,'printed_page':page-14,'chapter':4,'page_status':'items enumerated','item_ids':own,
     'continuation_item_ids':['8227:TB:Goldie:C4:Worked-illustration:1']if page==123 else[],
     'source_evidence':ev(page),'non_item_content':'All4D11–12on122,headinglessparametricrideexposition,twoFigure4.10panels,projection/pathfiguresandPrompt4enumerated. Thephotographandrhetoricalintroductionbelongtothecontext,notextracalculativeproblems.',
     'reader':'Codex author','date':'2026-11-18'})
if __name__=='__main__':
    for name,data in[
     ('answers-Goldie-C4-param-opening.json',{'scope':'Rod/projection/degree-sampleteachingandtheexplicitextra-scopephysicalprompt,PDF122–123.','items':answers}),
     ('census-Goldie-C4-param-opening.json',{'book':'Goldie','book_id':'8227-SRC-015','chapter':4,'source_path':SRC,'source_sha256':SHA,
      'scope':'Complete122–123including4D11–12andallparametricopeningrepresentations.','new_items':new+figures,
      'corrections':[{'item_id':'8227:TB:Goldie:C4:Worked-illustration:1','continuation_pdf_pages':[123]}],'pages':pages})]:
        (W/'tools/textbook-r5'/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
    print(len(answers),'items;',sum(len(r['subparts'])for r in answers),'outputs;',len(figures),'figures')
