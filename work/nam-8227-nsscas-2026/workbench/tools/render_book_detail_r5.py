"""High-resolution local textbook evidence; no PDF edits."""
import json,subprocess,sys
from PIL import Image
from analysis_sources import A,WB,ROOT,digest,write

def render(book,page,name,box,output_directory=None):
    src=next(s for s in json.loads((A/'textbook-inventory.json').read_text())['books']if(s['document_id']=='8227-SRC-015')==(book=='Goldie'))
    swift=WB/'tools/render_pdf_detail_r5.swift';cache=WB/'checks/r5/scale4';binary=cache/('render-'+digest(swift)[:12]);cache.mkdir(exist_ok=True)
    if not binary.exists():subprocess.run(['swiftc',str(swift),'-o',str(binary)],check=True,capture_output=True)
    directory=cache/src['sha256'][:16];target=directory/f'page-{page:04}.png'
    if not target.exists():subprocess.run([str(binary),str(ROOT/src['path']),str(directory),str(page)],check=True,capture_output=True)
    dest=(output_directory or WB/'checks/r5/textbooks')/(name+'.png');dest.parent.mkdir(parents=True,exist_ok=True)
    with Image.open(target)as image:image.crop(tuple(round(v*4)for v in box)).save(dest)
    result={'source_path':src['path'],'source_sha256':src['sha256'],'pdf_page':page,'printed_page':page-14 if book=='Goldie'else page-11 if page<=138 else page-12,'path':str(dest.relative_to(ROOT)),'sha256':digest(dest),'render_scale':4,'crop_box_pdf_points':box,'inspection':'pending; rendering is not reading'}
    write(dest.with_suffix('.json'),result);print(result['path'])
if __name__=='__main__':render(sys.argv[1],int(sys.argv[2]),sys.argv[3],list(map(float,sys.argv[4:])))
