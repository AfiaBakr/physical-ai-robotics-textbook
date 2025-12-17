# Quickstart Guide: Isaac AI Robot Brain Module (NVIDIA Isaac)

**Feature**: 003-isaac-ai-brain
**Created**: 2025-12-17
**Status**: Complete

## Overview

This quickstart guide provides the essential steps to set up your environment for the Isaac AI Robot Brain Module. This module focuses on teaching AI-driven perception, mapping, and navigation using NVIDIA Isaac in humanoid robotics.

## Prerequisites

Before starting this module, you should have:
- Basic understanding of ROS 2 concepts
- Knowledge of URDF (Unified Robot Description Format)
- Familiarity with robotics simulation concepts
- Understanding of fundamental robotics terminology

## Hardware Requirements

### Minimum Requirements
- CPU: Intel i5 or AMD Ryzen 5 (8+ cores)
- RAM: 16 GB
- GPU: NVIDIA RTX 2060 with 8GB VRAM
- Storage: 50 GB available space
- OS: Ubuntu 20.04 LTS or Windows 10/11

### Recommended Requirements
- CPU: Intel i7/i9 or AMD Ryzen 7/9 (8+ cores)
- RAM: 32 GB
- GPU: NVIDIA RTX 3080/4080 or higher with 12GB+ VRAM
- Storage: 100 GB SSD
- OS: Ubuntu 20.04 LTS (preferred for ROS 2 development)

## Software Installation

### Step 1: Install ROS 2
1. Follow the official ROS 2 installation guide for your OS: [https://docs.ros.org/en/humble/Installation.html](https://docs.ros.org/en/humble/Installation.html)
2. We recommend using ROS 2 Humble Hawksbill (LTS version)
3. Install the desktop version which includes development tools

### Step 2: Install NVIDIA Isaac Sim
1. Sign up for NVIDIA Developer account at [developer.nvidia.com](https://developer.nvidia.com)
2. Download Isaac Sim from the Isaac section
3. Follow the installation instructions for your platform
4. Ensure your GPU drivers are up to date (minimum driver version 515+)

### Step 3: Install Isaac ROS Packages
1. Add the Isaac ROS repository:
   ```bash
   sudo apt update && sudo apt install wget
   sudo wget -O /usr/share/keyrings/ros-archive-keyring.gpg https://raw.githubusercontent.com/RobotLocomotion/drake/main/setup/ubuntu/jammy/2022-10-11-ros-archive-keyring.gpg
   echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] http://packages.ros.org/ros2/ubuntu $(. /etc/os-release && echo $UBUNTU_CODENAME) main" | sudo tee /etc/apt/sources.list.d/ros2.list > /dev/null
   sudo apt update
   ```
2. Install Isaac ROS packages:
   ```bash
   sudo apt install ros-humble-isaac-ros-dev
   ```

### Step 4: Verify Installation
1. Source your ROS 2 installation:
   ```bash
   source /opt/ros/humble/setup.bash
   ```
2. Test Isaac Sim by launching a simple scene:
   ```bash
   # Navigate to your Isaac Sim installation
   # Launch Isaac Sim and verify the UI opens without errors
   ```

## Setting Up Your Workspace

### Create a ROS 2 Workspace
```bash
mkdir -p ~/isaac_ws/src
cd ~/isaac_ws
colcon build
source install/setup.bash
```

### Download Sample Assets
1. Clone the sample repository:
   ```bash
   cd ~/isaac_ws/src
   git clone https://github.com/NVIDIA-ISAAC-ROS/isaac_ros_common.git
   ```
2. Build the workspace again:
   ```bash
   cd ~/isaac_ws
   colcon build
   source install/setup.bash
   ```

## First Exercise: Hello Isaac Sim

### Objective
Launch Isaac Sim and explore a basic robot scene to familiarize yourself with the environment.

### Steps
1. Launch Isaac Sim:
   ```bash
   cd /path/to/isaac-sim
   ./isaac-sim.sh
   ```
2. Open the "Robotics" menu and select "Create New Scene"
3. Add a simple robot (e.g., a wheeled robot model)
4. Add basic sensors (RGB camera, depth camera)
5. Run the simulation and observe the robot and sensor outputs

### Expected Outcome
- Isaac Sim launches without errors
- You can see the 3D scene with the robot
- Sensor data is being generated and visualized
- You can pause and resume the simulation

## Troubleshooting Common Issues

### Isaac Sim Won't Launch
- Verify GPU drivers are up to date
- Check that your GPU meets the minimum requirements
- Ensure no other applications are using GPU exclusively

### ROS 2 Packages Not Found
- Verify you've sourced the ROS 2 setup file
- Check that Isaac ROS packages were installed correctly
- Confirm your workspace is built and sourced

### Performance Issues
- Close other GPU-intensive applications
- Reduce Isaac Sim quality settings temporarily
- Check that you have sufficient RAM available

## Next Steps

After completing this quickstart:
1. Proceed to Lesson 1: The AI-Robot Brain & Isaac Sim
2. Review the learning objectives for the module
3. Set up your development environment for the lab exercises
4. Join the community forum for additional support

## Additional Resources

- [NVIDIA Isaac Sim Documentation](https://docs.omniverse.nvidia.com/isaacsim/latest/isaacsim.html)
- [ROS 2 Documentation](https://docs.ros.org/en/humble/)
- [Isaac ROS GitHub Repository](https://github.com/NVIDIA-ISAAC-ROS)
- [NVIDIA Developer Forums](https://forums.developer.nvidia.com/)

## Support

If you encounter issues not covered in this quickstart:
1. Check the troubleshooting section above
2. Consult the additional resources
3. Post in the community forum with detailed error messages
4. Verify your hardware meets the requirements