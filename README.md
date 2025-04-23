# 🛡️ njRAT Malware Analysis & Toolkit Repository

This repository contains a comprehensive malware analysis of a suspected njRAT sample. It includes forensic artifacts, reverse engineering insights, dynamic behavior logs, and a custom-built automation tool designed to assist malware analysts during repetitive and tedious registry diff analysis.

---

## 📁 Repository Structure

```
.
├── data/         # Raw analysis artifacts (network, registry, strings, decompiled code)
├── tools/        # Custom tools and scripts built during analysis
├── report/       # Project report and documentation
```

📘 [**Evidence Summary**](data/README.md) – Explains all `.txt` and `.pcapng` evidence files used during analysis  
🔧 [**Tools Summary**](tools/README.md) – Describes the custom Python script and its automation logic  
📄 [**Report Summary**](report/README.md) – Shortened version of the final malware analysis writeup

---

## 📂 File-by-File Significance

### 📘 data/
- **FUN_0040a000.txt**: Decompiled function dump from Ghidra.
- **inetsim.txt**: Captured logs from simulated C2 traffic.
- **regshot.txt**: Registry snapshot diff after execution.
- **strings.txt**: Extracted hardcoded strings.
- **wireshark_njrat.pcapng**: Full packet capture of runtime behavior.

### 🔧 tools/
- **regshot_parser.py**:
  - Filters noisy registry diff logs.
  - Matches keywords like `UserAssist`, `Startup`, `WindowsUpdate`, etc.
  - Outputs filtered `.txt` summary to ease report writing.

### 📄 report/
- **final_report.docx**:
  - Covers static, dynamic, hybrid analysis.
  - Includes Ghidra, Process Monitor, network + registry artifacts.
  - Screenshots, decoded values, and conclusions.

---
🛠️ \*\*Automation Tool Overview: \*\***`regshot_parser.py`**

This script simplifies registry diff analysis by automatically filtering `regshot.txt` output for malware-relevant indicators.

**Key Features:**

- Parses the raw Regshot diff output
- Filters `Keys Added` and `Values Modified` based on specific keywords
- Highlights entries related to persistence, user activity tracking, or system configuration changes
- Outputs a clean and timestamped `.txt` file summarizing all matches
- Tracks frequency of matched keywords

**Keyword Matching:**
Customizable inside the script by editing the `KEYWORDS` list. Defaults include:

```
['Run', 'Startup', 'UserAssist', 'WindowsUpdate', 'Action Center', 'Explorer', 'SessionInfo']
```

**How to Use:**

```bash
cd tools
python regshot_parser.py
```

📄 Output will be saved as `filtered_regshot_<timestamp>.html` and `filtered_regshot_<timestamp>.txt`

**📸 Screenshot **
Below is an example of what the filtered output looks like:
data/regshot_parser.png

---

🚀 **Usage Instructions**

1. Clone the repo:

```bash
git clone https://github.com/chiraanth/njrat-analysis.git
cd njrat-analysis
```

2. Run the registry filter tool:

```bash
cd tools
python regshot_parser.py
```

✅ **Important:**

- The script will output a file named `filtered_regshot_<timestamp>.txt` in the same folder as the script.
- Open it in any text editor to review filtered registry keys.
- You can modify the list of keywords in the script by editing the `KEYWORDS` variable.

---

## 📌 Notes
- All artifacts are **sanitized**.
- This repository is meant for **academic and research purposes only**.
- ❌ No live malware samples are included.

---

## 📜 License
This project is licensed for academic, educational, and research use only. Commercial use is not permitted.

