# 🛠️ Tools Folder - njRAT Malware Analysis

This folder contains the Python automation tool developed as part of Section 10 of the njRAT analysis report. The tool was created to streamline a tedious but common task during malware investigation: identifying suspicious registry changes from Regshot logs.

---

## 🧪 Tool Overview: `regshot_parser.py`

### 📌 Purpose
After comparing two registry snapshots using Regshot, analysts receive a verbose diff log with hundreds of changes. This tool filters and highlights registry entries related to persistence, autorun, system modification, and user activity.

### 🔍 What It Detects
The script focuses on keywords such as:
- `Run`, `Startup`, `UserAssist`, `Explorer`
- `WindowsUpdate`, `SessionInfo`, `Action Center`

### ⚙️ How It Works
1. **Input:** Takes a Regshot diff file (text format) as input.
2. **Filtering:** Extracts "Keys Added" and "Values Modified" sections.
3. **Keyword Matching:** Filters lines that match suspicious registry-related keywords.
4. **Output:** Generates a timestamped filtered report showing only the relevant entries.

### 🧵 Sample Usage
```bash
python regshot_parser.py
```
Make sure the `INPUT_FILE` variable is correctly set to your Regshot `.txt` file.

---

## 📁 File(s) in this Folder
- **regshot_parser.py** – The main Python script for registry diff filtering.

---

## 📌 Disclaimer
This script was designed and tested for academic analysis purposes. It does not perform any real-time protection or detection and should only be used on Regshot output files generated in a safe, isolated environment.

