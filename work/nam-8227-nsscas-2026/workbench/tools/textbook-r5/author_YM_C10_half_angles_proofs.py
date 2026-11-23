"""YM464–465: original half-angle branches,parameter radicals and formal identity domains."""
import json
import author_YM_C10_opening as o
import author_YM_C10_compound_sine as s
import author_YM_C9_opening as g
from author_YM_C9_opening import h,W,SRC,SHA,pp,v,fig,figures,extra,compute,expression,equivalent
from author_YM_C4_trig_graphs import reasoning
g.answers.clear();g.new.clear();g.corrections.clear();figures.clear()
answers=g.answers;new=g.new;corrections=g.corrections;ev=o.ev;h.common.base.ev=ev
DOUBLE='8227:2020:M2:T3:O02:D03';COMP=o.COMPOUND;EVAL=o.EXACT;PYTH='8227:2020:M1:T6:O05:D01'
def value(label,expr,key,kp,constraints,domain=None):
 p=v(label,expr,key,kp,'Derive the missing ORIGINAL ratio and its sign from the specified obtuse/quadrant bounds. Apply the actually requested double/repeateddouble/half-angle identity. For a half-angle square root choose its sign from the original halved interval;do not output±merely because algebra produced a square.')
 p.update(assessed_8227_demand_ids=[DOUBLE,EVAL],component_demand_ids=[PYTH],response_format='symbolic',original_constraints=constraints)
 if domain:p['parameter_domain']=domain
 return p

def add(kind,n,page,note,parts):
 r=o.add(kind,n,page,note,parts);r.update(mapping_rationale='The source asks exact doubled/repeated/half-angle values,parameter expressions or analytic proofs. Branch selection follows ORIGINAL quadrants. Parameterradicalsneedtheactualacute-angle0<parameter<1domain. These expressions are not automatically higher-multiplier root-solving tasks.',value_level_scope_decisions=[dict(rule_id='8227:QUAL03',status='not applicable',quoted_value=note,reason='Theseareexactratios/parameterexpressions/identities,notboundedtrigonometric equationrootsets. The3x/4xproofargumentsdonotcreaterequiredhigher-multiplierperiodicsolutions.')],scope_check=dict(status='in-scope',basis=note,excluded_or_qualified_parts=[],limits_considered=['8227:QUAL03']),precision_angle_check=dict(source='Alloutputs exact. Originalobtuse/90..270constraintsdegrees;Q3originalintervalusesradiansπ/2..3π/2.',comparison='Keep correct halved-quadrant signs and realradicaldomain. Identityproofsretain original numerator/denominatorconditions;anintermediateformula withadditionalpolesmustnotdeletevalidcases.'))
 return r
ca='(-Rational(4,5))';sa='sqrt(1-Rational(4,5)**2)';c2=f'(2*({ca})**2-1)';s2=f'(2*({sa})*({ca}))'
constraints='OriginalcosA=−4/5andAobtuse,soAIIandA/2I;sinApositive.'
ps=[value('a-cos2A',c2,'Rational(7,25)',643,constraints),value('b-tan2A',s2+'/'+c2,'-Rational(24,7)',643,constraints),value('c-sin-halfA',f'sqrt((1-({ca}))/2)','sqrt(Rational(9,10))',643,constraints),value('d-cos4A','2*'+c2+'**2-1','-Rational(527,625)',643,constraints)]
ps[-1]['source_reading_resolution']='Nativekeyprints−527/625,matchingtheoriginal. Thumbnail−627suspicionCLEARED.'
add('Try-Now-13',1,464,'OriginalcosA−4/5andAobtuse:cos2A7/25,tan2A−24/7,positivesin(A/2)√(9/10),cos4A−527/625. Nativefinalkeycorrect.',ps)
sb='Rational(3,5)';cb='(-sqrt(1-Rational(3,5)**2))';s2=f'(2*({sb})*({cb}))';c2=f'(1-2*({sb})**2)';constraints='OriginalsinB=3/5andBobtuse,soBII,cosBnegative,B/2I.'
ps=[value('a-sin2B',s2,'-Rational(24,25)',643,constraints),value('b-sin4B','2*'+s2+'*'+c2,'-Rational(336,625)',643,constraints),value('c-tan-halfB',f'({sb})/(1+({cb}))','3',643,constraints)]
add('Try-Now-13',2,464,'OriginalsinB3/5andBobtuse:derivecosB−4/5,thennegative sin2B/sin4Bandpositivehalf-angletangent3.',ps)
t='-2';constraints='Originaltanx=−2andπ/2<x<3π/2forcesxII;thisisaRADIANquadrantconstraint.';c2=f'((1-({t})**2)/(1+({t})**2))';s2=f'(2*({t})/(1+({t})**2))'
ps=[value('a-cos2x',c2,'-Rational(3,5)',643,constraints),value('b-tan2x',f'2*({t})/(1-({t})**2)','Rational(4,3)',643,constraints),value('c-sin4x','2*'+s2+'*'+c2,'Rational(24,25)',643,constraints)]
add('Try-Now-13',3,464,'Originaltanx−2withradianxII:exactcos2x−3/5,tan2x4/3,sin4x24/25. Retain original quadrant rather than assuming tannegative means onlyIV.',ps)
constraints='OriginaltanA8/15,sinB−4/5,andboth90°<angle<270°. Positive tanforcesAIII;negative sinforcesBIII;B/2IIanditscosineNEGATIVE.'
sa='(-Rational(8,15)/sqrt(1+Rational(8,15)**2))';ca='(-1/sqrt(1+Rational(8,15)**2))';sb='(-Rational(4,5))';cb='(-sqrt(1-Rational(4,5)**2))'
p=value('a-sin-sum',f'({sa})*({cb})+({ca})*({sb})','Rational(84,85)',643,constraints);p['assessed_8227_demand_ids']=[COMP,EVAL]
q=value('b-cos-halfB',f'FiniteSet(-sqrt((1+({cb}))/2))','FiniteSet(-sqrt(Rational(1,5)),sqrt(Rational(1,5)))',643,constraints);q.update(author_expected_normalised='FiniteSet(-sqrt(Rational(1,5)))',printed_key_display='±√(1/5)',correct_answer='−√(1/5)only;B/2isquadrantII.')
add('Try-Now-13',4,464,'OriginalAIII/BIIIratiosgivesin(A+B)84/85;B/2isII,socos(B/2)mustbe−√(1/5). Printed±retainsaninvalidpositivebranch.',[p,q])
constraints='Originalsinθ=pandθacute,so0<p<1,cosθ=+√(1−p²),θ/2acute.'
ps=[value('a-sin2theta','2*p*sqrt(1-p**2)','2*p*sqrt(1-p**2)',464,constraints,'0<p<1'),value('b-cos-squared-half-theta','(1+sqrt(1-p**2))/2','(sqrt(1-p**2)+1)/2',464,constraints,'0<p<1')]
# Independently derive the requested forms through the ORIGINAL defining ratio/acute branch.
ps[0]['operation']={'kind':'identity','operands':['(2*sin(x)*cos(x)).subs({sin(x):p,cos(x):sqrt(1-p**2)})']};ps[1]['operation']={'kind':'identity','operands':['solve(2*y-1-sqrt(1-p**2),y)[0]']}
add('Example',14,464,'Fororiginalsinθ=pandacuteθ,expresssin2θandcos²(θ/2)intermsofp. Do not take an unnecessary square root of the explicitly SQUARED half-angle output;parameter0<p<1.',ps)
constraints='Originalcosθ=aandθacute,so0<a<1,sinθ=+√(1−a²)andθ/2I.'
ps=[value('a-sin4theta','(2*sin(2*x)*cos(2*x)).subs({sin(2*x):2*a*sqrt(1-a**2),cos(2*x):2*a**2-1})','4*a*sqrt(1-a**2)*(2*a**2-1)',643,constraints,'0<a<1'),value('b-sin-half-theta','sqrt(solve(1-2*y-a,y)[0])','sqrt((1-a)/2)',643,constraints,'0<a<1')]
ps[1]['source_reading_resolution']='Nativekeyradicalcovers theWHOLEfraction(1−a)/2. The thumbnail reading√(1−a)/2wasCLEARED;keyiscorrect.'
add('Try-Now',14,465,'Originalcosθ=aacute:sin4θ=4a√(1−a²)(2a²−1);sin(θ/2)=√((1−a)/2),withthewholefractionundertheradical. Parameter0<a<1.',ps)
p=s.proof('triple-tangent','tan(3*x)','(3*tan(x)-tan(x)**3)/(1-3*tan(x)**2)',465,'cosx≠0andcos3x≠0;the finaldisplayedRHSdenominatorisnonzero.','A domain-complete proof expandssin3x/cos3xanddividesbynonzerocos³x. Source insteadintroducestan2x,whosepolesareextra. Atxπ/4thefinalidentityisvalidwithvalue−1buttheintermediatetan2xisundefined;do not lose this case by the selected proof route.')
extra(p,'valid-original-point-lost-by-tan2-route','Tuple(tan(3*pi/4),((3*tan(x)-tan(x)**3)/(1-3*tan(x)**2)).subs(x,pi/4))','Tuple(-1,-1)')
add('Example',15,465,'Prove the original triple-tangentidentityonitscommon domain. Sourceexpansionthroughtan2xhasavoidableextrapoles;directsin3/cos3routepreservesthefinaldomain.',[p])
proofs=[('a','sin(3*x)','3*sin(x)-4*sin(x)**3','Allrealx.','Expandsin(2x+x),applyoriginaldouble-angleidentities,andcollectpowersofsinx.'),('b','cos(2*x)/sin(2*x)','((cos(x)/sin(x))**2-1)/(2*cos(x)/sin(x))','sinx≠0andcosx≠0,equivalentlysin2x≠0.','Expandoriginalcot2xascos2x/sin2x,thenexpresswithcotxwhilekeepingnonzerodenominators.'),('c','(sin(x)+sin(2*x))/(1+cos(x)+cos(2*x))','tan(x)','cosx≠0and1+2cosx≠0;theoriginaldenominatorfactorscosx(1+2cosx).','Expanddoubleangles,factor sinx(1+2cosx)overcosx(1+2cosx),andcancelonlytheoriginalnonzerofactor. Do notaddtheundefined0/0points cosx−1/2.'),('d','4*sin(x)*cos(x)*(cos(x)**2-sin(x)**2)','sin(4*x)','AllrealA.','Recognise2sinAcosAandsquare-differenceas sin2A/cos2A,thenapplydoubleangleasecondtime.'),('e','(cos(2*x)+9*cos(x)+5)/(cos(x)+4)','2*cos(x)+1','Allrealx;cosx+4≥3neverzero.','Replacecos2xby2cos²x−1,factor(2cosx+1)(cosx+4),andcancelthenonzerofactor.'),('f','1/sin(2*x)+cos(2*x)/sin(2*x)','cos(x)/sin(x)','sin2x≠0;equivalentlysinxandcosxnonzero.','Combineoriginalreciprocals,expand1+cos2x=2cos²xandsin2x=2sinxcosx,thencancelnonzerocosx. Do notextendtheleftsideoveritsoriginalpoles.')]
ps=[s.proof(label,lhs,rhs,644,domain,method)for label,lhs,rhs,domain,method in proofs]
for p in ps:p['assessed_8227_demand_ids']=[DOUBLE,EVAL]+([COMP]if p['subpart']=='a'else[])
add('Try-Now',15,465,'Six originaldouble-/triple-angleidentitiesinclude quotientcancellationwithremoved-domainpointsandall-real polynomialtrigidentities. Eachactualcommondomainandvisiblealgebraicrouteisrecorded.',ps)
refs=[(70,464,'Example14 SOLUTION acute-parameter triangle','Unitradius,sinθ=p,verticalp,positivehorizontal√(1−p²);sourceacuteθimplies0<p<1.',DOUBLE,'diagram','Example:14'),(71,464,'Example14 doubled-sine parameter working','2sinθcosθ=2p√(1−p²);positivecosinebranchcomesfromacuteθ.',DOUBLE,'table','Example:14'),(72,464,'Example14 squared-half-angle parameter working','cosθ=2cos²(θ/2)−1;solvetheactualSQUAREDoutputas(1+√(1−p²))/2.',DOUBLE,'table','Example:14'),(73,465,'Example15 source tan2x triple-angle proof route','tan3x=tan(2x+x)introducesunnecessarytan2xpoles. Finalcommon-domainidentitycaninsteadbederiveddirectlyfromsin3/cos3.',DOUBLE,'table','Example:15')]
for n,page,label,note,d,rep,parent in refs:
 fig(n,page,label,note,[d],rep,[],parent);figures[-1].update(item_id=f'8227:TB:YM:C10:Teaching-figure:{n}',printed_page=pp(page),source_evidence=ev(page),value_level_scope_decisions=[],item_kind='teaching-figure',parent_item_id='8227:TB:YM:C10:'+parent);figures[-1]['mathematical_feature_review']['method']='Readactualacute/obtusequadrants,half-anglepowers,radicalbarsandnativekeys. Derivebranchsignsfromtheoriginalintervalandretainallidentitydenominatorconditions.'
pages=[dict(pdf_page=page,printed_page=pp(page),chapter=10,page_status='items enumerated',item_ids=[r['item_id']for r in answers if r['source_pdf_page']==page]+[r['item_id']for r in figures if r['pdf_page']==page],continuation_item_ids=[],source_evidence=ev(page),reader='Codex author',date='2026-11-20',non_item_content='AllTry13Q1–4,Example14/Try14,Example15/Try15andfouractualsolutionpanelsenumerated. Clearedthumbnailradical/numeratorfalseleadsnotregisteredasdefects.',scope_screen='Original0<p/a<1andhalvedquadrantsspecified;proofargumentmultipliersnotmisclassifiedasbounded-equationlimits.')for page in[464,465]]
def save():
 for name,data in [('answers-YM-C10-half-angles-proofs.json',dict(scope='Complete464–465exacthalf-anglebranches,parameterradicalsandidentitydomains.',items=answers)),('census-YM-C10-half-angles-proofs.json',dict(book='YM',book_id='8227-SRC-017',chapter=10,source_path=SRC,source_sha256=SHA,scope='Complete464–465page/item/figurecensus.',new_items=new+figures,corrections=corrections,pages=pages))]:
  (W/'tools/textbook-r5'/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
 for row in answers:
  for p in row['subparts']:
   if'operation'in p:assert equivalent(compute(p['operation']),expression(p.get('author_expected_normalised',p['printed_key_normalised']))),(row['item_id'],p['subpart'])
   for name,op in p.get('additional_operations',{}).items():assert equivalent(compute(op),expression(p['additional_operation_expected'][name])),(row['item_id'],p['subpart'],name)
 print(len(answers),'items;',sum(len(r['subparts'])for r in answers),'responses;',len(figures),'references;',len(pages),'pages')
if __name__=='__main__':save()
