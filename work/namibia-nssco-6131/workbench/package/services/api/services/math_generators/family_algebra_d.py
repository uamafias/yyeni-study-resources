"""Generators for NSSCO Mathematics lessons 15818 (Algebraic Manipulation and Expansion),
15819 (Factorisation Basics), 15823 (Solving Quadratic Equations), 15831 (Straight Line
Graphs and Gradients), 15835 (Distance, Midpoint, Gradient), 15836 (Equations of Straight
Lines) and 15837 (Parallel Lines, Perpendicular Lines, Quadrilaterals, in coordinate form).

The levels follow the question shapes in the 2020-2024 papers for these lessons without
reusing any paper's wording or numbers. Questions that need a picture (read a gradient off
a drawn graph, draw a line, show-that proofs) are not generated; where the exam gives a
figure, the same information is given here as coordinates in the text.

Every problem is built backwards from its answer and re-checked with exact ``Fraction``
arithmetic before it is returned. A distractor carries the typed form of the wrong answer
a learner gives after one specific mistake; where the wrong answer is equivalent to the
right one as an expression (an incomplete factorisation), it is shown for feedback only and
has no typed form, because the program marker cannot tell it apart.
"""

from __future__ import annotations

from dataclasses import dataclass
from decimal import ROUND_HALF_UP, Decimal, getcontext
from fractions import Fraction
from math import gcd, isqrt
from typing import Any, Callable, Dict, List, Mapping, Optional, Sequence, Tuple

from .base import Distractor, GeneratedProblem, GeneratorError, MathGenerator, SeededRandom, Step
from .formatting import linear_latex, math, number_latex, point_latex

EXPANSION_ID = "nssco_algebraic_manipulation_expansion"
FACTORISATION_ID = "nssco_factorisation_basics"
QUADRATIC_ID = "nssco_solving_quadratic_equations"
LINE_GRAPH_ID = "nssco_straight_line_graphs_gradients"
COORDINATE_ID = "nssco_distance_midpoint_gradient"
LINE_EQUATION_ID = "nssco_equations_of_straight_lines"
PARALLEL_ID = "nssco_parallel_perpendicular_quadrilaterals"

_MAX_ATTEMPTS = 500
_LETTERS = ("a", "b", "m", "n", "p", "q", "t", "x", "y")


# --------------------------------------------------------------------------
# Shared helpers
# --------------------------------------------------------------------------


def _require(condition: bool, message: str) -> None:
    if not condition:
        raise GeneratorError(f"self-check failed: {message}")


def _nonzero(rng: SeededRandom, bound: int) -> int:
    return rng.randint(1, bound) * rng.choice((-1, 1))


def _t(value) -> str:
    """Plain typed form of a number: ``5``, ``-5/2``."""
    value = Fraction(value)
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def _decimal(value) -> Optional[str]:
    """Terminating decimal text for a Fraction, or None."""
    value = Fraction(value)
    den = value.denominator
    for p in (2, 5):
        while den % p == 0:
            den //= p
    if den != 1:
        return None
    text = format(Decimal(value.numerator) / Decimal(value.denominator), "f")
    return text.rstrip("0").rstrip(".") if "." in text else text


def _num_forms(value) -> List[str]:
    forms = [_t(value)]
    dec = _decimal(value)
    if dec and dec not in forms:
        forms.append(dec)
    return forms


def _is_squarefree_part(n: int) -> Tuple[int, int]:
    """(k, m) with n = k^2 * m and m square-free."""
    k = 1
    d = 2
    while d * d <= n:
        while n % (d * d) == 0:
            n //= d * d
            k *= d
        d += 1
    return k, n


def _surd_latex(k: int, m: int) -> str:
    if m == 1:
        return str(k)
    return (f"{k}" if k != 1 else "") + f"\\sqrt{{{m}}}"


def _surd_typed(k: int, m: int) -> str:
    if m == 1:
        return str(k)
    return (f"{k} " if k != 1 else "") + f"sqrt({m})"


@dataclass
class _Built:
    skill: str
    question: str
    answer: str
    # (error code, display answer, typed answer or "", value key). A candidate whose key equals
    # ``correct_key`` is dropped, as is any repeated key.
    items: List[Tuple[str, str, str, Any]]
    correct_key: Any
    machine: Dict[str, Any]
    steps: List[Tuple[str, str]]
    marking: Dict[str, Any]


class _FamilyGenerator(MathGenerator):
    builders: Mapping[int, Callable[[SeededRandom], _Built]] = {}

    def _build(self, rng: SeededRandom, seed: int, level: int) -> GeneratedProblem:
        built = self.builders[level](rng)
        notes = self.error_notes[built.skill]
        distractors: List[Distractor] = []
        seen = {built.correct_key}
        shown = {built.answer}
        for code, display, typed, key in built.items:
            if key in seen or display in shown:
                continue
            seen.add(key)
            shown.add(display)
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


def _marking(answer_type: str, expected: Sequence[str], **extra: Any) -> Dict[str, Any]:
    marking: Dict[str, Any] = {"answer_type": answer_type, "expected": list(expected), "typed": expected[0]}
    marking.update(extra)
    return marking


# --------------------------------------------------------------------------
# Tiny exact polynomial arithmetic (two variables), used only for building and self-checking
# --------------------------------------------------------------------------

Poly = Dict[Tuple[int, int], Fraction]


def _poly(*terms: Tuple[Any, int, int]) -> Poly:
    out: Poly = {}
    for c, i, j in terms:
        out[(i, j)] = out.get((i, j), Fraction(0)) + Fraction(c)
    return {k: v for k, v in out.items() if v != 0}


def _padd(a: Poly, b: Poly) -> Poly:
    out = dict(a)
    for k, v in b.items():
        out[k] = out.get(k, Fraction(0)) + v
    return {k: v for k, v in out.items() if v != 0}


def _pscale(a: Poly, c) -> Poly:
    return {k: v * Fraction(c) for k, v in a.items() if v * Fraction(c) != 0}


def _pmul(a: Poly, b: Poly) -> Poly:
    out: Poly = {}
    for (i1, j1), c1 in a.items():
        for (i2, j2), c2 in b.items():
            key = (i1 + i2, j1 + j2)
            out[key] = out.get(key, Fraction(0)) + c1 * c2
    return {k: v for k, v in out.items() if v != 0}


def _monomial(names: Sequence[str], i: int, j: int, typed: bool) -> str:
    out = ""
    for var, e in zip(names, (i, j)):
        if e == 0:
            continue
        out += var if e == 1 else (f"{var}^{e}" if typed else f"{var}^{{{e}}}")
    return out


def _render(poly: Poly, names: Sequence[str], typed: bool = False) -> str:
    """Terms by total degree (highest first), then by the power of the first letter."""
    if not poly:
        return "0"
    out = ""
    for (i, j), c in sorted(poly.items(), key=lambda kv: (-(kv[0][0] + kv[0][1]), -kv[0][0])):
        _require(c.denominator == 1, "polynomial coefficient is not a whole number")
        mono = _monomial(names, i, j, typed)
        mag = abs(int(c))
        body = mono if (mag == 1 and mono) else f"{mag}{mono}"
        if not out:
            out = ("-" if c < 0 else "") + body
        else:
            out += f" {'-' if c < 0 else '+'} {body}"
    return out


def _poly_key(poly: Poly) -> Tuple:
    return tuple(sorted((k, v) for k, v in poly.items()))


def _lin(c1: int, c0: int, var_index: int = 0) -> Poly:
    return _poly((c1, 1 if var_index == 0 else 0, 1 if var_index == 1 else 0), (c0, 0, 0))


def _bracket(c1: int, c0: int, var: str) -> str:
    return f"({linear_latex(c1, c0, var)})"


def _expr_marking(poly: Poly, names: Sequence[str], form: Optional[str]) -> Dict[str, Any]:
    marking = _marking("expression", [_render(poly, names, typed=True)])
    if form:
        marking["form"] = form
    return marking


def _poly_item(code: str, poly: Poly, names: Sequence[str]):
    return (code, math(_render(poly, names)), _render(poly, names, typed=True), _poly_key(poly))


# ==========================================================================
# Lesson 15818: Algebraic Manipulation and Expansion
# ==========================================================================

EXPANSION_ERROR_NOTES: Dict[str, Dict[str, str]] = {
    "collect_like_terms": {
        "sign_slip": "added the last term instead of subtracting it when collecting the second letter",
        "all_in_one": "added the coefficients of the unlike terms together as if every term were the same",
    },
    "expand_number_bracket": {
        "second_term_missed": "multiplied the first term in the bracket by the number but left the second term unchanged",
        "sign_slip": "multiplied by the number but gave the second term the wrong sign",
    },
    "expand_monomial_bracket": {
        "sign_slip": "gave the second term the wrong sign after multiplying by the outside term",
        "letter_dropped": "multiplied the numbers but forgot to multiply the second term by the letter outside the bracket",
        "letters_not_combined": "multiplied the numbers but did not add the powers of the letter in the first term",
    },
    "divide_algebraic_fraction": {
        "multiplied": "multiplied the fraction by the number instead of dividing",
        "inverted": "turned the number into a fraction but inverted the fraction being divided",
    },
    "expand_two_brackets": {
        "no_middle": "multiplied only the first terms and the last terms and left out the two middle products",
        "sign_slip": "got the sign of the last product wrong",
        "middle_subtracted": "subtracted the two middle products instead of adding them",
    },
    "expand_square_and_collect": {
        "middle_missing": "squared each term in the bracket and left out the middle term",
        "number_inside": "multiplied the bracket by the outside number before squaring it",
        "middle_sign": "got the sign of the middle term of the square wrong",
    },
    "expand_square_times_linear": {
        "square_no_middle": "squared each term in the bracket and left out the middle term before multiplying",
        "middle_sign": "got the sign of the middle term of the square wrong before multiplying",
        "last_product_missed": "multiplied the linear bracket by the first two terms of the square but not the last",
    },
}

EXPANSION_LEVEL_SKILLS: Dict[int, Tuple[str, ...]] = {
    1: ("collect_like_terms", "expand_number_bracket"),
    2: ("expand_monomial_bracket", "divide_algebraic_fraction"),
    3: ("expand_two_brackets",),
    4: ("expand_square_and_collect",),
    5: ("expand_square_times_linear",),
}


def _expansion_built(skill: str, command: str, expr_latex: str, correct: Poly, names: Sequence[str],
                     wrongs: Sequence[Tuple[str, Poly]], steps: Sequence[Tuple[str, str]],
                     machine: Dict[str, Any]) -> _Built:
    return _Built(
        skill=skill,
        question=f"{command} {math(expr_latex)}.",
        answer=math(_render(correct, names)),
        items=[_poly_item(code, p, names) for code, p in wrongs],
        correct_key=_poly_key(correct),
        machine={**machine, "task": skill, "names": list(names)},
        steps=list(steps),
        marking=_expr_marking(correct, names, "expanded"),
    )


def _expansion_level1(rng: SeededRandom) -> _Built:
    if rng.chance(1, 2):
        for _ in range(_MAX_ATTEMPTS):
            a, b, c, d = (_nonzero(rng, 9) for _ in range(4))
            if a + c == 0 or b + d == 0:
                continue
            terms = [(a, "x"), (b, "y"), (c, "x"), (d, "y")]
            # exam order: x, y, x, y or x, x, y, y
            if rng.chance(1, 2):
                terms = [terms[0], terms[2], terms[1], terms[3]]
            expr = ""
            for k, (coef, var) in enumerate(terms):
                body = var if abs(coef) == 1 else f"{abs(coef)}{var}"
                expr += (("-" if coef < 0 else "") + body) if k == 0 else f" {'-' if coef < 0 else '+'} {body}"
            names = ("x", "y")
            correct = _poly((a + c, 1, 0), (b + d, 0, 1))
            wrongs = [("sign_slip", _poly((a + c, 1, 0), (b - d, 0, 1))),
                      ("all_in_one", _poly((a + b + c + d, 1, 1)))]
            if b - d == 0:
                wrongs = wrongs[1:]
            steps = [("Collect the x terms", f"{a + c}x"), ("Collect the y terms", f"{b + d}y")]
            return _expansion_built("collect_like_terms", "Simplify", expr, correct, names, wrongs, steps,
                                    {"coefficients": [a, b, c, d]})
        raise GeneratorError("level 1 could not find a problem")
    for _ in range(_MAX_ATTEMPTS):
        v = rng.choice(_LETTERS)
        k = rng.randint(2, 9) * rng.choice((1, 1, -1))
        a = rng.randint(1, 6)
        b = _nonzero(rng, 9)
        names = (v, "z")
        expr = f"{k}({linear_latex(a, b, v)})"
        correct = _poly((k * a, 1, 0), (k * b, 0, 0))
        wrongs = [("second_term_missed", _poly((k * a, 1, 0), (b, 0, 0))),
                  ("sign_slip", _poly((k * a, 1, 0), (-k * b, 0, 0)))]
        steps = [("Multiply the first term by the number", f"{k * a}{v}"),
                 ("Multiply the second term by the number", f"{k * b}")]
        return _expansion_built("expand_number_bracket", "Expand", expr, correct, names, wrongs, steps,
                                {"k": k, "a": a, "b": b})
    raise GeneratorError("level 1 could not find a problem")


def _expansion_level2(rng: SeededRandom) -> _Built:
    if rng.chance(2, 3):
        two_letters = rng.chance(1, 2)
        for _ in range(_MAX_ATTEMPTS):
            if two_letters:
                names = ("x", "y")
                c = rng.randint(1, 4)
                a = rng.randint(1, 3)
                b = _nonzero(rng, 4)
                inner = f"{'' if a == 1 else a}x {'+' if b > 0 else '-'} {'' if abs(b) == 1 else abs(b)}y"
                expr = f"{'' if c == 1 else c}xy({inner})"
                correct = _poly((c * a, 2, 1), (c * b, 1, 2))
                wrongs = [("sign_slip", _poly((c * a, 2, 1), (-c * b, 1, 2))),
                          ("letters_not_combined", _poly((c * a, 1, 1), (c * b, 1, 2))),
                          ("letter_dropped", _poly((c * a, 2, 1), (c * b, 0, 1)))]
                steps = [("Multiply the first term by the outside term", _render(_poly((c * a, 2, 1)), names, True)),
                         ("Multiply the second term by the outside term", _render(_poly((c * b, 1, 2)), names, True))]
                machine = {"c": c, "a": a, "b": b, "two_letters": True}
            else:
                v = rng.choice(("m", "t", "x", "p", "n", "a"))
                names = (v, "z")
                k = _nonzero(rng, 6)
                a = rng.randint(1, 6)
                b = _nonzero(rng, 9)
                if abs(k) == 1:
                    continue
                expr = f"{k}{v}({linear_latex(a, b, v)})"
                correct = _poly((k * a, 2, 0), (k * b, 1, 0))
                wrongs = [("sign_slip", _poly((k * a, 2, 0), (-k * b, 1, 0))),
                          ("letter_dropped", _poly((k * a, 2, 0), (k * b, 0, 0))),
                          ("letters_not_combined", _poly((k * a, 1, 0), (k * b, 1, 0)))]
                steps = [("Multiply the first term by the outside term", _render(_poly((k * a, 2, 0)), names, True)),
                         ("Multiply the second term by the outside term", _render(_poly((k * b, 1, 0)), names, True))]
                machine = {"k": k, "a": a, "b": b, "two_letters": False}
            return _expansion_built("expand_monomial_bracket", "Expand", expr, correct, names, wrongs, steps, machine)
        raise GeneratorError("level 2 could not find a problem")
    for _ in range(_MAX_ATTEMPTS):
        v = rng.choice(("a", "b", "m", "n", "p", "t", "w"))
        p = rng.randint(1, 9)
        q = rng.randint(2, 9)
        r = rng.randint(2, 9)
        result = Fraction(p, q * r)
        if gcd(p, q) != 1 or result.numerator == p:  # keep the first fraction in lowest terms and force some cancelling
            continue
        num, den = result.numerator, result.denominator
        lead = "" if p == 1 else str(p)
        question = ''.join(['Simplify ', format(math(''.join(['\\frac{', format(lead, ''), format(v, ''), '}{', format(q, ''), '} \\div ', format(r, '')])), ''), '.'])
        answer_tex = f"\\frac{{{'' if num == 1 else num}{v}}}{{{den}}}" if den != 1 else f"{'' if num == 1 else num}{v}"
        answer_typed = f"{'' if num == 1 else num}{v}" + (f"/{den}" if den != 1 else "")
        mult = Fraction(p * r, q)
        inv = Fraction(q * r, p)
        wrong_mult_tex = (f"\\frac{{{'' if mult.numerator == 1 else mult.numerator}{v}}}{{{mult.denominator}}}"
                          if mult.denominator != 1 else f"{'' if mult.numerator == 1 else mult.numerator}{v}")
        wrong_mult_typed = f"{'' if mult.numerator == 1 else mult.numerator}{v}" + (f"/{mult.denominator}" if mult.denominator != 1 else "")
        inv_tex = f"\\frac{{{inv.numerator}}}{{{inv.denominator if inv.denominator != 1 else ''}{v}}}"
        inv_typed = f"{inv.numerator}/({inv.denominator}{v})"
        items = [("multiplied", math(wrong_mult_tex), wrong_mult_typed, ("m", mult)),
                 ("inverted", math(inv_tex), inv_typed, ("i", inv))]
        steps = [("Write the division as a multiplication by one over the number", f"{lead}{v}/({q}*{r})"),
                 ("Simplify the fraction", answer_typed)]
        return _Built(
            skill="divide_algebraic_fraction", question=question, answer=math(answer_tex), items=items,
            correct_key=("c", result),
            machine={"task": "divide_algebraic_fraction", "var": v, "p": p, "q": q, "r": r,
                     "result": [result.numerator, result.denominator]},
            steps=steps, marking=_marking("expression", [answer_typed]),
        )
    raise GeneratorError("level 2 could not find a problem")


def _expansion_level3(rng: SeededRandom) -> _Built:
    for _ in range(_MAX_ATTEMPTS):
        v = rng.choice(("m", "n", "x", "t", "p"))
        a, c = rng.randint(1, 3), rng.randint(1, 3)
        b, d = _nonzero(rng, 9), _nonzero(rng, 9)
        names = (v, "z")
        correct = _pmul(_lin(a, b), _lin(c, d))
        if len(correct) < 3 or gcd(a, abs(b)) != 1 or gcd(c, abs(d)) != 1:
            continue
        expr = f"{_bracket(a, b, v)}{_bracket(c, d, v)}"
        wrongs = [("no_middle", _poly((a * c, 2, 0), (b * d, 0, 0))),
                  ("sign_slip", _poly((a * c, 2, 0), (a * d + b * c, 1, 0), (-b * d, 0, 0))),
                  ("middle_subtracted", _poly((a * c, 2, 0), (a * d - b * c, 1, 0), (b * d, 0, 0)))]
        steps = [("Multiply the first terms", _render(_poly((a * c, 2, 0)), names, True)),
                 ("Add the two middle products", _render(_poly((a * d + b * c, 1, 0)), names, True)),
                 ("Multiply the last terms", str(b * d))]
        return _expansion_built("expand_two_brackets", "Expand and simplify", expr, correct, names, wrongs, steps,
                                {"a": a, "b": b, "c": c, "d": d})
    raise GeneratorError("level 3 could not find a problem")


def _expansion_level4(rng: SeededRandom) -> _Built:
    for _ in range(_MAX_ATTEMPTS):
        v = rng.choice(("t", "x", "n", "m"))
        a = rng.randint(1, 3)
        b = _nonzero(rng, 5)
        k = rng.choice((-4, -3, -2, -1, 2, 3, 4))
        m1, n1 = _nonzero(rng, 6), _nonzero(rng, 9)
        if gcd(a, abs(b)) != 1:
            continue
        names = (v, "z")
        square = _pmul(_lin(a, b), _lin(a, b))
        correct = _padd(_lin(m1, n1), _pscale(square, k))
        outer = f"{'-' if k < 0 else '+'} {'' if abs(k) == 1 else abs(k)}({linear_latex(a, b, v)})^{{2}}"
        expr = f"{linear_latex(m1, n1, v)} {outer}"
        no_middle = _poly((a * a, 2, 0), (b * b, 0, 0))
        number_inside = _pmul(_lin(k * a, k * b), _lin(k * a, k * b))
        bad_middle = _poly((a * a, 2, 0), (-2 * a * b, 1, 0), (b * b, 0, 0))
        wrongs = [("middle_missing", _padd(_lin(m1, n1), _pscale(no_middle, k))),
                  ("number_inside", _padd(_lin(m1, n1), number_inside)),
                  ("middle_sign", _padd(_lin(m1, n1), _pscale(bad_middle, k)))]
        steps = [("Expand the squared bracket", _render(square, names, True)),
                 ("Multiply by the number outside", _render(_pscale(square, k), names, True)),
                 ("Add the other terms and collect", _render(correct, names, True))]
        return _expansion_built("expand_square_and_collect", "Expand and simplify", expr, correct, names, wrongs,
                                steps, {"m": m1, "n": n1, "k": k, "a": a, "b": b})
    raise GeneratorError("level 4 could not find a problem")


def _expansion_level5(rng: SeededRandom) -> _Built:
    for _ in range(_MAX_ATTEMPTS):
        v = rng.choice(("x", "m", "t", "n"))
        a, c = rng.randint(1, 3), rng.randint(1, 2)
        b, d = _nonzero(rng, 5), _nonzero(rng, 4)
        if gcd(a, abs(b)) != 1 or gcd(c, abs(d)) != 1:
            continue
        names = (v, "z")
        lin_a = _lin(a, b)
        square = _pmul(_lin(c, d), _lin(c, d))
        correct = _pmul(lin_a, square)
        no_middle = _poly((c * c, 2, 0), (d * d, 0, 0))
        bad_middle = _poly((c * c, 2, 0), (-2 * c * d, 1, 0), (d * d, 0, 0))
        missed_last = _pmul(lin_a, _poly((c * c, 2, 0), (2 * c * d, 1, 0)))
        missed_last = _padd(missed_last, _poly((a * d * d, 1, 0)))  # forgot b * d^2 only
        wrongs = [("square_no_middle", _pmul(lin_a, no_middle)),
                  ("middle_sign", _pmul(lin_a, bad_middle)),
                  ("last_product_missed", missed_last)]
        expr = f"{_bracket(a, b, v)}{_bracket(c, d, v)}^{{2}}"
        steps = [("Expand the squared bracket", _render(square, names, True)),
                 ("Multiply by the other bracket", _render(correct, names, True))]
        return _expansion_built("expand_square_times_linear", "Expand and simplify", expr, correct, names, wrongs,
                                steps, {"a": a, "b": b, "c": c, "d": d})
    raise GeneratorError("level 5 could not find a problem")


class AlgebraicManipulationExpansionGenerator(_FamilyGenerator):
    generator_id = EXPANSION_ID
    version = 1
    levels = (1, 2, 3, 4, 5)
    level_skills = EXPANSION_LEVEL_SKILLS
    error_notes = EXPANSION_ERROR_NOTES
    builders = {1: _expansion_level1, 2: _expansion_level2, 3: _expansion_level3,
                4: _expansion_level4, 5: _expansion_level5}



# ==========================================================================
# Lesson 15819: Factorisation Basics
# ==========================================================================

FACTORISATION_ERROR_NOTES: Dict[str, Dict[str, str]] = {
    "common_number_factor": {
        "sign_slip": "took out the common factor but gave the second term inside the bracket the wrong sign",
        "second_not_divided": "took the common factor out of the first term only and left the second term unchanged inside the bracket",
        "not_complete": "took out a common factor but not the highest one, so the bracket can still be factorised",
    },
    "common_letter_factor": {
        "sign_slip": "took out the common factor but gave the second term inside the bracket the wrong sign",
        "power_too_low": "took out the letter to a lower power than the highest common power",
        "not_complete": "took out only part of the common factor (the number or the letter) so the bracket can still be factorised",
    },
    "difference_of_squares": {
        "squared_bracket": "wrote the same bracket twice, using the same sign in both, instead of one plus and one minus",
        "squares_not_rooted": "wrote the squared numbers in the brackets without taking their square roots",
        "factor_lost": "factorised the difference of squares but forgot the common factor taken out first",
        "not_complete": "took out the common factor but did not factorise the difference of squares that remained",
    },
    "factorise_by_grouping": {
        "sign_slip_second": "grouped correctly but gave the last term in the second bracket the wrong sign",
        "sign_slip_first": "grouped correctly but gave the second term in the first bracket the wrong sign",
        "not_combined": "factorised each pair of terms but did not combine the two parts into a product of two brackets",
        "brackets_swapped": "paired the wrong terms in the two brackets",
    },
}

FACTORISATION_LEVEL_SKILLS: Dict[int, Tuple[str, ...]] = {
    1: ("common_number_factor",),
    2: ("common_letter_factor",),
    3: ("difference_of_squares",),
    4: ("factorise_by_grouping",),
}

_LETTER_PAIRS = (("m", "n"), ("x", "y"), ("p", "q"), ("a", "b"), ("s", "t"))


def _term_tex(coef: int, mono: str, first: bool) -> str:
    mag = abs(coef)
    body = mono if (mag == 1 and mono) else f"{mag}{mono}"
    if first:
        return ("-" if coef < 0 else "") + body
    return f" {'-' if coef < 0 else '+'} {body}"


def _sum_tex(terms: Sequence[Tuple[int, str]]) -> str:
    """Terms joined with signs; a zero coefficient is left out (``4x^2 - 9``, never ``4x^2 + 0x - 9``)."""
    terms = [(c, m) for c, m in terms if c != 0]
    return "".join(_term_tex(c, m, k == 0) for k, (c, m) in enumerate(terms)) or "0"


def _pow(var: str, e: int, typed: bool = False) -> str:
    if e == 0:
        return ""
    if e == 1:
        return var
    return f"{var}^{e}" if typed else f"{var}^{{{e}}}"


def _product(g: int, power_part: str, inner: str) -> str:
    return f"{'' if g == 1 else g}{power_part}({inner})"


def _factorised_built(skill: str, expression: str, answer_tex: str, answer_typed: str,
                      items: List[Tuple[str, str, str, Any]], steps: List[Tuple[str, str]],
                      machine: Dict[str, Any], command: str = "Factorise completely") -> _Built:
    return _Built(
        skill=skill,
        question=f"{command} {math(expression)}.",
        answer=math(answer_tex),
        items=items,
        correct_key=("c", answer_typed),
        machine={**machine, "task": skill, "expression": expression},
        steps=steps,
        marking=_marking("expression", [answer_typed], form="factorised"),
    )


def _factor_level1(rng: SeededRandom) -> _Built:
    for _ in range(_MAX_ATTEMPTS):
        g = rng.randint(2, 9)
        a, b = rng.randint(1, 6), rng.randint(1, 6)
        if gcd(a, b) != 1:
            continue
        sign = rng.choice((1, -1))
        two_letters = rng.chance(1, 2)
        u, w = rng.choice(_LETTER_PAIRS) if two_letters else (rng.choice(("a", "m", "n", "p", "x", "y")), "")
        terms = [(g * a, u), (sign * g * b, w)]
        if not two_letters:
            terms[1] = (sign * g * b, "")
        expression = _sum_tex(terms)
        inner_l = _sum_tex([(a, u), (sign * b, w)])
        answer_tex = _product(g, "", inner_l)
        answer_typed = answer_tex
        wrong_sign = _product(g, "", _sum_tex([(a, u), (-sign * b, w)]))
        not_div = _product(g, "", _sum_tex([(a, u), (sign * g * b, w)]))
        items = [("sign_slip", math(wrong_sign), wrong_sign, ("t", wrong_sign)),
                 ("second_not_divided", math(not_div), not_div, ("t", not_div))]
        for d in range(2, g):
            if g % d == 0:
                q = g // d
                partial = _product(d, "", _sum_tex([(q * a, u), (sign * q * b, w)]))
                items.append(("not_complete", math(partial), "", ("inc", d)))
                break
        steps = [("Find the highest common factor of the numbers", str(g)),
                 ("Divide each term by it and write the results in the bracket", inner_l)]
        return _factorised_built("common_number_factor", expression, answer_tex, answer_typed, items, steps,
                                 {"g": g, "a": a, "b": b, "sign": sign, "letters": [u, w]})
    raise GeneratorError("level 1 could not find a problem")


def _factor_level2(rng: SeededRandom) -> _Built:
    for _ in range(_MAX_ATTEMPTS):
        v = rng.choice(("a", "m", "n", "p", "t", "x", "y"))
        g = rng.choice((1, 1, 2, 3, 4, 5, 6))
        a, b = rng.randint(1, 6), rng.randint(1, 16)
        if gcd(a, b) != 1:
            continue
        k, j = rng.randint(1, 2), rng.randint(1, 2)
        if k + j > 3:
            continue
        sign = rng.choice((1, -1))
        if j == 2:
            # keep the bracket from being a difference of two squares
            if sign == -1 and isqrt(a) ** 2 == a and isqrt(b) ** 2 == b:
                continue
        if g * a == 1 and g == 1 and k == 0:
            continue
        terms = [(g * a, _pow(v, k + j)), (sign * g * b, _pow(v, k))]
        expression = _sum_tex(terms)
        inner = _sum_tex([(a, _pow(v, j)), (sign * b, "")])
        answer_tex = _product(g, _pow(v, k), inner)
        answer_typed = f"{'' if g == 1 else g}{_pow(v, k, True)}({_sum_tex([(a, _pow(v, j, True)), (sign * b, '')])})"
        wrong_sign = f"{'' if g == 1 else g}{_pow(v, k, True)}({_sum_tex([(a, _pow(v, j, True)), (-sign * b, '')])})"
        low = k - 1
        low_tex = f"{'' if g == 1 else g}{_pow(v, low)}({_sum_tex([(a, _pow(v, j + 1)), (sign * b, _pow(v, 1))])})"
        low_typed = f"{'' if g == 1 else g}{_pow(v, low, True)}({_sum_tex([(a, _pow(v, j + 1, True)), (sign * b, v)])})"
        items = [("sign_slip", math(wrong_sign), wrong_sign, ("t", wrong_sign))]
        if low >= 0:
            items.append(("power_too_low", math(low_tex), "", ("low", low)))
        if g > 1:
            only_number = f"{g}({_sum_tex([(a, _pow(v, k + j)), (sign * b, _pow(v, k))])})"
            items.append(("not_complete", math(only_number), "", ("num", g)))
        else:
            only_letter = f"{_pow(v, k)}({_sum_tex([(a, _pow(v, j)), (sign * b, '')])})"
            items.append(("not_complete", math(only_letter), "", ("let", k)))
        steps = [("Find the highest common factor of the numbers and of the letters", f"{'' if g == 1 else g}{_pow(v, k, True)}"),
                 ("Divide each term by it and write the results in the bracket", _sum_tex([(a, _pow(v, j, True)), (sign * b, '')]))]
        return _factorised_built("common_letter_factor", expression, answer_tex, answer_typed, items, steps,
                                 {"g": g, "a": a, "b": b, "k": k, "j": j, "sign": sign, "var": v})
    raise GeneratorError("level 2 could not find a problem")


def _factor_level3(rng: SeededRandom) -> _Built:
    for _ in range(_MAX_ATTEMPTS):
        two_letters = rng.chance(2, 3)
        u, w = rng.choice(_LETTER_PAIRS) if two_letters else (rng.choice(("a", "m", "p", "x", "y")), "")
        common = rng.chance(1, 2)
        g = rng.choice((2, 3, 5)) if common else 1
        a, b = rng.randint(1, 7), rng.randint(1, 9)
        if gcd(a, b) != 1 or (not two_letters and not common and a == 1 and b == 1):
            continue
        first = _pow(u, 2)
        second = _pow(w, 2) if two_letters else ""
        expression = _sum_tex([(g * a * a, first), (-g * b * b, second)])
        left = _sum_tex([(a, u), (-b, w)])
        right = _sum_tex([(a, u), (b, w)])
        pre = "" if g == 1 else str(g)
        answer = f"{pre}({left})({right})"
        sq_typed = f"{pre}({left})^2"
        unrooted = f"{pre}({_sum_tex([(a * a, u), (-b * b, w)])})({_sum_tex([(a * a, u), (b * b, w)])})"
        items = [("squared_bracket", math(f"{pre}({left})^{{2}}"), sq_typed, ("sq",)),
                 ("squares_not_rooted", math(unrooted), unrooted, ("ur",))]
        if g > 1:
            items.append(("factor_lost", math(f"({left})({right})"), f"({left})({right})", ("lost",)))
            items.append(("not_complete", math(f"{g}({_sum_tex([(a * a, first), (-b * b, second)])})"), "", ("inc",)))
        steps = []
        if g > 1:
            steps.append(("Take out the common factor", f"{g}({_sum_tex([(a * a, first), (-b * b, second)])})"))
        steps.append(("Write each square as a square, then use the difference of two squares", answer))
        return _factorised_built("difference_of_squares", expression, answer, answer, items, steps,
                                 {"g": g, "a": a, "b": b, "letters": [u, w]})
    raise GeneratorError("level 3 could not find a problem")


def _factor_level4(rng: SeededRandom) -> _Built:
    for _ in range(_MAX_ATTEMPTS):
        u, v, w = rng.choice((("x", "z", "y"), ("m", "n", "p"), ("a", "c", "b"), ("p", "r", "q"), ("s", "u", "t")))
        a, c = rng.randint(1, 4), rng.randint(1, 4)
        b, d = _nonzero(rng, 5), _nonzero(rng, 3)
        if gcd(a, abs(b)) != 1 or gcd(c, abs(d)) != 1:
            continue
        terms = [(a * c, ''.join(sorted(u + w))), (a * d, u), (b * c, ''.join(sorted(v + w))), (b * d, v)]
        expression = _sum_tex(terms)
        first = _sum_tex([(a, u), (b, v)])
        second = _sum_tex([(c, w), (d, "")])
        answer = f"({first})({second})"
        wrong_second = f"({first})({_sum_tex([(c, w), (-d, '')])})"
        wrong_first = f"({_sum_tex([(a, u), (-b, v)])})({second})"
        grouped = f"{_term_tex(a, u, True)}({second}){_term_tex(b, v, False)}({second})"
        swapped = f"({_sum_tex([(a, u), (d, '')])})({_sum_tex([(c, w), (b, v)])})"
        items = [("sign_slip_second", math(wrong_second), wrong_second, ("s2",)),
                 ("sign_slip_first", math(wrong_first), wrong_first, ("s1",)),
                 ("not_combined", math(grouped), "", ("grp",)),
                 ("brackets_swapped", math(swapped), swapped, ("sw",))]
        steps = [("Group the terms in pairs and take out the common factor of each pair", grouped.replace(" ", "")),
                 ("Take out the common bracket", answer)]
        return _factorised_built("factorise_by_grouping", expression, answer, answer, items, steps,
                                 {"a": a, "b": b, "c": c, "d": d, "letters": [u, v, w]})
    raise GeneratorError("level 4 could not find a problem")


class FactorisationBasicsGenerator(_FamilyGenerator):
    generator_id = FACTORISATION_ID
    version = 2
    levels = (1, 2, 3, 4)
    level_skills = FACTORISATION_LEVEL_SKILLS
    error_notes = FACTORISATION_ERROR_NOTES
    builders = {1: _factor_level1, 2: _factor_level2, 3: _factor_level3, 4: _factor_level4}



# ==========================================================================
# Lesson 15823: Solving Quadratic Equations
# ==========================================================================

QUADRATIC_ERROR_NOTES: Dict[str, Dict[str, str]] = {
    "solve_factorised": {
        "signs_swapped": "gave each root the wrong sign (wrote the number in the bracket instead of its opposite)",
        "coefficient_ignored": "gave the opposite of each number in the brackets and did not divide by the number in front of x",
        "one_root_only": "found the root from one bracket and forgot the other bracket",
    },
    "solve_square": {
        "positive_only": "found the positive square root and forgot the negative one",
        "not_divided": "took the square root before dividing by the number in front of the squared letter",
        "root_forgotten": "divided correctly but did not take the square root",
    },
    "solve_by_factorising_monic": {
        "signs_swapped": "gave each root the wrong sign (wrote the number in the bracket instead of its opposite)",
        "one_sign_wrong": "gave one of the two roots the wrong sign",
        "one_root_only": "found one root and forgot the other",
    },
    "solve_by_factorising_general": {
        "signs_swapped": "gave each root the wrong sign (wrote the number in the bracket instead of its opposite)",
        "coefficient_ignored": "gave the opposite of each number in the brackets and did not divide by the number in front of x",
        "one_root_only": "found one root and forgot the other",
    },
    "quadratic_formula": {
        "sign_of_b": "used b instead of -b at the start of the formula",
        "divided_by_a": "divided by a instead of by 2a",
        "discriminant_sign": "added 4ac to b squared instead of subtracting it",
    },
    "quadratic_context_length": {
        "negative_root": "gave the negative root, which cannot be a length",
        "sign_of_b": "used b instead of -b at the start of the formula",
        "two_significant_figures": "gave the answer to two significant figures instead of three",
        "forgot_half": "forgot to divide by 2a at the end",
    },
}

QUADRATIC_LEVEL_SKILLS: Dict[int, Tuple[str, ...]] = {
    1: ("solve_factorised",),
    2: ("solve_square",),
    3: ("solve_by_factorising_monic",),
    4: ("solve_by_factorising_general",),
    5: ("quadratic_formula", "quadratic_context_length"),
}

_UNKNOWNS = ("x", "x", "x", "y", "p", "q", "t", "m")


def _rkey(values: Sequence[float]) -> Tuple:
    return tuple(sorted(round(float(v), 9) for v in values))


def _roots_answer(var: str, roots: Sequence[Fraction]) -> Tuple[str, List[str]]:
    """(display answer, expected typed answers) with the roots in increasing order."""
    ordered = sorted(roots)
    display = " or ".join(math(f"{var} = {number_latex(r)}") for r in ordered)
    typed = " or ".join(f"{var} = {_t(r)}" for r in ordered)
    return display, [typed]


def _roots_item(code: str, var: str, roots: Sequence[Fraction]):
    ordered = sorted(roots)
    display = " or ".join(math(f"{var} = {number_latex(r)}") for r in ordered)
    typed = " or ".join(f"{var} = {_t(r)}" for r in ordered)
    return (code, display, typed, _rkey(roots))


def _bracket_tex(m: int, k: int, var: str) -> str:
    """``(2x - 1)``, or ``(4 - x)`` when the coefficient of x is negative."""
    if m < 0:
        return f"({k} - {'' if m == -1 else abs(m)}{var})"
    return f"({linear_latex(m, k, var)})"


def _quadratic_built(skill: str, question: str, var: str, roots: Sequence[Fraction],
                     wrongs: Sequence[Tuple[str, Sequence[Fraction]]], steps: Sequence[Tuple[str, str]],
                     machine: Dict[str, Any], extra_expected: Sequence[str] = ()) -> _Built:
    display, expected = _roots_answer(var, roots)
    return _Built(
        skill=skill, question=question, answer=display,
        items=[_roots_item(code, var, r) for code, r in wrongs],
        correct_key=_rkey(roots),
        machine={**machine, "task": skill, "var": var, "roots": [[r.numerator, r.denominator] for r in sorted(roots)]},
        steps=list(steps),
        marking=_marking("equation_solution", [*expected, *extra_expected]),
    )


def _quadratic_level1(rng: SeededRandom) -> _Built:
    for _ in range(_MAX_ATTEMPTS):
        var = rng.choice(_UNKNOWNS)
        m1 = rng.choice((1, 1, 1, 2, 3, -1))
        m2 = rng.choice((1, 1, 1, 2, 3))
        k1, k2 = _nonzero(rng, 8), _nonzero(rng, 8)
        r1, r2 = Fraction(-k1, m1), Fraction(-k2, m2)
        if r1 == r2 or (m1 < 0 and m2 < 0):
            continue
        question = f"Solve {math(f'{_bracket_tex(m1, k1, var)}{_bracket_tex(m2, k2, var)} = 0')}."
        ignored = [Fraction(-k1), Fraction(-k2)] if (m1 != 1 or m2 != 1) else [Fraction(k1), Fraction(k2)]
        wrongs = [("signs_swapped", [-r1, -r2]), ("one_root_only", [r1])]
        if ignored[0] != ignored[1]:
            wrongs.insert(1, ("coefficient_ignored", ignored))
        steps = [("Set the first bracket equal to zero and solve", f"{var} = {_t(r1)}"),
                 ("Set the second bracket equal to zero and solve", f"{var} = {_t(r2)}")]
        return _quadratic_built("solve_factorised", question, var, [r1, r2], wrongs, steps,
                                {"factors": [[m1, k1], [m2, k2]]})
    raise GeneratorError("level 1 could not find a problem")


def _quadratic_level2(rng: SeededRandom) -> _Built:
    for _ in range(_MAX_ATTEMPTS):
        var = rng.choice(_UNKNOWNS)
        r = rng.randint(2, 12)
        a = rng.choice((1, 2, 3, 4, 5, 6, 7))
        k = a * r * r
        shape = rng.choice(("equals", "equals", "minus", "reversed"))
        lead = "" if a == 1 else str(a)
        if shape == "equals":
            question_tex = f"{lead}{var}^{{2}} = {k}"
        elif shape == "minus":
            question_tex = f"{lead}{var}^{{2}} - {k} = 0"
        else:
            question_tex = f"{k} = {lead}{var}^{{2}}"
        roots = [Fraction(r), Fraction(-r)]
        items = [_roots_item("positive_only", var, [Fraction(r)]),
                 ("not_divided", " or ".join(math(f"{var} = {sg}\\sqrt{{{k}}}") for sg in ("-", "")),
                  f"{var} = sqrt({k}) or {var} = -sqrt({k})", _surd_key(k)),
                 _roots_item("root_forgotten", var, [Fraction(k, a), Fraction(-k, a)])]
        display, expected = _roots_answer(var, roots)
        steps = [("Divide both sides by the number in front", f"{var}^2 = {r * r}"),
                 ("Take the square root, giving two answers", f"{var} = {r} or {var} = {-r}")]
        return _Built(
            skill="solve_square", question=f"Solve {math(question_tex)}.", answer=display, items=items,
            correct_key=_rkey(roots),
            machine={"task": "solve_square", "var": var, "a": a, "k": k, "roots": [[r, 1], [-r, 1]]},
            steps=steps, marking=_marking("equation_solution", [*expected, f"± {r}"]),
        )
    raise GeneratorError("level 2 could not find a problem")


def _surd_key(k: int) -> Tuple:
    root = k ** 0.5
    return _rkey([root, -root])


def _monic_forms(rng: SeededRandom, var: str, r1: int, r2: int) -> Tuple[str, str]:
    """(question LaTeX, shape name) for ``(var - r1)(var - r2) = 0`` written three ways."""
    s, p = r1 + r2, r1 * r2
    shape = rng.choice(("standard", "constant_right", "rearranged"))
    sq = f"{var}^{{2}}"

    def lhs(sign_s: int, sign_p: int) -> str:
        return _sum_tex([(1, sq), (sign_s * s, var), (sign_p * p, "")])

    if shape == "standard":
        return f"{lhs(-1, 1)} = 0", shape
    if shape == "constant_right":
        return f"{_sum_tex([(1, sq), (-s, var)])} = {-p}", shape
    return f"{sq} = {_sum_tex([(s, var), (-p, '')])}", shape


def _quadratic_level3(rng: SeededRandom) -> _Built:
    for _ in range(_MAX_ATTEMPTS):
        var = rng.choice(_UNKNOWNS)
        r1, r2 = rng.randint(-9, 9), rng.randint(-9, 9)
        if r1 == r2 or r1 == 0 or r2 == 0 or r1 + r2 == 0:
            continue
        tex, shape = _monic_forms(rng, var, r1, r2)
        roots = [Fraction(r1), Fraction(r2)]
        wrongs = [("signs_swapped", [Fraction(-r1), Fraction(-r2)]),
                  ("one_sign_wrong", [Fraction(-r1), Fraction(r2)]),
                  ("one_root_only", [Fraction(r1)])]
        steps = [("Write the equation as a quadratic equal to zero and factorise",
                  f"({var} {'-' if r1 > 0 else '+'} {abs(r1)})({var} {'-' if r2 > 0 else '+'} {abs(r2)}) = 0"),
                 ("Set each bracket equal to zero", f"{var} = {r1} or {var} = {r2}")]
        return _quadratic_built("solve_by_factorising_monic", f"Solve {math(tex)}.", var, roots, wrongs, steps,
                                {"r": [r1, r2], "shape": shape})
    raise GeneratorError("level 3 could not find a problem")


def _quadratic_level4(rng: SeededRandom) -> _Built:
    for _ in range(_MAX_ATTEMPTS):
        var = rng.choice(("x", "x", "x", "y", "p", "t"))
        m1, m2 = rng.randint(1, 3), rng.randint(1, 3)
        if m1 * m2 < 2:
            continue
        k1, k2 = _nonzero(rng, 6), _nonzero(rng, 6)
        if gcd(m1, abs(k1)) != 1 or gcd(m2, abs(k2)) != 1:
            continue
        r1, r2 = Fraction(-k1, m1), Fraction(-k2, m2)
        if r1 == r2:
            continue
        a, b, c = m1 * m2, m1 * k2 + m2 * k1, k1 * k2
        sq = f"{var}^{{2}}"
        shape = rng.choice(("standard", "constant_right", "rearranged"))
        if shape == "standard":
            tex = f"{_sum_tex([(a, sq), (b, var), (c, '')])} = 0"
        elif shape == "constant_right":
            tex = f"{_sum_tex([(a, sq), (b, var)])} = {-c}"
        else:
            tex = f"{_sum_tex([(a, sq)])} = {_sum_tex([(-b, var), (-c, '')])}"
        wrongs = [("signs_swapped", [-r1, -r2]),
                  ("coefficient_ignored", [Fraction(-k1), Fraction(-k2)]),
                  ("one_root_only", [r1])]
        steps = [("Write the equation as a quadratic equal to zero and factorise",
                  f"({_t(m1) if m1 != 1 else ''}{var} {'+' if k1 > 0 else '-'} {abs(k1)})"
                  f"({_t(m2) if m2 != 1 else ''}{var} {'+' if k2 > 0 else '-'} {abs(k2)}) = 0"),
                 ("Set each bracket equal to zero and solve", f"{var} = {_t(r1)} or {var} = {_t(r2)}")]
        return _quadratic_built("solve_by_factorising_general", f"Solve {math(tex)}.", var, [r1, r2], wrongs, steps,
                                {"abc": [a, b, c], "factors": [[m1, k1], [m2, k2]], "shape": shape})
    raise GeneratorError("level 4 could not find a problem")


def _sqrt_decimal(n: int) -> Decimal:
    getcontext().prec = 50
    return Decimal(n).sqrt()


def _dp(value: Decimal, places: int) -> Decimal:
    return value.quantize(Decimal(1).scaleb(-places), rounding=ROUND_HALF_UP)


def _sf(value: Decimal, digits: int) -> Decimal:
    exponent = value.adjusted() - (digits - 1)
    return value.quantize(Decimal(1).scaleb(exponent), rounding=ROUND_HALF_UP)


def _dec_text(value: Decimal) -> str:
    text = format(value, "f")
    return "0" if text in ("-0", "-0.0", "-0.00") else text


def _formula_roots(a: int, b: int, c: int, sign_b: int = -1, denominator: Optional[int] = None,
                   disc: Optional[int] = None) -> List[Decimal]:
    d = _sqrt_decimal(b * b - 4 * a * c if disc is None else disc)
    den = Decimal(2 * a if denominator is None else denominator)
    return [(Decimal(sign_b * b) + d) / den, (Decimal(sign_b * b) - d) / den]


def _quadratic_formula(rng: SeededRandom) -> _Built:
    for _ in range(_MAX_ATTEMPTS):
        var = rng.choice(("x", "x", "x", "y", "p"))
        a, b, c = rng.randint(1, 4), _nonzero(rng, 9), _nonzero(rng, 12)
        disc = b * b - 4 * a * c
        if disc <= 0 or isqrt(disc) ** 2 == disc:
            continue
        roots = [_dp(r, 2) for r in _formula_roots(a, b, c)]
        wrong_b = [_dp(r, 2) for r in _formula_roots(a, b, c, sign_b=1)]
        wrong_a = [_dp(r, 2) for r in _formula_roots(a, b, c, denominator=a)]
        alt_disc = b * b + 4 * a * c
        wrongs_raw = [("sign_of_b", wrong_b), ("divided_by_a", wrong_a)]
        if alt_disc > 0:
            wrongs_raw.append(("discriminant_sign", [_dp(r, 2) for r in _formula_roots(a, b, c, disc=alt_disc)]))
        if any(r == 0 for r in roots) or roots[0] == roots[1]:
            continue
        sq = f"{var}^{{2}}"
        if rng.chance(1, 2):
            tex = f"{_sum_tex([(a, sq), (b, var), (c, '')])} = 0"
        else:
            tex = f"{_sum_tex([(a, sq), (b, var)])} = {-c}"
        question = f"Solve {math(tex)}, giving your answers correct to 2 decimal places."

        def text_of(values: Sequence[Decimal]) -> Tuple[str, str]:
            ordered = sorted(values)
            return (" or ".join(math(f"{var} = {_dec_text(v)}") for v in ordered),
                    " or ".join(f"{var} = {_dec_text(v)}" for v in ordered))

        display, typed = text_of(roots)
        items = []
        for code, values in wrongs_raw:
            d_text, t_text = text_of(values)
            items.append((code, d_text, t_text, _rkey([float(v) for v in values])))
        steps = [("Write down a, b and c and substitute into the formula", f"a = {a}, b = {b}, c = {c}"),
                 ("Work out the discriminant", str(disc)),
                 ("Calculate both roots to 2 decimal places", typed)]
        return _Built(
            skill="quadratic_formula", question=question, answer=display, items=items,
            correct_key=_rkey([float(r) for r in roots]),
            machine={"task": "quadratic_formula", "var": var, "abc": [a, b, c], "disc": disc,
                     "roots_2dp": [_dec_text(r) for r in sorted(roots)]},
            steps=steps, marking=_marking("equation_solution", [typed]),
        )
    raise GeneratorError("level 5 could not find a quadratic-formula problem")


_GARDENS = ("vegetable garden at Rundu", "rectangular school plot in Katima Mulilo",
            "rectangular field near Keetmanshoop", "rectangular playground in Swakopmund",
            "rectangular classroom floor in Oshakati")


def _quadratic_context(rng: SeededRandom) -> _Built:
    for _ in range(_MAX_ATTEMPTS):
        k = rng.randint(2, 9)
        area = rng.randint(10, 150)
        disc = k * k + 4 * area
        if isqrt(disc) ** 2 == disc:
            continue
        d = _sqrt_decimal(disc)
        positive = (-Decimal(k) + d) / 2
        negative = (-Decimal(k) - d) / 2
        correct = _sf(positive, 3)
        wrong_neg = _sf(negative, 3)
        wrong_b = _sf((Decimal(k) + d) / 2, 3)
        wrong_half = _sf(-Decimal(k) + d, 3)
        wrong_2sf = _sf(positive, 2)
        place = rng.choice(_GARDENS)
        question = (f"A {place} has length {math(f'(x + {k})')} metres and width {math('x')} metres. "
                    f"Its area is {area} square metres. Calculate the value of {math('x')}, "
                    f"correct to 3 significant figures.")
        items = [("negative_root", math(_dec_text(wrong_neg)), _dec_text(wrong_neg), float(wrong_neg)),
                 ("sign_of_b", math(_dec_text(wrong_b)), _dec_text(wrong_b), float(wrong_b)),
                 ("two_significant_figures", math(_dec_text(wrong_2sf)), _dec_text(wrong_2sf), float(wrong_2sf)),
                 ("forgot_half", math(_dec_text(wrong_half)), _dec_text(wrong_half), float(wrong_half))]
        steps = [("Write the area as an equation and rearrange to equal zero", f"x^2 + {k}x - {area} = 0"),
                 ("Use the quadratic formula and keep the positive root", _dec_text(correct))]
        return _Built(
            skill="quadratic_context_length", question=question, answer=math(_dec_text(correct)), items=items,
            correct_key=float(correct),
            machine={"task": "quadratic_context_length", "k": k, "area": area, "disc": disc,
                     "root_3sf": _dec_text(correct)},
            steps=steps, marking=_marking("number_rounded", [_dec_text(correct)], rounding="sig_figs", digits=3),
        )
    raise GeneratorError("level 5 could not find a context problem")


def _quadratic_level5(rng: SeededRandom) -> _Built:
    return _quadratic_formula(rng) if rng.chance(3, 5) else _quadratic_context(rng)


class SolvingQuadraticEquationsGenerator(_FamilyGenerator):
    generator_id = QUADRATIC_ID
    version = 1
    levels = (1, 2, 3, 4, 5)
    level_skills = QUADRATIC_LEVEL_SKILLS
    error_notes = QUADRATIC_ERROR_NOTES
    builders = {1: _quadratic_level1, 2: _quadratic_level2, 3: _quadratic_level3,
                4: _quadratic_level4, 5: _quadratic_level5}



# ==========================================================================
# Coordinate geometry helpers (lessons 15831, 15835, 15836, 15837)
# ==========================================================================


def _mx_tex(m: Fraction, var: str = "x") -> str:
    sign = "-" if m < 0 else ""
    mag = abs(m)
    if mag.denominator == 1:
        return f"{sign}{var}" if mag == 1 else f"{sign}{int(mag)}{var}"
    return f"{sign}\\frac{{{mag.numerator}}}{{{mag.denominator}}}{var}"


def _line_tex(m: Fraction, c: Fraction) -> str:
    """``y = \\frac{3}{4}x - 2`` (c may be zero; m is never zero)."""
    out = f"y = {_mx_tex(m)}"
    if c != 0:
        out += f" {'+' if c > 0 else '-'} {number_latex(abs(c))}"
    return out


def _mx_typed(m: Fraction, dec: bool = False) -> str:
    sign = "-" if m < 0 else ""
    mag = abs(m)
    if dec:
        text = _decimal(mag)
        return f"{sign}{'' if text == '1' else text}x"
    if mag.denominator == 1:
        return f"{sign}{'' if mag == 1 else int(mag)}x"
    return f"{sign}{'' if mag.numerator == 1 else mag.numerator}x/{mag.denominator}"


def _line_typed(m: Fraction, c: Fraction, dec: bool = False) -> str:
    out = f"y = {_mx_typed(m, dec)}"
    if c != 0:
        out += f" {'+' if c > 0 else '-'} {(_decimal(abs(c)) if dec else _t(abs(c)))}"
    return out


def _line_expected(m: Fraction, c: Fraction) -> List[str]:
    forms = [_line_typed(m, c)]
    if _decimal(m) is not None and _decimal(c) is not None:
        alt = _line_typed(m, c, dec=True)
        if alt not in forms:
            forms.append(alt)
    return forms


def _line_key(m: Fraction, c: Fraction) -> Tuple:
    return ("line", m, c)


def _line_item(code: str, m: Fraction, c: Fraction):
    return (code, math(_line_tex(m, c)), _line_typed(m, c), _line_key(m, c))


def _pt(name: str, x, y) -> str:
    return f"{name}({number_latex(x)}, {number_latex(y)})"


def _pt_typed(x, y) -> str:
    return f"({_t(x)}, {_t(y)})"


def _pt_expected(x, y) -> List[str]:
    forms = [_pt_typed(x, y)]
    dx, dy = _decimal(x), _decimal(y)
    if dx is not None and dy is not None and (dx != _t(x) or dy != _t(y)):
        forms.append(f"({dx}, {dy})")
    return forms


def _pt_item(code: str, x, y):
    return (code, math(point_latex(Fraction(x), Fraction(y))), _pt_typed(x, y), ("pt", Fraction(x), Fraction(y)))


def _num_item(code: str, value):
    value = Fraction(value)
    return (code, math(number_latex(value)), _t(value), ("n", value))


def _number_built(skill: str, question: str, value, items, steps, machine, answer_type: str = "number_exact") -> _Built:
    value = Fraction(value)
    return _Built(skill=skill, question=question, answer=math(number_latex(value)), items=items,
                  correct_key=("n", value), machine={**machine, "task": skill}, steps=steps,
                  marking=_marking(answer_type, _num_forms(value)))


def _point_built(skill: str, question: str, x, y, items, steps, machine) -> _Built:
    x, y = Fraction(x), Fraction(y)
    return _Built(skill=skill, question=question, answer=math(point_latex(x, y)), items=items,
                  correct_key=("pt", x, y), machine={**machine, "task": skill}, steps=steps,
                  marking=_marking("coordinates", _pt_expected(x, y)))


def _line_built(skill: str, question: str, m: Fraction, c: Fraction, items, steps, machine) -> _Built:
    return _Built(skill=skill, question=question, answer=math(_line_tex(m, c)), items=items,
                  correct_key=_line_key(m, c), machine={**machine, "task": skill}, steps=steps,
                  marking=_marking("expression", _line_expected(m, c)))


_POINT_NAMES = (("A", "B"), ("P", "Q"), ("C", "D"), ("E", "F"), ("R", "S"), ("K", "L"))
_TRIPLES = ((3, 4, 5), (6, 8, 10), (5, 12, 13), (8, 15, 17), (9, 12, 15), (12, 16, 20), (7, 24, 25), (20, 21, 29))


# ==========================================================================
# Lesson 15831: Straight Line Graphs and Gradients
# ==========================================================================

LINE_GRAPH_ERROR_NOTES: Dict[str, Dict[str, str]] = {
    "gradient_from_equation": {
        "constant_as_gradient": "gave the constant term of the equation as the gradient",
        "sign_lost": "gave the size of the gradient but ignored the minus sign in front of the x term",
    },
    "intercept_from_equation": {
        "coordinates_swapped": "wrote the y-intercept with the coordinates the wrong way round, as a point on the x-axis",
        "gradient_as_intercept": "gave the gradient as the y-coordinate of the point where the line meets the y-axis",
    },
    "gradient_two_points": {
        "inverted": "divided the change in x by the change in y instead of the change in y by the change in x",
        "sign_error": "subtracted the coordinates in a different order on the top and the bottom, so the sign is wrong",
        "added": "added the coordinates instead of subtracting them",
    },
    "gradient_general_form": {
        "sign_lost": "rearranged correctly but lost the minus sign, giving the gradient as a divided by b",
        "coefficient_of_x": "gave the number in front of x as the gradient without rearranging the equation",
    },
    "intercept_general_form": {
        "not_divided": "gave the right-hand number as the y-coordinate without dividing by the number in front of y",
        "x_intercept": "found where the line meets the x-axis instead of the y-axis",
    },
    "point_on_line_value": {
        "sign_slip": "subtracted the constant instead of adding it after multiplying",
        "forgot_constant": "multiplied by the gradient but forgot to add the constant term",
    },
    "find_intercept_constant": {
        "sign_slip": "added the gradient times x instead of subtracting it when finding the constant",
        "forgot_gradient": "used the y-coordinate of the point as the constant without allowing for the gradient",
    },
    "axis_intercepts": {
        "order_swapped": "gave the intercepts the wrong way round, as (0, x-value) and (y-value, 0)",
        "coefficients_used": "gave the coefficients of x and y as the intercepts",
        "sign_slip": "made a sign error when dividing, so the intercepts have the wrong signs",
    },
}

LINE_GRAPH_LEVEL_SKILLS: Dict[int, Tuple[str, ...]] = {
    1: ("gradient_from_equation", "intercept_from_equation"),
    2: ("gradient_two_points",),
    3: ("gradient_general_form", "intercept_general_form"),
    4: ("point_on_line_value", "find_intercept_constant"),
    5: ("axis_intercepts",),
}


def _form_variants(m: Fraction, c: Fraction, kind: str) -> str:
    """LaTeX for y = mx + c written as ``y = mx + c``, ``y = c + mx`` or ``y = c - kx``."""
    if kind == "mc":
        return _line_tex(m, c)
    const = number_latex(c)
    if m < 0:
        mag = abs(m)
        body = f"{'' if mag == 1 else number_latex(mag)}x" if mag.denominator == 1 else _mx_tex(mag)
        return f"y = {const} - {body}"
    return f"y = {const} + {_mx_tex(m)}"


def _line_graph_level1(rng: SeededRandom) -> _Built:
    for _ in range(_MAX_ATTEMPTS):
        fractional = rng.chance(1, 5)
        m = Fraction(_nonzero(rng, 9)) if not fractional else Fraction(_nonzero(rng, 5), rng.choice((2, 3, 4)))
        c = Fraction(_nonzero(rng, 9))
        if m.denominator != 1 and gcd(abs(m.numerator), m.denominator) != 1:
            continue
        kind = rng.choice(("mc", "c_minus", "c_plus"))
        if kind == "c_minus" and m > 0:
            m = -m
        if kind == "c_plus" and m < 0:
            m = -m
        equation = _form_variants(m, c, kind)
        if rng.chance(2, 3):
            items = [_num_item("constant_as_gradient", c), _num_item("sign_lost", -m)]
            steps = [("Compare with y = mx + c; the gradient is the number multiplying x", _t(m))]
            return _number_built("gradient_from_equation", f"Write down the gradient of the line {math(equation)}.", m,
                                 items, steps, {"m": [m.numerator, m.denominator], "c": int(c), "kind": kind})
        items = [("coordinates_swapped", math(point_latex(c, Fraction(0))), _pt_typed(c, 0), ("pt", c, Fraction(0))),
                 ("gradient_as_intercept", math(point_latex(Fraction(0), m)), _pt_typed(0, m), ("pt", Fraction(0), m))]
        steps = [("The line meets the y-axis where x = 0, so y is the constant term", _t(c))]
        return _point_built("intercept_from_equation",
                            f"Write down the coordinates of the point where the line {math(equation)} meets the y-axis.",
                            0, c, items, steps, {"m": [m.numerator, m.denominator], "c": int(c), "kind": kind})
    raise GeneratorError("level 1 could not find a problem")


def _line_graph_level2(rng: SeededRandom) -> _Built:
    for _ in range(_MAX_ATTEMPTS):
        n1, n2 = rng.choice(_POINT_NAMES)
        x1, y1 = rng.randint(-8, 8), rng.randint(-8, 8)
        dx, dy = _nonzero(rng, 8), _nonzero(rng, 8)
        x2, y2 = x1 + dx, y1 + dy
        m = Fraction(dy, dx)
        if not (-9 <= x2 <= 9 and -9 <= y2 <= 9) or rng.chance(1, 3) and m.denominator == 1:
            continue
        items = [_num_item("inverted", Fraction(dx, dy)), _num_item("sign_error", -m)]
        if x1 + x2 != 0:
            items.append(_num_item("added", Fraction(y1 + y2, x1 + x2)))
        steps = [("Find the change in y and the change in x", f"{dy} and {dx}"),
                 ("Divide the change in y by the change in x", _t(m))]
        question = (f"The points {math(_pt(n1, x1, y1))} and {math(_pt(n2, x2, y2))} lie on a straight line. "
                    f"Calculate the gradient of the line.")
        return _number_built("gradient_two_points", question, m, items, steps,
                             {"p1": [x1, y1], "p2": [x2, y2]})
    raise GeneratorError("level 2 could not find a problem")


def _general_form(a: int, b: int, c: int) -> str:
    return f"{_sum_tex([(a, 'x'), (b, 'y')])} = {c}"


def _line_graph_level3(rng: SeededRandom) -> _Built:
    for _ in range(_MAX_ATTEMPTS):
        a, b, c = _nonzero(rng, 8), _nonzero(rng, 6), _nonzero(rng, 18)
        if abs(a) == abs(b) and rng.chance(1, 2):
            continue
        equation = _general_form(a, b, c)
        if rng.chance(1, 2):
            m = Fraction(-a, b)
            items = [_num_item("sign_lost", Fraction(a, b)), _num_item("coefficient_of_x", Fraction(a))]
            steps = [("Rearrange to make y the subject", f"y = {_t(Fraction(-a, b))}x + {_t(Fraction(c, b))}".replace("+ -", "- ")),
                     ("The gradient is the coefficient of x", _t(m))]
            return _number_built("gradient_general_form", f"Find the gradient of the line {math(equation)}.", m, items,
                                 steps, {"abc": [a, b, c]})
        y0 = Fraction(c, b)
        items = [("not_divided", math(point_latex(Fraction(0), Fraction(c))), _pt_typed(0, c), ("pt", Fraction(0), Fraction(c))),
                 ("x_intercept", math(point_latex(Fraction(c, a), Fraction(0))), _pt_typed(Fraction(c, a), 0),
                  ("pt", Fraction(c, a), Fraction(0)))]
        steps = [("Put x = 0 into the equation", f"{b}y = {c}"), ("Divide to find y", _t(y0))]
        return _point_built("intercept_general_form",
                            f"Find the coordinates of the point where the line {math(equation)} meets the y-axis.",
                            0, y0, items, steps, {"abc": [a, b, c]})
    raise GeneratorError("level 3 could not find a problem")


def _line_graph_level4(rng: SeededRandom) -> _Built:
    for _ in range(_MAX_ATTEMPTS):
        den = rng.choice((1, 1, 1, 2, 3))
        m = Fraction(_nonzero(rng, 6), den)
        c = Fraction(_nonzero(rng, 9))
        if m.denominator != 1 and gcd(abs(m.numerator), m.denominator) != 1:
            continue
        h = rng.randint(-6, 6) * m.denominator
        if h == 0 or abs(h) > 12:
            continue
        k = m * h + c
        if k.denominator != 1:
            continue
        equation = _line_tex(m, c)
        if rng.chance(1, 2):
            items = [_num_item("sign_slip", m * h - c), _num_item("forgot_constant", m * h)]
            steps = [("Substitute x into the equation", f"{_t(m * h)} + {_t(c)}".replace("+ -", "- ")),
                     ("Work out y", _t(k))]
            question = (f"The point {math(f'({h}, k)')} lies on the line {math(equation)}. "
                        f"Find the value of {math('k')}.")
            return _number_built("point_on_line_value", question, k, items, steps,
                                 {"m": [m.numerator, m.denominator], "c": int(c), "h": h})
        x0 = rng.randint(-6, 6) * m.denominator
        if x0 == 0:
            continue
        y0 = m * x0 + c
        if y0.denominator != 1:
            continue
        question = (f"The line {math(f'y = {_mx_tex(m)} + c')} passes through the point {math(f'({x0}, {int(y0)})')}. "
                    f"Find the value of {math('c')}.")
        items = [_num_item("sign_slip", y0 + m * x0), _num_item("forgot_gradient", y0)]
        steps = [("Substitute the coordinates of the point", f"{int(y0)} = {_t(m * x0)} + c"),
                 ("Solve for c", _t(c))]
        return _number_built("find_intercept_constant", question, c, items, steps,
                             {"m": [m.numerator, m.denominator], "point": [x0, int(y0)], "c": int(c)})
    raise GeneratorError("level 4 could not find a problem")


def _line_graph_level5(rng: SeededRandom) -> _Built:
    for _ in range(_MAX_ATTEMPTS):
        p, q = _nonzero(rng, 9), _nonzero(rng, 9)  # x-intercept p, y-intercept q
        scale = rng.randint(1, 3)
        if p == q and rng.chance(1, 2):
            continue
        a, b, c = scale * q, scale * p, scale * p * q
        equation = _general_form(a, b, c)
        expected_typed = f"({p}, 0), (0, {q})"
        answer = f"{math(f'({p}, 0)')} and {math(f'(0, {q})')}"
        items = [("order_swapped", f"{math(f'(0, {p})')} and {math(f'({q}, 0)')}", f"(0, {p}), ({q}, 0)", ("sw",)),
                 ("coefficients_used", f"{math(f'({a}, 0)')} and {math(f'(0, {b})')}", f"({a}, 0), (0, {b})", ("co",)),
                 ("sign_slip", f"{math(f'({-p}, 0)')} and {math(f'(0, {-q})')}", f"({-p}, 0), (0, {-q})", ("sg",))]
        steps = [("Put y = 0 to find where the line meets the x-axis", f"x = {p}"),
                 ("Put x = 0 to find where the line meets the y-axis", f"y = {q}")]
        question = (f"Find the coordinates of the points where the line {math(equation)} meets the x-axis and "
                    f"the y-axis, in that order.")
        return _Built(skill="axis_intercepts", question=question, answer=answer, items=items,
                      correct_key=("c", p, q),
                      machine={"task": "axis_intercepts", "abc": [a, b, c], "intercepts": [p, q]},
                      steps=steps, marking=_marking("coordinates", [expected_typed]))
    raise GeneratorError("level 5 could not find a problem")


class StraightLineGraphsGradientsGenerator(_FamilyGenerator):
    generator_id = LINE_GRAPH_ID
    version = 1
    levels = (1, 2, 3, 4, 5)
    level_skills = LINE_GRAPH_LEVEL_SKILLS
    error_notes = LINE_GRAPH_ERROR_NOTES
    builders = {1: _line_graph_level1, 2: _line_graph_level2, 3: _line_graph_level3,
                4: _line_graph_level4, 5: _line_graph_level5}



# ==========================================================================
# Lesson 15835: Distance, Midpoint, Gradient
# ==========================================================================

COORDINATE_ERROR_NOTES: Dict[str, Dict[str, str]] = {
    "midpoint": {
        "not_halved": "added the coordinates but forgot to divide by 2",
        "half_difference": "halved the differences between the coordinates instead of the sums",
        "mixed_up": "found the midpoint of the x values correctly but used the difference for the y values",
    },
    "distance_whole": {
        "no_square_root": "added the squares of the differences but did not take the square root",
        "added_differences": "added the differences in x and y instead of using Pythagoras' theorem",
    },
    "gradient_between_points": {
        "inverted": "divided the change in x by the change in y",
        "sign_error": "subtracted the coordinates in a different order on the top and the bottom, so the sign is wrong",
        "added": "added the coordinates instead of subtracting them",
    },
    "distance_surd": {
        "no_square_root": "added the squares of the differences but did not take the square root",
        "added_differences": "added the differences in x and y instead of using Pythagoras' theorem",
        "not_simplified": "left the square root unsimplified instead of writing it as a multiple of a smaller square root",
    },
    "midpoint_fraction": {
        "not_halved": "added the coordinates but forgot to divide by 2",
        "half_difference": "halved the differences between the coordinates instead of the sums",
        "mixed_up": "found the midpoint of the x values correctly but used the difference for the y values",
    },
    "find_other_end": {
        "used_difference": "subtracted the end point from the midpoint but did not double the result",
        "added": "added the end point to the midpoint instead of subtracting it from twice the midpoint",
        "midpoint_given_back": "gave the midpoint as the other end of the line",
    },
    "find_missing_coordinate_gradient": {
        "inverted": "used the gradient upside down when finding the missing coordinate",
        "sign_slip": "subtracted the change in y instead of adding it to the known y-coordinate",
        "forgot_start": "found the change in y but forgot to add it to the known y-coordinate",
    },
    "find_missing_coordinate_distance": {
        "one_value": "found only one of the two possible values",
        "no_square_root": "did not take the square root when finding the change in y",
    },
}

COORDINATE_LEVEL_SKILLS: Dict[int, Tuple[str, ...]] = {
    1: ("midpoint",),
    2: ("distance_whole",),
    3: ("gradient_between_points",),
    4: ("distance_surd", "midpoint_fraction"),
    5: ("find_other_end", "find_missing_coordinate_gradient", "find_missing_coordinate_distance"),
}


def _coordinate_level1(rng: SeededRandom) -> _Built:
    for _ in range(_MAX_ATTEMPTS):
        n1, n2 = rng.choice(_POINT_NAMES)
        x1, y1 = rng.randint(-9, 9), rng.randint(-9, 9)
        x2, y2 = rng.randint(-9, 9), rng.randint(-9, 9)
        if (x1 + x2) % 2 or (y1 + y2) % 2 or (x1, y1) == (x2, y2) or x1 == x2 or y1 == y2:
            continue
        mx, my = Fraction(x1 + x2, 2), Fraction(y1 + y2, 2)
        items = [_pt_item("not_halved", x1 + x2, y1 + y2),
                 _pt_item("half_difference", Fraction(x2 - x1, 2), Fraction(y2 - y1, 2)),
                 _pt_item("mixed_up", mx, Fraction(y2 - y1, 2))]
        steps = [("Add the x-coordinates and halve", _t(mx)), ("Add the y-coordinates and halve", _t(my))]
        question = (f"The points {math(_pt(n1, x1, y1))} and {math(_pt(n2, x2, y2))} are the ends of a line segment. "
                    f"Find the midpoint of {math(n1 + n2)}.")
        return _point_built("midpoint", question, mx, my, items, steps, {"p1": [x1, y1], "p2": [x2, y2]})
    raise GeneratorError("level 1 could not find a problem")


def _coordinate_level2(rng: SeededRandom) -> _Built:
    for _ in range(_MAX_ATTEMPTS):
        n1, n2 = rng.choice(_POINT_NAMES)
        a, b, length = rng.choice(_TRIPLES)
        dx, dy = (a, b) if rng.chance(1, 2) else (b, a)
        dx, dy = dx * rng.choice((1, -1)), dy * rng.choice((1, -1))
        x1, y1 = rng.randint(-9, 9), rng.randint(-9, 9)
        x2, y2 = x1 + dx, y1 + dy
        if abs(x2) > 25 or abs(y2) > 25:
            continue
        items = [_num_item("no_square_root", Fraction(dx * dx + dy * dy)),
                 _num_item("added_differences", Fraction(abs(dx) + abs(dy)))]
        steps = [("Find the differences in x and y", f"{abs(dx)} and {abs(dy)}"),
                 ("Add the squares of the differences", str(dx * dx + dy * dy)),
                 ("Take the square root", str(length))]
        question = (f"The points {math(_pt(n1, x1, y1))} and {math(_pt(n2, x2, y2))} are joined by a straight line. "
                    f"Calculate the length of {math(n1 + n2)}.")
        return _number_built("distance_whole", question, length, items, steps, {"p1": [x1, y1], "p2": [x2, y2]})
    raise GeneratorError("level 2 could not find a problem")


def _coordinate_level3(rng: SeededRandom) -> _Built:
    for _ in range(_MAX_ATTEMPTS):
        n1, n2 = rng.choice(_POINT_NAMES)
        x1, y1 = rng.randint(-8, 8), rng.randint(-8, 8)
        dx, dy = _nonzero(rng, 9), _nonzero(rng, 9)
        x2, y2 = x1 + dx, y1 + dy
        m = Fraction(dy, dx)
        if abs(x2) > 12 or abs(y2) > 12 or (m.denominator == 1 and rng.chance(2, 3)):
            continue
        items = [_num_item("inverted", Fraction(dx, dy)), _num_item("sign_error", -m),
                 _num_item("added", Fraction(y1 + y2, x1 + x2)) if x1 + x2 != 0 else _num_item("added", Fraction(dy * dx))]
        steps = [("Find the change in y and the change in x", f"{dy} and {dx}"),
                 ("Divide the change in y by the change in x", _t(m))]
        question = (f"Calculate the gradient of the line joining {math(_pt(n1, x1, y1))} and {math(_pt(n2, x2, y2))}.")
        return _number_built("gradient_between_points", question, m, items, steps,
                             {"p1": [x1, y1], "p2": [x2, y2]})
    raise GeneratorError("level 3 could not find a problem")


_SURD_SHAPES = tuple((a, b) for a in range(1, 9) for b in range(1, 9)
                     if a != b and _is_squarefree_part(a * a + b * b)[1] > 1 and _is_squarefree_part(a * a + b * b)[0] > 1)


def _coordinate_level4(rng: SeededRandom) -> _Built:
    if rng.chance(3, 5):
        for _ in range(_MAX_ATTEMPTS):
            n1, n2 = rng.choice(_POINT_NAMES)
            a, b = rng.choice(_SURD_SHAPES)
            dx, dy = a * rng.choice((1, -1)), b * rng.choice((1, -1))
            x1, y1 = rng.randint(-9, 9), rng.randint(-9, 9)
            x2, y2 = x1 + dx, y1 + dy
            total = dx * dx + dy * dy
            k, n = _is_squarefree_part(total)
            if abs(x2) > 14 or abs(y2) > 14:
                continue
            exact = _surd_typed(k, n)
            expected = [exact]
            items = [("no_square_root", math(str(total)), str(total), ("n", Fraction(total))),
                     ("added_differences", math(str(abs(dx) + abs(dy))), str(abs(dx) + abs(dy)),
                      ("n", Fraction(abs(dx) + abs(dy)))),
                     ("not_simplified", math(f"\\sqrt{{{total}}}"), "", ("raw", total))]
            steps = [("Add the squares of the differences", str(total)),
                     ("Write the square root as a multiple of a smaller square root", exact)]
            question = (''.join(['The points ', format(math(_pt(n1, x1, y1)), ''), ' and ', format(math(_pt(n2, x2, y2)), ''), ' are joined by a straight line. Find the length of ', format(math(n1 + n2), ''), ', giving your answer in the form ', format(math('k\\sqrt{n}'), ''), ' where ', format(math('n'), ''), ' is as small as possible.']))
            return _Built(skill="distance_surd", question=question, answer=math(_surd_latex(k, n)), items=items,
                          correct_key=("s", k, n),
                          machine={"task": "distance_surd", "p1": [x1, y1], "p2": [x2, y2], "k": k, "n": n},
                          steps=steps, marking=_marking("number_exact", expected))
        raise GeneratorError("level 4 could not find a distance problem")
    for _ in range(_MAX_ATTEMPTS):
        n1, n2 = rng.choice(_POINT_NAMES)
        x1, y1 = rng.randint(-9, 9), rng.randint(-9, 9)
        x2, y2 = rng.randint(-9, 9), rng.randint(-9, 9)
        if (x1 + x2) % 2 == 0 and (y1 + y2) % 2 == 0:
            continue
        if x1 == x2 or y1 == y2:
            continue
        mx, my = Fraction(x1 + x2, 2), Fraction(y1 + y2, 2)
        items = [_pt_item("not_halved", x1 + x2, y1 + y2),
                 _pt_item("half_difference", Fraction(x2 - x1, 2), Fraction(y2 - y1, 2)),
                 _pt_item("mixed_up", mx, Fraction(y2 - y1, 2))]
        steps = [("Add the x-coordinates and halve", _t(mx)), ("Add the y-coordinates and halve", _t(my))]
        question = (f"{math(_pt(n1, x1, y1))} and {math(_pt(n2, x2, y2))} are the ends of a line. "
                    f"Find the midpoint of {math(n1 + n2)}.")
        return _point_built("midpoint_fraction", question, mx, my, items, steps, {"p1": [x1, y1], "p2": [x2, y2]})
    raise GeneratorError("level 4 could not find a midpoint problem")


def _coordinate_level5(rng: SeededRandom) -> _Built:
    mode = rng.choice(("other_end", "gradient_k", "distance_k"))
    for _ in range(_MAX_ATTEMPTS):
        n1, n2 = rng.choice(_POINT_NAMES)
        if mode == "other_end":
            x1, y1 = rng.randint(-9, 9), rng.randint(-9, 9)
            qx, qy = rng.randint(-9, 9), rng.randint(-9, 9)
            if (qx, qy) == (x1, y1):
                continue
            mx, my = Fraction(x1 + qx, 2), Fraction(y1 + qy, 2)
            if mx.denominator != 1 or my.denominator != 1:
                continue
            items = [_pt_item("used_difference", mx - x1, my - y1), _pt_item("added", mx + x1, my + y1),
                     _pt_item("midpoint_given_back", mx, my)]
            steps = [("The x-coordinate of the end is twice the midpoint's minus the known one", str(qx)),
                     ("The y-coordinate of the end is twice the midpoint's minus the known one", str(qy))]
            question = (f"{math(n1 + n2)} is a line segment. The point {math(_pt(n1, x1, y1))} is one end and "
                        f"{math(_pt('M', mx, my))} is the midpoint of {math(n1 + n2)}. "
                        f"Find the coordinates of {math(n2)}.")
            return _point_built("find_other_end", question, qx, qy, items, steps,
                                {"p1": [x1, y1], "mid": [int(mx), int(my)], "p2": [qx, qy]})
        if mode == "gradient_k":
            num, den = _nonzero(rng, 5), rng.choice((1, 2, 3, 4))
            if gcd(abs(num), den) != 1:
                continue
            m = Fraction(num, den)
            x1, y1 = rng.randint(-6, 6), rng.randint(-6, 6)
            dx = den * rng.choice((-3, -2, -1, 1, 2, 3))
            x2 = x1 + dx
            k = y1 + m * dx
            if k.denominator != 1 or abs(k) > 20:
                continue
            items = [_num_item("inverted", y1 + dx / m), _num_item("sign_slip", y1 - m * dx),
                     _num_item("forgot_start", m * dx)]
            steps = [("Change in x", str(dx)), ("Change in y is the gradient times the change in x", _t(m * dx)),
                     ("Add it to the known y-coordinate", _t(k))]
            question = (f"The gradient of the line joining {math(_pt(n1, x1, y1))} and {math(f'{n2}({x2}, k)')} "
                        f"is {math(number_latex(m))}. Find the value of {math('k')}.")
            return _number_built("find_missing_coordinate_gradient", question, k, items, steps,
                                 {"p1": [x1, y1], "x2": x2, "m": [m.numerator, m.denominator]})
        a, b, length = rng.choice(_TRIPLES)
        dx, dy = (a, b) if rng.chance(1, 2) else (b, a)
        x1, y1 = rng.randint(-5, 5), rng.randint(-5, 5)
        x2 = x1 + dx * rng.choice((1, -1))
        k_values = [y1 + dy, y1 - dy]
        if abs(k_values[0]) > 30 or abs(k_values[1]) > 30:
            continue
        low, high = sorted(k_values)
        display = f"{math(f'k = {low}')} or {math(f'k = {high}')}"
        typed = f"k = {low} or k = {high}"
        wrong_sq = length * length - dx * dx
        items = [("one_value", math(f"k = {high}"), f"k = {high}", ("one", high)),
                 ("no_square_root", f"{math(f'k = {y1 - wrong_sq}')} or {math(f'k = {y1 + wrong_sq}')}",
                  f"k = {min(y1 - wrong_sq, y1 + wrong_sq)} or k = {max(y1 - wrong_sq, y1 + wrong_sq)}",
                  ("nr", wrong_sq))]
        steps = [("Use Pythagoras to find the difference in y", str(dy)),
                 ("Add and subtract it from the known y-coordinate", typed)]
        question = (f"The distance between {math(_pt(n1, x1, y1))} and {math(f'{n2}({x2}, k)')} is "
                    f"{length} units. Find the two possible values of {math('k')}.")
        return _Built(skill="find_missing_coordinate_distance", question=question, answer=display, items=items,
                      correct_key=("c", low, high),
                      machine={"task": "find_missing_coordinate_distance", "p1": [x1, y1], "x2": x2,
                               "length": length, "k": [low, high]},
                      steps=steps, marking=_marking("equation_solution", [typed]))
    raise GeneratorError("level 5 could not find a problem")


class DistanceMidpointGradientGenerator(_FamilyGenerator):
    generator_id = COORDINATE_ID
    version = 1
    levels = (1, 2, 3, 4, 5)
    level_skills = COORDINATE_LEVEL_SKILLS
    error_notes = COORDINATE_ERROR_NOTES
    builders = {1: _coordinate_level1, 2: _coordinate_level2, 3: _coordinate_level3,
                4: _coordinate_level4, 5: _coordinate_level5}



# ==========================================================================
# Lesson 15836: Equations of Straight Lines
# ==========================================================================

LINE_EQUATION_ERROR_NOTES: Dict[str, Dict[str, str]] = {
    "line_from_gradient_intercept": {
        "sign_of_c": "gave the y-intercept the wrong sign in the equation",
        "numbers_swapped": "swapped the gradient and the y-intercept in y = mx + c",
    },
    "line_from_gradient_point": {
        "sign_slip": "added the gradient times x to the y-coordinate instead of subtracting it when finding c",
        "point_as_intercept": "used the y-coordinate of the point as the y-intercept",
        "no_constant": "wrote the gradient and x only and left out the constant term",
    },
    "line_through_two_points": {
        "gradient_inverted": "used the change in x over the change in y as the gradient",
        "gradient_sign": "gave the gradient the wrong sign",
        "no_constant": "found the gradient but left out the constant term",
    },
    "parallel_line": {
        "perpendicular_gradient": "used the gradient of a perpendicular line instead of the same gradient",
        "same_constant": "used the same constant as the given line instead of finding a new one",
        "sign_slip": "added the gradient times x to the y-coordinate instead of subtracting it when finding c",
    },
    "perpendicular_line": {
        "reciprocal_only": "turned the gradient upside down but forgot to change its sign",
        "negative_only": "changed the sign of the gradient but forgot to turn it upside down",
        "same_gradient": "used the same gradient as the given line",
    },
    "line_intersection": {
        "coordinates_swapped": "found the right point but gave the coordinates the wrong way round",
        "sign_of_x": "made a sign error when solving, so the x-coordinate has the wrong sign",
        "wrong_line": "used the line through the first two points instead of the parallel line",
    },
    "lines_meet": {
        "coordinates_swapped": "found the right point but gave the coordinates the wrong way round",
        "sign_of_x": "made a sign error when solving, so the x-coordinate has the wrong sign",
        "x_only_substituted": "found x correctly but substituted into the wrong equation to find y",
    },
}

LINE_EQUATION_LEVEL_SKILLS: Dict[int, Tuple[str, ...]] = {
    1: ("line_from_gradient_intercept", "line_from_gradient_point"),
    2: ("line_through_two_points",),
    3: ("parallel_line",),
    4: ("perpendicular_line",),
    5: ("line_intersection", "lines_meet"),
}


def _line_equation_level1(rng: SeededRandom) -> _Built:
    for _ in range(_MAX_ATTEMPTS):
        m, c = Fraction(_nonzero(rng, 9)), Fraction(_nonzero(rng, 12))
        if rng.chance(1, 2):
            items = [_line_item("sign_of_c", m, -c)]
            if c != m:
                items.append(("numbers_swapped", math(_line_tex(c, m)), _line_typed(c, m), _line_key(c, m)))
            steps = [("Use y = mx + c with the gradient and the y-intercept", _line_typed(m, c))]
            question = (f"Find the equation of the line with gradient {math(number_latex(m))} that crosses the "
                        f"y-axis at the point {math(f'(0, {int(c)})')}.")
            return _line_built("line_from_gradient_intercept", question, m, c, items, steps,
                               {"m": int(m), "c": int(c)})
        x1 = _nonzero(rng, 6)
        y1 = m * x1 + c
        if abs(y1) > 30:
            continue
        items = [_line_item("sign_slip", m, y1 + m * x1), _line_item("point_as_intercept", m, y1)]
        steps = [("Substitute the point into y = mx + c", f"{int(y1)} = {int(m * x1)} + c"), ("Solve for c", str(int(c)))]
        question = (f"Find the equation of the line with gradient {math(number_latex(m))} that passes through "
                    f"the point {math(f'({x1}, {int(y1)})')}.")
        return _line_built("line_from_gradient_point", question, m, c, items, steps,
                           {"m": int(m), "point": [x1, int(y1)], "c": int(c)})
    raise GeneratorError("level 1 could not find a problem")


def _line_equation_level2(rng: SeededRandom) -> _Built:
    for _ in range(_MAX_ATTEMPTS):
        n1, n2 = rng.choice(_POINT_NAMES)
        den = rng.choice((1, 1, 2, 3, 4))
        m = Fraction(_nonzero(rng, 6), den)
        if gcd(abs(m.numerator), m.denominator) != 1:
            continue
        c = Fraction(_nonzero(rng, 9))
        a1, a2 = rng.randint(-4, 4), rng.randint(-4, 4)
        if a1 == a2:
            continue
        x1, x2 = den * a1, den * a2
        y1, y2 = m * x1 + c, m * x2 + c
        if abs(y1) > 20 or abs(y2) > 20 or y1.denominator != 1 or y2.denominator != 1:
            continue
        dy, dx = y2 - y1, x2 - x1
        items = [("gradient_inverted", math(_line_tex(Fraction(dx, dy), y1 - Fraction(dx, dy) * x1)),
                  _line_typed(Fraction(dx, dy), y1 - Fraction(dx, dy) * x1), _line_key(Fraction(dx, dy), y1 - Fraction(dx, dy) * x1)),
                 ("gradient_sign", math(_line_tex(-m, y1 + m * x1)), _line_typed(-m, y1 + m * x1), _line_key(-m, y1 + m * x1))]
        if c != 0:
            items.append(("no_constant", math(_line_tex(m, Fraction(0))), _line_typed(m, Fraction(0)), _line_key(m, Fraction(0))))
        steps = [("Find the gradient", _t(m)), ("Substitute one point to find c", f"{int(y1)} = {_t(m * x1)} + c"),
                 ("Write the equation", _line_typed(m, c))]
        question = (f"The points {math(_pt(n1, x1, int(y1)))} and {math(_pt(n2, x2, int(y2)))} lie on a straight line. "
                    f"Find the equation of the line in the form {math('y = mx + c')}.")
        return _line_built("line_through_two_points", question, m, c, items, steps,
                           {"p1": [x1, int(y1)], "p2": [x2, int(y2)], "m": [m.numerator, m.denominator], "c": int(c)})
    raise GeneratorError("level 2 could not find a problem")


def _given_line_tex(rng: SeededRandom, m: Fraction, k: Fraction) -> str:
    return _form_variants(m, k, rng.choice(("mc", "mc", "c_minus" if m < 0 else "mc")))


def _line_equation_level3(rng: SeededRandom) -> _Built:
    for _ in range(_MAX_ATTEMPTS):
        den = rng.choice((1, 1, 1, 2, 3))
        m = Fraction(_nonzero(rng, 7), den)
        if gcd(abs(m.numerator), m.denominator) != 1:
            continue
        k = Fraction(_nonzero(rng, 9))
        x1 = rng.randint(-6, 6) * den
        y1 = m * x1 + (k + rng.choice((-5, -3, -2, 2, 3, 5)))
        c = y1 - m * x1
        if x1 == 0 or abs(y1) > 25 or y1.denominator != 1 or c == k:
            continue
        perp = Fraction(-1) / m
        items = [_line_item("perpendicular_gradient", perp, y1 - perp * x1), _line_item("same_constant", m, k),
                 _line_item("sign_slip", m, y1 + m * x1)]
        steps = [("A parallel line has the same gradient", _t(m)), ("Substitute the point to find c", f"{int(y1)} = {_t(m * x1)} + c"),
                 ("Write the equation", _line_typed(m, c))]
        question = (f"Find the equation of the line parallel to {math(_given_line_tex(rng, m, k))} that passes through "
                    f"the point {math(f'({x1}, {int(y1)})')}. Give your answer in the form {math('y = mx + c')}.")
        return _line_built("parallel_line", question, m, c, items, steps,
                           {"m": [m.numerator, m.denominator], "k": int(k), "point": [x1, int(y1)], "c": [c.numerator, c.denominator]})
    raise GeneratorError("level 3 could not find a problem")


def _line_equation_level4(rng: SeededRandom) -> _Built:
    for _ in range(_MAX_ATTEMPTS):
        p, q = _nonzero(rng, 6), rng.randint(1, 3)
        if gcd(abs(p), q) != 1:
            continue
        m = Fraction(p, q)
        k = Fraction(_nonzero(rng, 9))
        perp = Fraction(-q, p)
        x1 = rng.randint(-5, 5) * abs(p)
        c = Fraction(_nonzero(rng, 9))
        y1 = perp * x1 + c
        if x1 == 0 or abs(y1) > 25 or y1.denominator != 1:
            continue
        items = [_line_item("reciprocal_only", Fraction(q, p), y1 - Fraction(q, p) * x1),
                 _line_item("negative_only", -m, y1 + m * x1),
                 _line_item("same_gradient", m, y1 - m * x1)]
        steps = [("The gradient of a perpendicular line is the negative reciprocal", _t(perp)),
                 ("Substitute the point to find c", f"{int(y1)} = {_t(perp * x1)} + c"),
                 ("Write the equation", _line_typed(perp, c))]
        question = (f"Find the equation of the line perpendicular to {math(_form_variants(m, k, 'mc'))} that passes "
                    f"through the point {math(f'({x1}, {int(y1)})')}. Give your answer in the form {math('y = mx + c')}.")
        return _line_built("perpendicular_line", question, perp, c, items, steps,
                           {"m": [m.numerator, m.denominator], "k": int(k), "point": [x1, int(y1)],
                            "perp": [perp.numerator, perp.denominator], "c": int(c)})
    raise GeneratorError("level 4 could not find a problem")


def _line_equation_level5(rng: SeededRandom) -> _Built:
    mode = rng.choice(("parallel_chain", "two_equations"))
    for _ in range(_MAX_ATTEMPTS):
        if mode == "two_equations":
            m1, m2 = _nonzero(rng, 5), _nonzero(rng, 5)
            if m1 == m2:
                continue
            xd, yd = rng.randint(-7, 7), rng.randint(-9, 9)
            c1, c2 = yd - m1 * xd, yd - m2 * xd
            if c1 == 0 or c2 == 0 or xd == 0 or yd == 0:
                continue
            items = [_pt_item("coordinates_swapped", yd, xd), _pt_item("sign_of_x", -xd, yd),
                     _pt_item("x_only_substituted", xd, m1 * xd)]
            steps = [("Make the two expressions for y equal", f"{m1}x + {c1} = {m2}x + {c2}".replace("+ -", "- ")),
                     ("Solve for x", str(xd)), ("Substitute to find y", str(yd))]
            question = (f"Find the coordinates of the point where the lines {math(_line_tex(Fraction(m1), Fraction(c1)))} "
                        f"and {math(_line_tex(Fraction(m2), Fraction(c2)))} meet.")
            return _point_built("lines_meet", question, xd, yd, items, steps,
                                {"lines": [[m1, c1], [m2, c2]], "point": [xd, yd]})
        den = rng.choice((1, 1, 2))
        pm = _nonzero(rng, 4)
        m1 = Fraction(pm, den)
        if gcd(abs(pm), den) != 1:
            continue
        m2 = _nonzero(rng, 4)
        if m1 == m2:
            continue
        xd, yd = rng.randint(-8, 8), rng.randint(-9, 9)
        c2 = yd - m2 * xd
        if c2 == 0:
            continue
        s, t = rng.choice((1, 2)), rng.choice((-2, -1, 1, 2))
        xa, ya = rng.randint(-6, 6), rng.randint(-6, 6)
        xb, yb = xa + den * s, ya + pm * s
        xc, yc = xd - den * t, yd - pm * t
        if max(abs(v) for v in (xb, yb, xc, yc)) > 14 or (xc, yc) == (xd, yd):
            continue
        cab = ya - m1 * xa
        wrong_x = (c2 - cab) / (m1 - m2)
        items = [_pt_item("coordinates_swapped", yd, xd), _pt_item("sign_of_x", -xd, yd),
                 _pt_item("wrong_line", wrong_x, m2 * wrong_x + c2)]
        c_cd = yc - m1 * xc
        steps = [("Find the gradient of AB", _t(m1)), ("Write the equation of CD, which has the same gradient", _line_typed(m1, c_cd)),
                 ("Solve with the other line to find x", str(xd)), ("Find y", str(yd))]
        question = (f"{math(_pt('A', xa, ya))}, {math(_pt('B', xb, yb))} and {math(_pt('C', xc, yc))} are three points. "
                    f"The line through {math('C')} that is parallel to {math('AB')} meets the line "
                    f"{math(_line_tex(Fraction(m2), Fraction(c2)))} at the point {math('D')}. "
                    f"Find the coordinates of {math('D')}.")
        return _point_built("line_intersection", question, xd, yd, items, steps,
                            {"A": [xa, ya], "B": [xb, yb], "C": [xc, yc], "line": [m2, c2], "D": [xd, yd]})
    raise GeneratorError("level 5 could not find a problem")


class EquationsStraightLinesGenerator(_FamilyGenerator):
    generator_id = LINE_EQUATION_ID
    version = 1
    levels = (1, 2, 3, 4, 5)
    level_skills = LINE_EQUATION_LEVEL_SKILLS
    error_notes = LINE_EQUATION_ERROR_NOTES
    builders = {1: _line_equation_level1, 2: _line_equation_level2, 3: _line_equation_level3,
                4: _line_equation_level4, 5: _line_equation_level5}



# ==========================================================================
# Lesson 15837: Parallel Lines, Perpendicular Lines, Quadrilaterals (coordinate form)
# ==========================================================================

PARALLEL_ERROR_NOTES: Dict[str, Dict[str, str]] = {
    "parallel_perpendicular_gradient": {
        "same_gradient": "gave the gradient of the given line instead of the gradient of a perpendicular line",
        "reciprocal_only": "turned the gradient upside down but forgot to change its sign",
        "negative_only": "changed the sign of the gradient but forgot to turn it upside down",
        "perpendicular_used": "gave the gradient of a perpendicular line where a parallel line was asked for",
        "parallel_used": "gave the gradient of the line itself where a perpendicular line was asked for",
    },
    "find_k_parallel": {
        "sign_error": "forgot the minus sign when rearranging the equation to find its gradient",
        "inverted": "set the gradients equal but divided the wrong way round when solving for k",
    },
    "find_k_perpendicular": {
        "sign_error": "forgot the minus sign when rearranging the equation to find its gradient",
        "parallel_used": "made the gradients equal instead of making their product -1",
        "inverted": "divided the wrong way round when solving for k",
    },
    "parallelogram_fourth_vertex": {
        "wrong_vertex": "added the wrong two vertices and subtracted the wrong one",
        "midpoint": "gave the midpoint of the diagonal instead of the missing vertex",
        "opposite_sign": "found the right distances but moved from the vertex in the wrong direction",
    },
    "rectangle_area": {
        "perimeter_style": "added the two side lengths instead of multiplying them",
        "no_root_factor": "multiplied the numbers in front of the square roots but forgot to multiply the square roots",
        "half_area": "found the area of the triangle instead of the rectangle",
    },
    "parallelogram_area": {
        "half_base": "used half of the base instead of the whole base",
        "lengths_added": "added the base and the height instead of multiplying",
        "no_root_factor": "multiplied the numbers in front of the square roots but forgot to multiply the square roots",
    },
}

PARALLEL_LEVEL_SKILLS: Dict[int, Tuple[str, ...]] = {
    1: ("parallel_perpendicular_gradient",),
    2: ("find_k_parallel", "find_k_perpendicular"),
    3: ("parallelogram_fourth_vertex",),
    4: ("rectangle_area",),
    5: ("parallelogram_area",),
}


def _parallel_level1(rng: SeededRandom) -> _Built:
    for _ in range(_MAX_ATTEMPTS):
        den = rng.choice((1, 1, 2, 3, 4))
        m = Fraction(_nonzero(rng, 8), den)
        if gcd(abs(m.numerator), m.denominator) != 1:
            continue
        c = Fraction(_nonzero(rng, 9))
        equation = _form_variants(m, c, "mc")
        perp = Fraction(-1) / m
        if rng.chance(1, 3):
            question = f"Write down the gradient of a line that is parallel to the line {math(equation)}."
            correct, skill = m, "parallel_perpendicular_gradient"
            items = [_num_item("perpendicular_used", perp), _num_item("reciprocal_only", 1 / m)]
            steps = [("Parallel lines have the same gradient", _t(m))]
            kind = "parallel"
        else:
            question = f"Write down the gradient of a line that is perpendicular to the line {math(equation)}."
            correct, skill = perp, "parallel_perpendicular_gradient"
            items = [_num_item("parallel_used", m), _num_item("reciprocal_only", 1 / m), _num_item("negative_only", -m)]
            steps = [("The gradient of the line is", _t(m)), ("Turn it upside down and change the sign", _t(perp))]
            kind = "perpendicular"
        return _number_built(skill, question, correct, items, steps,
                             {"m": [m.numerator, m.denominator], "c": int(c), "kind": kind})
    raise GeneratorError("level 1 could not find a problem")


def _parallel_level2(rng: SeededRandom) -> _Built:
    for _ in range(_MAX_ATTEMPTS):
        den = rng.choice((1, 2, 3, 4))
        num = _nonzero(rng, 7)
        if gcd(abs(num), den) != 1:
            continue
        m = Fraction(num, den)
        b = Fraction(_nonzero(rng, 9))
        t = _nonzero(rng, 3)
        e = _nonzero(rng, 12)
        if rng.chance(1, 2):
            # parallel: -a/k = m with a = num * t -> k = -den * t
            a = num * t
            k = -den * t
            question = (f"The lines {math(_line_tex(m, b))} and {math(f'{_coef_tex(a)}x + ky = {e}')} are parallel. "
                        f"Find the value of {math('k')}.")
            items = [_num_item("sign_error", den * t), _num_item("inverted", Fraction(a) * m)]
            steps = [("Make y the subject of the second equation to find its gradient", f"-{a}/k" if a > 0 else f"{-a}/k"),
                     ("Set the gradients equal and solve", str(k))]
            return _number_built("find_k_parallel", question, k, items, steps,
                                 {"m": [m.numerator, m.denominator], "a": a, "e": e})
        # perpendicular: -a/k = -den/num -> k = a*num/den with a = den*t
        a = den * t
        k = num * t
        question = (f"The lines {math(_line_tex(m, b))} and {math(f'{_coef_tex(a)}x + ky = {e}')} are perpendicular. "
                    f"Find the value of {math('k')}.")
        items = [_num_item("sign_error", -k), _num_item("parallel_used", -Fraction(a) / m),
                 _num_item("inverted", Fraction(den * a, num))]
        steps = [("Make y the subject of the second equation to find its gradient", f"-{a}/k" if a > 0 else f"{-a}/k"),
                 ("The product of the gradients is -1; solve for k", str(k))]
        return _number_built("find_k_perpendicular", question, k, items, steps,
                             {"m": [m.numerator, m.denominator], "a": a, "e": e})
    raise GeneratorError("level 2 could not find a problem")


def _coef_tex(a: int) -> str:
    return "" if a == 1 else ("-" if a == -1 else str(a))


def _parallel_level3(rng: SeededRandom) -> _Built:
    for _ in range(_MAX_ATTEMPTS):
        names = rng.choice((("P", "Q", "R", "S"), ("A", "B", "C", "D"), ("E", "F", "G", "H")))
        p = (rng.randint(-8, 8), rng.randint(-8, 8))
        q = (p[0] + _nonzero(rng, 9), p[1] + _nonzero(rng, 9))
        r = (q[0] + _nonzero(rng, 9), q[1] + _nonzero(rng, 9))
        s = (p[0] + r[0] - q[0], p[1] + r[1] - q[1])
        # the four points must form a real parallelogram (P, Q, R not in a line)
        if (q[0] - p[0]) * (r[1] - q[1]) == (q[1] - p[1]) * (r[0] - q[0]):
            continue
        if max(abs(v) for v in (*p, *q, *r, *s)) > 18:
            continue
        wrong1 = (q[0] + r[0] - p[0], q[1] + r[1] - p[1])
        wrong3 = (p[0] - r[0] + q[0], p[1] - r[1] + q[1])
        items = [_pt_item("wrong_vertex", *wrong1), _pt_item("midpoint", Fraction(p[0] + r[0], 2), Fraction(p[1] + r[1], 2)),
                 _pt_item("opposite_sign", *wrong3)]
        steps = [("The vector from Q to R is also the vector from P to S", f"({r[0] - q[0]}, {r[1] - q[1]})"),
                 ("Add it to P", _pt_typed(*s))]
        n1, n2, n3, n4 = names
        question = (f"{math(n1 + n2 + n3 + n4)} is a parallelogram with vertices {math(_pt(n1, *p))}, "
                    f"{math(_pt(n2, *q))} and {math(_pt(n3, *r))}. Find the coordinates of {math(n4)}.")
        return _point_built("parallelogram_fourth_vertex", question, s[0], s[1], items, steps,
                            {"vertices": [list(p), list(q), list(r)], "fourth": list(s)})
    raise GeneratorError("level 3 could not find a problem")


_PERP_DIRECTIONS = tuple((a, b) for a in range(1, 5) for b in range(1, 5)
                         if gcd(a, b) == 1 and _is_squarefree_part(a * a + b * b)[0] == 1 and a * a + b * b > 2 and a != b)


def _parallel_level4(rng: SeededRandom) -> _Built:
    for _ in range(_MAX_ATTEMPTS):
        names = rng.choice((("A", "B", "C", "D"), ("P", "Q", "R", "S"), ("E", "F", "G", "H")))
        a, b = rng.choice(_PERP_DIRECTIONS)
        n = a * a + b * b
        k1, k2 = rng.randint(1, 3), rng.randint(1, 3)
        if k1 == k2 and rng.chance(1, 2):
            continue
        sign = rng.choice((1, -1))
        p = (rng.randint(-7, 7), rng.randint(-7, 7))
        q = (p[0] + k1 * a, p[1] + k1 * b)
        u = (-b * sign, a * sign)
        r = (q[0] + k2 * u[0], q[1] + k2 * u[1])
        if max(abs(v) for v in (*p, *q, *r)) > 18:
            continue
        area = k1 * k2 * n
        items = [("perimeter_style", math(_surd_latex(k1 + k2, n)), _surd_typed(k1 + k2, n), ("sum", k1 + k2, n)),
                 _num_item("no_root_factor", Fraction(k1 * k2)), _num_item("half_area", Fraction(k1 * k2 * n, 2))]
        steps = [("Length of the first side", _surd_typed(k1, n)), ("Length of the second side", _surd_typed(k2, n)),
                 ("Multiply the two lengths", str(area))]
        n1, n2, n3, n4 = names
        question = (f"{math(n1 + n2 + n3 + n4)} is a rectangle. {math(_pt(n1, *p))}, {math(_pt(n2, *q))} and "
                    f"{math(_pt(n3, *r))} are three of its vertices. Calculate the area of the rectangle.")
        return _number_built("rectangle_area", question, area, items, steps,
                             {"vertices": [list(p), list(q), list(r)], "k": [k1, k2], "n": n})
    raise GeneratorError("level 4 could not find a problem")


def _parallel_level5(rng: SeededRandom) -> _Built:
    for _ in range(_MAX_ATTEMPTS):
        names = rng.choice((("P", "Q", "R", "S"), ("A", "B", "C", "D"), ("E", "F", "G", "H")))
        a, b = rng.choice(_PERP_DIRECTIONS)
        n = a * a + b * b
        k1, k2 = rng.randint(1, 3), rng.randint(1, 3)
        sign = rng.choice((1, -1))
        p = (rng.randint(-7, 7), rng.randint(-7, 7))
        q = (p[0] + 2 * k1 * a, p[1] + 2 * k1 * b)
        m = (p[0] + k1 * a, p[1] + k1 * b)
        s = (m[0] - sign * k2 * b, m[1] + sign * k2 * a)
        if max(abs(v) for v in (*p, *q, *m, *s)) > 18:
            continue
        base_k = 2 * k1
        area = base_k * k2 * n
        items = [_num_item("half_base", Fraction(k1 * k2 * n)),
                 ("lengths_added", math(_surd_latex(base_k + k2, n)), _surd_typed(base_k + k2, n), ("sum", base_k + k2, n)),
                 _num_item("no_root_factor", Fraction(base_k * k2))]
        steps = [("Length of the base", _surd_typed(base_k, n)), ("Perpendicular height", _surd_typed(k2, n)),
                 ("Area is base times perpendicular height", str(area))]
        n1, n2, n3, n4 = names
        question = (f"{math(n1 + n2 + n3 + n4)} is a parallelogram with {math(_pt(n1, *p))}, {math(_pt(n2, *q))} and "
                    f"{math(_pt(n4, *s))} as three of its vertices. {math('M')} is the midpoint of {math(n1 + n2)} and "
                    f"{math('M' + n4)} is perpendicular to {math(n1 + n2)}. Calculate the area of the parallelogram.")
        return _number_built("parallelogram_area", question, area, items, steps,
                             {"vertices": [list(p), list(q), list(s)], "mid": list(m), "k": [k1, k2], "n": n})
    raise GeneratorError("level 5 could not find a problem")


class ParallelPerpendicularQuadrilateralsGenerator(_FamilyGenerator):
    generator_id = PARALLEL_ID
    version = 1
    levels = (1, 2, 3, 4, 5)
    level_skills = PARALLEL_LEVEL_SKILLS
    error_notes = PARALLEL_ERROR_NOTES
    builders = {1: _parallel_level1, 2: _parallel_level2, 3: _parallel_level3,
                4: _parallel_level4, 5: _parallel_level5}


GENERATORS = [AlgebraicManipulationExpansionGenerator(), FactorisationBasicsGenerator(),
              SolvingQuadraticEquationsGenerator(), StraightLineGraphsGradientsGenerator(),
              DistanceMidpointGradientGenerator(), EquationsStraightLinesGenerator(),
              ParallelPerpendicularQuadrilateralsGenerator()]
