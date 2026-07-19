const fs = require('fs');
let css = fs.readFileSync('c:/Users/mitec/OneDrive/Documents/GitHub/SEO WITH Ibrar/frontend/src/app/globals.css', 'utf8');

// Replace color tokens
css = css.replace(/--color-primary:\s*#10b981;/g, '--color-primary: #16C784;');
css = css.replace(/--color-primary-hover:\s*#059669;/g, '--color-primary-hover: #12A86D;');
css = css.replace(/--color-dark-surface:\s*#0f172a;/g, '--color-dark-surface: rgba(15, 23, 42, 0.7);');

const ultraStyles = `
/* ==========================================================================
   Ultra Modern Hero Layout
   ========================================================================== */
.hero-ultra {
    padding: 100px 0 140px;
    position: relative;
    overflow: hidden;
    background-color: #050810;
    min-height: 100vh;
    display: flex;
    align-items: center;
}

/* Background Layers */
.hero-ultra-bg {
    position: absolute;
    inset: 0;
    z-index: 0;
    pointer-events: none;
    overflow: hidden;
}

/* Grid Pattern */
.hero-ultra-bg::before {
    content: '';
    position: absolute;
    inset: 0;
    background-size: 50px 50px;
    background-image: 
      linear-gradient(to right, rgba(255, 255, 255, 0.03) 1px, transparent 1px),
      linear-gradient(to bottom, rgba(255, 255, 255, 0.03) 1px, transparent 1px);
    mask-image: radial-gradient(ellipse at center, black 40%, transparent 80%);
    -webkit-mask-image: radial-gradient(ellipse at center, black 40%, transparent 80%);
}

/* Radial Glows */
.hero-glow-1 {
    position: absolute;
    top: 20%;
    left: -10%;
    width: 600px;
    height: 600px;
    background: radial-gradient(circle, rgba(22, 199, 132, 0.15) 0%, transparent 70%);
    filter: blur(80px);
}
.hero-glow-2 {
    position: absolute;
    bottom: -10%;
    right: 10%;
    width: 800px;
    height: 800px;
    background: radial-gradient(circle, rgba(15, 23, 42, 0.8) 0%, transparent 70%);
    filter: blur(100px);
}

.hero-ultra-container {
    position: relative;
    z-index: 10;
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 4rem;
    align-items: center;
}

/* Typography & Badges */
.badge-ultra {
    display: inline-flex;
    align-items: center;
    gap: 0.5rem;
    padding: 0.5rem 1rem;
    background: rgba(255, 255, 255, 0.05);
    border: 1px solid rgba(255, 255, 255, 0.1);
    border-radius: 100px;
    font-size: 0.875rem;
    font-weight: 500;
    color: rgba(255, 255, 255, 0.8);
    margin-bottom: 2rem;
    backdrop-filter: blur(10px);
}

.title-ultra {
    font-size: 4rem;
    font-weight: 800;
    line-height: 1.1;
    margin-bottom: 1.5rem;
    letter-spacing: -0.03em;
    color: #fff;
}

.title-gradient {
    background: linear-gradient(135deg, #16C784 0%, #3b82f6 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}

.desc-ultra {
    font-size: 1.125rem;
    color: rgba(255, 255, 255, 0.7);
    line-height: 1.7;
    margin-bottom: 2rem;
    max-width: 90%;
}

/* Bullet Points */
.bullet-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 1rem;
    margin-bottom: 2.5rem;
}
.bullet-item {
    display: flex;
    align-items: center;
    gap: 0.75rem;
    font-size: 0.95rem;
    color: rgba(255, 255, 255, 0.9);
}

/* CTAs */
.cta-group {
    display: flex;
    gap: 1rem;
    align-items: center;
    margin-bottom: 3rem;
}
.btn-ultra-primary {
    background: #16C784;
    color: #050810;
    padding: 1.2rem 2.5rem;
    border-radius: 100px;
    font-weight: 700;
    font-size: 1rem;
    box-shadow: 0 10px 30px rgba(22, 199, 132, 0.3);
    border: none;
    cursor: pointer;
    transition: all 0.3s ease;
}
.btn-ultra-primary:hover {
    transform: translateY(-2px);
    box-shadow: 0 15px 40px rgba(22, 199, 132, 0.5);
    background: #12A86D;
}
.btn-ultra-secondary {
    background: rgba(255, 255, 255, 0.05);
    color: #fff;
    padding: 1.2rem 2.5rem;
    border-radius: 100px;
    font-weight: 600;
    border: 1px solid rgba(255, 255, 255, 0.1);
    transition: all 0.3s ease;
}
.btn-ultra-secondary:hover {
    background: rgba(255, 255, 255, 0.1);
    transform: translateY(-2px);
}

/* Social Proof & Metrics */
.social-proof-section {
    display: flex;
    flex-wrap: wrap;
    gap: 2rem;
    align-items: center;
}
.avatar-stack {
    display: flex;
}
.avatar-stack img {
    width: 40px;
    height: 40px;
    border-radius: 50%;
    border: 2px solid #050810;
    margin-left: -12px;
    object-fit: cover;
}
.avatar-stack img:first-child {
    margin-left: 0;
}
.rating-box {
    display: flex;
    flex-direction: column;
    gap: 0.25rem;
}
.stars {
    color: #FBBF24;
    font-size: 1.2rem;
}
.trust-text {
    font-size: 0.85rem;
    color: rgba(255, 255, 255, 0.6);
}

.mini-stats-grid {
    display: flex;
    gap: 1rem;
    margin-top: 2rem;
}
.mini-stat-card {
    background: rgba(255, 255, 255, 0.03);
    border: 1px solid rgba(255, 255, 255, 0.08);
    border-radius: 16px;
    padding: 1rem;
    display: flex;
    align-items: center;
    gap: 1rem;
    backdrop-filter: blur(10px);
}
.mini-stat-icon {
    font-size: 1.5rem;
}
.mini-stat-info h4 {
    font-size: 1.1rem;
    color: #fff;
    margin-bottom: 0.2rem;
}
.mini-stat-info p {
    font-size: 0.75rem;
    color: rgba(255, 255, 255, 0.5);
    text-transform: uppercase;
    letter-spacing: 0.5px;
}

/* Right Side Portrait Area */
.portrait-stage {
    position: relative;
    width: 100%;
    height: 600px;
    display: flex;
    justify-content: center;
    align-items: flex-end;
}
.organic-blob {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    width: 450px;
    height: 450px;
    background: linear-gradient(135deg, rgba(22, 199, 132, 0.2), rgba(59, 130, 246, 0.2));
    border-radius: 40% 60% 70% 30% / 40% 50% 60% 50%;
    animation: morph 8s ease-in-out infinite alternate;
    z-index: 0;
    filter: blur(20px);
}
@keyframes morph {
    0% { border-radius: 40% 60% 70% 30% / 40% 50% 60% 50%; }
    100% { border-radius: 60% 40% 30% 70% / 60% 30% 70% 40%; }
}
.portrait-image-full {
    position: relative;
    z-index: 10;
    height: 100%;
    object-fit: contain;
    /* user specifically requested full size */
}

/* Floating Metric Cards */
.floating-metric {
    position: absolute;
    background: rgba(15, 23, 42, 0.6);
    backdrop-filter: blur(16px);
    -webkit-backdrop-filter: blur(16px);
    border: 1px solid rgba(255, 255, 255, 0.1);
    border-radius: 20px;
    padding: 1.25rem;
    box-shadow: 0 20px 40px rgba(0, 0, 0, 0.4);
    z-index: 20;
    display: flex;
    flex-direction: column;
    gap: 0.5rem;
    animation: float 6s ease-in-out infinite;
}
.metric-label {
    font-size: 0.75rem;
    color: rgba(255, 255, 255, 0.6);
    text-transform: uppercase;
    letter-spacing: 1px;
}
.metric-value {
    font-size: 1.5rem;
    font-weight: 800;
    color: #16C784;
}
.m-top-left { top: 10%; left: -10%; animation-delay: 0s; }
.m-top-right { top: 20%; right: -5%; animation-delay: 1s; }
.m-mid-right { top: 50%; right: -15%; animation-delay: 2s; }
.m-bot-left { bottom: 15%; left: -5%; animation-delay: 3s; }
.m-bot-right { bottom: 5%; right: 5%; animation-delay: 1.5s; }

/* Floating Icons */
.floating-icon {
    position: absolute;
    color: rgba(255, 255, 255, 0.4);
    z-index: 5;
    animation: float 5s ease-in-out infinite alternate;
}

@media (max-width: 1200px) {
    .floating-metric { display: none; } /* Hide complex cards on small screens to reduce clutter */
    .hero-ultra-container { grid-template-columns: 1fr; }
    .portrait-stage { height: 400px; margin-top: 3rem; }
}
`;

if (!css.includes('Ultra Modern Hero Layout')) {
  css += '\n' + ultraStyles;
}

fs.writeFileSync('c:/Users/mitec/OneDrive/Documents/GitHub/SEO WITH Ibrar/frontend/src/app/globals.css', css);
console.log('globals.css updated for Ultra Hero successfully.');
