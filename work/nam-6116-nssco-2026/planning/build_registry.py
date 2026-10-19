#!/usr/bin/env python3
"""Build the objective registry from the transcribed syllabus.

PLANNER.md section 2. Its objective_type vocabulary is business_*; 9702 Physics
uses phys_*/prac_*, so a subject-specific vocabulary is expected. Biology uses
bio_* for content and prac_* for the Paper 3 skills, which are assessed under a
different AO and must not be collapsed into content types.

Every objective in the syllabus is registered and mandatory. Measured exposure
calibrates emphasis later; it never removes an objective from the registry.
"""
import json, re, collections

WS = 'work/nam-6116-nssco-2026'
facts = json.load(open(f'{WS}/curriculum/syllabus-facts.json'))

# ---- classification -----------------------------------------------------------
# Verb-first. The leading verb of a syllabus objective is the strongest signal of
# what a learner must do; content words only refine it. The earlier content-first
# regex typed "explain how temperature affects transpiration" as quantitative (it
# contains "rate of") and "state the functions of lymphocytes" as a practical skill
# (it mentions the microscope). Anything this cannot settle is fixed by an explicit
# override in planning/objective_overrides.json, recorded as judgement.
#
# AO follows the syllabus's own descriptions (printed p.35-36 [PDF 38-39]):
#   A (AO1) knowledge with understanding: recall and explanation of taught content,
#           vocabulary, conventions, units, apparatus, applications and implications
#   B (AO2) handling information and solving problems: calculation, data, comparison,
#           prediction, reasoned explanation of relationships, unfamiliar situations
#   C (AO3) practical skills, assessed only on Paper 3
PRACTICAL = re.compile(
    r'^(investigate|design|plan|observe|record|measure|make (?:temporary|a clear|observations)|'
    r'prepare and stain|use and manipulate|handle|use (?:appropriate techniques|dialysis|usual)|'
    r'draw (?:and interpret|prepared|charts|an appropriate conclusion|organisms)|'
    r'complete tables|select suitable|label each|plot the|present points|interpret charts|'
    r'identify sources of error|suggest possible|analyse anomalous|discuss trends|evaluate presented|'
    r'interpret practical|recall (?:familiar|of simple)|describe(?:,)? (?:explain )?or comment|'
    r'name appropriate apparatus|recognise, observe|calculate the magnification of a drawing|'
    r'state the hypothesis|distinguish between independent|explore)\b', re.I)
PRAC_PRESENT = re.compile(r'^(complete tables|select suitable|label each|plot the|present points|'
                          r'draw charts|record results|make a clear|draw (?:and interpret )?prepared|'
                          r'draw organisms)', re.I)
PRAC_MMO = re.compile(r'^(make (?:temporary|observations)|prepare and stain|use and manipulate|handle|'
                      r'use (?:appropriate techniques|dialysis|usual)|measure|record readings|'
                      r'name appropriate apparatus|recognise, observe|recall)', re.I)
MATHS = re.compile(r'^(perform|use (?:averages|decimals|fractions|percentages|ratios|reciprocals|positive|'
                   r'standard notation|acceptable)|recognise and use|solve|calculate)\b', re.I)


def classify(text, code):
    """-> (objective_type, AOs, papers)"""
    t = ' '.join(text.split())
    low = t.lower()
    verb = low.split()[0]
    if PRACTICAL.match(t):
        # An objective to investigate, design or plan is practised as one coherent written plan (Paper 3
        # sets these at 4-5 marks: 2020 P3 1(c), 3(b); 2023 P3 3(c), 4(b); 2024 P3 1(a)), not as
        # fragments.
        if re.match(r'^(investigate|design and carry out|plan an experiment)', low):
            return 'prac_investigation', ['AO3'], ['3']
        ot = ('prac_presentation' if PRAC_PRESENT.match(t) else
              'prac_mmo' if PRAC_MMO.match(t) else 'prac_analysis')
        return ot, ['AO3'], ['3']
    if MATHS.match(t):
        return 'bio_quantitative', ['AO2'], ['1', '2']
    if verb == 'define':
        return 'bio_definition', ['AO1'], ['1', '2']
    if verb in ('compare', 'distinguish'):
        return 'bio_comparison', ['AO2'], ['1', '2']
    if verb in ('predict', 'suggest', 'interpret') or re.match(r'^(identify and explain|relate)\b', low):
        return 'bio_application', ['AO2'], ['1', '2']
    if verb == 'discuss' or re.match(r'^(consider|give reasons)', low):
        # The syllabus defines Discuss as "a critical account of the points involved" (printed p.39).
        # In the papers 6 of the 7 "discuss" parts ask for developed points ("discuss two effects",
        # "discuss how ... may affect"); one is two-sided ("advantages and disadvantages of a kidney
        # transplant compared with dialysis"). So only an objective that is itself two-sided is an
        # evaluation; the rest are reasoned explanations.
        if re.search(r'advantages and disadvantages|for and against|self-pollination and cross-pollination', low):
            return 'bio_evaluation', ['AO2'], ['1', '2']
        return 'bio_causal', ['AO2'], ['1', '2']
    if verb == 'explain':
        # explaining a taught mechanism is understanding (A1); explaining WHY an
        # outcome follows, or how a factor changes a rate, is reasoned explanation (B5)
        if re.search(r'\bwhy\b|\baffects?\b|\beffects? of\b|\bproblems?\b|\bdistribution\b|'
                     r'\bimportance\b|\breasons\b|\bcontributes\b|\bcauses\b', low):
            return 'bio_causal', ['AO2'], ['1', '2']
        return 'bio_process', ['AO1'], ['1', '2']
    if verb in ('identify', 'name', 'list') or re.match(r'^draw the (external )?structure', low):
        return 'bio_structure', ['AO1'], ['1', '2']
    if verb in ('describe', 'outline', 'state', 'construct', 'recall'):
        if re.search(r'\bstructure\b|\badaptive features\b|\badaptations\b|\badapted\b', low):
            return 'bio_structure', ['AO1'], ['1', '2']
        if re.search(r'^(describe|outline) (how|the (process|synthesis|formation|production|digestion|'
                     r'transfer|translocation|events|growth|maintenance|control|flow|increase|'
                     r'inheritance|carbon cycle|nitrogen cycle|processes))|\bcycle\b|^describe transpiration|'
                     r'^describe (?:asexual|spore|tuber|fertilisation|mutation|natural selection|evolution|'
                     r'temperature regulation|mitosis|the development)', low):
            return 'bio_process', ['AO1'], ['1', '2']
        if re.search(r'\bfunctions?\b|\broles?\b|\bimportance\b|\bsignificance\b|\buses?\b|\beffects?\b|'
                     r'\bcauses?\b|\bimplications\b|\bconsequences\b', low):
            # "state the function of X" is a fact to recall; "describe the role / effects /
            # causes of X" asks how one thing acts on another, which carries a reason
            return ('bio_function' if verb == 'state' else 'bio_relationship'), ['AO1'], ['1', '2']
        return 'bio_concept', ['AO1'], ['1', '2']
    return 'bio_concept', ['AO1'], ['1', '2']


# depth_tier: 1 a term to know, 2 a fact or relationship, 3 a multi-step idea, 4 a container
def tier(text, has_children):
    if has_children: return 4
    t = text.lower()
    if re.match(r'\s*(define|state|name|list|identify)\b', t): return 1
    if re.search(r'^(explain|discuss|investigate|evaluate|analyse|compare|design|plan|suggest|predict)|'
                 r'describe how|describe and explain|interpret', t): return 3
    return 2


OVR = json.load(open(f'{WS}/planning/objective_overrides.json'))
_ovr_used = set()


def override(text):
    for k, v in OVR['overrides'].items():
        if text.startswith(k):
            _ovr_used.add(k)
            return v
    return None


rows = [r for r in facts['content'] if not r['code'].isdigit()]
codes = {r['code'] for r in facts['content']}
def children(c): return any(o != c and o.startswith(c + '.') for o in codes)

objectives, sidecar, headings = [], {}, {}
# Registry shape follows the model workspaces (9702 Physics): topic containers with
# no parent, and every assessable objective directly under its topic. Sub-topic
# headings and the bullets that were decomposed are NOT registered as objectives,
# because build/make_work_order.py plans slots for every entry that has a parent,
# and a heading ("3.4 Biological molecules") or a list container is not a skill a
# card can test. Both are kept in the planning sidecar, so the decomposition stays
# traceable to the verbatim bullet.
for r in facts['content']:
    topic = r['code'].split('.')[0]
    if r['code'].isdigit():
        objectives.append({
            'objective_id': f"OBJ-6116-{topic}",
            'parent_id': None,
            'topic_id': topic,
            'syllabus_text': f"{r['code']} {r['title']}",
            'learner_objective': r['title'],
            'level': 'NSSCO Ordinary Level',
            'route_status': 'core',
            'mandatory': True,
            'objective_type': 'bio_concept',
            'depth_tier': 4,
            'command_words': [],
            'assessment_objectives': [],
            'syllabus_page': r['source']['printed_page'],
            'status': 'planned',
            'prerequisite_ids': [],
            'related_ids': [],
            'papers': ['1', '2', '3'],
            'sub_topic': r['code'],
        })
        sidecar[f"OBJ-6116-{topic}"] = {'is_container': True, 'kind': 'topic',
                                        'syllabus_pdf_page': r['source']['pdf_page']}
        continue
    headings[r['code']] = {'title': r['title'], 'syllabus_pdf_page': r['source']['pdf_page']}
    expanded = []
    for o in r['specific_objectives']:
        dec = o.get('decomposition')
        if o.get('absorbed_by'):
            continue                      # registered as a member of its lead-in bullet
        if dec:
            for mem in dec['members']:
                # member wording is complete in planning/decomposition.json
                expanded.append({'text': mem, 'source': o['source'], '_container': False,
                                 '_from': o['text'], '_kind': dec['kind']})
        else:
            expanded.append({'text': o['text'], 'source': o['source'], '_container': False})

    for i, o in enumerate(expanded, start=1):
        txt = o['text']
        # AO from the syllabus's own descriptions (printed p.35-36), not from a
        # verb list. A is recall and understanding of content; B is handling
        # information and solving problems, which the syllabus says is tested on
        # unfamiliar material; C is the practical skills, assessed only on Paper 3.
        ot, ao, papers = classify(txt, r['code'])
        ov = override(txt)
        if ov:
            ot, ao = ov['type'], ov['aos']
            papers = ['3'] if ao == ['AO3'] else ['1', '2']
        tr = (ov or {}).get('tier') or tier(txt, False)
        objectives.append({
            'objective_id': f"OBJ-6116-{r['code']}-{i:02d}",
            'parent_id': f"OBJ-6116-{topic}",
            'topic_id': topic,
            'syllabus_text': txt,
            'learner_objective': txt[0].upper() + txt[1:] if txt else txt,
            'level': 'NSSCO Ordinary Level',
            'route_status': 'core',
            'mandatory': True,
            'objective_type': ot,
            'depth_tier': tr,
            'command_words': (ov['command_words'] if ov and 'command_words' in ov else sorted({w for w in
                ['define','state','name','list','describe','explain','outline','calculate','suggest',
                 'compare','distinguish','identify','draw','plot','measure','investigate','predict',
                 'discuss','label','complete','determine']
                if re.search(r'\b'+w+r'\b', txt, re.I)})),
            'assessment_objectives': ao,
            'syllabus_page': o['source']['printed_page'],
            'status': 'planned',
            'prerequisite_ids': [],
            'related_ids': [],
            'papers': papers,
            'sub_topic': r['code'],
        })
        sidecar[objectives[-1]['objective_id']] = {
            'is_container': False,
            'sub_topic_title': r['title'],
            'decomposed_from': o.get('_from'),
            'decomposition_kind': o.get('_kind'),
            'classification': ('override: ' + ov['why']) if ov else 'verb-first rule',
            'syllabus_pdf_page': o['source']['pdf_page']}

# teaching dependencies (planning/dependencies.json): prerequisite_ids on every objective of the
# dependent sub-topic, resolved by the prerequisite's opening words
DEP = json.load(open(f'{WS}/planning/dependencies.json'))['dependencies']
leaves = [o for o in objectives if o['parent_id']]
for d in DEP:
    pre = []
    for start in d['requires']:
        hit = [o['objective_id'] for o in leaves if o['syllabus_text'].startswith(start)]
        if not hit:
            raise SystemExit('dependency for %s: no objective starts "%s"' % (d['for'], start))
        pre.append(hit[0])
    for o in leaves:
        if o['sub_topic'] == d['for'] or o['sub_topic'].startswith(d['for'] + '.'):
            o['prerequisite_ids'] = sorted(set(o['prerequisite_ids']) | set(pre))
# related_ids: objectives that share a misconception pair or are split from one bullet stay linked
by_bullet = {}
for o in leaves:
    src = sidecar[o['objective_id']].get('decomposed_from')
    if src:
        by_bullet.setdefault(src, []).append(o['objective_id'])
for ids in by_bullet.values():
    for oid in ids:
        o = next(x for x in leaves if x['objective_id'] == oid)
        o['related_ids'] = sorted(set(ids) - {oid})

# schema sets additionalProperties:false at the top level too
out = {'registry_id': 'REG-6116-NSSCO-2026', 'objectives': objectives}
json.dump(out, open(f'{WS}/curriculum/objective_registry.json','w'), indent=2, ensure_ascii=False)
json.dump({'source': 'curriculum/syllabus-facts.json',
           'rule': ('Every syllabus objective is registered and mandatory. Measured exposure '
                    'calibrates emphasis; it never removes an objective.'),
           'objective_count': len(objectives),
           'note': 'Planning-only fields. The registry schema sets additionalProperties:false, '
                   'so these are kept beside it rather than inside it.',
           'sub_topic_headings': headings,
           'by_objective_id': sidecar},
          open(f'{WS}/curriculum/objective_registry.planning.json','w'), indent=2, ensure_ascii=False)
unused = sorted(set(OVR['overrides']) - _ovr_used)
if unused:
    raise SystemExit('objective_overrides.json entries match no objective: %s' % unused)
leaf=[o for o in objectives if not sidecar[o['objective_id']]['is_container']]
print(f"objectives: {len(objectives)} ({len(leaf)} assessable, {len(objectives)-len(leaf)} containers)")
print("by type:", dict(collections.Counter(o['objective_type'] for o in leaf)))
print("by depth_tier:", dict(collections.Counter(o['depth_tier'] for o in leaf)))
print("by AO:", dict(collections.Counter((o['assessment_objectives'] or ['-'])[0] for o in leaf)))
print("by topic:", dict(collections.Counter(o['topic_id'] for o in leaf)))
