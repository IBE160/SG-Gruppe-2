from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import fitz  # PyMuPDF
import os
from dotenv import load_dotenv
from google import genai
import markdown
from pydantic import BaseModel
from typing import List, Optional
import json
import re
import logging

# === Logging setup ===
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("AI-Study-Buddy")

# === Load environment variables ===
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    logger.warning("⚠️ GEMINI_API_KEY is missing. AI features will not work.")
    api_key = None

# === Define data models ===
class FlashcardRequest(BaseModel):
    text: str
    num_flashcards: int = 5

# === Initialize Gemini client ===
client = genai.Client(api_key=api_key)

# === Initialize FastAPI app ===
app = FastAPI(title="AI Study Buddy Backend")

# === CORS setup ===
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# === Root endpoint ===
@app.get("/")
def read_root():
    return {"message": "✅ AI Study Buddy Backend is running (Gemini 2.5 Flash enabled)"}

# === Upload and summarize file ===
@app.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    try:
        if not (file.filename.endswith(".pdf") or file.filename.endswith(".txt")):
            raise HTTPException(status_code=400, detail="Only PDF and text files are supported")

        contents = await file.read()
        text = ""

        if file.filename.endswith(".pdf"):
            try:
                with fitz.open(stream=contents, filetype="pdf") as doc:
                    text = "".join([page.get_text() for page in doc])
            except Exception as e:
                logger.error(f"PDF parsing error: {e}")
                raise HTTPException(status_code=400, detail="Could not read PDF file")
        else:
            text = contents.decode("utf-8", errors="ignore")

        if not text.strip():
            raise HTTPException(status_code=400, detail="File contains no readable text")

        if not api_key:
            raise HTTPException(status_code=500, detail="GEMINI_API_KEY missing")

        logger.info("✅ Using Gemini 2.5 Flash model for summary")
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=f"Summarize this course material for students:\n{text[:30000]}",
        )

        summary = getattr(response, "text", None) or "No summary generated."
        html_output = markdown.markdown(summary)
        return {"summary_html": html_output, "raw_text": text}

    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error in /upload/: {e}")
        raise HTTPException(status_code=500, detail=str(e))

# === Generate flashcards ===
@app.post("/generate/flashcards/")
async def generate_flashcards(req: FlashcardRequest):
    try:
        text = (req.text or "").strip()
        if not text:
            raise HTTPException(status_code=400, detail="No text provided or file is empty")
        if not api_key:
            raise HTTPException(status_code=500, detail="GEMINI_API_KEY missing")

        logger.info("✅ Using Gemini 2.5 Flash model for flashcards")
        prompt = (
            f"Create {req.num_flashcards} concise flashcards from the text below. "
            "Return ONLY valid JSON array of objects with 'question' and 'answer' keys.\n\n"
            f"TEXT:\n{text[:10000]}"
        )

        response = client.models.generate_content(model="gemini-2.5-flash", contents=prompt)
        raw = getattr(response, "text", "") or ""

        # Attempt to parse JSON safely
        flashcards: Optional[List[dict]] = None
        try:
            flashcards = json.loads(raw)
        except Exception:
            match = re.search(r"\[.*\]", raw, re.DOTALL)
            if match:
                try:
                    flashcards = json.loads(match.group(0))
                except Exception:
                    flashcards = None

        if not flashcards:
            logger.warning(f"⚠️ Could not parse JSON. Raw model output: {raw[:300]}")
            return {"flashcards_raw": raw}

        normalized = [
            {"question": fc.get("question", "").strip(), "answer": fc.get("answer", "").strip()}
            for fc in flashcards if fc.get("question") and fc.get("answer")
        ]

        if not normalized:
            return {"flashcards_raw": raw}

        return {"flashcards": normalized}

    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error in /generate/flashcards/: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/generate/quiz/")
async def generate_quiz(req: FlashcardRequest):
    try:
        text = (req.text or "").strip()
        if not text:
            raise HTTPException(status_code=400, detail="No text provided.")
        if not api_key:
            raise HTTPException(status_code=500, detail="GEMINI_API_KEY missing")

        logger.info("✅ Using Gemini 2.5 Flash model for quiz generation")

        prompt = (
            "Generate 5 multiple-choice quiz questions from the text below. "
            "Each question must have exactly four options labeled A, B, C, D, and specify the correct letter. "
            "Return ONLY valid JSON in this format:\n"
            "{\n"
            "  \"quiz\": [\n"
            "    {\"question\": \"...\", \"options\": [\"A. ...\", \"B. ...\", \"C. ...\", \"D. ...\"], \"answer\": \"B\"}\n"
            "  ]\n"
            "}\n\n"
            f"TEXT:\n{text[:8000]}"
        )

        response = client.models.generate_content(model="gemini-2.5-flash", contents=prompt)
        raw = getattr(response, "text", "") or ""
        cleaned = re.sub(r"```(json|JSON)?", "", raw).strip().strip("`")

        match = re.search(r"\{.*\}", cleaned, re.DOTALL)
        quiz_json = match.group(0) if match else cleaned

        quiz_data = None
        try:
            quiz_data = json.loads(quiz_json)
        except Exception as e:
            logger.warning(f"⚠️ Could not parse quiz JSON: {e}")
            logger.warning(f"Raw output: {raw[:500]}")
            return {"quiz_raw": raw}

        final_quiz = []
        for q in quiz_data.get("quiz", []):
            correct_letter = q.get("answer", "").strip()
            correct_option = next((opt for opt in q.get("options", []) if opt.strip().startswith(correct_letter)), "")
            final_quiz.append({
                "question": q.get("question", "").strip(),
                "options": q.get("options", []),
                "correct": correct_option
            })

        return {"quiz": final_quiz or []}

    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error in /generate/quiz/: {e}")
        raise HTTPException(status_code=500, detail=str(e))