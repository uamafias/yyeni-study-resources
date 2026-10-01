#!/usr/bin/env python3
"""Author ITEM-9702-9-P01/P02/P03 (performance tasks) for topic 9 and merge with the
80 flashcards built by _build_items.py into learning-items/topic_9_items.json."""
import json, os, sys, hashlib

WS = '/Users/professor/Documents/YYeni Study Resources/work/cie-9702-as-2025-2027'
TD = os.path.join(WS, 'topics', '9')
sys.path.insert(0, '/Users/professor/Documents/YYeni Study Resources/standard/v0.2.0-draft/checks')
from yyeni_checks import _artefact_text

def H(x):
    return hashlib.sha256(_artefact_text(x).encode()).hexdigest()

CTX = {"sector": None, "business_size": None, "ownership": None, "situation": None, "facts": []}

def task(item_id, objectives, claims, item_type, aos, blooms, cw, tariff, difficulty,
         prompt, answer, guidance, provenance):
    it = {
        "item_id": item_id, "objective_ids": objectives, "claim_ids": claims,
        "item_type": item_type, "subtype": None, "assessment_objectives": aos,
        "blooms_level": blooms, "command_word": cw, "mark_tariff": tariff,
        "difficulty": difficulty, "prompt": prompt, "canonical_answer": answer,
        "marking_guidance": guidance, "context": dict(CTX),
        "prerequisite_item_ids": [], "core_status": "core",
        "intentional_duplicate_group": None, "provenance": provenance,
        "qa_status": "review_required",
        "claims_seen": {c: 1 for c in claims},
    }
    it["authored_hash"] = H(it)
    return it

tasks = []

# ---------------- P01: multiple_choice_set, 12 questions, Paper 1 style ----------------
tasks.append(task(
 "ITEM-9702-9-P01",
 ["OBJ-9702-9.1-03", "OBJ-9702-9.1-04", "OBJ-9702-9.2-02", "OBJ-9702-9.3-02",
  "OBJ-9702-9.3-03", "OBJ-9702-9.3-06", "OBJ-9702-9.3-07", "OBJ-9702-9.3-08"],
 ["CLM-9702-9-006", "CLM-9702-9-008", "CLM-9702-9-010", "CLM-9702-9-012",
  "CLM-9702-9-019", "CLM-9702-9-020", "CLM-9702-9-023", "CLM-9702-9-021",
  "CLM-9702-9-027", "CLM-9702-9-029", "CLM-9702-9-030", "CLM-9702-9-031"],
 "multiple_choice_set", ["AO1", "AO2"], "Apply", None, 12, 2,
 "Twelve questions in the style of Paper 1. Choose one option for each.\n\n"
 "1. A current of 0.50 A flows for 2.0 minutes. What charge passes a point in the wire?\n"
 "A  1.0 C\nB  60 C\nC  240 C\nD  4.0 C\n\n"
 "2. In I = Anvq, the symbol n stands for\n"
 "A  the total number of free electrons in the conductor\n"
 "B  the charge on one carrier\n"
 "C  the number of charge carriers per cubic metre\n"
 "D  the drift speed of the carriers\n\n"
 "3. The p.d. across a component is 12 V and 48 J of energy is converted from electrical form. "
 "What charge passed through the component?\n"
 "A  576 C\nB  4.0 C\nC  0.25 C\nD  60 C\n\n"
 "4. A component carries a current of 0.25 A when the p.d. across it is 6.0 V. Its resistance is\n"
 "A  1.5 Ω\nB  24 Ω\nC  0.042 Ω\nD  41 Ω\n\n"
 "5. On an I–V graph, the resistance at a point is\n"
 "A  the gradient of the graph at that point\n"
 "B  the area under the graph up to that point\n"
 "C  the current divided by the p.d. at that point\n"
 "D  the p.d. divided by the current at that point\n\n"
 "6. Which I–V characteristic is a straight line through the origin?\n"
 "A  a filament lamp at its rated current\n"
 "B  a semiconductor diode in the forward direction\n"
 "C  a metallic conductor at constant temperature\n"
 "D  a thermistor as it warms\n\n"
 "7. A diode in the forward direction passes a very small current at p.d. below about\n"
 "A  0.7 V\nB  7.0 V\nC  0.07 V\nD  70 V\n\n"
 "8. A wire of resistance R is replaced by a wire of the same metal with twice the length and "
 "twice the diameter. The new resistance is\n"
 "A  4R\nB  2R\nC  R/2\nD  R\n\n"
 "9. The unit of resistivity is\n"
 "A  Ω\nB  Ω m\nC  Ω m⁻¹\nD  Ω m²\n\n"
 "10. As the light intensity on a light-dependent resistor increases, its resistance\n"
 "A  increases\nB  decreases\nC  stays constant\nD  becomes zero\n\n"
 "11. As the temperature of a thermistor rises, its resistance\n"
 "A  rises, like a metal's\nB  falls, unlike a metal's\nC  stays constant\nD  becomes infinite\n\n"
 "12. A copper wire and a constantan wire have the same length and cross-sectional area. "
 "They have different resistances because they differ in\n"
 "A  resistivity\nB  length\nC  area\nD  number of drift speeds",
 "Key: 1 B, 2 C, 3 B, 4 B, 5 D, 6 C, 7 A, 8 C, 9 B, 10 B, 11 B, 12 A.\n"
 "1. Q = It: convert first, 2.0 minutes = 120 s, then 0.50 × 120 = 60 C, so B. A forgets the minutes-to-seconds conversion; C multiplies by 480; D divides instead of multiplying.\n"
 "2. n is the number density, carriers per cubic metre, so C. A is the total count, the error the misconception register names; B is q; D is v.\n"
 "3. Q = W/V: 48 ÷ 12 = 4.0 C, so B. A multiplies instead of dividing; C inverts the ratio; D divides by the wrong quantity.\n"
 "4. R = V/I: 6.0 ÷ 0.25 = 24 Ω, so B. A multiplies; C divides the wrong way round; D is a power-of-ten slip.\n"
 "5. Resistance at a point is V/I, the ratio of the coordinates, so D. A is the gradient error the register names; B confuses resistance with an area; C inverts the ratio.\n"
 "6. Only the metallic conductor at constant temperature gives proportionality, so C. A curves over as its temperature rises; B hugs the current axis then rises steeply; D changes resistance as conditions change.\n"
 "7. The forward threshold is about 0.7 V, so A. B, C and D are power-of-ten slips.\n"
 "8. Twice the length doubles R; twice the diameter makes the area four times larger, which quarters it. Together R × 2 ÷ 4 = R/2, so C. A squares both changes; B forgets the area; D treats them as cancelling.\n"
 "9. From R = ρL/A, ρ = RA/L, so the unit is Ω × m² ÷ m = Ω m, B. A is the unit of resistance; C divides by the wrong length power; D forgets to divide by L.\n"
 "10. Brighter light releases more charge carriers, so the resistance decreases, B. A reverses the direction, the error the register names; C and D ignore the mechanism.\n"
 "11. For a thermistor the resistance falls as temperature rises, unlike a metal's, so B. A gives the metal's behaviour; C and D ignore the release of carriers.\n"
 "12. Same length and area, so the difference is the material property, resistivity, A. B and C are given as the same; D is not a property at all.",
 ["The key: one mark per question, twelve marks in all — 1 B, 2 C, 3 B, 4 B, 5 D, 6 C, 7 A, 8 C, 9 B, 10 B, 11 B, 12 A.",
  "Each distractor is a named error: a minutes-to-seconds conversion slip, the total count in place of the number density, an inverted ratio, the gradient taken for V/I, a reversed direction of change for the LDR and the thermistor (the misconception register first)."],
 "Authored for the 9702 topic 9 claim ledger as a Paper 1 style multiple-choice set."))

# ---------------- P02: short_answer, ~8 marks, Paper 2 style ----------------
tasks.append(task(
 "ITEM-9702-9-P02",
 ["OBJ-9702-9.1-03", "OBJ-9702-9.2-01", "OBJ-9702-9.2-02", "OBJ-9702-9.3-04"],
 ["CLM-9702-9-006", "CLM-9702-9-011", "CLM-9702-9-012", "CLM-9702-9-013",
  "CLM-9702-9-024", "CLM-9702-9-019"],
 "short_answer", ["AO1", "AO2"], "Apply", "Define", 8, 3,
 "A desk lamp at a hostel in Ongwediva runs at a p.d. of 230 V and carries a current of 0.26 A. "
 "Answer the parts about this lamp.\n"
 "(a) Define the potential difference across a component. [1]\n"
 "(b) Calculate the charge that passes through the lamp in 5.0 minutes. [2]\n"
 "(c) Calculate the energy converted from electrical form in the lamp in 5.0 minutes. [2]\n"
 "(d) The lamp's filament is a thin metal wire. Explain why the resistance of the filament while "
 "the lamp runs is larger than the resistance measured with a tiny test current. [2]\n"
 "(e) State what is meant by an electric current. [1]",
 "(a) The potential difference across a component is the energy transferred from electrical to other "
 "forms per unit charge passing through it.\n"
 "(b) Equation: Q = It. Substitution: 5.0 minutes is 300 s, and Q = 0.26 × 300 = 78 C.\n"
 "Answer: 78 C.\n"
 "(c) Equation: W = VQ (or W = VIt). Substitution: W = 230 × 78 = 17940 J.\n"
 "Answer: 17940 J, so 1.8 × 10⁴ J to two significant figures.\n"
 "(d) At its running current the filament is hot, and its temperature rises with the current: the "
 "lattice ions vibrate with greater amplitude, so the conduction electrons collide with them more "
 "often and the ratio V/I is larger. A tiny test current leaves the filament near room temperature, "
 "where its resistance is smaller.\n"
 "(e) An electric current is a flow of charge carriers, such as the conduction electrons in the "
 "filament; the current at a point is the charge passing per unit time, I = Q/t.",
 ["Marks: (a) 1 — the definition as energy per unit charge, with the equation V = W/Q an equally full statement; "
  "(b) 2 — the equation Q = It with the time converted to 300 s and the substitution, giving 78 C with its unit; "
  "(c) 2 — the equation W = VQ, the substitution 230 × 78 = 17940, and the answer 1.8 × 10⁴ J with its unit; "
  "(d) 2 — the reason: the running current heats the filament, so its lattice ions vibrate with greater amplitude "
  "and the electrons collide with them more often, so the resistance is larger at the higher temperature; "
  "(e) 1 — a flow of charge carriers, with the rate idea I = Q/t accepted.",
  "Each part's marks are separate points; (b) and (c) need the equation before the substitution, because "
  "the working earns marks before the answer; every quantity carries its unit and the reason in (d) is "
  "physical, in the lattice, not a restatement of the observation."],
 "Authored for the 9702 topic 9 claim ledger as a Paper 2 style structured question."))

# ---------------- P03: calculation, ~5 marks ----------------
tasks.append(task(
 "ITEM-9702-9-P03",
 ["OBJ-9702-9.2-03", "OBJ-9702-9.3-02", "OBJ-9702-9.3-06"],
 ["CLM-9702-9-014", "CLM-9702-9-015", "CLM-9702-9-019", "CLM-9702-9-027",
  "CLM-9702-9-029"],
 "calculation", ["AO1", "AO2"], "Apply", "Calculate", 5, 3,
 "A heating element for a greenhouse at a farm near Mariental is a single uniform wire of the alloy "
 "constantan, 9.5 m long and 1.2 mm in diameter. The resistivity of constantan is 4.9 × 10⁻⁷ Ω m. "
 "The element is connected to a supply that keeps a p.d. of 230 V across it. Calculate the resistance "
 "of the wire, the current in it and the power it converts, giving each intermediate value to three "
 "significant figures and stating the number of significant figures in your final answers.",
 "Equation: the area is A = πd²/4, the resistance is R = ρL/A, the current is I = V/R and the power "
 "is P = VI.\n"
 "Area: convert the diameter first, 1.2 mm = 1.2 × 10⁻³ m. Then d² = (1.2 × 10⁻³)² = 1.44 × 10⁻⁶ m², "
 "and A = 3.142 × 1.44 × 10⁻⁶ ÷ 4 = 1.13 × 10⁻⁶ m².\n"
 "Resistance: R = ρL/A = (4.9 × 10⁻⁷ × 9.5) ÷ (1.13 × 10⁻⁶). The top line is 4.655 × 10⁻⁶, and "
 "4.655 × 10⁻⁶ ÷ 1.13 × 10⁻⁶ = 4.12 Ω.\n"
 "Answer: R = 4.12 Ω to three significant figures.\n"
 "Current: I = V/R = 230 ÷ 4.12 = 55.8 A to three significant figures.\n"
 "Power: P = VI = 230 × 55.8 = 12834 W.\n"
 "Answer: P = 12834 W, so 12800 W to three significant figures — three, because the working carries "
 "three and every datum supports it; the resistance is stated to two as 4.1 Ω when the data are "
 "counted strictly, because the resistivity datum 4.9 × 10⁻⁷ and the diameter 1.2 each carry two "
 "significant figures.",
 ["Equation: A = πd²/4, then R = ρL/A, then I = V/R, then P = VI, in symbols — 1 mark.",
  "Substitution and working: the area 1.13 × 10⁻⁶ m², the resistance 4.12 Ω, the current 55.8 A, "
  "each intermediate value to three significant figures — 2 marks.",
  "Answer: the resistance 4.1 Ω, the current 56 A and the power 12800 W, each with its unit and the "
  "number of significant figures justified against the data — 2 marks."],
 "Authored for the 9702 topic 9 claim ledger as a Paper 2 style multi-step calculation."))

# ---------------- merge with part 1 and write the dataset ----------------
part1_path = os.path.join(TD, '_items_part1.json')
if not os.path.exists(part1_path):
    raise SystemExit('run _build_items.py first to produce _items_part1.json')
part1 = json.load(open(part1_path))
assert len(part1) == 80, len(part1)

allitems = part1 + tasks
dataset = {
    "dataset_id": "ITEMS-9702-9",
    "topic_id": "9",
    "items": allitems,
}
out = os.path.join(TD, 'learning-items', 'topic_9_items.json')
os.makedirs(os.path.dirname(out), exist_ok=True)
json.dump(dataset, open(out, 'w'), indent=1, ensure_ascii=False)
print('items total:', len(allitems), '->', out)
