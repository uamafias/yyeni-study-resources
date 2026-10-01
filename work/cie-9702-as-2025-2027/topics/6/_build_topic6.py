#!/usr/bin/env python3
"""Build topic 6 (Deformation of solids): claim ledger, 2 content units, 61 learning items."""
import json, os, sys, hashlib

WS = '/Users/professor/Documents/YYeni Study Resources/work/cie-9702-as-2025-2027'
STD = '/Users/professor/Documents/YYeni Study Resources/standard/v0.2.0-draft'
TD = os.path.join(WS, 'topics', '6')
sys.path.insert(0, os.path.join(STD, 'checks'))
from yyeni_checks import _artefact_text

def H(x):
    return hashlib.sha256(_artefact_text(x).encode()).hexdigest()

CTX = {"sector": None, "business_size": None, "ownership": None, "situation": None, "facts": []}
PROV = "Authored for CIE 9702 AS Physics topic 6 from the topic claim ledger and work order."

# ---------------------------------------------------------------- claims
def claim(cid, objs, text, ctype):
    return {
        "claim_id": cid, "objective_ids": objs, "text": text, "claim_type": ctype,
        "provenance": "generated_gap", "evidence": [], "derived_from_claim_ids": [],
        "revision": 1,
        "verification": {"status": "unverified",
                          "method": "Authored originally for topic 6 of the 9702 AS workspace under standard v0.2.0-draft. Requires semantic review (RS-28).",
                          "reviewer_id": None, "reviewed_at": None, "confidence": 0.9},
        "publishable": False, "notes": [],
    }

O = {"11": "OBJ-9702-6.1-01", "12": "OBJ-9702-6.1-02", "13": "OBJ-9702-6.1-03",
     "14": "OBJ-9702-6.1-04", "15": "OBJ-9702-6.1-05", "16": "OBJ-9702-6.1-06",
     "21": "OBJ-9702-6.2-01", "22": "OBJ-9702-6.2-02", "23": "OBJ-9702-6.2-03",
     "24": "OBJ-9702-6.2-04"}

CLAIMS = [
 claim("CLM-9702-6-001", [O["11"]],
   "A deformation is a change in the shape or size of an object, produced by a pair of forces acting along a single line; in this topic forces and deformations are assumed to be in one dimension only.",
   "factual"),
 claim("CLM-9702-6-002", [O["11"]],
   "A tensile force pulls the two ends of an object away from each other along that line, making it longer; a compressive force pushes the ends towards each other, making it shorter; both are measured in newtons.",
   "factual"),
 claim("CLM-9702-6-003", [O["12"]],
   "The load on an object is the force applied to it, in N. The extension is the increase in length, stretched length − original length, in m. The compression is the matching decrease from the original length, also in m.",
   "definition"),
 claim("CLM-9702-6-004", [O["12"]],
   "The limit of proportionality is the point beyond which the force is no longer proportional to the extension.",
   "definition"),
 claim("CLM-9702-6-005", [O["12"]],
   "Up to the limit of proportionality a graph of force against extension is a straight line through the origin, and its gradient equals the spring constant; beyond it the line curves away and the gradient falls.",
   "factual"),
 claim("CLM-9702-6-006", [O["13"]],
   "Hooke’s law: the force on an object is proportional to its extension, F = kx, with F in N, x the extension in m and k the spring constant in N m⁻¹, provided the limit of proportionality is not exceeded.",
   "formula"),
 claim("CLM-9702-6-007", [O["13"]],
   "F = kx holds only within the limit of proportionality; beyond it the force is no longer proportional to the extension, so doubling the load no longer doubles the extension and the equation cannot be used.",
   "factual"),
 claim("CLM-9702-6-008", [O["13"], O["12"]],
   "In F = kx the quantity x is the extension — stretched length minus original length — and not the length of the loaded object; the test is whether the original length has been subtracted.",
   "misconception_correction"),
 claim("CLM-9702-6-009", [O["14"]],
   "The spring constant is the force per unit extension, k = F ÷ x, in N m⁻¹; it is the gradient of the force–extension graph within the limit of proportionality, and a stiffer spring has a larger k.",
   "definition"),
 claim("CLM-9702-6-010", [O["14"]],
   "Springs joined end to end each carry the whole load, so their extensions add and the combined spring constant is smaller than one spring’s; springs joined side by side share the load, so their spring constants add.",
   "factual"),
 claim("CLM-9702-6-011", [O["15"]],
   "Tensile stress is the force per unit cross-sectional area, σ = F ÷ A, in Pa (1 Pa = 1 N m⁻²). Tensile strain is the extension divided by the original length, ε = x ÷ L; it is a ratio of two lengths and has no unit.",
   "definition"),
 claim("CLM-9702-6-012", [O["15"]],
   "The Young modulus is the ratio of tensile stress to tensile strain for a material deformed within its limit of proportionality, E = FL ÷ Ax, in Pa; it is a property of the material alone, whereas the spring constant depends on the object’s dimensions.",
   "formula"),
 claim("CLM-9702-6-013", [O["16"]],
   "The Young modulus of a wire is found by clamping a long wire over a pulley, measuring the original length with a metre rule and the diameter at several points with a micrometer, loading in steps to record force and extension, then taking the gradient of the force–extension graph and using E = gradient × L ÷ A.",
   "procedural"),
 claim("CLM-9702-6-014", [O["16"]],
   "A long wire keeps the percentage uncertainty in the extension small, and the diameter is measured at several points and orientations and averaged, because it is squared in the area A = πd² ÷ 4 and its percentage uncertainty is doubled in A.",
   "factual"),
 claim("CLM-9702-6-015", [O["16"]],
   "The cross-sectional area of a wire is A = πd² ÷ 4, with the diameter d in m; 1 mm² = 1 × 10⁻⁶ m², so a wire of area 0.20 mm² has A = 2.0 × 10⁻⁷ m².",
   "factual"),
 claim("CLM-9702-6-016", [O["16"]],
   "The main limitations of the wire experiment are the small extension read against a millimetre rule, which gives a large percentage uncertainty in the gradient and so in E, and kinked wire, where the first loads straighten the kinks and shift every early reading the same way, a systematic error that makes E come out too small.",
   "evaluative"),
 claim("CLM-9702-6-017", [O["15"]],
   "Stress (force per unit area, in Pa), strain (extension ÷ original length, no unit) and elastic potential energy (the energy stored, in J) are three different quantities; the test is whether the quantity has a unit, and which one.",
   "misconception_correction"),
 claim("CLM-9702-6-018", [O["15"]],
   "The length in the denominator of a strain is the original, unstretched length; the test is which length sits on the bottom of the fraction.",
   "misconception_correction"),
 claim("CLM-9702-6-019", [O["21"]],
   "An elastic deformation is a change of shape that disappears when the load is removed; a plastic deformation is a permanent change of shape that stays when the load is removed; the elastic limit is the point beyond which an object will not return to its original shape when the load is removed.",
   "definition"),
 claim("CLM-9702-6-020", [O["21"]],
   "Beyond the elastic limit the deformation is plastic: the wire unloads along a straight line parallel to its initial loading line and reaches zero force at a non-zero extension, the permanent extension.",
   "factual"),
 claim("CLM-9702-6-021", [O["21"], O["12"]],
   "The limit of proportionality marks where the force stops being proportional to the extension and the graph’s straight line ends, whereas the elastic limit marks where the object stops returning to its original shape on unloading; the second lies at or beyond the first.",
   "comparison"),
 claim("CLM-9702-6-022", [O["22"]],
   "A force–extension graph for a ductile metal wire rises as a straight line through the origin to the limit of proportionality, curves through the elastic limit, then shows large extensions for small extra loads until the wire breaks.",
   "factual"),
 claim("CLM-9702-6-023", [O["22"], O["23"]],
   "The area under a force–extension graph represents the work done by the load, because work is force multiplied by the distance moved in the direction of the force.",
   "formula"),
 claim("CLM-9702-6-024", [O["22"], O["23"]],
   "Up to the elastic limit the work done by the load is stored as elastic potential energy and is recovered on unloading; beyond it, part of the work is dissipated in the permanent change of shape, so the stored energy is less than the work done.",
   "factual"),
 claim("CLM-9702-6-025", [O["24"], O["23"]],
   "For a material deformed within its limit of proportionality the elastic potential energy stored is EP = ½Fx = ½kx², with F the force in N, x the extension in m, k the spring constant in N m⁻¹ and the energy in J.",
   "formula"),
 claim("CLM-9702-6-026", [O["24"]],
   "The half in ½Fx appears because the force rises from zero in step with the extension, so the average force during the stretch is half the final force and the work done is the triangular area under the graph.",
   "causal"),
 claim("CLM-9702-6-027", [O["24"]],
   "Doubling the extension within the limit of proportionality multiplies the stored energy by four, because the force doubles as well as the extension; the test is whether the force stays the same as the extension grows.",
   "causal"),
]

# ---------------------------------------------------------------- content units
def blk(bid, btype, heading, text, claim_ids, ao):
    b = {"block_id": bid, "block_type": btype, "heading": heading, "text": text.strip(),
         "claim_ids": claim_ids, "context_tags": [], "assessment_objectives": ao,
         "claims_seen": {c: 1 for c in claim_ids}}
    b["authored_hash"] = H(b)
    return b

U61_BLOCKS = [
 blk("6.1-b1", "learner_objective", "What this section covers",
  """What a deformation is and how tensile and compressive forces cause it along one line; the terms load, extension, compression and limit of proportionality; Hooke’s law and the spring constant; stress, strain and the Young modulus; and an experiment to find the Young modulus of a metal wire.""",
  [], ["AO1"]),
 blk("6.1-b2", "definition", "Tensile and compressive forces",
  """A deformation is a change in the shape or the size of an object, produced by a pair of forces. In this topic every force and every deformation is one-dimensional: the forces act along a single line, the line of the object’s length. A tensile force is a force that pulls the two ends of the object away from each other along that line; the object gets longer, which is why a tow rope on a bakkie stuck in sand is under tension. A compressive force pushes the two ends towards each other; the object gets shorter, as the legs of a table are compressed by the load on the table top. Both kinds of force change the object’s length, and both are measured in newtons. A stretched rubber band and a squeezed sponge differ only in which of the two is acting, so the first question about any deformed object is which kind of force the load applies.""",
  ["CLM-9702-6-001", "CLM-9702-6-002"], ["AO1"]),
 blk("6.1-b3", "definition", "Load, extension and compression",
  """The load on an object is the force applied to it, measured in newtons (N). The extension is the increase in the object’s length: the stretched length minus the original length, in metres (m). The compression is the matching decrease in length: the original length minus the shortened length, also in metres. A spring of original length 0.25 m that stands 0.31 m long under a load has an extension of 0.31 − 0.25 = 0.06 m; the same spring squeezed to 0.22 m has a compression of 0.03 m. Extension and compression are differences from the original length, not whole lengths, and that one habit — subtract the original first — is the step most often skipped in calculations with Hooke’s law.""",
  ["CLM-9702-6-003", "CLM-9702-6-008"], ["AO1"]),
 blk("6.1-b4", "plain_explanation", "The limit of proportionality",
  """Load a spring in steps and plot the force against the extension. Up to a point the graph is a straight line through the origin: the force is proportional to the extension, so doubling the load doubles the extension. The limit of proportionality is the point beyond which the force is no longer proportional to the extension. Beyond it the graph curves away from the straight line: extra load buys less and less extra extension. Within the limit the line’s gradient is constant and equals the spring constant; beyond it the gradient falls. The limit of proportionality is a statement about the shape of the graph, and it is not the same point as the elastic limit, which is about whether the object returns to its original shape when the load is removed — a distinction taken up with elastic and plastic deformation in topic 6.2.""",
  ["CLM-9702-6-004", "CLM-9702-6-005", "CLM-9702-6-021"], ["AO1"]),
 blk("6.1-b5", "formula", "Hooke’s law",
  """Hooke’s law states that the force on an object is proportional to its extension, provided the limit of proportionality is not exceeded. In symbols, F = kx, where F is the force in newtons (N), x is the extension in metres (m) and k is the spring constant of the object, in newtons per metre (N m⁻¹). The equation is a proportionality with a condition: it describes the straight-line part of the force–extension graph only, so any load that has bent the graph cannot be put into F = kx. Because the law links force to extension, x is the increase in length, taken from the original length, and not the stretched length of the object itself.""",
  ["CLM-9702-6-006", "CLM-9702-6-007", "CLM-9702-6-008"], ["AO1"]),
 blk("6.1-b6", "worked_calculation", "Worked example: a scale spring at a garden shop",
  """A spring scale at a garden shop in Etunda has a spring of spring constant 45 N m⁻¹. A bag of fertiliser hangs at rest on the hook, stretching the spring within its limit of proportionality. The scale shows the bag’s weight as 7.2 N, so the force on the spring is 7.2 N. The extension comes from Hooke’s law: x = F ÷ k. Substitution: 7.2 ÷ 45 = 0.16, so the extension is 0.16 m to two significant figures, the precision of the data. If the spring’s original length is 0.120 m, its stretched length is 0.120 m + 0.16 m = 0.28 m — and it is the 0.16 m, the difference, that the law needed.""",
  ["CLM-9702-6-006", "CLM-9702-6-008"], ["AO2"]),
 blk("6.1-b7", "formula", "The spring constant",
  """The spring constant of an object is the force per unit extension, k = F ÷ x, with the force F in newtons and the extension x in metres, so k is measured in N m⁻¹. A stiff spring needs a large force for each metre of stretch, so it has a large spring constant; a soft spring has a small one. On the force–extension graph, within the limit of proportionality, the spring constant is the gradient of the straight line. Joining springs changes the combined constant. Springs joined end to end, in series, each carry the whole load, so each stretches fully and their extensions add: two identical springs in series stretch twice as far as one, and the pair behaves like one spring of half the spring constant. Springs joined side by side, in parallel, share the load between them, so each stretches less and the constants add: two identical springs in parallel behave like one spring of twice the constant. The test for which case you have: does each spring carry the full load?""",
  ["CLM-9702-6-009", "CLM-9702-6-010"], ["AO1"]),
 blk("6.1-b8", "definition", "Stress, strain and the Young modulus",
  """Two wires of the same steel, one thick and one thin, carry very different forces for the same stretch, so force and extension describe the object, not the material. Stress and strain strip the dimensions out. The tensile stress is the force divided by the cross-sectional area: σ = F ÷ A, with F in newtons and A in m², measured in pascals (Pa), where 1 Pa = 1 N m⁻². The tensile strain is the extension divided by the original length: ε = x ÷ L, a ratio of metres to metres, so it has no unit. The Young modulus is the ratio of the stress to the strain for a material deformed within its limit of proportionality: E = (F ÷ A) ÷ (x ÷ L) = FL ÷ Ax, also in pascals. Steel has E of about 2.0 × 10¹¹ Pa; rubber is around 2 × 10⁷ Pa; a larger Young modulus means a stiffer material. Unlike a spring constant, which depends on the length and area of the particular object, the Young modulus is a property of the material alone.""",
  ["CLM-9702-6-011", "CLM-9702-6-012", "CLM-9702-6-009"], ["AO1"]),
 blk("6.1-b9", "worked_calculation", "Worked example: a guy wire on the Kalahari",
  """A steel wire 2.5 m long ties a solar-pump frame to a post in the Kalahari. Its diameter is 0.80 mm, and the wind loads it with 89 N, well within its limit of proportionality. How much does it stretch? First the area: A = πd² ÷ 4. The diameter is 0.80 mm = 0.80 × 10⁻³ m, so d² = 0.64 × 10⁻⁶ m², and A = 3.142 × 0.64 × 10⁻⁶ ÷ 4 = 0.503 × 10⁻⁶ m², that is 5.03 × 10⁻⁷ m². Then the strain, using E = 2.0 × 10¹¹ Pa for steel: the stress is F ÷ A = 89 ÷ 5.03 × 10⁻⁷ = 1.77 × 10⁸ Pa, and the strain is stress ÷ E = 1.77 × 10⁸ ÷ 2.0 × 10¹¹ = 8.85 × 10⁻⁴. Finally the extension: x = strain × L = 8.85 × 10⁻⁴ × 2.5 = 2.21 × 10⁻³ m, so the wire stretches about 2.2 mm.""",
  ["CLM-9702-6-011", "CLM-9702-6-012", "CLM-9702-6-015"], ["AO2"]),
 blk("6.1-b10", "process", "An experiment to determine the Young modulus of a wire",
  """The Young modulus of a metal in the form of a wire is found by loading the wire and measuring how it stretches. Clamp a long wire — 2 m or more — at one end, pass it over a pulley at the edge of the bench, and hang a mass hanger from the other end, with a sticky marker on the wire beside a metre rule fixed alongside. First measure the original length L from the clamp to the marker with the metre rule, in metres. Then measure the diameter d of the wire with a micrometer screw gauge, at several places and at different orientations across the wire, and average the readings, since the area A = πd² ÷ 4 depends on the square of d. Now add masses one at a time, recording the load F = mg each time and reading the marker to find the extension x, the new length minus the original; unload in steps and check that the marker returns, so the wire has stayed within its elastic limit. Plot force against extension and take the gradient of the straight line: since F = (EA ÷ L)x, the gradient is EA ÷ L, and the final result is E = gradient × L ÷ A, in pascals.""",
  ["CLM-9702-6-013", "CLM-9702-6-014", "CLM-9702-6-012"], ["AO2"]),
 blk("6.1-b11", "limitation", "Sources of uncertainty in the experiment",
  """The weak point of the method is that the extension is small: a 2 m steel wire stretches a few millimetres, and a metre rule graduated in millimetres therefore gives a large percentage uncertainty in x, which feeds straight into E. A long wire helps because it makes the extension proportionally larger; a marker read with a set square held against the rule reduces the parallax in the reading. The diameter matters twice over: it is small, and it is squared in the area, so the percentage uncertainty in d is doubled in A — the reason for taking several micrometer readings and averaging them, which reduces the random scatter of the readings. A systematic error also lurks: new wire has kinks, and the first loads straighten them, so early extensions read too large; pre-stretching the wire with the hanger alone, and measuring the original length after that, keeps E from coming out too small.""",
  ["CLM-9702-6-016", "CLM-9702-6-014"], ["AO2"]),
 blk("6.1-b12", "misconception", "Extension, not total length",
  """The commonest slip in Hooke’s-law work is putting the length of the stretched object into F = kx where the extension belongs. A wire 1.50 m long that stands 1.68 m under a load has an extension of 1.68 − 1.50 = 0.18 m, not 1.68 m; using the whole length makes the extension — and so the calculated force — many times too large. The test: has the original length been subtracted before the value is used?""",
  ["CLM-9702-6-008"], ["AO2"]),
 blk("6.1-b13", "misconception", "Stress, strain and strain energy are three things",
  """Stress, strain and strain energy sound alike and are not the same quantity. Stress is force per unit cross-sectional area and is measured in Pa; strain is extension ÷ original length and has no unit at all; elastic potential energy (also called strain energy) is the energy stored in a deformed object and is measured in joules. A learner who writes of a “large strain in pascals” has mixed the first two. The test that tells them apart: does the quantity have a unit, and which one? Pa means stress, no unit means strain, J means energy.""",
  ["CLM-9702-6-017", "CLM-9702-6-011"], ["AO2"]),
 blk("6.1-b14", "misconception", "Strain divides by the original length",
  """Strain is the extension divided by the original, unstretched length of the object — the length before the load went on. Dividing by the stretched length instead, or by “the length of the wire” without saying which, makes the strain too small, and the difference grows the further the object is stretched: a wire stretched from 2.00 m to 2.02 m has strain 0.02 ÷ 2.00 = 0.010, not 0.02 ÷ 2.02. The test: which length sits on the bottom of the fraction?""",
  ["CLM-9702-6-018", "CLM-9702-6-011"], ["AO2"]),
 blk("6.1-b15", "cross_link", "Connections",
  """Forces and their vector addition come from topic 3; the work done when a force moves its point of application — the same idea as the area under a force–extension graph — is developed in topic 5, where the stored energy of this topic reappears as elastic potential energy in the conservation of energy. The practical skills used here — the micrometer, repeated readings and the gradient of a straight-line graph — are the tools of topic 12, and the cross-sectional area of a wire is the same A that appears with resistivity in topic 9.""",
  [], ["AO1"]),
 blk("6.1-b16", "summary", "Checking the topic",
  """You can state what a deformation is and name the tensile or compressive force that caused it; use load, extension, compression and limit of proportionality exactly; apply F = kx and k = F ÷ x with the right quantities and units; define stress, strain and the Young modulus and use them together; and describe, with its instruments and its uncertainties, an experiment that finds the Young modulus of a wire.""",
  [], ["AO1"]),
]

U62_BLOCKS = [
 blk("6.2-b1", "learner_objective", "What this section covers",
  """Elastic deformation and plastic deformation, and the elastic limit that separates them; the area under a force–extension graph as the work done by the load; the elastic potential energy stored within the limit of proportionality; and the formula EP = ½Fx = ½kx².""",
  [], ["AO1"]),
 blk("6.2-b2", "definition", "Elastic deformation, plastic deformation and the elastic limit",
  """An elastic deformation is a change of shape that disappears when the load is removed: the object returns to its original length. A plastic deformation is a permanent change of shape: it stays after the load is removed. A wire loaded within its elastic limit shows elastic deformation — unload it and it returns exactly; loaded beyond the elastic limit, the deformation becomes plastic and the wire keeps a permanent extension. The elastic limit is therefore the point beyond which an object will not return to its original shape when the load is removed. It sits at or a little beyond the limit of proportionality, which is a different point: the limit of proportionality marks where the force stops being proportional to the extension, where the graph’s straight line ends, whereas the elastic limit marks where the returning stops. Between the two, the graph curves but the wire still comes back.""",
  ["CLM-9702-6-019", "CLM-9702-6-021"], ["AO1"]),
 blk("6.2-b3", "interpretation", "The force–extension graph of a wire loaded to breaking",
  """Draw the axes: force on the vertical, extension on the horizontal, both with their units. For a ductile metal wire the loading curve is a straight line through the origin up to the limit of proportionality, then a gentle curve with a lessening gradient that passes the elastic limit. Beyond the elastic limit the deformation is plastic: the extension grows quickly, and large extensions follow from small extra loads; a neck forms and the wire breaks at its breaking stress. Unloading anywhere tells the two regions apart. Unload inside the elastic region and the line retraces itself back to the origin. Unload from beyond the elastic limit and the wire follows a straight line parallel to the original loading line, falling to zero force at a non-zero extension — the permanent extension left by the plastic deformation. The elastic limit is found on the graph, if at all, by this unloading test, not by looking for a bend in the loading curve. For example, a wire loaded to 70 N that unloads along a parallel line to zero force at 0.8 mm has a permanent extension of 0.8 mm; the same wire loaded to 40 N would have returned to the origin. Where on the curve the elastic limit sits, that example cannot say — only the unloading test locates it.""",
  ["CLM-9702-6-022", "CLM-9702-6-020", "CLM-9702-6-019"], ["AO2"]),
 blk("6.2-b4", "interpretation", "The area under the graph is the work done",
  """The work done by the load is the area under the force–extension graph, because work is force multiplied by the distance moved in the direction of the force, and on the graph the force is the height and the extension the width. Within the limit of proportionality the graph is a triangle, so the area is easy: a spring stretched 0.040 m by a force of 12 N has work done on it of half of 12 × 0.040 = 0.24, which is 0.24 J. Where the graph curves, the area is found by counting squares on the grid, each square worth its width in N multiplied by its height in m; the count is the work done whatever the shape of the line. Up to the elastic limit that work is stored as elastic potential energy and comes back out on unloading. Beyond the elastic limit, the loading curve and the parallel unloading line enclose an area as well: that energy is not stored — it is dissipated in making the change of shape permanent — which is why bending a wire back and forth warms it.""",
  ["CLM-9702-6-023", "CLM-9702-6-024"], ["AO2"]),
 blk("6.2-b5", "formula", "EP = ½Fx = ½kx²",
  """For a material deformed within its limit of proportionality, the elastic potential energy stored is EP = ½Fx = ½kx², where F is the force in newtons at the extension x, in metres, and k is the spring constant in N m⁻¹; the energy is in joules (J). The half is not decoration: the force rises from zero in step with the extension, so the average force during the stretch is half the final force, and the work done — the area of the triangle under the graph — is half the product of the final force and the extension. Since F = kx on the straight part of the graph, the two forms are the same equation: EP = ½Fx = ½ × kx × x = ½kx². Beyond the limit of proportionality the formula is not valid, because the graph is no longer a triangle.""",
  ["CLM-9702-6-025", "CLM-9702-6-026"], ["AO1"]),
 blk("6.2-b6", "worked_calculation", "Worked example: a gate spring in the Otavi hills",
  """A gate spring on a farm gate in the Otavi hills has a spring constant of 250 N m⁻¹. The gate swings the spring to an extension of 0.16 m, within its limit of proportionality, and the stored energy holds the gate shut. Stored energy: EP = ½kx². First square the extension: 0.16 × 0.16 = 0.0256 m². Then 250 × 0.0256 = 6.4, and half of that is 3.2, so EP = 3.2 J. Stretching the gate further, to 0.32 m, would not store 6.4 J but four times more, 12.8 J, because doubling the extension doubles the force as well.""",
  ["CLM-9702-6-025", "CLM-9702-6-027"], ["AO2"]),
 blk("6.2-b7", "analysis_chain", "Double the extension, four times the energy",
  """A learner who expects twice the extension to store twice the energy is assuming the force stays as it was. It does not: within the limit of proportionality the force grows with the extension, F = kx, so twice the stretch means twice the force at the end. The energy, EP = ½kx², carries one factor of the force and one of the extension, so doubling the extension doubles both factors: the stored energy is multiplied by four, not two. The test that keeps this straight: does the force stay the same as the extension grows? If it does, the work is Fx; if it grows with the stretch, the work is the triangle, ½Fx.""",
  ["CLM-9702-6-027", "CLM-9702-6-026"], ["AO2"]),
 blk("6.2-b8", "misconception", "The limit of proportionality is not the elastic limit",
  """Labelling the point where the force–extension graph stops being straight as “the elastic limit” is a confusion of two different markers. The end of the straight line is the limit of proportionality — a statement about the graph’s shape. The elastic limit is a statement about the object’s behaviour: beyond it the object does not return to its original shape when the load is removed. The test: is the question about the line going curved, or about the object not returning?""",
  ["CLM-9702-6-021", "CLM-9702-6-004"], ["AO2"]),
 blk("6.2-b9", "cross_link", "Connections",
  """The work–energy ideas here belong to topic 5: work done is force × distance, and the energy stored in a deformed object is elastic potential energy in the conservation of energy. Topic 3 supplies the force as a vector along one line. The graph skills — gradient as spring constant, area by triangle or by counting squares, the unloading test — are the same ones topic 12 practises on practical graphs.""",
  [], ["AO1"]),
 blk("6.2-b10", "summary", "Checking the topic",
  """You can state what elastic deformation and plastic deformation are and where the elastic limit sits; describe the force–extension graph of a wire loaded to breaking, with its straight region, its curve and its parallel unloading line; read from that graph both the work done by the load and the elastic potential energy stored within the limit of proportionality; and use EP = ½Fx = ½kx² with its condition and its units, saying why the energy quadruples when the extension doubles.""",
  [], ["AO1"]),
]

def wc(blocks):
    return sum(len(((b["heading"] or "") + " " + b["text"]).split()) for b in blocks)

UNIT61 = {
 "unit_id": "CU-9702-6.1", "title": "Stress and strain",
 "objective_ids": [O["11"], O["12"], O["13"], O["14"], O["15"], O["16"]],
 "level": "AS Level", "core_status": "core", "objective_type": "phys_quantitative",
 "depth_tier": 2, "word_budget": {"min": 1806, "target": 2196, "max": 2586},
 "blocks": U61_BLOCKS, "word_count": wc(U61_BLOCKS), "qa_status": "review_required",
 "notes": ["Authored from the topic 6 work order; unit 6.1 as the order requires."],
}
UNIT62 = {
 "unit_id": "CU-9702-6.2", "title": "Elastic and plastic behaviour",
 "objective_ids": [O["21"], O["22"], O["23"], O["24"]],
 "level": "AS Level", "core_status": "core", "objective_type": "phys_graph",
 "depth_tier": 3, "word_budget": {"min": 1204, "target": 1464, "max": 1724},
 "blocks": U62_BLOCKS, "word_count": wc(U62_BLOCKS), "qa_status": "review_required",
 "notes": ["Authored from the topic 6 work order; unit 6.2 as the order requires."],
}

# ---------------------------------------------------------------- items
def flash(slot, obj, sub, ao, cw, tariff, diff, blooms, claims, prompt, answer, guidance, mc=None):
    prov = PROV + (" Discrimination card for misconception entry %s from curriculum/misconceptions.json." % mc if mc else "")
    it = {
      "item_id": slot, "objective_ids": [obj], "claim_ids": claims,
      "item_type": "flashcard", "subtype": sub, "assessment_objectives": ao,
      "blooms_level": blooms, "command_word": cw, "mark_tariff": tariff,
      "difficulty": diff, "prompt": prompt, "canonical_answer": answer,
      "marking_guidance": guidance, "context": dict(CTX),
      "prerequisite_item_ids": [], "core_status": "core",
      "intentional_duplicate_group": None, "provenance": prov,
      "qa_status": "review_required", "claims_seen": {c: 1 for c in claims},
    }
    it["authored_hash"] = H(it)
    return it

ITEMS = []
A = ITEMS.append

# --- OBJ 6.1-01
A(flash("ITEM-9702-6-001-DEF", O["11"], "DEF", ["AO1"], "State", 1, 2, "Remember",
 ["CLM-9702-6-001", "CLM-9702-6-002"],
 "State what is meant by a deformation of an object, and name the two kinds of force that cause one in a single line.",
 "A deformation is a change in the shape or size of an object. In one dimension it is caused by a tensile force, which pulls the two ends of the object apart, or by a compressive force, which pushes them together.",
 ["1 mark: the definition names a change of shape or size, and the two forces — tensile and compressive — with the pulling and the pushing that each does along one line."]))
A(flash("ITEM-9702-6-002-MECH", O["11"], "MECH", ["AO2"], "Explain", 2, 2, "Understand",
 ["CLM-9702-6-001", "CLM-9702-6-002"],
 "A tow rope pulls a bakkie out of sand while the bakkie’s bumper pushes a fence post upright. Explain how the rope and the bumper each deform the object they act on.",
 "The rope exerts a tensile force: it pulls the rope’s two ends away from each other along one line, which makes the rope longer — an extension. The bumper exerts a compressive force: it pushes the post’s ends towards each other, which shortens it — a compression. In each case a pair of forces acts along a single line and changes the object’s length, which is the deformation.",
 ["How the tensile force acts: it pulls the ends apart along the line, which causes the extension of the rope — 1 mark.",
  "How the compressive force acts: it pushes the ends together, which causes the compression of the post — 1 mark."]))
A(flash("ITEM-9702-6-042-FEATURE", O["11"], "FEATURE", ["AO1"], "State", 1, 3, "Remember",
 ["CLM-9702-6-001"],
 "State one feature of a tensile force and one feature of a compressive force that distinguish the two, for deformation in one dimension.",
 "A tensile force acts to pull the two ends of the object away from each other, so the object’s length increases; a compressive force acts to push the ends towards each other, so the length decreases. Each is a property of the pair of forces acting along the single line of the deformation, not of the material.",
 ["1 mark: the stated features — a tensile force pulls the ends apart (lengthening) whereas a compressive force pushes them together (shortening), both along one line; each characteristic point needed."]))
A(flash("ITEM-9702-6-052-DIST", O["11"], "DIST", ["AO1"], "State", 1, 3, "Understand",
 ["CLM-9702-6-001", "CLM-9702-6-002"],
 "State the difference between a tensile force and a compressive force as causes of deformation in one dimension.",
 "A tensile force pulls the two ends of the object away from each other and makes it longer, whereas a compressive force pushes the ends towards each other and makes it shorter. Both are measured in newtons and both act along the one line of the deformation; the difference is the direction of the forces on the ends, which decides whether the length increases or decreases.",
 ["1 mark: the distinction — a tensile force pulls the ends apart causing an increase in length, whereas a compressive force pushes them together causing a decrease; both points of contrast are needed."]))

# --- OBJ 6.1-02
A(flash("ITEM-9702-6-003-DEF", O["12"], "DEF", ["AO1"], "State", 1, 2, "Remember",
 ["CLM-9702-6-003"],
 "State what is meant by the load on an object, and by its extension.",
 "The load is the force applied to the object, in newtons. The extension is the increase in length it causes: the stretched length minus the original length, in metres.",
 ["1 mark: the definition of each term — the load as the applied force in N, and the extension as stretched length minus original length in m; both meanings are needed for the mark."]))
A(flash("ITEM-9702-6-004-MECH", O["12"], "MECH", ["AO2"], "Explain", 2, 2, "Understand",
 ["CLM-9702-6-004", "CLM-9702-6-005"],
 "On a force–extension graph for a loaded spring, the straight line through the origin ends and the graph begins to curve. Explain how the limit of proportionality is identified and what changes there.",
 "The limit of proportionality is found as the last point on the straight line through the origin; beyond it the graph curves. Up to that point the force was proportional to the extension, so doubling the load doubled the extension and the gradient was constant. Beyond it the force is no longer proportional to the extension, so extra load produces less extra extension and the gradient falls. Nothing there says whether the spring returns to its original shape — that is a different point, the elastic limit.",
 ["How the point is identified: the last point on the straight line through the origin, with the graph curving beyond it — 1 mark.",
  "What changes there: the force stops being proportional to the extension, which causes the gradient of the graph to fall — 1 mark."]))
A(flash("ITEM-9702-6-043-FEATURE", O["12"], "FEATURE", ["AO1"], "State", 1, 3, "Remember",
 ["CLM-9702-6-005", "CLM-9702-6-009"],
 "State two features of the force–extension graph of a spring loaded within its limit of proportionality.",
 "The graph is a straight line through the origin, showing that the force is proportional to the extension; and its gradient is constant, equal to the spring constant k, the force per unit extension. Both features hold up to the limit of proportionality, where the line ends.",
 ["1 mark: two stated features — a straight line through the origin (force proportional to extension) and a constant gradient equal to the spring constant."]))
A(flash("ITEM-9702-6-053-DIST", O["12"], "DIST", ["AO1"], "State", 1, 3, "Understand",
 ["CLM-9702-6-003"],
 "State the difference between the extension and the compression of a loaded object.",
 "The extension is an increase in length: the stretched length minus the original length. The compression is a decrease in length: the original length minus the shortened length. Both are differences from the original length measured in metres, whereas the load itself is the force in newtons that causes one or the other.",
 ["1 mark: the distinction — an extension increases the length from the original whereas a compression decreases it; both are differences from the original length."]))

# --- OBJ 6.1-03 (Hooke's law)
A(flash("ITEM-9702-6-005-DEF", O["13"], "DEF", ["AO1"], "State", 1, 2, "Remember",
 ["CLM-9702-6-006"],
 "State Hooke’s law.",
 "The force on an object is proportional to its extension, provided the limit of proportionality is not exceeded: F = kx, with F the force in N, x the extension in m and k the spring constant in N m⁻¹.",
 ["1 mark: the law stated as a proportionality between force and extension, with its equation F = kx and the condition — within the limit of proportionality — that makes it a law."]))
A(flash("ITEM-9702-6-006-CALC", O["13"], "CALC", ["AO2"], "Calculate", 2, 2, "Apply",
 ["CLM-9702-6-006", "CLM-9702-6-008"],
 "A spring scale has a spring of spring constant 45 N m⁻¹. A bag weighing 7.2 N hangs at rest on it, within the limit of proportionality. Calculate the extension of the spring.",
 "x = F ÷ k. Substitution: 7.2 ÷ 45 = 0.16, so the extension is 0.16 m. The final answer: 0.16 m, given to two significant figures, the precision of the data.",
 ["Equation and substitution: x = F ÷ k with F = 7.2 N and k = 45 N m⁻¹ — 1 mark for the first step.",
  "Final answer: 0.16 m with its unit and two significant figures — 1 mark. Multiplying 7.2 by 45 instead of dividing gives 324, and using the spring’s stretched length instead of its extension gives a larger value still."]))
A(flash("ITEM-9702-6-007-CALC", O["13"], "CALC", ["AO2"], "Calculate", 2, 2, "Apply",
 ["CLM-9702-6-006", "CLM-9702-6-008"],
 "A screen-door spring of original length 0.25 m is 0.31 m long when the door is open. The door pulls on it with a force of 4.2 N, within its limit of proportionality. Calculate the spring constant of the spring.",
 "Extension first: x = 0.31 − 0.25 = 0.060 m. Then k = F ÷ x. Substitution: 4.2 ÷ 0.060 = 70, so k = 70 N m⁻¹ to two significant figures.",
 ["Equation and substitution: k = F ÷ x with the extension found first as 0.31 − 0.25 = 0.060 m — 1 mark for the step.",
  "Final answer: 70 N m⁻¹ with its unit and two significant figures — 1 mark. Using 0.31 m instead of the 0.060 m extension gives 14 N m⁻¹, the error of forgetting the original length."]))
A(flash("ITEM-9702-6-008-CALC", O["13"], "CALC", ["AO2"], "Calculate", 2, 2, "Apply",
 ["CLM-9702-6-006", "CLM-9702-6-007"],
 "A spring of spring constant 120 N m⁻¹ is stretched 0.050 m, which is within its limit of proportionality. Calculate the force exerted by the load.",
 "F = kx. Substitution: 120 × 0.050 = 6.0, so the force is 6.0 N, to two significant figures matching the data.",
 ["Equation and substitution: F = kx with k = 120 N m⁻¹ and x = 0.050 m — 1 mark.",
  "Final answer: 6.0 N with its unit, to two significant figures — 1 mark. Dividing instead of multiplying gives 2400, a value that cannot be a force in N."]))
A(flash("ITEM-9702-6-032-MISCON", O["13"], "MISCON", ["AO1"], "Explain", 1, 3, "Understand",
 ["CLM-9702-6-006", "CLM-9702-6-008"],
 "A wire of original length 1.50 m is 1.68 m long under a load. A learner puts 1.68 into F = kx as the extension. Explain the error.",
 "The law uses the extension, not the length of the stretched wire: extension = stretched length − original length, so the value that belongs in the equation is 1.68 − 1.50 = 0.18 m. Using 1.68 m instead makes the extension many times too large, and the force comes out wrong in the same ratio. The test: has the original length been subtracted?",
 ["1 mark: the error named — the length of the stretched wire used in place of the extension; in fact the extension is stretched length minus original length (0.18 m here), so the value the learner used is not the same quantity as the one F = kx needs."],
 mc="MC-9702-6-01"))
A(flash("ITEM-9702-6-044-FEATURE", O["13"], "FEATURE", ["AO1"], "State", 1, 3, "Remember",
 ["CLM-9702-6-006", "CLM-9702-6-007", "CLM-9702-6-005"],
 "State two features of Hooke’s law that a calculation must respect.",
 "It links force to extension — the increase in length from the original, not the stretched length — and it holds only within the limit of proportionality, where the graph is still a straight line through the origin. Beyond that point the force is no longer proportional to the extension, and the equation cannot be used.",
 ["1 mark: two stated features — the x in F = kx is the extension, and the law’s validity ends at the limit of proportionality, past which the force is no longer proportional to the extension."]))
A(flash("ITEM-9702-6-054-DIST", O["13"], "DIST", ["AO1"], "State", 1, 3, "Understand",
 ["CLM-9702-6-005", "CLM-9702-6-007"],
 "State the difference between how force and extension behave within the limit of proportionality and how they behave beyond it.",
 "Within the limit of proportionality the force is proportional to the extension, so the graph is a straight line through the origin and F = kx holds; beyond it the force is no longer proportional to the extension, the graph curves, and the equation cannot be used. In both regions the load still stretches the object — the difference is the proportionality, not the stretching.",
 ["1 mark: the distinction — proportional (straight-line graph, F = kx valid) within, whereas no longer proportional (curved graph) beyond; both regions described."]))

# --- OBJ 6.1-04 (spring constant)
A(flash("ITEM-9702-6-009-DEF", O["14"], "DEF", ["AO1"], "State", 1, 2, "Remember",
 ["CLM-9702-6-009"],
 "State what is meant by the spring constant of a spring, and give its unit.",
 "The spring constant is the force per unit extension, k = F ÷ x, with F in newtons and x the extension in metres; its unit is N m⁻¹. A stiffer spring has a larger spring constant, and it is the gradient of the force–extension graph within the limit of proportionality.",
 ["1 mark: the definition as force per unit extension with the equation k = F ÷ x and the unit N m⁻¹; the gradient property may add meaning but is not required."]))
A(flash("ITEM-9702-6-010-CALC", O["14"], "CALC", ["AO2"], "Calculate", 2, 2, "Apply",
 ["CLM-9702-6-008", "CLM-9702-6-009"],
 "A load of 3.6 N stretches a spring from 0.400 m to 0.460 m, within its limit of proportionality. Calculate the spring constant.",
 "Extension: x = 0.460 − 0.400 = 0.060 m. Spring constant: k = F ÷ x. Substitution: 3.6 ÷ 0.060 = 60, so k = 60 N m⁻¹ to two significant figures.",
 ["Equation and substitution: k = F ÷ x with the extension first found as 0.060 m — 1 mark.",
  "Final answer: 60 N m⁻¹ with its unit and two significant figures — 1 mark. Using 0.460 m instead of the extension gives 7.8 N m⁻¹, the length-for-extension error."]))
A(flash("ITEM-9702-6-011-CALC", O["14"], "CALC", ["AO2"], "Calculate", 2, 2, "Apply",
 ["CLM-9702-6-009", "CLM-9702-6-010"],
 "Two identical springs, each of spring constant 48 N m⁻¹, are joined end to end and a 1.2 N load is hung from the pair. Calculate the extension of the pair.",
 "End to end, each spring carries the whole 1.2 N load, so the extensions add and the pair behaves as one spring of half the constant: k = 48 ÷ 2 = 24 N m⁻¹. Extension: x = F ÷ k. Substitution: 1.2 ÷ 24 = 0.050, so the extension is 0.050 m to two significant figures.",
 ["Equation and substitution: the combined constant halved to 24 N m⁻¹ because each spring carries the whole load, then x = F ÷ k — 1 mark.",
  "Final answer: 0.050 m with its unit and two significant figures — 1 mark. Adding the constants to get 96 N m⁻¹ gives 0.0125 m, half the true extension."]))
A(flash("ITEM-9702-6-012-CALC", O["14"], "CALC", ["AO2"], "Calculate", 2, 2, "Apply",
 ["CLM-9702-6-009", "CLM-9702-6-010"],
 "An 8.0 N load hangs at rest from two identical springs joined side by side, so they share the load equally. Each spring has spring constant 50 N m⁻¹. Calculate the extension of each spring.",
 "Sharing equally, each spring carries 8.0 ÷ 2 = 4.0 N. Extension: x = F ÷ k. Substitution: 4.0 ÷ 50 = 0.080, so each spring extends 0.080 m to two significant figures.",
 ["Equation and substitution: the load halved to 4.0 N on each spring, then x = F ÷ k — 1 mark.",
  "Final answer: 0.080 m with its unit and two significant figures — 1 mark. Letting one spring carry the whole 8.0 N gives 0.16 m, the error of not sharing the load."]))
A(flash("ITEM-9702-6-033-MISCON", O["14"], "MISCON", ["AO1"], "Explain", 1, 3, "Understand",
 ["CLM-9702-6-009", "CLM-9702-6-010"],
 "A learner joins two springs end to end and adds their spring constants to find the stiffness of the pair. Explain the error.",
 "End to end, each spring carries the whole load, so each stretches fully and the two extensions add; the pair is softer, not stiffer, and for identical springs the combined constant is half of one spring’s. Adding constants belongs to springs side by side, which share the load. The test: does each spring carry the full load? If it does, the extensions add and the constants do not.",
 ["1 mark: the error named — spring constants added for a series pair when in fact each spring carries the whole load and the extensions add; constants add instead for springs side by side."],
 mc="MC-9702-6-02"))
A(flash("ITEM-9702-6-045-FEATURE", O["14"], "FEATURE", ["AO1"], "State", 1, 3, "Remember",
 ["CLM-9702-6-009", "CLM-9702-6-007"],
 "State two features of the spring constant that make it a property of the spring, within the limit of proportionality.",
 "It is defined as force per unit extension, k = F ÷ x, in N m⁻¹, and its value is set by the spring itself: the same spring gives the same gradient on the force–extension graph whatever load, within the limit of proportionality, produces the extension. Its validity ends where the straight line ends, because beyond that point the force is no longer proportional to the extension.",
 ["1 mark: two stated features — force per unit extension with the unit N m⁻¹, and a constant gradient for the given spring within the limit of proportionality."]))
A(flash("ITEM-9702-6-055-DIST", O["14"], "DIST", ["AO1"], "State", 1, 3, "Understand",
 ["CLM-9702-6-009", "CLM-9702-6-010"],
 "State the difference between the combined spring constant of two identical springs joined end to end and of the same two joined side by side.",
 "End to end, each spring carries the whole load, so the extensions add and the combined constant is half of one spring’s — the pair is softer. Side by side, the springs share the load, so the constants add and the combined constant is twice one spring’s. The difference comes from whether each spring carries the full load: it does when they are end to end, and it does not when they are side by side.",
 ["1 mark: the distinction — end to end the extensions add so the combined constant is halved, whereas side by side the constants add and it is doubled; the reason is whether each spring carries the full load."]))

# --- OBJ 6.1-05 (stress, strain, Young modulus)
A(flash("ITEM-9702-6-013-DEF", O["15"], "DEF", ["AO1"], "Define", 1, 1, "Remember",
 ["CLM-9702-6-011"],
 "Define stress and strain, and give the unit of each.",
 "Stress is the force per unit cross-sectional area, σ = F ÷ A, in pascals (Pa), where 1 Pa = 1 N m⁻². Strain is the extension divided by the original length, ε = x ÷ L; it is a ratio of two lengths, so it has no unit.",
 ["1 mark: both definitions with their symbols — stress as force per unit cross-sectional area in Pa, and strain as extension ÷ original length with no unit; each meaning must be exact for the mark."]))
A(flash("ITEM-9702-6-014-CALC", O["15"], "CALC", ["AO2"], "Calculate", 2, 1, "Apply",
 ["CLM-9702-6-011", "CLM-9702-6-015"],
 "A wire of cross-sectional area 0.30 mm² hangs vertically and carries a load of 60 N at its lower end, within its limit of proportionality. Calculate the stress in the wire, in Pa.",
 "Convert the area first: 0.30 mm² = 0.30 × 10⁻⁶ m² = 3.0 × 10⁻⁷ m². Stress: σ = F ÷ A. Substitution: 60 ÷ 3.0 = 20, so the stress is 20 × 10⁷ Pa, which is 2.0 × 10⁸ Pa to two significant figures.",
 ["Equation and substitution: σ = F ÷ A with the area converted to 3.0 × 10⁻⁷ m² first — 1 mark for the step.",
  "Final answer: 2.0 × 10⁸ Pa with its unit and two significant figures — 1 mark. Using 0.30 × 10⁻³ m² as the area gives 2.0 × 10⁵ Pa, the linear conversion instead of the squared one."]))
A(flash("ITEM-9702-6-034-MISCON", O["15"], "MISCON", ["AO1"], "Explain", 1, 2, "Understand",
 ["CLM-9702-6-011", "CLM-9702-6-017"],
 "A learner says a wire with a large strain also has a large stress, because the two quantities are nearly the same thing. Explain the error.",
 "Stress is force per unit cross-sectional area, in Pa; strain is extension ÷ original length and has no unit; they are not the same quantity and neither implies the other without the material’s Young modulus. Strain energy, if it enters the discussion, is the stored energy in J — a third quantity again. The test: does the quantity have a unit, and which one? Pa means stress, no unit means strain, J means energy.",
 ["1 mark: the error named — stress confused with strain, or strain with strain energy; in fact stress is force ÷ area in Pa whereas strain is extension ÷ original length with no unit, and the test is the unit each carries."],
 mc="MC-9702-6-03"))
A(flash("ITEM-9702-6-035-MISCON", O["15"], "MISCON", ["AO1"], "Explain", 1, 2, "Understand",
 ["CLM-9702-6-011", "CLM-9702-6-018"],
 "A learner defines strain as the extension divided by the length of the wire while it is stretched. Explain the error.",
 "The length in the denominator must be the original, unstretched length — the length before the load went on. Dividing by the stretched length makes the strain too small, and the difference grows the further the wire is stretched: a wire stretched from 2.00 m to 2.02 m has strain 0.02 ÷ 2.00 = 0.010, not 0.02 ÷ 2.02 = 0.0099. The test: which length sits on the bottom of the fraction?",
 ["1 mark: the error named — strain defined without the word original; the correct definition divides the extension by the original, unstretched length, and the test is which length appears on the bottom of the fraction."],
 mc="MC-9702-6-04"))
A(flash("ITEM-9702-6-048-FEATURE", O["15"], "FEATURE", ["AO1"], "State", 1, 2, "Remember",
 ["CLM-9702-6-012", "CLM-9702-6-009"],
 "State two features of the Young modulus that distinguish it from a spring constant.",
 "It is a property of the material alone — stress ÷ strain, in Pa — so wires of different lengths and areas of the same metal share one Young modulus, whereas a spring constant k, in N m⁻¹, depends on the object’s dimensions. And it applies within the limit of proportionality, where stress is proportional to strain.",
 ["1 mark: two stated features — a material property in Pa independent of the object’s dimensions, unlike the spring constant, and defined as stress ÷ strain within the limit of proportionality."]))
A(flash("ITEM-9702-6-058-DIST", O["15"], "DIST", ["AO1"], "State", 1, 2, "Understand",
 ["CLM-9702-6-009", "CLM-9702-6-012"],
 "State the difference between the spring constant of an object and the Young modulus of its material.",
 "The spring constant, k = F ÷ x in N m⁻¹, describes one object and depends on its length and cross-sectional area as well as its material; the Young modulus, E = stress ÷ strain in Pa, describes the material alone and is the same for every object made of it. Both are used within the limit of proportionality, where force is proportional to extension and stress to strain.",
 ["1 mark: the distinction — the spring constant belongs to the object and carries N m⁻¹, whereas the Young modulus belongs to the material and carries Pa; both valid within the limit of proportionality."]))

# --- OBJ 6.1-06 (Young modulus experiment)
A(flash("ITEM-9702-6-015-PROC", O["16"], "PROC", ["AO1"], "Describe", 3, 3, "Apply",
 ["CLM-9702-6-013", "CLM-9702-6-014", "CLM-9702-6-012"],
 "Describe an experiment to determine the Young modulus of a steel wire, saying what is measured in each step, with which instrument, and how the final result is obtained.",
 "First clamp a long wire at one end over a pulley at the bench edge and hang a mass hanger from its other end, with a marker on the wire beside a fixed metre rule; pre-stretch it with the hanger alone. Measure the original length L from clamp to marker with the metre rule. Then measure the diameter d with a micrometer screw gauge at several places and orientations, and average: the cross-sectional area is A = πd² ÷ 4. Then add masses one at a time; for each load F = mg, read the marker to get the extension x, the new length minus the original. Finally plot force against extension, take the gradient of the straight line within the limit of proportionality — the gradient is EA ÷ L — so the result is E = gradient × L ÷ A, in Pa.",
 ["Order of steps: first the length with the rule and the diameter with the micrometer, then the load and extension readings — 1 mark for the sequence and its instruments.",
  "The measured readings: L from the rule, d averaged from the micrometer, F = mg and the extension x from the marker — 1 mark.",
  "The final result: the gradient of the force–extension line gives E = gradient × L ÷ A in Pa, so the answer comes from the graph, not from one reading — 1 mark."]))
A(flash("ITEM-9702-6-016-LIM", O["16"], "LIM", ["AO2"], "Describe", 2, 3, "Evaluate",
 ["CLM-9702-6-016", "CLM-9702-6-013"],
 "Describe two limitations of the load–extension method for finding the Young modulus of a wire, and the effect each has on the value obtained.",
 "One limitation is the size of the extension: a steel wire a couple of metres long stretches by only a few millimetres, so a metre rule graduated in millimetres gives a large percentage uncertainty in x, and the gradient of the force–extension graph — and so the calculated E — is uncertain in the same proportion. A second is kinked wire: the first loads straighten the kinks, so the early extensions read too large; the gradient comes out too small and E comes out too small with it, an error that averaging repeats cannot remove because it is systematic and shifts every reading the same way, not random scatter.",
 ["Limitation and its effect: the small extension read against a millimetre rule, so the percentage uncertainty in x is large, which affects the gradient and so E — 1 mark.",
  "The kinks: the first loads straighten them, so the early readings overstate x, because the error is systematic and survives averaging — 1 mark."]))
A(flash("ITEM-9702-6-017-APP", O["16"], "APP", ["AO2"], "Explain", 1, 3, "Apply",
 ["CLM-9702-6-014", "CLM-9702-6-016"],
 "In this experiment the wire is made as long as the bench allows, and the diameter is measured at many points with a micrometer. Explain why both choices are made.",
 "Here the situation is that the extension is a few millimetres while the length is metres: a longer wire gives a proportionally larger extension, so its percentage uncertainty falls, because the reading error of the rule is fixed. The diameter enters as d² in the area A = πd² ÷ 4, so the percentage uncertainty in d is doubled in A; measuring at many points and averaging reduces the random scatter of the readings, which keeps the uncertainty in A — and so in E — small.",
 ["1 mark: the reasons for the situation given — a longer wire gives a larger extension with the same reading error, and averaging many diameter readings reduces the random scatter, so both keep the uncertainty in E small."]))
A(flash("ITEM-9702-6-036-MISCON", O["16"], "MISCON", ["AO1"], "Explain", 1, 4, "Understand",
 ["CLM-9702-6-015", "CLM-9702-6-011"],
 "A wire has a cross-sectional area of 0.20 mm². A learner converts this to 0.20 × 10⁻³ m² before calculating a stress. Explain the error.",
 "The millimetre is squared in mm², so the conversion factor is squared too: 1 mm² = 1 × 10⁻⁶ m², and 0.20 mm² is 2.0 × 10⁻⁷ m², not 0.20 × 10⁻³ m². Using the wrong area makes the stress — force ÷ area — a thousand times too small. The same slip comes from using the diameter as the radius: the area is A = πd² ÷ 4 = πr², so d and r must not be swapped. The test: has the area been converted to m², and was the diameter halved before squaring?",
 ["1 mark: the error named — the mm² conversion treated as linear instead of squared; in fact 1 mm² is 1 × 10⁻⁶ m², so 0.20 mm² is 2.0 × 10⁻⁷ m², and the companion slip is using the diameter as the radius in A = πd² ÷ 4."],
 mc="MC-9702-6-05"))
A(flash("ITEM-9702-6-039-FEATURE", O["16"], "FEATURE", ["AO1"], "State", 1, 4, "Remember",
 ["CLM-9702-6-013", "CLM-9702-6-014"],
 "State two features of the apparatus in a Young-modulus experiment that keep the uncertainty in the result small.",
 "A long wire, whose length is measured with a metre rule, makes the extension proportionally larger and so reduces the percentage uncertainty in it. A micrometer screw gauge, reading to 0.01 mm, measures the diameter at several points and orientations, and averaging those readings reduces the random scatter — important because the diameter is squared in the area. Both instruments are chosen for the size of the quantity they read.",
 ["1 mark: two stated features — the long wire read against a metre rule and the micrometer with averaged readings at several points, each named with the reason it reduces the uncertainty."]))
A(flash("ITEM-9702-6-049-DIST", O["16"], "DIST", ["AO1"], "State", 1, 4, "Understand",
 ["CLM-9702-6-013", "CLM-9702-6-014"],
 "State the difference between the part the metre rule and the part the micrometer screw gauge play in the Young-modulus experiment.",
 "The metre rule measures the original length of the wire, a quantity of metres with millimetre graduations, whereas the micrometer measures the wire’s diameter, a quantity of tenths of a millimetre needing a finer instrument; both feed the same calculation, the length directly into the strain and the diameter into the area A = πd² ÷ 4. The readings are of different sizes, so they need different instruments, while both contribute to the uncertainty in E.",
 ["1 mark: the distinction — the rule reads the length in m while the micrometer reads the diameter in mm at several points; both are needed, whereas neither can substitute for the other."]))

# --- OBJ 6.2-01
A(flash("ITEM-9702-6-018-DEF", O["21"], "DEF", ["AO1"], "State", 1, 2, "Remember",
 ["CLM-9702-6-019"],
 "State what is meant by elastic deformation and by plastic deformation.",
 "An elastic deformation is a change of shape that disappears when the load is removed: the object returns to its original length. A plastic deformation is a permanent change of shape: it stays after the load is removed.",
 ["1 mark: the definition of each — elastic deformation disappears on unloading, whereas plastic deformation is permanent; the meaning of both terms is needed for the mark."]))
A(flash("ITEM-9702-6-019-MECH", O["21"], "MECH", ["AO2"], "Explain", 2, 2, "Understand",
 ["CLM-9702-6-019", "CLM-9702-6-020"],
 "A wire is loaded a little beyond its elastic limit and then unloaded. Explain what happens to its length during loading and after the load is removed.",
 "Beyond the elastic limit the deformation is plastic, so during loading the extension grows quickly for small extra loads. When the load is removed the wire does not return to its original length: it follows a straight line parallel to its original loading line back to zero force, but that line reaches zero force at a non-zero extension — the permanent extension left by the plastic deformation. How far it sits past the original length measures how far past the elastic limit the loading went.",
 ["How the loading behaves: beyond the elastic limit the deformation becomes plastic, so the extension grows quickly — 1 mark.",
  "How the unloading behaves: the wire returns along a parallel line but keeps a permanent extension, because the deformation past the elastic limit does not disappear — 1 mark."]))
A(flash("ITEM-9702-6-038-MISCON", O["21"], "MISCON", ["AO1"], "Explain", 1, 3, "Understand",
 ["CLM-9702-6-021", "CLM-9702-6-019"],
 "A learner marks the point where a force–extension graph stops being straight and labels it the elastic limit. Explain the error.",
 "The end of the straight line is the limit of proportionality: beyond it the force is no longer proportional to the extension and the graph curves. The elastic limit is a different point: beyond it the object does not return to its original shape when the load is removed, and it lies at or beyond the limit of proportionality. The test: is the question about the line going curved, or about the object not returning? The first names the limit of proportionality, not the elastic limit.",
 ["1 mark: the error named — the limit of proportionality treated as if it were the elastic limit; in fact the first marks where proportionality ends, whereas the elastic limit marks where the deformation stops being reversible."],
 mc="MC-9702-6-07"))
A(flash("ITEM-9702-6-046-FEATURE", O["21"], "FEATURE", ["AO1"], "State", 1, 3, "Remember",
 ["CLM-9702-6-019", "CLM-9702-6-021"],
 "State two features of the behaviour of a material deformed within its elastic limit, one seen while it is loaded and one seen when the load is removed.",
 "While it is loaded, its deformation follows the force–extension graph, which has not passed the elastic limit and so may be straight or gently curved. When the load is removed, the deformation is elastic: the object returns exactly to its original shape, and its unloading line retraces the loading line. Points from both features mark out the elastic limit itself — beyond it, the deformation becomes plastic and permanent.",
 ["1 mark: two stated features — within the elastic limit the load still deforms the object along the graph, and on removal the elastic deformation disappears so the object returns to its original shape."]))
A(flash("ITEM-9702-6-056-DIST", O["21"], "DIST", ["AO1"], "State", 1, 3, "Understand",
 ["CLM-9702-6-021", "CLM-9702-6-004"],
 "State the difference between the limit of proportionality and the elastic limit.",
 "The limit of proportionality is the point beyond which force is no longer proportional to extension: the graph’s straight line ends there. The elastic limit is the point beyond which the object will not return to its original shape when the load is removed: the deformation becomes plastic there. Between the two, the graph curves while the object still returns to its original shape on unloading, so the two points are distinct though close together.",
 ["1 mark: the distinction — the limit of proportionality is about the graph going curved, whereas the elastic limit is about the object not returning to its original shape; both points named."]))

# --- OBJ 6.2-02 (area = work done)
A(flash("ITEM-9702-6-020-INTERP", O["22"], "INTERP", ["AO2"], "Determine", 2, 3, "Analyse",
 ["CLM-9702-6-022", "CLM-9702-6-023", "CLM-9702-6-024"],
 "A force–extension graph for a spring is a straight line from the origin to the point (0.040 m, 12 N). Determine the work done by the load in stretching the spring.",
 "The area under the force–extension graph represents the work done. The line is straight, so the area is a triangle: base × height ÷ 2. Reading the values from the graph, 12 × 0.040 = 0.48, and 0.48 ÷ 2 = 0.24, so the work done is 0.24 J.",
 ["Reading the graph: the area under the straight line, a triangle of height 12 N and base 0.040 m — 1 mark.",
  "What the area means: it represents the work done by the load, so the value is 0.24 J — 1 mark."]))
A(flash("ITEM-9702-6-021-INTERP", O["22"], "INTERP", ["AO2"], "Determine", 2, 3, "Analyse",
 ["CLM-9702-6-022", "CLM-9702-6-023"],
 "A force–extension graph rises as a straight line from the origin to (0.060 m, 9.0 N), then curves on to (0.10 m, 10.5 N). The area under the curved part, found by counting squares on the grid, is 0.064 J. Determine the total work done in reaching an extension of 0.10 m.",
 "The area under the whole graph represents the work done, so it is found in two pieces. The straight part is a triangle: 9.0 × 0.060 = 0.54, and 0.54 ÷ 2 = 0.27, so the first part is 0.27 J. The curved part is given as 0.064 J. Total: 0.27 + 0.064 = 0.334, so the work done is 0.334 J, which is 0.33 J to two significant figures.",
 ["Reading the graph: the triangle under the straight part and the given area under the curve, both treated as areas under the graph — 1 mark.",
  "What the areas mean: the total represents the work done by the load, so the value is 0.33 J to two significant figures — 1 mark."]))
A(flash("ITEM-9702-6-022-CALC", O["22"], "CALC", ["AO2"], "Determine", 2, 3, "Apply",
 ["CLM-9702-6-023", "CLM-9702-6-024", "CLM-9702-6-025"],
 "A spring of spring constant 200 N m⁻¹ is stretched 0.050 m, within its limit of proportionality. Determine the work done by the load.",
 "Within the limit of proportionality the work done is the elastic potential energy stored, EP = ½kx². First x² = 0.050 × 0.050 = 0.0025 m². Then 200 × 0.0025 = 0.50, and half of that is 0.25, so the work done is 0.25 J to two significant figures.",
 ["Equation and substitution: EP = ½kx² with k = 200 N m⁻¹ and x = 0.050 m — 1 mark.",
  "Final answer: 0.25 J with its unit and two significant figures; the value also equals the area under the graph, so the answer is the stored energy — 1 mark."]))
A(flash("ITEM-9702-6-023-APP", O["22"], "APP", ["AO2"], "Explain", 1, 3, "Apply",
 ["CLM-9702-6-023", "CLM-9702-6-024"],
 "Two springs are stretched by the same load within their limits of proportionality. The softer spring stretches twice as far as the stiffer one. Explain which spring has more work done on it.",
 "In this case the work done is the area under the force–extension graph, ½Fx. Both springs end at the same force F, but the softer one has twice the extension, so its triangle has the same height and twice the base — twice the area, and so twice the work done on it. Since the deformation stays within the limit of proportionality, that work is stored as elastic potential energy, of which the stiffer spring stores only half as much.",
 ["1 mark: the reason for this case — work done = ½Fx, so with the same force and twice the extension the softer spring has twice the work done on it, because the area under its graph is twice as large."]))
A(flash("ITEM-9702-6-040-FEATURE", O["22"], "FEATURE", ["AO1"], "State", 1, 4, "Remember",
 ["CLM-9702-6-023", "CLM-9702-6-024"],
 "State two features of the area under a force–extension graph.",
 "It represents the work done by the load in producing the extension, whatever the shape of the graph. Up to the elastic limit the same area equals the elastic potential energy stored, recovered on unloading; beyond the elastic limit the loading and unloading lines enclose an area whose energy is dissipated in the plastic deformation, so it is not stored.",
 ["1 mark: two stated features — the area represents work done by the load, and up to the elastic limit it equals the stored energy, whereas beyond it part is dissipated."]))
A(flash("ITEM-9702-6-050-DIST", O["22"], "DIST", ["AO1"], "State", 1, 4, "Understand",
 ["CLM-9702-6-023", "CLM-9702-6-024", "CLM-9702-6-019"],
 "State the difference between what the area under a loading graph means when the deformation is elastic and when it is plastic.",
 "In elastic deformation the area is the work done by the load and all of it is stored as elastic potential energy, given back when the object is unloaded. In plastic deformation the area is still the work done by the load, but the unloading line encloses an extra area with the loading curve: that part is dissipated in making the change of shape permanent, so less than the whole area is stored. The area means work done in both, whereas what is recovered differs.",
 ["1 mark: the distinction — elastic deformation stores the whole area as recoverable energy, whereas plastic deformation dissipates part of it, so the stored energy is less than the work done; both cases named."]))

# --- OBJ 6.2-03 (energy from area)
A(flash("ITEM-9702-6-024-INTERP", O["23"], "INTERP", ["AO2"], "Determine", 2, 3, "Analyse",
 ["CLM-9702-6-024", "CLM-9702-6-023", "CLM-9702-6-025"],
 "A force–extension graph for a spring is a straight line from the origin passing through (0.020 m, 5.0 N). Determine the elastic potential energy stored in the spring at that extension.",
 "The line is straight through the origin, so the spring is within its limit of proportionality and the stored energy is the triangular area. 5.0 × 0.020 = 0.10, and 0.10 ÷ 2 = 0.050, so the elastic potential energy stored is 0.050 J.",
 ["Reading the graph: the triangular area under the straight line, height 5.0 N and base 0.020 m — 1 mark.",
  "What the value means: within the limit of proportionality the area represents the stored energy, so it gives 0.050 J — 1 mark."]))
A(flash("ITEM-9702-6-025-INTERP", O["23"], "INTERP", ["AO2"], "Determine", 2, 3, "Analyse",
 ["CLM-9702-6-024", "CLM-9702-6-023"],
 "A wire loaded within its limit of proportionality has a force of 60 N at an extension of 1.2 mm. Determine the elastic potential energy stored in the wire.",
 "Convert first: the extension is 1.2 × 10⁻³ m. The stored energy is the triangular area under the straight line: 60 × 1.2 = 72, and the power of ten gives 72 × 10⁻³; halving, 72 ÷ 2 = 36, so the energy stored is 36 × 10⁻³ J, which is 0.036 J to two significant figures.",
 ["Reading the values: the force 60 N and the extension 1.2 × 10⁻³ m as the height and base of the triangle under the graph — 1 mark.",
  "What the area gives: within the limit of proportionality it represents the stored energy, so the result is 0.036 J — 1 mark."]))
A(flash("ITEM-9702-6-026-CALC", O["23"], "CALC", ["AO2"], "Calculate", 2, 3, "Apply",
 ["CLM-9702-6-025", "CLM-9702-6-024", "CLM-9702-6-009"],
 "A spring stretches 0.080 m under a load of 20 N, within its limit of proportionality. Calculate the elastic potential energy stored in the spring.",
 "First the spring constant: k = F ÷ x, and 20 ÷ 0.080 = 250, so k = 250 N m⁻¹. Then the stored energy: EP = ½kx². x² = 0.080 × 0.080 = 0.0064 m², and 250 × 0.0064 = 1.6, so half of that is 0.80. The elastic potential energy stored is 0.80 J to two significant figures.",
 ["Equation and substitution: k = F ÷ x found first, then EP = ½kx² with the substitution shown — 1 mark.",
  "Final answer: 0.80 J with its unit and two significant figures — 1 mark. Using ½Fx directly also reaches 0.80 J, the same area under the graph."]))
A(flash("ITEM-9702-6-027-APP", O["23"], "APP", ["AO2"], "Explain", 1, 3, "Apply",
 ["CLM-9702-6-026", "CLM-9702-6-025"],
 "A bow stores 25 J of elastic potential energy when its string is drawn 0.50 m, within the limit of proportionality of the bow’s spring action. Explain why the archer’s pulling force is not constant during the draw, and where the 25 J comes from.",
 "In this situation the bow behaves as a spring within its limit of proportionality, so the force rises from zero in step with the extension: at half the draw the force is half its final value. The 25 J is the work done by that growing force — the area under the force–extension triangle — which is why it equals ½Fx, half the product of the final force and the draw. A constant force of the final size would store twice as much, because its graph would be a rectangle, not a triangle.",
 ["1 mark: the reason for the situation given — the force grows from zero with the extension, so the stored 25 J comes from the triangular area ½Fx; therefore the energy is half of Fx, because the average force during the draw is half the final force."]))
A(flash("ITEM-9702-6-041-FEATURE", O["23"], "FEATURE", ["AO1"], "State", 1, 4, "Remember",
 ["CLM-9702-6-025", "CLM-9702-6-026"],
 "State two features of the formula EP = ½Fx = ½kx² that limit where it may be used.",
 "It applies only while the deformation is within the limit of proportionality, where the force–extension graph is a straight line through the origin; beyond it the graph curves and the triangular area the formula assumes is gone. And it presumes the force grows from zero, which is where the half comes from: the average force is half the final force. Both features are properties of the proportionality itself, not of the units.",
 ["1 mark: two stated features — validity within the limit of proportionality only, and the ½ arising because the force rises from zero so the area is a triangle."]))
A(flash("ITEM-9702-6-051-DIST", O["23"], "DIST", ["AO1"], "State", 1, 4, "Understand",
 ["CLM-9702-6-026", "CLM-9702-6-023"],
 "State the difference between Fx and ½Fx as measures of the work done on a spring stretched within its limit of proportionality.",
 "Fx is the work a constant force F would do over the extension x — the area of a rectangle under a horizontal line. For the spring the force grows from zero in step with the extension, so the graph is a triangle and the work is ½Fx, half the rectangle: the average force during the stretch is half the final force. Both products carry the unit J when F is in N and x in m, whereas only the second describes the spring within its limit of proportionality.",
 ["1 mark: the distinction — Fx suits a constant force (rectangular area), whereas ½Fx suits the spring whose force grows from zero (triangular area), so the work done on the spring is half of Fx."]))

# --- OBJ 6.2-04 (EP formulas)
A(flash("ITEM-9702-6-028-DEF", O["24"], "DEF", ["AO1"], "Define", 1, 2, "Remember",
 ["CLM-9702-6-025", "CLM-9702-6-024"],
 "Define the elastic potential energy of a stretched spring, giving its formula and unit.",
 "The elastic potential energy is the work done to deform the spring within its limit of proportionality, stored and recovered on unloading: the area under the force–extension graph, EP = ½Fx = ½kx², with F in N, x in m, k in N m⁻¹, and the energy in joules (J).",
 ["1 mark: the definition as stored work — the area under the graph within the limit of proportionality — with the equation ½Fx = ½kx² and the unit J named."]))
A(flash("ITEM-9702-6-029-CALC", O["24"], "CALC", ["AO2"], "Calculate", 2, 2, "Apply",
 ["CLM-9702-6-025"],
 "A spring of spring constant 150 N m⁻¹ is stretched 0.12 m, within its limit of proportionality. Calculate the elastic potential energy stored.",
 "EP = ½kx². First x² = 0.12 × 0.12 = 0.0144 m². Then 150 × 0.0144 = 2.16, and half of that is 1.08, so the stored energy is 1.08 J, which is 1.1 J to two significant figures.",
 ["Equation and substitution: EP = ½kx² with the square taken first — 1 mark.",
  "Final answer: 1.1 J with its unit and two significant figures — 1 mark. Forgetting the half gives 2.2 J, double the stored energy."]))
A(flash("ITEM-9702-6-030-CALC", O["24"], "CALC", ["AO2"], "Calculate", 2, 2, "Apply",
 ["CLM-9702-6-025"],
 "A load of 24 N produces an extension of 0.15 m in a spring, within its limit of proportionality. Calculate the elastic potential energy stored, using EP = ½Fx.",
 "EP = ½Fx. Substitution: 24 × 0.15 = 3.6, and half of that is 1.8, so the stored energy is 1.8 J to two significant figures.",
 ["Equation and substitution: EP = ½Fx with F = 24 N and x = 0.15 m — 1 mark.",
  "Final answer: 1.8 J with its unit and two significant figures — 1 mark. Using Fx without the half gives 3.6 J, which treats the force as constant."]))
A(flash("ITEM-9702-6-031-CALC", O["24"], "CALC", ["AO2"], "Calculate", 2, 2, "Apply",
 ["CLM-9702-6-025"],
 "The spring in a door catch has a spring constant of 2.5 × 10³ N m⁻¹ and stores 0.31 J when compressed, within its limit of proportionality. Calculate the compression.",
 "Rearranged: x² = 2EP ÷ k. First 2 × 0.31 = 0.62, then 0.62 ÷ 2500 = 0.000248, so x² = 2.48 × 10⁻⁴ m². The square root of 0.000248 is 0.0157, so the compression is 0.0157 m, which is 16 mm to two significant figures.",
 ["Equation and substitution: x² = 2EP ÷ k rearranged from ½kx² — 1 mark.",
  "Final answer: 16 mm with its unit and two significant figures — 1 mark. Halting before the square root leaves m², the wrong unit for a length."]))
A(flash("ITEM-9702-6-037-MISCON", O["24"], "MISCON", ["AO1"], "Explain", 1, 3, "Understand",
 ["CLM-9702-6-027", "CLM-9702-6-025"],
 "A spring stores 0.40 J when stretched 0.10 m within its limit of proportionality. A learner says stretching it to 0.20 m will store 0.80 J. Explain the error.",
 "The expectation assumes the force stays at its old value while the extension doubles. In fact F = kx, so doubling the extension doubles the final force as well, and EP = ½kx² carries both factors: the stored energy is multiplied by four — 0.40 × 4 = 1.6 — giving 1.6 J, not 0.80 J. The test: does the force stay the same as the extension grows? Within the limit of proportionality it does not.",
 ["1 mark: the error named — expecting double the extension to give double the energy; in fact the force doubles too, so ½kx² quadruples the stored energy to 1.6 J instead of doubling it."],
 mc="MC-9702-6-06"))
A(flash("ITEM-9702-6-047-FEATURE", O["24"], "FEATURE", ["AO1"], "State", 1, 3, "Remember",
 ["CLM-9702-6-025", "CLM-9702-6-027"],
 "State two features of the elastic potential energy stored in a spring stretched within its limit of proportionality.",
 "It equals the area under the force–extension graph, a triangle of height F and base x, and so is given by EP = ½Fx = ½kx² in joules. And it grows as the square of the extension: double the stretch stores four times the energy, because the force doubles with it. Both features hold only within the limit of proportionality.",
 ["1 mark: two stated features — the energy is the triangular area ½Fx = ½kx² in J, and it quadruples when the extension doubles because the force grows with the stretch."]))
A(flash("ITEM-9702-6-057-DIST", O["24"], "DIST", ["AO1"], "State", 1, 3, "Understand",
 ["CLM-9702-6-025", "CLM-9702-6-024", "CLM-9702-6-019"],
 "State the difference between the work done by the load and the energy stored in the spring when the deformation is elastic, and what changes when it is plastic.",
 "In elastic deformation the work done by the load equals the elastic potential energy stored: all of it is recovered on unloading. In plastic deformation the work done still equals the area under the loading graph, but part of it is dissipated in the permanent change of shape, so the stored energy is less than the work done. The difference between the two quantities is zero while the deformation is elastic, whereas once it is plastic the difference is the dissipated part.",
 ["1 mark: the distinction — elastic deformation stores all the work done as recoverable energy, whereas plastic deformation dissipates part of it, so the stored energy is then less than the work done; both cases named."]))

# --- performance tasks
P01 = {
 "item_id": "ITEM-9702-6-P01",
 "objective_ids": [O["14"], O["15"], O["21"], O["24"]],
 "claim_ids": ["CLM-9702-6-009", "CLM-9702-6-010", "CLM-9702-6-011", "CLM-9702-6-015",
               "CLM-9702-6-019", "CLM-9702-6-021", "CLM-9702-6-023", "CLM-9702-6-025", "CLM-9702-6-027"],
 "item_type": "multiple_choice_set", "subtype": None,
 "assessment_objectives": ["AO1", "AO2"], "blooms_level": "Apply", "command_word": None,
 "mark_tariff": 12, "difficulty": 3,
 "prompt": ("Twelve questions. Choose one option for each.\n\n"
  "1. Which quantity is defined as the force per unit cross-sectional area of a wire?\n"
  "A  strain\nB  stress\nC  the Young modulus\nD  the spring constant\n\n"
  "2. A spring of original length 0.30 m is 0.38 m long under a load. What value is its extension?\n"
  "A  0.38 m\nB  0.30 m\nC  0.080 m\nD  0.68 m\n\n"
  "3. What is 1 mm² in square metres?\n"
  "A  1 × 10⁻³ m²\nB  1 × 10⁻⁶ m²\nC  1 × 10⁻⁹ m²\nD  1 × 10⁻² m²\n\n"
  "4. A wire of cross-sectional area 1.5 mm² carries a force of 30 N. What is the stress in the wire?\n"
  "A  2.0 × 10⁷ Pa\nB  2.0 × 10⁴ Pa\nC  5.0 × 10⁻⁸ Pa\nD  45 Pa\n\n"
  "5. Which quantity has no unit?\n"
  "A  stress\nB  strain\nC  the Young modulus\nD  the spring constant\n\n"
  "6. Two identical springs, each of spring constant k, are joined end to end. What is the spring constant of the pair?\n"
  "A  2k\nB  k\nC  k/2\nD  k/4\n\n"
  "7. A spring stretches 0.060 m under a load of 3.0 N. What is its spring constant?\n"
  "A  0.020 N m⁻¹\nB  20 N m⁻¹\nC  50 N m⁻¹\nD  0.50 N m⁻¹\n\n"
  "8. Beyond the limit of proportionality of a wire:\n"
  "A  it does not return to its original shape when unloaded\n"
  "B  the force is no longer proportional to the extension\n"
  "C  the spring constant becomes zero\n"
  "D  no further extension is possible\n\n"
  "9. A wire is stretched beyond its elastic limit and the load is then removed. What happens to the wire?\n"
  "A  It returns to its original length.\nB  It keeps a permanent extension.\n"
  "C  It springs back shorter than its original length.\nD  It stores all the work done as elastic potential energy.\n\n"
  "10. A spring of spring constant 80 N m⁻¹ is stretched 0.10 m, within its limit of proportionality. What energy is stored?\n"
  "A  8.0 J\nB  0.40 J\nC  0.80 J\nD  4.0 J\n\n"
  "11. The same spring is stretched 0.20 m instead. Compared with the energy at 0.10 m, the stored energy is now:\n"
  "A  twice as much\nB  four times as much\nC  half as much\nD  the same\n\n"
  "12. The area under a force–extension graph up to the elastic limit represents:\n"
  "A  the spring constant\nB  the work done by the load\nC  the stress\nD  the elastic limit itself"),
 "canonical_answer": (
  "Key: 1 B, 2 C, 3 B, 4 A, 5 B, 6 C, 7 C, 8 B, 9 B, 10 B, 11 B, 12 B.\n"
  "1. Stress is force per unit cross-sectional area (B). A confuses stress with strain, the error the register records; C goes one step further to the modulus, stress ÷ strain; D is force per unit extension instead of per unit area.\n"
  "2. Extension is stretched length minus original length: 0.38 − 0.30 = 0.080 m (C). A uses the stretched length in place of the extension, the length-for-extension error; B uses the original length; D adds the two lengths together.\n"
  "3. The millimetre is squared, so the conversion factor is squared: 1 mm² = 1 × 10⁻⁶ m² (B). A uses 10⁻³, the linear conversion instead of the squared one; C cubes the factor; D shifts the power the wrong way.\n"
  "4. 30 ÷ 1.5 = 20, and the 10⁻⁶ of the area gives 2.0 × 10⁷ Pa (A). B divides by 1.5 × 10⁻³, the linear-conversion error; C inverts the fraction, dividing the area by the force; D multiplies instead of dividing.\n"
  "5. Strain is a ratio of two lengths, so it has no unit (B). A and C give Pa, the unit of stress and of the Young modulus; D gives N m⁻¹, the unit of a spring constant.\n"
  "6. End to end, each spring carries the whole load and the extensions add, so the pair has half the constant, k/2 (C). A adds the constants, the treatment for springs joined side by side; B assumes nothing changes; D squares instead of halving.\n"
  "7. k = F ÷ x, and 3.0 ÷ 0.060 = 50 N m⁻¹ (C). A inverts the division and misplaces the unit; B divides 1.2 by 0.060 after misreading the data; D divides by 6.0 instead of 0.060, a power-of-ten slip.\n"
  "8. Beyond the limit of proportionality the force is no longer proportional to the extension (B). A describes the elastic limit, treating the two points as the same — the confusion the register records; C invents a zero constant; D contradicts the graph, which keeps rising.\n"
  "9. Beyond the elastic limit the deformation is plastic, so the wire keeps a permanent extension (B). A describes elastic deformation, which returns to the original length; C invents an overshoot; D forgets that part of the work is dissipated in the plastic deformation.\n"
  "10. EP = ½kx², and 80 × 0.0100 = 0.80, so half of that is 0.40 J (B). A uses kx, missing the square of the extension; C uses kx² and forgets the half; D uses half of kx, missing the square.\n"
  "11. ½kx² quadruples when x doubles, so four times as much (B). A is the expectation that double the extension gives double the energy, the error the register records; C has the energy falling as the spring is stretched further; D forgets that the force grows with the extension.\n"
  "12. The area under the force–extension graph represents the work done by the load (B). A confuses the area with the gradient, which gives the spring constant; C reads an axis quantity, not an area; D names a point on the graph, not an area."),
 "marking_guidance": [
  "The key with its reason: one mark per question, the correct option justified against each distractor.",
  "Every distractor is a named error, drawn from the misconception register first: the length-for-extension slip, the unsquared mm² conversion, the linear-conversion error, adding series constants, the limit-of-proportionality confusion, and the double-for-double energy expectation."
 ],
 "context": dict(CTX), "prerequisite_item_ids": [], "core_status": "core",
 "intentional_duplicate_group": None,
 "provenance": "Authored for CIE 9702 AS Physics topic 6 from the topic claim ledger and work order.",
 "qa_status": "review_required",
 "claims_seen": {c: 1 for c in ["CLM-9702-6-009", "CLM-9702-6-010", "CLM-9702-6-011", "CLM-9702-6-015",
               "CLM-9702-6-019", "CLM-9702-6-021", "CLM-9702-6-023", "CLM-9702-6-025", "CLM-9702-6-027"]},
}

P01["authored_hash"] = H(P01)
ITEMS.append(P01)

P02 = {
 "item_id": "ITEM-9702-6-P02",
 "objective_ids": [O["12"], O["14"], O["21"], O["24"]],
 "claim_ids": ["CLM-9702-6-003", "CLM-9702-6-006", "CLM-9702-6-009", "CLM-9702-6-019", "CLM-9702-6-021", "CLM-9702-6-025"],
 "item_type": "short_answer", "subtype": None,
 "assessment_objectives": ["AO1", "AO2"], "blooms_level": "Apply", "command_word": "State",
 "mark_tariff": 8, "difficulty": 3,
 "prompt": ("A trader at a market in Oshakati weighs bags of maize with a spring scale. The scale’s spring has natural "
  "length 0.150 m and spring constant 240 N m⁻¹, and the scale is used within its limit of proportionality.\n"
  "(a) State what is meant by the extension of the spring. [1]\n"
  "(b) A bag of maize of mass 3.6 kg hangs at rest on the scale. Calculate the extension of the spring. Use g = 9.81 N kg⁻¹. [2]\n"
  "(c) The scale is overloaded once and the spring does not return to its original length when the load is removed. "
  "State the term for the change of shape the spring has undergone, and the name of the point beyond which that change begins. [2]\n"
  "(d) Calculate the elastic potential energy stored in the spring at the extension found in (b). [2]\n"
  "(e) Explain why the scale no longer reads zero when it is unloaded. [1]"),
 "canonical_answer": (
  "(a) The extension is the increase in the spring’s length from its original length: the stretched length minus the original length, in m.\n"
  "(b) The load is the weight of the bag: F = mg. Substitution: 3.6 × 9.81 = 35.256 N, which is 35.3 N to three significant figures. Then x = F ÷ k: 35.3 ÷ 240 = 0.14708, so the extension is 0.147 m to three significant figures.\n"
  "(c) The spring has undergone plastic deformation, a permanent change of shape; that change begins beyond the elastic limit.\n"
  "(d) EP = ½Fx. Substitution: 35.3 × 0.147 = 5.19, and half of that is 2.60, so the stored energy is 2.6 J to two significant figures.\n"
  "(e) Because the deformation was plastic, the spring keeps a permanent extension: with no load it now rests longer than its original length, so the pointer’s zero has shifted and every reading is offset."),
 "marking_guidance": [
  "Part (a): 1 mark for the meaning of extension as the increase in length from the original length.",
  "Part (b): 2 marks — the equation F = kx rearranged with the weight F = mg substituted, 1 mark for the working; the answer 0.147 m with its unit, 1 mark.",
  "Part (c): 2 marks — one point for the term plastic deformation and one because the change begins beyond the elastic limit.",
  "Part (d): 2 marks — the equation EP = ½Fx or ½kx² with the substitution, 1 mark; the answer 2.6 J with its unit, 1 mark.",
  "Part (e): 1 mark — because the plastic deformation is permanent, the spring’s zero has shifted, so the readings are offset."],
 "context": dict(CTX), "prerequisite_item_ids": [], "core_status": "core",
 "intentional_duplicate_group": None,
 "provenance": "Authored for CIE 9702 AS Physics topic 6 from the topic claim ledger and work order.",
 "qa_status": "review_required",
 "claims_seen": {c: 1 for c in ["CLM-9702-6-003", "CLM-9702-6-006", "CLM-9702-6-009", "CLM-9702-6-019", "CLM-9702-6-021", "CLM-9702-6-025"]},
}
P02["authored_hash"] = H(P02)
ITEMS.append(P02)

P03 = {
 "item_id": "ITEM-9702-6-P03",
 "objective_ids": [O["15"], O["16"]],
 "claim_ids": ["CLM-9702-6-011", "CLM-9702-6-012", "CLM-9702-6-015"],
 "item_type": "calculation", "subtype": None,
 "assessment_objectives": ["AO1", "AO2"], "blooms_level": "Apply", "command_word": "Calculate",
 "mark_tariff": 5, "difficulty": 3,
 "prompt": ("A steel wire 2.4 m long ties a solar-panel frame to a post on a farm near Gobabeb. The wire has a diameter "
  "of 0.60 mm. In a gust the wire carries a force of 45 N, within its limit of proportionality. The Young modulus "
  "of steel is 2.0 × 10¹¹ Pa. Calculate (a) the cross-sectional area of the wire in m², (b) the stress in the wire, "
  "(c) the strain of the wire, and (d) the extension of the wire in mm, stating to how many significant figures you give it. [5]"),
 "canonical_answer": (
  "(a) Convert the diameter first: d = 0.60 mm = 0.60 × 10⁻³ m, so d² = 0.36 × 10⁻⁶ m². Then A = πd² ÷ 4: "
  "3.142 × 0.36 = 1.131, and 1.131 ÷ 4 = 0.2828, so A = 0.2828 × 10⁻⁶ m², which is 2.8 × 10⁻⁷ m² to two significant figures.\n"
  "(b) Stress: σ = F ÷ A. Substitution: 45 ÷ 2.828 = 15.91, so the stress is 15.91 × 10⁷ Pa, which is 1.6 × 10⁸ Pa to two significant figures.\n"
  "(c) Strain: ε = σ ÷ E. Substitution: 15.91 ÷ 2.0 = 7.955, so the strain is 7.955 × 10⁻⁴, which is 8.0 × 10⁻⁴ to two significant figures.\n"
  "(d) Extension: x = strain × L. Substitution: 7.955 × 2.4 = 19.09, so x = 19.09 × 10⁻⁴ m, which is 1.9 mm to two significant figures — the same precision as the data."),
 "marking_guidance": [
  "Equation: A = πd² ÷ 4 with the diameter converted to metres before squaring — 1 mark.",
  "Substitution and working: σ = F ÷ A and ε = σ ÷ E, each intermediate value carried to at least three significant figures — 1 mark.",
  "Substitution for the extension: x = strain × original length, with the original 2.4 m used — 1 mark.",
  "Answer: 1.9 mm with its unit — 1 mark.",
  "Answer stated to two significant figures, justified because the data (0.60 mm, 45 N, 2.0 × 10¹¹ Pa) are given to two — 1 mark."],
 "context": dict(CTX), "prerequisite_item_ids": [], "core_status": "core",
 "intentional_duplicate_group": None,
 "provenance": "Authored for CIE 9702 AS Physics topic 6 from the topic claim ledger and work order.",
 "qa_status": "review_required",
 "claims_seen": {c: 1 for c in ["CLM-9702-6-011", "CLM-9702-6-012", "CLM-9702-6-015"]},
}
P03["authored_hash"] = H(P03)
ITEMS.append(P03)

# ---------------------------------------------------------------- write
def dump(path, obj):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(obj, fh, indent=1, ensure_ascii=False)
        fh.write("\n")

ledger = {"ledger_id": "CLM-LEDGER-9702-6", "claims": CLAIMS}
dump(os.path.join(TD, "claims/canonical_claim_ledger.json"), ledger)
dump(os.path.join(TD, "content-units/CU-9702-6.1.json"), UNIT61)
dump(os.path.join(TD, "content-units/CU-9702-6.2.json"), UNIT62)
dump(os.path.join(TD, "learning-items/topic_6_items.json"),
     {"dataset_id": "ITEMS-9702-6", "topic_id": "6", "items": ITEMS})

# ---------------------------------------------------------------- self-checks
ids = [i["item_id"] for i in ITEMS]
assert len(ITEMS) == 61, len(ITEMS)
assert len(set(ids)) == 61
cmap = {c["claim_id"]: set(c["objective_ids"]) for c in CLAIMS}
bad = []
for i in ITEMS:
    served = set()
    for c in i["claim_ids"]:
        served |= cmap.get(c, set())
    for o in i["objective_ids"]:
        if o not in served:
            bad.append((i["item_id"], o))
assert not bad, bad
cited = {c for i in ITEMS for c in i["claim_ids"]} | {c for u in (UNIT61, UNIT62) for b in u["blocks"] for c in b["claim_ids"]}
orphans = set(cmap) - cited
assert not orphans, orphans
# every claim cited by an item must be taught in a unit block
taught = {c for u in (UNIT61, UNIT62) for b in u["blocks"] for c in b["claim_ids"]}
unbacked = {c for i in ITEMS for c in i["claim_ids"]} - taught
assert not unbacked, unbacked
# word budgets
for u in (UNIT61, UNIT62):
    lo, hi = u["word_budget"]["min"], u["word_budget"]["max"]
    print(u["unit_id"], "words:", u["word_count"], "budget", lo, "-", hi,
          "OK" if lo <= u["word_count"] <= hi else "OUT")
print("claims:", len(CLAIMS), "items:", len(ITEMS))
print("BUILD OK")
