"""
FastAPI application for RAG Agent API.
"""
import logging
from datetime import datetime
from typing import Union
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from models import AskRequest, AskResponse, MatchedChunk, ErrorResponse
from agent import build_context, generate_answer, extract_sources, format_matched_chunks
from main import retrieve

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Initialize FastAPI app
app = FastAPI(
    title="RAG Agent API",
    description="API for querying a RAG agent that retrieves documents from Qdrant and generates responses using OpenAI.",
    version="1.0.0"
)

# Add CORS middleware for frontend integration
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",  # Docusaurus dev server
        "https://physical-ai-robotics-textbook-nine.vercel.app",  # Production
    ],
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS"],
    allow_headers=["Content-Type"],
)


@app.get("/health")
async def health_check():
    """
    Health check endpoint to verify service status.

    Returns:
        dict: Health status with timestamp
    """
    return {
        "status": "healthy",
        "timestamp": datetime.now().isoformat()
    }


@app.post("/ask", response_model=AskResponse)
async def ask_question(request: AskRequest) -> Union[AskResponse, JSONResponse]:
    """
    Submit a query to the RAG agent and receive an answer with sources.

    Args:
        request: AskRequest containing the user's query

    Returns:
        AskResponse with answer, sources, and matched_chunks

    Raises:
        HTTPException: 400 for invalid input, 500 for service errors
    """
    query = request.query.strip()

    # Log the incoming request
    logger.info(f"Received query: {query[:100]}...")

    # Validate query is not empty after stripping
    if not query:
        logger.warning("Empty query received after stripping whitespace")
        raise HTTPException(
            status_code=400,
            detail={"error": "Query cannot be empty", "code": "INVALID_INPUT"}
        )

    # Validate query length
    if len(query) > 1000:
        logger.warning(f"Query exceeds maximum length: {len(query)} chars")
        raise HTTPException(
            status_code=400,
            detail={"error": "Query exceeds maximum length of 1000 characters", "code": "INVALID_INPUT"}
        )

    try:
        # Step 1: Retrieve relevant context from Qdrant
        logger.info("Retrieving context from Qdrant...")
        retrieval_results = retrieve(query, k=5)

        # Check for retrieval errors
        if 'error' in retrieval_results:
            error_code = retrieval_results.get('code', 'INTERNAL_ERROR')
            if error_code == 'INVALID_INPUT':
                raise HTTPException(
                    status_code=400,
                    detail={"error": retrieval_results['error'], "code": error_code}
                )
            else:
                raise HTTPException(
                    status_code=500,
                    detail={"error": retrieval_results['error'], "code": "SERVICE_UNAVAILABLE"}
                )

        # Step 2: Check if we have results
        results = retrieval_results.get('results', [])
        no_results = len(results) == 0

        if no_results:
            logger.info(f"No results found for query: {query[:50]}...")

        # Step 3: Build context from retrieval results
        context = build_context(retrieval_results)

        # Step 4: Generate answer using OpenAI
        logger.info("Generating answer via OpenAI...")
        answer = generate_answer(query, context, no_results=no_results)

        # Step 5: Extract sources and format chunks
        sources = extract_sources(retrieval_results)
        matched_chunks_data = format_matched_chunks(retrieval_results)

        # Convert to Pydantic models
        matched_chunks = [
            MatchedChunk(
                chunk_id=chunk['chunk_id'],
                text=chunk['text'],
                relevance_score=chunk['relevance_score']
            )
            for chunk in matched_chunks_data
        ]

        logger.info(f"Successfully processed query. Found {len(sources)} sources.")

        return AskResponse(
            answer=answer,
            sources=sources,
            matched_chunks=matched_chunks
        )

    except HTTPException:
        # Re-raise HTTP exceptions
        raise
    except Exception as e:
        error_msg = str(e).lower()
        logger.error(f"Error processing query: {e}")

        # Determine error type based on message
        if 'cohere' in error_msg or 'embed' in error_msg:
            raise HTTPException(
                status_code=500,
                detail={"error": "Embedding service unavailable", "code": "SERVICE_UNAVAILABLE"}
            )
        elif 'qdrant' in error_msg or 'connection' in error_msg:
            raise HTTPException(
                status_code=500,
                detail={"error": "Database service unavailable", "code": "SERVICE_UNAVAILABLE"}
            )
        elif 'openai' in error_msg:
            raise HTTPException(
                status_code=500,
                detail={"error": "Generation service unavailable", "code": "SERVICE_UNAVAILABLE"}
            )
        else:
            raise HTTPException(
                status_code=500,
                detail={"error": "An unexpected error occurred", "code": "INTERNAL_ERROR"}
            )


# Run with: uvicorn api:app --reload --port 8000
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
