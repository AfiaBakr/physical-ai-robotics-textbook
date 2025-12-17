---
id: 007
title: Implement Module 4 VLA Mini-Projects and Labs Sidebar
stage: green
date: 2025-12-17
surface: agent
model: claude-opus-4.5
feature: 001-physical-ai-robotics-book
branch: 004-vla-module
user: user
command: /sp.implement
labels: ["module-4", "vla", "mini-projects", "labs", "sidebar"]
links:
  spec: specs/001-physical-ai-robotics-book/spec.md
  ticket: null
  adr: null
  pr: null
files:
  - physical-ai-robotics-textbook/sidebarsLabs.ts
  - physical-ai-robotics-textbook/docs/module-04-vla/lesson-03-vla-integration.mdx
  - physical-ai-robotics-textbook/labs/module-04/mini-project-01-simple-vla/starter/vla_pipeline.py
  - physical-ai-robotics-textbook/labs/module-04/mini-project-01-simple-vla/starter/speech_recognizer.py
  - physical-ai-robotics-textbook/labs/module-04/mini-project-01-simple-vla/starter/action_executor.py
  - physical-ai-robotics-textbook/labs/module-04/mini-project-01-simple-vla/solution/vla_pipeline.py
  - physical-ai-robotics-textbook/labs/module-04/mini-project-01-simple-vla/solution/speech_recognizer.py
  - physical-ai-robotics-textbook/labs/module-04/mini-project-01-simple-vla/solution/action_executor.py
  - physical-ai-robotics-textbook/labs/module-04/mini-project-02-advanced-vla/starter/vla_advanced_pipeline.py
  - physical-ai-robotics-textbook/labs/module-04/mini-project-02-advanced-vla/starter/vision_processor.py
  - physical-ai-robotics-textbook/labs/module-04/mini-project-02-advanced-vla/starter/cognitive_planner.py
  - physical-ai-robotics-textbook/labs/module-04/mini-project-02-advanced-vla/starter/safety_monitor.py
  - physical-ai-robotics-textbook/labs/module-04/mini-project-02-advanced-vla/solution/vla_advanced_pipeline.py
  - physical-ai-robotics-textbook/labs/module-04/mini-project-02-advanced-vla/solution/vision_processor.py
  - physical-ai-robotics-textbook/labs/module-04/mini-project-02-advanced-vla/solution/cognitive_planner.py
  - physical-ai-robotics-textbook/labs/module-04/mini-project-02-advanced-vla/solution/safety_monitor.py
  - specs/001-physical-ai-robotics-book/tasks-module-04.md
tests:
  - npm run build (Docusaurus build verification)
---

## Prompt

now check implement for book Physical AI & Humanoid Robotics module-4 in physical-ai-robotics-textbook folder and do remaining implement ensure labs and Mini-Projects in side bar of Labs

## Response snapshot

Completed implementation of Module 4 VLA mini-projects and Labs sidebar integration:

1. **Added Module 4 Labs to sidebarsLabs.ts** - Created new sidebar category for Module 4 Labs containing Mini-Projects subcategory with Simple VLA System and Advanced VLA System entries.

2. **Created Mini-Project 1 (Simple VLA System) starter files:**
   - vla_pipeline.py - Main orchestrator with TODO stubs
   - speech_recognizer.py - Speech recognition with TODO stubs
   - action_executor.py - ROS 2 action execution with TODO stubs

3. **Created Mini-Project 1 solution files:**
   - Complete implementations of all three modules

4. **Created Mini-Project 2 (Advanced VLA System) starter files:**
   - vla_advanced_pipeline.py - Advanced pipeline with TODO stubs
   - vision_processor.py - Object detection with TODO stubs
   - cognitive_planner.py - LLM-based planning with TODO stubs
   - safety_monitor.py - Safety monitoring with TODO stubs

5. **Created Mini-Project 2 solution files:**
   - Complete implementations of all four modules

6. **Fixed lesson-03-vla-integration.mdx:**
   - Added QuizComponent import
   - Replaced text-based quiz with proper QuizComponent props (10 questions)

7. **Verified Docusaurus build succeeds**

## Outcome

- Impact: Module 4 mini-projects and labs are now fully navigable in the sidebar with complete starter/solution code for both projects
- Tests: npm run build PASS
- Files: 18 files created/modified
- Next prompts: Run validation scripts, verify navigation works in dev server
- Reflection: The QuizComponent required proper props format (questions array), not child text content

## Evaluation notes (flywheel)

- Failure modes observed: Initial build failed due to missing QuizComponent import, then failed again due to incorrect QuizComponent usage (needed questions prop, not children)
- Graders run and results (PASS/FAIL): npm run build PASS
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): Test local dev server to verify sidebar navigation works correctly
