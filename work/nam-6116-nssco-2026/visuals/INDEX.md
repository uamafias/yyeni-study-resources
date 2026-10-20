# Biology 6116 visual bank

Plan approved by Lotto, 2026-10-18. The originally banked 254 image assets are operator-approved at their recorded file hashes. New item-specific graphs remain unapproved. Authored resources are in review; scientific verification and learner delivery remain separate.

**Counts.** 258 asset records (web 233, local_notes 10, original_graph 15). 317 stored files. 0 web originals not yet stored. 0 with a licence to block or check. 158 requirement × kind bindings: every need has a candidate (unreviewed) 76, partial 54, GAP 28. Needs: candidate (unreviewed) 228, variant to prepare 76, GAP 46. **Operator-approved image assets: 254. Scientific verification completed: 0. Requirements met: 0.**

## Three separate stages

1. **Preparation (now).** Locate, store and map. Graphs come from `planning/make_graphs_6116.py`, which reuses the plotting approach of `publish/cie-0455-igcse-2026/diagrams/make_diagrams_0455.py`. Micrographs and anatomical images are authentic, never generated.
2. **Approval (before release).** A Biology teacher checks identity, orientation, label positions, scale and syllabus scope. Reuse terms and attribution are checked against the file page. Each check is recorded with a name and date in `manifest.json`. None has been done.
3. **Delivery (blocked).** Current YYeni connector contracts expose card-side image asset fields and an attach action; actual image display and learner drawing or image submission remain undemonstrated. No card has been switched from a text task to a visual task.

## Files

- `manifest.json`: every asset, with source and page, creator, licence, reuse status, objectives, roles, inspection notes, scale, hashes and review state.
- `bindings.json`: requirement × kind → needs (teaching / question / answer / unfamiliar example / model drawing) → candidate files, plus missing structures, flags, content units and card slots.
- `source-inventory.json`: every local notes PDF and question paper, with candidate pages. Exam figures are reference only.
- `originals/`: unmodified external originals. Never edited.
- `variants/`: teaching, neutral-letter question and labelled answer overlays derived from originals; label positions are in `planning/visual_labels.json`.
- `reference-only/`: extractions from local notes. Rights are unknown, so these are never released.
- `provenance/`: Commons API metadata stored for each web original, fetched through the harvester (`_harvest/manifests/nam-6116-visual-bank.csv`).
- `generated/`: project-owned graphs (question and answer variants) and `graphs.json`.

## Rules applied

- An image that is found is not therefore accurate, reusable or sufficient. Every record stays `candidate (unreviewed)`.
- Originals stay untouched. Labelled teaching images, neutral-label question images and labelled answers are separate files.
- Scale bars are preserved. A doubtful magnification or scale is flagged and never used for a calculation.
- An unfamiliar-example need is met only by a second, different authentic specimen.
- A model-drawing need is a gap until a model drawing and its criteria exist. A photograph does not substitute.
- A text description never completes a visual objective.

## Explicit holds (excluded from candidate needs)

| Asset | Reason |
|---|---|
| BIO-6116-ROOT-001 | Defective scale label, beyond-syllabus labels and obscured starch-grain leader in variants. No counting towards any need until a corrected syllabus-limited variant and teacher review exist. Original preserved; no measurement use. |
| BIO-6116-ROOT-002 | organ and tissue identity unconfirmed (Commons says only "Dicot"); botanist to identify |
| BIO-6116-BLOOD-001 | Incomplete for the mapped full blood-cell requirement (no demonstrated lymphocyte); uncertain white-cell/platelet label placements. Hold pending exact-use teacher review and a separate lymphocyte field. |
| BIO-6116-OSMOSIS-001 | plasmolysis not clearly visible; confirm what the field shows before mapping it to osmosis objectives |
| BIO-6116-STEM-001 | Uncertain phloem placement and vascular-bundle extent in variants. Hold all uses pending teacher validation and appropriate bundle indication; original remains a sourcing candidate only. |
| BIO-6116-HUM-021 | Second white-cell identity uncertain. Hold pending a reviewed exact-use crop/label restriction; no cell-type key inferred from file title. |
| BIO-6116-HUM-023 | Commons metadata names no creator, so the attribution a CC licence requires cannot be written yet; confirm on the file page |
| BIO-6116-HUM-026 | Monocyte versus band-neutrophil identity unresolved. Hold pending expert confirmation of the exact intended phagocyte use. |
| BIO-6116-ORG-042 | looks like a scan of printed textbook artwork uploaded under a CC BY-SA claim; the uploader may not hold the rights. Do not use unless the original artwork's licence is traced |
| BIO-6116-GRAPH-HUMANPOP-001 | Approximate published values lack completed source/value verification. No counting towards graph needs before verification. |

## Assets

| Asset | Title | Source | Reuse | Files | Roles | Flags |
|---|---|---|---|---|---|---|
| BIO-6116-ROOT-001 | Ranunculus root cross-section | web | licensed CC BY-SA 4.0 | 4 | teaching |  |
| BIO-6116-ROOT-002 | Alternative dicot root cross-section | web | licensed CC BY 4.0 | 1 | unfamiliar_example | Low-detail field: identity and tissue visibility remain uncertain. Do not certify dicot anatomy from the file title alone.; Inspected 2026-10-18: TISSUE IDENTITY UNCERTAIN. The field is dominated by l… |
| BIO-6116-BLOOD-001 | Normal adult blood smear | web | licensed CC BY-SA 3.0 | 4 | question, unfamiliar_example | Inspected 2026-10-18: no lymphocyte visible. A lymphocyte-versus-phagocyte question needs a second field. |
| BIO-6116-LEAF-001 | Leaf tissue schematic | web | licensed CC BY-SA 3.0 | 1 | teaching | Source explicitly omits vascular tissue. Partial teaching support only; cannot satisfy full leaf structure requirement. |
| BIO-6116-OSMOSIS-001 | Red onion plasmolysis micrograph | web | licensed CC BY 4.0 | 1 | unfamiliar_example | Caption conflicts on 400× versus 4000×; do not claim magnification or use for a size calculation without resolving it. Confirm visible plasmolysis before labelling. |
| BIO-6116-NOTES-P003 | Apparatus (local notes candidate) | local_notes | REFERENCE ONLY: rights unknown | 1 | reference_only |  |
| BIO-6116-NOTES-P025 | Plant and animal cells (local notes candidate) | local_notes | REFERENCE ONLY: rights unknown | 2 | reference_only |  |
| BIO-6116-NOTES-P033 | Cell responses to osmosis (local notes candidate) | local_notes | REFERENCE ONLY: rights unknown | 2 | reference_only |  |
| BIO-6116-NOTES-P054 | Leaf cross-section (local notes candidate) | local_notes | REFERENCE ONLY: rights unknown | 1 | reference_only |  |
| BIO-6116-NOTES-P068 | Intestinal absorption (local notes candidate) | local_notes | REFERENCE ONLY: rights unknown | 1 | reference_only |  |
| BIO-6116-NOTES-P070 | Dicot root (local notes candidate) | local_notes | REFERENCE ONLY: rights unknown | 2 | reference_only |  |
| BIO-6116-NOTES-P071 | Dicot stem (local notes candidate) | local_notes | REFERENCE ONLY: rights unknown | 1 | reference_only |  |
| BIO-6116-NOTES-P078 | Heart anatomy (local notes candidate) | local_notes | REFERENCE ONLY: rights unknown | 1 | reference_only |  |
| BIO-6116-NOTES-P080 | Blood vessels (local notes candidate) | local_notes | REFERENCE ONLY: rights unknown | 3 | reference_only |  |
| BIO-6116-NOTES-P086 | Blood cells (local notes candidate) | local_notes | REFERENCE ONLY: rights unknown | 3 | reference_only |  |
| BIO-6116-STEM-001 | Sunflower stem cross-section micrograph | web | licensed CC0 | 4 | question, unfamiliar_example |  |
| BIO-6116-CELL-001 | Liver hepatocytes, H&E, high power | web | licensed CC BY-SA 4.0 | 1 | teaching, question |  |
| BIO-6116-CELL-002 | Liver section with 0.1 mm scale bar | web | licensed CC BY-SA 3.0 | 1 | question, unfamiliar_example |  |
| BIO-6116-CELL-003 | Palisade mesophyll cells with chloroplasts | web | licensed CC BY-SA 3.0 | 1 | unfamiliar_example |  |
| BIO-6116-CELL-004 | Syringa leaf TS, palisade layer, 400x | web | licensed CC0 | 1 | teaching, question, unfamiliar_example |  |
| BIO-6116-CELL-005 | Elodea leaf cells with chloroplasts, 400x | web | licensed CC BY-SA 3.0 | 1 | unfamiliar_example |  |
| BIO-6116-CELL-006 | Moss (Bryum capillare) leaf cells with chloroplasts | web | licensed CC BY-SA 4.0 | 1 | unfamiliar_example |  |
| BIO-6116-CELL-007 | Turgid Elodea cells, 400x | web | licensed CC BY 4.0 | 1 | teaching, unfamiliar_example |  |
| BIO-6116-CELL-008 | Onion epidermis cells, whole mount (OpenFlexure) | web | licensed CC BY 2.0 | 1 | teaching, question |  |
| BIO-6116-CELL-009 | Iodine-stained onion cells with eyepiece graticule | web | licensed CC BY 4.0 | 1 | unfamiliar_example, question |  |
| BIO-6116-CELL-010 | Human cheek cells, methylene blue, 400x | web | licensed CC BY-SA 4.0 | 1 | teaching, question |  |
| BIO-6116-CELL-011 | Human cheek cells, iodine stain, 400x | web | licensed CC BY-SA 4.0 | 1 | unfamiliar_example |  |
| BIO-6116-CELL-012 | Human cheek cell nucleus, high power | web | licensed CC BY-SA 4.0 | 1 | teaching, question, unfamiliar_example |  |
| BIO-6116-CELL-013 | Mammalian trachea, ciliated epithelium and cartilage (H&E) | web | licensed CC BY-SA 4.0 | 1 | teaching, question |  |
| BIO-6116-CELL-014 | Trachea t.s., ciliated epithelium, low power | web | licensed CC BY 4.0 | 1 | unfamiliar_example |  |
| BIO-6116-CELL-015 | Skeletal muscle, longitudinal, 400x | web | licensed CC BY-SA 4.0 | 1 | teaching, question |  |
| BIO-6116-CELL-016 | Smooth muscle, 400x | web | licensed CC BY-SA 4.0 | 1 | unfamiliar_example |  |
| BIO-6116-CELL-017 | Cardiac muscle, 400x | web | licensed CC BY-SA 4.0 | 1 | unfamiliar_example |  |
| BIO-6116-CELL-018 | Plant cell structure (labelled) | web | licensed Public domain | 1 | teaching |  |
| BIO-6116-CELL-019 | Animal cell structure (labelled) | web | licensed Public domain | 1 | teaching |  |
| BIO-6116-CELL-020 | Simple animal cell diagram (labelled) | web | licensed CC BY 4.0 | 1 | teaching |  |
| BIO-6116-CELL-021 | Mitochondria in lung cell, TEM | web | licensed Public domain | 1 | teaching, question |  |
| BIO-6116-CELL-022 | Elongated mitochondrion, TEM | web | licensed Public domain | 1 | unfamiliar_example |  |
| BIO-6116-CELL-023 | Pancreatic cell nucleus and rough ER, TEM | web | licensed Public domain | 1 | teaching, question |  |
| BIO-6116-CELL-024 | Pancreatic acinar cells, TEM | web | licensed Public domain | 1 | unfamiliar_example, question |  |
| BIO-6116-CELL-025 | Clara cell, lung, TEM | web | licensed Public domain | 1 | unfamiliar_example |  |
| BIO-6116-CELL-026 | Hepatocyte TEM with labelled organelles (n, rer, g, m) | web | licensed CC BY 4.0 | 1 | teaching |  |
| BIO-6116-CELL-027 | Golgi apparatus and vesicles in a leukocyte, TEM | web | licensed Public domain | 1 | teaching, question |  |
| BIO-6116-CELL-028 | Levels of body organisation (graphic) | web | licensed CC0 | 1 | teaching |  |
| BIO-6116-CELL-029 | Levels of organisation drawing, numbered 1-7 | web | licensed CC BY-SA 3.0 | 1 | question |  |
| BIO-6116-CELL-030 | Stage micrometer slide (0.01 mm) | web | licensed CC BY 4.0 | 1 | teaching |  |
| BIO-6116-CELL-031 | Stage micrometer divisions under the microscope | web | licensed CC BY 4.0 | 1 | teaching, question |  |
| BIO-6116-CELL-032 | 10 ml measuring cylinder (empty) | web | licensed CC BY-SA 4.0 | 1 | teaching |  |
| BIO-6116-CELL-033 | Mercury thermometer, Celsius scale | web | licensed CC BY-SA 3.0 | 1 | question |  |
| BIO-6116-CELL-034 | Maximum-minimum thermometer | web | licensed CC BY-SA 3.0 | 1 | unfamiliar_example |  |
| BIO-6116-CELL-035 | Rhoeo (Tradescantia) epidermis after plasmolysis | web | licensed CC BY-SA 3.0 | 1 | unfamiliar_example, question |  |
| BIO-6116-CELL-036 | Plasmolysed plant cells | web | licensed CC BY-SA 4.0 | 1 | unfamiliar_example |  |
| BIO-6116-CELL-037 | Elodea cell in hypotonic, isotonic, hypertonic solutions (diagram) | web | licensed CC BY-SA 4.0 | 1 | teaching |  |
| BIO-6116-CELL-038 | Turgor pressure in plant cells: plasmolysed, flaccid, turgid | web | licensed Public domain | 1 | teaching |  |
| BIO-6116-CELL-039 | Visking tubing osmometer (lettered a-f) | web | licensed CC BY-SA 3.0 | 1 | question |  |
| BIO-6116-CELL-040 | Before/after diagram of dialysis tubing | web | licensed CC0 | 1 | teaching |  |
| BIO-6116-CELL-041 | Potato osmometer experiment | web | licensed CC BY-SA 4.0 | 1 | question, unfamiliar_example |  |
| BIO-6116-CELL-042 | Red blood cells in hypertonic, isotonic, hypotonic solutions (diagram) | web | licensed Public domain | 1 | teaching |  |
| BIO-6116-CELL-043 | Human red blood cells in hypertonic, isotonic, hypotonic solutions (phase contrast) | web | licensed CC BY-SA 3.0 | 1 | teaching, question |  |
| BIO-6116-CELL-044 | Ligustrum leaf TS, 100x | web | licensed CC0 | 1 | teaching, question |  |
| BIO-6116-CELL-045 | Syringa (lilac) leaf TS from midrib to lamina, 100x | web | licensed CC0 | 1 | teaching, question, unfamiliar_example |  |
| BIO-6116-CELL-046 | Syringa leaf TS with midrib, 100x (brown stain) | web | licensed CC0 | 1 | unfamiliar_example |  |
| BIO-6116-CELL-047 | Syringa leaf blade with vein, 100x | web | licensed CC0 | 1 | question |  |
| BIO-6116-CELL-048 | Syringa leaf, lower epidermis and spongy mesophyll, 400x | web | licensed CC0 | 1 | question, unfamiliar_example |  |
| BIO-6116-CELL-049 | Ligustrum lower epidermis and spongy mesophyll, 400x | web | licensed CC0 | 1 | unfamiliar_example |  |
| BIO-6116-CELL-050 | Mesophytic leaf section (green/orange stain) | web | licensed CC BY-SA 3.0 | 1 | unfamiliar_example |  |
| BIO-6116-CELL-051 | Leaf cross-section diagram (labelled) | web | licensed CC BY-SA 4.0 | 1 | teaching |  |
| BIO-6116-CELL-052 | Tomato leaf epidermis varnish print with stomata, 400x | web | licensed CC BY-SA 4.0 | 1 | teaching, question |  |
| BIO-6116-CELL-053 | Runner bean leaf epidermis with stomata, 100x | web | licensed CC BY-SA 4.0 | 1 | question, unfamiliar_example |  |
| BIO-6116-CELL-054 | Tobacco plant upper leaf surface, SEM | web | licensed Public domain | 1 | unfamiliar_example |  |
| BIO-6116-CELL-055 | Nail-polish impression said to show stomata | web | licensed Public domain | 1 | question |  |
| BIO-6116-CELL-056 | Dicot root TS, stele and cortex, 100x | web | licensed CC BY 2.0 | 1 | question, unfamiliar_example |  |
| BIO-6116-CELL-057 | Ranunculus young root TS, 100x | web | licensed CC0 | 1 | teaching, question |  |
| BIO-6116-CELL-058 | Ranunculus root stele, 400x | web | licensed CC0 | 1 | teaching, question |  |
| BIO-6116-CELL-059 | Root tip and root hairs in soil (historic lantern slide) | web | licensed Public domain | 1 | teaching, question |  |
| BIO-6116-CELL-060 | Arabidopsis root with root hairs (fluorescence) | web | licensed CC BY 4.0 | 1 | unfamiliar_example |  |
| BIO-6116-CELL-061 | Sunflower stem TS, 100x (specimen 1.4-1.6 mm) | web | licensed CC BY 4.0 | 1 | question, unfamiliar_example |  |
| BIO-6116-CELL-062 | Young sunflower stem TS, 40x | web | licensed CC0 | 1 | teaching, question |  |
| BIO-6116-CELL-063 | Alfalfa (Medicago) stem TS, 40x | web | licensed CC0 | 1 | unfamiliar_example |  |
| BIO-6116-CELL-064 | Sunflower stem, outer tissues and vascular bundle, 400x | web | licensed CC0 | 1 | unfamiliar_example |  |
| BIO-6116-CELL-065 | Dicot stem TS, ink line drawing | web | licensed CC BY-SA 3.0 | 1 | question, teaching |  |
| BIO-6116-CELL-066 | Maize stem LS, xylem and phloem elements, 400x | web | licensed CC0 | 1 | teaching, unfamiliar_example |  |
| BIO-6116-CELL-067 | Pumpkin stem LS, sieve tubes, 400x | web | licensed CC0 | 1 | teaching, question |  |
| BIO-6116-CELL-068 | Onion root tip mitosis, several stages | web | licensed CC BY-SA 4.0 | 1 | teaching, question |  |
| BIO-6116-CELL-069 | Onion root tip squash, acetocarmine/orcein | web | licensed CC BY-SA 3.0 | 1 | question, unfamiliar_example |  |
| BIO-6116-CELL-070 | Onion root tip mitosis, 400x (watermarked) | web | licensed CC BY-SA 4.0 | 1 | unfamiliar_example |  |
| BIO-6116-CELL-071 | Onion root tip cell dividing, phase contrast, letters A and B | web | licensed CC BY-SA 4.0 | 1 | question |  |
| BIO-6116-CELL-072 | Lily pollen mother cells in meiosis I (metaphase, anaphase, telophase) | web | licensed CC BY-SA 3.0 | 1 | teaching, question |  |
| BIO-6116-CELL-073 | Lily meiosis: metaphase I and telophase I | web | licensed CC BY-SA 3.0 | 1 | unfamiliar_example, question |  |
| BIO-6116-CELL-074 | Lily anther cells in meiosis, 400x (watermarked) | web | licensed CC BY 3.0 | 1 | unfamiliar_example | stage of meiosis uncertain |
| BIO-6116-CELL-075 | Spinal cord cross-section: labelled diagram and micrograph | web | licensed CC BY 4.0 | 1 | teaching, question |  |
| BIO-6116-CELL-076 | Rat spinal cord TS | web | licensed CC BY-SA 3.0 | 1 | question, unfamiliar_example |  |
| BIO-6116-CELL-077 | Mammal spinal cord, part of TS | web | licensed CC BY-SA 3.0 | 1 | unfamiliar_example |  |
| BIO-6116-CELL-078 | Complete neurone diagram (labelled) | web | licensed Public domain | 1 | teaching |  |
| BIO-6116-CELL-079 | Unipolar sensory neurone (simple drawing) | web | licensed CC BY 3.0 | 1 | teaching |  |
| BIO-6116-CELL-080 | Multipolar motor neurone (simple drawing) | web | licensed CC BY 3.0 | 1 | teaching |  |
| BIO-6116-CELL-081 | Classification of neurones (3D renders) | web | licensed CC BY-SA 4.0 | 1 | unfamiliar_example |  |
| BIO-6116-CELL-082 | Withdrawal reflex arc illustration | web | licensed CC BY-SA 3.0 | 1 | teaching |  |
| BIO-6116-CELL-083 | Chemical synapse (OpenStax, labelled) | web | licensed CC BY 4.0 | 1 | teaching |  |
| BIO-6116-CELL-084 | Synapse illustration (labelled) | web | licensed CC BY-SA 3.0 | 1 | teaching |  |
| BIO-6116-CELL-085 | Simple synapse diagram | web | licensed CC BY-SA 1.0 | 1 | teaching |  |
| BIO-6116-CELL-086 | Labelled diagram of the eye | web | licensed CC BY-SA 4.0 | 1 | teaching |  |
| BIO-6116-CELL-087 | Human eye diagram without labels | web | licensed CC BY-SA 3.0 | 1 | question |  |
| BIO-6116-CELL-088 | Schematic diagram of the human eye (labelled) | web | licensed CC BY-SA 3.0 | 1 | teaching |  |
| BIO-6116-CELL-089 | Eye: lens, suspensory ligaments, ciliary muscle (labelled) | web | licensed CC BY-SA 4.0 | 1 | teaching |  |
| BIO-6116-CELL-090 | Focusing on distant and near objects | web | licensed CC BY-SA 2.5 | 1 | teaching, question |  |
| BIO-6116-CELL-091 | Accommodation: far point and near point (line drawing) | web | licensed Public domain | 1 | teaching |  |
| BIO-6116-CELL-092 | Major endocrine glands (male/female figure) | web | licensed Public domain | 1 | teaching |  |
| BIO-6116-CELL-093 | Endocrine glands of the reproductive system | web | licensed Public domain | 1 | teaching |  |
| BIO-6116-CELL-094 | Endocrine glands of the abdomen | web | licensed Public domain | 1 | teaching |  |
| BIO-6116-CELL-095 | Male urinary system (labelled) | web | licensed CC BY-SA 4.0 | 1 | teaching |  |
| BIO-6116-CELL-096 | Female urinary system (labelled) | web | licensed CC BY-SA 4.0 | 1 | teaching |  |
| BIO-6116-CELL-097 | Urinary system (unlabelled colour diagram) | web | licensed CC BY-SA 3.0 | 1 | question |  |
| BIO-6116-CELL-098 | Urinary system, numbered 1-14 | web | licensed CC BY-SA 3.0 | 1 | question |  |
| BIO-6116-CELL-099 | Urinary system with blank label lines | web | licensed Public domain | 1 | question |  |
| BIO-6116-CELL-100 | Urinary system line drawing (unlabelled) | web | licensed CC BY-SA 3.0 | 1 | question, unfamiliar_example |  |
| BIO-6116-HUM-001 | Digestive system diagram en | web | licensed Public domain | 1 | teaching |  |
| BIO-6116-HUM-002 | Intestinal villus simplified | web | licensed Public domain | 1 | teaching |  |
| BIO-6116-HUM-003 | Villi & microvilli of small intestine | web | licensed CC BY-SA 4.0 | 1 | teaching |  |
| BIO-6116-HUM-004 | Heart diagram-en | web | licensed CC BY-SA 3.0 | 1 | teaching |  |
| BIO-6116-HUM-005 | Diagram of the human heart (cropped) | web | licensed CC BY-SA 3.0 | 1 | teaching |  |
| BIO-6116-HUM-006 | Heart numlabels | web | licensed CC BY-SA 3.0 | 1 | question |  |
| BIO-6116-HUM-007 | Gray492 | web | licensed Public domain | 1 | teaching |  |
| BIO-6116-HUM-008 | Heart anterior exterior view | web | licensed CC BY 2.5 | 1 | question, unfamiliar_example |  |
| BIO-6116-HUM-009 | Artery Vein Capillary Comparison | web | licensed CC BY-SA 4.0 | 1 | teaching |  |
| BIO-6116-HUM-010 | Blood vessels-en | web | licensed CC BY-SA 3.0 | 1 | teaching |  |
| BIO-6116-HUM-011 | 2102 Comparison of Artery and Vein | web | licensed CC BY 3.0 | 1 | teaching |  |
| BIO-6116-HUM-012 | Blausen 0055 ArteryWallStructure | web | licensed CC BY 3.0 | 1 | teaching |  |
| BIO-6116-HUM-013 | 2101 Blood Flow Through the Heart | web | licensed CC BY 3.0 | 1 | teaching |  |
| BIO-6116-HUM-014 | 202410 Systemic and pulmonary circulation | web | licensed CC BY 4.0 | 1 | question |  |
| BIO-6116-HUM-015 | Blood oxygenation to the pulmonary and systemic circulation | web | licensed CC BY-SA 4.0 | 1 | teaching |  |
| BIO-6116-HUM-016 | Simple two pump circulation | web | licensed CC BY-SA 4.0 | 1 | teaching |  |
| BIO-6116-HUM-017 | Double closed circulation | web | licensed CC BY-SA 3.0 | 1 | question |  |
| BIO-6116-HUM-018 | Red White Blood cells | web | licensed Public domain | 1 | unfamiliar_example |  |
| BIO-6116-HUM-019 | Blood-lymphocyte2 | web | licensed CC BY-SA 4.0 | 1 | question |  |
| BIO-6116-HUM-020 | Blood-lymphocytes3 | web | licensed CC BY-SA 4.0 | 1 | teaching, question |  |
| BIO-6116-HUM-021 | Blood-lymphocytes2 | web | licensed CC BY-SA 4.0 | 1 | unfamiliar_example |  |
| BIO-6116-HUM-022 | Neutrophil in a blood smear | web | licensed CC BY-SA 3.0 | 1 | teaching |  |
| BIO-6116-HUM-023 | Segmented neutrophils | web | licensed CC BY-SA 3.0 | 1 | question |  |
| BIO-6116-HUM-024 | Neutrophil, erythrocytes and platelets in Wright-stained peripheral blood smear | web | licensed CC BY-SA 4.0 | 1 | unfamiliar_example |  |
| BIO-6116-HUM-025 | Blood-neutrophil2 | web | licensed CC BY-SA 4.0 | 1 | question |  |
| BIO-6116-HUM-026 | Blood-monocyte | web | licensed CC BY-SA 4.0 | 1 | unfamiliar_example |  |
| BIO-6116-HUM-027 | Alveolus diagram | web | licensed Public domain | 1 | teaching |  |
| BIO-6116-HUM-028 | 2309 The Respiratory Zone | web | licensed CC BY 3.0 | 1 | teaching |  |
| BIO-6116-HUM-029 | 2310 Structures of the Respiratory Zone-a | web | licensed CC BY 4.0 | 1 | teaching |  |
| BIO-6116-HUM-030 | Respiratory system complete en | web | licensed Public domain | 1 | teaching |  |
| BIO-6116-HUM-031 | 2316 Inspiration and Expiration | web | licensed CC BY 3.0 | 1 | teaching |  |
| BIO-6116-HUM-032 | External intercostal muscles frontal | web | licensed CC BY-SA 2.1 jp | 1 | teaching |  |
| BIO-6116-HUM-033 | Internal intercostal muscles frontal | web | licensed CC BY-SA 2.1 jp | 1 | teaching |  |
| BIO-6116-HUM-034 | MenstrualCycle2 en | web | licensed CC BY-SA 3.0 | 1 | teaching |  |
| BIO-6116-HUM-035 | Endocrine reproductive system en | web | licensed Public domain | 1 | teaching |  |
| BIO-6116-HUM-036 | Human male reproductive system en | web | licensed CC BY-SA 4.0 | 1 | teaching |  |
| BIO-6116-HUM-037 | Male genital system - Front view | web | licensed CC BY-SA 4.0 | 1 | teaching, unfamiliar_example |  |
| BIO-6116-HUM-038 | Male genital system - Front view-1 for quizzing | web | licensed CC BY-SA 4.0 | 1 | question |  |
| BIO-6116-HUM-039 | Male genital system - Sagittal view | web | licensed CC BY-SA 4.0 | 1 | unfamiliar_example, teaching |  |
| BIO-6116-HUM-040 | Male and female anatomy | web | licensed CC BY-SA 3.0 | 1 | question, unfamiliar_example |  |
| BIO-6116-HUM-041 | Scheme female reproductive system-en | web | licensed Public domain | 1 | teaching |  |
| BIO-6116-HUM-042 | Female genital system - Sagittal view | web | licensed CC BY-SA 4.0 | 1 | teaching, unfamiliar_example |  |
| BIO-6116-HUM-043 | Female reproductive system - anterior view | web | licensed CC0 | 1 | question |  |
| BIO-6116-HUM-044 | Placenta | web | licensed Public domain | 1 | teaching |  |
| BIO-6116-HUM-045 | 2910 The Placenta-02 | web | licensed CC BY 3.0 | 1 | teaching |  |
| BIO-6116-ORG-001 | Giant African land snail (Achatina fulica) Ranomafana | web | licensed CC BY-SA 4.0 | 1 | teaching, question |  |
| BIO-6116-ORG-002 | Achatina fulica (Giant African land snail) | web | licensed CC0 | 1 | question, unfamiliar_example |  |
| BIO-6116-ORG-003 | Octopus vulgaris 03 | web | licensed CC BY-SA 3.0 | 1 | unfamiliar_example |  |
| BIO-6116-ORG-004 | Snail diagram-en edit1 | web | licensed CC BY-SA 4.0 | 1 | teaching |  |
| BIO-6116-ORG-005 | Medicinal leech, Hirudo verbana | web | licensed CC BY-SA 4.0 | 1 | teaching, question |  |
| BIO-6116-ORG-006 | Lumbricidae earthworm on wet asphalt in Dnipro by baby-bear.org 01 | web | licensed CC BY 4.0 | 1 | question, unfamiliar_example |  |
| BIO-6116-ORG-007 | Hirudo medicinalis 01 | web | licensed CC BY-SA 4.0 | 1 | unfamiliar_example |  |
| BIO-6116-ORG-008 | Earthworm head | web | licensed CC BY-SA 4.0 | 1 | teaching |  |
| BIO-6116-ORG-009 | Oxycatantops spissus | web | licensed CC BY-SA 4.0 | 1 | teaching, question |  |
| BIO-6116-ORG-010 | Humbug Namib darkling beetle (Onymacris unguicularis) Swakopmund Namibia | web | licensed CC BY-SA 4.0 | 1 | unfamiliar_example, question |  |
| BIO-6116-ORG-011 | Onymacris unguicularis in Namib Desert | web | licensed CC BY-SA 3.0 | 1 | unfamiliar_example |  |
| BIO-6116-ORG-012 | Insect anatomy diagram | web | licensed CC BY-SA 3.0 | 1 | teaching |  |
| BIO-6116-ORG-013 | Parabuthus villosus, b, Usakos | web | licensed CC BY-SA 3.0 | 1 | teaching, question |  |
| BIO-6116-ORG-014 | Common Yellow-banded Baboon Spider (Harpactira tigrina) (33010615165) | web | licensed CC BY-SA 2.0 | 1 | teaching, question, unfamiliar_example |  |
| BIO-6116-ORG-015 | Scorpion (Parabuthus raudus) (6538398075) | web | licensed CC BY-SA 2.0 | 1 | unfamiliar_example |  |
| BIO-6116-ORG-016 | Spider external anatomy en | web | licensed CC BY-SA 4.0 | 1 | teaching |  |
| BIO-6116-ORG-017 | Potamonautes perlatus Cape River Crab 8806s | web | licensed CC BY-SA 3.0 | 1 | teaching, question |  |
| BIO-6116-ORG-018 | JasusLalandii | web | licensed Public domain | 1 | unfamiliar_example, question |  |
| BIO-6116-ORG-019 | West coast rock lobster, Jasus lalandii (5327331223) | web | licensed CC BY 2.0 | 1 | unfamiliar_example |  |
| BIO-6116-ORG-020 | Millipede, South Africa (40435620062) | web | licensed CC BY 2.0 | 1 | teaching, question |  |
| BIO-6116-ORG-021 | Millipede in South Africa 01 | web | licensed CC0 | 1 | unfamiliar_example, question |  |
| BIO-6116-ORG-022 | Scolopendra gigantea | web | licensed CC BY-SA 3.0 | 1 | teaching, question, unfamiliar_example |  |
| BIO-6116-ORG-023 | Hydrocynus vittatus 15808090 | web | licensed CC0 | 1 | teaching, question |  |
| BIO-6116-ORG-024 | Oreochromis-niloticus-Nairobi | web | licensed CC BY-SA 3.0 | 1 | teaching, question, unfamiliar_example |  |
| BIO-6116-ORG-025 | Pyxicephalus adspersus, Boston Aquarium | web | licensed CC BY-SA 3.0 | 1 | teaching, question |  |
| BIO-6116-ORG-026 | Sclerophrys gutturalis 349258132 | web | licensed CC0 | 1 | unfamiliar_example, question |  |
| BIO-6116-ORG-027 | Krallenfrosch Xenopus laevis | web | licensed CC BY 3.0 | 1 | unfamiliar_example |  |
| BIO-6116-ORG-028 | Chamaeleo namaquensis (Walvis Bay) | web | licensed CC BY-SA 3.0 | 1 | teaching, question |  |
| BIO-6116-ORG-029 | Leopard tortoise (Stigmochelys pardalis) juvenile | web | licensed CC BY-SA 4.0 | 1 | unfamiliar_example, question |  |
| BIO-6116-ORG-030 | Chamaeleo namaquensis (Namib-Naukluft, 2011) | web | licensed CC BY-SA 3.0 | 1 | unfamiliar_example |  |
| BIO-6116-ORG-031 | 154 Southern yellow-billed hornbill in Etosha National Park Photo by Giles Laurent | web | licensed CC BY-SA 4.0 | 1 | teaching, question |  |
| BIO-6116-ORG-032 | Lilac-breasted roller (Coracias caudatus caudatus) Botswana | web | licensed CC BY-SA 4.0 | 1 | unfamiliar_example, question |  |
| BIO-6116-ORG-033 | Antidorcas marsupialis, male (Etosha, 2012) | web | licensed CC BY-SA 3.0 | 1 | teaching, question |  |
| BIO-6116-ORG-034 | Meerkat (Suricata suricatta) with 3 young | web | licensed CC BY-SA 4.0 | 1 | unfamiliar_example, question |  |
| BIO-6116-ORG-035 | Monocot vs Dicot | web | licensed CC BY-SA 3.0 | 1 | teaching |  |
| BIO-6116-ORG-036 | Maize plant diagram | web | licensed CC0 | 1 | teaching |  |
| BIO-6116-ORG-037 | Zea mays kernel | web | licensed CC BY-SA 4.0 | 1 | teaching, question |  |
| BIO-6116-ORG-038 | Crinum moorei (Flower) | web | licensed CC BY-SA 3.0 | 1 | teaching, question |  |
| BIO-6116-ORG-039 | 01AA2026 Commelina communis flower | web | licensed CC BY 4.0 | 1 | unfamiliar_example, question |  |
| BIO-6116-ORG-040 | Parallel leaf venation | web | licensed CC0 | 1 | question, unfamiliar_example |  |
| BIO-6116-ORG-041 | Fibrous root | web | licensed CC BY-SA 4.0 | 1 | question, unfamiliar_example |  |
| BIO-6116-ORG-042 | Tap Root & Fibrous Root | web | licensed CC BY-SA 4.0 | 1 | teaching, question |  |
| BIO-6116-ORG-043 | Phaseolus seed L | web | licensed CC BY-SA 4.0 | 1 | teaching, question |  |
| BIO-6116-ORG-044 | Navy Bean Seed to Seedling Germination | web | licensed CC BY-SA 4.0 | 1 | unfamiliar_example, question |  |
| BIO-6116-ORG-045 | Hibiscus rosa-sinensis flower 2 | web | licensed CC BY-SA 4.0 | 1 | teaching, question |  |
| BIO-6116-ORG-046 | Tevenphage | web | licensed CC BY-SA 2.5 | 1 | teaching |  |
| BIO-6116-ORG-047 | Tobacco mosaic virus structure | web | licensed CC BY-SA 3.0 | 1 | teaching |  |
| BIO-6116-ORG-048 | TMV structure full | web | licensed CC BY-SA 3.0 | 1 | unfamiliar_example, teaching |  |
| BIO-6116-ORG-049 | DNA simple2 | web | licensed Public domain | 1 | teaching |  |
| BIO-6116-ORG-050 | Mature flower diagram | web | licensed Public domain | 1 | teaching |  |
| BIO-6116-ORG-051 | Lillium Stamens | web | licensed CC BY-SA 3.0 | 1 | teaching |  |
| BIO-6116-ORG-052 | Hibiscus pistil and stamens (14246111978) | web | licensed CC BY 2.0 | 1 | unfamiliar_example, question |  |
| BIO-6116-ORG-053 | Bee pollinating Aquilegia vulgaris | web | licensed CC BY-SA 3.0 | 1 | teaching, question |  |
| BIO-6116-ORG-054 | Malachite Sunbird (Nectarinia famosa) male on Aloe flowers (30216015541) | web | licensed CC BY-SA 2.0 | 1 | teaching, question |  |
| BIO-6116-ORG-055 | EB1911 Pollination - Grass Flower | web | licensed Public domain | 1 | teaching, question |  |
| BIO-6116-ORG-056 | Eustachys paspaloides, blomme, Skeerpoort | web | licensed CC BY-SA 3.0 | 1 | teaching, question, unfamiliar_example |  |
| BIO-6116-ORG-057 | Flowering pearl millet (4545169813) | web | licensed CC BY-SA 2.0 | 1 | teaching, question, unfamiliar_example |  |
| BIO-6116-ORG-058 | Zea mays silk | web | licensed CC BY-SA 3.0 | 1 | teaching, question |  |
| BIO-6116-ORG-059 | Tassels of maize | web | licensed CC BY-SA 4.0 | 1 | teaching, question |  |
| BIO-6116-ORG-060 | Pine releasing pollen into the wind in Tuntorp 1 | web | licensed CC BY-SA 4.0 | 1 | unfamiliar_example |  |
| BIO-6116-ORG-061 | Nymphaea leaf cross-section | web | licensed CC BY-SA 3.0 de | 1 | teaching, question |  |
| BIO-6116-ORG-062 | Nymphaea nouchali | web | licensed CC BY-SA 2.0 de | 1 | unfamiliar_example, question |  |
| BIO-6116-ORG-063 | Eichhornia crassipes from Maracaibo | web | licensed CC BY-SA 3.0 | 1 | teaching, question |  |
| BIO-6116-ORG-064 | Aloe dichotoma -Keetmanshoop, Namibia-21Aug2009-2 | web | licensed CC BY 2.0 | 1 | teaching, question |  |
| BIO-6116-ORG-065 | Aloidendron dichotomum K2 | web | licensed CC BY-SA 4.0 | 1 | unfamiliar_example |  |
| BIO-6116-ORG-066 | Welwitschia mirabilis | web | licensed CC BY-SA 4.0 | 1 | teaching, question |  |
| BIO-6116-ORG-067 | Welwitschia mirabilis kz03 | web | licensed CC BY-SA 4.0 | 1 | unfamiliar_example, question |  |
| BIO-6116-ORG-068 | Welwitschia mirabilis (female) | web | licensed CC BY-SA 4.0 | 1 | unfamiliar_example |  |
| BIO-6116-ORG-069 | Euphorbia virosa Namibia | web | licensed CC BY-SA 4.0 | 1 | teaching, question |  |
| BIO-6116-ORG-070 | Pachypodium lealii | web | licensed CC BY-SA 4.0 | 1 | teaching, question |  |
| BIO-6116-ORG-071 | Aloe littoralis (Windhoek Aloe)-2268 - Flickr - Ragnhild & Neil Crawford | web | licensed CC BY-SA 2.0 | 1 | unfamiliar_example, question |  |
| BIO-6116-ORG-072 | Aloe hereroensis Namibia | web | licensed CC BY-SA 2.0 | 1 | unfamiliar_example, question |  |
| BIO-6116-ORG-073 | Aloe littoralis (Windhoek Aloe) ^ Dusky Sunbird-1472 - Flickr - Ragnhild & Neil Crawford | web | licensed CC BY-SA 2.0 | 1 | unfamiliar_example |  |
| BIO-6116-ORG-074 | Lithops julii 001 GotBot 2015 | web | licensed CC BY 4.0 | 1 | unfamiliar_example |  |
| BIO-6116-ORG-075 | Food web diagram | web | licensed CC0 | 1 | teaching, question |  |
| BIO-6116-ORG-076 | Simplified food chain | web | licensed CC0 | 1 | question, teaching |  |
| BIO-6116-ORG-077 | Chesapeake Waterbird Food Web | web | licensed Public domain | 1 | teaching | labels 'Herbivores' and 'Primary Consumers' used as separate rows, which conflicts with syllabus usage |
| BIO-6116-ORG-078 | Ecological Pyramid | web | licensed CC BY-SA 4.0 | 1 | teaching |  |
| BIO-6116-ORG-079 | Nitrogen Cycle | web | licensed CC BY-SA 3.0 | 1 | teaching |  |
| BIO-6116-ORG-080 | Carbon cycle-cute diagram | web | licensed Public domain | 1 | teaching |  |
| BIO-6116-ORG-081 | World Population Growth 1700-2100 | web | licensed CC BY 4.0 | 1 | teaching, question |  |
| BIO-6116-ORG-082 | Population curve | web | licensed Public domain | 1 | question, unfamiliar_example |  |
| BIO-6116-GRAPH-OSMOSIS-001 | Potato tissue: change in mass against sucrose concentration | original_graph | project-owned (generated from declared data) | 4 | question, answer |  |
| BIO-6116-GRAPH-ENZYME-TEMP-001 | Rate of an enzyme-controlled reaction against temperature | original_graph | project-owned (generated from declared data) | 4 | question, answer |  |
| BIO-6116-GRAPH-ENZYME-PH-001 | Rate of an enzyme-controlled reaction against pH | original_graph | project-owned (generated from declared data) | 4 | question, answer |  |
| BIO-6116-GRAPH-PHOTO-LIGHT-001 | Rate of photosynthesis against light intensity at two carbon dioxide concentrations | original_graph | project-owned (generated from declared data) | 4 | question, answer |  |
| BIO-6116-GRAPH-PHOTO-CO2-001 | Rate of photosynthesis against carbon dioxide concentration | original_graph | project-owned (generated from declared data) | 4 | question, answer |  |
| BIO-6116-GRAPH-BREATHING-001 | Breathing rate before, during and after exercise | original_graph | project-owned (generated from declared data) | 4 | question, answer |  |
| BIO-6116-GRAPH-GROWTH-001 | Height of an annual plant from sowing to maturity | original_graph | project-owned (generated from declared data) | 4 | question, answer |  |
| BIO-6116-GRAPH-VARIATION-001 | Continuous and discontinuous variation | original_graph | project-owned (generated from declared data) | 2 | question, answer |  |
| BIO-6116-GRAPH-SIGMOID-001 | Sigmoid population growth curve | original_graph | project-owned (generated from declared data) | 4 | question, answer |  |
| BIO-6116-GRAPH-HUMANPOP-001 | World human population, 1800-2022 | original_graph | project-owned (generated from declared data) | 4 | question, answer |  |
| BIO-6116-GRAPH-PYRAMID-001 | Pyramids of numbers and biomass for one food chain | original_graph | project-owned (generated from declared data) | 4 | question, answer |  |
| BIO-6116-GRAPH-BREATH-VOLUME-001 | Breath volume trace at rest and during exercise | original_graph | project-owned (generated from declared data) | 4 | question, answer |  |
| BIO-6116-GRAPH-DRY-MASS-001 | Mean dry mass of an annual plant after sowing | original_graph | project-owned (generated from declared data) | 4 | question, answer |  |
| BIO-6116-GRAPH-GRASSLAND-BIOMASS-001 | Grassland biomass pyramid for item 5-016 | original_graph | project-owned (generated from declared data) | 4 | question, answer |  |
| BIO-6116-GRAPH-MODEL-TOWN-001 | Model-town population from the table in item 5-045 | original_graph | project-owned (generated from declared data) | 4 | question, answer |  |

## Requirements and gaps

| Requirement | Kind | Status | Needs | Missing in candidates |
|---|---|---|---|---|
| VIS-6116-1.2.2-02 | graph | every need has a candidate (unreviewed) | question: candidate (unreviewed); answer: candidate (unreviewed) |  |
| VIS-6116-1.2.3-02 | graph | every need has a candidate (unreviewed) | question: candidate (unreviewed); answer: candidate (unreviewed) |  |
| VIS-6116-1.2.3-03 | graph | every need has a candidate (unreviewed) | question: candidate (unreviewed); answer: candidate (unreviewed) |  |
| VIS-6116-1.2.3-06 | graph | every need has a candidate (unreviewed) | question: candidate (unreviewed); answer: candidate (unreviewed) |  |
| VIS-6116-1.2.3-07 | graph | every need has a candidate (unreviewed) | question: candidate (unreviewed); answer: candidate (unreviewed) |  |
| VIS-6116-1.2.3-08 | graph | every need has a candidate (unreviewed) | question: candidate (unreviewed); answer: candidate (unreviewed) |  |
| VIS-6116-1.2.6-11 | stimulus_image | partial | teaching: variant to prepare; question: candidate (unreviewed); answer: variant to prepare; unfamiliar_example: candidate (unreviewed) | calibration value for graticule, cell membrane, cell membrane and cytoplasm detail at this magnification, cell wall (correctly absent), chlo |
| VIS-6116-1.2.6-12 | model_drawing | GAP | model_drawing: GAP; marking_criteria: GAP |  |
| VIS-6116-1.2.6-12 | stimulus_image | partial | teaching: variant to prepare; question: candidate (unreviewed); answer: variant to prepare; unfamiliar_example: candidate (unreviewed) | cell membrane, cell wall (correctly absent), chloroplast (correctly absent), cytoplasm, distinct chloroplasts (stained purple, not resolved) |
| VIS-6116-1.2.6-12 | teaching_diagram | every need has a candidate (unreviewed) | teaching: candidate (unreviewed) | xylem and phloem distinguished |
| VIS-6116-1.2.6-13 | stimulus_image | partial | teaching: variant to prepare; question: candidate (unreviewed); answer: variant to prepare; unfamiliar_example: candidate (unreviewed) | cell membrane and cytoplasm detail at this magnification, prophase I, meiosis II |
| VIS-6116-1.2.6-14 | stimulus_image | partial | teaching: candidate (unreviewed); question: candidate (unreviewed); answer: variant to prepare; unfamiliar_example: candidate (unreviewed) | beaker of water, calibration value for graticule, cytoplasm detail, liquid and meniscus to read, scale for reading level, value of each divi |
| VIS-6116-2.1-04 | stimulus_image | partial | teaching: variant to prepare; question: candidate (unreviewed); answer: variant to prepare; unfamiliar_example: candidate (unreviewed) | abdomen partly hidden behind legs, antennae hard to see from front view, antennae very small, chaetae (too small), clitellum not obvious, cl |
| VIS-6116-2.2-01 | teaching_diagram | every need has a candidate (unreviewed) | teaching: candidate (unreviewed) | word labels (numbered circles only), word labels (numbers only; key in Commons description) |
| VIS-6116-2.2-03 | stimulus_image | partial | teaching: candidate (unreviewed); question: candidate (unreviewed); answer: variant to prepare; unfamiliar_example: candidate (unreviewed) | feathery stigmas (silks) not shown, flowers, seeds, flowers, seeds, roots, parallel veins not emphasised, pollen not visible, roots (fibrous |
| VIS-6116-2.2-03 | teaching_diagram | every need has a candidate (unreviewed) | teaching: candidate (unreviewed) | parallel veins not emphasised, roots (fibrous vs tap root) missing, seed shown only as cartoon, seed with single cotyledon, whole-plant feat |
| VIS-6116-2.2-04 | stimulus_image | partial | teaching: candidate (unreviewed); question: candidate (unreviewed); answer: variant to prepare; unfamiliar_example: candidate (unreviewed) | flowers, leaves, flowers, roots, roots (fibrous vs tap root) missing, seed (two cotyledons) and tap root not shown, seed shown only as carto |
| VIS-6116-2.2-04 | teaching_diagram | every need has a candidate (unreviewed) | teaching: candidate (unreviewed) | leaves, flowers, roots, roots (fibrous vs tap root) missing, seed shown only as cartoon |
| VIS-6116-2.2-05 | stimulus_image | partial | teaching: candidate (unreviewed); question: candidate (unreviewed); answer: variant to prepare; unfamiliar_example: candidate (unreviewed) | external shell (absent in octopus; useful contrast), head, soft muscular foot, tentacles/eyes |
| VIS-6116-2.2-05 | teaching_diagram | every need has a candidate (unreviewed) | teaching: candidate (unreviewed) |  |
| VIS-6116-2.2-06 | stimulus_image | partial | teaching: candidate (unreviewed); question: candidate (unreviewed); answer: variant to prepare; unfamiliar_example: candidate (unreviewed) | chaetae (bristles) not labelled, chaetae (too small), clitellum, clitellum not obvious, clitellum not visible, mouth/prostomium detail, suck |
| VIS-6116-2.2-06 | teaching_diagram | every need has a candidate (unreviewed) | teaching: candidate (unreviewed) | chaetae (bristles) not labelled, clitellum |
| VIS-6116-2.2-07 | stimulus_image | partial | teaching: candidate (unreviewed); question: candidate (unreviewed); answer: variant to prepare; unfamiliar_example: candidate (unreviewed) | antennae hard to see from front view, compound eyes small, far-side legs hidden, third pair of legs partly hidden in shadow, word labels (nu |
| VIS-6116-2.2-07 | teaching_diagram | every need has a candidate (unreviewed) | teaching: candidate (unreviewed) | word labels (numbers 1-32 only; key on Commons page) |
| VIS-6116-2.2-08 | stimulus_image | partial | teaching: candidate (unreviewed); question: candidate (unreviewed); answer: variant to prepare; unfamiliar_example: candidate (unreviewed) | abdomen partly hidden behind legs, fangs/chelicerae not visible, no antennae (correctly absent), tail and sting cut off at top edge |
| VIS-6116-2.2-08 | teaching_diagram | every need has a candidate (unreviewed) | teaching: candidate (unreviewed) |  |
| VIS-6116-2.2-09 | stimulus_image | partial | teaching: variant to prepare; question: candidate (unreviewed); answer: variant to prepare; unfamiliar_example: candidate (unreviewed) | abdomen and tail fan largely hidden, antennae very small, body regions unclear, dorsal carapace not seen (front-ventral view), long antennae |
| VIS-6116-2.2-09 | teaching_diagram | GAP | teaching: GAP |  |
| VIS-6116-2.2-10 | stimulus_image | partial | teaching: variant to prepare; question: candidate (unreviewed); answer: variant to prepare; unfamiliar_example: candidate (unreviewed) | detail of two leg pairs per segment requires zoom, poison claws (forcipules) not clearly seen, two pairs of legs per segment not resolvable |
| VIS-6116-2.2-10 | teaching_diagram | GAP | teaching: GAP |  |
| VIS-6116-2.2-11 | stimulus_image | partial | teaching: variant to prepare; question: candidate (unreviewed); answer: variant to prepare; unfamiliar_example: candidate (unreviewed) |  |
| VIS-6116-2.2-11 | teaching_diagram | GAP | teaching: GAP |  |
| VIS-6116-2.2-12 | stimulus_image | partial | teaching: variant to prepare; question: candidate (unreviewed); answer: variant to prepare; unfamiliar_example: candidate (unreviewed) | hind body and webbing out of frame, hind limbs and webbed feet largely hidden, tympanum not clearly distinguished, webbing not visible |
| VIS-6116-2.2-12 | teaching_diagram | GAP | teaching: GAP |  |
| VIS-6116-2.2-13 | stimulus_image | partial | teaching: variant to prepare; question: candidate (unreviewed); answer: variant to prepare; unfamiliar_example: candidate (unreviewed) | external ear opening absent in chameleons, tail hidden |
| VIS-6116-2.2-13 | teaching_diagram | GAP | teaching: GAP |  |
| VIS-6116-2.2-14 | stimulus_image | partial | teaching: variant to prepare; question: candidate (unreviewed); answer: variant to prepare; unfamiliar_example: candidate (unreviewed) | anthers/stigma not clearly resolved, feet/claws partly hidden in grass, pollen on bird not visible, wings folded |
| VIS-6116-2.2-14 | teaching_diagram | GAP | teaching: GAP |  |
| VIS-6116-2.2-15 | stimulus_image | partial | teaching: variant to prepare; question: candidate (unreviewed); answer: variant to prepare; unfamiliar_example: candidate (unreviewed) | mammary glands not discernible, mammary glands not visible, whiskers/vibrissae not visible |
| VIS-6116-2.2-15 | teaching_diagram | GAP | teaching: GAP |  |
| VIS-6116-2.2-16 | model_drawing | GAP | model_drawing: GAP; marking_criteria: GAP |  |
| VIS-6116-2.2-16 | teaching_diagram | GAP | teaching: GAP |  |
| VIS-6116-3.1-01 | stimulus_image | partial | teaching: candidate (unreviewed); question: candidate (unreviewed); answer: variant to prepare; unfamiliar_example: candidate (unreviewed) | calibration value for graticule, cell membrane and cytoplasm detail at this magnification, cell membrane labelled, cytoplasm detail, interna |
| VIS-6116-3.2-01 | stimulus_image | partial | teaching: candidate (unreviewed); question: candidate (unreviewed); answer: variant to prepare; unfamiliar_example: candidate (unreviewed) | cell membrane, cell membrane and cytoplasm detail at this magnification, cell wall (correctly absent), chloroplast (correctly absent), disti |
| VIS-6116-3.2-01 | teaching_diagram | every need has a candidate (unreviewed) | teaching: candidate (unreviewed) | phloem (source description says vascular tissue omitted), vacuole (small vacuoles in liver cell not shown), xylem |
| VIS-6116-3.2-02 | stimulus_image | partial | teaching: candidate (unreviewed); question: candidate (unreviewed); answer: variant to prepare; unfamiliar_example: candidate (unreviewed) | cell membrane, cell wall (correctly absent), chloroplast (correctly absent), distinct chloroplasts (stained purple, not resolved), nucleus,  |
| VIS-6116-3.2-03 | model_drawing | GAP | model_drawing: GAP; marking_criteria: GAP |  |
| VIS-6116-3.2-03 | stimulus_image | partial | teaching: variant to prepare; question: candidate (unreviewed); answer: variant to prepare; unfamiliar_example: candidate (unreviewed) | calibration value for graticule, cell membrane, cytoplasm, cytoplasm detail, nucleus, vacuole, vacuole boundary |
| VIS-6116-3.2-03 | teaching_diagram | GAP | teaching: GAP |  |
| VIS-6116-3.2-04 | model_drawing | GAP | model_drawing: GAP; marking_criteria: GAP |  |
| VIS-6116-3.2-04 | stimulus_image | partial | teaching: variant to prepare; question: candidate (unreviewed); answer: variant to prepare; unfamiliar_example: candidate (unreviewed) | cilia (not resolvable at this magnification), goblet cells not clearly distinguishable, several nuclei |
| VIS-6116-3.2-04 | teaching_diagram | GAP | teaching: GAP |  |
| VIS-6116-3.2-05 | stimulus_image | partial | teaching: candidate (unreviewed); question: candidate (unreviewed); answer: variant to prepare; unfamiliar_example: candidate (unreviewed) | free ribosomes clearly resolved, individually resolved ribosomes, ribosomes not labelled |
| VIS-6116-3.2-06 | stimulus_image | partial | teaching: candidate (unreviewed); question: candidate (unreviewed); answer: variant to prepare; unfamiliar_example: candidate (unreviewed) | free ribosomes clearly resolved, individually resolved ribosomes |
| VIS-6116-3.2-07 | stimulus_image | partial | teaching: candidate (unreviewed); question: candidate (unreviewed); answer: variant to prepare; unfamiliar_example: candidate (unreviewed) | individually resolved ribosomes, ribosomes not labelled |
| VIS-6116-3.2-08 | stimulus_image | partial | teaching: candidate (unreviewed); question: candidate (unreviewed); answer: variant to prepare; unfamiliar_example: candidate (unreviewed) | individually resolved ribosomes, ribosomes not labelled |
| VIS-6116-3.2-10 | stimulus_image | partial | teaching: candidate (unreviewed); question: candidate (unreviewed); answer: variant to prepare; unfamiliar_example: candidate (unreviewed) | cilia (not resolvable at this magnification), goblet cells not clearly distinguishable, pictures of each level, several nuclei |
| VIS-6116-3.2-10 | teaching_diagram | every need has a candidate (unreviewed) | teaching: candidate (unreviewed) | pictures of each level |
| VIS-6116-3.3.2-01 | stimulus_image | partial | teaching: candidate (unreviewed); question: candidate (unreviewed); answer: variant to prepare; unfamiliar_example: candidate (unreviewed) | cell membrane label, cell membrane labelled, nucleus, plasmolysis gap in hypertonic cell, vacuole outline |
| VIS-6116-3.3.2-01 | teaching_diagram | every need has a candidate (unreviewed) | teaching: candidate (unreviewed) | cell membrane label, plasmolysis gap in hypertonic cell |
| VIS-6116-3.3.2-02 | teaching_diagram | every need has a candidate (unreviewed) | teaching: candidate (unreviewed) |  |
| VIS-6116-3.3.2-03 | stimulus_image | partial | teaching: candidate (unreviewed); question: candidate (unreviewed); answer: variant to prepare; unfamiliar_example: candidate (unreviewed) | cell membrane label, cell membrane labelled, nucleus, vacuole outline |
| VIS-6116-3.3.2-04 | graph | every need has a candidate (unreviewed) | question: candidate (unreviewed); answer: candidate (unreviewed) |  |
| VIS-6116-3.3.2-04 | stimulus_image | partial | teaching: candidate (unreviewed); question: candidate (unreviewed); answer: variant to prepare; unfamiliar_example: candidate (unreviewed) | beaker of water, cell membrane labelled, change in level over time, nucleus, scale for reading level, water movement |
| VIS-6116-3.4-09 | teaching_diagram | every need has a candidate (unreviewed) | teaching: candidate (unreviewed) |  |
| VIS-6116-3.5-04 | graph | every need has a candidate (unreviewed) | question: candidate (unreviewed); answer: candidate (unreviewed) |  |
| VIS-6116-3.5-05 | graph | every need has a candidate (unreviewed) | question: candidate (unreviewed); answer: candidate (unreviewed) |  |
| VIS-6116-3.6.1.1-01 | stimulus_image | partial | teaching: candidate (unreviewed); question: candidate (unreviewed); answer: variant to prepare; unfamiliar_example: candidate (unreviewed) | air spaces label, distinct chloroplasts (stained purple, not resolved), guard cells (not clearly visible), phloem (source description says v |
| VIS-6116-3.6.1.1-01 | teaching_diagram | every need has a candidate (unreviewed) | teaching: candidate (unreviewed) | air spaces label, phloem (source description says vascular tissue omitted), vascular bundle (xylem, phloem), xylem |
| VIS-6116-3.6.1.1-06 | stimulus_image | partial | teaching: variant to prepare; question: candidate (unreviewed); answer: variant to prepare; unfamiliar_example: candidate (unreviewed) | clearly identifiable stomata |
| VIS-6116-3.6.1.1-07 | model_drawing | GAP | model_drawing: GAP; marking_criteria: GAP |  |
| VIS-6116-3.6.1.1-07 | stimulus_image | partial | teaching: candidate (unreviewed); question: candidate (unreviewed); answer: variant to prepare; unfamiliar_example: candidate (unreviewed) | air spaces label, clear epidermis, distinct chloroplasts (stained purple, not resolved), guard cells (not clearly visible), spongy mesophyll |
| VIS-6116-3.6.1.1-07 | teaching_diagram | every need has a candidate (unreviewed) | teaching: candidate (unreviewed) | air spaces label, vascular bundle (xylem, phloem) |
| VIS-6116-3.6.1.3-04 | graph | every need has a candidate (unreviewed) | question: candidate (unreviewed); answer: candidate (unreviewed) |  |
| VIS-6116-3.6.1.3-05 | graph | every need has a candidate (unreviewed) | question: candidate (unreviewed); answer: candidate (unreviewed) |  |
| VIS-6116-3.6.1.3-10 | graph | every need has a candidate (unreviewed) | question: candidate (unreviewed); answer: candidate (unreviewed) |  |
| VIS-6116-3.6.2.2-06 | teaching_diagram | every need has a candidate (unreviewed) | teaching: candidate (unreviewed) | no labels for functions (ingestion/digestion/absorption/egestion) - add in teaching text, sphincters not shown |
| VIS-6116-3.6.2.4-01 | teaching_diagram | every need has a candidate (unreviewed) | teaching: candidate (unreviewed) | arteriole/venule not distinguished, blood supply, capillaries, epithelium not named as such, lacteal, microvilli, no context of small intest |
| VIS-6116-3.6.2.4-03 | teaching_diagram | every need has a candidate (unreviewed) | teaching: candidate (unreviewed) | arteriole/venule not distinguished, blood supply, capillaries, epithelium not named as such, lacteal, microvilli, no context of small intest |
| VIS-6116-3.7-01 | stimulus_image | partial | teaching: variant to prepare; question: candidate (unreviewed); answer: variant to prepare; unfamiliar_example: candidate (unreviewed) | cortex, xylem, phloem, epidermis, internal tissues, phloem detail, root hairs |
| VIS-6116-3.7-01 | teaching_diagram | every need has a candidate (unreviewed) | teaching: candidate (unreviewed) | cortex, xylem, phloem |
| VIS-6116-3.7-02 | stimulus_image | partial | teaching: variant to prepare; question: candidate (unreviewed); answer: variant to prepare; unfamiliar_example: candidate (unreviewed) | xylem and phloem distinguished |
| VIS-6116-3.7-02 | teaching_diagram | every need has a candidate (unreviewed) | teaching: candidate (unreviewed) | xylem and phloem distinguished |
| VIS-6116-3.7-03 | model_drawing | GAP | model_drawing: GAP; marking_criteria: GAP |  |
| VIS-6116-3.7-03 | stimulus_image | partial | teaching: variant to prepare; question: candidate (unreviewed); answer: variant to prepare; unfamiliar_example: candidate (unreviewed) | epidermis, phloem detail, root hairs |
| VIS-6116-3.7-03 | teaching_diagram | GAP | teaching: GAP |  |
| VIS-6116-3.7-12 | stimulus_image | partial | teaching: variant to prepare; question: candidate (unreviewed); answer: variant to prepare; unfamiliar_example: candidate (unreviewed) | clearly identifiable stomata |
| VIS-6116-3.8.1-01 | teaching_diagram | every need has a candidate (unreviewed) | teaching: candidate (unreviewed) | chordae tendineae not labelled, coronary arteries, inferior vena cava, key exists only in Commons description (includes Latin), no differenc |
| VIS-6116-3.8.1-02 | model_drawing | GAP | model_drawing: GAP; marking_criteria: GAP |  |
| VIS-6116-3.8.1-02 | teaching_diagram | every need has a candidate (unreviewed) | teaching: candidate (unreviewed) | inferior vena cava, no labels, pulmonary veins |
| VIS-6116-3.8.1-03 | teaching_diagram | every need has a candidate (unreviewed) | teaching: candidate (unreviewed) | capillary, comparison with vein/capillary, elastic fibres not named, relative wall thickness not explicitly labelled, valve not drawn, only  |
| VIS-6116-3.8.1-04 | teaching_diagram | every need has a candidate (unreviewed) | teaching: candidate (unreviewed) | capillary, elastic fibres not named, relative wall thickness not explicitly labelled, valve not drawn, only stated in label, vein valve |
| VIS-6116-3.8.1-05 | teaching_diagram | every need has a candidate (unreviewed) | teaching: candidate (unreviewed) | elastic fibres not named, relative wall thickness not explicitly labelled, valve not drawn, only stated in label |
| VIS-6116-3.8.1-06 | teaching_diagram | every need has a candidate (unreviewed) | teaching: candidate (unreviewed) | chambers, chambers not named, chordae tendineae not labelled, coronary arteries, heart chambers not shown, no colour for oxygenated/deoxygen |
| VIS-6116-3.8.2-01 | stimulus_image | partial | teaching: variant to prepare; question: candidate (unreviewed); answer: variant to prepare; unfamiliar_example: candidate (unreviewed) | lymphocyte, no nucleus visible, not a light micrograph, phagocyte |
| VIS-6116-3.8.2-01 | teaching_diagram | GAP | teaching: GAP |  |
| VIS-6116-3.8.2-06 | stimulus_image | partial | teaching: variant to prepare; question: candidate (unreviewed); answer: variant to prepare; unfamiliar_example: candidate (unreviewed) | phagocyte |
| VIS-6116-3.8.2-07 | stimulus_image | partial | teaching: variant to prepare; question: candidate (unreviewed); answer: variant to prepare; unfamiliar_example: candidate (unreviewed) | lymphocyte |
| VIS-6116-3.9-02 | teaching_diagram | every need has a candidate (unreviewed) | teaching: candidate (unreviewed) | intercostal muscles, ribs, thin wall not labelled, thin wall not shown in section, ventilation, ventilation not shown |
| VIS-6116-3.9-03 | teaching_diagram | every need has a candidate (unreviewed) | teaching: candidate (unreviewed) | external intercostals, internal intercostal muscles, internal intercostals, no function arrows, no labels |
| VIS-6116-3.9-07 | graph | every need has a candidate (unreviewed) | question: candidate (unreviewed); answer: candidate (unreviewed) |  |
| VIS-6116-3.11-04 | stimulus_image | partial | teaching: candidate (unreviewed); question: candidate (unreviewed); answer: variant to prepare; unfamiliar_example: candidate (unreviewed) |  |
| VIS-6116-3.11-04 | teaching_diagram | every need has a candidate (unreviewed) | teaching: candidate (unreviewed) |  |
| VIS-6116-3.13.1-01 | stimulus_image | partial | teaching: candidate (unreviewed); question: GAP; answer: GAP; unfamiliar_example: GAP | motor/sensory/relay classification, myelin, part labels, sensory, relay, motor terms |
| VIS-6116-3.13.1-01 | teaching_diagram | every need has a candidate (unreviewed) | teaching: candidate (unreviewed) | motor/sensory/relay classification, myelin, part labels, sensory, relay, motor terms |
| VIS-6116-3.13.1-04 | teaching_diagram | every need has a candidate (unreviewed) | teaching: candidate (unreviewed) | motor/sensory/relay classification, receptors, vesicles |
| VIS-6116-3.13.1-07 | teaching_diagram | every need has a candidate (unreviewed) | teaching: candidate (unreviewed) | relay neurone |
| VIS-6116-3.13.1-08 | model_drawing | GAP | model_drawing: GAP; marking_criteria: GAP |  |
| VIS-6116-3.13.1-08 | stimulus_image | partial | teaching: candidate (unreviewed); question: candidate (unreviewed); answer: variant to prepare; unfamiliar_example: candidate (unreviewed) | central canal, dorsal root ganglion, whole section |
| VIS-6116-3.13.1-08 | teaching_diagram | every need has a candidate (unreviewed) | teaching: candidate (unreviewed) | dorsal root ganglion |
| VIS-6116-3.13.1-11 | teaching_diagram | every need has a candidate (unreviewed) | teaching: candidate (unreviewed) | blind spot |
| VIS-6116-3.13.1-12 | teaching_diagram | every need has a candidate (unreviewed) | teaching: candidate (unreviewed) | blind spot |
| VIS-6116-3.13.1-13 | teaching_diagram | every need has a candidate (unreviewed) | teaching: candidate (unreviewed) | blind spot |
| VIS-6116-3.13.1-14 | teaching_diagram | every need has a candidate (unreviewed) | teaching: candidate (unreviewed) | blind spot, ciliary muscle, cornea, iris, pupil, ciliary labels hidden in thumbnail, other eye parts unlabelled, suspensory ligaments |
| VIS-6116-3.13.1-15 | teaching_diagram | every need has a candidate (unreviewed) | teaching: candidate (unreviewed) | blind spot, cornea, iris, pupil, ciliary labels hidden in thumbnail |
| VIS-6116-3.13.1-16 | teaching_diagram | every need has a candidate (unreviewed) | teaching: candidate (unreviewed) | blind spot, cornea, iris, pupil, ciliary labels hidden in thumbnail |
| VIS-6116-3.13.1-17 | teaching_diagram | every need has a candidate (unreviewed) | teaching: candidate (unreviewed) | cornea, iris, pupil, ciliary labels hidden in thumbnail |
| VIS-6116-3.13.1-18 | teaching_diagram | GAP | teaching: GAP |  |
| VIS-6116-3.13.1-19 | teaching_diagram | every need has a candidate (unreviewed) | teaching: candidate (unreviewed) | blind spot, ciliary muscle, labels for ciliary muscle and suspensory ligaments, other eye parts unlabelled, suspensory ligaments |
| VIS-6116-3.13.1-20 | teaching_diagram | GAP | teaching: GAP |  |
| VIS-6116-3.13.3-02 | teaching_diagram | every need has a candidate (unreviewed) | teaching: candidate (unreviewed) | hormone names |
| VIS-6116-3.13.3-03 | teaching_diagram | every need has a candidate (unreviewed) | teaching: candidate (unreviewed) | hormone names |
| VIS-6116-3.13.3-04 | teaching_diagram | every need has a candidate (unreviewed) | teaching: candidate (unreviewed) | 'testosterone' named explicitly, hormone names |
| VIS-6116-3.13.3-05 | teaching_diagram | every need has a candidate (unreviewed) | teaching: candidate (unreviewed) | 'testosterone' named explicitly, hormone names |
| VIS-6116-4.1-04 | stimulus_image | partial | teaching: candidate (unreviewed); question: candidate (unreviewed); answer: variant to prepare; unfamiliar_example: candidate (unreviewed) |  |
| VIS-6116-4.1-05 | stimulus_image | partial | teaching: variant to prepare; question: candidate (unreviewed); answer: variant to prepare; unfamiliar_example: candidate (unreviewed) |  |
| VIS-6116-4.1-07 | model_drawing | GAP | model_drawing: GAP; marking_criteria: GAP |  |
| VIS-6116-4.1-07 | stimulus_image | partial | teaching: variant to prepare; question: candidate (unreviewed); answer: variant to prepare; unfamiliar_example: candidate (unreviewed) | clear meiotic stage, prophase I, meiosis II |
| VIS-6116-4.1-07 | teaching_diagram | GAP | teaching: GAP |  |
| VIS-6116-4.2.2-03 | stimulus_image | partial | teaching: candidate (unreviewed); question: candidate (unreviewed); answer: variant to prepare; unfamiliar_example: candidate (unreviewed) | anthers/stigma not clearly resolved, no explicit adaptation notes (e.g. scent, sticky pollen), no wind-pollinated comparison, ovary hidden,  |
| VIS-6116-4.2.2-03 | teaching_diagram | every need has a candidate (unreviewed) | teaching: candidate (unreviewed) | no explicit adaptation notes (e.g. scent, sticky pollen), no wind-pollinated comparison |
| VIS-6116-4.2.2-04 | stimulus_image | partial | teaching: candidate (unreviewed); question: candidate (unreviewed); answer: variant to prepare; unfamiliar_example: candidate (unreviewed) | anthers (male flowers elsewhere on plant), anthers not yet emerged, feathery stigmas (silks) not shown, feathery stigmas not clearly visible |
| VIS-6116-4.2.2-04 | teaching_diagram | every need has a candidate (unreviewed) | teaching: candidate (unreviewed) | parallel veins not emphasised, seed with single cotyledon, word labels (none) |
| VIS-6116-4.2.2-05 | model_drawing | GAP | model_drawing: GAP; marking_criteria: GAP |  |
| VIS-6116-4.2.2-05 | teaching_diagram | every need has a candidate (unreviewed) | teaching: candidate (unreviewed) | no explicit adaptation notes (e.g. scent, sticky pollen), no wind-pollinated comparison |
| VIS-6116-4.2.2-06 | model_drawing | GAP | model_drawing: GAP; marking_criteria: GAP |  |
| VIS-6116-4.2.2-06 | teaching_diagram | every need has a candidate (unreviewed) | teaching: candidate (unreviewed) | no explicit adaptation notes (e.g. scent, sticky pollen), no wind-pollinated comparison, parallel veins not emphasised, seed with single cot |
| VIS-6116-4.2.2-07 | teaching_diagram | GAP | teaching: GAP |  |
| VIS-6116-4.3.1-01 | teaching_diagram | every need has a candidate (unreviewed) | teaching: candidate (unreviewed) | corpus luteum, corpus luteum not named, exchange arrows for gases/nutrients/wastes, hormone production not shown, placenta / pregnancy not s |
| VIS-6116-4.3.2-01 | stimulus_image | partial | teaching: candidate (unreviewed); question: candidate (unreviewed); answer: variant to prepare; unfamiliar_example: GAP | no labels |
| VIS-6116-4.3.2-01 | teaching_diagram | every need has a candidate (unreviewed) | teaching: candidate (unreviewed) |  |
| VIS-6116-4.3.2-02 | stimulus_image | partial | teaching: candidate (unreviewed); question: candidate (unreviewed); answer: variant to prepare; unfamiliar_example: candidate (unreviewed) | endometrium not labelled, no labels, urethra/bladder |
| VIS-6116-4.3.2-02 | teaching_diagram | every need has a candidate (unreviewed) | teaching: candidate (unreviewed) | endometrium not labelled, urethra/bladder |
| VIS-6116-4.3.2-04 | teaching_diagram | every need has a candidate (unreviewed) | teaching: candidate (unreviewed) | amniotic sac/fluid not labelled, exchange arrows for gases/nutrients/wastes, hormone production not shown, maternal/fetal blood exchange not |
| VIS-6116-4.3.5-08 | graph | every need has a candidate (unreviewed) | question: candidate (unreviewed); answer: candidate (unreviewed) |  |
| VIS-6116-4.4.4-03 | stimulus_image | partial | teaching: candidate (unreviewed); question: candidate (unreviewed); answer: variant to prepare; unfamiliar_example: candidate (unreviewed) | leaf stalk, air spaces, stomata on upper surface not visible, root mass under water, stomata on upper surface not distinguishable at this si |
| VIS-6116-4.4.4-03 | teaching_diagram | every need has a candidate (unreviewed) | teaching: candidate (unreviewed) | stomata on upper surface not distinguishable at this size |
| VIS-6116-4.4.4-04 | stimulus_image | partial | teaching: variant to prepare; question: candidate (unreviewed); answer: variant to prepare; unfamiliar_example: candidate (unreviewed) | bird is small and partly hidden, close-up of spines/waxy surface, close-up of waxy cuticle/leaf surface, deep tap root (underground), habita |
| VIS-6116-4.4.4-04 | teaching_diagram | GAP | teaching: GAP |  |
| VIS-6116-5.1-10 | graph | every need has a candidate (unreviewed) | question: candidate (unreviewed); answer: candidate (unreviewed) |  |
| VIS-6116-5.1-11 | graph | every need has a candidate (unreviewed) | question: candidate (unreviewed); answer: candidate (unreviewed) |  |
| VIS-6116-5.1-11 | teaching_diagram | every need has a candidate (unreviewed) | teaching: candidate (unreviewed) | no pyramid, no text labels for producer/primary/secondary/tertiary/quaternary, no text labels for trophic levels, pyramid of numbers and pyr |
| VIS-6116-5.1-14 | graph | every need has a candidate (unreviewed) | question: candidate (unreviewed); answer: candidate (unreviewed) |  |
| VIS-6116-5.2-01 | teaching_diagram | every need has a candidate (unreviewed) | teaching: candidate (unreviewed) | Haber process/fertiliser, animals feeding on plants shown only as a rabbit without arrow label, lightning fixation |
| VIS-6116-5.2-06 | teaching_diagram | every need has a candidate (unreviewed) | teaching: candidate (unreviewed) | no explicit labels for photosynthesis, respiration, decomposition or combustion processes |
| VIS-6116-5.3-05 | graph | every need has a candidate (unreviewed) | question: candidate (unreviewed); answer: candidate (unreviewed) |  |
| VIS-6116-5.3-08 | graph | every need has a candidate (unreviewed) | question: candidate (unreviewed); answer: candidate (unreviewed) |  |
| VIS-6116-5.3-08 | stimulus_image | partial | teaching: candidate (unreviewed); question: GAP; answer: GAP; unfamiliar_example: GAP |  |
