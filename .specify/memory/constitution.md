<!--
Sync Impact Report:

- Version change: None -> 1.0.0
- List of modified principles:
  - [PRINCIPLE_1_NAME] -> I. Spec-Driven Development (SDD)
  - [PRINCIPLE_2_NAME] -> II. Test-Driven Development (TDD)
  - [PRINCIPLE_3_NAME] -> III. Simple, Composable Libraries
  - [PRINCIPLE_4_NAME] -> IV. Clear and Versioned APIs
- Added sections:
  - Governance
- Removed sections:
  - [PRINCIPLE_5_NAME]
  - [PRINCIPLE_6_NAME]
  - [SECTION_2_NAME]
  - [SECTION_3_NAME]
- Templates requiring updates:
  - ✅ .specify/templates/plan-template.md
  - ✅ .specify/templates/spec-template.md
  - ✅ .specify/templates/tasks-template.md
- Follow-up TODOs: None
-->
# Gemini CLI Agent Constitution

## Core Principles

### I. Spec-Driven Development (SDD)
All development work MUST begin with a clear, written specification (`spec.md`). The spec defines the "what" and "why," and must be approved before implementation begins. It serves as the single source of truth for a feature's requirements.
**Rationale:** Ensures clarity, alignment, and a shared understanding of goals before writing code, reducing rework and ambiguity.

### II. Test-Driven Development (TDD)
All code MUST be developed using the Red-Green-Refactor cycle. A failing test (`red`) must be written before any implementation code. The goal is to make the test pass (`green`), and then refactor the code for clarity and efficiency while keeping the test passing.
**Rationale:** Produces a comprehensive test suite, improves code quality, and ensures that the implementation precisely matches the requirements defined by the tests.

### III. Simple, Composable Libraries
Features SHOULD be implemented as small, single-purpose, composable libraries. Each library must be independently testable and have a clear, well-defined public interface.
**Rationale:** Promotes code reuse, simplifies maintenance, and allows for easier testing and debugging. Large, monolithic systems are to be avoided.

### IV. Clear and Versioned APIs
Any public-facing interface, whether it's a CLI, a function library, or a web service, MUST have a clear, documented, and versioned API. Breaking changes MUST result in a MAJOR version increment (following Semantic Versioning).
**Rationale:** Provides stability for consumers of the API and makes a clear contract for how the software is intended to be used.

## Governance
This Constitution is the highest-level governing document for the project. Amendments to this Constitution require a proposal, review, and majority approval from the core team. All changes must be documented in a new version of this file. All code contributions will be evaluated for compliance with these principles during code review.

**Version**: 1.0.0 | **Ratified**: 2025-12-06 | **Last Amended**: 2025-12-06