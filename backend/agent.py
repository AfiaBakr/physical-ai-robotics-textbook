"""
OpenAI Agent wrapper for RAG response generation.
"""
import os
import logging
from typing import List, Dict, Any, Optional
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize OpenAI client with OpenRouter
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
OPENROUTER_MODEL = os.getenv("OPENROUTER_MODEL", "mistralai/devstral-2512:free")

client: Optional[OpenAI] = None
if OPENROUTER_API_KEY and OPENROUTER_API_KEY != "your_OPENROUTER_API_KEY_here":
    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=OPENROUTER_API_KEY,
    )

# Configure logging
logger = logging.getLogger(__name__)


def build_context(retrieval_results: Dict[str, Any]) -> str:
    """
    Assemble context string from retrieval results for LLM prompt.

    Args:
        retrieval_results: Dict containing 'results' list with chunk_text and url fields

    Returns:
        str: Formatted context string with source attribution
    """
    if not retrieval_results or 'results' not in retrieval_results:
        return ""

    results = retrieval_results.get('results', [])
    if not results:
        return ""

    context_parts = []
    for i, result in enumerate(results, 1):
        chunk_text = result.get('chunk_text', '')
        url = result.get('url', 'Unknown source')
        if chunk_text:
            context_parts.append(f"[Source {i}: {url}]\n{chunk_text}")

    return "\n\n".join(context_parts)


def generate_answer(query: str, context: str, no_results: bool = False) -> str:
    """
    Generate an answer using OpenAI based on the query and retrieved context.

    Args:
        query: The user's natural language question
        context: The assembled context from retrieved documents
        no_results: If True, generate a "no information found" response

    Returns:
        str: The generated answer

    Raises:
        Exception: If OpenAI API call fails
    """
    if client is None:
        raise Exception("OpenAI client not initialized. Check OPENROUTER_API_KEY environment variable.")

    if no_results or not context:
        system_prompt = """You are a helpful assistant. The user asked a question but no relevant
information was found in the knowledge base. Politely inform them that you couldn't find
relevant information to answer their question, and suggest they try rephrasing or asking
about a different topic."""
        user_message = f"User question: {query}\n\nPlease respond that no relevant information was found."
    else:
        system_prompt = """You are a helpful assistant that answers questions based on the provided context.
Always base your answer on the given context. If the context doesn't contain enough information
to fully answer the question, acknowledge what you can answer and note any limitations.
Be concise but thorough."""
        user_message = f"""Context from knowledge base:
{context}

User question: {query}

Please provide a helpful answer based on the context above."""

    response = client.chat.completions.create(
        model=OPENROUTER_MODEL,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_message}
        ],
        temperature=0.7,
        max_tokens=1000
    )

    return response.choices[0].message.content or "Unable to generate response."


def extract_sources(retrieval_results: Dict[str, Any]) -> List[str]:
    """
    Extract unique source URLs from retrieval results.

    Args:
        retrieval_results: Dict containing 'results' list with url fields

    Returns:
        List[str]: List of unique source URLs
    """
    if not retrieval_results or 'results' not in retrieval_results:
        return []

    results = retrieval_results.get('results', [])
    sources = []
    seen = set()

    for result in results:
        url = result.get('url', '')
        if url and url not in seen:
            sources.append(url)
            seen.add(url)

    return sources


def format_matched_chunks(retrieval_results: Dict[str, Any]) -> List[Dict[str, Any]]:
    """
    Format retrieval results into MatchedChunk format.

    Args:
        retrieval_results: Dict containing 'results' list

    Returns:
        List[Dict]: List of matched chunks with chunk_id, text, relevance_score
    """
    if not retrieval_results or 'results' not in retrieval_results:
        return []

    results = retrieval_results.get('results', [])
    matched_chunks = []

    for result in results:
        matched_chunks.append({
            'chunk_id': result.get('chunk_id', ''),
            'text': result.get('chunk_text', ''),
            'relevance_score': result.get('relevance_score', 0.0)
        })

    return matched_chunks
