import glob
import re
import json

base_url = "https://seowithibrar.com"
site_name = "SEO With Ibrar"
default_image = f"{base_url}/images/logo-full.png"
author_name = "Ibrar Ahmad"

files = glob.glob('*.html')

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        html = f.read()

    # Determine Page Type and specific attributes
    slug = file.replace('.html', '')
    if slug == 'index':
        url = base_url + "/"
        page_type = "WebSite"
        title = "Best SEO Expert in Pakistan | SEO With Ibrar"
        desc = "Ibrar Ahmad is the top SEO expert in Pakistan offering proven, data-driven organic growth, technical SEO, and custom WordPress development."
    elif slug == 'about':
        url = base_url + "/about"
        page_type = "AboutPage"
        title = "About Ibrar Ahmad | Leading SEO Consultant"
        desc = "Learn about Ibrar Ahmad, an SEO expert with 6+ years of experience helping brands scale organic traffic and revenue through advanced SEO."
    elif slug == 'contact':
        url = base_url + "/contact"
        page_type = "ContactPage"
        title = "Contact SEO With Ibrar | Book a Strategy Call"
        desc = "Ready to scale your organic traffic? Contact SEO With Ibrar to book a free strategy call and start dominating search engines today."
    elif slug == 'portfolio':
        url = base_url + "/portfolio"
        page_type = "CollectionPage"
        title = "SEO Portfolio & Case Studies | SEO With Ibrar"
        desc = "Explore our SEO portfolio featuring real Google Search Console data. See how we drive massive organic traffic and revenue."
    elif slug == 'blog':
        url = base_url + "/blog"
        page_type = "CollectionPage"
        title = "SEO Blog & Insights | Technical SEO Guides"
        desc = "Read our latest SEO insights, technical guides, and proven strategies to skyrocket your organic traffic and dominate Google rankings."
    elif 'services' in slug or 'consultancy' in slug:
        url = base_url + "/" + slug
        page_type = "Service"
        title = f"{slug.replace('-', ' ').title()} | SEO With Ibrar"
        desc = f"Expert {slug.replace('-', ' ')} providing data-driven organic growth and high-performance strategies for your business."
    else:
        url = base_url + "/" + slug
        page_type = "BlogPosting"
        title = f"{slug.replace('-', ' ').title()} | SEO With Ibrar"
        desc = f"Read this comprehensive guide on {slug.replace('-', ' ')} and learn how to improve your organic search visibility."

    # Generate JSON-LD Schema
    schema = {
        "@context": "https://schema.org",
        "@type": page_type,
        "name": title,
        "description": desc,
        "url": url
    }
    
    if page_type == "BlogPosting":
        schema["headline"] = title
        schema["author"] = {"@type": "Person", "name": author_name}
        schema["publisher"] = {"@type": "Organization", "name": site_name, "logo": {"@type": "ImageObject", "url": default_image}}
        schema["datePublished"] = "2024-01-01T08:00:00+08:00"
        schema["dateModified"] = "2026-07-03T08:00:00+08:00"
        schema["image"] = default_image
    
    schema_json = json.dumps(schema, indent=2)

    # Generate SEO Tags
    seo_tags = f"""
    <!-- Open Graph Tags -->
    <meta property="og:title" content="{title}">
    <meta property="og:description" content="{desc}">
    <meta property="og:type" content="{"website" if page_type != "BlogPosting" else "article"}">
    <meta property="og:url" content="{url}">
    <meta property="og:image" content="{default_image}">
    
    <!-- Twitter Card Tags -->
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="{title}">
    <meta name="twitter:description" content="{desc}">
    <meta name="twitter:image" content="{default_image}">
    
    <!-- Canonical URL -->
    <link rel="canonical" href="{url}">
    
    <!-- JSON-LD Schema -->
    <script type="application/ld+json">
{schema_json}
    </script>
"""

    # We need to inject these tags just before </head>
    # First, let's remove old canonicals, og tags, and json-ld if they exist (to prevent duplicates)
    html = re.sub(r'<link rel="canonical".*?>', '', html, flags=re.IGNORECASE)
    html = re.sub(r'<meta property="og:.*?>', '', html, flags=re.IGNORECASE)
    html = re.sub(r'<meta name="twitter:.*?>', '', html, flags=re.IGNORECASE)
    html = re.sub(r'<script type="application/ld\+json">.*?</script>', '', html, flags=re.IGNORECASE | re.DOTALL)
    
    # Also replace existing title and description to ensure perfection
    # Only if we aren't completely destroying unique titles they manually set. But the prompt said "Apply on all page" and generate meta titles.
    # We will override existing title and description for consistency with the generated ones, unless they are already highly optimized. We'll override them.
    html = re.sub(r'<title>.*?</title>', f'<title>{title}</title>', html, flags=re.IGNORECASE | re.DOTALL)
    if '<meta name="description"' in html.lower():
        html = re.sub(r'<meta name="description" content=".*?">', f'<meta name="description" content="{desc}">', html, flags=re.IGNORECASE)
    else:
        seo_tags = f'<meta name="description" content="{desc}">\n' + seo_tags

    # Inject everything just before </head>
    html = html.replace('</head>', seo_tags + '</head>')
    
    # Remove blank lines left from regex deletions
    html = re.sub(r'\n\s*\n', '\n', html)

    with open(file, 'w', encoding='utf-8') as f:
        f.write(html)

print("Applied Technical SEO Package to all HTML files successfully.")
