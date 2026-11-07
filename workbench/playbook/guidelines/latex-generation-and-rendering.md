# Platform LaTeX generation and rendering

Extracted from the current codebase on 1 November 2026. Applies to questions, answers, worked solutions, marking feedback, tutoring, dictation previews and history across subjects. This reference consolidates existing contracts and distinguishes their requirements from legacy implementation gaps. Creating it does not change runtime behaviour.

## Sources and ownership

| Responsibility | Authoritative implementation / reference |
|---|---|
| Shared AI generation instructions | `services/api/services/math_formatting_instructions.py::LATEX_FORMATTING_INSTRUCTION` |
| End-to-end prompt, parsing and display contract | `docs/conventions/ai-generated-output-formatting.md` |
| Shared frontend renderer | `apps/web/components/MathMarkdown.js` |
| Structured-output LaTeX escape repair | `services/api/services/llm_json_repair.py` |
| General Markdown conventions | `apps/web/MARKDOWN_FORMATTING_GUIDELINES.md` |
| Frontend dictation prompt mirror | `apps/web/lib/dictation/latexFormattingInstruction.js` |

Change the shared prompt constant when changing generation rules; do not introduce independent prompt variants. The frontend dictation copy must match it exactly (`answerDictationHelpers.test.js` checks parity). Feature-specific pedagogy and layout may add requirements without changing mathematical syntax or transport semantics.

## 1. Generation rules

- Import and append `LATEX_FORMATTING_INSTRUCTION` whenever maths/science notation, equations, units, chemistry or worked calculations may appear. This includes user-facing feedback and grader-facing mathematical fields.
- Emit normal Markdown containing LaTeX, not HTML wrappers or a code block containing the whole response. When the API requires JSON, emit valid JSON only; the mathematical Markdown belongs inside its text fields.
- Use `$...$` for inline maths, separated from surrounding words by spaces. Example: `The value $x = 5$ satisfies the equation.`
- Use `$$...$$` for a key equation on its own line, with blank lines before and after. Do not place display maths in the middle of a sentence.
- Pair delimiters and braces. Keep ordinary explanatory words outside math mode; use `\text{...}` for words that genuinely belong inside an expression.
- Never wrap maths or a sentence containing maths in Markdown bold, italic or underline. Forbidden: `**$5y$**`, `*$x$*`, `__$x$__`, `**The answer is $x+2$**`. Bold the separate prose label, or introduce the result with “Note that” / “Important”. Mathematical notation such as `\mathbf{v}` is distinct from Markdown emphasis.
- Escape literal dollar signs in Markdown (`\$`). Currency such as `N$20` must remain currency, not accidentally open a mathematical span.
- Prefer clear, correctly rendered mathematical notation over decorative emphasis. A plain number or an isolated word does not need to become a display equation merely because it appears in a mathematical explanation.
- Before returning output, check delimiter pairing, absence of Markdown emphasis around maths and correct escaping for the actual output format.

## 2. Required notation vocabulary

These examples are **decoded Markdown**, not JSON strings.

| Use | Markdown / LaTeX |
|---|---|
| Fractions | `$\frac{a}{b}$` |
| Powers | `$x^2$`, `$x^{n+1}$` |
| Square / cube roots | `$\sqrt{x}$`, `$\sqrt[3]{x}$` |
| Sum | `$\sum_{i=1}^{n} i^2$` |
| Integral | `$\int_0^1 x^2 dx$` |
| Matrix; row separator is two backslashes | `$\begin{pmatrix} a & b \\ c & d \end{pmatrix}$` |
| Vectors | `$\vec{F}$`, `$\mathbf{v}$` |
| Units: spacing and upright text | `$5\text{ m/s}^2$` |
| Greek letters | `$\alpha$`, `$\beta$`, `$\gamma$`, `$\Delta$`, `$\omega$` |
| Physics | `$E=mc^2$`, `$F=ma$`, `$KE=\frac{1}{2}mv^2$` |
| Chemical formula | `$\text{H}_2\text{O}$` |
| Reaction / equilibrium | `$\rightarrow$`, `$\rightleftharpoons$` |
| Ions | `$\text{Na}^+$`, `$\text{SO}_4^{2-}$` |
| Rate equation | `$\text{rate}=k[A]^m[B]^n$` |
| Genetics probability / cross / ratio | `$P(Aa)=0.5$`, `$AA\times aa$`, `$3:1$` |
| Hardy–Weinberg | `$p^2+2pq+q^2=1$` |
| Economics derivative / optimisation | `$\frac{dQ}{dP}$`, `$\max_x U(x)$` |
| Profit | `$\pi=TR-TC$` |

These are examples already present in the shared instructions, not an exhaustive list of KaTeX-supported commands. Do not assume optional packages or arbitrary TeX macros are installed.

## 3. Explain the action, then show the equation

The assessment-authoring prompt requires one calculation step per line: formula, substitution and result must be visibly distinguishable. Paragraphs and equations must not collapse into one dense block.

```markdown
Divide both sides by 3.

$$
x = \frac{12}{3}
$$

So the value of $x$ is:

$$
x = 4
$$
```

Use blank lines between paragraphs, before/after lists, after headings and between question parts. Use real Markdown bullets (`-` / `*`) or numbered lists, not the literal bullet character `•`. Keep one list item per line; preserve meaningful steps and their order. Markdown hard breaks use two trailing spaces and a newline. Do not destroy those spaces in normalisation.

Digital assessment authoring additionally specifies:

- Each part has its own line, a blank line between parts and a bold **prose** part label such as `**(a)**` or `**(b)(i)**`.
- Marking points form a bulleted list under the matching part label, one accepted point per bullet, with plain-text credit such as `**(1 mark)**`.
- Question totals use `**[N]**` in the presentation/grading question fields; do not repeat that total tag in the marking scheme. This is a digital-assessment authoring convention, not a requirement to override Workbench’s separate marks presentation or mark-free guided practice.
- Calculation questions include required values and units; marking schemes include the complete formula/substitution/result and accepted marking points.

Workbench’s agreed additional presentation rules remain: clear sentence bullets beneath meaningful steps, equations beneath their explanation, adjacent step navigation, and a left-aligned bordered Final Answer taken from the exact saved recipe instance. Those are feature presentation/answer-authority rules, not new LaTeX delimiters.

## 4. Backslashes: source, transport and displayed content

Do not interpret the old instruction “use double backslashes” as permission to double every backslash in already-decoded Markdown.

| Layer | Example |
|---|---|
| Decoded Markdown passed to the renderer | `$\frac{1}{2}$` |
| JSON source encoding that string | `{"feedback":"$\\frac{1}{2}$"}` |
| Python raw string holding decoded Markdown | `r"$\frac{1}{2}$"` |
| Python/JavaScript ordinary string literal holding it | `"$\\frac{1}{2}$"` |
| Decoded matrix row break | `a & b \\ c & d` |
| JSON source encoding that row break | `"a & b \\\\ c & d"` |

Use the platform JSON serializer rather than hand-building JSON. Normal decoding restores one command backslash; a mathematical row break still requires two. Repeated blind unescaping can corrupt commands, row breaks, legitimate newlines and literal currency.

## 5. Backend parsing and storage

- Treat model output as untrusted. Validate/coerce structured fields and reject or recover malformed output deliberately.
- Extract user-facing text from known fields; do not display the enclosing JSON object, internal field names, schema labels, tool traces or provider/model names.
- Remove enclosing response fences where appropriate before structured parsing. Genuine code examples within an explanation are learner content and must remain intact.
- Use the shared `repair_latex_escapes` / `loads_with_latex` / `loads_object_with_latex` helpers where structured model output can contain mathematical commands. Their repair happens before JSON parsing because commands beginning `\f`, `\b`, `\t` or `\r` can otherwise be silently parsed as JSON control characters; `\p` / `\s` can make the parse fail.
- The shared helper tries repaired JSON first and returns a defensive failure for genuinely malformed input. Preserve the caller’s validation/error handling.
- Normalise escaped transport newlines and malformed LaTeX escapes at their proper boundary; do not change mathematical values or rewrite saved evidence to repair presentation.
- Socratic `normalize_outbound_whitespace` only caps excessive newlines outside fenced code and trims outer blank lines; it preserves spaces, tabs, indentation and Markdown hard breaks.

## 6. Frontend rendering

- Use `MathMarkdown` or a deliberately equivalent safe ReactMarkdown pipeline. Never show mathematical Markdown as raw text in a normal `<div>`, `<p>` or textarea preview.
- Shared stack: `remark-gfm`, `remark-breaks`, `remark-math`, then `rehype-katex`; load `katex/dist/katex.min.css`.
- Current KaTeX options are `strict:false`, `throwOnError:false`. They prevent a bad expression from crashing the screen; they do not prove that the expression is valid or readable.
- For untrusted AI prose, explicitly pass **both** `allowHtml={false}` and `allowImages={false}`. The shared component defaults both to true for older authored question-bank content, so callers must choose intentionally.
- Raw legacy question-bank HTML is a separate trusted-content path. Do not enable `rehype-raw` merely to render mathematics; KaTeX works without it.
- Disabling HTML alone does not disable Markdown images or tracking URLs. Image rendering requires an explicit safe-image policy.
- `normalizeQuestionContent` handles strings, known text-bearing objects, JSON-encoded objects and arrays. It selects display text rather than rendering object/schema syntax.
- `escapeCurrencyDollars` protects prefix currency such as `N$20`, `US$30`, `R$10` before math parsing. The existing regex intentionally does not reinterpret every trailing dollar sign.
- Preserve paragraph, list and part structure. Allow wide tables/matrices/equations to fit or scroll within the content panel; they must not force page-width overflow. The shared renderer already wraps tables for horizontal scrolling; each surface still needs layout verification for wide equations.
- Confirm equivalent rendering in learner answering, feedback, teacher preview/review and saved history, not just the initial question.

## 7. Actual integration map

| Area | Generation / parsing | Rendering |
|---|---|---|
| Digital assessment authoring | `services/api/services/assessment_question_generation.py` appends the shared instruction and adds question/mark-scheme layout rules | `apps/web/components/Assessments/Create/AssessmentPreview.js` and related question editors use `MathMarkdown` |
| Digital test tutoring | `services/api/services/digital_practice_test_service.py` imports/appends the shared instruction | Test/review surfaces use shared mathematical rendering |
| Digital test marking | `services/api/services/digital_practice_test_grading_service.py` appends the shared instruction; its response parser currently uses `json.loads` | Learner results and teacher DPT review use `MathMarkdown`; untrusted fields must opt into safe props |
| Learner digital test | Stored question/presentation fields | `apps/web/pages/learner/classrooms/[classId]/assessments/attempt/[assignmentId].js` |
| Digital test results | Saved question/memo and grading output | `apps/web/pages/learner/classrooms/[classId]/assessments/results/[attemptId].js` |
| Socratic tutoring | `fallback_prompt_handler.py` and `database_prompt_handler.py` contain embedded rule copies; `socratic_response_sanitizer.py` handles display prose/whitespace | `apps/web/components/ChatInterface/ChatMessage.js` uses its own ReactMarkdown + KaTeX stack |
| Dictation cleanup | Generated frontend instruction mirror; `answerCleanupPrompt.js` | Answer preview surface; parity tested in `answerDictationHelpers.test.js` |
| Workbench | `routers/maths_workbench.py`, `flashcard_grading_service.py`, recipe content formatters | `components/MathsWorkbench/Content.js` and shared renderer-backed feedback/steps |

This map confirms instruction/renderer usage; it does not certify every call site or prove that the full platform already conforms.

## 8. Existing contradictions and consolidation work

1. **Duplicated Socratic prompts:** the shared constant claims a single source, but the fallback and database prompt handlers still embed copies. Refactor those blocks to reuse the shared constant, taking care with their string escaping and stored/database prompt behaviour. Do not claim editing the constant updates those copies today.
2. **Ambiguous escape instruction:** clarify the shared constant to distinguish JSON encoding from decoded Markdown, then regenerate its frontend mirror and run parity/rendering tests. This extraction documents the distinction without changing live prompts.
3. **Old mixed-emphasis test document:** `apps/web/test-latex-rendering.md` expects bold/italic-wrapped maths to render. Treat these as legacy robustness cases, not approved generation examples; the central generation rule forbids producing them.
4. **Socratic HTML/image safety:** `ChatMessage.js` currently includes `rehype-raw` and automatic image conversions. It does not inherit `MathMarkdown`’s safe defaults/props or currency helper. Audit and migrate intentionally; do not present that legacy setup as the safe standard for new AI surfaces.
5. **Legacy video restriction:** the fallback prompt forbids LaTeX and YouTube links in the same message. This is a path-specific legacy instruction, not a demonstrated limitation of the shared KaTeX renderer. Verify the video/message path before retaining or removing it.
6. **Older MathLive utilities:** `latexProcessor.js` and `fixLatex.js` handle alternative delimiters and HTML transformations; one MathLive path sets `trust:true`. Their presence is not evidence they power current chat. Do not reuse them as the default untrusted-output renderer without a separate audit.
7. **Structured grading escape repair:** the shared JSON repair helper is not universally applied. Digital-test marking currently calls `json.loads` directly; inspect its full output-validation path before assuming it has the same repair protection as services that explicitly import the helper.

These are findings for follow-up, not repairs completed by this documentation change.

## 9. Verification checklist

- Inline and display maths render without visible raw commands; Markdown emphasis does not swallow formula delimiters.
- Fractions, roots, exponents, units, Greek letters, chemical notation and matrix row breaks survive JSON round trips.
- Literal currency alongside a real formula remains intact.
- Paragraphs, Markdown hard breaks, lists, part labels and formula/substitution/result layout survive parsing and rendering.
- Malformed/nested JSON, code-fenced envelopes, escaped newlines and command escapes fail safely without leaking metadata.
- Untrusted raw HTML and Markdown images cannot become active content on the safe rendering path.
- Wide content fits its panel or scrolls locally on small screens; verify feedback and history as well as live questions.
- Shared backend/frontend prompt copies remain equal. Do not call a tolerant renderer proof of mathematical correctness.

Existing focused checks: `services/api/tests/test_llm_json_repair.py`, `services/api/tests/test_socratic_response_sanitizer.py`, `apps/web/__tests__/MathMarkdown.test.js`, `MathMarkdownCurrency.test.js`, `answerDictationHelpers.test.js`, and `dictationAnswerRoute.test.js`.
