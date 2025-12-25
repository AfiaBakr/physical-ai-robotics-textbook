# Tasks: Frontend ↔ Backend Integration for RAG Book Chatbot

**Input**: Design documents from `/specs/005-frontend-rag-integration/`
**Prerequisites**: plan.md, spec.md, research.md, data-model.md, contracts/api-client.ts

**Tests**: Tests are included following the TDD principle from the constitution. Write tests FIRST, ensure they FAIL, then implement.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story?] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3, US4)
- Include exact file paths in descriptions

## Path Conventions

All paths are relative to `physical-ai-robotics-textbook/` (the Docusaurus frontend):
- Source code: `src/`
- Tests: `src/__tests__/` (co-located) or project root `tests/frontend/`

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and directory structure

- [x] T001 Create directory structure for ChatWidget in physical-ai-robotics-textbook/src/components/ChatWidget/
- [x] T002 [P] Create directory structure for services in physical-ai-robotics-textbook/src/services/
- [x] T003 [P] Create directory structure for hooks in physical-ai-robotics-textbook/src/hooks/
- [x] T004 [P] Create directory structure for types in physical-ai-robotics-textbook/src/types/
- [x] T005 [P] Create directory structure for theme in physical-ai-robotics-textbook/src/theme/
- [x] T006 Copy TypeScript type definitions from specs/005-frontend-rag-integration/contracts/api-client.ts to physical-ai-robotics-textbook/src/types/chat.ts

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

### Tests for Foundational (TDD) ⚠️

- [ ] T007 [P] Write unit tests for ragApi.ts in physical-ai-robotics-textbook/src/services/__tests__/ragApi.test.ts (test successful request, network error, timeout, validation)
- [ ] T008 [P] Write unit tests for useChatSession hook in physical-ai-robotics-textbook/src/hooks/__tests__/useChatSession.test.ts (test state management, sessionStorage sync)

### Implementation for Foundational

- [x] T009 Implement RAG API client with fetch in physical-ai-robotics-textbook/src/services/ragApi.ts (POST /ask, timeout, error handling)
- [x] T010 Implement useChatSession hook in physical-ai-robotics-textbook/src/hooks/useChatSession.ts (state management, sessionStorage persistence)
- [x] T011 Add CORS middleware configuration documentation for backend in specs/005-frontend-rag-integration/quickstart.md

**Checkpoint**: Foundation ready - user story implementation can now begin

---

## Phase 3: User Story 1 - Ask a Question About Book Content (Priority: P1) 🎯 MVP

**Goal**: Reader can open chat, type a question, submit it, see loading indicator, and receive answer with source links

**Independent Test**: Open chat interface, type "What is RAG?", verify answer and source links display

### Tests for User Story 1 (TDD) ⚠️

- [ ] T012 [P] [US1] Write unit tests for ChatInput component in physical-ai-robotics-textbook/src/components/ChatWidget/__tests__/ChatInput.test.tsx (validation, submit, character count)
- [ ] T013 [P] [US1] Write unit tests for ChatMessage component in physical-ai-robotics-textbook/src/components/ChatWidget/__tests__/ChatMessage.test.tsx (display user/assistant messages)
- [ ] T014 [P] [US1] Write unit tests for SourceLinks component in physical-ai-robotics-textbook/src/components/ChatWidget/__tests__/SourceLinks.test.tsx (render links, open in new tab)
- [ ] T015 [P] [US1] Write integration test for ChatWidget in physical-ai-robotics-textbook/src/components/ChatWidget/__tests__/ChatWidget.integration.test.tsx (full message flow)

### Implementation for User Story 1

- [x] T016 [P] [US1] Create ChatInput component with validation in physical-ai-robotics-textbook/src/components/ChatWidget/ChatInput.tsx (input field, submit button, character limit)
- [x] T017 [P] [US1] Create ChatMessage component in physical-ai-robotics-textbook/src/components/ChatWidget/ChatMessage.tsx (display role, content, timestamp)
- [x] T018 [P] [US1] Create SourceLinks component in physical-ai-robotics-textbook/src/components/ChatWidget/SourceLinks.tsx (clickable links, open in new tab)
- [x] T019 [US1] Create ChatPanel component in physical-ai-robotics-textbook/src/components/ChatWidget/ChatPanel.tsx (message list, input area, loading state)
- [x] T020 [US1] Create main ChatWidget container in physical-ai-robotics-textbook/src/components/ChatWidget/index.tsx (floating button, toggle panel)
- [x] T021 [US1] Create CSS module for ChatWidget in physical-ai-robotics-textbook/src/components/ChatWidget/styles.module.css (floating button, panel layout, basic styles)
- [x] T022 [US1] Create Root theme wrapper in physical-ai-robotics-textbook/src/theme/Root.tsx (inject ChatWidget globally)
- [x] T023 [US1] Export ChatWidget from components index in physical-ai-robotics-textbook/src/components/ChatWidget/index.tsx

**Checkpoint**: User Story 1 complete - Reader can ask questions and receive answers with sources

---

## Phase 4: User Story 2 - View Context Snippets (Priority: P2)

**Goal**: Reader can view matched content snippets that informed the answer, with relevance scores

**Independent Test**: Ask a question, verify matched chunks are visible/expandable with text and relevance indicator

### Tests for User Story 2 (TDD) ⚠️

- [ ] T024 [P] [US2] Write unit tests for MatchedChunks component in physical-ai-robotics-textbook/src/components/ChatWidget/__tests__/MatchedChunks.test.tsx (render chunks, expand/collapse, relevance score)

### Implementation for User Story 2

- [x] T025 [US2] Create MatchedChunks component in physical-ai-robotics-textbook/src/components/ChatWidget/MatchedChunks.tsx (expandable snippets, relevance indicator)
- [x] T026 [US2] Integrate MatchedChunks into ChatMessage in physical-ai-robotics-textbook/src/components/ChatWidget/ChatMessage.tsx (add expand section)
- [x] T027 [US2] Add CSS styles for MatchedChunks in physical-ai-robotics-textbook/src/components/ChatWidget/styles.module.css (expandable section, relevance bar)

**Checkpoint**: User Story 2 complete - Reader can view context snippets with relevance scores

---

## Phase 5: User Story 3 - Handle Errors Gracefully (Priority: P2)

**Goal**: Reader sees friendly error messages when backend is unavailable and can retry

**Independent Test**: Stop backend server, submit a question, verify error message and retry button appear

### Tests for User Story 3 (TDD) ⚠️

- [ ] T028 [P] [US3] Write unit tests for error states in physical-ai-robotics-textbook/src/components/ChatWidget/__tests__/ChatPanel.test.tsx (error display, retry button)
- [ ] T029 [P] [US3] Write integration test for error handling in physical-ai-robotics-textbook/src/components/ChatWidget/__tests__/ChatWidget.error.test.tsx (network error, timeout, server error)

### Implementation for User Story 3

- [x] T030 [US3] Add error state component to ChatPanel in physical-ai-robotics-textbook/src/components/ChatWidget/ChatPanel.tsx (error message, retry button)
- [x] T031 [US3] Implement retry functionality in useChatSession hook in physical-ai-robotics-textbook/src/hooks/useChatSession.ts (store lastQuery, retry action)
- [x] T032 [US3] Add CSS styles for error state in physical-ai-robotics-textbook/src/components/ChatWidget/styles.module.css (error banner, retry button)

**Checkpoint**: User Story 3 complete - Errors are handled gracefully with retry option

---

## Phase 6: User Story 4 - Maintain Conversation Context (Priority: P3)

**Goal**: Chat history persists within browser session across page navigations

**Independent Test**: Ask 3+ questions, navigate to different page, return, verify all history is preserved

### Tests for User Story 4 (TDD) ⚠️

- [ ] T033 [P] [US4] Write unit tests for session persistence in physical-ai-robotics-textbook/src/hooks/__tests__/useChatSession.persistence.test.ts (save to sessionStorage, restore on mount, clear on new session)

### Implementation for User Story 4

- [x] T034 [US4] Enhance useChatSession to persist messages in physical-ai-robotics-textbook/src/hooks/useChatSession.ts (sync to sessionStorage on change)
- [x] T035 [US4] Add message history restoration on mount in physical-ai-robotics-textbook/src/hooks/useChatSession.ts (load from sessionStorage)
- [x] T036 [US4] Verify history survives page navigation in physical-ai-robotics-textbook/src/components/ChatWidget/index.tsx (context preservation)

**Checkpoint**: User Story 4 complete - Chat history persists within session

---

## Phase 7: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [x] T037 [P] Add responsive CSS for mobile (320px minimum) in physical-ai-robotics-textbook/src/components/ChatWidget/styles.module.css
- [x] T038 [P] Add keyboard accessibility (Tab navigation, Enter to submit, Escape to close) in physical-ai-robotics-textbook/src/components/ChatWidget/index.tsx
- [x] T039 [P] Add ARIA labels and live regions in physical-ai-robotics-textbook/src/components/ChatWidget/ChatPanel.tsx
- [x] T040 [P] Add dark mode support using Docusaurus theme variables in physical-ai-robotics-textbook/src/components/ChatWidget/styles.module.css
- [ ] T041 Run quickstart.md validation (start backend, start frontend, test full flow)
- [ ] T042 Update quickstart.md with final setup instructions in specs/005-frontend-rag-integration/quickstart.md

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup (T001-T006) - BLOCKS all user stories
- **User Story 1 (Phase 3)**: Depends on Foundational (T007-T011)
- **User Story 2 (Phase 4)**: Depends on Foundational; enhances US1 components
- **User Story 3 (Phase 5)**: Depends on Foundational; enhances US1 components
- **User Story 4 (Phase 6)**: Depends on Foundational; enhances useChatSession hook
- **Polish (Phase 7)**: Depends on all user stories being complete

### User Story Dependencies

| User Story | Can Start After | Dependencies on Other Stories |
|------------|-----------------|------------------------------|
| US1 (P1)   | Phase 2 complete | None - fully independent |
| US2 (P2)   | Phase 2 complete | Enhances ChatMessage (US1), but testable independently |
| US3 (P2)   | Phase 2 complete | Enhances ChatPanel (US1), but testable independently |
| US4 (P3)   | Phase 2 complete | Enhances useChatSession, but testable independently |

### Within Each User Story

1. Tests MUST be written and FAIL before implementation
2. Components marked [P] can be built in parallel
3. Integration/container components depend on child components
4. Commit after each task or logical group

### Parallel Opportunities

**Phase 1 (all parallel)**:
- T001, T002, T003, T004, T005 - different directories

**Phase 2 (tests parallel, then implementation)**:
- T007, T008 - different test files
- T009, T010 - different source files

**Phase 3 - User Story 1 (tests parallel, components parallel)**:
- T012, T013, T014, T015 - different test files
- T016, T017, T018 - different component files

**Phase 4-6 (tests first, then implementation)**:
- Each phase has parallel test opportunities

---

## Parallel Example: User Story 1

```bash
# Step 1: Launch all tests for User Story 1 together (they should all fail initially):
Task T012: "Write unit tests for ChatInput component"
Task T013: "Write unit tests for ChatMessage component"
Task T014: "Write unit tests for SourceLinks component"
Task T015: "Write integration test for ChatWidget"

# Step 2: Implement parallel components:
Task T016: "Create ChatInput component"
Task T017: "Create ChatMessage component"
Task T018: "Create SourceLinks component"

# Step 3: Implement container (depends on above):
Task T019: "Create ChatPanel component"
Task T020: "Create main ChatWidget container"

# Step 4: Finalize:
Task T021: "Create CSS module"
Task T022: "Create Root theme wrapper"
Task T023: "Export ChatWidget"
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup (T001-T006)
2. Complete Phase 2: Foundational (T007-T011) - **CRITICAL**
3. Complete Phase 3: User Story 1 (T012-T023)
4. **STOP and VALIDATE**: Test US1 independently
5. Deploy/demo if ready - basic Q&A is functional

### Incremental Delivery

| Milestone | Tasks | Deliverable |
|-----------|-------|-------------|
| Foundation | T001-T011 | API client + state management ready |
| MVP | T012-T023 | Basic Q&A with sources (US1) |
| Enhanced | T024-T027 | Context snippets visible (US2) |
| Robust | T028-T032 | Error handling + retry (US3) |
| Complete | T033-T036 | Session persistence (US4) |
| Polished | T037-T042 | Mobile, a11y, dark mode |

### Task Summary

| Phase | User Story | Task Count | Parallel Tasks |
|-------|------------|------------|----------------|
| 1 - Setup | - | 6 | 5 |
| 2 - Foundational | - | 5 | 2 |
| 3 - US1 MVP | Ask Questions | 12 | 7 |
| 4 - US2 | Context Snippets | 4 | 1 |
| 5 - US3 | Error Handling | 5 | 2 |
| 6 - US4 | Session History | 4 | 1 |
| 7 - Polish | Cross-cutting | 6 | 4 |
| **Total** | | **42** | **22** |

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Verify tests fail before implementing (TDD Red-Green-Refactor)
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- Base path: `physical-ai-robotics-textbook/` (Docusaurus frontend)

