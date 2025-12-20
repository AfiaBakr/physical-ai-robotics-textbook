"""
Docusaurus Embedding Pipeline
A Python-based documentation content pipeline that extracts text from deployed Docusaurus URLs,
generates vector embeddings using Cohere, and stores them in a Qdrant vector database for RAG-based retrieval.
"""
import os
import requests
import time
import logging
from typing import List, Dict, Any, Optional
from urllib.parse import urljoin, urlparse
from bs4 import BeautifulSoup
from cohere import Client as CohereClient
from qdrant_client import QdrantClient
from qdrant_client.http import models
from qdrant_client.http.models import Distance, VectorParams
import re
import xml.etree.ElementTree as ET
from datetime import datetime
import hashlib
import backoff
from dotenv import load_dotenv


# Load environment variables from .env file
load_dotenv()

# Initialize clients
COHERE_API_KEY = os.getenv("COHERE_API_KEY")
QDRANT_URL = os.getenv("QDRANT_URL", "http://localhost:6333")
QDRANT_API_KEY = os.getenv("QDRANT_API_KEY")

co = CohereClient(api_key=COHERE_API_KEY)
qdrant_client = QdrantClient(
    url=QDRANT_URL,
    api_key=QDRANT_API_KEY,
    timeout=60
)


# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def is_valid_url(url: str) -> bool:
    """
    Validates if a URL is properly formatted.

    Args:
        url (str): The URL to validate

    Returns:
        bool: True if the URL is valid, False otherwise
    """
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except Exception:
        return False


@backoff.on_exception(backoff.expo, requests.RequestException, max_tries=3)
def make_request_with_retry(url: str, headers: Optional[Dict] = None) -> requests.Response:
    """
    Makes an HTTP request with retry mechanism.

    Args:
        url (str): The URL to request
        headers (Optional[Dict]): Optional headers to include in the request

    Returns:
        requests.Response: The response object

    Raises:
        requests.RequestException: If all retry attempts fail
    """
    if headers is None:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }

    response = requests.get(url, headers=headers, timeout=30)
    response.raise_for_status()
    return response


@backoff.on_exception(backoff.expo, Exception, max_tries=3)
def make_cohere_request(texts: List[str]) -> List[List[float]]:
    """
    Makes a request to Cohere API with retry mechanism.

    Args:
        texts (List[str]): List of texts to embed

    Returns:
        List[List[float]]: Embeddings for the texts

    Raises:
        Exception: If all retry attempts fail
    """
    response = co.embed(
        texts=texts,
        model='multilingual-22-12',  # Using a stable model
        input_type="search_document"
    )
    return [embedding for embedding in response.embeddings]


def get_all_urls(base_url: str) -> List[str]:
    """
    Fetch all accessible URLs from a Docusaurus documentation site.

    Args:
        base_url (str): The base URL of the Docusaurus site to crawl

    Returns:
        List[str]: A list of all discovered URLs on the site

    Raises:
        requests.RequestException: if the base URL is inaccessible
        ValueError: if the base URL is invalid
    """
    if not is_valid_url(base_url):
        raise ValueError(f"Invalid base URL: {base_url}")

    # First try to get URLs from sitemap
    sitemap_url = urljoin(base_url, "sitemap.xml")
    urls = set()

    try:
        response = make_request_with_retry(sitemap_url)
        sitemap_content = response.text
        root = ET.fromstring(sitemap_content)

        # Define the namespace for sitemap parsing
        namespace = {'sitemap': 'http://www.sitemaps.org/schemas/sitemap/0.9'}

        # Handle both sitemap index and regular sitemap
        if root.tag.endswith('sitemapindex'):
            # This is a sitemap index, get individual sitemaps
            for sitemap in root.findall('.//sitemap:loc', namespace):
                sitemap_loc = sitemap.text
                sitemap_response = make_request_with_retry(sitemap_loc)
                sitemap_doc = ET.fromstring(sitemap_response.text)

                for url_elem in sitemap_doc.findall('.//sitemap:loc', namespace):
                    url = url_elem.text
                    if url:
                        # Fix the "hhttps://" typo if present
                        if url.startswith("hhttps://"):
                            url = url.replace("hhttps://", "https://")

                        if url.startswith(base_url):
                            urls.add(url)
        else:
            # This is a regular sitemap
            for url_elem in root.findall('.//sitemap:loc', namespace):
                url = url_elem.text
                if url:
                    # Fix the "hhttps://" typo if present
                    if url.startswith("hhttps://"):
                        url = url.replace("hhttps://", "https://")

                    if url.startswith(base_url):
                        urls.add(url)
    except Exception as e:
        logger.warning(f"Sitemap not available or failed to parse: {sitemap_url}. Error: {e}")
        # Fallback to crawling the site
        urls = set()
        urls.add(base_url)  # Add base URL itself

    # If sitemap is not available or doesn't have all URLs, we can implement crawling here
    # For now, we'll use the sitemap as the primary source
    return list(urls)


def extract_text_from_url(url: str) -> Dict[str, str]:
    """
    Extract clean text content and metadata from a single URL.

    Args:
        url (str): The URL to extract content from

    Returns:
        Dict[str, str]: Contains keys 'text', 'title', and 'url'

    Raises:
        requests.RequestException: if the URL is inaccessible
        ValueError: if no content could be extracted
    """
    if not is_valid_url(url):
        raise ValueError(f"Invalid URL: {url}")

    response = make_request_with_retry(url)
    soup = BeautifulSoup(response.text, 'lxml')

    # Extract title
    title_tag = soup.find('title')
    title = title_tag.get_text().strip() if title_tag else "No Title"

    # Remove script and style elements
    for script in soup(["script", "style", "nav", "header", "footer", "aside"]):
        script.decompose()

    # Try to find main content area (Docusaurus specific selectors)
    main_content = None
    # Common Docusaurus selectors for main content
    selectors = [
        'main',  # Most common
        '.main-wrapper',  # Docusaurus v2
        '.container',  # General container
        '.docItemContainer',  # Docusaurus doc container
        '.markdown',  # Markdown content
        '.theme-doc-markdown',  # Docusaurus theme markdown
        '.article',  # General article
        'article',  # HTML5 article tag
        '.content',  # Generic content
        '.doc-content',  # Documentation content
        '.docs-content'  # Alternative documentation content
    ]

    for selector in selectors:
        main_content = soup.select_one(selector)
        if main_content:
            break

    # If no specific content area found, use the body
    if not main_content:
        main_content = soup.find('body')

    # Extract text from the main content area
    if main_content:
        text = main_content.get_text()
    else:
        text = soup.get_text()

    # Clean up the text
    lines = (line.strip() for line in text.splitlines())
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    text = ' '.join(chunk for chunk in chunks if chunk)

    # Additional cleaning to remove excessive whitespace and special characters
    text = re.sub(r'\s+', ' ', text)  # Replace multiple spaces with single space
    text = re.sub(r'\n\s*\n', '\n\n', text)  # Normalize paragraph breaks

    if not text.strip():
        raise ValueError(f"No content could be extracted from URL: {url}")

    return {
        'text': text,
        'title': title,
        'url': url
    }


def chunk_text(text: str, chunk_size: int = 1000, overlap: int = 100) -> List[str]:
    """
    Split a large text into smaller overlapping chunks.

    Args:
        text (str): The text to chunk
        chunk_size (int): Maximum size of each chunk (default: 1000)
        overlap (int): Number of overlapping characters between chunks (default: 100)

    Returns:
        List[str]: A list of text chunks

    Raises:
        None
    """
    if len(text) <= chunk_size:
        return [text]

    chunks = []
    start = 0

    while start < len(text):
        end = start + chunk_size
        chunk = text[start:end]

        # Adjust for overlap
        start = end - overlap if end < len(text) else end

        chunks.append(chunk)

    return chunks


def embed(texts: List[str]) -> List[List[float]]:
    """
    Generate vector embeddings for a list of text chunks using Cohere.

    Args:
        texts (List[str]): List of text chunks to embed

    Returns:
        List[List[float]]: List of embedding vectors, each represented as a list of floats

    Raises:
        Exception: if Cohere API call fails
        ValueError: if input texts are invalid
    """
    if not texts:
        raise ValueError("Input texts cannot be empty")

    # Validate input texts
    for i, text in enumerate(texts):
        if not isinstance(text, str) or not text.strip():
            raise ValueError(f"Text at index {i} is invalid: {text}")

    # Process in batches to handle rate limits
    embeddings = []
    batch_size = 96  # Cohere's recommended batch size for embeddings

    for i in range(0, len(texts), batch_size):
        batch = texts[i:i + batch_size]
        try:
            batch_embeddings = make_cohere_request(batch)
            embeddings.extend(batch_embeddings)
            logger.info(f"Processed batch {i//batch_size + 1}/{(len(texts)-1)//batch_size + 1}")

            # Add a small delay to respect rate limits
            time.sleep(0.1)
        except Exception as e:
            logger.error(f"Error processing batch {i//batch_size + 1}: {e}")
            raise

    return embeddings


def create_collection(collection_name: str) -> bool:
    """
    Create a new collection in Qdrant for storing embeddings.

    Args:
        collection_name (str): Name of the collection to create

    Returns:
        bool: True if collection was created successfully, False if it already existed

    Raises:
        Exception: if Qdrant connection fails
    """
    try:
        # Check if collection already exists
        collections = qdrant_client.get_collections()
        existing_collection_names = [collection.name for collection in collections.collections]

        if collection_name in existing_collection_names:
            logger.info(f"Collection '{collection_name}' already exists")
            return False

        # Create collection with appropriate vector size (for Cohere embeddings)
        # Cohere's multilingual-22-12 model produces 768-dimensional vectors
        qdrant_client.create_collection(
            collection_name=collection_name,
            vectors_config=VectorParams(size=768, distance=Distance.COSINE)
        )

        logger.info(f"Collection '{collection_name}' created successfully")
        return True
    except Exception as e:
        logger.error(f"Error creating collection '{collection_name}': {e}")
        raise


def save_chunk_to_qdrant(chunk_data: Dict) -> bool:
    """
    Save a text chunk and its embedding to the Qdrant collection.

    Args:
        chunk_data (Dict): Contains 'text', 'embedding', 'url', 'title', and any additional metadata

    Returns:
        bool: True if saved successfully

    Raises:
        Exception: if Qdrant connection fails
    """
    try:
        # Extract required data
        text = chunk_data.get('text', '')
        embedding = chunk_data.get('embedding', [])
        url = chunk_data.get('url', '')
        title = chunk_data.get('title', '')
        metadata = chunk_data.get('metadata', {})

        # Create a unique ID for this chunk
        text_hash = hashlib.md5(text.encode('utf-8')).hexdigest()
        chunk_id = f"{url}_{text_hash}"

        # Prepare payload with metadata
        payload = {
            'text_content': text,
            'source_url': url,
            'page_title': title,
            'chunk_index': chunk_data.get('chunk_index', 0),
            'created_at': int(datetime.now().timestamp()),
            'metadata': metadata
        }

        # Add any additional metadata from the input
        payload.update(metadata)

        # Upsert the point to Qdrant
        qdrant_client.upsert(
            collection_name="rag_embeddings",
            points=[
                models.PointStruct(
                    id=hash(chunk_id) % (10**9),  # Ensure ID is within valid range
                    vector=embedding,
                    payload=payload
                )
            ]
        )

        logger.info(f"Chunk saved to Qdrant: {url}")
        return True
    except Exception as e:
        logger.error(f"Error saving chunk to Qdrant: {e}")
        raise


def main():
    """
    Main function that orchestrates the entire pipeline:
    get_all_urls → extract_text_from_url → chunk_text → embed → create_collection → save_chunk_to_qdrant
    """
    # Configuration
    base_url = os.getenv("DOCS_BASE_URL", "https://physical-ai-robotics-textbook-nine.vercel.app/")
    chunk_size = int(os.getenv("CHUNK_SIZE", "1000"))
    overlap = int(os.getenv("OVERLAP", "100"))
    collection_name = "rag_embeddings"

    logger.info(f"Starting pipeline for: {base_url}")

    try:
        # Step 1: Create collection
        logger.info("Creating Qdrant collection...")
        create_collection(collection_name)

        # Step 2: Get all URLs from the site
        logger.info("Fetching URLs from the site...")
        urls = get_all_urls(base_url)
        logger.info(f"Found {len(urls)} URLs")

        # Process each URL
        for i, url in enumerate(urls):
            logger.info(f"Processing URL {i+1}/{len(urls)}: {url}")

            try:
                # Step 3: Extract text from URL
                content_data = extract_text_from_url(url)
                text = content_data['text']
                title = content_data['title']

                # Step 4: Chunk the text
                text_chunks = chunk_text(text, chunk_size=chunk_size, overlap=overlap)

                # Step 5: Embed the chunks
                if text_chunks:
                    embeddings = embed(text_chunks)

                    # Step 6: Save each chunk with its embedding to Qdrant
                    for idx, (chunk, embedding) in enumerate(zip(text_chunks, embeddings)):
                        chunk_data = {
                            'text': chunk,
                            'embedding': embedding,
                            'url': url,
                            'title': title,
                            'chunk_index': idx,
                            'metadata': {
                                'word_count': len(chunk.split()),
                                'content_type': 'documentation',
                                'processed_at': datetime.now().isoformat()
                            }
                        }
                        save_chunk_to_qdrant(chunk_data)

                logger.info(f"Successfully processed: {url}")
            except Exception as e:
                logger.error(f"Error processing URL {url}: {e}")
                continue  # Continue with next URL even if one fails

        logger.info("Pipeline completed successfully!")
    except Exception as e:
        logger.error(f"Pipeline failed: {e}")
        raise


if __name__ == "__main__":
    main()