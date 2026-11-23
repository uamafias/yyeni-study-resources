"""T5 implicit/parametric decisions and explicit-calculus application branches."""
import json
from pathlib import Path
W=Path(__file__).resolve().parents[2]
families=[];insights=[];extensions=[]
response_exclusions=[dict(item_id='8227:TB:Goldie:C4:Exercise-4E:8',part_labels=['iii'],
 rule_id='8227:LIMIT02',reason='This source part asks for all times without a finite interval. Its unbounded general trigonometric solution is explicitly outside8227;parts i/iiremain retained. Not a supporting recipe or in-scope variety branch.',
 applies_to='iii only',quoted_value='Find the values of t; no finite interval is supplied. Key t=0.6435+nπ.')]
def D(s):return '8227:2020:'+s
def A(n):return D('M2:T4:O03:D0'+str(n))
def M(b,k,ns,parts='*'):
 ch=4 if b=='Goldie' else 11
 return [dict(item_id=f'8227:TB:{b}:C{ch}:{k}:{n}',parts=parts,membership_reason='Explicit named source responses share the decision. Preserve the full connected item,original curve/parameter domain,source diagram roles,required method and singular-case notes.')for n in ns]
def G(k,ns,parts='*'):return M('Goldie',k,ns,parts)
def Y(k,ns,parts='*'):return M('YM',k,ns,parts)
def F(slug,title,decision,givens,constraints,rep,scaffold,methods,form,difficulty,distinction,ds,ms,pattern=None,exams=(),why=None):
 families.append(dict(family_id='8227:TEXTBOOK-FAMILY:'+slug,title=title,learner_decisions=decision,givens_and_unknowns=givens,
  constraints=constraints,representation_and_response=rep,scaffolding_and_connected_parts=scaffold,alternative_methods=methods,
  units_and_precision='Preserve exact coordinates,parameter ranges and original log/trig/root conditions. Radians for standard differentiation. Distinguish exact result,3sf,3dpand4sfand whether the task asks parameter,x-coordinate,wholepoint,ordinate or line form.',
  answer_form=form,difficulty_progression=difficulty,distinction_basis=distinction,assessed_demand_ids=ds,member_specs=ms,
  examination_relation=dict(kind='structural branch'if pattern else'textbook-only',pattern_ids=['8227:FAMILY:'+pattern]if pattern else[],part_ids=list(exams),
   evidence_label='examination-observed (NSSCAS 8227), comparative link only'if pattern else'textbook-derived',
   reason=why or 'Textbook-derived/supporting evidence. Complete matching examination structure has not been established;no award or frequency is inferred.')))

F('explicit-prescribed-gradient-points','Recover explicit-curve inputs or points for a prescribed nonzero gradient',
 'Set the derived gradient equal to the stated value,filter original domains and recover ordinates only when asked.',
 'Explicit curve and nonzero target gradient;unknown abscissas or complete coordinates.',
 'Original radical endpoints/poles excluded;two valid gradient positions may remain. This is not a stationary-point request merely because an equation is solved.',
 'Explicit formula to xsetorpairedpoints.',
 'A general derivative may be working rather than an additional output.',
 'Explicit differentiation,exact solving and original curve evaluation.',
 'Requested xvalues ORwholepoints,with exact/rounded form as specified.',
 'YMTry4Q5asks gradient-5;Try9Q2asksCOORDINATESbutitskeyonlyx;Revision11Q2repeats the source with a complete key. Goldie4C7requires both boundedgradient4positions.',
 'Target/output differences require distinct branches;explicit geometry is not implicit/parametric demandA3.',[D('M1:T8:O01:D01')],
 Y('Try-Now-4',[5])+Y('Try-Now-9',[2])+Y('Revision-Exercise-11',[2])+G('Exercise-4C',[7]))
F('explicit-tangent-incidence-parameter','Recover a tangent point from a further incidence condition',
 'Form the tangent at an unknown input and impose its passage through the specified point without dividing away exceptional parameter cases.',
 'Explicit curve,tangentpointabscissapandoriginincidence;unknownp.',
 'The line passes through both curvepointandorigin;checkp=0before any division byp.',
 'Curve/incidence condition to exact parameter.',
 'The tangent is an intermediate model;final requestedpnot an arbitrary tangent equation.',
 'Derivative and point-gradient tangent with incidence;original substitution verifiesp.',
 'All admissiblepvalues.',
 'YM41hasf=(4-x)e^xandorigincondition;correctp2requires preserving constants.',
 'Choosing an unknown point by tangent incidence is stronger than line construction at a given point.',[D('M1:T8:O03:D01')],Y('Example',[41]))
F('explicit-stationary-bounded-trig','Find all stationary targets of a bounded trigonometric curve',
 'Differentiate,solve the full boundedtrig equation and retain each original-domain solution and required classification/coordinate.',
 'Explicit trig/elementarycurve and finite interval;unknown stationary xvalues/points and sometimes nature.',
 'Complete interval solutions,not principalinverse only;original poles split domain. Sourceone-pointpremise can be false and remains a defect.',
 'Formula/given graph to complete bounded stationary set.',
 'Shown derivative or prescribedR-form can scaffold solving;do not omit the requiredrepresentation when it is credited.',
 'Standard/product/quotient/chain differentiation plus bounded trig solving and nature test where asked.',
 'All and only original-domain stationary outputs,with requested precision.',
 'Goldie4C10has two boundedpoints;YMTry23wrongly claims one whileπ/12and5π/12bothwork. YMExercise11Q10requiresRcos(2x+α)and4sfrootswithcycle shift.',
 'A bounded multibranch solve and requiredR-form are substantive,not just harder numbers.',[D('M1:T8:O04:D01')],
 G('Exercise-4C',[10,12,13])+Y('Example',[22,23])+Y('Try-Now-22',[1,2,3])+Y('Try-Now',[23])+Y('Exercise-11',[3],['b-stationary-M-coordinates'])+Y('Exercise-11',[10]),
 'stationary-points',['8227:EXAM:2024:P2:Q10:a','8227:EXAM:2024:P2:Q10:b'],
 'Observed stationary elementarycalculus supplies a comparison;boundedbranches,coordinates,nature and prescribedR-form differ by source.')
F('explicit-second-derivative-zero','Locate a point where the second derivative is zero',
 'Compute the second derivative,solve itszero condition and recover the ORIGINALcurvepoint without asserting the point is stationary.',
 'Explicit exponentialproductcurve;unknown point satisfyingf″=0.',
 'f″=0doesnotimplyf′=0or establishinflexionwithoutfurther curvatureevidence. No unaskednatureclassification.',
 'Explicit formula to exact coordinate point.',
 'The first derivative is working,not an extra responseunlessasked.',
 'Twice differentiation,exact root and originalordinateevaluation.',
 'Exact requested point,not merelyx.',
 'Goldie4B10andYMTry42Q2bothusexe^(-x/2);atx4thefirstderivativeisnonzero.',
 'The condition targets curvature derivativezero,not a stationary point of the originalcurve.',[],G('Exercise-4B',[10])+Y('Try-Now-42',[2]))
F('implicit-dependent-expression','Differentiate expressions involving a dependent variable',
 'Treatyasy(x),attachdy/dxto dependent factors and useproduct/chainrules without prematurely solving an absent curve equation.',
 'Individual expressions iny,xorboth;unknown formal derivative carryingdy/dx.',
 'Natural-log/trig domains;both terms forxyproducts. No fullF(x,y)=0curve is supplied in these building-block exercises.',
 'Dependent-variableexpression to formal derivative.',
 'These are scaffolds for the later implicitcurve tasks,not complete geometric applications.',
 'Product/chain rules with explicit dependent-variable notation.',
 'Every formal derivative with correctdy/dxfactors.',
 'Goldie15and4D1progress fromy4through mixedexponential/log/trigproducts.',
 'Expression-level differentiation is different evidence from isolatingdy/dxfor a completecurve.',[],G('Example',[15])+G('Exercise-4D',[1]))
F('implicit-curve-derivative','Derive the regular slope of an implicit curve',
 'Differentiate the ORIGINALcurve relation,collectalldy/dxtermsand isolate the finite slope only where the implicit denominator is nonzero.',
 'F(x,y)=0withpolynomial,log,exponentialortrigterms;unknown derivative expression.',
 'Originalcurve/log domains andFy≠0for a finiteratio. A zero denominator may indicateverticaltangent or a singularpoint,not zero slope.',
 'Implicit equation to slope expression inx,y.',
 'No geometricpoint/nature task is invented where only the derivative is asked.',
 'Implicit product/chainrule;valid explicit rearrangement/log solving if unconstrained and branch/domain preserved.',
 'Equivalent regular derivative with original conditions.',
 'YM27sin(xy)=xneedsbothchain/product;28has strictlypositive denominator2+3e^xy². YM16(c)canbesolvedexplicitlybefore differentiation butisnotageometricapplication.',
 'Implicitrepresentation,not the sophistication of an explicit quotient,defines this demand.',[A(1)],
 Y('Example',[24,25,26,27,28])+Y('Try-Now',[24,25,26,27,28])+Y('Example',[16],['c'])+Y('Try-Now',[16],['c']),
 'implicit',['8227:EXAM:2021:P2:Q10:a','8227:EXAM:2023:P2:Q8:a'],
 'The observed implicit-slope calculation anchors comparison;particular nestedlogs/trig and regularityconditions remain textbook branches.')
F('implicit-point-gradient-line','Apply an implicit derivative at a verified point or slope condition',
 'Verify originalincidenceandregularity,evaluate the derivative and construct the requestedtangent/normal or recover all prescribed-gradientpoints.',
 'Implicitcurve pluspoint,gradientorunknownconstantconditions;unknown slope,line,pointsorparameters.',
 'Fy≠0forfinitegradient;horizontal tangentnormalmay bevertical. Originalpositivelogargumentsmustholdbefore using the formula.',
 'Curve/pointcondition to scalar slope,lineor exactpointset.',
 'Preserve derivative→hencepointline and suppliedparameterconstraints;requestedintegerlineform matters.',
 'Implicit differentiation then coordinategeometry;explicitbranchalternative if valid and not method-prohibited.',
 'All asked slopes,lines,parameters and points in source-requestedform.',
 'Goldie16verifies(1,1);4D9recoversk,cfrompointandslope;YM31(a)/Try31Q2requestintegerlineforms;Try29Q4asksbothgradient-1points.',
 'Geometric use is additional to a derivative formula,with its own sourcepartlink.',[A(1),A(3)],
 G('Example',[16])+G('Exercise-4D',[2,3,4,9,11])+Y('Example',[29])+Y('Try-Now-29',[1,2,3,4])+Y('Example',[31],['a-tangent'])+Y('Try-Now-31',[2])+Y('Exercise-11',[6,7]),
 'implicit',['8227:EXAM:2021:P2:Q10:a','8227:EXAM:2021:P2:Q10:b','8227:EXAM:2023:P2:Q8:b'],
 'The examination slope-to-line chain is observed. Textbook parameter/slope-set and specifiedlineform branches add distinct givens/outputs.')
F('implicit-horizontal-and-singular','Locate implicit horizontal tangents and distinguish singular candidates',
 'Solve the originalcurve together withhorizontalnumeratorzero,then test the implicitdenominatorandseparate any singularbranchanalysis.',
 'Implicitcurve,possibly parameterised or accompaniedbygraph;unknown horizontalpoints,uniqueness,natureornonexistence.',
 'A0/0ratio isnotautomaticallya stationarypoint. Keepnonzeroparameterassumptions and check alloriginalequations;nonexistence needs a contradiction argument.',
 'Implicit equation/given graph to exactpoints/proof.',
 'Shownsloperelation andhence coordinates remain connected;additional graph/natureoutputs retained onlywhen asked.',
 'Implicit differentiation and joint equations;localbranch/curvatureanalysis for explicitly singularpoints rather than cancellation.',
 'Allregularhorizontalpoints and explicit singular/nonexistence qualification,with source-requiredproof.',
 'Goldie17’soriginneeds singularbranchqualification;18uses fourpointgradientchecks toclassifytwohorizontalpoints;YM31(b)/Try31Q1prove none. Goldie4D12requiresa≠0.',
 'Originalcurveandregularityare additional evidence beyondzeroingthe derivative numerator.',[A(1),A(3)],
 G('Example',[17,18])+G('Exercise-4D',[5,8,10,12])+Y('Example',[30])+Y('Try-Now',[30])+Y('Example',[31],['b-no-stationary-point'])+Y('Try-Now-31',[1])+Y('Revision-Exercise-11',[4]),
 'implicit',['8227:EXAM:2025:P2:Q5:answer'],
 'The observed implicit geometric demand provides comparison;singularorigin,parameteruniquenessandno-horizontalproofs are extra textbook branches.')
F('implicit-linked-normal-curve-sketch','Use an implicit normal to recover a second intersection and curve features',
 'Construct the actualnormal,reintersect itwiththeoriginalcurve excludingthecontactpoint,andderiveasymptotes/sketchfroman equivalentbranchform.',
 'Implicitrectangularhyperbolaandcontactpoint;unknown derivative,normal,secondintersection,asymptotesand sketch.',
 'Original denominator/polepreserved;thecontactpointisnot the requestedsecondintersection. Equivalentexplicitformmusthave samecurve.',
 'Implicit equation to connected lines,points,asymptotesand originalgraph.',
 'Allsourcei–ivremainconnected;thecurveplotis a requiredresponse rather than assumedgiven.',
 'Implicit/explicit slope,normal line,simultaneous solving and translatedreciprocalgraph.',
 'Every askedintermediate and finalgraphfeature.',
 'Goldie4D6uses(x-6)(y+4)=2andnormalat(7,-2).',
 'Secondintersectionandasymptote/sketchevidence broaden the implicitline task.',[A(1),A(3)],G('Exercise-4D',[6]),
 'implicit',['8227:EXAM:2021:P2:Q10:b'],
 'The exam normal/tangentapplication is related;the later reintersectionandcurveinvestigationare explicittextbook extensions.')
F('variable-exponent-log-differentiation','Differentiate a variable-exponent curve using the required logarithmic route',
 'Takebaseelnof theoriginalpositivecurve,differentiatethe resultingimplicitrelationandrestoretheoriginalybefore stationaryanalysis/sketch.',
 'y=x^xwithx>0andexplicitlogmethod;unknownlogrelation,derivative,stationarycoordinatesandsketch.',
 'Variableexponent isnotaconstant-powerderivative. Originalpositivexdomainandrequested3dpcoordinatesremain.',
 'Explicitvariable-exponentformula tologworking,derivative,pointandgraph.',
 'Keepmethod→differentiate→stationary→sketchsequence;noautomaticformal-log-diffrequirementforotherfree-methodsources.',
 'Source-requirednaturallogsandimplicit differentiation;exponentialrewrite checks answer.',
 'Complete requestedmethodandgraph/coordinateevidence.',
 'Goldie4D7makes thelogrouteexplicit and asks bothcoordinates3dp.',
 'Requiredlogarithmicmethodandvariableexponentdifferfrom an ordinaryx^nrationalpower task.',[A(1)],G('Exercise-4D',[7]))
F('parametric-point-plot-support','Explore supplied parametric positions and their plotted branches',
 'Evaluate the suppliedcoordinatepairusingONEparameter,plot the correctbranchandinterpret the actualdomain/projectionwithout inventingderivatives.',
 'Suppliedrideorparameterpairandsamplevalues;unknownpositions,plot,domainobservationor elimination.',
 'Parameterdomainmay extendbeyondsamples;theprojectionconstraintaskedneednotbe a completerange. Rideangles indegreesarepositionevaluations,notstandardradian derivativeformulae.',
 'Givenparameterformulas tocoordinate tables,plotsor explicitrelation.',
 'Supportonlywhere nodifferentiationrequest;keep sourceillustrationversusposedplot distinction.',
 'Directsubstitution,coordinateplotandvalidelimination.',
 'Allrequestedpoints/plot/observation,notunasked slope.',
 'Goldie19hasseparatet≠0branches;20tabulates-2..2;21asksxintermsofy. Theheadinglessride suppliespositionformulasbutnoderivative.',
 'Aparametricrepresentationdoesnotbyitselfdirectlyassess parametric differentiation.',[],G('Worked-illustration',[1])+G('Example',[19,20,21]))
F('parametric-regular-derivative','Derive a parametric slope and preserve regular/singular parameter distinctions',
 'Differentiatebothcoordinatefunctionswithrespecttothesameparameterandformthe ratio onlyonthecorrectregularbranch.',
 'x=X(t),y=Y(t)withdomain;unknown dy/dxinparameterformorproven targetform.',
 'X′≠0forfiniteratio;X′=Y′=0needsseparatebranchanalysis. Originalpoles/log/rootrestrictions remainaftercancellation.',
 'Parameterpair toexactgradientexpression.',
 'Specifiedshow-thatformmayrequiresimplification;itmustnotextendthesourcecurveoverexcludedparameters.',
 'Parametricchainratio,standard/product/quotientrulesandvalididentities;Cartesianeliminationcancheckstalledcases.',
 'Equivalentregularslope,source-requestedformandexplicitsingularqualification.',
 'YM32hascuspt0;Try32(a)stallsbuttheCartesianlinehasslope-5;Goldie4E14hasacuspwherecancellationisnotafiniteslope. YM35retainsoriginaltanpolesdespitefinalsinθ.',
 'Parametricrepresentationandregularityaredirectlyassessed;explicitquotientderivativesarenotthisdemand.',[A(2)],
 G('Exercise-4E',[1,5,10,12,14])+Y('Example',[32,33,34,35,36])+Y('Try-Now',[32,33,34,35])+Y('Try-Now-36',[1,2])+Y('Exercise-11',[8],['a-shown-derivative'])+Y('Example',[40],['a-shown-derivative'])+Y('Try-Now-40',[1],['a-shown-derivative'])+Y('Try-Now-40',[2],['a-shown-derivative'])+Y('Try-Now',[41],['a-shown-linear-derivative']),
 'parametric',['8227:EXAM:2022:P2:Q10:a','8227:EXAM:2024:P2:Q7:c'],
 'Observedparametricslopechainsanchorcomparison;stalled/cuspparametersandprescribedidentitysimplificationsareadditionalbranches.')
F('parametric-general-tangent-normal','Derive tangent/normal relations at a general parameter',
 'Combineparametricslopewiththecorrespondingpointandformageneralline,thenapplysourceaxisinterceptorconstantgeometryconditions.',
 'Parameterpairandpossiblyscaleconstant;unknowngeneraltangent/normal,interceptsandconstantlength/area.',
 'Nonzeroscaleconditionsmustbesupplied;generalimplicitlinecanincludeverticalcaseexcludedfroma slopequotient. Unsignedareaneedsabsoluteproduct,not2abwithoutsignassumption.',
 'Parametricformulas tolineequationsandgeometricidentities.',
 'Allgeneral→specialpoint→sketch/geometrypartsremainone sourcechain.',
 'Ratio derivativeandpoint-lineform,orparametricdirectionvectorlinevalidatverticaltangents;coordinategeometryforintercepts.',
 'Source-requestedgenerallines,intercepts,constantrelationandsketchonlywhereasked.',
 'Goldie22’sgeneraltangentincludesverticalvertex;4E4omitsa≠0/t≠0;4E6unsignedarea2|ab|;4E15’spositivea/openquadrantareessential.',
 'Generalparameterequationsandconstant-geometricproofarestrongerevidencethana numericlineatgiven t.',[A(2),A(3)],G('Example',[22,23])+G('Exercise-4E',[4,6,7,15]),
 'parametric',['8227:EXAM:2021:P2:Q7:answer'],
 'Theexamasksaparametricgeometricapplication;generalinterceptlociandconstantlength/areaproofsaretextbookbranches beyondthatfixedline.')
F('parametric-fixed-parameter-line','Construct a parametric tangent/normal at a stated parameter',
 'Evaluatethecurvepointandregulargradientatthesamegivenparameter,thenchoosetangentornormalandthespecifiedlineform.',
 'Parameterpairandgiven t/θ;unknownpointgradientandline.',
 'Originalparameterdomainandnonzerodirections;normalreciprocalcanrequireverticalform. Pointincidencealonemissesthewrongslopesourceerror.',
 'Parameterformulas tocompleteexactline.',
 'Givenparameterdoesnotasktosearchforanothercurvepoint;retainexplicitrequestedderivativebeforelineifasked.',
 'Parametricslopeandpoint-gradientline,orequivalentdirectionvectorline.',
 'Everyaskedgradient/line/interceptwithrequestedprecision/form.',
 'Goldie4E2usesθπ/6;YM39Q2’swrongkeylinepassesthroughcorrectpointbut slope1/8iswrongversus3/4. Someintegerlineformsareexplicitlyrequested.',
 'Fixedparameterevaluationisdifferentfromfindingtheparameterbyanaxis/slopecondition.',[A(2),A(3)],
 G('Exercise-4E',[2,3])+G('Exercise-4E',[8],['i','ii'])+Y('Try-Now-37',[2],['a-shown-derivative','b-tangent'])+Y('Try-Now-39',[2,3,4])+Y('Exercise-11',[9]),
 'parametric',['8227:EXAM:2021:P2:Q7:answer'],
 'Theobservedfixedparametriclineprovidescomparison;sourcegivenparameter,lineformandlaterinterceptoutputsremainbranchspecific.')
F('parametric-geometric-point-selection','Select a parametric point by an axis or supplied line condition',
 'FindtheparametercorrespondingtotheACTUALlabelledpositiveaxisinterceptor given normal,thenconstructtherequiredline/gradient.',
 'Parametriccurve,givenellipse/graphorlinecondition;unknownselectedpointandline/gradient.',
 'Positiveaxisdistinguishesoppositepoints;duplicateendpointparametersdonotmakeduplicatepoints. LabelBselectstheactualx-axisintercept,notanyintersection.',
 'Givenparametricgraph/formulastoidentifiedpointandline/gradient.',
 'Keeporiginalshownslopethenpointselectionandline;donotturnselectedpointintounauthorisedextra given.',
 'Coordinateconditionandparameterdomain,thenratio slopeandline;exactCartesianrelationascheck.',
 'Theuniquelyrequestedpoint/lineorgradient,withcorrectlabel/sign.',
 'YM39usespositivey-axis;Try39Q1asksitsnormal;40(c)askslabelledBgradient;Try40Q1(c)preservesP/Qsigns. Try41findsPfromaGIVENnormal.',
 'Inferringwhichparameterpointisintendedisextraevidencebeyondsubstitutingasuppliedt.',[A(2),A(3)],
 Y('Example',[39])+Y('Try-Now-39',[1])+Y('Example',[40],['c-gradient-at-B'])+Y('Try-Now-40',[1],['c-P-Q-gradients'])+Y('Try-Now-40',[2],['c-normal-gradient-at-x-two'])+Y('Try-Now',[41],['b-normal-point-P']))
F('parametric-prescribed-gradient','Recover parameters or coordinates from a parametric gradient condition',
 'Solve the regularslopetargeton theoriginalparameterdomain,andreturnthetargetquantityactuallyasked ratherthananintermediatet.',
 'Parametriccurveandnonzero targetgradient;unknownparameterorwholecoordinatepoint.',
 'Logdomainandstrictangleboundsfilteralgebraicroots. Avalidtvalueisnot acompletepointanswerwhenbothcoordinatesareasked.',
 'Parameterpair/gradientcondition toparameterorpointset.',
 'Shownslopeprecedestheinversegradient solvewhereasked;retainthatdependency.',
 'Parametricratio,exactexponential/trig/algebraicsolveandoriginalpointcheck.',
 'AlladmittedrequestedparametersORcoordinates,withsourceprecision.',
 'Goldie4E11/13askdifferenttargets;YMTry38Q1keyonlygivest2butaskscoordinates(6,5);Try38Q2needsactualclosed0..πbranch.',
 'Inversegradientrecoverychanges thelearnerdecisionfromdirectslopecalculation.',[A(2),A(3)],G('Exercise-4E',[11,13])+Y('Example',[38])+Y('Try-Now-38',[1,2]))
F('parametric-horizontal-vertical-stationary','Find parametric horizontal/vertical targets and justify nature on the curve',
 'DistinguishY′zero(horizontal),X′zero(vertical)andbothzero(singular),thenlocate/classifytheactualCartesianpointusingorientation-aware reasoning.',
 'Parametriccurveanddomainwithpossiblegivengraph;unknownhorizontal/verticalparameters,points,natureornonexistence.',
 'Checkothercoordinatevelocitynonzero;originaldomainrejectsfalsecandidates. ParameterrunningbackwardschangesCartesiansecond-derivativeinterpretation.',
 'Parametricformulagraphtoparameters,pointsandgeometricclassification/proof.',
 'RespectasksforonlyY,x,t,wholepointoradditionalnature;givenminimumnatureneednotbereprovedunlessasked.',
 'Ratioandregularitytests,orientation-awarederivativesigns,d²y/dx²wherevalid,orequivalentCartesianbound.',
 'Everyrequestedregulargeometrictarget,singularqualificationandvalidnatureproof.',
 'YMTry42Q1keyhaswrongMAXandmissingcoordinates;correct(2,-1)MIN. Goldie24hasmonotoneX(t);YM37requiresverticalsinθ3/8andnonzeroY′;Try37Q1provesnoverticaltangentfrompositiveX′.',
 'Stationarity/verticalityandparameterorientationareextraevidencebeyondaratioformula.',[A(2),A(3)],
 G('Example',[24])+G('Exercise-4E',[9])+Y('Example',[37,42])+Y('Try-Now-37',[1])+Y('Try-Now-37',[2],['c-horizontal-coordinates'])+Y('Example',[40],['b-stationary-A-C-parameters'])+Y('Try-Now-40',[1],['b-minimum-M'])+Y('Try-Now-40',[2],['b-minimum-coordinates'])+Y('Try-Now-42',[1])+Y('Exercise-11',[8],['b-stationary-coordinates'])+Y('Revision-Exercise-11',[5]),
 'parametric',['8227:EXAM:2022:P2:Q10:b'],
 'Observedparametricgeometricconditionsanchorcomparison;verticality,singularcasesandnatureorientationareexplicittextbookbranches,notallpresentinoneexampart.')

def X(family_id,reason,ms):extensions.append(dict(family_id='8227:TEXTBOOK-FAMILY:'+family_id,reason=reason,member_specs=ms))
X('gradient-point-evaluation','Elementary-functioninstances preserve scalargradient target;thefunctionclass adds derivative-method/domaincomponents,not implicit/parametricapplication.',
 G('Exercise-4C',[9])+G('Exercise-4C',[6],['ii'])+Y('Try-Now-4',[2,3])+Y('Try-Now-5',[3])+Y('Try-Now-9',[3])+Y('Try-Now-12',[3])+Y('Try-Now-17',[2])+Y('Try-Now-21',[1,2])+Y('Exercise-11',[5],['a-gradient-at-P']))
X('tangent-normal-at-point','Explicitcurveelementaryderivativebranches:requiredline atknownpoint,not implicit/parametric demand. Normalincidenceproof remains a named connected branch.',
 G('Exercise-4A',[2],['ii','iii','iv'])+G('Exercise-4A',[4],['ii','iii'])+G('Exercise-4B',[12])+G('Exercise-4C',[6],['iii','iv'])+G('Exercise-4C',[8,11])+Y('Example',[5,21])+Y('Try-Now-5',[1,2])+Y('Try-Now-9',[4,5])+Y('Try-Now-13',[4])+Y('Try-Now-21',[3])+Y('Exercise-11',[3],['a-origin-tangent'])+Y('Exercise-11',[4]))
X('tangent-normal-linked-geometry','Goldie4A5is a long EXPLICITroot-quotientcurve investigation with normal reintersections andtrianglearea. Preserve its model and allstage outputs;do notmis-tag asimplicit.',G('Exercise-4A',[5]))
X('stationary-classify-sketch','Goldieexplicit product/rational/e/lncurvesaddaskedgraphs;4A4has an empty stationaryset that must be justified. Whole source chains remain connected.',
 G('Exercise-4A',[3])+G('Exercise-4A',[4],['i','iv-no-stationary','iv-sketch'])+G('Exercise-4B',[6,9]))
X('stationary-analytic-targets','Explicitnontrigonometriccurveinstances retain requested abscissa-versus-coordinate/nature outputs;noneinherits implicit/parametric demand fromcomplexity.',
 G('Exercise-4A',[6,7])+G('Exercise-4B',[4,5,7,8,11])+Y('Example',[4,9,13,17])+Y('Try-Now-4',[1,4])+Y('Try-Now-9',[1])+Y('Try-Now-13',[1,2,3])+Y('Try-Now-17',[1])+Y('Exercise-11',[2])+Y('Exercise-11',[5],['b-minimum-coordinates'])+Y('Revision-Exercise-11',[3]))
X('direct-time-rate','Goldieriverheightmodel uses e^xandexplicit0..3hforecast;derivativeandfourratesareasked,not aninfiniteunqualifiedforecast.',G('Exercise-4B',[3]))
X('power-sum-differentiation','YMC11recoveredboxed y=x²primer remains explicitpowerpractice despite placement inimplicitexposition.',Y('Worked-illustration',[1]))
X('function-validity','Goldie4Prompt3asks thevertical-line/single-valuedtestonagivenmultibranchcurve,notone-to-oneinverseclassification.',G('Prompt',[3]))
F('same-gradient-curve-translation-support','Explain equal gradients on the common logarithm domain',
 'Use a constantverticaldifference toexplainwhythetwo curves share gradients,andstatewhere thatidentityisvalid.',
 'ln(3x)andlnxwiththeirsamedervative;unknownshape relationanddomain.',
 'Commonpositivexdomain;logidentitydoesnotextend to negativex.',
 'Functioncomparison toshortexplanation/domain.',
 'Noexponential/log equation isasked;thederivativesaregivencontext.',
 'ln(3x)=ln3+lnxandconstanttranslation.',
 'Verticaltranslationln3andx>0.',
 'GoldiePrompt2directsattention togeometryratherthanrecomputingacalculusformula.',
 'Supportingfunctionalinterpretation,notanewdirectderivativedemand.',[],G('Prompt',[2]))
F('explicit-root-arc-investigation','Use a supplied positive arc to connect derivative,maximum and endpoint slope',
 'Recoverthepositiveintercept,differentiatethesuppliedinnerrootthenproduct,andinterpretmaximum/origin/endpointgradientsontheACTUALarc.',
 'Givenpositivearc ofx√(9-2x²)on0..a;unknowna,derivative,maximumxandgradientfeatures.',
 'ThefullformulahasalargersymmetricdomainthantheGIVENpositivearc;endpointgradientisnonfinite,nottheformula’sfalselycancelledvalue.',
 'Givenarc toexactalgebra,maximumandgradientinterpretations.',
 'Keepinnerderivative→henceproduct andtheexplicitlyaskedorigin/endpointinterpretation.',
 'Chain/productrules,stationaryequationandone-sidedendpointanalysis.',
 'Allsixsourceoutputswithcorrectarc/endpointconditions.',
 'Goldie4A8asks acompleteconnectedcurveinvestigationwithpositivearcdata.',
 'Arc selection and endpointinterpretation areadditionallearnerdecisionsbeyond a productderivative.',[D('M2:T4:O02:D01'),D('M1:T8:O04:D01')],G('Exercise-4A',[8]))

def I(slug,title,ds,teaching,exam,difficulty,pitfalls,gaps,proposals,items,parts,grades):
 insights.append(dict(insight_id='8227:TEXTBOOK-INSIGHT:'+slug,title=title,demand_ids=ds,teaching_comparison=teaching,
  examination_comparison=exam,difficulty_and_grade_bounds=difficulty,pitfalls=pitfalls,gaps_and_representations=gaps,
  implications_for_step3=proposals,evidence_item_ids=items,examination_part_ids=parts,grade_descriptor_ids=grades,marking_rule_ids=[],examiner_error_ids=[]))
def S(b,k,n):return f'8227:TB:{b}:C{4 if b=="Goldie" else 11}:{k}:{n}'
I('implicit-curves-and-regularity','Implicit differentiation,regular slopes and original-curve geometry',[A(1)],
 'Goldie explicitly differentiatesdependent-ybuildingblocks before completeimplicitcurves andgivenpoint/geometrictasks. YMseparates polynomial,log,trigandexponentialrelations,thenpointgradients,horizontalpoints andlines. Some relations can be rearranged explicitly first;that validalternative is retained where not prohibited. Mere placement ofy=x²primerinimplicitexposition doesnotmake it an implicitproblem.',
 'NSSCAS2021P2Q10and2023P2Q8linkimplicitderivatives tolines;2025P2Q5adds geometricapplication. A derivativeformulaalone andits useatpointmustretainseparatepartlinks. An explicitcurve quotient orstationarypointdoesnotinheritM2T4O03D03justbecauseitsalgebraishard.',
 'A14explicitlynames finding/using implicitderivatives;C13/E13supply standardandproduct/quotientfoundations. The difficultboundary isregularity,not coefficient size:theimplicitdenominatorcanvanish,and0/0needsbranchanalysis. Formalfirst-principlesproofremainsoutside requiredscope.',
 'Goldie17’sorigin is singular andneeds a qualification;YM27’sx0componentmustnot beassigned afiniteratio. Splittingln(xy)into ln x+lnycanlose the negative-negativebranch;implicitproducttermsneedboth contributions. These are registeredsource/author cautions,no examiner-frequencyclaims.',
 'Bothbooks supply routine andelementaryimplicitcurves. Goldie adds generalparameteruniqueness andlogarithmicvariable-exponentwork;YM explicitgivenpointchecks make regularity inspectable. Optionalx^xlogroute doesnotturn allvariable-powerexpressions into constantpowerrules.',
 'Propose keepingF,itsdomain andpartialderivatives in the source-to-solution evidence,verifying pointincidence before slope,androutingFy=0/Fx=0cases to explicitbranchanalysis. Preserve source-enforcedmethod andrequestedlineform;do not upgrade every implicitformula to a fullgeometrictask.',
 [S('Goldie','Example',15),S('Goldie','Example',17),S('Goldie','Exercise-4D',7),S('Goldie','Exercise-4D',12),S('YM','Worked-illustration',1),S('YM','Example',27),S('YM','Try-Now',26)],
 ['8227:EXAM:2021:P2:Q10:a','8227:EXAM:2021:P2:Q10:b','8227:EXAM:2023:P2:Q8:a','8227:EXAM:2023:P2:Q8:b','8227:EXAM:2025:P2:Q5:answer'],['8227:GRADE:E:13','8227:GRADE:C:13','8227:GRADE:A:14'])
I('parametric-curves-geometry','Parametric differentiation and geometric use of implicit/parametric slopes',[A(2),A(3)],
 'Goldie introduces parametricpositiontables/plots andelimination before ratio derivatives,generaltangents/normals andconstantgeometryproofs. YM focuses on explicitparameterdomains,shownslopeforms,fixed/inferredpointlines,horizontal/verticalconditions andnature. Bothbooks have sourceswhere the finaltargetis t,x,Y,wholecoordinatesorline;thesearepreserved rather than acceptingoneintermediate for everyquestion.',
 'NSSCAS2021P2Q7and2022P2Q10observe parametricline/slope/geometricconditions;2024P2Q7(c)adds aparametricslopeapplication. The2024source diagramdefectremains recorded;itcannotdefine newgeometry. Graph-reading and branchselection are additional to thelastdy/dxcalculation. Explicitcurveapplications remainoutsideA3evenwhen theyuse product/quotientcalculus.',
 'A14includesparametric/implicitderivativeuse;C13suppliesrulefoundation. Harderbranches involveX′=0versusY′=0,both-zero stalls/cusps,parameterorientation andoriginalangle/logdomains. Generalintercepts require nonzeroscale assumptions and unsignedareacorrectness. No grade-specificparameterdomains are decided here.',
 'YMTry39Q2’swronglinehascorrectincidencebutwrongslope;Try42Q1missescoordinatesandcalls aminimumamaximumafter omittinganX-chainfactor. Goldie4E6prints2abwithouttheunsignedabsolutevaluequalification;4E4omitsa≠0. Somealgebraicallycancelledstationaryparametersarecusps rather than regularhorizontalpoints.',
 'Goldie offers moregeneralparameterline/interceptproofs,YM moregivenellipse-label/fixedprecisiontargets. Aplottedparametricpathwithoutanyderivativeaskis supportingrepresentationpractice,not directderivativecoverage. Negativeparameterneednotmeaninvalidnegativetimewhen tissimplyarealparameter.',
 'Propose literalparameterdomains,coordinatevelocityregularitychecks andindependentCartesian/nearbybranchverificationforsingularcases. Retainaxis-sign/pointlabels,askedoutputquantity andexactprecision. Futurediagram assets andmarkingmustderivepointlabels fromthesameparametricmodel;branchcriteriaandruntimegenerationwaitforstep3.',
 [S('Goldie','Example',19),S('Goldie','Example',22),S('Goldie','Exercise-4E',4),S('Goldie','Exercise-4E',6),S('Goldie','Exercise-4E',14),S('YM','Example',32),S('YM','Try-Now',32),S('YM','Try-Now-39',2),S('YM','Try-Now-42',1)],
 ['8227:EXAM:2021:P2:Q7:answer','8227:EXAM:2022:P2:Q10:a','8227:EXAM:2022:P2:Q10:b','8227:EXAM:2024:P2:Q7:c'],['8227:GRADE:C:13','8227:GRADE:A:14'])

if __name__=='__main__':
 target=W/'tools/textbook-r5/synthesis-implicit-param.json'
 target.write_text(json.dumps(dict(authorship='Codex author; independent review pending',scope='GoldieC4/YMC11implicit/parametricfamiliesand explicit-calculusapplicationextensions;twoinsightsectionscover3M2T4demands. Requiredmethod,geometricroleandsingularqualifications stayexplicit.',families=families,family_extensions=extensions,response_exclusions=response_exclusions,insights=insights),ensure_ascii=False,indent=2)+'\n')
 print(len(families),'authored families;',sum(len(f['member_specs'])for f in families),'explicit assignments')
