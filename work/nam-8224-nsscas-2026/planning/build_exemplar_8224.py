#!/usr/bin/env python3
"""Author the 8224 structural exemplars from the frozen work orders."""
from __future__ import annotations

import hashlib
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
WS = os.path.dirname(HERE)
ROOT = os.path.dirname(os.path.dirname(WS))
sys.path.insert(0, os.path.join(ROOT, "standard", "v0.2.0-draft", "checks"))
from yyeni_checks import _artefact_text  # noqa: E402


def load(path):
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)


def write(path, value):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(value, fh, indent=1, ensure_ascii=False)
        fh.write("\n")


def words(text):
    return len(re.findall(r"\b[\w′'⁻]+\b", text))


def stamp(value):
    value["authored_hash"] = hashlib.sha256(_artefact_text(value).encode()).hexdigest()


topic = "1.1"
topic_dir = os.path.join(WS, "topics", topic)
work_order = load(os.path.join(topic_dir, "work_order.json"))

claim_texts = {
    "OBJ-8224-1.1.1-01": [
        ("definition", "Relative isotopic mass is the mass of one atom of a specified isotope relative to one twelfth of the mass of one carbon-12 atom."),
        ("definition", "Relative atomic mass is the weighted mean mass of an atom of an element relative to one twelfth of the mass of one carbon-12 atom."),
        ("definition", "Relative molecular mass is the sum of the relative atomic masses in a molecule, while relative formula mass is the corresponding sum for a formula unit."),
    ],
    "OBJ-8224-1.1.2-01": [
        ("definition", "A mole is the amount of substance containing the Avogadro constant number of specified particles."),
        ("formula", "The amount of substance is n = N/NA, where N is the number of specified particles and NA is the Avogadro constant."),
        ("formula", "For a pure substance, amount in moles is n = m/M, where m is mass in grams and M is molar mass in g mol⁻¹."),
    ],
    "OBJ-8224-1.1.3-01": [
        ("interpretation", "In an atomic mass spectrum, a peak position identifies an isotopic mass and its relative intensity represents relative abundance."),
        ("interpretation", "A molecular-ion spectrum of a diatomic element can contain peaks for different pairs of isotopes, so the number of molecular peaks need not equal the number of isotopes."),
        ("scope", "Mass-spectrum questions in this syllabus require interpretation of masses and abundances, not an account of the instrument's operation."),
    ],
    "OBJ-8224-1.1.3-02": [
        ("formula", "Relative atomic mass is calculated as the sum of isotopic mass multiplied by abundance, divided by the sum of the abundances."),
        ("calculation", "When abundances are percentages their total is 100, but arbitrary peak heights must be divided by their actual total."),
        ("interpretation", "A relative atomic mass lies nearer the isotopic mass of the more abundant isotope because it is a weighted mean."),
    ],
    "OBJ-8224-1.1.3-03": [
        ("formula", "Percentage by mass of an element is the total relative mass contributed by that element in the formula divided by the relative formula or molecular mass, multiplied by 100%."),
        ("calculation", "A subscript in a chemical formula multiplies the relative atomic mass before the element's mass contribution is used."),
        ("interpretation", "Percentage composition compares mass contributions, not the fraction of atoms of each element."),
    ],
    "OBJ-8224-1.1.4-01": [
        ("definition", "An empirical formula gives the simplest whole-number ratio of atoms of each element in a compound."),
        ("definition", "A molecular formula gives the actual number of atoms of each element in one molecule."),
        ("relationship", "For a molecular substance, the molecular formula is a whole-number multiple of its empirical formula."),
    ],
    "OBJ-8224-1.1.4-02": [
        ("procedure", "To obtain an empirical formula from masses or percentages, convert each element to moles, divide by the smallest amount, then scale to whole numbers if necessary."),
        ("formula", "The molecular-formula multiplier is Mr divided by the empirical-formula mass."),
        ("procedure", "Combustion data are converted from masses of carbon dioxide and water to amounts of carbon and hydrogen before the simplest ratio is found."),
    ],
    "OBJ-8224-1.1.5-01": [
        ("principle", "A balanced chemical equation has the same number of atoms of each element on both sides because chemical reactions conserve atoms."),
        ("procedure", "Equation coefficients change the numbers of reacting particles; subscripts within correct chemical formulae are not changed to balance an equation."),
        ("representation", "State symbols identify physical states as (s), (l), (g) and (aq), with (aq) meaning dissolved in water."),
    ],
    "OBJ-8224-1.1.5-02": [
        ("formula", "A balanced equation supplies the mole ratio used to connect the amount of one reactant or product to another."),
        ("formula", "At the temperature and pressure specified by this syllabus, one mole of gas occupies 22.4 dm³ at s.t.p. and 24.0 dm³ at r.t.p."),
        ("formula", "Solution concentration is c = n/V when c is in mol dm⁻³, n is in mol and V is in dm³; volumes in cm³ are divided by 1000 before substitution."),
    ],
}

claims = []
claim_ids_by_objective = {}
n = 0
for objective_id, rows in claim_texts.items():
    claim_ids_by_objective[objective_id] = []
    for claim_type, text in rows:
        n += 1
        claim_id = f"CLM-8224-1.1-{n:03d}"
        claim_ids_by_objective[objective_id].append(claim_id)
        valid_claim_type = {
            "interpretation": "inference", "scope": "factual", "calculation": "formula",
            "relationship": "factual", "procedure": "procedural", "principle": "factual",
            "representation": "factual",
        }.get(claim_type, claim_type)
        claims.append({
            "claim_id": claim_id, "objective_ids": [objective_id], "text": text,
            "claim_type": valid_claim_type, "provenance": "generated_gap",
            "evidence": [{"source_id": "NSSCAS-8224-SYLLABUS", "locator": objective_id,
                          "support_type": "paraphrase"}],
            "derived_from_claim_ids": [], "revision": 1,
            "verification": {"status": "unverified", "method": "Authored from the verified 8224 syllabus objectives and transparent chemical derivation; requires independent semantic review under RS-28.", "reviewer_id": None, "reviewed_at": None, "confidence": 0.9},
            "publishable": False, "notes": [],
        })

ledger = {"ledger_id": "CLM-LEDGER-8224-1.1", "claims": claims}
write(os.path.join(topic_dir, "claims", "canonical_claim_ledger.json"), ledger)

unit_blocks = {
    "1.1.1": [
        ("learner_objective", "What relative mass means", "Chemical masses at this level are relative numbers. They compare an atom, molecule or formula unit with one twelfth of the mass of one carbon-12 atom. Because both masses are divided by the same reference mass, relative masses have no unit. The carbon-12 reference gives chemists a consistent scale for atoms that are too small to weigh individually in grams."),
        ("definition", "Four related quantities", "Relative isotopic mass refers to one specified isotope. Carbon-13 therefore has a relative isotopic mass close to 13. Relative atomic mass, Ar, is different: it is the weighted mean for the naturally occurring isotopes of an element. Its value can therefore be non-integral. Relative molecular mass, Mr, adds the Ar values of all atoms in one molecule. For CO2, Mr = 12.0 + (2 × 16.0) = 44.0. Relative formula mass is found in the same way for substances described by formula units rather than separate molecules. For MgO it is 24.3 + 16.0 = 40.3. Calling this a molecular mass would wrongly imply that ionic magnesium oxide exists as separate MgO molecules."),
        ("worked_example", "Choosing the correct mass", "A sample contains chlorine atoms, Cl2 molecules and sodium chloride. Use relative atomic mass for one chlorine atom or for the average mass of chlorine atoms in nature. Use relative molecular mass for Cl2 because it consists of molecules: Mr = 2Ar(Cl). Use relative formula mass for NaCl because the formula represents the simplest ratio of ions in its lattice. The arithmetic is similar, but the name records what kind of chemical entity the formula represents."),
        ("cross_link", "Where this leads", "Relative masses become molar masses when expressed in g mol⁻¹. That connection is used throughout stoichiometry. Atomic structure in topic 1.2 explains isotopes more fully, while the ideal-gas topic 1.4 develops gas calculations beyond the fixed molar volumes used here."),
    ],
    "1.1.2": [
        ("learner_objective", "Counting chemical particles", "A mole is a counting amount, just as a dozen means twelve objects. One mole contains the Avogadro constant number of specified entities, approximately 6.02 × 10²³. The entity must be named: atoms, molecules, ions, electrons or formula units. One mole of oxygen atoms and one mole of oxygen molecules contain the same number of named entities, but the molecules contain twice as many oxygen atoms."),
        ("definition", "Amount of substance", "Amount of substance has symbol n and unit mol. The particle relationship is n = N/NA, where N is the number of specified particles and NA is the Avogadro constant. Conversely, N = nNA. If a sample contains 0.250 mol of sodium ions, the number of ions is 0.250 × 6.02 × 10²³ = 1.505 × 10²³, reported as 1.51 × 10²³ ions to three significant figures."),
        ("worked_example", "From mass to moles", "Molar mass is the mass of one mole. Its numerical value follows from relative mass but it carries the unit g mol⁻¹. Water has Mr = 18.0, so its molar mass is 18.0 g mol⁻¹. For 4.50 g of water, n = m/M = 4.50 ÷ 18.0 = 0.250 mol. This amount contains 0.250 mol of water molecules, 0.500 mol of hydrogen atoms and 0.250 mol of oxygen atoms. The formula decides how particle counts are related."),
        ("cross_link", "Moles connect measurements to equations", "A balance measures mass, a gas syringe measures volume and volumetric apparatus measures solution volume. The mole converts each measurement into the common amount used by a balanced equation. That is why later calculations first convert the given quantity to moles, apply the equation ratio, then convert to the requested quantity."),
    ],
    "1.1.3": [
        ("learner_objective", "Reading isotope evidence", "A mass spectrum provides peak positions and relative intensities. For an atomic spectrum, a peak position corresponds to an isotopic mass and its intensity shows relative abundance. Interpretation begins with the species named in the question. A spectrum of atoms is not read in the same way as the molecular-ion region of a diatomic element."),
        ("explanation", "Atomic and molecular peaks", "Suppose an element X has isotopes of mass 35 and 37. Its atomic spectrum has two isotope peaks. Molecules X2 can contain 35-35, 35-37 or 37-37, producing molecular-ion masses 70, 72 and 74. Three molecular peaks therefore arise from two isotopes. The middle mass can be formed in two arrangements, so its expected relative intensity also reflects the number of combinations. The discriminating question is whether the peak represents one atom's ion or a molecule made from two atoms."),
        ("worked_calculation", "A weighted mean from percentages", "An element has isotopes of mass 24, 25 and 26 with abundances 79.0%, 10.0% and 11.0%. Multiply each mass by its abundance, add, and divide by the total abundance: Ar = [(24 × 79.0) + (25 × 10.0) + (26 × 11.0)] ÷ 100. The numerator is 1896 + 250 + 286 = 2432. Then 2432 ÷ 100 = 24.32. The answer lies close to 24 because mass 24 is the most abundant isotope."),
        ("worked_calculation", "Peak heights that are not percentages", "A spectrum shows isotope peaks at 63 and 65 with relative heights 9 and 4. The heights total 13, not 100. The correct mean is [(63 × 9) + (65 × 4)] ÷ 13 = (567 + 260) ÷ 13 = 827 ÷ 13 = 63.615..., so Ar = 63.6 to three significant figures. Dividing by 100 would give 8.27, which is outside the two isotopic masses and cannot be their weighted mean. A quick range check catches the error."),
        ("formula", "Percentage by mass", "For an element E in a compound, percentage by mass = (total Ar of E in the formula ÷ Mr or relative formula mass of the compound) × 100%. The word total matters because a subscript counts repeated atoms. In ammonium nitrate, NH4NO3, nitrogen contributes 2 × 14.0 = 28.0 while the relative formula mass is 80.0. The nitrogen percentage is 28.0 ÷ 80.0 × 100% = 35.0%. Counting only one nitrogen atom would halve the numerator incorrectly."),
        ("worked_calculation", "Comparing composition", "Calcium carbonate, CaCO3, has relative formula mass 40.1 + 12.0 + (3 × 16.0) = 100.1. Oxygen contributes 48.0, so its percentage by mass is 48.0 ÷ 100.1 × 100% = 47.952...%, or 48.0% to three significant figures. Percentages compare masses, not numbers of atoms: oxygen is three of the five atoms in the formula unit, but it is not 60% of the mass because the atoms have different relative masses."),
        ("interpretation", "Reasonableness checks", "A weighted mean must lie between the smallest and largest isotopic masses. A percentage by mass must lie from 0% to 100%. The mean should be pulled towards the more intense peak, and an element with a larger total mass contribution should have a larger percentage. These checks do not replace working, but they reveal an inverted ratio, a missed subscript or the wrong abundance total before the answer is accepted."),
        ("cross_link", "Scope and later use", "Only the masses and abundances shown by a spectrum are needed here; an account of the instrument is outside this objective. Weighted means and percentage composition feed directly into empirical-formula work in 1.1.4 and into reacting-mass calculations in 1.1.5."),
    ],
    "1.1.4": [
        ("learner_objective", "Two kinds of formula", "An empirical formula gives the simplest whole-number ratio of atoms of each element in a compound. A molecular formula gives the actual number of each kind of atom in one molecule. Ethene has molecular formula C2H4 and empirical formula CH2. A molecular formula is a whole-number multiple of the empirical formula, but the multiplier is not known from percentage composition alone. Later organic work also distinguishes structural condensed, displayed and skeletal formula representations; those show connectivity or shape in ways an empirical formula does not."),
        ("procedure", "From composition to empirical formula", "Treat percentage data as masses in a 100 g sample. Divide each mass by the element's Ar to obtain moles. Divide every mole value by the smallest. If the ratios are close to whole numbers, round only after considering the precision of the data. If a ratio is close to 1.5, 1.33 or 1.25, multiply all ratios by 2, 3 or 4 respectively. Multiplying only one ratio destroys the relative composition."),
        ("worked_calculation", "Empirical formula from percentages", "A compound contains 40.0% carbon, 6.7% hydrogen and 53.3% oxygen by mass. For 100 g: carbon moles = 40.0 ÷ 12.0 = 3.333; hydrogen moles = 6.7 ÷ 1.0 = 6.700; oxygen moles = 53.3 ÷ 16.0 = 3.331. Divide by 3.331 to obtain approximately 1.00 : 2.01 : 1.00. The simplest ratio is 1 : 2 : 1, so the empirical formula is CH2O. Formulae do not include decimal subscripts."),
        ("worked_calculation", "From empirical to molecular formula", "The empirical-formula mass of CH2O is 12.0 + 2.0 + 16.0 = 30.0. If the molecule has Mr = 180, the multiplier is 180 ÷ 30.0 = 6. The molecular formula is therefore C6H12O6. The multiplier must be a whole number because a molecule contains whole atoms. A non-integral result signals inconsistent data, incorrect relative masses or a wrong empirical formula."),
        ("worked_calculation", "Using combustion data", "Complete combustion converts all carbon in an organic sample to carbon dioxide and all hydrogen to water. If 0.880 g of CO2 forms, n(CO2) = 0.880 ÷ 44.0 = 0.0200 mol, so n(C) = 0.0200 mol. If 0.450 g of water forms, n(H2O) = 0.450 ÷ 18.0 = 0.0250 mol, so n(H) = 2 × 0.0250 = 0.0500 mol. The ratio C:H is 0.0200:0.0500 = 2:5. Any oxygen in the original compound must be found from a mass difference before its mole amount is included."),
        ("cross_link", "Formulae and equations", "A correct formula is fixed before an equation is balanced. The empirical formula describes composition; equation coefficients describe reacting amounts. Keeping those roles separate prevents the common error of altering a subscript in order to balance a reaction."),
    ],
    "1.1.5": [
        ("learner_objective", "Equations as amount relationships", "A chemical equation communicates identities, states and reacting ratios. First write correct chemical formulae. Then change coefficients until every element has the same atom count on each side. Do not alter formula subscripts. Add state symbols when the substances' states are known: (s), (l), (g) and (aq), where aqueous means dissolved in water."),
        ("worked_example", "Balancing with states", "Magnesium burns in oxygen to form magnesium oxide. The correct formulae are Mg, O2 and MgO. Oxygen is diatomic, so begin with Mg + O2 → MgO. Put 2 before MgO to give two oxygen atoms on the right, then 2 before Mg to restore magnesium balance: 2Mg(s) + O2(g) → 2MgO(s). The coefficients give the mole ratio 2:1:2."),
        ("procedure", "The stoichiometric route", "For reacting-mass, gas-volume and solution calculations, use the same route. Convert the given quantity to moles. Use the balanced-equation coefficient ratio. Convert the resulting moles to the requested mass, gas volume, concentration or solution volume. Units are part of the data: mass uses molar mass, gas volume uses the molar volume at the stated temperature and pressure, and solution work uses c = n/V with V in dm³."),
        ("worked_calculation", "Reacting masses", "Calcium carbonate decomposes: CaCO3(s) → CaO(s) + CO2(g). The mole ratio CaCO3:CaO is 1:1. For 25.0 g CaCO3, n = 25.0 ÷ 100.1 = 0.24975 mol. Therefore n(CaO) = 0.24975 mol. With M(CaO) = 56.1 g mol⁻¹, mass = 0.24975 × 56.1 = 14.011... g, so 14.0 g to three significant figures. Rounding the intermediate amount to 0.250 mol happens to be close here, but retaining digits protects the final answer."),
        ("worked_calculation", "Gas volumes at r.t.p. and s.t.p.", "Methane burns as CH4(g) + 2O2(g) → CO2(g) + 2H2O(l). At r.t.p., 0.350 mol CH4 needs 2 × 0.350 = 0.700 mol O2. Using 24.0 dm³ mol⁻¹ at r.t.p., V(O2) = 0.700 × 24.0 = 16.8 dm³. If the same amount were specified at s.t.p., the value would be 0.700 × 22.4 = 15.68 dm³. The condition named in the question selects the molar volume; it is not chosen from memory without checking."),
        ("worked_calculation", "Solutions", "A sodium hydroxide solution has concentration 0.150 mol dm⁻³ and volume 25.0 cm³. Convert the volume: 25.0 cm³ ÷ 1000 = 0.0250 dm³. Then n = cV = 0.150 × 0.0250 = 0.00375 mol. Conversely, if 0.00600 mol is present in 40.0 cm³, c = n/V = 0.00600 ÷ 0.0400 = 0.150 mol dm⁻³. Substituting a volume in cm³ directly would make the result 1000 times wrong."),
        ("interpretation", "Limiting amounts and significant figures", "When amounts of two reactants are supplied, compare moles divided by their equation coefficients. The smaller quotient identifies the reactant that runs out first and therefore limits the product. Carry extra digits through the calculation, then round the final answer to a precision justified by the data. State the unit and, for gases, the temperature and pressure. A bare number does not communicate the measured quantity."),
        ("cross_link", "Connections", "Topic 1.4 replaces fixed molar-volume relationships with pV = nRT when pressure and temperature are supplied. Later inorganic and organic topics provide many reactions to which the same balancing and mole-ratio method applies."),
    ],
}

supplements = {
    "1.1.1": "A relative mass answers a comparison question, so it is written without g or kg. The numerical value becomes a molar mass when the quantity is one mole and the unit g mol⁻¹ is attached. For example, Ar(Na) is 23.0, while the molar mass of sodium is 23.0 g mol⁻¹. Keeping the quantity and unit separate prevents a relative-mass answer from being given a mass unit.",
    "1.1.2": "The specified entity controls the conversion. One mole of Na2CO3 contains one mole of formula units, two moles of sodium ions and three moles of oxygen atoms. A question asking for ions therefore needs the formula subscript after the amount of formula units has been found. If 0.100 mol Na2CO3 is present, there are 0.200 mol Na+ ions, equal to 0.200 × 6.02 × 10²³ = 1.204 × 10²³ sodium ions. State the entity with the answer so that the count is meaningful.",
    "1.1.3": "Consider chlorine atoms with isotope peaks at 35 and 37 in a 3:1 intensity ratio. Using the heights directly, Ar = [(35 × 3) + (37 × 1)] ÷ 4 = 142 ÷ 4 = 35.5. If the same information is written as 75% and 25%, the result is [(35 × 75) + (37 × 25)] ÷ 100 = 3550 ÷ 100 = 35.5. The two methods agree because a weighted mean depends on relative proportions, not on whether the abundance scale totals 4, 100 or another value. For Cl2 molecular ions, the possible mass combinations are 35 + 35 = 70, 35 + 37 = 72 and 37 + 37 = 74. The existence of the mass-72 peak does not identify a third isotope of mass 36; it is the mixed-isotope molecule. Identify the species represented before interpreting the number of peaks.\n\nA percentage-by-mass calculation uses the complete formula. For hydrated or bracketed formulae, expand every multiplier before adding contributions. In Al2(SO4)3, aluminium contributes 2 × 27.0 = 54.0, sulfur contributes 3 × 32.1 = 96.3, and oxygen contributes 12 × 16.0 = 192.0. The formula mass is 342.3. Aluminium therefore contributes 54.0 ÷ 342.3 × 100% = 15.776...%, or 15.8% to three significant figures. A learner who counts four oxygen atoms has ignored the multiplier outside the brackets. As a final check, the separate element percentages for a pure compound should total about 100%, allowing for rounding.\n\nInterpretation questions may give a graph, a peak table or a list of intensities. Translate each representation into the same two ideas: mass and relative abundance. A taller peak means a larger proportion, not a heavier isotope. A peak farther to the right has greater mass, not necessarily greater abundance. Relative atomic mass combines both axes through the weighted-mean calculation. It is not normally a whole number because naturally occurring samples contain isotopes in proportions. If a calculated value lies outside the mass range, revisit the denominator and the multiplication before rounding. Recalculate from the original heights rather than from rounded intermediate percentages, because early rounding can move the final weighted mean. Keep at least one extra digit during working and round after the weighted sum has been divided by the abundance total.",
    "1.1.4": "Ratios close to simple fractions need careful scaling. If division by the smallest amount gives 1.00:1.50, multiply both values by 2 to obtain 2:3. For 1.00:1.33, multiply all values by 3 to obtain about 3:4. Do not round 1.50 to 2, because that changes the composition. The precision of the measured composition decides how close a ratio must be before it is recognised as a simple fraction.\n\nWhen the compound contains oxygen, its mass may be measured directly or obtained by difference. Suppose a 1.50 g sample contains 0.600 g carbon and 0.100 g hydrogen. The oxygen mass is 1.50 − 0.600 − 0.100 = 0.800 g. The amounts are C: 0.600 ÷ 12.0 = 0.0500 mol; H: 0.100 ÷ 1.00 = 0.100 mol; O: 0.800 ÷ 16.0 = 0.0500 mol. Dividing by 0.0500 gives 1:2:1 and empirical formula CH2O. This subtraction is valid only when the sample is stated to contain those three elements.\n\nThe empirical formula cannot by itself distinguish compounds that share the same simplest ratio. CH2O could correspond to CH2O, C2H4O2 or C6H12O6. Mr supplies the multiplier. Conversely, if the calculated multiplier is 2.98, experimental rounding may justify 3; a value such as 2.4 does not. Check the original mole ratios and data rather than forcing a molecular formula.",
    "1.1.5": "Take a mole ratio from a balanced equation. For N2(g) + 3H2(g) → 2NH3(g), one mole of nitrogen reacts with three moles of hydrogen and forms two moles of ammonia. If 0.400 mol N2 and 0.900 mol H2 are mixed, compare 0.400 ÷ 1 with 0.900 ÷ 3. The smaller value is 0.300 for hydrogen, so hydrogen limits the reaction and produces 2 × 0.300 = 0.600 mol NH3. Nitrogen is in excess.\n\nDirect gas-volume ratios are valid when the gaseous quantities are compared at the same temperature and pressure. Otherwise convert each volume to moles using the temperature and pressure supplied. In solution work, distinguish concentration from amount: concentration describes moles per dm³, while amount is the actual number of moles in the chosen volume. Reporting c = 0.150 mol without dm⁻³ confuses the two quantities. At the end, read the question again: the requested substance, temperature and pressure, unit and significant figures belong to the answer.",
}
for subtopic, text in supplements.items():
    unit_blocks[subtopic].append(("consolidation", "Consolidation and checks", text))

unit_by_sub = {u["sub_topic"]: u for u in work_order["content_units"]}
for subtopic, rows in unit_blocks.items():
    plan = unit_by_sub[subtopic]
    claim_ids = [cid for oid in plan["objective_ids"] for cid in claim_ids_by_objective[oid]]
    blocks = []
    for index, (kind, heading, text) in enumerate(rows, 1):
        valid_block_type = {"worked_example": "example", "explanation": "plain_explanation",
                            "procedure": "process", "consolidation": "summary"}.get(kind, kind)
        block = {
            "block_id": f"{subtopic}-b{index}", "block_type": valid_block_type, "heading": heading,
            "text": text, "claim_ids": claim_ids, "context_tags": [],
            "assessment_objectives": ["A", "B"],
            "claims_seen": {cid: 1 for cid in claim_ids},
        }
        if subtopic == "1.1.4" and index == 1:
            block["generalisation_scope"] = plan["objective_ids"]
        stamp(block)
        blocks.append(block)
    count = sum(words(block["text"]) for block in blocks)
    unit = {
        "unit_id": plan["unit_id"], "title": rows[0][1], "objective_ids": plan["objective_ids"],
        "level": "NSSCAS", "core_status": "core", "objective_type": "chemistry",
        "depth_tier": max(o["depth_tier"] for o in plan["objectives"]),
        "word_budget": {"min": plan["word_budget"][0], "target": round(sum(plan["word_budget"]) / 2), "max": plan["word_budget"][1]},
        "blocks": blocks, "word_count": count, "qa_status": "review_required", "notes": ["Topic 1.1 structural exemplar."],
    }
    write(os.path.join(topic_dir, plan["file"]), unit)

card_content = {
    "001": ("Define relative atomic mass.", "The weighted mean mass of an atom of an element relative to one twelfth of the mass of one carbon-12 atom."),
    "002": ("A learner calls the value calculated for MgO its relative molecular mass. Suggest the correct term and apply it to MgO.", "Given situation: MgO is represented by formula units, not separate molecules. Principle: add Ar values for its formula. Application: call 24.3 + 16.0 = 40.3 its relative formula mass."),
    "003": ("Define the mole.", "A mole is the amount of substance containing the Avogadro constant number of specified particles."),
    "004": ("Suggest how many chloride ions are present in 0.200 mol of chloride ions. Use NA = 6.02 × 10²³ mol⁻¹.", "Given situation: n = 0.200 mol. Principle: N = nNA. Application: 0.200 × 6.02 × 10²³ = 1.204 × 10²³ chloride ions."),
    "005": ("State what the position and relative intensity of a peak represent in an atomic mass spectrum.", "Feature: peak position represents isotopic mass. Property: relative intensity represents relative abundance. Point: interpret the species named by the question."),
    "006": ("An atomic spectrum has peaks at 20 and 22 with relative intensities 9 and 1. Determine which isotope is more abundant.", "Data: intensities are 9 and 1. Feature: the peak at 20 is nine times higher. Inference: the mass-20 isotope is more abundant."),
    "026": ("A molecular-ion spectrum of Cl2 has three main peaks. A learner concludes that chlorine has three isotopes. Explain the error.", "Error: the learner equates molecular peaks with isotope count. Correct idea: two chlorine isotopes can pair as light-light, light-heavy and heavy-heavy, giving three Cl2 molecular masses. Discriminating test: ask whether each peak represents one atom's ion or a molecule made from two atoms."),
    "007": ("State the relationship used to calculate relative atomic mass from isotopic masses and abundances.", "Feature: multiply each isotopic mass by its abundance. Property: add the products. Point: divide by the sum of the abundances, which is 100 only for percentage abundances."),
    "008": ("Copper has isotopes of mass 63 and 65 with relative abundances 69.2% and 30.8%. Calculate Ar(Cu).", "Relationship: Ar = Σ(mass × abundance)/Σabundance. Conversion: percentages total 100. Substitution: [(63 × 69.2) + (65 × 30.8)] ÷ 100 = (4359.6 + 2002.0) ÷ 100. Answer: 63.616, so 63.6 to three significant figures; relative atomic mass has no unit."),
    "009": ("A two-isotope element has Ar = 79.9 and isotope masses 79 and 81. Determine which isotope is more abundant.", "Data: Ar is 79.9. Feature: 79.9 is closer to 79 than to 81. Inference: the mass-79 isotope is more abundant."),
    "027": ("Peak heights 12 and 8 occur at masses 10 and 11. A learner divides the weighted sum by 100. Explain the error.", "Error: the peak heights are treated as percentages although they total 20. Correct idea: divide (10 × 12) + (11 × 8) by 12 + 8. Discriminating test: check whether the listed heights add to 100."),
    "010": ("State the relationship for calculating the percentage by mass of an element in a compound.", "Feature: find the element's total relative-mass contribution. Property: divide by the compound's Mr or relative formula mass. Point: multiply the ratio by 100%."),
    "011": ("Calculate the percentage by mass of oxygen in CaCO3. Use Ar: Ca = 40.1, C = 12.0, O = 16.0.", "Relationship: percentage O = oxygen contribution/formula mass × 100%. Conversion: three O atoms contribute 48.0. Substitution: 48.0 ÷ (40.1 + 12.0 + 48.0) × 100 = 47.952.... Answer: 48.0% to three significant figures; percentage has unit %."),
    "012": ("Determine which has the greater percentage by mass of nitrogen: NH3 or NH4NO3.", "Data: NH3 has Mr 17.0 and nitrogen contribution 14.0, giving 82.4%. NH4NO3 has formula mass 80.0 and nitrogen contribution 28.0, giving 35.0%. Feature: compare the calculated percentages. Inference: NH3 has the greater nitrogen percentage."),
    "013": ("Define empirical formula.", "The simplest whole-number ratio of atoms of each element in a compound."),
    "014": ("A compound has empirical formula CH2 and Mr = 56. Suggest its molecular formula.", "Given situation: empirical-formula mass = 14. Principle: multiplier = Mr/empirical-formula mass. Application: 56 ÷ 14 = 4, so the molecular formula is C4H8."),
    "015": ("State the main steps for obtaining an empirical formula from percentage composition.", "Feature: treat percentages as masses in 100 g. Property: convert each mass to moles and divide by the smallest. Point: scale all ratios together to the smallest whole numbers."),
    "016": ("A compound contains 40.0% C, 6.7% H and 53.3% O. Calculate its empirical formula. Use Ar: C = 12.0, H = 1.0, O = 16.0.", "Relationship: mole ratio = mass percentage/Ar. Conversion: C 40.0 ÷ 12.0 = 3.333; H 6.7 ÷ 1.0 = 6.700; O 53.3 ÷ 16.0 = 3.331. Substitution: divide by 3.331 to give 1.00:2.01:1.00. Answer: CH2O; formulae have no unit, and the ratios justify whole-number subscripts."),
    "017": ("A compound has empirical formula CH2O and Mr = 180. Determine its molecular formula.", "Data: empirical-formula mass = 30.0. Feature: 180 ÷ 30.0 = 6. Inference: multiply every empirical subscript by 6, giving C6H12O6."),
    "018": ("State what may be changed when balancing an equation and what state symbols show.", "Feature: change coefficients, not formula subscripts. Property: coefficients conserve each type of atom. Point: (s), (l), (g) and (aq) show solid, liquid, gas and dissolved-in-water states."),
    "019": ("Write the balanced equation, including state symbols, for magnesium solid burning in oxygen gas to form solid magnesium oxide.", "Reactants and products: Mg(s), O2(g), MgO(s). Balance: 2Mg(s) + O2(g) → 2MgO(s). State symbols are included as required."),
    "020": ("State the sequence used in a stoichiometric calculation.", "Feature: convert the given quantity to moles. Property: apply the balanced-equation mole ratio. Point: convert the resulting amount to the requested mass, gas volume or solution quantity."),
    "021": ("CaCO3(s) → CaO(s) + CO2(g). Calculate the mass of CaO formed from 10.0 g CaCO3. Use M(CaCO3) = 100.1 g mol⁻¹ and M(CaO) = 56.1 g mol⁻¹.", "Relationship: 1 mol CaCO3 gives 1 mol CaO. Conversion: n(CaCO3) = 10.0 ÷ 100.1 = 0.0999001 mol. Substitution: mass CaO = 0.0999001 × 56.1 = 5.6044 g. Answer: 5.60 g to three significant figures, with unit g."),
    "022": ("CH4(g) + 2O2(g) → CO2(g) + 2H2O(l). Calculate the volume of oxygen needed for 0.250 mol methane at r.t.p.", "Relationship: CH4:O2 = 1:2. Conversion: n(O2) = 2 × 0.250 = 0.500 mol. Substitution: V = nVm = 0.500 × 24.0 = 12.0 dm³. Answer: 12.0 dm³ at r.t.p., to three significant figures."),
    "023": ("Calculate the amount of NaOH in 35.0 cm³ of 0.120 mol dm⁻³ solution.", "Relationship: n = cV. Conversion: 35.0 cm³ ÷ 1000 = 0.0350 dm³. Substitution: n = 0.120 × 0.0350 = 0.00420 mol. Answer: 4.20 × 10⁻³ mol to three significant figures; unit mol."),
    "024": ("For 2A + B → product, a mixture contains 0.60 mol A and 0.40 mol B. Determine the limiting reactant.", "Data: amounts are 0.60 mol A and 0.40 mol B. Feature: divide by coefficients: A gives 0.60 ÷ 2 = 0.30; B gives 0.40 ÷ 1 = 0.40. Inference: A is limiting because its quotient is smaller."),
    "025": ("A learner uses 24.0 dm³ mol⁻¹ for a gas calculation stated at s.t.p. Explain the error.", "Error: the r.t.p. molar volume was used. Correct idea: use 22.4 dm³ mol⁻¹ at s.t.p. and 24.0 dm³ mol⁻¹ at r.t.p. Discriminating test: read whether the question specifies s.t.p. or r.t.p. before selecting Vm."),
}

def make_item(slot, prompt, answer, claim_ids):
    required = ", ".join(slot.get("marking_guidance_must_name") or [])
    item = {
        "item_id": slot["slot"], "objective_ids": [slot["objective_id"]], "claim_ids": claim_ids,
        "item_type": "flashcard", "subtype": slot["subtype"],
        "assessment_objectives": slot["assessment_objectives"], "blooms_level": slot["blooms_level"],
        "command_word": slot["command_word"], "mark_tariff": slot["mark_tariff"],
        "difficulty": slot["difficulty"], "prompt": prompt, "canonical_answer": answer,
        "marking_guidance": [f"Required answer parts: {required}. Award the stated tariff only when the response supplies these parts with chemically correct working or wording."],
        "context": {"sector": None, "business_size": None, "ownership": None, "situation": None, "facts": []},
        "prerequisite_item_ids": [], "core_status": "core", "intentional_duplicate_group": None,
        "provenance": "Authored for the 8224 Topic 1.1 structural exemplar from the verified syllabus objectives and local assessment patterns.",
        "qa_status": "review_required", "claims_seen": {cid: 1 for cid in claim_ids},
    }
    if slot.get("misconception_entry"):
        item["misconception_entry"] = slot["misconception_entry"]
    stamp(item)
    return item

items = []
for slot in work_order["item_slots"]:
    key = slot["slot"].split("-")[-2]
    prompt, answer = card_content[key]
    items.append(make_item(slot, prompt, answer, claim_ids_by_objective[slot["objective_id"]]))

all_claim_ids = [c["claim_id"] for c in claims]
performance_content = {
    "ITEM-8224-1.1-P01": (
        "Six questions. Choose one option for each.\n\n1. Which term is correct for MgO?\nA relative isotopic mass\nB relative atomic mass\nC relative molecular mass\nD relative formula mass\n\n2. One mole contains:\nA 6.02 × 10²³ g\nB 6.02 × 10²³ specified particles\nC one particle\nD Mr particles\n\n3. Peaks at mass 35 and 37 have intensities 3:1. Which isotope is more abundant?\nA mass 35\nB mass 37\nC equal abundance\nD cannot be determined\n\n4. What is the empirical formula of C2H6?\nA CH3\nB C2H6\nC CH2\nD C3H\n\n5. Which change balances H2 + O2 → H2O?\nA change H2O to H2O2\nB 2H2 + O2 → 2H2O\nC H2 + O → H2O\nD H2 + 2O2 → H2O\n\n6. What volume does 0.50 mol gas occupy at r.t.p.?\nA 11.2 dm³\nB 12.0 dm³\nC 22.4 dm³\nD 24.0 dm³",
        "Key: 1 D, 2 B, 3 A, 4 A, 5 B, 6 B.\n1 D is correct because MgO is a formula unit; C wrongly treats it as a molecule, B concerns one element, and A one isotope.\n2 B is the definition; A attaches a mass unit to a count, C ignores the Avogadro constant, and D confuses relative mass with particle number.\n3 A follows the 3:1 intensity; B reverses it, C ignores the different heights, and D overlooks the supplied data.\n4 A simplifies 2:6 to 1:3; B is molecular rather than empirical, and C and D use wrong ratios.\n5 B conserves H and O using coefficients; A changes a formula, C changes elemental oxygen, and D is unbalanced.\n6 B uses 0.50 × 24.0; A uses the s.t.p. value, while C and D are one-mole volumes.",
    ),
    "ITEM-8224-1.1-P02": (
        "A compound contains 24.0 g carbon and 4.00 g hydrogen and has Mr = 56.\n(a) Define empirical formula. [1]\n(b) Calculate the amount of carbon and hydrogen atoms represented by these masses. Use Ar(C) = 12.0 and Ar(H) = 1.00. [2]\n(c) Determine the empirical formula. [2]\n(d) Determine the molecular formula. [2]\n(e) State the distinction between relative molecular mass and relative formula mass. [1]",
        "(a) The simplest whole-number ratio of atoms of each element in a compound.\n(b) n(C) = 24.0 ÷ 12.0 = 2.00 mol; n(H) = 4.00 ÷ 1.00 = 4.00 mol.\n(c) Divide by 2.00 to give C:H = 1:2, so CH2.\n(d) Empirical-formula mass = 14; 56 ÷ 14 = 4, so C4H8.\n(e) Relative molecular mass sums Ar values in a molecule; relative formula mass makes the corresponding sum for a formula unit.",
    ),
    "ITEM-8224-1.1-P03": (
        "Hydrogen reacts with oxygen: 2H2(g) + O2(g) → 2H2O(l). A mixture contains 3.00 dm³ H2 and 2.00 dm³ O2 at r.t.p. Calculate the mass of water formed. Use Vm = 24.0 dm³ mol⁻¹ and M(H2O) = 18.0 g mol⁻¹.",
        "Equation: 2H2 + O2 → 2H2O. Working: n(H2) = 3.00 ÷ 24.0 = 0.125 mol; n(O2) = 2.00 ÷ 24.0 = 0.083333 mol. The equation needs 0.0625 mol O2 for 0.125 mol H2, so H2 is limiting. Therefore n(H2O) = 0.125 mol. Answer: mass = 0.125 × 18.0 = 2.25 g, with unit g and three significant figures.",
    ),
}
for task in work_order["performance_tasks"]:
    prompt, answer = performance_content[task["slot"]]
    guidance = ", ".join(task["marking_guidance_must_name"])
    item = {
        "item_id": task["slot"], "objective_ids": task["objective_ids"], "claim_ids": all_claim_ids,
        "item_type": task["item_type"], "subtype": None,
        "assessment_objectives": task["assessment_objectives"], "blooms_level": task["blooms_level"],
        "command_word": task["command_word"], "mark_tariff": task["mark_tariff"], "difficulty": 3,
        "prompt": prompt, "canonical_answer": answer,
        "marking_guidance": [f"Required task parts: {guidance}. Award marks part by part for chemically correct, creditworthy work; the total is {task['mark_tariff']}."],
        "context": {"sector": None, "business_size": None, "ownership": None, "situation": None, "facts": []},
        "prerequisite_item_ids": [], "core_status": "core", "intentional_duplicate_group": None,
        "provenance": "Authored for the 8224 Topic 1.1 structural exemplar from the verified syllabus objectives and local assessment patterns.",
        "qa_status": "review_required", "claims_seen": {cid: 1 for cid in all_claim_ids},
    }
    stamp(item)
    items.append(item)

write(os.path.join(topic_dir, "learning-items", "topic_1.1_items.json"), {
    "dataset_id": "ITEMS-8224-1.1", "topic_id": "1.1", "items": items,
})
write(os.path.join(topic_dir, "authoring_notes.json"), {
    "topic_id": "1.1",
    "deviations": [],
    "resolved_deviations": [{
        "item_id": "ITEM-8224-1.1-019-EQUATION",
        "previous": "Temporary PROC subtype while EQUATION was unsupported.",
        "resolution": "Restored planned EQUATION after Jeremy explicitly approved extending the shared schema on 2026-10-22.",
    }],
})

# A deliberately thin practical exemplar: one titration slice, kept outside the
# authored 5.1 topic so it demonstrates shape without pretending all 84 slots exist.
ex_dir = os.path.join(WS, "exemplar", "5.1")
prac_claims = [
    ("CLM-8224-5.1-EX-001", ["OBJ-8224-5.1.2-01"], "A burette reading is recorded to the nearest 0.05 cm³, with both initial and final readings shown to the same number of decimal places."),
    ("CLM-8224-5.1-EX-002", ["OBJ-8224-5.1.2-06"], "A titre is final burette reading minus initial burette reading, and concordant titres agree within 0.10 cm³ for this syllabus."),
    ("CLM-8224-5.1-EX-003", ["OBJ-8224-5.1.2-06"], "The mean titre uses concordant accurate titres and excludes the rough result."),
    ("CLM-8224-5.1-EX-004", ["OBJ-8224-5.1.2-06"], "A titration calculation converts the mean titre to dm³, finds moles from cV, applies the equation ratio and then determines the requested concentration."),
    ("CLM-8224-5.1-EX-005", ["OBJ-8224-5.1.4-07", "OBJ-8224-5.1.4-13"], "A specific improvement identifies the affected measurement and explains how the change reduces its uncertainty or bias."),
    ("CLM-8224-5.1-EX-006", ["OBJ-8224-5.1.1-04"], "The pipette is rinsed with the solution it will deliver and the burette with the solution it will contain so residual water does not dilute measured solutions."),
]
practical_ledger = {"ledger_id": "CLM-LEDGER-8224-5.1-EX", "claims": []}
for cid, objective_ids, text in prac_claims:
    practical_ledger["claims"].append({
        "claim_id": cid, "objective_ids": objective_ids,
        "text": text, "claim_type": "procedural", "provenance": "generated_gap",
        "evidence": [{"source_id": "NSSCAS-8224-SYLLABUS", "locator": "Annexe A",
                      "support_type": "paraphrase"}], "derived_from_claim_ids": [], "revision": 1,
        "verification": {"status": "unverified", "method": "Derived from verified Annexe A practical criteria; requires independent semantic review.", "reviewer_id": None, "reviewed_at": None, "confidence": 0.9},
        "publishable": False, "notes": [],
    })
write(os.path.join(ex_dir, "claims", "canonical_claim_ledger.json"), practical_ledger)
prac_ids = [cid for cid, _, _ in prac_claims]
practical_objectives = ["OBJ-8224-5.1.1-04", "OBJ-8224-5.1.2-01", "OBJ-8224-5.1.2-06",
                        "OBJ-8224-5.1.4-07", "OBJ-8224-5.1.4-13"]
prac_texts = [
    ("learner_objective", "A complete titration record", "A titration record must preserve the measurements from which the result is calculated. Record initial and final burette readings, then calculate the titre by subtraction. Use a single table with quantity-and-unit headings. Burette readings are written consistently to two decimal places because the scale is read to the nearest 0.05 cm³. A rough titre helps locate the endpoint but is not used in the mean."),
    ("procedure", "Preparing the apparatus", "Rinse the pipette with the solution it will deliver and the burette with the solution it will contain. Residual water would otherwise dilute a measured solution. Fill the burette, remove any air bubble from the jet and read the meniscus at eye level. Transfer the pipetted aliquot to a conical flask, add only a few drops of a suitable indicator, then add titrant while swirling. Near the endpoint, add titrant dropwise."),
    ("worked_calculation", "Concordance and the mean", "Suppose accurate titres are 24.35 cm³, 24.40 cm³ and 24.70 cm³. The first two differ by 0.05 cm³ and are concordant; the third is not. Mean titre = (24.35 + 24.40) ÷ 2 = 24.375 cm³, reported as 24.38 cm³ to match burette precision. The rough titre, if present, is excluded even when it lies close to the accurate values."),
    ("worked_calculation", "From titre to concentration", "For a 1:1 reaction, 25.00 cm³ of solution X reacts with an unrounded mean titre of 24.375 cm³ of 0.1000 mol dm⁻³ solution Y. Carry the unrounded mean through the calculation. Convert the titre: 24.375 cm³ = 0.024375 dm³. Moles Y = cV = 0.1000 × 0.024375 = 0.0024375 mol. The 1:1 ratio gives 0.0024375 mol X in 0.02500 dm³. Concentration X = 0.0024375 ÷ 0.02500 = 0.09750 mol dm⁻³ (four significant figures, matching the supplied concentration and pipetted volume)."),
    ("evaluation", "Specific evaluation", "An improvement must connect cause and effect. Repeating until concordant titres are obtained reduces the influence of random endpoint variation on the mean. Reading the meniscus at eye level reduces parallax in both burette readings. Replacing a measuring cylinder with a volumetric pipette improves the delivered aliquot because the pipette has a smaller uncertainty for that fixed volume. Saying only 'be more careful' does not identify a measurement or a corrective action."),
    ("consolidation", "Quality check before calculation", "Before using the mean, inspect the raw table. Confirm that final readings exceed initial readings, titres are calculated by subtraction, all readings use consistent decimal places and the selected accurate titres satisfy the concordance rule. Then carry the unrounded mean into the stoichiometric calculation. This separates recording errors from chemical reasoning and makes an anomalous run visible rather than hiding it inside an average."),
]
blocks = []
for i, (kind, heading, text) in enumerate(prac_texts, 1):
    valid_block_type = {"procedure": "process", "consolidation": "summary"}.get(kind, kind)
    block = {"block_id": f"5.1-ex-b{i}", "block_type": valid_block_type, "heading": heading, "text": text,
             "claim_ids": prac_ids, "context_tags": [], "assessment_objectives": ["C"],
             "claims_seen": {cid: 1 for cid in prac_ids}}
    stamp(block)
    blocks.append(block)
practical_unit = {"unit_id": "CU-8224-5.1-EX-TITRATION", "title": "Titration recording and calculation",
                  "objective_ids": practical_objectives,
                  "level": "NSSCAS", "core_status": "core", "objective_type": "practical",
                  "depth_tier": 2, "word_budget": {"min": 400, "target": 500, "max": 700},
                  "blocks": blocks, "word_count": sum(words(x["text"]) for x in blocks),
                  "qa_status": "review_required", "notes": ["Thin Paper 3 structural exemplar; not the complete 5.1 topic."]}
write(os.path.join(ex_dir, "content-units", "CU-8224-5.1-EX-TITRATION.json"), practical_unit)

practical_items = []
def add_practical(item_id, item_type, subtype, objective_ids, bloom, command, tariff, prompt, answer, guidance):
    item = {"item_id": item_id, "objective_ids": objective_ids, "claim_ids": prac_ids,
            "item_type": item_type, "subtype": subtype, "assessment_objectives": ["C"],
            "blooms_level": bloom, "command_word": command, "mark_tariff": tariff, "difficulty": 3,
            "prompt": prompt, "canonical_answer": answer, "marking_guidance": guidance,
            "context": {"sector": None, "business_size": None, "ownership": None, "situation": None, "facts": []},
            "prerequisite_item_ids": [], "core_status": "core", "intentional_duplicate_group": None,
            "provenance": "Authored for the 8224 thin Paper 3 structural exemplar from Annexe A.",
            "qa_status": "review_required", "claims_seen": {cid: 1 for cid in prac_ids}}
    stamp(item)
    practical_items.append(item)

add_practical("ITEM-8224-5.1-EX-01-PROC", "flashcard", "PROC", ["OBJ-8224-5.1.1-04"], "Apply", "Describe", 3,
              "Describe how to prepare a burette and pipette before a titration.",
              "Rinse the pipette with the solution it will deliver and the burette with the solution it will contain. Fill the burette, remove the air bubble from its jet and read the meniscus at eye level.",
              ["Sequence: rinse, fill and remove the jet bubble. Reagent or apparatus: name the pipette and burette solutions. Condition: read at eye level. Observation or result: no air remains in the jet."])
add_practical("ITEM-8224-5.1-EX-02-CALC", "flashcard", "CALC", ["OBJ-8224-5.1.2-06"], "Apply", "Calculate", 2,
              "Accurate titres are 24.35 cm³, 24.40 cm³ and 24.70 cm³. Calculate the mean concordant titre.",
              "The concordant pair is 24.35 and 24.40 cm³ because they differ by 0.05 cm³. Mean = (24.35 + 24.40) ÷ 2 = 24.375 cm³, so 24.38 cm³.",
              ["Relationship or equation: mean of concordant values. Conversion and substitution: use 24.35 and 24.40 only. Answer, unit and significant figures: 24.38 cm³."])
add_practical("ITEM-8224-5.1-EX-03-EVAL", "flashcard", "EVAL", ["OBJ-8224-5.1.4-07", "OBJ-8224-5.1.4-13"], "Evaluate", "Suggest", 2,
              "A learner measures the 25.0 cm³ aliquot with a measuring cylinder. Suggest one realistic improvement and explain it.",
              "Use a 25.0 cm³ volumetric pipette. Criterion: volume uncertainty. Evidence: a pipette is calibrated to deliver the fixed aliquot more precisely than a measuring cylinder. Limitation addressed: uncertainty in the aliquot. Judgement: the concentration calculated from it is more reliable.",
              ["Criterion: volume uncertainty. Evidence: pipette calibration. Limitation: measuring-cylinder precision. Judgement: improved reliability."])
add_practical("ITEM-8224-5.1-EX-P01", "practical_task", None,
              practical_objectives, "Analyse", "Determine", 20,
              "A learner pipettes 25.00 cm³ of solution X into a flask and titrates it with 0.1000 mol dm⁻³ solution Y. X and Y react in a 1:1 mole ratio.\n\n| run | initial burette reading / cm³ | final burette reading / cm³ |\n|---|---:|---:|\n| rough | 0.10 | 24.80 |\n| 1 | 1.20 | 25.55 |\n| 2 | 0.35 | 24.75 |\n| 3 | 2.10 | 26.80 |\n\n(a) Record the titre for each run in a new results column. [3]\n(b) Identify the concordant titres and calculate their mean. [3]\n(c) Calculate the concentration of X. [6]\n(d) Explain why the rough titre is not included in the mean. [2]\n(e) Identify one significant source of uncertainty in judging the endpoint and suggest a realistic improvement. [4]\n(f) State two features of a correctly formatted titration table. [2]",
              "(a) Rough 24.70 cm³; run 1 24.35 cm³; run 2 24.40 cm³; run 3 24.70 cm³.\n(b) Runs 1 and 2 are concordant; mean = (24.35 + 24.40) ÷ 2 = 24.38 cm³.\n(c) 24.375 cm³ = 0.024375 dm³. n(Y) = 0.1000 × 0.024375 = 0.0024375 mol. The ratio is 1:1, so n(X) = 0.0024375 mol. 25.00 cm³ = 0.02500 dm³. c(X) = 0.0024375 ÷ 0.02500 = 0.09750 mol dm⁻³.\n(d) The rough run locates the endpoint and is not an accurate repeat.\n(e) The colour change is judged by eye and may be overshot. Add titrant dropwise near the endpoint over a white tile while swirling, so the first permanent colour change is detected with less excess titrant.\n(f) Headings give quantity and unit, and all burette readings use consistent decimal places.",
              ["Apparatus and method: pipette, burette and endpoint procedure. Observations or data table: titres with quantity/unit headings. Working: conversion, cV and 1:1 ratio. Conclusion: 0.09750 mol dm⁻³. Error: subjective endpoint. Improvement: dropwise addition over a white tile."])
write(os.path.join(ex_dir, "learning-items", "topic_5.1_exemplar_items.json"),
      {"dataset_id": "ITEMS-8224-5.1-EX", "topic_id": "5.1", "items": practical_items})

readme = """# 8224 structural exemplar

Two slices define the authoring shape for Chemistry 8224:

- `topics/1.1/` is the complete content exemplar. It follows all 30 work-order slots and passes the topic checks.
- `exemplar/5.1/` is a deliberately thin Paper 3 titration slice: one content unit, three supporting cards and one integrated practical task. It demonstrates table, calculation and evaluation structure; it is not a substitute for the full 84-item Topic 5.1 work order.

Copy the field structure, claim stamping, calculation working, practical table conventions and marking-guidance vocabulary. Do not reuse its prompts or data in later resources.
"""
os.makedirs(os.path.join(WS, "exemplar"), exist_ok=True)
with open(os.path.join(WS, "exemplar", "README.md"), "w", encoding="utf-8") as fh:
    fh.write(readme)

print(f"Topic 1.1: {len(claims)} claims, {len(unit_blocks)} units, {len(items)} items")
print(f"Practical slice: {len(prac_claims)} claims, 1 unit, {len(practical_items)} items")
