"""Instance-bound maths marking snapshots, separate from final-answer checking.

The hash detects accidental mismatches; it is not an authentication signature.
Snapshots must come from trusted server-side generation, never learner input.
No DB or provider work happens here. Prepared graph references verify bundled bytes.
"""
from __future__ import annotations

from copy import deepcopy
import hashlib
import json

from .nssco_guidance import resolve

CONTRACT_VERSION = 'nssco-exam-guidance-v1'
MEMO_PREFIX = 'YYENI_MATH_GRADING_CONTRACT_V1\n'


class InvalidMarkingContract(ValueError):
    pass


def _digest(value):
    try:
        payload = json.dumps({k:v for k,v in value.items() if k != 'contract_hash'},
                             sort_keys=True, ensure_ascii=False, allow_nan=False,
                             separators=(',',':'))
    except (TypeError,ValueError,AttributeError,RecursionError) as exc:
        raise InvalidMarkingContract('Contract must contain only finite JSON data') from exc
    return hashlib.sha256(payload.encode('utf-8')).hexdigest()


def build_contract(problem):
    """Freeze this instance's proposed memo and awards, not a sample's numbers."""
    guidance = resolve(problem)
    contract = {
        'contract_version':CONTRACT_VERSION,
        'guidance_status':guidance['status'],
        'tariff_status':guidance['tariff_status'],
        'generator_id':problem.generator_id, 'generator_version':problem.generator_version,
        'seed':problem.seed, 'level':problem.level, 'skill':problem.skill,
        'question':problem.question, 'canonical_answer':problem.answer,
        'question_fingerprint':problem.fingerprint,
        'marks':guidance['marks'],
        'grading_guide_answer':guidance['grading_guide_answer'],
        'creditworthy_points':deepcopy(guidance['creditworthy_points']),
        'criteria':[{'criterion_id':f'c{i}', 'criterion':a['achievement'],
                     'marks_available':a['marks']} for i,a in enumerate(guidance['awards'],1)],
        'source_ids':list(guidance['sources']),
        'evidence_relation':guidance['evidence_relation'],
        'review_reason':guidance['review_reason'],
    }
    from ..math_generators.graph_bank import problem_references
    refs = problem_references(problem)
    if refs:
        contract['reference_images'] = refs
    contract['contract_hash'] = _digest(contract)
    validate_contract(contract, problem=problem)
    return contract


def validate_contract(value, *, question=None, max_marks=None, problem=None):
    """Raise on an invalid trusted snapshot before any provider call."""
    if not isinstance(value,dict) or value.get('contract_version') != CONTRACT_VERSION:
        raise InvalidMarkingContract('Unsupported marking contract')
    if value.get('contract_hash') != _digest(value):
        raise InvalidMarkingContract('Marking contract hash mismatch')
    for key in ('generator_id','skill','question','canonical_answer','grading_guide_answer',
                'guidance_status','tariff_status','evidence_relation','review_reason'):
        if not isinstance(value.get(key),str) or not value[key].strip():
            raise InvalidMarkingContract(f'Missing contract text: {key}')
    for key in ('generator_version','seed','level'):
        if type(value.get(key)) is not int or value[key] < (0 if key=='seed' else 1):
            raise InvalidMarkingContract(f'Invalid {key}')
    maximum = value.get('marks')
    if type(maximum) is not int or maximum < 1:
        raise InvalidMarkingContract('A maths tariff must be a positive whole number')
    criteria = value.get('criteria')
    if not isinstance(criteria,list) or not criteria:
        raise InvalidMarkingContract('Missing award criteria')
    ids = set(); total = 0
    for row in criteria:
        if not isinstance(row,dict): raise InvalidMarkingContract('Invalid award criterion')
        cid = row.get('criterion_id')
        if not isinstance(cid,str) or not cid.strip() or cid in ids:
            raise InvalidMarkingContract('Missing or duplicate criterion id')
        ids.add(cid)
        if not isinstance(row.get('criterion'),str) or not row['criterion'].strip():
            raise InvalidMarkingContract('Missing criterion achievement')
        if type(row.get('marks_available')) is not int or row['marks_available'] < 1:
            raise InvalidMarkingContract('Invalid criterion maximum')
        total += row['marks_available']
    if total != maximum: raise InvalidMarkingContract('Criteria do not sum to contract maximum')
    for key in ('source_ids','creditworthy_points'):
        if not isinstance(value.get(key),list) or not value[key] or any(not isinstance(s,str) or not s.strip() for s in value[key]):
            raise InvalidMarkingContract(f'Missing {key}')
    refs = value.get('reference_images', {})
    if not isinstance(refs,dict) or (refs and (set(refs) != {'question','answer'} or any(not isinstance(v,str) for v in refs.values()))):
        raise InvalidMarkingContract('Invalid reference images')
    from ..math_generators.base import visible_question_fingerprint
    fingerprint = visible_question_fingerprint(value['question'], refs.get('question'))
    if value.get('question_fingerprint') != fingerprint:
        raise InvalidMarkingContract('Question fingerprint mismatch')
    if question is not None and value['question'] != question:
        raise InvalidMarkingContract('Snapshot question differs from marking contract')
    if max_marks is not None:
        from .numeric import finite_number
        if finite_number(max_marks) != maximum:
            raise InvalidMarkingContract('Snapshot maximum differs from marking contract')
    if problem is not None:
        bindings = {'generator_id':problem.generator_id,'generator_version':problem.generator_version,
                    'seed':problem.seed,'level':problem.level,'skill':problem.skill,
                    'question':problem.question,'canonical_answer':problem.answer}
        if any(value.get(k)!=v for k,v in bindings.items()):
            raise InvalidMarkingContract('Generated instance differs from marking contract')
    from ..math_generators.graph_bank import validate_references
    try:
        validate_references(value)
    except (ValueError, OSError, KeyError, TypeError) as exc:
        raise InvalidMarkingContract('Prepared reference images unavailable or mismatched') from exc
    return deepcopy(value)


def dump_contract_memo(contract):
    return MEMO_PREFIX+json.dumps(validate_contract(contract),ensure_ascii=False,allow_nan=False)


def load_contract_memo(memo, *, question, max_marks):
    """Ordinary memos return None; malformed/unknown contract memos fail closed."""
    if not isinstance(memo,str):
        return None
    memo = memo.strip()
    if not memo.startswith('YYENI_MATH_GRADING_CONTRACT_'):
        return None
    if not memo.startswith(MEMO_PREFIX): raise InvalidMarkingContract('Unknown contract memo version')
    try:
        value = json.loads(memo[len(MEMO_PREFIX):])
    except (TypeError,ValueError,RecursionError) as exc:
        raise InvalidMarkingContract('Unreadable contract memo') from exc
    return validate_contract(value,question=question,max_marks=max_marks)
