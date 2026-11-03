"""Generators for NSSCO Mathematics lessons on trigonometry and bearings, vectors,
transformations in coordinate form, and matrices.

Lessons covered (one generator each; the three transformation lessons share one):

* 15847 Three-Figure Bearings and Right-Angled Triangles
* 15848 Angles of Elevation, Depression, and Extended Ratios
* 15849 The Sine/Cosine Rules and 3D Trigonometry (triangle-with-given-sides form)
* 15839 Vector Operations and Magnitude
* 15840 Position Vectors and Coplanar Vectors
* 15841-15843 Transformations in coordinate form
* 15844 Matrix Basics, Addition, and Subtraction
* 15845 Matrix Multiplication and Properties
* 15846 Determinants, Inverses, and Simultaneous Equations

The levels follow the question shapes in the 2020-2024 papers (not their wording or
numbers). Everything is described in words and numbers; questions that need a drawn
figure, a drawing by the learner or a described-in-words picture are not generated.

Every problem is built backwards from its answer or re-derived with exact ``Fraction``
arithmetic (or ``math`` for trigonometry) before it is returned. Trigonometric answers
are only kept when they are not within 0.02 of a rounding boundary, so a learner who
rounds an intermediate value slightly differently is not marked wrong by luck.
"""

from __future__ import annotations

import math
from dataclasses import dataclass
from decimal import ROUND_HALF_UP, Decimal
from fractions import Fraction
from typing import Any, Callable, Dict, List, Mapping, Optional, Sequence, Tuple

from .base import Distractor, GeneratedProblem, GeneratorError, MathGenerator, SeededRandom, Step
from .formatting import math as m_, number_latex

BEARINGS_ID = "nssco_bearings_right_angled_triangles"
ELEVATION_ID = "nssco_elevation_depression_extended_ratios"
SINECOS_ID = "nssco_sine_cosine_rules"
VECTOR_OPS_ID = "nssco_vector_operations_magnitude"
POSITION_ID = "nssco_position_vectors"
TRANSFORM_ID = "nssco_transformations_coordinates"
MATRIX_BASICS_ID = "nssco_matrix_basics"
MATRIX_MULT_ID = "nssco_matrix_multiplication"
DETERMINANT_ID = "nssco_determinants_inverses"

DEG = r"^{\circ}"
_MAX_ATTEMPTS = 400


class _Retry(Exception):
    """The drawn numbers are not suitable (near a rounding boundary, degenerate...)."""


def _require(condition: bool, message: str) -> None:
    if not condition:
        raise GeneratorError(f"self-check failed: {message}")


def _need(condition: bool) -> None:
    if not condition:
        raise _Retry()


# --------------------------------------------------------------------------
# Number formatting and rounding
# --------------------------------------------------------------------------


def _typed(value: Fraction) -> str:
    value = Fraction(value)
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def _dec_text(value: Fraction) -> str:
    """Whole numbers as integers, halves and quarters as decimals (1.5), else a fraction."""
    value = Fraction(value)
    if value.denominator == 1:
        return str(value.numerator)
    den = value.denominator
    while den % 2 == 0:
        den //= 2
    while den % 5 == 0:
        den //= 5
    if den == 1:
        text = format(Decimal(value.numerator) / Decimal(value.denominator), "f")
        return text
    return _typed(value)


def _latex(value: Fraction) -> str:
    return number_latex(Fraction(value))


def _places_for_sf(x: float, n: int) -> int:
    return n - 1 - int(math.floor(math.log10(abs(x))))


def _round_places(x: float, places: int, *, guard: bool = True) -> Decimal:
    scaled = x * (10 ** places)
    if guard:
        _need(abs((scaled - math.floor(scaled)) - 0.5) > 0.02)
    return Decimal(repr(x)).quantize(Decimal(1).scaleb(-places), rounding=ROUND_HALF_UP)


def _round(x: float, rounding: str, digits: int, *, guard: bool = True) -> Decimal:
    if rounding == "sig_figs":
        _need(x != 0)
        return _round_places(x, _places_for_sf(x, digits), guard=guard)
    out = _round_places(x, 1 if rounding == "angle_1dp" else digits, guard=guard)
    if guard:
        _need(out != 0)  # an answer that rounds to 0.000 (or -0.000) is a degenerate question
    return out


def _deg(x: float) -> float:
    return math.degrees(x)


def _s(value: Decimal) -> str:
    return format(value, "f")


def _bearing(value: int) -> str:
    return f"{value % 360:03d}"


# --------------------------------------------------------------------------
# Matrices and vectors as text
# --------------------------------------------------------------------------

Matrix = Tuple[Tuple[Fraction, ...], ...]


def _mat(rows: Sequence[Sequence[Any]]) -> Matrix:
    return tuple(tuple(Fraction(v) for v in row) for row in rows)


def _mat_latex(rows: Matrix) -> str:
    return r"\begin{pmatrix} " + r" \\ ".join(" & ".join(_latex(v) for v in row) for row in rows) + r" \end{pmatrix}"


def _mat_typed(rows: Matrix) -> str:
    return "(" + "; ".join(", ".join(_typed(v) for v in row) for row in rows) + ")"


def _col(*values: Any) -> Matrix:
    return _mat([[v] for v in values])


def _mat_mul(a: Matrix, b: Matrix) -> Matrix:
    return tuple(tuple(sum(a[i][k] * b[k][j] for k in range(len(b))) for j in range(len(b[0]))) for i in range(len(a)))


def _mat_add(a: Matrix, b: Matrix, sign: int = 1) -> Matrix:
    return tuple(tuple(x + sign * y for x, y in zip(ra, rb)) for ra, rb in zip(a, b))


def _mat_scale(k: Any, a: Matrix) -> Matrix:
    return tuple(tuple(Fraction(k) * v for v in row) for row in a)


def _det(a: Matrix) -> Fraction:
    return a[0][0] * a[1][1] - a[0][1] * a[1][0]


def _inverse(a: Matrix) -> Matrix:
    d = _det(a)
    _require(d != 0, "singular matrix")
    return ((a[1][1] / d, -a[0][1] / d), (-a[1][0] / d, a[0][0] / d))


def _rand_mat(rng: SeededRandom, low: int, high: int, rows: int = 2, cols: int = 2) -> Matrix:
    return _mat([[rng.randint(low, high) for _ in range(cols)] for _ in range(rows)])


def _vec_latex(v: Matrix) -> str:
    return _mat_latex(v)


def _letters(coefs: Mapping[str, Fraction], order: Sequence[str], *, latex: bool) -> str:
    out = ""
    for sym in order:
        c = Fraction(coefs.get(sym, 0))
        if c == 0:
            continue
        name = rf"\mathbf{{{sym}}}" if latex else sym
        mag = abs(c)
        if mag == 1:
            body = name
        elif mag.denominator == 1:
            body = f"{mag.numerator}{name}"
        else:
            body = (rf"\frac{{{mag.numerator}}}{{{mag.denominator}}}{name}" if latex
                    else f"({mag.numerator}/{mag.denominator}){name}")
        if not out:
            out = ("-" if c < 0 else "") + body
        else:
            out += f" {'-' if c < 0 else '+'} {body}"
    return out or "0"


# --------------------------------------------------------------------------
# Shared builder plumbing (same shape as the other family modules)
# --------------------------------------------------------------------------


@dataclass
class _Built:
    skill: str
    question: str
    answer: str
    items: List[Tuple[str, str, str, Any]]
    correct_key: Any
    machine: Dict[str, Any]
    steps: List[Tuple[str, str]]
    marking: Dict[str, Any]


class _FamilyGenerator(MathGenerator):
    builders: Mapping[int, Callable[[SeededRandom], _Built]] = {}

    def _build(self, rng: SeededRandom, seed: int, level: int) -> GeneratedProblem:
        for _ in range(_MAX_ATTEMPTS):
            try:
                built = self.builders[level](rng)
                distractors = self._distractors(built)
                # a problem that can be marked must have wrong answers to teach from
                _need(bool(distractors) or not built.marking)
            except _Retry:
                continue
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
        raise GeneratorError(f"{self.generator_id} level {level}: no suitable problem found")

    def _distractors(self, built: _Built) -> List[Distractor]:
        notes = self.error_notes[built.skill]
        out: List[Distractor] = []
        seen = {built.correct_key}
        for code, display, typed, key in built.items:
            if key in seen:
                continue
            seen.add(key)
            out.append(Distractor(display, code, notes[code], typed))
        return out


def _numeric(
    skill: str,
    question: str,
    value: float,
    *,
    rounding: str,
    digits: int,
    unit: str = "",
    degrees: bool = False,
    cands: Sequence[Tuple[str, Optional[float]]],
    machine: Dict[str, Any],
    steps: Sequence[Tuple[str, str]],
) -> _Built:
    """A rounded numerical answer, with wrong-method values rounded the same way."""
    correct = _round(value, rounding, digits)
    suffix = (DEG if degrees else "")
    tail = f" {unit}" if unit else ""
    items = []
    for code, wrong in cands:
        if wrong is None or isinstance(wrong, complex) or math.isnan(wrong) or math.isinf(wrong):
            continue
        w = _round(wrong, rounding, digits, guard=False)
        items.append((code, f"{m_(_s(w) + suffix)}{tail}", _s(w), _s(w)))
    return _Built(
        skill=skill,
        question=question,
        answer=f"{m_(_s(correct) + suffix)}{tail}",
        items=items,
        correct_key=_s(correct),
        machine={**machine, "value": _s(correct), "rounding": rounding, "digits": digits},
        steps=[*steps, ("Round the answer", _s(correct))],
        marking={"answer_type": "number_rounded", "expected": [_s(correct)], "rounding": rounding, "digits": digits, "typed": _s(correct)},
    )


def _exact(
    skill: str,
    question: str,
    value: Fraction,
    *,
    display: Optional[str] = None,
    typed: Optional[str] = None,
    unit: str = "",
    degrees: bool = False,
    cands: Sequence[Tuple[str, Fraction]],
    machine: Dict[str, Any],
    steps: Sequence[Tuple[str, str]],
    answer_type: str = "number_exact",
) -> _Built:
    value = Fraction(value)
    suffix = DEG if degrees else ""
    tail = f" {unit}" if unit else ""
    items = []
    for code, wrong in cands:
        wrong = Fraction(wrong)
        items.append((code, f"{m_(_latex(wrong) + suffix)}{tail}", _typed(wrong), wrong))
    t = typed if typed is not None else _typed(value)
    return _Built(
        skill=skill,
        question=question,
        answer=f"{m_((display or _latex(value)) + suffix)}{tail}",
        items=items,
        correct_key=value,
        machine={**machine, "value": _typed(value)},
        steps=list(steps),
        marking={"answer_type": answer_type, "expected": [t], "typed": t},
    )


# ==========================================================================
# Lesson 15847: Three-Figure Bearings and Right-Angled Triangles
# ==========================================================================

BEARINGS_ERROR_NOTES: Dict[str, Dict[str, str]] = {
    "right_angle_side": {
        "wrong_ratio": "used cosine where sine was needed (or the other way round)",
        "divided_instead": "divided by the ratio when the side had to be found by multiplying",
        "tangent_used": "used tangent although the hypotenuse was involved",
        "multiplied_instead": "multiplied by the ratio when the side had to be found by dividing",
        "hypotenuse_cos": "divided by cosine instead of sine when finding the hypotenuse",
    },
    "right_angle_angle": {
        "ratio_inverted": "wrote the ratio upside down before using the inverse function",
        "cos_used": "used inverse cosine where inverse sine was needed",
        "tan_used": "used inverse tangent where inverse sine was needed",
        "sin_used": "used inverse sine where inverse tangent was needed",
        "forgot_inverse": "worked out the ratio but did not use the inverse function to turn it into an angle",
    },
    "pythagoras_hypotenuse": {
        "subtracted_squares": "subtracted the squares of the shorter sides instead of adding",
        "no_root": "added the squares but did not take the square root",
        "added_legs": "added the two shorter sides instead of using Pythagoras",
    },
    "pythagoras_shorter": {
        "added_squares": "added the squares when finding a shorter side",
        "no_root": "subtracted the squares but did not take the square root",
        "subtracted_legs": "subtracted the two lengths instead of using Pythagoras",
    },
    "back_bearing": {
        "bearing_unchanged": "gave the same bearing for the journey back",
        "quarter_turn": "added 90 degrees instead of 180 degrees",
        "reflected": "took the bearing away from 360 degrees instead of adding 180 degrees",
        "not_reduced": "added 180 degrees but did not subtract 360 degrees from a result above 360",
    },
    "bearing_turn": {
        "turned_wrong_way": "took the turn away from the bearing instead of adding it",
        "back_bearing": "gave the bearing of the starting point instead of the new course",
        "not_reduced": "added the turn but did not subtract 360 degrees from a result above 360",
    },
    "journey_distance": {
        "added_legs": "added the two distances instead of using Pythagoras",
        "no_root": "added the squares of the two distances but did not take the square root",
    },
    "journey_bearing": {
        "bearing_forward": "gave the bearing of the finish from the start instead of the start from the finish",
        "ratio_inverted": "used the two distances the wrong way round in the tangent ratio",
        "angle_wrong_way": "measured the angle from the first leg in the wrong direction",
    },
}

BEARINGS_LEVEL_SKILLS: Dict[int, Tuple[str, ...]] = {
    1: ("right_angle_side",),
    2: ("right_angle_angle",),
    3: ("pythagoras_hypotenuse", "pythagoras_shorter"),
    4: ("back_bearing", "bearing_turn"),
    5: ("journey_distance", "journey_bearing"),
}

# Fictional navigation buoys: generated bearings never claim real-town geography.
_PLACES = ("Kudu Buoy", "Seal Buoy", "Dune Buoy", "Coral Buoy", "Gull Buoy", "Reef Buoy", "Dolphin Buoy", "Pelican Buoy", "Anchor Buoy", "Lagoon Buoy")


def _g(x: float) -> str:
    return f"{x:g}"


def _bearings_level1(rng: SeededRandom) -> _Built:
    variant = rng.choice(("ladder_height", "ladder_base", "ramp_rise", "ramp_length"))
    th = rng.randint(20, 70)
    r = math.radians(th)
    ang = f"{th}{DEG}"
    if variant == "ladder_height":
        L = rng.randint(30, 120) / 10
        q = (f"A ladder {_g(L)} m long leans against a vertical wall. The ladder makes an angle of {m_(ang)} with the horizontal ground. "
             "Calculate how far up the wall the ladder reaches. Give your answer correct to 3 significant figures.")
        val = L * math.sin(r)
        cands = [("wrong_ratio", L * math.cos(r)), ("divided_instead", L / math.sin(r)), ("tangent_used", L * math.tan(r))]
        steps = [("Use sine: opposite over hypotenuse", f"sin {th} = h / {_g(L)}"), ("Rearrange for h", f"h = {_g(L)} sin {th}")]
        unit = "m"
    elif variant == "ladder_base":
        L = rng.randint(30, 120) / 10
        q = (f"A ladder {_g(L)} m long leans against a vertical wall. The ladder makes an angle of {m_(ang)} with the horizontal ground. "
             "Calculate the distance of the foot of the ladder from the wall. Give your answer correct to 3 significant figures.")
        val = L * math.cos(r)
        cands = [("wrong_ratio", L * math.sin(r)), ("divided_instead", L / math.cos(r)), ("tangent_used", L * math.tan(r))]
        steps = [("Use cosine: adjacent over hypotenuse", f"cos {th} = d / {_g(L)}"), ("Rearrange for d", f"d = {_g(L)} cos {th}")]
        unit = "m"
    elif variant == "ramp_rise":
        d = rng.randint(20, 150) / 10
        q = (f"A ramp has a horizontal length of {_g(d)} m and rises at an angle of {m_(ang)} to the horizontal. "
             "Calculate the height of the top of the ramp above the ground. Give your answer correct to 3 significant figures.")
        val = d * math.tan(r)
        cands = [("wrong_ratio", d * math.sin(r)), ("divided_instead", d / math.tan(r)), ("tangent_used", d * math.cos(r))]
        steps = [("Use tangent: opposite over adjacent", f"tan {th} = h / {_g(d)}"), ("Rearrange for h", f"h = {_g(d)} tan {th}")]
        unit = "m"
    else:
        h = rng.randint(8, 40) / 10
        q = (f"A ramp rises {_g(h)} m above the ground and makes an angle of {m_(ang)} with the ground. "
             "Calculate the length of the sloping surface of the ramp. Give your answer correct to 3 significant figures.")
        val = h / math.sin(r)
        cands = [("multiplied_instead", h * math.sin(r)), ("hypotenuse_cos", h / math.cos(r)), ("wrong_ratio", h * math.cos(r))]
        steps = [("Use sine: opposite over hypotenuse", f"sin {th} = {_g(h)} / L"), ("Rearrange for L", f"L = {_g(h)} / sin {th}")]
        unit = "m"
    b = _numeric("right_angle_side", q, val, rounding="sig_figs", digits=3, unit=unit, cands=cands,
                 machine={"task": "right_angle_side", "variant": variant, "angle": th}, steps=steps)
    return b


def _bearings_level2(rng: SeededRandom) -> _Built:
    variant = rng.choice(("sin", "tan", "cos"))
    if variant == "sin":
        L = rng.randint(30, 90) / 10
        h = round(L * rng.randint(25, 80) / 100, 1)
        _need(0 < h < L)
        q = (f"A ramp is {_g(L)} m long and rises {_g(h)} m above the ground. Calculate the angle the ramp makes with the ground. "
             "Give your answer correct to 1 decimal place.")
        val = _deg(math.asin(h / L))
        cands = [("cos_used", _deg(math.acos(h / L))), ("tan_used", _deg(math.atan(h / L))), ("forgot_inverse", h / L)]
        steps = [("Use sine: opposite over hypotenuse", f"sin A = {_g(h)} / {_g(L)}"), ("Use the inverse function", f"A = sin^-1({_g(h)} / {_g(L)})")]
    elif variant == "tan":
        d = rng.randint(30, 150) / 10
        h = round(d * rng.randint(20, 150) / 100, 1)
        _need(h > 0)
        q = (f"A path rises {_g(h)} m over a horizontal distance of {_g(d)} m. Calculate the angle the path makes with the horizontal. "
             "Give your answer correct to 1 decimal place.")
        val = _deg(math.atan(h / d))
        cands = [("ratio_inverted", _deg(math.atan(d / h))), ("sin_used", _deg(math.asin(h / d)) if h < d else None), ("forgot_inverse", h / d)]
        steps = [("Use tangent: opposite over adjacent", f"tan A = {_g(h)} / {_g(d)}"), ("Use the inverse function", f"A = tan^-1({_g(h)} / {_g(d)})")]
    else:
        L = rng.randint(60, 200) / 10
        d = round(L * rng.randint(30, 90) / 100, 1)
        _need(0 < d < L)
        q = (f"A cable {_g(L)} m long is fixed to level ground at a point {_g(d)} m from the foot of a vertical mast. "
             "Calculate the angle the cable makes with the ground. Give your answer correct to 1 decimal place.")
        val = _deg(math.acos(d / L))
        cands = [("ratio_inverted", _deg(math.acos(L / d)) if L < d else None), ("sin_used", _deg(math.asin(d / L))), ("forgot_inverse", d / L)]
        steps = [("Use cosine: adjacent over hypotenuse", f"cos A = {_g(d)} / {_g(L)}"), ("Use the inverse function", f"A = cos^-1({_g(d)} / {_g(L)})")]
    return _numeric("right_angle_angle", q, val, rounding="angle_1dp", digits=1, degrees=True, cands=cands,
                    machine={"task": "right_angle_angle", "variant": variant}, steps=steps)


def _bearings_level3(rng: SeededRandom) -> _Built:
    variant = rng.choice(("diagonal", "ladder", "cone"))
    if variant == "diagonal":
        a, b = rng.randint(8, 60), rng.randint(8, 60)
        q = (f"A rectangular plot of land measures {a} m by {b} m. A path runs along a diagonal of the plot. "
             "Calculate the length of the path. Give your answer correct to 3 significant figures.")
        n = a * a + b * b
        val = math.sqrt(n)
        cands = [("subtracted_squares", math.sqrt(abs(a * a - b * b)) or None), ("no_root", float(n)), ("added_legs", float(a + b))]
        steps = [("Use Pythagoras", f"d^2 = {a}^2 + {b}^2"), ("Add the squares", str(n)), ("Take the square root", f"sqrt({n})")]
        skill = "pythagoras_hypotenuse"
    elif variant == "ladder":
        L = rng.randint(50, 120) / 10
        h = round(L * rng.randint(40, 95) / 100, 1)
        _need(0 < h < L)
        q = (f"A ladder {_g(L)} m long reaches {_g(h)} m up a vertical wall. Calculate the distance of the foot of the ladder from the wall. "
             "Give your answer correct to 3 significant figures.")
        n = L * L - h * h
        val = math.sqrt(n)
        cands = [("added_squares", math.sqrt(L * L + h * h)), ("no_root", n), ("subtracted_legs", L - h)]
        steps = [("Use Pythagoras", f"d^2 = {_g(L)}^2 - {_g(h)}^2"), ("Subtract the squares", f"{n:.2f}"), ("Take the square root", f"sqrt({n:.2f})")]
        skill = "pythagoras_shorter"
    else:
        r = rng.randint(2, 12)
        l = rng.randint(r + 2, r + 14)
        q = (f"A cone has a base radius of {r} cm and a slant height of {l} cm. Calculate the perpendicular height of the cone. "
             "Give your answer correct to 3 significant figures.")
        n = l * l - r * r
        val = math.sqrt(n)
        cands = [("added_squares", math.sqrt(l * l + r * r)), ("no_root", float(n)), ("subtracted_legs", float(l - r))]
        steps = [("Use Pythagoras", f"h^2 = {l}^2 - {r}^2"), ("Subtract the squares", str(n)), ("Take the square root", f"sqrt({n})")]
        skill = "pythagoras_shorter"
    return _numeric(skill, q, val, rounding="sig_figs", digits=3, unit="m" if variant != "cone" else "cm", cands=cands,
                    machine={"task": "pythagoras", "variant": variant}, steps=steps)


def _bearings_level4(rng: SeededRandom) -> _Built:
    a, b = rng.choice(_PLACES), rng.choice(_PLACES)
    _need(a != b)
    if rng.chance(2, 3):
        th = rng.randint(10, 350)
        _need(th % 90 != 0 and th != 180)
        q = (f"The bearing of {b} from {a} is {m_(_bearing(th) + DEG)}. Calculate the bearing of {a} from {b}.")
        ans = (th + 180) % 360
        cands = [("bearing_unchanged", th), ("quarter_turn", (th + 90) % 360), ("reflected", 360 - th)]
        if th >= 180:
            cands.append(("not_reduced", th + 180))
        steps = [("Back bearing: add or subtract 180", f"{th} {'+' if th < 180 else '-'} 180"), ("Write as a three-figure bearing", _bearing(ans))]
        skill = "back_bearing"
    else:
        th = rng.randint(10, 340)
        t = rng.randint(20, 160)
        q = (f"A ship leaves {a} on a bearing of {m_(_bearing(th) + DEG)}. After some time it turns clockwise through {m_(str(t) + DEG)} "
             f"and sails on the new course. Calculate the bearing of the new course.")
        ans = (th + t) % 360
        cands = [("turned_wrong_way", (th - t) % 360), ("back_bearing", (th + 180) % 360)]
        if th + t >= 360:
            cands.append(("not_reduced", th + t))
        steps = [("Add the turn to the bearing", f"{th} + {t}"), ("Write as a three-figure bearing", _bearing(ans))]
        skill = "bearing_turn"
    _need(ans % 90 != 0 or skill == "back_bearing")
    items = [(c, f"{m_(_bearing(v) + DEG)}" if v < 360 else m_(str(v) + DEG), str(v), v) for c, v in cands]
    return _Built(skill, q, m_(_bearing(ans) + DEG), items, ans, {"task": skill, "answer": ans}, steps,
                  {"answer_type": "number_exact", "expected": list(dict.fromkeys([str(ans), _bearing(ans)])), "typed": _bearing(ans)})


def _bearings_level5(rng: SeededRandom) -> _Built:
    a, b = rng.randint(5, 20), rng.randint(5, 20)
    th = rng.randint(10, 350)
    right = rng.chance(1, 2)
    th2 = (th + 90) % 360 if right else (th - 90) % 360
    p, r_ = rng.choice(_PLACES), rng.choice(_PLACES)
    _need(p != r_)
    intro = (f"A boat leaves {p} and sails {a} km on a bearing of {m_(_bearing(th) + DEG)}. It then sails {b} km on a bearing of "
             f"{m_(_bearing(th2) + DEG)} and arrives at {r_}.")
    if rng.chance(1, 2):
        q = intro + f" Calculate the distance from {p} to {r_}. Give your answer correct to 3 significant figures."
        n = a * a + b * b
        _need(math.isqrt(n) ** 2 != n)
        cands = [("added_legs", float(a + b)), ("no_root", float(n))]
        steps = [("The two legs are at right angles, so use Pythagoras", f"d^2 = {a}^2 + {b}^2"), ("Add the squares", str(n)), ("Take the square root", f"sqrt({n})")]
        return _numeric("journey_distance", q, math.sqrt(n), rounding="sig_figs", digits=3, unit="km", cands=cands,
                        machine={"task": "journey_distance", "legs": [a, b]}, steps=steps)
    q = intro + f" Calculate the bearing of {p} from {r_}. Give your answer correct to 1 decimal place."
    sgn = 1 if right else -1
    ang = _deg(math.atan(b / a))
    forward = (th + sgn * ang) % 360
    val = (forward + 180) % 360
    _need(min(val, 360 - val) > 1.0)  # a bearing next to north would round to 000.0 or 360.0
    cands = [
        ("bearing_forward", forward),
        ("ratio_inverted", (th + sgn * _deg(math.atan(a / b)) + 180) % 360),
        ("angle_wrong_way", (th - sgn * ang + 180) % 360),
    ]
    steps = [("Angle at the start between the first leg and the line to the finish", f"tan A = {b} / {a}"),
             ("Bearing of the finish from the start", f"{th} {'+' if right else '-'} A"),
             ("Add 180 for the bearing of the start from the finish", "+ 180")]
    return _numeric("journey_bearing", q, val, rounding="angle_1dp", digits=1, degrees=True, cands=cands,
                    machine={"task": "journey_bearing", "legs": [a, b], "bearing": th, "right": right}, steps=steps)


class BearingsRightAngledGenerator(_FamilyGenerator):
    generator_id = BEARINGS_ID
    version = 1
    levels = (1, 2, 3, 4, 5)
    level_skills = BEARINGS_LEVEL_SKILLS
    error_notes = BEARINGS_ERROR_NOTES
    builders = {1: _bearings_level1, 2: _bearings_level2, 3: _bearings_level3, 4: _bearings_level4, 5: _bearings_level5}



# ==========================================================================
# Lesson 15848: Angles of Elevation, Depression, and Extended Ratios
# ==========================================================================

ELEVATION_ERROR_NOTES: Dict[str, Dict[str, str]] = {
    "elevation_height": {
        "sin_used": "used sine instead of tangent for the opposite and adjacent sides",
        "divided_instead": "divided by tangent when the height had to be found by multiplying",
        "cos_used": "used cosine instead of tangent",
    },
    "elevation_distance": {
        "multiplied_instead": "multiplied by tangent when the distance had to be found by dividing",
        "sin_used": "divided by sine instead of tangent",
        "cos_used": "divided by cosine instead of tangent",
    },
    "depression_distance": {
        "multiplied_instead": "multiplied by tangent when the distance had to be found by dividing",
        "angle_from_cliff": "used the angle of depression as if it were measured from the vertical cliff",
        "sin_used": "divided by sine instead of tangent",
    },
    "depression_angle": {
        "ratio_inverted": "wrote the tangent ratio upside down before using the inverse function",
        "angle_from_vertical": "gave the angle between the line of sight and the cliff instead of the angle of depression",
        "forgot_inverse": "worked out the ratio but did not use the inverse function",
    },
    "calculator_difference": {
        "radian_mode": "worked with the calculator set to radians instead of degrees",
        "signs_swapped": "subtracted in the wrong order",
        "positive_sine": "treated the sine of the angle as positive although the angle is in the third quadrant",
    },
    "calculator_fraction": {
        "radian_mode": "worked with the calculator set to radians instead of degrees",
        "fraction_dropped": "left out the fraction in front of the trigonometric ratio",
        "minus_first": "subtracted before multiplying by the fraction",
    },
    "solve_trig_equation": {
        "one_solution_only": "gave only the angle shown by the calculator and missed the second solution in the range",
        "calculator_negative": "gave the negative angle shown by the calculator, which is outside the range",
        "wrong_second_angle": "found the second angle by subtracting from 180 when the pair needed 360",
    },
    "exact_ratio": {
        "sign_ignored": "found the size of the ratio correctly but ignored that the angle is in a quadrant where it is negative",
        "reciprocal": "wrote the ratio upside down",
        "cos_used": "gave the cosine instead of the tangent",
    },
    "exact_expression": {
        "sign_ignored": "ignored the minus sign of the ratio for the quadrant",
        "tangent_sign_only": "used the correct tangent but a positive sine",
        "added_ratios": "added the two ratios before multiplying by the coefficients",
    },
}

ELEVATION_LEVEL_SKILLS: Dict[int, Tuple[str, ...]] = {
    1: ("elevation_height", "elevation_distance"),
    2: ("depression_distance", "depression_angle"),
    3: ("calculator_difference", "calculator_fraction"),
    4: ("solve_trig_equation",),
    5: ("exact_ratio", "exact_expression"),
}

_STRUCTURES = ("radio mast", "church tower", "water tower", "lighthouse", "school flagpole", "windmill")
_SPOTS = ("Windhoek", "Swakopmund", "Rundu", "Oshakati", "Keetmanshoop")


def _elevation_level1(rng: SeededRandom) -> _Built:
    th = rng.randint(15, 70)
    r = math.radians(th)
    thing = rng.choice(_STRUCTURES)
    d = rng.randint(120, 900) / 10
    if rng.chance(2, 3):
        q = (f"A learner stands {_g(d)} m from the foot of the {thing} on level ground. The angle of elevation of the top of the {thing} "
             f"from the learner is {m_(str(th) + DEG)}. Calculate the height of the {thing}. Give your answer correct to 3 significant figures.")
        cands = [("sin_used", d * math.sin(r)), ("divided_instead", d / math.tan(r)), ("cos_used", d * math.cos(r))]
        steps = [("Use tangent: opposite over adjacent", f"tan {th} = h / {_g(d)}"), ("Rearrange for h", f"h = {_g(d)} tan {th}")]
        return _numeric("elevation_height", q, d * math.tan(r), rounding="sig_figs", digits=3, unit="m", cands=cands,
                        machine={"task": "elevation_height", "angle": th}, steps=steps)
    h = rng.randint(80, 600) / 10
    q = (f"The {thing} is {_g(h)} m high. A learner on level ground sees the top at an angle of elevation of {m_(str(th) + DEG)}. "
         f"Calculate the distance of the learner from the foot of the {thing}. Give your answer correct to 3 significant figures.")
    cands = [("multiplied_instead", h * math.tan(r)), ("sin_used", h / math.sin(r)), ("cos_used", h / math.cos(r))]
    steps = [("Use tangent: opposite over adjacent", f"tan {th} = {_g(h)} / d"), ("Rearrange for d", f"d = {_g(h)} / tan {th}")]
    return _numeric("elevation_distance", q, h / math.tan(r), rounding="sig_figs", digits=3, unit="m", cands=cands,
                    machine={"task": "elevation_distance", "angle": th}, steps=steps)


def _elevation_level2(rng: SeededRandom) -> _Built:
    if rng.chance(1, 2):
        th = rng.randint(15, 65)
        r = math.radians(th)
        h = rng.randint(200, 900) / 10
        q = (f"From the top of a cliff {_g(h)} m high, the angle of depression of a boat at sea is {m_(str(th) + DEG)}. "
             "Calculate the horizontal distance of the boat from the foot of the cliff. Give your answer correct to 3 significant figures.")
        cands = [("multiplied_instead", h * math.tan(r)), ("angle_from_cliff", h * math.tan(math.radians(90 - th))), ("sin_used", h / math.sin(r))]
        steps = [("The angle of depression equals the angle of elevation from the boat", f"tan {th} = {_g(h)} / d"), ("Rearrange for d", f"d = {_g(h)} / tan {th}")]
        return _numeric("depression_distance", q, h / math.tan(r), rounding="sig_figs", digits=3, unit="m", cands=cands,
                        machine={"task": "depression_distance", "angle": th}, steps=steps)
    h = rng.randint(200, 900) / 10
    d = round(h * rng.randint(60, 220) / 100, 0)
    _need(d > 0)
    d = float(d)
    q = (f"From the top of a cliff {_g(h)} m high, a boat is seen {_g(d)} m from the foot of the cliff, on level water. "
         "Calculate the angle of depression of the boat from the top of the cliff. Give your answer correct to 1 decimal place.")
    val = _deg(math.atan(h / d))
    cands = [("ratio_inverted", _deg(math.atan(d / h))), ("angle_from_vertical", 90 - val), ("forgot_inverse", h / d)]
    steps = [("Use tangent: opposite over adjacent", f"tan A = {_g(h)} / {_g(d)}"), ("Use the inverse function", f"A = tan^-1({_g(h)} / {_g(d)})")]
    return _numeric("depression_angle", q, val, rounding="angle_1dp", digits=1, degrees=True, cands=cands,
                    machine={"task": "depression_angle"}, steps=steps)


def _elevation_level3(rng: SeededRandom) -> _Built:
    if rng.chance(1, 2):
        A = rng.randint(100, 170)
        B = rng.randint(190, 260)
        val = math.cos(math.radians(A)) - math.sin(math.radians(B))
        q = (''.join(['Work out ', format(m_(''.join(['\\cos ', format(A, ''), format(DEG, ''), ' - \\sin ', format(B, ''), format(DEG, '')])), ''), '. Give your answer correct to 3 decimal places.']))
        cands = [("radian_mode", math.cos(A) - math.sin(B)), ("signs_swapped", math.sin(math.radians(B)) - math.cos(math.radians(A))),
                 ("positive_sine", math.cos(math.radians(A)) - abs(math.sin(math.radians(B))))]
        steps = [(f"cos {A}", f"{math.cos(math.radians(A)):.4f}"), (f"sin {B}", f"{math.sin(math.radians(B)):.4f}"), ("Subtract", f"{val:.4f}")]
        return _numeric("calculator_difference", q, val, rounding="decimal_places", digits=3, cands=cands,
                        machine={"task": "calculator_difference", "angles": [A, B]}, steps=steps)
    fn = rng.choice(("sin", "cos", "tan"))
    num, den = rng.choice(((1, 2), (1, 3), (2, 3), (3, 4), (2, 5), (3, 5), (5, 6)))
    th = rng.randint(15, 75)
    c = rng.randint(1, 3)
    f = getattr(math, fn)
    r = math.radians(th)
    val = num / den * f(r) - c
    q = (''.join(['Work out ', format(m_(''.join(['\\frac{', format(num, ''), '}{', format(den, ''), '}\\', format(fn, ''), ' ', format(th, ''), format(DEG, ''), ' - ', format(c, '')])), ''), '. Give your answer correct to 2 decimal places.']))
    cands = [("radian_mode", num / den * f(th) - c), ("fraction_dropped", f(r) - c), ("minus_first", num / den * (f(r) - c))]
    steps = [(f"{fn} {th}", f"{f(r):.4f}"), ("Multiply by the fraction", f"{num / den * f(r):.4f}"), (f"Subtract {c}", f"{val:.4f}")]
    return _numeric("calculator_fraction", q, val, rounding="decimal_places", digits=2, cands=cands,
                    machine={"task": "calculator_fraction", "fn": fn, "angle": th}, steps=steps)


def _elevation_level4(rng: SeededRandom) -> _Built:
    fn = rng.choice(("sin", "cos", "tan"))
    negative = rng.chance(3, 4)
    k = rng.randint(2, 6)
    if fn == "tan":
        target = rng.randint(5, 40) / 10
        m_val = round(target * k)
        _need(m_val >= 1)
        ratio = Fraction(m_val, k)
        a = _deg(math.atan(float(ratio)))
    else:
        m_val = rng.randint(1, k - 1)
        ratio = Fraction(m_val, k)
        a = _deg(math.asin(float(ratio))) if fn == "sin" else _deg(math.acos(float(ratio)))
    # solutions in [0, 360]
    if fn == "sin":
        sols = [180 + a, 360 - a] if negative else [a, 180 - a]
    elif fn == "cos":
        sols = [180 - a, 180 + a] if negative else [a, 360 - a]
    else:
        sols = [180 - a, 360 - a] if negative else [a, 180 + a]
    sols = sorted(sols)
    rounded = [_round_places(v, 1) for v in sols]
    sign = "-" if negative else ""
    q = (''.join(['Solve ', format(m_(''.join([format(k, ''), '\\', format(fn, ''), ' x = ', format(sign, ''), format(m_val, '')])), ''), ' for values of ', format(m_('x'), ''), ' from ', format(m_('0' + DEG), ''), ' to ', format(m_('360' + DEG), ''), ' inclusive. Give your answers correct to 1 decimal place.']))
    typed = f"x = {_s(rounded[0])} and x = {_s(rounded[1])}"
    cands_x = []
    first_calc = _round_places(math.degrees(getattr(math, 'a' + fn)(float(ratio) * (-1 if negative else 1))), 1, guard=False)
    cands_x.append(("one_solution_only", f"x = {_s(rounded[0])}", rf"x = {_s(rounded[0])}{DEG}"))
    if fn != "cos":
        cands_x.append(("calculator_negative", f"x = {_s(first_calc)}", rf"x = {_s(first_calc)}{DEG}"))
    wrong2 = _round_places(180 - sols[0] if sols[0] < 180 else 540 - sols[0], 1, guard=False)
    cands_x.append(("wrong_second_angle", f"x = {_s(rounded[0])} and x = {_s(wrong2)}", rf"x = {_s(rounded[0])}{DEG}, {_s(wrong2)}{DEG}"))
    items = [(c, m_(disp), t, t) for c, t, disp in cands_x]
    steps = [("Find the angle the calculator gives", f"{_s(first_calc)}"), ("Find the other solution in the range", _s(rounded[1])), ("Both solutions", typed)]
    return _Built("solve_trig_equation", q, m_(rf"x = {_s(rounded[0])}{DEG} \text{{ and }} x = {_s(rounded[1])}{DEG}"), items, typed,
                  {"task": "solve_trig_equation", "fn": fn, "k": k, "m": m_val, "negative": negative, "solutions": [_s(v) for v in rounded]}, steps,
                  {"answer_type": "equation_solution", "expected": [typed], "rounding": "none", "typed": typed})


_TRIPLES = ((3, 4, 5), (5, 12, 13), (8, 15, 17), (7, 24, 25), (20, 21, 29))


def _quadrant_signs(quadrant: int) -> Tuple[int, int]:
    """(sign of sine, sign of cosine) for quadrants 2, 3, 4."""
    return {2: (1, -1), 3: (-1, -1), 4: (-1, 1)}[quadrant]


def _elevation_level5(rng: SeededRandom) -> _Built:
    a, b, c = rng.choice(_TRIPLES)
    quadrant = rng.choice((2, 3, 4))
    ss, cs = _quadrant_signs(quadrant)
    ranges = {2: (90, 180), 3: (180, 270), 4: (270, 360)}[quadrant]
    given_fn = rng.choice(("sin", "cos"))
    opp, adj = (a, b) if rng.chance(1, 2) else (b, a)
    sin_v, cos_v = Fraction(ss * opp, c), Fraction(cs * adj, c)
    tan_v = sin_v / cos_v
    shown = sin_v if given_fn == "sin" else cos_v
    lo, hi = ranges
    intro = (''.join(['Given that ', format(m_(''.join(['\\', format(given_fn, ''), ' \\theta = ', format(_latex(shown), '')])), ''), ' and ', format(m_(''.join([format(lo, ''), format(DEG, ''), ' < \\theta < ', format(hi, ''), format(DEG, '')])), '')]))
    if rng.chance(1, 2):
        q = intro + ''.join([', find the value of ', format(m_('\\tan \\theta'), ''), ' as a common fraction.'])
        cands = [("sign_ignored", abs(tan_v)), ("reciprocal", 1 / tan_v), ("cos_used", cos_v if given_fn == "sin" else sin_v)]
        steps = [("Find the third side with Pythagoras", str(adj if given_fn == "sin" else opp)),
                 ("Decide the sign from the quadrant", f"{'-' if tan_v < 0 else '+'}"), ("tan = sin / cos", _typed(tan_v))]
        return _exact("exact_ratio", q, tan_v, cands=cands, machine={"task": "exact_ratio", "sin": _typed(sin_v), "cos": _typed(cos_v), "quadrant": quadrant}, steps=steps)
    p, r_ = rng.randint(2, 5), rng.randint(2, 5)
    val = p * tan_v + r_ * sin_v
    q = intro + ''.join([', find the value of ', format(m_(''.join([format(p, ''), '\\tan \\theta + ', format(r_, ''), '\\sin \\theta'])), ''), ' as a common fraction.'])
    cands = [("sign_ignored", p * abs(tan_v) + r_ * abs(sin_v)), ("tangent_sign_only", p * tan_v + r_ * abs(sin_v)), ("added_ratios", (p + r_) * (tan_v + sin_v))]
    steps = [("tan theta", _typed(tan_v)), ("sin theta", _typed(sin_v)), ("Substitute", _typed(val))]
    return _exact("exact_expression", q, val, cands=cands, machine={"task": "exact_expression", "p": p, "q": r_, "quadrant": quadrant}, steps=steps)


class ElevationExtendedRatiosGenerator(_FamilyGenerator):
    generator_id = ELEVATION_ID
    version = 1
    levels = (1, 2, 3, 4, 5)
    level_skills = ELEVATION_LEVEL_SKILLS
    error_notes = ELEVATION_ERROR_NOTES
    builders = {1: _elevation_level1, 2: _elevation_level2, 3: _elevation_level3, 4: _elevation_level4, 5: _elevation_level5}



# ==========================================================================
# Lesson 15849: The Sine/Cosine Rules and 3D Trigonometry
# ==========================================================================

SINECOS_ERROR_NOTES: Dict[str, Dict[str, str]] = {
    "area_two_sides": {
        "half_forgotten": "left out the half in the area formula",
        "cos_used": "used cosine of the angle instead of sine",
        "no_angle": "multiplied the two sides and halved without using the angle",
    },
    "area_exact": {
        "half_forgotten": "left out the half in the area formula",
    },
    "cosine_rule_side": {
        "no_root": "worked out the square of the side but did not take the square root",
        "plus_sign": "added the 2ab cos C term instead of subtracting it",
        "subtract_first": "subtracted 2ab from the squares before multiplying by cos C",
    },
    "sine_rule_angle": {
        "forgot_inverse": "worked out sin of the angle but did not use the inverse sine",
        "ratio_inverted": "turned the sine rule upside down",
        "cos_used": "used cosine in the sine rule",
    },
    "sine_rule_side": {
        "ratio_inverted": "turned the sine rule upside down",
        "cos_used": "used cosine of the angles in the sine rule",
    },
    "cosine_rule_angle": {
        "forgot_inverse": "worked out cos of the angle but did not use the inverse cosine",
        "side_not_squared": "did not square the third side before subtracting",
        "sign_reversed": "subtracted the squares in the wrong order, giving the supplementary angle",
    },
    "area_to_angle": {
        "half_forgotten": "left out the 2 when rearranging the area formula for sin C",
        "forgot_inverse": "found sin of the angle but did not use the inverse sine",
        "cos_used": "used inverse cosine where inverse sine was needed",
    },
    "pyramid_diagonal": {
        "added_sides": "added the two sides of the base instead of using Pythagoras",
        "no_root": "added the squares of the sides but did not take the square root",
    },
    "pyramid_height": {
        "added_squares": "added the squares when finding a shorter side of the right-angled triangle",
        "full_diagonal": "used the whole base diagonal instead of half of it",
        "no_root": "subtracted the squares but did not take the square root",
    },
}

SINECOS_LEVEL_SKILLS: Dict[int, Tuple[str, ...]] = {
    1: ("area_two_sides", "area_exact"),
    2: ("cosine_rule_side",),
    3: ("sine_rule_angle", "sine_rule_side"),
    4: ("cosine_rule_angle",),
    5: ("area_to_angle", "pyramid_diagonal", "pyramid_height"),
}

_TRI_NAMES = (("A", "B", "C"), ("P", "Q", "R"), ("X", "Y", "Z"), ("K", "L", "M"))
_SIN_COS = lambda t: (math.sin(math.radians(t)), math.cos(math.radians(t)))  # noqa: E731


def _angle_name(v: Tuple[str, str, str], i: int) -> str:
    """Name of the angle at vertex i, e.g. ``angle BAC`` for vertex index 0."""
    others = [v[j] for j in range(3) if j != i]
    return f"{others[0]}{v[i]}{others[1]}"


def _side_name(v: Tuple[str, str, str], i: int) -> str:
    """Name of the side opposite vertex i."""
    others = [v[j] for j in range(3) if j != i]
    return f"{others[0]}{others[1]}"


def _sinecos_level1(rng: SeededRandom) -> _Built:
    v = rng.choice(_TRI_NAMES)
    a, b = rng.randint(4, 40), rng.randint(4, 40)
    exact = rng.chance(1, 4)
    C = rng.choice((30, 150)) if exact else rng.randint(20, 150)
    if exact:
        _need((a * b) % 4 == 0)
    # the angle is at v[2], between the sides v[0]v[2] (length a) and v[1]v[2] (length b)
    q = (f"In triangle {''.join(v)}, {v[0]}{v[2]} = {a} cm, {v[1]}{v[2]} = {b} cm and angle {_angle_name(v, 2)} = {m_(str(C) + DEG)}. "
         "Calculate the area of the triangle." + ("" if exact else " Give your answer correct to 3 significant figures."))
    sC, cC = _SIN_COS(C)
    steps = [("Area = half ab sin C", f"0.5 x {a} x {b} x sin {C}")]
    unit = "cm$^2$"
    if exact:
        val = Fraction(a * b, 4)
        cands: List[Tuple[str, Fraction]] = [("half_forgotten", Fraction(a * b, 2))]
        return _exact("area_exact", q, val, unit=unit, cands=cands, machine={"task": "area_exact", "a": a, "b": b, "C": C},
                      steps=[*steps, ("sin 30 and sin 150 are one half", _typed(val))])
    val = 0.5 * a * b * sC
    cands_f = [("half_forgotten", a * b * sC), ("cos_used", 0.5 * a * b * cC), ("no_angle", 0.5 * a * b)]
    return _numeric("area_two_sides", q, val, rounding="sig_figs", digits=3, unit=unit, cands=cands_f,
                    machine={"task": "area", "a": a, "b": b, "C": C}, steps=steps)


def _sinecos_level2(rng: SeededRandom) -> _Built:
    v = rng.choice(_TRI_NAMES)
    a, b = rng.randint(5, 30), rng.randint(5, 30)
    C = rng.randint(25, 140)
    cC = math.cos(math.radians(C))
    c2 = a * a + b * b - 2 * a * b * cC
    q = (f"In triangle {''.join(v)}, {v[0]}{v[2]} = {a} cm, {v[1]}{v[2]} = {b} cm and angle {_angle_name(v, 2)} = {m_(str(C) + DEG)}. "
         f"Calculate the length of {v[0]}{v[1]}. Give your answer correct to 3 significant figures.")
    cands = [("no_root", c2), ("plus_sign", math.sqrt(a * a + b * b + 2 * a * b * cC)),
             ("subtract_first", math.sqrt(abs((a * a + b * b - 2 * a * b) * cC)) or None)]
    steps = [("Cosine rule", f"c^2 = {a}^2 + {b}^2 - 2 x {a} x {b} x cos {C}"), ("Evaluate c squared", f"{c2:.2f}"), ("Take the square root", f"{math.sqrt(c2):.2f}")]
    return _numeric("cosine_rule_side", q, math.sqrt(c2), rounding="sig_figs", digits=3, unit="cm", cands=cands,
                    machine={"task": "cosine_rule_side", "a": a, "b": b, "C": C}, steps=steps)


def _sinecos_level3(rng: SeededRandom) -> _Built:
    v = rng.choice(_TRI_NAMES)
    if rng.chance(1, 2):
        A = rng.randint(25, 75)
        a = rng.randint(8, 40)
        b = round(a * rng.randint(40, 92) / 100)
        _need(0 < b < a)
        sA, _ = _SIN_COS(A)
        sB = b * sA / a
        B = _deg(math.asin(sB))
        q = (f"In triangle {''.join(v)}, {_side_name(v, 0)} = {a} cm, {_side_name(v, 1)} = {b} cm and angle {_angle_name(v, 0)} = {m_(str(A) + DEG)}. "
             f"Given that angle {_angle_name(v, 1)} is acute, calculate angle {_angle_name(v, 1)}. Give your answer correct to 1 decimal place.")
        inv = a * sA / b
        cands = [("forgot_inverse", sB), ("ratio_inverted", _deg(math.asin(inv)) if inv <= 1 else None),
                 ("cos_used", _deg(math.acos(b * math.cos(math.radians(A)) / a)))]
        steps = [("Sine rule", f"sin B / {b} = sin {A} / {a}"), ("Rearrange", f"sin B = {b} sin {A} / {a}"), ("Inverse sine", f"{B:.2f}")]
        return _numeric("sine_rule_angle", q, B, rounding="angle_1dp", digits=1, degrees=True, cands=cands,
                        machine={"task": "sine_rule_angle", "a": a, "b": b, "A": A}, steps=steps)
    A, B = rng.randint(30, 80), rng.randint(30, 80)
    _need(A + B < 150 and A != B)
    a = rng.randint(6, 40)
    sA, cA = _SIN_COS(A)
    sB, cB = _SIN_COS(B)
    val = a * sB / sA
    q = (f"In triangle {''.join(v)}, angle {_angle_name(v, 0)} = {m_(str(A) + DEG)}, angle {_angle_name(v, 1)} = {m_(str(B) + DEG)} and "
         f"{_side_name(v, 0)} = {a} cm. Calculate the length of {_side_name(v, 1)}. Give your answer correct to 3 significant figures.")
    cands = [("ratio_inverted", a * sA / sB), ("cos_used", a * cB / cA)]
    steps = [("Sine rule", f"b / sin {B} = {a} / sin {A}"), ("Rearrange", f"b = {a} sin {B} / sin {A}")]
    return _numeric("sine_rule_side", q, val, rounding="sig_figs", digits=3, unit="cm", cands=cands,
                    machine={"task": "sine_rule_side", "a": a, "A": A, "B": B}, steps=steps)


def _sinecos_level4(rng: SeededRandom) -> _Built:
    v = rng.choice(_TRI_NAMES)
    a, b, c = rng.randint(5, 30), rng.randint(5, 30), rng.randint(5, 30)
    _need(a + b > c and a + c > b and b + c > a)
    cosv = (a * a + b * b - c * c) / (2 * a * b)
    _need(abs(cosv) < 0.95)
    C = _deg(math.acos(cosv))
    q = (f"In triangle {''.join(v)}, {_side_name(v, 0)} = {a} cm, {_side_name(v, 1)} = {b} cm and {_side_name(v, 2)} = {c} cm. "
         f"Calculate angle {_angle_name(v, 2)}. Give your answer correct to 1 decimal place.")
    cands = [("forgot_inverse", cosv), ("side_not_squared", _deg(math.acos((a * a + b * b - c) / (2 * a * b))) if abs((a * a + b * b - c) / (2 * a * b)) <= 1 else None),
             ("sign_reversed", 180 - C)]
    steps = [("Cosine rule", f"cos C = ({a}^2 + {b}^2 - {c}^2) / (2 x {a} x {b})"), ("Evaluate", f"{cosv:.4f}"), ("Inverse cosine", f"{C:.2f}")]
    return _numeric("cosine_rule_angle", q, C, rounding="angle_1dp", digits=1, degrees=True, cands=cands,
                    machine={"task": "cosine_rule_angle", "a": a, "b": b, "c": c}, steps=steps)


_SIN_TRIPLES = ((3, 5), (4, 5), (5, 13), (12, 13), (8, 17), (15, 17), (7, 25), (24, 25))


def _sinecos_level5(rng: SeededRandom) -> _Built:
    variant = rng.choice(("area_angle", "diagonal", "height"))
    if variant == "area_angle":
        v = rng.choice(_TRI_NAMES)
        p, qd = rng.choice(_SIN_TRIPLES)
        a, b = rng.randint(6, 30), rng.randint(6, 30)
        area = Fraction(a * b * p, 2 * qd)
        _need(area.denominator == 1 and area >= 5)
        C = _deg(math.asin(p / qd))
        q = (f"The area of triangle {''.join(v)} is {area} cm" + r"$^2$" + f". {v[0]}{v[2]} = {a} cm and {v[1]}{v[2]} = {b} cm. "
             f"Given that angle {_angle_name(v, 2)} is acute, calculate angle {_angle_name(v, 2)}. Give your answer correct to 1 decimal place.")
        ratio2 = float(2 * area) / (a * b)
        cands = [("half_forgotten", _deg(math.asin(float(area) / (a * b)))), ("forgot_inverse", ratio2), ("cos_used", _deg(math.acos(ratio2)))]
        steps = [("Area = half ab sin C", f"{area} = 0.5 x {a} x {b} x sin C"), ("Rearrange", f"sin C = {2 * area} / {a * b}"), ("Inverse sine", f"{C:.2f}")]
        return _numeric("area_to_angle", q, C, rounding="angle_1dp", digits=1, degrees=True, cands=cands,
                        machine={"task": "area_to_angle", "a": a, "b": b, "area": str(area)}, steps=steps)
    length, width = rng.randint(4, 24), rng.randint(4, 24)
    d = math.hypot(length, width)
    base = (f"A solid pyramid has a rectangular base measuring {length} cm by {width} cm. The apex is directly above the centre of the base "
            "and each sloping edge is {e} cm long.")
    if variant == "diagonal":
        q = (f"A solid pyramid has a rectangular base measuring {length} cm by {width} cm. Calculate the length of a diagonal of the base. "
             "Give your answer correct to 3 significant figures.")
        n = length * length + width * width
        _need(math.isqrt(n) ** 2 != n)
        cands = [("added_sides", float(length + width)), ("no_root", float(n))]
        steps = [("Pythagoras in the base", f"d^2 = {length}^2 + {width}^2"), ("Add the squares", str(n)), ("Take the square root", f"sqrt({n})")]
        return _numeric("pyramid_diagonal", q, d, rounding="sig_figs", digits=3, unit="cm", cands=cands,
                        machine={"task": "pyramid_diagonal", "l": length, "w": width}, steps=steps)
    e = rng.randint(int(d / 2) + 3, int(d / 2) + 20)
    h2 = e * e - (d / 2) ** 2
    _need(h2 > 4)
    q = base.format(e=e) + " Calculate the vertical height of the apex above the base. Give your answer correct to 3 significant figures."
    cands = [("added_squares", math.sqrt(e * e + (d / 2) ** 2)), ("full_diagonal", math.sqrt(e * e - d * d) if e * e > d * d else None), ("no_root", h2)]
    steps = [("Half the base diagonal", f"{d / 2:.2f}"), ("Pythagoras in the right-angled triangle", f"h^2 = {e}^2 - ({d / 2:.2f})^2"), ("Take the square root", f"{math.sqrt(h2):.2f}")]
    return _numeric("pyramid_height", q, math.sqrt(h2), rounding="sig_figs", digits=3, unit="cm", cands=cands,
                    machine={"task": "pyramid_height", "l": length, "w": width, "e": e}, steps=steps)


class SineCosineRulesGenerator(_FamilyGenerator):
    generator_id = SINECOS_ID
    version = 1
    levels = (1, 2, 3, 4, 5)
    level_skills = SINECOS_LEVEL_SKILLS
    error_notes = SINECOS_ERROR_NOTES
    builders = {1: _sinecos_level1, 2: _sinecos_level2, 3: _sinecos_level3, 4: _sinecos_level4, 5: _sinecos_level5}



# ==========================================================================
# Lesson 15839: Vector Operations and Magnitude
# ==========================================================================

VECTOR_OPS_ERROR_NOTES: Dict[str, Dict[str, str]] = {
    "vector_add": {
        "subtracted": "subtracted the vectors instead of adding them",
        "components_mixed": "added the top of one vector to the bottom of the other",
        "top_only": "added the top numbers correctly but copied the bottom number of the first vector",
    },
    "vector_subtract": {
        "added": "added the vectors instead of subtracting them",
        "order_reversed": "subtracted in the wrong order",
        "sign_slip": "made a sign error when subtracting a negative component",
    },
    "vector_scalar": {
        "one_component": "multiplied only one component by the scalar",
        "added_scalar": "added the scalar to each component instead of multiplying",
        "sign_dropped": "ignored the minus sign of the scalar for one component",
    },
    "magnitude": {
        "no_root": "added the squares of the components but did not take the square root",
        "added_components": "added the components instead of using Pythagoras",
        "subtracted_squares": "subtracted the squares of the components instead of adding them",
    },
    "combination": {
        "one_term": "multiplied only the first vector by its scalar",
        "sign_slip": "added the second scaled vector instead of subtracting it",
        "order_reversed": "subtracted the scaled vectors in the wrong order",
    },
    "combination_magnitude": {
        "no_root": "added the squares of the components but did not take the square root",
        "magnitudes_combined": "combined the magnitudes of the two vectors instead of the vectors themselves",
        "added_components": "added the components of the result instead of using Pythagoras",
    },
    "parallelogram_vector": {
        "wrong_direction": "gave the vector in the opposite direction",
        "added_instead": "added the two side vectors when the vector needed a difference",
        "one_side_only": "gave only one of the two side vectors",
    },
}

VECTOR_OPS_LEVEL_SKILLS: Dict[int, Tuple[str, ...]] = {
    1: ("vector_add", "vector_subtract", "vector_scalar"),
    2: ("magnitude",),
    3: ("combination", "combination_magnitude"),
    4: ("parallelogram_vector",),
}


def _vec(rng: SeededRandom, bound: int = 9) -> Tuple[int, int]:
    return rng.randint(-bound, bound), rng.randint(-bound, bound)


def _v_item(code: str, v: Tuple[Fraction, Fraction]) -> Tuple[str, str, str, Any]:
    vec = _col(*v)
    return (code, m_(_vec_latex(vec)), _mat_typed_col(v), (v[0], v[1]))


def _mat_typed_col(v: Sequence[Any]) -> str:
    return "(" + ", ".join(_typed(Fraction(x)) for x in v) + ")"


def _vec_answer(skill: str, question: str, ans: Tuple[Any, Any], cands: Sequence[Tuple[str, Tuple[Any, Any]]], machine: Dict[str, Any],
                steps: Sequence[Tuple[str, str]]) -> _Built:
    ans = (Fraction(ans[0]), Fraction(ans[1]))
    typed = _mat_typed_col(ans)
    return _Built(skill, question, m_(_vec_latex(_col(*ans))), [_v_item(c, (Fraction(w[0]), Fraction(w[1]))) for c, w in cands], (ans[0], ans[1]),
                  machine, list(steps), {"answer_type": "vector", "expected": [typed], "typed": typed})


def _col_q(v: Tuple[int, int]) -> str:
    return _vec_latex(_col(*v))


def _vector_ops_level1(rng: SeededRandom) -> _Built:
    variant = rng.choice(("add", "subtract", "scalar"))
    a, b = _vec(rng), _vec(rng)
    na, nb = rng.choice(("a", "p", "u", "m")), rng.choice(("b", "q", "v", "n"))
    if variant == "add":
        q = ''.join([format(m_(''.join(['\\mathbf{', format(na, ''), '} = ', format(_col_q(a), '')])), ''), ' and ', format(m_(''.join(['\\mathbf{', format(nb, ''), '} = ', format(_col_q(b), '')])), ''), '. Find ', format(m_(''.join(['\\mathbf{', format(na, ''), '} + \\mathbf{', format(nb, ''), '}'])), ''), '.'])
        ans = (a[0] + b[0], a[1] + b[1])
        cands = [("subtracted", (a[0] - b[0], a[1] - b[1])), ("components_mixed", (a[0] + b[1], a[1] + b[0])), ("top_only", (a[0] + b[0], a[1]))]
        steps = [("Add the top numbers", str(ans[0])), ("Add the bottom numbers", str(ans[1]))]
        skill = "vector_add"
    elif variant == "subtract":
        q = ''.join([format(m_(''.join(['\\mathbf{', format(na, ''), '} = ', format(_col_q(a), '')])), ''), ' and ', format(m_(''.join(['\\mathbf{', format(nb, ''), '} = ', format(_col_q(b), '')])), ''), '. Find ', format(m_(''.join(['\\mathbf{', format(na, ''), '} - \\mathbf{', format(nb, ''), '}'])), ''), '.'])
        ans = (a[0] - b[0], a[1] - b[1])
        cands = [("added", (a[0] + b[0], a[1] + b[1])), ("order_reversed", (b[0] - a[0], b[1] - a[1])), ("sign_slip", (a[0] - b[0], a[1] + b[1]))]
        steps = [("Subtract the top numbers", str(ans[0])), ("Subtract the bottom numbers", str(ans[1]))]
        skill = "vector_subtract"
    else:
        k = rng.choice((-4, -3, -2, 2, 3, 4, 5))
        q = ''.join([format(m_(''.join(['\\mathbf{', format(na, ''), '} = ', format(_col_q(a), '')])), ''), '. Find ', format(m_(''.join([format(k, ''), '\\mathbf{', format(na, ''), '}'])), ''), '.'])
        ans = (k * a[0], k * a[1])
        cands = [("one_component", (k * a[0], a[1])), ("added_scalar", (a[0] + k, a[1] + k)), ("sign_dropped", (k * a[0], abs(k * a[1])))]
        steps = [("Multiply the top number by the scalar", str(ans[0])), ("Multiply the bottom number by the scalar", str(ans[1]))]
        skill = "vector_scalar"
    return _vec_answer(skill, q, ans, cands, {"task": skill, "a": list(a), "b": list(b)}, steps)


def _vector_ops_level2(rng: SeededRandom) -> _Built:
    a = _vec(rng, 10)
    _need(a != (0, 0))
    n2 = a[0] * a[0] + a[1] * a[1]
    root = math.isqrt(n2)
    if rng.chance(1, 3):
        a = rng.choice(((3, 4), (-3, 4), (5, -12), (-8, 6), (12, 5), (-6, -8), (8, -15), (-9, 12), (10, 24)))
        n2 = a[0] * a[0] + a[1] * a[1]
        root = math.isqrt(n2)
    name = rng.choice(("a", "p", "v", "w"))
    q = ''.join([format(m_(''.join(['\\mathbf{', format(name, ''), '} = ', format(_col_q(a), '')])), ''), '. Calculate the magnitude of ', format(m_(''.join(['\\mathbf{', format(name, ''), '}'])), ''), '.'])
    steps = [("Square each component and add", f"{a[0]}^2 + {a[1]}^2 = {n2}"), ("Take the square root", str(root) if root * root == n2 else f"sqrt({n2})")]
    if root * root == n2:
        ans, disp, typed = Fraction(root), str(root), str(root)
    else:
        ans, disp, typed = None, rf"\sqrt{{{n2}}}", f"sqrt({n2})"
    wrong = [("no_root", Fraction(n2)), ("added_components", Fraction(abs(a[0]) + abs(a[1])))]
    if abs(a[0]) != abs(a[1]):
        wrong.append(("subtracted_squares", Fraction(abs(a[0] * a[0] - a[1] * a[1]))))
    if ans is not None:
        return _exact("magnitude", q, ans, cands=wrong, machine={"task": "magnitude", "a": list(a)}, steps=steps)
    items = [(c, m_(_latex(w)), _typed(w), w) for c, w in wrong]
    return _Built("magnitude", q, m_(disp), items, typed, {"task": "magnitude", "a": list(a), "value": typed}, steps,
                  {"answer_type": "number_exact", "expected": [typed], "typed": typed})


def _vector_ops_level3(rng: SeededRandom) -> _Built:
    a, b = _vec(rng, 6), _vec(rng, 6)
    k, l = rng.choice((2, 3, 4, 5)), rng.choice((2, 3, 4))
    res = (k * a[0] - l * b[0], k * a[1] - l * b[1])
    na, nb = "a", "b"
    head = ''.join([format(m_(''.join(['\\mathbf{a} = ', format(_col_q(a), '')])), ''), ' and ', format(m_(''.join(['\\mathbf{b} = ', format(_col_q(b), '')])), ''), '.'])
    expr = f"{k}\\mathbf{{a}} - {l}\\mathbf{{b}}"
    if rng.chance(1, 2):
        q = head + f" Find {m_(expr)}."
        cands = [("one_term", (k * a[0] - b[0], k * a[1] - b[1])), ("sign_slip", (k * a[0] + l * b[0], k * a[1] + l * b[1])),
                 ("order_reversed", (l * b[0] - k * a[0], l * b[1] - k * a[1]))]
        steps = [(f"Work out {k}a", f"({k * a[0]}, {k * a[1]})"), (f"Work out {l}b", f"({l * b[0]}, {l * b[1]})"), ("Subtract", f"({res[0]}, {res[1]})")]
        return _vec_answer("combination", q, res, cands, {"task": "combination", "a": list(a), "b": list(b), "k": k, "l": l}, steps)
    _need(res != (0, 0))
    n2 = res[0] ** 2 + res[1] ** 2
    q = head + f" Calculate {m_(rf'|{expr}|')}, the magnitude of {m_(expr)}."
    root = math.isqrt(n2)
    steps = [(f"Work out {expr}", f"({res[0]}, {res[1]})"), ("Square each component and add", str(n2)), ("Take the square root", str(root) if root * root == n2 else f"sqrt({n2})")]
    mag_a = a[0] ** 2 + a[1] ** 2
    mag_b = b[0] ** 2 + b[1] ** 2
    wrong = [("no_root", Fraction(n2)), ("added_components", Fraction(abs(res[0]) + abs(res[1])))]
    if root * root == n2:
        return _exact("combination_magnitude", q, Fraction(root), cands=wrong, machine={"task": "combination_magnitude", "a": list(a), "b": list(b), "k": k, "l": l}, steps=steps)
    typed = f"sqrt({n2})"
    items = [(c, m_(_latex(w)), _typed(w), w) for c, w in wrong]
    return _Built("combination_magnitude", q, m_(rf"\sqrt{{{n2}}}"), items, typed,
                  {"task": "combination_magnitude", "a": list(a), "b": list(b), "k": k, "l": l, "value": typed}, steps,
                  {"answer_type": "number_exact", "expected": [typed], "typed": typed})


def _vector_ops_level4(rng: SeededRandom) -> _Built:
    verts = rng.choice((("O", "A", "B", "C"), ("A", "B", "C", "D"), ("P", "Q", "R", "S")))
    u, v = rng.choice((("a", "c"), ("p", "q"), ("u", "v")))
    # positions relative to the first vertex: V0 = 0, V1 = u, V2 = u + v, V3 = v
    pos = {verts[0]: {}, verts[1]: {u: Fraction(1)}, verts[2]: {u: Fraction(1), v: Fraction(1)}, verts[3]: {v: Fraction(1)}}
    start, end = rng.choice([(s, e) for s in verts for e in verts if s != e and (s, e) not in ((verts[0], verts[1]), (verts[0], verts[3]))])
    res = {k: pos[end].get(k, Fraction(0)) - pos[start].get(k, Fraction(0)) for k in (u, v)}
    _need(any(res.values()))
    order = (u, v)
    wrong_dir = {k: -c for k, c in res.items()}
    one_side = {k: c for k, c in res.items() if k == next((k2 for k2 in order if res[k2] != 0), None)}
    added = {k: abs(c) for k, c in res.items()}
    q = (''.join([format(''.join(verts), ''), ' is a parallelogram. ', format(verts[0], ''), format(verts[1], ''), ' = ', format(m_(''.join(['\\mathbf{', format(u, ''), '}'])), ''), ' and ', format(verts[0], ''), format(verts[3], ''), ' = ', format(m_(''.join(['\\mathbf{', format(v, ''), '}'])), ''), '. Write down, in terms of ', format(m_(''.join(['\\mathbf{', format(u, ''), '}'])), ''), ' and ', format(m_(''.join(['\\mathbf{', format(v, ''), '}'])), ''), ', the vector ', format(start, ''), format(end, ''), '.']))
    typed = _letters(res, order, latex=False)
    ans = _letters(res, order, latex=True)
    cands = [("wrong_direction", wrong_dir), ("added_instead", added), ("one_side_only", one_side)]
    norm = lambda w: tuple(sorted((k, c) for k, c in w.items() if c != 0))  # noqa: E731
    items = [(c, m_(_letters(w, order, latex=True)), _letters(w, order, latex=False), norm(w)) for c, w in cands if any(w.values())]
    steps = [("Route from the start to the end along the sides", f"{start}{end}"), ("Simplify", typed)]
    return _Built("parallelogram_vector", q, m_(ans), items, norm(res),
                  {"task": "parallelogram_vector", "start": start, "end": end, "coefs": {k: _typed(c) for k, c in res.items()}}, steps,
                  {"answer_type": "vector", "expected": [typed], "typed": typed})


class VectorOperationsGenerator(_FamilyGenerator):
    generator_id = VECTOR_OPS_ID
    version = 1
    levels = (1, 2, 3, 4)
    level_skills = VECTOR_OPS_LEVEL_SKILLS
    error_notes = VECTOR_OPS_ERROR_NOTES
    builders = {1: _vector_ops_level1, 2: _vector_ops_level2, 3: _vector_ops_level3, 4: _vector_ops_level4}



# ==========================================================================
# Lesson 15840: Position Vectors and Coplanar Vectors
# ==========================================================================

POSITION_ERROR_NOTES: Dict[str, Dict[str, str]] = {
    "ratio_point_column": {
        "ratio_swapped": "used the ratio the wrong way round, measuring the larger share from A",
        "displacement_only": "gave the vector from A to P instead of the position vector of P",
        "measured_from_b": "measured the part of the way from B instead of from A",
    },
    "midpoint_column": {
        "sum_not_halved": "added the two position vectors but did not halve",
        "difference_halved": "halved the vector AB but did not add it to the position vector of A",
        "half_of_b": "halved only the position vector of B",
    },
    "position_letters": {
        "ratio_swapped": "used the ratio the wrong way round",
        "displacement_only": "gave the vector from A to M instead of the position vector of M",
        "not_divided": "did not divide by the total number of parts in the ratio",
    },
    "vector_in_triangle": {
        "ratio_swapped": "used the ratio the wrong way round",
        "wrong_direction": "gave the vector in the opposite direction",
        "position_only": "gave the position vector of the point instead of the vector asked for",
        "sign_reversed": "subtracted in the wrong order",
        "forgot_half": "used the whole of the vector instead of half of it",
    },
}

POSITION_LEVEL_SKILLS: Dict[int, Tuple[str, ...]] = {
    1: ("ratio_point_column",),
    2: ("midpoint_column",),
    3: ("position_letters",),
    4: ("vector_in_triangle",),
}


def _position_level1(rng: SeededRandom) -> _Built:
    mm, nn = rng.choice(((1, 2), (2, 1), (1, 3), (3, 1), (2, 3), (3, 2), (1, 4), (3, 4)))
    k = _vec(rng, 3)
    _need(k != (0, 0))
    a = _vec(rng, 8)
    d = ((mm + nn) * k[0], (mm + nn) * k[1])
    b = (a[0] + d[0], a[1] + d[1])
    p = (a[0] + mm * k[0], a[1] + mm * k[1])
    q = (''.join(['The position vectors of ', format(m_('A'), ''), ' and ', format(m_('B'), ''), ' are ', format(m_(''.join(['\\mathbf{a} = ', format(_col_q(a), '')])), ''), ' and ', format(m_(''.join(['\\mathbf{b} = ', format(_col_q(b), '')])), ''), '. The point ', format(m_('P'), ''), ' lies on ', format(m_('AB'), ''), ' so that ', format(m_(''.join(['AP : PB = ', format(mm, ''), ' : ', format(nn, '')])), ''), '. Find the position vector of ', format(m_('P'), ''), '.']))
    cands = [("ratio_swapped", (a[0] + nn * k[0], a[1] + nn * k[1])), ("displacement_only", (mm * k[0], mm * k[1])),
             ("measured_from_b", (b[0] - mm * k[0], b[1] - mm * k[1]))]
    steps = [("Vector AB", f"({d[0]}, {d[1]})"), (f"AP is {mm}/{mm + nn} of AB", f"({mm * k[0]}, {mm * k[1]})"), ("OP = OA + AP", f"({p[0]}, {p[1]})")]
    return _vec_answer("ratio_point_column", q, p, cands, {"task": "ratio_point", "a": list(a), "b": list(b), "m": mm, "n": nn}, steps)


def _position_level2(rng: SeededRandom) -> _Built:
    a, b = _vec(rng, 9), _vec(rng, 9)
    _need((a[0] + b[0]) % 2 == 0 and (a[1] + b[1]) % 2 == 0 and a != b)
    m_pt = ((a[0] + b[0]) // 2, (a[1] + b[1]) // 2)
    q = (''.join(['The position vectors of ', format(m_('A'), ''), ' and ', format(m_('B'), ''), ' are ', format(m_(''.join(['\\mathbf{a} = ', format(_col_q(a), '')])), ''), ' and ', format(m_(''.join(['\\mathbf{b} = ', format(_col_q(b), '')])), ''), '. ', format(m_('M'), ''), ' is the midpoint of ', format(m_('AB'), ''), '. Find the position vector of ', format(m_('M'), ''), '.']))
    cands = [("sum_not_halved", (a[0] + b[0], a[1] + b[1])), ("difference_halved", ((b[0] - a[0]) // 2 if (b[0] - a[0]) % 2 == 0 else Fraction(b[0] - a[0], 2),
                                                                                  (b[1] - a[1]) // 2 if (b[1] - a[1]) % 2 == 0 else Fraction(b[1] - a[1], 2))),
             ("half_of_b", (Fraction(b[0], 2), Fraction(b[1], 2)))]
    steps = [("Add the position vectors", f"({a[0] + b[0]}, {a[1] + b[1]})"), ("Halve", f"({m_pt[0]}, {m_pt[1]})")]
    return _vec_answer("midpoint_column", q, m_pt, cands, {"task": "midpoint", "a": list(a), "b": list(b)}, steps)


def _lin(c: Mapping[str, Fraction]) -> Tuple[Tuple[str, Fraction], ...]:
    return tuple(sorted((k, Fraction(v)) for k, v in c.items() if v != 0))


def _letter_items(cands: Sequence[Tuple[str, Mapping[str, Fraction]]], order: Sequence[str]) -> List[Tuple[str, str, str, Any]]:
    return [(c, m_(_letters(w, order, latex=True)), _letters(w, order, latex=False), _lin(w)) for c, w in cands if any(Fraction(v) != 0 for v in w.values())]


def _letter_answer(skill: str, question: str, res: Mapping[str, Fraction], cands: Sequence[Tuple[str, Mapping[str, Fraction]]],
                   order: Sequence[str], machine: Dict[str, Any], steps: Sequence[Tuple[str, str]]) -> _Built:
    typed = _letters(res, order, latex=False)
    return _Built(skill, question, m_(_letters(res, order, latex=True)), _letter_items(cands, order), _lin(res), machine, list(steps),
                  {"answer_type": "vector", "expected": [typed], "typed": typed})


_RATIOS = tuple((m, n) for m in range(1, 6) for n in range(1, 6) if m != n and math.gcd(m, n) == 1)


def _position_level3(rng: SeededRandom) -> _Built:
    mm, nn = rng.choice(_RATIOS)
    t = mm + nn
    A, B = rng.choice((("A", "B"), ("P", "Q")))
    a, b = ("a", "b") if A == "A" else ("p", "q")
    res = {a: Fraction(nn, t), b: Fraction(mm, t)}
    q = (''.join([format(m_(''.join(['O', format(A, ''), ' = \\mathbf{', format(a, ''), '}'])), ''), ' and ', format(m_(''.join(['O', format(B, ''), ' = \\mathbf{', format(b, ''), '}'])), ''), '. The point ', format(m_('M'), ''), ' lies on ', format(m_(''.join([format(A, ''), format(B, '')])), ''), ' so that ', format(m_(''.join([format(A, ''), 'M : M', format(B, ''), ' = ', format(mm, ''), ' : ', format(nn, '')])), ''), '. Find ', format(m_('OM'), ''), ' in terms of ', format(m_(''.join(['\\mathbf{', format(a, ''), '}'])), ''), ' and ', format(m_(''.join(['\\mathbf{', format(b, ''), '}'])), ''), '.']))
    cands = [("ratio_swapped", {a: Fraction(mm, t), b: Fraction(nn, t)}), ("displacement_only", {a: Fraction(-mm, t), b: Fraction(mm, t)}),
             ("not_divided", {a: Fraction(nn), b: Fraction(mm)})]
    steps = [(f"{A}{B} = {b} - {a}", f"{b} - {a}"), (f"{A}M is {mm}/{t} of {A}{B}", f"({mm}/{t})({b} - {a})"), (f"OM = OA + {A}M", _letters(res, (a, b), latex=False))]
    return _letter_answer("position_letters", q, res, cands, (a, b), {"task": "position_letters", "m": mm, "n": nn, "a": a, "b": b}, steps)


def _position_level4(rng: SeededRandom) -> _Built:
    mm, nn = rng.choice(_RATIOS)
    t = mm + nn
    a, b = "a", "b"
    om = {a: Fraction(nn, t), b: Fraction(mm, t)}
    head = (''.join(['In triangle ', format(m_('OAB'), ''), ', ', format(m_('OA = \\mathbf{a}'), ''), ' and ', format(m_('OB = \\mathbf{b}'), ''), '. The point ', format(m_('M'), ''), ' lies on ', format(m_('AB'), ''), ' so that ', format(m_(''.join(['AM : MB = ', format(mm, ''), ' : ', format(nn, '')])), ''), '.']))
    if rng.chance(1, 2):
        q = head + ''.join([' Find ', format(m_('AM'), ''), ' in terms of ', format(m_('\\mathbf{a}'), ''), ' and ', format(m_('\\mathbf{b}'), ''), '.'])
        res = {a: Fraction(-mm, t), b: Fraction(mm, t)}
        cands = [("ratio_swapped", {a: Fraction(-nn, t), b: Fraction(nn, t)}), ("wrong_direction", {a: Fraction(mm, t), b: Fraction(-mm, t)}), ("position_only", om)]
        steps = [("AB = b - a", "b - a"), (f"AM is {mm}/{t} of AB", f"({mm}/{t})(b - a)")]
        return _letter_answer("vector_in_triangle", q, res, cands, (a, b), {"task": "vector_AM", "m": mm, "n": nn}, steps)
    q = head + (''.join([' ', format(m_('N'), ''), ' is the midpoint of ', format(m_('OB'), ''), '. Find ', format(m_('MN'), ''), ' in terms of ', format(m_('\\mathbf{a}'), ''), ' and ', format(m_('\\mathbf{b}'), ''), '.']))
    res = {a: -om[a], b: Fraction(1, 2) - om[b]}
    _need(any(v != 0 for v in res.values()))
    cands = [("sign_reversed", {a: om[a], b: om[b] - Fraction(1, 2)}), ("forgot_half", {a: -om[a], b: 1 - om[b]}), ("position_only", om)]
    steps = [("OM", _letters(om, (a, b), latex=False)), ("ON = half of b", "(1/2)b"), ("MN = ON - OM", _letters(res, (a, b), latex=False))]
    return _letter_answer("vector_in_triangle", q, res, cands, (a, b), {"task": "vector_MN", "m": mm, "n": nn}, steps)


class PositionVectorsGenerator(_FamilyGenerator):
    generator_id = POSITION_ID
    version = 1
    levels = (1, 2, 3, 4)
    level_skills = POSITION_LEVEL_SKILLS
    error_notes = POSITION_ERROR_NOTES
    builders = {1: _position_level1, 2: _position_level2, 3: _position_level3, 4: _position_level4}


# ==========================================================================
# Lessons 15841-15843: Transformations in coordinate form
# ==========================================================================

TRANSFORM_ERROR_NOTES: Dict[str, Dict[str, str]] = {
    "translate_points": {
        "sign_reversed": "moved the shape in the opposite direction",
        "components_swapped": "used the top number for the up-and-down move and the bottom number for the sideways move",
        "x_only": "applied only the sideways part of the translation",
    },
    "reflect_points": {
        "wrong_axis": "reflected in the other axis or line",
        "negated_both": "changed the sign of both coordinates, which is a rotation of 180 degrees, not a reflection",
        "distance_not_doubled": "moved each point only as far as the mirror line instead of the same distance beyond it",
        "swapped_only": "swapped the coordinates when the mirror line is not y = x",
    },
    "rotate_points": {
        "wrong_direction": "turned the shape the other way round (clockwise instead of anticlockwise or the reverse)",
        "half_turn_used": "used a half turn instead of a quarter turn",
        "quarter_turn_used": "turned through 90 degrees when a half turn was asked for",
        "swapped_only": "swapped the coordinates without changing a sign",
        "centre_ignored": "turned about the origin although the centre was a different point",
    },
    "enlarge_points": {
        "centre_ignored": "multiplied the coordinates by the scale factor as if the centre were the origin",
        "scale_added": "added the scale factor to each coordinate instead of multiplying distances from the centre",
        "inverse_factor": "divided the distances from the centre by the scale factor instead of multiplying",
        "sign_ignored": "ignored the minus sign of a negative scale factor",
    },
    "describe_transformation": {
        "translation_instead": "gave a translation when the shape has been turned, reflected or enlarged",
        "centre_missing": "described the type of transformation but gave the wrong centre or line",
        "factor_wrong": "gave the wrong scale factor or angle",
    },
}

TRANSFORM_LEVEL_SKILLS: Dict[int, Tuple[str, ...]] = {
    1: ("translate_points",),
    2: ("reflect_points",),
    3: ("rotate_points",),
    4: ("enlarge_points",),
    5: ("describe_transformation",),
}

Point = Tuple[Fraction, Fraction]


def _pt(x: Any, y: Any) -> Point:
    return (Fraction(x), Fraction(y))


def _pt_text(p: Point) -> str:
    return f"({_dec_text(p[0])}, {_dec_text(p[1])})"


def _pts_text(points: Sequence[Point]) -> str:
    return ", ".join(_pt_text(p) for p in points)


def _scalene_triangle(rng: SeededRandom, low: int = -6, high: int = 6) -> List[Point]:
    for _ in range(100):
        pts = [_pt(rng.randint(low, high), rng.randint(low, high)) for _ in range(3)]
        (x1, y1), (x2, y2), (x3, y3) = pts
        area2 = (x2 - x1) * (y3 - y1) - (x3 - x1) * (y2 - y1)
        sides = sorted([(x1 - x2) ** 2 + (y1 - y2) ** 2, (x2 - x3) ** 2 + (y2 - y3) ** 2, (x1 - x3) ** 2 + (y1 - y3) ** 2])
        if area2 != 0 and len(set(sides)) == 3:
            return pts
    raise _Retry()


def _label(points: Sequence[Point], names: str = "ABC", prime: bool = False) -> str:
    return ", ".join(''.join([format(m_(''.join([format(n, ''), format(chr(39) if prime else '', ''), format(_pt_text(p), '')])), '')]) for n, p in zip(names, points))


def _apply_translate(points: Sequence[Point], v: Point) -> List[Point]:
    return [(x + v[0], y + v[1]) for x, y in points]


def _apply_rotate(points: Sequence[Point], centre: Point, quarter_turns_acw: int) -> List[Point]:
    out = []
    for x, y in points:
        dx, dy = x - centre[0], y - centre[1]
        for _ in range(quarter_turns_acw % 4):
            dx, dy = -dy, dx
        out.append((centre[0] + dx, centre[1] + dy))
    return out


def _apply_enlarge(points: Sequence[Point], centre: Point, k: Fraction) -> List[Point]:
    return [(centre[0] + k * (x - centre[0]), centre[1] + k * (y - centre[1])) for x, y in points]


def _reflect_one(p: Point, line: Tuple[str, Fraction]) -> Point:
    kind, c = line
    x, y = p
    if kind == "x":      # the line x = c
        return (2 * c - x, y)
    if kind == "y":      # the line y = c
        return (x, 2 * c - y)
    if kind == "y=x":
        return (y, x)
    if kind == "y=-x":
        return (-y, -x)
    raise GeneratorError("unknown line")


def _line_name(line: Tuple[str, Fraction]) -> str:
    kind, c = line
    if kind == "x":
        return "x = " + _dec_text(c) if c != 0 else "x = 0"
    if kind == "y":
        return "y = " + _dec_text(c) if c != 0 else "y = 0"
    return {"y=x": "y = x", "y=-x": "y = -x"}[kind]


def _points_answer(skill: str, question: str, image: Sequence[Point], cands: Sequence[Tuple[str, Sequence[Point]]], machine: Dict[str, Any],
                   steps: Sequence[Tuple[str, str]], names: str) -> _Built:
    typed = _pts_text(image)
    items = []
    seen = {tuple(image)}
    for code, pts in cands:
        t = tuple(pts)
        if t in seen:
            continue
        seen.add(t)
        items.append((code, m_(_pts_text(pts)), _pts_text(pts), t))
    display = ", ".join(m_(f"{n}' = {_pt_text(p)}") for n, p in zip(names, image))
    return _Built(skill, question, display, items, tuple(image), machine, list(steps),
                  {"answer_type": "coordinates", "expected": [typed], "typed": typed})


def _transform_level1(rng: SeededRandom) -> _Built:
    pts = _scalene_triangle(rng)
    v = (rng.randint(-8, 8), rng.randint(-8, 8))
    _need(v[0] != 0 and v[1] != 0 and abs(v[0]) != abs(v[1]))
    img = _apply_translate(pts, _pt(*v))
    q = (f"Triangle {m_('ABC')} has vertices {_label(pts)}. It is translated by the vector {m_(_col_q(v))}. "
         "Write down the coordinates of the images of A, B and C, in that order.")
    cands = [("sign_reversed", _apply_translate(pts, _pt(-v[0], -v[1]))), ("components_swapped", _apply_translate(pts, _pt(v[1], v[0]))),
             ("x_only", _apply_translate(pts, _pt(v[0], 0)))]
    steps = [("Add the top number to each x-coordinate", f"x + {v[0]}"), ("Add the bottom number to each y-coordinate", f"y + {v[1]}"), ("Images", _pts_text(img))]
    return _points_answer("translate_points", q, img, cands, {"task": "translate", "points": [_pt_text(p) for p in pts], "vector": list(v)}, steps, "ABC")


_REFLECT_LINES = (("y", Fraction(0)), ("x", Fraction(0)), ("x", None), ("y", None), ("y=x", Fraction(0)), ("y=-x", Fraction(0)))


def _transform_level2(rng: SeededRandom) -> _Built:
    pts = _scalene_triangle(rng)
    kind, c = rng.choice(_REFLECT_LINES)
    if c is None:
        c = Fraction(rng.randint(-4, 4))
        _need(c != 0)
    line = (kind, c)
    img = [_reflect_one(p, line) for p in pts]
    _need(tuple(img) != tuple(pts))
    name = _line_name(line)
    where = {"y": "the x-axis" if c == 0 else f"the line {m_(name)}", "x": "the y-axis" if c == 0 else f"the line {m_(name)}"}.get(kind, f"the line {m_(name)}")
    q = (f"Triangle {m_('ABC')} has vertices {_label(pts)}. It is reflected in {where}. "
         "Write down the coordinates of the images of A, B and C, in that order.")
    other = {"y": ("x", c), "x": ("y", c), "y=x": ("y=-x", Fraction(0)), "y=-x": ("y=x", Fraction(0))}[kind]
    cands: List[Tuple[str, Sequence[Point]]] = [("wrong_axis", [_reflect_one(p, other) for p in pts])]
    if kind in ("x", "y") and c == 0:
        cands.append(("negated_both", [(-x, -y) for x, y in pts]))
    elif kind in ("x", "y"):
        cands.append(("distance_not_doubled", [(c, y) if kind == "x" else (x, c) for x, y in pts]))
        cands.append(("negated_both", [(-x, -y) for x, y in pts]))
    else:
        cands.append(("negated_both", [(-x, -y) for x, y in pts]))
    cands.append(("swapped_only", [(y, x) for x, y in pts]))
    steps = [("Each image is the same distance from the mirror line on the other side", name), ("Images", _pts_text(img))]
    return _points_answer("reflect_points", q, img, cands, {"task": "reflect", "points": [_pt_text(p) for p in pts], "line": [kind, str(c)]}, steps, "ABC")


def _transform_level3(rng: SeededRandom) -> _Built:
    pts = _scalene_triangle(rng, -5, 5)
    about_origin = rng.chance(1, 2)
    centre = _pt(0, 0) if about_origin else _pt(rng.randint(-4, 4), rng.randint(-4, 4))
    _need(about_origin or centre != _pt(0, 0))
    turn = rng.choice((("90 degrees clockwise", 3), ("90 degrees anticlockwise", 1), ("180 degrees", 2)))
    text, quarters = turn
    img = _apply_rotate(pts, centre, quarters)
    where = "the origin" if about_origin else f"the point {m_(_pt_text(centre))}"
    q = (f"Triangle {m_('ABC')} has vertices {_label(pts)}. It is rotated through {text} about {where}. "
         "Write down the coordinates of the images of A, B and C, in that order.")
    cands: List[Tuple[str, Sequence[Point]]] = []
    if quarters in (1, 3):
        cands.append(("wrong_direction", _apply_rotate(pts, centre, 4 - quarters)))
        cands.append(("half_turn_used", _apply_rotate(pts, centre, 2)))
    else:
        cands.append(("quarter_turn_used", _apply_rotate(pts, centre, 1)))
    cands.append(("swapped_only", [(centre[0] + (y - centre[1]), centre[1] + (x - centre[0])) for x, y in pts]))
    if not about_origin:
        cands.append(("centre_ignored", _apply_rotate(pts, _pt(0, 0), quarters)))
    steps = [("Find each point's position relative to the centre", f"centre {_pt_text(centre)}"), ("Turn each offset", text), ("Images", _pts_text(img))]
    return _points_answer("rotate_points", q, img, cands, {"task": "rotate", "points": [_pt_text(p) for p in pts], "centre": [str(centre[0]), str(centre[1])], "quarters": quarters}, steps, "ABC")


def _transform_level4(rng: SeededRandom) -> _Built:
    k = rng.choice((Fraction(2), Fraction(3), Fraction(4), Fraction(-1), Fraction(-2), Fraction(1, 2)))
    about_origin = rng.chance(1, 2)
    centre = _pt(0, 0) if about_origin else _pt(rng.randint(-4, 4), rng.randint(-4, 4))
    _need(about_origin or centre != _pt(0, 0))
    lim = 3 if abs(k) >= 3 else 5
    pts = _scalene_triangle(rng, -lim, lim)
    if k == Fraction(1, 2):
        pts = [(centre[0] + 2 * round((x - centre[0]) / 2), centre[1] + 2 * round((y - centre[1]) / 2)) for x, y in pts]
        _need(len(set(pts)) == 3)
        (x1, y1), (x2, y2), (x3, y3) = pts
        _need((x2 - x1) * (y3 - y1) - (x3 - x1) * (y2 - y1) != 0)
    img = _apply_enlarge(pts, centre, k)
    ktext = "1/2" if k == Fraction(1, 2) else str(k)
    kdisp = r"\frac{1}{2}" if k == Fraction(1, 2) else str(k)
    where = "the origin" if about_origin else f"the point {m_(_pt_text(centre))}"
    q = (f"Triangle {m_('ABC')} has vertices {_label(pts)}. It is enlarged with scale factor {m_(kdisp)} and centre {where}. "
         "Write down the coordinates of the images of A, B and C, in that order.")
    cands: List[Tuple[str, Sequence[Point]]] = []
    if not about_origin:
        cands.append(("centre_ignored", [(k * x, k * y) for x, y in pts]))
    cands.append(("scale_added", [(x + k, y + k) for x, y in pts]))
    inverse = _apply_enlarge(pts, centre, 1 / k)
    if all(_dec_text(c) == str(c) or "/" not in _dec_text(c) for p_ in inverse for c in p_):
        cands.append(("inverse_factor", inverse))
    if k < 0:
        cands.append(("sign_ignored", _apply_enlarge(pts, centre, -k)))
    steps = [("Vector from the centre to each point", f"centre {_pt_text(centre)}"), (f"Multiply each vector by {ktext}", ktext), ("Add to the centre", _pts_text(img))]
    return _points_answer("enlarge_points", q, img, cands, {"task": "enlarge", "points": [_pt_text(p) for p in pts], "centre": [str(centre[0]), str(centre[1])], "k": ktext}, steps, "ABC")


def _transform_level5(rng: SeededRandom) -> _Built:
    pts = _scalene_triangle(rng, -5, 5)
    kind = rng.choice(("translation", "reflection", "rotation", "enlargement"))
    if kind == "translation":
        v = (rng.randint(-8, 8), rng.randint(-8, 8))
        _need(v != (0, 0))
        img = _apply_translate(pts, _pt(*v))
        ans = rf"Translation by the vector {m_(_col_q(v))}"
        wrong = [("centre_missing", rf"Translation by the vector {m_(_col_q((-v[0], -v[1])))}"), ("factor_wrong", rf"Translation by the vector {m_(_col_q((v[1], v[0])))}")]
        desc = {"type": "translation", "vector": list(v)}
    elif kind == "reflection":
        rk, c = rng.choice((("x", Fraction(rng.randint(-5, 5))), ("y", Fraction(rng.randint(-5, 5))), ("y=x", Fraction(0)), ("y=-x", Fraction(0))))
        line = (rk, c)
        img = [_reflect_one(p, line) for p in pts]
        _need(tuple(img) != tuple(pts))
        ans = f"Reflection in the line {m_(_line_name(line))}"
        other = (("y" if rk == "x" else "x"), c) if rk in ("x", "y") else (("y=-x" if rk == "y=x" else "y=x"), Fraction(0))
        wrong = [("centre_missing", f"Reflection in the line {m_(_line_name(other))}"), ("translation_instead", "Translation")]
        desc = {"type": "reflection", "line": [rk, str(c)]}
    elif kind == "rotation":
        quarters = rng.choice((1, 2, 3))
        centre = _pt(rng.randint(-3, 3), rng.randint(-3, 3))
        img = _apply_rotate(pts, centre, quarters)
        _need(tuple(img) != tuple(pts))
        angle = {1: "90 degrees anticlockwise", 2: "180 degrees", 3: "90 degrees clockwise"}[quarters]
        ans = f"Rotation through {angle} about the point {m_(_pt_text(centre))}"
        wrong_angle = {1: "90 degrees clockwise", 2: "90 degrees anticlockwise", 3: "90 degrees anticlockwise"}[quarters]
        wrong = [("factor_wrong", f"Rotation through {wrong_angle} about the point {m_(_pt_text(centre))}"),
                 ("centre_missing", f"Rotation through {angle} about the origin")]
        desc = {"type": "rotation", "quarters": quarters, "centre": [str(centre[0]), str(centre[1])]}
    else:
        k = rng.choice((Fraction(2), Fraction(3), Fraction(-1), Fraction(-2), Fraction(1, 2)))
        centre = _pt(rng.randint(-3, 3), rng.randint(-3, 3))
        if k == Fraction(1, 2):
            pts = [(centre[0] + 2 * round((x - centre[0]) / 2), centre[1] + 2 * round((y - centre[1]) / 2)) for x, y in pts]
            _need(len(set(pts)) == 3)
            (x1, y1), (x2, y2), (x3, y3) = pts
            _need((x2 - x1) * (y3 - y1) - (x3 - x1) * (y2 - y1) != 0)
            sides = sorted([(x1 - x2) ** 2 + (y1 - y2) ** 2, (x2 - x3) ** 2 + (y2 - y3) ** 2, (x1 - x3) ** 2 + (y1 - y3) ** 2])
            _need(len(set(sides)) == 3)
        img = _apply_enlarge(pts, centre, k)
        _need(tuple(img) != tuple(pts))
        kt = "1/2" if k == Fraction(1, 2) else str(k)
        kd = r"\frac{1}{2}" if k == Fraction(1, 2) else str(k)
        ans = f"Enlargement with scale factor {m_(kd)} and centre {m_(_pt_text(centre))}"
        wrong = [("factor_wrong", f"Enlargement with scale factor {m_(_latex(1 / k))} and centre {m_(_pt_text(centre))}"),
                 ("centre_missing", f"Enlargement with scale factor {m_(kd)} and centre the origin")]
        desc = {"type": "enlargement", "k": kt, "centre": [str(centre[0]), str(centre[1])]}
    q = (f"Triangle {m_('T')} has vertices {_label(pts)}. Its image {m_(chr(84) + chr(39))} has vertices {_label(img, prime=True)}. "
         f"Describe fully the single transformation that maps {m_('T')} onto {m_(chr(84) + chr(39))}.")
    items = [(c, d, "", d) for c, d in wrong]
    steps = [("Compare the object and the image: orientation, size and position", kind), ("Find the details from corresponding points", ans)]
    return _Built("describe_transformation", q, ans, items, ans,
                  {"task": "describe_transformation", "answer_type": "text_description", "points": [_pt_text(p) for p in pts], "image": [_pt_text(p) for p in img], "transform": desc},
                  steps, {"answer_type": "text_description", "expected": [ans], "typed": ans})


class TransformationsCoordinatesGenerator(_FamilyGenerator):
    generator_id = TRANSFORM_ID
    version = 1
    levels = (1, 2, 3, 4, 5)
    level_skills = TRANSFORM_LEVEL_SKILLS
    error_notes = TRANSFORM_ERROR_NOTES
    builders = {1: _transform_level1, 2: _transform_level2, 3: _transform_level3, 4: _transform_level4, 5: _transform_level5}



# ==========================================================================
# Matrix helpers shared by the three matrix lessons
# ==========================================================================


def _mat_key(a: Matrix) -> Tuple[Tuple[Fraction, ...], ...]:
    return a


def _mat_item(code: str, a: Matrix) -> Tuple[str, str, str, Any]:
    return (code, m_(_mat_latex(a)), _mat_typed(a), _mat_key(a))


def _mat_answer(skill: str, question: str, ans: Matrix, cands: Sequence[Tuple[str, Matrix]], machine: Dict[str, Any], steps: Sequence[Tuple[str, str]],
                display: Optional[str] = None) -> _Built:
    typed = _mat_typed(ans)
    return _Built(skill, question, m_(display or _mat_latex(ans)), [_mat_item(c, w) for c, w in cands], _mat_key(ans),
                  {**machine, "value": typed}, list(steps), {"answer_type": "matrix", "expected": [typed], "typed": typed})


def _named(name: str, a: Matrix) -> str:
    return m_(rf"\mathbf{{{name}}} = {_mat_latex(a)}")


# ==========================================================================
# Lesson 15844: Matrix Basics, Addition, and Subtraction
# ==========================================================================

MATRIX_BASICS_ERROR_NOTES: Dict[str, Dict[str, str]] = {
    "matrix_add": {
        "subtracted_instead": "subtracted the matrices instead of adding them",
        "entries_multiplied": "multiplied the matching entries instead of adding them",
        "sign_slip": "made a sign error when adding a negative entry",
    },
    "matrix_subtract": {
        "added_instead": "added the matrices instead of subtracting them",
        "order_reversed": "subtracted in the wrong order",
        "sign_slip": "made a sign error when subtracting a negative entry",
    },
    "matrix_scalar": {
        "one_row_only": "multiplied only the top row by the scalar",
        "scalar_added": "added the scalar to each entry instead of multiplying",
        "diagonal_only": "multiplied only the entries on the main diagonal",
    },
    "matrix_combination": {
        "sign_slip": "used the opposite sign between the two matrices",
        "first_not_scaled": "did not multiply the first matrix by the scalar",
        "both_scaled": "multiplied both matrices by the scalar when only the first was to be multiplied",
    },
    "equal_matrices": {
        "sign_slip": "moved the constant across with the wrong sign",
        "not_divided": "moved the constant correctly but forgot to divide by the coefficient",
        "values_swapped": "found both values but gave x and y the wrong way round",
    },
    "stock_matrix": {
        "added_instead": "added the sales to the stock instead of subtracting",
        "order_reversed": "subtracted the stock from the sales",
        "rows_mixed": "subtracted the entries from the wrong row",
    },
    "stock_total": {
        "one_row_only": "totalled only one row of the matrix",
        "diagonal_only": "added only the two entries on the main diagonal",
    },
}

MATRIX_BASICS_LEVEL_SKILLS: Dict[int, Tuple[str, ...]] = {
    1: ("matrix_add", "matrix_subtract"),
    2: ("matrix_scalar", "matrix_combination"),
    3: ("equal_matrices",),
    4: ("stock_matrix", "stock_total"),
}


def _matrix_basics_level1(rng: SeededRandom) -> _Built:
    A, B = _rand_mat(rng, -9, 9), _rand_mat(rng, -9, 9)
    if rng.chance(1, 2):
        q = ''.join([format(_named('A', A), ''), ' and ', format(_named('B', B), ''), '. Find ', format(m_('\\mathbf{A} + \\mathbf{B}'), ''), '.'])
        ans = _mat_add(A, B)
        cands = [("subtracted_instead", _mat_add(A, B, -1)), ("entries_multiplied", _mat(tuple(tuple(x * y for x, y in zip(ra, rb)) for ra, rb in zip(A, B)))),
                 ("sign_slip", _mat(tuple(tuple(x + (abs(y) if y < 0 else y) for x, y in zip(ra, rb)) for ra, rb in zip(A, B))))]
        steps = [("Add the entries in the same positions", _mat_typed(ans))]
        return _mat_answer("matrix_add", q, ans, cands, {"task": "add", "A": _mat_typed(A), "B": _mat_typed(B)}, steps)
    q = ''.join([format(_named('A', A), ''), ' and ', format(_named('B', B), ''), '. Find ', format(m_('\\mathbf{A} - \\mathbf{B}'), ''), '.'])
    ans = _mat_add(A, B, -1)
    cands = [("added_instead", _mat_add(A, B)), ("order_reversed", _mat_add(B, A, -1)),
             ("sign_slip", _mat(tuple(tuple(x - (abs(y) if y < 0 else y) for x, y in zip(ra, rb)) for ra, rb in zip(A, B))))]
    steps = [("Subtract the entries in the same positions", _mat_typed(ans))]
    return _mat_answer("matrix_subtract", q, ans, cands, {"task": "subtract", "A": _mat_typed(A), "B": _mat_typed(B)}, steps)


def _matrix_basics_level2(rng: SeededRandom) -> _Built:
    A, B = _rand_mat(rng, -7, 7), _rand_mat(rng, -7, 7)
    if rng.chance(1, 3):
        k = rng.choice((-3, -2, 2, 3, 4, 5))
        q = ''.join([format(_named('A', A), ''), '. Find ', format(m_(''.join([format(k, ''), '\\mathbf{A}'])), ''), '.'])
        ans = _mat_scale(k, A)
        cands = [("one_row_only", _mat(((k * A[0][0], k * A[0][1]), A[1]))), ("scalar_added", _mat(tuple(tuple(v + k for v in row) for row in A))),
                 ("diagonal_only", _mat(((k * A[0][0], A[0][1]), (A[1][0], k * A[1][1]))))]
        steps = [(f"Multiply every entry by {k}", _mat_typed(ans))]
        return _mat_answer("matrix_scalar", q, ans, cands, {"task": "scalar", "A": _mat_typed(A), "k": k}, steps)
    k = rng.choice((2, 3, 4))
    sign = rng.choice((1, -1))
    expr = rf"{k}\mathbf{{A}} {'+' if sign == 1 else '-'} \mathbf{{B}}"
    q = f"{_named('A', A)} and {_named('B', B)}. Find {m_(expr)}."
    ans = _mat_add(_mat_scale(k, A), B, sign)
    cands = [("sign_slip", _mat_add(_mat_scale(k, A), B, -sign)), ("first_not_scaled", _mat_add(A, B, sign)),
             ("both_scaled", _mat_add(_mat_scale(k, A), _mat_scale(k, B), sign))]
    steps = [(f"Work out {k}A", _mat_typed(_mat_scale(k, A))), ("Combine with B entry by entry", _mat_typed(ans))]
    return _mat_answer("matrix_combination", q, ans, cands, {"task": "combination", "A": _mat_typed(A), "B": _mat_typed(B), "k": k, "sign": sign}, steps)


def _matrix_basics_level3(rng: SeededRandom) -> _Built:
    x, y = rng.randint(-8, 8), rng.randint(-8, 8)
    _need(x != 0 and y != 0 and x != y)
    p, q_ = rng.randint(1, 4), rng.randint(1, 4)
    c1, c2 = rng.randint(-9, 9), rng.randint(-9, 9)
    _need(c1 != 0 and c2 != 0)
    v1, v2 = p * x + c1, q_ * y + c2
    r, s_ = rng.randint(-9, 9), rng.randint(-9, 9)

    def term(coef: int, var: str, const: int) -> str:
        c = var if coef == 1 else f"{coef}{var}"
        return f"{c} {'+' if const > 0 else '-'} {abs(const)}"

    left = rf"\begin{{pmatrix}} {term(p, 'x', c1)} & {r} \\ {s_} & {term(q_, 'y', c2)} \end{{pmatrix}}"
    right = _mat_latex(_mat(((v1, r), (s_, v2))))
    q = f"Given that {m_(f'{left} = {right}')}, find the value of {m_('x')} and the value of {m_('y')}."
    typed = f"x = {x} and y = {y}"
    cands = [("sign_slip", (Fraction(v1 + c1, p), Fraction(v2 + c2, q_))), ("not_divided", (Fraction(v1 - c1), Fraction(v2 - c2))), ("values_swapped", (Fraction(y), Fraction(x)))]
    items = []
    for code, (wx, wy) in cands:
        t = f"x = {_typed(wx)} and y = {_typed(wy)}"
        items.append((code, m_(rf"x = {_latex(wx)},\ y = {_latex(wy)}"), t, (wx, wy)))
    steps = [("Equate the top-left entries", f"{term(p, 'x', c1)} = {v1}"), ("Solve for x", f"x = {x}"), ("Equate the bottom-right entries", f"{term(q_, 'y', c2)} = {v2}"), ("Solve for y", f"y = {y}")]
    return _Built("equal_matrices", q, m_(rf"x = {x},\ y = {y}"), items, (Fraction(x), Fraction(y)),
                  {"task": "equal_matrices", "x": x, "y": y, "p": p, "q": q_, "c1": c1, "c2": c2}, steps,
                  {"answer_type": "equation_solution", "expected": [typed], "typed": typed})


_STOCK_ITEMS = (("shoes", "pairs of shoes", ("men", "women"), ("size 6", "size 8")),
                ("school jerseys", "jerseys", ("boys", "girls"), ("small", "large")),
                ("sacks of maize meal", "sacks", ("Windhoek store", "Oshakati store"), ("5 kg", "10 kg")),
                ("calculators", "calculators", ("basic", "scientific"), ("black", "blue")))


def _matrix_basics_level4(rng: SeededRandom) -> _Built:
    _, noun, rows, cols = rng.choice(_STOCK_ITEMS)
    S = _rand_mat(rng, 20, 140)
    R = _mat(tuple(tuple(Fraction(rng.randint(5, int(S[i][j]) - 5)) for j in range(2)) for i in range(2)))
    head = (''.join(['The fictional Kudu General Store sells ', format(noun, ''), '. The matrix ', format(m_(''.join(['\\mathbf{S} = ', format(_mat_latex(S), '')])), ''), ' shows the number in stock at the start of the week. The rows show ', format(rows[0], ''), ' and ', format(rows[1], ''), '; the columns show ', format(cols[0], ''), ' and ', format(cols[1], ''), '. The matrix ', format(m_(''.join(['\\mathbf{R} = ', format(_mat_latex(R), '')])), ''), ' shows the number sold during the week.']))
    if rng.chance(2, 3):
        q = head + f" Find the matrix that shows the number left in stock at the end of the week."
        ans = _mat_add(S, R, -1)
        cands = [("added_instead", _mat_add(S, R)), ("order_reversed", _mat_add(R, S, -1)),
                 ("rows_mixed", _mat(((S[0][0] - R[1][0], S[0][1] - R[1][1]), (S[1][0] - R[0][0], S[1][1] - R[0][1]))))]
        return _mat_answer("stock_matrix", q, ans, cands, {"task": "stock_left", "S": _mat_typed(S), "R": _mat_typed(R)}, [("Subtract the sales from the stock", _mat_typed(ans))])
    q = head + f" Calculate the total number of {noun} in stock at the start of the week."
    total = sum(S[i][j] for i in range(2) for j in range(2))
    cands = [("one_row_only", S[0][0] + S[0][1]), ("diagonal_only", S[0][0] + S[1][1])]
    return _exact("stock_total", q, total, cands=[(c, Fraction(v)) for c, v in cands], machine={"task": "stock_total", "S": _mat_typed(S)},
                  steps=[("Add all four entries of S", str(total))])


class MatrixBasicsGenerator(_FamilyGenerator):
    generator_id = MATRIX_BASICS_ID
    version = 1
    levels = (1, 2, 3, 4)
    level_skills = MATRIX_BASICS_LEVEL_SKILLS
    error_notes = MATRIX_BASICS_ERROR_NOTES
    builders = {1: _matrix_basics_level1, 2: _matrix_basics_level2, 3: _matrix_basics_level3, 4: _matrix_basics_level4}


# ==========================================================================
# Lesson 15845: Matrix Multiplication and Properties
# ==========================================================================

MATRIX_MULT_ERROR_NOTES: Dict[str, Dict[str, str]] = {
    "matrix_times_column": {
        "rows_by_rows": "multiplied the entries of the matrix by the entries of the column in the wrong pairs",
        "swapped_result": "worked out both entries correctly but wrote them in the wrong order",
        "entrywise": "multiplied only the entries in matching positions instead of adding the products",
    },
    "matrix_product": {
        "entrywise": "multiplied the matching entries instead of using rows times columns",
        "order_reversed": "multiplied the matrices in the wrong order",
        "rows_by_rows": "multiplied each row of the first matrix by each row of the second, not by its columns",
    },
    "matrix_reverse_order": {
        "order_reversed": "worked out AB when BA was asked for",
        "entrywise": "multiplied the matching entries instead of using rows times columns",
    },
    "matrix_square": {
        "entries_squared": "squared each entry instead of multiplying the matrix by itself",
        "doubled": "multiplied the matrix by 2 instead of by itself",
    },
    "unknown_in_product": {
        "sign_slip": "moved the known part across with the wrong sign",
        "not_divided": "moved the known part correctly but did not divide by the coefficient of k",
        "wrong_entry": "equated k to the wrong entry of the product",
    },
}

MATRIX_MULT_LEVEL_SKILLS: Dict[int, Tuple[str, ...]] = {
    1: ("matrix_times_column",),
    2: ("matrix_product",),
    3: ("matrix_reverse_order", "matrix_square"),
    4: ("unknown_in_product",),
}


def _matrix_mult_level1(rng: SeededRandom) -> _Built:
    A = _rand_mat(rng, -6, 6)
    v = _col(rng.randint(-6, 6), rng.randint(-6, 6))
    ans = _mat_mul(A, v)
    q = ''.join([format(_named('A', A), ''), ' and ', format(m_(''.join(['\\mathbf{v} = ', format(_mat_latex(v), '')])), ''), '. Find ', format(m_('\\mathbf{A}\\mathbf{v}'), ''), '.'])
    cands = [("rows_by_rows", _col(A[0][0] * v[0][0] + A[1][0] * v[1][0], A[0][1] * v[0][0] + A[1][1] * v[1][0])),
             ("swapped_result", _col(ans[1][0], ans[0][0])),
             ("entrywise", _col(A[0][0] * v[0][0], A[1][1] * v[1][0]))]
    steps = [("Top entry: row 1 times the column", f"{A[0][0]} x {v[0][0]} + {A[0][1]} x {v[1][0]}"), ("Bottom entry: row 2 times the column", f"{A[1][0]} x {v[0][0]} + {A[1][1]} x {v[1][0]}"),
             ("Result", _mat_typed(ans))]
    return _mat_answer("matrix_times_column", q, ans, cands, {"task": "matrix_times_column", "A": _mat_typed(A), "v": _mat_typed(v)}, steps)


def _matrix_mult_level2(rng: SeededRandom) -> _Built:
    A, B = _rand_mat(rng, -5, 5), _rand_mat(rng, -5, 5)
    ans = _mat_mul(A, B)
    _need(_mat_mul(B, A) != ans)
    q = ''.join([format(_named('A', A), ''), ' and ', format(_named('B', B), ''), '. Find ', format(m_('\\mathbf{A}\\mathbf{B}'), ''), '.'])
    rows_by_rows = _mat(tuple(tuple(sum(A[i][k] * B[j][k] for k in range(2)) for j in range(2)) for i in range(2)))
    cands = [("entrywise", _mat(tuple(tuple(x * y for x, y in zip(ra, rb)) for ra, rb in zip(A, B)))), ("order_reversed", _mat_mul(B, A)), ("rows_by_rows", rows_by_rows)]
    steps = [("Entry in row 1, column 1", f"{A[0][0]} x {B[0][0]} + {A[0][1]} x {B[1][0]}"), ("Complete the product", _mat_typed(ans))]
    return _mat_answer("matrix_product", q, ans, cands, {"task": "matrix_product", "A": _mat_typed(A), "B": _mat_typed(B)}, steps)


def _matrix_mult_level3(rng: SeededRandom) -> _Built:
    A, B = _rand_mat(rng, -5, 5), _rand_mat(rng, -5, 5)
    if rng.chance(1, 2):
        ans = _mat_mul(B, A)
        _need(_mat_mul(A, B) != ans)
        q = ''.join([format(_named('A', A), ''), ' and ', format(_named('B', B), ''), '. Find ', format(m_('\\mathbf{B}\\mathbf{A}'), ''), '.'])
        cands = [("order_reversed", _mat_mul(A, B)), ("entrywise", _mat(tuple(tuple(x * y for x, y in zip(ra, rb)) for ra, rb in zip(A, B))))]
        return _mat_answer("matrix_reverse_order", q, ans, cands, {"task": "matrix_BA", "A": _mat_typed(A), "B": _mat_typed(B)},
                           [("Rows of B times columns of A", _mat_typed(ans))])
    ans = _mat_mul(A, A)
    _need(ans != _mat_scale(2, A))
    q = ''.join([format(_named('A', A), ''), '. Find ', format(m_('\\mathbf{A}^{2}'), ''), '.'])
    cands = [("entries_squared", _mat(tuple(tuple(v * v for v in row) for row in A))), ("doubled", _mat_scale(2, A))]
    return _mat_answer("matrix_square", q, ans, cands, {"task": "matrix_square", "A": _mat_typed(A)}, [("A squared is A times A", _mat_typed(ans))])


def _matrix_mult_level4(rng: SeededRandom) -> _Built:
    k = rng.randint(-6, 6)
    _need(k != 0)
    p, r, s = rng.randint(-4, 4), rng.randint(-4, 4), rng.randint(-4, 4)
    u, v, w, z = (rng.randint(-4, 4) for _ in range(4))
    _need(w != 0 and p != 0)
    # A = (p k; r s), B = (u v; w z); the entry (1,1) of AB is p u + k w
    A_known = f"{_mat_latex(_mat(((p, k), (r, s))))}"
    A_text = rf"\begin{{pmatrix}} {p} & k \\ {r} & {s} \end{{pmatrix}}"
    A = _mat(((p, k), (r, s)))
    B = _mat(((u, v), (w, z)))
    AB = _mat_mul(A, B)
    q = (''.join([format(m_(''.join(['\\mathbf{A} = ', format(A_text, '')])), ''), ' and ', format(_named('B', B), ''), '. Given that ', format(m_(''.join(['\\mathbf{A}\\mathbf{B} = ', format(_mat_latex(AB), '')])), ''), ', find the value of ', format(m_('k'), ''), '.']))
    target = AB[0][0]
    cands = [("sign_slip", Fraction(target + p * u, w)), ("not_divided", Fraction(target - p * u)), ("wrong_entry", Fraction(AB[1][0] - r * u, w))]
    steps = [("Entry in row 1, column 1 of AB", f"{p} x {u} + k x {w} = {target}"), ("Rearrange", f"{w}k = {target - p * u}"), ("Solve", f"k = {k}")]
    return _exact("unknown_in_product", q, Fraction(k), cands=cands, machine={"task": "unknown_in_product", "k": k}, steps=steps)


class MatrixMultiplicationGenerator(_FamilyGenerator):
    generator_id = MATRIX_MULT_ID
    version = 1
    levels = (1, 2, 3, 4)
    level_skills = MATRIX_MULT_LEVEL_SKILLS
    error_notes = MATRIX_MULT_ERROR_NOTES
    builders = {1: _matrix_mult_level1, 2: _matrix_mult_level2, 3: _matrix_mult_level3, 4: _matrix_mult_level4}


# ==========================================================================
# Lesson 15846: Determinants, Inverses, and Simultaneous Equations
# ==========================================================================

DETERMINANT_ERROR_NOTES: Dict[str, Dict[str, str]] = {
    "determinant": {
        "diagonals_added": "added the two products instead of subtracting them",
        "order_reversed": "subtracted in the wrong order (bc - ad)",
        "wrong_diagonal": "multiplied the entries of the wrong diagonals",
    },
    "inverse": {
        "signs_not_changed": "swapped the entries of the leading diagonal but did not change the signs of the other two",
        "not_divided": "wrote the adjugate matrix but did not divide by the determinant",
        "determinant_sign": "divided by the determinant with the wrong sign",
        "diagonal_not_swapped": "changed the signs of the other two entries but did not swap the leading diagonal",
    },
    "missing_element": {
        "sign_slip": "moved the product across with the wrong sign",
        "not_divided": "moved the product correctly but did not divide by the coefficient",
        "determinant_reversed": "used bc - ad instead of ad - bc",
    },
    "matrix_method": {
        "swapped_values": "found both values but gave x and y the wrong way round",
        "signs_both": "found the right sizes but with both signs wrong",
        "one_sign": "found the correct x but the wrong sign for y",
    },
    "singular_matrix": {
        "sign_slip": "found the right size of k but the wrong sign",
        "determinant_one": "made the determinant equal to 1 instead of 0",
    },
}

DETERMINANT_LEVEL_SKILLS: Dict[int, Tuple[str, ...]] = {
    1: ("determinant",),
    2: ("inverse",),
    3: ("missing_element",),
    4: ("matrix_method",),
    5: ("singular_matrix",),
}


def _det_matrix(rng: SeededRandom, low: int = -6, high: int = 6) -> Matrix:
    for _ in range(100):
        A = _rand_mat(rng, low, high)
        if _det(A) != 0:
            return A
    raise _Retry()


def _determinant_level1(rng: SeededRandom) -> _Built:
    A = _det_matrix(rng, -9, 9)
    a, b, c, d = A[0][0], A[0][1], A[1][0], A[1][1]
    D = _det(A)
    q = ''.join([format(_named('A', A), ''), '. Calculate the determinant of ', format(m_('\\mathbf{A}'), ''), '.'])
    cands = [("diagonals_added", a * d + b * c), ("order_reversed", b * c - a * d), ("wrong_diagonal", a * b - c * d)]
    steps = [("Multiply the leading diagonal", f"{a} x {d}"), ("Multiply the other diagonal", f"{b} x {c}"), ("Subtract", str(D))]
    return _exact("determinant", q, D, cands=[(c_, Fraction(v)) for c_, v in cands], machine={"task": "determinant", "A": _mat_typed(A)}, steps=steps)


def _determinant_level2(rng: SeededRandom) -> _Built:
    A = _det_matrix(rng, -5, 5)
    D = _det(A)
    _need(abs(D) <= 12)
    a, b, c, d = A[0][0], A[0][1], A[1][0], A[1][1]
    inv = _inverse(A)
    q = ''.join([format(_named('A', A), ''), '. Find ', format(m_('\\mathbf{A}^{-1}'), ''), ', the inverse of ', format(m_('\\mathbf{A}'), ''), '.'])
    adj = _mat(((d, -b), (-c, a)))
    cands = [("signs_not_changed", _mat_scale(Fraction(1) / D, _mat(((d, b), (c, a))))), ("not_divided", adj),
             ("determinant_sign", _mat_scale(Fraction(-1) / D, adj)), ("diagonal_not_swapped", _mat_scale(Fraction(1) / D, _mat(((a, -b), (-c, d)))))]
    display = rf"\frac{{1}}{{{D}}}{_mat_latex(adj)}" if D != 1 else _mat_latex(adj)
    steps = [("Determinant", str(D)), ("Swap the leading diagonal and change the other signs", _mat_typed(adj)), ("Divide by the determinant", _mat_typed(inv))]
    return _mat_answer("inverse", q, inv, cands, {"task": "inverse", "A": _mat_typed(A), "det": str(D)}, steps, display=display)


def _determinant_level3(rng: SeededRandom) -> _Built:
    a, b, c, d = (rng.randint(-6, 6) for _ in range(4))
    D = a * d - b * c
    which = rng.choice(("a", "b", "c", "d"))
    cells = {"a": a, "b": b, "c": c, "d": d}
    _need(D != 0 and cells[which] != 0)
    divisor = {"a": d, "b": c, "c": b, "d": a}[which]
    _need(divisor != 0)
    shown = {k: (v if k != which else None) for k, v in cells.items()}
    t = {k: ("x" if v is None else str(v)) for k, v in shown.items()}
    mat_txt = rf"\begin{{pmatrix}} {t['a']} & {t['b']} \\ {t['c']} & {t['d']} \end{{pmatrix}}"
    q = ''.join(['The matrix ', format(m_(''.join(['\\mathbf{M} = ', format(mat_txt, '')])), ''), ' has determinant ', format(D, ''), '. Find the value of ', format(m_('x'), ''), '.'])
    val = Fraction(cells[which])
    prod = {"a": b * c, "d": b * c, "b": a * d, "c": a * d}[which]
    if which in ("a", "d"):
        cands = [("sign_slip", Fraction(D - prod, divisor)), ("not_divided", Fraction(D + prod)), ("determinant_reversed", Fraction(-D + prod, divisor))]
        steps = [("Write the determinant equation", f"{'x' if which == 'a' else a} x {'x' if which == 'd' else d} - {b} x {c} = {D}"), ("Rearrange", f"{divisor}x = {D + prod}"), ("Solve", f"x = {_typed(val)}")]
    else:
        cands = [("sign_slip", Fraction(D - prod, divisor)), ("not_divided", Fraction(prod - D)), ("determinant_reversed", Fraction(D + prod, divisor))]
        steps = [("Write the determinant equation", f"{a} x {d} - {'x' if which == 'b' else b} x {'x' if which == 'c' else c} = {D}"), ("Rearrange", f"{divisor}x = {prod - D}"), ("Solve", f"x = {_typed(val)}")]
    return _exact("missing_element", q, val, cands=cands, machine={"task": "missing_element", "which": which, "cells": {k: v for k, v in cells.items()}, "det": D}, steps=steps)


def _determinant_level4(rng: SeededRandom) -> _Built:
    A = _det_matrix(rng, -5, 5)
    D = _det(A)
    _need(abs(D) <= 10 and all(v != 0 for row in A for v in row))
    x, y = rng.randint(-6, 6), rng.randint(-6, 6)
    _need(x != 0 and y != 0 and x != y)
    p = A[0][0] * x + A[0][1] * y
    r = A[1][0] * x + A[1][1] * y

    def eq(c1: Fraction, c2: Fraction, rhs: Fraction) -> str:
        c1, c2 = int(c1), int(c2)
        first = ("" if c1 == 1 else "-" if c1 == -1 else str(c1)) + "x"
        second = ("" if abs(c2) == 1 else str(abs(c2))) + "y"
        return f"{first} {'+' if c2 > 0 else '-'} {second} = {int(rhs)}"

    q = ("Use a matrix method to solve the simultaneous equations " f"{m_(eq(A[0][0], A[0][1], p))} and {m_(eq(A[1][0], A[1][1], r))}.")
    typed = f"x = {x} and y = {y}"
    cands = [("swapped_values", (y, x)), ("signs_both", (-x, -y)), ("one_sign", (x, -y))]
    items = [(c_, m_(rf"x = {wx},\ y = {wy}"), f"x = {wx} and y = {wy}", (wx, wy)) for c_, (wx, wy) in cands]
    inv = _inverse(A)
    steps = [("Write as a matrix equation", f"{_mat_typed(A)} (x; y) = ({p}; {r})"), ("Inverse of the matrix", _mat_typed(inv)), ("Multiply both sides by the inverse", f"(x; y) = ({x}; {y})")]
    return _Built("matrix_method", q, m_(rf"x = {x},\ y = {y}"), items, (x, y), {"task": "matrix_method", "A": _mat_typed(A), "rhs": [p, r], "x": x, "y": y}, steps,
                  {"answer_type": "equation_solution", "expected": [typed], "typed": typed})


def _determinant_level5(rng: SeededRandom) -> _Built:
    # (a b; c k) is singular when a k - b c = 0, so k = b c / a
    a, b, c = rng.randint(-5, 5), rng.randint(-5, 5), rng.randint(-5, 5)
    _need(a != 0 and b != 0 and c != 0 and (b * c) % a == 0)
    k = (b * c) // a
    _need(k != 0)
    shown = rf"\begin{{pmatrix}} {a} & {b} \\ {c} & k \end{{pmatrix}}"
    q = ''.join(['The matrix ', format(m_(''.join(['\\mathbf{N} = ', format(shown, '')])), ''), ' has no inverse. Find the value of ', format(m_('k'), ''), '.'])
    cands = [("sign_slip", Fraction(-k)), ("determinant_one", Fraction(b * c + 1, a))]
    steps = [("No inverse means the determinant is zero", f"{a}k - {b} x {c} = 0"), ("Rearrange", f"{a}k = {b * c}"), ("Solve", f"k = {k}")]
    return _exact("singular_matrix", q, Fraction(k), cands=cands, machine={"task": "singular_matrix", "a": a, "b": b, "c": c}, steps=steps)


class DeterminantsInversesGenerator(_FamilyGenerator):
    generator_id = DETERMINANT_ID
    version = 1
    levels = (1, 2, 3, 4, 5)
    level_skills = DETERMINANT_LEVEL_SKILLS
    error_notes = DETERMINANT_ERROR_NOTES
    builders = {1: _determinant_level1, 2: _determinant_level2, 3: _determinant_level3, 4: _determinant_level4, 5: _determinant_level5}


GENERATORS = [BearingsRightAngledGenerator(), ElevationExtendedRatiosGenerator(), SineCosineRulesGenerator(), VectorOperationsGenerator(),
              PositionVectorsGenerator(), TransformationsCoordinatesGenerator(), MatrixBasicsGenerator(), MatrixMultiplicationGenerator(),
              DeterminantsInversesGenerator()]
