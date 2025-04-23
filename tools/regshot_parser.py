import datetime
import os
import re
from collections import defaultdict, Counter
import tkinter as tk
from tkinter import filedialog
import webbrowser

# === CONFIGURATION ===
KEYWORD_CATEGORIES = {
    "🔁 Persistence": [
        'Run', 'RunOnce', 'Startup', 'Start Menu', 'Shell Folders', 'StartupApproved',
        'TaskCache', 'TaskScheduler', 'Winlogon', 'Userinit', 'Load', 'Logon', 'Policies\\Explorer'
    ],
    "🌐 Network & Updates": [
        'WindowsUpdate', 'Auto Update', 'Internet Settings', 'ProxyServer',
        'WinInet', 'Winsock', 'Tcpip', 'Dhcp'
    ],
    "🕵️ Surveillance / TTPs": [
        'UserAssist', 'Explorer', 'SessionInfo', 'Shell', 'Action Center', 'RecentDocs', 'TypedURLs',
        'AppCompatFlags', 'MUICache', 'BackgroundActivityModerator', 'AppInit_DLLs'
    ],
    "🔒 Malware-Specific / System Config": [
        'Services', 'App Paths', 'Debugger', 'Image File Execution Options', 'Command Processor',
        'SystemCertificates', 'Active Setup', 'KnownDLLs', 'PowerShell', 'WMI', 'AutorunsDisabled'
    ],
    "🧩 Monitoring / Hijack Indicators": [
        'Security Center', 'FirewallPolicy', 'SystemRestore', 'SafeBoot', 'BITS',
        'Software\\Classes\\exefile\\shell\\open\\command'
    ],
    "🛰️ C2 & Traffic Indicators": [
        'ZoneMap', 'Internet Explorer', 'BrowserEmulation', 'FeatureControl'
    ],
    "🧠 Heuristic Flags": [
        'LoadBehavior', 'Enable', 'Disable', 'Hidden', 'NoDriveTypeAutoRun', 'NoAutoUpdate'
    ]
}

ALL_KEYWORDS = [kw for kws in KEYWORD_CATEGORIES.values() for kw in kws]
timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M")

# === GUI FILE PICKER ===
root = tk.Tk()
root.withdraw()
INPUT_FILE = filedialog.askopenfilename(title="Select your Regshot diff file", filetypes=[("Text Files", "*.txt")])
if not INPUT_FILE:
    print("❌ No file selected. Exiting.")
    exit()

base_name = os.path.splitext(os.path.basename(INPUT_FILE))[0]
OUTPUT_HTML = f"filtered_{base_name}_{timestamp}.html"
OUTPUT_TXT = f"filtered_{base_name}_{timestamp}.txt"

# === FILTERING ===
filtered_lines = []
keyword_hits = Counter()
category_hits = defaultdict(Counter)

with open(INPUT_FILE, "r", encoding="utf-8", errors="ignore") as f:
    lines = f.readlines()

for line in lines:
    for category, keywords in KEYWORD_CATEGORIES.items():
        for k in keywords:
            if k.lower() in line.lower():
                filtered_lines.append(line.strip())
                keyword_hits[k] += 1
                category_hits[category][k] += 1
                break

# === SAVE TXT OUTPUT ===
with open(OUTPUT_TXT, "w", encoding="utf-8") as out:
    out.write("🧹 [FILTERED REGSHOT LINES MATCHING KEYWORDS]\n\n")
    if filtered_lines:
        out.writelines(line + "\n" for line in filtered_lines)
    else:
        out.write("(None matched keywords)\n")

    out.write("\n📊 [KEYWORD MATCH SUMMARY BY CATEGORY]\n\n")
    for category, hits in category_hits.items():
        out.write(f"{category}:\n")
        for k, v in hits.items():
            out.write(f"  - {k}: {v} times\n")
        out.write("\n")

# === HTML OUTPUT ===
def highlight_keywords(line):
    for k in ALL_KEYWORDS:
        pattern = re.compile(re.escape(k), re.IGNORECASE)
        line = pattern.sub(f"<strong style='color:red'>\\g<0></strong>", line)
    return line

with open(OUTPUT_HTML, "w", encoding="utf-8") as html:
    html.write("<html><head><style>body { font-family: monospace; }</style></head><body>")
    html.write(f"<h2>🧹 Filtered Regshot Lines ({len(filtered_lines)} matches)</h2><ul>")
    for line in filtered_lines:
        html.write(f"<li>{highlight_keywords(line)}</li>")
    html.write("</ul><hr><h3>📊 Keyword Match Frequency by Category</h3>")
    for category, hits in category_hits.items():
        html.write(f"<h4>{category}</h4><ul>")
        for k, v in hits.items():
            html.write(f"<li><strong>{k}</strong>: {v} times</li>")
        html.write("</ul>")
    html.write(f"<br><small>📅 Generated on {timestamp}</small></body></html>")

# === PRINT SUMMARY ===
print("✅ Analysis complete!")
print(f"Filtered lines: {len(filtered_lines)}")
print(f"Matched keywords: {sum(keyword_hits.values())}")
print(f"Saved text report to: {OUTPUT_TXT}")
print(f"Saved HTML report to: {OUTPUT_HTML}")
webbrowser.open(OUTPUT_HTML)