"""Call the standard generator with a read-only projection for its legacy exposure reader.

Canonical measured metrics stay nested (C-39). No standard file is edited and no
stale top-level exposure fields are written to curriculum/exam-exposure.json.
"""
import importlib.util
import json
import sys
from review_fixes import ownership_for
from pathlib import Path
WS=Path(__file__).resolve().parents[1]
ROOT=WS.parents[1]
sys.path.insert(0,str(ROOT/'standard/v0.2.0-draft/build'))
import make_contract
from gates import require_prerequisites
require_prerequisites(str(WS))
original_reader=make_contract._json
def compatible_reader(path):
    data=original_reader(path)
    if str(path).endswith('curriculum/exam-exposure.json'):
        for entry in data['objectives']:
            ev=entry['evidence']; count=ev['distinct_series']
            entry.update(times_examined=ev['question_parts_naming_it'],marks_examined=ev['marks_examined'],
                         command_words=ev['command_words_observed'],
                         exposure_class='frequent' if count>=3 else 'occasional' if count==2 else 'rare' if count==1 else 'unseen')
    return data
make_contract._json=compatible_reader
written,skipped=make_contract.build(str(WS),force=True)
for tid in written:
    path=WS/'topics'/tid/'contract.json'
    data=json.loads(path.read_text())
    data['generated_by']='standard make_contract.build via planning/generate_contracts.py; nested-exposure input adapter'
    data['depth_constraints']['excluded_constructs_source']='Judgement boundaries from the NSSCO syllabus’s positive scope; no explicit syllabus prohibition was invented. See scope-scan.json provenance and manual constraints.'
    data['planning_notes']=['No standard tool was modified. Exposure projection is transient and recomputed from canonical nested metrics.',
                            'Overall AO targets are calculated 39/25.5/35.5; the standard generator labels the legacy field as stated.',
                            'Member exposure is not copied from its parent. Every specified member is taught regardless of zero direct frequency.']
    data['planning_notes'] += ownership_for(tid)
    data['depth_constraints']['adjacent_topics'] = ownership_for(tid)
    path.write_text(json.dumps(data,indent=2,ensure_ascii=False)+'\n')
print('Generated',len(written),'contracts; canonical nested exposure unchanged.')
