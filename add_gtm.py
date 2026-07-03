import glob
import re

html_files = glob.glob('*.html')

head_code = """<!-- Google Tag Manager -->
<script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
})(window,document,'script','dataLayer','GTM-KGLHCFG9');</script>
<!-- End Google Tag Manager -->"""

body_code = """<!-- Google Tag Manager (noscript) -->
<noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-KGLHCFG9"
height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
<!-- End Google Tag Manager (noscript) -->"""

for file in html_files:
    try:
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
            
        if 'GTM-KGLHCFG9' in content:
            print(f"GTM already exists in {file}, skipping.")
            continue
            
        # Insert after <head> or <head ...>
        # We use re.sub with count=1 to only replace the first occurrence
        content = re.sub(r'(<head[^>]*>)', r'\1\n' + head_code, content, count=1, flags=re.IGNORECASE)
        
        # Insert after <body> or <body ...>
        content = re.sub(r'(<body[^>]*>)', r'\1\n' + body_code, content, count=1, flags=re.IGNORECASE)
        
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
            
        print(f"Added GTM to {file}")
    except Exception as e:
        print(f"Error processing {file}: {e}")
