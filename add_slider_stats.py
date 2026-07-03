import re

# 1. Update portfolio.html with stats inside the slides
with open('portfolio.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace the slider track content entirely with the new structure including stats
new_slider_track = """<div class="slider-track" id="sliderTrack">
                        <div class="slide">
                            <img src="images/Local ecommeces.png" alt="Local Ecommerce SEO Graph" loading="lazy">
                            <div class="slide-caption">Local E-commerce Scale</div>
                            <div class="slide-stats">
                                <div class="stat-item">
                                    <span class="stat-value">+240%</span>
                                    <span class="stat-label">Organic Revenue</span>
                                </div>
                                <div class="stat-item">
                                    <span class="stat-value">50+</span>
                                    <span class="stat-label">Page 1 Keywords</span>
                                </div>
                            </div>
                        </div>
                        <div class="slide">
                            <img src="images/School Website.png" alt="School Website SEO Graph" loading="lazy">
                            <div class="slide-caption">School Website Growth</div>
                            <div class="slide-stats">
                                <div class="stat-item">
                                    <span class="stat-value">+180%</span>
                                    <span class="stat-label">Student Inquiries</span>
                                </div>
                                <div class="stat-item">
                                    <span class="stat-value">85%</span>
                                    <span class="stat-label">Lower Cost/Lead</span>
                                </div>
                            </div>
                        </div>
                        <div class="slide">
                            <img src="images/Visa Consutlacny in Karachi.png" alt="Visa Consultancy SEO Graph" loading="lazy">
                            <div class="slide-caption">Visa Consultancy in Karachi</div>
                            <div class="slide-stats">
                                <div class="stat-item">
                                    <span class="stat-value">+315%</span>
                                    <span class="stat-label">Organic Traffic</span>
                                </div>
                                <div class="stat-item">
                                    <span class="stat-value">#1</span>
                                    <span class="stat-label">Local Map Pack</span>
                                </div>
                            </div>
                        </div>
                        <div class="slide">
                            <img src="images/Education platfrom in lahore.png" alt="Education Platform SEO Graph" loading="lazy">
                            <div class="slide-caption">Education Platform in Lahore</div>
                            <div class="slide-stats">
                                <div class="stat-item">
                                    <span class="stat-value">+210%</span>
                                    <span class="stat-label">Traffic Growth</span>
                                </div>
                                <div class="stat-item">
                                    <span class="stat-value">100+</span>
                                    <span class="stat-label">Top 3 Rankings</span>
                                </div>
                            </div>
                        </div>
                    </div>"""

# Ensure we replace exactly the slider track area. I'll use regex to find everything from <div class="slider-track" id="sliderTrack"> up to but NOT including the <button class="slider-btn prev"
html = re.sub(r'<div class="slider-track" id="sliderTrack">.*?(?=<button class="slider-btn prev")', new_slider_track + '\n                    ', html, flags=re.DOTALL)

with open('portfolio.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated portfolio.html with stats overlays")

# 2. Add CSS to style the new stat boxes
css = """
/* Slide Stats Overlay */
.slide-stats {
    position: absolute;
    top: 20px;
    right: 20px;
    display: flex;
    gap: 1rem;
    background: rgba(17, 17, 17, 0.85);
    backdrop-filter: blur(12px);
    border: 1px solid rgba(255, 255, 255, 0.1);
    padding: 1rem 1.5rem;
    border-radius: 12px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.5);
    z-index: 5;
}

.stat-item {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
}

.stat-item:not(:last-child) {
    padding-right: 1rem;
    border-right: 1px solid rgba(255,255,255,0.1);
}

.stat-value {
    color: var(--color-primary);
    font-size: 1.5rem;
    font-weight: 800;
    line-height: 1;
    margin-bottom: 0.25rem;
}

.stat-label {
    color: rgba(255,255,255,0.7);
    font-size: 0.75rem;
    text-transform: uppercase;
    letter-spacing: 1px;
    font-weight: 600;
}

@media (max-width: 768px) {
    .slide-stats {
        top: 10px;
        right: 10px;
        padding: 0.75rem 1rem;
        gap: 0.75rem;
    }
    
    .stat-value {
        font-size: 1.2rem;
    }
    
    .stat-label {
        font-size: 0.65rem;
    }
    
    .slide-caption {
        bottom: 10px;
        left: 10px;
        font-size: 0.9rem;
        padding: 0.4rem 1rem;
    }
}
"""

with open('css/styles.css', 'a', encoding='utf-8') as f:
    f.write(css)

print("Added CSS for stats overlays.")
