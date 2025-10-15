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