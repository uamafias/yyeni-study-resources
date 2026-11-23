"""T5 numerical-method source groups; emit only after queued LIMIT08 repair."""
import json
from pathlib import Path
W=Path(__file__).resolve().parents[2]
families=[];insights=[];extensions=[]
def D(s):return '8227:2020:'+s
def N(o,n):return D(f'M2:T6:O0{o}:D0{n}')
def M(b,k,ns,parts='*'):
 ch=6 if b=='Goldie' else 13
 return [dict(item_id=f'8227:TB:{b}:C{ch}:{k}:{n}',parts=parts,membership_reason='Explicit source-response membership. Preserve original target root,source-given versus author-chosen start/map,rounding instructions,connected model and source scope/defect notes. No standalone recipe is approved.')for n in ns]
def G(k,ns,parts='*'):return M('Goldie',k,ns,parts)
def Y(k,ns,parts='*'):return M('YM',k,ns,parts)
def F(slug,title,decision,givens,constraints,rep,scaffold,methods,form,difficulty,distinction,ds,ms,exam=True,why=None):
 families.append(dict(family_id='8227:TEXTBOOK-FAMILY:'+slug,title=title,learner_decisions=decision,givens_and_unknowns=givens,
  constraints=constraints,representation_and_response=rep,scaffolding_and_connected_parts=scaffold,alternative_methods=methods,
  units_and_precision='Keep full internal states,source-required intermediate displays and finaldp/sf separate. A givenstart is binding;an open start’s authorbenchmark is not exclusive. Final root needs original-equation/target-interval certification,not only repeated rounded iterates. Trigonometric maps use radians.',
  answer_form=form,difficulty_progression=difficulty,distinction_basis=distinction,assessed_demand_ids=ds,member_specs=ms,
  examination_relation=dict(kind='structural branch'if exam else'textbook-only',pattern_ids=['8227:FAMILY:numerical-method-chain']if exam else[],part_ids=['8227:EXAM:2025:P2:Q12:a','8227:EXAM:2025:P2:Q12:b','8227:EXAM:2025:P2:Q12:c','8227:EXAM:2025:P2:Q12:d']if exam else[],
   evidence_label='examination-observed (NSSCAS 8227), comparative link only'if exam else'textbook-derived',
   reason=why or 'Observed numerical-method chains anchor the comparison. Source model,graph/sign evidence,provided map,target branch and precision differ;no blanket same-type label or official award is inferred.')))

F('numerical-graph-count-bracket','Use suitable graphs and signs to locate and count original roots',
 'Choose/read the actual graph pair,reason about the requested global/bounded count and certify named brackets by continuous sign change.',
 'Equation,possibly prescribedgraphs/finiteinterval;unknown sketch,count and endpoint proof.',
 'Continuity needed for signchangeexistence;finiteviewportalone doesnot prove globalcount. Preserve near-asymptote/negative roots and original log/rootdomain.',
 'Equation or given graph to sharedsketch,count and sign calculations.',
 'Graphcount and signbracket are separate evidence;sourcegivenpair versus chosenpair is a structural scaffoldbranch.',
 'Source-requiredgraphicalreasoning plus exactsigns/continuity;monotonicity validates count without replacing an askedplot.',
 'Allrequestedgraphs,count and brackets,not one approximate root alone.',
 'YM1cubic/linehasone;Try1Q1hasthree;Try1Q3needs the near-asymptote secondroot. Goldie6B5graph/uniqueness survives its excludedfree-mapchoice.',
 'Number/location reasoning differs from executing a recurrence whose convergence is already given.',[N(1,1),N(1,2)],
 Y('Example',[1,2])+Y('Try-Now-1',[1,2,3])+Y('Try-Now-2',[1,2,3,4])+G('Exercise-6B',[5],['i','ii'])+G('Exercise-6B',[6],['i']))
F('numerical-sign-existence','Certify a root bracket by calculation on a continuous residual',
 'Evaluate BOTHoriginalendpointsigns,check continuity and state existence without claiming uniqueness from signs alone.',
 'Equation and two endpoints;unknown root-existence proof.',
 'Discontinuity can give opposite signs without a root;zero endpoints require a different conclusion than an open bracket.',
 'Equation to exact/guard-digit signs and reason.',
 'This standalone proof is smaller than a fullgraph→rearrangement→iteration chain.',
 'Residualsignproduct or comparison of the originalequation sides,with continuity.',
 'Valid bracket conclusion and supporting sign evidence.',
 'GoldieExample1showstwoendpointcomparisonroutes for e^x-x=x²+2.',
 'Signexistence doesnot establish a complete realrootset.',[N(1,2)],G('Example',[1]))
F('numerical-search-and-bisection','Locate and refine the complete requested root set by search/bisection',
 'Find appropriate continuousbrackets,refine eachselectedroot and preserve allroots/required methodtraces.',
 'Equation/given graph with requestedaccuracy;unknown count,brackets and numerical roots.',
 'Even/touchingrootsneedadditionalreasoning;separate brackets for multiple roots;exactroot2is not forced approximate.',
 'Equation/graph to proof/sketch and saved search/bisection states.',
 'Source may ask no-stationaryproof first,or integernode search beforebisection;keep these stages.',
 'Decimal search/bisection as requested;independent original-root solver onlychecks the source methodresult.',
 'Everytargetroot to sourceprecision and any asked bracket/errorform.',
 'Goldie6A1hasno stationarypoints beforecount;6A3hasoneexactroot;6A6asks a±(1/2)^nintervalform;6A7startsfromgivenunscaledgraph.',
 'Refinement/complete-rootset is additional to one signbracket;these methods are textbook support,not a new claim that8227mandatesbisection.',[N(1,1),N(1,2)],G('Exercise-6A',[1,2,3,4,6,7]))
F('numerical-method-trace-comparison','Compare decimal search and bisection using actual traces',
 'Run BOTHsource-requiredmethods on both selectedouterroots,then justify the requested effort/efficiency comparison.',
 'Two quinticrootintervals and prescribed methods;unknown four traces/results and comparison.',
 'Target outerroots,not the attractingmiddle one;trace counts depend on stated algorithm and stopping convention.',
 'Equation/intervals to two methods and explanation.',
 'One finalrootlist doesnot demonstrate both methods.',
 'Decimal search and intervalbisection with independently certified finalroundingcells.',
 'Four specified method/targetresults and reasoned comparison.',
 'Goldie6A5asks twoouterrootsbybothmethods;the value changes are not extra independenttypes.',
 'Required methodcomparison adds evidence beyond a numerical root.',[N(1,2)],G('Exercise-6A',[5]),exam=False)
F('numerical-sign-search-limitations','Explain what sign searches can miss or falsely suggest',
 'Distinguish a touchingroot,multipleclosecrossings and a pole,using actual graph/domain rather than treating signchange as an unconditional rootdetector.',
 'Suppliedexamplegraphs or rationalfunctions/searchinterval;unknown sketch/root/searchdiagnosis.',
 'A reciprocalpole isnot a root;evenmultiplicitycan give equalendpointsigns;onebracket doesnot count enclosedroots.',
 'Graph/formula to featurechecks and explanation.',
 'Workedwarnings are supportingillustration;posed6A8asks everygraph/root/searchresponse.',
 'Exactroots/domainanalysis and source searchsimulation.',
 'Correctdiagnosis with requestedplots/rootsets.',
 'GoldieWorkedillustration3hasthreefailurewarnings;6A8contrasts1/x,x/(1+x²),x²/(1+x²)on-0.3..0.7.',
 'These are limitations of signsearch,not evidence that a fixedpointsequence itself failed toconverge.',[],G('Worked-illustration',[3])+G('Exercise-6A',[8]),exam=False)
F('numerical-iteration-fates','Interpret convergence,divergence and convergence to a different target',
 'Track the SUPPLIEDmap/start outcomes,check domains and distinguish failure toapproachanyroot from convergence to an unrequestedroot.',
 'Givenmaps,starts/targetintervals and sometimescobweb/curve;unknown outcomes and qualitative explanation.',
 'No formalderivative convergence theorem required byLIMIT08. Repeatedrootestimatealone is not proof of requestedroot/correctrounding. A validwrongtargetroot stillmisses thetask.',
 'Suppliedrecurrence/graph to traces and explanation.',
 'GoldieActivity2asks explanation referringtoasketch;numericfourstartoutcomesalone insufficient. Source derivative-tests elsewhere remain explanatoryextension,not mandatory.',
 'Actualiteration/domainchecks,qualitativegraphinterpretation and independentlyverifiedfixedpoint/residual.',
 'Everyrequestedoutcome,rootselection distinction and source-requiredvisual explanation.',
 'GoldieActivity1usescosine/repeatedroots;Activity2ends±2divergewhile±1approachmiddle;YM6/Try6compareprovidedmaps and targetroots.',
 'Changing the map/start can change fate,not merely the printednumbers.',[N(2,1),N(2,2)],G('Investigation',[1])+G('Activity',[2])+G('Prompt',[4,5])+Y('Example',[6])+Y('Try-Now-6',[1,2]))
F('numerical-rearrangement-branch-proof','Verify a supplied rearrangement without losing original branches',
 'Apply inverseoperationswiththeirconditions and decidewhetherthesuppliedfixedpointrelation is globallyequivalent or only selects the targetbranch.',
 'Originalequation andproposedrearrangements;unknown equivalence/branchproof.',
 'Principal evenrootsselectnonnegativevalues;logsrequirepositivearguments;denominatorsnonzero. A conditionalfixedpointlimit relation doesnotprove convergence.',
 'Equation/map to logicalproof with domainledger.',
 'Four suppliedformsremainparts ofonecomparison;no freelyinventedmapisrequired.',
 'Exactalgebra,domainimplications and originalequationcounterexample/bracketsfor lostbranches.',
 'Correctequivalence/conditionalstatementfor everyform.',
 'Goldie6B2principal4th/squarerootformsloseanegativeoriginalroot.',
 'Branch-preservingproofisstrongerthanwritingan algebraicallyplausibleformula.',[N(3,2)],G('Exercise-6B',[2]))
F('numerical-supplied-map-chain','Use a supplied map or rearrangement to find a certified target root',
 'Verifyoriginalbracket/maprelationasasked,executetheprovidedrecurrenceandapplyliteralintermediate/finalprecisiontotheselectedroot.',
 'Equation,map/rearrangement,targetinterval andgiven/openstart;unknownproofs,statesandroot.',
 'Every mapstateinreal domain;principalinverse selectsactualradianinterval. Sourceopenstart permits validalternatives;authorbenchmark isnot a newgiven.',
 'Equation/recurrence with sourcegraphasks toproof,traceandroundedroot.',
 'Preservegraph/sign/rearrangement/iterationparts distinctly. Goldie6B5(iv)needsanexplicitlysuppliedmapinanadaptationbecause itsownmap-choicepartisexcluded.',
 'Source recurrence with unrounded internalvalues and literal displays;independent original-rootbracketing/roundingcellcertifies stopping.',
 'Allsource-requiredproofs/states andtargetrootwithcorrecttrailingprecision.',
 'YM3findscoefficientsinPROVIDEDrationalform;Try5Q3writesrecurrencefromprovidedrootform;8usesboundedradianmap. Differentvalidmaps for thesameroot have differenttraces/invaliddomains.',
 'Providedmapexecutionandstoppingare notfree-choice map construction or a finalnumberonly.',[N(3,1),N(3,2),N(4,1),N(4,2)],
 G('Exercise-6B',[1,3,4,7,10,13,14,15])+G('Exercise-6B',[5],['iv'])+Y('Example',[3,5,8])+Y('Try-Now',[3,8])+Y('Try-Now-4',[3])+Y('Try-Now-5',[1,2,3])+Y('Exercise-13',[1,6])+Y('Revision-Exercise-13',[2]))
F('numerical-given-map-to-equation','Execute a given recurrence then derive its fixed-point equation/exact root',
 'Use the GIVENsequencefirst,thenpassconditionallytoafinitelimit,derive theoriginalalgebraicequationandselecttheexactroot.',
 'Recurrence/startandstatedconvergence;unknowniterates,limitpolynomialandexactroot.',
 'Originalpolynomialmaynotbegiven;do notsupplyitasanextra clue. Nonzerodenominatorlimit and realrootbranchmusthold.',
 'Suppliedrecurrenceto numerictrace,algebraicequationandexactvalue.',
 'Direction ismap→equation ratherthanequation→map. Sourcegivenconvergence isnotaseparateaskedproof.',
 'Literaliteration andconditionalfixedpointequation,algebraicrecovery/exactrootcheck.',
 'Requestedstates/finalprecision andcorrectexactlimit/equation.',
 'YM4andTry4Q2sharecuberoot12butdifferentmaps;Try4Q1gives8α³-α²-6;Revision13Q1givesα5=306. Goldie6B9statesconvergenceinthesetup.',
 'Reverse fixed-point interpretationasksdifferentknowledgefromverificationofanoriginalequationalreadygiven.',[N(2,1),N(3,1),N(4,1),N(4,2)],
 G('Exercise-6B',[9])+Y('Example',[4])+Y('Try-Now-4',[1,2])+Y('Revision-Exercise-13',[1]))
F('numerical-gradient-constraint-chain','Derive a supplied recurrence from a prescribed explicit-curve gradient',
 'Differentiate theoriginalcurve,imposethestatednonzerogradientandderive the PROVIDEDmapbeforebracketing/iteration.',
 'Explicitcurve,gradienttarget andsuppliedmapform;unknownrelation,bracket,statesandroot.',
 'Do not replace agradientconditionbyacurveordinateequation;providedlogmapdomainandoriginalpointconditionspersist.',
 'Curve/gradient tocalculusrelation,signproofandtrace.',
 'Keepderivative/modelbeforeiteration;requestedexplicitderivativeformulaonlywhereasked.',
 'Elementary/productrulethenalgebra/logs,originalresidualbracketandgiveniteration.',
 'Allrequestedrelations,signchecks,statesandroot.',
 'YM7asks5dpstateswhilekeyprints4;Try7Q1hasopenstartand4dp/2dp. Sourcebenchmarksarenotexclusive.',
 'Derivingtheresidualfromagradient isadditionalassessedreasoning absentfromabareequation.',[N(3,2),N(4,1),N(4,2)],Y('Example',[7])+Y('Try-Now-7',[1]))
F('numerical-stationary-constraint-chain','Derive a supplied fixed-point relation for a named stationary point',
 'Differentiate thecurve,selectthenamedinteriorstationarypointandtransformitsconditionintothesuppliedmapbefore numericalsolution.',
 'Curve/givengraphmaximum/minimum andsuppliedrearrangement;unknownstationaryrelation,bracket,statesandroot.',
 'Divisionbythepointabscissaneedsnonzerointeriorcondition. Principalatanbranchmustmatchradianinterval;knownotherstationary/endpointsarenottarget.',
 'Given curve/graphto calculus,proofsandnumericaltrace.',
 'A precedingexactminimumcanbedistinctfromthelaterintersectionroot;sourcepartsretainboth.',
 'Appropriatecalculus/algebra,providedmapandindependentoriginalstationary/intersectioncheck.',
 'Everyaskedexactcalculusresult,providedrelation,bracketandprecision-correctroot.',
 'Goldie6B11/12andYMExercise13Q4distinguish anexactminimum fromalaterroot;YMTry7Q2diagramnonzerompermitsdivision;Exercise13Q2has a boundedtrigmaximum.',
 'Modelderivation/namedpointselectioncannotbecollapsedintoaroutine recurrencebecausefinal arithmeticlooks similar.',[N(3,2),N(4,1),N(4,2)],
 G('Exercise-6B',[11,12])+Y('Try-Now-7',[2])+Y('Exercise-13',[2,4])+Y('Revision-Exercise-13',[3]))
F('numerical-parametric-gradient-chain','Derive a supplied recurrence from a parametric gradient condition',
 'Formtheparametricslopeonaregularbranch,imposegradient-1andderive the PROVIDEDrootrelationwithoutlosing its sign/domain.',
 'Parametriccurve,targetgradient,suppliedsixth-rootmapandgivenstart;unknownproof,statesandparameter.',
 'Evenrootrequirescorrectsignselection;X′/Y′regularityandoriginalrootdomainmusthold.',
 'Parameterformulas toderivativerelationandtrace.',
 'Parameterisnotthecurve’sx-coordinate;sourcefinalp/tprecisionpreserved.',
 'Parametricchainratio,branchawarealgebraandgiveniteration;originalgradientverifiesparameter.',
 'Requestedrelationandallstates/finalparameter.',
 'Goldie6B16andYM11repeat thecoremodel;YMtableheadingsareindexedonestep early.',
 'Parametric/geometricderivationisadditionaltoexplicitgradientchain.',[N(3,2),N(4,1),N(4,2)],G('Exercise-6B',[16])+Y('Example',[11]))
F('numerical-integral-bound-chain','Derive a supplied recurrence from a definite-integral target',
 'Integrate theactualfunction,applytheoriginalbounds/valueandderivetheprovidedmapwithallpositive/log/rootconditions.',
 'Definiteintegralwithunknownpositivebound,targetvalue andprovidedrearrangement;unknownrelation,bracketandroot.',
 'Originalintegralcontinuousonitsinterval;unknownboundrestrictionssuchasa>1matter. Source5sfversus5dpmustnotbeinterchanged.',
 'Givenintegralcondition toproofandnumericaltrace.',
 'Keepintegral→providedmap→sign/iterationchain;earlierchapterrepeataddsno structuralbreadth.',
 'Validprimitiveandendpointsubstitutionthenmapalgebra,independentintegral/residualreferenceanditeration.',
 'Requestedexactrelation androot/statesin literalprecision.',
 'Goldie6B8uses5dpstates/3dproot;YMExercise13Q3uses5sfstates/3sfroot;Q5hasmixedpower/logintegraland a>1.',
 'Integralmodellingandboundadmissibilityareadditionaltoarootalreadygivenasequation.',[N(3,2),N(4,1),N(4,2)],G('Exercise-6B',[8])+Y('Exercise-13',[3,5]))
F('numerical-circular-area-chain','Derive a supplied angle recurrence from circular area constraints',
 'Modelthegivenminorsegmentandtriangle/circleratio,selectthenondegenerateangleanduse theprovidediterationbeforeanychordrecovery.',
 'Given circle/segmentdiagram,arearelation,suppliedmap/start;unknownanglerelation,rootandpossiblychord.',
 'Minorangle0<α<π;excludezerodegeneracy;sharedradiuscancelsonlyintherightarearelation. Chordusesoriginalradiusandunit.',
 'Givengeometricdiagram to areaequation,iterationandrequestedlength.',
 'Chordis a laterdependentoutput,not a reason torequireanotherunaskedidentityproof.',
 'Segment/triangleareas,radiantrig,sourceiterationandindependentangle/chordcheck.',
 'Providedrelation,requiredstates/finalangleandaskedchord.',
 'YM9hassegmentone-sixthcircle;Try9Q1segment=triangleandradius8cmchord. Theyshareasegmentkernelbutdifferentgivenareaequations.',
 'Read/modelthearea isadditionalreasoning;circlelabels/scalesmustvaryconsistentlylater.',[N(3,2),N(4,1),N(4,2)],Y('Example',[9])+Y('Try-Now-9',[1]))
F('numerical-region-area-chain','Derive a supplied recurrence from a graph-defined equal-area condition',
 'ReadtheACTUALboundedregion,deriveitsareaandapplytheequalitybeforeusingtheprovidedmaponthenondegeneratebranch.',
 'Given graphwithrectangle/shadedregionorboundedexponentialarea;unknownarea,maprelationandroot.',
 'Distinguishrectangleminuscurvedarea andline-minuscurve;excludezerowidthendpoint. Allgraphlabelsremaincorrelated.',
 'Givengraph tointegral/areaformula,providedrelationandtrace.',
 'Arearesponseanditerationaredistinct;do notsupplythemodelasagivenin anequivalent-demandclaim.',
 'Sourcegeometryandintegrationthenprovidediteration;independentrecomputedareacondition.',
 'Askedareaexpression,providedmapproofandliteralnumericalprecision.',
 'YMTry9Q2hascosinecurve/rectangle;Revision13Q4hase^-xandy1withp>0.',
 'Model-specificregionreadingcannotcollapseintotheintegral-boundtaskwhere theintegralissupplied.',[N(3,2),N(4,1),N(4,2)],Y('Try-Now-9',[2])+Y('Revision-Exercise-13',[4]))
F('numerical-polynomial-preparation-chain','Use polynomial factors/division to derive a provided recurrence',
 'Establish/use thegivenlinearroot,factor/divideandderive thePROVIDEDcube-rootformwithoutpretendingthepolynomialrootwasalreadyknown.',
 'Quarticwithlabelledpositive/negativerootsandprovidedmaptemplate;unknownfactor/quotient/constantsandtargetroot.',
 'Retainselectedpositivebranch andsourcegivenfactor;differentrootlabelsarenot interchangeable.',
 'Givenpolynomial/graph tofactorisation,rearrangementandtrace.',
 'Factor/quotient→henceprovidedrelation→iteration staysconnected.',
 'Factor/remaindertheorem,polynomialdivision,branchalgebraandgiveniteration.',
 'Everyaskedfactor/quotient/mapcoefficientandrootatrequestedprecision.',
 'YM10usesroot3;Try10uses-2and6sfintermediate/4sffinalprecision. A higher sourcefactorial labeldoesnotchange theactualscope.',
 'Algebraicpreparationisextraevidencebeyondexecuting agivenrecurrence.',[N(3,2),N(4,1),N(4,2)],Y('Example',[10])+Y('Try-Now',[10]))
F('numerical-worked-demonstration-support','Audit worked search/iteration demonstrations without inventing posed tasks',
 'Tracktheexample’sactualstates/bracketsandread its interpretation while separatingworkedteachingfromseparatelyposedpractice.',
 'Unprompted decimal/bisection/fixedpoint/goldenratiotables;unknown internalQAfeature/statechecks.',
 'Fullinternalvaluesbeforedisplay;tableindexandprecisionheadercan bewrong. Formalderivativeconvergenceproofnotadded.',
 'Workedtable/cobweb toverifiedsupportingrecord.',
 'Multipleprintedstatesareoneworkedsource,notmanyassignedquestions. Supportinggoldenratioillustrationisnotexaminationfrequency.',
 'Independentquestion-operandcomputationandoriginalequationchecks.',
 'Source-featurecheckswithdefectsandinterpretationexplicit.',
 'GoldieWorked5hasanexactmiddlequinticrootdespite earlierfalseimpossibilityclaim;YMgolderatioheader5sfconflictswith3dpstopping.',
 'Proof/readingevidenceisretainedwithoutinflatingassessedtypecounts.',[],
 G('Worked-illustration',[1,2,4,5,6,7])+Y('Worked-illustration',[1,2,3]),exam=False)
F('numerical-search-explanation-support','Explain search certainty,precision and method selection',
 'Distinguishabracketcertificate,iterationevidence,absoluteerrorandroundeddisplay;state thesearchconventionwhen countingtrials.',
 'Conceptualprompts/activityandfiveequationswithmethodchoice;unknownreasoning andsupportingroot/searchresults.',
 'Intervalwidthalonedoesnotuniversallyguaranteeidenticalroundingendpoints;blanketquinticunsolvabilityisfalse. A chosenmethoddoesnotbecome directlyassessed.',
 'Text/table reasoning toexplanation.',
 'Prompt1’smethodchoicesareinternalsupport;noforcedcompleted-squareorgraphdemandisretrospectivelyadded.',
 'Exactcounterexamples,errorbounds/roundingcellsandoriginalequationchecks.',
 'Requestedreasoningwithclearassumptionsandaccuracymodel.',
 'GoldieActivity1comparesbisectioncountsfordigits;Prompt6countsthetrialsfor.012,.385,.989;Prompt3contrastsfinalsignproofwithfiniteiterationvalues.',
 'Conceptualsupportdoesnotclaimanadditionalexam-requiredsearchalgorithm.',[],G('Prompt',[1,3,6])+G('Activity',[1]),exam=False)

response_exclusions=[
 dict(item_id='8227:TB:Goldie:C6:Exercise-6B:5',part_labels=['iii'],rule_id='8227:LIMIT08',applies_to='iii only',quoted_value='Rearrange this equation in the form x = F(x).',reason='Originalfreelyinventedrearrangementexceedsprovided-map scope. Sourcegraph/uniquenessandexecutionfacetsremaininternalwithadaptationconditions.'),
 dict(item_id='8227:TB:Goldie:C6:Exercise-6B:6',part_labels=['ii'],rule_id='8227:LIMIT08',applies_to='ii only',quoted_value='Use the method of fixed-point iteration to find the second value to 3 decimal places.',reason='Originalsuppliesnomap/rearrangement;benchmarkusesanauthorchosenmap. Keepit asinternaloutside-scopeanswer evidence,not directprovided-iterationcoverage.'),
]
# Try11sharesacurvebutits(a)trapeziumand(b)iterationhavedifferentdemands.
for f in families:
 if f['family_id']=='8227:TEXTBOOK-FAMILY:numerical-supplied-map-chain':
  f['member_specs']+=Y('Try-Now',[11],['b-x2','b-x3','b-x4','b-x5','b-x6','b-root'])

def I(slug,title,ds,teaching,exam,difficulty,pitfalls,gaps,proposals,items,parts,grades):
 insights.append(dict(insight_id='8227:TEXTBOOK-INSIGHT:'+slug,title=title,demand_ids=ds,teaching_comparison=teaching,
  examination_comparison=exam,difficulty_and_grade_bounds=difficulty,pitfalls=pitfalls,gaps_and_representations=gaps,
  implications_for_step3=proposals,evidence_item_ids=items,examination_part_ids=parts,grade_descriptor_ids=grades,marking_rule_ids=[],examiner_error_ids=[]))
def S(b,k,n):return f'8227:TB:{b}:C{6 if b=="Goldie" else 13}:{k}:{n}'
I('numerical-graphs-and-brackets','Graphical root estimates,counts and continuous sign brackets',[N(1,1),N(1,2)],
 'Goldieexplicitly contrastsdecimal/bisectionsearch,rootcounts andfailureexamples;YMstartswithprescribed-versuschosen graphpairs,then calculationofnamedbrackets. Both keepgraphicalevidence separatefromnumericalsignproof. Asignchangeprovesexistenceonlywithcontinuity;globalcountneedsmorethana coarseviewport.',
 'NSSCAS2025P2Q12(a)(b)andtheothernumericalchainsanchorsketch/signbracketstructures. Goldie’salgorithmcomparisonsaretextbook-derivedsupport,notnewrequiredprocedures. YMTry1Q3’snear-asymptoterootandGoldie6A7’stwocrossingsshowwhyseeingonecrossing isnot a completecount.',
 'A15/C16includeapproximategraph/signlocation;E15supportsprovidediteration. Harderrootcountcases involvefiniteversusglobaldomain,touching/multiple roots andsingularities. Thebisectionerror-countinvestigationisoptionalpedagogicalbreadth,notanewsyllabusobjective.',
 'Goldie’sreciprocaldiscontinuitycounterexampledefeatssign-onlyexistence;atouchingzeroevadesa signchange. YM1andTry2Q1sourcegraphlabelsarewrong;Try2Q4upperendpointvalueiswrongwhilebracketremainsvalid. Registeredsourceerrorsarenotlearnermistakefrequencies.',
 'Both books supportgraph/signchains;Goldiehasmoresearch-mechanism/limitationswork,YMmoreexplicitmixedfunctionpairs. Givenunscaledgraphs andaskedsketchesrequiredifferentresponses. Afiniteplotnearalogasymptotecanmiss a realbranch.',
 'Propose originaldomain/continuityconditions,literalrootcountscopeandallrequestedgraph/signoutputs. Checkeachbracketagainsttheoriginalresidual;keeprootexistence,countandfinalroundingcertificatesseparate. Do notlabelalgorithmcomparisonsasNSSCASobservedunlessanoriginalpaperdoes.',
 [S('Goldie','Example',1),S('Goldie','Worked-illustration',3),S('Goldie','Exercise-6A',5),S('Goldie','Exercise-6A',7),S('Goldie','Exercise-6A',8),S('YM','Try-Now-1',3),S('YM','Try-Now-2',4)],
 ['8227:EXAM:2025:P2:Q12:a','8227:EXAM:2025:P2:Q12:b'],['8227:GRADE:A:15','8227:GRADE:C:16','8227:GRADE:E:15'])
I('numerical-fixedpoint-and-failure','Fixed-point meaning,supplied rearrangements and failure modes',[N(2,1),N(2,2),N(3,1),N(3,2)],
 'Goldiecomparesmaps/starts,targetrootversusotherrootandcobwebreasoning;YMcontrastsbad/goodprovidedmaps,thenlinksrecurrencestooriginalequationsinbothdirections. Aprovidedmap→polynomialtaskisnotthesameasverifyingagivenrearrangementoftheoriginalequation. Bothcontainexplanatoryderivativeconvergencecomments,butLIMIT08doesnotrequireaformaltest.',
 'NSSCAS2021P2Q8and2025P2Q12containprovided-recurrencerelation/iterationchains. Textbookfreeinventionofamapisadditional:Goldie6B5(iii)and6B6(ii)areexplicitlyoutsideoriginalprovided-formscope. Theirvalidinternalbenchmarksneedanadaptationwiththeformulaactuallysupplied. Sourceprincipalrootrearrangementsthatloseanegativerootmustretaintheirbranchqualification.',
 'C16namesconvergentapproximationmeaningandnotation;A15/C16relatethesuppliedmaptotheequation;E15explicitlyexcludesformalconvergenceconditionswhileunderstandingfailure. Logicalbranch,domainandtargetrootselectionincrease demand,notjustmoreiterationsteps.',
 'GoldieActivity2’s±2startsdivergewhile±1convergetothemiddlerootoutsidetheoutertargetintervals;thosearetwodifferentfailuretypes. Principal4th/squareroots in6B2loseanegativeoriginalroot. Afiniteapparentlystabletabledoesnotproveconvergenceorselectedrootvalidity.',
 'Bothbookscoverfailure,butGoldieexplicitlyasksagraph-basedexplanationwhereYMusescomparativeworking. Generalfree-mapinventionmustnotinflateprovided-rearrangementcoverage. Atextbookderivativecriterioncanremainoptionalexplanationwithoutbecomingamandatorymarkingstep.',
 'Propose keepingoriginalequation,providedF,real-mapdomain,targetintervalandstartseparate. Preserveconditionalfixedpointproofswithallinverseconditions. Userootresidual/intervalchecks toseparatewrongtargetfromdivergence. Do notaskformalconvergenceproofsinan8227recipe.',
 [S('Goldie','Activity',2),S('Goldie','Prompt',4),S('Goldie','Exercise-6B',2),S('Goldie','Exercise-6B',5),S('Goldie','Exercise-6B',6),S('YM','Example',4),S('YM','Example',6),S('YM','Try-Now-6',2)],
 ['8227:EXAM:2021:P2:Q8:a','8227:EXAM:2021:P2:Q8:b','8227:EXAM:2021:P2:Q8:c.i','8227:EXAM:2021:P2:Q8:c.ii','8227:EXAM:2025:P2:Q12:c'],['8227:GRADE:E:15','8227:GRADE:C:16','8227:GRADE:A:15'])
I('numerical-execution-stopping','Literal recurrence execution,precision and connected source models',[N(4,1),N(4,2)],
 'Bothbooks givefixedmapsandstartinstructionswithdifferentstate/finalprecision. YM13addsgeometricarea,calculusgradient,integralboundandpolynomialpreparationchains;Goldie6BprovidesseveralcloselyrelatedCambridge-attributedinternalexamples. Repeatedsourceoccurrencesdonotcreate newtypebreadth. Whenstartisopen,theprintedbenchmarkisonlyonevalidchoice.',
 'NSSCAS2025P2Q12(d)andearliernumericalchainsrequireexecutingtheprovidedformulaandrequestedprecision. Numericalrootagreementalonecannotdemonstrateactualiterations. Textbooktangent/maximum/area/integralpreparationchangeswhatisassessedbeforetherecurrence. YM11’sseparatetrapeziumpartanditerationpartsharea curvebutnocommonassessedmethod.',
 'E15explicitlyrequiresgiveniterationto prescribedaccuracy. Hardercaseschangebranch/domain,sourcegivenstart,mapdirectionorprecisionmodel. Moretable rowsarenot inherentlyhigherBloom/difficulty. Parameterdomainmustkeepeachactualiteratevalid;finalstateprecisionandanswerprecisionaredifferentrequirements.',
 'YMExample7asks5dpbutprints4;11indexesstatesonestepearly;goldenratioheader5sfconflictswith3dpstopping. Try4Q3key’s1.56iscorrect2dpbutwronglylabelled3dp. Earliernativefalseleads(suchasTry3positivesignandgoldenratio decimal)wereclearedandremaincleared. Theseare sourcelimits,notacceptablelearneranswers.',
 'Bothbooksofferrichconnectedchainsbutordinarynumericdrillsalonecannotcoverallmodelderivations. Finalroundingcanbecertifiedbyoriginal-equationroundingcellsratherthanonlyrepeateddisplays. Intermediatefullprecisionmustsurvivecorrectsource5sfversus5dpinstructions.',
 'Propose reproduciblefullstatetraces,exactstart/mapidentity,literaldisplayrulesandanindependentoriginalrootreference. Validateboundaryroundingcellsandtargetselection. Keepdistinctmodelpreparationsashonestbranchesandpreserveanygivenversusderiveddiagraminformation;detailedruntime/stoppingcontractsarestep3proposals.',
 [S('Goldie','Exercise-6B',8),S('Goldie','Exercise-6B',16),S('YM','Example',7),S('YM','Example',9),S('YM','Example',10),S('YM','Example',11),S('YM','Try-Now',11),S('YM','Worked-illustration',3),S('YM','Exercise-13',3)],
 ['8227:EXAM:2025:P2:Q12:d'],['8227:GRADE:E:15','8227:GRADE:C:16','8227:GRADE:A:15'])

if __name__=='__main__':
 target=W/'tools/textbook-r5/synthesis-numerical.json'
 target.write_text(json.dumps(dict(authorship='Codex author; independent review pending',scope='GoldieC6/YMC13numericalfamilieswithsource-suppliedmaps,modelchainsandliteralprecision;threeinsightsectionscover8M2T6demands. QueuedLIMIT08sourcecorrectionmustbeappliedbeforeassembly.',families=families,response_exclusions=response_exclusions,insights=insights),ensure_ascii=False,indent=2)+'\n')
 print(len(families),'authored families;',sum(len(f['member_specs'])for f in families),'explicit assignments')
