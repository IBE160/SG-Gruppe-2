# Development Log – AI Study Buddy

## 2025-10-15 — Gemini API Migration
**Changed:**
- Replaced `google-generativeai` with `google-genai`.
- Updated import in `main.py` to `from google import genai`.
- Adjusted model name to `gemini-2.5-flash`.
- Verified compatibility with FastAPI endpoints `/upload` and `/generate/flashcards`.

**Reason:**
- The old client (google-generativeai) is deprecated.
- Gemini 2.5 API requires the new unified client `google-genai`.

**Outcome:**
✅ Backend now loads successfully with Gemini 2.5 Flash and responds correctly via Swagger UI.

## 2025-10-16 — Legacy Structure Update
**Updated:**
- Added `.bmad-core/` and `planning/` folders to `.gitignore` to avoid pushing legacy BMAD documentation.
- Retained the folders locally for historical and reference purposes.

**Reason:**
- These directories are no longer part of the active AI Study Buddy architecture but may contain useful past agent definitions and workflows.

**Outcome:**
✅ Project repository is cleaner while keeping legacy data accessible locally.

## 2025-10-16 — Markdown Rendering Enhancement
**Implemented:**
- Installed and configured the `markdown` library in the backend environment.
- Updated `/upload` endpoint in `main.py` to convert Gemini API responses from Markdown to HTML using `markdown.markdown()`.
- Verified in Swagger UI (`http://127.0.0.1:8000/docs`) that HTML-formatted summaries are now returned correctly.
- Frontend updated to use `innerHTML` for proper display of formatted text.

**Reason:**
- Gemini responses included Markdown formatting that appeared as plain text in the browser.
- Conversion to HTML ensures structured display with headings, lists, and bold emphasis.

**Outcome:**
✅ Summaries now render cleanly with headings, bullet points, and paragraphs.
✅ Browser output is fully formatted and accessible.
✅ User experience significantly improved through readable, structured AI responses.