# SEO With Ibrar — Website Rules, Standards & Terms
One master document for design, layout, content, SEO, development, and site legal terms for seowithibrar.com.
Version 1.0 · Owner: Ibrar Ahmad · Applies to every page, template, and future edit.

How to read this: **MUST / MUST NOT** = mandatory. **SHOULD** = default unless there is a documented reason. Values in [BRACKETS] are filled once the final brand tokens are extracted from the reference screenshots.

---

## PART 1 — DESIGN RULES

### 1.1 Design tokens (single source of truth)
All styling MUST come from CSS variables. No hard-coded colors, fonts, or spacing in components.

| Token | Rule |
|---|---|
| --bg, --surface, --surface-2 | Page, card, and raised-card backgrounds. Max 3 background levels. |
| --text, --muted | Primary and secondary text. |
| --accent, --accent-2 | One main accent and one supporting accent. No third accent color. |
| --success | Used only for growth arrows and positive metrics. |
| --border | 1px subtle borders on all cards. |
| --radius-sm / md / lg | Fixed set [8 / 16 / 24px]. No other radius values. |
| --shadow-card, --shadow-hover | Two shadows only. |
| --font-display, --font-body | Maximum 2 font families. Max 3 weights per family. |
| --space-1 to --space-8 | 4px scale (4, 8, 12, 16, 24, 32, 48, 64, 96, 128). |

### 1.2 Color rules
- Accent color MUST be used for: primary buttons, italic heading words, active nav, number counters, links on hover.
- Accent MUST NOT be used as a body text color or for large background areas.
- Text contrast MUST meet WCAG AA (4.5:1 body, 3:1 large text and UI components).
- Never use color alone to convey meaning (add icon, arrow, or label).

### 1.3 Typography rules
- Display font for H1/H2/stat numbers; body font for everything else.
- Scale (desktop / mobile): H1 56/36px · H2 40/28px · H3 22/18px · body 17/16px · small 14px.
- Line height: headings 1.15, body 1.65. Max line length 70 characters.
- Signature heading style: in every H2, 1-2 words MUST be wrapped in italic accent color. Never more than 2 words.
- Section label: uppercase, 12-13px, letter-spacing 0.12em, prefixed with "— ".
- No ALL CAPS paragraphs, no underlined text except links.

### 1.4 Buttons & links
- Primary button: filled accent, arrow "→" at end of label, radius --radius-md.
- Secondary button: outline, same size as primary.
- Max 2 buttons per section (1 primary + 1 secondary).
- Button label: verb-first, 2-4 words ("Book Free Consultation →").
- Every primary CTA MUST open the consultation popup (`href="#open-consult"`).
- Hover: lift 2px + shadow. Focus: 2px visible outline in accent. Active: no lift.
- Minimum tap target 44×44px.

### 1.5 Cards
- Standard card: --surface, 1px --border, --radius-lg, padding 24-32px.
- Hover: translateY(-4px), border turns accent, shadow-hover. Transition 200-250ms ease.
- Every card in a grid MUST have equal height (CSS grid, align-items: stretch).
- Numbered cards use 2-digit counters (01-09) in the display font, muted color.

### 1.6 Imagery & icons
- Portrait: one professional photo, same crop used everywhere, WebP, max 120KB.
- Use real client result screenshots (GSC) for proof sections, with client permission. Blur or crop client-identifying data if permission is not given.
- Icons: one set only (line style, 1.5-2px stroke), consistent size per context (20/24/32px).
- All images: descriptive alt text, explicit width/height, lazy-load below the fold.
- No stock photos of people shaking hands, laptops with graphs, or generic "SEO" clip art.
- Flags/country row: only countries where you have actually worked.

### 1.7 Motion rules
- Allowed: fade-up on scroll (16px, 400ms), count-up on stats, floating hero cards (slow loop), hover lifts, accordion open/close.
- Not allowed: auto-playing sound, parallax, spinning elements, anything that loops faster than 6s.
- MUST honor `prefers-reduced-motion` (disable all animation).
- Animation MUST NOT delay content: no element hidden longer than 600ms after entering view.

---

## PART 2 — LAYOUT RULES

### 2.1 Grid & containers
- Max container width 1200px, side padding 24px (mobile 16px).
- 12-column grid desktop, 6 tablet, 4 mobile. Gap 24px.
- Section vertical padding: 96-128px desktop, 64px mobile.
- Alternate section backgrounds (--bg / --surface) to separate sections; no hard divider lines.

### 2.2 Breakpoints
| Name | Width | Layout |
|---|---|---|
| Mobile | up to 767px | 1 column, hamburger menu, stacked process steps |
| Tablet | 768-1023px | 2 columns, hero stacks |
| Desktop | 1024px and up | Full layout |
| Wide | 1440px and up | Container stays 1200px, centered |

No horizontal scroll at any width from 320px up.

### 2.3 Homepage section order (locked)
1 Header → 2 Hero → 3 About → 4 Stats → 5 Services (9 cards + 2 banners) → 6 Proven Results → 7 Case Studies → 8 Process (5 steps) → 9 Testimonials → 10 YouTube Insights → 11 FAQ → 12 Final CTA → 13 Footer → Cookie bar → Sticky mobile CTA.
- Order MUST NOT change without a documented reason.
- Maximum one new section per quarter. Every section needs a purpose: build trust, explain, or convert.

### 2.4 Section anatomy (every section)
Label → H2 → 1-2 line intro → content → optional CTA. Do not skip the label or intro.

### 2.5 Header & footer
- Header: sticky, 72px tall, solid background after 20px scroll. Max 6 top-level items + "Contact Me" button.
- Mega-dropdowns: title, 1-line description, one button, image. Open on hover (desktop), tap (mobile).
- Footer: 4-column link grid, brand line, LinkedIn/YouTube icons, copyright, "Let's Talk" button.
- Sticky mobile CTA: bottom bar, collapsible, never covers form fields or the cookie bar.

### 2.6 Page templates beyond the homepage
Service page: Hero → Problem → What's included → Process → Proof → FAQ → CTA.
Industry page: Hero → Industry challenges → My approach → Case study → FAQ → CTA.
Location page: Hero → Local market insight → Services → Proof → FAQ → CTA.
Blog post: Title → Author box → TOC → Body → Key takeaways → Related posts → CTA.
All reuse homepage components. No new component without adding it to Part 1 and Part 2.

---

## PART 3 — CONTENT RULES

### 3.1 Voice & tone
- First person ("I"), because this is a solo specialist brand. Never "we" unless referring to a named team on a specific project.
- Plain, confident, human. Short sentences. Explain jargon on first use.
- No hype words: "revolutionary", "game-changing", "skyrocket", "guaranteed", "best-in-class".
- No ranking guarantees, ever. Say "I focus on real strategy and steady growth."
- Roman Urdu or Urdu microcopy is allowed only on clearly marked Urdu pages.

### 3.2 Headline & copy formulas
- H1: name + role + location/qualifier. One per page.
- H2: promise or outcome, with italic accent words ("Real Numbers. *Real Growth.*").
- Intro paragraph: max 30 words. Body paragraph: max 4 lines desktop.
- Card description: 15-25 words. Button label: 2-4 words.
- Every section answers one question for the visitor: "Why should I trust Ibrar?" / "What do I get?" / "What happens next?"

### 3.3 Proof & claims (strict)
- Every number MUST be verifiable: Google Search Console, GA4, or a signed-off client document. Keep the source file.
- Show time frame and scope with every metric ("6 months, organic only").
- Testimonials MUST be real, with name, role, and city, and written consent. No stock avatars with fake names.
- Case studies MUST have client permission. If a client name cannot be shown, use industry + city.
- Do not claim awards, certifications, or partnerships you do not hold.
- Update stats at least every 6 months; show "Last updated [month year]" on the Proven Results section.
- Unverified figures MUST stay as `[VERIFY]` and MUST NOT be published.

### 3.4 Content structure rules
- One topic per page. One primary keyword and 3-6 secondary keywords per page, mapped in a keyword sheet.
- Use a topic-cluster model: pillar page → supporting pages → internal links both ways.
- Each page needs: unique title, meta description, one H1, logical H2/H3, at least one image, internal links (3+), one clear CTA.
- Include a short "key takeaways" or summary block on any page over 1,200 words.
- FAQs: write real questions from sales calls, GSC queries, and People Also Ask. Answers 40-80 words, direct first sentence.
- Write for AI search too: clear definitions, direct answers, structured lists, named entities, author credentials.

### 3.5 Originality & sourcing
- Content MUST be original. No copying from deeprahulseo.com or any competitor.
- No AI-generated text published without human edit for facts, voice, and local relevance.
- Cite sources for any third-party statistic (link to the source). No outdated stats older than 2 years unless historical.
- Images and tools MUST be owned, licensed, or free-license with attribution.

### 3.6 Naming & formatting conventions
- Brand name: "SEO With Ibrar" (site) and "Ibrar Ahmad" (person). Never abbreviate.
- Spelling: choose one variant (British or American) and use it everywhere. Recommended: British (optimisation), matching Pakistan usage.
- Dates: 11 October 2026. Numbers: 1,600 (comma), percentages with %, currency with code (PKR / USD).
- Headings in sentence case or title case, but consistent site-wide.

### 3.7 Content approval workflow
Draft → fact-check numbers → SEO check → design check → Ibrar approval → publish → log in changelog.
Interns MAY draft; only Ibrar approves publishing.

---

## PART 4 — SEO RULES

- Title tag 50-60 characters, includes primary keyword + brand. Meta description 140-160 characters with a CTA.
- URL: lowercase, hyphens, no stop words, max 5 words, no dates. Example: `/local-seo-services/`.
- One canonical per page, self-referencing. Noindex thin utility pages.
- Schema: Person + ProfessionalService (site-wide), FAQPage (FAQ blocks), BreadcrumbList (inner pages), Article (blogs), Review only for genuine reviews.
- Internal linking: every service page links to 3+ related pages; no orphan pages; descriptive anchor text, never "click here".
- Core Web Vitals targets: LCP under 2.5s, INP under 200ms, CLS under 0.1 (mobile).
- XML sitemap submitted to GSC; robots.txt allows crawling of all public pages.
- Track in GSC and GA4: consultation popup opens, form/WhatsApp/call clicks, scroll depth, case-study opens.
- Monthly SEO audit of own site (use the Full Page Audit workflow).

---

## PART 5 — DEVELOPMENT & PERFORMANCE RULES

- Build as clean semantic HTML first; convert to Elementor with one class per component and global colors/fonts mapped to the tokens.
- Elementor rules: use global styles only, no inline custom CSS per widget, containers (not legacy sections), max DOM depth 6, no unused widgets.
- Page weight under 1.5MB; images WebP/AVIF; fonts self-hosted or Google Fonts with `display=swap`, preload the display font only.
- JS: vanilla or minimal. No jQuery unless required by a plugin. Defer all non-critical scripts.
- Plugins: keep to the minimum list [SEO plugin, cache, security, forms, backup]. Remove anything unused.
- Security: HTTPS everywhere, security headers, login limits, 2FA for admin, weekly backups kept 30 days, updates tested on staging first.
- Staging workflow: build on staging → QA checklist → push live. No edits directly on production for layout changes.
- Version control: keep the master HTML/CSS and Elementor JSON export in one dated folder; log every release in a changelog.

---

## PART 6 — ACCESSIBILITY RULES

- WCAG 2.1 AA minimum.
- Keyboard: every interactive element reachable by Tab, logical order, visible focus, popup traps focus and closes on Esc.
- Landmarks: header, nav, main, footer. Skip-to-content link.
- Forms and popups: labelled inputs, error messages in text, no placeholder-only labels.
- Accordion and dropdowns use correct ARIA (`aria-expanded`, `aria-controls`).
- Videos: captions or transcript; lightbox must be dismissible.

---

## PART 7 — QA CHECKLIST (run before every publish)

**Design:** tokens only · 2 fonts max · contrast passes · hover/focus states · no off-grid spacing
**Layout:** 320 / 375 / 768 / 1024 / 1440px checked · no horizontal scroll · equal-height cards · section order intact
**Content:** every number sourced · no `[VERIFY]` left · testimonials consented · spelling variant consistent · no copied text
**SEO:** title/meta/H1 unique · schema validates · internal links added · canonical correct · sitemap updated
**Performance:** LCP/INP/CLS pass on mobile · images compressed · scripts deferred
**Functionality:** every CTA opens popup · WhatsApp/call/mail links work · accordion, dropdown, lightbox work · cookie bar saves choice · forms deliver to inbox
**Legal:** privacy, terms, and cookie pages linked in footer

---

## PART 8 — WEBSITE TERMS & CONDITIONS (draft for seowithibrar.com)

> This is a general-purpose draft to adapt. It is not legal advice. Have a qualified lawyer in Pakistan review it before publishing, especially the liability, refund, and governing-law clauses.

**Last updated: [DATE]**

**1. About these terms**
These terms apply to your use of seowithibrar.com ("the Site"), operated by Ibrar Ahmad, trading as SEO With Ibrar, based in Lahore, Pakistan. By using the Site you agree to these terms. If you do not agree, please stop using the Site.

**2. Services**
The Site describes SEO consulting services and offers free consultations, tools, and content. Information on the Site is general in nature. Paid services are governed by a separate written proposal or service agreement, which prevails over these terms if they conflict.

**3. No guarantee of results**
SEO outcomes depend on many factors outside my control, including search engine algorithms, competition, and your website's condition. I do not guarantee any specific ranking, traffic, or revenue. Case studies and results shown on the Site describe past client outcomes and are not a promise of future results.

**4. Free consultation**
A free consultation is an introductory discussion. It creates no obligation on either side and does not form a client relationship until a written agreement is signed.

**5. Free tools**
Tools such as the schema and robots.txt generators are provided "as is". You are responsible for reviewing and testing any output before using it on your website. I am not liable for issues caused by implementing generated code.

**6. Intellectual property**
All text, design, logos, graphics, and code on the Site belong to Ibrar Ahmad or are used under licence, and are protected by copyright. You may not copy, reproduce, or republish Site content, or replicate the Site's design, without written permission. You may quote short extracts with a clear link back to the source.

**7. Client work and confidentiality**
Case studies are shared with client permission. Client data is treated as confidential and used only for the agreed project.

**8. User conduct**
You agree not to misuse the Site, attempt unauthorised access, send spam or malicious code, scrape the Site at a rate that harms performance, or submit false information through forms.

**9. Third-party links and embeds**
The Site links to third-party services (for example YouTube, LinkedIn, WhatsApp, Google). I do not control and am not responsible for their content or privacy practices.

**10. Privacy and cookies**
How I collect and use personal data is described in the Privacy Policy, and cookie use in the Cookie Policy. Contact submissions (name, email, phone, message) are used to reply to your enquiry and are not sold.

**11. Disclaimer and limitation of liability**
The Site and its content are provided "as is" without warranties of any kind. To the maximum extent permitted by law, I am not liable for indirect, incidental, or consequential loss arising from use of the Site. Nothing here excludes liability that cannot be excluded by law.

**12. Payments and refunds (for paid services)**
[Define: payment schedule, currency, refund policy, cancellation notice period, and what happens on early termination. These must match your proposal template.]

**13. Changes**
I may update these terms at any time. The "Last updated" date shows the latest version. Continued use of the Site means you accept the changes.

**14. Governing law**
These terms are governed by the laws of Pakistan, and disputes fall under the courts of Lahore, unless a signed service agreement says otherwise. [Confirm with your lawyer.]

**15. Contact**
Ibrar Ahmad · [EMAIL] · [PHONE/WHATSAPP] · Lahore, Pakistan

### Companion pages to publish with it
- **Privacy Policy:** data collected (forms, WhatsApp clicks, analytics), purpose, retention, sharing with tools (Google Analytics, Search Console, email provider), user rights, contact for data requests.
- **Cookie Policy + banner:** list Analytics and Marketing categories, "Always on" essentials, Reject All / Save Preferences, no non-essential cookies before consent.
- **Disclaimer (optional):** results disclaimer for case-study and stats sections.

---

## PART 9 — GOVERNANCE

- Any change to a rule in Parts 1-6 MUST be written here first, with date and reason.
- Exceptions MUST be documented in the changelog with the page, the rule, and why.
- Review this document every 6 months or after any major redesign.
- Rule priority when rules conflict: Legal → Accessibility → Content accuracy → SEO → Design → Convenience.

### Changelog
| Date | Change | By |
|---|---|---|
| 2026-10-11 | v1.0 created | Ibrar Ahmad |
