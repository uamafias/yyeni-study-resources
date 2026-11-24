# Motion — D3 fixed paper exemplars

Recipe `WB8227-motion-integration@0.1.3`; classification `8227-pilot-design-0.1.1`. Newly authored Stage-D designs. Claude confirmation then Vitalis approval pending; no runtime items. Exact or 3 significant figures, decimal half-up. D1-MR01–09 and the work-order dependencies apply. All parts require visible evidence.

## polynomial-chain: normal

Author parameters (internal): `{"A": 2, "B": 1, "u": 3, "T": 2}`. Total 6 marks.

Stem: A particle passes O at t=0 with velocity 3 m/s. Its acceleration is $4 t + 1$ m/s². (a) Find velocity in terms of t, showing integration and the initial condition. [3] (b) Find distance travelled in the first 2 seconds, in metres, showing working. Exact or 3 significant figures. [3]

| Action | Reason | Result |
|---|---|---|
| Integrate acceleration | Acceleration is dv/dt | $v=2 t^{2} + t+C$ |
| Impose v(0)=3 | Initial velocity fixes the integration constant | $C=3$, so $v=2 t^{2} + t + 3$ |
| Integrate v, evaluate both bounds | v is positive throughout, so travelled distance equals displacement | $[\frac{2 t^{3}}{3} + \frac{t^{2}}{2} + 3 t]_0^{2}=\frac{40}{3}$ m, or 13.3 m (3 s.f.) |

V1–V3 and S1–S3 give 6/6. S3 depends on S1 and S2. A correct value from differentiating velocity or a calculator, without the required integration, earns no S3. A missing initial constant loses V3; visible integration of their velocity can retain S1/S2 but not canonical S3. A bare answer earns zero; practice recognises value correctness and asks for evidence.

Independent recomputation: `planning/d3/motion-design-check.json` uses separate CAS differentiation/integration and root isolation, with numerical quadrature for the mixed branch. All exact outputs agree. This is author verification, not independent acceptance or runtime marking.

## polynomial-chain: changed

Author parameters (internal): `{"A": 1, "B": 0, "u": 1, "T": 3}`. Total 6 marks.

Stem: A particle passes O at t=0 with velocity 1 m/s. Its acceleration is $2 t$ m/s². (a) Find velocity in terms of t, showing integration and the initial condition. [3] (b) Find distance travelled in the first 3 seconds, in metres, showing working. Exact or 3 significant figures. [3]

| Action | Reason | Result |
|---|---|---|
| Integrate acceleration | Acceleration is dv/dt | $v=t^{2}+C$ |
| Impose v(0)=1 | Initial velocity fixes the integration constant | $C=1$, so $v=t^{2} + 1$ |
| Integrate v, evaluate both bounds | v is positive throughout, so travelled distance equals displacement | $[\frac{t^{3}}{3} + t]_0^{3}=12$ m, or 12 m (exact) |

V1–V3 and S1–S3 give 6/6. S3 depends on S1 and S2. A correct value from differentiating velocity or a calculator, without the required integration, earns no S3. A missing initial constant loses V3; visible integration of their velocity can retain S1/S2 but not canonical S3. A bare answer earns zero; practice recognises value correctness and asks for evidence.

Independent recomputation: `planning/d3/motion-design-check.json` uses separate CAS differentiation/integration and root isolation, with numerical quadrature for the mixed branch. All exact outputs agree. This is author verification, not independent acceptance or runtime marking.

## polynomial-chain: boundary

Author parameters (internal): `{"A": 3, "B": 2, "u": 4, "T": 4}`. Total 6 marks.

Stem: A particle passes O at t=0 with velocity 4 m/s. Its acceleration is $6 t + 2$ m/s². (a) Find velocity in terms of t, showing integration and the initial condition. [3] (b) Find distance travelled in the first 4 seconds, in metres, showing working. Exact or 3 significant figures. [3]

| Action | Reason | Result |
|---|---|---|
| Integrate acceleration | Acceleration is dv/dt | $v=3 t^{2} + 2 t+C$ |
| Impose v(0)=4 | Initial velocity fixes the integration constant | $C=4$, so $v=3 t^{2} + 2 t + 4$ |
| Integrate v, evaluate both bounds | v is positive throughout, so travelled distance equals displacement | $[t^{3} + t^{2} + 4 t]_0^{4}=96$ m, or 96 m (exact) |

V1–V3 and S1–S3 give 6/6. S3 depends on S1 and S2. A correct value from differentiating velocity or a calculator, without the required integration, earns no S3. A missing initial constant loses V3; visible integration of their velocity can retain S1/S2 but not canonical S3. A bare answer earns zero; practice recognises value correctness and asks for evidence.

Independent recomputation: `planning/d3/motion-design-check.json` uses separate CAS differentiation/integration and root isolation, with numerical quadrature for the mixed branch. All exact outputs agree. This is author verification, not independent acceptance or runtime marking.

## exponential-positive: normal

Author parameters (internal): `{"V": 12, "k": "1/2", "T": 2}`. Total 5 marks.

Stem: The particle has velocity $v=12 e^{- \frac{t}{2}}$ m/s. (a) Find acceleration at time t, showing differentiation. [2] (b) Find distance travelled in the first 2 seconds in metres, showing integration and boundary evaluation; exact or 3 significant figures. [3]

| Action | Reason | Result |
|---|---|---|
| Differentiate the velocity | The chain multiplier is $- \frac{1}{2}$ and the exponential index stays unchanged | $a=- 6 e^{- \frac{t}{2}}$ m/s² |
| Integrate velocity | Integration needs the reciprocal chain factor | $F(t)=- 24 e^{- \frac{t}{2}}$ |
| Evaluate F(2)−F(0) | Velocity stays positive; both bounds matter | $d=24 - \frac{24}{e}$ m = 15.2 m (3 s.f.) |

E1–E5 give 5/5. Alternatively determine an integration constant from d(0)=0, then evaluate at T; fill the same awards, do not add them. A primitive coefficient used as a derivative is excluded at E2. Bounds substituted into the original velocity/derivative do not earn E4. Omitting the lower boundary retains E3 alone. OD-6 sample: copying V=12 as 21 preserves the object/difficulty. Correct working on that datum earns E1/E2 then MR−1 from E1 (1/2); E3/E4/E5 follow through with no second deduction (3/3), total 4/5. Wrong working and answer-only restrictions still apply.

Independent recomputation: `planning/d3/motion-design-check.json` uses separate CAS differentiation/integration and root isolation, with numerical quadrature for the mixed branch. All exact outputs agree. This is author verification, not independent acceptance or runtime marking.

## exponential-positive: changed

Author parameters (internal): `{"V": 18, "k": "1/3", "T": 3}`. Total 5 marks.

Stem: The particle has velocity $v=18 e^{- \frac{t}{3}}$ m/s. (a) Find acceleration at time t, showing differentiation. [2] (b) Find distance travelled in the first 3 seconds in metres, showing integration and boundary evaluation; exact or 3 significant figures. [3]

| Action | Reason | Result |
|---|---|---|
| Differentiate the velocity | The chain multiplier is $- \frac{1}{3}$ and the exponential index stays unchanged | $a=- 6 e^{- \frac{t}{3}}$ m/s² |
| Integrate velocity | Integration needs the reciprocal chain factor | $F(t)=- 54 e^{- \frac{t}{3}}$ |
| Evaluate F(3)−F(0) | Velocity stays positive; both bounds matter | $d=54 - \frac{54}{e}$ m = 34.1 m (3 s.f.) |

E1–E5 give 5/5. Alternatively determine an integration constant from d(0)=0, then evaluate at T; fill the same awards, do not add them. A primitive coefficient used as a derivative is excluded at E2. Bounds substituted into the original velocity/derivative do not earn E4. Omitting the lower boundary retains E3 alone. OD-6 sample: copying V=18 as 81 preserves the object/difficulty. Correct working on that datum earns E1/E2 then MR−1 from E1 (1/2); E3/E4/E5 follow through with no second deduction (3/3), total 4/5. Wrong working and answer-only restrictions still apply.

Independent recomputation: `planning/d3/motion-design-check.json` uses separate CAS differentiation/integration and root isolation, with numerical quadrature for the mixed branch. All exact outputs agree. This is author verification, not independent acceptance or runtime marking.

## exponential-positive: boundary

Author parameters (internal): `{"V": 30, "k": "1/4", "T": 4}`. Total 5 marks.

Stem: The particle has velocity $v=30 e^{- \frac{t}{4}}$ m/s. (a) Find acceleration at time t, showing differentiation. [2] (b) Find distance travelled in the first 4 seconds in metres, showing integration and boundary evaluation; exact or 3 significant figures. [3]

| Action | Reason | Result |
|---|---|---|
| Differentiate the velocity | The chain multiplier is $- \frac{1}{4}$ and the exponential index stays unchanged | $a=- \frac{15 e^{- \frac{t}{4}}}{2}$ m/s² |
| Integrate velocity | Integration needs the reciprocal chain factor | $F(t)=- 120 e^{- \frac{t}{4}}$ |
| Evaluate F(4)−F(0) | Velocity stays positive; both bounds matter | $d=120 - \frac{120}{e}$ m = 75.9 m (3 s.f.) |

E1–E5 give 5/5. Alternatively determine an integration constant from d(0)=0, then evaluate at T; fill the same awards, do not add them. A primitive coefficient used as a derivative is excluded at E2. Bounds substituted into the original velocity/derivative do not earn E4. Omitting the lower boundary retains E3 alone. OD-6 sample: copying V=30 as 36 preserves the object/difficulty. Correct working on that datum earns E1/E2 then MR−1 from E1 (1/2); E3/E4/E5 follow through with no second deduction (3/3), total 4/5. Wrong working and answer-only restrictions still apply.

Independent recomputation: `planning/d3/motion-design-check.json` uses separate CAS differentiation/integration and root isolation, with numerical quadrature for the mixed branch. All exact outputs agree. This is author verification, not independent acceptance or runtime marking.

## interior-reversal: normal

Author parameters (internal): `{"k": 2, "r": 1, "c": 1, "T": 3}`. Total 6 marks.

Stem: A particle has velocity $v=2 t^{2} - 2$ m/s for $0\le t\le 3$, with the positive direction stated. (a) Find total distance travelled in metres and justify your working. [4] (b) Find signed displacement in metres, showing working; exact or 3 significant figures. [2] Neither title nor stem tells the learner whether direction changes.

| Action | Reason | Result |
|---|---|---|
| Solve v=0 and compare roots with the interval | Decide whether distance needs one or two sign-constant legs | Roots [-1, 1]; Only 1 lies inside the interval; signs change there |
| Integrate the expanded velocity | Quadratic velocity needs a cubic primitive; endpoint triangles are not exact | $F(t)=\frac{2 t^{3}}{3} - 2 t$ |
| Evaluate each selected leg with both bounds | Travelled length adds nonnegative leg magnitudes | Signed legs $- \frac{4}{3}$ m, $\frac{40}{3}$ m; distance $\frac{44}{3}$ m |
| Add signed legs, or integrate over the complete interval | Displacement retains direction rather than taking magnitudes | $12$ m |

Distance earns R1–R4=4/4; displacement R5/R6=2/2. R1 allows a coherent visible root solve/check (one slip permitted), or a complete correct constant-sign proof; these are exclusive routes. R3 follows through that credible root only with an attempted primitive and both bounds. R4 depends on R2/R3 and www. A one-slip false interior root in a no-change case loses R4 even if the number coincides: 3/4. A correctly justified harmless extra partition may earn 4/4. A root check plus numerical quadrature legs without a primitive earns R1 only. Reusing the part-(a) primitive, or adding signed legs evaluated from an attempted primitive with both bounds, is valid for R5. Calculator legs alone earn 0/2 on displacement. A guessed split or an unchecked |net integral| cannot stand in for R1/R3 even if its value coincides.

Independent recomputation: `planning/d3/motion-design-check.json` uses separate CAS differentiation/integration and root isolation, with numerical quadrature for the mixed branch. All exact outputs agree. This is author verification, not independent acceptance or runtime marking.

## interior-reversal: changed

Author parameters (internal): `{"k": -1, "r": 4, "c": 1, "T": 3}`. Total 6 marks.

Stem: A particle has velocity $v=- t^{2} + 3 t + 4$ m/s for $0\le t\le 3$, with the positive direction stated. (a) Find total distance travelled in metres and justify your working. [4] (b) Find signed displacement in metres, showing working; exact or 3 significant figures. [2] Neither title nor stem tells the learner whether direction changes.

| Action | Reason | Result |
|---|---|---|
| Solve v=0 and compare roots with the interval | Decide whether distance needs one or two sign-constant legs | Roots [-1, 4]; Both roots lie outside (0,3); v stays positive throughout |
| Integrate the expanded velocity | Quadratic velocity needs a cubic primitive; endpoint triangles are not exact | $F(t)=- \frac{t^{3}}{3} + \frac{3 t^{2}}{2} + 4 t$ |
| Evaluate each selected leg with both bounds | Travelled length adds nonnegative leg magnitudes | Signed legs $\frac{33}{2}$ m; distance $\frac{33}{2}$ m |
| Add signed legs, or integrate over the complete interval | Displacement retains direction rather than taking magnitudes | $\frac{33}{2}$ m |

Distance earns R1–R4=4/4; displacement R5/R6=2/2. R1 allows a coherent visible root solve/check (one slip permitted), or a complete correct constant-sign proof; these are exclusive routes. R3 follows through that credible root only with an attempted primitive and both bounds. R4 depends on R2/R3 and www. A one-slip false interior root in a no-change case loses R4 even if the number coincides: 3/4. A correctly justified harmless extra partition may earn 4/4. A root check plus numerical quadrature legs without a primitive earns R1 only. Reusing the part-(a) primitive, or adding signed legs evaluated from an attempted primitive with both bounds, is valid for R5. Calculator legs alone earn 0/2 on displacement. A guessed split or an unchecked |net integral| cannot stand in for R1/R3 even if its value coincides.

Independent recomputation: `planning/d3/motion-design-check.json` uses separate CAS differentiation/integration and root isolation, with numerical quadrature for the mixed branch. All exact outputs agree. This is author verification, not independent acceptance or runtime marking.

## interior-reversal: boundary

Author parameters (internal): `{"k": 3, "r": 3, "c": 3, "T": 4}`. Total 6 marks.

Stem: A particle has velocity $v=3 t^{2} - 27$ m/s for $0\le t\le 4$, with the positive direction stated. (a) Find total distance travelled in metres and justify your working. [4] (b) Find signed displacement in metres, showing working; exact or 3 significant figures. [2] Neither title nor stem tells the learner whether direction changes.

| Action | Reason | Result |
|---|---|---|
| Solve v=0 and compare roots with the interval | Decide whether distance needs one or two sign-constant legs | Roots [-3, 3]; Only 3 lies inside the interval; signs change there |
| Integrate the expanded velocity | Quadratic velocity needs a cubic primitive; endpoint triangles are not exact | $F(t)=t^{3} - 27 t$ |
| Evaluate each selected leg with both bounds | Travelled length adds nonnegative leg magnitudes | Signed legs $-54$ m, $10$ m; distance $64$ m |
| Add signed legs, or integrate over the complete interval | Displacement retains direction rather than taking magnitudes | $-44$ m |

Distance earns R1–R4=4/4; displacement R5/R6=2/2. R1 allows a coherent visible root solve/check (one slip permitted), or a complete correct constant-sign proof; these are exclusive routes. R3 follows through that credible root only with an attempted primitive and both bounds. R4 depends on R2/R3 and www. A one-slip false interior root in a no-change case loses R4 even if the number coincides: 3/4. A correctly justified harmless extra partition may earn 4/4. A root check plus numerical quadrature legs without a primitive earns R1 only. Reusing the part-(a) primitive, or adding signed legs evaluated from an attempted primitive with both bounds, is valid for R5. Calculator legs alone earn 0/2 on displacement. A guessed split or an unchecked |net integral| cannot stand in for R1/R3 even if its value coincides.

Independent recomputation: `planning/d3/motion-design-check.json` uses separate CAS differentiation/integration and root isolation, with numerical quadrature for the mixed branch. All exact outputs agree. This is author verification, not independent acceptance or runtime marking.
