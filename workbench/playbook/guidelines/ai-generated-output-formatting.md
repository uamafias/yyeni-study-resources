# AI-Generated Output Formatting

This is the YYeni contract for any AI-generated text that reaches a user. It exists because raw JSON, escaped newlines, broken Markdown, and unrendered LaTeX make learner and teacher experiences feel unfinished.

Detailed mathematical syntax, escaping, renderer behaviour and known legacy gaps are consolidated in [Platform LaTeX generation and rendering](latex-generation-and-rendering.md).

## Non-negotiable rule

If an AI-generated response may be displayed to a learner, teacher, parent, school rep, or superadmin, the backend prompt, parser, and frontend renderer must be designed together.

Do not ship a prompt-only change and assume the UI will make it readable. Do not ship a UI-only renderer and assume the model will format cleanly.

## Backend prompt standard

- Reuse the shared LaTeX rules from `services/api/services/math_formatting_instructions.py::LATEX_FORMATTING_INSTRUCTION` whenever math, science notation, formulas, equations, units, chemistry symbols, or worked calculations can appear.
- Do not duplicate or rewrite those LaTeX rules inside one-off prompts. If the standard needs to improve, improve the shared constant.
- Tell the model to produce user-facing prose in clear Markdown with proper paragraph breaks, lists, and headings where helpful.
- If the model returns structured JSON, schema fields such as `assistant_reply`, `feedback`, `suggested_next_steps`, `video_search_queries`, or internal labels are for parsing only. They must never be visible in the learner or teacher UI.
- Keep user-facing text free of AI model names and provider names.

## Backend parsing standard

- Treat every LLM response as untrusted, even when the prompt asks for JSON.
- Defensively parse, coerce, and validate structured output before it reaches a route response.
- Unwrap JSON envelopes and Markdown code fences before display.
- Normalize escaped newlines and LaTeX escapes so the frontend receives normal Markdown/LaTeX text, not raw transport artifacts.
- Strip visible schema metadata before returning or persisting user-facing assistant messages.
- Add regression coverage for malformed JSON, nested JSON strings, escaped `\n`, raw field-name leakage, and LaTeX that must render.

## Frontend rendering standard

- Render user-facing AI Markdown/LaTeX through `MathMarkdown` or an equivalent safe renderer using ReactMarkdown, `remark-math`, and KaTeX.
- For untrusted AI output, use `allowHtml={false}` and `allowImages={false}` unless the surface has a deliberate safe-image policy.
- Do not render AI-generated Markdown/LaTeX as raw text in a plain `<div>`, `<p>`, or textarea preview.
- Preserve visual hierarchy: paragraphs should breathe, headings should be real headings, lists should be lists, and calculations should render as math instead of raw slash commands.
- Add frontend tests for any formatter/normalizer that protects a user-facing AI surface.

## Review checklist

Before approving a PR that displays AI-generated text, verify:

- The prompt imports or otherwise uses the shared `LATEX_FORMATTING_INSTRUCTION` when notation can appear.
- Structured AI output is parsed defensively and internal schema labels cannot leak into the UI.
- The frontend surface renders Markdown and LaTeX through `MathMarkdown` or an equivalent safe renderer.
- Tests cover malformed model output, metadata leakage, and LaTeX rendering.
- The feature changelog notes the user-facing AI output behavior if the feature was meaningfully touched.
