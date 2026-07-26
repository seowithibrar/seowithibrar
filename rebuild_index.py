import re
import os

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Extract head to preserve SEO
head_match = re.search(r'(<head>.*?</head>)', html, re.DOTALL)
head_content = head_match.group(1) if head_match else ""

if 'js/main.js' not in head_content:
    head_content = head_content.replace('</head>', '    <script src="js/main.js" defer></script>\n</head>')

new_body = """<body>
    <!-- Header Navigation -->
    <header class="navbar">
        <div class="container nav-container">
            <a href="index.html" class="logo">
                <img src="images/logo-full.png" alt="SEO With Ibrar Logo" class="logo-img">
            </a>
            
            <nav class="nav-menu">
                <a href="index.html" class="nav-link active">HOME</a>
                <div class="nav-item-dropdown">
                    <a href="#" class="nav-link">SERVICES <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M6 9l6 6 6-6"/></svg></a>
                    <div class="dropdown-menu">
                        <a href="seo-services-pakistan.html" class="dropdown-item">SEO Expert Services</a>
                        <a href="seo-services-visa-consultancy.html" class="dropdown-item">Visa Consultancy SEO</a>
                        <a href="seo-services-education.html" class="dropdown-item">Education SEO</a>
                        <a href="wordpress-design-services.html" class="dropdown-item">WordPress Solutions</a>
                    </div>
                </div>
                <a href="about.html" class="nav-link">ABOUT</a>
                <a href="portfolio.html" class="nav-link">PORTFOLIO</a>
                <a href="blog.html" class="nav-link">BLOG</a>
            </nav>
            
            <a href="contact.html" class="btn btn-primary nav-cta">Book Consultation</a>
            
            <button class="mobile-menu-btn" aria-label="Toggle Menu">
                <span></span>
                <span></span>
                <span></span>
            </button>
        </div>
    </header>

    <main>
        <!-- Premium Hero Section -->
        <section class="hero" style="background-color: var(--color-bg-alt); position: relative; overflow: hidden; padding: 180px 0 100px;">
            <div class="container grid-12 items-center">
                <div class="hero-content" style="grid-column: span 7; position: relative; z-index: 10;">
                    <div class="fade-up">
                        <div style="display: flex; gap: 12px; margin-bottom: 24px; align-items: center;">
                            <span class="badge badge-primary">
                                <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2L2 7l10 5 10-5-10-5zM2 17l10 5 10-5M2 12l10 5 10-5"/></svg>
                                Google SEO Specialist
                            </span>
                            <div style="display: flex; align-items: center; gap: 4px; font-size: 0.875rem; font-weight: 600; color: var(--color-gray-700);">
                                <span style="color: #F59E0B;">★★★★★</span> 5.0 Google Rating
                            </div>
                        </div>
                        <h1 style="margin-bottom: 24px; line-height: 1.1;">Dominate Search Rankings with Enterprise SEO</h1>
                        <p class="text-xl" style="color: var(--color-gray-600); max-width: 600px; margin-bottom: 40px;">Ibrar Ahmad is a specialized SEO consultant delivering high-ROI organic growth, technical SEO, and premium WordPress architecture for global brands.</p>
                        
                        <div class="flex gap-16">
                            <a href="contact.html" class="btn btn-primary" style="padding: 16px 32px; font-size: 1.125rem;">Start Your Growth</a>
                            <a href="portfolio.html" class="btn btn-secondary" style="padding: 16px 32px; font-size: 1.125rem;">View Case Studies</a>
                        </div>
                        
                        <div class="hero-metrics" style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 24px; margin-top: 64px; padding-top: 32px; border-top: 1px solid var(--color-border);">
                            <div class="metric-item">
                                <span class="metric-value" style="font-size: 2.5rem; letter-spacing: -1px;">+340%</span>
                                <span class="metric-label">Avg. Traffic Growth</span>
                            </div>
                            <div class="metric-item">
                                <span class="metric-value" style="font-size: 2.5rem; letter-spacing: -1px;">120+</span>
                                <span class="metric-label">Projects Ranked</span>
                            </div>
                            <div class="metric-item">
                                <span class="metric-value" style="font-size: 2.5rem; letter-spacing: -1px;">7+</span>
                                <span class="metric-label">Years Experience</span>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="hero-visual fade-up delay-200" style="grid-column: span 5; position: relative;">
                    <!-- Floating Achievement Cards -->
                    <div style="position: absolute; top: -30px; right: -20px; background: white; padding: 16px; border-radius: 12px; box-shadow: var(--shadow-lg); z-index: 20; border: 1px solid var(--color-border); display: flex; align-items: center; gap: 12px;">
                        <div style="width: 40px; height: 40px; border-radius: 50%; background: var(--color-primary-light); display: flex; align-items: center; justify-content: center; color: var(--color-primary);">
                            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="22 12 18 12 15 21 9 3 6 12 2 12"></polyline></svg>
                        </div>
                        <div>
                            <div style="font-size: 0.75rem; color: var(--color-gray-500); font-weight: 600; text-transform: uppercase;">Traffic Milestone</div>
                            <div style="font-size: 1.125rem; font-weight: 800; color: var(--color-gray-900);">1M+ Monthly</div>
                        </div>
                    </div>
                    
                    <div style="background: var(--color-white); padding: var(--space-24); border-radius: var(--radius-lg); box-shadow: var(--shadow-card); border: 1px solid var(--color-border); position: relative; z-index: 2;">
                        <div class="flex justify-between items-center mb-24">
                            <div class="text-bold">Traffic Overview (Last 12 Months)</div>
                            <div class="badge badge-primary">+215%</div>
                        </div>
                        <!-- Mockup Graph -->
                        <div style="height: 200px; background: linear-gradient(0deg, rgba(140,198,63,0.1) 0%, rgba(255,255,255,0) 100%); border-bottom: 2px solid var(--color-primary); position: relative; display: flex; align-items: flex-end;">
                            <svg viewBox="0 0 100 40" preserveAspectRatio="none" style="width: 100%; height: 100%; position: absolute; bottom: 0; left: 0;"><path d="M0,40 L10,35 L20,38 L30,25 L40,28 L50,15 L60,18 L70,8 L80,10 L90,2 L100,0 L100,40 Z" fill="rgba(140,198,63,0.2)"/></svg>
                        </div>
                        <!-- Client Logos Mini -->
                        <div style="display: flex; gap: 8px; margin-top: 16px; justify-content: center;">
                            <div style="width: 8px; height: 8px; border-radius: 50%; background: var(--color-gray-300);"></div>
                            <div style="width: 8px; height: 8px; border-radius: 50%; background: var(--color-gray-300);"></div>
                            <div style="width: 8px; height: 8px; border-radius: 50%; background: var(--color-primary);"></div>
                        </div>
                    </div>
                    
                    <img src="images/ibrar.png" alt="Ibrar Ahmad SEO Expert" style="position: absolute; bottom: -60px; left: -40px; width: 180px; height: 180px; object-fit: cover; border-radius: 50%; box-shadow: var(--shadow-lg); z-index: 3; border: 6px solid var(--color-white);">
                </div>
            </div>
        </section>

        <!-- Trust Section -->
        <section class="trust-section">
            <div class="container">
                <p class="text-center text-bold text-muted mb-24" style="font-size: 0.875rem; letter-spacing: 1px; text-transform: uppercase;">Trusted by global brands & powered by industry tools</p>
                <div class="logo-strip">
                    <span style="font-size: 1.5rem; font-weight: 800; color: var(--color-gray-400);">ahrefs</span>
                    <span style="font-size: 1.5rem; font-weight: 800; color: var(--color-gray-400);">SEMRUSH</span>
                    <span style="font-size: 1.5rem; font-weight: 800; color: var(--color-gray-400);">Google Search Console</span>
                    <span style="font-size: 1.5rem; font-weight: 800; color: var(--color-gray-400);">WordPress</span>
                    <span style="font-size: 1.5rem; font-weight: 800; color: var(--color-gray-400);">ScreamingFrog</span>
                    <span style="font-size: 1.5rem; font-weight: 800; color: var(--color-gray-400);">Cloudflare</span>
                </div>
            </div>
        </section>

        <!-- Services Section -->
        <section class="py-120">
            <div class="container">
                <div class="grid-12 items-center mb-64">
                    <div class="fade-up" style="grid-column: span 6;">
                        <span class="badge badge-primary mb-16">Services</span>
                        <h2 style="font-size: 2.5rem; margin-bottom: 0;">Specialized SEO Solutions</h2>
                    </div>
                    <div class="fade-up delay-100" style="grid-column: span 6;">
                        <p style="margin-bottom: 0; font-size: 1.125rem;">Comprehensive growth systems built on technical foundations, content authority, and conversion optimization. Every strategy is tailored to your business model.</p>
                    </div>
                </div>
                
                <div class="grid-12">
                    <div class="card fade-up delay-100" style="grid-column: span 4;">
                        <div class="card-icon">
                            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"></path><polyline points="3.27 6.96 12 12.01 20.73 6.96"></polyline><line x1="12" y1="22.08" x2="12" y2="12"></line></svg>
                        </div>
                        <h3 style="font-size: 1.5rem;">Enterprise SEO</h3>
                        <p style="font-size: 0.9375rem; margin-bottom: 32px;">Scalable organic growth strategies designed for large-scale websites to dominate highly competitive international search landscapes.</p>
                        <ul style="list-style: none; padding: 0; margin-bottom: 32px; flex-grow: 1;">
                            <li style="margin-bottom: 8px; display: flex; align-items: center; gap: 8px; font-size: 0.875rem;"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="var(--color-primary)" stroke-width="2"><polyline points="20 6 9 17 4 12"></polyline></svg> Global Search Domination</li>
                            <li style="margin-bottom: 8px; display: flex; align-items: center; gap: 8px; font-size: 0.875rem;"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="var(--color-primary)" stroke-width="2"><polyline points="20 6 9 17 4 12"></polyline></svg> Advanced Site Architecture</li>
                            <li style="margin-bottom: 8px; display: flex; align-items: center; gap: 8px; font-size: 0.875rem;"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="var(--color-primary)" stroke-width="2"><polyline points="20 6 9 17 4 12"></polyline></svg> AI & GEO Optimization</li>
                        </ul>
                        <a href="seo-services-pakistan.html" class="btn btn-secondary" style="width: 100%;">View Service</a>
                    </div>
                    
                    <div class="card fade-up delay-200" style="grid-column: span 4; border: 2px solid var(--color-primary); position: relative;">
                        <div style="position: absolute; top: -12px; left: 50%; transform: translateX(-50%); background: var(--color-primary); color: white; padding: 4px 16px; border-radius: 100px; font-size: 0.75rem; font-weight: 700; text-transform: uppercase; letter-spacing: 1px;">Most Popular</div>
                        <div class="card-icon" style="background: var(--color-primary-light);">
                            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 16 14"></polyline></svg>
                        </div>
                        <h3 style="font-size: 1.5rem;">Technical SEO</h3>
                        <p style="font-size: 0.9375rem; margin-bottom: 32px;">Advanced crawlability, indexing, and Core Web Vitals optimization to ensure search engines love your underlying architecture.</p>
                        <ul style="list-style: none; padding: 0; margin-bottom: 32px; flex-grow: 1;">
                            <li style="margin-bottom: 8px; display: flex; align-items: center; gap: 8px; font-size: 0.875rem;"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="var(--color-primary)" stroke-width="2"><polyline points="20 6 9 17 4 12"></polyline></svg> Core Web Vitals Fixes</li>
                            <li style="margin-bottom: 8px; display: flex; align-items: center; gap: 8px; font-size: 0.875rem;"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="var(--color-primary)" stroke-width="2"><polyline points="20 6 9 17 4 12"></polyline></svg> Schema Markup Integration</li>
                            <li style="margin-bottom: 8px; display: flex; align-items: center; gap: 8px; font-size: 0.875rem;"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="var(--color-primary)" stroke-width="2"><polyline points="20 6 9 17 4 12"></polyline></svg> JavaScript SEO Handling</li>
                        </ul>
                        <a href="seo-services-pakistan.html" class="btn btn-primary" style="width: 100%;">View Service</a>
                    </div>
                    
                    <div class="card fade-up delay-300" style="grid-column: span 4;">
                        <div class="card-icon">
                            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="3" width="20" height="14" rx="2" ry="2"></rect><line x1="8" y1="21" x2="16" y2="21"></line><line x1="12" y1="17" x2="12" y2="21"></line></svg>
                        </div>
                        <h3 style="font-size: 1.5rem;">WordPress Design</h3>
                        <p style="font-size: 0.9375rem; margin-bottom: 32px;">Custom, lightning-fast WordPress builds optimized precisely for search performance and maximum user conversion rates.</p>
                        <ul style="list-style: none; padding: 0; margin-bottom: 32px; flex-grow: 1;">
                            <li style="margin-bottom: 8px; display: flex; align-items: center; gap: 8px; font-size: 0.875rem;"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="var(--color-primary)" stroke-width="2"><polyline points="20 6 9 17 4 12"></polyline></svg> Custom Theme Development</li>
                            <li style="margin-bottom: 8px; display: flex; align-items: center; gap: 8px; font-size: 0.875rem;"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="var(--color-primary)" stroke-width="2"><polyline points="20 6 9 17 4 12"></polyline></svg> Conversion Rate Optimization</li>
                            <li style="margin-bottom: 8px; display: flex; align-items: center; gap: 8px; font-size: 0.875rem;"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="var(--color-primary)" stroke-width="2"><polyline points="20 6 9 17 4 12"></polyline></svg> Extreme Speed Optimization</li>
                        </ul>
                        <a href="wordpress-design-services.html" class="btn btn-secondary" style="width: 100%;">View Service</a>
                    </div>
                </div>
            </div>
        </section>

        <!-- Why Choose Me (Comparison) -->
        <section class="section-alt py-120">
            <div class="container">
                <div class="text-center fade-up mb-64">
                    <span class="badge badge-primary mb-16">The Difference</span>
                    <h2>Why Partner With Me?</h2>
                    <p class="mx-auto text-xl">I don't just sell keywords. I build revenue engines.</p>
                </div>
                
                <div class="grid-12">
                    <div class="card fade-up" style="grid-column: span 6; padding: var(--space-32);">
                        <div style="display: flex; gap: 24px;">
                            <div style="flex-shrink: 0; width: 48px; height: 48px; background: var(--color-gray-900); color: white; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: bold; font-size: 1.25rem;">01</div>
                            <div>
                                <h3 style="font-size: 1.25rem;">ROI-Obsessed Strategy</h3>
                                <p style="font-size: 0.9375rem; margin-bottom: 0;">We target keywords that bring buyers, not just browsers. Every SEO campaign is tied directly to your revenue goals and lead generation targets.</p>
                            </div>
                        </div>
                    </div>
                    <div class="card fade-up delay-100" style="grid-column: span 6; padding: var(--space-32);">
                        <div style="display: flex; gap: 24px;">
                            <div style="flex-shrink: 0; width: 48px; height: 48px; background: var(--color-gray-900); color: white; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: bold; font-size: 1.25rem;">02</div>
                            <div>
                                <h3 style="font-size: 1.25rem;">Absolute Transparency</h3>
                                <p style="font-size: 0.9375rem; margin-bottom: 0;">No black-box SEO. You receive access to real-time live dashboards, detailed monthly execution reports, and crystal-clear communication.</p>
                            </div>
                        </div>
                    </div>
                    <div class="card fade-up" style="grid-column: span 6; padding: var(--space-32);">
                        <div style="display: flex; gap: 24px;">
                            <div style="flex-shrink: 0; width: 48px; height: 48px; background: var(--color-gray-900); color: white; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: bold; font-size: 1.25rem;">03</div>
                            <div>
                                <h3 style="font-size: 1.25rem;">Technical Supremacy</h3>
                                <p style="font-size: 0.9375rem; margin-bottom: 0;">I am not just a marketer; I am a technical SEO expert. I fix deep server issues, JavaScript rendering problems, and Core Web Vitals directly.</p>
                            </div>
                        </div>
                    </div>
                    <div class="card fade-up delay-100" style="grid-column: span 6; padding: var(--space-32);">
                        <div style="display: flex; gap: 24px;">
                            <div style="flex-shrink: 0; width: 48px; height: 48px; background: var(--color-gray-900); color: white; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: bold; font-size: 1.25rem;">04</div>
                            <div>
                                <h3 style="font-size: 1.25rem;">AI & Future-Proofed</h3>
                                <p style="font-size: 0.9375rem; margin-bottom: 0;">We optimize for Generative Engine Optimization (GEO) and AI search engines, ensuring your brand survives the evolution of Google Search.</p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- SEO Process Timeline -->
        <section class="py-120">
            <div class="container">
                <div class="text-center fade-up mb-64">
                    <span class="badge badge-primary mb-16">The Process</span>
                    <h2>How We Win Together</h2>
                    <p class="mx-auto text-xl">A proven, systematic approach to dominating organic search.</p>
                </div>
                
                <div style="position: relative; max-width: 800px; margin: 0 auto;">
                    <!-- Timeline Line -->
                    <div style="position: absolute; top: 0; bottom: 0; left: 24px; width: 2px; background: var(--color-border); z-index: 1;"></div>
                    
                    <div class="fade-up mb-48" style="position: relative; z-index: 2; display: flex; gap: 32px;">
                        <div style="width: 50px; height: 50px; border-radius: 50%; background: var(--color-white); border: 2px solid var(--color-primary); display: flex; align-items: center; justify-content: center; flex-shrink: 0; box-shadow: var(--shadow-md);">
                            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="var(--color-primary)" stroke-width="2"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg>
                        </div>
                        <div class="card" style="padding: var(--space-32); width: 100%;">
                            <h3 style="font-size: 1.25rem;">1. Comprehensive Audit</h3>
                            <p style="font-size: 0.9375rem; margin-bottom: 0;">We analyze your site architecture, backlink profile, content gaps, and technical hurdles to establish an exact baseline.</p>
                        </div>
                    </div>
                    
                    <div class="fade-up mb-48" style="position: relative; z-index: 2; display: flex; gap: 32px;">
                        <div style="width: 50px; height: 50px; border-radius: 50%; background: var(--color-white); border: 2px solid var(--color-primary); display: flex; align-items: center; justify-content: center; flex-shrink: 0; box-shadow: var(--shadow-md);">
                            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="var(--color-primary)" stroke-width="2"><path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"></path></svg>
                        </div>
                        <div class="card" style="padding: var(--space-32); width: 100%;">
                            <h3 style="font-size: 1.25rem;">2. Strategy & Architecture</h3>
                            <p style="font-size: 0.9375rem; margin-bottom: 0;">We build a keyword map, restructure your site hierarchy for optimal crawl depth, and outline a 6-month content runway.</p>
                        </div>
                    </div>
                    
                    <div class="fade-up mb-48" style="position: relative; z-index: 2; display: flex; gap: 32px;">
                        <div style="width: 50px; height: 50px; border-radius: 50%; background: var(--color-white); border: 2px solid var(--color-primary); display: flex; align-items: center; justify-content: center; flex-shrink: 0; box-shadow: var(--shadow-md);">
                            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="var(--color-primary)" stroke-width="2"><polyline points="22 12 18 12 15 21 9 3 6 12 2 12"></polyline></svg>
                        </div>
                        <div class="card" style="padding: var(--space-32); width: 100%;">
                            <h3 style="font-size: 1.25rem;">3. Execution & Optimization</h3>
                            <p style="font-size: 0.9375rem; margin-bottom: 0;">Fixing technical debt, optimizing on-page elements, publishing authoritative content, and acquiring high-trust backlinks.</p>
                        </div>
                    </div>
                    
                    <div class="fade-up" style="position: relative; z-index: 2; display: flex; gap: 32px;">
                        <div style="width: 50px; height: 50px; border-radius: 50%; background: var(--color-primary); border: 2px solid var(--color-primary); display: flex; align-items: center; justify-content: center; flex-shrink: 0; box-shadow: var(--shadow-md); color: white;">
                            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="23 6 13.5 15.5 8.5 10.5 1 18"></polyline><polyline points="17 6 23 6 23 12"></polyline></svg>
                        </div>
                        <div class="card" style="padding: var(--space-32); width: 100%; border: 2px solid var(--color-primary);">
                            <h3 style="font-size: 1.25rem;">4. Growth & Reporting</h3>
                            <p style="font-size: 0.9375rem; margin-bottom: 0;">Continuous monitoring, A/B testing conversion elements, adjusting to algorithm updates, and scaling revenue.</p>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- Interactive Industries Grid -->
        <section class="section-alt py-120">
            <div class="container">
                <div class="text-center fade-up mb-64">
                    <span class="badge badge-primary mb-16">Industries</span>
                    <h2>Specialized Industry Expertise</h2>
                </div>
                
                <div class="grid-12">
                    <div class="card fade-up text-center items-center justify-center" style="grid-column: span 3; padding: var(--space-32);">
                        <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="var(--color-primary)" stroke-width="2" style="margin-bottom: 16px;"><path d="M22 10v6M2 10l10-5 10 5-10 5z"></path><path d="M6 12v5c3 3 9 3 12 0v-5"></path></svg>
                        <h4 style="margin: 0;">Education</h4>
                    </div>
                    <div class="card fade-up delay-100 text-center items-center justify-center" style="grid-column: span 3; padding: var(--space-32);">
                        <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="var(--color-primary)" stroke-width="2" style="margin-bottom: 16px;"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"></path></svg>
                        <h4 style="margin: 0;">Law Firms</h4>
                    </div>
                    <div class="card fade-up delay-200 text-center items-center justify-center" style="grid-column: span 3; padding: var(--space-32);">
                        <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="var(--color-primary)" stroke-width="2" style="margin-bottom: 16px;"><path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"></path><polyline points="9 22 9 12 15 12 15 22"></polyline></svg>
                        <h4 style="margin: 0;">Real Estate</h4>
                    </div>
                    <div class="card fade-up delay-300 text-center items-center justify-center" style="grid-column: span 3; padding: var(--space-32);">
                        <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="var(--color-primary)" stroke-width="2" style="margin-bottom: 16px;"><circle cx="12" cy="12" r="10"></circle><path d="M12 8v4l3 3"></path></svg>
                        <h4 style="margin: 0;">Visa Consultancy</h4>
                    </div>
                    <div class="card fade-up text-center items-center justify-center" style="grid-column: span 3; padding: var(--space-32);">
                        <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="var(--color-primary)" stroke-width="2" style="margin-bottom: 16px;"><path d="M20.59 13.41l-7.17 7.17a2 2 0 0 1-2.83 0L2 12V2h10l8.59 8.59a2 2 0 0 1 0 2.82z"></path><line x1="7" y1="7" x2="7.01" y2="7"></line></svg>
                        <h4 style="margin: 0;">E-commerce</h4>
                    </div>
                    <div class="card fade-up delay-100 text-center items-center justify-center" style="grid-column: span 3; padding: var(--space-32);">
                        <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="var(--color-primary)" stroke-width="2" style="margin-bottom: 16px;"><rect x="2" y="3" width="20" height="14" rx="2" ry="2"></rect><line x1="8" y1="21" x2="16" y2="21"></line><line x1="12" y1="17" x2="12" y2="21"></line></svg>
                        <h4 style="margin: 0;">SaaS</h4>
                    </div>
                    <div class="card fade-up delay-200 text-center items-center justify-center" style="grid-column: span 3; padding: var(--space-32);">
                        <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="var(--color-primary)" stroke-width="2" style="margin-bottom: 16px;"><path d="M19 14c1.49-1.46 3-3.21 3-5.5A5.5 5.5 0 0 0 16.5 3c-1.76 0-3 .5-4.5 2-1.5-1.5-2.74-2-4.5-2A5.5 5.5 0 0 0 2 8.5c0 2.3 1.5 4.05 3 5.5l7 7Z"></path></svg>
                        <h4 style="margin: 0;">Healthcare</h4>
                    </div>
                    <div class="card fade-up delay-300 text-center items-center justify-center" style="grid-column: span 3; padding: var(--space-32);">
                        <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="var(--color-primary)" stroke-width="2" style="margin-bottom: 16px;"><path d="M12 2v20M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"></path></svg>
                        <h4 style="margin: 0;">Finance</h4>
                    </div>
                </div>
            </div>
        </section>

        <!-- Call to Action -->
        <section class="section-dark py-120 text-center">
            <div class="container fade-up">
                <span class="badge" style="background: rgba(255,255,255,0.1); color: white; border: 1px solid rgba(255,255,255,0.2); margin-bottom: 24px;">Start Growing Today</span>
                <h2 style="font-size: 3rem; margin-bottom: var(--space-24);">Ready to scale your revenue?</h2>
                <p style="margin: 0 auto var(--space-48) auto; font-size: 1.25rem; max-width: 60ch;">Stop losing customers to competitors. Let's build a data-driven SEO strategy that turns your website into a reliable growth engine.</p>
                <div class="flex justify-center gap-16">
                    <a href="contact.html" class="btn btn-primary" style="background: var(--color-white); color: var(--color-gray-900);">Book Your Strategy Session</a>
                </div>
                <p style="font-size: 0.875rem; margin-top: 16px; opacity: 0.6;">No obligations. Just actionable SEO insights.</p>
            </div>
        </section>
    </main>

    <!-- Premium Footer -->
    <footer class="footer">
        <div class="container">
            <div class="footer-grid">
                <div style="grid-column: span 2;">
                    <img src="images/logo-full.png" alt="SEO With Ibrar" style="height: 40px; margin-bottom: 24px; filter: brightness(0) invert(1);">
                    <p style="font-size: 0.9375rem; max-width: 300px; line-height: 1.8;">Award-winning SEO consultant and Web Designer delivering data-driven organic growth and premium WordPress architecture for global brands.</p>
                    <div style="display: flex; gap: 16px; margin-top: 24px;">
                        <a href="#" style="color: white; opacity: 0.7;"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-2-2 2 2 0 0 0-2 2v7h-4v-7a6 6 0 0 1 6-6z"></path><rect x="2" y="9" width="4" height="12"></rect><circle cx="4" cy="4" r="2"></circle></svg></a>
                        <a href="#" style="color: white; opacity: 0.7;"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M23 3a10.9 10.9 0 0 1-3.14 1.53 4.48 4.48 0 0 0-7.86 3v1A10.66 10.66 0 0 1 3 4s-4 9 5 13a11.64 11.64 0 0 1-7 2c9 5 20 0 20-11.5a4.5 4.5 0 0 0-.08-.83A7.72 7.72 0 0 0 23 3z"></path></svg></a>
                    </div>
                </div>
                <div>
                    <div class="footer-heading">Services</div>
                    <div class="footer-links">
                        <a href="seo-services-pakistan.html">Enterprise SEO</a>
                        <a href="seo-services-visa-consultancy.html">Visa SEO</a>
                        <a href="seo-services-education.html">Education SEO</a>
                        <a href="wordpress-design-services.html">WordPress Dev</a>
                        <a href="seo-services-lahore.html">Local SEO</a>
                    </div>
                </div>
                <div>
                    <div class="footer-heading">Company</div>
                    <div class="footer-links">
                        <a href="about.html">About Ibrar</a>
                        <a href="portfolio.html">Case Studies</a>
                        <a href="blog.html">SEO Blog</a>
                        <a href="contact.html">Contact Us</a>
                    </div>
                </div>
                <div>
                    <div class="footer-heading">Legal</div>
                    <div class="footer-links">
                        <a href="#">Privacy Policy</a>
                        <a href="#">Terms of Service</a>
                        <a href="#">Cookie Policy</a>
                    </div>
                </div>
            </div>
            <div class="footer-bottom">
                <div>&copy; <span id="current-year"></span> SEO With Ibrar. All rights reserved. Built with precision.</div>
            </div>
        </div>
    </footer>
</body>
"""

final_html = f"<!DOCTYPE html>\n<html lang=\"en\">\n{head_content}\n{new_body}\n</html>"

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(final_html)

print("index.html successfully updated to the NEW design system Phase 3 requirements.")
