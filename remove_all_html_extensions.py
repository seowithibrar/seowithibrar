import glob
import re
import os

html_files = glob.glob('*.html')
for file in html_files:
    try:
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Regex to find href="something.html" or href="something.html#anchor"
        # Only targets relative local HTML files (not http:// or https://)
        # Matches href="page.html" and href="page.html#section"
        
        # This regex matches href=" followed by anything that isn't a quote or http, ends in .html, maybe #something
        new_content = re.sub(
            r'href="([^":/]+)\.html(#[^"]*)?"', 
            r'href="\1\2"', 
            content
        )
            
        if new_content != content:
            with open(file, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f'Removed .html extensions from links in {file}')
    except Exception as e:
        print(f"Error processing {file}: {e}")
