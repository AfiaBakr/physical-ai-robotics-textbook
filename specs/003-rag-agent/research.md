# Research: RAG Agent with Retrieval Integration

**Feature Branch**: `003-rag-agent`
**Date**: 2025-12-22
**Status**: Complete

## Overview

This document captures research findings and decisions for implementing the RAG Agent feature. The goal is to build a FastAPI endpoint that accepts user queries, retrieves relevant context from Qdrant, and generates grounded responses using OpenAI Agent SDK.

---

## 1. Existing Infrastructure Analysis

### Decision: Reuse Existing Cohere + Qdrant Pipeline
**Rationale**: The codebase already has a fully functional retrieval pipeline in `backend/main.py` with:
- Cohere embedding via `embed_query()` function (768-dimensional vectors)
- Qdrant search via `search_qdrant()` function
- Result formatting via `format_results()` function
- Error handling via `create_error_response()` function

**Alternatives Considered**:
- Implementing new embedding/retrieval from scratch - Rejected: unnecessary duplication
- Using different embedding model - Rejected: would require re-indexing all documents

**Existing Functions to Reuse**:
| Function | Purpose | Location |
|----------|---------|----------|
| `embed_query()` | Generate 768-dim query embedding | `backend/main.py:506-542` |
| `search_qdrant()` | Top-K similarity search | `backend/main.py:545-588` |
| `format_results()` | Standardize search results | `backend/main.py:591-639` |
| `create_error_response()` | Error response formatting | `backend/main.py:642-657` |
| `retrieve()` | Complete retrieval pipeline | `backend/main.py:660-718` |

---

## 2. OpenAI Agent SDK Integration

### Decision: Use OpenAI Agents SDK for Orchestration
**Rationale**: The OpenAI Agents SDK provides:
- Built-in context handling for RAG workflows
- Structured output generation
- Simple integration with retrieved context
- Production-ready error handling

**Alternatives Considered**:
- LangChain - Rejected: heavier dependency, more complexity than needed
- Direct OpenAI API calls - Rejected: requires more boilerplate code
- Anthropic Claude - Rejected: user specifically requested OpenAI SDK

**Implementation Pattern**:
```python
from openai import OpenAI

client = OpenAI()

# Use chat completions with system context
response = client.chat.completions.create(
    model="gpt-4o-mini",  # Cost-effective, fast
    messages=[
        {"role": "system", "content": f"Use the following context to answer: {context}"},
        {"role": "user", "content": query}
    ]
)
```

---

## 3. FastAPI Endpoint Design

### Decision: Single `/ask` POST Endpoint
**Rationale**: Aligns with spec requirements and follows RESTful conventions for action-based operations.

**Alternatives Considered**:
- GET endpoint - Rejected: query bodies in GET are non-standard
- WebSocket endpoint - Rejected: overkill for request/response pattern
- Multiple endpoints (embed, search, generate) - Rejected: leaks implementation details

**Request Schema**:
```json
{
  "query": "string (required, non-empty)"
}
```

**Response Schema (Success)**:
```json
{
  "answer": "Generated response text",
  "sources": ["url1", "url2"],
  "matched_chunks": [
    {
      "chunk_id": "string",
      "text": "chunk content",
      "relevance_score": 0.95
    }
  ]
}
```

**Response Schema (Error)**:
```json
{
  "error": "Error message",
  "code": "ERROR_CODE"
}
```

---

## 4. Error Handling Strategy

### Decision: Three-Tier Error Classification
**Rationale**: Provides clear, actionable feedback to API consumers.

| Error Type | HTTP Status | Error Code | Trigger |
|------------|-------------|------------|---------|
| Client Error | 400 | `INVALID_INPUT` | Missing/empty query |
| No Results | 200 | N/A | Empty retrieval (graceful) |
| Service Error | 500 | `SERVICE_UNAVAILABLE` | Cohere/Qdrant/OpenAI failure |

**Alternatives Considered**:
- 404 for no results - Rejected: resource exists, just no matches
- Different codes for each service - Rejected: implementation detail leak

---

## 5. Configuration Strategy

### Decision: Environment-Based Configuration
**Rationale**: Follows 12-factor app principles, secure credential handling.

**Required Environment Variables**:
| Variable | Purpose | Default |
|----------|---------|---------|
| `COHERE_API_KEY` | Embedding service auth | (required) |
| `QDRANT_URL` | Vector DB connection | `http://localhost:6333` |
| `QDRANT_API_KEY` | Vector DB auth | (optional) |
| `OPENAI_API_KEY` | LLM generation auth | (required) |
| `DEFAULT_TOP_K` | Results to retrieve | `5` |
| `OPENAI_MODEL` | Model for generation | `gpt-4o-mini` |

---

## 6. Agent Flow Design

### Decision: Deterministic Retrieval-Before-Generation
**Rationale**: Ensures answers are always grounded in retrieved context.

**Flow Diagram**:
```
Request → Validate → Embed Query → Search Qdrant → Build Context → OpenAI Generate → Format Response
    ↓         ↓           ↓              ↓              ↓               ↓              ↓
  400 err  400 err    500 err        500 err     (assemble)      500 err        200 OK
```

**Context Assembly Strategy**:
- Concatenate top-K chunks with source attribution
- Include chunk relevance scores for transparency
- Limit total context length to prevent token overflow

---

## 7. Testing Strategy

### Decision: Three Test Categories
**Rationale**: Covers contract validation, integration verification, and failure paths.

| Category | Test Type | Coverage |
|----------|-----------|----------|
| Contract | API schema validation | Request/response structure |
| Integration | End-to-end with mocks | Full pipeline execution |
| Error Paths | Failure simulation | All error scenarios |

**Testing Dependencies**:
- pytest for test framework
- httpx/TestClient for async API testing
- unittest.mock for service mocking

---

## 8. Performance Considerations

### Decision: Response Time Target of 5 Seconds
**Rationale**: Matches SC-001 from spec, accounts for external API latency.

**Latency Breakdown (Estimated)**:
| Step | Expected Latency |
|------|------------------|
| Input Validation | <10ms |
| Cohere Embedding | 200-500ms |
| Qdrant Search | 50-100ms |
| Context Assembly | <10ms |
| OpenAI Generation | 1-3s |
| Response Formatting | <10ms |
| **Total** | **1.5-4s typical** |

---

## Summary of Key Decisions

1. **Reuse existing Cohere + Qdrant pipeline** from `backend/main.py`
2. **Use OpenAI Agents SDK** for response generation (gpt-4o-mini)
3. **Single `/ask` POST endpoint** with JSON request/response
4. **Three-tier error classification** (400/200/500)
5. **Environment-based configuration** for all credentials
6. **Deterministic retrieval-before-generation** flow
7. **pytest + httpx** for testing
