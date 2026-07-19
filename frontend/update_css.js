const fs = require('fs');
let css = fs.readFileSync('c:/Users/mitec/OneDrive/Documents/GitHub/SEO WITH Ibrar/frontend/src/app/globals.css', 'utf8');

// Replace hardcoded RGBA greens with new Emerald green
css = css.replace(/140,\s*198,\s*63/g, '16, 185, 129');

// Dark mode overrides for specific elements that were light
css = css.replace(/background-color:\s*var\(--color-white\);/g, 'background-color: var(--color-dark-surface);');
css = css.replace(/color:\s*var\(--color-dark\);/g, 'color: var(--color-text-main);');

// Make navbar even more premium glassmorphic
css = css.replace(/background-color:\s*rgba\(15,\s*23,\s*42,\s*0\.9\);/, 'background-color: rgba(2, 6, 23, 0.7); backdrop-filter: blur(20px); -webkit-backdrop-filter: blur(20px);');

// Add animations and utility classes at the end
const animations = `
/* ==========================================================================
   Premium Micro-Animations & Utilities
   ========================================================================== */
@keyframes float {
  0% { transform: translateY(0px); }
  50% { transform: translateY(-10px); }
  100% { transform: translateY(0px); }
}

@keyframes pulse-glow {
  0% { box-shadow: 0 0 0 0 rgba(16, 185, 129, 0.4); }
  70% { box-shadow: 0 0 0 15px rgba(16, 185, 129, 0); }
  100% { box-shadow: 0 0 0 0 rgba(16, 185, 129, 0); }
}

@keyframes slideUpFade {
  from { opacity: 0; transform: translateY(30px); }
  to { opacity: 1; transform: translateY(0); }
}

.animate-float {
  animation: float 6s ease-in-out infinite;
}

.animate-slide-up {
  animation: slideUpFade 0.8s cubic-bezier(0.16, 1, 0.3, 1) forwards;
}

.glass-panel {
  background: rgba(15, 23, 42, 0.6);
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px);
  border: 1px solid rgba(255, 255, 255, 0.05);
  box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
  border-radius: 16px;
}

.text-gradient {
  background: linear-gradient(135deg, #10b981 0%, #3b82f6 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.btn-primary:hover {
  animation: pulse-glow 1.5s infinite;
}
`;

if (!css.includes('Premium Micro-Animations & Utilities')) {
  css += '\n' + animations;
}

fs.writeFileSync('c:/Users/mitec/OneDrive/Documents/GitHub/SEO WITH Ibrar/frontend/src/app/globals.css', css);
console.log('globals.css updated successfully.');
