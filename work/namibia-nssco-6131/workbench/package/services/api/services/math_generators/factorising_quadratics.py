"""Generator for NSSCO Mathematics lesson 15820,
"Factorising Quadratics and Completing the Square".

Five levels (see docs/investigations/2026-10-nssco-algebra-evidence-lessons-15819-15820.md,
section 3, for the spec and the open questions for the reviewing teacher):

1. Factorise ``x^2 + bx + c``, all terms positive.
2. Factorise ``x^2 + bx + c`` with negative terms (including ``x^2 - k^2``).
3. Factorise ``ax^2 + bx + c`` with ``a`` from 2 to 5 (factors ``(mx + p)(nx + q)``).
4. Write ``x^2 + bx + c`` as ``(x + p)^2 + q`` (even ``b``).
5. Write ``ax^2 + bx + c`` as ``a(x + p)^2 + q`` with ``a`` in {-1, 2, 3, 4, 5};
   about a quarter of these also ask for the turning point.

Every problem is built backwards from its answer, so the answer is exact. The
generator re-checks its own algebra with exact integer / fraction arithmetic
before returning, and every listed distractor is confirmed to differ from the
correct answer.
"""

from __future__ import annotations

from fractions import Fraction
from math import gcd
from typing import Dict, List, Optional, Sequence, Tuple

from .factorisation_forms import factor_product
from .base import Distractor, GeneratedProblem, GeneratorError, MathGenerator, SeededRandom, Step
from .formatting import (
    factors_latex,
    math,
    point_latex,
    quadratic_latex,
    square_form_latex,
)

GENERATOR_ID = "nssco_factorising_quadratics"
LESSON_ID = 15820  # YYeni lesson this generator serves (documentation only)

# Level parameters. Changing these changes which problems exist, so bump
# ``version`` on the generator class when they change.
L1_MAX = 12
L2_MAX = 12
L3_A_MAX = 5  # leading coefficient m*n stays within 2..5, like the exam's 5x^2 - 7x + 2
L3_CONST_MAX = 9
L4_P_MAX = 8
L4_Q_MAX = 15
L5_LEADS = (-1, 2, 3, 4, 5)
L5_P_MAX = 3  # keeps b = 2ap and c = ap^2 + q small, like 2x^2 + 4x - 5
L5_Q_MAX = 12
TURNING_POINT_SHARE = (1, 4)  # numerator, denominator; (0, 1) switches it off

_MAX_ATTEMPTS = 500

ERROR_NOTES: Dict[str, Dict[str, str]] = {
    "factorise_monic": {
        "sign_error": "put the wrong sign in both brackets (wrote the opposite of each number)",
        "wrong_factor_pair": (
            "picked two numbers that multiply to the constant term but do not add up to "
            "the coefficient of x"
        ),
        "solved_instead_of_factorising": (
            "solved the expression for x instead of writing it as a product of brackets"
        ),
    },
    "factorise_general": {
        "cross_term_swapped": (
            "put the constant terms in the wrong brackets, so the middle term comes out wrong"
        ),
        "sign_error": "put the wrong sign in both brackets (wrote the opposite of each number)",
        "solved_instead_of_factorising": (
            "solved the expression for x instead of writing it as a product of brackets"
        ),
    },
    "complete_square_monic": {
        "sign_of_p": "used the wrong sign inside the bracket",
        "forgot_to_subtract_square": (
            "did not subtract the square of the number in the bracket, so the constant "
            "outside the bracket is just the original constant"
        ),
        "p_not_halved": (
            "used the whole coefficient of x inside the bracket instead of half of it"
        ),
    },
    "complete_square_general": {
        "a_dropped": (
            "divided through by the leading coefficient and never multiplied it back, "
            "so the factor a is missing"
        ),
        "q_not_scaled": (
            "subtracted p squared instead of a times p squared when finding the constant"
        ),
        "sign_of_p": "used the wrong sign inside the bracket",
        "turning_point_sign_error": (
            "wrote the x-coordinate of the turning point with the wrong sign"
        ),
    },
}

LEVEL_SKILLS: Dict[int, Tuple[str, ...]] = {
    1: ("factorise_monic",),
    2: ("factorise_monic",),
    3: ("factorise_general",),
    4: ("complete_square_monic",),
    5: ("complete_square_general",),
}

Quadratic = Tuple[int, int, int]


def _require(condition: bool, message: str) -> None:
    if not condition:
        raise GeneratorError(f"self-check failed: {message}")


def _expand_factors(factors: Sequence[Tuple[int, int]]) -> Quadratic:
    """Multiply two linear factors ``(m1 x + k1)(m2 x + k2)`` exactly."""
    (m1, k1), (m2, k2) = factors
    return (m1 * m2, m1 * k2 + m2 * k1, k1 * k2)


def _expand_square_form(a: int, p: int, q: Fraction) -> Tuple[Fraction, Fraction, Fraction]:
    """Expand ``a(x + p)^2 + q`` exactly."""
    return (Fraction(a), Fraction(2 * a * p), Fraction(a * p * p) + q)


def _nonzero(rng: SeededRandom, bound: int) -> int:
    return rng.randint(1, bound) * rng.choice((-1, 1))


# --------------------------------------------------------------------------
# Factorising
# --------------------------------------------------------------------------


def _roots_answer(roots: Sequence[Fraction]) -> str:
    from .formatting import number_latex

    unique = sorted(set(roots))
    return " or ".join(math(f"x = {number_latex(r)}") for r in unique)


def _monic_problem(rng: SeededRandom, p: int, q: int) -> Tuple[str, str, List[Distractor], dict]:
    target = (1, p + q, p * q)
    factors = sorted([(1, p), (1, q)], key=lambda f: f[1])
    _require(_expand_factors(factors) == target, "monic factors do not expand to the quadratic")

    question = f"Factorise {math(quadratic_latex(*target))}."
    answer = math(factor_product(factors))

    candidates: List[Tuple[str, Optional[List[Tuple[int, int]]], str]] = []
    candidates.append(("sign_error", [(1, -p), (1, -q)], ""))

    b, c = target[1], target[2]
    pairs = []
    for s in range(-abs(c), abs(c) + 1):
        if s != 0 and c % s == 0:
            t = c // s
            if s <= t and s + t != b:
                pairs.append((s, t))
    if pairs:
        s, t = rng.choice(pairs)
        candidates.append(("wrong_factor_pair", [(1, s), (1, t)], ""))

    distractors: List[Distractor] = []
    notes = ERROR_NOTES["factorise_monic"]
    for code, fs, _ in candidates:
        assert fs is not None
        if _expand_factors(fs) == target:
            continue  # happens for e.g. (x - 3)(x + 3) under a sign flip
        distractors.append(
            Distractor(math(factors_latex(sorted(fs, key=lambda f: f[1]))), code, notes[code])
        )
    distractors.append(
        Distractor(
            _roots_answer([Fraction(-p), Fraction(-q)]),
            "solved_instead_of_factorising",
            notes["solved_instead_of_factorising"],
        )
    )
    machine = {
        "task": "factorise",
        "quadratic": list(target),
        "factors": [list(f) for f in factors],
    }
    return question, answer, distractors, machine


def _level1(rng: SeededRandom):
    p, q = sorted((rng.randint(1, L1_MAX), rng.randint(1, L1_MAX)))
    skill = "factorise_monic"
    return (skill,) + _monic_problem(rng, p, q)


def _level2(rng: SeededRandom):
    for _ in range(_MAX_ATTEMPTS):
        p, q = _nonzero(rng, L2_MAX), _nonzero(rng, L2_MAX)
        if p < 0 or q < 0:
            p, q = sorted((p, q))
            return ("factorise_monic",) + _monic_problem(rng, p, q)
    raise GeneratorError("level 2 could not find a problem")


def _general_problem(rng: SeededRandom, m: int, p: int, n: int, q: int):
    target = _expand_factors([(m, p), (n, q)])
    a, b, c = target
    factors = sorted([(m, p), (n, q)])
    _require(_expand_factors(factors) == target, "general factors do not expand to the quadratic")
    _require(b != 0, "middle term is zero")
    _require(gcd(gcd(a, abs(b)), abs(c)) == 1, "quadratic has a numeric common factor")

    question = f"Factorise {math(quadratic_latex(a, b, c))}."
    answer = math(factor_product(factors))
    notes = ERROR_NOTES["factorise_general"]

    candidates = [
        ("cross_term_swapped", [(m, q), (n, p)]),
        ("sign_error", [(m, -p), (n, -q)]),
    ]
    distractors: List[Distractor] = []
    for code, fs in candidates:
        if _expand_factors(fs) == target:
            continue
        distractors.append(
            Distractor(math(factors_latex(sorted(fs))), code, notes[code])
        )
    distractors.append(
        Distractor(
            _roots_answer([Fraction(-p, m), Fraction(-q, n)]),
            "solved_instead_of_factorising",
            notes["solved_instead_of_factorising"],
        )
    )
    machine = {
        "task": "factorise",
        "quadratic": [a, b, c],
        "factors": [list(f) for f in factors],
    }
    return question, answer, distractors, machine


def _level3(rng: SeededRandom):
    for _ in range(_MAX_ATTEMPTS):
        m, n = rng.randint(1, L3_A_MAX), rng.randint(1, L3_A_MAX)
        if m * n == 1 or m * n > L3_A_MAX:
            continue
        p, q = _nonzero(rng, L3_CONST_MAX), _nonzero(rng, L3_CONST_MAX)
        b = m * q + n * p
        if b == 0 or gcd(m, abs(p)) != 1 or gcd(n, abs(q)) != 1:
            continue
        if gcd(gcd(m * n, abs(b)), abs(p * q)) != 1:
            continue
        return ("factorise_general",) + _general_problem(rng, m, p, n, q)
    raise GeneratorError("level 3 could not find a problem")


# --------------------------------------------------------------------------
# Completing the square
# --------------------------------------------------------------------------


def _render_square_answer(
    a: int, p: int, q: Fraction, turning: bool, point: Optional[Tuple[Fraction, Fraction]] = None
) -> str:
    form = square_form_latex(a, p, q)
    if not turning:
        return math(form)
    x_tp, y_tp = point if point is not None else (Fraction(-p), q)
    return f"{math('y = ' + form)}; turning point {math(point_latex(x_tp, y_tp))}"


def _square_problem(
    rng: SeededRandom, a: int, p: int, q: int, *, skill: str, turning: bool
):
    b = 2 * a * p
    c = a * p * p + q
    target = (a, b, c)
    notes = ERROR_NOTES[skill]
    expanded = _expand_square_form(a, p, Fraction(q))
    _require(tuple(int(v) for v in expanded) == target, "square form does not expand to quadratic")
    _require(q != 0, "q is zero")

    expr = quadratic_latex(*target)
    if turning:
        question = (
            f"Express {math('y = ' + expr)} in the form {math('a(x + p)^2 + q')}. "
            f"Hence write down the coordinates of the turning point of the graph of "
            f"{math('y = ' + expr)}."
        )
    else:
        form_text = "a(x + p)^2 + q" if a != 1 else "(x + p)^2 + q"
        question = f"Write {math(expr)} in the form {math(form_text)}."
    answer = _render_square_answer(a, p, Fraction(q), turning)

    # (code, a', p', q') candidates; each must expand to something different.
    candidates: List[Tuple[str, int, int, Fraction]] = [("sign_of_p", a, -p, Fraction(q))]
    if skill == "complete_square_monic":
        candidates.append(("forgot_to_subtract_square", a, p, Fraction(c)))
        candidates.append(("p_not_halved", a, b, Fraction(c - b * b)))
    else:
        candidates.append(("a_dropped", 1, p, Fraction(q, a)))
        candidates.append(("q_not_scaled", a, p, Fraction(c - p * p)))

    distractors: List[Distractor] = []
    for code, a2, p2, q2 in candidates:
        if p2 == 0:
            continue
        if _expand_square_form(a2, p2, q2) == tuple(Fraction(v) for v in target):
            continue
        point = (Fraction(-p2), q2)
        distractors.append(
            Distractor(_render_square_answer(a2, p2, q2, turning, point), code, notes[code])
        )
    if turning:
        distractors.append(
            Distractor(
                _render_square_answer(a, p, Fraction(q), True, (Fraction(p), Fraction(q))),
                "turning_point_sign_error",
                notes["turning_point_sign_error"],
            )
        )
    machine = {
        "task": "complete_square",
        "quadratic": list(target),
        "form": {"a": a, "p": p, "q": q},
        "turning_point": [-p, q] if turning else None,
    }
    return question, answer, distractors, machine


def _level4(rng: SeededRandom):
    p, q = _nonzero(rng, L4_P_MAX), _nonzero(rng, L4_Q_MAX)
    return ("complete_square_monic",) + _square_problem(
        rng, 1, p, q, skill="complete_square_monic", turning=False
    )


def _level5(rng: SeededRandom):
    a = rng.choice(L5_LEADS)
    p, q = _nonzero(rng, L5_P_MAX), _nonzero(rng, L5_Q_MAX)
    turning = TURNING_POINT_SHARE[0] > 0 and rng.chance(*TURNING_POINT_SHARE)
    return ("complete_square_general",) + _square_problem(
        rng, a, p, q, skill="complete_square_general", turning=turning
    )


_LEVEL_BUILDERS = {1: _level1, 2: _level2, 3: _level3, 4: _level4, 5: _level5}


class FactorisingQuadraticsGenerator(MathGenerator):
    generator_id = GENERATOR_ID
    version = 2
    levels = (1, 2, 3, 4, 5)
    level_skills = LEVEL_SKILLS
    error_notes = ERROR_NOTES

    def _build(self, rng: SeededRandom, seed: int, level: int) -> GeneratedProblem:
        skill, question, answer, distractors, machine = _LEVEL_BUILDERS[level](rng)
        # A distractor must never equal the correct answer as text.
        distractors = [d for d in distractors if d.answer != answer]
        seen = set()
        distractors = [d for d in distractors if not (d.answer in seen or seen.add(d.answer))]
        from services.math_marking.parse import clean

        a, b, c = machine["quadratic"]
        if machine["task"] == "factorise":
            (m, p), (n, q) = machine["factors"]
            marking = {"answer_type": "expression", "expected": [clean(answer)], "typed": clean(answer), "form": "factorised"}
        else:
            p, q = machine["form"]["p"], machine["form"]["q"]
            form = square_form_latex(a,p,q)
            marking = {"answer_type": "expression", "expected": [form], "typed": form, "form": "completed_square"}
            if machine["turning_point"] is not None:
                # Both the expression AND point are required: a scalar shortcut
                # must not award this two-part question for either part alone.
                marking = {"answer_type": "text_description", "expected": [answer], "typed": answer}
        from types import SimpleNamespace
        from services.math_marking.factorising_program import quadratic_program
        program=quadratic_program(SimpleNamespace(machine=machine,answer=answer))
        steps=tuple(Step(row['action']+'. '+row['reason'],row['result']) for row in program.steps)
        distractors = [Distractor(d.answer, d.error_code, d.description, clean(d.answer)) for d in distractors]
        return GeneratedProblem(
            generator_id=self.generator_id,
            generator_version=self.version,
            seed=seed,
            level=level,
            skill=skill,
            question=question,
            answer=answer,
            distractors=tuple(distractors),
            machine=machine,
            steps=steps,
            marking=marking,
        )
