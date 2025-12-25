# Implementation Plan: RAG Agent with Retrieval Integration

**Branch**: `003-rag-agent` | **Date**: 2025-12-22 | **Spec**: [spec.md](./spec.md)
**Input**: Feature specification from `/specs/003-rag-agent/spec.md`

## Summary

Build a FastAPI backend agent that accepts user queries via a `/ask` endpoint, embeds queries using Cohere, retrieves relevant context from Qdrant, and generates grounded responses using OpenAI Agent SDK. The implementation reuses the existing embedding and retrieval pipeline from Spec-001/002 while adding new FastAPI server and OpenAI generation layers.

## Technical Context

**Language/Version**: Python 3.11
**Primary Dependencies**: FastAPI, uvicorn, openai, cohere, qdrant-client, pydantic
**Storage**: Qdrant (read-only - collection already exists from Spec-001)
**Testing**: pytest, httpx (for async API testing)
**Target Platform**: Linux server / containerized deployment
**Project Type**: Backend API service
**Performance Goals**: Response time < 5 seconds (SC-001)
**Constraints**: Stateless API, environment-based configuration
**Scale/Scope**: Single endpoint, existing document corpus

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

| Principle | Status | Notes |
|-----------|--------|-------|
| I. Spec-Driven Development | PASS | spec.md defines requirements before implementation |
| II. Test-Driven Development | PENDING | Tests will be written before implementation in tasks |
| III. Simple, Composable Libraries | PASS | Reuses existing retrieval module, adds focused agent module |
| IV. Clear and Versioned APIs | PASS | OpenAPI contract defined in contracts/openapi.yaml |

## Project Structure

### Documentation (this feature)

```text
specs/003-rag-agent/
├── spec.md              # Feature specification
├── plan.md              # This file
├── research.md          # Phase 0 research decisions
├── data-model.md        # Entity definitions
├── quickstart.md        # Implementation quickstart
├── contracts/
│   └── openapi.yaml     # API contract
├── checklists/
│   └── requirements.md  # Spec quality checklist
└── tasks.md             # Phase 2 output (from /sp.tasks)
```

### Source Code (repository root)

```text
backend/
├── main.py              # EXISTING: Embedding & retrieval pipeline
├── api.py               # NEW: FastAPI application with /ask endpoint
├── agent.py             # NEW: OpenAI agent wrapper for generation
├── models.py            # NEW: Pydantic request/response models
└── test_sitemap.py      # EXISTING: Sitemap tests

tests/
├── unit/
│   ├── test_retrieval.py    # EXISTING: Retrieval tests
│   └── test_agent.py        # NEW: Agent unit tests
├── integration/
│   └── test_api.py          # NEW: API contract tests
└── contract/
    └── test_ask_endpoint.py # NEW: /ask endpoint tests
```

**Structure Decision**: Backend-only structure extending existing `backend/` directory. No frontend required for this feature.

## Architecture Overview

### Agent Flow Diagram

```
┌─────────────────────────────────────────────────────────────────────┐
│                         FastAPI Server                               │
│  ┌─────────────────────────────────────────────────────────────┐   │
│  │  POST /ask                                                    │   │
│  │  ┌──────────────────────────────────────────────────────────┐│   │
│  │  │ 1. Validate AskRequest (query non-empty, <= 1000 chars) ││   │
│  │  └────────────────────────┬─────────────────────────────────┘│   │
│  │                           │                                   │   │
│  │  ┌────────────────────────▼─────────────────────────────────┐│   │
│  │  │ 2. Generate query embedding via Cohere (embed_query)     ││   │
│  │  └────────────────────────┬─────────────────────────────────┘│   │
│  │                           │                                   │   │
│  │  ┌────────────────────────▼─────────────────────────────────┐│   │
│  │  │ 3. Search Qdrant for top-K chunks (search_qdrant)        ││   │
│  │  └────────────────────────┬─────────────────────────────────┘│   │
│  │                           │                                   │   │
│  │  ┌────────────────────────▼─────────────────────────────────┐│   │
│  │  │ 4. Assemble context from retrieved chunks                ││   │
│  │  └────────────────────────┬─────────────────────────────────┘│   │
│  │                           │                                   │
│  │  ┌────────────────────────▼─────────────────────────────────┐│   │
│  │  │ 5. Generate answer via OpenAI Agent (with context)       ││   │
│  │  └────────────────────────┬─────────────────────────────────┘│   │
│  │                           │                                   │   │
│  │  ┌────────────────────────▼─────────────────────────────────┐│   │
│  │  │ 6. Return AskResponse (answer, sources, matched_chunks)  ││   │
│  │  └──────────────────────────────────────────────────────────┘│   │
│  └─────────────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────────┘
```

### Error Flow

```
Error at Step 1 → 400 Bad Request (INVALID_INPUT)
Error at Step 2 → 500 Internal Error (SERVICE_UNAVAILABLE - Cohere)
Error at Step 3 → 500 Internal Error (SERVICE_UNAVAILABLE - Qdrant)
Empty at Step 3 → 200 OK with graceful "no results" message
Error at Step 5 → 500 Internal Error (SERVICE_UNAVAILABLE - OpenAI)
```

## Key Design Decisions

| Decision | Rationale | Reference |
|----------|-----------|-----------|
| Reuse existing Cohere/Qdrant pipeline | Avoids duplication, tested code | research.md |
| Single `/ask` POST endpoint | RESTful design, action-based | contracts/openapi.yaml |
| OpenAI gpt-4o-mini model | Cost-effective, fast, sufficient quality | research.md |
| Environment-based configuration | 12-factor app, secure credentials | quickstart.md |
| Deterministic retrieval-before-generation | Ensures grounded responses | research.md |

## Dependencies to Install

```bash
pip install fastapi uvicorn openai httpx pytest-asyncio
```

Note: `cohere`, `qdrant-client`, `pydantic` already installed from Spec-001/002.

## Environment Variables

| Variable | Required | Default | Description |
|----------|----------|---------|-------------|
| `COHERE_API_KEY` | Yes | - | Cohere embedding API key |
| `QDRANT_URL` | No | `http://localhost:6333` | Qdrant server URL |
| `QDRANT_API_KEY` | No | - | Qdrant authentication |
| `OPENAI_API_KEY` | Yes | - | OpenAI API key (NEW) |
| `OPENAI_MODEL` | No | `gpt-4o-mini` | Model for generation |
| `DEFAULT_TOP_K` | No | `5` | Default retrieval count |

## Testing Strategy

### Test Categories

| Category | Focus | Files |
|----------|-------|-------|
| Unit | Agent generation, context assembly | `tests/unit/test_agent.py` |
| Integration | Full pipeline with mocked services | `tests/integration/test_api.py` |
| Contract | API schema validation | `tests/contract/test_ask_endpoint.py` |

### Test Scenarios

1. **Happy path**: Valid query → retrieval → generation → response
2. **Empty query**: Missing/empty query → 400 error
3. **No results**: Valid query, no matches → graceful message
4. **Service failures**: Cohere/Qdrant/OpenAI errors → 500 errors

## Complexity Tracking

> No violations identified. Design follows constitution principles.

## Related Documents

- [Feature Specification](./spec.md)
- [Research Decisions](./research.md)
- [Data Model](./data-model.md)
- [API Contract](./contracts/openapi.yaml)
- [Quickstart Guide](./quickstart.md)

## Next Steps

Run `/sp.tasks` to generate the implementation task list based on this plan.
