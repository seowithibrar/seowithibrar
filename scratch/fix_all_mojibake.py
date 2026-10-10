import glob
import re

files = glob.glob('*.html') + glob.glob('css/*.css') + glob.glob('js/*.js')

# Specific mojibake replacements
replacements = [
    # Right arrow variations
    ('ÃƒÂ¢Ã¢â‚¬Â ’', '&rarr;'),
    ('Ã¢â‚¬Â ’', '&rarr;'),
    ('â†’', '&rarr;'),
    
    # Down arrow variations
    ('ÃƒÂ¢Ã¢â‚¬Â “', '&darr;'),
    ('Ã¢â‚¬Â “', '&darr;'),
    ('â†“', '&darr;'),

    # Air plane
    ('ÃƒÂ¢Ã…â€œÃ‹â€ ️', '✈️'),
    ('ÃƒÂ¢Ã…â€œÃ‹â€ ', '✈️'),
    
    # Chart increasing
    ('ÃƒÂ°Ã…Â¸Ã¢â‚¬Å“Ã‹â€ ', '📈'),
    
    # Bar chart
    ('ÃƒÂ°Ã…Â¸Ã¢â‚¬Å“Ã…Â ', '📊'),
    ('ÃƒÂ°Ã…Â¸Ã¢â‚¬Å“Ã…Â', '📊'),
    
    # Tools / wrench
    ('ÃƒÂ°Ã…Â¸Ã¢â‚¬ÂºÃ‚Â ️', '🛠️'),
    ('ÃƒÂ°Ã…Â¸Ã¢â‚¬ÂºÃ‚Â ', '🛠️')
]

for fpath in files:
    with open(fpath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    modified = False
    for bad, good in replacements:
        if bad in content:
            content = content.replace(bad, good)
            modified = True
            
    if modified:
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Fixed mojibake in {fpath}")

print("Done fixing mojibake!")
