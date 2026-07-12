<?php
// Simple PHP logic to demonstrate it's a PHP file
$pageTitle = "Animated Professional Landing Page";
$currentYear = date('Y');
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title><?php echo $pageTitle; ?></title>
    
    <!-- Load Inter Font -->
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&display=swap" rel="stylesheet">
    
    <!-- Animate.css for professional animations -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/animate.css/4.1.1/animate.min.css"/>
    
    <style>
        :root {
            --primary-font: 'Inter', sans-serif;
            --color-bg: #0f172a;
            --color-surface: #1e293b;
            --color-text-main: #f8fafc;
            --color-text-muted: #94a3b8;
            --color-accent: #3b82f6;
            --container-width: 1200px;
        }

        * { box-sizing: border-box; }
        
        body {
            font-family: var(--primary-font);
            margin: 0;
            padding: 0;
            background: var(--color-bg);
            color: var(--color-text-main);
            overflow-x: hidden;
            line-height: 1.6;
        }

        .container {
            max-width: var(--container-width);
            margin: 0 auto;
            padding: 0 24px;
        }

        /* Hero Section */
        .hero {
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            text-align: center;
            position: relative;
            padding: 100px 0;
            overflow: hidden;
        }

        /* Background animated gradient blob */
        .blob {
            position: absolute;
            width: 600px;
            height: 600px;
            background: linear-gradient(135deg, #3b82f6 0%, #8b5cf6 100%);
            border-radius: 50%;
            filter: blur(100px);
            opacity: 0.2;
            animation: pulse-blob 8s infinite alternate ease-in-out;
            z-index: 0;
        }

        @keyframes pulse-blob {
            0% { transform: scale(1) translate(0, 0); }
            50% { transform: scale(1.2) translate(50px, -50px); }
            100% { transform: scale(1) translate(-50px, 50px); }
        }

        .hero-content {
            position: relative;
            z-index: 1;
            max-width: 800px;
        }

        h1 {
            font-size: clamp(3rem, 6vw, 5rem);
            font-weight: 800;
            margin-bottom: 24px;
            line-height: 1.1;
            background: linear-gradient(to right, #60a5fa, #c084fc);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }

        p.lead {
            font-size: 1.25rem;
            color: var(--color-text-muted);
            margin-bottom: 40px;
        }

        /* Animated Button */
        .btn {
            display: inline-flex;
            align-items: center;
            justify-content: center;
            padding: 16px 32px;
            background: var(--color-accent);
            color: white;
            text-decoration: none;
            font-weight: 600;
            border-radius: 50px;
            transition: all 0.3s ease;
            position: relative;
            overflow: hidden;
        }

        .btn::after {
            content: '';
            position: absolute;
            top: 50%;
            left: 50%;
            width: 300%;
            height: 300%;
            background: rgba(255,255,255,0.1);
            transform: translate(-50%, -50%) rotate(45deg) translateY(100%);
            transition: transform 0.5s ease;
        }

        .btn:hover {
            transform: translateY(-3px);
            box-shadow: 0 10px 25px -5px rgba(59, 130, 246, 0.5);
        }

        .btn:hover::after {
            transform: translate(-50%, -50%) rotate(45deg) translateY(0);
        }

        /* Features Grid */
        .features {
            padding: 100px 0;
            background: var(--color-surface);
        }

        .features-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 32px;
        }

        .feature-card {
            background: rgba(255,255,255,0.05);
            border: 1px solid rgba(255,255,255,0.1);
            padding: 40px;
            border-radius: 20px;
            transition: all 0.4s ease;
            opacity: 0;
            transform: translateY(30px);
        }

        .feature-card.visible {
            opacity: 1;
            transform: translateY(0);
        }

        .feature-card:hover {
            transform: translateY(-10px);
            background: rgba(255,255,255,0.08);
            border-color: rgba(255,255,255,0.2);
        }

        .icon-box {
            width: 60px;
            height: 60px;
            background: linear-gradient(135deg, #3b82f6, #8b5cf6);
            border-radius: 15px;
            margin-bottom: 24px;
            display: flex;
            align-items: center;
            justify-content: center;
        }

        h3 { font-size: 1.5rem; margin-bottom: 16px; }
        .feature-card p { color: var(--color-text-muted); }

        footer {
            text-align: center;
            padding: 40px 0;
            border-top: 1px solid rgba(255,255,255,0.1);
            color: var(--color-text-muted);
        }
    </style>
</head>
<body>

    <section class="hero">
        <div class="blob"></div>
        <div class="container hero-content">
            <h1 class="animate__animated animate__fadeInDown">Next-Gen Digital Experience</h1>
            <p class="lead animate__animated animate__fadeInUp animate__delay-1s">
                We craft beautiful, high-converting web applications with dynamic animations and flawless code structure.
            </p>
            <div class="animate__animated animate__zoomIn animate__delay-2s">
                <a href="#features" class="btn">Explore Features</a>
            </div>
        </div>
    </section>

    <section id="features" class="features">
        <div class="container">
            <div style="text-align: center; margin-bottom: 60px;">
                <h2 style="font-size: 2.5rem; margin-bottom: 16px;">Powerful Features</h2>
                <p style="color: var(--color-text-muted);">Built with performance and aesthetics in mind.</p>
            </div>

            <div class="features-grid">
                <div class="feature-card js-scroll">
                    <div class="icon-box">⚡</div>
                    <h3>Lightning Fast</h3>
                    <p>Optimized for Core Web Vitals to ensure instantaneous load times and smooth interactions.</p>
                </div>
                <div class="feature-card js-scroll" style="transition-delay: 0.1s;">
                    <div class="icon-box">🎨</div>
                    <h3>Premium Design</h3>
                    <p>Using modern aesthetics, glassmorphism, and responsive flexbox layouts.</p>
                </div>
                <div class="feature-card js-scroll" style="transition-delay: 0.2s;">
                    <div class="icon-box">📈</div>
                    <h3>SEO Optimized</h3>
                    <p>Clean semantic HTML and robust architecture to rank higher on search engines.</p>
                </div>
            </div>
        </div>
    </section>

    <footer>
        <div class="container">
            <p>&copy; <?php echo $currentYear; ?> <?php echo $pageTitle; ?>. All rights reserved.</p>
        </div>
    </footer>

    <!-- Intersection Observer for Scroll Animations -->
    <script>
        document.addEventListener("DOMContentLoaded", function() {
            const observerOptions = {
                root: null,
                rootMargin: '0px',
                threshold: 0.1
            };

            const observer = new IntersectionObserver((entries, observer) => {
                entries.forEach(entry => {
                    if (entry.isIntersecting) {
                        entry.target.classList.add('visible');
                        observer.unobserve(entry.target);
                    }
                });
            }, observerOptions);

            document.querySelectorAll('.js-scroll').forEach((el) => {
                observer.observe(el);
            });
        });
    </script>
</body>
</html>
