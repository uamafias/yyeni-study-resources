"""Use the unchanged shared publisher, then carry its referenced original PNG assets.

Learner text and authored hashes remain byte-identical: preserve diagrams/ paths
in both notes/ and flashcards/ rather than rewriting canonical answers.
"""
from pathlib import Path
import hashlib,json,re,shutil,subprocess,sys
W=Path(__file__).resolve().parents[1];R=W.parents[1];OUT=R/'publish'/W.name
for q in (W/'topics').glob('*/qa_report.json'):
 report=json.loads(q.read_text());assert report['release_decision']=='publish' and not any(c['status']=='fail' for c in report['deterministic_checks']),q
subprocess.run([sys.executable,str(R/'standard/v0.2.0-draft/build/publish_subject.py'),str(W)],check=True,cwd=R)
assets={}
for p in (W/'topics').glob('*/diagrams/*.png'):
 if p.name in assets:assert p.read_bytes()==assets[p.name].read_bytes(),p.name
 assets[p.name]=p
copies=[]
for folder in ['notes','flashcards']:
 for name,p in assets.items():
  target=OUT/folder/'diagrams'/name;target.parent.mkdir(exist_ok=True);shutil.copyfile(p,target)
  copies.append({'path':str(target.relative_to(OUT)),'source':str(p.relative_to(R)),'sha256':hashlib.sha256(target.read_bytes()).hexdigest()})
# Check actual references, including the JSON answers, from each containing folder.
refs=[]
for folder,pattern in [('notes','*.md'),('flashcards','*.json')]:
 for p in (OUT/folder).glob(pattern):
  for link in re.findall(r'!?\[[^\]]*\]\((diagrams/[^)]+)\)',p.read_text()):
   assert (p.parent/link).exists(),(p,link)
   refs.append({'file':str(p.relative_to(OUT)),'link':link})
manifest=json.loads((OUT/'MANIFEST.json').read_text());assert manifest['totals']['topics']==22 and manifest['totals']['items']==562 and not manifest['not_published']
items=[i for p in (OUT/'flashcards').glob('*.json') for i in json.loads(p.read_text())['items']]
assert sum(i['item_type']=='flashcard' for i in items)==474 and len(items)==562
mis=[i['misconception_entry'] for i in items if i.get('subtype')=='MISCON'];assert len(mis)==47 and len(set(mis))==47
(W/'publication-verification.json').write_text(json.dumps({'topics':22,'items':562,'flashcards':474,'practice_packages':88,'misconceptions_once_each':47,'image_assets':len(assets),'asset_copies':len(copies),'resolved_image_references':len(refs),'rendered_notes_words':manifest['totals']['notes_words'],'status':'Local package generated; independent review and platform import pending.','unresolved_image_links':0},indent=2)+'\n')
(OUT/'ASSET-MANIFEST.json').write_text(json.dumps({'generated_by':str(Path(__file__).relative_to(R)),'assets':copies,'references':refs},indent=2)+'\n')
print('Publication reconciled: 22 topics, 474 flashcards, 88 packages, 47 distinct misconception slots; all diagram references resolve.')
