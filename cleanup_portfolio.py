import re

with open('portfolio.html', 'r', encoding='utf-8') as f:
    html = f.read()

# We want to extract just the slider track and buttons so we don't lose the image paths
slider_track_match = re.search(r'(<div class="slider-track" id="sliderTrack">.*?</div>)', html, flags=re.DOTALL)
slider_track = slider_track_match.group(1) if slider_track_match else ''

# Construct the new main content
new_main = f"""
    <main class="dark-archive-main" style="min-height: 80vh; display: flex; flex-direction: column; justify-content: center;">
        <div class="container">
            <header class="dark-archive-header" style="margin-bottom: 3rem;">
                <h1 class="dark-archive-title">Our Client Success Stories</h1>
                <p class="dark-archive-subtitle" style="margin-bottom: 3rem;">
                    Discover how we have helped education brands, visa consultancies, and e-commerce stores scale their organic traffic and skyrocket revenue through data-driven SEO strategies.
                </p>
                <h2 style="font-size: 2rem; font-weight: 700; margin-bottom: 1rem;">Proven SEO Results</h2>
                <p style="color: rgba(255,255,255,0.7); max-width: 800px; margin: 0 auto;">
                    Real data from Google Search Console showcasing massive organic traffic growth, improved CTR, and top keyword rankings.
                </p>
            </header>

            <section class="seo-results-section" style="padding-top: 0;">
                <div class="slider-container">
                    {slider_track}
                    <button class="slider-btn prev" id="sliderPrev" aria-label="Previous Slide">
                        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="15 18 9 12 15 6"></polyline></svg>
                    </button>
                    <button class="slider-btn next" id="sliderNext" aria-label="Next Slide">
                        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="9 18 15 12 9 6"></polyline></svg>
                    </button>
                </div>
                
                <div class="slider-dots" id="sliderDots">
                    <div class="dot active" data-index="0"></div>
                    <div class="dot" data-index="1"></div>
                    <div class="dot" data-index="2"></div>
                    <div class="dot" data-index="3"></div>
                </div>
            </section>
        </div>
    </main>
"""

# Find where </header> ends and <footer> begins
new_html = re.sub(r'</header>.*?(<footer class="footer">)', r'</header>\n' + new_main + r'\n\1', html, flags=re.DOTALL)

# Let's also make sure the javascript for the filter is removed, we only need slider JS
new_html = re.sub(r'function filterPortfolio\(\).*?\}\);', '', new_html, flags=re.DOTALL)

with open('portfolio.html', 'w', encoding='utf-8') as f:
    f.write(new_html)

print("Updated portfolio.html to only show the slider and combined text.")
