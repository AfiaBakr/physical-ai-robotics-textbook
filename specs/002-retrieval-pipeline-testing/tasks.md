# Tasks: Retrieval Pipeline Testing

**Input**: Design documents from `/specs/002-retrieval-pipeline-testing/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Tests**: Tests are MANDATORY per constitution's Test-Driven Development (TDD) principle. Write tests FIRST, ensure they FAIL, then implement.

**Organization**: Tasks grouped by user story for independent implementation and testing.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (US1, US2, US3, US4)
- Include exact file paths in descriptions

## Path Conventions

Based on plan.md structure:
- **Backend code**: `backend/main.py`
- **Unit tests**: `tests/unit/test_retrieval.py`
- **Integration tests**: `tests/integration/test_retrieval_pipeline.py`

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and test structure

- [x] T001 Verify Qdrant collection exists and has vectors by running collection check in backend/main.py
- [x] T002 [P] Create tests/unit/ directory structure if not exists
- [x] T003 [P] Create tests/integration/ directory structure if not exists
- [x] T004 [P] Add pytest to backend/requirements.txt if not present
- [x] T005 Install test dependencies with `cd backend && uv pip install pytest`

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core retrieval infrastructure that ALL user stories depend on

**CRITICAL**: No user story work can begin until this phase is complete

- [x] T006 Implement `embed_query(query: str) -> List[float]` function in backend/main.py with Cohere search_query input_type
- [x] T007 Implement `search_qdrant(query_embedding: List[float], k: int = 5) -> List[ScoredPoint]` function in backend/main.py
- [x] T008 Implement `format_results(results: List[ScoredPoint], query: str, k: int) -> Dict[str, Any]` function in backend/main.py
- [x] T009 Implement `retrieve(query: str, k: int = 5) -> Dict[str, Any]` orchestrator function in backend/main.py

**Checkpoint**: Foundation ready - core retrieval functions implemented, user story testing can begin

---

## Phase 3: User Story 1 - Query Qdrant for Top-K Matches (Priority: P1) MVP

**Goal**: Submit a query and receive the top-K most relevant document chunks ranked by relevance score

**Independent Test**: Submit a known query and verify returned chunks are semantically relevant with correct count and ordering

### Tests for User Story 1 (MANDATORY)

> **NOTE: Write these tests FIRST, ensure they FAIL before implementation**

- [x] T010 [P] [US1] Create unit test file tests/unit/test_retrieval.py with test fixtures
- [x] T011 [P] [US1] Write test_embed_query_returns_768_dim_vector in tests/unit/test_retrieval.py
- [x] T012 [P] [US1] Write test_search_qdrant_returns_k_results in tests/unit/test_retrieval.py
- [x] T013 [P] [US1] Write test_search_qdrant_results_ordered_by_score in tests/unit/test_retrieval.py
- [x] T014 [US1] Write test_retrieve_returns_top_k_matches in tests/integration/test_retrieval_pipeline.py

### Implementation for User Story 1

- [x] T015 [US1] Add input validation to embed_query: reject empty query, validate max length in backend/main.py
- [x] T016 [US1] Add score range validation (0-1) to search results in backend/main.py
- [x] T017 [US1] Ensure results ordered by score descending in search_qdrant in backend/main.py
- [x] T018 [US1] Handle case when K exceeds available vectors (return all available) in backend/main.py
- [x] T019 [US1] Run tests and verify all US1 tests pass

**Checkpoint**: User Story 1 complete - Top-K retrieval working with correct ordering

---

## Phase 4: User Story 2 - Verify Retrieved Chunks Match Original Text (Priority: P1)

**Goal**: Verify that retrieved chunks contain the exact original text content (data integrity)

**Independent Test**: Compare retrieved chunk text against known stored text character-for-character

### Tests for User Story 2 (MANDATORY)

- [x] T020 [P] [US2] Write test_chunk_text_matches_stored_content in tests/integration/test_retrieval_pipeline.py
- [x] T021 [P] [US2] Write test_special_characters_preserved in tests/integration/test_retrieval_pipeline.py
- [x] T022 [P] [US2] Write test_unicode_text_integrity in tests/integration/test_retrieval_pipeline.py

### Implementation for User Story 2

- [x] T023 [US2] Verify text_content payload field extracted correctly in format_results in backend/main.py
- [x] T024 [US2] Add text integrity assertion in format_results (no truncation, no modification) in backend/main.py
- [x] T025 [US2] Run tests and verify all US2 tests pass

**Checkpoint**: User Story 2 complete - Text integrity verified, chunk text matches stored content

---

## Phase 5: User Story 3 - Metadata Return Verification (Priority: P2)

**Goal**: Verify retrieved chunks include correct metadata (url, chunk_id) for source attribution

**Independent Test**: Retrieve a chunk and verify url and chunk_id fields are present and accurate

### Tests for User Story 3 (MANDATORY)

- [x] T026 [P] [US3] Write test_url_metadata_returned in tests/integration/test_retrieval_pipeline.py
- [x] T027 [P] [US3] Write test_chunk_id_unique_per_result in tests/integration/test_retrieval_pipeline.py
- [x] T028 [P] [US3] Write test_multiple_chunks_same_url_different_ids in tests/integration/test_retrieval_pipeline.py

### Implementation for User Story 3

- [x] T029 [US3] Extract source_url to url field in format_results in backend/main.py
- [x] T030 [US3] Generate unique chunk_id from point.id and chunk_index in format_results in backend/main.py
- [x] T031 [US3] Validate all required metadata fields present before returning in backend/main.py
- [x] T032 [US3] Run tests and verify all US3 tests pass

**Checkpoint**: User Story 3 complete - Metadata (url, chunk_id) verified

---

## Phase 6: User Story 4 - End-to-End Pipeline Test with JSON Output (Priority: P2)

**Goal**: Run complete end-to-end test with clean JSON output matching schema

**Independent Test**: Run full query and validate JSON structure against QueryResponse/ErrorResponse schemas

### Tests for User Story 4 (MANDATORY)

- [x] T033 [P] [US4] Write test_json_output_matches_schema in tests/integration/test_retrieval_pipeline.py
- [x] T034 [P] [US4] Write test_empty_query_returns_error_json in tests/integration/test_retrieval_pipeline.py
- [x] T035 [P] [US4] Write test_no_matches_returns_empty_results in tests/integration/test_retrieval_pipeline.py
- [x] T036 [P] [US4] Write test_response_within_timeout in tests/integration/test_retrieval_pipeline.py

### Implementation for User Story 4

- [x] T037 [US4] Add timestamp field to QueryResponse in format_results in backend/main.py
- [x] T038 [US4] Implement ErrorResponse format for validation errors in retrieve in backend/main.py
- [x] T039 [US4] Add try-catch for Cohere/Qdrant failures returning SERVICE_UNAVAILABLE in retrieve in backend/main.py
- [x] T040 [US4] Ensure empty results returns success with empty array (not error) in retrieve in backend/main.py
- [x] T041 [US4] Run tests and verify all US4 tests pass
- [x] T042 [US4] Run full test suite: `cd backend && uv run pytest tests/ -v`

**Checkpoint**: User Story 4 complete - End-to-end JSON output verified

---

## Phase 7: Polish & Cross-Cutting Concerns

**Purpose**: Improvements affecting multiple user stories

- [x] T043 [P] Add docstrings to all new functions in backend/main.py per api-contract.md
- [x] T044 [P] Add logging for retrieval operations in backend/main.py
- [x] T045 Run quickstart.md verification checklist
- [x] T046 [P] Update backend/requirements.txt with final dependencies
- [x] T047 Final test run and verify 100% pass rate

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3-6)**: All depend on Foundational phase completion
  - US1 and US2 are both P1 - complete in order or parallel
  - US3 and US4 are both P2 - complete after P1 stories
- **Polish (Phase 7)**: Depends on all user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational - No dependencies on other stories
- **User Story 2 (P1)**: Can start after Foundational - Uses same functions as US1, no blocking dependency
- **User Story 3 (P2)**: Can start after Foundational - Independent metadata verification
- **User Story 4 (P2)**: Can start after Foundational - Tests full pipeline including error handling

### Within Each User Story

- Tests MUST be written and FAIL before implementation
- Implementation follows test requirements
- Verify tests pass before marking story complete
- Commit after each task or logical group

### Parallel Opportunities

- Setup tasks T002, T003, T004 can run in parallel
- All tests for each user story marked [P] can run in parallel
- US1 and US2 (both P1) can be developed in parallel after Foundational
- US3 and US4 (both P2) can be developed in parallel after Foundational
- Polish tasks marked [P] can run in parallel

---

## Parallel Example: User Story 1

```bash
# Launch all tests for User Story 1 together:
Task: "Write test_embed_query_returns_768_dim_vector in tests/unit/test_retrieval.py"
Task: "Write test_search_qdrant_returns_k_results in tests/unit/test_retrieval.py"
Task: "Write test_search_qdrant_results_ordered_by_score in tests/unit/test_retrieval.py"
```

## Parallel Example: User Story 4

```bash
# Launch all tests for User Story 4 together:
Task: "Write test_json_output_matches_schema in tests/integration/test_retrieval_pipeline.py"
Task: "Write test_empty_query_returns_error_json in tests/integration/test_retrieval_pipeline.py"
Task: "Write test_no_matches_returns_empty_results in tests/integration/test_retrieval_pipeline.py"
Task: "Write test_response_within_timeout in tests/integration/test_retrieval_pipeline.py"
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL - implements core functions)
3. Complete Phase 3: User Story 1 (Top-K retrieval)
4. **STOP and VALIDATE**: Test User Story 1 independently
5. Demo retrieval functionality

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 → Test independently → Core retrieval working
3. Add User Story 2 → Test independently → Data integrity verified
4. Add User Story 3 → Test independently → Metadata verified
5. Add User Story 4 → Test independently → Full pipeline with JSON validated
6. Each story adds confidence without breaking previous stories

### Single Developer Strategy

1. Complete Setup (T001-T005)
2. Complete Foundational (T006-T009) - Core implementation
3. User Story 1 (T010-T019) - TDD for Top-K
4. User Story 2 (T020-T025) - TDD for text integrity
5. User Story 3 (T026-T032) - TDD for metadata
6. User Story 4 (T033-T042) - TDD for JSON schema
7. Polish (T043-T047) - Documentation and final validation

---

## Summary

| Phase | Tasks | User Story | Independent Test |
|-------|-------|------------|------------------|
| Setup | T001-T005 | - | - |
| Foundational | T006-T009 | - | - |
| US1 (P1) | T010-T019 | Top-K Matches | Submit query, verify K results ordered by score |
| US2 (P1) | T020-T025 | Text Integrity | Compare chunk_text to stored content |
| US3 (P2) | T026-T032 | Metadata | Verify url, chunk_id present and accurate |
| US4 (P2) | T033-T042 | JSON Output | Validate full response against schema |
| Polish | T043-T047 | - | - |

**Total Tasks**: 47
**Parallel Opportunities**: 20 tasks marked [P]
**Suggested MVP**: Complete through User Story 1 (T019)

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Verify tests fail before implementing
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- All functions extend existing backend/main.py from spec-001
