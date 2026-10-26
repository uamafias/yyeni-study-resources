"""Paraphrased credit guidance from the 2020 report's scanned answer tables."""

import json
from pathlib import Path

WORK = Path(__file__).resolve().parents[1]

# Each entry corresponds to one printed marked part, in question order. The
# source pages are PDF viewer pages; OCR was checked against the page image.
POINTS = {
  (2, 1, 86): [
    "Select the element structure; the table accepts either of the two equivalent letter choices.",
    "Select the V-shaped molecule structure.",
    "Select the ammonia structure, identified by its effect on damp red litmus.",
    "Show three shared N–H electron pairs and the nitrogen lone pair in the ammonia diagram; each feature has separate credit.",
    "Name the C60 carbon structure as buckminsterfullerene; the generic fullerene name alone is insufficient.",
    "Define a nanomaterial by a particle dimension of approximately 1–100 nm in at least one dimension.",
    "Describe diamond as a giant covalent lattice and each carbon bonded to four others; two distinct points.",
    "Explain the hydrophilic ionic head and hydrophobic hydrocarbon tail, then connect head to water and tail to grease; two marks.",
    "State that soap forms scum or lathers poorly in hard water.",
    "Explain biodegradability through breakdown by bacteria or other microorganisms.",
  ],
  (2, 2, 87): [
    "Name two transition elements shown; iron, copper and vanadium are accepted choices.",
    "Name any displayed Period 3 element, using its correct name or symbol.",
    "Describe the increase in outer-shell electron count across Period 3.",
    "State that Group 0 atoms have a full outer electron shell.",
    "Name Group 0 as the noble or inert gases.",
  ],
  (2, 3, 88): [
    "Match the four supplied stoichiometric terms to their definitions; the report awards two marks for three correct links and one for one or two.",
    "Use the molar gas volume at room temperature and pressure to obtain 0.5 mol carbon dioxide.",
    "Use the one-to-one equation ratio to obtain 0.5 mol carbonate; follow-through is allowed.",
    "Divide the supplied mass by carbonate amount to obtain relative formula mass 84; follow-through is allowed.",
    "Subtract the carbonate group's relative mass from 84 to obtain relative atomic mass 24.",
    "Identify magnesium from the relative atomic mass; a chemically sensible follow-through answer is allowed.",
  ],
  (2, 4, 89): [
    "Distinguish fixed ions in solid lead bromide from mobile ions in the melt; moving electrons are not the reason.",
    "Complete four table entries: copper metal, copper ions, hydrogen and chlorine, with one mark for each correct entry.",
    "Explain that hydrogen fuel-cell operation forms water without pollutant products.",
    "Count bonds broken and formed, then subtract: 1369 minus 1856 gives −487 kJ/mol; show energy steps and unit for the three marks.",
    "Draw an exothermic energy profile with reactants above products, downward enthalpy change and activation energy to the peak; three distinct marks.",
  ],
  (2, 5, 91): [
    "Define an acid as a proton donor.",
    "Identify pure water as neutral in the supplied pH diagram.",
    "Choose a pH below 10 but above 7 when the alkaline solution is diluted.",
    "Explain that aluminium hydroxide is a base and reacts with gastric acid; two connected points.",
    "Write correct aluminium chloride and water products and balance the neutralisation equation; two marks.",
    "Calculate percentage purity as 14.2 ÷ 15.0 × 100 = 94.7%; the report explicitly rejects rounding to 95%, while allowing credit for working.",
    "Bubble gas through limewater and state that it turns milky/cloudy; the observation mark depends on the correct test.",
  ],
  (2, 6, 92): [
    "Compare aluminium with carbon in the reactivity series to explain the need for electrolysis.",
    "Explain that molten cryolite lowers the operating melting temperature or energy requirement.",
    "Give both balanced electrode half-equations for aluminium extraction, with anode oxygen formation and cathode aluminium formation.",
    "Give two advantages of aluminium alloys for aircraft, such as low density with greater strength or corrosion resistance.",
    "Give a valid use of pure aluminium, such as food containers or electrical cables.",
    "Name carbon dioxide from anode consumption and provide its balanced formation equation; two marks.",
  ],
  (2, 7, 93): [
    "Name the illustrated hydrocarbon as propene.",
    "Identify the hydroxyl group in ethanol; hydroxide is not accepted.",
    "State an alkene test reagent and its colour change; the observation credit depends on an appropriate reagent.",
    "Name substitution as the alkane–chlorine reaction type.",
    "Draw the full chloroethane structure with the carbon single bond and all atoms/bonds correctly shown; two marks.",
    "Identify condensation polymerisation of diamine and dicarboxylic acid.",
    "Name nylon or a polyamide as the polymer family.",
    "Draw the amide linkage in the polymer repeat; full orientation earns both marks, with partial credit for a reversed linkage.",
  ],
  (2, 8, 94): [
    "Name the Contact process.",
    "Identify sulfur and air as the raw materials; oxygen alone is not accepted for air.",
    "Identify sulfur dioxide as the named intermediate.",
    "Identify vanadium(V) oxide, including oxidation state; generic vanadium oxide is insufficient.",
    "Give supported temperature and pressure conditions, around 450 °C and low/atmospheric pressure, with units; two marks.",
    "Write the correct oleum-water equation and balance it to form two sulfuric acid molecules; two marks.",
    "Give a valid sulfuric-acid use such as fertilisers, detergents or battery acid; preservative is rejected.",
  ],
  (3, 1, 95): [
    "Choose the apparatus letters for separating and collecting sand: two distinct selections.",
    "Choose the apparatus letters for recovering the dissolved salt: two distinct selections.",
    "Choose the apparatus sequence for recovering water from the solution: the report awards the two marks across the required selections.",
  ],
  (3, 2, 97): [
    "Read the two thermometers at 21.2 °C and 25.0 °C, each to one decimal place, retaining the trailing zero; one mark per reading.",
    "Plot the nine data points accurately; the report allows one mark for five to eight correct and two for all nine.",
    "Draw a balanced straight best-fit line through the increasing-temperature points.",
    "Draw a balanced straight best-fit line through the decreasing-temperature points.",
    "Extend both lines to their intersection and read the maximum temperature, about 28.5 °C.",
    "Subtract starting temperature from maximum temperature to obtain a 7.3 °C rise.",
    "Read the acid volume at the maximum from the graph, about 26.0 cm³.",
    "Calculate solution mass from the two volumes, then use q = mcΔT to obtain about 1.56 kJ; two marks for method and result.",
    "Suggest a practical heat-loss reduction, such as insulation or a lid.",
    "Read about 12 cm³ from the graph at the specified temperature and show the horizontal/vertical read-off construction.",
  ],
  (3, 3, 98): [
    "Infer water from the combustion test and support it with the white-to-blue copper sulfate observation; two marks.",
    "Explain the funnel's gas-guiding role and the ice water's condensing role; two distinct marks.",
    "Infer from the observation that the liquid does not burn in air.",
    "Complete the pH entry as neutral, pH 7.",
    "Record bubbling or effervescence as the carbonate-test observation, rather than naming the gas.",
    "Classify the liquid as a weak acid from the supplied test.",
    "Name carbon dioxide as the gas produced in the carbonate reaction.",
    "Infer that the liquids are saturated, lacking carbon–carbon double bonds.",
    "Identify ethanol and support it with a valid observation or reaction from the supplied tests; two marks.",
  ],
  (3, 4, 99): [
    "Eight marks are awarded from nine method points: mix the stated reagents in a vessel; fit cotton wool; explain that it limits splashing while letting gas escape; place the vessel on an electronic balance; start timing and take initial mass; measure mass against time; tabulate paired readings; graph time against mass or mass loss; use curve steepness to infer rate. The report rejects volume-of-gas methods for this specified task.",
  ],
}


def main():
    rows = json.loads((WORK / "assessment-evidence/question_parts.json").read_text())["records"]
    out = {}
    for (paper, q, page), points in POINTS.items():
        subset = [r for r in rows if r["year"] == 2020 and r["paper_id"] == str(paper) and r["question_ref"].startswith(f"Q{q},")]
        assert len(points) == len(subset), (paper, q, len(points), len(subset))
        for row, point in zip(subset, points):
            source_page = 90 if row['evidence_id'] == 'QP-6117-2020-2-Q04-P05' else page
            out[row["evidence_id"]] = {"creditworthy_points": [point], "report_pdf_page": source_page,
                                       "method": "Paraphrased after reading the 2020 report page image and OCR; check image for exact alternatives."}
    assert len(out) == 77
    path = WORK / "assessment-evidence/manual-credit-2020.json"
    path.write_text(json.dumps({"status": "curated", "records": out}, indent=2, ensure_ascii=False) + "\n")
    print("Wrote 77 paraphrased 2020 written-part guidance entries")


if __name__ == "__main__":
    main()
