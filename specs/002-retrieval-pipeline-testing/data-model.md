# Data Model: Retrieval Pipeline Testing

**Feature**: 002-retrieval-pipeline-testing
**Date**: 2025-12-22
**Source**: spec.md Key Entities + research.md

## Entity Definitions

### Query

Represents a user's natural language search input.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| text | string | Yes | The natural language query string |
| k | integer | No | Number of results to return (default: 5) |

**Validation Rules**:
- `text` must be non-empty after trimming whitespace
- `text` maximum length: 10,000 characters (embedding model limit)
- `k` must be positive integer, range: 1-100

### StoredChunk (Existing in Qdrant)

Represents a document chunk stored in the Qdrant collection from spec-001.

| Field | Type | Storage Location | Description |
|-------|------|------------------|-------------|
| id | integer | point.id | Unique point identifier in Qdrant |
| vector | float[768] | point.vector | Cohere embedding vector |
| text_content | string | payload | Original chunk text |
| source_url | string | payload | Source document URL |
| page_title | string | payload | Document page title |
| chunk_index | integer | payload | Index within source document |
| created_at | integer | payload | Unix timestamp of creation |
| metadata | object | payload | Additional metadata |

### RetrievalResult

Represents a single chunk returned from a similarity search.

| Field | Type | Source | Description |
|-------|------|--------|-------------|
| chunk_text | string | payload.text_content | The retrieved chunk content |
| url | string | payload.source_url | Source document URL |
| chunk_id | string | Derived | Unique identifier (format: `{point_id}_{chunk_index}`) |
| relevance_score | float | ScoredPoint.score | Cosine similarity score (0-1) |

**Derivation Rules**:
- `chunk_id = f"{point_id}_{chunk_index}"` for unique identification
- `relevance_score` is normalized to 0-1 range (cosine similarity)

### QueryResponse

Complete JSON response for a retrieval query.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| query | string | Yes | The original query text |
| k | integer | Yes | Requested number of results |
| results | RetrievalResult[] | Yes | Array of retrieval results |
| total_results | integer | Yes | Actual count of results returned |
| timestamp | string | Yes | ISO-8601 timestamp of query |

**Example**:
```json
{
    "query": "What is a digital twin?",
    "k": 5,
    "results": [
        {
            "chunk_text": "A digital twin is a virtual representation...",
            "url": "https://example.com/docs/digital-twin",
            "chunk_id": "123456789_0",
            "relevance_score": 0.92
        }
    ],
    "total_results": 1,
    "timestamp": "2025-12-22T10:30:00Z"
}
```

### ErrorResponse

Structured error response for failed queries.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| error | string | Yes | Human-readable error message |
| code | string | Yes | Machine-readable error code |
| timestamp | string | Yes | ISO-8601 timestamp |

**Error Codes**:
| Code | Description | Trigger |
|------|-------------|---------|
| INVALID_INPUT | Input validation failed | Empty query, invalid k |
| SERVICE_UNAVAILABLE | External service failed | Qdrant/Cohere unavailable |
| INTERNAL_ERROR | Unexpected error | Unhandled exception |

## Entity Relationships

```
Query (input)
    │
    ▼
┌─────────────────┐
│  embed_query()  │ ──── Cohere API
└─────────────────┘
    │
    ▼ (query_embedding)
┌─────────────────┐
│ search_qdrant() │ ──── Qdrant Collection (rag_embeddings)
└─────────────────┘
    │
    ▼ (List[ScoredPoint])
┌─────────────────┐
│format_results() │
└─────────────────┘
    │
    ▼
QueryResponse (output)
    OR
ErrorResponse (on failure)
```

## State Transitions

The retrieval pipeline is stateless. Each query is independent.

```
[Query Received]
      │
      ▼
[Validate Input] ─── Invalid ──► [ErrorResponse: INVALID_INPUT]
      │
      │ Valid
      ▼
[Generate Query Embedding] ─── Cohere Fail ──► [ErrorResponse: SERVICE_UNAVAILABLE]
      │
      │ Success
      ▼
[Search Qdrant] ─── Qdrant Fail ──► [ErrorResponse: SERVICE_UNAVAILABLE]
      │
      │ Success (may be empty)
      ▼
[Format Results]
      │
      ▼
[QueryResponse]
```

## Data Integrity Guarantees

1. **Text Integrity**: `chunk_text` in response MUST exactly match `text_content` stored in Qdrant
2. **URL Integrity**: `url` in response MUST exactly match `source_url` stored in Qdrant
3. **ID Uniqueness**: `chunk_id` MUST be unique across all results
4. **Score Ordering**: Results MUST be ordered by `relevance_score` descending
5. **Count Accuracy**: `total_results` MUST equal `len(results)`
