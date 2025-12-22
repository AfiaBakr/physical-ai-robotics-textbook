"""
Pydantic models for RAG Agent API request/response schemas.
"""
from typing import List
from pydantic import BaseModel, Field


class MatchedChunk(BaseModel):
    """A single retrieved document chunk with metadata."""
    chunk_id: str = Field(..., description="Unique identifier for the chunk")
    text: str = Field(..., description="Content of the matched chunk")
    relevance_score: float = Field(..., ge=0.0, le=1.0, description="Similarity score (0.0 - 1.0)")


class AskRequest(BaseModel):
    """Incoming user request to the /ask endpoint."""
    query: str = Field(..., min_length=1, max_length=1000, description="Natural language question")


class AskResponse(BaseModel):
    """Successful response from the /ask endpoint."""
    answer: str = Field(..., description="Generated response from LLM")
    sources: List[str] = Field(default_factory=list, description="List of source URLs")
    matched_chunks: List[MatchedChunk] = Field(default_factory=list, description="Retrieved context chunks")


class ErrorResponse(BaseModel):
    """Error response for failed requests."""
    error: str = Field(..., description="Human-readable error message")
    code: str = Field(..., description="Machine-readable error code")
