#!/usr/bin/env python3
"""Write curriculum/visual-requirements.json: every objective that cannot be taught or tested in words alone.

The syllabus asks learners to identify structures from photomicrographs, slides, drawings and
diagrams, to interpret sections, and to produce biological drawings. A verbal description cannot
show whether a learner recognises an unfamiliar micrograph or draws the right spatial arrangement.

Asset preparation is supported separately from the shared build: extract, source or create
assets in visuals/ and keep proposed objective/card/notes/activity bindings. The shared build
does not automatically verify or package the bank. YYeni image display and learner drawing
submission remain unproven/unavailable until demonstrated. Acquisition is not review or delivery.

Kinds:
  stimulus_image    an image the learner must read: a photomicrograph, slide or diagram to identify from
  teaching_diagram  a labelled diagram the notes need to teach a structure
  model_drawing     a model labelled drawing beside the drawing criteria, for a drawing task
  graph             a graph to read or plot, generated from declared data alongside its table
"""
import json, re

WS = 'work/nam-6116-nssco-2026'
reg = [o for o in json.load(open(f'{WS}/curriculum/objective_registry.json'))['objectives'] if o.get('parent_id')]

STIM = re.compile(r'photomicrograph|images?\b|prepared slides?|slides? of|under (?:a|the) light microscope|'
                  r'from diagrams|in diagrams|on drawings|diagrams of|from drawings|seen in cross|transverse section', re.I)
DRAW = re.compile(r'\bdraw\b|make a clear, labelled line drawing', re.I)
GRAPH = re.compile(r'\b(?:graphs?|curves?|charts?|pyramids?|histograms?)\b', re.I)
STRUCT = re.compile(r'\b(?:structure|parts of|identify the (?:cornea|iris|pupil|lens|retina|optic|blind)|'
                    r'alimentary canal|reproductive system|heart|villus|villi|neurones|reflex arc|flowers?|root|stem|'
                    r'leaf|DNA|kidney|ureter|endocrine glands|adrenal|pancreas|testes|ovaries|placenta|spinal cord)\b',
                    re.I)
# Objectives the notes cannot teach well without a labelled diagram, though their wording names no image.
DIAGRAM_ALSO = ('describe the functions of the various parts of the alimentary canal', 'describe a simple reflex arc',
                'describe the double circulatory system', 'describe the function of the placenta',
                'describe the heart in terms of', 'state the functions of the internal and external intercostal',
                'describe how nerve impulses are transmitted across the synapse', 'describe the nitrogen cycle',
                'describe the role of photosynthesis in the carbon cycle', 'explain accommodation to view near')
SUPPLY = {
 'stimulus_image': 'an existing local-corpus candidate or an original/file-specifically licensed photomicrograph or diagram, inventoried in visuals/manifest.json with source, creator and rights; an independently reviewed unfamiliar example for testing, not the labelled image used to teach',
 'teaching_diagram': 'an original labelled line diagram (SVG) or an openly licensed one, labels in the syllabus terms',
 'model_drawing': 'an original model drawing (SVG) of the specimen used in the task, with the drawing criteria (clear continuous lines, no shading, correct proportions, ruled label lines, magnification where asked)',
 'graph': 'a reproducible original SVG/PNG graph from declared data plus its table; a table alone supports plotting practice but does not fulfil an image-interpretation stimulus',
}
# Judgement additions, each with its reason (planning/visual_requirement_additions.json): needs the
# wording rules cannot see, including the seven Codex added on 2026-10-18 (reviewed and kept).
ADD = json.load(open(f'{WS}/planning/visual_requirement_additions.json'))['additions']
EXTRA, WHY = {}, {}
for a in ADD:
    hits = [o['objective_id'] for o in reg if o['syllabus_text'].startswith(a['objective_starts'])]
    if not hits or (len(hits) > 1 and not a.get('all_matches')):
        raise SystemExit('visual addition "%s" matched %d objectives' % (a['objective_starts'], len(hits)))
    for h in hits:
        EXTRA.setdefault(h, []).extend(a['kinds'])
        WHY.setdefault(h, []).append(a['reason'])
# What each kind needs before the requirement is met. A found image is none of these by itself.
NEEDS = {
 'stimulus_image': ['teaching variant (labelled with syllabus terms)', 'question variant (no labels, or neutral letters)',
                    'answer variant (the question image with the correct labels)',
                    'unfamiliar example (a different specimen from the teaching image, for recognition practice)'],
 'teaching_diagram': ['teaching variant (labelled with syllabus terms; every structure the objective names)'],
 'model_drawing': ['model drawing of the specimen the task uses (original line drawing)', 'the drawing criteria it meets'],
 'graph': ['question variant (data or graph to read, no answer marked)', 'answer variant (the reading, plot or trend marked)'],
}
CHECK = ('a Biology teacher confirms that the structure shown is correct, the labels use the syllabus terms and point to '
         'the right part, the image is legible at phone size, and the licence permits use; recorded with name and date')
out = []
for o in reg:
    t = o['syllabus_text']; kinds = []
    if STIM.search(t): kinds.append('stimulus_image')
    if DRAW.search(t) and not re.search(r'draw (?:an )?appropriate conclusion|draw appropriate conclusions', t, re.I):
        kinds.append('model_drawing' if not GRAPH.search(t) else 'graph')
    if GRAPH.search(t) and 'graph' not in kinds: kinds.append('graph')
    if o['objective_type'] in ('bio_structure', 'task_drawing', 'task_drawing_interp') or (
            STRUCT.search(t) and re.match(r'^(identify|describe the structure|outline how the structure|name|draw)', t, re.I)) or \
            t.startswith(DIAGRAM_ALSO):
        kinds.append('teaching_diagram')
    kinds = sorted(set(kinds + EXTRA.get(o['objective_id'], [])))
    if not kinds:
        continue
    # stable: derived from the objective, so adding a requirement never renumbers the others
    out.append({'requirement_id': 'VIS-' + o['objective_id'][len('OBJ-'):], 'objective_id': o['objective_id'],
                'objective': t, 'kinds': kinds,
                'needs': {k: NEEDS[k] for k in kinds},
                'added_by_judgement': WHY.get(o['objective_id'], []),
                'supply': {k: SUPPLY[k] for k in kinds},
                'status': {k: 'PENDING: select/create asset, review and bind it; asset creation is supported outside the shared build'
                           for k in kinds},
                'acceptance_check': CHECK})
summary = {k: sum(1 for x in out if k in x['kinds']) for k in SUPPLY}
unresolved = len(out)
json.dump({'generated_by': f'{WS}/planning/build_visual_requirements.py', 'capability_status': 'ASSET PREPARATION SUPPORTED; SHARED-BUILD INTEGRATION AND YYENI DISPLAY PENDING',
           'rule': 'Existing visuals can be extracted or sourced now and graphs generated separately, as in Economics. Store candidates and source/rights records in visuals/; bind to objective, card side, notes and activity. Neither collecting a candidate nor passing a text-only check fulfils visual coverage. YYeni card-image display and learner drawing submission remain unavailable until demonstrated.', 'objectives_needing_visuals': len(out),
           'objectives_with_unresolved_visuals': unresolved, 'by_kind': summary,
           'authoring_rule': ('Prepare the visual bank during planning; full authoring remains unapproved. Once authoring is approved, an item that cannot be answered without an image names its '
                              'figure in the prompt as "Fig. <requirement_id>" and is listed in topics/<T>/authoring_notes.json '
                              'under visuals_pending; it is not released to learners until the figure exists and has passed '
                              'the acceptance check. Never replace a required image with a verbal description and call the '
                              'objective covered.'),
           'requirements': out}, open(f'{WS}/curriculum/visual-requirements.json', 'w'), indent=2, ensure_ascii=False)
print('%d objectives need visuals (%d unresolved); by kind %s' % (len(out), unresolved, summary))
