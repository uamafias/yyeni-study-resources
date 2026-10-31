"""Turn explicit Chemistry syllabus limits into reviewable scope rules."""

import json
from pathlib import Path


WORK = Path(__file__).resolve().parents[1]
FACTS = json.loads((WORK / "curriculum/syllabus-facts.json").read_text())
LIMITS = FACTS["stated_limits"]
PATTERNS = [
    r'(?i)\bninhydrin\b|named locating.agent recipes',
    r'(?i)\b[spdf][- ]orbitals?\b|d-block electron configuration|\b[1-7][spdf][1-9]\b|quantum numbers|\b[1-7][spdf]\b[^.\n]{0,50}(?:electron|configuration)|(?:electron|configuration)[^.\n]{0,50}\b[1-7][spdf]\b',
    r'(?i)bond.angle model of ozone|ring geometry of S8',
    r'(?i)PV\s*=\s*nRT|convert a gas volume between temperatures|ideal gas law|Boyle.?s law|Charles.?s law|combined gas law|(?:gas|oxygen|hydrogen|carbon dioxide)[^.\n]{0,100}(?:volume|cm[3³]|dm[3³])[^.\n]{0,100}(?:273(?:\.15)?\s*K|STP|standard temperature)|(?:volume|cm[3³]|dm[3³])[^.\n]{0,100}(?:gas|oxygen|hydrogen)[^.\n]{0,100}273(?:\.15)?\s*K',
    r'(?i)fuel.cell membrane construction|internal fuel.cell operation steps',
    r'(?i)non.aqueous Br[oø]nsted acid',
    r'(?i)tetraamminecopper|complex.ion ligand formula|\[Cu\(NH[3₃]\)[4₄]\]|ligand substitution mechanism',
    r'(?i)radical initiation|propagation termination mechanism|\bS[Nn][12]\b|curly arrows?|curved.arrow mechanism',
    r'(?i)electrophilic addition|arrow.pushing mechanism',
    r'(?i)steam addition arrow.pushing|hydration reaction mechanism',
    r'(?i)ethanol oxidation mechanism|full oxidation equation for ethanoic acid formation',
    r'(?i)draw specific amino acid structures|name (?:each|every|the) amino acids?(?: formed| produced| product)?|(?:draw|display|name|identify)[^.\n]{0,80}(?:glycine|alanine|specific amino acids)|H[2₂]N.?CH[2₂].?COOH',
]

RULES = [
    (0, "Specific chromatography locating agents", ["ninhydrin as a required locating agent", "named locating-agent recipes"], ["Use a locating agent to reveal a colourless spot."]),
    (1, "Orbital distributions beyond electron shells", ["s-orbital electron configuration", "p-orbital filling", "d-block electron configuration", "Write the 1s2 2s2 configuration", "Explain quantum numbers", "Write the 3d electron configuration"], ["Explain outer electrons using shell arrangements."]),
    (2, "Detailed structures of ozone and sulfur-eight", ["bond-angle model of ozone", "ring geometry of S8"], ["Identify O3 and S8 as molecules of one element."]),
    (3, "Gas-law and temperature-pressure volume conversions", ["PV = nRT problem", "convert a gas volume between temperatures", "Calculate the volume of oxygen gas at 273 K.", "Use the combined gas law to find the new volume."], ["Use 24 dm3 per mole at room temperature and pressure.", "Convert a thermometer reading of 0 °C to 273 K.", "Measure gas volume every ten seconds in a rate experiment."]),
    (4, "Fuel-cell construction detail", ["fuel-cell membrane construction", "internal fuel-cell operation steps"], ["Describe hydrogen reacting with oxygen to produce electrical energy."]),
    (5, "Acid-base proton-transfer definitions outside aqueous solution", ["non-aqueous Brønsted acid example"], ["Define acid and base by proton transfer in aqueous solution."]),
    (7, "Complex-ion formulae", ["tetraamminecopper(II) formula", "complex-ion ligand formula", "Write [Cu(NH3)4]2+", "Explain the ligand substitution mechanism"], ["Identify ions from precipitate observations with aqueous ammonia or sodium hydroxide."]),
    (8, "Alkane substitution mechanisms", ["radical initiation propagation termination mechanism", "Explain an SN1 mechanism with curly arrows", "Show an SN2 mechanism"], ["Describe substitution of an alkane with chlorine."]),
    (9, "Alkene addition mechanisms", ["electrophilic addition arrow-pushing mechanism"], ["Describe addition of bromine, hydrogen or steam to an alkene."]),
    (10, "Ethanol formation mechanism", ["steam addition arrow-pushing mechanism for ethene"], ["Describe ethanol formation by fermentation and hydration of ethene."]),
    (11, "Ethanoic-acid formation mechanisms and equations", ["ethanol oxidation mechanism", "full oxidation equation for ethanoic acid formation"], ["Describe formation of ethanoic acid from ethanol by oxidation."]),
    (12, "Structures and names of protein hydrolysis amino acids", ["draw specific amino acid structures from protein hydrolysis", "name each amino acid product", "Draw the displayed structure of glycine", "Identify alanine in this protein hydrolysate", "H2N-CH2-COOH", "Name each amino acid formed"], ["Describe protein hydrolysis to amino acids."]),
]


def main():
    rules = []
    for index, title, excluded_examples, allowed_examples in RULES:
        evidence = LIMITS[index]
        rules.append({
            "rule_id": f"SCOPE-6117-{len(rules)+1:02d}",
            "construct": title,
            "excluded_examples": excluded_examples,
            "allowed_examples": allowed_examples,
            "source": evidence["source"],
            "context_verbatim": evidence["context_verbatim"],
        })
    out = {
        "status": "draft_for_review",
        "source": FACTS["syllabus_file"],
        "paper_specific_rules": [
            {
                "rule": "Tests for cations with sodium hydroxide or ammonia and tests for anions are assessed only in Paper 3; flame and gas tests may occur in all three papers.",
                "source": LIMITS[6]["source"],
                "context_verbatim": LIMITS[6]["context_verbatim"],
            },
            {
                "rule": "Annexe B qualitative-analysis notes are not supplied with Paper 3.",
                "source": LIMITS[13]["source"],
                "context_verbatim": LIMITS[13]["context_verbatim"],
            },
        ],
        "rules": rules,
        "entries": [{"construct": rule['construct'], "pattern": pattern,
                     "source": f"syllabus PDF p. {rule['source']['pdf_page']}: {rule['source']['verbatim_line']}",
                     "must_catch": rule['excluded_examples'], "must_allow": rule['allowed_examples']}
                    for rule, pattern in zip(rules, PATTERNS)],
    }
    path = WORK / "curriculum/scope-scan.json"
    path.write_text(json.dumps(out, indent=2, ensure_ascii=False) + "\n")
    print(f"Wrote {len(rules)} content rules and 2 paper-specific rules")


if __name__ == "__main__":
    main()
