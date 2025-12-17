# API Contracts: Vision-Language-Action (VLA) Module

## Overview
This document defines the API contracts for the Vision-Language-Action (VLA) system, specifying the interfaces between different components and with external systems. These contracts ensure consistent communication and interoperability across the VLA pipeline.

## 1. Speech Recognition Service Contract

### 1.1 Transcribe Audio Endpoint
**Purpose**: Convert audio input to text using Whisper ASR

**Request**:
```
POST /api/v1/speech/transcribe
Content-Type: multipart/form-data or application/json
```

**Request Body** (for JSON):
```json
{
  "audio_data": "base64_encoded_audio",
  "sample_rate": 16000,
  "language": "en",
  "model_size": "large"
}
```

**Response**:
```json
{
  "transcription": {
    "text": "string",
    "confidence": 0.95,
    "language": "en",
    "processing_time": 1.2
  },
  "request_id": "uuid",
  "timestamp": "2025-12-17T10:30:00Z"
}
```

**Error Response**:
```json
{
  "error": {
    "code": "TRANSCRIPTION_ERROR",
    "message": "string",
    "details": {}
  },
  "request_id": "uuid",
  "timestamp": "2025-12-17T10:30:00Z"
}
```

### 1.2 Audio Processing Endpoint
**Purpose**: Preprocess audio data for noise reduction and normalization

**Request**:
```
POST /api/v1/speech/process
Content-Type: application/json
```

**Request Body**:
```json
{
  "audio_data": "base64_encoded_audio",
  "sample_rate": 16000,
  "noise_reduction": true,
  "normalization": true
}
```

**Response**:
```json
{
  "processed_audio": "base64_encoded_audio",
  "sample_rate": 16000,
  "duration": 2.5,
  "signal_quality": 0.85
}
```

## 2. Command Parsing Service Contract

### 2.1 Parse Command Endpoint
**Purpose**: Parse transcribed text into structured command format

**Request**:
```
POST /api/v1/command/parse
Content-Type: application/json
```

**Request Body**:
```json
{
  "raw_text": "Pick up the red ball from the table",
  "context": {
    "environment": "indoor",
    "robot_capabilities": ["grasp", "navigate"],
    "object_database": ["red ball", "table", "chair"]
  }
}
```

**Response**:
```json
{
  "parsed_command": {
    "intent": "grasp_object",
    "entities": [
      {
        "type": "object",
        "value": "red ball",
        "attributes": {"color": "red", "shape": "ball"}
      },
      {
        "type": "location",
        "value": "table"
      }
    ],
    "action_sequence": [
      {
        "action_type": "navigate_to",
        "parameters": {"location": "table"}
      },
      {
        "action_type": "locate_object",
        "parameters": {"object": "red ball"}
      },
      {
        "action_type": "grasp_object",
        "parameters": {"object": "red ball"}
      }
    ],
    "confidence": 0.87
  },
  "request_id": "uuid",
  "timestamp": "2025-12-17T10:30:00Z"
}
```

## 3. Cognitive Planning Service Contract

### 3.1 Generate Plan Endpoint
**Purpose**: Generate high-level cognitive plan from parsed command

**Request**:
```
POST /api/v1/planning/generate
Content-Type: application/json
```

**Request Body**:
```json
{
  "command": {
    "intent": "grasp_object",
    "entities": [...],
    "action_sequence": [...]
  },
  "context": {
    "environment_map": "map_id",
    "robot_state": {
      "position": {"x": 0.0, "y": 0.0, "z": 0.0},
      "battery_level": 0.85,
      "gripper_state": "open"
    },
    "object_poses": [
      {"id": "red_ball", "pose": {"x": 1.0, "y": 0.5, "z": 0.0}}
    ]
  }
}
```

**Response**:
```json
{
  "cognitive_plan": {
    "plan_id": "uuid",
    "overall_goal": "grasp_object",
    "plan_steps": [
      {
        "step_id": "uuid",
        "description": "Navigate to object location",
        "required_actions": [
          {
            "action_id": "uuid",
            "action_type": "navigate_to",
            "parameters": {"target_pose": {"x": 1.0, "y": 0.5, "z": 0.0}}
          }
        ],
        "preconditions": ["navigation_clear", "battery_level > 0.2"],
        "expected_outcomes": ["robot_at_target_pose"]
      }
    ],
    "estimated_duration": 45.0,
    "risk_assessment": {
      "risk_score": 0.15,
      "safety_risks": [],
      "mitigation_strategies": []
    }
  },
  "request_id": "uuid",
  "timestamp": "2025-12-17T10:30:00Z"
}
```

## 4. Vision System Service Contract

### 4.1 Detect Objects Endpoint
**Purpose**: Detect and recognize objects in a given image

**Request**:
```
POST /api/v1/vision/detect_objects
Content-Type: multipart/form-data or application/json
```

**Request Body** (for JSON):
```json
{
  "image_data": "base64_encoded_image",
  "model_name": "facebook/detr-resnet-50",
  "confidence_threshold": 0.7
}
```

**Response**:
```json
{
  "detection_results": {
    "objects": [
      {
        "object_id": "uuid",
        "class_label": "ball",
        "confidence": 0.92,
        "bounding_box": {
          "x_min": 0.3,
          "y_min": 0.4,
          "x_max": 0.5,
          "y_max": 0.6
        },
        "pose": {
          "position": {"x": 1.0, "y": 0.5, "z": 0.0},
          "orientation": {"x": 0.0, "y": 0.0, "z": 0.0, "w": 1.0}
        },
        "properties": {
          "color": "red",
          "size": "medium"
        }
      }
    ],
    "processing_time": 0.15,
    "image_resolution": {"width": 640, "height": 480}
  },
  "request_id": "uuid",
  "timestamp": "2025-12-17T10:30:00Z"
}
```

### 4.2 Estimate Pose Endpoint
**Purpose**: Estimate 3D pose of objects in the environment

**Request**:
```
POST /api/v1/vision/estimate_pose
Content-Type: application/json
```

**Request Body**:
```json
{
  "image_data": "base64_encoded_image",
  "object_id": "target_object",
  "camera_intrinsics": {
    "fx": 554.25,
    "fy": 554.25,
    "cx": 320.0,
    "cy": 240.0
  }
}
```

**Response**:
```json
{
  "pose_estimate": {
    "position": {"x": 1.0, "y": 0.5, "z": 0.0},
    "orientation": {"x": 0.0, "y": 0.0, "z": 0.0, "w": 1.0},
    "confidence": 0.89,
    "uncertainty": [
      [0.01, 0.0, 0.0],
      [0.0, 0.01, 0.0],
      [0.0, 0.0, 0.01]
    ]
  },
  "request_id": "uuid",
  "timestamp": "2025-12-17T10:30:00Z"
}
```

## 5. ROS 2 Interface Contract

### 5.1 Execute Action Endpoint
**Purpose**: Execute a robot action through ROS 2 action interface

**Request**:
```
POST /api/v1/ros2/execute_action
Content-Type: application/json
```

**Request Body**:
```json
{
  "action_name": "move_to_pose",
  "goal": {
    "target_pose": {
      "position": {"x": 1.0, "y": 0.5, "z": 0.0},
      "orientation": {"x": 0.0, "y": 0.0, "z": 0.0, "w": 1.0}
    },
    "tolerance": 0.1
  },
  "timeout": 30.0,
  "feedback_callback": true
}
```

**Response**:
```json
{
  "execution_result": {
    "success": true,
    "result_data": {
      "final_pose": {
        "position": {"x": 1.002, "y": 0.498, "z": 0.0},
        "orientation": {"x": 0.001, "y": -0.001, "z": 0.002, "w": 0.999}
      },
      "execution_time": 12.5
    },
    "error_code": null,
    "error_message": null
  },
  "request_id": "uuid",
  "action_id": "uuid",
  "timestamp": "2025-12-17T10:30:00Z"
}
```

### 5.2 Get Robot State Endpoint
**Purpose**: Retrieve current state of the robot

**Request**:
```
GET /api/v1/ros2/robot_state
```

**Response**:
```json
{
  "robot_state": {
    "position": {"x": 0.0, "y": 0.0, "z": 0.0},
    "orientation": {"x": 0.0, "y": 0.0, "z": 0.0, "w": 1.0},
    "battery_level": 0.85,
    "gripper_state": "open",
    "joint_states": {
      "arm_joint_1": 0.0,
      "arm_joint_2": 0.0,
      "gripper_joint": 0.5
    },
    "active_actions": [],
    "communication_status": "connected"
  },
  "timestamp": "2025-12-17T10:30:00Z"
}
```

## 6. VLA Pipeline Orchestration Contract

### 6.1 Process Command Endpoint
**Purpose**: Full VLA pipeline execution from speech input to action execution

**Request**:
```
POST /api/v1/vla/process_command
Content-Type: multipart/form-data or application/json
```

**Request Body** (for JSON):
```json
{
  "input_type": "speech",  // or "text"
  "input_data": "base64_encoded_audio_or_text",
  "context": {
    "environment": "kitchen",
    "robot_id": "robot1",
    "priority": 1
  }
}
```

**Response**:
```json
{
  "pipeline_result": {
    "command_id": "uuid",
    "pipeline_state": "completed",  // or "failed", "in_progress"
    "transcription": "Pick up the red ball from the table",
    "parsed_command": {...},
    "cognitive_plan": {...},
    "execution_results": [
      {
        "action_id": "uuid",
        "action_type": "navigate_to",
        "success": true,
        "execution_time": 15.2
      }
    ],
    "overall_success": true,
    "total_processing_time": 45.7
  },
  "request_id": "uuid",
  "timestamp": "2025-12-17T10:30:00Z"
}
```

### 6.2 Get Pipeline Status Endpoint
**Purpose**: Check status of ongoing VLA pipeline execution

**Request**:
```
GET /api/v1/vla/pipeline_status/{command_id}
```

**Response**:
```json
{
  "pipeline_status": {
    "command_id": "uuid",
    "current_stage": "executing_actions",  // listening, processing_speech, planning, executing, completed, failed
    "progress": 0.75,
    "current_action": "grasping_object",
    "estimated_remaining_time": 12.3,
    "error_message": null
  },
  "timestamp": "2025-12-17T10:30:00Z"
}
```

## 7. Error Handling Contract

### 7.1 Standard Error Format
All services must return errors in the following format:

```json
{
  "error": {
    "code": "ERROR_CODE",
    "message": "Human-readable error message",
    "details": {
      // Service-specific error details
    },
    "timestamp": "2025-12-17T10:30:00Z",
    "request_id": "uuid"
  }
}
```

### 7.2 Common Error Codes
- `VALIDATION_ERROR`: Request validation failed
- `PROCESSING_ERROR`: Error during processing
- `RESOURCE_UNAVAILABLE`: Required resource not available
- `TIMEOUT_ERROR`: Operation timed out
- `PERMISSION_DENIED`: Insufficient permissions
- `INTERNAL_ERROR`: Internal system error

## 8. Security Contract

### 8.1 Authentication
All API endpoints require authentication using API keys or JWT tokens.

### 8.2 Authorization
- Robot control endpoints require elevated permissions
- Read-only endpoints available with basic permissions
- Configuration endpoints require admin permissions

### 8.3 Rate Limiting
- Speech processing: 10 requests per minute per client
- Vision processing: 5 requests per minute per client
- Action execution: 20 requests per minute per robot