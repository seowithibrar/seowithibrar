import glob
import re

html_files = glob.glob('*.html')

for file in html_files:
    try:
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # 1. Update email address globally
        new_content = content.replace('seowithibrar@gmail.com', 'ibrar@seowithibrar.com')
        
        # 2. Specific form updates for contact.html
        if file == 'contact.html':
            # Update form action
            new_content = new_content.replace(
                '<form action="#" method="POST">',
                '<form action="https://formsubmit.co/ibrar@seowithibrar.com" method="POST">'
            )
            # Add name attributes to inputs
            new_content = re.sub(r'<input type="text" id="fullname"', r'<input type="text" name="fullname" id="fullname"', new_content)
            new_content = re.sub(r'<input type="email" id="email"', r'<input type="email" name="email" id="email"', new_content)
            new_content = re.sub(r'<input type="url" id="website"', r'<input type="url" name="website" id="website"', new_content)
            # Textarea
            new_content = re.sub(r'<textarea id="message"', r'<textarea name="message" id="message"', new_content)
            
            # Formsubmit hidden config (optional but good: disable captcha or set subject)
            hidden_fields = '<input type="hidden" name="_subject" value="New Contact Form Submission">\n'
            new_content = new_content.replace('method="POST">', f'method="POST">\n{hidden_fields}')

        if new_content != content:
            with open(file, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f'Updated {file}')
    except Exception as e:
        print(f"Error processing {file}: {e}")
