document.addEventListener('DOMContentLoaded', () => {
  // Initialize Lucide Icons
  if (typeof lucide !== 'undefined') {
    lucide.createIcons();
  }

  // --- HEADER SCROLL ACTION ---
  const header = document.getElementById('header');
  if (header) {
    window.addEventListener('scroll', () => {
      if (window.scrollY > 50) {
        header.classList.add('scrolled');
      } else {
        header.classList.remove('scrolled');
      }
    });
  }

  // --- HAMBURGER DRAWER ---
  const hamburger = document.getElementById('hamburger');
  const navLinks = document.getElementById('nav-links');
  
  if (hamburger && navLinks) {
    hamburger.addEventListener('click', (e) => {
      e.stopPropagation();
      navLinks.classList.toggle('open');
      const isOpened = navLinks.classList.contains('open');
      hamburger.innerHTML = isOpened ? '<i data-lucide="x"></i>' : '<i data-lucide="menu"></i>';
      lucide.createIcons();
    });

    // Close menu when clicking outside
    document.addEventListener('click', (e) => {
      if (navLinks.classList.contains('open') && !navLinks.contains(e.target) && !hamburger.contains(e.target)) {
        navLinks.classList.remove('open');
        hamburger.innerHTML = '<i data-lucide="menu"></i>';
        lucide.createIcons();
      }
    });

    // Close menu on link click
    navLinks.querySelectorAll('a').forEach(link => {
      link.addEventListener('click', () => {
        navLinks.classList.remove('open');
        hamburger.innerHTML = '<i data-lucide="menu"></i>';
        lucide.createIcons();
      });
    });
  }

  // --- CONSULTATION MODAL ---
  const modal = document.getElementById('contact-modal') || document.getElementById('contactModal');
  const openModalBtns = document.querySelectorAll('.open-modal-btn');
  const closeModalBtn = document.getElementById('modal-close') || (document.getElementById('contactModal') ? document.querySelector('#contactModal .modal-close') : null);
  const consultationForm = document.getElementById('consultation-form') || document.getElementById('modalForm');

  const openModal = () => {
    if (modal) {
      modal.classList.add('open');
      document.body.style.overflow = 'hidden'; // Stop background scrolling
    }
  };

  const closeModal = () => {
    if (modal) {
      modal.classList.remove('open');
      document.body.style.overflow = ''; // Resume scrolling
    }
  };

  openModalBtns.forEach(btn => btn.addEventListener('click', openModal));
  if (closeModalBtn) closeModalBtn.addEventListener('click', closeModal);

  // Close modal on background click
  if (modal) {
    modal.addEventListener('click', (e) => {
      if (e.target === modal) {
        closeModal();
      }
    });
  }

  // Global toggle function for inline onclick handlers
  window.toggleModal = function(modalId) {
    let m = document.getElementById(modalId);
    if (!m) {
      if (modalId === 'contactModal') {
        m = document.getElementById('contact-modal');
      } else if (modalId === 'contact-modal') {
        m = document.getElementById('contactModal');
      }
    }
    if (m) {
      m.classList.toggle('open');
      if (m.classList.contains('open')) {
        document.body.style.overflow = 'hidden';
      } else {
        document.body.style.overflow = '';
      }
    }
  };

  // Handle Form Submission
  if (consultationForm) {
    consultationForm.addEventListener('submit', (e) => {
      e.preventDefault();
      
      // Select input elements dynamically from the form
      const nameInput = consultationForm.querySelector('input[type="text"]') || document.getElementById('form-name');
      const emailInput = consultationForm.querySelector('input[type="email"]') || document.getElementById('form-email');
      const websiteInput = consultationForm.querySelector('input[type="url"]') || document.getElementById('form-website');
      const messageInput = consultationForm.querySelector('textarea') || document.getElementById('form-message');

      const name = nameInput ? nameInput.value : '';
      const email = emailInput ? emailInput.value : '';
      const website = websiteInput ? websiteInput.value : '';
      const message = messageInput ? messageInput.value : '';

      // Mock submitting states
      const submitBtn = consultationForm.querySelector('button[type="submit"]');
      const originalText = submitBtn.innerText;
      submitBtn.innerText = 'Sending Request...';
      submitBtn.disabled = true;

      setTimeout(() => {
        alert(`Thank you, ${name}! Your request has been received. Ibrar will get back to you shortly at ${email}.`);
        consultationForm.reset();
        submitBtn.innerText = originalText;
        submitBtn.disabled = false;
        closeModal();
      }, 1500);
    });
  }

  // Handle Embedded Form Submission
  const embeddedForm = document.getElementById('embedded-consultation-form');
  if (embeddedForm) {
    embeddedForm.addEventListener('submit', (e) => {
      e.preventDefault();
      
      const name = document.getElementById('embed-name').value;
      const email = document.getElementById('embed-email').value;

      const submitBtn = embeddedForm.querySelector('button[type="submit"]');
      const originalText = submitBtn.innerText;
      submitBtn.innerText = 'Sending Request...';
      submitBtn.disabled = true;

      setTimeout(() => {
        alert(`Thank you, ${name}! Your request has been received. Ibrar will get back to you shortly at ${email}.`);
        embeddedForm.reset();
        submitBtn.innerText = originalText;
        submitBtn.disabled = false;
      }, 1500);
    });
  }

  // --- FAQ ACCORDION ---
  const faqItems = document.querySelectorAll('.faq-item');
  faqItems.forEach(item => {
    const question = item.querySelector('.faq-question');
    const answer = item.querySelector('.faq-answer');

    if (question && answer) {
      question.addEventListener('click', () => {
        const isActive = item.classList.contains('active');
        
        // Close other open FAQ items
        faqItems.forEach(otherItem => {
          if (otherItem !== item && otherItem.classList.contains('active')) {
            otherItem.classList.remove('active');
            otherItem.querySelector('.faq-answer').style.maxHeight = null;
          }
        });

        // Toggle selected item
        if (isActive) {
          item.classList.remove('active');
          answer.style.maxHeight = null;
        } else {
          item.classList.add('active');
          // Add extra padding-bottom size
          answer.style.maxHeight = (answer.scrollHeight + 24) + 'px';
        }
      });
    }
  });

  // --- SCROLL REVEAL INTERSECTION OBSERVER ---
  const revealElements = document.querySelectorAll('.reveal');
  
  if ('IntersectionObserver' in window && revealElements.length > 0) {
    const observerOptions = {
      root: null,
      rootMargin: '0px',
      threshold: 0.15
    };

    const revealObserver = new IntersectionObserver((entries, observer) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('active');
          // Once animated, stop observing this element
          observer.unobserve(entry.target);
        }
      });
    }, observerOptions);

    revealElements.forEach(element => {
      revealObserver.observe(element);
    });
  } else {
    // Fallback if IntersectionObserver is not supported
    revealElements.forEach(element => {
      element.classList.add('active');
    });
  }

  // --- LIVE SEO SIMULATOR ---
  const simRunBtn = document.getElementById('sim-run-btn');
  if (simRunBtn) {
    simRunBtn.addEventListener('click', () => {
      const urlInput = document.getElementById('sim-url');
      const keywordSelect = document.getElementById('sim-keyword');
      const terminal = document.getElementById('sim-terminal');
      const logs = document.getElementById('sim-logs');
      const results = document.getElementById('sim-results');

      if (!urlInput.value) {
        alert("Please enter your institute's URL to run the scan.");
        return;
      }

      // Disable button
      simRunBtn.disabled = true;
      simRunBtn.innerText = "Scanning...";
      
      // Reset & show terminal
      results.style.display = 'none';
      terminal.style.display = 'block';
      logs.innerHTML = '';

      const targetUrl = new URL(urlInput.value.startsWith('http') ? urlInput.value : 'https://' + urlInput.value).hostname;
      const keyword = keywordSelect.value;

      const scanSteps = [
        `> Initializing crawler for ${targetUrl}...`,
        `> Fetching HTTPS headers and SSL status... [OK]`,
        `> Analyzing Core Web Vitals on cellular networks...`,
        `> Checking JSON-LD Course and EducationalOrganization Schemas... [MISSING]`,
        `> Mapping local citations against keyword: "${keyword}"...`,
        `> Evaluating domain authority and backlink profile...`,
        `> Generating final performance metrics...`
      ];

      let stepIndex = 0;

      const interval = setInterval(() => {
        if (stepIndex < scanSteps.length) {
          const logLine = document.createElement('div');
          logLine.innerText = scanSteps[stepIndex];
          // Add some color variance
          if (logLine.innerText.includes('[OK]')) logLine.innerHTML = logLine.innerHTML.replace('[OK]', '<span style="color: #10B981;">[OK]</span>');
          if (logLine.innerText.includes('[MISSING]')) logLine.innerHTML = logLine.innerHTML.replace('[MISSING]', '<span style="color: #EF4444;">[MISSING]</span>');
          
          logs.appendChild(logLine);
          stepIndex++;
        } else {
          clearInterval(interval);
          setTimeout(() => {
            terminal.style.display = 'none';
            results.style.display = 'block';
            simRunBtn.disabled = false;
            simRunBtn.innerText = "Run Live Scan";
            
            // Generate a random speed score between 88 and 96
            const randomScore = Math.floor(Math.random() * (96 - 88 + 1)) + 88;
            document.getElementById('sim-score').innerText = `${randomScore}/100`;
          }, 800); // Wait a bit before showing results
        }
      }, 700); // 700ms per simulated step
    });
  }
});
