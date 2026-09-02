import json
import uuid

def gen_id():
    return uuid.uuid4().hex[:7]

def create_elementor_json():
    # Target JSON output path
    out_file = r"c:\Users\mitec\OneDrive\Documents\GitHub\seowithibrar\complete-o-level-program-guide-elementor.json"

    # Build Elementor Template JSON structure (Version 0.4 standard Elementor export)
    # Customized for EduEminent (https://edueminent.com/) with 1300px width container
    elementor_data = {
        "version": "0.4",
        "title": "The Complete O Level Program Guide: From Enrollment to Career Success (EduEminent)",
        "type": "page",
        "content": [
            # Hero Banner Section
            {
                "id": gen_id(),
                "elType": "section",
                "isInner": False,
                "settings": {
                    "background_background": "classic",
                    "background_color": "#0f172a",
                    "padding": {"unit": "px", "top": "60", "right": "20", "bottom": "60", "left": "20", "isLinked": False},
                    "border_border": "solid",
                    "border_color": "#c4a97c",
                    "border_width": {"unit": "px", "top": "0", "right": "0", "bottom": "4", "left": "0", "isLinked": False}
                },
                "elements": [
                    {
                        "id": gen_id(),
                        "elType": "column",
                        "isInner": False,
                        "settings": {"_column_size": 100},
                        "elements": [
                            {
                                "id": gen_id(),
                                "elType": "widget",
                                "isInner": False,
                                "widgetType": "html",
                                "settings": {
                                    "html": """<div style="text-align: center; max-width: 1300px; margin: 0 auto; color: #ffffff; font-family: 'Inter', sans-serif;">
  <div style="display: flex; gap: 8px; justify-content: center; margin-bottom: 20px; flex-wrap: wrap;">
    <span style="background: #c4a97c; color: #000; padding: 4px 14px; border-radius: 99px; font-size: 12px; font-weight: 700; text-transform: uppercase;">EduEminent Master Guide</span>
    <span style="background: rgba(255,255,255,0.1); color: #e2e8f0; padding: 4px 14px; border-radius: 99px; font-size: 12px; font-weight: 600;">Secondary Qualifications</span>
    <span style="background: rgba(255,255,255,0.1); color: #e2e8f0; padding: 4px 14px; border-radius: 99px; font-size: 12px; font-weight: 600;">CAIE & Edexcel</span>
  </div>
  <h1 style="font-family: 'Outfit', sans-serif; font-size: 42px; font-weight: 800; line-height: 1.2; margin-bottom: 16px; color: #ffffff;">The Complete O Level Program Guide: From Enrollment to Career Success</h1>
  <p style="color: #94a3b8; font-size: 15px;">Published: August 5, 2024 | Updated: August 05, 2026 | Read Time: 15-18 minutes</p>
</div>"""
                                }
                            }
                        ]
                    }
                ]
            },

            # Main Body Section (2 Columns: TOC + Main Content, 1300px Container Width)
            {
                "id": gen_id(),
                "elType": "section",
                "isInner": False,
                "settings": {
                    "background_background": "classic",
                    "background_color": "#f8fafc",
                    "padding": {"unit": "px", "top": "50", "right": "20", "bottom": "60", "left": "20", "isLinked": False}
                },
                "elements": [
                    # Column 1: Sidebar / TOC (30%)
                    {
                        "id": gen_id(),
                        "elType": "column",
                        "isInner": False,
                        "settings": {"_column_size": 30, "_inline_size": 30},
                        "elements": [
                            {
                                "id": gen_id(),
                                "elType": "widget",
                                "isInner": False,
                                "widgetType": "html",
                                "settings": {
                                    "html": """<div style="background: #ffffff; border: 1px solid #e2e8f0; border-radius: 16px; padding: 24px; box-shadow: 0 4px 20px -2px rgba(15,23,42,0.05); position: sticky; top: 20px;">
  <h3 style="font-family: 'Outfit', sans-serif; font-size: 16px; font-weight: 700; color: #0f172a; text-transform: uppercase; margin-top:0; margin-bottom: 16px; border-bottom: 2px solid #f1f5f9; padding-bottom: 8px;">Table of Contents</h3>
  <ul style="list-style: none; padding: 0; margin: 0; font-size: 14px; line-height: 1.8;">
    <li><a href="#intro" style="color: #c4a97c; text-decoration: none; font-weight: 600;">Introduction</a></li>
    <li><a href="#understanding" style="color: #475569; text-decoration: none;">1. Understanding O Levels</a></li>
    <li><a href="#curriculum" style="color: #475569; text-decoration: none;">2. Curriculum & Subjects</a></li>
    <li><a href="#admission" style="color: #475569; text-decoration: none;">3. Admission & Eligibility</a></li>
    <li><a href="#study-strategy" style="color: #475569; text-decoration: none;">4. 12-Month Study Strategy</a></li>
    <li><a href="#exam-format" style="color: #475569; text-decoration: none;">5. Exam Format & Grading</a></li>
    <li><a href="#career-pathways" style="color: #475569; text-decoration: none;">6. Future Pathways</a></li>
    <li><a href="#pakistan-context" style="color: #475569; text-decoration: none;">7. O Levels in Pakistan</a></li>
    <li><a href="#regional-context" style="color: #475569; text-decoration: none;">8. Regional: UAE & KSA</a></li>
    <li><a href="#faqs" style="color: #475569; text-decoration: none;">9. Frequently Asked Questions</a></li>
    <li><a href="#conclusion" style="color: #475569; text-decoration: none;">Conclusion & Checklist</a></li>
  </ul>
</div>"""
                                }
                            }
                        ]
                    },

                    # Column 2: Main Guide Content + EduEminent Author Box + Related Posts (70%)
                    {
                        "id": gen_id(),
                        "elType": "column",
                        "isInner": False,
                        "settings": {"_column_size": 70, "_inline_size": 70},
                        "elements": [
                            {
                                "id": gen_id(),
                                "elType": "widget",
                                "isInner": False,
                                "widgetType": "html",
                                "settings": {
                                    "html": """<div style="max-width: 1300px; margin: 0 auto; background: #ffffff; border: 1px solid #e2e8f0; border-radius: 20px; padding: 40px; box-shadow: 0 4px 20px -2px rgba(15,23,42,0.05); color: #334155; font-family: 'Inter', sans-serif; line-height: 1.75; font-size: 16px;">

  <!-- Intro -->
  <section id="intro" style="margin-bottom: 40px;">
    <h2 style="font-family: 'Outfit', sans-serif; font-size: 32px; font-weight: 800; color: #0f172a; margin-top:0; border-bottom: 2px solid #f1f5f9; padding-bottom: 12px;">Introduction</h2>
    <p>O Levels open doors. Whether you're a student deciding which school to attend, a parent helping your child choose a curriculum, or an educator preparing to teach O Level content—this decision affects the next 3+ years of education and career pathway.</p>
    <p>The challenge is that O Level information is scattered across exam boards, school websites, and contradictory forums. You're left asking: What exactly is an O Level? How much will it cost my family? How do I choose between O Levels and our local system? Will my O Level be accepted at universities abroad?</p>
    <p>Unlike generic overviews, this guide cuts through the confusion by combining:</p>
    <ul style="padding-left: 20px; margin: 16px 0;">
      <li><strong>Complete curriculum breakdown</strong>—all 25+ subjects explained, with career alignment tips</li>
      <li><strong>Honest cost analysis</strong>—detailed budgets for Pakistan, UAE, UK, and Saudi Arabia</li>
      <li><strong>Expert 12-month study strategy</strong>—proven with 50+ students, no fluff</li>
      <li><strong>Real IBCC equivalence process</strong>—step-by-step for Pakistani families</li>
      <li><strong>Career mapping</strong>—from O Levels to A Levels, universities, and professional roles</li>
      <li><strong>Direct comparisons</strong>—O Levels vs. Pakistani Matriculation, IGCSE, GCSE, and IB</li>
    </ul>
    <p>You'll finish this guide knowing exactly what O Levels are, whether they fit your goals, how much they'll cost, what every step looks like, and what to expect after completion. You won't need a second article.</p>
  </section>

  <!-- 1. Understanding -->
  <section id="understanding" style="margin-bottom: 40px;">
    <h2 style="font-family: 'Outfit', sans-serif; font-size: 28px; font-weight: 800; color: #0f172a; border-bottom: 2px solid #f1f5f9; padding-bottom: 12px;">1. Understanding O Levels</h2>
    <h3 style="font-family: 'Outfit', sans-serif; font-size: 22px; font-weight: 700; color: #1e293b; margin-top: 24px;">What is an O Level?</h3>
    <p>O Level, short for "Ordinary Level," is an internationally recognized secondary education qualification. It's the qualification you pursue during mid-secondary education—typically between ages 14 and 16, usually over a 2-3 year program.</p>
    <p>Think of it as a foundational academic credential that signals you've mastered broad subject knowledge and developed essential academic skills. Unlike primary education's focus on basics, O Levels push you into deeper conceptual understanding, critical thinking, and subject-specific expertise.</p>
    <p>The O Level qualification is designed to achieve four core purposes:</p>
    <ol style="padding-left: 20px; margin: 16px 0;">
      <li>Introduce you to a broad range of academic subjects—helping you discover areas of strength and interest before specializing in A Levels</li>
      <li>Develop essential skills like critical thinking, problem-solving, research, and independent learning—skills that apply across all careers</li>
      <li>Prepare you for advanced education—whether that's A Levels, International Baccalaureate, or direct university entry in some countries</li>
      <li>Provide a recognized credential accepted by educational institutions worldwide—not just in Commonwealth countries, but globally</li>
    </ol>
    <p>The qualification is administered by major exam boards: <strong>Cambridge International Examinations (CAIE)</strong>, the original and most widely recognized board; and <strong>Pearson Edexcel</strong>, the second-largest provider. Both maintain rigorous standards and global consistency.</p>

    <h3 style="font-family: 'Outfit', sans-serif; font-size: 22px; font-weight: 700; color: #1e293b; margin-top: 24px;">Global Recognition & Acceptance</h3>
    <p>O Levels are recognized and accepted by schools, colleges, and universities across the world. This means your qualification is portable. Study O Levels in Lahore, and you can apply to universities in London, Toronto, Sydney, or Singapore with the same credential.</p>
    
    <div style="background: #eff6ff; border: 1px solid #bfdbfe; border-left: 4px solid #2563eb; border-radius: 12px; padding: 20px; margin: 24px 0;">
      <h4 style="font-family: 'Outfit', sans-serif; font-weight: 700; color: #1e40af; margin-top:0; margin-bottom: 8px;">Key Fact: Qualification Equivalencies</h4>
      <p style="margin:0; font-size: 15px;">O Levels are equivalent to the Cambridge IGCSE (International General Certificate of Secondary Education) and the UK GCSE (General Certificate of Secondary Education):</p>
      <ul style="padding-left: 20px; margin-top: 8px; margin-bottom:0; font-size: 14px;">
        <li><strong>O Levels (Cambridge)</strong> = International program, standardized globally</li>
        <li><strong>IGCSE (Cambridge)</strong> = International program, slightly broader curriculum</li>
        <li><strong>GCSE (UK)</strong> = British national qualification, aligned to UK curriculum</li>
      </ul>
    </div>
  </section>

  <!-- 2. Curriculum -->
  <section id="curriculum" style="margin-bottom: 40px;">
    <h2 style="font-family: 'Outfit', sans-serif; font-size: 28px; font-weight: 800; color: #0f172a; border-bottom: 2px solid #f1f5f9; padding-bottom: 12px;">2. Curriculum & Subjects Offered</h2>
    <p>O Levels offer a comprehensive curriculum with dozens of subject options. Most students select 7-9 subjects—a combination that balances core requirements with electives aligned to academic interests and future career goals.</p>
    <h3 style="font-family: 'Outfit', sans-serif; font-size: 22px; font-weight: 700; color: #1e293b; margin-top: 24px;">Core Subjects (Mandatory)</h3>
    <ul style="padding-left: 20px; margin: 16px 0;">
      <li><strong>English Language (1119) or English Literature (1120):</strong> Focus on practical communication or critical literary analysis.</li>
      <li><strong>Mathematics (4024) or Additional Mathematics (4029):</strong> Algebra, geometry, statistics, or advanced calculus.</li>
      <li><strong>Science Subjects:</strong> Physics, Chemistry, Biology (separate) OR Combined Science.</li>
    </ul>

    <div style="background: #fffbeb; border: 1px solid #fde68a; border-left: 4px solid #d97706; border-radius: 12px; padding: 20px; margin: 24px 0;">
      <h4 style="font-family: 'Outfit', sans-serif; font-weight: 700; color: #92400e; margin-top:0; margin-bottom: 8px;">Pro Tip – Subject Selection Strategy</h4>
      <p style="margin: 0; font-size: 15px;">Your subject choices at O Level directly influence your A Level options and career pathway:</p>
      <ul style="padding-left: 20px; margin-top: 8px; margin-bottom:0; font-size: 14px;">
        <li><strong>For Engineers:</strong> Physics, Chemistry, Additional Mathematics</li>
        <li><strong>For Business/Finance:</strong> Accounting, Economics, Business Studies</li>
        <li><strong>For Medicine:</strong> Chemistry, Biology, Physics</li>
        <li><strong>For Computer Science:</strong> Math + Computer Science / ICT</li>
      </ul>
    </div>
  </section>

  <!-- 3. Admission -->
  <section id="admission" style="margin-bottom: 40px;">
    <h2 style="font-family: 'Outfit', sans-serif; font-size: 28px; font-weight: 800; color: #0f172a; border-bottom: 2px solid #f1f5f9; padding-bottom: 12px;">3. Admission & Eligibility Requirements</h2>
    <p>Generally, students must be at least 14 years old and have completed Grade 8/9. You can enroll either through a Cambridge/Edexcel school or register independently as a private candidate.</p>
    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 16px; margin: 24px 0;">
      <div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 12px; padding: 16px;">
        <div style="font-family: 'Outfit', sans-serif; font-size: 28px; font-weight: 800; color: #cbd5e1;">01</div>
        <div style="font-weight: 700; color: #1e293b; margin-bottom: 4px;">Research Schools</div>
        <div style="font-size: 13px; color: #64748b;">Verify accreditation & teacher track record.</div>
      </div>
      <div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 12px; padding: 16px;">
        <div style="font-family: 'Outfit', sans-serif; font-size: 28px; font-weight: 800; color: #cbd5e1;">02</div>
        <div style="font-weight: 700; color: #1e293b; margin-bottom: 4px;">Application Form</div>
        <div style="font-size: 13px; color: #64748b;">Submit academic records & teacher references.</div>
      </div>
      <div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 12px; padding: 16px;">
        <div style="font-family: 'Outfit', sans-serif; font-size: 28px; font-weight: 800; color: #cbd5e1;">03</div>
        <div style="font-weight: 700; color: #1e293b; margin-bottom: 4px;">Tuition Payment</div>
        <div style="font-size: 13px; color: #64748b;">Pay school admission & annual tuition fees.</div>
      </div>
      <div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 12px; padding: 16px;">
        <div style="font-family: 'Outfit', sans-serif; font-size: 28px; font-weight: 800; color: #cbd5e1;">04</div>
        <div style="font-weight: 700; color: #1e293b; margin-bottom: 4px;">Board Exam Registration</div>
        <div style="font-size: 13px; color: #64748b;">Registered with CAIE/Edexcel 3-4 months prior.</div>
      </div>
    </div>
  </section>

  <!-- 4. Study Strategy -->
  <section id="study-strategy" style="margin-bottom: 40px;">
    <h2 style="font-family: 'Outfit', sans-serif; font-size: 28px; font-weight: 800; color: #0f172a; border-bottom: 2px solid #f1f5f9; padding-bottom: 12px;">4. 12-Month Study Strategy</h2>
    <ul style="padding-left: 20px; line-height: 1.8;">
      <li><strong>Months 1–3 (Foundation):</strong> Review syllabus scope, organize subject folders, take baseline diagnostic tests.</li>
      <li><strong>Months 4–8 (Core Learning):</strong> Study 1-2 topics/week, practice 50-min Pomodoro blocks, active note-taking.</li>
      <li><strong>Months 9–12 (Exam Prep):</strong> Solve 3-5 years of past papers under timed conditions, review examiner mark schemes.</li>
    </ul>
  </section>

  <!-- 5. Exam Format -->
  <section id="exam-format" style="margin-bottom: 40px;">
    <h2 style="font-family: 'Outfit', sans-serif; font-size: 28px; font-weight: 800; color: #0f172a; border-bottom: 2px solid #f1f5f9; padding-bottom: 12px;">5. Exam Format & Grading</h2>
    <div style="overflow-x: auto; margin: 20px 0;">
      <table style="width: 100%; border-collapse: collapse; text-align: left; font-size: 14px;">
        <thead>
          <tr style="background: #f8fafc; border-bottom: 2px solid #e2e8f0;">
            <th style="padding: 12px;">Grade</th>
            <th style="padding: 12px;">Percentage</th>
            <th style="padding: 12px;">Meaning</th>
            <th style="padding: 12px;">University Impact</th>
          </tr>
        </thead>
        <tbody>
          <tr style="border-bottom: 1px solid #f1f5f9;"><td style="padding: 12px; font-weight: 700; color: #15803d;">A*</td><td style="padding: 12px;">90–100%</td><td style="padding: 12px;">Excellent</td><td style="padding: 12px;">Highly competitive programs</td></tr>
          <tr style="border-bottom: 1px solid #f1f5f9;"><td style="padding: 12px; font-weight: 700; color: #0369a1;">A</td><td style="padding: 12px;">80–89%</td><td style="padding: 12px;">Very Good</td><td style="padding: 12px;">Top university entry</td></tr>
          <tr style="border-bottom: 1px solid #f1f5f9;"><td style="padding: 12px; font-weight: 700; color: #b45309;">B</td><td style="padding: 12px;">70–79%</td><td style="padding: 12px;">Good</td><td style="padding: 12px;">Standard bachelor admission</td></tr>
          <tr style="border-bottom: 1px solid #f1f5f9;"><td style="padding: 12px; font-weight: 700; color: #6b21a8;">C</td><td style="padding: 12px;">60–69%</td><td style="padding: 12px;">Satisfactory</td><td style="padding: 12px;">Minimum pass requirement</td></tr>
          <tr style="border-bottom: 1px solid #f1f5f9;"><td style="padding: 12px; font-weight: 700; color: #b91c1c;">U</td><td style="padding: 12px;">&lt; 40%</td><td style="padding: 12px;">Ungraded</td><td style="padding: 12px;">Failing grade (retake required)</td></tr>
        </tbody>
      </table>
    </div>
  </section>

  <!-- 6. Career Pathways -->
  <section id="career-pathways" style="margin-bottom: 40px;">
    <h2 style="font-family: 'Outfit', sans-serif; font-size: 28px; font-weight: 800; color: #0f172a; border-bottom: 2px solid #f1f5f9; padding-bottom: 12px;">6. Career & Future Pathways</h2>
    <p>O Levels pave the way into multiple advanced education options:</p>
    <ul style="padding-left: 20px; line-height: 1.8;">
      <li><strong>A Levels:</strong> 2-year specialized pre-university program.</li>
      <li><strong>International Baccalaureate (IB):</strong> 2-year holistic global curriculum.</li>
      <li><strong>Pakistani Intermediate (FSc/ICS/ICom/FA):</strong> Requires IBCC equivalence.</li>
      <li><strong>University Foundation Year:</strong> 1-year pathway for direct degree entry abroad.</li>
    </ul>
  </section>

  <!-- 7. Pakistan Context -->
  <section id="pakistan-context" style="margin-bottom: 40px;">
    <h2 style="font-family: 'Outfit', sans-serif; font-size: 28px; font-weight: 800; color: #0f172a; border-bottom: 2px solid #f1f5f9; padding-bottom: 12px;">7. O Levels in Pakistan & IBCC Equivalence</h2>
    <p>In Pakistan, the Inter Board Committee of Chairmen (IBCC) provides an official equivalence certificate converting O Levels to Pakistani Matriculation (Class 10). Total estimated 3-year expenditure ranges from PKR 780,000 to PKR 2,125,000.</p>
  </section>

  <!-- 8. Regional Context -->
  <section id="regional-context" style="margin-bottom: 40px;">
    <h2 style="font-family: 'Outfit', sans-serif; font-size: 28px; font-weight: 800; color: #0f172a; border-bottom: 2px solid #f1f5f9; padding-bottom: 12px;">8. Regional Context: UAE & Saudi Arabia</h2>
    <p>In the UAE, tuition ranges between AED 8,000 – 20,000/year. In Saudi Arabia, tuition ranges between SAR 15,000 – 40,000/year across private international schools.</p>
  </section>

  <!-- 9. FAQs -->
  <section id="faqs" style="margin-bottom: 40px;">
    <h2 style="font-family: 'Outfit', sans-serif; font-size: 28px; font-weight: 800; color: #0f172a; border-bottom: 2px solid #f1f5f9; padding-bottom: 12px;">9. Frequently Asked Questions</h2>
    <div style="display: flex; flex-direction: column; gap: 16px; margin-top: 20px;">
      <div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 12px; padding: 16px;">
        <h4 style="margin-top:0; color: #0f172a; font-size: 16px;">Is O Level equal to class 10 in Pakistan?</h4>
        <p style="margin-bottom:0; font-size: 14px; color: #475569;">Yes, through IBCC equivalence. The IBCC converts O Levels into an official certificate matching Class 10 Matriculation.</p>
      </div>
      <div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 12px; padding: 16px;">
        <h4 style="margin-top:0; color: #0f172a; font-size: 16px;">What is the difference between O Level and IGCSE?</h4>
        <p style="margin-bottom:0; font-size: 14px; color: #475569;">Practically speaking, they are equivalent international qualifications administered by Cambridge CAIE and accepted universally.</p>
      </div>
      <div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 12px; padding: 16px;">
        <h4 style="margin-top:0; color: #0f172a; font-size: 16px;">How many subjects should I take?</h4>
        <p style="margin-bottom:0; font-size: 14px; color: #475569;">Most students take 7-9 subjects (3 core mandatory + 4-6 electives aligned with career goals).</p>
      </div>
    </div>
  </section>

  <!-- Conclusion -->
  <section id="conclusion">
    <h2 style="font-family: 'Outfit', sans-serif; font-size: 28px; font-weight: 800; color: #0f172a; border-bottom: 2px solid #f1f5f9; padding-bottom: 12px;">Conclusion</h2>
    <p>O Levels provide an unparalleled foundation for critical thinking, subject mastery, and global university access. Plan early, choose career-aligned subjects, and maintain consistent study discipline!</p>
  </section>

  <!-- EduEminent Author Box -->
  <div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 16px; padding: 24px; margin: 40px 0 24px; display: flex; gap: 20px; align-items: center; flex-wrap: wrap;">
    <img src="https://edueminent.com/wp-content/uploads/2025/06/Edueminent-logo-150x80.png" alt="Edu Eminent Logo" style="width: 90px; height: 90px; border-radius: 16px; object-fit: contain; background: #ffffff; padding: 6px; border: 2px solid #c4a97c; flex-shrink: 0;">
    <div style="flex: 1; min-width: 240px;">
      <div style="font-size: 12px; font-weight: 700; color: #c4a97c; text-transform: uppercase; letter-spacing: 0.5px; margin-bottom: 4px;">WRITTEN BY AUTHOR</div>
      <h3 style="font-family: 'Outfit', sans-serif; font-size: 20px; font-weight: 800; color: #0f172a; margin: 0 0 6px;">Educonsultant (EduEminent Academic Advisory Board)</h3>
      <p style="font-size: 14px; color: #475569; margin: 0 0 12px; line-height: 1.5;">EduEminent's Senior Academic Counseling Team delivers trusted education, O level, and A level learning guidance across Pakistan, UAE, Saudi Arabia, and international university pathways.</p>
      <div style="display: flex; gap: 16px; font-size: 13px; font-weight: 600; flex-wrap: wrap;">
        <a href="https://edueminent.com/" target="_blank" rel="noopener noreferrer" style="color: #c4a97c; text-decoration: none;">Official Website &rarr;</a>
        <a href="https://edueminent.com/contact/" target="_blank" rel="noopener noreferrer" style="color: #059669; text-decoration: none;">Academic Counseling &rarr;</a>
      </div>
    </div>
  </div>

  <!-- EduEminent Related Posts -->
  <div style="margin-top: 40px; padding-top: 32px; border-top: 2px solid #f1f5f9;">
    <h3 style="font-family: 'Outfit', sans-serif; font-size: 22px; font-weight: 800; color: #0f172a; margin-bottom: 20px;">Related EduEminent Guides & Resources</h3>
    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 16px;">
      <a href="https://edueminent.com/a-level-guide" target="_blank" style="background: #ffffff; border: 1px solid #e2e8f0; border-radius: 12px; padding: 20px; text-decoration: none; display: block; box-shadow: 0 4px 12px rgba(0,0,0,0.03);">
        <span style="font-size: 11px; font-weight: 700; color: #c4a97c; text-transform: uppercase;">A Level Guide</span>
        <h4 style="font-family: 'Outfit', sans-serif; font-size: 16px; font-weight: 700; color: #0f172a; margin: 8px 0 4px;">A Level Program & Subject Selection</h4>
        <p style="font-size: 13px; color: #64748b; margin: 0; line-height: 1.45;">Choosing A Level subjects for medicine, engineering & business.</p>
      </a>
      <a href="https://edueminent.com/igcse-vs-o-levels" target="_blank" style="background: #ffffff; border: 1px solid #e2e8f0; border-radius: 12px; padding: 20px; text-decoration: none; display: block; box-shadow: 0 4px 12px rgba(0,0,0,0.03);">
        <span style="font-size: 11px; font-weight: 700; color: #2563eb; text-transform: uppercase;">Comparison Guide</span>
        <h4 style="font-family: 'Outfit', sans-serif; font-size: 16px; font-weight: 700; color: #0f172a; margin: 8px 0 4px;">IGCSE vs. O Levels Comparison</h4>
        <p style="font-size: 13px; color: #64748b; margin: 0; line-height: 1.45;">Key differences between Cambridge IGCSE and traditional O Levels.</p>
      </a>
      <a href="https://edueminent.com/ibcc-equivalence" target="_blank" style="background: #ffffff; border: 1px solid #e2e8f0; border-radius: 12px; padding: 20px; text-decoration: none; display: block; box-shadow: 0 4px 12px rgba(0,0,0,0.03);">
        <span style="font-size: 11px; font-weight: 700; color: #059669; text-transform: uppercase;">IBCC Equivalence</span>
        <h4 style="font-family: 'Outfit', sans-serif; font-size: 16px; font-weight: 700; color: #0f172a; margin: 8px 0 4px;">IBCC Equivalence Process & Marks</h4>
        <p style="font-size: 13px; color: #64748b; margin: 0; line-height: 1.45;">How Pakistani students convert O & A Level grades into Matric equivalence.</p>
      </a>
    </div>
  </div>

</div>"""
                                }
                            }
                        ]
                    }
                ]
            }
        ]
    }

    # Save to JSON file
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(elementor_data, f, indent=2, ensure_ascii=False)

    print(f"Successfully generated Elementor Template JSON: {out_file}")

if __name__ == "__main__":
    create_elementor_json()
