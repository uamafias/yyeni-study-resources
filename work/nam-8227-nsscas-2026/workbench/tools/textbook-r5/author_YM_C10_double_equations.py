"""YM466–467: original reciprocal equations,preserved cotangent zero and R-form conditions."""
import json
from author_YM_C4_composite_equations import roots
import author_YM_C10_opening as o
import author_YM_C10_compound_sine as s
import author_YM_C9_opening as g
from author_YM_C9_opening import h,W,SRC,SHA,pp,v,fig,figures,extra,compute,expression,equivalent
from author_YM_C4_trig_graphs import reasoning
g.answers.clear();g.new.clear();g.corrections.clear();figures.clear()
answers=g.answers;new=g.new;corrections=g.corrections;ev=o.ev;h.common.base.ev=ev
DOUBLE='8227:2020:M2:T3:O02:D03';EVAL=o.EXACT;RECIP=o.RECIP;BND='8227:2020:M1:T6:O06:D01';ALL='8227:2020:M1:T6:O06:D02';RFORM='8227:2020:M2:T3:O02:D04';D='(x*pi/180)'
def bounded(label,expr,key,kp,branches,unit='degree',hi=None,opened=False):
 p=roots(label,expr,key,kp,branches,unit=unit,hi=hi,approx=isinstance(key,list),opened=opened);p.update(assessed_8227_demand_ids=[DOUBLE,EVAL,RECIP,BND,ALL],response_format='numeric',original_equation_zero_form=expr,method='Derive from the ORIGINAL reciprocal/double-angle equation. Factor before dividing so a valid zero factor is retained. Solve every ratio branch in the actual finite degree/radian interval,exclude only ORIGINAL poles,andsubstituteeachcandidatebackbeforecomparingprintedvalues.')
 return p

def add(kind,n,page,note,parts,new_item=False):
 r=o.add(kind,n,page,note,parts,new_item);r.update(mapping_rationale='Double-angle/reciprocal transformation and complete original-domain root recovery are assessed. A valid cotangent zero at90degrees must survive even though1/tan is undefined there. Hence links preserve earlier identity and original domain;clearing/cancellation never admits extra poles.',value_level_scope_decisions=[dict(rule_id='8227:QUAL03',status='within',quoted_value=note,reason='Originalequationargumentshavemultiplier1or2. Cubesofcosinearepowersoftheratio,nottripledanglearguments.'),dict(rule_id='8227:LIMIT02',status='within',quoted_value=note,reason='Originalfiniteintervalskept;no generalperiodicfamilyrequested.')],scope_check=dict(status='in-scope',basis=note,excluded_or_qualified_parts=[],limits_considered=['8227:QUAL03','8227:LIMIT02']),precision_angle_check=dict(source='Example16/Try16useexplicitdegreeintervals;Example17/Try17useradians.Example17andTry17Q2request3sf.',comparison='Keepfullinternalrootsandcompletebranchsetsbeforewritten1dpdegree/3sfradiancomparison. Originalzero/polechecksusetheactualfunction,notanover-restrictedreciprocalalias.'))
 return r
p=bounded('roots',f'3*sin(2*{D})*tan({D})-2',['35.3','144.7'],466,[('sin','x','1/3',2)],hi='180',opened=True)
p['assessed_8227_demand_ids']=[DOUBLE,EVAL,BND,ALL];p['component_demand_ids']=['8227:2020:M1:T6:O05:D01']
add('Example',16,466,'Solve original3sin2θtanθ=2onSTRICT0<θ<180degrees. Transformation6sin²θ2retainsoriginalcosθ≠0;two roots35.3,144.7.',[p])
p=bounded('roots',f'2*cos(2*{D})-4*cos({D})+3','FiniteSet(60)',644,[('cos','x','1/2',1)],hi='180');p['assessed_8227_demand_ids']=[DOUBLE,EVAL,BND,ALL]
add('Try-Now-16',1,466,'Original2cos2θ=4cosθ−3onCLOSED0..180degreesreduces to repeatedcosinevalue1/2;only60degrees.',[p])
p=bounded('roots',f'5*tan(2*{D})-4*cot({D})',['28.1','151.9'],644,[('cos','x','0',1),('tan','x','2/7',2)],hi='180',opened=True)
p.update(difference_disposition='key incomplete',difference_reason='The printed key omits θ90degrees. In the ORIGINAL equation,tan180=0andcot90=0arebothdefined,so90isvalid. Algebraicfactoringretainscosθ0;dividingitawaywouldlosethisroot. Other printed28.1/151.9valuesarevalid.')
extra(p,'original-omitted-axis-root','5*tan(2*pi/2)-4*cos(pi/2)/sin(pi/2)','0')
add('Try-Now-16',2,466,'Solve original5tan2θ=4cotθonSTRICT0..180degrees. Correctroots28.1,90,151.9;keylosesthevalid90degreecotangentzero. Originalpoles45/135andendpointsremainexcluded.',[p])
p=bounded('roots',f'5*cos({D})*(1+cos(2*{D}))-4',['42.5','317.5'],644,[('cos','x','(2/5)**(1/3)',1)]);p['assessed_8227_demand_ids']=[DOUBLE,EVAL,BND,ALL]
add('Try-Now-16',3,466,'Original5cosθ(1+cos2θ)=4onCLOSED0..360degreesbecomes10cos³θ4,thenretainsbothangleswithpositivecosine. No reciprocalpoles.',[p])
p=s.proof('a-identity','2*(1/sin(2*x))*tan(x)','sec(x)**2',466,'sin2θ≠0andcosθ≠0;equivalentlysinθandcosθnonzero.','Expand the ORIGINAL doubleanglesine andtan=sin/cos,cancelonlynonzerosinθ,thenreachsec²θ. RHSaloneisdefinedatadditionalθvalues;theidentitydoesnotextendtheoriginalLHSthere.')
p['assessed_8227_demand_ids']=[DOUBLE,EVAL,RECIP]
q=bounded('b-roots','2*(1/sin(2*x))*tan(x)-5',['1.11','2.03'],466,[('cos','x','1/5',2)],unit='radian',hi='pi',opened=True);q['depends_on_source_parts']=['a-identity']
add('Example',17,466,'Prove original2cosec2θtanθ=sec²θ,thenHENCEsolveits5-equationonSTRICT0<θ<πradians. Both1.11,2.03areoriginal-domainvalid.',[p,q])
p=s.proof('a-identity','cos(2*x)/(1+cos(2*x))','1-sec(x)**2/2',644,'cosx≠0because1+cos2x=2cos²x.','Use the ORIGINAL doubleangleforms in numeratoranddenominator;rewritewithoutaddingthecosx0poles.');p['assessed_8227_demand_ids']=[DOUBLE,EVAL,RECIP]
q=bounded('b-roots','cos(2*x)/(1+cos(2*x))-13-5*tan(x)',['1.77'],644,[('tan','x','-5',1)],unit='radian',hi='pi');q['depends_on_source_parts']=['a-identity']
add('Try-Now-17',1,467,'Prove originalcos2x/(1+cos2x)=1−sec²x/2,thenuseittosolvetheoriginal13+5tanxequationonCLOSED0..πradians. Originalπ/2poleexcluded;uniqueroot1.77.',[p,q])
p=s.proof('a-identity','2*(1/sin(2*x))**2*(1-cos(2*x))','sec(x)**2',644,'sin2x≠0;bothsinxandcosxnonzero.','Use ORIGINAL1−cos2x=2sin²xandsin2x=2sinxcosx;cancelnonzerosin²xandreachsec²x. OriginalLHSremainsundefinedatadditionalpointswhereRHSisfinite.');p['assessed_8227_demand_ids']=[DOUBLE,EVAL,RECIP]
q=bounded('b-roots','2*(1/sin(2*x))**2*(1-cos(2*x))-tan(x)-21',['1.37','1.82'],644,[('tan','x','5',1),('tan','x','-4',1)],unit='radian',hi='pi',opened=True);q['depends_on_source_parts']=['a-identity']
add('Try-Now-17',2,467,'Prove original2cosec²2x(1−cos2x)=sec²x,thenHENCEsolveits tanx+21equationonSTRICT0..πradians,to3sf. Positive5/negative−4tangentbranchesbothkept.',[p,q])
ps=[]
for label,result,derivation in [('coefficient-pair','a=Rcosα,b=Rsinα.','Expand ORIGINALRsin(θ+α),equateitsindependentsinθ/cosθcoefficientswitha,b.'),('amplitude','R=√(a²+b²),withR>0onlyif(a,b)≠(0,0).','Square/addthetwoactualcoefficientrelations;sin²α+cos²α1givesR²=a²+b². SourcechoosespositiveR.'),('acute-phase','tanα=b/a,withacuteαonlywhena>0,b>0forTHISRsin(θ+α)form.','The source introductoryparagraphallowsreala,b,butitstableassumesRpositiveandαacute. Thoseconditionsforcebothcoefficientspositive. Forarbitraryrealsuseappropriatephase/quadrantoradifferent±form;zeroa/bneedseparateboundaryhandling. Do notdividebya0orclaimpositiveRforthezeropair.')]:
 p=reasoning(label,result,derivation,467,'matches');p.update(assessed_8227_demand_ids=[],teaches_8227_demand_ids=[RFORM],response_format='explanation',source_parameter_conditions='SourcechosenR>0andacuteα:conditionala>0,b>0. Generalrealcoefficientsneedextensions.');ps.append(p)
extra(ps[0],'original-expanded-coefficient-identity','trigsimp(expand_trig(k*sin(x+y))-(k*cos(y)*sin(x)+k*sin(y)*cos(x)))','0');extra(ps[1],'original-coefficient-square-sum','trigsimp((k*cos(y))**2+(k*sin(y))**2)','k**2')
r=add('Worked-derivation',2,467,'RecoveredR-formtable:a sinθ+b cosθ=Rsin(θ+α),coefficientpair,amplitudeandphase. Itsacuteα/Rpositiveassumptionisconditionalonpositivea,b,despitegeneralreal-coefficientprose.',ps,True);r.update(evidence_role='prerequisite/supporting worked R-form teaching derivation;not a separately asked exam proof.',teaches_8227_demand_ids=[RFORM],value_level_scope_decisions=[],scope_check=dict(status='in-scope',basis='ConditionalR-formcoefficient/amplitude/phaseexposition.',excluded_or_qualified_parts=[],limits_considered=[]));new[-1]['teaches_8227_demand_ids']=[RFORM]
refs=[(74,466,'Example16 double-angle equation working','6sin²θ=2followsontheoriginaltanθdomain;cosθ0isnotadded.',DOUBLE,'table','Example:16'),(75,466,'Example16 sine-quadrant solution diagram','Originalopen0..180degreescontainspositive-sinequadrantsI/II;both35.3,144.7shown.',ALL,'diagram','Example:16'),(76,466,'Example17 reciprocal identity working','Cancellationofsinθrequiresnonzerooriginalsin2θ;identitydoesnotextendLHSoveritspoles.',DOUBLE,'table','Example:17'),(77,466,'Example17 original first/second quadrant diagram','cos²θ1/5givesbothsignsinsideopen0..π;roundonceatendto3sf.',ALL,'diagram','Example:17'),(78,467,'R-form coefficient comparison','Rsin(θ+α)=Rcosαsinθ+Rsinαcosθ;matcha,bwithcorrectcoefficientroles.',RFORM,'table','Worked-derivation:2'),(79,467,'R-form amplitude derivation','Square/addgivesR²=a²+b²;positiveRrequiresnonzeropair.',RFORM,'table','Worked-derivation:2'),(80,467,'R-form acute-phase derivation and conditions','tanα=b/aassumesnonzeroa;acuteα/Rpositiveforthisplus-formrequiresa,bpositive. Generalrealsneedquadrant/zeroboundaries.',RFORM,'table','Worked-derivation:2')]
for n,page,label,note,d,rep,parent in refs:
 fig(n,page,label,note,[d],rep,[],parent);figures[-1].update(item_id=f'8227:TB:YM:C10:Teaching-figure:{n}',printed_page=pp(page),source_evidence=ev(page),value_level_scope_decisions=[],item_kind='teaching-figure',parent_item_id='8227:TB:YM:C10:'+parent);figures[-1]['mathematical_feature_review']['method']='Readoriginalreciprocalfunctionsandintervals;factorbeforedivisionandcheck90degreecotzero. ReadactualR-formreal-coefficientprosevsacute-phaseconditions;donotextendthechosenbranchsilently.'
pages=[dict(pdf_page=page,printed_page=pp(page),chapter=10,page_status='items enumerated',item_ids=[r['item_id']for r in answers if r['source_pdf_page']==page]+[r['item_id']for r in figures if r['pdf_page']==page],continuation_item_ids=[],source_evidence=ev(page),reader='Codex author',date='2026-11-20',non_item_content='AllExample16/Try16Q1–3,Example17/Try17Q1–2,theworkedR-formderivationandsevenactualpanelsenumerated. Omitted90degreekeyrootandacutephaseconditionsrecorded.',scope_screen='Originalboundedpolesandzero-brancheskept. R-formexpositionretainsconditionsratherthanclaimingallrealcoefficientsfitanacuteplus-phase.')for page in[466,467]]
def save():
 for name,data in [('answers-YM-C10-double-equations.json',dict(scope='Complete466–467originaldouble-angleequationsandconditionalR-formderivation.',items=answers)),('census-YM-C10-double-equations.json',dict(book='YM',book_id='8227-SRC-017',chapter=10,source_path=SRC,source_sha256=SHA,scope='Complete466–467page/item/figurecensus.',new_items=new+figures,corrections=corrections,pages=pages))]:
  (W/'tools/textbook-r5'/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
 for row in answers:
  for p in row['subparts']:
   if'operation'in p and'printed_key_normalised'in p:assert equivalent(compute(p['operation']),expression(p['printed_key_normalised'])),(row['item_id'],p['subpart'])
   for name,op in p.get('additional_operations',{}).items():assert equivalent(compute(op),expression(p['additional_operation_expected'][name])),(row['item_id'],p['subpart'],name)
 print(len(answers),'items;',sum(len(r['subparts'])for r in answers),'responses;',len(figures),'references;',len(pages),'pages')
if __name__=='__main__':save()
