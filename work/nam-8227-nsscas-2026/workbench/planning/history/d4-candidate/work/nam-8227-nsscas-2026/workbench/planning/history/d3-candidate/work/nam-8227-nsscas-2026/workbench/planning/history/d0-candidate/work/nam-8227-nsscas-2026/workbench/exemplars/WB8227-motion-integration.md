# Motion integration: nine worked design examples

NSSCAS Mathematics 8227, December 2020 syllabus, Grade 12. Owner Vitalis; Codex PLANNER calculus assistant; 23 November 2026. Proposed version 0.1.0. These are newly authored paper-design exemplars, not runtime learning items. Approval and independent review pending. Criteria suffixes and answer-only rules are in the matching workorder.

## polynomial-chain: normal (WB8227-motion-integration:polynomial-chain:normal)

Question. A particle moves along a straight coordinate line. Its acceleration is $a(t)=4 t + 1$ m s$^{-2}$, initial velocity is $3$ m s$^{-1}$, and it is at O when t=0. Find (velocity) v(t), then (distance) how far it is from O after $2$ s. Proposed marks 3+3.

1. **Action:** integrate acceleration. **Reason:** $a=dv/dt$. **Result:** $v=2 t^{2} + t+C$, and $v(0)=3$ fixes $C=3$, giving $v=2 t^{2} + t + 3$.
2. **Action:** integrate velocity from0 to2. **Reason:** v is positive throughout the interval, so signed displacement equals distance. **Result:** $s(t)=\frac{2 t^{3}}{3} + \frac{t^{2}}{2} + 3 t$, $s(0)=0$, and $d=s(2)=40/3$ m.

Marking: V1 M1 integration, V2 A1 antiderivative, V3 A1 initial constant; S1 M1 integration of v, S2 A1 correct primitive, S3 A1 final distance/unit:6/6. A correct final symbolic v can imply its3marks; a numeric-only distance earns S3 only.

Independent check: differentiate the final v and s to recover the supplied acceleration and v, and evaluate initial conditions and the endpoint.

## polynomial-chain: changed (WB8227-motion-integration:polynomial-chain:changed)

Question. A particle moves along a straight coordinate line. Its acceleration is $a(t)=2 t$ m s$^{-2}$, initial velocity is $1$ m s$^{-1}$, and it is at O when t=0. Find (velocity) v(t), then (distance) how far it is from O after $3$ s. Proposed marks 3+3.

1. **Action:** integrate acceleration. **Reason:** $a=dv/dt$. **Result:** $v=t^{2}+C$, and $v(0)=1$ fixes $C=1$, giving $v=t^{2} + 1$.
2. **Action:** integrate velocity from0 to3. **Reason:** v is positive throughout the interval, so signed displacement equals distance. **Result:** $s(t)=\frac{t^{3}}{3} + t$, $s(0)=0$, and $d=s(3)=12$ m.

Marking: V1 M1 integration, V2 A1 antiderivative, V3 A1 initial constant; S1 M1 integration of v, S2 A1 correct primitive, S3 A1 final distance/unit:6/6. A correct final symbolic v can imply its3marks; a numeric-only distance earns S3 only.

Independent check: differentiate the final v and s to recover the supplied acceleration and v, and evaluate initial conditions and the endpoint.

## polynomial-chain: boundary (WB8227-motion-integration:polynomial-chain:boundary)

Question. A particle moves along a straight coordinate line. Its acceleration is $a(t)=6 t + 2$ m s$^{-2}$, initial velocity is $4$ m s$^{-1}$, and it is at O when t=0. Find (velocity) v(t), then (distance) how far it is from O after $4$ s. Proposed marks 3+3.

1. **Action:** integrate acceleration. **Reason:** $a=dv/dt$. **Result:** $v=3 t^{2} + 2 t+C$, and $v(0)=4$ fixes $C=4$, giving $v=3 t^{2} + 2 t + 4$.
2. **Action:** integrate velocity from0 to4. **Reason:** v is positive throughout the interval, so signed displacement equals distance. **Result:** $s(t)=t^{3} + t^{2} + 4 t$, $s(0)=0$, and $d=s(4)=96$ m.

Marking: V1 M1 integration, V2 A1 antiderivative, V3 A1 initial constant; S1 M1 integration of v, S2 A1 correct primitive, S3 A1 final distance/unit:6/6. A correct final symbolic v can imply its3marks; a numeric-only distance earns S3 only.

Independent check: differentiate the final v and s to recover the supplied acceleration and v, and evaluate initial conditions and the endpoint.

## exponential-positive: normal (WB8227-motion-integration:exponential-positive:normal)

Question. A straight-line particle has velocity $v(t)=12 e^{- \frac{t}{2}}$ m s$^{-1}$, with t in seconds. Find (acceleration) a(t), then (distance) the distance travelled during its first $2$ s. Proposed marks 2+3.

1. **Action:** differentiate v. **Reason:** acceleration is dv/dt and the exponent has a chain factor. **Result:** $a(t)=- 6 e^{- \frac{t}{2}}$ m s$^{-2}$.
2. **Action:** integrate v over 0..2. **Reason:** v stays positive and distance equals its integral. **Result:** $d=[- 24 e^{- \frac{t}{2}}]_0^{2}=24 - \frac{24}{e}$ m, approximately $15.2$ m (3sf).

Marking: E1 B1 coefficient and E2 B1 exponential; E3 B1 primitive, E4 M1 both boundaries, E5 A1 final value/unit:5/5. Alternative initial-condition route determines the displacement constant before evaluating, same3distance marks, never an extra3.

Independent check: derivative of the primitive recovers v; direct definite integration and high-precision endpoint evaluation agree with the final expression and rounding.

## exponential-positive: changed (WB8227-motion-integration:exponential-positive:changed)

Question. A straight-line particle has velocity $v(t)=18 e^{- t}$ m s$^{-1}$, with t in seconds. Find (acceleration) a(t), then (distance) the distance travelled during its first $3$ s. Proposed marks 2+3.

1. **Action:** differentiate v. **Reason:** acceleration is dv/dt and the exponent has a chain factor. **Result:** $a(t)=- 18 e^{- t}$ m s$^{-2}$.
2. **Action:** integrate v over 0..3. **Reason:** v stays positive and distance equals its integral. **Result:** $d=[- 18 e^{- t}]_0^{3}=18 - \frac{18}{e^{3}}$ m, approximately $17.1$ m (3sf).

Marking: E1 B1 coefficient and E2 B1 exponential; E3 B1 primitive, E4 M1 both boundaries, E5 A1 final value/unit:5/5. Alternative initial-condition route determines the displacement constant before evaluating, same3distance marks, never an extra3.

Independent check: derivative of the primitive recovers v; direct definite integration and high-precision endpoint evaluation agree with the final expression and rounding.

## exponential-positive: boundary (WB8227-motion-integration:exponential-positive:boundary)

Question. A straight-line particle has velocity $v(t)=30 e^{- \frac{t}{4}}$ m s$^{-1}$, with t in seconds. Find (acceleration) a(t), then (distance) the distance travelled during its first $4$ s. Proposed marks 2+3.

1. **Action:** differentiate v. **Reason:** acceleration is dv/dt and the exponent has a chain factor. **Result:** $a(t)=- \frac{15 e^{- \frac{t}{4}}}{2}$ m s$^{-2}$.
2. **Action:** integrate v over 0..4. **Reason:** v stays positive and distance equals its integral. **Result:** $d=[- 120 e^{- \frac{t}{4}}]_0^{4}=120 - \frac{120}{e}$ m, approximately $75.9$ m (3sf).

Marking: E1 B1 coefficient and E2 B1 exponential; E3 B1 primitive, E4 M1 both boundaries, E5 A1 final value/unit:5/5. Alternative initial-condition route determines the displacement constant before evaluating, same3distance marks, never an extra3.

Independent check: derivative of the primitive recovers v; direct definite integration and high-precision endpoint evaluation agree with the final expression and rounding.

## interior-reversal: normal (WB8227-motion-integration:interior-reversal:normal)

Question. For 0≤t≤3, a particle has signed velocity $v(t)=2 t - 2$ m s$^{-1}$, positive in the increasing-coordinate direction. Find (rest) its rest time, (displacement) its signed displacement, and (distance) total travelled distance during this interval. Proposed marks 1+2+3.

1. **Action:** solve v=0. **Reason:** instantaneous rest occurs at zero velocity. **Result:** $t=1$ s, strictly inside the interval.
2. **Action:** integrate v over 0..3. **Reason:** this gives signed change in position. **Result:** $\int_0^{3}(2 t - 2)dt=3$ m.
3. **Action:** split the integral at 1 and add the absolute leg lengths. **Reason:** motion reverses and opposite directions do not cancel total distance. **Result:** first leg $1$m and second $4$ m, so $d=1+4=5$ m.

Marking: R1 B1 root; R2 M1 signed integral,R3 A1 displacement; R4 M1 sign split,R5 A1 leg magnitudes,R6 A1 total/unit: 6/6. Giving only the signed displacement as total does not demonstrate R4–R6.

Independent check: the two velocity triangles have areas $\tfrac{1}{2}(1)(2)=1$ and $\tfrac{1}{2}(2)(4)=4$. Their difference gives signed displacement and sum gives travelled distance. The changed case admits zero displacement without zero distance.

## interior-reversal: changed (WB8227-motion-integration:interior-reversal:changed)

Question. For 0≤t≤4, a particle has signed velocity $v(t)=t - 2$ m s$^{-1}$, positive in the increasing-coordinate direction. Find (rest) its rest time, (displacement) its signed displacement, and (distance) total travelled distance during this interval. Proposed marks 1+2+3.

1. **Action:** solve v=0. **Reason:** instantaneous rest occurs at zero velocity. **Result:** $t=2$ s, strictly inside the interval.
2. **Action:** integrate v over 0..4. **Reason:** this gives signed change in position. **Result:** $\int_0^{4}(t - 2)dt=0$ m.
3. **Action:** split the integral at 2 and add the absolute leg lengths. **Reason:** motion reverses and opposite directions do not cancel total distance. **Result:** first leg $2$m and second $2$ m, so $d=2+2=4$ m.

Marking: R1 B1 root; R2 M1 signed integral,R3 A1 displacement; R4 M1 sign split,R5 A1 leg magnitudes,R6 A1 total/unit: 6/6. Giving only the signed displacement as total does not demonstrate R4–R6.

Independent check: the two velocity triangles have areas $\tfrac{1}{2}(2)(2)=2$ and $\tfrac{1}{2}(2)(2)=2$. Their difference gives signed displacement and sum gives travelled distance. The changed case admits zero displacement without zero distance.

## interior-reversal: boundary (WB8227-motion-integration:interior-reversal:boundary)

Question. For 0≤t≤4, a particle has signed velocity $v(t)=3 t - 9$ m s$^{-1}$, positive in the increasing-coordinate direction. Find (rest) its rest time, (displacement) its signed displacement, and (distance) total travelled distance during this interval. Proposed marks 1+2+3.

1. **Action:** solve v=0. **Reason:** instantaneous rest occurs at zero velocity. **Result:** $t=3$ s, strictly inside the interval.
2. **Action:** integrate v over 0..4. **Reason:** this gives signed change in position. **Result:** $\int_0^{4}(3 t - 9)dt=-12$ m.
3. **Action:** split the integral at 3 and add the absolute leg lengths. **Reason:** motion reverses and opposite directions do not cancel total distance. **Result:** first leg $27/2$ m and second $3/2$ m, so $d=27/2+3/2=15$ m.

Marking: R1 B1 root; R2 M1 signed integral,R3 A1 displacement; R4 M1 sign split,R5 A1 leg magnitudes,R6 A1 total/unit: 6/6. Giving only the signed displacement as total does not demonstrate R4–R6.

Independent check: the two velocity triangles have areas $\tfrac{1}{2}(3)(9)=27/2$ and $\tfrac{1}{2}(1)(3)=3/2$. Their difference gives signed displacement and sum gives travelled distance. The changed case admits zero displacement without zero distance.

## Rejected boundaries and demand preservation

Reject T=0, negative elapsed time, inconsistent initial conditions, zero k in exponential/reversal, and a reversal time at or outside an endpoint in the interior-reversal branch. Do not use the simple integral0..T as total distance when velocity changes sign. A negative net displacement is admitted, not an error; a negative travelled distance is invalid. Preserve exact intermediate values and SI units, rounding only final nonexact values.

The polynomial branch is a connected initial-condition chain, exponential is two independent outputs sharing a velocity stem, and reversal changes the signed-area decision. These are explicit choices, not silent changes to one randomised template. Nine paper cases checked; no runtime generation, markup rendering, learner attempt or automatic marking run.
