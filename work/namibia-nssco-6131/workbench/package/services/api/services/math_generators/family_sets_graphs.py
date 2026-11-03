"""Generators for six NSSCO Mathematics lessons on sets, graphs and linear programming.

* 15801 Defining Sets and Standard Notation
* 15802 Venn Diagrams (text form: counts and listed elements, no drawing)
* 15832 Quadratic Graphs (from the equation: table values, intercepts, turning point, ranges)
* 15833 Sketching Quadratics and Estimating Gradients (text form: intercepts, turning point, chords)
* 15834 Advanced Graphs (reciprocal, cubic, exponential: values, asymptotes, exact solutions)
* 15829 Linear Programming (inequalities from words, testing points, best value; no shading)

Levels follow the question shapes in the 2020-2024 papers for these lessons without reusing
any paper's wording or numbers. Every problem is built backwards from its answer and
re-checked with exact ``Fraction`` arithmetic before it is returned. Distractors carry the
typed form of a wrong answer a learner would give after one specific, known mistake.

Anything that needs a drawn or plotted figure (shading a Venn diagram, plotting a curve,
sketching, shading a region, reading a value off a given graph) is not generated here.
"""

from __future__ import annotations

from dataclasses import dataclass
from decimal import Decimal
from fractions import Fraction
from typing import Any, Callable, Dict, List, Mapping, Sequence, Tuple

from .base import Distractor, GeneratedProblem, GeneratorError, MathGenerator, SeededRandom, Step
from .formatting import math, number_latex, polynomial_latex, quadratic_latex, square_form_latex

SETS_ID = "nssco_defining_sets_notation"
VENN_ID = "nssco_venn_diagrams"
QUAD_GRAPHS_ID = "nssco_quadratic_graphs"
SKETCH_ID = "nssco_sketching_quadratics_gradients"
ADV_ID = "nssco_advanced_graphs"
LINPROG_ID = "nssco_linear_programming"
_MAX_ATTEMPTS = 500


# --------------------------------------------------------------------------
# Shared helpers
# --------------------------------------------------------------------------


def _require(condition: bool, message: str) -> None:
    if not condition:
        raise GeneratorError(f"self-check failed: {message}")


def _t(value: Any) -> str:
    """Typed fraction or integer: ``3``, ``-7/6``."""
    value = Fraction(value)
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def _l(value: Any) -> str:
    return number_latex(Fraction(value))


def _dec(value: Any) -> str:
    """A terminating fraction as a decimal string (``0.25``), otherwise ``a/b``."""
    value = Fraction(value)
    d = value.denominator
    for p in (2, 5):
        while d % p == 0:
            d //= p
    if d != 1:
        return _t(value)
    text = format(Decimal(value.numerator) / Decimal(value.denominator), "f")
    return text.rstrip("0").rstrip(".") if "." in text else text


def _nonzero(rng: SeededRandom, low: int, high: int) -> int:
    while True:
        v = rng.randint(low, high)
        if v != 0:
            return v


def _set_l(items: Sequence[int]) -> str:
    return r"\{" + ", ".join(str(x) for x in sorted(items)) + r"\}"


def _set_t(items: Sequence[int]) -> str:
    return "{" + ", ".join(str(x) for x in sorted(items)) + "}"


def _pt_l(x: Any, y: Any) -> str:
    return f"({_l(x)}, {_l(y)})"


def _pt_t(x: Any, y: Any) -> str:
    return f"({_t(x)}, {_t(y)})"


def _poly_t(coefs: Sequence[int], var: str = "x") -> str:
    return polynomial_latex(list(coefs), var)


def _xs_math(xs: Sequence[Any], shown=str) -> str:
    """``x = -3, x = 1 and x = 4`` as math, with a real word for 'and'."""
    parts = [f"x = {shown(x)}" for x in xs]
    return math(",\\ ".join(parts[:-1]) + r"\ \text{and}\ " + parts[-1])


def _signed(c: int) -> str:
    return f"+ {c}" if c > 0 else f"- {-c}"


@dataclass
class _Built:
    skill: str
    question: str
    answer: str
    # (error code, display answer, typed answer, value key). A candidate whose key equals
    # ``correct_key`` is dropped, as is any repeated key.
    items: List[Tuple[str, str, str, Any]]
    correct_key: Any
    machine: Dict[str, Any]
    steps: List[Tuple[str, str]]
    marking: Dict[str, Any]


def _marking(answer_type: str, expected: Sequence[str], **extra: Any) -> Dict[str, Any]:
    marking: Dict[str, Any] = {"answer_type": answer_type, "expected": list(expected), "typed": expected[0]}
    marking.update(extra)
    return marking


class _FamilyGenerator(MathGenerator):
    """Shared plumbing: each level has a builder returning a :class:`_Built`."""

    builders: Mapping[int, Callable[[SeededRandom], _Built]] = {}

    def _build(self, rng: SeededRandom, seed: int, level: int) -> GeneratedProblem:
        built = self.builders[level](rng)
        notes = self.error_notes[built.skill]
        distractors: List[Distractor] = []
        seen = {built.correct_key}
        for code, display, typed, key in built.items:
            if key in seen:
                continue
            seen.add(key)
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


# ==========================================================================
# Set expressions (shared by lessons 15801 and 15802)
# ==========================================================================
# An expression is a tuple: ("set", "A"), ("not", e), ("and", e, e, ...), ("or", e, e, ...).


def _ev(e: tuple, member: Mapping[str, bool]) -> bool:
    kind = e[0]
    if kind == "set":
        return member[e[1]]
    if kind == "not":
        return not _ev(e[1], member)
    if kind == "and":
        return all(_ev(c, member) for c in e[1:])
    return any(_ev(c, member) for c in e[1:])


def _lx(e: tuple) -> str:
    kind = e[0]
    if kind == "set":
        return e[1]
    if kind == "not":
        inner = e[1]
        return inner[1] + "'" if inner[0] == "set" else f"({_lx(inner)})'"
    sym = r"\cap" if kind == "and" else r"\cup"
    parts = []
    for child in e[1:]:
        text = _lx(child)
        parts.append(f"({text})" if child[0] in ("and", "or") and child[0] != kind else text)
    return f" {sym} ".join(parts)


def _swap(e: tuple) -> tuple:
    """Exchange union and intersection everywhere."""
    if e[0] == "set":
        return e
    if e[0] == "not":
        return ("not", _swap(e[1]))
    return ("or" if e[0] == "and" else "and",) + tuple(_swap(c) for c in e[1:])


def _drop_not(e: tuple) -> tuple:
    """Forget every complement."""
    if e[0] == "set":
        return e
    if e[0] == "not":
        return _drop_not(e[1])
    return (e[0],) + tuple(_drop_not(c) for c in e[1:])


def _demorgan_wrong(e: tuple) -> tuple:
    """Complement each part but keep the same union/intersection (instead of switching it)."""
    if e[0] == "set":
        return e
    if e[0] == "not" and e[1][0] in ("and", "or"):
        return (e[1][0],) + tuple(("not", _demorgan_wrong(c)) for c in e[1][1:])
    if e[0] == "not":
        return ("not", _demorgan_wrong(e[1]))
    return (e[0],) + tuple(_demorgan_wrong(c) for c in e[1:])


def _has(e: tuple, kind: str) -> bool:
    return e[0] == kind or (e[0] != "set" and any(_has(c, kind) for c in e[1:]))


def _members(universe: Sequence[int], sets: Mapping[str, Sequence[int]]) -> Dict[int, Dict[str, bool]]:
    return {n: {name: n in s for name, s in sets.items()} for n in universe}


def _eval_set(e: tuple, universe: Sequence[int], member: Mapping[int, Mapping[str, bool]]) -> List[int]:
    return [n for n in universe if _ev(e, member[n])]


def _A(name: str) -> tuple:
    return ("set", name)


def _N(e: tuple) -> tuple:
    return ("not", e)


SETS_ERROR_NOTES: Dict[str, Dict[str, str]] = {
    "list_natural": {
        "includes_zero": "started the list at 0, although 0 is not a natural number",
        "includes_upper_limit": "included the upper limit although the question says 'less than'",
    },
    "list_multiples": {
        "includes_limit": "included the limit itself even though the numbers must be less than it",
        "missed_last": "stopped one multiple too early",
    },
    "list_primes": {
        "includes_one": "counted 1 as a prime number",
        "includes_limit": "included the limit itself even though the numbers must be less than it",
        "omits_two": "left out 2 because it is even, although it is prime",
    },
    "list_factors": {
        "prime_factors_only": "listed only the prime factors instead of all the factors",
        "missing_one_and_n": "left out 1 and the number itself",
    },
    "list_squares": {
        "includes_limit": "included the limit itself even though the numbers must be less than it",
        "missed_last": "stopped one square too early",
    },
    "set_operation_list": {
        "used_other_operation": "swapped union and intersection",
        "forgot_complement": "ignored the complement and listed the set itself",
        "complement_each_part": "took the complement of each set separately instead of the complement of the whole combination",
        "listed_one_set": "listed only one of the sets",
        "wrong_set_used": "took the complement of the other set",
    },
    "set_operation_count": {
        "used_other_operation": "swapped union and intersection",
        "forgot_complement": "ignored the complement and counted the set itself",
        "complement_each_part": "took the complement of each set separately instead of the complement of the whole combination",
        "added_counts": "added the number of elements in each set without allowing for the overlap",
        "listed_one_set": "counted the elements of only one of the sets",
        "wrong_set_used": "took the complement of the other set",
    },
    "notation_subset": {
        "reversed": "wrote the subset notation the wrong way round",
        "used_element_sign": "used the element sign for a relationship between two sets",
        "used_not_subset": "wrote that it is not a subset although all its elements are in the other set",
    },
    "notation_element": {
        "used_subset_sign": "used the subset sign for a single element",
        "used_not_element": "wrote that the element is not in the set",
        "reversed": "wrote the element sign the wrong way round",
    },
    "notation_not_element": {
        "used_element_sign": "wrote that the number is in the set when it is not",
        "used_subset_sign": "used the subset sign for a single element",
        "reversed": "wrote the element sign the wrong way round",
    },
    "set_cardinality": {
        "sum_of_elements": "added up the elements instead of counting them",
        "largest_element": "gave the largest element instead of the number of elements",
        "one_too_many": "counted one element too many",
    },
}

SETS_LEVEL_SKILLS: Dict[int, Tuple[str, ...]] = {
    1: ("list_natural", "list_multiples", "list_primes", "list_factors", "list_squares"),
    2: ("set_operation_list", "set_operation_count"),
    3: ("notation_subset", "notation_element", "notation_not_element", "set_cardinality"),
}

_PRIMES = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47)
_FACTOR_NUMBERS = (12, 16, 18, 20, 24, 28, 30, 32, 36, 40, 42, 45, 48, 50, 60, 64, 72, 80)


def _list_built(skill: str, question: str, correct: List[int], cands: Sequence[Tuple[str, List[int]]]) -> _Built:
    items = [(code, math(_set_l(s)), _set_t(s), frozenset(s)) for code, s in cands if s]
    return _Built(
        skill, question, math(_set_l(correct)), items, frozenset(correct),
        {"task": skill, "elements": sorted(correct)},
        [("List every number that fits the description", _set_t(correct))],
        _marking("set_answer", [_set_t(correct)]),
    )


def _s1_natural(rng: SeededRandom) -> _Built:
    n = rng.randint(7, 15)
    correct = list(range(1, n))
    return _list_built(
        "list_natural",
        ''.join(['The universal set ', format(math('\\xi'), ''), ' is the set of natural numbers less than ', format(n, ''), '. List all the elements of ', format(math('\\xi'), ''), '.']),
        correct,
        [("includes_zero", [0] + correct), ("includes_upper_limit", correct + [n])],
    )


def _s1_multiples(rng: SeededRandom) -> _Built:
    k = rng.randint(3, 9)
    m = rng.randint(4, 7)
    limit = k * m + (0 if rng.chance(1, 2) else rng.randint(1, k - 1))
    correct = [x for x in range(1, limit) if x % k == 0]
    cands = [("missed_last", correct[:-1])]
    if limit % k == 0:
        cands.append(("includes_limit", correct + [limit]))
    return _list_built("list_multiples", f"List all the multiples of {k} that are less than {limit}.", correct, cands)


def _s1_primes(rng: SeededRandom) -> _Built:
    limit = rng.randint(12, 30)
    if rng.chance(1, 2):
        limit = rng.choice([p for p in _PRIMES if 13 <= p <= 31])
    correct = [p for p in _PRIMES if p < limit]
    cands: List[Tuple[str, List[int]]] = [("includes_one", [1] + correct), ("omits_two", correct[1:])]
    if limit in _PRIMES:
        cands.append(("includes_limit", correct + [limit]))
    return _list_built("list_primes", f"List all the prime numbers that are less than {limit}.", correct, cands)


def _s1_factors(rng: SeededRandom) -> _Built:
    n = rng.choice(_FACTOR_NUMBERS)
    correct = [d for d in range(1, n + 1) if n % d == 0]
    primes = [d for d in correct if d > 1 and all(d % q for q in range(2, d))]
    return _list_built(
        "list_factors", f"List all the factors of {n}.", correct,
        [("prime_factors_only", primes), ("missing_one_and_n", correct[1:-1])],
    )


def _s1_squares(rng: SeededRandom) -> _Built:
    root = rng.randint(4, 8)
    limit = root * root + (0 if rng.chance(1, 2) else rng.randint(1, root))
    correct = [i * i for i in range(1, root + 1) if i * i < limit]
    cands = [("missed_last", correct[:-1])]
    if limit == root * root:
        cands.append(("includes_limit", correct + [limit]))
    return _list_built("list_squares", f"List all the square numbers that are less than {limit}.", correct, cands)


def _sets_level1(rng: SeededRandom) -> _Built:
    return rng.choice((_s1_natural, _s1_multiples, _s1_primes, _s1_factors, _s1_squares))(rng)


# Expressions for two sets. (expression, listed-as-sets alternatives built from transforms)
_TWO_SET_EXPRS: Tuple[tuple, ...] = (
    ("or", _A("A"), _A("B")),
    ("and", _A("A"), _A("B")),
    _N(_A("A")),
    _N(_A("B")),
    _N(("or", _A("A"), _A("B"))),
    _N(("and", _A("A"), _A("B"))),
    ("and", _A("A"), _N(_A("B"))),
    ("and", _N(_A("A")), _A("B")),
)


def _set_distractor_candidates(e: tuple, member, universe, names: Sequence[str]) -> List[Tuple[str, tuple]]:
    cands: List[Tuple[str, tuple]] = []
    if _has(e, "and") or _has(e, "or"):
        cands.append(("used_other_operation", _swap(e)))
    if _has(e, "not"):
        cands.append(("forgot_complement", _drop_not(e)))
        if e[0] == "not" and e[1][0] in ("and", "or"):
            cands.append(("complement_each_part", _demorgan_wrong(e)))
    if e[0] == "not" and e[1][0] == "set":
        other = [n for n in names if n != e[1][1]]
        if other:
            cands.append(("wrong_set_used", _N(_A(other[0]))))
    elif e[0] != "set" and e[0] != "not":
        cands.append(("listed_one_set", _A(names[0])))
    return cands


def _build_set_operation(rng: SeededRandom, names: Sequence[str], exprs: Sequence[tuple], universe_size: int, sizes: Tuple[int, int]) -> _Built:
    for _ in range(_MAX_ATTEMPTS):
        n = universe_size
        universe = list(range(1, n + 1))
        sets = {nm: _subset(rng, universe, rng.randint(*sizes)) for nm in names}
        member = _members(universe, sets)
        e = rng.choice(exprs)
        answer = _eval_set(e, universe, member)
        if not answer or len(answer) == len(universe):
            continue
        count = rng.chance(1, 3)
        # every set must have an element in and out of the union so the diagram is not degenerate
        if any(not s or len(s) == n for s in sets.values()):
            continue
        cands = _set_distractor_candidates(e, member, universe, names)
        header = r"\xi = " + _set_l(universe) + ", " + ", ".join(f"{nm} = {_set_l(sets[nm])}" for nm in names)
        if count:
            question = f"{math(header)}. Find {math('n(' + _lx(e) + ')')}."
            correct = len(answer)
            items = [(code, math(str(len(_eval_set(c, universe, member)))), str(len(_eval_set(c, universe, member))), len(_eval_set(c, universe, member))) for code, c in cands]
            if e[0] == "or" and len(e) == 3:
                total = len(sets[names[0]]) + len(sets[names[1]])
                items.append(("added_counts", math(str(total)), str(total), total))
            return _Built(
                "set_operation_count", question, math(str(correct)), items, correct,
                {"task": "set_count", "expression": _lx(e), "sets": {k: sorted(v) for k, v in sets.items()}},
                [("List the elements that fit", _set_t(answer)), ("Count them", str(correct))],
                _marking("number_exact", [str(correct)]),
            )
        question = f"{math(header)}. List the elements of {math(_lx(e))}."
        items = []
        for code, c in cands:
            alt = _eval_set(c, universe, member)
            if alt:
                items.append((code, math(_set_l(alt)), _set_t(alt), frozenset(alt)))
        return _Built(
            "set_operation_list", question, math(_set_l(answer)), items, frozenset(answer),
            {"task": "set_list", "expression": _lx(e), "sets": {k: sorted(v) for k, v in sets.items()}},
            [("Find the elements that fit", _set_t(answer))],
            _marking("set_answer", [_set_t(answer)]),
        )
    raise GeneratorError("set operation problem not found")


def _subset(rng: SeededRandom, universe: Sequence[int], size: int) -> List[int]:
    pool = list(universe)
    out = []
    for _ in range(size):
        out.append(pool.pop(rng.randbelow(len(pool))))
    return sorted(out)


def _sets_level2(rng: SeededRandom) -> _Built:
    return _build_set_operation(rng, ("A", "B"), _TWO_SET_EXPRS, rng.randint(10, 14), (4, 7))


_SET_NAME_PAIRS = (("A", "B"), ("P", "Q"), ("C", "D"), ("E", "W"), ("S", "T"), ("M", "N"))


def _sets_level3(rng: SeededRandom) -> _Built:
    kind = rng.choice(("subset", "element", "not_element", "cardinality"))
    x_name, y_name = rng.choice(_SET_NAME_PAIRS)
    universe = list(range(1, 21))
    big = _subset(rng, universe, rng.randint(5, 8))
    if kind == "subset":
        small = _subset(rng, big, rng.randint(2, 4))
        _require(set(small) < set(big), "subset must be proper")
        q = (f"{math(f'{x_name} = ' + _set_l(small))} and {math(f'{y_name} = ' + _set_l(big))}. "
             f"Write down, using set notation, the relationship between {math(x_name)} and {math(y_name)}.")
        ans = f"{x_name} ⊂ {y_name}"
        marking = _marking("set_answer", [ans, f"{x_name} ⊆ {y_name}"])
        cands = [
            ("reversed", f"{y_name} ⊂ {x_name}"),
            ("used_element_sign", f"{x_name} ∈ {y_name}"),
            ("used_not_subset", f"{x_name} ⊄ {y_name}"),
        ]
        skill = "notation_subset"
        steps = [("Every element of the first set is in the second", ans)]
        machine = {"task": "notation", "relation": "subset"}
    elif kind == "element":
        k = rng.choice(big)
        q = (f"{math(f'{y_name} = ' + _set_l(big))}. Use set notation to write the statement "
             f"\"{k} is an element of {y_name}\".")
        ans = f"{k} ∈ {y_name}"
        marking = _marking("set_answer", [ans])
        cands = [("used_subset_sign", f"{k} ⊂ {y_name}"), ("used_not_element", f"{k} ∉ {y_name}"), ("reversed", f"{y_name} ∈ {k}")]
        skill = "notation_element"
        steps = [("Use the element sign for a single member", ans)]
        machine = {"task": "notation", "relation": "element"}
    elif kind == "not_element":
        k = rng.choice([n for n in universe if n not in big])
        q = (f"{math(f'{y_name} = ' + _set_l(big))}. Use set notation to write the statement "
             f"\"{k} is not an element of {y_name}\".")
        ans = f"{k} ∉ {y_name}"
        marking = _marking("set_answer", [ans])
        cands = [("used_element_sign", f"{k} ∈ {y_name}"), ("used_subset_sign", f"{k} ⊄ {y_name}"), ("reversed", f"{y_name} ∉ {k}")]
        skill = "notation_not_element"
        steps = [("Use the not-an-element sign", ans)]
        machine = {"task": "notation", "relation": "not_element"}
    else:
        q = f"{math(f'{y_name} = ' + _set_l(big))}. Write down {math(f'n({y_name})')}."
        n = len(big)
        return _Built(
            "set_cardinality", q, math(str(n)),
            [("sum_of_elements", math(str(sum(big))), str(sum(big)), sum(big)),
             ("largest_element", math(str(max(big))), str(max(big)), max(big)),
             ("one_too_many", math(str(n + 1)), str(n + 1), n + 1)],
            n, {"task": "cardinality", "elements": big},
            [("Count the elements", str(n))], _marking("number_exact", [str(n)]),
        )
    items = [(code, math(text.replace("⊄", r"\not\subset").replace("⊂", r"\subset").replace("⊆", r"\subseteq").replace("∈", r"\in").replace("∉", r"\notin")), text, text) for code, text in cands]
    ans_l = math(ans.replace("⊄", r"\not\subset").replace("⊂", r"\subset").replace("∈", r"\in").replace("∉", r"\notin"))
    return _Built(skill, q, ans_l, items, ans, machine, steps, marking)


class SetsNotationGenerator(_FamilyGenerator):
    generator_id = SETS_ID
    version = 1
    levels = (1, 2, 3)
    level_skills = SETS_LEVEL_SKILLS
    error_notes = SETS_ERROR_NOTES
    builders = {1: _sets_level1, 2: _sets_level2, 3: _sets_level3}


# ==========================================================================
# Lesson 15802: Venn Diagrams (text form)
# ==========================================================================

VENN_ERROR_NOTES: Dict[str, Dict[str, str]] = {
    "venn_two_set_count": {
        "overlap_not_removed": "added the two set totals without taking off the learners counted twice",
        "total_used": "gave the whole class instead of the group asked for",
        "forgot_to_subtract_both": "subtracted only the overlap from the whole class",
        "other_set_used": "used the other set's total",
    },
    "venn_find_both": {
        "forgot_neither": "ignored the learners who study neither subject",
        "totals_added": "added the two subject totals and stopped",
        "difference": "subtracted one subject total from the other",
        "forgot_to_subtract": "found the number studying both but forgot to take it off the subject total for 'only'",
    },
    "venn_three_set_list": {
        "used_other_operation": "swapped union and intersection",
        "forgot_complement": "ignored the complement and listed the set itself",
        "complement_each_part": "took the complement of each set separately instead of the complement of the whole combination",
        "listed_one_set": "listed only one of the sets",
        "wrong_set_used": "took the complement of the other set",
    },
    "venn_probability": {
        "wrong_denominator": "divided by the size of the group instead of the whole class",
        "overlap_counted_twice": "counted the overlap in both circles",
        "count_only": "gave the number of learners instead of a probability",
        "inverted": "put the total on top and the group underneath",
    },
}

VENN_LEVEL_SKILLS: Dict[int, Tuple[str, ...]] = {
    1: ("venn_two_set_count",),
    2: ("venn_find_both",),
    3: ("venn_three_set_list",),
    4: ("venn_probability",),
}

_SUBJECT_PAIRS = (
    ("Biology", "Physics"), ("History", "Geography"), ("Afrikaans", "German"),
    ("Agriculture", "Business Studies"), ("Accounting", "Economics"), ("Art", "Music"),
)


def _venn_counts(rng: SeededRandom) -> Tuple[int, int, int, int]:
    return rng.randint(3, 10), rng.randint(4, 14), rng.randint(4, 14), rng.randint(2, 10)  # both, only A, only B, neither


def _venn1(rng: SeededRandom) -> _Built:
    both, a, b, d = _venn_counts(rng)
    sa, sb = rng.choice(_SUBJECT_PAIRS)
    total, n_a, n_b = a + b + both + d, a + both, b + both
    ask = rng.choice(("union", "only_a", "neither", "not_b"))
    stem = (f"In a class of {total} learners, {n_a} study {sa} and {n_b} study {sb}. "
            f"{both} learners study both {sa} and {sb}.")
    if ask == "union":
        q, ans, items = f"{stem} Find the number of learners who study {sa} or {sb} or both.", a + b + both, [
            ("overlap_not_removed", n_a + n_b), ("total_used", total), ("other_set_used", n_b)]
    elif ask == "only_a":
        q, ans, items = f"{stem} Find the number of learners who study {sa} only.", a, [
            ("overlap_not_removed", n_a), ("other_set_used", b), ("forgot_to_subtract_both", total - both)]
    elif ask == "neither":
        q, ans, items = f"{stem} Find the number of learners who study neither subject.", d, [
            ("overlap_not_removed", total - n_a - n_b), ("total_used", total - n_a), ("forgot_to_subtract_both", total - both)]
    else:
        q, ans, items = f"{stem} Find the number of learners who do not study {sb}.", a + d, [
            ("total_used", total), ("other_set_used", n_a), ("overlap_not_removed", total - b)]
    return _Built(
        "venn_two_set_count", q, math(str(ans)), [(c, math(str(v)), str(v), v) for c, v in items], ans,
        {"task": "two_set_count", "both": both, "only_a": a, "only_b": b, "neither": d, "ask": ask},
        [("Work out the learners in each region", f"only {sa} {a}, both {both}, only {sb} {b}, neither {d}"), ("Read off the group asked for", str(ans))],
        _marking("number_exact", [str(ans)]),
    )


def _venn2(rng: SeededRandom) -> _Built:
    both, a, b, d = _venn_counts(rng)
    sa, sb = rng.choice(_SUBJECT_PAIRS)
    total, n_a, n_b = a + b + both + d, a + both, b + both
    stem = f"{total} learners were asked about {sa} and {sb}. {n_a} study {sa}, {n_b} study {sb} and {d} study neither."
    if rng.chance(1, 2):
        q, ans = f"{stem} Find the number who study both subjects.", both
        items = [("forgot_neither", n_a + n_b - total), ("totals_added", n_a + n_b), ("difference", abs(n_a - n_b))]
        steps = [("Learners studying at least one subject", str(total - d)), ("Add the totals and take away that number", str(both))]
    else:
        q, ans = f"{stem} Find the number who study {sb} only.", b
        items = [("forgot_to_subtract", n_b), ("forgot_neither", n_b - (n_a + n_b - total)), ("difference", abs(n_a - n_b))]
        steps = [("Number studying both", str(both)), (f"Take it off the {sb} total", str(b))]
    _require(both >= 1 and total - d == a + b + both, "venn totals")
    return _Built(
        "venn_find_both", q, math(str(ans)), [(c, math(str(v)), str(v), v) for c, v in items], ans,
        {"task": "find_both", "both": both, "only_a": a, "only_b": b, "neither": d}, steps,
        _marking("number_exact", [str(ans)]),
    )


_THREE_SET_EXPRS: Tuple[tuple, ...] = (
    _N(_A("C")),
    ("and", _A("A"), _A("B"), _A("C")),
    ("or", _A("A"), _A("B")),
    ("and", _N(("or", _A("A"), _A("C"))), _A("B")),
    ("and", _A("A"), _N(_A("C"))),
    ("or", ("and", _A("A"), _A("B")), _A("C")),
    ("and", _A("B"), _N(("and", _A("A"), _A("C")))),
    _N(("or", _A("A"), _A("B"), _A("C"))),
)


def _venn3(rng: SeededRandom) -> _Built:
    for _ in range(_MAX_ATTEMPTS):
        universe = list(range(1, rng.randint(12, 15) + 1))
        sets = {nm: _subset(rng, universe, rng.randint(4, 8)) for nm in "ABC"}
        member = _members(universe, sets)
        e = rng.choice(_THREE_SET_EXPRS)
        answer = _eval_set(e, universe, member)
        if not answer or len(answer) == len(universe):
            continue
        cands = _set_distractor_candidates(e, member, universe, "ABC")
        items = []
        for code, c in cands:
            alt = _eval_set(c, universe, member)
            if alt:
                items.append((code, math(_set_l(alt)), _set_t(alt), frozenset(alt)))
        header = r"\xi = " + _set_l(universe) + ", " + ", ".join(f"{nm} = {_set_l(sets[nm])}" for nm in "ABC")
        q = f"{math(header)}. List the elements of {math(_lx(e))}."
        return _Built(
            "venn_three_set_list", q, math(_set_l(answer)), items, frozenset(answer),
            {"task": "three_set_list", "expression": _lx(e), "sets": {k: sorted(v) for k, v in sets.items()}},
            [("Check each element of the universal set against the expression", _set_t(answer))],
            _marking("set_answer", [_set_t(answer)]),
        )
    raise GeneratorError("three-set problem not found")


def _venn4(rng: SeededRandom) -> _Built:
    both, a, b, d = _venn_counts(rng)
    sa, sb = rng.choice(_SUBJECT_PAIRS)
    total, n_a, n_b = a + b + both + d, a + both, b + both
    ask = rng.choice(("only_a", "neither", "both", "sb"))
    stem = (f"In a class of {total} learners, {n_a} study {sa}, {n_b} study {sb} and {both} study both subjects. "
            f"A learner is chosen at random.")
    if ask == "only_a":
        q, num, items = f"{stem} Find the probability that the learner studies {sa} only.", a, [
            ("wrong_denominator", Fraction(a, n_a)), ("overlap_counted_twice", Fraction(n_a, total)), ("count_only", Fraction(a)), ("inverted", Fraction(total, a))]
    elif ask == "neither":
        q, num, items = f"{stem} Find the probability that the learner studies neither subject.", d, [
            ("wrong_denominator", Fraction(d, total - d)), ("overlap_counted_twice", Fraction(d + both, total)), ("count_only", Fraction(d)), ("inverted", Fraction(total, d))]
    elif ask == "both":
        q, num, items = f"{stem} Find the probability that the learner studies both subjects.", both, [
            ("wrong_denominator", Fraction(both, n_a)), ("overlap_counted_twice", Fraction(2 * both, total)), ("count_only", Fraction(both)), ("inverted", Fraction(total, both))]
    else:
        q, num, items = f"{stem} Find the probability that the learner studies {sb}.", n_b, [
            ("wrong_denominator", Fraction(n_b, n_a + n_b)), ("overlap_counted_twice", Fraction(b, total)), ("count_only", Fraction(n_b)), ("inverted", Fraction(total, n_b))]
    ans = Fraction(num, total)
    return _Built(
        "venn_probability", q, math(_l(ans)), [(c, math(_l(v)), _t(v), v) for c, v in items], ans,
        {"task": "venn_probability", "both": both, "only_a": a, "only_b": b, "neither": d, "ask": ask},
        [("Learners in the group asked for", str(num)), ("Divide by the whole class", _t(ans))],
        _marking("number_exact", [_t(ans)]),
    )


class VennDiagramsGenerator(_FamilyGenerator):
    generator_id = VENN_ID
    version = 1
    levels = (1, 2, 3, 4)
    level_skills = VENN_LEVEL_SKILLS
    error_notes = VENN_ERROR_NOTES
    builders = {1: _venn1, 2: _venn2, 3: _venn3, 4: _venn4}


# ==========================================================================
# Lesson 15832: Quadratic Graphs (from the equation)
# ==========================================================================

QUAD_ERROR_NOTES: Dict[str, Dict[str, str]] = {
    "quad_table_values": {
        "negative_square": "squared a negative x-value and kept the minus sign",
        "negative_linear_sign": "ignored the sign of a negative x-value in the x term",
        "sign_of_x_term": "used the opposite sign for the x term",
    },
    "quad_y_intercept": {
        "coordinates_swapped": "wrote the intercept with the x and y values the wrong way round",
        "x_coefficient_used": "used the coefficient of x instead of the constant term",
        "sign_error": "gave the constant term with the wrong sign",
    },
    "quad_other_root": {
        "sign_error": "gave the other x-intercept with the wrong sign",
        "coordinates_swapped": "wrote the intercept with the x and y values the wrong way round",
        "same_root": "repeated the x-intercept that was already given",
    },
    "quad_turning_point": {
        "sign_of_x": "gave the x-coordinate with the wrong sign",
        "intercept_used_for_y": "used the y-intercept as the y-coordinate of the turning point",
        "coordinates_swapped": "wrote the coordinates the wrong way round",
    },
    "quad_axis_of_symmetry": {
        "sign_of_x": "gave the line with the wrong sign",
        "constant_used": "used the constant term as the line of symmetry",
        "y_value_used": "gave the y-coordinate of the turning point as the line of symmetry",
    },
    "quad_extreme_value": {
        "intercept_used": "gave the y-intercept as the greatest or least value",
        "sign_error": "gave the right size of value with the wrong sign",
        "x_value_used": "gave the x-coordinate of the turning point instead of the y-value",
    },
    "quad_solve_f_equals_g": {
        "sign_error": "gave both solutions with the wrong sign",
        "one_root_only": "found only one of the two solutions",
        "solved_f_only": "solved f(x) = 0 instead of f(x) = g(x)",
    },
    "quad_range_of_x": {
        "wrong_region": "gave the region the wrong way round (inside instead of outside, or the reverse)",
        "includes_ends": "included the end values although the inequality is strict",
        "sign_error": "gave the end values with the wrong sign",
    },
}

QUAD_LEVEL_SKILLS: Dict[int, Tuple[str, ...]] = {
    1: ("quad_table_values",),
    2: ("quad_y_intercept", "quad_other_root"),
    3: ("quad_turning_point", "quad_axis_of_symmetry", "quad_extreme_value"),
    4: ("quad_solve_f_equals_g", "quad_range_of_x"),
}


def _y_expr(a: int, b: int, c: int) -> str:
    return quadratic_latex(a, b, c)


def _list_typed(values: Sequence[Any]) -> str:
    return ", ".join(_t(v) for v in values)


def _list_display(values: Sequence[Any]) -> str:
    return ", ".join(_l(v) for v in values)


def _quad1(rng: SeededRandom) -> _Built:
    for _ in range(_MAX_ATTEMPTS):
        r1, r2 = rng.randint(-4, 4), rng.randint(-4, 4)
        a = 1
        b, c = -(r1 + r2), r1 * r2
        if r1 == r2 or b == 0 or c == 0:
            continue
        xs = sorted(rng.randint(-3, 4) for _ in range(3))
        if len(set(xs)) < 3 or min(xs) >= 0:
            continue
        f = lambda x: a * x * x + b * x + c
        correct = [f(x) for x in xs]
        negsq = [(-(x * x) if x < 0 else x * x) + b * x + c for x in xs]
        negsign = [x * x + b * abs(x) + c for x in xs]
        flipb = [x * x - b * x + c for x in xs]
        items = [
            ("negative_square", negsq), ("negative_linear_sign", negsign), ("sign_of_x_term", flipb),
        ]
        q = (f"A table of values is needed for {math('y = ' + _y_expr(a, b, c))}. "
             f"Find the value of {math('y')} when {_xs_math(xs)}.")
        steps = [(f"Substitute x = {x}", str(v)) for x, v in zip(xs, correct)]
        return _Built(
            "quad_table_values", q, math(_list_display(correct)),
            [(code, math(_list_display(v)), _list_typed(v), tuple(v)) for code, v in items], tuple(correct),
            {"task": "table_values", "quadratic": [a, b, c], "x": xs}, steps,
            _marking("table_values", [_list_typed(correct)]),
        )
    raise GeneratorError("level 1 not found")


def _roots_quadratic(rng: SeededRandom, a_choices: Sequence[int] = (1, -1)) -> Tuple[int, int, int, int, int]:
    for _ in range(_MAX_ATTEMPTS):
        a = rng.choice(a_choices)
        r1, r2 = rng.randint(-6, 5), rng.randint(-6, 5)
        if r1 == r2 or r1 == 0 or r2 == 0:
            continue
        b, c = -a * (r1 + r2), a * r1 * r2
        if b == 0:
            continue
        return a, b, c, r1, r2
    raise GeneratorError("no quadratic found")


def _quad2(rng: SeededRandom) -> _Built:
    a, b, c, r1, r2 = _roots_quadratic(rng)
    expr = _y_expr(a, b, c)
    if rng.chance(1, 2):
        q = f"Write down the {math('y')}-intercept of {math('f(x) = ' + expr)}."
        ans = (0, c)
        items = [
            ("coordinates_swapped", (c, 0)), ("x_coefficient_used", (0, b)), ("sign_error", (0, -c)),
        ]
        return _Built(
            "quad_y_intercept", q, math(_pt_l(*ans)),
            [(code, math(_pt_l(*v)), _pt_t(*v), v) for code, v in items], ans,
            {"task": "y_intercept", "quadratic": [a, b, c]},
            [("Put x = 0", str(c))], _marking("coordinates", [_pt_t(*ans)]),
        )
    known, other = (r1, r2) if rng.chance(1, 2) else (r2, r1)
    q = (f"The graph of {math('f(x) = ' + expr)} crosses the {math('x')}-axis at {math(_pt_l(known, 0))} and at one other point. "
         f"Write down the coordinates of the other point.")
    ans = (other, 0)
    items = [("sign_error", (-other, 0)), ("coordinates_swapped", (0, other)), ("same_root", (known, 0))]
    return _Built(
        "quad_other_root", q, math(_pt_l(*ans)),
        [(code, math(_pt_l(*v)), _pt_t(*v), v) for code, v in items], ans,
        {"task": "other_root", "quadratic": [a, b, c], "given_root": known},
        [("Factorise or use the sum of the roots", f"roots {known} and {other}"), ("The other point is on the x-axis", _pt_t(*ans))],
        _marking("coordinates", [_pt_t(*ans)]),
    )


def _quad3(rng: SeededRandom) -> _Built:
    for _ in range(_MAX_ATTEMPTS):
        a = rng.choice((1, 1, -1))
        t = _nonzero(rng, -5, 5)
        w = rng.randint(1, 5)
        b, c = -2 * a * t, a * (t * t - w * w)
        y_t = -a * w * w
        if b == 0 or c == 0 or y_t == c:
            continue
        break
    else:
        raise GeneratorError("level 3 not found")
    expr = _y_expr(a, b, c)
    kind = rng.choice(("turning_point", "axis", "extreme"))
    shape = "minimum" if a > 0 else "maximum"
    if kind == "turning_point":
        q = f"Find the coordinates of the turning point of {math('y = ' + expr)}."
        ans = (t, y_t)
        items = [("sign_of_x", (-t, y_t)), ("intercept_used_for_y", (t, c)), ("coordinates_swapped", (y_t, t))]
        return _Built(
            "quad_turning_point", q, math(_pt_l(*ans)),
            [(code, math(_pt_l(*v)), _pt_t(*v), v) for code, v in items], ans,
            {"task": "turning_point", "quadratic": [a, b, c]},
            [("Complete the square or use x = -b/2a", f"x = {t}"), ("Substitute to find y", str(y_t))],
            _marking("coordinates", [_pt_t(*ans)]),
        )
    if kind == "axis":
        q = f"Write down the equation of the line of symmetry of the graph of {math('y = ' + expr)}."
        ans_text = f"x = {t}"
        items = [("sign_of_x", f"x = {-t}"), ("constant_used", f"x = {c}"), ("y_value_used", f"x = {y_t}")]
        return _Built(
            "quad_axis_of_symmetry", q, math(ans_text),
            [(code, math(text), text, text) for code, text in items], ans_text,
            {"task": "axis_of_symmetry", "quadratic": [a, b, c]},
            [("Line of symmetry through the turning point", ans_text)],
            _marking("equation_solution", [ans_text]),
        )
    q = f"Write down the {shape} value of {math('y')} for {math('y = ' + expr)}."
    items = [("intercept_used", c), ("sign_error", -y_t), ("x_value_used", t)]
    return _Built(
        "quad_extreme_value", q, math(str(y_t)),
        [(code, math(str(v)), str(v), v) for code, v in items], y_t,
        {"task": "extreme_value", "quadratic": [a, b, c], "kind": shape},
        [("Turning point", _pt_t(t, y_t)), ("Its y-value", str(y_t))],
        _marking("number_exact", [str(y_t)]),
    )


def _quad4(rng: SeededRandom) -> _Built:
    if rng.chance(1, 2):
        for _ in range(_MAX_ATTEMPTS):
            x1, x2 = rng.randint(-4, 4), rng.randint(-4, 4)
            b, c = rng.randint(-4, 4), rng.randint(-6, 6)
            m, n = b + x1 + x2, c - x1 * x2
            if x1 >= x2 or b == 0 or c == 0 or m == 0 or abs(m) > 9 or abs(n) > 12 or n == 0:
                continue
            roots_f = [r for r in range(-12, 13) if r * r + b * r + c == 0]
            break
        else:
            raise GeneratorError("level 4 solve not found")
        f_expr, g_expr = _y_expr(1, b, c), polynomial_latex([m, n])
        q = (f"{math('f(x) = ' + f_expr)} and {math('g(x) = ' + g_expr)}. Solve {math('f(x) = g(x)')}.")
        ans_text = f"x = {x1} or x = {x2}"
        items = [
            ("sign_error", f"x = {-x1} or x = {-x2}", frozenset((-x1, -x2))),
            ("one_root_only", f"x = {x1}", frozenset((x1,))),
        ]
        if len(roots_f) == 2 and frozenset(roots_f) != frozenset((x1, x2)):
            items.append(("solved_f_only", f"x = {roots_f[0]} or x = {roots_f[1]}", frozenset(roots_f)))
        return _Built(
            "quad_solve_f_equals_g", q, math(f"x = {x1}\\ \\text{{or}}\\ x = {x2}"),
            [(code, math(text.replace(" or ", r"\ \text{or}\ ")), text, key) for code, text, key in items], frozenset((x1, x2)),
            {"task": "solve_f_equals_g", "f": [1, b, c], "g": [m, n]},
            [("Set the two expressions equal and collect", f"{polynomial_latex([1, b - m, c - n])} = 0"), ("Factorise and solve", ans_text)],
            _marking("equation_solution", [ans_text]),
        )
    r1, r2 = sorted((_nonzero(rng, -5, 5), _nonzero(rng, -5, 5)))
    while r1 == r2:
        r1, r2 = sorted((_nonzero(rng, -5, 5), _nonzero(rng, -5, 5)))
    b, c = -(r1 + r2), r1 * r2
    expr = _y_expr(1, b, c)
    below = rng.chance(1, 2)
    if below:
        ans_text = f"{r1} < x < {r2}"
        items = [
            ("wrong_region", f"x < {r1} or x > {r2}", ("out", r1, r2)),
            ("includes_ends", f"{r1} <= x <= {r2}", ("closed_in", r1, r2)),
            ("sign_error", f"{-r2} < x < {-r1}", ("in", -r2, -r1)),
        ]
        correct_key = ("in", r1, r2)
        sign = "<"
    else:
        ans_text = f"x < {r1} or x > {r2}"
        items = [
            ("wrong_region", f"{r1} < x < {r2}", ("in", r1, r2)),
            ("includes_ends", f"x <= {r1} or x >= {r2}", ("closed_out", r1, r2)),
            ("sign_error", f"x < {-r2} or x > {-r1}", ("out", -r2, -r1)),
        ]
        correct_key = ("out", r1, r2)
        sign = ">"
    q = f"Find the range of values of {math('x')} for which {math('f(x) ' + sign + ' 0')}, where {math('f(x) = ' + expr)}."

    def latex(text: str) -> str:
        return math(text.replace("<=", r"\le").replace(">=", r"\ge").replace(" or ", r"\ \text{or}\ "))

    return _Built(
        "quad_range_of_x", q, latex(ans_text),
        [(code, latex(text), text, key) for code, text, key in items], correct_key,
        {"task": "range_of_x", "quadratic": [1, b, c], "sign": sign},
        [("Roots of f(x) = 0", f"x = {r1} or x = {r2}"), ("Choose the region where f(x) is " + ("negative" if below else "positive"), ans_text)],
        _marking("inequality", [ans_text]),
    )


class QuadraticGraphsGenerator(_FamilyGenerator):
    generator_id = QUAD_GRAPHS_ID
    version = 1
    levels = (1, 2, 3, 4)
    level_skills = QUAD_LEVEL_SKILLS
    error_notes = QUAD_ERROR_NOTES
    builders = {1: _quad1, 2: _quad2, 3: _quad3, 4: _quad4}


# ==========================================================================
# Lesson 15833: Sketching Quadratics and Estimating Gradients (text form)
# ==========================================================================

SKETCH_ERROR_NOTES: Dict[str, Dict[str, str]] = {
    "sketch_x_intercepts": {
        "sign_error": "gave the x-values with the wrong sign",
        "coordinates_swapped": "wrote the points with the x and y values the wrong way round",
        "factor_not_divided": "did not divide by the coefficient of x in a bracket like (2x + 1)",
    },
    "sketch_y_intercept": {
        "coordinates_swapped": "wrote the intercept with the x and y values the wrong way round",
        "sign_error": "gave the constant term with the wrong sign",
        "x_coefficient_used": "used the coefficient of x instead of the constant term",
    },
    "sketch_square_form": {
        "sign_of_x": "gave the x-coordinate with the wrong sign",
        "coordinates_swapped": "wrote the coordinates the wrong way round",
        "sign_of_y": "gave the y-coordinate with the wrong sign",
    },
    "sketch_turning_point": {
        "sign_of_x": "used x = b/2a instead of x = -b/2a",
        "forgot_two": "used x = -b/a and forgot the 2 in the denominator",
        "intercept_used_for_y": "used the y-intercept as the y-coordinate of the turning point",
        "forgot_to_divide_by_4a": "worked out the y-coordinate without dividing by the right amount",
    },
    "sketch_chord_gradient": {
        "rise_only": "gave the difference in y-values without dividing by the difference in x-values",
        "sign_reversed": "subtracted the values in the opposite order for the top and bottom",
        "inverted": "divided the change in x by the change in y",
    },
    "sketch_turning_gradient": {
        "gradient_of_chord": "worked out a chord gradient instead of recognising that the tangent at a turning point is flat",
        "y_value_used": "gave the y-coordinate of the turning point as the gradient",
        "x_value_used": "gave the x-coordinate of the turning point as the gradient",
    },
}

SKETCH_LEVEL_SKILLS: Dict[int, Tuple[str, ...]] = {
    1: ("sketch_x_intercepts", "sketch_y_intercept"),
    2: ("sketch_square_form",),
    3: ("sketch_turning_point",),
    4: ("sketch_chord_gradient", "sketch_turning_gradient"),
}


def _factored_quadratic(rng: SeededRandom) -> Tuple[int, int, int, Fraction, Fraction, Tuple[int, int, int, int]]:
    """Return (a, b, c, root1, root2, (m, p, n, q)) for (mx + p)(nx + q) possibly with a leading -1."""
    for _ in range(_MAX_ATTEMPTS):
        kind = rng.choice(("monic", "monic", "negative", "two"))
        if kind == "two":
            m, n, sign = 2, 1, 1
            p, q = rng.choice((1, 3, 5, -1, -3, -5)), _nonzero(rng, -5, 5)
        else:
            m, n, sign = 1, 1, (1 if kind == "monic" else -1)
            p, q = _nonzero(rng, -7, 7), _nonzero(rng, -7, 7)
        r1, r2 = Fraction(-p, m), Fraction(-q, n)
        if r1 == r2:
            continue
        a, b, c = sign * m * n, sign * (m * q + n * p), sign * p * q
        if b == 0:
            continue
        return a, b, c, r1, r2, (sign * m, p, n, q)
    raise GeneratorError("no factored quadratic found")


def _sketch1(rng: SeededRandom) -> _Built:
    a, b, c, r1, r2, (m, p, n, q) = _factored_quadratic(rng)
    expr = quadratic_latex(a, b, c)
    lo, hi = sorted((r1, r2))
    if rng.chance(1, 3):
        q_text = f"The curve {math('y = ' + expr)} crosses the {math('y')}-axis. Find the coordinates of the point where it does so."
        ans = (0, c)
        items = [("coordinates_swapped", (c, 0)), ("sign_error", (0, -c)), ("x_coefficient_used", (0, b))]
        return _Built(
            "sketch_y_intercept", q_text, math(_pt_l(*ans)),
            [(code, math(_pt_l(*v)), _pt_t(*v), v) for code, v in items], ans,
            {"task": "y_intercept", "quadratic": [a, b, c]}, [("Put x = 0", str(c))],
            _marking("coordinates", [_pt_t(*ans)]),
        )
    q_text = (f"The curve {math('y = ' + expr)} crosses the {math('x')}-axis at two points. "
              f"Find the coordinates of both points, giving the one with the smaller {math('x')}-value first.")
    ans_text = f"({_t(lo)}, 0), ({_t(hi)}, 0)"
    display = f"{_pt_l(lo, 0)}\\ \\text{{and}}\\ {_pt_l(hi, 0)}"
    items = [
        ("sign_error", sorted((-lo, -hi))),
        ("coordinates_swapped", None),
        ("factor_not_divided", sorted((Fraction(-p), Fraction(-q)))),
    ]
    out_items = []
    for code, v in items:
        if code == "coordinates_swapped":
            typed = f"(0, {_t(lo)}), (0, {_t(hi)})"
            out_items.append((code, math(f"{_pt_l(0, lo)}\\ \\text{{and}}\\ {_pt_l(0, hi)}"), typed, ("swap", lo, hi)))
        else:
            if code == "factor_not_divided" and m != 1 and abs(m) == 2 or code != "factor_not_divided":
                x1, x2 = v
                out_items.append((code, math(f"{_pt_l(x1, 0)}\\ \\text{{and}}\\ {_pt_l(x2, 0)}"), f"({_t(x1)}, 0), ({_t(x2)}, 0)", (x1, x2)))
    reversed_text = f"({_t(hi)}, 0), ({_t(lo)}, 0)"
    marking = _marking("coordinates", [ans_text, reversed_text])
    return _Built(
        "sketch_x_intercepts", q_text, math(display), out_items, (lo, hi),
        {"task": "x_intercepts", "quadratic": [a, b, c]},
        [("Factorise and put y = 0", f"x = {_t(lo)} or x = {_t(hi)}"), ("Write them as points on the x-axis", ans_text)],
        marking,
    )


def _sketch2(rng: SeededRandom) -> _Built:
    a = rng.choice((1, 1, 2, -1, 3))
    P = _nonzero(rng, -6, 6)
    qv = _nonzero(rng, -9, 9)
    x_t = -P
    expr = square_form_latex(a, P, qv)
    q = f"The equation of a curve is {math('y = ' + expr)}. Write down the coordinates of its turning point."
    ans = (x_t, qv)
    items = [("sign_of_x", (P, qv)), ("coordinates_swapped", (qv, x_t)), ("sign_of_y", (x_t, -qv))]
    return _Built(
        "sketch_square_form", q, math(_pt_l(*ans)),
        [(code, math(_pt_l(*v)), _pt_t(*v), v) for code, v in items], ans,
        {"task": "square_form_turning_point", "a": a, "p": P, "q": qv},
        [("The bracket is zero when x is", str(x_t)), ("The y-value is the number added", str(qv))],
        _marking("coordinates", [_pt_t(*ans)]),
    )


def _sketch3(rng: SeededRandom) -> _Built:
    for _ in range(_MAX_ATTEMPTS):
        a = rng.choice((1, -1, 2, 3, -2))
        b = _nonzero(rng, -9, 9)
        c = rng.randint(-9, 9)
        x_t = Fraction(-b, 2 * a)
        y_t = c - Fraction(b * b, 4 * a)
        if c == 0 or y_t == c or x_t == 0:
            continue
        break
    else:
        raise GeneratorError("level 3 not found")
    expr = quadratic_latex(a, b, c)
    q = f"Find the coordinates of the turning point of the curve {math('y = ' + expr)}."
    ans = (x_t, y_t)
    xr = Fraction(-b, a)
    items = [
        ("sign_of_x", (-x_t, y_t)),
        ("forgot_two", (xr, a * xr * xr + b * xr + c)),
        ("intercept_used_for_y", (x_t, c)),
    ]
    return _Built(
        "sketch_turning_point", q, math(_pt_l(*ans)),
        [(code, math(_pt_l(*v)), _pt_t(*v), v) for code, v in items], ans,
        {"task": "turning_point", "quadratic": [a, b, c]},
        [("x = -b/2a", _t(x_t)), ("Substitute to find y", _t(y_t))],
        _marking("coordinates", [_pt_t(*ans)]),
    )


def _sketch4(rng: SeededRandom) -> _Built:
    if rng.chance(1, 4):
        a, b, c, _, _, _ = _factored_quadratic(rng)
        x_t, y_t = Fraction(-b, 2 * a), c - Fraction(b * b, 4 * a)
        if x_t.denominator == 1 and y_t.denominator == 1:
            expr = quadratic_latex(a, b, c)
            q = (f"The curve {math('y = ' + expr)} has a turning point at {math(_pt_l(x_t, y_t))}. "
                 f"Write down the gradient of the tangent to the curve at the turning point.")
            items = [("gradient_of_chord", Fraction(c), ), ("y_value_used", y_t), ("x_value_used", x_t)]
            items = [(code, v) for code, v in items if v != 0]
            return _Built(
                "sketch_turning_gradient", q, math("0"),
                [(code, math(_l(v)), _t(v), v) for code, v in items], Fraction(0),
                {"task": "turning_point_gradient", "quadratic": [a, b, c]},
                [("The tangent at a turning point is horizontal", "0")], _marking("number_exact", ["0"]),
            )
    for _ in range(_MAX_ATTEMPTS):
        a = rng.choice((1, 1, 2, -1, 3))
        b = rng.randint(-6, 6)
        c = rng.randint(-8, 8)
        x1 = rng.randint(-3, 3)
        x2 = x1 + rng.randint(1, 4)
        f = lambda x: a * x * x + b * x + c
        dy, dx = f(x2) - f(x1), x2 - x1
        m = Fraction(dy, dx)
        if dy == 0 or m == dy or c == 0:
            continue
        break
    else:
        raise GeneratorError("level 4 not found")
    expr = quadratic_latex(a, b, c)
    q = (f"The points {math('P')} and {math('Q')} lie on the curve {math('y = ' + expr)}, where {math('x = ' + str(x1))} and {math('x = ' + str(x2))}. "
         f"Calculate the gradient of the chord {math('PQ')}.")
    items = [("rise_only", Fraction(dy)), ("sign_reversed", Fraction(dy, -dx)), ("inverted", Fraction(dx, dy))]
    return _Built(
        "sketch_chord_gradient", q, math(_l(m)),
        [(code, math(_l(v)), _t(v), v) for code, v in items], m,
        {"task": "chord_gradient", "quadratic": [a, b, c], "x": [x1, x2]},
        [("y-values at the two points", f"{f(x1)} and {f(x2)}"), ("Change in y over change in x", _t(m))],
        _marking("number_exact", [_t(m)]),
    )


class SketchingQuadraticsGenerator(_FamilyGenerator):
    generator_id = SKETCH_ID
    version = 1
    levels = (1, 2, 3, 4)
    level_skills = SKETCH_LEVEL_SKILLS
    error_notes = SKETCH_ERROR_NOTES
    builders = {1: _sketch1, 2: _sketch2, 3: _sketch3, 4: _sketch4}


# ==========================================================================
# Lesson 15834: Advanced Graphs (reciprocal, cubic, exponential)
# ==========================================================================

ADV_ERROR_NOTES: Dict[str, Dict[str, str]] = {
    "reciprocal_values": {
        "sign_lost": "ignored the minus sign of a negative x-value",
        "square_after_divide": "divided first and then squared, instead of dividing by the square",
        "double_denominator": "worked out the constant over twice the x-value",
    },
    "cubic_values": {
        "negative_cube": "cubed a negative number and gave a positive answer",
        "cube_as_triple": "multiplied by 3 instead of cubing",
        "sign_of_x_term": "used the opposite sign for the x term",
    },
    "exponential_values": {
        "multiplied": "multiplied the base by the power instead of raising it",
        "negative_power": "took a negative power as a negative number",
        "reciprocal_missed": "turned a negative power into the base itself, not its reciprocal",
    },
    "exponential_intercept": {
        "coordinates_swapped": "wrote the intercept with the x and y values the wrong way round",
        "asymptote_used": "gave the asymptote value as the intercept",
        "base_used": "gave the base as the y-intercept",
    },
    "asymptotes": {
        "swapped": "gave the vertical and horizontal asymptotes the wrong way round",
        "only_one": "gave only one of the two asymptotes",
        "sign_error": "gave the shift with the wrong sign",
        "ignored_shift": "ignored the number added to the function",
        "wrong_direction": "gave a vertical line where the asymptote is horizontal",
    },
    "solve_reciprocal_square": {
        "positive_only": "found only the positive solution",
        "root_not_taken": "forgot to take the square root",
    },
    "solve_reciprocal": {
        "multiplied": "multiplied the numbers instead of dividing",
        "inverted": "divided the numbers the wrong way round",
    },
    "solve_exponential": {
        "sign_error": "gave the power with the wrong sign",
        "divided_by_base": "divided by the base instead of finding the power",
    },
    "solve_cubic": {
        "divided_by_three": "divided by 3 instead of taking the cube root",
        "sign_error": "gave the cube root with the wrong sign",
    },
}

ADV_LEVEL_SKILLS: Dict[int, Tuple[str, ...]] = {
    1: ("reciprocal_values",),
    2: ("cubic_values",),
    3: ("exponential_values", "exponential_intercept"),
    4: ("asymptotes",),
    5: ("solve_reciprocal_square", "solve_reciprocal", "solve_exponential", "solve_cubic"),
}

_RECIP_X = (-5, -4, -2, -1, Fraction(-1, 2), Fraction(1, 2), 1, 2, 4, 5)


def _x_display(x: Any) -> str:
    return _dec(x)


def _adv1(rng: SeededRandom) -> _Built:
    for _ in range(_MAX_ATTEMPTS):
        k = rng.choice((1, 2, 4, 5, 8, 10))
        squared = rng.chance(1, 2)
        xs = sorted(rng.choice(_RECIP_X) for _ in range(3))
        if len(set(xs)) < 3 or (not squared and all(x > 0 for x in xs)):
            continue
        f = (lambda x: Fraction(k) / (Fraction(x) ** 2)) if squared else (lambda x: Fraction(k) / Fraction(x))
        correct = [f(x) for x in xs]
        if squared:
            alt1 = [(Fraction(k) / Fraction(x)) ** 2 for x in xs]
            alt2 = [Fraction(k) / (2 * Fraction(x)) for x in xs]
            items = [("square_after_divide", alt1), ("double_denominator", alt2)]
            expr = rf"\frac{{{k}}}{{x^{{2}}}}"
        else:
            items = [("sign_lost", [Fraction(k) / abs(Fraction(x)) for x in xs]), ("double_denominator", [Fraction(k) / (2 * Fraction(x)) for x in xs])]
            expr = rf"\frac{{{k}}}{{x}}"
        q = f"Find the value of {math('y')} when {_xs_math(xs, _x_display)} for the function {math('y = ' + expr)}."
        return _Built(
            "reciprocal_values", q, math(", ".join(_l(v) if v.denominator != 1 or True else str(v) for v in correct)),
            [(code, math(", ".join(_l(v) for v in vals)), ", ".join(_dec(v) for v in vals), tuple(vals)) for code, vals in items],
            tuple(correct), {"task": "reciprocal_values", "k": k, "squared": squared, "x": [str(x) for x in xs]},
            [(f"Substitute x = {_x_display(x)}", _dec(v)) for x, v in zip(xs, correct)],
            _marking("table_values", [", ".join(_dec(v) for v in correct)]),
        )
    raise GeneratorError("level 1 not found")


def _adv2(rng: SeededRandom) -> _Built:
    for _ in range(_MAX_ATTEMPTS):
        if rng.chance(1, 2):
            c = _nonzero(rng, -8, 8)
            coefs, f = [1, 0, 0, c], (lambda x: x ** 3 + c)
            sign_alt = lambda x: x ** 3 - c
        else:
            a = rng.randint(1, 9)
            coefs, f = [1, 0, -a, 0], (lambda x: x ** 3 - a * x)
            sign_alt = lambda x: x ** 3 + a * x
        xs = _subset(rng, list(range(-3, 4)), 3)
        if min(xs) >= 0:
            continue
        correct = [f(x) for x in xs]
        negcube = [(abs(x) ** 3 + (f(x) - x ** 3)) for x in xs]
        triple = [3 * x + (f(x) - x ** 3) for x in xs]
        items = [("negative_cube", negcube), ("cube_as_triple", triple), ("sign_of_x_term", [sign_alt(x) for x in xs])]
        q = f"Find the value of {math('y')} when {_xs_math(xs)} for the function {math('y = ' + polynomial_latex(coefs))}."
        return _Built(
            "cubic_values", q, math(", ".join(str(v) for v in correct)),
            [(code, math(", ".join(str(v) for v in vals)), ", ".join(str(v) for v in vals), tuple(vals)) for code, vals in items],
            tuple(correct), {"task": "cubic_values", "coefficients": coefs, "x": xs},
            [(f"Substitute x = {x}", str(v)) for x, v in zip(xs, correct)],
            _marking("table_values", [", ".join(str(v) for v in correct)]),
        )
    raise GeneratorError("level 2 not found")


def _exp_expr(a: int, b: int, k: int = 0) -> str:
    lead = "" if a == 1 else f"{a} \\times "
    text = f"{lead}{b}^{{x}}"
    return text + (f" + {k}" if k > 0 else f" - {-k}" if k < 0 else "")


def _adv3(rng: SeededRandom) -> _Built:
    a = rng.choice((1, 1, 2, 3, 4))
    b = rng.choice((2, 2, 3, 5, 10))
    if rng.chance(1, 3):
        q = f"The graph of {math('y = ' + _exp_expr(a, b))} crosses the {math('y')}-axis. Write down the coordinates of the point where it does so."
        ans = (0, a)
        items = [("coordinates_swapped", (a, 0)), ("base_used", (0, b)), ("asymptote_used", (0, 0))]
        return _Built(
            "exponential_intercept", q, math(_pt_l(*ans)),
            [(code, math(_pt_l(*v)), _pt_t(*v), v) for code, v in items], ans,
            {"task": "exp_intercept", "a": a, "b": b}, [("Anything to the power 0 is 1, so y is", str(a))],
            _marking("coordinates", [_pt_t(*ans)]),
        )
    for _ in range(_MAX_ATTEMPTS):
        xs = sorted(_subset(rng, list(range(-2, 4)), 3))
        if min(xs) >= 0:
            continue
        correct = [Fraction(a) * Fraction(b) ** x for x in xs]
        items = [
            ("multiplied", [Fraction(a * b * x) for x in xs]),
            ("negative_power", [Fraction(a) * (Fraction(b) ** x if x >= 0 else -(Fraction(b) ** abs(x))) for x in xs]),
            ("reciprocal_missed", [Fraction(a) * (Fraction(b) ** x if x >= 0 else Fraction(b) ** abs(x)) for x in xs]),
        ]
        q = f"Find the value of {math('y')} when {_xs_math(xs)} for the function {math('y = ' + _exp_expr(a, b))}."
        return _Built(
            "exponential_values", q, math(", ".join(_l(v) for v in correct)),
            [(code, math(", ".join(_l(v) for v in vals)), ", ".join(_t(v) for v in vals), tuple(vals)) for code, vals in items],
            tuple(correct), {"task": "exp_values", "a": a, "b": b, "x": xs},
            [(f"Substitute x = {x}", _t(v)) for x, v in zip(xs, correct)],
            _marking("table_values", [", ".join(_t(v) for v in correct)]),
        )
    raise GeneratorError("level 3 not found")


def _adv4(rng: SeededRandom) -> _Built:
    kind = rng.choice(("recip", "recip_sq", "exp"))
    c = _nonzero(rng, -6, 6)
    c_text = f" + {c}" if c > 0 else f" - {-c}"
    if kind in ("recip", "recip_sq"):
        k = rng.choice((1, 2, 3, 4, 5))
        body = rf"\frac{{{k}}}{{x}}" if kind == "recip" else rf"\frac{{{k}}}{{x^{{2}}}}"
        q = f"Write down the equations of the two asymptotes of the graph of {math('y = ' + body + c_text)}."
        ans = f"x = 0 and y = {c}"
        items = [
            ("swapped", f"x = {c} and y = 0"), ("only_one", f"y = {c}"), ("sign_error", f"x = 0 and y = {-c}"), ("ignored_shift", "x = 0 and y = 0"),
        ]
        steps = [("The graph is undefined at", "x = 0"), ("For large x the fraction shrinks to zero so y approaches", f"y = {c}")]
        display = lambda s: math(s.replace(" and ", r"\ \text{and}\ "))
        mk = _marking("equation_solution", [ans])
    else:
        b = rng.choice((2, 3, 5, 10))
        q = f"Write down the equation of the horizontal asymptote of the graph of {math('y = ' + _exp_expr(1, b, c))}."
        ans = f"y = {c}"
        items = [("ignored_shift", "y = 0"), ("sign_error", f"y = {-c}"), ("wrong_direction", f"x = {c}"), ("swapped", f"x = {-c}")]
        steps = [(f"As x gets very negative {b}^x approaches", "0"), ("So y approaches", ans)]
        display = math
        mk = _marking("equation_solution", [ans])
    return _Built(
        "asymptotes", q, display(ans),
        [(code, display(text), text, text) for code, text in items], ans,
        {"task": "asymptotes", "shape": kind, "shift": c}, steps, mk,
    )


def _adv5(rng: SeededRandom) -> _Built:
    kind = rng.choice(("recip_sq", "recip", "exp", "cubic"))
    if kind == "recip_sq":
        x0 = rng.randint(2, 6)
        k = rng.randint(1, 9)
        m = Fraction(k, x0 * x0)
        q = ''.join(['Solve ', format(math(''.join(['\\frac{', format(k, ''), '}{x^{2}} = ']) + _l(m)), ''), '.'])
        ans_text = f"x = {-x0} or x = {x0}"
        items = [("positive_only", f"x = {x0}"), ("root_not_taken", f"x = {-x0 * x0} or x = {x0 * x0}")]
        steps = [("Rearrange to x squared", f"x^2 = {x0 * x0}"), ("Take the square root, two solutions", ans_text)]
        skill = "solve_reciprocal_square"
        shown = math(f"x = {-x0}\\ \\text{{or}}\\ x = {x0}")
    elif kind == "recip":
        x0 = _nonzero(rng, -8, 8)
        k = rng.randint(2, 12)
        m = Fraction(k, x0)
        q = ''.join(['Solve ', format(math(''.join(['\\frac{', format(k, ''), '}{x} = ']) + _l(m)), ''), '.'])
        ans_text = f"x = {x0}"
        items = [("multiplied", f"x = {_t(k * m)}"), ("inverted", f"x = {_t(m / k)}")]
        steps = [("Multiply both sides by x and divide", ans_text)]
        skill = "solve_reciprocal"
        shown = math(ans_text)
    elif kind == "exp":
        b = rng.choice((2, 3, 5, 10))
        e = rng.randint(-3, 4)
        value = Fraction(b) ** e
        q = f"Solve {math(f'{b}^{{x}} = ' + _l(value))}."
        ans_text = f"x = {e}"
        items = [("sign_error", f"x = {-e}"), ("divided_by_base", f"x = {_t(value / b)}")]
        steps = [(f"Write the right-hand side as a power of {b}", f"{b}^{e}"), ("Equate the powers", ans_text)]
        skill = "solve_exponential"
        shown = math(ans_text)
    else:
        e = _nonzero(rng, -4, 4)
        value = e ** 3
        q = f"Solve {math(f'x^{{3}} = {value}')}."
        ans_text = f"x = {e}"
        items = [("divided_by_three", f"x = {_t(Fraction(value, 3))}"), ("sign_error", f"x = {-e}")]
        steps = [("Take the cube root of both sides", ans_text)]
        skill = "solve_cubic"
        shown = math(ans_text)
    out = [(code, math(text.replace(" or ", r"\ \text{or}\ ")) if " or " in text else math(text), text, text) for code, text in items]
    return _Built(
        skill, q, shown, out, ans_text, {"task": "solve_" + kind}, steps, _marking("equation_solution", [ans_text]),
    )


class AdvancedGraphsGenerator(_FamilyGenerator):
    generator_id = ADV_ID
    version = 1
    levels = (1, 2, 3, 4, 5)
    level_skills = ADV_LEVEL_SKILLS
    error_notes = ADV_ERROR_NOTES
    builders = {1: _adv1, 2: _adv2, 3: _adv3, 4: _adv4, 5: _adv5}


# ==========================================================================
# Lesson 15829: Linear Programming (inequalities and best value, no shading)
# ==========================================================================

LP_ERROR_NOTES: Dict[str, Dict[str, str]] = {
    "lp_write_inequality": {
        "reversed": "wrote the inequality sign the wrong way round",
        "strict": "used a strict sign where the limit itself is allowed",
        "non_strict": "allowed the limit itself where the wording says it must not be reached",
        "variables_swapped": "swapped which letter stands for which quantity",
        "one_term_only": "wrote the limit for only one of the two quantities",
    },
    "lp_test_points": {
        "one_inequality_only": "tested each point against only the first inequality",
        "boundary_excluded": "rejected points that lie exactly on a boundary line",
        "points_all": "counted every point without testing",
        "any_two": "counted points satisfying only some of the inequalities",
    },
    "lp_three_inequalities": {
        "one_reversed": "wrote one of the inequalities the wrong way round",
        "one_missing": "left one of the conditions out",
        "strict": "used a strict sign where the limit itself is allowed",
    },
    "lp_best_value": {
        "other_vertex": "worked out the value at a different corner of the region",
        "wrong_extreme": "found the least value when the greatest was asked for (or the reverse)",
        "total_only": "used the total limit instead of testing the corners",
    },
}

LP_LEVEL_SKILLS: Dict[int, Tuple[str, ...]] = {
    1: ("lp_write_inequality",),
    2: ("lp_test_points",),
    3: ("lp_three_inequalities",),
    4: ("lp_best_value",),
}

_LP_CONTEXTS = (
    ("a farmer plants maize on {x} hectares and sunflowers on {y} hectares", "hectares"),
    ("a taxi company in Windhoek buys {x} small taxis and {y} minibuses", "vehicles"),
    ("a school buys {x} desks and {y} chairs", "items"),
    ("a bakery in Swakopmund bakes {x} batches of rolls and {y} batches of bread", "batches"),
)

_REL_LATEX = {">": ">", ">=": r"\ge", "<": "<", "<=": r"\le"}
_FLIP = {">": "<", ">=": "<=", "<": ">", "<=": ">="}


def _ineq_l(text: str) -> str:
    return math(text.replace(">=", r"\ge").replace("<=", r"\le"))


def _lp1(rng: SeededRandom) -> _Built:
    ctx, unit = rng.choice(_LP_CONTEXTS)
    who = ctx.format(x="$x$", y="$y$")
    kind = rng.choice(("total_max", "x_min", "y_more", "y_twice", "weighted"))
    n = rng.randint(6, 12)
    if kind == "total_max":
        stmt, ans = f"The total is at most {n} {unit}.", f"x + y <= {n}"
        wrong = [("reversed", f"x + y >= {n}"), ("strict", f"x + y < {n}"), ("one_term_only", f"x <= {n}")]
    elif kind == "x_min":
        k = rng.randint(2, 5)
        stmt, ans = f"There must be at least {k} of the first kind.", f"x >= {k}"
        wrong = [("reversed", f"x <= {k}"), ("strict", f"x > {k}"), ("variables_swapped", f"y >= {k}")]
    elif kind == "y_more":
        stmt, ans = "There must be more of the second kind than of the first kind.", "y > x"
        wrong = [("reversed", "y < x"), ("non_strict", "y >= x"), ("variables_swapped", "x > y")]
    elif kind == "y_twice":
        stmt, ans = "There must be at least twice as many of the second kind as of the first kind.", "y >= 2x"
        wrong = [("reversed", "y <= 2x"), ("strict", "y > 2x"), ("variables_swapped", "x >= 2y")]
    else:
        a, b = rng.randint(2, 4), rng.randint(1, 3)
        if a == b:
            a += 1
        limit = rng.randint(8, 12)
        stmt = f"Each of the first kind needs {a} workers and each of the second kind needs {b} workers. At most {limit} workers are available."
        ans = f"{a}x + {b}y <= {limit}" if b != 1 else f"{a}x + y <= {limit}"
        wrong = [("reversed", ans.replace("<=", ">=")), ("strict", ans.replace("<=", "<")), ("variables_swapped", f"{b}x + {a}y <= {limit}" if b != 1 else f"x + {a}y <= {limit}")]
    q = f"In a project, {who}. {stmt} Write down an inequality, in terms of {math('x')} and {math('y')}, for this condition."
    return _Built(
        "lp_write_inequality", q, _ineq_l(ans), [(c, _ineq_l(t), t, t) for c, t in wrong], ans,
        {"task": "write_inequality", "kind": kind},
        [("Choose the sign from the wording", ans)], _marking("inequality", [ans]),
    )


def _lp2(rng: SeededRandom) -> _Built:
    for _ in range(_MAX_ATTEMPTS):
        T = rng.randint(7, 11)
        a, b = rng.randint(1, 3), rng.randint(1, 4)
        points = [(rng.randint(0, 8), rng.randint(0, 8)) for _ in range(5)]
        if len(set(points)) < 5:
            continue
        conds = [(lambda p: p[0] + p[1] <= T, f"x + y <= {T}"), (lambda p: p[0] >= a, f"x >= {a}"), (lambda p: p[1] >= b, f"y >= {b}")]
        good = [p for p in points if all(c(p) for c, _ in conds)]
        first_only = [p for p in points if conds[0][0](p)]
        strict = [p for p in points if p[0] + p[1] < T and p[0] > a and p[1] > b]
        some = [p for p in points if sum(1 for c, _ in conds if c(p)) >= 2]
        counts = {len(good), len(first_only), len(strict), len(some), 5}
        if len(good) < 1 or len(counts) < 4 or len(good) == 5:
            continue
        break
    else:
        raise GeneratorError("level 2 not found")
    pts = ", ".join(_pt_l(*p) for p in points)
    ineqs = ", ".join(_ineq_l(t)[1:-1] for _, t in conds)
    q = (f"The inequalities {math(ineqs)} describe a region. "
         f"How many of the points {math(pts)} satisfy all three inequalities?")
    steps = [(f"Test {_pt_t(*p)}", "satisfies all three" if p in good else "fails at least one") for p in points] + [("Count the points that pass", str(len(good)))]
    items = [("one_inequality_only", len(first_only)), ("boundary_excluded", len(strict)), ("points_all", 5), ("any_two", len(some))]
    return _Built(
        "lp_test_points", q, math(str(len(good))), [(c, math(str(v)), str(v), v) for c, v in items], len(good),
        {"task": "test_points", "points": [list(p) for p in points], "limits": [T, a, b]}, steps,
        _marking("number_exact", [str(len(good))]),
    )


def _lp3(rng: SeededRandom) -> _Built:
    ctx, unit = rng.choice(_LP_CONTEXTS)
    who = ctx.format(x="$x$", y="$y$")
    T = rng.randint(9, 12)
    second = rng.choice(("y_min", "y_more", "y_twice"))
    a, b = rng.randint(1, 3 if second == "y_twice" else 4), rng.randint(1, 4)
    if second == "y_min":
        stmt2, ineq2 = f"at least {b} of the second kind", f"y >= {b}"
    elif second == "y_more":
        stmt2, ineq2 = "more of the second kind than of the first kind", "y > x"
    else:
        stmt2, ineq2 = "at least twice as many of the second kind as of the first kind", "y >= 2x"
    stmt = f"There must be at least {a} of the first kind, {stmt2}, and at most {T} {unit} altogether."
    parts = [f"x >= {a}", ineq2, f"x + y <= {T}"]
    ans = "; ".join(parts)

    def latex(items: Sequence[str]) -> str:
        return math(",\\ ".join(i.replace(">=", r"\ge").replace("<=", r"\le") for i in items))

    flipped_idx = rng.randint(0, 2)
    flipped = list(parts)
    flipped[flipped_idx] = flipped[flipped_idx].replace(">=", "<<").replace("<=", ">=").replace("<<", "<=") if (">=" in flipped[flipped_idx] or "<=" in flipped[flipped_idx]) else flipped[flipped_idx].replace(">", "<")
    wrong = [
        ("one_reversed", flipped),
        ("one_missing", [p for i, p in enumerate(parts) if i != 1]),
        ("strict", [parts[0].replace(">=", ">"), parts[1], parts[2].replace("<=", "<")]),
    ]
    q = f"In a project, {who}. {stmt} Write down three inequalities that describe these conditions."
    return _Built(
        "lp_three_inequalities", q, latex(parts), [(c, latex(v), "; ".join(v), "; ".join(v)) for c, v in wrong], ans,
        {"task": "three_inequalities", "limits": [a, T], "second": second},
        [("The condition on the first kind", parts[0]), ("The condition on the second kind", parts[1]), ("The total limit", parts[2])],
        _marking("inequality", [ans]),
    )


def _lp4(rng: SeededRandom) -> _Built:
    for _ in range(_MAX_ATTEMPTS):
        a, b = rng.randint(1, 4), rng.randint(1, 4)
        T = rng.randint(max(a, b) + 4, 14)
        p, q_ = rng.randint(1, 6), rng.randint(1, 6)
        vertices = [(a, b), (T - b, b), (a, T - a)]
        if T - b <= a or T - a <= b or p == q_:
            continue
        values = [p * x + q_ * y for x, y in vertices]
        if len(set(values)) < 3:
            continue
        break
    else:
        raise GeneratorError("level 4 not found")
    greatest = rng.chance(2, 3)
    ans = max(values) if greatest else min(values)
    other = min(values) if greatest else max(values)
    mid = sorted(values)[1]
    ineqs = f"x >= {a}, y >= {b}, x + y <= {T}"
    obj = f"{'' if p == 1 else p}x + {'' if q_ == 1 else q_}y"
    word = "greatest" if greatest else "least"
    q = (f"The region defined by {math(ineqs.replace('>=', chr(92) + 'ge').replace('<=', chr(92) + 'le'))} is used by Kudu Crafts to plan production. Here x and y are the numbers of batches of two types of craft item. "
         f"The profit, in thousands of Namibian dollars, is {math('P = ' + obj)}. Find the {word} possible value of {math('P')}.")
    items = [("wrong_extreme", other), ("other_vertex", mid), ("total_only", p * T if greatest else q_ * T)]
    steps = [("The corners of the region", ", ".join(_pt_t(*v) for v in vertices))] + [(f"Value of P at {_pt_t(*v)}", str(val)) for v, val in zip(vertices, values)] + [(f"The {word} value", str(ans))]
    return _Built(
        "lp_best_value", q, math(str(ans)), [(c, math(str(v)), str(v), v) for c, v in items], ans,
        {"task": "best_value", "vertices": [list(v) for v in vertices], "objective": [p, q_], "greatest": greatest}, steps,
        _marking("number_exact", [str(ans)]),
    )


class LinearProgrammingGenerator(_FamilyGenerator):
    generator_id = LINPROG_ID
    version = 1
    levels = (1, 2, 3, 4)
    level_skills = LP_LEVEL_SKILLS
    error_notes = LP_ERROR_NOTES
    builders = {1: _lp1, 2: _lp2, 3: _lp3, 4: _lp4}


GENERATORS = [
    SetsNotationGenerator(),
    VennDiagramsGenerator(),
    QuadraticGraphsGenerator(),
    SketchingQuadraticsGenerator(),
    AdvancedGraphsGenerator(),
    LinearProgrammingGenerator(),
]
