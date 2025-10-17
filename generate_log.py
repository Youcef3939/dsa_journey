import os
import re

FOLDERS = ["arrays", "strings", "linked_lists", "dynamic_programming", "graphs"]
LOG_FILE = "DAILY_LOG.md"

log_entries = []

header_pattern = re.compile(r"^\s*(Problem|Difficulty|Date|Notes):\s*(.*)$", re.MULTILINE)

for folder in FOLDERS:
    path = os.path.join(os.getcwd(), folder)
    if not os.path.exists(path):
        continue
    for file in sorted(os.listdir(path)):
        if file.endswith(".py"):
            with open(os.path.join(path, file), encoding="utf-8") as f:
                content = f.read()
                header_info = {k: "N/A" for k in ["Problem", "Difficulty", "Date", "Notes"]}
                for match in header_pattern.findall(content):
                    key, value = match
                    header_info[key] = value.strip()
                log_entries.append(header_info)

log_entries.sort(key=lambda x: x["Date"])

with open(LOG_FILE, "w", encoding="utf-8") as f:
    f.write("| Day | Date | Problem | Difficulty | Notes |\n")
    f.write("|-----|------|---------|------------|-------|\n")
    for idx, entry in enumerate(log_entries, 1):
        f.write(f"| {idx} | {entry['Date']} | {entry['Problem']} | {entry['Difficulty']} | {entry['Notes']} |\n")

print(f"{LOG_FILE} updated with {len(log_entries)} entries")