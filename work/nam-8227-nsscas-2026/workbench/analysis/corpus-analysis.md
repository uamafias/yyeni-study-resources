# Mathematics 8227 source and problem-family analysis

Owner: Vitalis. Author: Codex, 15 November 2026. Qualification: Namibia NSSCAS,
Grade 12, NIED December 2020 edition. This is the first author analysis of the
commissioned steps 1–3, ready for selection/source review. No recipe work orders,
generator implementation, subject acceptance or learner assignment is approved here.

## Scope and source position

The syllabus was read before paper analysis. `curriculum/syllabus-facts.json` and
`objective_registry.json` at the subject root retain the exact source identity and
page quotations. Sixty specific-objective bullets across fifteen topic containers
are decomposed into 138 proposed learner demands in `demand-registry.json`.
The numbered abilities under technique with application are retained separately;
they are not eleven independently weighted AOs. Paper 1 and Paper 2 each carry
75 marks, two hours and 50%. No standalone command-word table was found in the
complete extracted syllabus; no list or per-ability weight was invented.

The assessment corpus is both papers for 2021–2025: ten papers, 119 connected
questions and 250 labelled assessed parts. All questions were read for structural
analysis from their extracted text. Parts retain source year/component/question/
label and the pages covering the connected question. The part tariffs reconcile
to 75 per paper, 750 overall. This is a census of this corpus, not a forecast of
all possible examination questions. Native extraction scrambles some mathematics
and omits diagram relationships; not every figure/formula has yet been visually
checked or every question independently solved.

Combined DNEA reports are now present for every year 2021–2025. The 2022–2024 gaps
were resolved by inspecting public embed attributes on the NANSO listing and
passing the observed download URLs to the existing Harvester. The sources were
not downloaded through a replacement scraping system. Cover years and Mathematics
section headings were checked; the Mathematics sections contain both commentary
and, in some years, explicit award tables.

The Namibia textbook now has a complete 663-page local OCR derivative, with page
hashes and bounded confidence/position records. OCR produced heading leads on
572 pages. Those are searchable leads, not 572 independently reviewed pages.
Seventeen selected textbook samples cover all thirteen Namibia-book chapters and
two supplementary Goldie numerical-method sections. Fifteen Namibia-book samples
have exact visually checked PDF/printed/item locators; two Goldie samples were
read as native text. The remaining exercises and answers have not been exhaustively
classified. Internal source derivatives must never enter learner delivery packages.

## Curriculum and pattern records

The generated `question-analysis.json` contains each assessed part's proposed
primary objective, any other directly assessed objective links, pattern links,
tariff and source locator. These mappings are analyst judgements pending review.
NSSCO prerequisite knowledge is declared separately; incidental use does not earn
direct AS objective coverage. Part Bloom labels remain explicitly unclassified:
this source analysis does not invent criterion-reviewed recipe classifications.

`problem-patterns.json` and `selection-table.md` propose 62 broad families, 61 with
sampled examination part links and one with syllabus/textbook evidence only.
They are analysis containers, not 62 approved recipes, assignment choices or
generators. Several contain structural branches requiring separation below.
`coverage-matrix.md` exposes all sixty objectives, their proposed demand counts
and candidate part links. A missing link means no link was established by this
pass; it does not prove absence from the corpus. A link does not certify every
sub-demand, representation or level of scaffolding.

## Patterns that require structural distinctions

| Family / source examples | Required learner decision or evidence | Consequence for recipe design |
|---|---|---|
| Discriminant: 2024 P1 Q5; 2025 P1 Q1(a) | Inequality conditions on root count versus proving rational roots for an allowed parameter domain | Distinct proof/condition branches; changing coefficient values cannot turn one into the other |
| Quadratic disguise: 2021 P1 Q3; 2024 P1 Q1; 2025 P1 Q11(b) | Recover radical/exponential/original-variable roots, reject inadmissible values and use interval/sign information | Preserve the substitution and recovery demand; a quadratic answer alone is insufficient |
| Functions: 2021 P1 Q12; 2025 P1 Q7 | Domain feasibility, one-to-one restriction, inverse branch, range and paired graph are different assessed operations | Preserve connected parts and exact restrictions; standalone drills need their own justification/givens |
| Circular diagrams: 2021 P1 Q7; 2024 P1 Q7; 2025 P1 Q10 | Identify whole versus shaded region, infer contact geometry, or derive radius/area relationships | Different geometrical reasoning may justify distinct recipes/branches despite shared sector formulae |
| Optimisation: 2022 P1 Q8; 2023 P1 Q13; 2024 P1 Q11; 2025 P1 Q9 | Perimeter-to-area model versus fixed-volume-to-surface model, followed by stationarity/classification where asked | Shared calculus engine is possible, but geometry/model/marking distinctions remain explicit |
| Trig graphs: 2022 P1 Q10; 2025 P1 Q4 | Read given graph parameters versus construct graph, overlay a line and count intersections | Input asset and visual-response requirements differ; graph-reading support does not establish graph-marking support |
| Parametric curves: 2021 P2 Q7; 2022 P2 Q10; 2024 P2 Q7 | Find relevant parameter at an axis crossing, detect vertical tangent, or solve numerical parameter before gradient | Connected structure and valid derivative conditions must be preserved; do not collapse into a single gradient substitution |
| Trig integration: 2022 P2 Q7; 2025 P2 Q10 | Use a prior identity at a changed argument versus recognise a prior derivative and combine antiderivatives | Different dependency/reasoning branches; solution steps do not define a universal mark scheme |
| Modulus: 2021 P2 Q3; 2024 P2 Q11; 2025 P2 Q2 | Compare two moduli, reason from line intersections, or remove modulus after exponential equivalence | Case selection, extraneous roots and required evidence differ; cosmetic variants stay inside each reviewed branch |
| Numerical methods: 2025 P2 Q12; Goldie PDF pp164/170 | Global root count, local sign bracket, rearrangement and accurate iteration; additionally recognise failed/wrong-root convergence | Keep global/local claims distinct. Unobserved but prescribed convergence understanding remains visible |

Ordinary variation changes allowed values/context while preserving those decisions.
Representation changes become structural only when they change the evidence the
learner must supply. Generator reuse and recipe/selection identities need not have
a one-to-one relationship. Final branch/recipe counts await design review.

## Marking evidence and limits

Separate complete scheme files have not been acquired. However, the official
reports contain linked award excerpts for 22 connected questions: two in 2021 P2,
all nine in 2023 P2 and all eleven in 2024 P2. `question-analysis.json` records
their exact report pages. This is excerpt availability, not a claim that every
criterion, alternative or cap was accurately transcribed or approved.

Two visually checked examples show why a universal answer-only rule would fail:

- 2023 report PDF p331 / printed p329: P2 Q1 distinguishes division, quotient,
  remainder, factorisation and roots. The factorisation table includes method,
  accuracy and special-case treatment, and explicitly rejects three correct
  factors without working. In Q2 on the same page, the modulus parameters can
  earn the marks when placed correctly in the formula.
- 2024 report PDF p343 / printed p341: P2 Q11 allocates visual sketch marks,
  accepts alternative algebraic methods for the intersection, restricts credit
  where two solutions are reported, and specifies follow-through for part (c).
  A photograph upload alone cannot establish those sketch criteria reliably.

The 2023 report's P2 general comments on PDF p330 distinguish “hence” from “hence,
or otherwise”. Do not turn that into a global prohibition on valid alternatives:
bind method restrictions to exact question wording and memo evidence. Record
dependencies for each branch; follow-through is an award rule, not merely an arrow
from an earlier part. Explicit annotation currently covers selected dependency
edges, not an exhaustive award-dependency graph.

`examiner-difficulties.json` contains twelve cited cohort difficulties: proof
conclusions, use of earlier results, constants in motion, domain restrictions,
nonquadratic tangency, connected rates, transformed graph intercepts, integrating
rational expressions, perpendicularity, substitution recovery, trapezium bias and
chain-rule/reverse-derivative distinctions. These can justify practice design;
they do not diagnose an individual learner from a wrong final answer alone.

## Textbook contributions and holds

`textbook-samples.json` records exercise/figure locators, objective links,
representation/decision distinctions and proposed disposition. Source expression
is not approved for direct reuse. New problems/diagrams should express the mapped
concepts and preserve mathematical validity across variations.

The book adds useful leads beyond the sampled exam-family links: recognising
functions from graphs/tables/pairs; degree/radian conversion; reading 3D coordinates
with changed origin; and unit vectors after connected displacement steps. Supporting
drills require a specific learning need and selection acceptance, rather than
automatic inclusion. The moving-secant investigation supports gradient intuition;
it does not make first-principles differentiation a required assessed technique.

Goldie's discussion of failed/wrong-root convergence supplies a textbook lead for
an explicit Namibia requirement not directly linked to an examined part in this
pass. Its formal derivative convergence condition remains outside required scope.
Similarly, general trig solutions, change-of-base logs and general integration by
substitution must not enter required assessed work merely because a textbook
contains them. Applicable syllabus exclusions must remain attached to branches.

## Source and capability findings

1. **SRC-8227-DOMAIN-2022-P1-Q13:** source PDF p18, visually confirmed. The stated
   domain is positive x, but the given point has negative x. This is a source
   contradiction, not an extraction error. Hold this exemplar's exact givens;
   do not alter the official PDF or silently inherit them into a recipe.
2. **SRC-8227-TEXTBOOK-REF:** Namibia textbook PDF p550 / printed p538, Try Now 21
   Q2(c) refers to an interval in part (a), while (a) asks for a stationary point.
   Treat the reference as unresolved; inspect surrounding context/answers before
   using it. Original authored prompts should state their interval unambiguously.
3. **CAP-8227-02:** eleven examination parts explicitly require a sketch/visual
   response in this pass. Their source evidence is preserved. Reliable visual
   response assessment and feedback remain unverified in YYeni; no demand was
   weakened to fit the current interface.
4. OCR and native extraction can damage mathematical expressions. The barcode on
   textbook PDF p663 confirms ISBN 9789991696645, but source completeness and
   publication/impression cannot be established from a barcode or page count.

## Review before recipe planning

Review the sixty-bullet syllabus transcription and decomposition, all part/objective
associations, and proposed family/branch distinctions. Reconcile exact atomic demands
and source roles, including the currently unlinked objective rows. Finish detailed
exercise-family enumeration for the unreviewed textbook space and marking transcription
where excerpts exist. Recover missing schemes/verify proof/final equivalence where
possible, keeping unresolved scope explicit. Check every selected diagram/formula
visually before work orders. This package establishes a substantial first map;
it does not certify that all exercises, all potential problem types or all marking
rules have been exhausted.

Author assembly checks are in `analysis-checks.json` and `ocr-validation.json`.
They establish literal quote presence, valid references, part tariffs matching
paper brackets, paper totals and OCR page identity/completeness. Independent
mathematical/content review, owner source/analysis acceptance and application
capability acceptance remain separate, pending acts.
