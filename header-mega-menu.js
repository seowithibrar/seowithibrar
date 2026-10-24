/**
 * Header & Mega Menu Interactions
 * SEO With Ibrar Ahmad
 */
(function() {
  function initHeaderMegaMenu() {
    const header = document.getElementById('siteHeader');
    const servicesDropdown = document.getElementById('servicesDropdown');
    const mobileToggle = document.getElementById('mobileToggle') || document.getElementById('mobileToggleBtn');
    const mobileDrawer = document.getElementById('mobileDrawer');
    const closeDrawerBtn = document.getElementById('closeDrawerBtn');

    // Sticky Scroll Shadow
    if (header) {
      window.addEventListener('scroll', function() {
        if (window.scrollY > 20) {
          header.classList.add('scrolled');
        } else {
          header.classList.remove('scrolled');
        }
      }, { passive: true });
    }

    // Click and touch support for Services Mega Menu
    if (servicesDropdown) {
      const toggleLink = servicesDropdown.querySelector('a.nav-link');
      if (toggleLink) {
        toggleLink.addEventListener('click', function(e) {
          e.preventDefault();
          servicesDropdown.classList.toggle('is-open');
          const isExpanded = servicesDropdown.classList.contains('is-open');
          toggleLink.setAttribute('aria-expanded', isExpanded ? 'true' : 'false');
        });
      }

      // Close on outside click
      document.addEventListener('click', function(e) {
        if (!servicesDropdown.contains(e.target)) {
          servicesDropdown.classList.remove('is-open');
          if (toggleLink) toggleLink.setAttribute('aria-expanded', 'false');
        }
      });
    }

    // Mobile Drawer Open/Close
    if (mobileToggle && mobileDrawer) {
      mobileToggle.addEventListener('click', function(e) {
        e.preventDefault();
        mobileDrawer.classList.add('active');
        document.body.style.overflow = 'hidden';
      });
    }

    if (closeDrawerBtn && mobileDrawer) {
      closeDrawerBtn.addEventListener('click', function(e) {
        e.preventDefault();
        mobileDrawer.classList.remove('active');
        const consultModal = document.getElementById('consultModal');
        const isModalActive = consultModal && consultModal.classList.contains('active');
        if (!isModalActive) {
          document.body.style.overflow = '';
        }
      });
    }

    // Close drawer when clicking backdrop
    if (mobileDrawer) {
      mobileDrawer.addEventListener('click', function(e) {
        if (e.target === mobileDrawer) {
          mobileDrawer.classList.remove('active');
          document.body.style.overflow = '';
        }
      });
    }
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initHeaderMegaMenu);
  } else {
    initHeaderMegaMenu();
  }
})();
