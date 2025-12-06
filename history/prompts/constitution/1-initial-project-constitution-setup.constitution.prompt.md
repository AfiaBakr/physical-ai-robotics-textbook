---
id: 1
title: "Initial Project Constitution Setup"
stage: constitution
date: 2025-12-06
surface: "agent"
model: "gemini"
branch: "main"
user: "user"
command: "/sp.constitution"
labels:
  - "constitution"
  - "setup"
links:
  spec: "null"
  ticket: "null"
  adr: "null"
  pr: "null"
files:
  - ".specify/memory/constitution.md"
  - ".specify/templates/tasks-template.md"
  - ".claude/commands/sp.plan.md"
  - ".claude/commands/sp.tasks.md"
tests:
  - "null"
---

# PROMPT

/sp.constitution

# RESPONSE

I have updated the constitution and ensured all dependent templates are consistent with the new principles.

The new constitution (v1.0.0) establishes four core principles:
1.  **Spec-Driven Development (SDD)**
2.  **Test-Driven Development (TDD)**
3.  **Simple, Composable Libraries**
4.  **Clear and Versioned APIs**

I have also updated the following files to align with these principles:
*   `.specify/templates/tasks-template.md` (Tests are now mandatory)
*   `.claude/commands/sp.plan.md` (Removed agent-specific reference)
*   `.claude/commands/sp.tasks.md` (Tests are now mandatory)

A suggested commit message is:
`docs: amend constitution to v1.0.0 (principle additions + governance update)`
