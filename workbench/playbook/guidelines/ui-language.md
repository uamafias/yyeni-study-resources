# UI Language Standards

Plain language wins. Reject teacher-jargon in user-facing strings.

## Replacement table

| Reject | Use |
|--------|-----|
| Threshold | Minimum passing score |
| Required | Must Complete |
| Submit | Save / Send / Confirm (specific to action) |
| Field | Box / Question / [specific noun] |
| Error 500 | Something went wrong on our side. Please try again. |
| "the test" / "YYeni testing" (flashcards) | Flashcard Recall Test |

**Marking standard.** How a Flashcard Recall Test answer is marked is set by [`flashcard-marking-guideline.md`](flashcard-marking-guideline.md), which is canonical. The grader prompt in `services/api/services/flashcard_grading_service.py` restates it; change the guideline first.

**Two different tests, two different names.** The **Flashcard Recall Test** is the graded flashcard round that moves memory boxes. The **Digital Practice Test** is the separate exam-style assessment. Never call either one just "the test" on a screen where both could be meant — learners and teachers read them as the same thing and act on the wrong one.

## Principles
- **Action verbs in buttons.** "Save changes" not "Submit." "Generate flashcards" not "OK."
- **No jargon in headers.** "Class performance" not "Aggregate analytics."
- **Concrete > abstract.** "John missed 3 of 10 questions" beats "Score: 70%."
- **Empathy in error states.** Tell the user what happened and what to do, not which exception was raised.

## AI model trade secrecy
Never reference the underlying AI model name in user-facing copy. No "Powered by Gemini," no model version strings in transaction logs, no "GPT" or any other vendor name. The AI is YYeni.
