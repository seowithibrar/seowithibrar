const fs = require('fs');

let html = fs.readFileSync('c:/Users/mitec/OneDrive/Documents/GitHub/SEO WITH Ibrar/index.html', 'utf8');
const mainMatch = html.match(/<main>([\s\S]*?)<\/main>/);

if (mainMatch) {
  let mainContent = mainMatch[1];
  
  // Basic JSX conversions
  mainContent = mainContent.replace(/class=/g, 'className=');
  mainContent = mainContent.replace(/for=/g, 'htmlFor=');
  mainContent = mainContent.replace(/<img([^>]*)>/g, (m, p1) => {
    if (p1.trim().endsWith('/')) return m;
    return '<img' + p1 + ' />';
  });
  mainContent = mainContent.replace(/<br>/g, '<br />');
  mainContent = mainContent.replace(/<hr([^>]*)>/g, (m, p1) => {
    if (p1.trim().endsWith('/')) return m;
    return '<hr' + p1 + ' />';
  });
  mainContent = mainContent.replace(/<input([^>]*)>/g, (m, p1) => {
    if (p1.trim().endsWith('/')) return m;
    return '<input' + p1 + ' />';
  });
  
  // Style strings to objects
  mainContent = mainContent.replace(/style="([^"]*)"/g, (m, p1) => {
    const parts = p1.split(';').filter(Boolean);
    const styleObj = {};
    parts.forEach(p => {
      const [k, v] = p.split(':');
      if (k && v) {
        const camelK = k.trim().replace(/-([a-z])/g, g => g[1].toUpperCase());
        styleObj[camelK] = v.trim();
      }
    });
    return 'style={{' + Object.entries(styleObj).map(([k,v]) => k + ': "' + v + '"').join(', ') + '}}';
  });

  // SVG attributes
  mainContent = mainContent.replace(/viewBox=/g, 'viewBox='); // Already camelCase or lowercase, let's just do lowercase replacements
  mainContent = mainContent.replace(/stroke-width=/g, 'strokeWidth=');
  mainContent = mainContent.replace(/stroke-linecap=/g, 'strokeLinecap=');
  mainContent = mainContent.replace(/stroke-linejoin=/g, 'strokeLinejoin=');
  mainContent = mainContent.replace(/clip-rule=/g, 'clipRule=');
  mainContent = mainContent.replace(/fill-rule=/g, 'fillRule=');

  const pageJsContent = `import Link from 'next/link';\n\nexport default function Home() {\n  return (\n    <>\n${mainContent}\n    </>\n  );\n}\n`;
  
  fs.writeFileSync('c:/Users/mitec/OneDrive/Documents/GitHub/SEO WITH Ibrar/frontend/src/app/page.js', pageJsContent);
  console.log('Conversion successful');
} else {
  console.log('Main not found');
}
