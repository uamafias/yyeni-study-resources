# Motion integration — D1 worked paper exemplars

Recipe `WB8227-motion-integration@0.1.1`. Newly authored design examples, not runtime instances. Claude short check then Vitalis approval pending. All parts require working under D1-MR01. See the work order for fully qualified criteria, partial credit and unit/precision rules.

## polynomial-chain: normal

Parameters: `{"A": 2, "B": 1, "u": 3, "T": 2}`. Total 6 marks.

Stem: acceleration is $a=4t+1$ m/s² and initial velocity 3 m/s. The particle passes O at t=0. Find velocity in terms of t; then distance travelled in the first 2 seconds in metres. Show your working; exact or 3 significant figures.

| Action | Reason | Result |
|---|---|---|
| Integrate acceleration | a=dv/dt | $v=2t^2+1t+C$ |
| Impose v(0)=3 | Integration constant must satisfy the given initial condition | $C=3$, so $v=2t^2+1t+3$ |
| Integrate velocity from 0 to 2 | Velocity stays positive, so distance equals displacement | $d=[2t^3/3+1t^2/2+3t]_0^{2}=40/3$ m, or 13.3 m (3 s.f.) |

Full work earns V1–V3 and S1–S3, 6/6. A bare correct velocity/distance earns 0/6; practice confirms the values and requests integration and initial-condition evidence. Omitting u loses V3; visible subsequent integration may retain S1/S2, not canonical S3.

Oracle: `planning/d1/motion-design-check.json` independently integrates/differentiates the source functions; exponential and quadratic-distance cases also agree with numerical quadrature. This is author verification, not independent vendor acceptance.

## polynomial-chain: changed

Parameters: `{"A": 1, "B": 0, "u": 1, "T": 3}`. Total 6 marks.

Stem: acceleration is $a=2t+0$ m/s² and initial velocity 1 m/s. The particle passes O at t=0. Find velocity in terms of t; then distance travelled in the first 3 seconds in metres. Show your working; exact or 3 significant figures.

| Action | Reason | Result |
|---|---|---|
| Integrate acceleration | a=dv/dt | $v=1t^2+0t+C$ |
| Impose v(0)=1 | Integration constant must satisfy the given initial condition | $C=1$, so $v=1t^2+0t+1$ |
| Integrate velocity from 0 to 3 | Velocity stays positive, so distance equals displacement | $d=[1t^3/3+0t^2/2+1t]_0^{3}=12$ m (exact) |

Full work earns V1–V3 and S1–S3, 6/6. A bare correct velocity/distance earns 0/6; practice confirms the values and requests integration and initial-condition evidence. Omitting u loses V3; visible subsequent integration may retain S1/S2, not canonical S3.

Oracle: `planning/d1/motion-design-check.json` independently integrates/differentiates the source functions; exponential and quadratic-distance cases also agree with numerical quadrature. This is author verification, not independent vendor acceptance.

## polynomial-chain: boundary

Parameters: `{"A": 3, "B": 2, "u": 4, "T": 4}`. Total 6 marks.

Stem: acceleration is $a=6t+2$ m/s² and initial velocity 4 m/s. The particle passes O at t=0. Find velocity in terms of t; then distance travelled in the first 4 seconds in metres. Show your working; exact or 3 significant figures.

| Action | Reason | Result |
|---|---|---|
| Integrate acceleration | a=dv/dt | $v=3t^2+2t+C$ |
| Impose v(0)=4 | Integration constant must satisfy the given initial condition | $C=4$, so $v=3t^2+2t+4$ |
| Integrate velocity from 0 to 4 | Velocity stays positive, so distance equals displacement | $d=[3t^3/3+2t^2/2+4t]_0^{4}=96$ m (exact) |

Full work earns V1–V3 and S1–S3, 6/6. A bare correct velocity/distance earns 0/6; practice confirms the values and requests integration and initial-condition evidence. Omitting u loses V3; visible subsequent integration may retain S1/S2, not canonical S3.

Oracle: `planning/d1/motion-design-check.json` independently integrates/differentiates the source functions; exponential and quadratic-distance cases also agree with numerical quadrature. This is author verification, not independent vendor acceptance.

## exponential-positive: normal

Parameters: `{"V": 12, "k": "1/2", "T": 2}`. Total 5 marks.

Stem: $v=12e^{-(1/2)t}$ m/s. Find acceleration with differentiation working, then distance in the first 2 seconds in metres, showing integration and boundaries. Exact or 3 significant figures.

| Action | Reason | Result |
|---|---|---|
| Differentiate v | Chain rule multiplies by −k; exponential index stays the same | $- 6 e^{- \frac{t}{2}}$ m/s² |
| Integrate v | Reciprocal chain factor is needed | $F(t)=-(12/(1/2))e^{-(1/2)t}$ |
| Evaluate F(2)−F(0) | Positive velocity; both boundaries count | $24 - \frac{24}{e}$ = 15.2 m (3 s.f.) |

Full work earns E1–E5, 5/5. Alternative: include C, impose d(0)=0, then evaluate d(T); it fills the same E3/E4/E5 awards. Omitting the lower boundary retains E3 only. A primitive coefficient used as the derivative fails E2 as well as E1. Bare values earn zero.

Oracle: `planning/d1/motion-design-check.json` independently integrates/differentiates the source functions; exponential and quadratic-distance cases also agree with numerical quadrature. This is author verification, not independent vendor acceptance.

## exponential-positive: changed

Parameters: `{"V": 18, "k": "1/3", "T": 3}`. Total 5 marks.

Stem: $v=18e^{-(1/3)t}$ m/s. Find acceleration with differentiation working, then distance in the first 3 seconds in metres, showing integration and boundaries. Exact or 3 significant figures.

| Action | Reason | Result |
|---|---|---|
| Differentiate v | Chain rule multiplies by −k; exponential index stays the same | $- 6 e^{- \frac{t}{3}}$ m/s² |
| Integrate v | Reciprocal chain factor is needed | $F(t)=-(18/(1/3))e^{-(1/3)t}$ |
| Evaluate F(3)−F(0) | Positive velocity; both boundaries count | $54 - \frac{54}{e}$ = 34.1 m (3 s.f.) |

Full work earns E1–E5, 5/5. Alternative: include C, impose d(0)=0, then evaluate d(T); it fills the same E3/E4/E5 awards. Omitting the lower boundary retains E3 only. A primitive coefficient used as the derivative fails E2 as well as E1. Bare values earn zero.

Oracle: `planning/d1/motion-design-check.json` independently integrates/differentiates the source functions; exponential and quadratic-distance cases also agree with numerical quadrature. This is author verification, not independent vendor acceptance.

## exponential-positive: boundary

Parameters: `{"V": 30, "k": "1/4", "T": 4}`. Total 5 marks.

Stem: $v=30e^{-(1/4)t}$ m/s. Find acceleration with differentiation working, then distance in the first 4 seconds in metres, showing integration and boundaries. Exact or 3 significant figures.

| Action | Reason | Result |
|---|---|---|
| Differentiate v | Chain rule multiplies by −k; exponential index stays the same | $- \frac{15 e^{- \frac{t}{4}}}{2}$ m/s² |
| Integrate v | Reciprocal chain factor is needed | $F(t)=-(30/(1/4))e^{-(1/4)t}$ |
| Evaluate F(4)−F(0) | Positive velocity; both boundaries count | $120 - \frac{120}{e}$ = 75.9 m (3 s.f.) |

Full work earns E1–E5, 5/5. Alternative: include C, impose d(0)=0, then evaluate d(T); it fills the same E3/E4/E5 awards. Omitting the lower boundary retains E3 only. A primitive coefficient used as the derivative fails E2 as well as E1. Bare values earn zero.

Oracle: `planning/d1/motion-design-check.json` independently integrates/differentiates the source functions; exponential and quadratic-distance cases also agree with numerical quadrature. This is author verification, not independent vendor acceptance.

## interior-reversal: normal

Parameters: `{"k": 2, "r": 1, "c": 1, "tail": 2, "T": 3}`. Total 6 marks.

Stem: a particle has velocity $v=2t^2+(0)t+(-2)$ m/s on $0\le t\le 3$, with the positive direction stated. Find (a) total distance travelled and justify the method, then (b) signed displacement, in metres. Show working; exact or 3 s.f. The learner stem supplies neither root nor reversal cue.

| Action | Reason | Result |
|---|---|---|
| Solve v=0 and test signs | Need travelled length, not net change | Roots 1 and −1; only 1 is in the interval; sign reverses there |
| Integrate the expanded quadratic | Curved velocity cannot be replaced by straight-line triangles | Primitive $\frac{2 t^{3}}{3} - 2 t$ |
| Evaluate each bounded leg | Absolute lengths add | Signed legs -4/3 m and 40/3 m; total 44/3 m |
| Evaluate the signed full integral | Displacement retains direction | 12 m |

Distance R1–R4 gives 4/4, displacement R5–R6 gives 2/2. A correct primitive and signed integral presented as total distance can earn R2 but loses R3/R4; R1 needs an actual root/sign decision. The separately labelled displacement can earn its own marks. An answer list without working earns zero.

Oracle: `planning/d1/motion-design-check.json` independently integrates/differentiates the source functions; exponential and quadratic-distance cases also agree with numerical quadrature. This is author verification, not independent vendor acceptance.

## interior-reversal: changed

Parameters: `{"k": -1, "r": 2, "c": 1, "tail": 3, "T": 5}`. Total 6 marks.

Stem: a particle has velocity $v=-1t^2+(1)t+(2)$ m/s on $0\le t\le 5$, with the positive direction stated. Find (a) total distance travelled and justify the method, then (b) signed displacement, in metres. Show working; exact or 3 s.f. The learner stem supplies neither root nor reversal cue.

| Action | Reason | Result |
|---|---|---|
| Solve v=0 and test signs | Need travelled length, not net change | Roots 2 and −1; only 2 is in the interval; sign reverses there |
| Integrate the expanded quadratic | Curved velocity cannot be replaced by straight-line triangles | Primitive $- \frac{t^{3}}{3} + \frac{t^{2}}{2} + 2 t$ |
| Evaluate each bounded leg | Absolute lengths add | Signed legs 10/3 m and -45/2 m; total 155/6 m |
| Evaluate the signed full integral | Displacement retains direction | -115/6 m |

Distance R1–R4 gives 4/4, displacement R5–R6 gives 2/2. A correct primitive and signed integral presented as total distance can earn R2 but loses R3/R4; R1 needs an actual root/sign decision. The separately labelled displacement can earn its own marks. An answer list without working earns zero.

Oracle: `planning/d1/motion-design-check.json` independently integrates/differentiates the source functions; exponential and quadratic-distance cases also agree with numerical quadrature. This is author verification, not independent vendor acceptance.

## interior-reversal: boundary

Parameters: `{"k": 3, "r": 3, "c": 3, "tail": 1, "T": 4}`. Total 6 marks.

Stem: a particle has velocity $v=3t^2+(0)t+(-27)$ m/s on $0\le t\le 4$, with the positive direction stated. Find (a) total distance travelled and justify the method, then (b) signed displacement, in metres. Show working; exact or 3 s.f. The learner stem supplies neither root nor reversal cue.

| Action | Reason | Result |
|---|---|---|
| Solve v=0 and test signs | Need travelled length, not net change | Roots 3 and −3; only 3 is in the interval; sign reverses there |
| Integrate the expanded quadratic | Curved velocity cannot be replaced by straight-line triangles | Primitive $t^{3} - 27 t$ |
| Evaluate each bounded leg | Absolute lengths add | Signed legs -54 m and 10 m; total 64 m |
| Evaluate the signed full integral | Displacement retains direction | -44 m |

Distance R1–R4 gives 4/4, displacement R5–R6 gives 2/2. A correct primitive and signed integral presented as total distance can earn R2 but loses R3/R4; R1 needs an actual root/sign decision. The separately labelled displacement can earn its own marks. An answer list without working earns zero.

Oracle: `planning/d1/motion-design-check.json` independently integrates/differentiates the source functions; exponential and quadratic-distance cases also agree with numerical quadrature. This is author verification, not independent vendor acceptance.
