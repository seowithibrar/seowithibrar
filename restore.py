import subprocess
import re

# Get old CSS
old_css = subprocess.check_output(['git', 'show', 'HEAD:css/styles.css']).decode('utf-8')

# Extract old header/footer HTML from about.html
with open('about.html', 'r', encoding='utf-8') as f:
    about_html = f.read()

header_match = re.search(r'(<header class="navbar">.*?</header>)', about_html, re.DOTALL)
footer_match = re.search(r'(<footer class="footer new-mega-footer">.*?</footer>)', about_html, re.DOTALL)

old_header = header_match.group(1) if header_match else ''
old_footer = footer_match.group(1) if footer_match else ''

# Now replace in index.html
with open('index.html', 'r', encoding='utf-8') as f:
    index_html = f.read()

index_html = re.sub(r'<header class="navbar">.*?</header>', old_header, index_html, flags=re.DOTALL)
index_html = re.sub(r'<footer class="footer">.*?</footer>', old_footer, index_html, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(index_html)

# Now, we need to extract the Mega Menu CSS, Navbar CSS, and Footer CSS from old_css
with open('css/styles.css', 'a', encoding='utf-8') as f:
    f.write('\n\n/* ================= RESTORED OLD NAV & FOOTER CSS ================= */\n')
    
    # Simple strategy: just append the WHOLE old CSS, but wrapped inside specific selectors if needed? No, that would break things.
    # Better: specifically extract the components.
    
    # 1. Navigation CSS
    nav_match = re.search(r'(/\* =+[^=]*\n\s*Navigation[^=]*=+ \*/.*?)(?:/\* =+[^=]*\n\s*Hero[^=]*=+ \*/)', old_css, re.DOTALL | re.IGNORECASE)
    if nav_match:
        f.write(nav_match.group(1))
    
    # 2. Mega Menu CSS
    mega_menu_match = re.search(r'(\.mega-menu\b.*?)(?:/\* =+|$)', old_css, re.DOTALL | re.IGNORECASE)
    if mega_menu_match:
        f.write("\n/* Mega Menu Extracted */\n")
        # Extract until the next major comment block
        mm_css = old_css[mega_menu_match.start():]
        next_block = re.search(r'/\* =+', mm_css[10:])
        if next_block:
            mm_css = mm_css[:10+next_block.start()]
        f.write(mm_css)

    # 3. Footer CSS
    footer_match = re.search(r'(/\* =+[^=]*\n\s*Footer[^=]*=+ \*/.*?)(?:/\* =+|$)', old_css, re.DOTALL | re.IGNORECASE)
    if footer_match:
        f.write(footer_match.group(1))
        
    # 4. new-mega-footer CSS (might be separate from original footer)
    mega_footer_match = re.search(r'(\.new-mega-footer\b.*?)(?:/\* =+|$)', old_css, re.DOTALL | re.IGNORECASE)
    if mega_footer_match:
        f.write("\n/* Mega Footer Extracted */\n")
        mf_css = old_css[mega_footer_match.start():]
        next_block2 = re.search(r'/\* =+', mf_css[10:])
        if next_block2:
            mf_css = mf_css[:10+next_block2.start()]
        f.write(mf_css)

print('Header and Footer restored successfully.')
