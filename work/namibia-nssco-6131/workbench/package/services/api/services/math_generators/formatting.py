"""LaTeX text helpers for generated algebra problems.

Output is plain LaTeX meant to sit inside ``$...$``. Callers add the dollar
signs. Coefficients may be ints or Fractions; a Fraction with denominator 1 is
written as an integer.
"""

from __future__ import annotations

import re
from fractions import Fraction
from typing import Sequence, Tuple, Union

Number = Union[int, Fraction]


def _as_fraction(value: Number) -> Fraction:
    return value if isinstance(value, Fraction) else Fraction(value)


def number_latex(value: Number) -> str:
    """``3``, ``-3``, ``\\frac{1}{2}``, ``-\\frac{1}{2}``."""
    frac = _as_fraction(value)
    sign = "-" if frac < 0 else ""
    frac = abs(frac)
    if frac.denominator == 1:
        return f"{sign}{frac.numerator}"
    return f"{sign}\\frac{{{frac.numerator}}}{{{frac.denominator}}}"


def signed_constant_latex(value: Number) -> str:
    """`` + 5`` or `` - 5`` (with spaces); empty string for zero."""
    frac = _as_fraction(value)
    if frac == 0:
        return ""
    sign = "-" if frac < 0 else "+"
    return f" {sign} {number_latex(abs(frac))}"


def _term(coef: int, suffix: str, first: bool) -> str:
    magnitude = abs(coef)
    body = suffix if (magnitude == 1 and suffix) else f"{magnitude}{suffix}"
    if first:
        return ("-" if coef < 0 else "") + body
    return f" {'-' if coef < 0 else '+'} {body}"


def polynomial_latex(coefficients: Sequence[int], variable: str = "x") -> str:
    """Highest power first, e.g. ``[2, -5, 3]`` -> ``2x^2 - 5x + 3``."""
    degree = len(coefficients) - 1
    parts = []
    for index, coef in enumerate(coefficients):
        if coef == 0:
            continue
        power = degree - index
        if power == 0:
            suffix = ""
        elif power == 1:
            suffix = variable
        else:
            suffix = f"{variable}^{power}"
        parts.append(_term(coef, suffix, first=not parts))
    return "".join(parts) if parts else "0"


def quadratic_latex(a: int, b: int, c: int, variable: str = "x") -> str:
    return polynomial_latex([a, b, c], variable)


def linear_latex(m: int, k: int, variable: str = "x") -> str:
    """``mx + k`` with the usual sign and coefficient-1 rules."""
    return polynomial_latex([m, k], variable)


def factors_latex(factors: Sequence[Tuple[int, int]]) -> str:
    """``[(1, 2), (1, 3)]`` -> ``(x + 2)(x + 3)``."""
    return "".join(f"({linear_latex(m, k)})" for m, k in factors)


def square_form_latex(a: int, p: int, q: Number) -> str:
    """``a(x + p)^2 + q`` with the leading 1 / -1 written the usual way."""
    if p == 0:
        raise ValueError("p must be non-zero")
    inner = f"x + {p}" if p > 0 else f"x - {-p}"
    lead = "" if a == 1 else ("-" if a == -1 else str(a))
    return f"{lead}({inner})^2{signed_constant_latex(q)}"


def point_latex(x: Number, y: Number) -> str:
    return f"({number_latex(x)}, {number_latex(y)})"


def math(text: str) -> str:
    """Wrap LaTeX in inline-math delimiters."""
    return f"${text}$"


_MONEY_SPAN = re.compile(r"\$([\d.,\\ ]*\d[\d.,\\ ]*)\$ Namibian dollars?\b")


def localise_money(text: str) -> str:
    """``$450$ Namibian dollars`` -> ``N$450`` (how the exam prints money).

    The web renderer treats a ``$`` glued to a letter on its left and a digit on its
    right as currency, not as the start of a formula, so ``N$450`` is safe in a
    question that also contains ``$...$`` maths. Phrases such as "in Namibian
    dollars" with no amount are left alone.
    """

    def amount(match: "re.Match[str]") -> str:
        return "N$" + match.group(1).replace("\\,", " ").strip()

    text = _MONEY_SPAN.sub(amount, text)
    return _spell_out_bare_naira_sign(text)


def _spell_out_bare_naira_sign(text: str) -> str:
    """A bare ``N$`` with no amount after it (as in "in N$,") would open a maths span in the
    renderer, so outside maths it is spelled out. Inside a ``$...$`` span (``$M \\cup N$``) it
    is only a letter and a closing delimiter and is left alone."""
    out = []
    in_math = False
    i = 0
    while i < len(text):
        ch = text[i]
        if ch == "$":
            prev = text[i - 1] if i else ""
            nxt = text[i + 1] if i + 1 < len(text) else ""
            if not in_math and prev.isalnum() and nxt.isdigit():
                out.append(ch)  # currency amount such as N$450
            elif not in_math and prev == "N" and (i < 2 or not (text[i - 2].isalnum() or text[i - 2] in "$\\")):
                out.pop()  # drop the N already written
                out.append("Namibian dollars")
            else:
                in_math = not in_math
                out.append(ch)
        else:
            out.append(ch)
        i += 1
    return "".join(out)
