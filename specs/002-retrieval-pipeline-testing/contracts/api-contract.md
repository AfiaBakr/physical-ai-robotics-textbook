# API Contract: Retrieval Pipeline

**Feature**: 002-retrieval-pipeline-testing
**Date**: 2025-12-22
**Version**: 1.0.0

## Overview

This document defines the function interfaces for the retrieval pipeline. Since this is a script-based implementation (single main.py), these are Python function contracts rather than HTTP API endpoints.

## Function Contracts

### 1. embed_query

Generates a vector embedding for a query string.

```python
def embed_query(query: str) -> List[float]:
    """
    Generate a vector embedding for a search query using Cohere.

    Args:
        query (str): The natural language query string

    Returns:
        List[float]: 768-dimensional embedding vector

    Raises:
        ValueError: If query is empty or exceeds maximum length
        Exception: If Cohere API call fails after retries

    Example:
        >>> embedding = embed_query("What is a digital twin?")
        >>> len(embedding)
        768
    """
```

**Behavioral Contract**:
- Uses `input_type="search_query"` (different from document embedding)
- Uses same model as storage: `multilingual-22-12`
- Includes retry logic with exponential backoff
- Validates query is non-empty before API call

---

### 2. search_qdrant

Performs similarity search in Qdrant collection.

```python
def search_qdrant(
    query_embedding: List[float],
    k: int = 5
) -> List[ScoredPoint]:
    """
    Perform Top-K similarity search in Qdrant.

    Args:
        query_embedding (List[float]): 768-dimensional query vector
        k (int): Number of results to return (default: 5)

    Returns:
        List[ScoredPoint]: Ordered list of scored points with payloads

    Raises:
        ValueError: If k is not positive or embedding dimension mismatch
        Exception: If Qdrant connection fails

    Example:
        >>> results = search_qdrant(embedding, k=3)
        >>> len(results) <= 3
        True
        >>> results[0].score >= results[1].score  # Ordered by score
        True
    """
```

**Behavioral Contract**:
- Collection name: `rag_embeddings` (hardcoded, matches spec-001)
- Always returns with payload (`with_payload=True`)
- Results ordered by score descending
- Returns empty list if no matches (not error)
- May return fewer than k results if collection has fewer points

---

### 3. format_results

Formats search results into standardized JSON structure.

```python
def format_results(
    results: List[ScoredPoint],
    query: str,
    k: int
) -> Dict[str, Any]:
    """
    Format Qdrant search results into standardized JSON response.

    Args:
        results (List[ScoredPoint]): Raw search results from Qdrant
        query (str): Original query string
        k (int): Requested number of results

    Returns:
        Dict[str, Any]: Formatted response matching QueryResponse schema

    Example:
        >>> response = format_results(results, "test query", 5)
        >>> response.keys()
        dict_keys(['query', 'k', 'results', 'total_results', 'timestamp'])
    """
```

**Output Schema**:
```json
{
    "query": "string",
    "k": "integer",
    "results": [
        {
            "chunk_text": "string",
            "url": "string",
            "chunk_id": "string",
            "relevance_score": "float"
        }
    ],
    "total_results": "integer",
    "timestamp": "ISO-8601 string"
}
```

**Field Mapping**:
| Output Field | Source |
|--------------|--------|
| chunk_text | `point.payload['text_content']` |
| url | `point.payload['source_url']` |
| chunk_id | `f"{point.id}_{point.payload['chunk_index']}"` |
| relevance_score | `point.score` |

---

### 4. retrieve

Main orchestrator function for the retrieval pipeline.

```python
def retrieve(query: str, k: int = 5) -> Dict[str, Any]:
    """
    Execute complete retrieval pipeline: embed query, search, format results.

    Args:
        query (str): Natural language query string
        k (int): Number of results to return (default: 5, max: 100)

    Returns:
        Dict[str, Any]: QueryResponse or ErrorResponse

    Example:
        >>> response = retrieve("What is reinforcement learning?", k=3)
        >>> if 'error' not in response:
        ...     print(f"Found {response['total_results']} results")
    """
```

**Success Response**: QueryResponse schema (see above)

**Error Response**:
```json
{
    "error": "string (human-readable message)",
    "code": "string (INVALID_INPUT | SERVICE_UNAVAILABLE | INTERNAL_ERROR)",
    "timestamp": "ISO-8601 string"
}
```

**Error Conditions**:
| Condition | Error Code | Message |
|-----------|------------|---------|
| Empty query | INVALID_INPUT | "Query cannot be empty" |
| Query too long | INVALID_INPUT | "Query exceeds maximum length" |
| Invalid k | INVALID_INPUT | "k must be positive integer between 1 and 100" |
| Cohere failure | SERVICE_UNAVAILABLE | "Embedding service unavailable" |
| Qdrant failure | SERVICE_UNAVAILABLE | "Database service unavailable" |
| Unexpected error | INTERNAL_ERROR | "An unexpected error occurred" |

---

## Test Function Contracts

### 5. test_retrieval (Integration Test Entry Point)

```python
def test_retrieval():
    """
    Run integration tests for the retrieval pipeline.

    Tests:
        1. Happy path - query returns results
        2. Empty query - returns error
        3. No matches - returns empty results (not error)
        4. Known query - returns expected chunk
        5. Metadata accuracy - url and chunk_id correct
        6. Text integrity - chunk_text matches stored
    """
```

---

## Sample Input/Output

### Successful Query

**Input**:
```python
retrieve("What is a digital twin in robotics?", k=3)
```

**Output**:
```json
{
    "query": "What is a digital twin in robotics?",
    "k": 3,
    "results": [
        {
            "chunk_text": "A digital twin is a virtual representation of a physical robot that mirrors its real-world counterpart in real-time...",
            "url": "https://physical-ai-robotics-textbook-nine.vercel.app/docs/digital-twin",
            "chunk_id": "123456789_0",
            "relevance_score": 0.94
        },
        {
            "chunk_text": "Digital twins enable simulation and testing of robot behaviors before deployment...",
            "url": "https://physical-ai-robotics-textbook-nine.vercel.app/docs/digital-twin",
            "chunk_id": "123456789_1",
            "relevance_score": 0.87
        }
    ],
    "total_results": 2,
    "timestamp": "2025-12-22T10:30:00Z"
}
```

### Empty Query Error

**Input**:
```python
retrieve("", k=5)
```

**Output**:
```json
{
    "error": "Query cannot be empty",
    "code": "INVALID_INPUT",
    "timestamp": "2025-12-22T10:30:00Z"
}
```

### No Matches

**Input**:
```python
retrieve("xyzzy frobozz magic word", k=5)
```

**Output**:
```json
{
    "query": "xyzzy frobozz magic word",
    "k": 5,
    "results": [],
    "total_results": 0,
    "timestamp": "2025-12-22T10:30:00Z"
}
```

---

## Versioning

| Version | Date | Changes |
|---------|------|---------|
| 1.0.0 | 2025-12-22 | Initial contract definition |
