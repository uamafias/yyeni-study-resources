# Worked exemplar — WB8227-trig-rform-equation, D4

NSSCAS Mathematics 8227, December 2020; Grade 12. Owner Vitalis; PLANNER Codex, 24 November 2026. Proposed version 0.1.4, classification `8227-pilot-design-0.1.1`. Original stage-D paper illustrations; no runtime items. D4 repair awaits Claude’s changed-scope confirmation, then Vitalis approval.

All three cases belong to `degree-cycle`, with 7 marks each. Conversion and the hence-equation remain connected. The new normal and boundary avoid the D0 rounding and inverse-ratio collisions. All current solutions retain guard digits until their requested final accuracy. Show only each question before submission.

## Normal — positive target requiring a wrap

Question: (a) Express $2\sin\theta+3\cos\theta$ as $R\sin(\theta+\alpha)$, with $R>0$ and $0^\circ<\alpha<90^\circ$. Give exact $R$ and $\alpha$ to two decimal places. [3] (b) Hence solve $2\sin\theta+3\cos\theta=1$ for $0^\circ<\theta<360^\circ$, giving the angles to one decimal place. [4]

1. Action: expand the requested shifted sine. Reason: an identity must have matching coefficients. Result:


$$
R\cos\alpha=2,\qquad R\sin\alpha=3.
$$


2. Action: square/add and divide. Reason: $\sin^2\alpha+\cos^2\alpha=1$ and the requested phase is acute. Result:


$$
R=\sqrt{13},\quad\alpha=\tan^{-1}\!\left(\frac32\right)=56.309932\ldots^\circ\approx56.31^\circ.
$$


   The amplitude, method and phase earn a-B1/a-M1/a-A1:3 marks.
3. Action: use that result in the original equation. Reason: the “Hence” instruction requires the prior representation. Result:


$$
\sin(\theta+\alpha)=\frac1{\sqrt{13}},\quad
   56.309932\ldots^\circ<\theta+\alpha<416.309932\ldots^\circ.
$$


   The calculator principal value is $\beta=16.102113\ldots^\circ$. Since $0<\beta<\alpha$, it is outside the shifted interval. The correct transformed angles are $180^\circ-\beta=163.897886\ldots^\circ$ and $360^\circ+\beta=376.102113\ldots^\circ$.
4. Action: subtract the unrounded phase and test the original bounds. Result:


$$
\theta=107.587953\ldots^\circ\quad\text{or}\quad319.792181\ldots^\circ.
$$


   Final answers: $107.6^\circ$ and $319.8^\circ$. The reduction, shifted two-root search and both accurate roots earn b-M1/b-M2/b-A1/b-A2:4 marks. Total7.

Independent checks use the half-angle polynomial $4t^2-4t-2=0$, where $t=\tan(\theta/2)$, and direct original-equation substitution. It is separate from the phase construction; both unrounded roots give one. The alpha and beta rounding choices do not flip either final root in this normal case.

## Changed — negative target

Question: (a) Express $4\sin\theta+3\cos\theta$ as $R\sin(\theta+\alpha)$ with the same restrictions, exact $R$ and phase to two decimal places. [3] (b) Hence solve $4\sin\theta+3\cos\theta=-2$ for $0^\circ<\theta<360^\circ$, to one decimal place. [4]

Expansion gives $R\cos\alpha=4$ and $R\sin\alpha=3$. Squaring/adding and dividing give


$$
R=5,\qquad\alpha=\tan^{-1}\!\left(\frac34\right)=36.869897\ldots^\circ\approx36.87^\circ.
$$


That earns3 marks. Now use the prior representation:


$$
\sin(\theta+\alpha)=-\frac25,\qquad
36.869897\ldots^\circ<\theta+\alpha<396.869897\ldots^\circ.
$$


Here $\beta=-23.578178\ldots^\circ$. The transformed angles $180^\circ-\beta=203.578178\ldots^\circ$ and $360^\circ+\beta=336.421821\ldots^\circ$ lie in the shifted interval. Subtracting the phase gives


$$
\theta=166.708280\ldots^\circ\quad\text{or}\quad299.551923\ldots^\circ,
$$


so the final answers are $166.7^\circ$ and $299.6^\circ$. Both substitute to negative two in the original equation; all 4equation marks are earned, total7. The negative target changes the sine-branch selection without changing the Bloom proposal.

## Admitted boundary — zero target, non-symmetric coefficients

Question: (a) Express $\sin\theta+4\cos\theta$ as $R\sin(\theta+\alpha)$ with the same restrictions, exact $R$ and phase to two decimal places. [3] (b) Hence solve $\sin\theta+4\cos\theta=0$ for $0^\circ<\theta<360^\circ$, to one decimal place. [4]

Coefficient matching gives $R\cos\alpha=1$, $R\sin\alpha=4$, so


$$
R=\sqrt{17},\qquad\alpha=\tan^{-1}(4)=75.963756\ldots^\circ\approx75.96^\circ.
$$


These earn3 marks. The reduced equation is $\sin(\theta+\alpha)=0$, with $75.963756\ldots^\circ<\theta+\alpha<435.963756\ldots^\circ$. Only the transformed roots $180^\circ$ and $360^\circ$ lie inside. Hence


$$
\theta=104.036243\ldots^\circ\quad\text{or}\quad284.036243\ldots^\circ,
$$


which give $104.0^\circ$ and $284.0^\circ$ to one decimal place [4 marks]. Direct substitution cancels sine and cosine terms exactly. Total7. Unlike the retired equal-coefficient boundary, the inverted phase ratio does not give the right phase.

## Rejected cases, precision and marking evidence

The in-grid tuple $(2,3,3)$ is rejected because $c=b$ gives an excluded endpoint root. The tuple $(1,1,2)$ fails feasibility. Scalar duplicate $(2,2,0)$ fails primitive normalisation, and all equal-coefficient tuples are now excluded diagnostically: reversing the ratio would otherwise remain invisible. The eight named rounding tuples—including the retired normal $(3,4,2)$—are outside the D1pool and retained only as later negative/rounding fixtures.

For that retired rounding fixture, the exact second root $330.448076\ldots^\circ$ rounds to $330.4^\circ$, but rounding both intermediates to two decimals gives $360+23.58-53.13=330.45$, rounded to $330.5^\circ$. Valid method marks survive; that accuracy mark does not. D1’s new normal avoids this knife edge. Near-two-decimal phase cases remain explicit E/F fixtures.

Under OD-1, a bare correct amplitude/phase earns0/3 and a bare correct root pair earns0/4; feedback recognises correctness and asks for the method. Full conversion plus the correct reduced equation and only $107.6^\circ$ earns5/7. Keeping the unwrapped $-40.2^\circ$ instead of $319.8^\circ$ loses the shifted-two-root method and its missing correct-root accuracy. If the correct pair and uncancelled $-40.2^\circ$ are all submitted, the coterminal outside value counts as an extra and b-A2 is lost. A complete non-hence route earns0for(b) because no R-form SC is printed; another question’s SC1 is not imported. Ambiguous digits request clarification with marking pending.

There are58 diagnostic full tuples,12 conversion prompts,10 phase subdecisions and three root-selection classes; these are not58distinct reasoning types. No-repeat follows both assessed part keys. The independent finite-domain checker, original-equation residuals and actual rounding fixtures are saved separately; no runtime generator or marker has been run.

## D2 follow-through fixtures (not additional branch choices)

For $(a,b,c)=(1,3,2)$ with the visible wrong phase $\alpha'=\tan^{-1}(1/3)$, use $R=\sqrt{10}$. Then $\beta=\sin^{-1}(2/\sqrt{10})\approx39.2315^\circ$ and $\alpha'\approx18.4349^\circ$. Their interval contains $\beta$ and $180^\circ-\beta$, giving their roots about $20.7966^\circ$ and $122.3335^\circ$. This earns b-M1/b-M2 for their coherent hence working, not canonical root accuracy.

For $(1,2,1)$ with $\alpha'=\tan^{-1}(1/2)\approx26.5651^\circ$, the transformed roots include $z=\alpha'$ and $z=180^\circ-\alpha'$. Reject the first because it gives $\theta=0$; the sole eligible own root is about $126.8699^\circ$. Showing the full search and endpoint rejection earns b-M2. Retaining both, including zero, does not. The canonical pair remains a separate c.a.o. accuracy reference. For eligible question-data misreads only, OD-6 A/B follow-through overrides that c.a.o. restriction; an independent named method error remains uncredited.

Rounding fixtures include the changed example's $299.5519\ldots^\circ$: rounding the phase to 1 d.p. gives $299.5^\circ$, whereas two 2-d.p. intermediate angles give the tie $299.55^\circ$, which round-half-up maps to the correct $299.6^\circ$. This is an accuracy/rounding distinction, not a new quadrant misconception. See the complete admitted-tuple fixture sets in `planning/d2/trig-d2-fixtures.json`.

## D3 OD-6 fixture

In the normal question, genuinely copying coefficient $a=2$ as $4$ gives $4\sin\theta+3\cos\theta=1$. Both tasks require the same conversion and two-root shifted-interval search with no endpoint shortcut. Coherent work gives $R=5$, $\alpha=36.8698976\ldots^\circ$, then roots $131.5931433\ldots^\circ$ and $334.6670614\ldots^\circ$ (131.6 and 334.7 to 1 d.p.). Raw awards are 3/3 in (a) and 4/4 in (b), following the misread data. Deduct a-B1 once in (a): 2/3 + 4/4 = 6/7. Reusing that coefficient in (b) does not trigger another deduction. The inverted-ratio calculation in the D2 fixtures is a named method error, not a genuine copied datum: its canonical accuracy losses and own-interval method rules remain. A misread making $|c|>R$ has no MR treatment; mark the canonical task normally.

If the copied coefficient is followed by the independent inverted-ratio error $\tan\alpha=4/3$, the raw conversion has only a-B1: OD-6 deducts that earned B1 once, giving 0/3. Coherent complete root work in that wrong phase’s own interval earns b-M1/b-M2 only, 2/4; canonical-or-misread-correct accuracy is not rescued. Combined total 2/7.
