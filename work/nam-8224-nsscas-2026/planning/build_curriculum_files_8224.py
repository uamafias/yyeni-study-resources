#!/usr/bin/env python3
"""Build curriculum/misconceptions.json, scope-scan.json and answer-shapes.json (step 3).
Misconception wording is ours; every entry cites the 2025 examiner report. Scope sentences come from syllabus-facts.json."""
import json, os, re, collections, datetime
HERE = os.path.dirname(os.path.abspath(__file__)); WS = os.path.dirname(HERE)
NOW = datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
bul = {b["objective_id"]: b for b in json.load(open(os.path.join(HERE, "syllabus_bullets.json")))}
facts = json.load(open(os.path.join(WS, "curriculum", "syllabus-facts.json")))
ev = json.load(open(os.path.join(WS, "assessment-evidence", "assessment_evidence.json")))["records"]

# ------------------------------------------------------------------ misconceptions
M = [
 ("1.1.5-02", "near_neighbour_term", "Using the r.t.p. molar gas volume (24 dm3 mol-1) in a calculation set at s.t.p.",
  "The molar gas volume is 22.4 dm3 mol-1 at s.t.p. and 24.0 dm3 mol-1 at r.t.p.; the conditions the question states decide which value to use.",
  "Does the question say s.t.p. or r.t.p.?", "2025 report, Paper 1 Q3 (51% correct)"),
 ("1.1.3-01", "wrong_angle_same_concept", "Counting the peaks in the mass spectrum of Cl2 as the number of chlorine isotopes.",
  "Peaks of a diatomic element's spectrum include molecular ions made from different isotope combinations, so there are more peaks than isotopes; the isotopes are found by working out which combinations produce each peak.",
  "Is this peak one atom's ion or an ion of a molecule made from two atoms?", "2025 report, Paper 2 Q1(b)(i)"),
 ("1.1.3-02", "wrong_angle_same_concept", "Dividing the sum of (mass x peak height) by 100 when the peak heights are not percentages.",
  "A weighted mean divides by the total of the weights; that total is 100 only when the heights are already percentages.",
  "Do the peak heights add up to 100?", "2025 report, Paper 2 Q1(b)(ii)"),
 ("1.2.1-01", "near_neighbour_term", "Giving the electron a relative mass of 0, or 'nil' for a neutron, as if mass and charge were the same thing.",
  "Relative mass: proton 1, neutron 1, electron about 1/1836 (very small but not zero). Relative charge: proton +1, neutron 0, electron -1.",
  "Is the table column asking about mass or charge?", "2025 report, Paper 2 Q2(a)"),
 ("1.2.1-01", "wrong_angle_same_concept", "Drawing electrons and protons deflected by the same amount in an electric field.",
  "Electron and proton carry charges of equal size but opposite sign, and the electron's mass is far smaller, so it is deflected much more and towards the other plate; neutrons are not deflected. (The syllabus names behaviour in electric fields only in the general objective of 1.2.1.)",
  "Which particle has the smaller mass for the same size of charge?", "2025 report, Paper 2 Q2(b)"),
 ("1.2.3-07", "wrong_angle_same_concept", "Writing chromium as 3d4 4s2, following the simple filling order.",
  "The ground-state configuration of chromium is 1s2 2s2 2p6 3s2 3p6 3d5 4s1: a half-filled 3d sub-shell with one 4s electron.",
  "Does the configuration follow the filling order, or the known exception for Cr?", "2025 report, Paper 2 Q2(c)(i)"),
 ("1.2.3-04", "near_neighbour_term", "Giving how many electrons the s, p and d sub-shells hold when asked how many orbitals of each type are occupied.",
  "Count orbitals, not electrons: an s sub-shell is 1 orbital, a p sub-shell 3 and a d sub-shell 5, and each holds up to 2 electrons.",
  "Is the question about orbitals or electrons?", "2025 report, Paper 2 Q2(c)(iv)"),
 ("2.2.1-05", "near_neighbour_term", "Naming NO2- as nitrate(V) because nitrate is the familiar oxyanion of nitrogen.",
  "Name an oxyanion from the oxidation number you calculate: nitrogen in NO2- is +3, so it is nitrate(III); NO3- is nitrate(V).",
  "What oxidation number does nitrogen have in this ion?", "2025 report, Paper 1 Q15 (24.5% correct)"),
 ("1.3.3-02", "adjacent_concept", "Treating hydrogen chloride as an ionic compound.",
  "Hydrogen chloride is a covalent molecule with a polar bond: the electrons are shared unequally, not transferred.",
  "Are electrons shared (unequally) or transferred from one atom to the other?", "2025 report, Paper 1 Q8 (67% correct; option C most chosen error)"),
 ("1.3.4-01", "near_neighbour_term", "Calling van der Waals forces (or other intermolecular forces) 'bonds' when asked for the bonding in a covalent substance.",
  "Bonding is what holds atoms together inside a molecule or lattice (covalent bonds in SO2); intermolecular forces act between molecules and are weaker.",
  "Does the force act inside the molecule or between molecules?", "2025 report, Paper 2 Q4(b)(iii)"),
 ("2.4.2-01", "adjacent_concept", "Drawing a reaction-pathway (energy profile) diagram when asked for a Boltzmann distribution curve.",
  "A Boltzmann curve plots number of molecules against energy; an energy profile plots energy against progress of reaction.",
  "What is on the vertical axis: number of molecules or energy?", "2025 report, Paper 2 Q3(a)(i)"),
 ("2.4.2-01", "wrong_angle_same_concept", "Saying the area under the right-hand part of the curve is the activation energy.",
  "Activation energy is a value on the energy axis; the area beyond it represents the fraction of molecules with energy at least equal to Ea.",
  "Is Ea a position on the axis or an area under the curve?", "2025 report, Paper 2 Q3(a)(ii)"),
 ("2.4.2-02", "wrong_angle_same_concept", "Explaining the faster rate at a higher temperature only as 'collisions are more frequent'.",
  "A higher temperature raises collision frequency, and also the proportion of molecules with energy at least Ea, so many more collisions are successful.",
  "Have you said more collisions or more successful collisions, and why?", "2025 report, Paper 2 Q3(a)(iv)"),
 ("2.3.1-07", "wrong_angle_same_concept", "Justifying an industrial temperature by yield alone or by rate alone.",
  "For an exothermic equilibrium process, a lower temperature favours the yield and a higher one speeds the reaction; the chosen temperature is a compromise between both.",
  "Have you discussed both rate and yield at the chosen temperature?", "2025 report, Paper 2 Q3(a)(v)"),
 ("3.1.3-02", "wrong_angle_same_concept", "Saying the maximum oxidation number of the Period 3 oxides rises and then falls across the period.",
  "Across the oxides from sodium to sulfur (the range the syllabus names) the oxidation number of the element rises from +1 to +6, matching the number of valence electrons used.",
  "Compare the oxidation number in Na2O, MgO, Al2O3, SiO2, P4O10 and SO3: does it ever fall?", "2025 report, Paper 2 Q4(b)(i)"),
 ("4.4.1-04", "near_neighbour_term", "Naming dilute acid as the reagent to dehydrate an alcohol to an alkene.",
  "Dehydration of an alcohol needs concentrated acid (or a hot catalyst); dilute acid supplies water and favours the reverse, hydration.",
  "Is the acid concentrated or dilute?", "2025 report, Paper 2 Q5(c)(i)"),
 ("4.4.1-07", "wrong_angle_same_concept", "Describing a positive alkaline iodine test as a colour change in solution.",
  "A positive alkaline iodine test gives a pale yellow precipitate (tri-iodomethane).",
  "Does the result describe a precipitate or only a colour change?", "2025 report, Paper 2 Q5(d)(ii)"),
 ("4.4.1-07", "near_neighbour_term", "Naming an iodoalkane such as iodobutane as the compound that forms in the alkaline iodine test.",
  "The yellow solid formed is tri-iodomethane, CHI3, produced from the CH3CH(OH)- group; the alcohol is not turned into an iodoalkane.",
  "Which group in the alcohol reacts, and what does it become?", "2025 report, Paper 2 Q5(d)(iii)"),
 ("4.2.2-09", "wrong_angle_same_concept", "Drawing the repeat unit of an addition polymer with the C=C double bond still in it.",
  "In addition polymerisation the double bond is used up: the repeat unit is saturated, with a bond extending out of each end.",
  "Does the repeat unit still contain C=C?", "2025 report, Paper 2 Q5(c)(ii)"),
]
entries = []
for i, (oid, kind, a, b, test, src) in enumerate(M, 1):
    full = "OBJ-8224-" + oid
    assert full in bul, full
    entries.append({"evidence_scope": "subject", "entry_id": "MC-8224-%02d" % i, "topic_id": bul[full]["unit"], "objective_id": full,
                    "objective_text": bul[full]["text"][:240], "a": a, "b": b, "kind": kind, "test": test, "n": 1, "series": ["2025"],
                    "evidence": src, "evidence_strength": "stated by the examiner report; single series; question paper not held"})
json.dump({"register_id": "MISCON-NAM-8224-NSSCAS-2026", "generated_at": NOW,
  "authority": "NSSCAS Examiners Report 2025, Chemistry 8224 Papers 1-3. Only examiner-report evidence held for this subject; 2021-2024 reports do not exist.",
  "derivation_policy": "Curated by hand from the located examiner statements and restated in our words. Slips, answering habits (for example citing parallax or human error as an experimental error), item-specific mistakes and items where the report states only the correct answer were left out. No report wording appears in learner-facing output.",
  "how_to_use": "Every entry earns one MISCON card on its objective: the error, the correct idea, and the test that tells them apart. Each is single-source (one report, one series), so under the two-source rule agreed for this run it needs a second source before it publishes as examiner-evidenced.",
  "kinds": {"adjacent_concept": "Two different concepts that sit near each other in the syllabus.", "near_neighbour_term": "Two similar terms or values confused.", "wrong_angle_same_concept": "The right concept approached or applied the wrong way."},
  "entries": entries}, open(os.path.join(WS, "curriculum", "misconceptions.json"), "w"), indent=1, ensure_ascii=False)

# ------------------------------------------------------------------ scope scan
lim = {l["verbatim"]: l for l in facts["limits"]}
def L(sub):
    for k, v in lim.items():
        if sub in k: return v
    raise SystemExit("limit not found: " + sub)
S = [
 ("how a mass spectrometer works", r"\bmagnetic field\b[^.]{0,60}\b(?:deflect|bend)|\b(?:deflect|bend)\w*[^.]{0,60}\bmagnetic field\b|\bmass spectrometer\b[^.]{0,100}\b(?:accelerat|ionis(?:ed|ation chamber)|vaporis)",
  ["the ions are accelerated and then deflected by a magnetic field before the detector", "in the mass spectrometer the sample is vaporised and ionised"],
  ["Each peak shows an ion with its m/e value and relative abundance.", "Electrons are deflected towards the positive plate in an electric field."], "working of the mass spectrometer is not required", "1.1.3"),
 ("hybridisation", r"\bsp[23]?\b[- ]hybrid|\bhybridi[sz](?:ed|ation)\b",
  ["the carbon atom is sp3 hybridised", "hybridisation of the orbitals explains the shape"], ["The molecule is tetrahedral because of electron-pair repulsion.", "The shapes follow the electron-pair repulsion model."], "hybridisation is not required", "1.3.4"),
 ("the relationship between Kp and Kc", r"\bK[p] ?= ?K[c] ?\(RT\)|Δn\b[^.]{0,30}RT|relationship between K[p] and K[c]",
  ["Kp = Kc(RT)^Δn links the two constants", "derive the relationship between Kp and Kc"], ["Write an expression for Kc for this reaction.", "Write an expression for Kp using partial pressures."], "relationship between Kp and Kc is not required", "2.3.1"),
 ("quadratic equations in equilibrium calculations", r"\bquadratic (?:equation|formula)\b|-b ?± ?√",
  ["solve the quadratic equation for x to find the equilibrium concentration", "use the quadratic formula"], ["Substitute the equilibrium concentrations into the Kc expression.", "Calculate Kc from the equilibrium concentrations."], "will not require the solving of quadratic equations", "2.3.1"),
 ("effect of paired electrons on ionisation energy", r"\bpaired[- ]electrons?\b[^.]{0,80}\bionisation energy\b|\bionisation energy\b[^.]{0,80}\bpaired[- ]electrons?\b|\bpaired[- ]electron repulsion\b",
  ["the first ionisation energy of oxygen is lower because of repulsion between paired electrons", "paired electron repulsion explains the dip at sulfur"], ["First ionisation energy generally increases across Period 3.", "Electrons are removed from the outer shell."], "effect of paired electrons in orbitals of sub-shells is not expected", "3.1.1 and 3.1.2"),
 ("E/Z priority rules", r"\bCahn[- ]Ingold[- ]Prelog\b|\bCIP\b rules?|\(E\)-|\(Z\)-|\b[EZ]-but-2-ene\b",
  ["assign (E) or (Z) using the Cahn-Ingold-Prelog priority rules", "name the isomer (Z)-but-2-ene"], ["Draw the cis and trans isomers of but-2-ene.", "Cis-trans isomerism arises from restricted rotation about C=C."], "use of E, Z nomenclature is acceptable but is not required", "4.5"),
 ("diastereoisomers", r"\bdiastereo(?:iso)?mers?\b|\bmeso (?:compound|form|isomer)\b",
  ["a molecule with two chiral centres has diastereoisomers", "the meso compound is optically inactive"], ["Enantiomers are non-superimposable mirror images.", "A chiral centre has four different groups attached."], "diastereoisomers is not required", "4.5"),
 ("systematic qualitative analysis and traditional separation", r"\bsystematic (?:qualitative )?analysis\b|\bseparation scheme\b|\bborax bead\b",
  ["use the systematic qualitative analysis scheme to separate the cations into groups", "a borax bead test identifies the metal"], ["Test for the sulfate ion with acidified barium nitrate.", "Add sodium hydroxide dropwise, then in excess, and record the observations."], "Systematic qualitative analysis and knowledge of traditional methods of separation will not be", "Paper 3, Annexe A"),
 ("ions outside the listed cations and anions", r"\b(?:nickel|cobalt|lead\(II\)|silver|tin\(II\)|lithium|potassium)\b[^.]{0,40}\b(?:ion|cation)s?\b[^.]{0,60}\b(?:test|precipitate|sodium hydroxide|aqueous ammonia)",
  ["nickel ions give a green precipitate with sodium hydroxide", "silver ions are tested with aqueous ammonia"], ["Aqueous copper(II) ions give a blue precipitate with sodium hydroxide.", "Potassium ions are spectator ions in this reaction."], "candidates will not be expected to identify the ions but only to draw conclusions of a general nature", "Paper 3, Annexe A"),
]
entries = []
for construct, pat, mc, ma, sub, applies in S:
    l = L(sub)
    entries.append({"construct": construct, "pattern": pat, "applies_to": applies, "controls": {"must_catch": mc, "must_allow": ma},
                    "source": "syllabus, page %s, %s" % (l["page"], l["applies_to"]), "syllabus_sentence": l["verbatim"],
                    "provenance": {"sentence": "syllabus", "pattern": "judgement"}})
entries.append({"construct": "weak-acid pH and acid dissociation constants", "pattern": r"\bKa\b|\bpKa\b|\bacid dissociation constant\b|\bbuffer(?:s| solution)?\b",
                "applies_to": "2.3.2", "controls": {"must_catch": ["calculate the pH of a weak acid using Ka", "a buffer resists changes in pH"], "must_allow": ["Calculate the pH of a strong acid from its concentration.", "Weak acids are only partly dissociated."]},
                "source": "syllabus, page 14, 2.3.2", "syllabus_sentence": "calculate [H+(aq)] and pH values for strong acids",
                "provenance": {"sentence": "syllabus (the bullet names strong acids only)", "pattern": "judgement; exclusion is inferred, not stated"}})
json.dump({"scope_scan_id": "SCOPE-SCAN-NAM-8224-NSSCAS", "generated_at": NOW,
  "rule": "RS-15. Each entry is one limit the syllabus states (or one inferred exclusion, labelled), with the pattern C-11 scans learner-facing text for. The sentence is the syllabus's; the pattern is our judgement. Patterns are drafts: C-11 must be run against real authored text and narrowed where it flags ordinary text.",
  "entries": entries}, open(os.path.join(WS, "curriculum", "scope-scan.json"), "w"), indent=1, ensure_ascii=False)

# ------------------------------------------------------------------ answer shapes
def base(cw):
    c = (cw or "").strip()
    low = c.lower()
    if any(k in low for k in ("record", "table", "carry out", "select reagents", "use observations", "weigh")): return "Practical: record / tests"
    if low.startswith(("which", "what", "how many")): return "Question word (which / what / how many)"
    if low.startswith("obtain"): return "Calculate"
    m = re.match(r"[A-Za-z]+", c)
    return m.group(0).title() if m else c
pp = [r for r in ev if r["evidence_type"] == "past_paper" and r["paper_id"] in ("P2", "P3") and r.get("command_word")]
obs = collections.defaultdict(lambda: collections.Counter()); paper = collections.defaultdict(collections.Counter)
for r in pp:
    obs[(base(r["command_word"]), r["mark_tariff"])][0] += 1; paper[(base(r["command_word"]), r["mark_tariff"])][r["paper_id"]] += 1
er = [r for r in ev if r["evidence_type"] == "examiner_report" and r["paper_id"] in ("P2", "P3") and r["mark_tariff"] and r["creditworthy_points"]]
pts = collections.Counter()
for r in er: pts[(r["mark_tariff"], len(r["creditworthy_points"]))] += 1
shapes = [{"command": c, "marks": m, "observed": obs[(c, m)][0], "papers": dict(paper[(c, m)])} for (c, m) in sorted(obs, key=lambda k: (-sum(obs[k].values()), k[0], k[1]))]
glossary = [w.strip().title() for cw in facts["command_words"] for w in cw["words"]]
seen = collections.Counter(); [seen.update({base(r["command_word"]): 1}) for r in pp]
doc = {"_provenance": {"derived_from": "Question papers 2021-2024 (Papers 2 and 3) for command words and tariffs; the 2025 examiner report for the shape of marking points",
        "derivation_policy": "structure only. No question or mark-scheme wording is reproduced in learner-facing output.",
        "status": "PARTIAL. There are no mark schemes for 2021-2024, so credited-answer shape is known only from the %d 2025 Paper 2/3 parts the report describes." % len(er),
        "validation": "Paper 2 tariffs sum to 60 on all four papers and Paper 3 to 40 on all four (2024 Paper 2 Q1(a)-(f) marks are inferred: the page shows only a total of 6).", "generated": NOW},
  "8224": {"subject": "Namibia NSSCAS Chemistry",
    "paper_architecture": {"P1": "40 four-choice items, 1 hour, 40 marks, AO A and B equally, command words not printed (syllabus p. 31).", "P2": "60 marks, 1 hour 15 minutes, compulsory structured and free-response questions, AO A and B equally (p. 31).", "P3": "40 marks, 2 hours, two or three timed experiments, AO C only (p. 31)."},
    "shapes": shapes,
    "listed_never_observed": sorted(w for w in glossary if w not in seen) ,
    "observed_not_in_glossary": sorted(k for k in seen if k not in glossary),
    "er2025_marking_points_vs_tariff": {"basis": "2025 report, Paper 2 and 3 parts with a tariff and listed marking points", "parts": len(er),
        "table": [{"tariff": t, "listed_points": n, "parts": c} for (t, n), c in sorted(pts.items())]},
    "stated_by_er2025": ["Give calculated answers to the number of significant figures the data justify, and say so in the working.",
        "Convert cm3 to dm3 before using a concentration or molar volume; use Ar values as printed (24.3 for Mg, not 24).",
        "Quote the printed tariff as the guide to how many separate points to make.",
        "Use the full term; give both the bond and the wavenumber range for infra-red peaks; draw displayed formulae with every bond, including O-H.",
        "Name versus formula: answer in the form asked.",
        "Practical: record readings to the burette's precision, put units in column headings, use concordant titres and exclude the rough titre; name an acceptable source of error (apparatus or method, not 'human error' or parallax); say 'soluble' or 'not soluble in excess' when adding excess NaOH or ammonia; draw a conclusion about the ions present."]}}
json.dump(doc, open(os.path.join(WS, "curriculum", "answer-shapes.json"), "w"), indent=1, ensure_ascii=False)
print("misconceptions", len(M), "| scope entries", len(S) + 1, "| shapes", len(shapes), "| ER parts with points", len(er))
print("listed never observed:", doc["8224"]["listed_never_observed"]); print("observed not in glossary:", doc["8224"]["observed_not_in_glossary"])
print("observed glossary words:", {k: v for k, v in seen.items() if k in glossary})
