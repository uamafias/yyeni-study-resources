"""Generators for NSSCO Mathematics lessons 15826 (Logarithms), 15825 (Sequences)
and 15827 (Functions).

The levels copy the question shapes, mark sizes and answer forms of the 2020-2024
papers (see ``analysis/raw`` in the study-resources workspace) without reusing
any wording or numbers. Every problem is built from chosen parameters, so the
answer is known exactly; the displayed question, the typed answer the marker
reads, the model working (``steps``) and the wrong answers from known mistakes
all come from the same parameters.

Logarithms (all to base 10 where a value is needed)
  1. Evaluate a sum/difference/multiple of logs of powers of 10, no calculator.
  2. Split one logarithm into separate logarithms, or write one in terms of ``m``.
  3. Write a sum of logarithm terms as a single logarithm.
  4. Solve ``a^x = c`` or ``a^(x+b) = c`` using logarithms, to 3 significant figures.
  5. Solve ``k a^x = c`` or ``a^(px+q) = c`` using logarithms, to 3 significant figures.

Sequences
  1. Write down the next term of an arithmetic sequence.
  2. Find the nth term of a linear sequence (sometimes in a savings context).
  3. Find the number of terms of an arithmetic progression.
  4. Find ``a`` and ``d`` from two terms, or the sum of an arithmetic series.
  5. Terms of an arithmetic progression that form a geometric progression: find the ratio.

Functions
  1. Evaluate ``f(k)`` (linear, squaring, ``c - x^2``), or solve ``x^3 = n``.
  2. Find the inverse of a linear function.
  3. Composite value, solve ``f(x) = px + q``, or ``g(kx)``.
  4. Simplify a composite of two linear functions.
  5. Simplify a composite that involves a squaring function.
"""

from __future__ import annotations

import math
from decimal import ROUND_HALF_UP, Decimal
from fractions import Fraction
from typing import Callable, Dict, List, Mapping, Optional, Sequence, Tuple

from .base import Distractor, GeneratedProblem, GeneratorError, MathGenerator, SeededRandom, Step
from .formatting import math as tex, number_latex, polynomial_latex

LOG_ID = "nssco_logarithms"
SEQ_ID = "nssco_sequences"
FUN_ID = "nssco_functions"

_MAX_ATTEMPTS = 400
_PROBES_X = (1.7, -2.3, 3.1)  # irrational-looking points used to tell two expressions apart
_PROBES_LOG = (1.7, 2.9, 4.3)  # positive points, for expressions that contain a logarithm


def _require(condition: bool, message: str) -> None:
    if not condition:
        raise GeneratorError(message)


# --------------------------------------------------------------------------
# Shared helpers
# --------------------------------------------------------------------------


class _Cand:
    """A wrong answer: ``probe`` is its value(s) at fixed test points, so we can
    prove it differs from the right answer without a computer algebra system."""

    __slots__ = ("code", "display", "typed", "probe")

    def __init__(self, code: str, display: str, typed: str, probe: Sequence[float]) -> None:
        self.code, self.display, self.typed, self.probe = code, display, typed, tuple(probe)


def _same_probe(a: Sequence[float], b: Sequence[float]) -> bool:
    return len(a) == len(b) and all(abs(x - y) <= 1e-9 * max(1.0, abs(x), abs(y)) for x, y in zip(a, b))


def _distractors(
    notes: Mapping[str, str],
    correct_display: str,
    correct_typed: str,
    correct_probe: Sequence[float],
    candidates: Sequence[_Cand],
) -> Tuple[Distractor, ...]:
    out: List[Distractor] = []
    seen_probe: List[Sequence[float]] = [correct_probe]
    seen_display = {correct_display}
    seen_typed = {correct_typed.replace(" ", "")}
    for c in candidates:
        if c.display in seen_display or c.typed.replace(" ", "") in seen_typed:
            continue
        if any(_same_probe(c.probe, p) for p in seen_probe):
            continue
        seen_probe.append(c.probe)
        seen_display.add(c.display)
        seen_typed.add(c.typed.replace(" ", ""))
        out.append(Distractor(c.display, c.code, notes[c.code], typed=c.typed))
    return tuple(out)


def _sig(value: float, digits: int = 3) -> Decimal:
    """``value`` rounded half-up to ``digits`` significant figures."""
    d = Decimal(repr(float(value)))
    if d == 0:
        return d
    exp = d.adjusted() - (digits - 1)
    return d.quantize(Decimal(1).scaleb(exp), rounding=ROUND_HALF_UP)


def _sig_text(value: float, digits: int = 3) -> str:
    return format(_sig(value, digits), "f")


def _short_exact(x: Fraction) -> bool:
    """A terminating decimal that already has at most 3 significant figures (0.5, -2.25, 12): it can be written exactly as '3 s.f.'."""
    if not _is_terminating(x):
        return False
    digits = _dec_text(x).lstrip("-").replace(".", "").lstrip("0")
    return len(digits) <= 3


def _safe_rounding(value: float, digits: int = 3) -> bool:
    """False when ``value`` sits so close to a rounding boundary that float error could matter."""
    if value == 0:
        return False
    scaled = abs(value) / (10 ** (math.floor(math.log10(abs(value))) - (digits - 1)))
    return abs((scaled - math.floor(scaled)) - 0.5) > 0.02


def _frac_text(f: Fraction) -> str:
    return str(f.numerator) if f.denominator == 1 else f"{f.numerator}/{f.denominator}"


def _dec_text(f: Fraction) -> str:
    """A terminating fraction as a plain decimal: 3/8 -> 0.375, 5 -> 5."""
    if f.denominator == 1:
        return str(f.numerator)
    text = format(Decimal(f.numerator) / Decimal(f.denominator), "f")
    return text.rstrip("0").rstrip(".") if "." in text else text


def _is_terminating(f: Fraction) -> bool:
    d = f.denominator
    for p in (2, 5):
        while d % p == 0:
            d //= p
    return d == 1


def _nonzero(rng: SeededRandom, low: int, high: int) -> int:
    value = 0
    while value == 0:
        value = rng.randint(low, high)
    return value


def _is_prime_power(n: int) -> bool:
    if n < 2:
        return False
    for p in range(2, int(n**0.5) + 1):
        if n % p == 0:
            while n % p == 0:
                n //= p
            return n == 1
    return True


def _ordinal(n: int) -> str:
    if 10 <= n % 100 <= 20:
        suffix = "th"
    else:
        suffix = {1: "st", 2: "nd", 3: "rd"}.get(n % 10, "th")
    return f"{n}{suffix}"


def _pow_text(base: int, exponent: int) -> str:
    """``10`` to a (possibly negative) power as a plain number: 1000, 0.01."""
    if exponent >= 0:
        return str(base**exponent)
    return "0." + "0" * (-exponent - 1) + "1"


def _signed(v: int) -> str:
    """`` + 4`` or `` - 4``."""
    return f" + {v}" if v >= 0 else f" - {-v}"


def _lin(a: int, b: int, var: str = "x") -> str:
    return polynomial_latex([a, b], var)


def _lin_tex_styled(a: int, b: int, style: int, var: str = "x") -> str:
    """``ax + b`` (style 0) or ``b + ax`` (style 1), the way papers write both."""
    if style == 1 and b != 0:
        return f"{b} {'-' if a < 0 else '+'} {'' if abs(a) == 1 else abs(a)}{var}"
    return _lin(a, b, var)


def _problem(
    gen: MathGenerator,
    seed: int,
    level: int,
    skill: str,
    question: str,
    answer: str,
    distractors: Tuple[Distractor, ...],
    steps: Sequence[Step],
    marking: Mapping[str, object],
    machine: Mapping[str, object],
) -> GeneratedProblem:
    return GeneratedProblem(
        generator_id=gen.generator_id,
        generator_version=gen.version,
        seed=seed,
        level=level,
        skill=skill,
        question=question,
        answer=answer,
        distractors=distractors,
        machine=dict(machine),
        steps=tuple(steps),
        marking=dict(marking),
    )


# ==========================================================================
# Logarithms (lesson 15826)
# ==========================================================================

LOG_NOTES: Dict[str, Dict[str, str]] = {
    "evaluate_log_powers": {
        "multiplied_exponents": "multiplied the two powers instead of adding them (treated a sum of logarithms as a product)",
        "added_numbers": "added the numbers inside the logarithms instead of the exponents",
        "added_instead_of_subtracting": "added the exponents when the logarithms were subtracted",
        "divided_exponents": "divided the exponents instead of subtracting them",
        "added_multiplier": "added the multiplier to the exponent instead of multiplying",
        "multiplier_dropped": "ignored the multiplier in front of the logarithm",
    },
    "split_log": {
        "power_law_misapplied": "turned the power into a plain multiple of x instead of a multiple of log x",
        "multiplier_on_constant": "put the power in front of the log of the constant instead of the log of x",
        "power_split_as_product": "split the power into a product of the index and x inside separate logarithms",
        "root_as_x": "wrote the root as an extra x instead of one half of log x",
        "log_of_difference": "wrote the difference of two logarithms as one logarithm of the difference",
        "sign_of_second_term": "added the two logarithms when the original was a quotient",
    },
    "log_in_terms_of_m": {
        "wrote_log_m": "wrote log of m instead of a multiple of m",
        "power_added": "added the index to m instead of multiplying m by it",
        "sign_lost": "lost the negative sign from the reciprocal",
        "indices_added": "added the indices of the numerator and denominator instead of subtracting",
    },
    "combine_logs": {
        "constant_forgotten": "left out the constant term when combining the logarithms",
        "added_inside_log": "added the terms inside one logarithm instead of multiplying them",
        "power_misapplied": "multiplied the variable by the index instead of raising it to the index",
        "log_of_sum_expanded": "expanded the logarithm of a sum as the sum of two logarithms",
        "summed_instead_of_combined": "added the numbers instead of multiplying them",
        "quotient_as_product": "multiplied by the term that should have been divided",
        "subtracted_inside": "subtracted inside the logarithm instead of dividing",
    },
    "solve_exponential": {
        "ratio_inverted": "divided the logarithms the wrong way round",
        "divided_values_not_logs": "divided the two numbers instead of dividing their logarithms",
        "premature_rounding": "rounded the logarithms before dividing, so the answer is not accurate to 3 significant figures",
        "too_few_figures": "gave the answer to fewer than 3 significant figures",
        "power_not_removed": "forgot to take the constant out of the power after dividing the logarithms",
        "constant_sign_error": "moved the constant in the power across with the wrong sign",
        "bases_multiplied": "multiplied the number in front by the base before taking logarithms",
        "not_divided_first": "did not divide both sides by the number in front before taking logarithms",
        "forgot_to_divide_by_coefficient": "did not divide by the coefficient of x in the power",
    },
}

LOG_LEVEL_SKILLS: Dict[int, Tuple[str, ...]] = {
    1: ("evaluate_log_powers",),
    2: ("split_log", "log_in_terms_of_m"),
    3: ("combine_logs",),
    4: ("solve_exponential",),
    5: ("solve_exponential",),
}

_SPLIT_CONSTANTS = [k for k in range(6, 100) if not _is_prime_power(k) and k not in (10, 100)] + [10]
_BASES = (2, 3, 5, 6, 7)


def _lg(v: float) -> float:
    return math.log(v)


# ---- level 1 ---------------------------------------------------------------


def _log_level1(rng: SeededRandom, gen: MathGenerator):
    notes = LOG_NOTES["evaluate_log_powers"]
    shape = rng.choice(("sum", "diff", "multiple"))
    exps = [e for e in range(-3, 5) if e != 0]
    if shape == "sum":
        a, b = rng.choice(exps), rng.choice(exps)
        value = a + b
        question_expr = f"\\log {_pow_text(10, a)} + \\log {_pow_text(10, b)}"
        cands = [
            _Cand("multiplied_exponents", tex(str(a * b)), str(a * b), (a * b,)),
            _Cand(
                "added_numbers",
                tex(str(Fraction(10) ** a + Fraction(10) ** b)),
                str(float(Fraction(10) ** a + Fraction(10) ** b)),
                (float(Fraction(10) ** a + Fraction(10) ** b),),
            ),
        ]
        steps = [
            Step(f"Write the first logarithm as its exponent, since the number is a power of 10", str(a)),
            Step("Write the second logarithm as its exponent", str(b)),
            Step("Add the exponents", str(value)),
        ]
    elif shape == "diff":
        a, b = rng.choice(exps), rng.choice(exps)
        while a == b:
            b = rng.choice(exps)
        value = a - b
        question_expr = f"\\log {_pow_text(10, a)} - \\log {_pow_text(10, b)}"
        cands = [
            _Cand("added_instead_of_subtracting", tex(str(a + b)), str(a + b), (a + b,)),
            _Cand("divided_exponents", tex(number_latex(Fraction(a, b))), _frac_text(Fraction(a, b)), (a / b,)),
        ]
        steps = [
            Step("Write the first logarithm as its exponent", str(a)),
            Step("Write the second logarithm as its exponent", str(b)),
            Step("Subtract the exponents", str(value)),
        ]
    else:
        n, a = rng.randint(2, 5), rng.choice([1, 2, 3, 4, -1, -2])
        value = n * a
        question_expr = f"{n}\\log {_pow_text(10, a)}"
        cands = [
            _Cand("added_multiplier", tex(str(n + a)), str(n + a), (n + a,)),
            _Cand("multiplier_dropped", tex(str(a)), str(a), (a,)),
        ]
        steps = [
            Step("Write the logarithm as its exponent", str(a)),
            Step("Multiply by the number in front", str(value)),
        ]
    question = f"Evaluate {tex(question_expr)} without using a calculator. Show your working."
    answer = tex(str(value))
    typed = str(value)
    marking = {"answer_type": "number_exact", "expected": [typed], "typed": typed}
    d = _distractors(notes, answer, typed, (value,), cands)
    return "evaluate_log_powers", question, answer, d, steps, marking, {"task": "evaluate_log", "shape": shape, "value": value}


# ---- level 2 ---------------------------------------------------------------


def _log_level2(rng: SeededRandom, gen: MathGenerator):
    shape = rng.choice(("power", "root", "quotient", "in_terms_of_m"))
    if shape == "in_terms_of_m":
        return _log_in_terms_of_m(rng)
    notes = LOG_NOTES["split_log"]
    k = rng.choice(_SPLIT_CONSTANTS)
    pts = _PROBES_LOG

    def probe(fn: Callable[[float], float]) -> List[float]:
        return [fn(x) for x in pts]

    if shape == "power":
        n = rng.randint(2, 5)
        arg = f"{k}x^{n}"
        question = ''.join(['Express ', format(tex(''.join(['\\log (', format(arg, ''), ')'])), ''), ' as separate logarithms.'])
        answer = tex(f"\\log {k} + {n}\\log x")
        typed = f"log({k}) + {n}*log(x)"
        correct_probe = probe(lambda x: _lg(k) + n * _lg(x))
        cands = [
            _Cand("power_law_misapplied", tex(f"\\log {k} + {n}x"), f"log({k}) + {n}*x", probe(lambda x: _lg(k) + n * x)),
            _Cand("multiplier_on_constant", tex(f"{n}\\log {k} + \\log x"), f"{n}*log({k}) + log(x)", probe(lambda x: n * _lg(k) + _lg(x))),
            _Cand(
                "power_split_as_product",
                tex(f"\\log {k} + \\log {n} + \\log x"),
                f"log({k}) + log({n}) + log(x)",
                probe(lambda x: _lg(k) + _lg(n) + _lg(x)),
            ),
        ]
        steps = [
            Step("Use the product law to separate the constant from the power", f"log({k}) + log(x^{n})"),
            Step("Use the power law on the second logarithm", typed),
        ]
        task = {"form": "k x^n", "k": k, "n": n}
    elif shape == "root":
        arg = f"{k}\\sqrt{{x}}"
        question = ''.join(['Express ', format(tex(''.join(['\\log (', format(arg, ''), ')'])), ''), ' as separate logarithms.'])
        answer = tex(f"\\log {k} + \\frac{{1}}{{2}}\\log x")
        typed = f"log({k}) + (1/2)*log(x)"
        correct_probe = probe(lambda x: _lg(k) + 0.5 * _lg(x))
        cands = [
            _Cand("root_as_x", tex(f"\\log {k} + x"), f"log({k}) + x", probe(lambda x: _lg(k) + x)),
            _Cand("power_law_misapplied", tex(f"\\log {k} + 2\\log x"), f"log({k}) + 2*log(x)", probe(lambda x: _lg(k) + 2 * _lg(x))),
            _Cand("multiplier_on_constant", tex(f"\\frac{{1}}{{2}}\\log {k} + \\log x"), f"(1/2)*log({k}) + log(x)", probe(lambda x: 0.5 * _lg(k) + _lg(x))),
        ]
        steps = [
            Step("Write the square root as a power of one half", f"log({k}) + log(x^(1/2))"),
            Step("Use the power law", typed),
        ]
        task = {"form": "k sqrt(x)", "k": k}
    else:
        n = rng.randint(2, 4)
        arg = f"\\frac{{x^{n}}}{{{k}}}"
        question = ''.join(['Express ', format(tex(''.join(['\\log \\left(', format(arg, ''), '\\right)'])), ''), ' as separate logarithms.'])
        answer = tex(f"{n}\\log x - \\log {k}")
        typed = f"{n}*log(x) - log({k})"
        correct_probe = probe(lambda x: n * _lg(x) - _lg(k))
        cands = [
            _Cand("sign_of_second_term", tex(f"{n}\\log x + \\log {k}"), f"{n}*log(x) + log({k})", probe(lambda x: n * _lg(x) + _lg(k))),
            _Cand("log_of_difference", tex(f"\\log ({n}x - {k})"), f"log({n}*x - {k})", probe(lambda x: _lg(abs(n * x - k)) if n * x != k else 0.0)),
            _Cand("power_law_misapplied", tex(f"{n}x - \\log {k}"), f"{n}*x - log({k})", probe(lambda x: n * x - _lg(k))),
        ]
        steps = [
            Step("Use the quotient law", f"log(x^{n}) - log({k})"),
            Step("Use the power law on the first logarithm", typed),
        ]
        task = {"form": "x^n / k", "k": k, "n": n}
    marking = {"answer_type": "expression", "expected": [typed], "typed": typed}
    d = _distractors(notes, answer, typed, correct_probe, cands)
    return "split_log", question, answer, d, steps, marking, {"task": "split_log", **task}


def _log_in_terms_of_m(rng: SeededRandom):
    notes = LOG_NOTES["log_in_terms_of_m"]
    p = rng.choice((2, 3, 5, 7))
    shape = rng.choice(("power", "reciprocal", "quotient", "root_quotient"))
    mvals = (0.7, 1.9, -0.4)
    if shape == "power":
        a = rng.randint(2, 5)
        arg, coef = f"{p ** a}", Fraction(a)
        cands = [
            ("wrote_log_m", f"{a}\\log m", f"{a}*log(m)", lambda m, a=a: a * _lg(abs(m)) if m else 0.0),
            ("power_added", f"m + {a}", f"m + {a}", lambda m, a=a: m + a),
        ]
        step1 = f"Write {p ** a} as a power of {p}"
        step1v = f"log({p}^{a})"
    elif shape == "reciprocal":
        a = rng.randint(1, 4)
        arg, coef = f"\\frac{{1}}{{{p ** a}}}", Fraction(-a)
        cands = [
            ("sign_lost", f"{a}m", f"{a}*m", lambda m, a=a: a * m),
            ("wrote_log_m", f"-{a}\\log m", f"-{a}*log(m)", lambda m, a=a: -a * _lg(abs(m)) if m else 0.0),
        ]
        step1 = f"Write the reciprocal of {p ** a} as a negative power of {p}"
        step1v = f"log({p}^(-{a}))"
    elif shape == "quotient":
        a = rng.randint(2, 5)
        b = rng.randint(1, a - 1)
        arg, coef = f"\\frac{{{p ** a}}}{{{p ** b}}}", Fraction(a - b)
        cands = [
            ("indices_added", f"{a + b}m", f"{a + b}*m", lambda m, a=a, b=b: (a + b) * m),
            ("wrote_log_m", f"{a - b}\\log m", f"{a - b}*log(m)", lambda m, a=a, b=b: (a - b) * _lg(abs(m)) if m else 0.0),
        ]
        step1 = f"Write the numerator and denominator as powers of {p}"
        step1v = f"log({p}^{a}/{p}^{b})"
    else:
        q = rng.choice((2, 3))
        b = rng.randint(1, 2)
        root = "\\sqrt" if q == 2 else "\\sqrt[3]"
        arg, coef = f"\\frac{{{root}{{{p}}}}}{{{p ** b}}}", Fraction(1, q) - b
        cands = [
            ("indices_added", number_latex(Fraction(1, q) + b) + "m", f"({_frac_text(Fraction(1, q) + b)})*m", lambda m, q=q, b=b: (1 / q + b) * m),
            ("sign_lost", number_latex(Fraction(1, q) - b)[1:] + "m" if (Fraction(1, q) - b) < 0 else number_latex(b - Fraction(1, q)) + "m",
             f"({_frac_text(b - Fraction(1, q))})*m", lambda m, q=q, b=b: (b - 1 / q) * m),
        ]
        step1 = f"Write the numerator and denominator as powers of {p}"
        step1v = f"log({p}^(1/{q})/{p}^{b})"
    question = (
        ''.join(['Given that ', format(tex(''.join(['\\log ', format(p, ''), ' = m'])), ''), ', express ', format(tex(''.join(['\\log \\left(', format(arg, ''), '\\right)']) if '\\frac' in arg else ''.join(['\\log ', format(arg, '')])), ''), ' in terms of ', format(tex('m'), ''), '.'])
    )
    coef_tex = number_latex(coef)
    answer_tex = {"1": "m", "-1": "-m"}.get(coef_tex, f"{coef_tex}m")
    answer = tex(answer_tex)
    typed = f"({_frac_text(coef)})*m" if coef.denominator != 1 else f"{coef.numerator}*m"
    correct_probe = [float(coef) * m for m in mvals]
    cand_objs = []
    for code, disp, typ, fn in cands:
        cand_objs.append(_Cand(code, tex(disp), typ, [fn(m) for m in mvals]))
    steps = [
        Step(step1, step1v),
        Step("Use the power law to bring down the index", typed),
    ]
    marking = {"answer_type": "expression", "expected": [typed], "typed": typed}
    d = _distractors(notes, answer, typed, correct_probe, cand_objs)
    return "log_in_terms_of_m", question, answer, d, steps, marking, {"task": "log_in_terms_of_m", "p": p, "coefficient": [coef.numerator, coef.denominator]}


# ---- level 3 ---------------------------------------------------------------


def _prod_tex(parts: Sequence[str]) -> str:
    return "".join(parts)


def _log_level3(rng: SeededRandom, gen: MathGenerator):
    notes = LOG_NOTES["combine_logs"]
    shape = rng.choice(("constant", "numbers", "powers"))
    pts = _PROBES_LOG
    if shape == "constant":
        c = rng.choice((1, 2))
        n = rng.randint(2, 4)
        t = rng.randint(1, 4)
        ten = 10**c
        lead = "1" if c == 1 else "2"
        expr = f"{lead} + {n}\\log x + \\log (x + {t})"
        question = f"Express {tex(expr)} as a single logarithm."
        arg = f"{ten}x^{n}(x + {t})"
        answer = tex(f"\\log ({arg})")
        typed = f"log({ten}*x^{n}*(x + {t}))"
        probe = lambda fn: [fn(x) for x in pts]
        correct_probe = probe(lambda x: _lg(ten * x**n * (x + t)))
        cands = [
            _Cand("constant_forgotten", tex(f"\\log (x^{n}(x + {t}))"), f"log(x^{n}*(x + {t}))", probe(lambda x: _lg(x**n * (x + t)))),
            _Cand("added_inside_log", tex(f"\\log ({ten}x^{n} + x + {t})"), f"log({ten}*x^{n} + x + {t})", probe(lambda x: _lg(abs(ten * x**n + x + t)))),
            _Cand("power_misapplied", tex(f"\\log ({ten}\\cdot {n}x(x + {t}))"), f"log({ten}*{n}*x*(x + {t}))", probe(lambda x: _lg(ten * n * x * (x + t)))),
            _Cand(
                "log_of_sum_expanded",
                tex(f"\\log ({ten}x^{n + 1}" + (f"" if t == 1 else f" \\cdot {t}") + ")"),
                f"log({ten}*{t}*x^{n + 1})" if t != 1 else f"log({ten}*x^{n + 1})",
                probe(lambda x: _lg(ten * t * x ** (n + 1))),
            ),
        ]
        steps = [
            Step(f"Write {lead} as a logarithm of {ten}", f"log({ten}) + {n}*log(x) + log(x + {t})"),
            Step("Use the power law to move the index inside the logarithm", f"log({ten}) + log(x^{n}) + log(x + {t})"),
            Step("Use the product law to combine", typed),
        ]
        task = {"form": "constant + n log x + log(x+t)", "constant": c, "n": n, "t": t}
    elif shape == "numbers":
        while True:
            a, b = rng.randint(2, 15), rng.randint(2, 15)
            c = rng.randint(2, 9)
            if (a * b) % c == 0:
                val = a * b // c
                if val >= 2 and val not in (a, b) and a != b and a + b - c >= 2 and a * b - c >= 2 and (a + b - c) != val and (a * b * c) != val and (a * b - c) != val:
                    break
        question = ''.join(['Write ', format(tex(''.join(['\\log ', format(a, ''), ' + \\log ', format(b, ''), ' - \\log ', format(c, '')])), ''), ' as a single logarithm.'])
        answer = tex(f"\\log {val}")
        typed = f"log({val})"
        correct_probe = (_lg(val),)
        cands = [
            _Cand("summed_instead_of_combined", tex(f"\\log {a + b - c}"), f"log({a + b - c})", (_lg(a + b - c),)),
            _Cand("quotient_as_product", tex(f"\\log {a * b * c}"), f"log({a * b * c})", (_lg(a * b * c),)),
            _Cand("subtracted_inside", tex(f"\\log {a * b - c}"), f"log({a * b - c})", (_lg(a * b - c),)),
        ]
        steps = [
            Step("Use the product law on the first two logarithms", f"log({a * b})"),
            Step("Use the quotient law for the subtraction", f"log({a * b}/{c})"),
            Step("Work out the quotient", typed),
        ]
        task = {"form": "log a + log b - log c", "a": a, "b": b, "c": c}
    else:
        p, q = rng.randint(2, 4), rng.randint(2, 4)
        expr = f"{p}\\log x + {q}\\log y - \\log z"
        question = f"Express {tex(expr)} as a single logarithm."
        answer = tex(f"\\log \\left(\\frac{{x^{p}y^{q}}}{{z}}\\right)")
        typed = f"log(x^{p}*y^{q}/z)"
        # probe at three (x, y, z) triples
        triples = ((1.7, 2.3, 3.1), (2.9, 1.3, 4.4), (3.6, 2.2, 1.9))
        correct_probe = [_lg(x**p * y**q / z) for x, y, z in triples]
        cands = [
            _Cand("quotient_as_product", tex(f"\\log ({'x^' + str(p)}y^{q}z)"), f"log(x^{p}*y^{q}*z)", [_lg(x**p * y**q * z) for x, y, z in triples]),
            _Cand("power_misapplied", tex(f"\\log \\left(\\frac{{{p}x\\cdot {q}y}}{{z}}\\right)"), f"log({p}*x*{q}*y/z)", [_lg(p * x * q * y / z) for x, y, z in triples]),
            _Cand("added_inside_log", tex(f"\\log (x^{p} + y^{q} - z)"), f"log(x^{p} + y^{q} - z)", [_lg(abs(x**p + y**q - z)) for x, y, z in triples]),
        ]
        steps = [
            Step("Use the power law to move the indices inside", f"log(x^{p}) + log(y^{q}) - log(z)"),
            Step("Use the product law on the first two terms", f"log(x^{p}*y^{q}) - log(z)"),
            Step("Use the quotient law", typed),
        ]
        task = {"form": "p log x + q log y - log z", "p": p, "q": q}
    marking = {"answer_type": "expression", "expected": [typed], "typed": typed}
    d = _distractors(notes, answer, typed, correct_probe, cands)
    return "combine_logs", question, answer, d, steps, marking, {"task": "combine_logs", **task}


# ---- levels 4 and 5 ---------------------------------------------------------


def _log_solution(base: int, c: float) -> float:
    return math.log(c) / math.log(base)


def _solve_problem(rng: SeededRandom, level: int):
    notes = LOG_NOTES["solve_exponential"]
    for _ in range(_MAX_ATTEMPTS):
        a = rng.choice(_BASES)
        if level == 4:
            shape = rng.choice(("plain", "shifted", "decimal"))
        else:
            shape = rng.choice(("multiplied", "linear_power"))
        if shape == "plain":
            c = rng.randint(3, 90)
            if c in {a**i for i in range(1, 8)}:
                continue
            x = _log_solution(a, c)
            expr, steps_eq = f"{a}^x = {c}", f"x*log({a}) = log({c})"
            cands = [
                ("ratio_inverted", math.log(a) / math.log(c)),
                ("divided_values_not_logs", c / a),
                ("premature_rounding", round(math.log(c), 2) / round(math.log(a), 2)),
            ]
            final_steps = [
                Step("Take logarithms of both sides and bring down the power", steps_eq),
                Step("Divide by the logarithm of the base", f"x = log({c})/log({a})"),
            ]
            facts = {"form": "a^x = c", "a": a, "c": c}
        elif shape == "decimal":
            c = rng.choice((1.5, 2.5, 3.5, 4.5, 6.5, 7.5, 0.6, 0.8))
            x = _log_solution(a, c)
            expr, steps_eq = f"{a}^x = {c}", f"x*log({a}) = log({c})"
            cands = [
                ("ratio_inverted", math.log(a) / math.log(c) if c != 1 else 0.0),
                ("divided_values_not_logs", c / a),
                ("premature_rounding", round(math.log(c), 2) / round(math.log(a), 2)),
            ]
            final_steps = [
                Step("Take logarithms of both sides and bring down the power", steps_eq),
                Step("Divide by the logarithm of the base", f"x = log({c})/log({a})"),
            ]
            facts = {"form": "a^x = c (decimal)", "a": a, "c": c}
        elif shape == "shifted":
            b = rng.randint(1, 3)
            c = rng.randint(a + 1, 90)
            if c in {a**i for i in range(1, 8)}:
                continue
            x = _log_solution(a, c) - b
            expr, steps_eq = f"{a}^{{x + {b}}} = {c}", f"(x + {b})*log({a}) = log({c})"
            cands = [
                ("power_not_removed", _log_solution(a, c)),
                ("constant_sign_error", _log_solution(a, c) + b),
                ("ratio_inverted", math.log(a) / math.log(c) - b),
            ]
            final_steps = [
                Step("Take logarithms of both sides and bring down the power", steps_eq),
                Step("Divide by the logarithm of the base", f"x + {b} = log({c})/log({a})"),
                Step("Subtract the constant", f"x = log({c})/log({a}) - {b}"),
            ]
            facts = {"form": "a^(x+b) = c", "a": a, "b": b, "c": c}
        elif shape == "multiplied":
            k = rng.randint(2, 9)
            d = rng.randint(3, 40)
            if d in {a**i for i in range(1, 8)}:
                continue
            c = k * d
            x = _log_solution(a, d)
            expr, steps_eq = f"{k}({a})^x = {c}", f"x*log({a}) = log({d})"
            cands = [
                ("bases_multiplied", math.log(c) / math.log(k * a)),
                ("not_divided_first", _log_solution(a, c)),
                ("ratio_inverted", math.log(a) / math.log(d)),
            ]
            final_steps = [
                Step("Divide both sides by the number in front", f"{a}^x = {d}"),
                Step("Take logarithms of both sides and bring down the power", steps_eq),
                Step("Divide by the logarithm of the base", f"x = log({d})/log({a})"),
            ]
            facts = {"form": "k a^x = c", "k": k, "a": a, "c": c}
        else:  # linear_power
            pcoef = rng.randint(2, 4)
            q = rng.choice((-3, -2, -1, 1, 2))
            c = rng.randint(a + 1, 90)
            if c in {a**i for i in range(1, 8)}:
                continue
            x = (_log_solution(a, c) - q) / pcoef
            qtex = f"{pcoef}x - {-q}" if q < 0 else f"{pcoef}x + {q}"
            expr, steps_eq = f"{a}^{{{qtex}}} = {c}", f"({pcoef}*x + {q})*log({a}) = log({c})"
            cands = [
                ("forgot_to_divide_by_coefficient", _log_solution(a, c) - q),
                ("constant_sign_error", (_log_solution(a, c) + q) / pcoef),
                ("ratio_inverted", (math.log(a) / math.log(c) - q) / pcoef),
            ]
            final_steps = [
                Step("Take logarithms of both sides and bring down the power", steps_eq),
                Step("Divide by the logarithm of the base", f"{pcoef}*x + {q} = log({c})/log({a})"),
                Step("Solve for x", f"x = (log({c})/log({a}) - {q})/{pcoef}"),
            ]
            facts = {"form": "a^(px+q) = c", "a": a, "p": pcoef, "q": q, "c": c}
        if not _safe_rounding(x) or abs(x) < 1e-3 or abs(x) > 99:
            continue
        # self-check: the solution satisfies the equation (floating point, relative)
        if shape == "plain" or shape == "decimal":
            lhs, rhs = a**x, c
        elif shape == "shifted":
            lhs, rhs = a ** (x + facts["b"]), c
        elif shape == "multiplied":
            lhs, rhs = facts["k"] * a**x, c
        else:
            lhs, rhs = a ** (facts["p"] * x + facts["q"]), c
        _require(abs(lhs - rhs) <= 1e-9 * abs(rhs), "solution does not satisfy the equation")
        correct = _sig_text(x)
        cand_objs: List[_Cand] = []
        for code, val in cands:
            if not _safe_rounding(val) or val == 0:
                continue
            shown = _sig_text(val)
            cand_objs.append(_Cand(code, tex(f"x = {shown}"), shown, (float(Decimal(shown)),)))
        # a value rounded to too few figures
        two = _sig_text(x, 2)
        cand_objs.append(_Cand("too_few_figures", tex(f"x = {two}"), two, (float(Decimal(two)),)))
        question = (
            f"Solve the equation {tex(expr)} using logarithms. "
            f"Give your answer correct to 3 significant figures."
        )
        answer = tex(f"x = {correct}")
        steps = list(final_steps) + [Step("Round to 3 significant figures", correct)]
        marking = {"answer_type": "number_rounded", "expected": [f"{x:.12f}"], "rounding": "sig_figs", "digits": 3, "typed": correct}
        d = _distractors(notes, answer, correct, (float(Decimal(correct)),), cand_objs)
        return "solve_exponential", question, answer, d, steps, marking, {"task": "solve_exponential", "x": x, **facts}
    raise GeneratorError("could not build an exponential equation")


class LogarithmsGenerator(MathGenerator):
    generator_id = LOG_ID
    version = 1
    levels = (1, 2, 3, 4, 5)
    level_skills = LOG_LEVEL_SKILLS
    error_notes = LOG_NOTES

    def _build(self, rng: SeededRandom, seed: int, level: int) -> GeneratedProblem:
        if level == 1:
            built = _log_level1(rng, self)
        elif level == 2:
            built = _log_level2(rng, self)
        elif level == 3:
            built = _log_level3(rng, self)
        else:
            built = _solve_problem(rng, level)
        skill, question, answer, distractors, steps, marking, machine = built
        return _problem(self, seed, level, skill, question, answer, distractors, steps, marking, machine)


# ==========================================================================
# Sequences (lesson 15825)
# ==========================================================================

SEQ_NOTES: Dict[str, Dict[str, str]] = {
    "next_term": {
        "difference_sign_flipped": "went the wrong way, subtracting the common difference instead of adding it",
        "added_two_terms": "added the last two terms instead of adding the common difference",
        "repeated_last_gap": "added the wrong gap between terms",
    },
    "nth_term_linear": {
        "constant_not_adjusted": "wrote the first term as the constant instead of the first term minus the common difference",
        "difference_added_to_n": "wrote n plus the common difference instead of the difference multiplied by n",
        "constant_dropped": "left out the constant term",
        "gave_next_term": "gave the next term of the sequence instead of an expression for the nth term",
        "difference_sign_flipped": "used the wrong sign for the common difference",
    },
    "number_of_terms": {
        "forgot_to_add_one": "divided the total rise by the common difference and stopped, forgetting to add one",
        "added_one_too_many": "added one too many terms to the count",
        "used_n_not_n_minus_1": "used n instead of n minus 1 in the nth term formula",
    },
    "ap_a_and_d": {
        "position_off_by_one": "used the term number as the multiple of d instead of one less than the term number",
        "d_sign_flipped": "found the right size of d but gave it the wrong sign",
        "a_and_d_swapped": "gave the common difference as the first term and the first term as the common difference",
    },
    "ap_sum": {
        "half_forgotten": "forgot to halve when using the sum formula",
        "one_term_missing": "counted one term too few in the number of terms",
        "one_term_extra": "counted one term too many in the number of terms",
    },
    "ap_to_gp": {
        "ratio_inverted": "wrote the ratio the wrong way round (earlier term over later term)",
        "ratio_sign_flipped": "gave the right size of ratio with the wrong sign",
        "wrong_term_pair": "found the ratio of the wrong pair of terms",
    },
}

SEQ_LEVEL_SKILLS: Dict[int, Tuple[str, ...]] = {
    1: ("next_term",),
    2: ("nth_term_linear",),
    3: ("number_of_terms",),
    4: ("ap_a_and_d", "ap_sum"),
    5: ("ap_to_gp",),
}

_CONTEXTS = (
    ("Ndapewa", "She saves N${a} in the first week, N${b} in the second week and N${c} in the third week, and so on.",
     "the amount, in N$, that she saves in week {n}"),
    ("Tuyeni", "A taxi in Windhoek charges N${a} for a journey of 1 km, N${b} for 2 km and N${c} for 3 km, and so on.",
     "the charge, in N$, for a journey of {n} km"),
)


def _seq_level1(rng: SeededRandom, gen: MathGenerator):
    notes = SEQ_NOTES["next_term"]
    a = rng.randint(-10, 30)
    d = _nonzero(rng, -9, 9)
    terms = [a + i * d for i in range(4)]
    nxt = a + 4 * d
    shown = ", ".join(str(t) for t in terms)
    question = ''.join(['Write down the next term in the sequence ', format(tex(shown + ', \\dots'), '')])
    answer = tex(str(nxt))
    typed = str(nxt)
    last, prev = terms[-1], terms[-2]
    cands = [
        _Cand("difference_sign_flipped", tex(str(last - d)), str(last - d), (float(last - d),)),
        _Cand("added_two_terms", tex(str(last + prev)), str(last + prev), (float(last + prev),)),
        _Cand("repeated_last_gap", tex(str(last + d + 1)), str(last + d + 1), (float(last + d + 1),)),
    ]
    steps = [Step("Find the common difference", str(d)), Step("Add it to the last term", typed)]
    marking = {"answer_type": "number_exact", "expected": [typed], "typed": typed}
    dd = _distractors(notes, answer, typed, (float(nxt),), cands)
    return "next_term", question, answer, dd, steps, marking, {"task": "next_term", "a": a, "d": d}


def _seq_level2(rng: SeededRandom, gen: MathGenerator):
    notes = SEQ_NOTES["nth_term_linear"]
    a = rng.randint(-8, 40)
    d = _nonzero(rng, -9, 9)
    c = a - d
    terms = [a + i * d for i in range(4)]
    contextual = rng.chance(1, 4)
    if contextual:
        a_i = rng.randint(30, 80)
        d_i = rng.choice((5, 10, 15, 20, 25))
        a, d = a_i, d_i
        c = a - d
        terms = [a + i * d for i in range(3)]
        name, template, quantity = rng.choice(_CONTEXTS)
        body = template.format(a=terms[0], b=terms[1], c=terms[2])
        question = (
            f"{name} lives in Namibia. {body} The amounts form a linear sequence. "
            f"Find an expression, in terms of {tex('n')}, for {quantity.format(n=tex('n'))}."
        )
    else:
        shown = ", ".join(str(t) for t in terms)
        question = ''.join(['Find an expression, in terms of ', format(tex('n'), ''), ', for the ', format(tex('n'), ''), 'th term of the sequence ', format(tex(shown + ', \\dots'), '')])
    typed = _lin(d, c, "n")
    answer = tex(typed)
    probe = lambda fn: [fn(n) for n in (1.7, 4.0, 9.0)]
    correct_probe = probe(lambda n: d * n + c)
    nxt = a + len(terms) * d
    cands = [
        _Cand("constant_not_adjusted", tex(_lin(d, a, "n")), _lin(d, a, "n"), probe(lambda n: d * n + a)),
        _Cand("difference_added_to_n", tex(_lin(1, d, "n")), _lin(1, d, "n"), probe(lambda n: n + d)),
        _Cand("constant_dropped", tex(_lin(d, 0, "n")), _lin(d, 0, "n"), probe(lambda n: d * n)),
        _Cand("gave_next_term", tex(str(nxt)), str(nxt), probe(lambda n: nxt)),
        _Cand("difference_sign_flipped", tex(_lin(-d, c, "n")), _lin(-d, c, "n"), probe(lambda n: -d * n + c)),
    ]
    steps = [
        Step("Find the common difference", str(d)),
        Step("Subtract the common difference from the first term to find the constant", str(c)),
        Step("Write the nth term as dn + c", typed),
    ]
    marking = {"answer_type": "expression", "expected": [typed], "typed": typed}
    dd = _distractors(notes, answer, typed, correct_probe, cands)
    return "nth_term_linear", question, answer, dd, steps, marking, {"task": "nth_term", "a": a, "d": d, "context": contextual}


def _seq_level3(rng: SeededRandom, gen: MathGenerator):
    notes = SEQ_NOTES["number_of_terms"]
    a = rng.randint(2, 30)
    d = rng.randint(2, 9)
    n = rng.randint(12, 60)
    last = a + (n - 1) * d
    series = f"{a} + {a + d} + {a + 2 * d} + \\dots + {last}"
    question = f"Find the number of terms in the arithmetic progression {tex(series)}"
    answer = tex(str(n))
    typed = str(n)
    cands = [
        _Cand("forgot_to_add_one", tex(str(n - 1)), str(n - 1), (float(n - 1),)),
        _Cand("added_one_too_many", tex(str(n + 1)), str(n + 1), (float(n + 1),)),
        _Cand("used_n_not_n_minus_1", tex(str(n - 2)), str(n - 2), (float(n - 2),)),
    ]
    _require(a + (n - 1) * d == last, "arithmetic progression does not end at the last term")
    steps = [
        Step("Use the nth term formula for the last term", f"{last} = {a} + (n - 1)*{d}"),
        Step("Find n minus 1", str((last - a) // d)),
        Step("Find n", typed),
    ]
    marking = {"answer_type": "number_exact", "expected": [typed], "typed": typed}
    dd = _distractors(notes, answer, typed, (float(n),), cands)
    return "number_of_terms", question, answer, dd, steps, marking, {"task": "number_of_terms", "a": a, "d": d, "n": n}


def _seq_level4(rng: SeededRandom, gen: MathGenerator):
    if rng.chance(1, 2):
        return _seq_a_and_d(rng)
    return _seq_sum(rng)


def _seq_a_and_d(rng: SeededRandom):
    notes = SEQ_NOTES["ap_a_and_d"]
    for _ in range(_MAX_ATTEMPTS):
        a = rng.randint(-10, 30)
        d = _nonzero(rng, -6, 9)
        j = rng.randint(2, 8)
        k = rng.randint(j + 3, 20)
        tj, tk = a + (j - 1) * d, a + (k - 1) * d
        if a == d:
            continue
        break
    question = (
        f"The {_ordinal(j)} term of an arithmetic progression is {tex(str(tj))} and the "
        f"{_ordinal(k)} term is {tex(str(tk))}. Find the first term {tex('a')} and the common difference {tex('d')}."
    )
    answer = tex(f"a = {a},\\ d = {d}")
    typed = f"a = {a}, d = {d}"
    a_off = a - d  # using T_j = a + j d instead of a + (j - 1) d
    cands = [
        _Cand("position_off_by_one", tex(f"a = {a_off},\\ d = {d}"), f"a = {a_off}, d = {d}", (float(a_off), float(d))),
        _Cand("d_sign_flipped", tex(f"a = {a},\\ d = {-d}"), f"a = {a}, d = {-d}", (float(a), float(-d))),
        _Cand("a_and_d_swapped", tex(f"a = {d},\\ d = {a}"), f"a = {d}, d = {a}", (float(d), float(a))),
    ]
    steps = [
        Step(f"Write the two terms using a + (n - 1)d", f"a + {j - 1}d = {tj}"),
        Step("Subtract to find d", f"d = {d}"),
        Step("Substitute to find a", f"a = {a}"),
    ]
    marking = {"answer_type": "sequence", "expected": [typed], "typed": typed}
    dd = _distractors(notes, answer, typed, (float(a), float(d)), cands)
    return "ap_a_and_d", question, answer, dd, steps, marking, {"task": "ap_a_and_d", "a": a, "d": d, "j": j, "k": k}


def _seq_sum(rng: SeededRandom):
    notes = SEQ_NOTES["ap_sum"]
    a = rng.randint(2, 30)
    d = rng.randint(2, 9)
    n = rng.randint(12, 50)
    last = a + (n - 1) * d
    total = n * (a + last) // 2
    _require(n * (a + last) % 2 == 0, "sum is not a whole number")
    series = f"{a} + {a + d} + {a + 2 * d} + \\dots + {last}"
    question = f"Find the sum of the terms in the arithmetic progression {tex(series)}"
    answer = tex(str(total))
    typed = str(total)
    cands = [
        _Cand("half_forgotten", tex(str(n * (a + last))), str(n * (a + last)), (float(n * (a + last)),)),
        _Cand("one_term_missing", tex(_frac_latex(Fraction((n - 1) * (a + last), 2))), _frac_text(Fraction((n - 1) * (a + last), 2)), ((n - 1) * (a + last) / 2,)),
        _Cand("one_term_extra", tex(_frac_latex(Fraction((n + 1) * (a + last), 2))), _frac_text(Fraction((n + 1) * (a + last), 2)), ((n + 1) * (a + last) / 2,)),
    ]
    steps = [
        Step("Find the number of terms", str(n)),
        Step("Use the sum formula n/2 times (first + last)", f"{n}/2*({a} + {last})"),
        Step("Work out the sum", typed),
    ]
    marking = {"answer_type": "number_exact", "expected": [typed], "typed": typed}
    dd = _distractors(notes, answer, typed, (float(total),), cands)
    return "ap_sum", question, answer, dd, steps, marking, {"task": "ap_sum", "a": a, "d": d, "n": n}


def _frac_latex(f: Fraction) -> str:
    return number_latex(f)


def _gp_triples() -> List[Tuple[int, int, int, Fraction, Fraction]]:
    """Positions (j, k, l) whose AP terms form a GP, with u = a/d and the ratio r."""
    out = []
    for j in range(1, 10):
        for k in range(j + 1, 14):
            for l in range(k + 1, 18):
                denom = 2 * k - j - l
                if denom == 0:
                    continue
                u = Fraction((j - 1) * (l - 1) - (k - 1) ** 2, denom)
                t_j, t_k, t_l = u + j - 1, u + k - 1, u + l - 1
                if 0 in (t_j, t_k, t_l) or u == 0:
                    continue
                r = t_k / t_j
                if r == 1 or r == -1 or abs(r.numerator) > 20 or abs(r.denominator) > 20:
                    continue
                if t_l / t_k != r:
                    continue
                out.append((j, k, l, u, r))
    return out


_GP_TRIPLES = _gp_triples()


def _seq_level5(rng: SeededRandom, gen: MathGenerator):
    notes = SEQ_NOTES["ap_to_gp"]
    j, k, l, u, r = rng.choice(_GP_TRIPLES)
    question = (
        ''.join(['An arithmetic progression has first term ', format(tex('a'), ''), ' and common difference ', format(tex('d'), ''), ', where ', format(tex('d \\neq 0'), ''), '. Its ', format(_ordinal(j), ''), ', ', format(_ordinal(k), ''), ' and ', format(_ordinal(l), ''), ' terms form a geometric progression. Find the common ratio of the geometric progression.'])
    )
    answer = tex(f"r = {number_latex(r)}")
    typed = _frac_text(r)
    inverse = 1 / r
    other = Fraction(l - k, k - j)
    cands = [
        _Cand("ratio_inverted", tex(f"r = {number_latex(inverse)}"), _frac_text(inverse), (float(inverse),)),
        _Cand("ratio_sign_flipped", tex(f"r = {number_latex(-r)}"), _frac_text(-r), (float(-r),)),
        _Cand("wrong_term_pair", tex(f"r = {number_latex(other)}"), _frac_text(other), (float(other),)),
    ]
    u_text = _frac_text(u)
    t_j, t_k, t_l = u + j - 1, u + k - 1, u + l - 1
    _require(t_k * t_k == t_j * t_l, "terms do not form a geometric progression")
    steps = [
        Step("Write the middle term using a and d", f"a + {k - 1}*d"),
        Step("Use (middle term) squared = (first term)(last term)", f"(a + {k - 1}*d)^2 = (a + {j - 1}*d)(a + {l - 1}*d)"),
        Step("Solve for a in terms of d", f"a = {u_text}*d"),
        Step("Divide the second term by the first term", typed),
    ]
    marking = {"answer_type": "number_exact", "expected": [typed], "typed": typed}
    dd = _distractors(notes, answer, typed, (float(r),), cands)
    return "ap_to_gp", question, answer, dd, steps, marking, {"task": "ap_to_gp", "j": j, "k": k, "l": l, "a_over_d": [u.numerator, u.denominator], "ratio": [r.numerator, r.denominator]}


class SequencesGenerator(MathGenerator):
    generator_id = SEQ_ID
    version = 1
    levels = (1, 2, 3, 4, 5)
    level_skills = SEQ_LEVEL_SKILLS
    error_notes = SEQ_NOTES

    def _build(self, rng: SeededRandom, seed: int, level: int) -> GeneratedProblem:
        builder = {1: _seq_level1, 2: _seq_level2, 3: _seq_level3, 4: _seq_level4, 5: _seq_level5}[level]
        skill, question, answer, distractors, steps, marking, machine = builder(rng, self)
        return _problem(self, seed, level, skill, question, answer, distractors, steps, marking, machine)


# ==========================================================================
# Functions (lesson 15827)
# ==========================================================================

FUN_NOTES: Dict[str, Dict[str, str]] = {
    "evaluate_function": {
        "negative_square_lost": "treated a negative number squared as a negative result",
        "sign_of_input_lost": "dropped the negative sign of the input before substituting",
        "wrong_sign_after_square": "subtracted the square with the wrong sign",
        "cube_instead_of_root": "cubed the number instead of taking the cube root",
        "divided_by_three": "divided by 3 instead of taking the cube root",
    },
    "inverse_linear": {
        "sign_of_constant": "moved the constant across with the wrong sign",
        "constant_not_divided": "divided only the x term by the coefficient and left the constant undivided",
        "multiplied_not_divided": "multiplied by the coefficient instead of dividing",
        "reciprocal_taken": "wrote the reciprocal of the function instead of its inverse",
    },
    "composite_value": {
        "wrong_order": "applied the two functions in the wrong order",
        "negative_square_lost": "treated a negative number squared as a negative result",
        "inner_function_skipped": "put the number straight into the outer function",
    },
    "solve_function_equation": {
        "wrong_sign_collecting": "added a term that should have been subtracted when collecting x terms",
        "wrong_sign_constant": "moved the constant across with the wrong sign",
        "too_few_figures": "gave the answer to fewer than 3 significant figures",
    },
    "function_of_expression": {
        "multiplied_function": "multiplied the whole function by the number instead of replacing x",
        "multiplier_on_constant": "replaced x by the expression in the x term but also multiplied the constant",
        "added_instead_of_replaced": "added the number to the function instead of replacing x",
    },
    "composite_linear": {
        "wrong_order": "applied the two functions in the wrong order",
        "not_bracketed": "did not put brackets round the inner function, so the outer coefficient multiplied only its first term",
        "expansion_sign_error": "made a sign error when multiplying out the bracket",
    },
    "composite_quadratic": {
        "squared_only_constant": "squared only the constant term of the inner function",
        "middle_term_missing": "expanded the square of a bracket without the middle term",
        "wrong_order": "applied the two functions in the wrong order",
        "not_bracketed": "did not put brackets round the inner function before squaring",
    },
}

FUN_LEVEL_SKILLS: Dict[int, Tuple[str, ...]] = {
    1: ("evaluate_function",),
    2: ("inverse_linear",),
    3: ("composite_value", "solve_function_equation", "function_of_expression"),
    4: ("composite_linear",),
    5: ("composite_quadratic",),
}


def _fn(name: str, rhs: str) -> str:
    return f"{name}(x) = {rhs}"


def _fun_level1(rng: SeededRandom, gen: MathGenerator):
    notes = FUN_NOTES["evaluate_function"]
    shape = rng.choice(("linear", "square", "const_minus_square", "cube_equation"))
    if shape == "cube_equation":
        r = rng.randint(3, 14)
        n = r**3
        question = f"Solve {tex(f'x^3 = {n}')}."
        answer = tex(f"x = {r}")
        typed = str(r)
        cands = [
            _Cand("cube_instead_of_root", tex(f"x = {n ** 3}"), str(n**3), (float(n**3),)),
            _Cand("divided_by_three", tex(f"x = \\frac{{{n}}}{{3}}"), f"{n}/3", (n / 3,)),
        ]
        steps = [Step("Take the cube root of both sides", f"x = {r}")]
        marking = {"answer_type": "number_exact", "expected": [typed], "typed": typed}
        dd = _distractors(notes, answer, typed, (float(r),), cands)
        return "evaluate_function", question, answer, dd, steps, marking, {"task": "cube_equation", "n": n}
    k = rng.randint(1, 6)
    x0 = -k if rng.chance(3, 4) else k
    if shape == "linear":
        a = _nonzero(rng, -7, 7)
        b = rng.randint(-9, 9)
        style = rng.randint(0, 1)
        defn = _fn("f", _lin_tex_styled(a, b, style))
        value = a * x0 + b
        cands = [
            _Cand("sign_of_input_lost", tex(str(a * abs(x0) + b)), str(a * abs(x0) + b), (float(a * abs(x0) + b),)),
            _Cand("sign_of_input_lost", tex(str(-(a * x0) + b)), str(-(a * x0) + b), (float(-(a * x0) + b),)),
        ]
        steps = [Step("Substitute the value of x", f"{a}*({x0}) + {b}" if b >= 0 else f"{a}*({x0}) - {-b}"), Step("Work out the value", str(value))]
        facts = {"form": "ax + b", "a": a, "b": b}
    elif shape == "square":
        defn = _fn("f", "x^2")
        value = x0 * x0
        cands = [_Cand("negative_square_lost", tex(str(-value)), str(-value), (float(-value),))]
        steps = [Step("Substitute and square the bracket", f"({x0})^2"), Step("Work out the value", str(value))]
        facts = {"form": "x^2"}
    else:
        c = rng.randint(-5, 12)
        defn = _fn("f", f"{c} - x^2" if c != 0 else "-x^2")
        value = c - x0 * x0
        cands = [
            _Cand("wrong_sign_after_square", tex(str(c + x0 * x0)), str(c + x0 * x0), (float(c + x0 * x0),)),
            _Cand("negative_square_lost", tex(str(-(c) - x0 * x0)), str(-(c) - x0 * x0), (float(-(c) - x0 * x0),)),
        ]
        steps = [Step("Substitute and square the bracket first", f"{c} - ({x0})^2"), Step("Work out the value", str(value))]
        facts = {"form": "c - x^2", "c": c}
    question = f"Given that {tex(defn)}, find {tex(f'f({x0})')}."
    answer = tex(str(value))
    typed = str(value)
    marking = {"answer_type": "number_exact", "expected": [typed], "typed": typed}
    dd = _distractors(notes, answer, typed, (float(value),), cands)
    return "evaluate_function", question, answer, dd, steps, marking, {"task": "evaluate_function", "x": x0, **facts}


def _linear_pair(rng: SeededRandom, a_lo=-7, a_hi=7, b_lo=-9, b_hi=9) -> Tuple[int, int]:
    return _nonzero(rng, a_lo, a_hi), rng.randint(b_lo, b_hi)


def _fun_level2(rng: SeededRandom, gen: MathGenerator):
    notes = FUN_NOTES["inverse_linear"]
    name = rng.choice(("f", "g", "h"))
    a = _nonzero(rng, -7, 7)
    while abs(a) == 1:
        a = _nonzero(rng, -7, 7)
    b = _nonzero(rng, -9, 9)
    style = rng.randint(0, 1)
    defn = _fn(name, _lin_tex_styled(a, b, style))
    question = f"Given that {tex(defn)}, find {tex(f'{name}^{{-1}}(x)')}."
    # (x - b)/a, written with a positive denominator
    if a > 0:
        num_tex, den = (f"x - {b}" if b > 0 else f"x + {-b}"), a
        typed = f"(x - {b})/{a}" if b > 0 else f"(x + {-b})/{a}"
    else:
        num_tex, den = (f"{b} - x" if b > 0 else f"-{-b} - x"), -a
        typed = f"({b} - x)/{den}"
    answer = tex(f"{name}^{{-1}}(x) = \\frac{{{num_tex}}}{{{den}}}")
    probe = lambda fn: [fn(x) for x in _PROBES_X]
    correct_probe = probe(lambda x: (x - b) / a)

    def disp(num: str, den_: str) -> str:
        return tex(f"{name}^{{-1}}(x) = \\frac{{{num}}}{{{den_}}}")

    cands = [
        _Cand("sign_of_constant", disp(f"x + {b}" if b > 0 else f"x - {-b}", str(a)) if a > 0 else tex(f"{name}^{{-1}}(x) = \\frac{{x + {b}}}{{{a}}}" if b > 0 else f"{name}^{{-1}}(x) = \\frac{{x - {-b}}}{{{a}}}"),
              f"(x + {b})/{a}" if b > 0 else f"(x - {-b})/{a}", probe(lambda x: (x + b) / a)),
        _Cand("constant_not_divided", tex(f"{name}^{{-1}}(x) = \\frac{{x}}{{{a}}} - {b}" if b > 0 else f"{name}^{{-1}}(x) = \\frac{{x}}{{{a}}} + {-b}"),
              f"x/{a} - {b}" if b > 0 else f"x/{a} + {-b}", probe(lambda x: x / a - b)),
        _Cand("multiplied_not_divided", tex(f"{name}^{{-1}}(x) = {a}(x - {b})" if b > 0 else f"{name}^{{-1}}(x) = {a}(x + {-b})"),
              f"{a}*(x - {b})" if b > 0 else f"{a}*(x + {-b})", probe(lambda x: a * (x - b))),
        _Cand("reciprocal_taken", tex(f"{name}^{{-1}}(x) = \\frac{{1}}{{{_lin(a, b)}}}"), f"1/({_lin(a, b)})", probe(lambda x: 1 / (a * x + b))),
    ]
    steps = [
        Step("Write y = f(x) and swap x and y", f"x = {a}*y + {b}" if b > 0 else f"x = {a}*y - {-b}"),
        Step("Rearrange to make y the subject", typed),
    ]
    marking = {"answer_type": "expression", "expected": [typed], "typed": typed}
    dd = _distractors(notes, answer, typed, correct_probe, cands)
    return "inverse_linear", question, answer, dd, steps, marking, {"task": "inverse_linear", "a": a, "b": b, "name": name}


def _fun_level3(rng: SeededRandom, gen: MathGenerator):
    shape = rng.choice(("composite_value", "solve_equation", "function_of_expression"))
    if shape == "composite_value":
        return _composite_value(rng)
    if shape == "solve_equation":
        return _solve_function_equation(rng)
    return _function_of_expression(rng)


def _composite_value(rng: SeededRandom):
    notes = FUN_NOTES["composite_value"]
    a, b = _linear_pair(rng, -5, 5, -6, 6)
    outer_shape = rng.choice(("square", "linear"))
    x0 = rng.randint(1, 4)
    inner = a * x0 + b
    if outer_shape == "square":
        c = rng.choice((0, 0, -3, 2, 5))
        value = inner * inner + c
        gdef = "x^2" if c == 0 else (f"x^2 + {c}" if c > 0 else f"x^2 - {-c}")
        g_of = lambda t: t * t + c
        wrong_inner_neg = -(inner * inner) + c if inner < 0 else None
    else:
        e, h = _linear_pair(rng, -5, 5, -6, 6)
        value = e * inner + h
        gdef = _lin(e, h)
        g_of = lambda t: e * t + h
        wrong_inner_neg = None
    question = (
        f"Given that {tex(_fn('f', _lin_tex_styled(a, b, rng.randint(0, 1))))} and {tex(_fn('g', gdef))}, "
        f"find {tex(f'gf({x0})')}."
    )
    answer = tex(str(value))
    typed = str(value)
    cands = [
        _Cand("wrong_order", tex(str(a * g_of(x0) + b)), str(a * g_of(x0) + b), (float(a * g_of(x0) + b),)),
        _Cand("inner_function_skipped", tex(str(g_of(x0))), str(g_of(x0)), (float(g_of(x0)),)),
    ]
    if wrong_inner_neg is not None:
        cands.append(_Cand("negative_square_lost", tex(str(wrong_inner_neg)), str(wrong_inner_neg), (float(wrong_inner_neg),)))
    steps = [
        Step(f"Work out f({x0}) first", str(inner)),
        Step("Put the result into g", str(value)),
    ]
    marking = {"answer_type": "number_exact", "expected": [typed], "typed": typed}
    dd = _distractors(notes, answer, typed, (float(value),), cands)
    return "composite_value", question, answer, dd, steps, marking, {"task": "composite_value", "x": x0}


def _solve_function_equation(rng: SeededRandom):
    notes = FUN_NOTES["solve_function_equation"]
    for _ in range(_MAX_ATTEMPTS):
        a, b = _linear_pair(rng, -6, 6, -9, 9)
        p, q = _linear_pair(rng, -3, 3, -9, 9)
        if a == p:
            continue
        x = Fraction(q - b, a - p)
        if x == 0 or (x.denominator == 1 and rng.chance(2, 3)):
            continue  # prefer fractional answers, as the papers do
        if not _short_exact(x) and not _safe_rounding(float(x)):
            continue
        break
    style = rng.randint(0, 1)
    question = (
        f"Given that {tex(_fn('f', _lin_tex_styled(a, b, style)))}, solve {tex(f'f(x) = {_lin_tex_styled(p, q, style)}')}. "
        f"Give your answer correct to 3 significant figures."
    )
    correct_val = float(x)
    shown = _sig_text(correct_val)
    answer = tex(f"x = {shown}")
    typed = shown
    cand_defs = [
        ("wrong_sign_collecting", Fraction(q - b, a + p) if a + p else None),
        ("wrong_sign_constant", Fraction(q + b, a - p)),
    ]
    cands = []
    for code, val in cand_defs:
        if val is None or val == 0:
            continue
        v = float(val)
        s = _sig_text(v)
        if _safe_rounding(v) or _short_exact(val):
            cands.append(_Cand(code, tex(f"x = {s}"), s, (float(_sig(v)),)))
    if not _short_exact(x):
        two = _sig_text(correct_val, 2)
        cands.append(_Cand("too_few_figures", tex(f"x = {two}"), two, (float(Decimal(two)),)))
    steps = [
        Step("Set f(x) equal to the right-hand side", f"{_lin(a, b)} = {_lin(p, q)}"),
        Step("Collect the x terms on one side", f"{_lin(a - p, 0)} = {q - b}"),
        Step("Divide to find x", f"x = {_frac_text(x)}"),
    ]
    marking = {"answer_type": "number_rounded", "expected": [_frac_text(x)], "rounding": "sig_figs", "digits": 3, "typed": typed}
    probe = (float(_sig(correct_val)),)
    dd = _distractors(notes, answer, typed, probe, cands)
    return "solve_function_equation", question, answer, dd, steps, marking, {"task": "solve_function_equation", "a": a, "b": b, "p": p, "q": q}


def _function_of_expression(rng: SeededRandom):
    notes = FUN_NOTES["function_of_expression"]
    a, b = _linear_pair(rng, -5, 5, -9, 9)
    while b == 0:
        a, b = _linear_pair(rng, -5, 5, -9, 9)
    k = rng.randint(2, 4)
    question = f"Given that {tex(_fn('g', _lin(a, b)))}, find {tex(f'g({k}x)')}."
    typed = _lin(a * k, b)
    answer = tex(typed)
    probe = lambda fn: [fn(x) for x in _PROBES_X]
    correct_probe = probe(lambda x: a * k * x + b)
    cands = [
        _Cand("multiplied_function", tex(f"{k}({_lin(a, b)})"), f"{k}*({_lin(a, b)})", probe(lambda x: k * (a * x + b))),
        _Cand("multiplier_on_constant", tex(_lin(a * k, b * k)), _lin(a * k, b * k), probe(lambda x: a * k * x + b * k)),
        _Cand("added_instead_of_replaced", tex(_lin(a, b + k)), _lin(a, b + k), probe(lambda x: a * x + b + k)),
    ]
    steps = [
        Step("Replace x by the new expression", f"{a}*({k}*x) + {b}" if b > 0 else f"{a}*({k}*x) - {-b}"),
        Step("Simplify", typed),
    ]
    marking = {"answer_type": "expression", "expected": [typed], "typed": typed}
    dd = _distractors(notes, answer, typed, correct_probe, cands)
    return "function_of_expression", question, answer, dd, steps, marking, {"task": "function_of_expression", "a": a, "b": b, "k": k}


def _fun_level4(rng: SeededRandom, gen: MathGenerator):
    notes = FUN_NOTES["composite_linear"]
    for _ in range(_MAX_ATTEMPTS):
        a, b = _linear_pair(rng, -7, 7, -9, 9)
        c, d = _linear_pair(rng, -7, 7, -9, 9)
        if abs(a) > 1 and abs(c) > 1 and b != 0 and d != 0:
            break
    order = rng.choice(("fg", "gf"))
    f_tex = _fn("f", _lin_tex_styled(a, b, rng.randint(0, 1)))
    g_tex = _fn("g", _lin_tex_styled(c, d, rng.randint(0, 1)))
    if order == "fg":
        outer, inner = (a, b), (c, d)
    else:
        outer, inner = (c, d), (a, b)
    (oa, ob), (ia, ib) = outer, inner
    slope, const = oa * ia, oa * ib + ob
    question = f"Given that {tex(f_tex)} and {tex(g_tex)}, find {tex(f'{order}(x)')} in its simplest form."
    typed = _lin(slope, const)
    answer = tex(typed)
    probe = lambda fn: [fn(x) for x in _PROBES_X]
    correct_probe = probe(lambda x: slope * x + const)
    wrong_slope, wrong_const = ia * oa, ia * ob + ib  # applied in the other order
    cands = [
        _Cand("wrong_order", tex(_lin(wrong_slope, wrong_const)), _lin(wrong_slope, wrong_const), probe(lambda x: wrong_slope * x + wrong_const)),
        _Cand("not_bracketed", tex(_lin(slope, ib + ob)), _lin(slope, ib + ob), probe(lambda x: slope * x + ib + ob)),
        _Cand("expansion_sign_error", tex(_lin(slope, -oa * ib + ob)), _lin(slope, -oa * ib + ob), probe(lambda x: slope * x - oa * ib + ob)),
    ]
    steps = [
        Step("Replace x in the outer function by the inner function", f"{oa}*({_lin(ia, ib)}) + {ob}" if ob >= 0 else f"{oa}*({_lin(ia, ib)}) - {-ob}"),
        Step("Expand the bracket", f"{_lin(slope, oa * ib)} + {ob}" if ob >= 0 else f"{_lin(slope, oa * ib)} - {-ob}"),
        Step("Collect like terms", typed),
    ]
    marking = {"answer_type": "expression", "expected": [typed], "typed": typed, "form": "expanded"}
    dd = _distractors(notes, answer, typed, correct_probe, cands)
    return "composite_linear", question, answer, dd, steps, marking, {"task": "composite_linear", "order": order, "f": [a, b], "g": [c, d]}


def _fun_level5(rng: SeededRandom, gen: MathGenerator):
    notes = FUN_NOTES["composite_quadratic"]
    shape = rng.choice(("c_minus_square", "square"))
    u = _nonzero(rng, -5, 5)
    while abs(u) == 1:
        u = _nonzero(rng, -5, 5)
    v = _nonzero(rng, -7, 7)
    probe = lambda fn: [fn(x) for x in _PROBES_X]
    inner_tex = _lin(u, v)
    if shape == "c_minus_square":
        s = rng.randint(-4, 12)
        outer_def = f"{s} - x^2" if s != 0 else "-x^2"
        f_tex, g_tex = _fn("f", outer_def), _fn("g", inner_tex)
        typed = polynomial_latex([-u * u, -2 * u * v, s - v * v])
        h = lambda x: s - (u * x + v) ** 2
        const = s - v * v
        cands = [
            _Cand("squared_only_constant", tex(polynomial_latex([-u, const])), polynomial_latex([-u, const]), probe(lambda x: -u * x + const)),
            _Cand("middle_term_missing", tex(polynomial_latex([-u * u, 0, const])), polynomial_latex([-u * u, 0, const]), probe(lambda x: -u * u * x * x + const)),
            _Cand("wrong_order", tex(f"{u}({s} - x^2){_signed(v)}"), f"{u}*({s} - x^2){_signed(v)}", probe(lambda x: u * (s - x * x) + v)),
            _Cand("not_bracketed", tex(polynomial_latex([-u * u, 0, s])), polynomial_latex([-u * u, 0, s]), probe(lambda x: s - u * u * x * x)),
        ]
        steps = [
            Step("Replace x in the outer function by the inner function, using brackets", f"{s} - ({inner_tex})^2"),
            Step("Expand the squared bracket", f"{s} - ({polynomial_latex([u * u, 2 * u * v, v * v])})"),
            Step("Simplify", typed),
        ]
        order = "fg"
    else:
        k = rng.choice((1, 1, 2, 3))
        outer_def = "x^2" if k == 1 else f"{k}x^2"
        f_tex, g_tex = _fn("f", inner_tex), _fn("g", outer_def)
        typed = polynomial_latex([k * u * u, 2 * k * u * v, k * v * v])
        h = lambda x: k * (u * x + v) ** 2
        cands = [
            _Cand("squared_only_constant", tex(polynomial_latex([k * u, k * v * v])), polynomial_latex([k * u, k * v * v]), probe(lambda x: k * u * x + k * v * v)),
            _Cand("middle_term_missing", tex(polynomial_latex([k * u * u, 0, k * v * v])), polynomial_latex([k * u * u, 0, k * v * v]), probe(lambda x: k * u * u * x * x + k * v * v)),
            _Cand("wrong_order", tex(polynomial_latex([k * u, 0, v])), polynomial_latex([k * u, 0, v]), probe(lambda x: k * u * x * x + v)),
            _Cand("not_bracketed", tex(polynomial_latex([k * u * u, 0, v])), polynomial_latex([k * u * u, 0, v]), probe(lambda x: k * u * u * x * x + v)),
        ]
        steps = [
            Step("Replace x in the outer function by the inner function, using brackets", f"{k}*({inner_tex})^2"),
            Step("Expand the squared bracket", f"{k}*({polynomial_latex([u * u, 2 * u * v, v * v])})"),
            Step("Simplify", typed),
        ]
        order = "gf"
    question = f"Given that {tex(f_tex)} and {tex(g_tex)}, find {tex(f'{order}(x)')} in its simplest form."
    answer = tex(typed)
    correct_probe = probe(h)
    marking = {"answer_type": "expression", "expected": [typed], "typed": typed, "form": "expanded"}
    dd = _distractors(notes, answer, typed, correct_probe, cands)
    return "composite_quadratic", question, answer, dd, steps, marking, {"task": "composite_quadratic", "shape": shape, "u": u, "v": v}


class FunctionsGenerator(MathGenerator):
    generator_id = FUN_ID
    version = 1
    levels = (1, 2, 3, 4, 5)
    level_skills = FUN_LEVEL_SKILLS
    error_notes = FUN_NOTES

    def _build(self, rng: SeededRandom, seed: int, level: int) -> GeneratedProblem:
        builder = {1: _fun_level1, 2: _fun_level2, 3: _fun_level3, 4: _fun_level4, 5: _fun_level5}[level]
        skill, question, answer, distractors, steps, marking, machine = builder(rng, self)
        return _problem(self, seed, level, skill, question, answer, distractors, steps, marking, machine)


GENERATORS = [LogarithmsGenerator(), SequencesGenerator(), FunctionsGenerator()]
