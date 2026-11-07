"""Compatibility provider for the original NSSCO Maths recipes.

The application owns assignment/renewal, grading calls and saved learner data.
This provider owns generation and immutable canonical marking evidence.
"""
from copy import deepcopy
import hashlib
import json
from pathlib import Path

from .services.api.services.math_workbench.registry import generate_question, validate_question, grading_contract

ROOT = Path(__file__).resolve().parent


class MathsProvider:
    def __init__(self):
        self.rows = json.loads((ROOT / 'provider-catalogue.json').read_text())
        self.by_key = {row['id']: row for row in self.rows}

    def describe(self):
        return {'package_id': 'namibia-nssco-6131', 'version': '1.0.1'}

    def list_recipes(self):
        return deepcopy(self.rows)

    def generate(self, key, recipe_version, seed):
        row = self.by_key[key]
        question = generate_question(row['recipeId'], seed, version=recipe_version)
        # Selection demands such as HCF/LCM share one historical generator.
        # The caller handles a nonmatching branch by choosing another seed.
        if row.get('task') is not None and question.get('source_branch', {}).get('task') != row['task']:
            raise ValueError('Seed produces another selection branch')
        from .services.api.services.math_workbench.practice_hints import help_for
        question['pilot_key'] = key
        question['practice_help'] = help_for(question)
        if not question['grading_contract'].get('source_marking_contract'):
            # Adapt the native authored memo; preserve the original contract/hash.
            rules = json.loads((ROOT / 'provider-rules.json').read_text())
            parts = question['parts']
            memo = {'contract_version': 'workbench-exam-guidance-v1',
                    'package_id': self.describe()['package_id'],
                    'recipe_id': question['recipe_id'], 'recipe_version': recipe_version,
                    'question': question['stem']+'\n\n'+'\n\n'.join(p['prompt'] for p in parts),
                    'canonical_answer': '\n\n'.join(chr(97+i)+') '+p['reference_answer'] for i,p in enumerate(parts)),
                    'grading_guide_answer': json.dumps(question['grading_contract'], ensure_ascii=False),
                    'subject_rules': rules, 'marks': question['proposed_total_marks'],
                    'criteria': [{'criterion_id': f'{chr(97+i)}.{j+1}',
                                  'criterion': c['achievement'], 'marks_available': c['marks']}
                                 for i,p in enumerate(parts) for j,c in enumerate(p['criteria'])]}
            memo['contract_hash'] = hashlib.sha256(json.dumps(memo,sort_keys=True,ensure_ascii=False,
                allow_nan=False,separators=(',',':')).encode()).hexdigest()
            question['marking_memo'] = memo
        return question

    def validate_instance(self, instance):
        try:
            validate_question(instance)
            if grading_contract(instance)['contract_hash'] != instance['grading_contract']['contract_hash']:
                return {'valid': False, 'reason': 'marking evidence differs'}
        except (AssertionError, KeyError, TypeError, ValueError):
            return {'valid': False, 'reason': 'question validation failed'}
        return {'valid': True}

    def resolve_asset(self, asset_id, digest, role):
        from .services.api.services.math_generators.graph_bank import read_asset
        data = read_asset(asset_id)
        if hashlib.sha256(data).hexdigest() != digest:
            raise ValueError('Asset digest differs')
        if asset_id.startswith('yyeni-graph:'):
            from .services.api.services.math_generators.graph_bank import entries, reference
            for row in entries():
                source_role = 'question' if role == 'question' else 'answer'
                if reference(row, source_role) == asset_id:
                    return 'services/api/data/flashcard_graphs/v1/' + row['assets'][source_role]['filename']
            raise ValueError('Asset role differs from reference')
        if asset_id == 'yyeni-diagram:v1:' + digest:
            return 'services/api/data/flashcard_diagrams/v1/' + digest + '.png'
        raise ValueError('Unknown asset identity')


def create_provider():
    return MathsProvider()
