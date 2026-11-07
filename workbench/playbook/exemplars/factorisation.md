# Factorisation: complete design exemplar

Owner design accepted by Jeremy, 7 November 2026. Claude's 7 November closure
review accepted the exemplar for the generic playbook design, with the subject
marking caveats below retained. It does not register another
recipe, implement a generator or approve a subject release. Read the
[workflow](../README.md), [work-order template](../templates.md) and [quality gates](../quality.md).

## Sources and limits

Paths are relative to yyeni-study-resources, not a machine-specific application root.

| Authority | Exact path and locator | Evidence |
|---|---|---|
| Syllabus | `Syllabi/Namibian Curricula/NSSCO (New)/NSSCO_Mathematics_syllabus.pdf`; NIED 2018/code 6131, printed/PDF p18 section (b); Topic 6 heading on p17; assessment pp27–28 | Common-factor extraction and difference-of-squares factorisation are specified |
| Paper | `Question Banks/Namibian Curricula/NSSCO (New)/Mathematics/2023/Ordinary - Mathematics Paper 2 6131-2 - First Revised Proof 21.03.2023.pdf`; printed/PDF p4, Q4(b), 3 marks | A complete-factorisation task combines common factor and difference of squares; explicitly a revised proof |
| Report and embedded marking table | `Question Banks/Namibian Examiner Reports/NSSCO (New) /2023/Examiners Report NSSCO 2023.pdf`; Mathematics 6131 Paper 2 Q4, printed pp580–581 / PDF pp582–583 | Learners stop after common-factor extraction or lose the factor; table provides method/special-case awards |

Source SHA-256 values in table order:

```text
e930d3cb57c36be9967db72c68445d46233dcca0e1cfefc3d08cf738d8263388
8510affcaa55cf99eff4ebf23d1e6749ffa934e217e210de62f3f1a7b362f7ea
f9abfa704d1525e5cab63ddefa8cb674e6e6936dc1df68f51a76457913a80773
```

No standalone matching mark-scheme PDF was found in the scoped local search.
Use the report's actual table, not an invented document. The proof and table match,
but final-paper confirmation and adapted-rule ambiguities remain subject to source
review before release. No frequency/whole-syllabus claim follows from one pattern.
The first Claude review inspected p18, proof p4 and report PDF pp582–583; it
recomputed the three original examples by hand. It did not independently close
the marking adaptations or inspect the new boundary cases below.

## Analysis decision and economy

Include the demand of completely factorising a two-variable expression requiring
a numerical common factor and then a difference of squares. These are successive
decisions in one pattern, not two obligatory new recipes. Existing common-factor
and difference-of-squares recipes must be audited before reuse/extension/new
authoring is chosen. An extension changes version and undergoes re-review;
saved learner evidence never changes. This example does not assume new-question
version pinning for old decks has already been implemented.

Q4(b) supplies all its givens and does not use Q4(a)'s substitution result or
Q4(c)'s separate fraction. This justifies the focused task; a shared algebra topic
is not itself a multipart dependency. Fractions require their own pattern decision.
For genuinely connected parts, keep the full task. A future split must identify
the discriminating learner decision and separately justified practice need.

## Original learner task

Factorise completely: $18x^2 - 50y^2$. [3]

Use new coefficients and necessary mathematical terminology, not copied exam prose.
The purpose is to recognise both stages and preserve equivalence throughout.

| Action | Reason | Result |
|---|---|---|
| Extract the highest common numerical factor, 2 | Keep the factor outside so the value of the expression is unchanged | $2(9x^2 - 25y^2)$ |
| Identify the squared terms | $9x^2 = (3x)^2$ and $25y^2 = (5y)^2$ | $2[(3x)^2 - (5y)^2]$ |
| Apply $A^2 - B^2 = (A - B)(A + B)$ | Opposite signs make the cross terms cancel | $2(3x - 5y)(3x + 5y)$ |

Expanding the final result returns $18x^2 - 50y^2$. Three explanatory steps do
not define three marking points automatically.

## Variation and explicit illustrative boundaries

Use the same intended decisions with different valid coefficients:

| Case | Question expression | Complete result |
|---|---|---|
| Normal | $18x^2 - 50y^2$ | $2(3x - 5y)(3x + 5y)$ |
| Fresh variant | $48x^2 - 75y^2$ | $3(4x - 5y)(4x + 5y)$ |
| Further variant | $20x^2 - 45y^2$ | $5(2x - 3y)(2x + 3y)$ |
| Small admitted boundary | $8x^2 - 18y^2$ | $2(2x - 3y)(2x + 3y)$ |
| Upper coefficient boundary | $125x^2 - 80y^2$ | $5(5x - 4y)(5x + 4y)$ |

For this **finite design illustration only**, declare
$k(a^2x^2 - b^2y^2)$ with integers $2 \leq k \leq 5$,
$2 \leq a,b \leq 5$ and $\gcd(a,b)=1$. This leaves 40 ordered parameter choices,
all requiring a common factor and two distinct squared terms; the largest
coefficient is 125. These bounds make boundary reasoning auditable. They are
author-chosen, NOT a corpus-established production difficulty range. Before any
real release, calibrate coefficient bounds and complexity against the accepted
corpus and independently review the resulting domain. Do not infer them from one paper.

Excluded checks: $k=1$ removes the first decision; $a=0$ removes a term; negative
or noninteger domain values leave this declared branch; non-coprime $a,b$ mean
$k$ is not the highest common factor; a plus sign creates a different task.
Grouping, fractions, trinomial and non-square forms need separate analysis; not
every producible expression belongs here. These variants share one recipe and
may reuse existing machinery. No generator is being built in this exercise.

Exhaustion of the finite illustration must be disclosed; another attempt is
available, but no claim of unlimited unseen instances is justified. Never silently
recycle a seen item while calling it fresh.

## Proposed marking: answer-only and alternatives explicit

The source task has three marks, with common-factor method credit and a two-mark
binomial stage plus special cases. The new coefficients require an adapted memo,
not a claim of official approval. The source's special-case list has a potentially
ambiguous printed alternative; do not silently correct or generalise it. A reviewer
must resolve exact award dependencies/precedence before an assignable release.

**Answer-only rule for this proposed recipe:** a correct completely factorised
expression demonstrates the requested product structure and earns full credit
without additional prose. This is not a universal method-mark rule. A numerical
answer in another recipe may leave method evidence absent; its work order must
state the appropriate rule and source basis instead of copying this one.

| Submitted evidence | Adapted proposal, not release-approved | Feedback focus |
|---|---|---|
| $2(3x - 5y)(3x + 5y)$, equivalent valid ordering/sign form | 3/3 | Complete correct factorisation; no invented repair |
| $2(9x^2 - 25y^2)$ and stops | 1/3 | Preserve correct extraction; recognise the remaining difference of squares |
| $(3x - 5y)(3x + 5y)$ with outer factor lost | Proposed 2/3 from binomial-stage credit; dependence on common-factor award must be independently confirmed | Retain valid bracket work; restore 2 to preserve equivalence |
| $2(3x - 5y)(3x - 5y)$ | Proposed special-case 2/3, interpreted from a listed same-sign source case; confirm interpretation | Opposite signs are needed for cancellation |
| $(6x - 10y)(3x + 5y)$ | Proposed special-case 2/3 from the source's redistributed-factor case | Equivalent product, but a numerical factor remains inside one bracket |
| Unexplained wrong answer | Only supported achievements earn credit; do not infer an unseen method | Ask for the calculation if its cause cannot be determined |
| Unreadable or contradictory evidence | Unresolved for clarification/review, not a fabricated reliable mark | Say what needs clarifying |

Special-case awards are alternative total awards, never added on top of overlapping
method credit. Cap at three and declare precedence in the reviewed memo. Equivalent
bracket order/sign handling must be tested; algebraic equivalence alone does not
establish complete factorisation when a numerical common factor remains inside.

## Support, feedback and independent application

Before practice submission, optional answer-free hints ask the learner to inspect
the coefficients for a common factor, then the remaining terms for a known pattern.
A worked example uses different values. The current answer/solution is unavailable
until submission. Record support used; preserve original work.

After the learner submits $2(9x^2 - 25y^2)$, sample feedback is:

> You correctly took out the common factor 2. Both terms inside the bracket are
> squares, so you can factorise further. Use opposite-sign brackets and keep the
> 2 outside.

Post-submission repair makes the action/reason/result concrete: identify $3x$ and
$5y$ as the squared quantities' bases; explain why opposite signs cancel cross
terms; show $2(3x - 5y)(3x + 5y)$. The separate canonical solution stays authoritative.
If the outer 2 was lost, recognise the correct brackets and repair equivalence;
do not invent a different misconception or overwrite the learner's response.

The learner may try $48x^2 - 75y^2$ without passing first. A first-attempt fully
correct response on that unseen instance, without optional support, is recorded
as **one independent observation of the intended two-stage performance**. A
correction of the old question is a different observation. Neither alone proves
mastery or measured learning effectiveness. Existing next-card/test unlock rules remain.

In Workbench Test, preserve no-support answering and question-by-question
post-submission solution/feedback review with existing timer rules. A later
instance after this feedback is after-feedback evidence, not a claim of an
entirely unaided round. Both modes use the same accepted memo.

## Remaining acceptance limits

Owner acceptance covered the intended design and generation-time text standard.
Author checking covers algebra, declared finite-domain boundaries and document
consistency. Independent playbook closure is complete; actual recipe release
acceptance of the marking interpretations remains pending. Full corpus selection, existing-recipe/domain audit,
rendered interface proof, generator tests and operational validation remain later
work. No new content is registered or assigned by this document.
