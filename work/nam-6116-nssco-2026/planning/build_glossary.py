#!/usr/bin/env python3
"""Write curriculum/glossary.json: settled senses for the terms learners confuse.

Shape follows the model (9702 Physics): every term is one the examiner reports record
candidates confusing, or one a confused term depends on. Where the syllabus itself
defines the term ("define X as ..."), the sense is taken from the registry so the notes
use the syllabus's definition exactly; otherwise the sense is ours (provenance
judgement). The command-word glossary is kept as a second list, with use_in_prompts
read from the framework so the two can never disagree.
"""
import json, re

WS = 'work/nam-6116-nssco-2026'
reg = [o for o in json.load(open(f'{WS}/curriculum/objective_registry.json'))['objectives'] if o['parent_id']]
facts = json.load(open(f'{WS}/curriculum/syllabus-facts.json'))
fw = json.load(open(f'{WS}/curriculum/assessment-framework.json'))
mis = json.load(open(f'{WS}/curriculum/misconceptions.json'))['misconceptions']


def syllabus_def(term_regex):
    hits = [o for o in reg if re.match(r'define (the term )?(an? )?' + term_regex + r' (as|in terms of)', o['syllabus_text'], re.I)]
    if len(hits) != 1:
        raise SystemExit('expected one syllabus definition for %s, found %d' % (term_regex, len(hits)))
    o = hits[0]
    sense = re.sub(r'^define (the term )?(an? )?' + term_regex + r' (as )?', '', o['syllabus_text'], flags=re.I)
    return sense[0].upper() + sense[1:], o['objective_id']


# (term, syllabus regex or None, our sense if None, homonym warning, misconception ids)
TERMS = [
 ('aerobic respiration', 'aerobic respiration', None, 'Not breathing: respiration happens in every cell; breathing moves air.', []),
 ('breathing', None, 'The movement of air into and out of the lungs.', 'Not respiration.', []),
 ('egestion', 'egestion', None, 'Not excretion: egested food was never part of the body\'s metabolism.', []),
 ('excretion', None, 'The removal from the body of the waste products of metabolism, such as urea and carbon dioxide.', 'Not egestion.', []),
 ('growth', 'growth', None, 'Not development.', []),
 ('development', 'development', None, 'Not growth.', []),
 ('genotype', 'genotype', None, 'Not phenotype: the genotype is written in allele symbols.', ['MISCON-6116-014']),
 ('phenotype', 'phenotype', None, 'Not genotype: the phenotype is a description, such as "tall".', ['MISCON-6116-014']),
 ('mitosis', 'mitosis', None, 'Not meiosis.', ['MISCON-6116-005']),
 ('meiosis', 'meiosis', None, 'Not mitosis.', ['MISCON-6116-005']),
 ('diffusion', None, 'The net movement of particles from a region of higher concentration to a region of lower concentration, down a concentration gradient, using the kinetic energy of the particles only.', 'Needs no energy from respiration; contrast active transport.', ['MISCON-6116-031']),
 ('active transport', 'active transport', None, 'Needs energy from respiration; diffusion and osmosis do not.', ['MISCON-6116-031']),
 ('osmosis', None, 'The net movement of water molecules from a dilute solution to a more concentrated solution through a partially permeable membrane.', None, ['MISCON-6116-007']),
 ('turgid / flaccid / plasmolysed', None, 'Words for the state of a plant cell: firm and pressed against its wall; soft; with the cytoplasm pulled away from the wall.', 'Describe the cell, never the solution.', ['MISCON-6116-007']),
 ('hypertonic / isotonic / hypotonic', None, 'Words for a solution compared with the cell contents: more concentrated; the same; more dilute.', 'Describe the solution, never the cell.', ['MISCON-6116-007']),
 ('magnification', None, 'Image size divided by actual size, both in the same unit. It has no unit and is written with a times sign, such as ×400.', 'Not actual size, which is a length with a unit.', ['MISCON-6116-008']),
 ('denatured', None, 'Describes an enzyme whose active site has changed shape, so its substrate no longer fits.', 'Not "killed": an enzyme is a protein, not a living thing.', ['MISCON-6116-021']),
 ('xylem', None, 'The tissue that carries water and mineral ions up from the roots.', 'Not phloem.', ['MISCON-6116-022']),
 ('phloem', None, 'The tissue that carries sucrose and amino acids from where they are made or stored to where they are used.', 'Not xylem.', ['MISCON-6116-022']),
 ('translocation', 'translocation', None, 'Happens in phloem, not xylem.', ['MISCON-6116-022']),
 ('transpiration', 'transpiration', None, 'Water evaporates at the mesophyll cell surfaces; vapour then diffuses out through the stomata.', ['MISCON-6116-017']),
 ('independent variable', None, 'The variable the investigator chooses to change.', 'Not the dependent variable, which is measured.', ['MISCON-6116-029']),
 ('dependent variable', None, 'The variable the investigator measures.', 'Not the independent variable, which is changed.', ['MISCON-6116-029']),
 ('producer', 'producer', None, 'Not a decomposer.', ['MISCON-6116-033']),
 ('decomposer', 'decomposer', None, 'Not a producer.', ['MISCON-6116-033']),
 ('deamination', 'deamination', None, 'An excretory process of the liver; bile production is a different liver function.', ['MISCON-6116-037']),
 ('pathogen', 'pathogen', None, None, []),
 ('extinction', None, 'The permanent loss of a species: no living members remain anywhere.', 'Not "endangered", where some members still live.', []),
 ('active immunity', 'active immunity', None, 'Not passive immunity: memory cells are made.', []),
 ('passive immunity', 'passive immunity', None, 'Not active immunity: no memory cells are made.', []),
]

terms = []
for term, rx, own, warn, mids in TERMS:
    if rx:
        sense, oid = syllabus_def(rx)
        prov = {'provenance': 'syllabus', 'objective_id': oid}
    else:
        sense, prov = own, {'provenance': 'judgement'}
    terms.append({'term': term, 'sense': sense, 'homonym_warning': warn,
                  'misconception_ids': mids, **prov})

known = {m['misconception_id'] for m in mis}
bad = sorted({i for t in terms for i in t['misconception_ids']} - known)
if bad:
    raise SystemExit('glossary cites misconceptions not in the register: %s' % bad)

use = {c['word']: c['use_in_prompts'] for c in fw['command_words']}
cw = [{'term': w['word'], 'meaning': w['meaning'],
       'use_in_prompts': use.get(w['word'].lower().replace('/ ', '/'), False),
       'source': w['source']} for w in facts['command_words']]

json.dump({'glossary_id': 'GLOSSARY-6116', 'status': 'settled',
           'note': ('Terms the examiner reports record candidates confusing, or that a confused term '
                    'depends on. Where the syllabus defines a term, its definition is used verbatim. '
                    'Use these senses exactly, everywhere.'),
           'terms': terms,
           'command_words': {'source': 'syllabus glossary printed p.39-40 [PDF 42-43]',
                             'use_in_prompts_from': 'curriculum/assessment-framework.json', 'words': cw}},
          open(f'{WS}/curriculum/glossary.json', 'w'), indent=2, ensure_ascii=False)
print('glossary: %d terms (%d from the syllabus), %d command words'
      % (len(terms), sum(t['provenance'] == 'syllabus' for t in terms), len(cw)))
