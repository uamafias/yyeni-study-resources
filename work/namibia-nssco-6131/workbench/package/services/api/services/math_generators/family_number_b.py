"""Generators for seven more NSSCO Mathematics number and measures lessons.

* 15792 Number Classifications and Properties -> ``nssco_number_classifications_properties``
* 15793 Directed Numbers in Action            -> ``nssco_directed_numbers_in_action``
* 15796 Standard Form, Estimates, Approximations -> ``nssco_standard_form_estimates_approximations``
* 15797 Limits of Accuracy (Bounds)           -> ``nssco_limits_of_accuracy``
* 15799 Personal Finance and Currency         -> ``nssco_personal_finance_currency``
* 15803 Metric Units and Conversions          -> ``nssco_metric_units_conversions``
* 15804 Time, Clocks, and Timetables          -> ``nssco_time_clocks_timetables``

Levels follow the shapes of the 2020-2024 Paper 1 / Paper 2 parts for these lessons
(one- and two-mark "Write down / Find / Calculate / State" parts; answers as exact
numbers, bounds written as inequalities, standard form, clock times and durations).
Every problem is built backwards from its answer and recomputed in exact ``Fraction``
arithmetic. Distractors are the answers a learner gets from one specific, known
mistake; a distractor equal to the correct answer is dropped.

Money is written "Namibian dollars" in question text (the exam prints "N$"; a bare
dollar sign would clash with the ``$...$`` maths delimiters).

Reuses the assembly helpers of ``family_number`` (``_Spec``, ``_assemble`` ...).
"""

from __future__ import annotations

from decimal import ROUND_DOWN, ROUND_HALF_UP, Decimal, getcontext
from fractions import Fraction
from math import gcd, isqrt
from typing import Any, Dict, List, Optional, Sequence, Tuple

from .base import GeneratorError, SeededRandom
from .family_number import (
    _FamilyGenerator,
    _Retry,
    _Spec,
    _dec_str,
    _fmt_rounded,
    _frac_str,
    _numeric_spec,
    _nad,
    _pick_names,
    _require,
    _round_dec,
)
from .formatting import math

getcontext().prec = 60

_TOWNS = (
    "Windhoek",
    "Walvis Bay",
    "Swakopmund",
    "Oshakati",
    "Rundu",
    "Keetmanshoop",
    "Katima Mulilo",
    "Otjiwarongo",
    "Gobabis",
    "Mariental",
)


# --------------------------------------------------------------------------
# Small shared helpers
# --------------------------------------------------------------------------


def _shuffle(rng: SeededRandom, items: Sequence[Any]) -> List[Any]:
    out = list(items)
    for i in range(len(out) - 1, 0, -1):
        j = rng.randint(0, i)
        out[i], out[j] = out[j], out[i]
    return out


def _is_prime(n: int) -> bool:
    if n < 2:
        return False
    for p in range(2, isqrt(n) + 1):
        if n % p == 0:
            return False
    return True


def _is_square(n: int) -> bool:
    return n >= 0 and isqrt(n) ** 2 == n


def _is_cube(n: int) -> bool:
    if n < 0:
        return False
    r = round(n ** (1 / 3))
    return any((r + d) ** 3 == n for d in (-1, 0, 1))


def _signed(x: Any) -> str:
    """A number for display inside maths; negative numbers keep their minus sign."""
    return str(x)


def _label_spec(
    skill: str,
    question: str,
    display: str,
    expected: List[str],
    wrongs: Sequence[Tuple[str, str, str]],
    machine: Dict[str, Any],
    steps: Sequence[Tuple[str, str]],
    answer_type: str = "set_answer",
) -> _Spec:
    """A spec whose answer is a word or symbol. ``wrongs`` is (code, display, typed)."""
    correct = frozenset(expected)
    dists = [(code, shown, typed, typed) for code, shown, typed in wrongs]
    return _Spec(
        skill=skill,
        question=question,
        answer=display,
        typed=expected[0],
        expected=list(expected),
        answer_type=answer_type,
        correct_key=correct,
        steps=list(steps),
        dists=dists,
        machine=dict(machine, answer=expected[0]),
    )


def _words_below_1000(n: int) -> str:
    ones = (
        "zero one two three four five six seven eight nine ten eleven twelve thirteen fourteen "
        "fifteen sixteen seventeen eighteen nineteen"
    ).split()
    tens = "_ _ twenty thirty forty fifty sixty seventy eighty ninety".split()
    if n < 20:
        return ones[n]
    if n < 100:
        t, o = divmod(n, 10)
        return tens[t] + ("-" + ones[o] if o else "")
    h, r = divmod(n, 100)
    return ones[h] + " hundred" + (" and " + _words_below_1000(r) if r else "")


def _words(n: int) -> str:
    if n < 1000:
        return _words_below_1000(n)
    th, r = divmod(n, 1000)
    text = _words_below_1000(th) + " thousand"
    if r:
        text += (" and " if r < 100 else " ") + _words_below_1000(r)
    return text


def _round_sf_fraction(x: Fraction, digits: int) -> Fraction:
    return Fraction(str(_round_dec(x, "sig_figs", digits)))


def _trunc(x: Fraction, mode: str, digits: int) -> Decimal:
    """Cut ``x`` off (no rounding) at the place the rounding rule names."""
    d = Decimal(x.numerator) / Decimal(x.denominator)
    if mode == "sig_figs":
        exp = d.adjusted() - (digits - 1)
        return d.quantize(Decimal(1).scaleb(exp), rounding=ROUND_DOWN)
    return d.quantize(Decimal(1).scaleb(-digits), rounding=ROUND_DOWN)


def _fmt_plain(d: Decimal, mode: str) -> str:
    if mode == "decimal_places":
        return format(d, "f")
    return format(d.normalize(), "f")


# ==========================================================================
# 15792 Number Classifications and Properties
# ==========================================================================

NC_NOTES: Dict[str, Dict[str, str]] = {
    "pick_from_list": {
        "other_item": "chose a number that is in the list but does not fit the description",
        "decimal_item": "chose a decimal or a fraction instead of the integer asked for",
    },
    "classify_number": {
        "any_root_irrational": "said irrational because the expression contains a square root, without simplifying it",
        "assumed_rational": "said rational because the numbers inside the roots are whole numbers",
        "said_non_real": "said non-real for a number that is a real number",
        "negative_root_irrational": "said irrational for the square root of a negative number",
        "negative_root_rational": "said rational for the square root of a negative number",
    },
    "prime_factorisation": {
        "stopped_early": "stopped dividing while one of the factors was still not a prime number",
        "exponent_slip": "made a slip in one of the powers, so the product is no longer the given number",
        "primes_listed_once": "wrote each prime factor only once and left out the repeats",
    },
    "hcf_lcm": {
        "swapped_hcf_lcm": "found the lowest common multiple when asked for the highest common factor, or the other way round",
        "product_of_numbers": "multiplied the two numbers and did not divide by the highest common factor",
        "smallest_common_factor": "gave the smallest prime common factor instead of the highest common factor",
        "common_prime_once": "took each prime factor only once, ignoring the highest power",
    },
    "number_words": {
        "zero_dropped": "left out the zero that holds a place, so the digits sit in the wrong columns",
        "extra_zero": "wrote one zero too many, so the number is ten times too big",
    },
    "place_value": {
        "one_column_left": "gave the place one column to the left of the correct one",
        "one_column_right": "gave the place one column to the right of the correct one",
    },
    "primes_in_range": {
        "included_non_prime": "listed an odd number that is not prime as one of the two primes",
        "only_one": "gave only one of the two prime numbers",
    },
}

NC_LEVEL_SKILLS = {
    1: ("pick_from_list",),
    2: ("classify_number",),
    3: ("prime_factorisation",),
    4: ("hcf_lcm",),
    5: ("number_words", "place_value", "primes_in_range"),
}

_NEG_DECIMALS = ("-1.5", "-2.5", "-0.5", "-3.2", "-4.5", "-0.8")


def _nc_l1(rng: SeededRandom) -> _Spec:
    kind = rng.choice(("square", "cube", "prime", "multiple", "negative_integer"))
    pool = [n for n in range(2, 151)]
    k = 0
    if kind == "square":
        target = rng.choice([n * n for n in range(2, 13)])
        fits = _is_square
        ask = "the square number"
    elif kind == "cube":
        target = rng.choice([8, 27, 64, 125])
        fits = _is_cube
        ask = "the cube number"
    elif kind == "prime":
        target = rng.choice([n for n in range(5, 120) if _is_prime(n)])
        fits = _is_prime
        ask = "the prime number"
    elif kind == "multiple":
        k = rng.choice((4, 6, 7, 8, 9, 12))
        target = k * rng.randint(3, 14)
        fits = lambda n, k=k: n % k == 0
        ask = f"the multiple of {k}"
    else:
        target = -rng.randint(1, 15)
        fits = lambda n: False
        ask = "the negative integer"
    decoys: List[str] = []
    values: Dict[str, Fraction] = {}
    if kind == "negative_integer":
        for _ in range(2):
            s = rng.choice(_NEG_DECIMALS)
            if s not in decoys:
                decoys.append(s)
        while len(decoys) < 5:
            n = str(rng.randint(1, 60))
            if n not in decoys:
                decoys.append(n)
    else:
        guard = 0
        while len(decoys) < 5:
            guard += 1
            _require(guard < 500, "no decoys")
            n = rng.choice(pool)
            if n == target or fits(n) or str(n) in decoys:
                continue
            if kind == "multiple" and n % k == 0:
                continue
            decoys.append(str(n))
    _require(sum(1 for d in decoys if d.lstrip("-").replace(".", "").isdigit() and not "." in d and fits(int(d))) == 0, "decoy fits")
    items = _shuffle(rng, [str(target)] + decoys)
    shown = ", ".join(math(x) for x in items)
    question = f"Here is a list of numbers: {shown}. Write down {ask}."
    wrongs = []
    for d in decoys[:3]:
        code = "decimal_item" if "." in d else "other_item"
        wrongs.append((code, math(d), d))
    return _numeric_spec(
        "pick_from_list",
        question,
        Fraction(target),
        [(f"check each number against 'is {ask[4:]}'", str(target))],
        [(c, Fraction(t)) for c, _, t in wrongs],
        {"task": "pick_from_list", "kind": kind, "list": items},
    )


def _nc_l2(rng: SeededRandom) -> _Spec:
    kind = rng.choice(
        ("root", "root", "sum", "difference", "product", "quotient", "two_roots", "recurring", "negative_root")
    )
    nonsq = [n for n in range(2, 61) if not _is_square(n)]
    sq = [n * n for n in range(2, 11)]
    options = "rational or irrational"
    if kind == "root":
        n = rng.choice(nonsq + sq)
        expr, label = f"\\sqrt{{{n}}}", "rational" if _is_square(n) else "irrational"
        step = f"{n} is {'' if _is_square(n) else 'not '}a perfect square"
    elif kind == "sum":
        n = rng.choice(nonsq)
        expr, label, step = f"\\sqrt{{{n}}} + \\sqrt{{{n}}}", "irrational", "it equals 2 times the root"
    elif kind == "difference":
        n = rng.choice(nonsq)
        expr, label, step = f"\\sqrt{{{n}}} - \\sqrt{{{n}}}", "rational", "it equals 0"
    elif kind == "product":
        n = rng.choice(nonsq)
        expr, label, step = f"\\sqrt{{{n}}} \\times \\sqrt{{{n}}}", "rational", f"it equals {n}"
    elif kind == "quotient":
        n = rng.choice(nonsq)
        expr, label, step = f"\\sqrt{{{n}}} \\div \\sqrt{{{n}}}", "rational", "it equals 1"
    elif kind == "two_roots":
        for _ in range(300):
            a = rng.choice(nonsq)
            if rng.chance(1, 2):
                cands = [n for n in nonsq if n != a and _is_square(a * n)]
                if not cands:
                    continue
                b = rng.choice(cands)
            else:
                b = rng.choice(nonsq)
                if b == a or _is_square(a * b):
                    continue
            break
        else:
            raise _Retry
        prod = a * b
        expr = f"\\sqrt{{{a}}} \\times \\sqrt{{{b}}}"
        label = "rational" if _is_square(prod) else "irrational"
        step = f"the product {a} x {b} = {prod} is {'' if _is_square(prod) else 'not '}a perfect square"
    elif kind == "recurring":
        d = rng.randint(1, 9)
        expr, label, step = f"0.\\dot{{{d}}}", "rational", "a recurring decimal can be written as a fraction"
    else:
        n = rng.randint(2, 30)
        expr, label, step = f"\\sqrt{{-{n}}}", "non-real", "the square root of a negative number is not a real number"
        options = "non-real, rational or irrational"
    question = f"State whether {math(expr)} is {options}."
    labels = ["rational", "irrational"] + (["non-real"] if kind == "negative_root" else [])
    wrongs = []
    for w in labels:
        if w == label:
            continue
        if label == "rational" and w == "irrational":
            code = "any_root_irrational"
        elif label == "irrational" and w == "rational":
            code = "assumed_rational"
        elif label == "non-real":
            code = "negative_root_irrational" if w == "irrational" else "negative_root_rational"
        else:
            code = "said_non_real"
        wrongs.append((code, w, w))
    return _label_spec(
        "classify_number",
        question,
        label,
        [label],
        wrongs,
        {"task": "classify_number", "kind": kind, "expression": expr},
        [(step, label)],
    )


def _factorise(n: int) -> List[Tuple[int, int]]:
    out, p = [], 2
    while n > 1:
        e = 0
        while n % p == 0:
            n //= p
            e += 1
        if e:
            out.append((p, e))
        p += 1
    return out


def _index_typed(fs: Sequence[Tuple[int, int]]) -> str:
    return " × ".join(f"{p}^{e}" if e > 1 else str(p) for p, e in fs)


def _index_latex(fs: Sequence[Tuple[int, int]]) -> str:
    return " \\times ".join(f"{p}^{{{e}}}" if e > 1 else str(p) for p, e in fs)


def _expanded_typed(fs: Sequence[Tuple[int, int]]) -> str:
    return " × ".join(str(p) for p, e in fs for _ in range(e))


def _nc_l3(rng: SeededRandom) -> _Spec:
    primes = (2, 3, 5, 7, 11, 13)
    for _ in range(300):
        count = rng.randint(2, 3)
        chosen = sorted({rng.choice(primes) for _ in range(count)})
        fs = [(p, rng.randint(1, 4) if p <= 3 else rng.randint(1, 2)) for p in chosen]
        n = 1
        for p, e in fs:
            n *= p**e
        if 24 <= n <= 540 and any(e > 1 for _, e in fs):
            break
    else:
        raise _Retry
    typed = _index_typed(fs).replace("×", "x")
    expected = [_index_typed(fs)]
    if _expanded_typed(fs) not in expected:
        expected.append(_expanded_typed(fs))
    question = f"Express {math(str(n))} as a product of its prime factors."
    # distractors
    wrongs: List[Tuple[str, str, str]] = []
    small = fs[0][0]
    cofactor = n // small
    if not _is_prime(cofactor):
        wrongs.append(("stopped_early", math(f"{small} \\times {cofactor}"), f"{small} x {cofactor}"))
    slip = [(p, e) for p, e in fs]
    i = max(range(len(slip)), key=lambda j: slip[j][1])
    slip[i] = (slip[i][0], slip[i][1] - 1)
    slip_fs = [(p, e) for p, e in slip if e > 0]
    wrongs.append(("exponent_slip", math(_index_latex(slip_fs)), _index_typed(slip_fs).replace("×", "x")))
    once = [(p, 1) for p, _ in fs]
    wrongs.append(("primes_listed_once", math(_index_latex(once)), _index_typed(once).replace("×", "x")))
    steps: List[Tuple[str, str]] = []
    rest = n
    for p, e in fs:
        for _ in range(e):
            rest //= p
            steps.append((f"divide by the prime {p}", str(rest)))
    steps.append(("write the primes as a product", f"{_index_typed(fs).replace('×', 'x')}"))
    keys = frozenset(expected)
    spec = _Spec(
        skill="prime_factorisation",
        question=question,
        answer=math(_index_latex(fs)),
        typed=typed,
        expected=expected,
        answer_type="expression",
        form="prime_factors",
        correct_key=keys,
        steps=steps,
        dists=[(c, d, t, t) for c, d, t in wrongs],
        machine={"task": "prime_factorisation", "n": n, "factors": [list(f) for f in fs], "answer": typed},
    )
    return spec


def _nc_l4(rng: SeededRandom) -> _Spec:
    g = rng.choice((2, 3, 4, 5, 6, 7, 8, 9, 12))
    for _ in range(100):
        m, n = rng.randint(2, 15), rng.randint(2, 15)
        if gcd(m, n) == 1 and m != n:
            break
    a, b = g * m, g * n
    _require(gcd(a, b) == g, "hcf")
    lcm = g * m * n
    which = rng.choice(("hcf", "lcm"))
    factorised = rng.chance(1, 3) and all(x <= 200 for x in (a, b))
    if factorised:
        fa, fb = _factorise(a), _factorise(b)
        given = (
            f"{math(f'{a} = ' + _index_latex(fa))} and {math(f'{b} = ' + _index_latex(fb))}"
        )
        question = f"Given that {given}, find the {'highest common factor' if which == 'hcf' else 'lowest common multiple'} of {math(str(a))} and {math(str(b))}."
    else:
        question = (
            f"Find the {'highest common factor' if which == 'hcf' else 'lowest common multiple'} "
            f"of {math(str(a))} and {math(str(b))}."
        )
    if which == "hcf":
        value = Fraction(g)
        sp = min(f for f in range(2, g + 1) if g % f == 0)
        dl = [("swapped_hcf_lcm", Fraction(lcm)), ("product_of_numbers", Fraction(a * b))]
        if sp != g:
            dl.append(("smallest_common_factor", Fraction(sp)))
        steps = [("common factors of both numbers, highest one", str(g))]
    else:
        value = Fraction(lcm)
        dl = [("swapped_hcf_lcm", Fraction(g)), ("product_of_numbers", Fraction(a * b))]
        steps = [("lowest number that both divide into", str(lcm))]
    return _numeric_spec("hcf_lcm", question, value, steps, dl, {"task": which, "a": a, "b": b})


_PLACES = (("tenth", "1/10"), ("hundredth", "1/100"), ("thousandth", "1/1000"))


def _nc_l5(rng: SeededRandom) -> _Spec:
    kind = rng.choice(("words", "place_value", "primes"))
    if kind == "words":
        for _ in range(100):
            if rng.chance(1, 2):
                th, r = rng.randint(1, 9) * 100 + rng.randint(0, 1) * 0, rng.randint(1, 99)
            else:
                th, r = rng.randint(10, 999), rng.randint(1, 999)
            n = th * 1000 + r
            digits = str(n)
            if "0" in digits[:-1] and len(digits) >= 6:
                break
        else:
            raise _Retry
        question = f"Write {_words(n)} in figures."
        dropped = digits.replace("0", "", 1)
        extra = digits[:-3] + "0" + digits[-3:]
        _require(len({digits, dropped, extra}) == 3, "number words distractors")
        return _numeric_spec(
            "number_words",
            question,
            Fraction(n),
            [("write each part of the number in its columns, with 0 as a place holder", digits)],
            [("zero_dropped", Fraction(int(dropped))), ("extra_zero", Fraction(int(extra)))],
            {"task": "number_words", "n": n},
        )
    if kind == "place_value":
        for _ in range(100):
            ds = [rng.randint(1, 9) for _ in range(3)]
            if len(set(ds)) == 3:
                break
        else:
            raise _Retry
        whole = rng.randint(1, 9)
        while whole in ds:
            whole = rng.randint(1, 9)
        pos = rng.randint(1, 3)
        number = f"{whole}.{ds[0]}{ds[1]}{ds[2]}"
        digit = ds[pos - 1]
        word, frac = _PLACES[pos - 1]
        question = f"State the place value of the digit {math(str(digit))} in the number {math(number)}."
        expected = [word, word + "s", frac]
        wrongs = []
        left = _PLACES[pos - 2][0] if pos >= 2 else "ones"
        if pos >= 2:
            wrongs.append(("one_column_left", left, left))
        if pos <= 2:
            right = _PLACES[pos][0]
            wrongs.append(("one_column_right", right, right))
        return _label_spec(
            "place_value",
            question,
            word,
            expected,
            wrongs,
            {"task": "place_value", "number": number, "digit": digit},
            [("read which column the digit is in", word)],
        )
    windows = []
    for k in range(2, 31):
        ps = [n for n in range(10 * k + 1, 10 * k + 10) if _is_prime(n)]
        if len(ps) == 2:
            windows.append((10 * k, ps))
    lo, ps = rng.choice(windows)
    hi = lo + 10
    question = f"Write down the two prime numbers between {math(str(lo))} and {math(str(hi))}."
    typed = f"{ps[0]} and {ps[1]}"
    odd_comp = [n for n in range(lo + 1, hi) if n % 2 == 1 and not _is_prime(n)]
    comp = rng.choice(odd_comp)
    wrongs = [
        ("included_non_prime", math(f"{ps[0]}, {comp}"), f"{ps[0]} and {comp}"),
        ("only_one", math(str(ps[0])), str(ps[0])),
    ]
    return _Spec(
        skill="primes_in_range",
        question=question,
        answer=math(f"{ps[0]}, {ps[1]}"),
        typed=typed,
        expected=[typed],
        answer_type="number_exact",
        correct_key=frozenset([typed]),
        steps=[("test each odd number in the range for factors", f"{ps[0]}, {ps[1]}")],
        dists=[(c, d, t, t) for c, d, t in wrongs],
        machine={"task": "primes_in_range", "lo": lo, "hi": hi, "primes": ps, "answer": typed},
    )


class NumberClassificationsGenerator(_FamilyGenerator):
    generator_id = "nssco_number_classifications_properties"
    version = 1
    levels = (1, 2, 3, 4, 5)
    level_skills = NC_LEVEL_SKILLS
    error_notes = NC_NOTES
    builders = {1: _nc_l1, 2: _nc_l2, 3: _nc_l3, 4: _nc_l4, 5: _nc_l5}



# ==========================================================================
# 15793 Directed Numbers in Action
# ==========================================================================

DN_NOTES: Dict[str, Dict[str, str]] = {
    "temperature_change": {
        "subtracted_sizes": "subtracted the two temperatures as if both were positive, so the drop below zero was lost",
        "ignored_negative": "gave only the positive temperature as the change",
        "ignored_positive": "gave only the temperature below zero as the change",
    },
    "temperature_after_change": {
        "sign_ignored": "worked out the right size but gave it without the minus sign",
        "wrong_direction": "added when the temperature dropped (or subtracted when it rose)",
    },
    "compare_negatives": {
        "compared_as_positive": "compared the numbers as if they were positive, so the symbol points the wrong way",
    },
    "directed_arithmetic": {
        "left_to_right": "worked from left to right and did not do the multiplication or division first",
        "sign_slip": "got the sign of one product or quotient wrong",
    },
    "balance_and_position": {
        "debt_ignored": "treated the starting negative amount as a positive amount",
        "direction_slip": "added a change that should have been subtracted",
    },
}

DN_LEVEL_SKILLS = {
    1: ("temperature_change",),
    2: ("temperature_after_change",),
    3: ("compare_negatives",),
    4: ("directed_arithmetic",),
    5: ("balance_and_position",),
}

_DEG = "^\\circ \\text{C}"


def _deg(v: Any) -> str:
    return math(f"{v}{_DEG}")


def _dn_l1(rng: SeededRandom) -> _Spec:
    town = rng.choice(_TOWNS)
    hi, lo = rng.randint(3, 34), rng.randint(1, 19)
    fall = rng.chance(1, 2)
    if fall:
        question = (
            f"At midday the temperature in {town} was {_deg(hi)}. At midnight it was {_deg(-lo)}. "
            f"By how many degrees did the temperature fall?"
        )
    else:
        question = (
            f"At 04:00 the temperature in {town} was {_deg(-lo)}. At 14:00 it was {_deg(hi)}. "
            f"By how many degrees did the temperature rise?"
        )
    value = hi + lo
    dl = [
        ("subtracted_sizes", Fraction(abs(hi - lo))),
        ("ignored_negative", Fraction(hi)),
        ("ignored_positive", Fraction(lo)),
    ]
    steps = [("add the distance above zero and the distance below zero", str(value))]
    return _numeric_spec(
        "temperature_change", question, Fraction(value), steps, dl, {"task": "temperature_change", "hi": hi, "lo": -lo}
    )


def _dn_l2(rng: SeededRandom) -> _Spec:
    town = rng.choice(_TOWNS)
    for _ in range(200):
        start = rng.randint(-8, 12)
        drop = rng.randint(2, 15)
        down = rng.chance(2, 3)
        end = start - drop if down else start + drop
        if (down and end < 0) or (not down and start < 0):
            break
    else:
        raise _Retry
    if down:
        question = (
            f"The temperature in {town} at 05:00 is {_deg(start)}. By 07:00 the temperature has dropped by "
            f"{_deg(drop)}. Find the temperature at 07:00."
        )
        wrong_dir = start + drop
    else:
        question = (
            f"The temperature in {town} at 05:00 is {_deg(start)}. By 12:00 the temperature has risen by "
            f"{_deg(drop)}. Find the temperature at 12:00."
        )
        wrong_dir = start - drop
    dl = [("sign_ignored", Fraction(abs(end))), ("wrong_direction", Fraction(wrong_dir))]
    return _numeric_spec(
        "temperature_after_change",
        question,
        Fraction(end),
        [("apply the change to the starting temperature", str(end))],
        dl,
        {"task": "temperature_after_change", "start": start, "change": -drop if down else drop},
        suffix=_DEG,
    )


def _dn_l3(rng: SeededRandom) -> _Spec:
    for _ in range(200):
        whole = rng.randint(0, 9)
        a = "".join(str(rng.randint(0, 9)) for _ in range(3))
        b = "".join(str(rng.randint(0, 9)) for _ in range(rng.choice((2, 4))))
        va, vb = Fraction(f"{whole}.{a}"), Fraction(f"{whole}.{b}")
        if va != vb and a[0] == b[0]:
            break
    else:
        raise _Retry
    # statement: -va ? -vb ; larger positive means smaller negative
    symbol = "<" if va > vb else ">"
    other = ">" if symbol == "<" else "<"
    question = (
        ''.join(['Write ', format(math('>'), ''), ', ', format(math('<'), ''), ' or ', format(math('='), ''), ' in the box to make the statement correct: ', format(math('-' + str(whole) + '.' + a + ' \\; \\square \\; -' + str(whole) + '.' + b), '')])
    )
    return _label_spec(
        "compare_negatives",
        question,
        math(symbol),
        [symbol],
        [("compared_as_positive", math(other), other)],
        {"task": "compare_negatives", "left": f"-{whole}.{a}", "right": f"-{whole}.{b}"},
        [("the number further from zero in the negative direction is smaller", symbol)],
    )


_OPS = ("+", "-", "*", "/")
_OP_LATEX = {"+": "+", "-": "-", "*": "\\times", "/": "\\div"}


def _eval_proper(nums: List[int], ops: List[str]) -> Optional[Fraction]:
    vals = [Fraction(n) for n in nums]
    ops = list(ops)
    i = 0
    while i < len(ops):
        if ops[i] in "*/":
            if ops[i] == "/":
                if vals[i + 1] == 0 or vals[i] % vals[i + 1] != 0:
                    return None
                v = vals[i] / vals[i + 1]
            else:
                v = vals[i] * vals[i + 1]
            vals[i : i + 2] = [v]
            del ops[i]
        else:
            i += 1
    acc = vals[0]
    for op, v in zip(ops, vals[1:]):
        acc = acc + v if op == "+" else acc - v
    return acc


def _eval_left_to_right(nums: List[int], ops: List[str]) -> Optional[Fraction]:
    acc = Fraction(nums[0])
    for op, n in zip(ops, nums[1:]):
        if op == "+":
            acc += n
        elif op == "-":
            acc -= n
        elif op == "*":
            acc *= n
        else:
            if n == 0:
                return None
            acc /= n
    return acc


def _term_latex(n: int, first: bool) -> str:
    return str(n) if (n >= 0 or first) else f"({n})"


def _dn_l4(rng: SeededRandom) -> _Spec:
    for _ in range(2000):
        count = rng.choice((3, 4))
        nums = [rng.randint(2, 9) * rng.choice((1, 1, -1)) for _ in range(count)]
        ops = [rng.choice(_OPS) for _ in range(count - 1)]
        if not any(o in "*/" for o in ops) or not any(n < 0 for n in nums):
            continue
        value = _eval_proper(nums, ops)
        naive = _eval_left_to_right(nums, ops)
        if value is None or value.denominator != 1 or abs(value) > 80 or naive is None or naive.denominator != 1:
            continue
        if naive == value:
            continue
        break
    else:
        raise _Retry
    text = _term_latex(nums[0], True)
    for op, n in zip(ops, nums[1:]):
        text += f" {_OP_LATEX[op]} {_term_latex(n, False)}"
    question = f"Work out {math(text)}."
    # one sign slip: flip the sign of the final answer
    dl = [("left_to_right", naive), ("sign_slip", -value)]
    steps = []
    work_nums, work_ops = list(map(Fraction, nums)), list(ops)
    i = 0
    while i < len(work_ops):
        if work_ops[i] in "*/":
            v = work_nums[i] * work_nums[i + 1] if work_ops[i] == "*" else work_nums[i] / work_nums[i + 1]
            steps.append((f"do the {'multiplication' if work_ops[i] == '*' else 'division'} first", _frac_str(v)))
            work_nums[i : i + 2] = [v]
            del work_ops[i]
        else:
            i += 1
    steps.append(("then add and subtract from left to right", _frac_str(value)))
    return _numeric_spec(
        "directed_arithmetic", question, value, steps, dl, {"task": "directed_arithmetic", "nums": nums, "ops": ops}
    )


def _dn_l5(rng: SeededRandom) -> _Spec:
    kind = rng.choice(("bank", "diver"))
    if kind == "bank":
        name = _pick_names(rng, 1)[0]
        for _ in range(300):
            start = -rng.randint(1, 6) * 50
            changes = [rng.randint(2, 12) * 25 * rng.choice((1, -1)) for _ in range(3)]
            end = start + sum(changes)
            if any(c > 0 for c in changes) and any(c < 0 for c in changes) and end != start and abs(end) <= 600:
                break
        else:
            raise _Retry
        parts = []
        for i, c in enumerate(changes):
            verb = "deposits" if c > 0 else "withdraws"
            parts.append(f"{verb} {math(str(abs(c)))} Namibian dollars")
        question = (
            f"{name}'s bank balance is {math(str(start))} Namibian dollars (an overdraft). "
            f"{name} {parts[0]}, then {parts[1]}, then {parts[2]}. Find the new balance, in Namibian dollars."
        )
        wrong_start = abs(start) + sum(changes)
        wrong_dir = start - sum(changes)
        suffix = ""
    else:
        for _ in range(300):
            start = -rng.randint(3, 20)
            changes = [rng.randint(2, 12) * rng.choice((1, -1)) for _ in range(3)]
            end = start + sum(changes)
            if any(c > 0 for c in changes) and any(c < 0 for c in changes) and end != start and end < 3:
                break
        else:
            raise _Retry
        names = []
        for c in changes:
            names.append(f"rises {abs(c)} m" if c > 0 else f"dives a further {abs(c)} m")
        question = (
            f"A diver is at {math(str(start))} m (below sea level). The diver {names[0]}, then {names[1]}, then "
            f"{names[2]}. Find the new position, in metres, relative to sea level."
        )
        wrong_start = abs(start) + sum(changes)
        wrong_dir = start - sum(changes)
        suffix = ""
    running, steps = start, []
    for c in changes:
        running += c
        steps.append((f"apply the change {c:+d}", str(running)))
    dl = [("debt_ignored", Fraction(wrong_start)), ("direction_slip", Fraction(wrong_dir))]
    return _numeric_spec(
        "balance_and_position",
        question,
        Fraction(end),
        steps,
        dl,
        {"task": "balance_and_position", "kind": kind, "start": start, "changes": changes},
        suffix=suffix,
    )


class DirectedNumbersGenerator(_FamilyGenerator):
    generator_id = "nssco_directed_numbers_in_action"
    version = 1
    levels = (1, 2, 3, 4, 5)
    level_skills = DN_LEVEL_SKILLS
    error_notes = DN_NOTES
    builders = {1: _dn_l1, 2: _dn_l2, 3: _dn_l3, 4: _dn_l4, 5: _dn_l5}



# ==========================================================================
# 15796 Standard Form, Estimates, and Approximations
# ==========================================================================

SF_NOTES: Dict[str, Dict[str, str]] = {
    "standard_form_conversion": {
        "power_off_by_one": "counted the places the decimal point moved incorrectly, so the power of 10 is one out",
        "power_sign_flipped": "gave a positive power for a small number, or a negative power for a large number",
        "zeros_off_by_one": "wrote one zero too few or too many when changing back to an ordinary number",
        "wrong_direction": "moved the decimal point the wrong way, giving a large number instead of a small one",
    },
    "round_number": {
        "truncated": "cut the number off at the place asked for without rounding up",
        "other_rule": "used decimal places where significant figures were asked for, or the other way round",
        "wrong_place": "rounded to one place more or one place fewer than the question asked",
    },
    "estimate_by_rounding": {
        "two_sig_figs": "rounded each number to 2 significant figures instead of 1",
        "truncated": "cut each number off to 1 significant figure instead of rounding",
        "nearest_whole": "rounded each number to the nearest whole number instead of 1 significant figure",
    },
    "standard_form_calculation": {
        "exponent_added_for_division": "added the powers of 10 when dividing instead of subtracting",
        "power_one_too_big": "did not adjust the power of 10 after the number part left the range 1 to 10, so the power is one too big",
        "power_one_too_small": "adjusted the power of 10 the wrong way after the number part left the range 1 to 10, so the power is one too small",
        "exponent_subtracted_for_multiplication": "subtracted the powers of 10 when multiplying instead of adding",
    },
    "calculator_to_sig_figs": {
        "rounded_too_early": "rounded a root to 1 decimal place before finishing, so the 3 significant figure answer is out",
        "wrong_root": "used a square root where a cube root was needed",
        "combined_roots_sum": "added the numbers first and took a single square root",
        "combined_roots": "multiplied the numbers under one square root",
        "squared_not_cubed": "squared the bracket instead of cubing it",
        "cubed_separately": "cubed each part of the bracket separately instead of cubing the whole bracket",
        "root_ignored": "did not take the square root",
        "multiplied_instead": "multiplied by the number instead of dividing",
    },
}

SF_LEVEL_SKILLS = {
    1: ("standard_form_conversion",),
    2: ("round_number",),
    3: ("estimate_by_rounding",),
    4: ("standard_form_calculation",),
    5: ("calculator_to_sig_figs",),
}


def _std_parts(v: Fraction) -> Tuple[Fraction, int]:
    """(mantissa, exponent) with 1 <= mantissa < 10."""
    e = 0
    m = v
    while m >= 10:
        m /= 10
        e += 1
    while m < 1:
        m *= 10
        e -= 1
    return m, e


def _std_typed(m: Fraction, e: int) -> str:
    return f"{_dec_str(m)} x 10^{e}"


def _std_latex(m: Fraction, e: int) -> str:
    return f"{_dec_str(m)} \\times 10^{{{e}}}"


def _ordinary(v: Fraction) -> str:
    return _dec_str(v)


def _sf_l1(rng: SeededRandom) -> _Spec:
    digits = rng.choice((1, 2, 3))
    mant = Fraction(rng.randint(10 ** (digits - 1), 10**digits - 1), 10 ** (digits - 1))
    e = rng.choice([-7, -6, -5, -4, -3, -2, 3, 4, 5, 6, 7, 8])
    v = mant * Fraction(10) ** e
    forward = rng.chance(1, 2)
    if forward:
        question = f"Write {math(_ordinary(v))} in standard form."
        correct_typed = _std_typed(mant, e)
        dl_vals = [
            ("power_off_by_one", (mant, e + 1 if e < 0 else e - 1)),
            ("power_sign_flipped", (mant, -e)),
        ]
        spec_dists = [
            (c, math(_std_latex(m, ee)), _std_typed(m, ee), v2)
            for c, (m, ee) in dl_vals
            for v2 in [m * Fraction(10) ** ee]
        ]
        return _Spec(
            skill="standard_form_conversion",
            question=question,
            answer=math(_std_latex(mant, e)),
            typed=correct_typed,
            expected=[correct_typed],
            answer_type="standard_form",
            correct_key=v,
            steps=[("move the decimal point to leave a number from 1 to 10", _dec_str(mant)), ("count the places moved", str(e))],
            dists=spec_dists,
            machine={"task": "to_standard_form", "value": _ordinary(v), "answer": correct_typed},
        )
    question = f"Write {math(_std_latex(mant, e))} as an ordinary number."
    wrong_zero = mant * Fraction(10) ** (e + (1 if rng.chance(1, 2) else -1))
    wrong_dir = mant * Fraction(10) ** (-e)
    dl = [("zeros_off_by_one", wrong_zero), ("wrong_direction", wrong_dir)]
    return _numeric_spec(
        "standard_form_conversion",
        question,
        v,
        [("move the decimal point the number of places in the power", _ordinary(v))],
        dl,
        {"task": "from_standard_form", "mantissa": _dec_str(mant), "exponent": e},
    )


def _sf_decimal_value(rng: SeededRandom, places: int) -> Fraction:
    for _ in range(100):
        whole = rng.choice((0, 0, 1, 2, 3, 12, 27, 45, 138, 604))
        frac = "".join(str(rng.randint(0, 9)) for _ in range(places))
        if frac[-1] == "0" or (whole == 0 and set(frac) == {"0"}):
            continue
        return Fraction(f"{whole}.{frac}")
    raise _Retry


def _sf_l2(rng: SeededRandom) -> _Spec:
    kind = rng.choice(("dp", "dp", "sf", "sf", "nearest"))
    if kind == "nearest":
        unit = rng.choice((10, 100, 1))
        x = Fraction(rng.randint(1500, 98000), rng.choice((1, 10)))
        q, r = divmod(x / unit, 1)
        rounded = (q + (1 if r >= Fraction(1, 2) else 0)) * unit
        name = {1: "whole number", 10: "10", 100: "100"}[unit]
        question = f"Round {math(_dec_str(x))} to the nearest {name}."
        trunc = q * unit
        other = (q + 1) * unit if r < Fraction(1, 2) else (q) * unit
        dl = [("truncated", trunc), ("wrong_place", other)]
        spec = _numeric_spec(
            "round_number",
            question,
            rounded,
            [(f"look at the digit after the {name} place and round", _dec_str(rounded))],
            dl,
            {"task": "round_nearest", "value": _dec_str(x), "unit": unit},
            mode=None,
            answer_type="number_rounded",
        )
        spec.rounding = "nearest_unit"
        return spec
    digits = rng.choice((1, 2, 3))
    mode = "decimal_places" if kind == "dp" else "sig_figs"
    x = _sf_decimal_value(rng, digits + rng.choice((1, 2, 3)))
    # sometimes make the next digit exactly 5 so half-way rounding is tested
    if mode == "decimal_places" and rng.chance(1, 4):
        x = Fraction(f"{rng.randint(1, 9)}.{''.join(str(rng.randint(0, 9)) for _ in range(digits))}5")
    ok = _fmt_rounded(x, mode, digits)
    word = {"decimal_places": "decimal place" + ("s" if digits > 1 else ""), "sig_figs": "significant figure" + ("s" if digits > 1 else "")}[mode]
    question = f"Round {math(_dec_str(x))} to {digits} {word}."
    t = _fmt_plain(_trunc(x, mode, digits), mode)
    other_mode = "sig_figs" if mode == "decimal_places" else "decimal_places"
    o = _fmt_rounded(x, other_mode, digits)
    place_off = _fmt_rounded(x, mode, digits + 1 if digits < 3 else digits - 1)
    cands = [("truncated", t), ("other_rule", o), ("wrong_place", place_off)]
    keys_ok = Decimal(ok)
    dists = []
    for code, typed in cands:
        if Decimal(typed) == keys_ok:
            continue
        dists.append((code, math(typed), typed, Decimal(typed)))
    return _Spec(
        skill="round_number",
        question=question,
        answer=math(ok),
        typed=ok,
        expected=[ok],
        answer_type="number_rounded",
        correct_key=keys_ok,
        steps=[(f"look at the digit after the {word.split()[0]} limit and round", ok)],
        dists=dists,
        machine={"task": "round", "value": _dec_str(x), "mode": mode, "digits": digits, "answer": ok},
        rounding=mode,
        digits=digits,
    )


def _sf_l3(rng: SeededRandom) -> _Spec:
    shape = rng.choice(("mul_div", "mul_div", "add_div", "div_mul"))
    for _ in range(500):
        a = Fraction(rng.randint(150, 990), rng.choice((10, 10, 100)))
        b = Fraction(rng.randint(21, 99), 10)
        c = Fraction(rng.randint(21, 99), rng.choice((100, 10)))
        ra, rb, rc = (_round_sf_fraction(v, 1) for v in (a, b, c))
        if 0 in (ra, rb, rc):
            continue
        if shape == "mul_div":
            expr, est = f"\\frac{{{_dec_str(a)} \\times {_dec_str(b)}}}{{{_dec_str(c)}}}", ra * rb / rc
            f = lambda x, y, z: x * y / z
        elif shape == "add_div":
            expr, est = f"\\frac{{{_dec_str(a)} + {_dec_str(b)}}}{{{_dec_str(c)}}}", (ra + rb) / rc
            f = lambda x, y, z: (x + y) / z
        else:
            expr, est = f"\\frac{{{_dec_str(a)}}}{{{_dec_str(b)} \\times {_dec_str(c)}}}", ra / (rb * rc)
            f = lambda x, y, z: x / (y * z)
        try:
            _dec_str(est)
        except _Retry:
            continue
        tw = [_round_sf_fraction(v, 2) for v in (a, b, c)]
        tr = [Fraction(str(_trunc(v, "sig_figs", 1))) for v in (a, b, c)]
        nw = [Fraction(int(v + Fraction(1, 2))) for v in (a, b, c)]
        if 0 in tr or 0 in nw or 0 in tw:
            continue
        d_two, d_tr, d_nw = f(*tw), f(*tr), f(*nw)
        break
    else:
        raise _Retry
    question = f"Estimate the value of {math(expr)} by rounding each number to 1 significant figure."
    steps = [
        (f"round {_dec_str(v)} to 1 significant figure", _dec_str(r)) for v, r in ((a, ra), (b, rb), (c, rc))
    ] + [("work out the estimate with the rounded numbers", _dec_str(est))]
    dl = [("two_sig_figs", d_two), ("truncated", d_tr), ("nearest_whole", d_nw)]
    return _numeric_spec(
        "estimate_by_rounding",
        question,
        est,
        steps,
        dl,
        {"task": "estimate", "shape": shape, "numbers": [_dec_str(a), _dec_str(b), _dec_str(c)]},
    )


def _sf_l4(rng: SeededRandom) -> _Spec:
    kind = rng.choice(("ordinary_div", "std_mul", "std_div", "ordinary_mul"))
    for _ in range(300):
        m1 = Fraction(rng.randint(12, 99), 10)
        m2 = Fraction(rng.randint(12, 99), 10)
        e1, e2 = rng.choice([-6, -5, -4, -3, -2, 2, 3, 4, 5, 6, 7]), rng.choice([-6, -5, -4, -3, -2, 2, 3, 4, 5, 6, 7])
        if m1 == m2 or e1 == e2:
            continue
        if kind == "ordinary_div":
            n = Fraction(rng.choice((4, 8, 12, 16, 24, 36, 48, 72)) * rng.choice((1, 10, 100)))
            d = Fraction(rng.choice((16, 25, 32, 64, 125, 160, 250, 400)) * 10 ** rng.randint(1, 4))
            value = n / d
            text = f"Divide {math(_dec_str(n))} by {math(_dec_str(d))}. Give your answer in standard form."
        elif kind == "std_mul":
            value = m1 * m2 * Fraction(10) ** (e1 + e2)
            text = (
                ''.join(['Work out ', format(math(''.join(['(', format(_std_latex(m1, e1), ''), ') \\times (', format(_std_latex(m2, e2), ''), ')'])), ''), '. Give your answer in standard form.'])
            )
        elif kind == "std_div":
            value = m1 / m2 * Fraction(10) ** (e1 - e2)
            text = (
                ''.join(['Work out ', format(math(''.join(['(', format(_std_latex(m1, e1), ''), ') \\div (', format(_std_latex(m2, e2), ''), ')'])), ''), '. Give your answer in standard form.'])
            )
        else:
            a = Fraction(rng.randint(2, 9) * rng.choice((1, 5)), 10 ** rng.randint(1, 4))
            b = Fraction(rng.randint(2, 9) * 10 ** rng.randint(1, 5))
            value = a * b
            text = f"Work out {math(_dec_str(a))} times {math(_dec_str(b))}. Give your answer in standard form."
        try:
            mant, ex = _std_parts(value)
            _dec_str(mant)
            _dec_str(value) if abs(ex) < 12 else None
        except _Retry:
            continue
        if len(str(mant.numerator)) > 5:
            continue
        break
    else:
        raise _Retry
    typed = _std_typed(mant, ex)
    dl_pairs: List[Tuple[str, Tuple[Fraction, int]]] = []
    if kind in ("ordinary_div", "std_div"):
        dl_pairs.append(("power_one_too_big", (mant, ex + 1)))
        if kind == "std_div":
            dl_pairs.append(("exponent_added_for_division", (mant, ex + 2 * e2)))
        else:
            dl_pairs.append(("power_one_too_small", (mant, ex - 1)))
    else:
        dl_pairs.append(("power_one_too_big", (mant, ex + 1)))
        if kind == "std_mul":
            dl_pairs.append(("exponent_subtracted_for_multiplication", (mant, e1 - e2)))
        else:
            dl_pairs.append(("power_one_too_small", (mant, ex - 1)))
    dists = []
    seen = set()
    for code, (m, ee) in dl_pairs:
        v2 = m * Fraction(10) ** ee
        if v2 == value or (m, ee) in seen:
            continue
        seen.add((m, ee))
        dists.append((code, math(_std_latex(m, ee)), _std_typed(m, ee), v2))
    return _Spec(
        skill="standard_form_calculation",
        question=text,
        answer=math(_std_latex(mant, ex)),
        typed=typed,
        expected=[typed],
        answer_type="standard_form",
        correct_key=value,
        steps=[("work out the number part and the power of 10", _dec_str(value) if abs(ex) < 10 else typed), ("write it with a number from 1 to 10", typed)],
        dists=dists,
        machine={"task": kind, "answer": typed},
    )


def _dec_root(x: int, k: int) -> Decimal:
    if k == 2:
        return Decimal(x).sqrt()
    return (Decimal(x).ln() / Decimal(k)).exp()


def _sig3(d: Decimal) -> Decimal:
    exp = d.adjusted() - 2
    return d.quantize(Decimal(1).scaleb(exp), rounding=ROUND_HALF_UP)


def _safe_round(d: Decimal) -> bool:
    """True when 3 s.f. rounding of ``d`` is not within a hair of a rounding boundary."""
    exp = d.adjusted() - 2
    scaled = d / Decimal(1).scaleb(exp)
    frac = scaled - scaled.to_integral_value(rounding=ROUND_DOWN)
    return abs(frac - Decimal("0.5")) > Decimal("0.01")


def _sf_l5(rng: SeededRandom) -> _Spec:
    kind = rng.choice(("root_plus_cube_root", "cube_of_sum", "root_over", "product_roots"))
    nonsq = [n for n in range(2, 90) if not _is_square(n)]
    noncube = [n for n in range(2, 200) if not _is_cube(n)]
    for _ in range(300):
        if kind == "root_plus_cube_root":
            a, b = rng.choice(nonsq), rng.choice(noncube)
            expr = f"\\sqrt{{{a}}} + \\sqrt[3]{{{b}}}"
            value = _dec_root(a, 2) + _dec_root(b, 3)
            wrongs = [
                ("rounded_too_early", Decimal(str(_round_dec(Fraction(str(_dec_root(a, 2))), "decimal_places", 1))) + Decimal(str(_round_dec(Fraction(str(_dec_root(b, 3))), "decimal_places", 1)))),
                ("wrong_root", _dec_root(a, 2) + _dec_root(b, 2)),
                ("combined_roots_sum", _dec_root(a + b, 2)),
            ]
        elif kind == "cube_of_sum":
            a, b = rng.randint(2, 9), rng.choice(nonsq)
            expr = f"\\left({a} + \\sqrt{{{b}}}\\right)^{{3}}"
            value = (Decimal(a) + _dec_root(b, 2)) ** 3
            wrongs = [
                ("cubed_separately", Decimal(a) ** 3 + _dec_root(b, 2) ** 3),
                ("squared_not_cubed", (Decimal(a) + _dec_root(b, 2)) ** 2),
                ("rounded_too_early", (Decimal(a) + _round_dec(Fraction(str(_dec_root(b, 2))), "decimal_places", 1)) ** 3),
            ]
        elif kind == "root_over":
            a, b = rng.choice(nonsq), rng.randint(3, 9)
            expr = f"\\frac{{\\sqrt{{{a}}}}}{{{b}}}"
            value = _dec_root(a, 2) / Decimal(b)
            wrongs = [
                ("multiplied_instead", _dec_root(a, 2) * Decimal(b)),
                ("root_ignored", Decimal(a) / Decimal(b)),
                ("rounded_too_early", Decimal(str(_round_dec(Fraction(str(_dec_root(a, 2))), "decimal_places", 1))) / Decimal(b)),
            ]
        else:
            a, b = rng.choice(nonsq), rng.choice(noncube)
            expr = f"\\sqrt{{{a}}} \\times \\sqrt[3]{{{b}}}"
            value = _dec_root(a, 2) * _dec_root(b, 3)
            wrongs = [
                ("wrong_root", _dec_root(a, 2) * _dec_root(b, 2)),
                ("combined_roots", _dec_root(a * b, 2)),
                ("rounded_too_early", Decimal(str(_round_dec(Fraction(str(_dec_root(a, 2))), "decimal_places", 1))) * Decimal(str(_round_dec(Fraction(str(_dec_root(b, 3))), "decimal_places", 1)))),
            ]
        if _safe_round(value) and all(_safe_round(w) for _, w in wrongs):
            break
    else:
        raise _Retry
    question = (
        f"Use your calculator to work out {math(expr)}. Give your answer correct to 3 significant figures."
    )
    typed = format(_sig3(value), "f")
    dists = []
    for code, w in wrongs:
        wt = format(_sig3(w), "f")
        dists.append((code, math(wt), wt, Decimal(wt)))
    return _Spec(
        skill="calculator_to_sig_figs",
        question=question,
        answer=math(typed),
        typed=typed,
        expected=[typed],
        answer_type="number_rounded",
        correct_key=Decimal(typed),
        steps=[("evaluate on the calculator without rounding in between", format(value.quantize(Decimal("0.0001")), "f")), ("round to 3 significant figures", typed)],
        dists=dists,
        machine={"task": kind, "expression": expr, "answer": typed},
        rounding="sig_figs",
        digits=3,
    )


class StandardFormEstimatesGenerator(_FamilyGenerator):
    generator_id = "nssco_standard_form_estimates_approximations"
    version = 1
    levels = (1, 2, 3, 4, 5)
    level_skills = SF_LEVEL_SKILLS
    error_notes = SF_NOTES
    builders = {1: _sf_l1, 2: _sf_l2, 3: _sf_l3, 4: _sf_l4, 5: _sf_l5}



# ==========================================================================
# 15797 Limits of Accuracy (Bounds)
# ==========================================================================

LA_NOTES: Dict[str, Dict[str, str]] = {
    "bounds_inequality": {
        "whole_unit_step": "went a whole unit either side of the value instead of half a unit",
        "upper_bound_included": "wrote the upper bound with 'less than or equal to', but the upper bound itself is not reached",
        "rounded_up_only": "took the value as the lower bound and a whole unit above as the upper bound",
    },
    "single_bound": {
        "whole_unit_step": "added or subtracted a whole unit instead of half a unit",
        "value_unchanged": "gave the stated value instead of its bound",
        "recurring_nines": "wrote the bound with a string of nines (for example 8.349) instead of the exact bound",
    },
    "rectangle_bounds": {
        "given_values_used": "used the stated lengths instead of their bounds",
        "wrong_bounds_used": "used the lower bounds where upper bounds were needed, or the other way round",
        "whole_unit_added": "added a whole unit to each length instead of half a unit",
    },
    "combined_bounds": {
        "swapped_bounds": "used the bounds the wrong way round, so the answer is the smallest value where the largest was asked for (or the other way round)",
        "given_values_used": "worked with the stated values and did not use bounds",
        "same_bound_both": "used both upper bounds (or both lower bounds) when one of each was needed",
    },
    "bounds_of_measure": {
        "given_values_used": "used the stated values instead of their bounds",
        "wrong_bounds_used": "used the lower bound where the upper bound was needed, or the other way round",
        "upper_both": "used the upper bound of every measurement when the smallest result needs lower bounds",
    },
}

LA_LEVEL_SKILLS = {
    1: ("bounds_inequality",),
    2: ("single_bound",),
    3: ("rectangle_bounds",),
    4: ("combined_bounds",),
    5: ("bounds_of_measure",),
}

# (quantity, letter, unit name for 'nearest', abbreviation)
_QUANTITIES = (
    ("length", "l", "metre", "m"),
    ("width", "w", "centimetre", "cm"),
    ("mass", "m", "kilogram", "kg"),
    ("time", "t", "second", "s"),
    ("height", "h", "centimetre", "cm"),
    ("distance", "d", "kilometre", "km"),
)
_THINGS = {
    "length": ("a rope", "a classroom", "a fence", "a plank"),
    "width": ("a table", "a poster", "a door", "a banner"),
    "mass": ("a parcel", "a bag of maize meal", "a suitcase", "a watermelon"),
    "time": ("a race", "a phone call", "a bus journey", "a test"),
    "height": ("a bookshelf", "a flagpole", "a tree seedling", "a water tank"),
    "distance": ("a road trip", "a footpath", "a school run", "a cycle route"),
}


def _fixed(v: Fraction, u: Fraction) -> str:
    """``v`` written with as many decimal places as its accuracy states (34 -> 34.0 for 1 d.p.)."""
    places = 0 if u >= 1 else (1 if u == Fraction(1, 10) else 2)
    return format((Decimal(v.numerator) / Decimal(v.denominator)).quantize(Decimal(1).scaleb(-places)), "f")


def _subject(qty: str, thing: str) -> str:
    return f"The time taken for {thing}" if qty == "time" else f"The {qty} of {thing}"


_PLURAL = {"length": "lengths", "width": "widths", "mass": "masses", "distance": "distances", "height": "heights", "time": "times"}


def _accuracy(rng: SeededRandom, unit_name: str) -> Tuple[Fraction, str]:
    kind = rng.choice(("nearest", "nearest", "dp1", "dp1", "dp2", "ten"))
    if kind == "nearest":
        return Fraction(1), f"to the nearest {unit_name}"
    if kind == "dp1":
        return Fraction(1, 10), "correct to 1 decimal place"
    if kind == "dp2":
        return Fraction(1, 100), "correct to 2 decimal places"
    return Fraction(10), "to the nearest 10"


def _measure(rng: SeededRandom, unit: Fraction) -> Fraction:
    if unit == 10:
        return Fraction(rng.randint(3, 98) * 10)
    if unit == 1:
        return Fraction(rng.randint(4, 95))
    if unit == Fraction(1, 10):
        return Fraction(rng.randint(31, 989), 10)
    return Fraction(rng.randint(311, 9989), 100)


def _lo(v: Fraction, u: Fraction) -> Fraction:
    return v - u / 2


def _hi(v: Fraction, u: Fraction) -> Fraction:
    return v + u / 2


def _la_l1(rng: SeededRandom) -> _Spec:
    qty, letter, unit_name, _ = rng.choice(_QUANTITIES)
    thing = rng.choice(_THINGS[qty])
    u, phrase = _accuracy(rng, unit_name)
    v = _measure(rng, u)
    lo, hi = _lo(v, u), _hi(v, u)
    shown = _fixed(v, u)
    question = (
        ''.join([format(_subject(qty, thing), ''), ' is ', format(math(shown), ''), ' ', format(_abbr(qty, unit_name), ''), ', ', format(phrase, ''), '. Complete the inequality: ', format(math(''.join(['\\square \\le ', format(letter, ''), ' < \\square'])), '')])
    )
    typed = f"{_dec_str(lo)} <= {letter} < {_dec_str(hi)}"
    show = f"{_dec_str(lo)} \\le {letter} < {_dec_str(hi)}"
    wrongs = [
        ("whole_unit_step", f"{_dec_str(v - u)} <= {letter} < {_dec_str(v + u)}", f"{_dec_str(v - u)} \\le {letter} < {_dec_str(v + u)}"),
        ("upper_bound_included", f"{_dec_str(lo)} <= {letter} <= {_dec_str(hi)}", f"{_dec_str(lo)} \\le {letter} \\le {_dec_str(hi)}"),
        ("rounded_up_only", f"{_dec_str(v)} <= {letter} < {_dec_str(v + u)}", f"{_dec_str(v)} \\le {letter} < {_dec_str(v + u)}"),
    ]
    return _Spec(
        skill="bounds_inequality",
        question=question,
        answer=math(show),
        typed=typed,
        expected=[typed],
        answer_type="inequality",
        correct_key=typed,
        steps=[("half of the accuracy is " + _dec_str(u / 2), _dec_str(u / 2)), ("lower bound", _dec_str(lo)), ("upper bound", _dec_str(hi))],
        dists=[(c, math(d), t, t) for c, t, d in wrongs],
        machine={"task": "bounds_inequality", "value": shown, "unit": _dec_str(u), "lower": _dec_str(lo), "upper": _dec_str(hi), "answer": typed},
    )


def _abbr(qty: str, unit_name: str) -> str:
    return {"metre": "m", "centimetre": "cm", "kilogram": "kg", "second": "s", "kilometre": "km"}[unit_name]


def _la_l2(rng: SeededRandom) -> _Spec:
    qty, letter, unit_name, _ = rng.choice(_QUANTITIES)
    thing = rng.choice(_THINGS[qty])
    u, phrase = _accuracy(rng, unit_name)
    v = _measure(rng, u)
    which = rng.choice(("upper", "lower"))
    bound = _hi(v, u) if which == "upper" else _lo(v, u)
    question = (
        f"{_subject(qty, thing)} is {math(_fixed(v, u))} {_abbr(qty, unit_name)}, {phrase}. "
        f"Write down the {which} bound of the {qty}."
    )
    sign = 1 if which == "upper" else -1
    dl = [
        ("whole_unit_step", v + sign * u),
        ("value_unchanged", v),
    ]
    if which == "upper":
        d = len(_dec_str(bound).split(".")[1]) if "." in _dec_str(bound) else 0
        dl.append(("recurring_nines", bound - Fraction(1, 10) ** (d + 1)))
    return _numeric_spec(
        "single_bound",
        question,
        bound,
        [("half of the accuracy is " + _dec_str(u / 2), _dec_str(u / 2)), (f"{which} bound", _dec_str(bound))],
        dl,
        {"task": "single_bound", "which": which, "value": _dec_str(v), "unit": _dec_str(u)},
    )


def _la_l3(rng: SeededRandom) -> _Spec:
    for _ in range(100):
        unit_name = rng.choice(("metre", "centimetre"))
        u, phrase = _accuracy(rng, unit_name)
        if u != 10:
            break
    a, b = _measure(rng, u), _measure(rng, u)
    if u == 1:
        a, b = Fraction(rng.randint(4, 30)), Fraction(rng.randint(4, 30))
    ab = _abbr("length", unit_name)
    task = rng.choice(("max_area", "min_area", "max_perimeter", "min_perimeter"))
    word = {"max_area": "largest possible area", "min_area": "smallest possible area", "max_perimeter": "upper bound of the perimeter", "min_perimeter": "lower bound of the perimeter"}[task]
    is_area = task.endswith("area")
    shape = "rectangle"
    question = (
        f"The length and width of a {shape} are {math(_fixed(a, u))} {ab} and {math(_fixed(b, u))} {ab}, each {phrase}. "
        f"Calculate the {word} of the {shape}. "
    ) + ("Give the area in square " + {"metre": "metres", "centimetre": "centimetres"}[unit_name] + "." if is_area else "")
    question = question.strip()
    ua, ub = _hi, _lo
    if task == "max_area":
        value = _hi(a, u) * _hi(b, u)
        wrong_b = _lo(a, u) * _lo(b, u)
    elif task == "min_area":
        value = _lo(a, u) * _lo(b, u)
        wrong_b = _hi(a, u) * _hi(b, u)
    elif task == "max_perimeter":
        value = 2 * (_hi(a, u) + _hi(b, u))
        wrong_b = 2 * (_lo(a, u) + _lo(b, u))
    else:
        value = 2 * (_lo(a, u) + _lo(b, u))
        wrong_b = 2 * (_hi(a, u) + _hi(b, u))
    given = a * b if is_area else 2 * (a + b)
    whole = (a + u) * (b + u) if is_area else 2 * (a + b + 2 * u)
    if task.startswith("min"):
        whole = (a - u) * (b - u) if is_area else 2 * (a + b - 2 * u)
    dl = [("given_values_used", given), ("wrong_bounds_used", wrong_b), ("whole_unit_added", whole)]
    steps = [
        ("bounds of the length", f"{_dec_str(_lo(a, u))}, {_dec_str(_hi(a, u))}"),
        ("bounds of the width", f"{_dec_str(_lo(b, u))}, {_dec_str(_hi(b, u))}"),
        (word, _dec_str(value)),
    ]
    return _numeric_spec(
        "rectangle_bounds", question, value, steps, dl, {"task": task, "a": _dec_str(a), "b": _dec_str(b), "unit": _dec_str(u)}
    )


def _la_l4(rng: SeededRandom) -> _Spec:
    qty, letter, unit_name, _ = rng.choice(_QUANTITIES[:3] + _QUANTITIES[5:])
    thing = rng.choice(_THINGS[qty])
    u = Fraction(1, 10)
    x = _measure(rng, u)
    y = _measure(rng, u)
    if rng.chance(1, 2):
        x, y = max(x, y), min(x, y)
    else:
        x, y = max(x, y) + 2, min(x, y)
    _require(x > y, "x > y")
    task = rng.choice(("max_diff", "min_diff", "max_sum", "min_sum"))
    ab = _abbr(qty, unit_name)
    other = {"length": "width", "mass": "mass", "distance": "distance"}.get(qty, qty)
    word = {"max_diff": "largest possible value of x - y", "min_diff": "smallest possible value of x - y", "max_sum": "largest possible value of x + y", "min_sum": "smallest possible value of x + y"}[task]
    question = (
        f"Two {_PLURAL[qty]} are {math('x = ' + _fixed(x, u))} {ab} and {math('y = ' + _fixed(y, u))} {ab}, "
        f"each correct to 1 decimal place. Find the "
        f"{'largest' if task.startswith('max') else 'smallest'} possible value of "
        f"{math('x - y' if 'diff' in task else 'x + y')}."
    )
    if task == "max_diff":
        value, same = _hi(x, u) - _lo(y, u), _hi(x, u) - _hi(y, u)
    elif task == "min_diff":
        value, same = _lo(x, u) - _hi(y, u), _lo(x, u) - _lo(y, u)
    elif task == "max_sum":
        value, same = _hi(x, u) + _hi(y, u), _hi(x, u) + _lo(y, u)
    else:
        value, same = _lo(x, u) + _lo(y, u), _lo(x, u) + _hi(y, u)
    given = x - y if "diff" in task else x + y
    opposite = {"max_diff": _lo(x, u) - _hi(y, u), "min_diff": _hi(x, u) - _lo(y, u), "max_sum": _lo(x, u) + _lo(y, u), "min_sum": _hi(x, u) + _hi(y, u)}[task]
    dl = [("given_values_used", given), ("same_bound_both", same), ("swapped_bounds", opposite)]
    steps = [
        ("bounds of x", f"{_dec_str(_lo(x, u))}, {_dec_str(_hi(x, u))}"),
        ("bounds of y", f"{_dec_str(_lo(y, u))}, {_dec_str(_hi(y, u))}"),
        ("combine the bounds that give the extreme value", _dec_str(value)),
    ]
    return _numeric_spec(
        "combined_bounds", question, value, steps, dl, {"task": task, "x": _dec_str(x), "y": _dec_str(y)}
    )


def _la_l5(rng: SeededRandom) -> _Spec:
    task = rng.choice(("triangle_min_area", "cuboid_min_volume", "speed_max"))
    u1 = Fraction(1, 10)
    if task == "triangle_min_area":
        a, b = _measure(rng, u1), _measure(rng, u1)
        question = (
            f"A right-angled triangle has perpendicular sides of {math(_fixed(a, u1))} cm and {math(_fixed(b, u1))} cm, "
            f"each correct to 1 decimal place. Calculate the smallest possible area of the triangle, in square centimetres."
        )
        value = _lo(a, u1) * _lo(b, u1) / 2
        dl = [
            ("given_values_used", a * b / 2),
            ("wrong_bounds_used", _hi(a, u1) * _hi(b, u1) / 2),
        ]
        steps = [("lower bounds of the two sides", f"{_dec_str(_lo(a, u1))}, {_dec_str(_lo(b, u1))}"), ("half the product", _dec_str(value))]
        return _numeric_spec("bounds_of_measure", question, value, steps, dl, {"task": task, "a": _dec_str(a), "b": _dec_str(b)})
    if task == "cuboid_min_volume":
        a, b, c = (Fraction(rng.randint(20, 109), 10) for _ in range(3))
        question = (
            f"A cuboid measures {math(_fixed(a, u1))} cm by {math(_fixed(b, u1))} cm by {math(_fixed(c, u1))} cm, each correct "
            f"to 1 decimal place. Calculate the smallest possible volume of the cuboid, in cubic centimetres."
        )
        value = _lo(a, u1) * _lo(b, u1) * _lo(c, u1)
        dl = [("given_values_used", a * b * c), ("wrong_bounds_used", _hi(a, u1) * _hi(b, u1) * _hi(c, u1))]
        steps = [("lower bounds of the three lengths", f"{_dec_str(_lo(a, u1))}, {_dec_str(_lo(b, u1))}, {_dec_str(_lo(c, u1))}"), ("multiply the lower bounds", _dec_str(value))]
        return _numeric_spec("bounds_of_measure", question, value, steps, dl, {"task": task, "a": _dec_str(a), "b": _dec_str(b), "c": _dec_str(c)})
    dist = Fraction(rng.randint(40, 480))
    time = Fraction(rng.randint(8, 59), 10)
    question = (
        f"A bus travels {math(_dec_str(dist))} km, correct to the nearest kilometre, in {math(_fixed(time, u1))} hours, "
        f"correct to 1 decimal place. Calculate the greatest possible average speed of the bus, in kilometres per hour. "
        f"Give your answer correct to 3 significant figures."
    )
    value = _hi(dist, Fraction(1)) / _lo(time, u1)
    dl = [
        ("given_values_used", dist / time),
        ("wrong_bounds_used", _lo(dist, Fraction(1)) / _hi(time, u1)),
        ("upper_both", _hi(dist, Fraction(1)) / _hi(time, u1)),
    ]
    steps = [
        ("upper bound of the distance", _dec_str(_hi(dist, Fraction(1)))),
        ("lower bound of the time", _dec_str(_lo(time, u1))),
        ("divide the upper distance by the lower time", _fmt_rounded(value, "sig_figs", 3)),
    ]
    return _numeric_spec(
        "bounds_of_measure", question, value, steps, dl, {"task": task, "distance": _dec_str(dist), "time": _dec_str(time)},
        mode="sig_figs", digits=3,
    )


class LimitsOfAccuracyGenerator(_FamilyGenerator):
    generator_id = "nssco_limits_of_accuracy"
    version = 1
    levels = (1, 2, 3, 4, 5)
    level_skills = LA_LEVEL_SKILLS
    error_notes = LA_NOTES
    builders = {1: _la_l1, 2: _la_l2, 3: _la_l3, 4: _la_l4, 5: _la_l5}



# ==========================================================================
# 15799 Personal Finance and Currency
# ==========================================================================

PF_NOTES: Dict[str, Dict[str, str]] = {
    "change_from_purchase": {
        "quantity_ignored": "used the price of one of each item and did not multiply by how many were bought",
        "total_given": "gave the total cost instead of the change",
        "paid_added": "added the total cost to the amount paid instead of subtracting",
    },
    "simple_interest": {
        "months_as_years": "used the number of months as if it were years",
        "percent_not_divided": "did not divide by 100 when using the percentage",
        "total_not_interest": "gave the total amount (principal plus interest) instead of the interest",
    },
    "currency_conversion": {
        "wrong_direction": "multiplied when the money should be divided by the rate, or divided when it should be multiplied",
        "truncated": "cut the answer off after 2 decimal places instead of rounding",
    },
    "simple_interest_unknown": {
        "amount_not_interest": "used the final amount as the interest, so the principal was not taken off",
        "time_ignored": "did not divide by the number of years",
        "rate_ignored": "did not divide by the rate",
        "multiplied_instead": "multiplied by the rate and the time instead of dividing by them",
    },
    "compound_interest": {
        "simple_interest_used": "worked out simple interest instead of compound interest",
        "one_year_short": "compounded for one year fewer than the question asked",
        "interest_only": "gave the interest earned instead of the total amount",
    },
}

PF_LEVEL_SKILLS = {
    1: ("change_from_purchase",),
    2: ("simple_interest",),
    3: ("currency_conversion",),
    4: ("simple_interest_unknown",),
    5: ("compound_interest",),
}

_RATE_PHRASES = (
    ("euro", "euros", "1 euro", Fraction(172, 10)),
    ("US dollar", "US dollars", "1 US dollar", Fraction(1835, 100)),
    ("British pound", "British pounds", "1 British pound", Fraction(2340, 100)),
)


def _money(x: Fraction) -> str:
    return _dec_str(x)


def _pf_l1(rng: SeededRandom) -> _Spec:
    name = _pick_names(rng, 1)[0]
    item_a = rng.choice(("exercise books", "school diaries", "notebooks", "novels", "textbooks"))
    item_b = rng.choice(("magazines", "newspapers", "comics", "maps"))
    na, nb = rng.randint(2, 5), rng.randint(2, 4)
    pa = Fraction(rng.randint(18, 95), 2)
    pb = Fraction(rng.randint(8, 40), 2)
    total = na * pa + nb * pb
    note = next(n for n in (50, 100, 200, 300, 500, 1000) if n > total)
    change = note - total
    question = (
        f"{name} buys {na} {item_a} at {math(_money(pa))} Namibian dollars each and {nb} {item_b} at "
        f"{math(_money(pb))} Namibian dollars each. {name} pays with a {math(str(note))} Namibian dollar note. "
        f"Calculate the change {name} receives, in Namibian dollars."
    )
    dl = [
        ("quantity_ignored", note - (pa + pb)),
        ("total_given", total),
        ("paid_added", note + total),
    ]
    steps = [
        (f"cost of the {item_a}", _money(na * pa)),
        (f"cost of the {item_b}", _money(nb * pb)),
        ("total cost", _money(total)),
        ("subtract the total from the amount paid", _money(change)),
    ]
    return _numeric_spec(
        "change_from_purchase", question, change, steps, dl, {"task": "change", "na": na, "pa": _money(pa), "nb": nb, "pb": _money(pb), "paid": note}
    )


def _pf_l2(rng: SeededRandom) -> _Spec:
    place = rng.choice(("a bank in Windhoek", "a building society in Walvis Bay", "a savings account in Oshakati"))
    p = rng.choice((1000, 1200, 1500, 2000, 2400, 2500, 3000, 4000, 5000, 6000, 8000))
    r = rng.choice((2, 3, 4, 5, 6, 8, 10))
    months = rng.chance(1, 2)
    if months:
        m = rng.choice((3, 6, 9, 18))
        t = Fraction(m, 12)
        period = f"{m} months"
    else:
        t = Fraction(rng.randint(2, 6))
        period = f"{int(t)} years"
    interest = Fraction(p) * r * t / 100
    question = (
        ''.join(['Saara invests ', format(math(str(p)), ''), ' Namibian dollars in ', format(place, ''), ' at ', format(math(''.join([format(r, ''), '\\%'])), ''), ' per year simple interest. Calculate the simple interest earned in ', format(period, ''), '.'])
    )
    t_wrong = Fraction(m) if months else t
    dl = [
        ("percent_not_divided", Fraction(p) * r * t),
        ("total_not_interest", p + interest),
    ]
    if months:
        dl.insert(0, ("months_as_years", Fraction(p) * r * t_wrong / 100))
    steps = [
        ("time in years", _money(t)),
        ("simple interest = principal x rate x time / 100", _money(interest)),
    ]
    return _numeric_spec(
        "simple_interest", question, interest, steps, dl, {"task": "simple_interest", "p": p, "r": r, "t": _money(t)}
    )


def _pf_l3(rng: SeededRandom) -> _Spec:
    sing, plural, one, rate = rng.choice(_RATE_PHRASES)
    to_foreign = rng.chance(1, 2)
    if to_foreign:
        amount = Fraction(rng.randint(50, 900) * 10)
        question = (
            f"The exchange rate is {one} = {math(_money(rate))} Namibian dollars. Convert "
            f"{math(_dec_str(amount))} Namibian dollars to {plural}. Give your answer correct to 2 decimal places."
        )
        value = amount / rate
        dl = [("wrong_direction", amount * rate), ("truncated", Fraction(int(value * 100), 100))]
        steps = [("divide the Namibian dollars by the rate", _fmt_rounded(value, "decimal_places", 2))]
    else:
        amount = Fraction(rng.randint(20, 900))
        question = (
            f"The exchange rate is {one} = {math(_money(rate))} Namibian dollars. Convert "
            f"{math(_dec_str(amount))} {plural} to Namibian dollars. Give your answer correct to 2 decimal places."
        )
        value = amount * rate
        dl = [("wrong_direction", amount / rate), ("truncated", Fraction(int(value * 100), 100))]
        steps = [("multiply the foreign money by the rate", _fmt_rounded(value, "decimal_places", 2))]
    return _numeric_spec(
        "currency_conversion", question, value, steps, dl, {"task": "currency", "amount": _dec_str(amount), "rate": _money(rate), "to_foreign": to_foreign},
        mode="decimal_places", digits=2,
    )


def _pf_l4(rng: SeededRandom) -> _Spec:
    unknown = rng.choice(("rate", "time", "principal"))
    p = rng.choice((1000, 1500, 2000, 2500, 3000, 4000, 5000, 8000))
    r = rng.choice((Fraction(5, 2), Fraction(4), Fraction(5), Fraction(25, 4), Fraction(15, 2), Fraction(9, 2)))
    t = rng.randint(2, 6)
    interest = Fraction(p) * r * t / 100
    amount = p + interest
    place = rng.choice(("a bank in Rundu", "a savings club in Keetmanshoop", "a building society in Windhoek"))
    if unknown == "rate":
        question = (
            f"Saara invests {math(str(p))} Namibian dollars in {place} at simple interest for {t} years. "
            f"The total amount at the end is {math(_money(amount))} Namibian dollars. Calculate the rate of simple interest per year, as a percentage."
        )
        value = r
        dl = [("amount_not_interest", amount * 100 / (p * t)), ("time_ignored", interest * 100 / p)]
        steps = [("interest = amount - principal", _money(interest)), ("rate = interest x 100 / (principal x time)", _money(r))]
    elif unknown == "time":
        question = (
            ''.join(['Saara invests ', format(math(str(p)), ''), ' Namibian dollars in ', format(place, ''), ' at ', format(math(_money(r) + '\\%'), ''), ' per year simple interest. After how many years will the total amount be ', format(math(_money(amount)), ''), ' Namibian dollars?'])
        )
        value = Fraction(t)
        dl = [("amount_not_interest", amount * 100 / (p * r)), ("rate_ignored", interest * 100 / p)]
        steps = [("interest = amount - principal", _money(interest)), ("time = interest x 100 / (principal x rate)", str(t))]
    else:
        question = (
            ''.join(['An investment in ', format(place, ''), ' earns simple interest at ', format(math(_money(r) + '\\%'), ''), ' per year. After ', format(t, ''), ' years the interest earned is ', format(math(_money(interest)), ''), ' Namibian dollars. Calculate the amount invested, in Namibian dollars.'])
        )
        value = Fraction(p)
        dl = [("multiplied_instead", interest * r * t / 100), ("time_ignored", interest * 100 / r)]
        steps = [("principal = interest x 100 / (rate x time)", str(p))]
    return _numeric_spec(
        "simple_interest_unknown", question, value, steps, dl, {"task": unknown, "p": p, "r": _money(r), "t": t, "amount": _money(amount)}
    )


def _pf_l5(rng: SeededRandom) -> _Spec:
    p = rng.choice((2000, 3000, 4000, 5000, 6000, 8000, 10000, 12000, 15000, 20000))
    r = rng.choice((Fraction(3), Fraction(4), Fraction(5), Fraction(6), Fraction(8), Fraction(9, 2), Fraction(15, 2), Fraction(10)))
    n = rng.choice((2, 2, 3, 4))
    amount = Fraction(p) * (1 + r / 100) ** n
    interest = amount - p
    place = rng.choice(("a bank in Windhoek", "a building society in Walvis Bay", "a savings account in Swakopmund"))
    ask_interest = rng.chance(1, 3)
    what = "interest earned" if ask_interest else "total amount"
    question = (
        ''.join(['Saara invests ', format(math(str(p)), ''), ' Namibian dollars in ', format(place, ''), ' at ', format(math(_money(r) + '\\%'), ''), ' per year compound interest. Calculate the ', format(what, ''), ' after ', format(n, ''), ' years. Give your answer correct to 2 decimal places.'])
    )
    simple = Fraction(p) * (1 + r * n / 100)
    short = Fraction(p) * (1 + r / 100) ** (n - 1)
    if ask_interest:
        value = interest
        dl = [("simple_interest_used", simple - p), ("one_year_short", short - p)]
    else:
        value = amount
        dl = [("simple_interest_used", simple), ("one_year_short", short), ("interest_only", interest)]
    steps, running = [], Fraction(p)
    for year in range(1, n + 1):
        running = running * (1 + r / 100)
        steps.append((f"amount after year {year}", _fmt_rounded(running, "decimal_places", 2)))
    if ask_interest:
        steps.append(("subtract the amount invested", _fmt_rounded(interest, "decimal_places", 2)))
    return _numeric_spec(
        "compound_interest", question, value, steps, dl, {"task": "compound_interest", "p": p, "r": _money(r), "n": n, "ask": what},
        mode="decimal_places", digits=2,
    )


class PersonalFinanceGenerator(_FamilyGenerator):
    generator_id = "nssco_personal_finance_currency"
    version = 1
    levels = (1, 2, 3, 4, 5)
    level_skills = PF_LEVEL_SKILLS
    error_notes = PF_NOTES
    builders = {1: _pf_l1, 2: _pf_l2, 3: _pf_l3, 4: _pf_l4, 5: _pf_l5}



# ==========================================================================
# 15803 Metric Units and Conversions
# ==========================================================================

MU_NOTES: Dict[str, Dict[str, str]] = {
    "length_mass_capacity": {
        "factor_100": "used a factor of 100 where 1000 (or 10) was needed",
        "factor_10000": "used a factor of 10 000 where 1000 was needed",
        "wrong_direction": "divided when converting to a smaller unit, or multiplied when converting to a larger unit",
    },
    "area_volume": {
        "linear_factor": "used the factor for length (such as 100 or 1000) instead of squaring or cubing it",
        "factor_off": "used a factor that is a power of 10 too small",
        "wrong_direction": "divided when converting to a smaller unit, or multiplied when converting to a larger unit",
    },
    "speed_conversion": {
        "wrong_direction": "multiplied by 3.6 when the speed had to be divided by 3.6, or the other way round",
        "factor_36": "used 36 instead of 3.6",
        "factor_60": "used 60 instead of 3.6, as if converting hours to minutes only",
    },
    "compound_units": {
        "time_not_converted": "converted the distance or volume but forgot to convert the time unit",
        "wrong_direction": "multiplied by the factor when it should divide, or the other way round",
        "no_conversion": "gave the same number, as if the units did not need converting",
        "factor_off": "used a factor that is a power of 10 out",
    },
}

MU_LEVEL_SKILLS = {
    1: ("length_mass_capacity",),
    2: ("area_volume",),
    3: ("speed_conversion",),
    4: ("compound_units",),
}

# (from unit, to unit, factor) where 1 from-unit = factor to-units. Names as the papers write them.
_LMC = (
    ("km", "metres", 1000, "length"),
    ("m", "centimetres", 100, "length"),
    ("cm", "millimetres", 10, "length"),
    ("m", "millimetres", 1000, "length"),
    ("kg", "grams", 1000, "mass"),
    ("g", "milligrams", 1000, "mass"),
    ("tonnes", "kilograms", 1000, "mass"),
    ("litres", "millilitres", 1000, "capacity"),
    ("cm^3", "millilitres", 1, "capacity"),
)


def _qty(v: Any, unit: str) -> str:
    """A measurement inside maths: ``7.9\\text{ kg}`` or ``25\\text{ cm}^{3}``."""
    text = v if isinstance(v, str) else _dec_str(v)
    if "^" in unit:
        base, power = unit.split("^")
        return math(f"{text}\\text{{ {base}}}^{{{power}}}")
    return math(f"{text}\\text{{ {unit}}}")


def _mu_value(rng: SeededRandom) -> Fraction:
    kind = rng.choice(("int", "int", "dec1", "dec2"))
    if kind == "int":
        return Fraction(rng.randint(2, 95))
    if kind == "dec1":
        return Fraction(rng.randint(11, 480), 10)
    return Fraction(rng.randint(105, 990), 100) if rng.chance(1, 2) else Fraction(rng.randint(5, 95), 100)


def _mu_l1(rng: SeededRandom) -> _Spec:
    frm, to, f, kind = rng.choice(_LMC)
    down = rng.chance(2, 3) or f == 1
    v = _mu_value(rng)
    if down:
        ask_from, ask_to, factor = frm, to, f
        value = v * f
    else:
        # convert the small unit back to the large one
        ask_from, ask_to, factor = to, frm, Fraction(1, f)
        v = Fraction(rng.randint(20, 9500), rng.choice((1, 10)))
        value = v / f
    names = {"metres": "metres", "millimetres": "millimetres", "centimetres": "centimetres", "grams": "grams", "milligrams": "milligrams", "kilograms": "kilograms", "millilitres": "millilitres", "litres": "litres", "km": "kilometres", "m": "metres", "cm": "centimetres", "kg": "kilograms", "g": "grams", "tonnes": "tonnes", "cm^3": "cm^3"}
    unit_from_txt = _qty(v, ask_from)
    to_name = names[ask_to] if ask_to != "cm^3" else "cubic centimetres"
    question = f"Convert {unit_from_txt} to {to_name}."
    f_eff = f if down else f
    dl = []
    if f > 1:
        dl += [
            ("factor_100", v * 100 if down else v / 100),
            ("factor_10000", v * 10000 if down else v / 10000),
            ("wrong_direction", v / f if down else v * f),
        ]
    else:
        dl += [("factor_100", v * 100), ("wrong_direction", v / 1000)]
    steps = [(f"multiply by {f}" if down else f"divide by {f}", _dec_str(value))]
    return _numeric_spec(
        "length_mass_capacity", question, value, steps, dl, {"task": "convert", "from": ask_from, "to": ask_to, "value": _dec_str(v)}
    )


_AV = (
    ("m^2", "cm^2", 10_000, "100"),
    ("cm^2", "mm^2", 100, "10"),
    ("km^2", "m^2", 1_000_000, "1000"),
    ("m^3", "cm^3", 1_000_000, "100"),
    ("cm^3", "mm^3", 1000, "10"),
    ("m^3", "litres", 1000, None),
    ("litres", "cm^3", 1000, None),
)


def _mu_l2(rng: SeededRandom) -> _Spec:
    frm, to, f, lin = rng.choice(_AV)
    down = rng.chance(2, 3)
    if down:
        v = rng.choice((Fraction(rng.randint(2, 40)), Fraction(rng.randint(11, 190), 10), Fraction(rng.randint(5, 95), 100)))
        value = v * f
        a, b = frm, to
    else:
        v = Fraction(rng.randint(2, 900) * (f // 100 if f >= 100 else 1))
        value = v / f
        a, b = to, frm
    names = {"m^2": "square metres", "cm^2": "square centimetres", "mm^2": "square millimetres", "km^2": "square kilometres", "m^3": "cubic metres", "cm^3": "cubic centimetres", "mm^3": "cubic millimetres", "litres": "litres"}
    shown_from = _qty(v, a)
    question = f"Convert {shown_from} to {names[b]}."
    dl = []
    if lin is not None:
        lf = int(lin)
        dl.append(("linear_factor", v * lf if down else v / lf))
        dl.append(("factor_off", v * (f // 10) if down else v / (f // 10)))
    else:
        dl.append(("factor_off", v * (f // 10) if down else v / (f // 10)))
    dl.append(("wrong_direction", v / f if down else v * f))
    steps = [(f"multiply by {f}" if down else f"divide by {f}", _dec_str(value))]
    return _numeric_spec(
        "area_volume", question, value, steps, dl, {"task": "convert_area_volume", "from": a, "to": b, "value": _dec_str(v)}
    )


def _mu_l3(rng: SeededRandom) -> _Spec:
    to_ms = rng.chance(1, 2)
    if to_ms:
        ms = Fraction(rng.randint(2, 40) * rng.choice((1, 1, 2)), rng.choice((1, 2)))
        kmh = ms * Fraction(36, 10)
        context = rng.choice(("A cheetah", "A train", "A cyclist", "A minibus"))
        question = f"{context} travels at {_qty(kmh, 'km/h')}. Convert this speed to metres per second."
        value = ms
        dl = [("wrong_direction", kmh * Fraction(36, 10)), ("factor_36", kmh / 36), ("factor_60", kmh / 60)]
        steps = [("divide by 3.6", _dec_str(ms))]
    else:
        ms = Fraction(rng.randint(2, 50), rng.choice((1, 2, 5)))
        kmh = ms * Fraction(36, 10)
        context = rng.choice(("A runner", "A bus", "A racing pigeon", "A bicycle"))
        question = f"{context} travels at {_qty(ms, 'm/s')}. Convert this speed to kilometres per hour."
        value = kmh
        dl = [("wrong_direction", ms / Fraction(36, 10)), ("factor_36", ms * 36), ("factor_60", ms * 60)]
        steps = [("multiply by 3.6", _dec_str(kmh))]
    for code, d in list(dl):
        try:
            _dec_str(d)
        except _Retry:
            pass
    return _numeric_spec(
        "speed_conversion", question, value, steps, dl, {"task": "speed_conversion", "to_ms": to_ms, "kmh": _dec_str(kmh), "ms": _dec_str(ms)}
    )


def _mu_l4(rng: SeededRandom) -> _Spec:
    kind = rng.choice(("density", "density_back", "litres_per_min", "kmh_to_m_per_min"))
    if kind == "density":
        v = Fraction(rng.randint(5, 220), 10)
        metal = rng.choice(("aluminium", "iron", "copper", "granite", "pine wood", "sandstone"))
        question = f"The density of {metal} is {_qty(v, 'g/cm^3')}. Write this density in kilograms per cubic metre."
        value = v * 1000
        dl = [("factor_off", v * 100), ("no_conversion", v), ("wrong_direction", v / 1000)]
        steps = [("1 g/cm^3 = 1000 kg/m^3, so multiply by 1000", _dec_str(value))]
    elif kind == "density_back":
        v = Fraction(rng.randint(5, 220) * 100, 1)
        question = f"The density of a metal is {_qty(v, 'kg/m^3')}. Write this density in grams per cubic centimetre."
        value = v / 1000
        dl = [("factor_off", v / 100), ("wrong_direction", v * 1000), ("no_conversion", v)]
        steps = [("divide by 1000", _dec_str(value))]
    elif kind == "litres_per_min":
        lpm = Fraction(rng.randint(2, 30) * 3)
        tap = rng.choice(("A tap", "A borehole pump", "A hose", "A water pump"))
        question = ''.join([format(tap, ''), ' fills a tank at ', format(math(_dec_str(lpm) + '\\text{ litres per minute}'), ''), '. Convert this rate to millilitres per second.'])
        value = lpm * 1000 / 60
        dl = [("time_not_converted", lpm * 1000), ("factor_off", lpm * 100 / 60), ("wrong_direction", lpm * 1000 * 60)]
        steps = [("convert litres to millilitres", _dec_str(lpm * 1000)), ("convert minutes to seconds by dividing by 60", _dec_str(value))]
    else:
        kmh = Fraction(rng.randint(2, 30) * 3)
        question = ''.join(['A truck travels at ', format(math(_dec_str(kmh) + '\\text{ km/h}'), ''), '. Convert this speed to metres per minute.'])
        value = kmh * 1000 / 60
        dl = [("time_not_converted", kmh * 1000), ("factor_off", kmh * 100 / 60), ("wrong_direction", kmh * 1000 * 60)]
        steps = [("convert kilometres to metres", _dec_str(kmh * 1000)), ("divide by 60 to change hours to minutes", _dec_str(value))]
    try:
        _dec_str(value)
    except _Retry:
        # 1000/60 = 50/3 is only terminating for multiples of 3; guaranteed by construction
        raise
    return _numeric_spec(
        "compound_units", question, value, steps, dl, {"task": kind, "answer": _dec_str(value)}
    )


class MetricUnitsGenerator(_FamilyGenerator):
    generator_id = "nssco_metric_units_conversions"
    version = 1
    levels = (1, 2, 3, 4)
    level_skills = MU_LEVEL_SKILLS
    error_notes = MU_NOTES
    builders = {1: _mu_l1, 2: _mu_l2, 3: _mu_l3, 4: _mu_l4}



# ==========================================================================
# 15804 Time, Clocks, and Timetables
# ==========================================================================

TT_NOTES: Dict[str, Dict[str, str]] = {
    "duration_minutes": {
        "decimal_subtraction": "subtracted the clock times as ordinary numbers, forgetting that an hour has 60 minutes, not 100",
        "hour_not_counted": "ignored the hour change and subtracted only the minutes",
    },
    "duration_hours_minutes": {
        "decimal_subtraction": "subtracted the minutes as if there were 100 in an hour, so the minutes part is wrong",
        "hour_off_by_one": "was one hour out after borrowing from the hours",
        "wrong_period": "treated the later time as if it were on the 12-hour clock",
    },
    "clock_time_after": {
        "no_carry": "added the minutes but did not carry the extra hour",
        "sign_dropped": "found the number of minutes but gave the time on the wrong side of the hour",
        "subtracted_instead": "subtracted the time when it should have been added, or the other way round",
    },
    "decimal_hours": {
        "minutes_as_decimal": "wrote the minutes straight after the decimal point (for example 2 h 18 min as 2.18 hours)",
        "decimal_as_minutes": "read the decimal part of the hours as minutes (for example 3.35 hours as 3 h 35 min)",
    },
    "latest_departure": {
        "added_instead": "added the journey time to the arrival time instead of subtracting",
        "no_borrow": "subtracted the minutes the wrong way round and did not borrow an hour",
    },
    "timetable_total": {
        "wait_ignored": "left out the waiting time between the two journeys",
        "wait_twice": "counted the waiting time twice",
        "second_leg_only": "added only the second journey to the departure time",
    },
}

TT_LEVEL_SKILLS = {
    1: ("duration_minutes",),
    2: ("duration_hours_minutes",),
    3: ("clock_time_after",),
    4: ("decimal_hours", "latest_departure"),
    5: ("timetable_total",),
}


def _hhmm(m: int) -> str:
    m %= 1440
    return f"{m // 60:02d}:{m % 60:02d}"


def _dur(m: int) -> str:
    h, mi = divmod(m, 60)
    parts = []
    if h:
        parts.append(f"{h} hour" + ("s" if h != 1 else ""))
    if mi or not h:
        parts.append(f"{mi} minute" + ("s" if mi != 1 else ""))
    return " ".join(parts)


def _time_spec(
    skill: str,
    question: str,
    value: int,
    shown: str,
    typed: str,
    wrongs: Sequence[Tuple[str, int, str, str]],
    steps: Sequence[Tuple[str, str]],
    machine: Dict[str, Any],
    clock: bool,
) -> _Spec:
    """``wrongs`` are (code, minutes, display, typed); keys are minutes (mod a day for clock times)."""
    mod = 1440 if clock else 10**9
    dists = [(c, math(d) if False else d, t, m % mod) for c, m, d, t in wrongs]
    return _Spec(
        skill=skill,
        question=question,
        answer=shown,
        typed=typed,
        expected=[typed],
        answer_type="time_or_date",
        correct_key=value % mod,
        steps=list(steps),
        dists=dists,
        machine=dict(machine, answer=typed),
    )


def _tt_l1(rng: SeededRandom) -> _Spec:
    for _ in range(300):
        h = rng.randint(6, 20)
        m1 = rng.randint(10, 55)
        d = rng.randint(15, 58)
        start = h * 60 + m1
        end = start + d
        if end // 60 == h + 1 and (end % 60) < m1:
            break
    else:
        raise _Retry
    place = rng.choice(_TOWNS)
    vehicle = rng.choice(("A bus", "A taxi", "A train", "A minibus"))
    question = (
        f"{vehicle} leaves {place} at {math(_hhmm(start))} and arrives at {math(_hhmm(end))}. "
        f"How many minutes did the journey take?"
    )
    # decimal subtraction: (end hh.mm) - (start hh.mm) read as numbers of hundred
    dec = (end // 60 * 100 + end % 60) - (start // 60 * 100 + start % 60)
    wrongs = [("decimal_subtraction", dec, f"{dec} minutes", f"{dec} minutes")]
    only_minutes = abs((end % 60) - (start % 60))
    wrongs.append(("hour_not_counted", only_minutes, f"{only_minutes} minutes", f"{only_minutes} minutes"))
    shown = f"{d} minutes"
    steps = [(f"minutes from {_hhmm(start)} to the next hour", str(60 - m1)), ("add the minutes after the hour", str(end % 60)), ("total minutes", str(d))]
    return _time_spec("duration_minutes", question, d, shown, shown, wrongs, steps, {"task": "duration_minutes", "start": _hhmm(start), "end": _hhmm(end)}, False)


def _tt_l2(rng: SeededRandom) -> _Spec:
    for _ in range(500):
        start = rng.randint(0, 23 * 60 + 59)
        d = rng.randint(65, 14 * 60)
        end = start + d
        if end >= 1440 and rng.chance(2, 3):
            continue
        borrow = (end % 60) < (start % 60)
        if borrow or rng.chance(1, 4):
            break
    else:
        raise _Retry
    next_day = end >= 1440
    place1 = rng.choice(_TOWNS)
    vehicle = rng.choice(("A flight", "A bus", "A train", "A truck"))
    when = " the next day" if next_day else ""
    question = (
        f"{vehicle} from {place1} leaves at {math(_hhmm(start))} and arrives at {math(_hhmm(end))}{when}. "
        f"Calculate the journey time in hours and minutes."
    )
    sh, sm = divmod(start % 1440, 60)
    eh, em = divmod(end % 1440 + (1440 if next_day else 0), 60)
    decimal_minutes = (eh * 100 + em) - (sh * 100 + sm)
    dec_h, dec_m = divmod(decimal_minutes, 100)
    wrongs = []
    if borrow:
        wrongs.append(("decimal_subtraction", dec_h * 60 + dec_m, f"{dec_h} hours {dec_m} minutes", f"{dec_h} hours {dec_m} minutes"))
        wrongs.append(("hour_off_by_one", d + 60, _dur(d + 60), _dur(d + 60)))
    else:
        wrongs.append(("hour_off_by_one", d - 60, _dur(d - 60), _dur(d - 60)))
    twelve = end % 1440
    if twelve >= 13 * 60:
        t12 = (twelve - 12 * 60) - (start % 1440) if (twelve - 12 * 60) > (start % 1440) else None
        if t12 is not None and t12 > 0 and t12 != d:
            wrongs.append(("wrong_period", t12, _dur(t12), _dur(t12)))
    steps = [("time from the start to midnight or the next whole hour", str(60 - start % 60)), ("add the remaining hours and minutes", _dur(d))]
    return _time_spec("duration_hours_minutes", question, d, _dur(d), _dur(d), wrongs, steps, {"task": "duration_hours_minutes", "start": _hhmm(start), "end": _hhmm(end)}, False)


def _tt_l3(rng: SeededRandom) -> _Spec:
    kind = rng.choice(("arrive", "late", "early_midnight"))
    if kind == "arrive":
        start = rng.randint(5 * 60, 18 * 60 + 59)
        d = rng.randint(55, 5 * 60 + 40)
        end = start + d
        h, m = divmod(d, 60)
        question = (
            f"A bus leaves Windhoek at {math(_hhmm(start))}. The journey takes {_dur(d)}. "
            f"At what time does the bus arrive? Give your answer in the 24-hour clock."
        )
        if (start % 60) + m < 60:
            raise _Retry
        value = end
        no_carry = (start // 60 + h) * 60 + (start % 60 + m) % 60
        wrongs = [("no_carry", no_carry, _hhmm(no_carry), _hhmm(no_carry)), ("subtracted_instead", start - d, _hhmm(start - d), _hhmm(start - d))]
        steps = [("add the hours", _hhmm(start + h * 60)), ("add the minutes and carry the extra hour", _hhmm(end))]
    elif kind == "late":
        sched = rng.randint(5 * 60, 20 * 60 + 30)
        late = rng.randint(12, 55)
        if (sched % 60) + late < 60:
            raise _Retry
        end = sched + late
        place = rng.choice(_TOWNS)
        question = (
            f"A flight from {place} is scheduled to take off at {math(_hhmm(sched))}. It takes off {late} minutes late. "
            f"At what time does it take off? Give your answer in the 24-hour clock."
        )
        value = end
        no_carry = (sched // 60) * 60 + (sched % 60 + late) % 60
        wrongs = [("no_carry", no_carry, _hhmm(no_carry), _hhmm(no_carry)), ("subtracted_instead", sched - late, _hhmm(sched - late), _hhmm(sched - late))]
        steps = [(f"add {late} minutes and carry the extra hour", _hhmm(end))]
    else:
        sched = rng.choice((0, 0, 1)) * 60 + rng.randint(1, 14)
        early = rng.randint(sched % 60 + 1, sched % 60 + 40) if sched < 60 else rng.randint(sched % 60 + 1, 40)
        end = sched - early
        question = (
            f"A plane is scheduled to land at {math(_hhmm(sched))}. It lands {early} minutes before its scheduled time. "
            f"At what time does it land? Give your answer in the 24-hour clock."
        )
        value = end
        diff = early - sched
        wrongs = [("sign_dropped", diff, _hhmm(diff), _hhmm(diff)), ("subtracted_instead", sched + early, _hhmm(sched + early), _hhmm(sched + early))]
        steps = [(f"go back {early} minutes, crossing midnight if needed", _hhmm(end))]
    shown = _hhmm(value)
    return _time_spec("clock_time_after", question, value, shown, shown, wrongs, steps, {"task": kind, "answer": shown}, True)


def _tt_l4(rng: SeededRandom) -> _Spec:
    kind = rng.choice(("hours_to_hm", "hm_to_decimal", "latest_departure", "latest_departure"))
    if kind == "hours_to_hm":
        h = rng.randint(1, 6)
        minutes = rng.choice([6, 12, 18, 21, 24, 30, 33, 36, 42, 45, 48, 54, 9, 15, 27, 39, 51])
        dec = Fraction(h * 60 + minutes, 60)
        if dec.denominator not in (1, 2, 4, 5, 10, 20, 25, 50, 100):
            raise _Retry
        question = f"A journey takes {math(_dec_str(dec))} hours. Write this time in hours and minutes."
        value = h * 60 + minutes
        mm = int(round((dec - h) * 100))
        wrongs = [("decimal_as_minutes", h * 60 + mm, _dur(h * 60 + mm), _dur(h * 60 + mm))]
        if mm < 60 and h * 60 + mm == value:
            wrongs = []
        steps = [("multiply the decimal part by 60", str(minutes))]
        return _time_spec("decimal_hours", question, value, _dur(value), _dur(value), wrongs, steps, {"task": kind, "hours": _dec_str(dec)}, False)
    if kind == "hm_to_decimal":
        h = rng.randint(1, 5)
        minutes = rng.choice([6, 12, 18, 24, 30, 36, 42, 48, 54, 15, 45, 9, 21])
        dec = Fraction(h * 60 + minutes, 60)
        if dec.denominator not in (1, 2, 4, 5, 10, 20, 25, 50, 100):
            raise _Retry
        question = f"A repair takes {_dur(h * 60 + minutes)}. Write this time as a decimal number of hours."
        wrongs = [("minutes_as_decimal", Fraction(h * 100 + minutes, 100))]
        dists = []
        for c, v in wrongs:
            if v != dec:
                dists.append((c, math(_dec_str(v)), _dec_str(v), v))
        return _Spec(
            skill="decimal_hours",
            question=question,
            answer=math(_dec_str(dec)),
            typed=_dec_str(dec),
            expected=[_dec_str(dec)],
            answer_type="number_exact",
            correct_key=dec,
            steps=[("divide the minutes by 60", _dec_str(Fraction(minutes, 60))), ("add the whole hours", _dec_str(dec))],
            dists=dists,
            machine={"task": kind, "h": h, "m": minutes, "answer": _dec_str(dec)},
        )
    arrive = rng.randint(30, 23 * 60 + 40)
    d = rng.randint(45, 5 * 60 + 50)
    start = arrive - d
    h, m = divmod(d, 60)
    place = rng.choice(_TOWNS)
    question = (
        f"A bus must arrive in {place} at {math(_hhmm(arrive))}. The journey takes {_dur(d)}. "
        f"Find the latest time the bus can leave. Give your answer in the 24-hour clock."
    )
    wrongs = [("added_instead", arrive + d, _hhmm(arrive + d), _hhmm(arrive + d))]
    if (arrive % 60) < m:
        no_borrow = ((arrive // 60) - h) * 60 + (m - arrive % 60)
        wrongs.append(("no_borrow", no_borrow, _hhmm(no_borrow), _hhmm(no_borrow)))
    shown = _hhmm(start)
    steps = [(f"subtract {h} hours", _hhmm(arrive - h * 60)), (f"subtract {m} minutes, borrowing an hour if needed", shown)]
    return _time_spec("latest_departure", question, start, shown, shown, wrongs, steps, {"task": kind, "answer": shown}, True)


def _tt_l5(rng: SeededRandom) -> _Spec:
    for _ in range(300):
        depart = rng.randint(5 * 60, 15 * 60 + 40)
        l1 = rng.randint(70, 4 * 60 + 40)
        wait = rng.randint(15, 55)
        l2 = rng.randint(50, 3 * 60 + 50)
        arrive = depart + l1 + wait + l2
        if arrive < 1440:
            break
    else:
        raise _Retry
    a, b, c = _TOWNS_TRIP[rng.randint(0, len(_TOWNS_TRIP) - 1)]
    h1, m1 = divmod(l1, 60)
    h2, m2 = divmod(l2, 60)
    ask_total = rng.chance(1, 2)
    base = (
        f"A bus leaves {a} at {math(_hhmm(depart))} and travels to {b}. The journey takes {_dur(l1)}. "
        f"The bus waits in {b} for {wait} minutes and then travels to {c}. The second journey takes {_dur(l2)}. "
    )
    if ask_total:
        total = l1 + wait + l2
        question = base + f"Calculate the total time from leaving {a} to arriving in {c}, in hours and minutes."
        wrongs = [
            ("wait_ignored", l1 + l2, _dur(l1 + l2), _dur(l1 + l2)),
            ("wait_twice", l1 + 2 * wait + l2, _dur(l1 + 2 * wait + l2), _dur(l1 + 2 * wait + l2)),
        ]
        steps = [("first journey", _dur(l1)), ("add the wait", _dur(l1 + wait)), ("add the second journey", _dur(total))]
        return _time_spec("timetable_total", question, total, _dur(total), _dur(total), wrongs, steps, {"task": "total_time", "answer": _dur(total)}, False)
    question = base + f"At what time does the bus arrive in {c}? Give your answer in the 24-hour clock."
    wrongs = [
        ("wait_ignored", depart + l1 + l2, _hhmm(depart + l1 + l2), _hhmm(depart + l1 + l2)),
        ("wait_twice", depart + l1 + 2 * wait + l2, _hhmm(depart + l1 + 2 * wait + l2), _hhmm(depart + l1 + 2 * wait + l2)),
        ("second_leg_only", depart + l2, _hhmm(depart + l2), _hhmm(depart + l2)),
    ]
    steps = [("arrival in the first town", _hhmm(depart + l1)), ("leave after the wait", _hhmm(depart + l1 + wait)), ("arrive after the second journey", _hhmm(arrive))]
    return _time_spec("timetable_total", question, arrive, _hhmm(arrive), _hhmm(arrive), wrongs, steps, {"task": "arrival_time", "answer": _hhmm(arrive)}, True)


_TOWNS_TRIP = (
    ("Windhoek", "Otjiwarongo", "Tsumeb"),
    ("Walvis Bay", "Swakopmund", "Windhoek"),
    ("Keetmanshoop", "Mariental", "Windhoek"),
    ("Rundu", "Grootfontein", "Windhoek"),
    ("Oshakati", "Ondangwa", "Rundu"),
    ("Gobabis", "Windhoek", "Walvis Bay"),
)


class TimeClocksTimetablesGenerator(_FamilyGenerator):
    generator_id = "nssco_time_clocks_timetables"
    version = 1
    levels = (1, 2, 3, 4, 5)
    level_skills = TT_LEVEL_SKILLS
    error_notes = TT_NOTES
    builders = {1: _tt_l1, 2: _tt_l2, 3: _tt_l3, 4: _tt_l4, 5: _tt_l5}


GENERATORS = [
    NumberClassificationsGenerator(),
    DirectedNumbersGenerator(),
    StandardFormEstimatesGenerator(),
    LimitsOfAccuracyGenerator(),
    PersonalFinanceGenerator(),
    MetricUnitsGenerator(),
    TimeClocksTimetablesGenerator(),
]
