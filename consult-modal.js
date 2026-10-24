/**
 * Consultation Popup Modal Controller
 * SEO With Ibrar Ahmad
 */
(function() {
  // Ensure styles are loaded
  function ensureStyles() {
    if (!document.querySelector('link[href*="consult-modal.css"]')) {
      const link = document.createElement('link');
      link.rel = 'stylesheet';
      link.href = 'consult-modal.css';
      document.head.appendChild(link);
    }
  }

  // Create Modal DOM structure if not already present
  function ensureModalDOM() {
    if (document.getElementById('consultModal')) return;

    const modalHTML = `
      <div class="consult-modal-overlay" id="consultModal" role="dialog" aria-modal="true" aria-labelledby="consultModalHeading">
        <div class="consult-modal-dialog">
          <button class="consult-modal-close" onclick="closeConsultModal()" aria-label="Close Free Consultation Dialog">
            <svg width="11" height="11" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round"><line x1="18" y1="6" x2="6" y2="18"></line><line x1="6" y1="6" x2="18" y2="18"></line></svg>
            <span>CLOSE</span>
          </button>

          <div class="consult-modal-grid">
            <div class="consult-modal-content">
              <div class="consult-kicker">FREE CONSULTATION</div>
              <h2 class="consult-heading" id="consultModalHeading">
                Let's Talk About<br>
                Your <span class="text-accent-lime">SEO Growth</span>
              </h2>
              <p class="consult-subtext">
                Choose how you'd like to connect. I respond within 24 hours — no sales pitch, just real strategy.
              </p>

              <div class="consult-channels-list">
                <!-- Call Me -->
                <a href="tel:+923174835008" class="consult-channel-card" aria-label="Call Ibrar Ahmad directly">
                  <div class="consult-channel-left">
                    <div class="consult-channel-icon icon-phone">
                      <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                        <path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"></path>
                      </svg>
                    </div>
                    <div class="consult-channel-info">
                      <div class="consult-channel-title">
                        Call Me <span class="consult-channel-tag">(Pakistan &amp; Global)</span>
                      </div>
                      <div class="consult-channel-detail">+92-3174835008</div>
                    </div>
                  </div>
                  <div class="consult-channel-arrow">
                    <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
                  </div>
                </a>

                <!-- WhatsApp -->
                <a href="https://wa.me/923174835008" target="_blank" rel="noopener noreferrer" class="consult-channel-card" aria-label="Chat with Ibrar on WhatsApp">
                  <div class="consult-channel-left">
                    <div class="consult-channel-icon icon-whatsapp">
                      <svg width="22" height="22" viewBox="0 0 24 24" fill="currentColor">
                        <path d="M.057 24l1.687-6.163c-1.041-1.804-1.588-3.849-1.587-5.946.003-6.556 5.338-11.891 11.893-11.891 3.181.001 6.167 1.24 8.413 3.488 2.245 2.248 3.481 5.236 3.48 8.414-.003 6.557-5.338 11.892-11.893 11.892-1.99-.001-3.951-.5-5.688-1.448l-6.305 1.654zm6.597-3.807c1.676.995 3.276 1.591 5.392 1.592 5.448 0 9.886-4.434 9.889-9.885.002-5.462-4.415-9.89-9.881-9.892-5.452 0-9.887 4.434-9.889 9.884-.001 2.225.651 3.891 1.746 5.634l-.999 3.648 3.742-.981zm11.387-5.464c-.074-.124-.272-.198-.57-.347-.297-.149-1.758-.868-2.031-.967-.272-.099-.47-.149-.669.149-.198.297-.768.967-.941 1.165-.173.198-.347.223-.644.074-.297-.149-1.255-.462-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.297-.347.446-.521.151-.172.2-.296.3-.495.099-.198.05-.372-.025-.521-.075-.148-.669-1.611-.916-2.206-.242-.579-.487-.501-.669-.51l-.57-.01c-.198 0-.52.074-.792.372s-1.04 1.016-1.04 2.479 1.065 2.876 1.213 3.074c.149.198 2.095 3.2 5.076 4.487.709.306 1.263.489 1.694.626.712.226 1.36.194 1.872.118.571-.085 1.758-.719 2.006-1.413.248-.695.248-1.29.173-1.414z"/>
                      </svg>
                    </div>
                    <div class="consult-channel-info">
                      <div class="consult-channel-title">Chat on WhatsApp</div>
                      <div class="consult-channel-detail">Usually replies within 1 hour</div>
                    </div>
                  </div>
                  <div class="consult-channel-arrow">
                    <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
                  </div>
                </a>

                <!-- Email -->
                <a href="mailto:seowithibrar@gmail.com" class="consult-channel-card" aria-label="Send email to Ibrar Ahmad">
                  <div class="consult-channel-left">
                    <div class="consult-channel-icon icon-email">
                      <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                        <path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"></path>
                        <polyline points="22,6 12,13 2,6"></polyline>
                      </svg>
                    </div>
                    <div class="consult-channel-info">
                      <div class="consult-channel-title">Send Me an Email</div>
                      <div class="consult-channel-detail">seowithibrar@gmail.com</div>
                    </div>
                  </div>
                  <div class="consult-channel-arrow">
                    <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
                  </div>
                </a>
              </div>

              <div class="consult-footer-note">
                Response within 24 hours · <span class="highlight-lime">No commitment required</span>
              </div>
            </div>

            <div class="consult-avatar-side">
              <img src="images/ibrar-consult-avatar.webp" alt="Ibrar Ahmad — SEO Consultant" class="consult-avatar-img" width="896" height="1200" loading="lazy">
            </div>
          </div>
        </div>
      </div>
    `;

    document.body.insertAdjacentHTML('beforeend', modalHTML);
  }

  // Global Controls
  window.openConsultModal = function(e) {
    if (e && e.preventDefault) e.preventDefault();
    ensureModalDOM();
    const modal = document.getElementById('consultModal');
    if (modal) {
      modal.classList.add('active');
      document.body.style.overflow = 'hidden';
    }
  };

  window.closeConsultModal = function() {
    const modal = document.getElementById('consultModal');
    if (modal) {
      modal.classList.remove('active');
      const lightbox = document.getElementById('caseLightbox');
      const mobileDrawer = document.getElementById('mobileDrawer');
      const isLightboxActive = lightbox && lightbox.classList.contains('active');
      const isDrawerActive = mobileDrawer && mobileDrawer.classList.contains('active');
      if (!isLightboxActive && !isDrawerActive) {
        document.body.style.overflow = '';
      }
    }
  };

  function initConsultModal() {
    ensureStyles();
    ensureModalDOM();

    // Event delegation for links pointing to #open-consult
    document.addEventListener('click', function(e) {
      const trigger = e.target.closest('a[href="#open-consult"], .btn-open-consult');
      if (trigger) {
        e.preventDefault();
        window.openConsultModal(e);
      }
    });

    // Close on overlay backdrop click
    document.addEventListener('click', function(e) {
      const modal = document.getElementById('consultModal');
      if (modal && e.target === modal) {
        window.closeConsultModal();
      }
    });

    // Close on Escape key
    window.addEventListener('keydown', function(e) {
      if (e.key === 'Escape') {
        window.closeConsultModal();
      }
    });

    // Auto open if URL has #open-consult
    if (window.location.hash === '#open-consult') {
      setTimeout(window.openConsultModal, 200);
    }
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initConsultModal);
  } else {
    initConsultModal();
  }
})();
