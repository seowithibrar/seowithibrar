# SEO With Ibrar — Homepage Build Prompt
(Reference layout: deeprahulseo.com · Target: seowithibrar.com)

## HOW TO USE
1. Paste everything inside the PROMPT block into Claude (or Claude Code).
2. Attach 3-4 full-page screenshots of https://deeprahulseo.com/ (hero, services grid, case studies, FAQ). The page text gave me the structure; the exact colors, fonts and spacing can only be matched accurately from screenshots.
3. Replace every [BRACKET] value with your real data before publishing.

---

## PROMPT

```
<role>
You are a senior front-end designer and WordPress/Elementor developer. You build conversion-focused personal-brand websites for SEO consultants.
</role>

<task>
Build the complete homepage of seowithibrar.com as ONE self-contained file (HTML + CSS + JS in a single file, no external dependencies except Google Fonts). Replicate the layout, section order, component types, and interaction patterns of the attached reference screenshots (deeprahulseo.com) exactly. Do NOT copy any of Deep Rahul's text, logo, photos, or numbers. All copy comes from the CONTENT section below.
</task>

<context>
- Owner: Ibrar Ahmad, SEO consultant, Lahore, Pakistan. Brand: "SEO With Ibrar".
- Positioning: solo specialist (not an agency), 5 years of SEO experience, 30+ client websites, focus on local SEO for education institutes, visa/immigration consultancies, modest fashion, and e-commerce.
- Also runs a YouTube channel (@seowithibrar) on Local SEO, AI automation, LinkedIn marketing.
- Goal of the page: get visitors to open the "Free Consultation" popup (primary CTA) or view the portfolio (secondary CTA).
- Output will later be converted to Elementor, so use clean semantic sections, one class per component, CSS variables for all colors/fonts/spacing.
</context>

<design_rules>
- Match the reference's color palette, font pairing, border radius, shadows, and section spacing from the screenshots. Extract them into CSS variables at :root (--bg, --surface, --text, --muted, --accent, --accent-2, --border, --radius, --font-display, --font-body). If a screenshot is missing, ask nothing: use a dark-neutral/accent-highlight scheme and keep every value in variables so it is easy to change.
- Section label pattern: small uppercase label with a leading dash ("— About Me"), then an H2 where 1-2 words are italic/accent-colored ("Turning Search Engines Into *Revenue Machines*").
- Cards: rounded corners, subtle border, hover lift (translateY -4px) and accent border glow.
- Numbered items use big "01 02 03" counters.
- Smooth scroll, fade-up on scroll (IntersectionObserver), count-up animation on stat numbers.
- Fully responsive: desktop 1200px container, tablet 2-col, mobile 1-col, hamburger menu under 900px. Test mentally at 375px.
- Accessibility: one H1, logical H2/H3, alt text on every image, visible focus states, contrast AA.
- Performance: no layout shift, lazy-load below-fold images, system-font fallback.
</design_rules>

<page_structure>
Build these sections in this exact order.

0. STICKY HEADER
   - Left: logo (placeholder "SEO With Ibrar" wordmark).
   - Center nav: Portfolio | SEO Service | [White Label SEO – optional] | [SEO Mock Interview – optional] | SEO Tools (dropdown: Robots.txt Generator, Schema Generator) | Blogs.
   - Each top-level item opens a MEGA-DROPDOWN panel on hover with: bold title, one-line description, a button, and an image placeholder on the right.
   - Right: "Contact Me" button that opens the consultation popup.
   - Mobile: hamburger opens full-screen menu with the same links and a Close button.

1. CONSULTATION POPUP (modal)
   - Badge "Free Consultation". Heading: "Let's Talk About Your *SEO Growth*".
   - Sub: "Choose how you'd like to connect. I respond within 24 hours, no sales pitch, just real strategy."
   - Three contact cards: Call, WhatsApp ("Usually replies within 1 hour"), Email.
   - Footer line: "Response within 24 hours · No commitment required".
   - Opens from every element with href="#open-consult". Closes on X, overlay click, Esc.

2. HERO (two columns)
   - Left: pill "Looking for Organic Growth?", "Hi, I'm" + H1 name, role line "SEO Consultant", paragraph with 2 bold phrases, two buttons (primary "Get Free Consultation →", secondary "View Portfolio").
   - Right: layered visual composition built in pure CSS/SVG:
     a) Live SERP card ("Page 1", two result rows with #1 / #2 badges).
     b) SEO Dashboard card with LIVE dot, 3 mini stat tiles, and a line/area chart (Clicks vs Impressions) with a "+X% in N months" chip.
     c) LLM Visibility card with 4 horizontal progress bars (ChatGPT, Gemini, Perplexity, Claude).
     d) GEO/AEO badge card ("A+ AI Search Ready") with tag chips: Structured Data, E-E-A-T, AEO, GEO.
     Cards float with slow looping animation.
   - Under hero: "Trusted by businesses in" row with country flags + a rating chip.

3. ABOUT
   - Left: portrait photo with floating badge ("5+ Years of Expertise").
   - Right: label "— About Me", H2, one paragraph, then 3 icon-feature rows (Results Over Rankings / Data-Driven Every Step / Built for Long-Term Growth), then two buttons.

4. RESULTS BY THE NUMBERS
   - Label, H2, 4 large stat tiles with count-up: years of experience, websites managed, client satisfaction, keywords in top positions. Each has a small caption.

5. SERVICES (9-card grid, 3x3)
   - Label "— What I Do", H2 with italic accent, intro paragraph.
   - Each card: number 01-09, H3, 2-line description, "Learn More →" link.
   - After the grid, two wide promo banners side by side: "SEO Mock Interview" (optional) and "Free SEO Tools".

6. PROVEN RESULTS
   - Label, H2, short intro.
   - Row of 4 big metric chips (value + label + context).
   - Row of 3 result cards with mini data tables (Industry title, 3 key/value rows, green "↑" footer).

7. CASE STUDIES
   - Label, H2, intro.
   - 3x2 grid of image cards: industry tag, one-line headline with metrics, arrow button.
   - Clicking a card opens a lightbox/modal: image, "Project Overview", "Key Objectives" list, and CTA "Book a Free Consultation →".

8. PROCESS (horizontal 5-step flow)
   - Label, H2, subline.
   - 5 numbered steps connected by a line/arrows; on mobile stack vertically.
   - CTA "Start the Process →" + microcopy "Free consultation · No commitment · Response within 24 hours".

9. TESTIMONIALS
   - Label, H2.
   - Left: summary card (big rating %, 5 stars, "Client Satisfaction", "View All Reviews" link).
   - Right: slider/grid of 4 testimonial cards (stars, quote, avatar initials, name, role · city).

10. VIDEO / SOCIAL INSIGHTS
   - Eyebrow "From YouTube" (use YouTube instead of Instagram), H2 "Real SEO Insights, Explained Simply", sub line.
   - 4 vertical video thumbnail cards with play icon and title; click opens a video lightbox (YouTube embed placeholder).
   - Button "See more on YouTube".

11. FAQ
   - Label "Common Questions", H2 "Things People Usually Ask Me", intro.
   - 10 accordion items (one open at a time, plus/minus icon).
   - Below: "Still have a question?" + "Book a free consultation" link.
   - Add FAQPage JSON-LD schema.

12. FINAL CTA
   - Label "— Let's Work Together", H2 "Ready to Build *Sustainable Search Growth?*", paragraph.
   - 4 check chips: Free Strategy Call, No Lock-ins, Custom Roadmap, Results-First.
   - Two buttons + microcopy + 3 contact links (Email, LinkedIn, Call).

13. FOOTER
   - Top bar: LinkedIn icon link, "All Rights Reserved", "Developed By Ibrar Ahmad", "Let's Talk" button.
   - "View More SEO Pages" 4-column link grid: SEO Services | Industry SEO | SEO Consultants | Location & Tools.
   - One-line brand description.

14. COOKIE BAR (bottom)
   - "Always on: Analytics", "Marketing", buttons "Reject All" and "Save Preferences".

15. STICKY MOBILE BAR
   - Small fixed bottom button "Book Free Call →" visible on mobile only, with a collapse (−) control.
</page_structure>

<content>
Use this copy. Items in [BRACKETS] are placeholders the owner will fill. NEVER invent statistics, client names, or testimonials: leave the placeholder visible.

META
- Title: Ibrar Ahmad | SEO Consultant in Lahore | 5+ Years of Experience
- Description: Hi, I am Ibrar Ahmad, an SEO consultant based in Lahore, Pakistan. I help education, visa, e-commerce and local businesses grow with data-driven SEO. Book a free consultation.

HERO
- Pill: Looking for Organic Growth?
- H1: Ibrar Ahmad
- Role: SEO Consultant
- Paragraph: I turn **organic search** into your most powerful revenue channel by combining technical precision, content strategy, and data-driven decisions to deliver **rankings that last**.
- Buttons: Get Free Consultation → / View Portfolio
- Dashboard stats: Websites [30+] · Keywords Top 3 [VERIFY] · Best Traffic Growth [VERIFY]
- Chart chip: [+X% in N months]
- Trusted-by countries: [Pakistan, UK, UAE, USA, Canada, Australia – keep only real ones]

ABOUT
- Floating badge: 5+ Years of Expertise
- H2: Turning Search Engines Into *Revenue Machines*
- Paragraph: I'm Ibrar Ahmad, an SEO consultant based in Lahore with 5 years of hands-on experience. I work as a solo specialist, with a small team of interns supporting execution, and manage 30+ client websites across education, visa and immigration, modest fashion, and e-commerce. I treat every project like my own business.
- Features:
  1. Results Over Rankings: I focus on qualified traffic, leads, and revenue, not vanity metrics.
  2. Data-Driven Every Step: Every strategy is backed by GA4, GSC, and competitive research.
  3. Built for Long-Term Growth: What I build today keeps delivering organic visibility for years.

STATS (4 tiles): 5+ Years of Experience · 30+ Websites Managed · [VERIFY]% Client Satisfaction · [VERIFY] Keywords in Top 3

SERVICES (9)
01 SEO Strategy & Growth Planning — Custom roadmaps built around keyword gaps, competitor analysis, and ROI potential, tailored to your business goals.
02 Technical SEO & Site Audits — Crawlability, Core Web Vitals, schema, indexing fixes, speed, migrations, and in-depth audits.
03 Keyword Research & Mapping — Intent, volume, difficulty, and opportunity mapped to the right pages.
04 On-Page SEO Optimisation — Titles, meta, headings, internal links, images, and content improvements.
05 Content & AI Strategy — Topic clusters, pillar pages, and optimisation for Google plus AI search (ChatGPT, Perplexity, AI Overviews).
06 Local SEO — Google Business Profile, citations, map pack rankings, and location keywords for local businesses.
07 eCommerce & International SEO — Product and category SEO, marketplace visibility, hreflang, and multi-country targeting.
08 Link Building & Digital PR — White-hat backlinks through guest posts, outreach, and editorial placements.
09 Data, Tracking & Reporting — GA4, GSC, GTM, and Looker Studio dashboards with real growth metrics.
Banners: "For SEO Job Seekers — SEO Mock Interview" [optional, remove if not offered] · "Free SEO Tools — Robots.txt & Schema Generator" [or other tool names]

PROVEN RESULTS
- H2: Real Numbers. *Real Growth.*
- Intro: Real results for real clients using ethical, data-driven SEO.
- 4 metric chips and 3 detail cards: [fill from real GSC screenshots: education, visa/immigration, modest fashion, e-commerce]

CASE STUDIES (6 cards): [Industry tag] + [headline with real GSC metrics]. Suggested verticals: Education Institute, Visa Consultancy, Modest Fashion, E-Commerce, Local Service, [other].

PROCESS (5 steps)
01 Free Consultation — We discuss your business, goals & current SEO situation.
02 SEO Audit & Research — Technical audit, keyword research & competitor mapping.
03 Strategy & Roadmap — Custom SEO plan with priorities, timelines & KPIs.
04 Execution & Optimisation — Technical fixes, content, on-page SEO & link building, all live.
05 Track, Report & Scale — Monthly GSC reports & continuous optimisation for compounding growth.

TESTIMONIALS: 4 cards from real clients [NAME, ROLE · CITY, QUOTE]. Rating summary [VERIFY].

VIDEO SECTION: 4 titles from the @seowithibrar YouTube channel [pick: Local SEO, AI automation, LinkedIn marketing topics].

FAQ (write in my voice, plain English, no sales talk)
1. How long does SEO take to show results? — Small gains usually appear in 3-4 months, bigger growth in 6-12 months, and it compounds with consistency.
2. Do you guarantee #1 ranking on Google? — No. No honest SEO can. I focus on real strategy and steady growth.
3. How much does SEO cost? — Depends on site size, industry, and competition. Free call first, then a clear price with no hidden charges.
4. Do you only work with big companies? — No. Clients range from local institutes and consultancies to e-commerce brands.
5. Will I get regular updates? — Yes, monthly Google Search Console reports with real numbers.
6. What services are included? — Technical, on-page, content, link building, local SEO, and AI search optimisation (AEO/GEO), based on what your site needs.
7. Can SEO help my business get more customers? — Yes. It brings people already searching for what you offer, leading to more calls, leads, and sales.
8. Do I need a long-term contract? — No. Start small and continue if you like the results.
9. What if my website already has SEO problems? — I start with a full audit, then fix issues step by step.
10. How do I get started? — Book a free 30-minute call. No pressure, no obligation.

FINAL CTA
- H2: Ready to Build *Sustainable Search Growth?*
- Paragraph: Let's build an SEO strategy that turns Google into your biggest lead generator. Book a free 30-minute consultation and get a custom growth roadmap.
- Contacts: [EMAIL] · [LINKEDIN URL] · [PHONE/WHATSAPP]

FOOTER LINK GROUPS
- SEO Services: SEO Services, Local SEO, Technical SEO, On-Page SEO, Content SEO, Link Building, Shopify SEO
- Industry SEO: Education SEO, Visa & Immigration SEO, Modest Fashion / E-commerce SEO, Healthcare SEO [keep only pages that exist]
- SEO Consultants: SEO Consultant in Lahore, SEO Consultant Pakistan, SEO Consultant for Small Business [adjust]
- Location & Tools: SEO Services in Lahore, Karachi, Islamabad [adjust], Schema Generator, Robots.txt Generator
</content>

<constraints>
- MUST output a single file, complete, no truncation, no "rest remains the same".
- MUST keep section order and component types identical to the reference.
- MUST NOT reuse any Deep Rahul wording, images, logo, or numbers.
- MUST leave unverified numbers as visible [VERIFY] placeholders.
- MUST include: meta tags, Open Graph, Person + ProfessionalService + FAQPage JSON-LD, sitemap-friendly heading hierarchy.
- Only build what is listed. Do not add extra sections or features.
</constraints>

<success_criteria>
1. Side by side with the reference screenshots, the section order, grid layouts, card styles and popup behavior match.
2. All 15 sections render at 1440px, 768px, and 375px with no horizontal scroll.
3. Every CTA opens the consultation popup; accordion, mega-menu, case-study lightbox and count-up all work.
4. No copied text from deeprahulseo.com appears anywhere.
</success_criteria>
```

---

## FILL-IN CHECKLIST (before you run the prompt)
- [ ] Logo + portrait photo
- [ ] Real stats (keywords in top 3, satisfaction %, best traffic growth)
- [ ] 6 real case studies with GSC screenshots (get client permission)
- [ ] 4 real testimonials
- [ ] Email, WhatsApp/phone, LinkedIn URL
- [ ] Decide: keep or remove White Label SEO and SEO Mock Interview
- [ ] 4 YouTube video titles + thumbnails
- [ ] Footer links that point to pages that actually exist
