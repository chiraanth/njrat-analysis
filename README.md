# njRAT Malware Analysis & Toolkit Repository

This repository contains a comprehensive malware analysis of a suspected njRAT sample. It includes forensic artifacts, reverse engineering insights, dynamic behavior logs, and a custom-built automation tool designed to assist malware analysts during repetitive and tedious registry diff analysis.

---

## Repository Structure

```
.
├── data/
│   ├── FUN_0040a000.txt          # Decompiled/reversed function output (possibly unpacked) from the malware binary
│   ├── inetsim.txt               # Output from INetSim analysis simulating C2 communications
│   ├── regshot.txt               # Registry diff before and after malware execution
│   ├── strings.txt               # All extracted strings from the malware binary
│   ├── wireshark_njrat.pcapng   # Packet capture of malware traffic (e.g., C2, DNS, HTTP requests)
│
├── tools/
│   └── regshot_parser.py         # Custom Python script to parse and filter registry diffs by malware-relevant keywords
│
├── report/
│   └── final_report.docx         # Full written report documenting static, dynamic, and hybrid analysis with screenshots
```

---

## File-by-File Significance

### data/
- **FUN_0040a000.txt**
  - Contains reverse engineered disassembly or decompiled output from a key malware function.
  - Helps reveal string decryption, API calls, or logic used for unpacking or persistence.

- **inetsim.txt**
  - Logs captured by INetSim that show how the malware attempts to reach external endpoints.
  - Includes fake DNS resolution, HTTP beaconing, and fake SMTP/FTP interactions.

- **regshot.txt**
  - Raw output of a registry comparison done before and after running the malware.
  - Used to identify persistence techniques like autorun keys, WindowsUpdate tampering, or UserAssist artifacts.

- **strings.txt**
  - All ASCII/Unicode strings pulled from the malware binary.
  - Useful to locate file paths, domains, mutexes, or hardcoded indicators.

- **wireshark_njrat.pcapng**
  - Captures live network traffic during sandboxed malware execution.
  - Validates attempts to connect to a C2 server, download additional payloads, or exfiltrate data.

### tools/
- **regshot_parser.py**
  - An automation script that filters out only malware-relevant registry keys from the full Regshot diff.
  - Looks for keywords like: `Run`, `UserAssist`, `Startup`, `WindowsUpdate`, `Action Center`, etc.
  - Outputs a timestamped HTML file showing only matches and match counts, making manual review faster.

### report/
- **final_report.docx**
  - The complete write-up that includes:
    - Static analysis with tools like PEiD, strings, and disassemblers.
    - Dynamic analysis using x32dbg, Process Monitor, INetSim.
    - Registry and file system changes.
    - Packet-level network behavior.
    - Automation (Section 10): the regshot_parser tool and its usage.
    - Screenshots and analysis walkthroughs.

---

## Usage Instructions

1. Clone the repo:
   ```bash
   git clone https://github.com/chiraanth/njrat-analysis.git
   cd njrat-analysis
   ```

2. To run the automation tool:
   ```bash
   cd tools
   python regshot_parser.py
   ```
   Ensure that a regshot file is present. The script will create a filtered `.html` file summarizing matches.

---

## Notes
- All artifacts are anonymized or sanitized.
- This repository is for **educational and academic research purposes only**.
- No live malware samples are hosted here.


## License
This project is licensed for academic, educational, and research use only. Commercial use is not permitted.

