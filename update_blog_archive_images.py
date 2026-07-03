import re
import glob

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
        
        # Robustly extract the featured image src
        image = 'images/ibrar.png'
        img_tags = re.findall(r'<img[^>]+>', html)
        for img_tag in img_tags:
            if 'post-featured-image' in img_tag:
                src_match = re.search(r'src="([^"]+)"', img_tag)
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
