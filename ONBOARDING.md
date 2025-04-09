# 🛍 ONBOARDING.md – Welcome to SyncFX

Welcome to **SyncFX** – a plugin that syncs music beats to video cuts and effects inside Adobe Premiere Pro.

This onboarding doc will help developers set up, contribute, and collaborate effectively as part of the SyncFX team.

---

## 🔧 Local Setup Instructions

### 1. Prerequisites
- GitHub account (and collaborator access to the repo)
- Git installed: https://git-scm.com/
- GitHub Desktop (preferred for all devs): https://desktop.github.com/
- Python 3.10+ installed
- Node.js installed (optional – for bridge integration)
- VS Code (recommended)
- Adobe Premiere Pro (optional for plugin testing)

---

### 2. Cloning the Repo

Use GitHub Desktop to clone the project:

1. Click "Clone a repository from the Internet"
2. Paste this URL: `https://github.com/SyncFXPro/SyncFX.git`
3. Choose a local folder (example: `H:\SyncFX`)

✅ Now you’re working locally.

---

### 3. Running Beat Detection (Python)

Install required libraries:
```bash
pip install librosa
```

Run detection manually:
```bash
python engine/beat_detector.py sample.mp3
```

Or via JS bridge:
```bash
node bridge/run_python.js
```

You should see beat timestamps printed to the terminal.

---

### 4. Git Workflow: Push & Pull

#### Pushing your changes:
Use the `push.bat` script (provided) to:
- Stage all files
- Prompt you for a commit message
- Push to GitHub

#### Pulling updates:
Use `GitHub Desktop → Fetch origin → Pull` every time before you start your workday.

✅ This prevents conflicts and ensures your code is synced.

---

## 🧠 Git Basics for Collaboration

### 💡 What happens when multiple devs edit the same file?

#### Scenario: Different lines or functions
✅ Git will merge everything automatically. Your work and Sasha’s will both appear in the file.

#### Scenario: Same line
⚠️ Git will flag a conflict. You’ll see both versions and will need to manually choose one.

```diff
<<<<<<< HEAD
tempo = 120
=======
tempo = 135
>>>>>>> sasha-branch
```

✅ Resolve it by picking the correct value, then commit.

---

## 📁 Folder Structure

```text
SyncFX/
├── engine/         # Python beat detection
│   └── beat_detector.py
├── plugin/         # Premiere Pro panel (CEP)
│   ├── index.html
│   ├── index.js
│   └── manifest.xml
├── bridge/         # JS-Python communication
│   └── run_python.js
├── sample.mp3      # Test file
├── push.bat        # Push to GitHub helper
├── sync.bat        # Pull from GitHub helper
├── README.md
├── ONBOARDING.md   # You're here
```

---

## 📌 Tasks, Issues & Tracking

We use **GitHub Issues** to:
- Track bugs
- Assign tasks
- Plan features

Go to: `https://github.com/SyncFXPro/SyncFX/issues`

> Use Google Docs and Sheets for high-level planning, roadmaps, and brainstorming.

---

## 🙌 Final Notes

- Always commit before pulling
- Pull every day before starting
- Don't be afraid of merge conflicts – they’re normal
- Ask questions. Automate everything. Build together

Welcome to the team 🧠⚙️