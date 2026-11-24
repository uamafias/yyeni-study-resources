# Implicit gradient and normal: six worked design examples

NSSCAS Mathematics 8227, December 2020 syllabus, Grade 12. Owner Vitalis; Codex PLANNER calculus assistant; 23 November 2026. Proposed version 0.1.0. These are newly authored paper-design exemplars, not runtime learning items. Approval and independent review pending. Criteria suffixes and answer-only rules are in the matching workorder.

## gradient: normal (WB8227-implicit-normal:gradient:normal)

Question. The curve satisfies $3e^{2x}y+y^2=4$. At the point $(0,-4)$, find its gradient.  Show the working used. Proposed tariff 5; the showing-work request makes the explicit method requirements visible.

1. **Action:** differentiate the relation. **Reason:** the exponential times y needs a product rule, and y depends on x. **Result:** $6e^{2x}y+3e^{2x}y'+2yy'=0$.
2. **Action:** substitute the point. **Reason:** the requested gradient belongs to this local curve branch. **Result:** $(3+2(-4))m=-(6)(-4)$, so $m=-24/5$.

Marking: G1 M1 product attempt, G2 A1 correct product terms, G3 B1 correct $2yy\prime$ and zero constant derivative, G4 M1 point substitution, G5 A1 $-24/5$:5/5. No second allocation for rearranging the same derivative. Exact answers; no physical units.

Independent check: solve the quadratic locally as $y=(-a e^{kx}+\sigma\sqrt{a^2e^{2kx}+4C})/2$, where $\sigma=\operatorname{sign}(a+2q)$, and differentiate at zero. It gives the same m; tangent and normal slopes multiply to −1. This checks a different derivation, not a second call to a generator answer.

## gradient: changed (WB8227-implicit-normal:gradient:changed)

Question. The curve satisfies $3e^{x}y+y^2=-2$. At the point $(0,-1)$, find its gradient.  Show the working used. Proposed tariff 5; the showing-work request makes the explicit method requirements visible.

1. **Action:** differentiate the relation. **Reason:** the exponential times y needs a product rule, and y depends on x. **Result:** $3e^{x}y+3e^{x}y'+2yy'=0$.
2. **Action:** substitute the point. **Reason:** the requested gradient belongs to this local curve branch. **Result:** $(3+2(-1))m=-(3)(-1)$, so $m=3$.

Marking: G1 M1 product attempt, G2 A1 correct product terms, G3 B1 correct $2yy\prime$ and zero constant derivative, G4 M1 point substitution, G5 A1 $3$:5/5. No second allocation for rearranging the same derivative. Exact answers; no physical units.

Independent check: solve the quadratic locally as $y=(-a e^{kx}+\sigma\sqrt{a^2e^{2kx}+4C})/2$, where $\sigma=\operatorname{sign}(a+2q)$, and differentiate at zero. It gives the same m; tangent and normal slopes multiply to −1. This checks a different derivation, not a second call to a generator answer.

## gradient: boundary (WB8227-implicit-normal:gradient:boundary)

Question. The curve satisfies $4e^{3x}y+y^2=5$. At the point $(0,-5)$, find its gradient.  Show the working used. Proposed tariff 5; the showing-work request makes the explicit method requirements visible.

1. **Action:** differentiate the relation. **Reason:** the exponential times y needs a product rule, and y depends on x. **Result:** $12e^{3x}y+4e^{3x}y'+2yy'=0$.
2. **Action:** substitute the point. **Reason:** the requested gradient belongs to this local curve branch. **Result:** $(4+2(-5))m=-(12)(-5)$, so $m=-10$.

Marking: G1 M1 product attempt, G2 A1 correct product terms, G3 B1 correct $2yy\prime$ and zero constant derivative, G4 M1 point substitution, G5 A1 $-10$:5/5. No second allocation for rearranging the same derivative. Exact answers; no physical units.

Independent check: solve the quadratic locally as $y=(-a e^{kx}+\sigma\sqrt{a^2e^{2kx}+4C})/2$, where $\sigma=\operatorname{sign}(a+2q)$, and differentiate at zero. It gives the same m; tangent and normal slopes multiply to −1. This checks a different derivation, not a second call to a generator answer.

## normal: normal (WB8227-implicit-normal:normal:normal)

Question. The curve satisfies $3e^{2x}y+y^2=4$. At the point $(0,-4)$, find its gradient. Then find the normal equation at this point. Show the working used. Proposed tariff 5+2=7; the showing-work request makes the explicit method requirements visible.

1. **Action:** differentiate the relation. **Reason:** the exponential times y needs a product rule, and y depends on x. **Result:** $6e^{2x}y+3e^{2x}y'+2yy'=0$.
2. **Action:** substitute the point. **Reason:** the requested gradient belongs to this local curve branch. **Result:** $(3+2(-4))m=-(6)(-4)$, so $m=-24/5$.
3. **Action:** take the negative reciprocal and use the point. **Reason:** a normal is perpendicular to the tangent. **Result:** $y-(-4)=(5/24)x$. Equivalent standard affine forms are accepted.

Marking: G1 M1 product attempt, G2 A1 correct product terms, G3 B1 correct $2yy\prime$ and zero constant derivative, G4 M1 point substitution, G5 A1 $-24/5$:5/5. N1 M1 negative reciprocal, N2 A1 correct normal $y-(-4)=\frac{5}{24}x$:2/2. No second allocation for rearranging the same derivative. Exact answers; no physical units.

Independent check: solve the quadratic locally as $y=(-a e^{kx}+\sigma\sqrt{a^2e^{2kx}+4C})/2$, where $\sigma=\operatorname{sign}(a+2q)$, and differentiate at zero. It gives the same m; tangent and normal slopes multiply to −1. This checks a different derivation, not a second call to a generator answer.

## normal: changed (WB8227-implicit-normal:normal:changed)

Question. The curve satisfies $3e^{x}y+y^2=-2$. At the point $(0,-1)$, find its gradient. Then find the normal equation at this point. Show the working used. Proposed tariff 5+2=7; the showing-work request makes the explicit method requirements visible.

1. **Action:** differentiate the relation. **Reason:** the exponential times y needs a product rule, and y depends on x. **Result:** $3e^{x}y+3e^{x}y'+2yy'=0$.
2. **Action:** substitute the point. **Reason:** the requested gradient belongs to this local curve branch. **Result:** $(3+2(-1))m=-(3)(-1)$, so $m=3$.
3. **Action:** take the negative reciprocal and use the point. **Reason:** a normal is perpendicular to the tangent. **Result:** $y-(-1)=(-1/3)x$. Equivalent standard affine forms are accepted.

Marking: G1 M1 product attempt, G2 A1 correct product terms, G3 B1 correct $2yy\prime$ and zero constant derivative, G4 M1 point substitution, G5 A1 $3$:5/5. N1 M1 negative reciprocal, N2 A1 correct normal $y-(-1)=\frac{-1}{3}x$:2/2. No second allocation for rearranging the same derivative. Exact answers; no physical units.

Independent check: solve the quadratic locally as $y=(-a e^{kx}+\sigma\sqrt{a^2e^{2kx}+4C})/2$, where $\sigma=\operatorname{sign}(a+2q)$, and differentiate at zero. It gives the same m; tangent and normal slopes multiply to −1. This checks a different derivation, not a second call to a generator answer.

## normal: boundary (WB8227-implicit-normal:normal:boundary)

Question. The curve satisfies $4e^{3x}y+y^2=5$. At the point $(0,-5)$, find its gradient. Then find the normal equation at this point. Show the working used. Proposed tariff 5+2=7; the showing-work request makes the explicit method requirements visible.

1. **Action:** differentiate the relation. **Reason:** the exponential times y needs a product rule, and y depends on x. **Result:** $12e^{3x}y+4e^{3x}y'+2yy'=0$.
2. **Action:** substitute the point. **Reason:** the requested gradient belongs to this local curve branch. **Result:** $(4+2(-5))m=-(12)(-5)$, so $m=-10$.
3. **Action:** take the negative reciprocal and use the point. **Reason:** a normal is perpendicular to the tangent. **Result:** $y-(-5)=(1/10)x$. Equivalent standard affine forms are accepted.

Marking: G1 M1 product attempt, G2 A1 correct product terms, G3 B1 correct $2yy\prime$ and zero constant derivative, G4 M1 point substitution, G5 A1 $-10$:5/5. N1 M1 negative reciprocal, N2 A1 correct normal $y-(-5)=\frac{1}{10}x$:2/2. No second allocation for rearranging the same derivative. Exact answers; no physical units.

Independent check: solve the quadratic locally as $y=(-a e^{kx}+\sigma\sqrt{a^2e^{2kx}+4C})/2$, where $\sigma=\operatorname{sign}(a+2q)$, and differentiate at zero. It gives the same m; tangent and normal slopes multiply to −1. This checks a different derivation, not a second call to a generator answer.

## Rejected/diagnostic cases and coverage limits

Reject a=4,q=-2 (denominator zero), k=0 (exponential differentiation demand lost), q=0 (zero gradient, changes normal handling), and q=-a (constant zero enables an unintended factorisation). A point not satisfying the given curve is invalid. Do not label a zero/undefined gradient case a normal variation of this recipe.

The changed tuple has positive gradient and the boundary tuple has the largest admitted a,k,|q|. Both branches retain the same implicit/product/composite demands. Their extra normal output changes the branch's whole-question reference scope, not its gradient-part classification. Six cases checked; no runtime seed/renderer/marker tested.
