"""YM456–459: compound cosine/tangent,quadrant decisions and original proof domains."""
import json
import author_YM_C10_opening as o
import author_YM_C10_compound_sine as s
import author_YM_C9_opening as g
from author_YM_C9_opening import h,W,SRC,SHA,pp,v,fig,figures,extra,compute,expression,equivalent
from author_YM_C4_trig_graphs import reasoning
g.answers.clear();g.new.clear();g.corrections.clear();figures.clear()
answers=g.answers;new=g.new;corrections=g.corrections;ev=o.ev;h.common.base.ev=ev
COMP=o.COMPOUND;EVAL=o.EXACT;SPECIAL=s.SPECIAL

def exact(label,original,key,kp,special=False):
 p=s.exact(label,original,key,kp,special);return p

def ratio(label,expr,key,kp,constraints):
 p=v(label,expr,key,kp,'Start with the ORIGINAL supplied ratio and angle/quadrant constraints. Derive each missing ratio via1−sin²/1−cos²or1+tan²,choose its sign from the ORIGINAL quadrant,then apply the actual requested compound formula. Do not copy an unsigned reference triangle or swap the requested sine/cosine outputs to match a key.')
 p.update(assessed_8227_demand_ids=[COMP,EVAL],response_format='numeric',original_constraints=constraints)
 return p

def add(kind,n,page,note,parts):
 r=o.add(kind,n,page,note,parts);r.update(mapping_rationale='The discriminating decisions are reverse recognition,choosing a valid decomposition,determining missing ratio signs from ORIGINAL quadrants,and preserving identity common domains. Distinct source numerical angles within one recognition pattern are variations,not automatically separate families.',value_level_scope_decisions=[dict(rule_id='8227:QUAL03',status='not applicable',quoted_value=note,reason='Exact ratio/expression/proof outputs are requested,not periodic equation solution sets.')],scope_check=dict(status='in-scope',basis=note,excluded_or_qualified_parts=[],limits_considered=['8227:QUAL03']),precision_angle_check=dict(source='No-calculator exact values and formal identities throughout. Given quadrant bounds are degrees;some exact angles are explicitly radians.',comparison='Keep exact fractions/surds and correct sine/cosine signs. Original cotangent proofs may have a wider natural domain than an intermediate1/tan route;do not drop valid zeros merely to fit that route.'))
 return r
ps=[exact('a','cos(75*pi/180)*cos(15*pi/180)+sin(75*pi/180)*sin(15*pi/180)','Rational(1,2)',456,True),exact('b','cos(105*pi/180)','(sqrt(2)-sqrt(6))/4',456),exact('c','cos(19*pi/12)','(sqrt(6)-sqrt(2))/4',456)]
ps[0]['learner_decomposition']='cos(75°−15°)=cos60°.';ps[1]['learner_decomposition']='105°=60°+45°;cosinequadrantIIisnegative.';ps[2]['learner_decomposition']='19π/12=3π/4+5π/6;the actualcosineisquadrantIVpositive.'
add('Example',7,456,'Three original no-calculator cosine tasks:reverse differencepattern,cos105°,cos19π/12. Preserve each original argument and quadrant.',ps)
ps=[exact('a','cos(65*pi/180)*cos(25*pi/180)-sin(65*pi/180)*sin(25*pi/180)','0',643,True),exact('b','cos(15*pi/180)','(sqrt(2)+sqrt(6))/4',643),exact('c','cos(11*pi/12)','(-sqrt(6)-sqrt(2))/4',643)]
ps[0]['learner_decomposition']='cos(65°+25°)=cos90°=0.'
add('Try-Now',7,456,'Evaluate reversecosine-sumpattern65°/25°,cos15°,cos11π/12exactly. The last cosine must be negative in quadrantII.',ps)
constraints='OriginalcosA=8/17,sinB=−3/5,andA/BinSAMEquadrant. PositivecosAandnegativesinBtogetherforceBOTHintoquadrantIV.'
sa='(-sqrt(1-Rational(8,17)**2))';ca='Rational(8,17)';sb='(-Rational(3,5))';cb='sqrt(1-Rational(3,5)**2)'
p=ratio('a-cos-sum',f'({ca})*({cb})-({sa})*({sb})','-Rational(13,85)',457,constraints)
q=ratio('b-sin-difference',f'({sa})*({cb})-({ca})*({sb})','-Rational(36,85)',457,constraints)
add('Example',8,457,'Same-quadrantconstraintswithcosA8/17andsinB−3/5forcebothIV;derive sinA−15/17,cosB4/5,beforecos(A+B)and sin(A−B). Both outputs negative.',[p,q])
constraints='OriginalsinA=−3/5with270°<A<360°;cosB=8/17with0°<B<90°.'
sa='(-Rational(3,5))';ca='sqrt(1-Rational(3,5)**2)';cb='Rational(8,17)';sb='sqrt(1-Rational(8,17)**2)'
p=ratio('a-cos-difference',f'({ca})*({cb})+({sa})*({sb})','-Rational(13,85)',643,constraints)
p['author_source_working_comparison']=dict(status='key wrong',reason='The native key writescos(A−B)=cosAcosB−sinAsinB,which has the wrong compound sign. Its next line writes positive3/5in the added product and still concludes−13/85. The final−13/85IScorrect for the original signed ratios,but the displayed method is inconsistent.',observed_step='cos(A−B)=cosAcosB−sinAsinB;then(4/5)(8/17)+(3/5)(15/17)=−13/85.',correct_step='cos(A−B)=cosAcosB+sinAsinB=(4/5)(8/17)+(−3/5)(15/17)=−13/85.')
q=ratio('b-sin-sum',f'({sa})*({cb})+({ca})*({sb})','Rational(36,85)',643,constraints)
add('Try-Now-8',1,457,'Original AIV/BIconstrain missing signs;cos(A−B)=−13/85and sin(A+B)=36/85. Finalkeysagree,butnative(a)methodhaswrongformulasignandmissingnegativefactor.',[p,q])
constraints='OriginalsinA=3/5,tanB=5/12,andBOTH90°<angle<270°. Positive sine forcesAII;positive tangent forcesBIII.'
sa='Rational(3,5)';ca='(-sqrt(1-Rational(3,5)**2))';cb='(-1/sqrt(1+Rational(5,12)**2))';sb=f'(Rational(5,12)*({cb}))'
sdiff=f'(({sa})*({cb})-({ca})*({sb}))';cdiff=f'(({ca})*({cb})+({sa})*({sb}))'
p=ratio('a-sin-difference',sdiff,'Rational(63,65)',643,constraints);p['author_expected_normalised']='-Rational(56,65)'
q=ratio('b-cos-sum',f'({ca})*({cb})-({sa})*({sb})','-Rational(56,65)',643,constraints);q['author_expected_normalised']='Rational(63,65)'
r=reasoning('c-tan-difference','tan(A−B)=−56/33.','From the ORIGINAL signed ratiossin(A−B)=−56/65andcos(A−B)=33/65≠0. Their ratio is−56/33. The inspected completeTry8answerblock643goesdirectlyfrom2(b)toTry9;thereisNOprinted2(c). This is author-derived,not an attributed book answer.',643,'no key');r.update(assessed_8227_demand_ids=[COMP,EVAL],response_format='numeric',key_presence='no separate key',inspected_key_pdf_pages=[642,643,644],original_constraints=constraints);extra(r,'original-signed-compound-ratio',sdiff+'/'+cdiff,'-Rational(56,33)')
row=add('Try-Now-8',2,457,'OriginalAII/BIIIconstrain missing signs. Nativekeyswaps(a)/(b):correctsin(A−B)=−56/65,cos(A+B)=63/65. Sourcealsoasks(c)tan(A−B)=−56/33,butkeyomitsit.',[p,q,r]);r.update(answer_pdf_page=None,answer_printed_page=None,key_evidence=ev(643))
p=exact('value','(1+tan(15*pi/180))/(1-tan(15*pi/180))','sqrt(3)',458,True);p['learner_decomposition']='Replace1bytan45°andrecognise tan(45°+15°)=tan60°. Originaldenominatornonzero.'
add('Example',9,458,'No-calculator quotient(1+tan15°)/(1−tan15°)asksasurd;recognisesumtangentandreturn√3. Denominatornotzero.',[p])
ps=[exact('a','(1-tan(15*pi/180))/(1+tan(15*pi/180))','sqrt(3)/3',643,True),exact('b','tan(-15*pi/180)','-2+sqrt(3)',643),exact('c','cos(7*pi/12)/sin(7*pi/12)','-2+sqrt(3)',643)]
ps[0]['learner_decomposition']='tan(45°−15°)=tan30°.';ps[1]['learner_decomposition']='tan(30°−45°),oroddtangentof15°.';ps[2]['learner_decomposition']='cot(7π/12)=tan(π/2−7π/12)=tan(−π/12),withvalidoriginalsine denominator.'
add('Try-Now',9,459,'Evaluate three exact tangent/cotangent expressions;original7π/12isradiansanditscotangentnegative. Preserve reciprocaldomainanddifferencesign.',ps)
p=s.proof('identity','cos(pi/4-b)/sin(pi/4-b)','(sin(b)+cos(b))/(cos(b)-sin(b))',459,'sin(π/4−B)≠0,equivalentlycosB−sinB≠0.','A domain-complete proof expands ORIGINALcos(π/4−B)andsin(π/4−B)directly,then cancels their commonnonzero1/√2. The source instead firstuses1/tanandtanB,which introduces avoidable holes. Record that route only on its narrower common domain;the direct proof preservesvalid originalzeros.')
p['source_intermediate_domain_caution']='ForB=3π/4,the ORIGINALcot(−π/2)=0andRHS0aredefined,butthe source’s firsttan(−π/2)stepisundefined. ForB=π/2,the originalidentityisalsodefinedalthoughintermediatetanBisnot.'
extra(p,'valid-zero-lost-by-reciprocal-tan-route','Tuple((cos(pi/4-b)/sin(pi/4-b)).subs(b,3*pi/4),((sin(b)+cos(b))/(cos(b)-sin(b))).subs(b,3*pi/4))','Tuple(0,0)')
add('Example',10,459,'Prove originalcot(π/4−B)=(sinB+cosB)/(cosB−sinB). Directcos/sinproofcoversnaturalcommondomain;source1/tanrouteisconditionallyvalidandlosesvalidzerosifusedwithoutcare.',[p])
ps=[s.proof('a','tan(a-pi/4)','(sin(a)-cos(a))/(sin(a)+cos(a))',643,'cos(A−π/4)≠0,equivalentlysinA+cosA≠0.','Expand ORIGINALsineandcosineofA−π/4andtaketheirratio. ThisavoidstanAintermediatesandretainsvalidcosA0cases.'),s.proof('b','cos(a-b)/sin(a-b)','(cos(a)*cos(b)/(sin(a)*sin(b))+1)/(cos(b)/sin(b)-cos(a)/sin(a))',643,'sinA≠0,sinB≠0,and sin(A−B)≠0;the printedcotB−cotAdenominatorisnonzeroonthatdomain.','Rewrite ORIGINALcotA/cotBusingcos/sin,multiplythroughbynonzerosinAsinB,andrecognise compoundcosine/sineofA−B. Keep the common-domain restrictions rather than extending RHS to undefined individualcotangents.')]
add('Try-Now',10,459,'Prove tangent-shiftandcotangent-difference identities. Preserve original denominatorconditionsanduse a route that does not dropvalidnatural-domaincases unnecessarily.',ps)
refs=[(37,456,'Example7 reverse-cosine-difference working','75−15=60degreesandcos60=.5;recognise the plus-between-productsasCOSINEDIFFERENCE.',COMP,'table','Example:7'),(38,456,'Example7 exact quadrant coordinate reminders','Coordinatesfor60/45/3π/4/5π/6supplysignedratios;coordinateordercos,sin.',SPECIAL,'table','Example:7'),(39,456,'Example7 nonstandard cosine decompositions','105=60+45and19π/12=3π/4+5π/6. Originalquadrantsgiveoppositeoutputsigns.',COMP,'table','Example:7'),(40,457,'Example8 SOLUTION signed AIV triangle','Pythagorean8,15,17trianglehasx8,y−15,r17;thisisworkedsolution,notgivendiagram.',COMP,'diagram','Example:8'),(41,457,'Example8 SOLUTION signed BIV triangle','Pythagorean3,4,5trianglehasx4,y−3,r5;sinnegative,cospositive.',COMP,'diagram','Example:8'),(42,457,'Example8 signed compound working','cos(A+B)=−13/85,sin(A−B)=−36/85fromthetwoactualIVratios.',COMP,'table','Example:8'),(43,457,'Pythagorean triples reminder','3:4:5,5:12:13,7:24:25,8:15:17,9:40:41andpositivemultiples. A triple determinesmagnitudes,notquadrantsigns.',COMP,'table',None),(44,458,'Tangent-sum sine/cosine derivation','Divide compound sine/cosine bynonzerocosAcosB;the resulting tangentidentityhascommon-domainlimitations.',COMP,'table',None),(45,458,'Tangent-difference parity derivation','ReplaceBby−B,usetangentoddness;denominatorbecomes1+tanAtanB.',COMP,'table',None),(46,458,'Tangent formula pair','tan(A±B)=(tanA±tanB)/(1∓tanAtanB)wherealloriginaldisplayedtermsdefined.',COMP,'table',None),(47,458,'Example9 tangent-pattern working','1=tan45convertsquotienttotheadditionpattern;resulttan60√3.',COMP,'table','Example:9'),(48,458,'Example9 degree30/60 solution triangle','Exactlegs1,√3,hypotenuse2;tan60√3.',SPECIAL,'diagram','Example:9'),(49,459,'Example10 source reciprocal-tangent proof route','PrintedrouteusestanB,andreciprocaloftan(π/4−B). Directcos/sinproofisneededtoavoidlosingvalidcotangentzeros.',COMP,'table','Example:10'),(50,459,'Example10 radianπ/4 solution triangle','Unitunit legs and√2hypotenuse;sin/cosπ/4both1/√2.',SPECIAL,'diagram','Example:10')]
for n,page,label,note,d,rep,parent in refs:
 fig(n,page,label,note,[d],rep,[],parent);figures[-1].update(item_id=f'8227:TB:YM:C10:Teaching-figure:{n}',printed_page=pp(page),source_evidence=ev(page),value_level_scope_decisions=[],item_kind='teaching-figure',parent_item_id='8227:TB:YM:C10:'+parent if parent else None)
 figures[-1]['mathematical_feature_review']['method']='Readactualsourcequadrantbounds,ratio/anglelabelsandrequestedoutputletters. Independentlyderiveallmissingratiosfromoriginalsandsigns. Inspectproofcommon-domainholesandkeylabelswapsseparatelyfromcorrectfinalvalues.'
pages=[dict(pdf_page=page,printed_page=pp(page),chapter=10,page_status='items enumerated',item_ids=[r['item_id']for r in answers if r['source_pdf_page']==page]+[r['item_id']for r in figures if r['pdf_page']==page],continuation_item_ids=[],source_evidence=ev(page),reader='Codex author',date='2026-11-20',non_item_content='AllExamples7–10,Try7/Try8Q1–2/Try9/Try10and14reference/solutionpanelsenumerated. Try8Q2keyswapsa/bandhasnoc;originalsourceidentitiespreserved.',scope_screen='No-calculatorexactcompoundvalues/proofs. Originalquadrantsandfullidentitycommondomainsretained.')for page in range(456,460)]
def save():
 for name,data in [('answers-YM-C10-compound-cos-tan.json',dict(scope='Complete456–459cosine/tangentcompounds,quadrantsandidentitydomains.',items=answers)),('census-YM-C10-compound-cos-tan.json',dict(book='YM',book_id='8227-SRC-017',chapter=10,source_path=SRC,source_sha256=SHA,scope='Complete456–459page/item/figurecensus.',new_items=new+figures,corrections=corrections,pages=pages))]:
  (W/'tools/textbook-r5'/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
 for row in answers:
  for p in row['subparts']:
   if'operation'in p:assert equivalent(compute(p['operation']),expression(p.get('author_expected_normalised',p['printed_key_normalised']))),(row['item_id'],p['subpart'])
   for name,op in p.get('additional_operations',{}).items():assert equivalent(compute(op),expression(p['additional_operation_expected'][name])),(row['item_id'],p['subpart'],name)
 print(len(answers),'items;',sum(len(r['subparts'])for r in answers),'responses;',len(figures),'references;',len(pages),'pages')
if __name__=='__main__':save()
