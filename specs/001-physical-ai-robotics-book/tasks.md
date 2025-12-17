# Tasks: Module 1 - The Robotic Nervous System (ROS 2)

**Input**: Design documents from `/specs/001-physical-ai-robotics-book/`
**Prerequisites**: plan.md, spec.md, research.md, data-model.md, contracts/content-schema.yaml

**Tests**: Code validation and content quality tests are included as per constitution's TDD principle.

**Organization**: Tasks are grouped by lesson (5 lessons) to enable incremental implementation and testing.

**Scope**: Module 1 (Weeks 1-4) - The Robotic Nervous System (ROS 2)

## Format: `[ID] [P?] [Lesson] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Lesson]**: Which lesson this task belongs to (L1-L5)
- Include exact file paths in descriptions

## Module 1 Lesson Structure

| Lesson | Title | Content Focus |
|--------|-------|---------------|
| L1 | Physical AI & the Robotic Nervous System | Physical AI intro, embodied intelligence, ROS 2 as nervous system |
| L2 | ROS 2 Core Architecture | Nodes, Topics, Services, Actions, ROS Graph |
| L3 | Python Agents with rclpy | rclpy basics, publishers, subscribers, services |
| L4 | Humanoid URDF Fundamentals | URDF structure, links, joints, coordinate frames |
| L5 | Simulation, Practice & Review | Simulation workflow, mini-projects, summary, quiz |

## Path Conventions

Project root: `physical-ai-robotics-textbook/`
- Content: `docs/module-01-ros2/` (5 lessons as MDX files)
- Labs: `labs/module-01/` (hands-on exercises)
- Assets: `static/diagrams/`, `static/img/`
- Scripts: `scripts/` (validation tools)
- Config: `docusaurus.config.ts`, `sidebars.ts`, `package.json`

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Verify Docusaurus project and establish Module 1 structure

- [X] T001 Verify Docusaurus project exists in physical-ai-robotics-textbook/
- [X] T002 Verify Mermaid and math plugins installed in package.json
- [X] T003 Verify custom CSS black/gray theme in src/css/custom.css
- [X] T004 Verify sidebars.ts and sidebarsLabs.ts configured
- [ ] T005 Create docs/module-01-ros2/ directory for Module 1 content
- [ ] T006 [P] Create labs/module-01/ directory for Module 1 labs
- [ ] T007 [P] Create static/diagrams/module-01/ directory for Module 1 diagrams
- [ ] T008 [P] Create scripts/validate_code_examples.py for ROS 2 code validation
- [ ] T009 [P] Create scripts/count_words.py for word count validation
- [ ] T010 Update sidebars.ts to include Module 1 navigation structure

**Checkpoint**: Module 1 directory structure ready

---

## Phase 2: Foundational (Module 1 Templates)

**Purpose**: Create templates and shared components for Module 1

- [ ] T011 Create docs/module-01-ros2/_category_.json with module metadata
- [ ] T012 Create labs/module-01/_templates/lab-template.md with standard sections
- [ ] T013 [P] Create labs/module-01/_templates/validate-template.py for lab validation
- [ ] T014 [P] Create src/components/QuizComponent.jsx for lesson quizzes
- [ ] T015 Verify Docusaurus build succeeds with Module 1 structure (`npm run build`)

**Checkpoint**: Foundation ready - lesson content creation can begin

---

## Phase 3: Lesson 1 - Physical AI & the Robotic Nervous System (L1) 🎯 MVP

**Goal**: Students understand Physical AI, embodied intelligence, and why ROS 2 is the "nervous system"

**Independent Test**: Student explains Physical AI vs digital AI, describes embodied intelligence, identifies ROS 2's role

### Content for Lesson 1

- [ ] T016 [P] [L1] Write docs/module-01-ros2/lesson-01-physical-ai.mdx frontmatter and learning objectives
- [ ] T017 [P] [L1] Write Section 1.1: What is Physical AI? (200 words) in docs/module-01-ros2/lesson-01-physical-ai.mdx
- [ ] T018 [P] [L1] Write Section 1.2: Embodied Intelligence Principles (250 words) in docs/module-01-ros2/lesson-01-physical-ai.mdx
- [ ] T019 [P] [L1] Write Section 1.3: The Robotic Nervous System Concept (200 words) in docs/module-01-ros2/lesson-01-physical-ai.mdx
- [ ] T020 [P] [L1] Write Section 1.4: Real-World Humanoid Robotics (150 words) in docs/module-01-ros2/lesson-01-physical-ai.mdx
- [ ] T021 [L1] Write Lesson 1 summary and preview of Lesson 2 in docs/module-01-ros2/lesson-01-physical-ai.mdx

### Diagrams for Lesson 1

- [ ] T022 [P] [L1] Create static/diagrams/module-01/physical-ai-vs-digital-ai.svg comparing AI paradigms
- [ ] T023 [P] [L1] Create static/diagrams/module-01/humanoid-anatomy.svg with labeled components (sensors, actuators, joints)
- [ ] T024 [P] [L1] Create Mermaid diagram: perception → reasoning → action loop in docs/module-01-ros2/lesson-01-physical-ai.mdx
- [ ] T025 [L1] Embed diagrams with alt text in docs/module-01-ros2/lesson-01-physical-ai.mdx

### Citations for Lesson 1

- [ ] T026 [P] [L1] Add Brooks (1999) citation to docs/appendix/references.mdx
- [ ] T027 [P] [L1] Add Pfeifer & Bongard (2007) citation to docs/appendix/references.mdx
- [ ] T028 [P] [L1] Add recent humanoid robotics citation (2020+) to docs/appendix/references.mdx

### Validation for Lesson 1

- [ ] T029 [L1] Run scripts/count_words.py to verify Lesson 1 is 750-900 words
- [ ] T030 [L1] Build Docusaurus and verify Lesson 1 renders without errors

**Checkpoint**: Lesson 1 complete - Physical AI foundation established

---

## Phase 4: Lesson 2 - ROS 2 Core Architecture (L2) 🎯 MVP

**Goal**: Students understand ROS 2 nodes, topics, services, actions, and ROS graph

**Independent Test**: Student explains each ROS 2 component, draws ROS graph, describes message flow

### Content for Lesson 2

- [ ] T031 [P] [L2] Write docs/module-01-ros2/lesson-02-ros2-architecture.mdx frontmatter and learning objectives
- [ ] T032 [P] [L2] Write Section 2.1: ROS 2 as the Robotic Nervous System (150 words) in docs/module-01-ros2/lesson-02-ros2-architecture.mdx
- [ ] T033 [P] [L2] Write Section 2.2: Nodes - Independent Processes (200 words) in docs/module-01-ros2/lesson-02-ros2-architecture.mdx
- [ ] T034 [P] [L2] Write Section 2.3: Topics - Asynchronous Messaging (250 words) in docs/module-01-ros2/lesson-02-ros2-architecture.mdx
- [ ] T035 [P] [L2] Write Section 2.4: Services - Request-Response (200 words) in docs/module-01-ros2/lesson-02-ros2-architecture.mdx
- [ ] T036 [P] [L2] Write Section 2.5: Actions - Long-Running Tasks (150 words) in docs/module-01-ros2/lesson-02-ros2-architecture.mdx
- [ ] T037 [P] [L2] Write Section 2.6: The ROS Graph (150 words) in docs/module-01-ros2/lesson-02-ros2-architecture.mdx
- [ ] T038 [L2] Write Lesson 2 summary and preview of Lesson 3 in docs/module-01-ros2/lesson-02-ros2-architecture.mdx

### Diagrams for Lesson 2

- [ ] T039 [P] [L2] Create Mermaid ROS 2 graph diagram (nodes + topics) in docs/module-01-ros2/lesson-02-ros2-architecture.mdx
- [ ] T040 [P] [L2] Create Mermaid sequence diagram: publisher → topic → subscriber in docs/module-01-ros2/lesson-02-ros2-architecture.mdx
- [ ] T041 [P] [L2] Create Mermaid sequence diagram: service client → server → response in docs/module-01-ros2/lesson-02-ros2-architecture.mdx
- [ ] T042 [P] [L2] Create static/diagrams/module-01/ros2-architecture-layers.svg showing DDS foundation

### Citations for Lesson 2

- [ ] T043 [P] [L2] Add Quigley et al. (2009) ROS citation to docs/appendix/references.mdx
- [ ] T044 [P] [L2] Add Macenski et al. (2022) ROS 2 citation to docs/appendix/references.mdx
- [ ] T045 [P] [L2] Add ROS 2 Documentation (2024) citations to docs/appendix/references.mdx

### Validation for Lesson 2

- [ ] T046 [L2] Run scripts/count_words.py to verify Lesson 2 is 1000-1200 words
- [ ] T047 [L2] Build Docusaurus and verify Lesson 2 renders without errors

**Checkpoint**: Lesson 2 complete - ROS 2 architecture understood

---

## Phase 5: Lesson 3 - Python Agents with rclpy (L3) 🎯 MVP

**Goal**: Students create ROS 2 nodes with Python, implement pub/sub and services

**Independent Test**: Student runs publisher/subscriber nodes, creates service, verifies message exchange

### Content for Lesson 3

- [ ] T048 [P] [L3] Write docs/module-01-ros2/lesson-03-rclpy-agents.mdx frontmatter and learning objectives
- [ ] T049 [P] [L3] Write Section 3.1: Introduction to rclpy (150 words) in docs/module-01-ros2/lesson-03-rclpy-agents.mdx
- [ ] T050 [P] [L3] Write Section 3.2: Creating Your First Node (200 words) in docs/module-01-ros2/lesson-03-rclpy-agents.mdx
- [ ] T051 [P] [L3] Write Section 3.3: Publisher Node (200 words) in docs/module-01-ros2/lesson-03-rclpy-agents.mdx
- [ ] T052 [P] [L3] Write Section 3.4: Subscriber Node (200 words) in docs/module-01-ros2/lesson-03-rclpy-agents.mdx
- [ ] T053 [P] [L3] Write Section 3.5: Service Server (200 words) in docs/module-01-ros2/lesson-03-rclpy-agents.mdx
- [ ] T054 [P] [L3] Write Section 3.6: Agent Pattern - Perception to Action (200 words) in docs/module-01-ros2/lesson-03-rclpy-agents.mdx
- [ ] T055 [L3] Write Lesson 3 summary and preview of Lesson 4 in docs/module-01-ros2/lesson-03-rclpy-agents.mdx

### Code Examples for Lesson 3

- [ ] T056 [P] [L3] Write minimal ROS 2 node (10 lines Python) in docs/module-01-ros2/lesson-03-rclpy-agents.mdx
- [ ] T057 [P] [L3] Write publisher node example (20 lines Python) in docs/module-01-ros2/lesson-03-rclpy-agents.mdx
- [ ] T058 [P] [L3] Write subscriber node example (15 lines Python) in docs/module-01-ros2/lesson-03-rclpy-agents.mdx
- [ ] T059 [P] [L3] Write service server example (20 lines Python) in docs/module-01-ros2/lesson-03-rclpy-agents.mdx
- [ ] T060 [P] [L3] Write simple agent loop example (25 lines Python) in docs/module-01-ros2/lesson-03-rclpy-agents.mdx
- [ ] T061 [L3] Add all code examples to scripts/validate_code_examples.py test suite

### Diagrams for Lesson 3

- [ ] T062 [P] [L3] Create static/diagrams/module-01/agent-controller-interface.svg (perception-planning-action)

### Labs for Lesson 3

- [ ] T063 [P] [L3] Create labs/module-01/lab-01-hello-ros2/README.md (60 min, first node)
- [ ] T064 [P] [L3] Create labs/module-01/lab-01-hello-ros2/starter/ with minimal node template
- [ ] T065 [P] [L3] Create labs/module-01/lab-01-hello-ros2/solution/ with complete node
- [ ] T066 [P] [L3] Create labs/module-01/lab-01-hello-ros2/validate.py to verify node runs
- [ ] T067 [P] [L3] Create labs/module-01/lab-02-pubsub/README.md (90 min, pub/sub pair)
- [ ] T068 [P] [L3] Create labs/module-01/lab-02-pubsub/starter/ with templates
- [ ] T069 [P] [L3] Create labs/module-01/lab-02-pubsub/solution/ with working pair
- [ ] T070 [P] [L3] Create labs/module-01/lab-02-pubsub/validate.py to verify message exchange
- [ ] T071 [P] [L3] Create labs/module-01/lab-03-services/README.md (90 min, service)
- [ ] T072 [P] [L3] Create labs/module-01/lab-03-services/starter/ with service template
- [ ] T073 [P] [L3] Create labs/module-01/lab-03-services/solution/ with working service
- [ ] T074 [P] [L3] Create labs/module-01/lab-03-services/validate.py to test service calls

### Validation for Lesson 3

- [ ] T075 [L3] Run scripts/validate_code_examples.py to test all Python examples
- [ ] T076 [L3] Run labs/module-01/lab-01-hello-ros2/validate.py
- [ ] T077 [L3] Run labs/module-01/lab-02-pubsub/validate.py
- [ ] T078 [L3] Run labs/module-01/lab-03-services/validate.py
- [ ] T079 [L3] Run scripts/count_words.py to verify Lesson 3 is 1100-1300 words
- [ ] T080 [L3] Build Docusaurus and verify Lesson 3 renders without errors

**Checkpoint**: Lesson 3 complete - students can create ROS 2 Python agents

---

## Phase 6: Lesson 4 - Humanoid URDF Fundamentals (L4)

**Goal**: Students understand URDF structure, create simple robot models

**Independent Test**: Student creates 2-DOF arm URDF, spawns in RViz, verifies joints work

### Content for Lesson 4

- [ ] T081 [P] [L4] Write docs/module-01-ros2/lesson-04-urdf-fundamentals.mdx frontmatter and learning objectives
- [ ] T082 [P] [L4] Write Section 4.1: What is URDF? (150 words) in docs/module-01-ros2/lesson-04-urdf-fundamentals.mdx
- [ ] T083 [P] [L4] Write Section 4.2: Links - Robot Body Parts (200 words) in docs/module-01-ros2/lesson-04-urdf-fundamentals.mdx
- [ ] T084 [P] [L4] Write Section 4.3: Joints - Connections (200 words) in docs/module-01-ros2/lesson-04-urdf-fundamentals.mdx
- [ ] T085 [P] [L4] Write Section 4.4: Coordinate Frames (150 words) in docs/module-01-ros2/lesson-04-urdf-fundamentals.mdx
- [ ] T086 [P] [L4] Write Section 4.5: Simplified Humanoid Model (200 words) in docs/module-01-ros2/lesson-04-urdf-fundamentals.mdx
- [ ] T087 [L4] Write Lesson 4 summary and preview of Lesson 5 in docs/module-01-ros2/lesson-04-urdf-fundamentals.mdx

### Code Examples for Lesson 4

- [ ] T088 [P] [L4] Write 2-DOF arm URDF example (15 lines XML) in docs/module-01-ros2/lesson-04-urdf-fundamentals.mdx
- [ ] T089 [P] [L4] Write humanoid upper body URDF snippet (20 lines XML) in docs/module-01-ros2/lesson-04-urdf-fundamentals.mdx

### Diagrams for Lesson 4

- [ ] T090 [P] [L4] Create Mermaid tree diagram: URDF link-joint hierarchy in docs/module-01-ros2/lesson-04-urdf-fundamentals.mdx
- [ ] T091 [P] [L4] Create static/diagrams/module-01/urdf-hierarchy.svg showing 2-DOF arm structure
- [ ] T092 [P] [L4] Create static/diagrams/module-01/humanoid-kinematic-chain.svg showing upper body

### Citations for Lesson 4

- [ ] T093 [P] [L4] Add URDF XML Specification citation to docs/appendix/references.mdx
- [ ] T094 [P] [L4] Add Willow Garage URDF Tutorial citation to docs/appendix/references.mdx

### Lab for Lesson 4

- [ ] T095 [P] [L4] Create labs/module-01/lab-04-urdf-basics/README.md (120 min, 2-DOF arm)
- [ ] T096 [P] [L4] Create labs/module-01/lab-04-urdf-basics/starter/ with single-link URDF
- [ ] T097 [P] [L4] Create labs/module-01/lab-04-urdf-basics/solution/ with complete 2-DOF arm
- [ ] T098 [P] [L4] Create labs/module-01/lab-04-urdf-basics/validate.py to parse and verify URDF

### Validation for Lesson 4

- [ ] T099 [L4] Run labs/module-01/lab-04-urdf-basics/validate.py
- [ ] T100 [L4] Run scripts/count_words.py to verify Lesson 4 is 850-1000 words
- [ ] T101 [L4] Build Docusaurus and verify Lesson 4 renders without errors

**Checkpoint**: Lesson 4 complete - students can create URDF models

---

## Phase 7: Lesson 5 - Simulation, Practice & Review (L5)

**Goal**: Students understand simulation workflow, complete mini-projects, demonstrate learning

**Independent Test**: Student completes mini-project, passes review quiz with 80%+

### Content for Lesson 5

- [ ] T102 [P] [L5] Write docs/module-01-ros2/lesson-05-simulation-review.mdx frontmatter and learning objectives
- [ ] T103 [P] [L5] Write Section 5.1: Simulation Workflow (200 words) in docs/module-01-ros2/lesson-05-simulation-review.mdx
- [ ] T104 [P] [L5] Write Section 5.2: Gazebo/Isaac Sim Overview (200 words) in docs/module-01-ros2/lesson-05-simulation-review.mdx
- [ ] T105 [P] [L5] Write Section 5.3: Connecting URDF with ROS 2 Nodes (200 words) in docs/module-01-ros2/lesson-05-simulation-review.mdx
- [ ] T106 [P] [L5] Write Section 5.4: Mini-Project Descriptions (300 words) in docs/module-01-ros2/lesson-05-simulation-review.mdx
- [ ] T107 [P] [L5] Write Section 5.5: Module 1 Summary (200 words) in docs/module-01-ros2/lesson-05-simulation-review.mdx
- [ ] T108 [L5] Write Module 1 key takeaways in docs/module-01-ros2/lesson-05-simulation-review.mdx

### Mini-Projects for Lesson 5

- [ ] T109 [P] [L5] Create labs/module-01/mini-project-01-robot-talker/README.md (multi-node ROS 2 system)
- [ ] T110 [P] [L5] Create labs/module-01/mini-project-01-robot-talker/starter/ with project template
- [ ] T111 [P] [L5] Create labs/module-01/mini-project-01-robot-talker/solution/ with reference implementation
- [ ] T112 [P] [L5] Create labs/module-01/mini-project-02-arm-controller/README.md (URDF + ROS 2 control)
- [ ] T113 [P] [L5] Create labs/module-01/mini-project-02-arm-controller/starter/ with project template
- [ ] T114 [P] [L5] Create labs/module-01/mini-project-02-arm-controller/solution/ with reference implementation

### Review Quiz for Lesson 5

- [ ] T115 [P] [L5] Create review quiz (10-15 questions) covering all 5 lessons using QuizComponent in docs/module-01-ros2/lesson-05-simulation-review.mdx
- [ ] T116 [L5] Include questions on: Physical AI, ROS 2 concepts, rclpy, URDF, simulation workflow

### Diagrams for Lesson 5

- [ ] T117 [P] [L5] Create Mermaid flowchart: simulation workflow (URDF → spawn → control → feedback) in docs/module-01-ros2/lesson-05-simulation-review.mdx
- [ ] T118 [P] [L5] Create static/diagrams/module-01/module-overview.svg summarizing Module 1 concepts

### Validation for Lesson 5

- [ ] T119 [L5] Run scripts/count_words.py to verify Lesson 5 is 1000-1200 words
- [ ] T120 [L5] Build Docusaurus and verify Lesson 5 renders without errors

**Checkpoint**: Lesson 5 complete - Module 1 content fully delivered

---

## Phase 8: Polish & Module 1 Finalization

**Purpose**: Final quality checks, validation, and Module 1 completion

### Content Finalization

- [ ] T121 [P] Create docs/module-01-ros2/index.mdx with Module 1 overview and lesson navigation
- [ ] T122 [P] Update docs/intro.mdx to include Module 1 in course overview
- [ ] T123 [P] Update labs/intro.mdx to include Module 1 labs

### Validation Scripts

- [ ] T124 Run scripts/validate_code_examples.py on ALL Module 1 code examples
- [ ] T125 Run scripts/count_words.py to verify Module 1 total is 4500-5500 words
- [ ] T126 Run all lab validation scripts (lab-01 through lab-04, mini-projects)

### Build & Deploy

- [ ] T127 Run `npm run build` to verify Docusaurus builds without errors
- [ ] T128 Test Module 1 navigation in local development server
- [ ] T129 Verify all Mermaid diagrams render correctly
- [ ] T130 Verify all code examples have syntax highlighting
- [ ] T131 Test responsive design on mobile devices

### Documentation

- [ ] T132 [P] Add Module 1 learning outcomes summary to docs/appendix/references.mdx
- [ ] T133 [P] Update sidebars.ts with final Module 1 navigation structure
- [ ] T134 Verify at least 9 APA citations for Module 1 in docs/appendix/references.mdx

### Final Review

- [ ] T135 Verify all success criteria met (SC-001: ROS 2 setup, SC-005: Physical AI, SC-012: code runs)
- [ ] T136 Deploy to GitHub Pages using `npm run deploy` (if ready)

**Checkpoint**: Module 1 complete, validated, and ready for students

---

## Dependencies & Execution Order

### Phase Dependencies

- **Phase 1 (Setup)**: No dependencies - verify existing infrastructure
- **Phase 2 (Foundational)**: Depends on Setup - create Module 1 structure
- **Phases 3-7 (Lessons 1-5)**: All depend on Foundational phase
  - Lessons can proceed sequentially or in parallel
  - Recommended: L1 → L2 → L3 → L4 → L5 (conceptual flow)
- **Phase 8 (Polish)**: Depends on all lessons complete

### Within Each Lesson

- Content sections can be written in parallel [P]
- Diagrams can be created in parallel [P]
- Code examples can be written in parallel [P]
- Labs can be created in parallel [P]
- Validation runs after content complete

### Parallel Opportunities

- All Setup tasks marked [P] (T006-T009)
- All content sections within a lesson marked [P]
- All diagrams within a lesson marked [P]
- All code examples within a lesson marked [P]
- All lab creation tasks marked [P]
- Polish tasks marked [P] (T121-T123, T132-T133)

---

## Parallel Example: Lesson 3 (rclpy)

```bash
# Launch all content sections together:
Task T049: "Write Section 3.1: Introduction to rclpy"
Task T050: "Write Section 3.2: Creating Your First Node"
Task T051: "Write Section 3.3: Publisher Node"
Task T052: "Write Section 3.4: Subscriber Node"
Task T053: "Write Section 3.5: Service Server"
Task T054: "Write Section 3.6: Agent Pattern"

# Launch all code examples together:
Task T056: "Write minimal node (10 lines)"
Task T057: "Write publisher (20 lines)"
Task T058: "Write subscriber (15 lines)"
Task T059: "Write service server (20 lines)"
Task T060: "Write agent loop (25 lines)"

# Launch all lab creation tasks together:
Task T063-T066: "Create Lab 1 (hello-ros2)"
Task T067-T070: "Create Lab 2 (pubsub)"
Task T071-T074: "Create Lab 3 (services)"
```

---

## Implementation Strategy

### MVP First (Lessons 1-3 Only)

1. Complete Phase 1: Setup verification
2. Complete Phase 2: Module 1 structure
3. Complete Phase 3: Lesson 1 (Physical AI foundation)
4. Complete Phase 4: Lesson 2 (ROS 2 architecture)
5. Complete Phase 5: Lesson 3 (rclpy + Labs)
6. **STOP and VALIDATE**: Test Lessons 1-3 independently
7. Deploy/demo if ready - this is the core MVP!

### Incremental Delivery

1. Setup + Foundational → Foundation ready
2. Add Lesson 1 → Deploy/Demo (Physical AI concepts)
3. Add Lesson 2 → Deploy/Demo (ROS 2 theory)
4. Add Lesson 3 + Labs → Deploy/Demo (Hands-on rclpy)
5. Add Lesson 4 + Lab → Deploy/Demo (URDF)
6. Add Lesson 5 + Quiz → Deploy/Demo (Complete Module 1)
7. Each lesson adds value without breaking previous lessons

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together
2. Once Phase 2 is done:
   - Writer A: Lessons 1-2 (theory content)
   - Writer B: Lesson 3 (Python code + labs)
   - Writer C: Lesson 4-5 (URDF + simulation)
3. All converge for Phase 8 (Polish)

---

## Task Count Summary

| Phase | Task Count | Key Deliverables |
|-------|------------|------------------|
| Phase 1 (Setup) | 10 | Directory structure, validation scripts |
| Phase 2 (Foundational) | 5 | Templates, QuizComponent |
| Phase 3 (Lesson 1) | 15 | Physical AI content (~800 words), 3 diagrams, 3 citations |
| Phase 4 (Lesson 2) | 17 | ROS 2 architecture (~1100 words), 4 diagrams, 3 citations |
| Phase 5 (Lesson 3) | 33 | rclpy content (~1200 words), 5 code examples, 3 labs |
| Phase 6 (Lesson 4) | 21 | URDF content (~900 words), 2 code examples, 1 lab |
| Phase 7 (Lesson 5) | 19 | Simulation + review (~1100 words), 2 mini-projects, quiz |
| Phase 8 (Polish) | 16 | Validation, build, deploy |
| **Total** | **136** | Complete Module 1 chapter with labs and assessment |

---

## Success Metrics (Module 1)

| Metric | Target | Validation |
|--------|--------|------------|
| Word Count | 4500-5500 words | scripts/count_words.py |
| Code Examples | 100% run successfully | scripts/validate_code_examples.py |
| APA Citations | 9+ citations | Manual review |
| Labs | 4 labs + 2 mini-projects | Lab validate.py scripts |
| Diagrams | 10+ diagrams | Visual inspection |
| Quiz Questions | 10-15 questions | QuizComponent |
| Build | No errors | npm run build |

---

## Notes

- [P] tasks = different files, no dependencies, can run in parallel
- [Lesson] label (L1-L5) maps task to specific lesson for traceability
- All code examples target ROS 2 Humble
- All Python code must be 10-30 lines per example
- Word count targets per lesson: L1 (800), L2 (1100), L3 (1200), L4 (900), L5 (1100)
- Total Module 1: ~5100 words
- Verify validation scripts pass before marking lesson complete
- Commit after each logical task group
