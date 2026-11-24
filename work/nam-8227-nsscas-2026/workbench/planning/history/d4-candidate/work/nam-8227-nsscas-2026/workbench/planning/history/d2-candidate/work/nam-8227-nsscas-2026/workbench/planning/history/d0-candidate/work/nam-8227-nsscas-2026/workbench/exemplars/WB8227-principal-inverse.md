# Worked design exemplar — WB8227-principal-inverse

NSSCAS Mathematics 8227, December 2020; Grade 12. Owner Vitalis; PLANNER Codex, 23 November 2026. Proposed version 0.1.0; owner approval and independent design review pending. These are original paper design illustrations, not runtime learner items.

The `admissible-linear` branch asks for an exact solution using radians, with the principal-value step [2]. The `range-obstruction` branch asks for an explanation of whether there is a real solution using the principal inverse-sine range [2]. The response formats remain different. All six questions below are newly authored; the held Namibian original is not a learner exemplar.

## Admissible-linear — normal

Question: Solve $\sin^{-1}(4x)=-\frac{\pi}{6}$ exactly, using radians and showing the principal-value step. [2]

Action: check the target angle. Reason: inverse sine returns values only in $[-\pi/2,\pi/2]$. Result: $-\pi/6$ is allowed. Taking sine is then reversible for this equation, so
$$4x=\sin\!\left(-\frac{\pi}{6}\right)=-\frac12\qquad\text{[V-M1]}.$$
Divide by four to isolate the original variable:
$$x=-\frac18\qquad\text{[V-A1]}.$$
Total: 2 marks. Independent reverse check: $4x=-1/2$ and $\sin^{-1}(-1/2)=-\pi/6$; other periodic angles are not outputs of this inverse relation.

## Admissible-linear — changed special angle

Question: Solve $\sin^{-1}(5x)=\frac{\pi}{4}$ exactly, using radians and showing the principal-value step. [2]

The target $\pi/4$ lies in the principal interval. Taking sine gives $5x=\sqrt2/2$ [M1]. Division gives
$$x=\frac{\sqrt2}{10}\qquad\text{[A1]}.$$
Total: 2. This changes the exact reference-triangle ratio as well as the scale recovery. Reverse check: $5x=\sqrt2/2$ has inverse sine $\pi/4$ uniquely. The equivalent $1/(5\sqrt2)$ is accepted; adding the negative value is not.

## Admissible-linear — admitted finite-domain boundary

Question: Solve $\sin^{-1}(5x)=\frac{\pi}{3}$ exactly, using radians and showing the principal-value step. [2]

The multiplier is at its largest admitted value and the positive target at its largest admitted non-axis value. Since $\pi/3\in[-\pi/2,\pi/2]$, taking sine gives $5x=\sqrt3/2$ [M1], so
$$x=\frac{\sqrt3}{10}\qquad\text{[A1]}.$$
The exact inverse check holds; total 2. This does not broaden the branch to a nonlinear inner expression or inverse differentiation.

## Range-obstruction — normal

Question: Explain whether $\sin^{-1}(4x)=\frac{2\pi}{3}$ has a real solution, using the principal range of inverse sine. [2]

For any real inverse-sine input, the output lies in $[-\pi/2,\pi/2]$ [X-B1]. Since $2\pi/3>\pi/2$, there is no real solution [X-B2]. Total: 2. As an independent check of a tempting wrong method, taking sine would produce $x=\sqrt3/8$, but
$$\sin^{-1}\!\left(4\cdot\frac{\sqrt3}{8}\right)=\frac{\pi}{3}\ne\frac{2\pi}{3}.$$
The forward transformation lost the range restriction; the check earns no extra mark.

## Range-obstruction — changed negative target

Question: Explain whether $\sin^{-1}(3x)=-\frac{3\pi}{4}$ has a real solution, using the principal range. [2]

The principal interval is $[-\pi/2,\pi/2]$ [B1]. Because $-3\pi/4<-\pi/2$, no real solution exists [B1]. Total: 2. The false forward-sine candidate would be $x=-\sqrt2/6$, but its inverse substitution gives $-\pi/4$, not $-3\pi/4$. This tests failure at the lower rather than upper side of the interval.

## Range-obstruction — admitted target boundary

Question: Explain whether $\sin^{-1}(5x)=\pi$ has a real solution, using the principal range. [2]

State $[-\pi/2,\pi/2]$ [B1]. The largest admitted positive obstruction target, $\pi$, lies outside it, so there is no real solution [B1]. Total: 2. Forward sine misleadingly gives $x=0$, while inverse substitution gives zero rather than $\pi$. No trigonometric evaluation is necessary for the correct explanation.

## Excluded boundaries, alternatives and partial credit

A zero multiplier is outside the unique-recovery branch. The target $\pi/2$ is mathematically valid, but outside this pilot's non-axis special-angle domain; it must not be called impossible. A degree-labelled target in a radian instance is invalid data. A principal target $\pi/4$ routed to `range-obstruction` is a branch-selection error, not a learner error.

For the normal valid case, the equivalent unreduced fraction $-2/16$ earns 2 marks. Correctly finding $4x=-1/2$ but leaving $x=-1/2$ earns 1. A correct exact final $x=-1/8$ alone earns 2 under the proposed implied-method rule; an inexact $-0.13$ cannot earn the exact accuracy mark. For the normal obstruction, 'no real solution' alone earns 1; the range without the conclusion earns 1; the forward candidate $\sqrt3/8$ without recognising the inverse-range failure earns zero. An unreadable sign triggers clarification/pending marking rather than an invented error diagnosis.

There are 24 admitted equations in each branch, 48 total. Branch maxima differ: Apply3 for exact recovery, Understand2 for the range explanation. The simple Cambridge anchor applies only to `admissible-linear`; the obstruction branch is syllabus-derived and has no learner same-type label. Cosine/tangent principal values and the axis/nonlinear facets remain explicit later work. All six examples were independently checked by exact inverse substitution or range comparison. No runtime generator, marker or app test was run.
