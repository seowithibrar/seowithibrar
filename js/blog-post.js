/**
 * Blog Post Template — JavaScript
 * SEO With Ibrar
 * Handles: reading progress, TOC highlighting, FAQ accordion,
 * table filters, smooth scroll, and mobile TOC toggle.
 */
document.addEventListener('DOMContentLoaded', () => {
  /* ==========================================
     1. READING PROGRESS BAR
     ========================================== */
  const progressBar = document.getElementById('bp-progress');
  if (progressBar) {
    const updateProgress = () => {
      const scrollTop = window.scrollY;
      const docHeight = document.documentElement.scrollHeight - window.innerHeight;
      const progress = docHeight > 0 ? (scrollTop / docHeight) * 100 : 0;
      progressBar.style.width = progress + '%';
    };
    window.addEventListener('scroll', updateProgress, { passive: true });
    updateProgress();
  }

  /* ==========================================
     2. TABLE OF CONTENTS — ACTIVE HIGHLIGHTING
     ========================================== */
  const tocLinks = document.querySelectorAll('.bp-toc-list a');
  const sections = [];

  tocLinks.forEach(link => {
    const id = link.getAttribute('href');
    if (id && id.startsWith('#')) {
      const section = document.getElementById(id.substring(1));
      if (section) {
        sections.push({ el: section, link: link });
      }
    }
  });

  if (sections.length > 0) {
    const observerOptions = {
      root: null,
      rootMargin: '-80px 0px -60% 0px',
      threshold: 0
    };

    const tocObserver = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          // Remove active from all links
          tocLinks.forEach(l => l.classList.remove('active'));
          // Set active on matching links (both sidebar and mobile)
          const targetId = entry.target.id;
          document.querySelectorAll(`.bp-toc-list a[href="#${targetId}"]`).forEach(l => {
            l.classList.add('active');
          });
        }
      });
    }, observerOptions);

    sections.forEach(s => tocObserver.observe(s.el));
  }

  /* ==========================================
     3. MOBILE TOC ACCORDION
     ========================================== */
  const tocToggle = document.getElementById('bp-toc-toggle');
  const tocContent = document.getElementById('bp-toc-content');

  if (tocToggle && tocContent) {
    tocToggle.addEventListener('click', () => {
      const isOpen = tocContent.classList.toggle('open');
      tocToggle.setAttribute('aria-expanded', isOpen);
    });
  }

  /* ==========================================
     4. FAQ ACCORDION
     ========================================== */
  const faqItems = document.querySelectorAll('.bp-faq-item');

  faqItems.forEach(item => {
    const button = item.querySelector('.bp-faq-question');
    const answer = item.querySelector('.bp-faq-answer');

    if (button && answer) {
      button.addEventListener('click', () => {
        const isOpen = item.classList.contains('open');

        // Close all others
        faqItems.forEach(other => {
          if (other !== item) {
            other.classList.remove('open');
            const otherBtn = other.querySelector('.bp-faq-question');
            const otherAnswer = other.querySelector('.bp-faq-answer');
            if (otherBtn) otherBtn.setAttribute('aria-expanded', 'false');
            if (otherAnswer) otherAnswer.style.maxHeight = '0';
          }
        });

        // Toggle current
        if (isOpen) {
          item.classList.remove('open');
          button.setAttribute('aria-expanded', 'false');
          answer.style.maxHeight = '0';
        } else {
          item.classList.add('open');
          button.setAttribute('aria-expanded', 'true');
          answer.style.maxHeight = answer.scrollHeight + 'px';
        }
      });
    }
  });

  /* ==========================================
     5. COMPARISON TABLE FILTERS
     ========================================== */
  const filterButtons = document.querySelectorAll('.bp-filter-btn');
  const tableRows = document.querySelectorAll('.bp-table tbody tr');

  filterButtons.forEach(btn => {
    btn.addEventListener('click', () => {
      // Update active state
      filterButtons.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');

      const filter = btn.getAttribute('data-filter');

      tableRows.forEach(row => {
        if (filter === 'all') {
          row.style.display = '';
        } else {
          const location = (row.getAttribute('data-location') || '').toLowerCase();
          const spec = (row.getAttribute('data-specialization') || '').toLowerCase();
          const match = location.includes(filter.toLowerCase()) ||
                        spec.includes(filter.toLowerCase());
          row.style.display = match ? '' : 'none';
        }
      });
    });
  });

  /* ==========================================
     6. SMOOTH SCROLL WITH HEADER OFFSET
     ========================================== */
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
      const targetId = this.getAttribute('href');
      if (targetId === '#') return;

      const target = document.querySelector(targetId);
      if (target) {
        e.preventDefault();
        const headerOffset = 80;
        const elementPosition = target.getBoundingClientRect().top;
        const offsetPosition = elementPosition + window.scrollY - headerOffset;

        window.scrollTo({
          top: offsetPosition,
          behavior: 'smooth'
        });

        // Close mobile TOC if open
        if (tocContent && tocContent.classList.contains('open')) {
          tocContent.classList.remove('open');
          if (tocToggle) tocToggle.setAttribute('aria-expanded', 'false');
        }
      }
    });
  });

  /* ==========================================
     7. FADE-IN ANIMATIONS
     ========================================== */
  const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  if (!prefersReducedMotion) {
    const fadeElements = document.querySelectorAll('.bp-fade-in');
    if (fadeElements.length > 0) {
      const fadeObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
          if (entry.isIntersecting) {
            entry.target.classList.add('visible');
            fadeObserver.unobserve(entry.target);
          }
        });
      }, {
        root: null,
        rootMargin: '0px',
        threshold: 0.1
      });

      fadeElements.forEach(el => fadeObserver.observe(el));
    }
  } else {
    // If reduced motion, make everything visible immediately
    document.querySelectorAll('.bp-fade-in').forEach(el => {
      el.classList.add('visible');
    });
  }
});
