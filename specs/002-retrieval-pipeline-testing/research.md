# Research: Retrieval Pipeline Testing

**Feature**: 002-retrieval-pipeline-testing
**Date**: 2025-12-22
**Status**: Complete

## Technical Context Analysis

Based on analysis of the existing embedding pipeline (spec-001) and user requirements:

### Existing Infrastructure

| Component | Implementation | Notes |
|-----------|---------------|-------|
| Vector DB | Qdrant (cloud/local) | Collection: `rag_embeddings` |
| Embedding Model | Cohere `multilingual-22-12` | 768-dimensional vectors |
| Storage Format | PointStruct with payload | Includes text_content, source_url, chunk_index |
| Language | Python 3.11 | Single main.py approach |
| Package Manager | uv | With qdrant-client, cohere |

### Research Items Resolved

#### 1. Qdrant Search API Pattern

**Decision**: Use `qdrant_client.search()` with cosine similarity

**Rationale**:
- Collection already configured with `Distance.COSINE`
- Native support for Top-K via `limit` parameter
- Returns `ScoredPoint` objects with payload and score

**Alternatives Considered**:
- `query_points()` - newer API but less mature
- `scroll()` - for pagination, not similarity search

**Best Practice**:
```python
results = qdrant_client.search(
    collection_name="rag_embeddings",
    query_vector=query_embedding,
    limit=k,
    with_payload=True
)
```

#### 2. Query Embedding Approach

**Decision**: Use same Cohere model with `input_type="search_query"`

**Rationale**:
- Must match model used for document embeddings (`multilingual-22-12`)
- Cohere recommends different input_type for queries vs documents
- Existing `embed()` function uses `input_type="search_document"`

**Implementation**:
```python
def embed_query(query: str) -> List[float]:
    response = co.embed(
        texts=[query],
        model='multilingual-22-12',
        input_type="search_query"  # Different from document embedding
    )
    return response.embeddings[0]
```

#### 3. Payload Field Mapping

**Decision**: Map existing payload fields to output schema

**Existing Payload Structure** (from main.py:397-404):
```python
{
    'text_content': text,      # → chunk_text
    'source_url': url,         # → url
    'chunk_index': idx,        # Part of chunk_id generation
    'page_title': title,
    'created_at': timestamp,
    'metadata': {...}
}
```

**Mapping for Retrieval Output**:
| Stored Field | Output Field | Notes |
|--------------|--------------|-------|
| text_content | chunk_text | Exact text content |
| source_url | url | Source URL |
| point.id + chunk_index | chunk_id | Unique identifier |
| score | relevance_score | From search result |

#### 4. JSON Output Schema

**Decision**: Structured JSON with query info, results array, metadata

**Rationale**:
- Consistent with REST API conventions
- Machine-parseable for automated testing
- Includes all required fields from spec

**Schema**:
```json
{
    "query": "string",
    "k": 5,
    "results": [
        {
            "chunk_text": "string",
            "url": "string",
            "chunk_id": "string",
            "relevance_score": 0.95
        }
    ],
    "total_results": 5,
    "timestamp": "ISO-8601"
}
```

#### 5. Error Handling Strategy

**Decision**: Return structured error responses, never crash

| Error Type | Response | HTTP-like Code |
|------------|----------|----------------|
| Empty query | `{"error": "Query cannot be empty", "code": "INVALID_INPUT"}` | 400 |
| No matches | `{"query": "...", "results": [], "total_results": 0}` | 200 |
| Qdrant failure | `{"error": "Database connection failed", "code": "SERVICE_UNAVAILABLE"}` | 503 |
| Cohere failure | `{"error": "Embedding service failed", "code": "SERVICE_UNAVAILABLE"}` | 503 |

#### 6. Testing Strategy

**Decision**: Separate test functions with known fixtures

**Test Categories**:
1. **Unit Tests**: Function-level validation
   - `test_embed_query()` - validates query embedding
   - `test_format_results()` - JSON structure validation

2. **Integration Tests**: End-to-end with Qdrant
   - `test_happy_path_retrieval()` - full pipeline
   - `test_known_query_retrieval()` - expected chunk verification
   - `test_empty_results()` - no matches scenario

3. **Validation Tests**: Data integrity
   - `test_chunk_text_integrity()` - exact text match
   - `test_metadata_accuracy()` - url/chunk_id verification

## Dependencies Confirmed

| Package | Version | Purpose |
|---------|---------|---------|
| qdrant-client | existing | Vector database client |
| cohere | existing | Embedding generation |
| python-dotenv | existing | Environment variables |
| pytest | to add | Testing framework |

## Architecture Decisions

### Single File Approach
Continue with single main.py as per spec-001 pattern. Add retrieval functions to existing file.

### Function Additions to main.py
1. `embed_query(query: str) -> List[float]` - Generate query embedding
2. `search_qdrant(query_embedding, k) -> List[ScoredPoint]` - Perform search
3. `format_results(results, query, k) -> Dict` - Format JSON output
4. `retrieve(query: str, k: int = 5) -> Dict` - Main retrieval function (orchestrator)

### Test File Structure
```
tests/
├── unit/
│   └── test_retrieval.py
└── integration/
    └── test_retrieval_pipeline.py
```

## Next Steps

1. Generate data-model.md with entity definitions
2. Generate API contracts for retrieval functions
3. Generate quickstart.md for developer onboarding
4. Update plan.md with complete implementation details
