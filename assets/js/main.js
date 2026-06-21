document.addEventListener("DOMContentLoaded", () => {
  // ── NAVBAR: Active page highlight ──
  (function () {
    const currentPath = window.location.pathname;
    document.querySelectorAll(".nav-link").forEach(link => {
      const href = link.getAttribute("href");
      if (href && currentPath.includes(href.replace("/index.html", ""))) {
        link.classList.add("current");
      }
    });

    // Homepage special case
    if (currentPath === "/" || currentPath.endsWith("index.html")) {
      document.querySelector('.nav-link[href="/index.html"]')
        ?.classList.add("current");
    }
  })();

  // ── HAMBURGER MENU TOGGLE ──
  const hamburger = document.getElementById("hamburger");
  const mobileMenu = document.getElementById("mobile-menu");

  hamburger?.addEventListener("click", () => {
    hamburger.classList.toggle("open");
    mobileMenu.classList.toggle("open");
  });

  // Close on outside click
  document.addEventListener("click", (e) => {
    if (!hamburger?.contains(e.target) && 
        !mobileMenu?.contains(e.target)) {
      hamburger?.classList.remove("open");
      mobileMenu?.classList.remove("open");
    }
  });

  // Close on resize
  window.addEventListener("resize", () => {
    if (window.innerWidth > 1024) {
      hamburger?.classList.remove("open");
      mobileMenu?.classList.remove("open");
    }
  });

  // ── PORTFOLIO FILTER BEHAVIOR ──
  const filterBtns = document.querySelectorAll(".filter-btn");
  const portfolioCards = document.querySelectorAll(".portfolio-card");

  filterBtns.forEach(btn => {
    btn.addEventListener("click", () => {
      filterBtns.forEach(b => b.classList.remove("active"));
      btn.classList.add("active");

      const filter = btn.getAttribute("data-filter");
      portfolioCards.forEach(card => {
        if (filter === "all" || 
            card.getAttribute("data-category") === filter) {
          card.classList.remove("hidden");
        } else {
          card.classList.add("hidden");
        }
      });
    });
  });

  // ── FAQ ACCORDION ──
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
            const otherAnswer = otherItem.querySelector('.faq-answer');
            if (otherAnswer) otherAnswer.style.maxHeight = null;
          }
        });

        // Toggle selected item
        if (isActive) {
          item.classList.remove('active');
          answer.style.maxHeight = null;
        } else {
          item.classList.add('active');
          answer.style.maxHeight = (answer.scrollHeight + 24) + 'px';
        }
      });
    }
  });

  // ── CONSULTATION MODAL ──
  const modal = document.getElementById('contact-modal');
  const openModalBtns = document.querySelectorAll('.open-modal-btn');
  const closeModalBtn = document.getElementById('modal-close');
  const consultationForm = document.getElementById('consultation-form');

  const openModal = () => {
    if (modal) {
      modal.classList.add('open');
      document.body.style.overflow = 'hidden';
    }
  };

  const closeModal = () => {
    if (modal) {
      modal.classList.remove('open');
      document.body.style.overflow = '';
    }
  };

  openModalBtns.forEach(btn => btn.addEventListener('click', openModal));
  if (closeModalBtn) closeModalBtn.addEventListener('click', closeModal);

  if (modal) {
    modal.addEventListener('click', (e) => {
      if (e.target === modal) {
        closeModal();
      }
    });
  }

  // Handle Form Submission
  if (consultationForm) {
    consultationForm.addEventListener('submit', (e) => {
      e.preventDefault();
      
      const name = document.getElementById('form-name')?.value || "Guest";
      const email = document.getElementById('form-email')?.value || "";

      const submitBtn = consultationForm.querySelector('button[type="submit"]');
      if (submitBtn) {
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
      }
    });
  }

  // Handle Embedded Form Submission
  const embeddedForm = document.getElementById('embedded-consultation-form');
  if (embeddedForm) {
    embeddedForm.addEventListener('submit', (e) => {
      e.preventDefault();
      
      const name = document.getElementById('embed-name')?.value || "Guest";
      const email = document.getElementById('embed-email')?.value || "";

      const submitBtn = embeddedForm.querySelector('button[type="submit"]');
      if (submitBtn) {
        const originalText = submitBtn.innerText;
        submitBtn.innerText = 'Sending Request...';
        submitBtn.disabled = true;

        setTimeout(() => {
          alert(`Thank you, ${name}! Your request has been received. Ibrar will get back to you shortly at ${email}.`);
          embeddedForm.reset();
          submitBtn.innerText = originalText;
          submitBtn.disabled = false;
        }, 1500);
      }
    });
  }

  // ── LIVE SEO SIMULATOR ──
  const simRunBtn = document.getElementById('sim-run-btn');
  if (simRunBtn) {
    simRunBtn.addEventListener('click', () => {
      const urlInput = document.getElementById('sim-url');
      const keywordSelect = document.getElementById('sim-keyword');
      const terminal = document.getElementById('sim-terminal');
      const logs = document.getElementById('sim-logs');
      const results = document.getElementById('sim-results');

      if (!urlInput || !urlInput.value) {
        alert("Please enter your institute's URL to run the scan.");
        return;
      }

      simRunBtn.disabled = true;
      simRunBtn.innerText = "Scanning...";
      
      if (results) results.style.display = 'none';
      if (terminal) terminal.style.display = 'block';
      if (logs) logs.innerHTML = '';

      const targetUrl = new URL(urlInput.value.startsWith('http') ? urlInput.value : 'https://' + urlInput.value).hostname;
      const keyword = keywordSelect ? keywordSelect.value : "";

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
          if (logLine.innerText.includes('[OK]')) {
            logLine.innerHTML = logLine.innerHTML.replace('[OK]', '<span style="color: #39e07b;">[OK]</span>');
          }
          if (logLine.innerText.includes('[MISSING]')) {
            logLine.innerHTML = logLine.innerHTML.replace('[MISSING]', '<span style="color: #EF4444;">[MISSING]</span>');
          }
          
          if (logs) logs.appendChild(logLine);
          stepIndex++;
        } else {
          clearInterval(interval);
          setTimeout(() => {
            if (terminal) terminal.style.display = 'none';
            if (results) results.style.display = 'block';
            simRunBtn.disabled = false;
            simRunBtn.innerText = "Run Live Scan";
            
            const scoreVal = document.getElementById('sim-score');
            if (scoreVal) {
              const randomScore = Math.floor(Math.random() * (96 - 88 + 1)) + 88;
              scoreVal.innerText = `${randomScore}/100`;
            }
          }, 800);
        }
      }, 700);
    });
  }
});
