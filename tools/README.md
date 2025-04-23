# 🛠️ Tools Folder - njRAT Malware Analysis

This folder contains the Python automation tool developed as part of Section 10 of the njRAT analysis report. The tool was created to streamline a tedious but common task during malware investigation: identifying suspicious registry changes from Regshot logs.

---

## 🧪 Tool Overview: `regshot_parser.py`

### 📌 Purpose
After comparing two registry snapshots using Regshot, analysts receive a verbose diff log with hundreds of changes. This tool filters and highlights registry entries related to persistence, autorun, system modification, and user activity.

### 🔍 What It Detects
The script focuses on a rich set of keywords related to:
- **Persistence:** `Run`, `Startup`, `RunOnce`, `TaskScheduler`, `Winlogon`, `Userinit`
- **Network/Update:** `WindowsUpdate`, `ProxyServer`, `Dhcp`, `Tcpip`, `WinInet`
- **User Activity Tracking:** `UserAssist`, `Explorer`, `SessionInfo`, `TypedURLs`, `RecentDocs`
- **Malware TTPs:** `AppCompatFlags`, `Debugger`, `IFEO`, `AppInit_DLLs`, `Active Setup`
- **Hijacks & Misuse:** `BITS`, `SystemCertificates`, `FirewallPolicy`, `SafeBoot`, `PowerShell`

### ⚙️ How It Works
1. **Input:** Uses a file picker to select a Regshot diff file (`.txt`)
2. **Keyword Matching:** Searches for known suspicious strings in "Keys Added" and "Values Modified"
3. **Output Files:**
   - `filtered_<filename>_<timestamp>.txt`: Clean summary
   - `filtered_<filename>_<timestamp>.html`: Enhanced with match counts and highlighted terms

### 🧵 Sample Usage
```bash
cd tools
python regshot_parser.py
```

---

## 📸 Screenshot Example

![Filtered Output Preview](data/regshot_parser.png)


---

## 📁 File(s) in this Folder
- **regshot_parser.py** – Main script that automates Regshot diff analysis.

---

## 📌 Disclaimer
This script was designed and tested for academic analysis purposes. It does not perform any real-time protection or detection and should only be used on Regshot output files generated in a safe, isolated environment.
