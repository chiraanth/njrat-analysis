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

📘 [**Data README**](data/README.md) – Explains all `.txt` and `.pcapng` evidence files used during analysis  
🔧 [**Tools README**](tools/README.md) – Describes the custom Python script and its automation logic  
📄 [**Report Summary **](report/README.md) – Shortened version of the final malware analysis writeup

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

## 🚀 Usage Instructions

1. **Clone the repo**
```bash
git clone https://github.com/chiraanth/njrat-analysis.git
cd njrat-analysis
```

2. **Run the registry filter tool**
```bash
cd tools
python regshot_parser.py
```
✅ Make sure `regshot.txt` is present in the `data/` folder. A filtered `.txt` summary will be generated.

---

## 📌 Notes
- All artifacts are **sanitized**.
- This repository is meant for **academic and research purposes only**.
- ❌ No live malware samples are included.

---

## 📜 License
This project is licensed for academic, educational, and research use only. Commercial use is not permitted.

