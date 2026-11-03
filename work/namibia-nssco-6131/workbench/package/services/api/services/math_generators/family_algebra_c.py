"""Generators for NSSCO Mathematics lessons 15824 (Inequalities and Indices) and
15822 (Linear and Simultaneous Equations).

The levels follow the question shapes in the 2020-2024 papers for these lessons
(one-step to two-fraction linear equations, elimination, line-and-curve pairs,
index laws, fractional and negative indices, linear and double inequalities,
exponential equations) without reusing any paper's wording or numbers.

Every problem is built backwards from its answer and re-checked with exact
``Fraction`` arithmetic before it is returned. Distractors carry the typed form
of a wrong answer a learner would give after one specific, known mistake.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from math import gcd
from typing import Any, Callable, Dict, List, Mapping, Optional, Sequence, Tuple

from .base import Distractor, GeneratedProblem, GeneratorError, MathGenerator, SeededRandom, Step
from .formatting import linear_latex, math, number_latex

LINEAR_GENERATOR_ID = "nssco_linear_simultaneous_equations"
INDICES_GENERATOR_ID = "nssco_inequalities_indices"
_MAX_ATTEMPTS = 500


# --------------------------------------------------------------------------
# Shared helpers
# --------------------------------------------------------------------------


def _require(condition: bool, message: str) -> None:
    if not condition:
        raise GeneratorError(f"self-check failed: {message}")


def _nonzero(rng: SeededRandom, bound: int) -> int:
    return rng.randint(1, bound) * rng.choice((-1, 1))


def _typed(value: Fraction) -> str:
    value = Fraction(value)
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def _divisors(n: int) -> List[int]:
    return [d for d in range(1, n + 1) if n % d == 0]


def _lcm(a: int, b: int) -> int:
    return a * b // gcd(a, b)


def _coef(c: int, var: str) -> str:
    """``3x``, ``x``, ``-x``."""
    if c == 1:
        return var
    if c == -1:
        return f"-{var}"
    return f"{c}{var}"


def _lin2(a: int, b: int) -> str:
    """``ax + by`` with the usual sign and coefficient-1 rules (a, b non-zero)."""
    first = _coef(a, "x")
    second_body = "y" if abs(b) == 1 else f"{abs(b)}y"
    return f"{first} {'-' if b < 0 else '+'} {second_body}"


def _poly_text(terms: Sequence[Tuple[int, str]]) -> str:
    """Plain text such as ``x^2 - x + 3`` from (coefficient, symbol) pairs; zero terms are dropped."""
    out = ""
    for c, sym in terms:
        if c == 0:
            continue
        body = sym if (abs(c) == 1 and sym) else f"{abs(c)}{sym}"
        out += (f"-{body}" if c < 0 else body) if not out else f" {'-' if c < 0 else '+'} {body}"
    return out or "0"


def _power(base: str, exponent: int) -> str:
    """LaTeX ``x^{3}``; exponent 1 is written as the bare base."""
    return base if exponent == 1 else f"{base}^{{{exponent}}}"


def _power_typed(base: str, exponent: int) -> str:
    if exponent == 1:
        return base
    return f"{base}^{exponent}" if exponent >= 0 else f"{base}^({exponent})"


def _mono(c: int, parts: Sequence[Tuple[str, int]]) -> Tuple[str, str]:
    """(LaTeX, typed) for ``c x^a y^b``; zero exponents are dropped."""
    parts = [(v, e) for v, e in parts if e != 0]
    lead = "" if (c == 1 and parts) else ("-" if (c == -1 and parts) else str(c))
    return (
        lead + "".join(_power(v, e) for v, e in parts),
        lead + "".join(_power_typed(v, e) for v, e in parts),
    )


_REL_LATEX = {">": ">", ">=": r"\ge", "<": "<", "<=": r"\le"}
_FLIP = {">": "<", ">=": "<=", "<": ">", "<=": ">="}


def _ineq(var: str, op: str, value: Fraction) -> Tuple[str, str]:
    return (f"{var} {_REL_LATEX[op]} {number_latex(value)}", f"{var} {op} {_typed(value)}")


@dataclass
class _Built:
    skill: str
    question: str
    answer: str
    # (error code, display answer, typed answer, value key). A candidate whose key
    # equals ``correct_key`` is dropped, as is any repeated key.
    items: List[Tuple[str, str, str, Any]]
    correct_key: Any
    machine: Dict[str, Any]
    steps: List[Tuple[str, str]]
    marking: Dict[str, Any]


def _eq_marking(expected: Sequence[str], answer_type: str = "equation_solution", **extra: Any) -> Dict[str, Any]:
    marking: Dict[str, Any] = {"answer_type": answer_type, "expected": list(expected), "typed": expected[0]}
    marking.update(extra)
    return marking


class _FamilyGenerator(MathGenerator):
    """Shared plumbing: each level has a builder returning a :class:`_Built`."""

    builders: Mapping[int, Callable[[SeededRandom], _Built]] = {}

    def _build(self, rng: SeededRandom, seed: int, level: int) -> GeneratedProblem:
        built = self.builders[level](rng)
        notes = self.error_notes[built.skill]
        distractors: List[Distractor] = []
        seen = {built.correct_key}
        for code, display, typed, key in built.items:
            if key in seen:
                continue
            seen.add(key)
            distractors.append(Distractor(display, code, notes[code], typed))
        return GeneratedProblem(
            generator_id=self.generator_id,
            generator_version=self.version,
            seed=seed,
            level=level,
            skill=built.skill,
            question=built.question,
            answer=built.answer,
            distractors=tuple(distractors),
            machine=built.machine,
            steps=tuple(Step(d, v) for d, v in built.steps),
            marking=built.marking,
        )


# ==========================================================================
# Lesson 15822: Linear and Simultaneous Equations
# ==========================================================================

LINEAR_ERROR_NOTES: Dict[str, Dict[str, str]] = {
    "linear_two_step": {
        "sign_slip_constant": "added the constant to the right-hand side instead of subtracting it",
        "not_divided": "moved the constant correctly but forgot to divide by the coefficient of x",
        "sign_error_final": "found the right size of answer but gave it the wrong sign",
    },
    "linear_fraction_answer": {
        "sign_slip_constant": "added the constant to the right-hand side instead of subtracting it",
        "not_divided": "moved the constant correctly but forgot to divide by the coefficient of x",
        "sign_error_final": "found the right size of answer but gave it the wrong sign",
    },
    "linear_reversed": {
        "sign_dropped": "lost the minus sign on the x term when dividing, so the answer has the wrong sign",
        "sign_slip_constant": "added the right-hand number instead of subtracting it",
        "not_divided": "moved the numbers correctly but forgot to divide by the coefficient of x",
    },
    "linear_both_sides": {
        "sign_slip_constant": "added the constant on the left to the constant on the right instead of subtracting",
        "sign_slip_x_term": "added the x terms from both sides instead of subtracting one from the other",
        "not_divided": "collected the terms correctly but forgot to divide by the coefficient of x",
    },
    "cost_equation": {
        "forgot_fixed_cost": "divided the whole amount by the price of the unknown items without taking off the cost of the others",
        "total_items": "found the total number of items instead of the number asked for",
        "one_price_removed": "took off the cost of only one of the fixed items",
    },
    "fraction_one": {
        "sign_slip_constant": "added the constant instead of subtracting it after clearing the fraction",
        "forgot_to_multiply": "subtracted the constant but did not multiply the right-hand side by the denominator",
        "fraction_inverted": "divided by the denominator instead of multiplying",
    },
    "fraction_coefficient": {
        "inverted": "multiplied by the numerator coefficient and divided by the denominator, the wrong way round",
        "multiplied_by_coefficient": "multiplied by the coefficient of x instead of dividing by it",
    },
    "constant_over_linear": {
        "sign_slip_constant": "added the constant instead of subtracting it after clearing the fraction",
        "not_divided_by_rhs": "forgot to divide the numerator by the right-hand side first",
        "forgot_to_divide_coefficient": "cleared the fraction correctly but forgot to divide by the coefficient of x",
    },
    "fraction_two": {
        "constants_not_multiplied": "multiplied the x terms by the common denominator but not the constants",
        "right_side_not_multiplied": "multiplied the left-hand side by the common denominator but not the right-hand side",
    },
    "simultaneous_linear": {
        "sign_slip_elimination": "added the equations when they should be subtracted (or the reverse), so one value is wrong",
        "sign_slip_substitution": "found one value correctly but made a sign error when substituting to find the other",
        "values_swapped": "found both values but gave x and y the wrong way round",
    },
    "simultaneous_line_curve": {
        "one_solution_only": "found only one of the two solutions",
        "x_values_only": "gave the x-values but did not find the matching y-values",
        "sign_of_x": "gave the x-values with the wrong sign",
    },
}

LINEAR_LEVEL_SKILLS: Dict[int, Tuple[str, ...]] = {
    1: ("linear_two_step", "linear_fraction_answer", "linear_reversed"),
    2: ("linear_both_sides", "cost_equation"),
    3: ("fraction_one", "fraction_coefficient", "constant_over_linear", "fraction_two"),
    4: ("simultaneous_linear",),
    5: ("simultaneous_line_curve",),
}


def _solve_marking(x: Fraction) -> Dict[str, Any]:
    return _eq_marking([f"x = {_typed(x)}"])


def _linear_answer(x: Fraction) -> str:
    return math(f"x = {number_latex(x)}")


# ---- level 1: one- and two-step equations ---------------------------------


def _l1_two_step(rng: SeededRandom, *, fractional: bool) -> _Built:
    for _ in range(_MAX_ATTEMPTS):
        a = rng.randint(2, 9)
        b = _nonzero(rng, 12)
        if fractional:
            c = _nonzero(rng, 14)
            if (c - b) % a == 0 or c == b:
                continue
        else:
            c = a * _nonzero(rng, 10) + b
        x = Fraction(c - b, a)
        _require(a * x + b == c and x != 0, "linear solution")
        skill = "linear_fraction_answer" if fractional else "linear_two_step"
        items = [
            ("sign_slip_constant", None, None, Fraction(c + b, a)),
            ("not_divided", None, None, Fraction(c - b)),
            ("sign_error_final", None, None, -x),
        ]
        items = [(code, math(f"x = {number_latex(v)}"), f"x = {_typed(v)}", v) for code, _, _, v in items]
        return _Built(
            skill=skill,
            question=f"Solve {math(f'{linear_latex(a, b)} = {c}')}.",
            answer=_linear_answer(x),
            items=items,
            correct_key=x,
            machine={"task": "linear", "a": a, "b": b, "c": c, "x": [x.numerator, x.denominator]},
            steps=[(f"Subtract {b} from both sides" if b > 0 else f"Add {-b} to both sides", f"{_coef(a, 'x')} = {c - b}"),
                   ("Divide both sides by the coefficient of x", f"x = {_typed(x)}")],
            marking=_solve_marking(x),
        )
    raise GeneratorError("level 1 could not find a problem")


def _l1_reversed(rng: SeededRandom) -> _Built:
    for _ in range(_MAX_ATTEMPTS):
        q = rng.randint(2, 6)
        p = _nonzero(rng, 9)
        r = _nonzero(rng, 12)
        if p == r:
            continue
        x = Fraction(p - r, q)
        _require(p - q * x == r, "reversed linear solution")
        items = [
            ("sign_dropped", None, None, Fraction(r - p, q)),
            ("sign_slip_constant", None, None, Fraction(p + r, q)),
            ("not_divided", None, None, Fraction(p - r)),
        ]
        items = [(c, math(f"x = {number_latex(v)}"), f"x = {_typed(v)}", v) for c, _, _, v in items]
        return _Built(
            skill="linear_reversed",
            question=''.join(['Solve ', format(math(''.join([format(p, ''), ' - ', format(_coef(q, 'x'), ''), ' = ', format(r, '')])), ''), '.']),
            answer=_linear_answer(x),
            items=items,
            correct_key=x,
            machine={"task": "linear_reversed", "p": p, "q": q, "r": r, "x": [x.numerator, x.denominator]},
            steps=[("Collect the x term on one side", f"{_coef(q, 'x')} = {p - r}"),
                   ("Divide both sides by the coefficient of x", f"x = {_typed(x)}")],
            marking=_solve_marking(x),
        )
    raise GeneratorError("level 1 could not find a problem")


def _linear_level1(rng: SeededRandom) -> _Built:
    variant = rng.choice(("two_step", "two_step", "fractional", "reversed"))
    if variant == "reversed":
        return _l1_reversed(rng)
    return _l1_two_step(rng, fractional=(variant == "fractional"))


# ---- level 2: unknown on both sides, and a cost problem --------------------


def _l2_both_sides(rng: SeededRandom) -> _Built:
    for _ in range(_MAX_ATTEMPTS):
        a, c = _nonzero(rng, 6), _nonzero(rng, 6)
        k = a - c
        if k == 0 or abs(k) > 9:
            continue
        den = rng.choice([1, 1] + [d for d in _divisors(abs(k)) if d <= 5])
        x = Fraction(_nonzero(rng, 12), den)
        b = _nonzero(rng, 9)
        d_frac = b + k * x
        _require(d_frac.denominator == 1, "constant is whole")
        d = int(d_frac)
        if d == 0 or x == 0:
            continue
        _require(a * x + b == c * x + d, "both-sides solution")
        items = [("sign_slip_constant", Fraction(d + b, k)), ("not_divided", Fraction(d - b))]
        if a + c != 0:
            items.append(("sign_slip_x_term", Fraction(d - b, a + c)))
        items = [(code, math(f"x = {number_latex(v)}"), f"x = {_typed(v)}", v) for code, v in items]
        return _Built(
            skill="linear_both_sides",
            question=f"Solve {math(f'{linear_latex(a, b)} = {linear_latex(c, d)}')}.",
            answer=_linear_answer(x),
            items=items,
            correct_key=x,
            machine={"task": "linear_both_sides", "a": a, "b": b, "c": c, "d": d, "x": [x.numerator, x.denominator]},
            steps=[("Collect the x terms on one side and the numbers on the other", f"{_coef(k, 'x')} = {d - b}"),
                   ("Divide both sides by the coefficient of x", f"x = {_typed(x)}")],
            marking=_solve_marking(x),
        )
    raise GeneratorError("level 2 could not find a problem")


_BUYERS = ("Tangeni", "Hanna", "Selma", "Petrus", "Maria", "Johannes", "Ndapewa", "Elias")
_FIXED_ITEMS = (("notebooks", "pens"), ("loaves of bread", "bottles of milk"), ("exercise books", "rulers"),
                ("mangoes", "oranges"), ("T-shirts", "caps"))


def _l2_cost(rng: SeededRandom) -> _Built:
    for _ in range(_MAX_ATTEMPTS):
        m, n = rng.randint(2, 6), rng.randint(2, 9)
        p, q = rng.randint(4, 30), rng.randint(2, 12)
        if p == q:
            continue
        total = m * p + n * q
        _require(m * p + n * q == total, "cost total")
        who = rng.choice(_BUYERS)
        fixed, unknown = rng.choice(_FIXED_ITEMS)
        def money(v: int) -> str:
            return math(f"\\text{{N\\textdollar}}{v}")

        question = (
            f"{who} buys {m} {fixed} at {money(p)} each and some {unknown} at {money(q)} each. "
            f"{who} spends {money(total)} altogether. Calculate the number of {unknown} bought."
        )
        items = [
            ("forgot_fixed_cost", Fraction(total, q)),
            ("total_items", Fraction(n + m)),
            ("one_price_removed", Fraction(total - p, q)),
        ]
        items = [(code, f"${_typed(v)}$" if v.denominator == 1 else math(number_latex(v)), _typed(v), v) for code, v in items]
        return _Built(
            skill="cost_equation",
            question=question,
            answer=f"${n}$",
            items=items,
            correct_key=Fraction(n),
            machine={"task": "cost", "fixed_count": m, "fixed_price": p, "unit_price": q, "total": total, "n": n},
            steps=[(f"Cost of the {fixed}", str(m * p)),
                   (f"Amount left for the {unknown}", str(total - m * p)),
                   (f"Divide by the price of one", str(n))],
            marking=_eq_marking([str(n)], "number_exact"),
        )
    raise GeneratorError("level 2 could not find a problem")


def _linear_level2(rng: SeededRandom) -> _Built:
    return _l2_cost(rng) if rng.chance(1, 3) else _l2_both_sides(rng)


# ---- level 3: equations with fractions --------------------------------------


def _l3_one_fraction(rng: SeededRandom) -> _Built:
    q, r = rng.randint(3, 9), rng.randint(2, 9)
    p = _nonzero(rng, 9)
    x = Fraction(q * r - p)
    _require(Fraction(x + p, q) == r, "one-fraction solution")
    cands = [("sign_slip_constant", Fraction(q * r + p)), ("forgot_to_multiply", Fraction(r - p)),
             ("fraction_inverted", Fraction(r, q) - p)]
    items = [(c, math(f"x = {number_latex(v)}"), f"x = {_typed(v)}", v) for c, v in cands]
    return _Built(
        skill="fraction_one",
        question=''.join(['Solve ', format(math(''.join(['\\frac{', format(linear_latex(1, p), ''), '}{', format(q, ''), '} = ', format(r, '')])), ''), '.']),
        answer=_linear_answer(x),
        items=items,
        correct_key=x,
        machine={"task": "fraction_one", "p": p, "q": q, "r": r, "x": [x.numerator, 1]},
        steps=[("Multiply both sides by the denominator", f"{linear_latex(1, p)} = {q * r}"),
               ("Solve for x", f"x = {_typed(x)}")],
        marking=_solve_marking(x),
    )


def _l3_coefficient(rng: SeededRandom) -> _Built:
    for _ in range(_MAX_ATTEMPTS):
        a, q = rng.randint(2, 4), rng.randint(3, 7)
        if gcd(a, q) != 1:
            continue
        t = rng.randint(1, 6)
        x, r = Fraction(q * t), a * t
        _require(Fraction(a * x, q) - r == 0, "coefficient-fraction solution")
        cands = [("inverted", Fraction(a * r, q)), ("multiplied_by_coefficient", Fraction(q * r * a))]
        items = [(c, math(f"x = {number_latex(v)}"), f"x = {_typed(v)}", v) for c, v in cands]
        return _Built(
            skill="fraction_coefficient",
            question=''.join(['Solve ', format(math(''.join(['\\frac{', format(a, ''), 'x}{', format(q, ''), '} - ', format(r, ''), ' = 0'])), ''), '.']),
            answer=_linear_answer(x),
            items=items,
            correct_key=x,
            machine={"task": "fraction_coefficient", "a": a, "q": q, "r": r, "x": [x.numerator, 1]},
            steps=[("Add the number to both sides", f"{a}x/{q} = {r}"), ("Multiply by the denominator and divide by the coefficient", f"x = {_typed(x)}")],
            marking=_solve_marking(x),
        )
    raise GeneratorError("level 3 could not find a problem")


def _l3_constant_over_linear(rng: SeededRandom) -> _Built:
    for _ in range(_MAX_ATTEMPTS):
        p = rng.randint(1, 4)
        den = rng.choice(_divisors(p))
        x = Fraction(_nonzero(rng, 9), den)
        qq = _nonzero(rng, 8)
        d_val = p * x + qq
        _require(d_val.denominator == 1, "denominator is whole")
        denom = int(d_val)
        if denom <= 0:
            continue
        d = rng.randint(2, 5)
        a = d * denom
        _require(Fraction(a) / (p * x + qq) == d, "constant-over-linear solution")
        cands = [
            ("sign_slip_constant", (Fraction(a, d) + qq) / p),
            ("not_divided_by_rhs", Fraction(a - qq, p)),
            ("forgot_to_divide_coefficient", Fraction(a, d) - qq),
        ]
        items = [(c, math(f"x = {number_latex(v)}"), f"x = {_typed(v)}", v) for c, v in cands]
        return _Built(
            skill="constant_over_linear",
            question=''.join(['Solve ', format(math(''.join(['\\frac{', format(a, ''), '}{', format(linear_latex(p, qq), ''), '} = ', format(d, '')])), ''), '.']),
            answer=_linear_answer(x),
            items=items,
            correct_key=x,
            machine={"task": "constant_over_linear", "a": a, "p": p, "q": qq, "d": d, "x": [x.numerator, x.denominator]},
            steps=[("Multiply both sides by the denominator", f"{a} = {d}({linear_latex(p, qq)})"),
                   ("Divide both sides by the right-hand number", f"{linear_latex(p, qq)} = {denom}"),
                   ("Solve for x", f"x = {_typed(x)}")],
            marking=_solve_marking(x),
        )
    raise GeneratorError("level 3 could not find a problem")


def _l3_two_fractions(rng: SeededRandom) -> _Built:
    for _ in range(_MAX_ATTEMPTS):
        m, n = rng.choice((2, 3, 4, 5)), rng.choice((2, 3, 4, 5))
        if m == n:
            continue
        x = Fraction(_nonzero(rng, 9))
        a, b = _nonzero(rng, 6), _nonzero(rng, 6)
        total = Fraction(x + a, m) + Fraction(x + b, n)
        big = _lcm(m, n)
        nm, mm = big // m, big // n  # multipliers for the first and second fraction
        _require(nm * (x + a) + mm * (x + b) == total * big, "two-fraction identity")
        k = nm + mm
        cands = [
            ("constants_not_multiplied", (total * big - a - b) / k),
            ("right_side_not_multiplied", (total - nm * a - mm * b) / k),
        ]
        items = [(c, math(f"x = {number_latex(v)}"), f"x = {_typed(v)}", v) for c, v in cands]
        return _Built(
            skill="fraction_two",
            question=(''.join(['Solve ', format(math(''.join(['\\frac{', format(linear_latex(1, a), ''), '}{', format(m, ''), '} + \\frac{', format(linear_latex(1, b), ''), '}{', format(n, ''), '} = ', format(number_latex(total), '')])), ''), '.'])),
            answer=_linear_answer(x),
            items=items,
            correct_key=x,
            machine={"task": "fraction_two", "a": a, "b": b, "m": m, "n": n,
                     "total": [total.numerator, total.denominator], "x": [x.numerator, 1]},
            steps=[("Multiply every term by the common denominator",
                    f"{nm}({linear_latex(1, a)}) + {mm}({linear_latex(1, b)}) = {_typed(total * big)}"),
                   ("Collect the x terms", f"{_coef(k, 'x')} = {_typed(total * big - nm * a - mm * b)}"),
                   ("Solve for x", f"x = {_typed(x)}")],
            marking=_solve_marking(x),
        )
    raise GeneratorError("level 3 could not find a problem")


def _linear_level3(rng: SeededRandom) -> _Built:
    roll = rng.randint(1, 10)
    if roll <= 3:
        return _l3_one_fraction(rng)
    if roll <= 5:
        return _l3_coefficient(rng)
    if roll <= 8:
        return _l3_constant_over_linear(rng)
    return _l3_two_fractions(rng)


# ---- level 4: simultaneous linear equations ----------------------------------


def _eliminate(style: str, a1: int, b1: int, p: int, a2: int, b2: int, q: int, *, wrong: bool) -> Optional[Tuple[Fraction, Fraction]]:
    """Solve the pair by the elimination route ``style``; ``wrong`` flips the add/subtract step."""
    if style in ("opposite", "equal"):
        add = (style == "opposite") != wrong
        coef = a1 + a2 if add else a1 - a2
        rhs = p + q if add else p - q
        if coef == 0:
            return None
        x = Fraction(rhs, coef)
        y = (Fraction(p) - a1 * x) / b1
        return x, y
    k = a1 // a2  # style "scale": multiply the second equation by k, then eliminate x
    coef = b1 - k * b2 if not wrong else b1 + k * b2
    rhs = p - k * q if not wrong else p + k * q
    if coef == 0:
        return None
    y = Fraction(rhs, coef)
    x = (Fraction(p) - b1 * y) / a1
    return x, y


def _pair_text(x: Fraction, y: Fraction) -> Tuple[str, str]:
    return (math(f"x = {number_latex(x)},\\ y = {number_latex(y)}"), f"x = {_typed(x)} and y = {_typed(y)}")


def _linear_level4(rng: SeededRandom) -> _Built:
    for _ in range(_MAX_ATTEMPTS):
        x0, y0 = _nonzero(rng, 7), _nonzero(rng, 7)
        style = rng.choice(("opposite", "equal", "scale"))
        if style == "opposite":
            b1 = rng.randint(1, 5)
            a1, a2, b2 = rng.randint(1, 6), rng.randint(1, 6), -b1
        elif style == "equal":
            b1 = rng.randint(1, 5)
            a1, a2, b2 = rng.randint(1, 6), rng.randint(1, 6), b1
            if a1 == a2:
                continue
        else:
            a2, k = rng.randint(1, 3), rng.randint(2, 3)
            a1 = k * a2
            b1, b2 = _nonzero(rng, 4), _nonzero(rng, 4)
            if b1 == k * b2:
                continue
        p, q = a1 * x0 + b1 * y0, a2 * x0 + b2 * y0
        _require(a1 * b2 - a2 * b1 != 0, "independent equations")
        good = _eliminate(style, a1, b1, p, a2, b2, q, wrong=False)
        _require(good == (Fraction(x0), Fraction(y0)), "elimination recovers the solution")
        cands = [("values_swapped", (Fraction(y0), Fraction(x0))), ("sign_slip_substitution", (Fraction(x0), Fraction(-y0)))]
        bad = _eliminate(style, a1, b1, p, a2, b2, q, wrong=True)
        if bad is not None:
            cands.insert(0, ("sign_slip_elimination", bad))
        items = [(code, _pair_text(x, y)[0], _pair_text(x, y)[1], (x, y)) for code, (x, y) in cands]
        if style == "opposite":
            steps = [("Add the equations to eliminate y", f"{a1 + a2}x = {p + q}")]
        elif style == "equal":
            steps = [("Subtract the equations to eliminate y", f"{_coef(a1 - a2, 'x')} = {p - q}")]
        else:
            k = a1 // a2
            steps = [(f"Multiply the second equation by {k}", f"{_lin2(a1, k * b2)} = {k * q}"),
                     ("Subtract to eliminate x", f"{_coef(b1 - k * b2, 'y')} = {p - k * q}")]
        steps += [("Find the first value", f"{'x' if style != 'scale' else 'y'} = {x0 if style != 'scale' else y0}"),
                  ("Substitute to find the other value", f"{'y' if style != 'scale' else 'x'} = {y0 if style != 'scale' else x0}")]
        return _Built(
            skill="simultaneous_linear",
            question=f"Solve the simultaneous equations {math(f'{_lin2(a1, b1)} = {p}')} and {math(f'{_lin2(a2, b2)} = {q}')}.",
            answer=_pair_text(Fraction(x0), Fraction(y0))[0],
            items=items,
            correct_key=(Fraction(x0), Fraction(y0)),
            machine={"task": "simultaneous_linear", "eq1": [a1, b1, p], "eq2": [a2, b2, q], "style": style, "solution": [x0, y0]},
            steps=steps,
            marking=_eq_marking([f"x = {x0} and y = {y0}"]),
        )
    raise GeneratorError("level 4 could not find a problem")


# ---- level 5: one linear and one quadratic equation -------------------------------


def _linear_level5(rng: SeededRandom) -> _Built:
    for _ in range(_MAX_ATTEMPTS):
        x1, x2 = rng.randint(-5, 5), rng.randint(-5, 5)
        if x1 >= x2:
            continue
        k = rng.choice((0, 0, 0, -3, -2, -1, 1, 2, 3, 4))
        m, n = x1 + x2, k - x1 * x2
        sols = []
        for xv in (x1, x2):
            yv = xv * xv + k
            _require(yv == m * xv + n, "solution lies on the line")
            sols.append((xv, yv))
        curve = "y = x^{2}" if k == 0 else f"y = x^{{2}} {'+' if k > 0 else '-'} {abs(k)}"
        if rng.chance(1, 2):
            line = f"y = {linear_latex(m, n) if m != 0 else str(n)}" if n != 0 or m != 0 else "y = 0"
            line_style = "slope"
        else:
            line = f"{_lin2(-m, 1) if m != 0 else 'y'} = {n}"
            line_style = "general"
        answer_typed = "; ".join(f"x = {xv}, y = {yv}" for xv, yv in sols)
        pairs_typed = ", ".join(f"({xv}, {yv})" for xv, yv in sols)
        answer_disp = "; ".join(f"$x = {xv},\\ y = {yv}$" for xv, yv in sols)
        correct_key = frozenset(sols)
        cands = [
            ("one_solution_only", f"$x = {x1},\\ y = {sols[0][1]}$", f"x = {x1}, y = {sols[0][1]}", frozenset([sols[0]])),
            ("x_values_only", f"$x = {x1}$ or $x = {x2}$", f"x = {x1} or x = {x2}", ("x_only", x1, x2)),
            ("sign_of_x", "; ".join(f"$x = {-xv},\\ y = {yv}$" for xv, yv in sols),
             "; ".join(f"x = {-xv}, y = {yv}" for xv, yv in sols), frozenset((-xv, yv) for xv, yv in sols)),
        ]
        steps = [
            ("Equate the two expressions for y", f"{_poly_text([(1, 'x^2'), (k, '')])} = {_poly_text([(m, 'x'), (n, '')])}"),
            ("Rearrange to a quadratic equal to zero", f"{_poly_text([(1, 'x^2'), (-m, 'x'), (k - n, '')])} = 0"),
            ("Factorise", f"(x {'-' if x1 > 0 else '+'} {abs(x1)})(x {'-' if x2 > 0 else '+'} {abs(x2)}) = 0".replace(" + 0", "").replace(" - 0", "")),
            ("Solve for x", f"x = {x1} or x = {x2}"),
            ("Substitute to find y", f"y = {sols[0][1]} and y = {sols[1][1]}"),
        ]
        return _Built(
            skill="simultaneous_line_curve",
            question=f"Solve the simultaneous equations {math(curve)} and {math(line)}.",
            answer=answer_disp,
            items=cands,
            correct_key=correct_key,
            machine={"task": "simultaneous_line_curve", "k": k, "m": m, "n": n, "line_style": line_style,
                     "solutions": [list(s) for s in sols]},
            steps=steps,
            marking=_eq_marking([answer_typed, pairs_typed]),
        )
    raise GeneratorError("level 5 could not find a problem")


class LinearSimultaneousGenerator(_FamilyGenerator):
    generator_id = LINEAR_GENERATOR_ID
    version = 1
    levels = (1, 2, 3, 4, 5)
    level_skills = LINEAR_LEVEL_SKILLS
    error_notes = LINEAR_ERROR_NOTES
    builders = {1: _linear_level1, 2: _linear_level2, 3: _linear_level3, 4: _linear_level4, 5: _linear_level5}


# ==========================================================================
# Lesson 15824: Inequalities and Indices
# ==========================================================================

INDICES_ERROR_NOTES: Dict[str, Dict[str, str]] = {
    "index_multiply": {"indices_multiplied": "multiplied the powers instead of adding them"},
    "index_divide": {"indices_added": "added the powers instead of subtracting them"},
    "index_power": {"indices_added": "added the powers instead of multiplying them"},
    "power_of_product": {
        "coefficient_not_raised": "raised the letters to the power but left the number unchanged",
        "indices_added": "added the power outside the bracket to the powers inside instead of multiplying",
    },
    "product_of_terms": {
        "coefficients_added": "added the numbers instead of multiplying them",
        "indices_multiplied": "multiplied the powers instead of adding them",
    },
    "divide_terms": {
        "indices_added": "added the powers instead of subtracting them",
        "coefficient_not_divided": "subtracted the powers but left the number unchanged",
    },
    "evaluate_fractional": {
        "divided_by_index_denominator": "divided the number by the denominator of the power instead of taking the root",
        "halved_instead": "took a square root regardless of the denominator of the power",
    },
    "evaluate_negative": {
        "negative_result": "treated the negative power as making the answer negative",
        "sign_ignored": "ignored the minus sign in the power and worked out the positive power",
        "multiplied": "multiplied the base by the power instead of using repeated multiplication",
    },
    "evaluate_fractional_power": {
        "multiplied_then_divided": "multiplied the base by the top of the power and divided by the bottom",
        "root_forgotten": "raised to the top of the power but did not take the root",
    },
    "inequality_basic": {
        "sign_reversed": "reversed the inequality sign although no negative number was involved",
        "sign_slip_constant": "added the constant to the right-hand side instead of subtracting it",
    },
    "inequality_form_solve": {
        "sign_reversed": "reversed the inequality sign although no negative number was involved",
        "sign_slip_constant": "added the number to the right-hand side instead of subtracting it",
    },
    "inequality_both_sides": {
        "sign_not_reversed": "divided by a negative number without reversing the inequality sign",
        "sign_slip_constant": "moved the number across with the wrong sign",
    },
    "inequality_brackets": {
        "sign_not_reversed": "divided by a negative number without reversing the inequality sign",
        "sign_slip_constant": "moved the number across with the wrong sign",
    },
    "inequality_double": {
        "constant_added": "added the constant to each part instead of subtracting it",
        "one_end_only": "took the constant from the left part only",
    },
    "exponential_equal_bases": {
        "sign_ignored": "lost the minus sign of the power when writing the right-hand side as a power",
        "divided_by_base": "divided the right-hand side by the base once instead of finding the power",
        "constant_slip": "added the constant in the power instead of subtracting it",
        "not_divided": "forgot to divide by the coefficient of x",
    },
    "numeric_index_simplify": {
        "bracket_sign": "forgot that subtracting the bracket in the denominator's power changes its sign",
        "indices_multiplied": "multiplied the powers instead of adding them",
    },
    "single_power": {
        "base_sign": "added instead of subtracted when dividing the powers",
        "converted_wrongly": "wrote 25 as 5 to the power 1 instead of 5 to the power 2",
    },
}

INDICES_LEVEL_SKILLS: Dict[int, Tuple[str, ...]] = {
    1: ("index_multiply", "index_divide", "index_power"),
    2: ("power_of_product", "product_of_terms", "divide_terms", "evaluate_fractional", "evaluate_negative", "evaluate_fractional_power"),
    3: ("inequality_basic", "inequality_form_solve"),
    4: ("inequality_both_sides", "inequality_brackets", "inequality_double"),
    5: ("exponential_equal_bases", "numeric_index_simplify", "single_power"),
}

_LETTER_PAIRS = (("x", "y"), ("a", "b"), ("m", "n"), ("p", "q"), ("s", "t"))


def _expr_marking(expected: str, answer_type: str = "expression") -> Dict[str, Any]:
    return _eq_marking([expected], answer_type)


def _simplify_built(skill: str, question: str, ans: Tuple[str, str], cands: Sequence[Tuple[str, Tuple[str, str]]],
                    machine: Dict[str, Any], steps: List[Tuple[str, str]]) -> _Built:
    items = [(code, math(latex), typed, typed) for code, (latex, typed) in cands]
    return _Built(skill, question, math(ans[0]), items, ans[1], machine, steps, _expr_marking(ans[1]))


# ---- level 1: single index laws ---------------------------------------------------


def _indices_level1(rng: SeededRandom) -> _Built:
    v = rng.choice(("x", "y", "a", "b", "m", "n", "p", "t", "w"))
    kind = rng.choice(("index_multiply", "index_divide", "index_power"))
    if kind == "index_multiply":
        m, n = rng.randint(2, 9), rng.randint(2, 9)
        res, wrong = m + n, m * n
        question = ''.join(['Simplify ', format(math(''.join([format(_power(v, m), ''), ' \\times ', format(_power(v, n), '')])), ''), '.'])
        code = "indices_multiplied"
        steps = [("Add the powers", f"{v}^({m}+{n})"), ("Write the result", _power_typed(v, res))]
    elif kind == "index_divide":
        n = rng.randint(2, 7)
        m = n + rng.randint(1, 6)
        res, wrong = m - n, m + n
        question = ''.join(['Simplify ', format(math(''.join([format(_power(v, m), ''), ' \\div ', format(_power(v, n), '')])), ''), '.'])
        code = "indices_added"
        steps = [("Subtract the powers", f"{v}^({m}-{n})"), ("Write the result", _power_typed(v, res))]
    else:
        m, n = rng.randint(2, 5), rng.randint(2, 5)
        res, wrong = m * n, m + n
        question = f"Simplify {math(f'({_power(v, m)})^{{{n}}}')}."
        code = "indices_added"
        steps = [("Multiply the powers", f"{v}^({m}*{n})"), ("Write the result", _power_typed(v, res))]
    return _simplify_built(
        kind, question, (_power(v, res), _power_typed(v, res)),
        [(code, (_power(v, wrong), _power_typed(v, wrong)))],
        {"task": kind, "var": v, "m": m, "n": n, "result": res}, steps,
    )


# ---- level 2: products, quotients and values of powers ------------------------------


def _l2_power_of_product(rng: SeededRandom) -> _Built:
    v, w = rng.choice(_LETTER_PAIRS)
    c, k = rng.randint(2, 4), rng.randint(2, 3)
    a, b = rng.randint(1, 4), rng.randint(1, 4)
    inner = _mono(c, [(v, a), (w, b)])
    ans = _mono(c ** k, [(v, a * k), (w, b * k)])
    wrong1 = _mono(c, [(v, a * k), (w, b * k)])
    wrong2 = _mono(c ** k, [(v, a + k), (w, b + k)])
    return _simplify_built(
        "power_of_product", f"Simplify {math(f'({inner[0]})^{{{k}}}')}.", ans,
        [("coefficient_not_raised", wrong1), ("indices_added", wrong2)],
        {"task": "power_of_product", "c": c, "k": k, "a": a, "b": b, "vars": [v, w]},
        [("Raise each factor to the power", f"{c}^{k} {v}^({a}*{k}) {w}^({b}*{k})"), ("Write the result", ans[1])],
    )


def _l2_product(rng: SeededRandom) -> _Built:
    v, w = rng.choice(_LETTER_PAIRS)
    c1, c2 = rng.randint(2, 5), rng.randint(2, 5)
    a, b, c, d = rng.randint(1, 5), rng.randint(1, 4), rng.randint(1, 5), rng.randint(1, 4)
    t1, t2 = _mono(c1, [(v, a), (w, b)]), _mono(c2, [(v, c), (w, d)])
    ans = _mono(c1 * c2, [(v, a + c), (w, b + d)])
    wrong1 = _mono(c1 + c2, [(v, a + c), (w, b + d)])
    wrong2 = _mono(c1 * c2, [(v, a * c), (w, b * d)])
    return _simplify_built(
        "product_of_terms", ''.join(['Simplify ', format(math(''.join([format(t1[0], ''), ' \\times ', format(t2[0], '')])), ''), '.']), ans,
        [("coefficients_added", wrong1), ("indices_multiplied", wrong2)],
        {"task": "product_of_terms", "c1": c1, "c2": c2, "exps": [a, b, c, d], "vars": [v, w]},
        [("Multiply the numbers and add the powers", ans[1])],
    )


def _l2_divide(rng: SeededRandom) -> _Built:
    v = rng.choice(("x", "y", "a", "m", "t"))
    c2, r = rng.randint(2, 4), rng.randint(2, 5)
    c1 = c2 * r
    e2 = rng.randint(1, 5)
    e1 = e2 + rng.randint(1, 5)
    ans = _mono(r, [(v, e1 - e2)])
    wrong1 = _mono(r, [(v, e1 + e2)])
    wrong2 = _mono(c1, [(v, e1 - e2)])
    top, bottom = _mono(c1, [(v, e1)]), _mono(c2, [(v, e2)])
    return _simplify_built(
        "divide_terms", ''.join(['Simplify ', format(math(''.join(['\\frac{', format(top[0], ''), '}{', format(bottom[0], ''), '}'])), ''), '.']), ans,
        [("indices_added", wrong1), ("coefficient_not_divided", wrong2)],
        {"task": "divide_terms", "c1": c1, "c2": c2, "e1": e1, "e2": e2, "var": v},
        [("Divide the numbers and subtract the powers", ans[1])],
    )


def _num_built(skill: str, question: str, value: Fraction, cands: Sequence[Tuple[str, Fraction]],
               machine: Dict[str, Any], steps: List[Tuple[str, str]]) -> _Built:
    items = [(c, math(number_latex(v)), _typed(v), v) for c, v in cands]
    return _Built(skill, question, math(number_latex(value)), items, value, machine, steps, _eq_marking([_typed(value)], "number_exact"))


def _l2_evaluate(rng: SeededRandom) -> _Built:
    kind = rng.choice(("evaluate_fractional", "evaluate_negative", "evaluate_fractional_power"))
    if kind == "evaluate_fractional":
        n = rng.randint(2, 4)
        b = rng.randint(2, 5) if n > 2 else rng.randint(2, 12)
        base = b ** n
        question = ''.join(['Evaluate ', format(math(''.join([format(base, ''), '^{\\frac{1}{', format(n, ''), '}}'])), ''), '.'])
        return _num_built(kind, question, Fraction(b), [("divided_by_index_denominator", Fraction(base, n)), ("halved_instead", Fraction(base, 2))],
                          {"task": kind, "base": base, "n": n, "b": b}, [("Take the root", f"{base}^(1/{n}) = {b}")])
    if kind == "evaluate_negative":
        b, k = rng.randint(2, 6), rng.randint(1, 3)
        value = Fraction(1, b ** k)
        question = f"Evaluate {math(f'{b}^{{-{k}}}')}."
        return _num_built(kind, question, value,
                          [("negative_result", Fraction(-(b ** k))), ("sign_ignored", Fraction(b ** k)), ("multiplied", Fraction(-b * k))],
                          {"task": kind, "b": b, "k": k}, [("Write as a reciprocal", f"1/{b}^{k}"), ("Evaluate", _typed(value))])
    n, m = rng.choice((2, 3)), rng.randint(2, 3)
    b = rng.randint(2, 4) if n == 3 else rng.randint(2, 6)
    base = b ** n
    question = ''.join(['Evaluate ', format(math(''.join([format(base, ''), '^{\\frac{', format(m, ''), '}{', format(n, ''), '}}'])), ''), '.'])
    value = Fraction(b ** m)
    return _num_built(kind, question, value,
                      [("multiplied_then_divided", Fraction(base * m, n)), ("root_forgotten", Fraction(base ** m))],
                      {"task": kind, "base": base, "m": m, "n": n, "b": b}, [("Take the root first", f"{base}^(1/{n}) = {b}"), ("Raise to the power", _typed(value))])


def _indices_level2(rng: SeededRandom) -> _Built:
    roll = rng.randint(1, 10)
    if roll <= 2:
        return _l2_power_of_product(rng)
    if roll <= 4:
        return _l2_product(rng)
    if roll <= 6:
        return _l2_divide(rng)
    return _l2_evaluate(rng)


# ---- level 3: linear inequalities -----------------------------------------------------


def _ineq_built(skill: str, question: str, var: str, op: str, r: Fraction, cands: Sequence[Tuple[str, str, Fraction]],
                machine: Dict[str, Any], steps: List[Tuple[str, str]], answer_prefix: str = "") -> _Built:
    latex, typed = _ineq(var, op, r)
    items = []
    for code, cop, cv in cands:
        l, t = _ineq(var, cop, cv)
        items.append((code, math(l), t, (cop, cv)))
    return _Built(skill, question, f"{answer_prefix}{math(latex)}", items, (op, r), machine, steps,
                  _eq_marking([typed], "inequality"))


def _indices_level3(rng: SeededRandom) -> _Built:
    for _ in range(_MAX_ATTEMPTS):
        a = rng.randint(2, 6)
        b = _nonzero(rng, 9)
        op = rng.choice((">", ">=", "<", "<="))
        if rng.chance(1, 2):
            # a x + b (op) c with a whole-number boundary
            r = Fraction(_nonzero(rng, 9))
            c = a * int(r) + b
            question = f"Solve the inequality {math(f'{linear_latex(a, b)} {_REL_LATEX[op]} {c}')}."
            cands = [("sign_reversed", _FLIP[op], r), ("sign_slip_constant", op, Fraction(c + b, a))]
            return _ineq_built("inequality_basic", question, "x", op, r, cands,
                               {"task": "inequality_basic", "a": a, "b": b, "c": c, "op": op, "r": [r.numerator, 1]},
                               [("Subtract the constant from both sides" if b > 0 else "Add to both sides", f"{_coef(a, 'x')} {op} {c - b}"),
                                ("Divide both sides by the positive coefficient", _ineq("x", op, r)[1])])
        # "form then solve" with a boundary that comes from the statement
        r = Fraction(rng.randint(2, 12))
        c = a * int(r) - rng.randint(1, 9)
        bb = a * int(r) - c  # subtracting bb from a times the number
        if bb <= 0 or c == 0:
            continue
        phrase = {">": "more than", ">=": "at least", "<": "less than", "<=": "at most"}[op]
        question = (f"Subtracting {bb} from {a} times a number gives a result that is {phrase} {c}. "
                    f"Write down an inequality in {math('x')} and solve it.")
        formed = f"{linear_latex(a, -bb)} {_REL_LATEX[op]} {c}"
        cands = [("sign_reversed", _FLIP[op], r), ("sign_slip_constant", op, Fraction(c - bb, a))]
        return _ineq_built("inequality_form_solve", question, "x", op, r, cands,
                           {"task": "inequality_form_solve", "a": a, "bb": bb, "c": c, "op": op, "r": [r.numerator, 1]},
                           [("Form the inequality", f"{linear_latex(a, -bb)} {op} {c}"),
                            ("Add the number to both sides", f"{_coef(a, 'x')} {op} {c + bb}"),
                            ("Divide both sides by the coefficient", _ineq("x", op, r)[1])],
                           answer_prefix=f"{math(formed)}; ")
    raise GeneratorError("level 3 could not find a problem")


# ---- level 4: harder inequalities and double inequalities ------------------------------


def _threshold(rng: SeededRandom, k: int) -> Fraction:
    den = rng.choice([1] + [d for d in _divisors(abs(k)) if d <= 4])
    return Fraction(_nonzero(rng, 9), den)


def _l4_both_sides(rng: SeededRandom, *, brackets: bool) -> _Built:
    for _ in range(_MAX_ATTEMPTS):
        op = rng.choice((">", ">=", "<", "<="))
        if brackets:
            a, b = rng.randint(2, 6), _nonzero(rng, 6)
            c = rng.randint(-3, 3)
        else:
            a, c, b = _nonzero(rng, 6), _nonzero(rng, 6), _nonzero(rng, 9)
        k = a - c
        if k == 0 or abs(k) > 8:
            continue
        r = _threshold(rng, k)
        rhs_const = (a * b if brackets else b) + k * r
        if rhs_const.denominator != 1 or rhs_const == 0:
            continue
        d = int(rhs_const)
        final_op = op if k > 0 else _FLIP[op]
        left = f"{a}({linear_latex(1, b)})" if brackets else linear_latex(a, b)
        right = linear_latex(c, d) if c != 0 else str(d)
        question = f"Solve the inequality {math(f'{left} {_REL_LATEX[op]} {right}')}."
        shift = d - (a * b if brackets else b)
        cands = [("sign_slip_constant", final_op, Fraction(d + (a * b if brackets else b), k))]
        if k < 0:
            cands.insert(0, ("sign_not_reversed", op, r))
        skill = "inequality_brackets" if brackets else "inequality_both_sides"
        steps = []
        if brackets:
            steps.append(("Expand the bracket", f"{_coef(a, 'x')} + {a * b} {op} {right}".replace("+ -", "- ")))
        steps += [("Collect the x terms and the numbers", f"{_coef(k, 'x')} {op} {shift}"),
                  ("Divide, reversing the sign if the coefficient is negative", _ineq("x", final_op, r)[1])]
        return _ineq_built(skill, question, "x", final_op, r, cands,
                           {"task": skill, "a": a, "b": b, "c": c, "d": d, "op": op, "r": [r.numerator, r.denominator]}, steps)
    raise GeneratorError("level 4 could not find a problem")


def _l4_double(rng: SeededRandom) -> _Built:
    for _ in range(_MAX_ATTEMPTS):
        v = rng.choice(("p", "x", "n", "t", "y"))
        m, n = rng.randint(2, 5), _nonzero(rng, 6)
        lo = rng.randint(-7, 2)
        hi = lo + rng.randint(2, 9)
        if lo == hi:
            continue
        op_lo, op_hi = rng.choice(("<=", "<")), rng.choice(("<=", "<"))
        low_val, high_val = m * lo + n, m * hi + n
        question = (''.join(['Solve the inequality ', format(math(''.join([format(low_val, ''), ' ', format(_REL_LATEX[op_lo], ''), ' ', format(linear_latex(m, n).replace('x', v), ''), ' ', format(_REL_LATEX[op_hi], ''), ' ', format(high_val, '')])), ''), '.']))
        ans_l = f"{lo} {_REL_LATEX[op_lo]} {v} {_REL_LATEX[op_hi]} {hi}"
        ans_t = f"{lo} {op_lo} {v} {op_hi} {hi}"

        def chain(l: Fraction, h: Fraction) -> Tuple[str, str]:
            return (f"{number_latex(l)} {_REL_LATEX[op_lo]} {v} {_REL_LATEX[op_hi]} {number_latex(h)}",
                    f"{_typed(l)} {op_lo} {v} {op_hi} {_typed(h)}")

        c1 = chain(Fraction(low_val + n, m), Fraction(high_val + n, m))
        c2 = chain(Fraction(low_val - n, m), Fraction(high_val, m))
        items = [("constant_added", math(c1[0]), c1[1], (Fraction(low_val + n, m), Fraction(high_val + n, m))),
                 ("one_end_only", math(c2[0]), c2[1], (Fraction(low_val - n, m), Fraction(high_val, m)))]
        return _Built(
            skill="inequality_double",
            question=question,
            answer=math(ans_l),
            items=items,
            correct_key=(Fraction(lo), Fraction(hi)),
            machine={"task": "inequality_double", "var": v, "m": m, "n": n, "lo": lo, "hi": hi, "ops": [op_lo, op_hi]},
            steps=[("Subtract the constant from every part", f"{low_val - n} {op_lo} {_coef(m, v)} {op_hi} {high_val - n}"),
                   ("Divide every part by the coefficient", ans_t)],
            marking=_eq_marking([ans_t], "inequality"),
        )
    raise GeneratorError("level 4 could not find a problem")


def _indices_level4(rng: SeededRandom) -> _Built:
    roll = rng.randint(1, 10)
    if roll <= 4:
        return _l4_both_sides(rng, brackets=False)
    if roll <= 7:
        return _l4_both_sides(rng, brackets=True)
    return _l4_double(rng)


# ---- level 5: index equations and numerical simplification --------------------------------


def _l5_exponential(rng: SeededRandom) -> _Built:
    b = rng.choice((2, 3, 5))
    if rng.chance(1, 2):
        # b^x = N where N is a power (possibly a reciprocal) of b
        k = rng.choice((-4, -3, -2, -1, 2, 3, 4))
        if b == 5 and abs(k) > 3:
            k = 2 * (1 if k > 0 else -1)
        rhs_latex = number_latex(Fraction(b) ** k)
        x = Fraction(k)
        cands = [("sign_ignored", -x), ("divided_by_base", Fraction(b ** abs(k), b))]
        question = f"Solve {math(f'{b}^{{x}} = {rhs_latex}')}."
        steps = [(f"Write the right-hand side as a power of {b}", f"{b}^x = {b}^({k})"), ("Equate the powers", f"x = {k}")]
        machine = {"task": "exponential_simple", "b": b, "k": k}
    else:
        for _ in range(_MAX_ATTEMPTS):
            pp, q = rng.randint(2, 4), _nonzero(rng, 5)
            x = Fraction(rng.randint(1, 5))
            r = pp * int(x) + q
            if r < 1 or r > 5:
                continue
            break
        else:
            raise GeneratorError("level 5 could not find a problem")
        exp_latex = linear_latex(pp, q)
        question = f"Solve {math(f'{b}^{{{exp_latex}}} = {b ** r}')}."
        cands = [("constant_slip", Fraction(r + q, pp)), ("not_divided", Fraction(r - q)), ("sign_ignored", Fraction(r, pp))]
        steps = [(f"Write the right-hand side as a power of {b}", f"{b}^({exp_latex}) = {b}^{r}".replace("^(", "^(")),
                 ("Equate the powers", f"{exp_latex} = {r}"), ("Solve for x", f"x = {_typed(x)}")]
        machine = {"task": "exponential_linear", "b": b, "p": pp, "q": q, "r": r}
    items = [(c, math(f"x = {number_latex(v)}"), f"x = {_typed(v)}", v) for c, v in cands]
    return _Built("exponential_equal_bases", question, _linear_answer(x), items, x, machine, steps, _solve_marking(x))


def _l5_numeric(rng: SeededRandom) -> _Built:
    for _ in range(_MAX_ATTEMPTS):
        b = rng.choice((2, 3, 5))
        a1, a2, c = rng.randint(1, 5), rng.randint(1, 4), rng.randint(1, 5)
        e = a1 - a2 + c
        if e < 1 or e > 6:
            continue
        value = b ** e
        top = f"{b}^{{x {'+' if a1 > 0 else '-'} {abs(a1)}}} \\times {b}^{{x {'-' if a2 > 0 else '+'} {abs(a2)}}}"
        bottom = f"{b}^{{2x - {c}}}"
        question = ''.join(['Simplify ', format(math(''.join(['\\frac{', format(top, ''), '}{', format(bottom, ''), '}'])), ''), ' giving your answer as a number.'])
        wrong1 = Fraction(b ** max(a1 - a2 - c, 0)) if a1 - a2 - c >= 0 else Fraction(1, b ** (c + a2 - a1))
        wrong2 = Fraction(b ** (a1 * a2 * c)) if a1 * a2 * c <= 8 else Fraction(b ** (a1 + a2 + c))
        items = [("bracket_sign", math(number_latex(wrong1)), _typed(wrong1), wrong1),
                 ("indices_multiplied", math(number_latex(wrong2)), _typed(wrong2), wrong2)]
        return _Built(
            skill="numeric_index_simplify", question=question, answer=math(number_latex(Fraction(value))), items=items,
            correct_key=Fraction(value),
            machine={"task": "numeric_index", "b": b, "a1": a1, "a2": a2, "c": c, "exponent": e},
            steps=[("Add the powers on top", f"{b}^(2x + {a1 - a2})"), ("Subtract the power underneath", f"{b}^({e})"), ("Evaluate", str(value))],
            marking=_eq_marking([str(value)], "number_exact"),
        )
    raise GeneratorError("level 5 could not find a problem")


def _l5_single_power(rng: SeededRandom) -> _Built:
    p, q, r = rng.randint(1, 3), rng.randint(1, 3), rng.randint(1, 2)
    ex, ey = 3 * p - r, 2 * q
    question = (''.join(['Simplify ', format(math(''.join(['\\frac{125^{', format(_coef(p, 'x'), ''), '} \\times 25^{', format(_coef(q, 'y'), ''), '}}{5^{', format(_coef(r, 'x'), ''), '}}'])), ''), ', giving your answer as a single power of ', format(math('5'), ''), '.']))

    def power_form(a: int, b: int) -> Tuple[str, str]:
        inner_l = f"{_coef(a, 'x')} + {_coef(b, 'y')}"
        return (f"5^{{{inner_l}}}", f"5^({inner_l})")

    ans = power_form(ex, ey)
    wrong1 = power_form(3 * p + r, ey)
    wrong2 = power_form(ex, q)
    items = [("base_sign", math(wrong1[0]), wrong1[1], wrong1[1]), ("converted_wrongly", math(wrong2[0]), wrong2[1], wrong2[1])]
    return _Built(
        skill="single_power", question=question, answer=math(ans[0]), items=items, correct_key=ans[1],
        machine={"task": "single_power", "p": p, "q": q, "r": r, "ex": ex, "ey": ey},
        steps=[("Write 125 and 25 as powers of 5", f"5^({3 * p}x) * 5^({2 * q}y) / 5^({r}x)"),
               ("Add and subtract the powers", ans[1])],
        marking=_expr_marking(ans[1]),
    )


def _indices_level5(rng: SeededRandom) -> _Built:
    roll = rng.randint(1, 10)
    if roll <= 4:
        return _l5_exponential(rng)
    if roll <= 7:
        return _l5_numeric(rng)
    return _l5_single_power(rng)


class InequalitiesIndicesGenerator(_FamilyGenerator):
    generator_id = INDICES_GENERATOR_ID
    version = 1
    levels = (1, 2, 3, 4, 5)
    level_skills = INDICES_LEVEL_SKILLS
    error_notes = INDICES_ERROR_NOTES
    builders = {1: _indices_level1, 2: _indices_level2, 3: _indices_level3, 4: _indices_level4, 5: _indices_level5}


GENERATORS = [LinearSimultaneousGenerator(), InequalitiesIndicesGenerator()]
