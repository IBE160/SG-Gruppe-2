from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import fitz  # PyMuPDF
import os
from dotenv import load_dotenv
from google import genai
import markdown

# Load environment variables
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    print("⚠️ Warning: GEMINI_API_KEY is missing or invalid. The app will run, but AI features will not work until a valid key is set.")
    api_key = None

# Initialize Gemini client
client = genai.Client(api_key=api_key)

# Initialize FastAPI app
app = FastAPI(title="AI Study Buddy Backend")

# CORS setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://127.0.0.1:8000",
        "http://localhost:8000",
        "http://localhost:5173",
        "http://127.0.0.1:5173",
        "*",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Root endpoint
@app.get("/")
def read_root():
    return {"message": "AI Study Buddy Backend is running (Gemini 2.5 enabled)"}

# Upload and summarize file
@app.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    try:
        if not (file.filename.endswith(".pdf") or file.filename.endswith(".txt")):
            raise HTTPException(status_code=400, detail="Only PDF and text files are supported")

        contents = await file.read()
        text = ""

        if file.filename.endswith(".pdf"):
            with fitz.open(stream=contents, filetype="pdf") as doc:
                text = "".join([page.get_text() for page in doc])
        else:
            text = contents.decode("utf-8")

        if not text.strip():
            raise HTTPException(status_code=400, detail="File contains no readable text")

        if not api_key:
            raise HTTPException(status_code=500, detail="AI features are disabled because GEMINI_API_KEY is missing.")

        # Generate summary using Gemini 2.5 Flash
        print("✅ Using Gemini 2.5 Flash model")
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=f"Summarize this course material for students:\n{text}",
        )

        summary = getattr(response, "text", None) or "No summary generated."
        # Convert Markdown to HTML for proper rendering in frontend
        html_output = markdown.markdown(summary)
        return {"summary": html_output}

    except Exception as e:
        print(f"Error in /upload/: {e}")
        raise HTTPException(status_code=500, detail=str(e))

# Generate flashcards
@app.post("/generate/flashcards/")
async def generate_flashcards(file: UploadFile = File(...)):
    try:
        contents = await file.read()
        text = ""

        if file.filename.endswith(".pdf"):
            with fitz.open(stream=contents, filetype="pdf") as doc:
                text = "".join([page.get_text() for page in doc])
        else:
            text = contents.decode("utf-8")

        if not text.strip():
            raise HTTPException(status_code=400, detail="File contains no readable text")

        if not api_key:
            raise HTTPException(status_code=500, detail="AI features are disabled because GEMINI_API_KEY is missing.")

        print("✅ Using Gemini 2.5 Flash model for flashcards")
        prompt = (
            "Create 5 concise flashcards from this text. "
            "Each flashcard should be in JSON with 'question' and 'answer' keys.\n"
            f"{text}"
        )

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
        )

        flashcards = getattr(response, "text", None) or "No flashcards generated."
        return {"flashcards": flashcards}

    except Exception as e:
        print(f"Error in /generate/flashcards/: {e}")
        raise HTTPException(status_code=500, detail=str(e))
    