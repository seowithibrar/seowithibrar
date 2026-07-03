import re

# 1. Update CSS
css_additions = """
/* ==========================================================================
   SEO Results Slider (Portfolio)
   ========================================================================== */
.seo-results-section {
    padding: 3rem 0;
    margin-bottom: 2rem;
}

.seo-results-header {
    text-align: center;
    margin-bottom: 2rem;
}

.seo-results-header h2 {
    font-size: 2rem;
    font-weight: 700;
    margin-bottom: 1rem;
}

.seo-results-header p {
    color: rgba(255,255,255,0.7);
    max-width: 600px;
    margin: 0 auto;
}

.slider-container {
    position: relative;
    max-width: 1000px;
    margin: 0 auto;
    overflow: hidden;
    border-radius: 12px;
    background: #111;
    box-shadow: 0 20px 40px rgba(0,0,0,0.4);
    border: 1px solid rgba(255,255,255,0.1);
}

.slider-track {
    display: flex;
    transition: transform 0.5s ease-in-out;
}

.slide {
    min-width: 100%;
    box-sizing: border-box;
}

.slide img {
    width: 100%;
    display: block;
    border-radius: 12px;
}

.slider-btn {
    position: absolute;
    top: 50%;
    transform: translateY(-50%);
    background: rgba(255,255,255,0.1);
    backdrop-filter: blur(4px);
    border: none;
    color: white;
    width: 40px;
    height: 40px;
    border-radius: 50%;
    cursor: pointer;
    display: flex;
    align-items: center;
    justify-content: center;
    transition: background 0.3s;
    z-index: 10;
}

.slider-btn:hover {
    background: var(--color-primary);
}

.slider-btn.prev {
    left: 1rem;
}

.slider-btn.next {
    right: 1rem;
}

.slider-dots {
    display: flex;
    justify-content: center;
    gap: 0.5rem;
    margin-top: 1.5rem;
}

.dot {
    width: 10px;
    height: 10px;
    border-radius: 50%;
    background: rgba(255,255,255,0.3);
    cursor: pointer;
    transition: background 0.3s, transform 0.3s;
}

.dot.active {
    background: var(--color-primary);
    transform: scale(1.3);
}
"""
with open('css/styles.css', 'a', encoding='utf-8') as f:
    f.write(css_additions)
print("Added Slider CSS to styles.css")

# 2. Update HTML
slider_html = """
            <section class="seo-results-section">
                <div class="seo-results-header">
                    <h2>Proven SEO Results</h2>
                    <p>Real data from Google Search Console showcasing massive organic traffic growth, improved CTR, and top keyword rankings.</p>
                </div>
                
                <div class="slider-container">
                    <div class="slider-track" id="sliderTrack">
                        <div class="slide"><img src="images/gsc-result-1.png" alt="SEO Result 1" loading="lazy"></div>
                        <div class="slide"><img src="images/gsc-result-2.png" alt="SEO Result 2" loading="lazy"></div>
                        <div class="slide"><img src="images/gsc-result-3.png" alt="SEO Result 3" loading="lazy"></div>
                        <div class="slide"><img src="images/gsc-result-4.png" alt="SEO Result 4" loading="lazy"></div>
                    </div>
                    
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
"""

with open('portfolio.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Insert slider right after the header in the container
html = html.replace('</header>', '</header>\n' + slider_html)

# Add Slider JavaScript
slider_js = """
            // Slider Logic
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
"""

# Insert the JS into the existing <script> block
html = html.replace('filterPortfolio();\n                });\n            });', 'filterPortfolio();\n                });\n            });\n\n' + slider_js)

with open('portfolio.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Injected Slider into portfolio.html")
