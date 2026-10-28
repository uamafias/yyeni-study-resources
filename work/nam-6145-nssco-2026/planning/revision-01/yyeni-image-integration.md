# 6145 diagram attachment design — checked 28 October 2026

Read-only live tool: YYeni get_flashcard_contracts. It exposes question_asset_id and answer_asset_id as optional managed image IDs; question/answer are Markdown and LaTeX. The app uses question_image_url and answer_image_url. The teacher AddCardModal obtains url/publicUrl from /api/chat/upload-lesson-res, PUTs the image to GCS and saves publicUrl. Learner practice.js and workout.js render the URLs on their respective sides.

Do not infer that arbitrary GCS objects are accepted as MCP managed assets. Use import_flashcard_image or the supported managed render flow at the later import stage; record actual returned IDs. No image was rendered or imported through the connected app in this planning pass. No storage bucket/ACL or deployed UI acceptance was tested.

Repository canonical learning items have no native asset_id fields. A sidecar mapping must join each repository item ID to question/answer PNGs and later managed IDs. This file is an integration observation, not a claim that image assets exist.
