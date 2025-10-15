
# BMAD Brief – AI Study Buddy

## Background
Students often spend excessive time manually summarizing lecture notes and creating study materials, especially when dealing with large and complex syllabi. This process is inefficient and can detract from actual learning. Manual approaches are also prone to error and inconsistency. Artificial Intelligence offers a scalable solution by automating the generation of summaries, flashcards, and quizzes from uploaded course materials, allowing students to focus on understanding and retention.

## Goal
Design and develop a prototype application called **AI Study Buddy** to help higher education students prepare for exams by transforming their course materials into actionable learning aids. The focus is on leveraging the Gemini API for advanced text processing and ensuring a user-friendly experience tailored to student needs.

## Scope
- **Input:** Uploaded course material (PDF or text files) and user preferences (e.g., level of detail, language, number of questions).
- **Output:** AI-generated summaries, flashcards (Q&A), quizzes with answers, and key term lists.
- **Platform:** Web-based prototype with a simple, accessible interface.
- **Users:** Higher education students seeking to optimize their study process.

## Key Features
- Upload lecture notes or course material in PDF/text format.
- Generate concise and detailed summaries.
- Create flashcards for active recall.
- Generate quizzes with answers for self-assessment.
- Extract and list key concepts and terms.

## Technical Approach
- **Frontend:** Built with React and Tailwind CSS for a responsive, accessible, and modern user interface.
- **Backend:** FastAPI (Python) handles file uploads, parsing (using PyMuPDF), and AI integration.
- **AI Engine:** Gemini 1.5 Pro API processes text and generates study aids.

## Constraints
- The prototype must be deliverable within a single semester.
- Emphasis on core functionality and robust AI integration over advanced UI polish.
- All prompt documentation and BMAD role files must be maintained and reproducible as part of the project.
- Use of Gemini API must comply with privacy and security guidelines.

## Success Criteria
- The application runs locally and successfully produces summaries, flashcards, and quizzes from sample course material.
- All BMAD documentation (designer, developer, tester, scrummaster) is complete and up to date.
- Prompts and AI responses are stored in the project and can be reused.
- The system uses Gemini API for text generation and demonstrates value to students through improved study efficiency.