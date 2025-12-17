# Quickstart Guide: Vision-Language-Action (VLA) Module

## Overview
This guide provides a quick introduction to setting up and running the Vision-Language-Action (VLA) system for Physical AI & Humanoid Robotics. Follow these steps to get your VLA system up and running with basic functionality.

## Prerequisites

### System Requirements
- **Operating System**: Ubuntu 22.04 LTS (recommended) or compatible Linux distribution
- **Python**: Python 3.11 or higher
- **RAM**: Minimum 8GB (16GB recommended for optimal performance)
- **GPU**: NVIDIA GPU with CUDA support (optional but recommended for vision processing)
- **Disk Space**: At least 10GB free space for models and dependencies

### Hardware Requirements (for real robot deployment)
- Compatible humanoid robot platform with ROS 2 support
- RGB-D camera for vision processing
- Microphone array for speech recognition
- Speakers for audio feedback (optional)

## Installation

### 1. Clone the Repository
```bash
git clone <repository-url>
cd <repository-directory>
git checkout 004-vla-module  # Switch to the VLA module branch
```

### 2. Set Up Python Environment
```bash
# Create a virtual environment
python -m venv vla_env
source vla_env/bin/activate  # On Windows: vla_env\Scripts\activate

# Upgrade pip
pip install --upgrade pip
```

### 3. Install ROS 2 (Humble Hawksbill)
Follow the official ROS 2 installation guide for Ubuntu 22.04:
```bash
# Add ROS 2 apt repository
sudo apt update && sudo apt install -y curl gnupg lsb-release
curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros-iron/rpm/ros.key | sudo gpg --dearmor -o /usr/share/keyrings/ros-archive-keyring.gpg

# Add the repository to your sources list
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] http://packages.ros.org/ros2/ubuntu $(source /etc/os-release && echo $UBUNTU_CODENAME) main" | sudo tee /etc/apt/sources.list.d/ros2.list > /dev/null

# Install ROS 2 packages
sudo apt update
sudo apt install -y ros-humble-desktop
sudo apt install -y python3-colcon-common-extensions
sudo apt install -y python3-rosdep python3-vcstool
```

### 4. Install Python Dependencies
```bash
# Activate your virtual environment
source vla_env/bin/activate

# Install core dependencies
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
pip install transformers openai-whisper opencv-python numpy scipy

# Install ROS 2 Python packages
pip install roslibpy rclpy

# Install additional dependencies
pip install speechrecognition pyaudio transformers accelerate datasets
```

### 5. Install Additional Tools
```bash
# For simulation (Gazebo)
sudo apt install -y ros-humble-gazebo-ros-pkgs ros-humble-gazebo-ros2-control ros-humble-gazebo-ros2-control-demos

# For visualization
sudo apt install -y ros-humble-rviz2 ros-humble-ros2-controllers ros-humble-joint-state-publisher-gui
```

## Configuration

### 1. Environment Setup
Create a configuration file at `vla_module/config/vla_config.yaml`:

```yaml
# VLA Module Configuration
speech_recognition:
  model_size: "large"  # Options: tiny, base, small, medium, large
  language: "en"
  device: "cuda"  # Options: cuda, cpu
  sample_rate: 16000

vision_system:
  model_name: "facebook/detr-resnet-50"
  confidence_threshold: 0.7
  device: "cuda"  # Options: cuda, cpu
  camera_topic: "/camera/color/image_raw"

llm_planning:
  model_name: "gpt-3.5-turbo"  # Or local model like "llama"
  max_tokens: 500
  temperature: 0.3
  api_key: "your-api-key-here"  # Or local model path

ros2_interfaces:
  action_timeout: 30.0  # seconds
  feedback_frequency: 1.0  # Hz
  robot_namespace: "/robot1"

simulation:
  enabled: true
  world_file: "default_world.sdf"
  physics_engine: "ode"

logging:
  level: "INFO"
  file_path: "./logs/vla_system.log"
  max_file_size: "10MB"
  backup_count: 5
```

### 2. Model Downloads
Download required models (this may take some time):

```bash
# Download Whisper model for speech recognition
python -c "import openai_whisper; openai_whisper.load_model('large')"

# Download vision model
python -c "from transformers import DetrImageProcessor, DetrForObjectDetection; DetrImageProcessor.from_pretrained('facebook/detr-resnet-50'); DetrForObjectDetection.from_pretrained('facebook/detr-resnet-50')"
```

## Running the System

### 1. Start ROS 2 Environment
```bash
# Source ROS 2 setup
source /opt/ros/humble/setup.bash
source install/setup.bash  # If you built from source

# Start ROS 2 daemon
ros2 daemon start
```

### 2. Launch Simulation (Optional - for testing without real robot)
```bash
# Terminal 1: Launch Gazebo simulation
ros2 launch vla_module simulation.launch.py

# Terminal 2: Launch robot controllers
ros2 launch vla_module robot_controllers.launch.py
```

### 3. Run the VLA Pipeline
```bash
# In your virtual environment
source vla_env/bin/activate

# Run the main VLA system
python -m vla_module.vla_pipeline.vla_manager --config-path ./vla_module/config/vla_config.yaml
```

### 4. Test with Sample Commands
Once the system is running, you can test it with these sample commands:

```
"Move to the kitchen"
"Pick up the red ball"
"Go to the table and wait there"
"Bring me the cup from the counter"
```

## Basic Usage Examples

### Example 1: Simple Object Grasping
```python
from vla_module.vla_pipeline.vla_manager import VLAManager
from vla_module.utils.config_loader import ConfigLoader

# Load configuration
config = ConfigLoader.load_config("./vla_module/config/vla_config.yaml")

# Initialize VLA manager
vla_manager = VLAManager(config)

# Process a command
command = "Grasp the blue cube on the table"
result = vla_manager.process_command(command)

print(f"Command processed: {result.success}")
print(f"Generated plan: {result.plan_steps}")
```

### Example 2: Vision-Only Processing
```python
from vla_module.vision_system.object_detector import ObjectDetector

detector = ObjectDetector(model_name="facebook/detr-resnet-50")

# Process an image
image_path = "./test_images/scene.jpg"
objects = detector.detect_objects(image_path)

for obj in objects:
    print(f"Detected {obj.class_label} with confidence {obj.confidence:.2f}")
```

### Example 3: Speech Recognition Test
```python
from vla_module.speech_recognition.whisper_interface import WhisperInterface

whisper = WhisperInterface(model_size="large")

# Transcribe audio file
audio_path = "./test_audio/command.wav"
transcription = whisper.transcribe(audio_path)

print(f"Transcribed: {transcription.text}")
print(f"Confidence: {transcription.confidence:.2f}")
```

## Troubleshooting

### Common Issues

#### Issue: CUDA out of memory
**Solution**:
- Reduce batch size in configuration
- Use CPU instead of GPU by changing device to "cpu"
- Close other GPU-intensive applications

#### Issue: ROS 2 nodes not communicating
**Solution**:
- Check if ROS 2 daemon is running: `ros2 daemon status`
- Verify network configuration if using multiple machines
- Check ROS_DOMAIN_ID environment variable

#### Issue: Speech recognition not working
**Solution**:
- Check microphone permissions
- Verify PyAudio installation: `python -c "import pyaudio"`
- Test with audio file instead of live recording

#### Issue: Vision system not detecting objects
**Solution**:
- Verify camera connection and topic
- Check lighting conditions
- Adjust confidence threshold in config

### Checking System Status
```bash
# Check running ROS 2 nodes
ros2 node list

# Check active topics
ros2 topic list

# Monitor system performance
python -m vla_module.utils.system_monitor
```

## Next Steps

1. **Customize Configuration**: Modify the configuration file to suit your specific robot and environment
2. **Train Custom Models**: Fine-tune models for your specific domain and vocabulary
3. **Add New Actions**: Extend the action library with custom robot capabilities
4. **Integrate with Real Robot**: Connect to your physical robot platform
5. **Performance Tuning**: Optimize for your specific hardware and use case

## Getting Help

- Check the [full documentation](./docs/)
- Look at the [examples folder](./examples/)
- Review the [API reference](./api/)
- Join our [community forum](link-to-forum)

For technical issues, please open an issue on the repository with:
- Your system configuration
- Steps to reproduce the issue
- Relevant log files
- Expected vs. actual behavior