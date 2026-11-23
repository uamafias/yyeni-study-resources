"""YM532–533: reconstructing curves and the specific given shaded regions."""
import json
import author_YM_C12_opening as a
from author_YM_C12_opening import h,W,SRC,SHA,pp,ev,v,reasoning,fig,figures,extra,compute,expression,equivalent
h.answers.clear();h.new.clear();h.corrections.clear();figures.clear()
answers=h.answers;new=h.new;corrections=h.corrections
EXP=a.EXP;DEF=a.DEF;LOG=a.LOG;CONST='8227:2020:M1:T9:O02:D01';CURVE='8227:2020:M1:T9:O02:D02';AREA='8227:2020:M1:T9:O04:D01'
def val(label,expr,key,kp,direct,method,comp=None):
 p=a.val(label,expr,key,kp,method,direct);p['component_demand_ids']=comp or[];return p

def add(kind,n,page,note,parts,rep='text'):
 r=a.add(kind,n,page,note,parts);r.update(representation=rep,mapping_rationale='A requested reconstructed curve assesses both fixing integration constants and recovering the curve. Shaded-area tasks directly assess the specific represented region;definite integration/exponential primitives are components unless independently asked. A required equation and its rearranged form retain positive-parameter/logarithm/square-root constraints. No implicit/parametric differentiation is involved.');return r

def recovered(kind,n,second,first,point,curve,kp,note):
 expr='integrate('+first+',x)'+('-1'if n==2 and kind!='Example'else'+1'if n==1 and kind!='Example'else'-2'if n==3 else'+1')
 # Independently verified constants from source initial conditions are substituted;
 # original derivative and point constraints are checked separately below.
 p=val('curve',expr,curve,kp,[CONST,CURVE],'Integrate the ORIGINAL given derivative;for a second derivative integrate TWICE. Determine each constant from its own ORIGINAL gradient/point condition. Verify the final curve against the original derivative order and all initial data.',[EXP])
 extra(p,'original-derivative','diff('+curve+',x'+(',2'if second else'')+')',second or first)
 extra(p,'original-point','('+curve+').subs(x,'+point[0]+')',point[1])
 if second:extra(p,'original-gradient-at-zero','diff('+curve+',x).subs(x,0)','1'if kind=='Example'else'-8')
 return add(kind,n,532,note,[p])
recovered('Example',4,'2*exp(-x)','-2*exp(-x)+3',('1','2/exp(1)+4'),'2*exp(-x)+3*x+1',532,'GivenSECONDderivative2e^(−x),gradient1at0,andpoint(1,2/e+4):recovercurve2e^(−x)+3x+1. Bothconstantsarefixedfromdifferentconditions.')
recovered('Try-Now-4',1,None,'6*exp(2*x)+2*exp(-x)',('0','2'),'3*exp(2*x)-2*exp(-x)+1',650,'GivenFIRSTderivative6e^(2x)+2e^(−x)andpoint(0,2):recover3e^(2x)−2e^(−x)+1.')
# This first primitive has value5/2at0;the originalpointy1fixesconstant−3/2.
p=val('curve','integrate(exp(2*x)-2*exp(-x),x)-Rational(3,2)','exp(2*x)/2+2*exp(-x)-Rational(3,2)',650,[CONST,CURVE],'Integrate ORIGINAL e^(2x)−2e^(−x),then use y(0)=1tofixC−3/2. Differentiate recoveredcurveandchecktheoriginalpoint.',[EXP]);extra(p,'original-derivative','diff(exp(2*x)/2+2*exp(-x)-Rational(3,2),x)','exp(2*x)-2*exp(-x)');extra(p,'original-point','(exp(2*x)/2+2*exp(-x)-Rational(3,2)).subs(x,0)','1')
add('Try-Now-4',2,532,'Originalfirstderivativee^(2x)−2e^(−x),point(0,1):recovere^(2x)/2+2e^(−x)−3/2. Negativeouterderivativecoefficientdoesnotgiveanegativeprimitivecoefficient.',[p])
recovered('Try-Now-4',3,'20*exp(-2*x)','-10*exp(-2*x)+2',('1','5/exp(2)'),'5*exp(-2*x)+2*x-2',650,'GivenSECONDderivative20e^(−2x),gradient−8at0,andpoint(1,5/e²):recover5e^(−2x)+2x−2.')
p=val('a-area','integrate(exp(2*x),(x,0,p))','(exp(2*p)-1)/2',533,[AREA],'Read ORIGINALGIVENgraph:curvee^(2x),lowerboundaryy0,leftx0,rightxp>0. Positivecurvegivesarea(e^(2p)−1)/2.',[EXP,DEF]);p.update(given_representation='graph',original_integrand='exp(2*x)',shaded_interval=['0','p'],original_parameter_domain='p>0asshownbythegivenregion',units='units^2',printed_key_units='units^2')
q=val('b-p','log(11)/2','Rational(6,5)',533,[AREA,LOG],'SettheORIGINALareaexpressionequal5: e^(2p)=11,sop=ln11/2. Roundonlyfinalp2sf1.2,keepingp>0. Area5isnotthecurveordinate.',[EXP,DEF]);q.update(operation=dict(kind='rounded',operands=['log(11)/2'],significant_figures=2),requested_precision='2 significant figures',given_representation='graph',depends_on_source_parts=['a-area']);extra(q,'original-area-equation','((exp(2*p)-1)/2).subs(p,log(11)/2)','5')
add('Example',5,533,'GIVENgraphy=e^(2x),shadedregionbetweenx0,xp,y0:(a)area(p);(b)HENCEfindpforarea5,to2sf1.2.',[p,q],'graph')
p=val('equation','integrate(8*x+exp(x)/2,(x,0,a))-Rational(1,2)','4*a**2+exp(a)/2-1',533,[AREA],'OriginalGIVENregionunder8x+e^x/2from0topositivea. Actualarea4a²+(e^a−1)/2equals1/2;equation8a²+e^a−2=0. Bothpositiveaandoriginalshadeboundariesretained.',[EXP,DEF]);p.update(given_representation='graph',original_integrand='8*x+exp(x)/2',shaded_interval=['0','a'],equation_zero_form=True)
q=reasoning('shown-rearrangement','a=sqrt((2−e^a)/8).','Fromoriginalareaequation8a²=2−e^a. Sourcea>0selectsthePOSITIVEsquare-rootbranch. Theequationforces2−e^a>0andhence0<a<ln2. Squaringwithoutthatbranchrestrictionwouldintroduceextraneousnegativea.',533,'show/prove');q.update(assessed_8227_demand_ids=[AREA],component_demand_ids=[EXP,DEF],given_representation='graph',response_format='proof/show-that',depends_on_source_parts=['equation']);extra(q,'same-zero-form','2*(4*a**2+exp(a)/2-1)-(8*a**2+exp(a)-2)','0')
add('Try-Now-5',1,533,'GIVENgraph8x+e^x/2andpositivea,shadedarea1/2:findareaequation,thenSHOWpositive-rootrearrangementa=√[(2−e^a)/8].',[p,q],'graph')
p=val('a-area','integrate(1-exp(-x),(x,0,p))','p+exp(-p)-1',533,[AREA],'OriginalGIVENshadeisBETWEENuppery1andlowere^(−x),fromtheirintersectionx0torightxp>0. Integratetopminusbottom1−e^(−x),notjustthecurve.',[EXP,DEF]);p.update(given_representation='graph',original_integrand='1-exp(-x)',shaded_interval=['0','p'],units='units^2',original_parameter_domain='p>0fromactualgivendiagram')
q=reasoning('b-shown-relation','p=2−e^(−p).','Settheindependentlyderivedoriginalarea p+e^(−p)−1equal1andretainpositivep. Rearranginggives p=2−e^(−p);noextra numericalsolveasked.',533,'show/prove');q.update(assessed_8227_demand_ids=[AREA],component_demand_ids=[EXP,DEF],given_representation='graph',response_format='proof/show-that',depends_on_source_parts=['a-area']);extra(q,'same-original-area-equation','(p+exp(-p)-2)-(p-(2-exp(-p)))','0')
add('Try-Now-5',2,533,'GIVENe^(−x),y1,xpboundshadeabovecurve:(a)areap+e^(−p)−1;(b)SHOWarea1impliesp2−e^(−p).',[p,q],'graph')
refs=[(9,532,'Example4 first recovery and gradient condition','Originalsecond2e^−xintegratesto−2e^−x+C1;gradient1at0fixesC1=3.',CONST,'Example:4',False),(10,532,'Example4 second recovery and point condition','Integrateagainandusepoint(1,2/e+4)tofixC2=1.',CURVE,'Example:4',False),(11,533,'Example5 GIVEN exponential shaded region','Axes,positiveincreasinge^(2x),rightboundaryp,andshadebetween0andpabovey0. pvaries;curveandbounddefinitionsmustremainconsistent.',AREA,'Example:5',True),(12,533,'Example5 area working','Integralofpositivee^(2x)over[0,p]gives(e^(2p)−1)/2.',AREA,'Example:5',False),(13,533,'Example5 logarithmic bound recovery','Area5forces e^(2p)=11,p=ln11/2≈1.2to2sf.',LOG,'Example:5',False),(14,533,'Try5Q1 GIVEN shaded graph','Curve8x+e^x/2,axesandrightbounda>0. Shadeundercurveabovexaxisbetween0anda. Area1/2isintegratedregion,notordinate.',AREA,'Try-Now-5:1',True),(15,533,'Try5Q2 GIVEN between-curves graph','Decayinge^−xintersectshorizontaly1at(0,1);shadeabovecurvebelow1from0torightboundp.',AREA,'Try-Now-5:2',True)]
for n,page,label,note,d,parent,given in refs:
 fig(n,page,label,note,[d],'graph'if given else'table',[],parent);figures[-1].update(item_id=f'8227:TB:YM:C12:Teaching-figure:{n}',printed_page=pp(page),source_evidence=ev(page),value_level_scope_decisions=[],item_kind='given-figure'if given else'teaching-figure',parent_item_id='8227:TB:YM:C12:'+parent)
 figures[-1]['mathematical_feature_review']['method']='Readactualgivenregionsandtheirfixedboundaries;top-minus-bottomandpositiveparameterbranchespreserved. Recomputeoriginalcurveconstraintsandareas. Solutionworkingpanelsareseparatefromgivengraphs.'
pages=[dict(pdf_page=page,printed_page=pp(page),chapter=12,page_status='items enumerated',item_ids=[r['item_id']for r in answers if r['source_pdf_page']==page]+[r['item_id']for r in figures if r['pdf_page']==page],continuation_item_ids=[],source_evidence=ev(page),reader='Codex author',date='2026-11-20',non_item_content='AllExample4/Try4Q1–3,Example5/Try5Q1–2andsevengiven/workingpanelsenumerated. GIVENgraphsnotrequestedsketchresponses.',scope_screen='Oneversustwointegrationconstants,originalpoint/gradientconditions,andtheactualshadedgeometricregion. No general substitution.')for page in range(532,534)]
def save():
 for row in answers:
  for p in row['subparts']:
   if'operation'in p:assert equivalent(compute(p['operation']),expression(p.get('author_expected_normalised',p['printed_key_normalised']))),(row['item_id'],p['subpart'])
   for name,op in p.get('additional_operations',{}).items():assert equivalent(compute(op),expression(p['additional_operation_expected'][name])),(row['item_id'],p['subpart'],name)
 for name,data in [('answers-YM-C12-curves.json',dict(scope='Complete532–533curve/arearesponses.',items=answers)),('census-YM-C12-curves.json',dict(book='YM',book_id='8227-SRC-017',chapter=12,source_path=SRC,source_sha256=SHA,scope='Complete532–533page/item/given-graphcensus.',new_items=new+figures,corrections=corrections,pages=pages))]:(W/'tools/textbook-r5'/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
 print(len(answers),'items;',sum(len(r['subparts'])for r in answers),'responses;',len(figures),'references;',len(pages),'pages')
if __name__=='__main__':save()
