# Spec Kit (Spec-Driven Development)

This repository is equipped with GitHub's **Spec Kit** architecture for **Spec-Driven Development (SDD)** with AI coding agents.

## Structure

```
.specify/
├── memory/
│   └── constitution.md     # Project principles, non-negotiables, and engineering standards
├── templates/
│   ├── spec-template.md    # Standard feature specification template
│   ├── plan-template.md    # Technical implementation blueprint template
│   └── tasks-template.md   # Actionable task checklist template
└── specs/                  # Feature specifications and execution artifacts
    └── 001-fix-star-ratings/
```

## Workflow Lifecycle

1. **Constitution**: The foundation rules in `.specify/memory/constitution.md` (aligned with `AGENTS.md`) guide every decision.
2. **Specify**: Define *what* you want to build and *why* using `spec-template.md`. Focus on intent and acceptance criteria.
3. **Plan**: Derive a technical architecture and file impact map using `plan-template.md`.
4. **Tasks**: Break down the blueprint into atomic, checkable tasks using `tasks-template.md`.
5. **Implement**: Execute tasks one by one, keeping existing functionality protected.
6. **Verify**: Test responsive layouts, character encodings, and SEO integrity.
