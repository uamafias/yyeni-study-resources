# Brief: sourcing candidate visuals for NSSCO Biology 6116

You find candidate images for the requirements in `needs_<AREA>.json`. You write one file,
`candidates_<AREA>.json`. You change nothing else, and you do not commit.

## What is needed

Each requirement names an objective and kinds:
- **stimulus_image**: a real image a learner identifies structures from (photomicrograph, slide, photograph).
  It needs at least two different specimens: one to teach with, and one *unfamiliar example* for recognition
  practice.
- **teaching_diagram**: a clear diagram that shows every structure the objective names.

One good image may serve several requirements; list every objective it serves. `existing_candidates` names
assets already in the bank. Do not repeat them. Add a different specimen where an unfamiliar example is still needed.

## Where to look

Use Wikimedia Commons only, through its API with curl (`-A "YYeniVisualBank/0.1 (educational curation)"`).
- Search: `https://commons.wikimedia.org/w/api.php?action=query&format=json&list=search&srnamespace=6&srlimit=20&srsearch=<terms>`
- File metadata: `...&prop=imageinfo&iiprop=url|size|extmetadata&iiurlwidth=800&titles=File:<name>`. This returns
  `Artist`, `LicenseShortName`, `LicenseUrl`, `ImageDescription` and a thumbnail URL.

Licences allowed: CC0, public domain, CC BY, CC BY-SA. Reject NC, ND, "fair use", unknown, and any file whose
licence the API does not state. Prefer authentic micrographs and photographs to drawings for stimulus images.
Never use AI-generated images.

## Inspect before you propose

For each image you propose, download its 800-px thumbnail to
`/private/tmp/claude-501/-Users-yyeniai/2e531971-eaf4-4d19-8acd-0e09c1a53e69/scratchpad/vis_<AREA>/`.
Wait at least 3 seconds between downloads; on HTTP 429, wait 60 seconds and continue. Look at it with the Read
tool, then record what you actually see:
- the structures visible, and those the objective needs that are missing;
- whether it already carries labels (labels make it a teaching image, not a question image);
- whether it has a scale bar, a stated magnification, or neither;
- anything doubtful: tissue identity, orientation, staining, labels in another language, watermarks.

If you could not inspect an image, say so (`"inspected": false`). Never guess what an image shows from its title.

## Output: `candidates_<AREA>.json`

A JSON list. Use this record shape for each candidate:

```json
{"asset_id": "BIO-6116-<PREFIX>-001", "title": "...", "source_kind": "web",
 "source_url": "https://commons.wikimedia.org/wiki/File:...", "download_url": "<original file URL>",
 "source_locator": "Commons file page; metadata via API on 2026-10-18",
 "objective_ids": ["OBJ-6116-..."], "kinds": ["stimulus_image" | "teaching_diagram"],
 "roles": ["teaching" | "question" | "unfamiliar_example"],
 "image_type": "micrograph | photograph | schematic | labelled diagram",
 "has_labels": true, "labels_language": "en",
 "scale": {"scale_bar": false, "magnification_stated": "400x per description, unverified", "note": "..."},
 "structures_visible": ["..."], "structures_missing": ["..."],
 "rights": {"status": "file-specific licence recorded; attribution review pending", "creator": "...",
            "licence": "CC BY-SA 4.0", "licence_url": "...", "changes": "none; original to be preserved"},
 "suitability_concerns": ["..."], "inspected": true, "width": 0, "height": 0}
```

Asset ID prefixes: CELL (area A), HUM (area B), ORG (area C). Number them from 001.

## Report

Under 200 words:
- how many candidates, and how many inspected;
- requirements still without any candidate;
- stimulus requirements still without an unfamiliar example;
- problems you met.
