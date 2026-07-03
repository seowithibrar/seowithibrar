import re

images = [
    "AG bookkeeping services llc.webp",
    "Blexry.webp",
    "Cheese Club.webp",
    "Edvanture Consultancy.webp",
    "Euro immigration Consultancy.webp",
    "Euro Immigration Consutlancy Pakistan.webp",
    "Haya Collective.webp",
    "KIMS.webp",
    "knowledge kastle.webp",
    "Navid saqib.webp",
    "Spark Vis Consutlancy.webp",
    "Vip Group.webp",
    "Zaka Foods.webp"
]

# 1. Update CSS
css_additions = """
/* ==========================================================================
   WordPress Development Portfolio Slider (Device Mockups)
   ========================================================================== */
.wp-portfolio-section {
    padding: 5rem 0;
    margin-bottom: 2rem;
    border-top: 1px solid rgba(255,255,255,0.05);
}

.wp-slider-container {
    position: relative;
    max-width: 1200px;
    margin: 0 auto;
    overflow: hidden;
}

.wp-slider-track {
    display: flex;
    transition: transform 0.6s cubic-bezier(0.25, 1, 0.5, 1);
}

.wp-slide {
    min-width: 100%;
    box-sizing: border-box;
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 2rem;
    padding: 2rem;
}

/* Desktop Device Mockup */
.device-desktop {
    width: 65%;
    background: #2a2a2a;
    border-radius: 12px;
    box-shadow: 0 20px 50px rgba(0,0,0,0.6);
    overflow: hidden;
    border: 1px solid rgba(255,255,255,0.1);
    position: relative;
}

.device-desktop-header {
    height: 30px;
    background: #1a1a1a;
    display: flex;
    align-items: center;
    padding: 0 15px;
    gap: 6px;
    border-bottom: 1px solid rgba(255,255,255,0.05);
}

.device-dot {
    width: 10px;
    height: 10px;
    border-radius: 50%;
}
.device-dot.red { background: #ff5f56; }
.device-dot.yellow { background: #ffbd2e; }
.device-dot.green { background: #27c93f; }

.device-desktop-screen {
    width: 100%;
    aspect-ratio: 16 / 9;
    overflow: hidden;
    position: relative;
}

/* Mobile Device Mockup */
.device-mobile {
    width: 22%;
    background: #1a1a1a;
    border-radius: 30px;
    box-shadow: 0 20px 50px rgba(0,0,0,0.6);
    overflow: hidden;
    border: 6px solid #333;
    position: relative;
    aspect-ratio: 9 / 19.5;
}

.device-mobile-notch {
    position: absolute;
    top: 0;
    left: 50%;
    transform: translateX(-50%);
    width: 40%;
    height: 20px;
    background: #333;
    border-bottom-left-radius: 10px;
    border-bottom-right-radius: 10px;
    z-index: 10;
}

.device-mobile-screen {
    width: 100%;
    height: 100%;
    overflow: hidden;
    position: relative;
}

/* Image styles within screens */
.device-desktop-screen img,
.device-mobile-screen img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    object-position: top;
    display: block;
    transition: transform 0.3s ease;
}

.device-desktop-screen:hover img,
.device-mobile-screen:hover img {
    transform: translateY(-2%);
}

.wp-slide-caption {
    position: absolute;
    bottom: -40px;
    left: 50%;
    transform: translateX(-50%);
    color: rgba(255,255,255,0.7);
    font-size: 1.1rem;
    font-weight: 600;
    letter-spacing: 1px;
    text-transform: uppercase;
}

/* Buttons for WP slider */
.wp-slider-btn {
    position: absolute;
    top: 50%;
    transform: translateY(-50%);
    background: rgba(255,255,255,0.1);
    backdrop-filter: blur(4px);
    border: 1px solid rgba(255,255,255,0.1);
    color: white;
    width: 50px;
    height: 50px;
    border-radius: 50%;
    cursor: pointer;
    display: flex;
    align-items: center;
    justify-content: center;
    transition: all 0.3s;
    z-index: 20;
}

.wp-slider-btn:hover {
    background: var(--color-primary);
    transform: translateY(-50%) scale(1.1);
}

.wp-slider-btn.prev {
    left: 10px;
}

.wp-slider-btn.next {
    right: 10px;
}

/* Mobile Responsiveness */
@media (max-width: 900px) {
    .wp-slide {
        flex-direction: column;
        padding: 1rem;
        gap: 1.5rem;
    }
    .device-desktop {
        width: 100%;
    }
    .device-mobile {
        width: 40%;
        display: none; /* Hide mobile on small screens to save space */
    }
}
"""
with open('css/styles.css', 'a', encoding='utf-8') as f:
    f.write(css_additions)
print("Added WP Slider CSS to styles.css")

# 2. Build HTML for slides
slides_html = ""
for img in images:
    site_name = img.replace(".webp", "")
    slides_html += f"""
                        <div class="wp-slide">
                            <div class="device-desktop">
                                <div class="device-desktop-header">
                                    <div class="device-dot red"></div>
                                    <div class="device-dot yellow"></div>
                                    <div class="device-dot green"></div>
                                </div>
                                <div class="device-desktop-screen">
                                    <img src="images/{img}" alt="{site_name} Desktop View" loading="lazy">
                                </div>
                            </div>
                            <div class="device-mobile">
                                <div class="device-mobile-notch"></div>
                                <div class="device-mobile-screen">
                                    <img src="images/{img}" alt="{site_name} Mobile View" loading="lazy">
                                </div>
                            </div>
                            <div class="wp-slide-caption">{site_name}</div>
                        </div>
"""

wp_section_html = f"""
            <section class="wp-portfolio-section">
                <header class="dark-archive-header" style="text-align: center; margin-bottom: 3rem;">
                    <h2 style="font-size: 2.2rem; font-weight: 700; margin-bottom: 1rem;">Premium WordPress Development</h2>
                    <p style="color: rgba(255,255,255,0.7); max-width: 800px; margin: 0 auto;">
                        High-performance, enterprise-grade WordPress websites built for speed, conversion, and perfect responsiveness across all devices.
                    </p>
                </header>
                
                <div class="wp-slider-container">
                    <div class="wp-slider-track" id="wpSliderTrack">
                        {slides_html}
                    </div>
                    
                    <button class="wp-slider-btn prev" id="wpSliderPrev" aria-label="Previous WP Slide">
                        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="15 18 9 12 15 6"></polyline></svg>
                    </button>
                    <button class="wp-slider-btn next" id="wpSliderNext" aria-label="Next WP Slide">
                        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="9 18 15 12 9 6"></polyline></svg>
                    </button>
                </div>
            </section>
"""

with open('portfolio.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Insert the WP section right before the CTA div
cta_start = '<div style="text-align: center; margin-top: 5rem;">'
html = html.replace(cta_start, wp_section_html + '\n            ' + cta_start)

# Add Slider JavaScript for the new WP slider
wp_slider_js = """
        // WP Slider Logic
        const wpTrack = document.getElementById('wpSliderTrack');
        const wpPrevBtn = document.getElementById('wpSliderPrev');
        const wpNextBtn = document.getElementById('wpSliderNext');
        let wpCurrentIndex = 0;
        const wpTotalSlides = 13;

        function updateWpSlider() {
            wpTrack.style.transform = `translateX(-${wpCurrentIndex * 100}%)`;
        }

        if(wpNextBtn && wpPrevBtn && wpTrack) {
            wpNextBtn.addEventListener('click', () => {
                wpCurrentIndex = (wpCurrentIndex + 1) % wpTotalSlides;
                updateWpSlider();
            });

            wpPrevBtn.addEventListener('click', () => {
                wpCurrentIndex = (wpCurrentIndex - 1 + wpTotalSlides) % wpTotalSlides;
                updateWpSlider();
            });
        }
"""

# Insert the JS into the existing DOMContentLoaded block
html = html.replace("const totalSlides = 4;", "const totalSlides = 4;\n" + wp_slider_js)

with open('portfolio.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Injected WP Slider into portfolio.html")
