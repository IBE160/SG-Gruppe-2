// script.js – AI Study Buddy Frontend Prototype (Phase 2)

let lastUploadedText = "";

const uploadSection = document.getElementById('upload');
const resultsSection = document.getElementById('results');
const settingsSection = document.getElementById('settings');
const uploadStatus = document.getElementById('uploadStatus');

function showSection(sectionId) {
  document.querySelectorAll('section').forEach((section) => {
    section.classList.add('hidden');
  });
  document.getElementById(sectionId).classList.remove('hidden');
}

function showTab(tabId) {
  document.querySelectorAll('.tab-content').forEach((tab) => {
    tab.classList.add('hidden');
  });
  document.getElementById(tabId).classList.remove('hidden');
}

// Upload file to FastAPI backend
async function uploadFile() {
  const fileInput = document.getElementById('fileInput');
  const file = fileInput.files[0];

  if (!file) {
    uploadStatus.innerText = "⚠️ Velg en fil før du laster opp.";
    uploadStatus.style.color = "#FF8200";
    return;
  }

  const formData = new FormData();
  formData.append("file", file);

  uploadStatus.innerText = "⏳ Laster opp...";
  uploadStatus.style.color = "#003366";

  try {
    const response = await fetch("http://127.0.0.1:8000/upload/", {
      method: "POST",
      body: formData,
    });

    if (!response.ok) {
      const errText = await response.text();
      throw new Error(`Feil ved opplasting: ${response.statusText}\n${errText}`);
    }

    const result = await response.json();

    uploadStatus.innerText = "✅ Fil lastet opp og analysert!";
    uploadStatus.style.color = "green";

    // Show results section
    showSection("results");
    showTab("summary");

    // Render HTML summary returned by backend
    const summaryEl = document.getElementById("summaryContent");
    summaryEl.innerHTML = result.summary_html || "<p>Ingen oppsummering generert.</p>";

    // Save raw text for flashcard generation
    lastUploadedText = result.raw_text?.trim() || "";

    if (lastUploadedText.length < 50) {
      console.warn("⚠️ Filen inneholder svært lite tekst, resultat kan bli begrenset.");
    }

    // Auto-generate flashcards using the raw text and current settings
    const count = parseInt(document.getElementById('flashcardCount').value || "5", 10);
    if (lastUploadedText) {
      await generateFlashcards(lastUploadedText, count);
    } else {
      console.warn("Ingen tekst tilgjengelig for flashcards.");
    }

  } catch (error) {
    console.error("Upload error:", error);
    uploadStatus.innerText = "❌ Noe gikk galt under opplasting. Kontroller at filen ikke er tom.";
    uploadStatus.style.color = "red";
  }
}

async function generateFlashcards(text, num) {
  const list = document.getElementById("flashcardList");
  list.innerHTML = "<li>⏳ Genererer flashcards...</li>";

  try {
    const resp = await fetch("http://127.0.0.1:8000/generate/flashcards/", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ text: text.slice(0, 8000), num_flashcards: num }),
    });

    if (!resp.ok) {
      const errText = await resp.text();
      throw new Error(`Feil fra server: ${resp.status} ${resp.statusText}\n${errText}`);
    }

    const data = await resp.json();
    list.innerHTML = "";

    if (Array.isArray(data.flashcards)) {
      data.flashcards.forEach((fc, i) => {
        const li = document.createElement("li");
        li.innerHTML = `<strong>Q${i + 1}:</strong> ${fc.question}<br/><strong>A:</strong> ${fc.answer}`;
        list.appendChild(li);
      });
    } else if (data.flashcards_raw) {
      const li = document.createElement("li");
      li.textContent = data.flashcards_raw.slice(0, 500);
      list.appendChild(li);
    } else {
      list.innerHTML = "<li>Ingen flashcards generert.</li>";
    }
  } catch (err) {
    console.error("Flashcards error:", err);
    list.innerHTML = "<li>❌ Kunne ikke generere flashcards. Kontroller at teksten ble analysert riktig.</li>";
  }
}

// Save settings (future feature)
function saveSettings() {
  const summaryLength = document.getElementById('summaryLength').value;
  const flashcardCount = document.getElementById('flashcardCount').value;
  const language = document.getElementById('language').value;

  console.log("Settings saved:", {
    summaryLength,
    flashcardCount,
    language,
  });

  alert("✅ Innstillinger lagret!");

  // Regenerate flashcards with new count if we already have text
  if (lastUploadedText) {
    const count = parseInt(document.getElementById('flashcardCount').value || "5", 10);
    generateFlashcards(lastUploadedText, count);
  }
}