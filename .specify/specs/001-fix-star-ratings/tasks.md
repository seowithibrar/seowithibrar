# Tasks Breakdown: Fix Star Rating Mojibake & Setup Spec-Kit

> **Spec Reference**: `.specify/specs/001-fix-star-ratings/spec.md`  
> **Plan Reference**: `.specify/specs/001-fix-star-ratings/plan.md`  

---

## Task Checklist

### 1. Website Encoding Fix
- [x] **Task 1.1**: Move `<meta charset="UTF-8">` to top of `<head>` in `index.html`
- [x] **Task 1.2**: Replace `★★★★★` with `&#9733;&#9733;&#9733;&#9733;&#9733;` in `index.html` line 180
- [x] **Task 1.3**: Update charset and testimonial star entities in `seo-services-lahore.html`
- [x] **Task 1.4**: Update charset and testimonial star entities in `about.html`
- [x] **Task 1.5**: Update charset and testimonial star entities in `contact.html`
- [x] **Task 1.6**: Update `rebuild_index.py` script with entity format

### 2. GitHub Spec-Kit Architecture
- [x] **Task 2.1**: Author `.specify/memory/constitution.md` with project rules and gates
- [x] **Task 2.2**: Create `.specify/templates/spec-template.md`
- [x] **Task 2.3**: Create `.specify/templates/plan-template.md`
- [x] **Task 2.4**: Create `.specify/templates/tasks-template.md`
- [x] **Task 2.5**: Document setup in `.specify/README.md`
- [x] **Task 2.6**: Record initial execution spec in `.specify/specs/001-fix-star-ratings/`

### 3. Verification
- [x] Verify `index.html` structure and character entity rendering
- [x] Verify `.specify/` files created and valid
- [x] Generate walkthrough report
