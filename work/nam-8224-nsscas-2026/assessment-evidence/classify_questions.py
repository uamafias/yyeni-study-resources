#!/usr/bin/env python3
"""Keyword classifier for NSSCAS Chemistry 8224 past papers (Papers 1 and 2).

Reproducible: reads the PDFs in Question Banks/ with pdftotext, writes
  evidence-rows.csv   one row per Paper 1 question / Paper 2 mark-bearing part
  reconciliation.txt  detected marks vs printed totals, per paper
It is a planning aid, NOT evidence of what examiners credited. Keyword
classification is unvalidated until checked against a manually coded sample.

Run:  python3 classify_questions.py
"""
import csv, collections, glob, os, re, subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
PAPERS = os.path.join(ROOT, "Question Banks", "Namibian Curricula", "NSSCAS", "Chemistry (8224)")
PRINTED_TOTAL = {1: 40, 2: 60}

KW = {
 "1.1 Atoms, molecules, stoichiometry": ["mole", "relative atomic mass", "relative molecular", "relative formula", "avogadro", "empirical formula", "molecular formula", "mass spectr", "percentage yield", "mol dm", "mol/dm", "limiting", "stoichiometr", "dm3", "amount of substance", "ionic equation", "balanced equation", "concentration"],
 "1.2 Atomic structure": ["proton", "neutron", "electron configuration", "electronic configuration", "orbital", "sub-shell", "subshell", "nucleon", "isotope", "deflect", "nuclear charge", "shielding", "atomic structure"],
 "1.3 Chemical bonding": ["ionic bond", "covalent", "dative", "electronegativ", "dipole", "hydrogen bond", "van der waals", "intermolecular", "metallic bond", "lattice", "shape of", "bond angle", "sigma", "pi bond", "giant", "lone pair", "polar", "london", "bonding"],
 "1.4 Ideal and real gases": ["ideal gas", "pv", "real gas", "kinetic theory", "gas constant", "pressure", "molar gas volume"],
 "2.1 Chemical energetics": ["enthalpy", "hess", "bond energy", "exothermic", "endothermic", "calorimet", "energy change", "δh", "∆h", "heat energy"],
 "2.2 Electrochemistry": ["oxidation number", "redox", "oxidising", "reducing", "electrolysis", "electrode", "anode", "cathode", "half-equation", "half equation", "oxidation state", "oxidised", "reduced"],
 "2.3 Equilibria": ["equilibrium", "kc", "le chatelier", "brønsted", "bronsted", "ph ", "buffer", "ka ", "dissociat", "acid", "alkali", "kw"],
 "2.4 Reaction kinetics": ["rate of reaction", "activation energy", "catalyst", "boltzmann", "collision", "rate equation", "order of reaction", "half-life", "enzyme", "rate constant", "rate "],
 "3.1 Periodicity": ["period 3", "ionisation energy", "atomic radius", "periodicity", "sodium to argon", "melting point", "oxide of", "across the period", "chlorides of"],
 "3.2 Group 2": ["group 2", "group ii", "magnesium", "calcium", "barium", "strontium", "thermal decomposition", "thermal stability", "carbonate"],
 "3.3 Transition elements": ["transition", "complex ion", "ligand", "copper", "iron", "manganese", "coloured", "variable oxidation", "vanadium", "chromium", "extraction of"],
 "3.4 Group 17": ["halogen", "chlorine", "bromine", "iodine", "halide", "disproportionation", "silver nitrate", "bleach", "water treatment", "group 17", "group vii"],
 "3.5 Nitrogen and Sulfur": ["ammonia", "nitrogen", "nitrate", "acid rain", "sulfur", "sulphur", "haber", "fertili", "nox", "contact process", "sulfuric"],
 "4.1 Foundations of organic": ["functional group", "homologous", "nucleophil", "electrophil", "free radical", "mechanism", "curly", "infra-red", "infrared", "spectrum", "bond fission", "general formula", "heterolytic", "homolytic"],
 "4.2 Hydrocarbons": ["alkane", "alkene", "cracking", "addition polymer", "combustion", "ethene", "hydrocarbon", "crude oil", "propene", "poly", "methane"],
 "4.3 Halogen derivatives": ["halogenoalkane", "haloalkane", "nucleophilic substitution", "bromoethane", "chloroethane", "bromo", "chloro", "iodo", "fluoro", "cfc", "hydrolysis of", "c-br", "c-cl", "c-hal"],
 "4.4 Hydroxyl compounds": ["alcohol", "ethanol", "propan", "butan-", "dehydrat", "primary alcohol", "secondary alcohol", "hydroxyl"],
 "4.5 Isomerism": ["isomer", "cis", "trans", "stereo", "chiral", "optical", "e/z"],
 "4.6 Carbonyl compounds": ["aldehyde", "ketone", "carbonyl", "tollens", "fehling", "2,4-dnph", "nucleophilic addition", "hcn"],
 "4.7 Carboxylic acids/derivatives": ["carboxylic", "ester", "amine", "ethanoic", "amide", "ethanoate", "propanoic"],
}


def scores(text):
    t = " " + text.lower() + " "
    sc = collections.Counter()
    for topic, words in KW.items():
        for w in words:
            n = t.count(w)
            if n:
                sc[topic] += n * (2 if len(w) > 6 else 1)
    return sc


def classify(text):
    """-> (primary, secondary, confidence)"""
    sc = scores(text).most_common(2)
    if not sc:
        return "unclassified", "", "none"
    p, ps = sc[0]
    s, ss = (sc[1] if len(sc) > 1 else ("", 0))
    secondary = s if ss >= 0.5 * ps else ""
    conf = "high" if ps >= 3 and ps >= 2 * ss else ("medium" if ps >= 2 and ps > ss else "low")
    return p, secondary, conf


def pages(pdf):
    out = subprocess.run(["pdftotext", "-layout", pdf, "-"], capture_output=True, text=True, check=True).stdout
    lines, page = [], 1
    for chunk in out.split("\f"):
        for l in chunk.splitlines():
            if re.fullmatch(r"\s*[A-Z]( [A-Z])*\s*", l):   # watermark letters
                continue
            lines.append((page, l))
        page += 1
    return lines


def split_questions(lines, maxq):
    starts, want = [], 1
    for i, (_, l) in enumerate(lines):
        m = re.match(r"^\s{0,2}(\d{1,2})\.?\s+(?=[A-Z(“\"'0-9])", l)
        if m and int(m.group(1)) == want and want <= maxq:
            starts.append(i)
            want += 1
    starts.append(len(lines))
    return [(k + 1, lines[starts[k]:starts[k + 1]]) for k in range(len(starts) - 1)]


def paper_file(year, paper):
    pat = "%s/%s/*%d*.pdf" % (PAPERS, year, paper)
    cands = [f for f in glob.glob(pat) if re.search(r"8224[-_]?%d" % paper, os.path.basename(f))]
    return cands[0] if cands else None


def rows_p1(year, pdf):
    rows = []
    for qn, q in split_questions(pages(pdf), 40):
        text = "\n".join(l for _, l in q)[:1200]
        p, s, c = classify(text)
        rows.append([year, 1, qn, "", 1, p, s, c, q[0][0]])
    return rows


def rows_p2(year, pdf):
    rows, recon = [], []
    for qn, q in split_questions(pages(pdf), 12):
        toks = [(i, int(m.group(1))) for i, (_, l) in enumerate(q) for m in [re.search(r"\[(\d{1,2})\]\s*$", l.strip())] if m]
        if not toks:
            continue
        marks = [k for _, k in toks]
        # These papers print no question subtotals (verified: all four years reconcile
        # to the printed paper total when every [n] is a part mark), so every [n] is a part.
        subtotal = False
        parts = toks
        qtext = "\n".join(l for _, l in q)
        qp, _, _ = classify(qtext)
        prev = 0
        for idx, (i, k) in enumerate(parts, 1):
            seg = "\n".join(l for _, l in q[prev:i + 1]); prev = i + 1
            p, s, c = classify(seg)
            if p == "unclassified":
                p, s, c = qp, "", "low"
            rows.append([year, 2, qn, idx, k, p, s, c, q[i][0]])
        recon.append((qn, sum(k for _, k in parts), marks[-1] if subtotal else None))
    return rows, recon


def main():
    all_rows, report = [], []
    for year in ("2021", "2022", "2023", "2024"):
        f1, f2 = paper_file(year, 1), paper_file(year, 2)
        r1 = rows_p1(year, f1); all_rows += r1
        r2, recon = rows_p2(year, f2); all_rows += r2
        got2 = sum(r[4] for r in r2)
        report.append("%s Paper 1: %d of 40 questions parsed" % (year, len(r1)))
        report.append("%s Paper 2: %d of 60 marks captured; question subtotals found for %s" % (
            year, got2, ", ".join("Q%d=%s" % (qn, st) for qn, _, st in recon if st is not None) or "none"))
        mism = [(qn, s, st) for qn, s, st in recon if st is not None and s != st]
        if mism:
            report.append("   subtotal mismatches (question, summed parts, printed): %s" % mism)
    with open(os.path.join(HERE, "evidence-rows.csv"), "w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["year", "paper", "question", "part_index", "marks", "primary_topic", "secondary_topic", "confidence", "pdf_page"])
        w.writerows(all_rows)
    open(os.path.join(HERE, "reconciliation.txt"), "w").write("\n".join(report) + "\n")
    print("\n".join(report))


if __name__ == "__main__":
    main()
