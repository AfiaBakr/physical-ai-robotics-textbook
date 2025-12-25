# Tasks: RAG Agent with Retrieval Integration

**Input**: Design documents from `/specs/003-rag-agent/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Tests**: Tests are MANDATORY as per the constitution's Test-Driven Development (TDD) principle.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Backend**: `backend/` at repository root (extending existing structure)
- **Tests**: `tests/` at repository root

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and dependencies for FastAPI + OpenAI integration

- [x] T001 Install new dependencies: `pip install fastapi uvicorn openai httpx pytest-asyncio`
- [x] T002 [P] Update `.env` file with OPENAI_API_KEY placeholder
- [x] T003 [P] Create backend/models.py with Pydantic model stubs
- [x] T004 [P] Create backend/agent.py with OpenAI client initialization stub
- [x] T005 Create backend/api.py with FastAPI app initialization

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**CRITICAL**: No user story work can begin until this phase is complete

- [x] T006 Implement AskRequest Pydantic model in backend/models.py
- [x] T007 [P] Implement AskResponse Pydantic model in backend/models.py
- [x] T008 [P] Implement MatchedChunk Pydantic model in backend/models.py
- [x] T009 [P] Implement ErrorResponse Pydantic model in backend/models.py
- [x] T010 Implement context assembly function in backend/agent.py (builds context from retrieval results)
- [x] T011 Implement generate_answer function in backend/agent.py (calls OpenAI with context)
- [x] T012 Add /health endpoint in backend/api.py for service health checks
- [x] T013 [P] Create tests/contract/__init__.py and tests/integration/__init__.py directories

**Checkpoint**: Foundation ready - user story implementation can now begin

---

## Phase 3: User Story 1 - Submit Query and Receive Answer (Priority: P1) MVP

**Goal**: User submits a query and receives an answer with sources and matched chunks

**Independent Test**: POST to /ask with valid query returns JSON with answer, sources, matched_chunks

### Tests for User Story 1 (MANDATORY)

> **NOTE: Write these tests FIRST, ensure they FAIL before implementation**

- [x] T014 [P] [US1] Contract test for POST /ask success response in tests/contract/test_ask_endpoint.py
- [x] T015 [P] [US1] Contract test for AskResponse schema validation in tests/contract/test_ask_endpoint.py
- [x] T016 [P] [US1] Integration test for full RAG pipeline in tests/integration/test_api.py

### Implementation for User Story 1

- [x] T017 [US1] Implement /ask POST endpoint route in backend/api.py
- [x] T018 [US1] Add query validation (non-empty, max 1000 chars) in /ask endpoint
- [x] T019 [US1] Integrate retrieve() function from main.py in /ask endpoint
- [x] T020 [US1] Integrate context assembly from agent.py in /ask endpoint
- [x] T021 [US1] Integrate generate_answer from agent.py in /ask endpoint
- [x] T022 [US1] Format response as AskResponse (answer, sources, matched_chunks)
- [x] T023 [US1] Add request logging for /ask endpoint
- [x] T024 [US1] Verify tests pass for User Story 1

**Checkpoint**: User Story 1 fully functional - can submit queries and receive answers

---

## Phase 4: User Story 2 - Handle Missing Query (Priority: P2)

**Goal**: Return clear error when query is missing or empty

**Independent Test**: POST to /ask with empty/missing query returns 400 with INVALID_INPUT error

### Tests for User Story 2 (MANDATORY)

- [x] T025 [P] [US2] Contract test for empty query error in tests/contract/test_ask_endpoint.py
- [x] T026 [P] [US2] Contract test for missing query field error in tests/contract/test_ask_endpoint.py
- [x] T027 [P] [US2] Integration test for validation error flow in tests/integration/test_api.py

### Implementation for User Story 2

- [x] T028 [US2] Add HTTPException for empty query string in backend/api.py
- [x] T029 [US2] Add HTTPException for missing query field in backend/api.py
- [x] T030 [US2] Return ErrorResponse with code INVALID_INPUT for validation failures
- [x] T031 [US2] Log validation errors in /ask endpoint
- [x] T032 [US2] Verify tests pass for User Story 2

**Checkpoint**: User Story 2 complete - validation errors return proper 400 responses

---

## Phase 5: User Story 3 - Handle No Results Found (Priority: P2)

**Goal**: Return graceful message when no relevant documents match the query

**Independent Test**: POST to /ask with unrelated query returns 200 with "no results" message

### Tests for User Story 3 (MANDATORY)

- [x] T033 [P] [US3] Contract test for empty results response in tests/contract/test_ask_endpoint.py
- [x] T034 [P] [US3] Integration test for no-match query flow in tests/integration/test_api.py

### Implementation for User Story 3

- [x] T035 [US3] Detect empty retrieval results in /ask endpoint
- [x] T036 [US3] Generate graceful "no relevant information found" answer via OpenAI
- [x] T037 [US3] Return AskResponse with empty sources and matched_chunks arrays
- [x] T038 [US3] Log no-results queries for monitoring
- [x] T039 [US3] Verify tests pass for User Story 3

**Checkpoint**: User Story 3 complete - no results handled gracefully

---

## Phase 6: Edge Cases & Service Failures

**Purpose**: Handle service failures and edge cases identified in spec

### Tests for Edge Cases (MANDATORY)

- [x] T040 [P] Unit test for Cohere embedding failure handling in tests/unit/test_agent.py
- [x] T041 [P] Unit test for Qdrant connection failure handling in tests/unit/test_agent.py
- [x] T042 [P] Unit test for OpenAI generation failure handling in tests/unit/test_agent.py
- [x] T043 [P] Contract test for long query (>1000 chars) in tests/contract/test_ask_endpoint.py

### Implementation for Edge Cases

- [x] T044 Add try/except for Cohere API failures in /ask endpoint, return 500 SERVICE_UNAVAILABLE
- [x] T045 Add try/except for Qdrant connection failures in /ask endpoint, return 500 SERVICE_UNAVAILABLE
- [x] T046 Add try/except for OpenAI API failures in /ask endpoint, return 500 SERVICE_UNAVAILABLE
- [x] T047 Handle query length > 1000 chars with 400 INVALID_INPUT error
- [x] T048 Verify all edge case tests pass

**Checkpoint**: All error paths handled with appropriate error responses

---

## Phase 7: Polish & Cross-Cutting Concerns

**Purpose**: Final improvements and validation

- [x] T049 [P] Add docstrings to all public functions in backend/api.py
- [x] T050 [P] Add docstrings to all public functions in backend/agent.py
- [x] T051 [P] Add docstrings to all Pydantic models in backend/models.py
- [ ] T052 Run all tests and ensure 100% pass rate
- [ ] T053 Manual test using quickstart.md validation steps
- [ ] T054 Verify response time < 5 seconds (SC-001)

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3-5)**: All depend on Foundational phase completion
  - User stories can proceed in parallel (if staffed)
  - Or sequentially in priority order (P1 → P2 → P3)
- **Edge Cases (Phase 6)**: Depends on User Story 1 completion
- **Polish (Phase 7)**: Depends on all phases being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P2)**: Can start after Foundational (Phase 2) - Builds on /ask endpoint from US1
- **User Story 3 (P2)**: Can start after Foundational (Phase 2) - Builds on /ask endpoint from US1

### Within Each User Story

- Tests MUST be written and FAIL before implementation
- Models before services
- Services before endpoints
- Core implementation before integration
- Story complete before moving to next priority

### Parallel Opportunities

- Phase 1: T002, T003, T004 can run in parallel
- Phase 2: T007, T008, T009, T013 can run in parallel
- Phase 3: T014, T015, T016 can run in parallel (tests)
- Phase 4: T025, T026, T027 can run in parallel (tests)
- Phase 5: T033, T034 can run in parallel (tests)
- Phase 6: T040, T041, T042, T043 can run in parallel (tests)
- Phase 7: T049, T050, T051 can run in parallel (docstrings)

---

## Parallel Example: User Story 1 Tests

```bash
# Launch all tests for User Story 1 together:
Task: "Contract test for POST /ask success response in tests/contract/test_ask_endpoint.py"
Task: "Contract test for AskResponse schema validation in tests/contract/test_ask_endpoint.py"
Task: "Integration test for full RAG pipeline in tests/integration/test_api.py"
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3. Complete Phase 3: User Story 1
4. **STOP and VALIDATE**: Test User Story 1 independently
5. Deploy/demo if ready

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 → Test independently → Deploy/Demo (MVP!)
3. Add User Story 2 → Test independently → Deploy/Demo
4. Add User Story 3 → Test independently → Deploy/Demo
5. Add Edge Cases → Final hardening
6. Polish → Production ready

### Recommended Execution Order

```
T001 → T002-T005 (parallel) → T006 → T007-T009 (parallel) → T010-T013 →
T014-T016 (parallel tests) → T017-T024 (implementation) →
T025-T027 (parallel tests) → T028-T032 (implementation) →
T033-T034 (parallel tests) → T035-T039 (implementation) →
T040-T043 (parallel tests) → T044-T048 (implementation) →
T049-T051 (parallel docstrings) → T052-T054 (validation)
```

---

## Summary

| Phase | Task Count | Parallelizable | Story |
|-------|------------|----------------|-------|
| Phase 1: Setup | 5 | 4 | - |
| Phase 2: Foundational | 8 | 5 | - |
| Phase 3: User Story 1 | 11 | 3 | US1 (MVP) |
| Phase 4: User Story 2 | 8 | 3 | US2 |
| Phase 5: User Story 3 | 7 | 2 | US3 |
| Phase 6: Edge Cases | 9 | 4 | - |
| Phase 7: Polish | 6 | 3 | - |
| **Total** | **54** | **24** | |

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Verify tests fail before implementing
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
