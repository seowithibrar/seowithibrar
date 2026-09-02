import re

html_path = r"c:\Users\mitec\OneDrive\Documents\GitHub\seowithibrar\top-seo-experts-in-pakistan.html"
css_path = r"c:\Users\mitec\OneDrive\Documents\GitHub\seowithibrar\css\blog-post.css"

# ---------------------------------------------------------
# 1. UPDATE CSS (Width 1300px + 1200x628 image & Table styles)
# ---------------------------------------------------------
with open(css_path, "r", encoding="utf-8") as f:
    css_content = f.read()

# Append or update container width rules and data-table styles in blog-post.css
new_css_additions = """

/* ==========================================================================
   POST CONTAINER WIDTH & 1200x628 EXPERT IMAGE & DATA TABLE EXTENSIONS
   ========================================================================== */

.bp-breadcrumbs-inner {
  max-width: 1300px !important;
}

.bp-hero-inner {
  max-width: 1300px !important;
}

.bp-hero-image {
  max-width: 1300px !important;
}

.bp-article-wrapper {
  max-width: 1300px !important;
}

/* 1200x628 Expert Image Banner Layout */
.bp-expert-header {
  flex-direction: column !important;
  gap: 16px !important;
}

.bp-expert-photo-col {
  width: 100% !important;
}

.bp-expert-photo {
  width: 100% !important;
  max-width: 1200px !important;
  height: auto !important;
  aspect-ratio: 1200 / 628 !important;
  object-fit: cover !important;
  border-radius: 12px !important;
  border: 1px solid var(--color-gray-200) !important;
  display: block !important;
}

/* Key-Value Data Tables inside Expert Cards */
.bp-data-table-wrapper {
  margin: 20px 0 24px;
  overflow-x: auto;
  border-radius: 10px;
  border: 1px solid #e2e8f0;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.04);
}

.bp-data-table {
  width: 100%;
  border-collapse: collapse;
  background: #ffffff;
  font-size: 0.9375rem;
}

.bp-data-table tr {
  border-bottom: 1px solid #e2e8f0;
}

.bp-data-table tr:last-child {
  border-bottom: none;
}

.bp-data-table td {
  padding: 14px 18px;
  line-height: 1.65;
  vertical-align: top;
}

.bp-data-table td.bp-kv-key {
  width: 28%;
  min-width: 180px;
  font-weight: 700;
  color: #0f172a;
  background: #f8fafc;
  border-right: 1px solid #e2e8f0;
}

.bp-data-table td.bp-kv-val {
  width: 72%;
  color: #334155;
}

.bp-data-table td.bp-kv-val strong {
  color: #0f172a;
}
"""

if "bp-data-table" not in css_content:
    css_content += new_css_additions
    with open(css_path, "w", encoding="utf-8") as f:
        f.write(css_content)
    print("Updated blog-post.css with 1300px container width, 1200x628 image aspect ratio, and data table CSS.")

# ---------------------------------------------------------
# 2. UPDATE HTML (Expert Image Dimensions & Tables)
# ---------------------------------------------------------
with open(html_path, "r", encoding="utf-8") as f:
    html_content = f.read()

# Update all expert img tags width="100" height="100" or width="80" height="80" to width="1200" height="628" inside expert cards
html_content = re.sub(
    r'(<div class="bp-expert-photo-col">\s*<img src="[^"]+" alt="[^"]+" class="bp-expert-photo") width="\d+" height="\d+"',
    r'\1 width="1200" height="628"',
    html_content
)

# Replace bulleted/plain lists in Expert 5, 6, 7, 12, 15, 16 with proper HTML tables matching the screenshot

# Expert 5 (SEOWITHIBRAR)
exp5_old = """              <p><strong>Why SEOWITHIBRAR Stands Out:</strong></p>
              <ul class="bp-checklist" style="margin-bottom: 1rem;">
                <li><strong>Comprehensive SEO Strategies:</strong> Mastering both on-page and off-page SEO techniques, including local SEO, semantic SEO, and SEO audit services in Pakistan.</li>
                <li><strong>Proven Results:</strong> Consistently ranks websites on the first page of search engines for competitive keywords.</li>
                <li><strong>Industry Leader:</strong> Regularly shares insights and tips on SEO, making it easier for businesses to achieve their digital marketing goals.</li>
                <li><strong>Trusted by Clients:</strong> A long list of satisfied clients attests to SEOWITHIBRAR’s ability to deliver results.</li>
              </ul>
              <p><strong>Achievements:</strong></p>
              <ul class="bp-checklist" style="margin-bottom: 1rem;">
                <li><strong>Thought Leadership:</strong> Recognized as a leading voice in SEO, frequently sharing actionable insights through workshops, seminars, and online training programs, inspiring a new wave of digital marketers. He is one of 2025’s top SEO professionals in Lahore and a freelance SEO consultant with proven results in Pakistan.</li>
                <li><strong>Content Strategy Mastery:</strong> Developed content strategies that resulted in a 300% increase in organic engagement for client blogs and websites.</li>
                <li>Successfully optimized websites across various industries, from e-commerce to education.</li>
                <li>Recognized as a thought leader in SEO through workshops, web design, and blogs.</li>
              </ul>"""

exp5_new = """              <p><strong>Why SEOWITHIBRAR Stands Out:</strong></p>
              <div class="bp-data-table-wrapper">
                <table class="bp-data-table">
                  <tbody>
                    <tr>
                      <td class="bp-kv-key">Comprehensive SEO Strategies</td>
                      <td class="bp-kv-val">Mastering both on-page and off-page SEO techniques, including local SEO, semantic SEO, and SEO audit services in Pakistan.</td>
                    </tr>
                    <tr>
                      <td class="bp-kv-key">Proven Results</td>
                      <td class="bp-kv-val">Consistently ranks websites on the first page of search engines for competitive keywords.</td>
                    </tr>
                    <tr>
                      <td class="bp-kv-key">Industry Leader</td>
                      <td class="bp-kv-val">Regularly shares insights and tips on SEO, making it easier for businesses to achieve their digital marketing goals.</td>
                    </tr>
                    <tr>
                      <td class="bp-kv-key">Trusted by Clients</td>
                      <td class="bp-kv-val">A long list of satisfied clients attests to SEOWITHIBRAR’s ability to deliver results.</td>
                    </tr>
                  </tbody>
                </table>
              </div>

              <p><strong>Achievements:</strong></p>
              <div class="bp-data-table-wrapper">
                <table class="bp-data-table">
                  <tbody>
                    <tr>
                      <td class="bp-kv-key">Thought Leadership</td>
                      <td class="bp-kv-val">Recognized as a leading voice in SEO, frequently sharing actionable insights through workshops, seminars, and online training programs, inspiring a new wave of digital marketers. He is one of 2025’s top SEO professionals in Lahore and a freelance SEO consultant with proven results in Pakistan.</td>
                    </tr>
                    <tr>
                      <td class="bp-kv-key">Content Strategy Mastery</td>
                      <td class="bp-kv-val">Developed content strategies that resulted in a 300% increase in organic engagement for client blogs and websites.</td>
                    </tr>
                    <tr>
                      <td class="bp-kv-key">Multi-Industry Optimization</td>
                      <td class="bp-kv-val">Successfully optimized websites across various industries, from e-commerce to education.</td>
                    </tr>
                    <tr>
                      <td class="bp-kv-key">Thought Leadership &amp; Workshops</td>
                      <td class="bp-kv-val">Recognized as a thought leader in SEO through workshops, web design, and blogs.</td>
                    </tr>
                  </tbody>
                </table>
              </div>"""

if exp5_old in html_content:
    html_content = html_content.replace(exp5_old, exp5_new)
    print("Replaced Expert 5 lists with proper HTML tables.")
else:
    print("WARNING: exp5_old not found directly.")

# Expert 6 (Imran Khadim)
exp6_old = """              <p><strong>Achievements:</strong></p>
              <ul class="bp-checklist" style="margin-bottom: 1rem;">
                <li>Helped multiple small businesses dominate their local markets.</li>
                <li>Recognized as a freelance SEO consultant with proven results in Pakistan.</li>
              </ul>"""

exp6_new = """              <p><strong>Achievements:</strong></p>
              <div class="bp-data-table-wrapper">
                <table class="bp-data-table">
                  <tbody>
                    <tr>
                      <td class="bp-kv-key">Local Market Dominance</td>
                      <td class="bp-kv-val">Helped multiple small businesses dominate their local markets.</td>
                    </tr>
                    <tr>
                      <td class="bp-kv-key">Proven SEO Consultant</td>
                      <td class="bp-kv-val">Recognized as a freelance SEO consultant with proven results in Pakistan.</td>
                    </tr>
                  </tbody>
                </table>
              </div>"""

if exp6_old in html_content:
    html_content = html_content.replace(exp6_old, exp6_new)
    print("Replaced Expert 6 lists with proper HTML tables.")

# Expert 7 (Usman Latif)
exp7_old = """              <p><strong>Achievements:</strong></p>
              <ul class="bp-checklist" style="margin-bottom: 1rem;">
                <li>Optimized hundreds of websites for speed and user experience.</li>
                <li>Trained a large audience in SEO and digital marketing best practices.</li>
              </ul>"""

exp7_new = """              <p><strong>Achievements:</strong></p>
              <div class="bp-data-table-wrapper">
                <table class="bp-data-table">
                  <tbody>
                    <tr>
                      <td class="bp-kv-key">Speed &amp; UX Optimization</td>
                      <td class="bp-kv-val">Optimized hundreds of websites for speed and user experience.</td>
                    </tr>
                    <tr>
                      <td class="bp-kv-key">Digital Skills Trainer</td>
                      <td class="bp-kv-val">Trained a large audience in SEO and digital marketing best practices.</td>
                    </tr>
                  </tbody>
                </table>
              </div>"""

if exp7_old in html_content:
    html_content = html_content.replace(exp7_old, exp7_new)
    print("Replaced Expert 7 lists with proper HTML tables.")

# Expert 12 (Falak Naz Soomro)
exp12_old = """              <p><strong>SEO & Digital Marketing Expertise:</strong></p>
              <ul class="bp-checklist" style="margin-bottom: 1rem;">
                <li><strong>On-Page SEO:</strong> Optimize website content, structure, and speed for better search engine visibility and user engagement.</li>
                <li><strong>Off-Page SEO:</strong> Build high-quality backlinks and strengthen domain authority to boost rankings and credibility.</li>
                <li><strong>Technical SEO:</strong> Identify and fix website performance issues, ensuring optimal crawlability, indexing, and site health.</li>
                <li><strong>SEO Audits:</strong> Conduct in-depth audits to analyze and improve website performance, fixing technical errors and optimizing SEO strategies.</li>
                <li><strong>Fiverr SEO:</strong> Optimize Fiverr gigs and profiles to increase visibility, attract potential clients, and improve conversions.</li>
                <li><strong>LinkedIn Optimization:</strong> Enhance LinkedIn profiles for better networking, job opportunities, and professional growth.</li>
                <li><strong>YouTube Channel (50 K+ Subscribers):</strong> Falak is also a YouTube content creator with over 50,000 subscribers, where she shares expert insights on SEO, digital marketing, and online business growth. Her content helps businesses, freelancers, and individuals stay ahead in the competitive digital landscape by providing actionable tips and strategies.</li>
              </ul>"""

exp12_new = """              <p><strong>SEO &amp; Digital Marketing Expertise:</strong></p>
              <div class="bp-data-table-wrapper">
                <table class="bp-data-table">
                  <tbody>
                    <tr>
                      <td class="bp-kv-key">On-Page SEO</td>
                      <td class="bp-kv-val">Optimize website content, structure, and speed for better search engine visibility and user engagement.</td>
                    </tr>
                    <tr>
                      <td class="bp-kv-key">Off-Page SEO</td>
                      <td class="bp-kv-val">Build high-quality backlinks and strengthen domain authority to boost rankings and credibility.</td>
                    </tr>
                    <tr>
                      <td class="bp-kv-key">Technical SEO</td>
                      <td class="bp-kv-val">Identify and fix website performance issues, ensuring optimal crawlability, indexing, and site health.</td>
                    </tr>
                    <tr>
                      <td class="bp-kv-key">SEO Audits</td>
                      <td class="bp-kv-val">Conduct in-depth audits to analyze and improve website performance, fixing technical errors and optimizing SEO strategies.</td>
                    </tr>
                    <tr>
                      <td class="bp-kv-key">Fiverr SEO</td>
                      <td class="bp-kv-val">Optimize Fiverr gigs and profiles to increase visibility, attract potential clients, and improve conversions.</td>
                    </tr>
                    <tr>
                      <td class="bp-kv-key">LinkedIn Optimization</td>
                      <td class="bp-kv-val">Enhance LinkedIn profiles for better networking, job opportunities, and professional growth.</td>
                    </tr>
                    <tr>
                      <td class="bp-kv-key">YouTube Channel (50K+ Subs)</td>
                      <td class="bp-kv-val">Shares expert insights on SEO, digital marketing, and online business growth to empower freelancers and businesses.</td>
                    </tr>
                  </tbody>
                </table>
              </div>"""

if exp12_old in html_content:
    html_content = html_content.replace(exp12_old, exp12_new)
    print("Replaced Expert 12 lists with proper HTML tables.")

# Expert 15 (Osama Arshad)
exp15_old = """              <p><strong>Why Osama Arshad Stands Out:</strong></p>
              <ul class="bp-checklist" style="margin-bottom: 1rem;">
                <li><strong>End-to-End Digital Solutions:</strong> Master’s in both technical SEO and web development, ensuring websites are optimized for speed, structure, and search engines.</li>
                <li><strong>Data-Driven Growth:</strong> Crafts tailored SEO strategies backed by analytics to boost rankings and organic traffic.</li>
                <li><strong>Cross-Disciplinary Expertise:</strong> Uniquely bridges design, development, and SEO for holistic digital success.</li>
                <li><strong>Industry Educator:</strong> Shares insights through workshops and content, empowering aspiring developers and marketers.</li>
              </ul>
              <p><strong>Achievements:</strong></p>
              <ul class="bp-checklist" style="margin-bottom: 1rem;">
                <li>Optimized 200+ websites for SEO and performance, enhancing visibility and conversions.</li>
                <li>Developed scalable web solutions for startups and enterprises, integrating SEO best practices.</li>
                <li>Recognized as a thought leader at tech conferences for his innovative approaches to digital growth.</li>
              </ul>"""

exp15_new = """              <p><strong>Why Osama Arshad Stands Out:</strong></p>
              <div class="bp-data-table-wrapper">
                <table class="bp-data-table">
                  <tbody>
                    <tr>
                      <td class="bp-kv-key">End-to-End Digital Solutions</td>
                      <td class="bp-kv-val">Master’s in both technical SEO and web development, ensuring websites are optimized for speed, structure, and search engines.</td>
                    </tr>
                    <tr>
                      <td class="bp-kv-key">Data-Driven Growth</td>
                      <td class="bp-kv-val">Crafts tailored SEO strategies backed by analytics to boost rankings and organic traffic.</td>
                    </tr>
                    <tr>
                      <td class="bp-kv-key">Cross-Disciplinary Expertise</td>
                      <td class="bp-kv-val">Uniquely bridges design, development, and SEO for holistic digital success.</td>
                    </tr>
                    <tr>
                      <td class="bp-kv-key">Industry Educator</td>
                      <td class="bp-kv-val">Shares insights through workshops and content, empowering aspiring developers and marketers.</td>
                    </tr>
                  </tbody>
                </table>
              </div>

              <p><strong>Achievements:</strong></p>
              <div class="bp-data-table-wrapper">
                <table class="bp-data-table">
                  <tbody>
                    <tr>
                      <td class="bp-kv-key">200+ Sites Optimized</td>
                      <td class="bp-kv-val">Optimized 200+ websites for SEO and performance, enhancing visibility and conversions.</td>
                    </tr>
                    <tr>
                      <td class="bp-kv-key">Scalable Solutions</td>
                      <td class="bp-kv-val">Developed scalable web solutions for startups and enterprises, integrating SEO best practices.</td>
                    </tr>
                    <tr>
                      <td class="bp-kv-key">Tech Speaker &amp; Leader</td>
                      <td class="bp-kv-val">Recognized as a thought leader at tech conferences for his innovative approaches to digital growth.</td>
                    </tr>
                  </tbody>
                </table>
              </div>"""

if exp15_old in html_content:
    html_content = html_content.replace(exp15_old, exp15_new)
    print("Replaced Expert 15 lists with proper HTML tables.")

# Expert 16 (Syed Muzammil Javed)
exp16_old = """              <p><strong>Public Achievements & Key Milestones 🚀</strong></p>
              <ul class="bp-checklist" style="margin-bottom: 1rem;">
                <li><strong>Founder & CEO of SMJ Solutions:</strong> Leading a digital marketing agency specializing in SEO, business automation, paid ads, and eCommerce growth strategies.</li>
                <li><strong>Top-Rated Freelancer & Digital Marketing Expert:</strong> Successfully worked with US-based companies, helping them scale globally with data-driven marketing strategies.</li>
                <li><strong>Trainer & Mentor to 200+ Students:</strong> Conducted professional training programs, empowering students with practical digital marketing skills for successful careers.</li>
                <li>Collaborated with Arfa Foundation, Enablers, and NAVTTC, and contributed to business empowerment initiatives in both the government and private sectors.</li>
              </ul>"""

exp16_new = """              <p><strong>Public Achievements &amp; Key Milestones 🚀</strong></p>
              <div class="bp-data-table-wrapper">
                <table class="bp-data-table">
                  <tbody>
                    <tr>
                      <td class="bp-kv-key">Founder &amp; CEO of SMJ Solutions</td>
                      <td class="bp-kv-val">Leading a digital marketing agency specializing in SEO, business automation, paid ads, and eCommerce growth strategies.</td>
                    </tr>
                    <tr>
                      <td class="bp-kv-key">Top-Rated Freelancer</td>
                      <td class="bp-kv-val">Successfully worked with US-based companies, helping them scale globally with data-driven marketing strategies.</td>
                    </tr>
                    <tr>
                      <td class="bp-kv-key">Trainer &amp; Mentor</td>
                      <td class="bp-kv-val">Conducted professional training programs for 200+ students, empowering them with practical digital marketing skills.</td>
                    </tr>
                    <tr>
                      <td class="bp-kv-key">Strategic Collaborations</td>
                      <td class="bp-kv-val">Collaborated with Arfa Foundation, Enablers, and NAVTTC to empower businesses across public and private sectors.</td>
                    </tr>
                  </tbody>
                </table>
              </div>"""

if exp16_old in html_content:
    html_content = html_content.replace(exp16_old, exp16_new)
    print("Replaced Expert 16 lists with proper HTML tables.")

with open(html_path, "w", encoding="utf-8") as f:
    f.write(html_content)

print("Finished applying table and width updates to HTML & CSS.")
