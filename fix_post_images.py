import re
import glob

files = glob.glob('blog-post-*.html')
for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        html = f.read()
    
    title_match = re.search(r'<h1 class="blog-hero-title">(.*?)</h1>', html)
    if title_match:
        title = title_match.group(1)
        slug = re.sub(r'[^a-z0-9]+', '-', title.lower()).strip('-')
        new_img_src = f'images/{slug}.webp'
        
        # Replace only the post-featured-image if it is ibrar.png
        html = re.sub(r'(<img[^>]*class="post-featured-image"[^>]*src=")images/ibrar\.png(")', r'\g<1>' + new_img_src + r'\2', html)
        
        with open(file, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f'Updated {file} to use {new_img_src}')
