import glob
import re

html_files = sorted(glob.glob('*.html'))

for page in html_files:
    print(f"\n==================== {page} ====================")
    with open(page, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    # 1. Check style tag syntax & content: '?'
    styles = re.findall(r'<style[^>]*>(.*?)</style>', content, re.DOTALL | re.IGNORECASE)
    q_matches = []
    for s_idx, s in enumerate(styles):
        lines = s.split('\n')
        for l_num, line in enumerate(lines, 1):
            if "content: '?'" in line or 'content: "?"' in line:
                q_matches.append(f"Style block line {l_num}: {line.strip()}")
            if "content:" in line and ("?" in line or "\\\\" in line):
                q_matches.append(f"Special content line {l_num}: {line.strip()}")
                
    if q_matches:
        print("  [CORRUPTED CONTENT]:")
        for q in q_matches:
            print("   -", q)
    else:
        print("  - No corrupted content: '?' found in <style>")

    # 2. Check for unmatched braces in <style>
    for s_idx, s in enumerate(styles):
        if s.count('{') != s.count('}'):
            print(f"  [BRACE MISMATCH in <style {s_idx}>]: open={s.count('{')}, close={s.count('}')}")

    # 3. Check for undefined var(--...)
    used_vars = set(re.findall(r'var\((--[a-zA-Z0-9_-]+)', content))
    # Check against styles.css
    with open('css/styles.css', 'r', encoding='utf-8') as sf:
        styles_css = sf.read()
    defined_vars = set(re.findall(r'(--[a-zA-Z0-9_-]+)\s*:', styles_css))
    page_vars = set(re.findall(r'(--[a-zA-Z0-9_-]+)\s*:', content))
    all_defs = defined_vars.union(page_vars)
    missing = [v for v in used_vars if v not in all_defs]
    if missing:
        print(f"  [MISSING CSS VARS]: {missing}")
    else:
        print("  - All CSS variables resolved")
        
    # 4. Check for unclosed <style> tag or duplicate DOCTYPE
    if content.count('<!DOCTYPE') > 1:
        print(f"  [DUPLICATE DOCTYPE]: count={content.count('<!DOCTYPE')}")
    if content.count('<html') > 1:
        print(f"  [DUPLICATE <HTML>]: count={content.count('<html')}")
    if content.count('<head') > 1:
        print(f"  [DUPLICATE <HEAD>]: count={content.count('<head')}")
