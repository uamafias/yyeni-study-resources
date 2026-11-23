"""YM534–535: logarithmic primitives with branch conditions; a pole-crossing defect."""
import json
import author_YM_C12_opening as a
from author_YM_C12_opening import h,W,SRC,SHA,pp,ev,v,reasoning,fig,figures,extra,compute,expression,equivalent
from verify_textbook_answers_r5 import primitive_agrees
h.answers.clear();h.new.clear();h.corrections.clear();figures.clear()
answers=h.answers;new=h.new;corrections=h.corrections
EXP=a.EXP;DEF=a.DEF;POWER='8227:2020:M1:T9:O01:D02';LOG=a.LOG

def add(kind,n,page,note,parts):
 r=a.add(kind,n,page,note,parts);r.update(mapping_rationale='Reciprocal-affine integration directly assesses M2T5O01D01. Polynomial/reciprocal-power terms in the same asked primitive additionally assess M1T9O01D02. An explicitly requested validity interval is retained separately. The source first gives ordinary logarithms on their positive-argument branch;the real primitive with ln|u| also exists separately on the negative branch. This does not allow crossing a pole in a definite integral.',precision_angle_check=dict(source='Exact logarithmic primitives and finite values;no numerical rounding orangle.',comparison='Compare primitive derivatives on original connected real components. Positive-argument ordinary ln is a restricted source branch;use ln|u| for both nonzero components. The severe Example8(b)error is a pole crossing,which absolute-value bars do not repair.'))
 if any(POWER in p.get('assessed_8227_demand_ids',[])for p in parts):
  actual='Example7expanded16x^(−2)−8x^(−1)+1.'if kind=='Example'else'Try7(a)9+12/x+4/x²;(b)1−10/x+25/x²;(c)π/(2x²)+7/(2x).'
  r['value_level_scope_decisions'].append(dict(rule_id='8227:QUAL05',status='within',quoted_value=actual,reason='ActualM1powertermsn−2and0arerationalandnot−1. Theexplicitn−1termsuseMath2logarithmicintegration;theexcludedpower-formulaexceptionisnotignored.'))
  r['scope_check']['limits_considered'].append('8227:QUAL05')
 return r

def ip(label,f,key,kp,positive,excluded,mixed=False):
 p=a.primitive(label,f,key,kp);p.update(assessed_8227_demand_ids=[EXP,POWER]if mixed else[EXP],original_domain=excluded,printed_primitive_domain=positive,source_convention='Printedordinarylnprimitivecorrectonitsstatedpositive-argumentbranch. AcompleteREALprimitiveusesln|affineargument|onseparatecomponents;constantsmaydiffer. Source534ruleand535noteareinternalconventionevidence,notanofficialmarkingrestriction.',author_answer_form='PrimitiveplusarbitraryCineachconnectednonzero-denominatorcomponent;extendordinarylntoln|u|fornegativearguments.')
 return p

def domain(label,condition,kp,full):
 p=reasoning(label,condition,'Theordinarylnargumentmustbepositive.Solvetheactualaffineinequalitywithoutlosingthecoefficientssign. ThisisvalidityofthePRINTEDordinary-lnformula;theoriginalrationalintegrandhasseparatecomponents'+full+'.',kp,'matches');p.update(assessed_8227_demand_ids=[EXP],component_demand_ids=[LOG],given_representation='text',response_format='explanation',original_integrand_domain=full);return p
ps=[]
for l,f,k,pos,full in [('a','1/(3*x)','log(x)/3','x>0','x≠0'),('b','5/(4*x+3)','5*log(4*x+3)/4','x>−3/4','x≠−3/4'),('c','6/(1-6*x)','-log(1-6*x)','x<1/6','x≠1/6')]:ps.extend([ip(l+'-primitive',f,k,534,pos,full),domain(l+'-validity',pos,534,full)])
add('Example',6,534,'Integrate1/(3x),5/(4x+3),6/(1−6x)ANDstatethevalidityofthechosenordinary-lnformulas. Correctrestrictedbranchesx>0,x>−3/4,x<1/6;fullrealprimitivesretainbothpole-separatedcomponents.',ps)
ps=[]
for l,f,k,pos,full in [('a','5/x','5*log(x)','x>0','x≠0'),('b','1/(3*x-1)','log(3*x-1)/3','x>1/3','x≠1/3'),('c','3/(7-9*x)','-log(7-9*x)/3','x<7/9','x≠7/9')]:ps.extend([ip(l+'primitive',f,k,650,pos,full),domain(l+'validity',pos,650,full)])
add('Try-Now',6,535,'Integrate5/x,1/(3x−1),3/(7−9x),ANDstatetheordinary-lnvalidityintervalforeach. Negativeinner−9requires−1/3andflipsdomaininequality.',ps)
add('Example',7,535,'ExpandORIGINAL(4−x)²/x²=16/x²−8/x+1beforeintegrating. Restrictedprintedprimitive−16/x−8lnx+x+Cisvalidx>0;fullrealprimitiveusesln|x|onx≠0.',[ip('primitive','(4-x)**2/x**2','-16/x-8*log(x)+x',535,'x>0','x≠0',True)])
add('Try-Now',7,535,'Integratethreeoriginalrationalexpressionsafterdivision/expansion:(3+2/x)²,(x−5)²/x²,(π+7x)/(2x²). Preserveπandthefactor1/2;alloriginaldenominatorsexclude0.',[ip('a','(3+2/x)**2','9*x+12*log(x)-4/x',650,'x>0','x≠0',True),ip('b','(x-5)**2/x**2','x-10*log(x)-25/x',650,'x>0','x≠0',True),ip('c','(pi+7*x)/(2*x**2)','-pi/(2*x)+7*log(x)/2',650,'x>0','x≠0',True)])
p=a.dv('a','1/(2*x+1)',2,4,'log(Rational(9,5))/2',535)
q=reasoning('b','Divergent ordinary improper integral;no finite value.','The ORIGINAL4/(3−2x)hasapolex3/2INSIDE[1,3]. Splitthere. Leftintegralapproaches+infinity;rightapproaches−infinity. Bothmustconvergeseparatelyforanordinaryimproperintegral,soitisundefined. Printed−ln9comesfrominvalidendpointsubtractionacrossthepole. ln|u|doesnotrestorecontinuity;aprincipalvalueisnottherequesteddefiniteintegral.',535,'key wrong');q.update(assessed_8227_demand_ids=[],component_demand_ids=[EXP,DEF],given_representation='text',response_format='explanation',original_integrand='4/(3-2*x)',original_bounds=['1','3'],original_domain='x≠3/2;originalintervalcrossesthepole',printed_key_normalised='-log(9)',source_interpretation='Defectivefinite-integralworkedexemplar;excludedfromvalidtaskcoverage.')
extra(q,'left-one-sided-integral','limit(-2*log(2*b),b,0,dir="+")','oo');extra(q,'right-one-sided-integral','limit(-2*log(3)+2*log(2*b),b,0,dir="+")','-oo');extra(q,'invalid-endpoint-difference','-2*log(Abs(3-2*3))+2*log(Abs(3-2*1))','-log(9)')
r=add('Example',8,535,'Twofinite-integralworkedexamples:(a)1/(2x+1)on[2,4]isproperwithanswer(1/2)ln(9/5);(b)4/(3−2x)on[1,3]crosses3/2andprinted−ln9isinvalid.',[p,q]);r['scope_check'].update(status='in-scope-parts-only',excluded_or_qualified_parts=['Part(b)defectivepole-crossingtask;noordinaryfiniteintegralexists. Retaininternaldiagnosis,notvalidexemplarcoverage.'])
refs=[(16,534,'Reciprocal-affine positive-argument integration rules','Ordinarylnxandln(ax+b)rulesarepresentedwithpositivearguments. Generalrealformln|u|appliesonbothnonzerocomponents,withnonzeroa;ifa0theintegrandconstant1/bintegratesx/bwhenb≠0.',EXP,None),(17,534,'Example6(a) scalar reciprocal working','1/(3x)=(1/3)(1/x);ordinarylnxbranchx>0.',EXP,'Example:6'),(18,534,'Example6(b) affine reciprocal working','5/(4x+3)gives5/4ln(4x+3),branchx>−3/4.',EXP,'Example:6'),(19,534,'Example6(c) negative affine coefficient working','6/(1−6x)gives−ln(1−6x),branchx<1/6.',EXP,'Example:6'),(20,535,'Example7 expansion and primitive working','Expand(4−x)²beforedividingbyx²;middleterm−8/xrequireslogprimitive.',EXP,'Example:7'),(21,535,'Example8(a) valid logarithmic endpoints','[2,4]containsnopoleof1/(2x+1),soendpointdifference(1/2)ln(9/5)isvalid.',DEF,'Example:8'),(22,535,'Example8(b) invalid pole-crossing working','Nativebounds1and3straddlex3/2. Printed−ln9isnotordinaryintegral;one-sidedlimitsdivergeoppositely.',DEF,'Example:8'),(23,535,'Absolute-log convention note','Sourceadvisesabsolutevalueonlyfordefiniteintegrals. Retainthisasaninternalconventioncaution:negative-branchindefiniteprimitivesalsoneedrealargument−uor|u|. AbsolutevaluesDONOTpermitcrossingapole.',EXP,None)]
for n,page,label,note,d,parent in refs:
 fig(n,page,label,note,[d],'table',[],parent);figures[-1].update(item_id=f'8227:TB:YM:C12:Teaching-figure:{n}',printed_page=pp(page),source_evidence=ev(page),value_level_scope_decisions=[],item_kind='teaching-figure',parent_item_id='8227:TB:YM:C12:'+parent if parent else None)
 figures[-1]['mathematical_feature_review']['method']='Readordinarylnpositivebranchesandactualnativebounds. Differentiateindependentlytranscribedprimitivekeys;distinguishrestrictedcorrectformsfromincorrectpole-crossingevaluation. Bothone-sidedlimitsandoriginaldenominatorexclusionsretained.'
pages=[dict(pdf_page=page,printed_page=pp(page),chapter=12,page_status='items enumerated',item_ids=[r['item_id']for r in answers if r['source_pdf_page']==page]+[r['item_id']for r in figures if r['pdf_page']==page],continuation_item_ids=[],source_evidence=ev(page),reader='Codex author',date='2026-11-20',non_item_content='AllExample6/Try6,Example7/Try7,Example8andactualrule/working/conventionpanelsenumerated. Askedvaliditystatementsareseparateresponses. Formulaillustrationsinteachingrulesremainpanels,notinventedindependentquestions.',scope_screen='Reciprocal-affineandmixedpowerintegration;Example8(b)defectivepolecrossingexcludedasvalidtask. Positiveordinarylnbranchdoesnotdescribeentirerationalintegranddomain.')for page in range(534,536)]
def save():
 for row in answers:
  for p in row['subparts']:
   if'operation'in p:
    got=compute(p['operation']);expected=expression(p.get('author_expected_normalised',p['printed_key_normalised']))
    assert primitive_agrees(p['operation'],got,expected)if p.get('answer_equivalence')=='up-to-additive-constant'else equivalent(got,expected),(row['item_id'],p['subpart'])
   for name,op in p.get('additional_operations',{}).items():assert equivalent(compute(op),expression(p['additional_operation_expected'][name])),(row['item_id'],p['subpart'],name)
 for name,data in [('answers-YM-C12-logarithms.json',dict(scope='Complete534–535reciprocalprimitiveanddomainresponses;polecrossingdefectretained.',items=answers)),('census-YM-C12-logarithms.json',dict(book='YM',book_id='8227-SRC-017',chapter=12,source_path=SRC,source_sha256=SHA,scope='Complete534–535page/item/panelcensus.',new_items=new+figures,corrections=corrections,pages=pages))]:(W/'tools/textbook-r5'/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
 print(len(answers),'items;',sum(len(r['subparts'])for r in answers),'responses;',len(figures),'references;',len(pages),'pages')
if __name__=='__main__':save()
