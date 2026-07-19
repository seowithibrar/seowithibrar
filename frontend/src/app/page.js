import Link from 'next/link';

export default function Home() {
  return (
    <>

        {/**/}
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
        {/**/}
        <section className="trusted-by">
            <div className="container text-center">
                <p className="section-subtitle">TRUSTED BY TOOLS I USE</p>
                <div className="tools-grid">
                    {/**/}
                    <div className="tool-logo">Google Analytics</div>
                    <div className="tool-logo">Google Search Console</div>
                    <div className="tool-logo">Ahrefs</div>
                    <div className="tool-logo">SEMRush</div>
                    <div className="tool-logo">ScreamingFrog</div>
                    <div className="tool-logo">WordPress</div>
                    <div className="tool-logo">Elementor</div>
                </div>
            </div>
        </section>
        {/**/}
        <section className="about-modern" id="about">
            <div className="container" style={{maxWidth: "1200px"}}>
                <div className="about-modern-grid">
                    {/**/}
                    <div>
                        {/**/}
                        <div style={{position: "relative", borderRadius: "24px", padding: "1.5rem", background: "linear-gradient(135deg, rgba(183, 255, 0, 0.4), rgba(183, 255, 0, 0.05))", marginBottom: "2rem"}}>
                            <img src="images/ibrar.png" alt="Ibrar Ahmad" style={{width: "100%", borderRadius: "16px", display: "block"}} />
                            {/**/}
                            <div style={{position: "absolute", bottom: "0", left: "50%", transform: "translate(-50%, 50%)", background: "var(--color-dark)", color: "var(--color-white)", padding: "0.5rem 1.5rem", borderRadius: "30px", fontSize: "0.75rem", fontWeight: "700", whiteSpace: "nowrap", display: "flex", alignItems: "center", gap: "0.5rem", border: "4px solid var(--color-white)"}}>
                                <span style={{color: "var(--color-primary)"}}>●</span> IBRAR AHMAD • LEAD CONSULTANT
                            </div>
                        </div>
                        {/**/}
                        <div style={{border: "1px solid var(--color-border)", borderRadius: "16px", padding: "2rem", background: "var(--color-white)"}}>
                            <div style={{display: "flex", justifyContent: "space-between", alignItems: "center", marginBottom: "1.5rem", borderBottom: "1px solid var(--color-border)", paddingBottom: "1rem"}}>
                                <span style={{fontSize: "0.75rem", fontWeight: "700", color: "#a1a1aa", letterSpacing: "1px", textTransform: "uppercase"}}>Verified Performance Metrics</span>
                                <span style={{fontSize: "0.85rem", fontWeight: "600", color: "var(--color-primary)", display: "flex", alignItems: "center", gap: "0.25rem"}}><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2"><path d="M22 12h-4l-3 9L9 3l-3 9H2"></path></svg> Lahore-Based</span>
                            </div>
                            <div style={{display: "grid", gridTemplateColumns: "1fr 1fr", gap: "1.5rem"}}>
                                <div>
                                    <div style={{fontSize: "1.5rem", fontWeight: "800", color: "var(--color-dark)", marginBottom: "0.25rem"}}>7+ Years</div>
                                    <div style={{fontSize: "0.85rem", fontWeight: "700", color: "var(--color-dark)"}}>SEO Expertise</div>
                                    <div style={{fontSize: "0.75rem", color: "#a1a1aa"}}>Client Deliveries</div>
                                </div>
                                <div>
                                    <div style={{fontSize: "1.5rem", fontWeight: "800", color: "var(--color-dark)", marginBottom: "0.25rem"}}>120+</div>
                                    <div style={{fontSize: "0.85rem", fontWeight: "700", color: "var(--color-dark)"}}>Projects Completed</div>
                                    <div style={{fontSize: "0.75rem", color: "#a1a1aa"}}>Brands Ranked</div>
                                </div>
                                <div>
                                    <div style={{fontSize: "1.5rem", fontWeight: "800", color: "var(--color-dark)", marginBottom: "0.25rem"}}>98%</div>
                                    <div style={{fontSize: "0.85rem", fontWeight: "700", color: "var(--color-dark)"}}>Core Web Vitals</div>
                                    <div style={{fontSize: "0.75rem", color: "#a1a1aa"}}>WordPress Page Speed</div>
                                </div>
                                <div>
                                    <div style={{fontSize: "1.5rem", fontWeight: "800", color: "var(--color-dark)", marginBottom: "0.25rem"}}>+340%</div>
                                    <div style={{fontSize: "0.85rem", fontWeight: "700", color: "var(--color-dark)"}}>Avg. Traffic Growth</div>
                                    <div style={{fontSize: "0.75rem", color: "#a1a1aa"}}>Organic Strategy</div>
                                </div>
                            </div>
                        </div>
                    </div>
                    {/**/}
                    <div>
                        <span className="pill-badge" style={{background: "rgba(140, 198, 63, 0.15)", color: "var(--color-primary)", marginBottom: "1.5rem", border: "1px solid rgba(140, 198, 63, 0.3)"}}>
                            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" style={{marginRight: "4px"}}><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path><circle cx="12" cy="7" r="4"></circle></svg>
                            ABOUT IBRAR AHMAD • LEAD CONSULTANT
                        </span>
                        <h2 style={{fontSize: "3rem", fontWeight: "800", color: "var(--color-dark)", lineHeight: "1.1", marginBottom: "2rem"}}>
                            Empowering Business Visibility: Meet Ibrar Ahmad
                        </h2>
                        <div style={{width: "40px", height: "3px", backgroundColor: "var(--color-primary)", marginBottom: "2rem"}}></div>
                        <div style={{color: "var(--color-text-muted)", fontSize: "1.05rem", lineHeight: "1.8", marginBottom: "2.5rem"}}>
                            <p style={{marginBottom: "1.25rem"}}>As an independent <strong>SEO Consultant</strong> and custom <strong>WordPress Engineer</strong> based in Lahore, Pakistan, I bridge the gap between high-performance web speeds and organic search rankings. Over the past seven years, I have collaborated with direct enterprise brands, immigration authorities, training institutes, and academies to transform their websites into consistent inquiry pipelines.</p>
                            <p style={{marginBottom: "1.25rem"}}>My working philosophy focuses on real-world business objectives rather than empty keywords or vanity metrics. I clean up cluttered code, set up crawlable JSON-LD schemas, and implement white-hat optimization and speed strategies to ensure Google and users enjoy an absolute premium page experience.</p>
                            <p>Every campaign is managed with direct 1-to-1 support, weekly reports, and transparent work channels.</p>
                        </div>
                        {/**/}
                        <div style={{display: "grid", gridTemplateColumns: "repeat(auto-fit, minmax(240px, 1fr))", gap: "1.5rem", marginBottom: "3rem"}}>
                            <div style={{display: "flex", gap: "0.75rem", alignItems: "flex-start"}}>
                                <div style={{color: "var(--color-primary)", marginTop: "2px"}}><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path><polyline points="22 4 12 14.01 9 11.01"></polyline></svg></div>
                                <div>
                                    <h4 style={{fontSize: "0.95rem", fontWeight: "700", color: "var(--color-dark)", marginBottom: "0.25rem"}}>Technical SEO Audit</h4>
                                    <p style={{fontSize: "0.85rem", color: "#a1a1aa", lineHeight: "1.5"}}>Solving core crawlability and modern site indexing issues.</p>
                                </div>
                            </div>
                            <div style={{display: "flex", gap: "0.75rem", alignItems: "flex-start"}}>
                                <div style={{color: "var(--color-primary)", marginTop: "2px"}}><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path><polyline points="22 4 12 14.01 9 11.01"></polyline></svg></div>
                                <div>
                                    <h4 style={{fontSize: "0.95rem", fontWeight: "700", color: "var(--color-dark)", marginBottom: "0.25rem"}}>WordPress Clean Code</h4>
                                    <p style={{fontSize: "0.85rem", color: "#a1a1aa", lineHeight: "1.5"}}>Eliminating bloated plugins for pristine loading speed.</p>
                                </div>
                            </div>
                            <div style={{display: "flex", gap: "0.75rem", alignItems: "flex-start"}}>
                                <div style={{color: "var(--color-primary)", marginTop: "2px"}}><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path><polyline points="22 4 12 14.01 9 11.01"></polyline></svg></div>
                                <div>
                                    <h4 style={{fontSize: "0.95rem", fontWeight: "700", color: "var(--color-dark)", marginBottom: "0.25rem"}}>Semantic Content Hubs</h4>
                                    <p style={{fontSize: "0.85rem", color: "#a1a1aa", lineHeight: "1.5"}}>Targeting transactional search intents for real business leads.</p>
                                </div>
                            </div>
                            <div style={{display: "flex", gap: "0.75rem", alignItems: "flex-start"}}>
                                <div style={{color: "var(--color-primary)", marginTop: "2px"}}><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path><polyline points="22 4 12 14.01 9 11.01"></polyline></svg></div>
                                <div>
                                    <h4 style={{fontSize: "0.95rem", fontWeight: "700", color: "var(--color-dark)", marginBottom: "0.25rem"}}>Local Maps Dominance</h4>
                                    <p style={{fontSize: "0.85rem", color: "#a1a1aa", lineHeight: "1.5"}}>Structuring structured local maps schemas and organic directories.</p>
                                </div>
                            </div>
                        </div>
                        <div style={{display: "flex", gap: "1rem", flexWrap: "wrap"}}>
                            <a href="#" className="btn" style={{backgroundColor: "#0077b5", color: "white", display: "inline-flex", alignItems: "center", gap: "0.5rem", border: "none", padding: "0.75rem 1.5rem", fontWeight: "700"}}>
                                <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor"><path d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433c-1.144 0-2.063-.926-2.063-2.065 0-1.138.92-2.063 2.063-2.063 1.14 0 2.064.925 2.064 2.063 0 1.139-.925 2.065-2.064 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z"/></svg>
                                CONNECT ON LINKEDIN
                            </a>
                            <a href="contact" className="btn btn-dark" style={{display: "inline-flex", alignItems: "center", gap: "0.5rem", padding: "0.75rem 1.5rem", fontWeight: "700"}}>
                                BOOK CALL WITH IBRAR 
                                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
                            </a>
                        </div>
                    </div>
                </div>
            </div>
        </section>
        {/**/}
        <section className="services" id="services">
            <div className="container">
                <span className="pill-badge">CORE SERVICES</span>
                <h2 className="section-title text-center">SEO Services</h2>
                <p className="text-center" style={{maxWidth: "800px", margin: "0 auto", color: "var(--color-text-muted)"}}>
                    SEO services help your business get found when people search online for your products or services. I focus on improving search visibility, attracting the right audience, and turning website visits into real inquiries. The goal is steady growth, not temporary rankings.
                </p>
                <div className="services-grid">
                    <div className="service-card">
                        <div className="service-icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg></div>
                        <h4 className="service-title">Keyword Research & Search Targeting</h4>
                        <p className="service-desc">My research shows how your potential customers search and target keywords with intent.</p>
                    </div>
                    <div className="service-card">
                        <div className="service-icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline></svg></div>
                        <h4 className="service-title">On-Page SEO Optimization</h4>
                        <p className="service-desc">Your pages are optimized so search engines and users understand your content clearly.</p>
                    </div>
                    <div className="service-card">
                        <div className="service-icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2"><path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94l-3.76 3.76z"></path></svg></div>
                        <h4 className="service-title">Technical SEO Improvements</h4>
                        <p className="service-desc">Website structure, speed, and indexing issues are fixed to support better performance.</p>
                    </div>
                    <div className="service-card">
                        <div className="service-icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2"><path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71"></path></svg></div>
                        <h4 className="service-title">Content Optimization</h4>
                        <p className="service-desc">Existing content is improved to increase relevance, clarity, and engagement.</p>
                    </div>
                    <div className="service-card">
                        <div className="service-icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"></path><circle cx="12" cy="10" r="3"></circle></svg></div>
                        <h4 className="service-title">Local SEO</h4>
                        <p className="service-desc">Location based SEO helps nearby customers find your business easily.</p>
                    </div>
                </div>
                <div className="text-center" style={{marginTop: "3rem"}}>
                    <a href="#contact" className="btn btn-primary">Explore SEO Services</a>
                </div>
            </div>
        </section>
        {/**/}
        <section className="services" style={{backgroundColor: "var(--color-white)"}}>
            <div className="container">
                <h2 className="section-title text-center">Website Development Services</h2>
                <p className="text-center" style={{maxWidth: "800px", margin: "0 auto", color: "var(--color-text-muted)"}}>
                    Website development focuses on building clean, fast, and professional websites that support real business goals. Every website is created to be easy to use, easy to understand, and ready to convert visitors into inquiries.
                </p>
                <div className="services-grid">
                    <div className="service-card" style={{backgroundColor: "var(--color-bg-light)"}}>
                        <div className="service-icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2"><rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect></svg></div>
                        <h4 className="service-title">Custom Website Design</h4>
                        <p className="service-desc">Websites are designed to match your brand and present your services clearly.</p>
                    </div>
                    <div className="service-card" style={{backgroundColor: "var(--color-bg-light)"}}>
                        <div className="service-icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2"><rect x="5" y="2" width="14" height="20" rx="2" ry="2"></rect><line x1="12" y1="18" x2="12.01" y2="18"></line></svg></div>
                        <h4 className="service-title">Responsive & Mobile-Friendly</h4>
                        <p className="service-desc">Your website works smoothly across mobile, tablet, and desktop devices.</p>
                    </div>
                    <div className="service-card" style={{backgroundColor: "var(--color-bg-light)"}}>
                        <div className="service-icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2"><polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"></polygon></svg></div>
                        <h4 className="service-title">Fast Performance</h4>
                        <p className="service-desc">Speed and performance are optimized to improve user experience and engagement.</p>
                    </div>
                    <div className="service-card" style={{backgroundColor: "var(--color-bg-light)"}}>
                        <div className="service-icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2"><polygon points="12 2 2 7 12 12 22 7 12 2"></polygon><polyline points="2 17 12 22 22 17"></polyline><polyline points="2 12 12 17 22 12"></polyline></svg></div>
                        <h4 className="service-title">User-Friendly Structure</h4>
                        <p className="service-desc">Pages are organized so visitors can navigate easily and find information quickly.</p>
                    </div>
                    <div className="service-card" style={{backgroundColor: "var(--color-bg-light)"}}>
                        <div className="service-icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"></path></svg></div>
                        <h4 className="service-title">Website Maintenance & Support</h4>
                        <p className="service-desc">Ongoing support keeps your website secure, updated, and running smoothly.</p>
                    </div>
                </div>
                <div className="text-center" style={{marginTop: "3rem"}}>
                    <a href="#contact" className="btn btn-outline">Explore Website Development Services</a>
                </div>
            </div>
        </section>
        {/**/}
        <section className="process" style={{backgroundColor: "var(--color-bg-light)"}}>
            <div className="container process-container">
                <div className="process-header text-center">
                    <span className="pill-badge">HOW IT WORKS</span>
                    <h2 className="section-title">How Does SEO With Ibrar Work?</h2>
                    <p className="text-center" style={{maxWidth: "600px", margin: "0 auto", color: "var(--color-text-muted)"}}>
                        I follow a clear and structured process so everything stays simple, transparent, and focused on results.
                    </p>
                </div>
                <div className="process-timeline">
                    {/**/}
                    <div className="process-step">
                        <div className="step-icon">
                            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg>
                        </div>
                        <div className="step-number">01</div>
                        <h5 className="step-title">Understand Your Goals</h5>
                        <p className="step-desc">I start by understanding your business, services, and what you want to achieve online. This helps set clear direction before any work begins.</p>
                    </div>
                    <div className="step-arrow">→</div>
                    {/**/}
                    <div className="process-step">
                        <div className="step-icon">
                            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2"><polygon points="12 2 2 7 12 12 22 7 12 2"></polygon><polyline points="2 17 12 22 22 17"></polyline><polyline points="2 12 12 17 22 12"></polyline></svg>
                        </div>
                        <div className="step-number">02</div>
                        <h5 className="step-title">Plan and Execute</h5>
                        <p className="step-desc">Based on your goals, I create a clear strategy and start working on SEO or website improvements step by step, without guesswork.</p>
                    </div>
                    <div className="step-arrow">→</div>
                    {/**/}
                    <div className="process-step">
                        <div className="step-icon">
                            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2"><polyline points="23 6 13.5 15.5 8.5 10.5 1 18"></polyline><polyline points="17 6 23 6 23 12"></polyline></svg>
                        </div>
                        <div className="step-number">03</div>
                        <h5 className="step-title">Review and Improve</h5>
                        <p className="step-desc">Progress is reviewed regularly. Improvements are made based on performance, user behavior, and long-term growth goals.</p>
                    </div>
                </div>
            </div>
        </section>
        {/**/}
        <section className="why-choose" style={{backgroundColor: "var(--color-white)"}}>
            <div className="container">
                <div className="why-box">
                    <div className="why-content">
                        <h2 className="section-title text-white">Why Businesses Choose<br /><span className="text-green">SEO with Ibrar</span></h2>
                        <p className="why-desc">
                            I don’t offer random services. I focus on work that actually supports visibility, trust, and long-term growth. These are the core reasons businesses choose to work with SEO with Ibrar.
                        </p>
                    </div>
                    <div className="why-features">
                        <div className="check-item">
                            <div className="check-icon">✓</div>
                            <div>
                                <h5 className="check-title">Results-Focused Approach</h5>
                                <p className="check-desc">Every strategy is built around real business goals, not guesses or vanity metrics.</p>
                            </div>
                        </div>
                        <div className="check-item">
                            <div className="check-icon">✓</div>
                            <div>
                                <h5 className="check-title">Clear Communication</h5>
                                <p className="check-desc">You always know what is happening, why it matters, and how it supports growth.</p>
                            </div>
                        </div>
                        <div className="check-item">
                            <div className="check-icon">✓</div>
                            <div>
                                <h5 className="check-title">SEO & Website Expertise</h5>
                                <p className="check-desc">SEO and website structure work together to improve visibility, experience, and conversions.</p>
                            </div>
                        </div>
                        <div className="check-item">
                            <div className="check-icon">✓</div>
                            <div>
                                <h5 className="check-title">Long-Term Growth Mindset</h5>
                                <p className="check-desc">Ethical strategies create stable visibility and growth instead of short-term spikes.</p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>
        {/**/}
        <section className="services" style={{backgroundColor: "var(--color-bg-light)"}}>
            <div className="container">
                <span className="pill-badge">WHO I WORK WITH</span>
                <h2 className="section-title text-center">Industries I Work With</h2>
                <p className="text-center" style={{maxWidth: "800px", margin: "0 auto 3rem", color: "var(--color-text-muted)"}}>
                    Different industries have different challenges. I work with businesses that need visibility, trust, and consistent leads through SEO and strong websites. The approach is always adjusted based on how each industry works online.
                </p>
                <div className="services-grid" style={{gridTemplateColumns: "repeat(auto-fit, minmax(300px, 1fr))"}}>
                    <div className="service-card">
                        <div className="service-icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"></path><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"></path></svg></div>
                        <h4 className="service-title">Education & Training</h4>
                        <p className="service-desc">I work with schools, academies, coaching centers, and education platforms that want more inquiries and a stronger online presence. SEO and websites are built to attract students, explain offerings clearly, and support enrollment goals without confusion.</p>
                    </div>
                    <div className="service-card">
                        <div className="service-icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2"><circle cx="12" cy="12" r="10"></circle><path d="M12 2a14.5 14.5 0 0 0 0 20 14.5 14.5 0 0 0 0-20"></path><path d="M2 12h20"></path></svg></div>
                        <h4 className="service-title">Visa & Immigration Services</h4>
                        <p className="service-desc">Visa and immigration services depend heavily on trust. I help visa consultants and agencies build professional websites and search visibility so potential clients can find them easily and feel confident reaching out.</p>
                    </div>
                </div>
            </div>
        </section>
        {/**/}
        <section style={{padding: "8rem 0", backgroundColor: "#f8f9fa"}}>
            <div className="container">
                <div className="testimonial-header">
                    <div style={{maxWidth: "700px"}}>
                        <span style={{textTransform: "uppercase", letterSpacing: "4px", fontSize: "0.75rem", fontWeight: "700", color: "var(--color-dark)", display: "block", marginBottom: "1.5rem"}}>T E S T I M O N I A L S</span>
                        <h2 style={{fontSize: "2.5rem", fontWeight: "700", color: "var(--color-dark)", marginBottom: "1rem", lineHeight: "1.2"}}>
                            What Clients Share About Their <span style={{color: "#999"}}>Experience</span>
                        </h2>
                        <p style={{color: "var(--color-text-muted)", fontSize: "1.1rem"}}>Our clients share their experience of working with us, highlighting clear communication, consistent progress, and practical SEO support.</p>
                    </div>
                    <div>
                        <button className="nav-btn-circle" aria-label="Previous" onclick="document.querySelector('.testimonial-slider').scrollBy({left: -400, behavior: 'smooth'})">←</button>
                        <button className="nav-btn-circle" aria-label="Next" onclick="document.querySelector('.testimonial-slider').scrollBy({left: 400, behavior: 'smooth'})">→</button>
                    </div>
                </div>
                <div className="testimonial-slider">
                    <div className="testimonial-green-card">
                        <div style={{fontSize: "4rem", fontWeight: "300", lineHeight: "1", marginBottom: "1.5rem", letterSpacing: "-2px"}}>50+</div>
                        <div style={{fontSize: "0.9rem", fontWeight: "600"}}>Successfully delivered projects</div>
                    </div>
                    <div className="testimonial-card">
                        <div>
                            <div style={{fontSize: "3rem", fontFamily: "serif", color: "var(--color-dark)", lineHeight: "0.5", marginBottom: "2rem"}}>“</div>
                            <p style={{color: "var(--color-text-muted)", fontSize: "0.95rem", lineHeight: "1.7", marginBottom: "2rem"}}>Our website traffic improved gradually, and more relevant inquiries started coming in. The SEO process was explained clearly, and the results were consistent.</p>
                        </div>
                        <div style={{display: "flex", alignItems: "center", gap: "1rem"}}>
                            <div style={{width: "40px", height: "40px", borderRadius: "50%", background: "#e9ecef", display: "flex", alignItems: "center", justifyContent: "center", fontWeight: "bold", color: "var(--color-dark)", fontSize: "0.8rem"}}>AR</div>
                            <div>
                                <h4 style={{fontSize: "0.95rem", fontWeight: "700", color: "var(--color-dark)", marginBottom: "0.15rem"}}>Ahmed Raza</h4>
                                <span style={{fontSize: "0.8rem", color: "var(--color-text-muted)"}}>MD, Local Services</span>
                            </div>
                        </div>
                    </div>
                    <div className="testimonial-card">
                        <div>
                            <div style={{fontSize: "3rem", fontFamily: "serif", color: "var(--color-dark)", lineHeight: "0.5", marginBottom: "2rem"}}>“</div>
                            <p style={{color: "var(--color-text-muted)", fontSize: "0.95rem", lineHeight: "1.7", marginBottom: "2rem"}}>They communicated everything in simple terms and focused on long-term improvement instead of quick promises. We saw steady growth in visibility.</p>
                        </div>
                        <div style={{display: "flex", alignItems: "center", gap: "1rem"}}>
                            <div style={{width: "40px", height: "40px", borderRadius: "50%", background: "#e9ecef", display: "flex", alignItems: "center", justifyContent: "center", fontWeight: "bold", color: "var(--color-dark)", fontSize: "0.8rem"}}>SK</div>
                            <div>
                                <h4 style={{fontSize: "0.95rem", fontWeight: "700", color: "var(--color-dark)", marginBottom: "0.15rem"}}>Sarah Khan</h4>
                                <span style={{fontSize: "0.8rem", color: "var(--color-text-muted)"}}>Founder, Online Store</span>
                            </div>
                        </div>
                    </div>
                    <div className="testimonial-card">
                        <div>
                            <div style={{fontSize: "3rem", fontFamily: "serif", color: "var(--color-dark)", lineHeight: "0.5", marginBottom: "2rem"}}>“</div>
                            <p style={{color: "var(--color-text-muted)", fontSize: "0.95rem", lineHeight: "1.7", marginBottom: "2rem"}}>The team worked professionally and shared clear reports. Our search visibility improved, and the quality of leads also became better.</p>
                        </div>
                        <div style={{display: "flex", alignItems: "center", gap: "1rem"}}>
                            <div style={{width: "40px", height: "40px", borderRadius: "50%", background: "#e9ecef", display: "flex", alignItems: "center", justifyContent: "center", fontWeight: "bold", color: "var(--color-dark)", fontSize: "0.8rem"}}>UA</div>
                            <div>
                                <h4 style={{fontSize: "0.95rem", fontWeight: "700", color: "var(--color-dark)", marginBottom: "0.15rem"}}>Usman Ali</h4>
                                <span style={{fontSize: "0.8rem", color: "var(--color-text-muted)"}}>Marketing Manager</span>
                            </div>
                        </div>
                    </div>
                    <div className="testimonial-card">
                        <div>
                            <div style={{fontSize: "3rem", fontFamily: "serif", color: "var(--color-dark)", lineHeight: "0.5", marginBottom: "2rem"}}>“</div>
                            <p style={{color: "var(--color-text-muted)", fontSize: "0.95rem", lineHeight: "1.7", marginBottom: "2rem"}}>What I appreciated most was the honest guidance. They focused on what was best for our business, not unnecessary SEO work.</p>
                        </div>
                        <div style={{display: "flex", alignItems: "center", gap: "1rem"}}>
                            <div style={{width: "40px", height: "40px", borderRadius: "50%", background: "#e9ecef", display: "flex", alignItems: "center", justifyContent: "center", fontWeight: "bold", color: "var(--color-dark)", fontSize: "0.8rem"}}>AM</div>
                            <div>
                                <h4 style={{fontSize: "0.95rem", fontWeight: "700", color: "var(--color-dark)", marginBottom: "0.15rem"}}>Ayesha Malik</h4>
                                <span style={{fontSize: "0.8rem", color: "var(--color-text-muted)"}}>Business Owner</span>
                            </div>
                        </div>
                    </div>
                    <div className="testimonial-card">
                        <div>
                            <div style={{fontSize: "3rem", fontFamily: "serif", color: "var(--color-dark)", lineHeight: "0.5", marginBottom: "2rem"}}>“</div>
                            <p style={{color: "var(--color-text-muted)", fontSize: "0.95rem", lineHeight: "1.7", marginBottom: "2rem"}}>Reliable SEO support with transparent reporting. Our online presence improved, and we gained more confidence in our website’s performance.</p>
                        </div>
                        <div style={{display: "flex", alignItems: "center", gap: "1rem"}}>
                            <div style={{width: "40px", height: "40px", borderRadius: "50%", background: "#e9ecef", display: "flex", alignItems: "center", justifyContent: "center", fontWeight: "bold", color: "var(--color-dark)", fontSize: "0.8rem"}}>BH</div>
                            <div>
                                <h4 style={{fontSize: "0.95rem", fontWeight: "700", color: "var(--color-dark)", marginBottom: "0.15rem"}}>Bilal Hussain</h4>
                                <span style={{fontSize: "0.8rem", color: "var(--color-text-muted)"}}>Operations Head</span>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>
        {/**/}
        <section className="process" style={{backgroundColor: "var(--color-white)"}}>
            <div className="container" style={{maxWidth: "800px"}}>
                <h2 className="section-title text-center" style={{marginBottom: "3rem"}}>Frequently Asked Questions</h2>
                <div style={{display: "flex", flexDirection: "column", gap: "1.5rem"}}>
                    <div style={{paddingBottom: "1.5rem", borderBottom: "1px solid var(--color-border)"}}>
                        <h4 style={{fontWeight: "700", marginBottom: "0.5rem", color: "var(--color-dark)"}}>1. What services do you offer?</h4>
                        <p style={{color: "var(--color-text-muted)"}}>I provide SEO services and website development solutions designed to improve visibility, trust, and online performance for businesses.</p>
                    </div>
                    <div style={{paddingBottom: "1.5rem", borderBottom: "1px solid var(--color-border)"}}>
                        <h4 style={{fontWeight: "700", marginBottom: "0.5rem", color: "var(--color-dark)"}}>2. How long does SEO take to show results?</h4>
                        <p style={{color: "var(--color-text-muted)"}}>SEO is a gradual process. Most businesses start seeing noticeable improvement within three to six months, depending on competition.</p>
                    </div>
                    <div style={{paddingBottom: "1.5rem", borderBottom: "1px solid var(--color-border)"}}>
                        <h4 style={{fontWeight: "700", marginBottom: "0.5rem", color: "var(--color-dark)"}}>3. Do you work with small businesses and startups?</h4>
                        <p style={{color: "var(--color-text-muted)"}}>Yes. I work with small businesses, startups, and growing brands that want steady and reliable online growth.</p>
                    </div>
                    <div style={{paddingBottom: "1.5rem", borderBottom: "1px solid var(--color-border)"}}>
                        <h4 style={{fontWeight: "700", marginBottom: "0.5rem", color: "var(--color-dark)"}}>4. Will my website be mobile-friendly?</h4>
                        <p style={{color: "var(--color-text-muted)"}}>Yes. Every website is built to work smoothly on mobile, tablet, and desktop devices for a better user experience.</p>
                    </div>
                    <div style={{paddingBottom: "1.5rem", borderBottom: "1px solid var(--color-border)"}}>
                        <h4 style={{fontWeight: "700", marginBottom: "0.5rem", color: "var(--color-dark)"}}>5. Can you help improve an existing website?</h4>
                        <p style={{color: "var(--color-text-muted)"}}>Absolutely. I can optimize your current website for better performance, structure, and search visibility.</p>
                    </div>
                    <div style={{paddingBottom: "1.5rem", borderBottom: "1px solid var(--color-border)"}}>
                        <h4 style={{fontWeight: "700", marginBottom: "0.5rem", color: "var(--color-dark)"}}>6. Do you provide ongoing support after project completion?</h4>
                        <p style={{color: "var(--color-text-muted)"}}>Yes. Ongoing support and maintenance options are available to keep your website updated and running smoothly.</p>
                    </div>
                    <div style={{paddingBottom: "1.5rem"}}>
                        <h4 style={{fontWeight: "700", marginBottom: "0.5rem", color: "var(--color-dark)"}}>7. How do we get started?</h4>
                        <p style={{color: "var(--color-text-muted)"}}>You can start by requesting a free consultation. We’ll discuss your goals and decide the best next steps.</p>
                    </div>
                </div>
            </div>
        </section>
        {/**/}
        <section id="blog" style={{backgroundColor: "var(--color-white)", padding: "5rem 0"}}>
            <div className="container">
                <div style={{display: "flex", justifyContent: "space-between", alignItems: "flex-end", marginBottom: "3rem"}}>
                    <div>
                        <p className="section-subtitle">LATEST INSIGHTS</p>
                        <h2 className="section-title">Our Recent Articles</h2>
                    </div>
                    <a href="blog" className="btn btn-outline" style={{display: "inline-flex", alignItems: "center", gap: "0.5rem"}}>
                        View All Posts <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
                    </a>
                </div>
                <div className="blog-grid">
                    {/**/}
                    <div className="blog-card">
                        <div className="blog-image">
                            <img src="images/top-seo-experts-pakistan.webp" alt="Top 15+ SEO Experts in Pakistan" />
                        </div>
                        <div className="blog-content">
                            <div className="blog-meta">
                                <span className="blog-category">MODERN SEO</span>
                                <span className="blog-date">July 3, 2025</span>
                            </div>
                            <h3 className="blog-title"><a href="top-seo-experts-in-pakistan">Top 15+ SEO Experts in Pakistan – Ibrar Leads the Way!</a></h3>
                            <p className="blog-excerpt">In the ever-evolving world of digital marketing, Search Engine Optimization (SEO) plays a crucial role in driving organic traffic and improving online visibility.</p>
                            <a href="top-seo-experts-in-pakistan" className="blog-read-more">Read More <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2"><path d="M5 12h14M12 5l7 7-7 7"/></svg></a>
                        </div>
                    </div>
                    {/**/}
                    <div className="blog-card">
                        <div className="blog-image">
                            <img src="images/ultimate-guide-to-wordpress-speed-optimization.webp" alt="WordPress Speed Optimization" />
                        </div>
                        <div className="blog-content">
                            <div className="blog-meta">
                                <span className="blog-category">WordPress</span>
                                <span className="blog-date">Oct 05, 2026</span>
                            </div>
                            <h3 className="blog-title"><a href="ultimate-guide-to-wordpress-speed-optimization">Ultimate Guide to WordPress Speed Optimization</a></h3>
                            <p className="blog-excerpt">Is your slow website killing your conversion rate? Learn how to optimize your WordPress site to load in under 2 seconds and improve core web vitals.</p>
                            <a href="ultimate-guide-to-wordpress-speed-optimization" className="blog-read-more">Read More <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2"><path d="M5 12h14M12 5l7 7-7 7"/></svg></a>
                        </div>
                    </div>
                    {/**/}
                    <div className="blog-card">
                        <div className="blog-image">
                            <img src="images/geo-generative-engine-optimization-vs-traditional-seo.webp" alt="GEO vs Traditional SEO" />
                        </div>
                        <div className="blog-content">
                            <div className="blog-meta">
                                <span className="blog-category">Future of Search</span>
                                <span className="blog-date">Sep 28, 2026</span>
                            </div>
                            <h3 className="blog-title"><a href="geo-generative-engine-optimization-vs-traditional-seo">GEO (Generative Engine Optimization) vs Traditional SEO</a></h3>
                            <p className="blog-excerpt">As AI search engines evolve, how you optimize your content must change. Here is what you need to know about preparing for Generative Engine Optimization.</p>
                            <a href="geo-generative-engine-optimization-vs-traditional-seo" className="blog-read-more">Read More <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2"><path d="M5 12h14M12 5l7 7-7 7"/></svg></a>
                        </div>
                    </div>
                </div>
            </div>
        </section>
    {/**/}
        <section className="cta-banner" style={{backgroundColor: "var(--color-bg-light)", padding: "4rem 0 6rem 0"}}>
            <div className="container">
                <div className="cta-box">
                    <div className="cta-content">
                        <h2 className="cta-title">Are You Prepared to Expand Your Online Presence?</h2>
                        <p className="cta-desc">If your business isn’t getting the attention it deserves, it’s time to change that. Whether you need stronger visibility or a website that actually works, I help you move forward with clear strategy and real focus.</p>
                    </div>
                    <a href="http://127.0.0.1:5500/contact.html" className="btn btn-dark">Get a Free Consultation</a>
                </div>
            </div>
        </section>
    
    </>
  );
}
