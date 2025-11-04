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
✅ User experience significantly improved through readable, structured AI responses.git add .
git commit -m "Added frontend prototype (HTML/CSS/JS) and integrated Markdown-rendered Gemini responses in backend"
git push origin main


## 2025-10-19 — Designer Phase 2 Updates
- Extended design to include Results and Settings screens.
- Updated visual layout and accessibility guidelines.
- Prepared style_guide.md with color, typography, and layout specifications.
- Verified consistent design across upload → results → settings flow.

## 2025-10-19 — Phase 2: Dynamic Frontend-Backend Integration

### Summary
Phase 2 focused on connecting the FastAPI backend with the static HTML/CSS/JS frontend. The goal was to enable a working flow from file upload → AI summary generation → display of results in the browser.

### Implemented Features
✅ Established full communication between `script.js` and FastAPI endpoints (`/upload` and `/generate/flashcards`).  
✅ Markdown-to-HTML conversion added to backend for improved readability.  
✅ Frontend navigation structure implemented (Upload, Results, Settings).  
✅ Basic accessibility compliance verified (ARIA roles, contrast, focus states).  
✅ Designed consistent interface based on WCAG and Norwegian government design standards.

### Testing
- Verified via Swagger UI (`http://127.0.0.1:8000/docs`) and browser UI.  
- Uploaded PDFs successfully and viewed formatted AI summaries in browser.  
- Flashcards generation tested and functional.  
- Quiz placeholder ready for implementation in Phase 3.

### Reflection
This phase completed the integration layer between backend and frontend, achieving an interactive MVP skeleton.  
The project is now ready for **Phase 3: full AI functionality and user experience refinement**.


---

## 2025-11-04 — Phase 3: Quiz Functionality Implementation

**Implemented:**
- Added `/generate/quiz/` endpoint in `main.py` with Gemini 2.5 Flash.
- Created a structured JSON prompt ensuring valid, predictable output from Gemini.
- Integrated robust response parsing with automatic JSON cleaning and validation.
- Updated `script.js` to display quiz questions, answer options, and highlight correct answers.
- Added “Generer Quiz” button in `index.html` linked to backend endpoint.

**Reason:**
- The quiz generation previously returned inconsistent or empty data due to unstructured Gemini responses.
- This update ensures stable and accurate parsing, allowing for real-time quiz creation from uploaded study materials.

**Outcome:**
✅ Gemini 2.5 Flash now generates quizzes reliably.  
✅ Quiz questions and answers display correctly in the web UI.  
✅ End-to-end functionality verified from upload → summary → flashcards → quiz.  
✅ Phase 3 milestone successfully achieved.