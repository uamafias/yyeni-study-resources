"""OCR report pages containing images; retain OCR as unverified internal aid."""
from pathlib import Path
from collections import defaultdict
import concurrent.futures,json,subprocess,tempfile

ROOT=Path(__file__).resolve().parents[3];WORK=ROOT/'work/nam-6118-nssco-2026'


def run(job):
    year,path,page=job
    with tempfile.TemporaryDirectory(prefix='6118-report-ocr-') as d:
        target=Path(d)/'page'
        subprocess.run(['pdftoppm','-f',str(page),'-l',str(page),'-r','220','-singlefile','-png',str(ROOT/path),str(target)],check=True)
        text=subprocess.run(['tesseract',str(target)+'.png','stdout','--psm','3'],text=True,capture_output=True,check=True).stdout
        return year,page,text


def main():
    inv=json.loads((WORK/'curriculum/source-inventory.json').read_text())
    jobs=[]
    for source in inv['entries']:
        if source['kind']!='combined_examiner_report' or source['year']==2020:continue
        r=source['physics_pdf_pages']
        image_list=subprocess.check_output(['pdfimages','-f',str(r['first']),'-l',str(r['last']),'-list',str(ROOT/source['path'])],text=True)
        pages=sorted({int(line.split()[0]) for line in image_list.splitlines()[2:] if line.split() and line.split()[0].isdigit()})
        jobs.extend((source['year'],source['path'],page) for page in pages)
    output=defaultdict(list)
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:
        for year,page,text in pool.map(run,jobs):output[year].append((page,text))
    for year,pages in output.items():
        path=WORK/f'planning/extracted/{year}-report.ocr-draft.txt'
        path.write_text('\n\n'.join(f'=== SOURCE PDF PAGE {page}; OCR DRAFT, VERIFY IMAGE ===\n{text}' for page,text in sorted(pages)))
        print(year, len(pages),'image pages OCRed',flush=True)


if __name__=='__main__':main()
