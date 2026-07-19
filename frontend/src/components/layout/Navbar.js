import Link from 'next/link';

export default function Navbar() {
  return (
    <header className="navbar">
      <div className="container nav-container">
        <Link href="/" className="logo">
          <img src="/images/logo-full.png" alt="SEO With Ibrar Logo" className="logo-img" />
        </Link>
        <nav className="nav-menu">
          <Link href="/" className="nav-link">HOME</Link>
          <div className="nav-item-dropdown">
            <span className="nav-link">SERVICE <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" style={{marginLeft: '2px'}}><path d="M6 9l6 6 6-6"/></svg></span>
            <div className="mega-menu">
              <div className="mega-column">
                <div className="mega-column-header">SEO SERVICES</div>
                <div className="mega-column-items">
                  <Link href="/seo-services-pakistan" className="mega-item">
                    <div className="mega-item-dot"></div>
                    <div className="mega-item-content">
                      <div className="mega-item-title">SEO Expert Services</div>
                      <div className="mega-item-desc">Our primary organic growth plans</div>
                    </div>
                  </Link>
                  <Link href="/seo-services-visa-consultancy" className="mega-item">
                    <div className="mega-item-dot"></div>
                    <div className="mega-item-content">
                      <div className="mega-item-title">Visa Consultancy SEO</div>
                      <div className="mega-item-desc">Drive target candidate leads</div>
                    </div>
                  </Link>
                  <Link href="/seo-services-education" className="mega-item">
                    <div className="mega-item-dot"></div>
                    <div className="mega-item-content">
                      <div className="mega-item-title">Education SEO</div>
                      <div className="mega-item-desc">Optimize academic trust & signups</div>
                    </div>
                  </Link>
                </div>
              </div>
              <div className="mega-column">
                <div className="mega-column-header">WORDPRESS SOLUTIONS</div>
                <div className="mega-column-items">
                  <Link href="/wordpress-design-services" className="mega-item">
                    <div className="mega-item-dot"></div>
                    <div className="mega-item-content">
                      <div className="mega-item-title">WordPress Solutions</div>
                      <div className="mega-item-desc">High performance enterprise sites</div>
                    </div>
                  </Link>
                  <Link href="/wordpress-design-services-for-visa-consultancy" className="mega-item">
                    <div className="mega-item-dot"></div>
                    <div className="mega-item-content">
                      <div className="mega-item-title">WordPress Visa Services</div>
                      <div className="mega-item-desc">Immigration consulting portals</div>
                    </div>
                  </Link>
                  <Link href="/wordpress-design-services-for-education" className="mega-item">
                    <div className="mega-item-dot"></div>
                    <div className="mega-item-content">
                      <div className="mega-item-title">WordPress Education Services</div>
                      <div className="mega-item-desc">Academies, colleges & platforms</div>
                    </div>
                  </Link>
                </div>
              </div>
            </div>
          </div>
          <div className="nav-item-dropdown">
            <span className="nav-link">LOCATIONS <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" style={{marginLeft: '2px'}}><path d="M6 9l6 6 6-6"/></svg></span>
            <div className="mega-menu" style={{width: '250px', gridTemplateColumns: '1fr'}}>
              <div className="mega-column">
                <Link href="/seo-services-lahore" className="mega-item">
                  <div className="mega-item-dot"></div>
                  <div className="mega-item-content">
                    <div className="mega-item-title">SEO Services Lahore</div>
                  </div>
                </Link>
              </div>
            </div>
          </div>
          <Link href="/about" className="nav-link">ABOUT US</Link>
          <Link href="/contact" className="nav-link">CONTACT US</Link>
          <Link href="/portfolio" className="nav-link">PORTFOLIO</Link>
          <Link href="/blog" className="nav-link">BLOG</Link>
        </nav>
        <Link href="/contact" className="btn btn-primary nav-cta">FREE CONSULTATION CALL</Link>
        <button className="mobile-menu-btn" aria-label="Toggle Menu">
          <span></span>
          <span></span>
          <span></span>
        </button>
      </div>
    </header>
  );
}
