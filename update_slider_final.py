import re

# 1. Update HTML
html_replacements = """
                    <div class="slider-track" id="sliderTrack">
                        <div class="slide">
                            <img src="images/School Website.png" alt="School Website SEO Graph" loading="lazy">
                            <div class="slide-caption">School Website Growth</div>
                        </div>
                        <div class="slide">
                            <img src="images/Visa Consutlacny in Karachi.png" alt="Visa Consultancy SEO Graph" loading="lazy">
                            <div class="slide-caption">Visa Consultancy in Karachi</div>
                        </div>
                        <div class="slide">
                            <img src="images/Education platfrom in lahore.png" alt="Education Platform SEO Graph" loading="lazy">
                            <div class="slide-caption">Education Platform in Lahore</div>
                        </div>
                        <div class="slide">
                            <img src="images/Local ecommeces.png" alt="Local Ecommerce SEO Graph" loading="lazy">
                            <div class="slide-caption">Local E-commerce Scale</div>
                        </div>
                    </div>
"""

with open('portfolio.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace the slider track content
html = re.sub(r'<div class="slider-track" id="sliderTrack">.*?</div>\s*<button class="slider-btn prev"', html_replacements + '                    <button class="slider-btn prev"', html, flags=re.DOTALL)

with open('portfolio.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated slider images and added captions in portfolio.html")

# 2. Add CSS for slide captions
css_caption = """
/* Slider Captions */
.slide {
    position: relative;
}

.slide-caption {
    position: absolute;
    bottom: 20px;
    left: 20px;
    background: rgba(0, 0, 0, 0.7);
    color: white;
    padding: 0.5rem 1.5rem;
    border-radius: 50px;
    font-weight: 700;
    font-size: 1.1rem;
    backdrop-filter: blur(8px);
    border: 1px solid rgba(255, 255, 255, 0.2);
    box-shadow: 0 4px 15px rgba(0,0,0,0.3);
}
"""

with open('css/styles.css', 'a', encoding='utf-8') as f:
    f.write(css_caption)
print("Added caption styles to styles.css")
