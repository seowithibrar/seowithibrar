import re

path = r'c:\Users\mitec\OneDrive\Documents\GitHub\seowithibrar\top-seo-experts-in-pakistan.html'

with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Title
content = content.replace(
    'Top 15+ SEO Experts in Pakistan – Ibrar Leads the Way!',
    'Top 15+ SEO Experts in Pakistan <br> – Ibrar Leads the Way!'
)
content = content.replace(
    'Top 15+ SEO Experts in Pakistan â€“ Ibrar Leads the Way!',
    'Top 15+ SEO Experts in Pakistan <br> â€“ Ibrar Leads the Way!'
)

# 2. Featured Image Overlap
content = content.replace(
    'margin-top: -8rem; position: relative; z-index: 10;',
    'margin-top: 0; position: relative; z-index: 10;'
)

# 3. Expert Cards Layout
# Replace inline styles and structure
pattern = re.compile(
    r'<div class="premium-expert-card"[^>]*>\s*<div[^>]*>\s*<h3 id="([^"]+)" class="premium-expert-name">([^<]+)</h3>\s*</div>\s*<div class="premium-expert-image-col"[^>]*>\s*<div class="premium-expert-badge">(\d+)</div>\s*(<img[^>]+>)\s*</div>',
    re.MULTILINE | re.IGNORECASE
)
replacement = r"""<div class="premium-expert-card">
              <div class="premium-expert-header" style="display: flex; align-items: center; gap: 1rem; margin-bottom: 1rem;">
                <div class="premium-expert-badge" style="background: var(--color-primary); color: white; width: 40px; height: 40px; display: flex; align-items: center; justify-content: center; border-radius: 8px; font-weight: bold; font-size: 1.2rem;">\3</div>
                <h3 id="\1" class="premium-expert-name" style="margin: 0; font-size: 1.5rem;">\2</h3>
              </div>
              <div class="premium-expert-image-col" style="margin-bottom: 1rem;">
                \4
              </div>"""

content, count = pattern.subn(replacement, content)
print(f"Replaced {count} expert cards.")

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)
