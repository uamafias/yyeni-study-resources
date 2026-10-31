"""Curated, meaning-mapped findings from the six Chemistry examiner reports."""

import json
import re
from pathlib import Path
from verify_report_citations import verify_findings, verify_answer_links, verify_manual_plans


ROOT = Path(__file__).resolve().parents[3]
WORK = Path(__file__).resolve().parents[1]

FINDINGS = [
    (2020, 88, "2", "4", "syllabus:5.1", "misconception", "Candidates predicted oxygen at a copper anode as though the electrode were inert; the report explains that the copper electrode takes part in the reaction."),
    (2021, 88, "3", "4", "syllabus:1.2.1", "omission", "Candidates struggled with planning investigations and were advised to plan answers before writing to avoid steps being out of sequence."),
    (2022, 93, "2", "3", "syllabus:7.4", "misconception", "Candidates treated preparation of an insoluble salt as though it required evaporation and crystallisation."),
    (2022, 94, "2", "5(b)", "syllabus:6.4", "misconception", "Candidates confused reaction rate with the time taken by a reaction."),
    (2022, 98, "3", "1", "syllabus:1.5", "misconception", "Some candidates added burette readings or subtracted them in the wrong order instead of finding the titre."),
    (2023, 97, "2", "1", "syllabus:2.2", "misconception", "Candidates confused atoms and elements and did not consistently use proton and neutron numbers to identify isotopes."),
    (2023, 106, "3", "3", "syllabus:8.1", "misconception", "Candidates mixed up flame tests with gas tests involving a lighted or glowing splint."),
    (2024, 105, "1", "9", "syllabus:2.2", "misconception", "Candidates confused an isotope with an allotrope."),
    (2024, 106, "1", "13", "syllabus:4.1", "misconception", "Candidates did not distinguish a mole from the Avogadro constant."),
    (2024, 106, "1", "27", "syllabus:8.2", "misconception", "Candidates confused tests using a glowing splint and a lighted splint."),
    (2024, 107, "2", None, "syllabus:5.1", "omission", "The report identifies ionic equations and ionic half-equations as recurring weak areas."),
    (2025, 92, "2", None, "syllabus:4.2", "omission", "Some candidates omitted calculation working or used incorrect units, losing available method credit."),
    (2025, 92, "2", "3(d)", "syllabus:6.4", "command-word miss", "Candidates explained the effect of pressure on equilibrium position when asked about reaction rate."),
    (2025, 100, "3", "4", "syllabus:1.2.1", "omission", "In planning answers, candidates named apparatus without saying what it was used for; a bare list did not earn the available credit."),
    (2021, 83, "2", "2", "syllabus:2.4", "misconception", "Candidates named electrons rather than mobile ions as charge carriers in a molten ionic compound."),
    (2021, 86, "2", "7", "syllabus:4.1", "omission", "Many candidates stopped an empirical-formula calculation after dividing by the smallest amount and did not scale the ratio to whole numbers."),
    (2021, 90, "3", "4", "syllabus:1.2.1", "omission", "Many planning responses scored only 0–3 marks or described reactions using apparatus and reactants that had not been provided."),
    (2022, 93, "2", "3", "syllabus:7.4", "omission", "Candidates often could not describe the carbon-dioxide test correctly."),
    (2022, 94, "2", "4", "syllabus:4.1", "omission", "In concentration calculations candidates often did not convert cubic centimetres into cubic decimetres."),
    (2022, 94, "2", "4", "syllabus:4.1", "omission", "Candidates applied Avogadro's constant without first using the equation's two-to-one water-to-acid mole ratio."),
    (2022, 99, "3", "2(b)", "syllabus:1.2.1", "omission", "Candidates struggled to plot the points at 2, 6 and 8 minutes, used oversized plotting blobs, and drew curves that did not balance the points."),
    (2022, 99, "3", "2", "syllabus:1.2.1", "misconception", "Candidates added masses at different times instead of subtracting them to find mass lost during an interval."),
    (2022, 100, "3", "3", "syllabus:8.1", "misconception", "Candidates described green copper(II) carbonate as blue, apparently confusing the solid with copper(II) sulfate."),
    (2022, 101, "3", "4", "syllabus:1.2.1", "omission", "Some candidates substituted fractional distillation or crystallisation for chromatography or misused the mortar and pestle."),
    (2023, 105, "3", "2", "syllabus:1.2.1", "misconception", "A flat gas-volume curve was described as equilibrium or a constant reaction rather than a completed reaction."),
    (2023, 106, "3", "3", "syllabus:8.1", "omission", "Candidates found negative chloride tests difficult and often reported a positive result instead."),
    (2023, 106, "3", "4", "syllabus:1.2.1", "misconception", "Some plans treated the marked-cross paper as chromatography paper rather than placing it beneath the flask to time clouding."),
    (2024, 108, "2", "2(a)", "syllabus:2.1.2", "misconception", "Candidates counted bromide-ion electrons as though bromide were a neutral bromine atom."),
    (2024, 108, "2", "2(c)", "syllabus:2.4.2", "misconception", "Some candidates drew covalent sharing instead of electron transfer when representing magnesium bromide."),
    (2024, 108, "2", "2(d)(ii)", "syllabus:5.1", "misconception", "Some candidates used the word electrons instead of ions in their answers to Q2(d)(ii)."),
    (2024, 110, "2", "4", "syllabus:7.4", "command-word miss", "Some candidates named apparatus where the question requested suitable starting materials."),
    (2025, 92, "2", "1(b)(ii)", "syllabus:2.1.2", "misconception", "Some candidates did not distinguish an atom from an ion when explaining electron and proton counts."),
    (2025, 101, "3", "3(b)", "syllabus:C3", "misconception", "Candidates called the deep-blue solution after excess ammonia a precipitate, losing the distinction between solid and dissolved product."),
    (2025, 102, "3", "4", "syllabus:1.2.1", "omission", "Planning answers used 'amount' or 'drops' for hydrochloric acid instead of specifying a controlled volume."),
]

DIAGNOSTICS = [
    "Compare the anode product for copper(II) sulfate using a copper anode and an inert carbon anode; explain the role of the electrode.",
    "Choose the separation steps for an insoluble precipitate and a soluble salt made in solution, explaining why the sequences differ.",
    "Given two reaction curves, identify which is faster using gradient rather than total elapsed time.",
    "Calculate a titre from two burette readings, stating which reading is initial and which is final.",
    "Given proton, neutron and electron counts, select isotopes of one element and explain the shared and differing counts.",
    "Match a flame colour test, a glowing splint test and a lighted splint test to the substances each can identify.",
    "Decide whether two carbon structures are isotopes or allotropes, and justify using atomic nuclei versus structure.",
    "Distinguish one mole as an amount of substance from the Avogadro constant as particles per mole.",
    "Choose the correct splint test for oxygen and hydrogen, then state the expected result of each.",
    "Explain conductivity in molten magnesium chloride by naming the moving charged particles; contrast these with electrons in a metal.",
    "Given two mass readings at different times, calculate the mass lost over that interval and explain the subtraction.",
    "Compare the appearance of copper(II) carbonate powder with blue copper(II) sulfate solution.",
    "Explain what a plateau in a gas-volume-versus-time graph means for reactant consumption and rate.",
    "Place a marked cross in a disappearing-cross rate experiment and explain how it signals the endpoint.",
    "Count electrons in bromine and bromide, then explain the one-electron difference from charge.",
    "Draw electron transfer for magnesium bromide and distinguish it from a covalent shared pair.",
    "Name the charge carrier in molten magnesium bromide and explain why it can move.",
    "Given proton and electron counts, classify a particle as an atom or an ion and state the reason.",
    "After excess ammonia is added to a copper(II) mixture, distinguish the precipitate from the coloured solution.",
]

# Printed subpart labels are resolved to the marked-part index where extraction
# groups diagrams and compound prompts differently from text line breaks.
FINDING_PART_TARGETS = {
    (2022, "3", "2(b)"): {2},
    (2024, "2", "2(a)"): {1},
    (2024, "2", "2(c)"): {3},
    (2024, "2", "2(d)(ii)"): {5},
    (2025, "2", "1(b)(ii)"): {7},
    (2025, "3", "3(b)"): {2},
}


def report_path(year):
    if year < 2024:
        return next((ROOT / f"Question Banks/Namibian Curricula/NSSCO (New)/Chemistry (6117)/{year}").glob("*Report*.pdf"))
    return next((ROOT / f"Question Banks/Namibian Examiner Reports/NSSCO (New) /{year}").glob("*.pdf"))


def main():
    verify_findings(FINDINGS, report_path, WORK / 'assessment-evidence/report-citation-audit.json')
    records = []
    misconceptions = []
    diagnostic_index = 0
    for index, (year, page, paper, question, objective, kind, finding) in enumerate(FINDINGS, 1):
        source = report_path(year).relative_to(ROOT)
        locator = f"{source}, PDF viewer p. {page}, Chemistry 6117 Paper {paper}" + (f" Q{question}" if question else "")
        records.append({
            "evidence_id": f"ER-6117-{year}-{index:02d}",
            "source_id": f"ER-6117-{year}",
            "evidence_type": "examiner_report",
            "exam_series": "Oct/Nov",
            "year": year,
            "paper_id": paper,
            "variant": None,
            "question_ref": question,
            "mark_tariff": None,
            "objective_ids": [objective],
            "command_word": None,
            "ao_focus": ["C"] if paper == "3" else ["A", "B"],
            "context_type": "examiner finding",
            "context_summary": finding,
            "creditworthy_points": [],
            "examiner_findings": [finding],
            "common_errors": [finding],
            "strong_response_features": [],
            "source_locator": locator,
            "notes": [kind, "Mapped by reading the reported task and its chemistry meaning; syllabus subtopic IDs are provisional until the objective registry exists."],
        })
        if (year, paper, question) == (2024, '2', '2(d)(ii)'):
            records[-1]['notes'].append('Question context: the paper asks why the ionic compound must be aqueous or molten. The report itself says only that some candidates used electrons instead of ions; molten is not part of that report comment.')
        if kind == "misconception":
            misconceptions.append({
                "id": f"MIS-6117-{len(misconceptions)+1:02d}",
                "syllabus_subtopic": objective,
                "confusion": finding,
                "diagnostic_test": DIAGNOSTICS[diagnostic_index],
                "evidence_id": records[-1]["evidence_id"],
            })
            diagnostic_index += 1
    assert diagnostic_index == len(DIAGNOSTICS)
    question_parts = json.loads((WORK / "assessment-evidence/question_parts.json").read_text())["records"]
    guidance = json.loads((WORK / "assessment-evidence/report-guidance-alignment.json").read_text())
    verify_answer_links(guidance['aligned_parts'], report_path, WORK / 'assessment-evidence/report-answer-page-audit.json')
    reviewed_links = json.loads((WORK / "assessment-evidence/report-alignment-audit.json").read_text())
    verified_ids = {entry["evidence_id"] for entry in reviewed_links["parts"] if entry["status"].startswith("verified_")}
    assert set(guidance["aligned_parts"]) == {entry["evidence_id"] for entry in reviewed_links["parts"]}
    manual_guidance = {}
    for filename in ("manual-credit-2020.json", "manual-credit-supplement.json"):
        manual_guidance.update(json.loads((WORK / "assessment-evidence" / filename).read_text())["records"])
    verify_manual_plans(manual_guidance, report_path, WORK / 'assessment-evidence/manual-plan-page-audit.json')
    # Representative point-level guidance transcribed by meaning from the 2025
    # report's answer tables. Keep the report wording out of learner resources.
    credit = {
        ("2", "Q1, marked part 7"): ["Identify the electron excess relative to protons, or that an electron was gained."],
        ("2", "Q1, marked part 8"): ["Identify a valid isotope pair.", "Explain that proton count is the same while neutron count differs."],
        ("2", "Q2, marked part 1"): ["State that an acid donates a proton."],
        ("2", "Q2, marked part 2"): ["Give the complete neutralisation ionic equation with both reactants and water product."],
        ("2", "Q2, marked part 3"): ["Name a suitable sodium compound.", "Name sulfuric acid as the second reagent."],
        ("2", "Q2, marked part 7"): ["Use concentration times volume in dm³ to obtain 0.00400 mol HCl. The report's ‘0.02 seen’ line conflicts with the question and its following mole-ratio answer; see source-discrepancies.json.", "Show sufficient working for the calculation credit."],
        ("2", "Q2, marked part 8"): ["Apply the two-to-one mole ratio from the equation; follow-through from the preceding result is allowed."],
        ("2", "Q2, marked part 9"): ["Determine the relative formula mass.", "Use amount times relative formula mass to obtain mass; follow-through is allowed."],
        ("3", "Q1, marked part 1"): ["State the distinct purposes of the separation apparatus and condenser."],
        ("3", "Q1, marked part 7"): ["Choose a heating method without a naked flame.", "Explain the choice from the flammability of the mixture."],
        ("3", "Q2, marked part 4"): ["Measure mass.", "Measure elapsed time."],
        ("3", "Q2, marked part 5"): ["Show a reaction vessel.", "Show a labelled gas collection and measurement device.", "Make the gas path closed and unblocked."],
        ("3", "Q2, marked part 6"): ["Plot the full data series correctly.", "Draw an appropriate smooth best curve."],
        ("3", "Q2, marked part 7"): ["Read the first interval from the graph.", "Subtract that reading from the later cumulative volume for the next interval."],
        ("3", "Q2, marked part 8"): ["Calculate volume per second for the first interval.", "Calculate volume per second for the second interval."],
        ("3", "Q3, marked part 1"): ["Describe the precipitate colour.", "State that it remains insoluble in excess reagent."],
        ("3", "Q3, marked part 2"): ["Describe the initial precipitate.", "State its dissolution in excess reagent.", "Describe the resulting solution colour."],
        ("3", "Q3, marked part 4"): ["Identify the cation.", "Identify the anion."],
        ("3", "Q4, marked part 1"): [
            "M1 (1 mark): put each metal separately in contact with hydrochloric acid using a suitable reaction vessel.",
            "M2–M3 (2 marks together): make a fair comparison using distinct controls from acid volume, acid concentration, acid temperature, metal surface area or form, and metal mass; the report caps this section at two marks from four valid control points.",
            "M4–M5 (2 marks together): state a coherent pair of measurements. Accepted routes include timing from metal addition until reaction ends, measuring gas volume after a fixed interval, or comparing initial and peak temperatures.",
            "M6 (1 mark): rank the metals from the chosen measure; shorter time, greater fixed-time gas volume, or greater temperature change indicates the more reactive metal, as applicable.",
            "Apparatus earns credit only when its use in the method is stated; a bare list does not earn that credit.",
        ],
    }
    for row in question_parts:
        row["notes"].append("Mapping: " + row.pop("mapping_method") + "; confidence: " + row.pop("mapping_confidence") + "; chemistry context: " + row.pop("context_topic_id"))
        row["notes"].append("Command source: " + row.pop("command_origin"))
        skill = row.pop("practical_skill_type", None)
        if skill:
            row["notes"].append("Practical skill type: " + skill)
        source_rows = guidance["aligned_parts"].get(row["evidence_id"]) if row["evidence_id"] in verified_ids else None
        if source_rows:
            row["notes"].append("Internal answer-table extraction: " + source_rows["source_locator"] + "; link verified in report-alignment-audit.json")
            if not row["creditworthy_points"]:
                row["creditworthy_points"] = [
                    "INTERNAL SOURCE ANSWER (paraphrase before learner use): " + re.sub(r"\s+", " ", source["source_text"]).strip()
                    for source in source_rows["source_rows"]
                ]
        elif row["paper_id"] != "1":
            row["notes"].append("No safely part-aligned answer-table row yet; see report-guidance-alignment.json for question-level status.")
        if row["year"] != 2025:
            continue
        points = credit.get((row["paper_id"], row["question_ref"]))
        if points:
            row["creditworthy_points"] = points
            row["notes"].append("Credit shape paraphrased from 2025 Chemistry examiner-report answer table; inspect the report for exact alternatives and allocations.")
            row["notes"].append("2025 examiner report PDF viewer pp. 93–94 (Paper 2) or pp. 100–102 (Paper 3).")
    for row in question_parts:
        manual = manual_guidance.get(row["evidence_id"])
        if manual:
            row["creditworthy_points"] = manual["creditworthy_points"]
            row["notes"].append(f"Paraphrased report credit structure; PDF viewer p. {manual['report_pdf_page']}.")
        for finding in records:
            if finding["year"] != row["year"] or finding["paper_id"] != row["paper_id"]:
                continue
            qref = finding["question_ref"]
            if qref and not row["question_ref"].startswith("Q" + re.match(r"\d+", qref).group() + ","):
                continue
            if qref is None:
                continue
            targets = FINDING_PART_TARGETS.get((finding["year"], finding["paper_id"], qref))
            if targets and int(row["question_ref"].rsplit(" ", 1)[-1]) not in targets:
                continue
            row["examiner_findings"].extend(finding["examiner_findings"])
            row["common_errors"].extend(finding["common_errors"])
    evidence = {
        "map_id": "AE-NAM-6117-NSSCO-2020-2025",
        "status": "partial",
        "records": question_parts + records,
    }
    (WORK / "assessment-evidence").mkdir(exist_ok=True)
    (WORK / "curriculum").mkdir(exist_ok=True)
    (WORK / "assessment-evidence/assessment_evidence.json").write_text(json.dumps(evidence, indent=2, ensure_ascii=False) + "\n")
    (WORK / "curriculum/misconceptions.json").write_text(json.dumps({"status": "curated", "records": misconceptions}, indent=2, ensure_ascii=False) + "\n")
    print(f"Wrote {len(question_parts)} paper items/parts, {len(records)} examiner findings and {len(misconceptions)} curated misconceptions")


if __name__ == "__main__":
    main()
