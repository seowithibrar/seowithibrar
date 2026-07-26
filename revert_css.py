import os

css_path = r'c:\Users\mitec\OneDrive\Documents\GitHub\seowithibrar\css\styles.css'
with open(css_path, 'r', encoding='utf-8') as f:
    css_content = f.read()

# Find the marker where I appended the bad CSS
marker = "/* ==========================================================================\n   Premium SEO Editorial Redesign\n   ========================================================================== */"
if marker in css_content:
    clean_css = css_content.split(marker)[0]
    with open(css_path, 'w', encoding='utf-8') as f:
        f.write(clean_css)
    print("Reverted CSS.")
else:
    print("CSS marker not found.")
