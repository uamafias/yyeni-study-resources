"""YM540–541: power reduction, exact finite integrals and scaffolded identity chains."""
import json
import author_YM_C12_trig_opening as t
import author_YM_C12_opening as a
from author_YM_C12_opening import h,W,SRC,SHA,pp,ev,fig,figures,extra,compute,expression,equivalent
from verify_textbook_answers_r5 import primitive_agrees
h.answers.clear();h.new.clear();h.corrections.clear();figures.clear()
answers=h.answers;new=h.new;corrections=h.corrections
TRIG=t.TRIG;IDENT=t.IDENT;SQUARE=t.SQUARE;DEF=a.DEF;DOUBLE='8227:2020:M2:T3:O02:D03';COMPOUND='8227:2020:M2:T3:O02:D02'
def add(kind,n,page,note,parts):
 r=a.add(kind,n,page,note,parts);r.update(mapping_rationale='Unscaffolded sin²/cos²/cos⁴ integrals require identity choice and transformed-square integration. A separate shown identity directly assesses its requested transformation;the HENCE integral uses a supplied identity and must not automatically claim an independent identity-selection decision. Cubic sine derived through a supplied triple-angle relation is distinct from ordinary squared-power reduction. Exact finite evaluation and original radian intervals remain visible.',precision_angle_check=dict(source='Exactradianprimitive/finiteintegralanswers;noapproximationsrequested.',comparison='Keepπandradicals,innerargumentmultipliersandallcross-terms. Tan/secintervalsarecheckedforpoles;ordinarysine/cosinepowersarecontinuous.'))
 return r

def ip(l,f,k,kp):
 p=t.ip(l,f,k,kp);p.update(assessed_8227_demand_ids=[IDENT,SQUARE],component_demand_ids=[TRIG]);return p

def dv(l,f,lo,hi,k,kp,direct=None,show=False):
 p=a.dv(l,f,lo,hi,k,kp);p.update(assessed_8227_demand_ids=direct if direct is not None else[TRIG,DEF],component_demand_ids=[TRIG]if direct and TRIG not in direct else[],source_angle_unit='radians')
 if show:p.update(check_mode='show/prove',response_format='proof/show-that')
 return p

def proof(l,lhs,rhs,kp,method,compound=False):
 p=a.val(l,'trigsimp(expand_trig(('+lhs+')-('+rhs+')))','0',kp,method,[DOUBLE]+([COMPOUND]if compound else[]));p.update(check_mode='show/prove',response_format='proof/show-that',original_lhs=lhs,original_rhs=rhs,original_common_domain='Allrealradianarguments;nosine/cosinepolesinthisidentity.');return p
add('Example',14,540,'Indefinitepowerreduction:(a)3cos²x;(b)sin²3x. DoubletheORIGINALinnerargumentbeforeintegratingthecosineterm;factor1/12in(b).',[ip('a','3*cos(x)**2','3*x/2+3*sin(2*x)/4',540),ip('b','sin(3*x)**2','x/2-sin(6*x)/12',540)])
add('Try-Now',14,540,'Fourpower-reductionprimitives:3sin²x,4cos²(x/2),2sin²2x,cos⁴x. Lastrequiresrepeatedreduction,retainingconstant3/8andbothharmonics2x,4x.',[ip('a','3*sin(x)**2','3*x/2-3*sin(2*x)/4',650),ip('b','4*cos(x/2)**2','2*x+2*sin(x)',650),ip('c','2*sin(2*x)**2','x-sin(4*x)/4',651),ip('d','cos(x)**4','3*x/8+sin(2*x)/4+sin(4*x)/32',651)])
add('Example',15,540,'Exact0..π/6integralcos²x+sin2x. Choosehalf-angleformforcos²,thenretainπ/12+√3/8+1/4.',[dv('exact-integral','cos(x)**2+sin(2*x)',0,'pi/6','pi/12+sqrt(3)/8+Rational(1,4)',540,[IDENT,SQUARE,DEF])])
add('Try-Now-15',1,540,'Exact0..π/2integralsin2x+cosx;bothtermsprimitiveatbothendpoints,sum2.',[dv('exact-integral','sin(2*x)+cos(x)',0,'pi/2','2',651)])
add('Try-Now-15',2,540,'Exact0..π/6integralcos2x+sinx;preservenegativecosineprimitive,result1−√3/4.',[dv('exact-integral','cos(2*x)+sin(x)',0,'pi/6','1-sqrt(3)/4',651)])
add('Try-Now-15',3,540,'Exact0..π/3integralsin2x+sec²x;wholeintervalavoidsfirstsecantpoleπ/2,result3/4+√3.',[dv('exact-integral','sin(2*x)+sec(x)**2',0,'pi/3','Rational(3,4)+sqrt(3)',651)])
p=dv('shown-integral','3+2*tan(x)**2','-pi/4','pi/4','4+pi/2',540,[IDENT,TRIG,DEF],True);p.update(source_variable='theta',normalised_variable='x',required_method='Usetan²θ=sec²θ−1;keepbothsymmetricendpointsandtheirconstants. Entireintervalavoidstanpoles.')
add('Try-Now-15',4,540,'SHOW−π/4..π/4integral(3+2tan²θ)dθ=(8+π)/2. Symmetryisavalidalternativeonceintegrand/domainarechecked.',[p])
p=proof('a-identity','(2*sin(x)+cos(x))**2','Rational(5,2)+2*sin(2*x)-3*cos(2*x)/2',541,'ExpandORIGINALsquarewithcrossterm4sinxcosx. ReducetheTWOdistinctsquaresanduse2sinxcosx=sin2x;retainconstant5/2,sinecoefficient2,cosine−3/2.')
q=dv('b-exact-integral','(2*sin(x)+cos(x))**2',0,'pi/4','5*pi/8+Rational(1,4)',541,[SQUARE,DEF]);q['depends_on_source_parts']=['a-identity'];q['required_method']='HENCEusetheidentityalreadyestablishedin(a). Anindependentchoiceofidentityisnottheadditionaldemandhere.'
add('Example',16,541,'(a)SHOWtheexpanded/reducedidentityfor(2sinx+cosx)²;(b)HENCEexact0..π/4integral5π/8+1/4. Identityproductionandscaffoldeduseareseparateparts.',[p,q])
p=proof('identity','tan(x)**2+cos(x)**2','sec(x)**2+cos(2*x)/2-Rational(1,2)',541,'Onoriginalcosx≠0,usetan²=sec²−1andcos²=(1+cos2x)/2. Retainnegativeconstant−1/2.');p['original_common_domain']='cosx≠0;identicalonbothsidesonlyontheircommondomain.'
q=dv('exact-integral','tan(x)**2+cos(x)**2',0,'pi/4','Rational(5,4)-pi/8',651,[SQUARE,TRIG,DEF]);q['depends_on_source_parts']=['identity']
add('Try-Now-16',1,541,'SHOWtan²x+cos²x=sec²x+(1/2)cos2x−1/2,andHENCEexact0..π/4integral5/4−π/8. Sourcekeysuppliesonlyfinalintegral;identitycheckedagainststem.',[p,q])
p=proof('a-identity','12*sin(x)**2*cos(x)**2','3*(1-cos(4*x))/2',541,'Originalproduct12sin²xcos²x=3sin²2x;powerreductionof2xgives(3/2)(1−cos4x).')
q=dv('b-shown-integral','12*sin(x)**2*cos(x)**2','pi/4','pi/3','pi/8+3*sqrt(3)/16',541,[SQUARE,DEF],True);q['depends_on_source_parts']=['a-identity']
add('Try-Now-16',2,541,'(a)SHOW12sin²xcos²x=(3/2)(1−cos4x);(b)HENCEshowπ/4..π/3integralπ/8+3√3/16. Boundsandnegativeendpointcosineprimitivearepreserved.',[p,q])
p=proof('a-required-expansion','sin(3*x)','3*sin(x)-4*sin(x)**3',541,'REQUIREDroute:expandoriginalsin(2x+x)bysineaddition,thenuseactualdouble-angleandPythagoreanidentitiestoreach3sinx−4sin³x. Averifiedidentityaloneisnotproofthatthelearnerusedtherequiredroute.',True);p['required_method']='Expand sin(2x+x) and use double-angle formulae.'
q=dv('b-shown-integral','sin(x)**3',0,'pi/3','Rational(5,24)',541,[TRIG,DEF],True);q['depends_on_source_parts']=['a-required-expansion'];q['required_method']='HENCErearrange(a):sin³x=(3sinx−sin3x)/4,beforeintegrating. Generalintegrationbysubstitutionnotrequired.'
add('Try-Now-16',3,541,'(a)ByREQUIREDcompoundexpansionanddouble-angleformulaeSHOWsin3x=3sinx−4sin³x;(b)HENCEshow0..π/3integralsin³x=5/24.',[p,q])
refs=[(44,540,'Example14(a) cosine-square reduction working','3cos²x→(3/2)(1+cos2x).',[IDENT,SQUARE],'table','Example:14'),(45,540,'Example14(b) sine-square affine reduction working','sin²3x→(1−cos6x)/2;inner6factorretained.',[IDENT,SQUARE],'table','Example:14'),(46,540,'Example15 transformed finite-integral working','Usecos²xhalf-anglebeforeintegratingallterms.',[IDENT,SQUARE,DEF],'table','Example:15'),(47,540,'Example15 exact-endpoint evaluation working','Substitute0andπ/6intooneprimitive,retainingradicalandπterms.',[DEF],'table','Example:15'),(48,540,'Example15 thirty-sixty solution reference triangle','Sides1,√3,2withanglesπ/6,π/3;solutionaidforexactendpointvalues,notgivenregiongeometry.',[TRIG],'diagram','Example:15'),(49,540,'Example15 zero-angle limiting reference diagram','Displayed0lengthopposite0°isadegeneratelimitingreference,notanordinarynondegeneratetriangleorvariableconstruction. Itillustratessin0=0,cos0=1.',[TRIG],'diagram','Example:15'),(50,541,'Example16(a) expanded identity working','Allsquareandcrosstermcoefficientsretained;target5/2+2sin2x−(3/2)cos2x.',[DOUBLE],'table','Example:16'),(51,541,'Example16(b) scaffolded integration working','Useprecedingidentityratherthanrequirenewidentitychoice.',[SQUARE,DEF],'table','Example:16'),(52,541,'Example16(b) exact endpoints working','Atπ/4and0theconstanttermsdiffer;answer5π/8+1/4.',[DEF],'table','Example:16')]
for n,page,label,note,ds,rep,parent in refs:
 fig(n,page,label,note,ds,rep,[],parent);figures[-1].update(item_id=f'8227:TB:YM:C12:Teaching-figure:{n}',printed_page=pp(page),source_evidence=ev(page),value_level_scope_decisions=[],item_kind='teaching-figure',parent_item_id='8227:TB:YM:C12:'+parent)
 figures[-1]['mathematical_feature_review']['method']='Readactualradianbounds,powers,cross-termsandHENCEscaffolding. Independentlyintegrateoriginalexpressionsandcheckidentities. Solutiontrianglesareexact-valueaids;the0°referenceisdegenerate,notvalidgeneraltrianglegeometry.'
pages=[dict(pdf_page=page,printed_page=pp(page),chapter=12,page_status='items enumerated',item_ids=[r['item_id']for r in answers if r['source_pdf_page']==page]+[r['item_id']for r in figures if r['pdf_page']==page],continuation_item_ids=[],source_evidence=ev(page),reader='Codex author',date='2026-11-20',non_item_content='AllExample14/Try14,Example15/Try15Q1–4,Example16/Try16Q1–3andactualsolution/referencepanelsenumerated. EachshownidentityanditsHENCEintegralhasitsownresponseanddependency.',scope_screen='Identityfacilitatedintegrationincludesrepeatedpowerreductionandscaffoldedtriple-anglecubic. No general substitutionscopeinferred;allfiniteintervalscontinuous.')for page in range(540,542)]
def save():
 for row in answers:
  for p in row['subparts']:
   if'operation'in p:
    got=compute(p['operation']);expected=expression(p.get('author_expected_normalised',p['printed_key_normalised']))
    assert primitive_agrees(p['operation'],got,expected)if p.get('answer_equivalence')=='up-to-additive-constant'else equivalent(got,expected),(row['item_id'],p['subpart'])
 for name,data in [('answers-YM-C12-trig-powers.json',dict(scope='Complete540–541identity/power/finiteintegralresponses.',items=answers)),('census-YM-C12-trig-powers.json',dict(book='YM',book_id='8227-SRC-017',chapter=12,source_path=SRC,source_sha256=SHA,scope='Complete540–541page/item/solutionfigurecensus.',new_items=new+figures,corrections=corrections,pages=pages))]:(W/'tools/textbook-r5'/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
 print(len(answers),'items;',sum(len(r['subparts'])for r in answers),'responses;',len(figures),'references;',len(pages),'pages')
if __name__=='__main__':save()
