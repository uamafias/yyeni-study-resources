"""Explicit final T5 comparisons; no automatic demand/topic-to-family matching.

All links are conservative structural comparisons. R2-02 recipe-branch same-type
identity remains deferred. Rows name actual inspected,unheld examination parts.
"""
LINKS={}
def add(slugs,patterns,parts,reason):
    for slug in slugs.split(','):
        assert slug not in LINKS
        LINKS[slug]=dict(kind='structural branch',
            pattern_ids=['8227:FAMILY:'+p for p in patterns.split(',')],
            part_ids=['8227:EXAM:'+p for p in parts.split(',')],
            evidence_label='examination-observed (NSSCAS 8227), comparative link only',
            reason=reason+' This compares source structure;it neither approves a recipe branch nor claims identical whole-question demand or official marking.')

add('circle-arc-major-minor,curvilinear-perimeter','circular-symbolic','2021:P1:Q7:a',
    'The examination models an arc/perimeter relation. Textbook direct major/minor arcs are supporting branches;multi-centre and tangent boundaries change the geometric reconstruction.')
add('circle-major-sector,overlapping-sector-area','circular-symbolic','2021:P1:Q7:b',
    'The examination calculates a region area after earlier circular modelling. Textbook simple-sector and overlap/gap decisions retain their own region boundaries and scaffolding.')
add('sector-perimeter-inverse,annular-sector-model,sector-segment-equality','circular-symbolic','2021:P1:Q7:a,2021:P1:Q7:b',
    'The observed chain relates circular measures to a derived area. Textbook inverse givens,annular holes or equal-area equations change the learner decisions;their extra structure is not claimed observed wholesale.')
add('trig-reflection-pair,trig-formula-restricted-sketch,trig-graph-investigation','trig-graph-sketch','2025:P1:Q4:a',
    'The observed part asks a restricted transformed-sine sketch. Textbook reflection pairs,multirow investigations and other base functions extend its visual demand;the complete investigation is not an examination-observed task.')
add('trig-analytic-features,trig-maxmin-parameters,trig-given-graph-reading','trig-graph-reading','2022:P1:Q10:a,2024:P1:Q9:a',
    'Observed supplied-graph parameter/feature reading anchors comparison. Formula-to-feature or stated-extrema-to-constants reverses the input direction and is supporting practice,not identical graph-reading evidence.')
add('trig-shared-graph-deductions,reciprocal-graph-uniqueness','line-curve','2025:P1:Q4:b,2025:P1:Q4:c',
    'The observed line/curve shared-sketch count is explicit. Textbook chosen-line or reciprocal uniqueness explanations add different original-domain/monotonicity evidence;the actual full source response is retained.')
add('special-angle-exact-values','bounded-trig','2022:P1:Q9:b',
    'Exact special values appear inside the observed bounded-solving response. Isolated ratio recall/evaluation supports that step but does not cover the complete equation-solving demand.')
add('ratio-recovery-quadrant,reciprocal-pythagorean-equations,compound-parameter-ratio-chain','advanced-trig-solve','2024:P2:Q9:a',
    'The observed acute reciprocal/Pythagorean equation asks an exact tangent ratio before a later compound part. Textbook unrestricted-quadrant or full bounded-angle outputs change the target and retain extra sign/branch work.')
add('identity-expansion-basic,identity-fraction-cancellation,identity-conjugate-square,identity-common-expression','basic-trig-proof','2021:P1:Q5:b,2023:P1:Q8:a',
    'The observed proof responses use basic identities. Source expansions,conjugates,fraction aggregation and common-expression routes remain distinct valid method branches with original common domains.')
add('bounded-basic-trig-roots,bounded-squared-ratio,bounded-affine-argument','bounded-trig','2021:P1:Q5:a,2022:P1:Q9:b',
    'Observed finite trig solving anchors complete bounded enumeration. Squared ratios,negative windows and shifted/multiple arguments alter branch recovery and are not collapsed into numerical substitutions.')
add('trig-factor-zero-branches,trig-hence-transformed-equation','bounded-trig','2023:P1:Q8:b',
    'The observed solution uses a preceding basic identity. Textbook zero-factor and changed-argument cases preserve actual hence links,original poles and all finite branches.')
add('trig-quadratic-reduction,trig-fourth-power-substitution','bounded-trig','2022:P1:Q9:a,2022:P1:Q9:b',
    'The examination explicitly reduces then solves a trig equation. Textbook quadratic-in-squared-ratio or rational-denominator branches add their own algebraic range and pole checks.')
add('trig-proof-hence-solve','basic-trig-proof,bounded-trig','2023:P1:Q8:a,2023:P1:Q8:b',
    'The observed proof/hence-solve chain provides the dependency structure. Source expressions and domains may differ;identity proof and original-equation verification remain separately required.')
add('trig-intersections-analytic','bounded-trig','2021:P1:Q5:a',
    'Both require bounded original-equation roots. The textbook supplies a graph and asks named coordinates,so reading labels and evaluating ordinates are extra structural evidence beyond the observed anonymous root list.')
add('trig-coefficients-zeros-sketch','trig-graph-reading,trig-graph-sketch','2024:P1:Q9:a,2025:P1:Q4:a',
    'Separate observed parts anchor parameter reading and a restricted sketch. The textbook joins value-based recovery,zeros and sketch in one chain;this does not assert that complete chain was sampled in one exam question.')
add('reciprocal-exact-values,compound-exact-angle,compound-signed-given-ratios','exact-trig-evaluation','2024:P2:Q9:b',
    'The observed part uses a prior exact ratio for a compound value. Basic reciprocal/special values are supporting preparation;two-angle signs and derived halves are additional source branches.')
add('reciprocal-sign-and-graph','trapezium-chain','2025:P2:Q4:b',
    'The observed part requires a reciprocal graph and bias explanation. Standalone source reciprocal sketches/sign reasoning support the graph component without covering the numerical/explanatory whole.')
add('compound-expand-simplify,compound-coordinate-geometry,compound-bounded-equations','advanced-trig-solve','2021:P2:Q6:a,2021:P2:Q6:b',
    'The observed compound-angle reduction/exact solving anchors comparison. Reverse simplification and coordinate reconstruction change the givens or remove later solving;they remain explicit source branches.')
add('compound-identity-proof,advanced-double-triple-proof,advanced-proof-hence-roots','advanced-trig-proof','2022:P2:Q7:a',
    'Observed reciprocal/double identity proof anchors method comparison. Textbook compound/triple proofs or subsequent integral/root targets change the specific reasoning/evidence;not every extra target is an observed whole task.')
add('double-angle-simplification,double-angle-bounded-equations,derived-triple-angle-equations','advanced-trig-proof,advanced-trig-solve','2022:P2:Q7:a,2021:P2:Q6:b',
    'Observed advanced identity and solving parts anchor comparison. Derived higher forms and standalone simplification extend or isolate those decisions;general unbounded solutions remain excluded.')
add('trig-sketch-reduce-intersections','trig-graph-sketch,bounded-trig','2025:P1:Q4:a,2022:P1:Q9:b',
    'The sources join required shared sketches,shown reduction and exact intersections. Separate observed parts support those decisions;the complete source chain is not claimed sampled as one examination item.')
add('rform-coefficient-conversion,rform-solve-cycle,rform-original-domain-reduction,rform-multiple-cycles','r-form','2021:P2:Q12:a.i,2021:P2:Q12:a.ii',
    'The observed R-conversion followed by an original equation anchors the chain. Textbook standalone conversion,reciprocal preprocessing and changed multiple-argument windows remain different structural branches.')
add('rform-extrema-sketch-solve,rform-extrema-arguments,rform-nonlinear-extrema,rform-corridor-model,phasor-current-investigation','r-form','2022:P2:Q6:a,2022:P2:Q6:b.ii',
    'Observed R-conversion and related extremum/argument work anchor comparison. Textbook graphs,nonlinear range maps,projection modelling and cancellation investigations add decisions not certified by that sampled chain.')
add('trig-mixed-revision-equations','bounded-trig','2021:P1:Q5:a',
    'The observed finite-root demand supports individual source equation branches. The mixed source set deliberately varies method selection and is not one approved recipe or one observed examination structure.')
add('elementary-exponential-primitives,elementary-log-primitives-domains,elementary-proper-exponential-integrals,elementary-reciprocal-definite-logform','standard-antiderivatives,definite-integral','2021:P2:Q2:answer',
    'Observed reciprocal/exponential integration and definite evaluation anchor comparison. Isolated primitives,explicit validity intervals and source-specific single-log forms retain their own requested evidence.')
add('elementary-trig-primitives,elementary-trig-definite','standard-antiderivatives','2021:P2:Q9:b',
    'The observed transformed trig integral includes standard affine reverse differentiation. Textbook direct forms isolate that component without covering its identity preparation.')
add('secant-identity-integral,trig-square-power-reduction-integral,identity-hence-integral-chain,finite-trig-product-integration,rform-trig-integration-chain','trig-integration','2021:P2:Q9:b,2023:P2:Q5:b',
    'Observed identity-assisted trig integration anchors comparison. Source free-choice versus supplied/proved identity,R preprocessing,repeated reduction and connected exact targets remain named structural branches.')
add('given-derivative-product-reversal','reverse-given-derivative','2024:P2:Q4:b',
    'The observed target uses a preceding derivative. Textbook supplied-product or secant/cotangent derivative scaffolds are prescribed reverse recognition only where the original actually supplies them.')
add('log-derivative-division-integral-chain,mixed-retained-definite-integrals','algebra-before-integration,definite-integral','2021:P2:Q9:a,2021:P2:Q2:answer',
    'Observed algebra before a listed primitive and definite evaluation support comparison. Supplied coefficient templates,log derivatives or odd-term symmetry change the source preparation;unsupplied general decomposition is not inferred.')
add('elementary-area-given-region,elementary-area-inverse-bound,elementary-complement-horizontal-area,power-area-sign-and-shift','integral-area','2022:P2:Q3:c',
    'Observed identity-assisted region integration anchors the area decision. Textbook function classes,inverse bounds,complementary or horizontal strips and changed input representations are explicit branches,not identical whole demands.')
add('elementary-trig-washer-volume','integral-volume,trig-integration','2024:P2:Q6:b',
    'The observed volume uses a transformed trig integral. Textbook radius expansion/identity reuse must preserve its own original region,bounds and axis;no unrelated preceding line region is imported.')
add('trapezium-prescribed-estimate,trapezium-tabulated-motion,trapezium-refinement-limitations,trapezium-exact-comparison','trapezium-chain','2023:P2:Q6:a',
    'The observed prescribed interval/ordinate estimate anchors calculation. Source data tables,refinement studies,exact comparisons and motion limitations extend the evidence beyond a single numeric estimate.')
add('trapezium-graph-bias-chain,trapezium-stationary-preparation,trapezium-complement-bias,trapezium-oscillation-aliasing,trapezium-method-investigation','trapezium-chain','2023:P2:Q6:a,2023:P2:Q6:d,2025:P2:Q4:b',
    'Observed estimate plus graph-based bias anchors comparison. Source stationary preparation,complement reversal,aliasing and counterexample investigations contain additional explicitly retained decisions;the whole investigation is not an observed exam type.')
