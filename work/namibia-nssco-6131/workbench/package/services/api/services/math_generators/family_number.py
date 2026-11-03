"""Generators for three NSSCO Mathematics number lessons.

* 15795 Advanced Percentage Calculations   -> ``nssco_advanced_percentages``
* 15794 Fractions, Decimals, Percentages, Ordering -> ``nssco_fractions_decimals_percentages``
* 15798 Ratios, Scales, Rates              -> ``nssco_ratios_scales_rates``

Levels follow the shapes of the 2020-2024 Paper 1 / Paper 2 questions for these
lessons (one- and two-mark "Find / Calculate / Work out / Write down" parts,
3 s.f. for percentages and speeds, 2 d.p. for compound interest, answers as
exact whole numbers or decimals for reverse percentages, ratios and maps).

Every problem is built backwards from its answer and recomputed in exact
``Fraction`` arithmetic before it is returned. Distractors are the answers a
learner gets from one specific, known mistake; any distractor that rounds to the
correct answer is dropped.

Money is written "Namibian dollars" in the question text. The exam prints
"N$", but a dollar sign in question text would clash with the ``$...$`` maths
delimiters, so it is spelled out. Learners may still type N$ in an answer; the
marker ignores it.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from decimal import ROUND_HALF_UP, Decimal
from fractions import Fraction
from math import gcd
from typing import Any, Callable, Dict, List, Optional, Sequence, Tuple

from .base import Distractor, GeneratedProblem, GeneratorError, MathGenerator, SeededRandom, Step
from .formatting import math, number_latex

_MAX_ATTEMPTS = 200
_MAX_DISTRACTORS = 3


class _Retry(Exception):
    """This draw cannot give a clean problem; try the next random numbers."""


def _require(condition: bool, message: str) -> None:
    if not condition:
        raise GeneratorError(f"self-check failed: {message}")


# --------------------------------------------------------------------------
# Number formatting and rounding (matches how services.math_marking rounds)
# --------------------------------------------------------------------------


def _dec_str(x: Fraction) -> str:
    """Exact terminating decimal as text; ``_Retry`` if it does not terminate."""
    d = x.denominator
    for p in (2, 5):
        while d % p == 0:
            d //= p
    if d != 1:
        raise _Retry
    sign = "-" if x < 0 else ""
    x = abs(x)
    k = 0
    while (x * 10**k).denominator != 1:
        k += 1
    n = int(x * 10**k)
    if k == 0:
        return sign + str(n)
    s = str(n).rjust(k + 1, "0")
    return sign + s[:-k] + "." + s[-k:]


def _to_decimal(x: Fraction) -> Decimal:
    return Decimal(x.numerator) / Decimal(x.denominator)


def _round_dec(x: Fraction, mode: str, digits: int) -> Decimal:
    d = _to_decimal(x)
    if mode == "sig_figs":
        if d == 0:
            return Decimal(0)
        exp = d.adjusted() - (digits - 1)
        return d.quantize(Decimal(1).scaleb(exp), rounding=ROUND_HALF_UP)
    return d.quantize(Decimal(1).scaleb(-digits), rounding=ROUND_HALF_UP)


def _fmt_rounded(x: Fraction, mode: str, digits: int) -> str:
    d = _round_dec(x, mode, digits)
    if mode == "decimal_places":
        return format(d, "f")
    return format(d.normalize(), "f")


def _typed_number(x: Fraction, mode: Optional[str], digits: int, loose: bool = False) -> str:
    """Plain text a learner would type for ``x`` under the rounding rule."""
    if mode is None:
        try:
            return _dec_str(x)
        except _Retry:
            if not loose:
                raise
            return _fmt_rounded(x, "decimal_places", 2)
    return _fmt_rounded(x, mode, digits)


def _key(x: Fraction, mode: Optional[str], digits: int) -> Any:
    """What the marker will treat as 'the same answer'."""
    if mode is None:
        return x
    return _round_dec(x, mode, digits)


def _fmt_money_dp(x: Fraction) -> str:
    return _fmt_rounded(x, "decimal_places", 2)


def _mixed_latex(x: Fraction) -> str:
    sign = "-" if x < 0 else ""
    x = abs(x)
    q, r = divmod(x.numerator, x.denominator)
    if r == 0:
        return f"{sign}{q}"
    if q == 0:
        return f"{sign}\\frac{{{r}}}{{{x.denominator}}}"
    return f"{sign}{q}\\frac{{{r}}}{{{x.denominator}}}"


def _mixed_typed(x: Fraction) -> str:
    sign = "-" if x < 0 else ""
    x = abs(x)
    q, r = divmod(x.numerator, x.denominator)
    if r == 0:
        return f"{sign}{q}"
    if q == 0:
        return f"{sign}{r}/{x.denominator}"
    return f"{sign}{q} {r}/{x.denominator}"


def _frac_str(x: Fraction) -> str:
    return str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}"


def _nad(value: str) -> str:
    return f"{math(value)} Namibian dollars"


def _hours(t: Fraction) -> str:
    return f"{math(_dec_str(t))} hour" if t == 1 else f"{math(_dec_str(t))} hours"


def _pct(p: Any) -> str:
    return math(f"{p}\\%")


# --------------------------------------------------------------------------
# Common problem assembly
# --------------------------------------------------------------------------


@dataclass
class _Spec:
    skill: str
    question: str
    answer: str  # display text
    typed: str  # what a learner types for the right answer
    expected: List[str]
    answer_type: str
    correct_key: Any
    steps: List[Tuple[str, str]]
    # (error code, display answer, typed text, key)
    dists: List[Tuple[str, str, str, Any]]
    machine: Dict[str, Any]
    rounding: Optional[str] = None
    digits: int = 3
    form: Optional[str] = None  # e.g. "prime_factors": a form the marker must enforce


def _numeric_spec(
    skill: str,
    question: str,
    value: Fraction,
    steps: Sequence[Tuple[str, str]],
    dists: Sequence[Tuple[str, Fraction]],
    machine: Dict[str, Any],
    *,
    mode: Optional[str] = None,
    digits: int = 3,
    suffix: str = "",
    answer_type: Optional[str] = None,
) -> _Spec:
    typed = _typed_number(value, mode, digits)
    if answer_type is None:
        answer_type = "number_exact" if mode is None else "number_rounded"
    dlist = []
    for code, dv in dists:
        dt = _typed_number(dv, mode, digits, loose=True)
        dlist.append((code, math(dt + suffix), dt, _key(Fraction(dt) if mode is None else dv, mode, digits)))
    return _Spec(
        skill=skill,
        question=question,
        answer=math(typed + suffix),
        typed=typed,
        expected=[typed],
        answer_type=answer_type,
        correct_key=_key(value, mode, digits),
        steps=list(steps),
        dists=dlist,
        machine=dict(machine, answer=typed),
        rounding=mode,
        digits=digits,
    )


def _fraction_spec(
    skill: str,
    question: str,
    value: Fraction,
    steps: Sequence[Tuple[str, str]],
    dists: Sequence[Tuple[str, Fraction]],
    machine: Dict[str, Any],
    *,
    mixed: bool = True,
) -> _Spec:
    typed = _mixed_typed(value) if mixed else _frac_str(value)
    show = _mixed_latex if mixed else (lambda f: number_latex(f))
    dlist = []
    for code, dv in dists:
        dt = _mixed_typed(dv) if mixed else _frac_str(dv)
        dlist.append((code, math(show(dv)), dt, dv))
    expected = [typed] if typed == _frac_str(value) else [typed, _frac_str(value)]
    return _Spec(
        skill=skill,
        question=question,
        answer=math(show(value)),
        typed=typed,
        expected=expected,
        answer_type="number_exact",
        correct_key=value,
        steps=list(steps),
        dists=dlist,
        machine=dict(machine, answer=typed),
        form="mixed_number" if skill == "improper_to_mixed" else "simplest_fraction",
    )


def _assemble(generator: MathGenerator, seed: int, level: int, spec: _Spec) -> GeneratedProblem:
    correct = spec.correct_key
    seen_keys: List[Any] = []
    seen_answers = {spec.answer}
    distractors: List[Distractor] = []
    for code, display, typed, key in spec.dists:
        if isinstance(correct, (set, frozenset)):
            same = key in correct
        else:
            same = key == correct
        if same or key in seen_keys or display in seen_answers:
            continue
        seen_keys.append(key)
        seen_answers.add(display)
        note = generator.error_notes[spec.skill][code]
        distractors.append(Distractor(display, code, note, typed=typed))
        if len(distractors) == _MAX_DISTRACTORS:
            break
    _require(bool(spec.steps), "no model steps")
    marking: Dict[str, Any] = {
        "answer_type": spec.answer_type,
        "expected": list(spec.expected),
        "typed": spec.typed,
    }
    if spec.rounding:
        marking["rounding"] = spec.rounding
        marking["digits"] = spec.digits
    if spec.form:
        marking["form"] = spec.form
    return GeneratedProblem(
        generator_id=generator.generator_id,
        generator_version=generator.version,
        seed=seed,
        level=level,
        skill=spec.skill,
        question=spec.question,
        answer=spec.answer,
        distractors=tuple(distractors),
        machine=spec.machine,
        steps=tuple(Step(d, v) for d, v in spec.steps),
        marking=marking,
    )


class _FamilyGenerator(MathGenerator):
    """Shared ``_build``: try the level's builder until it yields a clean problem."""

    builders: Dict[int, Callable[[SeededRandom], _Spec]] = {}

    def _build(self, rng: SeededRandom, seed: int, level: int) -> GeneratedProblem:
        builder = self.builders[level]
        for _ in range(_MAX_ATTEMPTS):
            try:
                spec = builder(rng)
            except _Retry:
                continue
            return _assemble(self, seed, level, spec)
        raise GeneratorError(f"{self.generator_id} level {level}: no clean problem found")


# --------------------------------------------------------------------------
# Shared Namibian contexts
# --------------------------------------------------------------------------

_ITEMS = (
    "pair of school shoes",
    "school backpack",
    "football",
    "scientific calculator",
    "bicycle",
    "jacket",
    "radio",
    "microwave oven",
    "bag of maize meal",
    "cellphone cover",
)
_SHOPS = (
    "Kudu Stationers in Windhoek",
    "Harbour Stores in Walvis Bay",
    "Selma’s stall at Oshakati market",
    "Dune Stores in Swakopmund",
    "Karoo Traders in Keetmanshoop",
    "River Stores in Rundu",
)
_NAMES = ("Ndapewa", "Tuli", "Hileni", "Johannes", "Selma", "Petrus", "Kaleb", "Maria", "Aina", "Sakeus")


def _pick_names(rng: SeededRandom, count: int) -> List[str]:
    pool = list(_NAMES)
    out = []
    for _ in range(count):
        out.append(pool.pop(rng.randint(0, len(pool) - 1)))
    return out


# ==========================================================================
# 15795 Advanced Percentage Calculations
# ==========================================================================

PCT_NOTES: Dict[str, Dict[str, str]] = {
    "percentage_change_amount": {
        "amount_only": "found the percentage of the amount but did not add it to (or subtract it from) the original",
        "wrong_direction": "added the percentage when the price goes down, or subtracted it when the price goes up",
        "percent_as_number": "added or subtracted the percentage as a plain number instead of a percentage of the amount",
    },
    "percentage_remaining": {
        "sold_amount": "found the number that were sold instead of the number that remain",
        "percent_as_number": "subtracted the percentage as a plain number of items",
    },
    "profit_loss_percentage": {
        "of_selling_price": "divided the profit (or loss) by the selling price instead of the cost price",
        "amount_not_percentage": "gave the profit (or loss) in dollars instead of as a percentage",
        "not_multiplied_by_100": "divided the profit (or loss) by the cost price but did not multiply by 100",
    },
    "reverse_percentage": {
        "forward_percentage": "worked out the percentage change of the given price instead of undoing it",
        "opposite_change": "took the percentage off (or added it to) the given price instead of dividing by the multiplier",
        "percent_as_number": "added or subtracted the percentage as a plain number",
    },
    "percentage_change": {
        "divided_by_new": "divided the change by the new value instead of the original value",
        "ratio_not_change": "found the new value as a percentage of the original instead of the change",
        "difference_only": "gave the difference between the two values and did not convert it to a percentage",
    },
    "express_as_percentage": {
        "inverted": "divided the whole by the part instead of the part by the whole",
        "not_multiplied_by_100": "divided the part by the whole but did not multiply by 100",
        "difference_used": "worked with the difference between the whole and the part instead of the part",
    },
    "compound_interest": {
        "simple_interest": "used simple interest, the same amount added each year, instead of compounding",
        "one_year_only": "applied the percentage for one year only",
        "interest_only": "gave the interest earned instead of the total amount",
        "amount_not_interest": "gave the total amount instead of just the interest earned",
        "compound_growth": "increased the value each year when the value is falling",
        "linear_decrease": "reduced by the same amount each year instead of compounding the decrease",
    },
}

PCT_LEVEL_SKILLS: Dict[int, Tuple[str, ...]] = {
    1: ("percentage_change_amount", "percentage_remaining"),
    2: ("profit_loss_percentage",),
    3: ("reverse_percentage",),
    4: ("percentage_change", "express_as_percentage"),
    5: ("compound_interest",),
}


def _pct_l1(rng: SeededRandom) -> _Spec:
    kind = rng.choice(("increase", "decrease", "remaining"))
    if kind == "remaining":
        n = rng.randint(2, 60) * 20
        p = rng.choice(tuple(range(15, 95, 5)))
        sold = Fraction(n * p, 100)
        left = Fraction(n) - sold
        _require(left == Fraction(n * (100 - p), 100) and left.denominator == 1, "remaining count")
        item = rng.choice(("copies of a school magazine", "tickets for a school concert", "learner diaries"))
        question = (
            f"A school printed {math(str(n))} {item}. {_pct(p)} of them were sold. "
            f"Calculate how many were not sold."
        )
        steps = [
            (f"Find {p}% of {n}", _frac_str(sold)),
            (f"Subtract from {n}", _frac_str(left)),
        ]
        dists = [
            ("sold_amount", sold),
            ("percent_as_number", Fraction(n - p)),
        ]
        return _numeric_spec(
            "percentage_remaining", question, left, steps, dists,
            {"task": "percentage_remaining", "total": n, "percent": p},
        )
    price = rng.randint(10, 90) * 10
    p = rng.choice((5, 8, 10, 12, 15, 20, 25, 30, 35, 40))
    item = rng.choice(_ITEMS)
    shop = rng.choice(_SHOPS)
    amount = Fraction(price * p, 100)
    if kind == "increase":
        new = Fraction(price) + amount
        _require(new == Fraction(price * (100 + p), 100), "increase")
        question = (
            f"The price of a {item} at {shop} is {_nad(str(price))}. "
            f"The price increases by {_pct(p)}. Find the new price."
        )
        dists = [
            ("amount_only", amount),
            ("wrong_direction", Fraction(price) - amount),
            ("percent_as_number", Fraction(price + p)),
        ]
        steps = [
            (f"Find {p}% of {price}", _dec_str(amount)),
            (f"Add to {price}", _dec_str(new)),
        ]
    else:
        new = Fraction(price) - amount
        _require(new == Fraction(price * (100 - p), 100), "decrease")
        question = (
            f"{shop[0].upper() + shop[1:]} reduces the price of a {item} from {_nad(str(price))} "
            f"by {_pct(p)}. Find the new price."
        )
        dists = [
            ("amount_only", amount),
            ("wrong_direction", Fraction(price) + amount),
            ("percent_as_number", Fraction(price - p)),
        ]
        steps = [
            (f"Find {p}% of {price}", _dec_str(amount)),
            (f"Subtract from {price}", _dec_str(new)),
        ]
    return _numeric_spec(
        "percentage_change_amount", question, new, steps, dists,
        {"task": kind, "amount": price, "percent": p},
    )


def _pct_l2(rng: SeededRandom) -> _Spec:
    cost = rng.randint(10, 200) * 10
    kind = rng.choice(("profit", "loss"))
    diff = rng.randint(max(1, cost // 20 // 10), max(2, cost * 2 // 5 // 10)) * 10
    sell = cost + diff if kind == "profit" else cost - diff
    _require(sell > 0 and diff > 0, "selling price")
    pct = Fraction(diff * 100, cost)
    _require(pct == Fraction(abs(sell - cost) * 100, cost), "percentage")
    item = rng.choice(_ITEMS)
    shop = rng.choice(_SHOPS)
    question = (
        f"{shop[0].upper() + shop[1:]} buys a {item} for {_nad(str(cost))} and sells it for "
        f"{_nad(str(sell))}. Calculate the percentage {kind}. "
        f"Give your answer correct to 3 significant figures."
    )
    typed = _typed_number(pct, "sig_figs", 3)
    steps = [
        (f"Find the {kind}", str(diff)),
        (f"Divide by the cost price and multiply by 100", f"{diff}/{cost}*100"),
        ("Round to 3 significant figures", typed),
    ]
    dists = [
        ("of_selling_price", Fraction(diff * 100, sell)),
        ("amount_not_percentage", Fraction(diff)),
        ("not_multiplied_by_100", Fraction(diff, cost)),
    ]
    return _numeric_spec(
        "profit_loss_percentage", question, pct, steps, dists,
        {"task": kind, "cost": cost, "selling": sell},
        mode="sig_figs", digits=3, suffix="\\%",
    )


def _pct_l3(rng: SeededRandom) -> _Spec:
    original = rng.randint(4, 80) * 25
    p = rng.choice((5, 8, 10, 12, 15, 20, 25, 30, 40))
    kind = rng.choice(("increase", "decrease"))
    mult = Fraction(100 + p if kind == "increase" else 100 - p, 100)
    given = Fraction(original) * mult
    _dec_str(given)
    _require(given / mult == original, "reverse percentage")
    item = rng.choice(_ITEMS)
    if kind == "increase":
        question = (
            f"After an increase of {_pct(p)}, the price of a {item} is {_nad(_dec_str(given))}. "
            f"Calculate the original price."
        )
        opposite = Fraction(100 - p, 100)
        forward = Fraction(100 + p, 100)
        plain = given - p
    else:
        question = (
            f"A {item} is sold in a sale for {_nad(_dec_str(given))}, "
            f"which is a reduction of {_pct(p)} on the original price. "
            f"Calculate the original price."
        )
        opposite = Fraction(100 + p, 100)
        forward = Fraction(100 - p, 100)
        plain = given + p
    mult_text = _dec_str(mult)
    steps = [
        (f"The given price is {mult_text} times the original price", mult_text),
        ("Divide by the multiplier", f"{_dec_str(given)}/{mult_text}"),
        ("Original price", str(original)),
    ]
    dists = [
        ("forward_percentage", given * forward),
        ("opposite_change", given * opposite),
        ("percent_as_number", plain),
    ]
    return _numeric_spec(
        "reverse_percentage", question, Fraction(original), steps, dists,
        {"task": f"reverse_{kind}", "given": _dec_str(given), "percent": p},
    )


def _pct_l4(rng: SeededRandom) -> _Spec:
    kind = rng.choice(("change", "change", "express"))
    if kind == "express":
        whole = rng.randint(20, 200)
        part = rng.randint(5, whole - 1)
        pct = Fraction(part * 100, whole)
        who = rng.choice(_NAMES)
        question = (
            f"{who} scored {math(str(part))} marks out of {math(str(whole))} in a test. "
            f"Express {who}'s score as a percentage of the total marks. "
            f"Give your answer correct to 3 significant figures."
        )
        typed = _typed_number(pct, "sig_figs", 3)
        steps = [
            ("Write the score as a fraction of the total", f"{part}/{whole}"),
            ("Multiply by 100", f"{part}/{whole}*100"),
            ("Round to 3 significant figures", typed),
        ]
        dists = [
            ("inverted", Fraction(whole * 100, part)),
            ("not_multiplied_by_100", Fraction(part, whole)),
            ("difference_used", Fraction((whole - part) * 100, whole)),
        ]
        return _numeric_spec(
            "express_as_percentage", question, pct, steps, dists,
            {"task": "express_as_percentage", "part": part, "whole": whole},
            mode="sig_figs", digits=3, suffix="\\%",
        )
    old = rng.randint(20, 300)
    change = rng.randint(3, max(4, old // 2))
    direction = rng.choice(("decrease", "increase"))
    new = old - change if direction == "decrease" else old + change
    _require(new > 0 and new != old, "new value")
    pct = Fraction(change * 100, old)
    unit = rng.choice(("bags of cement", "tickets", "bottles of water", "phone cases"))
    wk = rng.randint(1, 8)
    question = (
        f"Kudu Stores sold {math(str(old))} {unit} in week {wk} and {math(str(new))} {unit} in week {wk + 1}. "
        f"Calculate the percentage {direction} in sales from week {wk} to week {wk + 1}. "
        f"Give your answer correct to 3 significant figures."
    )
    typed = _typed_number(pct, "sig_figs", 3)
    steps = [
        ("Find the change", str(change)),
        ("Divide by the original value", f"{change}/{old}"),
        ("Multiply by 100 and round to 3 significant figures", typed),
    ]
    dists = [
        ("divided_by_new", Fraction(change * 100, new)),
        ("ratio_not_change", Fraction(new * 100, old)),
        ("difference_only", Fraction(change)),
    ]
    return _numeric_spec(
        "percentage_change", question, pct, steps, dists,
        {"task": f"percentage_{direction}", "old": old, "new": new},
        mode="sig_figs", digits=3, suffix="\\%",
    )


def _pct_l5(rng: SeededRandom) -> _Spec:
    principal = rng.randint(2, 40) * 500
    rate = rng.choice((3, 4, 5, 6, 7, 8, 9, 10, 12, 15))
    years = rng.randint(2, 5)
    kind = rng.choice(("amount", "interest", "depreciation"))
    mult = Fraction(100 + rate, 100)
    dep = Fraction(100 - rate, 100)
    growth = Fraction(principal) * mult**years
    decay = Fraction(principal) * dep**years
    simple = Fraction(principal) * (1 + Fraction(rate * years, 100))
    linear = Fraction(principal) * (1 - Fraction(rate * years, 100))
    bank = rng.choice(("a bank in Windhoek", "a savings account at a Namibian bank", "a building society in Walvis Bay"))
    if kind == "amount":
        question = (
            f"{_nad(str(principal))} is invested in {bank} at {_pct(rate)} per year compound interest. "
            f"Calculate the total amount after {years} years. Give your answer correct to 2 decimal places."
        )
        value = growth
        mult_text = _dec_str(mult)
        steps = [
            ("Multiplier for one year", mult_text),
            (f"Multiply the investment by the multiplier {years} times", f"{principal}*{mult_text}^{years}"),
            ("Round to 2 decimal places", _fmt_money_dp(value)),
        ]
        dists = [
            ("simple_interest", simple),
            ("one_year_only", Fraction(principal) * mult),
            ("interest_only", growth - principal),
        ]
        skill_machine = {"task": "compound_amount"}
    elif kind == "interest":
        question = (
            f"{_nad(str(principal))} is invested in {bank} at {_pct(rate)} per year compound interest. "
            f"Calculate the interest earned after {years} years. Give your answer correct to 2 decimal places."
        )
        value = growth - principal
        mult_text = _dec_str(mult)
        steps = [
            ("Multiplier for one year", mult_text),
            ("Total amount after the years", f"{principal}*{mult_text}^{years}"),
            ("Subtract the original investment and round to 2 decimal places", _fmt_money_dp(value)),
        ]
        dists = [
            ("amount_not_interest", growth),
            ("simple_interest", simple - principal),
            ("one_year_only", Fraction(principal * rate, 100)),
        ]
        skill_machine = {"task": "compound_interest"}
    else:
        item = rng.choice(("car", "tractor", "delivery van", "minibus"))
        question = (
            f"Kudu Traders buys a {item} for {_nad(str(principal))}. Its value falls by {_pct(rate)} "
            f"each year. Calculate its value after {years} years. "
            f"Give your answer correct to 2 decimal places."
        )
        value = decay
        mult_text = _dec_str(dep)
        steps = [
            ("Multiplier for one year", mult_text),
            (f"Multiply the value by the multiplier {years} times", f"{principal}*{mult_text}^{years}"),
            ("Round to 2 decimal places", _fmt_money_dp(value)),
        ]
        dists = [
            ("linear_decrease", linear),
            ("compound_growth", growth),
            ("one_year_only", Fraction(principal) * dep),
        ]
        skill_machine = {"task": "depreciation"}
    _require(value > 0, "value")
    machine = dict(skill_machine, principal=principal, rate=rate, years=years)
    return _numeric_spec(
        "compound_interest", question, value, steps, dists, machine,
        mode="decimal_places", digits=2,
    )


class AdvancedPercentagesGenerator(_FamilyGenerator):
    generator_id = "nssco_advanced_percentages"
    version = 1
    levels = (1, 2, 3, 4, 5)
    level_skills = PCT_LEVEL_SKILLS
    error_notes = PCT_NOTES
    builders = {1: _pct_l1, 2: _pct_l2, 3: _pct_l3, 4: _pct_l4, 5: _pct_l5}


# ==========================================================================
# 15794 Fractions, Decimals, Percentages, Ordering
# ==========================================================================

FDP_NOTES: Dict[str, Dict[str, str]] = {
    "fraction_to_decimal": {
        "numerator_after_point": "wrote the numerator straight after the decimal point",
        "inverted_division": "divided the denominator by the numerator",
        "place_value_slip": "divided correctly but put the decimal point one place out",
    },
    "decimal_to_fraction": {
        "over_ten": "wrote the digits over 10 instead of over 100",
        "over_thousand": "wrote the digits over 1000 instead of over 100",
        "inverted": "turned the fraction upside down",
    },
    "fraction_to_percentage": {
        "no_scaling": "divided the numerator by the denominator and stopped, without multiplying by 100",
        "times_ten": "multiplied by 10 instead of by 100",
        "inverted": "divided the denominator by the numerator before multiplying by 100",
    },
    "percentage_to_fraction": {
        "over_ten": "wrote the percentage over 10 instead of over 100",
        "over_thousand": "wrote the percentage over 1000 instead of over 100",
        "inverted": "turned the fraction upside down",
    },
    "improper_to_mixed": {
        "swapped_parts": "swapped the remainder and the denominator in the fraction part",
        "remainder_off_by_one": "made an arithmetic slip in the remainder",
    },
    "equivalent_fraction": {
        "added_not_multiplied": "added the same number to the top as was added to the bottom instead of multiplying",
        "copied_denominator": "copied the new denominator into the numerator",
    },
    "fraction_of_quantity": {
        "inverted_fraction": "used the fraction upside down (divided by the numerator and multiplied by the denominator)",
        "one_part_only": "divided by the denominator but did not multiply by the numerator",
        "multiplied_only": "multiplied by the numerator and did not divide by the denominator",
    },
    "recurring_decimal_to_fraction": {
        "over_ten_power": "wrote the repeating digits over 10 or 100 instead of over 9 or 99",
        "reciprocal": "wrote the fraction upside down",
        "one_over_digit": "wrote 1 over the repeating digit",
        "over_ten_power_alt": "wrote the repeating digits over 10 instead of over 99",
    },
    "order_fractions": {
        "descending": "ordered them from largest to smallest instead of smallest to largest",
        "by_numerator": "ordered the fractions by the size of the numerators only",
        "by_denominator": "ordered the fractions by the size of the denominators only",
    },
    "pick_from_mixed_list": {
        "other_item": "compared the numbers as written, ignoring that some are fractions or percentages",
    },
    "compare_with_symbol": {
        "wrong_symbol": "compared the two numbers incorrectly and chose the wrong symbol",
    },
    "fraction_arithmetic": {
        "tops_and_bottoms": "added the numerators and added the denominators",
        "tops_over_product": "added the numerators and multiplied the denominators",
        "wholes_separate": "subtracted the whole numbers and the fractions separately, always taking the smaller from the larger",
        "tops_and_bottoms_sub": "subtracted the numerators and subtracted the denominators",
        "kept_first_denominator": "multiplied the numerators but kept the first denominator",
        "common_denominator_tops": "found a common denominator and multiplied only the numerators",
        "multiplied_instead": "multiplied by the second fraction instead of dividing by it",
        "inverted_first": "turned the first fraction upside down instead of the second",
    },
    "whole_from_fraction": {
        "fraction_of_part": "found the fraction of the given amount instead of the whole",
        "one_part_only": "divided the amount by the numerator and did not multiply by the denominator",
        "inverted": "divided by the denominator and multiplied by the numerator",
    },
    "successive_fractions": {
        "second_share_only": "gave the second share instead of what is left",
        "second_fraction_of_total": "took the second fraction of the whole amount instead of the remainder",
        "percent_of_remainder": "found the percentage of the remainder instead of the whole",
        "percent_inverted": "divided the total by the amount left",
    },
}

FDP_LEVEL_SKILLS: Dict[int, Tuple[str, ...]] = {
    1: ("fraction_to_decimal", "decimal_to_fraction", "fraction_to_percentage", "percentage_to_fraction"),
    2: ("improper_to_mixed", "equivalent_fraction", "fraction_of_quantity", "recurring_decimal_to_fraction"),
    3: ("order_fractions", "pick_from_mixed_list", "compare_with_symbol"),
    4: ("fraction_arithmetic",),
    5: ("whole_from_fraction", "successive_fractions"),
}


def _simplest(n: int, d: int) -> Fraction:
    return Fraction(n, d)


def _fdp_l1(rng: SeededRandom) -> _Spec:
    kind = rng.choice(("frac_to_dec", "dec_to_frac", "frac_to_pct", "pct_to_frac"))
    if kind == "frac_to_dec":
        d = rng.choice((4, 5, 8, 20, 25, 40, 50))
        n = rng.randint(1, d - 1)
        if gcd(n, d) != 1:
            raise _Retry
        value = Fraction(n, d)
        question = ''.join(['Write ', format(math(''.join(['\\frac{', format(n, ''), '}{', format(d, ''), '}'])), ''), ' as a decimal.'])
        typed = _dec_str(value)
        steps = [("Divide the numerator by the denominator", f"{n}/{d}"), ("Decimal", typed)]
        dists = [
            ("numerator_after_point", Fraction(n, 10 ** len(str(n)))),
            ("inverted_division", Fraction(d, n)),
            ("place_value_slip", value / 10),
        ]
        return _numeric_spec("fraction_to_decimal", question, value, steps, dists, {"task": "fraction_to_decimal", "n": n, "d": d})
    if kind == "dec_to_frac":
        k = rng.randint(5, 95)
        if k % 10 == 0:
            raise _Retry
        value = Fraction(k, 100)
        question = f"Write {math(_dec_str(value))} as a fraction in its simplest form."
        steps = [("Write over 100", f"{k}/100"), ("Simplify", _frac_str(value))]
        dists = [
            ("over_ten", Fraction(k, 10)),
            ("over_thousand", Fraction(k, 1000)),
            ("inverted", Fraction(100, k)),
        ]
        return _fraction_spec("decimal_to_fraction", question, value, steps, dists, {"task": "decimal_to_fraction", "decimal": _dec_str(value)}, mixed=False)
    if kind == "frac_to_pct":
        d = rng.choice((2, 4, 5, 8, 10, 20, 25, 40, 50))
        n = rng.randint(1, d - 1)
        if gcd(n, d) != 1:
            raise _Retry
        value = Fraction(n * 100, d)
        question = ''.join(['Write ', format(math(''.join(['\\frac{', format(n, ''), '}{', format(d, ''), '}'])), ''), ' as a percentage.'])
        steps = [("Multiply the fraction by 100", f"{n}/{d}*100"), ("Percentage", _dec_str(value))]
        dists = [
            ("no_scaling", Fraction(n, d)),
            ("times_ten", Fraction(n * 10, d)),
            ("inverted", Fraction(d * 100, n)),
        ]
        return _numeric_spec("fraction_to_percentage", question, value, steps, dists, {"task": "fraction_to_percentage", "n": n, "d": d}, suffix="\\%")
    p = rng.choice(tuple(range(5, 100, 5)))
    value = Fraction(p, 100)
    question = f"Write {_pct(p)} as a fraction in its simplest form."
    steps = [("Write over 100", f"{p}/100"), ("Simplify", _frac_str(value))]
    dists = [
        ("over_ten", Fraction(p, 10)),
        ("over_thousand", Fraction(p, 1000)),
        ("inverted", Fraction(100, p)),
    ]
    return _fraction_spec("percentage_to_fraction", question, value, steps, dists, {"task": "percentage_to_fraction", "percent": p}, mixed=False)


def _fdp_l2(rng: SeededRandom) -> _Spec:
    kind = rng.choice(("mixed", "equivalent", "of_quantity", "recurring"))
    if kind == "mixed":
        d = rng.randint(3, 12)
        q = rng.randint(2, 9)
        r = rng.randint(1, d - 1)
        if gcd(r, d) != 1:
            raise _Retry
        n = q * d + r
        value = Fraction(n, d)
        _require(_mixed_typed(value) == f"{q} {r}/{d}", "mixed number")
        question = ''.join(['Write ', format(math(''.join(['\\frac{', format(n, ''), '}{', format(d, ''), '}'])), ''), ' as a mixed number.'])
        steps = [("Divide the numerator by the denominator", f"{q} remainder {r}"), ("Mixed number", _mixed_typed(value))]
        dists = [
            ("swapped_parts", Fraction(q * r + d, r)),
            ("remainder_off_by_one", Fraction(q * d + r + 1, d)),
        ]
        spec = _fraction_spec("improper_to_mixed", question, value, steps, dists, {"task": "improper_to_mixed", "n": n, "d": d})
        # the swapped-parts mistake is typed as "q d/r"
        spec.dists[0] = ("swapped_parts", math(f"{q}\\frac{{{d}}}{{{r}}}"), f"{q} {d}/{r}", Fraction(q) + Fraction(d, r))
        return spec
    if kind == "equivalent":
        b = rng.randint(3, 9)
        a = rng.randint(1, b - 1)
        if gcd(a, b) != 1:
            raise _Retry
        k = rng.randint(2, 9)
        big = b * k
        value = Fraction(a * k)
        question = (
            ''.join(['Find the missing number: ', format(math(''.join(['\\frac{', format(a, ''), '}{', format(b, ''), '} = \\frac{\\square}{', format(big, ''), '}'])), '')])
        )
        steps = [("Find what the denominator was multiplied by", str(k)), ("Multiply the numerator by the same number", str(a * k))]
        dists = [
            ("added_not_multiplied", Fraction(a + (big - b))),
            ("copied_denominator", Fraction(big)),
        ]
        return _numeric_spec("equivalent_fraction", question, value, steps, dists, {"task": "equivalent_fraction", "a": a, "b": b, "big": big})
    if kind == "of_quantity":
        d = rng.choice((3, 4, 5, 6, 8, 10))
        n = rng.randint(1, d - 1)
        if gcd(n, d) != 1:
            raise _Retry
        q = d * rng.randint(100 // d + 1, 900 // d)
        value = Fraction(q * n, d)
        thing = rng.choice(("cupcakes", "learners in a school", "bags of maize meal", "tickets"))
        question = ''.join(['Selma’s shop has ', format(math(str(q)), ''), ' ', format(thing, ''), '. Find ', format(math(''.join(['\\frac{', format(n, ''), '}{', format(d, ''), '}'])), ''), ' of the ', format(thing, ''), '.'])
        steps = [("Divide by the denominator", _frac_str(Fraction(q, d))), ("Multiply by the numerator", _frac_str(value))]
        dists = [
            ("inverted_fraction", Fraction(q * d, n)),
            ("one_part_only", Fraction(q, d)),
            ("multiplied_only", Fraction(q * n)),
        ]
        return _numeric_spec("fraction_of_quantity", question, value, steps, dists, {"task": "fraction_of_quantity", "quantity": q, "n": n, "d": d})
    # recurring decimals
    if rng.chance(1, 2):
        digit = rng.randint(1, 8)
        value = Fraction(digit, 9)
        shown = f"0.\\dot{{{digit}}}"
        steps = [("Let x be the recurring decimal; multiply by 10 and subtract", f"9x={digit}"), ("Fraction", _frac_str(value))]
        dists = [
            ("over_ten_power", Fraction(digit, 10)),
            ("reciprocal", Fraction(9, digit)),
            ("one_over_digit", Fraction(1, digit)),
        ]
    else:
        a, b = rng.randint(1, 9), rng.randint(0, 9)
        two = 10 * a + b
        if two % 11 == 0:
            raise _Retry
        value = Fraction(two, 99)
        shown = f"0.\\dot{{{a}}}\\dot{{{b}}}"
        steps = [("Let x be the recurring decimal; multiply by 100 and subtract", f"99x={two}"), ("Fraction", _frac_str(value))]
        dists = [
            ("over_ten_power", Fraction(two, 100)),
            ("reciprocal", Fraction(99, two)),
            ("over_ten_power_alt", Fraction(two, 10)),
        ]
    question = f"Write {math(shown)} as a fraction in its simplest form."
    return _fraction_spec("recurring_decimal_to_fraction", question, value, steps, dists, {"task": "recurring_to_fraction", "shown": shown}, mixed=False)


_FRACTION_DENOMS = (2, 3, 4, 5, 6, 8, 10, 12, 15, 20)


def _l3_order(rng: SeededRandom) -> _Spec:
    fractions: List[Fraction] = []
    attempts = 0
    while len(fractions) < 3:
        attempts += 1
        if attempts > 60:
            raise _Retry
        d = rng.choice(_FRACTION_DENOMS)
        n = rng.randint(1, d - 1)
        f = Fraction(n, d)
        if f.denominator != d or f in fractions:  # keep the printed form simplest
            continue
        fractions.append(f)
    if len({f.denominator for f in fractions}) < 2:
        raise _Retry
    shown = fractions[:]
    ascending = sorted(fractions)
    typed = ", ".join(_frac_str(f) for f in ascending)

    def latex(f: Fraction) -> str:
        return f"\\frac{{{f.numerator}}}{{{f.denominator}}}"

    question = (
        "Write these fractions in order of size, starting with the smallest: "
        + ", ".join(math(latex(f)) for f in shown)
        + "."
    )
    by_num = sorted(fractions, key=lambda f: (f.numerator, f.denominator))
    by_den = sorted(fractions, key=lambda f: (-f.denominator, f.numerator))
    dists = []
    for code, order in (
        ("descending", list(reversed(ascending))),
        ("by_numerator", by_num),
        ("by_denominator", by_den),
    ):
        text = ", ".join(_frac_str(f) for f in order)
        dists.append((code, ", ".join(math(latex(f)) for f in order), text, text))
    steps = [
        ("Write each fraction over a common denominator", ", ".join(_frac_str(f) for f in shown)),
        ("Order the fractions", typed),
    ]
    return _Spec(
        skill="order_fractions",
        question=question,
        answer=", ".join(math(latex(f)) for f in ascending),
        typed=typed,
        expected=[typed],
        answer_type="sequence",
        correct_key=typed,
        steps=steps,
        dists=dists,
        machine={"task": "order_fractions", "shown": [_frac_str(f) for f in shown], "ascending": [_frac_str(f) for f in ascending]},
    )


def _literal_value(text: str) -> Fraction:
    """The number the marker reads from a list item (it drops % and keeps the rest)."""
    t = text.replace("%", "")
    return Fraction(t)


def _l3_pick(rng: SeededRandom) -> _Spec:
    items: List[Tuple[str, Fraction, str]] = []  # (listed text, true value, latex)
    values: List[Fraction] = []
    for _ in range(40):
        if len(items) == 5:
            break
        style = rng.choice(("decimal", "fraction", "percent"))
        if style == "decimal":
            v = Fraction(rng.randint(20, 90), 100)
            text, latex = _dec_str(v), _dec_str(v)
        elif style == "fraction":
            d = rng.choice((3, 4, 5, 6, 8, 9, 12, 16, 20, 25))
            n = rng.randint(max(1, d // 5), d - 1)
            v = Fraction(n, d)
            if v.denominator != d:
                continue
            text, latex = f"{n}/{d}", f"\\frac{{{n}}}{{{d}}}"
        else:
            tenths = rng.randint(200, 900)
            v = Fraction(tenths, 1000)
            p = v * 100
            text = _dec_str(p) + "%"
            latex = _dec_str(p) + "\\%"
        if any(abs(v - w) < Fraction(1, 50) for w in values):
            continue
        values.append(v)
        items.append((text, v, latex))
    if len(items) < 5:
        raise _Retry
    rng_order = items[:]
    want_largest = rng.chance(1, 2)
    target = max(items, key=lambda t: t[1]) if want_largest else min(items, key=lambda t: t[1])
    word = "largest" if want_largest else "smallest"
    question = (
        "Here is a list of numbers: " + ", ".join(math(i[2]) for i in rng_order) + ". "
        f"Write down the {word} number in the list."
    )
    text, v, latex = target
    accepted = [text]
    try:
        eq = _dec_str(v)
        if eq not in accepted:
            accepted.append(eq)
    except _Retry:
        pass
    accepted_lits = {_literal_value(a) for a in accepted}
    dists = []
    for t, tv, tl in items:
        if t == text:
            continue
        dists.append(("other_item", math(tl), t, _literal_value(t)))
    steps = [
        ("Write every number as a decimal", ", ".join(_dec_str(i[1]) if i[1].denominator in (1, 2, 4, 5, 8, 10, 20, 25, 40, 50, 100, 125, 200, 250, 500, 1000) else _frac_str(i[1]) for i in rng_order)),
        (f"Pick the {word}", text),
    ]
    return _Spec(
        skill="pick_from_mixed_list",
        question=question,
        answer=math(latex),
        typed=text,
        expected=accepted,
        answer_type="number_exact",
        correct_key=frozenset(accepted_lits),
        steps=steps,
        dists=dists,
        machine={"task": f"pick_{word}", "items": [i[0] for i in rng_order]},
    )


def _l3_symbol(rng: SeededRandom) -> _Spec:
    style = rng.choice(("fraction_decimal", "negative_fractions", "fraction_percent"))
    if style == "negative_fractions":
        a, b = rng.randint(2, 12), rng.randint(2, 12)
        if a == b:
            raise _Retry
        x, y = Fraction(-1, a), Fraction(-1, b)
        left, right = f"-\\frac{{1}}{{{a}}}", f"-\\frac{{1}}{{{b}}}"
        decs = (_frac_str(x), _frac_str(y))
    elif style == "fraction_decimal":
        d = rng.choice((4, 5, 8, 20, 25))
        n = rng.randint(1, d - 1)
        x = Fraction(n, d)
        if x.denominator != d:
            raise _Retry
        if rng.chance(1, 4):
            y = x
        else:
            y = Fraction(rng.randint(1, 99), 100)
        left, right = f"\\frac{{{n}}}{{{d}}}", _dec_str(y)
        decs = (_dec_str(x), _dec_str(y))
    else:
        d = rng.choice((4, 5, 8, 10, 20, 25))
        n = rng.randint(1, d - 1)
        x = Fraction(n, d)
        if x.denominator != d:
            raise _Retry
        pct = x * 100 if rng.chance(1, 4) else Fraction(rng.randint(5, 95))
        y = pct / 100
        left, right = f"\\frac{{{n}}}{{{d}}}", _dec_str(pct) + "\\%"
        decs = (_dec_str(x), _dec_str(y))
    symbol = ">" if x > y else "<" if x < y else "="
    question = (
        ''.join(['Write ', format(math('>'), ''), ', ', format(math('<'), ''), ' or ', format(math('='), ''), ' in the box to make the statement correct: ', format(math(left + ' \\; \\square \\; ' + right), '')])
    )
    others = [s for s in (">", "<", "=") if s != symbol]
    dists = [("wrong_symbol", math(s), s, s) for s in others]
    steps = [("Write both numbers in the same form", f"{decs[0]} and {decs[1]}"), ("Compare", symbol)]
    return _Spec(
        skill="compare_with_symbol",
        question=question,
        answer=math(symbol),
        typed=symbol,
        expected=[symbol],
        answer_type="set_answer",
        correct_key=symbol,
        steps=steps,
        dists=dists[:2],
        machine={"task": "compare_with_symbol", "symbol": symbol},
    )


def _fdp_l3(rng: SeededRandom) -> _Spec:
    kind = rng.choice(("order", "pick", "symbol"))
    return {"order": _l3_order, "pick": _l3_pick, "symbol": _l3_symbol}[kind](rng)


def _proper(rng: SeededRandom) -> Fraction:
    d = rng.choice((2, 3, 4, 5, 6, 8, 10, 12))
    n = rng.randint(1, d - 1)
    f = Fraction(n, d)
    if f.denominator != d:
        raise _Retry
    return f


def _display(f: Fraction) -> str:
    return _mixed_latex(f)


def _fdp_l4(rng: SeededRandom) -> _Spec:
    op = rng.choice(("add", "sub", "mul", "div"))
    if op == "add":
        x, y = _proper(rng), _proper(rng)
        if x.denominator == y.denominator:
            raise _Retry
        value = x + y
        lcm = x.denominator * y.denominator // gcd(x.denominator, y.denominator)
        a, b = x.numerator * (lcm // x.denominator), y.numerator * (lcm // y.denominator)
        question = f"Without using a calculator, work out {math(_display(x) + ' + ' + _display(y))}. Give your answer as a mixed number or a fraction in its simplest form."
        steps = [
            ("Write with a common denominator", f"{a}/{lcm}+{b}/{lcm}"),
            ("Add the numerators", f"{a + b}/{lcm}"),
            ("Simplify", _mixed_typed(value)),
        ]
        dists = [
            ("tops_and_bottoms", Fraction(x.numerator + y.numerator, x.denominator + y.denominator)),
            ("tops_over_product", Fraction(x.numerator + y.numerator, x.denominator * y.denominator)),
        ]
    elif op == "sub":
        w1, w2 = rng.randint(2, 6), rng.randint(1, 3)
        x, y = _proper(rng), _proper(rng)
        if w1 <= w2 or x.denominator == y.denominator:
            raise _Retry
        big, small = w1 + x, w2 + y
        value = big - small
        if value <= 0:
            raise _Retry
        question = f"Without using a calculator, work out {math(_display(big) + ' - ' + _display(small))}. Show all your working."
        steps = [
            ("Write as improper fractions", f"{_frac_str(big)}-{_frac_str(small)}"),
            ("Use a common denominator and subtract", _frac_str(value)),
            ("Simplify", _mixed_typed(value)),
        ]
        dists = [
            ("wholes_separate", Fraction(w1 - w2) + abs(x - y)),
            ("tops_and_bottoms_sub", Fraction(big.numerator - small.numerator, abs(big.denominator - small.denominator) or 1)),
        ]
        x, y = big, small
    elif op == "mul":
        x = _proper(rng) + (rng.randint(1, 4) if rng.chance(1, 2) else 0)
        y = _proper(rng)
        value = x * y
        question = ''.join(['Without using a calculator, work out ', format(math(_display(x) + ' \\times ' + _display(y)), ''), '. Give your answer in its simplest form.'])
        steps = [
            ("Write as improper fractions", f"{_frac_str(x)}*{_frac_str(y)}"),
            ("Multiply numerators and denominators", _frac_str(value)),
            ("Simplify", _mixed_typed(value)),
        ]
        lcm = x.denominator * y.denominator // gcd(x.denominator, y.denominator)
        dists = [
            ("kept_first_denominator", Fraction(x.numerator * y.numerator, x.denominator)),
            ("common_denominator_tops", Fraction(x.numerator * (lcm // x.denominator) * y.numerator * (lcm // y.denominator), lcm)),
        ]
    else:
        x = _proper(rng) + rng.randint(1, 8)
        y = _proper(rng)
        value = x / y
        question = ''.join(['Without using a calculator, find the value of ', format(math(_display(x) + ' \\div ' + _display(y)), ''), '. Give your answer in its simplest form.'])
        steps = [
            ("Write as improper fractions", f"{_frac_str(x)}/({_frac_str(y)})"),
            ("Multiply by the reciprocal of the second fraction", f"{_frac_str(x)}*{_frac_str(1 / y)}"),
            ("Simplify", _mixed_typed(value)),
        ]
        dists = [
            ("multiplied_instead", x * y),
            ("inverted_first", y / x),
        ]
    _require(value == {"add": x + y, "sub": x - y, "mul": x * y, "div": x / y}[op], "arithmetic")
    return _fraction_spec("fraction_arithmetic", question, value, steps, dists, {"task": f"fraction_{op}", "x": _frac_str(x), "y": _frac_str(y)})


def _fdp_l5(rng: SeededRandom) -> _Spec:
    kind = rng.choice(("whole", "successive", "successive"))
    if kind == "whole":
        n, d = rng.choice(((3, 8), (2, 5), (3, 5), (5, 8), (3, 4), (7, 10), (4, 9), (5, 6), (2, 3)))
        whole = d * rng.randint(1000 // d + 1, 9000 // d)
        part = Fraction(whole * n, d)
        _require(part.denominator == 1, "part")
        who = rng.choice(_NAMES)
        what = rng.choice(("rent", "school fees", "food", "transport"))
        question = (
            ''.join([format(who, ''), ' spends ', format(math(''.join(['\\frac{', format(n, ''), '}{', format(d, ''), '}'])), ''), ' of the monthly pay on ', format(what, ''), '. This is ', format(_nad(str(part)), ''), '. Calculate the monthly pay.'])
        )
        value = Fraction(whole)
        steps = [
            (f"{n} parts are {int(part)}, so one part is", _frac_str(part / n)),
            (f"Multiply by {d} for the whole", str(whole)),
        ]
        dists = [
            ("fraction_of_part", part * Fraction(n, d)),
            ("one_part_only", part / n),
            ("inverted", part / d * n),
        ]
        return _numeric_spec("whole_from_fraction", question, value, steps, dists, {"task": "whole_from_fraction", "part": int(part), "n": n, "d": d})
    b, d = rng.choice((3, 4, 5, 6)), rng.choice((3, 4, 5, 6))
    a, c = rng.randint(1, b - 1), rng.randint(1, d - 1)
    if gcd(a, b) != 1 or gcd(c, d) != 1:
        raise _Retry
    unit = b * d
    total = unit * rng.randint(max(2, 120 // unit), max(3, 1200 // unit))
    first = Fraction(total * a, b)
    rest = Fraction(total) - first
    second = rest * Fraction(c, d)
    left = rest - second
    _require(first.denominator == 1 and second.denominator == 1 and left > 0, "shares")
    thing = rng.choice(("cupcakes", "exercise books", "oranges"))
    group1, group2 = rng.choice((("the junior primary learners", "the senior primary learners"), ("the Grade 8 learners", "the Grade 9 learners")))
    base = (
        ''.join(['A baker makes ', format(math(str(total)), ''), ' ', format(thing, ''), '. ', format(math(''.join(['\\frac{', format(a, ''), '}{', format(b, ''), '}'])), ''), ' of them are given to ', format(group1, ''), '. ', format(math(''.join(['\\frac{', format(c, ''), '}{', format(d, ''), '}'])), ''), ' of the remaining ', format(thing, ''), ' are given to ', format(group2, ''), '. '])
    )
    machine = {"task": "successive_fractions", "total": total, "a": a, "b": b, "c": c, "d": d}
    steps = [
        ("Number given to the first group", str(int(first))),
        ("Number remaining", str(int(rest))),
        ("Number given to the second group", str(int(second))),
        ("Number left", str(int(left))),
    ]
    if rng.chance(1, 2):
        question = base + f"Work out the number of {thing} that are left."
        dists = [
            ("second_share_only", second),
            ("second_fraction_of_total", Fraction(total) - first - Fraction(total * c, d)),
        ]
        return _numeric_spec("successive_fractions", question, left, steps, dists, machine)
    pct = left * 100 / total
    question = (
        base
        + f"Express the number of {thing} that are left as a percentage of all the {thing} made. "
        + "Give your answer correct to 3 significant figures."
    )
    typed = _typed_number(pct, "sig_figs", 3)
    steps = steps[:-1] + [
        ("Number left", str(int(left))),
        ("Divide by the total and multiply by 100", f"{int(left)}/{total}*100"),
        ("Round to 3 significant figures", typed),
    ]
    dists = [
        ("percent_of_remainder", left * 100 / rest),
        ("percent_inverted", Fraction(total * 100, 1) / left),
        ("second_share_only", second * 100 / total),
    ]
    return _numeric_spec(
        "successive_fractions", question, pct, steps, dists, dict(machine, ask="percentage"),
        mode="sig_figs", digits=3, suffix="\\%",
    )


class FractionsDecimalsPercentagesGenerator(_FamilyGenerator):
    generator_id = "nssco_fractions_decimals_percentages"
    version = 1
    levels = (1, 2, 3, 4, 5)
    level_skills = FDP_LEVEL_SKILLS
    error_notes = FDP_NOTES
    builders = {1: _fdp_l1, 2: _fdp_l2, 3: _fdp_l3, 4: _fdp_l4, 5: _fdp_l5}


# ==========================================================================
# 15798 Ratios, Scales, Rates
# ==========================================================================

RATIO_NOTES: Dict[str, Dict[str, str]] = {
    "simplify_ratio": {
        "reversed": "wrote the ratio the wrong way round",
        "not_simplified": "left the ratio in its original form",
    },
    "share_in_ratio": {
        "one_part_only": "found the value of one part but did not multiply by the number of parts",
        "divided_by_share": "divided the total by the number of parts for this person instead of by the total number of parts",
        "other_share": "gave the share of a different person",
    },
    "ratio_from_given_part": {
        "other_share_only": "found another share instead of the total",
        "added_parts": "added the total number of parts to the given amount",
        "divided_by_total_parts": "divided the given amount by the total number of parts",
        "one_part_only": "found the value of one part only",
        "total_not_share": "gave the total instead of the share that was asked for",
    },
    "map_scale": {
        "no_conversion": "multiplied by the scale but did not change centimetres into kilometres",
        "wrong_conversion": "changed centimetres into kilometres by dividing by 1000 instead of 100 000",
        "multiplied_instead": "multiplied by the scale when going from the real distance to the map",
        "forgot_km_to_cm": "divided by the scale without changing kilometres into centimetres",
        "km_to_cm_wrong": "changed kilometres into centimetres by multiplying by 1000 instead of 100 000",
    },
    "unit_rate": {
        "not_divided_by_quantity": "multiplied the cost by 100 without dividing by the quantity",
        "per_kg_only": "found the cost per kilogram and stopped",
        "multiplied_by_quantity": "multiplied the cost by the quantity",
        "added_difference": "added the difference in the number of items to the cost",
        "multiplied_by_total": "multiplied the cost by the new number of items",
    },
    "inverse_proportion": {
        "direct_proportion": "treated the situation as direct proportion instead of inverse proportion",
        "added_difference": "added the difference in hours to the number of workers",
        "product_of_values": "multiplied the new number of hours by the number of workers",
    },
    "speed_distance_time": {
        "minutes_as_decimal": "wrote 2 hours 15 minutes as 2.15 hours",
        "ignored_minutes": "ignored the minutes in the time",
        "speed_times_time": "multiplied the distance by the time",
        "mean_of_speeds": "took the mean of the two speeds instead of dividing total distance by total time",
        "first_leg_only": "used the first part of the journey only",
        "average_speed_as_mean": "added the two speeds and halved them",
        "metres_per_minute": "gave the speed in metres per minute",
        "km_per_minute": "gave the speed in kilometres per minute",
        "no_km_conversion": "changed minutes to hours but left the distance in metres",
        "wrong_time_used": "used the time of the first part of the journey for both parts",
    },
}

RATIO_LEVEL_SKILLS: Dict[int, Tuple[str, ...]] = {
    1: ("simplify_ratio", "share_in_ratio"),
    2: ("ratio_from_given_part",),
    3: ("map_scale",),
    4: ("unit_rate", "inverse_proportion"),
    5: ("speed_distance_time",),
}


def _ratio_text(parts: Sequence[int]) -> str:
    return " : ".join(str(p) for p in parts)


def _ratio_l1(rng: SeededRandom) -> _Spec:
    if rng.chance(1, 2):
        a, b = rng.randint(1, 9), rng.randint(1, 9)
        if gcd(a, b) != 1 or a == b:
            raise _Retry
        g = rng.randint(2, 12)
        x, y = a * g, b * g
        what = rng.choice((("girls", "boys"), ("pens", "pencils"), ("chairs", "tables")))
        question = (
            f"A school has {math(str(x))} {what[0]} and {math(str(y))} {what[1]}. "
            f"Write the ratio of {what[0]} to {what[1]} in its simplest form."
        )
        typed = f"{a}:{b}"
        dists = [
            ("reversed", f"{b} : {a}", f"{b}:{a}", f"{b}:{a}"),
            ("not_simplified", f"{x} : {y}", f"{x}:{y}", f"{x}:{y}"),
        ]
        dists = [(c, math(d), t, k) for c, d, t, k in dists]
        steps = [(f"Divide both numbers by their highest common factor, {g}", f"{a}:{b}")]
        return _Spec(
            skill="simplify_ratio", question=question, answer=math(f"{a} : {b}"), typed=typed,
            expected=[typed], answer_type="sequence", correct_key=typed, steps=steps, dists=dists,
            machine={"task": "simplify_ratio", "x": x, "y": y},
        )
    n_parts = rng.choice((2, 3))
    parts = [rng.randint(1, 7) for _ in range(n_parts)]
    if gcd(*parts) != 1 or len(set(parts)) < 2:
        raise _Retry
    unit = rng.randint(2, 40) * 5
    total = unit * sum(parts)
    who = _pick_names(rng, n_parts)
    idx = rng.randint(0, n_parts - 1)
    share = unit * parts[idx]
    names = " and ".join([", ".join(who[:-1]), who[-1]]) if n_parts == 3 else f"{who[0]} and {who[1]}"
    question = (
        f"{_nad(str(total))} is shared between {names} in the ratio {math(_ratio_text(parts))}. "
        f"Calculate how much {who[idx]} receives."
    )
    steps = [
        ("Add the parts of the ratio", str(sum(parts))),
        ("Value of one part", str(unit)),
        (f"Multiply by {parts[idx]}", str(share)),
    ]
    other = parts[(idx + 1) % n_parts]
    dists = [
        ("one_part_only", Fraction(unit)),
        ("divided_by_share", Fraction(total, parts[idx])),
        ("other_share", Fraction(unit * other)),
    ]
    return _numeric_spec("share_in_ratio", question, Fraction(share), steps, dists, {"task": "share_in_ratio", "total": total, "ratio": parts, "index": idx})


def _ratio_l2(rng: SeededRandom) -> _Spec:
    n_parts = rng.choice((2, 2, 3))
    parts = [rng.randint(1, 8) for _ in range(n_parts)]
    if len(set(parts)) < 2:
        raise _Retry
    if gcd(*parts) != 1:
        raise _Retry
    unit = rng.randint(2, 60) * 5
    idx = rng.randint(0, n_parts - 1)
    given = unit * parts[idx]
    total = unit * sum(parts)
    ask_total = rng.chance(2, 3)
    other_idx = (idx + 1) % n_parts
    who = _pick_names(rng, 3)
    if rng.chance(1, 2):
        names = f"{who[0]} and {who[1]}" if n_parts == 2 else f"{who[0]}, {who[1]} and {who[2]}"
        intro = f"{names} share some money in the ratio {math(_ratio_text(parts))}. {who[idx]} receives {_nad(str(given))}. "
        unit_name = "Namibian dollars"
    else:
        metals = ("copper", "tin", "zinc")
        names = ", ".join(metals[:n_parts - 1]) + " and " + metals[n_parts - 1] if n_parts == 3 else f"{metals[0]} and {metals[1]}"
        who = list(metals)
        intro = (
            f"An alloy is made of {names} in the ratio {math(_ratio_text(parts))}. "
            f"The mass of the {who[idx]} is {math(str(given))} g. "
        )
        unit_name = "grams"
    steps = [
        (f"{parts[idx]} parts are {given}, so one part is", str(unit)),
    ]
    if ask_total:
        question = intro + ("Calculate the total amount of money shared." if unit_name != "grams" else "Calculate the total mass of the alloy in grams.")
        value = Fraction(total)
        steps += [("Multiply by the total number of parts", str(total))]
        dists = [
            ("other_share_only", Fraction(unit * parts[other_idx])),
            ("added_parts", Fraction(given + sum(parts))),
            ("divided_by_total_parts", Fraction(given, sum(parts))),
        ]
        machine = {"task": "ratio_find_total", "given": given, "ratio": parts, "index": idx}
        return _numeric_spec("ratio_from_given_part", question, value, steps, dists, machine)
    question = intro + f"Calculate the {'amount' if unit_name != 'grams' else 'mass in grams'} of the {who[other_idx]} " \
        + ("receives." if False else "")
    question = (
        intro
        + (f"Calculate how much {who[other_idx]} receives." if unit_name != "grams" else f"Calculate the mass of the {who[other_idx]} in grams.")
    )
    value = Fraction(unit * parts[other_idx])
    steps += [(f"Multiply by {parts[other_idx]}", _frac_str(value))]
    dists = [
        ("one_part_only", Fraction(unit)),
        ("total_not_share", Fraction(total)),
        ("divided_by_total_parts", Fraction(given, sum(parts))),
    ]
    return _numeric_spec(
        "ratio_from_given_part", question, value, steps, dists,
        {"task": "ratio_find_other", "given": given, "ratio": parts, "index": idx, "other": other_idx},
    )


def _ratio_l3(rng: SeededRandom) -> _Spec:
    scale = rng.choice((20000, 25000, 50000, 100000, 200000, 250000, 500000))
    kind = rng.choice(("to_actual", "to_actual", "to_map"))
    if kind == "to_actual":
        length = Fraction(rng.randint(20, 150), 10)
        actual_km = length * scale / 100000
        _dec_str(actual_km)
        if actual_km.denominator not in (1, 2, 4, 5, 10, 20, 25, 50, 100):
            raise _Retry
        question = (
            f"The scale of a map is {math(f'1 : {scale}')}. Two towns in Namibia are "
            f"{math(_dec_str(length))} cm apart on the map. Calculate the actual distance between the towns, in kilometres."
        )
        steps = [
            ("Actual distance in centimetres", _dec_str(length * scale)),
            ("Change centimetres into kilometres (divide by 100 000)", _dec_str(actual_km)),
        ]
        dists = [
            ("no_conversion", length * scale),
            ("wrong_conversion", length * scale / 1000),
        ]
        return _numeric_spec("map_scale", question, actual_km, steps, dists, {"task": "map_to_actual", "scale": scale, "length_cm": _dec_str(length)})
    actual = Fraction(rng.randint(10, 400), 10)
    length = actual * 100000 / scale
    _dec_str(length)
    if length.denominator not in (1, 2, 4, 5, 10, 20, 25, 50, 100):
        raise _Retry
    question = (
        f"The scale of a map is {math(f'1 : {scale}')}. The actual distance between two villages is "
        f"{math(_dec_str(actual))} km. Calculate the distance between the villages on the map, in centimetres."
    )
    steps = [
        ("Actual distance in centimetres", _dec_str(actual * 100000)),
        ("Divide by the scale", _dec_str(length)),
    ]
    dists = [
        ("forgot_km_to_cm", actual / scale),
        ("multiplied_instead", actual * scale / 100000),
        ("km_to_cm_wrong", actual * 1000 / scale),
    ]
    return _numeric_spec("map_scale", question, length, steps, dists, {"task": "actual_to_map", "scale": scale, "actual_km": _dec_str(actual)})


def _ratio_l4(rng: SeededRandom) -> _Spec:
    kind = rng.choice(("per100", "direct", "inverse", "inverse"))
    if kind == "per100":
        per100 = rng.randint(2, 60) * 200
        qty = Fraction(rng.randint(20, 900), 1000)
        cost = Fraction(per100) * qty / 100
        _dec_str(cost)
        if cost.denominator not in (1, 2, 4, 5, 10, 20, 25, 50, 100):
            raise _Retry
        question = (
            f"{math(_dec_str(qty))} kg of dried fish costs {_nad(_dec_str(cost))}. "
            f"Calculate the cost of {math('100')} kg of the dried fish."
        )
        steps = [
            ("Cost of 1 kg", _dec_str(cost / qty) if (cost / qty).denominator in (1, 2, 4, 5, 8, 10, 20, 25, 40, 50) else _frac_str(cost / qty)),
            ("Multiply by 100", str(per100)),
        ]
        dists = [
            ("not_divided_by_quantity", cost * 100),
            ("per_kg_only", cost / qty),
            ("multiplied_by_quantity", cost * qty),
        ]
        return _numeric_spec("unit_rate", question, Fraction(per100), steps, dists, {"task": "cost_per_100kg", "kg": _dec_str(qty), "cost": _dec_str(cost)})
    if kind == "direct":
        k = rng.randint(3, 12)
        m = rng.randint(2, 25)
        if m == k:
            raise _Retry
        each = Fraction(rng.randint(50, 2500), 100)
        total = each * k
        value = each * m
        thing = rng.choice(("loaves of bread", "exercise books", "bottles of cooking oil"))
        question = (
            f"{math(str(k))} {thing} cost {_nad(_dec_str(total))}. "
            f"Calculate the cost of {math(str(m))} {thing}."
        )
        steps = [
            ("Cost of one", _dec_str(each)),
            (f"Multiply by {m}", _dec_str(value)),
        ]
        dists = [
            ("added_difference", total + (m - k)),
            ("multiplied_by_total", total * m),
        ]
        return _numeric_spec("unit_rate", question, value, steps, dists, {"task": "direct_proportion", "k": k, "m": m})
    w = rng.randint(6, 30)
    t = rng.randint(10, 60)
    work = w * t
    divisors = [x for x in range(5, 91) if work % x == 0 and x != t and 4 <= work // x <= 80]
    if not divisors:
        raise _Retry
    t2 = rng.choice(divisors)
    w2 = work // t2
    if w2 == w:
        raise _Retry
    job = rng.choice(("paint a school hall", "plant a field of maize", "build a classroom wall"))
    question = (
        f"{math(str(w))} workers can {job} in {math(str(t))} hours. "
        f"All the workers work at the same rate. How many workers are needed to do the same job in {math(str(t2))} hours?"
    )
    steps = [
        ("Total worker-hours for the job", f"{w}*{t}"),
        ("Divide by the new number of hours", str(w2)),
    ]
    dists = [
        ("direct_proportion", Fraction(w * t2, t)),
        ("added_difference", Fraction(w + (t - t2))),
        ("product_of_values", Fraction(w * t2)),
    ]
    return _numeric_spec("inverse_proportion", question, Fraction(w2), steps, dists, {"task": "inverse_proportion", "workers": w, "hours": t, "new_hours": t2})


def _ratio_l5(rng: SeededRandom) -> _Spec:
    kind = rng.choice(("average", "legs_distance", "legs_speed", "convert"))
    if kind == "average":
        hours = rng.randint(1, 4)
        minutes = rng.choice((10, 15, 20, 30, 40, 45))
        distance = rng.randint(60, 420)
        time = Fraction(hours) + Fraction(minutes, 60)
        speed = distance / time
        question = (
            f"A bus travels {math(str(distance))} km from Windhoek in {math(str(hours))} hours and "
            f"{math(str(minutes))} minutes. Calculate its average speed in kilometres per hour. "
            f"Give your answer correct to 3 significant figures."
        )
        time_text = _frac_str(time)
        steps = [
            ("Write the time in hours", time_text),
            ("Divide distance by time", f"{distance}/({time_text})"),
            ("Round to 3 significant figures", _typed_number(speed, "sig_figs", 3)),
        ]
        dists = [
            ("minutes_as_decimal", Fraction(distance) / (Fraction(hours) + Fraction(minutes, 100))),
            ("ignored_minutes", Fraction(distance, hours)),
            ("speed_times_time", Fraction(distance) * time),
        ]
        return _numeric_spec(
            "speed_distance_time", question, speed, steps, dists,
            {"task": "average_speed", "distance": distance, "hours": hours, "minutes": minutes},
            mode="sig_figs", digits=3,
        )
    if kind in ("legs_distance", "legs_speed"):
        s1, s2 = rng.randint(6, 12) * 10, rng.randint(4, 11) * 10
        t1, t2 = Fraction(rng.randint(1, 5), 2), Fraction(rng.randint(1, 6), 2)
        if s1 == s2:
            raise _Retry
        d1, d2 = s1 * t1, s2 * t2
        total = d1 + d2
        ttot = t1 + t2
        trip = (
            f"A minibus travels at {math(str(s1))} km/h for {_hours(t1)} and then at "
            f"{math(str(s2))} km/h for {_hours(t2)}."
        )
        machine = {"s1": s1, "t1": _dec_str(t1), "s2": s2, "t2": _dec_str(t2)}
        if kind == "legs_distance":
            question = trip + " Calculate the total distance travelled, in kilometres."
            steps = [
                ("Distance for the first part", _dec_str(d1)),
                ("Distance for the second part", _dec_str(d2)),
                ("Add the distances", _dec_str(total)),
            ]
            dists = [
                ("first_leg_only", d1),
                ("mean_of_speeds", Fraction(s1 + s2, 2) * ttot),
                ("wrong_time_used", s2 * t1 + d1),
            ]
            return _numeric_spec("speed_distance_time", question, total, steps, dists, dict(machine, task="total_distance"))
        question = trip + " Calculate the average speed for the whole journey. Give your answer correct to 3 significant figures."
        speed = total / ttot
        steps = [
            ("Total distance", _dec_str(total)),
            ("Total time", _dec_str(ttot)),
            ("Divide total distance by total time", _typed_number(speed, "sig_figs", 3)),
        ]
        dists = [
            ("average_speed_as_mean", Fraction(s1 + s2, 2)),
            ("first_leg_only", Fraction(s1)),
            ("speed_times_time", total * ttot),
        ]
        return _numeric_spec(
            "speed_distance_time", question, speed, steps, dists, dict(machine, task="average_speed_two_legs"),
            mode="sig_figs", digits=3,
        )
    metres = rng.randint(30, 400) * 10
    minutes = rng.randint(2, 25)
    speed = Fraction(metres, 1000) / Fraction(minutes, 60)
    thing = rng.choice(("Tangeni, a runner,", "Selma, a cyclist,", "Hilma, a learner on a bicycle,"))
    question = (
        f"{thing} travels {math(str(metres))} m in {math(str(minutes))} minutes. "
        f"Calculate the average speed in kilometres per hour. Give your answer correct to 3 significant figures."
    )
    steps = [
        ("Change the distance to kilometres", _dec_str(Fraction(metres, 1000))),
        ("Change the time to hours", _frac_str(Fraction(minutes, 60))),
        ("Divide distance by time", _typed_number(speed, "sig_figs", 3)),
    ]
    dists = [
        ("metres_per_minute", Fraction(metres, minutes)),
        ("km_per_minute", Fraction(metres, 1000 * minutes)),
        ("no_km_conversion", Fraction(metres * 60, minutes)),
    ]
    return _numeric_spec(
        "speed_distance_time", question, speed, steps, dists, {"task": "speed_unit_conversion", "metres": metres, "minutes": minutes},
        mode="sig_figs", digits=3,
    )


class RatiosScalesRatesGenerator(_FamilyGenerator):
    generator_id = "nssco_ratios_scales_rates"
    version = 2
    levels = (1, 2, 3, 4, 5)
    level_skills = RATIO_LEVEL_SKILLS
    error_notes = RATIO_NOTES
    builders = {1: _ratio_l1, 2: _ratio_l2, 3: _ratio_l3, 4: _ratio_l4, 5: _ratio_l5}


GENERATORS = [
    AdvancedPercentagesGenerator(),
    FractionsDecimalsPercentagesGenerator(),
    RatiosScalesRatesGenerator(),
]
