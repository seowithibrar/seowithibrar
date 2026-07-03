import re

# Read the current CSS
with open('css/styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

# The massive UI/UX modernization CSS to append
modernization_css = """

/* ==========================================================================
   UI/UX MODERNIZATION OVERHAUL — July 2026
   All styles below enhance existing components without breaking anything.
   ========================================================================== */

/* ---------- Phase 1: Enhanced Design Tokens ---------- */
:root {
    /* Glow & Glass Tokens */
    --glow-primary: 0 0 30px rgba(140, 198, 63, 0.3), 0 0 60px rgba(140, 198, 63, 0.1);
    --glow-primary-intense: 0 0 40px rgba(140, 198, 63, 0.5), 0 0 80px rgba(140, 198, 63, 0.15);
    --glass-bg: rgba(255, 255, 255, 0.03);
    --glass-bg-light: rgba(255, 255, 255, 0.06);
    --glass-border: rgba(255, 255, 255, 0.08);
    --glass-border-hover: rgba(255, 255, 255, 0.18);

    /* Gradient Tokens */
    --gradient-hero: linear-gradient(135deg, #0a0a0a 0%, #111827 40%, #0f172a 100%);
    --gradient-card-border: linear-gradient(135deg, rgba(140, 198, 63, 0.4), rgba(140, 198, 63, 0.05));
    --gradient-text: linear-gradient(135deg, #ffffff 0%, rgba(255,255,255,0.7) 100%);

    /* Animation Tokens */
    --ease-premium: cubic-bezier(0.25, 0.46, 0.45, 0.94);
    --ease-bounce: cubic-bezier(0.34, 1.56, 0.64, 1);
    --transition-premium: all 0.4s var(--ease-premium);
}

/* ---------- Phase 2: Premium Animations ---------- */

@keyframes fadeInUp {
    from {
        opacity: 0;
        transform: translateY(30px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

@keyframes fadeInLeft {
    from {
        opacity: 0;
        transform: translateX(-30px);
    }
    to {
        opacity: 1;
        transform: translateX(0);
    }
}

@keyframes fadeInRight {
    from {
        opacity: 0;
        transform: translateX(30px);
    }
    to {
        opacity: 1;
        transform: translateX(0);
    }
}

@keyframes scaleIn {
    from {
        opacity: 0;
        transform: scale(0.9);
    }
    to {
        opacity: 1;
        transform: scale(1);
    }
}

@keyframes shimmer {
    0% { background-position: -200% center; }
    100% { background-position: 200% center; }
}

@keyframes pulseGlow {
    0%, 100% { box-shadow: var(--glow-primary); }
    50% { box-shadow: var(--glow-primary-intense); }
}

@keyframes gradientShift {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

@keyframes subtleFloat {
    0%, 100% { transform: translateY(0px); }
    50% { transform: translateY(-8px); }
}

@keyframes borderGlow {
    0%, 100% { border-color: rgba(140, 198, 63, 0.2); }
    50% { border-color: rgba(140, 198, 63, 0.6); }
}

/* Noise texture overlay for premium depth */
body::after {
    content: '';
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    pointer-events: none;
    z-index: 9999;
    opacity: 0.015;
    background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 256 256' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noise'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noise)'/%3E%3C/svg%3E");
}

/* ---------- Phase 2: Enhanced Buttons ---------- */

.btn-primary {
    background: linear-gradient(135deg, #8cc63f 0%, #7ab332 50%, #8cc63f 100%);
    background-size: 200% auto;
    position: relative;
    overflow: hidden;
    transition: var(--transition-premium);
}

.btn-primary::before {
    content: '';
    position: absolute;
    top: 0;
    left: -100%;
    width: 100%;
    height: 100%;
    background: linear-gradient(90deg, transparent, rgba(255,255,255,0.2), transparent);
    transition: left 0.5s ease;
}

.btn-primary:hover {
    transform: translateY(-3px);
    box-shadow: var(--glow-primary-intense);
    background-position: right center;
}

.btn-primary:hover::before {
    left: 100%;
}

.btn-primary:active {
    transform: translateY(-1px);
}

/* CTA Button Pulse */
.nav-cta {
    animation: pulseGlow 3s ease-in-out infinite;
}

.nav-cta:hover {
    animation: none;
    box-shadow: var(--glow-primary-intense);
}

/* ---------- Phase 2: Enhanced Cards ---------- */

.service-card {
    position: relative;
    overflow: hidden;
    transition: var(--transition-premium);
}

.service-card::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    width: 3px;
    height: 0;
    background: linear-gradient(180deg, var(--color-primary), transparent);
    transition: height 0.4s var(--ease-premium);
}

.service-card:hover::before {
    height: 100%;
}

.service-card:hover {
    transform: translateY(-8px);
    box-shadow: 0 20px 40px rgba(0, 0, 0, 0.1), 0 0 0 1px rgba(140, 198, 63, 0.2);
}

.service-icon {
    transition: var(--transition-premium);
}

.service-card:hover .service-icon {
    background-color: var(--color-primary);
    color: white;
    transform: scale(1.1) rotate(5deg);
}

/* Glass Card Enhancement */
.glass-card {
    transition: var(--transition-premium);
}

.glass-card:hover {
    transform: translateY(-8px);
    border-color: rgba(140, 198, 63, 0.3);
    box-shadow: 0 20px 50px rgba(0, 0, 0, 0.3), var(--glow-primary);
}

/* Process Card Enhancement */
.process-card {
    transition: var(--transition-premium);
}

.process-card::before {
    content: '';
    position: absolute;
    bottom: 0;
    left: 0;
    width: 0;
    height: 3px;
    background: var(--color-primary);
    transition: width 0.4s var(--ease-premium);
}

.process-card:hover::before {
    width: 100%;
}

.process-card:hover {
    transform: translateY(-8px);
    box-shadow: 0 20px 40px rgba(0, 0, 0, 0.08);
    border-color: rgba(140, 198, 63, 0.3);
}

/* WP Feature Card Enhancement */
.wp-feature-card {
    transition: var(--transition-premium);
    position: relative;
    overflow: hidden;
}

.wp-feature-card::after {
    content: '';
    position: absolute;
    top: -50%;
    left: -50%;
    width: 200%;
    height: 200%;
    background: radial-gradient(circle, rgba(140, 198, 63, 0.05) 0%, transparent 70%);
    opacity: 0;
    transition: opacity 0.4s ease;
}

.wp-feature-card:hover::after {
    opacity: 1;
}

/* ---------- Phase 3: Hero Section Dark Upgrade ---------- */

.hero {
    background: var(--gradient-hero) !important;
    position: relative;
    overflow: hidden;
}

.hero::before {
    background-image:
        linear-gradient(rgba(140, 198, 63, 0.03) 1px, transparent 1px),
        linear-gradient(90deg, rgba(140, 198, 63, 0.03) 1px, transparent 1px) !important;
    background-size: 60px 60px !important;
}

/* Glow orb behind hero */
.hero::after {
    content: '';
    position: absolute;
    top: 20%;
    right: 15%;
    width: 500px;
    height: 500px;
    background: radial-gradient(circle, rgba(140, 198, 63, 0.12) 0%, transparent 70%);
    border-radius: 50%;
    filter: blur(60px);
    z-index: 0;
    animation: subtleFloat 8s ease-in-out infinite;
}

.hero > * {
    position: relative;
    z-index: 1;
}

.hero-title {
    color: var(--color-white) !important;
    animation: fadeInUp 0.8s var(--ease-premium) both;
}

.hero-description {
    color: rgba(255, 255, 255, 0.6) !important;
    animation: fadeInUp 0.8s var(--ease-premium) 0.2s both;
}

.hero-actions {
    animation: fadeInUp 0.8s var(--ease-premium) 0.4s both;
}

.client-rating {
    animation: fadeInUp 0.8s var(--ease-premium) 0.6s both;
}

.pill-badge {
    animation: fadeInUp 0.8s var(--ease-premium) both;
}

.hero-visual {
    animation: fadeInRight 1s var(--ease-premium) 0.3s both;
}

.rating-text {
    color: rgba(255, 255, 255, 0.6) !important;
}

.stars {
    color: #fbbc05 !important;
}

/* Floating Cards — Premium glass effect in dark hero */
.floating-card {
    background: rgba(255, 255, 255, 0.08) !important;
    backdrop-filter: blur(16px) !important;
    -webkit-backdrop-filter: blur(16px) !important;
    border: 1px solid rgba(255, 255, 255, 0.1) !important;
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3) !important;
    transition: var(--transition-premium);
}

.floating-card:hover {
    border-color: rgba(140, 198, 63, 0.3) !important;
    box-shadow: 0 12px 40px rgba(0, 0, 0, 0.4), var(--glow-primary) !important;
}

.card-number {
    color: var(--color-white) !important;
}

.card-label {
    color: rgba(255, 255, 255, 0.6) !important;
}

.bg-shape-green {
    background-color: rgba(140, 198, 63, 0.08) !important;
    filter: blur(80px) !important;
    width: 550px !important;
    height: 550px !important;
}

.main-portrait {
    box-shadow: 0 25px 60px rgba(0, 0, 0, 0.5) !important;
    border: 2px solid rgba(255, 255, 255, 0.05);
}

/* Chart card specific */
.chart-title {
    color: rgba(255, 255, 255, 0.8);
}

/* ---------- Phase 3: Trusted By Section ---------- */

.trusted-by {
    background-color: #0a0a0a !important;
    border-bottom: 1px solid rgba(255, 255, 255, 0.05) !important;
    padding: 4rem 0 !important;
}

.section-subtitle {
    color: rgba(255, 255, 255, 0.4) !important;
}

.tool-logo {
    color: rgba(255, 255, 255, 0.35) !important;
    transition: var(--transition-premium);
    cursor: default;
}

.tool-logo:hover {
    color: var(--color-primary) !important;
    transform: scale(1.05);
}

/* ---------- Phase 3: About Section Enhancement ---------- */

.about-modern {
    background: linear-gradient(180deg, #fafdf7 0%, var(--color-white) 100%) !important;
}

/* ---------- Phase 3: Services Section Enhancement ---------- */

.services {
    background: linear-gradient(180deg, var(--color-bg-light) 0%, #f0f5eb 100%) !important;
    position: relative;
}

/* ---------- Phase 3: Why Choose Me Enhancement ---------- */

.why-box {
    background: linear-gradient(135deg, #111827 0%, #0f172a 100%) !important;
    border: 1px solid rgba(255, 255, 255, 0.05);
    position: relative;
    overflow: hidden;
}

.why-box::before {
    content: '';
    position: absolute;
    top: -50%;
    right: -30%;
    width: 600px;
    height: 600px;
    background: radial-gradient(circle, rgba(140, 198, 63, 0.08) 0%, transparent 70%);
    border-radius: 50%;
    pointer-events: none;
}

.check-icon {
    transition: var(--transition-premium);
}

.check-item:hover .check-icon {
    transform: scale(1.15);
    box-shadow: 0 0 15px rgba(140, 198, 63, 0.4);
}

/* ---------- Phase 3: CTA Banner Enhancement ---------- */

.cta-box {
    position: relative;
    overflow: hidden;
    background: linear-gradient(135deg, #8cc63f 0%, #6fa830 100%) !important;
}

.cta-box::before {
    content: '';
    position: absolute;
    top: -50%;
    right: -20%;
    width: 400px;
    height: 400px;
    background: radial-gradient(circle, rgba(255,255,255,0.15) 0%, transparent 70%);
    border-radius: 50%;
}

/* ---------- Phase 3: Blog Cards Enhancement ---------- */

.dark-blog-card {
    transition: var(--transition-premium);
}

.dark-blog-card:hover {
    transform: translateY(-8px);
}

.dark-blog-image img {
    transition: transform 0.6s var(--ease-premium) !important;
}

.dark-blog-card:hover .dark-blog-image img {
    transform: scale(1.08);
}

/* ---------- Phase 3: FAQ Enhancement ---------- */

.faq-accordion details {
    transition: var(--transition-premium);
}

.faq-accordion details:hover {
    border-color: rgba(140, 198, 63, 0.3);
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.05);
}

.faq-accordion details[open] {
    border-color: var(--color-primary);
    box-shadow: 0 4px 20px rgba(140, 198, 63, 0.1);
}

.faq-accordion summary {
    transition: color 0.3s ease;
}

.faq-accordion details[open] summary {
    color: var(--color-primary);
}

/* ---------- Phase 3: Score Circle Enhancement ---------- */

.score-circle {
    position: relative;
    transition: var(--transition-premium);
}

.score-circle:hover {
    box-shadow: var(--glow-primary);
    transform: scale(1.05);
}

/* ---------- Phase 3: Terminal Window Enhancement ---------- */

.terminal-window {
    transition: var(--transition-premium);
}

.terminal-window:hover {
    box-shadow: 0 30px 60px -12px rgba(0, 0, 0, 0.6), 0 0 0 1px rgba(140, 198, 63, 0.1);
    transform: translateY(-4px);
}

/* ---------- Phase 3: Blog Post Reading Enhancement ---------- */

.blog-hero-title {
    animation: fadeInUp 0.6s var(--ease-premium) both;
}

.blog-body {
    font-size: 1.1rem;
    line-height: 1.85;
}

.blog-body h2 {
    position: relative;
    padding-left: 1rem;
}

.blog-body h2::before {
    content: '';
    position: absolute;
    left: 0;
    top: 0;
    bottom: 0;
    width: 3px;
    background: linear-gradient(180deg, var(--color-primary), transparent);
    border-radius: 2px;
}

.blog-body blockquote {
    border-left: 3px solid var(--color-primary);
    padding: 1.5rem 2rem;
    background: rgba(140, 198, 63, 0.05);
    border-radius: 0 12px 12px 0;
    margin: 2rem 0;
    font-style: italic;
}

/* ---------- Phase 4: Footer Premium Upgrade ---------- */

.footer, .footer.new-mega-footer {
    position: relative;
}

.footer::before, .footer.new-mega-footer::before {
    content: '';
    position: absolute;
    top: 0;
    left: 5%;
    right: 5%;
    height: 1px;
    background: linear-gradient(90deg, transparent, var(--color-primary), transparent);
    opacity: 0.5;
}

.footer-links a {
    position: relative;
    display: inline-block;
    transition: var(--transition-premium);
}

.footer-links a::after {
    content: '';
    position: absolute;
    bottom: -2px;
    left: 0;
    width: 0;
    height: 1px;
    background: var(--color-primary);
    transition: width 0.3s var(--ease-premium);
}

.footer-links a:hover {
    color: var(--color-primary) !important;
    transform: translateX(4px);
}

.footer-links a:hover::after {
    width: 100%;
}

.social-link {
    transition: var(--transition-premium);
}

.social-link:hover {
    transform: translateY(-3px);
    box-shadow: 0 4px 15px rgba(140, 198, 63, 0.3);
}

.newsletter-input {
    transition: var(--transition-premium);
}

.newsletter-input:focus {
    box-shadow: 0 0 0 2px rgba(140, 198, 63, 0.3);
}

.newsletter-btn {
    transition: var(--transition-premium);
}

.newsletter-btn:hover {
    transform: scale(1.05);
    box-shadow: 0 0 15px rgba(140, 198, 63, 0.4);
}

/* ---------- Phase 4: Mega Menu Enhancement ---------- */

.mega-menu {
    transition: all 0.35s var(--ease-premium) !important;
}

.mega-item {
    transition: var(--transition-premium);
    border-radius: 8px;
    padding: 0.5rem !important;
}

.mega-item:hover {
    background: rgba(140, 198, 63, 0.05);
    transform: translateX(4px);
}

.mega-item-dot {
    transition: var(--transition-premium);
}

.mega-item:hover .mega-item-dot {
    background: var(--color-primary);
    box-shadow: 0 0 8px rgba(140, 198, 63, 0.5);
}

/* ---------- Phase 5: Mobile Experience Polish ---------- */

@media (max-width: 992px) {
    /* Ensure dark hero text is readable */
    .hero-title {
        font-size: 2.8rem !important;
    }

    /* Better touch targets */
    .btn {
        min-height: 48px;
        min-width: 48px;
    }

    .nav-link {
        min-height: 44px;
        display: flex;
        align-items: center;
    }

    /* Better card spacing on tablet */
    .service-card {
        padding: 2rem;
    }
}

@media (max-width: 768px) {
    .hero {
        padding: 5rem 0 4rem !important;
    }

    .hero-title {
        font-size: 2.2rem !important;
    }

    /* Floating cards smaller on mobile */
    .floating-card {
        padding: 0.75rem !important;
        border-radius: 10px !important;
    }

    .card-number {
        font-size: 1.2rem !important;
    }

    .card-label {
        font-size: 0.7rem !important;
    }

    /* Section titles */
    .section-title {
        font-size: 1.8rem !important;
    }

    /* Better stats banner on mobile */
    .stat-number {
        font-size: 2rem;
    }

    /* Full-width buttons on small screens */
    .hero-actions .btn {
        width: 100%;
        justify-content: center;
    }
}

@media (max-width: 480px) {
    .hero-title {
        font-size: 1.8rem !important;
    }

    .hero {
        padding: 4rem 0 3rem !important;
    }

    /* Stack everything */
    .cta-box {
        padding: 2rem 1.5rem !important;
    }

    .cta-title {
        font-size: 1.5rem;
    }

    .why-box {
        padding: 2rem 1.25rem !important;
    }
}

/* ---------- Scrollbar Styling ---------- */
::-webkit-scrollbar {
    width: 8px;
}

::-webkit-scrollbar-track {
    background: #111;
}

::-webkit-scrollbar-thumb {
    background: rgba(140, 198, 63, 0.3);
    border-radius: 10px;
}

::-webkit-scrollbar-thumb:hover {
    background: rgba(140, 198, 63, 0.6);
}

/* ---------- Selection Highlight ---------- */
::selection {
    background: rgba(140, 198, 63, 0.3);
    color: white;
}

::-moz-selection {
    background: rgba(140, 198, 63, 0.3);
    color: white;
}

/* ---------- Smooth Page Transitions ---------- */
html {
    scroll-behavior: smooth;
}

/* Focus States for Accessibility */
*:focus-visible {
    outline: 2px solid var(--color-primary);
    outline-offset: 3px;
    border-radius: 4px;
}

/* Form Input Enhancements */
input[type="text"],
input[type="email"],
input[type="tel"],
input[type="url"],
textarea,
select {
    transition: var(--transition-premium);
}

input[type="text"]:focus,
input[type="email"]:focus,
input[type="tel"]:focus,
input[type="url"]:focus,
textarea:focus,
select:focus {
    border-color: var(--color-primary) !important;
    box-shadow: 0 0 0 3px rgba(140, 198, 63, 0.15), 0 0 20px rgba(140, 198, 63, 0.08) !important;
}

/* ---------- Link hover effects globally ---------- */
a {
    transition: var(--transition-premium);
}

/* ---------- Image hover zoom for any card ---------- */
.dark-blog-image,
.white-image-card .card-img-placeholder {
    overflow: hidden;
}

/* ---------- Slider enhancements ---------- */
.slider-container,
.wp-slider-container {
    transition: var(--transition-premium);
}

.slider-container:hover,
.wp-slider-container:hover {
    box-shadow: 0 25px 50px rgba(0, 0, 0, 0.5);
}

/* Active dot animation */
.dot.active {
    animation: pulseGlow 2s ease-in-out infinite;
    box-shadow: 0 0 10px rgba(140, 198, 63, 0.5);
}

/* ---------- Device Mockup enhancements ---------- */
.device-desktop {
    transition: var(--transition-premium);
}

.device-desktop:hover {
    box-shadow: 0 25px 60px rgba(0, 0, 0, 0.7), 0 0 0 1px rgba(140, 198, 63, 0.15);
}

.device-mobile {
    transition: var(--transition-premium);
}

.device-mobile:hover {
    box-shadow: 0 25px 60px rgba(0, 0, 0, 0.7), 0 0 0 1px rgba(140, 198, 63, 0.15);
}

/* Device screen scroll-on-hover enhancement */
.device-desktop-screen:hover img {
    transform: translateY(-5%) !important;
    transition: transform 3s ease !important;
}

.device-mobile-screen:hover img {
    transform: translateY(-8%) !important;
    transition: transform 4s ease !important;
}

/* ---------- Print Styles ---------- */
@media print {
    .navbar, .footer, .floating-card, body::after {
        display: none !important;
    }

    .hero {
        background: white !important;
    }

    .hero-title, .section-title {
        color: black !important;
    }
}
"""

# Append to existing CSS
with open('css/styles.css', 'a', encoding='utf-8') as f:
    f.write(modernization_css)

print("Successfully appended UI/UX modernization CSS!")
print(f"Original CSS: {len(css)} characters")
print(f"Added CSS: {len(modernization_css)} characters")
print(f"Total CSS: {len(css) + len(modernization_css)} characters")
