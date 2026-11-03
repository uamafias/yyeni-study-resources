"""Generators for seven NSSCO Mathematics geometry and mensuration lessons.

* 15805 Perimeters and Areas of 2D Polygons   -> ``nssco_perimeters_areas_polygons``
* 15806 Circles, Arcs, and Sectors            -> ``nssco_circles_arcs_sectors``
* 15807 Surface Area and Volume of 3D Shapes  -> ``nssco_surface_area_volume``
* 15809 Similarity and Congruence (scale factors) -> ``nssco_similarity_scale_factors``
* 15811 Angle and Perpendicular Bisectors (numeric) -> ``nssco_bisectors_numeric``
* 15814 Angle Properties (Lines and Polygons) -> ``nssco_angles_lines_polygons``
* 15815 Angle Properties (Circles)            -> ``nssco_angles_circles``

Every question is written so that it can be answered without a drawn diagram: shapes
are fully described in words, and angle questions name their points and say which side
of a chord, line or arc each point lies on. Constructions and questions that depend on
a printed figure are not generated.

Levels follow the 2020-2024 papers: "Find / Calculate" parts worth 1-3 marks, answers to
3 significant figures unless "in terms of pi" or a whole number is natural, angles as
whole degrees, and the exam's own formulas stated in the question where the paper states
them (sphere volume, cone curved surface area).

Every problem is built backwards from its answer and recomputed before it is returned.
Distractors are the answers a learner gets from one specific, known mistake; any that
rounds to the correct answer is dropped. For circle and angle problems the reason for each
step is written into the model working (a judge marks reasons; the program marks the angle).

Money is not used here. Places and contexts are Namibian.
"""

from __future__ import annotations

import math as _math
import re
from decimal import Decimal, localcontext
from fractions import Fraction
from typing import Dict, List, Optional, Tuple

from .base import GeneratorError, SeededRandom
from .family_number import (
    _FamilyGenerator,
    _Retry,
    _Spec,
    _dec_str,
    _frac_str,
    _numeric_spec,
    _require,
)
from .formatting import math

PI = Fraction(Decimal("3.14159265358979323846264338327950288419716939937510582097494459"))

_PLACES = ("Windhoek", "Rundu", "Oshakati", "Swakopmund", "Keetmanshoop", "Walvis Bay", "Katima Mulilo", "Otjiwarongo")
_NAMES = ("Ndapewa", "Tuli", "Hileni", "Johannes", "Selma", "Petrus", "Kaleb", "Maria", "Aina", "Sakeus")


def _sqrt(n: int) -> Fraction:
    """Square root of a non-negative integer to about 55 digits (exact for perfect squares)."""
    root = _math.isqrt(n)
    if root * root == n:
        return Fraction(root)
    with localcontext() as ctx:
        ctx.prec = 60
        return Fraction(Decimal(n).sqrt())


def _sv(x) -> str:
    """Step value text: a terminating decimal, else a fraction."""
    x = Fraction(x)
    try:
        return _dec_str(x)
    except _Retry:
        return _frac_str(x)


def _m(x) -> str:
    return math(_sv(x))


def _deg(x) -> str:
    return math(f"{_sv(x)}^\\circ")


def _angle(name: str, value=None) -> str:
    """``angle $ABC = 56^\\circ$`` (or just ``angle $ABC$``)."""
    if value is None:
        return f"angle ${name}$"
    return f"angle ${name} = {_sv(value)}^\\circ$"


def _pi_typed(coef: Fraction) -> str:
    if coef.denominator == 1:
        return "pi" if coef == 1 else f"{coef.numerator}pi"
    return f"{coef.numerator}pi/{coef.denominator}"


def _pi_latex(coef: Fraction) -> str:
    if coef.denominator == 1:
        return "\\pi" if coef == 1 else f"{coef.numerator}\\pi"
    return f"\\frac{{{coef.numerator}}}{{{coef.denominator}}}\\pi"


def _pi_exact_spec(skill, question, coef, steps, dists, machine, *, suffix="") -> _Spec:
    """An answer 'in terms of pi': ``coef`` is the multiple of pi."""
    typed = _pi_typed(coef)
    dlist = [(code, math(_pi_latex(dc) + suffix), _pi_typed(dc), dc) for code, dc in dists]
    return _Spec(
        skill=skill,
        question=question,
        answer=math(_pi_latex(coef) + suffix),
        typed=typed,
        expected=[typed],
        answer_type="number_exact",
        correct_key=coef,
        steps=list(steps),
        dists=dlist,
        machine=dict(machine, answer=typed),
    )


def _pi_spec(skill, question, coef, steps, dists, machine, *, exact: bool, suffix="") -> _Spec:
    """A multiple of pi, asked either in terms of pi or to 3 significant figures."""
    if exact:
        return _pi_exact_spec(skill, question, coef, steps, dists, machine, suffix=suffix)
    spec = _numeric_spec(
        skill, question, coef * PI, steps, [(c, dc * PI) for c, dc in dists], machine,
        mode="sig_figs", digits=3, suffix=suffix,
    )
    spec.expected.append(_pi_typed(coef))
    return spec


_EXACT_NOTE = " Give your answer in terms of $\\pi$."
_SF3_NOTE = " Give your answer correct to 3 significant figures."


def _ask(exact: bool) -> str:
    return _EXACT_NOTE if exact else _SF3_NOTE


# ==========================================================================
# 15805 Perimeters and Areas of 2D Polygons
# ==========================================================================

AREA_NOTES: Dict[str, Dict[str, str]] = {
    "area_perimeter_basic": {
        "perimeter_for_area": "worked out the perimeter when the area was asked for",
        "area_for_perimeter": "worked out the area when the perimeter was asked for",
        "added_two_sides": "added the length and the width once instead of doubling the sum for the perimeter",
        "forgot_half": "used base times height for a triangle and did not halve it",
        "used_slant_side": "multiplied the base by the slant side instead of the perpendicular height",
        "treated_as_triangle": "halved base times height, as for a triangle, for a parallelogram",
    },
    "trapezium": {
        "forgot_half": "added the parallel sides and multiplied by the height but did not halve",
        "used_one_parallel_side": "used only one of the parallel sides in the formula",
        "forgot_to_double": "divided the area by the sum of the parallel sides without doubling it first",
        "divided_by_one_side": "divided twice the area by one parallel side instead of by their sum",
    },
    "right_triangle_perimeter": {
        "hypotenuse_added": "used the sum of the two short sides as the third side",
        "hypotenuse_subtracted": "subtracted the squares instead of adding them when using Pythagoras",
        "area_not_perimeter": "worked out the area of the triangle instead of the perimeter",
        "missing_hypotenuse": "added the two short sides and forgot the longest side",
    },
    "composite_area": {
        "forgot_half": "used base times height for the triangle and did not halve it",
        "rectangle_only": "found the area of the rectangle and left out the triangle",
        "triangle_only": "found the area of the triangle and left out the rectangle",
    },
    "circle_in_square": {
        "circle_area": "gave the area of the circle instead of the area left over",
        "square_area": "gave the area of the whole square",
        "halved_region": "took half of the area that is left over",
        "diagonal_squared": "squared the diagonal (the diameter) and forgot to halve it",
        "radius_squared": "used the radius as the side of the square",
        "square_only": "gave the area of the square instead of the area between the circle and the square",
        "circle_minus_r_squared": "subtracted only radius squared for the square",
    },
}

AREA_LEVEL_SKILLS: Dict[int, Tuple[str, ...]] = {
    1: ("area_perimeter_basic",),
    2: ("trapezium",),
    3: ("right_triangle_perimeter", "composite_area"),
    4: ("circle_in_square",),
}


def _area_l1(rng: SeededRandom) -> _Spec:
    kind = rng.choice(("rect_area", "rect_perimeter", "triangle", "parallelogram"))
    place = rng.choice(_PLACES)
    skill = "area_perimeter_basic"
    if kind in ("rect_area", "rect_perimeter"):
        length = rng.randint(6, 40)
        width = rng.randint(3, length - 1)
        thing = rng.choice(("field", "vegetable garden", "school playground", "plot of land"))
        shape = f"A rectangular {thing} in {place} is {_m(length)} m long and {_m(width)} m wide."
        if kind == "rect_area":
            value = length * width
            q = f"{shape} Calculate the area of the {thing}."
            steps = [("Multiply the length by the width", _sv(value))]
            dists = [("perimeter_for_area", 2 * (length + width)), ("added_two_sides", length + width)]
        else:
            value = 2 * (length + width)
            q = f"{shape} Calculate the perimeter of the {thing}."
            steps = [("Add the length and the width", _sv(length + width)), ("Double the sum", _sv(value))]
            dists = [("area_for_perimeter", length * width), ("added_two_sides", length + width)]
        machine = {"task": kind, "length": length, "width": width}
    elif kind == "triangle":
        base, height = rng.randint(5, 30), rng.randint(4, 24)
        value = Fraction(base * height, 2)
        q = (f"A triangular sail has a base of {_m(base)} cm and a perpendicular height of {_m(height)} cm. "
             "Find the area of the sail.")
        steps = [("Multiply base by height", _sv(base * height)), ("Halve the product", _sv(value))]
        dists = [("forgot_half", base * height)]
        machine = {"task": "triangle_area", "base": base, "height": height}
    else:
        base, height = rng.randint(6, 30), rng.randint(4, 20)
        slant = height + rng.randint(1, 6)
        value = base * height
        q = (f"A parallelogram has a base of {_m(base)} cm, a slant side of {_m(slant)} cm and a perpendicular "
             f"height of {_m(height)} cm. Calculate the area of the parallelogram.")
        steps = [("Multiply the base by the perpendicular height", _sv(value))]
        dists = [("used_slant_side", base * slant), ("treated_as_triangle", Fraction(base * height, 2))]
        machine = {"task": "parallelogram_area", "base": base, "height": height, "slant": slant}
    return _numeric_spec(skill, q, Fraction(value), steps, [(c, Fraction(v)) for c, v in dists], machine)


def _area_l2(rng: SeededRandom) -> _Spec:
    a = rng.randint(3, 14)
    b = a + rng.randint(2, 10)
    h = rng.randint(3, 16)
    if (a + b) * h % 2:
        raise _Retry
    if rng.chance(1, 3):
        area = Fraction((a + b) * h, 2)
        q = (f"A trapezium has parallel sides of {_m(a)} cm and {_m(b)} cm and an area of {_m(area)} cm$^2$. "
             "Find the perpendicular distance between the parallel sides.")
        steps = [("Double the area", _sv(2 * area)), ("Divide by the sum of the parallel sides", _sv(h))]
        dists = [("forgot_to_double", area / (a + b)), ("divided_by_one_side", 2 * area / b)]
        return _numeric_spec("trapezium", q, Fraction(h), steps, dists,
                             {"task": "trapezium_height", "a": a, "b": b, "area": str(area)})
    value = Fraction((a + b) * h, 2)
    q = (f"A trapezium has parallel sides of {_m(a)} cm and {_m(b)} cm. The perpendicular distance between "
         f"the parallel sides is {_m(h)} cm. Find the area of the trapezium.")
    steps = [("Add the parallel sides", _sv(a + b)), ("Multiply by the height", _sv((a + b) * h)), ("Halve", _sv(value))]
    dists = [("forgot_half", Fraction((a + b) * h)), ("used_one_parallel_side", Fraction(b * h, 2))]
    return _numeric_spec("trapezium", q, value, steps, dists, {"task": "trapezium_area", "a": a, "b": b, "h": h})


_TRIPLES = ((3, 4, 5), (5, 12, 13), (6, 8, 10), (8, 15, 17), (9, 12, 15), (7, 24, 25), (12, 16, 20), (20, 21, 29))
_TRIANGLE_LABELS = ("MDC", "PQR", "XYZ", "ABC", "KLN")


def _area_l3(rng: SeededRandom) -> _Spec:
    if rng.chance(1, 2):
        label = rng.choice(_TRIANGLE_LABELS)
        if rng.chance(2, 5):
            a, b, _ = rng.choice(_TRIPLES)
            if rng.chance(1, 2):
                a, b = b, a
        else:
            a, b = rng.randint(3, 16), rng.randint(3, 16)
        c2 = a * a + b * b
        hyp = _sqrt(c2)
        exact = hyp.denominator == 1
        value = a + b + hyp
        q = (f"Triangle ${label}$ has a right angle at ${label[1]}$. ${label[:2]}$ = {_m(a)} cm and "
             f"${label[1:]}$ = {_m(b)} cm. Calculate the perimeter of triangle ${label}$.")
        dists = [("hypotenuse_added", Fraction(2 * (a + b))), ("area_not_perimeter", Fraction(a * b, 2)), ("missing_hypotenuse", Fraction(a + b))]
        if a != b:
            dists.append(("hypotenuse_subtracted", a + b + _sqrt(abs(a * a - b * b))))
        steps = [("Use Pythagoras: sum of the squares of the short sides", _sv(c2)),
                 ("Square root to find the longest side", _sv(hyp) if exact else f"{float(hyp):.4f}"),
                 ("Add the three sides", _sv(value) if exact else f"{float(value):.4f}")]
        machine = {"task": "right_triangle_perimeter", "a": a, "b": b}
        if exact:
            return _numeric_spec("right_triangle_perimeter", q, value, steps, dists, machine)
        return _numeric_spec("right_triangle_perimeter", q + _SF3_NOTE, value, steps, dists, machine, mode="sig_figs", digits=3)
    a, b = rng.randint(4, 20), rng.randint(3, 15)
    c, h = rng.randint(3, 14), rng.randint(3, 14)
    if (c * h) % 2:
        raise _Retry
    tri = Fraction(c * h, 2)
    value = a * b + tri
    q = (f"A plot of land is made from a rectangle {_m(a)} m by {_m(b)} m and a right-angled triangle that is "
         f"joined to one side of the rectangle. The triangle has a base of {_m(c)} m and a perpendicular height of "
         f"{_m(h)} m. Calculate the total area of the plot.")
    steps = [("Area of the rectangle", _sv(a * b)), ("Area of the triangle", _sv(tri)), ("Add the two areas", _sv(value))]
    dists = [("forgot_half", Fraction(a * b + c * h)), ("rectangle_only", Fraction(a * b)), ("triangle_only", tri)]
    return _numeric_spec("composite_area", q, Fraction(value), steps, dists, {"task": "composite_area", "a": a, "b": b, "c": c, "h": h})


def _area_l4(rng: SeededRandom) -> _Spec:
    r = rng.randint(3, 15)
    kind = rng.choice(("left_over", "square_in_circle", "ring_square"))
    skill = "circle_in_square"
    if kind == "left_over":
        value = 4 * r * r - PI * r * r
        q = (f"A circle of radius {_m(r)} cm is drawn inside a square so that the circle touches all four sides of "
             f"the square. Calculate the area of the square that is not covered by the circle.{_SF3_NOTE}")
        steps = [("Side of the square is the diameter", _sv(2 * r)), ("Area of the square", _sv(4 * r * r)),
                 ("Area of the circle in terms of pi", _pi_typed(Fraction(r * r))), ("Subtract", f"{float(value):.4f}")]
        dists = [("circle_area", PI * r * r), ("square_area", Fraction(4 * r * r)), ("halved_region", value / 2)]
        return _numeric_spec(skill, q, value, steps, dists, {"task": "left_over", "r": r}, mode="sig_figs", digits=3)
    if kind == "square_in_circle":
        value = Fraction(2 * r * r)
        q = (f"A square is drawn inside a circle of radius {_m(r)} cm so that all four corners of the square lie on "
             "the circle. Find the area of the square.")
        steps = [("The diagonal of the square is the diameter", _sv(2 * r)), ("Area of a square from its diagonal d is d squared over 2", _sv(value))]
        dists = [("diagonal_squared", Fraction(4 * r * r)), ("radius_squared", Fraction(r * r)), ("circle_area", PI * r * r)]
        return _numeric_spec(skill, q, value, steps, dists, {"task": "square_in_circle", "r": r})
    value = PI * r * r - 2 * r * r
    q = (f"A square is drawn inside a circle of radius {_m(r)} cm so that all four corners of the square lie on the "
         f"circle. Calculate the area of the circle that is outside the square.{_SF3_NOTE}")
    steps = [("Area of the circle in terms of pi", _pi_typed(Fraction(r * r))), ("Area of the square", _sv(2 * r * r)),
             ("Subtract", f"{float(value):.4f}")]
    dists = [("circle_area", PI * r * r), ("square_only", Fraction(2 * r * r)), ("circle_minus_r_squared", PI * r * r - r * r)]
    return _numeric_spec(skill, q, value, steps, dists, {"task": "circle_outside_square", "r": r}, mode="sig_figs", digits=3)


class PerimetersAreasGenerator(_FamilyGenerator):
    generator_id = "nssco_perimeters_areas_polygons"
    version = 1
    levels = (1, 2, 3, 4)
    level_skills = AREA_LEVEL_SKILLS
    error_notes = AREA_NOTES
    builders = {1: _area_l1, 2: _area_l2, 3: _area_l3, 4: _area_l4}


# ==========================================================================
# 15806 Circles, Arcs, and Sectors
# ==========================================================================

CIRCLE_NOTES: Dict[str, Dict[str, str]] = {
    "circle_basic": {
        "diameter_as_radius": "used the diameter where the radius belongs in the formula",
        "radius_as_diameter": "used the radius where the diameter belongs in the formula",
        "swapped_formulas": "used the area formula for the circumference, or the circumference formula for the area",
        "forgot_to_square": "did not square the radius in the area formula",
    },
    "sector_arc_area": {
        "swapped_formulas": "used the sector area formula for the arc length, or the arc length formula for the area",
        "divided_by_180": "divided the angle by 180 instead of 360",
        "diameter_as_radius": "used the diameter where the radius belongs in the formula",
        "forgot_to_square": "did not square the radius in the sector area formula",
    },
    "circle_inverse": {
        "used_diameter": "gave the diameter instead of the radius",
        "forgot_square_root": "did not take the square root after dividing by pi",
        "divided_by_two": "divided the given number by two instead of taking the square root",
        "missing_factor_two": "left the 2 out of the arc length formula",
        "used_area_formula": "used the sector area formula in place of the arc length formula",
        "used_arc_formula": "used the arc length formula in place of the sector area formula",
        "halved": "halved the radius",
        "diameter_as_radius": "used the diameter where the radius belongs in the formula",
    },
    "sector_perimeter": {
        "arc_only": "gave the arc length and left out the two straight edges",
        "one_radius": "added one radius to the arc length instead of two",
        "area_for_perimeter": "worked out the area of the sector instead of its perimeter",
    },
    "segment_area": {
        "whole_region": "gave the whole region between the circle and the square instead of one segment",
        "quarter_circle": "used a quarter of the circle instead of subtracting the triangle",
        "sector_only": "gave the area of the sector and did not subtract the triangle",
        "triangle_only": "gave the area of the triangle instead of the segment",
        "triangle_added": "added the area of the triangle to the sector instead of subtracting",
        "difference_of_radii": "squared the difference of the radii instead of subtracting the squares",
        "outer_only": "gave the area of the larger circle",
        "calculator_in_radians": "used a calculator in the wrong angle mode for the triangle",
    },
    "ring_area": {
        "difference_of_radii": "squared the difference of the radii instead of subtracting the squares",
        "outer_only": "gave the area of the larger circle",
        "inner_only": "gave the area of the smaller circle",
    },
}

CIRCLE_LEVEL_SKILLS: Dict[int, Tuple[str, ...]] = {
    1: ("circle_basic",),
    2: ("sector_arc_area",),
    3: ("circle_inverse",),
    4: ("sector_perimeter", "segment_area"),
    5: ("segment_area", "ring_area"),
}

_SECTOR_ANGLES = (20, 30, 36, 40, 45, 60, 72, 90, 120, 135, 150, 180, 240)


def _circle_l1(rng: SeededRandom) -> _Spec:
    what = rng.choice(("circumference", "area"))
    use_diameter = rng.chance(1, 2)
    exact = rng.chance(1, 2)
    r = rng.randint(2, 15)
    given = f"a diameter of {_m(2 * r)} cm" if use_diameter else f"a radius of {_m(r)} cm"
    thing = rng.choice(("circular pond", "circular table top", "round garden", "circular water tank"))
    q = f"A {thing} has {given}. Calculate the {what} of the {thing}.{_ask(exact)}"
    if what == "circumference":
        coef = Fraction(2 * r)
        steps = [("Use circumference = 2 pi r (or pi d)", _pi_typed(coef))]
        dists = [("swapped_formulas", Fraction(r * r))]
        dists.append(("diameter_as_radius", Fraction(4 * r)) if use_diameter else ("radius_as_diameter", Fraction(r)))
    else:
        coef = Fraction(r * r)
        steps = [("Find the radius", _sv(r)), ("Use area = pi r squared", _pi_typed(coef))]
        dists = [("swapped_formulas", Fraction(2 * r)), ("forgot_to_square", Fraction(r))]
        if use_diameter:
            dists.append(("diameter_as_radius", Fraction(4 * r * r)))
    return _pi_spec("circle_basic", q, coef, steps, dists, {"task": what, "r": r, "given_diameter": use_diameter}, exact=exact)


def _circle_l2(rng: SeededRandom) -> _Spec:
    theta = rng.choice(_SECTOR_ANGLES)
    r = rng.randint(3, 20)
    what = rng.choice(("arc", "area"))
    exact = rng.chance(1, 3)
    share = Fraction(theta, 360)
    shape = f"A sector of a circle has an angle of {_deg(theta)} at the centre and a radius of {_m(r)} cm."
    if what == "arc":
        q = f"{shape} Calculate the length of the arc of the sector.{_ask(exact)}"
        coef = share * 2 * r
        steps = [("Fraction of the circle", _frac_str(share)), ("Arc length = fraction x 2 pi r", _pi_typed(coef))]
        dists = [("swapped_formulas", share * r * r), ("divided_by_180", Fraction(theta, 180) * 2 * r), ("diameter_as_radius", share * 4 * r)]
    else:
        q = f"{shape} Calculate the area of the sector.{_ask(exact)}"
        coef = share * r * r
        steps = [("Fraction of the circle", _frac_str(share)), ("Sector area = fraction x pi r squared", _pi_typed(coef))]
        dists = [("swapped_formulas", share * 2 * r), ("divided_by_180", Fraction(theta, 180) * r * r), ("forgot_to_square", share * r)]
    return _pi_spec("sector_arc_area", q, coef, steps, dists, {"task": f"sector_{what}", "theta": theta, "r": r}, exact=exact)


def _circle_l3(rng: SeededRandom) -> _Spec:
    kind = rng.choice(("radius_from_circumference", "radius_from_area", "angle_from_arc", "angle_from_area"))
    skill = "circle_inverse"
    if kind == "radius_from_circumference":
        r = rng.randint(3, 25)
        q = f"The circumference of a circle is ${2 * r}\\pi$ cm. Find the radius of the circle."
        steps = [("Divide the circumference by 2 pi", _sv(r))]
        return _numeric_spec(skill, q, Fraction(r), steps, [("used_diameter", Fraction(2 * r)), ("halved", Fraction(r, 2))],
                             {"task": kind, "r": r})
    if kind == "radius_from_area":
        r = rng.randint(3, 25)
        q = f"The area of a circle is ${r * r}\\pi$ cm$^2$. Find the radius of the circle."
        steps = [("Divide the area by pi to get the radius squared", _sv(r * r)), ("Take the square root", _sv(r))]
        return _numeric_spec(skill, q, Fraction(r), steps,
                             [("forgot_square_root", Fraction(r * r)), ("divided_by_two", Fraction(r * r, 2))], {"task": kind, "r": r})
    theta = rng.choice(_SECTOR_ANGLES[:-1])
    r = rng.randint(3, 18)
    if kind == "angle_from_arc":
        coef = Fraction(theta * 2 * r, 360)
        _dec_str(coef)
        q = (f"A sector of a circle has a radius of {_m(r)} cm. The length of its arc is ${_sv(coef)}\\pi$ cm. "
             "Calculate the angle of the sector at the centre.")
        steps = [("Arc length = angle over 360 x 2 pi r, so angle over 360", _frac_str(Fraction(theta, 360))), ("Multiply by 360", _sv(theta))]
        dists = [("missing_factor_two", Fraction(2 * theta)), ("used_area_formula", Fraction(360) * coef / (r * r))]
        return _numeric_spec(skill, q, Fraction(theta), steps, dists, {"task": kind, "theta": theta, "r": r})
    coef = Fraction(theta * r * r, 360)
    _dec_str(coef)
    q = (f"A sector of a circle has a radius of {_m(r)} cm. The area of the sector is ${_sv(coef)}\\pi$ cm$^2$. "
         "Calculate the angle of the sector at the centre.")
    steps = [("Sector area = angle over 360 x pi r squared, so angle over 360", _frac_str(Fraction(theta, 360))), ("Multiply by 360", _sv(theta))]
    dists = [("used_arc_formula", Fraction(360) * coef / (2 * r)), ("diameter_as_radius", Fraction(360) * coef / (4 * r * r))]
    return _numeric_spec(skill, q, Fraction(theta), steps, dists, {"task": kind, "theta": theta, "r": r})


def _sin_deg(theta: int) -> Fraction:
    return {30: Fraction(1, 2), 60: _sqrt(3) / 2, 90: Fraction(1), 120: _sqrt(3) / 2, 150: Fraction(1, 2)}[theta]


def _circle_l4(rng: SeededRandom) -> _Spec:
    kind = rng.choice(("sector_perimeter", "segment_square"))
    r = rng.randint(3, 16)
    if kind == "sector_perimeter":
        theta = rng.choice((30, 40, 45, 60, 72, 90, 120, 135, 150))
        arc = Fraction(theta, 360) * 2 * r * PI
        value = arc + 2 * r
        q = (f"A sector of a circle has an angle of {_deg(theta)} at the centre and a radius of {_m(r)} cm. "
             f"Calculate the perimeter of the sector.{_SF3_NOTE}")
        steps = [("Arc length", f"{float(arc):.4f}"), ("Add the two radii", _sv(2 * r)), ("Perimeter", f"{float(value):.4f}")]
        dists = [("arc_only", arc), ("one_radius", arc + r), ("area_for_perimeter", Fraction(theta, 360) * r * r * PI)]
        return _numeric_spec("sector_perimeter", q, value, steps, dists, {"task": kind, "theta": theta, "r": r}, mode="sig_figs", digits=3)
    value = (PI * r * r - 2 * r * r) / 4
    q = (f"A square is drawn inside a circle of radius {_m(r)} cm so that all four corners of the square lie on the "
         f"circle. The square divides the part of the circle outside it into four equal segments. Calculate the area "
         f"of one segment.{_SF3_NOTE}")
    steps = [("Area of the circle", _pi_typed(Fraction(r * r))), ("Area of the square", _sv(2 * r * r)),
             ("Area outside the square", f"{float(PI * r * r - 2 * r * r):.4f}"), ("Divide by 4", f"{float(value):.4f}")]
    dists = [("whole_region", PI * r * r - 2 * r * r), ("quarter_circle", PI * r * r / 4)]
    return _numeric_spec("segment_area", q, value, steps, dists, {"task": kind, "r": r}, mode="sig_figs", digits=3)


def _circle_l5(rng: SeededRandom) -> _Spec:
    if rng.chance(1, 2):
        theta = rng.choice((60, 90, 120))
        r = rng.randint(4, 16)
        sector = Fraction(theta, 360) * PI * r * r
        tri = Fraction(r * r, 2) * _sin_deg(theta)
        value = sector - tri
        q = (f"A chord $AB$ of a circle with centre $O$ and radius {_m(r)} cm makes an angle of {_deg(theta)} at $O$. "
             f"Calculate the area of the segment between the chord $AB$ and the minor arc $AB$.{_SF3_NOTE}")
        steps = [("Area of sector OAB", f"{float(sector):.4f}"), ("Area of triangle OAB = half r squared sin of the angle", f"{float(tri):.4f}"),
                 ("Subtract", f"{float(value):.4f}")]
        dists = [("sector_only", sector), ("triangle_only", tri), ("triangle_added", sector + tri)]
        return _numeric_spec("segment_area", q, value, steps, dists, {"task": "segment_chord", "theta": theta, "r": r}, mode="sig_figs", digits=3)
    big = rng.randint(6, 20)
    small = rng.randint(2, big - 2)
    coef = Fraction(big * big - small * small)
    exact = rng.chance(1, 2)
    q = (f"Two circles have the same centre. The smaller circle has a radius of {_m(small)} cm and the larger circle has a "
         f"radius of {_m(big)} cm. Calculate the area of the ring between the two circles.{_ask(exact)}")
    steps = [("Area of the larger circle", _pi_typed(Fraction(big * big))), ("Area of the smaller circle", _pi_typed(Fraction(small * small))),
             ("Subtract", _pi_typed(coef))]
    dists = [("difference_of_radii", Fraction((big - small) ** 2)), ("outer_only", Fraction(big * big)), ("inner_only", Fraction(small * small))]
    return _pi_spec("ring_area", q, coef, steps, dists, {"task": "ring", "big": big, "small": small}, exact=exact)


class CirclesArcsSectorsGenerator(_FamilyGenerator):
    generator_id = "nssco_circles_arcs_sectors"
    version = 1
    levels = (1, 2, 3, 4, 5)
    level_skills = CIRCLE_LEVEL_SKILLS
    error_notes = CIRCLE_NOTES
    builders = {1: _circle_l1, 2: _circle_l2, 3: _circle_l3, 4: _circle_l4, 5: _circle_l5}


# ==========================================================================
# 15807 Surface Area and Volume of 3D Shapes
# ==========================================================================

SOLID_NOTES: Dict[str, Dict[str, str]] = {
    "cuboid_cylinder_basic": {
        "volume_for_area": "worked out the volume when the surface area was asked for",
        "area_for_volume": "worked out a surface area when the volume was asked for",
        "missing_double": "left out the doubling when adding the three pairs of faces",
        "diameter_as_radius": "used the diameter where the radius belongs in the formula",
        "forgot_to_square": "did not square the radius in the volume formula",
        "added_dimensions": "added the dimensions instead of multiplying them",
    },
    "volume_formulas": {
        "forgot_third": "left out the one third in the formula",
        "diameter_as_radius": "used the diameter where the radius belongs in the formula",
        "forgot_to_halve": "gave the volume of the whole sphere instead of the hemisphere",
        "forgot_to_cube": "squared the radius instead of cubing it",
        "slant_for_height": "used the slant height where the vertical height belongs",
        "forgot_to_square": "did not square the radius",
    },
    "curved_surface_area": {
        "height_for_slant": "used the vertical height where the slant height belongs",
        "added_base": "added the area of the circular base to the curved surface",
        "cylinder_formula": "used the cylinder formula 2 pi r h for the cone",
        "diameter_as_radius": "used the diameter where the radius belongs in the formula",
        "forgot_two": "left the 2 out of the curved surface area formula",
        "half_missing": "did not halve for a hemisphere",
    },
    "composite_volume": {
        "forgot_hemisphere": "found the volume of the cylinder only",
        "full_sphere": "used a whole sphere instead of a hemisphere",
        "forgot_half": "gave the volume of the whole cylinder instead of the half cylinder",
        "cylinder_height_total": "used the total height as the height of the cylinder",
        "diameter_as_radius": "used the diameter where the radius belongs in the formula",
    },
    "solid_inverse": {
        "forgot_to_divide_by_r_squared": "divided the volume by pi only and forgot to divide by the radius squared",
        "diameter_as_radius": "used the diameter where the radius belongs in the formula",
        "no_conversion": "did not convert cubic metres to litres",
        "wrong_conversion": "converted using 100 instead of 1000",
        "base_included": "included the area of the circular base in the curved surface area",
        "sphere_for_hemisphere": "used the whole sphere's surface area for the hemisphere",
        "forgot_hemisphere": "left out the curved surface of the hemisphere",
        "r_not_halved": "did not halve the diameter to find the radius",
    },
}

SOLID_LEVEL_SKILLS: Dict[int, Tuple[str, ...]] = {
    1: ("cuboid_cylinder_basic",),
    2: ("volume_formulas",),
    3: ("curved_surface_area",),
    4: ("composite_volume",),
    5: ("solid_inverse",),
}

_SPHERE_FORMULA = "The volume of a sphere of radius $r$ is $\\frac{4}{3}\\pi r^3$."
_CONE_FORMULA = "The volume of a cone with base radius $r$ and height $h$ is $\\frac{1}{3}\\pi r^2 h$."
_CSA_FORMULA = "The curved surface area of a cone with base radius $r$ and slant height $l$ is $\\pi r l$."
_PYRAMID_FORMULA = "The volume of a pyramid is $\\frac{1}{3} \\times$ base area $\\times$ height."


def _solid_l1(rng: SeededRandom) -> _Spec:
    kind = rng.choice(("cuboid_volume", "cuboid_area", "cylinder_volume"))
    skill = "cuboid_cylinder_basic"
    if kind in ("cuboid_volume", "cuboid_area"):
        l, w, h = rng.randint(4, 20), rng.randint(3, 14), rng.randint(2, 12)
        solid = rng.choice(("water tank", "wooden box", "classroom cupboard", "concrete block"))
        shape = f"A {solid} is a cuboid measuring {_m(l)} cm by {_m(w)} cm by {_m(h)} cm."
        if kind == "cuboid_volume":
            value = l * w * h
            q = f"{shape} Calculate the volume of the {solid}."
            steps = [("Multiply length, width and height", _sv(value))]
            dists = [("area_for_volume", 2 * (l * w + l * h + w * h)), ("added_dimensions", l + w + h)]
        else:
            value = 2 * (l * w + l * h + w * h)
            q = f"{shape} Calculate the total surface area of the {solid}."
            steps = [("Add the areas of the three different faces", _sv(l * w + l * h + w * h)), ("Double", _sv(value))]
            dists = [("volume_for_area", l * w * h), ("missing_double", l * w + l * h + w * h)]
        return _numeric_spec(skill, q, Fraction(value), steps, [(c, Fraction(v)) for c, v in dists], {"task": kind, "l": l, "w": w, "h": h})
    r, h = rng.randint(2, 12), rng.randint(3, 20)
    exact = rng.chance(1, 2)
    coef = Fraction(r * r * h)
    q = (f"A cylindrical water tank has a radius of {_m(r)} cm and a height of {_m(h)} cm. "
         f"Calculate the volume of the tank.{_ask(exact)}")
    steps = [("Area of the circular base", _pi_typed(Fraction(r * r))), ("Multiply by the height", _pi_typed(coef))]
    dists = [("diameter_as_radius", Fraction(4 * r * r * h)), ("forgot_to_square", Fraction(r * h))]
    return _pi_spec(skill, q, coef, steps, dists, {"task": kind, "r": r, "h": h}, exact=exact)


def _solid_l2(rng: SeededRandom) -> _Spec:
    kind = rng.choice(("sphere", "hemisphere", "cone", "pyramid"))
    skill = "volume_formulas"
    r = rng.randint(2, 12)
    if kind in ("sphere", "hemisphere"):
        if kind == "sphere":
            coef = Fraction(4 * r**3, 3)
            q = f"{_SPHERE_FORMULA} A solid metal sphere has a radius of {_m(r)} cm. Calculate its volume."
            dists = [("forgot_to_cube", Fraction(4 * r * r, 3)), ("diameter_as_radius", Fraction(32 * r**3, 3))]
        else:
            coef = Fraction(2 * r**3, 3)
            q = f"{_SPHERE_FORMULA} A solid hemisphere has a radius of {_m(r)} cm. Calculate its volume."
            dists = [("forgot_to_halve", Fraction(4 * r**3, 3)), ("diameter_as_radius", Fraction(16 * r**3, 3))]
        steps = [("Substitute into the formula (for a hemisphere take half of the sphere)", _pi_typed(coef))]
        return _pi_spec(skill, q + _SF3_NOTE, coef, steps, dists, {"task": kind, "r": r}, exact=False)
    h = rng.randint(3, 18)
    if kind == "cone":
        coef = Fraction(r * r * h, 3)
        q = (f"{_CONE_FORMULA} A cone has a base radius of {_m(r)} cm and a height of {_m(h)} cm. Calculate its volume.")
        steps = [("Substitute into one third pi r squared h", _pi_typed(coef))]
        dists = [("forgot_third", Fraction(r * r * h)), ("diameter_as_radius", Fraction(4 * r * r * h, 3)), ("forgot_to_square", Fraction(r * h, 3))]
        return _pi_spec(skill, q + _SF3_NOTE, coef, steps, dists, {"task": kind, "r": r, "h": h}, exact=False)
    s = rng.randint(3, 15)
    if (s * s * h) % 3:
        raise _Retry
    value = Fraction(s * s * h, 3)
    q = (f"{_PYRAMID_FORMULA} A pyramid has a square base of side {_m(s)} cm and a vertical height of {_m(h)} cm. "
         "Calculate its volume.")
    steps = [("Area of the base", _sv(s * s)), ("Multiply by the height", _sv(s * s * h)), ("Take one third", _sv(value))]
    dists = [("forgot_third", Fraction(s * s * h)), ("forgot_to_square", Fraction(s * h, 3))]
    return _numeric_spec(skill, q, value, steps, [(c, Fraction(v)) for c, v in dists], {"task": kind, "s": s, "h": h})


_CONE_TRIPLES = ((3, 4, 5), (5, 12, 13), (6, 8, 10), (8, 6, 10), (9, 12, 15), (8, 15, 17), (12, 5, 13), (7, 24, 25))


def _solid_l3(rng: SeededRandom) -> _Spec:
    skill = "curved_surface_area"
    exact = rng.chance(1, 2)
    kind = rng.choice(("cone_slant", "cone_height", "cylinder"))
    if kind == "cylinder":
        r, h = rng.randint(2, 12), rng.randint(3, 20)
        coef = Fraction(2 * r * h)
        q = (f"A cylindrical pipe has a radius of {_m(r)} cm and a length of {_m(h)} cm. Calculate the curved surface area "
             f"of the pipe (do not include the ends).{_ask(exact)}")
        steps = [("Curved surface area = 2 pi r h", _pi_typed(coef))]
        dists = [("forgot_two", Fraction(r * h)), ("added_base", Fraction(2 * r * h + r * r)), ("diameter_as_radius", Fraction(4 * r * h))]
        return _pi_spec(skill, q, coef, steps, dists, {"task": kind, "r": r, "h": h}, exact=exact)
    r, h, l = rng.choice(_CONE_TRIPLES)
    coef = Fraction(r * l)
    if kind == "cone_slant":
        q = (f"{_CSA_FORMULA} A cone has a base radius of {_m(r)} cm and a slant height of {_m(l)} cm. Calculate the "
             f"curved surface area of the cone.{_ask(exact)}")
        steps = [("Substitute into pi r l", _pi_typed(coef))]
    else:
        q = (f"{_CSA_FORMULA} A cone has a base radius of {_m(r)} cm and a vertical height of {_m(h)} cm. Calculate the "
             f"curved surface area of the cone.{_ask(exact)}")
        steps = [("Find the slant height by Pythagoras", _sv(l)), ("Substitute into pi r l", _pi_typed(coef))]
    dists = [("height_for_slant", Fraction(r * h)), ("added_base", Fraction(r * l + r * r)), ("cylinder_formula", Fraction(2 * r * h))]
    return _pi_spec(skill, q, coef, steps, dists, {"task": kind, "r": r, "h": h, "l": l}, exact=exact)


def _solid_l4(rng: SeededRandom) -> _Spec:
    skill = "composite_volume"
    r = rng.randint(2, 10)
    if rng.chance(1, 3):
        length = rng.randint(5, 30)
        coef = Fraction(r * r * length, 2)
        q = (f"A water trough is in the shape of a half-cylinder. The semicircular ends have a radius of {_m(r)} cm and the "
             f"trough is {_m(length)} cm long. Calculate the volume of water the trough holds when it is full.{_SF3_NOTE}")
        steps = [("Volume of a whole cylinder", _pi_typed(Fraction(r * r * length))), ("Halve", _pi_typed(coef))]
        dists = [("forgot_half", Fraction(r * r * length)), ("diameter_as_radius", Fraction(4 * r * r * length, 2))]
        return _pi_spec(skill, q, coef, steps, dists, {"task": "half_cylinder", "r": r, "length": length}, exact=False)
    h = rng.randint(3, 16)
    cyl = Fraction(r * r * h)
    hemi = Fraction(2 * r**3, 3)
    coef = cyl + hemi
    total = h + r
    thing = rng.choice(("grain silo", "water tower", "storage tank"))
    q = (f"{_SPHERE_FORMULA} A {thing} is made from a cylinder with a hemisphere on top. Both have a radius of {_m(r)} m. "
         f"The cylinder is {_m(h)} m high. Calculate the total volume of the {thing}.{_SF3_NOTE}")
    steps = [("Volume of the cylinder", _pi_typed(cyl)), ("Volume of the hemisphere", _pi_typed(hemi)), ("Add", _pi_typed(coef))]
    dists = [("forgot_hemisphere", cyl), ("full_sphere", cyl + 2 * hemi), ("cylinder_height_total", Fraction(r * r * total) + hemi)]
    return _pi_spec(skill, q, coef, steps, dists, {"task": "cylinder_hemisphere", "r": r, "h": h}, exact=False)


def _solid_l5(rng: SeededRandom) -> _Spec:
    skill = "solid_inverse"
    kind = rng.choice(("height_from_volume", "litres", "silo_curved"))
    if kind == "height_from_volume":
        r, h = rng.randint(2, 12), rng.randint(3, 25)
        vol = Fraction(r * r * h)
        q = (f"A cylinder has a base radius of {_m(r)} cm and a volume of ${_sv(vol)}\\pi$ cm$^3$. "
             "Calculate the height of the cylinder.")
        steps = [("Volume = pi r squared h, so divide by pi r squared", _sv(h))]
        dists = [("forgot_to_divide_by_r_squared", vol), ("diameter_as_radius", vol / (4 * r * r))]
        return _numeric_spec(skill, q, Fraction(h), steps, dists, {"task": kind, "r": r, "h": h})
    if kind == "litres":
        r10 = rng.randint(5, 20)  # radius in tenths of a metre
        r = Fraction(r10, 10)
        h = Fraction(rng.randint(10, 30), 10)
        vol_m3 = PI * r * r * h
        litres = vol_m3 * 1000
        q = (f"A cylindrical tank has a diameter of {_m(2 * r)} m and a height of {_m(h)} m. How many litres of water can "
             f"it hold? (1 cubic metre = 1000 litres){_SF3_NOTE}")
        steps = [("Radius", _sv(r)), ("Volume in cubic metres", f"{float(vol_m3):.4f}"), ("Multiply by 1000", f"{float(litres):.4f}")]
        dists = [("no_conversion", vol_m3), ("wrong_conversion", vol_m3 * 100), ("r_not_halved", PI * (2 * r) ** 2 * h * 1000)]
        return _numeric_spec(skill, q, litres, steps, dists, {"task": kind, "d": str(2 * r), "h": str(h)}, mode="sig_figs", digits=3)
    r, h = rng.randint(2, 10), rng.randint(3, 15)
    coef = Fraction(2 * r * h + 2 * r * r)
    thing = rng.choice(("grain silo", "water tower"))
    q = (f"A {thing} is made from a cylinder with a hemisphere on top. Both have a radius of {_m(r)} m and the cylinder is "
         f"{_m(h)} m high. The curved surface area of a sphere of radius $r$ is $4\\pi r^2$. Calculate the total curved "
         f"surface area of the {thing} (do not include the circular base).{_SF3_NOTE}")
    steps = [("Curved surface of the cylinder", _pi_typed(Fraction(2 * r * h))), ("Curved surface of the hemisphere", _pi_typed(Fraction(2 * r * r))),
             ("Add", _pi_typed(coef))]
    dists = [("base_included", coef + r * r), ("sphere_for_hemisphere", Fraction(2 * r * h + 4 * r * r)), ("forgot_hemisphere", Fraction(2 * r * h))]
    return _pi_spec(skill, q, coef, steps, dists, {"task": kind, "r": r, "h": h}, exact=False)


class SurfaceAreaVolumeGenerator(_FamilyGenerator):
    generator_id = "nssco_surface_area_volume"
    version = 1
    levels = (1, 2, 3, 4, 5)
    level_skills = SOLID_LEVEL_SKILLS
    error_notes = SOLID_NOTES
    builders = {1: _solid_l1, 2: _solid_l2, 3: _solid_l3, 4: _solid_l4, 5: _solid_l5}


# ==========================================================================
# 15809 Similarity and Congruence (scale factors)
# ==========================================================================

SIMILAR_NOTES: Dict[str, Dict[str, str]] = {
    "similar_lengths": {
        "added_difference": "added the difference between the two known lengths instead of multiplying by the scale factor",
        "inverted_ratio": "multiplied by the scale factor the wrong way round",
    },
    "area_scale": {
        "length_factor_only": "multiplied by the length scale factor and did not square it",
        "cubed": "cubed the length scale factor, as for volumes",
        "inverted_ratio": "used the area scale factor the wrong way round",
        "not_square_rooted": "multiplied by the ratio of the areas instead of its square root",
    },
    "volume_scale": {
        "length_factor_only": "multiplied by the length scale factor and did not cube it",
        "squared": "squared the length scale factor, as for areas",
        "no_cube_root": "multiplied by the ratio of the volumes without taking the cube root",
        "inverted_ratio": "used the scale factor the wrong way round",
    },
    "mixed_scale": {
        "used_area_ratio": "multiplied the volume by the ratio of the areas",
        "length_factor_only": "multiplied by the length scale factor only",
        "squared": "squared the length scale factor instead of cubing it",
        "cubed": "cubed the length scale factor instead of squaring it",
        "used_volume_ratio": "multiplied the area by the ratio of the volumes",
    },
}

SIMILAR_LEVEL_SKILLS: Dict[int, Tuple[str, ...]] = {
    1: ("similar_lengths",),
    2: ("area_scale",),
    3: ("volume_scale",),
    4: ("mixed_scale",),
}

_SIMILAR_OBJECTS = ("cylindrical water tanks", "plastic bottles", "tins of beans", "cardboard boxes", "paint tins")


def _scale_pair(rng: SeededRandom, low: int = 2, high: int = 5) -> Tuple[int, int]:
    """(a, b) coprime with a < b: lengths of two similar shapes are in the ratio a : b."""
    while True:
        a = rng.randint(low, high)
        b = rng.randint(a + 1, high + 3)
        if _math.gcd(a, b) == 1:
            return a, b


def _sim_l1(rng: SeededRandom) -> _Spec:
    a, b = _scale_pair(rng, 2, 8)
    k = rng.randint(1, 6)
    c = a * k
    value = Fraction(b * k)
    t1, t2 = rng.choice((("ABC", "PQR"), ("DEF", "XYZ"), ("KLM", "STU")))
    q = (f"Triangles ${t1}$ and ${t2}$ are similar. ${t1[:2]}$ = {_m(a)} cm corresponds to ${t2[:2]}$ = {_m(b)} cm. "
         f"${t1[1:]}$ = {_m(c)} cm. Calculate the length of ${t2[1:]}$.")
    steps = [("Scale factor", _frac_str(Fraction(b, a))), ("Multiply the known side by the scale factor", _sv(value))]
    dists = [("added_difference", Fraction(c + b - a)), ("inverted_ratio", Fraction(c * a, b))]
    return _numeric_spec("similar_lengths", q, value, steps, dists, {"task": "similar_lengths", "a": a, "b": b, "c": c})


def _sim_l2(rng: SeededRandom) -> _Spec:
    a, b = _scale_pair(rng, 2, 6)
    obj = rng.choice(_SIMILAR_OBJECTS)
    if rng.chance(1, 2):
        area = rng.randint(2, 9) * a * a
        value = Fraction(area * b * b, a * a)
        q = (f"Two similar {obj} have heights of {_m(a)} cm and {_m(b)} cm. The surface area of the smaller one is "
             f"{_m(area)} cm$^2$. Calculate the surface area of the larger one.")
        steps = [("Length scale factor", _frac_str(Fraction(b, a))), ("Area scale factor is the square", _frac_str(Fraction(b * b, a * a))),
                 ("Multiply the area", _sv(value))]
        dists = [("length_factor_only", Fraction(area * b, a)), ("cubed", Fraction(area * b**3, a**3)), ("inverted_ratio", Fraction(area * a * a, b * b))]
        return _numeric_spec("area_scale", q, value, steps, dists, {"task": "area_from_heights", "a": a, "b": b, "area": area})
    h = rng.randint(1, 5) * a
    value = Fraction(h * b, a)
    q = (f"Two similar {obj} have surface areas of {_m(a * a * 4)} cm$^2$ and {_m(b * b * 4)} cm$^2$. The smaller one is "
         f"{_m(h)} cm high. Calculate the height of the larger one.")
    steps = [("Area scale factor", _frac_str(Fraction(b * b, a * a))), ("Length scale factor is the square root", _frac_str(Fraction(b, a))),
             ("Multiply the height", _sv(value))]
    dists = [("not_square_rooted", Fraction(h * b * b, a * a)), ("inverted_ratio", Fraction(h * a, b))]
    return _numeric_spec("area_scale", q, value, steps, dists, {"task": "height_from_areas", "a": a, "b": b, "h": h})


def _sim_l3(rng: SeededRandom) -> _Spec:
    a, b = _scale_pair(rng, 2, 5)
    obj = rng.choice(_SIMILAR_OBJECTS)
    if rng.chance(1, 2):
        v = rng.randint(2, 12) * a**3
        value = Fraction(v * b**3, a**3)
        q = (f"Two similar {obj} have heights of {_m(a * 3)} cm and {_m(b * 3)} cm. The capacity of the smaller one is "
             f"{_m(v)} cm$^3$. Calculate the capacity of the larger one.")
        steps = [("Length scale factor", _frac_str(Fraction(b, a))), ("Volume scale factor is the cube", _frac_str(Fraction(b**3, a**3))),
                 ("Multiply the capacity", _sv(value))]
        dists = [("length_factor_only", Fraction(v * b, a)), ("squared", Fraction(v * b * b, a * a)), ("inverted_ratio", Fraction(v * a**3, b**3))]
        return _numeric_spec("volume_scale", q, value, steps, dists, {"task": "volume_from_heights", "a": a, "b": b, "v": v})
    h = rng.randint(1, 6) * a
    value = Fraction(h * b, a)
    q = (f"Two similar {obj} hold {_m(a**3 * 5)} cm$^3$ and {_m(b**3 * 5)} cm$^3$. The smaller one is {_m(h)} cm high. "
         "Calculate the height of the larger one.")
    steps = [("Volume scale factor", _frac_str(Fraction(b**3, a**3))), ("Length scale factor is the cube root", _frac_str(Fraction(b, a))),
             ("Multiply the height", _sv(value))]
    dists = [("no_cube_root", Fraction(h * b**3, a**3)), ("inverted_ratio", Fraction(h * a, b))]
    return _numeric_spec("volume_scale", q, value, steps, dists, {"task": "height_from_volumes", "a": a, "b": b, "h": h})


def _sim_l4(rng: SeededRandom) -> _Spec:
    a, b = _scale_pair(rng, 2, 5)
    obj = rng.choice(_SIMILAR_OBJECTS)
    if rng.chance(1, 2):
        v = rng.randint(2, 9) * a**3
        value = Fraction(v * b**3, a**3)
        q = (f"Two similar {obj} have surface areas in the ratio ${a * a} : {b * b}$. The volume of the smaller one is "
             f"{_m(v)} cm$^3$. Calculate the volume of the larger one.")
        steps = [("Length ratio is the square root of the area ratio", f"{a}:{b}"), ("Volume scale factor is the cube", _frac_str(Fraction(b**3, a**3))),
                 ("Multiply the volume", _sv(value))]
        dists = [("used_area_ratio", Fraction(v * b * b, a * a)), ("length_factor_only", Fraction(v * b, a)), ("squared", Fraction(v * b**4, a**4))]
        return _numeric_spec("mixed_scale", q, value, steps, dists, {"task": "volume_from_area_ratio", "a": a, "b": b, "v": v})
    area = rng.randint(2, 9) * a * a
    value = Fraction(area * b * b, a * a)
    q = (f"Two similar {obj} have volumes in the ratio ${a**3} : {b**3}$. The surface area of the smaller one is "
         f"{_m(area)} cm$^2$. Calculate the surface area of the larger one.")
    steps = [("Length ratio is the cube root of the volume ratio", f"{a}:{b}"), ("Area scale factor is the square", _frac_str(Fraction(b * b, a * a))),
             ("Multiply the area", _sv(value))]
    dists = [("used_volume_ratio", Fraction(area * b**3, a**3)), ("length_factor_only", Fraction(area * b, a)), ("cubed", Fraction(area * b**3, a**3))]
    return _numeric_spec("mixed_scale", q, value, steps, dists, {"task": "area_from_volume_ratio", "a": a, "b": b, "area": area})


class SimilarityScaleFactorsGenerator(_FamilyGenerator):
    generator_id = "nssco_similarity_scale_factors"
    version = 1
    levels = (1, 2, 3, 4)
    level_skills = SIMILAR_LEVEL_SKILLS
    error_notes = SIMILAR_NOTES
    builders = {1: _sim_l1, 2: _sim_l2, 3: _sim_l3, 4: _sim_l4}


# ==========================================================================
# 15811 Angle and Perpendicular Bisectors (numeric questions only)
# ==========================================================================

BISECTOR_NOTES: Dict[str, Dict[str, str]] = {
    "angle_bisector_half": {
        "not_halved": "gave the whole angle instead of half of it",
        "doubled": "doubled the angle when the angle was to be halved",
        "not_doubled": "gave the half-angle and did not double it to find the whole angle",
        "halved_again": "halved the angle again instead of doubling it",
    },
    "perpendicular_bisector": {
        "half_chord_not_used": "used the whole chord instead of the half where the half was needed",
        "subtracted": "subtracted instead of using Pythagoras",
        "doubled": "doubled the length instead of halving it",
        "hypotenuse_as_leg": "added the squares instead of subtracting for a shorter side",
    },
    "bisector_in_triangle": {
        "not_halved": "used the whole angle at the vertex instead of half of it",
        "missing_step": "stopped before subtracting from 180 degrees",
        "exterior_confusion": "added the two angles instead of using the angle sum of the triangle",
    },
}

BISECTOR_LEVEL_SKILLS: Dict[int, Tuple[str, ...]] = {
    1: ("angle_bisector_half",),
    2: ("perpendicular_bisector",),
    3: ("bisector_in_triangle",),
}


def _bis_l1(rng: SeededRandom) -> _Spec:
    whole = rng.randint(20, 85) * 2
    half = whole // 2
    labels = rng.choice((("ABC", "ABD", "DBC", "BD"), ("PQR", "PQS", "SQR", "QS"), ("XYZ", "XYW", "WYZ", "YW")))
    abc, abd, dbc, line = labels
    if rng.chance(1, 2):
        q = (f"${line}$ is the bisector of {_angle(abc, whole)}. Calculate {_angle(abd)}.")
        steps = [("A bisector cuts the angle into two equal parts, so halve it", _sv(half))]
        dists = [("not_halved", whole), ("doubled", 2 * whole)]
        return _numeric_spec("angle_bisector_half", q, Fraction(half), steps, [(c, Fraction(v)) for c, v in dists],
                             {"task": "half", "whole": whole}, suffix="^\\circ")
    q = (f"${line}$ is the bisector of {_angle(abc)}. {_angle(dbc, half)}. Calculate {_angle(abc)}.")
    steps = [("The bisector cuts the angle into two equal parts, so double", _sv(whole))]
    dists = [("not_doubled", half), ("halved_again", Fraction(half, 2))]
    return _numeric_spec("angle_bisector_half", q, Fraction(whole), steps, [(c, Fraction(v)) for c, v in dists],
                         {"task": "double", "half": half}, suffix="^\\circ")


def _bis_l2(rng: SeededRandom) -> _Spec:
    skill = "perpendicular_bisector"
    kind = rng.choice(("equal_distance", "midpoint", "pythagoras"))
    if kind == "equal_distance":
        pa = rng.randint(5, 40)
        q = (f"$P$ is a point on the perpendicular bisector of the line $AB$. $PA$ = {_m(pa)} cm. Write down the length of $PB$.")
        steps = [("Every point on the perpendicular bisector is the same distance from A and B", _sv(pa))]
        return _numeric_spec(skill, q, Fraction(pa), steps, [("doubled", Fraction(2 * pa)), ("half_chord_not_used", Fraction(pa, 2))],
                             {"task": kind, "pa": pa})
    if kind == "midpoint":
        am = rng.randint(3, 30)
        q = (f"The perpendicular bisector of $AB$ meets $AB$ at $M$. $AB$ = {_m(2 * am)} cm. Calculate the length of $AM$.")
        steps = [("The perpendicular bisector passes through the midpoint, so halve AB", _sv(am))]
        return _numeric_spec(skill, q, Fraction(am), steps, [("half_chord_not_used", Fraction(2 * am)), ("doubled", Fraction(4 * am))],
                             {"task": kind, "am": am})
    half, pm, pa = rng.choice([(12, 5, 13), (6, 8, 10), (8, 6, 10), (15, 8, 17), (9, 12, 15), (20, 21, 29), (24, 7, 25), (5, 12, 13)])
    q = (f"$P$ is a point on the perpendicular bisector of $AB$ and the bisector meets $AB$ at $M$. $AB$ = {_m(2 * half)} cm "
         f"and $PA$ = {_m(pa)} cm. Calculate the length of $PM$.")
    steps = [("AM is half of AB", _sv(half)), ("Pythagoras in triangle AMP: PA squared minus AM squared", _sv(pa * pa - half * half)),
             ("Square root", _sv(pm))]
    dists = [("subtracted", Fraction(pa - half)), ("hypotenuse_as_leg", _sqrt(pa * pa + half * half))]
    return _numeric_spec(skill, q, Fraction(pm), steps, dists, {"task": kind, "half": half, "pm": pm, "pa": pa}, mode=None)


def _bis_l3(rng: SeededRandom) -> _Spec:
    b = rng.randint(20, 80) * 2
    c = rng.randint(20, 100)
    if b + c >= 175:
        raise _Retry
    value = 180 - c - b // 2
    q = (f"In triangle $ABC$, {_angle('ABC', b)} and {_angle('ACB', c)}. The bisector of {_angle('ABC')} meets $AC$ at $D$. "
         f"Calculate {_angle('BDC')}.")
    steps = [("Half of angle ABC", _sv(b // 2)), ("Angle sum of triangle BDC is 180", _sv(180 - c - b // 2))]
    dists = [("not_halved", 180 - c - b), ("exterior_confusion", c + b // 2), ("missing_step", c + b // 2)]
    dists = [(code, Fraction(v)) for code, v in dists if v > 0]
    return _numeric_spec("bisector_in_triangle", q, Fraction(value), steps, dists, {"task": "bdc", "b": b, "c": c}, suffix="^\\circ")


class BisectorsNumericGenerator(_FamilyGenerator):
    generator_id = "nssco_bisectors_numeric"
    version = 1
    levels = (1, 2, 3)
    level_skills = BISECTOR_LEVEL_SKILLS
    error_notes = BISECTOR_NOTES
    builders = {1: _bis_l1, 2: _bis_l2, 3: _bis_l3}


# ==========================================================================
# 15814 Angle Properties (Lines and Polygons)
# ==========================================================================

LINES_NOTES: Dict[str, Dict[str, str]] = {
    "lines_basic": {
        "vertically_opposite_used": "gave the given angle when the angle asked for is next to it on a straight line",
        "supplementary_used": "subtracted from 180 when the angles are vertically opposite and equal",
        "used_360": "used 360 degrees where the angles lie on a straight line",
        "used_180": "used 180 degrees where the angles are round a point",
        "used_90": "used 90 degrees instead of 180",
        "sum_given": "gave the total of the angles that are known instead of the missing angle",
    },
    "triangle_angles": {
        "used_180_minus_apex": "gave 180 minus the apex angle instead of sharing it between the two base angles",
        "apex_halved": "halved the apex angle",
        "base_again": "gave the base angle again as the apex angle",
        "subtracted_once": "took one base angle from 180 degrees and did not take the second one off",
        "interior_angle": "gave the interior angle at C instead of the exterior angle",
        "used_180_minus_one": "took only one of the two angles from 180 degrees",
    },
    "parallel_lines": {
        "used_co_interior": "treated the angles as co-interior (adding to 180) when they are equal",
        "used_equal": "treated the angles as equal when they are co-interior and add up to 180",
    },
    "polygon_angles": {
        "used_180": "used 180 where the sum of the exterior angles (360) belongs",
        "interior_angle": "gave the interior angle instead of the number of sides",
        "exterior_angle": "gave the exterior angle instead of the interior angle",
        "sum_of_angles": "gave the sum of the interior angles instead of one angle",
        "n_times_180": "multiplied the number of sides by 180 instead of using (n minus 2) lots of 180",
        "n_minus_1_times_180": "used (n minus 1) lots of 180 degrees",
        "used_360": "used 360 as the sum of the angles of any polygon",
        "not_divided": "did not divide the remaining angle by the number of equal angles",
        "used_n_times_180": "multiplied the number of sides by 180 degrees for the angle sum",
    },
    "polygon_multistep": {
        "interior_angle": "gave the interior angle of the polygon instead of the base angle of the triangle",
        "exterior_angle": "gave the exterior angle of the polygon instead of the base angle of the triangle",
        "base_angle_not_halved": "did not share the remaining angle between the two base angles",
        "used_180": "shared 180 degrees instead of 360 degrees between the parts",
        "smallest_angle": "gave the smallest angle instead of the largest",
    },
}

LINES_LEVEL_SKILLS: Dict[int, Tuple[str, ...]] = {
    1: ("lines_basic",),
    2: ("triangle_angles",),
    3: ("parallel_lines",),
    4: ("polygon_angles",),
    5: ("polygon_multistep",),
}


def _pos(dists):
    return [(c, Fraction(v)) for c, v in dists if v > 0]


def _lines_l1(rng: SeededRandom) -> _Spec:
    skill = "lines_basic"
    kind = rng.choice(("crossing_adjacent", "crossing_opposite", "straight_line", "point"))
    if kind.startswith("crossing"):
        x = rng.choice([v for v in range(25, 156) if v != 90])
        base = f"The straight lines $AB$ and $CD$ cross at $O$. {_angle('AOC', x)}."
        if kind == "crossing_adjacent":
            q, ans = f"{base} Calculate {_angle('COB')}.", 180 - x
            steps = [("Angles on a straight line add up to 180", _sv(ans))]
            dists = [("vertically_opposite_used", x), ("used_360", 360 - x), ("used_90", 90 - x)]
        else:
            q, ans = f"{base} Calculate {_angle('BOD')}.", x
            steps = [("Vertically opposite angles are equal", _sv(ans))]
            dists = [("supplementary_used", 180 - x), ("used_360", 360 - x), ("used_90", 90 - x)]
        return _numeric_spec(skill, q, Fraction(ans), steps, _pos(dists), {"task": kind, "x": x}, suffix="^\\circ")
    if kind == "straight_line":
        a, b = rng.randint(25, 80), rng.randint(25, 80)
        ans = 180 - a - b
        q = (f"Three angles on a straight line are ${a}^\\circ$, ${b}^\\circ$ and $a^\\circ$. Calculate the value of $a$.")
        steps = [("Angles on a straight line add up to 180", _sv(ans))]
        return _numeric_spec(skill, q, Fraction(ans), steps, _pos([("used_360", 360 - a - b), ("used_90", 90 - a - b)]),
                             {"task": kind, "a": a, "b": b})
    a, b, c = rng.randint(50, 120), rng.randint(50, 120), rng.randint(40, 100)
    ans = 360 - a - b - c
    if ans <= 0:
        raise _Retry
    q = (f"Four angles meet at a point. Three of them are ${a}^\\circ$, ${b}^\\circ$ and ${c}^\\circ$. "
         "Calculate the fourth angle.")
    steps = [("Angles round a point add up to 360", _sv(ans))]
    return _numeric_spec(skill, q, Fraction(ans), steps, _pos([("used_180", 180 - a - b - c), ("sum_given", a + b + c)]),
                         {"task": kind, "a": a, "b": b, "c": c}, suffix="^\\circ")


def _lines_l2(rng: SeededRandom) -> _Spec:
    skill = "triangle_angles"
    kind = rng.choice(("isosceles_apex", "isosceles_base", "exterior"))
    if kind == "isosceles_apex":
        apex = rng.randint(20, 80) * 2 - (0 if rng.chance(1, 2) else 0)
        ans = (180 - apex) // 2
        q = f"Triangle $ABC$ is isosceles with $AB = AC$. {_angle('BAC', apex)}. Calculate {_angle('ABC')}."
        steps = [("The base angles are equal and the angles add up to 180", _sv(180 - apex)), ("Share between the two base angles", _sv(ans))]
        return _numeric_spec(skill, q, Fraction(ans), steps, _pos([("used_180_minus_apex", 180 - apex), ("apex_halved", apex // 2)]),
                             {"task": kind, "apex": apex}, suffix="^\\circ")
    if kind == "isosceles_base":
        base = rng.randint(25, 80)
        ans = 180 - 2 * base
        q = f"Triangle $ABC$ is isosceles with $AB = AC$. {_angle('ABC', base)}. Calculate {_angle('BAC')}."
        steps = [("The base angles are equal, so ACB is also the same size", _sv(base)), ("Angles in a triangle add up to 180", _sv(ans))]
        return _numeric_spec(skill, q, Fraction(ans), steps, _pos([("base_again", base), ("subtracted_once", 180 - base)]),
                             {"task": kind, "base": base}, suffix="^\\circ")
    a, b = rng.randint(30, 85), rng.randint(30, 85)
    ans = a + b
    q = (f"In triangle $ABC$, the side $BC$ is extended to a point $D$. {_angle('BAC', a)} and {_angle('ABC', b)}. "
         f"Calculate {_angle('ACD')}.")
    steps = [("An exterior angle of a triangle equals the sum of the two opposite interior angles", _sv(ans))]
    return _numeric_spec(skill, q, Fraction(ans), steps, _pos([("interior_angle", 180 - a - b), ("used_180_minus_one", 180 - a)]),
                         {"task": kind, "a": a, "b": b}, suffix="^\\circ")


_PARALLEL_INTRO = (
    "The line $AB$ is parallel to the line $CD$ and lies above it, with $A$ and $C$ on the left. A straight line $EF$ "
    "crosses $AB$ at $P$ and $CD$ at $Q$, with $E$ above $AB$ and $F$ below $CD$."
)
# (given angle, angle to find, relation, rule)
_PARALLEL_CASES = (
    ("APQ", "PQD", "equal", "Alternate angles are equal"),
    ("BPQ", "PQC", "equal", "Alternate angles are equal"),
    ("PQD", "APQ", "equal", "Alternate angles are equal"),
    ("PQC", "BPQ", "equal", "Alternate angles are equal"),
    ("EPB", "PQD", "equal", "Corresponding angles are equal"),
    ("EPA", "PQC", "equal", "Corresponding angles are equal"),
    ("BPQ", "FQD", "equal", "Corresponding angles are equal"),
    ("APQ", "FQC", "equal", "Corresponding angles are equal"),
    ("PQD", "EPB", "equal", "Corresponding angles are equal"),
    ("APQ", "PQC", "sum", "Co-interior angles add up to 180"),
    ("BPQ", "PQD", "sum", "Co-interior angles add up to 180"),
    ("PQC", "APQ", "sum", "Co-interior angles add up to 180"),
    ("PQD", "BPQ", "sum", "Co-interior angles add up to 180"),
)


def parallel_line_angles(theta_degrees: float) -> Dict[str, float]:
    """All the named angles in the parallel-lines figure, measured from coordinates.

    ``theta`` is angle BPQ. Used to check every case in ``_PARALLEL_CASES`` holds.
    """
    t = _math.radians(theta_degrees)
    d = (_math.cos(t), -_math.sin(t))
    P = (0.0, 1.0)
    Q = (_math.cos(t) / _math.sin(t), 0.0)
    pts = {
        "P": P, "Q": Q,
        "A": (P[0] - 1, P[1]), "B": (P[0] + 1, P[1]), "C": (Q[0] - 1, Q[1]), "D": (Q[0] + 1, Q[1]),
        "E": (P[0] - d[0], P[1] - d[1]), "F": (Q[0] + d[0], Q[1] + d[1]),
    }

    def ang(x, v, y):
        a = (pts[x][0] - pts[v][0], pts[x][1] - pts[v][1])
        b = (pts[y][0] - pts[v][0], pts[y][1] - pts[v][1])
        c = (a[0] * b[0] + a[1] * b[1]) / (_math.hypot(*a) * _math.hypot(*b))
        return _math.degrees(_math.acos(max(-1.0, min(1.0, c))))

    return {name: ang(name[0], name[1], name[2]) for name in ("EPB", "EPA", "APQ", "BPQ", "PQC", "PQD", "FQC", "FQD")}


def _lines_l3(rng: SeededRandom) -> _Spec:
    given, find, relation, rule = rng.choice(_PARALLEL_CASES)
    x = rng.choice([v for v in range(30, 151) if v != 90])
    # prove the relation from coordinates, for a figure whose angle BPQ is 70 degrees
    angles = parallel_line_angles(70.0)
    if relation == "equal":
        _require(abs(angles[given] - angles[find]) < 1e-9, f"{given}={find} fails in the figure")
        ans = x
    else:
        _require(abs(angles[given] + angles[find] - 180) < 1e-9, f"{given}+{find}=180 fails in the figure")
        ans = 180 - x
    q = f"{_PARALLEL_INTRO} {_angle(given, x)}. Calculate {_angle(find)}."
    steps = [(rule, _sv(ans))]
    wrong = ("used_co_interior", 180 - x) if relation == "equal" else ("used_equal", x)
    return _numeric_spec("parallel_lines", q, Fraction(ans), steps, _pos([wrong]),
                         {"task": "parallel_lines", "given": given, "find": find, "relation": relation, "x": x}, suffix="^\\circ")


_WORD = {2: "Two", 3: "Three", 4: "Four"}
_NUMBER_WORD = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six"}
_REGULAR_SIDES = (5, 6, 8, 9, 10, 12, 15, 18, 20, 24, 30, 36)


def _lines_l4(rng: SeededRandom) -> _Spec:
    skill = "polygon_angles"
    kind = rng.choice(("sides_from_exterior", "interior_regular", "sum_interior", "unknown_angle"))
    if kind == "sides_from_exterior":
        n = rng.choice(_REGULAR_SIDES)
        e = 360 // n
        q = f"A regular polygon has an exterior angle of ${e}^\\circ$. Find the number of sides of the polygon."
        steps = [("The exterior angles of a polygon add up to 360", _sv(360)), ("Divide 360 by the exterior angle", _sv(n))]
        dists = [("used_180", Fraction(180, e)), ("interior_angle", Fraction(180 - e))]
        return _numeric_spec(skill, q, Fraction(n), steps, dists, {"task": kind, "n": n})
    if kind == "interior_regular":
        n = rng.choice(_REGULAR_SIDES)
        ans = 180 - 360 // n
        q = f"Calculate the size of one interior angle of a regular polygon with {_m(n)} sides."
        steps = [("Sum of the interior angles is (n minus 2) x 180", _sv((n - 2) * 180)), ("Divide by the number of sides", _sv(ans))]
        dists = [("exterior_angle", Fraction(360, n)), ("sum_of_angles", Fraction((n - 2) * 180))]
        return _numeric_spec(skill, q, Fraction(ans), steps, dists, {"task": kind, "n": n}, suffix="^\\circ")
    if kind == "sum_interior":
        n = rng.randint(5, 12)
        ans = (n - 2) * 180
        q = f"Calculate the sum of the interior angles of a polygon with {_m(n)} sides."
        steps = [("Sum = (n minus 2) x 180", _sv(ans))]
        dists = [("n_times_180", Fraction(n * 180)), ("n_minus_1_times_180", Fraction((n - 1) * 180))]
        return _numeric_spec(skill, q, Fraction(ans), steps, dists, {"task": kind, "n": n}, suffix="^\\circ")
    n = rng.randint(5, 8)
    k = rng.randint(2, 4)
    total = (n - 2) * 180
    x = rng.randint(100, 150)
    others = n - k
    known: List[int] = [rng.randint(70, 170) for _ in range(others - 1)]
    last = total - k * x - sum(known)
    if not 60 <= last <= 175:
        raise _Retry
    known.append(last)
    names = {5: "five", 6: "six", 7: "seven", 8: "eight"}[n]
    listed = ", ".join(f"${v}^\\circ$" for v in known[:-1]) + (" and " if others > 1 else "") + f"${known[-1]}^\\circ$"
    q = (f"A polygon has {names} sides. {_WORD[k]} of its interior angles are equal to $x^\\circ$. The other {_NUMBER_WORD[others]} interior angles "
         f"are {listed}. Calculate the value of $x$.")
    steps = [("Sum of the interior angles is (n minus 2) x 180", _sv(total)), ("Subtract the known angles", _sv(total - sum(known))),
             ("Divide by the number of equal angles", _sv(x))]
    dists = [("not_divided", Fraction(total - sum(known))), ("used_360", Fraction(360 - sum(known), k)), ("used_n_times_180", Fraction(n * 180 - sum(known), k))]
    return _numeric_spec(skill, q, Fraction(x), steps, _pos(dists), {"task": kind, "n": n, "k": k, "known": known}, suffix="^\\circ")


_RATIO_TOTALS = (8, 9, 10, 12, 15, 18, 20, 24, 30, 36)


def _ratio_parts(rng: SeededRandom) -> List[int]:
    """Four ratio parts whose total divides 360 and whose largest part gives an angle under 180."""
    total = rng.choice(_RATIO_TOTALS)
    cuts = sorted(rng.randint(1, total - 1) for _ in range(3))
    parts = [cuts[0], cuts[1] - cuts[0], cuts[2] - cuts[1], total - cuts[2]]
    if min(parts) < 1 or Fraction(360 * max(parts), total) >= 180 or len(set(parts)) < 3:
        raise _Retry
    return sorted(parts)


def _lines_l5(rng: SeededRandom) -> _Spec:
    skill = "polygon_multistep"
    if rng.chance(1, 2):
        n = rng.choice((5, 6, 8, 9, 10, 12, 15, 18, 20, 24))
        letters = "ABCDEFGHIJKL"[:n]
        interior = 180 - 360 // n
        ans = Fraction(180, n)
        q = (f"${letters}$ is a regular polygon with {_m(n)} sides. Calculate {_angle('CAB')}.")
        steps = [("Interior angle of the regular polygon", _sv(interior)),
                 ("Triangle ABC is isosceles, so share 180 minus the interior angle between the base angles", _sv(ans))]
        dists = [("interior_angle", Fraction(interior)), ("exterior_angle", Fraction(360, n)), ("base_angle_not_halved", Fraction(360, n) + 0)]
        return _numeric_spec(skill, q, ans, steps, dists, {"task": "regular_diagonal", "n": n}, suffix="^\\circ")
    parts = _ratio_parts(rng)
    unit = Fraction(360, sum(parts))
    ans = unit * max(parts)
    q = (f"The four interior angles of a quadrilateral are in the ratio ${' : '.join(str(p) for p in parts)}$. "
         "Calculate the size of the largest angle.")
    steps = [("Add the parts of the ratio", _sv(sum(parts))), ("One part is 360 divided by the total", _sv(unit)), ("Multiply by the largest part", _sv(ans))]
    dists = [("used_180", Fraction(180, sum(parts)) * max(parts)), ("smallest_angle", unit * min(parts))]
    return _numeric_spec(skill, q, ans, steps, dists, {"task": "ratio_quadrilateral", "parts": list(parts)}, suffix="^\\circ")


class AnglesLinesPolygonsGenerator(_FamilyGenerator):
    generator_id = "nssco_angles_lines_polygons"
    version = 1
    levels = (1, 2, 3, 4, 5)
    level_skills = LINES_LEVEL_SKILLS
    error_notes = LINES_NOTES
    builders = {1: _lines_l1, 2: _lines_l2, 3: _lines_l3, 4: _lines_l4, 5: _lines_l5}


# ==========================================================================
# 15815 Angle Properties (Circles)
# ==========================================================================

CIRCLE_ANGLE_NOTES: Dict[str, Dict[str, str]] = {
    "centre_circumference": {
        "not_doubled": "gave the angle at the circumference as the angle at the centre",
        "reflex": "gave the reflex angle at the centre when the other angle was asked for",
        "non_reflex": "gave the angle that is not reflex when the reflex angle was asked for",
        "not_halved": "gave the angle at the centre as the angle at the circumference",
        "used_reflex_angle": "halved the reflex angle at the centre instead of the angle given",
        "forgot_right_angle": "used 180 degrees instead of 90 degrees for the angle in a semicircle",
        "used_x": "gave the angle already known",
    },
    "same_segment_cyclic": {
        "used_supplement": "subtracted from 180 when the angles are in the same segment and equal",
        "doubled": "doubled the angle",
        "equal_angle": "gave the angle itself instead of subtracting from 180 for opposite angles of a cyclic quadrilateral",
        "used_360": "subtracted from 360 instead of 180",
        "used_90": "subtracted from 90 instead of 180",
    },
    "tangent_radius": {
        "used_180": "subtracted from 180 instead of using the right angle between a tangent and a radius",
        "used_x": "gave the angle already known",
        "not_halved": "did not share the remaining angle between the two equal base angles",
        "used_90": "subtracted the angle at the centre from 90 instead of 180 before halving",
    },
    "tangent_chord_pairs": {
        "not_halved": "did not share the remaining angle between the two equal base angles",
        "used_x": "gave the angle already known",
        "used_90": "took the angle from 90 degrees without halving 180 first",
        "used_supplement": "subtracted from 180 when the angles are equal (alternate segment theorem)",
        "not_doubled": "gave the angle at the circumference as the angle at the centre",
        "used_180": "subtracted twice the angle from 180 instead of using the alternate segment theorem",
        "half": "halved the angle at the centre",
    },
    "circle_chain": {
        "not_halved": "did not halve the angle at the centre before finding the opposite angle",
        "angle_at_circumference": "gave the angle at the circumference instead of the angle in the opposite segment",
        "used_centre": "gave the angle at the centre",
        "used_180": "subtracted from 180 instead of sharing it between the two equal base angles",
        "used_y": "gave half the angle at the centre",
        "used_x": "gave the angle already known",
    },
}

CIRCLE_ANGLE_LEVEL_SKILLS: Dict[int, Tuple[str, ...]] = {
    1: ("centre_circumference",),
    2: ("same_segment_cyclic",),
    3: ("tangent_radius",),
    4: ("tangent_chord_pairs",),
    5: ("circle_chain",),
}


def _circ_l1(rng: SeededRandom) -> _Spec:
    skill = "centre_circumference"
    kind = rng.choice(("at_centre", "at_circumference", "reflex", "semicircle"))
    if kind == "at_centre":
        x = rng.randint(15, 80)
        q = (f"$A$, $B$ and $C$ are points on a circle with centre $O$. $B$ lies on the major arc $AC$. {_angle('ABC', x)}. "
             f"Calculate {_angle('AOC')}.")
        steps = [("The angle at the centre is twice the angle at the circumference", _sv(2 * x))]
        return _numeric_spec(skill, q, Fraction(2 * x), steps, _pos([("not_doubled", x), ("reflex", 360 - 2 * x)]),
                             {"task": kind, "x": x}, suffix="^\\circ")
    if kind == "at_circumference":
        y = rng.randint(15, 85) * 2
        q = (f"$A$, $B$ and $C$ are points on a circle with centre $O$. $B$ lies on the major arc $AC$. {_angle('AOC', y)}. "
             f"Calculate {_angle('ABC')}.")
        steps = [("The angle at the circumference is half the angle at the centre", _sv(y // 2))]
        return _numeric_spec(skill, q, Fraction(y // 2), steps, _pos([("not_halved", y), ("used_reflex_angle", 180 - y // 2)]),
                             {"task": kind, "y": y}, suffix="^\\circ")
    if kind == "reflex":
        x = rng.randint(95, 175)
        q = (f"$A$, $B$ and $C$ are points on a circle with centre $O$. $B$ lies on the minor arc $AC$. {_angle('ABC', x)}. "
             "Calculate the reflex angle $AOC$.")
        steps = [("The reflex angle at the centre is twice the angle at the circumference", _sv(2 * x))]
        return _numeric_spec(skill, q, Fraction(2 * x), steps, _pos([("not_doubled", x), ("non_reflex", 360 - 2 * x)]),
                             {"task": kind, "x": x}, suffix="^\\circ")
    x = rng.randint(15, 75)
    q = (f"$AB$ is a diameter of a circle and $C$ is a point on the circle. {_angle('ABC', x)}. Calculate {_angle('BAC')}.")
    steps = [("The angle in a semicircle is 90", "90"), ("Angles in triangle ABC add up to 180", _sv(90 - x))]
    return _numeric_spec(skill, q, Fraction(90 - x), steps, _pos([("forgot_right_angle", 180 - x), ("used_x", x)]),
                         {"task": kind, "x": x}, suffix="^\\circ")


def _circ_l2(rng: SeededRandom) -> _Spec:
    skill = "same_segment_cyclic"
    kind = rng.choice(("same_segment", "cyclic_bcd", "cyclic_adc"))
    x = rng.choice([v for v in range(30, 150) if v != 90])
    if kind == "same_segment":
        q = (f"$A$, $B$, $C$ and $D$ lie on a circle. $C$ and $D$ are on the same side of the chord $AB$. "
             f"{_angle('ACB', x)}. Calculate {_angle('ADB')}.")
        steps = [("Angles in the same segment are equal", _sv(x))]
        return _numeric_spec(skill, q, Fraction(x), steps, _pos([("used_supplement", 180 - x), ("doubled", 2 * x)]),
                             {"task": kind, "x": x}, suffix="^\\circ")
    given, find = ("ABC", "ADC") if kind == "cyclic_adc" else ("BAD", "BCD")
    q = f"$ABCD$ is a cyclic quadrilateral. {_angle(given, x)}. Calculate {_angle(find)}."
    steps = [("Opposite angles of a cyclic quadrilateral add up to 180", _sv(180 - x))]
    return _numeric_spec(skill, q, Fraction(180 - x), steps, _pos([("equal_angle", x), ("used_360", 360 - x), ("used_90", 90 - x)]),
                         {"task": kind, "given": given, "find": find, "x": x}, suffix="^\\circ")


def _circ_l3(rng: SeededRandom) -> _Spec:
    skill = "tangent_radius"
    kind = rng.choice(("tangent_triangle", "radii_isosceles", "tangent_chord_radius"))
    if kind == "tangent_triangle":
        x = rng.randint(20, 75)
        q = (f"$PT$ is a tangent to a circle with centre $O$, touching the circle at $T$. {_angle('TOP', x)}. "
             f"Calculate {_angle('OPT')}.")
        steps = [("A tangent is perpendicular to the radius, so angle OTP is 90", "90"), ("Angles in triangle OTP add up to 180", _sv(90 - x))]
        return _numeric_spec(skill, q, Fraction(90 - x), steps, _pos([("used_180", 180 - x), ("used_x", x)]), {"task": kind, "x": x}, suffix="^\\circ")
    if kind == "radii_isosceles":
        x = rng.randint(20, 80) * 2
        ans = (180 - x) // 2
        q = (f"$A$ and $B$ are points on a circle with centre $O$. {_angle('AOB', x)}. Calculate {_angle('OAB')}.")
        steps = [("OA and OB are radii, so triangle OAB is isosceles", "180"), ("Share 180 minus the angle at the centre between the base angles", _sv(ans))]
        return _numeric_spec(skill, q, Fraction(ans), steps, _pos([("not_halved", 180 - x), ("used_x", x // 2), ("used_90", 90 - x)]),
                             {"task": kind, "x": x}, suffix="^\\circ")
    x = rng.randint(15, 70)
    q = (f"$TA$ is a tangent to a circle with centre $O$, touching the circle at $A$. $B$ is a point on the circle on the same "
         f"side of $OA$ as $T$. {_angle('OAB', x)}. Calculate {_angle('TAB')}.")
    steps = [("A tangent is perpendicular to the radius, so angle TAO is 90", "90"), ("Subtract angle OAB", _sv(90 - x))]
    return _numeric_spec(skill, q, Fraction(90 - x), steps, _pos([("used_180", 180 - x), ("used_x", x)]), {"task": kind, "x": x}, suffix="^\\circ")


def _circ_l4(rng: SeededRandom) -> _Spec:
    skill = "tangent_chord_pairs"
    kind = rng.choice(("tangent_pair_pab", "tangent_pair_aob", "alt_segment_acb", "alt_segment_aob", "alt_segment_oab"))
    if kind.startswith("tangent_pair"):
        x = rng.randint(15, 55) * 2
        base = (f"$PA$ and $PB$ are tangents to a circle with centre $O$, touching the circle at $A$ and $B$. {_angle('APB', x)}.")
        if kind == "tangent_pair_pab":
            ans = (180 - x) // 2
            q = f"{base} Calculate {_angle('PAB')}."
            steps = [("Tangents from a point are equal in length, so triangle PAB is isosceles", "180"), ("Share between the base angles", _sv(ans))]
            dists = [("not_halved", 180 - x), ("used_x", x // 2), ("used_90", 90 - x)]
        else:
            ans = 180 - x
            q = f"{base} Calculate {_angle('AOB')}."
            steps = [("Angles OAP and OBP are 90 (tangent and radius)", "90"), ("Angles in quadrilateral OAPB add up to 360", _sv(ans))]
            dists = [("used_x", x), ("used_90", 90 - x), ("half", (180 - x) // 2)]
        return _numeric_spec(skill, q, Fraction(ans), steps, _pos(dists), {"task": kind, "x": x}, suffix="^\\circ")
    x = rng.randint(20, 80)
    base = (f"The line $TA$ is a tangent to a circle with centre $O$, touching the circle at $A$. $B$ and $C$ are points on the "
            f"circle, with $C$ on the opposite side of the chord $AB$ from $T$. {_angle('TAB', x)}.")
    if kind == "alt_segment_acb":
        q, ans = f"{base} Calculate {_angle('ACB')}.", x
        steps = [("Angle between a tangent and a chord equals the angle in the alternate segment", _sv(ans))]
        dists = [("used_supplement", 180 - x), ("used_90", 90 - x)]
    elif kind == "alt_segment_aob":
        q, ans = f"{base} Calculate {_angle('AOB')}.", 2 * x
        steps = [("Angle ACB equals angle TAB (alternate segment)", _sv(x)), ("The angle at the centre is twice the angle at the circumference", _sv(ans))]
        dists = [("not_doubled", x), ("used_180", 180 - 2 * x)]
    else:
        q, ans = f"{base} Calculate {_angle('OAB')}.", 90 - x
        steps = [("The tangent is perpendicular to the radius OA", "90"), ("Subtract angle TAB", _sv(ans))]
        dists = [("used_x", x), ("used_180", 180 - 2 * x), ("not_halved", 180 - 2 * x)]
        dists = [dists[0], dists[1]]
    return _numeric_spec(skill, q, Fraction(ans), steps, _pos(dists), {"task": kind, "x": x}, suffix="^\\circ")


def _circ_l5(rng: SeededRandom) -> _Spec:
    skill = "circle_chain"
    y = rng.randint(30, 85) * 2
    kind = rng.choice(("adc", "oac", "obc_tangent"))
    if kind in ("adc", "oac"):
        base = (f"$A$, $B$, $C$ and $D$ lie in that order on a circle with centre $O$. $B$ lies on the major arc $AC$ and $D$ lies "
                f"on the minor arc $AC$. {_angle('AOC', y)}.")
        if kind == "adc":
            ans = 180 - y // 2
            q = f"{base} Calculate {_angle('ADC')}."
            steps = [("The angle at the circumference is half the angle at the centre: angle ABC", _sv(y // 2)),
                     ("Opposite angles of a cyclic quadrilateral add up to 180", _sv(ans))]
            dists = [("not_halved", 180 - y), ("angle_at_circumference", y // 2), ("used_centre", y)]
        else:
            ans = 90 - y // 2
            q = f"{base} Calculate {_angle('OAC')}."
            steps = [("OA and OC are radii, so triangle OAC is isosceles", "180"), ("Share 180 minus the angle at the centre between the base angles", _sv(ans))]
            dists = [("used_180", 180 - y), ("used_y", y // 2)]
        return _numeric_spec(skill, q, Fraction(ans), steps, _pos(dists), {"task": kind, "y": y}, suffix="^\\circ")
    x = rng.randint(15, 70)
    q = (f"The line $TA$ is a tangent to a circle with centre $O$, touching the circle at $A$. $B$ is a point on the circle on the "
         f"same side of $OA$ as $T$. {_angle('TAB', x)}. Calculate {_angle('OBA')}.")
    steps = [("The tangent is perpendicular to the radius, so angle OAB", _sv(90 - x)), ("OA = OB, so triangle OAB is isosceles and angle OBA is equal to angle OAB", _sv(90 - x))]
    return _numeric_spec(skill, q, Fraction(90 - x), steps, _pos([("used_x", x), ("used_180", 180 - 2 * x)]), {"task": "obt_tangent", "x": x}, suffix="^\\circ")


class AnglesCirclesGenerator(_FamilyGenerator):
    generator_id = "nssco_angles_circles"
    version = 1
    levels = (1, 2, 3, 4, 5)
    level_skills = CIRCLE_ANGLE_LEVEL_SKILLS
    error_notes = CIRCLE_ANGLE_NOTES
    builders = {1: _circ_l1, 2: _circ_l2, 3: _circ_l3, 4: _circ_l4, 5: _circ_l5}


def _capitalised(builder):
    """A question may start a sentence with an angle name: write 'Angle', not 'angle'."""

    def wrapped(rng: SeededRandom) -> _Spec:
        spec = builder(rng)
        spec.question = re.sub(r"(^|(?<=[.?] ))angle \$", "Angle $", spec.question)
        return spec

    wrapped.__name__ = builder.__name__
    return wrapped


for _cls in (
    PerimetersAreasGenerator, CirclesArcsSectorsGenerator, SurfaceAreaVolumeGenerator, SimilarityScaleFactorsGenerator,
    BisectorsNumericGenerator, AnglesLinesPolygonsGenerator, AnglesCirclesGenerator,
):
    _cls.builders = {level: _capitalised(fn) for level, fn in _cls.builders.items()}


GENERATORS = [
    PerimetersAreasGenerator(),
    CirclesArcsSectorsGenerator(),
    SurfaceAreaVolumeGenerator(),
    SimilarityScaleFactorsGenerator(),
    BisectorsNumericGenerator(),
    AnglesLinesPolygonsGenerator(),
    AnglesCirclesGenerator(),
]
