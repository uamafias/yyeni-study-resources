"""Render with the unchanged standard, then order sections by their syllabus numbers.
The generic renderer ranks cross-mapped units by their earliest linked objective,
which can put a later Chemistry section near the front.
"""
import re,sys
from pathlib import Path
W=Path(__file__).resolve().parents[1];R=W.parents[1]
sys.path.insert(0,str(R/'standard/v0.2.0-draft/build'))
import render_notes
from naming import notes_filename
import json
for t in map(str,range(1,13)):
 td=W/'topics'/t;contract=json.loads((td/'contract.json').read_text())
 text=render_notes.render(str(W),t)
 text=re.sub(r'^\*.*Offline study notes.*\*$', '*NSSCO Chemistry 6117 — study notes. Worked examples teach methods; assessment tasks are supplied separately.*',text,flags=re.M)
 matches=list(re.finditer(r'^## (\d+(?:\.\d+)*)\s[^\n]*$',text,re.M))
 if matches:
  sections=[(tuple(map(int,m.group(1).split('.'))),text[m.start():matches[i+1].start() if i+1<len(matches) else len(text)]) for i,m in enumerate(matches)]
  text=text[:matches[0].start()]+''.join(s for _,s in sorted(sections,key=lambda p:p[0]))
 out=td/notes_filename(t,contract['topic_title']);out.write_text(text)
 print(t,out.name)
