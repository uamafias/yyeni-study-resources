"""Shared conformance gates for generated problems (no database or model calls)."""
from __future__ import annotations

import re
from collections import Counter
from time import monotonic

from services.math_marking import check
from services.math_marking.grading_contract import build_contract
from . import generate_problem, get_generator


def validate_problem(p):
    assert p.question.strip() and p.answer.strip(), "empty question or answer"
    # A mathematically checkable answer is insufficient without a valid,
    # instance-bound marking memo. This gate does not approve its draft tariff.
    build_contract(p)
    assert not re.search(r"\*\*|__|(?<!\$)\*[^*\s]",p.question.replace("$$","")), "Markdown emphasis"
    assert re.sub(r"(?<=[A-Za-z0-9])\$(?=\d)","",p.question).count("$")%2==0, "unbalanced maths delimiters"
    assert p.steps and all(s.description and s.value for s in p.steps), "missing model working"
    assert all(d.answer != p.answer for d in p.distractors), "correct answer listed as mistake"
    assert len({d.answer for d in p.distractors})==len(p.distractors), "duplicate distractors"
    m=p.marking
    assert m.get("answer_type") and m.get("expected") and m.get("typed"), "missing marking metadata"
    kw={k:m[k] for k in ("rounding","digits","form") if k in m}
    verdict=check(m["answer_type"],m["expected"],m["typed"],**kw)
    assert verdict.correct or verdict.needs_judge, f"own answer rejected: {verdict.reason}"
    last=p.steps[-1]
    assert last.answer_type==m["answer_type"], "final working step has no answer type"
    terminal=check(m["answer_type"],m["expected"],last.value,**kw)
    assert terminal.correct or terminal.needs_judge, "working does not finish at the required answer"
    for d in p.distractors:
        if d.typed:
            assert not check(m["answer_type"],m["expected"],d.typed,**kw).correct, f"accepted distractor: {d.error_code}"
    return verdict.needs_judge


def audit_level(case):
    gid,level,count=case
    start=monotonic(); fingerprints=set(); skills=Counter(); judge=0; failures=[]; failed=0
    for seed in range(count):
        try:
            p=generate_problem(gid,seed,level)
            assert p==generate_problem(gid,seed,level), "not deterministic"
            judge+=int(validate_problem(p))
            fingerprints.add(p.fingerprint); skills[p.skill]+=1
        except Exception as exc:
            failed+=1
            if len(failures)<10:
                failures.append({"seed":seed,"error":f"{type(exc).__name__}: {exc}"})
    if count >= 300 and len(fingerprints)<20 and failed==0:
        failed+=1; failures.append({"seed":None,"error":f"only {len(fingerprints)} distinct questions"})
    return {"generator_id":gid,"version":get_generator(gid).version,"level":level,
            "seeds_attempted":count,"distinct_questions":len(fingerprints),"judge_only":judge,
            "skills":dict(skills),"failed":failed,"failures":failures,"seconds":round(monotonic()-start,3)}
