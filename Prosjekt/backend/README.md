

# AI Study Buddy – Backend Setup Guide

This document describes how to set up, run, and maintain the **AI Study Buddy Backend**, built using **FastAPI** and integrated with **Google Gemini 2.5 API**.

---

## 📘 Overview
The backend provides API endpoints for:
- Uploading PDF course materials.
- Extracting and summarizing text content.
- Generating flashcards and learning prompts using Gemini AI.

It is designed for seamless integration with the frontend (Next.js / React-based UI).

---

## ⚙️ Requirements
Make sure you have:
- **Python 3.9+**
- **pip** (latest version)
- **Virtual environment** (`venv`)
- A valid **Gemini API key** from [Google AI Studio](https://aistudio.google.com/app/apikey)

---

## 🧩 Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/revoul23/AI-Study-Buddy.git
cd AI-Study-Buddy/Prosjekt/backend
```

### 2. Create and activate a virtual environment
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables
Create a file named `.env` in the `backend/` folder and add your Gemini API key:

```bash
GEMINI_API_KEY=your_api_key_here
```

---

## 🚀 Run the Backend
Start the FastAPI development server:

```bash
uvicorn main:app --reload
```

Then open your browser at:  
👉 [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

This opens the interactive Swagger UI where you can test:
- `POST /upload/` — Upload PDF and summarize.
- `POST /generate/flashcards/` — Generate learning cards.

---

## 🧠 Tech Stack
- **FastAPI** – REST API framework
- **Uvicorn** – ASGI server
- **PyMuPDF** – PDF text extraction
- **Google GenAI (gemini-2.5-flash)** – Text generation and summarization
- **dotenv** – Environment configuration

---

## 🧰 Troubleshooting

### ❌ `ImportError: cannot import name 'genai'`
➡️ Ensure `google-genai` is installed:
```bash
pip install google-genai
```

### ❌ API returns 500 Internal Server Error
➡️ Verify `.env` contains a valid `GEMINI_API_KEY`.

### ⚠️ SSL Warning (macOS)
If you see `NotOpenSSLWarning`, it’s safe to ignore when running locally.

---

## 🪶 Notes
All API usage is logged in `docs/dev_log.md`.  
Keep this README focused on backend setup and developer usage.

---