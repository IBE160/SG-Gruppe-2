
# Project Description – AI Study Buddy

## Project Code and Title
**IBE160 – Programming with AI**  
**Project Title:** AI Study Buddy

## Overview
AI Study Buddy is an application designed to help students process their course materials more efficiently. By leveraging artificial intelligence, the system generates summaries, flashcards, and quiz questions from uploaded lecture notes or study materials. The aim is to provide students with a practical tool for learning and exam preparation, while giving developers hands-on experience with text processing, AI integration, and secure web application development.

## Problem Statement
Students spend significant time manually summarizing notes and creating learning materials, an inefficient process that becomes overwhelming with large syllabi. There is a clear need for a digital assistant to help students structure their study process and reduce repetitive, time-consuming tasks.

## Objectives
- Develop an AI-powered application supporting student learning and exam preparation.
- Implement functionality for creating summaries, flashcards, and quiz questions from uploaded content.
- Gain experience integrating AI into real applications, including handling basic security and privacy considerations.

## Functionality
- **Input:** Uploaded course material (PDF/text), user preferences (level of detail, language, number of questions).
- **Output:** Summaries, flashcards (Q&A format), quizzes with answers, key concept lists.
- **Optional:** Login functionality if users want to save their materials.

## Key Features
- Upload lecture notes or course material (PDF/text).
- Generate summaries of different lengths.
- Create flashcards for active recall.
- Generate quizzes with answer keys.
- Provide a list of key terms from the text.

## Data and Processing
- **Data In:** PDF or text files from students’ notes or course material.
- **Data Out:** Summaries, flashcards, quiz questions, and key terms.
- **Key Decisions:**  
  - Choice of LLM (Gemini 1.5 Pro).  
  - Granularity of summaries.  
  - Quiz type (multiple choice vs open-ended).  
  - Handling of tables/figures.  
  - Local vs cloud-based processing.

## Security and Privacy
- Notes may contain protected course material, so privacy is a priority.
- Possible use of anonymization or encrypted storage.
- Login is only required if users want to save their materials.

## Complexity
- **Difficulty Level:** 🟢 Simple  
  - Requires basic text processing, AI integration, and a simple user interface.
  - Can be extended with advanced features (adaptive quizzes, study progress tracking).

## Expected Learning Outcomes
- Gain experience with AI-based text generation and API integration.
- Understand how to integrate AI models into a web application.
- Learn to handle user data and basic privacy/security issues.
- Improve skills in interface design and interactive learning tools.

## Summary
AI Study Buddy is a manageable yet meaningful project. It has a low technical threshold, fits within the semester timeframe, and provides strong learning outcomes by combining programming, AI integration, and user-focused design.

---

## Technical Summary
- **Frontend:** React and Tailwind CSS for a responsive, accessible user interface.
- **Backend:** FastAPI (Python), with PyMuPDF for PDF parsing and handling file uploads.
- **AI Engine:** Gemini 1.5 Pro API for text summarization, flashcard, and quiz generation.
- **Hosting:** Local prototype for development and demonstration.
- **Data Handling:** Secure PDF/text upload, text extraction, AI-powered study aid generation.
- **Security:** API keys and sensitive data managed via environment variables (`.env`); HTTPS recommended for deployment to protect data in transit.