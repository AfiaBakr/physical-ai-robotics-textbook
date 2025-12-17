# Tasks: Physical AI & Humanoid Robotics Textbook - Module 2

**Input**: Design documents from `/specs/001-physical-ai-robotics-book/`
**Prerequisites**: plan.md (required), spec.md (required), modules/module-02-digital-twin-spec.md, research.md, data-model.md, contracts/module-02-schema.yaml
**Feature**: Module 2 - The Digital Twin (Gazebo & Unity)

**Tests**: This module focuses on educational content. Validation is via lab validation scripts that verify student deliverables.

**Organization**: Tasks are grouped by user story from module-02-digital-twin-spec.md to enable independent implementation and testing.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (US1-US5 from Module 2 spec)
- Include exact file paths in descriptions

## Path Conventions

Based on plan.md structure:
- **Lessons**: `physical-ai-robotics-textbook/docs/module-02-simulation/`
- **Labs**: `physical-ai-robotics-textbook/labs/module-02/`
- **Static assets**: `physical-ai-robotics-textbook/static/diagrams/`
- **Components**: `physical-ai-robotics-textbook/src/components/`

---

## Phase 1: Setup (Module Structure)

**Purpose**: Create Module 2 directory structure and configuration files

- [X] T001 Create module directory structure at physical-ai-robotics-textbook/docs/module-02-simulation/
- [X] T002 Create `_category_.json` in physical-ai-robotics-textbook/docs/module-02-simulation/
- [X] T003 [P] Create labs directory structure at physical-ai-robotics-textbook/labs/module-02/
- [X] T004 [P] Create `_category_.json` in physical-ai-robotics-textbook/labs/module-02/
- [X] T005 [P] Create diagrams directory at physical-ai-robotics-textbook/static/diagrams/module-02/
- [X] T006 Update sidebars.ts to include Module 2 navigation in physical-ai-robotics-textbook/sidebars.ts
- [X] T007 Update sidebarsLabs.ts to include Module 2 labs in physical-ai-robotics-textbook/sidebarsLabs.ts

---

## Phase 2: Foundational (Shared Content Elements)

**Purpose**: Create reusable assets and infrastructure required by multiple lessons

**CRITICAL**: Complete before starting user story phases

- [X] T008 Create Simulation Pipeline Mermaid diagram (m2-diag-1) in physical-ai-robotics-textbook/docs/module-02-simulation/lesson-01-digital-twin.mdx
- [X] T009 [P] Create Sensor Raycasting Flow Mermaid diagram (m2-diag-2) for physical-ai-robotics-textbook/docs/module-02-simulation/lesson-03-sensors-unity.mdx
- [X] T010 [P] Create Gazebo vs Unity Comparison diagram (m2-diag-3) for physical-ai-robotics-textbook/docs/module-02-simulation/lesson-03-sensors-unity.mdx
- [X] T011 Add 5 APA citations to physical-ai-robotics-textbook/docs/appendix/references.mdx per module-02-schema.yaml

**Checkpoint**: Foundation ready - user story implementation can now begin

---

## Phase 3: User Story 1 - Understanding Digital Twins (Priority: P1) MVP

**Goal**: Students learn the digital twin paradigm and understand why simulation matters before learning specific tools

**Independent Test**: Student can explain digital twin concept, articulate 3 benefits of simulation-first development, and describe URDF-to-physical-robot relationship

### Lesson Content for US1

- [X] T012 [US1] Create lesson-01-digital-twin.mdx frontmatter and learning objectives in physical-ai-robotics-textbook/docs/module-02-simulation/lesson-01-digital-twin.mdx
- [X] T013 [US1] Write Section m2-l1-s1 "What is a Digital Twin?" (conceptual) with 2 real-world examples (Boston Dynamics, NASA) in physical-ai-robotics-textbook/docs/module-02-simulation/lesson-01-digital-twin.mdx
- [X] T014 [US1] Write benefits of simulation-first development (safety, cost, speed, repeatability) in lesson-01-digital-twin.mdx
- [X] T015 [US1] Connect URDF/SDF knowledge from Module 1 to digital twin concept in lesson-01-digital-twin.mdx
- [X] T016 [US1] Embed Simulation Pipeline Mermaid diagram (m2-diag-1) in lesson-01-digital-twin.mdx

### Lab for US1

- [X] T017 [P] [US1] Create lab-01-physics-experiments/ directory structure with starter/ and solution/ subdirectories
- [X] T018 [US1] Write lab-01-physics-experiments/README.md with objective, prerequisites, 5-7 steps, and deliverable
- [X] T019 [US1] Create starter/physics_observer.py template with TODOs in labs/module-02/lab-01-physics-experiments/starter/
- [X] T020 [US1] Create solution/physics_observer.py with complete implementation in labs/module-02/lab-01-physics-experiments/solution/
- [X] T021 [US1] Create validate.py script to check physics parameter modifications in labs/module-02/lab-01-physics-experiments/

**Checkpoint**: User Story 1 complete - students can explain digital twins and observe physics parameters

---

## Phase 4: User Story 2 - Physics Simulation Fundamentals (Priority: P1)

**Goal**: Students understand core physics simulation concepts (rigid body dynamics, collision detection, friction models, time stepping)

**Independent Test**: Student can explain how physics engines calculate motion, identify collision detection methods, and predict friction coefficient effects

### Lesson Content for US2

- [X] T022 [US2] Write Section m2-l1-s2 "Physics Simulation Fundamentals" in lesson-01-digital-twin.mdx
- [X] T023 [US2] Explain rigid body dynamics (mass, inertia tensor, center of mass) conceptually in lesson-01-digital-twin.mdx
- [X] T024 [US2] Explain collision detection (bounding boxes, mesh collision, contact points) in lesson-01-digital-twin.mdx
- [X] T025 [US2] Explain friction models (Coulomb friction, slip/no-slip states) in lesson-01-digital-twin.mdx
- [X] T026 [US2] Explain time stepping (fixed vs variable step, real-time factor) in lesson-01-digital-twin.mdx
- [X] T027 [US2] Add physics engine comparison overview (ODE, Bullet, DART) in lesson-01-digital-twin.mdx

### Lab Enhancements for US2

- [X] T028 [US2] Add physics experiments (gravity, friction, collision) to lab-01-physics-experiments/README.md
- [X] T029 [US2] Create physics parameter modification examples in starter/physics_observer.py
- [X] T030 [US2] Add reflection questions about physics behavior to lab-01-physics-experiments/README.md

**Checkpoint**: User Story 2 complete - students understand physics simulation fundamentals

---

## Phase 5: User Story 3 - Gazebo Simulation Mastery (Priority: P1)

**Goal**: Students set up Gazebo, load URDF/SDF models, create worlds, and interface with ROS 2

**Independent Test**: Student can launch Gazebo with custom world, spawn robot from URDF, send velocity commands via ROS 2, and visualize sensor data

### Lesson Content for US3

- [X] T031 [US3] Create lesson-02-gazebo-workflows.mdx frontmatter and learning objectives in physical-ai-robotics-textbook/docs/module-02-simulation/lesson-02-gazebo-workflows.mdx
- [X] T032 [US3] Write Section m2-l2-s1 "Gazebo Architecture" with architecture diagram in lesson-02-gazebo-workflows.mdx
- [X] T033 [US3] Write Section m2-l2-s2 "World Files and SDF" with SDF code examples in lesson-02-gazebo-workflows.mdx
- [X] T034 [US3] Explain URDF-to-SDF conversion and when to use each format in lesson-02-gazebo-workflows.mdx
- [X] T035 [US3] Write Section m2-l2-s3 "ROS 2 Integration with ros_gz" hands-on tutorial in lesson-02-gazebo-workflows.mdx
- [X] T036 [US3] Add robot spawning and cmd_vel control examples in lesson-02-gazebo-workflows.mdx

### Lab for US3

- [X] T037 [P] [US3] Create lab-02-gazebo-worlds/ directory structure with starter/worlds/ and solution/worlds/ subdirectories
- [X] T038 [US3] Write lab-02-gazebo-worlds/README.md with objective, prerequisites, 6-8 steps, and deliverable
- [X] T039 [US3] Create starter/worlds/empty_world.sdf template with TODOs in labs/module-02/lab-02-gazebo-worlds/starter/worlds/
- [X] T040 [US3] Create solution/worlds/custom_world.sdf with terrain, 3+ obstacles, lighting in labs/module-02/lab-02-gazebo-worlds/solution/worlds/
- [X] T041 [US3] Create validate.py script to check SDF structure and physics parameters in labs/module-02/lab-02-gazebo-worlds/

**Checkpoint**: User Story 3 complete - students can create and control robots in Gazebo with ROS 2

---

## Phase 6: User Story 4 - Unity for High-Fidelity Visualization (Priority: P2)

**Goal**: Students understand Unity's role, particularly for photorealistic rendering and human-robot interaction scenarios

**Independent Test**: Student can explain Gazebo vs Unity trade-offs, describe Unity's rendering pipeline advantages, and identify Unity-ROS 2 integration patterns

### Lesson Content for US4

- [X] T042 [US4] Create lesson-03-sensors-unity.mdx frontmatter and learning objectives in physical-ai-robotics-textbook/docs/module-02-simulation/lesson-03-sensors-unity.mdx
- [X] T043 [US4] Write Section m2-l3-s1 "Unity for Robotics Overview" (conceptual, no hands-on) in lesson-03-sensors-unity.mdx
- [X] T044 [US4] Write Section m2-l3-s2 "Gazebo vs Unity Comparison" with comparison table in lesson-03-sensors-unity.mdx
- [X] T045 [US4] Embed Gazebo vs Unity Comparison diagram (m2-diag-3) in lesson-03-sensors-unity.mdx
- [X] T046 [US4] Explain ROS-Unity-Bridge architecture with data flow diagram in lesson-03-sensors-unity.mdx
- [X] T047 [US4] Add decision framework: when to use Gazebo vs Unity vs hybrid in lesson-03-sensors-unity.mdx

**Checkpoint**: User Story 4 complete - students can recommend appropriate simulator for given scenarios

---

## Phase 7: User Story 5 - Simulated Sensors and Data Pipelines (Priority: P1)

**Goal**: Students configure and use simulated sensors (camera, LiDAR, IMU, depth camera) in Gazebo with ROS 2 integration

**Independent Test**: Student can configure multiple sensors in Gazebo, visualize in RViz2, and write ROS 2 node that processes sensor messages

### Lesson Content for US5

- [X] T048 [US5] Write Section m2-l3-s3 "Simulated Sensors Configuration" hands-on tutorial in lesson-03-sensors-unity.mdx
- [X] T049 [US5] Document camera sensor configuration (Gazebo plugin, ROS 2 topic, Image message) in lesson-03-sensors-unity.mdx
- [X] T050 [US5] Document depth camera sensor configuration (Gazebo plugin, PointCloud2 message) in lesson-03-sensors-unity.mdx
- [X] T051 [US5] Document LiDAR sensor configuration (Gazebo plugin, LaserScan message) in lesson-03-sensors-unity.mdx
- [X] T052 [US5] Document IMU sensor configuration (Gazebo plugin, Imu message) in lesson-03-sensors-unity.mdx
- [X] T053 [US5] Write Section m2-l3-s4 "Sensor Data Pipelines" with RViz2 visualization guide in lesson-03-sensors-unity.mdx
- [X] T054 [US5] Embed Sensor Raycasting Flow diagram (m2-diag-2) in lesson-03-sensors-unity.mdx

### Lab for US5

- [X] T055 [P] [US5] Create lab-03-sensor-visualization/ directory structure with starter/ and solution/ subdirectories
- [X] T056 [US5] Write lab-03-sensor-visualization/README.md with objective, prerequisites, 7-9 steps, and deliverable
- [X] T057 [US5] Create starter/sensor_config.yaml template with TODOs in labs/module-02/lab-03-sensor-visualization/starter/
- [X] T058 [US5] Create starter/sensor_analyzer.py ROS 2 node template in labs/module-02/lab-03-sensor-visualization/starter/
- [X] T059 [US5] Create solution/sensor_config.yaml with 3 sensor configurations in labs/module-02/lab-03-sensor-visualization/solution/
- [X] T060 [US5] Create solution/sensor_analyzer.py with complete sensor processing in labs/module-02/lab-03-sensor-visualization/solution/
- [X] T061 [US5] Create validate.py script to check sensor topics and message types in labs/module-02/lab-03-sensor-visualization/

**Checkpoint**: User Story 5 complete - students can configure sensors and consume data in ROS 2

---

## Phase 8: Assessment & Closure

**Purpose**: Module quiz and final validation

### Quiz Creation

- [X] T062 Create 10-question quiz covering all 5 learning outcomes (LO-01 to LO-05)
- [X] T063 [P] Add 2 questions for LO-01 (digital twin concept) - multiple choice
- [X] T064 [P] Add 2 questions for LO-02 (physics fundamentals) - multiple choice
- [X] T065 [P] Add 2 questions for LO-03 (Gazebo usage) - true/false and multiple choice
- [X] T066 [P] Add 2 questions for LO-04 (Unity role) - multiple choice
- [X] T067 [P] Add 2 questions for LO-05 (simulated sensors) - multiple choice
- [X] T068 Integrate quiz into lesson-03-sensors-unity.mdx using QuizComponent in physical-ai-robotics-textbook/docs/module-02-simulation/lesson-03-sensors-unity.mdx

---

## Phase 9: Polish & Cross-Cutting Concerns

**Purpose**: Final validation and documentation updates

- [X] T069 [P] Verify all Mermaid diagrams render correctly in Docusaurus
- [X] T070 [P] Verify all internal links between lessons work
- [X] T071 [P] Verify all code examples are syntactically correct
- [X] T072 Run `npm run build` to verify Docusaurus build succeeds
- [X] T073 Test lab-01 validation script with starter and solution code
- [X] T074 Test lab-02 validation script with starter and solution SDF
- [X] T075 Test lab-03 validation script with starter and solution configs
- [X] T076 Update physical-ai-robotics-textbook/docs/appendix/references.mdx with 5 new Module 2 citations
- [X] T077 Review word count (target: 2000-2500 words for Module 2)
- [X] T078 Final review against module-02-digital-twin-spec.md requirements

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Phase 1 (T001-T007)
- **User Stories (Phase 3-7)**: Depend on Phase 2 (T008-T011)
  - US1 (Phase 3) and US2 (Phase 4) share lesson-01 - execute sequentially
  - US3 (Phase 5) can start after Phase 2 - independent lesson
  - US4 and US5 (Phase 6-7) share lesson-03 - execute sequentially
- **Assessment (Phase 8)**: Depends on all lessons complete (T012-T061)
- **Polish (Phase 9)**: Depends on all content complete

### User Story Dependencies

- **US1 (Understanding Digital Twins)**: Phase 2 complete → can start
- **US2 (Physics Fundamentals)**: US1 lesson complete (T012-T016) → can add to same lesson
- **US3 (Gazebo Mastery)**: Phase 2 complete → can start in parallel with US1/US2 (different lesson file)
- **US4 (Unity Visualization)**: Phase 2 complete → can start after US3 or in parallel (different section of lesson-03)
- **US5 (Sensors)**: Phase 2 complete → can start after US4 or in parallel (different section of lesson-03)

### Parallel Opportunities

**Setup Phase (T001-T007)**:
```
Parallel: T003, T004, T005 (different directories)
Sequential: T006, T007 (depends on directories)
```

**Foundational Phase (T008-T011)**:
```
Parallel: T009, T010, T011 (different files)
Sequential: T008 (must exist before embedding)
```

**Lab Creation (same structure applies to each lab)**:
```
Parallel: Directory creation (T017, T037, T055)
Sequential: README → starter → solution → validate
```

**Quiz Questions (T063-T067)**:
```
Parallel: All 5 question pairs (different learning outcomes)
```

---

## Implementation Strategy

### MVP First (User Stories 1, 2, 3, 5 - All P1 priorities)

1. Complete Phase 1: Setup (T001-T007)
2. Complete Phase 2: Foundational (T008-T011)
3. Complete Phase 3: US1 - Digital Twin Concept (T012-T021)
4. Complete Phase 4: US2 - Physics Fundamentals (T022-T030)
5. Complete Phase 5: US3 - Gazebo Mastery (T031-T041)
6. Complete Phase 7: US5 - Sensors (T048-T061)
7. **STOP and VALIDATE**: Run all validation scripts, build Docusaurus
8. Optional: Add US4 (Unity) for completeness

### Incremental Delivery

1. Setup + Foundational → Structure ready
2. Add US1 + US2 → Lesson 1 complete → Can teach digital twin concepts
3. Add US3 → Lesson 2 complete → Can teach Gazebo workflows
4. Add US4 + US5 → Lesson 3 complete → Module 2 complete
5. Add Quiz → Assessment ready → Full module deployable

---

## Summary

| Phase | Tasks | User Story | Key Deliverable |
|-------|-------|------------|-----------------|
| 1 | T001-T007 | - | Directory structure |
| 2 | T008-T011 | - | Diagrams + Citations |
| 3 | T012-T021 | US1 (P1) | Lesson 1 + Lab 1 |
| 4 | T022-T030 | US2 (P1) | Lesson 1 physics content |
| 5 | T031-T041 | US3 (P1) | Lesson 2 + Lab 2 |
| 6 | T042-T047 | US4 (P2) | Lesson 3 Unity section |
| 7 | T048-T061 | US5 (P1) | Lesson 3 sensors + Lab 3 |
| 8 | T062-T068 | - | 10-question quiz |
| 9 | T069-T078 | - | Validation + Polish |

**Total Tasks**: 78
**P1 Tasks**: 51 (US1, US2, US3, US5)
**P2 Tasks**: 6 (US4)
**Setup/Polish**: 21

**Parallel Opportunities**: 28 tasks marked [P]
**MVP Scope**: Phases 1-5, 7 (excludes Unity comparison for minimal viable module)

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each lesson can be taught independently once complete
- Validation scripts use `rclpy` - require ROS 2 Humble environment
- All SDF examples target Gazebo Fortress (version 1.8)
- Quiz uses existing QuizComponent from Module 1
