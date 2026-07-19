const fs = require('fs');

let css = fs.readFileSync('c:/Users/mitec/OneDrive/Documents/GitHub/SEO WITH Ibrar/frontend/src/app/globals.css', 'utf8');

const heroStyles = `
/* ==========================================================================
   Hero Redesign Utilities
   ========================================================================== */
.bg-grid {
    background-size: 40px 40px;
    background-image: linear-gradient(to right, rgba(255, 255, 255, 0.05) 1px, transparent 1px),
                      linear-gradient(to bottom, rgba(255, 255, 255, 0.05) 1px, transparent 1px);
    position: relative;
}

.bg-grid::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0; bottom: 0;
    background: radial-gradient(circle at center, transparent 0%, var(--color-dark) 80%);
    pointer-events: none;
    z-index: 0;
}

.hero-redesign {
    padding: 120px 0;
    position: relative;
    overflow: hidden;
    background-color: var(--color-dark);
}

.hero-redesign-container {
    display: grid;
    grid-template-columns: 1.2fr 0.8fr;
    gap: 4rem;
    align-items: center;
    position: relative;
    z-index: 1;
}

@media (max-width: 992px) {
    .hero-redesign-container {
        grid-template-columns: 1fr;
        text-align: center;
    }
}

.hero-redesign-content h1 {
    font-size: 4.5rem;
    font-weight: 800;
    line-height: 1.1;
    margin-bottom: 1.5rem;
    letter-spacing: -1px;
}

.hero-redesign-content p {
    font-size: 1.1rem;
    color: var(--color-text-muted);
    max-width: 600px;
    margin-bottom: 2.5rem;
}

@media (max-width: 992px) {
    .hero-redesign-content p {
        margin-left: auto;
        margin-right: auto;
    }
    .hero-redesign-content h1 {
        font-size: 3rem;
    }
}

.portrait-container {
    position: relative;
    display: flex;
    justify-content: center;
    align-items: center;
}

.portrait-mask {
    width: 450px;
    height: 450px;
    background: linear-gradient(135deg, rgba(16, 185, 129, 0.1), rgba(59, 130, 246, 0.1));
    border-radius: 50%;
    overflow: hidden;
    position: relative;
    border: 1px solid rgba(255,255,255,0.05);
    box-shadow: 0 0 80px rgba(16, 185, 129, 0.15);
}

.portrait-img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    object-position: top center;
    mix-blend-mode: normal;
}

/* Floating Sparkles */
.sparkle {
    position: absolute;
    color: var(--color-primary);
    animation: pulse-glow 2s infinite alternate;
}

.sparkle-1 { top: -20px; right: 20px; font-size: 3rem; animation-delay: 0s; }
.sparkle-2 { top: 40px; right: -30px; font-size: 1.5rem; animation-delay: 0.5s; }
.sparkle-3 { bottom: 40px; left: -20px; font-size: 2rem; animation-delay: 1s; }
`;

if (!css.includes('Hero Redesign Utilities')) {
  css += '\n' + heroStyles;
}

fs.writeFileSync('c:/Users/mitec/OneDrive/Documents/GitHub/SEO WITH Ibrar/frontend/src/app/globals.css', css);
console.log('globals.css updated successfully.');
