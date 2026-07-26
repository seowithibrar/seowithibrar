import re

path = r'c:\Users\mitec\OneDrive\Documents\GitHub\seowithibrar\top-seo-experts-in-pakistan.html'

with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Title
content = content.replace(
    'Top 15+ SEO Experts in Pakistan – Ibrar Leads the Way!',
    'Top 15+ SEO Experts in Pakistan <br> – Ibrar Leads the Way!'
)
content = content.replace(
    'Top 15+ SEO Experts in Pakistan â€“ Ibrar Leads the Way!',
    'Top 15+ SEO Experts in Pakistan <br> â€“ Ibrar Leads the Way!'
)

# 2. Featured Image Overlap
content = content.replace(
    '<div class="container article-layout-grid" style="margin-top: -3rem; position: relative; z-index: 10;">',
    '<div class="container article-layout-grid" style="margin-top: 4rem; position: relative; z-index: 10;">'
)
content = content.replace(
    'style="border-radius: 20px; box-shadow: 0 20px 40px rgba(0,0,0,0.1); margin-top: -8rem; position: relative; z-index: 10; border: 8px solid #fff;"',
    'style="border-radius: 20px; box-shadow: 0 20px 40px rgba(0,0,0,0.1); margin-top: 0; position: relative; z-index: 10; border: 8px solid #fff;"'
)

# 3. Expert Cards Layout
# The old HTML has style attributes like:
# <div class="premium-expert-card" style="...">
#   <div style="...">
#     <h3 id="m-tanveer-nandla" class="premium-expert-name">M. Tanveer Nandla</h3>
#   </div>
#   <div class="premium-expert-image-col" style="...">
#     <div class="premium-expert-badge">1</div>
#     <img ...>
#   </div>

pattern = re.compile(
    r'<div class="premium-expert-card"[^>]*>\s*<div[^>]*>\s*<h3 id="([^"]+)" class="premium-expert-name">([^<]+)</h3>\s*</div>\s*<div class="premium-expert-image-col"[^>]*>\s*<div class="premium-expert-badge">(\d+)</div>\s*(<img[^>]+>)\s*</div>',
    re.MULTILINE | re.IGNORECASE
)
replacement = r"""<div class="premium-expert-card">
              <div class="premium-expert-header">
                <div class="premium-expert-badge">\3</div>
                <h3 id="\1" class="premium-expert-name">\2</h3>
              </div>
              <div class="premium-expert-image-col">
                \4
              </div>"""

content, count = pattern.subn(replacement, content)
print(f"Replaced {count} expert cards.")

# 4. Sidebar and Bottom Content
sidebar_html = """
        <!-- Bottom Post Navigation & Related -->
        <div class="post-navigation">
          <div class="nav-links prev">
            <span class="nav-label">Previous Post</span>
            <a href="#" class="nav-title">How to Optimize WordPress Speed in 2026</a>
          </div>
          <div class="nav-links next">
            <span class="nav-label">Next Post</span>
            <a href="#" class="nav-title">Top 10 Local SEO Strategies for Agencies</a>
          </div>
        </div>

        <div class="bottom-related-posts">
          <h3>Related Articles</h3>
          <div class="related-cards-grid">
            <div class="sidebar-widget">
              <h4 style="margin: 0 0 10px 0;"><a href="#" style="text-decoration: none; color: #0f172a;">SEO Audit Checklist</a></h4>
              <p style="font-size: 0.9rem; color: #4b5563;">Complete guide to auditing your website.</p>
            </div>
            <div class="sidebar-widget">
              <h4 style="margin: 0 0 10px 0;"><a href="#" style="text-decoration: none; color: #0f172a;">Link Building 101</a></h4>
              <p style="font-size: 0.9rem; color: #4b5563;">How to get high quality backlinks safely.</p>
            </div>
          </div>
        </div>

        <div class="bottom-cta-banner">
          <h2>Ready to Rank Higher?</h2>
          <p>Get a custom SEO strategy tailored to your business goals. Our experts are here to help you dominate search results.</p>
          <a href="contact.html" class="btn btn-primary" style="font-size: 1.1rem; padding: 16px 32px;">Book Free Consultation</a>
        </div>
      </article>

      <aside class="blog-sidebar">
        <!-- Table of Contents -->
        <div class="sidebar-widget">
          <div class="sidebar-widget-title">Table of Contents</div>
          <ul class="toc-list">
            <li><a href="#introduction">Introduction</a></li>
            <li><a href="#list-of-top-seo-experts">List of Top SEO Experts</a></li>
            <li><a href="#m-tanveer-nandla" class="toc-h3">1. M. Tanveer Nandla</a></li>
            <li><a href="#salman-baig" class="toc-h3">2. Salman Baig</a></li>
            <li><a href="#aleem-iqbal" class="toc-h3">3. Aleem Iqbal</a></li>
            <li><a href="#saad-raza" class="toc-h3">4. Saad Raza</a></li>
            <li><a href="#ibrar-ahmad-(seowithibrar)" class="toc-h3">5. Ibrar Ahmad</a></li>
            <li><a href="#imran-khadim" class="toc-h3">6. Imran Khadim</a></li>
            <li><a href="#usman-latif" class="toc-h3">7. Usman Latif</a></li>
          </ul>
        </div>

        <!-- Call To Action -->
        <div class="sidebar-widget cta-widget">
          <div class="sidebar-widget-title">Need Expert SEO?</div>
          <p>Boost your organic traffic and outrank competitors with our proven SEO strategies.</p>
          <a href="contact.html" class="btn btn-primary" style="padding: 12px 0;">Contact Us Now</a>
        </div>

        <!-- Related Posts -->
        <div class="sidebar-widget">
          <div class="sidebar-widget-title">Related Posts</div>
          <div class="related-post-item">
            <img src="images/top-seo-experts-pakistan.webp" alt="SEO Post">
            <div class="related-post-item-content">
              <h4><a href="#">Technical SEO Guide 2026</a></h4>
              <div class="related-post-date">July 10, 2026</div>
            </div>
          </div>
          <div class="related-post-item">
            <img src="images/top-seo-experts-pakistan.webp" alt="SEO Post">
            <div class="related-post-item-content">
              <h4><a href="#">Content Strategy for Agencies</a></h4>
              <div class="related-post-date">July 5, 2026</div>
            </div>
          </div>
          <div class="related-post-item">
            <img src="images/top-seo-experts-pakistan.webp" alt="SEO Post">
            <div class="related-post-item-content">
              <h4><a href="#">Local SEO Masterclass</a></h4>
              <div class="related-post-date">June 28, 2026</div>
            </div>
          </div>
        </div>
      </aside>
"""

if "<!-- Bottom Post Navigation & Related -->" not in content:
    content = content.replace("</article>", sidebar_html)
    print("Added Sidebar and Bottom content.")
else:
    print("Sidebar already exists.")

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)
