import re

# Read current index.html
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Verify navbar and footer boundaries
main_start = content.find('<main>')
main_end = content.find('</main>')

if main_start == -1 or main_end == -1:
    print("Error: Could not locate <main> boundaries")
    exit(1)

print(f"<main> starts at index {main_start}, ends at {main_end}")
