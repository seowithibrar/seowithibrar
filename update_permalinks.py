import os
import glob
import re

# Define the mapping of old to new filenames
renames = {
    'blog-post-2.html': 'ultimate-guide-to-wordpress-speed-optimization.html',
    'blog-post-3.html': 'geo-generative-engine-optimization-vs-traditional-seo.html',
    'blog-post-4.html': 'seo-services-for-visa-consultancy.html',
    'blog-post-5.html': 'top-seo-experts-in-pakistan.html'
}

# 1. Update internal links in all HTML files
html_files = glob.glob('*.html')
for file in html_files:
    try:
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
            
        new_content = content
        for old, new in renames.items():
            # Use regex to replace exact occurrences within href attributes
            new_content = re.sub(rf'href="{old}"', f'href="{new}"', new_content)
            # Also replace if there are any trailing hashes just in case
            new_content = re.sub(rf'href="{old}#([^"]*)"', rf'href="{new}#\1"', new_content)
            
        if new_content != content:
            with open(file, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f'Updated links in {file}')
    except Exception as e:
        print(f"Error processing {file}: {e}")

# 2. Rename the files
for old, new in renames.items():
    if os.path.exists(old):
        os.rename(old, new)
        print(f'Renamed {old} -> {new}')
    elif os.path.exists(new):
        print(f'Already renamed to {new}')
    else:
        print(f'Could not find {old} to rename!')

