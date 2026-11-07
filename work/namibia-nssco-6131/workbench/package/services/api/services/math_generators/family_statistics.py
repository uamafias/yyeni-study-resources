"""Generators for the Topic 12 (Statistics and Probability) lessons in text form.

One generator per lesson. Every problem is built backwards from its answer and
re-checked with exact arithmetic (``Fraction`` and ``itertools`` enumeration)
before it is returned. Data are shown as lists and short LaTeX tables; questions
that need a drawn figure (histograms, reading a graph) are out of scope here.

Question shapes follow the 2020-2024 NSSCO papers (mean/median/mode/range, a
missing value from the mean, the change in a mean, grouped means, cumulative
frequency tables, probability of beads/letters/two-way tables, tree diagrams
without replacement and at least one) but never reuse their wording or numbers.

Lessons and ids:

* ``nssco_mean_median_mode_range``      (4 levels)
* ``nssco_grouped_data_mean``           (5 levels)
* ``nssco_simple_probability``          (5 levels)
* ``nssco_tree_diagrams``               (5 levels)
* ``nssco_cumulative_frequency_reading`` (4 levels)
"""

from __future__ import annotations

import itertools
import statistics
from decimal import ROUND_HALF_UP, Decimal
from fractions import Fraction
from typing import Any, Callable, Dict, List, Mapping, Sequence, Tuple

from ..math_marking import check

from .base import Distractor, GeneratedProblem, GeneratorError, MathGenerator, SeededRandom, Step
from .formatting import math, number_latex

_MAX_ATTEMPTS = 500

NAMES = ("Tangeni", "Ndapewa", "Johannes", "Hilma", "Petrus", "Selma", "Mateus", "Kaarina", "Elia", "Saara")


# --------------------------------------------------------------------------
# shared helpers
# --------------------------------------------------------------------------


def _require(condition: bool, message: str) -> None:
    if not condition:
        raise GeneratorError(message)


def _shuffled(rng: SeededRandom, items: Sequence[Any]) -> List[Any]:
    out = list(items)
    for i in range(len(out) - 1, 0, -1):
        j = rng.randbelow(i + 1)
        out[i], out[j] = out[j], out[i]
    return out


def _sample(rng: SeededRandom, items: Sequence[Any], k: int) -> List[Any]:
    return _shuffled(rng, items)[:k]


def _frac_text(f: Fraction) -> str:
    return str(f.numerator) if f.denominator == 1 else f"{f.numerator}/{f.denominator}"


def _terminating(f: Fraction) -> bool:
    d = f.denominator
    for p in (2, 5):
        while d % p == 0:
            d //= p
    return d == 1


def _dec_text(f: Fraction) -> str:
    """Exact decimal text of a terminating fraction (``0.375``, ``63.5``, ``12``)."""
    _require(_terminating(f), "not a terminating decimal")
    text = format((Decimal(f.numerator) / Decimal(f.denominator)).normalize(), "f")
    return text


def _num_text(f: Fraction) -> str:
    return _dec_text(f) if _terminating(f) else _frac_text(f)


def _prob_expected(f: Fraction) -> List[str]:
    out = [_frac_text(f)]
    if f.denominator != 1 and _terminating(f):
        out.append(_dec_text(f))
    return out


def _prob_display(f: Fraction) -> str:
    return math(number_latex(f))


def _round(value: Fraction, mode: str, digits: int) -> str:
    """HALF_UP rounding, written the way the marker rounds (``sig_figs`` / ``decimal_places``)."""
    d = Decimal(value.numerator) / Decimal(value.denominator)
    if mode == "sig_figs":
        if d == 0:
            return "0"
        q = Decimal(1).scaleb(d.adjusted() - (digits - 1))
    else:
        q = Decimal(1).scaleb(-digits)
    return format(d.quantize(q, rounding=ROUND_HALF_UP), "f")


def _list_text(values: Sequence[Any]) -> str:
    return ", ".join(str(v) for v in values)


def _interval(lo: int, hi: int, var: str) -> Tuple[str, str]:
    """(LaTeX, plain text) of the class ``lo <= var < hi``."""
    return f"{lo} \\le {var} < {hi}", f"{lo} <= {var} < {hi}"


def _table(header: Sequence[str], rows: Sequence[Sequence[str]], align: str = "") -> str:
    cols = align or "|" + "|".join("c" for _ in header) + "|"
    lines = ["\\begin{array}{" + cols + "}\\hline", " & ".join(header) + " \\\\ \\hline"]
    lines += [" & ".join(r) + " \\\\ \\hline" for r in rows]
    lines.append("\\end{array}")
    return " ".join(lines)


Candidate = Tuple[str, str, str]  # (error code, display text, typed text)


def _prob_candidates(answer: Fraction, options: Sequence[Tuple[str, Fraction]]) -> List[Candidate]:
    out: List[Candidate] = []
    for code, value in options:
        if value == answer or value <= 0 or value >= 1:
            continue
        out.append((code, _prob_display(value), _frac_text(value)))
    return out


def _number_candidates(answer: Any, options: Sequence[Tuple[str, Fraction]]) -> List[Candidate]:
    out: List[Candidate] = []
    for code, value in options:
        value = Fraction(value)
        if value == Fraction(answer) or value < 0:
            continue
        out.append((code, math(_num_text(value)), _num_text(value)))
    return out


class _StatGenerator(MathGenerator):
    """Shared plumbing: pick a level builder, then tidy the distractors."""

    version = 1
    _builders: Mapping[int, Callable[..., Dict[str, Any]]] = {}

    def _build(self, rng: SeededRandom, seed: int, level: int) -> GeneratedProblem:
        b = self._builders[level](rng)
        marking = dict(b["marking"])
        if "as a fraction in its simplest form" in b["question"]:
            marking["form"] = "simplest_fraction"
        marking["typed"] = b.get("typed", marking["expected"][0])
        kw = {k: marking[k] for k in ("rounding", "digits", "form") if k in marking}
        own = check(marking["answer_type"], marking["expected"], marking["typed"], **kw)
        _require(own.correct, f"{self.generator_id}: own answer rejected by the marker: {marking['typed']!r}")
        seen = {b["answer"]}
        distractors: List[Distractor] = []
        for code, display, typed in b["cands"]:
            if display in seen or not typed:
                continue
            if check(marking["answer_type"], marking["expected"], typed, **kw).correct:
                continue
            seen.add(display)
            distractors.append(Distractor(display, code, self.error_notes[b["skill"]][code], typed))
        return GeneratedProblem(
            generator_id=self.generator_id,
            generator_version=self.version,
            seed=seed,
            level=level,
            skill=b["skill"],
            question=b["question"],
            answer=b["answer"],
            distractors=tuple(distractors),
            machine=b["machine"],
            steps=tuple(Step(d, v) for d, v in b["steps"]),
            marking=marking,
        )


# ==========================================================================
# 1. Mean, median, mode and range
# ==========================================================================

_LIST_CONTEXTS = (
    ("The ages, in years, of {n} members of a Windhoek chess club are", "ages", 12, 30),
    ("The masses, in kilograms, of {n} parcels at the Katima Mulilo post office are", "masses", 2, 40),
    ("The daily rainfall, in millimetres, recorded at Rundu on {n} days was", "rainfall amounts", 0, 45),
    ("The number of passengers on {n} buses from Oshakati to Ondangwa was", "numbers", 18, 64),
    ("The marks of {n} learners in a Grade 10 mathematics quiz were", "marks", 8, 49),
    ("The prices, in Namibian dollars, of {n} loaves of bread at different Swakopmund shops were", "prices", 9, 28),
)
_WORDS = {4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten", 12: "twelve"}

_MEAN_ERRORS: Dict[str, Dict[str, str]] = {
    "single_statistic": {
        "largest_value": "gave the largest value instead of the statistic that was asked for",
        "median_for_mode": "gave the middle value instead of the value that appears most often",
        "mode_for_median": "gave the value that appears most often instead of the middle value",
        "unsorted_middle": "took the middle number of the list without putting the values in order first",
        "max_plus_min": "added the largest and smallest values instead of subtracting",
        "mean_for_median": "worked out the mean instead of the median",
        "median_for_mean": "gave the middle value instead of adding all the values and dividing",
        "forgot_divide": "added the values but did not divide by how many there are",
        "divide_n_minus_1": "divided the total by one less than the number of values",
        "lower_middle": "gave only the lower of the two middle values",
        "upper_middle": "gave only the higher of the two middle values",
        "mode_for_mean": "gave the value that appears most often instead of the mean",
    },
    "missing_value_from_mean": {
        "x_equals_mean": "assumed the missing value equals the mean",
        "used_n_minus_1": "multiplied the mean by one less than the number of values",
        "added_known": "added the known values to the total instead of subtracting them",
        "forgot_total": "subtracted the known values from the mean instead of from the total",
    },
    "change_in_mean": {
        "used_n_both": "used the number before the change for both totals",
        "new_mean_only": "gave the new mean as the new value",
        "difference_only": "gave only the change in the mean",
        "added_totals": "added the old total to the new total instead of subtracting",
    },
}


def _distinct_values(rng: SeededRandom, count: int, lo: int, hi: int, exclude: Sequence[int] = ()) -> List[int]:
    pool = [v for v in range(lo, hi + 1) if v not in exclude]
    _require(len(pool) >= count, "value range too small")
    return _sample(rng, pool, count)


def _list_with_mode(rng: SeededRandom, n: int, lo: int, hi: int) -> Tuple[List[int], int]:
    mode = rng.randint(lo + 1, hi - 1)
    rest = _distinct_values(rng, n - 2, lo, hi, exclude=(mode,))
    return _shuffled(rng, [mode, mode] + rest), mode


def _list_intro(rng: SeededRandom, n: int) -> Tuple[str, str]:
    template, noun, lo, hi = rng.choice(_LIST_CONTEXTS)
    return template.format(n=_WORDS[n]), noun


def _level_stats_odd(rng: SeededRandom) -> Dict[str, Any]:
    n = rng.choice((5, 7))
    template, noun, lo, hi = rng.choice(_LIST_CONTEXTS)
    stat = rng.choice(("mode", "median", "range"))
    values, mode = _list_with_mode(rng, n, lo, hi)
    ordered = sorted(values)
    results = {"mode": mode, "median": ordered[n // 2], "range": ordered[-1] - ordered[0]}
    ans = results[stat]
    _require(ans == {"mode": statistics.mode(values), "median": statistics.median(values), "range": max(values) - min(values)}[stat], "stat mismatch")
    options = {
        "mode": [("largest_value", ordered[-1]), ("median_for_mode", ordered[n // 2])],
        "median": [("unsorted_middle", values[n // 2]), ("mode_for_median", mode), ("largest_value", ordered[-1])],
        "range": [("largest_value", ordered[-1]), ("max_plus_min", ordered[-1] + ordered[0])],
    }[stat]
    question = f"{template.format(n=_WORDS[n])} {math(_list_text(values))}. Find the {stat} of these {noun}."
    steps = [("Write the values in order", _list_text(ordered))]
    if stat == "range":
        steps.append(("Largest value minus smallest value", f"{ordered[-1]} - {ordered[0]} = {ans}"))
    steps.append((f"The {stat}", str(ans)))
    return {
        "skill": "single_statistic",
        "question": question,
        "answer": math(str(ans)),
        "cands": _number_candidates(ans, [(c, Fraction(v)) for c, v in options]),
        "machine": {"task": stat, "values": values},
        "steps": steps,
        "marking": {"answer_type": "number_exact", "expected": [str(ans)]},
    }


def _level_stats_even(rng: SeededRandom) -> Dict[str, Any]:
    n = rng.choice((8, 10, 12))
    template, noun, lo, hi = rng.choice(_LIST_CONTEXTS)
    stat = rng.choice(("mean", "median", "mode", "range"))
    for _ in range(_MAX_ATTEMPTS):
        values, mode = _list_with_mode(rng, n, lo, hi)
        if stat != "mean" or sum(values) % n == 0:
            break
    else:
        raise GeneratorError("level 2 could not find a list with a whole-number mean")
    ordered = sorted(values)
    total = sum(values)
    mid_low, mid_high = ordered[n // 2 - 1], ordered[n // 2]
    median = Fraction(mid_low + mid_high, 2)
    ans = {"mean": Fraction(total, n), "median": median, "mode": Fraction(mode), "range": Fraction(ordered[-1] - ordered[0])}[stat]
    _require(ans == Fraction(statistics.mean(values) if stat == "mean" else statistics.median(values) if stat == "median" else statistics.mode(values) if stat == "mode" else max(values) - min(values)), "stat mismatch")
    options = {
        "mean": [("median_for_mean", median), ("forgot_divide", Fraction(total)), ("divide_n_minus_1", Fraction(total, n - 1)), ("mode_for_mean", Fraction(mode))],
        "median": [("lower_middle", Fraction(mid_low)), ("upper_middle", Fraction(mid_high)), ("mean_for_median", Fraction(total, n)), ("mode_for_median", Fraction(mode))],
        "mode": [("largest_value", Fraction(ordered[-1])), ("median_for_mode", median)],
        "range": [("largest_value", Fraction(ordered[-1])), ("max_plus_min", Fraction(ordered[-1] + ordered[0]))],
    }[stat]
    question = f"{template.format(n=_WORDS[n])} {math(_list_text(values))}. Find the {stat} of these {noun}."
    steps: List[Tuple[str, str]] = []
    if stat == "mean":
        steps = [("Add all the values", str(total)), ("Divide the total by the number of values", f"{total} / {n} = {_num_text(ans)}")]
    elif stat == "median":
        steps = [("Write the values in order", _list_text(ordered)), ("Add the two middle values and halve", f"({mid_low} + {mid_high}) / 2 = {_num_text(ans)}")]
    elif stat == "mode":
        steps = [("Write the values in order", _list_text(ordered)), ("The value that appears most often", str(mode))]
    else:
        steps = [("Write the values in order", _list_text(ordered)), ("Largest minus smallest", f"{ordered[-1]} - {ordered[0]} = {ans}")]
    return {
        "skill": "single_statistic",
        "question": question,
        "answer": math(_num_text(ans)),
        "cands": _number_candidates(ans, options),
        "machine": {"task": stat, "values": values},
        "steps": steps,
        "marking": {"answer_type": "number_exact", "expected": [_num_text(ans)] + ([_frac_text(ans)] if not ans.denominator == 1 and _num_text(ans) != _frac_text(ans) else [])},
    }


def _level_missing_value(rng: SeededRandom) -> Dict[str, Any]:
    for _ in range(_MAX_ATTEMPTS):
        n = rng.randint(4, 6)
        mean = rng.randint(8, 40)
        known = [max(1, mean + rng.randint(-12, 12)) for _ in range(n - 1)]
        x = n * mean - sum(known)
        if 1 <= x <= 2 * mean + 10 and x != mean:
            break
    else:
        raise GeneratorError("level 3 could not find a missing-value problem")
    shown = _list_text(known) + ", x"
    question = f"{_WORDS[n].capitalize()} numbers are {math(shown)}. Their mean is {math(str(mean))}. Find the value of {math('x')}."
    _require(Fraction(sum(known) + x, n) == mean, "mean does not match")
    options = [
        ("x_equals_mean", Fraction(mean)),
        ("used_n_minus_1", Fraction((n - 1) * mean - sum(known))),
        ("added_known", Fraction(n * mean + sum(known))),
        ("forgot_total", Fraction(mean - sum(known))),
    ]
    return {
        "skill": "missing_value_from_mean",
        "question": question,
        "answer": math(str(x)),
        "cands": _number_candidates(x, options),
        "machine": {"task": "missing_value", "known": known, "mean": mean, "x": x},
        "steps": [
            (f"Total of all {n} numbers = {n} x mean", str(n * mean)),
            ("Total of the known numbers", str(sum(known))),
            ("x = total - known total", str(x)),
        ],
        "marking": {"answer_type": "number_exact", "expected": [str(x)]},
    }


def _level_change_in_mean(rng: SeededRandom) -> Dict[str, Any]:
    for _ in range(_MAX_ATTEMPTS):
        n2 = rng.choice((5, 10))
        n = n2 - 1
        mean = rng.randint(40, 70)
        x = rng.randint(35, 90)
        new_mean = Fraction(n * mean + x, n2)
        if x != mean and new_mean != mean:
            break
    else:
        raise GeneratorError("level 4 could not find a change-in-mean problem")
    who = rng.choice(NAMES)
    question = (
        f"The mean mass of {n} learners in a Namibian under-16 rugby squad is {math(str(mean))} kg. "
        f"When {who} joins the squad, the mean mass of the {n2} learners is {math(_dec_text(new_mean))} kg. "
        f"Calculate {who}'s mass."
    )
    _require(Fraction(n * mean + x, n2) == new_mean, "new mean does not match")
    options = [
        ("used_n_both", Fraction(n * new_mean - n * mean)),
        ("new_mean_only", new_mean),
        ("difference_only", abs(new_mean - mean)),
        ("added_totals", Fraction(n2 * new_mean + n * mean)),
    ]
    return {
        "skill": "change_in_mean",
        "question": question,
        "answer": math(str(x)),
        "cands": _number_candidates(x, options),
        "machine": {"task": "change_in_mean", "n_before": n, "mean_before": mean, "n_after": n2, "mean_after": _dec_text(new_mean), "x": x},
        "steps": [
            (f"Total mass of the {n2} learners = {n2} x new mean", _dec_text(n2 * new_mean)),
            (f"Total mass of the original {n} learners = {n} x mean", str(n * mean)),
            ("New learner's mass = new total - old total", str(x)),
        ],
        "marking": {"answer_type": "number_exact", "expected": [str(x)]},
    }


class MeanMedianModeRangeGenerator(_StatGenerator):
    generator_id = "nssco_mean_median_mode_range"
    levels = (1, 2, 3, 4)
    error_notes = _MEAN_ERRORS
    level_skills = {1: ("single_statistic",), 2: ("single_statistic",), 3: ("missing_value_from_mean",), 4: ("change_in_mean",)}
    _builders = {1: _level_stats_odd, 2: _level_stats_even, 3: _level_missing_value, 4: _level_change_in_mean}


# ==========================================================================
# 2. Grouped data and estimating the mean
# ==========================================================================

_GROUP_CONTEXTS = (
    ("t", "time", "minutes", "The table shows the time, {var} minutes, that {n} learners took to walk to a school in Ongwediva.", 5),
    ("m", "mark", "", "The table shows the marks, {var}, of {n} learners in a Grade 11 mathematics test at a Walvis Bay school.", 0),
    ("h", "height", "cm", "The table shows the heights, {var} cm, of {n} recruits who joined the Namibian Police Band.", 150),
    ("d", "distance", "km", "The table shows the distances, {var} km, that {n} taxi drivers in Windhoek travelled in one day.", 10),
)
_NICE_N = (20, 25, 40, 50)

_GROUP_ERRORS: Dict[str, Dict[str, str]] = {
    "modal_class": {
        "second_highest": "named the class with the second largest frequency",
        "median_class": "named the class that contains the middle value instead of the class with the largest frequency",
        "neighbour_class": "named the class next to the one with the largest frequency",
    },
    "median_class": {
        "modal_class": "named the class with the largest frequency instead of the class holding the middle value",
        "middle_class_of_table": "named the middle row of the table without using the frequencies",
        "half_of_n_as_class": "named the class holding the value at position N, not N divided by 2",
    },
    "percentage_at_least": {
        "count_only": "gave the number of learners instead of a percentage",
        "percentage_below": "gave the percentage below the boundary instead of at or above it",
        "one_class_only": "gave the percentage for the single class next to the boundary",
    },
    "grouped_mean": {
        "lower_limits": "used the lower limit of each class instead of the midpoint",
        "divide_by_classes": "divided the total by the number of classes instead of the number of values",
        "mean_of_midpoints": "found the mean of the midpoints without multiplying by the frequencies",
        "upper_limits": "used the upper limit of each class instead of the midpoint",
        "fd_as_frequency": "used the frequency density as if it were the frequency",
        "freq_times_width": "multiplied each frequency by the class width instead of by the midpoint",
        "rounding": "did not round the answer as the question asked",
    },
}


def _equal_classes(rng: SeededRandom, k: int, start: int, width: int) -> List[Tuple[int, int]]:
    return [(start + i * width, start + (i + 1) * width) for i in range(k)]


def _split_total(rng: SeededRandom, total: int, k: int, floor: int = 1) -> List[int]:
    """k positive integers that add to ``total``."""
    parts = [floor] * k
    for _ in range(total - floor * k):
        parts[rng.randbelow(k)] += 1
    return parts


def _freq_table(var: str, classes: Sequence[Tuple[int, int]], freqs: Sequence[int], label: str) -> str:
    rows = [[_interval(lo, hi, var)[0], str(f)] for (lo, hi), f in zip(classes, freqs)]
    return math(_table([var, "\\text{Frequency}"], rows))


def _level_modal_class(rng: SeededRandom) -> Dict[str, Any]:
    var, noun, unit, intro, base = rng.choice(_GROUP_CONTEXTS)
    width = rng.choice((5, 10))
    k = rng.randint(4, 6)
    for _ in range(_MAX_ATTEMPTS):
        n = rng.choice(_NICE_N)
        freqs = _split_total(rng, n, k, floor=1)
        top = max(freqs)
        if freqs.count(top) == 1 and sorted(freqs)[-2] < top:
            break
    else:
        raise GeneratorError("level 1 could not find a unique modal class")
    start = base + rng.choice((0, 5, 10)) * (1 if base else 1)
    classes = _equal_classes(rng, k, start, width)
    mi = freqs.index(max(freqs))
    latex, plain = _interval(*classes[mi], var)
    median_class = _median_class_index(classes, freqs)
    order = sorted(range(k), key=lambda i: -freqs[i])
    second = order[1]
    opts: List[Candidate] = []
    for code, idx in (("second_highest", second), ("median_class", median_class), ("neighbour_class", mi + 1 if mi + 1 < k else mi - 1)):
        if idx != mi:
            lt, pl = _interval(*classes[idx], var)
            opts.append((code, math(lt), pl))
    question = f"{intro.format(var=var, n=n)} {_freq_table(var, classes, freqs, noun)} Write down the modal class."
    return {
        "skill": "modal_class",
        "question": question,
        "answer": math(latex),
        "cands": opts,
        "machine": {"task": "modal_class", "classes": [list(c) for c in classes], "freqs": freqs, "var": var},
        "steps": [("The largest frequency", str(freqs[mi])), ("The class with the largest frequency", plain)],
        "marking": {"answer_type": "graph_reading", "expected": [plain]},
    }


def _median_class_index(classes: Sequence[Tuple[int, int]], freqs: Sequence[int]) -> int:
    n = sum(freqs)
    pos = (n + 1) / 2
    running = 0
    for i, f in enumerate(freqs):
        running += f
        if running >= pos:
            return i
    raise GeneratorError("median not found")


def _level_median_or_percentage(rng: SeededRandom) -> Dict[str, Any]:
    var, noun, unit, intro, base = rng.choice(_GROUP_CONTEXTS)
    width = rng.choice((5, 10))
    k = rng.randint(4, 6)
    skill = rng.choice(("median_class", "percentage_at_least"))
    for _ in range(_MAX_ATTEMPTS):
        n = rng.choice(_NICE_N)
        freqs = _split_total(rng, n, k, floor=1)
        if skill == "median_class":
            # both middle positions must fall in the same class
            cum = list(itertools.accumulate(freqs))
            lo_pos, hi_pos = (n + 1) // 2, n // 2 + 1
            a = next(i for i, c in enumerate(cum) if c >= lo_pos)
            b = next(i for i, c in enumerate(cum) if c >= hi_pos)
            if a == b and a != freqs.index(max(freqs)):
                break
        else:
            cut = rng.randint(1, k - 1)
            above = sum(freqs[cut:])
            if above * 100 % n == 0 and above != n // 2:
                break
    else:
        raise GeneratorError("level 2 could not find a suitable table")
    start = base + rng.choice((0, 5, 10))
    classes = _equal_classes(rng, k, start, width)
    table = _freq_table(var, classes, freqs, noun)
    if skill == "median_class":
        idx = _median_class_index(classes, freqs)
        latex, plain = _interval(*classes[idx], var)
        cum = list(itertools.accumulate(freqs))
        mode_idx = freqs.index(max(freqs))
        opts = []
        for code, j in (("modal_class", mode_idx), ("middle_class_of_table", k // 2)):
            if j != idx:
                lt, pl = _interval(*classes[j], var)
                opts.append((code, math(lt), pl))
        wrong = next((i for i, c in enumerate(cum) if c >= n), None)
        if wrong is not None and wrong != idx:
            lt, pl = _interval(*classes[wrong], var)
            opts.append(("half_of_n_as_class", math(lt), pl))
        question = f"{intro.format(var=var, n=n)} {table} In which class does the median lie?"
        return {
            "skill": skill,
            "question": question,
            "answer": math(latex),
            "cands": opts,
            "machine": {"task": skill, "classes": [list(c) for c in classes], "freqs": freqs, "var": var},
            "steps": [
                (f"Position of the middle value = ({n} + 1) / 2", f"{(n + 1) / 2:g}"),
                ("Cumulative frequencies", _list_text(cum)),
                ("The class that first reaches that position", plain),
            ],
            "marking": {"answer_type": "graph_reading", "expected": [plain]},
        }
    boundary = classes[cut][0]
    pct = Fraction(above * 100, n)
    below_pct = 100 - pct
    class_pct = Fraction(freqs[cut] * 100, n)
    options = [("count_only", Fraction(above)), ("percentage_below", below_pct), ("one_class_only", class_pct)]
    question = (
        ''.join([format(intro.format(var=var, n=n), ''), ' ', format(table, ''), ' Work out the percentage of the ', format(n, ''), ' with ', format(math(var + ' \\ge ' + str(boundary)), ''), '.'])
    )
    return {
        "skill": skill,
        "question": question,
        "answer": math(str(pct.numerator)),
        "cands": _number_candidates(pct, options),
        "machine": {"task": skill, "classes": [list(c) for c in classes], "freqs": freqs, "var": var, "boundary": boundary},
        "steps": [
            (f"Number with {var} at least {boundary}", str(above)),
            ("Percentage = number / total x 100", f"{above} / {n} x 100 = {pct.numerator}"),
        ],
        "marking": {"answer_type": "number_exact", "expected": [str(pct.numerator)]},
    }


def _mean_problem(
    rng: SeededRandom,
    classes: Sequence[Tuple[int, int]],
    freqs: Sequence[int],
    var: str,
    intro: str,
    *,
    rounding: Tuple[str, int],
    table_markup: str,
    freq_shown: Sequence[Fraction] = (),
    skill: str = "grouped_mean",
    extra_cands: Sequence[Tuple[str, Fraction]] = (),
    note: str = "",
) -> Dict[str, Any]:
    n = sum(freqs)
    mids = [Fraction(lo + hi, 2) for lo, hi in classes]
    total = sum(f * m for f, m in zip(freqs, mids))
    mean = total / n
    mode, digits = rounding
    answer_text = _round(mean, mode, digits)
    k = len(classes)
    cands = [
        ("lower_limits", sum(f * lo for f, (lo, _) in zip(freqs, classes)) / n),
        ("upper_limits", sum(f * hi for f, (_, hi) in zip(freqs, classes)) / n),
        ("divide_by_classes", total / k),
        ("mean_of_midpoints", sum(mids) / k),
        ("freq_times_width", Fraction(sum(f * (hi - lo) for f, (lo, hi) in zip(freqs, classes)), n)),
    ] + list(extra_cands)
    out: List[Candidate] = []
    for code, value in cands:
        text = _round(Fraction(value), mode, digits)
        out.append((code, math(text), text))
    if mode == "sig_figs":
        how = f"Give your answer correct to {digits} significant figures." if digits != 1 else "Give your answer correct to 1 significant figure."
    elif digits == 0:
        how = "Give your answer to the nearest whole number."
    else:
        how = f"Give your answer correct to {digits} decimal place{'s' if digits > 1 else ''}."
    mid_text = ", ".join(_dec_text(m) for m in mids)
    fx = ", ".join(_dec_text(f * m) for f, m in zip(freqs, mids))
    return {
        "skill": skill,
        "question": f"{intro} {table_markup} Calculate an estimate of the mean. {how}",
        "answer": math(answer_text),
        "cands": out,
        "machine": {"task": skill, "classes": [list(c) for c in classes], "freqs": list(freqs), "var": var, "n": n, "exact_mean": _frac_text(mean)},
        "steps": [
            ("Midpoint of each class", mid_text),
            ("Frequency x midpoint for each class", fx),
            (f"Total of frequency x midpoint (the {n} values)", _dec_text(total)),
            (f"Estimate of the mean = total / {n}", answer_text),
        ],
        "marking": {"answer_type": "number_rounded", "expected": [answer_text], "rounding": mode, "digits": digits},
    }


def _level_mean_equal(rng: SeededRandom) -> Dict[str, Any]:
    var, noun, unit, intro, base = rng.choice(_GROUP_CONTEXTS)
    width = rng.choice((5, 10, 20)) if var in ("h", "m") else rng.choice((5, 10))
    k = rng.randint(4, 6)
    n = rng.choice(_NICE_N)
    freqs = _split_total(rng, n, k, floor=1)
    start = base + rng.choice((0, 5, 10, 20))
    classes = _equal_classes(rng, k, start, width)
    mode, digits = rng.choice((("sig_figs", 3), ("decimal_places", 1)))
    return _mean_problem(
        rng, classes, freqs, var, intro.format(var=var, n=n),
        rounding=(mode, digits), table_markup=_freq_table(var, classes, freqs, noun),
    )


_UNEQUAL_WIDTHS = ((5, 5, 10, 20), (10, 10, 20, 20, 40), (4, 4, 8, 16), (5, 10, 10, 25), (2, 3, 5, 10))


def _unequal_classes(rng: SeededRandom, start: int) -> List[Tuple[int, int]]:
    widths = rng.choice(_UNEQUAL_WIDTHS)
    classes, lo = [], start
    for w in widths:
        classes.append((lo, lo + w))
        lo += w
    return classes


def _level_mean_unequal(rng: SeededRandom) -> Dict[str, Any]:
    var, noun, unit, intro, base = rng.choice(_GROUP_CONTEXTS)
    classes = _unequal_classes(rng, rng.choice((0, 0, 5)))
    k = len(classes)
    n = rng.choice(_NICE_N)
    freqs = _split_total(rng, n, k, floor=1)
    mode, digits = rng.choice((("sig_figs", 3), ("decimal_places", 1), ("decimal_places", 0)))
    return _mean_problem(
        rng, classes, freqs, var, intro.format(var=var, n=n),
        rounding=(mode, digits), table_markup=_freq_table(var, classes, freqs, noun),
    )


def _level_mean_from_density(rng: SeededRandom) -> Dict[str, Any]:
    var, noun, unit, intro, base = rng.choice(_GROUP_CONTEXTS)
    for _ in range(_MAX_ATTEMPTS):
        classes = _unequal_classes(rng, rng.choice((0, 0, 5)))
        freqs = [rng.randint(2, 30) for _ in classes]
        densities = [Fraction(f, hi - lo) for f, (lo, hi) in zip(freqs, classes)]
        if all(_terminating(d) and len(_dec_text(d)) <= 6 for d in densities) and sum(freqs) >= 20:
            break
    else:
        raise GeneratorError("level 5 could not find a frequency-density table")
    n = sum(freqs)
    rows = [[_interval(lo, hi, var)[0], _dec_text(d)] for (lo, hi), d in zip(classes, densities)]
    markup = math(_table([var, "\\text{Frequency density}"], rows))
    mode, digits = rng.choice((("sig_figs", 3), ("decimal_places", 1)))
    mids = [Fraction(lo + hi, 2) for lo, hi in classes]
    fd_total = sum(d for d in densities)
    wrong_fd = sum(d * m for d, m in zip(densities, mids)) / fd_total
    problem = _mean_problem(
        rng, classes, freqs, var,
        intro.format(var=var, n="a group of").replace("a group of ", "a group of ").replace(" of  ", " of "),
        rounding=(mode, digits), table_markup=markup, extra_cands=[("fd_as_frequency", wrong_fd)],
    )
    problem["question"] = problem["question"].replace(
        "Calculate an estimate of the mean.",
        "The frequency density is frequency divided by class width. Calculate an estimate of the mean.",
    )
    problem["steps"] = [
        ("Frequency = frequency density x class width", _list_text(freqs)),
    ] + list(problem["steps"])
    problem["machine"]["densities"] = [_dec_text(d) for d in densities]
    return problem


class GroupedDataMeanGenerator(_StatGenerator):
    generator_id = "nssco_grouped_data_mean"
    levels = (1, 2, 3, 4, 5)
    error_notes = _GROUP_ERRORS
    level_skills = {
        1: ("modal_class",),
        2: ("median_class", "percentage_at_least"),
        3: ("grouped_mean",),
        4: ("grouped_mean",),
        5: ("grouped_mean",),
    }
    _builders = {1: _level_modal_class, 2: _level_median_or_percentage, 3: _level_mean_equal, 4: _level_mean_unequal, 5: _level_mean_from_density}


# ==========================================================================
# 3. Simple probability
# ==========================================================================

_COLOURS = ("red", "blue", "green", "white", "yellow", "black", "orange", "purple")
_WORD_BANK = ("WINDHOEK", "NAMIBIA", "SWAKOPMUND", "OSHAKATI", "KATIMA MULILO", "OKAHANDJA", "WALVIS BAY", "ONDANGWA", "KEETMANSHOOP", "RUNDU")
_PROB_ERRORS: Dict[str, Dict[str, str]] = {
    "count_objects": {
        "part_to_part": "compared the favourable outcomes with the other outcomes instead of with all outcomes",
        "forgot_total": "wrote the number of favourable outcomes over the number of favourable outcomes plus one",
        "complement": "gave the probability of the opposite event",
        "wrong_total": "used a total that left out one of the outcomes",
        "counted_one": "treated the colour that is not in the bag as if one of them were in it",
    },
    "numbers_and_letters": {
        "part_to_part": "compared the favourable outcomes with the other outcomes instead of with all outcomes",
        "complement": "gave the probability of the opposite event",
        "miscount_up": "counted one too many favourable outcomes",
        "miscount_down": "counted one too few favourable outcomes",
        "one_letter_only": "counted only one of the two letters asked for",
    },
    "two_way_table": {
        "row_total": "divided by the total of one row instead of by all the learners",
        "column_total": "divided by the total of one column instead of by all the learners",
        "complement": "gave the probability of the opposite event",
        "part_to_part": "compared the favourable outcomes with the other outcomes instead of with all outcomes",
    },
    "probability_total": {
        "sum_only": "added up the given probabilities and stopped",
        "added_instead": "added a probability to 1 instead of subtracting from 1",
        "given_probability": "gave the probability that was in the table instead of the opposite event",
        "percent_slip": "made a place-value slip when changing between decimals and percentages",
        "complement_of_one_class": "subtracted only one of the given probabilities from 1",
    },
    "expected_frequency": {
        "complement_times_n": "multiplied the number of trials by the probability of the opposite event",
        "divided": "divided the number of trials by the probability",
        "probability_times_denominator": "multiplied the fraction by its denominator instead of by the number of trials",
    },
    "two_dice": {
        "unordered_pairs": "counted each pair of scores once instead of both ways round",
        "over_six": "divided by 6 instead of by the 36 possible outcomes",
        "over_eleven": "divided by the 11 possible totals, as though they were equally likely",
        "complement": "gave the probability of the opposite event",
        "miscount_up": "counted one extra outcome",
    },
}


def _balls_level(rng: SeededRandom) -> Dict[str, Any]:
    k = rng.randint(3, 4)
    colours = _sample(rng, _COLOURS, k)
    counts = [rng.randint(1, 12) for _ in colours]
    total = sum(counts)
    kind = rng.choice(("one", "one", "two", "not", "impossible"))
    thing = rng.choice(("balls", "beads", "sweets", "marbles"))
    singular = thing[:-1]
    bag = ", ".join(f"{c} {colour}" for c, colour in zip(counts[:-1], colours[:-1])) + f" and {counts[-1]} {colours[-1]}"
    intro = f"A bag contains {bag} {thing}. One {singular} is taken at random. "
    steps: List[Tuple[str, str]] = [(f"Total number of {thing}", str(total))]
    if kind == "impossible":
        absent = next(c for c in ("black", "pink", "grey", "brown") if c not in colours)
        ans, q = Fraction(0), f"Find the probability that the {singular} is {absent}."
        options = [("part_to_part", Fraction(0))]
        steps.append((f"No {absent} {thing}", "0"))
        cands: List[Candidate] = []
        if total:
            cands = _prob_candidates(ans, [("counted_one", Fraction(1, total))])
    elif kind == "one":
        i = rng.randbelow(k)
        ans = Fraction(counts[i], total)
        q = f"Find the probability that the {singular} is {colours[i]}."
        steps.append((f"Number of {colours[i]} {thing}", str(counts[i])))
        cands = _prob_candidates(ans, [("part_to_part", Fraction(counts[i], total - counts[i])), ("forgot_total", Fraction(counts[i], counts[i] + 1)), ("complement", 1 - ans)])
    elif kind == "two":
        i, j = _sample(rng, list(range(k)), 2)
        ans = Fraction(counts[i] + counts[j], total)
        q = f"Find the probability that the {singular} is {colours[i]} or {colours[j]}."
        steps.append((f"Number that are {colours[i]} or {colours[j]}", str(counts[i] + counts[j])))
        cands = _prob_candidates(ans, [("part_to_part", Fraction(counts[i] + counts[j], total - counts[i] - counts[j])), ("complement", 1 - ans), ("wrong_total", Fraction(counts[i] + counts[j], total - 1))])
    else:
        i = rng.randbelow(k)
        ans = Fraction(total - counts[i], total)
        q = f"Find the probability that the {singular} is not {colours[i]}."
        steps.append((f"Number that are not {colours[i]}", str(total - counts[i])))
        cands = _prob_candidates(ans, [("complement", Fraction(counts[i], total)), ("part_to_part", Fraction(total - counts[i], counts[i])), ("wrong_total", Fraction(total - counts[i], total - 1))])
    steps.append(("Probability = favourable / total, in its simplest form", _frac_text(ans)))
    return {
        "skill": "count_objects",
        "question": intro + q,
        "answer": _prob_display(ans),
        "cands": cands,
        "machine": {"task": kind, "colours": colours, "counts": counts},
        "steps": steps,
        "marking": {"answer_type": "number_exact", "expected": _prob_expected(ans)},
    }


def _is_square(n: int) -> bool:
    return int(n**0.5) ** 2 == n


def _is_cube(n: int) -> bool:
    return round(n ** (1 / 3)) ** 3 == n


def _is_prime(n: int) -> bool:
    return n > 1 and all(n % p for p in range(2, int(n**0.5) + 1))


def _beads_properties(top: int) -> List[Tuple[str, Callable[[int], bool]]]:
    props: List[Tuple[str, Callable[[int], bool]]] = [
        ("a square number", _is_square),
        ("a prime number", _is_prime),
        ("a cube number", _is_cube),
        ("an even number", lambda n: n % 2 == 0),
    ]
    for m in (3, 4, 5, 6):
        props.append((f"a multiple of {m}", lambda n, m=m: n % m == 0))
    for k in (6, 9, 11):
        if k < top:
            props.append((f"less than {k}", lambda n, k=k: n < k))
    return props


def _numbers_and_letters_level(rng: SeededRandom) -> Dict[str, Any]:
    if rng.chance(1, 2):
        top = rng.choice((15, 20, 25, 30))
        name, pred = rng.choice(_beads_properties(top))
        favourable = [n for n in range(1, top + 1) if pred(n)]
        _require(0 < len(favourable) < top, "degenerate property")
        ans = Fraction(len(favourable), top)
        question = (
            f"A bag holds {top} beads numbered {math('1')} to {math(str(top))}. One bead is chosen at random. "
            f"Write down the probability that the number on it is {name}."
        )
        cands = _prob_candidates(ans, [
            ("part_to_part", Fraction(len(favourable), top - len(favourable))),
            ("complement", 1 - ans),
            ("miscount_up", Fraction(len(favourable) + 1, top)),
            ("miscount_down", Fraction(len(favourable) - 1, top)),
        ])
        steps = [
            (f"The numbers that are {name}", _list_text(favourable)),
            ("Probability = favourable / total, in its simplest form", _frac_text(ans)),
        ]
        machine = {"task": "beads", "top": top, "property": name, "favourable": favourable}
    else:
        word = rng.choice(_WORD_BANK)
        letters = [ch for ch in word if ch != " "]
        total = len(letters)
        distinct = sorted(set(letters))
        kind = rng.choice(("letter", "not_letter", "two_letters"))
        if kind == "letter":
            ch = rng.choice(distinct)
            fav = [c for c in letters if c == ch]
            q = f"Write down the probability that the card shows the letter {ch}."
        elif kind == "not_letter":
            ch = rng.choice(distinct)
            fav = [c for c in letters if c != ch]
            q = f"Write down the probability that the card does not show the letter {ch}."
        else:
            a, b = _sample(rng, distinct, 2)
            fav = [c for c in letters if c in (a, b)]
            q = f"Write down the probability that the card shows the letter {a} or the letter {b}."
        _require(0 < len(fav) < total, "degenerate letter event")
        ans = Fraction(len(fav), total)
        question = (
            f"Each letter of the word {word} is written on its own card (spaces are ignored). "
            f"The cards are placed face down and one card is chosen at random. {q}"
        )
        options = [
            ("part_to_part", Fraction(len(fav), total - len(fav))),
            ("miscount_up", Fraction(len(fav) + 1, total)),
            ("miscount_down", Fraction(len(fav) - 1, total)),
        ]
        if kind == "two_letters":
            options.append(("one_letter_only", Fraction(len([c for c in letters if c == a]), total)))
        else:
            options.append(("complement", 1 - ans))
        cands = _prob_candidates(ans, options)
        steps = [(f"Number of cards = number of letters in {word}", str(total)), ("Number of favourable cards", str(len(fav))), ("Probability in its simplest form", _frac_text(ans))]
        machine = {"task": "letters", "word": word, "kind": kind, "favourable": len(fav), "total": total}
    return {
        "skill": "numbers_and_letters",
        "question": question,
        "answer": _prob_display(ans),
        "cands": cands,
        "machine": machine,
        "steps": steps,
        "marking": {"answer_type": "number_exact", "expected": _prob_expected(ans)},
    }


def _two_way_level(rng: SeededRandom) -> Dict[str, Any]:
    if rng.chance(1, 2):
        rows_names, cols_names = ("Boys", "Girls"), ("Left-handed", "Right-handed")
        counts = [[rng.randint(1, 18), rng.randint(5, 25)], [rng.randint(1, 18), rng.randint(5, 25)]]
        intro = "The table shows the handedness of the learners in a Grade 10 class at a school in Rundu."
        noun = "learner"
    else:
        rows_names, cols_names = ("Male", "Female"), ("Botswana", "Zambia", "South Africa")
        counts = [[rng.randint(4, 24) for _ in cols_names] for _ in rows_names]
        intro = "Staff at a Windhoek school were asked which neighbouring country they would most like to visit."
        noun = "staff member"
    row_tot = [sum(r) for r in counts]
    col_tot = [sum(counts[r][c] for r in range(2)) for c in range(len(cols_names))]
    total = sum(row_tot)
    table = math(_table([""] + [f"\\text{{{c}}}" for c in cols_names], [[f"\\text{{{rows_names[r]}}}"] + [str(v) for v in counts[r]] for r in range(2)]))
    kind = rng.choice(("row", "column", "joint", "not_column"))
    r, c = rng.randbelow(2), rng.randbelow(len(cols_names))
    if kind == "row":
        fav, desc = row_tot[r], f"is {rows_names[r].lower()}" if rows_names[r] in ("Male", "Female") else f"is a {rows_names[r].lower()[:-1]}"
        wrong_den = col_tot[c]
    elif kind == "column":
        fav, desc = col_tot[c], f"chose {cols_names[c]}" if len(cols_names) == 3 else f"is {cols_names[c].lower()}"
        wrong_den = row_tot[r]
    elif kind == "joint":
        fav = counts[r][c]
        desc = (
            f"is {rows_names[r].lower()} and chose {cols_names[c]}"
            if len(cols_names) == 3
            else f"is a {cols_names[c].lower()} {rows_names[r].lower()[:-1]}"
        )
        wrong_den = row_tot[r]
    else:
        fav = total - col_tot[c]
        desc = f"did not choose {cols_names[c]}" if len(cols_names) == 3 else f"is not {cols_names[c].lower()}"
        wrong_den = col_tot[c]
    ans = Fraction(fav, total)
    _require(0 < fav < total, "degenerate two-way event")
    question = f"{intro} {table} One {noun} is chosen at random. Find the probability that the {noun} {desc}."
    cands = _prob_candidates(ans, [
        ("row_total", Fraction(fav, row_tot[r])),
        ("column_total", Fraction(fav, wrong_den)),
        ("complement", 1 - ans),
        ("part_to_part", Fraction(fav, total - fav)),
    ])
    return {
        "skill": "two_way_table",
        "question": question,
        "answer": _prob_display(ans),
        "cands": cands,
        "machine": {"task": "two_way", "counts": counts, "rows": list(rows_names), "cols": list(cols_names), "kind": kind, "r": r, "c": c, "favourable": fav, "total": total},
        "steps": [
            (f"Total number of {noun}s", str(total)),
            ("Number that fit the event", str(fav)),
            ("Probability in its simplest form", _frac_text(ans)),
        ],
        "marking": {"answer_type": "number_exact", "expected": _prob_expected(ans)},
    }


def _probability_totals_level(rng: SeededRandom) -> Dict[str, Any]:
    kind = rng.choice(("missing", "not_event", "expected"))
    if kind == "expected":
        den = rng.choice((3, 4, 5, 6, 8, 10))
        num = rng.randint(1, den - 1)
        p = Fraction(num, den)
        days = den * rng.randint(10, 40)
        ans = p * days
        question = (
            f"The probability that a minibus taxi from Oshakati arrives late is {math(number_latex(p))}. "
            f"The taxi makes the trip on {math(str(days))} days. Work out the number of days on which it is expected to arrive late."
        )
        cands = _number_candidates(ans, [
            ("complement_times_n", (1 - p) * days),
            ("divided", Fraction(days) / p),
            ("probability_times_denominator", Fraction(num * den)),
        ])
        return {
            "skill": "expected_frequency",
            "question": question,
            "answer": math(str(int(ans))),
            "cands": cands,
            "machine": {"task": "expected", "p": _frac_text(p), "n": days},
            "steps": [(f"Expected number = probability x number of days", f"{_frac_text(p)} x {days} = {int(ans)}")],
            "marking": {"answer_type": "number_exact", "expected": [str(int(ans))]},
        }
    k = rng.randint(3, 4)
    for _ in range(_MAX_ATTEMPTS):
        hundredths = [rng.randint(5, 45) for _ in range(k)]
        if sum(hundredths) == 100:
            break
        hundredths[-1] = 100 - sum(hundredths[:-1])
        if all(5 <= h <= 60 for h in hundredths):
            break
    else:
        raise GeneratorError("level 4 could not build a probability table")
    colours = _sample(rng, _COLOURS, k)
    probs = [Fraction(h, 100) for h in hundredths]
    _require(sum(probs) == 1, "probabilities do not total 1")
    if kind == "missing":
        i = rng.randbelow(k)
        shown = [("y" if j == i else _dec_text(probs[j])) for j in range(k)]
        rows = [[f"\\text{{{colours[j].capitalize()}}}", shown[j]] for j in range(k)]
        question = (
            ''.join(['A spinner has ', format(k, ''), ' coloured sections. The table shows the probability of each colour. ', format(math(_table(['\\text{Colour}', '\\text{Probability}'], rows)), ''), ' Find the value of ', format(math('y'), ''), '.'])
        )
        ans = probs[i]
        given_sum = 1 - ans
        cands = [
            ("sum_only", Fraction(given_sum)),
            ("added_instead", 1 + given_sum),
            ("complement_of_one_class", 1 - next(probs[j] for j in range(k) if j != i)),
            ("percent_slip", ans * 10),
        ]
        out = []
        for code, v in cands:
            if v == ans or v < 0 or v > 1:
                continue
            out.append((code, math(_dec_text(v)), _dec_text(v)))
        return {
            "skill": "probability_total",
            "question": question,
            "answer": math(_dec_text(ans)),
            "cands": out,
            "machine": {"task": "missing_probability", "probs": [_dec_text(p) for p in probs], "missing": i},
            "steps": [("The probabilities add up to 1, so y = 1 - the others", _dec_text(ans))],
            "marking": {"answer_type": "number_exact", "expected": [_dec_text(ans), _frac_text(ans), f"{hundredths[i]}%"]},
        }
    i = rng.randbelow(k)
    rows = [[f"\\text{{{colours[j].capitalize()}}}", _dec_text(probs[j])] for j in range(k)]
    ans = 1 - probs[i]
    question = (
        ''.join(['A spinner has ', format(k, ''), ' coloured sections. The table shows the probability of each colour. ', format(math(_table(['\\text{Colour}', '\\text{Probability}'], rows)), ''), ' Find the probability that the spinner does not land on ', format(colours[i], ''), '.'])
    )
    others = [probs[j] for j in range(k) if j != i]
    cands = [
        ("given_probability", probs[i]),
        ("complement_of_one_class", 1 - others[0]),
        ("percent_slip", ans / 10),
    ]
    out = []
    for code, v in cands:
        if v == ans or v < 0 or v > 1:
            continue
        out.append((code, math(_dec_text(v)), _dec_text(v)))
    return {
        "skill": "probability_total",
        "question": question,
        "answer": math(_dec_text(ans)),
        "cands": out,
        "machine": {"task": "not_event", "probs": [_dec_text(p) for p in probs], "index": i},
        "steps": [(f"P(not {colours[i]}) = 1 - P({colours[i]})", _dec_text(ans))],
        "marking": {"answer_type": "number_exact", "expected": [_dec_text(ans), _frac_text(ans), f"{int(ans * 100)}%"]},
    }


_DICE_EVENTS: Tuple[Tuple[str, Callable[[int, int], bool]], ...] = tuple(
    [(f"the difference between the scores (larger minus smaller) is {k}", lambda a, b, k=k: abs(a - b) == k) for k in (0, 1, 2, 3)]
    + [(f"the difference between the scores is less than {k}", lambda a, b, k=k: abs(a - b) < k) for k in (2, 3)]
    + [(f"the sum of the scores is {k}", lambda a, b, k=k: a + b == k) for k in (4, 5, 6, 7, 8, 9)]
    + [(f"the sum of the scores is more than {k}", lambda a, b, k=k: a + b > k) for k in (7, 8, 9)]
    + [(f"the difference between the scores is {k}", lambda a, b, k=k: abs(a - b) == k) for k in (4, 5)]
    + [(f"the difference between the scores is more than {k}", lambda a, b, k=k: abs(a - b) > k) for k in (1, 2, 3)]
    + [(f"the sum of the scores is {k}", lambda a, b, k=k: a + b == k) for k in (3, 10, 11)]
    + [(f"the sum of the scores is less than {k}", lambda a, b, k=k: a + b < k) for k in (5, 6, 7)]
    + [(f"the sum of the scores is at least {k}", lambda a, b, k=k: a + b >= k) for k in (10, 11)]
    + [("the product of the scores is odd", lambda a, b: (a * b) % 2 == 1), ("the larger score is 5 or more", lambda a, b: max(a, b) >= 5)]
    + [("the product of the scores is even", lambda a, b: (a * b) % 2 == 0), ("the two scores are the same", lambda a, b: a == b)]
)


def _two_dice_level(rng: SeededRandom) -> Dict[str, Any]:
    desc, pred = rng.choice(_DICE_EVENTS)
    outcomes = [(a, b) for a in range(1, 7) for b in range(1, 7)]
    fav = [o for o in outcomes if pred(*o)]
    _require(0 < len(fav) < 36, "degenerate dice event")
    ans = Fraction(len(fav), 36)
    unordered = len({tuple(sorted(o)) for o in fav})
    totals = len({a + b for a, b in outcomes})
    question = (
        f"Two fair dice, each numbered {math('1')} to {math('6')}, are thrown. "
        f"Write down the probability that {desc}. Give your answer as a fraction in its simplest form."
    )
    cands = _prob_candidates(ans, [
        ("unordered_pairs", Fraction(unordered, 36)),
        ("over_six", Fraction(len(fav), 6)),
        ("over_eleven", Fraction(1, totals)),
        ("complement", 1 - ans),
        ("miscount_up", Fraction(len(fav) + 1, 36)),
    ])
    return {
        "skill": "two_dice",
        "question": question,
        "answer": _prob_display(ans),
        "cands": cands,
        "machine": {"task": "two_dice", "event": desc, "favourable": len(fav)},
        "steps": [
            ("Total number of equally likely outcomes", "36"),
            ("Number of outcomes that fit the event, counting both orders", str(len(fav))),
            ("Probability in its simplest form", _frac_text(ans)),
        ],
        "marking": {"answer_type": "number_exact", "expected": _prob_expected(ans)},
    }


class SimpleProbabilityGenerator(_StatGenerator):
    generator_id = "nssco_simple_probability"
    levels = (1, 2, 3, 4, 5)
    error_notes = _PROB_ERRORS
    level_skills = {
        1: ("count_objects",),
        2: ("numbers_and_letters",),
        3: ("two_way_table",),
        4: ("probability_total", "expected_frequency"),
        5: ("two_dice",),
    }
    _builders = {1: _balls_level, 2: _numbers_and_letters_level, 3: _two_way_level, 4: _probability_totals_level, 5: _two_dice_level}


# ==========================================================================
# 4. Combined events and tree diagrams
# ==========================================================================

_PAIRS = (("red", "blue"), ("green", "white"), ("yellow", "black"), ("orange", "purple"))
_TREE_ERRORS: Dict[str, Dict[str, str]] = {
    "independent_events": {
        "added": "added the two probabilities instead of multiplying them",
        "wrong_branch": "used the probability of passing where the question asked about failing",
        "complement_of_product": "gave 1 minus the product",
        "pass_pass": "multiplied the two probabilities of passing whatever the question asked",
    },
    "without_replacement": {
        "with_replacement": "put the object back, so the second probability used the original total",
        "denominator_not_reduced": "kept the same top number for the second pick",
        "added": "added the two probabilities instead of multiplying them",
        "only_one_order": "counted only one order of the two colours",
        "complement_of_one_branch": "subtracted only one branch from 1",
        "first_only": "gave the probability of the first pick only",
    },
    "three_draws": {
        "with_replacement": "put each object back, so every pick used the original total",
        "denominator_not_reduced": "kept the same top number for the second and third picks",
        "complement_wrong_event": "worked out the probability of none and gave that as the answer",
        "added": "added the three probabilities instead of multiplying them",
    },
    "total_probability": {
        "one_branch_only": "used only one of the branches that lead to the event",
        "added_conditionals": "added the two conditional probabilities without multiplying by the branch probabilities",
        "joint_only": "gave only the probability of the first route",
        "complement_of_joint": "subtracted only one branch from 1",
        "swapped_branches": "multiplied each conditional probability by the wrong first-stage probability",
    },
}


def _pick_fraction(rng: SeededRandom) -> Fraction:
    den = rng.choice((3, 4, 5, 6, 8, 10))
    return Fraction(rng.randint(1, den - 1), den)


def _level_independent(rng: SeededRandom) -> Dict[str, Any]:
    for _ in range(_MAX_ATTEMPTS):
        a, b = _pick_fraction(rng), _pick_fraction(rng)
        if a != b:
            break
    who = rng.choice(NAMES)
    kind = rng.choice(("both_fail", "pass_fail", "fail_pass", "both_pass"))
    probs = {"both_fail": ((1 - a), (1 - b)), "pass_fail": (a, 1 - b), "fail_pass": (1 - a, b), "both_pass": (a, b)}[kind]
    ans = probs[0] * probs[1]
    text = {
        "both_fail": "fails both tests",
        "pass_fail": "passes the first test and fails the second test",
        "fail_pass": "fails the first test and passes the second test",
        "both_pass": "passes both tests",
    }[kind]
    question = (
        f"The probability that {who} passes a first driving test at a Windhoek driving school is {math(number_latex(a))}. "
        f"The probability that {who} passes a second test is {math(number_latex(b))}. The two tests are independent. "
        f"Calculate the probability that {who} {text}."
    )
    cands = _prob_candidates(ans, [
        ("added", probs[0] + probs[1]),
        ("pass_pass", a * b),
        ("wrong_branch", (1 - probs[0]) * (1 - probs[1]) if kind != "both_pass" else a * (1 - b)),
        ("complement_of_product", 1 - ans),
    ])
    return {
        "skill": "independent_events",
        "question": question,
        "answer": _prob_display(ans),
        "cands": cands,
        "machine": {"task": kind, "p_first": _frac_text(a), "p_second": _frac_text(b), "branches": [_frac_text(probs[0]), _frac_text(probs[1])]},
        "steps": [
            ("Probability for the first test", _frac_text(probs[0])),
            ("Probability for the second test", _frac_text(probs[1])),
            ("Multiply, because the tests are independent", _frac_text(ans)),
        ],
        "marking": {"answer_type": "number_exact", "expected": _prob_expected(ans)},
    }


def _bag(rng: SeededRandom, lo: int, hi: int) -> Tuple[Tuple[str, str], int, int, str]:
    colours = rng.choice(_PAIRS)
    r, b = rng.randint(2, 7), rng.randint(2, 7)
    while not lo <= r + b <= hi:
        r, b = rng.randint(2, 7), rng.randint(2, 7)
    thing = rng.choice(("marbles", "beads", "sweets"))
    return colours, r, b, thing


def _enumerate(items: Sequence[int], k: int, event: Callable[[Tuple[int, ...]], bool]) -> Fraction:
    """Exact probability by listing every ordered pick without replacement."""
    perms = list(itertools.permutations(range(len(items)), k))
    return Fraction(sum(1 for p in perms if event(tuple(items[i] for i in p))), len(perms))


def _bag_text(colours: Tuple[str, str], r: int, b: int, thing: str) -> str:
    return f"{r} {colours[0]} and {b} {colours[1]} {thing}"


def _level_two_draws(rng: SeededRandom) -> Dict[str, Any]:
    colours, r, b, thing = _bag(rng, 6, 12)
    n = r + b
    items = [0] * r + [1] * b
    skill_pick = rng.choice(("both_first", "both_second", "second_given_first"))
    intro = f"A bag contains {_bag_text(colours, r, b, thing)}. "
    if skill_pick == "second_given_first":
        ans = Fraction(r - 1, n - 1) if rng.chance(1, 2) else Fraction(r, n - 1)
        first_red = ans == Fraction(r - 1, n - 1)
        first = colours[0] if first_red else colours[1]
        question = (
            intro + f"Two {thing} are taken at random, one after the other, without replacement. "
            f"The first one is {first}. Write down the probability that the second one is {colours[0]}."
        )
        fav = r - 1 if first_red else r
        ans = Fraction(fav, n - 1)
        cands = _prob_candidates(ans, [
            ("with_replacement", Fraction(r, n)),
            ("denominator_not_reduced", Fraction(fav, n)),
            ("first_only", Fraction(r, n)),
        ])
        steps = [(f"{thing.capitalize()} left after the first is taken", str(n - 1)), (f"Number of {colours[0]} left", str(fav)), ("Probability", _frac_text(ans))]
        machine = {"task": "second_given_first", "r": r, "b": b, "first": first}
    else:
        want = 0 if skill_pick == "both_first" else 1
        c = (r, b)[want]
        ans = Fraction(c * (c - 1), n * (n - 1))
        ans_enum = _enumerate(items, 2, lambda p: p == (want, want))
        _require(ans == ans_enum, "two-draw enumeration mismatch")
        question = (
            intro + f"Two {thing} are taken at random, one after the other, without replacement. "
            f"Find the probability that both are {colours[want]}."
        )
        cands = _prob_candidates(ans, [
            ("with_replacement", Fraction(c, n) ** 2),
            ("denominator_not_reduced", Fraction(c, n) * Fraction(c - 1, n)),
            ("added", Fraction(c, n) + Fraction(c - 1, n - 1)),
            ("first_only", Fraction(c, n)),
        ])
        steps = [
            (f"P(first is {colours[want]})", _frac_text(Fraction(c, n))),
            (f"P(second is {colours[want]} | first was)", _frac_text(Fraction(c - 1, n - 1))),
            ("Multiply the two probabilities", _frac_text(ans)),
        ]
        machine = {"task": "both_same", "r": r, "b": b, "want": want}
    return {
        "skill": "without_replacement",
        "question": question,
        "answer": _prob_display(ans),
        "cands": cands,
        "machine": machine,
        "steps": steps,
        "marking": {"answer_type": "number_exact", "expected": _prob_expected(ans)},
    }


def _level_one_of_each(rng: SeededRandom) -> Dict[str, Any]:
    colours, r, b, thing = _bag(rng, 6, 12)
    n = r + b
    items = [0] * r + [1] * b
    kind = rng.choice(("one_each", "at_least_one"))
    intro = f"A bag contains {_bag_text(colours, r, b, thing)}. Two {thing} are taken at random, one after the other, without replacement. "
    if kind == "one_each":
        ans = Fraction(2 * r * b, n * (n - 1))
        _require(ans == _enumerate(items, 2, lambda p: p[0] != p[1]), "one-each enumeration mismatch")
        question = intro + f"Find the probability that one is {colours[0]} and one is {colours[1]}."
        one_order = Fraction(r * b, n * (n - 1))
        cands = _prob_candidates(ans, [
            ("only_one_order", one_order),
            ("with_replacement", Fraction(2 * r * b, n * n)),
            ("added", Fraction(r, n) + Fraction(b, n - 1)),
            ("complement_of_one_branch", 1 - one_order),
        ])
        steps = [
            (f"P({colours[0]} then {colours[1]})", _frac_text(one_order)),
            (f"P({colours[1]} then {colours[0]})", _frac_text(one_order)),
            ("Add the two routes", _frac_text(ans)),
        ]
    else:
        want = rng.randint(0, 1)
        c = (r, b)[want]
        other = n - c
        none = Fraction(other * (other - 1), n * (n - 1))
        ans = 1 - none
        _require(ans == _enumerate(items, 2, lambda p: want in p), "at-least-one enumeration mismatch")
        question = intro + f"Find the probability that at least one of the {thing} is {colours[want]}."
        cands = _prob_candidates(ans, [
            ("complement_of_one_branch", 1 - Fraction(other, n)),
            ("with_replacement", 1 - Fraction(other, n) ** 2),
            ("first_only", Fraction(c, n)),
            ("added", Fraction(c, n) + Fraction(c, n - 1)),
        ])
        steps = [
            (f"P(neither is {colours[want]})", _frac_text(none)),
            ("P(at least one) = 1 - P(none)", _frac_text(ans)),
        ]
        one_order = None
    return {
        "skill": "without_replacement",
        "question": question,
        "answer": _prob_display(ans),
        "cands": cands,
        "machine": {"task": kind, "r": r, "b": b, **({"want": want} if kind == "at_least_one" else {})},
        "steps": steps,
        "marking": {"answer_type": "number_exact", "expected": _prob_expected(ans)},
    }


def _level_three_draws(rng: SeededRandom) -> Dict[str, Any]:
    kind = rng.choice(("all_three", "at_least_one"))
    for _ in range(_MAX_ATTEMPTS):
        colours, r, b, thing = _bag(rng, 7, 12)
        want = rng.randint(0, 1)
        c = (r, b)[want]
        if c >= 3 and (r + b - c) >= 3:
            break
    else:
        raise GeneratorError("level 4 could not find a three-draw bag")
    n = r + b
    items = [0] * r + [1] * b
    other = n - c
    intro = f"A bag contains {_bag_text(colours, r, b, thing)}. Three {thing} are taken at random, one after the other, without replacement. "
    if kind == "all_three":
        _require(c >= 3, "not enough of one colour")
        ans = Fraction(c * (c - 1) * (c - 2), n * (n - 1) * (n - 2))
        _require(ans == _enumerate(items, 3, lambda p: p == (want, want, want)), "three-draw enumeration mismatch")
        question = intro + f"Find the probability that all three are {colours[want]}."
        cands = _prob_candidates(ans, [
            ("with_replacement", Fraction(c, n) ** 3),
            ("denominator_not_reduced", Fraction(c * (c - 1) * (c - 2), n**3)),
            ("added", Fraction(c, n) + Fraction(c - 1, n - 1) + Fraction(c - 2, n - 2)),
        ])
        steps = [
            ("First pick", _frac_text(Fraction(c, n))),
            ("Second pick", _frac_text(Fraction(c - 1, n - 1))),
            ("Third pick", _frac_text(Fraction(c - 2, n - 2))),
            ("Multiply the three probabilities", _frac_text(ans)),
        ]
    else:
        _require(other >= 3, "not enough of the other colour")
        none = Fraction(other * (other - 1) * (other - 2), n * (n - 1) * (n - 2))
        ans = 1 - none
        _require(ans == _enumerate(items, 3, lambda p: want in p), "three-draw at-least-one mismatch")
        question = intro + f"Find the probability that at least one of the three {thing} is {colours[want]}."
        cands = _prob_candidates(ans, [
            ("complement_wrong_event", none),
            ("with_replacement", 1 - Fraction(other, n) ** 3),
            ("denominator_not_reduced", 1 - Fraction(other * (other - 1) * (other - 2), n**3)),
        ])
        steps = [
            (f"P(none is {colours[want]})", _frac_text(none)),
            ("P(at least one) = 1 - P(none)", _frac_text(ans)),
        ]
    return {
        "skill": "three_draws",
        "question": question,
        "answer": _prob_display(ans),
        "cands": cands,
        "machine": {"task": kind, "r": r, "b": b, "want": want},
        "steps": steps,
        "marking": {"answer_type": "number_exact", "expected": _prob_expected(ans)},
    }


_ROUTES = (("cycles", "walks", "bicycle", "on foot"), ("takes the bus", "walks", "bus", "on foot"), ("is driven", "cycles", "car", "bicycle"))


def _level_total_probability(rng: SeededRandom) -> Dict[str, Any]:
    for _ in range(_MAX_ATTEMPTS):
        p = _pick_fraction(rng)
        q1, q2 = _pick_fraction(rng), _pick_fraction(rng)
        if q1 != q2 and p != Fraction(1, 2):
            break
    first, second, mode1, mode2 = rng.choice(_ROUTES)
    who = rng.choice(NAMES)
    joint = p * q1
    late = p * q1 + (1 - p) * q2
    kind = rng.choice(("joint_late", "total_late", "not_late"))
    intro = (
        f"On a school day, {who} {first} to school with probability {math(number_latex(p))} and otherwise {second}. "
        f"When {who} {first}, the probability of being late is {math(number_latex(q1))}. "
        f"When {who} {second}, the probability of being late is {math(number_latex(q2))}. "
    )
    if kind == "joint_late":
        ans = joint
        question = intro + f"Calculate the probability that {who} {first} and is late."
        cands = _prob_candidates(ans, [("added_conditionals", q1 + q2), ("swapped_branches", (1 - p) * q1), ("complement_of_joint", 1 - ans), ("one_branch_only", q1)])
        steps = [(f"P({first}) x P(late | {first})", f"{_frac_text(p)} x {_frac_text(q1)} = {_frac_text(ans)}")]
    elif kind == "total_late":
        ans = late
        question = intro + f"Calculate the probability that {who} is late."
        cands = _prob_candidates(ans, [("joint_only", joint), ("added_conditionals", q1 + q2), ("swapped_branches", (1 - p) * q1 + p * q2), ("one_branch_only", (1 - p) * q2)])
        steps = [
            (f"Route 1: {first} and late", _frac_text(joint)),
            (f"Route 2: {second} and late", _frac_text((1 - p) * q2)),
            ("Add the two routes", _frac_text(ans)),
        ]
    else:
        ans = 1 - late
        question = intro + f"Calculate the probability that {who} is not late."
        cands = _prob_candidates(ans, [("complement_of_joint", 1 - joint), ("joint_only", late), ("swapped_branches", 1 - ((1 - p) * q1 + p * q2)), ("one_branch_only", 1 - (1 - p) * q2)])
        steps = [
            (f"P(late) = P({first} and late) + P({second} and late)", _frac_text(late)),
            ("P(not late) = 1 - P(late)", _frac_text(ans)),
        ]
    # exact check: enumerate the four routes
    routes = {("a", "l"): p * q1, ("a", "n"): p * (1 - q1), ("b", "l"): (1 - p) * q2, ("b", "n"): (1 - p) * (1 - q2)}
    _require(sum(routes.values()) == 1, "routes do not total 1")
    _require(ans == {"joint_late": routes[("a", "l")], "total_late": routes[("a", "l")] + routes[("b", "l")], "not_late": routes[("a", "n")] + routes[("b", "n")]}[kind], "route mismatch")
    return {
        "skill": "total_probability",
        "question": question,
        "answer": _prob_display(ans),
        "cands": cands,
        "machine": {"task": kind, "p": _frac_text(p), "q1": _frac_text(q1), "q2": _frac_text(q2)},
        "steps": steps,
        "marking": {"answer_type": "number_exact", "expected": _prob_expected(ans)},
    }


class TreeDiagramsGenerator(_StatGenerator):
    generator_id = "nssco_tree_diagrams"
    levels = (1, 2, 3, 4, 5)
    error_notes = {
        "independent_events": _TREE_ERRORS["independent_events"],
        "without_replacement": _TREE_ERRORS["without_replacement"],
        "three_draws": _TREE_ERRORS["three_draws"],
        "total_probability": _TREE_ERRORS["total_probability"],
    }
    level_skills = {
        1: ("independent_events",),
        2: ("without_replacement",),
        3: ("without_replacement",),
        4: ("three_draws",),
        5: ("total_probability",),
    }
    _builders = {1: _level_independent, 2: _level_two_draws, 3: _level_one_of_each, 4: _level_three_draws, 5: _level_total_probability}


# ==========================================================================
# 5. Cumulative frequency, read from a table
# ==========================================================================

_CF_CONTEXTS = (
    ("m", "marks", "The table shows the marks, {var}, that {n} learners scored in a Grade 11 science test at an Otjiwarongo school.", 0),
    ("t", "minutes", "The table shows the time, {var} minutes, that {n} customers waited in a Windhoek bank.", 0),
    ("d", "distance", "The table shows the distance, {var} km, that {n} learners travel to school in the Kavango region.", 0),
    ("w", "mass", "The table shows the mass, {var} kg, of {n} bags of maize meal packed at a Mariental mill.", 40),
)
_CF_ERRORS: Dict[str, Dict[str, str]] = {
    "complete_cumulative": {
        "frequencies_copied": "wrote the frequencies again instead of running totals",
        "skipped_class": "left one frequency out of the running total",
        "reverse_total": "added the frequencies starting from the last class",
    },
    "frequencies_from_cumulative": {
        "cumulative_copied": "wrote the cumulative frequencies again instead of the frequency of each class",
        "wrong_difference": "subtracted the wrong pair of cumulative frequencies",
        "forgot_first": "subtracted from zero for the first class instead of keeping its value",
    },
    "count_from_cumulative": {
        "total_minus_wrong": "subtracted from the total using the wrong boundary",
        "forgot_subtract": "gave the cumulative frequency where a difference was needed",
        "off_by_class": "used the cumulative frequency of the neighbouring boundary",
    },
    "quartile_work": {
        "added_quartiles": "added the quartiles instead of subtracting",
        "wrong_quartiles": "subtracted the median from the upper quartile",
        "median_minus_lower": "subtracted the lower quartile from the median instead of from the upper quartile",
        "next_class": "named the class after the one that reaches the middle value",
        "previous_class": "named the class before the one that reaches the middle value",
        "modal_class": "named the class with the largest frequency instead of the class holding the middle value",
    },
}


def _cf_setup(rng: SeededRandom, k_lo: int = 4, k_hi: int = 6) -> Tuple[str, str, str, int, List[Tuple[int, int]], List[int], List[int]]:
    var, unit, intro, base = rng.choice(_CF_CONTEXTS)
    width = rng.choice((10, 20)) if var != "w" else rng.choice((5, 10))
    k = rng.randint(k_lo, k_hi)
    start = base
    classes = [(start + i * width, start + (i + 1) * width) for i in range(k)]
    freqs = [rng.randint(3, 60) for _ in range(k)]
    cum = list(itertools.accumulate(freqs))
    return var, unit, intro, base, classes, freqs, cum


def _cf_boundaries(classes: Sequence[Tuple[int, int]], var: str, cum: Sequence[int]) -> str:
    rows = [[f"{var} < {hi}", str(c)] for (lo, hi), c in zip(classes, cum)]
    return math(_table([var, "\\text{Cumulative frequency}"], rows))


def _cf_freq_table(classes: Sequence[Tuple[int, int]], var: str, freqs: Sequence[int]) -> str:
    rows = [[_interval(lo, hi, var)[0], str(f)] for (lo, hi), f in zip(classes, freqs)]
    return math(_table([var, "\\text{Frequency}"], rows))


def _list_marking(values: Sequence[int]) -> Dict[str, Any]:
    return {"answer_type": "table_values", "expected": [_list_text(values)]}


def _level_complete_cumulative(rng: SeededRandom) -> Dict[str, Any]:
    var, unit, intro, base, classes, freqs, cum = _cf_setup(rng)
    n = cum[-1]
    question = (
        f"{intro.format(var=var, n=n)} {_cf_freq_table(classes, var, freqs)} "
        f"Complete the cumulative frequency column. Write the {len(cum)} cumulative frequencies in order, starting with the first class."
    )
    wrong_skip = list(itertools.accumulate(freqs[:1] + freqs[2:]))
    reverse = list(itertools.accumulate(reversed(freqs)))
    cands = []
    for code, vals in (("frequencies_copied", freqs), ("skipped_class", wrong_skip + [wrong_skip[-1]]), ("reverse_total", reverse)):
        if list(vals) != cum and len(vals) == len(cum):
            cands.append((code, math(_list_text(vals)), _list_text(vals)))
    return {
        "skill": "complete_cumulative",
        "question": question,
        "answer": math(_list_text(cum)),
        "cands": cands,
        "machine": {"task": "complete_cumulative", "classes": [list(c) for c in classes], "freqs": freqs, "cum": cum, "var": var},
        "steps": [(f"Running total up to class {i + 1}", str(c)) for i, c in enumerate(cum)],
        "marking": _list_marking(cum),
    }


def _level_frequencies_from_cumulative(rng: SeededRandom) -> Dict[str, Any]:
    var, unit, intro, base, classes, freqs, cum = _cf_setup(rng)
    n = cum[-1]
    question = (
        f"{intro.format(var=var, n=n)} {_cf_boundaries(classes, var, cum)} "
        f"Work out the frequency of each class. Write the {len(freqs)} frequencies in order, starting with the lowest class."
    )
    diff_wrong = [cum[0]] + [cum[i] - cum[i - 2] if i >= 2 else cum[i] for i in range(1, len(cum))]
    zero_wrong = [cum[0] - 0] + [cum[i] - cum[i - 1] for i in range(1, len(cum))]
    forgot_first = [cum[i] - (cum[i - 1] if i else cum[0]) for i in range(len(cum))]
    cands = []
    for code, vals in (("cumulative_copied", cum), ("wrong_difference", diff_wrong), ("forgot_first", forgot_first)):
        if list(vals) != freqs:
            cands.append((code, math(_list_text(vals)), _list_text(vals)))
    _require(zero_wrong == freqs, "frequencies from cumulative mismatch")
    return {
        "skill": "frequencies_from_cumulative",
        "question": question,
        "answer": math(_list_text(freqs)),
        "cands": cands,
        "machine": {"task": "frequencies_from_cumulative", "classes": [list(c) for c in classes], "freqs": freqs, "cum": cum, "var": var},
        "steps": [("First class = first cumulative frequency", str(cum[0]))] + [(f"Class {i + 1} = {cum[i]} - {cum[i - 1]}", str(freqs[i])) for i in range(1, len(freqs))],
        "marking": _list_marking(freqs),
    }


def _level_counts(rng: SeededRandom) -> Dict[str, Any]:
    var, unit, intro, base, classes, freqs, cum = _cf_setup(rng, 5, 6)
    n = cum[-1]
    bounds = [hi for _, hi in classes]
    kind = rng.choice(("less_than", "at_least", "between"))
    table = _cf_boundaries(classes, var, cum)
    cum_at = dict(zip(bounds, cum))
    if kind == "less_than":
        b = rng.choice(bounds[:-1])
        ans = cum_at[b]
        q = f"How many {unit_noun(unit)} had {math(var + ' < ' + str(b))}?"
        steps = [(f"Cumulative frequency at {var} < {b}", str(ans))]
        options = [("forgot_subtract", n - ans), ("off_by_class", cum_at[bounds[bounds.index(b) + 1]])]
    elif kind == "at_least":
        b = rng.choice(bounds[:-1])
        ans = n - cum_at[b]
        q = ''.join(['How many ', format(unit_noun(unit), ''), ' had ', format(math(var + ' \\ge ' + str(b)), ''), '?'])
        steps = [("Total", str(n)), (f"Cumulative frequency at {var} < {b}", str(cum_at[b])), ("Total minus the number below", str(ans))]
        options = [("forgot_subtract", cum_at[b]), ("total_minus_wrong", n - cum_at[bounds[bounds.index(b) + 1]]), ("off_by_class", n - cum_at[bounds[bounds.index(b) - 1]] if bounds.index(b) else n)]
    else:
        i, j = sorted(_sample(rng, list(range(len(bounds) - 1)), 2))
        lo_b, hi_b = bounds[i], bounds[j]
        ans = cum[j] - cum[i]
        q = ''.join(['How many ', format(unit_noun(unit), ''), ' had ', format(math(str(lo_b) + ' \\le ' + var + ' < ' + str(hi_b)), ''), '?'])
        steps = [(f"Cumulative frequency at {var} < {hi_b}", str(cum[j])), (f"Cumulative frequency at {var} < {lo_b}", str(cum[i])), ("Subtract", str(ans))]
        options = [("forgot_subtract", cum[j]), ("total_minus_wrong", n - cum[j]), ("off_by_class", cum[j + 1] - cum[i])]
    question = f"{intro.format(var=var, n=n)} {table} {q}"
    cands = _number_candidates(ans, [(c, Fraction(v)) for c, v in options])
    return {
        "skill": "count_from_cumulative",
        "question": question,
        "answer": math(str(ans)),
        "cands": cands,
        "machine": {"task": kind, "classes": [list(c) for c in classes], "freqs": freqs, "cum": cum, "var": var, "n": n},
        "steps": steps,
        "marking": {"answer_type": "number_exact", "expected": [str(ans)]},
    }


def unit_noun(unit: str) -> str:
    return {"marks": "learners", "minutes": "customers", "distance": "learners", "mass": "bags"}[unit]


def _level_quartile_work(rng: SeededRandom) -> Dict[str, Any]:
    kind = rng.choice(("iqr", "median_class"))
    if kind == "iqr":
        who = rng.choice(("runners", "cyclists"))
        lq = rng.randint(15, 60)
        uq = lq + rng.randint(15, 50)
        med = rng.randint(lq + 4, uq - 4)
        ans = uq - lq
        question = (
            f"A cumulative frequency graph of the times, in minutes, taken by {who} to finish a race in Swakopmund gives a lower quartile of "
            f"{math(str(lq))}, a median of {math(str(med))} and an upper quartile of {math(str(uq))}. Find the interquartile range."
        )
        cands = _number_candidates(ans, [("added_quartiles", Fraction(lq + uq)), ("wrong_quartiles", Fraction(uq - med)), ("median_minus_lower", Fraction(med - lq))])
        return {
            "skill": "quartile_work",
            "question": question,
            "answer": math(str(ans)),
            "cands": cands,
            "machine": {"task": "iqr", "lq": lq, "median": med, "uq": uq},
            "steps": [("Interquartile range = upper quartile - lower quartile", f"{uq} - {lq} = {ans}")],
            "marking": {"answer_type": "number_exact", "expected": [str(ans)]},
        }
    for _ in range(_MAX_ATTEMPTS):
        var, unit, intro, base, classes, freqs, cum = _cf_setup(rng, 5, 6)
        n = cum[-1]
        if n % 2 or n // 2 in cum or n // 2 + 1 in cum:
            continue
        idx = next(i for i, c in enumerate(cum) if c >= n / 2)
        if 0 < idx < len(classes) - 1 and idx != freqs.index(max(freqs)):
            break
    else:
        raise GeneratorError("level 4 could not find a median-class problem")
    latex, plain = _interval(*classes[idx], var)
    table = _cf_boundaries(classes, var, cum)
    question = f"{intro.format(var=var, n=n)} {table} In which class does the median lie?"
    options = [
        ("next_class", classes[idx + 1]),
        ("previous_class", classes[idx - 1]),
        ("modal_class", classes[freqs.index(max(freqs))]),
    ]
    cands = []
    for code, cls in options:
        lt, pl = _interval(*cls, var)
        if pl != plain:
            cands.append((code, math(lt), pl))
    # a class is chosen from the cumulative column, so the boundary-class text must be well formed
    return {
        "skill": "quartile_work",
        "question": question,
        "answer": math(latex),
        "cands": cands,
        "machine": {"task": "median_class", "classes": [list(c) for c in classes], "freqs": freqs, "cum": cum, "var": var, "n": n},
        "steps": [(f"Position of the median = {n} / 2", str(n // 2)), ("First cumulative frequency to reach that position", str(cum[idx])), ("The class", plain)],
        "marking": {"answer_type": "graph_reading", "expected": [plain]},
    }


class CumulativeFrequencyReadingGenerator(_StatGenerator):
    generator_id = "nssco_cumulative_frequency_reading"
    levels = (1, 2, 3, 4)
    error_notes = {
        "complete_cumulative": _CF_ERRORS["complete_cumulative"],
        "frequencies_from_cumulative": _CF_ERRORS["frequencies_from_cumulative"],
        "count_from_cumulative": _CF_ERRORS["count_from_cumulative"],
        "quartile_work": _CF_ERRORS["quartile_work"],
    }
    level_skills = {
        1: ("complete_cumulative",),
        2: ("frequencies_from_cumulative",),
        3: ("count_from_cumulative",),
        4: ("quartile_work",),
    }
    _builders = {1: _level_complete_cumulative, 2: _level_frequencies_from_cumulative, 3: _level_counts, 4: _level_quartile_work}


GENERATORS = [
    MeanMedianModeRangeGenerator(),
    GroupedDataMeanGenerator(),
    SimpleProbabilityGenerator(),
    TreeDiagramsGenerator(),
    CumulativeFrequencyReadingGenerator(),
]
