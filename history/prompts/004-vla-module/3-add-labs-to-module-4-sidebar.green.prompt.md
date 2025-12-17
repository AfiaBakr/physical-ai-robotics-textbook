---
id: 3
title: Add Labs to Module 4 Sidebar
stage: green
date: 2025-12-17
surface: agent
model: claude-opus-4-5-20251101
feature: 004-vla-module
branch: 004-vla-module
user: architect
command: /sp.implement
labels: ["labs", "sidebar", "vla", "module-4", "docusaurus"]
links:
  spec: specs/004-vla-module/spec.md
  ticket: null
  adr: null
  pr: null
files:
  - physical-ai-robotics-textbook/sidebarsLabs.ts
  - physical-ai-robotics-textbook/labs/module-04/lab-01-speech-to-command/README.md
  - physical-ai-robotics-textbook/labs/module-04/lab-01-speech-to-command/starter/speech_to_command.py
  - physical-ai-robotics-textbook/labs/module-04/lab-01-speech-to-command/validate.py
  - physical-ai-robotics-textbook/labs/module-04/lab-02-llm-cognitive-planning/README.md
  - physical-ai-robotics-textbook/labs/module-04/lab-02-llm-cognitive-planning/starter/cognitive_planner.py
  - physical-ai-robotics-textbook/labs/module-04/lab-02-llm-cognitive-planning/validate.py
  - physical-ai-robotics-textbook/labs/module-04/lab-03-vla-pipeline-integration/README.md
  - physical-ai-robotics-textbook/labs/module-04/lab-03-vla-pipeline-integration/starter/vla_pipeline.py
  - physical-ai-robotics-textbook/labs/module-04/lab-03-vla-pipeline-integration/validate.py
tests:
  - N/A (content creation task)
---

## Prompt

add 3 labs in list in Lab side bar for book Physical AI & Humanoid Robotics module-4 in physical-ai-robotics-textbook folder.

## Response snapshot

Successfully added 3 labs to Module 4 (Vision-Language-Action) in the Labs sidebar:

1. **Lab 1: Speech to Command** - Converting spoken commands to structured robot tasks using Whisper ASR and natural language parsing
2. **Lab 2: LLM Cognitive Planning** - Task decomposition using Large Language Models for robot action planning
3. **Lab 3: VLA Pipeline Integration** - End-to-end integration of all VLA components (Vision, Language, Action)

Each lab includes:
- Comprehensive README.md with objectives, prerequisites, learning outcomes, and step-by-step instructions
- Starter Python files with TODOs for students to implement
- Validation scripts to verify completion

The labs align with the VLA module spec's user stories:
- Lab 1 covers US2 (Converting Spoken Commands to Robot Tasks)
- Lab 2 covers US3 (Cognitive Planning with LLMs)
- Lab 3 covers US6 (End-to-End Autonomous System)

## Outcome

- ✅ Impact: Added 3 complete labs with documentation and starter code for Module 4 VLA content
- 🧪 Tests: Validation scripts created for each lab
- 📁 Files: 10 files created/modified (1 sidebar config, 3 READMEs, 3 starter files, 3 validate files)
- 🔁 Next prompts: Consider adding solution files for each lab, creating mini-project connections
- 🧠 Reflection: Labs designed to progressively build VLA skills from components to integration

## Evaluation notes (flywheel)

- Failure modes observed: None - all files created successfully
- Graders run and results (PASS/FAIL): N/A - content creation
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): Add solution files for reference implementations
