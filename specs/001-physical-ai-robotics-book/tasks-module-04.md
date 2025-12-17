# Tasks: Module 4 - Vision-Language-Action (VLA) Systems

**Input**: Design documents from `/specs/001-physical-ai-robotics-book/`
**Prerequisites**: plan.md, spec.md, research.md, data-model.md, contracts/content-schema.yaml

**Tests**: Code validation and content quality tests are included as per constitution's TDD principle.

**Organization**: Tasks are grouped by lesson (3 lessons) to enable incremental implementation and testing.

**Scope**: Module 4 (Weeks 13-16) - Vision-Language-Action (VLA) Systems

## Format: `[ID] [P?] [Lesson] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Lesson]**: Which lesson this task belongs to (L1-L3)
- Include exact file paths in descriptions

## Module 4 Lesson Structure

| Lesson | Title | Content Focus |
|--------|-------|---------------|
| L1 | Introduction to Vision-Language-Action (VLA) Paradigm | VLA concept, multimodal AI, embodied cognition |
| L2 | VLA Pipeline Components & Integration | Speech recognition, LLM planning, ROS 2 action execution |
| L3 | End-to-End VLA Systems & Mini-Projects | Complete system integration, capstone projects |

## Path Conventions

Project root: `physical-ai-robotics-textbook/`
- Content: `docs/module-04-vla/` (3 lessons as MDX files)
- Labs: `labs/module-04/` (hands-on exercises)
- Assets: `static/diagrams/`, `static/img/`
- Scripts: `scripts/` (validation tools)
- Config: `docusaurus.config.ts`, `sidebars.ts`, `package.json`

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Verify Docusaurus project and establish Module 4 structure

- [ ] T001 Verify Docusaurus project exists in physical-ai-robotics-textbook/
- [ ] T002 Verify Mermaid and math plugins installed in package.json
- [ ] T003 Verify custom CSS black/gray theme in src/css/custom.css
- [ ] T004 Verify sidebars.ts and sidebarsLabs.ts configured
- [ ] T005 Create docs/module-04-vla/ directory for Module 4 content
- [ ] T006 [P] Create labs/module-04/ directory for Module 4 labs
- [ ] T007 [P] Create static/diagrams/module-04/ directory for Module 4 diagrams
- [ ] T008 [P] Create scripts/validate_code_examples.py for VLA code validation
- [ ] T009 [P] Create scripts/count_words.py for word count validation
- [ ] T010 Update sidebars.ts to include Module 4 navigation structure

**Checkpoint**: Module 4 directory structure ready

---

## Phase 2: Foundational (Module 4 Templates)

**Purpose**: Create templates and shared components for Module 4

- [ ] T011 Create docs/module-04-vla/_category_.json with module metadata
- [ ] T012 Create labs/module-04/_templates/lab-template.md with standard sections
- [ ] T013 [P] Create labs/module-04/_templates/validate-template.py for lab validation
- [ ] T014 [P] Create src/components/QuizComponent.jsx for lesson quizzes
- [ ] T015 Verify Docusaurus build succeeds with Module 4 structure (`npm run build`)

**Checkpoint**: Foundation ready - lesson content creation can begin

---

## Phase 3: Lesson 1 - Introduction to Vision-Language-Action (VLA) Paradigm (L1) 🎯 MVP

**Goal**: Students understand VLA concept, multimodal AI, and embodied cognition principles

**Independent Test**: Student explains VLA paradigm, describes multimodal integration, identifies key components

### Content for Lesson 1

- [ ] T016 [P] [L1] Write docs/module-04-vla/lesson-01-vla-introduction.mdx frontmatter and learning objectives
- [ ] T017 [P] [L1] Write Section 1.1: What is VLA? (200 words) in docs/module-04-vla/lesson-01-vla-introduction.mdx
- [ ] T018 [P] [L1] Write Section 1.2: Multimodal AI Principles (250 words) in docs/module-04-vla/lesson-01-vla-introduction.mdx
- [ ] T019 [P] [L1] Write Section 1.3: Embodied Cognition in VLA Systems (200 words) in docs/module-04-vla/lesson-01-vla-introduction.mdx
- [ ] T020 [P] [L1] Write Section 1.4: Real-World VLA Applications (150 words) in docs/module-04-vla/lesson-01-vla-introduction.mdx
- [ ] T021 [L1] Write Lesson 1 summary and preview of Lesson 2 in docs/module-04-vla/lesson-01-vla-introduction.mdx

### Diagrams for Lesson 1

- [ ] T022 [P] [L1] Create static/diagrams/module-04/vla-architecture.svg showing vision-language-action flow
- [ ] T023 [P] [L1] Create static/diagrams/module-04/multimodal-processing.svg with labeled components (vision, language, action)
- [ ] T024 [P] [L1] Create Mermaid diagram: speech → vision → LLM → action pipeline in docs/module-04-vla/lesson-01-vla-introduction.mdx
- [ ] T025 [L1] Embed diagrams with alt text in docs/module-04-vla/lesson-01-vla-introduction.mdx

### Citations for Lesson 1

- [ ] T026 [P] [L1] Add OpenVLA citation to docs/appendix/references.mdx
- [ ] T027 [P] [L1] Add RT-2 citation to docs/appendix/references.mdx
- [ ] T028 [P] [L1] Add recent VLA robotics citation (2023-2024) to docs/appendix/references.mdx

### Validation for Lesson 1

- [ ] T029 [L1] Run scripts/count_words.py to verify Lesson 1 is 750-900 words
- [ ] T030 [L1] Build Docusaurus and verify Lesson 1 renders without errors

**Checkpoint**: Lesson 1 complete - VLA foundation established

---

## Phase 4: Lesson 2 - VLA Pipeline Components & Integration (L2) 🎯 MVP

**Goal**: Students understand VLA pipeline components: speech recognition, LLM planning, ROS 2 action execution

**Independent Test**: Student explains each VLA component, draws VLA pipeline, describes multimodal data flow

### Content for Lesson 2

- [ ] T031 [P] [L2] Write docs/module-04-vla/lesson-02-vla-components.mdx frontmatter and learning objectives
- [ ] T032 [P] [L2] Write Section 2.1: VLA as Multimodal Integration (150 words) in docs/module-04-vla/lesson-02-vla-components.mdx
- [ ] T033 [P] [L2] Write Section 2.2: Speech Recognition & Command Parsing (200 words) in docs/module-04-vla/lesson-02-vla-components.mdx
- [ ] T034 [P] [L2] Write Section 2.3: LLM-Based Cognitive Planning (250 words) in docs/module-04-vla/lesson-02-vla-components.mdx
- [ ] T035 [P] [L2] Write Section 2.4: ROS 2 Action Execution (200 words) in docs/module-04-vla/lesson-02-vla-components.mdx
- [ ] T036 [P] [L2] Write Section 2.5: Vision Integration for Object-Aware Actions (150 words) in docs/module-04-vla/lesson-02-vla-components.mdx
- [ ] T037 [P] [L2] Write Section 2.6: The VLA Pipeline Flow (150 words) in docs/module-04-vla/lesson-02-vla-components.mdx
- [ ] T038 [L2] Write Lesson 2 summary and preview of Lesson 3 in docs/module-04-vla/lesson-02-vla-components.mdx

### Diagrams for Lesson 2

- [ ] T039 [P] [L2] Create Mermaid VLA pipeline diagram (speech → vision → LLM → action) in docs/module-04-vla/lesson-02-vla-components.mdx
- [ ] T040 [P] [L2] Create Mermaid sequence diagram: spoken command → processed → action in docs/module-04-vla/lesson-02-vla-components.mdx
- [ ] T041 [P] [L2] Create static/diagrams/module-04/vla-components-layers.svg showing component integration
- [ ] T042 [P] [L2] Create static/diagrams/module-04/multimodal-data-flow.svg showing data transformation

### Citations for Lesson 2

- [ ] T043 [P] [L2] Add Whisper speech recognition citation to docs/appendix/references.mdx
- [ ] T044 [P] [L2] Add LLM planning citation to docs/appendix/references.mdx
- [ ] T045 [P] [L2] Add VLA system architecture citations to docs/appendix/references.mdx

### Validation for Lesson 2

- [ ] T046 [L2] Run scripts/count_words.py to verify Lesson 2 is 1000-1200 words
- [ ] T047 [L2] Build Docusaurus and verify Lesson 2 renders without errors

**Checkpoint**: Lesson 2 complete - VLA pipeline understood

---

## Phase 5: Lesson 3 - End-to-End VLA Systems & Mini-Projects (L3) 🎯 MVP

**Goal**: Students understand complete VLA system integration and implement mini-projects

**Independent Test**: Student runs complete VLA pipeline, implements multimodal command processing, demonstrates end-to-end system

### Content for Lesson 3

- [ ] T048 [P] [L3] Write docs/module-04-vla/lesson-03-vla-integration.mdx frontmatter and learning objectives
- [ ] T049 [P] [L3] Write Section 3.1: Complete VLA System Architecture (150 words) in docs/module-04-vla/lesson-03-vla-integration.mdx
- [ ] T050 [P] [L3] Write Section 3.2: Integration Challenges (200 words) in docs/module-04-vla/lesson-03-vla-integration.mdx
- [ ] T051 [P] [L3] Write Section 3.3: Real-Time Processing Considerations (200 words) in docs/module-04-vla/lesson-03-vla-integration.mdx
- [ ] T052 [P] [L3] Write Section 3.4: Safety & Error Handling in VLA Systems (200 words) in docs/module-04-vla/lesson-03-vla-integration.mdx
- [ ] T053 [P] [L3] Write Section 3.5: Mini-Project Descriptions (200 words) in docs/module-04-vla/lesson-03-vla-integration.mdx
- [ ] T054 [L3] Write Lesson 3 summary and course conclusion in docs/module-04-vla/lesson-03-vla-integration.mdx

### Code Examples for Lesson 3

- [ ] T055 [P] [L3] Write VLA pipeline orchestrator example (30 lines Python) in docs/module-04-vla/lesson-03-vla-integration.mdx
- [ ] T056 [P] [L3] Write multimodal data flow example (25 lines Python) in docs/module-04-vla/lesson-03-vla-integration.mdx
- [ ] T057 [P] [L3] Write error handling example (20 lines Python) in docs/module-04-vla/lesson-03-vla-integration.mdx
- [ ] T058 [P] [L3] Write safety monitoring example (20 lines Python) in docs/module-04-vla/lesson-03-vla-integration.mdx
- [ ] T059 [L3] Add all code examples to scripts/validate_code_examples.py test suite

### Diagrams for Lesson 3

- [ ] T060 [P] [L3] Create static/diagrams/module-04/vla-system-architecture.svg (complete system view)
- [ ] T061 [P] [L3] Create Mermaid state diagram: VLA system states in docs/module-04-vla/lesson-03-vla-integration.mdx

### Mini-Projects for Lesson 3

- [X] T062 [P] [L3] Create labs/module-04/mini-project-01-simple-vla/README.md (basic speech-to-action)
- [X] T063 [P] [L3] Create labs/module-04/mini-project-01-simple-vla/starter/ with basic VLA template
- [X] T064 [P] [L3] Create labs/module-04/mini-project-01-simple-vla/solution/ with complete VLA implementation
- [X] T065 [P] [L3] Create labs/module-04/mini-project-01-simple-vla/validate.py to verify VLA pipeline
- [X] T066 [P] [L3] Create labs/module-04/mini-project-02-advanced-vla/README.md (object-aware VLA)
- [X] T067 [P] [L3] Create labs/module-04/mini-project-02-advanced-vla/starter/ with advanced template
- [X] T068 [P] [L3] Create labs/module-04/mini-project-02-advanced-vla/solution/ with complete system
- [X] T069 [P] [L3] Create labs/module-04/mini-project-02-advanced-vla/validate.py to test multimodal processing

### Review Quiz for Lesson 3

- [X] T070 [P] [L3] Create review quiz (10-15 questions) covering all 3 lessons using QuizComponent in docs/module-04-vla/lesson-03-vla-integration.mdx
- [X] T071 [L3] Include questions on: VLA paradigm, pipeline components, system integration

### Validation for Lesson 3

- [ ] T072 [L3] Run scripts/validate_code_examples.py to test all Python examples
- [ ] T073 [L3] Run labs/module-04/mini-project-01-simple-vla/validate.py
- [ ] T074 [L3] Run labs/module-04/mini-project-02-advanced-vla/validate.py
- [ ] T075 [L3] Run scripts/count_words.py to verify Lesson 3 is 1000-1200 words
- [ ] T076 [L3] Build Docusaurus and verify Lesson 3 renders without errors

**Checkpoint**: Lesson 3 complete - students can implement complete VLA systems

---

## Phase 6: Polish & Module 4 Finalization

**Purpose**: Final quality checks, validation, and Module 4 completion

### Content Finalization

- [ ] T077 [P] Create docs/module-04-vla/index.mdx with Module 4 overview and lesson navigation
- [ ] T078 [P] Update docs/intro.mdx to include Module 4 in course overview
- [ ] T079 [P] Update labs/intro.mdx to include Module 4 labs
- [ ] T080 [P] Update docs/module-03-perception/lesson-03-perception-pipelines.mdx to reference Module 4

### Validation Scripts

- [ ] T081 Run scripts/validate_code_examples.py on ALL Module 4 code examples
- [ ] T082 Run scripts/count_words.py to verify Module 4 total is 2500-3500 words
- [ ] T083 Run all lab validation scripts (mini-project-01 through mini-project-02)
- [ ] T084 Verify all VLA code examples run successfully

### Build & Deploy

- [X] T085 Run `npm run build` to verify Docusaurus builds without errors
- [ ] T086 Test Module 4 navigation in local development server
- [ ] T087 Verify all Mermaid diagrams render correctly
- [ ] T088 Verify all code examples have syntax highlighting
- [ ] T089 Test responsive design on mobile devices

### Documentation

- [ ] T090 [P] Add Module 4 learning outcomes summary to docs/appendix/references.mdx
- [X] T091 [P] Update sidebars.ts with final Module 4 navigation structure
- [ ] T092 Verify at least 6 APA citations for Module 4 in docs/appendix/references.mdx

### Final Review

- [ ] T093 Verify all success criteria met (SC-001: VLA understanding, SC-002: Pipeline integration)
- [ ] T094 Deploy to GitHub Pages using `npm run deploy` (if ready)

**Checkpoint**: Module 4 complete, validated, and ready for students

---

## Dependencies & Execution Order

### Phase Dependencies

- **Phase 1 (Setup)**: No dependencies - verify existing infrastructure
- **Phase 2 (Foundational)**: Depends on Setup - create Module 4 structure
- **Phases 3-5 (Lessons 1-3)**: All depend on Foundational phase
  - Lessons can proceed sequentially or in parallel
  - Recommended: L1 → L2 → L3 (conceptual flow)
- **Phase 6 (Polish)**: Depends on all lessons complete

### Within Each Lesson

- Content sections can be written in parallel [P]
- Diagrams can be created in parallel [P]
- Code examples can be written in parallel [P]
- Mini-projects can be created in parallel [P]
- Validation runs after content complete

### Parallel Opportunities

- All Setup tasks marked [P] (T006-T009)
- All content sections within a lesson marked [P]
- All diagrams within a lesson marked [P]
- All code examples within a lesson marked [P]
- All mini-project creation tasks marked [P]
- Polish tasks marked [P] (T077-T079, T090-T091)

---

## Implementation Strategy

### MVP First (Lessons 1-2 Only)

1. Complete Phase 1: Setup verification
2. Complete Phase 2: Module 4 structure
3. Complete Phase 3: Lesson 1 (VLA foundation)
4. Complete Phase 4: Lesson 2 (Pipeline components)
5. **STOP and VALIDATE**: Test Lessons 1-2 independently
6. Deploy/demo if ready - this is the core MVP!

### Incremental Delivery

1. Setup + Foundational → Foundation ready
2. Add Lesson 1 → Deploy/Demo (VLA concepts)
3. Add Lesson 2 → Deploy/Demo (Pipeline components)
4. Add Lesson 3 + Mini-Projects → Deploy/Demo (Complete Module 4)
5. Each lesson adds value without breaking previous lessons

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together
2. Once Phase 2 is done:
   - Writer A: Lessons 1-2 (theory content)
   - Writer B: Lesson 3 (integration + mini-projects)
   - Writer C: Mini-projects and validation
3. All converge for Phase 6 (Polish)

---

## Task Count Summary

| Phase | Task Count | Key Deliverables |
|-------|------------|------------------|
| Phase 1 (Setup) | 10 | Directory structure, validation scripts |
| Phase 2 (Foundational) | 5 | Templates, QuizComponent |
| Phase 3 (Lesson 1) | 15 | VLA introduction (~800 words), 3 diagrams, 3 citations |
| Phase 4 (Lesson 2) | 17 | Pipeline components (~1100 words), 4 diagrams, 3 citations |
| Phase 5 (Lesson 3) | 24 | Integration + mini-projects (~1100 words), 2 code examples, 2 mini-projects |
| Phase 6 (Polish) | 16 | Validation, build, deploy |
| **Total** | **87** | Complete Module 4 chapter with mini-projects and assessment |

---

## Success Metrics (Module 4)

| Metric | Target | Validation |
|--------|--------|------------|
| Word Count | 2500-3500 words | scripts/count_words.py |
| Code Examples | 100% run successfully | scripts/validate_code_examples.py |
| APA Citations | 6+ citations | Manual review |
| Mini-Projects | 2 projects | Project validate.py scripts |
| Diagrams | 8+ diagrams | Visual inspection |
| Quiz Questions | 10-15 questions | QuizComponent |
| Build | No errors | npm run build |

---

## Notes

- [P] tasks = different files, no dependencies, can run in parallel
- [Lesson] label (L1-L3) maps task to specific lesson for traceability
- All code examples target ROS 2 Humble with VLA integration
- All Python code must be 15-30 lines per example
- Word count targets per lesson: L1 (800), L2 (1100), L3 (1100)
- Total Module 4: ~3000 words
- Verify validation scripts pass before marking lesson complete
- Commit after each logical task group