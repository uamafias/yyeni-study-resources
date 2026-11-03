"""Refresh derived presentation in the candidate bank, preserving every raw field.

Never operates on learner snapshots or historical review packets. Used when
only display conversion changes, avoiding an unrelated regeneration of maths.
"""
import argparse,json,sys,types
from pathlib import Path
API=Path(__file__).resolve().parents[1]
m=types.ModuleType('services');m.__path__=[str(API/'services')];sys.modules.setdefault('services',m)
from services.math_workbench.content_format import attach_display_content
from services.math_workbench.registry import grading_contract,generate_question

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--recipe',action='append',default=[]);args=parser.parse_args()
    path=API/'data/imports/nam-6131-nssco-2026/workbench-bank.json';bank=json.loads(path.read_text())
    for card in bank['recipe_cards']:
        q=card['question_snapshot']
        if card['recipe_id'] in args.recipe:
            assert card['source_kind']=='new_generator','Retained source repairs require the full bank builder'
            q=generate_question(card['recipe_id'],card['generator_params']['seed'],version=card['generator_params']['recipe_version'])
            assert q['objective_ids']==card['objective_ids']
            card['question_snapshot']=q
        attach_display_content(q);q['grading_contract']=grading_contract(q)
        card['contract_hash']=q['grading_contract']['contract_hash']
    path.write_text(json.dumps(bank,separators=(',',':'),ensure_ascii=False)+'\n')
    print('Refreshed derived presentation for',len(bank['recipe_cards']),'candidate cards')
if __name__=='__main__':main()
