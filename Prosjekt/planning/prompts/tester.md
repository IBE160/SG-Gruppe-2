

# Tester Role – AI Study Buddy

## Role Description
Ensure the application meets functional and non-functional requirements by planning, executing, and documenting tests. The tester is responsible for validating all core features, checking AI outputs for accuracy and usefulness, and ensuring the application is robust and accessible for students.

## Responsibilities
- Develop and maintain a comprehensive test plan.
- Write and execute unit, integration, and user acceptance tests.
- Validate AI-generated outputs (summaries, flashcards, quizzes) for relevance and clarity.
- Document bugs and issues, and verify fixes.
- Define and track validation metrics for project success.

---

## Prompts and AI Responses

### Prompt 1 – Test Plan
**Prompt:**  
Define a test plan for the AI Study Buddy application. What should be tested and how (unit, integration, user testing)?

**AI Response:**  
- **Unit Tests:**  
  - Test backend endpoints for file upload, text extraction, and AI response handling.  
  - Validate PDF parsing and error cases.
- **Integration Tests:**  
  - End-to-end test: Upload file → generate study aids → display results.  
  - Check frontend-backend communication.
- **User Testing:**  
  - Recruit sample students to use the app and provide feedback on usability and output quality.  
  - Record and address any issues with navigation, accessibility, or AI results.

### Prompt 2 – Automated Tests
**Prompt:**  
Create example automated tests for FastAPI endpoints. What should be checked?

**AI Response:**  
- Test `/upload` endpoint with valid and invalid files (PDF, TXT, unsupported formats).  
- Test `/generate` endpoint with sample text, verify response contains summaries, flashcards, and quizzes.  
- Test error handling (e.g., empty file, API failure).  
- Example (using pytest):  
  ```python
  def test_upload_valid_pdf(client):
      response = client.post("/upload", files={"file": ("notes.pdf", b"%PDF-1.4 ...")})
      assert response.status_code == 200
      assert "file_id" in response.json()
  ```

### Prompt 3 – Validation Metrics
**Prompt:**  
Define validation metrics for the project. What does success look like?

**AI Response:**  
- Application produces accurate and relevant summaries, flashcards, and quizzes for a variety of input materials.
- All core features function as intended (file upload, processing, output display).
- At least 90% of automated tests pass.
- User feedback indicates improved study efficiency and satisfaction.
- Accessibility criteria (WCAG AA) are met.