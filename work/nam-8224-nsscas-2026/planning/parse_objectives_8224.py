#!/usr/bin/env python3
"""Parse every specific-objective bullet of the 8224 syllabus content tables (step 2/3 support).
Writes planning/syllabus_bullets.json: [{unit, theme, n, text, page, pdf_page}]. Text is the syllabus
wording, one bullet per entry; later steps use it as syllabus_text. Validate counts before use."""
import json, os, re, subprocess
HERE = os.path.dirname(os.path.abspath(__file__)); WS = os.path.dirname(HERE)
ROOT = os.path.abspath(os.path.join(WS, "..", ".."))
PDF = os.path.join(ROOT, "Syllabi/Namibian Curricula/NSSCAS/NSSCAS_8224_Chemistry_approved_syllabus_updated_20_November_2020.pdf")
BUL = ""
facts = json.load(open(os.path.join(WS, "curriculum", "syllabus-facts.json")))
pages = sorted({o["pdf_page"] for o in facts["content_outline"]})
first, last = pages[0], pages[-1]
def lay(n): return subprocess.run(["pdftotext", "-layout", "-f", str(n), "-l", str(n), PDF, "-"], capture_output=True, text=True).stdout
def printed(n):
    m = re.match(r"NSSCAS Chemistry Syllabus, NIED 2020\s*\n\s*(\d+)", subprocess.run(["pdftotext", "-raw", "-f", str(n), "-l", str(n), PDF, "-"], capture_output=True, text=True).stdout)
    return int(m.group(1)) if m else None
out = []; unit = None; theme = None; cur = None
def flush():
    global cur
    if cur and cur["text"].strip():
        cur["text"] = re.sub(r"\s+", " ", cur["text"]).strip(); out.append(cur)
    cur = None
for n in range(first, last + 1):
    lines = lay(n).splitlines()
    hdr = next((l for l in lines if "SPECIFIC OBJECTIVES" in l), None)
    col = hdr.index("SPECIFIC OBJECTIVES") if hdr else None
    pp = printed(n)
    for l in lines:
        m = re.match(r"^\s*THEME (\d)", l)
        if m: theme = m.group(1); continue
        m = re.match(r"^\s*(\d\.\d(?:\.\d)?)\s*[A-Z]", l)
        if m and m.group(1)[0] == theme:
            flush(); unit = m.group(1)
        if col is None or unit is None: continue
        if "SPECIFIC OBJECTIVES" in l or "Learners should be able" in l or "TOPIC" in l[:8]: continue
        seg = l[col - 3:] if len(l) > col - 3 else ""
        idx = seg.find(BUL)
        # a bullet that belongs to the specific column sits within 5 chars of the column start
        if 0 <= idx <= 6:
            flush(); cur = {"unit": unit, "theme": theme, "text": seg[idx + 1:], "page": pp, "pdf_page": n}
        elif cur is not None and seg.strip() and not re.match(r"^NSSCAS Chemistry", l.strip()) and not re.match(r"^\s*\d+\s*$", l):
            cur["text"] += " " + seg.strip().replace(BUL, "")
    # leave cur open across pages (objective may continue) but close at unit change handled above
flush()
for i, o in enumerate(out):
    o["n"] = sum(1 for p in out[:i + 1] if p["unit"] == o["unit"])
json.dump(out, open(os.path.join(HERE, "syllabus_bullets.json"), "w"), indent=1, ensure_ascii=False)
from collections import Counter
c = Counter(o["unit"] for o in out)
print("bullets:", len(out), "| units with bullets:", len(c))
print({k: v for k, v in sorted(c.items())})
