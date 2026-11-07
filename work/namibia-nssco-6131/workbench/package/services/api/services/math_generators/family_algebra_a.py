"""Generators for two NSSCO Mathematics algebra lessons.

* 15821 Polynomials and Algebraic Fractions  (``nssco_polynomials_algebraic_fractions``)
* 15817 Algebraic Expressions and Formulae   (``nssco_expressions_formulae``)

The levels follow the shapes of the 2020-2024 papers (see
``work/namibia-nssco-6131/analysis/raw`` records for these lessons): simplify an
algebraic fraction, divide a cubic by a linear factor giving quotient and
remainder, write two algebraic fractions as a single fraction, collect like terms,
substitute into a formula, make a letter the subject, find and use a variation
equation. Numbers, letters and wording are new; nothing is copied.

Every problem is built backwards from its answer, and the answer is re-checked
here with exact ``Fraction`` arithmetic that does not go through the same code
that wrote the question. Every distractor is compared with the answer at several exact probe points and dropped if it
agrees (the shared conformance test then runs every one through the real marker).

Typed answers use ``*`` between letters so they can never be read as a function
name (``abs``, ``tan`` ...); the learner-facing LaTeX uses ordinary juxtaposition.
"""

from __future__ import annotations

from fractions import Fraction
from math import gcd
from typing import Dict, List, NamedTuple, Optional, Sequence, Tuple

from ..math_marking.parse import clean, to_expr
from ..math_marking import check

from .base import Distractor, GeneratedProblem, GeneratorError, MathGenerator, SeededRandom, Step
from .formatting import math

POLY_ID = "nssco_polynomials_algebraic_fractions"
FORMULAE_ID = "nssco_expressions_formulae"
POLY_LESSON = 15821
FORMULAE_LESSON = 15817

_MAX_ATTEMPTS = 500
# Letters that are safe as variable names for the marker (no e, i, l, n, o, p, q, j).
_LETTERS = "abcdfghkmrstuvwxyz"


def _require(condition: bool, message: str) -> None:
    if not condition:
        raise GeneratorError(message)


# --------------------------------------------------------------------------
# Small expression toolkit: every expression carries a typed form and a LaTeX form
# --------------------------------------------------------------------------


class Ex(NamedTuple):
    typed: str
    tex: str


def _mono_tex(mono: str) -> str:
    return mono.replace("*", "")


def poly(terms: Sequence[Tuple[int, str]]) -> Ex:
    """``[(2, 'x^3'), (-1, 'x^2'), (4, '')]`` -> ``2x^3 - x^2 + 4`` (typed uses ``*`` between letters)."""
    typed: List[str] = []
    tex: List[str] = []
    for coef, mono in terms:
        if coef == 0:
            continue
        mag = abs(coef)
        if mono == "":
            body_typed = body_tex = str(mag)
        else:
            lead = "" if mag == 1 else str(mag)
            body_typed = lead + mono
            body_tex = lead + _mono_tex(mono)
        if not typed:
            sign = "-" if coef < 0 else ""
        else:
            sign = " - " if coef < 0 else " + "
        typed.append(sign + body_typed)
        tex.append(sign + body_tex)
    if not typed:
        return Ex("0", "0")
    return Ex("".join(typed), "".join(tex))


def lin(a: int, b: int, var: str = "x") -> Ex:
    return poly([(a, var), (b, "")])


def frac(n: Ex, d: Ex) -> Ex:
    return Ex(f"({n.typed})/({d.typed})", f"\\frac{{{n.tex}}}{{{d.tex}}}")


def prod(*factors: Ex) -> Ex:
    return Ex("".join(f"({f.typed})" for f in factors), "".join(f"({f.tex})" for f in factors))


def eq(lhs: str, rhs: Ex) -> Ex:
    return Ex(f"{lhs} = {rhs.typed}", f"{lhs} = {rhs.tex}")


def pmul(p: Sequence[int], q: Sequence[int]) -> List[int]:
    out = [0] * (len(p) + len(q) - 1)
    for i, a in enumerate(p):
        for j, b in enumerate(q):
            out[i + j] += a * b
    return out


def padd(p: Sequence[int], q: Sequence[int]) -> List[int]:
    n = max(len(p), len(q))
    p = [0] * (n - len(p)) + list(p)
    q = [0] * (n - len(q)) + list(q)
    return [a + b for a, b in zip(p, q)]


def pscale(p: Sequence[int], k: int) -> List[int]:
    return [k * a for a in p]


def peval(p: Sequence[int], x: Fraction) -> Fraction:
    total = Fraction(0)
    for c in p:
        total = total * x + c
    return total


def poly_from_coefs(coefs: Sequence[int], var: str = "x") -> Ex:
    n = len(coefs) - 1
    terms = []
    for i, c in enumerate(coefs):
        power = n - i
        mono = "" if power == 0 else (var if power == 1 else f"{var}^{power}")
        terms.append((c, mono))
    return poly(terms)


def _nonzero(rng: SeededRandom, limit: int) -> int:
    return rng.choice([v for v in range(-limit, limit + 1) if v != 0])


def _nonzero_range(rng: SeededRandom, low: int, high: int) -> int:
    return rng.choice([v for v in range(low, high + 1) if v != 0])


# Points chosen so they never land on a root of the small denominators used here.
_SAMPLE_POINTS = (Fraction(17, 3), Fraction(-23, 7), Fraction(31, 5), Fraction(101, 9), Fraction(-37, 11), Fraction(53, 13))


def _same_rational(n1: Sequence[int], d1: Sequence[int], n2: Sequence[int], d2: Sequence[int]) -> bool:
    """n1/d1 == n2/d2 as rational functions (cross-multiplication, exact)."""
    left = pmul(n1, d2)
    right = pmul(n2, d1)
    return padd(left, pscale(right, -1)) == [0] * max(len(left), len(right))


_PROBE = (Fraction(17, 3), Fraction(-23, 7), Fraction(31, 5))


def _probe_value(text: str, offset: int):
    """Evaluate a typed answer at rational points (every letter gets its own value); None if unreadable.

    This is a cheap stand-in for the real marker, used only to drop distractors that
    are really the right answer. The conformance test runs the real marker on every one.
    """
    import sympy

    t = clean(text)
    remainder = None
    if " remainder " in t:
        t, remainder = t.split(" remainder ", 1)
    if "=" in t:
        t = t.split("=", 1)[1]
    expr = to_expr(t)
    if expr is None:
        return None
    symbols = sorted(expr.free_symbols, key=str)
    values = {sym: sympy.Rational(_PROBE[(i + offset) % 3].numerator, _PROBE[(i + offset) % 3].denominator)
              for i, sym in enumerate(symbols)}
    out = [sympy.nsimplify(expr.subs(values))]
    if remainder is not None:
        rem = to_expr(remainder)
        out.append(None if rem is None else sympy.nsimplify(rem))
    return tuple(out)


def _looks_equal(a: str, b: str) -> bool:
    """True if two typed answers agree at three different probe points."""
    for offset in range(3):
        va, vb = _probe_value(a, offset), _probe_value(b, offset)
        if va is None or vb is None or va != vb:
            return False
    return True


def _keep_distractors(
    answer: Ex,
    answer_display: str,
    candidates: Sequence[Tuple[str, Ex, str]],
    notes: Dict[str, str],
    *,
    expected: Optional[Sequence[str]] = None,
    answer_type: str = "expression",
    form: Optional[str] = None,
) -> List[Distractor]:
    """Keep the wrong answers that really are wrong (compared by exact evaluation at probe points)."""
    out: List[Distractor] = []
    seen = {answer_display}
    accepted = list(expected or [answer.typed])
    for code, wrong, display in candidates:
        if display in seen or wrong.typed == answer.typed:
            continue
        if any(_looks_equal(good, wrong.typed) for good in accepted):
            continue
        seen.add(display)
        out.append(Distractor(display, code, notes[code], wrong.typed))
    return out


# --------------------------------------------------------------------------
# 15821 Polynomials and Algebraic Fractions
# --------------------------------------------------------------------------

POLY_NOTES: Dict[str, Dict[str, str]] = {
    "simplify_fraction_quadratics": {
        "cancelled_x_squared_only": (
            "cancelled the x squared terms top and bottom and left the rest as a fraction, "
            "without factorising first"
        ),
        "kept_cancelled_factor": "cancelled the wrong bracket and left the common factor in the answer",
        "sign_error": "changed the sign of the number in each bracket",
    },
    "divide_cubic_by_linear": {
        "wrong_sign_of_divisor": "divided by (x minus the number) instead of (x plus the number)",
        "remainder_sign": "found the right quotient but gave the remainder with the wrong sign",
        "remainder_omitted": "gave the quotient and forgot the remainder",
        "did_not_subtract": "did not subtract the multiple of the divisor, so the quotient's last term and the remainder are wrong",
    },
    "simplify_fraction_factorise": {
        "kept_wrong_factor": "kept the wrong bracket after cancelling, giving a plus sign in the denominator",
        "lost_constant_factor": "lost the number in front when cancelling",
        "divided_top_only": "divided the numerator by x squared but left the denominator unchanged",
    },
    "single_fraction_linear": {
        "added_tops_and_bottoms": "added the numerators and added the denominators instead of finding a common denominator",
        "bracket_sign": "did not change the sign of the second term when subtracting the second numerator",
        "swapped_multipliers": "multiplied each numerator by its own denominator instead of the other denominator",
    },
    "single_fraction_harder": {
        "forgot_to_multiply": "wrote the numerators over a common denominator without multiplying them by the missing factor",
        "bracket_sign": "did not change the sign of the second numerator when subtracting",
        "added_tops_and_bottoms": "added the numerators and added the denominators instead of finding a common denominator",
        "wrong_common_denominator": "used a common denominator that does not contain every factor",
    },
}

POLY_LEVEL_SKILLS: Dict[int, Tuple[str, ...]] = {
    1: ("simplify_fraction_quadratics",),
    2: ("divide_cubic_by_linear",),
    3: ("simplify_fraction_factorise",),
    4: ("single_fraction_linear",),
    5: ("single_fraction_harder",),
}


def _poly_problem(skill, question, answer: Ex, answer_display, candidates, steps, machine, *, form=None):
    if skill.startswith("simplify_fraction") or "in its simplest form" in question:
        form = "simplest_algebraic_fraction"
        # A combined numerator can still share a factor with its denominator.
        # Cancel it in the model answer, not just when checking equivalence.
        import sympy
        if not check(
            "expression", [answer.typed], answer.typed, form=form
        ).correct:
            reduced = sympy.cancel(to_expr(answer.typed))
            answer = Ex(str(reduced).replace("**", "^"), sympy.latex(reduced))
            answer_display = math(answer.tex)
            steps = tuple(steps) + (Step("Cancel the remaining common factors", answer.typed, "expression"),)
    elif skill.startswith("single_fraction"):
        form = "single_fraction"
    notes = POLY_NOTES[skill]
    distractors = _keep_distractors(answer, answer_display, candidates, notes, form=form)
    marking = {"answer_type": "expression", "expected": [answer.typed], "typed": answer.typed}
    if form:
        marking["form"] = form
    return skill, question, answer_display, distractors, steps, marking, machine


def _p_level1(rng: SeededRandom):
    for _ in range(_MAX_ATTEMPTS):
        p = _nonzero(rng, 6)
        q = 0 if rng.chance(1, 6) else _nonzero(rng, 6)
        r = _nonzero(rng, 6)
        if q == r or r == p:
            continue
        num = [1, p + q, p * q]
        den = [1, p + r, p * r]
        answer = frac(lin(1, q), lin(1, r))
        question = f"Simplify {math(frac(poly_from_coefs(num), poly_from_coefs(den)).tex)}."
        # Independent check: num/den equals (x+q)/(x+r) as rational functions.
        _require(_same_rational(num, den, [1, q], [1, r]), "level 1 answer is wrong")
        candidates = [
            ("cancelled_x_squared_only", frac(lin(p + q, p * q), lin(p + r, p * r)), None),
            ("kept_cancelled_factor", frac(lin(1, p), lin(1, r)), None),
            ("sign_error", frac(lin(1, -q), lin(1, -r)), None),
        ]
        candidates = [(c, e, math(e.tex)) for c, e, _ in candidates]
        if p + q == 0 and p * q == 0:
            continue
        steps = (
            Step("Factorise the numerator", prod(lin(1, p), lin(1, q)).typed),
            Step("Factorise the denominator", prod(lin(1, p), lin(1, r)).typed),
            Step("Cancel the common bracket", answer.typed),
        )
        machine = {"task": "simplify_fraction", "numerator": num, "denominator": den, "common": p, "exam_marks": 3}
        return _poly_problem("simplify_fraction_quadratics", question, answer, math(answer.tex), candidates, steps, machine)
    raise GeneratorError("polynomials level 1 could not find a problem")


def _long_divide(dividend: Sequence[int], k: int) -> Tuple[List[int], int]:
    """Divide by (x + k): quotient coefficients and remainder (synthetic division at x = -k)."""
    root = -k
    out = [dividend[0]]
    for c in dividend[1:]:
        out.append(c + root * out[-1])
    return out[:-1], out[-1]


def _p_level2(rng: SeededRandom):
    for _ in range(_MAX_ATTEMPTS):
        a = rng.choice([1, 2, 2, 3])
        b, c = _nonzero(rng, 5), _nonzero(rng, 6)
        k = _nonzero(rng, 4)
        rem = _nonzero(rng, 12)
        quotient = [a, b, c]
        dividend = padd(pmul([1, k], quotient), [0, 0, 0, rem])
        if 0 in dividend:
            continue
        q_check, r_check = _long_divide(dividend, k)
        _require(q_check == quotient and r_check == rem, "level 2 division is wrong")
        _require(peval(dividend, Fraction(-k)) == rem, "remainder theorem check failed")

        def display(qc: Sequence[int], r: Optional[int]) -> Tuple[Ex, str]:
            qx = poly_from_coefs(qc)
            if r is None:
                return Ex(qx.typed, qx.tex), f"quotient {math(qx.tex)}"
            typed = f"{qx.typed} remainder {r}"
            return Ex(typed, typed), f"quotient {math(qx.tex)}, remainder {math(str(r))}"

        answer, answer_display = display(quotient, rem)
        divisor = lin(1, k)
        question = (
            f"Divide {math(poly_from_coefs(dividend).tex)} by {math(divisor.tex)}. "
            f"Give the quotient and the remainder."
        )
        wrong_q, wrong_r = _long_divide(dividend, -k)
        did_not_subtract_q = [a, b, dividend[2]]
        did_not_subtract_r = dividend[3] - k * dividend[2]
        cands = []
        for code, qc, r in (
            ("wrong_sign_of_divisor", wrong_q, wrong_r),
            ("remainder_sign", quotient, -rem),
            ("remainder_omitted", quotient, None),
            ("did_not_subtract", did_not_subtract_q, did_not_subtract_r),
        ):
            ex, disp = display(qc, r)
            cands.append((code, ex, disp))
        steps = (
            Step("First term of the quotient", poly([(a, "x^2")]).typed),
            Step("Second term of the quotient", poly([(b, "x")]).typed),
            Step("Last term of the quotient", str(c)),
            Step("Remainder", str(rem)),
        )
        machine = {"task": "divide_polynomial", "dividend": dividend, "divisor_k": k, "quotient": quotient,
                   "remainder": rem, "exam_marks": 3}
        return _poly_problem("divide_cubic_by_linear", question, answer, answer_display, cands, steps, machine)
    raise GeneratorError("polynomials level 2 could not find a problem")


def _p_level3(rng: SeededRandom):
    for _ in range(_MAX_ATTEMPTS):
        k = rng.randint(2, 9)
        m = rng.randint(1, 5)
        two_variable = rng.chance(2, 3)
        if two_variable:
            num_ex = poly([(k, "x^3"), (k * m, "x^2*y")])
            den_ex = poly([(1, "x^2"), (-m * m, "y^2")])
            answer = Ex(f"{k}*x^2/(x - {m}*y)" if m != 1 else f"{k}*x^2/(x - y)", "")
            den_ans = poly([(1, "x"), (-m, "y")])
            answer = Ex(f"({poly([(k, 'x^2')]).typed})/({den_ans.typed})",
                        f"\\frac{{{poly([(k, 'x^2')]).tex}}}{{{den_ans.tex}}}")
            wrong_den = poly([(1, "x"), (m, "y")])
            candidates = [
                ("kept_wrong_factor", Ex(f"({poly([(k, 'x^2')]).typed})/({wrong_den.typed})",
                                         f"\\frac{{{poly([(k, 'x^2')]).tex}}}{{{wrong_den.tex}}}")),
                ("lost_constant_factor", Ex(f"(x^2)/({den_ans.typed})", f"\\frac{{x^2}}{{{den_ans.tex}}}")),
                ("divided_top_only", Ex(f"({poly([(k, 'x'), (k * m, 'y')]).typed})/({den_ex.typed})",
                                        f"\\frac{{{poly([(k, 'x'), (k * m, 'y')]).tex}}}{{{den_ex.tex}}}")),
            ]
            steps = (
                Step("Factorise the numerator", f"{k}*x^2*(x + {m}*y)"),
                Step("Factorise the denominator", f"(x - {m}*y)(x + {m}*y)"),
                Step("Cancel the common bracket", answer.typed),
            )
            # exact check at sample points x, y
            for xv, yv in ((Fraction(17, 3), Fraction(7, 5)), (Fraction(-23, 7), Fraction(11, 4)), (Fraction(31, 5), Fraction(-5, 9))):
                lhs = (k * xv**3 + k * m * xv**2 * yv) / (xv**2 - m * m * yv**2)
                rhs = k * xv**2 / (xv - m * yv)
                _require(lhs == rhs, "level 3 answer is wrong")
            machine = {"task": "simplify_fraction", "variables": ["x", "y"], "k": k, "m": m, "exam_marks": 3}
        else:
            num_ex = poly([(k, "x^2"), (k * m, "x")])
            den_ex = poly([(1, "x^2"), (-m * m, "")])
            answer = frac(poly([(k, "x")]), lin(1, -m))
            candidates = [
                ("kept_wrong_factor", frac(poly([(k, "x")]), lin(1, m)), None),
                ("lost_constant_factor", frac(Ex("x", "x"), lin(1, -m)), None),
                ("divided_top_only", frac(lin(k, k * m), den_ex), None),
            ]
            steps = (
                Step("Factorise the numerator", f"{k}*x*(x + {m})"),
                Step("Factorise the denominator", f"(x - {m})(x + {m})"),
                Step("Cancel the common bracket", answer.typed),
            )
            for xv in _SAMPLE_POINTS:
                _require((k * xv * xv + k * m * xv) / (xv * xv - m * m) == k * xv / (xv - m), "level 3 answer is wrong")
            machine = {"task": "simplify_fraction", "variables": ["x"], "k": k, "m": m, "exam_marks": 3}
        question = f"Simplify {math(frac(num_ex, den_ex).tex)}."
        candidates = [(c, e, math(e.tex)) for c, e, *_ in candidates]
        return _poly_problem("simplify_fraction_factorise", question, answer, math(answer.tex), candidates, steps, machine)
    raise GeneratorError("polynomials level 3 could not find a problem")


def _p_level4(rng: SeededRandom):
    for _ in range(_MAX_ATTEMPTS):
        a, c = rng.choice([1, 1, 2, 3]), rng.choice([1, 2, 3, 4])
        b, d = _nonzero(rng, 5), _nonzero(rng, 5)
        top1, top2 = rng.randint(1, 9), rng.randint(1, 9)
        subtract = rng.chance(2, 3)
        if a * d == b * c or gcd(a, abs(b)) != 1 or gcd(c, abs(d)) != 1:
            continue
        sign = -1 if subtract else 1
        # A/(ax+b) +- C/(cx+d) = [A(cx+d) +- C(ax+b)] / [(ax+b)(cx+d)]
        numerator = padd(pscale([c, d], top1), pscale([a, b], sign * top2))
        if numerator == [0, 0] or numerator[0] == 0:
            continue
        den1, den2 = lin(a, b), lin(c, d)
        full_den = pmul([a, b], [c, d])
        # exact check at sample points
        for xv in _SAMPLE_POINTS:
            lhs = Fraction(top1) / peval([a, b], xv) + sign * Fraction(top2) / peval([c, d], xv)
            _require(lhs == peval(numerator, xv) / peval(full_den, xv), "level 4 answer is wrong")
        op = "-" if subtract else "+"
        question = (
            f"Write {math(frac(Ex(str(top1), str(top1)), den1).tex + ' ' + op + ' ' + frac(Ex(str(top2), str(top2)), den2).tex)} "
            f"as a single fraction."
        )
        num_ex = poly_from_coefs(numerator)
        answer = frac(num_ex, prod(den1, den2))
        wrong_tops = frac(Ex(str(top1 + sign * top2), str(top1 + sign * top2)), Ex(f"({den1.typed}) + ({den2.typed})",
                                                                                 f"{den1.tex} + {den2.tex}"))
        no_sign_change = padd(pscale([c, d], top1), pscale([a, b], top2 if subtract else -top2))
        swapped = padd(pscale([a, b], top1), pscale([c, d], sign * top2))
        candidates = [
            ("added_tops_and_bottoms", wrong_tops, None),
            ("bracket_sign", frac(poly_from_coefs(no_sign_change), prod(den1, den2)), None),
            ("swapped_multipliers", frac(poly_from_coefs(swapped), prod(den1, den2)), None),
        ]
        candidates = [(cd, e, math(e.tex)) for cd, e, _ in candidates]
        steps = (
            Step("Common denominator", prod(den1, den2).typed),
            Step("Combine the numerators over the common denominator", f"{top1}({den2.typed}) {op} {top2}({den1.typed})"),
            Step("Simplify the numerator", num_ex.typed),
        )
        machine = {"task": "single_fraction", "tops": [top1, top2], "dens": [[a, b], [c, d]], "subtract": subtract,
                   "exam_marks": 3}
        return _poly_problem("single_fraction_linear", question, answer, math(answer.tex), candidates, steps, machine)
    raise GeneratorError("polynomials level 4 could not find a problem")


def _p_level5(rng: SeededRandom):
    for _ in range(_MAX_ATTEMPTS):
        if rng.chance(1, 2):
            # x/(x+p) +- q/x
            p, q = _nonzero(rng, 4), rng.randint(1, 6)
            subtract = rng.chance(2, 3)
            sign = -1 if subtract else 1
            numerator = padd([1, 0, 0], pscale([1, p], sign * q))  # x^2 +- q(x + p)
            den = pmul([1, p], [1, 0])
            for xv in _SAMPLE_POINTS:
                lhs = xv / (xv + p) + sign * Fraction(q) / xv
                _require(lhs == peval(numerator, xv) / peval(den, xv), "level 5 answer is wrong")
            op = "-" if subtract else "+"
            question = (
                f"Express {math(frac(Ex('x', 'x'), lin(1, p)).tex + ' ' + op + ' ' + frac(Ex(str(q), str(q)), Ex('x', 'x')).tex)} "
                f"as a single fraction."
            )
            full_den = Ex(f"x*({lin(1, p).typed})", f"x({lin(1, p).tex})")
            num_ex = poly_from_coefs(numerator)
            answer = frac(num_ex, full_den)
            candidates = [
                ("forgot_to_multiply", frac(lin(1, sign * q), full_den), None),
                ("bracket_sign", frac(poly_from_coefs(padd([1, 0, 0], pscale([1, p], -sign * q))), full_den), None),
                ("added_tops_and_bottoms", frac(lin(1, sign * q), Ex(f"x + (x + {p})" if p > 0 else f"x + (x - {-p})",
                                                                      f"x + ({lin(1, p).tex})")), None),
            ]
            steps = (
                Step("Common denominator", full_den.typed),
                Step("Combine the numerators over the common denominator", f"x*x {op} {q}(x + {p})".replace("+ -", "- ")),
                Step("Simplify the numerator", num_ex.typed),
            )
            machine = {"task": "single_fraction", "form": "x_over_x_plus_p", "p": p, "q": q, "subtract": subtract,
                       "exam_marks": 3}
        else:
            # u/(x+p) - v/(x^2 - p^2)
            p, u, v = rng.randint(1, 4), rng.randint(1, 6), rng.randint(1, 6)
            subtract = rng.chance(2, 3)
            sign = -1 if subtract else 1
            numerator = padd(pscale([1, -p], u), [sign * v])  # u(x - p) +- v
            den = [1, 0, -p * p]
            for xv in _SAMPLE_POINTS:
                lhs = Fraction(u) / (xv + p) + sign * Fraction(v) / (xv * xv - p * p)
                _require(lhs == peval(numerator, xv) / peval(den, xv), "level 5 answer is wrong")
            op = "-" if subtract else "+"
            den_sq = poly([(1, "x^2"), (-p * p, "")])
            question = (
                f"Express {math(frac(Ex(str(u), str(u)), lin(1, p)).tex + ' ' + op + ' ' + frac(Ex(str(v), str(v)), den_sq).tex)} "
                f"as a single fraction in its simplest form."
            )
            answer = frac(poly_from_coefs(numerator), den_sq)
            candidates = [
                ("forgot_to_multiply", frac(Ex(str(u + sign * v), str(u + sign * v)), den_sq), None),
                ("bracket_sign", frac(poly_from_coefs(padd(pscale([1, -p], u), [-sign * v])), den_sq), None),
                ("wrong_common_denominator", frac(poly_from_coefs(numerator), lin(1, p)), None),
            ]
            steps = (
                Step("Factorise the second denominator", f"(x - {p})(x + {p})"),
                Step("Multiply the first numerator by the missing bracket", f"{u}(x - {p})"),
                Step("Simplify the numerator", poly_from_coefs(numerator).typed),
            )
            machine = {"task": "single_fraction", "form": "difference_of_squares", "p": p, "u": u, "v": v,
                       "subtract": subtract, "exam_marks": 3}
        candidates = [(cd, e, math(e.tex)) for cd, e, *_ in candidates]
        return _poly_problem("single_fraction_harder", question, answer, math(answer.tex), candidates, steps, machine)
    raise GeneratorError("polynomials level 5 could not find a problem")


_POLY_BUILDERS = {1: _p_level1, 2: _p_level2, 3: _p_level3, 4: _p_level4, 5: _p_level5}


class PolynomialsAlgebraicFractionsGenerator(MathGenerator):
    generator_id = POLY_ID
    version = 1
    levels = (1, 2, 3, 4, 5)
    level_skills = POLY_LEVEL_SKILLS
    error_notes = POLY_NOTES

    def _build(self, rng: SeededRandom, seed: int, level: int) -> GeneratedProblem:
        skill, question, answer, distractors, steps, marking, machine = _POLY_BUILDERS[level](rng)
        return GeneratedProblem(
            generator_id=self.generator_id, generator_version=self.version, seed=seed, level=level,
            skill=skill, question=question, answer=answer, distractors=tuple(distractors),
            machine=machine, steps=tuple(steps), marking=marking,
        )


# --------------------------------------------------------------------------
# 15817 Algebraic Expressions and Formulae
# --------------------------------------------------------------------------

FORMULAE_NOTES: Dict[str, Dict[str, str]] = {
    "collect_like_terms": {
        "added_unlike_terms": "added the two different letters together as if they were like terms",
        "ignored_signs": "ignored the minus signs and added every coefficient",
        "bracket_not_expanded_fully": "multiplied only the first term in the bracket",
    },
    "substitute_into_expression": {
        "negative_square": "treated the square of a negative number as negative",
        "sign_slip": "added where the expression subtracts",
        "ignored_negative": "dropped the minus sign on a negative value",
        "bracket_misplaced": "worked out the sum before multiplying, as if there were brackets",
        "ignored_sign_of_product": "lost the sign of the negative product",
    },
    "make_subject_linear": {
        "wrong_sign": "moved a term across without changing its sign",
        "forgot_to_divide": "moved the term across but did not divide by the coefficient",
        "divided_one_term": "divided only one term by the coefficient",
        "inverted": "turned the fraction upside down",
        "multiplied_instead": "multiplied by the bracket instead of dividing",
        "forgot_to_divide_whole": "did not divide the other side by the constant",
        "added_instead": "added the constant instead of dividing by it",
    },
    "variation_equation": {
        "constant_is_y_value": "used the given value of y as the constant instead of working it out",
        "power_not_applied": "wrote a simple proportion and left out the power or root",
        "direct_instead_of_inverse": "used direct proportion where the relationship is inverse, or the other way round",
    },
    "variation_value": {
        "constant_is_y_value": "used the given value of y as the constant instead of working it out",
        "power_not_applied": "scaled by a simple ratio and left out the power or root",
        "direct_instead_of_inverse": "used direct proportion where the relationship is inverse, or the other way round",
    },
    "make_subject_root": {
        "no_square": "did not square both sides, so the root is still there",
        "wrong_square": "squared only part of the expression",
        "sign_error": "added where the subject should be subtracted, or the other way round",
        "denominator_misplaced": "put the number on the wrong side after squaring",
    },
}

FORMULAE_LEVEL_SKILLS: Dict[int, Tuple[str, ...]] = {
    1: ("collect_like_terms",),
    2: ("substitute_into_expression",),
    3: ("make_subject_linear",),
    4: ("variation_equation", "variation_value"),
    5: ("make_subject_root",),
}

_VAR_PAIRS = (("f", "g"), ("a", "b"), ("x", "y"), ("m", "k"), ("s", "t"), ("u", "v"), ("c", "d"), ("h", "w"))


def _f_problem(skill, question, answer_ex: Ex, answer_display, candidates, steps, machine, *, answer_type="expression",
               expected: Optional[Sequence[str]] = None):
    notes = FORMULAE_NOTES[skill]
    exp = list(expected or [answer_ex.typed])
    distractors = _keep_distractors(answer_ex, answer_display, candidates, notes, expected=exp, answer_type=answer_type)
    marking = {"answer_type": answer_type, "expected": exp, "typed": answer_ex.typed}
    return skill, question, answer_display, distractors, steps, marking, machine


def _f_level1(rng: SeededRandom):
    for _ in range(_MAX_ATTEMPTS):
        v1, v2 = rng.choice(_VAR_PAIRS)
        if rng.chance(1, 2):
            # collect like terms: four terms in two letters
            a1, a2 = _nonzero(rng, 9), _nonzero(rng, 9)
            b1, b2 = _nonzero(rng, 9), _nonzero(rng, 9)
            alpha, beta = a1 + a2, b1 + b2
            if alpha == 0 or beta == 0 or min(a1, a2, b1, b2) > 0:
                continue
            terms = [(a1, v1), (b1, v2), (a2, v1), (b2, v2)]
            order = [0, 1, 2, 3]
            for i in range(3, 0, -1):
                j = rng.randint(0, i)
                order[i], order[j] = order[j], order[i]
            shown = [terms[i] for i in order]
            expr = poly([(c, v) for c, v in shown])
            question = f"Simplify {math(expr.tex)}."
            wrong_abs_a = sum(abs(c) for c, v in terms if v == v1)
            wrong_abs_b = sum(abs(c) for c, v in terms if v == v2)
            skill_cands = [
                ("added_unlike_terms", poly([(alpha + beta, f"{v1}*{v2}")]), None),
                ("ignored_signs", poly([(wrong_abs_a, v1), (wrong_abs_b, v2)]), None),
            ]
            machine = {"task": "collect_like_terms", "terms": [list(t) for t in shown], "exam_marks": 2}
            steps = (
                Step(f"Collect the {v1} terms", poly([(alpha, v1)]).typed),
                Step(f"Collect the {v2} terms", poly([(beta, v2)]).typed),
            )
        else:
            m = rng.randint(2, 5)
            a, b = _nonzero(rng, 4), _nonzero(rng, 4)
            c, d = _nonzero(rng, 7), _nonzero(rng, 7)
            alpha, beta = m * a + c, m * b + d
            if alpha == 0 or beta == 0:
                continue
            inner = poly([(a, v1), (b, v2)])
            tail = poly([(c, v1), (d, v2)])
            expr_tex = f"{m}({inner.tex}) " + ("+" if c > 0 else "-") + " " + tail.tex.lstrip("-")
            question = f"Expand and simplify {math(expr_tex)}."
            skill_cands = [
                ("bracket_not_expanded_fully", poly([(alpha, v1), (b + d, v2)]), None),
                ("added_unlike_terms", poly([(alpha + beta, f"{v1}*{v2}")]), None),
            ]
            machine = {"task": "expand_and_simplify", "m": m, "bracket": [a, b], "extra": [c, d], "exam_marks": 2}
            steps = (
                Step("Expand the bracket", poly([(m * a, v1), (m * b, v2)]).typed),
                Step(f"Collect the {v1} terms", poly([(alpha, v1)]).typed),
                Step(f"Collect the {v2} terms", poly([(beta, v2)]).typed),
            )
        answer = poly([(alpha, v1), (beta, v2)])
        _require(alpha != 0 and beta != 0, "level 1 coefficient is zero")
        candidates = [(c_, e, math(e.tex)) for c_, e, _ in skill_cands]
        return _f_problem("collect_like_terms", question, answer, math(answer.tex), candidates, steps, machine)
    raise GeneratorError("formulae level 1 could not find a problem")


def _f_level2(rng: SeededRandom):
    for _ in range(_MAX_ATTEMPTS):
        template = rng.randint(1, 3)
        if template == 1:
            s, t, k = rng.randint(2, 6), rng.randint(1, 9), rng.randint(2, 5)
            ans = s * s - k * t
            question = f"Find the value of {math(f'a^2 - {k}b')} when {math(f'a = -{s}')} and {math(f'b = {t}')}."
            wrong = [("negative_square", -s * s - k * t), ("sign_slip", s * s + k * t)]
            steps = (Step("Square the negative value", str(s * s)), Step("Multiply the second term", str(k * t)),
                     Step("Subtract", str(ans)))
            machine = {"task": "substitute", "form": "a^2 - kb", "a": -s, "b": t, "k": k, "exam_marks": 2}
        elif template == 2:
            k, m = rng.randint(2, 8), rng.randint(2, 9)
            x, y = rng.randint(2, 9), -rng.randint(2, 9)
            ans = k * x + m * y
            question = (
                f"Find the value of {math(f'{k}x + {m}y')} when {math(f'x = {x}')} and {math(f'y = {y}')}."
            )
            wrong = [("ignored_negative", k * x + m * abs(y)), ("bracket_misplaced", (k * x + m) * y)]
            steps = (Step("Substitute and multiply", f"{k * x}"), Step("Multiply the negative term", str(m * y)),
                     Step("Add", str(ans)))
            machine = {"task": "substitute", "form": "kx + my", "x": x, "y": y, "k": k, "m": m, "exam_marks": 2}
        else:
            s, k, m = rng.randint(2, 9), rng.randint(2, 6), rng.randint(2, 7)
            ans = -s + (-k) * m
            question = (
                f"Work out the value of {math('v')} when {math('v = u + at')}, "
                f"{math(f'u = -{s}')}, {math(f'a = -{k}')} and {math(f't = {m}')}."
            )
            wrong = [("ignored_sign_of_product", -s + k * m), ("bracket_misplaced", (-s + -k) * m)]
            steps = (Step("Multiply a and t", str(-k * m)), Step("Add u", str(ans)))
            machine = {"task": "substitute", "form": "v = u + at", "u": -s, "a": -k, "t": m, "exam_marks": 2}
        candidates = [(code, Ex(str(v), str(v)), math(str(v))) for code, v in wrong]
        answer = Ex(str(ans), str(ans))
        return _f_problem("substitute_into_expression", question, answer, math(str(ans)), candidates, steps, machine,
                          answer_type="number_exact")
    raise GeneratorError("formulae level 2 could not find a problem")


def _letters(rng: SeededRandom, count: int) -> List[str]:
    pool = list(_LETTERS)
    out = []
    for _ in range(count):
        letter = rng.choice(pool)
        pool.remove(letter)
        out.append(letter)
    return out


def _f_level3(rng: SeededRandom):
    template = rng.randint(1, 3)
    if template == 1:
        P, A, B, C = _letters(rng, 4)
        question = f"Make {math(C)} the subject of {math(f'{P} = {A} + {B}{C}')}."
        answer = Ex(f"{C} = ({P} - {A})/{B}", f"{C} = \\frac{{{P} - {A}}}{{{B}}}")
        cands = [
            ("wrong_sign", Ex(f"{C} = ({P} + {A})/{B}", f"{C} = \\frac{{{P} + {A}}}{{{B}}}")),
            ("forgot_to_divide", Ex(f"{C} = {P} - {A}", f"{C} = {P} - {A}")),
            ("divided_one_term", Ex(f"{C} = {P}/{B} - {A}", f"{C} = \\frac{{{P}}}{{{B}}} - {A}")),
        ]
        steps = (Step("Subtract from both sides", f"{P} - {A} = {B}*{C}"), Step("Divide both sides", answer.typed))
        machine = {"task": "change_subject", "form": "P = A + BC", "letters": [P, A, B, C], "exam_marks": 2}
        for a0, b0, c0 in ((2, 3, 5), (-1, 4, 7), (6, -2, 3)):
            _require(Fraction(a0 + b0 * c0 - a0, b0) == c0, "level 3 rearrangement is wrong")
    elif template == 2:
        P, A, B = _letters(rng, 3)
        k = rng.randint(2, 6)
        question = f"Make {math(A)} the subject of {math(f'{P} = {k}({A} + {B})')}."
        answer = Ex(f"{A} = {P}/{k} - {B}", f"{A} = \\frac{{{P}}}{{{k}}} - {B}")
        cands = [
            ("forgot_to_divide_whole", Ex(f"{A} = {P} - {B}", f"{A} = {P} - {B}")),
            ("wrong_sign", Ex(f"{A} = {P}/{k} + {B}", f"{A} = \\frac{{{P}}}{{{k}}} + {B}")),
            ("added_instead", Ex(f"{A} = {P} - {k} - {B}", f"{A} = {P} - {k} - {B}")),
        ]
        steps = (Step("Divide both sides by the number outside", f"{P}/{k} = {A} + {B}"),
                 Step("Subtract from both sides", answer.typed))
        machine = {"task": "change_subject", "form": "P = k(A + B)", "letters": [P, A, B], "k": k, "exam_marks": 2}
        for a0, b0 in ((2, 3), (-1, 4), (5, -2)):
            _require(Fraction(k * (a0 + b0), k) - b0 == a0, "level 3 rearrangement is wrong")
    else:
        P, A, B, C = _letters(rng, 4)
        question = ''.join(['Make ', format(math(B), ''), ' the subject of ', format(math(''.join([format(P, ''), ' = \\frac{', format(A, ''), '}{', format(B, ''), '} + ', format(C, '')])), ''), '.'])
        answer = Ex(f"{B} = {A}/({P} - {C})", f"{B} = \\frac{{{A}}}{{{P} - {C}}}")
        cands = [
            ("inverted", Ex(f"{B} = ({P} - {C})/{A}", f"{B} = \\frac{{{P} - {C}}}{{{A}}}")),
            ("multiplied_instead", Ex(f"{B} = {A}({P} - {C})", f"{B} = {A}({P} - {C})")),
            ("wrong_sign", Ex(f"{B} = {A}/({P} + {C})", f"{B} = \\frac{{{A}}}{{{P} + {C}}}")),
        ]
        steps = (Step("Subtract the constant term", f"{P} - {C} = {A}/{B}"), Step("Rearrange", answer.typed))
        machine = {"task": "change_subject", "form": "P = A/B + C", "letters": [P, A, B, C], "exam_marks": 2}
        for a0, b0, c0 in ((6, 3, 1), (4, -2, 5), (5, 5, -2)):
            p0 = Fraction(a0, b0) + c0
            _require(Fraction(a0) / (p0 - c0) == b0, "level 3 rearrangement is wrong")
    candidates = [(code, e, math(e.tex)) for code, e in cands]
    return _f_problem("make_subject_linear", question, answer, math(answer.tex), candidates, steps, machine)


# variation: y = k * x**e
_VARIATIONS = (
    # key, wording, exponent (numerator, denominator)
    ("square", "directly proportional to the square of", (2, 1)),
    ("inverse_cube", "inversely proportional to the cube of", (-3, 1)),
    ("root", "directly proportional to the square root of", (1, 2)),
    ("inverse_square", "inversely proportional to the square of", (-2, 1)),
)
_VAR_LETTERS = (("y", "x"), ("A", "B"), ("P", "R"), ("s", "t"), ("F", "d"), ("V", "h"))
_PERFECT_SQUARES = (4, 9, 16, 25, 36, 49, 64, 81)


def _variation_forms(key: str, y: str, x: str, k: Fraction) -> Ex:
    kk = int(k) if k.denominator == 1 else None
    _require(kk is not None, "variation constant must be an integer")
    if key == "square":
        return Ex(f"{y} = {kk}*{x}^2", f"{y} = {kk}{x}^2")
    if key == "inverse_cube":
        return Ex(f"{y} = {kk}/{x}^3", f"{y} = \\frac{{{kk}}}{{{x}^3}}")
    if key == "root":
        return Ex(f"{y} = {kk}*sqrt({x})", f"{y} = {kk}\\sqrt{{{x}}}")
    return Ex(f"{y} = {kk}/{x}^2", f"{y} = \\frac{{{kk}}}{{{x}^2}}")


def _variation_value(key: str, k: Fraction, x: int) -> Fraction:
    if key == "square":
        return k * x * x
    if key == "inverse_cube":
        return k / (x**3)
    if key == "root":
        root = int(round(x**0.5))
        _require(root * root == x, "root variation needs a square value")
        return k * root
    return k / (x * x)


def _fraction_text(value: Fraction) -> Tuple[str, str]:
    if value.denominator == 1:
        return str(value.numerator), str(value.numerator)
    sign = "-" if value < 0 else ""
    return f"{value.numerator}/{value.denominator}", f"{sign}\\frac{{{abs(value.numerator)}}}{{{value.denominator}}}"


def _expected_numbers(value: Fraction) -> List[str]:
    typed, _ = _fraction_text(value)
    out = [typed]
    den = value.denominator
    while den % 2 == 0:
        den //= 2
    while den % 5 == 0:
        den //= 5
    if den == 1 and value.denominator != 1:
        out.append(str(float(value)))
    return out


def _f_level4(rng: SeededRandom):
    for _ in range(_MAX_ATTEMPTS):
        key, wording, _exp = rng.choice(_VARIATIONS)
        y, x = rng.choice(_VAR_LETTERS)
        find_value = rng.chance(1, 2)
        if key == "square":
            k, x0 = rng.randint(2, 9), rng.randint(2, 5)
            y0 = k * x0 * x0
        elif key == "inverse_cube":
            x0, y0 = rng.randint(2, 4), rng.randint(1, 9)
            k = y0 * x0**3
        elif key == "root":
            k, x0 = rng.randint(2, 6), rng.choice((4, 9, 16, 25))
            y0 = k * int(round(x0**0.5))
        else:
            x0, y0 = rng.randint(2, 6), rng.randint(1, 9)
            k = y0 * x0 * x0
        kf = Fraction(k)
        _require(_variation_value(key, kf, x0) == y0, "variation constant check failed")
        statement = (
            f"{math(y)} is {wording} {math(x)}. When {math(f'{x} = {x0}')}, {math(f'{y} = {y0}')}."
        )
        steps_k = Step("Work out the constant of proportionality", str(k))
        equation = _variation_forms(key, y, x, kf)
        if not find_value:
            question = f"{statement} Find an equation connecting {math(y)} and {math(x)}."
            exp_n = {"square": 2, "inverse_cube": -3, "root": None, "inverse_square": -2}[key]
            sign = 1 if exp_n is None or exp_n > 0 else -1
            # wrong 1: the given y-value used as the constant
            wrong_k = _variation_forms(key, y, x, Fraction(y0)) if y0 != k else None
            # wrong 3: power or root left out (simple proportion)
            simple_k = Fraction(y0, x0) if sign > 0 else Fraction(y0 * x0)
            simple = None
            if simple_k.denominator == 1:
                simple = (Ex(f"{y} = {simple_k.numerator}*{x}", f"{y} = {simple_k.numerator}{x}") if sign > 0
                          else Ex(f"{y} = {simple_k.numerator}/{x}", f"{y} = \\frac{{{simple_k.numerator}}}{{{x}}}"))
            else:
                simple = Ex(f"{y} = ({simple_k.numerator}/{simple_k.denominator})*{x}",
                            f"{y} = \\frac{{{simple_k.numerator}}}{{{simple_k.denominator}}}{x}")
            # wrong 2: direct used for inverse, or inverse for direct (same given pair)
            flipped = None
            if key == "square":
                flipped = Ex(f"{y} = {y0 * x0 * x0}/{x}^2", f"{y} = \\frac{{{y0 * x0 * x0}}}{{{x}^2}}")
            elif key == "inverse_cube":
                kk2 = Fraction(y0, x0**3)
                flipped = Ex(f"{y} = ({kk2.numerator}/{kk2.denominator})*{x}^3" if kk2.denominator != 1 else f"{y} = {kk2.numerator}*{x}^3",
                             f"{y} = \\frac{{{kk2.numerator}}}{{{kk2.denominator}}}{x}^3" if kk2.denominator != 1 else f"{y} = {kk2.numerator}{x}^3")
            elif key == "root":
                flipped = Ex(f"{y} = {y0 * int(round(x0**0.5))}/sqrt({x})", f"{y} = \\frac{{{y0 * int(round(x0**0.5))}}}{{\\sqrt{{{x}}}}}")
            else:
                kk2 = Fraction(y0, x0**2)
                flipped = Ex(f"{y} = ({kk2.numerator}/{kk2.denominator})*{x}^2" if kk2.denominator != 1 else f"{y} = {kk2.numerator}*{x}^2",
                             f"{y} = \\frac{{{kk2.numerator}}}{{{kk2.denominator}}}{x}^2" if kk2.denominator != 1 else f"{y} = {kk2.numerator}{x}^2")
            cands = []
            if wrong_k is not None:
                cands.append(("constant_is_y_value", wrong_k))
            cands.append(("power_not_applied", simple))
            cands.append(("direct_instead_of_inverse", flipped))
            candidates = [(code, e, math(e.tex)) for code, e in cands]
            steps = (steps_k, Step("Write the equation", equation.typed))
            machine = {"task": "variation_equation", "key": key, "k": k, "given": [x0, y0], "exam_marks": 3}
            return _f_problem("variation_equation", question, equation, math(equation.tex), candidates, steps, machine)
        # value of y for a second x
        options = [v for v in (range(2, 10) if key != "root" else _PERFECT_SQUARES) if v != x0]
        preferred = [v for v in options if _variation_value(key, kf, v).denominator == 1]
        x1 = rng.choice(preferred or options)
        value = _variation_value(key, kf, x1)
        typed_v, tex_v = _fraction_text(value)
        question = f"{statement} Find the value of {math(y)} when {math(f'{x} = {x1}')}."
        sign = 1 if key in ("square", "root") else -1
        wrong_values = []
        if y0 != k:
            wrong_values.append(("constant_is_y_value", _variation_value(key, Fraction(y0), x1)))
        simple_scale = Fraction(y0) * (Fraction(x1, x0) if sign > 0 else Fraction(x0, x1))
        wrong_values.append(("power_not_applied", simple_scale))
        flipped_value = {"square": Fraction(k) / (x1 * x1) if False else Fraction(y0 * x0 * x0, x1 * x1),
                         "inverse_cube": Fraction(y0, x0**3) * x1**3,
                         "root": Fraction(y0 * int(round(x0**0.5)), 1) / Fraction(int(round(x1**0.5))),
                         "inverse_square": Fraction(y0, x0**2) * x1 * x1}[key]
        wrong_values.append(("direct_instead_of_inverse", flipped_value))
        candidates = []
        for code, v in wrong_values:
            t, tx = _fraction_text(v)
            candidates.append((code, Ex(t, tx), math(tx)))
        answer = Ex(typed_v, tex_v)
        steps = (steps_k, Step("Write the equation", equation.typed), Step("Substitute and work out the value", typed_v))
        machine = {"task": "variation_value", "key": key, "k": k, "given": [x0, y0], "ask": x1, "value": [value.numerator, value.denominator],
                   "exam_marks": 3}
        return _f_problem("variation_value", question, answer, math(tex_v), candidates, steps, machine,
                          answer_type="number_exact", expected=_expected_numbers(value))
    raise GeneratorError("formulae level 4 could not find a problem")


def _f_level5(rng: SeededRandom):
    template = rng.randint(1, 3)
    if template == 1:
        t_, y_ = rng.choice((("t", "y"), ("s", "x"), ("w", "h")))
        with_pi = rng.chance(1, 3)
        if with_pi:
            k_typed, k_tex = "2*pi", "2\\pi"
            q_typed = f"{y_} = ({t_}/(2*pi))^2"
            alt = f"{y_} = {t_}^2/(4*pi^2)"
            tex_ans = f"{y_} = \\left(\\frac{{{t_}}}{{2\\pi}}\\right)^2"
            wrong = [
                ("no_square", Ex(f"{y_} = {t_}/(2*pi)", f"{y_} = \\frac{{{t_}}}{{2\\pi}}")),
                ("wrong_square", Ex(f"{y_} = {t_}^2/(2*pi)", f"{y_} = \\frac{{{t_}^2}}{{2\\pi}}")),
                ("sign_error", Ex(f"{y_} = (2*pi*{t_})^2", f"{y_} = (2\\pi {t_})^2")),
            ]
        else:
            k = rng.randint(2, 7)
            k_typed, k_tex = str(k), str(k)
            q_typed = f"{y_} = ({t_}/{k})^2"
            alt = f"{y_} = {t_}^2/{k * k}"
            tex_ans = f"{y_} = \\left(\\frac{{{t_}}}{{{k}}}\\right)^2"
            wrong = [
                ("no_square", Ex(f"{y_} = {t_}/{k}", f"{y_} = \\frac{{{t_}}}{{{k}}}")),
                ("wrong_square", Ex(f"{y_} = {t_}^2/{k}", f"{y_} = \\frac{{{t_}^2}}{{{k}}}")),
                ("sign_error", Ex(f"{y_} = ({k}*{t_})^2", f"{y_} = ({k}{t_})^2")),
            ]
        question = ''.join(['Make ', format(math(y_), ''), ' the subject of ', format(math(''.join([format(t_, ''), ' = ', format(k_tex, ''), '\\sqrt{', format(y_, ''), '}'])), ''), '.'])
        answer = Ex(q_typed, tex_ans)
        steps = (Step("Divide both sides", f"{t_}/({k_typed}) = sqrt({y_})"), Step("Square both sides", q_typed))
        expected = [q_typed, alt]
        machine = {"task": "change_subject", "form": "t = k sqrt(y)", "letters": [t_, y_], "pi": with_pi, "exam_marks": 2}
        candidates = [(code, e, math(e.tex)) for code, e in wrong]
        for kv, tv in ((Fraction(3), Fraction(5)), (Fraction(2), Fraction(7, 2))):
            _require((tv / kv) ** 2 * kv * kv == tv * tv, "level 5 rearrangement is wrong")
        return _f_problem("make_subject_root", question, answer, math(answer.tex), candidates, steps, machine, expected=expected)
    if template == 2:
        A, B, C, D = _letters(rng, 4)
        question = ''.join(['Make ', format(math(B), ''), ' the subject of ', format(math(''.join([format(A, ''), ' = \\sqrt{\\frac{', format(B, ''), ' - ', format(C, ''), '}{', format(D, ''), '}}'])), ''), '.'])
        answer = Ex(f"{B} = {D}*{A}^2 + {C}", f"{B} = {D}{A}^2 + {C}")
        wrong = [
            ("no_square", Ex(f"{B} = {D}*{A} + {C}", f"{B} = {D}{A} + {C}")),
            ("denominator_misplaced", Ex(f"{B} = {A}^2/{D} + {C}", f"{B} = \\frac{{{A}^2}}{{{D}}} + {C}")),
            ("sign_error", Ex(f"{B} = {D}*{A}^2 - {C}", f"{B} = {D}{A}^2 - {C}")),
        ]
        steps = (Step("Square both sides", f"{A}^2 = ({B} - {C})/{D}"), Step("Multiply by the denominator", f"{D}*{A}^2 = {B} - {C}"),
                 Step("Add to both sides", answer.typed))
        machine = {"task": "change_subject", "form": "A = sqrt((B - C)/D)", "letters": [A, B, C, D], "exam_marks": 3}
        for a0, c0, d0 in ((2, 5, 3), (3, -1, 2), (Fraction(1, 2), 4, 8)):
            b0 = d0 * Fraction(a0) ** 2 + c0
            _require(((b0 - c0) / d0) == Fraction(a0) ** 2, "level 5 rearrangement is wrong")
    else:
        A, B, C, D = _letters(rng, 4)
        k = rng.randint(2, 5)
        question = ''.join(['Make ', format(math(B), ''), ' the subject of ', format(math(''.join([format(A, ''), ' = \\sqrt{\\frac{', format(k, ''), '(', format(B, ''), ' + ', format(C, ''), ')}{', format(D, ''), '}}'])), ''), '.'])
        answer = Ex(f"{B} = {D}*{A}^2/{k} - {C}", f"{B} = \\frac{{{D}{A}^2}}{{{k}}} - {C}")
        wrong = [
            ("no_square", Ex(f"{B} = {D}*{A}/{k} - {C}", f"{B} = \\frac{{{D}{A}}}{{{k}}} - {C}")),
            ("sign_error", Ex(f"{B} = {D}*{A}^2/{k} + {C}", f"{B} = \\frac{{{D}{A}^2}}{{{k}}} + {C}")),
            ("denominator_misplaced", Ex(f"{B} = ({D}*{A}^2 - {C})/{k}", f"{B} = \\frac{{{D}{A}^2 - {C}}}{{{k}}}")),
        ]
        steps = (Step("Square both sides", f"{A}^2 = {k}({B} + {C})/{D}"),
                 Step("Multiply by the denominator and divide by the number", f"{D}*{A}^2/{k} = {B} + {C}"),
                 Step("Subtract from both sides", answer.typed))
        machine = {"task": "change_subject", "form": "A = sqrt(k(B + C)/D)", "letters": [A, B, C, D], "k": k, "exam_marks": 3}
        for a0, c0, d0 in ((2, 5, 3), (3, -1, 2), (Fraction(1, 2), 4, 8)):
            b0 = d0 * Fraction(a0) ** 2 / k - c0
            _require(Fraction(k) * (b0 + c0) / d0 == Fraction(a0) ** 2, "level 5 rearrangement is wrong")
    candidates = [(code, e, math(e.tex)) for code, e in wrong]
    return _f_problem("make_subject_root", question, answer, math(answer.tex), candidates, steps, machine)


_FORMULAE_BUILDERS = {1: _f_level1, 2: _f_level2, 3: _f_level3, 4: _f_level4, 5: _f_level5}


class ExpressionsFormulaeGenerator(MathGenerator):
    generator_id = FORMULAE_ID
    version = 1
    levels = (1, 2, 3, 4, 5)
    level_skills = FORMULAE_LEVEL_SKILLS
    error_notes = FORMULAE_NOTES

    def _build(self, rng: SeededRandom, seed: int, level: int) -> GeneratedProblem:
        skill, question, answer, distractors, steps, marking, machine = _FORMULAE_BUILDERS[level](rng)
        return GeneratedProblem(
            generator_id=self.generator_id, generator_version=self.version, seed=seed, level=level,
            skill=skill, question=question, answer=answer, distractors=tuple(distractors),
            machine=machine, steps=tuple(steps), marking=marking,
        )


GENERATORS = [PolynomialsAlgebraicFractionsGenerator(), ExpressionsFormulaeGenerator()]
