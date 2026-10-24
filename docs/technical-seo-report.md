# Technical SEO & Performance Engineering Report

**Website**: [https://seowithibrar.com/](https://seowithibrar.com/)  
**Platform**: Vercel Edge Hosting / Static Site Generation  
**Scope**: Crawlability, Core Web Vitals, HTTP Configuration, Canonical Routing, and Asset Delivery  
**Report Date**: October 2026  

---

## 1. Technical Issue Matrix

| Issue | Affected URL / File | Severity | Root Cause | Implemented Fix | Validation Method | Result | Remaining Action |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Broken WebP Case Study Images** | `index.html` (lines 2887–2938) | **High** | Homepage referenced obsolete external image URLs (`KIMS.webp`, `Euro...webp`, `Navid...webp`, `geo...webp`) that returned 404. | Mapped cards to verified local case study assets (`Education platfrom in lahore.png`, `Visa Consutlacny in Karachi.png`, `School Website.png`, `Local ecommeces.png`) with natural width/height. | Python DOM image crawler + HTTP status inspection. | **Resolved** (All 4 images render locally, 0 broken requests). | None. |
| **Missing Image Dimensions (CLS Risk)** | All 15 HTML templates (`*.html`) | **Medium** | `<img>` elements lacked explicit `width` and `height` attributes, triggering layout recalculations during initial page paint. | Extracted natural dimensions from image headers via PIL and injected explicit `width` and `height` attributes site-wide. | Python verification script checking all `<img>` nodes. | **Resolved** (0 missing dimension tags across site). | None. |
| **Duplicate & Conflicting H1 Headings** | `about.html`, `blog.html`, `contact.html` | **Medium** | Multiple headings were marked up as `<h1>` or secondary display wrappers competed with the primary page title. | Demoted secondary decorative headings to styled `<div>` or `<h2>` elements, retaining exactly one semantic `<h1>` per template. | DOM query counting `len(soup.find_all('h1'))`. | **Resolved** (Exactly 1 H1 per page across all 15 pages). | None. |
| **Missing HTTP Security & Caching Headers** | `vercel.json` | **Medium** | Default deployment configuration lacked explicit security headers and long-term asset cache control. | Added `X-Content-Type-Options: nosniff`, `X-Frame-Options: SAMEORIGIN`, `Referrer-Policy: strict-origin-when-cross-origin`, `Permissions-Policy`, and 1-year immutable caching for `/images/(.*)`. | Configuration syntax validation + response header curl testing. | **Resolved** (Headers active on all Vercel edge routes). | None. |
| **Unindexed Internal Doc Folders** | `robots.txt` | **Low** | `robots.txt` did not disallow internal markdown audit reports and scratch scripts. | Added `Disallow: /scratch/` and `Disallow: /docs/` to `robots.txt`. | Robot exclusion syntax validation. | **Resolved** (Documentation directories blocked from search indexation). | None. |
| **Malformatted Image Filename in Top Experts Directory** | `top-seo-experts-in-pakistan.html` | **Low** | Image tag referenced `images/Syed Muzammil Javed's.webp` with an apostrophe in filename. | Updated tag to clean reference `images/Syed Muzammil Javed.webp` with complete alt and dimension attributes. | Image path verification script. | **Resolved** (Clean asset loading across all browsers). | None. |
| **Incomplete JSON-LD Knowledge Graphs** | All 15 HTML templates | **Medium** | Pages lacked standardized schema or had disconnected entities without publisher/provider linkage. | Injected complete `@graph` schema arrays for `WebSite`, `Person`, `ProfessionalService`, `Service`, `BreadcrumbList`, and `FAQPage`. | Python `json.loads` syntax and entity link validation. | **Resolved** (15/15 pages contain valid structured data). | None. |
| **Consultation Modal Grid HTML Syntax Error** | `index.html` | **High** | Stray closing `</div>` prematurely severed the modal container, ejecting `.consult-avatar-side` outside the CSS grid layout. | Removed premature closing `</div>` and aligned grid column child elements cleanly. | Visual inspection and DOM tree traversal. | **Resolved** (Modal opens as a unified two-column desktop interface). | None. |

---

## 2. Core Web Vitals & Performance Strategy

### Largest Contentful Paint (LCP)
- **Hero Image Prioritization**: The primary above-the-fold hero image (`images/ibrar.png`) on `index.html` and header banners on subpages are configured with `fetchpriority="high"` and do **not** use `loading="lazy"`.
- **Preload Optimization**: Browser begins parsing and downloading hero assets immediately without waiting for layout execution.

### Cumulative Layout Shift (CLS)
- **Aspect Ratio Protection**: Every image now declares explicit `width` and `height` attributes matching natural image ratios (e.g. `width="1577" height="524"`).
- **Font Display**: CSS utilizes `font-display: swap` to prevent invisible text during font download.

### Interaction to Next Paint (INP)
- **Lightweight Scripting**: Zero bloated JavaScript frameworks. All modal triggers, lightbox handlers, and mobile menu toggles use minimal native JavaScript.
- **Asynchronous Execution**: Heavy non-critical scripts execute asynchronously.

---

## 3. Crawlability & Canonical URL Architecture

1. **Protocol & Hostname**: Canonical URLs consistently resolve to `https://seowithibrar.com`.
2. **Path Normalization**: Handled by Vercel clean URL engine:
   - Request to `/about.html` redirects automatically to `/about`.
   - Trailing slash variant `/about/` redirects automatically to `/about`.
   - Internal links across menus and footers point directly to extensionless canonical paths.
3. **Sitemap Indexing**: `sitemap.xml` lists all 15 public canonical URLs with current `lastmod` timestamps.
