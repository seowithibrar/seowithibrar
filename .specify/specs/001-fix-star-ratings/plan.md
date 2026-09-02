# Technical Plan: Fix Star Rating Mojibake & Setup Spec-Kit

> **Spec Reference**: `.specify/specs/001-fix-star-ratings/spec.md`  
> **Status**: Completed  

---

## 1. Architectural Overview
- Replace raw multibyte Unicode star characters with HTML numeric entity references (`&#9733;`), which are decoded identically by all browsers regardless of transport encoding headers.
- Re-position `<meta charset="UTF-8">` to line 4 directly below `<head>` in `index.html` and related pages.
- Scaffold `.specify/` with constitution, templates, and specs.

---

## 2. File Map

| Action | File Path | Purpose |
| :--- | :--- | :--- |
| `MODIFY` | `index.html` | Fix charset order and hero badge star rating entities |
| `MODIFY` | `seo-services-lahore.html` | Fix charset order and testimonial star entities |
| `MODIFY` | `about.html` | Fix charset order and testimonial star entities |
| `MODIFY` | `contact.html` | Fix charset order and testimonial star entities |
| `MODIFY` | `rebuild_index.py` | Sync script with HTML entities for star ratings |
| `NEW` | `.specify/memory/constitution.md` | Core project constitution |
| `NEW` | `.specify/templates/*` | Spec-Kit standard templates |
| `NEW` | `.specify/README.md` | Spec-Kit documentation |
