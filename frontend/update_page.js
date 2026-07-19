const fs = require('fs');
let content = fs.readFileSync('c:/Users/mitec/OneDrive/Documents/GitHub/SEO WITH Ibrar/frontend/src/app/page.js', 'utf8');

content = content.replace('className="hero-content"', 'className="hero-content animate-slide-up"');
content = content.replace('className="text-green">Results', 'className="text-gradient">Results');
content = content.replace('className="floating-card card-projects"', 'className="floating-card card-projects animate-float glass-panel"');
content = content.replace('className="floating-card card-satisfaction"', 'className="floating-card card-satisfaction animate-float glass-panel" style={{animationDelay: "0.5s"}}');
content = content.replace('className="floating-card card-experience"', 'className="floating-card card-experience animate-float glass-panel" style={{animationDelay: "1s"}}');
content = content.replace('className="floating-card card-chart"', 'className="floating-card card-chart animate-float glass-panel" style={{animationDelay: "1.5s"}}');

fs.writeFileSync('c:/Users/mitec/OneDrive/Documents/GitHub/SEO WITH Ibrar/frontend/src/app/page.js', content);
console.log('page.js updated successfully');
