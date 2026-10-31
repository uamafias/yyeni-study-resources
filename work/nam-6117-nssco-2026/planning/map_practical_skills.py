"""Human-read mapping of every Paper 3 marked part to syllabus C criteria."""

import json
import re
from pathlib import Path

WORK = Path(__file__).resolve().parents[1]

# Each entry follows the printed marked-part sequence within its main question.
# C1 safe technique/apparatus; C2 planning; C3 observation/measurement/recording;
# C4 interpretation/data; C5 method evaluation. The second axis preserves the
# specific practical task so graphs, tests and planning do not collapse together.
MAP = {
  2020: {
    1: "C1:separation C1:separation C1:separation",
    2: "C3:measurement C3:graph_plotting C3:graph_drawing C3:graph_drawing C4:graph_reading C4:calculation C4:graph_reading C4:calculation C5:method_improvement C4:graph_reading",
    3: "C4:observation_inference C1:apparatus_purpose C4:observation_inference C3:observation_recording C3:observation_recording C4:qualitative_inference C4:gas_identification C4:observation_inference C4:qualitative_inference",
    4: "C2:investigation_planning",
  },
  2021: {
    1: "C1:sample_preparation C1:measurement_accuracy C1:separation C1:apparatus_identification C3:chromatogram_label C4:chromatogram_interpretation C1:chromatography_technique C4:rf_calculation",
    2: "C3:graph_plotting C4:graph_reading C2:fair_test_control C5:error_and_improvement C4:graph_prediction",
    3: "C3:qualitative_observation C3:qualitative_observation C3:qualitative_observation C3:qualitative_observation C1:gas_test C4:qualitative_inference C1:safety",
    4: "C2:investigation_planning",
  },
  2022: {
    1: "C1:apparatus_identification C3:observation_recording C5:method_evaluation C3:measurement C4:calculation C4:method_interpretation C5:reliability_improvement",
    2: "C3:measurement C3:graph_plotting C4:graph_reading C4:prediction C4:calculation C4:rate_calculation C2:fair_test_control",
    3: "C3:qualitative_observation C3:qualitative_observation C4:observation_inference C1:separation C1:flame_test",
    4: "C2:investigation_planning",
  },
  2023: {
    1: "C1:gas_test C1:apparatus_identification C1:separation",
    2: "C3:measurement C3:graph_plotting C4:rate_calculation C4:observation_inference C4:rate_interpretation C5:method_evaluation",
    3: "C1:safety C4:qualitative_inference C4:qualitative_inference C1:safety C3:qualitative_observation C3:qualitative_observation C3:qualitative_observation C3:flame_observation",
    4: "C2:investigation_planning",
  },
  2024: {
    1: "C1:chromatography_technique C5:apparatus_error C1:chromatography_technique C4:chromatogram_interpretation C4:chromatogram_interpretation C5:method_improvement",
    2: "C1:apparatus_identification C1:separation C1:apparatus_drawing C4:observation_inference C1:crystallisation",
    3: "C3:data_table C3:graph_plotting C4:graph_reading C4:graph_prediction C4:observation_inference C1:gas_test",
    4: "C4:qualitative_inference C3:qualitative_observation C3:flame_observation C3:qualitative_observation C3:qualitative_observation",
    5: "C2:investigation_planning",
  },
  2025: {
    1: "C1:apparatus_purpose C1:apparatus_safety C5:apparatus_error C4:measurement_prediction C4:distillation_interpretation C4:distillation_interpretation C1:heating_safety",
    2: "C1:apparatus_identification C1:safety C1:apparatus_purpose C3:measurement_planning C1:apparatus_drawing C3:graph_plotting C4:graph_reading C4:rate_calculation C5:accuracy_evaluation",
    3: "C3:qualitative_observation C3:qualitative_observation C3:qualitative_observation C4:qualitative_inference",
    4: "C2:investigation_planning",
  },
}


def main():
    path = WORK / "assessment-evidence/question_parts.json"
    data = json.loads(path.read_text())
    seen = 0
    for row in data["records"]:
        if row["paper_id"] != "3":
            continue
        q = int(re.search(r"Q(\d+)", row["question_ref"]).group(1))
        part = int(re.search(r"marked part (\d+)", row["question_ref"]).group(1))
        entry = MAP[row["year"]][q].split()[part - 1]
        criterion, skill = entry.split(":")
        row["objective_ids"] = [f"syllabus:{criterion}"]
        row["practical_skill_type"] = skill
        row["mapping_method"] = "Human reading of marked practical task against syllabus AO C criteria; chemistry context retained separately."
        row["mapping_confidence"] = "high"
        seen += 1
    assert seen == 126
    for year, questions in MAP.items():
        for q, assignment in questions.items():
            actual = [row for row in data["records"] if row["year"] == year and row["paper_id"] == "3" and row["question_ref"].startswith(f"Q{q},")]
            assert len(assignment.split()) == len(actual), (year, q, len(assignment.split()), len(actual))
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print("Mapped", seen, "Paper 3 parts to C1–C5 and specific skill types")


if __name__ == "__main__":
    main()
