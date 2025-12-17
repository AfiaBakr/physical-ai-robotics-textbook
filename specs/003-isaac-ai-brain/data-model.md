# Data Model: Isaac AI Robot Brain Module (NVIDIA Isaac)

**Feature**: 003-isaac-ai-brain
**Created**: 2025-12-17
**Status**: Complete

## Overview

This module focuses on educational content rather than data processing systems. The data model represents the organizational structure for the educational content and supporting materials.

## Content Entities

### Lesson
- **id**: String (unique identifier for the lesson)
- **title**: String (lesson title)
- **objectives**: Array<String> (learning objectives for the lesson)
- **content**: String (main content in markdown format)
- **duration**: Number (estimated completion time in minutes)
- **prerequisites**: Array<String> (required knowledge or completed lessons)
- **related_labs**: Array<String> (IDs of related lab exercises)
- **diagrams**: Array<String> (IDs of diagrams used in the lesson)

### Lab Exercise
- **id**: String (unique identifier for the lab)
- **title**: String (lab title)
- **objectives**: Array<String> (learning objectives for the lab)
- **steps**: Array<String> (sequential steps to complete the lab)
- **expected_outcome**: String (description of successful completion)
- **difficulty**: Enum ("beginner", "intermediate", "advanced")
- **estimated_time**: Number (time needed in minutes)
- **required_tools**: Array<String> (tools needed for the lab)
- **validation_criteria**: Array<String> (how to verify success)

### Diagram
- **id**: String (unique identifier for the diagram)
- **title**: String (diagram title)
- **type**: Enum ("workflow", "architecture", "process", "comparison", "overview")
- **description**: String (explanation of what the diagram shows)
- **source**: String (file path or generation method)
- **target_lesson**: String (ID of lesson that uses this diagram)
- **alt_text**: String (accessibility description)

### Assessment
- **id**: String (unique identifier for the assessment)
- **type**: Enum ("quiz", "review", "practical", "conceptual")
- **questions**: Array<Object> (array of question objects)
- **learning_outcome_alignment**: Array<String> (IDs of learning outcomes addressed)
- **difficulty**: Enum ("beginner", "intermediate", "advanced")
- **time_limit**: Number (time limit in minutes, if applicable)

### Question (nested in Assessment)
- **id**: String (unique identifier for the question)
- **text**: String (the question text)
- **type**: Enum ("multiple_choice", "true_false", "short_answer", "practical_task")
- **options**: Array<String> (for multiple choice questions)
- **correct_answer**: String | Array<String> (the correct answer(s))
- **explanation**: String (explanation of the correct answer)

### Learning Outcome
- **id**: String (unique identifier for the learning outcome)
- **description**: String (what the learner will be able to do)
- **associated_lessons**: Array<String> (IDs of lessons that address this outcome)
- **assessment_methods**: Array<String> (how this outcome will be assessed)

## Simulation Environment Entities

### Isaac Sim Scene
- **id**: String (unique identifier for the scene)
- **name**: String (scene name)
- **description**: String (what the scene is designed for)
- **robot_model**: String (URDF model used in the scene)
- **sensors_configured**: Array<String> (sensors available in the scene)
- **navigation_goals**: Array<Object> (predefined navigation goals for exercises)
- **assets_path**: String (path to scene assets)

### Robot Configuration
- **id**: String (unique identifier for the robot config)
- **name**: String (robot name)
- **urdf_path**: String (path to URDF file)
- **sensors**: Array<Object> (sensor configurations)
- **actuators**: Array<Object> (actuator configurations)
- **navigation_capabilities**: Object (navigation-specific configurations)

## Educational Workflow

The data model supports the following workflow:
1. Learners progress through lessons in sequence (with proper prerequisites)
2. Each lesson includes related lab exercises for hands-on practice
3. Diagrams support visual understanding of concepts
4. Assessments validate learning outcomes
5. All content is aligned with the module's learning objectives

## Relationships

- **Lesson** 1-to-many **Lab Exercise**: Each lesson may have multiple related labs
- **Lesson** 1-to-many **Diagram**: Each lesson may use multiple diagrams
- **Assessment** many-to-many **Learning Outcome**: Assessments may test multiple outcomes
- **Lesson** many-to-many **Learning Outcome**: Lessons address multiple outcomes
- **Lab Exercise** 1-to-1 **Isaac Sim Scene**: Each lab uses a specific scene

## Validation Rules

- Each lesson must have at least one related lab exercise
- All learning outcomes must be addressed by at least one lesson
- All assessments must align with at least one learning outcome
- Diagrams must have appropriate alt text for accessibility
- Lab exercises must have clearly defined validation criteria
- Prerequisites must be satisfied before accessing advanced content