import glob
import re

html_files = glob.glob('*.html')
css_files = glob.glob('css/*.css')

def check_css_text(source_name, text):
    lines = text.split('\n')
    for idx, line in enumerate(lines, 1):
        clean = re.sub(r'/\*.*?\*/', '', line).strip()
        if not clean or clean.startswith('/*') or clean.startswith('*'):
            continue
        
        # Check unmatched single quote
        sq = clean.count("'")
        if sq % 2 != 0:
            print(f"[{source_name}:{idx}] Unmatched single quote: {clean}")
            
        # Check unmatched double quote
        dq = clean.count('"')
        if dq % 2 != 0:
            print(f"[{source_name}:{idx}] Unmatched double quote: {clean}")
            
        # Check unmatched parens
        if clean.count('(') != clean.count(')'):
            print(f"[{source_name}:{idx}] Unmatched parenthesis: {clean}")

for cf in css_files:
    with open(cf, 'r', encoding='utf-8', errors='ignore') as f:
        check_css_text(cf, f.read())

for hf in html_files:
    with open(hf, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    styles = re.findall(r'<style[^>]*>(.*?)</style>', content, re.DOTALL | re.IGNORECASE)
    for i, s in enumerate(styles):
        check_css_text(f"{hf} <style>", s)
