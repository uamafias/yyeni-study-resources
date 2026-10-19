#!/usr/bin/env python3
"""Write the 6116 Biology structural exemplar: two slices that pass the full check suite.

The content below is authored (original wording, Namibian contexts, nothing taken from any
paper, mark scheme or examiner report). Everything else is looked up: each item takes its
item_id, subtype, AOs, Bloom level, command word, tariff and difficulty from the live work order
slot for its objective and subtype, so a rebuilt work order cannot leave the exemplar stale;
authored_hash uses the checks' own _artefact_text; claims_seen records each cited claim's
revision; each content unit's word_budget is read from curriculum/notes-budget.json.

    python3 work/nam-6116-nssco-2026/planning/make_exemplar.py [<out-dir>]

Slices:
  topic 3  the whole of 3.3.2 Osmosis and 3.3.3 Active transport, written at the revised notes
           budget: every slot of those ten objectives (20 cards, two of them MISCON) plus a
           multiple-choice set, a structured question and an Alternative-to-Practical task.
           This is the representative learner-facing section.
  topic 4  4.4.2 monohybrid inheritance, two objectives: DEF, MISCON, CALC, INTERP and a
           structured question.
"""
import hashlib, json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
WS = os.path.dirname(HERE)
ROOT = os.path.dirname(os.path.dirname(WS))
sys.path.insert(0, os.path.join(ROOT, 'standard', 'v0.2.0-draft', 'checks'))
from yyeni_checks import _artefact_text  # noqa: E402

OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.join(WS, 'exemplar')
CTX = {'sector': None, 'business_size': None, 'ownership': None, 'situation': None, 'facts': []}
VER = {'status': 'unverified',
       'method': ('Authored for the 6116 structural exemplar under standard v0.2.0-draft. '
                  'Requires semantic review (RS-28).'),
       'reviewer_id': None, 'reviewed_at': None, 'confidence': 0.9}
PROV = 'Authored for the 6116 structural exemplar from the topic %s claim ledger.'
BUDGET = json.load(open(os.path.join(WS, 'curriculum', 'notes-budget.json')))['units']
WO = {t: json.load(open(os.path.join(WS, 'topics', t, 'work_order.json'))) for t in ('3', '4')}


def stamp(x):
    x['authored_hash'] = hashlib.sha256(_artefact_text(x).encode()).hexdigest()
    return x


def claim(t, n, objs, text, ctype, prov='generated_gap'):
    return {'claim_id': 'CLM-6116-%s-%03d' % (t, n), 'objective_ids': ['OBJ-6116-' + o for o in objs],
            'text': text, 'claim_type': ctype, 'provenance': prov, 'evidence': [],
            'derived_from_claim_ids': [], 'revision': 1, 'verification': dict(VER),
            'publishable': False, 'notes': []}


def C(t, *ns):
    return ['CLM-6116-%s-%03d' % (t, n) for n in ns]


def block(bid, btype, heading, text, cids, ao):
    return stamp({'block_id': bid, 'block_type': btype, 'heading': heading, 'text': text,
                  'claim_ids': cids, 'context_tags': [], 'assessment_objectives': ao,
                  'claims_seen': {c: 1 for c in cids}})


def slot(t, obj, sub):
    hits = [s for s in WO[t]['item_slots'] if s['objective_id'] == 'OBJ-6116-' + obj and s['subtype'] == sub]
    if len(hits) != 1:
        raise SystemExit('topic %s: %d slots for %s %s' % (t, len(hits), obj, sub))
    return hits[0]


def card(t, obj, sub, cids, prompt, answer, guide):
    s = slot(t, obj, sub)
    i = {'item_id': s['slot'], 'objective_ids': [s['objective_id']], 'claim_ids': cids,
         'item_type': 'flashcard', 'subtype': sub, 'assessment_objectives': s['assessment_objectives'],
         'blooms_level': s['blooms_level'], 'command_word': s['command_word'],
         'mark_tariff': s['mark_tariff'], 'difficulty': s['difficulty'], 'prompt': prompt,
         'canonical_answer': answer, 'marking_guidance': guide, 'context': dict(CTX),
         'prerequisite_item_ids': [], 'core_status': 'core', 'intentional_duplicate_group': None,
         'provenance': PROV % t, 'qa_status': 'review_required', 'claims_seen': {c: 1 for c in cids}}
    if s.get('misconception_entry'):
        i['misconception_entry'] = s['misconception_entry']
    return stamp(i)


def task(t, kind, objs, cids, ao, cw, tariff, diff, prompt, answer, guide):
    p = [x for x in WO[t]['performance_tasks'] if x['item_type'] == kind][0]
    return stamp({'item_id': p['slot'], 'objective_ids': ['OBJ-6116-' + o for o in objs], 'claim_ids': cids,
                  'item_type': kind, 'subtype': None, 'assessment_objectives': ao,
                  'blooms_level': p['blooms_level'], 'command_word': cw, 'mark_tariff': tariff,
                  'difficulty': diff, 'prompt': prompt, 'canonical_answer': answer,
                  'marking_guidance': guide, 'context': dict(CTX), 'prerequisite_item_ids': [],
                  'core_status': 'core', 'intentional_duplicate_group': None, 'provenance': PROV % t,
                  'qa_status': 'review_required', 'claims_seen': {c: 1 for c in cids}})


def unit(uid, title, objs, otype, tier, blocks):
    reg = {o['objective_id']: o['syllabus_text'] for o in
           json.load(open(os.path.join(WS, 'curriculum', 'objective_registry.json')))['objectives']}
    texts = [reg['OBJ-6116-' + o] for o in objs]
    words = sum(len(b['text'].split()) + len(b['heading'].split()) for b in blocks)
    b = dict(BUDGET[uid])
    whole = [x for x in WO[uid.split('-')[2].split('.')[0]]['content_units'] if x['unit_id'] == uid][0]
    share = len(objs) / len(whole['objective_ids'])
    note = 'Word budget from curriculum/notes-budget.json (per syllabus bullet).'
    if share < 1:
        # a partial slice is budgeted by the same model as a whole unit, on its own objectives
        sys.path.insert(0, HERE)
        from notes_budget import budget_for
        lo, hi = budget_for(texts)
        b = {'min': lo, 'max': hi}
        note += (' This slice covers %d of the unit\'s %d objectives, so its budget is the same model applied '
                 'to those objectives alone.' % (len(objs), len(whole['objective_ids'])))
    return {'unit_id': uid, 'title': title, 'objective_ids': ['OBJ-6116-' + o for o in objs],
            'level': 'NSSCO Ordinary Level', 'core_status': 'core', 'objective_type': otype,
            'depth_tier': tier, 'word_budget': {'min': b['min'], 'target': (b['min'] + b['max']) // 2,
                                                'max': b['max']},
            'blocks': blocks, 'word_count': words, 'qa_status': 'review_required',
            'notes': [note]}


def write(path, data):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w') as fh:
        json.dump(data, fh, indent=1, ensure_ascii=False)
        fh.write('\n')


# ============================================================ topic 3: 3.3.2 and 3.3.3 in full
c3 = [
 claim('3', 1, ['3.3.3-01'], 'Active transport is the movement of particles through a cell membrane from a region of '
       'lower concentration to a region of higher concentration using energy from respiration.',
       'definition', 'syllabus_direct'),
 claim('3', 2, ['3.3.2-01'], 'Osmosis is the net movement of water molecules from a dilute solution to a more '
       'concentrated solution through a partially permeable membrane.', 'definition'),
 claim('3', 3, ['3.3.2-01'], 'A plant cell in a hypotonic solution, one more dilute than its cell sap, takes in water '
       'by osmosis; the vacuole swells and the cytoplasm presses against the cell wall, so the cell becomes turgid. '
       'The strong cell wall stops it bursting.', 'causal'),
 claim('3', 4, ['3.3.2-01'], 'A plant cell in a hypertonic solution, one more concentrated than its cell sap, loses '
       'water by osmosis and becomes flaccid; if water loss continues, the cell membrane, with the cytoplasm inside '
       'it, pulls away from the cell wall and the cell is plasmolysed.', 'causal'),
 claim('3', 5, ['3.3.2-01', '3.3.2-02'], 'In an isotonic solution, one with the same concentration as the cell '
       'contents, there is no net movement of water, so the cell neither swells nor shrinks.', 'factual'),
 claim('3', 6, ['3.3.2-01'], 'Turgid, flaccid and plasmolysed describe the state of a cell; hypertonic, isotonic and '
       'hypotonic describe a solution compared with the cell contents.', 'misconception_correction'),
 claim('3', 7, ['3.3.3-01'], 'Only movement against a concentration gradient, active transport, needs energy from '
       'respiration; diffusion and osmosis move particles down a gradient and need none.',
       'misconception_correction'),
 claim('3', 8, ['3.3.2-04'], 'To investigate osmosis in potato, cut cylinders of equal size, blot and weigh each, place '
       'one in each of a range of sucrose solutions for the same time at the same temperature, then blot and '
       'reweigh; the percentage change in mass shows whether each cylinder gained or lost water.', 'procedural'),
 claim('3', 9, ['3.3.2-04'], 'The sucrose concentration at which a cylinder would neither gain nor lose mass matches '
       'the concentration of the cell contents; it lies between the last solution that caused a gain and the first '
       'that caused a loss.', 'inference'),
 claim('3', 10, ['3.3.2-04', '3.3.2-03'], 'Blotting every piece of tissue in the same way before weighing removes '
       'surface solution, which would otherwise add mass the cells did not take up; repeating each concentration '
       'and averaging reduces the effect of one unusual piece; and the tissue needs enough time in the solution '
       'for water to move.', 'procedural'),
 claim('3', 11, ['3.3.2-02'], 'An animal cell in a solution more dilute than its cytoplasm takes in water by osmosis '
       'and swells; it has no cell wall, so it can burst.', 'causal'),
 claim('3', 12, ['3.3.2-02'], 'An animal cell in a solution more concentrated than its cytoplasm loses water by '
       'osmosis and shrinks, becoming shrivelled.', 'causal'),
 claim('3', 13, ['3.3.2-03'], 'Onion epidermis mounted in a concentrated salt solution and viewed under a light '
       'microscope after several minutes shows plasmolysed cells, with the cell membrane and cytoplasm pulled away from the cell walls; '
       'epidermis mounted in water shows turgid cells.', 'procedural'),
 claim('3', 14, ['3.3.2-03', '3.3.2-06'], 'Turgor pressure is the pressure of the cell contents pushing outwards on the '
       'cell wall when a plant cell has taken in water; the wall pushes back and stops further expansion.', 'factual'),
 claim('3', 15, ['3.3.2-04'], 'Visking tubing is a partially permeable membrane: a bag of tubing filled with sucrose '
       'solution and placed in water gains water by osmosis, so it swells and gains mass.', 'procedural'),
 claim('3', 16, ['3.3.2-05'], 'Water moves by osmosis from a region of higher water potential to a region of lower '
       'water potential. Water potential depends mainly on how dilute a solution is, and also on pressure; at the '
       'same pressure, a dilute solution has a higher water potential than a concentrated one.', 'factual'),
 claim('3', 17, ['3.3.2-05'], 'Soil water usually has a higher water potential than the cell sap of a root hair cell, '
       'so water enters the root hair by osmosis; it then moves across the root towards the xylem, down a water '
       'potential gradient, travelling through the cells and along the cell walls between them.', 'causal'),
 claim('3', 18, ['3.3.2-05'], 'If the soil water becomes more concentrated than the root cell sap, so that its water '
       'potential is lower, water leaves the root cells by osmosis instead of entering and the plant can wilt; '
       'adding too much fertiliser is one way this can happen.', 'causal'),
 claim('3', 19, ['3.3.2-06'], 'Turgid cells press against their walls and against one another, which makes soft stems '
       'and leaves firm; when the cells lose water and become flaccid, these parts droop.', 'causal'),
 claim('3', 20, ['3.3.3-02'], 'Mineral ions such as nitrate are often more concentrated inside root hair cells than in '
       'the soil water, so root hair cells take them in against the concentration gradient by active transport.',
       'causal'),
 claim('3', 21, ['3.3.3-02'], 'Active transport uses energy from respiration, so root cells need oxygen to take up '
       'ions; in waterlogged soil, which holds little oxygen, ion uptake falls.', 'causal'),
 claim('3', 22, ['3.3.3-03'], 'Epithelial cells of the villi take in glucose by active transport, so glucose can still '
       'be absorbed when its concentration in the gut is lower than in the cells, and little is left to be lost.',
       'causal'),
 claim('3', 23, ['3.3.3-03'], 'Cells lining the kidney tubules reabsorb glucose by active transport, returning it to the '
       'blood so that it is not lost in the urine.', 'causal'),
 claim('3', 24, ['3.3.3-04'], 'In active transport a particle binds to a specific carrier protein in the membrane; the '
       'carrier changes shape and moves the particle across, releasing it on the other side. The energy comes from '
       'respiration, used directly by some carriers and indirectly by others, so active transport stops when '
       'respiration stops.', 'procedural'),
 claim('3', 25, ['3.3.3-04'], 'Cells that carry out a lot of active transport, such as root hair cells and the '
       'epithelial cells of villi, contain many mitochondria, which release the energy it needs.', 'factual'),
 claim('3', 26, ['3.3.3-01'], 'Simple diffusion needs no transport protein. Water can cross the membrane directly and '
       'also through water channel proteins. Active transport needs carrier proteins.', 'comparison'),
 claim('3', 27, ['3.3.2-03'], 'If no plasmolysis is seen, possible reasons include too little time for water to leave '
       'the cells or a solution that is not concentrated enough.', 'inference'),
 claim('3', 29, ['3.3.2-03'], 'The effect of solution concentration on plant cells can be measured by mounting epidermis '
       'in each solution and counting the percentage of cells that are plasmolysed in a field of view after a fixed '
       'time.', 'procedural'),
 claim('3', 28, ['3.3.2-04'], 'In an osmosis investigation with potato, the independent variable is the concentration '
       'of the solution and the dependent variable is the percentage change in mass; the size of the cylinders, the '
       'time, the temperature and the potato used are kept the same, and each concentration is repeated.',
       'procedural'),
]

u332 = unit('CU-6116-3.3.2', 'Osmosis',
            ['3.3.2-01', '3.3.2-02', '3.3.2-03', '3.3.2-04', '3.3.2-05', '3.3.2-06'], 'bio_relationship', 3, [
 block('3.3.2-b0', 'summary', 'Key points',
       '| Learn | |\n|---|---|\n'
       '| Osmosis | net movement of water from a dilute to a more concentrated solution through a partially permeable membrane |\n'
       '| Plant cell, more dilute outside | water in, turgid; the wall stops it bursting |\n'
       '| Plant cell, more concentrated outside | water out, flaccid, then plasmolysed (membrane pulls away from the wall) |\n'
       '| Animal cell | no wall: swells and can burst, or shrinks and shrivels |\n'
       '| Words | turgid, flaccid, plasmolysed describe cells; hypotonic, isotonic, hypertonic describe solutions |\n'
       '| Roots | water enters root hairs by osmosis and moves down a water potential gradient to the xylem |',
       C('3', 2, 3, 4, 6, 11, 12, 17), ['AO1']),
 block('3.3.2-b1', 'learner_objective', 'What this section covers',
       'What osmosis is; what it does to plant and animal cells in solutions of different concentration; how it '
       'lets roots take in water and keeps soft plant parts firm; and three ways to investigate it.', [], ['AO1']),
 block('3.3.2-b2', 'definition', 'Osmosis and water potential',
       'Osmosis is the net movement of water molecules from a dilute solution to a more concentrated solution through '
       'a partially permeable membrane. Net means overall: water molecules cross the membrane in both directions, '
       'but more cross from the dilute side, so water builds up on the concentrated side. The membrane lets water '
       'molecules through but holds back larger solute molecules such as sucrose. Biologists describe the same idea '
       'with water potential: water moves by osmosis from a region of higher water potential to a region of lower '
       'water potential. Water potential depends mainly on how dilute a solution is, and also on pressure. At the '
       'same pressure, a dilute solution has a higher water potential than a concentrated one.', C('3', 2, 16), ['AO1']),
 block('3.3.2-b3', 'plain_explanation', 'Plant cells in a more dilute solution',
       'In a plant cell the cell membrane is the partially permeable membrane and the cell sap in the vacuole is the '
       'solution inside. Put the cell into a hypotonic solution, one more dilute than its cell sap, and water enters '
       'by osmosis. The vacuole swells and pushes the cytoplasm against the cell wall. This outward push is turgor '
       'pressure, and the wall pushes back. The cell becomes turgid but does not burst, because the wall is strong. '
       'In an isotonic solution, with the same concentration as the cell sap, there is no net movement of water and '
       'the cell stays the same size.', C('3', 3, 5, 14), ['AO1']),
 block('3.3.2-b4', 'plain_explanation', 'Plant cells in a more concentrated solution',
       'Put the same cell into a hypertonic solution, one more concentrated than its cell sap, and water leaves by '
       'osmosis. The vacuole shrinks and the cell becomes flaccid, or soft. If water keeps leaving, the cell '
       'membrane, with the cytoplasm inside it, pulls away from the cell wall. The cell is then plasmolysed. The space between wall and membrane fills with '
       'the outside solution, because the wall lets it through.', C('3', 4), ['AO1']),
 block('3.3.2-b5', 'comparison', 'Animal cells have no wall',
       'An animal cell, such as a red blood cell, also gains or loses water by osmosis, but it has no cell wall. In a '
       'solution more dilute than its cytoplasm it takes in water and swells, and with nothing to resist the '
       'swelling it can burst. In a solution more concentrated than its cytoplasm it loses water and shrinks, '
       'becoming shrivelled. In an isotonic solution it keeps its shape. This is why fluids given to patients through '
       'a drip have the same concentration as blood plasma.', C('3', 11, 12, 5), ['AO1']),
 block('3.3.2-b6', 'misconception', 'Cell words and solution words',
       'Two sets of words are easy to mix up. Turgid, flaccid and plasmolysed describe the cell. Hypertonic, '
       'isotonic and hypotonic describe the solution, compared with the cell contents. In an answer about osmosis, '
       'use a solution word for the solution and a cell word for the cell.', C('3', 6), ['AO1']),
 block('3.3.2-b7', 'analysis_chain', 'How roots take in water',
       'Soil water is usually more dilute than the cell sap of a root hair cell, so it usually has a higher water '
       'potential, and water enters the root hair by osmosis. From there water moves across the root towards the '
       'xylem, down a water potential gradient. Some of it travels through the cells and some along the cell walls '
       'between them. The xylem then carries it up the plant. The gradient can be reversed. If the soil water '
       'becomes more concentrated than the root cell sap, its water potential is lower, and water leaves the roots by '
       'osmosis: the plant can wilt even though the soil is wet. Adding too much fertiliser is one way this can '
       'happen.',
       C('3', 16, 17, 18), ['AO2']),
 block('3.3.2-b8', 'process', 'How turgor pressure supports a plant',
       'A young stem of pumpkin or a leaf of spinach has no wood to hold it up. It stays firm because its cells are '
       'turgid: water has entered by osmosis, each vacuole has swollen, and the turgor pressure of each cell pushes '
       'its contents against its wall. Turgid cells press against one another like tightly packed balloons, and the '
       'whole stem or leaf becomes firm. When the plant loses more water than it takes in, the cells become flaccid '
       'and the soft parts droop.', C('3', 14, 19), ['AO1']),
 block('3.3.2-b9', 'practice_guidance', 'Seeing plasmolysis under the microscope',
       'Peel a thin strip of epidermis from the inside of an onion scale leaf. Mount one piece in a drop of water and '
       'another in a drop of concentrated salt solution, add coverslips and leave both for about ten minutes. Under '
       'the microscope the cells in water are turgid, with the cytoplasm pressed against the walls. The cells in '
       'salt solution are plasmolysed: the cell membrane and cytoplasm have pulled away from the walls. Red onion makes this easier to '
       'see, because the coloured cell sap shows the shrinking vacuole. To turn this into an investigation, mount '
       'strips in a range of salt concentrations, wait the same time for each, and count the percentage of cells '
       'plasmolysed in a field of view.', C('3', 13, 29), ['AO3']),
 block('3.3.2-b10', 'process', 'Investigating osmosis with potato cylinders',
       'Plan it first. The independent variable is the concentration of the solution; the dependent variable is the '
       'percentage change in mass; keep the size of the cylinders, the time, the temperature and the potato the '
       'same, and repeat each concentration. Then cut cylinders of potato of the same length and diameter with a '
       'cork borer. Blot each one dry and weigh it. Put one cylinder '
       'into each of a range of sucrose solutions, for example from 0.0 to 0.8 mol/dm³, for the same time and at the '
       'same temperature. Then remove each cylinder, blot it in the same way and weigh it again. A gain in mass means '
       'water entered the cells; a loss means water left.', C('3', 8, 28), ['AO3']),
 block('3.3.2-b11', 'worked_calculation', 'Worked example: percentage change in mass',
       'A potato cylinder weighs 2.00 g at the start and 2.16 g after 30 minutes in '
       '0.1 mol/dm³ sucrose. The change is 2.16 - 2.00 = 0.16 g. As a percentage of the starting mass, '
       '0.16 ÷ 2.00 = 0.08, and 0.08 × 100 = 8, so the cylinder gained 8%. Percentages let you compare cylinders '
       'that started at different masses. If a second cylinder lost mass in 0.3 mol/dm³, the concentration of the '
       'cell contents lies between 0.1 and 0.3 mol/dm³: the solution with no change in mass would match it.',
       C('3', 8, 9), ['AO3']),
 block('3.3.2-b12', 'example', 'A model cell made of Visking tubing',
       'Visking tubing is a partially permeable membrane. Tie one end, fill the tube with sucrose solution, tie the '
       'other end and weigh it. Leave it in a beaker of water. Water enters by osmosis, so the bag swells, becomes '
       'firm and gains mass, much as a plant cell becomes turgid. A bag of water placed in sucrose solution does the '
       'opposite.', C('3', 15), ['AO3']),
 block('3.3.2-b13', 'limitation', 'Making the results trustworthy',
       'Solution left on the surface of a piece of tissue adds mass that the cells did not take up, so blot every '
       'piece in the same way before each weighing. One piece can behave unusually, so repeat each concentration '
       'and work out the mean. Water moves slowly, so give the tissue enough time in each solution, and keep the '
       'time the same for every piece. If an expected change is not seen, think about what else could explain it: '
       'too little time, or a solution that is not concentrated enough.', C('3', 10, 27), ['AO3']),
 block('3.3.2-b14', 'cross_link', 'Where this connects',
       'Osmosis is a special case of diffusion (3.3.1), for water through a partially permeable membrane. Active '
       'transport (3.3.3) moves particles the other way, against a gradient. Water uptake by roots continues in '
       'Transport in plants (3.7), which explains transpiration and wilting. The skills the investigations use, '
       'naming the independent, dependent and controlled variables, setting out a results table and working out a '
       'percentage change, are taught in Scientific processes (1.1 and 1.2).', [], ['AO1']),
])

u333 = unit('CU-6116-3.3.3', 'Active transport', ['3.3.3-01', '3.3.3-02', '3.3.3-03', '3.3.3-04'],
            'bio_evaluation', 3, [
 block('3.3.3-b0', 'summary', 'Key points',
       '| Learn | |\n|---|---|\n'
       '| Active transport | particles move against a concentration gradient, using energy from respiration, through carrier proteins |\n'
       '| Where it matters | ions into root hairs; glucose into villus cells; glucose reabsorbed in kidney tubules |\n'
       '| What stops it | anything that stops respiration, such as no oxygen in waterlogged soil |\n'
       '| Diffusion and osmosis | down a gradient, no energy from respiration |',
       C('3', 1, 20, 21, 22, 23, 7), ['AO1']),
 block('3.3.3-b1', 'learner_objective', 'What this section covers',
       'What active transport is, how carrier proteins do it, and why root hair cells, the villi and the kidney '
       'tubules depend on it.', [], ['AO1']),
 block('3.3.3-b2', 'definition', 'Active transport',
       'Active transport is the movement of particles through a cell membrane from a region of lower concentration '
       'to a region of higher concentration using energy from respiration.', C('3', 1), ['AO1']),
 block('3.3.3-b3', 'process', 'How carrier proteins move particles',
       'Active transport is done by carrier proteins in the cell membrane. A particle binds to a carrier protein that '
       'fits it, on one side of the membrane. The carrier changes shape and moves the particle across, releasing it '
       'on the other side. The energy for this comes from respiration: some carriers use it directly, others use it '
       'indirectly, but either way active transport stops when respiration stops. Cells that do a lot of active '
       'transport contain many mitochondria, which release this energy.', C('3', 24, 25), ['AO1']),
 block('3.3.3-b4', 'plain_explanation', 'Root hair cells',
       'Mineral ions such as nitrate are often more concentrated inside root hair cells than in the soil water around '
       'them. Diffusion would carry them out, not in, so root hair cells take them in against the concentration '
       'gradient by active transport. This needs energy from respiration, so roots need oxygen. In waterlogged soil, '
       'which holds little oxygen, the roots take up fewer ions, and crops can show signs of mineral deficiency.',
       C('3', 20, 21), ['AO1']),
 block('3.3.3-b5', 'plain_explanation', 'The villi and the kidney tubules',
       'Epithelial cells of the villi in the small intestine take in glucose by active transport. Glucose can then be '
       'absorbed even when there is less of it in the gut than in the cells, so little is left to be lost. Cells '
       'lining the kidney tubules reabsorb glucose in the same way, returning it to the blood so that it is not '
       'lost in the urine.', C('3', 22, 23), ['AO1']),
 block('3.3.3-b6a', 'comparison', 'Three ways across a membrane',
       'The table sets the three processes side by side.\n\n'
       '| | Diffusion | Osmosis | Active transport |\n|---|---|---|---|\n'
       '| What moves | particles of a gas or solute | water molecules | particles such as ions or glucose |\n'
       '| Direction | down a concentration gradient | from a dilute to a more concentrated solution | '
       'against a concentration gradient |\n'
       '| Energy from respiration | not needed | not needed | needed |\n'
       '| Proteins in the membrane | none needed for simple diffusion | water also passes through water channel '
       'proteins | carrier proteins needed |\n\n'
       'A quick test: ask which way the particles go compared with their gradient. Down the gradient, the cell '
       'spends no energy from respiration. Against the gradient, it must.', C('3', 1, 2, 7, 24, 26), ['AO1']),
 block('3.3.3-b8', 'cross_link', 'Where this connects',
       'A concentration gradient, and diffusion down one, are explained in Diffusion (3.3.1). Mitochondria and '
       'their job are in Cell structure (3.2). Root hairs return in Transport in plants (3.7), the villi in '
       'Absorption (3.6.2.4), and the kidney in Excretion in humans (3.11).', [], ['AO1']),
 block('3.3.3-b7', 'misconception', 'Not every movement needs energy',
       'Only active transport needs energy from respiration, because it moves particles against a concentration '
       'gradient. Diffusion and osmosis move particles down a gradient, from where there are more to where there '
       'are fewer, and need no energy from respiration.', C('3', 7), ['AO1']),
])

i3 = [
 card('3', '3.3.2-01', 'FEATURE', C('3', 2, 3),
      'A strip of onion epidermis is placed in a solution that is more dilute than its cell sap. Describe what '
      'happens to the cells.',
      'Water enters the cells by osmosis. The vacuoles swell and push the cytoplasm against the cell walls, so the '
      'cells become turgid. The walls stop them bursting.',
      ['1 mark: the fact that water enters by osmosis.',
       '1 mark: the feature named: the cells become turgid, with the vacuole swelling against the wall.']),
 card('3', '3.3.2-01', 'WHY', C('3', 3),
      'Explain why a plant cell placed in pure water swells but does not burst.',
      'Pure water is more dilute than the cell sap, so water enters the cell by osmosis and the vacuole swells. The '
      'cell wall is strong and resists the pressure, so the cell becomes turgid instead of bursting.',
      ['1 mark: the reason water enters: the water is more dilute than the cell sap, because of which water moves in '
       'by osmosis.',
       '1 mark: the reason it does not burst: the cell wall resists the pressure, so the cell becomes turgid.']),
 card('3', '3.3.2-01', 'MISCON', C('3', 6, 3),
      'A learner writes: "The potato cells were placed in a turgid solution and became hypertonic." Explain the error '
      'in this sentence.',
      'The two kinds of word have been swapped. Hypertonic describes a solution, compared with the cell contents; '
      'turgid describes a cell that has swollen against its wall. A correct sentence is: "The potato cells were '
      'placed in a hypotonic solution and became turgid."',
      ['1 mark: names the confusion: a cell word used for the solution and a solution word used for the cell.',
       '1 mark: a correct statement that uses a solution word for the solution and a matching cell word for the cell.']),
 card('3', '3.3.2-02', 'FEATURE', C('3', 12),
      'A red blood cell is placed in a salt solution that is more concentrated than its cytoplasm. Describe what '
      'happens to the cell.',
      'Water leaves the cell by osmosis, so the cell shrinks and becomes shrivelled.',
      ['1 mark: the fact that water leaves by osmosis.',
       '1 mark: the feature named: the cell shrinks and becomes shrivelled.']),
 card('3', '3.3.2-02', 'WHY', C('3', 11, 3),
      'Explain why a red blood cell placed in pure water can burst, while a leaf cell placed in pure water does not.',
      'Water enters both by osmosis. The red blood cell has no cell wall to resist swelling, so it can burst; the '
      'leaf cell\'s wall resists, so it becomes turgid.',
      ['1 mark: the reason both take in water: because pure water is more dilute, water enters by osmosis.',
       '1 mark: the reason for the difference: the animal cell has no cell wall to resist swelling.']),
 card('3', '3.3.2-03', 'SYNTH', C('3', 29, 13),
      'Describe how you would investigate the effect of salt solution concentration on onion epidermis cells, using '
      'a light microscope.',
      'Independent variable: salt concentration, for example water and four stronger solutions. Method: mount a '
      'strip of epidermis in a drop of each, add a coverslip, wait ten minutes. Dependent variable: count the cells in '
      'one field of view and the number plasmolysed; work out the percentage. Keep the same: the onion, the size of '
      'strip, the waiting time and the temperature. Repeat with three fields for each solution and find the mean.',
      ['1 mark: independent variable: the salt concentration changed, with a range of at least four.',
       '1 mark: method: epidermis mounted in each solution under a coverslip and left for a fixed time.',
       '1 mark: dependent variable: the percentage of cells plasmolysed, counted in a field of view (measured).',
       '1 mark: two variables kept the same (controlled): onion, strip size, time, temperature.',
       '1 mark: repeat counts for each solution and calculate a mean.']),
 card('3', '3.3.2-03', 'LIM', C('3', 27, 13),
      'A learner mounts onion epidermis in concentrated salt solution and looks at it straight away. No cells look '
      'plasmolysed. Suggest why, and how the method could be improved.',
      'One likely reason is that there was not enough time: water leaves the cells by osmosis over several minutes. '
      'Another possibility is that the salt solution was not concentrated enough. Improvement: leave the slide for '
      'about ten minutes before looking (or use a more concentrated solution), and compare it with a strip mounted '
      'in water.',
      ['1 mark: a plausible error and its effect: too little time for water to leave the cells by osmosis; accept a '
       'solution not concentrated enough.',
       '1 mark: an improvement tied to the error given: wait several minutes, or use a more concentrated solution.']),
 card('3', '3.3.2-03', 'APP', C('3', 3, 4, 14, 19),
      'Strips of pumpkin stem are left for an hour, some in pure water and some in a concentrated sugar solution. '
      'Explain why the strips from the water feel firm and those from the sugar solution feel soft.',
      'In water, the cells take in water by osmosis and become turgid, so the strip is firm. The sugar solution is '
      'more concentrated than the cell sap, so the cells lose water, become flaccid and the strip is soft.',
      ['1 mark: the given situation in water: cells turgid, so the strip is firm.',
       '1 mark: in sugar solution: water lost because the solution is more concentrated, so cells flaccid.']),
 card('3', '3.3.2-04', 'SYNTH', C('3', 28, 8),
      'Describe how you would investigate how the concentration of sucrose solution affects the change in mass of '
      'potato tissue.',
      'Independent variable: sucrose concentration, 0.0 to 0.8 mol/dm³. Method: cut equal cylinders with a cork '
      'borer, blot and weigh each, leave one in each solution for 30 minutes, blot the same way and reweigh. '
      'Dependent variable: percentage change in mass. Keep the same: cylinder size, time, temperature, potato. Repeat '
      'each concentration three times and find the mean.',
      ['1 mark: independent variable: the sucrose concentration changed, over a range.',
       '1 mark: method: equal cylinders blotted and weighed before and after a fixed time in the solution.',
       '1 mark: dependent variable: percentage change in mass (measured).',
       '1 mark: two variables kept the same (controlled): cylinder size, time, temperature, potato.',
       '1 mark: repeats at each concentration and a mean.']),
 card('3', '3.3.2-04', 'LIM', C('3', 10),
      'In an osmosis investigation, a learner weighs each potato cylinder straight from its solution, without '
      'blotting it. Suggest how this affects the results and how the method could be improved.',
      'Solution left on the surface adds mass that the cells did not take up, so every cylinder seems to gain more '
      'mass, or lose less, than it really did. Improvement: blot every cylinder in the same way before each weighing.',
      ['1 mark: the error and its effect: surface solution makes each mass gain too large or each loss too small.',
       '1 mark: the improvement: blot every cylinder in the same way before weighing.']),
 card('3', '3.3.2-04', 'APP', C('3', 9, 3, 4),
      'A learner repeats the osmosis investigation with sweet potato. The cylinders gain mass in pure water and in '
      '0.1 mol/dm³ sucrose, and lose mass in 0.2 mol/dm³ sucrose and every stronger solution. Suggest the '
      'concentration of the sweet potato cell contents, and explain your answer.',
      'Between 0.1 and 0.2 mol/dm³: the cylinders gain water from weaker solutions and lose it to stronger ones, so '
      'the match lies between the last gain and the first loss.',
      ['1 mark: a value for this situation: between 0.1 and 0.2 mol/dm³.',
       '1 mark: the reasoning, because water enters from a more dilute solution and leaves into a more concentrated '
       'one, so no change happens where the two match.']),
 card('3', '3.3.2-05', 'CHAIN', C('3', 16, 17),
      'Explain how water in the soil reaches the xylem in a root.',
      'Soil water usually has a higher water potential than the cell sap of a root hair cell, so water enters the '
      'root hair by osmosis. Because the water potential is lower towards the centre of the root, water then moves '
      'across the root, through the cells and along the cell walls, so the result is that it reaches the xylem.',
      ['1 mark: the starting difference: when the soil water has a higher water potential than the root hair cell '
       'sap, water enters by osmosis.',
       '1 mark: because there is a water potential gradient across the root, water moves towards the centre, so the '
       'effect is that it reaches the xylem.']),
 card('3', '3.3.2-05', 'APP', C('3', 18, 19),
      'A gardener adds far too much fertiliser to a bed of seedlings. The soil is still wet, but the '
      'seedlings wilt. Explain why.',
      'Likely, the dissolved fertiliser made the soil water more concentrated than the root cell sap (lower water '
      'potential). If so, water leaves the roots by osmosis, the cells become flaccid and the seedlings wilt.',
      ['1 mark: the given situation: if the soil water has become more concentrated than the root cell sap (lower '
       'water potential).',
       '1 mark: so water leaves the roots by osmosis, because the gradient is reversed, and the cells become flaccid.']),
 card('3', '3.3.2-06', 'PROC', C('3', 14, 19),
      'Outline how turgor pressure supports the soft stem of a pumpkin plant.',
      'First, water enters the stem cells by osmosis and each vacuole swells. Then the cell contents push outwards on '
      'the cell wall: this is turgor pressure, and the wall pushes back. The result is firm, turgid cells pressing '
      'against one another, so the stem stays upright.',
      ['1 mark: first step: water enters the cells by osmosis and the vacuoles swell.',
       '1 mark: then turgor pressure pushes the cell contents against the wall, which resists.',
       '1 mark: result: turgid cells press against each other, so the stem is firm.']),
 card('3', '3.3.3-01', 'DEF', C('3', 1),
      'Define active transport.',
      'Active transport is the movement of particles through a cell membrane from a region of lower concentration to '
      'a region of higher concentration using energy from respiration.',
      ['1 mark: the definition: movement of particles through a cell membrane from lower to higher concentration.',
       '1 mark: the key feature it must include: using energy from respiration.']),
 card('3', '3.3.3-01', 'MISCON', C('3', 7, 2),
      'A learner says: "Water enters root hair cells by osmosis, so the cells must use energy from respiration to '
      'take it in." Explain the error.',
      'Osmosis needs no energy from respiration: water moves down its own gradient, from the more dilute soil water '
      'into the more concentrated cell sap. Only active transport, which moves particles against a concentration '
      'gradient, needs energy from respiration.',
      ['1 mark: names the error: osmosis has been treated as needing energy.',
       '1 mark: the correct statement: only active transport, against a gradient, needs energy from respiration.']),
 card('3', '3.3.3-02', 'CHAIN', C('3', 20, 21, 25),
      'Discuss the importance of active transport in the uptake of mineral ions by root hair cells.',
      'Ions such as nitrate are often more concentrated inside root hair cells than in soil water, so they can only '
      'be taken in against the gradient, by active transport. This lets the plant gather the ions it needs for '
      'growth. It uses energy from respiration, so when waterlogged soil lacks oxygen, uptake falls.',
      ['1 mark: when ions are more concentrated inside the root hair cell than in the soil water, they can only be '
       'taken in against the gradient, by active transport.',
       '1 mark: so the plant can gather the ions it needs for growth, because diffusion alone would not.',
       '1 mark: it depends on respiration, so the effect of a lack of oxygen (waterlogged soil) is less uptake.']),
 card('3', '3.3.3-02', 'APP', C('3', 21, 20),
      'Maize in a field that has been flooded for a week shows signs of mineral deficiency, although the '
      'soil contains plenty of mineral ions. Suggest why.',
      'In this flooded field the soil holds little oxygen, so the root cells respire less and release less energy. '
      'Active transport needs that energy, so the roots take up fewer ions.',
      ['1 mark: the given situation: flooded soil holds little oxygen, so less respiration in the roots.',
       '1 mark: so less active transport, because it needs energy from respiration: fewer ions taken up.']),
 card('3', '3.3.3-03', 'CHAIN', C('3', 22, 23, 25),
      'Discuss the importance of active transport in the villi of the small intestine and in the kidney tubules.',
      'Villus cells take in glucose by active transport even when less is left in the gut than in the cells, so '
      'little is lost. Kidney tubule cells reabsorb glucose the same way, so none is lost in urine. Both need energy '
      'from respiration, so these cells have many mitochondria.',
      ['1 mark: in the villi, glucose is absorbed even when less is in the gut than in the cells, so little is lost.',
       '1 mark: in the kidney tubules, glucose is reabsorbed by active transport, so the effect is none lost in urine.',
       '1 mark: because it depends on respiration, these cells have many mitochondria.']),
 card('3', '3.3.3-03', 'APP', C('3', 23, 1),
      'A poison stops respiration in the cells lining the kidney tubules. Suggest what would happen to the amount of '
      'glucose in the urine, and why.',
      'In this case glucose would appear in the urine. Without respiration there is no energy for active transport, '
      'so the tubule cells cannot reabsorb glucose and it stays in the urine.',
      ['1 mark: the given situation leads to more glucose in the urine.',
       '1 mark: because active transport needs energy from respiration, so glucose is not reabsorbed.']),
 card('3', '3.3.3-04', 'PROC', C('3', 24),
      'Describe how a carrier protein moves a particle across a cell membrane during active transport.',
      'First the particle binds to a carrier protein in the membrane that fits it. Then the carrier changes shape and '
      'moves the particle across; the energy for this comes from respiration. The result is that the particle is '
      'released on the other side of the membrane.',
      ['1 mark: first step: the particle binds to a specific carrier protein in the membrane.',
       '1 mark: then the carrier changes shape, using energy that comes from respiration; the result is the particle '
       'released on the other side.']),
 card('3', '3.3.3-04', 'APP', C('3', 22, 24, 25),
      'Cells lining the villi contain many more mitochondria than most other cells of the gut wall. Describe how '
      'this links to the work villus cells do.',
      'In this case villus cells take in glucose by active transport, which needs energy from respiration; many '
      'mitochondria supply that energy.',
      ['1 mark: the given situation: villus cells take in glucose by active transport using carrier proteins.',
       '1 mark: because this needs energy from respiration, so many mitochondria supply it.']),
 task('3', 'multiple_choice_set', ['3.3.2-01', '3.3.3-01'], C('3', 4, 6, 7), ['AO1', 'AO2'], None, 3, 2,
      'Three questions. Choose one option for each.\n\n'
      '1. A plant cell is placed in a solution more concentrated than its cell sap. What happens?\n'
      'A  Water enters and the cell becomes turgid.\nB  Water leaves and the cell becomes flaccid.\n'
      'C  Sucrose enters and the cell bursts.\nD  No water moves, because the cell wall stops it.\n\n'
      '2. Which movement needs energy from respiration?\n'
      'A  oxygen diffusing into a respiring cell\nB  water entering a root hair cell by osmosis\n'
      'C  ions moving into a cell from a lower to a higher concentration\n'
      'D  water leaving a cell placed in a hypertonic solution\n\n'
      '3. Which word describes a solution, not a cell?\nA  turgid\nB  flaccid\nC  hypotonic\nD  plasmolysed',
      'Key: 1 B, 2 C, 3 C.\n'
      '1. The solution is more concentrated, so water leaves by osmosis and the cell becomes flaccid (B). A has the '
      'direction backwards; C has the solute moving, not water; D treats the wall as a barrier to water.\n'
      '2. Only movement against a gradient needs energy (C). A, B and D are all down a gradient.\n'
      '3. Hypotonic compares a solution with the cell contents (C). A, B and D describe the state of a cell.',
      ['The key: one mark per correct option, three marks in all.',
       'Each distractor is a named error: direction of water reversed, energy demanded for passive movement, a cell '
       'word given for a solution.']),
 task('3', 'short_answer', ['3.3.2-01'], C('3', 2, 4, 5), ['AO1', 'AO2'], 'state', 8, 3,
      'A learner studies thin slices of red onion under a microscope.\n'
      '(a) State what is meant by osmosis. [2]\n'
      '(b) Name the type of solution in which the onion cells show no net gain or loss of water. [1]\n'
      '(c) Describe what happens to an onion cell placed in a solution more dilute than its cell sap. [2]\n'
      '(d) A slice is left in a concentrated salt solution for 20 minutes. Suggest what the cells will look like '
      'under the microscope, and explain why. [3]',
      '(a) The net movement of water molecules from a dilute solution to a more concentrated solution, through a '
      'partially permeable membrane.\n(b) Isotonic.\n'
      '(c) Water enters by osmosis; the vacuole swells and the cell becomes turgid.\n'
      '(d) The cell membrane and cytoplasm will have pulled away from the cell walls: the cells are plasmolysed. The salt solution is '
      'more concentrated than the cell sap, so water left the cells by osmosis.',
      ['(a) 2 marks: 1 mark for net movement of water from dilute to more concentrated; 1 mark for through a '
       'partially permeable membrane.',
       '(b) 1 mark: isotonic.',
       '(c) 2 marks: 1 mark for water enters by osmosis; 1 mark for the cell becomes turgid.',
       '(d) 3 marks, three creditable points: 1 mark for the cell membrane (with the cytoplasm) pulled away from the cell wall, i.e. '
       'plasmolysed; flaccid or "shrunk" alone does not earn it. 1 mark for the solution being more concentrated '
       'than the cell sap; 1 mark for water leaving by osmosis.']),
 task('3', 'practical_task', ['3.3.2-04'], C('3', 8, 9, 10), ['AO3'], 'identify', 10, 3,
      'A learner investigated osmosis using cylinders of equal length and diameter, cut with a cork borer from one '
      'potato. Each cylinder was blotted, weighed, left in a sucrose solution for 30 minutes at room temperature, then '
      'blotted and weighed again.\n\n'
      '| Concentration of sucrose / mol/dm³ | Mass at start / g | Mass after 30 minutes / g | Change in mass / % |\n'
      '|---|---|---|---|\n'
      '| 0.0 | 2.50 | 2.80 | +12 |\n| 0.2 | 2.40 | 2.52 | |\n| 0.4 | 2.50 | 2.45 | |\n'
      '| 0.6 | 2.60 | 2.34 | |\n| 0.8 | 2.50 | 2.15 | -14 |\n\n'
      '(a) Identify the independent variable and the dependent variable. [2]\n'
      '(b) Complete the table by calculating the three missing percentage changes. [3]\n'
      '(c) Determine, from the table, the range of concentrations that contains the concentration of the potato cell '
      'contents, and explain your answer. [2]\n'
      '(d) State one variable, other than time, that was kept the same. [1]\n'
      '(e) Suggest one source of error in this method and an improvement for it. [2]',
      '(a) Independent: the concentration of the sucrose solution. Dependent: the percentage change in mass.\n'
      '(b) 0.2: 2.52 - 2.40 = 0.12 g, and 0.12 ÷ 2.40 = 0.05, which is +5%. 0.4: 2.45 - 2.50 = -0.05 g, and '
      '0.05 ÷ 2.50 = 0.02, which is -2%. 0.6: 2.34 - 2.60 = -0.26 g, and 0.26 ÷ 2.60 = 0.10, which is -10%.\n'
      '(c) Between 0.2 and 0.4 mol/dm³: the cylinder gained mass at 0.2 and lost mass at 0.4, so the solution '
      'matching the cell contents lies between them.\n'
      '(d) Temperature, or the size of the cylinders, or the potato they were cut from.\n'
      '(e) Only one cylinder was used at each concentration, so one unusual cylinder could mislead; repeat each '
      'concentration three times and calculate the mean.',
      ['(a) 2 marks: 1 mark for each variable correctly identified.',
       '(b) 3 marks: one mark per correct percentage with its sign; the table headings already carry the units.',
       '(c) 2 marks: 1 mark for the range from the data; 1 mark for the conclusion that no change in mass occurs '
       'where the solution matches the cell contents.',
       '(d) 1 mark: any one variable the method states was kept the same: the size of the cylinders, the temperature '
       'or the potato used.',
       '(e) 2 marks: 1 mark for a source of error; 1 mark for an improvement tied to that error.']),
]

# ============================================================ topic 4: 4.4.2, two objectives
c4 = [
 claim('4', 1, ['4.4.2-01'], 'Genotype is the genetic make-up of an organism in terms of the alleles present.',
       'definition', 'syllabus_direct'),
 claim('4', 2, ['4.4.2-01'], 'A genotype is written in allele symbols: a capital letter for the dominant allele and the '
       'same letter in lower case for the recessive allele, for example Tt.', 'factual'),
 claim('4', 3, ['4.4.2-01'], 'In a genetic diagram the parents are written as genotypes, pairs of allele symbols; a '
       'description such as tall or short is a phenotype and is not written in place of a genotype.',
       'misconception_correction'),
 claim('4', 4, ['4.4.2-07'], 'A genetic diagram for a monohybrid cross shows the parental phenotypes and genotypes, '
       'the gametes each parent can make, every possible fertilisation, and the offspring genotypes and phenotypes '
       'with their ratio.', 'procedural'),
 claim('4', 5, ['4.4.2-07'], 'Crossing two heterozygous parents (Tt × Tt) gives offspring genotypes TT, Tt and tt in '
       'the ratio 1 : 2 : 1, and phenotypes in the ratio 3 dominant : 1 recessive.', 'factual'),
 claim('4', 6, ['4.4.2-07'], 'Crossing a heterozygous parent with a homozygous recessive parent (Tt × tt) gives '
       'offspring Tt and tt in the ratio 1 : 1.', 'factual'),
 claim('4', 7, ['4.4.2-07'], 'A ratio from a genetic diagram predicts proportions, not exact numbers: a large number of '
       'offspring comes close to the ratio, but a small number can differ from it by chance.', 'inference'),
]
u442 = unit('CU-6116-4.4.2', 'Monohybrid inheritance', ['4.4.2-01', '4.4.2-07'], 'bio_quantitative', 2, [
 block('4.4.2-b0', 'summary', 'Key points',
       '| Learn | |\n|---|---|\n'
       '| Genotype | the alleles present, written as symbols: TT, Tt, tt |\n'
       '| Tt × Tt | 1 TT : 2 Tt : 1 tt, so 3 dominant : 1 recessive |\n'
       '| Tt × tt | 1 Tt : 1 tt |',
       C('4', 1, 2, 5, 6), ['AO1']),
 block('4.4.2-b1', 'learner_objective', 'What this section covers',
       'Genotypes, and genetic diagrams for monohybrid crosses.', [], ['AO1']),
 block('4.4.2-b2', 'definition', 'Genotype',
       'Genotype is the genetic make-up of an organism in terms of the alleles present. It is written in allele '
       'symbols: a capital letter for the dominant allele and the same letter in lower case for the recessive '
       'allele. Tt is a genotype.', C('4', 1, 2), ['AO1']),
 block('4.4.2-b3', 'process', 'Setting out a genetic diagram',
       'A genetic diagram has the same lines every time. First the parental phenotypes, then the parental genotypes, '
       'then the gametes each parent can make, then every possible fertilisation, often in a grid, and finally the '
       'offspring genotypes and phenotypes with their ratio.', C('4', 4), ['AO1']),
 block('4.4.2-b4', 'worked_calculation', 'Worked example: two heterozygous parents',
       'In a pearl millet variety grown in a school garden in Ondangwa, the allele for tall stems (T) is dominant to '
       'the allele for short stems (t). Two heterozygous tall plants are crossed: Tt × Tt. Each parent makes gametes '
       'T and t. The four fertilisations give TT, Tt, Tt and tt, so the genotype ratio is 1 : 2 : 1 and the phenotype '
       'ratio is 3 tall : 1 short. If 120 seeds grow, about 120 ÷ 4 = 30 are expected to be short, and 30 × 3 = 90 '
       'tall.', C('4', 4, 5), ['AO2']),
 block('4.4.2-b5', 'worked_application', 'A heterozygous parent and a homozygous recessive parent',
       'Cross a heterozygous tall plant with a short plant: Tt × tt. The tall parent makes gametes T and t; the short '
       'parent makes only t. The offspring are Tt and tt in the ratio 1 : 1, so about half are tall and half are '
       'short. Ratios like these predict proportions: a small number of offspring can differ from them by chance.',
       C('4', 6, 7), ['AO2']),
 block('4.4.2-b7', 'misconception', 'Genotype is not phenotype',
       'In a genetic diagram, the parents are written as genotypes, pairs of allele symbols such as Tt and tt. Words '
       'such as tall and short are phenotypes. They belong on the phenotype lines and never replace the genotypes.',
       C('4', 3), ['AO1']),
])
i4 = [
 card('4', '4.4.2-01', 'DEF', C('4', 1),
      'Define genotype.',
      'Genotype is the genetic make-up of an organism in terms of the alleles present.',
      ['1 mark: the definition: the genetic make-up of an organism.',
       '1 mark: the key feature it must include: in terms of the alleles present.']),
 card('4', '4.4.2-01', 'MISCON', C('4', 3, 2),
      'For a plant in which tall (T) is dominant to short (t), a learner records a cross only as '
      '"tall × short". Explain why this does not specify both parental genotypes.',
      'Tall and short describe phenotypes, not pairs of alleles. The short parent is tt, but the tall '
      'parent could be TT or Tt, so the record does not identify one genotype pair.',
      ['1 mark: identifies the error: tall and short are phenotypes, whereas genotypes are written as allele pairs.',
       '1 mark: the short parent must be tt but the tall parent could be TT or Tt, so its genotype is not specified.']),
 card('4', '4.4.2-07', 'CALC', C('4', 4, 5),
      'In a pearl millet variety, the allele for tall stems (T) is dominant to the allele for short stems (t). Two '
      'heterozygous tall plants are crossed, and 160 seeds grow into plants. Draw a genetic diagram for this cross, '
      'and use it to calculate how many plants are expected to be short.',
      'Parental phenotypes: tall × tall. Parental genotypes: Tt × Tt. Gametes: T, t and T, t. Offspring genotypes: '
      'TT, Tt, Tt, tt. Offspring phenotypes: 3 tall : 1 short. Short plants expected: 160 ÷ 4 = 40.',
      ['1 mark: method: parental phenotypes and genotypes (Tt × Tt) on the diagram.',
       '1 mark: gametes T and t from each parent.',
       '1 mark: all four offspring genotypes, from a grid or lines.',
       '1 mark: phenotype ratio 3 tall : 1 short.',
       '1 mark: final answer: 40 short plants, with working.']),
 card('4', '4.4.2-07', 'WHY', C('4', 5, 7),
      'Two heterozygous tall plants (Tt) are crossed. Explain why about one offspring in four is short, and why a '
      'small number of seeds may not show this ratio exactly.',
      'Each parent passes on T or t with equal chance, so one fertilisation in four gives tt, which is short. The '
      'ratio is a probability: a small number of offspring can differ from it by chance.',
      ['1 mark: the reason: each parent gives t half the time, so tt is one in four.',
       '1 mark: because the ratio is a probability, small samples differ by chance.']),
 task('4', 'short_answer', ['4.4.2-01', '4.4.2-07'], C('4', 2, 4, 5, 7), ['AO1', 'AO2'], 'state', 8, 3,
      'In a pearl millet variety, the allele for tall stems (T) is dominant to the allele for short stems (t).\n'
      '(a) State the genotype of a short plant. [1]\n'
      '(b) Name the phenotype of a plant with the genotype Tt. [1]\n'
      '(c) Draw a genetic diagram to show a cross between two heterozygous plants. [3]\n'
      '(d) A farmer near Outapi grows 200 plants from this cross. Calculate how many are expected to be tall. [2]\n'
      '(e) Suggest why the number of tall plants the farmer counts may differ from your answer to (d). [1]',
      '(a) tt.\n(b) Tall.\n'
      '(c) Parents: Tt × Tt. Gametes: T and t from each parent. Offspring: TT, Tt, Tt, tt; 3 tall : 1 short.\n'
      '(d) 200 ÷ 4 = 50 short, so 50 × 3 = 150 tall.\n'
      '(e) A ratio predicts proportions; the actual offspring can differ from it by chance.',
      ['(a) 1 mark: tt. (b) 1 mark: tall.',
       '(c) 3 marks: 1 mark for parental genotypes and gametes; 1 mark for all four offspring genotypes; 1 mark for '
       'the 3 : 1 phenotype ratio. Accept a grid in place of lines.',
       '(d) 2 marks: 1 mark for the working (one in four short, or three in four tall); 1 mark for 150.',
       '(e) 1 mark: chance, or a ratio is a prediction, is the creditable point.']),
]

# ---- evidence (planning/references.json). Section-level locators; the teacher verifier checks each.
OS = 'SRC-OSB2E'
EVIDENCE = {
 ('3', 1): [('SRC-SYL-6116', 'printed p.11, 3.3.3: the syllabus definition', 'direct')],
 ('3', 2): [(OS, '5.2 Passive Transport (osmosis)', 'paraphrase')],
 ('3', 3): [(OS, '5.2 Passive Transport (tonicity in plant cells)', 'paraphrase')],
 ('3', 4): [(OS, '5.2 Passive Transport (tonicity in plant cells; plasmolysis)', 'paraphrase')],
 ('3', 5): [(OS, '5.2 Passive Transport (isotonic solutions)', 'paraphrase')],
 ('3', 6): [(OS, '5.2 Passive Transport (tonicity describes a solution relative to the cell)', 'paraphrase')],
 ('3', 7): [(OS, '5.2 Passive Transport; 5.3 Active Transport', 'paraphrase')],
 ('3', 9): [(OS, '5.2 Passive Transport (net movement of water and tonicity)', 'derivation')],
 ('3', 11): [(OS, '5.2 Passive Transport (red blood cells in hypotonic and hypertonic solutions)', 'paraphrase')],
 ('3', 12): [(OS, '5.2 Passive Transport (red blood cells in hypertonic solutions)', 'paraphrase')],
 ('3', 14): [(OS, '5.2 Passive Transport (turgor pressure); 30.5 Transport of Water and Solutes in Plants', 'paraphrase')],
 ('3', 16): [(OS, '30.5 Transport of Water and Solutes in Plants (water potential: solute and pressure)', 'paraphrase')],
 ('3', 17): [(OS, '30.5 Transport of Water and Solutes in Plants (movement of water through the root)', 'paraphrase')],
 ('3', 18): [(OS, '30.5 Transport of Water and Solutes in Plants (water potential gradients)', 'derivation')],
 ('3', 19): [(OS, '5.2 Passive Transport (turgor and wilting)', 'paraphrase')],
 ('3', 20): [(OS, '5.3 Active Transport (moving substances against a gradient)', 'derivation')],
 ('3', 21): [(OS, '5.3 Active Transport (energy requirement)', 'derivation')],
 ('3', 22): [(OS, '34.3 Digestive System Processes (absorption)', 'paraphrase')],
 ('3', 23): [(OS, '41.3 Kidney Function and Physiology (reabsorption)', 'paraphrase')],
 ('3', 24): [(OS, '5.3 Active Transport (carrier proteins; primary and secondary active transport)', 'paraphrase')],
 ('3', 25): [(OS, '4.3 Eukaryotic Cells (mitochondria); 5.3 Active Transport', 'derivation')],
 ('3', 26): [(OS, '5.2 Passive Transport (facilitated transport; aquaporins)', 'paraphrase')],
 ('4', 1): [('SRC-SYL-6116', 'printed p.28, 4.4.2: the syllabus definition', 'direct')],
 ('4', 2): [(OS, '12.2 Characteristics and Traits (alleles and their notation)', 'paraphrase')],
 ('4', 3): [(OS, '12.2 Characteristics and Traits (genotype and phenotype)', 'paraphrase')],
 ('4', 4): [(OS, '12.2 Characteristics and Traits (Punnett square)', 'paraphrase')],
 ('4', 5): [(OS, '12.2 Characteristics and Traits (monohybrid cross ratios)', 'paraphrase')],
 ('4', 6): [(OS, '12.2 Characteristics and Traits (test cross)', 'paraphrase')],
 ('4', 7): [(OS, '12.1 Mendel\'s Experiments and the Laws of Probability', 'derivation')],
}
for t, claims in (('3', c3), ('4', c4)):
    for c in claims:
        n = int(c['claim_id'].rsplit('-', 1)[1])
        ev = EVIDENCE.get((t, n))
        if ev:
            c['evidence'] = [{'source_id': a, 'locator': b, 'support_type': k} for a, b, k in ev]
        else:
            c['notes'] = ['No approved reference cited: a practical procedure. The teacher verifier checks it against '
                          'SRC-SCHOOL once the operator names that textbook (planning/references.json).']

for t, claims, units, items in (('3', c3, [u332, u333], i3), ('4', c4, [u442], i4)):
    base = os.path.join(OUT, t)
    for sub in ('claims', 'content-units', 'learning-items'):
        d = os.path.join(base, sub)
        if os.path.isdir(d):
            for f in os.listdir(d):
                os.remove(os.path.join(d, f))
    write(os.path.join(base, 'claims', 'canonical_claim_ledger.json'),
          {'ledger_id': 'CLM-LEDGER-6116-%s' % t, 'claims': claims})
    for u in units:
        write(os.path.join(base, 'content-units', '%s.json' % u['unit_id']), u)
    write(os.path.join(base, 'learning-items', 'topic_%s_items.json' % t),
          {'dataset_id': 'ITEMS-6116-%s' % t, 'topic_id': t, 'items': items})
    print('topic %s: %d claims, %d units (%s words), %d items -> %s'
          % (t, len(claims), len(units), '+'.join(str(u['word_count']) for u in units), len(items), base))
