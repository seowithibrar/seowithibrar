import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Prepare modern CSS to insert into <head>
css_block = """    <style>
        /* ==========================================================================
           HYBRID AGENCY REDESIGN — BESPOKE ARCHITECTURE
           Dark Obsidian Hero & CTA + Crisp Modern High-Contrast Light Bento Grids
           ========================================================================== */
        :root {
            --obsidian-bg: #070c18;
            --obsidian-surface: #0e1628;
            --obsidian-border: rgba(255, 255, 255, 0.08);
            --brand-green: #8cc63f;
            --brand-green-hover: #7bb332;
            --brand-green-glow: rgba(140, 198, 63, 0.25);
            --shadow-xl: 0 25px 50px -12px rgba(0, 0, 0, 0.25);
        }

        /* 1. HERO SECTION (Dark Obsidian Surface) */
        .hero-agency {
            background: radial-gradient(circle at 50% -20%, rgba(140, 198, 63, 0.12) 0%, transparent 60%),
                        linear-gradient(180deg, #070c18 0%, #0d1527 100%);
            color: #ffffff;
            position: relative;
            padding: 180px 0 100px;
            overflow: hidden;
            border-bottom: 1px solid rgba(255, 255, 255, 0.08);
        }
        .hero-agency::before {
            content: '';
            position: absolute;
            top: 25%;
            right: 8%;
            width: 480px;
            height: 480px;
            background: radial-gradient(circle, rgba(56, 189, 248, 0.05) 0%, transparent 70%);
            pointer-events: none;
        }

        .hero-badge-pill {
            display: inline-flex;
            align-items: center;
            gap: 10px;
            background: rgba(140, 198, 63, 0.12);
            border: 1px solid rgba(140, 198, 63, 0.3);
            color: var(--brand-green);
            padding: 7px 20px;
            border-radius: 999px;
            font-size: 0.8rem;
            font-weight: 700;
            letter-spacing: 0.5px;
            text-transform: uppercase;
            margin-bottom: 24px;
        }
        .hero-badge-pill .pulse-dot {
            width: 8px;
            height: 8px;
            background-color: var(--brand-green);
            border-radius: 50%;
            box-shadow: 0 0 10px var(--brand-green);
            display: inline-block;
        }

        .hero-title-main {
            font-size: 3.6rem;
            font-weight: 900;
            line-height: 1.08;
            letter-spacing: -0.035em;
            color: #ffffff;
            margin-bottom: 24px;
        }
        .hero-title-main .text-highlight {
            background: linear-gradient(135deg, #ffffff 30%, #8cc63f 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }

        .hero-desc-main {
            font-size: 1.15rem;
            line-height: 1.7;
            color: #cbd5e1;
            max-width: 620px;
            margin-bottom: 40px;
        }

        .hero-actions {
            display: flex;
            align-items: center;
            gap: 16px;
            flex-wrap: wrap;
            margin-bottom: 56px;
        }
        .btn-agency-primary {
            background-color: var(--brand-green);
            color: #070c18 !important;
            font-weight: 800;
            font-size: 1.05rem;
            padding: 16px 36px;
            border-radius: 12px;
            display: inline-flex;
            align-items: center;
            gap: 10px;
            transition: all 0.25s cubic-bezier(0.4, 0, 0.2, 1);
            box-shadow: 0 10px 25px rgba(140, 198, 63, 0.25);
            text-decoration: none;
        }
        .btn-agency-primary:hover {
            background-color: var(--brand-green-hover);
            transform: translateY(-2px);
            box-shadow: 0 14px 30px rgba(140, 198, 63, 0.35);
        }
        .btn-agency-secondary {
            background: rgba(255, 255, 255, 0.05);
            border: 1px solid rgba(255, 255, 255, 0.15);
            color: #ffffff !important;
            font-weight: 700;
            font-size: 1.05rem;
            padding: 16px 32px;
            border-radius: 12px;
            display: inline-flex;
            align-items: center;
            gap: 8px;
            transition: all 0.25s ease;
            text-decoration: none;
            backdrop-filter: blur(8px);
        }
        .btn-agency-secondary:hover {
            background: rgba(255, 255, 255, 0.1);
            border-color: rgba(255, 255, 255, 0.3);
            transform: translateY(-2px);
        }

        .hero-metrics-bar {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 20px;
            padding-top: 32px;
            border-top: 1px solid rgba(255, 255, 255, 0.1);
        }
        .hero-metric-box .metric-num {
            font-size: 2.25rem;
            font-weight: 900;
            letter-spacing: -0.02em;
            color: #ffffff;
            line-height: 1;
            margin-bottom: 6px;
        }
        .hero-metric-box .metric-num span {
            color: var(--brand-green);
        }
        .hero-metric-box .metric-tag {
            font-size: 0.8rem;
            color: #94a3b8;
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }

        /* Hero Right: Production Cockpit Card */
        .hero-cockpit {
            position: relative;
            background: rgba(14, 22, 40, 0.7);
            border: 1px solid rgba(255, 255, 255, 0.12);
            border-radius: 28px;
            padding: 24px;
            box-shadow: 0 30px 60px rgba(0, 0, 0, 0.5);
            backdrop-filter: blur(16px);
        }
        .cockpit-top-bar {
            display: flex;
            align-items: center;
            justify-content: space-between;
            padding-bottom: 16px;
            margin-bottom: 20px;
            border-bottom: 1px solid rgba(255, 255, 255, 0.08);
            font-size: 0.75rem;
            color: #94a3b8;
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 1px;
        }
        .cockpit-dots {
            display: flex;
            gap: 6px;
        }
        .cockpit-dot {
            width: 9px;
            height: 9px;
            border-radius: 50%;
        }
        .cockpit-dot.red { background: #ef4444; }
        .cockpit-dot.yellow { background: #f59e0b; }
        .cockpit-dot.green { background: #10b981; }

        .cockpit-photo-wrap {
            position: relative;
            border-radius: 20px;
            overflow: hidden;
            background: linear-gradient(180deg, #131d33 0%, #090e1a 100%);
            aspect-ratio: 4/4.8;
            display: flex;
            align-items: flex-end;
            justify-content: center;
            border: 1px solid rgba(255, 255, 255, 0.06);
        }
        .cockpit-photo-wrap img {
            width: 100%;
            height: 100%;
            object-fit: cover;
            object-position: bottom;
            pointer-events: none;
        }

        .cockpit-badge-top {
            position: absolute;
            top: 16px;
            left: 16px;
            background: rgba(9, 14, 26, 0.9);
            border: 1px solid rgba(140, 198, 63, 0.4);
            padding: 8px 14px;
            border-radius: 12px;
            backdrop-filter: blur(10px);
            display: flex;
            align-items: center;
            gap: 8px;
            font-size: 0.75rem;
            font-weight: 800;
            color: #ffffff;
            z-index: 5;
        }
        .cockpit-badge-bottom {
            position: absolute;
            bottom: 16px;
            right: 16px;
            background: rgba(9, 14, 26, 0.92);
            border: 1px solid rgba(255, 255, 255, 0.15);
            padding: 10px 18px;
            border-radius: 14px;
            backdrop-filter: blur(12px);
            display: flex;
            align-items: center;
            gap: 10px;
            font-size: 0.8rem;
            font-weight: 800;
            color: var(--brand-green);
            z-index: 5;
            box-shadow: 0 10px 25px rgba(0,0,0,0.4);
        }

        /* 2. TRUSTED MARQUEE RIBBON */
        .trust-ribbon {
            background: #090e1a;
            border-bottom: 1px solid rgba(255, 255, 255, 0.08);
            padding: 26px 0;
        }
        .trust-ribbon-inner {
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 24px;
            flex-wrap: wrap;
        }
        .trust-label {
            font-size: 0.75rem;
            font-weight: 700;
            letter-spacing: 1.5px;
            text-transform: uppercase;
            color: #64748b;
        }
        .trust-logos-list {
            display: flex;
            align-items: center;
            gap: 40px;
            flex-wrap: wrap;
        }
        .trust-item-name {
            font-size: 1.25rem;
            font-weight: 800;
            letter-spacing: -0.5px;
            color: #94a3b8;
            transition: color 0.2s ease;
        }
        .trust-item-name:hover {
            color: #ffffff;
        }

        /* 3. SECTION HEADERS */
        .section-header-modern {
            text-align: center;
            max-width: 780px;
            margin: 0 auto 56px;
        }
        .section-eyebrow {
            display: inline-flex;
            align-items: center;
            gap: 8px;
            background: rgba(140, 198, 63, 0.12);
            color: #4d7c0f;
            border: 1px solid rgba(140, 198, 63, 0.25);
            font-size: 0.75rem;
            font-weight: 800;
            padding: 6px 16px;
            border-radius: 999px;
            text-transform: uppercase;
            letter-spacing: 1px;
            margin-bottom: 16px;
        }
        .section-heading-lg {
            font-size: 2.85rem;
            font-weight: 900;
            line-height: 1.12;
            letter-spacing: -0.03em;
            color: #0f172a;
            margin-bottom: 16px;
        }
        .section-subtext {
            font-size: 1.05rem;
            line-height: 1.7;
            color: #64748b;
        }

        /* 4. ASYMMETRIC BENTO GRID */
        .bento-grid-12 {
            display: grid;
            grid-template-columns: repeat(12, 1fr);
            gap: 28px;
        }
        .bento-card {
            background: #ffffff;
            border: 1px solid #e2e8f0;
            border-radius: 24px;
            padding: 40px;
            position: relative;
            overflow: hidden;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.03);
            transition: transform 0.3s cubic-bezier(0.4, 0, 0.2, 1), box-shadow 0.3s ease, border-color 0.3s ease;
        }
        .bento-card:hover {
            transform: translateY(-6px);
            box-shadow: 0 20px 40px rgba(0, 0, 0, 0.07);
            border-color: #cbd5e1;
        }
        .bento-card-featured {
            background: linear-gradient(145deg, #0f172a 0%, #1e293b 100%);
            color: #ffffff;
            border-color: rgba(255, 255, 255, 0.1);
        }
        .bento-card-featured .bento-title {
            color: #ffffff;
        }
        .bento-card-featured .bento-desc {
            color: #94a3b8;
        }
        .bento-card-featured:hover {
            border-color: var(--brand-green);
            box-shadow: 0 25px 50px rgba(0, 0, 0, 0.35);
        }

        .bento-icon-box {
            width: 52px;
            height: 52px;
            border-radius: 14px;
            display: flex;
            align-items: center;
            justify-content: center;
            margin-bottom: 24px;
            font-weight: 800;
        }
        .bento-icon-light {
            background: rgba(140, 198, 63, 0.15);
            color: #4d7c0f;
        }
        .bento-icon-dark {
            background: rgba(140, 198, 63, 0.2);
            color: var(--brand-green);
        }

        .bento-tag {
            font-size: 0.72rem;
            font-weight: 800;
            letter-spacing: 0.5px;
            text-transform: uppercase;
            padding: 4px 12px;
            border-radius: 999px;
            display: inline-block;
            margin-bottom: 12px;
        }
        .bento-tag-green {
            background: rgba(140, 198, 63, 0.15);
            color: #4d7c0f;
        }
        .bento-tag-white {
            background: rgba(255, 255, 255, 0.1);
            color: var(--brand-green);
        }

        .bento-title {
            font-size: 1.55rem;
            font-weight: 800;
            color: #0f172a;
            margin-bottom: 12px;
            line-height: 1.25;
            letter-spacing: -0.02em;
        }
        .bento-desc {
            font-size: 0.95rem;
            color: #64748b;
            line-height: 1.65;
            margin-bottom: 28px;
        }

        .bento-link {
            display: inline-flex;
            align-items: center;
            gap: 8px;
            font-size: 0.92rem;
            font-weight: 800;
            color: #0f172a;
            text-decoration: none;
            transition: color 0.2s ease, gap 0.2s ease;
        }
        .bento-card-featured .bento-link {
            color: var(--brand-green);
        }
        .bento-link:hover {
            gap: 12px;
            color: var(--brand-green);
        }

        /* 5. DATA PROOF & CASE STUDIES CARDS */
        .case-studies-grid {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 28px;
        }
        .case-card-modern {
            background: #ffffff;
            border: 1px solid #e2e8f0;
            border-radius: 20px;
            overflow: hidden;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            box-shadow: 0 4px 16px rgba(0,0,0,0.03);
            transition: all 0.3s ease;
        }
        .case-card-modern:hover {
            transform: translateY(-6px);
            box-shadow: 0 20px 40px rgba(0,0,0,0.08);
            border-color: var(--brand-green);
        }
        .case-card-img-wrap {
            height: 200px;
            background: #0f172a;
            position: relative;
            overflow: hidden;
        }
        .case-card-img-wrap img {
            width: 100%;
            height: 100%;
            object-fit: cover;
            transition: transform 0.4s ease;
        }
        .case-card-modern:hover .case-card-img-wrap img {
            transform: scale(1.04);
        }
        .case-card-body {
            padding: 28px;
        }
        .case-pill {
            font-size: 0.72rem;
            font-weight: 800;
            color: #4d7c0f;
            background: rgba(140, 198, 63, 0.14);
            padding: 4px 10px;
            border-radius: 6px;
            text-transform: uppercase;
            display: inline-block;
            margin-bottom: 10px;
        }
        .case-card-title {
            font-size: 1.25rem;
            font-weight: 800;
            color: #0f172a;
            margin-bottom: 12px;
            line-height: 1.3;
        }
        .case-stat-box {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 12px;
            background: #f8fafc;
            border: 1px solid #f1f5f9;
            padding: 14px;
            border-radius: 12px;
            margin-top: 16px;
        }
        .case-stat-val {
            font-size: 1.25rem;
            font-weight: 900;
            color: #0f172a;
        }
        .case-stat-label {
            font-size: 0.72rem;
            color: #64748b;
            font-weight: 600;
        }

        /* 6. SCIENTIFIC FRAMEWORK PROCESS (4 Steps) */
        .process-steps-grid {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 24px;
        }
        .process-step-card {
            background: #ffffff;
            border: 1px solid #e2e8f0;
            border-radius: 20px;
            padding: 32px 24px;
            position: relative;
            transition: all 0.25s ease;
        }
        .process-step-card:hover {
            border-color: var(--brand-green);
            transform: translateY(-4px);
            box-shadow: 0 12px 30px rgba(0,0,0,0.05);
        }
        .step-num-badge {
            font-size: 1.75rem;
            font-weight: 900;
            color: var(--brand-green);
            margin-bottom: 16px;
            line-height: 1;
        }
        .step-card-title {
            font-size: 1.15rem;
            font-weight: 800;
            color: #0f172a;
            margin-bottom: 10px;
        }
        .step-card-desc {
            font-size: 0.88rem;
            color: #64748b;
            line-height: 1.6;
        }

        /* 7. AUTHENTIC CONSULTANT BIO ROW */
        .bio-section-box {
            background: #090e1a;
            color: #ffffff;
            border-radius: 28px;
            padding: 64px;
            display: grid;
            grid-template-columns: 1fr 1.2fr;
            gap: 56px;
            align-items: center;
            border: 1px solid rgba(255, 255, 255, 0.08);
            box-shadow: 0 30px 60px rgba(0,0,0,0.3);
        }
        .bio-photo-card {
            position: relative;
            border-radius: 22px;
            overflow: hidden;
            background: linear-gradient(180deg, #131c31 0%, #060a12 100%);
            aspect-ratio: 4/4.8;
            border: 1px solid rgba(255, 255, 255, 0.1);
        }
        .bio-photo-card img {
            width: 100%;
            height: 100%;
            object-fit: cover;
            object-position: bottom;
        }

        /* 8. FAQ ACCORDION HYBRID */
        .faq-accordion-box {
            max-width: 820px;
            margin: 0 auto;
        }
        .faq-card-item {
            background: #ffffff;
            border: 1px solid #e2e8f0;
            border-radius: 14px;
            margin-bottom: 14px;
            overflow: hidden;
            transition: border-color 0.2s ease;
        }
        .faq-card-item summary {
            padding: 22px 28px;
            font-size: 1.05rem;
            font-weight: 700;
            color: #0f172a;
            cursor: pointer;
            display: flex;
            justify-content: space-between;
            align-items: center;
            user-select: none;
        }
        .faq-card-item summary::-webkit-details-marker {
            display: none;
        }
        .faq-card-item summary::after {
            content: '+';
            font-size: 1.4rem;
            font-weight: 800;
            color: var(--brand-green);
            transition: transform 0.2s ease;
        }
        .faq-card-item details[open] summary::after {
            content: '\\2212';
        }
        .faq-answer-inner {
            padding: 0 28px 24px;
            color: #64748b;
            font-size: 0.95rem;
            line-height: 1.7;
            border-top: 1px solid #f1f5f9;
            padding-top: 16px;
        }

        /* Responsive Breakpoints */
        @media (max-width: 1024px) {
            .hero-title-main { font-size: 2.75rem; }
            .hero-agency { padding: 140px 0 80px; }
            .bento-grid-12 { grid-template-columns: 1fr; }
            .bento-card { grid-column: span 12 !important; }
            .hero-metrics-bar { grid-template-columns: repeat(2, 1fr); }
            .case-studies-grid { grid-template-columns: 1fr; }
            .process-steps-grid { grid-template-columns: repeat(2, 1fr); }
            .bio-section-box { grid-template-columns: 1fr; padding: 40px; }
        }
        @media (max-width: 768px) {
            .hero-title-main { font-size: 2.2rem; }
            .hero-desc-main { font-size: 1rem; }
            .hero-agency { padding: 120px 0 60px; }
            .hero-metrics-bar { grid-template-columns: 1fr 1fr; gap: 16px; }
            .process-steps-grid { grid-template-columns: 1fr; }
            .trust-ribbon-inner { justify-content: center; }
            .trust-logos-list { justify-content: center; gap: 20px; }
            .section-heading-lg { font-size: 2.1rem; }
        }
    </style>"""

# 2. Prepare modern <main> HTML
modern_main = """    <main>
        <!-- 1. Hero Section (Obsidian Dark Hybrid) -->
        <section class="hero-agency">
            <div class="container grid-12 items-center">
                <div class="hero-content" style="grid-column: span 7; position: relative; z-index: 10;">
                    <div class="fade-up">
                        <div class="hero-badge-pill">
                            <span class="pulse-dot"></span>
                            Top-Ranked SEO Consultant in Pakistan • 5.0 ★ Rating
                        </div>
                        <h1 class="hero-title-main">
                            Dominate Search Rankings with <span class="text-highlight">Enterprise Technical SEO</span>
                        </h1>
                        <p class="hero-desc-main">
                            Ibrar Ahmad is a specialized SEO consultant and WordPress engineer helping high-growth brands, immigration firms, and academies scale verified organic revenue and conquer tough search competition.
                        </p>
                        
                        <div class="hero-actions">
                            <a href="contact" class="btn-agency-primary">
                                Start Your Growth
                                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
                            </a>
                            <a href="portfolio" class="btn-agency-secondary">
                                View Case Studies
                            </a>
                        </div>
                        
                        <div class="hero-metrics-bar">
                            <div class="hero-metric-box">
                                <div class="metric-num">+340<span>%</span></div>
                                <div class="metric-tag">Avg. Traffic Growth</div>
                            </div>
                            <div class="hero-metric-box">
                                <div class="metric-num">120<span>+</span></div>
                                <div class="metric-tag">Brands Ranked</div>
                            </div>
                            <div class="hero-metric-box">
                                <div class="metric-num">98<span>%</span></div>
                                <div class="metric-tag">Core Web Vitals</div>
                            </div>
                            <div class="hero-metric-box">
                                <div class="metric-num">7<span>+</span></div>
                                <div class="metric-tag">Years Experience</div>
                            </div>
                        </div>
                    </div>
                </div>

                <div class="fade-up delay-200" style="grid-column: span 5;">
                    <div class="hero-cockpit">
                        <div class="cockpit-top-bar">
                            <div class="cockpit-dots">
                                <div class="cockpit-dot red"></div>
                                <div class="cockpit-dot yellow"></div>
                                <div class="cockpit-dot green"></div>
                            </div>
                            <div>Verified Production Data • GSC Active</div>
                        </div>
                        <div class="cockpit-photo-wrap">
                            <img src="images/Ibrar Ahmad.png" alt="Ibrar Ahmad - Senior SEO Consultant and WordPress Engineer in Pakistan">
                            <div class="cockpit-badge-top">
                                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="var(--brand-green)" stroke-width="2.5"><polyline points="20 6 9 17 4 12"></polyline></svg>
                                100% White-Hat Only
                            </div>
                            <div class="cockpit-badge-bottom">
                                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon></svg>
                                #1 Organic Rankings
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- 2. Trust Ribbon -->
        <section class="trust-ribbon">
            <div class="container trust-ribbon-inner">
                <div class="trust-label">Industry Tools & Verification:</div>
                <div class="trust-logos-list">
                    <span class="trust-item-name">ahrefs</span>
                    <span class="trust-item-name">SEMRUSH</span>
                    <span class="trust-item-name">Google Search Console</span>
                    <span class="trust-item-name">WordPress</span>
                    <span class="trust-item-name">ScreamingFrog</span>
                    <span class="trust-item-name">Cloudflare</span>
                </div>
            </div>
        </section>

        <!-- 3. Asymmetric Bento Grid: Strategic SEO Services -->
        <section class="py-120" style="background: #ffffff;">
            <div class="container">
                <div class="section-header-modern fade-up">
                    <span class="section-eyebrow">Organic Growth Architecture</span>
                    <h2 class="section-heading-lg">Precision SEO Services Built for Revenue</h2>
                    <p class="section-subtext">
                        We don't chase vanity metrics. Every SEO deployment is engineered around high-converting transactional searches, rock-solid technical health, and sustainable market dominance.
                    </p>
                </div>

                <div class="bento-grid-12">
                    <!-- Featured Bento Card: Enterprise SEO (Span 8) -->
                    <div class="bento-card bento-card-featured fade-up" style="grid-column: span 8;">
                        <div>
                            <div class="bento-icon-box bento-icon-dark">
                                <svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"></path></svg>
                            </div>
                            <span class="bento-tag bento-tag-white">Pillar Growth Program</span>
                            <h3 class="bento-title">Enterprise & Nationwide SEO</h3>
                            <p class="bento-desc">
                                End-to-end organic growth campaigns designed to dominate competitive high-volume keywords across Pakistan and international markets. Includes deep crawl optimization, semantic content clusters, entity-based internal linking, and white-hat digital PR acquisition.
                            </p>
                        </div>
                        <div>
                            <a href="seo-services-pakistan" class="bento-link">
                                Explore Enterprise SEO Solutions
                                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
                            </a>
                        </div>
                    </div>

                    <!-- Bento Card 2: Local Map Pack Dominance (Span 4) -->
                    <div class="bento-card fade-up delay-100" style="grid-column: span 4;">
                        <div>
                            <div class="bento-icon-box bento-icon-light">
                                <svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="10" r="3"></circle><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"></path></svg>
                            </div>
                            <span class="bento-tag bento-tag-green">Hyper-Local Map Pack</span>
                            <h3 class="bento-title">Local SEO & Google Maps</h3>
                            <p class="bento-desc">
                                Dominate the 3-Pack on Google Maps in Lahore, Karachi, and Islamabad. Local schema markup, geo-tagged citations, and high-trust local relevance.
                            </p>
                        </div>
                        <div>
                            <a href="seo-services-lahore" class="bento-link">
                                Discover Local SEO
                                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
                            </a>
                        </div>
                    </div>

                    <!-- Bento Card 3: Visa & Immigration SEO (Span 6) -->
                    <div class="bento-card fade-up delay-200" style="grid-column: span 6;">
                        <div>
                            <div class="bento-icon-box bento-icon-light">
                                <svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"></path></svg>
                            </div>
                            <span class="bento-tag bento-tag-green">Niche Vertical Authority</span>
                            <h3 class="bento-title">Visa & Immigration Consultancy SEO</h3>
                            <p class="bento-desc">
                                Specialized search strategies built exclusively for visa consultancies. Capture students and professionals searching for study abroad, work visas, and citizenship services with high conversion qualification.
                            </p>
                        </div>
                        <div>
                            <a href="seo-services-visa-consultancy" class="bento-link">
                                Visa Consultancy Strategies
                                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
                            </a>
                        </div>
                    </div>

                    <!-- Bento Card 4: Education & Academy SEO (Span 6) -->
                    <div class="bento-card fade-up delay-300" style="grid-column: span 6;">
                        <div>
                            <div class="bento-icon-box bento-icon-light">
                                <svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"></path><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"></path></svg>
                            </div>
                            <span class="bento-tag bento-tag-green">Enrollment Generation</span>
                            <h3 class="bento-title">Education & Academic Platform SEO</h3>
                            <p class="bento-desc">
                                Turn organic search queries into student enrollments for colleges, academies, and online learning platforms through syllabus hubs, high-trust accreditation markup, and localized academic visibility.
                            </p>
                        </div>
                        <div>
                            <a href="seo-services-education" class="bento-link">
                                Education SEO Solutions
                                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
                            </a>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- 4. WordPress Solutions Bento Grid -->
        <section class="py-120" style="background: #f8fafc; border-top: 1px solid #e2e8f0; border-bottom: 1px solid #e2e8f0;">
            <div class="container">
                <div class="section-header-modern fade-up">
                    <span class="section-eyebrow">Engineering Excellence</span>
                    <h2 class="section-heading-lg">WordPress Built for Extreme Speed & Conversion</h2>
                    <p class="section-subtext">
                        A slow or bloated website kills organic rankings. We engineer lightweight, custom WordPress web applications built with zero plugin bloat, sub-second load times, and perfect Core Web Vitals.
                    </p>
                </div>

                <div class="bento-grid-12">
                    <!-- WordPress Core Card (Span 6) -->
                    <div class="bento-card fade-up" style="grid-column: span 6; background: #ffffff;">
                        <div>
                            <div class="bento-icon-box bento-icon-light">
                                <svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="3" width="20" height="14" rx="2" ry="2"></rect><line x1="8" y1="21" x2="16" y2="21"></line><line x1="12" y1="17" x2="12" y2="21"></line></svg>
                            </div>
                            <span class="bento-tag bento-tag-green">Core Web Vitals 95+</span>
                            <h3 class="bento-title">Custom High-Speed WordPress Solutions</h3>
                            <p class="bento-desc">
                                Bespoke WordPress themes, streamlined CSS architectures, optimized database queries, and caching configurations engineered to pass Google Core Web Vitals with flawless efficiency.
                            </p>
                        </div>
                        <div>
                            <a href="wordpress-design-services" class="bento-link">
                                View WordPress Architecture
                                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
                            </a>
                        </div>
                    </div>

                    <!-- Visa Consultancy Portals (Span 3) -->
                    <div class="bento-card fade-up delay-100" style="grid-column: span 3; background: #ffffff;">
                        <div>
                            <div class="bento-icon-box bento-icon-light">
                                <svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" y1="13" x2="8" y2="13"></line><line x1="16" y1="17" x2="8" y2="17"></line></svg>
                            </div>
                            <span class="bento-tag bento-tag-green">Lead Funnels</span>
                            <h3 class="bento-title">Visa Portals</h3>
                            <p class="bento-desc">
                                High-trust application portals with interactive eligibility calculators and inquiry funnels.
                            </p>
                        </div>
                        <div>
                            <a href="wordpress-design-services-for-visa-consultancy" class="bento-link">
                                Visa Sites
                                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
                            </a>
                        </div>
                    </div>

                    <!-- Education Platforms (Span 3) -->
                    <div class="bento-card fade-up delay-200" style="grid-column: span 3; background: #ffffff;">
                        <div>
                            <div class="bento-icon-box bento-icon-light">
                                <svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 10v6M2 10l10-5 10 5-10 5z"></path><path d="M6 12v5c3 3 9 3 12 0v-5"></path></svg>
                            </div>
                            <span class="bento-tag bento-tag-green">Academic LMS</span>
                            <h3 class="bento-title">Education Portals</h3>
                            <p class="bento-desc">
                                Fast course catalogs, teacher directories, and admission portals for academies and colleges.
                            </p>
                        </div>
                        <div>
                            <a href="wordpress-design-services-for-education" class="bento-link">
                                Education Sites
                                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
                            </a>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- 5. Data Proof: Case Studies Showcase -->
        <section class="py-120" style="background: #ffffff;">
            <div class="container">
                <div class="section-header-modern fade-up">
                    <span class="section-eyebrow">Verified Evidence</span>
                    <h2 class="section-heading-lg">Data Over Promises: Live Case Studies</h2>
                    <p class="section-subtext">
                        Explore real Google Search Console organic growth curves, keyword ranking improvements, and revenue increases delivered for our clients.
                    </p>
                </div>

                <div class="case-studies-grid">
                    <!-- Case Study 1 -->
                    <div class="case-card-modern fade-up">
                        <div class="case-card-img-wrap">
                            <img src="images/Euro Immigration Consutlancy Pakistan.webp" alt="Euro Immigration Consultancy SEO Growth Case Study">
                        </div>
                        <div class="case-card-body">
                            <span class="case-pill">Immigration Consultancy</span>
                            <h3 class="case-card-title">Euro Immigration: 380% Increase in Qualified Visa Inquiries</h3>
                            <p style="font-size: 0.9rem; color: #64748b; line-height: 1.6;">
                                Restructured core service silos, resolved deep indexation issues, and secured top-3 rankings across Pakistan for high-ticket study and immigration terms.
                            </p>
                            <div class="case-stat-box">
                                <div>
                                    <div class="case-stat-val">+380%</div>
                                    <div class="case-stat-label">Inquiry Growth</div>
                                </div>
                                <div>
                                    <div class="case-stat-val">#1-3</div>
                                    <div class="case-stat-label">Top Rankings</div>
                                </div>
                            </div>
                        </div>
                    </div>

                    <!-- Case Study 2 -->
                    <div class="case-card-modern fade-up delay-100">
                        <div class="case-card-img-wrap">
                            <img src="images/KIMS.webp" alt="KIMS Academic Platform SEO Case Study">
                        </div>
                        <div class="case-card-body">
                            <span class="case-pill">Education & Academy</span>
                            <h3 class="case-card-title">KIMS Academy: 240% Lift in Student Enrollments</h3>
                            <p style="font-size: 0.9rem; color: #64748b; line-height: 1.6;">
                                Built high-authority course hubs, fixed mobile Core Web Vitals, and captured high-intent academic search queries directly from competitors.
                            </p>
                            <div class="case-stat-box">
                                <div>
                                    <div class="case-stat-val">+240%</div>
                                    <div class="case-stat-label">Enrollment Lift</div>
                                </div>
                                <div>
                                    <div class="case-stat-val">99/100</div>
                                    <div class="case-stat-label">Mobile Speed</div>
                                </div>
                            </div>
                        </div>
                    </div>

                    <!-- Case Study 3 -->
                    <div class="case-card-modern fade-up delay-200">
                        <div class="case-card-img-wrap">
                            <img src="images/seo_strategy_growth_dashboard.webp" alt="GSC Organic Traffic Growth Case Study">
                        </div>
                        <div class="case-card-body">
                            <span class="case-pill">National Growth</span>
                            <h3 class="case-card-title">Local Brands: +410% Organic Revenue Lift</h3>
                            <p style="font-size: 0.9rem; color: #64748b; line-height: 1.6;">
                                Comprehensive technical clean-up, schema implementation, and intent-targeted content scaling that converted organic traffic into repeat business.
                            </p>
                            <div class="case-stat-box">
                                <div>
                                    <div class="case-stat-val">+410%</div>
                                    <div class="case-stat-label">Traffic Lift</div>
                                </div>
                                <div>
                                    <div class="case-stat-val">0</div>
                                    <div class="case-stat-label">Penalties</div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>

                <div class="text-center" style="margin-top: 48px;">
                    <a href="portfolio" class="btn btn-secondary" style="padding: 14px 32px; font-weight: 700;">
                        Explore All 12+ Detailed Case Studies &rarr;
                    </a>
                </div>
            </div>
        </section>

        <!-- 6. Scientific 4-Step SEO Process -->
        <section class="py-120" style="background: #f8fafc; border-top: 1px solid #e2e8f0;">
            <div class="container">
                <div class="section-header-modern fade-up">
                    <span class="section-eyebrow">Methodology</span>
                    <h2 class="section-heading-lg">The 4-Step Scientific SEO Framework</h2>
                    <p class="section-subtext">
                        A rigorous, predictable framework built to systematically identify bottlenecks, build undeniable topical relevance, and capture durable search rankings.
                    </p>
                </div>

                <div class="process-steps-grid">
                    <div class="process-step-card fade-up">
                        <div class="step-num-badge">01</div>
                        <h3 class="step-card-title">Deep Technical Audit</h3>
                        <p class="step-card-desc">
                            We analyze server logs, crawl budget wastage, indexation barriers, canonical errors, and Core Web Vitals to establish a pristine technical baseline.
                        </p>
                    </div>

                    <div class="process-step-card fade-up delay-100">
                        <div class="step-num-badge">02</div>
                        <h3 class="step-card-title">Search Intent Architecture</h3>
                        <p class="step-card-desc">
                            We map out buyer journeys, group keywords into commercial topic clusters, and restructure site navigation for effortless Google bot crawling.
                        </p>
                    </div>

                    <div class="process-step-card fade-up delay-200">
                        <div class="step-num-badge">03</div>
                        <h3 class="step-card-title">White-Hat Execution</h3>
                        <p class="step-card-desc">
                            Publishing authoritative content hubs, embedding rich JSON-LD schemas, tuning on-page relevance, and acquiring genuine high-trust editorial backlinks.
                        </p>
                    </div>

                    <div class="process-step-card fade-up delay-300">
                        <div class="step-num-badge">04</div>
                        <h3 class="step-card-title">Revenue Scaling</h3>
                        <p class="step-card-desc">
                            Continuous A/B testing of conversion triggers, tracking Google Search Console movements, algorithm defense, and scaling customer inquiry volume.
                        </p>
                    </div>
                </div>
            </div>
        </section>

        <!-- 7. Meet Your Consultant: Ibrar Ahmad -->
        <section class="py-120" style="background: #ffffff;">
            <div class="container">
                <div class="bio-section-box fade-up">
                    <div class="bio-photo-card">
                        <img src="images/Ibrar Ahmad.png" alt="Ibrar Ahmad SEO Expert and WordPress Developer">
                    </div>
                    <div>
                        <span style="background: rgba(140, 198, 63, 0.15); border: 1px solid rgba(140, 198, 63, 0.35); color: var(--brand-green); font-size: 0.75rem; font-weight: 800; padding: 6px 14px; border-radius: 999px; text-transform: uppercase; letter-spacing: 0.5px; display: inline-block; margin-bottom: 20px;">
                            Verified Consultant Profile
                        </span>
                        <h2 style="font-size: 2.75rem; font-weight: 900; line-height: 1.15; color: #ffffff; letter-spacing: -0.03em; margin-bottom: 20px;">
                            Work Directly with Ibrar Ahmad
                        </h2>
                        <p style="font-size: 1.05rem; line-height: 1.7; color: #cbd5e1; margin-bottom: 20px;">
                            Unlike bloated marketing agencies that pass your project to inexperienced interns, working with <strong>SEO with Ibrar</strong> means you communicate directly with a Senior Technical SEO Consultant and WordPress Engineer with 7+ years of hands-on experience.
                        </p>
                        <p style="font-size: 1rem; line-height: 1.7; color: #94a3b8; margin-bottom: 32px;">
                            Based in Lahore, Pakistan, I provide transparent, weekly communication channels, custom analytics dashboards, and proven white-hat methodologies that protect your business against Google algorithm updates.
                        </p>
                        
                        <div style="display: flex; gap: 16px; flex-wrap: wrap; align-items: center;">
                            <a href="https://pk.linkedin.com/in/seowithibrar" target="_blank" rel="noopener noreferrer" style="background: #0077b5; color: #ffffff; padding: 12px 24px; border-radius: 10px; font-weight: 800; font-size: 0.9rem; text-decoration: none; display: inline-flex; align-items: center; gap: 8px;">
                                <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M19 3a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h14m-.5 15.5v-5.3a3.26 3.26 0 0 0-3.26-3.26c-.85 0-1.84.52-2.28 1.3v-1.11h-2.79v8.37h2.79v-4.93c0-.77.62-1.4 1.39-1.4a1.4 1.4 0 0 1 1.4 1.4v4.93h2.75M6.46 10.9v8.37H9.25V10.9H6.46M7.86 6.78a1.62 1.62 0 1 0 0 3.24 1.62 1.62 0 0 0 0-3.24z"/></svg>
                                Connect on LinkedIn
                            </a>
                            <a href="contact" class="btn-agency-primary" style="padding: 12px 24px; font-size: 0.9rem;">
                                Book Free Consultation Call
                            </a>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- 8. Interactive FAQ Accordion -->
        <section class="py-120" style="background: #f8fafc; border-top: 1px solid #e2e8f0;">
            <div class="container">
                <div class="section-header-modern fade-up">
                    <span class="section-eyebrow">Clear Answers</span>
                    <h2 class="section-heading-lg">Frequently Asked Questions</h2>
                    <p class="section-subtext">
                        Honest answers about deliverables, timelines, guarantees, and working procedures.
                    </p>
                </div>

                <div class="faq-accordion-box fade-up">
                    <div class="faq-card-item">
                        <details>
                            <summary>How long does it typically take to see measurable SEO results?</summary>
                            <div class="faq-answer-inner">
                                For most established websites, early ranking improvements and click growth appear within 60 to 90 days following our technical crawl fixes and intent architecture updates. Competitive commercial terms typically mature into top 3 positions within 4 to 6 months of continuous optimization.
                            </div>
                        </details>
                    </div>

                    <div class="faq-card-item">
                        <details>
                            <summary>Why do you combine Technical SEO with WordPress Development?</summary>
                            <div class="faq-answer-inner">
                                SEO and web development are deeply intertwined. If a website is built on bloated code, slow plugins, or improper DOM structures, even the best SEO strategy will fail Google Core Web Vitals. By optimizing both code architecture and organic keyword strategy together, we achieve faster indexing and dramatically higher conversion rates.
                            </div>
                        </details>
                    </div>

                    <div class="faq-card-item">
                        <details>
                            <summary>Do you use 100% white-hat SEO techniques?</summary>
                            <div class="faq-answer-inner">
                                Yes. Every tactic adheres strictly to Google Webmaster Guidelines. We never use automated link spam, PBNs, or low-quality scraped content. Our strategies are built to withstand algorithm updates and build long-term business equity.
                            </div>
                        </details>
                    </div>

                    <div class="faq-card-item">
                        <details>
                            <summary>How do we get started with an SEO audit?</summary>
                            <div class="faq-answer-inner">
                                Simply fill out our contact form or send a WhatsApp message. We will review your current website performance, identify your core keyword targets, and schedule a 20-minute strategic consultation call.
                            </div>
                        </details>
                    </div>
                </div>
            </div>
        </section>

        <!-- 9. Final High-Impact CTA Banner (Dark Obsidian Glassmorphism) -->
        <section class="cta-banner" style="background: radial-gradient(circle at 50% 0%, rgba(140, 198, 63, 0.15) 0%, transparent 60%), linear-gradient(145deg, #070c18 0%, #0d1527 100%); padding: 6.5rem 0; position: relative; overflow: hidden; border-top: 1px solid rgba(255,255,255,0.08);">
            <div class="container text-center" style="max-width: 860px; position: relative; z-index: 10;">
                <span style="background: rgba(140, 198, 63, 0.15); border: 1px solid rgba(140, 198, 63, 0.35); color: var(--brand-green); padding: 0.5rem 1.25rem; border-radius: 30px; font-size: 0.82rem; font-weight: 800; display: inline-block; margin-bottom: 1.5rem; letter-spacing: 0.5px; text-transform: uppercase;">
                    🚀 Start Scaling Your Organic Revenue
                </span>
                <h2 class="cta-title" style="color: #ffffff; font-size: 2.85rem; font-weight: 900; line-height: 1.15; margin-bottom: 1.25rem; letter-spacing: -0.03em;">
                    Ready to Outrank Competitors & Capture Real Business Leads?
                </h2>
                <p class="cta-desc" style="color: #cbd5e1; font-size: 1.1rem; line-height: 1.7; margin-bottom: 1.25rem;">
                    Don't let valuable clients click on competitors. Book your free technical SEO consultation today. We will audit your current website, pinpoint growth bottlenecks, and chart out a clear roadmap to Google dominance.
                </p>
                <p class="cta-desc" style="color: #94a3b8; font-size: 1rem; line-height: 1.7; margin-bottom: 2.5rem; font-weight: 600;">
                    Direct 1-on-1 consultation with Ibrar Ahmad. No sales pressure, just actionable strategy.
                </p>

                <div style="display: flex; gap: 1rem; justify-content: center; align-items: center; flex-wrap: wrap;">
                    <a href="contact" class="btn-agency-primary" style="padding: 16px 36px;">
                        Get Free SEO Audit & Consultation
                    </a>
                    <a href="https://wa.me/923174835008" target="_blank" rel="noopener noreferrer" class="btn" style="background: #25D366; color: #ffffff; padding: 16px 32px; font-size: 1.05rem; font-weight: 700; border: none; border-radius: 12px; display: inline-flex; align-items: center; gap: 0.5rem; box-shadow: 0 10px 25px rgba(37,211,102,0.25);">
                        <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor"><path d="M.057 24l1.687-6.163c-1.041-1.804-1.588-3.849-1.587-5.946.003-6.556 5.338-11.891 11.893-11.891 3.181.001 6.167 1.24 8.413 3.488 2.245 2.248 3.481 5.236 3.48 8.414-.003 6.557-5.338 11.892-11.893 11.892-1.99-.001-3.951-.5-5.688-1.448l-6.305 1.654zm6.597-3.807c1.676.995 3.276 1.591 5.392 1.592 5.448 0 9.886-4.434 9.889-9.885.002-5.462-4.415-9.89-9.881-9.892-5.452 0-9.887 4.434-9.889 9.884-.001 2.225.651 3.891 1.746 5.634l-.999 3.648 3.742-.981zm11.387-5.464c-.074-.124-.272-.198-.57-.347-.297-.149-1.758-.868-2.031-.967-.272-.099-.47-.149-.669.149-.198.297-.768.967-.941 1.165-.173.198-.347.223-.644.074-.297-.149-1.255-.462-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.297-.347.446-.521.151-.172.2-.296.3-.495.099-.198.05-.372-.025-.521-.075-.148-.669-1.611-.916-2.206-.242-.579-.487-.501-.669-.51l-.57-.01c-.198 0-.52.074-.792.372s-1.04 1.016-1.04 2.479 1.065 2.876 1.213 3.074c.149.198 2.095 3.2 5.076 4.487.709.306 1.263.489 1.694.626.712.226 1.36.194 1.872.118.571-.085 1.758-.719 2.006-1.413.248-.695.248-1.29.173-1.414z"/></svg>
                        WhatsApp Instant Chat
                    </a>
                </div>
            </div>
        </section>
    </main>"""

# 3. Replace <style>...</style> in <head>
old_style_match = re.search(r'<style>.*?</style>', content, re.DOTALL)
if old_style_match:
    content = content[:old_style_match.start()] + css_block + content[old_style_match.end():]
else:
    head_end = content.find('</head>')
    content = content[:head_end] + css_block + '\n' + content[head_end:]

# 4. Replace <main>...</main>
main_start = content.find('<main>')
main_end = content.find('</main>') + len('</main>')

new_content = content[:main_start] + modern_main + content[main_end:]

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("index.html modern redesign written successfully!")
