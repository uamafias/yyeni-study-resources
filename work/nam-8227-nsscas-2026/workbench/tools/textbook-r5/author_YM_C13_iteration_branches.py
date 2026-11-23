"""YM566–567: reverse equations, positive target root and logarithmic iteration precision."""
import json
import author_YM_C13_iteration_examples as b
import author_YM_C13_opening as a
from author_YM_C13_opening import h,W,SRC,SHA,pp,ev,fig,figures,extra,compute,expression,equivalent,BRACKET,ROOTG
h.answers.clear();h.new.clear();h.corrections.clear();figures.clear();h.common.base.ev=ev
answers=h.answers;new=h.new;corrections=h.corrections
RELATE=b.RELATE;REARRANGE=b.REARRANGE;ITERATE=b.ITERATE;STOP=b.STOP

def add(kind,n,page,note,parts,rep='text'):
 r=a.add(kind,n,page,note,parts);r.update(representation=rep,mapping_rationale='Preservewhetheroriginalequationisgivenorderivedfrommap,thestipulatedversusopenstart,andwhichrootisspecifiedbyGIVENdiagram. Noall-rootscoveragefromfindingpositiveP. Sourcefull-precisionstatesandfinalprecisionaredifferentrequirements;wrongtableheaderisrecordedwithoutchangingthecorrectfinalanswer.',value_level_scope_decisions=[dict(rule_id='8227:LIMIT08',status='within',quoted_value=note,reason='Suppliedmaporprovidedrearrangement,explicitstoppingaccuracyandqualitativeconvergence. Noformalderivativecriterionrequired.')],scope_check=dict(status='in-scope',basis=note,excluded_or_qualified_parts=[],limits_considered=['8227:LIMIT08']),precision_angle_check=dict(source='Try4Q1/Q2root3dp,eachstate5dp;Try4Q3root2dp,each4dp;Example5root3dp,each5dp.',comparison='Unroundedinternalstates;checkoriginal/derivedequationandlasttworoundedstatesindependently. Example5tableheader2dpiswrong;question,displayparenthesesandfinalansweruse3dp.'))
 if rep=='graph':
  for p in parts:p['given_representation']='graph'
 return r
F='real_root(x**2+6,3)/2'
parts=b.sequence_parts('a',F,'1',['0.95647','0.95257','0.95222','0.95220'],5,653,'8*x**3-x**2-6',['Rational(9,10)','1'],'0.952',3,'Initialx1=1explicitlygiven;realcuberootmapalwayspositive.',equation_origin='Derived from supplied fixed point;part(b)asks the original polynomial.')
# Native key653 prints0.95222 for x4, but the source requests5dp.
# Independent full-precision x4=0.952228858... rounds0.95223.
wrong=next(p for p in parts if p['subpart']=='a-x4')
wrong.update(author_expected_normalised='Rational(95223,100000)',source_precision_note='Nativekeyx4.95222wrongatrequested5dp;correct.95223. Noellipsis/prefixinstruction. Finalroot.952at3dpunchanged.')
p=b.val('b-polynomial','expand((2*x)**3-(x**2+6))','8*x**3-x**2-6',653,[RELATE,REARRANGE],'Atfixedpoint,2x=realcuberoot(x²+6);cubingisbijectiveoverreals,giving8x³−x²−6=0. Nonzeroscalarmultiplesoftheequationarealsovalid;thebookcanonicalcoefficienttriple8,−1,−6isnotanexclusivelearnerformat.')
parts.append(p);add('Try-Now-4',1,566,'GIVENhalf-real-cuberootmap,start1:(a)each5dp,final3dp.952;(b)DERIVEpolynomial8x³−x²−6=0. Suppliedmaptoequationisdirectionofassessment;nooriginalpolynomialgiveninitially.',parts)
F='2+4/(x**2+2*x+4)'
parts=b.sequence_parts('a',F,'2',['2.33333','2.28346','2.29025','2.28932','2.28944'],5,653,'x**3-12',['2','Rational(7,3)'],'2.289',3,'Initialx1=2explicitlygiven;denominator(x+1)²+3>0forrealx.',equation_origin='Derived from supplied fixed point;part(b)asks equation and exact root.')
p=b.val('b-fixed-equation','expand((x-2)*(x**2+2*x+4)-4)','x**3-12',653,[RELATE,REARRANGE],'Atfixedpointmultiplybystrictlypositivedenominator(x+1)²+3. Expandto x³−12=0;nonewexcludedzeroornegative-rootbranchintroduced.')
q=b.val('b-exact-alpha','Tuple(*solveset(x**3-12,x,domain=S.Reals))[0]','real_root(12,3)',653,[RELATE],'DerivedequationhasoneREALrootcuberoot12. Checkitintheoriginalsuppliedmap;donotconfusethethreecomplexcubicrootswithrealα.');extra(q,'original-map-residual','simplify((x-(2+4/(x**2+2*x+4))).subs(x,real_root(12,3)))','0');q['depends_on_source_parts']=['b-fixed-equation']
parts.extend([p,q]);r=add('Try-Now-4',2,566,'GIVENalternativeF2+4/(x²+2x+4),start2:(a)each5dp,final3dp2.289;(b)DERIVEfixedpointequationandcuberoot12. SamefixedpointasExample4,differentmap/tracedomainandconvergencepattern.',parts);r['source_related_item_ids']=['8227:TB:YM:C13:Example:4']
original='x**4+2*x-9'
p=a.bracket('a-positive-P-bracket',original,'Rational(3,2)','Rational(8,5)','-Rational(15,16)','Rational(471,625)',653,'Originalpolynomialf1.5−.9375,f1.6+.7536. GIVENPisthePOSITIVEaxisintersection;do notreturnthenegativerootalsovisibleinthegraph.')
q=a.a.reasoning('b-provided-rearrangement','x=real cube root(9/x−2) for the indicated positive P.','OriginalP>0fromGIVENgraphand(a),soxnonzero. Dividex⁴+2x−9=0byxtoobtainx³=9/x−2;takeREALcuberoot,bijectiononthereals. Mapundefinedat0;preservepositive-targetcontextratherthanclaimingallstartsfindP.',654,'show/prove');q.update(assessed_8227_demand_ids=[REARRANGE,RELATE],component_demand_ids=[],given_representation='graph',response_format='proof/show-that',depends_on_source_parts=['a-positive-P-bracket']);extra(q,'original-nonzero-reconstruction','expand(x*(x**3+2-9/x))',original)
parts=[p,q]+b.sequence_parts('c','real_root(9/x-2,3)','Rational(31,20)',['1.5614','1.5556'],4,654,original,['Rational(3,2)','Rational(8,5)'],'1.56',2,'No start specified;bookkeyuses1.55insidegivenpositivebracket. Otherappropriatepositivechoicesarevalid.')
for p in parts[2:]:p.setdefault('depends_on_source_parts',[]).append('b-provided-rearrangement')
add('Try-Now-4',3,566,'GIVENquarticx⁴+2x−9andpositiveP:(a)verify1.5..1.6;(b)showprovidedrealcuberootmap9/x−2;(c)each4dp,root2dp1.56. No stipulatedstart;benchmark1.55notexclusive.',parts,'graph')
original='3*exp(x)-8+2*x'
p=a.sketch('a-one-root-pair',['3*exp(x)','8-2*x'],'Sameaxes:3e^xpositiveincreasing,through(0,3);line8−2xthrough(0,8),(4,0);exactlyONEintersectionin(.7,.8).','Choosepairfromoriginal3e^x=8−2x. Differencederivative3e^x+2>0,limitsnegative/positiveinfinity,soexactlyoneglobalroot. Appropriateaxesincludeinterceptsandcrossing;noformaliterationconvergencecriterionneeded.',567)
q=a.bracket('b-sign-bracket',original,'Rational(7,10)','Rational(4,5)','3*exp(Rational(7,10))-Rational(33,5)','3*exp(Rational(4,5))-Rational(32,5)',567,'Originalcontinuousf.7≈−.559andf.8≈+.277givesrootin(.7,.8),uniquefrom(a).');q['depends_on_source_parts']=['a-one-root-pair']
r=a.a.reasoning('c-provided-log-rearrangement','x=ln((8−2x)/3),withx<4.','Originalequationgives e^x=(8−2x)/3>0,hencex<4. Takingnatural loggivesthesuppliedform. Converselyexponentiatingthisreal-logformrecoverstheoriginalequation. Keepstrictpositiveargument;divisionby3isnonzero.',567,'show/prove');r.update(assessed_8227_demand_ids=[REARRANGE,RELATE],component_demand_ids=[],given_representation='text',response_format='proof/show-that',original_domain='x<4forrealiterationmap',depends_on_source_parts=['b-sign-bracket']);extra(r,'exponential-original-reconstruction','expand(3*(exp(x)-(8-2*x)/3))',original)
parts=[p,q,r]+b.sequence_parts('d','log((8-2*x)/3)','Rational(3,4)',['0.77319','0.76603','0.76825','0.76756'],5,567,original,['Rational(7,10)','Rational(4,5)'],'0.768',3,'No stipulatedstart;sourceworkingchooses0.75insidegivenbracket. Keeprealmapdomainx<4.')
for p in parts[3:]:
 p.setdefault('depends_on_source_parts',[]).append('c-provided-log-rearrangement')
 p['source_precision_header_anomaly']='Nativeworkingtableheaderincorrectlysayssamecorrectto2dp;question,three-decimalparenthesisedstatesandfinal.768require3dp.'
add('Example',5,567,'(a)ASKEDsuitablepairshowone3e^x=8−2xroot;(b).7..8bracket;(c)deriveprovidedlogmap,x<4;(d)each5dp,final3dp.768. Nativeworkingtable2dpheaderwrong;actualinstruction/final3dpretained.',parts)
refs=[(25,566,'Try4Q3 GIVEN quartic and positive target P','Originalx⁴+2x−9hasnegativeandpositiveaxisroots;Pexplicitlypositive. NoASKEDsketchresponse,onlyGIVENtargetgeometry.',[BRACKET],'graph','Try-Now-4:3',True),(26,567,'Example5 exponential ordinate table','3e^xat−6,0,1displayedapproximately.007,3,8.2;notexactequalities.',[ROOTG],'table','Example:5',False),(27,567,'Example5 linear ordinate table','Original8−2xat4and0gives0and8.',[ROOTG],'table','Example:5',False),(28,567,'Example5 SOLUTION one-intersection graph','Chosen3e^xand8−2xoneintersection;graphisananswer,notaGIVENdiagram.',[ROOTG],'graph','Example:5',False),(29,567,'Example5 sign-bracket working','Unroundedf.7negative,f.8positive;printed−.559,+.277are3sfdisplays.',[BRACKET],'table','Example:5',False),(30,567,'Example5 real-log rearrangement working','Originalequationforcespositive(8−2x)/3;realmapx<4.',[REARRANGE],'table','Example:5',False),(31,567,'Example5 iteration table with wrong precision header','Nativeheader2dpwrong:sourcequestionandfinal3dp. Full5dpstates.77319,.76603,.76825,.76756;lasttwoagreeat3dp.',[ITERATE,STOP],'table','Example:5',False)]
for n,page,label,note,ds,rep,parent,given in refs:
 fig(n,page,label,note,ds,rep,[],parent);figures[-1].update(item_id=f'8227:TB:YM:C13:Teaching-figure:{n}',printed_page=pp(page),source_evidence=ev(page),value_level_scope_decisions=[],item_kind='given-figure'if given else'teaching-figure',parent_item_id='8227:TB:YM:C13:'+parent)
 figures[-1]['mathematical_feature_review']['method']='Readactualmap,targetP,initial-valuepolicyandrequesteddisplay/finalprecision. Nativeheadercheckseparatestypofromcorrectsequence/finalanswer. Replayunroundedstatesandverifytheoriginal/derivedequationindependently. Givenquarticdiagramnotcountedasanaskedsketch.'
pages=[dict(pdf_page=page,printed_page=pp(page),chapter=13,page_status='items enumerated',item_ids=[r['item_id']for r in answers if r['source_pdf_page']==page]+[r['item_id']for r in figures if r['pdf_page']==page],continuation_item_ids=[],source_evidence=ev(page),reader='Codex author',date='2026-11-20',non_item_content='AllTry4Q1–3,Example5andactualGIVENquartic/solutiontables/graph/rearrangement/iterationpanelsenumerated. Everyexplicitlyrequestedcalculatedstatechecked;giveninitialvaluesnotinventedasseparatelyassessedanswers.',scope_screen='Suppliedmaps,providedrearrangementsandfixed-pointequationderivation;positivePtargetandlogdomainx<4kept. Formalconvergencecriterionnotrequired;tableheadertypodoesnotchangerequested3dp.')for page in range(566,568)]
def save():
 for row in answers:
  for p in row['subparts']:
   if'operation'in p:
    target=p.get('author_expected_normalised',p.get('printed_key_normalised',p.get('author_check_target_normalised')))
    assert equivalent(compute(p['operation']),expression(target)),(row['item_id'],p['subpart'])
   for name,op in p.get('additional_operations',{}).items():
    if name in p.get('additional_operation_expected',{}):assert equivalent(compute(op),expression(p['additional_operation_expected'][name])),(row['item_id'],p['subpart'],name)
 for name,data in [('answers-YM-C13-iteration-branches.json',dict(scope='Complete566–567reverse-equation/target/log-iterationresponses.',items=answers)),('census-YM-C13-iteration-branches.json',dict(book='YM',book_id='8227-SRC-017',chapter=13,source_path=SRC,source_sha256=SHA,scope='Complete566–567page/item/givenandsolutionpanelcensus.',new_items=new+figures,corrections=corrections,pages=pages))]:(W/'tools/textbook-r5'/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
 print(len(answers),'items;',sum(len(r['subparts'])for r in answers),'responses;',len(figures),'references;',len(pages),'pages')
if __name__=='__main__':save()
