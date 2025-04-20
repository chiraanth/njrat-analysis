# 📁 Data Folder - njRAT Malware Analysis

This folder contains supporting files used throughout the analysis of the njRAT malware sample. These include output logs from tools, extracted metadata, and artifacts from both static and dynamic analysis.

---

## 📂 Contents

### 🔸 `strings.txt`
- Extracted using the `strings` utility from the njRAT binary.
- Used to identify suspicious filenames, URLs, registry paths, and other hardcoded artifacts.

### 🔸 `FUN_0040a000.txt`
- Decompiled function dump from Ghidra.
- Key logic related to runtime behavior and obfuscation is analyzed in Section 4 of the report.

### 🔸 `wireshark_njrat.pcapng`
- Captured during dynamic analysis using Wireshark.
- Shows HTTP connection attempts to fake INetSim endpoints.

### 🔸 `inetsim.txt`
- Logs from INetSim (Internet Services Simulation) used to simulate common services during the malware's network activity.
- Helps verify C2-like behavior.

### 🔸 `regshot.txt`
- Output of registry differences captured via Regshot.
- Used to analyze persistence mechanisms and registry modifications (Section 6).

---

## 📎 Usage Notes
- All files were generated in a controlled Windows 7 VM.
- No live malware is present in this folder.
- These files serve as references for analysis and validation of tool functionality (e.g., `regshot_parser.py`).

---

## ⚠️ Disclaimer
This folder **does not** contain any active malware. All artifacts were collected for academic purposes and are safe for reference and educational analysis only.

