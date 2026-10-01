"""Build the 65 learning items for CIE 9702 AS Physics topic 4 (Forces, density and pressure).

Run from the REPO ROOT:
    python3 work/cie-9702-as-2025-2027/topics/4/build_items.py
"""
import json
import os
import sys

REPO = '/Users/professor/Documents/YYeni Study Resources'
sys.path.insert(0, os.path.join(REPO, 'standard/v0.2.0-draft/checks'))
from yyeni_checks import _artefact_text
import hashlib

WS = os.path.join(REPO, 'work/cie-9702-as-2025-2027')
TOPIC = '4'

# claim revision map from the ledger
ledger = json.load(open(os.path.join(WS, 'topics/4/claims/canonical_claim_ledger.json')))
REV = {c['claim_id']: c['revision'] for c in ledger['claims']}

items = []


def _stamp(item, claims):
    """Attach provenance, qa_status, claims_seen and authored_hash."""
    item.setdefault('context', {'sector': None, 'business_size': None, 'ownership': None,
                                 'situation': None, 'facts': []})
    item.setdefault('prerequisite_item_ids', [])
    item.setdefault('core_status', 'core')
    item.setdefault('intentional_duplicate_group', None)
    item['provenance'] = 'Authored for CIE 9702 AS Physics topic 4 from the topic claim ledger and work order.'
    item['qa_status'] = 'review_required'
    item['claims_seen'] = {cid: REV[cid] for cid in claims}
    item['authored_hash'] = hashlib.sha256(_artefact_text(item).encode()).hexdigest()
    return item


def flash(item_id, slot, objective_id, claims, prompt, canonical_answer, guidance,
          command_word, subtype, assessment_objectives, blooms_level, mark_tariff,
          difficulty, misconception_entry=None):
    it = {
        'item_id': item_id,
        'objective_ids': [objective_id],
        'claim_ids': list(claims),
        'item_type': 'flashcard',
        'subtype': subtype,
        'assessment_objectives': assessment_objectives,
        'blooms_level': blooms_level,
        'command_word': command_word,
        'mark_tariff': mark_tariff,
        'difficulty': difficulty,
        'prompt': prompt,
        'canonical_answer': canonical_answer,
        'marking_guidance': guidance,
        'context': {'sector': None, 'business_size': None, 'ownership': None,
                    'situation': None, 'facts': []},
        'prerequisite_item_ids': [],
        'core_status': 'core',
        'intentional_duplicate_group': None,
    }
    _stamp(it, claims)
    items.append(it)


# ---------------------------------------------------------------------------
# OBJ-9702-4.1-01  centre of gravity
# ---------------------------------------------------------------------------
flash('ITEM-9702-4-001-DEF', 1, 'OBJ-9702-4.1-01', ['CLM-9702-4-001'],
      'State what is meant by the centre of gravity of an object.',
      'The centre of gravity of an object is the single point at which the whole weight of the object may be taken to act.',
      ['1 mark: the definition as the point where the whole weight may be taken to act. A statement in terms of mass, or of the pull of gravity, does not carry the mark: the weight may be taken to act there, and that is the whole meaning.'],
      'State', 'DEF', ['AO1'], 'Remember', 1, 2)

flash('ITEM-9702-4-002-MECH', 2, 'OBJ-9702-4.1-01', ['CLM-9702-4-002', 'CLM-9702-4-003'],
      'A uniform beam rests on a pivot placed directly under its mid-point, and the beam sits level. Explain how the idea of the centre of gravity shows that the beam does not start to turn.',
      'The centre of gravity of the uniform beam sits at its geometric centre, directly above the pivot, because for a uniform object of symmetrical shape the centre of gravity is at the geometric centre. Taking the whole weight as a single force acting at that point gives the same turning effect as the weights of all the parts of the beam acting separately, so the whole weight acts along a line passing through the pivot. The perpendicular distance from the pivot to the line of action of the weight is zero, so the weight has no moment about the pivot, and the beam does not start to turn.',
      ['The beam\'s centre of gravity sits at its geometric centre, directly above the pivot, and the single weight taken to act there reproduces the turning effect of all the parts - 1 mark.',
       'Because the weight then acts through the pivot, its moment about the pivot is zero, so there is nothing to turn the beam - 1 mark.'],
      'Explain', 'MECH', ['AO2'], 'Understand', 2, 2)

flash('ITEM-9702-4-036-MISCON', 36, 'OBJ-9702-4.1-01', ['CLM-9702-4-001', 'CLM-9702-4-002'],
      'A learner writes: "The centre of gravity of an object is the point where the Earth\'s pull on the object is concentrated, so the weight really acts there and nowhere else." Explain the error in this statement.',
      'The error is treating the centre of gravity as the point where the weight really acts, or as a point defined by mass or the pull of gravity. In fact the Earth pulls on every part of the object, and the single force at the centre of gravity is a shortcut: the whole weight may be taken to act there because it gives the same turning effect as all the parts acting together. The test is whether the definition says the weight is taken to act there; a real point of application is not being claimed.',
      ['1 mark: the error named - the weight is taken to act at the centre of gravity, it does not really act only there; the Earth pulls on every part, and the point is a shortcut that reproduces the same turning effect, not a concentration of mass or pull.'],
      'Explain', 'MISCON', ['AO1'], 'Understand', 1, 3,
      misconception_entry='MC-9702-4-01')

flash('ITEM-9702-4-046-FEATURE', 46, 'OBJ-9702-4.1-01', ['CLM-9702-4-002'],
      'State two features of the centre of gravity of an object.',
      'Two features: for a uniform object of symmetrical shape it sits at the geometric centre; and for some objects, such as a uniform ring, it lies outside the material of the object altogether.',
      ['1 mark per feature: any two correct features, such as its position at the geometric centre of a uniform symmetrical object, the property that it lies outside the material for a ring, or that it is the point where the moments of the weights of all the parts balance.'],
      'State', 'FEATURE', ['AO1'], 'Remember', 1, 3)

flash('ITEM-9702-4-059-DIST', 59, 'OBJ-9702-4.1-01', ['CLM-9702-4-002'],
      'A uniform metre rule and a uniform ring both have a centre of gravity. State how the position of the centre of gravity differs between them.',
      'Both are uniform and symmetrical, so in both cases the centre of gravity sits at the geometric centre of the object. The difference is where that centre lies: for the metre rule the centre of gravity is inside the material of the rule, at the 50 cm mark, whereas for the ring the geometric centre is in the empty space of the hole, so the centre of gravity lies outside the material of the ring.',
      ['1 mark: the difference - the rule\'s centre of gravity is within its material while the ring\'s lies outside the material, in the space of the hole; both sit at the geometric centre, and the contrast is the position relative to the material.'],
      'State', 'DIST', ['AO1'], 'Understand', 1, 3)

# ---------------------------------------------------------------------------
# OBJ-9702-4.1-02  moment of a force
# ---------------------------------------------------------------------------
flash('ITEM-9702-4-003-DEF', 3, 'OBJ-9702-4.1-02', ['CLM-9702-4-004', 'CLM-9702-4-005'],
      'Define the moment of a force about a point.',
      'The moment of a force about a point is the force multiplied by the perpendicular distance from the point to the line of action of the force. In symbols, moment = Fd, where F is the force in newtons (N), d is the perpendicular distance in metres (m), and the unit of moment is the newton metre (N m).',
      ['1 mark: the definition as force × perpendicular distance from the point to the line of action, with the equation and its unit named.'],
      'Define', 'DEF', ['AO1'], 'Remember', 1, 1)

flash('ITEM-9702-4-004-CALC', 4, 'OBJ-9702-4.1-02', ['CLM-9702-4-005', 'CLM-9702-4-006'],
      'A door in a classroom in Tsumeb is 0.85 m wide, hinged along one edge. A student pushes the door with a force of 12 N at right angles to the door, at the edge furthest from the hinge. Calculate the moment of the force about the hinge.',
      'Moment = Fd, where F is the force and d is the perpendicular distance from the hinge to the line of action of the force. Substitution: moment = 12 N × 0.85 m = 10.2 N m. The moment is 10 N m to two significant figures.',
      ['Equation and substitution: moment = Fd with F = 12 N and d = 0.85 m, the width of the door, measured perpendicular to the force - 1 mark (the first step).',
       'Answer: 10.2 N m, giving 10 N m to two significant figures, with the unit - 1 mark. Using the diagonal distance to the handle, or the distance along the door\'s face, is the wrong distance.'],
      'Calculate', 'CALC', ['AO2'], 'Apply', 2, 1)

flash('ITEM-9702-4-037-MISCON', 37, 'OBJ-9702-4.1-02', ['CLM-9702-4-004', 'CLM-9702-4-006'],
      'A learner calculates the moment of a force about a pivot by multiplying the force by the distance from the pivot to the point where the force is applied, measured along the lever. The force is not at right angles to the lever. Explain the error and how to correct it.',
      'The error is multiplying the force by a distance that is not perpendicular to it. The moment is the force multiplied by the perpendicular distance from the pivot to the line of action of the force, not the distance to the point of application measured along the lever. The correction is to use the perpendicular distance from the pivot to the force\'s line of action, or to multiply the force by the sine of the angle it makes with the lever and by the distance along the lever, which is the same thing.',
      ['1 mark: the error named - the distance used is not perpendicular to the force; the distance needed is the perpendicular distance from the pivot to the line of action, or equivalently the force\'s perpendicular component, instead of the slant distance along the lever.'],
      'Explain', 'MISCON', ['AO1'], 'Understand', 1, 2,
      misconception_entry='MC-9702-4-02')

flash('ITEM-9702-4-054-FEATURE', 54, 'OBJ-9702-4.1-02', ['CLM-9702-4-005', 'CLM-9702-4-006'],
      'State two features of the moment of a force about a point.',
      'Two features: its size is the force multiplied by the perpendicular distance from the point to the line of action of the force, measured in newton metres; and a force whose line of action passes through the point has zero moment about that point, however large the force is.',
      ['1 mark per feature: any two correct features, such as the unit N m, the zero moment of a force acting through the point, or the dependence of the moment on the perpendicular distance rather than the slant distance.'],
      'State', 'FEATURE', ['AO1'], 'Remember', 1, 2)

# ---------------------------------------------------------------------------
# OBJ-9702-4.1-03  couple
# ---------------------------------------------------------------------------
flash('ITEM-9702-4-005-DEF', 5, 'OBJ-9702-4.1-03', ['CLM-9702-4-008', 'CLM-9702-4-009'],
      'State what is meant by a couple.',
      'A couple is a pair of forces that are equal in size, opposite in direction and parallel, and whose lines of action do not coincide. The two forces sum to zero, so a couple produces no resultant force: it acts to produce rotation only.',
      ['1 mark: the definition as a pair of equal, opposite, parallel forces whose lines of action do not coincide, producing rotation only. A single force turning something is not a couple.'],
      'State', 'DEF', ['AO1'], 'Remember', 1, 2)

flash('ITEM-9702-4-006-MECH', 6, 'OBJ-9702-4.1-03', ['CLM-9702-4-009', 'CLM-9702-4-010'],
      'A driver turns a steering wheel by pushing one side of the rim with a force of 9.0 N and pulling the opposite side with a force of 9.0 N, both forces tangential to the rim and opposite in direction. Explain how these two forces turn the wheel without pushing it sideways.',
      'The two forces are equal in size and opposite in direction, so as pushes they sum to zero: no resultant force acts on the wheel, and it is not pushed sideways. Because their lines of action do not coincide, the two forces do produce a turning effect. Each force has a moment about the centre of the wheel in the same sense, so the moments add, and the total moment comes out the same whatever point is chosen: the pair of forces acts to produce rotation only.',
      ['How the push cancels: the forces are equal and opposite, so they sum to zero and give no resultant push - 1 mark.',
       'How the turn survives: because the lines of action do not coincide, each force has a moment in the same sense, so the pair produces rotation only - 1 mark.'],
      'Explain', 'MECH', ['AO2'], 'Understand', 2, 2)

flash('ITEM-9702-4-047-FEATURE', 47, 'OBJ-9702-4.1-03', ['CLM-9702-4-008', 'CLM-9702-4-010'],
      'State two features of the total moment of a couple.',
      'Two features: it is the same about every point in the plane of the couple, whatever point is chosen as the pivot; and it is a pure turning effect, because the two forces sum to zero and leave no resultant force.',
      ['1 mark per feature: any two correct features, such as the total moment being independent of the chosen point, the zero resultant force, or the requirement that the two forces be equal, opposite and parallel.'],
      'State', 'FEATURE', ['AO1'], 'Remember', 1, 3)

flash('ITEM-9702-4-060-DIST', 60, 'OBJ-9702-4.1-03', ['CLM-9702-4-009', 'CLM-9702-4-010'],
      'One force acts alone on a wheel; two equal and opposite parallel forces act on a second wheel, their lines of action apart. State the difference between the turning effects the two wheels experience.',
      'The single force both pushes and turns: it has a moment about a point not on its line of action, and it also leaves a resultant force on the wheel, equal to itself. The pair of forces is a couple: the two forces sum to zero, so there is no resultant force, and the pair produces rotation only, with a total moment that is the same about every point. The difference is that the single force gives turning together with a push, whereas the couple gives turning alone.',
      ['1 mark: the difference - the single force leaves a resultant push as well as a moment, whereas the couple produces rotation only, its forces summing to zero and its total moment being the same about any point.'],
      'State', 'DIST', ['AO1'], 'Understand', 1, 3)

# ---------------------------------------------------------------------------
# OBJ-9702-4.1-04  torque of a couple
# ---------------------------------------------------------------------------
flash('ITEM-9702-4-007-DEF', 7, 'OBJ-9702-4.1-04', ['CLM-9702-4-011', 'CLM-9702-4-012'],
      'Define the torque of a couple.',
      'The torque of a couple is one of the forces multiplied by the perpendicular distance between the lines of action of the two forces. In symbols, torque = Fs, where F is one of the forces in newtons (N), s is the perpendicular distance between the forces in metres (m), and the unit of torque is the newton metre (N m).',
      ['1 mark: the definition as one force × the perpendicular distance between the lines of action, with the equation and its unit named.'],
      'Define', 'DEF', ['AO1'], 'Remember', 1, 1)

flash('ITEM-9702-4-008-CALC', 8, 'OBJ-9702-4.1-04', ['CLM-9702-4-012', 'CLM-9702-4-013'],
      'A mechanic tightens a bolt with a torque wrench by gripping opposite sides of a disc of diameter 0.24 m. Each hand applies 25 N tangentially to the edge of the disc, one up and one down. Calculate the torque applied to the bolt.',
      'The two hands form a couple. Torque = Fs, where F is one of the forces and s is the perpendicular distance between the two lines of action, which is the diameter of the disc. Substitution: torque = 25 N × 0.24 m = 6.0 N m. The torque is 6.0 N m to two significant figures.',
      ['Equation and substitution: torque = Fs with F = 25 N and s = 0.24 m, the diameter, because the forces act at opposite edges - 1 mark (the first step).',
       'Answer: 6.0 N m with the unit, to two significant figures - 1 mark. Using the radius 0.12 m gives 3.0 N m, which uses only half of the torque.'],
      'Calculate', 'CALC', ['AO2'], 'Apply', 2, 1)

flash('ITEM-9702-4-039-MISCON', 39, 'OBJ-9702-4.1-04', ['CLM-9702-4-009', 'CLM-9702-4-011'],
      'A learner meets this question: "Two parallel forces of 8.0 N each act on a wheel, opposite in direction, with lines of action 0.30 m apart. Find the resultant force and the torque." The learner answers: "Resultant force 16 N, torque 2.4 N m." Explain both errors and give the correct answers.',
      'The first error is treating the couple as if it gives a resultant force. The two forces are equal in size and opposite in direction, so they sum to zero: a couple produces no resultant force at all, and the correct resultant is 0 N, not 16 N. The torque answer is right in value but for the wrong reason shown, and a common slip halves it: the torque is one force multiplied by the full perpendicular distance between the lines of action, 8.0 N × 0.30 m = 2.4 N m. A learner taking moments about a point midway between the forces gets 8.0 N × 0.15 m from each force and must add both, 1.2 + 1.2 = 2.4 N m; quoting a single 1.2 N m is the half-torque error, and it is what the reasoning must avoid.',
      ['1 mark: the errors named - a couple gives no resultant force, its two forces summing to zero rather than adding, and the torque is one force × the full perpendicular distance between the lines of action, not half of it; the common error in the torque is quoting a single half-moment, and the correct answers are 0 N and 2.4 N m.'],
      'Explain', 'MISCON', ['AO1'], 'Understand', 1, 2,
      misconception_entry='MC-9702-4-04')

flash('ITEM-9702-4-055-FEATURE', 55, 'OBJ-9702-4.1-04', ['CLM-9702-4-012', 'CLM-9702-4-013'],
      'State two features of the torque of a couple.',
      'Two features: it is one of the forces multiplied by the perpendicular distance between the lines of action, measured in newton metres; and it can be stated without naming a pivot, because the total moment of a couple is the same about every point.',
      ['1 mark per feature: any two correct features, such as the unit N m, the independence of the chosen point, or the definition as one force × the separation of the lines of action.'],
      'State', 'FEATURE', ['AO1'], 'Remember', 1, 2)

# ---------------------------------------------------------------------------
# OBJ-9702-4.2-01  principle of moments
# ---------------------------------------------------------------------------
flash('ITEM-9702-4-009-DEF', 9, 'OBJ-9702-4.2-01', ['CLM-9702-4-014'],
      'State the principle of moments.',
      'For a body in equilibrium, the sum of the clockwise moments about a single point is equal to the sum of the anticlockwise moments about that same point.',
      ['1 mark: the definition names the two sums, the single point both are taken about, and the equilibrium condition. A statement with the sums but no common point, or with no equilibrium condition, is incomplete.'],
      'State', 'DEF', ['AO1'], 'Remember', 1, 2)

flash('ITEM-9702-4-010-CALC', 10, 'OBJ-9702-4.2-01', ['CLM-9702-4-014', 'CLM-9702-4-016'],
      'A seesaw in a park in Katutura has a pivot at its centre. A child of weight 320 N sits 1.5 m from the pivot on one side. Calculate how far from the pivot, on the other side, her friend of weight 480 N must sit for the seesaw to balance.',
      'The seesaw balances when the moments about the pivot are equal. The child\'s anticlockwise moment: 320 N × 1.5 m = 480 N m. The friend\'s clockwise moment must equal it: 480 N × d = 480 N m, so d = 480 ÷ 480 = 1.0 m. The friend sits 1.0 m from the pivot, that is 1.0 m to two significant figures.',
      ['Equation and working: the moments about the pivot, 320 × 1.5 = 480 N m anticlockwise set equal to 480 × d clockwise - 1 mark (the first step).',
       'Answer: d = 480 ÷ 480 = 1.0 m with the unit, to two significant figures - 1 mark. Sitting the friend 1.5 m out as well ignores the different weight.'],
      'Calculate', 'CALC', ['AO2'], 'Apply', 2, 2)

flash('ITEM-9702-4-011-CALC', 11, 'OBJ-9702-4.2-01', ['CLM-9702-4-014', 'CLM-9702-4-015'],
      'A non-uniform beam of weight 90.0 N and length 2.40 m rests on a pivot at one end, A, and is held horizontal by a vertical rope at the other end, B. The rope\'s tension is 60.0 N. The beam\'s centre of gravity is a distance d from A. Calculate d.',
      'The beam is in equilibrium, so the moments about any single point balance. Take moments about A, which removes the pivot\'s reaction from the equation. The rope\'s tension at B gives an anticlockwise moment of 60.0 N × 2.40 m = 144 N m. The weight gives a clockwise moment of 90.0 N × d. Setting them equal: 90.0 × d = 144, so d = 144 ÷ 90.0 = 1.60 m. The centre of gravity is 1.60 m from A, that is 1.60 m to three significant figures.',
      ['Equation: the moments balance, Σanticlockwise = Σclockwise about the single point A - 1 mark.',
       'Answer: 90.0 × d = 144 so d = 1.60 m with its unit, to three significant figures - 1 mark.'],
      'Calculate', 'CALC', ['AO2'], 'Apply', 2, 2)

flash('ITEM-9702-4-012-CALC', 12, 'OBJ-9702-4.2-01', ['CLM-9702-4-014', 'CLM-9702-4-016'],
      'A uniform plank of weight 150 N and length 3.0 m rests on a support at one end, A, and on a second support 2.1 m from A, overhanging it by 0.90 m. The plank is in equilibrium. Calculate the force from the second support on the plank.',
      'Take moments about A, which removes the first support\'s force from the equation. The plank is uniform, so its weight acts at its centre, 1.5 m from A, giving a clockwise moment of 150 N × 1.5 m = 225 N m. The second support\'s force R acts upward at 2.1 m from A, giving an anticlockwise moment of R × 2.1 m. Balance: R × 2.1 = 225, so R = 225 ÷ 2.1 = 107 N. The second support pushes up with 107 N, that is 110 N to two significant figures.',
      ['Equation: the moments balance about the single point A, weight 150 × 1.5 = 225 N m clockwise against support force R × 2.1 m anticlockwise - 1 mark.',
       'Answer: R = 225 ÷ 2.1 = 107 N, which is 110 N to two significant figures, with the unit - 1 mark.'],
      'Calculate', 'CALC', ['AO2'], 'Apply', 2, 2)

flash('ITEM-9702-4-038-MISCON', 38, 'OBJ-9702-4.2-01', ['CLM-9702-4-014'],
      'A learner states the principle of moments as: "Clockwise moments equal anticlockwise moments." Explain why this statement is incomplete.',
      'The error is stating the principle without the sums, the common point or the equilibrium condition. The full statement is: for a body in equilibrium, the sum of the clockwise moments about a single point is equal to the sum of the anticlockwise moments about that same point. Without the equilibrium condition the claim is false in general: a body out of equilibrium has unequal moments. Without naming a single common point, the two sums could be taken about different points and the equality means nothing.',
      ['1 mark: the error named - the sums, the single point and the equilibrium condition are all missing; the equality holds only for a body in equilibrium, and only when both sums are taken about the same point.'],
      'Explain', 'MISCON', ['AO1'], 'Understand', 1, 3,
      misconception_entry='MC-9702-4-03')

flash('ITEM-9702-4-048-FEATURE', 48, 'OBJ-9702-4.2-01', ['CLM-9702-4-015', 'CLM-9702-4-016'],
      'State two features of how the principle of moments is applied.',
      'Two features: the point for taking moments can be chosen freely, and choosing a point that an unknown force acts through removes that force from the equation, because its moment about that point is zero; and any force that acts at an angle is resolved into components first, or its perpendicular distance is measured directly, before each moment is calculated.',
      ['1 mark per feature: any two correct features, such as the free choice of the point, the removal of an unknown force by taking moments where it acts, or the resolving of slanted forces before summing the moments.'],
      'State', 'FEATURE', ['AO1'], 'Remember', 1, 3)

flash('ITEM-9702-4-061-DIST', 61, 'OBJ-9702-4.2-01', ['CLM-9702-4-014', 'CLM-9702-4-016'],
      'Moments can be taken about a support of a balanced beam, or about the beam\'s far end, where no force acts. State the difference between the two choices when the moments equation is written down.',
      'Both choices are valid, because the principle holds about any single point. The difference is what each equation contains. About the support, the support\'s own force has zero moment and disappears from the equation, leaving only the weights and any other forces. About the far end, the support\'s force does appear, as does every other force, so the equation has more terms and contains the unknown support force. The support choice is the one that removes an unknown; the far-end choice keeps it in.',
      ['1 mark: the difference - about the support the support\'s force drops out of the equation, whereas about a point no force acts through every force appears, including the support\'s; both hold for a body in equilibrium, and the contrast is which forces the equation contains.'],
      'State', 'DIST', ['AO1'], 'Understand', 1, 3)

# ---------------------------------------------------------------------------
# OBJ-9702-4.2-02  equilibrium
# ---------------------------------------------------------------------------
flash('ITEM-9702-4-013-DEF', 13, 'OBJ-9702-4.2-02', ['CLM-9702-4-017'],
      'State the conditions for a system to be in equilibrium.',
      'A system is in equilibrium when the resultant force on it is zero and the resultant torque on it is zero. Both conditions must hold at the same time.',
      ['1 mark: the definition names both zero resultants - force and torque - as the two conditions. One condition alone is incomplete.'],
      'State', 'DEF', ['AO1'], 'Remember', 1, 2)

flash('ITEM-9702-4-014-MECH', 14, 'OBJ-9702-4.2-02', ['CLM-9702-4-017', 'CLM-9702-4-019'],
      'A picture hangs motionless on a single nail, with two forces acting on it: its weight, and the push of the nail. Explain how the two equilibrium conditions apply to the picture.',
      'First condition: the resultant force on the picture is zero, because the nail\'s push on it balances its weight; the two forces are equal in size and opposite in direction. Second condition: the resultant torque on it is zero; the nail\'s push acts through the point where the string sits, and the weight of the picture acts through its centre of gravity, and because the picture hangs so that these two forces act along the same line, neither causes a turn. With no resultant force and no resultant torque, the picture does not accelerate and does not begin to rotate, so it stays at rest.',
      ['How the forces balance: the nail\'s push equals the weight, so the resultant force is zero - 1 mark.',
       'How the turning balances: the two forces act along the same line, so the resultant torque is zero, and with both conditions met the picture neither accelerates nor begins to rotate - 1 mark.'],
      'Explain', 'MECH', ['AO2'], 'Understand', 2, 2)

flash('ITEM-9702-4-040-MISCON', 40, 'OBJ-9702-4.2-02', ['CLM-9702-4-017', 'CLM-9702-4-018'],
      'A ball is thrown straight up. At the highest point of its flight the ball is momentarily at rest. A learner concludes that at that instant the ball is in equilibrium. Explain the error.',
      'The error is concluding equilibrium from being at rest. Being at rest shows nothing about the forces. At the highest point the ball\'s weight still acts on it, so the resultant force on the ball is not zero, and the ball is not in equilibrium: it accelerates downward at g at that very instant. Equilibrium requires zero resultant force and zero resultant torque, checked as two separate conditions, not one.',
      ['1 mark: the error named - rest does not show equilibrium; at the top the weight still acts, so the resultant force is not zero and the ball accelerates, which is not the state of zero resultant force and zero resultant torque.'],
      'Explain', 'MISCON', ['AO1'], 'Understand', 1, 3,
      misconception_entry='MC-9702-4-05')

flash('ITEM-9702-4-049-FEATURE', 49, 'OBJ-9702-4.2-02', ['CLM-9702-4-017', 'CLM-9702-4-019'],
      'State two features of a system in equilibrium.',
      'Two features: the resultant force on it is zero and the resultant torque on it is zero, both at the same time; and it does not accelerate and does not begin to rotate, so it stays at rest or continues at a steady velocity without starting to turn.',
      ['1 mark per feature: any two correct features, such as the two zero resultants, the absence of acceleration, or the absence of any starting to rotate.'],
      'State', 'FEATURE', ['AO1'], 'Remember', 1, 3)

flash('ITEM-9702-4-062-DIST', 62, 'OBJ-9702-4.2-02', ['CLM-9702-4-017', 'CLM-9702-4-018'],
      'A box sits at rest on a flat floor, in equilibrium. A second box is dropped and passes the top of its fall, momentarily at rest but not in equilibrium. State the difference between the two situations.',
      'Both boxes are at rest at the instant described, but the difference is in the forces. The box on the floor has zero resultant force acting on it - its weight is balanced by the floor\'s push - and zero resultant torque, so it satisfies both equilibrium conditions. The falling box at the top of its flight has its weight acting on it with nothing balancing it, so the resultant force on it is not zero, and it is not in equilibrium however still it looks. Being at rest is not what makes the difference; the zero resultants are.',
      ['1 mark: the difference - the resting box has both resultants zero whereas the falling box has an unbalanced weight, so rest alone is not the distinction; the zero resultant force and zero resultant torque are.'],
      'State', 'DIST', ['AO1'], 'Understand', 1, 3)

# ---------------------------------------------------------------------------
# OBJ-9702-4.2-03  vector triangle
# ---------------------------------------------------------------------------
flash('ITEM-9702-4-015-DEF', 15, 'OBJ-9702-4.2-03', ['CLM-9702-4-020', 'CLM-9702-4-021'],
      'State how a vector triangle represents three coplanar forces in equilibrium.',
      'The three forces are drawn head to tail, each as an arrow parallel to one of the forces and scaled to its size. Because the forces are in equilibrium, the third arrow\'s tip returns to the first arrow\'s tail: the triangle closes. A closed triangle of vectors has no resultant, so the forces it represents balance, and no side of the triangle is a resultant force.',
      ['1 mark: the definition names the head-to-tail construction and the closed triangle, with no side being a resultant.'],
      'State', 'DEF', ['AO1'], 'Remember', 1, 2)

flash('ITEM-9702-4-016-CALC', 16, 'OBJ-9702-4.2-03', ['CLM-9702-4-020', 'CLM-9702-4-022'],
      'A lamp of weight 24 N hangs from a cable that makes an angle of 35° with the vertical, pulled sideways by a horizontal cord so that it is in equilibrium. Using a vector triangle, calculate the tension in the cable.',
      'The three forces in equilibrium are the weight 24 N straight down, the cable\'s tension T along the cable at 35° to the vertical, and the cord\'s horizontal pull. Drawn head to tail they close as a right-angled triangle: the weight is the side adjacent to the 35° angle, the horizontal pull is the side opposite it, and the tension is the hypotenuse. So cos 35° = 24 ÷ T, which gives T = 24 ÷ cos 35° = 24 ÷ 0.819 = 29.3 N. The tension is 29 N to two significant figures.',
      ['The triangle: weight down, tension along the cable, horizontal pull closing it, with the tension as the hypotenuse and the weight adjacent to the 35° angle - 1 mark.',
       'The equation and answer: T = 24 ÷ cos 35° = 29.3 N, which is 29 N to two significant figures, with the unit - 1 mark.'],
      'Calculate', 'CALC', ['AO2'], 'Apply', 2, 2)

flash('ITEM-9702-4-017-CALC', 17, 'OBJ-9702-4.2-03', ['CLM-9702-4-020', 'CLM-9702-4-022'],
      'A sign of weight 60 N hangs in equilibrium from two ropes. Each rope makes an angle of 25° with the vertical, one on each side, and the tensions in the two ropes are equal. Using a vector triangle, calculate the tension in each rope.',
      'By symmetry the two tensions T are equal, and each makes 25° with the vertical. The three forces - the weight down and the two tensions - close as a triangle in which the vertical components of the two tensions together carry the weight: 2 × T × cos 25° = 60 N. So T = 60 ÷ (2 × cos 25°) = 60 ÷ 1.812 = 33.1 N. The tension is 33 N to two significant figures.',
      ['The triangle and its geometry: two equal tensions at 25° to the vertical balancing the 60 N weight, drawn head to tail and closing - 1 mark.',
       'The equation and answer: 2T cos 25° = 60, so T = 33.1 N, which is 33 N to two significant figures, with the unit - 1 mark.'],
      'Calculate', 'CALC', ['AO2'], 'Apply', 2, 2)

flash('ITEM-9702-4-018-CALC', 18, 'OBJ-9702-4.2-03', ['CLM-9702-4-020', 'CLM-9702-4-022'],
      'A washing line in Okahandja sags in the middle. At the lowest point, the two halves of the line each make an angle of 20° with the horizontal, and a basket of weight 18 N hangs in equilibrium from that point. Using a vector triangle, calculate the tension in each half of the line.',
      'The three forces at the lowest point - the basket\'s weight 18 N down and the two tensions T along the line halves - are in equilibrium and close as a triangle. Each tension makes 20° with the horizontal, so it makes 70° with the vertical. The vertical components of the two tensions together carry the weight: 2 × T × cos 70° = 18 N. So T = 18 ÷ (2 × cos 70°) = 18 ÷ 0.684 = 26.3 N. The tension is 26 N to two significant figures.',
      ['The triangle and its geometry: two equal tensions at 70° to the vertical balancing the 18 N weight, closing head to tail - 1 mark.',
       'The equation and answer: 2T cos 70° = 18, so T = 26.3 N, which is 26 N to two significant figures, with the unit - 1 mark. Using 20° with the vertical instead of 70° gives 9.6 N, the angle confusion.'],
      'Calculate', 'CALC', ['AO2'], 'Apply', 2, 2)

flash('ITEM-9702-4-041-MISCON', 41, 'OBJ-9702-4.2-03', ['CLM-9702-4-020', 'CLM-9702-4-021'],
      'A learner draws the triangle of vectors for a picture hanging in equilibrium from two wires, and labels the shortest side of the triangle "resultant". Explain the error.',
      'The error is labelling one side of the triangle of forces for a body in equilibrium as the resultant. The three sides of the closed triangle are the three forces themselves, drawn head to tail; the triangle closes precisely because the forces add to zero, and a closed triangle of vectors has no resultant. There is no resultant force to label: equilibrium means the resultant is zero, and no side of the closed triangle represents it.',
      ['1 mark: the error named - in equilibrium the triangle closes and its sides are the three forces themselves, so there is no resultant; the test is whether the triangle closes, and it does.'],
      'Explain', 'MISCON', ['AO1'], 'Understand', 1, 3,
      misconception_entry='MC-9702-4-06')

flash('ITEM-9702-4-050-FEATURE', 50, 'OBJ-9702-4.2-03', ['CLM-9702-4-020', 'CLM-9702-4-022'],
      'State two features of the vector triangle for three coplanar forces in equilibrium.',
      'Two features: it closes, because the forces drawn head to tail add to zero, and no side of it is a resultant force; and its inside angles come from the geometry of the situation, such as the angle a rope makes with the vertical, from which the force sizes follow by trigonometry.',
      ['1 mark per feature: any two correct features, such as the closed triangle, the sides being the forces themselves, or the angles coming from the situation\'s geometry.'],
      'State', 'FEATURE', ['AO1'], 'Remember', 1, 3)

# ---------------------------------------------------------------------------
# OBJ-9702-4.3-01  density
# ---------------------------------------------------------------------------
flash('ITEM-9702-4-019-DEF', 19, 'OBJ-9702-4.3-01', ['CLM-9702-4-023'],
      'Define density.',
      'Density is mass per unit volume: ρ = m/V, where ρ is the density, m is the mass in kilograms (kg), V is the volume in cubic metres (m³), and the unit of density is kg m⁻³.',
      ['1 mark: the definition as mass per unit volume with the equation and its unit named.'],
      'Define', 'DEF', ['AO1'], 'Remember', 1, 1)

flash('ITEM-9702-4-020-CALC', 20, 'OBJ-9702-4.3-01', ['CLM-9702-4-023', 'CLM-9702-4-025'],
      'A drum in a shebeen in Ondangwa holds 200 litres of oil. The mass of the oil is 168 kg. Calculate the density of the oil.',
      'Convert first: 200 litres = 0.200 m³, because 1 litre = 1.0 × 10⁻³ m³. Then ρ = m/V, so ρ = 168 kg ÷ 0.200 m³ = 840 kg m⁻³. The density is 840 kg m⁻³ to three significant figures.',
      ['Equation and substitution, with the volume converted to base units first: ρ = m/V with m = 168 kg and V = 0.200 m³ - 1 mark (the first step).',
       'Answer: 840 kg m⁻³ with the unit, to three significant figures - 1 mark. Dividing 168 by 200 gives 0.84, the litres left unconverted.'],
      'Calculate', 'CALC', ['AO2'], 'Apply', 2, 1)

flash('ITEM-9702-4-042-MISCON', 42, 'OBJ-9702-4.3-01', ['CLM-9702-4-024'],
      'A wooden block floats half-submerged in water. A learner says: "The block is in water, so its density is 1000 kg m⁻³, the density of water." Explain the error.',
      'The error is confusing the density of the object with the density of the fluid it sits in. Density is mass per unit volume, and the ratio must use the mass and the volume of the same thing. The block\'s density is its own mass divided by its own volume; the water\'s density belongs with the volume of water the block displaces, which is what sets the upthrust. The test is to ask whose mass and whose volume are in the ratio: the block\'s density is found from the block alone.',
      ['1 mark: the error named - the fluid\'s density has been used for the object; density is mass per unit volume of the thing itself, and the fluid\'s density belongs with the displaced volume in the upthrust, not with the block\'s own density.'],
      'Explain', 'MISCON', ['AO1'], 'Understand', 1, 2,
      misconception_entry='MC-9702-4-07')

flash('ITEM-9702-4-056-FEATURE', 56, 'OBJ-9702-4.3-01', ['CLM-9702-4-023', 'CLM-9702-4-025'],
      'State two features of density.',
      'Two features: it is mass per unit volume, with unit kg m⁻³; and the density of a sample is found by measuring its mass and its volume and dividing the mass by the volume.',
      ['1 mark per feature: any two correct features, such as the definition as a ratio, the unit kg m⁻³, or the measurement route through mass and volume.'],
      'State', 'FEATURE', ['AO1'], 'Remember', 1, 2)

# ---------------------------------------------------------------------------
# OBJ-9702-4.3-02  pressure
# ---------------------------------------------------------------------------
flash('ITEM-9702-4-021-DEF', 21, 'OBJ-9702-4.3-02', ['CLM-9702-4-026'],
      'Define pressure.',
      'Pressure is force per unit area, acting at right angles to the area: p = F/A, where p is the pressure, F is the force in newtons (N), A is the area in square metres (m²), and the unit of pressure is the pascal (Pa), equal to one newton per square metre.',
      ['1 mark: the definition as force per unit area at right angles to the area, with the equation and its unit named.'],
      'Define', 'DEF', ['AO1'], 'Remember', 1, 1)

flash('ITEM-9702-4-022-CALC', 22, 'OBJ-9702-4.3-02', ['CLM-9702-4-026', 'CLM-9702-4-027'],
      'A builder in Swakopmund stands on a flat roof, and his weight of 720 N is spread evenly over the soles of both shoes, total area 0.040 m². Calculate the pressure on the roof.',
      'p = F/A, where F is the force and A is the area it acts over. Substitution: p = 720 N ÷ 0.040 m² = 18000 Pa. The pressure is 1.8 × 10⁴ Pa to two significant figures.',
      ['Equation and substitution: p = F/A with F = 720 N and A = 0.040 m² - 1 mark (the first step).',
       'Answer: 18000 Pa, which is 1.8 × 10⁴ Pa to two significant figures, with the unit - 1 mark. Multiplying instead of dividing gives 28.8, the inverted ratio.'],
      'Calculate', 'CALC', ['AO2'], 'Apply', 2, 1)

flash('ITEM-9702-4-057-FEATURE', 57, 'OBJ-9702-4.3-02', ['CLM-9702-4-026', 'CLM-9702-4-028'],
      'State two features of pressure in a fluid at rest.',
      'Two features: a fluid at rest presses at right angles against any surface it touches, whatever the orientation of that surface; and pressure is force per unit area measured in pascals, not a force measured in newtons.',
      ['1 mark per feature: any two correct features, such as the right-angle action on any surface, the pascal as the unit, or the distinction from force.'],
      'State', 'FEATURE', ['AO1'], 'Remember', 1, 2)

# ---------------------------------------------------------------------------
# OBJ-9702-4.3-03  derive ∆p = ρg∆h
# ---------------------------------------------------------------------------
flash('ITEM-9702-4-023-PROC', 23, 'OBJ-9702-4.3-03', ['CLM-9702-4-031', 'CLM-9702-4-029'],
      'Show, from the definitions of pressure and density, that the pressure difference between two depths ∆h apart in a liquid of density ρ is ∆p = ρg∆h. Set out the steps in order.',
      'Start with a vertical column of the liquid, cross-sectional area A, running from the upper depth to the lower depth, ∆h below it. Then find the weight of that column: its volume is A∆h, so its mass is m = ρA∆h from the definition of density, and its weight is W = mg = ρgA∆h. This weight presses on the base of the column, area A, so from the definition of pressure the extra pressure at the lower depth is ∆p = F/A = ρgA∆h ÷ A. The area cancels, and the result is ∆p = ρg∆h.',
      ['The order of the steps: first the column of area A and height ∆h, then the mass from the density definition, then the weight, then the division by the area - 1 mark.',
       'The definitions used: density for m = ρA∆h and pressure for ∆p = F/A, with the weight ρgA∆h as the measured quantity - 1 mark.',
       'The result: the area cancels, so the final equation is ∆p = ρg∆h - 1 mark. This gives the difference in pressure between the two depths.'],
      'Show', 'PROC', ['AO2'], 'Apply', 2, 3)

flash('ITEM-9702-4-024-CALC', 24, 'OBJ-9702-4.3-03', ['CLM-9702-4-029', 'CLM-9702-4-031'],
      'Show that the pressure at the bottom of a tank of water of depth 4.0 m exceeds the pressure at the surface by about 3.9 × 10⁴ Pa. The density of water is 1000 kg m⁻³ and g = 9.81 N kg⁻¹.',
      'The pressure difference between the surface and the bottom is ∆p = ρg∆h, which follows from the definitions of pressure and density. Substitution: ∆p = 1000 kg m⁻³ × 9.81 N kg⁻¹ × 4.0 m = 39240 Pa. This is 3.9 × 10⁴ Pa to two significant figures, which is the value to be shown.',
      ['Equation and substitution: ∆p = ρg∆h with ρ = 1000 kg m⁻³, g = 9.81 N kg⁻¹ and ∆h = 4.0 m - 1 mark.',
       'The result: 39240 Pa = 3.9 × 10⁴ Pa to two significant figures, matching the value given, with the unit - 1 mark.'],
      'Show', 'CALC', ['AO2'], 'Apply', 2, 3)

flash('ITEM-9702-4-025-APP', 25, 'OBJ-9702-4.3-03', ['CLM-9702-4-030', 'CLM-9702-4-032'],
      'A reservoir behind a dam near Keetmanshoop is 40 m deep at the wall; a neighbour\'s farm tank holds water 4.0 m deep. Both contain water, and both are open to the air. Explain, using the derivation of ∆p = ρg∆h, why the pressure difference from surface to bottom is ten times greater in the reservoir than in the tank.',
      'In this situation the derivation shows that the pressure difference from the surface to a depth is ∆p = ρg∆h, where ∆h is the vertical distance and the area has cancelled out. Because both hold the same liquid, ρ is the same, and g is the same; only ∆h differs. The reservoir\'s ∆h is 40 m and the tank\'s is 4.0 m, so since ∆p is proportional to ∆h, the reservoir\'s pressure difference is ten times the tank\'s: the shape and width of the container play no part, because the cross-sectional area cancelled in the derivation.',
      ['The situation given: the same liquid in both, so only the vertical depth ∆h differs - 1 mark.',
       'Because the area cancels in the derivation of ∆p = ρg∆h, the pressure difference depends on ∆h alone, so 40 m gives ten times the ∆p of 4.0 m - 1 mark.'],
      'Explain', 'APP', ['AO2'], 'Apply', 1, 3)

flash('ITEM-9702-4-045-FEATURE', 45, 'OBJ-9702-4.3-03', ['CLM-9702-4-030', 'CLM-9702-4-032'],
      'State two features of the equation ∆p = ρg∆h.',
      'Two features: it gives a difference in pressure between two depths, with ∆h measured vertically, whatever the shape of the container between them; and the cross-sectional area cancels in its derivation, so the pressure difference does not depend on the shape or width of the container.',
      ['1 mark per feature: any two correct features, such as the vertical ∆h, the pressure difference rather than a single pressure, or the independence from container shape.'],
      'State', 'FEATURE', ['AO1'], 'Remember', 1, 4)

flash('ITEM-9702-4-058-DIST', 58, 'OBJ-9702-4.3-03', ['CLM-9702-4-030', 'CLM-9702-4-035'],
      'A wide dam reservoir and a thin vertical pipe are filled with water to the same depth. State the difference between the pressure at the bottom of the reservoir and the pressure at the bottom of the pipe.',
      'There is no difference in the pressure difference from the surface: both have the same ∆h and the same liquid, so ∆p = ρg∆h is the same in both. What differs is the force on the base: the reservoir\'s base has a much larger area, so the same pressure acting on it gives a much larger force, whereas the pipe\'s narrow base carries a small force. The pressure at equal depth is the same; the force is not.',
      ['1 mark: the difference - the pressure at the same depth is the same, because ∆p = ρg∆h depends on ∆h and not on the width, whereas the force on the base differs with the area; both hold for the same liquid at the same depth.'],
      'State', 'DIST', ['AO1'], 'Understand', 1, 4)

# ---------------------------------------------------------------------------
# OBJ-9702-4.3-04  use ∆p = ρg∆h
# ---------------------------------------------------------------------------
flash('ITEM-9702-4-026-DEF', 26, 'OBJ-9702-4.3-04', ['CLM-9702-4-033', 'CLM-9702-4-035'],
      'State the equation for the pressure difference between two depths in a liquid, naming each symbol and its unit.',
      '∆p = ρg∆h, where ∆p is the pressure difference in pascals (Pa), ρ is the density of the liquid in kg m⁻³, g is the acceleration of free fall in N kg⁻¹, and ∆h is the vertical distance between the two depths in metres (m). Where the surface is open to the air, the total pressure at depth is the atmospheric pressure plus this difference.',
      ['1 mark: the equation with each symbol and its unit named, and the pressure difference - not a single pressure - identified as what it gives.'],
      'State', 'DEF', ['AO1'], 'Remember', 1, 2)

flash('ITEM-9702-4-027-CALC', 27, 'OBJ-9702-4.3-04', ['CLM-9702-4-033', 'CLM-9702-4-035'],
      'A borehole outside Gobabis has water standing 25 m below the top of the casing. The density of water is 1000 kg m⁻³ and g = 9.81 N kg⁻¹. Atmospheric pressure is 1.0 × 10⁵ Pa. Calculate the total pressure 25 m down, at the surface of the water in the hole.',
      'The pressure difference from the open top down to the water surface is ∆p = ρg∆h. First ρg = 1000 × 9.81 = 9810 Pa m⁻¹, then ∆p = 9810 × 25 = 245250 Pa. The total pressure there is the atmospheric pressure plus this difference: 1.0 × 10⁵ + 2.4525 × 10⁵ = 3.4525 × 10⁵ Pa, which is 3.5 × 10⁵ Pa to two significant figures.',
      ['Equation and substitution: ∆p = ρg∆h with ρ = 1000 kg m⁻³, g = 9.81 N kg⁻¹, ∆h = 25 m, giving 245250 Pa - 1 mark.',
       'Answer: the total 3.4525 × 10⁵ Pa, which is 3.5 × 10⁵ Pa to two significant figures, with the unit; the atmospheric pressure must be added, and giving 2.5 × 10⁵ Pa alone omits it - 1 mark.'],
      'Calculate', 'CALC', ['AO2'], 'Apply', 2, 2)

flash('ITEM-9702-4-028-CALC', 28, 'OBJ-9702-4.3-04', ['CLM-9702-4-033', 'CLM-9702-4-034'],
      'A diver descends in a lake in the Okavango panhandle from a depth of 5.0 m to a depth of 12 m. The density of the lake water is 1000 kg m⁻³ and g = 9.81 N kg⁻¹. Calculate the increase in the pressure on the diver.',
      'The increase is the difference of pressure between the two depths: ∆p = ρg∆h, with ∆h = 12 − 5.0 = 7.0 m. First ρg = 1000 × 9.81 = 9810 Pa m⁻¹, then ∆p = 9810 × 7.0 = 68670 Pa. The pressure increases by 6.9 × 10⁴ Pa to two significant figures.',
      ['Equation and substitution: ∆p = ρg∆h with ∆h = 12 − 5.0 = 7.0 m, the vertical difference of the two depths - 1 mark.',
       'Answer: 68670 Pa, which is 6.9 × 10⁴ Pa to two significant figures, with the unit - 1 mark. Using 12 m as ∆h gives 1.2 × 10⁵ Pa, a single depth where a difference is needed.'],
      'Calculate', 'CALC', ['AO2'], 'Apply', 2, 2)

flash('ITEM-9702-4-029-CALC', 29, 'OBJ-9702-4.3-04', ['CLM-9702-4-033', 'CLM-9702-4-035'],
      'A sealed tank on a farm near Mariental is filled to the top with fuel of density 800 kg m⁻³. The pressure on the bottom of the tank is 2.3 × 10⁵ Pa above the pressure at the top. The top is vented so the fuel\'s surface is at atmospheric pressure. g = 9.81 N kg⁻¹. Calculate the depth of the fuel.',
      'Rearranging ∆p = ρg∆h for the depth: ∆h = ∆p ÷ (ρg). Substitution: ∆h = (2.3 × 10⁵) ÷ (800 × 9.81) = 230000 ÷ 7848 = 29.3 m. The depth of fuel is 29 m to two significant figures.',
      ['Equation and substitution: ∆h = ∆p ÷ (ρg), with ∆p = 2.3 × 10⁵ Pa, ρ = 800 kg m⁻³ and g = 9.81 N kg⁻¹ - 1 mark.',
       'Answer: 29.3 m, which is 29 m to two significant figures, with the unit - 1 mark. Multiplying ρg by a guessed depth instead of dividing inverts the ratio.'],
      'Calculate', 'CALC', ['AO2'], 'Apply', 2, 2)

flash('ITEM-9702-4-044-MISCON', 44, 'OBJ-9702-4.3-04', ['CLM-9702-4-026', 'CLM-9702-4-033'],
      'A learner working out the extra force on a submerged plate writes: "The pressure at 3.0 m is ρg∆h = 1000 × 9.81 × 3.0 = 29430 N." Explain the two errors in this line.',
      'The first error is confusing pressure with force: ρg∆h gives a pressure in pascals, not a force in newtons; 29430 N is the wrong unit for what was computed. The second error is using a single pressure where the change in pressure is needed: ∆p = ρg∆h gives the difference between two depths, 3.0 m apart here, and it is that difference which acts as the extra pressure, to be multiplied by the plate\'s area if a force is wanted.',
      ['1 mark: the two errors named - the value is a pressure in Pa, not a force in N, and ∆p = ρg∆h gives the change in pressure between two depths, not a single pressure; the second error is calling a difference a single value, and the area must be brought in to reach a force.'],
      'Explain', 'MISCON', ['AO1'], 'Understand', 1, 3,
      misconception_entry='MC-9702-4-09')

flash('ITEM-9702-4-051-FEATURE', 51, 'OBJ-9702-4.3-04', ['CLM-9702-4-033', 'CLM-9702-4-034'],
      'State two features of how ∆p = ρg∆h is used.',
      'Two features: it is used with a single liquid of density ρ, giving the pressure difference between two depths in that liquid; and for a fixed liquid the pressure difference grows in direct proportion to the vertical depth difference, so doubling ∆h doubles ∆p.',
      ['1 mark per feature: any two correct features, such as the single-liquid requirement, the direct proportion to ∆h, or the vertical measurement of ∆h.'],
      'State', 'FEATURE', ['AO1'], 'Remember', 1, 3)

# ---------------------------------------------------------------------------
# OBJ-9702-4.3-05  upthrust from pressure difference
# ---------------------------------------------------------------------------
flash('ITEM-9702-4-030-DEF', 30, 'OBJ-9702-4.3-05', ['CLM-9702-4-036', 'CLM-9702-4-038'],
      'State what is meant by the upthrust on an object in a fluid, and where it comes from.',
      'The upthrust is the resultant upward force on an object in a fluid, and it arises from a difference in hydrostatic pressure: the pressure at the object\'s lower face, which sits deeper, exceeds the pressure at its upper face, so the fluid pushes up harder than it pushes down. Upthrust is a force in newtons; pressure is force per unit area in pascals, and the two are not the same quantity.',
      ['1 mark: the definition as a resultant upward force caused by the pressure difference between the lower and upper faces, with the unit distinction from pressure named.'],
      'State', 'DEF', ['AO1'], 'Remember', 1, 2)

flash('ITEM-9702-4-031-MECH', 31, 'OBJ-9702-4.3-05', ['CLM-9702-4-036', 'CLM-9702-4-037'],
      'A rectangular block is held fully underwater, its top face 2.0 m below the surface and its bottom face 2.5 m below. Explain how the difference in hydrostatic pressure on its two faces gives rise to an upward force on the block.',
      'Pressure in water increases with depth, so because the block\'s bottom face sits 0.5 m deeper than its top face, the pressure on the bottom face exceeds the pressure on the top face. Force is pressure times area, and the two faces have the same area, so the upward push on the bottom face is larger than the downward push on the top face. The difference between the two is a resultant upward force: the upthrust, which acts on the block however deep it sits, because the two pressures grow together and their difference stays fixed.',
      ['How the pressure difference arises: the bottom face is deeper, so its pressure exceeds the top face\'s - 1 mark.',
       'How that becomes a force: pressure times area on equal areas gives a larger upward push, so the resultant is the upthrust - 1 mark.'],
      'Explain', 'MECH', ['AO2'], 'Understand', 2, 2)

flash('ITEM-9702-4-052-FEATURE', 52, 'OBJ-9702-4.3-05', ['CLM-9702-4-036', 'CLM-9702-4-038'],
      'State two features of the upthrust on an object in a fluid.',
      'Two features: it is caused by a difference in hydrostatic pressure between the object\'s lower and upper faces; and it is a force measured in newtons, unlike pressure, which is force per unit area measured in pascals.',
      ['1 mark per feature: any two correct features, such as the pressure-difference cause, the upward direction, or the unit distinction from pressure.'],
      'State', 'FEATURE', ['AO1'], 'Remember', 1, 3)

# ---------------------------------------------------------------------------
# OBJ-9702-4.3-06  F = ρgV
# ---------------------------------------------------------------------------
flash('ITEM-9702-4-032-DEF', 32, 'OBJ-9702-4.3-06', ['CLM-9702-4-039', 'CLM-9702-4-040'],
      'State Archimedes\' principle, including the equation for the upthrust.',
      'Archimedes\' principle states that the upthrust on an object in a fluid is equal to the weight of the fluid the object displaces. The upthrust is F = ρgV, where ρ is the density of the fluid in kg m⁻³, g is the acceleration of free fall, and V is the volume of fluid displaced in m³.',
      ['1 mark: the principle as the weight of displaced fluid, with the equation F = ρgV and each symbol\'s meaning named.'],
      'State', 'DEF', ['AO1'], 'Remember', 1, 2)

flash('ITEM-9702-4-033-CALC', 33, 'OBJ-9702-4.3-06', ['CLM-9702-4-039', 'CLM-9702-4-042'],
      'A stone of volume 1.2 × 10⁻⁴ m³ hangs fully submerged in a bucket of water. The density of water is 1000 kg m⁻³ and g = 9.81 N kg⁻¹. Calculate the upthrust on the stone.',
      'Fully submerged, the stone displaces its own volume of water: V = 1.2 × 10⁻⁴ m³. F = ρgV, where ρ is the density of the fluid - the water, not the stone. Substitution: F = 1000 × 9.81 × 1.2 × 10⁻⁴ = 1.1772 N. The upthrust is 1.2 N to two significant figures.',
      ['Equation and substitution: F = ρgV with ρ = 1000 kg m⁻³, the fluid\'s density, and V = 1.2 × 10⁻⁴ m³, the displaced volume - 1 mark (the first step).',
       'Answer: 1.1772 N, which is 1.2 N to two significant figures, with the unit - 1 mark. The stone\'s own density or weight does not enter the upthrust.'],
      'Calculate', 'CALC', ['AO2'], 'Apply', 2, 2)

flash('ITEM-9702-4-034-CALC', 34, 'OBJ-9702-4.3-06', ['CLM-9702-4-039', 'CLM-9702-4-041'],
      'A raft floats on a river near Katima Mulino, with 0.85 m³ of its hull below the waterline. The density of the river water is 1000 kg m⁻³ and g = 9.81 N kg⁻¹. Calculate the weight of the raft and its load.',
      'The raft floats in equilibrium, so the upthrust balances the total weight. The submerged hull displaces V = 0.85 m³ of water, so the upthrust is F = ρgV. First ρg = 1000 × 9.81 = 9810 N m⁻³, then F = 9810 × 0.85 = 8338.5 N. The weight of the raft and its load equals the upthrust: 8338.5 N, which is 8.3 × 10³ N to two significant figures.',
      ['Equation and substitution: F = ρgV with ρ = 1000 kg m⁻³ and V = 0.85 m³ displaced, giving 8338.5 N - 1 mark.',
       'Answer: because it floats in equilibrium the weight equals the upthrust, 8.3 × 10³ N to two significant figures, with the unit - 1 mark.'],
      'Calculate', 'CALC', ['AO2'], 'Apply', 2, 2)

flash('ITEM-9702-4-035-CALC', 35, 'OBJ-9702-4.3-06', ['CLM-9702-4-039', 'CLM-9702-4-040'],
      'A sample of a plastic has a mass of 21.0 g and floats in water with three quarters of its volume submerged. The density of water is 1000 kg m⁻³ and g = 9.81 N kg⁻¹. Calculate the volume of the sample.',
      'Floating in equilibrium, the upthrust equals the sample\'s weight. Weight: W = mg = 0.0210 kg × 9.81 N kg⁻¹ = 0.20601 N. This equals the upthrust on the displaced volume: 1000 × V(displaced) × 9.81 = 0.20601 N. First 0.20601 ÷ 9.81 = 0.021 kg, then V(displaced) = 0.021 ÷ 1000 = 0.000021 m³, which is 2.1 × 10⁻⁵ m³. The displaced volume is three quarters of the sample\'s volume, so the sample\'s volume is 0.000021 ÷ 0.75 = 0.000028 m³. The volume of the sample is 2.8 × 10⁻⁵ m³ to two significant figures.',
      ['Equation: the weight equals the upthrust on the displaced volume, W = mg = 0.20601 N, so 1000 × 9.81 × V(displaced) = 0.20601 N - 1 mark.',
       'Answer: V(displaced) = 2.100 × 10⁻⁵ m³, then the sample\'s volume = 2.800 × 10⁻⁵ m³, which is 2.8 × 10⁻⁵ m³ to two significant figures, with the unit - 1 mark. Taking the displaced volume as the whole volume omits the three quarters.'],
      'Calculate', 'CALC', ['AO2'], 'Apply', 2, 2)

flash('ITEM-9702-4-043-MISCON', 43, 'OBJ-9702-4.3-06', ['CLM-9702-4-039', 'CLM-9702-4-042'],
      'A learner calculating the reading on a spring balance holding a 5.0 N block submerged in water writes: "The upthrust is 5.0 N, the block\'s weight, and the balance reads 10 N because the upthrust adds to the weight." Explain the errors.',
      'Both statements are errors. The upthrust is the weight of the fluid displaced, F = ρgV, with the fluid\'s density and the displaced volume; the block\'s weight of 5.0 N is not the upthrust unless the block happens to displace exactly its own weight of fluid, which is not given. And the upthrust acts upwards, against the weight, so it takes away from the downward pull on the balance rather than adding to it: the balance reads the weight minus the upthrust, a value smaller than 5.0 N, not 10 N.',
      ['1 mark: the two errors named - the upthrust is ρ(fluid)gV(displaced), not the object\'s weight, and it acts upwards against the weight, so the reading is reduced, not doubled; adding the upthrust to the weight is the second error, and the correct reading is less than 5.0 N.'],
      'Explain', 'MISCON', ['AO1'], 'Understand', 1, 3,
      misconception_entry='MC-9702-4-08')

flash('ITEM-9702-4-053-FEATURE', 53, 'OBJ-9702-4.3-06', ['CLM-9702-4-039', 'CLM-9702-4-041'],
      'State two features of the upthrust calculated from F = ρgV.',
      'Two features: ρ is the density of the fluid and V is the volume of fluid displaced, so the object\'s own density and weight do not enter the upthrust; and a floating object displaces a volume of fluid whose weight equals the object\'s own weight, so the upthrust on it balances its weight.',
      ['1 mark per feature: any two correct features, such as the fluid\'s density and the displaced volume being the quantities in the equation, or the balance of upthrust and weight for a floating object.'],
      'State', 'FEATURE', ['AO1'], 'Remember', 1, 3)

# ---------------------------------------------------------------------------
# Performance tasks
# ---------------------------------------------------------------------------
P01_CLAIMS = ['CLM-9702-4-001', 'CLM-9702-4-005', 'CLM-9702-4-012', 'CLM-9702-4-014',
              'CLM-9702-4-017', 'CLM-9702-4-023', 'CLM-9702-4-026', 'CLM-9702-4-029',
              'CLM-9702-4-033', 'CLM-9702-4-039']
p01 = {
    'item_id': 'ITEM-9702-4-P01',
    'objective_ids': ['OBJ-9702-4.1-01', 'OBJ-9702-4.1-02', 'OBJ-9702-4.1-04', 'OBJ-9702-4.2-01'],
    'claim_ids': P01_CLAIMS,
    'item_type': 'multiple_choice_set',
    'subtype': None,
    'assessment_objectives': ['AO1', 'AO2'],
    'blooms_level': 'Apply',
    'command_word': None,
    'mark_tariff': 12,
    'difficulty': 3,
    'prompt': (
        'Twelve questions. Choose one option for each.\n\n'
        '1. The centre of gravity of an object is the point at which\n'
        'A  the mass of the object is concentrated\n'
        'B  the whole weight may be taken to act\n'
        'C  the Earth\'s pull is strongest\n'
        'D  the object balances on any edge\n\n'
        '2. The unit of the moment of a force is\n'
        'A  N\n'
        'B  N m\n'
        'C  N m⁻¹\n'
        'D  J\n\n'
        '3. A force of 20 N acts at right angles to a door, 0.75 m from the hinge. The moment about the hinge is\n'
        'A  26.7 N m\n'
        'B  20 N m\n'
        'C  15 N m\n'
        'D  27 N\n\n'
        '4. Which pair of forces forms a couple?\n'
        'A  Two equal forces along the same line, pointing the same way\n'
        'B  Two unequal parallel forces, opposite in direction\n'
        'C  Two equal perpendicular forces\n'
        'D  Two equal parallel forces, opposite in direction, not along the same line\n\n'
        '5. Two forces of 6.0 N each are applied tangentially to opposite edges of a steering wheel of diameter 0.36 m. The torque is\n'
        'A  1.08 N m\n'
        'B  2.16 N m\n'
        'C  4.32 N m\n'
        'D  6.0 N m\n\n'
        '6. The principle of moments applies to a body\n'
        'A  at rest\n'
        'B  moving at constant velocity\n'
        'C  in equilibrium\n'
        'D  with zero weight\n\n'
        '7. A uniform beam of weight 120 N is pivoted at its centre. A 40 N weight hangs 0.90 m left of the pivot. The beam balances when a 60 N weight hangs\n'
        'A  0.60 m right of the pivot\n'
        'B  1.35 m right of the pivot\n'
        'C  0.90 m right of the pivot\n'
        'D  0.30 m right of the pivot\n\n'
        '8. A system is in equilibrium when\n'
        'A  it is at rest\n'
        'B  the resultant force is zero\n'
        'C  the resultant torque is zero\n'
        'D  both the resultant force and the resultant torque are zero\n\n'
        '9. Three coplanar forces in equilibrium are drawn head to tail. The triangle formed is\n'
        'A  open, with the gap equal to the resultant\n'
        'B  closed, with one side the resultant\n'
        'C  closed, with no resultant\n'
        'D  right-angled whenever the three forces are equal in size\n\n'
        '10. A block of mass 0.60 kg occupies 2.4 × 10⁻⁴ m³. Its density is\n'
        'A  2500 kg m⁻³\n'
        'B  1.4 × 10⁻⁴ kg m⁻³\n'
        'C  250 kg m⁻³\n'
        'D  4.0 × 10⁻³ kg m⁻³\n\n'
        '11. The pressure difference between the top and the bottom of a tank of water 3.0 m deep is (ρ = 1000 kg m⁻³, g = 9.81 N kg⁻¹)\n'
        'A  3.3 × 10⁻⁵ Pa\n'
        'B  2.9 × 10⁴ Pa\n'
        'C  3.0 × 10³ Pa\n'
        'D  9.81 Pa\n\n'
        '12. An object displaces 5.0 × 10⁻⁵ m³ of water (ρ = 1000 kg m⁻³, g = 9.81 N kg⁻¹). The upthrust on it is\n'
        'A  0.049 N\n'
        'B  0.49 N\n'
        'C  4.9 × 10⁻⁴ N\n'
        'D  5.0 N'
    ),
    'canonical_answer': (
        'Key: 1 B, 2 B, 3 C, 4 D, 5 B, 6 C, 7 A, 8 D, 9 C, 10 A, 11 B, 12 B.\n'
        '1. B: the weight may be taken to act at the centre of gravity. A and C define it through mass or the pull of gravity, the registered error; D describes a balance test, not the definition.\n'
        '2. B: moment = force × distance, N × m = N m. A drops the distance; C divides instead of multiplying; J is the unit of work, a different quantity.\n'
        '3. C: moment = 20 × 0.75 = 15 N m. A inverts the product; B uses 1 m as the distance; D carries the unit of force, not moment.\n'
        '4. D: a couple is two equal, opposite, parallel forces whose lines of action do not coincide. A gives no turning effect; B is unequal forces, which leave a resultant; C is neither parallel nor opposite.\n'
        '5. B: torque = one force × the distance between the lines of action = 6.0 × 0.36 = 2.16 N m. A uses the radius instead of the diameter, half the torque; C adds the two forces first, the resultant-force error; D states a force, not a torque.\n'
        '6. C: the principle is stated for a body in equilibrium. A confuses rest with equilibrium, the registered error; B misses the turning condition; D is irrelevant to moments.\n'
        '7. A: clockwise 40 × 0.90 = 36 N m must equal 60 × d, so d = 36 ÷ 60 = 0.60 m. B divides the wrong way; C assumes the distances must match, ignoring the weights; D uses the difference of the weights as a force.\n'
        '8. D: equilibrium needs both zero resultants. A is the rest-means-equilibrium error; B and C each give one condition alone.\n'
        '9. C: the triangle closes, so the forces add to zero and there is no resultant. A describes a non-equilibrium set; B labels a side as the resultant, the registered error; D is false: equal forces can meet at 60°, since the angles come from the situation.\n'
        '10. A: ρ = 0.60 ÷ 2.4 × 10⁻⁴ = 2500 kg m⁻³. B inverts the ratio, 2.4 × 10⁻⁴ ÷ 0.60 = 4.0 × 10⁻⁴; C misplaces the power of ten; D has no route from the data.\n'
        '11. B: ρg = 1000 × 9.81 = 9810 Pa m⁻¹, and ∆p = 9810 × 3.0 = 29430 Pa = 2.9 × 10⁴ Pa. A inverts the product; C drops g; D reports g itself as a pressure.\n'
        '12. B: ρg = 1000 × 9.81 = 9810 N m⁻³, and F = 9810 × 5.0 × 10⁻⁵ = 0.49 N. A misses a power of ten; C multiplies by the wrong power of ten; D gives a weight, not an upthrust from these data.'
    ),
    'marking_guidance': [
        'The key: one mark per correct option, twelve marks in all.',
        'Every distractor is a named error from the misconception register: the centre of gravity defined through mass or gravity, the distance not perpendicular, a couple treated as a resultant force, rest mistaken for equilibrium, a side of the closed triangle labelled the resultant, a single pressure where a difference is needed, the object\'s weight in place of the upthrust.'
    ],
}
_stamp(p01, P01_CLAIMS)
items.append(p01)

P02_CLAIMS = ['CLM-9702-4-001', 'CLM-9702-4-005', 'CLM-9702-4-014', 'CLM-9702-4-016',
              'CLM-9702-4-017', 'CLM-9702-4-026', 'CLM-9702-4-033', 'CLM-9702-4-039']
p02 = {
    'item_id': 'ITEM-9702-4-P02',
    'objective_ids': ['OBJ-9702-4.2-01', 'OBJ-9702-4.2-02', 'OBJ-9702-4.3-04', 'OBJ-9702-4.3-06'],
    'claim_ids': P02_CLAIMS,
    'item_type': 'short_answer',
    'subtype': None,
    'assessment_objectives': ['AO1', 'AO2'],
    'blooms_level': 'Apply',
    'command_word': 'Calculate',
    'mark_tariff': 8,
    'difficulty': 3,
    'prompt': (
        'A mobile water tank on a farm outside Otjiwarongo stands on a rectangular steel skid. The tank and its water have a total weight of 4800 N, and their combined centre of gravity is directly above the mid-point of the skid. The skid is 2.4 m long and rests on two supports, one under each end, A and B. A rope is tied to the skid at B to stop it sliding.\n'
        '(a) Define the centre of gravity of an object. [1]\n'
        '(b) The supports are at the ends of the skid, 2.4 m apart, and the centre of gravity is midway. State the force from each support on the skid. [1]\n'
        '(c) The skid is instead parked with support A at one end and a stone under a point 1.8 m from A, the skid overhanging the stone by 0.60 m. The centre of gravity is still midway along the skid, 1.2 m from A. Calculate the force from the stone on the skid. [2]\n'
        '(d) State the two conditions for the skid and tank to be in equilibrium. [1]\n'
        '(e) The tank is 1.6 m tall and full of water. The density of water is 1000 kg m⁻³ and g = 9.81 N kg⁻¹. Calculate the pressure difference between the top and the bottom of the water. [2]\n'
        '(f) The tank\'s outlet is a hole of area 3.0 × 10⁻⁴ m² closed by a plug. Calculate the extra force pushing on the plug when the tank is full, relative to empty. [1]'
    ),
    'canonical_answer': (
        '(a) The centre of gravity is the single point at which the whole weight of an object may be taken to act.\n'
        '(b) The weight acts midway, 1.2 m from each support, so by symmetry each support carries half: 4800 ÷ 2 = 2400 N, an upward force of 2400 N from each support.\n'
        '(c) Take moments about A, which removes the support force at A from the equation. The weight gives a clockwise moment of 4800 N × 1.2 m = 5760 N m. The stone\'s force S acts upward at 1.8 m from A, giving an anticlockwise moment of S × 1.8 m. Balance: S × 1.8 = 5760, so S = 5760 ÷ 1.8 = 3200 N. The stone pushes up with 3200 N, which is 3200 N to two significant figures.\n'
        '(d) The resultant force on the system is zero and the resultant torque on it is zero.\n'
        '(e) ρg = 1000 × 9.81 = 9810 Pa m⁻¹, and ∆p = ρg∆h = 9810 × 1.6 = 15696 Pa, which is 1.6 × 10⁴ Pa to two significant figures.\n'
        '(f) The pressure difference acts on the plug\'s area: F = ∆p × A = 15696 × 3.0 × 10⁻⁴ = 4.7088 N, which is 4.7 N to two significant figures.'
    ),
    'marking_guidance': [
        'Part (a): 1 mark for the definition as the point where the whole weight may be taken to act.',
        'Part (b): 1 mark for 2400 N from each support, by symmetry, with the unit.',
        'Part (c): 2 marks - moments about A with the weight 4800 × 1.2 = 5760 N m, 1 mark; the balance S = 5760 ÷ 1.8 = 3200 N with its unit, 1 mark.',
        'Part (d): 1 mark for both conditions: zero resultant force and zero resultant torque.',
        'Part (e): 2 marks - the equation ∆p = ρg∆h with ∆h = 1.6 m, 1 mark; the answer 15696 Pa = 1.6 × 10⁴ Pa with its unit, 1 mark.',
        'Part (f): 1 mark for the extra force from the pressure difference times the area, 4.7 N with its unit. The reason: the full tank\'s pressure difference acts across the plug, and force is pressure times area.'
    ],
}
_stamp(p02, P02_CLAIMS)
items.append(p02)

P03_CLAIMS = ['CLM-9702-4-023', 'CLM-9702-4-026', 'CLM-9702-4-029', 'CLM-9702-4-033',
              'CLM-9702-4-039', 'CLM-9702-4-041']
p03 = {
    'item_id': 'ITEM-9702-4-P03',
    'objective_ids': ['OBJ-9702-4.3-01', 'OBJ-9702-4.3-04', 'OBJ-9702-4.3-06'],
    'claim_ids': P03_CLAIMS,
    'item_type': 'calculation',
    'subtype': None,
    'assessment_objectives': ['AO1', 'AO2'],
    'blooms_level': 'Apply',
    'command_word': 'Calculate',
    'mark_tariff': 5,
    'difficulty': 3,
    'prompt': (
        'A cattle-trough in the Otjozondjupa region is a rectangular tank, open at the top, with a base of area 1.5 m². It is filled to a depth of 0.45 m with water. A hollow steel ball of volume 8.0 × 10⁻³ m³ is pushed underwater and held just below the surface by a rope. '
        'The density of water is 1000 kg m⁻³ and g = 9.81 N kg⁻¹. '
        '(a) Calculate the mass of the water in the trough. '
        '(b) Calculate the pressure difference between the surface and the base of the trough. '
        '(c) Calculate the upthrust on the steel ball. '
        '(d) The rope is cut and the ball floats with two thirds of its volume submerged. Calculate the weight of the ball.'
    ),
    'canonical_answer': (
        '(a) The volume of water: V = 1.5 m² × 0.45 m = 0.675 m³. Mass: m = ρV = 1000 × 0.675 = 675 kg, which is 675 kg to three significant figures.\n'
        '(b) ρg = 1000 × 9.81 = 9810 Pa m⁻¹, and ∆p = ρg∆h = 9810 × 0.45 = 4414.5 Pa, which is 4.4 × 10³ Pa to two significant figures.\n'
        '(c) Fully submerged, the ball displaces its own volume: F = ρgV. With ρg = 9810 N m⁻³, F = 9810 × 8.0 × 10⁻³ = 78.48 N, which is 78 N to two significant figures.\n'
        '(d) Floating in equilibrium, the upthrust equals the ball\'s weight. The displaced volume is two thirds of 8.0 × 10⁻³ m³, which is 5.333 × 10⁻³ m³. Weight: W = 9810 × 5.333 × 10⁻³ = 52.32 N, which is 52 N to two significant figures. Each answer is rounded once, at the end, and given to two or three significant figures, the precision of the data.'
    ),
    'marking_guidance': [
        'Equation: the volume from area × depth, then m = ρV for the mass - 1 mark.',
        'Substitution and working: 1.5 × 0.45 = 0.675 m³ then 1000 × 0.675 = 675 kg - 1 mark.',
        'The pressure difference: ∆p = ρg∆h = 1000 × 9.81 × 0.45 = 4414.5 Pa = 4.4 × 10³ Pa with its unit - 1 mark.',
        'The upthrust: F = ρgV with the ball fully submerged, 1000 × 9.81 × 8.0 × 10⁻³ = 78.48 N = 78 N with its unit - 1 mark.',
        'Answer: the floating weight from two thirds of the volume displaced, 52.32 N = 52 N with its unit, stated to two significant figures, justified by the precision of the data - 1 mark.'
    ],
}
_stamp(p03, P03_CLAIMS)
items.append(p03)

# ---------------------------------------------------------------------------
dataset = {
    'dataset_id': 'ITEMS-9702-4',
    'topic_id': '4',
    'items': items,
}
out = os.path.join(WS, 'topics/4/learning-items/topic_4_items.json')
os.makedirs(os.path.dirname(out), exist_ok=True)
with open(out, 'w') as fh:
    json.dump(dataset, fh, indent=1, ensure_ascii=False)
print('wrote', len(items), 'items to', out)
