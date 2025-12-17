# Quickstart Guide: Physical AI & Humanoid Robotics Textbook

**Feature**: 001-physical-ai-robotics-book
**Date**: 2025-12-15
**Purpose**: Get started creating textbook content quickly

## Overview

This guide helps you start creating content for the Physical AI & Humanoid Robotics textbook using Docusaurus, following the data model and project structure defined in this specification.

---

## Prerequisites

Before you begin, ensure you have:

- **Node.js** 18.x or higher ([Download](https://nodejs.org/))
- **Git** for version control
- **Text editor** (VS Code recommended)
- **Basic Markdown knowledge**

---

## Quick Setup (5 minutes)

### 1. Initialize Docusaurus Project

```bash
# Create new Docusaurus site
npx create-docusaurus@latest physical-ai-robotics-textbook classic

cd physical-ai-robotics-textbook

# Install additional plugins
npm install --save @docusaurus/theme-mermaid
npm install --save remark-math rehype-katex  # For mathematical notation
```

### 2. Configure Docusaurus

Edit `docusaurus.config.js`:

```javascript
module.exports = {
  title: 'Physical AI & Humanoid Robotics',
  tagline: 'A Complete Course on Embodied Intelligence',
  url: 'https://yourusername.github.io',
  baseUrl: '/physical-ai-robotics-textbook/',

  markdown: {
    mermaid: true,
  },
  themes: ['@docusaurus/theme-mermaid'],

  themeConfig: {
    navbar: {
      title: 'Physical AI',
      items: [
        {to: '/docs/intro', label: 'Course', position: 'left'},
        {to: '/labs', label: 'Labs', position: 'left'},
        {href: 'https://github.com/yourusername/physical-ai-robotics-textbook', label: 'GitHub', position: 'right'},
      ],
    },
  },

  plugins: [
    [
      '@docusaurus/plugin-content-docs',
      {
        id: 'labs',
        path: 'labs',
        routeBasePath: 'labs',
        sidebarPath: require.resolve('./sidebarsLabs.js'),
      },
    ],
  ],
};
```

### 3. Create Initial Content Structure

```bash
# Create directories
mkdir -p docs/appendix
mkdir -p labs
mkdir -p static/diagrams
mkdir -p static/img

# Create first chapter
cat > docs/chapter-01-physical-ai-intro.mdx << 'EOF'
---
sidebar_position: 1
---

# Chapter 1: Introduction to Physical AI

## Learning Objectives

By the end of this chapter, you will be able to:

1. Define Physical AI and explain how it differs from purely digital AI
2. Describe the key components of embodied intelligence
3. Identify real-world applications of humanoid robotics

## 1.1 What is Physical AI?

Physical AI represents the convergence of artificial intelligence with physical embodiment...

<!-- Continue with content -->
EOF
```

### 4. Run Development Server

```bash
npm start
```

Your textbook will be available at `http://localhost:3000`

---

---

## Module 2: Simulation Environment Setup

After completing the basic setup, prepare for Module 2 content:

### 1. Install Gazebo Dependencies

```bash
# Install Gazebo Fortress (for Ubuntu 22.04 + ROS 2 Humble)
sudo apt update
sudo apt install ros-humble-ros-gz

# Verify installation
gz sim --version
```

### 2. Install ROS-Gazebo Bridge

```bash
# Install ros_gz bridge packages
sudo apt install ros-humble-ros-gz-bridge ros-humble-ros-gz-sim

# Verify bridge availability
ros2 pkg list | grep ros_gz
```

### 3. Create Module 2 Lab Structure

```bash
# Create Module 2 directories
mkdir -p labs/module-02/lab-01-physics-experiments/{starter,solution}
mkdir -p labs/module-02/lab-02-gazebo-worlds/{starter,solution}/worlds
mkdir -p labs/module-02/lab-03-sensor-visualization/{starter,solution}

# Create category file
cat > labs/module-02/_category_.json << 'EOF'
{
  "label": "Module 2: The Digital Twin",
  "position": 2,
  "link": {
    "type": "generated-index",
    "description": "Hands-on labs for Gazebo simulation and sensor configuration."
  }
}
EOF
```

### 4. Create Sample Gazebo World File

```bash
cat > labs/module-02/lab-02-gazebo-worlds/starter/worlds/empty_world.sdf << 'EOF'
<?xml version="1.0" ?>
<sdf version="1.8">
  <world name="module2_world">
    <physics name="1ms" type="ode">
      <max_step_size>0.001</max_step_size>
      <real_time_factor>1.0</real_time_factor>
    </physics>
    <plugin
      filename="gz-sim-physics-system"
      name="gz::sim::systems::Physics">
    </plugin>
    <plugin
      filename="gz-sim-scene-broadcaster-system"
      name="gz::sim::systems::SceneBroadcaster">
    </plugin>
    <light type="directional" name="sun">
      <cast_shadows>true</cast_shadows>
      <pose>0 0 10 0 0 0</pose>
      <diffuse>0.8 0.8 0.8 1</diffuse>
    </light>
    <model name="ground_plane">
      <static>true</static>
      <link name="link">
        <collision name="collision">
          <geometry>
            <plane>
              <normal>0 0 1</normal>
            </plane>
          </geometry>
        </collision>
      </link>
    </model>
  </world>
</sdf>
EOF
```

### 5. Test Gazebo Launch

```bash
# Launch Gazebo with the sample world
gz sim labs/module-02/lab-02-gazebo-worlds/starter/worlds/empty_world.sdf
```

---

## Next Steps

1. **Read the full data model**: [data-model.md](./data-model.md)
2. **Review Module 1 plan**: [plan.md](./plan.md)
3. **Review Module 2 spec**: [modules/module-02-digital-twin-spec.md](./modules/module-02-digital-twin-spec.md)
4. **Start writing content**: Follow lesson template structure
5. **Create labs**: Follow lab template structure with validation scripts

---

## Resources

### General
- [Docusaurus Documentation](https://docusaurus.io/docs)
- [Mermaid Syntax](https://mermaid.js.org/intro/)
- [APA Citation Style Guide](https://apastyle.apa.org/)

### Module 1 - ROS 2
- [ROS 2 Humble Docs](https://docs.ros.org/en/humble/)
- [rclpy API Reference](https://docs.ros2.org/humble/api/rclpy/)

### Module 2 - Simulation
- [Gazebo Sim Documentation](https://gazebosim.org/docs)
- [ros_gz Bridge Tutorial](https://gazebosim.org/docs/fortress/ros2_integration)
- [SDF Format Specification](http://sdformat.org/spec)
- [Unity Robotics Hub](https://github.com/Unity-Technologies/Unity-Robotics-Hub)
