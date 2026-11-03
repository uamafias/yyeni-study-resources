"""Turn what learners type, and what mark schemes print, into things we can compare."""

from __future__ import annotations

import re
from fractions import Fraction
from typing import List, Optional

import sympy
from sympy.parsing.sympy_parser import (
    convert_xor,
    split_symbols,
    implicit_multiplication_application,
    parse_expr,
    standard_transformations,
)

_TRANSFORMS = standard_transformations + (split_symbols, implicit_multiplication_application, convert_xor)

_SUPERSCRIPTS = str.maketrans("⁰¹²³⁴⁵⁶⁷⁸⁹⁻", "0123456789-")
_SYMBOLS = {
    "−": "-", "–": "-", "—": "-", "×": "*", "÷": "/", "·": "*", "≥": ">=", "≤": "<=",
    "º": "°", "π": "pi", "√": "sqrt", "∞": "oo",
}
_CURRENCY = re.compile(r"(N\$|\$|£|€|\bN\s?\$)")
_UNIT_WORDS = re.compile(
    r"(?<=[\d)])\s*(units?|years?|days?|weeks?|months?|kilometres|kilometers|metres|meters|centimetres|centimeters|millimetres|"
    r"kilograms|grams|litres|liters|minutes|minute|mins|min|hours|hour|hrs|hr|seconds|"
    r"km/h|m/s|km|cm|mm|kg|ml|mph|dollars|cents|degrees|deg|sq\.? ?m|m²|cm²|m³|cm³|m|g|l|s|h)(?:\^[23])?\b\.?",
    re.IGNORECASE,
)


_FRAC = re.compile(r"\\[dt]?frac\s*\{([^{}]*)\}\s*\{([^{}]*)\}")
_SQRT = re.compile(r"\\sqrt\s*\{([^{}]*)\}")
_TEXT = re.compile(r"\\(?:text|mathrm|textrm|operatorname|mathit)\s*\{([^{}]*)\}")
_MATRIX = re.compile(r"\\begin\{[pbvBV]?matrix\}(.*?)\\end\{[pbvBV]?matrix\}", re.DOTALL)
_LATEX_WORDS = {
    r"\times": "*", r"\cdot": "*", r"\div": "/", r"\pi": "pi", r"\%": "%", r"\degree": "°", r"\circ": "°",
    r"\leq": "<=", r"\geq": ">=", r"\le": "<=", r"\ge": ">=", r"\neq": "!=", r"\ne": "!=", r"\lt": "<", r"\gt": ">",
    r"\infty": "oo", r"\left": "", r"\right": "", r"\;": " ", r"\,": " ", r"\!": " ", r"\quad": " ", r"\ ": " ",
    r"\{": "{", r"\}": "}", r"\dots": "", r"\ldots": "",
}


def latex_to_plain(text: str) -> str:
    """Turn what the maths keyboard types (``$$\\frac{1}{2}$$``, ``x^{2}``, ``\\begin{pmatrix}1&2\\\\3&4\\end{pmatrix}``) into the plain notation the
    checker reads. Text without a backslash or ``$$`` is returned unchanged. Anything not understood is left as it is,
    which the checker then reads as unreadable and hands to the grader."""
    if "\\" not in text and "$" not in text and "{" not in text:
        return text
    if len(text) > 600:
        return text
    t = re.sub(r"N\$\s*(?=\d)", "", text)  # N$450 is currency, not a maths delimiter
    t = t.replace("$$", " ").replace("$", " ")
    # A standalone mixed number uses adjacency, not multiplication. Preserve
    # its fractional part before the general fraction converter adds brackets.
    mixed = re.fullmatch(r"\s*([-+]?\d+)\s*\\[dt]?frac\s*\{(\d+)\}\s*\{(\d+)\}\s*", t)
    if mixed:
        return f"{mixed[1]} {mixed[2]}/{mixed[3]}"
    t = _MATRIX.sub(lambda m: "(" + "; ".join(" ".join(c.strip() for c in row.split("&")) for row in re.split(r"\\\\", m.group(1)) if row.strip()) + ")", t)
    t = _TEXT.sub(lambda m: " " + m.group(1).strip() + " ", t)
    for _ in range(12):  # nested fractions and roots, innermost first
        new = _FRAC.sub(lambda m: f"(({m.group(1)})/({m.group(2)}))", t)
        new = _SQRT.sub(lambda m: f"sqrt({m.group(1)})", new)
        if new == t:
            break
        t = new
    for word, plain in sorted(_LATEX_WORDS.items(), key=lambda kv: -len(kv[0])):
        t = t.replace(word, plain)
    t = re.sub(r"\^\{\s*°\s*\}", "°", t)
    t = re.sub(r"\^\{([^{}]*)\}", r"^(\1)", t)
    t = re.sub(r"_\{[^{}]*\}", "", t)
    return re.sub(r"\s+", " ", t).strip()


def clean(text: str) -> str:
    """Normalise symbols and whitespace; keep digits, letters, operators and brackets."""
    text = latex_to_plain(text)
    text = text.strip()
    # superscript digits become ^digits
    text = re.sub(r"([A-Za-z0-9)])([⁰¹²³⁴⁵⁶⁷⁸⁹⁻]+)", lambda m: m.group(1) + "^" + m.group(2).translate(_SUPERSCRIPTS), text)
    for a, b in _SYMBOLS.items():
        text = text.replace(a, b)
    # The keyboard writes cm^{2} as "cm ^(2)" after text/LaTeX cleanup.
    # Preserve that exponent as part of the unit; stripping only "cm" would
    # incorrectly turn 5 cm^{2} into the numerical calculation 5^2.
    text = re.sub(r"([A-Za-z]+)\s*\^\(([23])\)", r"\1^\2", text)
    text = _CURRENCY.sub("", text)
    text = text.replace(" ", " ").replace("$", "")
    text = re.sub(r"\s+", " ", text)
    return text.strip().rstrip(".")


def strip_units(text: str) -> str:
    text = re.sub(r"(?<=[\d.\s])\(\s*(?:%|[A-Za-z/]{1,8})\s*\)\s*$", "", text.strip())
    text = re.sub(r"^\(\s*[A-Za-z ]{2,10}\)\s*(?=\d)", "", text)
    text = re.sub(r"°\s*[CcFf]\b", "", text)
    text = _UNIT_WORDS.sub("", text)
    return text.replace("°", "").replace("%", "").strip()


_UNIT_CANON = {
    "kilometres": "km", "kilometers": "km", "km": "km", "metres": "m", "meters": "m", "m": "m",
    "centimetres": "cm", "centimeters": "cm", "cm": "cm", "millimetres": "mm", "mm": "mm",
    "kilograms": "kg", "kg": "kg", "grams": "g", "g": "g", "litres": "l", "liters": "l", "l": "l", "ml": "ml",
    "hours": "h", "hour": "h", "hrs": "h", "hr": "h", "h": "h", "minutes": "min", "minute": "min", "mins": "min", "min": "min",
    "seconds": "s", "s": "s", "km/h": "km/h", "m/s": "m/s", "mph": "mph", "degrees": "deg", "deg": "deg",
    "days": "day", "years": "year", "year": "year", "weeks": "week", "months": "month", "units": "unit", "unit": "unit",
    "dollars": "dollar", "cents": "cent",
}


def unit_of(text: str) -> Optional[str]:
    """The unit a number is written with (``5 cm`` -> ``cm``, ``20%`` -> ``%``, ``40°`` -> ``deg``), or None."""
    t = clean(text)
    t = re.sub(r"^[A-Za-z]\s*=\s*", "", t)
    if re.search(r"\d\s*%", t):
        return "%"
    if re.search(r"\d\s*°\s*[CcFf]\b", t):
        return "degc"
    if re.search(r"\d\s*°", t):
        return "deg"
    m = re.search(r"(?<=[\d)])\s*([A-Za-z/]+)(?:\^([23]))?\s*$", t)
    if m and m.group(1).lower() in _UNIT_CANON:
        return _UNIT_CANON[m.group(1).lower()] + ("^" + m.group(2) if m.group(2) else "")
    return None


def _fix_commas(text: str) -> str:
    # 1,250 and 12 000 -> 1250, 12000 (thousands separators) but keep "3, 4" lists
    text = re.sub(r"(?<=\d),(?=\d{3}(?!\d))", "", text)
    return re.sub(r"(?<=\d) (?=\d{3}(?!\d))", "", text)


MAX_INPUT_CHARS = 300
MAX_EXPONENT = 64


def _too_expensive(t: str) -> bool:
    """Refuse text that could make the parser or sympy do unbounded work (huge powers, factorials, giant integers)."""
    if len(t) > MAX_INPUT_CHARS or "!" in t:
        return True
    if re.search(r"\d{16,}", t.replace(" ", "")):
        return True
    for m in re.finditer(r"(?:\^|\*\*)\s*\(([^()]*)\)", t):
        # Compute no exponent expressions supplied by a learner. Literal
        # rational powers (surds) and a single symbolic power are sufficient.
        value = m[1].strip()
        literal = re.fullmatch(r"[-+]?\d+(?:\.\d+)?(?:\s*/\s*\d+)?|[A-Za-z]", value)
        # Index-law questions legitimately use 5^(8x+2y). Permit sums of
        # bounded linear terms, while refusing numeric exponent calculations.
        linear = re.fullmatch(r"[-+]?\s*(?:\d{1,2}\s*\*?\s*)?[A-Za-z](?:\s*[+-]\s*(?:(?:\d{1,2}\s*\*?\s*)?[A-Za-z]|\d{1,2}))*", value)
        if not (literal or linear):
            return True
    if re.search(r"(?:\^|\*\*)\s*\(?\s*[-+]?\s*(?:\d+(?:\.\d+)?|[A-Za-z])\s*\)?\s*(?:\^|\*\*)", t):  # a power of a power: 9^9^9, x^(2)^3
        return True
    for m in re.finditer(r"(?:\^|\*\*)\s*\(?\s*(-?\d+)", t):
        if abs(int(m.group(1))) > MAX_EXPONENT:
            return True
    return t.count("(") > 40


# The only names learner text can reach. No Python built-ins (``sum``, ``pow``, ``eval``,
# ``__import__``) and no other sympy functions: anything else is split into single-letter
# variables or rejected, never called.
_NAMESPACE = {
    "__builtins__": {},
    "sqrt": sympy.sqrt, "log": sympy.log, "pi": sympy.pi, "oo": sympy.oo,
    "Integer": sympy.Integer, "Float": sympy.Float, "Rational": sympy.Rational,
    "Symbol": sympy.Symbol, "Function": sympy.Function,
    "Add": sympy.Add, "Mul": sympy.Mul, "Pow": sympy.Pow,
}
MAX_OPS = 120  # symbolic size limit for a parsed answer


def safe_parse(text: str, *, evaluate: bool = True) -> sympy.Expr:
    """Parse preprocessed text with no Python built-ins; raises on anything unreadable or oversized."""
    expr = parse_expr(text, transformations=_TRANSFORMS, evaluate=evaluate, global_dict=dict(_NAMESPACE), local_dict={})
    if not isinstance(expr, sympy.Basic):
        raise ValueError("not an expression")
    if sympy.count_ops(expr, visual=False) > MAX_OPS or len(expr.free_symbols) > 8:
        raise ValueError("expression too large to check")
    return expr


def to_expr(text: str) -> Optional[sympy.Expr]:
    """Parse a maths expression; ``None`` if it cannot be read."""
    if _too_expensive(text):
        return None
    t = _fix_commas(clean(text)).replace("[", "(").replace("]", ")")
    t = re.sub(r"(?<=\d) x (?=\d)", "*", t)
    t = re.sub(r"(\d)\s*pi\b", r"\1*pi", t)
    t = re.sub(r"(?<![A-Za-z])sqrt\s*([0-9A-Za-z.]+)", r"sqrt(\1)", t)
    t = re.sub(r"(?<![A-Za-z])log\s*([0-9]+(?:\.[0-9]+)?|[A-Za-z])(?![\w(])", r"log(\1)", t)
    t = re.sub(r"\^(-\d+(?:\.\d+)?)", r"**(\1)", t)
    t = t.replace("^", "**")
    if not t or re.search(r"[A-Za-z]{4,}", re.sub(r"sqrt|pi|oo", "", t)):
        return None
    if _too_expensive(t):
        return None  # also inspect powers revealed by LaTeX normalization
    try:
        return safe_parse(t)
    except Exception:
        return None


_NUM = r"[-+]?\s*(?:\d+\s*/\s*\d+|\d*\.\d+|\d+)"


def to_number(text: str) -> Optional[Fraction]:
    """Read a plain number (integer, decimal, fraction, percent, mixed number)."""
    if len(text) > MAX_INPUT_CHARS:
        return None
    t = strip_units(_fix_commas(clean(text)))
    t = re.sub(r"^[A-Za-z]\s*=\s*", "", t)
    m = re.fullmatch(r"([-+]?)\s*(\d+)\s+(\d+)\s*/\s*(\d+)", t)  # mixed number 2 1/2
    try:
        if m:
            v = Fraction(int(m[2])) + Fraction(int(m[3]), int(m[4]))
            return -v if m[1] == "-" else v
        if re.fullmatch(_NUM, t):
            return Fraction(t.replace(" ", ""))
        expr = to_expr(t)
        if expr is not None and expr.is_number and expr.is_rational:
            return Fraction(int(expr.p), int(expr.q))
    except Exception:
        return None
    return None


def numbers_in(text: str) -> List[Fraction]:
    if len(text) > MAX_INPUT_CHARS:
        return []
    return _numbers_in(text)


def _numbers_in(text: str) -> List[Fraction]:
    """Every number in order, e.g. ``(-6, -2)`` -> [-6, -2]; fractions like 1/14 stay whole.

    A dash between two numbers is a range (``125-135``), not a minus sign.
    """
    t = _fix_commas(clean(text))
    t = re.sub(r"(\d)(?:-|\s-\s|\s+to\s+)(?=\d)", r"\1 to ", t)
    out = []
    for m in re.finditer(r"(?<![\w.])[-+]?\s*(?:\d+\s*/\s*\d+|\d*\.\d+|\d+)", t):
        try:
            out.append(Fraction(m.group(0).replace(" ", "")))
        except Exception:
            pass
    return out


_ALT_SPLIT = re.compile(r"\s+(?:or|OR|accept|isw)\b\.?\s*|\s+/\s+|\s*;\s*(?=[A-Za-z(\d\-])", re.IGNORECASE)


def official_alternatives(text: Optional[str], *, required_list: bool = False) -> List[str]:
    """Split a printed mark-scheme answer into the separate answers it accepts.

    Mark schemes write ``0.8 / 4/5``, ``-1.5 oe``, ``26.3(4339183)°`` and
    ``x = -1 or x = 3``. We drop calculator tails and ``a.r.t``/``oe`` words and split
    on ``or``.

    An ``or`` can mean "either of these is accepted" (``0.8 / 4/5``) or "both are needed"
    (``x = -1 or x = 3``); the text alone cannot tell, so the caller says which:

    * default (``required_list=False``): the pieces are alternatives; if there is only one
      piece, that one answer. The whole string is returned only when it is the one answer.
    * ``required_list=True``: the whole cleaned string, to be read as a list by the checker
      for equation solutions, coordinate pairs and sets.
    """
    if not text:
        return []
    s = re.sub(r"(?<=\d)\.?\(\s*[\d. ]+(?:\)|$)(?:\.\.\.)?", "", text)   # 26.3(4339183) -> 26.3, 149.(44..) -> 149
    s = re.sub(r"\(\s*(?:accept|also|garbled|exact|strictly|recurring)[^)]*\)?", "", s, flags=re.IGNORECASE)
    s = re.sub(r"\b(?:a\.r\.t|art|ft|cao|c\.a\.o\.?)\b\.?", "", s, flags=re.IGNORECASE)
    s = re.sub(r"\s+(?:o\.?e\.?|isw|recurring)\b", "", s, flags=re.IGNORECASE)
    s = re.sub(r"\[[^\]]*[A-Za-z]{4,}[^\]]*\]", "", s)
    s = s.replace("...", "").replace("[", "").replace("]", "")
    parts = [p.strip(" ;,") for p in _ALT_SPLIT.split(s) if p and p.strip(" ;,")]
    full = s.strip(" ;,")
    if required_list or len(parts) < 2:
        out = [full]
    else:
        out = [p for p in parts if p]
    seen, uniq = set(), []
    for p in out:
        if p and p not in seen:
            seen.add(p)
            uniq.append(p)
    return uniq
