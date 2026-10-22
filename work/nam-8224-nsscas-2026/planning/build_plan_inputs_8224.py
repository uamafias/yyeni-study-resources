#!/usr/bin/env python3
"""Build the Step 4 planning inputs for Namibia NSSCAS Chemistry 8224.

Sources are the verified syllabus facts, the meaning-mapped assessment evidence,
the exposure map and Annexe A (Paper 3 practical skills).  This script writes
only generated planning inputs; the standard build tools create contracts and
work orders from them.
"""
from __future__ import annotations

import collections
import datetime
import json
import os
import re

import yaml

HERE = os.path.dirname(os.path.abspath(__file__))
WS = os.path.dirname(HERE)
CUR = os.path.join(WS, "curriculum")
NOW = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def load(path):
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)


def write_json(path, value):
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(value, fh, indent=1, ensure_ascii=False)
        fh.write("\n")


facts = load(os.path.join(CUR, "syllabus-facts.json"))
bullets = load(os.path.join(HERE, "syllabus_bullets.json"))
evidence = load(os.path.join(WS, "assessment-evidence", "assessment_evidence.json"))["records"]
old_exposure = load(os.path.join(CUR, "exam-exposure.json"))

outline = facts["content_outline"]
topic_rows = {x["id"]: x for x in outline if x["level"] == "topic"}
subtopic_rows = {x["id"]: x for x in outline if x["level"] == "subtopic"}


def topic_for(unit):
    return ".".join(unit.split(".")[:2])


def objective_type(text):
    low = text.lower()
    if low.startswith("define") or "define and use" in low:
        return "chem_definition"
    if any(x in low for x in ("calculate", "calculations", "determine enthalpy", "use the mole",
                              "use the ideal gas equation", "pV = nRT")):
        return "chem_quantitative"
    if any(x in low for x in ("construct equations", "write equations", "construct ionic",
                              "balance chemical equations", "balanced equations")):
        return "chem_equation"
    if any(x in low for x in ("mechanism", "free radical", "electrophilic", "nucleophilic")):
        return "chem_mechanism"
    if any(x in low for x in ("draw", "formulae", "structure", "shapes", "bond angles", "stereoisomer")):
        return "chem_representation"
    if any(x in low for x in ("name", "nomenclature")):
        return "chem_nomenclature"
    if any(x in low for x in ("interpret", "deduce", "analyse", "use data", "spectrum", "spectra", "graph")):
        return "chem_data_interpretation"
    if any(x in low for x in ("compare", "contrast", "distinguish")):
        return "chem_comparison"
    if ("reactions of" in low or "chemistry of" in low or
            (low.startswith(("describe the reaction", "describe and explain the reaction")))):
        return "chem_reaction"
    if any(x in low for x in ("explain", "account for", "in terms of")):
        return "chem_explanation"
    if any(x in low for x in ("trend", "variation", "relationship", "effect of")):
        return "chem_relationship"
    if any(x in low for x in ("describe", "state", "recall", "know", "recognise", "identify", "give")):
        return "chem_description"
    return "chem_concept"


def depth_tier(text, typ):
    low = text.lower()
    if typ in ("chem_definition", "chem_nomenclature") or low.startswith(("state", "recall", "know", "name")):
        return 1
    if typ in ("chem_data_interpretation", "chem_relationship", "chem_mechanism") or low.startswith(("analyse", "deduce", "suggest")):
        return 3
    return 2


COMMANDS_BY_TYPE = {
    "chem_definition": ["Define", "State"],
    "chem_quantitative": ["Calculate", "Determine"],
    "chem_quantitative_multi": ["Calculate", "Determine"],
    "chem_equation": ["Write", "Construct"],
    "chem_reaction": ["Describe", "Write", "Explain"],
    "chem_reaction_multi": ["Describe", "Write", "Explain"],
    "chem_particle_field": ["Describe", "Sketch", "Explain"],
    "chem_mechanism": ["Explain", "Describe", "Draw"],
    "chem_representation": ["Draw", "Sketch", "Identify"],
    "chem_nomenclature": ["Name", "Give", "Identify"],
    "chem_data_interpretation": ["Determine", "Identify", "State", "Explain"],
    "chem_comparison": ["Contrast", "Describe", "Explain"],
    "chem_explanation": ["Explain", "Describe"],
    "chem_relationship": ["Explain", "Describe", "State"],
    "chem_description": ["State", "Describe", "Identify", "Give"],
    "chem_concept": ["State", "Explain", "Suggest"],
}


source_rationale = (
    "No approved learner notes or textbook are held in the local Chemistry corpus. "
    "Claims must be sourced to an approved local authority or transparently derived from verified premises, "
    "then independently reviewed under the playbook."
)

registry = []
for tid, row in sorted(topic_rows.items(), key=lambda kv: [int(x) for x in kv[0].split(".")]):
    registry.append({
        "objective_id": f"OBJ-8224-{tid}", "parent_id": None, "topic_id": tid,
        "syllabus_text": f"{tid} {row['title']}",
        "learner_objective": f"{row['title']} (syllabus topic {tid})",
        "level": "NSSCAS", "route_status": "core", "mandatory": True,
        "objective_type": "chem_topic_container", "assessment_objectives": ["A", "B"],
        "command_words": [], "prerequisite_ids": [], "related_ids": [], "depth_tier": 4,
        "source_coverage": {"rating": 0, "action": "generate_gap", "rationale": source_rationale},
        "status": "planned", "syllabus_page": row["page"], "papers": ["1", "2"],
    })

for b in bullets:
    tid = topic_for(b["unit"])
    oid = f"OBJ-8224-{b['unit']}-{b['n']:02d}"
    typ = objective_type(b["text"])
    if oid == "OBJ-8224-1.1.5-02":
        typ = "chem_quantitative_multi"
    elif typ == "chem_reaction" and any(marker in b["text"].lower() for marker in (
            "following reactions", "with oxygen, water and dilute acids", "with oxygen",
            "with: - aqueous silver", "cold and with hot")):
        typ = "chem_reaction_multi"
    sub = subtopic_rows.get(b["unit"], {})
    item = {
        "objective_id": oid, "parent_id": f"OBJ-8224-{tid}", "topic_id": tid,
        "syllabus_text": b["text"], "learner_objective": b["text"],
        "sub_topic": b["unit"], "sub_topic_heading": sub.get("title", b["unit"]),
        "syllabus_page": b["page"], "papers": ["1", "2"],
        "level": "NSSCAS", "route_status": "core", "mandatory": True,
        "objective_type": typ, "assessment_objectives": ["A", "B"],
        "command_words": COMMANDS_BY_TYPE[typ], "prerequisite_ids": [], "related_ids": [],
        "depth_tier": depth_tier(b["text"], typ),
        "source_coverage": {"rating": 0, "action": "generate_gap", "rationale": source_rationale},
        "status": "planned",
    }
    if "not required" in b["text"].lower() or "will not require" in b["text"].lower():
        item["syllabus_guidance"] = b["text"]
    registry.append(item)

# The 1.2.1 heading-level syllabus objective also names behaviour of the three
# subatomic particles in electric fields.  The bullet extractor captured the
# narrower bullets but not this assessable heading-level demand; the 2025 report
# confirms that it is examined.  Keep it explicit so it cannot disappear from
# the work order.
registry.append({
    "objective_id": "OBJ-8224-1.2.1-04", "parent_id": "OBJ-8224-1.2", "topic_id": "1.2",
    "syllabus_text": "describe and sketch the behaviour of protons, neutrons and electrons in an electric field",
    "learner_objective": "Describe and sketch how protons, neutrons and electrons behave in an electric field",
    "sub_topic": "1.2.1", "sub_topic_heading": "Particles in the atom", "syllabus_page": 7,
    "papers": ["1", "2"], "level": "NSSCAS", "route_status": "core", "mandatory": True,
    "objective_type": "chem_particle_field", "assessment_objectives": ["A", "B"],
    "command_words": ["Describe", "Sketch", "Explain"], "prerequisite_ids": ["OBJ-8224-1.2.1-01"],
    "related_ids": [], "depth_tier": 2,
    "source_coverage": {"rating": 1, "action": "generate_gap", "rationale":
                        "Syllabus 1.2.1 heading-level objective; corroborated by 2025 examiner report Paper 2 Q2(b)."},
    "status": "planned",
})

# Annexe A, pp. 38-42: each bullet below is one explicit practical expectation.
practical_groups = [
    ("5.1.1", "Manipulation, measurement and observation", "prac_mmo", 38, [
        "set up apparatus", "follow instructions given in written or diagrammatic form",
        "collect an appropriate quantity of data or observations, including subtle differences in colour, solubility or quantity",
        "make measurements using pipettes, burettes, measuring cylinders, thermometers, timing devices and other common laboratory apparatus",
        "make accurate and consistent measurements and observations",
        "decide how many tests or observations to perform",
        "make measurements that span a range and have a distribution appropriate to the experiment",
        "decide how long to leave experiments running before taking readings",
        "identify where repeated readings or observations are appropriate and replicate them as necessary",
        "identify appropriate confirmatory tests and their nature",
        "select reagents to distinguish between given ions",
    ]),
    ("5.1.2", "Recording data, observations and reasoning", "prac_recording", 39, [
        "present numerical data, values or observations in a single table of results",
        "draw an appropriate results table before taking readings or making observations",
        "include columns for raw data, calculated values and analyses or conclusions where needed",
        "use column headings containing both the quantity and the unit in accepted scientific form",
        "record raw readings to consistent precision and observations to a consistent level of detail",
        "show working in calculations and the key steps in reasoning",
        "use an appropriate number of significant figures for calculated quantities",
    ]),
    ("5.1.3", "Data layout and graphical treatment", "prac_presentation", 40, [
        "choose a suitable clear method of presenting data using tables, graphs or both",
        "plot appropriate variables on clearly labelled axes with suitable scales",
        "plot all points or bars to an appropriate accuracy",
        "draw straight lines of best fit or curves that show the trend",
        "select variables and scales to obtain a linear graph of the form y = mx + c where appropriate",
        "determine and interpret the slope and intercept of a linear graph",
        "use a tangent gradient as a rate of change and interpret an area where it has physical significance",
    ]),
    ("5.1.4", "Analysis, conclusions and evaluation", "prac_analysis", 41, [
        "describe patterns and trends in tables and graphs using supporting values where appropriate",
        "describe and summarise the key points of a set of observations",
        "find an unknown value from coordinates or intercepts on a graph",
        "calculate quantities from data and calculate means from repeated values",
        "determine the gradient of a straight-line graph or a tangent to a curve",
        "evaluate the effectiveness of control variables",
        "identify the most significant sources of error in an experiment",
        "estimate uncertainty quantitatively and express it as an absolute or percentage error",
        "distinguish between systematic and random errors",
        "draw conclusions from data, observations and calculated values",
        "decide whether experimental data support a stated hypothesis and make further predictions",
        "give scientific explanations for practical data, observations and conclusions",
        "suggest realistic modifications that improve accuracy or observations",
        "suggest an extension that answers a specified new question",
    ]),
]

registry.append({
    "objective_id": "OBJ-8224-5.1", "parent_id": None, "topic_id": "5.1",
    "syllabus_text": "5.1 Advanced practical skills",
    "learner_objective": "Advanced practical skills (Paper 3)", "level": "NSSCAS",
    "route_status": "core", "mandatory": True, "objective_type": "chem_topic_container",
    "assessment_objectives": ["C"], "command_words": [], "prerequisite_ids": [],
    "related_ids": [], "depth_tier": 4,
    "source_coverage": {"rating": 0, "action": "generate_gap", "rationale": source_rationale},
    "status": "planned", "syllabus_page": 36, "papers": ["3"],
})
for sub, heading, typ, page, texts in practical_groups:
    for n, text in enumerate(texts, 1):
        registry.append({
            "objective_id": f"OBJ-8224-{sub}-{n:02d}", "parent_id": "OBJ-8224-5.1",
            "topic_id": "5.1", "syllabus_text": text, "learner_objective": text,
            "sub_topic": sub, "sub_topic_heading": heading, "syllabus_page": page,
            "papers": ["3"], "level": "NSSCAS", "route_status": "core", "mandatory": True,
            "objective_type": typ, "assessment_objectives": ["C"],
            "command_words": ["Record", "Plot", "Calculate", "Determine", "Describe", "Suggest", "Explain"],
            "prerequisite_ids": [], "related_ids": [], "depth_tier": 2 if typ != "prac_analysis" else 3,
            "source_coverage": {"rating": 0, "action": "generate_gap", "rationale": source_rationale},
            "status": "planned",
        })

write_json(os.path.join(CUR, "objective_registry.json"), {
    "registry_id": "REGISTRY-NAM-8224-NSSCAS-2026",
    "qualification_profile_id": "nam-8224-nsscas-2026",
    "subject_profile_id": "yyeni-subject-chemistry-nsscas-v0.2.0",
    "generated_at": NOW,
    "authority": "NSSCAS Chemistry 8224 approved syllabus, NIED 2020, including Annexe A",
    "granularity_note": "One objective per specific-objective bullet; Paper 3 Annexe A lists are decomposed one bullet per objective.",
    "papers_note": "Topics 1.1-4.7 feed Papers 1 and 2; topic 5.1 is the Paper 3 practical-skills strand.",
    "objectives": registry,
})

# The standard generator filters misconception entries by whole-topic id (for
# example 1.2), not by syllabus subtopic (1.2.1).  Preserve the finer locator in
# sub_topic_id while normalising topic_id so every evidenced misconception gets
# its planned discriminating slot.
misconceptions_path = os.path.join(CUR, "misconceptions.json")
misconceptions = load(misconceptions_path)
for entry in misconceptions.get("entries", []):
    original_topic = entry.get("topic_id")
    if original_topic and original_topic.count(".") >= 2:
        entry["sub_topic_id"] = original_topic
        entry["topic_id"] = topic_for(original_topic)
write_json(misconceptions_path, misconceptions)

# Standardise the Step 3 exposure map for the contract/work-order tools.
by_oid = collections.defaultdict(list)
for rec in evidence:
    for oid in rec.get("objective_ids") or []:
        by_oid[oid].append(rec)
old_by_id = {x["objective_id"]: x for x in old_exposure["objectives"]}
exposure = []
for obj in registry:
    if not obj["parent_id"]:
        continue
    oid = obj["objective_id"]
    rows = by_oid.get(oid, [])
    if obj["topic_id"] == "5.1":
        skill = obj["objective_type"].replace("prac_", "")
        if skill == "mmo":
            wanted = "collecting"
        elif skill == "recording" or skill == "presentation":
            wanted = "collecting"
        else:
            wanted = "analysing"
        rows = [r for r in evidence if r.get("paper_id") == "P3" and any(f"skill_category: {wanted}" in n for n in r.get("notes", []))]
    series = sorted({str(r.get("exam_series") or r.get("year")) for r in rows})
    commands = collections.Counter((r.get("command_word") or "").split()[0].title() for r in rows if r.get("command_word"))
    raw_commands = collections.Counter(r.get("command_word") for r in rows if r.get("command_word"))
    tariffs = collections.Counter(str(r.get("mark_tariff") or 0) for r in rows if r.get("mark_tariff"))
    marks = sum(r.get("mark_tariff") or 0 for r in rows)
    old = old_by_id.get(oid, {})
    old_class = old.get("exam_exposure") or old.get("exposure_class")
    if obj["topic_id"] == "5.1":
        cls = "core"
    elif old_class in ("probed_high", "core", "frequent"):
        cls = "core" if len(series) >= 3 else "frequent"
    elif old_class in ("probed_low", "occasional", "rare"):
        cls = "occasional" if len(series) >= 2 else "rare"
    else:
        cls = "unseen"
    exposure.append({
        "objective_id": oid, "topic_id": obj["topic_id"], "syllabus_text": obj["syllabus_text"],
        "times_examined": len(rows), "marks_examined": marks, "series_spread": len(series),
        "series": series, "tariffs": dict(tariffs), "command_words": dict(commands),
        "modal_tariff": int(tariffs.most_common(1)[0][0]) if tariffs else None,
        "evidence": {
            "question_parts_naming_it": len(by_oid.get(oid, [])),
            "distinct_series": len({r.get("exam_series") for r in by_oid.get(oid, [])}),
            "max_mark_tariff": max([r.get("mark_tariff") or 0 for r in by_oid.get(oid, [])] or [0]),
            "command_words_observed": dict(collections.Counter(r.get("command_word") for r in by_oid.get(oid, []) if r.get("command_word"))),
        },
        "frequency_basis": "skill_category_proxy_not_objective_frequency" if obj["topic_id"] == "5.1" else "direct_objective_mapping",
        "exposure_class": cls,
    })
write_json(os.path.join(CUR, "exam-exposure.json"), {
    "map_id": "EXPOSURE-NAM-8224-NSSCAS-2026", "generated_at": NOW,
    "method": "Meaning-mapped assessment evidence, normalised for the v0.2.0 contract and work-order builders.",
    "objectives": exposure,
})


def base_command(value):
    low = (value or "").strip().lower()
    if any(k in low for k in ("record", "carry out", "select reagents", "use observations", "weigh")):
        return "Record"
    if low.startswith(("which", "what", "how many")):
        return "Question word"
    if low.startswith("obtain"):
        return "Calculate"
    match = re.match(r"[A-Za-z]+", value or "")
    return match.group(0).title() if match else value


observed = collections.defaultdict(lambda: {"n": 0, "tariffs": collections.Counter(), "papers": collections.Counter()})
for rec in evidence:
    if rec["evidence_type"] != "past_paper" or rec["paper_id"] not in ("P2", "P3") or not rec.get("command_word"):
        continue
    word = base_command(rec["command_word"])
    observed[word]["n"] += 1
    observed[word]["tariffs"][str(rec.get("mark_tariff") or 0)] += 1
    observed[word]["papers"][rec["paper_id"].replace("P", "")] += 1

syllabus_words = {}
for row in facts["command_words"]:
    for word in row["words"]:
        syllabus_words[word.split(" /")[0]] = row

ao_for_word = {
    "Define": ["A"], "State": ["A"], "Name": ["A"], "Give": ["A"], "Write": ["A"],
    "Identify": ["A", "B"], "Describe": ["A", "B"], "Explain": ["A", "B"],
    "Calculate": ["B"], "Determine": ["B"], "Suggest": ["B"], "Construct": ["B"],
    "Draw": ["B"], "Sketch": ["B"], "Complete": ["B"], "Use": ["B"], "Contrast": ["B"],
    "Plot": ["C"], "Record": ["C"], "Insert": ["C"], "Question word": ["A", "B"],
}
commands = []
for word, info in sorted(observed.items(), key=lambda kv: (-kv[1]["n"], kv[0])):
    tariffs = info["tariffs"]
    modal = int(tariffs.most_common(1)[0][0]) if tariffs else None
    commands.append({
        "word": word, "meaning": None, "meaning_provenance": "syllabus glossary" if word in syllabus_words else "observed in papers",
        "in_syllabus_table": word in syllabus_words, "primary_assessment_objectives": ao_for_word.get(word, ["A", "B"]),
        "assessment_objectives_provenance": "judgement from command shape and paper",
        "observed_count": info["n"], "observed_tariffs": dict(tariffs), "modal_tariff": modal,
        "papers": dict(info["papers"]), "observation_provenance": "2021-2024 corpus",
        "verdict": "practical_instruction" if word in ("Plot", "Record", "Insert") else "primary",
        "use_in_prompts": word not in ("Plot", "Record", "Insert", "Question word"),
        "exact_mark_tariff": modal, "used_at_level": True,
    })

# Sketch is evidenced in the 2025 examiner report even though the corresponding
# paper is not held in the 2021-2024 question-paper corpus.
if "Sketch" not in {c["word"] for c in commands}:
    commands.append({
        "word": "Sketch", "meaning": None, "meaning_provenance": "syllabus glossary",
        "in_syllabus_table": "Sketch" in syllabus_words, "primary_assessment_objectives": ["B"],
        "assessment_objectives_provenance": "judgement from command shape and examiner report",
        "observed_count": 1, "observed_tariffs": {"2": 1}, "modal_tariff": 2,
        "papers": {"2": 1}, "observation_provenance": "2025 examiner report, Paper 2 Q2(b)",
        "verdict": "primary", "use_in_prompts": True, "exact_mark_tariff": 2, "used_at_level": True,
    })

seen = {c["word"] for c in commands}
listed_never = sorted({w for row in facts["command_words"] for w in row["words"] if w not in seen})

subtype_map = [
    ("DEF", ["A"], "Remember"), ("FEATURE", ["A"], "Understand"),
    ("DIST", ["A", "B"], "Analyse"), ("PROC", ["A", "B"], "Apply"),
    ("WHY", ["A", "B"], "Understand"), ("MECH", ["A", "B"], "Analyse"),
    ("CHAIN", ["B"], "Analyse"), ("APP", ["B"], "Apply"),
    ("CALC", ["B"], "Apply"), ("INTERP", ["B"], "Analyse"),
    ("DIAGRAM", ["B"], "Apply"), ("EQUATION", ["A", "B"], "Apply"),
    ("EVAL", ["B"], "Evaluate"), ("MISCON", ["A", "B"], "Understand"),
    ("SYNTH", ["B"], "Analyse"),
]
# A subtype can serve theory or Paper 3. Per-objective and per-paper mappings
# in subject-profile.yaml select the actual AO; this is the permitted union.
subtype_map = [(s, ao + (["C"] if s in {"PROC", "APP", "CALC", "INTERP", "EVAL", "SYNTH"} else []), bloom)
               for s, ao, bloom in subtype_map]
framework = {
    "framework_id": "FRAMEWORK-NAM-8224-NSSCAS-2026", "generated_at": NOW,
    "authority": "NSSCAS Chemistry 8224 syllabus (NIED 2020) and the 2021-2025 local assessment corpus",
    "syllabus_facts_ref": "curriculum/syllabus-facts.json",
    "provenance_rule": "AO names, weights and paper structures are syllabus facts; command frequencies and tariffs are corpus observations; subtype mappings are planning judgement.",
    "evidence_window": "Question papers 2021-2024 and the NSSCAS Examiners Report 2025; no mark schemes held.",
    "assessment_objectives": [{
        "code": a["code"], "name": a["name"], "definition": "; ".join(a["can_do"]),
        "qualification_weight_percent": facts["ao_weights"]["qualification_percent_as_printed"][a["code"]],
        "provenance": f"syllabus page {a['source']['page']}",
    } for a in facts["assessment_objectives"]],
    "papers": [{
        "paper": p["paper"], "name": p["name"], "marks": p["marks"], "duration_minutes": p["duration_minutes"],
        "weight_percent": p["weight_percent"], "ao_split": facts["ao_weights"]["per_component_percent"][f"P{p['paper']}"],
        "structure": p["verbatim"], "provenance": f"syllabus page {p['source']['page']}",
    } for p in facts["papers"]],
    "command_words": commands,
    "command_words_listed_but_never_used": listed_never,
    "flashcard_subtype_ao_map": [{"subtype": s, "assessment_objectives": ao, "blooms_level": bloom} for s, ao, bloom in subtype_map],
    "blooms_taxonomy": {
        "levels": [{"level": x} for x in ["Remember", "Understand", "Apply", "Analyse", "Evaluate", "Create"]],
        "by_performance_task": {"multiple_choice_set": "Apply", "short_answer": "Apply", "calculation": "Apply", "practical_task": "Analyse"},
    },
    "ao_mark_budget": {
        "basis": "Use the qualification percentages printed by the syllabus: 40/40/20. The 35.7/35.7/28.6 figure derived from raw paper marks is recorded but is not the governing target.",
        "stated_qualification_weight_percent": facts["ao_weights"]["qualification_percent_as_printed"],
        "derived_from_marks_percent": facts["ao_weights"]["derived_from_marks_percent"],
    },
    "item_mix_target": {"target_share_percent": facts["ao_weights"]["qualification_percent_as_printed"]},
}
write_json(os.path.join(CUR, "assessment-framework.json"), framework)

terms = [
    ("relative atomic mass", "The weighted mean mass of an atom of an element relative to one twelfth of the mass of a carbon-12 atom.", "Not the mass number of one isotope."),
    ("mole", "The amount of substance containing the Avogadro constant number of specified particles.", "Always state which particles are counted."),
    ("empirical formula", "The simplest whole-number ratio of atoms of each element in a compound.", "Not necessarily the molecular formula."),
    ("molecular formula", "The actual number of atoms of each element in one molecule.", "It is a whole-number multiple of the empirical formula for a molecular substance."),
    ("oxidation number", "The charge assigned to an atom by the agreed electron-accounting rules.", "Not necessarily an actual ionic charge."),
    ("standard enthalpy change", "The enthalpy change when reactants and products are in their standard states under standard conditions.", "The named process—formation, combustion or neutralisation—must also be stated."),
    ("activation energy", "The minimum energy that colliding particles must have for a reaction to occur.", "On a Boltzmann graph it is a position on the energy axis, not an area."),
    ("dynamic equilibrium", "A closed-system state in which forward and reverse reactions continue at equal rates, so concentrations remain constant.", "Equal rates do not mean equal concentrations."),
    ("catalyst", "A substance that increases reaction rate by providing an alternative pathway of lower activation energy and is regenerated overall.", "It does not change the equilibrium position."),
    ("electrophile", "An electron-pair acceptor.", "Usually electron-deficient; do not define it only as a positive ion."),
    ("nucleophile", "An electron-pair donor.", "Its lone pair or negative charge is the reactive feature."),
    ("free radical", "A species containing an unpaired electron.", "The dot represents the unpaired electron."),
    ("homologous series", "A family of organic compounds with the same functional group and general formula, similar chemical properties and a gradual change in physical properties.", "Successive members differ by CH2."),
    ("structural isomer", "A compound with the same molecular formula as another compound but a different structural formula.", "Different connectivity, not merely a different drawing."),
    ("stereoisomer", "A compound with the same structural formula as another but a different arrangement of atoms in space.", "Includes cis-trans and optical isomerism in this syllabus."),
    ("concordant titres", "Titre values that agree within 0.10 cm3 for this syllabus.", "The rough titre is not used in the mean."),
    ("random error", "Unpredictable variation that causes repeated readings to scatter.", "Repeating and averaging can reduce its effect."),
    ("systematic error", "An error that shifts readings consistently in one direction.", "Repeating does not remove it."),
    ("precision", "The closeness of repeated measurements to one another and the resolution with which readings are recorded.", "Not the same as accuracy."),
    ("accuracy", "The closeness of a measured or calculated value to the accepted value.", "A precise set of readings may still be inaccurate."),
]
write_json(os.path.join(CUR, "glossary.json"), {
    "glossary_id": "GLOSSARY-NAM-8224-NSSCAS-2026", "status": "planning-draft",
    "note": "Settled senses needed by the first planning pass. Expand only from the syllabus and reviewed Chemistry sources before authoring each affected topic.",
    "terms": [{"term": t, "sense": s, "homonym_warning": h} for t, s, h in terms],
})

qualification = {
    "profile_id": "nam-8224-nsscas-2026", "version": "0.2.0-draft", "status": "draft",
    "board": "Namibia Ministry of Education, Arts and Culture / NIED", "qualification": "NSSCAS",
    "subject": "Chemistry", "syllabus_code": "8224", "examination_years": [2026], "route": "advanced_subsidiary",
    "source": facts["source_document"],
    "assessment_objectives": framework["assessment_objectives"], "papers": framework["papers"],
    "ao_source_note": framework["ao_mark_budget"]["basis"],
    "learner_context": {"region": "Namibia", "medium": "English", "currency": "N$"},
    "prior_teaching": "NSSCO-level Chemistry knowledge is assumed; the learner resource still introduces every NSSCAS term before using it.",
}
with open(os.path.join(WS, "qualification-profile.yaml"), "w", encoding="utf-8") as fh:
    yaml.safe_dump(qualification, fh, sort_keys=False, allow_unicode=True, width=110)

subject_profile = {
    "profile_id": "yyeni-subject-chemistry-nsscas-v0.2.0", "version": "0.2.0-draft", "status": "draft",
    "subject_name": "Chemistry (Namibia NSSCAS 8224)", "language_variant": "British English",
    "purpose": "A full teaching and retrieval-practice model derived from the verified syllabus and the local assessment corpus.",
    "depth_model": {"note_mode": "full teaching depth", "words_per_objective": "230-470 depending on exposure"},
    "terminology_rules": [
        "Use syllabus wording and curriculum/glossary.json for settled meanings.",
        "Write chemical formulae and equations unambiguously; include state symbols when the task requires them.",
        "For calculations show the relationship, substitution, units, conversion and justified significant figures.",
        "Never describe corpus frequency or examiner behaviour in learner-facing text.",
    ],
    "answer_structures": {
        "DEF": ["definition", "required term", "conditions where relevant"],
        "FEATURE": ["feature", "property", "point"], "DIST": ["similarity", "difference", "whereas"],
        "PROC": ["sequence", "reagent or apparatus", "condition", "observation or result"],
        "WHY": ["reason", "because", "effect"], "MECH": ["electron movement", "intermediate", "product"],
        "CHAIN": ["change", "because", "therefore", "result"], "APP": ["given situation", "principle", "application"],
        "CALC": ["relationship or equation", "conversion", "substitution", "answer", "unit", "significant figures"],
        "INTERP": ["data or representation", "feature", "inference"],
        "DIAGRAM": ["required labels", "bonds or axes", "unambiguous representation"],
        "EQUATION": ["reactants", "products", "balance", "state symbols where required"],
        "EVAL": ["criterion", "evidence", "limitation", "judgement"],
        "MISCON": ["error", "correct idea", "discriminating test"], "SYNTH": ["linked objectives", "reasoning chain"],
        "multiple_choice_set": ["key", "correct option", "distractor", "error"],
        "short_answer": ["part", "mark", "creditworthy point"],
        "calculation": ["equation", "working", "answer", "unit", "significant figures"],
        "practical_task": ["apparatus and method", "observations or data table", "working", "conclusion", "error", "improvement"],
    },
    "variant_register": [
        {"term": "conditions", "variants": ["s.t.p.", "r.t.p."], "consequence": "The molar gas volume changes from 22.4 to 24.0 dm3 mol-1.", "teach_as": "Carry the stated temperature and pressure into every gas-volume calculation."},
        {"term": "formula", "variants": ["molecular", "empirical", "structural condensed", "displayed", "skeletal"], "consequence": "Each representation supplies different information.", "teach_as": "Answer in the representation requested."},
    ],
    "depictions": {"chart_model": "managed visual or bounded data table", "code_fence_languages": [], "rule": "Use managed diagrams for structures, apparatus and graphs where a visual is essential; every visual is reviewed by a person."},
    "conditioned_mechanisms": [
        {"mechanism_id": "CM-8224-EQUILIBRIUM", "name": "Equilibrium response", "rationale": "A predicted shift depends on the stated change and reaction conditions.", "asserted_when": ["equilibrium", "Le Chatelier"], "required_conditions": [{"name": "the imposed change is stated", "any_of": ["temperature", "pressure", "concentration"]}]},
        {"mechanism_id": "CM-8224-GAS-VOLUME", "name": "Molar gas volume", "rationale": "22.4 and 24.0 dm3 mol-1 apply under different conditions.", "asserted_when": ["molar gas volume", "dm3 mol-1"], "required_conditions": [{"name": "conditions are named", "any_of": ["s.t.p.", "r.t.p.", "273 K", "298 K"]}]},
    ],
    "prohibited_patterns": [
        "Do not teach beyond the explicit syllabus scope limits in curriculum/scope-scan.json.",
        "Do not reproduce question-paper, examiner-report or future marking-scheme wording.",
        "Do not present a practical observation as remembered recall when Paper 3 supplies qualitative-analysis notes and tests observation, recording and conclusion.",
    ],
    "glossary_homonyms": [{"term": t, "senses": [s], "rule": h} for t, s, h in terms if h],
    "slot_plan": {
        "subtypes_by_objective_type": {
            "chem_definition": ["DEF", "APP"], "chem_quantitative": ["FEATURE", "CALC", "INTERP"],
            "chem_quantitative_multi": ["FEATURE", "CALC", "CALC", "CALC", "INTERP"],
            "chem_equation": ["FEATURE", "EQUATION"], "chem_reaction": ["FEATURE", "EQUATION", "APP"],
            "chem_reaction_multi": ["FEATURE", "EQUATION", "EQUATION", "APP"],
            "chem_particle_field": ["FEATURE", "DIAGRAM"], "chem_mechanism": ["FEATURE", "MECH", "DIAGRAM"],
            "chem_representation": ["FEATURE", "DIAGRAM"], "chem_nomenclature": ["DEF", "APP"],
            "chem_data_interpretation": ["FEATURE", "INTERP"], "chem_comparison": ["FEATURE", "DIST"],
            "chem_explanation": ["FEATURE", "MECH"], "chem_relationship": ["FEATURE", "CHAIN"],
            "chem_description": ["FEATURE", "APP"], "chem_concept": ["FEATURE", "WHY"],
            "prac_mmo": ["PROC", "APP"], "prac_recording": ["PROC", "CALC"],
            "prac_presentation": ["INTERP", "APP"], "prac_analysis": ["INTERP", "EVAL"],
        },
        "subtypes_by_tier": {1: [], 2: [], 3: [], 4: []},
        "high_tariff": {"threshold": 99, "adds": []},
        "command_words_by_subtype": {
            "DEF": ["Define", "Name", "Give", "State"], "FEATURE": ["State", "Describe", "Identify", "Give"],
            "DIST": ["Contrast", "Describe", "Explain"], "PROC": ["Describe", "Write", "Construct"],
            "WHY": ["Explain"], "MECH": ["Explain", "Describe"], "CHAIN": ["Explain", "Describe"],
            "APP": ["Suggest", "Determine", "Explain"], "CALC": ["Calculate", "Determine"],
            "INTERP": ["Determine", "Identify", "State", "Explain"], "DIAGRAM": ["Draw", "Sketch", "Construct"],
            "EQUATION": ["Write", "Construct"], "EVAL": ["Suggest", "Explain", "Describe"],
            "MISCON": ["Explain", "State"], "SYNTH": ["Explain", "Calculate", "Determine"],
        },
        "tariff_overrides": {"MECH:Explain": 2, "CHAIN:Explain": 2, "EVAL:Suggest": 2, "PROC:Describe": 3,
                             "DIAGRAM:Draw": 2, "DIAGRAM:Sketch": 2, "EQUATION:Write": 2,
                             "CALC:Calculate": 3, "CALC:Determine": 2},
        "ao_by_objective_type": {
            "*": {"DEF": ["A"], "FEATURE": ["A"], "DIST": ["A", "B"], "PROC": ["A", "B"], "WHY": ["A"], "MECH": ["A", "B"], "CHAIN": ["B"], "APP": ["B"], "CALC": ["B"], "INTERP": ["B"], "DIAGRAM": ["B"], "EQUATION": ["A", "B"], "EVAL": ["B"], "MISCON": ["A", "B"], "SYNTH": ["B"]},
            "prac_mmo": {"PROC": ["C"], "APP": ["C"], "EVAL": ["C"]},
            "prac_recording": {"PROC": ["C"], "APP": ["C"], "CALC": ["C"]},
            "prac_presentation": {"PROC": ["C"], "INTERP": ["C"], "APP": ["C"]},
            "prac_analysis": {"INTERP": ["C"], "CALC": ["C"], "EVAL": ["C"], "APP": ["C"], "SYNTH": ["C"]},
        },
        "ao_by_paper": {"1+2": {"C": "B"}, "3": {"A": "C", "B": "C"}},
        "topic_targets_by_paper": {"1+2": {"A": 50, "B": 50, "C": 0}, "3": {"A": 0, "B": 0, "C": 100}},
        "misconception_slots": "one_per_entry",
        "top_up": [],
        "performance_tasks": [
            {"item_type": "multiple_choice_set", "papers": ["1"], "brief": "A set of {n} original four-option questions for this topic, about half recall and half application or calculation, with a key and an explanation of every distractor."},
            {"item_type": "short_answer", "papers": ["2"], "brief": "An original structured response with linked 1-3 mark parts using the topic's observed command words and tariffs, about 8 marks.", "ao_split": {"A": 4, "B": 4}},
            {"item_type": "calculation", "papers": ["2"], "brief": "An original multi-step calculation or quantitative interpretation, about 5 marks, with conversions, working, units and justified significant figures.", "ao_split": {"A": 1, "B": 4}},
            {"item_type": "practical_task", "papers": ["3"], "brief": "A 20-mark titration or volumetric-analysis task with readings, a correctly formatted table, concordance, calculations, conclusion and evaluation.", "ao_split": {"C": 20}},
            {"item_type": "practical_task", "papers": ["3"], "brief": "A 20-mark redox-titration task with readings, a correctly formatted table, concordance, stoichiometric calculations, conclusion and evaluation.", "ao_split": {"C": 20}},
            {"item_type": "practical_task", "papers": ["3"], "brief": "A 20-mark thermometric or enthalpy task with original data, calculation, conclusion, uncertainty and improvement.", "ao_split": {"C": 20}},
            {"item_type": "practical_task", "papers": ["3"], "brief": "A 20-mark rates or gravimetric task with original data, a graph or linear treatment, calculation, conclusion, uncertainty and improvement.", "ao_split": {"C": 20}},
            {"item_type": "practical_task", "papers": ["3"], "brief": "A 20-mark qualitative-analysis task requiring precise observations, use of excess reagent where relevant, deductions and confirmatory tests using supplied notes.", "ao_split": {"C": 20}},
            {"item_type": "practical_task", "papers": ["3"], "brief": "A 20-mark planning and evaluation task covering apparatus, control variables, error, uncertainty, realistic improvements and an extension.", "ao_split": {"C": 20}},
        ],
    },
}
with open(os.path.join(WS, "subject-profile.yaml"), "w", encoding="utf-8") as fh:
    yaml.safe_dump(subject_profile, fh, sort_keys=False, allow_unicode=True, width=120)

theme_titles = {str(t["theme"]): t["title"] for t in facts["themes"]}
theme_titles["5"] = "Advanced practical skills"
write_json(os.path.join(CUR, "unit_titles.json"), theme_titles)

print("registry objectives", len(registry), "assessable", sum(1 for x in registry if x["parent_id"]))
print("exposure records", len(exposure), "command words", len(commands), "glossary terms", len(terms))
