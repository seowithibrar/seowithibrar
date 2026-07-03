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
        
        # Replace ibrar.png with the new slug ONLY if it's on a line containing 'post-featured-image'
        lines = html.split('\n')
        new_lines = []
        for line in lines:
            if 'post-featured-image' in line and 'images/ibrar.png' in line:
                line = line.replace('images/ibrar.png', new_img_src)
            new_lines.append(line)
            
        new_html = '\n'.join(new_lines)
        
        with open(file, 'w', encoding='utf-8') as f:
            f.write(new_html)
        print(f'Updated {file} to use {new_img_src}')

# Now regenerate the blog archive cards
def generate_dark_blog_archive():
    files = glob.glob('blog-post-*.html')
    files.sort()
    
    cards_html = ""
    categories = set()
    
    for file in files:
        with open(file, 'r', encoding='utf-8') as f:
            html = f.read()
            
        title_match = re.search(r'<h1 class="blog-hero-title">(.*?)</h1>', html)
        title = title_match.group(1) if title_match else 'Untitled Post'
        
        cat_match = re.search(r'<div class="blog-hero-category">(.*?)</div>', html)
        category = cat_match.group(1) if cat_match else 'Blog'
        categories.add(category)
        
        excerpt_match = re.search(r'<p class="post-excerpt"[^>]*>(.*?)</p>', html)
        excerpt = excerpt_match.group(1) if excerpt_match else 'Read our latest blog post on SEO With Ibrar.'
        
        # Find the image src in the line with 'post-featured-image'
        image = 'images/ibrar.png'
        for line in html.split('\n'):
            if 'post-featured-image' in line:
                src_match = re.search(r'src="([^"]+)"', line)
                if src_match:
                    image = src_match.group(1)
                    break
        
        card = f"""
                <div class="dark-blog-card" data-category="{category}">
                    <div class="dark-blog-image">
                        <img src="{image}" alt="{title}" loading="lazy">
                    </div>
                    <div class="dark-blog-content">
                        <div class="dark-blog-meta">
                            <span class="dark-blog-category">{category}</span>
                        </div>
                        <h3 class="dark-blog-title"><a href="{file}">{title}</a></h3>
                        <p class="dark-blog-excerpt">{excerpt}</p>
                    </div>
                </div>
"""
        cards_html += card
        
    with open('blog.html', 'r', encoding='utf-8') as f:
        blog_html = f.read()
        
    blog_html = re.sub(r'(<div class="dark-blog-grid"[^>]*>).*?(</div>\s*</div>\s*</main>)', r'\1\n' + cards_html + r'            \2', blog_html, flags=re.DOTALL)
    
    with open('blog.html', 'w', encoding='utf-8') as f:
        f.write(blog_html)
        
    print("Updated blog.html cards with accurate featured images.")

generate_dark_blog_archive()
