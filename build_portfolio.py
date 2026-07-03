import re

# We will read blog.html as a template for the header, footer, and CSS linking.
with open('blog.html', 'r', encoding='utf-8') as f:
    template_html = f.read()

# Replace the <title>
template_html = re.sub(r'<title>.*?</title>', '<title>Client Portfolio & Case Studies | SEO With Ibrar</title>', template_html)

# Create the portfolio main content
portfolio_main = """
    <main class="dark-archive-main">
        <div class="container">
            <header class="dark-archive-header">
                <h1 class="dark-archive-title">Our Client Success Stories</h1>
                <p class="dark-archive-subtitle">
                    Discover how we have helped education brands, visa consultancies, and e-commerce stores scale their organic traffic and skyrocket revenue through data-driven SEO strategies.
                </p>
            </header>

            <div class="dark-archive-controls">
                <div class="dark-filter-group" id="portfolio-filters">
                    <button class="dark-filter-btn active" data-filter="all">All Industries</button>
                    <button class="dark-filter-btn" data-filter="Visa Consultancy">Visa Consultancy</button>
                    <button class="dark-filter-btn" data-filter="Education">Education</button>
                    <button class="dark-filter-btn" data-filter="E-commerce">E-commerce</button>
                </div>
            </div>

            <div class="dark-blog-grid" id="portfolio-grid">
                
                <!-- Case Study 1 -->
                <div class="dark-blog-card portfolio-card" data-category="Visa Consultancy">
                    <div class="dark-blog-image">
                        <img src="images/seo-services-for-visa-consultancy.webp" alt="Visa Consultancy Growth" loading="lazy">
                    </div>
                    <div class="dark-blog-content portfolio-content">
                        <div class="dark-blog-meta">
                            <span class="dark-blog-category">Visa Consultancy</span>
                        </div>
                        <h3 class="dark-blog-title"><a href="seo-services-visa-consultancy.html">Leading Visa Agency Dominates Local Search</a></h3>
                        
                        <div class="portfolio-metrics">
                            <div class="metric">
                                <span class="metric-value">+315%</span>
                                <span class="metric-label">Organic Traffic</span>
                            </div>
                            <div class="metric">
                                <span class="metric-value">#1</span>
                                <span class="metric-label">Local Map Pack</span>
                            </div>
                        </div>

                        <p class="dark-blog-excerpt">We completely overhauled the technical SEO architecture and local footprint for a top visa consulting agency, resulting in triple-digit growth in qualified leads.</p>
                        
                    </div>
                </div>

                <!-- Case Study 2 -->
                <div class="dark-blog-card portfolio-card" data-category="E-commerce">
                    <div class="dark-blog-image">
                        <img src="images/top-seo-experts-pakistan.webp" alt="Ecommerce Growth" loading="lazy">
                    </div>
                    <div class="dark-blog-content portfolio-content">
                        <div class="dark-blog-meta">
                            <span class="dark-blog-category">E-commerce</span>
                        </div>
                        <h3 class="dark-blog-title"><a href="#">Fashion Retailer Skyrockets Organic Revenue</a></h3>
                        
                        <div class="portfolio-metrics">
                            <div class="metric">
                                <span class="metric-value">+240%</span>
                                <span class="metric-label">Organic Revenue</span>
                            </div>
                            <div class="metric">
                                <span class="metric-value">50+</span>
                                <span class="metric-label">Target Keywords on Page 1</span>
                            </div>
                        </div>

                        <p class="dark-blog-excerpt">Through comprehensive category optimization and resolving critical technical crawl issues, we helped this online store capture significant market share.</p>
                        
                    </div>
                </div>

                <!-- Case Study 3 -->
                <div class="dark-blog-card portfolio-card" data-category="Education">
                    <div class="dark-blog-image">
                        <img src="images/geo-generative-engine-optimization-vs-traditional-seo.webp" alt="Education SEO" loading="lazy">
                    </div>
                    <div class="dark-blog-content portfolio-content">
                        <div class="dark-blog-meta">
                            <span class="dark-blog-category">Education</span>
                        </div>
                        <h3 class="dark-blog-title"><a href="seo-services-education.html">University Enrollment Surges via Search</a></h3>
                        
                        <div class="portfolio-metrics">
                            <div class="metric">
                                <span class="metric-value">+180%</span>
                                <span class="metric-label">Student Inquiries</span>
                            </div>
                            <div class="metric">
                                <span class="metric-value">85%</span>
                                <span class="metric-label">Lower Cost Per Lead</span>
                            </div>
                        </div>

                        <p class="dark-blog-excerpt">By targeting high-intent degree queries and optimizing their program pages, we shifted their reliance away from paid ads to sustainable organic growth.</p>
                        
                    </div>
                </div>

            </div>
            
            <div style="text-align: center; margin-top: 5rem;">
                <h2 style="font-size: 2.5rem; margin-bottom: 1.5rem; font-weight: 800;">Ready to be our next success story?</h2>
                <p style="color: rgba(255,255,255,0.7); max-width: 600px; margin: 0 auto 2rem auto;">Let's discuss how data-driven SEO can transform your business growth.</p>
                <a href="contact.html" class="btn btn-primary" style="padding: 1rem 2.5rem; font-size: 1.1rem; border-radius: 50px;">Book a Strategy Call</a>
            </div>

        </div>
    </main>

    <script>
        document.addEventListener('DOMContentLoaded', () => {
            const filterBtns = document.querySelectorAll('#portfolio-filters .dark-filter-btn');
            const cards = document.querySelectorAll('.portfolio-card');

            function filterPortfolio() {
                const activeFilter = document.querySelector('#portfolio-filters .dark-filter-btn.active').getAttribute('data-filter');

                cards.forEach(card => {
                    const category = card.getAttribute('data-category');
                    if (activeFilter === 'all' || category === activeFilter) {
                        card.style.display = 'flex';
                    } else {
                        card.style.display = 'none';
                    }
                });
            }

            filterBtns.forEach(btn => {
                btn.addEventListener('click', () => {
                    filterBtns.forEach(b => b.classList.remove('active'));
                    btn.classList.add('active');
                    filterPortfolio();
                });
            });
        });
    </script>
"""

# Replace the <main> section
portfolio_html = re.sub(r'<main.*?</main>', portfolio_main, template_html, flags=re.DOTALL)

# Strip out the blog-specific script at the bottom if it was captured
portfolio_html = re.sub(r'<script>\s*document\.addEventListener\(\'DOMContentLoaded\', \(\) => {\s*const filterBtns = document\.querySelectorAll\(\'\.dark-filter-btn\'\);.*?</script>', '', portfolio_html, flags=re.DOTALL)

with open('portfolio.html', 'w', encoding='utf-8') as f:
    f.write(portfolio_html)

print("Created portfolio.html")

# Create CSS styles for the portfolio metrics
css_styles = """
/* ==========================================================================
   Portfolio Page Additions
   ========================================================================== */
.portfolio-metrics {
    display: flex;
    gap: 1.5rem;
    margin: 1.5rem 0;
    padding: 1rem 0;
    border-top: 1px solid rgba(255, 255, 255, 0.1);
    border-bottom: 1px solid rgba(255, 255, 255, 0.1);
}

.portfolio-metrics .metric {
    display: flex;
    flex-direction: column;
}

.portfolio-metrics .metric-value {
    font-size: 1.5rem;
    font-weight: 800;
    color: #84cc16;
}

.portfolio-metrics .metric-label {
    font-size: 0.75rem;
    color: rgba(255, 255, 255, 0.6);
    text-transform: uppercase;
    letter-spacing: 1px;
}
"""

with open('css/styles.css', 'a', encoding='utf-8') as f:
    f.write(css_styles)

print("Appended portfolio CSS to styles.css")

