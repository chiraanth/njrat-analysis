# 📄  njRAT Malware Analysis

This is a summarized academic report documenting the complete malware analysis process for a sample njRAT binary.

---

## 🔍 Summary of Analysis

**Malware Sample:** njRAT Remote Access Trojan  
**Hash (SHA-256):** `c582b5864a67c2d63f8d3a8faf08b47e94646a96cd81abe507d8d08df13e40c4`

### 1. Static Analysis
- **Unpacked Sample:** PEiD confirmed the binary was not packed.
- **Strings:** Extracted hardcoded paths and hints of C2 functionality.
- **Imports:** Used `CreateFileW`, `RegSetValueExW`, and network APIs from `WININET.DLL` and `WSOCK32.DLL`.

### 2. Decompiled Behavior (Ghidra)
- Found dynamic loading of libraries, encrypted strings, and use of Windows registry API for persistence.

### 3. Dynamic Analysis
- **Network Behavior:** Outbound HTTP connections to fake INetSim endpoints; no DNS exfil observed in test.
- **Registry Changes:** Added keys under `UserAssist`, `WindowsUpdate`, and startup directories.
- **File System:** Dropped a `.url` file to the Startup folder for persistence.

### 4. Debugger Behavior
- Observed runtime calls to `CreateFileW` and `VirtualAlloc`, suggesting memory unpacking.
- Used x64dbg to analyze malware behavior and confirm file writes.

### 5. Automation Tool
- A Python-based Regshot parser was created to filter diff logs and highlight malware-related registry keys.
- This tool helps speed up analysis in future reverse engineering workflows.

---


## 📌 Disclaimer
No malicious code is included in this repository. All samples were analyzed in a controlled and isolated virtual environment.

This summary is shared for educational purposes only.

