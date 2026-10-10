import glob
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

files = glob.glob('*.html') + glob.glob('css/*.css') + glob.glob('js/*.js')

# Mojibake triggers
bad_tokens = ['Ã', 'Â', 'â€', 'â€™', 'â€”', 'â€œ', 'â€˜', 'â€¢', 'â–', 'âž']

results = {}

for fpath in sorted(files):
    with open(fpath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    matches = []
    lines = content.split('\n')
    for lno, line in enumerate(lines, 1):
        found = [b for b in bad_tokens if b in line]
        if found:
            matches.append((lno, found, line.strip()))
            
    if matches:
        results[fpath] = matches

print(f"Found mojibake in {len(results)} files:\n")
for fpath, matches in results.items():
    print(f"=== {fpath}: {len(matches)} occurrences ===")
    for lno, found, text in matches[:15]:
        print(f"  Line {lno} [{','.join(found)}]: {text[:140]}")
    if len(matches) > 15:
        print(f"  ... and {len(matches) - 15} more.")
    print()
