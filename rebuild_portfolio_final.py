import re

with open('portfolio.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Extract exactly the top navigation
header_match = re.search(r'(.*?</header>)', html, flags=re.DOTALL)
top_nav = header_match.group(1) if header_match else ''

# Extract exactly the footer
footer_match = re.search(r'(<footer class="footer new-mega-footer">.*)', html, flags=re.DOTALL)
footer = footer_match.group(1) if footer_match else ''

# Extract just one instance of the slider track so we keep the correct image paths and captions
slider_track_match = re.search(r'(<div class="slider-track" id="sliderTrack">.*?</div>\s*<button class="slider-btn prev")', html, flags=re.DOTALL)
if slider_track_match:
    track_only = re.search(r'(<div class="slider-track" id="sliderTrack">.*?</div>)', slider_track_match.group(1), flags=re.DOTALL).group(1)
else:
    print("Could not find slider track")
    exit()

# Build the perfectly clean main section
new_main = f"""
    <main class="dark-archive-main" style="min-height: 80vh; padding: 4rem 0;">
        <div class="container">
            <header class="dark-archive-header" style="text-align: center; margin-bottom: 3rem;">
                <h1 class="dark-archive-title" style="font-size: 3rem; margin-bottom: 1.5rem;">Our Client Success Stories</h1>
                <p class="dark-archive-subtitle" style="margin: 0 auto 4rem auto; max-width: 800px; line-height: 1.6;">
                    Discover how we have helped education brands, visa consultancies, and e-commerce stores scale their organic traffic and skyrocket revenue through data-driven SEO strategies.
                </p>
                
                <h2 style="font-size: 2.2rem; font-weight: 700; margin-bottom: 1rem;">Proven SEO Results</h2>
                <p style="color: rgba(255,255,255,0.7); max-width: 800px; margin: 0 auto;">
                    Real data from Google Search Console showcasing massive organic traffic growth, improved CTR, and top keyword rankings.
                </p>
            </header>

            <section class="seo-results-section" style="padding-top: 1rem;">
                <div class="slider-container">
                    {track_only}
                    <button class="slider-btn prev" id="sliderPrev" aria-label="Previous Slide">
                        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="15 18 9 12 15 6"></polyline></svg>
                    </button>
                    <button class="slider-btn next" id="sliderNext" aria-label="Next Slide">
                        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="9 18 15 12 9 6"></polyline></svg>
                    </button>
                </div>
                
                <div class="slider-dots" id="sliderDots" style="margin-bottom: 2rem;">
                    <div class="dot active" data-index="0"></div>
                    <div class="dot" data-index="1"></div>
                    <div class="dot" data-index="2"></div>
                    <div class="dot" data-index="3"></div>
                </div>
            </section>
            
            <div style="text-align: center; margin-top: 5rem;">
                <h2 style="font-size: 2.5rem; margin-bottom: 1.5rem; font-weight: 800;">Ready to be our next success story?</h2>
                <p style="color: rgba(255,255,255,0.7); max-width: 600px; margin: 0 auto 2rem auto;">Let's discuss how data-driven SEO can transform your business growth.</p>
                <a href="contact.html" class="btn btn-primary" style="padding: 1rem 2.5rem; font-size: 1.1rem; border-radius: 50px;">Book a Strategy Call</a>
            </div>
            
        </div>
    </main>
"""

# Slider JS
slider_js = """
    <script>
        document.addEventListener('DOMContentLoaded', () => {
            const track = document.getElementById('sliderTrack');
            const prevBtn = document.getElementById('sliderPrev');
            const nextBtn = document.getElementById('sliderNext');
            const dots = document.querySelectorAll('.dot');
            let currentIndex = 0;
            const totalSlides = 4;

            function updateSlider() {
                track.style.transform = `translateX(-${currentIndex * 100}%)`;
                dots.forEach((dot, index) => {
                    dot.classList.toggle('active', index === currentIndex);
                });
            }

            if(nextBtn && prevBtn && track) {
                nextBtn.addEventListener('click', () => {
                    currentIndex = (currentIndex + 1) % totalSlides;
                    updateSlider();
                });

                prevBtn.addEventListener('click', () => {
                    currentIndex = (currentIndex - 1 + totalSlides) % totalSlides;
                    updateSlider();
                });

                dots.forEach(dot => {
                    dot.addEventListener('click', (e) => {
                        currentIndex = parseInt(e.target.getAttribute('data-index'));
                        updateSlider();
                    });
                });
            }
        });
    </script>
"""

# Combine everything
final_html = top_nav + "\n" + new_main + "\n" + footer

# Remove any old slider scripts
final_html = re.sub(r'<script>\s*document\.addEventListener.*?updateSlider.*?\}\);\s*</script>', '', final_html, flags=re.DOTALL)
# Inject slider JS before closing body tag
final_html = final_html.replace('</body>', slider_js + '\n</body>')

with open('portfolio.html', 'w', encoding='utf-8') as f:
    f.write(final_html)

print("Perfectly rebuilt portfolio.html!")
