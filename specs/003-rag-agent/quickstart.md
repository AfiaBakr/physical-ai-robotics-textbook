# Quickstart: RAG Agent with Retrieval Integration

**Feature Branch**: `003-rag-agent`
**Date**: 2025-12-22

## Prerequisites

Before implementing this feature, ensure:

1. **Qdrant is running** with indexed documents (from Spec-001/002)
2. **Environment variables** are configured
3. **Python 3.11+** is installed

## Environment Setup

Create or update `.env` file:

```bash
# Existing (from Spec-001/002)
COHERE_API_KEY=your_cohere_api_key
QDRANT_URL=http://localhost:6333
QDRANT_API_KEY=your_qdrant_api_key  # optional for local

# New for this feature
OPENAI_API_KEY=your_openai_api_key
OPENAI_MODEL=gpt-4o-mini  # optional, default: gpt-4o-mini
DEFAULT_TOP_K=5  # optional, default: 5
```

## Quick Implementation Guide

### Step 1: Install New Dependencies

```bash
pip install fastapi uvicorn openai
```

### Step 2: Create FastAPI Application

The `/ask` endpoint will be added to the existing `backend/` structure:

```
backend/
├── main.py           # Existing embedding/retrieval functions
├── api.py            # NEW: FastAPI application
├── agent.py          # NEW: OpenAI agent wrapper
└── models.py         # NEW: Pydantic models
```

### Step 3: Run the Server

```bash
cd backend
uvicorn api:app --reload --port 8000
```

### Step 4: Test the Endpoint

```bash
curl -X POST http://localhost:8000/ask \
  -H "Content-Type: application/json" \
  -d '{"query": "What is machine learning?"}'
```

Expected response:
```json
{
  "answer": "Machine learning is...",
  "sources": ["https://..."],
  "matched_chunks": [...]
}
```

## Key Integration Points

### Reusing Existing Functions

```python
# From backend/main.py
from main import retrieve, embed_query, search_qdrant
```

### Agent Flow

```python
# Pseudocode for /ask endpoint
def ask(query: str) -> AskResponse:
    # 1. Validate input
    if not query.strip():
        raise HTTPException(400, "Query cannot be empty")

    # 2. Retrieve context (reuses existing pipeline)
    retrieval_result = retrieve(query, k=5)

    # 3. Build context for LLM
    context = build_context(retrieval_result)

    # 4. Generate response via OpenAI
    answer = generate_answer(query, context)

    # 5. Return formatted response
    return AskResponse(
        answer=answer,
        sources=extract_sources(retrieval_result),
        matched_chunks=format_chunks(retrieval_result)
    )
```

## Testing Checklist

- [ ] Server starts without errors
- [ ] `/ask` returns 200 with valid query
- [ ] `/ask` returns 400 with empty query
- [ ] `/ask` returns 400 with missing query field
- [ ] Response contains `answer`, `sources`, `matched_chunks`
- [ ] Empty retrieval returns graceful message

## Common Issues

| Issue | Solution |
|-------|----------|
| `OPENAI_API_KEY not set` | Add to `.env` file |
| `Qdrant connection refused` | Ensure Qdrant is running |
| `No results found` | Verify documents are indexed |
| `Timeout errors` | Check API rate limits |

## Next Steps

After quickstart validation:
1. Run `/sp.tasks` to generate implementation tasks
2. Follow TDD: write tests first, then implement
3. Document any deviations from this plan
