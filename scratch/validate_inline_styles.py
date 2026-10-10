import glob
import re

html_files = glob.glob('*.html')

print("--- VALIDATING INLINE style=\"...\" ATTRIBUTES ---")
for hf in html_files:
    with open(hf, 'r', encoding='utf-8', errors='ignore') as f:
        html = f.read()
    
    # Find all style="..."
    inline_styles = re.findall(r'style="([^"]*)"', html, flags=re.IGNORECASE)
    for s in inline_styles:
        s = s.strip()
        if not s:
            continue
        # Check declarations
        decls = [d.strip() for d in s.split(';') if d.strip()]
        for d in decls:
            if ':' not in d:
                print(f"[MISSING COLON IN INLINE STYLE] {hf}: '{d}' in style='{s}'")
            else:
                prop, val = d.split(':', 1)
                prop = prop.strip()
                val = val.strip()
                if not prop or not val:
                    print(f"[EMPTY PROP/VAL IN INLINE STYLE] {hf}: '{d}'")
                if '?' in prop or '?' in val:
                    print(f"[QUESTION MARK IN INLINE STYLE] {hf}: '{d}'")
