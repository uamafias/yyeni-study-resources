"""Read-only operation scan; output stays under checks/r5,never analysis/."""
import json,os,sys
from pathlib import Path
WB=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(WB/'tools'))
from verify_textbook_answers_r5 import compute
rows=[]
for path in sorted((WB/'tools/textbook-r5').glob('answers-*.json')):
    for item in json.loads(path.read_text())['items']:
        for part in item['subparts']:
            for name,operation in [('main',part.get('operation',{})),*part.get('additional_operations',{}).items()]:
                if operation.get('kind')!='real-elementary-antiderivative':continue
                rows.append(dict(item_id=item['item_id'],subpart=part['subpart'],operation_name=name,
                    input_file=path.name,operation=operation,result=str(compute(operation))))
target=WB/f'checks/r5/primitive-seed-{os.environ["PYTHONHASHSEED"]}.json'
target.write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n')
print(len(rows),'primitive representations checked;',target.name)
