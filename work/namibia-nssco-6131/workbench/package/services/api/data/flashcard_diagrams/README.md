# Prepared visual maths content

Twenty authored families, 48 levels, 1,495 fixed question/diagram instances and
1,912 immutable PNGs. Each level has at least 23 distinct question/image identities
for ten canonical examples, ten fresh questions and three historical avoidances.
Banks are finite; they do not create unlimited new art. The API must ship this
manifest and every referenced PNG, retaining them for historical attempts.

Preparation uses installed Pillow and a local font, without a paid provider:

```
services/api/venv/bin/python services/api/scripts/prepare_visual_flashcard_banks.py --font /path/to/Arial.ttf
```

Source builders are offline authoring inputs. Runtime recipes read prepared
content; the browser JSON/SVG renderer stays paused. The script refuses to replace
an existing manifest. Changed content needs a new version and additive asset
reader support. The font itself and preparation checkpoints are not distributed.

The manifest contains plain questions, written answers, separate explanations,
instance-specific proposed marking achievements, source IDs and SHA-256 image
references. Existing authorised Studio responses/reveal rules deliver the PNGs;
these files are not public web assets. Reference diagrams remain distinct from
learner photos, including grading retries. The offline preview deduplicates PNG
files; current runtime payloads inline bounded images. If combined testing finds
large-deck response-size problems, private lazy delivery can reuse these identities.

Source-ID checks do not establish live AI marking accuracy or teacher approval of
adapted tariffs. Native Topic 12 classroom IDs and actual import remain target-DB
work; offline preview IDs are never valid live lesson IDs. Full learner testing
follows integration, as requested.
