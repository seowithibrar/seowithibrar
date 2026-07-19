const fs = require('fs');
let content = fs.readFileSync('c:/Users/mitec/OneDrive/Documents/GitHub/SEO WITH Ibrar/frontend/src/app/page.js', 'utf8');

const heroRegex = /<section className="hero" id="home">([\s\S]*?)<\/section>/;

const newHero = `
<section className="hero-redesign bg-grid" id="home">
    <div className="container hero-redesign-container">
        {/* Left Side: Typography & CTA */}
        <div className="hero-redesign-content animate-slide-up">
            <h1 className="hero-title">
                Welcome to my new <br />
                <span className="text-gradient">Portfolio Website</span>
            </h1>
            <p className="hero-description">
                Hello I am Ibrar, Professional SEO Expert & Full-stack Developer. This is my portfolio site here I am presenting my projects and services. Let's Explore.
            </p>
            <div className="hero-actions" style={{display: 'flex', gap: '1rem', alignItems: 'center'}}>
                <a href="/contact" className="btn btn-primary" style={{borderRadius: '8px'}}>
                    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4M7 10l5 5 5-5M12 15V3"/></svg>
                    Download CV
                </a>
            </div>
        </div>

        {/* Right Side: Portrait Mask */}
        <div className="portrait-container animate-float">
            {/* Sparkles */}
            <svg className="sparkle sparkle-1" width="40" height="40" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2L15 9L22 12L15 15L12 22L9 15L2 12L9 9L12 2Z"/></svg>
            <svg className="sparkle sparkle-2" width="24" height="24" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2L15 9L22 12L15 15L12 22L9 15L2 12L9 9L12 2Z"/></svg>
            <svg className="sparkle sparkle-3" width="32" height="32" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2L15 9L22 12L15 15L12 22L9 15L2 12L9 9L12 2Z"/></svg>
            
            <div className="portrait-mask">
                <img src="/images/ibrar.png" alt="Ibrar SEO Expert" className="portrait-img" />
            </div>
        </div>
    </div>
</section>
`;

if (heroRegex.test(content)) {
    content = content.replace(heroRegex, newHero.trim());
    fs.writeFileSync('c:/Users/mitec/OneDrive/Documents/GitHub/SEO WITH Ibrar/frontend/src/app/page.js', content);
    console.log('page.js hero updated successfully');
} else {
    console.log('Hero section not found');
}
