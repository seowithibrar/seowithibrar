import glob
import re

# Collect all defined CSS variables
css_files = glob.glob('css/*.css')
html_files = glob.glob('*.html')

defined_vars = set()
for cf in css_files:
    with open(cf, 'r', encoding='utf-8', errors='ignore') as f:
        matches = re.findall(r'(--[a-zA-Z0-9_-]+)\s*:', f.read())
        defined_vars.update(matches)

print(f"Total defined CSS variables in CSS files: {len(defined_vars)}")

# Check variables used in HTML files and CSS files
used_vars = set()
for cf in css_files:
    with open(cf, 'r', encoding='utf-8', errors='ignore') as f:
        matches = re.findall(r'var\((--[a-zA-Z0-9_-]+)', f.read())
        for v in matches:
            if v not in defined_vars:
                print(f"[UNDEFINED VAR IN {cf}]: {v}")

for hf in html_files:
    with open(hf, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    page_vars = set(re.findall(r'(--[a-zA-Z0-9_-]+)\s*:', content))
    all_defined = defined_vars.union(page_vars)
    matches = re.findall(r'var\((--[a-zA-Z0-9_-]+)', content)
    for v in matches:
        if v not in all_defined:
            print(f"[UNDEFINED VAR IN {hf}]: {v}")
