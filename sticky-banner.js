/**
 * Sticky Bottom SEO Review Banner Controller
 * Matches reference design 1:1 with floating bottom stickiness,
 * cutout avatar rising above top border, and consultation integration.
 */
(function() {
  const STORAGE_KEY = 'seo_sticky_banner_minimized';

  // Ensure CSS stylesheet is loaded
  function ensureStyles() {
    if (!document.querySelector('link[href*="sticky-banner.css"]')) {
      const link = document.createElement('link');
      link.rel = 'stylesheet';
      link.href = 'sticky-banner.css';
      document.head.appendChild(link);
    }
  }

  // Ensure DOM elements exist
  function ensureBannerDOM() {
    if (document.getElementById('seoStickyBannerWrap')) return;

    const bannerHTML = `
      <!-- Sticky Bottom SEO Review Banner -->
      <div class="seo-sticky-banner-wrap" id="seoStickyBannerWrap" role="complementary" aria-label="Free SEO Review Sticky Banner">
        <div class="seo-sticky-card">
          <!-- Left Text Content -->
          <div class="seo-sticky-content">
            <span class="seo-sticky-kicker">FREE SEO REVIEW</span>
            <h3 class="seo-sticky-heading">Not Sure Where Your SEO Stands?</h3>
            <p class="seo-sticky-subtext">Free, honest review — no pressure, no sales pitch.</p>
          </div>

          <!-- Middle / CTA Action Button -->
          <div class="seo-sticky-action-wrap">
            <a href="#open-consult" class="seo-sticky-btn" id="seoStickyBookBtn" aria-label="Book Free Call">
              <span>BOOK FREE CALL</span>
              <svg class="seo-sticky-arrow" width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
                <line x1="5" y1="12" x2="19" y2="12"></line>
                <polyline points="12 5 19 12 12 19"></polyline>
              </svg>
            </a>
          </div>

          <!-- Sticking Out Avatar Cutout -->
          <div class="seo-sticky-avatar-wrap" aria-hidden="true">
            <img src="images/ibrar-consult-avatar.webp" alt="Ibrar Ahmad — SEO Specialist" class="seo-sticky-avatar-img" width="896" height="1200" loading="eager" onerror="this.src='images/ibrar-consult-avatar.png'">
          </div>

          <!-- Minimize Button -->
          <button type="button" class="seo-sticky-toggle-btn" id="seoStickyToggleBtn" aria-label="Minimize Review Bar">
            <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round">
              <line x1="5" y1="12" x2="19" y2="12"></line>
            </svg>
          </button>
        </div>
      </div>

      <!-- Minimized Floating Trigger Bubble -->
      <button type="button" class="seo-sticky-bubble" id="seoStickyBubble" aria-label="Expand Free SEO Review Bar">
        <img src="images/ibrar-consult-avatar.webp" alt="Free Review" class="seo-bubble-avatar-img" width="38" height="38" loading="lazy" onerror="this.src='images/ibrar-consult-avatar.png'">
        <div class="seo-bubble-text">
          <span class="seo-bubble-kicker">FREE SEO REVIEW</span>
          <span class="seo-bubble-title">Book Free Call →</span>
        </div>
      </button>
    `;

    document.body.insertAdjacentHTML('beforeend', bannerHTML);
  }

  // Minimize banner
  window.minimizeStickyBanner = function() {
    const banner = document.getElementById('seoStickyBannerWrap');
    const bubble = document.getElementById('seoStickyBubble');
    if (banner) banner.classList.add('is-minimized');
    if (bubble) bubble.classList.add('is-visible');
    try {
      sessionStorage.setItem(STORAGE_KEY, 'true');
    } catch (e) {}
  };

  // Expand / restore banner
  window.expandStickyBanner = function() {
    const banner = document.getElementById('seoStickyBannerWrap');
    const bubble = document.getElementById('seoStickyBubble');
    if (banner) banner.classList.remove('is-minimized');
    if (bubble) bubble.classList.remove('is-visible');
    try {
      sessionStorage.removeItem(STORAGE_KEY);
    } catch (e) {}
  };

  window.toggleStickyBanner = function() {
    const banner = document.getElementById('seoStickyBannerWrap');
    if (banner && banner.classList.contains('is-minimized')) {
      window.expandStickyBanner();
    } else {
      window.minimizeStickyBanner();
    }
  };

  function initStickyBanner() {
    ensureStyles();
    ensureBannerDOM();

    // Check if previously minimized in this session
    try {
      if (sessionStorage.getItem(STORAGE_KEY) === 'true') {
        window.minimizeStickyBanner();
      }
    } catch (e) {}

    // Event listener for minimize button
    const toggleBtn = document.getElementById('seoStickyToggleBtn');
    if (toggleBtn) {
      toggleBtn.addEventListener('click', function(e) {
        e.stopPropagation();
        e.preventDefault();
        window.minimizeStickyBanner();
      });
    }

    // Event listener for floating restored bubble
    const bubble = document.getElementById('seoStickyBubble');
    if (bubble) {
      bubble.addEventListener('click', function(e) {
        e.preventDefault();
        window.expandStickyBanner();
      });
    }

    // Event listener for Book Free Call button
    const bookBtn = document.getElementById('seoStickyBookBtn');
    if (bookBtn) {
      bookBtn.addEventListener('click', function(e) {
        e.preventDefault();
        if (typeof window.openConsultModal === 'function') {
          window.openConsultModal(e);
        } else {
          // Fallback if modal script not ready: jump to contact
          window.location.href = 'contact.html';
        }
      });
    }
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initStickyBanner);
  } else {
    initStickyBanner();
  }
})();
