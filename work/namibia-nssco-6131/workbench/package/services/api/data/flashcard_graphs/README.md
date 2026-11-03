# Prepared flashcard graph pilot

Original straight-line gradient questions, authored from exact rational data.
`v1/manifest.json` binds forty question/solution PNG pairs by SHA-256. This is a
finite technical pilot, not complete visual maths coverage or an official exam
question bank. The two-mark allocation adapts the existing coordinate-gradient
source; it still requires teacher acceptance of this visual demand.

PNG preparation uses Pillow at build time:

```
services/api/venv/bin/python services/api/scripts/prepare_flashcard_graph_bank.py --font /path/to/Arial.ttf
```

These checked-in bytes were prepared with the local macOS Arial font. The font
is not distributed here. No font or plotting dependency is needed to serve the
prepared images. Render differences must produce a new bank version; never
replace old manifests or PNGs after cards have been imported. Saved attempts
rely on those exact bytes. Include this directory when releasing the API.

Image columns store short `yyeni-graph:v1:...` references, not image bytes. Studio
expands references to bounded PNG data URLs only inside existing authorised
responses and solution-reveal conditions. There is no public asset endpoint.
The contract hashes the references and verifies them against its seed's exact
question/answer. Missing or corrupt files prevent marking. Grader images 1–2
are question/solution references; only later images are learner evidence.

Bank size and inline delivery are deliberately bounded. Use existing private
asset delivery when expanding substantially; do not add permanent public
solution links. The paused custom visual renderer is not used by this pilot.
