"""Compare every local/publisher syllabus page at a fixed raster resolution.

The publisher PDF must be supplied from the recorded retrieval. Both PDFs remain
untouched; rendered intermediates are temporary. This tests current page images,
not historical validity, accessibility structure or interactive PDF behaviour.
"""
from pathlib import Path
import datetime
import hashlib
import json
import subprocess
import sys
import tempfile
from PIL import Image, ImageChops

ROOT=Path(__file__).resolve().parents[3]
WORK=ROOT/'work/nam-6118-nssco-2026'


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    publisher=Path(sys.argv[1]).resolve()
    currency=json.loads((WORK/'curriculum/syllabus-currency.json').read_text())
    local=ROOT/currency['local_pdf']
    assert sha(local)==currency['local_sha256']
    assert sha(publisher)==currency['official_sha256']
    results=[]
    with tempfile.TemporaryDirectory(prefix='6118-page-comparison-') as temp:
        directory=Path(temp)
        for name,pdf in [('local',local),('publisher',publisher)]:
            subprocess.run(['pdftoppm','-r','144','-png',str(pdf),str(directory/name)],check=True)
        local_pages=sorted(directory.glob('local-*.png'))
        publisher_pages=sorted(directory.glob('publisher-*.png'))
        assert len(local_pages)==len(publisher_pages)==52
        for left,right in zip(local_pages,publisher_pages):
            number=int(left.stem.rsplit('-',1)[1])
            assert number==int(right.stem.rsplit('-',1)[1])
            with Image.open(left) as a,Image.open(right) as b:
                a=a.convert('RGB');b=b.convert('RGB')
                assert a.size==b.size,(number,a.size,b.size)
                diff=ImageChops.difference(a,b)
                box=diff.getbbox()
                # A single RGB pixel is different if any of its channels differs.
                r,g,blue=diff.split()
                mask=ImageChops.lighter(ImageChops.lighter(r,g),blue)
                hist=mask.histogram()
                count=a.width*a.height-hist[0]
                row=dict(pdf_page=number,width=a.width,height=a.height,
                         local_png_sha256=sha(left),publisher_png_sha256=sha(right),
                         pixel_equal=box is None,differing_pixels=count,
                         differing_pixel_fraction=count/(a.width*a.height),difference_bbox=box,
                         maximum_channel_difference=max(upper for lower,upper in diff.getextrema()))
                if box:
                    out=WORK/'review/syllabus-image-differences'
                    out.mkdir(exist_ok=True)
                    a.save(out/f'page-{number:02d}-local.png')
                    b.save(out/f'page-{number:02d}-publisher.png')
                    # Contrast is amplified only in this diagnostic image.
                    diff.point(lambda value:min(value*10,255)).save(out/f'page-{number:02d}-difference.png')
                results.append(row)
    report=dict(checked_at_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
                local_pdf_path=str(local.relative_to(ROOT)),local_sha256=sha(local),
                publisher_pdf_url=currency['official_pdf_url'],publisher_sha256=sha(publisher),
                publisher_retrieved_at_utc=currency['retrieved_at_utc'],
                method='Poppler pdftoppm -r 144 -png for all 52 pages of both PDFs; exact RGB pixel comparison with Pillow.',
                renderer=subprocess.run(['pdftoppm','-v'],text=True,capture_output=True).stderr.splitlines()[0],
                pillow_version=Image.__version__,pages_compared=len(results),
                pixel_equal_pages=sum(row['pixel_equal'] for row in results),
                differing_pages=[row['pdf_page'] for row in results if not row['pixel_equal']],
                scope_limit='Fixed-resolution current page rendering, including diagrams. Does not establish unchanged historical content, cohort validity, hidden metadata or PDF structural identity.',
                pages=results)
    dest=WORK/'review/syllabus-page-image-comparison.json'
    dest.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({key:report[key] for key in ('pages_compared','pixel_equal_pages','differing_pages','method')},indent=2))


if __name__=='__main__':
    main()
