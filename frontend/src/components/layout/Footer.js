import Link from 'next/link';

export default function Footer() {
  return (
    <footer className="footer new-mega-footer">
      <div className="container footer-container-new">
        <div className="footer-col-main">
          <Link href="/" className="logo footer-logo" style={{marginBottom: '1.5rem', display: 'inline-flex', alignItems: 'center'}}>
            <img src="/images/logo-full.png" alt="SEO With Ibrar Logo" className="logo-img" />
          </Link>
          <p className="footer-desc" style={{color: 'rgba(255, 255, 255, 0.6)', fontSize: '0.85rem', lineHeight: '1.6', marginBottom: '2rem'}}>
            Pristine, results-driven organic search engine optimization and custom WordPress development. We focus strictly on white-hat growth, transparent reporting, and turning website traffic into physical business leads.
          </p>
          <div className="footer-location" style={{display: 'flex', alignItems: 'center', gap: '0.5rem', color: 'rgba(255, 255, 255, 0.5)', fontSize: '0.85rem'}}>
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="var(--color-primary)" strokeWidth="2"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"></path><circle cx="12" cy="10" r="3"></circle></svg>
            Lahore, Punjab, Pakistan
          </div>
        </div>
        <div className="footer-col">
          <div className="mega-column-header" style={{marginBottom: '2rem'}}>OUR SERVICES</div>
          <ul className="footer-links" style={{listStyle: 'none', padding: 0}}>
            <li><Link href="/seo-services-pakistan">SEO Expert Services</Link></li>
            <li><Link href="/seo-services-visa-consultancy">Visa Consultancy SEO</Link></li>
            <li><Link href="/seo-services-education">Education SEO</Link></li>
            <li><Link href="/wordpress-design-services">WordPress Solutions</Link></li>
            <li><Link href="/wordpress-design-services-for-visa-consultancy">WordPress Visa Services</Link></li>
            <li><Link href="/wordpress-design-services-for-education">WordPress Education Services</Link></li>
          </ul>
        </div>
        <div className="footer-col">
          <div className="mega-column-header" style={{marginBottom: '2rem', color: '#3b82f6'}}>LOCALIZED SEO HUBS</div>
          <ul className="footer-links" style={{listStyle: 'none', padding: 0}}>
            <li><Link href="/seo-services-pakistan">SEO Services in Pakistan</Link></li>
            <li><Link href="/seo-services-lahore">SEO Services in Lahore</Link></li>
            <li><Link href="/seo-services-karachi">Karachi SEO Solutions</Link></li>
            <li><Link href="/seo-services-islamabad">Islamabad SEO Solutions</Link></li>
            <li><Link href="/seo-services-faisalabad">Faisalabad SEO Solutions</Link></li>
            <li><Link href="/seo-services-rawalpindi">Rawalpindi SEO Solutions</Link></li>
          </ul>
        </div>
        <div className="footer-col">
          <div style={{display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '2rem'}}>
            <div>
              <div className="mega-column-header" style={{marginBottom: '2rem'}}>INSIGHTS HUB</div>
              <Link href="/portfolio" style={{color: 'var(--color-primary)', fontSize: '0.8rem', fontWeight: 700, display: 'flex', alignItems: 'center', gap: '0.5rem', marginBottom: '1rem', textTransform: 'uppercase'}}>
                <svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor" stroke="none"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon></svg>
                CLIENT PORTFOLIO STUDIES
              </Link>
              <Link href="/blog" style={{color: 'var(--color-primary)', fontSize: '0.8rem', fontWeight: 700, display: 'block', marginBottom: '1.5rem', textTransform: 'uppercase'}}>
                VIEW ALL ARTICLES
              </Link>
              <ul className="footer-links" style={{listStyle: 'none', padding: 0}}>
                <li><Link href="/blog">How to Rank Your Visa Agency #1...</Link></li>
                <li><Link href="/ultimate-guide-to-wordpress-speed-optimization">WordPress Speed Optimization</Link></li>
                <li><Link href="/geo-generative-engine-optimization-vs-traditional-seo">GEO</Link></li>
              </ul>
            </div>
            <div>
              <div className="mega-column-header" style={{marginBottom: '2rem'}}>QUALITY & SUPPORT</div>
              <div style={{background: 'rgba(255, 255, 255, 0.03)', border: '1px solid rgba(255, 255, 255, 0.05)', borderRadius: '12px', padding: '1.5rem'}}>
                <div style={{color: 'var(--color-primary)', fontSize: '0.85rem', fontWeight: 700, display: 'flex', alignItems: 'center', gap: '0.5rem', marginBottom: '1rem', textTransform: 'uppercase'}}>
                  <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="3"><polyline points="20 6 9 17 4 12"></polyline></svg>
                  WHITEHAT CERTIFIED
                </div>
                <p style={{color: 'rgba(255, 255, 255, 0.5)', fontSize: '0.75rem', lineHeight: '1.5', marginBottom: '1.5rem'}}>
                  Every tactic strictly adheres to webmaster rules. We never employ spam comments, hidden redirects, or low-quality backlink layers.
                </p>
                <div style={{color: 'rgba(255, 255, 255, 0.3)', fontSize: '0.65rem', textTransform: 'uppercase', letterSpacing: '1px', marginBottom: '0.25rem'}}>DIRECT CHANNEL</div>
                <a href="mailto:ibrar@seowithibrar.com" style={{color: 'white', fontSize: '0.85rem', fontWeight: 600}}>ibrar@seowithibrar.com</a>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div className="footer-bottom" style={{borderTop: '1px solid rgba(255, 255, 255, 0.05)', padding: '1.5rem 0', marginTop: '1rem'}}>
        <div className="container" style={{display: 'flex', justifyContent: 'space-between', alignItems: 'center', fontSize: '0.75rem', color: 'rgba(255, 255, 255, 0.4)', flexWrap: 'wrap', gap: '1rem'}}>
          <div style={{display: 'flex', alignItems: 'center', gap: '1.5rem'}}>
            <span>&copy; 2026 SEO with Ibrar. All rights reserved. Registered Lahore SEO Agency.</span>
            <a href="https://linkedin.com/in/ibrar-ahmad" target="_blank" rel="noopener noreferrer" style={{color: 'rgba(255, 255, 255, 0.6)', display: 'flex', alignItems: 'center', gap: '0.25rem', fontWeight: 600, letterSpacing: '1px', transition: 'var(--transition)'}}>
              LINKEDIN PROFILE <svg width="10" height="10" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2"><line x1="7" y1="17" x2="17" y2="7"></line><polyline points="7 7 17 7 17 17"></polyline></svg>
            </a>
          </div>
          <div style={{display: 'flex', alignItems: 'center', gap: '1.5rem', textTransform: 'uppercase', fontWeight: 600, letterSpacing: '1px'}}>
            <span>GOOGLE SEARCH CONSOLE VERIFIED</span>
            <span style={{color: 'var(--color-primary)'}}>SHOW TECH AUDIT</span>
          </div>
        </div>
      </div>
    </footer>
  );
}
