#!/usr/bin/env python3
"""Authoring build for topic 3 (Dynamics) of CIE 9702 AS Physics.

Writes claims/canonical_claim_ledger.json, content-units/CU-9702-3.{1,2,3}.json,
learning-items/topic_3_items.json and authoring_notes.json under this directory.
Hashes are computed with the standard's own _artefact_text so C-30 verifies.
"""
import json, os, sys, hashlib

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, '..', '..', '..', '..'))
sys.path.insert(0, os.path.join(REPO, 'standard', 'v0.2.0-draft', 'checks'))
from yyeni_checks import _artefact_text

PROV = "Authored for CIE 9702 AS Physics topic 3 from the topic claim ledger and work order."
VERIF = {
    "status": "unverified",
    "method": "Authored originally for CIE 9702 AS Physics topic 3 under standard v0.2.0-draft. Requires semantic review (RS-28).",
    "reviewer_id": None,
    "reviewed_at": None,
    "confidence": 0.9,
}

# ---------------------------------------------------------------- claims
# (claim_id, objective_ids, text, claim_type)
C = []
def cl(cid, objs, text, ctype):
    C.append({"claim_id": cid, "objective_ids": objs, "text": text,
              "claim_type": ctype, "provenance": "generated_gap", "evidence": [],
              "derived_from_claim_ids": [], "verification": dict(VERIF),
              "publishable": False, "notes": [], "revision": 1})

cl("CLM-9702-3-001", ["OBJ-9702-3.1-01"],
   "Mass is the property of an object that resists a change in its motion; it is measured in kilograms (kg) and is a scalar.",
   "definition")
cl("CLM-9702-3-002", ["OBJ-9702-3.1-01", "OBJ-9702-3.1-06"],
   "Mass is not weight: mass, in kilograms, is the property that resists change in motion, while weight, in newtons, is the force of a gravitational field on that mass.",
   "comparison")
cl("CLM-9702-3-003", ["OBJ-9702-3.1-01"],
   "Under a fixed resultant force, the acceleration is a = F ÷ m, so a larger mass accelerates less: doubling the mass halves the acceleration.",
   "causal")
cl("CLM-9702-3-004", ["OBJ-9702-3.1-02"],
   "For a body of constant mass, the resultant force F and the acceleration a are linked by F = ma, with F in newtons, m in kilograms and a in m s⁻²; the F is the resultant of every force acting, combined with their directions.",
   "formula")
cl("CLM-9702-3-005", ["OBJ-9702-3.1-02"],
   "The acceleration of a body points in the same direction as the resultant force on it, whatever the direction of the body's velocity; slowing is acceleration against the velocity.",
   "factual")
cl("CLM-9702-3-006", ["OBJ-9702-3.1-02"],
   "F = ma takes the resultant of every force acting on the body, not one force alone: the driving force, the weight or a tension on its own is not F until the other forces have been combined with it.",
   "misconception_correction")
cl("CLM-9702-3-007", ["OBJ-9702-3.1-03"],
   "Linear momentum is the product of the mass and the velocity of a body, p = mv, a vector with unit kg m s⁻¹, written N s; its direction is the direction of the velocity.",
   "definition")
cl("CLM-9702-3-008", ["OBJ-9702-3.1-03"],
   "A change in momentum is a vector change: after a rebound the velocity reverses its sign, so the change in momentum is the sum of the magnitudes of the momenta before and after, not their difference.",
   "misconception_correction")
cl("CLM-9702-3-009", ["OBJ-9702-3.1-04"],
   "Force is defined as the rate of change of momentum, F = ∆p ÷ ∆t, with ∆p in N s and ∆t in seconds; one newton changes the momentum of a body by 1 kg m s⁻¹ each second. For a constant mass this gives F = ma.",
   "definition")
cl("CLM-9702-3-010", ["OBJ-9702-3.1-04"],
   "The change in momentum ∆p, measured in N s, is not itself a force; dividing it by the time taken gives the average resultant force, in newtons.",
   "misconception_correction")
cl("CLM-9702-3-011", ["OBJ-9702-3.1-05"],
   "Newton's first law: a body remains at rest, or continues to move in a straight line at constant velocity, unless a resultant force acts on it; balanced forces leave the state of motion unchanged.",
   "definition")
cl("CLM-9702-3-012", ["OBJ-9702-3.1-05"],
   "Newton's second law: the resultant force on a body is proportional to the rate of change of momentum of the body, and the rate of change of momentum is in the direction of the force; F = ma is the special case for a constant mass.",
   "definition")
cl("CLM-9702-3-013", ["OBJ-9702-3.1-05"],
   "Newton's third law: when one body exerts a force on a second, the second exerts on the first a force equal in size, opposite in direction and of the same type.",
   "definition")
cl("CLM-9702-3-014", ["OBJ-9702-3.1-05"],
   "The two forces of a third-law pair act on two different bodies, so they cannot balance each other on one object; two forces that balance on one object, such as the weight of a book and the table's push on it, are not a third-law pair.",
   "misconception_correction")
cl("CLM-9702-3-015", ["OBJ-9702-3.1-06"],
   "The weight of an object is the force of a gravitational field on it: W = mg, with m in kg, g the acceleration of free fall in m s⁻² (N kg⁻¹) and W in newtons, directed downward.",
   "definition")
cl("CLM-9702-3-016", ["OBJ-9702-3.1-06"],
   "Near the Earth's surface g = 9.81 m s⁻², so each kilogram of mass carries 9.81 N of weight there; the mass of an object is fixed, while its weight varies from place to place as g varies.",
   "factual")
cl("CLM-9702-3-017", ["OBJ-9702-3.1-06"],
   "Mass is measured in kilograms and weight in newtons: a statement that gives a weight in kilograms mixes the two, because a weight is a force and comes from W = mg.",
   "misconception_correction")
cl("CLM-9702-3-018", ["OBJ-9702-3.2-01"],
   "A frictional force acts where two surfaces are in contact, along the surfaces, in the direction that opposes relative sliding or attempted sliding between them.",
   "definition")
cl("CLM-9702-3-019", ["OBJ-9702-3.2-01"],
   "A drag force is the resistive push of a fluid on an object moving through it; it acts against the velocity, and its size increases as the speed increases (air resistance is drag in air).",
   "definition")
cl("CLM-9702-3-020", ["OBJ-9702-3.2-01"],
   "Drag acts against the velocity and depends on the speed; upthrust is the upward push of a fluid that arises from the pressure of the fluid and acts whether the object moves or not - drag is not upthrust.",
   "misconception_correction")
cl("CLM-9702-3-021", ["OBJ-9702-3.2-02"],
   "An object falling from rest in air starts with acceleration g, and as its speed grows the drag grows, so the resultant force (weight minus drag) falls and the acceleration falls below g; in a vacuum the acceleration stays g throughout the fall.",
   "causal")
cl("CLM-9702-3-022", ["OBJ-9702-3.2-02"],
   "A velocity–time graph for a fall through air starts with gradient 9.81 m s⁻² and flattens as the drag grows with speed, ending in a horizontal line where the drag balances the weight and the resultant force is zero.",
   "factual")
cl("CLM-9702-3-023", ["OBJ-9702-3.2-03"],
   "Terminal velocity is the constant velocity a falling object reaches when the drag equals the weight: the forces balance, the resultant force is zero, and both forces still act at full size.",
   "definition")
cl("CLM-9702-3-024", ["OBJ-9702-3.2-03"],
   "A falling object speeds up while its drag is below its weight; the drag rises with the speed until it equals the weight, and then the forces balance, the resultant force is zero and the velocity stays constant.",
   "causal")
cl("CLM-9702-3-025", ["OBJ-9702-3.3-01"],
   "The principle of conservation of momentum: the total momentum of a system stays constant, provided that no resultant external force acts on the system.",
   "definition")
cl("CLM-9702-3-026", ["OBJ-9702-3.3-01"],
   "The principle is about the total momentum of the whole system, and it carries its condition; it is a principle about motion, distinct from the principle of moments, which is about turning effects.",
   "misconception_correction")
cl("CLM-9702-3-027", ["OBJ-9702-3.3-02"],
   "In one dimension, momentum problems are solved by choosing a positive direction, giving every velocity its sign, and equating the total momentum before the interaction to the total momentum after: m1u1 + m2u2 = m1v1 + m2v2.",
   "procedural")
cl("CLM-9702-3-028", ["OBJ-9702-3.3-02"],
   "In two dimensions, the total momentum of a system is conserved separately in each of two perpendicular directions, so each direction gives its own equation, and an unknown velocity is found from its components.",
   "procedural")
cl("CLM-9702-3-029", ["OBJ-9702-3.3-03"],
   "In an elastic collision, the total kinetic energy of the system is conserved and the relative speed of approach of the two objects equals their relative speed of separation.",
   "definition")
cl("CLM-9702-3-030", ["OBJ-9702-3.3-03"],
   "Kinetic energy is conserved in a collision when the collision is elastic; momentum is conserved in the interaction whether the collision is elastic or inelastic.",
   "misconception_correction")
cl("CLM-9702-3-031", ["OBJ-9702-3.3-04"],
   "The total momentum of a system stays constant in an interaction between its objects, while its total kinetic energy may fall, transferring to other stores; that fall is what makes the interaction inelastic.",
   "factual")
cl("CLM-9702-3-032", ["OBJ-9702-3.3-02"],
   "A change in kinetic energy is found by squaring each speed on its own: ∆Ek = ½mv² − ½mu²; the squared difference ½m(v − u)² is not the energy change.",
   "misconception_correction")
cl("CLM-9702-3-033", ["OBJ-9702-3.3-04"],
   "The pushes two objects give each other in an interaction are equal in size and opposite in direction, so the momentum one object gains equals the momentum the other loses, and the vector total stays constant.",
   "causal")

CLAIM_TEXTS = {c["claim_id"]: c["text"] for c in C}

# ---------------------------------------------------------------- content units
def blk(bid, btype, heading, text, claims, aos):
    return {"block_id": bid, "block_type": btype, "heading": heading, "text": text,
            "claim_ids": claims, "context_tags": [], "assessment_objectives": aos,
            "claims_seen": {c: 1 for c in claims},
            "authored_hash": hashlib.sha256(_artefact_text({"heading": heading, "text": text}).encode()).hexdigest()}

U31_BLOCKS = [
blk("3.1-b1", "learner_objective", "What this section covers",
    "Mass as the property that resists change in motion; the equation F = ma and the fact that acceleration and resultant force point the same way; linear momentum as mass × velocity; force as the rate of change of momentum; Newton's three laws of motion, stated and used; and weight as the force of a gravitational field on a mass, W = mg.", [], ["AO1"]),
blk("3.1-b2", "definition", "Mass",
    "Mass is the property of an object that resists a change in its motion. It is measured in kilograms (kg) and is a scalar: an object carries the same mass on the B1 road, at the bottom of a borehole and on the Moon. The push that sets an empty donkey cart rolling will barely shift the same cart loaded with maize meal, because the loaded cart has more mass and so resists the change more. Under a fixed resultant force the acceleration is a = F ÷ m, so doubling the mass halves the acceleration: a 240 kg steel drum needs twenty times the force of a 12 kg drum to reach the same acceleration. Mass resists a change in motion in both directions: it makes stopping harder as well as starting, which is why a heavy lorry is harder to slow than a car at the same speed.",
    ["CLM-9702-3-001", "CLM-9702-3-003"], ["AO1"]),
blk("3.1-b3", "plain_explanation", "Mass is not weight",
    "Mass and weight are different quantities with different units. Mass, in kilograms, is the property that resists a change in motion; weight, in newtons, is the force a gravitational field exerts on that mass. A 25 kg bag of cement keeps its 25 kg everywhere, while its weight is smaller on the Moon than at the coast. The test is the unit: a quantity in kilograms is a mass, and a quantity in newtons is a force, so a label that reads 'weighs 25 kg' is giving the mass, because a weight cannot be measured in kilograms. Mixing the two is a common error: weight must be calculated as W = mg before it can enter an equation of forces.",
    ["CLM-9702-3-002", "CLM-9702-3-017"], ["AO1"]),
blk("3.1-b4", "formula", "The equation F = ma",
    "For a body of constant mass, the resultant force F on the body and its acceleration a are linked by F = ma, where F is measured in newtons (N), m in kilograms (kg) and a in metres per second squared (m s⁻²). The F in this equation is the resultant of every force acting on the body, found by combining all of them with their directions. An engine's driving force on a minibus is not the force that accelerates it: the driving force, the drag and any frictional force must be combined first, and the resultant goes into F = ma. Prefixes are converted before the substitution: a resultant force of 3.0 kN on a 1200 kg vehicle means F = 3000 N, and a = 3000 ÷ 1200 = 2.5 m s⁻².",
    ["CLM-9702-3-004", "CLM-9702-3-006"], ["AO1"]),
blk("3.1-b5", "plain_explanation", "Force and acceleration point the same way",
    "Acceleration is a vector, and it points in the same direction as the resultant force, whatever the body's velocity happens to be. When a taxi brakes, its velocity is still forward while the resultant force, and so the acceleration, points backwards; the speed falls because acceleration and velocity point in opposite directions. A body that speeds up has acceleration along its velocity; a body that slows has acceleration against it. Reverse the direction of the resultant force and the acceleration reverses with it.",
    ["CLM-9702-3-005"], ["AO1"]),
blk("3.1-b6", "worked_calculation", "Worked example: a taxi pulling away",
    "A minibus taxi of mass 1800 kg pulls away from a rank in Otjiwarongo and reaches 20 m s⁻¹ in 8.0 s. The acceleration comes first: a = ∆v ÷ ∆t = 20 ÷ 8.0 = 2.5 m s⁻². Then F = ma, so the resultant force is 1800 × 2.5 = 4500 N. Notice the plan: kinematics gives the acceleration, and F = ma turns it into a force. The answer of 4500 N is the resultant of the driving force and the resistive forces together, so the engine itself pushes with more than 4500 N.",
    ["CLM-9702-3-004"], ["AO2"]),
blk("3.1-b7", "worked_calculation", "Worked example: forces in opposite directions",
    "A boat of mass 600 kg crossing the Hardap Dam has a propeller driving force of 1200 N and, at one moment, a drag from the water of 450 N. The two forces oppose, so the resultant is 1200 − 450 = 750 N, and a = F ÷ m = 750 ÷ 600 = 1.25 m s⁻². If the drag were equal in size to the driving force, the resultant would be zero and the acceleration would be zero, whatever the speed: a steady speed needs no resultant force at all, which is what the first law says.",
    ["CLM-9702-3-004", "CLM-9702-3-006"], ["AO2"]),
blk("3.1-b8", "definition", "Linear momentum",
    "The linear momentum of a body is the product of its mass m and its velocity v: p = mv, where p is momentum in kilograms metres per second (kg m s⁻¹), also written N s, m in kilograms and v in metres per second. Momentum is a vector: its direction is the direction of the velocity. A minibus of mass 1800 kg moving at 12 m s⁻¹ carries a momentum of 21600 kg m s⁻¹ along the road, and the same minibus reversing at 12 m s⁻¹ carries a momentum of the same size in the opposite direction. The word momentum on its own means this quantity of motion, not a turning effect.",
    ["CLM-9702-3-007"], ["AO1"]),
blk("3.1-b9", "worked_calculation", "Worked example: momentum on the road",
    "A loaded truck of mass 3000 kg rolls at 15 m s⁻¹; a cyclist of total mass 70 kg rides at 5.0 m s⁻¹. Truck: p = mv = 3000 × 15 = 45000 kg m s⁻¹. Cyclist: p = 70 × 5.0 = 350 kg m s⁻¹. Both momenta point along the direction of travel. If the truck and the cyclist travel in opposite directions, their momenta point in opposite directions too, and when a total is needed the signs matter: 45000 east and 350 west give a total of 44650 east, not 45350.",
    ["CLM-9702-3-007"], ["AO2"]),
blk("3.1-b10", "misconception", "Rebounds: the change is a vector change",
    "A common error treats momentum as a size that can be subtracted. Momentum is a vector, so a change in momentum is found from velocities with their signs. A ball of mass 0.20 kg arriving at a wall at 6.0 m s⁻¹ and leaving at 4.0 m s⁻¹ changes its momentum by 0.20 × 6.0 + 0.20 × 4.0 = 2.0 N s, because the reversal of direction means the magnitudes of the two momenta add. The test is whether the object reversed its direction: when it did, the change in momentum is the sum of the magnitudes, and subtracting them leaves out the reversal.",
    ["CLM-9702-3-008"], ["AO1"]),
blk("3.1-b11", "definition", "Force as rate of change of momentum",
    "Force is defined as the rate of change of momentum: F = ∆p ÷ ∆t, where ∆p is the change in momentum in N s (kg m s⁻¹) and ∆t is the time over which it happens, in seconds (s). One newton is the force that changes the momentum of a body by 1 kg m s⁻¹ each second. When the mass stays constant, ∆p = m∆v, so F = m∆v ÷ ∆t = ma, and the definition collapses to F = ma. Keep the two quantities apart: ∆p, the change in momentum, is measured in N s, while ∆p divided by the time is a force, in newtons. An answer in N s is not yet a force; the division by time has to happen.",
    ["CLM-9702-3-009", "CLM-9702-3-010"], ["AO1"]),
blk("3.1-b12", "worked_calculation", "Worked example: catching a cricket ball",
    "A cricket ball of mass 0.16 kg reaches a fielder at 35 m s⁻¹ and is brought to rest in the gloves in 0.12 s. The change in momentum is ∆p = 0.16 × 35 = 5.6 N s. The force is the rate of change: F = ∆p ÷ ∆t = 5.6 ÷ 0.12 = 46.7 N, so about 47 N. By pulling the hands back while catching, a fielder stretches ∆t and so reduces ∆p ÷ ∆t for the same ∆p: the same momentum change, delivered over a longer time, needs a smaller force.",
    ["CLM-9702-3-009"], ["AO2"]),
blk("3.1-b13", "definition", "Newton's first law",
    "Newton's first law of motion states that a body remains at rest, or continues to move in a straight line at constant velocity, unless a resultant force acts on it. A suitcase standing in the aisle of a moving minibus lurches forward when the driver brakes, because with nothing holding it, no horizontal force acts to slow it with the vehicle. Balanced forces are as good as no force for this law: a crate hanging motionless on a crane cable has weight and tension pulling equally in opposite directions, the resultant is zero, and the crate keeps its state of rest.",
    ["CLM-9702-3-011"], ["AO1"]),
blk("3.1-b14", "definition", "Newton's second law",
    "Newton's second law of motion states that the resultant force on a body is proportional to the rate of change of momentum of the body, and that the rate of change of momentum is in the direction of the force. For a body of constant mass this gives F = ma at once, because the rate of change of momentum is then m times the acceleration. The law itself is the statement about momentum: quoting F = ma as the law drops the physics it rests on. The law also shows why a fixed force gives a heavy load a smaller acceleration, and why the same force acting for the same time produces the same change of momentum, whatever mass it meets.",
    ["CLM-9702-3-012"], ["AO1"]),
blk("3.1-b15", "definition", "Newton's third law",
    "Newton's third law of motion states that when one body exerts a force on a second body, the second body exerts on the first a force that is equal in size, opposite in direction, and of the same type. The push of a shoe on gravel is paired with the push of the gravel on the shoe; the pull of the Earth on a hanging crate is paired with the pull of the crate on the Earth. Both forces of a pair appear together and disappear together: each force is one half of a pair.",
    ["CLM-9702-3-013"], ["AO1"]),
blk("3.1-b16", "misconception", "A third-law pair does not cancel on one body",
    "Two forces that balance on one object are not a third-law pair. The weight of a book and the table's upward push on it both act on the book, and they cancel - but a third-law pair acts on two different bodies, so the two forces of a pair cannot cancel each other. The book's weight is paired with the book's pull on the Earth, and the table's push with the book's push on the table; each of those pairs spans two bodies. The test is to ask which object each force acts on: forces on the same object may balance; forces of one pair, acting on different objects, never meet to be added.",
    ["CLM-9702-3-014"], ["AO1"]),
blk("3.1-b17", "definition", "Weight",
    "The weight of an object is the force of a gravitational field on it. It is calculated as W = mg, where W is the weight in newtons (N), m is the mass in kilograms (kg) and g is the acceleration of free fall, in m s⁻², sometimes written N kg⁻¹. Near the Earth's surface g = 9.81 m s⁻², so each kilogram of mass carries 9.81 N of weight there; a 48 kg gas cylinder weighs 48 × 9.81 = 471 N, which is 470 N to two significant figures. Weight is a vector, pointing downward, and it changes from place to place as g changes, while the mass stays fixed: on the Moon, with g = 1.62 m s⁻², the same cylinder weighs 77.9 N.",
    ["CLM-9702-3-015", "CLM-9702-3-016"], ["AO1"]),
blk("3.1-b18", "worked_calculation", "Worked example: a crate on a lifting cable",
    "A crate of building supplies of mass 400 kg is winched upward at a construction site in Windhoek, accelerating upward at 1.5 m s⁻². Two forces act on the crate: the tension T upward and the weight W downward. The resultant is T − W, and F = ma gives T − W = ma. Weight first: W = mg = 400 × 9.81 = 3924 N. Resultant force: ma = 400 × 1.5 = 600 N. So T = 3924 + 600 = 4524 N, which is 4500 N to two significant figures. The cable must pull harder than the weight by exactly the amount that accelerates the load.",
    ["CLM-9702-3-015", "CLM-9702-3-004"], ["AO2"]),
blk("3.1-b19", "cross_link", "Connections",
    "Dynamics builds directly on topic 2 (Kinematics): the acceleration that F = ma needs is the one read from a velocity–time graph or found with the equations of uniformly accelerated motion. It runs forward into topic 4 (Forces, density and pressure), which adds the other forces a body meets, and into topic 5 (Work, energy and power), which treats collisions and braking in terms of energy instead of momentum. The momentum methods here also prepare the particle physics of topic 11, where the same conservation principle is used to analyse the tracks of particles too small to see.",
    [], ["AO1"]),
blk("3.1-b20", "summary", "Checking the topic",
    "Mass resists change in motion; force changes momentum at a rate F = ∆p ÷ ∆t, which for constant mass is F = ma. The three laws of motion tie force to the motion it produces, and weight is the gravitational force W = mg on a mass. Every force in a calculation is a resultant, every momentum is a vector, and every weight is in newtons.",
    [], ["AO1"]),
]

U32_BLOCKS = [
blk("3.2-b1", "learner_objective", "What this section covers",
    "What frictional forces and viscous and drag forces, including air resistance, do; how an object moves in a uniform gravitational field when air resistance is present; and why an object moving against a resistive force can reach a terminal velocity - the constant velocity at which the resistive force balances the weight, so the resultant force is zero.", [], ["AO1"]),
blk("3.2-b2", "plain_explanation", "Friction",
    "Friction is a force that acts where two surfaces are in contact, along the surfaces, in the direction that opposes relative sliding between them. When a sack is dragged across a concrete floor, the floor pulls backward on the sack; when the tyres of a bakkie grip the gravel of a farm road, the road pushes the tyre forward, which is what friction looks like when it helps rather than hinders. Before sliding starts, friction adjusts itself to match the push, up to a limit beyond which the object gives way and slides. Friction is treated qualitatively here: what matters is its direction, along the contact and opposing the sliding, and the fact that it acts whether the object moves or is only about to move.",
    ["CLM-9702-3-018"], ["AO1"]),
blk("3.2-b3", "plain_explanation", "Drag and viscous forces",
    "A drag force is the resistive push of a fluid - air, water, oil - on an object moving through it. Air resistance is drag in air. A simple model is enough here: drag acts against the velocity, and its size increases as the speed increases, so in most real cases doubling the speed more than doubles the drag. A related group of forces are the viscous forces inside a liquid: pour honey in Windhoek's winter cold and it creeps, because the layers of the liquid drag on each other as they flow. The physics that matters is the direction and the speed-dependence: drag opposes the velocity and grows with speed, and where there is no motion relative to the fluid there is no drag from that motion.",
    ["CLM-9702-3-019"], ["AO1"]),
blk("3.2-b4", "misconception", "Drag is not upthrust",
    "Two errors recur in learners' diagrams: drag drawn along the direction of motion, and drag labelled upthrust. Drag acts against the velocity, so on a falling raindrop it points upward. It is not upthrust: upthrust is the upward push a fluid gives an object immersed in it, arising from the pressure of the fluid, and it acts whether the object moves or not, while drag depends on the speed. The test is whether the force depends on how fast the object moves through the fluid: if it does, it is drag; if it acts at any speed, including rest, it is upthrust.",
    ["CLM-9702-3-020"], ["AO1"]),
blk("3.2-b5", "plain_explanation", "Falling in air, not in a vacuum",
    "In a vacuum, in the uniform gravitational field near the Earth's surface, an object falling from rest gains 9.81 m s⁻¹ of speed each second, whatever its mass: the acceleration of free fall g is the same for everything. In air the fall is different. The weight stays constant, but the drag grows as the speed grows, so the resultant force, weight minus drag, shrinks as the object falls faster. With a smaller resultant force the acceleration is smaller, so the object gains speed ever more slowly: it still speeds up, but at a falling rate. A cricket ball dropped from a height shows this only slightly, because its drag stays small beside its weight; a sheet of paper or a parachute shows it dramatically.",
    ["CLM-9702-3-021"], ["AO1"]),
blk("3.2-b6", "plain_explanation", "The velocity–time graph of a fall through air",
    "Picture velocity on the vertical axis and time on the horizontal axis, for an object dropped from rest. The graph starts at the origin with a steep gradient of 9.81 m s⁻², the acceleration of free fall, because at the moment of release the drag is still zero. As the speed builds, so does the drag, the resultant force falls and the gradient of the graph becomes less steep. The curve flattens towards a horizontal line: a constant final velocity, at which the drag has grown to equal the weight, the forces balance and the resultant force is zero. The gradient of the graph at any point is the acceleration at that point.",
    ["CLM-9702-3-022"], ["AO1"]),
blk("3.2-b7", "definition", "Terminal velocity",
    "The terminal velocity of a falling object is the constant velocity it reaches when the drag has grown until it equals the weight: the two forces balance, so the resultant force is zero, and from then on the velocity stops changing. The forces have not gone away: weight and drag both still act, at full size, each second of the fall. Terminal velocity is reached, not switched on: the approach is gradual, and a heavier object, or one that presents a smaller area to the air, reaches a higher terminal velocity because its drag has more growing to do before it matches the weight.",
    ["CLM-9702-3-023"], ["AO1"]),
blk("3.2-b8", "analysis_chain", "How terminal velocity is reached",
    "Chain the ideas in order. Release: the weight acts, the drag is zero, so the resultant force is the full weight and the acceleration is g. The object speeds up. The drag grows with speed, so the resultant force, weight minus drag, becomes smaller, so the acceleration becomes smaller, because a = F ÷ m. The speed still increases, the drag still grows, and the acceleration fades. When the drag equals the weight, the forces balance and the resultant force is zero, so the acceleration is zero and the velocity stays constant: the object continues to fall at the terminal velocity. Each link follows from the one before, and the whole chain rests on the single fact that drag depends on speed.",
    ["CLM-9702-3-024"], ["AO2"]),
blk("3.2-b9", "cross_link", "Connections",
    "Topic 2 (Kinematics) supplies the velocity–time graphs this unit describes in words, and the value g = 9.81 m s⁻² used there is the same one in W = mg. Topic 4 (Forces, density and pressure) takes upthrust further, and topic 5 (Work, energy and power) follows the energy a falling object loses to drag. Topic 12 (Practical skills) shows how the motion of a falling object can be measured with a stopwatch, a metre rule and care over timing errors.",
    [], ["AO1"]),
blk("3.2-b10", "summary", "Checking the topic",
    "Friction acts along contacting surfaces against sliding; drag acts against the velocity and grows with speed; falling in air means an acceleration that starts at g and fades as drag builds; and terminal velocity is the constant velocity reached when drag equals weight, the forces balance and the resultant force is zero.",
    [], ["AO1"]),
]

U33_BLOCKS = [
blk("3.3-b1", "learner_objective", "What this section covers",
    "The principle of conservation of momentum, stated with its condition; applying it in one and two dimensions; what makes a collision elastic; and how the momentum of a system stays constant even when its kinetic energy does not.", [], ["AO1"]),
blk("3.3-b2", "definition", "The principle of conservation of momentum",
    "The principle of conservation of momentum states that the total momentum of a system stays constant, provided that no resultant external force acts on the system. 'Total' and the condition both matter: it is the momentum of the whole system, added as vectors, that is constant, and it stays constant only while no resultant external force intervenes. In a collision between two trolleys, the trolleys push each other with forces that are internal to the pair, so each trolley's own momentum changes while the total does not.",
    ["CLM-9702-3-025"], ["AO1"]),
blk("3.3-b3", "misconception", "Total, condition, and not moments",
    "The statement is often damaged in three ways. Momentum without 'total' suggests that each object keeps its own momentum, which is false: in each collision the objects exchange momentum. With the condition dropped, the principle claims too much: a resultant external force changes the total, which is what happens to a ball in flight under its weight. And a third error confuses this principle with the principle of moments: conservation of momentum is about motion, while the principle of moments is about turning effects. The test is whether the quantity is a momentum, mass times velocity, or a turning effect about a point.",
    ["CLM-9702-3-026"], ["AO1"]),
blk("3.3-b4", "plain_explanation", "Using the principle in one dimension",
    "The working is the same every time. Choose one direction along the line as positive and write every velocity with its sign, so a velocity in the other direction counts as negative. Add the momentum of each object before the interaction to get the total before; do the same after. Equate the totals, because the total momentum of the system stays constant provided no resultant external force acts, and solve for the unknown. In symbols: m1u1 + m2u2 = m1v1 + m2v2, where m1 and m2 are the masses in kg and u1, u2, v1, v2 are the velocities before and after, in m s⁻¹, each carrying its sign.",
    ["CLM-9702-3-027"], ["AO1"]),
blk("3.3-b5", "worked_calculation", "Worked example: trolleys that lock together",
    "A loaded trolley of mass 6.0 kg rolls at 2.5 m s⁻¹ and locks onto a stationary trolley of mass 2.0 kg. Total momentum before: 6.0 × 2.5 = 15 kg m s⁻¹, and the second trolley contributes none. After locking, the pair move as one body of mass 8.0 kg with a common velocity v, so the momentum after is 8.0v. Equating the totals: 8.0 × v = 15, so v = 15 ÷ 8.0 = 1.875, which is 1.9 m s⁻¹ to two significant figures, in the original direction. The interaction is inelastic - the trolleys end up sharing a velocity - and the later blocks show what that costs in kinetic energy.",
    ["CLM-9702-3-025", "CLM-9702-3-027"], ["AO2"]),
blk("3.3-b6", "worked_calculation", "Worked example: an elastic collision",
    "Two gliders on a near-frictionless air track collide head-on. Glider A has mass 0.50 kg and speed 4.0 m s⁻¹; glider B has mass 0.30 kg and is at rest. The collision is elastic, so two equations hold. Momentum: 0.50 × 4.0 = (0.50 × vA) + (0.30 × vB), that is, 2.0 = 0.50vA + 0.30vB. Relative speeds: the speed of approach is 4.0 − 0 = 4.0 m s⁻¹, and in an elastic collision the speed of separation is the same, so vB − vA = 4.0, which gives vB = vA + 4.0. Substitute: 2.0 = 0.50vA + 0.30vA + 0.30 × 4.0 = 0.80vA + 1.20, so 0.80vA = 2.0 − 1.2 = 0.80, and vA = 0.80 ÷ 0.80 = 1.0 m s⁻¹. Then vB = 1.0 + 4.0 = 5.0 m s⁻¹. A check on the kinetic energy confirms the elastic label: before, 0.5 × 0.50 × 16.0 = 4.0 J; after, 0.5 × 0.50 × 1.00 + 0.5 × 0.30 × 25.0 = 0.25 + 3.75 = 4.0 J.",
    ["CLM-9702-3-029", "CLM-9702-3-027"], ["AO2"]),
blk("3.3-b7", "plain_explanation", "Two dimensions",
    "An interaction in a plane, such as two pucks striking glancing blows, is handled by resolving. Take two perpendicular axes, commonly east–west and north–south. The total momentum of the system is conserved in each direction separately, provided no resultant external force acts in that direction: the eastward components before the interaction give the eastward components after, and the same for the northward components, whatever mixing happens in between. Solve each direction's equation on its own, then combine the components of an unknown velocity - its size from Pythagoras, its direction from the tangent of the angle - to state the velocity in full.",
    ["CLM-9702-3-028"], ["AO1"]),
blk("3.3-b8", "definition", "Elastic and inelastic collisions",
    "Two words sort the collisions, and the answer to any question about energy in a collision depends on which one applies. In an elastic collision the total kinetic energy of the system is conserved, and the relative speed of approach of the two objects equals their relative speed of separation. In an inelastic collision the total momentum is still conserved, but some kinetic energy transfers to other stores, warming the objects and the air and making sound; the relative speed of separation is then smaller than the relative speed of approach. Whenever kinetic energy enters an answer, say which kind of collision is meant, because momentum is conserved in both and kinetic energy is not.",
    ["CLM-9702-3-029", "CLM-9702-3-030"], ["AO1"]),
blk("3.3-b9", "plain_explanation", "Momentum kept, kinetic energy not",
    "While the total momentum of a system stays constant in an interaction, its total kinetic energy may change, and in most real interactions it falls. The reason momentum survives is the third law: the two objects push each other with forces equal in size and opposite in direction, so the momentum one object gains is equal to the momentum the other loses, and the vector total is untouched. Kinetic energy has no such guarantee, because the pushes can do work that ends up in other stores. Two identical trolleys of mass 1.2 kg, one moving at 5.0 m s⁻¹, lock together: the shared velocity after comes from momentum, with the total before of 1.2 × 5.0 = 6.0 kg m s⁻¹ shared by 2.4 kg, so v = 6.0 ÷ 2.4 = 2.5 m s⁻¹. The total momentum is 6.0 kg m s⁻¹ before and after, while the kinetic energy falls from 0.5 × 1.2 × 25.0 = 15 J to 0.5 × 2.4 × 6.25 = 7.5 J: half of it has left.",
    ["CLM-9702-3-031", "CLM-9702-3-033"], ["AO1"]),
blk("3.3-b10", "misconception", "Square each speed first",
    "When a change in kinetic energy is needed, each speed is squared on its own. The change for a body of mass m speeding up from u to v is ½mv² − ½mu², first term minus second term. The error to avoid is ½m(v − u)², squaring the difference of the speeds: squares do not survive subtraction, and ½m(v − u)² is not the energy change. For a crate going from 2.0 m s⁻¹ to 6.0 m s⁻¹, the gain is ½ × 30 × 36.0 − ½ × 30 × 4.00 = 540 − 60 = 480 J, while the incorrect form gives ½ × 30 × 16.0 = 240 J, half the truth. The test: is each speed squared before the subtraction?",
    ["CLM-9702-3-032"], ["AO1"]),
blk("3.3-b11", "cross_link", "Connections",
    "Conservation of momentum is the working tool of topic 11 (Particle physics), where unseen particles are inferred from the momentum missing after a collision, and it returns in topic 5 (Work, energy and power) whenever the energy books of an interaction are balanced. Topic 2 (Kinematics) supplies the velocities that momenta are built from, and topic 12 (Practical skills) shows how air-track and ticker-timer experiments make interactions measurable.",
    [], ["AO1"]),
blk("3.3-b12", "summary", "Checking the topic",
    "Total momentum is constant provided no resultant external force acts; work with signs in one dimension and with components in two. Elastic collisions keep kinetic energy and match the relative speeds of approach and separation; inelastic ones keep the momentum and lose some kinetic energy to other stores; and every energy change is computed by squaring each speed first.",
    [], ["AO1"]),
]

def unit(uid, title, objs, otype, blocks, wb):
    wc = sum(len((b["heading"] + " " + b["text"]).split()) for b in blocks)
    return {
        "unit_id": uid, "title": title, "objective_ids": objs, "level": "AS Level",
        "core_status": "core", "objective_type": otype, "depth_tier": 2,
        "word_budget": wb, "blocks": blocks, "word_count": wc,
        "qa_status": "review_required",
        "notes": ["Authored from the topic 3 work order; blocks cite the topic claim ledger."],
    }

UNITS = [
unit("CU-9702-3.1", "Momentum and Newton's laws of motion",
     ["OBJ-9702-3.1-01", "OBJ-9702-3.1-02", "OBJ-9702-3.1-03",
      "OBJ-9702-3.1-04", "OBJ-9702-3.1-05", "OBJ-9702-3.1-06"],
     "phys_quantitative", U31_BLOCKS, {"min": 1804, "target": 2192, "max": 2580}),
unit("CU-9702-3.2", "Non-uniform motion",
     ["OBJ-9702-3.2-01", "OBJ-9702-3.2-02", "OBJ-9702-3.2-03"],
     "phys_concept", U32_BLOCKS, {"min": 902, "target": 1096, "max": 1290}),
unit("CU-9702-3.3", "Linear momentum and its conservation",
     ["OBJ-9702-3.3-01", "OBJ-9702-3.3-02", "OBJ-9702-3.3-03", "OBJ-9702-3.3-04"],
     "phys_quantitative", U33_BLOCKS, {"min": 1203, "target": 1461, "max": 1720}),
]

# ---------------------------------------------------------------- items
def item(iid, objs, claims, subtype, aos, blooms, cw, tariff, diff, prompt, answer, guidance,
         itype="flashcard", prov=PROV):
    d = {
        "item_id": iid, "objective_ids": objs, "claim_ids": claims,
        "item_type": itype, "subtype": subtype,
        "assessment_objectives": aos, "blooms_level": blooms,
        "command_word": cw, "mark_tariff": tariff, "difficulty": diff,
        "prompt": prompt, "canonical_answer": answer, "marking_guidance": guidance,
        "context": {"sector": None, "business_size": None, "ownership": None,
                    "situation": None, "facts": []},
        "prerequisite_item_ids": [], "core_status": "core",
        "intentional_duplicate_group": None,
        "provenance": prov, "qa_status": "review_required",
        "claims_seen": {c: 1 for c in claims},
    }
    d["authored_hash"] = hashlib.sha256(_artefact_text(d).encode()).hexdigest()
    return d

MP = "Discrimination card for misconception entry {mc}: the error, the correct idea and the test, from curriculum/misconceptions.json."

ITEMS = []

ITEMS.append(item("ITEM-9702-3-001-DEF", ["OBJ-9702-3.1-01"], ["CLM-9702-3-001"],
    "DEF", ["AO1"], "Remember", "Define", 1, 1,
    "Define mass.",
    "Mass is the property of an object that resists a change in its motion; it is measured in kilograms (kg).",
    ["1 mark: the definition names the property that resists a change in motion, with its unit, the kilogram. 'How much matter the object contains' does not say what the property does and does not carry the mark."]))

ITEMS.append(item("ITEM-9702-3-002-CALC", ["OBJ-9702-3.1-01"], ["CLM-9702-3-003"],
    "CALC", ["AO2"], "Apply", "Calculate", 2, 1,
    "A winch at a depot in Walvis Bay applies a resultant force of 60 N to two carts in turn: an empty cart of mass 15 kg and a loaded cart of mass 240 kg. Calculate the acceleration of each cart.",
    "a = F ÷ m. For the empty cart: 60 ÷ 15 = 4.00, so 4.0 m s⁻² to two significant figures. For the loaded cart: 60 ÷ 240 = 0.25 m s⁻². Under the same resultant force the larger mass accelerates less, which is what mass as the property resisting change in motion means.",
    ["Equation and substitutions: a = F ÷ m, with 60 ÷ 15 and 60 ÷ 240 - 1 mark for the working.",
     "Answer: 4.0 m s⁻² and 0.25 m s⁻², each with its unit and to two significant figures - 1 mark."]))

ITEMS.append(item("ITEM-9702-3-003-DEF", ["OBJ-9702-3.1-02"], ["CLM-9702-3-004"],
    "DEF", ["AO1"], "Remember", "State", 1, 2,
    "State the equation linking resultant force, mass and acceleration, naming each symbol and its unit.",
    "F = ma, where F is the resultant force in newtons (N), m is the mass in kilograms (kg) and a is the acceleration in m s⁻².",
    ["1 mark: the equation F = ma with F named as the resultant force and each symbol's meaning and unit given - newtons, kilograms and m s⁻². Calling F 'the force' without 'resultant' is not the equation the objective asks for."]))

ITEMS.append(item("ITEM-9702-3-004-CALC", ["OBJ-9702-3.1-02"], ["CLM-9702-3-004"],
    "CALC", ["AO2"], "Apply", "Calculate", 2, 2,
    "A minibus taxi of mass 1800 kg accelerates uniformly from rest to 24 m s⁻¹ in 12 s on a straight stretch of the B1. Calculate the resultant force acting on the taxi.",
    "The acceleration first: a = ∆v ÷ ∆t = 24 ÷ 12 = 2.0 m s⁻². Then F = ma = 1800 × 2.0 = 3600 N, so the resultant force is 3600 N to two significant figures.",
    ["Equation and substitution: a = ∆v ÷ ∆t = 24 ÷ 12 = 2.0 m s⁻², then F = ma = 1800 × 2.0 - 1 mark for the two steps.",
     "Answer: 3600 N with its unit, to two significant figures - 1 mark."]))

ITEMS.append(item("ITEM-9702-3-005-CALC", ["OBJ-9702-3.1-02"], ["CLM-9702-3-004", "CLM-9702-3-006"],
    "CALC", ["AO2"], "Apply", "Calculate", 2, 2,
    "A boat of mass 600 kg is crossing the Hardap Dam. At one moment the propeller gives a driving force of 900 N and the water gives a drag of 300 N. Calculate the acceleration of the boat at that moment.",
    "The resultant force is the driving force minus the drag: 900 − 300 = 600 N. Then a = F ÷ m = 600 ÷ 600 = 1.0 m s⁻² forward, to two significant figures.",
    ["Equation and working: the resultant force 900 − 300 = 600 N, then a = F ÷ m = 600 ÷ 600 - 1 mark.",
     "Answer: 1.0 m s⁻² with its unit, to two significant figures - 1 mark."]))

ITEMS.append(item("ITEM-9702-3-006-CALC", ["OBJ-9702-3.1-02"], ["CLM-9702-3-004", "CLM-9702-3-006"],
    "CALC", ["AO2"], "Apply", "Calculate", 2, 2,
    "A supermarket trolley in Otjiwarongo gains speed at 1.5 m s⁻² when pushed with a resultant force of 45 N. Calculate the mass of the trolley with its load.",
    "F = ma rearranged for the mass: m = F ÷ a = 45 ÷ 1.5 = 30 kg, so the trolley and its load have a mass of 30 kg to two significant figures.",
    ["Equation rearranged and substituted: m = F ÷ a = 45 ÷ 1.5 - 1 mark.",
     "Answer: 30 kg with its unit, to two significant figures - 1 mark."]))

ITEMS.append(item("ITEM-9702-3-035-MISCON", ["OBJ-9702-3.1-02"], ["CLM-9702-3-006"],
    "MISCON", ["AO1"], "Understand", "Explain", 1, 3,
    "In a homework a learner divides the driving force of an engine by the mass of the vehicle and calls the result the acceleration, even though the question says drag acts too. Explain the error.",
    "F = ma needs the resultant force: the driving force alone is not the resultant when drag acts too. Every force on the object must be combined, with directions, before F = ma is used. The error is taking one force alone in place of the resultant; in fact the resultant is the driving force minus the drag, so the acceleration is smaller than the learner's value. The test: how many forces act on the object? Here two do, so one force alone cannot stand in for the resultant.",
    ["1 mark: the error named - one force used instead of the resultant of every force; in fact the resultant is the driving force minus the drag, so the acceleration comes out smaller."],
    prov=PROV + " " + MP.format(mc="MC-9702-3-01")))

ITEMS.append(item("ITEM-9702-3-046-FEATURE", ["OBJ-9702-3.1-02"], ["CLM-9702-3-005"],
    "FEATURE", ["AO1"], "Remember", "State", 1, 3,
    "State two features of the relationship between the resultant force on a body and its acceleration.",
    "The acceleration points in the same direction as the resultant force, whatever the direction of the body's velocity, and its magnitude is proportional to the magnitude of the resultant force when the mass is fixed: double the force and the acceleration doubles. A body with zero resultant force has zero acceleration, whatever its velocity.",
    ["1 mark: two features named - the shared direction of acceleration and resultant force, and the proportionality between them (or the zero resultant that gives zero acceleration)."]))

ITEMS.append(item("ITEM-9702-3-007-DEF", ["OBJ-9702-3.1-03"], ["CLM-9702-3-007"],
    "DEF", ["AO1"], "Remember", "Define", 1, 1,
    "Define linear momentum.",
    "Linear momentum is the product of the mass and the velocity of a body: p = mv, a vector with unit kg m s⁻¹, also written N s, pointing along the velocity.",
    ["1 mark: the definition as mass × velocity, stated as a vector with its unit. 'Mass times speed' drops the direction and is not the definition."]))

ITEMS.append(item("ITEM-9702-3-008-CALC", ["OBJ-9702-3.1-03"], ["CLM-9702-3-007"],
    "CALC", ["AO2"], "Apply", "Calculate", 2, 1,
    "A rugby player of mass 85 kg sprints down the wing at 7.5 m s⁻¹. Calculate the player's momentum.",
    "p = mv = 85 × 7.5 = 637.5 kg m s⁻¹, which is 640 kg m s⁻¹ to two significant figures, directed along the sprint.",
    ["Equation and substitution: p = mv = 85 × 7.5 - 1 mark.",
     "Answer: 637.5 kg m s⁻¹, so 640 kg m s⁻¹ to two significant figures, with its unit - 1 mark."]))

ITEMS.append(item("ITEM-9702-3-038-MISCON", ["OBJ-9702-3.1-03"], ["CLM-9702-3-008"],
    "MISCON", ["AO1"], "Understand", "Explain", 1, 2,
    "A ball of mass 0.20 kg hits a wall at 6.0 m s⁻¹ and rebounds at 4.0 m s⁻¹. A learner writes the change in momentum as 0.20 × (6.0 − 4.0) = 0.40 N s. Explain the error.",
    "Momentum is a vector, so the change is found from velocities with their signs. The incoming momentum is 0.20 × 6.0 = 1.2 N s toward the wall and the outgoing momentum is 0.20 × 4.0 = 0.80 N s away from it. Because the object reversed its direction, the two magnitudes add: the change is 1.2 + 0.80 = 2.0 N s in size. The error is subtracting the sizes of the momenta, which leaves out the reversal. The test: did the object reverse its direction? Here it did, so the magnitudes add.",
    ["1 mark: the error named - sizes subtracted instead of a vector change taken; in fact the rebound reverses the velocity's sign, so the change is the sum of the magnitudes, 2.0 N s."],
    prov=PROV + " " + MP.format(mc="MC-9702-3-04")))

ITEMS.append(item("ITEM-9702-3-009-DEF", ["OBJ-9702-3.1-04"], ["CLM-9702-3-009"],
    "DEF", ["AO1"], "Remember", "Define", 1, 1,
    "Define force as the rate of change of momentum.",
    "Force is the rate of change of momentum: F = ∆p ÷ ∆t, where ∆p is the change in momentum in N s and ∆t is the time taken in s; the unit is the newton. For a constant mass this reduces to F = ma.",
    ["1 mark: the definition as the rate of change of momentum, with the equation and its unit. 'The change in momentum' without the rate is not the definition."]))

ITEMS.append(item("ITEM-9702-3-010-CALC", ["OBJ-9702-3.1-04"], ["CLM-9702-3-009"],
    "CALC", ["AO2"], "Apply", "Determine", 2, 1,
    "A fast bowl reaches a wicketkeeper's gloves at 12 m s⁻¹ and is brought to rest in 0.15 s. The ball has a mass of 0.16 kg. Determine the average force the ball exerts on the gloves.",
    "The momentum change of the ball: ∆p = mv = 0.16 × 12 = 1.92 N s. The average force on the ball is F = ∆p ÷ ∆t = 1.92 ÷ 0.15 = 12.8 N, so 13 N to two significant figures; the ball pushes the gloves with the same size of force, forward.",
    ["Equation and substitution: ∆p = 0.16 × 12 = 1.92 N s, then F = ∆p ÷ ∆t = 1.92 ÷ 0.15 - 1 mark for the working.",
     "Answer: 12.8 N, so 13 N to two significant figures, with the unit - 1 mark."]))

ITEMS.append(item("ITEM-9702-3-039-MISCON", ["OBJ-9702-3.1-04"], ["CLM-9702-3-010"],
    "MISCON", ["AO1"], "Understand", "Explain", 1, 2,
    "In a homework a learner states that a ball undergoes a change in momentum of 4.0 N s and concludes that the force on the ball was 4.0 N. Explain the error.",
    "∆p, the change in momentum, is measured in N s; it becomes a force when divided by the time taken, because force is defined as the rate of change of momentum. The error is confusing the change with the rate of change: the answer must be divided by a time. If the change took 0.50 s, the average force would be 4.0 ÷ 0.50 = 8.0 N. The test: has the answer been divided by a time? If not, it is a change in momentum, not a force.",
    ["1 mark: the error named - the change in momentum used instead of the rate; in fact the force is ∆p divided by the time, and it comes out in newtons."],
    prov=PROV + " " + MP.format(mc="MC-9702-3-05")))

ITEMS.append(item("ITEM-9702-3-011-DEF", ["OBJ-9702-3.1-05"], ["CLM-9702-3-011"],
    "DEF", ["AO1"], "Remember", "State", 1, 2,
    "State Newton's first law of motion.",
    "A body remains at rest, or continues to move in a straight line at constant velocity, unless a resultant force acts on it.",
    ["1 mark: the law stated with 'resultant force'; 'unless a force acts' is not the law, because balanced forces leave the motion unchanged."]))

ITEMS.append(item("ITEM-9702-3-012-CALC", ["OBJ-9702-3.1-05"], ["CLM-9702-3-012", "CLM-9702-3-015"],
    "CALC", ["AO2"], "Apply", "Calculate", 2, 2,
    "A crate of mass 250 kg is lifted off a ship's deck in Walvis Bay by a rope, accelerating upward at 1.2 m s⁻². Calculate the tension in the rope.",
    "Two forces act on the crate: the tension T upward and the weight downward. The resultant is T − W, and the second law gives T − W = ma. The weight: W = mg = 250 × 9.81 = 2453 N. The resultant force: ma = 250 × 1.2 = 300 N. So T = 2453 + 300 = 2753 N, which is 2800 N to two significant figures.",
    ["Equation and working: the weight 250 × 9.81 = 2453 N and the resultant ma = 250 × 1.2 = 300 N, combined as T = 2453 + 300 - 1 mark.",
     "Answer: 2753 N, so 2800 N to two significant figures, with the unit - 1 mark."]))

ITEMS.append(item("ITEM-9702-3-013-CALC", ["OBJ-9702-3.1-05"], ["CLM-9702-3-012", "CLM-9702-3-013"],
    "CALC", ["AO2"], "Apply", "Calculate", 2, 2,
    "Two skaters at rest on smooth ice push each other apart with a push of 120 N. One skater has mass 60 kg and the other 40 kg. Calculate the acceleration of each skater.",
    "By Newton's third law, each skater feels a push of the same size, 120 N, in opposite directions. For the 60 kg skater: a = F ÷ m = 120 ÷ 60 = 2.0 m s⁻². For the 40 kg skater: 120 ÷ 40 = 3.0 m s⁻². The lighter skater gains the larger acceleration from the same push.",
    ["Equation and substitution: a = F ÷ m for each skater, 120 ÷ 60 and 120 ÷ 40, using the third-law fact that the two pushes are equal in size - 1 mark.",
     "Answer: 2.0 m s⁻² and 3.0 m s⁻², with units, to two significant figures - 1 mark."]))

ITEMS.append(item("ITEM-9702-3-014-CALC", ["OBJ-9702-3.1-05"], ["CLM-9702-3-012"],
    "CALC", ["AO2"], "Apply", "Calculate", 2, 2,
    "A minibus brakes hard and slows from 20 m s⁻¹ to rest in 2.5 s. A passenger of mass 70 kg is held by the seat belt. Calculate the force the belt exerts on the passenger during the stop.",
    "The passenger's change of velocity matches the minibus's: a = ∆v ÷ ∆t = 20 ÷ 2.5 = 8.0 m s⁻² backward. The belt's force: F = ma = 70 × 8.0 = 560 N, backward on the passenger, to two significant figures. The belt supplies the resultant force that slows the passenger with the vehicle; the passenger's own tendency, by the first law, is to keep the forward velocity.",
    ["Equation and substitution: a = ∆v ÷ ∆t = 20 ÷ 2.5 = 8.0 m s⁻², then F = ma = 70 × 8.0 - 1 mark.",
     "Answer: 560 N with the unit, backward on the passenger, to two significant figures - 1 mark."]))

ITEMS.append(item("ITEM-9702-3-036-MISCON", ["OBJ-9702-3.1-05"], ["CLM-9702-3-012"],
    "MISCON", ["AO1"], "Understand", "Explain", 1, 3,
    "'Force equals mass times acceleration' - a learner offers this as a statement of Newton's second law of motion. Explain the error.",
    "The second law links the resultant force to the rate of change of momentum: the two are proportional and point the same way. F = ma is the special case for a constant mass; stated as the law itself, it drops the rate of change of momentum, which is what the law asserts. The error is giving the special case in place of the law. The test: does the statement mention the rate of change of momentum?",
    ["1 mark: the error named - the special case stated instead of the law; in fact the law is about the rate of change of momentum, and F = ma follows when the mass is constant."],
    prov=PROV + " " + MP.format(mc="MC-9702-3-02")))

ITEMS.append(item("ITEM-9702-3-037-MISCON", ["OBJ-9702-3.1-05"], ["CLM-9702-3-014"],
    "MISCON", ["AO1"], "Understand", "Explain", 1, 3,
    "A book rests on a table. A learner says the book's weight and the table's upward push on the book form a Newton's third law pair, and that this is why the two forces cancel. Explain the error.",
    "The two forces named both act on the book, and they cancel because the book is in equilibrium - but they are not a third-law pair, whose two forces act on two different bodies. The book's weight is paired with the pull of the book on the Earth; the table's push on the book is paired with the push of the book on the table. The error is treating the forces of a third-law pair as though they acted on one object and could balance it; a true pair never cancels anything, because each of its forces acts on a different body. The test: which object does each force act on?",
    ["1 mark: the error named - a pair treated as two forces on one object; in fact each force of a third-law pair acts on a different body, so the pair does not balance anything."],
    prov=PROV + " " + MP.format(mc="MC-9702-3-03")))

ITEMS.append(item("ITEM-9702-3-047-FEATURE", ["OBJ-9702-3.1-05"], ["CLM-9702-3-013"],
    "FEATURE", ["AO1"], "Remember", "State", 1, 3,
    "State three features of the two forces in a Newton's third law pair.",
    "The two forces are equal in size and opposite in direction, they are of the same type (both gravitational pulls, or both contact pushes), and they act on two different bodies, so they never cancel on one object.",
    ["1 mark: three characteristic features named - equal in size, opposite in direction with the same type of force, and two different bodies acted on."]))

ITEMS.append(item("ITEM-9702-3-015-DEF", ["OBJ-9702-3.1-06"], ["CLM-9702-3-015"],
    "DEF", ["AO1"], "Remember", "State", 1, 2,
    "State what is meant by the weight of an object, and give the equation for it.",
    "The weight of an object is the force of a gravitational field on it: W = mg, where m is the mass in kilograms, g is the acceleration of free fall in m s⁻² and W is the weight in newtons, directed downward.",
    ["1 mark: the meaning - weight as the force of a gravitational field on a mass - with the equation W = mg and its symbols and units. 'How heavy it feels' is a description, not a definition."]))

ITEMS.append(item("ITEM-9702-3-016-CALC", ["OBJ-9702-3.1-06"], ["CLM-9702-3-015"],
    "CALC", ["AO2"], "Apply", "Calculate", 2, 2,
    "A gas cylinder delivered to a farm near Tsumeb has a mass of 48 kg. Calculate its weight.",
    "W = mg = 48 × 9.81 = 471 N, which is 470 N to two significant figures, directed downward.",
    ["Equation and substitution: W = mg = 48 × 9.81 - 1 mark.",
     "Answer: 471 N, so 470 N to two significant figures, with the unit - 1 mark."]))

ITEMS.append(item("ITEM-9702-3-017-CALC", ["OBJ-9702-3.1-06"], ["CLM-9702-3-015", "CLM-9702-3-016"],
    "CALC", ["AO2"], "Apply", "Calculate", 2, 2,
    "A geologist's kit of mass 12 kg is flown from Windhoek to a lunar-style training camp where the acceleration of free fall is 1.62 m s⁻². Calculate the weight of the kit at the camp and back in Windhoek, where g = 9.81 m s⁻².",
    "At the camp: W = mg = 12 × 1.62 = 19.4 N. In Windhoek: W = 12 × 9.81 = 118 N. The mass is 12 kg in both places; the weight differs because g differs.",
    ["Equation and substitutions: W = mg with 12 × 1.62 at the camp and 12 × 9.81 in Windhoek - 1 mark for the working.",
     "Answer: 19.4 N and 118 N, each with its unit, to three significant figures - 1 mark."]))

ITEMS.append(item("ITEM-9702-3-018-CALC", ["OBJ-9702-3.1-06"], ["CLM-9702-3-015", "CLM-9702-3-012"],
    "CALC", ["AO2"], "Apply", "Calculate", 2, 2,
    "A helicopter lowers a crate of relief supplies of mass 300 kg on a cable, bringing it from 6.0 m s⁻¹ to rest in 3.0 s while it still moves downward. Calculate the tension in the cable.",
    "The crate slows, so its acceleration points upward: a = ∆v ÷ ∆t = 6.0 ÷ 3.0 = 2.0 m s⁻². Two forces act: the tension T upward and the weight W = 300 × 9.81 = 2943 N downward. The resultant is T − W = ma = 300 × 2.0 = 600 N, so T = 2943 + 600 = 3543 N, which is 3500 N to two significant figures.",
    ["Equation and working: the deceleration 6.0 ÷ 3.0 = 2.0 m s⁻², the weight 300 × 9.81 = 2943 N, and T = 2943 + 600 with ma = 300 × 2.0 = 600 N - 1 mark.",
     "Answer: 3543 N, so 3500 N to two significant figures, with the unit - 1 mark."]))

ITEMS.append(item("ITEM-9702-3-040-MISCON", ["OBJ-9702-3.1-06"], ["CLM-9702-3-017"],
    "MISCON", ["AO1"], "Understand", "Explain", 1, 3,
    "At a market a learner reads 'weighs 2.5 kg' on a packet of steak and writes in their notes that the weight of the steak is 2.5 kg. Explain the error.",
    "The packet's mass is 2.5 kg; its weight is a force, W = mg = 2.5 × 9.81 = 24.5 N, not 2.5 kg. The error is mixing mass, the property in kilograms that resists a change in motion, with weight, the gravitational force in newtons on that mass. The test: is the answer in kilograms or in newtons? A weight is in newtons.",
    ["1 mark: the error named - kilograms stated as a weight; in fact the mass is in kilograms and the weight is the force mg, in newtons."],
    prov=PROV + " " + MP.format(mc="MC-9702-3-06")))

ITEMS.append(item("ITEM-9702-3-048-FEATURE", ["OBJ-9702-3.1-06"], ["CLM-9702-3-002", "CLM-9702-3-015"],
    "FEATURE", ["AO1"], "Remember", "State", 1, 3,
    "State two features that distinguish mass from weight.",
    "Mass is measured in kilograms and is the property that resists a change in motion; weight is measured in newtons and is the force of a gravitational field on that mass, W = mg. Mass is fixed for the object, while weight varies from place to place as g varies: on the Moon the kit's mass is what it was on Earth, and its weight is smaller.",
    ["1 mark: two distinguishing features named - the units (kilograms against newtons) and what each is (resistance to change in motion against the gravitational force mg)."]))

ITEMS.append(item("ITEM-9702-3-019-DEF", ["OBJ-9702-3.2-01"], ["CLM-9702-3-018"],
    "DEF", ["AO1"], "Remember", "State", 1, 2,
    "State what is meant by a frictional force.",
    "A frictional force acts where two surfaces are in contact, along the surfaces, in the direction that opposes relative sliding or attempted sliding between them; it acts whether the object is moving or only about to move.",
    ["1 mark: the meaning - a force at contacting surfaces opposing relative sliding, acting along the surfaces. Its direction, opposite to the motion or the attempted motion, is the point the statement must carry."]))

ITEMS.append(item("ITEM-9702-3-020-MECH", ["OBJ-9702-3.2-01"], ["CLM-9702-3-019"],
    "MECH", ["AO2"], "Understand", "Explain", 2, 2,
    "Explain how the drag on a minibus taxi changes as it speeds up on the open road, and how this affects the acceleration produced by a constant driving force.",
    "Drag from the air acts against the velocity, and its size increases as the speed increases. The resultant forward force is the driving force minus the drag, so as the taxi speeds up the drag grows, the resultant force falls and the acceleration falls, because a = F ÷ m. The acceleration fades because the resultant force fades, not because the driving force changes.",
    ["How: drag increases with speed and acts against the velocity - 1 mark.",
     "Because the resultant force (driving force minus drag) then falls, the acceleration falls with it, since a = F ÷ m - 1 mark."]))

ITEMS.append(item("ITEM-9702-3-042-MISCON", ["OBJ-9702-3.2-01"], ["CLM-9702-3-020"],
    "MISCON", ["AO1"], "Understand", "Explain", 1, 3,
    "On a diagram a learner draws the drag on a falling raindrop pointing downward, in the direction of motion, and labels it 'upthrust'. Explain the error.",
    "Drag acts against the velocity, so on a falling raindrop it points upward, opposite to the motion; it is not upthrust. Upthrust is the upward push a fluid gives an immersed object, arising from the pressure of the fluid, and it acts whether or not the drop moves; drag depends on how fast the drop moves and grows with that speed. The error is drawing the drag along the motion and swapping it for upthrust. The test: does the force depend on how fast the object moves? Drag does; upthrust does not.",
    ["1 mark: the error named - drag drawn along the motion or confused with upthrust; in fact drag acts against the velocity and increases with speed, while upthrust does not depend on speed."],
    prov=PROV + " " + MP.format(mc="MC-9702-3-08")))

ITEMS.append(item("ITEM-9702-3-049-FEATURE", ["OBJ-9702-3.2-01"], ["CLM-9702-3-019"],
    "FEATURE", ["AO1"], "Remember", "State", 1, 3,
    "State two features of the drag on a body moving through a fluid.",
    "Drag acts in the direction opposite to the velocity, and its size increases as the speed increases; it acts on a rising, falling or travelling body alike, provided the body moves through the fluid.",
    ["1 mark: two features named - the direction against the velocity, and the increase with speed."]))

ITEMS.append(item("ITEM-9702-3-021-DEF", ["OBJ-9702-3.2-02"], ["CLM-9702-3-021"],
    "DEF", ["AO1"], "Remember", "State", 1, 2,
    "State how the motion of an object falling from rest in air differs from the same fall in a vacuum.",
    "In a vacuum, in the uniform gravitational field near the Earth's surface, the object falls with the constant acceleration g = 9.81 m s⁻², whatever its mass. In air it starts with the same acceleration, but as its speed grows so does the drag, so the resultant force falls below the weight and the acceleration falls below g, fading as the velocity settles towards a final constant value.",
    ["1 mark: the meaning - constant acceleration g in a vacuum, an acceleration that starts at g and falls in air because the drag grows with speed and the resultant force falls."]))

ITEMS.append(item("ITEM-9702-3-022-FEATURE", ["OBJ-9702-3.2-02"], ["CLM-9702-3-022"],
    "FEATURE", ["AO1"], "Remember", "State", 1, 2,
    "State two features of the velocity–time graph for an object falling from rest through air until it reaches terminal velocity.",
    "The graph starts at the origin with a gradient of 9.81 m s⁻², the acceleration of free fall, and the gradient falls as the speed builds, because the drag grows and the resultant force falls. It ends as a horizontal line: a constant velocity, at which the drag equals the weight, the forces balance and the resultant force is zero.",
    ["1 mark: two features named - the initial gradient of 9.81 m s⁻² growing less steep as drag rises with speed, and the horizontal line where the resultant force is zero because the drag balances the weight."]))

ITEMS.append(item("ITEM-9702-3-023-DEF", ["OBJ-9702-3.2-03"], ["CLM-9702-3-023"],
    "DEF", ["AO1"], "Remember", "State", 1, 2,
    "State what is meant by terminal velocity.",
    "Terminal velocity is the constant velocity a falling object reaches when the drag has grown until it equals the weight: the forces balance, the resultant force is zero, and both forces still act at full size. The object keeps falling at that velocity; it does not stop.",
    ["1 mark: the meaning - the constant velocity reached when the resistive force balances the weight, so the resultant force is zero. 'No forces act' is not the meaning: both forces still act and cancel."]))

ITEMS.append(item("ITEM-9702-3-024-MECH", ["OBJ-9702-3.2-03"], ["CLM-9702-3-024", "CLM-9702-3-023"],
    "MECH", ["AO2"], "Understand", "Explain", 2, 2,
    "Explain how a skydiver falling from a plane reaches terminal velocity before the parachute opens.",
    "The skydiver's weight stays constant while the drag grows with speed. Starting from rest, the weight exceeds the drag, so there is a downward resultant force and the speed increases. As the speed increases the drag increases, so the resultant force falls, so the acceleration falls, because a = F ÷ m. When the drag has grown until it equals the weight, the forces balance and the resultant force is zero, so the acceleration is zero and the velocity stays constant: that constant velocity is the terminal velocity.",
    ["How: the speed increases while the drag is below the weight, and the drag rises with the speed - 1 mark.",
     "Then the forces balance, the resultant force is zero and the velocity becomes constant, which is the terminal velocity - 1 mark."]))

ITEMS.append(item("ITEM-9702-3-041-MISCON", ["OBJ-9702-3.2-03"], ["CLM-9702-3-023"],
    "MISCON", ["AO1"], "Understand", "Explain", 1, 3,
    "A learner writes: 'At terminal velocity the skydiver is in equilibrium, so no force acts on them.' Explain the error.",
    "The error is 'no force': weight and drag both act at terminal velocity, at full size, and each of them is still there. Because they are equal in size and opposite in direction, the resultant force is zero - the forces balance - and so the velocity stays constant. The forces have not disappeared; they cancel. The test: zero resultant force, not zero force.",
    ["1 mark: the error named - 'no force' written in place of 'no resultant force'; in fact the weight and the drag still act and balance, which is why the velocity is constant."],
    prov=PROV + " " + MP.format(mc="MC-9702-3-07")))

ITEMS.append(item("ITEM-9702-3-025-DEF", ["OBJ-9702-3.3-01"], ["CLM-9702-3-025"],
    "DEF", ["AO1"], "Remember", "State", 1, 2,
    "State the principle of conservation of momentum.",
    "The total momentum of a system stays constant, provided that no resultant external force acts on the system.",
    ["1 mark: the law stated with 'total' and the condition of no resultant external force. Either one missing drops the mark, because the principle is about motion, not turning."]))

ITEMS.append(item("ITEM-9702-3-026-FEATURE", ["OBJ-9702-3.3-01"], ["CLM-9702-3-025"],
    "FEATURE", ["AO1"], "Remember", "State", 1, 2,
    "State two features of the principle of conservation of momentum that make it usable in problems.",
    "It applies to the total momentum of the whole system, added as vectors, in each direction separately; and it holds whatever the interaction - sticking, springing apart or glancing - provided that no resultant external force acts on the system.",
    ["1 mark: two characteristic features named - the total momentum of the system as a whole, and the condition of no resultant external force under which it stays constant."]))

ITEMS.append(item("ITEM-9702-3-043-MISCON", ["OBJ-9702-3.3-01"], ["CLM-9702-3-026"],
    "MISCON", ["AO1"], "Understand", "Explain", 1, 3,
    "A learner states the principle of conservation of momentum as 'momentum is constant' and, asked what it says about a see-saw, answers that it is the same principle as the principle of moments. Explain the errors.",
    "The statement drops 'total' and the condition: the principle says the total momentum of a system stays constant provided no resultant external force acts on it - each object's own momentum can change while the total does not. And the principle of moments is a different principle, about turning effects of forces about a point, while conservation of momentum is about motion. The error is confusing a quantity of motion with a turning effect. The test: is the principle about turning (moments) or about motion (momentum)?",
    ["1 mark: the errors named - 'total' and the condition dropped, and momentum confused with moments; in fact the principle is about the total momentum of a system, a quantity of motion, not about turning effects."],
    prov=PROV + " " + MP.format(mc="MC-9702-3-09")))

ITEMS.append(item("ITEM-9702-3-027-DEF", ["OBJ-9702-3.3-02"], ["CLM-9702-3-027"],
    "DEF", ["AO1"], "Remember", "State", 1, 2,
    "State the steps for applying the principle of conservation of momentum to an interaction along a straight line.",
    "Choose one direction as positive and give every velocity its sign. Write the total momentum before the interaction as the sum of each object's mv, and the total after in the same way. Equate the two totals, because the total momentum of the system stays constant provided no resultant external force acts, and solve for the unknown.",
    ["1 mark: the steps - a chosen positive direction with signs on every velocity, and the total momentum before equated to the total momentum after; the equation this gives is the working basis of the method."]))

ITEMS.append(item("ITEM-9702-3-028-CALC", ["OBJ-9702-3.3-02"], ["CLM-9702-3-027", "CLM-9702-3-025"],
    "CALC", ["AO2"], "Apply", "Calculate", 2, 2,
    "A runaway supermarket trolley of mass 2.0 kg moving at 3.0 m s⁻¹ catches a stationary trolley of mass 1.0 kg at a market in Gobabis, and the two lock together. Calculate their common velocity.",
    "Take the trolley's original direction as positive. Total momentum before: 2.0 × 3.0 = 6.0 kg m s⁻¹, and the stationary trolley contributes none. After locking, the pair move as one body of mass 3.0 kg: 3.0 × v = 6.0, so v = 6.0 ÷ 3.0 = 2.0 m s⁻¹ in the original direction.",
    ["Equation and substitution: total momentum before 2.0 × 3.0 = 6.0 kg m s⁻¹, equated to (2.0 + 1.0) × v after - 1 mark.",
     "Answer: v = 6.0 ÷ 3.0 = 2.0 m s⁻¹, with the unit and direction - 1 mark."]))

ITEMS.append(item("ITEM-9702-3-029-CALC", ["OBJ-9702-3.3-02"], ["CLM-9702-3-027", "CLM-9702-3-008"],
    "CALC", ["AO2"], "Apply", "Calculate", 2, 2,
    "In a game of marbles at a school in Otjiwarongo, a marble of mass 20 g moving at 1.5 m s⁻¹ strikes a stationary marble of mass 30 g head-on, and the first marble rebounds at 0.30 m s⁻¹. Calculate the velocity of the second marble after the impact.",
    "Convert first: 20 g is 0.020 kg and 30 g is 0.030 kg. Take the first marble's original direction as positive. Momentum before: 0.020 × 1.5 = 0.030 kg m s⁻¹. After: the first marble carries 0.020 × 0.30 = 0.0060 kg m s⁻¹ in the negative direction, so the second must carry 0.030 + 0.0060 = 0.036 kg m s⁻¹ in the positive direction. Its velocity: 0.036 ÷ 0.030 = 1.20, so 1.2 m s⁻¹ forwards, to two significant figures.",
    ["Equation and substitution: 0.020 × 1.5 = 0.030 kg m s⁻¹ before; after, the rebound taken with its sign, 0.030 + 0.0060 = 0.036 kg m s⁻¹ - 1 mark for the working.",
     "Answer: v = 0.036 ÷ 0.030 = 1.2 m s⁻¹ forwards, with the unit - 1 mark."]))

ITEMS.append(item("ITEM-9702-3-030-CALC", ["OBJ-9702-3.3-02"], ["CLM-9702-3-028", "CLM-9702-3-025"],
    "CALC", ["AO2"], "Apply", "Calculate", 2, 2,
    "At a crossroads in Ongwediva, a car of mass 1500 kg travelling east at 20 m s⁻¹ collides with a car of mass 1000 kg travelling north at 15 m s⁻¹, and the two lock together. Calculate the velocity of the wreckage immediately after the collision.",
    "Momentum is conserved separately in each perpendicular direction. Eastward, before: 1500 × 20 = 30000 kg m s⁻¹; after: 2500 × vE, so vE = 30000 ÷ 2500 = 12.0 m s⁻¹. Northward, before: 1000 × 15 = 15000 kg m s⁻¹; after: 2500 × vN, so vN = 15000 ÷ 2500 = 6.0 m s⁻¹. The speed is the square root of (12.0² + 6.0²), the square root of 180, which is 13.4 m s⁻¹; the tangent of the angle north of east is 6.0 ÷ 12.0 = 0.50, so the direction is 27° north of east.",
    ["Equation and working, one direction at a time: eastward 1500 × 20 = 30000 kg m s⁻¹ and northward 1000 × 15 = 15000 kg m s⁻¹ before, each shared by 2500 kg after - 1 mark.",
     "Answer: 13.4 m s⁻¹ at 27° north of east, with the unit, to three significant figures - 1 mark."]))

ITEMS.append(item("ITEM-9702-3-045-MISCON", ["OBJ-9702-3.3-02"], ["CLM-9702-3-032"],
    "MISCON", ["AO1"], "Understand", "Explain", 1, 3,
    "Working out the kinetic energy gained by a crate of mass 30 kg as it speeds up from 2.0 m s⁻¹ to 6.0 m s⁻¹, a learner writes ∆Ek = ½m(v − u)² and gets 240 J. Explain the error.",
    "Each speed must be squared on its own, because Ek = ½mv². The gain is (0.5 × 30 × 36.0) − (0.5 × 30 × 4.00) = 540 − 60 = 480 J. The learner's form, 0.5 × 30 × 16.0 = 240 J, squares the difference of the speeds instead: squares do not distribute over a subtraction. The error gives half the true gain here. The test: is each speed squared before the subtraction?",
    ["1 mark: the error named - the difference of the speeds squared instead of each speed squared; in fact ∆Ek = ½mv² − ½mu², here 480 J, not 240 J."],
    prov=PROV + " " + MP.format(mc="MC-9702-3-11")))

ITEMS.append(item("ITEM-9702-3-031-DEF", ["OBJ-9702-3.3-03"], ["CLM-9702-3-029"],
    "DEF", ["AO1"], "Remember", "State", 1, 2,
    "State what happens to the total kinetic energy and to the relative speed in an elastic collision.",
    "In an elastic collision the total kinetic energy of the system is conserved, and the relative speed of approach of the two objects equals their relative speed of separation.",
    ["1 mark: the law for an elastic collision - kinetic energy conserved, and relative speed of approach equal to relative speed of separation. The word 'elastic' belongs in the answer, because in an inelastic collision neither holds."]))

ITEMS.append(item("ITEM-9702-3-032-FEATURE", ["OBJ-9702-3.3-03"], ["CLM-9702-3-029"],
    "FEATURE", ["AO1"], "Remember", "State", 1, 2,
    "State two features of an elastic collision between two objects.",
    "The total kinetic energy of the pair is the same after as before, and the relative speed of separation equals the relative speed of approach: the difference of the two velocities keeps its size across the collision, with its sign reversed.",
    ["1 mark: two characteristic features named - conserved total kinetic energy, and equal relative speeds of approach and separation."]))

ITEMS.append(item("ITEM-9702-3-044-MISCON", ["OBJ-9702-3.3-03"], ["CLM-9702-3-030"],
    "MISCON", ["AO1"], "Understand", "Explain", 1, 3,
    "Two lumps of clay rolled along a bench collide and stick. A learner calculates the speed of the pair from momentum, then claims the total kinetic energy before the collision equals the total after, 'because energy is conserved'. Explain the error.",
    "Momentum is conserved in the interaction, but kinetic energy is conserved only in an elastic collision. When the lumps stick, the collision is inelastic: the total momentum after equals the total before, while some kinetic energy transfers to other stores, warming the clay and making sound. The error is assuming kinetic energy is conserved in every collision. The test: is the collision stated to be elastic? Here it is not, so the momentum calculation stands and the kinetic energy claim fails.",
    ["1 mark: the error named - kinetic energy assumed conserved in a sticking (inelastic) collision; in fact momentum is conserved in the interaction, and kinetic energy only in an elastic one."],
    prov=PROV + " " + MP.format(mc="MC-9702-3-10")))

ITEMS.append(item("ITEM-9702-3-033-DEF", ["OBJ-9702-3.3-04"], ["CLM-9702-3-031"],
    "DEF", ["AO1"], "Remember", "State", 1, 2,
    "State what happens to the total momentum and to the total kinetic energy of a system of two interacting objects.",
    "The total momentum of the system stays constant in the interaction, provided no resultant external force acts on it, while the total kinetic energy may change: some may transfer to other stores, which is what makes the interaction inelastic.",
    ["1 mark: the law - momentum conserved provided no resultant external force, kinetic energy may change; the word 'may' carries the point, because an elastic interaction is the case in which it happens not to."]))

ITEMS.append(item("ITEM-9702-3-034-MECH", ["OBJ-9702-3.3-04"], ["CLM-9702-3-031", "CLM-9702-3-033"],
    "MECH", ["AO2"], "Understand", "Explain", 2, 2,
    "In a shunting yard at Gobabis, a truck of mass 2.0 × 10⁴ kg rolling at 3.0 m s⁻¹ runs into a stationary truck of mass 1.0 × 10⁴ kg and the two couple. Explain how the total momentum is conserved while the kinetic energy is not, and determine the speed of the coupled trucks.",
    "The two trucks form one system, and along the track no resultant external force acts, so the total momentum stays constant: before, 20000 × 3.0 = 60000 kg m s⁻¹; after, 30000 × v, so v = 60000 ÷ 30000 = 2.0 m s⁻¹. The kinetic energy is not conserved: before, 0.5 × 20000 × 9.00 = 90000 J; after, 0.5 × 30000 × 4.00 = 60000 J. The fall is 90000 − 60000 = 30000 J, transferred to other stores in the coupling - the jolt, the warming and the sound. Momentum survives because the coupling forces are equal in size and opposite in direction, so the momentum one truck loses equals the momentum the other gains; kinetic energy has no such guarantee in an inelastic interaction.",
    ["How: the totals of momentum are equal before and after, as the working 20000 × 3.0 = 60000 kg m s⁻¹ and 60000 ÷ 30000 = 2.0 m s⁻¹ shows - 1 mark.",
     "Because the coupling is inelastic, the kinetic energy falls, by 30000 J to other stores - 1 mark."]))

# ---------------------------------------------------------------- performance tasks

ITEMS.append(item("ITEM-9702-3-P01",
    ["OBJ-9702-3.1-03", "OBJ-9702-3.1-04", "OBJ-9702-3.2-03", "OBJ-9702-3.3-02"],
    ["CLM-9702-3-007", "CLM-9702-3-008", "CLM-9702-3-009", "CLM-9702-3-023",
     "CLM-9702-3-024", "CLM-9702-3-027", "CLM-9702-3-028"],
    None, ["AO1", "AO2"], "Apply", None, 12, 3,
    "Twelve questions in the style of Paper 1. Choose one option for each.\n\n"
    "1. Which quantity is defined as the product of the mass and the velocity of a body?\nA  the moment of a force\nB  kinetic energy\nC  linear momentum\nD  weight\n\n"
    "2. Force is defined as\nA  the rate of change of momentum\nB  the change in momentum\nC  the product of mass and velocity\nD  the product of mass and acceleration\n\n"
    "3. The two forces of a Newton's third law pair\nA  act on the same body and balance each other\nB  are of different types but equal in size\nC  act on the same body and add to give the resultant\nD  act on two different bodies and do not cancel\n\n"
    "4. At terminal velocity,\nA  the drag has fallen to zero\nB  the resultant force is zero because the drag balances the weight\nC  no force acts on the object\nD  the weight has fallen to zero\n\n"
    "5. The principle of conservation of momentum states that\nA  the total momentum of a system stays constant provided no resultant external force acts\nB  the momentum of each object in the system stays constant\nC  the total momentum stays constant whatever external forces act\nD  the total kinetic energy stays constant\n\n"
    "6. In an elastic collision,\nA  the objects stick together\nB  total kinetic energy is conserved but the relative speeds differ\nC  total momentum is conserved, total kinetic energy is conserved, and the relative speed of approach equals the relative speed of separation\nD  total momentum is not conserved\n\n"
    "7. A resultant force of 15 N acts on a body of mass 3.0 kg. Its acceleration is\nA  5.0 m s⁻²\nB  45 m s⁻²\nC  0.20 m s⁻²\nD  15 m s⁻²\n\n"
    "8. A sack of mass 6.0 kg hangs at rest. Its weight is\nA  6.0 N\nB  9.81 N\nC  0.61 N\nD  59 N\n\n"
    "9. A ball of mass 0.40 kg moving at 8.0 m s⁻¹ is caught and stopped in 0.20 s. The force on the catcher's hands is\nA  3.2 N\nB  16 N\nC  1.6 N\nD  64 N\n\n"
    "10. A rail truck of mass 4.0 × 10³ kg moving at 3.0 m s⁻¹ collides with a stationary rail truck of mass 2.0 × 10³ kg and they lock together. Their common speed is\nA  2.0 m s⁻¹\nB  3.0 m s⁻¹\nC  1.0 m s⁻¹\nD  6.0 m s⁻¹\n\n"
    "11. As a skydiver who is still speeding up falls faster, the drag on them\nA  decreases, because the air thins\nB  acts along the motion, helping gravity\nC  is replaced by upthrust once the fall is steady\nD  increases, because it depends on the speed\n\n"
    "12. A learner throws a ball of mass 0.30 kg at a wall at 5.0 m s⁻¹ and it bounces straight back at 3.0 m s⁻¹. The magnitude of the change in its momentum is\nA  zero\nB  0.60 N s\nC  2.4 N s\nD  1.5 N s",
    "Key: 1 C, 2 A, 3 D, 4 B, 5 A, 6 C, 7 A, 8 D, 9 B, 10 A, 11 D, 12 C.\n"
    "1. Momentum is mass × velocity (C). A is the turning effect of a force, a different quantity; B is ½mv²; D is mg.\n"
    "2. Force is the rate of change of momentum (A). B is the change in momentum, in N s, not yet a force; C defines momentum; D is the special case F = ma for a constant mass, not the definition.\n"
    "3. A third-law pair is equal in size, opposite in direction, of the same type, and acts on two different bodies (D). A and C put both forces of the pair on one object, where they would balance instead; B has the types different.\n"
    "4. At terminal velocity the resultant force is zero because the drag balances the weight (B). C claims no force acts, which is false: both forces still act. A and D remove forces that are present.\n"
    "5. The principle needs the total momentum and the condition of no resultant external force (A). B drops 'total'; C drops the condition; D is a statement about kinetic energy, not momentum.\n"
    "6. Elastic means total kinetic energy conserved and the relative speed of approach equal to the relative speed of separation (C). A describes sticking, an inelastic collision; B halves the definition; D breaks momentum conservation.\n"
    "7. a = F ÷ m = 15 ÷ 3.0 = 5.0 m s⁻² (A). B multiplies instead of dividing; C inverts the ratio; D is the force, not the acceleration.\n"
    "8. W = mg = 6.0 × 9.81 = 58.86 N, so 59 N (D). A keeps the number of kilograms as a force; B quotes g; C divides instead of multiplying.\n"
    "9. ∆p = 0.40 × 8.0 = 3.2 N s; F = ∆p ÷ ∆t = 3.2 ÷ 0.20 = 16 N (B). A is the change in momentum used as a force without dividing by the time; C divides by 2.0 s; D divides the wrong way round.\n"
    "10. Momentum before: 4000 × 3.0 = 12000 kg m s⁻¹; after, mass 6000 kg, so v = 12000 ÷ 6000 = 2.0 m s⁻¹ (A). B keeps the first truck's speed; C subtracts the masses; D adds the speeds.\n"
    "11. Drag increases with speed (D). A has the change backwards; B draws the drag along the motion; C swaps drag for upthrust.\n"
    "12. The velocities reverse, so the magnitudes add: 0.30 × 5.0 = 1.5 N s and 0.30 × 3.0 = 0.90 N s, and 1.5 + 0.90 = 2.4 N s (C). A treats momentum as a scalar; B subtracts the sizes, leaving out the reversal; D is the initial momentum alone.",
    ["The key: one mark per correct option, twelve marks in all - the correct option lettered for each question.",
     "Each distractor comes from a named error in the misconception register: the moment confused with momentum, the change in momentum used as a force, a third-law pair balanced on one body, 'no force' at terminal velocity, the condition dropped from the conservation principle, kinetic energy assumed conserved in a sticking collision, a slip in F ÷ m, kilograms used as a weight, and sizes subtracted on a rebound."],
    itype="multiple_choice_set",
    prov=PROV + " Twelve questions spanning the topic; the four objectives listed are the spine of the set."))

ITEMS.append(item("ITEM-9702-3-P02",
    ["OBJ-9702-3.1-03", "OBJ-9702-3.1-04", "OBJ-9702-3.1-05"],
    ["CLM-9702-3-007", "CLM-9702-3-008", "CLM-9702-3-009", "CLM-9702-3-013"],
    None, ["AO1", "AO2"], "Apply", "Define", 8, 3,
    "Water from a fire hose strikes a burning wall. The hose delivers 25 kg of water each second, and the water arrives horizontally at 20 m s⁻¹ and runs down the wall without bouncing back.\n"
    "(a) Define linear momentum. [1]\n"
    "(b) Calculate the momentum of the water that arrives at the wall each second. [1]\n"
    "(c) Determine the average force that the water exerts on the wall. [2]\n"
    "(d) State Newton's third law of motion and use it to state the size and direction of the force the wall exerts on the water. [2]\n"
    "(e) A learner suggests that the force on the wall would be larger if the water bounced straight back from the wall at 5.0 m s⁻¹ instead of stopping. Explain whether the suggestion is right. [2]",
    "(a) Linear momentum is the product of the mass and the velocity of a body: p = mv, a vector with unit kg m s⁻¹ (N s).\n"
    "(b) p = mv = 25 × 20 = 500 kg m s⁻¹ each second, directed horizontally at the wall.\n"
    "(c) Each second, 500 N s of horizontal momentum arrives and runs away with none, so the water's horizontal momentum falls by 500 N s in every 1.0 s. F = ∆p ÷ ∆t = 500 ÷ 1.0 = 500 N, and the water pushes the wall with a force of 500 N, into the wall.\n"
    "(d) Newton's third law: when one body exerts a force on a second, the second exerts on the first a force equal in size, opposite in direction and of the same type. The water pushes the wall with 500 N into the wall, so the wall pushes the water with 500 N, away from the wall.\n"
    "(e) The suggestion is right. On a rebound the water's horizontal velocity changes from 20 m s⁻¹ toward the wall to 5.0 m s⁻¹ away from it, a change of 20 + 5.0 = 25 m s⁻¹, because the direction reverses and the magnitudes add. The momentum change each second is then 25 × 25 = 625 N s, so the force is 625 N, larger than 500 N: the reversal makes the momentum change bigger, and so makes the force bigger.",
    ["Part (a): 1 mark for the definition of momentum as mass × velocity, named as a vector with its unit.",
     "Part (b): 1 mark for 25 × 20 = 500 kg m s⁻¹ with the unit.",
     "Part (c): 2 marks - the equation F = ∆p ÷ ∆t applied to the water stopped each second, 1 mark for the working and 1 mark for the 500 N answer with its unit.",
     "Part (d): 2 marks - 1 mark for the third law stated with equal size, opposite direction and the same type, 1 mark for the 500 N reply force, away from the wall.",
     "Part (e): 2 marks - the reason: on a rebound the velocity change is 20 + 5.0 = 25 m s⁻¹ because the direction reverses, and the force is then 25 × 25 = 625 N, greater than before."],
    itype="short_answer",
    prov=PROV + " Structured question around one situation, in the style of Paper 2."))

ITEMS.append(item("ITEM-9702-3-P03",
    ["OBJ-9702-3.1-03", "OBJ-9702-3.1-04"],
    ["CLM-9702-3-007", "CLM-9702-3-009", "CLM-9702-3-010"],
    None, ["AO1", "AO2"], "Apply", "Calculate", 5, 3,
    "At a vehicle testing ground outside Otjiwarongo, a car of mass 1500 kg moving at 16 m s⁻¹ is stopped by a crash barrier, first in 0.25 s and then, with a crumple section fitted to the barrier, in 0.60 s.\n"
    "(a) Calculate the momentum of the car before the impact.\n"
    "(b) Calculate the average force on the car during the first stop.\n"
    "(c) Calculate the average force with the crumple section fitted, and give your answers to the number of significant figures the data justify.",
    "(a) The equation in symbols: p = mv, where m is the mass in kg and v the velocity in m s⁻¹. Substitution: p = 1500 × 16 = 24000 kg m s⁻¹, which is 2.4 × 10⁴ kg m s⁻¹ to two significant figures.\n"
    "(b) The car's momentum falls from 24000 kg m s⁻¹ to zero, so ∆p = 24000 N s. The equation: F = ∆p ÷ ∆t. Substitution: F = 24000 ÷ 0.25 = 96000 N, which is 9.6 × 10⁴ N to two significant figures.\n"
    "(c) The same momentum change over 0.60 s: F = 24000 ÷ 0.60 = 40000 N, which is 4.0 × 10⁴ N to two significant figures. The data are given to two significant figures (16, 0.25, 0.60), so the answers are stated to two. The crumple section cuts the force from 96000 N to 40000 N because it stretches the same momentum change over a longer time.",
    ["Equation: p = mv for part (a), and F = ∆p ÷ ∆t for parts (b) and (c) - 1 mark.",
     "Substitution and working: 1500 × 16 = 24000 kg m s⁻¹, then 24000 ÷ 0.25 = 96000 N and 24000 ÷ 0.60 = 40000 N - 2 marks.",
     "Answer with its unit: 2.4 × 10⁴ kg m s⁻¹, 9.6 × 10⁴ N and 4.0 × 10⁴ N, each given to two significant figures, the choice justified by the precision of the data - 2 marks."],
    itype="calculation",
    prov=PROV + " Multi-step calculation in an everyday situation, in the style of Paper 2."))

# ---------------------------------------------------------------- write out
os.makedirs(os.path.join(HERE, 'claims'), exist_ok=True)
os.makedirs(os.path.join(HERE, 'content-units'), exist_ok=True)
os.makedirs(os.path.join(HERE, 'learning-items'), exist_ok=True)

with open(os.path.join(HERE, 'claims', 'canonical_claim_ledger.json'), 'w') as f:
    json.dump({"ledger_id": "CLM-LEDGER-9702-3", "claims": C}, f, indent=1, ensure_ascii=False)

for u in UNITS:
    with open(os.path.join(HERE, 'content-units', u["unit_id"] + '.json'), 'w') as f:
        json.dump(u, f, indent=1, ensure_ascii=False)

with open(os.path.join(HERE, 'learning-items', 'topic_3_items.json'), 'w') as f:
    json.dump({"dataset_id": "ITEMS-9702-3", "topic_id": "3", "items": ITEMS}, f, indent=1, ensure_ascii=False)

AUTHORING_NOTES = {
    "topic_id": "3",
    "deviations": [
        {
            "from": "The work order's eleven MISCON slots declare a misconception_entry field (e.g. misconception_entry: MC-9702-3-01) to be carried onto the item.",
            "to": "The misconception entry id is recorded in the item's provenance string instead, and each MISCON card's prompt, canonical answer and marking guidance name the error and its test from curriculum/misconceptions.json.",
            "why": "The learning_items schema (standard v0.2.0-draft) sets additionalProperties: false and has no misconception_entry field, so the entry id cannot live on the item itself without failing C-00."
        },
        {
            "from": "The P01 brief asks for 2-4 objectives that the task genuinely exercises.",
            "to": "Four objectives are listed (OBJ-9702-3.1-03, OBJ-9702-3.1-04, OBJ-9702-3.2-03, OBJ-9702-3.3-02) as the spine of the twelve-question set; the remaining questions exercise further objectives of the topic, as a Paper 1 section does.",
            "why": "The twelve questions span the topic's objectives; listing all nine they touch would break the brief's own 2-4 limit, so the four the set leans on hardest are named and the rest are covered by their own flashcards."
        }
    ]
}
with open(os.path.join(HERE, 'authoring_notes.json'), 'w') as f:
    json.dump(AUTHORING_NOTES, f, indent=1, ensure_ascii=False)

print("claims:", len(C))
for u in UNITS:
    print(u["unit_id"], "words:", u["word_count"], "budget:", u["word_budget"])
print("items:", len(ITEMS))
