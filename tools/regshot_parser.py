import datetime
import os
from collections import Counter
import tkinter as tk
from tkinter import filedialog
import webbrowser
# === CONFIG ===
KEYWORDS = [
    # Persistence-related
    'Run', 'RunOnce', 'Startup', 'Start Menu', 'Shell Folders', 'StartupApproved',
    'TaskCache', 'TaskScheduler', 'Winlogon', 'Userinit', 'Load', 'Logon', 'Policies\\Explorer',

    # Network & Update
    'WindowsUpdate', 'Auto Update', 'Internet Settings', 'ProxyServer', 'WinInet', 'Winsock', 'Tcpip', 'Dhcp',

    # System Surveillance / TTPs
    'UserAssist', 'Explorer', 'SessionInfo', 'Shell', 'Action Center', 'RecentDocs', 'TypedURLs', 'AppCompatFlags',
    'MUICache', 'BackgroundActivityModerator', 'AppInit_DLLs',

    # Misc and Malware-specific
    'Services', 'App Paths', 'Debugger', 'Image File Execution Options', 'Command Processor',
    'SystemCertificates', 'Active Setup', 'KnownDLLs', 'PowerShell', 'WMI', 'AutorunsDisabled',

    # Monitoring Tools / Hijack Traces
    'Security Center', 'FirewallPolicy', 'SystemRestore', 'SafeBoot', 'BITS',
    'Software\\Classes\\exefile\\shell\\open\\command',

    # C2 & Traffic Indicators
    'ZoneMap', 'Internet Explorer', 'BrowserEmulation', 'FeatureControl',

    # Misc heuristic indicators
    'LoadBehavior', 'Enable', 'Disable', 'Hidden', 'NoDriveTypeAutoRun', 'NoAutoUpdate',
]

timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M")

# === GUI FILE PICKER ===
root = tk.Tk()
root.withdraw()
INPUT_FILE = filedialog.askopenfilename(title="Select your Regshot diff file", filetypes=[("Text Files", "*.txt")])

if not INPUT_FILE:
    print(" No file selected. Exiting.")
    exit()

base_name = os.path.splitext(os.path.basename(INPUT_FILE))[0]
OUTPUT_HTML = f"filtered_{base_name}_{timestamp}.html"
OUTPUT_TXT = f"filtered_{base_name}_{timestamp}.txt"

# === PROCESSING ===
filtered_lines = []
keyword_hits = Counter()

with open(INPUT_FILE, "r", encoding="utf-8", errors="ignore") as f:
    lines = f.readlines()

for line in lines:
    for k in KEYWORDS:
        if k.lower() in line.lower():
            filtered_lines.append(line.strip())
            keyword_hits[k] += 1
            break  # Only count once per line

# === SAVE TXT OUTPUT ===
with open(OUTPUT_TXT, "w", encoding="utf-8") as out:
    out.write("[FILTERED REGSHOT LINES MATCHING KEYWORDS]\n")
    if filtered_lines:
        out.writelines(line + "\n" for line in filtered_lines)
    else:
        out.write("(None matched keywords)\n")

# === SAVE HTML OUTPUT ===
def highlight_keywords(line):
    for k in KEYWORDS:
        pattern = re.compile(re.escape(k), re.IGNORECASE)
        line = pattern.sub(f"<strong style='color:red'>\\g<0></strong>", line)
    return line


with open(OUTPUT_HTML, "w", encoding="utf-8") as html:
    html.write("<html><head><style>body { font-family: monospace; }</style></head><body>")
    html.write(f"<h2> Filtered Regshot Lines ({len(filtered_lines)} matches)</h2><ul>")
    for line in filtered_lines:
        html.write(f"<li>{highlight_keywords(line)}</li>")
    html.write("</ul><hr>")
    html.write("<h3> Keyword Match Frequency</h3><ul>")
    for k, v in keyword_hits.most_common():
        html.write(f"<li><strong>{k}</strong>: {v} times</li>")
    html.write("</ul><br><small>Generated on {}</small></body></html>".format(timestamp))

# === PRINT SUMMARY ===
print("\n Analysis complete!")
print(f" Filtered lines: {len(filtered_lines)}")
print(f" Keywords matched: {sum(keyword_hits.values())}")
print(f" Saved text file to: {OUTPUT_TXT}")
print(f" Saved HTML report to: {OUTPUT_HTML}")
webbrowser.open(OUTPUT_HTML)

if not filtered_lines:
    print(" No registry lines matched the given keywords. Try expanding the keyword list.")
