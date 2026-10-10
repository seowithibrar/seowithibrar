import glob
import re

css_files = glob.glob('css/*.css')
html_files = glob.glob('*.html')

def check_css_content(filename, content):
    # Remove comments
    stripped = re.sub(r'/\*.*?\*/', '', content, flags=re.DOTALL)
    
    # Check for unclosed braces or brackets
    if content.count('{') != content.count('}'):
        print(f"[BRACE MISMATCH] {filename}: open={content.count('{')}, close={content.count('}')}")
        
    # Find blocks { ... }
    # Nested blocks (like @media)
    # Simple regex block finder
    blocks = re.findall(r'([^{}]+)\{([^{}]*)\}', stripped)
    for selector, body in blocks:
        selector = selector.strip()
        lines = [d.strip() for d in body.split(';') if d.strip()]
        for decl in lines:
            if decl.startswith('@') or decl.startswith('from') or decl.startswith('to') or decl.endswith('%'):
                continue
            if ':' not in decl:
                print(f"[MISSING COLON] {filename} in '{selector[:40]}': '{decl}'")
            else:
                parts = decl.split(':', 1)
                prop = parts[0].strip()
                val = parts[1].strip()
                if not prop or not val:
                    print(f"[EMPTY PROP/VAL] {filename} in '{selector[:40]}': '{decl}'")
                if 'undefined' in val.lower():
                    print(f"[UNDEFINED VALUE] {filename} in '{selector[:40]}': '{decl}'")
                if 'nan' in val.lower() and not 'finance' in val.lower():
                    print(f"[NAN VALUE] {filename} in '{selector[:40]}': '{decl}'")

print("--- VALIDATING CSS FILES ---")
for cf in css_files:
    with open(cf, 'r', encoding='utf-8', errors='ignore') as f:
        check_css_content(cf, f.read())

print("--- VALIDATING HTML INLINE STYLES ---")
for hf in html_files:
    with open(hf, 'r', encoding='utf-8', errors='ignore') as f:
        html = f.read()
    styles = re.findall(r'<style[^>]*>(.*?)</style>', html, flags=re.DOTALL | re.IGNORECASE)
    for i, s in enumerate(styles):
        check_css_content(f"{hf} <style {i}>", s)
