"""Recover embedded image-based memo tables; OCR is an internal draft aid."""
from pathlib import Path
import concurrent.futures
import subprocess
import tempfile

ROOT=Path(__file__).resolve().parents[3]
WORK=ROOT/'work/nam-6118-nssco-2026'
PDF=ROOT/'Question Banks/Namibian Examiner Reports/NSSCO (New) /2020/NSSCO(New) Examiners Report 2020 (1).pdf'


def page(number):
    with tempfile.TemporaryDirectory(prefix=f'6118-ocr-{number}-') as temp:
        prefix=Path(temp)/'page'
        subprocess.run(['pdftoppm','-f',str(number),'-l',str(number),'-r','220','-singlefile','-png',str(PDF),str(prefix)],check=True)
        result=subprocess.run(['tesseract',str(prefix)+'.png','stdout','--psm','3'],text=True,capture_output=True,check=True)
        return number,result.stdout


def main():
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:
        pages=list(pool.map(page,range(467,478)))
    dest=WORK/'planning/extracted/2020-report.ocr-draft.txt'
    dest.write_text('\n\n'.join(f'=== SOURCE PDF PAGE {number}; OCR DRAFT, VERIFY IMAGE ===\n{text}' for number,text in pages))
    print(f'OCR complete: {len(pages)} pages; image verification required before accepting numerical/memo rows.')


if __name__=='__main__':main()
