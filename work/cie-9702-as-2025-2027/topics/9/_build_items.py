#!/usr/bin/env python3
"""Build topics/9/learning-items/topic_9_items.json from the slot spec."""
import json, os, sys, hashlib

WS = '/Users/professor/Documents/YYeni Study Resources/work/cie-9702-as-2025-2027'
STD = '/Users/professor/Documents/YYeni Study Resources/standard/v0.2.0-draft'
TD = os.path.join(WS, 'topics', '9')
sys.path.insert(0, os.path.join(STD, 'checks'))
from yyeni_checks import _artefact_text

def H(x):
    return hashlib.sha256(_artefact_text(x).encode()).hexdigest()

CTX = {"sector": None, "business_size": None, "ownership": None, "situation": None, "facts": []}

def flash(slot, obj, sub, ao, cw, tariff, diff, blooms, claims, prompt, answer, guidance, misc=None):
    it = {
        "item_id": slot, "objective_ids": [obj], "claim_ids": claims,
        "item_type": "flashcard", "subtype": sub, "assessment_objectives": ao,
        "blooms_level": blooms, "command_word": cw, "mark_tariff": tariff,
        "difficulty": diff, "prompt": prompt, "canonical_answer": answer,
        "marking_guidance": guidance, "context": dict(CTX),
        "prerequisite_item_ids": [], "core_status": "core",
        "intentional_duplicate_group": None,
        "provenance": ("Authored for topic 9 of the 9702 AS workspace from the topic 9 claim ledger."
                       + (" Discriminates misconception %s from curriculum/misconceptions.json." % misc["mc"] if misc else "")),
        "qa_status": "review_required",
        "claims_seen": {c: 1 for c in claims},
    }
    it["authored_hash"] = H(it)
    return it

items = []

# ================= 9.1-01 current is a flow of charge carriers =================
items.append(flash(
 "ITEM-9702-9-001-DEF","OBJ-9702-9.1-01","DEF",["AO1"],"State",1,2,"Remember",
 ["CLM-9702-9-001","CLM-9702-9-002"],
 "State what is meant by an electric current.",
 "An electric current is a flow of charge carriers, such as conduction electrons in a metal wire or ions in a conducting liquid. The current at a point is the charge passing that point per unit time, I = Q/t.",
 ["1 mark: the definition as a flow of charge carriers; the rate idea or the equation I = Q/t with its symbols earns the mark as well as the word flow."]))

items.append(flash(
 "ITEM-9702-9-002-MECH","OBJ-9702-9.1-01","MECH",["AO2"],"Explain",2,2,"Understand",
 ["CLM-9702-9-001","CLM-9702-9-002"],
 "In the conducting liquid between two electrodes of a copper-refining tank near Tsumeb, positive ions drift towards one electrode and negative ions drift towards the other. Explain how two opposite drifts produce one current, not two.",
 "The current is the rate at which charge passes a cross-section of the liquid. A positive ion moving one way and a negative ion moving the other way both shift positive charge in the same direction round the circuit, so their contributions add. Because each carrier carries a whole-number multiple of the elementary charge, the single current is the total charge passing per second divided by the time, I = Q/t.",
 ["1 mark: how the two streams add - both drifts move positive charge the same way round, so the charges passed per second add, because the negative ion moving one way is equivalent to positive charge moving the other way.",
  "1 mark: the current is then one quantity, the charge passing a point per unit time, I = Q/t."]))

items.append(flash(
 "ITEM-9702-9-055-FEATURE","OBJ-9702-9.1-01","FEATURE",["AO1"],"State",1,3,"Remember",
 ["CLM-9702-9-001","CLM-9702-9-003"],
 "State one feature of the charge carriers in a metal wire that distinguishes them from the carriers in a conducting liquid.",
 "In a metal the charge carriers are free conduction electrons, negatively charged, all drifting in one direction with a small speed; in a conducting liquid the carriers include positive ions drifting one way as well as negative ions drifting the other.",
 ["1 mark: one distinguishing feature, such as electrons only versus ions of both signs; the negative charge of the electron is itself a creditable characteristic."]))

items.append(flash(
 "ITEM-9702-9-069-DIST","OBJ-9702-9.1-01","DIST",["AO1"],"State",1,3,"Understand",
 ["CLM-9702-9-003"],
 "State the difference between conventional current and the drift of the conduction electrons in a metal wire.",
 "Conventional current is taken in the direction in which positive charge would move. The conduction electrons are negative, so they drift in the direction opposite to the conventional current; both refer to the one flow of charge in the wire.",
 ["1 mark: the difference stated with its whereas - conventional current follows positive charge, while the electrons drift the opposite way because they carry negative charge."]))

# ================= 9.1-02 quantised charge =================
items.append(flash(
 "ITEM-9702-9-003-DEF","OBJ-9702-9.1-02","DEF",["AO1"],"State",1,2,"Remember",
 ["CLM-9702-9-004"],
 "State what is meant by the statement that the charge on charge carriers is quantised.",
 "Charge comes in whole packets: the charge on any carrier is a whole-number multiple of the elementary charge e = 1.60 × 10⁻¹⁹ C. No carrier holds a fraction of e.",
 ["1 mark: the definition - charge in whole-number multiples of e, with the value of e stated or implied as the unit of quantisation."]))

items.append(flash(
 "ITEM-9702-9-004-MECH","OBJ-9702-9.1-02","MECH",["AO2"],"Explain",2,2,"Understand",
 ["CLM-9702-9-004","CLM-9702-9-005"],
 "A dust grain in an Opuwo workshop acquires a charge of −4.8 × 10⁻¹⁹ C, and a learner says this is the charge of three electrons. Explain how the numbers support the learner, and then explain why a grain charge of −4.0 × 10⁻¹⁹ C could not be built from electrons.",
 "The test is whether the charge is a whole-number multiple of e. For the first grain: 4.8 ÷ 1.60 = 3.0, so the charge is exactly 3e, which three electrons supply. For the second: 4.0 ÷ 1.60 = 2.5, not a whole number, so no whole number of electrons, each of charge −e, can hold that charge; charge is quantised, so it cannot be built.",
 ["1 mark: how the first number works - it is 3e, because 4.8 ÷ 1.60 = 3.0 is a whole number of elementary charges.",
  "1 mark: why the second fails - 4.0 ÷ 1.60 = 2.5 is not a whole number of packets, so the charge cannot be built from carriers that each hold e."]))

items.append(flash(
 "ITEM-9702-9-050-MISCON","OBJ-9702-9.1-02","MISCON",["AO1"],"Explain",1,3,"Understand",
 ["CLM-9702-9-004","CLM-9702-9-005"],
 "A learner states that every charge carrier in a circuit is an electron, and that a single carrier can hold a charge of 0.80 × 10⁻¹⁹ C. Explain the two errors and give the test that separates them from the truth.",
 "Error one: charge carriers are not only electrons; positive ions carry charge in conducting liquids and in some detectors, so assuming only electrons carry charge goes wrong. Error two: 0.80 × 10⁻¹⁹ C is half of e, and charge is quantised, so no single carrier holds it; every carrier holds a whole-number multiple of e = 1.60 × 10⁻¹⁹ C. The test: is the charge a whole-number multiple of e, and can the carrier be something other than an electron?",
 ["1 mark: both errors named with the correction - carriers may instead be ions, and in fact no carrier can hold a charge that is not a whole-number multiple of e; the error statement is the confusion the card clears."],
 misc={"mc":"MC-9702-9-05"}))

items.append(flash(
 "ITEM-9702-9-056-FEATURE","OBJ-9702-9.1-02","FEATURE",["AO1"],"State",1,3,"Remember",
 ["CLM-9702-9-004"],
 "State one feature of the elementary charge e.",
 "The elementary charge is the size of the smallest packet of charge, e = 1.60 × 10⁻¹⁹ C; the charge on any carrier is a whole-number multiple of it, positive or negative.",
 ["1 mark: one correct feature, such as its value 1.60 × 10⁻¹⁹ C, or the property that all carrier charges are whole-number multiples of it."]))

items.append(flash(
 "ITEM-9702-9-070-DIST","OBJ-9702-9.1-02","DIST",["AO1"],"State",1,3,"Understand",
 ["CLM-9702-9-004","CLM-9702-9-005"],
 "State the difference between the charge on a single electron and the charge on an object that has gained excess electrons.",
 "A single electron holds exactly −e = −1.60 × 10⁻¹⁹ C. An object with excess electrons holds a whole-number multiple of e set by how many electrons it gained, for example five excess electrons give −8.0 × 10⁻¹⁹ C.",
 ["1 mark: the distinction - one electron holds exactly one packet, whereas an object holds a whole-number multiple of e depending on the count of carriers."]))

# ================= 9.1-03 Q = It =================
items.append(flash(
 "ITEM-9702-9-005-DEF","OBJ-9702-9.1-03","DEF",["AO1"],"State",1,2,"Remember",
 ["CLM-9702-9-006","CLM-9702-9-007"],
 "State the equation linking charge, current and time, giving the unit of each symbol.",
 "Q = It. The charge Q is in coulombs, the current I is in amperes and the time t is in seconds; one coulomb passes when one ampere flows for one second.",
 ["1 mark: the equation Q = It stated with the meaning and unit of every symbol - coulombs, amperes, seconds."]))

items.append(flash(
 "ITEM-9702-9-006-CALC","OBJ-9702-9.1-03","CALC",["AO2"],"Calculate",2,2,"Apply",
 ["CLM-9702-9-006"],
 "A display spotlight in a museum in Windhoek draws a current of 0.45 A for 5.0 minutes. Calculate the charge that passes through it.",
 "Convert the time first: 5.0 minutes is 5.0 × 60 = 300 s. Then Q = It = 0.45 × 300 = 135 C. The charge that passes is 135 C, which is 140 C to two significant figures.",
 ["Equation and substitution: Q = It with the time converted to 300 s and the working 0.45 × 300 = 135 - 1 mark.",
  "Final answer: 140 C to two significant figures, with the unit - 1 mark. A charge of 2.25 C means the minutes were not converted."]))

items.append(flash(
 "ITEM-9702-9-007-CALC","OBJ-9702-9.1-03","CALC",["AO2"],"Calculate",2,2,"Apply",
 ["CLM-9702-9-006"],
 "The flash tube of a camera passes a charge of 0.15 C in a time of 2.0 ms. Calculate the average current in the tube.",
 "Convert the time: 2.0 ms is 2.0 × 10⁻³ s = 0.0020 s. Rearranged, I = Q/t. Substitute: I = 0.15 ÷ 0.0020 = 75 A. The average current is 75 A, which is 75 A to two significant figures.",
 ["Equation and substitution: I = Q/t with the time converted to 0.0020 s and the working 0.15 ÷ 0.0020 = 75 - 1 mark.",
  "Final answer: 75 A with the unit - 1 mark. An answer of 0.075 A comes from dividing by 2.0 without converting the milliseconds."]))

items.append(flash(
 "ITEM-9702-9-008-CALC","OBJ-9702-9.1-03","CALC",["AO2"],"Calculate",2,2,"Apply",
 ["CLM-9702-9-006"],
 "A maintenance charger at a garage in Otjiwarongo feeds a lorry battery with a steady current of 0.25 A. Calculate the time taken for a charge of 900 C to pass.",
 "Rearranged, t = Q/I. Substitute: t = 900 ÷ 0.25 = 3600 s. The time is 3600 s, which is 1.0 hour, so 3.6 × 10³ s to two significant figures.",
 ["Equation and substitution: t = Q/I with the working 900 ÷ 0.25 = 3600 - 1 mark.",
  "Final answer: 3600 s with the unit, or 1.0 hour stated as the same time - 1 mark."]))

items.append(flash(
 "ITEM-9702-9-057-FEATURE","OBJ-9702-9.1-03","FEATURE",["AO1"],"State",1,3,"Remember",
 ["CLM-9702-9-007"],
 "State one feature of the coulomb as a unit.",
 "One coulomb is the charge that passes a point when a current of one ampere flows for one second; it is about 6.25 × 10¹⁸ elementary charges.",
 ["1 mark: one correct feature, such as the definition through one ampere for one second, or its size in elementary charges."]))

items.append(flash(
 "ITEM-9702-9-071-DIST","OBJ-9702-9.1-03","DIST",["AO1"],"State",1,3,"Understand",
 ["CLM-9702-9-002","CLM-9702-9-006"],
 "State the difference between the current in a wire and the charge that passes a point in the wire.",
 "Current is a rate: the charge passing per unit time, in amperes, which are coulombs per second. Charge is the total that has passed, in coulombs. They are linked by Q = It.",
 ["1 mark: the difference - a rate in amperes whereas a total in coulombs, with Q = It naming how the two relate."]))

# ================= 9.1-04 I = Anvq =================
items.append(flash(
 "ITEM-9702-9-009-DEF","OBJ-9702-9.1-04","DEF",["AO1"],"State",1,2,"Remember",
 ["CLM-9702-9-008"],
 "State the expression for the current in a current-carrying conductor in terms of the charge carriers, defining every symbol and its unit.",
 "I = Anvq. The current I is in amperes; A is the cross-sectional area of the conductor in m²; n is the number density of the charge carriers, in carriers per m³, written m⁻³; v is the drift speed of the carriers in m s⁻¹; q is the charge on one carrier in coulombs.",
 ["1 mark: the equation I = Anvq with every symbol defined and its unit given - area in m², number density in m⁻³, drift speed in m s⁻¹, charge in coulombs."]))

items.append(flash(
 "ITEM-9702-9-010-CALC","OBJ-9702-9.1-04","CALC",["AO2"],"Calculate",2,2,"Apply",
 ["CLM-9702-9-008"],
 "A manganin wire of cross-sectional area 0.50 mm² carries a current of 2.4 A. Manganin has a number density of conduction electrons of 3.2 × 10²⁸ m⁻³. Calculate the drift speed of the electrons.",
 "Convert the area: 0.50 mm² is 0.50 × 10⁻⁶ m². Rearranged, v = I ÷ (Anq). First Anq = 0.50 × 3.2 = 1.6, then 1.6 × 1.60 = 2.56, and the powers of ten give 10⁻⁶⁺²⁸⁻¹⁹ = 10³, so Anq = 2.56 × 10³ = 2560. Substitute: v = 2.4 ÷ 2560 = 0.0009375 m s⁻¹. That is 9.375 × 10⁻⁴ m s⁻¹, so the drift speed is 9.4 × 10⁻⁴ m s⁻¹ to two significant figures.",
 ["Equation and substitution: v = I/(Anq) with the area converted and the working shown step by step to Anq = 2560 - 1 mark.",
  "Final answer: 9.4 × 10⁻⁴ m s⁻¹ with the unit and two significant figures - 1 mark. Forgetting to convert the area gives a value 10⁶ times too small."]))

items.append(flash(
 "ITEM-9702-9-011-CALC","OBJ-9702-9.1-04","CALC",["AO2"],"Calculate",2,2,"Apply",
 ["CLM-9702-9-008"],
 "A strip of conducting glass used in a laboratory sensor carries a current of 5.0 A. Its cross-sectional area is 0.75 mm² and the drift speed of its carriers is measured as 1.5 × 10⁻⁴ m s⁻¹. Calculate the number density of the carriers, each of charge 1.60 × 10⁻¹⁹ C.",
 "Rearranged, n = I ÷ (Avq). First the area: 0.75 mm² is 0.75 × 10⁻⁶ m². Then Avq = 0.75 × 1.5 = 1.125, and 1.125 × 1.60 = 1.8, with the powers of ten giving 10⁻⁶⁻⁴⁻¹⁹ = 10⁻²⁹, so Avq = 1.8 × 10⁻²⁹. Substitute: n = 5.0 ÷ 1.8 = 2.78, so n = 2.78 × 10²⁹ m⁻³. The number density is 2.8 × 10²⁹ m⁻³ to two significant figures.",
 ["Equation and substitution: n = I/(Avq) with the area converted and the bottom line built step by step - 1 mark.",
  "Final answer: 2.8 × 10²⁹ m⁻³ with the unit and two significant figures - 1 mark."]))

items.append(flash(
 "ITEM-9702-9-012-CALC","OBJ-9702-9.1-04","CALC",["AO2"],"Calculate",2,2,"Apply",
 ["CLM-9702-9-008"],
 "An experimental power cable of a new alloy carries 8.0 A. The number density of its conduction electrons is 6.0 × 10²⁸ m⁻³ and their drift speed is 3.0 × 10⁻⁴ m s⁻¹. Calculate the cross-sectional area of the cable.",
 "Rearranged, A = I ÷ (nvq). First nvq = 6.0 × 3.0 = 18, then 18 × 1.60 = 28.8, and the powers of ten give 10²⁸⁻⁴⁻¹⁹ = 10⁵, so nvq = 28.8 × 10⁵ = 2.88 × 10⁶. Substitute: A = 8.0 ÷ 2.88 = 2.78, so A = 2.78 × 10⁻⁶ m². The cross-sectional area is 2.8 × 10⁻⁶ m² to two significant figures, which is 2.8 mm².",
 ["Equation and substitution: A = I/(nvq) with the bottom line assembled step by step to 2.88 × 10⁶ - 1 mark.",
  "Final answer: 2.8 × 10⁻⁶ m², or 2.8 mm², with the unit and two significant figures - 1 mark."]))

items.append(flash(
 "ITEM-9702-9-049-MISCON","OBJ-9702-9.1-04","MISCON",["AO1"],"Explain",1,3,"Understand",
 ["CLM-9702-9-008","CLM-9702-9-010"],
 "A learner calculates the current in a wire by multiplying the total number of free electrons in the whole wire by the charge on each and by their drift speed. Explain the error and give the test that identifies it.",
 "The error is using the total number of electrons in the wire. Only the carriers that pass a cross-section each second make the current: I = Anvq uses the number density n, the carriers per cubic metre, times the area, times the distance drifted per second. The test: is the quantity entered a number per cubic metre? A total count is not; n multiplied by A and by v counts exactly the carriers that pass.",
 ["1 mark: the error named - a total count used instead of the density - and the correction stated: in fact n is a number per cubic metre, and the carriers contributing are only those passing the cross-section each second."],
 misc={"mc":"MC-9702-9-04"}))

items.append(flash(
 "ITEM-9702-9-058-FEATURE","OBJ-9702-9.1-04","FEATURE",["AO1"],"State",1,3,"Remember",
 ["CLM-9702-9-009"],
 "State one feature of the drift speed of conduction electrons in a metal carrying an everyday current.",
 "It is very small, of the order of 10⁻⁴ m s⁻¹ for currents of a few amperes in ordinary wires, because the number density of carriers, about 10²⁸ to 10²⁹ m⁻³, is so large that a slow drift carries the charge.",
 ["1 mark: one correct feature, such as its small order of size, or the reason for it in the large number density of carriers."]))

items.append(flash(
 "ITEM-9702-9-072-DIST","OBJ-9702-9.1-04","DIST",["AO1"],"State",1,3,"Understand",
 ["CLM-9702-9-008","CLM-9702-9-010"],
 "State the difference between the number density n in I = Anvq and the total number of free electrons in a wire.",
 "The number density counts carriers per cubic metre of the conductor, whereas the total number counts every free electron in the whole sample. Only n, multiplied by the area and the distance drifted per second, gives the carriers that pass a point and so make the current.",
 ["1 mark: the distinction - per cubic metre versus the whole wire - with the point that only the density enters the equation because the current is made by carriers passing a cross-section."]))

# ================= 9.2-01 define p.d. =================
items.append(flash(
 "ITEM-9702-9-013-DEF","OBJ-9702-9.2-01","DEF",["AO1"],"Define",1,1,"Remember",
 ["CLM-9702-9-011","CLM-9702-9-012"],
 "Define the potential difference across a component.",
 "The potential difference across a component is the energy transferred from electrical to other forms per unit charge passing through it, V = W/Q.",
 ["1 mark: the definition as energy transferred per unit charge; the equation with its symbols is an equally full statement of the meaning."]))

items.append(flash(
 "ITEM-9702-9-014-CALC","OBJ-9702-9.2-01","CALC",["AO2"],"Calculate",2,1,"Apply",
 ["CLM-9702-9-012"],
 "A bedside lamp at a hostel in Outapi converts 84 J of electrical energy while charge passes through it from a 12 V supply. Calculate the charge that passes.",
 "Rearranged, Q = W/V. Substitute: Q = 84 ÷ 12 = 7.0 C. The charge that passes is 7.0 C.",
 ["Equation and substitution: Q = W/V with the working 84 ÷ 12 = 7.0 - 1 mark.",
  "Final answer: 7.0 C with the unit - 1 mark."]))

items.append(flash(
 "ITEM-9702-9-046-MISCON","OBJ-9702-9.2-01","MISCON",["AO1"],"Explain",1,2,"Understand",
 ["CLM-9702-9-011","CLM-9702-9-012"],
 "A learner defines potential difference as 'the energy used up in a component'. Explain what the definition leaves out, and give the full definition.",
 "The definition leaves out the division by charge: it states an energy, not a ratio. Potential difference is the energy transferred from electrical to other forms per unit charge passing through the component, V = W/Q. The test: is energy divided by charge? Without that division a big lamp and a small lamp running on the same p.d. would seem to have different potential differences across them, which they do not.",
 ["1 mark: the error named - the missing per unit charge - and in fact the correct ratio given, V = W/Q, as the definition that can be tested with numbers."],
 misc={"mc":"MC-9702-9-01"}))

items.append(flash(
 "ITEM-9702-9-065-FEATURE","OBJ-9702-9.2-01","FEATURE",["AO1"],"State",1,2,"Remember",
 ["CLM-9702-9-011"],
 "State one feature of the potential difference across a component.",
 "It is measured in volts, and one volt is one joule per coulomb: the p.d. tells how much energy each coulomb passing through the component converts from electrical form. A voltmeter reads it, connected across the component.",
 ["1 mark: one correct feature, such as its unit and its meaning as joules per coulomb, or how it is measured."]))

items.append(flash(
 "ITEM-9702-9-080-DIST","OBJ-9702-9.2-01","DIST",["AO1"],"State",1,2,"Understand",
 ["CLM-9702-9-011","CLM-9702-9-012"],
 "State the difference between a potential difference of 6 V across a component and an energy transfer of 6 J in it.",
 "The 6 V is a ratio: 6 joules converted per coulomb that passes, whatever the total. The 6 J is a total energy, for all the charge that passed. They are linked by W = VQ: the 6 V component converts 6 J for every coulomb.",
 ["1 mark: the difference - a per-coulomb ratio whereas a total - with W = VQ naming how the two relate."]))

# ================= 9.2-02 V = W/Q =================
items.append(flash(
 "ITEM-9702-9-015-DEF","OBJ-9702-9.2-02","DEF",["AO1"],"State",1,2,"Remember",
 ["CLM-9702-9-012"],
 "State the equation linking potential difference, energy transferred and charge, giving the unit of each symbol.",
 "V = W/Q. The potential difference V is in volts, the energy W transferred from electrical form is in joules and the charge Q is in coulombs; one volt is one joule per coulomb.",
 ["1 mark: the equation V = W/Q with the meaning and unit of each symbol - volts, joules, coulombs."]))

items.append(flash(
 "ITEM-9702-9-016-CALC","OBJ-9702-9.2-02","CALC",["AO2"],"Calculate",2,2,"Apply",
 ["CLM-9702-9-012"],
 "A booster pump for a hostel garden in Outjo converts 7.2 × 10⁴ J of electrical energy while a charge of 3.0 × 10² C passes through it. Calculate the potential difference across the pump.",
 "V = W/Q. Substitute with the powers of ten: 7.2 ÷ 3.0 = 2.4, and 10⁴ ÷ 10² = 10², so V = 2.4 × 10² V = 240 V. The potential difference across the pump is 240 V.",
 ["Equation and substitution: V = W/Q with the working 7.2 ÷ 3.0 = 2.4 and the powers of ten combined - 1 mark.",
  "Final answer: 240 V with the unit - 1 mark."]))

items.append(flash(
 "ITEM-9702-9-017-CALC","OBJ-9702-9.2-02","CALC",["AO2"],"Calculate",2,2,"Apply",
 ["CLM-9702-9-012","CLM-9702-9-013"],
 "A doorbell at a clinic in Karibib operates at a potential difference of 8.0 V, and 4.5 C of charge passes through it each time it rings. Calculate the energy converted from electrical form per ring.",
 "W = VQ. Substitute: W = 8.0 × 4.5 = 36 J. The energy converted per ring is 36 J.",
 ["Equation and substitution: W = VQ with the working 8.0 × 4.5 = 36 - 1 mark.",
  "Final answer: 36 J with the unit - 1 mark."]))

items.append(flash(
 "ITEM-9702-9-018-CALC","OBJ-9702-9.2-02","CALC",["AO2"],"Calculate",2,2,"Apply",
 ["CLM-9702-9-012","CLM-9702-9-013","CLM-9702-9-006"],
 "A camping fridge at a site by the Hardap Dam runs at 12 V and draws a current of 2.5 A for 4.0 minutes. Calculate the charge that passes and the energy it converts in that time.",
 "Charge first: t = 4.0 minutes is 240 s, and Q = It = 2.5 × 240 = 600 C. Then energy: W = VQ = 12 × 600 = 7200 J. The charge is 600 C and the energy converted is 7200 J, which is 7.2 × 10³ J to two significant figures.",
 ["Equation and substitution: Q = It with the time converted, giving 600 C - 1 mark, used with W = VQ and the working 12 × 600 = 7200.",
  "Final answer: 7.2 × 10³ J with the unit and two significant figures - 1 mark."]))

items.append(flash(
 "ITEM-9702-9-059-FEATURE","OBJ-9702-9.2-02","FEATURE",["AO1"],"State",1,3,"Remember",
 ["CLM-9702-9-012"],
 "State one feature of the volt.",
 "One volt is one joule per coulomb: a component with a p.d. of one volt across it converts one joule of electrical energy per coulomb passing through it.",
 ["1 mark: one correct feature, such as the definition of the volt as a joule per coulomb, with the equation V = W/Q behind it."]))

items.append(flash(
 "ITEM-9702-9-073-DIST","OBJ-9702-9.2-02","DIST",["AO1"],"State",1,3,"Understand",
 ["CLM-9702-9-012","CLM-9702-9-013"],
 "State the difference between W = VQ and W = VIt as routes to the energy converted in a component.",
 "W = VQ needs the charge that passed; W = VIt needs the current and the time, and uses Q = It to supply the same charge. They give the same energy, so the difference is only in what data the question hands over.",
 ["1 mark: the difference - one is entered with a charge, whereas the other is entered with a current and a time, both valid because Q = It links the inputs."]))

# ================= 9.2-03 power =================
items.append(flash(
 "ITEM-9702-9-019-DEF","OBJ-9702-9.2-03","DEF",["AO1"],"State",1,2,"Remember",
 ["CLM-9702-9-014","CLM-9702-9-015"],
 "State three equations for the electrical power converted in a component of resistance R, giving the unit of each quantity.",
 "P = VI, P = I²R and P = V²/R. The power P is in watts, the potential difference V in volts, the current I in amperes and the resistance R in ohms.",
 ["1 mark: all three equations stated with the unit of each symbol - watts, volts, amperes, ohms; two of the three named is not the full definition set."]))

items.append(flash(
 "ITEM-9702-9-020-CALC","OBJ-9702-9.2-03","CALC",["AO2"],"Calculate",2,2,"Apply",
 ["CLM-9702-9-014"],
 "A strip light in a shop in Gobabis works at a potential difference of 230 V and carries a current of 0.35 A. Calculate the power it converts.",
 "P = VI. Substitute: P = 230 × 0.35 = 80.5 W. The power converted is 80.5 W, which is 81 W to two significant figures.",
 ["Equation and substitution: P = VI with the working 230 × 0.35 = 80.5 - 1 mark.",
  "Final answer: 81 W to two significant figures, with the unit - 1 mark."]))

items.append(flash(
 "ITEM-9702-9-021-CALC","OBJ-9702-9.2-03","CALC",["AO2"],"Calculate",2,2,"Apply",
 ["CLM-9702-9-015"],
 "The heating element of a kettle at a guest house in Swakopmund has a resistance of 25 Ω and carries a current of 9.2 A. Calculate the power it converts, using P = I²R.",
 "P = I²R. First the square: 9.2 × 9.2 = 84.64. Substitute: P = 84.64 × 25 = 2116 W. The power converted is 2116 W, which is 2100 W to two significant figures.",
 ["Equation and substitution: P = I²R with the working 84.64 × 25 = 2116 - 1 mark.",
  "Final answer: 2100 W to two significant figures, with the unit - 1 mark. Using 9.2 × 25 without squaring gives 230 W."]))

items.append(flash(
 "ITEM-9702-9-022-CALC","OBJ-9702-9.2-03","CALC",["AO2"],"Calculate",2,2,"Apply",
 ["CLM-9702-9-015"],
 "An oven element of resistance 26 Ω is connected to a supply that keeps 230 V across it. Calculate the power it converts, using P = V²/R.",
 "P = V²/R. First the square: 230 × 230 = 52900. Substitute: P = 52900 ÷ 26 = 2035 W. The power converted is 2035 W, which is 2000 W to two significant figures.",
 ["Equation and substitution: P = V²/R with the working 52900 ÷ 26 = 2035 - 1 mark.",
  "Final answer: 2000 W to two significant figures, with the unit - 1 mark."]))

items.append(flash(
 "ITEM-9702-9-051-MISCON","OBJ-9702-9.2-03","MISCON",["AO1"],"Explain",1,3,"Understand",
 ["CLM-9702-9-016"],
 "Two heater elements, one of 10 Ω and one of 30 Ω, are connected one at a time across the same 230 V supply. A learner uses P = I²R to conclude that the 30 Ω element converts more power. Explain the error and give the test for choosing the power equation.",
 "The error is applying P = I²R where the current is not shared: connected across the same supply, the two elements carry different currents, so comparing R through I²R goes wrong. When the potential difference is the same, use P = V²/R: the 30 Ω element converts less power, because the same 230 V drives a smaller current through the larger resistance. The test: which quantity is the same for both components? Use the form containing it.",
 ["1 mark: the error named - P = I²R used when the currents differ - and in fact the correct choice stated: the form of the power equation whose other quantity is shared, V²/R here."],
 misc={"mc":"MC-9702-9-06"}))

items.append(flash(
 "ITEM-9702-9-060-FEATURE","OBJ-9702-9.2-03","FEATURE",["AO1"],"State",1,3,"Remember",
 ["CLM-9702-9-015"],
 "State one feature shared by the three power equations P = VI, P = I²R and P = V²/R.",
 "All three describe the same component and give the same power, in watts; each is obtained from another by substituting V = IR, so they are one relationship in three forms.",
 ["1 mark: one correct feature, such as their equivalence through V = IR, or that each gives power in watts for the same component."]))

items.append(flash(
 "ITEM-9702-9-074-DIST","OBJ-9702-9.2-03","DIST",["AO1"],"State",1,3,"Understand",
 ["CLM-9702-9-014"],
 "State the difference between the energy a lamp converts in one minute and its power.",
 "Energy is a total, in joules, for the whole minute; power is the rate of converting it, in watts, which are joules per second. They are linked by W = Pt.",
 ["1 mark: the difference - a total in joules whereas a rate in watts - with W = Pt naming the link."]))

# ================= 9.3-01 define resistance =================
items.append(flash(
 "ITEM-9702-9-023-DEF","OBJ-9702-9.3-01","DEF",["AO1"],"Define",1,1,"Remember",
 ["CLM-9702-9-017","CLM-9702-9-018"],
 "Define resistance.",
 "The resistance of a component is the ratio of the potential difference across it to the current in it, R = V/I. Its unit is the ohm, which is one volt per ampere.",
 ["1 mark: the definition as the ratio V/I, with the unit or the equation completing the meaning; 'opposition to current' is a description, not the definition."]))

items.append(flash(
 "ITEM-9702-9-024-CALC","OBJ-9702-9.3-01","CALC",["AO2"],"Calculate",2,1,"Apply",
 ["CLM-9702-9-017"],
 "A radio at a caravan in Khorixas draws a current of 0.060 A from a battery that keeps a potential difference of 9.0 V across it. Calculate the resistance of the radio.",
 "R = V/I. Substitute: R = 9.0 ÷ 0.060 = 150 Ω. The resistance is 150 Ω.",
 ["Equation and substitution: R = V/I with the working 9.0 ÷ 0.060 = 150 - 1 mark.",
  "Final answer: 150 Ω with the unit - 1 mark."]))

items.append(flash(
 "ITEM-9702-9-047-MISCON","OBJ-9702-9.3-01","MISCON",["AO1"],"Explain",1,2,"Understand",
 ["CLM-9702-9-017","CLM-9702-9-018"],
 "Asked to state the unit in which resistance is measured, a learner writes 'resistance is how much the component opposes the current'. Explain the confusion and give both the definition asked for and the definition of the unit.",
 "The learner has answered a different question: 'opposition to current' describes resistance in words but gives neither the unit nor a testable ratio. Resistance is defined as R = V/I. The unit is the ohm: the resistance of a component in which a p.d. of one volt drives a current of one ampere, so one ohm is one volt per ampere. The test: is the question asking for the quantity or for its unit?",
 ["1 mark: the confusion named - a verbal description offered instead of the unit - and in fact both given: the ratio R = V/I and the ohm as one volt per ampere."],
 misc={"mc":"MC-9702-9-02"}))

items.append(flash(
 "ITEM-9702-9-066-FEATURE","OBJ-9702-9.3-01","FEATURE",["AO1"],"State",1,2,"Remember",
 ["CLM-9702-9-018"],
 "State one feature of the ohm.",
 "One ohm is the resistance of a component in which a potential difference of one volt drives a current of one ampere; it is equal to one volt per ampere.",
 ["1 mark: one correct feature, such as the definition of the ohm through one volt and one ampere, or its value in volts per ampere."]))

# ================= 9.3-02 V = IR =================
items.append(flash(
 "ITEM-9702-9-025-DEF","OBJ-9702-9.3-02","DEF",["AO1"],"State",1,2,"Remember",
 ["CLM-9702-9-019"],
 "State the equation linking potential difference, current and resistance, giving the unit of each symbol.",
 "V = IR. The potential difference V is in volts, the current I is in amperes and the resistance R is in ohms.",
 ["1 mark: the equation V = IR with the meaning and unit of every symbol."]))

items.append(flash(
 "ITEM-9702-9-026-CALC","OBJ-9702-9.3-02","CALC",["AO2"],"Calculate",2,2,"Apply",
 ["CLM-9702-9-019"],
 "A relay coil in the control box of a borehole pump near Grootfontein has a resistance of 47 Ω and carries a current of 0.12 A. Calculate the potential difference across the coil.",
 "V = IR. Substitute: V = 47 × 0.12 = 5.64 V. The potential difference across the coil is 5.64 V, which is 5.6 V to two significant figures.",
 ["Equation and substitution: V = IR with the working 47 × 0.12 = 5.64 - 1 mark.",
  "Final answer: 5.6 V to two significant figures, with the unit - 1 mark."]))

items.append(flash(
 "ITEM-9702-9-027-CALC","OBJ-9702-9.3-02","CALC",["AO2"],"Calculate",2,2,"Apply",
 ["CLM-9702-9-019"],
 "A 6.0 V battery drives a current through a resistor of resistance 33 Ω in a hand-crank radio. Calculate the current in the resistor.",
 "Rearranged, I = V/R. Substitute: I = 6.0 ÷ 33 = 0.1818 A. The current is 0.1818 A, which is 0.18 A to two significant figures.",
 ["Equation and substitution: I = V/R with the working 6.0 ÷ 33 = 0.1818 - 1 mark.",
  "Final answer: 0.18 A to two significant figures, with the unit - 1 mark. Multiplying instead of dividing gives 198, a current far beyond the battery."]))

items.append(flash(
 "ITEM-9702-9-028-CALC","OBJ-9702-9.3-02","CALC",["AO2"],"Calculate",2,2,"Apply",
 ["CLM-9702-9-019"],
 "A headlamp in a minibus taxi on the B1 carries a current of 2.6 A when the potential difference across it is 10.4 V. Calculate the resistance of the headlamp filament at this operating point.",
 "R = V/I. Substitute: R = 10.4 ÷ 2.6 = 4.0 Ω. The resistance at this operating point is 4.0 Ω, to two significant figures.",
 ["Equation and substitution: R = V/I with the working 10.4 ÷ 2.6 = 4.0 - 1 mark.",
  "Final answer: 4.0 Ω with the unit and two significant figures - 1 mark; the resistance stated is the value at that current, since a filament's resistance changes with temperature."]))

items.append(flash(
 "ITEM-9702-9-061-FEATURE","OBJ-9702-9.3-02","FEATURE",["AO1"],"State",1,3,"Remember",
 ["CLM-9702-9-019"],
 "State one feature of V = IR when it is applied to a component whose resistance changes with temperature.",
 "The equation still holds at every instant: the ratio of the p.d. to the current at that instant is the resistance at that instant. It does not say the current is proportional to the p.d. unless the resistance is constant.",
 ["1 mark: one correct feature, such as its validity at each instant, or the point that proportionality needs a constant resistance."]))

items.append(flash(
 "ITEM-9702-9-075-DIST","OBJ-9702-9.3-02","DIST",["AO1"],"State",1,3,"Understand",
 ["CLM-9702-9-020"],
 "On an I–V graph, a student marks a point where the readings are 0.80 V and 0.040 A, and says the resistance there is the gradient of the graph. State the difference between the resistance at that point and the gradient of the I–V graph.",
 "The resistance at the point is the ratio of the coordinates, V/I = 0.80 ÷ 0.040 = 20 Ω. The gradient of an I–V graph is the change in current divided by the change in p.d., a different quantity; the two agree as numbers for the resistance ratio only when the graph is a straight line through the origin.",
 ["1 mark: the difference - a ratio of the two readings at the point, 20 Ω, whereas the gradient is a slope between two points - so the two are not the same quantity except on a line through the origin."]))

# ================= 9.3-03 I–V characteristics =================
items.append(flash(
 "ITEM-9702-9-029-INTERP","OBJ-9702-9.3-03","INTERP",["AO2"],"Determine",2,3,"Analyse",
 ["CLM-9702-9-020","CLM-9702-9-021","CLM-9702-9-026"],
 "The I–V characteristic of a component is a straight line through the origin. A reading taken from the graph gives a current of 0.15 A at a potential difference of 4.5 V. Determine the resistance of the component, and state what the shape of the graph shows about it.",
 "The resistance is the ratio of the coordinates at the point: R = V/I = 4.5 ÷ 0.15 = 30 Ω. The straight line through the origin means the graph shows a constant resistance: the ratio V/I is the same at every point, so the component is ohmic at that temperature.",
 ["1 mark: the resistance read from the graph as the ratio of the values, R = 4.5 ÷ 0.15 = 30 Ω - the reading, not the gradient, gives it.",
  "1 mark: what the trace shows - a straight line through the origin represents a constant resistance, so the same 30 Ω holds at every point on it."]))

items.append(flash(
 "ITEM-9702-9-030-INTERP","OBJ-9702-9.3-03","INTERP",["AO2"],"Determine",2,3,"Analyse",
 ["CLM-9702-9-020","CLM-9702-9-023"],
 "Readings for a semiconductor diode in the forward direction are given in the table. Determine the potential difference at which the current starts to rise steeply, and determine the resistance of the diode at the largest reading.\n\n| Potential difference / V | 0.3 | 0.5 | 0.7 | 0.9 |\n| Current / mA | 0.4 | 1.2 | 18 | 62 |",
 "The table values show the current near zero up to 0.5 V, then rising steeply: the steep rise begins at about 0.7 V. At the largest reading the resistance is the ratio of the coordinates: R = V/I = 0.9 ÷ 0.062 = 14.5 Ω. The diode's resistance falls as the forward p.d. rises past the threshold, which the table readings show directly.",
 ["1 mark: the threshold read from the table as about 0.7 V, using the jump in the current values between 0.5 V and 0.7 V.",
  "1 mark: the resistance at 0.9 V as the ratio of the readings, 0.9 ÷ 0.062 = 14.5 Ω - the graph and table mean a ratio of coordinates, so the reading gives the resistance at that point."]))

items.append(flash(
 "ITEM-9702-9-031-CALC","OBJ-9702-9.3-03","CALC",["AO2"],"Determine",2,3,"Apply",
 ["CLM-9702-9-021","CLM-9702-9-026"],
 "The I–V graph of a metallic conductor held at constant temperature is a straight line through the origin that passes through the point where the p.d. is 5.0 V and the current is 0.20 A. Determine the resistance of the conductor, and determine the current at a potential difference of 7.5 V.",
 "The resistance is the ratio at the given point: R = V/I = 5.0 ÷ 0.20 = 25 Ω. Because the line is straight through the origin, the resistance is constant, so at 7.5 V the current is I = V/R = 7.5 ÷ 25 = 0.30 A.",
 ["Equation and substitution: R = V/I with the working 5.0 ÷ 0.20 = 25, then I = V/R with the working 7.5 ÷ 25 = 0.30 - 1 mark.",
  "Final answer: 25 Ω and 0.30 A, each with its unit - 1 mark. The constant resistance follows from the line passing through the origin."]))

items.append(flash(
 "ITEM-9702-9-032-APP","OBJ-9702-9.3-03","APP",["AO2"],"Explain",1,3,"Apply",
 ["CLM-9702-9-020","CLM-9702-9-022"],
 "A component in a school laboratory gives an I–V graph that curves over: its gradient decreases as the potential difference increases. Explain what this graph shows about the resistance of the component as the current increases.",
 "In this case the resistance rises as the current increases: since resistance at a point is the ratio V/I of the coordinates, and the curve's current grows less than in proportion to the p.d., the ratio grows along the graph. This is the characteristic of a filament lamp, whose temperature rises with the current.",
 ["1 mark: the explanation for this case - the resistance increases with current, because the ratio V/I grows along the curve; so the component behaves like a filament lamp, heating as the current rises."]))

items.append(flash(
 "ITEM-9702-9-048-MISCON","OBJ-9702-9.3-03","MISCON",["AO1"],"Explain",1,4,"Understand",
 ["CLM-9702-9-020"],
 "A learner studies an I–V graph that is a straight line cutting the current axis at 0.2 A, well above the origin, and concludes that the component has a constant resistance because the line is straight. Explain the error and give the test that separates a constant resistance from a merely straight line.",
 "The error is taking the gradient for the resistance. Resistance at a point is the ratio V/I of the coordinates there, not the gradient of the line. Because the line does not pass through the origin, V/I changes along it, so the resistance is not constant however straight the line is. The test: does the straight line pass through the origin? Only then is V/I the same at every point.",
 ["1 mark: the error named - straightness confused with constant resistance - and in fact the correct test given: the ratio V/I is the resistance at a point, and only a line through the origin gives the same ratio everywhere."],
 misc={"mc":"MC-9702-9-03"}))

items.append(flash(
 "ITEM-9702-9-053-FEATURE","OBJ-9702-9.3-03","FEATURE",["AO1"],"State",1,4,"Remember",
 ["CLM-9702-9-023"],
 "State one feature of the I–V characteristic of a semiconductor diode.",
 "The current stays very small until the forward potential difference reaches about 0.7 V, and above that threshold it rises steeply; in the reverse direction the current is very small at any potential difference, so the diode conducts in one direction only.",
 ["1 mark: one correct feature, such as the 0.7 V forward threshold, the steep rise above it, or the very small reverse current."]))

items.append(flash(
 "ITEM-9702-9-067-DIST","OBJ-9702-9.3-03","DIST",["AO1"],"State",1,4,"Understand",
 ["CLM-9702-9-021","CLM-9702-9-022"],
 "State the difference between the I–V characteristic of a metallic conductor at constant temperature and that of a filament lamp.",
 "The metallic conductor at constant temperature gives a straight line through the origin: current proportional to p.d., constant resistance. The filament lamp gives a curve whose gradient decreases as the p.d. rises, because its temperature increases with the current, so its resistance rises.",
 ["1 mark: the difference - a straight line through the origin, whereas a curve that flattens, with the reason in the lamp's rising temperature."]))

# ================= 9.3-04 filament lamp resistance =================
items.append(flash(
 "ITEM-9702-9-033-DEF","OBJ-9702-9.3-04","DEF",["AO1"],"State",1,3,"Remember",
 ["CLM-9702-9-024"],
 "State how the resistance of a filament lamp changes as the current in it increases, and the reason.",
 "The resistance increases as the current increases, because the larger current raises the temperature of the filament.",
 ["1 mark: the definition of the change with its cause - resistance increases, because the filament's temperature rises with the current."]))

items.append(flash(
 "ITEM-9702-9-034-MECH","OBJ-9702-9.3-04","MECH",["AO2"],"Explain",2,3,"Understand",
 ["CLM-9702-9-024"],
 "Explain, in terms of the lattice of the metal, how an increase in current raises the resistance of a filament lamp.",
 "A larger current converts more power in the filament, so its temperature rises. At the higher temperature the lattice ions vibrate with greater amplitude, and the conduction electrons collide with them more often, so a larger potential difference is needed to drive each ampere: the resistance, the ratio V/I, has increased.",
 ["1 mark: the chain to the lattice - the temperature rises, which causes the lattice ions to vibrate with greater amplitude.",
  "1 mark: how that raises resistance - the conduction electrons collide with the ions more often, so the ratio V/I increases."]))

items.append(flash(
 "ITEM-9702-9-035-APP","OBJ-9702-9.3-04","APP",["AO2"],"Explain",1,3,"Apply",
 ["CLM-9702-9-024","CLM-9702-9-019"],
 "A continuity meter passes a tiny current through a car headlamp and reads 1.5 Ω. The headlamp is rated 12 V, 36 W. In this situation the operating resistance differs from the meter reading. Explain why.",
 "At its rating the lamp's resistance is R = V²/P = 144 ÷ 36 = 4.0 Ω, nearly three times the meter's 1.5 Ω. The meter's current is far too small to warm the filament, so it measures the cold resistance; at the operating current the filament runs hot, and its resistance is higher because the hotter lattice obstructs the conduction electrons more.",
 ["1 mark: the explanation for this case - the meter reads the cold filament, whereas at 12 V the lamp runs hot, so the resistance is 4.0 Ω instead of 1.5 Ω; the difference exists because the operating current raises the filament's temperature."]))

items.append(flash(
 "ITEM-9702-9-054-FEATURE","OBJ-9702-9.3-04","FEATURE",["AO1"],"State",1,4,"Remember",
 ["CLM-9702-9-022"],
 "State one feature of the I–V characteristic of a filament lamp.",
 "The graph curves over as the potential difference increases: its gradient decreases at larger currents, because the lamp's temperature and resistance rise with the current. The curve has the same shape in both directions.",
 ["1 mark: one correct feature, such as the decreasing gradient at large p.d., or the same shape both ways round."]))

items.append(flash(
 "ITEM-9702-9-068-DIST","OBJ-9702-9.3-04","DIST",["AO1"],"State",1,4,"Understand",
 ["CLM-9702-9-024"],
 "State the difference between the resistance of a filament lamp at a very small current and its resistance at its rated current.",
 "At a very small current the filament stays near room temperature and the resistance is small and steady. At the rated current the filament runs at its working temperature, and the resistance is several times larger because the current itself has heated the filament.",
 ["1 mark: the distinction - cold and small, whereas hot and larger at the rated current - with the cause being the temperature the operating current produces."]))

# ================= 9.3-05 Ohm's law =================
items.append(flash(
 "ITEM-9702-9-036-DEF","OBJ-9702-9.3-05","DEF",["AO1"],"State",1,2,"Remember",
 ["CLM-9702-9-025"],
 "State Ohm's law.",
 "The current through a conductor is proportional to the potential difference across it, provided the temperature and other physical conditions stay constant.",
 ["1 mark: the law stated with its condition - proportionality of current to p.d., provided the temperature and other physical conditions are constant."]))

items.append(flash(
 "ITEM-9702-9-037-FEATURE","OBJ-9702-9.3-05","FEATURE",["AO1"],"State",1,2,"Remember",
 ["CLM-9702-9-025","CLM-9702-9-026"],
 "State one feature of a conductor that obeys Ohm's law.",
 "Its resistance is constant at that temperature, and its I–V graph is a straight line through the origin: the ratio V/I is the same at every point.",
 ["1 mark: one correct feature, such as the constant resistance or the straight-line graph through the origin."]))

items.append(flash(
 "ITEM-9702-9-076-DIST","OBJ-9702-9.3-05","DIST",["AO1"],"State",1,3,"Understand",
 ["CLM-9702-9-026"],
 "State the difference between a component that obeys Ohm's law over a range of potential difference and one that does not.",
 "The ohmic component keeps a constant resistance over the range, so doubling the p.d. doubles the current and its I–V graph is a straight line through the origin. The non-ohmic component's resistance changes with the current, as a filament lamp's does when it warms, so its graph curves.",
 ["1 mark: the difference - constant resistance with current proportional to p.d., whereas a resistance that changes with current gives a curved characteristic."]))

# ================= 9.3-06 R = rho L / A =================
items.append(flash(
 "ITEM-9702-9-038-DEF","OBJ-9702-9.3-06","DEF",["AO1"],"State",1,2,"Remember",
 ["CLM-9702-9-027"],
 "State the equation for the resistance of a uniform wire, defining each symbol and its unit.",
 "R = ρL/A. The resistance R is in ohms; ρ is the resistivity of the material in Ω m; L is the length of the wire in m; A is the cross-sectional area in m².",
 ["1 mark: the equation R = ρL/A with every symbol defined and its unit given - resistivity in Ω m, length in m, area in m²."]))

items.append(flash(
 "ITEM-9702-9-039-CALC","OBJ-9702-9.3-06","CALC",["AO2"],"Calculate",2,2,"Apply",
 ["CLM-9702-9-027"],
 "A sensor cable to a weather station on the Gamsberg is 35 m long and has a cross-sectional area of 1.0 mm². The resistivity of its copper is 1.7 × 10⁻⁸ Ω m. Calculate the resistance of the cable.",
 "Convert the area: 1.0 mm² is 1.0 × 10⁻⁶ m². Then R = ρL/A = (1.7 × 10⁻⁸ × 35) ÷ (1.0 × 10⁻⁶). The top line is 1.7 × 35 = 59.5, so 59.5 × 10⁻⁸, and dividing by 1.0 × 10⁻⁶ gives R = 0.595 Ω. The resistance is 0.595 Ω, which is 0.60 Ω to two significant figures.",
 ["Equation and substitution: R = ρL/A with the area converted and the top line 1.7 × 35 = 59.5 - 1 mark.",
  "Final answer: 0.60 Ω to two significant figures, with the unit - 1 mark."]))

items.append(flash(
 "ITEM-9702-9-040-CALC","OBJ-9702-9.3-06","CALC",["AO2"],"Calculate",2,2,"Apply",
 ["CLM-9702-9-027","CLM-9702-9-029"],
 "A heating element wire is 2.0 m long with a cross-sectional area of 8.0 × 10⁻⁷ m², and its resistance is measured as 11 Ω. Calculate the resistivity of the metal.",
 "Rearranged, ρ = RA/L. Substitute: ρ = (11 × 8.0 × 10⁻⁷) ÷ 2.0. The top line is 8.0 × 11 = 88, so 88 × 10⁻⁷, and 88 ÷ 2.0 = 44, so ρ = 44 × 10⁻⁷ Ω m. The resistivity is 4.4 × 10⁻⁶ Ω m to two significant figures.",
 ["Equation and substitution: ρ = RA/L with the working 8.0 × 11 = 88 and 88 ÷ 2.0 = 44 - 1 mark.",
  "Final answer: 4.4 × 10⁻⁶ Ω m with the unit and two significant figures - 1 mark. This is the resistivity of the material alone, whatever the wire's shape."]))

items.append(flash(
 "ITEM-9702-9-041-CALC","OBJ-9702-9.3-06","CALC",["AO2"],"Calculate",2,2,"Apply",
 ["CLM-9702-9-027"],
 "A sensor lead must have a resistance no greater than 0.90 Ω over its length of 4.0 m. The wire metal has a resistivity of 5.5 × 10⁻⁸ Ω m. Calculate the smallest cross-sectional area the lead can have.",
 "Rearranged, A = ρL/R. Substitute: A = (5.5 × 10⁻⁸ × 4.0) ÷ 0.90. The top line is 5.5 × 4.0 = 22, so 22 × 10⁻⁸, and 22 ÷ 0.90 = 24.4, so A = 24.4 × 10⁻⁸ m². The smallest area is 2.44 × 10⁻⁷ m², which is 2.4 × 10⁻⁷ m² to two significant figures.",
 ["Equation and substitution: A = ρL/R with the working 5.5 × 4.0 = 22 and 22 ÷ 0.90 = 24.4 - 1 mark.",
  "Final answer: 2.4 × 10⁻⁷ m² with the unit and two significant figures - 1 mark."]))

items.append(flash(
 "ITEM-9702-9-062-FEATURE","OBJ-9702-9.3-06","FEATURE",["AO1"],"State",1,3,"Remember",
 ["CLM-9702-9-029"],
 "State one feature of the resistivity of a material.",
 "Resistivity is a property of the material alone, in Ω m: wires of the same metal with different lengths and cross-sections have different resistances but share one resistivity.",
 ["1 mark: one correct feature, such as belonging to the material rather than the sample, or its unit Ω m."]))

items.append(flash(
 "ITEM-9702-9-077-DIST","OBJ-9702-9.3-06","DIST",["AO1"],"State",1,3,"Understand",
 ["CLM-9702-9-027","CLM-9702-9-029"],
 "State the difference between the resistance of a wire and the resistivity of its material.",
 "Resistance, in Ω, belongs to the particular wire and depends on its length and cross-sectional area as well as its material. Resistivity, in Ω m, belongs to the material alone. R = ρL/A links them.",
 ["1 mark: the difference - a property of the sample in Ω, whereas a property of the material in Ω m - with R = ρL/A naming the link."]))

# ================= 9.3-07 LDR =================
items.append(flash(
 "ITEM-9702-9-042-DEF","OBJ-9702-9.3-07","DEF",["AO1"],"State",1,2,"Remember",
 ["CLM-9702-9-030"],
 "State how the resistance of a light-dependent resistor changes as the light intensity on it increases, and the physical reason.",
 "The resistance decreases as the light intensity increases, because brighter light releases more charge carriers in the semiconductor, so a larger current flows for the same potential difference.",
 ["1 mark: the direction of the change with its meaning and cause - resistance decreases with increasing light intensity, because more charge carriers are released."]))

items.append(flash(
 "ITEM-9702-9-043-MECH","OBJ-9702-9.3-07","MECH",["AO2"],"Explain",2,2,"Understand",
 ["CLM-9702-9-030"],
 "A security lamp at a lodge near the Etosha gate uses a light-dependent resistor to sense darkness. Explain how the fall in light intensity at dusk changes the LDR's resistance, and how that change comes about in the semiconductor.",
 "As the light intensity falls, fewer charge carriers are released in the semiconductor, so the resistance of the LDR increases. Because the resistance is larger, the same potential difference drives a smaller current through the sensing circuit, and the circuit reads the change and switches the lamp on.",
 ["1 mark: how dusk acts - less light releases fewer charge carriers, which causes the resistance to rise.",
  "1 mark: the consequence in the circuit - the smaller current at the same p.d. is what the switching circuit detects."]))

items.append(flash(
 "ITEM-9702-9-052-MISCON","OBJ-9702-9.3-07","MISCON",["AO1"],"Explain",1,3,"Understand",
 ["CLM-9702-9-030","CLM-9702-9-032"],
 "A learner says that as the light gets brighter, an LDR's resistance rises, because 'more energy must be resisted'. Explain the error and give the test that fixes the direction of the change.",
 "The error is the direction: the resistance of an LDR decreases as the light intensity increases. Brighter light releases more charge carriers in the semiconductor, so more current flows for the same p.d., which is what a smaller resistance means. The test: more light gives more or fewer charge carriers? More carriers, so the resistance falls.",
 ["1 mark: the error named - direction reversed - and in fact the correct mechanism: more light releases more carriers, so the resistance decreases instead of rising."],
 misc={"mc":"MC-9702-9-07"}))

items.append(flash(
 "ITEM-9702-9-063-FEATURE","OBJ-9702-9.3-07","FEATURE",["AO1"],"State",1,3,"Remember",
 ["CLM-9702-9-030"],
 "State one feature of a light-dependent resistor.",
 "It is a semiconductor component whose resistance is large in the dark and small in bright light, because the light itself releases the charge carriers that carry its current.",
 ["1 mark: one correct feature, such as the large dark resistance and small bright-light resistance, or the release of carriers by light."]))

items.append(flash(
 "ITEM-9702-9-078-DIST","OBJ-9702-9.3-07","DIST",["AO1"],"State",1,3,"Understand",
 ["CLM-9702-9-032"],
 "State the difference between a light-dependent resistor and a thermistor in what each responds to.",
 "The LDR responds to light intensity: its resistance decreases as the light on it increases. The thermistor responds to temperature: its resistance decreases as its temperature increases. Both work by the release of extra charge carriers in a semiconductor.",
 ["1 mark: the difference - light intensity, whereas temperature - with both resistances falling as the carrier number rises."]))

# ================= 9.3-08 thermistor =================
items.append(flash(
 "ITEM-9702-9-044-DEF","OBJ-9702-9.3-08","DEF",["AO1"],"State",1,2,"Remember",
 ["CLM-9702-9-031"],
 "State how the resistance of a thermistor changes as its temperature increases, and the physical reason.",
 "The resistance decreases as the temperature increases, because the higher temperature releases more charge carriers in the semiconductor.",
 ["1 mark: the direction of the change with its meaning and cause - resistance decreases with increasing temperature, because more charge carriers are released."]))

items.append(flash(
 "ITEM-9702-9-045-MECH","OBJ-9702-9.3-08","MECH",["AO2"],"Explain",2,2,"Understand",
 ["CLM-9702-9-031","CLM-9702-9-033"],
 "The coolant sensor of a minibus taxi engine is a thermistor. Explain how a rise in coolant temperature changes the sensor's resistance, and why the direction of the change differs from that in the metal wires nearby.",
 "The higher temperature releases more charge carriers in the thermistor's semiconductor, so its resistance decreases. In the metal wires the number of carriers is fixed and the hotter lattice obstructs them more, so a metal's resistance increases with temperature; the thermistor's carrier number grows fast enough to win the other way.",
 ["1 mark: how the sensor responds - more carriers released at the higher temperature, which causes its resistance to fall.",
  "1 mark: why the metal differs - fixed carrier number and a hotter lattice, so the metal's resistance rises instead."]))

items.append(flash(
 "ITEM-9702-9-064-FEATURE","OBJ-9702-9.3-08","FEATURE",["AO1"],"State",1,3,"Remember",
 ["CLM-9702-9-031"],
 "State one feature of a thermistor as used at AS level.",
 "It is a semiconductor component whose resistance decreases as its temperature increases, which makes it useful as a temperature sensor.",
 ["1 mark: one correct feature, such as the falling resistance with rising temperature, or its use in temperature sensing."]))

items.append(flash(
 "ITEM-9702-9-079-DIST","OBJ-9702-9.3-08","DIST",["AO1"],"State",1,3,"Understand",
 ["CLM-9702-9-033"],
 "State the difference between the way the resistance of a metal wire changes as its temperature rises and the way a thermistor's changes.",
 "The metal's resistance increases with temperature, because its carrier number is fixed and its hotter lattice obstructs the carriers more. The thermistor's resistance decreases with temperature, because the higher temperature releases more charge carriers, and their number grows faster than the obstruction.",
 ["1 mark: the difference - a metal rises, whereas a thermistor falls - each with its physical reason."]))

print("flashcards built:", len(items))
with open(os.path.join(TD, '_items_part1.json'), 'w') as f:
    json.dump(items, f, indent=1, ensure_ascii=False)
