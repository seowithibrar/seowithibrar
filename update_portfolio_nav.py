import glob
import re

html_files = glob.glob('*.html')
for file in html_files:
    try:
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Update navigation links from index.html#portfolio to portfolio.html
        new_content = re.sub(r'href="index\.html#portfolio"', 'href="portfolio.html"', content)
        
        if new_content != content:
            with open(file, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f'Updated navigation link in {file}')
    except Exception as e:
        print(f"Error processing {file}: {e}")
