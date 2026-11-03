"""Trusted, versioned PNG references for the bounded prepared-graph pilot.

Short references fit existing image columns. Only authorised payload builders
expand them to inline PNGs; there is no public asset/solution download endpoint.
Retain all old manifests and bytes for historical attempts.
"""
import base64
import hashlib
import json
from pathlib import Path

GENERATOR_ID = 'nssco_prepared_line_graphs'
ROOT = Path(__file__).resolve().parents[2] / 'data' / 'flashcard_graphs' / 'v1'
PREFIX = 'yyeni-graph:v1:'


def entries():
    return json.loads((ROOT / 'manifest.json').read_text())


def reference(entry, role):
    return f"{PREFIX}{entry['id']}:{role}:{entry['assets'][role]['sha256']}"


def references(entry):
    return {role: reference(entry, role) for role in ('question', 'answer')}


def read_asset(value):
    if isinstance(value,str) and value.startswith('yyeni-diagram:'):
        from .prepared_visual_bank import read_asset as read_diagram
        return read_diagram(value)
    if not isinstance(value, str) or not value.startswith(PREFIX):
        raise ValueError('Unknown prepared graph reference')
    parts = value[len(PREFIX):].split(':')
    if len(parts) != 3 or parts[1] not in ('question', 'answer'):
        raise ValueError('Invalid prepared graph reference')
    ident, role, digest = parts
    entry = next((e for e in entries() if e['id'] == ident), None)
    if entry is None or reference(entry, role) != value:
        raise ValueError('Prepared graph identity mismatch')
    asset = entry['assets'][role]
    filename = asset['filename']
    if Path(filename).name != filename:
        raise ValueError('Invalid prepared graph path')
    data = (ROOT / filename).read_bytes()
    if not data.startswith(b'\x89PNG\r\n\x1a\n') or hashlib.sha256(data).hexdigest() != digest:
        raise ValueError('Prepared graph bytes differ from saved reference')
    return data


def display_image(value):
    if isinstance(value, str) and value.startswith(('yyeni-graph:', 'yyeni-diagram:')):
        return 'data:image/png;base64,' + base64.b64encode(read_asset(value)).decode('ascii')
    return value


def problem_references(problem):
    if problem.generator_id != GENERATOR_ID and not problem.generator_id.startswith('nssco_visual_'):
        return {}
    refs = dict(problem.machine.get('reference_images', {}))
    for value in refs.values(): read_asset(value)
    return refs


def validate_references(contract):
    """Bind assets to the trusted seed's exact instance, not just a valid PNG."""
    if contract.get('generator_id') != GENERATOR_ID and not str(contract.get('generator_id','')).startswith('nssco_visual_'):
        if contract.get('reference_images'):
            raise ValueError('Unexpected prepared references')
        return {}
    from . import generate_problem
    problem = generate_problem(contract['generator_id'], contract['seed'], contract['level'])
    if contract.get('generator_id')=='nssco_visual_linear_programming' and contract.get('generator_version')==1:
        # Historical v1 contracts bind to the immutable prepared row, not the
        # corrected v2 prose. Never rewrite a learner's saved reference.
        from dataclasses import replace
        from .prepared_visual_bank import catalog
        rows=catalog()[problem.generator_id]['levels'][str(problem.level)]
        original=rows[problem.seed%len(rows)]
        problem=replace(problem,answer=original['answer'],generator_version=1)
    expected = problem_references(problem)
    if contract.get('reference_images') != expected or contract['question'] != problem.question or contract['canonical_answer'] != problem.answer:
        raise ValueError('Prepared graph does not match the saved instance')
    return expected


def prepared_reference_images(contract):
    from media.prepare_images import PreparedImage
    refs = validate_references(contract)
    return [PreparedImage(base64.b64encode(read_asset(refs[role])).decode('ascii'),
                          'image/png', f'reference-{role}', False)
            for role in ('question', 'answer')] if refs else []


def teaching(problem):
    if problem.generator_id != GENERATOR_ID and not problem.generator_id.startswith('nssco_visual_'):
        return None
    return problem.answer, problem.machine['explanation']
