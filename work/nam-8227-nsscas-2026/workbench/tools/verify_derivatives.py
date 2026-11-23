"""Recompute existing layout-text derivatives from read-only PDFs. No web access."""
import json
import argparse
import hashlib
import platform
import subprocess
from importlib.metadata import version
from pypdf import PdfReader
from analysis_sources import A, ROOT, WB, digest, write

def main():
 parser=argparse.ArgumentParser(description=__doc__)
 parser.add_argument('--rebuild-layout',action='store_true',help='Regenerate frozen layout derivatives only when all bytes match the manifest')
 args=parser.parse_args()
 results=[]
 for entry in json.loads((WB/'tools/layout_source_inputs.json').read_text()):
  path=ROOT/entry['target'];source=ROOT/entry['source']
  assert digest(source)==entry['source_sha256'],path
  reader=PdfReader(source)
  rebuilt={'source':entry['source'],'sha256':entry['source_sha256'],
    'pages':[{'pdf_page':n,'text':page.extract_text(extraction_mode='layout')} for n,page in enumerate(reader.pages,1)]}
  payload=(json.dumps(rebuilt,ensure_ascii=False,indent=2)+'\n').encode()
  assert hashlib.sha256(payload).hexdigest()==entry['expected_derivative_sha256'],(path,'recomputed derivative bytes differ')
  if args.rebuild_layout:path.write_bytes(payload)
  assert path.read_bytes()==payload,(path,'saved derivative differs')
  results.append({'path':str(path.relative_to(ROOT)),'sha256':digest(path),'source_path':entry['source'],
    'source_sha256':entry['source_sha256'],'pages_recomputed':len(reader.pages),'status':'all serialized derivative bytes identical'})
 meta=json.loads((A/'ocr/ymxc/metadata.json').read_text())
 ocr=[]
 for n in range(1,664):
  path=A/'ocr/ymxc'/f'page-{n:04d}.json';d=json.loads(path.read_text())
  assert d['source_sha256']==meta['source_sha256'] and d['pdf_page']==n
  ocr.append({'path':str(path.relative_to(ROOT)),'sha256':digest(path)})
 env={'python':platform.python_version(),'macos':platform.mac_ver()[0],
   'macos_build':subprocess.check_output(['sw_vers','-buildVersion'],text=True).strip(),
   'dependencies':{n:version(n) for n in ['pypdf','PyMuPDF','Pillow','sympy']}}
 write(WB/'checks/derivative-verification.json',{'environment':env,'layout_derivatives':results,'ocr_page_records':ocr,
   'ocr_reproduction_limit':'Existing 663 OCR pages/hash settings verified; original run did not record macOS build or per-page settings. This repair does not retrofit that evidence or claim OCR byte reproducibility across Vision versions.',
   'current_ocr_settings':meta,'source_originals_modified':False})
 print(json.dumps({'layout_files':len(results),'layout_pages':sum(x['pages_recomputed'] for x in results),'ocr_pages':len(ocr),'environment':env},indent=2))
if __name__=='__main__':main()
