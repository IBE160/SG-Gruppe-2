

# Designer Role – AI Study Buddy

## Vision
Create an accessible, student-focused interface that is easy to use, visually clear, and inclusive. The design should be inspired by Norwegian government digital services, emphasizing simplicity, accessibility, and compliance with WCAG standards. The application must be approachable for students of all backgrounds and abilities, with a logical flow from uploading materials to reviewing generated study aids.

## Responsibilities
- Design intuitive layouts for uploading notes, displaying results, and adjusting settings.
- Develop a minimalistic, modern user interface with a focus on clarity and accessibility.
- Ensure navigation is smooth and logical: upload → results → settings/options.
- Select a color palette, fonts, and icons that enhance readability and are accessible to all users.
- Document accessibility considerations, including color contrast, font size, and keyboard navigation.

## Deliverables
- Wireframes or sketches of main screens (upload, results, settings).
- Style guide (color palette, fonts, icons).
- Accessibility notes and recommendations.

---

## Prompts and AI Responses

### Prompt 1 – Interface and Structure
**Prompt:**  
Design the user interface for the AI Study Buddy application. The main screens should include:  
1. Upload – where the user selects and uploads their PDF or text notes.  
2. Results – where the user views generated summaries, flashcards, and quizzes.  
3. Settings – where the user can adjust preferences (e.g., summary length, number of flashcards).  
Provide a wireframe or description for each screen, focusing on logical flow and clarity.

**AI Response:**  
1. **Upload Screen:**  
   - Central upload area with drag-and-drop and file picker options.  
   - Instructions and supported file types (PDF, TXT).  
   - Progress indicator for upload and parsing.  
   - Button to proceed to results after upload is complete.
2. **Results Screen:**  
   - Tabs or cards for Summaries, Flashcards, and Quizzes.  
   - Each section displays generated content with options to copy, download, or mark as favorite.  
   - Clear navigation back to upload or to settings.
3. **Settings Screen:**  
   - Sliders or dropdowns for adjusting summary length, number of flashcards, and quiz preferences.  
   - Option to select language (if supported).  
   - Save and reset buttons.  
   - Accessibility settings (font size, high contrast mode).

### Prompt 2 – Style and Accessibility
**Prompt:**  
Create a style guide for the AI Study Buddy app. Specify a color palette, font choices, and iconography that ensure high accessibility and readability. Reference Norwegian government digital design guidelines and WCAG standards.

**AI Response:**  
- **Color Palette:**  
  - Primary: Deep blue (#003366), Secondary: Light blue (#E6F0FA), Accent: Orange (#FF8200), Background: White (#FFFFFF), Text: Dark gray (#222222).
  - All color combinations meet WCAG AA contrast requirements.
- **Fonts:**  
  - Headings: Inter, bold, large size (1.5–2rem).  
  - Body: Inter or Arial, regular, at least 16px.
- **Icons:**  
  - Use simple, universally recognizable icons (upload, settings, flashcard, quiz).  
  - Sourced from open-access icon libraries.
- **Accessibility:**  

  - Sufficient color contrast.  
  - Keyboard navigable.  
  - Alt text on all images and icons.  
  - Responsive layout for mobile and desktop.

---

### Prompt 3 – Frontend Prototype UI (Phase 2)
**Prompt:**  
Design the first HTML/CSS/JS prototype for the AI Study Buddy frontend. Use the existing style guide (colors, fonts, layout) to build a simple upload interface that connects to the FastAPI backend. Include placeholders for results and settings screens to be implemented later.

**AI Response:**  
- **index.html:**  
  - Contains a header with the app title “AI Study Buddy”.  
  - Central upload card with drag-and-drop or “Choose File” button.  
  - A “Generate Study Aids” button triggering API call to `/upload`.  
  - Placeholder sections for “Results” and “Settings”.
- **style.css:**  
  - Uses the defined palette: Deep blue (#003366), Light blue (#E6F0FA), and Accent orange (#FF8200).  
  - Applies modern, accessible design: large buttons, high contrast, and responsive grid.  
  - Fonts: Inter, sans-serif, minimum 16px.
- **script.js:**  
  - Handles file upload and POSTs data to the FastAPI `/upload` endpoint.  
  - Displays success or error messages dynamically.  
  - Logs response to console for now (future integration: display flashcards and summaries).
- **Next Step:**  
  - Expand the UI with React components for a more dynamic experience once prototype testing is completed.

### Prompt 6 – Designer Support (Frontend Phase 2)
**Prompt:**  
Refine and extend the UI for AI Study Buddy to include **Results** and **Settings** screens.  
Ensure visual consistency, accessibility, and clarity across all sections (Upload, Results, Settings).

**Requirements:**
- Follow the established color palette and typography.  
- Provide layout descriptions for each screen:
  - **Results:** Tabs for Summary, Flashcards, Quiz.  
  - **Settings:** Form elements for summary length, flashcard count, and language.  
- Ensure:
  - High color contrast (meets WCAG AA).  
  - Clear focus states for keyboard navigation.  
  - Responsive layout for mobile and desktop.

**Deliverables:**
- Updated visual layout guidelines (in `docs/style_guide.md`).  
- Accessibility notes.  
- Optional wireframes or mockups for frontend reference.