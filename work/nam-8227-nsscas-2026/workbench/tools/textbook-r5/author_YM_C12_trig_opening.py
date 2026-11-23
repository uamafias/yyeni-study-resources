"""YM538–539: radian affine trig primitives and identity prerequisites."""
import json
import author_YM_C12_opening as a
from author_YM_C12_opening import h,W,SRC,SHA,pp,ev,fig,figures,extra,compute,expression,equivalent
from verify_textbook_answers_r5 import primitive_agrees
h.answers.clear();h.new.clear();h.corrections.clear();figures.clear()
answers=h.answers;new=h.new;corrections=h.corrections
TRIG='8227:2020:M2:T5:O01:D02';IDENT='8227:2020:M2:T5:O02:D01';SQUARE='8227:2020:M2:T5:O02:D02';POWER='8227:2020:M1:T9:O01:D02';DERIV='8227:2020:M2:T4:O01:D01'
def ip(label,f,key,kp,identity=False,power=False,domain='Allrealradianx.'):
 p=a.primitive(label,f,key,kp);p.update(assessed_8227_demand_ids=[TRIG]+([IDENT]if identity else[])+([POWER]if power else[]),component_demand_ids=[],original_domain=domain,source_angle_unit='radians',author_method='Integrate ORIGINAL affine trig argument in RADIANS,retaining its inner coefficient and sign. For tan²use sec²−1 before integrating;1/cos² is sec² by definition. Keep original cosine/tangent poles and compare separately transcribed primitive up to arbitrary constants on each original connected component.')
 return p

def add(kind,n,page,note,parts):
 r=a.add(kind,n,page,note,parts);r.update(mapping_rationale='Basic affine sin/cos/sec² integration directly assesses M2T5O01D02. A tan² integral additionally demands choosing tan²=sec²−1;merely recognising1/cos²as sec² does not create a new power-reduction family. Actual polynomial/rational power terms are directly assessed when included in the requested primitive. The unassigned half-angle teaching panels teach identity choice/square reduction but are not extra questions.',precision_angle_check=dict(source='AllargumentsandprimitivesinRADIANS;exactsymbolicformsplusC. No degree-modebranchorrounding.',comparison='Differentiateoriginalkeyonitsoriginalconnectedrealcomponent. Negativeinnercoefficientchangesprimitivesign;cosine/tangentpolesremainexcluded.'))
 if any(POWER in p.get('assessed_8227_demand_ids',[])for p in parts):
  actual={('Try-Now',12):'Part(b)explicit4xhaspower1.',('Example',13):'Part(a)x²haspower2;part(b)1/x²haspower−2.',('Try-Now',13):'Part(a)√xhaspower1/2;part(b)constant2haspower0.'}[(kind,n)]
  r['value_level_scope_decisions'].append(dict(rule_id='8227:QUAL05',status='within',quoted_value=actual,reason='Theactualdirectpower-integrationsubtermsarerationalpowersdifferentfrom−1. TrigtermsarehandledbyM2T5,notbyextendingthepowerformula.'))
  r['scope_check']['limits_considered'].append('8227:QUAL05')
 return r
add('Example',11,538,'Threebasicradianprimitives:cos2x,sin3x,sec²(x/2). Innercoefficient1/2inlastrequiresfactor2,not1/2.',[ip('a','cos(2*x)','sin(2*x)/2',538),ip('b','sin(3*x)','-cos(3*x)/3',538),ip('c','sec(x/2)**2','2*tan(x/2)',538,domain='cos(x/2)≠0;separateconnectedcomponents.')])
add('Try-Now',11,538,'Threebasicradianprimitives:sin4x,cos(x/3),sec²2x. Preservefactor−1/4,3,1/2respectively.',[ip('a','sin(4*x)','-cos(4*x)/4',650),ip('b','cos(x/3)','3*sin(x/3)',650),ip('c','sec(2*x)**2','tan(2*x)/2',650,domain='cos2x≠0;separateconnectedcomponents.')])
add('Example',12,539,'Integrate(a)tan²xbychoosingsec²x−1;(b)4/(5cos²3x)byreciprocaldefinitionandaffineinnerfactor3.',[ip('a','tan(x)**2','tan(x)-x',539,identity=True,domain='cosx≠0;separateconnectedcomponents.'),ip('b','4/(5*cos(3*x)**2)','4*tan(3*x)/15',539,domain='cos3x≠0;separateconnectedcomponents.')])
add('Try-Now',12,539,'Integrate(a)tan²2xvia sec²2x−1;(b)4x+1/(2cos²7x),retainingthepolynomialprimitiveandfactor1/14.',[ip('a','tan(2*x)**2','tan(2*x)/2-x',650,identity=True,domain='cos2x≠0.'),ip('b','4*x+1/(2*cos(7*x)**2)','2*x**2+tan(7*x)/14',650,power=True,domain='cos7x≠0.')])
add('Example',13,539,'Mixedprimitives:(a)x²+sec²(2−3x);(b)1/x²−3sin(8x+5). Retainoriginalnegativeinner−3andoriginalpolex0.',[ip('a','x**2+sec(2-3*x)**2','x**3/3-tan(2-3*x)/3',539,power=True,domain='cos(2−3x)≠0.'),ip('b','1/x**2-3*sin(8*x+5)','-1/x+3*cos(8*x+5)/8',539,power=True,domain='x≠0;independentconstantsoneachcomponent.')])
# SymPy leaves the shifted secant-square sum unevaluated. Normalize the
# independently transcribed original by the reciprocal definition, not by
# supplying a primitive; assert that rewrite separately.
p=answers[-1]['subparts'][0]
p['operation']['operands']=['x**2+1/cos(2-3*x)**2']
p['operation']['integration_coordinate']={'scale':'3','offset':'-2'}
p['integration_input_normalization']='sec(u)^2=1/cos(u)^2 on the original cos(u)≠0 components; original integrand retained separately. Internal CAS uses affine coordinateu3x−2 toavoidunresolvedorremovable-half-angleforms;thisisnotarequiredlearnergeneralsubstitutionmethod.'
extra(p,'original-integrand-rewrite','trigsimp(x**2+sec(2-3*x)**2-(x**2+1/cos(2-3*x)**2))','0')
add('Try-Now',13,539,'Mixedprimitives:(a)√x+cos(5x−3);(b)2+3cos(2−3x). Evenrootdomainkeptandnegativeinnercoefficientin(b)cancelsouter3to−sin.',[ip('a','sqrt(x)+cos(5*x-3)','2*x**Rational(3,2)/3+sin(5*x-3)/5',650,power=True,domain='Originalx≥0;primitiveonx>0withcontinuousextensionto0.'),ip('b','2+3*cos(2-3*x)','2*x-sin(2-3*x)',650,power=True)])
refs=[(32,538,'Radian derivative reference table','Sixbasic/affine sin,cos,tanderivatives;retaininnerfactorandnegativecosinederivative. Derivativecontextdoesnotturntheassignedintegralsintoderivativequestions.',[DERIV],None),(33,538,'Radian integration reference table','Sixbasic/affine cos,sin,sec²primitives;dividebynonzeroinnerfactor,includeC. Forzeroaffineslopeintegrandisconstantwherefinite,notdivisionby0.',[TRIG],None),(34,538,'Example11(a) working','cos2xprimitive(1/2)sin2x+C.',[TRIG],'Example:11'),(35,538,'Example11(b) working','sin3xprimitive−(1/3)cos3x+C.',[TRIG],'Example:11'),(36,538,'Example11(c) working','sec²(x/2)primitive2tan(x/2)+C,originalcos(x/2)≠0.',[TRIG],'Example:11'),(37,539,'Tangent-square identity panel','tan²x=sec²x−1oncosx≠0. Choosearearrangementwhosepieceshaveknownprimitives.',[IDENT],'Example:12'),(38,539,'Example12(a) transformed tangent-square working','Integratesec²x−1totanx−x+C.',[IDENT,TRIG],'Example:12'),(39,539,'Example12(b) reciprocal-cosine working','4/(5cos²3x)=(4/5)sec²3x;primitive(4/15)tan3x+C.',[TRIG],'Example:12'),(40,539,'Example13(a) mixed-power and secant working','Originalnegativeinner2−3xcontributes−1/3inprimitive.',[TRIG,POWER],'Example:13'),(41,539,'Example13(b) reciprocal-power and sine working','Primitive−1/x+(3/8)cos(8x+5)+C;originalx≠0.',[TRIG,POWER],'Example:13'),(42,539,'Sine-square half-angle teaching panel','sin²x=(1−cos2x)/2. Thisunassignedreferencefacilitatesthenextintegrationsequence.',[IDENT,SQUARE],None),(43,539,'Cosine-square half-angle teaching panel','cos²x=(1+cos2x)/2. Distinguishpowerreductionfromtheunrelatedtan²rearrangement.',[IDENT,SQUARE],None)]
for n,page,label,note,ds,parent in refs:
 fig(n,page,label,note,ds,'table',[],parent);figures[-1].update(item_id=f'8227:TB:YM:C12:Teaching-figure:{n}',printed_page=pp(page),source_evidence=ev(page),value_level_scope_decisions=[],item_kind='teaching-figure',parent_item_id='8227:TB:YM:C12:'+parent if parent else None)
 figures[-1]['mathematical_feature_review']['method']='Readactualradianarguments,coefficients,polesandpower-reductionidentities. Independentlydifferentiateeverytranscribedprimitive. Reference/solutionpanelsarenotgivendiagramsoraskedsketches.'
pages=[dict(pdf_page=page,printed_page=pp(page),chapter=12,page_status='items enumerated',item_ids=[r['item_id']for r in answers if r['source_pdf_page']==page]+[r['item_id']for r in figures if r['pdf_page']==page],continuation_item_ids=[],source_evidence=ev(page),reader='Codex author',date='2026-11-20',non_item_content='AllExample11/Try11,Example12/Try12,Example13/Try13andactualradianreference/solution/identitypanelsenumerated. Thetwohalf-anglepanelsareteachingevidence,notassignedextras.',scope_screen='Simpleaffine sin/cos/sec²radianintegration,optionalpowersummedterms,andrequiredtan²identitychoice. Originaleven-rootandtrigpoledomainsretained.')for page in range(538,540)]
def save():
 for row in answers:
  for p in row['subparts']:
   if'operation'in p:assert primitive_agrees(p['operation'],compute(p['operation']),expression(p['printed_key_normalised'])),(row['item_id'],p['subpart'])
 for name,data in [('answers-YM-C12-trig-opening.json',dict(scope='Complete538–539radianprimitiveandidentityresponses.',items=answers)),('census-YM-C12-trig-opening.json',dict(book='YM',book_id='8227-SRC-017',chapter=12,source_path=SRC,source_sha256=SHA,scope='Complete538–539page/item/referencecensus.',new_items=new+figures,corrections=corrections,pages=pages))]:(W/'tools/textbook-r5'/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
 print(len(answers),'items;',sum(len(r['subparts'])for r in answers),'responses;',len(figures),'references;',len(pages),'pages')
if __name__=='__main__':save()
