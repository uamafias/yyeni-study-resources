"""Local PDF evidence utilities for the 8227 analysis; never downloads or edits PDFs."""
from pathlib import Path
import hashlib
import json
import re
import subprocess
import tempfile
import pymupdf
from PIL import Image
from pypdf import PdfReader

ROOT = Path(__file__).resolve().parents[4]
WB = Path(__file__).resolve().parents[1]
A = WB / 'analysis'


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def write(path, value):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n')


def evidence_path(value):
    """Persisted evidence must relocate with this subject workspace."""
    p=Path(value)
    assert not p.is_absolute(), ('absolute evidence path',value)
    resolved=(ROOT/p).resolve()
    assert resolved.is_relative_to(WB.resolve()), ('outside-workspace evidence path',value)
    assert resolved.is_file(), ('missing evidence',value)
    return resolved


def clean(text):
    return re.sub(r'\s+', ' ', re.sub(r'\.{4,}', '', text)).strip()


def paper_scan(year, component):
    data = json.loads((A / 'extracted' / f'{year}-P{component}.json').read_text())
    path = ROOT / data['source']
    assert digest(path) == data['sha256']
    pages = PdfReader(path).pages
    chunks = []
    for n, p in enumerate(pages, 1):
        text = p.extract_text()
        if n > 1 and re.search(r'FORMULAE\s+AND\s+NOTATIONS', text, re.I):
            break
        if n > 1:
            chunks.append((n, text))
    marks = []
    previous = []
    for n, text in chunks:
        start = 0
        for m in re.finditer(r'\[\s*(\d+)\s*\]', text):
            segments = previous + [{'pdf_page':n,'text':text[start:m.start()]}]
            segment = '\n'.join(x['text'] for x in segments)
            marks.append({'pdf_page': n, 'marks': int(m[1]), 'segment': segment,
                          'segment_pages':segments,
                          'cue_hits': [x.group(0) for x in re.finditer(
                              r'hence(?:,?\s+or\s+otherwise)?|found\s+in\s+part|using\s+your|'
                              r'use\s+your\s+(?:graphs?|sketch)|these\s+values|\bparts?\s*\(', segment, re.I)]})
            start = m.end()
            previous = []
        previous.append({'pdf_page':n,'text':text[start:]})
    return data, marks


def crop_asset(source_path, pdf_page, box, asset_id, purpose):
    """box is PDF points, top-left origin; output is a rendered source crop."""
    path = ROOT / source_path
    document = pymupdf.open(path)
    page = document[pdf_page - 1]
    rect = pymupdf.Rect(box)
    assert not rect.is_empty and page.rect.contains(rect), (asset_id, box)
    from check_crop_containment import validate
    containment=validate(source_path,pdf_page,list(box),asset_id)
    target = A / 'assets' / (asset_id + '.png')
    target.parent.mkdir(exist_ok=True)
    # Some 2023/2024 papers render almost white with the installed PyMuPDF renderer although the
    # text layer is black. PDFKit preserves their lines, labels and shading.
    rendered = render_page(source_path, pdf_page)
    with Image.open(rendered) as im:
        im.crop(tuple(round(v * 2) for v in box)).save(target)
    return {'asset_id': asset_id, 'path': str(target.relative_to(ROOT)),
            'sha256': digest(target), 'source_path': source_path,
            'source_sha256': digest(path), 'pdf_page': pdf_page,
            'crop_box_pdf_points': list(box), 'coordinate_system': 'top-left; PDF points',
            'render_engine': 'macOS PDFKit; render_pdf_macos.swift', 'dpi': 144,
            'containment_check':containment,'intentional_exclusions':containment['intentional_exclusions'],
            'purpose': purpose, 'origin': 'rendered-source-crop; original bytes unchanged'}


def render_page(source_path, pdf_page):
    cache = Path(tempfile.gettempdir()) / '8227-repair-r2' / 'renders'
    cache.mkdir(parents=True, exist_ok=True)
    swift = WB / 'tools/render_pdf_macos.swift'
    binary = cache / ('render-' + digest(swift)[:12])
    if not binary.exists():
        subprocess.run(['swiftc', str(swift), '-o', str(binary)], check=True,
                       capture_output=True)
    directory = cache / digest(swift)[:12] / digest(ROOT / source_path)
    target = directory / f'page-{pdf_page:04d}.png'
    if not target.exists():
        subprocess.run([str(binary), str(ROOT / source_path), str(directory), str(pdf_page)],
                       check=True, capture_output=True)
    return target


def reference_label(ref):
    if ref['relation'] == 'derived-from':
        return (f'Adapted from Cambridge International AS Level Mathematics 9709, Paper {ref["paper"]}, '
                f'{ref["session"]} {ref["year"]}, Question {ref["question"]}')
    if ref['relation'] == 'related':
        return None
    part = ref['part']
    suffix = '' if part in [None, '', 'answer'] else ''.join('(' + p + ')' for p in part.split('.'))
    if ref['board'] == 'NSSCAS':
        text = (f'NSSCAS Mathematics 8227, {ref["year"]} Paper {ref["paper"]}, '
                f'Question {ref["question"]}{suffix}, page {ref["printed_page"]}')
    else:
        text = (f'Cambridge International AS Level Mathematics 9709, Paper {ref["paper"]}, '
                f'{ref["session"]} {ref["year"]}, Question {ref["question"]}{suffix}, '
                f'page {ref["printed_page"]}')
    return ('Same type as ' + text) if ref['relation'] == 'same-type' else text
