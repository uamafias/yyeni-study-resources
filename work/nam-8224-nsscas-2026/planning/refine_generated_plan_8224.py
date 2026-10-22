#!/usr/bin/env python3
"""Apply Chemistry-specific refinements after the standard plan generators.

The shared generator deliberately stays qualification-neutral.  This script
keeps the few 8224 decisions that its schema cannot yet express reproducible:
bounded practical-note volume and fully labelled performance-task slots.
"""
from __future__ import annotations

import importlib.util
import json
import math
import os
import re


HERE = os.path.dirname(os.path.abspath(__file__))
WS = os.path.dirname(HERE)
ROOT = os.path.dirname(os.path.dirname(WS))


def load(path):
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)


def write(path, value):
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(value, fh, indent=1, ensure_ascii=False)
        fh.write("\n")


def load_renderer():
    path = os.path.join(ROOT, "standard", "v0.2.0-draft", "build", "make_work_order.py")
    spec = importlib.util.spec_from_file_location("make_work_order_8224_renderer", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.as_markdown


registry = load(os.path.join(WS, "curriculum", "objective_registry.json"))["objectives"]
by_topic = {}
topic_titles = {}
for objective in registry:
    if objective.get("parent_id"):
        by_topic.setdefault(objective["topic_id"], []).append(objective)
    else:
        topic_titles[objective["topic_id"]] = objective["learner_objective"].split(" (syllabus topic")[0]

adjacency = {
    "1.1": ["1.2", "1.4"], "1.2": ["1.1", "1.3", "3.1"],
    "1.3": ["1.2", "3.1", "4.1"], "1.4": ["1.1"],
    "2.1": ["2.3", "2.4"], "2.2": ["3.1", "3.3", "3.4"],
    "2.3": ["2.1", "2.4", "3.5"], "2.4": ["2.1", "2.3"],
    "3.1": ["1.3", "3.2", "3.3", "3.4", "3.5"], "3.2": ["3.1"],
    "3.3": ["2.2", "3.1"], "3.4": ["2.2", "3.1"], "3.5": ["2.3", "3.1"],
    "4.1": ["1.3", "4.2", "4.5"], "4.2": ["4.1", "4.3", "4.4"],
    "4.3": ["4.1", "4.2", "4.4"], "4.4": ["4.1", "4.2", "4.6", "4.7"],
    "4.5": ["4.1"], "4.6": ["4.4", "4.7"], "4.7": ["4.4", "4.6"],
    "5.1": [],
}


def choose_objectives(objectives, brief, limit=4):
    words = {w.strip(".,;:()–-").lower() for w in brief.split() if len(w) >= 5}
    scored = []
    for objective in objectives:
        text = objective["syllabus_text"].lower()
        score = sum(1 for word in words if word in text)
        scored.append((score, objective["objective_id"]))
    scored.sort(key=lambda row: (-row[0], row[1]))
    chosen = [oid for score, oid in scored if score > 0][:limit]
    if len(chosen) < 2:
        chosen.extend(oid for _, oid in scored if oid not in chosen)
    return chosen[: min(limit, len(objectives))]


labels = {
    "multiple_choice_set": (["A", "B"], "Identify", None),
    "short_answer": (["A", "B"], "Explain", 8),
    "calculation": (["A", "B"], "Calculate", 5),
    "practical_task": (["C"], "Determine", 20),
}

render = load_renderer()
topics_dir = os.path.join(WS, "topics")
coverage_rows = []
subject_marks = {"A": 0.0, "B": 0.0, "C": 0.0}
for topic in sorted(by_topic, key=lambda value: [int(x) for x in value.split(".")]):
    topic_dir = os.path.join(topics_dir, topic)
    contract_path = os.path.join(topic_dir, "contract.json")
    work_order_path = os.path.join(topic_dir, "work_order.json")
    contract = load(contract_path)
    work_order = load(work_order_path)
    contract["generated_by"] = "make_contract.py + planning/refine_generated_plan_8224.py"
    work_order["generated_by"] = (
        "build/make_work_order.py + planning/refine_generated_plan_8224.py — regenerate, never edit"
    )
    neighbours = [f"{topic_titles[other]} — taught in topic {other}"
                  for other in adjacency.get(topic, [])]
    contract["depth_constraints"]["adjacent_topics"] = neighbours
    work_order["adjacent_topics"] = neighbours
    contract["depth_constraints"]["excluded_constructs_source"] += (
        " All syllabus exclusions remain on every contract deliberately, because the playbook requires "
        "every contract to carry every scope limit; adjacency is curated here instead of keyword-derived."
    )

    if topic == "5.1":
        contract["depth_constraints"]["word_budget"] = {"min": 6000, "max": 8000}
        contract["depth_constraints"]["word_budget_note"] = (
            "Chemistry planning judgement: the 39 Annexe A criteria are taught as four integrated "
            "practical-skill units, not as 39 repetitive mini-lessons."
        )
        total_objectives = sum(len(unit["objective_ids"]) for unit in work_order["content_units"])
        used_min = used_max = 0
        for index, unit in enumerate(work_order["content_units"]):
            count = len(unit["objective_ids"])
            if index == len(work_order["content_units"]) - 1:
                budget = [6000 - used_min, 8000 - used_max]
            else:
                budget = [math.floor(6000 * count / total_objectives),
                          math.floor(8000 * count / total_objectives)]
                used_min += budget[0]
                used_max += budget[1]
            unit["word_budget"] = budget

    objectives = by_topic[topic]
    for task in work_order["performance_tasks"]:
        aos, command, tariff = labels[task["item_type"]]
        if task["item_type"] == "multiple_choice_set":
            tariff = max(4, min(12, round(4 + 8 * (len(objectives) - 3) / 22)))
            task["brief"] = re.sub(r"A set of \d+", f"A set of {tariff}", task["brief"])
        task["assessment_objectives"] = aos
        task["command_word"] = command
        task["mark_tariff"] = tariff
        task["objective_ids"] = choose_objectives(objectives, task["brief"])

    marks = {"A": 0.0, "B": 0.0, "C": 0.0}
    for slot in work_order["item_slots"]:
        aos = slot.get("assessment_objectives") or ["A"]
        tariff = slot.get("mark_tariff") or 0
        for ao in aos:
            marks[ao] += tariff / len(aos)
    for task in work_order["performance_tasks"]:
        if task["item_type"] == "multiple_choice_set":
            marks["A"] += task["mark_tariff"] / 2
            marks["B"] += task["mark_tariff"] / 2
        elif task["item_type"] == "short_answer":
            marks["A"] += 4
            marks["B"] += 4
        elif task["item_type"] == "calculation":
            marks["A"] += 1
            marks["B"] += 4
        else:
            marks["C"] += task["mark_tariff"]
    total_marks = sum(marks.values()) or 1
    shares = {ao: round(100 * value / total_marks) for ao, value in marks.items()}
    work_order["marks_equivalent_total"] = round(total_marks)
    work_order["planned_ao_mix_by_marks"] = {
        ao: {"planned_share_percent": shares[ao], "syllabus_weight_percent": target}
        for ao, target in {"A": 40, "B": 40, "C": 20}.items()
    }
    for ao in subject_marks:
        subject_marks[ao] += marks[ao]
    coverage_rows.append((topic, work_order["topic_title"], len(objectives),
                          work_order["planned_item_count"], round(total_marks), shares))

    write(contract_path, contract)
    write(work_order_path, work_order)
    with open(os.path.join(topic_dir, "work_order.md"), "w", encoding="utf-8") as fh:
        fh.write(render(work_order))

subject_total = sum(subject_marks.values()) or 1
subject_shares = {ao: round(100 * value / subject_total) for ao, value in subject_marks.items()}
gaps = {ao: subject_shares[ao] - target for ao, target in {"A": 40, "B": 40, "C": 20}.items()}
largest_gap = max(abs(value) for value in gaps.values())
lines = [
    "# AO coverage — whole subject", "",
    "*Generated by planning/refine_generated_plan_8224.py after the standard builders. Regenerate, never edit.*", "",
    "The syllabus states its assessment-objective weights as a share of **marks**, across the whole examination. "
    "The subject total is the governing comparison; individual topics naturally differ.", "",
    "## Subject total", "", "| AO | planned | syllabus weight | gap |", "|---|---:|---:|---:|",
]
for ao, target in {"A": 40, "B": 40, "C": 20}.items():
    lines.append(f"| {ao} | {subject_shares[ao]}% | {target}% | {gaps[ao]:+d} |")
lines += ["", f"{'✅' if largest_gap <= 5 else '❌'} **largest gap {largest_gap} points** across "
          f"{round(subject_total):,} marks-equivalent of practice.", "",
          "A gap inside 5 points is the plan matching the exam. A larger gap means the item plan needs more "
          "of that kind of genuine practice, not padding.", "", "## By topic", "",
          "| Topic | Objectives | Items | Marks-eq | A | B | C |", "|---|---:|---:|---:|---:|---:|---:|"]
for topic, title, objectives, items, marks_total, shares in coverage_rows:
    lines.append(f"| **{topic}** {title} | {objectives} | {items} | {marks_total} | "
                 f"{shares['A']}% | {shares['B']}% | {shares['C']}% |")
lines.append("")
with open(os.path.join(WS, "curriculum", "ao_coverage.md"), "w", encoding="utf-8") as fh:
    fh.write("\n".join(lines))

print(f"refined 21 work orders; Paper 3 notes 6,000-8,000 words; AO gap {largest_gap} points")
