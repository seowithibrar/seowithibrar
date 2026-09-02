# Project Constitution

> **Status**: Active  
> **Source of Truth**: Aligned with `AGENTS.md`  
> **Scope**: All AI-assisted and human development across the `seowithibrar` website and assets.

---

## 1. Core Principles & Philosophy

1. **Production-Ready Only**: Every deliverable must be fully functional, styled, accessible, and tested. No placeholder code, mock data, or partial implementations.
2. **Existing Code Protection**:
   - Never break existing functionality or delete working features.
   - Never remove working code or refactor unrelated files.
   - Strictly touch only the files required for the assigned task.
3. **Spec-Driven Progression**: No code should be written without clear intent, specification, and validation criteria.

---

## 2. Permissions & Gates (Mandatory Approval)

Stop and require explicit user approval before executing any of the following:
- Deleting, moving, or renaming files
- Installing or updating packages/dependencies
- Changing folder or repository structure
- Database or schema modifications
- Global CSS or JavaScript changes
- Navigation or header/footer redesigns
- Large-scale UI alterations
- SEO architecture or permalink restructuring

---

## 3. Engineering & Code Standards

- **Semantic & Clean HTML**: Always use proper HTML5 semantic elements (`<header>`, `<nav>`, `<main>`, `<section>`, `<article>`, `<footer>`).
- **UTF-8 & Character Encodings**:
  - Always declare `<meta charset="UTF-8">` as the very first child of `<head>`.
  - Use HTML character entities (e.g., `&#9733;` for stars) or SVG vectors for special symbols to avoid encoding mojibake across diverse clients/browsers.
- **Maintainable CSS**:
  - Use CSS custom properties defined in design system tokens.
  - Maintain pixel-perfect spacing, fluid typography, and consistent color harmony.
- **Performant JavaScript**:
  - Modular, vanilla JS with no unneeded library dependencies.
  - Zero console errors and graceful degradation.

---

## 4. SEO & Accessibility Mandates

- Exactly one `<h1>` per page reflecting the primary keyword and search intent.
- Proper heading hierarchy (`<h1>` → `<h2>` → `<h3>`) without skipping levels.
- Comprehensive descriptive meta tags: `title`, `description`, `canonical`, and Open Graph / Twitter cards.
- Meaningful `alt` attributes on all images.
- Valid Schema.org JSON-LD structured data.
- Meet WCAG 2.1 AA accessibility standards for color contrast, focus outlines, and keyboard navigation.

---

## 5. Spec-Driven Development (SDD) Workflow

For every new feature or major change:
1. **Constitution**: Ensure alignment with this rulebook.
2. **Specify (`/speckit.specify`)**: Draft the feature specification in `.specify/specs/`.
3. **Plan (`/speckit.plan`)**: Formulate a technical blueprint and file map.
4. **Tasks (`/speckit.tasks`)**: Break the plan into granular, verifiable checkboxes.
5. **Implement (`/speckit.implement`)**: Execute step-by-step with continuous validation.
6. **Verify (`/speckit.converge`)**: Test responsive behavior, check console, and confirm intent.
