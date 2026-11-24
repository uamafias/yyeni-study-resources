# Worked design exemplar — WB8227-trig-rform-equation

NSSCAS Mathematics 8227, December 2020; Grade 12. Owner Vitalis; PLANNER Codex, 23 November 2026. Proposed version 0.1.0; owner approval and independent design review pending. These are original paper design illustrations, not runtime learner items.

All three cases belong to branch `degree-cycle`. The work order fixes the criterion IDs, credit and permitted variation. Each card keeps conversion and its hence-equation connected. Show the question before submission; all workings below are solution-reveal material. No source diagram is reused.

## Normal — positive right side

Question: (a) Express $3\sin\theta+4\cos\theta$ in the form $R\sin(\theta+\alpha)$, where $R>0$ and $0^\circ<\alpha<90^\circ$. Give $R$ exactly and $\alpha$ to two decimal places. [3] (b) Hence solve $3\sin\theta+4\cos\theta=2$ for $0^\circ<\theta<360^\circ$, giving the angles to one decimal place. [4]

1. Action: expand and compare coefficients. Reason: an identity has equal sine and cosine coefficients for every angle. Result:

   $$
   R\cos\alpha=3,\qquad R\sin\alpha=4.
   $$

2. Action: square and add, then divide the coefficient equations. Reason: $\cos^2\alpha+\sin^2\alpha=1$, and the phase must be acute. Result:

   $$
   R=5,\qquad \alpha=\tan^{-1}\!\left(\frac43\right)=53.130102\ldots^\circ.
   $$

   Display $\alpha=53.13^\circ$; retain the unrounded value for the next part. These satisfy a-B1, a-M1 and a-A1: 3 marks. A rounded displayed phase is an approximation to the identity, not a new exact coefficient.
3. Action: reduce the equation and shift its entire interval. Reason: both sine branches must be found over the interval of the transformed argument. Result:

   $$
   \sin(\theta+\alpha)=\frac25,\qquad
   53.130102\ldots^\circ<\theta+\alpha<413.130102\ldots^\circ.
   $$

   The two transformed angles are $156.421821\ldots^\circ$ and $383.578178\ldots^\circ$.
4. Action: subtract the unrounded phase and check the original equation. Reason: the question's interval is for $\theta$. Result:

   $$
   \theta=103.291719\ldots^\circ\quad\text{or}\quad330.448076\ldots^\circ.
   $$

   The final answers are $103.3^\circ$ and $330.4^\circ$. The reduction, both branches and two correct final roots satisfy b-M1, b-M2, b-A1 and b-A2: 4 marks. Total: 7 marks.

Independent checks use a direct evaluator of the original left side, not the phase answer formula; both unrounded roots give $2$ with residual below $2\times10^{-13}$. Also $3^2+4^2=25$ and $5\cos\alpha=3$, $5\sin\alpha=4$.

## Changed — negative right side

Question: (a) Express $4\sin\theta+3\cos\theta$ as $R\sin(\theta+\alpha)$ under the same positive-amplitude and acute-phase conditions. Give exact $R$ and $\alpha$ to two decimal places. [3] (b) Hence solve $4\sin\theta+3\cos\theta=-2$ for $0^\circ<\theta<360^\circ$, to one decimal place. [4]

Expand and match coefficients to give $R\cos\alpha=4$ and $R\sin\alpha=3$. Squaring/adding and dividing give

$$
R=5,\qquad \alpha=\tan^{-1}\!\left(\frac34\right)=36.869897\ldots^\circ\approx36.87^\circ.
$$

These earn the 3 conversion marks. The equation becomes

$$
\sin(\theta+\alpha)=-\frac25,\qquad
36.869897\ldots^\circ<\theta+\alpha<396.869897\ldots^\circ.
$$

Negative sine needs the third- and fourth-quadrant transformed angles $203.578178\ldots^\circ$ and $336.421821\ldots^\circ$. Subtracting the phase gives

$$
\theta=166.708280\ldots^\circ\quad\text{or}\quad299.551923\ldots^\circ.
$$

Thus the final answers are $166.7^\circ$ and $299.6^\circ$. Both satisfy the original equation and strict interval; all 4 equation marks are earned, total 7. The sign change requires a different quadrant selection, while staying within the same assessed decision. No higher Bloom level is inferred from it.

Independent substitution gives $-2$ in each case with residual below $2\times10^{-13}$.

## Admitted boundary — zero right side

Question: (a) Express $\sin\theta+\cos\theta$ as $R\sin(\theta+\alpha)$ with the same restrictions, giving exact $R$ and $\alpha$ to two decimal places. [3] (b) Hence solve $\sin\theta+\cos\theta=0$ for $0^\circ<\theta<360^\circ$, to one decimal place. [4]

Coefficient matching gives $R\cos\alpha=R\sin\alpha=1$, so $R=\sqrt2$ and $\alpha=45.00^\circ$ [a: 3]. The equation is $\sin(\theta+45^\circ)=0$, with $45^\circ<\theta+45^\circ<405^\circ$. Only $180^\circ$ and $360^\circ$ are transformed roots in that interval. Therefore

$$
\theta=135.0^\circ\quad\text{or}\quad315.0^\circ.
$$

Both exact special-angle substitutions give zero [b: 4]; total 7. The principal calculator output $0^\circ$ for the transformed angle lies outside the shifted interval.

## Excluded boundaries and response examples

The tuple $(a,b,c)=(0,1,0)$ violates the nonzero-coefficient/acute-phase invariant. The tuple $(1,1,2)$ has $|c|>R$ and no two-root solution set. The tuple $(3,4,4)$ has an excluded endpoint root, so it is outside this strict-open pilot branch. The tuple $(2,2,0)$ is a scalar duplicate of $(1,1,0)$ and fails the primitive-tuple constraint. Excluding these branch choices does not say they are illegitimate mathematical questions.

For the normal case, full conversion plus the correct reduced equation but only the root $103.3^\circ$ earns 5 of 7 marks. A complete final pair alone in part (b) earns its two accuracy marks, not unseen method marks. If both transformed angles are shown but the learner writes $103.3^\circ$ and $383.6^\circ$, b-M1/b-M2 and the first accuracy mark can be earned; the second value was not shifted back and also violates the original interval. Feedback points to those visible facts. An illegible digit requests clarification with marking pending.

Capacity is 78 primitive mathematical tuples, independently integer-counted; not 90 raw tuples or unlimited renewal. All 78 were also checked with an independent half-angle quadratic oracle, separate from the phase construction. No runtime generator, marker, learner diagram or app renderer is certified by this paper design.
