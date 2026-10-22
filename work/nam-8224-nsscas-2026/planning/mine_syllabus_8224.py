#!/usr/bin/env python3
"""Transcribe NSSCAS Chemistry 8224 syllabus facts, each with its page and verbatim line.

Step 2 of TEAM-PLAYBOOK. Every value is located IN the PDF text by pattern (never typed from
memory); the quote is the line as extracted, whitespace-normalised. Run with --verify to
re-open the PDF with a separate extraction and fail if any quote is not on the page it cites.

  python3 planning/mine_syllabus_8224.py            # writes curriculum/syllabus-facts.json
  python3 planning/mine_syllabus_8224.py --verify
"""
import json, os, re, subprocess, sys, datetime

HERE = os.path.dirname(os.path.abspath(__file__))
WS = os.path.dirname(HERE)
ROOT = os.path.abspath(os.path.join(WS, "..", ".."))
SYL = "Syllabi/Namibian Curricula/NSSCAS/NSSCAS_8224_Chemistry_approved_syllabus_updated_20_November_2020.pdf"
PDF = os.path.join(ROOT, SYL)
OUT = os.path.join(WS, "curriculum", "syllabus-facts.json")


def norm(s):
    s = s.replace("‘", "'").replace("’", "'").replace("„", "'").replace("‟", "'").replace("“", '"').replace("”", '"')
    return re.sub(r"\s+", " ", s).strip()


def page_text(n, mode):
    return subprocess.run(["pdftotext", "-" + mode, "-f", str(n), "-l", str(n), PDF, "-"],
                          capture_output=True, text=True, check=True).stdout


NPAGES = int(re.search(r"Pages:\s+(\d+)", subprocess.run(["pdfinfo", PDF], capture_output=True, text=True).stdout).group(1))
LAY = {n: page_text(n, "layout") for n in range(1, NPAGES + 1)}
RAW = {n: page_text(n, "raw") for n in range(1, NPAGES + 1)}


def printed(n):
    m = re.match(r"NSSCAS Chemistry Syllabus, NIED 2020\s*\n\s*(\d+)", RAW[n])
    return int(m.group(1)) if m else None


def find(regex, mode="layout", first=1, last=None, section=None, flags=0):
    """first line matching regex -> citation dict with the verbatim (normalised) line."""
    src = LAY if mode == "layout" else RAW
    for n in range(first, (last or NPAGES) + 1):
        for line in src[n].splitlines():
            if re.search(regex, norm(line), flags):
                return {"page": printed(n), "pdf_page": n, "section": section, "verbatim": norm(line), "mode": mode}
    raise SystemExit("NOT FOUND in syllabus: %r" % regex)


def cite(c):
    return {"page": c["page"], "pdf_page": c["pdf_page"], "section": c["section"]}


def build():
    facts = {
        "facts_id": "SYLFACTS-NAM-8224-NSSCAS-2026",
        "generated_at": datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"),
        "generated_by": "planning/mine_syllabus_8224.py",
        "authority": "NSSCAS Chemistry syllabus 8224, NIED 2020 (updated 20 November 2020).",
        "source_document": SYL,
        "pages_in_document": NPAGES,
        "rule": "STEP ZERO of the pipeline. Every value here is transcribed from the syllabus and carries the page that states it (printed page and PDF page) and the verbatim line. A value without a citation is a value we do not have.",
        "route": "NSSCAS (Advanced Subsidiary), Grade 12",
        "papers_sat": ["1 Multiple choice", "2 Structured questions", "3 Advanced practical skills"],
    }
    # ---- qualification facts
    q = {}
    q["guided_learning_hours"] = find(r"learners have about 180", section="4.1 Guided learning hours")
    q["duration"] = find(r"one year, but this is for guidance only|duration of one year", section="4.1 Guided learning hours")
    q["prior_learning"] = find(r"studied Chemistry at Namibia Senior Secondary Certificate Ordinary", section="4.2 Prior learning")
    q["grades"] = find(r"grades a, b, c, d or e", section="4.4 Grading and reporting")
    facts["qualification_facts"] = {k: {"verbatim": v["verbatim"], "source": cite(v)} for k, v in q.items()}

    # ---- assessment objectives
    aos = []
    sec6 = find(r"^A Knowledge with understanding", section="6 Assessment objectives", first=15)
    grid_pg = find(r"SPECIFICATION GRID", section="8 Specification grid", first=15)
    specs = {"A": ("A Knowledge with", r"^A Knowledge with 40%"), "B": ("B Handling information", r"^B Handling information, 40%"), "C": ("C Practical", r"^C Practical \(experimental 20%")}
    names = {"A": "Knowledge with understanding", "B": "Handling information, application and solving problems", "C": "Practical (experimental and investigative) skills and abilities"}
    for code in "ABC":
        gl = find(specs[code][1], first=grid_pg["pdf_page"], section="8 Specification grid")
        # sub-skills A1.. B1.. C1.. : lines starting with code+digit within section 6 pages
        subs = []
        for n in range(sec6["pdf_page"], sec6["pdf_page"] + 2):
            lines = LAY[n].splitlines()
            for i, line in enumerate(lines):
                m = re.match(r"^\s*(%s\d)\s+(\S.*)$" % code, line)
                if m:
                    text = norm(m.group(2)); j = i + 1
                    while j < len(lines) and lines[j].strip() and not re.match(r"^\s*([ABC]\d|[ABC]\s)\s*", lines[j]) and not re.match(r"^\s*(Learners|The Learning Content|These skills|NSSCAS)", lines[j]):
                        text += " " + norm(lines[j]); j += 1
                    subs.append({"code": m.group(1), "text": text, "first_line": norm(line), "page": printed(n), "pdf_page": n})
        aos.append({"code": code, "name": names[code], "can_do": [s["text"] for s in subs], "sub_skills": subs,
                    "source": {"page": sec6["page"], "pdf_page": sec6["pdf_page"], "section": "6 Assessment objectives"},
                    "verbatim": find(r"^%s (Knowledge with understanding|Handling information, application|Practical \(experimental and investigative\))" % code, section="6", first=15)["verbatim"],
                    "grid_line": gl["verbatim"], "grid_source": cite(gl)})
    facts["assessment_objectives"] = aos

    # ---- paper structure
    papers = []
    scheme = find(r"SCHEME OF ASSESSMENT", first=15, section="7")["pdf_page"]
    pdefs = [("1", "Theory: Multiple choice questions", r"^Paper 1: This paper consists of forty multiple-choice 1 hour 40", 60, r"^Paper 1 31%"),
             ("2", "Theory: Structured questions", r"^Paper 2: This paper consists of compulsory short- 1 hour 15 60", 75, r"^Paper 2 46%"),
             ("3", "Advanced practical skills", r"^Paper 3: This paper requires learners to carry out 2 hours 40", 120, r"^Paper 3 23%")]
    marks = {"1": 40, "2": 60, "3": 40}; pct = {"1": 31, "2": 46, "3": 23}
    for pid, nm, rx, dur, wrx in pdefs:
        c = find(rx, first=scheme, section="7 Scheme of assessment"); w = find(wrx, first=scheme, section="7 Scheme of assessment")
        papers.append({"paper": pid, "name": nm, "marks": marks[pid], "duration_minutes": dur, "weight_percent": pct[pid],
                       "source": cite(c), "verbatim": c["verbatim"], "weight_source": cite(w), "weight_verbatim": w["verbatim"]})
    facts["papers"] = papers
    facts["paper_total_marks"] = {"value": 140, "verbatim": find(r"^TOTAL 140", first=scheme, section="7")["verbatim"], "source": cite(find(r"^TOTAL 140", first=scheme, section="7"))}
    facts["paper_weight_statement"] = (lambda c: {"verbatim": c["verbatim"], "source": cite(c)})(find(r"constitute 77% of the final assessment while Paper 3 will constitute 23%", first=scheme, section="7"))
    # grid marks per AO per paper (from the grid lines)
    gm = {}
    for code in "ABC":
        gl = [a for a in aos if a["code"] == code][0]["grid_line"]
        nums = re.findall(r"(\d+)%\s+(\d+)\s+(\d+)\s+(\d+)", gl)[0]
        gm[code] = {"printed_qualification_percent": int(nums[0]), "marks": {"P1": int(nums[1]), "P2": int(nums[2]), "P3": int(nums[3])}}
    facts["ao_weights"] = {
        "qualification_percent_as_printed": {k: v["printed_qualification_percent"] for k, v in gm.items()},
        "grid_marks": {k: v["marks"] for k, v in gm.items()},
        "per_component_percent": {"P1": {"A": 50, "B": 50, "C": 0}, "P2": {"A": 50, "B": 50, "C": 0}, "P3": {"A": 0, "B": 0, "C": 100}},
        "derived_from_marks_percent": {k: round(100 * sum(v["marks"].values()) / 140, 1) for k, v in gm.items()},
        "source": {"section": "8 Specification grid", "page": [a for a in aos][0]["grid_source"]["page"], "pdf_page": aos[0]["grid_source"]["pdf_page"]},
    }
    facts["paper_derived_from_marks_percent"] = {p["paper"]: round(100 * p["marks"] / 140, 1) for p in papers}
    facts["resources_supplied"] = {
        "paper_3_qualitative_notes": (lambda c: {"verbatim": c["verbatim"], "source": cite(c)})(find(r"\(annexe D\) will be supplied with paper 3", first=scheme, section="7")),
        "data_booklet": (lambda c: {"verbatim": c["verbatim"], "source": cite(c)})(find(r"data booklet contains the information that will be made available to candidates for paper 1 and", first=40, section="Annexe E")),
    }
    facts["recall_cap"] = (lambda c: {"verbatim": c["verbatim"], "source": cite(c)})(find(r"20% recall", first=grid_pg["pdf_page"], section="8"))
    facts["skills_vs_knowledge"] = (lambda c: {"verbatim": c["verbatim"], "source": cite(c)})(find(r"greater weighting of 60 per cent for skills", first=grid_pg["pdf_page"], section="8"))

    # ---- command words (glossary table)
    cw = []
    g0 = find(r"GLOSSARY OF COMMAND WORDS", first=15, section="10")["pdf_page"]
    rows = [("Define", r"^Define \(the is intended literally"), ("What do you understand by / What is meant by", r"^What do you normally implies"),
            ("State", r"^State implies a concise answer"), ("List", r"^List requires a number of points"), ("Explain", r"^Explain may imply reasoning"),
            ("Describe", r"^Describe requires candidates to state in words"), ("Discuss", r"^Discuss requires candidates"), ("Outline", r"^Outline implies brevity"),
            ("Deduce / predict", r"^Deduce/ implies that the candidate is not expected"), ("Comment", r"^Comment is intended as an open-ended"),
            ("Suggest", r"^Suggest is used in two main contexts"), ("Find", r"^Find is a general term"), ("Calculate", r"^Calculate is used when a numerical answer"),
            ("Measure", r"^Measure implies that the quantity"), ("Determine", r"^Determine often implies"), ("Estimate", r"^Estimate implies a reasoned"),
            ("Sketch", r"^Sketch when applied to graph work"), ("Construct", r"^Construct is often used in relation to chemical equations"),
            ("Compare", r"^Compare requires candidates"), ("Classify", r"^Classify requires candidates")]
    for word, rx in rows:
        c = find(rx, first=g0, last=g0 + 2, section="10 Glossary of command words")
        cw.append({"word": word, "words": [w.strip() for w in re.split(r"/", word)] if word.startswith("Deduce") else [word],
                   "verbatim": c["verbatim"], "source": cite(c)})
    facts["command_words"] = cw
    facts["command_word_table"] = {"count": len(cw), "page": cw[0]["source"]["page"], "section": "10 Glossary of command words",
        "note": "The syllabus calls this glossary 'a guide... not exhaustive'. Words observed in the papers but not listed, and listed words never observed, are recorded in the corpus analysis, never guessed."}

    # ---- content outline (themes, topics, sub-topics) from raw text
    outline, themes = [], []
    first_c = find(r"^THEME 1: THE PARTICULATE NATURE", mode="raw", first=9, section="5 Learning content")["pdf_page"]
    last_c = find(r"^6\.\s+ASSESSMENT OBJECTIVES|ASSESSMENT OBJECTIVES$", mode="raw", first=first_c, section="6")["pdf_page"]
    cur_theme = None
    for n in range(first_c, last_c + 1):
        lines = RAW[n].splitlines()
        for i, line in enumerate(lines):
            t = line.strip()
            m = re.match(r"^THEME (\d): (.+)$", t)
            if m:
                themes.append({"theme": m.group(1), "title": m.group(2).title().replace("And", "and"), "verbatim": t, "page": printed(n), "pdf_page": n}); cur_theme = m.group(1); continue
            m = re.match(r"^(\d\.\d(?:\.\d)?)\s*([A-Z][^\n]*)$", t)
            if m and m.group(1)[0] == cur_theme:
                title = m.group(2).strip(); j = i + 1
                while j < len(lines):
                    nx = lines[j].strip()
                    if (not nx) or ord(nx[0]) > 0xE000 or nx[0] in "•" or re.match(r"^(know|understand|show|appreciate|recognise|be able|Learners|TOPIC|This topic|The |SPECIFIC|GENERAL)", nx) or len(nx) > 60:
                        break
                    title += " " + nx; j += 1
                title = re.sub(r"\s+(know|understand|show understanding|appreciate)\b.*$", "", norm(title))
                title = re.sub(r"[\ue000-\uf8ff\u2022]", "", title).strip()
                outline.append({"id": m.group(1), "level": "subtopic" if m.group(1).count(".") == 2 else "topic", "theme": cur_theme,
                                "title": norm(title), "verbatim": t, "page": printed(n), "pdf_page": n})
    facts["themes"] = themes
    facts["content_outline"] = outline

    # ---- stated limits (wrapped lines are joined with the next line; glossary pages excluded)
    limits, seen = [], set()
    rx = re.compile(r"(not required|is not expected|not be expected|will not (be|require)|is not needed|should not attempt|only to draw conclusions|is not examined|no knowledge)", re.I)
    db_refs = []
    ctx_id = None
    gl_pages = {g0, g0 + 1}
    for n in range(first_c, NPAGES + 1):
        if n in gl_pages: continue
        lines = [l.strip() for l in RAW[n].splitlines()]
        for k, t in enumerate(lines):
            m = re.match(r"^(\d\.\d(?:\.\d)?)", t)
            if m: ctx_id = m.group(1)
            nxt = lines[k + 1] if k + 1 < len(lines) else ""
            if re.search(r"data booklet", t + " " + nxt, re.I) and "Annexe E" not in t and n <= last_c:
                db_refs.append({"applies_to": ctx_id, "verbatim": norm(t), "page": printed(n), "pdf_page": n})
            joined = norm(t + " " + nxt)
            if rx.search(t) or (rx.search(joined) and not rx.search(norm(nxt))):
                key = (n, norm(t))
                if key in seen: continue
                seen.add(key)
                quote = norm(t) if rx.search(t) else joined
                where = ctx_id if n <= last_c else "Annexe A / Paper 3"
                limits.append({"applies_to": where, "verbatim": quote, "page": printed(n), "pdf_page": n})
    facts["limits"] = limits
    facts["data_booklet_references"] = db_refs
    facts["transcribed_notes"] = [
        {"note": "Syllabus contradiction (paper weights): printed 31/46/23 percent; marks 40/60/40 of 140 give 28.6/42.9/28.6 percent. Not resolved here.", "cites": ["papers[*].weight_verbatim", "papers[*].verbatim"]},
        {"note": "Syllabus contradiction (AO weights): printed 40/40/20 percent; grid marks A 50, B 50, C 40 of 140 give 35.7/35.7/28.6 percent. Not resolved here.", "cites": ["ao_weights"]},
    ]
    return facts


def verify():
    d = json.load(open(OUT)); bad = 0; n = 0

    def walk(o):
        if isinstance(o, dict):
            if "verbatim" in o and ("pdf_page" in o or ("source" in o and "pdf_page" in o["source"])):
                yield o
            for v in o.values():
                yield from walk(v)
        elif isinstance(o, list):
            for v in o:
                yield from walk(v)
    for o in walk(d):
        pg = o.get("pdf_page") or o["source"]["pdf_page"]
        txt = norm(page_text(pg, "layout")) + " " + norm(page_text(pg, "raw"))
        n += 1
        if norm(o["verbatim"]) not in txt:
            bad += 1; print("NOT ON PAGE", pg, repr(o["verbatim"][:90]))
    for o in d["assessment_objectives"]:
        for s in o["sub_skills"]:
            n += 1
            if norm(s["first_line"]) not in norm(page_text(s["pdf_page"], "layout")):
                bad += 1; print("SUBSKILL NOT ON PAGE", s["code"])
    print("verified %d quotes, %d failures" % (n, bad)); sys.exit(1 if bad else 0)


if __name__ == "__main__":
    if "--verify" in sys.argv:
        verify()
    f = build()
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    json.dump(f, open(OUT, "w"), indent=1, ensure_ascii=False)
    print("wrote", OUT, "| themes", len(f["themes"]), "| outline", len(f["content_outline"]), "| command words", len(f["command_words"]), "| limits", len(f["limits"]))
