# Research & Design Decisions: Physical AI & Humanoid Robotics Textbook

**Feature**: 001-physical-ai-robotics-book
**Date**: 2025-12-15
**Purpose**: Document research findings and design decisions for Module 1 (ROS 2) and overall textbook architecture

## Phase 0: Research Findings

### 1. Content Format & Tooling

**Decision**: Use Docusaurus v3 with MDX for textbook content

**Rationale**:
- Docusaurus is the industry-standard static site generator for technical documentation
- MDX support enables embedding React components for interactive diagrams and code playgrounds
- Built-in versioning, search, and i18n capabilities
- GitHub Pages deployment is native and well-documented
- Active community and maintained by Meta

**Alternatives Considered**:
- **MkDocs Material**: Python-based, simpler but less extensible for interactive content
- **GitBook**: Commercial SaaS with vendor lock-in concerns
- **Jupyter Book**: Excellent for code-heavy content but overkill for primarily text-based chapters

**Technical Requirements**:
- Node.js 18+
- Docusaurus 3.x
- MDX plugins for Mermaid diagrams
- Syntax highlighting for Python, C++, XML (URDF)

---

### 2. ROS 2 Distribution Selection

**Decision**: Target ROS 2 Humble Hawksbill (LTS release)

**Rationale**:
- Humble is the current Long-Term Support release (until May 2027)
- Widest compatibility with Ubuntu 22.04 LTS (most common student environment)
- Stable package ecosystem with mature documentation
- Gazebo Classic and Gazebo Garden support
- Isaac Sim 2023.1+ supports Humble

**Alternatives Considered**:
- **ROS 2 Iron/Jazzy**: Newer but shorter support window, potential instability
- **ROS 2 Foxy**: Older LTS but approaching EOL (May 2023), outdated examples

**Version Specification**: All code examples will explicitly state ROS 2 Humble compatibility

---

### 3. Programming Language for Examples

**Decision**: Python 3.10+ using rclpy (primary), with C++ examples for performance-critical sections

**Rationale**:
- Python is the assumed prerequisite language for AI/ML students
- rclpy provides full ROS 2 functionality with cleaner syntax than C++
- Faster iteration for learning and prototyping
- C++ examples in Weeks 9-10 for real-time control introduces production-grade patterns

**Alternatives Considered**:
- **C++ only**: Steeper learning curve, slower initial progress
- **Python only**: Misses opportunity to demonstrate performance trade-offs

**Teaching Approach**: Introduce Python → demonstrate same concept in C++ → discuss when to use each

---

### 4. Simulation Environment Choice

**Decision**: Primary = Gazebo Classic 11, Secondary = NVIDIA Isaac Sim

**Rationale**:
- Gazebo Classic has lowest barrier to entry (included with ROS 2 Desktop)
- Extensive URDF support and community resources
- Isaac Sim introduced in advanced chapters (Weeks 7-8) after fundamentals are solid
- Unity considered out of scope to limit tooling complexity

**Alternatives Considered**:
- **Gazebo Garden/Fortress**: Newer but breaking API changes, less stable
- **Unity + ROS-Unity Bridge**: Requires C# knowledge, additional cognitive load
- **PyBullet**: Lightweight but lacks ROS 2 integration maturity

**Tradeoffs**:
- Gazebo Classic is deprecated in favor of Gazebo Garden, but Classic is more stable for education
- Will include migration guide as appendix for students wanting to upgrade

---

### 5. URDF Coverage Depth

**Decision**: Balanced approach - Start with simple 2-DOF arm, progress to 12-DOF humanoid torso+arms

**Rationale**:
- Full humanoid (20+ DOF) overwhelms beginners
- 2-DOF arm (Week 3-4) teaches joints, links, actuators without complexity
- 12-DOF upper body (Week 5-6) sufficient for manipulation tasks in capstone
- Students can extend to full biped in capstone if interested

**Alternatives Considered**:
- **Basic joints only**: Too abstract, students don't see humanoid relevance
- **Full 20+ DOF humanoid**: Too complex for foundational learning, long compile times

**Educational Progression**:
1. Week 3: Single revolute joint (concept)
2. Week 4: 2-DOF planar arm (kinematics)
3. Week 5-6: 12-DOF torso + arms (realistic manipulation)

---

### 6. Code Example Length

**Decision**: Minimal runnable examples (10-30 lines) with full projects in GitHub repo

**Rationale**:
- Textbook examples must fit on screen without scrolling for readability
- Minimal examples isolate concepts being taught
- Full-featured code in companion GitHub repo for students to clone and extend

**Structure**:
- **In-text**: Code snippets with key concepts highlighted
- **GitHub repo**: `physical-ai-robotics-labs/` with complete, tested projects
- **Each chapter**: Link to corresponding lab directory

**Alternatives Considered**:
- **Extended examples in textbook**: Clutters narrative, hard to print
- **Abbreviated pseudocode**: Students can't run it, reduces learning efficacy

---

### 7. Diagram and Visualization Strategy

**Decision**: Mermaid for architecture diagrams, custom SVG for robot schematics, RViz screenshots for runtime visualization

**Rationale**:
- Mermaid integrates natively with Docusaurus MDX
- Version-controllable (text-based) and easy to update
- SVG for anatomical diagrams ensures high-quality printing
- RViz screenshots show students what to expect in their own environment

**Diagram Types**:
- **ROS 2 graphs**: Mermaid flowcharts/graphs
- **Message flows**: Mermaid sequence diagrams
- **URDF hierarchy**: Mermaid tree diagrams
- **Humanoid anatomy**: Custom SVG (sourced or created with Inkscape)
- **Simulation screenshots**: PNG from Gazebo/Isaac Sim

---

### 8. Citation Strategy

**Decision**: 15+ APA citations distributed across theoretical foundations, ROS 2 docs, simulation papers, VLA research

**Citation Distribution**:
- Physical AI foundations: 3-4 papers (Brooks, Pfeifer, etc.)
- ROS 2 documentation: 2-3 official docs + key tutorials
- Humanoid robotics: 3-4 papers (ATLAS, NAO, Boston Dynamics)
- Simulation: 2-3 (Gazebo, Isaac Sim whitepapers)
- VLA: 3-4 recent papers (2022-2024, RT-1, RT-2, PaLM-E)

**Sources**:
- Peer-reviewed: IEEE Xplore, arXiv robotics, ICRA/IROS proceedings
- Technical documentation: ROS 2 docs, Gazebo tutorials, NVIDIA developer docs
- Industry reports: Boston Dynamics, Agility Robotics case studies

---

### 9. Lab Exercise Design

**Decision**: Scaffolded labs with starter code, clear objectives, and validation scripts

**Lab Structure**:
1. **Objective**: What student will accomplish (1-2 sentences)
2. **Prerequisites**: Prior knowledge/labs required
3. **Starter Code**: Partial implementation with TODOs
4. **Step-by-Step**: 5-10 numbered steps with expected outputs
5. **Validation**: Automated test script students run to verify success
6. **Extensions**: Optional challenges for advanced students

**Time Budget**: Each lab 1-3 hours (align with SC-009)

---

### 10. Hardware/Software Requirements Documentation

**Decision**: Create dedicated "Setup Guide" appendix with tiered requirements

**Requirement Tiers**:
- **Minimum** (Weeks 1-6): 8GB RAM, Ubuntu 22.04, integrated GPU
- **Recommended** (Weeks 7-10): 16GB RAM, NVIDIA GPU (4GB VRAM), Ubuntu 22.04
- **Cloud Alternative**: Instructions for Google Colab + ROS 2 Docker, AWS RoboMaker

**Software Stack**:
- Ubuntu 22.04 LTS (native or WSL2)
- ROS 2 Humble Desktop
- Python 3.10+
- Gazebo Classic 11
- Isaac Sim 2023.1+ (optional, Weeks 7-8)
- VS Code + ROS extension

---

---

## Module 2: The Digital Twin (Gazebo & Unity) - Research Findings

**Date**: 2025-12-17
**Purpose**: Document research findings for Module 2 simulation content

### 11. Digital Twin Concept Framing

**Decision**: Frame digital twin as "synchronized virtual replica for validation" with robotics-specific examples

**Rationale**:
- Industry 4.0 digital twin concept extends well to robotics
- Students understand the "test before deploy" value proposition immediately
- Connects URDF knowledge from Module 1 to simulation purpose in Module 2

**Key Teaching Points**:
- URDF/SDF as the "blueprint" shared between simulation and reality
- ROS 2 as the communication layer that works identically in both contexts
- Sim-to-real gap awareness (where digital twin diverges from reality)

**Real-World Examples**:
1. Boston Dynamics: Simulation-first development for Spot and Atlas
2. Agility Robotics: Digit simulation for warehouse testing
3. NASA: Mars rover simulation before deployment

**Alternatives Considered**:
- Abstract physics-first approach: Too theoretical, loses practical motivation
- Hardware-first approach: Expensive, dangerous, not reproducible for students

---

### 12. Gazebo Version Selection

**Decision**: Target Gazebo Fortress (LTS) with Harmonic as alternative

**Rationale**:
- Gazebo Fortress is the recommended LTS release for ROS 2 Humble
- Better physics engine options (Bullet, DART, TPE) than Gazebo Classic
- Modern SDF format with cleaner sensor definitions
- ros_gz bridge packages provide native ROS 2 integration
- Updated Module 1 research: Gazebo Classic is deprecated

**Version Specification**:
- **Primary**: Gazebo Fortress (supported through Sep 2026)
- **Alternative**: Gazebo Harmonic (for students wanting latest features)
- **Compatibility**: All examples tested on both versions

**Alternatives Considered**:
- **Gazebo Classic**: Deprecated, will lose support
- **Gazebo Garden**: Non-LTS, shorter support window
- **Gazebo Ionic**: Too new, not enough community resources

**Breaking Change Notes**:
- Gazebo Sim (Fortress+) uses different package naming than Gazebo Classic
- Commands use `gz sim` instead of `gazebo`
- URDF-to-SDF conversion may require adjustments

---

### 13. Physics Engine Depth

**Decision**: Conceptual coverage with practical demonstrations, not mathematical derivations

**Rationale**:
- Target audience is beginner-to-intermediate (not physics PhD students)
- Focus on "what happens" and "why it matters" rather than equations
- Hands-on experiments (change gravity, friction, mass) teach intuition
- Deep physics derivations available in external references if needed

**Topics Covered**:
1. **Rigid Body Dynamics**: Mass, inertia tensor, center of mass (conceptual)
2. **Collision Detection**: Bounding boxes, mesh collision, contact points
3. **Friction Models**: Coulomb friction, slip/no-slip states
4. **Time Stepping**: Fixed vs variable step, real-time factor
5. **Physics Engines**: ODE (default), Bullet, DART comparison overview

**Teaching Approach**:
- Visual demonstrations via Gazebo GUI
- "Change this parameter, observe that behavior" experiments
- Avoid differential equations; use intuitive explanations

**Alternatives Considered**:
- Full mathematical treatment: Appropriate for graduate physics course, not this textbook
- No physics at all: Students can't debug sim-to-real issues

---

### 14. Unity Coverage Scope

**Decision**: Conceptual comparison and architecture overview; no hands-on Unity labs

**Rationale**:
- Unity requires C# knowledge and different development environment
- Installing Unity + ROS-Unity-Bridge adds significant setup complexity
- Module 2 already covers Gazebo hands-on; Unity is comparative context
- Students can pursue Unity with external tutorials after understanding concepts
- Keeps module focused and achievable within time constraints

**Unity Content Scope**:
1. When to use Unity vs Gazebo (decision framework)
2. Unity's rendering pipeline for photorealistic environments
3. ROS-Unity-Bridge architecture diagram
4. Use cases: VR/AR robotics, human-robot interaction, synthetic data

**What's NOT Covered**:
- Unity installation
- C# programming
- Unity Editor workflows
- Hands-on Unity labs

**Alternatives Considered**:
- Full Unity labs: Doubles module scope, requires C# prerequisite
- No Unity mention: Leaves gap in students' tooling knowledge

---

### 15. Sensor Simulation Strategy

**Decision**: Cover 4 sensor types with Gazebo configuration and ROS 2 data consumption

**Sensor Coverage**:
| Sensor | Gazebo Plugin | ROS 2 Message Type | Use Case |
|--------|---------------|-------------------|----------|
| Camera | `libgazebo_ros_camera.so` | `sensor_msgs/Image` | Visual perception, object detection |
| Depth Camera | `libgazebo_ros_depth_camera.so` | `sensor_msgs/Image` + `PointCloud2` | 3D reconstruction, obstacle detection |
| LiDAR | `libgazebo_ros_ray_sensor.so` | `sensor_msgs/LaserScan` | 2D navigation, SLAM |
| IMU | `libgazebo_ros_imu.so` | `sensor_msgs/Imu` | Orientation, motion tracking |

**Teaching Progression**:
1. Camera: Most intuitive, students see what robot "sees"
2. LiDAR: Raycasting concept, visualize in RViz2
3. IMU: Orientation and acceleration data interpretation
4. Depth Camera: Combine visual + depth for 3D understanding

**Rationale**:
- These 4 sensors cover most robotics perception needs
- All have well-supported Gazebo plugins
- RViz2 visualization available for each
- Prepares students for Module 3 (perception algorithms)

**Alternatives Considered**:
- More sensors (GPS, force-torque, contact): Too many for one module
- Fewer sensors: Incomplete coverage of common robot sensors

---

### 16. SDF vs URDF Clarification

**Decision**: Teach URDF-to-SDF workflow; SDF for world files, URDF for robot models

**Rationale**:
- Students know URDF from Module 1 (don't abandon prior learning)
- SDF is more powerful but learning two formats is cognitive overload
- Practical approach: URDF for robots, SDF for worlds
- Gazebo converts URDF to SDF automatically; explain this process

**Content Structure**:
1. Review URDF from Module 1
2. Introduce SDF format and key differences
3. Show automatic URDF-to-SDF conversion
4. Teach SDF world file creation (lighting, terrain, obstacles)
5. Best practices: when to use each format

**Key Differences to Highlight**:
| Aspect | URDF | SDF |
|--------|------|-----|
| Origin | ROS-native | Gazebo-native |
| Physics | Limited | Full engine support |
| Sensors | Requires Gazebo plugins | Native sensor tags |
| World definition | Not supported | Full world support |
| Nested models | Not supported | Supported |

---

### 17. Mermaid Diagrams for Module 2

**Decision**: Create 3 required diagrams using Mermaid for MDX embedding

**Diagram 1: Simulation Pipeline**
```
graph LR
    A[URDF/SDF Model] --> B[Gazebo Sim]
    B --> C[Physics Engine]
    B --> D[Sensor Plugins]
    D --> E[ros_gz Bridge]
    E --> F[ROS 2 Topics]
    F --> G[Control Nodes]
    G --> E
    E --> B
```

**Diagram 2: Sensor Raycasting Flow**
```
sequenceDiagram
    participant S as Sensor Plugin
    participant P as Physics Engine
    participant B as ros_gz Bridge
    participant R as ROS 2 Topic
    S->>P: Cast ray/render frame
    P->>S: Collision points / pixels
    S->>B: Sensor data
    B->>R: Publish message
```

**Diagram 3: Gazebo vs Unity Comparison**
```
graph TB
    subgraph Gazebo
        G1[Open Source]
        G2[ROS Native]
        G3[Physics Focus]
        G4[Functional Graphics]
    end
    subgraph Unity
        U1[Proprietary]
        U2[ROS Bridge Required]
        U3[Rendering Focus]
        U4[Photorealistic Graphics]
    end
```

---

### 18. Lab Validation Scripts for Module 2

**Decision**: Python-based validation scripts checking Gazebo state and ROS 2 topics

**Validation Approach**:
- Scripts use `rclpy` to check topic publication
- Parse Gazebo world state via `gz` CLI commands
- Provide pass/fail feedback with error guidance

**Lab 1 Validation**: Check that robot spawned and topics publishing
**Lab 2 Validation**: Verify custom world file structure and physics parameters
**Lab 3 Validation**: Confirm 4 sensor types configured and publishing correct message types
**Lab 4 Validation**: Verify custom node subscribes and processes sensor data correctly

**Technical Requirements**:
- Scripts compatible with ROS 2 Humble + Gazebo Fortress
- No external dependencies beyond rclpy and standard library
- Clear error messages guiding students to fix issues

---

### 19. Module 2 Citation Strategy

**Decision**: 5+ new citations focused on simulation and digital twins

**Citation Categories**:
1. **Digital Twin Foundations**: 1-2 papers on digital twin concept
2. **Gazebo Documentation**: Official Gazebo Sim documentation
3. **Physics Simulation**: 1-2 papers on robotics simulation
4. **Sensor Simulation**: 1 paper on synthetic sensor data
5. **Unity/Visualization**: 1 reference on high-fidelity robotics visualization

**Proposed Citations**:
1. Grieves, M. (2014). Digital Twin: Manufacturing Excellence through Virtual Factory Replication.
2. Gazebo Documentation. (2024). Gazebo Sim: User Guide. Open Robotics.
3. Collins, J., et al. (2021). A Review of Physics Simulators for Robotic Applications. IEEE Access.
4. Mittal, M., et al. (2023). Orbit: A Unified Simulation Framework for Interactive Robot Learning. IEEE RA-L.
5. Unity Technologies. (2024). Unity Robotics Hub: ROS-Unity Integration.

---

## Phase 0 Summary

All technical unknowns resolved for Module 1 and Module 2. Ready to proceed to Phase 1 (data model and contracts).

**Key Takeaways - Module 1**:
1. Docusaurus + MDX for textbook format
2. ROS 2 Humble (LTS) for stability
3. Python-first with strategic C++ examples
4. Gazebo Classic primary, Isaac Sim advanced
5. Balanced URDF progression (2-DOF → 12-DOF)
6. Minimal in-text code + full GitHub repo
7. Mermaid + SVG + screenshots for diagrams
8. 15+ citations across theory, tools, and research
9. Scaffolded labs with validation scripts
10. Tiered hardware requirements + cloud alternatives

**Key Takeaways - Module 2**:
11. Digital twin as "synchronized virtual replica" with real-world examples
12. Gazebo Fortress (LTS) as primary simulator, not Classic
13. Conceptual physics coverage with hands-on experiments
14. Unity as conceptual comparison only (no hands-on labs)
15. 4 sensors covered: camera, depth camera, LiDAR, IMU
16. URDF for robots, SDF for worlds (practical workflow)
17. 3 Mermaid diagrams for architecture visualization
18. Python validation scripts for each lab
19. 5+ new citations for simulation content
