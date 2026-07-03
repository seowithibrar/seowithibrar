import glob
import re

blog_slugs = [
    'ultimate-guide-to-wordpress-speed-optimization',
    'geo-generative-engine-optimization-vs-traditional-seo',
    'seo-services-for-visa-consultancy',
    'top-seo-experts-in-pakistan'
]

html_files = glob.glob('*.html')
for file in html_files:
    try:
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
            
        new_content = content
        for slug in blog_slugs:
            # Replace href="slug.html" with href="slug"
            new_content = re.sub(rf'href="{slug}\.html"', f'href="{slug}"', new_content)
            # Replace href="slug.html#section" with href="slug#section"
            new_content = re.sub(rf'href="{slug}\.html#([^"]*)"', rf'href="{slug}#\1"', new_content)
            
        if new_content != content:
            with open(file, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f'Removed .html extensions from links in {file}')
    except Exception as e:
        print(f"Error processing {file}: {e}")
