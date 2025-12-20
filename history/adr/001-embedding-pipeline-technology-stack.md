# Architectural Decision Record: Embedding Pipeline Technology Stack

## Decision

Selected Python 3.11 with Cohere for embeddings and Qdrant for vector storage for the documentation content pipeline, implemented as a single main.py file with specific function requirements.

## Status

Accepted

## Context

The project requires building a documentation content pipeline that:
- Extracts text from deployed Docusaurus URLs
- Generates vector embeddings using an external service
- Stores embeddings in a vector database for RAG-based retrieval
- Must be implemented as a single main.py file with specific functions

## Options Considered

### Embedding Service
1. **Cohere** (Selected)
   - Pros: Good multilingual support, reliable API, competitive pricing
   - Cons: Proprietary service, requires API key

2. **OpenAI**
   - Pros: Well-established, good documentation
   - Cons: Potentially higher cost, less optimized for RAG

3. **Self-hosted models (Sentence Transformers)**
   - Pros: No API dependencies, cost-effective for high volume
   - Cons: Requires more infrastructure, potentially lower quality

### Vector Database
1. **Qdrant** (Selected)
   - Pros: Open-source, self-hostable, good Python client, efficient
   - Cons: Less mature ecosystem than Pinecone

2. **Pinecone**
   - Pros: Mature managed service, good documentation
   - Cons: Proprietary, can be expensive

3. **Weaviate**
   - Pros: Open-source, good features
   - Cons: More complex setup

### Architecture
1. **Single File (main.py)** (Selected per requirement)
   - Pros: Simple deployment, meets user requirement
   - Cons: Less maintainable, violates modularity principles

2. **Modular Approach**
   - Pros: More maintainable, follows best practices
   - Cons: Doesn't meet user's explicit single-file requirement

## Consequences

- The solution will be tightly coupled but simple to deploy
- External service dependencies require proper error handling and rate limiting
- Open-source vector database allows for self-hosting and control
- Single-file architecture may impact maintainability for large features