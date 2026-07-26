import os
import re
import json

# Rename the file first
old_file = 'Wordpress-design-services-for-visa-consultancy.html'
new_file = 'wordpress-design-services-for-visa-consultancy.html'
if os.path.exists(old_file) and not os.path.exists(new_file):
    os.rename(old_file, new_file)

# SEO metadata definitions
seo_data = {
    'index.html': {
        'title': 'Best SEO Expert in Pakistan | SEO & WordPress by Ibrar',
        'desc': 'Ibrar Ahmad is a top SEO expert in Pakistan, delivering data-driven organic growth, technical SEO, and custom WordPress development for local businesses.',
        'schema': {
          "@context": "https://schema.org",
          "@type": "ProfessionalService",
          "name": "SEO With Ibrar",
          "url": "https://seowithibrar.com/",
          "image": "https://seowithibrar.com/images/logo-full.png",
          "founder": {
            "@type": "Person",
            "name": "Ibrar Ahmad",
            "jobTitle": "SEO Consultant & WordPress Engineer"
          },
          "areaServed": ["Lahore", "Karachi", "Islamabad", "Faisalabad", "Rawalpindi", "Pakistan"],
          "address": {
            "@type": "PostalAddress",
            "addressLocality": "Lahore",
            "addressRegion": "Punjab",
            "addressCountry": "PK"
          },
          "email": "ibrar@seowithibrar.com"
        }
    },
    'seo-services-pakistan.html': {
        'title': 'SEO Services in Pakistan | SEO With Ibrar',
        'desc': 'Get result-driven SEO services in Pakistan from Ibrar Ahmad. Improve rankings, organic traffic and qualified leads for businesses in Lahore, Karachi and Islamabad.'
    },
    'seo-services-visa-consultancy.html': {
        'title': 'SEO Services for Visa Consultancy | SEO With Ibrar',
        'desc': 'Get more study, work and immigration client inquiries with SEO built specifically for visa consultancies. Rank higher, build trust, and grow leads.',
        'schema': [
            {
              "@context": "https://schema.org",
              "@type": "Service",
              "serviceType": "SEO Services for Visa Consultancy",
              "provider": { "@type": "Person", "name": "Ibrar Ahmad" },
              "areaServed": "Pakistan",
              "url": "https://seowithibrar.com/seo-services-visa-consultancy"
            },
            {
              "@context": "https://schema.org",
              "@type": "FAQPage",
              "mainEntity": [
                {
                  "@type": "Question",
                  "name": "What is SEO for visa consultancy?",
                  "acceptedAnswer": {
                    "@type": "Answer",
                    "text": "SEO for visa consultancy helps your business appear on Google when people search for visa services, connecting you with clients seeking study, work, or immigration assistance."
                  }
                }
              ]
            }
        ]
    },
    'seo-services-education.html': {
        'title': 'SEO Services for Education Institutes | SEO With Ibrar',
        'desc': 'Boost admissions with SEO built for schools, colleges and academies. Ibrar Ahmad helps education institutes rank higher and attract more student inquiries.'
    },
    'wordpress-design-services.html': {
        'title': 'WordPress Design Services in Pakistan | SEO With Ibrar',
        'desc': 'Get fast, secure, SEO-friendly WordPress websites built by Ibrar Ahmad. Custom design, WooCommerce, speed optimization and ongoing support for Pakistan.'
    },
    'wordpress-design-services-for-visa-consultancy.html': {
        'title': 'WordPress Design for Visa Consultancies | SEO With Ibrar',
        'desc': 'Turn website visitors into visa clients with a fast, trustworthy WordPress site built for consultancies. Custom design and lead-focused pages.'
    },
    'wordpress-design-services-for-education.html': {
        'title': 'WordPress Design Services for Education | SEO With Ibrar',
        'desc': 'Build a professional, admissions-focused WordPress website for your school or academy. Fast, mobile-friendly and SEO-ready sites by Ibrar Ahmad.'
    },
    'seo-services-lahore.html': {
        'title': 'SEO Services in Lahore, Pakistan | SEO With Ibrar',
        'desc': 'Grow your Lahore business with local SEO from Ibrar Ahmad. Rank higher in DHA, Gulberg and Johar Town searches and turn visibility into real inquiries.'
    },
    'about.html': {
        'desc': 'Meet Ibrar Ahmad, a Lahore-based SEO consultant with 7+ years of experience helping brands across Pakistan scale organic traffic and revenue.'
    },
    'portfolio.html': {
        'desc': 'Explore real SEO case studies and Google Search Console data from Ibrar Ahmad\'s clients, showing organic traffic growth, rankings and revenue results.'
    },
    'top-seo-experts-in-pakistan.html': {
        'title': 'Top 15+ SEO Experts in Pakistan (2026) | SEO With Ibrar',
        'desc': 'Discover Pakistan\'s top 15+ SEO experts, including Ibrar Ahmad, and see what makes their strategies effective for ranking businesses higher.'
    },
    'ultimate-guide-to-wordpress-speed-optimization.html': {
        'title': 'WordPress Speed Optimization Guide | SEO With Ibrar',
        'desc': 'Learn how to speed up your WordPress site with practical, step-by-step tips that improve Core Web Vitals, user experience and search rankings.'
    },
    'geo-generative-engine-optimization-vs-traditional-seo.html': {
        'title': 'GEO vs Traditional SEO Explained | SEO With Ibrar',
        'desc': 'Understand how Generative Engine Optimization (GEO) differs from traditional SEO, and what it means for staying visible in AI-powered search results.'
    }
}

for file, data in seo_data.items():
    if not os.path.exists(file):
        print(f"File not found: {file}")
        continue
        
    with open(file, 'r', encoding='utf-8') as f:
        html = f.read()
        
    title = data.get('title')
    desc = data.get('desc')
    
    # 1. Replace Title
    if title:
        html = re.sub(r'<title>.*?</title>', f'<title>{title}</title>', html, flags=re.IGNORECASE | re.DOTALL)
        html = re.sub(r'<meta property="og:title" content=".*?">', f'<meta property="og:title" content="{title}">', html, flags=re.IGNORECASE)
        html = re.sub(r'<meta name="twitter:title" content=".*?">', f'<meta name="twitter:title" content="{title}">', html, flags=re.IGNORECASE)

    # 2. Replace Description
    if desc:
        # replace standard meta description
        html = re.sub(r'<meta name="description"[\s\S]*?content=".*?"\s*>', f'<meta name="description" content="{desc}">', html, flags=re.IGNORECASE)
        # fallback if format is slightly different
        if '<meta name="description"' not in html:
            html = re.sub(r'<meta name="description" content=".*?">', f'<meta name="description" content="{desc}">', html, flags=re.IGNORECASE)
            
        html = re.sub(r'<meta property="og:description" content=".*?">', f'<meta property="og:description" content="{desc}">', html, flags=re.IGNORECASE)
        html = re.sub(r'<meta name="twitter:description" content=".*?">', f'<meta name="twitter:description" content="{desc}">', html, flags=re.IGNORECASE)

    # 3. Handle JSON-LD Schema
    schema_data = data.get('schema')
    if schema_data:
        # Remove existing schema
        html = re.sub(r'<script type="application/ld\+json">.*?</script>', '', html, flags=re.IGNORECASE | re.DOTALL)
        
        # Add new schema
        if isinstance(schema_data, list):
            schema_scripts = "\n".join([f'<script type="application/ld+json">\n{json.dumps(s, indent=2)}\n</script>' for s in schema_data])
        else:
            schema_scripts = f'<script type="application/ld+json">\n{json.dumps(schema_data, indent=2)}\n</script>'
        
        # Inject just before </head>
        html = html.replace('</head>', schema_scripts + '\n</head>')

    # 4. Special rewrites for seo-services-education.html
    if file == 'seo-services-education.html':
        html = html.replace('VISA CONSULTANCY SEO', 'EDUCATION SEO')
        html = html.replace('a visa consultant', 'an education institution')
        html = html.replace('visa consultancy', 'education institution')
        html = html.replace('visa support', 'admissions')
        html = html.replace('a study visa, work visa, visit visa, or immigration process', 'school admissions, university enrollment, or short courses')
        html = html.replace('visa consultants', 'education institutes')
        html = html.replace('visa seekers', 'students and parents')
        html = html.replace('Visa professionals', 'School administrators and marketers')
        html = html.replace('Student Visa Consultants', 'Schools & Academies')
        html = html.replace('Immigration & PR Consultants', 'Colleges & Universities')
        html = html.replace('Travel & Visit Visa Agencies', 'Online Course Providers')
        html = html.replace('Work Visa Consultants', 'Vocational Institutes')
        html = html.replace('Legal & Corporate Visas', 'Tuition Centers')
        html = html.replace('Visa Service Keyword Targeting', 'Education Service Keyword Targeting')
        html = html.replace('visa-related', 'education-related')
        html = html.replace('visa categories', 'education categories')
        html = html.replace('Visa SEO is not generic SEO', 'Education SEO is not generic SEO')
        html = html.replace('visa clients', 'student enrollments')
        html = html.replace('visa services', 'education services')

    with open(file, 'w', encoding='utf-8') as f:
        f.write(html)

print("SEO updates applied.")
