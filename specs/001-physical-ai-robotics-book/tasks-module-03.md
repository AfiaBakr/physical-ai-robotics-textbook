# Tasks: Module 3 - Perception & Sensors (Computer Vision & Sensor Fusion)

**Input**: Design documents from `/specs/001-physical-ai-robotics-book/`
**Prerequisites**: Module 1 (ROS 2), Module 2 (Simulation), plan.md, spec.md, research.md, data-model.md, contracts/content-schema.yaml

**Tests**: Code validation and content quality tests are included as per constitution's TDD principle.

**Organization**: Tasks are grouped by lesson (3 lessons) to enable incremental implementation and testing.

**Scope**: Module 3 (Weeks 7-9) - Perception & Sensors (Computer Vision & Sensor Fusion)

## Format: `[ID] [P?] [US?] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[US3]**: Maps to User Story 3 from spec.md (perception algorithms)
- Include exact file paths in descriptions

## Module 3 Lesson Structure

| Lesson | Title | Content Focus |
|--------|-------|---------------|
| L1 | Computer Vision Fundamentals | Image processing, OpenCV, ROS 2 image transport, camera calibration |
| L2 | Multi-Sensor Integration | LiDAR, IMU, depth sensors, sensor fusion concepts, message types |
| L3 | Perception Pipelines | Object detection, tracking, sensor data processing, ROS 2 perception nodes |

## Path Conventions

Project root: `physical-ai-robotics-textbook/`
- Content: `docs/module-03-perception/` (3 lessons as MDX files)
- Labs: `labs/module-03/` (hands-on exercises)
- Assets: `static/diagrams/`, `static/img/`
- Scripts: `scripts/` (validation tools)
- Config: `docusaurus.config.ts`, `sidebars.ts`, `package.json`

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Verify Docusaurus project and establish Module 3 structure

- [X] T001 Verify Module 1 and Module 2 are complete and functional
- [X] T002 Verify OpenCV and sensor processing dependencies documented in package.json
- [X] T003 Create docs/module-03-perception/ directory for Module 3 content
- [X] T004 [P] Create labs/module-03/ directory for Module 3 labs
- [X] T005 [P] Create static/diagrams/module-03/ directory for Module 3 diagrams
- [X] T006 [P] Create scripts/validate_cv_examples.py for computer vision code validation
- [X] T007 Update sidebars.ts to include Module 3 navigation structure

**Checkpoint**: Module 3 directory structure ready

---

## Phase 2: Foundational (Module 3 Templates)

**Purpose**: Create templates and shared components for Module 3

- [X] T008 Create docs/module-03-perception/_category_.json with module metadata
- [X] T009 Create labs/module-03/_templates/cv-lab-template.md with standard sections
- [X] T010 [P] Create labs/module-03/_templates/validate-cv-template.py for CV lab validation
- [X] T011 [P] Create src/components/SensorVisualizer.tsx for sensor data visualization
- [X] T012 Verify Docusaurus build succeeds with Module 3 structure (`npm run build`)

**Checkpoint**: Foundation ready - lesson content creation can begin

---

## Phase 3: Lesson 1 - Computer Vision Fundamentals (L1) 🎯 MVP

**Goal**: Students understand image processing basics, OpenCV integration with ROS 2, and camera data handling

**Independent Test**: Student processes camera images with OpenCV, publishes results to ROS 2 topics, demonstrates image transport

**User Story**: [US3] Students configure and use simulated sensors (cameras, LiDAR, IMU, depth sensors) in Gazebo, understanding how sensor data is generated, published to ROS 2 topics, and consumed by perception nodes.

### Content for Lesson 1

- [X] T013 [P] [L1] Write docs/module-03-perception/lesson-01-computer-vision.mdx frontmatter and learning objectives
- [X] T014 [P] [L1] Write Section 1.1: Introduction to Computer Vision (200 words) in docs/module-03-perception/lesson-01-computer-vision.mdx
- [X] T015 [P] [L1] Write Section 1.2: OpenCV Basics with ROS 2 (250 words) in docs/module-03-perception/lesson-01-computer-vision.mdx
- [X] T016 [P] [L1] Write Section 1.3: ROS 2 Image Transport (200 words) in docs/module-03-perception/lesson-01-computer-vision.mdx
- [X] T017 [P] [L1] Write Section 1.4: Camera Calibration Concepts (150 words) in docs/module-03-perception/lesson-01-computer-vision.mdx
- [X] T018 [L1] Write Lesson 1 summary and preview of Lesson 2 in docs/module-03-perception/lesson-01-computer-vision.mdx

### Code Examples for Lesson 1

- [X] T019 [P] [L1] Write basic image subscriber (15 lines Python) in docs/module-03-perception/lesson-01-computer-vision.mdx
- [X] T020 [P] [L1] Write image processing pipeline (25 lines Python) in docs/module-03-perception/lesson-01-computer-vision.mdx
- [X] T021 [P] [L1] Write color filtering example (20 lines Python) in docs/module-03-perception/lesson-01-computer-vision.mdx
- [X] T022 [L1] Add all code examples to scripts/validate_cv_examples.py test suite

### Diagrams for Lesson 1

- [X] T023 [P] [L1] Create static/diagrams/module-03/cv-pipeline.svg showing image processing flow (Mermaid in MDX)
- [X] T024 [P] [L1] Create static/diagrams/module-03/ros-image-transport.svg showing sensor_msgs/Image flow (Mermaid in MDX)
- [X] T025 [P] [L1] Create Mermaid diagram: camera → image topic → processing → results in docs/module-03-perception/lesson-01-computer-vision.mdx
- [X] T026 [L1] Embed diagrams with alt text in docs/module-03-perception/lesson-01-computer-vision.mdx

### Citations for Lesson 1

- [X] T027 [P] [L1] Add OpenCV library citation to docs/appendix/references.mdx
- [X] T028 [P] [L1] Add computer vision textbook citation (2020+) to docs/appendix/references.mdx
- [X] T029 [P] [L1] Add ROS 2 image transport tutorials citation to docs/appendix/references.mdx

### Labs for Lesson 1

- [X] T030 [P] [L1] Create labs/module-03/lab-01-image-subscriber/README.md (60 min, basic image processing)
- [X] T031 [P] [L1] Create labs/module-03/lab-01-image-subscriber/starter/ with image subscriber template
- [X] T032 [P] [L1] Create labs/module-03/lab-01-image-subscriber/solution/ with complete image processing
- [X] T033 [P] [L1] Create labs/module-03/lab-01-image-subscriber/validate.py to verify image processing

### Validation for Lesson 1

- [X] T034 [L1] Run scripts/count_words.py to verify Lesson 1 is 750-900 words
- [X] T035 [L1] Build Docusaurus and verify Lesson 1 renders without errors
- [X] T036 [L1] Run scripts/validate_cv_examples.py to test all Python examples

**Checkpoint**: Lesson 1 complete - Computer Vision fundamentals established

---

## Phase 4: Lesson 2 - Multi-Sensor Integration (L2) 🎯 MVP

**Goal**: Students understand different sensor types (LiDAR, IMU, depth), their ROS 2 message types, and fusion concepts

**Independent Test**: Student subscribes to multiple sensor topics, visualizes data, explains message differences

**User Story**: [US3] Students configure and use simulated sensors (cameras, LiDAR, IMU, depth sensors) in Gazebo, understanding how sensor data is generated, published to ROS 2 topics, and consumed by perception nodes.

### Content for Lesson 2

- [X] T037 [P] [L2] Write docs/module-03-perception/lesson-02-multi-sensor.mdx frontmatter and learning objectives
- [X] T038 [P] [L2] Write Section 2.1: Sensor Types Overview (200 words) in docs/module-03-perception/lesson-02-multi-sensor.mdx
- [X] T039 [P] [L2] Write Section 2.2: LiDAR and Point Clouds (250 words) in docs/module-03-perception/lesson-02-multi-sensor.mdx
- [X] T040 [P] [L2] Write Section 2.3: IMU and Inertial Sensing (200 words) in docs/module-03-perception/lesson-02-multi-sensor.mdx
- [X] T041 [P] [L2] Write Section 2.4: Depth Sensors and 3D Perception (150 words) in docs/module-03-perception/lesson-02-multi-sensor.mdx
- [X] T042 [P] [L2] Write Section 2.5: Sensor Fusion Concepts (200 words) in docs/module-03-perception/lesson-02-multi-sensor.mdx
- [X] T043 [L2] Write Lesson 2 summary and preview of Lesson 3 in docs/module-03-perception/lesson-02-multi-sensor.mdx

### Code Examples for Lesson 2

- [X] T044 [P] [L2] Write LiDAR point cloud subscriber (20 lines Python) in docs/module-03-perception/lesson-02-multi-sensor.mdx
- [X] T045 [P] [L2] Write IMU data processing (15 lines Python) in docs/module-03-perception/lesson-02-multi-sensor.mdx
- [X] T046 [P] [L2] Write depth image processing (20 lines Python) in docs/module-03-perception/lesson-02-multi-sensor.mdx
- [X] T047 [P] [L2] Write sensor synchronization example (25 lines Python) in docs/module-03-perception/lesson-02-multi-sensor.mdx
- [X] T048 [L2] Add all code examples to scripts/validate_cv_examples.py test suite

### Diagrams for Lesson 2

- [X] T049 [P] [L2] Create static/diagrams/module-03/sensor-types-comparison.svg comparing camera, LiDAR, IMU, depth (Mermaid in MDX)
- [X] T050 [P] [L2] Create Mermaid diagram: multi-sensor data flow in docs/module-03-perception/lesson-02-multi-sensor.mdx
- [X] T051 [P] [L2] Create static/diagrams/module-03/point-cloud-visualization.svg showing 3D point clouds (Mermaid in MDX)

### Citations for Lesson 2

- [X] T052 [P] [L2] Add PCL (Point Cloud Library) citation to docs/appendix/references.mdx
- [X] T053 [P] [L2] Add sensor fusion research paper citation to docs/appendix/references.mdx
- [X] T054 [P] [L2] Add ROS 2 sensor message types documentation to docs/appendix/references.mdx

### Labs for Lesson 2

- [ ] T055 [P] [L2] Create labs/module-03/lab-02-lidar-processing/README.md (90 min, LiDAR point clouds)
- [ ] T056 [P] [L2] Create labs/module-03/lab-02-lidar-processing/starter/ with point cloud template
- [ ] T057 [P] [L2] Create labs/module-03/lab-02-lidar-processing/solution/ with complete processing
- [ ] T058 [P] [L2] Create labs/module-03/lab-02-lidar-processing/validate.py to verify point cloud processing
- [ ] T059 [P] [L2] Create labs/module-03/lab-03-sensor-fusion/README.md (120 min, multi-sensor integration)
- [ ] T060 [P] [L2] Create labs/module-03/lab-03-sensor-fusion/starter/ with multi-sensor template
- [ ] T061 [P] [L2] Create labs/module-03/lab-03-sensor-fusion/solution/ with fusion algorithm
- [ ] T062 [P] [L2] Create labs/module-03/lab-03-sensor-fusion/validate.py to verify sensor fusion

### Validation for Lesson 2

- [ ] T063 [L2] Run scripts/count_words.py to verify Lesson 2 is 950-1100 words
- [ ] T064 [L2] Build Docusaurus and verify Lesson 2 renders without errors
- [ ] T065 [L2] Run scripts/validate_cv_examples.py to test all Python examples
- [ ] T066 [L2] Run labs/module-03/lab-02-lidar-processing/validate.py
- [ ] T067 [L2] Run labs/module-03/lab-03-sensor-fusion/validate.py

**Checkpoint**: Lesson 2 complete - Multi-sensor integration understood

---

## Phase 5: Lesson 3 - Perception Pipelines (L3) 🎯 MVP

**Goal**: Students build complete perception pipelines with object detection, tracking, and integration with ROS 2

**Independent Test**: Student implements object detection pipeline, tracks objects over time, integrates with ROS 2 control nodes

**User Story**: [US4] Students integrate NVIDIA Isaac Sim for advanced perception models, leveraging GPU-accelerated simulation, synthetic data generation, and pre-trained vision models to enable robust robot perception in complex environments.

### Content for Lesson 3

- [ ] T068 [P] [L3] Write docs/module-03-perception/lesson-03-perception-pipelines.mdx frontmatter and learning objectives
- [ ] T069 [P] [L3] Write Section 3.1: Object Detection Basics (200 words) in docs/module-03-perception/lesson-03-perception-pipelines.mdx
- [ ] T070 [P] [L3] Write Section 3.2: YOLO and CNN Integration (250 words) in docs/module-03-perception/lesson-03-perception-pipelines.mdx
- [ ] T071 [P] [L3] Write Section 3.3: Object Tracking Over Time (200 words) in docs/module-03-perception/lesson-03-perception-pipelines.mdx
- [ ] T072 [P] [L3] Write Section 3.4: Perception to Action Pipeline (200 words) in docs/module-03-perception/lesson-03-perception-pipelines.mdx
- [ ] T073 [P] [L3] Write Section 3.5: Performance and Accuracy Metrics (150 words) in docs/module-03-perception/lesson-03-perception-pipelines.mdx
- [ ] T074 [L3] Write Lesson 3 summary and preview of Module 4 in docs/module-03-perception/lesson-03-perception-pipelines.mdx

### Code Examples for Lesson 3

- [ ] T075 [P] [L3] Write object detection node (30 lines Python) in docs/module-03-perception/lesson-03-perception-pipelines.mdx
- [ ] T076 [P] [L3] Write tracking algorithm (25 lines Python) in docs/module-03-perception/lesson-03-perception-pipelines.mdx
- [ ] T077 [P] [L3] Write perception-to-control interface (20 lines Python) in docs/module-03-perception/lesson-03-perception-pipelines.mdx
- [ ] T078 [P] [L3] Write performance metrics calculator (15 lines Python) in docs/module-03-perception/lesson-03-perception-pipelines.mdx
- [ ] T079 [L3] Add all code examples to scripts/validate_cv_examples.py test suite

### Diagrams for Lesson 3

- [ ] T080 [P] [L3] Create Mermaid diagram: perception pipeline flow in docs/module-03-perception/lesson-03-perception-pipelines.mdx
- [ ] T081 [P] [L3] Create static/diagrams/module-03/object-detection-workflow.svg showing detection process
- [ ] T082 [P] [L3] Create static/diagrams/module-03/perception-to-action.svg showing full pipeline

### Citations for Lesson 3

- [ ] T083 [P] [L3] Add YOLO paper citation (v5 or newer) to docs/appendix/references.mdx
- [ ] T084 [P] [L3] Add object tracking research citation to docs/appendix/references.mdx
- [ ] T085 [P] [L3] Add perception metrics evaluation paper to docs/appendix/references.mdx

### Labs for Lesson 3

- [ ] T086 [P] [L3] Create labs/module-03/lab-04-object-detection/README.md (120 min, detection pipeline)
- [ ] T087 [P] [L3] Create labs/module-03/lab-04-object-detection/starter/ with basic detection template
- [ ] T088 [P] [L3] Create labs/module-03/lab-04-object-detection/solution/ with complete detector
- [ ] T089 [P] [L3] Create labs/module-03/lab-04-object-detection/validate.py to verify detection accuracy
- [ ] T090 [P] [L3] Create labs/module-03/lab-05-perception-integration/README.md (150 min, full pipeline)
- [ ] T091 [P] [L3] Create labs/module-03/lab-05-perception-integration/starter/ with pipeline template
- [ ] T092 [P] [L3] Create labs/module-03/lab-05-perception-integration/solution/ with complete pipeline
- [ ] T093 [P] [L3] Create labs/module-03/lab-05-perception-integration/validate.py to verify full pipeline

### Review Quiz for Lesson 3

- [ ] T094 [P] [L3] Create review quiz (12-15 questions) covering all 3 lessons using QuizComponent in docs/module-03-perception/lesson-03-perception-pipelines.mdx
- [ ] T095 [L3] Include questions on: Computer vision, sensor types, perception pipelines, fusion

### Validation for Lesson 3

- [ ] T096 [L3] Run scripts/count_words.py to verify Lesson 3 is 1050-1200 words
- [ ] T097 [L3] Build Docusaurus and verify Lesson 3 renders without errors
- [ ] T098 [L3] Run scripts/validate_cv_examples.py to test all Python examples
- [ ] T099 [L3] Run labs/module-03/lab-04-object-detection/validate.py
- [ ] T100 [L3] Run labs/module-03/lab-05-perception-integration/validate.py

**Checkpoint**: Lesson 3 complete - Complete perception pipelines mastered

---

## Phase 6: Polish & Module 3 Finalization

**Purpose**: Final quality checks, validation, and Module 3 completion

### Content Finalization

- [ ] T101 [P] Create docs/module-03-perception/index.mdx with Module 3 overview and lesson navigation
- [ ] T102 [P] Update docs/intro.mdx to include Module 3 in course overview
- [ ] T103 [P] Update labs/intro.mdx to include Module 3 labs

### Validation Scripts

- [ ] T104 Run scripts/validate_cv_examples.py on ALL Module 3 code examples
- [ ] T105 Run scripts/count_words.py to verify Module 3 total is 2750-3200 words
- [ ] T106 Run all lab validation scripts (lab-01 through lab-05)

### Build & Deploy

- [ ] T107 Run `npm run build` to verify Docusaurus builds without errors
- [ ] T108 Test Module 3 navigation in local development server
- [ ] T109 Verify all Mermaid diagrams render correctly
- [ ] T110 Verify all code examples have syntax highlighting
- [ ] T111 Test responsive design on mobile devices

### Documentation

- [ ] T112 [P] Add Module 3 learning outcomes summary to docs/appendix/references.mdx
- [ ] T113 [P] Update sidebars.ts with final Module 3 navigation structure
- [ ] T114 Verify at least 9 APA citations for Module 3 in docs/appendix/references.mdx

### Final Review

- [ ] T115 Verify all success criteria met (students can process sensor data, build perception pipelines)
- [ ] T116 Deploy to GitHub Pages using `npm run deploy` (if ready)

**Checkpoint**: Module 3 complete, validated, and ready for students

---

## Dependencies & Execution Order

### Phase Dependencies

- **Phase 1 (Setup)**: Depends on Module 1 & 2 completion
- **Phase 2 (Foundational)**: Depends on Setup - create Module 3 structure
- **Phases 3-5 (Lessons 1-3)**: All depend on Foundational phase
  - Lessons can proceed sequentially or in parallel
  - Recommended: L1 → L2 → L3 (conceptual flow)
- **Phase 6 (Polish)**: Depends on all lessons complete

### Within Each Lesson

- Content sections can be written in parallel [P]
- Code examples can be written in parallel [P]
- Diagrams can be created in parallel [P]
- Labs can be created in parallel [P]
- Validation runs after content complete

### Parallel Opportunities

- All Setup tasks marked [P] (T003-T006)
- All content sections within a lesson marked [P]
- All code examples within a lesson marked [P]
- All diagrams within a lesson marked [P]
- All lab creation tasks marked [P]
- Polish tasks marked [P] (T101-T103, T112-T113)

---

## Parallel Example: Lesson 2 (Multi-Sensor)

```bash
# Launch all content sections together:
Task T038: "Write Section 2.1: Sensor Types Overview"
Task T039: "Write Section 2.2: LiDAR and Point Clouds"
Task T040: "Write Section 2.3: IMU and Inertial Sensing"
Task T041: "Write Section 2.4: Depth Sensors"
Task T042: "Write Section 2.5: Sensor Fusion Concepts"

# Launch all code examples together:
Task T044: "Write LiDAR subscriber (20 lines)"
Task T045: "Write IMU processing (15 lines)"
Task T046: "Write depth processing (20 lines)"
Task T047: "Write sync example (25 lines)"

# Launch all lab creation tasks together:
Task T055-T058: "Create Lab 2 (LiDAR processing)"
Task T059-T062: "Create Lab 3 (Sensor fusion)"
```

---

## Implementation Strategy

### MVP First (Lessons 1-2 Only)

1. Complete Phase 1: Setup verification
2. Complete Phase 2: Module 3 structure
3. Complete Phase 3: Lesson 1 (Computer Vision basics)
4. Complete Phase 4: Lesson 2 (Multi-sensor integration)
5. **STOP and VALIDATE**: Test Lessons 1-2 independently
6. Deploy/demo if ready - this is the core MVP!

### Incremental Delivery

1. Setup + Foundational → Foundation ready
2. Add Lesson 1 → Deploy/Demo (Computer vision)
3. Add Lesson 2 → Deploy/Demo (Multi-sensor)
4. Add Lesson 3 → Deploy/Demo (Complete perception pipelines)
5. Each lesson adds value without breaking previous lessons

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together
2. Once Phase 2 is done:
   - Writer A: Lessons 1 (Computer vision content)
   - Writer B: Lesson 2 (Sensor integration content)
   - Writer C: Lesson 3 + Labs (Perception pipelines)
3. All converge for Phase 6 (Polish)

---

## Task Count Summary

| Phase | Task Count | Key Deliverables |
|-------|------------|------------------|
| Phase 1 (Setup) | 7 | Directory structure, validation scripts |
| Phase 2 (Foundational) | 5 | Templates, SensorVisualizer |
| Phase 3 (Lesson 1) | 23 | CV content (~800 words), 4 code examples, 3 diagrams, 1 lab |
| Phase 4 (Lesson 2) | 32 | Multi-sensor content (~1000 words), 4 code examples, 3 diagrams, 2 labs |
| Phase 5 (Lesson 3) | 33 | Perception pipelines (~1100 words), 4 code examples, 3 diagrams, 2 labs, quiz |
| Phase 6 (Polish) | 16 | Validation, build, deploy |
| **Total** | **116** | Complete Module 3 chapter with labs and assessment |

---

## Success Metrics (Module 3)

| Metric | Target | Validation |
|--------|--------|------------|
| Word Count | 2750-3200 words | scripts/count_words.py |
| Code Examples | 100% run successfully | scripts/validate_cv_examples.py |
| APA Citations | 9+ citations | Manual review |
| Labs | 5 labs total | Lab validate.py scripts |
| Diagrams | 9+ diagrams | Visual inspection |
| Quiz Questions | 12-15 questions | QuizComponent |
| Build | No errors | npm run build |

---

## Notes

- [P] tasks = different files, no dependencies, can run in parallel
- [US3] label maps task to User Story 3 from spec.md (perception algorithms)
- All code examples target ROS 2 Humble with OpenCV
- All Python code must be 10-30 lines per example
- Word count targets per lesson: L1 (800), L2 (1000), L3 (1100)
- Total Module 3: ~2900 words
- Verify validation scripts pass before marking lesson complete
- Commit after each logical task group