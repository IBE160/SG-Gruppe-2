

// script.js – AI Study Buddy Frontend Prototype

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
      throw new Error(`Feil ved opplasting: ${response.statusText}`);
    }

    const result = await response.json();
    console.log("Backend response:", result);

    uploadStatus.innerText = "✅ Fil lastet opp og analysert!";
    uploadStatus.style.color = "green";

    showSection("results");

    // Placeholder: Display content in results
    document.getElementById("summary").innerHTML = `
      <h3>Oppsummering</h3>
      <p>${result.summary || "Ingen oppsummering generert ennå."}</p>
    `;

  } catch (error) {
    console.error("Upload error:", error);
    uploadStatus.innerText = "❌ Noe gikk galt under opplasting.";
    uploadStatus.style.color = "red";
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
    language
  });

  alert("✅ Innstillinger lagret!");
}