import glob
import re
import json

files = glob.glob('*.html')
report = {}

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
        
    has_meta_desc = bool(re.search(r'<meta name="description"', content, flags=re.IGNORECASE))
    has_canonical = bool(re.search(r'<link rel="canonical"', content, flags=re.IGNORECASE))
    has_og = bool(re.search(r'property="og:', content, flags=re.IGNORECASE))
    has_schema = bool(re.search(r'type="application/ld\+json"', content, flags=re.IGNORECASE))
    
    h1s = re.findall(r'<h1.*?>.*?</h1>', content, flags=re.IGNORECASE | re.DOTALL)
    
    images = re.findall(r'<img[^>]+>', content, flags=re.IGNORECASE)
    missing_alt = [img for img in images if 'alt=' not in img.lower()]
    
    report[file] = {
        'has_meta_desc': has_meta_desc,
        'has_canonical': has_canonical,
        'has_og_tags': has_og,
        'has_schema': has_schema,
        'h1_count': len(h1s),
        'images_missing_alt': len(missing_alt)
    }

print(json.dumps(report, indent=2))
