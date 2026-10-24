# Website SEO Audit Report: SEO With Ibrar

**Website**: [https://seowithibrar.com/](https://seowithibrar.com/)  
**Business**: SEO With Ibrar  
**Owner / Lead Consultant**: Ibrar Ahmad  
**Primary Location**: Lahore, Punjab, Pakistan  
**Audit Date**: October 2026  
**Auditor**: Senior Technical SEO & Structured Data Specialist  

---

## 1. Executive Summary

This comprehensive audit evaluated the technical infrastructure, on-page optimization, content hierarchy, structured data implementation, and performance characteristics of **SEO With Ibrar** ([https://seowithibrar.com/](https://seowithibrar.com/)).

Prior to optimization, the site presented several key opportunities for improvement:
1. **Metadata inconsistencies**: Several pages contained non-standard title lengths, generic portfolio titles, broken punctuation encoding (``), and meta descriptions with unverified marketing claims ("skyrocket", "dominate Google rankings").
2. **Heading architecture**: Multiple pages (notably `about.html`, `blog.html`, and `contact.html`) featured duplicate `<h1>` elements or secondary headings styled as primary headings, obscuring the primary topical entity.
3. **Structured data**: Pages lacked localized, interconnected JSON-LD graphs linking the primary `Organization`/`ProfessionalService` entity, founder `Person` entity, and individual service deliverables.
4. **Asset performance**: Images lacked explicit `width` and `height` attributes (causing Cumulative Layout Shift risks), 4 case study images on the homepage pointed to missing `.webp` URLs, and above-the-fold hero images were not prioritized for Largest Contentful Paint (LCP).
5. **Security & caching headers**: Static assets and security headers (`X-Content-Type-Options`, `X-Frame-Options`, `Referrer-Policy`, `Cache-Control`) were not explicitly defined in the platform configuration.

All issues have been systematically addressed directly in the codebase, tested, and validated.

---

## 2. Platform Architecture & Rendering Analysis

| Attribute | Details |
| :--- | :--- |
| **Framework** | Semantic HTML5, Vanilla Modern CSS, Vanilla JavaScript (ES6+) |
| **Rendering Method** | Static Site Generation (SSG) / Pre-rendered static files |
| **Hosting & CDN** | Vercel Global Edge Network |
| **URL Routing** | Clean URLs enabled (`cleanUrls: true`, `trailingSlash: false`) via `vercel.json` |
| **Total Public Pages** | 15 indexable pages (0 orphan pages) |
| **Canonical Scheme** | Strictly `https://seowithibrar.com/<slug>` (root `https://seowithibrar.com/`) |

---

## 3. Public Page Inventory

The public site comprises 15 crawlable, indexable URLs organized logically into core informational pages, regional localized services, and specialized vertical service offerings:

| URL Path | Template File | Intent & Topic Category | Target Geo / Audience |
| :--- | :--- | :--- | :--- |
| `/` | `index.html` | Core Homepage & Portfolio | Lahore / Global Businesses |
| `/about` | `about.html` | Founder Background & E-E-A-T | Nationwide / International |
| `/blog` | `blog.html` | Editorial & Technical Articles | Website Owners & Marketers |
| `/contact` | `contact.html` | Inquiry & Strategy Booking | Prospective Commercial Clients |
| `/top-seo-experts-in-pakistan` | `top-seo-experts-in-pakistan.html` | Industry Directory & Authority Guide | Pakistan Digital Market |
| `/seo-services-pakistan` | `seo-services-pakistan.html` | National Organic Search Services | Pakistan Businesses |
| `/seo-services-lahore` | `seo-services-lahore.html` | Localized Metropolitan Search | Lahore (DHA, Gulberg, Johar Town) |
| `/seo-services-karachi` | `seo-services-karachi.html` | Commercial & Corporate Search | Karachi (Clifton, DHA, Korangi) |
| `/seo-services-islamabad` | `seo-services-islamabad.html` | Corporate & Tech Hub SEO | Islamabad & Rawalpindi |
| `/seo-services-visa-consultancy` | `seo-services-visa-consultancy.html` | Niche Student / Immigration SEO | Visa & Immigration Firms |
| `/seo-services-visa-consultancy-karachi` | `seo-services-visa-consultancy-karachi.html` | Localized Visa Niche Search | Karachi Immigration Consultancies |
| `/seo-services-education` | `seo-services-education.html` | Education Admissions Search | Schools, Colleges, Academies |
| `/wordpress-design-services` | `wordpress-design-services.html` | High-Speed Custom Web Development | National / International |
| `/wordpress-design-services-for-visa-consultancy` | `wordpress-design-services-for-visa-consultancy.html` | Lead-Generation Niche Web Design | Visa Agencies |
| `/wordpress-design-services-for-education` | `wordpress-design-services-for-education.html` | Admissions-Focused Educational Web Design | Schools & Higher Ed |

---

## 4. Meta Title & Description Audit

### Title Tags
- **Standardized Format**: `[Primary Search Intent Keyword] | SEO With Ibrar` (or location-specific variant).
- **Length Compliance**: All 15 pages target between 41 and 62 characters (optimal display in desktop and mobile SERPs).
- **Brand Consistency**: The brand suffix `| SEO With Ibrar` is preserved on all pages for authoritative entity recognition.
- **Deduplication**: 100% of titles are unique across the entire site.

### Meta Descriptions
- **Length Compliance**: All descriptions range between 147 and 162 characters, avoiding snippet truncation.
- **Content Alignment**: Summarizes visible page content, primary deliverables, and clear call to action without unsupported guarantees.
- **Quality Standard**: Removed promotional hyperbole (e.g. "skyrocket", "dominate search engines", "rank #1").

---

## 5. Heading Structure & Semantic Hierarchy

- **Single Primary H1**: Each of the 15 indexable pages has exactly one `<h1>` tag clearly defining the subject matter.
  - Homepage: `SEO Consultant in Lahore & Digital Growth Strategist`
  - About: `About Ibrar Ahmad – SEO Consultant in Lahore, Pakistan`
  - Blog: `SEO Insights & Technical Strategy Blog`
  - Contact: `Contact SEO With Ibrar | Inquire About Services`
- **Accessible Order**: Heading levels descend logically from `<h1>` to `<h2>` (major thematic sections) and `<h3>` (sub-features, case studies, FAQ items).
- **Zero Hidden Headings**: No off-screen or keyword-stuffed heading tags are present.

---

## 6. Canonicalization, Crawling & Indexing

- **Self-Referential Canonicals**: Every page points to its preferred canonical HTTPS URL without `.html` extension and without trailing slashes.
- **Sitemap Consistency**: `sitemap.xml` strictly mirrors the 15 canonical URLs with exact protocol and casing.
- **Robots Directives**:
  - `robots.txt` allows all legitimate search crawlers.
  - Explicit `Disallow: /scratch/` and `Disallow: /docs/` directives protect internal utilities and markdown audit deliverables from indexing.
  - Canonical declaration links to `https://seowithibrar.com/sitemap.xml`.
- **Redirects Management**: `vercel.json` provides permanent 301 redirects for legacy URLs (`/portfolio`, `/portfolio.html`, etc.) directly to their active counterparts.

---

## 7. Structured Data (JSON-LD)

- **Syntax & Standards**: 100% valid JSON-LD graphs using `@graph` arrays where multiple entities interact.
- **Entity Identity**:
  - `ProfessionalService`: Represents `SEO With Ibrar` anchored at `https://seowithibrar.com/#business` with geographic service area in Lahore and verified contact details.
  - `Person`: Represents founder `Ibrar Ahmad` anchored at `https://seowithibrar.com/#person` with verified job title and official social media profiles (LinkedIn, YouTube).
  - `WebSite`: Anchored at `https://seowithibrar.com/#website`.
  - `Service`: Tailored to each individual service page, referencing `#business` as provider.
  - `BreadcrumbList`: Injected across all 14 subpages with logical hierarchical trail.
  - `FAQPage`: Present only on pages featuring visible accordions and genuine FAQ content.
  - `Article`: Present on editorial guide `top-seo-experts-in-pakistan.html`.

---

## 8. Image Optimization & Core Web Vitals (CWV)

- **Zero Broken Image Links**: Verified that all `<img>` tags point to existing local files in `images/`.
- **Aspect Ratio & Layout Shift**: Natural image dimensions (`width` and `height`) have been programmatically embedded into all image tags across all 15 templates to prevent Cumulative Layout Shift (CLS).
- **Asynchronous Decoding**: `decoding="async"` applied site-wide.
- **Loading Strategy**:
  - Above-the-fold hero images: `fetchpriority="high"` without lazy loading, maximizing Largest Contentful Paint (LCP) speed.
  - Below-the-fold images: `loading="lazy"` to minimize initial DOM execution weight and network payload.

---

## 9. Security & HTTP Header Hardening

Configured within `vercel.json`:
- `X-Content-Type-Options: nosniff` (MIME sniffing prevention)
- `X-Frame-Options: SAMEORIGIN` (Clickjacking defense)
- `Referrer-Policy: strict-origin-when-cross-origin` (Data privacy)
- `Permissions-Policy: camera=(), microphone=(), geolocation=()` (Feature restriction)
- `Cache-Control`: 1-year immutable caching for static assets in `/images/` and stale-while-revalidate for CSS/JS.
