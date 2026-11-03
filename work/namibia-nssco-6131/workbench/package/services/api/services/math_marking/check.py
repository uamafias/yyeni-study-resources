"""Decide whether a typed final answer matches the right one."""

from __future__ import annotations

import re
from dataclasses import dataclass
from decimal import ROUND_HALF_UP, Decimal
from functools import lru_cache
from fractions import Fraction
from math import gcd
from typing import Dict, List, Optional, Sequence, Tuple, Union

import sympy

from .parse import clean, numbers_in, strip_units, to_expr, to_number, unit_of

Expected = Union[str, Sequence[str]]

# Answer types that a program can decide (matches analysis/taxonomy.json).
NUMBER_TYPES = {"number_exact", "number_rounded", "standard_form", "table_values", "graph_reading"}
EXPRESSION_TYPES = {"expression"}
SOLUTION_TYPES = {"equation_solution"}
TUPLE_TYPES = {"coordinates", "vector", "matrix", "sequence"}
SET_TYPES = {"set_answer"}
JUDGE_TYPES = {"text_reason", "text_description", "show_that", "other", "draw_or_construct"}


@dataclass(frozen=True)
class Verdict:
    correct: bool
    reason: str
    needs_judge: bool = False
    unreadable: bool = False
    # The learner typed a unit and the card gave us nothing to compare it with, so the
    # unit has NOT been checked. Callers must not treat the answer as fully verified.
    unit_unchecked: bool = False


def _v(ok: bool, reason: str) -> Verdict:
    return Verdict(ok, reason)


def _judge(reason: str) -> Verdict:
    return Verdict(False, reason, needs_judge=True)


def _alts(expected: Expected) -> List[str]:
    return [expected] if isinstance(expected, str) else list(expected)


# ---------------------------------------------------------------- numbers
def _round_to(value: Fraction, rounding: str, n: int) -> Decimal:
    d = Decimal(value.numerator) / Decimal(value.denominator)
    if rounding == "sig_figs":
        if d == 0:
            return Decimal(0)
        exp = d.adjusted() - (n - 1)
        q = Decimal(1).scaleb(exp)
        return d.quantize(q, rounding=ROUND_HALF_UP) if exp < 0 or True else d
    places = 1 if rounding == "angle_1dp" else n
    return d.quantize(Decimal(1).scaleb(-places), rounding=ROUND_HALF_UP)


def _std_form(text: str) -> Optional[Fraction]:
    t = strip_units(clean(text)).replace(" ", "")
    m = re.fullmatch(r"([-+]?\d*\.?\d+)\*?(?:x|\*)?10\^\(?(-?\d+)\)?", t.replace("x", "*"))
    if not m or abs(int(m[2])) > 300 or len(m[1]) > 30:
        return None
    return Fraction(m[1]) * (Fraction(10) ** int(m[2]))


def _num(text: str) -> Optional[Fraction]:
    v = _std_form(text)
    return v if v is not None else to_number(text)


def _range(text: str) -> Optional[Tuple[Fraction, Fraction]]:
    m = re.fullmatch(r"\s*([\d.]+)\s*(?:-|to)\s*([\d.]+)\s*", strip_units(clean(text)))
    return (Fraction(m[1]), Fraction(m[2])) if m else None


def _fix(text: str) -> str:
    return clean(text)


def _exact_value(text: str) -> Optional[sympy.Expr]:
    expr = to_expr(strip_units(_fix(text)))
    return expr if expr is not None and expr.is_number else None


_STRICT_ROUNDING = ("sig_figs", "decimal_places", "angle_1dp")


def check_number(expected: Expected, given: str, rounding: str = "none", digits: int = 3) -> Verdict:
    g = _num(given)
    g_exact = None if g is not None else _exact_value(given)
    if g is None and g_exact is None:
        return Verdict(False, "could not read a number", unreadable=True)
    given_unit = unit_of(given)
    strict = rounding in _STRICT_ROUNDING
    unit_unchecked = False
    for e in _alts(expected):
        expected_unit = unit_of(e)
        if given_unit and expected_unit and given_unit != expected_unit:
            continue  # right number, wrong unit
        unchecked = bool(given_unit and not expected_unit)
        rng = _range(e)
        if rng and g is not None:
            if rng[0] <= g <= rng[1]:
                return Verdict(True, "inside the accepted range", unit_unchecked=unchecked)
            continue
        ev = _num(e)
        if ev is None:
            e_exact = _exact_value(e)
            if e_exact is None:
                continue
            gv = g_exact if g_exact is not None else sympy.Rational(g.numerator, g.denominator)
            # An exact form (36pi, 4sqrt(5)) that the card lists as an accepted answer is accepted as written,
            # even when a rounding rule is stated: mark schemes list both ("113 or 36pi").
            if _same_value(e_exact, gv):
                return Verdict(True, "equal", unit_unchecked=unchecked)
            if strict:
                ef = Fraction(str(sympy.N(e_exact, 30)))
                gf = Fraction(str(sympy.N(gv, 30)))
                want = _round_to(ef, rounding, digits)
                if Decimal(gf.numerator) / Decimal(gf.denominator) == want and g_exact is None:
                    return Verdict(True, "equal after rounding", unit_unchecked=unchecked)
            continue
        if g_exact is not None:
            continue  # an exact surd where a number was wanted
        if not strict:
            if g == ev:
                return Verdict(True, "equal", unit_unchecked=unchecked)
        else:
            want = _round_to(ev, rounding, digits)
            got = Decimal(g.numerator) / Decimal(g.denominator)
            if got == want:
                return Verdict(True, "equal after rounding", unit_unchecked=unchecked)
    return _v(False, "different value" if not (given_unit and any(unit_of(e) and unit_of(e) != given_unit for e in _alts(expected))) else "different unit")


# ---------------------------------------------------------------- expressions
MAX_EXPANDED_TERMS = 3000


def _expanded_terms(e) -> int:
    """Upper bound on the number of terms ``sympy.expand`` would produce (it can blow up: (a+b+c+d)**64)."""
    cap = MAX_EXPANDED_TERMS * 1000
    if e.is_Add:
        return min(sum(_expanded_terms(a) for a in e.args), cap)
    if e.is_Mul:
        n = 1
        for a in e.args:
            n *= _expanded_terms(a)
            if n > cap:
                return cap
        return n
    if e.is_Pow and e.exp.is_Integer and e.exp > 0:
        return min(_expanded_terms(e.base) ** int(e.exp), cap)
    return 1


def _cheap(*exprs) -> bool:
    return all(_expanded_terms(e) <= MAX_EXPANDED_TERMS for e in exprs)


def _equiv(a: sympy.Expr, b: sympy.Expr) -> bool:
    try:
        if not _cheap(a, b):
            return False
        return sympy.simplify(sympy.expand(a - b)) == 0
    except Exception:
        return False


def _equiv_log(a: sympy.Expr, b: sympy.Expr) -> bool:
    try:
        if not _cheap(a, b):
            return False
        return sympy.simplify(sympy.expand_log(sympy.expand(a - b), force=True)) == 0
    except Exception:
        return False


def _remainder_parts(text: str) -> Optional[Tuple[str, str]]:
    m = re.fullmatch(r"(.+?)\s+remainder\s+(.+)", clean(text), flags=re.IGNORECASE)
    return (m[1], m[2]) if m else None


def _fully_factorised(text: str) -> bool:
    """True if the typed expression is a product (or power) whose bracketed parts cannot be factorised further."""
    from .parse import safe_parse

    t = clean(text)
    if "=" in t:
        t = t.split("=", 1)[1]
    t = re.sub(r"\^(-\d+)", r"**(\1)", t).replace("^", "**")
    try:
        expr = safe_parse(t, evaluate=False)
    except Exception:
        return False
    if expr.is_Add or expr.is_Atom:
        return False
    factors = list(expr.args) if expr.is_Mul else [expr]
    for f in factors:
        base = f.base if f.is_Pow else f
        if base.is_Add:
            content, parts = sympy.factor_list(sympy.expand(base))
            if len(parts) != 1 or parts[0][1] != 1 or abs(content) != 1:
                return False
    return True


def _prime_factor_counts(text: str):
    """``2^2 x 3``, ``2 x 2 x 3``, ``2²×3`` -> Counter({2: 2, 3: 1}); None unless it is a product of primes."""
    from collections import Counter

    t = clean(text)
    t = re.sub(r"(?<=[\d)])\s*[x×·]\s*(?=[\d(])", "*", t)
    t = t.replace("×", "*").replace("·", "*")
    counts: Counter = Counter()
    for tok in t.split("*"):
        m = re.fullmatch(r"\s*\(?\s*(\d+)\s*(?:\^\s*\(?\s*(\d+)\s*\)?)?\s*\)?\s*", tok)
        if not m:
            return None
        base, exp = int(m.group(1)), int(m.group(2) or 1)
        if base < 2 or base > 10**9 or exp < 1 or exp > 64 or sympy.factorint(base) != {base: 1}:
            return None
        counts[base] += exp
    return counts


def check_prime_factors(expected: Expected, given: str) -> Verdict:
    g = _prime_factor_counts(given)
    if g is None:
        return _v(False, "not written as a product of prime numbers")
    for e in _alts(expected):
        ev = _prime_factor_counts(e)
        if ev is not None and ev == g:
            return _v(True, "same prime factors")
    return _v(False, "different prime factors")


def _simplest_surds(text: str) -> bool:
    """Every root is written ``sqrt(n)`` / ``sqrt n`` / ``√n`` with n a whole number with no square factor.

    ``sqrt(80)`` fails (16 divides it), ``4 sqrt(5)`` passes, and any other way of writing a root
    (``sqrt(5*16)``, ``80^(1/2)``, ``80**0.5``) fails because it is not the simplest written form.
    """
    t = clean(text).replace("√", "sqrt")
    if re.search(r"\^\s*\(?\s*(?:1\s*/\s*2|0?\.5)\s*\)?|\*\*\s*\(?\s*(?:1\s*/\s*2|0?\.5)", t):
        return False
    for m in re.finditer(r"sqrt", t):
        rest = t[m.end():]
        n = re.match(r"\s*\(\s*(\d+)\s*\)|\s*(\d+)", rest)
        if not n:
            return False  # sqrt of something that is not a plain whole number
        k = int(n.group(1) or n.group(2))
        if any(e > 1 for e in sympy.factorint(k).values()):
            return False
    return True


def _fraction_form(text: str, *, mixed_only: bool = False) -> bool:
    """Check the written integers before Fraction/SymPy cancels common factors.

    Redundant brackets from the maths keyboard are harmless; calculations,
    decimals, negative denominators and unreduced fractional parts are not.
    """
    t = clean(text)
    for _ in range(20):
        reduced = re.sub(r"\(\s*([-+]?\d+)\s*\)", r"\1", t)
        reduced = re.sub(r"\(\s*([-+]?\d+\s*/\s*\d+)\s*\)", r"\1", reduced)
        if reduced == t:
            break
        t = reduced
    m = re.fullmatch(r"([-+]?)\s*(?:(\d+)\s+)?(\d+)\s*/\s*(\d+)", t)
    if m:
        whole, n, d = m[2], int(m[3]), int(m[4])
        return d > 1 and gcd(n, d) == 1 and (whole is None or (int(whole) > 0 and 0 < n < d)) and (not mixed_only or whole is not None)
    return not mixed_only and bool(re.fullmatch(r"[-+]?\d+", t))


def _completed_square(text: str) -> bool:
    """Require a(x+p)^2+q with a monic linear bracket, not its expansion."""
    from .parse import safe_parse

    t = clean(text).split("=", 1)[-1].replace("^", "**")
    try:
        expr = safe_parse(t, evaluate=False)
        terms = list(expr.args) if expr.is_Add else [expr]
        square_terms = [term for term in terms if term.free_symbols]
        if len(square_terms) != 1:
            return False
        factors = list(square_terms[0].args) if square_terms[0].is_Mul else square_terms
        powers = [f for f in factors if f.free_symbols]
        if len(powers) != 1 or not powers[0].is_Pow or powers[0].exp != 2:
            return False
        base = powers[0].base
        if len(base.free_symbols) != 1:
            return False
        x = next(iter(base.free_symbols))
        return sympy.Poly(base, x).degree() == 1 and sympy.Poly(base, x).LC() == 1
    except Exception:
        return False


def _algebraic_fraction(text: str, *, simplest: bool) -> bool:
    """Check the written fraction before automatic cancellation can hide work."""
    from .parse import safe_parse

    try:
        expr = safe_parse(clean(text).replace("^", "**"), evaluate=False)
        # A sum containing separate variable denominators is not one fraction.
        for node in sympy.preorder_traversal(expr):
            if node.is_Add and any(term.as_numer_denom()[1].free_symbols for term in node.args):
                return False
        num, den = expr.as_numer_denom()
        symbols = sorted(expr.free_symbols, key=str)
        if not symbols or len(symbols) > 3:
            return False
        if max(sympy.Poly(num, *symbols).total_degree(), sympy.Poly(den, *symbols).total_degree()) > 6:
            return False
        common = sympy.gcd(num, den)
        return not simplest or common in (1, -1)
    except (ValueError, TypeError, sympy.PolynomialError):
        return False


def check_expression(expected: Expected, given: str, form: Optional[str] = None) -> Verdict:
    g_text = clean(given)
    g_rem = _remainder_parts(g_text)
    for e in _alts(expected):
        e_rem = _remainder_parts(e)
        if e_rem and g_rem:
            q1, r1, q2, r2 = (to_expr(x) for x in (*e_rem, *g_rem))
            if None not in (q1, r1, q2, r2) and _equiv(q1, q2) and _equiv(r1, r2):
                return _v(True, "same quotient and remainder")
            return _v(False, "different quotient or remainder")
        if e_rem or g_rem:
            return Verdict(False, "could not read quotient and remainder", unreadable=bool(e_rem and not g_rem))
    for e in _alts(expected):
        e_text = clean(e)
        if "=" in e_text and "=" in g_text and "==" not in e_text and ">=" not in e_text and "<=" not in e_text:
            el, er = (to_expr(p) for p in e_text.split("=", 1))
            gl, gr = (to_expr(p) for p in g_text.split("=", 1))
            if None in (el, er, gl, gr):
                continue
            if el == gl and _equiv(er, gr):
                return _v(True, "equivalent equation")
            diff_e, diff_g = el - er, gl - gr
            if diff_e != 0 and diff_g != 0:
                try:
                    ratio = sympy.simplify(diff_g / diff_e)
                    if ratio.is_number and ratio != 0:
                        return _v(True, "equivalent equation")
                except Exception:
                    pass
            continue
        if "=" in e_text and "=" not in g_text and ">=" not in e_text and "<=" not in e_text:
            e_text = e_text.split("=", 1)[1]
        if "=" in g_text and "=" not in e_text and ">=" not in g_text and "<=" not in g_text:
            g_text = g_text.split("=", 1)[1]
        ee, ge = to_expr(e_text), to_expr(g_text)
        if ge is None:
            return Verdict(False, "could not read an expression", unreadable=True)
        if ee is None:
            continue
        if _equiv(ee, ge) or _equiv_log(ee, ge):
            if form == "factorised" and not _fully_factorised(g_text):
                return _v(False, "equivalent but not fully factorised")
            if form == "expanded" and sympy.expand(ge) != ge:
                return _v(False, "equivalent but not expanded")
            return _v(True, "equivalent")
    return _v(False, "not equivalent")


# ---------------------------------------------------------------- solutions
def _assignments(text: str) -> Dict[str, List[Fraction]]:
    """``x = -1 or x = 3`` -> {x: [-1, 3]}; bare numbers go under ``""``."""
    out: Dict[str, List[Fraction]] = {}
    t = clean(text).replace("[", "").replace("]", "")
    t = re.sub(r"±\s*(\S+)", r"\1, -\1", t) if "±" in t else t
    t = re.sub(r"\b(and|or)\b", ",", t)
    t = re.sub(r"\s*;\s*", ",", t)
    for part in re.split(r",(?!\d{3}\b)", t):
        part = part.strip()
        if not part:
            continue
        m = re.fullmatch(r"\[?\(?([A-Za-z])\)?\s*=\s*(.+?)\]?", part)
        var, rhs = (m[1], m[2]) if m else ("", part)
        v = _num(rhs)
        if v is None:
            expr = to_expr(rhs)
            if expr is None or not expr.is_number:
                return {}
            out.setdefault(var, []).append(expr)  # type: ignore[arg-type]
            continue
        out.setdefault(var, []).append(sympy.Rational(v.numerator, v.denominator))
    named = [k for k in out if k]
    if "" in out and len(named) == 1:  # "x = 109.5, 250.5": the bare values belong to x
        out[named[0]] += out.pop("")
    return out


def _same_value(x, y) -> bool:
    try:
        return x == y or sympy.simplify(x - y) == 0
    except Exception:
        return False


def _same_multiset(a: list, b: list) -> bool:
    if len(a) != len(b):
        return False
    rest = list(b)
    for x in a:
        for i, y in enumerate(rest):
            if _same_value(x, y):
                del rest[i]
                break
        else:
            return False
    return True


def _sequential_groups(text: str) -> List[str]:
    """Split ``x=-4, y=9, x=3, y=16`` into ``x=-4, y=9`` and ``x=3, y=16``: a group ends when a variable repeats."""
    t = clean(text).replace("[", "").replace("]", "")
    parts = [p.strip() for p in re.split(r"\s*,\s*|\s+(?:and|AND)\s+", t) if p.strip()]
    groups: List[List[str]] = [[]]
    seen: set = set()
    for part in parts:
        m = re.match(r"([A-Za-z])\s*=", part)
        if m and m.group(1) in seen:
            groups.append([])
            seen = set()
        if m:
            seen.add(m.group(1))
        groups[-1].append(part)
    return [", ".join(g) for g in groups if g]


def _paired_groups(text: str):
    """``x = -4, y = 16; x = 3, y = 9`` -> [{x: -4, y: 16}, {x: 3, y: 9}] (None unless 2+ groups name the same variables)."""
    groups = [g for g in re.split(r"\s*;\s*|\s+(?:or|OR)\s+", clean(text)) if g.strip()]
    if len(groups) < 2:
        groups = _sequential_groups(text)
    if len(groups) < 2:
        return None
    parsed = [_assignments(g) for g in groups]
    if any(not a or "" in a or any(len(v) != 1 for v in a.values()) for a in parsed):
        return None
    if len({tuple(sorted(a)) for a in parsed}) != 1 or len(parsed[0]) < 2:
        return None
    return [{k: v[0] for k, v in a.items()} for a in parsed]


def _same_groups(a, b) -> bool:
    if len(a) != len(b):
        return False
    rest = list(b)
    for x in a:
        for i, y in enumerate(rest):
            if set(x) == set(y) and all(_same_value(x[k], y[k]) for k in x):
                del rest[i]
                break
        else:
            return False
    return True


def _pairs(text: str) -> Optional[List[Tuple[Fraction, ...]]]:
    groups = re.findall(r"\(([^()]*,[^()]*)\)", clean(text))
    if not groups:
        return None
    return [tuple(numbers_in(x)) for x in groups]


def check_solutions(expected: Expected, given: str, rounding: str = "none", digits: int = 3) -> Verdict:
    gp = _pairs(given)
    if gp and any(_pairs(e) for e in _alts(expected)):
        for e in _alts(expected):
            ep = _pairs(e)
            if ep and sorted(ep) == sorted(gp):
                return _v(True, "same pairs")
        return _v(False, "different pairs")
    paired = _paired_groups(given)
    if paired is not None:
        for e in _alts(expected):
            ep = _paired_groups(e)
            if ep is not None and _same_groups(ep, paired):
                return _v(True, "same paired solutions")
        if any(_paired_groups(e) is not None for e in _alts(expected)):
            return _v(False, "different paired solutions")
    g = _assignments(given)
    if not g:
        return Verdict(False, "could not read the solutions", unreadable=True)
    for e in _alts(expected):
        ex = _assignments(e)
        if not ex:
            continue
        # a bare list may stand for named solutions and vice versa
        if set(ex) == set(g) and all(_same_multiset(ex[k], g[k]) for k in ex):
            return _v(True, "same solutions")
        flat_e = [x for k in sorted(ex) for x in ex[k]]
        flat_g = [x for k in sorted(g) for x in g[k]]
        if set(ex) <= {""} or set(g) <= {""}:
            if _same_multiset(flat_e, flat_g):
                return _v(True, "same solutions")
        if rounding in ("sig_figs", "decimal_places", "angle_1dp") and set(ex) == set(g) and len(flat_e) == len(flat_g) == 1:
            if check_number(str(float(flat_e[0])), str(float(flat_g[0])), rounding, digits).correct:
                return _v(True, "same after rounding")
    return _v(False, "different solutions")


# ---------------------------------------------------------------- ordered lists
_WORDS = re.compile(r"\bcolumn vector\b|\bcolumn\b|\bmatrix\b|\brow\b|\bas a \d ?x ?\d\b|\(\s*[A-Za-z ]{2,12}\)", re.IGNORECASE)


def _bare(text: str) -> str:
    return _WORDS.sub(" ", text)


_SCALAR_MATRIX = re.compile(r"^\s*([-+]?\s*\d+\s*/\s*\d+|[-+]?\s*\d*\.\d+|[-+]?\s*\d+)\s*(?:x|\*)?\s*(?=[\(\[])")


def _row_lengths(text: str) -> List[int]:
    """Entries per row: rows are separated by ';', by '],[' or by new lines."""
    t = _bare(clean(text))
    m = _SCALAR_MATRIX.match(t)
    if m:
        t = t[m.end():]
    if "[[" in t.replace(" ", "") or re.search(r"\]\s*,\s*\[", t):
        rows = re.findall(r"\[([^\[\]]*)\]", t)
    elif ";" in t:
        rows = t.split(";")
    else:
        rows = [t]
    return [len(numbers_in(r)) for r in rows if numbers_in(r)]


def _matrix_entries(text: str) -> List[Fraction]:
    """Entries of a matrix, with a leading scalar (``1/7 (2 1; 3 5)``) multiplied in."""
    t = _bare(clean(text))
    m = _SCALAR_MATRIX.match(t)
    if m:
        k = Fraction(m.group(1).replace(" ", ""))
        return [k * v for v in numbers_in(t[m.end():])]
    return numbers_in(t)


_VALUE_TOKEN = re.compile(r"[-+]?\d+(?:\.\d+)?(?:\s*/\s*\d+)?")


def _is_plain_list(text: str) -> bool:
    """Only numbers separated by commas, semicolons, spaces or brackets: no '+', '*', 'x', words..."""
    t = _bare(clean(text))
    t = re.sub(r"[()\[\]{}]", " ", t)
    t = _fix_commas_for_lists(t)
    for tok in re.split(r"[,;:\s]+", t.strip()):
        if tok and not _VALUE_TOKEN.fullmatch(tok):
            return False
    return True


def _fix_commas_for_lists(t: str) -> str:
    return re.sub(r"(?<=\d)\s*/\s*(?=\d)", "/", t)


def check_tuple(expected: Expected, given: str, matrix: bool = False) -> Verdict:
    if matrix:
        g = _matrix_entries(given)
        if not g or not _is_plain_list(re.sub(_SCALAR_MATRIX, " ", _bare(clean(given)), count=1)):
            return Verdict(False, "could not read the matrix entries", unreadable=not g)
        for e in _alts(expected):
            if _matrix_entries(e) != g:
                continue
            want_rows, got_rows = _row_lengths(e), _row_lengths(given)
            if len(want_rows) > 1 and want_rows != got_rows:
                continue  # same numbers, different shape
            return _v(True, "same entries")
        if any(_matrix_entries(e) for e in _alts(expected)):
            return _v(False, "different entries or shape")
    if any(re.search(r"[A-Za-z]\s*=.*,", x) for x in _alts(expected)):
        return check_solutions(expected, given)
    if any(re.search(r"[A-Za-z]", _bare(x)) for x in _alts(expected)):
        return check_expression([_bare(x) for x in _alts(expected)], _bare(given))
    given = _bare(given)
    g = numbers_in(given)
    if not g:
        return Verdict(False, "could not read numbers", unreadable=True)
    if not _is_plain_list(given):
        return _v(False, "not written as a list of values")
    for e in _alts(expected):
        ev = numbers_in(_bare(e))
        if ev and ev == g:
            return _v(True, "same values in order")
    return _v(False, "different values")


# ---------------------------------------------------------------- sets
def _elements(text: str) -> Optional[List[str]]:
    t = clean(text).strip("{} ").strip()
    if not t:
        return []
    parts = [p.strip() for p in re.split(r"[,;]", t) if p.strip()]
    out = []
    for p in parts:
        v = _num(p)
        out.append(str(v) if v is not None else p.lower())
    return out


def check_set(expected: Expected, given: str) -> Verdict:
    g = _elements(given)
    if g is None:
        return Verdict(False, "could not read a set", unreadable=True)
    for e in _alts(expected):
        ev = _elements(e)
        if ev is not None and set(ev) == set(g) and len(set(g)) == len(g):
            return _v(True, "same elements")
    return _v(False, "different elements")


# ---------------------------------------------------------------- inequalities
_REL = re.compile(r"(>=|<=|!=|>|<)")
def _inequality_regions(text):
    """Parse bounded, low-degree polynomial conditions using exact coefficients."""
    regions = []
    for chunk in re.split(r"\s+or\s+", clean(text), flags=re.IGNORECASE):
        conditions = []
        for piece in re.split(r"\s+and\s+|[;,]", chunk, flags=re.IGNORECASE):
            if not piece.strip():
                continue
            bits = _REL.split(piece)
            if len(bits) < 3:
                return None
            exprs = [to_expr(x) for x in bits[0::2]]
            if None in exprs:
                return None
            for left, op, right in zip(exprs, bits[1::2], exprs[1:]):
                diff = left - right
                diff = diff.xreplace({f: sympy.Rational(str(f)) for f in diff.atoms(sympy.Float)})
                names = sorted(diff.free_symbols, key=str)
                if not names or len(names) > 2:
                    return None
                try:
                    poly = sympy.Poly(diff, *names)
                    if poly.total_degree() > 2 or not all(c.is_Rational for c in poly.coeffs()):
                        return None
                except sympy.PolynomialError:
                    return None
                if op in (">", ">="):
                    diff = -diff
                    op = "<" if op == ">" else "<="
                lead = sympy.Poly(diff, *names).LC()
                diff = sympy.expand(diff / (lead if op == "!=" else abs(lead)))
                conditions.append((diff, op))
        if not conditions:
            return None
        regions.append(tuple(conditions))
    if sum(map(len, regions)) > 8:
        return None
    return tuple(regions)


def _region_key(regions):
    return frozenset(frozenset((sympy.srepr(d), op) for d, op in region) for region in regions)


def _inequality_set(regions, name):
    var = sympy.Symbol(str(name), real=True)
    result = sympy.S.EmptySet
    for region in regions:
        interval = sympy.S.Reals
        for diff, op in region:
            expr = diff.subs(name, var)
            rel = {"<": sympy.Lt, "<=": sympy.Le, "!=": sympy.Ne}[op](expr, 0)
            interval = interval.intersect(sympy.solve_univariate_inequality(rel, var, relational=False))
        result = result.union(interval)
    return result


@lru_cache(maxsize=2048)
def _parsed_inequality(text):
    return _inequality_regions(text)


def check_inequality(expected: Expected, given: str) -> Verdict:
    """Never award equivalence from a grid of sampled points.

    Normalize linear/polynomial conditions exactly first. For one variable,
    compare exact solution sets (including open boundaries and excluded roots).
    Multivariable rewrites that cannot be proved by normalization remain for the
    judge; a false negative here never withholds a mark automatically.
    """
    gc = _parsed_inequality(given)
    if gc is None:
        return Verdict(False, "could not read a bounded polynomial inequality", unreadable=True)
    for e in _alts(expected):
        ec = _parsed_inequality(e)
        if ec is None:
            continue
        if _region_key(ec) == _region_key(gc):
            return _v(True, "same exact conditions")
        names = set().union(*(d.free_symbols for region in ec + gc for d, _ in region))
        if len(names) == 1:
            name = next(iter(names))
            try:
                if _inequality_set(ec, name) == _inequality_set(gc, name):
                    return _v(True, "same exact range of values")
            except (NotImplementedError, ValueError, TypeError):
                continue
    return _v(False, "ranges differ or equivalence was not proved")


# ---------------------------------------------------------------- time
def _time_value(text: str) -> Optional[Tuple[str, int]]:
    """('clock', minutes since midnight) for 13:09 / 7.17 pm, ('duration', minutes) for 4 h 32 min; None if unreadable
    or impossible (37:09, 12:69)."""
    t = clean(text).lower()
    t = t.replace("a:m", "am").replace("p:m", "pm").replace("a.m.", "am").replace("p.m.", "pm")
    m = re.search(r"(\d{1,2})\s*[:.]\s*(\d{2})\s*([ap]m)?\b", t)
    if m and (":" in t or m.group(3)):
        h, mi = int(m[1]), int(m[2])
        if mi > 59 or h > 23 or (m.group(3) and not 1 <= h <= 12):
            return None
        if m.group(3) == "pm" and h < 12:
            h += 12
        if m.group(3) == "am" and h == 12:
            h = 0
        return "clock", h * 60 + mi
    d = re.search(r"(\d+)\s*(?:days?|d)\b", t)
    h = re.search(r"(\d+)\s*(?:hours?|hrs?|h)\b", t)
    mi = re.search(r"(\d+)\s*(?:minutes?|mins?|m)\b", t)
    if h or mi or d:
        return "duration", (int(d[1]) * 1440 if d else 0) + (int(h[1]) * 60 if h else 0) + (int(mi[1]) if mi else 0)
    return None


def check_time(expected: Expected, given: str) -> Verdict:
    g = _time_value(given)
    durations = [e for e in _alts(expected) if ":" not in e and re.search(r"[a-z]", e.lower())]
    if g is None and durations and re.fullmatch(r"\s*\d+\s*", given):
        g = ("duration", int(given))  # a bare number for a duration means minutes
    if g is None:
        return Verdict(False, "could not read a time", unreadable=True)
    for e in _alts(expected):
        ev = _time_value(e)
        if ev is not None and ev == g:
            return _v(True, "same time")
    return _v(False, "different time")


# ---------------------------------------------------------------- entry point
def check(
    answer_type: str,
    expected: Expected,
    given: str,
    *,
    rounding: str = "none",
    digits: int = 3,
    form: Optional[str] = None,
) -> Verdict:
    """Mark one final answer.

    ``expected`` is one answer or a list of equally good answers. ``rounding`` is one of
    ``none, sig_figs, decimal_places, angle_1dp, nearest_unit``; ``digits`` is the number
    of figures or places. ``form`` can be ``factorised`` or ``expanded``.
    """
    if not given or not given.strip():
        return Verdict(False, "no answer")
    if len(given) > 2000:
        return Verdict(False, "answer too long to check", unreadable=True)
    try:
        verdict = _check(answer_type, expected, given, rounding=rounding, digits=digits, form=form)
    except Exception:  # whatever a learner types, the checker must answer, never raise
        return Verdict(False, "could not check this answer", unreadable=True)
    if verdict.correct and form == "simplest_surd" and not _simplest_surds(given):
        return _v(False, "equal, but the surd is not in simplest form")
    if verdict.correct and form in ("simplest_fraction", "mixed_number") and not _fraction_form(given, mixed_only=form == "mixed_number"):
        return _v(False, "equal, but not written in the required fraction form")
    if verdict.correct and form == "completed_square" and not _completed_square(given):
        return _v(False, "equal, but not written in completed-square form")
    if verdict.correct and form in ("single_fraction", "simplest_algebraic_fraction") and not _algebraic_fraction(given, simplest=form == "simplest_algebraic_fraction"):
        return _v(False, "equal, but not written in the required algebraic fraction form")
    return verdict


def _check(answer_type, expected, given, *, rounding, digits, form):
    if form == "prime_factors":
        return check_prime_factors(expected, given)
    if answer_type in JUDGE_TYPES:
        return _judge(f"{answer_type} needs a judge")
    if answer_type == "graph_reading" and not any(numbers_in(x) for x in _alts(expected)):
        norm = lambda x: re.sub(r"[^a-z0-9]", "", x.lower())
        return _v(any(norm(x) == norm(given) for x in _alts(expected)), "same label") if given.strip() else _v(False, "no answer")
    if answer_type == "graph_reading" and any(_REL.search(clean(x)) for x in _alts(expected)):
        return check_inequality(expected, given)
    if answer_type == "graph_reading" and any(_range(x) for x in _alts(expected)):
        return check_number(expected, given, rounding, digits)
    if answer_type in ("table_values", "graph_reading") and any(len(numbers_in(x)) > 1 for x in _alts(expected)):
        return check_tuple(expected, given)
    if answer_type == "standard_form":
        gv = _std_form(given)
        if gv is None:
            return Verdict(False, "could not read standard form", unreadable=True)
        mantissa = re.match(r"\s*[-+]?\s*(\d*\.?\d+)", strip_units(clean(given)))
        if not mantissa or not (1 <= Fraction(mantissa[1]) < 10):
            return _v(False, "not in standard form (the first number must be from 1 up to 10)")
    if answer_type in NUMBER_TYPES:
        if any(re.search(r"[A-Za-z]\s*=|\band\b", x) or re.search(r"\d\s*,\s*[\[\-\d(A-Za-z]", x) for x in _alts(expected)):
            return check_solutions(expected, given, rounding, digits)
        return check_number(expected, given, rounding, digits)
    if answer_type in EXPRESSION_TYPES:
        return check_expression(expected, given, form)
    if answer_type in SOLUTION_TYPES:
        return check_solutions(expected, given, rounding, digits)
    if answer_type in TUPLE_TYPES:
        if answer_type == "sequence" and not any(re.search(r"[A-Za-z]\s*=.*,", x) for x in _alts(expected)) and any(re.search(r"[A-Za-z]", x) for x in _alts(expected)):
            return check_expression(expected, given)
        return check_tuple(expected, given, matrix=(answer_type == "matrix"))
    if answer_type in SET_TYPES:
        return check_set(expected, given)
    if answer_type == "inequality":
        return check_inequality(expected, given)
    if answer_type == "time_or_date":
        return check_time(expected, given)
    return _judge(f"unknown answer type {answer_type}")
