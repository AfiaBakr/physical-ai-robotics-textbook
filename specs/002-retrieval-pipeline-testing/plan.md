# Implementation Plan: Retrieval Pipeline Testing

**Branch**: `002-retrieval-pipeline-testing` | **Date**: 2025-12-22 | **Spec**: [spec.md](./spec.md)
**Input**: Feature specification from `/specs/002-retrieval-pipeline-testing/spec.md`

**Note**: This template is filled in by the `/sp.plan` command. See `.specify/templates/commands/plan.md` for the execution workflow.

## Summary

A Python-based retrieval testing pipeline that queries the existing Qdrant vector database (populated by spec-001), generates query embeddings using Cohere, performs Top-K similarity search, and returns results in clean JSON format. The implementation extends the existing `main.py` with retrieval functions for validating the RAG ingestion pipeline.

## Technical Context

**Language/Version**: Python 3.11
**Primary Dependencies**: uv (package manager), cohere (embedding service), qdrant-client (vector database), pytest (testing)
**Storage**: Qdrant vector database (existing `rag_embeddings` collection from spec-001)
**Embedding Service**: Cohere API (same `multilingual-22-12` model as spec-001)
**Testing**: pytest (for unit/integration tests)
**Target Platform**: Backend/single-project - retrieval-only pipeline
**Project Type**: Backend/single-project - extends existing embedding pipeline
**Performance Goals**: Query response time < 2 seconds for up to 100,000 vectors
**Constraints**: <2s p95 latency, handle Qdrant/Cohere failures gracefully, memory-efficient
**Scale/Scope**: Same scale as spec-001 (up to 10,000 pages), configurable Top-K (1-100)

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

- **I. Spec-Driven Development (SDD)**: ✅ Feature specification exists and clearly defines requirements
- **II. Test-Driven Development (TDD)**: ✅ Will implement with TDD approach using pytest
- **III. Simple, Composable Libraries**: ⚠️ Extends single main.py file - justified by continuity with spec-001 approach
- **IV. Clear and Versioned APIs**: ✅ API contracts defined in contracts/api-contract.md

**Post-Design Assessment**: The single-file approach continues from spec-001 per user's established pattern. The API contract document addresses clear interfaces. Test-driven development will be followed during implementation.

## Project Structure

### Documentation (this feature)

```text
specs/002-retrieval-pipeline-testing/
├── plan.md              # This file (/sp.plan command output)
├── research.md          # Phase 0 output (/sp.plan command)
├── data-model.md        # Phase 1 output (/sp.plan command)
├── quickstart.md        # Phase 1 output (/sp.plan command)
├── contracts/           # Phase 1 output (/sp.plan command)
│   └── api-contract.md  # Function interface definitions
└── tasks.md             # Phase 2 output (/sp.tasks command - NOT created by /sp.plan)
```

### Source Code (repository root)

```text
backend/
├── main.py              # Extended with retrieval functions
├── requirements.txt     # Python dependencies (add pytest)
└── .env                 # Environment variables

tests/
├── unit/
│   └── test_retrieval.py        # Unit tests for retrieval functions
└── integration/
    └── test_retrieval_pipeline.py # End-to-end pipeline tests
```

**Structure Decision**: Extends existing `backend/main.py` from spec-001 with new retrieval functions. Test files created under `tests/` following spec-001 structure.

## Complexity Tracking

> **Fill ONLY if Constitution Check has violations that must be justified**

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
| Single main.py file | Continuity with spec-001 user requirement | Modular approach would break established pattern |

## Architecture Alignment

Based on user input and spec-001 analysis:

### Pipeline Flow

```
┌─────────────────────────────────────────────────────────────────┐
│                    Retrieval Pipeline                           │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  Input: Query String                                            │
│     │                                                           │
│     ▼                                                           │
│  ┌─────────────────┐                                           │
│  │  Validate Input │ ──── Empty? ──► ErrorResponse             │
│  └─────────────────┘                                           │
│     │                                                           │
│     ▼                                                           │
│  ┌─────────────────┐       ┌──────────────┐                    │
│  │  embed_query()  │ ◄────►│  Cohere API  │                    │
│  └─────────────────┘       │ (search_query)│                    │
│     │                      └──────────────┘                    │
│     ▼ (768-dim vector)                                         │
│  ┌─────────────────┐       ┌──────────────┐                    │
│  │ search_qdrant() │ ◄────►│   Qdrant     │                    │
│  └─────────────────┘       │ (rag_embeddings)                  │
│     │                      └──────────────┘                    │
│     ▼ (List[ScoredPoint])                                      │
│  ┌─────────────────┐                                           │
│  │ format_results()│                                           │
│  └─────────────────┘                                           │
│     │                                                           │
│     ▼                                                           │
│  Output: JSON Response                                          │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### Functions to Implement

| Function | Purpose | Dependencies |
|----------|---------|--------------|
| `embed_query(query)` | Generate 768-dim query embedding | Cohere API |
| `search_qdrant(embedding, k)` | Top-K similarity search | Qdrant client |
| `format_results(results, query, k)` | Format JSON output | None |
| `retrieve(query, k=5)` | Orchestrator function | All above |

### Payload Field Mapping

| Stored (spec-001) | Retrieved (spec-002) |
|-------------------|----------------------|
| text_content | chunk_text |
| source_url | url |
| point.id + chunk_index | chunk_id |
| (computed) | relevance_score |

## Validation Strategy

### 1. Semantic Relevance
- Query returns semantically related chunks
- Top result has highest relevance score
- Results ordered by score descending

### 2. Text Integrity
- `chunk_text` exactly matches stored `text_content`
- No truncation or corruption
- Special characters preserved

### 3. Metadata Accuracy
- `url` matches stored `source_url`
- `chunk_id` is unique and traceable
- All required fields present

### 4. JSON Schema Consistency
- Valid JSON for all responses
- Schema matches contract definition
- Error responses follow error schema

## Testing Strategy

### Test Categories

| Test | Type | Purpose |
|------|------|---------|
| test_embed_query | Unit | Validate query embedding |
| test_search_qdrant | Unit | Validate search function |
| test_format_results | Unit | Validate JSON formatting |
| test_happy_path | Integration | Full pipeline success |
| test_known_query | Integration | Expected chunk verification |
| test_empty_query | Integration | Error handling |
| test_no_matches | Integration | Empty results handling |
| test_text_integrity | Validation | Chunk text matches stored |
| test_metadata_accuracy | Validation | URL/chunk_id correct |

### Test Fixtures

```python
# Known query that should return specific results
KNOWN_QUERY = "What is a digital twin?"
EXPECTED_URL_PATTERN = "physical-ai-robotics"

# Empty collection scenario (mock)
EMPTY_COLLECTION = []
```

## Error Handling

| Scenario | Response |
|----------|----------|
| Empty query | `{"error": "Query cannot be empty", "code": "INVALID_INPUT"}` |
| Query too long | `{"error": "Query exceeds maximum length", "code": "INVALID_INPUT"}` |
| Invalid k | `{"error": "k must be positive integer", "code": "INVALID_INPUT"}` |
| No matches | `{"query": "...", "results": [], "total_results": 0}` (success) |
| Cohere failure | `{"error": "Embedding service unavailable", "code": "SERVICE_UNAVAILABLE"}` |
| Qdrant failure | `{"error": "Database service unavailable", "code": "SERVICE_UNAVAILABLE"}` |

## Deliverables

| Deliverable | Location | Description |
|-------------|----------|-------------|
| Retrieval functions | `backend/main.py` | embed_query, search_qdrant, format_results, retrieve |
| Unit tests | `tests/unit/test_retrieval.py` | Function-level tests |
| Integration tests | `tests/integration/test_retrieval_pipeline.py` | End-to-end tests |
| Sample input/output | `contracts/api-contract.md` | JSON examples |
| Verification checklist | `quickstart.md` | Manual verification steps |

## Next Steps

1. Run `/sp.tasks` to generate implementation tasks
2. Implement retrieval functions using TDD
3. Run test suite and verify all pass
4. Document any issues or deviations

## Related Documents

- [spec.md](./spec.md) - Feature specification
- [research.md](./research.md) - Technical research
- [data-model.md](./data-model.md) - Entity definitions
- [contracts/api-contract.md](./contracts/api-contract.md) - Function interfaces
- [quickstart.md](./quickstart.md) - Developer guide
