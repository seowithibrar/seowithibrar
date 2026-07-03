import glob
import os
from datetime import datetime

html_files = glob.glob('*.html')
base_url = "https://seowithibrar.com"

# XML Header
sitemap = '<?xml version="1.0" encoding="UTF-8"?>\n'
sitemap += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'

for file in html_files:
    # Exclude any 404 pages if they exist
    if '404' in file:
        continue
        
    # Remove .html extension
    slug = file.replace('.html', '')
    
    # Handle index.html as root
    if slug == 'index':
        url = f"{base_url}/"
        priority = "1.0"
    else:
        url = f"{base_url}/{slug}"
        priority = "0.8"
        
    lastmod = datetime.fromtimestamp(os.path.getmtime(file)).strftime('%Y-%m-%d')
    
    sitemap += '  <url>\n'
    sitemap += f'    <loc>{url}</loc>\n'
    sitemap += f'    <lastmod>{lastmod}</lastmod>\n'
    sitemap += '    <changefreq>weekly</changefreq>\n'
    sitemap += f'    <priority>{priority}</priority>\n'
    sitemap += '  </url>\n'

sitemap += '</urlset>'

with open('sitemap.xml', 'w', encoding='utf-8') as f:
    f.write(sitemap)
    
print("sitemap.xml generated successfully!")
