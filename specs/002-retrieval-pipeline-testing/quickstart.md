# Quickstart: Retrieval Pipeline Testing

**Feature**: 002-retrieval-pipeline-testing
**Date**: 2025-12-22

## Prerequisites

Before running the retrieval pipeline, ensure:

1. **Spec-001 Complete**: The embedding pipeline has been run and vectors are stored in Qdrant
2. **Environment Variables**: `.env` file configured with API keys
3. **Python 3.11**: Installed with uv package manager

## Environment Setup

### 1. Verify Environment Variables

Ensure your `backend/.env` file contains:

```bash
COHERE_API_KEY=your_cohere_api_key
QDRANT_URL=https://your-qdrant-instance.cloud.qdrant.io
QDRANT_API_KEY=your_qdrant_api_key
```

### 2. Verify Qdrant Collection

The `rag_embeddings` collection should exist with stored vectors:

```bash
cd backend
uv run python -c "
from qdrant_client import QdrantClient
import os
from dotenv import load_dotenv

load_dotenv()
client = QdrantClient(url=os.getenv('QDRANT_URL'), api_key=os.getenv('QDRANT_API_KEY'))
info = client.get_collection('rag_embeddings')
print(f'Collection: rag_embeddings')
print(f'Points count: {info.points_count}')
print(f'Vector size: {info.config.params.vectors.size}')
"
```

Expected output:
```
Collection: rag_embeddings
Points count: [number > 0]
Vector size: 768
```

## Usage

### Basic Retrieval

After implementing the retrieval functions in `main.py`:

```python
from main import retrieve

# Simple query
result = retrieve("What is a digital twin?")
print(result)

# With custom k
result = retrieve("reinforcement learning robots", k=10)
print(f"Found {result['total_results']} results")

# Iterate results
for r in result['results']:
    print(f"Score: {r['relevance_score']:.2f} - {r['url']}")
```

### Error Handling

```python
from main import retrieve

result = retrieve("")  # Empty query
if 'error' in result:
    print(f"Error: {result['error']} ({result['code']})")
```

## Running Tests

### Unit Tests

```bash
cd backend
uv run pytest tests/unit/test_retrieval.py -v
```

### Integration Tests

```bash
cd backend
uv run pytest tests/integration/test_retrieval_pipeline.py -v
```

### All Tests

```bash
cd backend
uv run pytest tests/ -v --tb=short
```

## Verification Checklist

After implementation, verify:

- [ ] Query returns Top-K results ordered by relevance score
- [ ] `chunk_text` matches original stored text exactly
- [ ] `url` matches `source_url` from storage
- [ ] `chunk_id` is unique for each result
- [ ] Empty query returns error response (not exception)
- [ ] No matches returns empty results array (not error)
- [ ] JSON output validates against schema
- [ ] Response time < 2 seconds for standard queries

## Sample Test Query

Use this query to verify the pipeline works with the Physical AI Robotics textbook:

```python
result = retrieve("What are the key components of a robotic system?", k=3)

# Expected: Results about robotic systems from the textbook
assert 'results' in result
assert result['total_results'] >= 0
for r in result['results']:
    assert 'chunk_text' in r
    assert 'url' in r
    assert 'chunk_id' in r
    assert 0 <= r['relevance_score'] <= 1
```

## Troubleshooting

### No Results Returned

1. Verify Qdrant collection has points: `info.points_count > 0`
2. Check query is semantically related to stored content
3. Verify embedding model matches storage model

### Connection Errors

1. Check `QDRANT_URL` is correct
2. Verify `QDRANT_API_KEY` is valid
3. Check network connectivity to Qdrant

### Embedding Errors

1. Verify `COHERE_API_KEY` is valid
2. Check Cohere API rate limits
3. Ensure query is not empty

## Next Steps

1. Run `/sp.tasks` to generate implementation tasks
2. Implement retrieval functions in `main.py`
3. Create test files under `tests/`
4. Run verification checklist
