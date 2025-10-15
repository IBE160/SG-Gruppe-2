# Revised Project Proposal – AI Study Buddy

## Course Information
**Course Code:** IBE160 – Programming with AI  
**Project Title:** AI Study Buddy  

---

## 1. Project Overview
AI Study Buddy is a web application that helps students process and understand their course material more effectively. 
By integrating artificial intelligence through the Google Gemini API, the system automatically generates summaries, 
flashcards, and quiz questions from uploaded lecture notes or study documents. 
The goal is to give students a practical study assistant while allowing us as developers to gain real-world experience 
with AI integration, web development, and data privacy.

---

## 2. Problem Statement
Students often spend many hours summarizing lecture notes and creating study aids manually. 
This process is repetitive, time-consuming, and inefficient — particularly in large courses. 
AI Study Buddy automates this process by allowing students to upload material and receive structured learning tools instantly, 
helping them study smarter and save valuable time.

---

## 3. Objectives
- Develop an AI-powered web application that assists students in learning and exam preparation.  
- Implement functionality for generating summaries, flashcards, and quiz questions from uploaded material.  
- Integrate the Gemini API for intelligent text analysis and generation.  
- Ensure basic privacy and security by using environment variables for API keys and secure file handling.  
- Deliver a functional prototype within six weeks.  

---

## 4. Technical Architecture

### System Overview
```
[ User ] → [ React + Tailwind (Frontend) ] → [ FastAPI (Python Backend) ] → [ Gemini API (Google) ] → [ (Optional) Supabase Database ]
```

### Component Summary

| Component | Technology | Description |
|------------|-------------|--------------|
| Frontend | React + Tailwind CSS | User interface for file upload and displaying generated content |
| Backend | Python + FastAPI | Handles requests, communicates with AI, and returns formatted data |
| AI Model | Gemini 1.5 Pro (Google AI) | Generates summaries, flashcards, and quizzes |
| PDF Parser | PyMuPDF | Extracts text content from uploaded PDF files |
| Database (optional) | Supabase (PostgreSQL) | Stores user profiles and generated results if login is implemented |
| Security | .env file | Stores API keys securely |

### Example: Secure Gemini API Integration in Python
```python
import os
import google.generativeai as genai

# Load Gemini API key from environment variable
api_key = os.getenv('GEMINI_API_KEY')
if not api_key:
    raise EnvironmentError('GEMINI_API_KEY not found. Please set it in your .env file.')

# Configure Gemini client
genai.configure(api_key=api_key)

# Example usage
model = genai.GenerativeModel('gemini-1.5-pro')
response = model.generate_content('Summarize this lecture note text...')
print(response.text)
```

---

## 5. Minimum Viable Product (MVP)

### Must-Have Features
- Upload text or PDF files  
- Generate summaries  
- Generate flashcards (Q&A format)  
- Generate quiz questions (multiple-choice)  
- Display or download generated content  

### Nice-to-Have Features
- User login and saved materials  
- Study progress tracking  
- Language selection (English/Norwegian)  
- Export to JSON or CSV  

---

## 6. Data Processing and Privacy
- **File handling:** Files processed temporarily and deleted after completion.  
- **Security:** HTTPS for all data communication.  
- **API Key:** Stored securely in a `.env` file (never hardcoded).  
- **Privacy:** Users retain full ownership of their uploaded data.  
- **Max file size:** 10 MB per PDF.  
- **Error handling:** Informative messages shown if unreadable or scanned PDFs.  

---

## 7. Timeline and Milestones (6 Weeks)

| Week | Focus Area | Deliverables |
|------|-------------|--------------|
| 1 | Project setup | React + FastAPI initialized, repository created |
| 2 | File upload & text extraction | PDF to text function ready |
| 3 | AI integration | Connect Gemini API and generate summaries |
| 4 | Flashcards & quiz generation | Add multiple output types |
| 5 | UI and login | Polished frontend, Supabase integration (optional) |
| 6 | Testing & documentation | Final testing, bug fixing, user feedback, and report |

---

## 8. Learning Outcomes
- Integrate AI models in a web-based application.  
- Develop a complete system (frontend + backend).  
- Manage user data securely and responsibly.  
- Build a practical tool for real educational use cases.  

---

## 9. Summary
This revised proposal includes detailed architecture, MVP scope, timeline, and security planning as requested. 
AI Study Buddy is realistic, educational, and achievable within the course timeframe, offering hands-on experience 
with Gemini API integration and secure web application development.
