# Data Model: RAG Agent with Retrieval Integration

**Feature Branch**: `003-rag-agent`
**Date**: 2025-12-22
**Status**: Complete

## Overview

This document defines the data entities, their attributes, and relationships for the RAG Agent feature.

---

## Entities

### 1. AskRequest

**Description**: Incoming user request to the `/ask` endpoint.

| Attribute | Type | Required | Validation | Description |
|-----------|------|----------|------------|-------------|
| `query` | string | Yes | Non-empty, max 1000 chars | Natural language question |

**Example**:
```json
{
  "query": "What is machine learning?"
}
```

---

### 2. AskResponse

**Description**: Successful response from the `/ask` endpoint.

| Attribute | Type | Required | Description |
|-----------|------|----------|-------------|
| `answer` | string | Yes | Generated response from LLM |
| `sources` | array[string] | Yes | List of source URLs |
| `matched_chunks` | array[MatchedChunk] | Yes | Retrieved context chunks |

**Example**:
```json
{
  "answer": "Machine learning is a subset of artificial intelligence...",
  "sources": [
    "https://docs.example.com/ml-intro",
    "https://docs.example.com/ml-basics"
  ],
  "matched_chunks": [
    {
      "chunk_id": "12345_0",
      "text": "Machine learning involves training algorithms...",
      "relevance_score": 0.95
    }
  ]
}
```

---

### 3. MatchedChunk

**Description**: A single retrieved document chunk with metadata.

| Attribute | Type | Required | Description |
|-----------|------|----------|-------------|
| `chunk_id` | string | Yes | Unique identifier for the chunk |
| `text` | string | Yes | Content of the matched chunk |
| `relevance_score` | float | Yes | Similarity score (0.0 - 1.0) |

---

### 4. ErrorResponse

**Description**: Error response for failed requests.

| Attribute | Type | Required | Description |
|-----------|------|----------|-------------|
| `error` | string | Yes | Human-readable error message |
| `code` | string | Yes | Machine-readable error code |

**Error Codes**:
| Code | HTTP Status | Description |
|------|-------------|-------------|
| `INVALID_INPUT` | 400 | Missing or invalid query |
| `NO_RESULTS` | 200 | Query valid but no matches found |
| `SERVICE_UNAVAILABLE` | 500 | External service failure |
| `INTERNAL_ERROR` | 500 | Unexpected server error |

**Example**:
```json
{
  "error": "Query cannot be empty",
  "code": "INVALID_INPUT"
}
```

---

### 5. RetrievalContext (Internal)

**Description**: Internal data structure for assembling context for LLM.

| Attribute | Type | Description |
|-----------|------|-------------|
| `chunks` | array[MatchedChunk] | Retrieved chunks |
| `total_tokens` | int | Estimated token count |
| `sources` | set[string] | Unique source URLs |

---

## Entity Relationships

```
AskRequest
    │
    ▼
┌─────────────────────────────────────────────────┐
│  RAG Agent Pipeline                              │
│  ┌────────────────────────────────────────────┐ │
│  │ 1. Validate AskRequest                      │ │
│  │ 2. Embed query via Cohere                   │ │
│  │ 3. Search Qdrant → MatchedChunk[]           │ │
│  │ 4. Build RetrievalContext                   │ │
│  │ 5. Generate answer via OpenAI               │ │
│  └────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────┘
    │
    ▼
AskResponse OR ErrorResponse
```

---

## Validation Rules

### AskRequest Validation

| Rule | Validation | Error |
|------|------------|-------|
| Query presence | `query` field must exist | 400 INVALID_INPUT |
| Query non-empty | `query.strip()` must be non-empty | 400 INVALID_INPUT |
| Query length | `len(query) <= 1000` | 400 INVALID_INPUT |

### Response Constraints

| Rule | Constraint |
|------|------------|
| Answer presence | Always present on success |
| Sources presence | Always present (may be empty array) |
| Matched chunks | Always present (may be empty array) |
| Relevance score range | 0.0 <= score <= 1.0 |

---

## State Transitions

This feature is **stateless**. Each request is independent with no session management.

| State | Description |
|-------|-------------|
| Request Received | Incoming POST to `/ask` |
| Validating | Checking query constraints |
| Embedding | Generating query vector |
| Searching | Querying Qdrant |
| Generating | Calling OpenAI LLM |
| Response Sent | Final response returned |

---

## Integration with Existing Data

### Qdrant Collection: `rag_embeddings`

The RAG Agent reads from the existing collection populated by the embedding pipeline.

**Stored Payload Fields**:
| Field | Type | Used By RAG Agent |
|-------|------|-------------------|
| `text_content` | string | Yes - chunk text |
| `source_url` | string | Yes - source URL |
| `page_title` | string | No |
| `chunk_index` | int | Yes - for chunk_id |
| `created_at` | timestamp | No |
| `metadata` | object | No |

---

## No Database Changes Required

This feature is **read-only** against Qdrant. No schema changes, migrations, or new collections needed.
