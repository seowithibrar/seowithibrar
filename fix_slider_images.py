import re

with open('portfolio.html', 'r', encoding='utf-8') as f:
    html = f.read()

for i in range(1, 5):
    placeholder = f'https://placehold.co/1000x350/222/84cc16?text=Save+Image+As:+images/gsc-result-{i}.png'
    html = html.replace(f'images/gsc-result-{i}.png', placeholder)

with open('portfolio.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated portfolio.html with placeholders")
