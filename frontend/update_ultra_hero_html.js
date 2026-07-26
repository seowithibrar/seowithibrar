const fs = require('fs');
let content = fs.readFileSync('c:/Users/mitec/OneDrive/Documents/GitHub/SEO WITH Ibrar/frontend/src/app/page.js', 'utf8');

// The regex will match either the old "hero" or "hero-redesign bg-grid"
const heroRegex = /<section className=\"hero[^>]*>([\s\S]*?)<\/section>/;

const newHero = `
<section className="hero-ultra" id="home">
    <div className="hero-ultra-bg">
        <div className="hero-glow-1"></div>
        <div className="hero-glow-2"></div>
    </div>
    
    <div className="container hero-ultra-container">
        {/* Left Side: Typography & CTA */}
        <div className="animate-slide-up" style={{position: 'relative', zIndex: 20}}>
            <div className="badge-ultra">
                ⭐ Trusted by 500+ Businesses Worldwide
            </div>
            
            <h1 className="title-ultra">
                Grow Your Business With<br />
                <span className="title-gradient">Local SEO, AI SEO &<br />Google Rankings</span> That Convert
            </h1>
            
            <p className="desc-ultra">
                Helping local businesses dominate Google Search, Google Maps and AI Search through proven SEO strategies that generate real traffic, leads and sales.
            </p>
            
            <div className="bullet-grid">
                <div className="bullet-item"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#16C784" strokeWidth="3"><polyline points="20 6 9 17 4 12"></polyline></svg> Local SEO Expert</div>
                <div className="bullet-item"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#16C784" strokeWidth="3"><polyline points="20 6 9 17 4 12"></polyline></svg> Technical SEO Audits</div>
                <div className="bullet-item"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#16C784" strokeWidth="3"><polyline points="20 6 9 17 4 12"></polyline></svg> AI Search Optimization</div>
                <div className="bullet-item"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#16C784" strokeWidth="3"><polyline points="20 6 9 17 4 12"></polyline></svg> Google Maps Ranking</div>
                <div className="bullet-item"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#16C784" strokeWidth="3"><polyline points="20 6 9 17 4 12"></polyline></svg> Content Strategy</div>
                <div className="bullet-item"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#16C784" strokeWidth="3"><polyline points="20 6 9 17 4 12"></polyline></svg> 8+ Years Experience</div>
            </div>
            
            <div className="cta-group">
                <a href="/contact" className="btn-ultra-primary">Book Free Strategy Call</a>
                <a href="/portfolio" className="btn-ultra-secondary">View Case Studies</a>
            </div>
            
            <div className="social-proof-section">
                <div className="rating-box">
                    <div className="stars">★★★★★</div>
                    <span className="trust-text" style={{fontWeight: 600, color: '#fff'}}>4.9/5 Rating</span>
                </div>
                
                <div style={{display: 'flex', alignItems: 'center', gap: '1rem', borderLeft: '1px solid rgba(255,255,255,0.1)', paddingLeft: '2rem'}}>
                    <div className="avatar-stack">
                        {/* Placeholder Avatars */}
                        <img src="https://i.pravatar.cc/100?img=1" alt="Client" />
                        <img src="https://i.pravatar.cc/100?img=2" alt="Client" />
                        <img src="https://i.pravatar.cc/100?img=3" alt="Client" />
                        <img src="https://i.pravatar.cc/100?img=4" alt="Client" />
                        <img src="https://i.pravatar.cc/100?img=5" alt="Client" />
                    </div>
                    <span className="trust-text">Trusted by 500+<br/>Business Owners</span>
                </div>
            </div>
            
            <div className="mini-stats-grid">
                <div className="mini-stat-card">
                    <div className="mini-stat-icon">📈</div>
                    <div className="mini-stat-info">
                        <h4>1200+</h4>
                        <p>Keywords Ranked</p>
                    </div>
                </div>
                <div className="mini-stat-card">
                    <div className="mini-stat-icon">🚀</div>
                    <div className="mini-stat-info">
                        <h4>$8M+</h4>
                        <p>Revenue Generated</p>
                    </div>
                </div>
            </div>
        </div>

        {/* Right Side: Portrait & Floating Elements */}
        <div className="portrait-stage">
            <div className="organic-blob"></div>
            
            <img src="/images/ibrar.png" alt="Ibrar SEO Expert" className="portrait-image-full animate-slide-up" style={{animationDelay: '0.2s'}} />
            
            {/* Floating Metric Cards */}
            <div className="floating-metric m-top-left">
                <span className="metric-label">Google Rankings</span>
                <span className="metric-value">#1</span>
            </div>
            
            <div className="floating-metric m-top-right">
                <span className="metric-label">Organic Traffic</span>
                <span className="metric-value">+420%</span>
            </div>
            
            <div className="floating-metric m-mid-right">
                <span className="metric-label">Leads Generated</span>
                <span className="metric-value">18,500+</span>
            </div>
            
            <div className="floating-metric m-bot-left">
                <span className="metric-label">Happy Clients</span>
                <span className="metric-value">500+</span>
            </div>
            
            <div className="floating-metric m-bot-right">
                <span className="metric-label">SEO Score</span>
                <span className="metric-value">98%</span>
            </div>
            
            {/* Floating SEO Icons */}
            <svg className="floating-icon" style={{top: '5%', left: '20%', animationDelay: '0.5s'}} width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.5"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg>
            <svg className="floating-icon" style={{top: '40%', left: '-5%', animationDelay: '1.2s'}} width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.5"><path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"></path></svg>
            <svg className="floating-icon" style={{top: '80%', left: '10%', animationDelay: '2.1s'}} width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.5"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"></path><circle cx="12" cy="10" r="3"></circle></svg>
            <svg className="floating-icon" style={{top: '10%', right: '30%', animationDelay: '0.8s'}} width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.5"><polyline points="22 12 18 12 15 21 9 3 6 12 2 12"></polyline></svg>
            <svg className="floating-icon" style={{top: '60%', right: '0%', animationDelay: '1.7s'}} width="36" height="36" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.5"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon></svg>
        </div>
    </div>
</section>
`;

if (heroRegex.test(content)) {
    content = content.replace(heroRegex, newHero.trim());
    fs.writeFileSync('c:/Users/mitec/OneDrive/Documents/GitHub/SEO WITH Ibrar/frontend/src/app/page.js', content);
    console.log('page.js ultra hero updated successfully');
} else {
    console.log('Hero section not found');
}
